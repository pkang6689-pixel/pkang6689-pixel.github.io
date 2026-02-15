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
    '.dev-btn.green:hover { background:#15803d; }';
  document.head.appendChild(style);

  // Toggle collapse
  var collapsed = false;
  panel.querySelector('#dev-tools-toggle').addEventListener('click', function () {
    collapsed = !collapsed;
    panel.querySelector('#dev-tools-body').classList.toggle('collapsed', collapsed);
    this.textContent = collapsed ? '\u25BC' : '\u25B2';
    this.title = collapsed ? 'Expand' : 'Collapse';
  });

  // Detect page type from URL
  var path = decodeURIComponent(window.location.pathname);
  var body = panel.querySelector('#dev-tools-body');
  var buttons = [];

  // --- Quiz page ---
  var quizMatch = path.match(/Lesson\s+(\w+)\.(\d+)_Quiz/);
  if (quizMatch) {
    var qUnit = quizMatch[1];
    var qLesson = quizMatch[2];

    buttons.push({
      text: '\u2714 Complete This Quiz',
      cls: 'green',
      action: function () {
        // Mark all answers correct
        document.querySelectorAll('.quiz-question').forEach(function (q) {
          var correctInput = q.querySelector('input[value="correct"]');
          if (correctInput) {
            correctInput.checked = true;
            var submitBtn = q.querySelector('.action-button');
            if (submitBtn && !submitBtn.disabled) submitBtn.click();
          }
        });
      }
    });

    buttons.push({
      text: '\u274C Clear This Lesson Completion',
      cls: 'red',
      action: function () {
        localStorage.removeItem('chem_u' + qUnit + '_l' + qLesson + '_completed');
        alert('Cleared completion for Lesson ' + qUnit + '.' + qLesson);
      }
    });
  }

  // --- Unit Test page ---
  var testMatch = path.match(/Unit(\w+)_Test/);
  if (testMatch) {
    var tUnit = testMatch[1];
    var testLessonMap = {
      '1': 9, '2': 6, '3': 9, '4': 10,
      '5A': 9, '5B': 6,
      '6': 8, '7': 9, '8': 10, '9': 9,
      '10': 11, '11': 7, '12': 6
    };
    var tLesson = testLessonMap[tUnit];

    buttons.push({
      text: '\u2714 Complete This Unit Test',
      cls: 'green',
      action: function () {
        // Auto-answer all quiz questions correctly
        var form = document.getElementById('quiz-form');
        if (form) {
          form.querySelectorAll('.quiz-question').forEach(function (q) {
            var correctInput = q.querySelector('input[value="correct"]');
            if (correctInput) {
              correctInput.checked = true;
              var submitBtn = q.querySelector('button[onclick^="checkQuizAnswer"]');
              if (submitBtn && !submitBtn.disabled) submitBtn.click();
            }
          });
        }
      }
    });

    if (tLesson) {
      buttons.push({
        text: '\u274C Clear This Test Completion',
        cls: 'red',
        action: function () {
          localStorage.removeItem('chem_u' + tUnit + '_l' + tLesson + '_completed');
          alert('Cleared completion for Unit ' + tUnit + ' Test');
        }
      });
    }
  }

  // --- chem.html (course map) ---
  var isChemMap = path.indexOf('chem.html') !== -1;
  if (isChemMap) {
    buttons.push({
      text: '\u274C Clear All Progress',
      cls: 'red',
      action: function () {
        if (confirm('Clear ALL progress data? This cannot be undone.')) {
          if (typeof clearAllProgress === 'function') clearAllProgress();
        }
      }
    });

    buttons.push({
      text: '\u2714 Complete All Lessons',
      cls: 'green',
      action: function () {
        // Set all lessons as completed
        var allLessons = {
          '1': 9, '2': 6, '3': 9, '4': 10,
          '5A': 9, '5B': 6,
          '6': 8, '7': 9, '8': 10, '9': 9,
          '10': 11, '11': 7, '12': 6
        };
        for (var u in allLessons) {
          for (var l = 1; l <= allLessons[u]; l++) {
            localStorage.setItem('chem_u' + u + '_l' + l + '_started', 'true');
            localStorage.setItem('chem_u' + u + '_l' + l + '_completed', 'true');
          }
        }
        alert('All lessons marked as completed. Reload the page to see changes.');
        location.reload();
      }
    });
  }

  // --- Always-available buttons ---
  buttons.push({
    text: '\uD83D\uDCCB Show localStorage Keys',
    cls: '',
    action: function () {
      var keys = [];
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.startsWith('chem_u')) keys.push(k + ' = ' + localStorage.getItem(k));
      }
      keys.sort();
      alert('Chemistry Progress Keys (' + keys.length + '):\n\n' + (keys.length ? keys.join('\n') : '(none)'));
    }
  });

  // Build button elements
  if (buttons.length === 0) return;

  buttons.forEach(function (b) {
    var btn = document.createElement('button');
    btn.className = 'dev-btn' + (b.cls ? ' ' + b.cls : '');
    btn.textContent = b.text;
    btn.addEventListener('click', b.action);
    body.appendChild(btn);
  });

  // Add panel to DOM after page loads
  function mount() {
    document.body.appendChild(panel);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
