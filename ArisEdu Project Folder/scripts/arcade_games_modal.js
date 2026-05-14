// arcade_games_modal.js — replaces "Other games" dropdown with a card-grid modal

(function() {

var GAMES = [
  // Study tools — inline on practice page
  { inline: 'flashcard',   title: 'Flashcard Game',  desc: 'Study with flippable question cards!', category: 'study',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="8" y="12" width="48" height="32" rx="4" fill="#3b82f6"/><rect x="14" y="18" width="36" height="20" rx="2" fill="#1e3a5f"/><path d="M 22 28 L 28 34 L 42 20" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><rect x="20" y="44" width="24" height="4" rx="2" fill="#60a5fa" opacity=".6"/><rect x="24" y="48" width="16" height="4" rx="2" fill="#60a5fa" opacity=".4"/></svg>' },
  { inline: 'blockpuzzle', title: 'Block Puzzle',    desc: 'Drag & drop shapes, clear rows!',      category: 'study',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="8" y="8" width="12" height="12" rx="2" fill="#14b8a6"/><rect x="22" y="8" width="12" height="12" rx="2" fill="#0d9488"/><rect x="8" y="22" width="12" height="12" rx="2" fill="#0d9488"/><rect x="22" y="22" width="12" height="12" rx="2" fill="#14b8a6"/><rect x="36" y="22" width="12" height="12" rx="2" fill="#14b8a6" opacity=".5"/><rect x="8" y="36" width="12" height="12" rx="2" fill="#14b8a6" opacity=".5"/><rect x="22" y="36" width="12" height="12" rx="2" fill="#0d9488" opacity=".5"/><rect x="36" y="36" width="12" height="12" rx="2" fill="#14b8a6" opacity=".3"/><rect x="36" y="8" width="12" height="12" rx="2" fill="#14b8a6" opacity=".3"/></svg>' },
  // Modern games
  { href: '../../../games/GameArena.html',      title: 'Apocalypse Arena', desc: 'Survive endless waves of enemies!',          category: 'modern', icon: '<span style="font-size:2.2rem">⚔️</span>' },
  { href: '../../../games/GameAvoid.html',      title: 'AVOIDance',        desc: 'Dodge the red blocks!',                      category: 'modern',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><circle cx="32" cy="32" r="10" fill="#3b82f6"/><rect x="8" y="8" width="12" height="12" rx="2" fill="#ef4444" transform="rotate(45 14 14)"/><rect x="44" y="12" width="10" height="10" rx="2" fill="#ef4444" transform="rotate(15 49 17)"/><rect x="12" y="44" width="14" height="14" rx="2" fill="#ef4444" transform="rotate(-20 19 51)"/><rect x="48" y="46" width="8" height="8" rx="2" fill="#ef4444" transform="rotate(60 52 50)"/><path d="M 32 32 L 40 18" stroke="#3b82f6" stroke-width="4" stroke-dasharray="4 4" opacity="0.6" stroke-linecap="round"/></svg>' },
  { href: '../../../games/GameBubble.html',     title: 'Bubble Shooter',   desc: 'Shoot bubbles, match colors!',               category: 'retro',  icon: '<span style="font-size:2.2rem">🫧</span>' },
  { href: '../../../games/GameMemory.html',     title: 'Card Match',       desc: 'Find the matching pairs!',                   category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="6" y="8" width="22" height="32" rx="4" fill="#f8fafc" stroke="#94a3b8" stroke-width="2" transform="rotate(-15 17 24)"/><path d="M 17 24 L 17 18 M 14 21 L 20 21" stroke="#ef4444" stroke-width="3" stroke-linecap="round" transform="rotate(-15 17 24)"/><rect x="28" y="16" width="24" height="36" rx="4" fill="#334155" stroke="#475569" stroke-width="2" transform="rotate(10 40 34)"/><circle cx="40" cy="34" r="6" fill="#a8a29e" transform="rotate(10 40 34)"/></svg>' },
  { href: '../../../games/GameCraft2D.html',    title: 'Craft 2D',         desc: 'Mine, place blocks, build your world!',      category: 'modern', icon: '<span style="font-size:2.2rem">⛏️</span>' },
  { href: '../../../games/GameCatch.html',      title: 'Fruit Catcher',    desc: 'Catch falling fruits!',                      category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><path d="M 12 40 L 20 56 L 44 56 L 52 40 Z" fill="#f59e0b"/><circle cx="32" cy="24" r="8" fill="#22c55e"/><path d="M 32 16 Q 35 10 40 12" stroke="#16a34a" stroke-width="3" stroke-linecap="round" fill="none"/><circle cx="18" cy="16" r="6" fill="#ef4444"/><circle cx="48" cy="28" r="5" fill="#f97316"/></svg>' },
  { href: '../../../games/GameTower.html',      title: 'Lab Defense',      desc: 'Defend your lab against attacks!',           category: 'modern', icon: '<span style="font-size:2.2rem">🧪</span>' },
  { href: '../../../games/GameFactory.html',    title: 'Particle Clicker', desc: 'Click, upgrade, build your particle empire!', category: 'modern', icon: '<span style="font-size:2.2rem">⚛️</span>' },
  { href: '../../../games/GamePlatformer.html', title: 'Platformer',       desc: 'Jump, run, and reach the flag!',             category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="4" y="52" width="56" height="8" rx="2" fill="#3b82f6" opacity=".3"/><rect x="20" y="36" width="24" height="6" rx="2" fill="#3b82f6" opacity=".5"/><rect x="36" y="20" width="20" height="6" rx="2" fill="#3b82f6" opacity=".7"/><rect x="8" y="20" width="16" height="6" rx="2" fill="#3b82f6" opacity=".7"/><rect x="24" y="42" width="8" height="10" rx="1" fill="#3b82f6"/><circle cx="28" cy="38" r="5" fill="#60a5fa"/><circle cx="26" cy="37" r="1" fill="white"/><circle cx="30" cy="37" r="1" fill="white"/></svg>' },
  { href: '../../../games/GameJump.html',       title: 'Runner',           desc: 'Jump over obstacles!',                       category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="0" y="52" width="64" height="4" fill="#e2e8f0"/><rect x="12" y="24" width="16" height="16" rx="4" fill="#3b82f6"/><rect x="44" y="40" width="12" height="12" rx="2" fill="#ef4444"/><path d="M 18 42 L 14 52 M 22 42 L 26 52" stroke="#3b82f6" stroke-width="4" stroke-linecap="round"/></svg>' },
  { href: '../../../games/GameShoot.html',      title: 'Target Aim',       desc: 'Click targets quickly!',                     category: 'modern',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><circle cx="32" cy="32" r="24" fill="#ef4444"/><circle cx="32" cy="32" r="16" fill="#f8fafc"/><circle cx="32" cy="32" r="8" fill="#ef4444"/><path d="M 32 2 L 32 14 M 32 62 L 32 50 M 2 32 L 14 32 M 62 32 L 50 32" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg>' },
  { href: '../../../games/GameSpaceship.html',  title: 'Space Shooter',    desc: 'Blast enemies, dodge asteroids!',            category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><polygon points="32,4 22,44 32,38 42,44" fill="#8b5cf6"/><polygon points="32,38 22,44 18,52 32,46" fill="#7c3aed"/><polygon points="32,38 42,44 46,52 32,46" fill="#6d28d9"/><rect x="30" y="46" width="4" height="10" rx="1" fill="#f97316"/></svg>' },
  // Retro / classic games
  { href: '../../../games/Game2048.html',       title: '2048',             desc: 'Slide tiles, merge to 2048!',                category: 'retro',  icon: '<span style="font-size:2.2rem">2️⃣</span>' },
  { href: '../../../games/GameBreakout.html',   title: 'Breakout',         desc: 'Smash all the bricks!',                      category: 'retro',  icon: '<span style="font-size:2.2rem">🧱</span>' },
  { href: '../../../games/GameFlappy.html',     title: 'Flappy Bird',      desc: 'Tap to fly, dodge the pipes!',               category: 'retro',  icon: '<span style="font-size:2.2rem">🐦</span>' },
  { href: '../../../games/GameMinesweeper.html',title: 'Minesweeper',      desc: 'Find all the safe squares!',                 category: 'retro',  icon: '<span style="font-size:2.2rem">💣</span>' },
  { href: '../../../games/GamePacman.html',     title: 'Pac-Man',          desc: 'Chomp pellets, dodge ghosts!',               category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><path d="M32 8 A24 24 0 1 1 32 56 A24 24 0 0 1 32 8 Z" fill="#facc15"/><path d="M32 32 L56 20 L56 44 Z" fill="#1e293b"/><circle cx="36" cy="22" r="3" fill="#0f172a"/></svg>' },
  { href: '../../../games/GamePong.html',       title: 'Pong',             desc: 'Classic paddle game!',                       category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="8" y="20" width="8" height="24" rx="4" fill="#3b82f6"/><rect x="48" y="20" width="8" height="24" rx="4" fill="#ef4444"/><circle cx="32" cy="32" r="6" fill="#f8fafc"/><path d="M 32 8 L 32 56" stroke="#334155" stroke-width="2" stroke-dasharray="4 4"/></svg>' },
  { href: '../../../games/GameSnake.html',      title: 'Snake',            desc: 'Eat apples, grow longer!',                   category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="8" y="28" width="8" height="8" rx="1" fill="#22c55e"/><rect x="16" y="28" width="8" height="8" rx="1" fill="#16a34a"/><rect x="24" y="28" width="8" height="8" rx="1" fill="#22c55e"/><rect x="32" y="28" width="8" height="8" rx="1" fill="#16a34a"/><rect x="32" y="20" width="8" height="8" rx="1" fill="#22c55e"/><rect x="40" y="20" width="8" height="8" rx="1" fill="#16a34a"/><circle cx="46" cy="23" r="1.5" fill="white"/><circle cx="52" cy="44" r="4" fill="#ef4444"/></svg>' },
  { href: '../../../games/GameTetris.html',     title: 'Tetris',           desc: 'Stack blocks, clear lines!',                 category: 'retro',
    icon: '<svg viewBox="0 0 64 64" width="44" height="44" fill="none"><rect x="16" y="8" width="10" height="10" rx="1" fill="#ef4444"/><rect x="26" y="8" width="10" height="10" rx="1" fill="#ef4444"/><rect x="26" y="18" width="10" height="10" rx="1" fill="#ef4444"/><rect x="36" y="18" width="10" height="10" rx="1" fill="#ef4444"/><rect x="8" y="44" width="10" height="10" rx="1" fill="#3b82f6"/><rect x="18" y="44" width="10" height="10" rx="1" fill="#3b82f6"/><rect x="28" y="44" width="10" height="10" rx="1" fill="#3b82f6"/><rect x="38" y="44" width="10" height="10" rx="1" fill="#3b82f6"/></svg>' }
];

function buildModal() {
    var overlay = document.createElement('div');
    overlay.id = 'arcade-games-modal-overlay';
    overlay.style.cssText = [
        'display:none',
        'position:fixed',
        'inset:0',
        'background:rgba(0,0,0,0.65)',
        'backdrop-filter:blur(4px)',
        'z-index:9999',
        'align-items:center',
        'justify-content:center',
        'padding:1rem'
    ].join(';');

    var box = document.createElement('div');
    box.style.cssText = [
        'background:#0f172a',
        'border:1px solid #1e293b',
        'border-radius:1.25rem',
        'width:min(900px,96vw)',
        'max-height:80vh',
        'display:flex',
        'flex-direction:column',
        'overflow:hidden',
        'box-shadow:0 24px 48px rgba(0,0,0,0.5)'
    ].join(';');

    // Header
    var header = document.createElement('div');
    header.style.cssText = 'display:flex;align-items:center;justify-content:space-between;padding:1.25rem 1.5rem;border-bottom:1px solid #1e293b;flex-shrink:0;';
    header.innerHTML = '<h2 style="margin:0;font-size:1.25rem;font-weight:700;color:#f1f5f9;">🎮 Arcade Games</h2>';
    var closeBtn = document.createElement('button');
    closeBtn.innerHTML = '✕';
    closeBtn.style.cssText = 'background:none;border:none;color:#94a3b8;font-size:1.25rem;cursor:pointer;padding:0.25rem 0.5rem;border-radius:0.375rem;line-height:1;';
    closeBtn.onmouseenter = function() { closeBtn.style.color = '#f1f5f9'; closeBtn.style.background = '#1e293b'; };
    closeBtn.onmouseleave = function() { closeBtn.style.color = '#94a3b8'; closeBtn.style.background = 'none'; };
    closeBtn.onclick = closeModal;
    header.appendChild(closeBtn);

    // Grid
    var grid = document.createElement('div');
    grid.style.cssText = 'overflow-y:auto;padding:1.25rem;display:grid;grid-template-columns:repeat(3,1fr);gap:0.875rem;';

    var categoryOrder = ['study', 'modern', 'retro'];
    var categoryLabels = { study: '📚 Primary Tools', modern: '✨ Modern Style', retro: '👾 Retro Style' };
    categoryOrder.forEach(function(catKey) {
        var catGames = GAMES.filter(function(g) { return g.category === catKey; });
        if (!catGames.length) return;
        var sectionHead = document.createElement('div');
        sectionHead.style.cssText = 'grid-column:1/-1;color:#94a3b8;font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;padding:0.5rem 0 0.25rem;border-bottom:1px solid #1e293b;margin-top:0.25rem;';
        sectionHead.textContent = categoryLabels[catKey];
        grid.appendChild(sectionHead);
        catGames.forEach(function(g) {
    var card = document.createElement('button');
        card.type = 'button';
        card.style.cssText = [
            'background:#1e293b',
            'border:1px solid #334155',
            'border-radius:0.875rem',
            'padding:1rem 0.875rem',
            'cursor:pointer',
            'text-align:left',
            'transition:transform 0.15s,box-shadow 0.15s,border-color 0.15s',
            'display:flex',
            'flex-direction:column',
            'gap:0.5rem'
        ].join(';');
        card.innerHTML =
            '<div style="display:flex;align-items:center;justify-content:center;height:56px;">' + g.icon + '</div>' +
            '<div style="font-size:0.8rem;font-weight:700;color:#f1f5f9;text-transform:uppercase;letter-spacing:0.04em;">' + g.title + '</div>' +
            '<div style="font-size:0.72rem;color:#64748b;line-height:1.4;">' + g.desc + '</div>';
        card.onmouseenter = function() {
            card.style.transform = 'translateY(-3px)';
            card.style.boxShadow = '0 8px 20px rgba(0,0,0,0.3)';
            card.style.borderColor = '#475569';
        };
        card.onmouseleave = function() {
            card.style.transform = '';
            card.style.boxShadow = '';
            card.style.borderColor = '#334155';
        };
        if (g.inline) {
            // Show existing inline container
            (function(inlineKey) {
                card.onclick = function() {
                    closeModal();
                    var flashcard = document.getElementById('flashcard-game');
                    var blockpuzzle = document.getElementById('blockpuzzle-container');
                    var iframeContainer = document.getElementById('arcade-iframe-container');
                    if (iframeContainer) { iframeContainer.style.display = 'none'; var fr = document.getElementById('arcade-iframe'); if (fr) fr.src = ''; }
                    if (inlineKey === 'flashcard') {
                        if (blockpuzzle) blockpuzzle.style.display = 'none';
                        if (flashcard) { flashcard.style.display = ''; flashcard.scrollIntoView({behavior:'smooth',block:'start'}); }
                    } else {
                        if (flashcard) flashcard.style.display = 'none';
                        if (blockpuzzle) { blockpuzzle.style.display = 'flex'; blockpuzzle.scrollIntoView({behavior:'smooth',block:'start'}); }
                    }
                };
            })(g.inline);
        } else {
            // Arcade iframe game — call the launcher from practice_games.js directly
            (function(game) {
                card.onclick = function() {
                    closeModal();
                    if (typeof window._launchArcadeGame === 'function') {
                        window._launchArcadeGame(game.href, game.title);
                    }
                };
            })(g);
        }
        grid.appendChild(card);
        }); // end catGames.forEach
    }); // end categoryOrder.forEach

    box.appendChild(header);
    box.appendChild(grid);
    overlay.appendChild(box);

    // Close on backdrop click
    overlay.onclick = function(e) { if (e.target === overlay) closeModal(); };
    // Close on Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeModal();
    });

    document.body.appendChild(overlay);
    return overlay;
}

function openModal() {
    var overlay = document.getElementById('arcade-games-modal-overlay') || buildModal();
    overlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    var overlay = document.getElementById('arcade-games-modal-overlay');
    if (overlay) overlay.style.display = 'none';
    document.body.style.overflow = '';
}

// Intercept "Other games" button — replace dropdown toggle with modal open
// The inline onclick="togglePracticesPanel(this)" fires before this listener,
// so we force-close the panel it just opened.
document.addEventListener('click', function(e) {
    var btn = e.target.closest('.view-other-Practices');
    if (!btn) return;
    e.stopImmediatePropagation();
    e.preventDefault();
    // Close the dropdown panel the inline handler just opened
    var menu = btn.closest('.Practices-menu') || btn.closest('.side-buttons');
    if (menu) {
        var panel = menu.querySelector('.Practices-panel');
        if (panel) { panel.classList.remove('is-open'); panel.setAttribute('aria-hidden', 'true'); }
    }
    openModal();
});

})();
