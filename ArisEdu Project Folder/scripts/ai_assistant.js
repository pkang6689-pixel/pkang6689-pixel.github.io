(async function() {
    function _t(key) {
        if (window.arisTranslate) return window.arisTranslate(key);
        if (window.globalTranslations && window.globalTranslations[key]) return window.globalTranslations[key];
        return key;
    }

    // --- AI Assistant Logic (Gemini via Cloud Function) ---
    const SYSTEM_PROMPT = `You are Aris, an AI tutor for ArisEdu. You use the Socratic method exclusively.

CORE RULES:
1. NEVER give direct answers to questions about course content, problems, or exercises.
2. ALWAYS respond with a guiding question or a small hint that leads the student to think.
3. Keep every response under 80 words — concise and focused.
4. Be warm, encouraging, and patient at all times.

HOW TO RESPOND IN EACH SITUATION:
- Student asks "What is X?" → Ask what they already know about X, then build from there.
- Student asks "How do I solve this?" → Ask what the first step or key concept might be.
- Student gives a WRONG answer → Don't say "wrong". Ask "What makes you think that?" or point to the flaw with a question.
- Student gives a CORRECT answer → Confirm briefly, then ask a follow-up to deepen understanding.
- Student says "I don't know" → Give one small hint, then ask a simpler leading question.
- Student says "just tell me the answer" → Firmly but kindly refuse. Give a hint instead.
- Student seems frustrated → Acknowledge it, reassure them, then break the problem into a smaller first step.

NEVER: lecture, give long explanations, list multiple concepts at once, or solve the problem for the student.

Context: The student is currently studying "${document.title}".`;

    const FUNCTION_URL = "https://callaitutor-vc6l2zw6va-df.a.run.app";

    const AI_Markup = `
    <div id="ai-chat-overlay" style="display: none; position: fixed; bottom: 80px; right: 20px; width: 380px; height: 550px; background: white; border-radius: 1rem; box-shadow: 0 4px 20px rgba(0,0,0,0.2); z-index: 9999; flex-direction: column; overflow: hidden; font-family: 'Poppins', sans-serif;">
        <div id="ai-drag-handle" style="background: linear-gradient(135deg, #3b82f6 0%, #10b981 100%); padding: 1rem; color: white; display: flex; justify-content: space-between; align-items: center; cursor: grab; user-select: none;">
            <div style="font-weight: bold; display: flex; align-items: center; gap: 0.5rem;">
                <span>🤖</span> Aris AI Tutor
            </div>
            <button id="ai-minimize" style="background: none; border: none; color: white; cursor: pointer;">✕</button>
        </div>
        <div id="ai-chat-interface" style="display: flex; flex: 1; flex-direction: column; height: 100%;">
            <div id="ai-messages" style="flex: 1; padding: 1rem; overflow-y: auto; background: #f8fafc; display: flex; flex-direction: column; gap: 0.8rem;">
                <div class="ai-message" style="background: #e2e8f0; color: #334155; padding: 0.8rem; border-radius: 0.8rem 0.8rem 0.8rem 0; align-self: flex-start; max-width: 85%;">
                    ${_t("Hello! I'm Aris AI Tutor. Ask me anything about what you're learning!")}
                </div>
            </div>
            <div style="padding: 1rem; border-top: 1px solid #e2e8f0; background: white; display: flex; gap: 0.5rem;">
                <input type="text" id="ai-input" placeholder="${_t('Ask a question...')}" style="flex: 1; padding: 0.6rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; outline: none;">
                <button id="ai-send" style="background: #3b82f6; color: white; border: none; padding: 0.6rem 1rem; border-radius: 0.5rem; cursor: pointer;">➤</button>
            </div>
        </div>
    </div>
    `;

    // Inject CSS for dark mode support
    const style = document.createElement('style');
    style.textContent = `
        body.dark-mode #ai-chat-overlay { background: #1e293b; border: 1px solid #334155; }
        body.dark-mode #ai-messages { background: #0f172a; }
        body.dark-mode .ai-message { background: #334155 !important; color: #e2e8f0 !important; }
        body.dark-mode .user-message { background: #3b82f6 !important; color: white !important; }
        body.dark-mode #ai-input { background: #1e293b; color: white; border-color: #334155; }
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
            // Don't hide the button – tools_panel.js will morph it into a Tools dropdown.
            // Just skip binding AI click and don't create the overlay.
            window._arisAiHidden = true;
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
            document.getElementById('ai-send').addEventListener('click', handleUserMessage);
            document.getElementById('ai-input').addEventListener('keypress', (e) => {
                if (e.key === 'Enter') handleUserMessage();
            });

            // Make the popup draggable via the header bar
            initDrag();
        }
    }

    function initDrag() {
        const overlay = document.getElementById('ai-chat-overlay');
        const handle = document.getElementById('ai-drag-handle');
        let isDragging = false, offsetX = 0, offsetY = 0;

        handle.addEventListener('mousedown', (e) => {
            if (e.target.closest('button')) return; // don't drag when clicking buttons
            isDragging = true;
            const rect = overlay.getBoundingClientRect();
            offsetX = e.clientX - rect.left;
            offsetY = e.clientY - rect.top;
            handle.style.cursor = 'grabbing';
            e.preventDefault();
        });

        handle.addEventListener('touchstart', (e) => {
            if (e.target.closest('button')) return;
            isDragging = true;
            const rect = overlay.getBoundingClientRect();
            const touch = e.touches[0];
            offsetX = touch.clientX - rect.left;
            offsetY = touch.clientY - rect.top;
        }, { passive: true });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            moveOverlay(e.clientX, e.clientY);
        });

        document.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            const touch = e.touches[0];
            moveOverlay(touch.clientX, touch.clientY);
        }, { passive: true });

        function moveOverlay(cx, cy) {
            let newLeft = cx - offsetX;
            let newTop = cy - offsetY;
            // Clamp inside viewport
            const maxLeft = window.innerWidth - overlay.offsetWidth;
            const maxTop = window.innerHeight - overlay.offsetHeight;
            newLeft = Math.max(0, Math.min(newLeft, maxLeft));
            newTop = Math.max(0, Math.min(newTop, maxTop));
            // Switch from bottom/right positioning to top/left
            overlay.style.bottom = 'auto';
            overlay.style.right = 'auto';
            overlay.style.left = newLeft + 'px';
            overlay.style.top = newTop + 'px';
        }

        function stopDrag() {
            if (isDragging) {
                isDragging = false;
                handle.style.cursor = 'grab';
            }
        }
        document.addEventListener('mouseup', stopDrag);
        document.addEventListener('touchend', stopDrag);
    }

    function toggleAI() {
        const overlay = document.getElementById('ai-chat-overlay');
        if (overlay) {
            overlay.style.display = overlay.style.display === 'none' ? 'flex' : 'none';
        }
    }

    async function handleUserMessage() {
        const input = document.getElementById('ai-input');
        const message = input.value.trim();
        if (!message) return;

        addMessage(message, 'user');
        conversationHistory.push({ role: "user", content: message });
        input.value = '';

        const sendBtn = document.getElementById('ai-send');
        sendBtn.disabled = true;
        const typingId = addMessage(_t('Thinking...'), 'ai', true);

        try {
            const response = await fetch(FUNCTION_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ messages: conversationHistory }),
            });

            const typingEl = document.getElementById(typingId);
            if (typingEl) typingEl.remove();

            if (!response.ok) {
                const err = await response.json().catch(() => ({}));
                throw new Error(err.error || `HTTP ${response.status}`);
            }

            const data = await response.json();
            addMessage(data.content, 'ai');
            conversationHistory.push({ role: "assistant", content: data.content });

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
        } finally {
            sendBtn.disabled = false;
            document.getElementById('ai-input').focus();
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
