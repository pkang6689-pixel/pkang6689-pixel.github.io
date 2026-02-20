// ============================================
// Developer Tools — restricted to dev account
// ============================================
(function () {
  'use strict';

  var DEV_EMAIL = 'pkang6689@gmail.com';

  function isDev() {
    try {
      var u = JSON.parse(localStorage.getItem('user'));
      return u && u.email && u.email.toLowerCase() === DEV_EMAIL;
    } catch (e) {
      return false;
    }
  }

  // Expose globally so chem.html can guard its own buttons
  window._isDevUser = isDev;

  if (!isDev()) return;

  // ---- Build floating dev panel ----
  var panel = document.createElement('div');
  panel.id = 'dev-tools-panel';
  panel.innerHTML =
    '<div id="dev-tools-header">' +
      '<span>\u2699 Dev Tools</span>' +
      '<button id="dev-tools-toggle" title="Collapse">\u25B2</button>' +
    '</div>' +
    '<div id="dev-tools-body"></div>';

  // Styles
  var style = document.createElement('style');
  style.textContent =
    '#dev-tools-panel {' +
      'position:fixed; bottom:1rem; right:1rem; z-index:10000;' +
      'background:#1e293b; color:#f8fafc; border:2px solid #3b82f6;' +
      'border-radius:0.75rem; font-family:monospace; font-size:0.85rem;' +
      'box-shadow:0 4px 24px rgba(0,0,0,0.4); min-width:200px;' +
      'transition: opacity 0.2s;' +
    '}' +
    '#dev-tools-header {' +
      'display:flex; justify-content:space-between; align-items:center;' +
      'padding:0.5rem 0.75rem; background:#334155; border-radius:0.65rem 0.65rem 0 0;' +
      'cursor:move; user-select:none;' +
    '}' +
    '#dev-tools-header span { font-weight:700; }' +
    '#dev-tools-toggle {' +
      'background:none; border:none; color:#94a3b8; font-size:1rem; cursor:pointer; padding:0 0.25rem;' +
    '}' +
    '#dev-tools-toggle:hover { color:#f8fafc; }' +
    '#dev-tools-body { padding:0.5rem 0.75rem 0.75rem; }' +
    '#dev-tools-body.collapsed { display:none; }' +
    '.dev-btn {' +
      'display:block; width:100%; margin-top:0.4rem; padding:0.45rem 0.75rem;' +
      'background:#3b82f6; color:#fff; border:none; border-radius:0.4rem;' +
      'cursor:pointer; font-size:0.8rem; font-family:monospace; text-align:left;' +
    '}' +
    '.dev-btn:hover { background:#2563eb; }' +
    '.dev-btn.red { background:#ef4444; }' +
    '.dev-btn.red:hover { background:#dc2626; }' +
    '.dev-btn.green { background:#16a34a; }' +
    '.dev-btn.green:hover { background:#15803d; }' +
    '.dev-section-title { font-weight:700; color:#94a3b8; font-size:0.75rem; margin-top:0.75rem; border-bottom:1px solid #475569; padding-bottom:0.2rem; margin-bottom:0.2rem; }';
  document.head.appendChild(style);

  // Toggle collapse
  var collapsed = false;
  panel.querySelector('#dev-tools-toggle').addEventListener('click', function () {
    collapsed = !collapsed;
    panel.querySelector('#dev-tools-body').classList.toggle('collapsed', collapsed);
    this.textContent = collapsed ? '\u25BC' : '\u25B2';
    this.title = collapsed ? 'Expand' : 'Collapse';
  });
  
  // Make draggable
  (function() {
      var header = panel.querySelector('#dev-tools-header');
      var isDragging = false;
      var startX, startY;
      var startLeft, startTop; // We use right/bottom in CSS, but for dragging we might need to compute or simply set fixed positions
      
      header.addEventListener('mousedown', function(e) {
         isDragging = true;
         // convert to clear top/left to avoid fighting bottom/right CSS
         var rect = panel.getBoundingClientRect();
         panel.style.bottom = 'auto';
         panel.style.right = 'auto';
         panel.style.top = rect.top + 'px';
         panel.style.left = rect.left + 'px';
         
         startX = e.clientX;
         startY = e.clientY;
         startLeft = rect.left;
         startTop = rect.top;
      });
      
      document.addEventListener('mousemove', function(e) {
          if(!isDragging) return;
          e.preventDefault();
          var dx = e.clientX - startX;
          var dy = e.clientY - startY;
          panel.style.left = (startLeft + dx) + 'px';
          panel.style.top = (startTop + dy) + 'px';
      });
      
      document.addEventListener('mouseup', function() { isDragging = false; });
  })();

  // Detect page type from URL
  var path = decodeURIComponent(window.location.pathname);
  var body = panel.querySelector('#dev-tools-body');
  
  // --- Global Utils ---
  function addSection(title) {
      var div = document.createElement('div');
      div.className = 'dev-section-title';
      div.textContent = title;
      body.appendChild(div);
  }
  
  function addButton(text, action, cls) {
      var btn = document.createElement('button');
      btn.className = 'dev-btn' + (cls ? ' ' + cls : '');
      btn.textContent = text;
      btn.addEventListener('click', action);
      body.appendChild(btn);
  }
  
  // --- Language Switcher (synced with Preferences.html) ---
  addSection('Language Shortcut');
  var langs = [
      { code: 'english', label: 'English' },
      { code: 'chinese', label: '中文' },
      { code: 'traditional', label: '繁體中文' }
  ];
  
  var langContainer = document.createElement('div');
  langContainer.style.display = 'grid';
  langContainer.style.gridTemplateColumns = '1fr 1fr 1fr';
  langContainer.style.gap = '0.5rem';
  langContainer.style.marginTop = '0.4rem';
  
  langs.forEach(function(l) {
      var btn = document.createElement('button');
      btn.textContent = l.label;
      btn.style.background = '#475569';
      btn.style.border = 'none';
      btn.style.color = '#fff';
      btn.style.borderRadius = '0.25rem';
      btn.style.cursor = 'pointer';
      btn.style.fontSize = '0.75rem';
      btn.style.padding = '0.3rem';
      
      // Highlight current
      var current = localStorage.getItem('arisEduLanguage') || 'english';
      if(current === l.code) {
          btn.style.background = '#3b82f6';
          btn.style.fontWeight = 'bold';
      }
      
      btn.onclick = function() {
          localStorage.setItem('arisEduLanguage', l.code);
          location.reload();
      };
      langContainer.appendChild(btn);
  });
  body.appendChild(langContainer);
  
  // --- Progress Controls ---
  addSection('Progress Controls');
  
  // generic clear current page
  // Determine context
  var contextKeyPrefix = '';
  // Chemistry context
  if (path.indexOf('chem.html') !== -1 || path.indexOf('ChemistryLessons') !== -1) {
      contextKeyPrefix = 'chem_u';
      
      addButton('\u2714 Finish All Chemistry', function() {
        if(!confirm('Complete ALL Chemistry lessons?')) return;
        var allLessons = { '1': 9, '2': 6, '3': 9, '4': 10, '5A': 9, '5B': 6, '6': 8, '7': 9, '8': 10, '9': 9, '10': 11, '11': 7, '12': 6 };
        for (var u in allLessons) {
          for (var l = 1; l <= allLessons[u]; l++) {
            localStorage.setItem('chem_u' + u + '_l' + l + '_started', 'true');
            localStorage.setItem('chem_u' + u + '_l' + l + '_completed', 'true');
          }
        }
        location.reload();
      }, 'green');
      
  } else if (path.indexOf('physics.html') !== -1 || path.indexOf('PhysicsLessons') !== -1) {
      contextKeyPrefix = 'physics_u';
      
      addButton('\u2714 Finish All Physics', function() {
        if(!confirm('Complete ALL Physics lessons?')) return;
        // Mock data for Physics (Units 1-11)
        // assuming standard structure or grab from page if possible.
        // Let's assume 6 lessons per unit for now as safe default based on U11.
         for (var u=1; u<=11; u++) {
            for (var l=1; l<=10; l++) {
                 // blind write
                localStorage.setItem('physics_u' + u + '_l' + l + '_started', 'true');
                localStorage.setItem('physics_u' + u + '_l' + l + '_completed', 'true');
            }
         }
        location.reload();
      }, 'green');
  } else if (path.indexOf('bio.html') !== -1 || path.indexOf('BiologyLessons') !== -1) {
      contextKeyPrefix = 'bio_u';
      
      addButton('\u2714 Finish All Biology', function() {
        if(!confirm('Complete ALL Biology lessons?')) return;
        // Biology units from bio.html (max lesson number per unit including test)
        // Unit 1: 7 lessons + test (l8) = 8
        // Unit 2: 7 lessons + test (l8) = 8
        // Unit 3: 5 lessons + test (l6) = 6
        // Unit 4: 6 lessons + test (l7) = 7
        // Unit 5: 6 lessons + test (l7) = 7
        // Unit 6: 6 lessons + test (l7) = 7
        // Unit 7: 6 lessons + test (l7) = 7
        // Unit 8: 5 lessons + test (l6) = 6
        // Unit 9: 5 lessons + test (l6) = 6
        // Unit 10: 6 lessons + test (l7) = 7
        // Unit 11: 6 lessons + test (l7) = 7
        // Unit 12: 6 lessons + test (l7) = 7
        var allLessons = { '1': 8, '2': 8, '3': 6, '4': 7, '5': 7, '6': 7, '7': 7, '8': 6, '9': 6, '10': 7, '11': 7, '12': 7 };
        for (var u in allLessons) {
          for (var l = 1; l <= allLessons[u]; l++) {
            localStorage.setItem('bio_u' + u + '_l' + l + '_started', 'true');
            localStorage.setItem('bio_u' + u + '_l' + l + '_completed', 'true');
          }
        }
        location.reload();
      }, 'green');
  }

  // Common Clear
  addButton('\u274C Reset Local Progress', function() {
      if(!confirm('Clear progress for the current context?')) return;
      
      // If on a specific lesson page, maybe only clear that unit?
      // Or just clear all keys matching prefix
      if (contextKeyPrefix) {
          var toRemove = [];
          for(var i=0; i<localStorage.length; i++) {
              var k = localStorage.key(i);
              if(k.startsWith(contextKeyPrefix)) toRemove.push(k);
          }
          toRemove.forEach(k => localStorage.removeItem(k));
          alert('Cleared ' + toRemove.length + ' keys.');
          location.reload();
      } else {
          alert('Not in a known course context.');
      }
  }, 'red');

  // --- Quiz page Specific ---
  // Matches both "Lesson 1.1_Quiz" (chemistry, space) and "Lesson7.1_Quiz" (physics, no space)
  var quizMatch = path.match(/Lesson[\s]?(\w+)\.(\d+)_Quiz/);
  
  if (quizMatch) {
    var qUnit = quizMatch[1];
    var qLesson = quizMatch[2];
    var prefix = (path.indexOf('Physics') !== -1) ? 'physics_u' : 'chem_u';

    addSection('Quiz Actions');
    addButton('\u2714 Auto-Pass Quiz', function () {
        // Mark all answers correct
        document.querySelectorAll('.quiz-question').forEach(function (q) {
          var correctInput = q.querySelector('input[value="correct"]');
          if (correctInput) {
            correctInput.checked = true;
            // Try to find generic submit button
            var submitBtn = q.querySelector('button') || q.querySelector('.action-button');
            if (submitBtn && !submitBtn.disabled) submitBtn.click();
          }
        });
        // Also force storage just in case
        localStorage.setItem(prefix + qUnit + '_l' + qLesson + '_completed', 'true');
    }, 'green');
  }

  // --- Unit Test page ---
  var testMatch = path.match(/Unit(\w+)_Test/);
  if (testMatch) {
    addSection('Unit Test Actions');
    var tUnit = testMatch[1];
    var prefix = (path.indexOf('Physics') !== -1) ? 'physics_u' : 'chem_u'; // Physics unit tests?
    
    addButton('\u2714 Pass Unit Test', function () {
        var form = document.getElementById('quiz-form');
        if (form) {
          form.querySelectorAll('.quiz-question').forEach(function (q) {
            var correctInput = q.querySelector('input[value="correct"]');
            if (correctInput) {
              correctInput.checked = true;
              var submitBtn = q.querySelector('button') || q.querySelector('.action-button');
              if (submitBtn && !submitBtn.disabled) submitBtn.click();
            }
          });
        }
    }, 'green');
  }

  // --- Misc ---
  addSection('Time Tracking');
  
  function addTimeMinutes(minutes) {
    var today = new Date().toISOString().slice(0, 10); // YYYY-MM-DD
    var storageKey = 'arisEdu_time_' + today;
    var existing = parseInt(localStorage.getItem(storageKey)) || 0;
    localStorage.setItem(storageKey, existing + minutes);
    alert('Added ' + minutes + ' minutes.\nTotal today: ' + (existing + minutes) + ' minutes.');
  }
  
  var timeContainer = document.createElement('div');
  timeContainer.style.display = 'grid';
  timeContainer.style.gridTemplateColumns = '1fr 1fr 1fr';
  timeContainer.style.gap = '0.5rem';
  timeContainer.style.marginTop = '0.4rem';
  
  var timeAmounts = [
    { label: '+5m', minutes: 5 },
    { label: '+30m', minutes: 30 },
    { label: '+1h', minutes: 60 }
  ];
  
  timeAmounts.forEach(function(t) {
    var btn = document.createElement('button');
    btn.textContent = t.label;
    btn.style.background = '#16a34a';
    btn.style.border = 'none';
    btn.style.color = '#fff';
    btn.style.borderRadius = '0.25rem';
    btn.style.cursor = 'pointer';
    btn.style.fontSize = '0.75rem';
    btn.style.padding = '0.3rem';
    btn.onmouseover = function() { btn.style.background = '#15803d'; };
    btn.onmouseout = function() { btn.style.background = '#16a34a'; };
    btn.onclick = function() { addTimeMinutes(t.minutes); };
    timeContainer.appendChild(btn);
  });
  body.appendChild(timeContainer);
  
  addButton('\u274C Clear Time Data', function() {
    if(!confirm('Clear all time tracking data?')) return;
    var toRemove = [];
    for(var i=0; i<localStorage.length; i++) {
      var k = localStorage.key(i);
      if(k && k.startsWith('arisEdu_time_')) toRemove.push(k);
    }
    toRemove.forEach(k => localStorage.removeItem(k));
    alert('Cleared ' + toRemove.length + ' time entries.');
  }, 'red');
  
  addSection('Debug Stats');
  addButton('\uD83D\uDCCB Show Storage Keys', function () {
      var keys = [];
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && (k.startsWith('chem_u') || k.startsWith('physics_u'))) keys.push(k + ' = ' + localStorage.getItem(k));
      }
      keys.sort();
      alert('Progress Keys (' + keys.length + '):\n\n' + (keys.length ? keys.slice(0,50).join('\n') + (keys.length > 50 ? '\n...and more' : '') : '(none)'));
  });

  // Add panel to DOM after page loads
  function mount() {
    if(!document.getElementById('dev-tools-panel')) {
        document.body.appendChild(panel);
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
