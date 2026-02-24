// game_switcher.js — Shared game switching logic for practice views
// Handles switching between Flashcards, Climb, Mix & Match, and Block Puzzle games.

(function() {
  window.switchToClimb = function() {
    ['flashcard-game', 'climb-game-container', 'mixmatch-container', 'blockpuzzle-container'].forEach(function(id) {
      var el = document.getElementById(id);
      if (el) el.style.display = 'none';
    });
    var climbGame = document.getElementById('climb-game-container');
    if (climbGame) { climbGame.style.display = 'block'; if (window.initClimbGame) window.initClimbGame(); }
  };

  window.switchToFlashcards = function() {
    ['flashcard-game', 'climb-game-container', 'mixmatch-container', 'blockpuzzle-container'].forEach(function(id) {
      var el = document.getElementById(id);
      if (el) el.style.display = 'none';
    });
    var flashcardGame = document.querySelector('.flashcard-game');
    if (flashcardGame) flashcardGame.style.display = 'flex';
    if (typeof window.initFlashcards === 'function') window.initFlashcards();
  };

  document.addEventListener('DOMContentLoaded', function() {
    // Climb Link
    document.querySelectorAll('a[href="#climb"]').forEach(function(el) {
      el.addEventListener('click', function(e) {
        e.preventDefault();
        window.switchToClimb();
        if (window.togglePracticesPanel && el.closest('.Practices-menu')) {
          var btn = el.closest('.Practices-menu').querySelector('.view-other-Practices');
          if (btn) window.togglePracticesPanel(btn);
        }
      });
    });

    // Flashcard Link
    document.querySelectorAll('a[href="#flashcard-game"]').forEach(function(el) {
      el.addEventListener('click', function(e) {
        e.preventDefault();
        window.switchToFlashcards();
        if (window.togglePracticesPanel && el.closest('.Practices-menu')) {
          var btn = el.closest('.Practices-menu').querySelector('.view-other-Practices');
          if (btn) window.togglePracticesPanel(btn);
        }
      });
    });
  });
})();
