
// Start of quiz logic
(function() {
    function _t(key, fallback) {
        var t = window.arisEduTranslations || window.globalTranslations;
        return (t && t[key]) || fallback || key;
    }
    window.toggleToPractice = function(event) {
        // Find current quiz view
        const quizView = document.getElementById('quiz-content-view');
        if(quizView) {
            quizView.style.display = 'none';
        }

        const practiceView = document.getElementById('practice-content-view');
        if (practiceView) {
            practiceView.style.display = 'block'; 
            window.scrollTo(0,0);
        } else {
             // Fallback if no embedded practice view, try linking to separate file
             // Use updated taskbar logic for link resolution
             const practiceLink = document.querySelector('a[href*="Practice.html"]');
             if(practiceLink) {
                 location.href = practiceLink.href;
             }
        }
    };

    window.randomizeQuizQuestions = function() {
        const container = document.querySelector('.quiz-container form');
        if(!container) return;
        const questions = Array.from(container.querySelectorAll('.quiz-question'));
        
        // Fisher-Yates shuffle
        for (let i = questions.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [questions[i], questions[j]] = [questions[j], questions[i]];
        }
        
        questions.forEach(q => container.appendChild(q));

        questions.forEach((q, index) => {
            const p = q.querySelector('p');
            if(p) {
                p.textContent = p.textContent.replace(/^\d+\.\s*/, `${index + 1}. `);
            }
        });
    };

    // New function to check quiz answer by automatically detecting the correct value
    window.checkQuiz = function(questionName) {
        const parent = document.querySelector(`.quiz-question input[name="${questionName}"]`)?.closest('.quiz-question');
        if (!parent) return;
        
        const submitBtn = parent.querySelector('.action-button');
        const selected = parent.querySelector(`input[name="${questionName}"]:checked`);
        
        if (!selected) {
            alert('Please select an answer first');
            return;
        }
        
        // Get the value of the selected answer ('correct' or 'wrong')
        const correctValue = selected.value;
        
        // Call the main checkQuizAnswer function with the correct value
        window.checkQuizAnswer(questionName, correctValue, submitBtn);
    };

    window.checkQuizAnswer = function(name, correct, btn) {
        try {
            const parent = btn.closest('.quiz-question');
            if(!parent) return;

            // Get or Init Attempts
            let attemptsElem = parent.querySelector('.attempts-indicator');
            if (!attemptsElem) return;
            
            let attempts = parseInt(parent.dataset.attempts || '2');

            const selected = parent.querySelector(`input[name="${name}"]:checked`);
            let feedback = parent.querySelector('.feedback');
            if(!feedback) {
                feedback = document.createElement('div');
                feedback.className = 'feedback';
                feedback.style.marginTop = '1rem';
                feedback.style.fontWeight = 'bold';
                feedback.style.padding = '0.5rem';
                feedback.style.borderRadius = '0.5rem';
                parent.appendChild(feedback);
            }
            
            if (!selected) {
                feedback.textContent = _t("Please select an answer first.");
                feedback.style.color = "#ea580c";
                feedback.style.background = "#fff7ed";
                return;
            }

            if (btn.disabled) return;
            // Ensure attempts doesn't go below 0 logically before checking
             if (attempts <= 0 && selected.value !== correct) {
                 // Already failed, just show correct/incorrect state again if needed or return
                 // But wait, if attempts <= 0, we shouldn't even be here unless button is enabled
                 // If button is enabled but attempts <= 0, we should disable it
                 btn.disabled = true;
                 return;
             }

            if (selected.value === correct) {
                feedback.textContent = _t("Correct! Great job.");
                feedback.style.color = "#16a34a"; 
                feedback.style.background = "#dcfce7";
                btn.disabled = true;
                const inputs = parent.querySelectorAll('input');
                inputs.forEach(i => i.disabled = true);
                attemptsElem.style.display = 'none';
                // Hide Try Again on correct answer
                const tryAgainBtn = parent.querySelector('.nav-button');
                if (tryAgainBtn) tryAgainBtn.style.display = 'none';
                // Check if ALL questions are now correct
                checkQuizCompletion();
            } else {
                attempts--;
                parent.dataset.attempts = attempts;
                attemptsElem.textContent = _t("Attempts left:") + " " + attempts;
                attemptsElem.style.display = 'block';

                if (attempts <= 0) {
                     // Find the correct answer text to display
                     const correctInput = parent.querySelector(`input[name="${name}"][value="correct"]`);
                     const correctText = correctInput ? correctInput.parentElement.textContent.trim() : '';
                     feedback.textContent = correctText
                         ? _t("Incorrect. The correct answer was:", "\u4e0d\u6b63\u786e\u3002\u6b63\u786e\u7b54\u6848\u662f\uff1a") + " " + correctText
                         : _t("Incorrect.", "\u4e0d\u6b63\u786e\u3002");
                     feedback.style.color = "#dc2626";
                     feedback.style.background = "#fee2e2";
                     btn.disabled = true;
                     const inputs = parent.querySelectorAll('input');
                     inputs.forEach(i => i.disabled = true);
                     // Highlight Try Again button
                     const tryAgainBtn = parent.querySelector('.nav-button');
                     if (tryAgainBtn) {
                         tryAgainBtn.style.background = '#3b82f6';
                         tryAgainBtn.style.color = '#fff';
                         tryAgainBtn.style.animation = 'pulse 1.5s infinite';
                     }
                } else {
                     feedback.textContent = _t("Incorrect. Try again!");
                     feedback.style.color = "#dc2626";
                     feedback.style.background = "#fee2e2";
                }
            }
        } catch (e) {
            console.error("Quiz Error:", e);
        }
    };

    // Check if every question on the quiz has been answered correctly
    function checkQuizCompletion() {
        const questions = document.querySelectorAll('.quiz-question');
        if (questions.length === 0) return;

        const allCorrect = Array.from(questions).every(q => {
            const fb = q.querySelector('.feedback');
            return fb && (fb.textContent.startsWith('Correct') || fb.textContent.startsWith(_t('Correct')));
        });
        if (!allCorrect) return;

        // Call the per-file markQuizComplete() if it exists (each quiz file defines its own)
        if (typeof window.markQuizComplete === 'function') {
            window.markQuizComplete();
        } else {
            // Fallback: parse lesson info from URL
            const path = decodeURIComponent(window.location.pathname);
            const match = path.match(/Lesson\s*(\w+)\.(\d+)_Quiz/);
            if (match) {
                const unit = match[1];
                const lesson = match[2];
                // Detect physics vs chemistry from path
                const subject = path.includes('PhysicsLessons') ? 'physics' : 'chem';
                localStorage.setItem(`${subject}_u${unit}_l${lesson}_completed`, 'true');
            }
        }

        // Show success banner
        const resultsDiv = document.getElementById('quiz-results');
        if (resultsDiv) {
            resultsDiv.style.display = 'block';
            resultsDiv.style.color = '#16a34a';
            resultsDiv.style.background = '#dcfce7';
            resultsDiv.style.textAlign = 'center';
            resultsDiv.style.fontSize = '1.25rem';
            resultsDiv.textContent = _t('\u2714 All Correct! Lesson completed.');
        }
    }

    // Navigation / UI Helpers
    window.togglePracticesPanel = function(button) {
        if (!button) return;
        const menu = button.closest('.Practices-menu') || button.closest('.side-buttons'); 
        if (!menu) return;
        const panel = menu.querySelector('.Practices-panel');
        if (!panel) return;
        const isOpen = panel.classList.toggle('is-open');
        panel.setAttribute('aria-hidden', (!isOpen).toString());
    };

    // Reset a quiz question: clear answer, re-enable inputs, shuffle options for a fresh attempt
    window.resetQuizQuestion = function(btn) {
        const p = btn.closest('.quiz-question');
        if (!p) return;
        // Remove feedback
        const f = p.querySelector('.feedback');
        if (f) f.remove();
        // Re-enable and uncheck all inputs
        p.querySelectorAll('input').forEach(i => { i.disabled = false; i.checked = false; });
        p.dataset.status = '';
        p.dataset.attempts = '2';
        // Reset attempts indicator
        const attemptsIndicator = p.querySelector('.attempts-indicator');
        if (attemptsIndicator) { attemptsIndicator.style.display = 'none'; attemptsIndicator.textContent = ''; }
        // Re-enable submit button
        const submitBtn = p.querySelector('.action-button');
        if (submitBtn) submitBtn.disabled = false;
        // Reset Try Again button styling
        btn.style.background = '';
        btn.style.color = '';
        btn.style.animation = '';

        // Shuffle answer labels so it feels like a new question
        const labels = Array.from(p.querySelectorAll('label'));
        if (labels.length > 1) {
            const container = labels[0].parentElement;
            // Fisher-Yates shuffle
            for (let i = labels.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [labels[i], labels[j]] = [labels[j], labels[i]];
            }
            // Re-insert before the attempts-indicator div
            const refNode = p.querySelector('.attempts-indicator');
            labels.forEach(label => container.insertBefore(label, refNode));
        }

        // Scroll this question into view
        p.scrollIntoView({ behavior: 'smooth', block: 'center' });
    };

    // Auto-Initialization Logic
    document.addEventListener('DOMContentLoaded', () => {
        // Inject pulse animation for Try Again button highlight
        if (!document.getElementById('quiz-ui-styles')) {
            const style = document.createElement('style');
            style.id = 'quiz-ui-styles';
            style.textContent = '@keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.7; } }';
            document.head.appendChild(style);
        }

        // Fix for Quiz pages showing Summary by default
        const path = window.location.pathname;
        // Check if we are on a Quiz page
        if (path.endsWith('Quiz.html') || path.indexOf('Quiz.html') !== -1) {
            
            // 1. Hide Summary View
            const summaryView = document.getElementById('summary-content-view');
            if (summaryView) summaryView.style.display = 'none';
            
            // 2. Hide Practice View
            const practiceView = document.getElementById('practice-content-view');
            if (practiceView) practiceView.style.display = 'none';
            
            // 3. Show Quiz View
            const quizView = document.getElementById('quiz-content-view');
            if (quizView) quizView.style.display = 'block'; // Make sure this is block
            
            // 4. Randomize Questions
            if (window.randomizeQuizQuestions) window.randomizeQuizQuestions();
            
            // 5. Scroll top
            window.scrollTo(0, 0);
        }
    });
    
})();
