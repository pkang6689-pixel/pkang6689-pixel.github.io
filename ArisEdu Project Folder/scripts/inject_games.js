// inject_games.js — Dynamically injects the practice games HTML into #practice-content-view
// This replaces ~170 lines of repeated HTML in every lesson file.

(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var container = document.getElementById('practice-content-view');
    if (!container) return;
    // Keep existing title if present
    var titleEl = container.querySelector('.page-title');
    var titleHTML = titleEl ? titleEl.outerHTML : '';

    container.innerHTML = titleHTML + '\n' +
    '<div class="diagram-card">\n' +
    '<!-- Flashcard Game -->\n' +
    '<div class="flashcard-game" id="flashcard-game" style="margin-top:2rem;display:flex;flex-direction:column;align-items:center;perspective:1000px;overflow:hidden;">\n' +
    '  <div class="flashcard-box" id="flashcard" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">\n' +
    '    <span id="flashcard-content" style="width:100%;display:block;"></span>\n' +
    '  </div>\n' +
    '  <div style="display:flex;gap:1rem;">\n' +
    '    <button id="prev-flashcard" style="background:#ef4444;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">\n' +
    '      <svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg"><path d="M15 6l-6 6 6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>\n' +
    '    </button>\n' +
    '    <button id="next-flashcard" style="background:#10b981;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">\n' +
    '      <svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg"><path d="M9 6l6 6-6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>\n' +
    '    </button>\n' +
    '    <button id="shuffle-flashcard" title="Shuffle flashcards">\n' +
    '      <svg fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M4 4h7l-1.5 1.5M20 20h-7l1.5-1.5M4 20l16-16" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>\n' +
    '      Shuffle\n' +
    '    </button>\n' +
    '  </div>\n' +
    '</div>\n' +
    '<!-- Climb Game -->\n' +
    '<div id="climb-game-container" style="display:none; width:100%;">\n' +
    '  <div id="climb-game-ui" style="height:100%;display:flex;flex-direction:column;position:relative;overflow:hidden;background-color:#e2e8f0;border-radius:1rem;height:64rem;font-family:\'Orbitron\',sans-serif;">\n' +
    '    <div id="climb-space-bg" style="position:absolute;top:0;left:0;width:100%;height:100%;background:radial-gradient(ellipse at bottom,#1e293b 0%,#020617 100%);z-index:0;overflow:hidden;">\n' +
    '      <div id="climb-stars" style="position:absolute;top:0;left:0;width:100%;height:100%;"></div>\n' +
    '      <div class="climb-planet" style="position:absolute;top:15%;left:10%;width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,#4ade80,#166534);box-shadow:inset -20px -20px 40px rgba(0,0,0,0.5),0 0 20px rgba(74,222,128,0.3);opacity:0.9;animation:floatPlanet 20s infinite ease-in-out;"></div>\n' +
    '      <div class="climb-planet" style="position:absolute;bottom:20%;right:15%;width:180px;height:180px;border-radius:50%;background:linear-gradient(135deg,#fca5a5,#991b1b);box-shadow:inset -30px -30px 60px rgba(0,0,0,0.5),0 0 30px rgba(248,113,113,0.3);opacity:0.8;animation:floatPlanet 25s infinite ease-in-out reverse;"></div>\n' +
    '      <div class="climb-planet" style="position:absolute;top:40%;right:30%;width:40px;height:40px;border-radius:50%;background:#fbbf24;box-shadow:0 0 15px #fbbf24;opacity:0.9;animation:floatPlanet 15s infinite ease-in-out;"></div>\n' +
    '    </div>\n' +
    '    <button id="climb-fullscreen-btn" onclick="toggleClimbFullscreen()" onmouseout="this.style.transform=\'scale(1)\'" onmouseover="this.style.transform=\'scale(1.1)\'" style="position:absolute;bottom:1rem;right:1rem;z-index:50;background:rgba(255,255,255,0.9);border:none;border-radius:50%;width:3rem;height:3rem;cursor:pointer;box-shadow:0 4px 6px rgba(0,0,0,0.1);display:flex;align-items:center;justify-content:center;transition:transform 0.2s;" title="Toggle Fullscreen">\n' +
    '      <svg fill="none" height="24" stroke="#334155" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2-2h3"></path></svg>\n' +
    '    </button>\n' +
    '    <div id="climb-ladder-bg" style="position:absolute;top:0;left:0;width:100%;height:200%;background:repeating-linear-gradient(180deg,#94a3b8 0,#94a3b8 2px,transparent 2px,transparent 40px);opacity:0.3;animation:slideLadder 10s linear infinite;"></div>\n' +
    '    <div id="climb-header" style="z-index:10;padding:1rem;background:rgba(255,255,255,0.95);display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 4px rgba(0,0,0,0.1);">\n' +
    '      <span id="climb-score" style="font-weight:bold;">Score: 0</span>\n' +
    '      <button onclick="resetToClimbMenu()" style="background:#ef4444;color:white;border:none;padding:0.5rem 1rem;border-radius:0.5rem;cursor:pointer;font-weight:600;margin-right:0.5rem;">Restart</button>\n' +
    '      <button id="climb-pause-btn" onclick="toggleClimbPause()" style="background:#f59e0b;color:white;border:none;padding:0.5rem 1rem;border-radius:0.5rem;cursor:pointer;font-weight:600;">Pause</button>\n' +
    '    </div>\n' +
    '    <div style="flex:1;position:relative;width:100%;overflow:hidden;">\n' +
    '      <div id="climb-fuel-text" style="position:absolute;left:2rem;bottom:calc(2rem + 605px);width:60px;text-align:center;font-weight:bold;font-size:1rem;color:#334155;white-space:nowrap;z-index:20;">Fuel Bar</div>\n' +
    '      <div id="climb-fuel-container" style="position:absolute;bottom:2rem;left:2rem;width:60px;height:600px;background:rgba(255,255,255,0.3);border:2px solid #334155;border-radius:10px;overflow:hidden;z-index:10;box-shadow:0 4px 6px rgba(0,0,0,0.1);">\n' +
    '        <div id="climb-fuel-fill" style="position:absolute;bottom:0;left:0;width:100%;height:50%;background:linear-gradient(to top,#f59e0b,#ef4444);transition:height 0.5s ease;"></div>\n' +
    '      </div>\n' +
    '      <div id="climb-player" style="position:absolute;bottom:35%;left:50%;transform:translateX(-50%);width:240px;height:240px;transition:bottom 0.5s cubic-bezier(0.175,0.885,0.32,1.275);z-index:5;">\n' +
    '        <svg style="width:100%;height:100%;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">\n' +
    '          <path d="M18 42 L 8 58 L 22 58 L 24 48 Z" fill="#ef4444" stroke="#991b1b" stroke-linejoin="round" stroke-width="1.5"></path>\n' +
    '          <path d="M46 42 L 56 58 L 42 58 L 40 48 Z" fill="#ef4444" stroke="#991b1b" stroke-linejoin="round" stroke-width="1.5"></path>\n' +
    '          <ellipse cx="32" cy="32" fill="#e2e8f0" rx="14" ry="28" stroke="#475569" stroke-width="2"></ellipse>\n' +
    '          <circle cx="32" cy="24" fill="#3b82f6" r="7" stroke="#1d4ed8" stroke-width="1.5"></circle>\n' +
    '          <circle cx="33" cy="22" fill="white" opacity="0.6" r="2.5"></circle>\n' +
    '          <path d="M26 56 Q 32 72 38 56" fill="#f59e0b" id="climb-flame-outer" stroke="#d97706" stroke-width="1" style="transform-origin:32px 56px;transition:transform 0.1s ease-out;"></path>\n' +
    '          <path d="M29 56 Q 32 66 35 56" fill="#fef3c7" id="climb-flame-inner" style="transform-origin:32px 56px;transition:transform 0.1s ease-out;"></path>\n' +
    '        </svg>\n' +
    '      </div>\n' +
    '    </div>\n' +
    '    <div id="climb-start-screen" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:60;background:rgba(255,255,255,0.95);padding:2rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);width:80%;max-width:400px;text-align:center;border:1px solid #cbd5e1;display:flex;flex-direction:column;align-items:center;">\n' +
    '      <h3 style="color:#1e293b;margin-top:0;">Ready to Fly?</h3>\n' +
    '      <p style="color:#64748b;margin-bottom:1.5rem;">Answer correctly to fly up against the moving ladder!</p>\n' +
    '      <div style="font-size:0.9rem;color:#64748b;margin-bottom:1rem;">Spacebar = Boost (Uses Fuel)<br/>Correct Answer = +Fuel</div>\n' +
    '      <button onclick="startClimbGame()" style="background:#0f172a;color:white;padding:0.75rem 2rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;font-size:1.1rem;transition:background 0.2s;">Start Flying</button>\n' +
    '    </div>\n' +
    '    <div id="climb-game-over" style="display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:60;background:rgba(255,255,255,0.95);padding:2rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);width:80%;max-width:400px;text-align:center;border:1px solid #cbd5e1;flex-direction:column;align-items:center;">\n' +
    '      <h3 id="climb-result-title" style="font-size:1.5rem;margin-bottom:0.5rem;color:#1e293b;">Game Over!</h3>\n' +
    '      <p id="climb-final-score" style="color:#64748b;margin-bottom:1.5rem;"></p>\n' +
    '      <div style="display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap;">\n' +
    '        <button onclick="startClimbGame()" style="background:#10b981;color:white;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;">Play Again</button>\n' +
    '        <button onclick="alert(\'Leaderboard coming soon!\')" style="background:#f59e0b;color:white;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;display:flex;align-items:center;gap:0.5rem;">🏆 Leaderboard</button>\n' +
    '      </div>\n' +
    '    </div>\n' +
    '    <div id="climb-paused-screen" style="display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:60;background:rgba(255,255,255,0.95);padding:2rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);width:80%;max-width:400px;text-align:center;border:1px solid #cbd5e1;flex-direction:column;align-items:center;">\n' +
    '      <h3 style="color:#1e293b;margin-top:0;">Game Paused</h3>\n' +
    '      <button onclick="toggleClimbPause()" style="background:#f59e0b;color:white;padding:0.75rem 2rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;font-size:1.1rem;transition:background 0.2s;">Resume</button>\n' +
    '    </div>\n' +
    '    <div id="climb-interaction" style="position:absolute;z-index:20;background:rgba(255,255,255,0.95);padding:1.5rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);border:1px solid #cbd5e1;min-height:200px;display:none;flex-direction:column;justify-content:center;top:50%;right:2rem;transform:translateY(-50%);width:300px">\n' +
    '      <div id="climb-question-area" style="display:block;text-align:center;width:100%;max-width:600px;margin:0 auto;">\n' +
    '        <p id="climb-question-text" style="font-weight:bold;margin-bottom:1.5rem;font-size:1.1rem;color:#1e293b;line-height:1.5;"></p>\n' +
    '        <div id="climb-options" style="display:grid;gap:0.75rem;grid-template-columns:1fr;"></div>\n' +
    '        <div id="climb-feedback" style="margin-top:1rem;height:1.5rem;font-weight:bold;"></div>\n' +
    '      </div>\n' +
    '    </div>\n' +
    '  </div>\n' +
    '</div>\n' +
    '<!-- Mix & Match -->\n' +
    '<div id="mixmatch-container" style="display:none;flex-direction:column;align-items:center;width:100%;">\n' +
    '  <div class="w-full max-w-4xl flex justify-between items-center mb-8">\n' +
    '    <div>\n' +
    '      <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">Mix &amp; Match</h1>\n' +
    '      <p class="text-slate-400">Match the terms to their definitions!</p>\n' +
    '    </div>\n' +
    '    <div class="text-right">\n' +
    '      <div class="text-sm text-slate-400">Streak</div>\n' +
    '      <div class="text-2xl font-bold text-yellow-400" id="mixmatch-streak-display">0</div>\n' +
    '    </div>\n' +
    '  </div>\n' +
    '  <div class="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-4xl" id="mixmatch-game-board"></div>\n' +
    '  <div class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50" id="mixmatch-win-screen">\n' +
    '    <div class="bg-slate-800 p-8 rounded-2xl text-center border border-slate-700 max-w-md mx-4">\n' +
    '      <div class="text-6xl mb-4">🎉</div>\n' +
    '      <h2 class="text-3xl font-bold mb-2">Level Complete!</h2>\n' +
    '      <p class="text-slate-400 mb-6">You matched all terms correctly.</p>\n' +
    '      <button class="bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-8 rounded-full transition-all hover:scale-105 active:scale-95" onclick="window.startMixMatchGame()">Play Again</button>\n' +
    '    </div>\n' +
    '  </div>\n' +
    '</div>\n' +
    '<!-- Block Puzzle -->\n' +
    '<div id="blockpuzzle-container" style="display:none;flex-direction:column;align-items:center;justify-content:center;width:100%;">\n' +
    '  <div class="relative w-full max-w-md bg-gray-800 rounded-2xl shadow-2xl p-6 border border-gray-700">\n' +
    '    <div class="flex justify-between items-end mb-6">\n' +
    '      <div>\n' +
    '        <h1 class="text-2xl font-bold bg-gradient-to-r from-green-400 to-emerald-600 bg-clip-text text-transparent">BLOCK PUZZLE</h1>\n' +
    '        <p class="text-xs text-gray-400">Clear lines to score!</p>\n' +
    '      </div>\n' +
    '      <div class="text-right">\n' +
    '        <div class="text-xs text-gray-400 font-sans">SCORE</div>\n' +
    '        <div class="text-3xl font-bold text-white" id="bp-score">0</div>\n' +
    '      </div>\n' +
    '    </div>\n' +
    '    <div class="grid grid-cols-8 gap-1 bg-gray-900 p-2 rounded-lg border-2 border-gray-700 mx-auto" id="bp-board" style="width:340px;height:340px;"></div>\n' +
    '    <div class="mt-8 flex justify-center gap-4 h-24 items-center min-h-[6rem]" id="bp-hand"></div>\n' +
    '    <div class="hidden absolute inset-0 bg-black/90 rounded-2xl z-20 flex flex-col items-center justify-center text-center p-6 backdrop-blur-sm" id="bp-game-over">\n' +
    '      <h2 class="text-3xl text-red-500 font-bold mb-2">GAME OVER</h2>\n' +
    '      <p class="text-gray-300 mb-6">No more moves possible!</p>\n' +
    '      <div class="text-4xl font-bold text-white mb-8" id="bp-final-score">0</div>\n' +
    '      <button class="bg-green-600 hover:bg-green-500 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition active:scale-95" onclick="window.resetBlockGame()">TRY AGAIN</button>\n' +
    '    </div>\n' +
    '  </div>\n' +
    '</div>\n' +
    '</div>\n' +
    '<div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">\n' +
    '  <div class="Practices-menu" style="position:relative;margin-right:1rem;">\n' +
    '    <button class="side-button view-other-Practices" onclick="togglePracticesPanel(this)" type="button">Other games</button>\n' +
    '    <div aria-hidden="true" class="Practices-panel">\n' +
    '      <div class="Practices-panel-item"><a href="#flashcard-game">Flashcard Game</a></div>\n' +
    '      <div class="Practices-panel-item"><a href="#climb">Boost</a></div>\n' +
    '      <div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div>\n' +
    '      <div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>\n' +
    '    </div>\n' +
    '  </div>\n' +
    '  <button class="side-button" onclick="toggleToQuiz(event)">Next Up: Quiz</button>\n' +
    '</div>';

    // Inject climb game CSS
    if (!document.getElementById('climb-game-styles')) {
      var style = document.createElement('style');
      style.id = 'climb-game-styles';
      style.textContent =
        '@keyframes twinkle { 0% { opacity:0.3; transform:scale(0.8); } 100% { opacity:1; transform:scale(1.2); } }\n' +
        '@keyframes floatPlanet { 0% { transform:translateY(0px); } 50% { transform:translateY(-20px); } 100% { transform:translateY(0px); } }\n' +
        '@keyframes slideLadder { from { background-position: 0 0; } to { background-position: 0 40px; } }\n' +
        '.climb-option-btn { background:#f1f5f9; border:2px solid #e2e8f0; padding:0.75rem; border-radius:0.5rem; cursor:pointer; font-size:1rem; color:#334155; transition:all 0.2s; text-align:left; }\n' +
        '.climb-option-btn:hover { background:#e2e8f0; border-color:#cbd5e1; }\n' +
        'body:not(.dark-mode) #climb-space-bg { background:radial-gradient(ellipse at bottom,#bae6fd 0%,#0369a1 100%) !important; }\n' +
        'body:not(.dark-mode) #climb-stars div { opacity:0.3 !important; }\n' +
        'body.dark-mode #climb-game-ui { background-color:#0f172a !important; }\n' +
        'body.dark-mode #climb-ladder-bg { background-image:repeating-linear-gradient(180deg,#334155 0,#334155 2px,transparent 2px,transparent 40px) !important; opacity:0.2 !important; }\n' +
        'body.dark-mode #climb-header { background:rgba(15,23,42,0.95) !important; box-shadow:0 2px 4px rgba(0,0,0,0.3) !important; }\n' +
        'body.dark-mode #climb-score { color:#e2e8f0 !important; }\n' +
        'body.dark-mode #climb-interaction { background:#1e293b !important; border-color:#334155 !important; }\n' +
        'body.dark-mode #climb-start-screen h3, body.dark-mode #climb-game-over h3, body.dark-mode #climb-paused-screen h3 { color:#f8fafc !important; }\n' +
        'body.dark-mode #climb-start-screen p, body.dark-mode #climb-game-over p, body.dark-mode #climb-question-text { color:#cbd5e1 !important; }\n' +
        'body.dark-mode .climb-option-btn { background:#334155 !important; border-color:#475569 !important; color:#e2e8f0 !important; }\n' +
        'body.dark-mode .climb-option-btn:hover { background:#475569 !important; border-color:#64748b !important; }\n' +
        'body.dark-mode #climb-fullscreen-btn { background:rgba(30,41,59,0.9) !important; }\n' +
        'body.dark-mode #climb-fullscreen-btn svg { stroke:#e2e8f0 !important; }\n' +
        'body.dark-mode #climb-start-screen, body.dark-mode #climb-game-over, body.dark-mode #climb-paused-screen { background:rgba(30,41,59,0.95) !important; border-color:#475569 !important; }\n' +
        'body.dark-mode #climb-start-screen div { color:#cbd5e1 !important; }\n' +
        'body.dark-mode #climb-fuel-text { color:#e2e8f0 !important; }';
      document.head.appendChild(style);
    }
  });
})();
