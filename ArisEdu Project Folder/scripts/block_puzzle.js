// Dedicated Block Puzzle Script - Guarantees isolation from practice_games.js crashes
console.log("Loading Independent Block Puzzle Script...");

// Override whatever practice_games.js did
window.initBlockPuzzle = function() {
    console.log("Stub Function triggered...");
    if(window.realInitBlockPuzzle) {
        window.realInitBlockPuzzle();
    } else {
         // If real logic missing, define it here
         defineBlockPuzzleLogic();
         window.realInitBlockPuzzle();
    }
};

// Force define logic here to ensure it exists
function defineBlockPuzzleLogic() {
    console.log("Defining Block Puzzle Logic (Independent)...");
    window.bpError = null;
    window.bpInitialized = false;

    window.realInitBlockPuzzle = function() {
            if(window.bpInitialized) {
                 window.resetBlockGame();
                 return;
            }
            window.bpInitialized = true;
            console.log("Block Puzzle Initialized (Independent)");
            
            document.addEventListener('mousemove', handleDragMove);
            document.addEventListener('touchmove', handleDragMove, {passive: false});
            document.addEventListener('mouseup', handleDragEnd);
            document.addEventListener('touchend', handleDragEnd);
            
            if(!document.getElementById('bp-question-modal')) createQuestionModal();
            window.resetBlockGame();
        };

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
            let boardEl = document.getElementById('bp-board');
            if(!boardEl) {
                // If container wiped, recreate critical structure
                const container = document.getElementById('blockpuzzle-container');
                if(container) {
                     console.log("Rebuilding Game HTML Structure...");
                     container.innerHTML = `
<div class="relative w-full max-w-md bg-gray-800 rounded-2xl shadow-2xl p-6 border border-gray-700">
<div class="flex justify-between items-end mb-6">
<div>
<h1 class="text-2xl font-bold bg-gradient-to-r from-green-400 to-emerald-600 bg-clip-text text-transparent">BLOCK PUZZLE</h1>
<p class="text-xs text-gray-400">Clear lines to score!</p>
</div>
<div class="text-right">
<div class="text-xs text-gray-400 font-sans">SCORE</div>
<div class="text-3xl font-bold text-white" id="bp-score">0</div>
</div>
</div>
<div class="grid grid-cols-8 gap-1 bg-gray-900 p-2 rounded-lg border-2 border-gray-700 mx-auto" id="bp-board" style="width: 340px; height: 340px;">
</div>
<div class="mt-8 flex justify-center gap-4 h-24 items-center min-h-[6rem]" id="bp-hand">
</div>
<div class="hidden absolute inset-0 bg-black/90 rounded-2xl z-20 flex flex-col items-center justify-center text-center p-6 backdrop-blur-sm" id="bp-game-over">
<h2 class="text-3xl text-red-500 font-bold mb-2">GAME OVER</h2>
<p class="text-gray-300 mb-6">No more moves possible!</p>
<div class="text-4xl font-bold text-white mb-8" id="bp-final-score">0</div>
<button class="bg-green-600 hover:bg-green-500 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition active:scale-95" onclick="window.resetBlockGame()">
                TRY AGAIN
            </button>
</div>
</div>
                     `;
                     boardEl = document.getElementById('bp-board');
                } else {
                    return;
                }
            }
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
            const pt = 25; 
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
                // visual feedback
            }
        }
        function clearPreview() {} 

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
        
        function checkGameOver() { }
        function triggerQuestion() { spawnBlocks(); }
    }
    
    // Auto-execute definition logic immediately
    defineBlockPuzzleLogic();

console.log("Block Puzzle Script Definition Complete");
