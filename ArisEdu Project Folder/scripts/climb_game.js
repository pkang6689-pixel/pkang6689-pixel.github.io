// climb_game.js — Shared Climb (Boost) game logic for all lesson pages
// Extracted from inline <script> blocks repeated in every lesson file.

(function() {
    var climbScore = 0;
    var playerPosition = 35;
    var isGameRunning = false;
    var isPaused = false;
    var spacePressed = false;
    var gameLoopId = null;
    var currentQuestion = null;
    var climbFuel = 50;
    var downwardAccel = 0;

    var WIN_HEIGHT = 90;
    var CLIMB_STEP = 15;
    var FALL_RATE = 0.04;
    var TICK_RATE = 20;

    document.addEventListener('keydown', function(e) { if (e.code === 'Space') { spacePressed = true; if (isGameRunning) e.preventDefault(); } });
    document.addEventListener('keyup', function(e) { if (e.code === 'Space') spacePressed = false; });

    window.initClimbGame = function() {
        var bg = document.getElementById('climb-stars');
        if (bg && bg.innerHTML === '') {
            for (var i = 0; i < 60; i++) {
                var m = document.createElement('div');
                m.style.position = 'absolute';
                m.style.left = Math.random() * 100 + '%';
                m.style.top = Math.random() * 100 + '%';
                var size = Math.random() * 2 + 1;
                m.style.width = size + 'px';
                m.style.height = size + 'px';
                m.style.background = '#fff';
                m.style.borderRadius = '50%';
                m.style.opacity = Math.random() * 0.7 + 0.3;
                m.style.animation = 'twinkle ' + (Math.random() * 4 + 2) + 's infinite alternate ease-in-out';
                bg.appendChild(m);
            }
        }
        var ui = document.getElementById('climb-game-ui');
        if (ui) ui.style.display = 'flex';
        var interaction = document.getElementById('climb-interaction');
        if (interaction) interaction.style.display = 'none';
        var start = document.getElementById('climb-start-screen');
        if (start) start.style.display = 'flex';
    };

    window.toggleClimbFullscreen = function() {
        var elem = document.getElementById('climb-game-ui');
        if (!document.fullscreenElement) {
            if (elem.requestFullscreen) elem.requestFullscreen().catch(function() {});
            else if (elem.webkitRequestFullscreen) elem.webkitRequestFullscreen();
            else if (elem.msRequestFullscreen) elem.msRequestFullscreen();
        } else {
            if (document.exitFullscreen) document.exitFullscreen();
            else if (document.webkitExitFullscreen) document.webkitExitFullscreen();
            else if (document.msExitFullscreen) document.msExitFullscreen();
        }
    };

    window.exitClimbGame = function() {
        var ui = document.getElementById('climb-game-ui');
        if (ui) ui.style.display = 'none';
        isGameRunning = false;
        if (gameLoopId) clearInterval(gameLoopId);
        window.switchToFlashcards();
    };

    window.toggleClimbPause = function() {
        if (!isGameRunning && !isPaused) return;
        isPaused = !isPaused;
        var btn = document.getElementById('climb-pause-btn');
        if (btn) btn.innerText = isPaused ? 'Resume' : 'Pause';
        var pauseScreen = document.getElementById('climb-paused-screen');
        if (pauseScreen) pauseScreen.style.display = isPaused ? 'flex' : 'none';
    };

    window.resetToClimbMenu = function() {
        isGameRunning = false;
        isPaused = false;
        if (gameLoopId) clearInterval(gameLoopId);
        var el;
        el = document.getElementById('climb-game-ui'); if (el) el.style.display = 'flex';
        el = document.getElementById('climb-start-screen'); if (el) el.style.display = 'flex';
        el = document.getElementById('climb-game-over'); if (el) el.style.display = 'none';
        el = document.getElementById('climb-interaction'); if (el) el.style.display = 'none';
        el = document.getElementById('climb-paused-screen'); if (el) el.style.display = 'none';
        el = document.getElementById('climb-pause-btn'); if (el) el.innerText = 'Pause';
        el = document.getElementById('climb-interaction'); if (el) el.style.opacity = '1';
    };

    window.startClimbGame = function() {
        isPaused = false;
        var pBtn = document.getElementById('climb-pause-btn');
        if (pBtn) pBtn.innerText = 'Pause';
        var interaction = document.getElementById('climb-interaction');
        if (interaction) interaction.style.opacity = '1';
        climbScore = 0;
        climbFuel = 50;
        playerPosition = 35;
        isGameRunning = true;
        var el;
        el = document.getElementById('climb-start-screen'); if (el) el.style.display = 'none';
        el = document.getElementById('climb-game-over'); if (el) el.style.display = 'none';
        el = document.getElementById('climb-question-area'); if (el) el.style.display = 'block';
        el = document.getElementById('climb-interaction'); if (el) el.style.display = 'flex';
        updateDisplay();
        nextClimbQuestion();
        if (gameLoopId) clearInterval(gameLoopId);
        gameLoopId = setInterval(gameLoop, TICK_RATE);
    };

    function gameLoop() {
        if (!isGameRunning || isPaused) return;
        var isBoosting = spacePressed && climbFuel > 0;
        if (isBoosting) {
            playerPosition = Math.min(95, playerPosition + 0.5);
            climbFuel = Math.max(0, climbFuel - 0.2);
        }
        var fOut = document.getElementById('climb-flame-outer');
        var fIn = document.getElementById('climb-flame-inner');
        if (fOut && fIn) {
            var scale = isBoosting ? 'scale(1.2, 2.0)' : 'scale(1, 1)';
            fOut.style.transform = scale;
            fIn.style.transform = scale;
        }
        var effectiveFall = FALL_RATE;
        if (climbFuel <= 0) {
            downwardAccel += 0.007;
            effectiveFall += downwardAccel;
        } else {
            downwardAccel = 0;
        }
        playerPosition -= effectiveFall;
        climbFuel = Math.max(0, climbFuel - 0.1);
        if (playerPosition <= 0) { endGame(); }
        updatePlayerPos();
        updateFuelDisplay();
    }

    function updateDisplay() {
        var el = document.getElementById('climb-score');
        if (el) el.innerText = 'Score: ' + climbScore;
        updatePlayerPos();
        updateFuelDisplay();
    }

    function updateFuelDisplay() {
        var fill = document.getElementById('climb-fuel-fill');
        if (fill) fill.style.height = climbFuel + '%';
    }

    function updatePlayerPos() {
        var player = document.getElementById('climb-player');
        if (player) player.style.bottom = Math.max(0, playerPosition) + '%';
    }

    function nextClimbQuestion() {
        var feedback = document.getElementById('climb-feedback');
        if (feedback) { feedback.innerText = ''; feedback.className = ''; }
        if (!window.lessonFlashcards || window.lessonFlashcards.length === 0) {
            var qt = document.getElementById('climb-question-text');
            if (qt) qt.innerText = 'No flashcards found for this lesson!';
            return;
        }
        if (!window.usedFlashcardIndices) window.usedFlashcardIndices = [];
        var availablePool = window.lessonFlashcards.map(function(_, i) { return i; }).filter(function(i) { return window.usedFlashcardIndices.indexOf(i) === -1; });
        var qIdx;
        if (availablePool.length > 0) {
            qIdx = availablePool[Math.floor(Math.random() * availablePool.length)];
        } else {
            window.usedFlashcardIndices = [];
            qIdx = Math.floor(Math.random() * window.lessonFlashcards.length);
        }
        window.usedFlashcardIndices.push(qIdx);
        currentQuestion = window.lessonFlashcards[qIdx];
        var _tr = window.arisTranslate || function(t){return t;};
        var questionText = document.getElementById('climb-question-text');
        if (questionText) questionText.innerText = _tr(currentQuestion.question);

        var options = [currentQuestion.answer];
        var uniqueOptions = {};
        uniqueOptions[currentQuestion.answer] = true;
        var allAnswers = window.lessonFlashcards.map(function(f) { return f.answer; });
        for (var i = allAnswers.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = allAnswers[i]; allAnswers[i] = allAnswers[j]; allAnswers[j] = tmp;
        }
        for (var k = 0; k < allAnswers.length; k++) {
            if (!uniqueOptions[allAnswers[k]]) {
                options.push(allAnswers[k]);
                uniqueOptions[allAnswers[k]] = true;
                if (options.length >= 3) break;
            }
        }
        for (var i2 = options.length - 1; i2 > 0; i2--) {
            var j2 = Math.floor(Math.random() * (i2 + 1));
            var tmp2 = options[i2]; options[i2] = options[j2]; options[j2] = tmp2;
        }
        var optionsContainer = document.getElementById('climb-options');
        if (optionsContainer) {
            optionsContainer.innerHTML = '';
            options.forEach(function(opt) {
                var btn = document.createElement('button');
                btn.className = 'climb-option-btn';
                btn.innerText = _tr(opt);
                btn.onclick = function() { handleClimbAnswer(opt); };
                optionsContainer.appendChild(btn);
            });
        }
    }

    function handleClimbAnswer(selected) {
        if (!isGameRunning || isPaused) return;
        var feedback = document.getElementById('climb-feedback');
        if (selected === currentQuestion.answer) {
            climbScore += 10;
            climbFuel = Math.min(100, climbFuel + 20);
            if (feedback) { feedback.innerText = 'Correct! Adding fuel...'; feedback.style.color = '#16a34a'; }
        } else {
            playerPosition -= 5;
            if (feedback) { feedback.innerText = 'Oops! Slipping down...'; feedback.style.color = '#dc2626'; }
        }
        updateDisplay();
        var btns = document.querySelectorAll('.climb-option-btn');
        btns.forEach(function(b) { b.disabled = true; });
        setTimeout(function() { nextClimbQuestion(); }, 1000);
    }

    function endGame() {
        isGameRunning = false;
        clearInterval(gameLoopId);
        var el;
        el = document.getElementById('climb-question-area'); if (el) el.style.display = 'none';
        el = document.getElementById('climb-interaction'); if (el) el.style.display = 'none';
        var gameOverScreen = document.getElementById('climb-game-over');
        if (gameOverScreen) gameOverScreen.style.display = 'flex';
        var title = document.getElementById('climb-result-title');
        var msg = document.getElementById('climb-final-score');
        var storageKey = 'climbHighScore';
        try {
            var currentUser = JSON.parse(localStorage.getItem('user'));
            if (currentUser && currentUser.email) storageKey = 'climbHighScore_' + currentUser.email;
        } catch (e) { console.error(e); }
        var highScore = parseInt(localStorage.getItem(storageKey) || '0');
        if (climbScore > highScore) {
            highScore = climbScore;
            localStorage.setItem(storageKey, highScore);
            if (title) { title.innerText = '🏆 New High Score! 🏆'; title.style.color = '#f59e0b'; }
        } else {
            if (title) { title.innerText = 'Game Over'; title.style.color = '#1e293b'; }
        }
        if (msg) msg.innerHTML = 'Score: ' + climbScore + '<br><span style="font-size:0.9em; color:#64748b">Best: ' + highScore + '</span>';
    }
})();
