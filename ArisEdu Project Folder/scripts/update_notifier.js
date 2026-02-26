// update_notifier.js - Shows update log on first visit after an update (with translations)
(function() {
  'use strict';
  
  // Get current language
  function getCurrentLanguage() {
    return localStorage.getItem('arisEduLanguage') || 'english';
  }
  
  // Translation object
  const updateTranslations = {
    'english': {
      'whatsNew': "What's New",
      'features': '✨ Features',
      'improvements': '⚡ Improvements',
      'bugFixes': '🐛 Bug Fixes',
      'gotIt': 'Got it!'
    },
    'chinese': {
      'whatsNew': '新更新',
      'features': '✨ 功能',
      'improvements': '⚡ 改进',
      'bugFixes': '🐛  错误修复',
      'gotIt': '知道了'
    },
    'traditional': {
      'whatsNew': '新更新',
      'features': '✨ 功能',
      'improvements': '⚡ 改進',
      'bugFixes': '🐛  錯誤修復',
      'gotIt': '知道了'
    }
  };
  
  function getTranslation(key) {
    const lang = getCurrentLanguage();
    const langTranslations = updateTranslations[lang] || updateTranslations['english'];
    return langTranslations[key] || updateTranslations['english'][key];
  }
  
  // Ensure fetch works with relative paths for local file system
  function getLogsPath() {
      // Logic similar to taskbar.js path resolution
      if (window.location.protocol === 'file:') {
          const path = decodeURIComponent(window.location.pathname);
          if (path.includes('ArisEdu Project Folder')) {
             const parts = path.split('ArisEdu Project Folder');
             if (parts.length > 1) {
                 const depth = (parts[1].match(/\//g) || []).length - 1; // Subtract 1 for filename
                 let rel = "../"; // We need to go up out of ArisEdu Project Folder to root
                 for(let i=0; i<depth; i++) rel += "../";
                 return rel + "update_logs.json";
             }
          }
      }
      return "/update_logs.json";
  }

  // Fetch update logs
  fetch(getLogsPath())
    .then(response => response.json())
    .then(data => {
      const currentVersion = data.version;
      const lastSeenVersion = localStorage.getItem('arisEduLastSeenVersion') || '0.0.0';
      
      // Store for manual viewing via dev tools
      window.arisEduLatestUpdate = data.updates[0];
      
      // EXPOSE INTERFACE FOR BELL BUTTON
      window.showArisEduUpdate = function() {
          showUpdateModal(data);
      };
      
      // If version changed, show update modal
      if (currentVersion !== lastSeenVersion) {
        showUpdateModal(data);
        localStorage.setItem('arisEduLastSeenVersion', currentVersion);
      }
  })
  .catch(err => console.error('Failed to load update logs:', err));
  
  // Revised showUpdateModal with Navigation
  function showUpdateModal(data) {
    const updates = data.updates;
    let currentIndex = 0;

    // Create modal overlay
    const overlay = document.createElement('div');
    overlay.id = 'update-modal-overlay';
    overlay.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(5px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
    `;
    
    // Create modal container
    const modal = document.createElement('div');
    modal.className = "update-modal-content"; // For styling
    
    // Inject styles for dark/light mode arrows
    if(!document.getElementById('update-modal-styles')) {
        const s = document.createElement('style');
        s.id = 'update-modal-styles';
        s.innerHTML = `
            .update-nav-btn {
                padding: 0.35rem 0.85rem;
                cursor: pointer;
                border-radius: 0.4rem;
                font-size: 1.1rem;
                transition: all 0.2s ease;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            /* Light Mode Default */
            .update-nav-btn {
                background: #f1f5f9;
                border: 1px solid #cbd5e1;
                color: #334155;
            }
            .update-nav-btn:hover:not(:disabled) {
                background: #e2e8f0;
                color: #0f172a;
                transform: translateY(-1px);
            }
            
            /* Dark Mode */
            body.dark-mode .update-nav-btn {
                background: #1e293b;
                border: 1px solid #334155;
                color: #e2e8f0;
            }
            body.dark-mode .update-nav-btn:hover:not(:disabled) {
                background: #334155;
                color: #fff;
                border-color: #475569;
            }
            
            .update-nav-btn:disabled {
                opacity: 0.4;
                cursor: not-allowed;
                transform: none !important;
            }
        `;
        document.head.appendChild(s);
    }

    modal.style.cssText = `
      background: var(--card-bg, #ffffff);
      border-radius: 1rem;
      padding: 2rem;
      width: 90%;
      max-width: 500px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
      color: var(--text-color, #0f172a);
      position: relative;
    `;

    // Render Function
    function renderCurrentUpdate() {
        const update = updates[currentIndex];
        
        let content = `
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 2rem;">✨</span>
                <h2 style="margin: 0; font-size: 1.5rem; font-weight: 700;">${getTranslation('whatsNew')}</h2>
            </div>
            <div style="display: flex; gap: 0.5rem;">
                <button id="prev-update-btn" class="update-nav-btn" ${currentIndex >= updates.length - 1 ? 'disabled' : ''}>←</button>
                <button id="next-update-btn" class="update-nav-btn" ${currentIndex <= 0 ? 'disabled' : ''}>→</button>
            </div>
          </div>
          
          <div style="flex: 1; overflow-y: auto; padding-right: 0.5rem;">
              <p style="margin: 0 0 0.5rem 0; font-size: 0.9rem; color: var(--text-muted, #666);">Version ${update.version} • ${update.date}</p>
              <h3 style="margin: 1rem 0 0.5rem 0; font-size: 1.1rem; font-weight: 600;">${update.title}</h3>
        `;
        
        if (update.features && update.features.length > 0) {
          content += `
            <div style="margin: 1rem 0;">
              <h4 style="margin: 0.5rem 0; font-weight: 600; font-size: 0.95rem;">${getTranslation('features')}</h4>
              <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                ${update.features.map(f => `<li style="margin: 0.25rem 0;">${f}</li>`).join('')}
              </ul>
            </div>
          `;
        }
        
        if (update.improvements && update.improvements.length > 0) {
          content += `
            <div style="margin: 1rem 0;">
              <h4 style="margin: 0.5rem 0; font-weight: 600; font-size: 0.95rem;">${getTranslation('improvements')}</h4>
              <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                ${update.improvements.map(i => `<li style="margin: 0.25rem 0;">${i}</li>`).join('')}
              </ul>
            </div>
          `;
        }
        
        if (update.bugFixes && update.bugFixes.length > 0) {
          content += `
            <div style="margin: 1rem 0;">
              <h4 style="margin: 0.5rem 0; font-weight: 600; font-size: 0.95rem;">${getTranslation('bugFixes')}</h4>
              <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
                ${update.bugFixes.map(b => `<li style="margin: 0.25rem 0;">${b}</li>`).join('')}
              </ul>
            </div>
          `;
        }
        
        content += `</div>`; // End scrollable area

        content += `
          <button id="close-update-modal" style="
            margin-top: 1.5rem;
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(135deg, #3b82f6 0%, #10b981 50%, #8b5cf6 100%);
            color: white;
            border: none;
            border-radius: 0.5rem;
            font-weight: 600;
            cursor: pointer;
            font-size: 1rem;
          ">${getTranslation('gotIt')}</button>
        `;

        modal.innerHTML = content;
        
        // Re-attach listeners using modal.querySelector since it might not be in DOM yet
        const closeBtn = modal.querySelector('#close-update-modal');
        if(closeBtn) closeBtn.addEventListener('click', () => overlay.remove());
        
        const prevBtn = modal.querySelector('#prev-update-btn');
        const nextBtn = modal.querySelector('#next-update-btn');
        
        if(prevBtn) prevBtn.addEventListener('click', () => {
             if(currentIndex < updates.length - 1) {
                 currentIndex++;
                 renderCurrentUpdate();
             }
        });
        
        if(nextBtn) nextBtn.addEventListener('click', () => {
             if(currentIndex > 0) {
                 currentIndex--;
                 renderCurrentUpdate();
             }
        });
    }

    renderCurrentUpdate();
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    // Close on overlay click
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) {
        overlay.remove();
      }
    });

    // Make content readable in Dark Mode
    if(document.body.classList.contains('dark-mode')) {
        modal.style.background = '#1e293b';
        modal.style.color = '#e2e8f0';
    }
  }
  
  // Expose function globally to show updates from dev tools (forces fetch to get full history)
  // Note: This overrides the initial binding inside the first fetch callback, 
  // but ensures a fresh fetch if valid.
  window.showArisEduUpdate = function() {
      fetch(getLogsPath())
        .then(response => response.json())
        .then(data => {
          showUpdateModal(data);
        })
        .catch(err => console.error('Failed to load update logs:', err));
  };
})();
