/**
 * Arcade Core - Shared functionality for all arcade games
 * Handles: Token drain, pause, game over, sidebar, Firebase
 */

// Embed mode: hide sidebar immediately before DOM renders (prevents flash)
// Games can set window.keepSidebarInEmbed = true (before this script) to keep sidebar visible
if (new URLSearchParams(window.location.search).get('embed') === '1') {
    (function() {
        var s = document.createElement('style');
        var sidebarRule = window.keepSidebarInEmbed ? '' : '#game-sidebar{display:none!important}';
        var flexRule = window.keepSidebarInEmbed
            ? 'body>.flex{height:100%!important;flex-direction:row!important;padding:0.5rem!important}'
            : 'body>.flex{height:100%!important;flex-direction:column!important;padding:0.5rem!important}';
        s.textContent = sidebarRule + 'html,body{height:100%!important;overflow:hidden!important;padding:0!important;margin:0!important}' + flexRule + '#game-wrapper{width:100%!important;max-width:100%!important;height:100%!important;flex:1!important;min-height:0!important}';
        document.head.appendChild(s);
    })();
}

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
    
    // Set up title if element exists
    const titleEl = document.querySelector('[role="game-title"]');
    if (titleEl) {
        titleEl.textContent = gameTitle;
    }
    
    // Reset game state (ensures pause screen is hidden, game over is hidden, etc)
    resetArcadeGame();
    
    return true;
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