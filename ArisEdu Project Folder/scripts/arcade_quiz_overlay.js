/**
 * arcade_quiz_overlay.js
 * Every INTERVAL_MS (default 30s), pauses the arcade game and shows a
 * question drawn from the lesson the student came from.
 * Questions are stored in sessionStorage by practice_games.js before launch.
 * Skipped for games with built-in quiz (window.hasBuiltInQuiz = true).
 */
(function () {
    // Skip for games that have their own question system (e.g. GameBlocks)
    if (window.hasBuiltInQuiz) return;

    var INTERVAL_MS = 30000;   // ms between questions

    // Load questions saved by practice page
    var questions = [];
    try {
        var raw = sessionStorage.getItem('arcadeLessonQuestions');
        if (raw) questions = JSON.parse(raw);
    } catch (e) {}

    if (!questions || questions.length === 0) return; // no lesson context — skip

    // Shuffle
    for (var i = questions.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var tmp = questions[i]; questions[i] = questions[j]; questions[j] = tmp;
    }

    var qIdx = 0;
    var overlayEl = null;
    var scheduleTimer = null;

    function escHtml(s) {
        return String(s)
            .replace(/&/g, '&amp;').replace(/</g, '&lt;')
            .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    function tryPause() {
        try { if (typeof window.pauseGame === 'function') window.pauseGame(); } catch (e) {}
        window.arcadeOverlayActive = true;
    }

    function tryResume() {
        window.arcadeOverlayActive = false;
        try { if (typeof window.resumeGame === 'function') window.resumeGame(); } catch (e) {}
    }

    function scheduleNext() {
        clearTimeout(scheduleTimer);
        scheduleTimer = setTimeout(showQuestion, INTERVAL_MS);
    }

    function showQuestion() {
        if (overlayEl) return; // already showing

        var q = questions[qIdx % questions.length];
        qIdx++;
        tryPause();

        var optLetters = ['A', 'B', 'C', 'D', 'E'];
        var selectedIdx = null;
        var submitted = false;

        // Build option labels (quiz-style radio buttons)
        var optionsHtml = '';
        if (q.options && q.options.length > 0) {
            optionsHtml = q.options.map(function (opt, i) {
                return '<label class="aqo-opt-label" data-idx="' + i + '" style="'
                    + 'display:flex;align-items:center;gap:clamp(0.4rem,1.5vw,0.75rem);'
                    + 'padding:clamp(0.5rem,1.5vw,0.9rem) clamp(0.5rem,2vw,1rem);'
                    + 'border:2px solid #374151;border-radius:0.6rem;background:#1f2937;'
                    + 'cursor:pointer;margin-bottom:clamp(0.4rem,1.5vw,0.75rem);'
                    + 'transition:border-color 0.15s,background 0.15s;">'
                    + '<span style="display:inline-flex;align-items:center;justify-content:center;'
                    + 'min-width:clamp(20px,4vw,28px);width:clamp(20px,4vw,28px);height:clamp(20px,4vw,28px);'
                    + 'background:#3b82f6;color:#fff;flex-shrink:0;'
                    + 'border-radius:50%;font-weight:700;font-size:clamp(0.65rem,1.8vw,0.85rem);">' + optLetters[i] + '</span>'
                    + '<span style="color:#e5e7eb;font-size:clamp(0.75rem,2vw,0.95rem);">' + escHtml(opt) + '</span>'
                    + '</label>';
            }).join('');
        } else {
            optionsHtml = '<div style="background:#111827;border-radius:0.75rem;padding:1rem;'
                + 'color:#9ca3af;font-size:0.9rem;">'
                + 'Answer: <strong style="color:#f3f4f6;">' + escHtml(q.answer) + '</strong></div>';
        }

        overlayEl = document.createElement('div');
        overlayEl.style.cssText =
            'position:fixed;inset:0;background:rgba(0,0,0,0.92);z-index:999999;'
            + 'display:flex;align-items:flex-start;justify-content:center;'
            + 'padding:clamp(0.5rem,3vw,1.5rem);box-sizing:border-box;'
            + 'font-family:\'Poppins\',\'Segoe UI\',sans-serif;overflow-y:auto;';

        overlayEl.innerHTML =
            '<div style="background:#111827;border:1px solid #374151;border-radius:0.75rem;'
            + 'width:min(680px,100%);margin:auto;box-shadow:0 24px 48px rgba(0,0,0,0.6);overflow:hidden;">'
            // Header bar
            + '<div style="background:#1f2937;border-bottom:1px solid #374151;'
            + 'padding:clamp(0.5rem,2vw,1rem) clamp(0.75rem,3vw,1.5rem);'
            + 'display:flex;align-items:center;">'
            + '<span style="color:#3b82f6;font-size:clamp(0.6rem,1.5vw,0.75rem);font-weight:700;letter-spacing:2px;text-transform:uppercase;">Lesson Check</span>'
            + '</div>'
            // Body
            + '<div style="padding:clamp(0.75rem,3vw,2rem);'
            + 'max-height:calc(100vh - clamp(1rem,6vw,3rem));overflow-y:auto;box-sizing:border-box;">'
            + '<h3 style="font-size:clamp(0.85rem,2.5vw,1.1rem);font-weight:600;color:#f3f4f6;line-height:1.5;margin:0 0 clamp(0.75rem,2vw,1.5rem);">'
            + escHtml(q.question) + '</h3>'
            + '<div id="aqo-opts">' + optionsHtml + '</div>'
            + '<div id="aqo-feedback" style="margin-top:0.75rem;padding:0.75rem 1rem;border-radius:0.5rem;'
            + 'border-left:4px solid transparent;display:none;'
            + 'font-size:clamp(0.75rem,2vw,0.9rem);font-weight:600;"></div>'
            + '<div style="margin-top:1rem;display:flex;justify-content:flex-end;gap:0.5rem;">'
            + '<button id="aqo-submit" style="padding:clamp(0.4rem,1.5vw,0.7rem) clamp(0.75rem,3vw,1.75rem);'
            + 'background:#3b82f6;color:#fff;border:none;border-radius:0.5rem;cursor:pointer;'
            + 'font-size:clamp(0.75rem,2vw,0.95rem);font-weight:600;'
            + 'font-family:inherit;transition:background 0.15s;">Submit</button>'
            + '<button id="aqo-continue" style="padding:clamp(0.4rem,1.5vw,0.7rem) clamp(0.75rem,3vw,1.75rem);'
            + 'background:#16a34a;color:#fff;border:none;border-radius:0.5rem;cursor:pointer;'
            + 'font-size:clamp(0.75rem,2vw,0.95rem);font-weight:600;'
            + 'font-family:inherit;display:none;transition:background 0.15s;">Continue</button>'
            + '</div>'
            + '</div></div>';

        document.body.appendChild(overlayEl);

        // Option selection
        overlayEl.querySelectorAll('.aqo-opt-label').forEach(function (lbl) {
            lbl.addEventListener('click', function () {
                if (submitted) return;
                selectedIdx = parseInt(lbl.getAttribute('data-idx'));
                overlayEl.querySelectorAll('.aqo-opt-label').forEach(function (l) {
                    l.style.borderColor = '#374151';
                    l.style.background = '#1f2937';
                });
                lbl.style.borderColor = '#3b82f6';
                lbl.style.background = '#1e3a8a';
            });
        });

        // Submit
        var submitBtn = overlayEl.querySelector('#aqo-submit');
        var continueBtn = overlayEl.querySelector('#aqo-continue');
        var fbEl = overlayEl.querySelector('#aqo-feedback');

        submitBtn.addEventListener('mouseenter', function () { submitBtn.style.background = '#2563eb'; });
        submitBtn.addEventListener('mouseleave', function () { submitBtn.style.background = '#3b82f6'; });
        continueBtn.addEventListener('mouseenter', function () { continueBtn.style.background = '#15803d'; });
        continueBtn.addEventListener('mouseleave', function () { continueBtn.style.background = '#16a34a'; });

        submitBtn.addEventListener('click', function () {
            if (submitted) return;
            if (selectedIdx === null && q.options && q.options.length > 0) {
                fbEl.textContent = 'Please select an answer first.';
                fbEl.style.display = 'block';
                fbEl.style.background = '#fff7ed';
                fbEl.style.borderColor = '#f97316';
                fbEl.style.color = '#c2410c';
                return;
            }
            submitted = true;
            submitBtn.style.display = 'none';

            // Disable options
            overlayEl.querySelectorAll('.aqo-opt-label').forEach(function (l) {
                l.style.cursor = 'default';
                l.style.pointerEvents = 'none';
            });

            if (q.options && q.options.length > 0) {
                var isCorrect = q.options[selectedIdx] === q.answer;
                // Colour options
                overlayEl.querySelectorAll('.aqo-opt-label').forEach(function (l, i) {
                    if (q.options[i] === q.answer) {
                        l.style.borderColor = '#10b981'; l.style.background = '#065f46';
                    } else if (i === selectedIdx && !isCorrect) {
                        l.style.borderColor = '#ef4444'; l.style.background = '#7f1d1d';
                    }
                });
                fbEl.textContent = isCorrect ? '✓ Correct! Great job.' : '✗ Incorrect — correct answer highlighted above.';
                fbEl.style.display = 'block';
                fbEl.style.background = isCorrect ? '#065f46' : '#7f1d1d';
                fbEl.style.borderColor = isCorrect ? '#10b981' : '#ef4444';
                fbEl.style.color = isCorrect ? '#d1fae5' : '#fee2e2';
            }

            continueBtn.style.display = 'block';
        });

        continueBtn.addEventListener('click', closeOverlay);
    }

    function closeOverlay() {
        if (overlayEl) { overlayEl.remove(); overlayEl = null; }
        tryResume();
        scheduleNext();
    }

    // Expose for games that want to manually trigger
    window.arcadeShowQuestion = showQuestion;
    window.arcadeCloseOverlay = closeOverlay;

    // Start after first interval
    scheduleNext();
})();
