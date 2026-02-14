
// Start of quiz logic
(function() {
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

    window.checkQuizAnswer = function(name, correct, btn) {
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
            feedback.textContent = "Please select an answer first.";
            feedback.style.color = "#ea580c";
            feedback.style.background = "#fff7ed";
            return;
        }

        if (attempts <= 0 || btn.disabled) return;
        
        if (selected.value === correct) {
            feedback.textContent = "Correct! Great job.";
            feedback.style.color = "#16a34a"; 
            feedback.style.background = "#dcfce7";
            btn.disabled = true;
            const inputs = parent.querySelectorAll('input');
            inputs.forEach(i => i.disabled = true);
            attemptsElem.style.display = 'none';
        } else {
            attempts--;
            parent.dataset.attempts = attempts;
            attemptsElem.textContent = `Attempts left: ${attempts}`;

            if (attempts <= 0) {
                 feedback.textContent = `Incorrect. The correct answer was option ${correct.toUpperCase()}.`;
                 feedback.style.color = "#dc2626";
                 feedback.style.background = "#fee2e2";
                 btn.disabled = true;
                 const inputs = parent.querySelectorAll('input');
                 inputs.forEach(i => i.disabled = true);
            } else {
                 feedback.textContent = "Incorrect. Try again!";
                 feedback.style.color = "#dc2626";
                 feedback.style.background = "#fee2e2";
            }
        }
    };

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

    // Reset a quiz question (clear answer, re-enable inputs)
    window.resetQuizQuestion = function(btn) {
        const p = btn.closest('.quiz-question');
        if (!p) return;
        const f = p.querySelector('.feedback');
        if (f) f.remove();
        p.querySelectorAll('input').forEach(i => { i.disabled = false; i.checked = false; });
        p.dataset.status = '';
        p.dataset.attempts = '2';
        const attemptsIndicator = p.querySelector('.attempts-indicator');
        if (attemptsIndicator) { attemptsIndicator.style.display = 'none'; attemptsIndicator.textContent = ''; }
        const submitBtn = p.querySelector('.action-button');
        if (submitBtn) submitBtn.disabled = false;
    };

    // Auto-Initialization Logic
    document.addEventListener('DOMContentLoaded', () => {
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
