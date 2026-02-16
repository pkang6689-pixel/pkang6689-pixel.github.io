// taskbar.js — Shared taskbar injection + logic for all pages
(function () {
  // Determine page type and back-button behavior from URL
  var path = decodeURIComponent(window.location.pathname);
  var filename = path.split('/').pop();
  var backText = '';
  var backUrl = '';
  var showBack = true;

  // Detect the lesson-folder context from the URL
  var parts = path.split('/');
  var lessonFolder = '';
  for (var i = 0; i < parts.length; i++) {
    if (parts[i].indexOf('Lessons') !== -1) { lessonFolder = parts[i]; break; }
  }

  // Map lesson folders → course pages
  var courseMap = {
    ChemistryLessons: '/ArisEdu Project Folder/chem.html',
    PhysicsLessons:   '/ArisEdu Project Folder/physics.html',
    BiologyLessons:   '/ArisEdu Project Folder/bio.html',
    Algebra1Lessons:  '/ArisEdu Project Folder/algebra1.html',
    Algebra2Lessons:  '/ArisEdu Project Folder/algebra2.html',
    GeometryLessons:  '/ArisEdu Project Folder/geometry.html'
  };

  // --- Chemistry lesson files (underscore suffixes) ---
  if (filename.indexOf('_Practice') !== -1) {
    backText = '\u2190 Back to Summary';
    backUrl = filename.replace('_Practice.html', '_Summary.html');
  } else if (filename.indexOf('_Summary') !== -1) {
    backText = '\u2190 Back to Lesson';
    backUrl = filename.replace('_Summary.html', '_Video.html');
  } else if (filename.indexOf('_Quiz') !== -1) {
    backText = '\u2190 Back to Practice';
    backUrl = filename.replace('_Quiz.html', '_Practice.html');
  }
  // --- Legacy check (space-separated names) ---
  else if (filename.indexOf(' Practice') !== -1) {
    backText = '\u2190 Back to Summary';
    backUrl = filename.replace(' Practice.html', ' Summary.html');
  } else if (filename.indexOf(' Summary') !== -1) {
    backText = '\u2190 Back to Lesson';
    var lessonMatch = filename.match(/Lesson\s(\d+\.\d+)/);
    if (lessonMatch) {
        backUrl = 'Lesson ' + lessonMatch[1] + '_Video.html';
    } else {
        backUrl = filename.replace(' Summary.html', '.html');
    }
  } else if (filename.indexOf(' Quiz') !== -1) {
    backText = '\u2190 Back to Practice';
    backUrl = filename.replace(' Quiz.html', ' Practice.html');
  }
  // --- Physics lesson files (camelCase, no spaces) ---
  else if (/^PhysicsLesson[\d]/.test(filename) && /Summary\.html$/.test(filename)) {
    backText = '\u2190 Back to Lesson';
    backUrl = filename.replace('Summary.html', '.html');
  }
  else if (/^PhysicsLesson[\d]/.test(filename) && !/Summary\.html$/.test(filename)) {
    // Main Physics lesson → back to PhysicsUnit overview
    backText = '\u2190 Back to Unit';
    var unitMatch = filename.match(/PhysicsLesson(\d+)\./);
    if (unitMatch) backUrl = '/ArisEdu Project Folder/PhysicsLessons/PhysicsUnit' + unitMatch[1] + '.html';
    else backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
  }
  // --- PhysicsUnit overview pages ---
  else if (/^PhysicsUnit\d+\.html$/.test(filename)) {
    backText = '\u2190 Back to Physics';
    backUrl = '/ArisEdu Project Folder/physics.html';
  }
  // --- Chemistry/other main lesson files (inside a Unit folder) ---
  else if (lessonFolder && /^Lesson\s/.test(filename)) {
    backText = '\u2190 Back to Course';
    backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
  }
  // --- Course pages (chem.html, physics.html, etc.) —→ back to Courses ---
  else if (/^(chem|physics|bio|algebra1|algebra2|geometry)\.html$/.test(filename)) {
    backText = '\u2190 Back to Courses';
    backUrl = '/ArisEdu Project Folder/Courses.html';
  }
  // --- Top-level pages without a back button ---
  else {
    showBack = false;
  }

  // Only inject HTML if it doesn't already exist
  if (!document.querySelector('nav.taskbar')) {
    var backBtnHtml = showBack
      ? '<button class="taskbar-button" id="back-button">' + backText + '</button>'
      : '';
    var nav = document.createElement('nav');
    nav.className = 'taskbar';
    nav.innerHTML =
      '<div class="taskbar-container">' +
        backBtnHtml +
        '<button class="taskbar-button" id="search-button">\uD83D\uDD0D Search</button>' +
        '<a class="taskbar-button" href="/index.html" id="homepage-button">\uD83C\uDFE0 Homepage</a>' +
        '<a class="taskbar-button" href="/ArisEdu Project Folder/Courses.html" id="course-button">\uD83D\uDCDA Courses</a>' +
        '<button class="taskbar-button" id="ai-assistant-button">\uD83E\uDD16 AI (WIP)</button>' +
        '<button class="taskbar-button" id="settings-button">\u2699\uFE0F Settings</button>' +
        '<a class="taskbar-button" href="/ArisEdu Project Folder/LoginSignup.html" id="login-signup-button">\uD83D\uDD10 Login/Signup</a>' +
      '</div>' +
      '<div aria-hidden="true" class="settings-menu" id="settings-menu">' +
        '<div class="settings-item">' +
          '<label style="display:flex;align-items:center;gap:0.5rem;cursor:pointer;">' +
            '<input checked id="dark-mode-checkbox" type="checkbox"/>' +
            '<span>Dark Mode</span>' +
          '</label>' +
        '</div>' +
        '<a class="settings-item" href="/ArisEdu Project Folder/Preferences.html">Preferences</a>' +
      '</div>';
    document.body.insertBefore(nav, document.body.firstChild);
  }

  // --- AI Assistant ---
  (function() {
    const AI_BUTTON_ID = 'ai-assistant-button';
    const STORAGE_KEY_API_KEY = 'arisEdu_gemini_api_key';

    // State
    let apiKey = localStorage.getItem(STORAGE_KEY_API_KEY) || '';
    let chatHistory = []; // format: { role: 'user'|'model', parts: [{ text: '...' }] }
    let isSettingsOpen = false;
    let isLoading = false;
    let isOpen = false;

    // DOM Elements
    let container = null;
    let chatContainer = null;
    let inputField = null;
    let sendButton = null;
    let settingsPanel = null;
    let msgList = null;

    function init() {
        const aiButton = document.getElementById(AI_BUTTON_ID);
        if (!aiButton) {
            // If button not found, it might be that taskbar hasn't injected it yet.
            // Since this script runs after taskbar injection in the same file, it should be fine.
            // But let's be safe.
            setTimeout(init, 500); 
            return;
        }

        // Override existing click handler by cloning
        // (This removes the 'mock' event listener if any was attached before, 
        // though we are replacing that code block entirely, existing DOM elements might persist if not reloaded)
        const newButton = aiButton.cloneNode(true);
        aiButton.parentNode.replaceChild(newButton, aiButton);
        
        newButton.onclick = (e) => {
            e.preventDefault();
            toggleAssistant();
        };

        // Create UI if not exists
        if (!document.getElementById('ai-assistant-container')) {
            createInterface();
        }
    }

    function createInterface() {
        // Main Container
        container = document.createElement('div');
        container.id = 'ai-assistant-container';
        // Using existing CSS variables for theming
        container.style.cssText = `
            position: fixed;
            bottom: 80px;
            right: 20px;
            width: 350px;
            height: 500px;
            background: var(--card-bg, #ffffff);
            color: var(--text-color, #000);
            border: 1px solid var(--border-color, #ccc);
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            display: none; 
            flex-direction: column;
            z-index: 9999;
            overflow: hidden;
            font-family: inherit;
            transition: all 0.3s ease;
        `;

        // Header
        const header = document.createElement('div');
        header.style.cssText = `
            padding: 10px 15px;
            background: var(--primary-color, #4a90e2);
            color: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: bold;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        `;
        header.innerHTML = `
            <span style="font-size: 1.1em;">AI</span>
            <div style="display: flex; gap: 15px; align-items: center;">
                <button id="ai-settings-btn" style="background:none; border:none; color:white; cursor:pointer; font-size: 1.2em;" title="Settings">⚙️</button>
                <button id="ai-close-btn" style="background:none; border:none; color:white; cursor:pointer; font-size: 1.2em;" title="Close">✕</button>
            </div>
        `;
        container.appendChild(header);

        // Body Wrapper
        const bodyWrapper = document.createElement('div');
        bodyWrapper.style.cssText = `
            position: relative;
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        `;

        // Settings Panel
        settingsPanel = document.createElement('div');
        settingsPanel.id = 'ai-settings-panel';
        settingsPanel.style.cssText = `
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--card-bg, #ffffff);
            padding: 20px;
            box-sizing: border-box;
            display: none;
            flex-direction: column;
            gap: 15px;
            z-index: 10;
        `;
        
        const keyInputVal = apiKey || '';
        settingsPanel.innerHTML = `
            <h3 style="margin: 0; border-bottom: 1px solid var(--border-color, #ccc); padding-bottom: 10px;">Settings</h3>
            <div>
                <label style="display:block; margin-bottom:5px; font-weight: bold; font-size:0.9em;">Google Gemini API Key</label>
                <input type="password" id="ai-api-key-input" placeholder="Enter API Key" style="
                    width: 100%;
                    padding: 10px;
                    border: 1px solid var(--border-color, #ccc);
                    border-radius: 6px;
                    background: var(--input-bg, #fff);
                    color: var(--text-color, #000);
                    box-sizing: border-box;
                " value="${keyInputVal}">
            </div>
            <div style="font-size: 0.85em; color: var(--text-muted, #666); line-height: 1.4;">
                To use the AI assistant, you need a free API key from Google. 
                <br><br>
                <a href="https://aistudio.google.com/app/apikey" target="_blank" style="color: var(--primary-color, #4a90e2); text-decoration: underline;">Get a key here</a>
            </div>
            <div style="margin-top: auto; display: flex; gap: 10px;">
                <button id="ai-save-key-btn" style="
                    flex: 1;
                    padding: 10px;
                    background: var(--primary-color, #4a90e2);
                    color: white;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    font-weight: bold;
                ">Save API Key</button>
            </div>
        `;
        bodyWrapper.appendChild(settingsPanel);

        // Chat Interface
        chatContainer = document.createElement('div');
        chatContainer.style.cssText = `
            flex: 1;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            background: var(--card-bg, #ffffff);
        `;

        // Messages List
        msgList = document.createElement('div');
        msgList.id = 'ai-msg-list';
        msgList.style.cssText = `
            flex: 1;
            overflow-y: auto;
            padding: 15px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        `;
        
        chatContainer.appendChild(msgList);

        // Input Area
        const inputArea = document.createElement('div');
        inputArea.style.cssText = `
            padding: 15px;
            border-top: 1px solid var(--border-color, #eee);
            display: flex;
            gap: 10px;
            background: var(--bg-secondary, rgba(0,0,0,0.02));
            align-items: center;
        `;
        
        inputField = document.createElement('input');
        inputField.type = 'text';
        inputField.placeholder = 'Type your question...';
        inputField.style.cssText = `
            flex: 1;
            padding: 10px 15px;
            border: 1px solid var(--border-color, #ccc);
            border-radius: 20px;
            outline: none;
            background: var(--input-bg, #fff);
            color: var(--text-color, #000);
            font-size: 0.95em;
        `;
        inputField.onkeydown = (e) => {
            if (e.key === 'Enter') sendMessage();
        };

        sendButton = document.createElement('button');
        sendButton.innerHTML = '➤';
        sendButton.style.cssText = `
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: none;
            background: var(--primary-color, #4a90e2);
            color: white;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.2em;
            transition: opacity 0.2s;
        `;
        sendButton.onclick = sendMessage;

        inputArea.appendChild(inputField);
        inputArea.appendChild(sendButton);
        chatContainer.appendChild(inputArea);

        bodyWrapper.appendChild(chatContainer);
        container.appendChild(bodyWrapper);
        document.body.appendChild(container);

        // Setup Event Listeners
        setupListeners();
    }

    function setupListeners() {
        document.getElementById('ai-close-btn').onclick = toggleAssistant;
        
        document.getElementById('ai-settings-btn').onclick = () => {
            isSettingsOpen = !isSettingsOpen;
            settingsPanel.style.display = isSettingsOpen ? 'flex' : 'none';
        };

        document.getElementById('ai-save-key-btn').onclick = () => {
            const keyInput = document.getElementById('ai-api-key-input');
            const newKey = keyInput.value.trim();
            if (newKey) {
                apiKey = newKey;
                localStorage.setItem(STORAGE_KEY_API_KEY, apiKey);
                isSettingsOpen = false;
                settingsPanel.style.display = 'none';
                
                // Provide feedback
                if (chatHistory.length === 0) {
                   msgList.innerHTML = ''; // Clear initial warning
                   appendMessage('model', 'API Key saved! I\'m ready to help.');
                } else {
                   appendMessage('system', 'API Key updated successfully.');
                }
            } else {
                alert('Please enter a valid API key.');
            }
        };
    }

    function toggleAssistant() {
        isOpen = !isOpen;
        if (!container && isOpen) {
             createInterface();
        }
        if (container) {
             container.style.display = isOpen ? 'flex' : 'none';
             if (isOpen) {
                 if (!apiKey) {
                     isSettingsOpen = true;
                     settingsPanel.style.display = 'flex';
                 } else if (msgList.children.length === 0) {
                     appendMessage('model', 'Hello! I am your study assistant. How can I help you today?');
                 }
                 if (inputField) inputField.focus();
             }
        }
    }

    function appendMessage(role, text) {
        if (!msgList) return;
        const msgDiv = document.createElement('div');
        const isUser = role === 'user';
        const isSystem = role === 'system';
        
        // Message Bubble Styles
        const bubbleStyle = isUser 
            ? `
                background: var(--primary-color, #4a90e2);
                color: white;
                align-self: flex-end;
                border-bottom-right-radius: 4px;
            ` 
            : (isSystem ? `
                background: transparent;
                color: var(--text-muted, #777);
                align-self: center;
                text-align: center;
                font-style: italic;
                border: 1px dashed var(--border-color, #ccc);
            ` : `
                background: var(--bg-secondary, #f1f3f4);
                color: var(--text-color, #000);
                align-self: flex-start;
                border-bottom-left-radius: 4px;
                border: 1px solid var(--border-color, transparent);
            `);

        msgDiv.style.cssText = `
            max-width: 85%;
            padding: 10px 14px;
            border-radius: 12px;
            font-size: 0.95em;
            line-height: 1.5;
            word-wrap: break-word;
            margin-bottom: 5px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
            ${bubbleStyle}
        `;

        if (isSystem) {
             msgDiv.innerHTML = text;
        } else {
            msgDiv.innerHTML = formatMarkdown(text);
        }

        msgList.appendChild(msgDiv);
        scrollToBottom();
    }

    function scrollToBottom() {
        if (msgList) msgList.scrollTop = msgList.scrollHeight;
    }

    function formatMarkdown(text) {
        if (!text) return '';
        return text
            .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/g, '<em>$1</em>')
            .replace(/`(.*?)`/g, '<code style="background:rgba(127,127,127,0.2); padding:2px 4px; border-radius:3px; font-family:monospace;">$1</code>')
            .replace(/\n/g, '<br>');
    }

    async function sendMessage() {
        if (!apiKey) {
            isSettingsOpen = true;
            settingsPanel.style.display = 'flex';
            if (document.getElementById('ai-api-key-input')) {
                document.getElementById('ai-api-key-input').focus();
            }
            return;
        }

        const text = inputField.value.trim();
        if (!text || isLoading) return;

        // UI Updates
        inputField.value = '';
        isLoading = true;
        sendButton.disabled = true;
        sendButton.style.opacity = '0.5';
        appendMessage('user', text);

        // Update History
        chatHistory.push({ role: 'user', parts: [{ text: text }] });
        
        // Limit History (Last 10 turns = 20 messages)
        if (chatHistory.length > 20) {
            chatHistory = chatHistory.slice(chatHistory.length - 20);
        }

        // Thinking Indicator
        const thinkingId = 'ai-thinking-' + Date.now();
        const thinkingDiv = document.createElement('div');
        thinkingDiv.id = thinkingId;
        thinkingDiv.textContent = 'Thinking...';
        thinkingDiv.style.cssText = `
            align-self: flex-start;
            color: var(--text-muted, #999);
            font-size: 0.85em;
            margin-left: 10px;
            margin-bottom: 5px;
            font-style: italic;
        `;
        msgList.appendChild(thinkingDiv);
        scrollToBottom();

        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;
            const response = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: chatHistory
                })
            });

            // Remove thinking
            const tDiv = document.getElementById(thinkingId);
            if(tDiv) tDiv.remove();

            if (!response.ok) {
                const errData = await response.json().catch(() => ({}));
                throw new Error(errData.error?.message || response.statusText);
            }

            const data = await response.json();

            if (data.candidates && data.candidates.length > 0 && data.candidates[0].content) {
                const responseText = data.candidates[0].content.parts[0].text;
                appendMessage('model', responseText);
                chatHistory.push({ role: 'model', parts: [{ text: responseText }] });
            } else {
                appendMessage('system', 'Empty response from AI.');
            }

        } catch (error) {
            console.error('AI Error:', error);
            const tDiv = document.getElementById(thinkingId);
            if(tDiv) tDiv.remove();
            
            let errorMsg = 'Error connecting to AI. Please try again.';
            if (error.message.includes('API key') || error.message.includes('403') || error.message.includes('400')) {
                errorMsg = 'Invalid API Key or Bad Request. Please check your settings.';
                isSettingsOpen = true;
                settingsPanel.style.display = 'flex';
            }
            appendMessage('system', errorMsg);
        } finally {
            isLoading = false;
            sendButton.disabled = false;
            sendButton.style.opacity = '1';
            if (inputField) inputField.focus();
            scrollToBottom();
        }
    }

    // Initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        setTimeout(init, 100); // Small delay to ensure button exists
    }

  })();

  // --- Back button ---
  var backBtn = document.getElementById('back-button');
  if (backBtn) {
    backBtn.addEventListener('click', function () {
      window.location.href = backUrl;
    });
  }

  // --- Settings toggle ---
  var settingsBtn = document.getElementById('settings-button');
  if (settingsBtn) {
    settingsBtn.addEventListener('click', function () {
      var menu = document.getElementById('settings-menu');
      if (!menu) return;
      var isHidden = menu.getAttribute('aria-hidden') === 'true';
      menu.setAttribute('aria-hidden', String(!isHidden));
      if (isHidden) {
        menu.style.visibility = 'visible';
        menu.style.opacity = '1';
        menu.style.transform = 'translateY(0)';
      } else {
        menu.style.visibility = 'hidden';
        menu.style.opacity = '0';
        menu.style.transform = 'translateY(-6px)';
      }
    });
  }

  // --- Dark mode sync ---
  var checkbox = document.getElementById('dark-mode-checkbox');
  if (checkbox) {
    var stored = localStorage.getItem('arisEduDarkMode');
    var prefersDark = stored === null ? true : stored === 'true';
    if (prefersDark) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
    checkbox.checked = prefersDark;
    checkbox.addEventListener('change', function (event) {
      var isDark = event.target.checked;
      localStorage.setItem('arisEduDarkMode', String(isDark));
      if (isDark) {
        document.body.classList.add('dark-mode');
      } else {
        document.body.classList.remove('dark-mode');
      }
      if (window.applyArisTheme) { window.applyArisTheme(); }
    });
  }

  // --- Settings menu alignment ---
  (function () {
    var sBtn = document.getElementById('settings-button');
    var sMenu = document.getElementById('settings-menu');
    if (!sBtn || !sMenu) return;
    var wrapper = document.createElement('span');
    wrapper.style.position = 'relative';
    wrapper.style.display = 'inline-flex';
    sBtn.parentElement.insertBefore(wrapper, sBtn);
    wrapper.appendChild(sBtn);
    wrapper.appendChild(sMenu);
    sMenu.style.position = 'absolute';
    sMenu.style.top = '100%';
    sMenu.style.left = '0';
    sMenu.style.right = 'auto';
    sMenu.style.marginTop = '0.35rem';
  })();

  // --- Login / Signup account display ---
  (function () {
    var loginButton = document.getElementById('login-signup-button');
    if (!loginButton) return;
    var storedUser = localStorage.getItem('user');
    if (!storedUser) return;
    var user;
    try { user = JSON.parse(storedUser); } catch (e) { return; }
    var name = user && (user.name || user.email);
    if (!name) return;

    loginButton.textContent = '\uD83D\uDC64 ' + name;
    loginButton.removeAttribute('href');
    loginButton.setAttribute('aria-haspopup', 'true');
    loginButton.setAttribute('aria-expanded', 'false');

    var isDarkMode = document.body.classList.contains('dark-mode');
    var menu = document.createElement('div');
    menu.className = 'account-menu';
    menu.setAttribute('role', 'menu');
    menu.setAttribute('aria-hidden', 'true');
    menu.style.position = 'absolute';
    menu.style.top = '100%';
    menu.style.left = '0';
    menu.style.right = 'auto';
    menu.style.minWidth = '160px';
    menu.style.marginTop = '0.35rem';
    menu.style.background = isDarkMode ? '#0f172a' : 'white';
    menu.style.border = isDarkMode ? '1px solid #1f2937' : '1px solid #e2e8f0';
    menu.style.borderRadius = '0.5rem';
    menu.style.boxShadow = isDarkMode
      ? '0 12px 24px rgba(2, 6, 23, 0.6)'
      : '0 10px 20px rgba(2, 6, 23, 0.15)';
    menu.style.padding = '0.4rem';
    menu.style.display = 'none';
    menu.style.zIndex = '2000';

    var logoutButton = document.createElement('button');
    logoutButton.type = 'button';
    logoutButton.textContent = 'Log out';
    logoutButton.setAttribute('role', 'menuitem');
    logoutButton.style.width = '100%';
    logoutButton.style.background = 'transparent';
    logoutButton.style.border = 'none';
    logoutButton.style.textAlign = 'left';
    logoutButton.style.padding = '0.5rem 0.75rem';
    logoutButton.style.borderRadius = '0.4rem';
    logoutButton.style.cursor = 'pointer';
    logoutButton.style.fontWeight = '600';
    logoutButton.style.color = isDarkMode ? '#e2e8f0' : '#0f172a';

    logoutButton.addEventListener('mouseenter', function () {
      logoutButton.style.background = isDarkMode
        ? 'rgba(148, 163, 184, 0.2)'
        : 'rgba(15, 23, 42, 0.08)';
    });
    logoutButton.addEventListener('mouseleave', function () {
      logoutButton.style.background = 'transparent';
    });

    logoutButton.addEventListener('click', function (event) {
      event.preventDefault();
      localStorage.removeItem('user');
      menu.style.display = 'none';
      loginButton.setAttribute('aria-expanded', 'false');
      window.location.href = '/ArisEdu Project Folder/LoginSignup.html';
    });

    menu.appendChild(logoutButton);

    var parent = loginButton.parentElement;
    if (parent) {
      var wrapper = document.createElement('span');
      wrapper.style.position = 'relative';
      wrapper.style.display = 'inline-flex';
      parent.insertBefore(wrapper, loginButton);
      wrapper.appendChild(loginButton);
      wrapper.appendChild(menu);
    }

    function closeMenu() {
      menu.style.display = 'none';
      loginButton.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-hidden', 'true');
    }

    function toggleMenu(event) {
      event.preventDefault();
      var isOpen = menu.style.display === 'block';
      if (isOpen) {
        closeMenu();
      } else {
        menu.style.display = 'block';
        menu.setAttribute('aria-hidden', 'false');
        loginButton.setAttribute('aria-expanded', 'true');
      }
    }

    loginButton.addEventListener('click', toggleMenu);

    document.addEventListener('click', function (event) {
      if (!menu.contains(event.target) && event.target !== loginButton) {
        closeMenu();
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        closeMenu();
      }
    });
  })();
})();
