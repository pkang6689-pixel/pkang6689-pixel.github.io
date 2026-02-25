
// Start of quiz logic
(function() {
    // Quiz Analytics Tracking
    const quizAnalytics = {
        quizStartTime: null,
        quizEndTime: null,
        questions: {}, // { questionName: { startTime, endTime, wrongAttempts, correctText } }
        completedCount: 0,
        totalQuestions: 0
    };

    function _t(key, fallback) {
        var t = window.arisEduTranslations || window.globalTranslations;
        return (t && t[key]) || fallback || key;
    }

    // Track when a question is first interacted with
    function trackQuestionStart(questionName) {
        if (!quizAnalytics.questions[questionName]) {
            quizAnalytics.questions[questionName] = {
                startTime: Date.now(),
                endTime: null,
                wrongAttempts: 0,
                question: '',
                correctText: ''
            };
        } else if (quizAnalytics.questions[questionName].startTime === null) {
            // Set startTime if it's null (was pre-initialized but not yet started)
            quizAnalytics.questions[questionName].startTime = Date.now();
        }
    }

    // Track when a question is answered (correctly or incorrectly)
    function trackQuestionEnd(questionName) {
        if (quizAnalytics.questions[questionName]) {
            quizAnalytics.questions[questionName].endTime = Date.now();
        }
    }

    // Record a wrong attempt on a question
    function recordWrongAttempt(questionName, parent) {
        if (quizAnalytics.questions[questionName]) {
            quizAnalytics.questions[questionName].wrongAttempts++;
        }
        // Extract question text
        const qText = parent.querySelector('p');
        if (qText && !quizAnalytics.questions[questionName].question) {
            quizAnalytics.questions[questionName].question = qText.textContent;
        }
    }

    // Format time duration in mm:ss format
    function formatDuration(ms) {
        const seconds = Math.floor(ms / 1000);
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        return `${minutes}:${secs.toString().padStart(2, '0')}`;
    }

    // Create and show the quiz completion screen
    function showQuizCompletionScreen() {
        if (!quizAnalytics.quizStartTime || !quizAnalytics.quizEndTime) {
            return; // Missing timing data
        }

        const totalTime = quizAnalytics.quizEndTime - quizAnalytics.quizStartTime;
        const wrongAnswers = Object.entries(quizAnalytics.questions)
            .filter(([_, data]) => data.wrongAttempts > 0)
            .map(([name, data]) => ({
                name,
                ...data
            }));

        // Create modal HTML
        const modal = document.createElement('div');
        modal.id = 'quiz-completion-modal';
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(4px);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1rem;
        `;

        const content = document.createElement('div');
        content.style.cssText = `
            background: white;
            border-radius: 1.5rem;
            padding: 2rem;
            max-width: 700px;
            width: 100%;
            max-height: 90vh;
            overflow-y: auto;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        `;

        // Dark mode support
        if (document.body.classList.contains('dark-mode')) {
            content.style.background = '#1e293b';
            content.style.color = '#e2e8f0';
        }

        // Header
        const header = document.createElement('div');
        header.style.cssText = `
            text-align: center;
            margin-bottom: 2rem;
            border-bottom: 2px solid #10b981;
            padding-bottom: 1rem;
        `;
        header.innerHTML = `
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎉</div>
            <h2 style="font-size: 2rem; margin: 0.5rem 0; font-weight: 700;">Quiz Complete!</h2>
            <p style="margin: 0.5rem 0; font-size: 1.1rem; opacity: 0.9;">Great job finishing this quiz</p>
        `;
        content.appendChild(header);

        // Overall Statistics
        const stats = document.createElement('div');
        stats.style.cssText = `
            background: ${document.body.classList.contains('dark-mode') ? '#334155' : '#f1f5f9'};
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 2rem;
        `;

        const accuracy = ((quizAnalytics.totalQuestions - wrongAnswers.length) / quizAnalytics.totalQuestions * 100).toFixed(0);
        const avgTimePerQuestion = (totalTime / quizAnalytics.totalQuestions / 1000).toFixed(1);

        stats.innerHTML = `
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div style="text-align: center; padding: 1rem; background: ${document.body.classList.contains('dark-mode') ? '#475569' : '#e0f2fe'}; border-radius: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: 700; color: #0ea5e9;">⏱️ ${formatDuration(totalTime)}</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Total Time</div>
                </div>
                <div style="text-align: center; padding: 1rem; background: ${document.body.classList.contains('dark-mode') ? '#475569' : '#e0f2fe'}; border-radius: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: 700; color: #10b981;">${accuracy}%</div>
                    <div style="font-size: 0.9rem; opacity: 0.8;">Accuracy</div>
                </div>
            </div>
            <div style="text-align: center; padding: 1rem; background: ${document.body.classList.contains('dark-mode') ? '#475569' : '#e0f2fe'}; border-radius: 0.5rem;">
                <div style="font-size: 1.5rem; font-weight: 700;">${avgTimePerQuestion}s</div>
                <div style="font-size: 0.9rem; opacity: 0.8;">Avg Time per Question</div>
            </div>
        `;
        content.appendChild(stats);

        // Time per question breakdown
        const timingSection = document.createElement('div');
        timingSection.style.cssText = `margin-bottom: 2rem;`;
        timingSection.innerHTML = `<h3 style="font-size: 1.3rem; margin-bottom: 1rem; font-weight: 700;">⏱️ Time per Question</h3>`;

        const timingList = document.createElement('div');
        Object.entries(quizAnalytics.questions).forEach(([_, data], index) => {
            const qTime = (data.endTime - data.startTime) / 1000;
            const qDiv = document.createElement('div');
            qDiv.style.cssText = `
                padding: 0.75rem;
                margin-bottom: 0.5rem;
                border-radius: 0.5rem;
                background: ${document.body.classList.contains('dark-mode') ? '#334155' : '#f1f5f9'};
                display: flex;
                justify-content: space-between;
                align-items: center;
            `;
            qDiv.innerHTML = `
                <span>Question ${index + 1}</span>
                <span style="font-weight: 600; color: #0ea5e9;">${qTime.toFixed(1)}s</span>
            `;
            timingList.appendChild(qDiv);
        });
        timingSection.appendChild(timingList);
        content.appendChild(timingSection);

        // Wrong answers section (if any)
        if (wrongAnswers.length > 0) {
            const wrongSection = document.createElement('div');
            wrongSection.style.cssText = `
                background: ${document.body.classList.contains('dark-mode') ? '#7f1d1d' : '#fee2e2'};
                border-left: 4px solid #dc2626;
                padding: 1.5rem;
                border-radius: 0.5rem;
                margin-bottom: 2rem;
            `;
            wrongSection.innerHTML = `<h3 style="font-size: 1.3rem; margin: 0 0 1rem 0; font-weight: 700; color: #dc2626;">❌ Questions with Wrong Attempts</h3>`;

            const wrongList = document.createElement('div');
            wrongAnswers.forEach(({ name, wrongAttempts, question }, index) => {
                const wrongDiv = document.createElement('div');
                wrongDiv.style.cssText = `
                    padding: 0.75rem;
                    margin-bottom: 0.75rem;
                    background: ${document.body.classList.contains('dark-mode') ? '#5f2424' : '#fecaca'};
                    border-radius: 0.5rem;
                    border-left: 3px solid #dc2626;
                `;
                wrongDiv.innerHTML = `
                    <div style="font-weight: 600; margin-bottom: 0.25rem;">${question.substring(0, 80)}...</div>
                    <div style="font-size: 0.85rem; opacity: 0.8;">❌ ${wrongAttempts} wrong ${wrongAttempts === 1 ? 'attempt' : 'attempts'}</div>
                `;
                wrongList.appendChild(wrongDiv);
            });
            wrongSection.appendChild(wrongList);
            content.appendChild(wrongSection);
        }

        // Action buttons
        const buttonContainer = document.createElement('div');
        buttonContainer.style.cssText = `
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid ${document.body.classList.contains('dark-mode') ? '#475569' : '#e2e8f0'};
        `;

        const closeBtn = document.createElement('button');
        closeBtn.textContent = '✕ Close';
        closeBtn.style.cssText = `
            padding: 0.75rem 1.5rem;
            background: #64748b;
            color: white;
            border: none;
            border-radius: 0.5rem;
            font-weight: 600;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.2s;
        `;
        closeBtn.onmouseover = () => closeBtn.style.background = '#475569';
        closeBtn.onmouseout = () => closeBtn.style.background = '#64748b';
        closeBtn.onclick = () => modal.remove();

        const continueBtn = document.createElement('button');
        continueBtn.textContent = '→ Continue to Practice';
        continueBtn.style.cssText = `
            padding: 0.75rem 1.5rem;
            background: #10b981;
            color: white;
            border: none;
            border-radius: 0.5rem;
            font-weight: 600;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.2s;
        `;
        continueBtn.onmouseover = () => continueBtn.style.background = '#059669';
        continueBtn.onmouseout = () => continueBtn.style.background = '#10b981';
        continueBtn.onclick = () => {
            modal.remove();
            window.toggleToPractice();
        };

        buttonContainer.appendChild(closeBtn);
        buttonContainer.appendChild(continueBtn);
        content.appendChild(buttonContainer);

        modal.appendChild(content);
        document.body.appendChild(modal);
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

            // Track question interaction
            trackQuestionStart(name);
            
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
                feedback.textContent = _t("Correct! Great job.", "Correct! Great job.");
                feedback.style.color = "#16a34a"; 
                feedback.style.background = "#dcfce7";
                btn.disabled = true;
                const inputs = parent.querySelectorAll('input');
                inputs.forEach(i => i.disabled = true);
                attemptsElem.style.display = 'none';
                // Hide Try Again on correct answer
                const tryAgainBtn = parent.querySelector('.nav-button');
                if (tryAgainBtn) tryAgainBtn.style.display = 'none';
                
                // Track the correct answer
                trackQuestionEnd(name);
                const correctInput = parent.querySelector(`input[name="${name}"][value="correct"]`);
                if (correctInput) {
                    quizAnalytics.questions[name].correctText = correctInput.parentElement.textContent.trim();
                }
                
                // Check if ALL questions are now correct
                checkQuizCompletion();
            } else {
                // Track wrong attempt
                recordWrongAttempt(name, parent);
                
                attempts--;
                parent.dataset.attempts = attempts;
                attemptsElem.textContent = _t("Attempts left:") + " " + attempts;
                attemptsElem.style.display = 'block';

                if (attempts <= 0) {
                     // Find the correct answer text to display
                     const correctInput = parent.querySelector(`input[name="${name}"][value="correct"]`);
                     const correctText = correctInput ? correctInput.parentElement.textContent.trim() : '';
                     feedback.textContent = correctText
                         ? _t("Incorrect. The correct answer was:", "Incorrect. The correct answer was:") + " " + correctText
                         : _t("Incorrect.", "Incorrect.");
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

        // Record quiz end time
        quizAnalytics.quizEndTime = Date.now();

        // Call the per-file markQuizComplete() if it exists (each quiz file defines its own)
        if (typeof window.markQuizComplete === 'function') {
            window.markQuizComplete();
        } else {
            // Fallback: parse lesson info from URL and detect course
            const path = decodeURIComponent(window.location.pathname);
            const lessonMatch = path.match(/Lesson\s*(\d+)\.(\d+)_Quiz/);
            
            if (lessonMatch) {
                const unit = lessonMatch[1];
                const lesson = lessonMatch[2];
                
                // Detect course from path
                let coursePrefix = null;
                if (path.includes('Algebra1Lessons')) coursePrefix = 'alg1';
                else if (path.includes('Algebra2Lessons')) coursePrefix = 'alg2';
                else if (path.includes('GeometryLessons')) coursePrefix = 'geometry';
                else if (path.includes('PhysicsLessons')) coursePrefix = 'physics';
                else if (path.includes('ChemistryLessons')) coursePrefix = 'chem';
                else if (path.includes('BiologyLessons')) coursePrefix = 'bio';
                
                if (coursePrefix) {
                    localStorage.setItem(`${coursePrefix}_u${unit}_l${lesson}_completed`, 'true');
                }
            }
        }

        // Show detailed completion screen
        showQuizCompletionScreen();
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
            
            // 4. Initialize quiz analytics
            quizAnalytics.quizStartTime = Date.now();
            const questions = document.querySelectorAll('.quiz-question');
            quizAnalytics.totalQuestions = questions.length;
            
            // Pre-initialize analytics for each question
            let qIndex = 1;
            questions.forEach(q => {
                // Find the question name from input element
                const input = q.querySelector('input[type="radio"]');
                if (input) {
                    const qName = input.name;
                    quizAnalytics.questions[qName] = {
                        startTime: null,
                        endTime: null,
                        wrongAttempts: 0,
                        question: '',
                        correctText: ''
                    };
                    // Extract question text
                    const qText = q.querySelector('p');
                    if (qText) {
                        quizAnalytics.questions[qName].question = qText.textContent;
                    }
                }
            });
            
            // 5. Randomize Questions
            if (window.randomizeQuizQuestions) window.randomizeQuizQuestions();
            
            // 6. Scroll top
            window.scrollTo(0, 0);
        }
    });
    
})();
