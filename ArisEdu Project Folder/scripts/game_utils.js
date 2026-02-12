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
