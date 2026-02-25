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
  
  // Fetch update logs
  fetch('/update_logs.json')
    .then(response => response.json())
    .then(data => {
      const currentVersion = data.version;
      const lastSeenVersion = localStorage.getItem('arisEduLastSeenVersion') || '0.0.0';
      
      // Store for manual viewing via dev tools
      window.arisEduLatestUpdate = data.updates[0];
      
      // If version changed, show update modal
      if (currentVersion !== lastSeenVersion) {
        showUpdateModal(data);
        localStorage.setItem('arisEduLastSeenVersion', currentVersion);
      }
    })
    .catch(err => console.error('Failed to load update logs:', err));
  
  function showUpdateModal(data) {
    const latestUpdate = data.updates[0]; // First item is latest
    
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
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 9999;
    `;
    
    // Create modal content
    const modal = document.createElement('div');
    modal.style.cssText = `
      background: var(--card-bg, #ffffff);
      border-radius: 1rem;
      padding: 2rem;
      max-width: 500px;
      max-height: 80vh;
      overflow-y: auto;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
      color: var(--text-color, #0f172a);
    `;
    
    let content = `
      <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
        <span style="font-size: 2rem;">✨</span>
        <h2 style="margin: 0; font-size: 1.5rem; font-weight: 700;">${getTranslation('whatsNew')}</h2>
      </div>
      <p style="margin: 0 0 0.5rem 0; font-size: 0.9rem; color: var(--text-muted, #666);">Version ${latestUpdate.version} • ${latestUpdate.date}</p>
      <h3 style="margin: 1rem 0 0.5rem 0; font-size: 1.1rem; font-weight: 600;">${latestUpdate.title}</h3>
    `;
    
    if (latestUpdate.features && latestUpdate.features.length > 0) {
      content += `
        <div style="margin: 1rem 0;">
          <h4 style="margin: 0.5rem 0; font-weight: 600; font-size: 0.95rem;">${getTranslation('features')}</h4>
          <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
            ${latestUpdate.features.map(f => `<li style="margin: 0.25rem 0;">${f}</li>`).join('')}
          </ul>
        </div>
      `;
    }
    
    if (latestUpdate.improvements && latestUpdate.improvements.length > 0) {
      content += `
        <div style="margin: 1rem 0;">
          <h4 style="margin: 0.5rem 0; font-weight: 600; font-size: 0.95rem;">${getTranslation('improvements')}</h4>
          <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
            ${latestUpdate.improvements.map(i => `<li style="margin: 0.25rem 0;">${i}</li>`).join('')}
          </ul>
        </div>
      `;
    }
    
    if (latestUpdate.bugFixes && latestUpdate.bugFixes.length > 0) {
      content += `
        <div style="margin: 1rem 0;">
          <h4 style="margin: 0.5rem 0; font-weight: 600; font-size: 0.95rem;">${getTranslation('bugFixes')}</h4>
          <ul style="margin: 0.5rem 0; padding-left: 1.5rem;">
            ${latestUpdate.bugFixes.map(b => `<li style="margin: 0.25rem 0;">${b}</li>`).join('')}
          </ul>
        </div>
      `;
    }
    
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
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    // Close button handler
    document.getElementById('close-update-modal').addEventListener('click', function() {
      overlay.remove();
    });
    
    // Close on overlay click
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) {
        overlay.remove();
      }
    });
  }
  
  // Expose function globally to show updates from dev tools
  window.showArisEduUpdate = function() {
    if (window.arisEduLatestUpdate) {
      showUpdateModal({ updates: [window.arisEduLatestUpdate] });
    } else {
      fetch('/update_logs.json')
        .then(response => response.json())
        .then(data => {
          showUpdateModal(data);
        })
        .catch(err => console.error('Failed to load update logs:', err));
    }
  };
})();
