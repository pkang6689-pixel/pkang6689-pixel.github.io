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

  // Render Body
  var body = panel.querySelector('#dev-tools-body');
  
  // Section: Badges
  (function() {
      var title = document.createElement('div');
      title.className = 'dev-section-title';
      title.textContent = 'BADGES';
      body.appendChild(title);

      var select = document.createElement('select');
      select.style.cssText = 'width:100%; padding:0.3rem; background:#334155; color:white; border:none; border-radius:0.3rem; margin-bottom:0.3rem;';
      
      // Get badges from window.BadgeSystem if available, else hardcode list for now
      var badgeKeys = [
          'first_visit', 'night_owl', 'early_bird', 'scholar', 
          'dedicated', 'completionist', 'quiz_master', 
          'algebra_master', 'physics_pro', 'chemistry_whiz', 'polyglot',
          'streak_3', 'streak_7', 'streak_30'
      ];
      
      badgeKeys.forEach(function(key) {
          var opt = document.createElement('option');
          opt.value = key;
          opt.textContent = key.replace(/_/g, ' ').toUpperCase();
          select.appendChild(opt);
      });

      var btn = document.createElement('button');
      btn.className = 'dev-btn green';
      btn.textContent = 'Award Selected Badge';
      btn.onclick = function() {
          if (window.BadgeSystem) {
              window.BadgeSystem.award(select.value);
              console.log('Awarded:', select.value);
          } else {
              alert('BadgeSystem not loaded on this page.');
          }
      };

      body.appendChild(select);
      body.appendChild(btn);

      var resetBtn = document.createElement('button');
      resetBtn.className = 'dev-btn red';
      resetBtn.textContent = 'Reset All Badges';
      resetBtn.style.marginTop = '0.5rem';
      resetBtn.onclick = function() {
          localStorage.removeItem('arisEdu_badges');
          alert('Badges reset.');
      };
      body.appendChild(resetBtn);
  })();

  // Section: Navigation logic (existing tools would go here if any)
  
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
  
  // --- Update Log ---
  addSection('Updates');
  addButton('📋 View Latest Update', function() {
      if (typeof window.showArisEduUpdate === 'function') {
          window.showArisEduUpdate();
      } else {
          alert('Update notifier not loaded yet.');
      }
  });
  
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
  } else if (path.indexOf('geometry.html') !== -1 || path.indexOf('GeometryLessons') !== -1) {
      contextKeyPrefix = 'geometry_u';

      addButton('\u2714 Finish All Geometry', function() {
        if(!confirm('Complete ALL Geometry lessons?')) return;
        var allLessons = { '1': 8, '2': 10, '3': 8, '4': 9, '5': 7, '6': 8, '7': 9, '8': 9, '9': 8, '10': 10, '11': 7, '12': 10, '13': 8 };
        for (var u in allLessons) {
          for (var l = 1; l <= allLessons[u]; l++) {
            localStorage.setItem('geometry_u' + u + '_l' + l + '_started', 'true');
            localStorage.setItem('geometry_u' + u + '_l' + l + '_completed', 'true');
          }
        }
        location.reload();
      }, 'green');
  } else if (path.indexOf('algebra1.html') !== -1 || path.indexOf('Algebra1Lessons') !== -1) {
      contextKeyPrefix = 'alg1_u';

      addButton('\u2714 Finish All Algebra 1', function() {
        if(!confirm('Complete ALL Algebra 1 lessons?')) return;
        var allLessons = { '1': 8, '2': 10, '3': 6, '4': 9, '5': 13, '6': 16, '7': 11, '8': 10, '9': 12, '10': 11, '11': 8, '12': 5 };
        for (var u in allLessons) {
          for (var l = 1; l <= allLessons[u]; l++) {
            localStorage.setItem('alg1_u' + u + '_l' + l + '_started', 'true');
            localStorage.setItem('alg1_u' + u + '_l' + l + '_completed', 'true');
          }
        }
        location.reload();
      }, 'green');
  } else if (path.indexOf('algebra2.html') !== -1 || path.indexOf('Algebra2Lessons') !== -1) {
      contextKeyPrefix = 'alg2_u';

      addButton('\u2714 Finish All Algebra 2', function() {
        if(!confirm('Complete ALL Algebra 2 lessons?')) return;
        var allLessons = { '1': 10, '2': 8, '3': 8, '4': 7, '5': 8, '6': 6, '7': 8, '8': 7, '9': 5 };
        for (var u in allLessons) {
          for (var l = 1; l <= allLessons[u]; l++) {
            localStorage.setItem('alg2_u' + u + '_l' + l + '_started', 'true');
            localStorage.setItem('alg2_u' + u + '_l' + l + '_completed', 'true');
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
    var prefix = 'chem_u';
    if (path.indexOf('Physics') !== -1) prefix = 'physics_u';
    else if (path.indexOf('Algebra1') !== -1) prefix = 'alg1_u';
    else if (path.indexOf('Algebra2') !== -1) prefix = 'alg2_u';
    else if (path.indexOf('Geometry') !== -1) prefix = 'geometry_u';
    else if (path.indexOf('Biology') !== -1) prefix = 'bio_u';

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
    var prefix = 'chem_u';
    if (path.indexOf('Physics') !== -1) prefix = 'physics_u';
    else if (path.indexOf('Algebra1') !== -1) prefix = 'alg1_u';
    else if (path.indexOf('Algebra2') !== -1) prefix = 'alg2_u';
    else if (path.indexOf('Geometry') !== -1) prefix = 'geometry_u';
    else if (path.indexOf('Biology') !== -1) prefix = 'bio_u';
    
    addButton('\u2714 Pass Unit Test', function () {
        // First, switch to quiz view if not already visible
        var practiceView = document.getElementById('practice-content-view');
        var quizView = document.getElementById('quiz-content-view');
        if (practiceView) practiceView.style.display = 'none';
        if (quizView) quizView.style.display = 'block';
        if (window.showQuiz) window.showQuiz();
        
        var form = document.getElementById('quiz-form');
        if (form) {
          var questions = Array.from(form.querySelectorAll('.quiz-question'));
          var questionIndex = 0;
          
          function clickNextButton() {
            if (questionIndex < questions.length) {
              var q = questions[questionIndex];
              // Find "Check Answer" button by looking at onclick attribute text
              var checkBtn = null;
              var buttons = q.querySelectorAll('button');
              for (var i = 0; i < buttons.length; i++) {
                var b = buttons[i];
                // Check onclick attribute directly (works for inline onclick="...")
                var onclickAttr = b.getAttribute('onclick') || '';
                if (onclickAttr.indexOf('checkQuizAnswer') !== -1) {
                  checkBtn = b;
                  break;
                }
                // Fallback: check onclick property  
                if (b.onclick && b.onclick.toString().indexOf('checkQuizAnswer') !== -1) {
                  checkBtn = b;
                  break;
                }
              }
              
              if (checkBtn && !checkBtn.disabled) {
                // Extract question name and correct answer from onclick attribute
                var onclickStr = checkBtn.getAttribute('onclick') || '';
                if (!onclickStr && checkBtn.onclick) {
                  onclickStr = checkBtn.onclick.toString();
                }
                var match = onclickStr.match(/checkQuizAnswer\(\s*'([^']*)'\s*,\s*'([^']*)'/);
                if (match) {
                  var questionName = match[1];
                  var correctAnswer = match[2];
                  var correctInput = q.querySelector('input[name="' + questionName + '"][value="' + correctAnswer + '"]');
                  if (correctInput) {
                    correctInput.checked = true;
                    // Call checkQuizAnswer directly via the global function
                    if (window.checkQuizAnswer) {
                      window.checkQuizAnswer(questionName, correctAnswer, checkBtn);
                    }
                    // Ensure dataset.status is set 
                    q.dataset.status = 'correct';
                    // Ensure button is disabled
                    checkBtn.disabled = true;
                  }
                }
              }
              
              questionIndex++;
              setTimeout(clickNextButton, 100);
            } else {
              // All buttons clicked — trigger completion
              setTimeout(function() {
                // Ensure all questions marked correct and buttons disabled
                questions.forEach(function(q) {
                  q.dataset.status = 'correct';
                  var btns = q.querySelectorAll('button');
                  for (var i = 0; i < btns.length; i++) {
                    btns[i].disabled = true;
                  }
                });
                
                if (window.checkQuizCompletion) {
                  window.checkQuizCompletion();
                }
              }, 300);
            }
          }
          
          clickNextButton();
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
  
  // --- Homepage-only: Tutorial replay ---
  if (path.indexOf('index.html') !== -1 || path === '/' || path === '') {
    addSection('Tutorial');
    addButton('\uD83C\uDF93 Replay Welcome Tutorial', function() {
      localStorage.removeItem('arisEdu_tutorialCompleted');
      if (window.startTutorial) {
        window.startTutorial();
      } else {
        location.reload();
      }
    });
  }

  addSection('Debug Stats');
  addButton('\uD83D\uDCCB Show Storage Keys', function () {
      var keys = [];
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && (k.startsWith('alg1_u') || k.startsWith('alg2_u') || k.startsWith('chem_u') || k.startsWith('physics_u') || k.startsWith('bio_u') || k.startsWith('geometry_u'))) keys.push(k + ' = ' + localStorage.getItem(k));
      }
      keys.sort();
      alert('Progress Keys (' + keys.length + '):\n\n' + (keys.length ? keys.slice(0,50).join('\n') + (keys.length > 50 ? '\n...and more' : '') : '(none)'));
  });

  // ── Translation Debugger (inline panel) ──
  addSection('Translation Debugger');
  
  var transDebugContainer = document.createElement('div');
  transDebugContainer.id = 'trans-debug-container';
  transDebugContainer.style.cssText = 'display:none; margin-top:0.4rem; background:#0f172a; border:1px solid #334155; border-radius:0.4rem; padding:0.5rem 0.6rem; font-size:0.75rem; max-height:300px; overflow-y:auto;';
  
  addButton('\u2699 Open Translation Debugger', function() {
      var container = document.getElementById('trans-debug-container');
      if (!container) return;
      var isOpen = container.style.display !== 'none';
      if (isOpen) {
          container.style.display = 'none';
          return;
      }
      container.style.display = 'block';
      
      // Gather data
      if (!window.getTranslationDebugData) {
          container.innerHTML = '<span style="color:#f38ba8;">Translation script not loaded.</span>';
          return;
      }
      var d = window.getTranslationDebugData();
      var pct = d.matchableNodes > 0 ? Math.round(d.matchedNodes / d.matchableNodes * 100) : 0;
      var statusColor = d.isChinese ? '#a6e3a1' : '#f9e2af';
      
      var h = '';
      h += '<div style="display:flex;justify-content:space-between;margin-bottom:4px;"><span style="color:#94a3b8;">Language</span><span style="color:#f8fafc;font-weight:bold;">' + d.lang + '</span></div>';
      h += '<div style="display:flex;justify-content:space-between;margin-bottom:4px;"><span style="color:#94a3b8;">Chinese Active</span><span style="color:' + statusColor + ';font-weight:bold;">' + (d.isChinese ? 'YES' : 'NO') + '</span></div>';
      h += '<div style="background:#1e293b;border-radius:4px;padding:6px 8px;margin:6px 0;">';
      h += r('Translation keys', d.totalKeys, '#a6e3a1');
      h += r('.translatable els', d.translatableCount, '#89dceb');
      h += r('[data-en] els', d.dataEnCount, '#89dceb');
      h += r('Text nodes', d.matchableNodes, '#c4b5fd');
      h += r('Matched', d.matchedNodes, '#a6e3a1');
      h += r('Unmatched', d.unmatchedNodes, d.unmatchedNodes > 0 ? '#f38ba8' : '#a6e3a1');
      h += '</div>';
      // Progress bar
      h += '<div style="display:flex;justify-content:space-between;margin-bottom:3px;"><span style="color:#94a3b8;">Match Rate</span><span style="color:#f8fafc;">' + pct + '%</span></div>';
      h += '<div style="background:#334155;border-radius:3px;height:5px;overflow:hidden;margin-bottom:8px;">';
      h += '<div style="background:' + (pct > 70 ? '#a6e3a1' : pct > 40 ? '#f9e2af' : '#f38ba8') + ';height:100%;width:' + pct + '%;border-radius:3px;"></div></div>';
      // Unmatched samples
      if (d.unmatchedSamples.length > 0) {
          h += '<div style="color:#f38ba8;font-weight:bold;margin-bottom:4px;">Unmatched (' + d.unmatchedSamples.length + ')</div>';
          for (var i = 0; i < d.unmatchedSamples.length; i++) {
              h += '<div style="padding:2px 0;border-bottom:1px solid #1e293b;color:#94a3b8;word-break:break-all;font-size:0.7rem;">' + esc(d.unmatchedSamples[i]) + '</div>';
          }
      }
      // Refresh
      h += '<div style="text-align:center;margin-top:8px;"><button onclick="document.getElementById(\'trans-debug-container\').style.display=\'none\';document.querySelector(\'[data-trans-debug-btn]\').click();" style="background:#3b82f6;color:#fff;border:none;border-radius:3px;padding:3px 12px;cursor:pointer;font-size:0.7rem;">Refresh</button></div>';
      container.innerHTML = h;
      
      function r(label, val, color) {
          return '<div style="display:flex;justify-content:space-between;padding:1px 0;"><span style="color:#94a3b8;">' + label + '</span><span style="color:' + color + ';font-weight:bold;">' + val + '</span></div>';
      }
      function esc(s) { return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  });
  
  // Mark the button so refresh can find it
  body.lastChild.setAttribute('data-trans-debug-btn', '1');
  body.appendChild(transDebugContainer);

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
