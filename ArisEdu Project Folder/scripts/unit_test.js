// unit_test.js — Shared logic for Unit Test pages
// Injects practice games HTML, climb game logic, quiz/practice view switching, quiz completion tracking

(function () {
  function _t(key, fallback) {
    var langMode = null;
    try { langMode = localStorage.getItem('arisEduLanguage'); } catch(e) {}
    
    // Default to English if no language preference
    var isChineseMode = (langMode === 'chinese' || langMode === 'traditional' || langMode === 'zh');
    
    if (!isChineseMode) {
        // English mode: return English (key itself as fallback)
        return fallback || key;
    }
    
    // Chinese mode: return Chinese translation
    var t = window.arisEduTranslations || window.globalTranslations;
    return (t && t[key]) || fallback || key;
  }

  // ========== 1. Inject Practice Games HTML ==========
  function injectPracticeGamesHTML() {
    const practiceView = document.getElementById('practice-content-view');
    if (!practiceView) return;

    // Find the title element already in the page
    const titleEl = practiceView.querySelector('.page-title');
    const titleHTML = titleEl ? titleEl.outerHTML : '';

    practiceView.innerHTML = `
      ${titleHTML}
      <div class="diagram-card">
        <!-- Flashcard Game -->
        <div class="flashcard-game" id="flashcard-game" style="margin-top:2rem;display:flex;flex-direction:column;align-items:center;perspective:1000px;overflow:hidden;">
          <div class="flashcard-box" id="flashcard" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">
            <span id="flashcard-content" style="width:100%;display:block;"></span>
          </div>
          <div style="display:flex;gap:1rem;">
            <button id="prev-flashcard" style="background:#ef4444;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
              <svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg"><path d="M15 6l-6 6 6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
            </button>
            <button id="next-flashcard" style="background:#10b981;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
              <svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg"><path d="M9 6l6 6-6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path></svg>
            </button>
            <button id="shuffle-flashcard" title="Shuffle flashcards">
              <svg fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M4 4h7l-1.5 1.5M20 20h-7l1.5-1.5M4 20l16-16" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path></svg>
              Shuffle
            </button>
            <span id="flashcard-counter" style="display:flex;align-items:center;font-weight:600;font-size:1rem;color:#64748b;white-space:nowrap;"></span>
          </div>
        </div>

        <!-- Climb Game -->
        <div id="climb-game-container" style="display:none; width:100%;">
          <div id="climb-game-ui" style="height:100%;display:flex;flex-direction:column;position:relative;overflow:hidden;background-color:#e2e8f0;border-radius:1rem;height:64rem;font-family:'Orbitron',sans-serif;">
            <div id="climb-space-bg" style="position:absolute;top:0;left:0;width:100%;height:100%;background:radial-gradient(ellipse at bottom,#1e293b 0%,#020617 100%);z-index:0;overflow:hidden;">
              <div id="climb-stars" style="position:absolute;top:0;left:0;width:100%;height:100%;"></div>
              <div class="climb-planet" style="position:absolute;top:15%;left:10%;width:100px;height:100px;border-radius:50%;background:linear-gradient(135deg,#4ade80,#166534);box-shadow:inset -20px -20px 40px rgba(0,0,0,0.5),0 0 20px rgba(74,222,128,0.3);opacity:0.9;animation:floatPlanet 20s infinite ease-in-out;"></div>
              <div class="climb-planet" style="position:absolute;bottom:20%;right:15%;width:180px;height:180px;border-radius:50%;background:linear-gradient(135deg,#fca5a5,#991b1b);box-shadow:inset -30px -30px 60px rgba(0,0,0,0.5),0 0 30px rgba(248,113,113,0.3);opacity:0.8;animation:floatPlanet 25s infinite ease-in-out reverse;"></div>
              <div class="climb-planet" style="position:absolute;top:40%;right:30%;width:40px;height:40px;border-radius:50%;background:#fbbf24;box-shadow:0 0 15px #fbbf24;opacity:0.9;animation:floatPlanet 15s infinite ease-in-out;"></div>
            </div>
            <button id="climb-fullscreen-btn" onclick="toggleClimbFullscreen()" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.1)'" style="position:absolute;bottom:1rem;right:1rem;z-index:50;background:rgba(255,255,255,0.9);border:none;border-radius:50%;width:3rem;height:3rem;cursor:pointer;box-shadow:0 4px 6px rgba(0,0,0,0.1);display:flex;align-items:center;justify-content:center;transition:transform 0.2s;" title="Toggle Fullscreen">
              <svg fill="none" height="24" stroke="#334155" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2-2h3"></path></svg>
            </button>
            <div id="climb-ladder-bg" style="position:absolute;top:0;left:0;width:100%;height:200%;background:repeating-linear-gradient(180deg,#94a3b8 0,#94a3b8 2px,transparent 2px,transparent 40px);opacity:0.3;animation:slideLadder 10s linear infinite;"></div>
            <div id="climb-header" style="z-index:10;padding:1rem;background:rgba(255,255,255,0.95);display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 4px rgba(0,0,0,0.1);">
              <span id="climb-score" style="font-weight:bold;">Score: 0</span>
              <button onclick="resetToClimbMenu()" style="background:#ef4444;color:white;border:none;padding:0.5rem 1rem;border-radius:0.5rem;cursor:pointer;font-weight:600;margin-right:0.5rem;">Restart</button>
              <button id="climb-pause-btn" onclick="toggleClimbPause()" style="background:#f59e0b;color:white;border:none;padding:0.5rem 1rem;border-radius:0.5rem;cursor:pointer;font-weight:600;">Pause</button>
            </div>
            <div style="flex:1;position:relative;width:100%;overflow:hidden;">
              <div id="climb-fuel-text" style="position:absolute;left:2rem;bottom:calc(2rem + 605px);width:60px;text-align:center;font-weight:bold;font-size:1rem;color:#334155;white-space:nowrap;z-index:20;">Fuel Bar</div>
              <div id="climb-fuel-container" style="position:absolute;bottom:2rem;left:2rem;width:60px;height:600px;background:rgba(255,255,255,0.3);border:2px solid #334155;border-radius:10px;overflow:hidden;z-index:10;box-shadow:0 4px 6px rgba(0,0,0,0.1);">
                <div id="climb-fuel-fill" style="position:absolute;bottom:0;left:0;width:100%;height:50%;background:linear-gradient(to top,#f59e0b,#ef4444);transition:height 0.5s ease;"></div>
              </div>
              <div id="climb-player" style="position:absolute;bottom:35%;left:50%;transform:translateX(-50%);width:240px;height:240px;transition:bottom 0.5s cubic-bezier(0.175,0.885,0.32,1.275);z-index:5;">
                <svg style="width:100%;height:100%;filter:drop-shadow(0 4px 6px rgba(0,0,0,0.3));" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
                  <path d="M18 42 L 8 58 L 22 58 L 24 48 Z" fill="#ef4444" stroke="#991b1b" stroke-linejoin="round" stroke-width="1.5"></path>
                  <path d="M46 42 L 56 58 L 42 58 L 40 48 Z" fill="#ef4444" stroke="#991b1b" stroke-linejoin="round" stroke-width="1.5"></path>
                  <ellipse cx="32" cy="32" fill="#e2e8f0" rx="14" ry="28" stroke="#475569" stroke-width="2"></ellipse>
                  <circle cx="32" cy="24" fill="#3b82f6" r="7" stroke="#1d4ed8" stroke-width="1.5"></circle>
                  <circle cx="33" cy="22" fill="white" opacity="0.6" r="2.5"></circle>
                  <path d="M26 56 Q 32 72 38 56" fill="#f59e0b" id="climb-flame-outer" stroke="#d97706" stroke-width="1" style="transform-origin:32px 56px;transition:transform 0.1s ease-out;"></path>
                  <path d="M29 56 Q 32 66 35 56" fill="#fef3c7" id="climb-flame-inner" style="transform-origin:32px 56px;transition:transform 0.1s ease-out;"></path>
                </svg>
              </div>
            </div>
            <div id="climb-start-screen" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:60;background:rgba(255,255,255,0.95);padding:2rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);width:80%;max-width:400px;text-align:center;border:1px solid #cbd5e1;display:flex;flex-direction:column;align-items:center;">
              <h3 style="color:#1e293b;margin-top:0;">Ready to Fly?</h3>
              <p style="color:#64748b;margin-bottom:1.5rem;">Answer correctly to fly up against the moving ladder!</p>
              <div style="font-size:0.9rem;color:#64748b;margin-bottom:1rem;">Spacebar = Boost (Uses Fuel)<br/>Correct Answer = +Fuel</div>
              <button onclick="startClimbGame()" style="background:#0f172a;color:white;padding:0.75rem 2rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;font-size:1.1rem;transition:background 0.2s;">Start Flying</button>
            </div>
            <div id="climb-game-over" style="display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:60;background:rgba(255,255,255,0.95);padding:2rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);width:80%;max-width:400px;text-align:center;border:1px solid #cbd5e1;flex-direction:column;align-items:center;">
              <h3 id="climb-result-title" style="font-size:1.5rem;margin-bottom:0.5rem;color:#1e293b;">Game Over!</h3>
              <p id="climb-final-score" style="color:#64748b;margin-bottom:1.5rem;"></p>
              <div style="display:flex;gap:0.5rem;justify-content:center;flex-wrap:wrap;">
                <button onclick="startClimbGame()" style="background:#10b981;color:white;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;">Play Again</button>
                <button onclick="alert('Leaderboard coming soon!')" style="background:#f59e0b;color:white;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;display:flex;align-items:center;gap:0.5rem;">🏆 Leaderboard</button>
              </div>
            </div>
            <div id="climb-paused-screen" style="display:none;position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);z-index:60;background:rgba(255,255,255,0.95);padding:2rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);width:80%;max-width:400px;text-align:center;border:1px solid #cbd5e1;flex-direction:column;align-items:center;">
              <h3 style="color:#1e293b;margin-top:0;">Game Paused</h3>
              <button onclick="toggleClimbPause()" style="background:#f59e0b;color:white;padding:0.75rem 2rem;border:none;border-radius:0.5rem;cursor:pointer;font-weight:600;font-size:1.1rem;transition:background 0.2s;">Resume</button>
            </div>
            <div id="climb-interaction" style="position:absolute;z-index:20;background:rgba(255,255,255,0.95);padding:1.5rem;border-radius:1rem;box-shadow:0 10px 25px rgba(0,0,0,0.2);border:1px solid #cbd5e1;min-height:200px;display:none;flex-direction:column;justify-content:center;top:50%;right:2rem;transform:translateY(-50%);width:300px;">
              <div id="climb-question-area" style="display:block;text-align:center;width:100%;max-width:600px;margin:0 auto;">
                <p id="climb-question-text" style="font-weight:bold;margin-bottom:1.5rem;font-size:1.1rem;color:#1e293b;line-height:1.5;"></p>
                <div id="climb-options" style="display:grid;gap:0.75rem;grid-template-columns:1fr;"></div>
                <div id="climb-feedback" style="margin-top:1rem;height:1.5rem;font-weight:bold;"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mix & Match -->
        <div id="mixmatch-container" style="display:none;flex-direction:column;align-items:center;width:100%;">
          <div class="w-full max-w-4xl flex justify-between items-center mb-8">
            <div>
              <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-400 to-cyan-300 bg-clip-text text-transparent">Mix &amp; Match</h1>
              <p class="text-slate-400">Match the terms to their definitions!</p>
            </div>
            <div class="text-right">
              <div class="text-sm text-slate-400">Streak</div>
              <div class="text-2xl font-bold text-yellow-400" id="mixmatch-streak-display">0</div>
            </div>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 w-full max-w-4xl" id="mixmatch-game-board"></div>
          <div class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50" id="mixmatch-win-screen">
            <div class="bg-slate-800 p-8 rounded-2xl text-center border border-slate-700 max-w-md mx-4">
              <div class="text-6xl mb-4">🎉</div>
              <h2 class="text-3xl font-bold mb-2">Level Complete!</h2>
              <p class="text-slate-400 mb-6">You matched all terms correctly.</p>
              <button class="bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-8 rounded-full transition-all hover:scale-105 active:scale-95" onclick="window.startMixMatchGame()">Play Again</button>
            </div>
          </div>
        </div>

        <!-- Block Puzzle -->
        <div id="blockpuzzle-container" style="display:none;flex-direction:column;align-items:center;justify-content:center;width:100%;">
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
            <div class="grid grid-cols-8 gap-1 bg-gray-900 p-2 rounded-lg border-2 border-gray-700 mx-auto" id="bp-board" style="width:340px;height:340px;"></div>
            <div class="mt-8 flex justify-center gap-4 h-24 items-center min-h-[6rem]" id="bp-hand"></div>
            <div class="hidden absolute inset-0 bg-black/90 rounded-2xl z-20 flex flex-col items-center justify-center text-center p-6 backdrop-blur-sm" id="bp-game-over">
              <h2 class="text-3xl text-red-500 font-bold mb-2">GAME OVER</h2>
              <p class="text-gray-300 mb-6">No more moves possible!</p>
              <div class="text-4xl font-bold text-white mb-8" id="bp-final-score">0</div>
              <button class="bg-green-600 hover:bg-green-500 text-white font-bold py-3 px-8 rounded-lg shadow-lg transform transition active:scale-95" onclick="window.resetBlockGame()">TRY AGAIN</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Practice Actions Menu -->
      <div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">
        <div class="Practices-menu" style="position:relative;margin-right:1rem;">
          <button class="side-button view-other-Practices" onclick="togglePracticesPanel(this)" type="button">Other games</button>
          <div aria-hidden="true" class="Practices-panel">
            <div class="Practices-panel-item"><a href="#flashcard-game">Flashcard Game</a></div>
            <div class="Practices-panel-item"><a href="#climb">Boost</a></div>
            <div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div>
            <div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>
          </div>
        </div>
        <button class="side-button" id="take-test-btn" style="text-align:center;text-decoration:none;display:block;">Take the test</button>
      </div>
    `;
  }

  // ========== 2. Inject Quiz Finish Screen ==========
  function injectQuizFinishScreen() {
    const quizView = document.getElementById('quiz-content-view');
    if (!quizView) return;

    // Check if finish screen already exists
    if (document.getElementById('quiz-finish-screen')) return;

    const quizForm = document.getElementById('quiz-form');
    if (!quizForm) return;

    // Detect course from URL for 'Back to Course' button
    var coursePath = decodeURIComponent(window.location.pathname).toLowerCase();
    var courseMap = {
      'algebra1lessons': { url: '../../algebra1.html', label: 'Back to Algebra 1' },
      'algebra2lessons': { url: '../../algebra2.html', label: 'Back to Algebra 2' },
      'geometrylessons': { url: '../../geometry.html', label: 'Back to Geometry' },
      'physicslessons':  { url: '../../physics.html',  label: 'Back to Physics' },
      'chemistrylessons': { url: '../../chem.html',    label: 'Back to Chemistry' },
      'biologylessons':  { url: '../../bio.html',      label: 'Back to Biology' }
    };
    var backUrl = '../../Courses.html';
    var backLabel = 'Back to Course';
    Object.keys(courseMap).forEach(function(key) {
      if (coursePath.includes(key)) {
        backUrl = courseMap[key].url;
        backLabel = courseMap[key].label;
      }
    });

    // Insert after quiz-form
    const finishHTML = `
      <div id="quiz-results" style="margin-top:2rem;font-weight:bold;display:none;padding:1rem;border-radius:0.5rem;"></div>
      <div id="quiz-finish-screen" style="display:none;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:2rem;border-radius:1rem;box-shadow:0 4px 6px rgba(0,0,0,0.1);margin-top:2rem;">
        <h2 style="font-size:2rem;font-weight:700;margin-bottom:1.5rem;">🎉 Quiz Completed!</h2>
        <div style="font-size:1.25rem;margin-bottom:0.75rem;">Score: <span id="quiz-final-score" style="font-weight:700;">0/5</span></div>
        <div style="font-size:1.25rem;margin-bottom:0.75rem;">Percentage: <span id="quiz-final-percent" style="font-weight:700;">0%</span></div>
        <div style="font-size:1.25rem;margin-bottom:2rem;">Time Spent: <span id="quiz-time-spent" style="font-weight:700;">00:00</span></div>
        <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;width:100%;">
          <button class="side-button" onclick="location.reload()" style="flex:1;min-width:150px;">Retake Quiz</button>
          <button class="side-button" onclick="window.location.href='${backUrl}'" style="flex:1;min-width:150px;">${backLabel}</button>
        </div>
        <div style="margin-top:1.5rem;width:100%;">
          <button class="side-button" onclick="navigateBackToPractice()" style="width:100%;margin-bottom:0.5rem;">Back to Practice</button>
        </div>
      </div>
    `;

    quizForm.insertAdjacentHTML('afterend', finishHTML);
  }

  // ========== 3. Dark Mode Styles for Quiz Finish Screen ==========
  function injectQuizFinishStyles() {
    if (document.getElementById('quiz-finish-styles')) return;
    const style = document.createElement('style');
    style.id = 'quiz-finish-styles';
    style.textContent = `
      #quiz-finish-screen {
        background: #f8fafc;
        color: #0f172a;
        transition: background-color 0.3s, color 0.3s;
        width: 100%;
        max-width: 600px;
        margin: 2rem auto;
        padding: 2rem !important;
      }
      #quiz-finish-screen h2 { color: #0f172a; }
      #quiz-finish-screen div { color: #334155; }
      body.dark-mode #quiz-finish-screen {
        background: #1e293b;
        color: #e2e8f0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
      }
      body.dark-mode #quiz-finish-screen h2 { color: #f8fafc; }
      body.dark-mode #quiz-finish-screen div { color: #cbd5e1; }
    `;
    document.head.appendChild(style);
  }

  // ========== 4. Game Switching Logic ==========
  window.switchToClimb = function () {
    ['flashcard-game', 'climb-game-container', 'mixmatch-container', 'blockpuzzle-container'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.style.display = 'none';
    });
    var climbGame = document.getElementById('climb-game-container');
    if (climbGame) { climbGame.style.display = 'block'; if (window.initClimbGame) window.initClimbGame(); }
  };

  window.switchToFlashcards = function () {
    ['flashcard-game', 'climb-game-container', 'mixmatch-container', 'blockpuzzle-container'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.style.display = 'none';
    });
    var flashcardGame = document.querySelector('.flashcard-game');
    if (flashcardGame) flashcardGame.style.display = 'flex';
    if (typeof window.initFlashcards === 'function') window.initFlashcards();
  };

  // ========== 4b. Navigate back to practice (works on test-only pages) ==========
  window.navigateBackToPractice = function () {
    var practiceView = document.getElementById('practice-content-view');
    if (practiceView) {
      // Combined page — just show practice view
      showPractice();
    } else {
      // Test-only page — navigate to _Test_Practice.html
      var currentUrl = window.location.href;
      var practiceUrl = currentUrl.replace('_Test.html', '_Test_Practice.html');
      window.location.href = practiceUrl;
    }
  };

  // ========== 5. Show Quiz / Show Practice ==========
  var quizStartTime = 0;

  window.showQuiz = function () {
    quizStartTime = Date.now();
    var practiceView = document.getElementById('practice-content-view');
    var quizView = document.getElementById('quiz-content-view');
    if (practiceView) practiceView.style.display = 'none';
    if (quizView) quizView.style.display = 'block';

    var finishScreen = document.getElementById('quiz-finish-screen');
    if (finishScreen) finishScreen.style.display = 'none';
    var quizForm = document.getElementById('quiz-form');
    if (quizForm) quizForm.style.display = 'block';

    window.scrollTo(0, 0);
  };

  window.showPractice = function () {
    var quizView = document.getElementById('quiz-content-view');
    var practiceView = document.getElementById('practice-content-view');
    if (quizView) quizView.style.display = 'none';
    if (practiceView) practiceView.style.display = 'block';
    window.scrollTo(0, 0);
  };

  // ========== 5b. Helper: derive storage key from URL ==========
  function getUnitTestStorageKey() {
    var testPath = decodeURIComponent(window.location.pathname);
    var unitMatch = testPath.match(/Unit(\w+)_Test/);
    if (!unitMatch) return null;
    var unitId = unitMatch[1];
    var coursePrefix, lessonNum;
    if (testPath.includes('Algebra1Lessons')) { coursePrefix = 'alg1'; lessonNum = 10; }
    else if (testPath.includes('Algebra2Lessons')) { coursePrefix = 'alg2'; lessonNum = 10; }
    else if (testPath.includes('GeometryLessons')) { coursePrefix = 'geometry'; lessonNum = 8; }
    else if (testPath.includes('PhysicsLessons')) {
      coursePrefix = 'physics';
      var pMap = {'1':7,'2':7,'3':9,'4':7,'5':7,'6':7,'7':9,'8':7,'9':7,'10':10,'11':7};
      lessonNum = pMap[unitId];
    } else if (testPath.includes('ChemistryLessons')) {
      coursePrefix = 'chem';
      var cMap = {'1':9,'2':6,'3':9,'4':10,'5A':9,'5B':6,'6':8,'7':9,'8':10,'9':9,'10':11,'11':7,'12':6};
      lessonNum = cMap[unitId];
    } else if (testPath.includes('BiologyLessons')) { coursePrefix = 'bio'; lessonNum = 8; }
    if (coursePrefix && lessonNum) return coursePrefix + '_u' + unitId + '_l' + lessonNum + '_completed';
    return null;
  }

  // ========== 6. Quiz Completion Tracking ==========
  window.checkQuizCompletion = function () {
    var form = document.getElementById('quiz-form');
    var questions = Array.from(form.querySelectorAll('.quiz-question'));

    var allAnswered = true;
    var correctCount = 0;
    var totalQuestions = questions.length;

    questions.forEach(function (q) {
      var btn = q.querySelector('button[onclick^="checkQuizAnswer"]');
      if (btn && !btn.disabled) {
        allAnswered = false;
      }
      if (q.dataset.status === 'correct') {
        correctCount++;
      }
    });

    if (allAnswered && totalQuestions > 0) {
      var endTime = Date.now();
      var timeSpent = endTime - quizStartTime;

      // Mark unit test as completed in localStorage if all correct
      if (correctCount === totalQuestions) {
        var testPath = decodeURIComponent(window.location.pathname);
        var unitMatch = testPath.match(/Unit(\w+)_Test/);
        
        if (unitMatch) {
          var unitId = unitMatch[1];
          var lessonNum;
          var coursePrefix;
          
          // Detect course from path
          if (testPath.includes('Algebra1Lessons')) {
            coursePrefix = 'alg1';
            var alg1TestLessonMap = {
              '1': 8, '2': 10, '3': 8, '4': 9, '5': 11, '6': 7,
              '7': 9, '8': 5, '9': 5, '10': 5, '11': 4, '12': 5
            };
            lessonNum = alg1TestLessonMap[unitId] || 10; 
          } else if (testPath.includes('Algebra2Lessons')) {
            coursePrefix = 'alg2';
             var alg2TestLessonMap = {
              '1': 10, '2': 8, '3': 8, '4': 7, '5': 8,
              '6': 6, '7': 8, '8': 7, '9': 5
            };
            lessonNum = alg2TestLessonMap[unitId] || 10;
          } else if (testPath.includes('GeometryLessons')) {
            coursePrefix = 'geometry';
            var geomTestLessonMap = {
              '1': 8, '2': 10, '3': 8, '4': 9, '5': 7,
              '6': 8, '7': 9, '8': 9, '9': 8, '10': 10,
              '11': 7, '12': 10, '13': 8
            };
            lessonNum = geomTestLessonMap[unitId] || 8;
          } else if (testPath.includes('PhysicsLessons')) {
            coursePrefix = 'physics';
            var physicsTestLessonMap = {
              '1': 7, '2': 7, '3': 9, '4': 7, '5': 7, '6': 7,
              '7': 9, '8': 7, '9': 7, '10': 10, '11': 7
            };
            lessonNum = physicsTestLessonMap[unitId];
          } else if (testPath.includes('ChemistryLessons')) {
            coursePrefix = 'chem';
            var chemTestLessonMap = {
              '1': 9, '2': 6, '3': 9, '4': 10,
              '5A': 9, '5B': 6,
              '6': 8, '7': 9, '8': 10, '9': 9,
              '10': 11, '11': 7, '12': 6
            };
            lessonNum = chemTestLessonMap[unitId];
          } else if (testPath.includes('BiologyLessons')) {
            coursePrefix = 'bio';
            lessonNum = 8; // Assuming same as geometry
          }
          
          if (coursePrefix && lessonNum) {
            localStorage.setItem(coursePrefix + '_u' + unitId + '_l' + lessonNum + '_completed', 'true');
          }
        }
      }

      form.style.display = 'none';

      var finishScreen = document.getElementById('quiz-finish-screen');
      if (finishScreen) {
        finishScreen.style.display = 'flex';
        document.getElementById('quiz-final-score').textContent = correctCount + '/' + totalQuestions;
        document.getElementById('quiz-final-percent').textContent = Math.round((correctCount / totalQuestions) * 100) + '%';

        var seconds = Math.floor(timeSpent / 1000);
        var m = Math.floor(seconds / 60).toString().padStart(2, '0');
        var s = (seconds % 60).toString().padStart(2, '0');
        document.getElementById('quiz-time-spent').textContent = m + ':' + s;
      }
    }
  };

  // ========== 7. Climb Game Logic ==========
  (function () {
    var climbScore = 0;
    var playerPosition = 35;
    var isGameRunning = false;
    var isPaused = false;
    var spacePressed = false;
    var gameLoopId = null;
    var currentQuestion = null;
    var climbFuel = 50;
    var downwardAccel = 0;

    document.addEventListener('keydown', function (e) { if (e.code === 'Space') { spacePressed = true; if (isGameRunning) e.preventDefault(); } });
    document.addEventListener('keyup', function (e) { if (e.code === 'Space') spacePressed = false; });

    var WIN_HEIGHT = 90;
    var CLIMB_STEP = 15;
    var FALL_RATE = 0.04;
    var TICK_RATE = 20;

    window.initClimbGame = function () {
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

    window.toggleClimbFullscreen = function () {
      var elem = document.getElementById('climb-game-ui');
      if (!document.fullscreenElement) {
        if (elem.requestFullscreen) elem.requestFullscreen().catch(function () {});
        else if (elem.webkitRequestFullscreen) elem.webkitRequestFullscreen();
        else if (elem.msRequestFullscreen) elem.msRequestFullscreen();
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
        else if (document.webkitExitFullscreen) document.webkitExitFullscreen();
        else if (document.msExitFullscreen) document.msExitFullscreen();
      }
    };

    window.exitClimbGame = function () {
      var ui = document.getElementById('climb-game-ui');
      if (ui) ui.style.display = 'none';
      isGameRunning = false;
      if (gameLoopId) clearInterval(gameLoopId);
      window.switchToFlashcards();
    };

    window.toggleClimbPause = function () {
      if (!isGameRunning && !isPaused) return;
      isPaused = !isPaused;
      var btn = document.getElementById('climb-pause-btn');
      if (btn) btn.innerText = isPaused ? _t('Resume', '继续') : _t('Pause', '暂停');
      var pauseScreen = document.getElementById('climb-paused-screen');
      if (pauseScreen) pauseScreen.style.display = isPaused ? 'flex' : 'none';
    };

    window.resetToClimbMenu = function () {
      isGameRunning = false;
      isPaused = false;
      if (gameLoopId) clearInterval(gameLoopId);
      document.getElementById('climb-game-ui').style.display = 'flex';
      document.getElementById('climb-start-screen').style.display = 'flex';
      document.getElementById('climb-game-over').style.display = 'none';
      document.getElementById('climb-interaction').style.display = 'none';
      var pauseScreen = document.getElementById('climb-paused-screen');
      if (pauseScreen) pauseScreen.style.display = 'none';
      var pBtn = document.getElementById('climb-pause-btn');
      if (pBtn) pBtn.innerText = _t('Pause', '暂停');
      var interaction = document.getElementById('climb-interaction');
      if (interaction) interaction.style.opacity = '1';
    };

    window.startClimbGame = function () {
      isPaused = false;
      var pBtn = document.getElementById('climb-pause-btn');
      if (pBtn) pBtn.innerText = _t('Pause', '暂停');
      var interaction = document.getElementById('climb-interaction');
      if (interaction) interaction.style.opacity = '1';
      climbScore = 0;
      climbFuel = 50;
      playerPosition = 35;
      isGameRunning = true;
      document.getElementById('climb-start-screen').style.display = 'none';
      document.getElementById('climb-game-over').style.display = 'none';
      document.getElementById('climb-question-area').style.display = 'block';
      document.getElementById('climb-interaction').style.display = 'flex';
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
        if (typeof updateFuelDisplay === 'function') updateFuelDisplay();
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
      if (playerPosition <= 0) endGame();
      updatePlayerPos();
      updateFuelDisplay();
    }

    function updateDisplay() {
      document.getElementById('climb-score').innerText = _t('Score:', '分数:') + ' ' + climbScore;
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
      feedback.innerText = '';
      feedback.className = '';
      if (!window.lessonFlashcards || window.lessonFlashcards.length === 0) {
        document.getElementById('climb-question-text').innerText = 'No flashcards found for this lesson!';
        return;
      }
      if (!window.usedFlashcardIndices) window.usedFlashcardIndices = [];
      if (!window.lessonFlashcards) {
        if (typeof window.initFlashcards === 'function') window.initFlashcards();
      }
      var availablePool = [];
      if (window.lessonFlashcards) {
        availablePool = window.lessonFlashcards
          .map(function (_, i) { return i; })
          .filter(function (i) { return !window.usedFlashcardIndices.includes(i); });
      }
      var qIdx;
      if (availablePool.length > 0) {
        qIdx = availablePool[Math.floor(Math.random() * availablePool.length)];
      } else {
        window.usedFlashcardIndices = [];
        qIdx = Math.floor(Math.random() * (window.lessonFlashcards ? window.lessonFlashcards.length : 0));
      }
      window.usedFlashcardIndices.push(qIdx);
      currentQuestion = window.lessonFlashcards[qIdx];
      var _tr = window.arisTranslate || function(t){return t;};
      document.getElementById('climb-question-text').innerText = _tr(currentQuestion.question);

      var options = [currentQuestion.answer];
      var uniqueOptions = new Set([currentQuestion.answer]);
      var allAnswers = window.lessonFlashcards.map(function (f) { return f.answer; });
      for (var i = allAnswers.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var t = allAnswers[i]; allAnswers[i] = allAnswers[j]; allAnswers[j] = t;
      }
      for (var k = 0; k < allAnswers.length; k++) {
        if (!uniqueOptions.has(allAnswers[k])) {
          options.push(allAnswers[k]);
          uniqueOptions.add(allAnswers[k]);
          if (options.length >= 3) break;
        }
      }
      for (var i2 = options.length - 1; i2 > 0; i2--) {
        var j2 = Math.floor(Math.random() * (i2 + 1));
        var t2 = options[i2]; options[i2] = options[j2]; options[j2] = t2;
      }

      var optionsContainer = document.getElementById('climb-options');
      optionsContainer.innerHTML = '';
      options.forEach(function (opt) {
        var btn = document.createElement('button');
        btn.className = 'climb-option-btn';
        btn.innerText = _tr(opt);
        btn.onclick = function () { handleClimbAnswer(opt); };
        optionsContainer.appendChild(btn);
      });
    }

    function handleClimbAnswer(selected) {
      if (isPaused || !isGameRunning) return;
      var isBoosting = spacePressed && climbFuel > 0;
      if (isBoosting) {
        playerPosition = Math.min(95, playerPosition + 0.5);
        climbFuel = Math.max(0, climbFuel - 0.2);
        if (typeof updateFuelDisplay === 'function') updateFuelDisplay();
      }
      var fOut = document.getElementById('climb-flame-outer');
      var fIn = document.getElementById('climb-flame-inner');
      if (fOut && fIn) {
        var scale = isBoosting ? 'scale(1.2, 2.0)' : 'scale(1, 1)';
        fOut.style.transform = scale;
        fIn.style.transform = scale;
      }
      var feedback = document.getElementById('climb-feedback');
      if (selected === currentQuestion.answer) {
        climbScore += 10;
        climbFuel = Math.min(100, climbFuel + 20);
        feedback.innerText = _t('Correct! Adding fuel...');
        feedback.style.color = '#16a34a';
      } else {
        playerPosition -= 5;
        feedback.innerText = _t('Oops! Slipping down...');
        feedback.style.color = '#dc2626';
      }
      updateDisplay();
      var btns = document.querySelectorAll('.climb-option-btn');
      btns.forEach(function (b) { b.disabled = true; });
      setTimeout(function () { nextClimbQuestion(); }, 1000);
    }

    function endGame() {
      isGameRunning = false;
      clearInterval(gameLoopId);
      document.getElementById('climb-question-area').style.display = 'none';
      document.getElementById('climb-interaction').style.display = 'none';
      var gameOverScreen = document.getElementById('climb-game-over');
      gameOverScreen.style.display = 'flex';
      var title = document.getElementById('climb-result-title');
      var msg = document.getElementById('climb-final-score');
      var storageKey = 'climbHighScore';
      try {
        var currentUser = JSON.parse(localStorage.getItem('user'));
        if (currentUser && currentUser.email) storageKey = 'climbHighScore_' + currentUser.email;
      } catch (e) { console.error(e); }
      var highScore = parseInt(localStorage.getItem(storageKey) || 0);
      if (climbScore > highScore) {
        highScore = climbScore;
        localStorage.setItem(storageKey, highScore);
        title.innerText = _t('🏆 New High Score! 🏆');
        title.style.color = '#f59e0b';
      } else {
        title.innerText = _t('Game Over', '游戏结束');
        title.style.color = '#1e293b';
      }
      msg.innerHTML = _t('Score:', '分数:') + ' ' + climbScore + '<br><span style="font-size:0.9em; color:#64748b">' + _t('Best:', '最高：') + ' ' + highScore + '</span>';
    }
  })();

  // ========== 8. Init on DOMContentLoaded ==========
  document.addEventListener('DOMContentLoaded', function () {
    var hasPracticeView = !!document.getElementById('practice-content-view');
    var hasQuizView = !!document.getElementById('quiz-content-view');
    
    if (hasPracticeView && hasQuizView) {
      // Combined page — inject games HTML and show practice
      injectPracticeGamesHTML();
      showPractice();
    } else if (hasPracticeView && !hasQuizView) {
      // Practice-only page (_Test_Practice.html) — already has flashcard HTML
      // Do NOT call injectPracticeGamesHTML() as it would destroy existing content
      // Just reset flashcards init flag so they can be initialized with the existing DOM
      window.flashcardsInitialized = false;
      if (typeof window.initFlashcards === 'function') window.initFlashcards();
      showPractice();
    }
    
    if (hasQuizView) {
      // Test page or combined page — inject finish screen
      injectQuizFinishStyles();
      injectQuizFinishScreen();
      
      // If no practice view, show quiz directly and start timer
      if (!hasPracticeView) {
        // Check if already completed
        var storageKey = getUnitTestStorageKey();
        if (storageKey && localStorage.getItem(storageKey) === 'true') {
          // Show "Already Completed" screen
          var quizView = document.getElementById('quiz-content-view');
          if (quizView) quizView.style.display = 'block';
          var quizForm = document.getElementById('quiz-form');
          if (quizForm) quizForm.style.display = 'none';
          var finishScreen = document.getElementById('quiz-finish-screen');
          if (finishScreen) {
            finishScreen.style.display = 'flex';
            var h2 = finishScreen.querySelector('h2');
            if (h2) h2.textContent = '\u2705 Already Completed!';
            var scoreEl = document.getElementById('quiz-final-score');
            if (scoreEl) scoreEl.parentElement.style.display = 'none';
            var pctEl = document.getElementById('quiz-final-percent');
            if (pctEl) pctEl.parentElement.style.display = 'none';
            var timeEl = document.getElementById('quiz-time-spent');
            if (timeEl) timeEl.parentElement.style.display = 'none';
          }
        } else {
          quizStartTime = Date.now();
          var quizView = document.getElementById('quiz-content-view');
          if (quizView) quizView.style.display = 'block';
        }
      }
    }

    // "Take the test" button — navigate to _Test.html on practice-only pages, or switch view
    var takeTestBtn = document.getElementById('take-test-btn');
    if (takeTestBtn) {
      takeTestBtn.addEventListener('click', function () {
        if (hasQuizView) {
          // Combined page — switch to quiz view
          window.showQuiz();
        } else {
          // Practice-only page — navigate to test file
          var currentUrl = window.location.href;
          window.location.href = currentUrl.replace('_Test_Practice.html', '_Test.html');
        }
      });
    }

    // Attach listeners to practice menu items
    document.querySelectorAll('a[href="#climb"]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        window.switchToClimb();
        if (window.togglePracticesPanel && el.closest('.Practices-menu')) {
          var btn = el.closest('.Practices-menu').querySelector('.view-other-Practices');
          if (btn) window.togglePracticesPanel(btn);
        }
      });
    });

    document.querySelectorAll('a[href="#flashcard-game"]').forEach(function (el) {
      el.addEventListener('click', function (e) {
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
