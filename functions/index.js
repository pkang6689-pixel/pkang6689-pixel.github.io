const { onRequest } = require("firebase-functions/v2/https");
const { initializeApp } = require("firebase-admin/app");
const { getFirestore, FieldValue } = require("firebase-admin/firestore");
const { GoogleGenAI } = require("@google/genai");

// ai instance created per-request (needs API key from secret env var)

initializeApp();

const DAILY_GLOBAL_LIMIT = 500; // max messages/day across all users (cost cap)
const MAX_MESSAGE_LENGTH = 2000;

exports.callAITutor = onRequest(
  {
    region: "asia-east2",
    cors: true,
    invoker: "public",
    timeoutSeconds: 30,
    memory: "256MiB",
    secrets: ["GEMINI_API_KEY"],
  },
  async (req, res) => {
    if (req.method !== "POST") {
      return res.status(405).json({ error: "Method not allowed" });
    }

    const { messages } = req.body;

    // Validate input
    if (!messages || !Array.isArray(messages) || messages.length === 0) {
      return res.status(400).json({ error: "messages array is required" });
    }

    const validRoles = ["system", "user", "assistant"];
    for (const msg of messages) {
      if (!validRoles.includes(msg.role) || typeof msg.content !== "string") {
        return res.status(400).json({ error: "Invalid message format" });
      }
      if (msg.content.length > MAX_MESSAGE_LENGTH) {
        return res.status(400).json({ error: "Message too long" });
      }
    }

    // Global daily usage cap (prevents runaway costs)
    const db = getFirestore();
    const today = new Date().toISOString().split("T")[0];
    const usageRef = db.collection("_aiUsage").doc(today);

    try {
      await db.runTransaction(async (tx) => {
        const doc = await tx.get(usageRef);
        const current = doc.exists ? (doc.data().count || 0) : 0;
        if (current >= DAILY_GLOBAL_LIMIT) {
          throw new Error("DAILY_LIMIT_REACHED");
        }
        tx.set(
          usageRef,
          { count: current + 1, updatedAt: FieldValue.serverTimestamp() },
          { merge: true }
        );
      });
    } catch (err) {
      if (err.message === "DAILY_LIMIT_REACHED") {
        return res
          .status(429)
          .json({ error: "Daily message limit reached. Please try again tomorrow." });
      }
      console.error("Firestore transaction error:", err);
      return res.status(500).json({ error: "Internal server error" });
    }

    // Call Gemini via consumer API (generativelanguage.googleapis.com)
    const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });
    try {
      const systemMessage = messages.find((m) => m.role === "system");
      const chatMessages = messages.filter((m) => m.role !== "system");

      if (chatMessages.length === 0) {
        return res.status(400).json({ error: "No chat messages provided" });
      }

      const contents = chatMessages.map((m) => ({
        role: m.role === "assistant" ? "model" : "user",
        parts: [{ text: m.content }],
      }));

      const response = await ai.models.generateContent({
        model: "gemini-2.0-flash",
        contents: contents,
        config: {
          maxOutputTokens: 512,
          temperature: 0.7,
          ...(systemMessage?.content && { systemInstruction: systemMessage.content }),
        },
      });

      const responseText = response.candidates[0].content.parts[0].text;
      return res.status(200).json({ content: responseText });
    } catch (err) {
      console.error("Gemini error:", err);
      return res.status(502).json({ error: "AI service error. Please try again." });
    }
  }
);
