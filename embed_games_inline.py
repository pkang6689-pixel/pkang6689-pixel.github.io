import os
import re
from bs4 import BeautifulSoup

# --- 1. Prepare Mix & Match Content ---
mixmatch_html = """
<div id="mixmatch-container" style="display:none; flex-direction:column; align-items:center; width:100%;">
    <div class="w-full max-w-4xl flex justify-between items-center mb-8">
        <div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">Mix & Match</h1>
            <p class="text-slate-400">Match the terms to their definitions!</p>
        </div>
        <div class="text-right">
            <div class="text-sm text-slate-400">Streak</div>
            <div id="mixmatch-streak-display" class="text-2xl font-bold text-yellow-400">0</div>
        </div>
    </div>

    <div id="mixmatch-game-board" class="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-4xl">
        <!-- Cards injected here -->
    </div>

    <div id="mixmatch-win-screen" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
        <div class="bg-slate-800 p-8 rounded-2xl text-center border border-slate-700 max-w-md mx-4">
            <div class="text-6xl mb-4">🎉</div>
            <h2 class="text-3xl font-bold mb-2">Level Complete!</h2>
            <p class="text-slate-400 mb-6">You matched all terms correctly.</p>
            <button onclick="window.startMixMatchGame()" class="bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-8 rounded-full transition-all hover:scale-105 active:scale-95">
                Play Again
            </button>
        </div>
    </div>
</div>
"""

mixmatch_js = """
(function() {
    window.initMixMatch = function() {
        if(window.mixMatchInitialized) return;
        window.mixMatchInitialized = true;
        window.startMixMatchGame();
    };

    const vocabulary = [
        { term: "Atom", def: "Basic unit of Matter" },
        { term: "Proton", def: "Positively charged particle" },
        { term: "Electron", def: "Negatively charged particle" },
        { term: "Neutron", def: "Neutral particle in nucleus" },
        { term: "Isotope", def: "Same protons, different neutrons" },
        { term: "Ion", def: "Charged atom or molecule" },
        { term: "Molecule", def: "Group of atoms bonded together" },
        { term: "Element", def: "Pure substance of one atom type" }
    ];

    let selectedCards = [];
    let matchedPairs = 0;
    let streak = 0;

    window.startMixMatchGame = function() {
        const gameContainer = document.getElementById('mixmatch-game-board');
        const winScreen = document.getElementById('mixmatch-win-screen');
        
        gameContainer.innerHTML = '';
        winScreen.classList.add('hidden');
        selectedCards = [];
        matchedPairs = 0;
        streak = 0;
        updateStreak(0);

        let gameItems = [];
        vocabulary.forEach((item, index) => {
            gameItems.push({ id: index, text: item.term, type: 'term' });
            gameItems.push({ id: index, text: item.def, type: 'def' });
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
        const isMatch = c1.dataset.id === c2.dataset.id && c1.dataset.type !== c2.dataset.type;

        if (isMatch) {
            setTimeout(() => {
                c1.classList.add('invisible', 'opacity-0', 'transition-opacity', 'duration-500');
                c2.classList.add('invisible', 'opacity-0', 'transition-opacity', 'duration-500');
                matchedPairs++;
                updateStreak(1);
                if (matchedPairs === vocabulary.length) {
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
"""

# --- 2. Prepare Block Puzzle Content ---
blockpuzzle_html = """
<div id="blockpuzzle-container" style="display:none; flex-direction:column; align-items:center; justify-content:center; width:100%;">
    <div class="relative w-full max-w-md bg-gray-800 rounded-2xl shadow-2xl p-6 border border-gray-700">
        <div class="flex justify-between items-end mb-6">
            <div>
                <h1 class="text-2xl font-bold bg-gradient-to-r from-green-400 to-emerald-600 bg-clip-text text-transparent">BLOCK PUZZLE</h1>
                <p class="text-xs text-gray-400">Clear lines to score!</p>
            </div>
            <div class="text-right">
                <div class="text-xs text-gray-400 font-sans">SCORE</div>
                <div id="bp-score" class="text-3xl font-bold text-white">0</div>
            </div>
        </div>

        <div id="bp-board" class="grid grid-cols-8 gap-1 bg-gray-900 p-2 rounded-lg border-2 border-gray-700 mx-auto" style="width: 340px; height: 340px;">
        </div>

        <div id="bp-hand" class="mt-8 flex justify-center gap-4 h-24 items-center min-h-[6rem]">
        </div>

        <div id="bp-game-over" class="hidden absolute inset-0 bg-black/90 rounded-2xl z-20 flex flex-col items-center justify-center text-center p-6 backdrop-blur-sm">
            <h2 class="text-3xl text-red-500 font-bold mb-2">GAME OVER</h2>
            <p class="text-gray-300 mb-6">No more moves possible!</p>
            <div class="text-4xl font-bold text-white mb-8" id="bp-final-score">0</div>
            <button onclick="window.resetBlockGame()" class="bg-green-600 hover:bg-green-500 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition active:scale-95">
                TRY AGAIN
            </button>
        </div>
    </div>
</div>
"""

blockpuzzle_js = """
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
    let activeSelection = null;

    window.initBlockPuzzle = function() {
        if(window.bpInitialized) return;
        window.bpInitialized = true;
        window.resetBlockGame();
    };

    window.resetBlockGame = function() {
        grid = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(0));
        score = 0;
        document.getElementById('bp-score').innerText = 0;
        initBoard();
        spawnBlocks();
        document.getElementById('bp-game-over').classList.add('hidden');
    };

    function initBoard() {
        const boardEl = document.getElementById('bp-board');
        boardEl.innerHTML = '';
        for(let y=0; y<BOARD_SIZE; y++) {
            for(let x=0; x<BOARD_SIZE; x++) {
                const cell = document.createElement('div');
                cell.className = 'w-full h-full bg-gray-800 rounded-sm';
                cell.dataset.x = x;
                cell.dataset.y = y;
                cell.onclick = (e) => handleBoardClick(x, y);
                boardEl.appendChild(cell);
            }
        }
    }

    function handleBoardClick(x, y) {
        if(!activeSelection) return;
        tryPlaceBlock(x, y);
    }

    function spawnBlocks() {
        const handEl = document.getElementById('bp-hand');
        handEl.innerHTML = '';
        for(let i=0; i<3; i++) {
            const shape = SHAPES[Math.floor(Math.random() * SHAPES.length)];
            const color = colors[Math.floor(Math.random() * colors.length)];
            createDraggableBlock(shape, color);
        }
    }

    function createDraggableBlock(shapeMatrix, color) {
        const handEl = document.getElementById('bp-hand');
        const container = document.createElement('div');
        container.className = 'block-shape relative cursor-pointer';
        const size = 15;
        const w = shapeMatrix[0].length * size;
        const h = shapeMatrix.length * size;
        container.style.width = `${w}px`;
        container.style.height = `${h}px`;
        
        shapeMatrix.forEach((row, r) => {
            row.forEach((active, c) => {
                if(active) {
                    const block = document.createElement('div');
                    block.style.position = 'absolute';
                    block.style.left = `${c * size}px`;
                    block.style.top = `${r * size}px`;
                    block.style.width = `${size-1}px`;
                    block.style.height = `${size-1}px`;
                    block.style.backgroundColor = color;
                    container.appendChild(block);
                }
            });
        });

        container.onclick = (e) => selectBlock(container, shapeMatrix, color);
        handEl.appendChild(container);
    }

    function selectBlock(el, shape, color) {
        if (activeSelection) {
            activeSelection.el.style.opacity = '1';
            activeSelection.el.style.border = 'none';
        }
        activeSelection = { el, shape, color };
        el.style.opacity = '0.7';
        el.style.border = '2px dashed white';
    }

    function tryPlaceBlock(x, y) {
        const { shape, color } = activeSelection;
        if (canPlace(shape, x, y)) {
            place(shape, x, y, color);
            activeSelection.el.remove();
            activeSelection = null;
            checkLines();
            if (document.getElementById('bp-hand').children.length === 0) spawnBlocks();
            // checkGameOver(); // Simplified for now
        }
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
        for (let r=0; r<shape.length; r++) {
            for (let c=0; c<shape[0].length; c++) {
                if (shape[r][c]) {
                    grid[y+r][x+c] = 1;
                    const cell = document.getElementById('bp-board').children[(y+r) * BOARD_SIZE + (x+c)];
                    cell.style.backgroundColor = color;
                    cell.style.boxShadow = `0 0 10px ${color}`;
                }
            }
        }
        score += 10;
        document.getElementById('bp-score').innerText = score;
    }

    function checkLines() {
        let linesCleared = 0;
        // Rows
        for(let y=0; y<BOARD_SIZE; y++) {
            if(grid[y].every(v => v === 1)) {
                clearRow(y);
                linesCleared++;
            }
        }
        // Cols
        for(let x=0; x<BOARD_SIZE; x++) {
            if(grid.every(row => row[x] === 1)) {
                clearCol(x);
                linesCleared++;
            }
        }
        if(linesCleared > 0) {
            score += linesCleared * 100;
            document.getElementById('bp-score').innerText = score;
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
        const cell = document.getElementById('bp-board').children[y * BOARD_SIZE + x];
        cell.style.backgroundColor = '';
        cell.style.boxShadow = '';
        cell.className = 'w-full h-full bg-gray-800 rounded-sm transform scale-0 transaction-all';
        setTimeout(() => cell.className = 'w-full h-full bg-gray-800 rounded-sm', 300);
    }
})();
"""

switcher_js = """
// Game Switcher Logic
document.addEventListener('DOMContentLoaded', () => {
    
    // Helper to hide all
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
            if(window.togglePracticesPanel) window.togglePracticesPanel(el.closest('.Practices-menu').querySelector('button'));
        });
    });

    document.querySelectorAll('a[href="#blockpuzzle"]').forEach(el => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            window.switchToBlockPuzzle();
            if(window.togglePracticesPanel) window.togglePracticesPanel(el.closest('.Practices-menu').querySelector('button'));
        });
    });
    
    // Also patch existing Flashcards/Climb listeners to ensure they hide new games
    const oldFlash = window.switchToFlashcards;
    window.switchToFlashcards = function() {
        hideAllGames();
        const el = document.getElementById('flashcard-game');
        if(el) el.style.display = 'flex';
    };

    // Hook into Boost link if it exists and uses a global function?
    // Usually it just toggles display manually in its own listener, so hideAllGames helped.
});
"""

directory = "ArisEdu Project Folder/ChemistryLessons/Unit1"
files = [f for f in os.listdir(directory) if f.startswith("Lesson 1.") and f.endswith(".html")]

for filename in files:
    filepath = os.path.join(directory, filename)
    print(f"Processing {filename}...")
    
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    modified = False

    # 1. Inject HTML structures if not present
    card = soup.find("div", class_="diagram-card")
    if card:
        # Check MixMatch
        if not soup.find(id="mixmatch-container"):
            mm_soup = BeautifulSoup(mixmatch_html, "html.parser")
            card.append(mm_soup)
            modified = True
            print("  - Injected Mix & Match HTML")
        
        # Check BlockPuzzle
        if not soup.find(id="blockpuzzle-container"):
            bp_soup = BeautifulSoup(blockpuzzle_html, "html.parser")
            card.append(bp_soup)
            modified = True
            print("  - Injected Block Puzzle HTML")
    
    # 2. Update Menu Links
    panel = soup.find("div", class_="Practices-panel")
    if panel:
        # Find old links and replace
        for a in panel.find_all("a"):
            if "GameMatch.html" in a.get('href', ''):
                a['href'] = "#mixmatch"
                a.string = "Mix & Match"
                del a['target']
                modified = True
                print("  - Updated Mix & Match link")
            if "GameBlocks.html" in a.get('href', ''):
                a['href'] = "#blockpuzzle"
                a.string = "Block Puzzle"
                del a['target']
                modified = True
                print("  - Updated Block Puzzle link")
    
    # 3. Inject Scripts
    # We can append them to the body or the last script tag
    if modified:
        body = soup.find("body")
        if body:
            # Check if we already injected (rough check)
            text = str(soup)
            if "window.initMixMatch" not in text:
                 s_mm = soup.new_tag("script")
                 s_mm.string = mixmatch_js
                 body.append(s_mm)
                 print("  - Injected Mix & Match JS")
                 
            if "window.initBlockPuzzle" not in text:
                 s_bp = soup.new_tag("script")
                 s_bp.string = blockpuzzle_js
                 body.append(s_bp)
                 print("  - Injected Block Puzzle JS")
                 
            if "window.switchToMixMatch" not in text:
                 s_sw = soup.new_tag("script")
                 s_sw.string = switcher_js
                 body.append(s_sw)
                 print("  - Injected Switcher JS")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"  - Saved changes.")
    else:
        print("  - No changes needed.")
