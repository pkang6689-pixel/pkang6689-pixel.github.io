/**
 * Arcade Core - Shared functionality for all arcade games
 * Handles: Token drain, pause, game over, sidebar, Firebase
 */

let arcadeState = {
    gamePaused: false,
    gameOver: false,
    animFrame: null,
    timerIntervalId: null,
    drainIntervalId: null
};

/**
 * Initialize arcade game - call this at the start of each game
 * @param {string} gameTitle - Title of the game
 * @param {string} colorClass1 - First gradient color class (e.g., 'blue-400')
 * @param {string} colorClass2 - Second gradient color class (e.g., 'indigo-500')
 */
async function initializeArcadeGame(gameTitle, colorClass1, colorClass2) {
    await initializeFirebase();
    
    // Check access
    if (sessionStorage.getItem('validGameAccess') !== 'true') {
        alert('You must access this game from the Arcade page.');
        window.location.href = '../arcade.html';
        return false;
    }
    
    // Set up title if element exists
    const titleEl = document.querySelector('[role="game-title"]');
    if (titleEl) {
        titleEl.textContent = gameTitle;
    }
    
    // Reset game state (ensures pause screen is hidden, game over is hidden, etc)
    resetArcadeGame();
    
    // Initialize token drain
    initializeTokenDrain();
    
    return true;
}

/**
 * Show out of tokens popup
 */
function showOutOfTokensPopup() {
    clearInterval(arcadeState.timerIntervalId);
    clearInterval(arcadeState.drainIntervalId);

    const overlay = document.createElement('div');
    overlay.style.cssText = 'position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.8);backdrop-filter:blur(4px);z-index:99999;display:flex;align-items:center;justify-content:center;';
    
    const modal = document.createElement('div');
    modal.style.cssText = 'background:white;border-radius:1rem;padding:2rem;max-width:400px;text-align:center;box-shadow:0 20px 25px rgba(0,0,0,0.3);';
    
    modal.innerHTML = `
        <div style="font-size:3rem;margin-bottom:1rem;">💸</div>
        <h2 style="font-size:1.5rem;font-weight:700;margin-bottom:1rem;color:#1e293b;">Out of Tokens!</h2>
        <p style="margin-bottom:1.5rem;color:#64748b;">Your token balance hit zero.</p>
        <p style="margin-bottom:1.5rem;color:#94a3b8;font-size:0.85rem;">Earn more tokens by completing lessons and quizzes!</p>
        <button id="back-to-arcade" style="padding:0.75rem 1.5rem;border-radius:0.5rem;border:none;background:#f59e0b;color:#000;cursor:pointer;font-weight:700;font-size:1rem;">Back to Arcade</button>
    `;
    
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
    
    modal.querySelector('#back-to-arcade').onclick = () => {
        sessionStorage.removeItem('validGameAccess');
        window.location.href = '../arcade.html';
    };
}

/**
 * Initialize token drain system
 */
function initializeTokenDrain() {
    const sidebar = document.getElementById('game-sidebar');
    if (!sidebar) return;
    
    let timerDisplay = document.getElementById('game-session-timer');
    if (!timerDisplay) {
        timerDisplay = document.createElement('div');
        timerDisplay.id = 'game-session-timer';
        sidebar.appendChild(timerDisplay);
    }

    function updateTimerDisplay() {
        const user = JSON.parse(localStorage.getItem('user') || '{}');
        const remaining = Math.max(0, user.points || 0);
        timerDisplay.textContent = remaining + '💎';
        timerDisplay.className = remaining <= 20 ? 'warning' : '';
        
        if (remaining <= 0) {
            showOutOfTokensPopup();
        }
    }
    
    function drainTokens() {
        const user = JSON.parse(localStorage.getItem('user') || '{}');
        const pts = user.points || 0;
        if (pts > 0 && !arcadeState.gamePaused && !arcadeState.gameOver) {
            user.points = pts - 1;
            localStorage.setItem('user', JSON.stringify(user));
            updateTimerDisplay();
            if (user.points <= 0) {
                showOutOfTokensPopup();
            }
        }
    }

    if (arcadeState.timerIntervalId) clearInterval(arcadeState.timerIntervalId);
    if (arcadeState.drainIntervalId) clearInterval(arcadeState.drainIntervalId);
    
    updateTimerDisplay();
    
    const user = JSON.parse(localStorage.getItem('user') || '{}');
    if ((user.points || 0) > 0) {
        arcadeState.drainIntervalId = setInterval(drainTokens, 1000);
    } else {
        showOutOfTokensPopup();
    }
}

/**
 * Toggle pause state
 */
function togglePause() {
    if (arcadeState.gameOver) return;
    arcadeState.gamePaused = !arcadeState.gamePaused;
    const pauseScreen = document.getElementById('pause-screen');
    if (pauseScreen) {
        if (arcadeState.gamePaused) {
            pauseScreen.style.display = 'flex';
        } else {
            pauseScreen.style.display = 'none';
        }
    }
}

/**
 * Set game over state
 */
function setGameOver(isGameOver = true) {
    arcadeState.gameOver = isGameOver;
    const gameOverScreen = document.getElementById('game-over');
    if (gameOverScreen) {
        if (isGameOver) {
            gameOverScreen.style.display = 'flex';
        } else {
            gameOverScreen.style.display = 'none';
        }
    }
}

/**
 * Reset game state
 */
function resetArcadeGame() {
    arcadeState.gamePaused = false;
    arcadeState.gameOver = false;
    const gameOverScreen = document.getElementById('game-over');
    const pauseScreen = document.getElementById('pause-screen');
    if (gameOverScreen) gameOverScreen.style.display = 'none';
    if (pauseScreen) pauseScreen.style.display = 'none';
}

/**
 * Check if game is paused
 */
function isGamePaused() {
    return arcadeState.gamePaused;
}

/**
 * Check if game is over
 */
function isGameOver() {
    return arcadeState.gameOver;
}

/**
 * Get paused or game over state
 */
function shouldSkipGameUpdate() {
    return arcadeState.gamePaused || arcadeState.gameOver;
}

/**
 * Stop token drain when exiting
 */
function stopArcadeGame() {
    clearInterval(arcadeState.timerIntervalId);
    clearInterval(arcadeState.drainIntervalId);
    if (arcadeState.animFrame) {
        cancelAnimationFrame(arcadeState.animFrame);
    }
}

// Clean up on page unload
window.addEventListener('beforeunload', stopArcadeGame);

// Global keyboard shortcut for pause (P / Escape) — works for all arcade games
document.addEventListener('keydown', function(e) {
    if (e.key === 'p' || e.key === 'P' || e.key === 'Escape') {
        // Don't pause if start screen is still visible
        const startScreen = document.getElementById('start-screen');
        if (startScreen && startScreen.style.display !== 'none') return;
        e.preventDefault();
        togglePause();
    }
});

/**
 * Auto-scale the main game canvas to fill available wrapper space.
 * Sets CSS width/height on the largest canvas inside #game-wrapper.
 * Canvas rendering resolution (attributes) stays unchanged.
 * Games with mouse input must use corrected coordinates:
 *   const scaleX = canvas.width / rect.width;
 *   const x = (e.clientX - rect.left) * scaleX;
 */
(function() {
    function findMainCanvas() {
        var w = document.getElementById('game-wrapper');
        if (!w) return null;
        var main = null, maxA = 0;
        w.querySelectorAll('canvas').forEach(function(c) {
            var a = c.width * c.height;
            if (a > maxA) { maxA = a; main = c; }
        });
        return main;
    }

    function scaleCanvas() {
        var wrapper = document.getElementById('game-wrapper');
        var mc = findMainCanvas();
        if (!wrapper || !mc || mc.width < 1 || mc.height < 1) return;

        // Measure non-canvas sibling heights once
        if (mc._sibH == null) {
            mc._sibH = 0;
            for (var i = 0; i < wrapper.children.length; i++) {
                var ch = wrapper.children[i];
                if (ch === mc || ch.contains(mc) || ch.tagName === 'CANVAS') continue;
                var s = getComputedStyle(ch);
                if (s.position === 'absolute' || s.position === 'fixed' || s.display === 'none') continue;
                mc._sibH += ch.offsetHeight + parseFloat(s.marginTop || 0) + parseFloat(s.marginBottom || 0);
            }
            mc._sibH = Math.max(mc._sibH, 40);
        }

        var cs = getComputedStyle(wrapper);
        var pX = parseFloat(cs.paddingLeft || 0) + parseFloat(cs.paddingRight || 0);
        var pY = parseFloat(cs.paddingTop || 0) + parseFloat(cs.paddingBottom || 0);
        var wR = wrapper.getBoundingClientRect();
        var availW = wR.width - pX;
        var availH = wR.height - pY - mc._sibH;

        if (availW < 50 || availH < 50) return;

        var ratio = mc.width / mc.height;
        var dW, dH;
        if (availW / availH > ratio) { dH = availH; dW = dH * ratio; }
        else { dW = availW; dH = dW / ratio; }

        mc.style.width = Math.floor(dW) + 'px';
        mc.style.height = Math.floor(dH) + 'px';
    }

    window.addEventListener('load', function() { setTimeout(scaleCanvas, 80); });
    var rt;
    window.addEventListener('resize', function() { clearTimeout(rt); rt = setTimeout(scaleCanvas, 200); });
    // Expose so games can re-trigger after dynamic canvas resize
    window._acScaleCanvas = scaleCanvas;
})();