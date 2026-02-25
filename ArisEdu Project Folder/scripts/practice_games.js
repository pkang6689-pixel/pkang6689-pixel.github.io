
// Toggle Practices Panel
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
var _tr = function(t) { return (window.arisTranslate ? window.arisTranslate(t) : t); };
window.togglePracticesPanel = function(button) {
    if (!button) return;
    const menu = button.closest('.Practices-menu') || button.closest('.side-buttons'); 
    if (!menu) return;
    const panel = menu.querySelector('.Practices-panel');
    if (!panel) return;
    const isOpen = panel.classList.toggle('is-open');
    panel.setAttribute('aria-hidden', (!isOpen).toString());
};

// ========== VIEW SWITCHING LOGIC ==========
window.toggleToSummary = function(event) {
    if (event) event.preventDefault();
    const lessonView = document.getElementById('lesson-content-view');
    const practiceView = document.getElementById('practice-content-view');
    const summaryView = document.getElementById('summary-content-view');
    const quizView = document.getElementById('quiz-content-view');
    if (lessonView) lessonView.style.display = 'none';
    if (practiceView) practiceView.style.display = 'none';
    if (quizView) quizView.style.display = 'none';
    if (summaryView) summaryView.style.display = 'block';
    if (window.randomizeQuizQuestions) window.randomizeQuizQuestions();
    window.scrollTo(0, 0);
};

window.toggleToPractice = function(event) {
    if (event) event.preventDefault();
    const lessonView = document.getElementById('lesson-content-view');
    const practiceView = document.getElementById('practice-content-view');
    const summaryView = document.getElementById('summary-content-view');
    const quizView = document.getElementById('quiz-content-view');
    if (lessonView) lessonView.style.display = 'none';
    if (summaryView) summaryView.style.display = 'none';
    if (quizView) quizView.style.display = 'none';
    if (practiceView) practiceView.style.display = 'block';
    if (typeof window.initFlashcards === 'function') {
        try { window.initFlashcards(); } catch (err) { console.error("Error initializing flashcards:", err); }
    }
    if (window.randomizeQuizQuestions) window.randomizeQuizQuestions();
    window.scrollTo(0, 0);
};

window.toggleToQuiz = function(event) {
    window.usedFlashcardIndices = [];
    if (event) event.preventDefault();
    const lessonView = document.getElementById('lesson-content-view');
    const practiceView = document.getElementById('practice-content-view');
    const summaryView = document.getElementById('summary-content-view');
    const quizView = document.getElementById('quiz-content-view');
    if (lessonView) lessonView.style.display = 'none';
    if (practiceView) practiceView.style.display = 'none';
    if (summaryView) summaryView.style.display = 'none';
    if (quizView) quizView.style.display = 'block';
    if (window.randomizeQuizQuestions) window.randomizeQuizQuestions();
    window.scrollTo(0, 0);
};

window.randomizeQuizQuestions = function() {
    const form = document.getElementById('quiz-form');
    if (!form) return;
    let questions = Array.from(form.querySelectorAll('.quiz-question'));
    if (questions.length === 0) return;
    if (form.dataset.shuffled === 'true') return;
    for (let i = questions.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [questions[i], questions[j]] = [questions[j], questions[i]];
    }
    const selected = questions.slice(0, 5);
    form.innerHTML = '';
    selected.forEach((q, index) => {
        const p = q.querySelector('p');
        if (p) p.textContent = p.textContent.replace(/^\d+\.\s*/, `${index + 1}. `);
        form.appendChild(q);
    });
    form.dataset.shuffled = 'true';
};

window.checkQuizAnswer = function(name, correct, btn) {
    const parent = btn.closest('.quiz-question');
    if (!parent) return;
    let attemptsElem = parent.querySelector('.attempts-indicator');
    if (!attemptsElem) return;
    let attempts = parseInt(parent.dataset.attempts || '2');
    const selected = parent.querySelector(`input[name="${name}"]:checked`);
    let feedback = parent.querySelector('.feedback');
    if (!feedback) {
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
        const msg = (window.globalTranslations && window.globalTranslations["Correct! Great job."]) || "Correct! Great job.";
        feedback.textContent = msg;
        feedback.style.color = "#16a34a";
        feedback.style.background = "#dcfce7";
        btn.disabled = true;
        parent.querySelectorAll('input').forEach(i => i.disabled = true);
        attemptsElem.style.display = 'none';
    } else {
        attempts--;
        parent.dataset.attempts = attempts;
        const attemptsPrefix = (window.globalTranslations && window.globalTranslations["Attempts left:"]) || "Attempts left:";
        attemptsElem.textContent = `${attemptsPrefix} ${attempts}`;
        if (attempts <= 0) {
            const prefix = (window.globalTranslations && window.globalTranslations["Incorrect. The correct answer was option"]) || "Incorrect. The correct answer was option";
            feedback.textContent = `${prefix} ${correct.toUpperCase()}.`;
            feedback.style.color = "#dc2626";
            feedback.style.background = "#fee2e2";
            btn.disabled = true;
            parent.querySelectorAll('input').forEach(i => i.disabled = true);
        } else {
            const msg = (window.globalTranslations && window.globalTranslations["Incorrect. Try again!"]) || "Incorrect. Try again!";
            feedback.textContent = msg;
            feedback.style.color = "#dc2626";
            feedback.style.background = "#fee2e2";
        }
    }
};

// Global Click Delegation for Game Switching
window.attachPracticeListeners = function() {
    console.log("Setting up Global Delegated Event Listeners for Practice Games...");
    
    // Remove old listeners if possible? (Hard with anonymous functions, but we use a flag)
    if (window._practiceListenersAttached) return;
    window._practiceListenersAttached = true;

    document.addEventListener('click', function(e) {
        // Look for anchor tag with href starting with #
        const link = e.target.closest('a[href^="#"]');
        if (!link) return;
        
        const href = link.getAttribute('href');
        let matched = false;
        
        if (href === '#mixmatch') {
            console.log("Delegated Click: Mix & Match");
            window.switchToMixMatch();
            matched = true;
        } else if (href === '#climb') {
            console.log("Delegated Click: Climb");
            window.switchToClimb();
            matched = true;
        } else if (href === '#blockpuzzle') {
            console.log("Delegated Click: Block Puzzle");
            window.switchToBlockPuzzle();
            matched = true;
        } else if (href === '#flashcard-game') {
            console.log("Delegated Click: Flashcards");
            window.switchToFlashcards();
            matched = true;
        }

        if (matched) {
            e.preventDefault();
            // Handle Dropdown Menu Toggling
            if (window.togglePracticesPanel && link.closest('.Practices-menu')) {
                const btn = link.closest('.Practices-menu').querySelector('.view-other-Practices');
                if(btn) window.togglePracticesPanel(btn);
            }
        }
    });
};

// ========== CLEAN GAME SWITCHERS ==========
// Helper: Hide all game containers
function hideAllGameContainers() {
    ['flashcard-game', 'climb-game-container', 'mixmatch-container', 'blockpuzzle-container'].forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.setProperty('display', 'none', 'important');
    });
}

window.switchToFlashcards = function() {
    console.log("Switching to Flashcards");
    hideAllGameContainers();
    const el = document.getElementById('flashcard-game');
    if (el) el.style.setProperty('display', 'flex', 'important');
    if (typeof window.initFlashcards === 'function') window.initFlashcards();
};

window.switchToClimb = function() {
    console.log("Switching to Climb");
    hideAllGameContainers();
    const el = document.getElementById('climb-game-container');
    if (el) el.style.setProperty('display', 'block', 'important');
    if (typeof window.initClimbGame === 'function') window.initClimbGame();
};

window.switchToMixMatch = function() {
    console.log("Switching to Mix & Match");
    hideAllGameContainers();
    const el = document.getElementById('mixmatch-container');
    if (el) el.style.setProperty('display', 'flex', 'important');
    if (typeof window.initMixMatch === 'function') window.initMixMatch();
};

window.switchToBlockPuzzle = function() {
    console.log("Switching to Block Puzzle");
    hideAllGameContainers();
    const el = document.getElementById('blockpuzzle-container');
    if (el) el.style.setProperty('display', 'flex', 'important');
    if (typeof window.initBlockPuzzle === 'function') window.initBlockPuzzle();
};

// ========== FLASHCARD GAME LOGIC ==========
window.flashcardsInitialized = false;
window.initFlashcards = function() {
    if (window.flashcardsInitialized) return;

    if (!window.lessonFlashcards || window.lessonFlashcards.length === 0) {
        console.warn("window.lessonFlashcards is empty or undefined. Flashcards will not load.");
        return;
    }

    const flashcards = window.lessonFlashcards;
    let currentFlashcard = 0;
    let flashcardOrder = [...Array(flashcards.length).keys()];

    const flashcardContent = document.getElementById('flashcard-content');
    const flashcardDiv = document.getElementById('flashcard');
    const nextFlashcardBtn = document.getElementById('next-flashcard');
    const prevFlashcardBtn = document.getElementById('prev-flashcard');
    const shuffleFlashcardBtn = document.getElementById('shuffle-flashcard');
    const flashcardCounter = document.getElementById('flashcard-counter');

    if (!flashcardContent || !flashcardDiv || !nextFlashcardBtn || !prevFlashcardBtn || !shuffleFlashcardBtn) {
        return;
    }

    let showingAnswer = false;
    let cardsViewed = 1;
    const viewedSet = new Set([flashcardOrder[currentFlashcard]]);

    function updateCounter() {
        if (flashcardCounter) {
            flashcardCounter.textContent = cardsViewed + ' / ' + flashcards.length;
        }
    }

    function trackViewed() {
        const idx = flashcardOrder[currentFlashcard];
        if (!viewedSet.has(idx)) {
            viewedSet.add(idx);
            cardsViewed = viewedSet.size;
        }
    }

    function updateFlashcard() {
        showingAnswer = false;
        const idx = flashcardOrder[currentFlashcard];
        const rawText = flashcards[idx].question;
        const text = (typeof window.arisTranslate === 'function') ? window.arisTranslate(rawText) : rawText;
        flashcardContent.textContent = text;
        autoAdjustFontSize(text);
        trackViewed();
        updateCounter();
    }

    function autoAdjustFontSize(text) {
        if (!flashcardContent) return;
        let length = text.length;
        let size;
        if (length < 60) size = 2.5;
        else if (length < 120) size = 1.5;
        else if (length < 200) size = 1.1;
        else size = 0.8;
        flashcardContent.style.fontSize = size + 'rem';
    }

    let isFlipping = false;

    // Flip card on click
    flashcardDiv.addEventListener('click', () => {
        if (isFlipping) return;
        isFlipping = true;
        const direction = !showingAnswer ? 1 : -1;
        flashcardDiv.style.transition = "transform 0.15s ease-in, background 0.2s, color 0.2s";
        flashcardDiv.style.transform = `rotateX(${90 * direction}deg)`;
        setTimeout(() => {
            const idx = flashcardOrder[currentFlashcard];
            if (!showingAnswer) {
                const answerText = (typeof window.arisTranslate === 'function') ? window.arisTranslate(flashcards[idx].answer) : flashcards[idx].answer;
                flashcardContent.textContent = answerText;
                autoAdjustFontSize(answerText);
                showingAnswer = true;
            } else {
                const questionText = (typeof window.arisTranslate === 'function') ? window.arisTranslate(flashcards[idx].question) : flashcards[idx].question;
                flashcardContent.textContent = questionText;
                autoAdjustFontSize(questionText);
                showingAnswer = false;
            }
            flashcardDiv.style.transition = "none";
            flashcardDiv.style.transform = `rotateX(${-90 * direction}deg)`;
            void flashcardDiv.offsetWidth;
            flashcardDiv.style.transition = "transform 0.15s ease-out, background 0.2s, color 0.2s";
            flashcardDiv.style.transform = "rotateX(0deg)";
            setTimeout(() => { isFlipping = false; }, 150);
        }, 150);
    });

    // Next card
    nextFlashcardBtn.addEventListener('click', () => {
        if (isFlipping) return;
        isFlipping = true;
        flashcardDiv.style.transition = "transform 0.25s ease-in, opacity 0.25s ease-in";
        flashcardDiv.style.transform = "translateX(-120%) rotate(-10deg)";
        flashcardDiv.style.opacity = "0";
        setTimeout(() => {
            currentFlashcard = (currentFlashcard + 1) % flashcardOrder.length;
            updateFlashcard();
            flashcardDiv.style.transition = "none";
            flashcardDiv.style.transform = "translateX(120%) rotate(10deg)";
            void flashcardDiv.offsetWidth;
            flashcardDiv.style.transition = "transform 0.25s ease-out, opacity 0.25s ease-out, background 0.2s, color 0.2s";
            flashcardDiv.style.transform = "translateX(0) rotate(0)";
            flashcardDiv.style.opacity = "1";
            setTimeout(() => { isFlipping = false; }, 250);
        }, 250);
    });

    // Prev card
    prevFlashcardBtn.addEventListener('click', () => {
        if (isFlipping) return;
        isFlipping = true;
        flashcardDiv.style.transition = "transform 0.25s ease-in, opacity 0.25s ease-in";
        flashcardDiv.style.transform = "translateX(120%) rotate(10deg)";
        flashcardDiv.style.opacity = "0";
        setTimeout(() => {
            currentFlashcard = (currentFlashcard - 1 + flashcardOrder.length) % flashcardOrder.length;
            updateFlashcard();
            flashcardDiv.style.transition = "none";
            flashcardDiv.style.transform = "translateX(-120%) rotate(-10deg)";
            void flashcardDiv.offsetWidth;
            flashcardDiv.style.transition = "transform 0.25s ease-out, opacity 0.25s ease-out, background 0.2s, color 0.2s";
            flashcardDiv.style.transform = "translateX(0) rotate(0)";
            flashcardDiv.style.opacity = "1";
            setTimeout(() => { isFlipping = false; }, 250);
        }, 250);
    });

    // Shuffle
    shuffleFlashcardBtn.addEventListener('click', () => {
        if (isFlipping) return;
        isFlipping = true;
        const lastCardIdx = flashcardOrder[currentFlashcard];
        function shuffleArray(array) {
            let arr = array.slice();
            for (let i = arr.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [arr[i], arr[j]] = [arr[j], arr[i]];
            }
            return arr;
        }
        flashcardOrder = shuffleArray(flashcardOrder);
        if (flashcardOrder.length > 1 && flashcardOrder[0] === lastCardIdx) {
            [flashcardOrder[0], flashcardOrder[1]] = [flashcardOrder[1], flashcardOrder[0]];
        }
        currentFlashcard = 0;

        const container = flashcardDiv.parentElement;
        if (getComputedStyle(container).position === 'static') {
            container.style.position = 'relative';
        }
        const clones = [];
        flashcardDiv.style.transition = 'all 0.3s ease';
        flashcardDiv.style.zIndex = '10';
        for (let i = 0; i < 3; i++) {
            const clone = flashcardDiv.cloneNode(true);
            clone.removeAttribute('id');
            clone.style.position = 'absolute';
            clone.style.left = flashcardDiv.offsetLeft + 'px';
            clone.style.top = flashcardDiv.offsetTop + 'px';
            clone.style.width = flashcardDiv.offsetWidth + 'px';
            clone.style.height = flashcardDiv.offsetHeight + 'px';
            clone.style.zIndex = '5';
            clone.style.transition = 'all 0.3s ease';
            clone.style.opacity = '1';
            clone.querySelectorAll('[id]').forEach(el => el.removeAttribute('id'));
            container.appendChild(clone);
            clones.push(clone);
        }
        requestAnimationFrame(() => {
            flashcardDiv.style.transform = `translate(${Math.random()*30-15}px, ${Math.random()*30-15}px) rotate(${Math.random()*10-5}deg)`;
            clones.forEach((clone) => {
                const x = Math.random() * 120 - 60;
                const y = Math.random() * 80 - 40;
                const rot = Math.random() * 40 - 20;
                clone.style.transform = `translate(${x}px, ${y}px) rotate(${rot}deg) scale(0.95)`;
                clone.style.opacity = '0.8';
                clone.style.boxShadow = '0 10px 20px rgba(0,0,0,0.2)';
            });
        });
        setTimeout(() => {
            updateFlashcard();
            flashcardDiv.style.transform = 'translate(0,0) rotate(0deg)';
            clones.forEach(clone => {
                clone.style.transform = 'translate(0,0) rotate(0) scale(1)';
                clone.style.opacity = '0';
            });
            setTimeout(() => {
                clones.forEach(c => c.remove());
                flashcardDiv.style.zIndex = '';
                isFlipping = false;
            }, 300);
        }, 300);
    });

    updateFlashcard();
    window.flashcardsInitialized = true;
};

// Climb Game
(function() {
  try {
    let climbScore = 0;
    
    let playerPosition = 35; 
    let isGameRunning = false; let isPaused = false; let spacePressed = false;
    let gameLoopId = null;
    let currentQuestion = null;
    document.addEventListener('keydown', (e) => { if(e.code === 'Space') { spacePressed = true; if(isGameRunning) e.preventDefault(); } });
    document.addEventListener('keyup', (e) => { if(e.code === 'Space') spacePressed = false; });
    let climbFuel = 50; let downwardAccel = 0;
    
    var WIN_HEIGHT = 90; 
    var CLIMB_STEP = 15; 
    var FALL_RATE = 0.04; 
    var TICK_RATE = 20; 
    
    window.initClimbGame = function() {
    const bg = document.getElementById('climb-stars');
    if(bg && bg.innerHTML === '') {
        for(let i=0; i<60; i++) {
            const m = document.createElement('div');
            m.style.position = 'absolute';
            m.style.left = Math.random()*100 + '%';
            m.style.top = Math.random()*100 + '%';
            const size = Math.random()*2 + 1;
            m.style.width = size + 'px';
            m.style.height = size + 'px';
            m.style.background = '#fff';
            m.style.borderRadius = '50%';
            m.style.opacity = Math.random()*0.7 + 0.3;
            m.style.animation = `twinkle ${Math.random()*4+2}s infinite alternate ease-in-out`;
            bg.appendChild(m);
        }
    }

        const ui = document.getElementById('climb-game-ui');
        if(ui) ui.style.display = 'flex';
        const interaction = document.getElementById('climb-interaction'); if(interaction) interaction.style.display = 'none';
        const start = document.getElementById('climb-start-screen'); if(start) start.style.display = 'flex';
    }

    window.toggleClimbFullscreen = function() {
        const elem = document.getElementById('climb-game-ui');
        if (!document.fullscreenElement) {
            if (elem.requestFullscreen) {
                elem.requestFullscreen().catch(err => {
                    console.error(`Error attempting to enable fullscreen: ${err.message}`);
                });
            } else if (elem.webkitRequestFullscreen) { /* Safari */
                elem.webkitRequestFullscreen();
            } else if (elem.msRequestFullscreen) { /* IE11 */
                elem.msRequestFullscreen();
            }
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.webkitExitFullscreen) { /* Safari */
                document.webkitExitFullscreen();
            } else if (document.msExitFullscreen) { /* IE11 */
                document.msExitFullscreen();
            }
        }
    };
window.exitClimbGame = function() {
        const ui = document.getElementById('climb-game-ui');
        if(ui) ui.style.display = 'none';
        isGameRunning = false;
        if(gameLoopId) clearInterval(gameLoopId);
        window.switchToFlashcards();
    }

    window.toggleClimbPause = function() {
        if (!isGameRunning && !isPaused) return;
        isPaused = !isPaused;
        const btn = document.getElementById('climb-pause-btn');
        if (btn) btn.innerText = isPaused ? _t("Resume", "Resume") : _t("Pause", "Pause");
        
        const pauseScreen = document.getElementById('climb-paused-screen');
        if(pauseScreen) pauseScreen.style.display = isPaused ? 'flex' : 'none';
    };

    window.resetToClimbMenu = function() {
        isGameRunning = false;
        isPaused = false;
        if(gameLoopId) clearInterval(gameLoopId);
        
        document.getElementById('climb-game-ui').style.display = 'flex';
        document.getElementById('climb-start-screen').style.display = 'flex';
        document.getElementById('climb-game-over').style.display = 'none';
        document.getElementById('climb-interaction').style.display = 'none';
        
        const pauseScreen = document.getElementById('climb-paused-screen');
        if(pauseScreen) pauseScreen.style.display = 'none';
        
        const pBtn = document.getElementById('climb-pause-btn');
        if(pBtn) pBtn.innerText = _t("Pause", "Pause");
        
        const interaction = document.getElementById('climb-interaction');
        if (interaction) interaction.style.opacity = "1";
    }

    window.startClimbGame = function() {
        isPaused = false;
        const pBtn = document.getElementById('climb-pause-btn');
        if(pBtn) pBtn.innerText = _t("Pause", "Pause");
        const interaction = document.getElementById('climb-interaction');
        if (interaction) interaction.style.opacity = "1";

        climbScore = 0;
        climbFuel = 50;
        
        playerPosition = 35;
        isGameRunning = true;
        
        document.getElementById('climb-start-screen').style.display = 'none';
        document.getElementById('climb-game-over').style.display = 'none';
        document.getElementById('climb-question-area').style.display = 'block';
        document.getElementById('climb-interaction').style.display = 'flex';
        
        updateDisplay();
        nextClimbQuestion();
        
        if(gameLoopId) clearInterval(gameLoopId);
        gameLoopId = setInterval(gameLoop, TICK_RATE);
    }
    
    function gameLoop() {
        if(!isGameRunning || isPaused) return;
        
        const isBoosting = spacePressed && climbFuel > 0;
        if(isBoosting) {
            playerPosition = Math.min(95, playerPosition + 0.5);
            climbFuel = Math.max(0, climbFuel - 0.2);
            if(typeof updateFuelDisplay === 'function') updateFuelDisplay();
        }
        
        const fOut = document.getElementById('climb-flame-outer');
        const fIn = document.getElementById('climb-flame-inner');
        if(fOut && fIn) {
            const scale = isBoosting ? "scale(1.2, 2.0)" : "scale(1, 1)";
            fOut.style.transform = scale;
            fIn.style.transform = scale;
        }

        let effectiveFall = FALL_RATE;
        if (climbFuel <= 0) {
            downwardAccel += 0.007;
            effectiveFall += downwardAccel;
        } else {
            downwardAccel = 0;
        }
        playerPosition -= effectiveFall;
        climbFuel = Math.max(0, climbFuel - 0.1); 
        
        if (playerPosition <= 0) {
            endGame();
        }
        
        updatePlayerPos();
        updateFuelDisplay();
    }
    
    function updateDisplay() {
        document.getElementById('climb-score').innerText = _t("Score:", "Score:") + " " + climbScore;
        
        updatePlayerPos();
        updateFuelDisplay();
    }
    
        function updateFuelDisplay() {
        const fill = document.getElementById('climb-fuel-fill');
        if(fill) fill.style.height = `${climbFuel}%`;
    }
    
    function updatePlayerPos() {
        const player = document.getElementById('climb-player');
        if(player) player.style.bottom = `${Math.max(0, playerPosition)}%`;
    }
    
    function nextClimbQuestion() {
        const feedback = document.getElementById('climb-feedback');
        feedback.innerText = '';
        feedback.className = '';
        
        if (!window.lessonFlashcards || window.lessonFlashcards.length === 0) {
            const qt = document.getElementById('climb-question-text');
            const msg = (window.globalTranslations && window.globalTranslations["No flashcards found for this lesson!"]) || "No flashcards found for this lesson!";
            if(qt) qt.innerText = msg;
            return;
        }
        
        if (!window.usedFlashcardIndices) window.usedFlashcardIndices = [];
    
        if (!window.lessonFlashcards) {
            if (typeof window.initFlashcards === 'function') window.initFlashcards();
        }
        
        let availablePool = [];
        if (window.lessonFlashcards) {
            availablePool = window.lessonFlashcards
                .map((_, i) => i)
                .filter(i => !window.usedFlashcardIndices.includes(i));
        }
        
        let qIdx;
        if (availablePool.length > 0) {
            const randomPoolIdx = Math.floor(Math.random() * availablePool.length);
            qIdx = availablePool[randomPoolIdx];
        } else {
            window.usedFlashcardIndices = [];
            qIdx = Math.floor(Math.random() * (window.lessonFlashcards ? window.lessonFlashcards.length : 0));
        }
        window.usedFlashcardIndices.push(qIdx);
        currentQuestion = window.lessonFlashcards[qIdx];
        
        document.getElementById('climb-question-text').innerText = _tr(currentQuestion.question);
        
        const options = [currentQuestion.answer];
        const uniqueOptions = new Set([currentQuestion.answer]);
        
        const allAnswers = window.lessonFlashcards.map(f => f.answer);
        for (let i = allAnswers.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [allAnswers[i], allAnswers[j]] = [allAnswers[j], allAnswers[i]];
        }
        
        for(let ans of allAnswers) {
            if(!uniqueOptions.has(ans)) {
                options.push(ans);
                uniqueOptions.add(ans);
                if(options.length >= 3) break; 
            }
        }
        
        for (let i = options.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [options[i], options[j]] = [options[j], options[i]];
        }
        
        const optionsContainer = document.getElementById('climb-options');
        optionsContainer.innerHTML = '';
        
        options.forEach(opt => {
            const btn = document.createElement('button');
            btn.className = 'climb-option-btn';
            btn.innerText = _tr(opt);
            btn.onclick = () => handleClimbAnswer(opt);
            optionsContainer.appendChild(btn);
        });
    }
    
    let answerLocked = false;
    function handleClimbAnswer(selected) { if(isPaused) return;
        if(!isGameRunning || isPaused) return;
        if(answerLocked) return;
        answerLocked = true;
        
        // Disable all buttons immediately to prevent spam
        document.querySelectorAll('.climb-option-btn').forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
        
        const isBoosting = spacePressed && climbFuel > 0;
        if(isBoosting) {
            playerPosition = Math.min(95, playerPosition + 0.5);
            climbFuel = Math.max(0, climbFuel - 0.2);
            if(typeof updateFuelDisplay === 'function') updateFuelDisplay();
        }
        
        const fOut = document.getElementById('climb-flame-outer');
        const fIn = document.getElementById('climb-flame-inner');
        if(fOut && fIn) {
            const scale = isBoosting ? "scale(1.2, 2.0)" : "scale(1, 1)";
            fOut.style.transform = scale;
            fIn.style.transform = scale;
        }

        const feedback = document.getElementById('climb-feedback');
        
        if(selected === currentQuestion.answer) {
            // Correct
            climbScore += 10;
            climbFuel = Math.min(100, climbFuel + 20);
            feedback.innerText = (window.globalTranslations && window.globalTranslations["Correct! Adding fuel..."]) || "Correct! Adding fuel...";
            feedback.style.color = "#16a34a";

        } else {
            // Incorrect
            playerPosition -= 5;
            feedback.innerText = (window.globalTranslations && window.globalTranslations["Oops! Slipping down..."]) || "Oops! Slipping down...";
            feedback.style.color = "#dc2626";
        }
        
        updateDisplay();
        
        const btns = document.querySelectorAll('.climb-option-btn');
        btns.forEach(b => b.disabled = true);
        
        setTimeout(() => {
            answerLocked = false;
            nextClimbQuestion();
        }, 1000);
    }
    
        function endGame() {
        isGameRunning = false;
        clearInterval(gameLoopId);
        
        document.getElementById('climb-question-area').style.display = 'none';
        document.getElementById('climb-interaction').style.display = 'none';
        const gameOverScreen = document.getElementById('climb-game-over');
        gameOverScreen.style.display = 'flex';
        
        const title = document.getElementById('climb-result-title');
        const msg = document.getElementById('climb-final-score');
        
        let storageKey = 'climbHighScore';
        try {
            const currentUser = JSON.parse(localStorage.getItem('user'));
            if(currentUser && currentUser.email) {
                storageKey = 'climbHighScore_' + currentUser.email;
            }
        } catch(e) { console.error(e); }

        let highScore = localStorage.getItem(storageKey) || 0;
        highScore = parseInt(highScore);
        if(climbScore > highScore) {
            highScore = climbScore;
            localStorage.setItem(storageKey, highScore);
            title.innerText = (window.globalTranslations && window.globalTranslations["🏆 New High Score! 🏆"]) || "🏆 New High Score! 🏆";
            title.style.color = "#f59e0b";
        } else {
            title.innerText = (window.globalTranslations && window.globalTranslations["Game Over"]) || "Game Over";
            title.style.color = "#1e293b";
        }
        
        const scoreLabel = (window.globalTranslations && window.globalTranslations["Score:"]) || "Score:";
        const bestLabel = (window.globalTranslations && window.globalTranslations["Best:"]) || "Best:";
        msg.innerHTML = `${scoreLabel} ${climbScore}<br><span style="font-size:0.9em; color:#64748b">${bestLabel} ${highScore}</span>`;
    }
  } catch(e) { console.error("Climb Game Init Failed:", e); }
})();

// Mix Match
(function() {
  try {
    window.initMixMatch = function() {
        if(window.mixMatchInitialized) return;
        window.mixMatchInitialized = true;
        window.startMixMatchGame();
    };

    let selectedCards = [];
    let matchedPairs = 0;
    let totalPairsInGame = 0;
    let streak = 0;

    const MIX_MATCH_MAX_PAIRS = 10; // Cap similar to lesson Practice files

    window.startMixMatchGame = function() {
        if ((!window.lessonFlashcards || window.lessonFlashcards.length === 0) && window.initFlashcards) {
            window.initFlashcards();
        }
        const gameContainer = document.getElementById('mixmatch-game-board');
        const winScreen = document.getElementById('mixmatch-win-screen');
        
        if(!gameContainer) return;

        gameContainer.innerHTML = '';
        if(winScreen) winScreen.classList.add('hidden');
        selectedCards = [];
        matchedPairs = 0;
        streak = 0;
        updateStreak(0);

        const data = window.lessonFlashcards || [];
        // Pick a random subset of pairs when there are more than the cap
        let indices = data.map((_, i) => i);
        if (data.length > MIX_MATCH_MAX_PAIRS) {
            indices = indices.sort(() => Math.random() - 0.5).slice(0, MIX_MATCH_MAX_PAIRS);
        }
        totalPairsInGame = indices.length;

        let gameItems = [];
        indices.forEach(idx => {
            gameItems.push({ id: idx, text: _tr(data[idx].question), type: 'term' });
            gameItems.push({ id: idx, text: _tr(data[idx].answer), type: 'def' });
        });

        gameItems.sort(() => Math.random() - 0.5).forEach(item => {
            gameContainer.appendChild(createCard(item.id, item.text, item.type));
        });
    }

    function createCard(id, text, type) {
        const div = document.createElement('div');
        div.className = 'mm-card';
        div.dataset.id = id;
        div.dataset.type = type;
        div.innerHTML = `<span class="font-semibold text-sm md:text-base">${text}</span>`;
        div.onclick = () => handleCardClick(div);
        return div;
    }

    function handleCardClick(card) {
        if (card.classList.contains('selected') || card.classList.contains('invisible')) return;
        if (selectedCards.length >= 2) return;

        card.classList.add('selected');
        selectedCards.push(card);

        if (selectedCards.length === 2) {
            checkMatch();
        }
    }

    function checkMatch() {
        const [c1, c2] = selectedCards;
        let isMatch = false;
        
        if (c1.dataset.type !== c2.dataset.type) {
            // Compare by card id — both cards must reference the same flashcard index
            isMatch = c1.dataset.id === c2.dataset.id;
        }

        if (isMatch) {
            setTimeout(() => {
                c1.classList.add('invisible', 'opacity-0', 'transition-opacity', 'duration-500');
                c2.classList.add('invisible', 'opacity-0', 'transition-opacity', 'duration-500');
                matchedPairs++;
                updateStreak(1);
                if (matchedPairs === totalPairsInGame) {
                    const winScrn = document.getElementById('mixmatch-win-screen');
                    if(winScrn) setTimeout(() => winScrn.classList.remove('hidden'), 500);
                }
            }, 300);
        } else {
            c1.classList.add('wrong');
            c2.classList.add('wrong');
            
            updateStreak(-streak);
            setTimeout(() => {
                c1.classList.remove('wrong', 'selected');
                c2.classList.remove('wrong', 'selected');
            }, 800);
        }
        selectedCards = [];
    }

    function updateStreak(change) {
        streak = change === -streak ? 0 : streak + change;
        const disp = document.getElementById('mixmatch-streak-display');
        if(disp) {
            disp.textContent = streak;
            disp.classList.add('pop-anim');
            setTimeout(() => disp.classList.remove('pop-anim'), 300);
        }
    }
  } catch(e) { console.error("MixMatch Failed Init:", e); }
})();

console.log("Middle of script file reached - MixMatch loaded, BlockPuzzle starting...");

// Block Puzzle - Clean Re-Write
(function() {
    // Global Access Point
    window.initBlockPuzzle = function() {
        if(!window.realInitBlockPuzzle) {
            console.error("Block Puzzle: realInitBlockPuzzle is missing. The module failed to load.");
            const c = document.getElementById('blockpuzzle-container');
            if(c && window.bpError) c.innerHTML = '<div style="color:red;padding:20px;">Startup Error: ' + window.bpError + '</div>';
            else if (c) c.innerHTML = '<div style="color:red;padding:20px;">Game Module Failed</div>';
            return;
        }
        window.realInitBlockPuzzle();
    };

    window.bpError = null;

    try {
        console.log("Block Puzzle Module Loading...");
        const BOARD_SIZE = 8;
        let grid = [];
        let score = 0;
        const colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6', '#ec4899'];
        const SHAPES = [
            [[1]], [[1, 1]], [[1, 1, 1]], [[1, 1, 1, 1]], 
            [[1, 1], [1, 1]], [[1, 0], [1, 1]], 
            [[1, 1, 1], [0, 1, 0]], [[1, 1, 0], [0, 1, 1]]
        ];
        
        let draggedBlock = null;
        let dragStartPos = { x: 0, y: 0 };
        let dragOffset = { x: 0, y: 0 };
        let currentPreview = [];

        // Real Logic
        window.realInitBlockPuzzle = function() {
            if(window.bpInitialized) {
                 window.resetBlockGame();
                 return;
            }
            window.bpInitialized = true;
            console.log("Block Puzzle Initialized");
            
            document.addEventListener('mousemove', handleDragMove);
            document.addEventListener('touchmove', handleDragMove, {passive: false});
            document.addEventListener('mouseup', handleDragEnd);
            document.addEventListener('touchend', handleDragEnd);
            
            if(!document.getElementById('bp-question-modal')) createQuestionModal();
            window.resetBlockGame();
        };

        window.resetBlockGame = function() {
            grid = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(0));
            score = 0;
            const scoreEl = document.getElementById('bp-score');
            if(scoreEl) scoreEl.innerText = 0;
            initBoard();
            spawnBlocks();
            const go = document.getElementById('bp-game-over');
            if(go) go.classList.add('hidden');
        };

        function initBoard() {
            const boardEl = document.getElementById('bp-board');
            if(!boardEl) return;
            boardEl.innerHTML = '';
            for(let y=0; y<BOARD_SIZE; y++) {
                for(let x=0; x<BOARD_SIZE; x++) {
                    const cell = document.createElement('div');
                    cell.className = 'w-full h-full bg-gray-800 rounded-sm border border-gray-700/50';
                    cell.dataset.x = x; cell.dataset.y = y;
                    boardEl.appendChild(cell);
                }
            }
        }

        function createQuestionModal() {
            const modal = document.createElement('div');
            modal.id = 'bp-question-modal';
            modal.className = 'hidden fixed inset-0 bg-black/90 z-50 flex items-center justify-center p-4 backdrop-blur-sm';
            modal.innerHTML = `
                <div class="bg-gray-800 p-6 rounded-2xl border border-gray-700 max-w-lg w-full text-center shadow-2xl">
                    <h3 class="text-2xl font-bold text-white mb-4">Bonus Question!</h3>
                    <div id="bp-q-text" class="text-lg text-white mb-6 font-medium"></div>
                    <div id="bp-q-options" class="grid gap-3"></div>
                </div>`;
            document.body.appendChild(modal);
        }

        function spawnBlocks() {
            const handEl = document.getElementById('bp-hand');
            if(!handEl) return;
            
            // Layout fixes
            handEl.style.display = 'flex';
            handEl.style.justifyContent = 'center';
            handEl.style.gap = '15px';
            handEl.style.border = '1px dashed #475569';
            handEl.style.minHeight = '100px';
            handEl.innerHTML = '';
            
            for(let i=0; i<3; i++) {
                try {
                    const shape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
                    const color = colors[Math.floor(Math.random() * colors.length)];
                    createDraggableBlock(shape, color);
                } catch(e) { console.error(e); }
            }
        }

        function createDraggableBlock(shapeMatrix, color) {
            const handEl = document.getElementById('bp-hand');
            const pt = 25; // Block Pixel Size //
            const w = shapeMatrix[0].length * pt;
            const h = shapeMatrix.length * pt;
            
            const container = document.createElement('div');
            container.style.width = w + 'px';
            container.style.height = h + 'px';
            container.style.position = 'relative';
            container.style.cursor = 'grab';
            container.dataset.shape = JSON.stringify(shapeMatrix);
            container.dataset.color = color;
            
            shapeMatrix.forEach((row, r) => {
                row.forEach((active, c) => {
                    if(active) {
                        const b = document.createElement('div');
                        b.style.position = 'absolute';
                        b.style.left = (c*pt) + 'px';
                        b.style.top = (r*pt) + 'px';
                        b.style.width = (pt-2) + 'px';
                        b.style.height = (pt-2) + 'px';
                        b.style.backgroundColor = color;
                        b.style.border = '1px solid white';
                        container.appendChild(b);
                    }
                });
            });
            
            container.addEventListener('mousedown', startDrag);
            container.addEventListener('touchstart', startDrag, {passive:false});
            handEl.appendChild(container);
        }

        function startDrag(e) {
            e.preventDefault(); e.stopPropagation();
            draggedBlock = e.currentTarget;
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            const rect = draggedBlock.getBoundingClientRect();
            dragOffset = { x: clientX - rect.left, y: clientY - rect.top };
            
            draggedBlock.style.position = 'fixed';
            draggedBlock.style.left = rect.left + 'px';
            draggedBlock.style.top = rect.top + 'px';
            draggedBlock.style.zIndex = 10000;
            draggedBlock.style.transform = 'scale(1.2)';
        }

        function handleDragMove(e) {
            if(!draggedBlock) return;
            e.preventDefault();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            draggedBlock.style.left = (clientX - dragOffset.x) + 'px';
            draggedBlock.style.top = (clientY - dragOffset.y) + 'px';
            updatePreview(clientX, clientY);
        }

        function handleDragEnd(e) {
            if(!draggedBlock) return;
            const clientX = e.changedTouches ? e.changedTouches[0].clientX : e.clientX;
            const clientY = e.changedTouches ? e.changedTouches[0].clientY : e.clientY;
            
            clearPreview();
            if(attemptPlace(clientX, clientY)) {
                draggedBlock.remove();
                checkLines();
                if(document.getElementById('bp-hand').children.length === 0) triggerQuestion();
                else checkGameOver();
            } else {
                draggedBlock.style.position = '';
                draggedBlock.style.left = ''; draggedBlock.style.top = '';
                draggedBlock.style.zIndex = ''; draggedBlock.style.transform = '';
            }
            draggedBlock = null;
        }

        function getBoardCoords(cx, cy) {
            const board = document.getElementById('bp-board');
            if(!board) return null;
            const rect = board.getBoundingClientRect();
            if(cx < rect.left || cx > rect.right || cy < rect.top || cy > rect.bottom) return null;
            
            const cell = rect.width / BOARD_SIZE;
            const bx = draggedBlock.getBoundingClientRect();
            const col = Math.floor((bx.left + cell/2 - rect.left) / cell);
            const row = Math.floor((bx.top + cell/2 - rect.top) / cell);
            
            if(col >= 0 && col < BOARD_SIZE && row >= 0 && row < BOARD_SIZE) return {x:col, y:row};
            return null;
        }

        function updatePreview(cx, cy) {
            clearPreview();
            const c = getBoardCoords(cx, cy);
            if(!c) return;
            if(canPlace(JSON.parse(draggedBlock.dataset.shape), c.x, c.y)) {
                // simple visual feedback
            }
        }
        function clearPreview() {} // TODO: Impl

        function canPlace(shape, x, y) {
            for(let r=0; r<shape.length; r++) {
                for(let c=0; c<shape[0].length; c++) {
                    if(shape[r][c]) {
                        if(x+c >= BOARD_SIZE || y+r >= BOARD_SIZE || grid[y+r][x+c]) return false;
                    }
                }
            }
            return true;
        }

        function attemptPlace(cx, cy) {
            const c = getBoardCoords(cx, cy);
            if(!c) return false;
            const shape = JSON.parse(draggedBlock.dataset.shape);
            if(canPlace(shape, c.x, c.y)) {
                place(shape, c.x, c.y, draggedBlock.dataset.color);
                return true;
            }
            return false;
        }

        function place(shape, x, y, color) {
            const board = document.getElementById('bp-board');
            for(let r=0; r<shape.length; r++) {
                for(let c=0; c<shape[0].length; c++) {
                    if(shape[r][c]) {
                        grid[y+r][x+c] = 1;
                        const cell = board.children[(y+r)*BOARD_SIZE + (x+c)];
                        cell.style.backgroundColor = color;
                        cell.style.opacity = 1;
                    }
                }
            }
            score += 10;
            document.getElementById('bp-score').innerText = score;
        }
        
        function checkLines() {
            // Simple line clear
            for(let y=0; y<BOARD_SIZE; y++) {
                if(grid[y].every(v => v===1)) {
                    grid[y].fill(0);
                    for(let x=0; x<BOARD_SIZE; x++) {
                         const cell = document.getElementById('bp-board').children[y*BOARD_SIZE+x];
                         cell.style.backgroundColor = '';
                    }
                    score += 100;
                }
            }
            for(let x=0; x<BOARD_SIZE; x++) {
                if(grid.every(r => r[x]===1)) {
                    for(let y=0; y<BOARD_SIZE; y++) {
                        grid[y][x] = 0;
                        const cell = document.getElementById('bp-board').children[y*BOARD_SIZE+x];
                        cell.style.backgroundColor = '';
                    }
                    score += 100;
                }
            }
            document.getElementById('bp-score').innerText = score;
        }
        
        function checkGameOver() {
            // Check if ANY block in hand can fit
            // ...
        }

        function triggerQuestion() { spawnBlocks(); } // Placeholder

    } catch(e) {
        window.bpError = e.message + " " + e.stack;
        console.error(e);
    }
})();


// On DOM Ready check
const initPracticeGames = () => {
    console.log("Initializing Practice Games Logic...");
    if(window.attachPracticeListeners) window.attachPracticeListeners();
    if(window.lessonFlashcards && window.initFlashcards) {
        window.initFlashcards();
    }
};

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPracticeGames);
} else {
    initPracticeGames();
}
