(function() {
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
    let climbScore = 0;
    
    let playerPosition = 35; // percent from bottom
    let isGameRunning = false; let isPaused = false; let spacePressed = false;
    let gameLoopId = null;
    let currentQuestion = null;
    document.addEventListener('keydown', (e) => { if(e.code === 'Space') { spacePressed = true; if(isGameRunning) e.preventDefault(); } });
    document.addEventListener('keyup', (e) => { if(e.code === 'Space') spacePressed = false; });
    let climbFuel = 50; let downwardAccel = 0;
    
    // Config
    const WIN_HEIGHT = 90; // percent
    const CLIMB_STEP = 15; // percent
    const FALL_RATE = 0.04; // percent per tick (simulates moving ladder)
    const TICK_RATE = 20; // ms
    
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
        if(pBtn) pBtn.innerText = _t("Pause", "暂停");
        
        const interaction = document.getElementById('climb-interaction');
        if (interaction) interaction.style.opacity = "1";
    }

    window.startClimbGame = function() {
        isPaused = false;
        const pBtn = document.getElementById('climb-pause-btn');
        if(pBtn) pBtn.innerText = _t("Pause", "暂停");
        const interaction = document.getElementById('climb-interaction');
        if (interaction) interaction.style.opacity = "1";

        // Reset State
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
        
        // Start "Ladder Going Down" Mechanics
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
        
        // Visual Boost Effect
        const fOut = document.getElementById('climb-flame-outer');
        const fIn = document.getElementById('climb-flame-inner');
        if(fOut && fIn) {
            const scale = isBoosting ? "scale(1.2, 2.0)" : "scale(1, 1)";
            fOut.style.transform = scale;
            fIn.style.transform = scale;
        }

        // Ladder moves down, so character moves down relative to viewport if they don't climb
        // Or simply: Gravity pulls them down
        let effectiveFall = FALL_RATE;
        if (climbFuel <= 0) {
            downwardAccel += 0.007;
            effectiveFall += downwardAccel;
        } else {
            downwardAccel = 0;
        }
        playerPosition -= effectiveFall;
        climbFuel = Math.max(0, climbFuel - 0.1); // Faster at higher levels?
        
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
            document.getElementById('climb-question-text').innerText = _t("No flashcards found for this lesson!");
            return;
        }
        
        // Pick random question
            // Unique Question Logic
    if (!window.usedFlashcardIndices) window.usedFlashcardIndices = [];
    
    // Safety check for flashcards
    if (!window.lessonFlashcards) {
        if (typeof window.initFlashcards === 'function') window.initFlashcards();
    }
    
    // Filter available indices
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
        // Reset if exhausted to avoid infinite loops or empty
        window.usedFlashcardIndices = [];
        qIdx = Math.floor(Math.random() * (window.lessonFlashcards ? window.lessonFlashcards.length : 0));
    }
    window.usedFlashcardIndices.push(qIdx);
        currentQuestion = window.lessonFlashcards[qIdx];
        
        var _tr = window.arisTranslate || function(t){return t;};
        document.getElementById('climb-question-text').innerText = _tr(currentQuestion.question);
        
        // Generate Distractors
        const options = [currentQuestion.answer];
        const uniqueOptions = new Set([currentQuestion.answer]);
        
        // Try to get 2 unique distractors (or fewer if not enough unique answers exist)
        const allAnswers = window.lessonFlashcards.map(f => f.answer);
        // Shuffle all answers first to ensure randomness in selection
        for (let i = allAnswers.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [allAnswers[i], allAnswers[j]] = [allAnswers[j], allAnswers[i]];
        }
        
        for(let ans of allAnswers) {
            if(!uniqueOptions.has(ans)) {
                options.push(ans);
                uniqueOptions.add(ans);
                if(options.length >= 3) break; // 1 correct + 2 distractors
            }
        }
        
        // Shuffle Options
        for (let i = options.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [options[i], options[j]] = [options[j], options[i]];
        }
        
        // Render Options
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
    
    function handleClimbAnswer(selected) { if(isPaused) return;
        if(!isGameRunning || isPaused) return;
        
        const isBoosting = spacePressed && climbFuel > 0;
        if(isBoosting) {
            playerPosition = Math.min(95, playerPosition + 0.5);
            climbFuel = Math.max(0, climbFuel - 0.2);
            if(typeof updateFuelDisplay === 'function') updateFuelDisplay();
        }
        
        // Visual Boost Effect
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
            // playerPosition += CLIMB_STEP; // Disabled for manual boost
            feedback.innerText = _t("Correct! Adding fuel...");
            feedback.style.color = "#16a34a";

        } else {
            // Incorrect
            playerPosition -= 5; // Slip down
            feedback.innerText = _t("Oops! Slipping down...");
            feedback.style.color = "#dc2626";
        }
        
        updateDisplay();
        
        // Disable buttons temporarily
        const btns = document.querySelectorAll('.climb-option-btn');
        btns.forEach(b => b.disabled = true);
        
        setTimeout(() => {
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
        
        // High Score Logic
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
            title.innerText = _t("🏆 New High Score! 🏆");
            title.style.color = "#f59e0b";
        } else {
            title.innerText = _t("Game Over", "Game Over");
            title.style.color = "#1e293b";
        }
        
        msg.innerHTML = _t("Score:", "Score:") + " " + climbScore + '<br><span style="font-size:0.9em; color:#64748b">' + _t("Best:", "Best:") + " " + highScore + '</span>';
    }
})();
</script>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script>
(function() {
    window.initMixMatch = function() {
        if(window.mixMatchInitialized) return;
        window.mixMatchInitialized = true;
        window.startMixMatchGame();
    };

    let selectedCards = [];
    let matchedPairs = 0;
    let streak = 0;

    window.startMixMatchGame = function() {
        if ((!window.lessonFlashcards || window.lessonFlashcards.length === 0) && window.initFlashcards) {
            window.initFlashcards();
        }
        const gameContainer = document.getElementById('mixmatch-game-board');
        const winScreen = document.getElementById('mixmatch-win-screen');
        
        gameContainer.innerHTML = '';
        winScreen.classList.add('hidden');
        selectedCards = [];
        matchedPairs = 0;
        streak = 0;
        updateStreak(0);

        const data = window.lessonFlashcards || [];
        let gameItems = [];
        data.forEach((item, index) => {
            gameItems.push({ id: index, text: _tr(item.question), type: 'term' });
            gameItems.push({ id: index, text: _tr(item.answer), type: 'def' });
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
                if (matchedPairs === (window.lessonFlashcards ? window.lessonFlashcards.length : 0)) {
                    setTimeout(() => document.getElementById('mixmatch-win-screen').classList.remove('hidden'), 500);
                }
            }, 300);
        } else {
            updateStreak(-streak);
            setTimeout(() => {
                [c1, c2].forEach(c => {
                    c.classList.remove('selected');
                });
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
})();
</script><script>
(function() {
    const BOARD_SIZE = 8;
    let grid = [];
    let score = 0;
    const colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#8b5cf6', '#ec4899'];
    const SHAPES = [
        [[1]], [[1, 1]], [[1, 1, 1]], [[1, 1, 1, 1]], 
        [[1, 1], [1, 1]], [[1, 0], [1, 1]], 
        [[1, 1, 1], [0, 1, 0]], [[1, 1, 0], [0, 1, 1]]
    ];
    
    // Drag State
    let draggedBlock = null;
    let dragStartPos = { x: 0, y: 0 };
    let dragOffset = { x: 0, y: 0 };
    let currentPreview = [];

    window.initBlockPuzzle = function() {
        if(window.bpInitialized) return;
        window.bpInitialized = true;
        window.resetBlockGame();
        
        // Global listeners for drag
        document.addEventListener('mousemove', handleDragMove);
        document.addEventListener('touchmove', handleDragMove, {passive: false});
        document.addEventListener('mouseup', handleDragEnd);
        document.addEventListener('touchend', handleDragEnd);
        
        // Create Modal if it doesn't exist
        if(!document.getElementById('bp-question-modal')) {
             createQuestionModal();
        }
    };
    
    function createQuestionModal() {
        const modal = document.createElement('div');
        modal.id = 'bp-question-modal';
        modal.className = 'hidden fixed inset-0 bg-black/90 z-50 flex items-center justify-center p-4 backdrop-blur-sm';
        modal.innerHTML = `
            <div class="bg-gray-800 p-6 rounded-2xl border border-gray-700 max-w-lg w-full text-center shadow-2xl">
                <h3 class="text-2xl font-bold text-white mb-4">Bonus Question!</h3>
                <p class="text-gray-400 mb-6">Answer correctly to get more blocks.</p>
                <div id="bp-q-text" class="text-lg text-white mb-6 font-medium"></div>
                <div id="bp-q-options" class="grid gap-3"></div>
            </div>
        `;
        document.body.appendChild(modal);
    }

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
                cell.dataset.x = x;
                cell.dataset.y = y;
                boardEl.appendChild(cell);
            }
        }
    }

    function spawnBlocks() {
        const handEl = document.getElementById('bp-hand');
        if(!handEl) return;
        handEl.innerHTML = '';
        for(let i=0; i<3; i++) {
            const shape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
            const color = colors[Math.floor(Math.random() * colors.length)];
            createDraggableBlock(shape, color);
        }
    }
    
    function triggerQuestion() {
        // Find question
        const flashcards = window.lessonFlashcards || [];
        if(flashcards.length === 0) {
            spawnBlocks();
            checkGameOver();
            return;
        }
        
        const qIdx = Math.floor(Math.random() * flashcards.length);
        const q = flashcards[qIdx];
        
        const modal = document.getElementById('bp-question-modal');
        const qText = document.getElementById('bp-q-text');
        const qOpts = document.getElementById('bp-q-options');
        
        qText.textContent = q.question;
        qOpts.innerHTML = '';
        
        // Generate Distractors
        let answers = [q.answer];
        const uniqueSet = new Set([q.answer]);
        
        const pool = flashcards.filter((_, i) => i !== qIdx);
        // Shuffle pool
        pool.sort(() => Math.random() - 0.5);
        
        for(let item of pool) {
             if(!uniqueSet.has(item.answer)) {
                 answers.push(item.answer);
                 uniqueSet.add(item.answer);
                 if(answers.length >= 4) break;
             }
        }
        
        answers.sort(() => Math.random() - 0.5);
        
        answers.forEach(ans => {
            const btn = document.createElement('button');
            btn.className = 'w-full text-left p-3 rounded-lg bg-gray-700 hover:bg-gray-600 text-gray-200 transition-colors border border-gray-600';
            btn.textContent = ans;
            btn.onclick = () => {
                if(ans === q.answer) {
                    // Correct
                    modal.classList.add('hidden');
                    spawnBlocks();
                    checkGameOver();
                } else {
                    // Incorrect
                    btn.className = 'w-full text-left p-3 rounded-lg bg-red-900/50 border border-red-500 text-red-200';
                    setTimeout(() => {
                         btn.className = 'w-full text-left p-3 rounded-lg bg-gray-700 hover:bg-gray-600 text-gray-200 transition-colors border border-gray-600';
                    }, 1000);
                }
            };
            qOpts.appendChild(btn);
        });
        
        modal.classList.remove('hidden');
    }

    function createDraggableBlock(shapeMatrix, color) {
        const handEl = document.getElementById('bp-hand');
        const container = document.createElement('div');
        container.className = 'block-shape relative touch-none select-none';
        const displaySize = 15; 
        const w = shapeMatrix[0].length * displaySize;
        const h = shapeMatrix.length * displaySize;
        container.style.width = `${w}px`;
        container.style.height = `${h}px`;
        
        container.dataset.shape = JSON.stringify(shapeMatrix);
        container.dataset.color = color;

        shapeMatrix.forEach((row, r) => {
            row.forEach((active, c) => {
                if(active) {
                    const block = document.createElement('div');
                    block.style.position = 'absolute';
                    block.style.left = `${c * displaySize}px`;
                    block.style.top = `${r * displaySize}px`;
                    block.style.width = `${displaySize-1}px`;
                    block.style.height = `${displaySize-1}px`;
                    block.style.backgroundColor = color;
                    block.style.borderRadius = '2px';
                    block.style.pointerEvents = 'none';
                    container.appendChild(block);
                }
            });
        });

        const startDrag = (e) => {
            e.preventDefault();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            
            draggedBlock = container;
            const rect = container.getBoundingClientRect();
            dragOffset.x = clientX - rect.left;
            dragOffset.y = clientY - rect.top;
            
            container.style.position = 'fixed';
            container.style.left = `${rect.left}px`;
            container.style.top = `${rect.top}px`;
            container.style.zIndex = '1000';
            container.style.transform = 'scale(2.8)';
            container.style.transformOrigin = 'top left';
            container.style.opacity = '0.9';
            container.style.cursor = 'grabbing';
        };

        container.addEventListener('mousedown', startDrag);
        container.addEventListener('touchstart', startDrag, {passive: false});

        handEl.appendChild(container);
    }

    function handleDragMove(e) {
        if(!draggedBlock) return;
        e.preventDefault();
        
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;

        const x = clientX - dragOffset.x;
        const y = clientY - dragOffset.y;
        
        draggedBlock.style.left = `${x}px`;
        draggedBlock.style.top = `${y}px`;

        updatePreview(clientX, clientY);
    }

    function handleDragEnd(e) {
        if(!draggedBlock) return;
        
        const clientX = e.changedTouches ? e.changedTouches[0].clientX : e.clientX;
        const clientY = e.changedTouches ? e.changedTouches[0].clientY : e.clientY;
        
        // FIX: Clear preview BEFORE attempting place so we don't wipe the new color
        const previewCells = [...currentPreview]; // Copy
        clearPreview();
        
        const success = attemptPlace(clientX, clientY);
        
        if (success) {
            draggedBlock.remove();
            checkLines();
            if (document.getElementById('bp-hand').children.length === 0) {
                triggerQuestion();
            } else {
                checkGameOver();
            }
        } else {
            draggedBlock.style.position = '';
            draggedBlock.style.left = '';
            draggedBlock.style.top = '';
            draggedBlock.style.zIndex = '';
            draggedBlock.style.transform = '';
            draggedBlock.style.opacity = '';
            draggedBlock.style.cursor = 'pointer';
        }
        
        draggedBlock = null;
    }

    function getBoardCoords(clientX, clientY) {
        const board = document.getElementById('bp-board');
        if(!board) return null;
        const rect = board.getBoundingClientRect();
        
        if (clientX < rect.left || clientX > rect.right || clientY < rect.top || clientY > rect.bottom) {
            return null;
        }

        const cellSize = rect.width / BOARD_SIZE;
        const blockRect = draggedBlock.getBoundingClientRect();
        // Target using center of top-left block cell
        const sampleX = blockRect.left + (cellSize / 2); 
        const sampleY = blockRect.top + (cellSize / 2);

        const col = Math.floor((sampleX - rect.left) / cellSize);
        const row = Math.floor((sampleY - rect.top) / cellSize);

        if (col >= 0 && col < BOARD_SIZE && row >= 0 && row < BOARD_SIZE) {
            return { x: col, y: row };
        }
        return null;
    }

    function updatePreview(cX, cY) {
        clearPreview();
        const coords = getBoardCoords(cX, cY);
        if(!coords) return;
        
        const shape = JSON.parse(draggedBlock.dataset.shape);
        const {x, y} = coords;
        
        if (canPlace(shape, x, y)) {
            const color = draggedBlock.dataset.color;
            const boardEl = document.getElementById('bp-board');
            
            for (let r=0; r<shape.length; r++) {
                for (let c=0; c<shape[0].length; c++) {
                    if (shape[r][c]) {
                        const cellIdx = (y+r) * BOARD_SIZE + (x+c);
                        if(cellIdx < boardEl.children.length) {
                             const cell = boardEl.children[cellIdx];
                             cell.style.backgroundColor = color;
                             cell.style.opacity = '0.5';
                             currentPreview.push(cell);
                        }
                    }
                }
            }
        }
    }

    function clearPreview() {
        currentPreview.forEach(cell => {
            cell.style.backgroundColor = '';
            cell.style.opacity = '';
        });
        currentPreview = [];
    }

    function attemptPlace(cX, cY) {
        const coords = getBoardCoords(cX, cY);
        if(!coords) return false;
        
        const shape = JSON.parse(draggedBlock.dataset.shape);
        const {x, y} = coords;
        const color = draggedBlock.dataset.color;

        if (canPlace(shape, x, y)) {
            place(shape, x, y, color);
            return true;
        }
        return false;
    }

    function canPlace(shape, x, y) {
        for (let r=0; r<shape.length; r++) {
            for (let c=0; c<shape[0].length; c++) {
                if (shape[r][c]) {
                    const boardX = x + c;
                    const boardY = y + r;
                    if (boardX >= BOARD_SIZE || boardY >= BOARD_SIZE || grid[boardY][boardX]) return false;
                }
            }
        }
        return true;
    }

    function place(shape, x, y, color) {
        const boardEl = document.getElementById('bp-board');
        for (let r=0; r<shape.length; r++) {
            for (let c=0; c<shape[0].length; c++) {
                if (shape[r][c]) {
                    grid[y+r][x+c] = 1;
                    const cell = boardEl.children[(y+r) * BOARD_SIZE + (x+c)];
                    cell.style.backgroundColor = color;
                    cell.style.boxShadow = `0 0 10px ${color}`;
                    // Important: Reset classes to ensure color visibility if class conflict exists
                    // cell.className = 'w-full h-full rounded-sm'; 
                    // Actually, keeping the class is fine if style.backgroundColor is set inline.
                    cell.style.opacity = '1';
                }
            }
        }
        score += 10;
        const scoreEl = document.getElementById('bp-score');
        if(scoreEl) scoreEl.innerText = score;
    }

    function checkLines() {
        let linesCleared = 0;
        for(let y=0; y<BOARD_SIZE; y++) {
            if(grid[y].every(v => v === 1)) {
                clearRow(y);
                linesCleared++;
            }
        }
        for(let x=0; x<BOARD_SIZE; x++) {
            if(grid.every(row => row[x] === 1)) {
                clearCol(x);
                linesCleared++;
            }
        }
        if(linesCleared > 0) {
            score += linesCleared * 100;
            const scoreEl = document.getElementById('bp-score');
            if(scoreEl) scoreEl.innerText = score;
        }
    }

    function clearRow(y) {
        grid[y].fill(0);
        for(let x=0; x<BOARD_SIZE; x++) resetCell(x, y);
    }

    function clearCol(x) {
        for(let y=0; y<BOARD_SIZE; y++) {
            grid[y][x] = 0;
            resetCell(x, y);
        }
    }

    function resetCell(x, y) {
        const boardEl = document.getElementById('bp-board');
        if(boardEl) {
            const cell = boardEl.children[y * BOARD_SIZE + x];
            cell.style.backgroundColor = ''; 
            cell.className = 'w-full h-full bg-gray-800 rounded-sm border border-gray-700/50';
            cell.style.boxShadow = '';
            cell.style.opacity = '';
        }
    }

    function checkGameOver() {
        const hand = document.getElementById('bp-hand');
        if(hand.children.length === 0) return;
        
        let canMove = false;
        
        Array.from(hand.children).forEach(block => {
            const shape = JSON.parse(block.dataset.shape);
            for(let y=0; y<BOARD_SIZE; y++) {
                for(let x=0; x<BOARD_SIZE; x++) {
                    if(canPlace(shape, x, y)) {
                        canMove = true;
                    }
                }
            }
        });
        
        if(!canMove) {
            document.getElementById('bp-game-over').classList.remove('hidden');
            document.getElementById('bp-final-score').innerText = score;
        }
    }

})();