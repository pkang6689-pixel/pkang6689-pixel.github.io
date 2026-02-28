
// Start of quiz logic
(function() {
    // MS Mode Detection — students from middle school courses get easier quizzes
    const _msOrigin = (sessionStorage.getItem('courseOrigin') || '');
    const isMS = _msOrigin.startsWith('ms_');
    const MS_ATTEMPTS = 3;   // MS students get 3 attempts (vs 2 for HS)
    const MS_MAX_QUESTIONS = 5; // MS quizzes show at most 5 questions

    // Quiz Analytics Tracking
    const quizAnalytics = {
        quizStartTime: null,
        quizEndTime: null,
        questions: {}, // { questionName: { startTime, endTime, wrongAttempts, correctText } }
        completedCount: 0,
        totalQuestions: 0
    };

    function _t(key, fallback) {
        var langMode = null;
        try { langMode = localStorage.getItem('arisEduLanguage'); } catch(e) {}
        
        // Default to English if no language preference
        var isChineseMode = (langMode === 'chinese' || langMode === 'traditional' || langMode === 'zh');
        
        if (!isChineseMode) {
            // English mode: return English (key itself as fallback)
            return fallback || key;
        }
        
        // Chinese mode: return Chinese translation
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

    // Show explanation modal for why no tokens were awarded (daily cap hit)
    function showTokenCapExplanation() {
        const explanationModal = document.createElement('div');
        explanationModal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(4px);
            z-index: 10001;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 1rem;
        `;

        const explanationBox = document.createElement('div');
        explanationBox.style.cssText = `
            background: ${document.body.classList.contains('dark-mode') ? '#1e293b' : 'white'};
            border-radius: 1rem;
            padding: 2rem;
            max-width: 480px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            color: ${document.body.classList.contains('dark-mode') ? '#e2e8f0' : '#0f172a'};
        `;

        explanationBox.innerHTML = `
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <div style="font-size: 3rem; margin-bottom: 0.5rem;">🎮</div>
                <h2 style="font-size: 1.5rem; font-weight: 700; margin: 0 0 0.5rem 0;">Daily Token Limit</h2>
            </div>
            <div style="background: ${document.body.classList.contains('dark-mode') ? '#334155' : '#f8fafc'}; border-radius: 0.75rem; padding: 1.25rem; margin-bottom: 1.5rem; line-height: 1.6;">
                <p style="margin: 0 0 1rem 0; color: ${document.body.classList.contains('dark-mode') ? '#cbd5e1' : '#475569'};">
                    <strong style="color: ${document.body.classList.contains('dark-mode') ? '#e2e8f0' : '#0f172a'};">You've already earned tokens for this lesson today!</strong>
                </p>
                <p style="margin: 0; color: ${document.body.classList.contains('dark-mode') ? '#cbd5e1' : '#475569'};">
                    Each lesson can award <strong style="color: ${document.body.classList.contains('dark-mode') ? '#22c55e' : '#16a34a'};">100 arcade tokens once per day</strong>. Come back tomorrow to earn tokens from this lesson again.
                </p>
            </div>
            <div style="background: ${document.body.classList.contains('dark-mode') ? '#14532d' : '#dcfce7'}; border-left: 4px solid ${document.body.classList.contains('dark-mode') ? '#22c55e' : '#16a34a'}; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1.5rem;">
                <div style="font-weight: 700; margin-bottom: 0.5rem; color: ${document.body.classList.contains('dark-mode') ? '#22c55e' : '#16a34a'};">💡 Pro Tip</div>
                <div style="font-size: 0.9rem; color: ${document.body.classList.contains('dark-mode') ? '#cbd5e1' : '#475569'};">
                    Try different lessons across your courses to keep earning tokens today!
                </div>
            </div>
            <button id="close-token-explanation" style="
                width: 100%;
                padding: 0.75rem;
                background: #3b82f6;
                color: white;
                border: none;
                border-radius: 0.5rem;
                font-weight: 600;
                font-size: 1rem;
                cursor: pointer;
            ">Got it!</button>
        `;

        explanationModal.appendChild(explanationBox);
        document.body.appendChild(explanationModal);

        // Close handlers
        const closeBtn = explanationBox.querySelector('#close-token-explanation');
        closeBtn.addEventListener('click', () => explanationModal.remove());
        explanationModal.addEventListener('click', (e) => {
            if (e.target === explanationModal) explanationModal.remove();
        });
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

        // ARCADE TOKENS SECTION (always shown, prominent)
        const tokensEarned = (typeof quizAnalytics.tokensAwarded === 'number') ? quizAnalytics.tokensAwarded : 0;
        const totalTokens = (typeof quizAnalytics.totalTokensAfter === 'number') ? quizAnalytics.totalTokensAfter : null;
        const earnedTokens = tokensEarned > 0;
        
        const arcadeBox = document.createElement('div');
        arcadeBox.style.cssText = `
            margin-bottom: 2rem;
            padding: 2rem;
            border-radius: 1.25rem;
            background: ${earnedTokens 
                ? (document.body.classList.contains('dark-mode') ? 'linear-gradient(135deg, #14532d 0%, #166534 100%)' : 'linear-gradient(135deg, #dcfce7 0%, #bbf7d0 100%)')
                : (document.body.classList.contains('dark-mode') ? '#334155' : '#f1f5f9')
            };
            border: 3px solid ${earnedTokens 
                ? (document.body.classList.contains('dark-mode') ? '#22c55e' : '#16a34a')
                : (document.body.classList.contains('dark-mode') ? '#475569' : '#cbd5e1')
            };
            text-align: center;
            position: relative;
        `;

        const tokenDisplayHTML = earnedTokens
            ? `
                <div style="font-size: 4rem; margin-bottom: 0.5rem;">🎮</div>
                <div style="font-size: 2.5rem; font-weight: 900; color: ${document.body.classList.contains('dark-mode') ? '#22c55e' : '#16a34a'}; margin-bottom: 0.5rem; text-shadow: 0 2px 8px rgba(0,0,0,0.1);">
                    +${tokensEarned} Arcade Tokens!
                </div>
                ${totalTokens !== null ? `<div style="font-size: 1.1rem; opacity: 0.85; color: ${document.body.classList.contains('dark-mode') ? '#e2e8f0' : '#475569'};">Total: ${totalTokens} 💎</div>` : ''}
            `
            : `
                <div style="font-size: 3.5rem; margin-bottom: 0.5rem; opacity: 0.6;">🎮</div>
                <div style="display: flex; align-items: center; justify-content: center; gap: 0.75rem; margin-bottom: 0.5rem;">
                    <div style="font-size: 2rem; font-weight: 900; color: ${document.body.classList.contains('dark-mode') ? '#94a3b8' : '#64748b'};">
                        +0 Arcade Tokens
                    </div>
                    <button id="token-cap-help-btn" style="width: 2rem; height: 2rem; border-radius: 50%; background: ${document.body.classList.contains('dark-mode') ? '#475569' : '#e2e8f0'}; color: ${document.body.classList.contains('dark-mode') ? '#e2e8f0' : '#475569'}; border: 2px solid ${document.body.classList.contains('dark-mode') ? '#64748b' : '#94a3b8'}; font-size: 1.2rem; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; line-height: 1;">?</button>
                </div>
                <div style="font-size: 0.95rem; opacity: 0.75; color: ${document.body.classList.contains('dark-mode') ? '#cbd5e1' : '#64748b'}; margin-bottom: 0.5rem;">Already earned today</div>
                ${totalTokens !== null ? `<div style="font-size: 1rem; opacity: 0.7; color: ${document.body.classList.contains('dark-mode') ? '#94a3b8' : '#64748b'};">Current balance: ${totalTokens} 💎</div>` : ''}
            `;

        arcadeBox.innerHTML = tokenDisplayHTML;
        content.appendChild(arcadeBox);

        // Add help modal for token cap explanation (shown when button clicked)
        if (!earnedTokens) {
            setTimeout(() => {
                const helpBtn = document.getElementById('token-cap-help-btn');
                if (helpBtn) {
                    helpBtn.addEventListener('click', (e) => {
                        e.stopPropagation();
                        showTokenCapExplanation();
                    });
                }
            }, 0);
        }

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

        const retakeBtn = document.createElement('button');
        retakeBtn.textContent = '↻ Retake Quiz';
        retakeBtn.style.cssText = `
            padding: 0.75rem 1.5rem;
            background: #3b82f6;
            color: white;
            border: none;
            border-radius: 0.5rem;
            font-weight: 600;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.2s;
        `;
        retakeBtn.onmouseover = () => retakeBtn.style.background = '#2563eb';
        retakeBtn.onmouseout = () => retakeBtn.style.background = '#3b82f6';
        retakeBtn.onclick = () => {
            modal.remove();
            location.reload();
        };

        buttonContainer.appendChild(retakeBtn);
        buttonContainer.appendChild(closeBtn);
        buttonContainer.appendChild(continueBtn);
        content.appendChild(buttonContainer);

        modal.appendChild(content);
        document.body.appendChild(modal);
    }
    // Helper: get practice file URL from current quiz URL
    function getPracticeFileUrl() {
        var path = window.location.pathname;
        if (path.indexOf('_Quiz.html') !== -1) {
            return path.replace('_Quiz.html', '_Practice.html');
        }
        // Legacy space-separated names
        if (path.indexOf(' Quiz.html') !== -1) {
            return path.replace(' Quiz.html', ' Practice.html');
        }
        return null;
    }

    // Helper: get localStorage key for current lesson quiz
    function getLessonQuizStorageKey() {
        var path = decodeURIComponent(window.location.pathname);
        var match = path.match(/Lesson\s*(\d+)\.(\d+)/);
        if (!match) return null;
        var unit = match[1], lesson = match[2];
        var prefix = 'chem';
        if (path.indexOf('Physics') !== -1) prefix = 'physics';
        else if (path.indexOf('Algebra1') !== -1) prefix = 'alg1';
        else if (path.indexOf('Algebra2') !== -1) prefix = 'alg2';
        else if (path.indexOf('Geometry') !== -1) prefix = 'geometry';
        else if (path.indexOf('Biology') !== -1) prefix = 'bio';
        return prefix + '_u' + unit + '_l' + lesson + '_completed';
    }

    function getLocalDateStamp() {
        const now = new Date();
        const year = now.getFullYear();
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const day = String(now.getDate()).padStart(2, '0');
        return `${year}-${month}-${day}`;
    }

    function getLessonDailyRewardStorageKey() {
        const completionKey = getLessonQuizStorageKey();
        if (!completionKey) return null;
        return completionKey.replace(/_completed$/, '_rewarded_date');
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
            // Navigate to separate practice file
            var practiceUrl = getPracticeFileUrl();
            if (practiceUrl) {
                window.location.href = practiceUrl;
            } else {
                // Fallback: try finding a practice link in the page
                const practiceLink = document.querySelector('a[href*="Practice.html"]');
                if(practiceLink) {
                    location.href = practiceLink.href;
                }
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

    // Only define checkQuizAnswer if quiz_logic.js hasn't already defined it
    // quiz_logic.js handles unit tests (value="a","b","c","d"), quiz_ui.js handles lesson quizzes (value="correct","wrong")
    if (!window.checkQuizAnswer) {
    window.checkQuizAnswer = function(name, correct, btn) {
        try {
            const parent = btn.closest('.quiz-question');
            if(!parent) return;

            // Track question interaction
            trackQuestionStart(name);
            
            // Get or Init Attempts — MS students get 3 attempts
            let attemptsElem = parent.querySelector('.attempts-indicator');
            if (!attemptsElem) return;
            
            const defaultAttempts = isMS ? MS_ATTEMPTS : 2;
            let attempts = parseInt(parent.dataset.attempts || String(defaultAttempts));

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
                feedback.textContent = _t("Please select an answer first.", "Please select an answer first.");
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
                attemptsElem.textContent = _t("Attempts left:", "Attempts left:") + " " + attempts;
                attemptsElem.style.display = 'block';

                // MS Mode: eliminate one wrong option after each wrong answer
                if (isMS && attempts > 0) {
                    const wrongInputs = Array.from(parent.querySelectorAll(`input[name="${name}"][value="wrong"]`));
                    const eliminable = wrongInputs.filter(i => {
                        const lbl = i.closest('label') || i.parentElement;
                        return !lbl.classList.contains('ms-eliminated') && !i.checked;
                    });
                    if (eliminable.length > 0) {
                        const pick = eliminable[Math.floor(Math.random() * eliminable.length)];
                        const lbl = pick.closest('label') || pick.parentElement;
                        lbl.classList.add('ms-eliminated');
                        lbl.style.opacity = '0.35';
                        lbl.style.textDecoration = 'line-through';
                        lbl.style.pointerEvents = 'none';
                        pick.disabled = true;
                    }
                }

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
                     feedback.textContent = _t("Incorrect. Try again!", "Incorrect. Try again!");
                     feedback.style.color = "#dc2626";
                     feedback.style.background = "#fee2e2";
                }
            }
        } catch (e) {
            console.error("Quiz Error:", e);
        }
    };
    } // end if (!window.checkQuizAnswer)

    // Award arcade tokens once per lesson per day
    function awardLessonTokensIfFirstCompletion() {
        if (typeof getLessonDailyRewardStorageKey !== 'function' || typeof getLessonQuizStorageKey !== 'function') return;

        const completionKey = getLessonQuizStorageKey();
        const dailyRewardKey = getLessonDailyRewardStorageKey();
        if (!completionKey || !dailyRewardKey) return;

        const today = getLocalDateStamp();

        let alreadyRewardedToday = false;
        try {
            alreadyRewardedToday = (localStorage.getItem(dailyRewardKey) === today);
        } catch (e) {
            alreadyRewardedToday = false;
        }

        // If this lesson has already rewarded tokens today, do not award again
        if (alreadyRewardedToday) {
            quizAnalytics.tokensAwarded = 0;
            // Still get the current token balance to show in the completion screen
            try {
                const user = JSON.parse(localStorage.getItem('user') || '{}');
                quizAnalytics.totalTokensAfter = parseInt(user.points || '0', 10) || 0;
            } catch (e) {
                quizAnalytics.totalTokensAfter = 0;
            }
            return;
        }

        // Award 100 arcade tokens and mark lesson as completed + rewarded today
        let user = {};
        try {
            user = JSON.parse(localStorage.getItem('user') || '{}');
        } catch (e) {
            user = {};
        }

        const currentPoints = parseInt(user.points || '0', 10) || 0;
        const reward = 100;
        user.points = currentPoints + reward;

        try {
            localStorage.setItem('user', JSON.stringify(user));
            localStorage.setItem(completionKey, 'true');
            
            // Mirror HS completion to MS lesson (one-way: HS→MS only)
            mirrorHSToMSCompletion();
            
            localStorage.setItem(dailyRewardKey, today);
        } catch (e) {
            // If storage fails, just skip without breaking quiz flow
        }

        quizAnalytics.tokensAwarded = reward;
        quizAnalytics.totalTokensAfter = user.points;
    }

    // Mirror HS lesson completion to MS lesson (one-way: HS→MS only)
    // When an HS student completes a lesson, mark the corresponding MS lesson as complete too
    function mirrorHSToMSCompletion() {
        // Only mirror for HS students (MS students completing should NOT affect HS)
        if (isMS) return;

        try {
            const completionKey = getLessonQuizStorageKey();
            if (!completionKey) return;

            // Parse the lesson info from the current URL
            const path = decodeURIComponent(window.location.pathname);
            const lessonMatch = path.match(/Lesson\s*(\w+)\.(\d+)_Quiz/);
            if (!lessonMatch) return;

            const unit = lessonMatch[1];
            const lesson = lessonMatch[2];

            // Determine course and MS prefix
            let folder = null;
            let msPrefix = null;

            if (path.includes('Algebra1Lessons'))      { folder = 'Algebra1Lessons'; msPrefix = 'ms_alg1'; }
            else if (path.includes('Algebra2Lessons')) { folder = 'Algebra2Lessons'; msPrefix = 'ms_alg2'; }
            else if (path.includes('GeometryLessons')) { folder = 'GeometryLessons'; msPrefix = 'ms_geom'; }
            else if (path.includes('PhysicsLessons'))  { folder = 'PhysicsLessons';  msPrefix = 'ms_phys'; }
            else if (path.includes('ChemistryLessons')){ folder = 'ChemistryLessons'; msPrefix = 'ms_chem'; }
            else if (path.includes('BiologyLessons'))  { folder = 'BiologyLessons';  msPrefix = 'ms_bio'; }

            if (!folder || !msPrefix) return;

            // Look up the MS mapping (created when MS page was visited)
            const msMap = JSON.parse(localStorage.getItem('_msMap_' + folder) || '{}');
            const msEntry = msMap[unit + '_' + lesson];

            if (msEntry) {
                // Parse MS unit and lesson (handle units like "5A" with underscores)
                const mp = msEntry.split('_');
                const msUnit = mp[0];
                const msLesson = mp.slice(1).join('_');
                const msCompletionKey = msPrefix + '_u' + msUnit + '_l' + msLesson + '_completed';

                // Mark corresponding MS lesson as complete
                localStorage.setItem(msCompletionKey, 'true');
            }
        } catch (e) {
            // Silently fail if mirroring doesn't work (don't break quiz flow)
            console.debug('Error mirroring HS completion to MS:', e);
        }
    }

    // Check if every question on the quiz has been answered correctly
    function checkQuizCompletion() {
        // Only check visible questions (MS mode may hide some)
        const questions = Array.from(document.querySelectorAll('.quiz-question')).filter(q => q.style.display !== 'none');
        if (questions.length === 0) return;

        const allCorrect = Array.from(questions).every(q => {
            const fb = q.querySelector('.feedback');
            return fb && (fb.textContent.startsWith('Correct') || fb.textContent.startsWith(_t('Correct')));
        });
        if (!allCorrect) return;

        // Record quiz end time
        quizAnalytics.quizEndTime = Date.now();

        // Award tokens (only on first completion of this lesson)
        awardLessonTokensIfFirstCompletion();

        // Call the per-file markQuizComplete() if it exists (each quiz file defines its own)
        if (typeof window.markQuizComplete === 'function') {
            window.markQuizComplete();
        } else {
            // Fallback: parse lesson info from URL and detect course
            const path = decodeURIComponent(window.location.pathname);
            const lessonMatch = path.match(/Lesson\s*(\w+)\.(\d+)_Quiz/);
            
            if (lessonMatch) {
                const unit = lessonMatch[1];
                const lesson = lessonMatch[2];
                
                // Detect course from path
                let coursePrefix = null;
                let msPrefix = null;
                if (path.includes('Algebra1Lessons'))      { coursePrefix = 'alg1';     msPrefix = 'ms_alg1'; }
                else if (path.includes('Algebra2Lessons')) { coursePrefix = 'alg2';     msPrefix = 'ms_alg2'; }
                else if (path.includes('GeometryLessons')) { coursePrefix = 'geometry'; msPrefix = 'ms_geom'; }
                else if (path.includes('PhysicsLessons'))  { coursePrefix = 'physics';  msPrefix = 'ms_phys'; }
                else if (path.includes('ChemistryLessons')){ coursePrefix = 'chem';     msPrefix = 'ms_chem'; }
                else if (path.includes('BiologyLessons'))  { coursePrefix = 'bio';      msPrefix = 'ms_bio'; }
                
                if (coursePrefix) {
                    if (isMS) {
                        // MS student: write MS key only (do NOT write HS key)
                        if (msPrefix) {
                            try {
                                var folder = path.match(/(Algebra1Lessons|Algebra2Lessons|GeometryLessons|PhysicsLessons|ChemistryLessons|BiologyLessons)/);
                                if (folder) {
                                    var msMap = JSON.parse(localStorage.getItem('_msMap_' + folder[1]) || '{}');
                                    var msEntry = msMap[unit + '_' + lesson];
                                    if (msEntry) {
                                        var mp = msEntry.split('_');
                                        localStorage.setItem(msPrefix + '_u' + mp[0] + '_l' + mp.slice(1).join('_') + '_completed', 'true');
                                    }
                                }
                            } catch(e) {}
                        }
                    } else {
                        // HS student: write HS key + also mirror to MS
                        localStorage.setItem(`${coursePrefix}_u${unit}_l${lesson}_completed`, 'true');
                        if (msPrefix) {
                            try {
                                var folder = path.match(/(Algebra1Lessons|Algebra2Lessons|GeometryLessons|PhysicsLessons|ChemistryLessons|BiologyLessons)/);
                                if (folder) {
                                    var msMap = JSON.parse(localStorage.getItem('_msMap_' + folder[1]) || '{}');
                                    var msEntry = msMap[unit + '_' + lesson];
                                    if (msEntry) {
                                        var mp = msEntry.split('_');
                                        localStorage.setItem(msPrefix + '_u' + mp[0] + '_l' + mp.slice(1).join('_') + '_completed', 'true');
                                    }
                                }
                            } catch(e) {}
                        }
                    }
                }
            }
        }

        // Show detailed completion screen
        showQuizCompletionScreen();
    }

    function showCompletionScreenFromAlreadyCompleted() {
        const now = Date.now();
        const visibleQuestions = Array.from(document.querySelectorAll('.quiz-question')).filter(q => q.style.display !== 'none');

        if (!quizAnalytics.quizStartTime) quizAnalytics.quizStartTime = now;
        quizAnalytics.quizEndTime = now;
        quizAnalytics.tokensAwarded = 0;
        quizAnalytics.totalTokensAfter = undefined;

        if (!quizAnalytics.totalQuestions || quizAnalytics.totalQuestions <= 0) {
            quizAnalytics.totalQuestions = visibleQuestions.length || 1;
        }

        if (!quizAnalytics.questions || Object.keys(quizAnalytics.questions).length === 0) {
            quizAnalytics.questions = {};
            visibleQuestions.forEach((q, index) => {
                const input = q.querySelector('input[type="radio"]');
                const name = input ? input.name : ('q' + (index + 1));
                const qText = q.querySelector('p');
                quizAnalytics.questions[name] = {
                    startTime: now,
                    endTime: now,
                    wrongAttempts: 0,
                    question: qText ? qText.textContent : '',
                    correctText: ''
                };
            });
        } else {
            Object.keys(quizAnalytics.questions).forEach((name) => {
                if (!quizAnalytics.questions[name].startTime) quizAnalytics.questions[name].startTime = now;
                if (!quizAnalytics.questions[name].endTime) quizAnalytics.questions[name].endTime = now;
                if (typeof quizAnalytics.questions[name].wrongAttempts !== 'number') quizAnalytics.questions[name].wrongAttempts = 0;
            });
        }

        const alreadyModal = document.getElementById('already-completed-modal');
        if (alreadyModal) alreadyModal.remove();
        showQuizCompletionScreen();
    }
    
    // Expose checkQuizCompletion to window ONLY if it hasn't been defined by unit_test.js
    // This prevents overriding the unit test version on unit test pages
    if (!window.checkQuizCompletion) {
        window.checkQuizCompletion = checkQuizCompletion;
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
        p.dataset.attempts = isMS ? String(MS_ATTEMPTS) : '2';
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

        // Reset MS eliminated labels
        p.querySelectorAll('.ms-eliminated').forEach(lbl => {
            lbl.classList.remove('ms-eliminated');
            lbl.style.opacity = '';
            lbl.style.textDecoration = '';
            lbl.style.pointerEvents = '';
            const inp = lbl.querySelector('input');
            if (inp) inp.disabled = false;
        });

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
        const fileName = decodeURIComponent(path.split('/').pop() || '');
        // Check if we are on a lesson Quiz page (Lesson X.Y_Quiz.html), not a Unit test page
        const isLessonQuiz = (fileName.endsWith('Quiz.html') || fileName.indexOf('Quiz.html') !== -1) && fileName.indexOf('Unit') === -1;
        if (isLessonQuiz) {
            // Check if already completed
            var quizKey = getLessonQuizStorageKey();
            if (quizKey && localStorage.getItem(quizKey) === 'true') {
                // Show already completed modal
                const modal = document.createElement('div');
                modal.id = 'already-completed-modal';
                modal.style.cssText = 'position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(15,23,42,0.95);backdrop-filter:blur(4px);z-index:10000;display:flex;align-items:center;justify-content:center;padding:1rem;';
                const box = document.createElement('div');
                box.style.cssText = 'background:white;border-radius:1.5rem;padding:2.5rem;max-width:420px;width:100%;text-align:center;box-shadow:0 25px 50px -12px rgba(0,0,0,0.25);';
                if (document.body.classList.contains('dark-mode')) { box.style.background = '#1e293b'; box.style.color = '#e2e8f0'; }
                box.innerHTML = '<h2 style="font-size:2rem;margin-bottom:1rem;">\u2705 Already Completed!</h2><p style="color:#64748b;margin-bottom:2rem;">You\'ve already passed this quiz.<br>Arcade tokens reset daily for each lesson, so you can earn again tomorrow.</p><div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;"></div>';
                var btnContainer = box.querySelector('div:last-child');
                var retakeBtn = document.createElement('button');
                retakeBtn.textContent = '\u21BB Retake Quiz';
                retakeBtn.style.cssText = 'padding:0.75rem 1.5rem;background:#3b82f6;color:white;border:none;border-radius:0.5rem;font-weight:600;cursor:pointer;font-size:1rem;';
                retakeBtn.onclick = function() { var key = getLessonQuizStorageKey(); if (key) localStorage.removeItem(key); location.reload(); };
                var practiceBtn = document.createElement('button');
                practiceBtn.textContent = '\uD83D\uDCDD Go to Practice';
                practiceBtn.style.cssText = 'padding:0.75rem 1.5rem;background:#10b981;color:white;border:none;border-radius:0.5rem;font-weight:600;cursor:pointer;font-size:1rem;';
                practiceBtn.onclick = function() { var url = getPracticeFileUrl(); if (url) window.location.href = url; };
                var completeBtn = document.createElement('button');
                completeBtn.textContent = '\uD83D\uDCCA Show Complete Screen';
                completeBtn.style.cssText = 'padding:0.75rem 1.5rem;background:#8b5cf6;color:white;border:none;border-radius:0.5rem;font-weight:600;cursor:pointer;font-size:1rem;';
                completeBtn.onclick = function() { showCompletionScreenFromAlreadyCompleted(); };
                btnContainer.appendChild(retakeBtn);
                btnContainer.appendChild(practiceBtn);
                btnContainer.appendChild(completeBtn);
                modal.appendChild(box);
                document.body.appendChild(modal);
            }
        }
        if (isLessonQuiz) {
            
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
            
            // 5a. MS Mode: remove HS-only questions before shuffling
            if (isMS) {
                document.querySelectorAll('.quiz-question[data-hs-only="true"]').forEach(function(q) { q.remove(); });
            }

            // 5. Randomize Questions (shuffle BEFORE MS mode hides extras)
            if (window.randomizeQuizQuestions) window.randomizeQuizQuestions();

            // 6. MS Mode: limit visible questions, set extra attempts, show badge
            if (isMS) {
                const allQ = Array.from(document.querySelectorAll('.quiz-question'));
                if (allQ.length > MS_MAX_QUESTIONS) {
                    allQ.slice(MS_MAX_QUESTIONS).forEach(q => { q.style.display = 'none'; });
                }
                allQ.filter(q => q.style.display !== 'none').forEach(q => {
                    q.dataset.attempts = String(MS_ATTEMPTS);
                });
                // Re-number visible questions
                let visNum = 1;
                allQ.filter(q => q.style.display !== 'none').forEach(q => {
                    const p = q.querySelector('p');
                    if (p) p.textContent = p.textContent.replace(/^\d+\.\s*/, `${visNum++}. `);
                });
                // Inject MS mode badge
                const qv = document.getElementById('quiz-content-view');
                if (qv) {
                    const badge = document.createElement('div');
                    badge.style.cssText = 'background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;padding:0.5rem 1rem;border-radius:0.5rem;font-size:0.85rem;font-weight:700;display:inline-flex;align-items:center;gap:0.4rem;margin-bottom:1rem;';
                    badge.innerHTML = '📘 Middle School Mode &mdash; 3 attempts per question, wrong answers eliminated';
                    const titleEl = qv.querySelector('.page-title');
                    if (titleEl) titleEl.after(badge);
                    else qv.prepend(badge);
                }
            }

            quizAnalytics.totalQuestions = Array.from(document.querySelectorAll('.quiz-question')).filter(q => q.style.display !== 'none').length;
            
            // 7. Scroll top
            window.scrollTo(0, 0);
        }
    });
    
})();
