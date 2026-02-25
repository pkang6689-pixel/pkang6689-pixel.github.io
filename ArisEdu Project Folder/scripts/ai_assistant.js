(async function() {
    // --- AI Assistant Logic (WebLLM - In-Browser AI) ---
    const SYSTEM_PROMPT = `
    You are an AI tutor for ArisEdu. Your goal is to guide students through their lessons using the Socratic method.
    DO NOT give direct answers to problems. Instead, ask guiding questions to help the student find the answer themselves.
    Be encouraging, patient, and concise. Explain concepts simply.
    If the student asks for the answer, firmly but politely refuse and offer a hint instead.
    Context: The student is currently on the page "${document.title}".
    `;

    // Dynamic import for WebLLM
    let webllm;
    let engine;
    
    const AI_Markup = `
    <div id="ai-chat-overlay" style="display: none; position: fixed; bottom: 80px; right: 20px; width: 380px; height: 550px; background: white; border-radius: 1rem; box-shadow: 0 4px 20px rgba(0,0,0,0.2); z-index: 9999; flex-direction: column; overflow: hidden; font-family: 'Poppins', sans-serif;">
        <div style="background: linear-gradient(135deg, #3b82f6 0%, #10b981 100%); padding: 1rem; color: white; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-weight: bold; display: flex; align-items: center; gap: 0.5rem;">
                <span>🤖</span> Aris AI Tutor (Local)
            </div>
            <div style="display:flex; gap:0.5rem;">
                <button id="ai-minimize" style="background: none; border: none; color: white; cursor: pointer;">✕</button>
            </div>
        </div>
        
        <!-- Model Loading Screen -->
        <div id="ai-loading-screen" style="display:flex; flex-direction:column; align-items:center; justify-content:center; padding:2rem; text-align:center; height:100%; gap:1rem; background:#f8fafc;">
            <div style="font-size:3rem;">🧠</div>
            <h3 style="margin:0; color:#334155;">Initialize AI Tutor</h3>
            <p style="font-size:0.9rem; color:#64748b;">This runs entirely in your browser. No API key required.<br>First load may take a minute (~2GB download).</p>
            <div id="ai-progress-container" style="width:100%; display:none;">
                <div style="width:100%; background:#e2e8f0; border-radius:1rem; height:8px; overflow:hidden;">
                    <div id="ai-progress-bar" style="width:0%; height:100%; background:#3b82f6; transition:width 0.2s;"></div>
                </div>
                <p id="ai-progress-text" style="font-size:0.8rem; color:#64748b; margin-top:0.5rem;">Initializing...</p>
            </div>
            <button id="ai-start-engine" style="background:#3b82f6; color:white; padding:0.8rem 1.5rem; border-radius:0.5rem; border:none; font-weight:600; cursor:pointer; box-shadow:0 2px 4px rgba(59,130,246,0.3);">Start AI Engine</button>
        </div>

        <div id="ai-chat-interface" style="display:none; flex: 1; flex-direction: column; height: 100%;">
            <div id="ai-messages" style="flex: 1; padding: 1rem; overflow-y: auto; background: #f8fafc; display: flex; flex-direction: column; gap: 0.8rem;">
                <div class="ai-message" style="background: #e2e8f0; color: #334155; padding: 0.8rem; border-radius: 0.8rem 0.8rem 0.8rem 0; align-self: flex-start; max-width: 85%;">
                    Hello! I'm running locally on your device. I'm ready to help you learn!
                </div>
            </div>
            <div style="padding: 1rem; border-top: 1px solid #e2e8f0; background: white; display: flex; gap: 0.5rem;">
                <input type="text" id="ai-input" placeholder="Ask a question..." style="flex: 1; padding: 0.6rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; outline: none;">
                <button id="ai-send" style="background: #3b82f6; color: white; border: none; padding: 0.6rem 1rem; border-radius: 0.5rem; cursor: pointer;">➤</button>
            </div>
        </div>
    </div>
    `;

    // Inject CSS for dark mode support
    const style = document.createElement('style');
    style.textContent = `
        body.dark-mode #ai-chat-overlay { background: #1e293b; border: 1px solid #334155; }
        body.dark-mode #ai-messages, body.dark-mode #ai-loading-screen { background: #0f172a; }
        body.dark-mode .ai-message { background: #334155 !important; color: #e2e8f0 !important; }
        body.dark-mode .user-message { background: #3b82f6 !important; color: white !important; }
        body.dark-mode #ai-input { background: #1e293b; color: white; border-color: #334155; }
        body.dark-mode #ai-loading-screen h3 { color: #e2e8f0 !important; }
        body.dark-mode #ai-loading-screen p { color: #94a3b8 !important; }
    `;
    document.head.appendChild(style);

    // Context History
    let conversationHistory = [
        { role: "system", content: SYSTEM_PROMPT }
    ];

    // Helper to check if we should hide the AI (Quiz/Test files)
    function shouldHideAI() {
        const path = window.location.pathname.toLowerCase();
        const title = document.title.toLowerCase();
        const exclusions = ['quiz', 'test', 'exam'];
        if (exclusions.some(keyword => path.includes(keyword) || title.includes(keyword))) {
            return true;
        }
        return false;
    }

    function initAI() {
        if (shouldHideAI()) {
            const aiBtn = document.getElementById('ai-assistant-button');
            if (aiBtn) aiBtn.style.display = 'none';
            return;
        }

        const aiBtn = document.getElementById('ai-assistant-button');
        if (aiBtn) {
            aiBtn.textContent = '🤖 AI'; 
            aiBtn.addEventListener('click', toggleAI);
        }

        if (!document.getElementById('ai-chat-overlay')) {
            document.body.insertAdjacentHTML('beforeend', AI_Markup);
            
            document.getElementById('ai-minimize').addEventListener('click', toggleAI);
            document.getElementById('ai-start-engine').addEventListener('click', startEngine);
            document.getElementById('ai-send').addEventListener('click', handleUserMessage);
            document.getElementById('ai-input').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') handleUserMessage();
            });
        }
    }

    function toggleAI() {
        const overlay = document.getElementById('ai-chat-overlay');
        if (overlay) {
            overlay.style.display = overlay.style.display === 'none' ? 'flex' : 'none';
        }
    }

    async function startEngine() {
        const btn = document.getElementById('ai-start-engine');
        const progressContainer = document.getElementById('ai-progress-container');
        const progressBar = document.getElementById('ai-progress-bar');
        const progressText = document.getElementById('ai-progress-text');

        btn.style.display = 'none';
        progressContainer.style.display = 'block';

        try {
            // Import WebLLM only when needed
            if (!webllm) {
                // Use explicit module script tag or dynamic import
                webllm = await import('https://esm.run/@mlc-ai/web-llm');
            }

            // Callback for progress updates
            const initProgressCallback = (report) => {
                const percentage = Math.round(report.progress * 100);
                progressBar.style.width = percentage + '%';
                progressText.textContent = report.text;
            };

            // Using Llama-3-8B-Instruct-q4f32_1-MLC-1k as a balanced choice
            // Or use Phi-3-mini-4k-instruct-q4f16_1-MLC for faster load (approx 2.3GB)
            const selectedModel = "Phi-3-mini-4k-instruct-q4f16_1-MLC";
            
            engine = await webllm.CreateMLCEngine(
                selectedModel,
                { initProgressCallback: initProgressCallback }
            );

            // Engine Ready!
            document.getElementById('ai-loading-screen').style.display = 'none';
            document.getElementById('ai-chat-interface').style.display = 'flex';
            document.getElementById('ai-input').focus();

        } catch (error) {
            console.error(error);
            progressText.textContent = "Error loading engine: " + error.message;
            progressText.style.color = '#ef4444';
            btn.style.display = 'block';
            btn.textContent = 'Retry';
        }
    }

    async function handleUserMessage() {
        const input = document.getElementById('ai-input');
        const message = input.value.trim();
        if (!message) return;

        if (!engine) {
            addMessage("Please start the AI engine first.", 'ai');
            return;
        }

        addMessage(message, 'user');
        conversationHistory.push({ role: "user", content: message });
        input.value = '';

        const typingId = addMessage('Thinking...', 'ai', true);

        try {
            const completion = await engine.chat.completions.create({
                messages: conversationHistory,
                temperature: 0.7,
                max_tokens: 256, // Keep responses short for speed
            });

            const responseText = completion.choices[0].message.content;
            
            const typingEl = document.getElementById(typingId);
            if (typingEl) typingEl.remove();
            
            addMessage(responseText, 'ai');
            conversationHistory.push({ role: "assistant", content: responseText });

            // Manage context window
            if (conversationHistory.length > 10) {
                 conversationHistory = [
                    conversationHistory[0],
                    ...conversationHistory.slice(conversationHistory.length - 9)
                ];
            }

        } catch (error) {
            const typingEl = document.getElementById(typingId);
            if (typingEl) typingEl.remove();
            addMessage(`Error: ${error.message}`, 'ai');
        }
    }

    function addMessage(text, sender, isTyping = false) {
        const container = document.getElementById('ai-messages');
        const msgDiv = document.createElement('div');
        const id = 'msg-' + Date.now();
        msgDiv.id = id;
        msgDiv.className = sender === 'user' ? 'user-message' : 'ai-message';
        
        if (sender === 'user') {
            msgDiv.style.cssText = 'background: #3b82f6; color: white; padding: 0.8rem; border-radius: 0.8rem 0.8rem 0 0.8rem; align-self: flex-end; max-width: 85%;';
        } else {
            msgDiv.style.cssText = 'background: #e2e8f0; color: #334155; padding: 0.8rem; border-radius: 0.8rem 0.8rem 0.8rem 0; align-self: flex-start; max-width: 85%;';
        }
        
        msgDiv.textContent = text;
        container.appendChild(msgDiv);
        container.scrollTop = container.scrollHeight;
        return id;
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAI);
    } else {
        initAI();
    }
})();
