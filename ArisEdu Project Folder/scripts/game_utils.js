// Game Switcher Logic & Auto-Initialization
document.addEventListener('DOMContentLoaded', () => {
    
    // Helper to hide all game containers
    function hideAllGames() {
        const games = ['flashcard-game', 'climb-game-container', 'mixmatch-container', 'blockpuzzle-container'];
        games.forEach(id => {
            const el = document.getElementById(id);
            if(el) el.style.display = 'none';
        });
    }

    // MixMatch Switch
    window.switchToMixMatch = function() {
        hideAllGames();
        const el = document.getElementById('mixmatch-container');
        if(el) {
            el.style.display = 'flex';
            if(window.initMixMatch) window.initMixMatch();
        }
    };

    // BlockPuzzle Switch
    window.switchToBlockPuzzle = function() {
        hideAllGames();
        const el = document.getElementById('blockpuzzle-container');
        if(el) {
            el.style.display = 'flex';
            if(window.initBlockPuzzle) window.initBlockPuzzle();
        }
    };

    // Listeners for Menu Links
    document.querySelectorAll('a[href="#mixmatch"]').forEach(el => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            window.switchToMixMatch();
            if(window.togglePracticesPanel) {
                const practicesMenu = el.closest('.Practices-menu');
                if (practicesMenu) {
                     window.togglePracticesPanel(practicesMenu.querySelector('button'));
                }
            }
        });
    });

    document.querySelectorAll('a[href="#blockpuzzle"]').forEach(el => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            window.switchToBlockPuzzle();
            if(window.togglePracticesPanel) {
                const practicesMenu = el.closest('.Practices-menu');
                if (practicesMenu) {
                     window.togglePracticesPanel(practicesMenu.querySelector('button'));
                }
            }
        });
    });
    
    // Patch existing Flashcards/Climb listeners to ensure they hide new games
    const oldFlash = window.switchToFlashcards;
    window.switchToFlashcards = function() {
        hideAllGames();
        const el = document.getElementById('flashcard-game');
        if(el) el.style.display = 'flex';
    };

    // Auto-initialize flashcards if available
    if (typeof window.initFlashcards === 'function') {
        window.initFlashcards();
    }
});

// Global Quiz Reset Logic
window.resetQuizQuestion = function(btn) {
    const p = btn.closest('.quiz-question');
    if (!p) return;
    
    // Remove feedback
    const f = p.querySelector('.feedback');
    if (f) f.remove();
    
    // Re-enable and uncheck inputs
    p.querySelectorAll('input').forEach(i => {
        i.disabled = false;
        i.checked = false;
    });
    
    // Reset status
    p.dataset.status = '';
    
    // Reset attempts count and display
    p.dataset.attempts = '2'; 
    const attemptsIndicator = p.querySelector('.attempts-indicator');
    if (attemptsIndicator) {
        attemptsIndicator.style.display = 'none';
        attemptsIndicator.textContent = '';
    }
    
    // Re-enable Submit button
    // Look for previous sibling usually, or query inside parent
    const submitBtn = p.querySelector('.action-button');
    if (submitBtn) {
        submitBtn.disabled = false;
    }
};
