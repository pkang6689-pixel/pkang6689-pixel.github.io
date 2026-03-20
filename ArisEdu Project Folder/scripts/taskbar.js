
// Inject AI Assistant and Features Scripts
(function() {
    // Translation Helper - expose globally
    window._t = window._t || function(key) {
        if (window.arisTranslate) return window.arisTranslate(key);
        if (window.globalTranslations && window.globalTranslations[key]) return window.globalTranslations[key];
        return key;
    };

    // Detect base path for GitHub Pages vs Local File
    // If we are in /ArisEdu Project Folder/, scripts are in ./scripts/
    // If we are in root, scripts are in ./ArisEdu Project Folder/scripts/
    
    // Safe Script Path Calculation
    function getScriptPath(filename) {
        // Handle local file system paths vs server paths
        const isFileProtocol = window.location.protocol === 'file:';
        
        // Base absolute path for server/github pages
        const serverPath = "/ArisEdu Project Folder/scripts/" + filename;
        
        if (!isFileProtocol) return serverPath;

        // LOCAL FILE SYSTEM LOGIC
        // Check if we are inside "ArisEdu Project Folder"
        const path = decodeURIComponent(window.location.pathname);
        if (path.includes('ArisEdu Project Folder')) {
             // Split by the folder name to determine depth
             const parts = path.split('ArisEdu Project Folder');
             // The second part is inevitably the path AFTER the project folder
             // e.g., "/Dashboard.html" or "/Algebra1Lessons/Unit1/Lesson1.html"
             
             if (parts.length > 1) {
                 const relativePath = parts[1];
                 // Count how many directory levels deep we are
                 // /Dashboard.html -> 1 slash -> 0 folders deep -> scripts/
                 // /Algebra1Lessons/Unit1/Lesson1.html -> 3 slashes -> 2 folders deep -> ../../scripts/
                 
                 // Remove leading slash if present
                 const cleanPath = relativePath.startsWith('/') ? relativePath.substring(1) : relativePath;
                 const segments = cleanPath.split('/').length - 1; // -1 because filename doesn't count as folder
                 
                 let rel = "scripts/";
                 for(let i=0; i<segments; i++) rel = "../" + rel;
                 return rel + filename;
             }
        }
        
        // Fallback: Assume we are in root and scripts are in subdir
        return "ArisEdu Project Folder/scripts/" + filename;
    }

    [
        "ai_assistant.js",
        "tools_panel.js",
        "badges.js",
        "ambience_controller.js",
        "layout_adjuster.js",
        "update_notifier.js",
        "course-progress-firebase.js"
    ].forEach(name => {
        // Check if script already exists to prevent duplicates
        // Note: querySelector logic is imperfect for relative paths, check src content
        const targetSrc = getScriptPath(name);
        
        // Check if any script ends with this filename
        const exists = Array.from(document.scripts).some(s => s.src.includes(name));
        
        if(!exists) {
            var script = document.createElement('script');
            script.src = targetSrc;
            if (name === "course-progress-firebase.js") {
                script.type = "module";
            }
            document.head.appendChild(script);
        }
    });
})();

// taskbar.js — Shared taskbar injection + logic for all pages
(function () {
    // --- Inject vital styles for taskbar components (e.g. settings menu) ---
    if(!document.getElementById('aris-taskbar-styles')) {
        const style = document.createElement('style');
        style.id = 'aris-taskbar-styles';
        style.innerHTML = `
            .settings-menu {
                position: fixed;
                z-index: var(--z-settings); /* Higher than modal */
                background-color: #ffffff;
                color: #0f172a;
                padding: 0.5rem;
                border-radius: 0.75rem;
                box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
                min-width: 220px;
                visibility: hidden;
                opacity: 0;
                transform: translateY(-10px) scale(0.95);
                transition: opacity 0.2s, transform 0.2s, visibility 0.2s;
                border: 1px solid #e2e8f0;
                top: 60px; /* Fallback */
            }
            body.dark-mode .settings-menu {
                background-color: #1e293b; 
                color: #f1f5f9;
                border-color: #334155;
                box-shadow: 0 10px 25px -5px rgba(0,0,0,0.5), 0 8px 10px -6px rgba(0,0,0,0.5);
            }
            .settings-item {
                padding: 0.75rem 1rem;
                display: flex;
                align-items: center;
                gap: 0.75rem;
                color: inherit;
                text-decoration: none;
                cursor: pointer;
                border-radius: 0.5rem;
                transition: background 0.2s, color 0.2s;
                font-weight: 500;
                font-size: 0.95rem;
            }
            .settings-item:hover {
                background-color: #f1f5f9;
                color: #3b82f6;
            }
            body.dark-mode .settings-item:hover {
                background-color: rgba(255,255,255,0.08);
                color: #3b82f6;
            }
        `;
        document.head.appendChild(style);
    }

  // Determine page type and back-button behavior from URL
  var path = decodeURIComponent(window.location.pathname);
  var filename = path.split('/').pop();
  var backText = '';
  var backUrl = '';
  var showBack = true;

  // Detect the lesson-folder context from the URL
  var parts = path.split('/');
  var lessonFolder = '';
  for (var i = 0; i < parts.length; i++) {
    if (parts[i].indexOf('Lessons') !== -1) { lessonFolder = parts[i]; break; }
  }

  // Map lesson folders → course pages (default: high school)
  var courseMap = {
    ChemistryLessons: '/ArisEdu Project Folder/CourseHomepage/chem.html',
    PhysicsLessons:   '/ArisEdu Project Folder/CourseHomepage/physics.html',
    BiologyLessons:   '/ArisEdu Project Folder/CourseHomepage/bio.html',
    Algebra1Lessons:  '/ArisEdu Project Folder/CourseHomepage/algebra1.html',
    Algebra2Lessons:  '/ArisEdu Project Folder/CourseHomepage/algebra2.html',
    GeometryLessons:  '/ArisEdu Project Folder/CourseHomepage/geometry.html',
    AnatomyLessons:   '/ArisEdu Project Folder/CourseHomepage/anatomy.html',
    AstronomyLessons: '/ArisEdu Project Folder/CourseHomepage/astronomy.html',
    EarthScienceLessons: '/ArisEdu Project Folder/CourseHomepage/earth_science.html',
    EnvironmentalScienceLessons: '/ArisEdu Project Folder/CourseHomepage/environmental_science.html',
    FinancialMathLessons: '/ArisEdu Project Folder/CourseHomepage/financial_math.html',
    IntegratedScienceLessons: '/ArisEdu Project Folder/CourseHomepage/integrated_science.html',
    LinearAlgebraLessons: '/ArisEdu Project Folder/CourseHomepage/linear_algebra.html',
    MarineScienceLessons: '/ArisEdu Project Folder/CourseHomepage/marine_science.html',
    PrecalculusLessons: '/ArisEdu Project Folder/CourseHomepage/precalculus.html',
    StatisticsLessons: '/ArisEdu Project Folder/CourseHomepage/statistics.html',
    TrigonometryLessons: '/ArisEdu Project Folder/CourseHomepage/trigonometry.html',
    MS_Algebra1Lessons: '/ArisEdu Project Folder/CourseHomepage/ms_algebra1.html',
    MS_Algebra2Lessons: '/ArisEdu Project Folder/CourseHomepage/ms_algebra2.html',
    MS_BiologyLessons: '/ArisEdu Project Folder/CourseHomepage/ms_bio.html',
    MS_ChemistryLessons: '/ArisEdu Project Folder/CourseHomepage/ms_chem.html',
    MS_GeometryLessons: '/ArisEdu Project Folder/CourseHomepage/ms_geometry.html',
    MS_PhysicsLessons: '/ArisEdu Project Folder/CourseHomepage/ms_physics.html'
  };

  // --- Course origin tracking (middle school / high school) ---
  // Map course page filenames to their lesson folder
  var fileToLessonFolder = {
    'chem.html': 'ChemistryLessons', 'ms_chem.html': 'MS_ChemistryLessons',
    'physics.html': 'PhysicsLessons', 'ms_physics.html': 'MS_PhysicsLessons',
    'bio.html': 'BiologyLessons', 'ms_bio.html': 'MS_BiologyLessons',
    'algebra1.html': 'Algebra1Lessons', 'ms_algebra1.html': 'MS_Algebra1Lessons',
    'algebra2.html': 'Algebra2Lessons', 'ms_algebra2.html': 'MS_Algebra2Lessons',
    'geometry.html': 'GeometryLessons', 'ms_geometry.html': 'MS_GeometryLessons',
    'anatomy.html': 'AnatomyLessons',
    'astronomy.html': 'AstronomyLessons',
    'earth_science.html': 'EarthScienceLessons',
    'environmental_science.html': 'EnvironmentalScienceLessons',
    'financial_math.html': 'FinancialMathLessons',
    'integrated_science.html': 'IntegratedScienceLessons',
    'linear_algebra.html': 'LinearAlgebraLessons',
    'marine_science.html': 'MarineScienceLessons',
    'precalculus.html': 'PrecalculusLessons',
    'statistics.html': 'StatisticsLessons',
    'trigonometry.html': 'TrigonometryLessons'
  };

  // If we're on a course page (HS or MS), store origin for lesson back-navigation
  var folderForCurrent = fileToLessonFolder[filename];
  if (folderForCurrent) {
    try {
      sessionStorage.setItem('courseOrigin_' + folderForCurrent, '/ArisEdu Project Folder/CourseHomepage/' + filename);
      // Also set simple courseOrigin for MS-mode detection in other scripts
      sessionStorage.setItem('courseOrigin', filename);
    } catch(e) {}
  }

  // If we're on a lesson page, override courseMap with stored origin
  if (lessonFolder) {
    try {
      var storedOrigin = sessionStorage.getItem('courseOrigin_' + lessonFolder);
      if (storedOrigin) {
        courseMap[lessonFolder] = storedOrigin;
        // Also set simple courseOrigin for MS-mode detection in other scripts
        var _originFile = storedOrigin.split('/').pop();
        sessionStorage.setItem('courseOrigin', _originFile);
      }
    } catch(e) {}
  }

  // --- Chemistry lesson files (underscore suffixes) ---
  if (filename.indexOf('_Practice') !== -1) {
    if (filename.includes('Test')) {
         // Special handling for Unit Tests: Back to Course
         backText = '\u2190 Back to Course';
         backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
    } else {
         backText = '\u2190 Back to Summary';
         backUrl = filename.replace('_Practice.html', '_Summary.html');
    }
  } else if (filename.indexOf('_Summary') !== -1) {
    backText = '\u2190 Back to Lesson';
    backUrl = filename.replace('_Summary.html', '_Video.html');
  } else if (filename.indexOf('_Quiz') !== -1) {
    backText = '\u2190 Back to Practice';
    backUrl = filename.replace('_Quiz.html', '_Practice.html');
  } else if (filename.indexOf('_Video') !== -1) {
    backText = '\u2190 Back to Course';
    backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
  }
  // --- Legacy check (space-separated names) ---
  else if (filename.indexOf(' Practice') !== -1) {
    backText = '\u2190 Back to Summary';
    backUrl = filename.replace(' Practice.html', ' Summary.html');
  } else if (filename.indexOf(' Summary') !== -1) {
    backText = '\u2190 Back to Lesson';
    var lessonMatch = filename.match(/Lesson\s(\d+\.\d+)/);
    if (lessonMatch) {
        backUrl = 'Lesson ' + lessonMatch[1] + '_Video.html';
    } else {
        backUrl = filename.replace(' Summary.html', '.html');
    }
  } else if (filename.indexOf(' Quiz') !== -1) {
    backText = '\u2190 Back to Practice';
    backUrl = filename.replace(' Quiz.html', ' Practice.html');
  }
  // --- Any lesson file in a Unit folder (catches both physics and chemistry) ---
  else if (lessonFolder && /^Lesson/.test(filename)) {
    backText = '\u2190 Back to Course';
    backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
  }
  // --- Course pages (chem.html, ms_chem.html, physics.html, etc.) —→ back to Courses ---
  else if (/^(ms_)?(chem|physics|bio|algebra1|algebra2|geometry|anatomy|astronomy|earth_science|environmental_science|financial_math|integrated_science|linear_algebra|marine_science|precalculus|statistics|trigonometry|ap_biology|ap_chemistry|ap_calculus|ap_environmental_science|ap_hug|ap_physics1|ap_physics2|ap_physics_mechanics|ap_statistics)\.html$/.test(filename)) {
    backText = '\u2190 Back to Courses';
    backUrl = '/ArisEdu Project Folder/Courses.html';
  }
  // --- Top-level pages without a back button ---
  else {
    showBack = false;
  }

  // Only inject HTML if it doesn't already exist
  if (!document.querySelector('nav.taskbar')) {
    var tbSettings = {};
    try { tbSettings = JSON.parse(localStorage.getItem('arisEduTaskbarSettings') || '{}'); } catch(e){}
    var getDisp = function(k) { return (tbSettings[k] === false) ? ' style="display:none"' : ''; };

    var backBtnHtml = showBack
      ? '<button class="taskbar-button" id="back-button">' + backText + '</button>'
      : '';
    var nav = document.createElement('nav');
    nav.className = 'taskbar';

    // ========== BUILD BREADCRUMBS ==========
    var breadcrumbs = [];
    breadcrumbs.push({label: '\uD83C\uDFE0 Home', url: '/index.html'});

    // Determine breadcrumb chain from URL context
    if (lessonFolder) {
      breadcrumbs.push({label: 'Courses', url: '/ArisEdu Project Folder/Courses.html'});
      // Friendly course name from folder
      var courseFriendly = {
        ChemistryLessons: 'Chemistry', PhysicsLessons: 'Physics', BiologyLessons: 'Biology',
        Algebra1Lessons: 'Algebra 1', Algebra2Lessons: 'Algebra 2', GeometryLessons: 'Geometry',
        AnatomyLessons: 'Anatomy', AstronomyLessons: 'Astronomy',
        EarthScienceLessons: 'Earth Science', EnvironmentalScienceLessons: 'Environmental Science',
        FinancialMathLessons: 'Financial Math', IntegratedScienceLessons: 'Integrated Science',
        LinearAlgebraLessons: 'Linear Algebra', MarineScienceLessons: 'Marine Science',
        PrecalculusLessons: 'Precalculus', StatisticsLessons: 'Statistics',
        TrigonometryLessons: 'Trigonometry',
        MS_Algebra1Lessons: 'MS Algebra 1', MS_Algebra2Lessons: 'MS Algebra 2',
        MS_BiologyLessons: 'MS Biology', MS_ChemistryLessons: 'MS Chemistry',
        MS_GeometryLessons: 'MS Geometry', MS_PhysicsLessons: 'MS Physics'
      };
      var courseLabel = courseFriendly[lessonFolder] || lessonFolder.replace('Lessons','');
      breadcrumbs.push({label: courseLabel, url: courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html'});

      // Parse unit from path (e.g., "Unit3")
      var unitMatch = path.match(/Unit\s*(\w+)/i);
      if (unitMatch) {
        breadcrumbs.push({label: 'Unit ' + unitMatch[1], url: null});
      }

      // Parse lesson from filename
      var lessonFileMatch = filename.match(/Lesson\s*(\w+\.\d+)/);
      if (lessonFileMatch) {
        var pageType = '';
        if (filename.indexOf('_Video') !== -1) pageType = 'Video';
        else if (filename.indexOf('_Summary') !== -1) pageType = 'Summary';
        else if (filename.indexOf('_Practice') !== -1) pageType = 'Practice';
        else if (filename.indexOf('_Quiz') !== -1) pageType = 'Quiz';
        var lessonLabel = 'Lesson ' + lessonFileMatch[1];
        if (pageType) lessonLabel += ' \u2014 ' + pageType;
        breadcrumbs.push({label: lessonLabel, url: null});
      } else if (filename.indexOf('Test') !== -1) {
        breadcrumbs.push({label: 'Unit Test', url: null});
      }
    } else if (/^(ms_)?(chem|physics|bio|algebra1|algebra2|geometry|anatomy|astronomy|earth_science|environmental_science|financial_math|integrated_science|linear_algebra|marine_science|precalculus|statistics|trigonometry|ap_biology|ap_chemistry|ap_calculus|ap_environmental_science|ap_hug|ap_physics1|ap_physics2|ap_physics_mechanics|ap_statistics)\.html$/.test(filename)) {
      breadcrumbs.push({label: 'Courses', url: '/ArisEdu Project Folder/Courses.html'});
      // Derive friendly name from filename
      var subjectName = filename.replace('.html','').replace(/_/g,' ').replace(/\bms\b/i,'MS').replace(/\bap\b/i,'AP');
      subjectName = subjectName.replace(/\b\w/g, function(c){ return c.toUpperCase(); });
      breadcrumbs.push({label: subjectName, url: null});
    } else if (filename === 'Courses.html') {
      breadcrumbs.push({label: 'Courses', url: null});
    } else if (filename === 'Dashboard.html') {
      breadcrumbs.push({label: 'Dashboard', url: null});
    } else if (filename === 'arcade.html') {
      breadcrumbs.push({label: 'Arcade', url: null});
    } else if (filename === 'forums.html') {
      breadcrumbs.push({label: 'Forums', url: null});
    } else if (filename === 'Preferences.html') {
      breadcrumbs.push({label: 'Preferences', url: null});
    } else if (filename === 'FAQ.html') {
      breadcrumbs.push({label: 'Help', url: null});
    } else if (filename === 'Login.html' || filename === 'Signup.html' || filename === 'LoginSignup.html') {
      breadcrumbs.push({label: 'Login', url: null});
    } else if (filename === 'AccountInfo.html') {
      breadcrumbs.push({label: 'Account', url: null});
    }

    var bcHtml = '';
    if (breadcrumbs.length > 1) {
      bcHtml = '<div class="breadcrumb-bar">';
      for (var bi = 0; bi < breadcrumbs.length; bi++) {
        if (bi > 0) bcHtml += '<span class="breadcrumb-sep">\u203A</span>';
        var isLast = (bi === breadcrumbs.length - 1);
        if (isLast || !breadcrumbs[bi].url) {
          bcHtml += '<span class="' + (isLast ? 'bc-current' : '') + '">' + breadcrumbs[bi].label + '</span>';
        } else {
          bcHtml += '<a href="' + breadcrumbs[bi].url + '">' + breadcrumbs[bi].label + '</a>';
        }
      }
      bcHtml += '</div>';
    }

    // ========== LANGUAGE DROPDOWN HTML (shared) ==========
    var langDropdownHtml =
      '<div id="language-dropdown" style="display:none;position:fixed;z-index:var(--z-dropdown);min-width:160px;background:var(--card-bg,#ffffff);border:1px solid var(--border-color,#e2e8f0);border-radius:0.5rem;box-shadow:0 8px 24px rgba(0,0,0,0.15);overflow:hidden;">' +
        '<button class="lang-option" data-lang="english" style="display:block;width:100%;text-align:left;padding:0.6rem 1rem;background:none;border:none;color:var(--text-color,#0f172a);cursor:pointer;font-size:0.95rem;">English</button>' +
        '<button class="lang-option" data-lang="spanish" style="display:block;width:100%;text-align:left;padding:0.6rem 1rem;background:none;border:none;color:var(--text-color,#0f172a);cursor:pointer;font-size:0.95rem;">Español</button>' +
        '<button class="lang-option" data-lang="hindi" style="display:block;width:100%;text-align:left;padding:0.6rem 1rem;background:none;border:none;color:var(--text-color,#0f172a);cursor:pointer;font-size:0.95rem;">हिन्दी</button>' +
        '<button class="lang-option" data-lang="chinese" style="display:block;width:100%;text-align:left;padding:0.6rem 1rem;background:none;border:none;color:var(--text-color,#0f172a);cursor:pointer;font-size:0.95rem;">中文</button>' +
        '<button class="lang-option" data-lang="traditional" style="display:block;width:100%;text-align:left;padding:0.6rem 1rem;background:none;border:none;color:var(--text-color,#0f172a);cursor:pointer;font-size:0.95rem;">繁體中文</button>' +
        '<div style="border-top:1px solid var(--border-color,#e2e8f0);padding:0.5rem 1rem;font-size:0.8rem;color:var(--text-muted,#64748b);text-align:center;">💡 Reload to apply</div>' +
      '</div>';

    // ========== SETTINGS MENU HTML (shared) ==========
    var settingsMenuHtml =
      '<div aria-hidden="true" class="settings-menu" id="settings-menu" role="menu" aria-label="Settings">' +
        '<div class="settings-item" role="menuitem">' +
          '<label style="display:flex;align-items:center;gap:0.5rem;cursor:pointer;">' +
            '<input checked id="dark-mode-checkbox" type="checkbox" aria-label="Toggle dark mode"/>' +
            '<span>Dark Mode</span>' +
          '</label>' +
        '</div>' +
        '<a class="settings-item" href="/ArisEdu Project Folder/Preferences.html" data-i18n="Preferences" role="menuitem">Preferences</a>' +
        '<a class="settings-item" href="/ArisEdu Project Folder/FAQ.html" data-i18n="Help" role="menuitem">Help</a>' +
      '</div>';

    // ========== MOBILE DRAWER HTML ==========
    var mobileDrawerHtml =
      '<div class="mobile-drawer-overlay" id="mobile-drawer-overlay"></div>' +
      '<div class="mobile-drawer" id="mobile-drawer" role="dialog" aria-modal="true" aria-label="Navigation menu">' +
        '<div class="mobile-drawer-header">' +
          '<span class="drawer-title">Menu</span>' +
          '<button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close menu">&times;</button>' +
        '</div>' +
        '<nav class="mobile-drawer-section" aria-label="Main pages">' +
          '<div class="mobile-drawer-section-title">Navigation</div>' +
          '<a class="drawer-item" href="/index.html">\uD83C\uDFE0 Home</a>' +
          '<a class="drawer-item" href="/ArisEdu Project Folder/Dashboard.html">\uD83D\uDCCA Dashboard</a>' +
          '<a class="drawer-item" href="/ArisEdu Project Folder/Courses.html">\uD83D\uDCDA Courses</a>' +
        '</nav>' +
        '<div class="drawer-divider"></div>' +
        '<nav class="mobile-drawer-section" aria-label="Discover">' +
          '<div class="mobile-drawer-section-title">Discover</div>' +
          '<a class="drawer-item" href="/ArisEdu Project Folder/arcade.html">\uD83D\uDC7E Arcade</a>' +
          '<button class="drawer-item" id="drawer-forums-btn">\uD83D\uDCAC Forums</button>' +
        '</nav>' +
        '<div class="drawer-divider"></div>' +
        '<div class="mobile-drawer-section" role="group" aria-label="Tools">' +
          '<div class="mobile-drawer-section-title">Tools</div>' +
          '<button class="drawer-item" id="drawer-search-btn">\uD83D\uDD0D Search</button>' +
          '<button class="drawer-item" id="drawer-ai-btn">\uD83E\uDD16 AI Assistant</button>' +
          '<button class="drawer-item" id="drawer-update-btn">\uD83D\uDD14 Updates</button>' +
        '</div>' +
        '<div class="drawer-divider"></div>' +
        '<div class="mobile-drawer-section" role="group" aria-label="Account">' +
          '<div class="mobile-drawer-section-title">Account</div>' +
          '<button class="drawer-item" id="drawer-settings-btn">\u2699\uFE0F Settings</button>' +
          '<a class="drawer-item" href="/ArisEdu Project Folder/Login.html" id="drawer-login-btn">\uD83D\uDD10 Login</a>' +
          '<button class="drawer-item" id="drawer-lang-btn">\uD83C\uDF0D Language</button>' +
        '</div>' +
      '</div>';

    // ========== CONSOLIDATED TASKBAR LAYOUT ==========
    nav.setAttribute('role', 'navigation');
    nav.setAttribute('aria-label', 'Main navigation');
  // --- Build lesson-nav center section (only on lesson pages) ---
  // Uses the same circle + connector stepper as the page progress bar
  var lessonNavHtml = '';
  if (lessonFolder && /^Lesson/.test(filename)) {
    var lessonBase = '';
    var m = filename.match(/^(Lesson\s*\d+\.\d+)/);
    if (m) lessonBase = m[1];
    if (lessonBase) {
      var usesUnderscore = filename.indexOf('_Video') !== -1 || filename.indexOf('_Summary') !== -1 || filename.indexOf('_Practice') !== -1 || filename.indexOf('_Quiz') !== -1;
      var sep = usesUnderscore ? '_' : ' ';
      var tbSteps = [
        { key: 'Video',    label: 'Video',    icon: '\u25B6',        suffix: sep + 'Video.html' },
        { key: 'Summary',  label: 'Summary',  icon: '\uD83D\uDCCB', suffix: sep + 'Summary.html' },
        { key: 'Practice', label: 'Practice', icon: '\uD83C\uDFAF', suffix: sep + 'Practice.html' },
        { key: 'Quiz',     label: 'Quiz',     icon: '\u2714',        suffix: sep + 'Quiz.html' }
      ];
      var tbStepOrder = { Video: 0, Summary: 1, Practice: 2, Quiz: 3 };
      var curType = '';
      if (filename.indexOf('Video') !== -1) curType = 'Video';
      else if (filename.indexOf('Summary') !== -1) curType = 'Summary';
      else if (filename.indexOf('Practice') !== -1) curType = 'Practice';
      else if (filename.indexOf('Quiz') !== -1) curType = 'Quiz';
      var curIdx = tbStepOrder[curType] || 0;

      lessonNavHtml = '<div class="taskbar-center" role="navigation" aria-label="Lesson steps">' +
        '<div class="tb-progress-bar">';
      for (var si = 0; si < tbSteps.length; si++) {
        var s = tbSteps[si];
        var state = si < curIdx ? 'completed' : si === curIdx ? 'current' : 'upcoming';
        var stepUrl = lessonBase + s.suffix;
        lessonNavHtml += '<div class="tb-lp-step tb-lp-' + state + '"' + (state === 'current' ? ' aria-current="step"' : '') + '>';
        if (si > 0) {
          lessonNavHtml += '<div class="tb-lp-connector tb-lp-connector-' + (si <= curIdx ? 'done' : 'pending') + '"></div>';
        }
        if (si !== curIdx) {
          lessonNavHtml += '<a href="' + stepUrl + '" class="tb-lp-dot-link" aria-label="' + s.label + '">';
        }
        lessonNavHtml += '<div class="tb-lp-dot">' + s.icon + '</div>';
        lessonNavHtml += '<span class="tb-lp-label">' + s.label + '</span>';
        if (si !== curIdx) {
          lessonNavHtml += '</a>';
        }
        lessonNavHtml += '</div>';
      }
      lessonNavHtml += '</div></div>';
    }
  }

    nav.innerHTML =
      '<a class="skip-to-content" href="#main-content">Skip to content</a>' +
      '<div class="taskbar-container">' +
        // Dev Tools
        '<button id="dev-icon-toggle" style="position:absolute; left:0; top:0; z-index:var(--z-hamburger); background:none; border:none; color:rgba(255,255,255,0.3); font-size:1.2rem; cursor:pointer; padding:0.5rem;" title="Dev Tools" aria-label="Developer tools">🛠️</button>' +

        // LEFT: Primary Navigation
        '<div class="taskbar-left" role="group" aria-label="Site navigation">' +
          backBtnHtml +
          '<a class="taskbar-button" href="/index.html" id="homepage-button"'+getDisp('homepage')+' aria-label="Home">\uD83C\uDFE0 Home</a>' +
          '<a class="taskbar-button" href="/ArisEdu Project Folder/Dashboard.html" id="dashboard-button"'+getDisp('dashboard')+' aria-label="Dashboard">\uD83D\uDCCA Dashboard</a>' +
          '<a class="taskbar-button" href="/ArisEdu Project Folder/Courses.html" id="course-button"'+getDisp('courses')+' aria-label="Courses">\uD83D\uDCDA Courses</a>' +
        '</div>' +

        // CENTER: Lesson navigation (only on lesson pages)
        lessonNavHtml +

        // RIGHT: Utilities + More menu
        '<div class="taskbar-right" role="group" aria-label="Tools and settings">' +
          '<button class="taskbar-button" id="search-button"'+getDisp('search')+' aria-label="Search">\uD83D\uDD0D Search</button>' +
          '<button class="taskbar-button" id="ai-assistant-button"'+getDisp('ai')+' aria-label="AI Assistant">\uD83E\uDD16 AI</button>' +
          '<button class="taskbar-button" id="streak-button" title="Current Login Streak" style="display:none; color: #fbbf24;" aria-label="Login streak">🔥 0</button>' +

          // "More" overflow menu
          '<div class="taskbar-more-wrap">' +
            '<button class="taskbar-more-btn" id="more-menu-btn" title="More" aria-haspopup="true" aria-expanded="false">\u22EF More</button>' +
            '<div class="taskbar-more-panel" id="more-menu-panel" role="menu" aria-label="More options">' +
              '<a class="more-item" href="/ArisEdu Project Folder/TeacherAnalytics.html" role="menuitem">📊 Teacher Analytics</a>' +
              '<a class="more-item" href="/ArisEdu Project Folder/arcade.html"'+getDisp('arcade')+' role="menuitem">\uD83D\uDC7E Arcade</a>' +
              '<button class="more-item" id="more-forums-btn"'+getDisp('forums')+' role="menuitem">\uD83D\uDCAC Forums</button>' +
              '<button class="more-item" id="more-update-btn" role="menuitem">\uD83D\uDD14 Updates</button>' +
            '</div>' +
          '</div>' +

          '<button class="taskbar-button taskbar-icon-btn" id="settings-button" aria-haspopup="true" aria-expanded="false" aria-label="Settings"><span class="tb-icon">\u2699\uFE0F</span><span class="tb-label">Settings</span></button>' +
          '<a class="taskbar-button taskbar-icon-btn" href="/ArisEdu Project Folder/Login.html" id="login-signup-button"'+getDisp('login')+' aria-label="Login or sign up"><span class="tb-icon">\uD83D\uDD10</span><span class="tb-label">Login</span></a>' +
          '<button id="language-toggle-button" class="taskbar-button taskbar-icon-btn" title="Switch Language" style="background:none;border:none;color:rgba(255,255,255,0.85);cursor:pointer;" aria-haspopup="true" aria-expanded="false" aria-label="Switch language"><span class="tb-icon">🌍</span><span class="tb-label">Lang</span></button>' +
        '</div>' +

        // Hamburger for mobile
        '<button class="hamburger-btn" id="hamburger-btn" aria-label="Open menu" aria-expanded="false">&#9776;</button>' +
      '</div>' +
      bcHtml +
      langDropdownHtml +
      settingsMenuHtml;

    document.body.insertBefore(nav, document.body.firstChild);

    // Add skip-to-content target on main content area
    var mainEl = document.querySelector('.main-container');
    if (mainEl && !mainEl.id) mainEl.id = 'main-content';

    // Inject mobile drawer (outside the nav, appended to body)
    var drawerContainer = document.createElement('div');
    drawerContainer.innerHTML = mobileDrawerHtml;
    while (drawerContainer.firstChild) {
      document.body.appendChild(drawerContainer.firstChild);
    }

    // ========== MORE MENU LOGIC ==========
    var moreBtn = document.getElementById('more-menu-btn');
    var morePanel = document.getElementById('more-menu-panel');
    function closeMoreMenu() {
      if (morePanel) morePanel.classList.remove('is-open');
      if (moreBtn) moreBtn.setAttribute('aria-expanded', 'false');
    }
    function openMoreMenu() {
      if (!morePanel || !moreBtn) return;
      morePanel.classList.add('is-open');
      moreBtn.setAttribute('aria-expanded', 'true');
      var rect = moreBtn.getBoundingClientRect();
      morePanel.style.top = rect.bottom + 4 + 'px';
      morePanel.style.left = Math.max(0, rect.right - morePanel.offsetWidth) + 'px';
      // Focus first item
      var firstItem = morePanel.querySelector('.more-item');
      if (firstItem) firstItem.focus();
    }
    if (moreBtn && morePanel) {
      moreBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        morePanel.classList.contains('is-open') ? closeMoreMenu() : openMoreMenu();
      });
      // Arrow keys and Escape within More menu
      morePanel.addEventListener('keydown', function(e) {
        var items = morePanel.querySelectorAll('.more-item');
        var idx = Array.prototype.indexOf.call(items, document.activeElement);
        if (e.key === 'ArrowDown') { e.preventDefault(); if (idx < items.length - 1) items[idx + 1].focus(); }
        else if (e.key === 'ArrowUp') { e.preventDefault(); if (idx > 0) items[idx - 1].focus(); }
        else if (e.key === 'Escape') { closeMoreMenu(); moreBtn.focus(); }
      });
      document.addEventListener('click', function(e) {
        if (!morePanel.contains(e.target) && e.target !== moreBtn) {
          closeMoreMenu();
        }
      });
      // Wire up More menu buttons
      var moreForumsBtn = document.getElementById('more-forums-btn');
      if (moreForumsBtn) moreForumsBtn.addEventListener('click', function(){ window.location.href = '/ArisEdu Project Folder/forums.html'; });
      var moreUpdateBtn = document.getElementById('more-update-btn');
      if (moreUpdateBtn) moreUpdateBtn.addEventListener('click', function(){ if(window.showArisEduUpdate) window.showArisEduUpdate(); });
      
      // Hide Teacher Analytics button for non-teachers
      (async function() {
        try {
          // Wait for Firebase to be available
          let attempts = 0;
          while ((!window.db || !window.auth) && attempts < 20) {
            await new Promise(r => setTimeout(r, 100));
            attempts++;
          }
          
          if (window.auth && window.auth.currentUser) {
            const { getDoc, doc } = await import('../firebase-config.js');
            const userRef = doc(window.db, 'users', window.auth.currentUser.uid);
            const userSnap = await getDoc(userRef);
            
            if (!userSnap.exists() || userSnap.data().role !== 'teacher') {
              // Hide Teacher Analytics button for students
              const teacherAnalyticsLink = document.querySelector('a[href*="TeacherAnalytics"]');
              if (teacherAnalyticsLink) {
                teacherAnalyticsLink.style.display = 'none';
              }
            }
          }
        } catch (error) {
          // If error, hide the button to be safe (don't expose teacher tools)
          const teacherAnalyticsLink = document.querySelector('a[href*="TeacherAnalytics"]');
          if (teacherAnalyticsLink) {
            teacherAnalyticsLink.style.display = 'none';
          }
        }
      })();
    }

    // ========== HAMBURGER DRAWER LOGIC ==========
    var hamburgerBtn = document.getElementById('hamburger-btn');
    var drawerOverlay = document.getElementById('mobile-drawer-overlay');
    var drawer = document.getElementById('mobile-drawer');
    var drawerClose = document.getElementById('mobile-drawer-close');

    function openDrawer() {
      if (drawerOverlay) drawerOverlay.classList.add('is-open');
      if (drawer) drawer.classList.add('is-open');
      if (hamburgerBtn) hamburgerBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      // Focus first focusable element in drawer
      if (drawerClose) drawerClose.focus();
    }
    function closeDrawer() {
      if (drawerOverlay) drawerOverlay.classList.remove('is-open');
      if (drawer) drawer.classList.remove('is-open');
      if (hamburgerBtn) hamburgerBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
      if (hamburgerBtn) hamburgerBtn.focus();
    }
    // Focus trap inside drawer when open
    if (drawer) {
      drawer.addEventListener('keydown', function(e) {
        if (e.key !== 'Tab') return;
        var focusable = drawer.querySelectorAll('a[href], button, input, [tabindex]:not([tabindex="-1"])');
        if (!focusable.length) return;
        var first = focusable[0], last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      });
    }

    if (hamburgerBtn) hamburgerBtn.addEventListener('click', openDrawer);
    if (drawerOverlay) drawerOverlay.addEventListener('click', closeDrawer);
    if (drawerClose) drawerClose.addEventListener('click', closeDrawer);

    // Wire up drawer buttons
    var drawerForums = document.getElementById('drawer-forums-btn');
    if (drawerForums) drawerForums.addEventListener('click', function(){ closeDrawer(); window.location.href = '/ArisEdu Project Folder/forums.html'; });
    var drawerSearch = document.getElementById('drawer-search-btn');
    if (drawerSearch) drawerSearch.addEventListener('click', function(){ closeDrawer(); var sb = document.getElementById('search-button'); if(sb) sb.click(); });
    var drawerAI = document.getElementById('drawer-ai-btn');
    if (drawerAI) drawerAI.addEventListener('click', function(){ closeDrawer(); var ab = document.getElementById('ai-assistant-button'); if(ab) ab.click(); });
    var drawerUpdate = document.getElementById('drawer-update-btn');
    if (drawerUpdate) drawerUpdate.addEventListener('click', function(){ closeDrawer(); if(window.showArisEduUpdate) window.showArisEduUpdate(); });
    var drawerSettings = document.getElementById('drawer-settings-btn');
    if (drawerSettings) drawerSettings.addEventListener('click', function(){ closeDrawer(); var sb = document.getElementById('settings-button'); if(sb) sb.click(); });
    var drawerLang = document.getElementById('drawer-lang-btn');
    if (drawerLang) drawerLang.addEventListener('click', function(){ closeDrawer(); var lb = document.getElementById('language-toggle-button'); if(lb) lb.click(); });

    // Close drawer & More menu on Escape
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeDrawer();
        closeMoreMenu();
      }
    });
  }

  // ========== LESSON PROGRESSION INDICATOR ==========
  // Shows a step bar (Video → Summary → Practice → Quiz) on lesson pages
  (function() {
    // Only show on lesson pages (inside a Lessons folder, not unit tests)
    if (!lessonFolder) return;
    var lessonMatch = filename.match(/Lesson\s*(\w+\.\d+)/);
    if (!lessonMatch) return; // Skip unit tests and non-lesson pages

    var lessonId = lessonMatch[1]; // e.g. "3.1"
    var baseName = filename.replace(/_Video\.html|_Summary\.html|_Practice\.html|_Quiz\.html/, '');

    // Determine current step
    var currentStep = '';
    if (filename.indexOf('_Video') !== -1) currentStep = 'video';
    else if (filename.indexOf('_Summary') !== -1) currentStep = 'summary';
    else if (filename.indexOf('_Practice') !== -1) currentStep = 'practice';
    else if (filename.indexOf('_Quiz') !== -1) currentStep = 'quiz';
    if (!currentStep) return;

    var steps = [
      { key: 'video',    label: 'Video',    icon: '\u25B6', suffix: '_Video.html' },
      { key: 'summary',  label: 'Summary',  icon: '\uD83D\uDCCB', suffix: '_Summary.html' },
      { key: 'practice', label: 'Practice', icon: '\uD83C\uDFAF', suffix: '_Practice.html' },
      { key: 'quiz',     label: 'Quiz',     icon: '\u2714', suffix: '_Quiz.html' }
    ];

    var stepOrder = { video: 0, summary: 1, practice: 2, quiz: 3 };
    var currentIdx = stepOrder[currentStep];

    // Build the step bar HTML with ARIA progress indicators
    var progressHtml = '<div class="lesson-progress-bar" id="lesson-progress-bar" role="navigation" aria-label="Lesson steps">';
    for (var si = 0; si < steps.length; si++) {
      var s = steps[si];
      var state = 'upcoming';
      if (si < currentIdx) state = 'completed';
      else if (si === currentIdx) state = 'current';

      var stepUrl = baseName + s.suffix;
      var isClickable = (si !== currentIdx);

      var stepAriaLabel = s.label + ' — ' + (state === 'completed' ? 'completed' : state === 'current' ? 'current step' : 'upcoming');
      progressHtml += '<div class="lp-step lp-' + state + '"' + (state === 'current' ? ' aria-current="step"' : '') + '>';
      if (si > 0) {
        progressHtml += '<div class="lp-connector lp-connector-' + (si <= currentIdx ? 'done' : 'pending') + '"></div>';
      }
      if (isClickable) {
        progressHtml += '<a href="' + stepUrl + '" class="lp-dot-link" aria-label="' + stepAriaLabel + '">';
      }
      progressHtml += '<div class="lp-dot">' + s.icon + '</div>';
      progressHtml += '<span class="lp-label">' + s.label + '</span>';
      if (isClickable) {
        progressHtml += '</a>';
      }
      progressHtml += '</div>';
    }
    progressHtml += '</div>';

    // Inject into the main-container, at the very bottom
    function injectProgressBar() {
      var mainContainer = document.querySelector('.main-container');
      if (!mainContainer) return;
      if (document.getElementById('lesson-progress-bar')) return;
      var div = document.createElement('div');
      div.innerHTML = progressHtml;
      mainContainer.appendChild(div.firstChild);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', injectProgressBar);
    } else {
      injectProgressBar();
    }
  })();

  // ========== COURSE SIDEBAR NAVIGATION ==========
  // Auto-generates a collapsible sidebar on course homepage pages
  (function() {
    // Only show on course homepage pages
    var isCourseHomepage = path.indexOf('CourseHomepage') !== -1 && filename.endsWith('.html');
    if (!isCourseHomepage) return;

    function buildSidebar() {
      var mainContainer = document.querySelector('.main-container');
      if (!mainContainer || document.getElementById('course-sidebar')) return;

      // Parse all segment groups to extract units and lessons
      // Match standard, and bio.html's top/bottom patterns
      var segmentGroups = document.querySelectorAll('[id^="segments-unit-"], [id^="segments-top-unit-"], [id^="segments-bottom-unit-"]');
      if (!segmentGroups.length) return;

      // Determine the localStorage prefix for progress
      // AP courses expose courseConfig.coursePrefix; regular courses use filename stem
      var progressPrefix = '';
      if (typeof courseConfig !== 'undefined' && courseConfig && courseConfig.coursePrefix) {
        progressPrefix = courseConfig.coursePrefix;
      } else {
        progressPrefix = filename.replace('.html', '');
      }

      var unitMap = {}; // deduplicate units (bio.html has top + bottom for same unit)
      segmentGroups.forEach(function(group) {
        var unitId = group.id.replace('segments-unit-', '').replace('segments-top-unit-', '').replace('segments-bottom-unit-', '');
        if (!unitMap[unitId]) unitMap[unitId] = [];
        var lessons = unitMap[unitId];

        // Pattern 1: Regular courses — <a href> wrapping rect/path
        var links = group.querySelectorAll('a[href]');
        if (links.length > 0) {
          links.forEach(function(a) {
            var href = a.getAttribute('href') || '';
            var el = a.querySelector('rect, path');
            var nameMatch = (el ? el.getAttribute('onmouseenter') : '') || '';
            var labelMatch = nameMatch.match(/showLessonPopup\(event,\s*'([^']+)'/);
            var lessonName = labelMatch ? labelMatch[1] : 'Lesson';
            lessons.push({ href: href, name: lessonName });
          });
        } else {
          // Pattern 2: AP/dynamic courses — <g onclick> wrapping rect
          var gElements = group.querySelectorAll('g[onclick]');
          gElements.forEach(function(g) {
            var onclick = g.getAttribute('onclick') || '';
            var hrefMatch = onclick.match(/window\.location\.href='([^']+)'/);
            var href = hrefMatch ? hrefMatch[1] : '#';
            var rect = g.querySelector('rect');
            var nameAttr = (rect ? rect.getAttribute('onmouseenter') : '') || '';
            var labelMatch = nameAttr.match(/showLessonPopup\(event,\s*'([^']+)'/);
            var lessonName = labelMatch ? labelMatch[1] : 'Lesson';
            var isUnitTest = onclick.indexOf(', 99)') !== -1;
            if (!isUnitTest) {
              lessons.push({ href: href, name: lessonName });
            }
          });
        }
      });

      // Convert map to array
      var units = [];
      var unitIds = Object.keys(unitMap);
      // Sort unit IDs numerically where possible
      unitIds.sort(function(a, b) {
        var na = parseFloat(a), nb = parseFloat(b);
        if (!isNaN(na) && !isNaN(nb)) return na - nb;
        return a.localeCompare(b);
      });
      unitIds.forEach(function(id) {
        if (unitMap[id].length > 0) {
          units.push({ id: id, lessons: unitMap[id] });
        }
      });

      if (!units.length) return;

      // Build sidebar HTML
      var sidebarHtml = '<aside class="course-sidebar" id="course-sidebar" role="complementary" aria-label="Course units">';
      sidebarHtml += '<div class="cs-header">';
      sidebarHtml += '<span class="cs-title">Units</span>';
      sidebarHtml += '<button class="cs-collapse-btn" id="cs-collapse-btn" title="Collapse sidebar" aria-label="Collapse sidebar"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg></button>';
      sidebarHtml += '</div>';

      units.forEach(function(unit, idx) {
        var completedCount = 0;
        var totalLessons = unit.lessons.length;
        unit.lessons.forEach(function(lesson, li) {
          var completedKey = progressPrefix + '_u' + unit.id + '_l' + (li + 1) + '_completed';
          if (localStorage.getItem(completedKey) === 'true') completedCount++;
        });

        var isExpanded = idx === 0; // First unit expanded by default
        var allDone = completedCount === totalLessons;
        var unitProgressLabel = completedCount + ' of ' + totalLessons + ' lessons completed';
        sidebarHtml += '<div class="cs-unit' + (isExpanded ? ' is-expanded' : '') + '" data-unit="' + unit.id + '">';
        sidebarHtml += '<button class="cs-unit-header" aria-expanded="' + isExpanded + '">';
        sidebarHtml += '<span class="cs-unit-name">Unit ' + unit.id + '</span>';
        sidebarHtml += '<span class="cs-unit-progress' + (allDone ? ' cs-unit-done' : '') + '" aria-label="' + unitProgressLabel + '">' + completedCount + '/' + totalLessons + (allDone ? ' \u2713' : '') + '</span>';
        sidebarHtml += '<span class="cs-chevron"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg></span>';
        sidebarHtml += '</button>';
        sidebarHtml += '<div class="cs-lessons"><div class="cs-lessons-inner">';

        unit.lessons.forEach(function(lesson, li) {
          var startedKey = progressPrefix + '_u' + unit.id + '_l' + (li + 1) + '_started';
          var completedKey = progressPrefix + '_u' + unit.id + '_l' + (li + 1) + '_completed';
          var isCompleted = localStorage.getItem(completedKey) === 'true';
          var isStarted = localStorage.getItem(startedKey) === 'true';
          var statusClass = isCompleted ? 'cs-completed' : (isStarted ? 'cs-started' : '');
          var statusIcon = isCompleted ? '\u2713 ' : (isStarted ? '\u25CB ' : '');
          var statusLabel = isCompleted ? ' (completed)' : (isStarted ? ' (in progress)' : '');

          sidebarHtml += '<a class="cs-lesson ' + statusClass + '" href="' + lesson.href + '" aria-label="' + lesson.name + statusLabel + '">';
          sidebarHtml += '<span class="cs-lesson-status" aria-hidden="true">' + statusIcon + '</span>';
          sidebarHtml += '<span class="cs-lesson-name">' + lesson.name + '</span>';
          sidebarHtml += '</a>';
        });

        sidebarHtml += '</div></div></div>';
      });

      sidebarHtml += '</aside>';

      // Find the courses-container and wrap it + sidebar in a flex row
      var coursesContainer = mainContainer.querySelector('.courses-container') || mainContainer.querySelector('#courses-container');
      var sidebarTmp = document.createElement('div');
      sidebarTmp.innerHTML = sidebarHtml;
      var sidebarNode = sidebarTmp.firstChild;

      if (coursesContainer) {
        // Create a flex wrapper around sidebar + courses-container
        var flexWrapper = document.createElement('div');
        flexWrapper.className = 'cs-layout-wrapper';
        flexWrapper.style.display = 'flex';
        flexWrapper.style.gap = '0';
        flexWrapper.style.alignItems = 'flex-start';
        flexWrapper.style.width = '100%';
        // Insert wrapper where courses-container was
        coursesContainer.parentNode.insertBefore(flexWrapper, coursesContainer);
        flexWrapper.appendChild(sidebarNode);
        flexWrapper.appendChild(coursesContainer);
        // Make courses-container fill remaining space
        coursesContainer.style.flex = '1';
        coursesContainer.style.minWidth = '0';
      } else {
        // Fallback: prepend sidebar to main-container
        mainContainer.insertBefore(sidebarNode, mainContainer.firstChild);
        mainContainer.style.display = 'flex';
        mainContainer.style.gap = '0';
        mainContainer.style.alignItems = 'flex-start';
      }

      // Sidebar toggle logic
      var sidebarEl = document.getElementById('course-sidebar');
      var collapseBtn = document.getElementById('cs-collapse-btn');

      if (collapseBtn && sidebarEl) {
        collapseBtn.addEventListener('click', function() {
          sidebarEl.classList.toggle('is-collapsed');
          var isCollapsed = sidebarEl.classList.contains('is-collapsed');
          collapseBtn.setAttribute('aria-label', isCollapsed ? 'Expand sidebar' : 'Collapse sidebar');
          var svg = collapseBtn.querySelector('svg');
          if (svg) {
            svg.style.transform = isCollapsed ? 'rotate(180deg)' : '';
          }
        });
      }

      // Unit expand/collapse with aria-expanded
      var unitHeaders = sidebarEl.querySelectorAll('.cs-unit-header');
      unitHeaders.forEach(function(header) {
        header.addEventListener('click', function() {
          var unitDiv = header.closest('.cs-unit');
          if (unitDiv) {
            unitDiv.classList.toggle('is-expanded');
            header.setAttribute('aria-expanded', unitDiv.classList.contains('is-expanded'));
          }
        });
      });

      // Scroll to current unit if possible (highlight the unit matching the page scroll)
      // On click, also trigger the corresponding markLessonStarted if available

      // Mobile sidebar toggle button (appears at 768px and below)
      var mobileToggle = document.createElement('button');
      mobileToggle.className = 'cs-mobile-toggle';
      mobileToggle.innerHTML = '\u2630 Units';
      mobileToggle.title = 'Toggle unit sidebar';
      mobileToggle.setAttribute('aria-label', 'Toggle unit sidebar');
      mainContainer.appendChild(mobileToggle);

      var sidebarOverlay = document.createElement('div');
      sidebarOverlay.className = 'cs-mobile-overlay';
      mainContainer.appendChild(sidebarOverlay);

      function openMobileSidebar() {
        sidebarEl.classList.add('is-mobile-open');
        sidebarOverlay.classList.add('is-open');
      }
      function closeMobileSidebar() {
        sidebarEl.classList.remove('is-mobile-open');
        sidebarOverlay.classList.remove('is-open');
      }

      mobileToggle.addEventListener('click', openMobileSidebar);
      sidebarOverlay.addEventListener('click', closeMobileSidebar);
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        // Delay slightly to let dynamic course scripts populate the grid
        setTimeout(buildSidebar, 150);
      });
    } else {
      // Small delay to ensure course page scripts have run
      setTimeout(buildSidebar, 150);
    }
  })();

  // --- Translate Taskbar Buttons ---
  (function() {
    function translateTaskbarButtons() {
      var lang = null;
      try { lang = localStorage.getItem('arisEduLanguage'); } catch(e) {}
      
      if (!lang || lang === 'english') return; // No translation needed for English
      
      // Get translation dictionary based on language
      var dict = {};
      if (window.globalTranslations && (lang === 'chinese' || lang === 'traditional')) {
        dict = window.globalTranslations;
      } else if (window.spanishTranslations && lang === 'spanish') {
        dict = window.spanishTranslations;
      } else if (window.hindiTranslations && lang === 'hindi') {
        dict = window.hindiTranslations;
      }
      
      if (!dict || Object.keys(dict).length === 0) {
        setTimeout(translateTaskbarButtons, 100); // Retry if translations not loaded
        return;
      }
      
      // Translation mapping
      var buttonTranslations = {
        'Home': dict['Home'],
        'Homepage': dict['Home'],
        'Dashboard': dict['Dashboard'],
        'Courses': dict['Courses'],
        'Arcade': dict['Arcade'],
        'Forums': dict['Forums'],
        'Search': dict['Search'],
        'AI': dict['AI'],
        'Settings': dict['Settings'],
        'Login': dict['Login'],
        'Login/Signup': dict['Login'],
        'Dark Mode': dict['Dark Mode'],
        'Preferences': dict['Preferences'],
        'Help': dict['Help']
      };
      
      // Translate taskbar buttons
      var buttons = document.querySelectorAll('.taskbar-button, .settings-item');
      buttons.forEach(function(btn) {
        var fullText = btn.textContent || btn.innerText || '';
        
        // Try each English text to find and replace it
        for (var enText in buttonTranslations) {
          if (buttonTranslations[enText] && fullText.indexOf(enText) !== -1) {
            // Replace the English text with the translated version
            var newText = fullText.replace(enText, buttonTranslations[enText]);
            btn.textContent = newText;
            break;
          }
        }
      });
    }
    
    // Translate when page loads (with delay to ensure all translations loaded)
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        setTimeout(translateTaskbarButtons, 300);
      });
    } else {
      setTimeout(translateTaskbarButtons, 300);
    }
    
    // Also translate when language changes
    window.addEventListener('languageChanged', function() {
      setTimeout(translateTaskbarButtons, 100);
    });
  })();

  // --- Audio Toggle Handler Removed ---


  // --- Language Toggle (Globe Icon) with Dropdown ---
  (function() {
    var langBtn = document.getElementById('language-toggle-button');
    var dropdown = document.getElementById('language-dropdown');
    if (!langBtn || !dropdown) return;

    // Highlight current language
    function updateHighlight() {
      var current = localStorage.getItem('arisEduLanguage') || 'english';
      var opts = dropdown.querySelectorAll('.lang-option');
      for (var i = 0; i < opts.length; i++) {
        opts[i].style.background = opts[i].getAttribute('data-lang') === current
          ? 'rgba(102,126,234,0.35)' : 'none';
      }
    }

    // Toggle dropdown
    langBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      var open = dropdown.style.display !== 'none';
      dropdown.style.display = open ? 'none' : 'block';
      if (!open) {
        var rect = langBtn.getBoundingClientRect();
        dropdown.style.top = rect.bottom + 4 + 'px';
        dropdown.style.left = '';
        dropdown.style.right = (window.innerWidth - rect.right) + 'px';
        updateHighlight();
      }
    });

    // Hover effect on options
    dropdown.addEventListener('mouseover', function(e) {
      if (e.target.classList.contains('lang-option')) e.target.style.background = 'rgba(102,126,234,0.25)';
    });
    dropdown.addEventListener('mouseout', function(e) {
      if (e.target.classList.contains('lang-option')) {
        var current = localStorage.getItem('arisEduLanguage') || 'english';
        e.target.style.background = e.target.getAttribute('data-lang') === current ? 'rgba(102,126,234,0.35)' : 'none';
      }
    });

    // Language selection
    dropdown.addEventListener('click', function(e) {
      var btn = e.target.closest('.lang-option');
      if (!btn) return;
      var lang = btn.getAttribute('data-lang');
      localStorage.setItem('arisEduLanguage', lang);
      dropdown.style.display = 'none';
      if (lang === 'english') {
        location.reload();
      } else if (window.applyTranslations) {
        window.applyTranslations();
        updateHighlight();
        // Dispatch custom event for taskbar translation
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
      } else {
        location.reload();
      }
    });

    // Close dropdown when clicking elsewhere
    document.addEventListener('click', function(e) {
      if (!langBtn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.style.display = 'none';
      }
    });
  })();

    // Bind Dev Tools Button Logic
    document.addEventListener('click', function(e) {
        if(e.target && e.target.id === 'dev-icon-toggle') {
             // Dispatch a custom event or check if dev_tools.js has exposed a toggle function
             
             var panel = document.getElementById('dev-tools-panel');
             if(panel) {
                 panel.style.display = (panel.style.display === 'none' || panel.style.display === '') ? 'block' : 'none';
             } else {
                 // Force override
                 window._isDevUser = function() { return true; };
                 var script = document.createElement('script');
                 script.src = '/ArisEdu Project Folder/scripts/dev_tools.js?v=' + Date.now();
                 document.body.appendChild(script);
             }
        }
    });

  // --- Back button ---
  var backBtn = document.getElementById('back-button');
  if (backBtn) {
    backBtn.addEventListener('click', function () {
      window.location.href = backUrl;
    });
  }

  // --- Settings toggle ---
  var settingsBtn = document.getElementById('settings-button');
  if (settingsBtn) {
    settingsBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var menu = document.getElementById('settings-menu');
      if (!menu) return;
      var isHidden = menu.getAttribute('aria-hidden') === 'true';
      menu.setAttribute('aria-hidden', String(!isHidden));
      settingsBtn.setAttribute('aria-expanded', String(isHidden));
      if (isHidden) {
        var rect = settingsBtn.getBoundingClientRect();
        menu.style.top = rect.bottom + 4 + 'px';
        menu.style.left = rect.left + 'px';
        menu.style.visibility = 'visible';
        menu.style.opacity = '1';
        menu.style.transform = 'translateY(0)';
      } else {
        menu.style.visibility = 'hidden';
        menu.style.opacity = '0';
        menu.style.transform = 'translateY(-6px)';
      }
    });

    // Close settings menu when clicking outside
    document.addEventListener('click', function (e) {
      var menu = document.getElementById('settings-menu');
      if (!menu) return;
      if (!menu.contains(e.target) && e.target !== settingsBtn) {
        menu.setAttribute('aria-hidden', 'true');
        settingsBtn.setAttribute('aria-expanded', 'false');
        menu.style.visibility = 'hidden';
        menu.style.opacity = '0';
        menu.style.transform = 'translateY(-6px)';
      }
    });
  }

  // --- Dark mode sync ---
  var checkbox = document.getElementById('dark-mode-checkbox');
  if (checkbox) {
    var stored = localStorage.getItem('arisEduDarkMode');
    var prefersDark = stored === null ? true : stored === 'true';
    if (prefersDark) {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
    checkbox.checked = prefersDark;
    checkbox.addEventListener('change', function (event) {
      var isDark = event.target.checked;
      localStorage.setItem('arisEduDarkMode', String(isDark));
      if (isDark) {
        document.body.classList.add('dark-mode');
      } else {
        document.body.classList.remove('dark-mode');
      }
      if (window.applyArisTheme) { window.applyArisTheme(); }
    });
  }

  // --- Settings menu: move to body so it's not clipped by taskbar overflow ---
  (function () {
    var sMenu = document.getElementById('settings-menu');
    if (sMenu && sMenu.parentElement) {
      document.body.appendChild(sMenu);
    }
  })();

  // --- Language dropdown: move to body so it's not clipped by taskbar overflow ---
  (function () {
    var langDrop = document.getElementById('language-dropdown');
    if (langDrop && langDrop.parentElement) {
      document.body.appendChild(langDrop);
    }
  })();

  // --- Login / Signup account display ---
  (function () {
    var loginButton = document.getElementById('login-signup-button');
    if (!loginButton) return;
    var storedUser = localStorage.getItem('user');
    if (!storedUser) return;
    var user;
    try { user = JSON.parse(storedUser); } catch (e) { return; }
    var name = user && (user.name || user.email);
    if (!name) return;

    loginButton.textContent = '\uD83D\uDC64 ' + name;
    loginButton.removeAttribute('href');
    loginButton.setAttribute('aria-haspopup', 'true');
    loginButton.setAttribute('aria-expanded', 'false');

    var isDarkMode = document.body.classList.contains('dark-mode');
    var menu = document.createElement('div');
    menu.className = 'account-menu';
    menu.setAttribute('role', 'menu');
    menu.setAttribute('aria-hidden', 'true');
    menu.style.position = 'fixed';
    menu.style.minWidth = '160px';
    menu.style.borderRadius = '0.5rem';
    menu.style.padding = '0.4rem';
    menu.style.display = 'none';
    menu.style.zIndex = '10000';

    // Theme-aware styling function for account menu
    function updateAccountMenuTheme() {
      var dark = document.body.classList.contains('dark-mode');
      menu.style.background = dark ? '#0f172a' : 'white';
      menu.style.border = dark ? '1px solid #1f2937' : '1px solid #e2e8f0';
      menu.style.boxShadow = dark
        ? '0 12px 24px rgba(2, 6, 23, 0.6)'
        : '0 10px 20px rgba(2, 6, 23, 0.15)';
      // Update child items
      var items = menu.querySelectorAll('[role="menuitem"]');
      items.forEach(function(item) {
        item.style.color = dark ? '#e2e8f0' : '#0f172a';
      });
    }
    updateAccountMenuTheme();

    // Listen for dark mode changes
    var observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(m) {
        if (m.attributeName === 'class') updateAccountMenuTheme();
      });
    });
    observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });

    var logoutButton = document.createElement('button');
    logoutButton.type = 'button';
    logoutButton.textContent = 'Log out';
    logoutButton.setAttribute('role', 'menuitem');
    logoutButton.style.width = '100%';
    logoutButton.style.background = 'transparent';
    logoutButton.style.border = 'none';
    logoutButton.style.textAlign = 'left';
    logoutButton.style.padding = '0.5rem 0.75rem';
    logoutButton.style.borderRadius = '0.4rem';
    logoutButton.style.cursor = 'pointer';
    logoutButton.style.fontWeight = '600';
    logoutButton.style.color = isDarkMode ? '#e2e8f0' : '#0f172a';

    logoutButton.addEventListener('mouseenter', function () {
      var dark = document.body.classList.contains('dark-mode');
      logoutButton.style.background = dark
        ? 'rgba(148, 163, 184, 0.2)'
        : 'rgba(15, 23, 42, 0.08)';
    });
    logoutButton.addEventListener('mouseleave', function () {
      logoutButton.style.background = 'transparent';
    });

    logoutButton.addEventListener('click', function (event) {
      event.preventDefault();
      localStorage.removeItem('user');
      menu.style.display = 'none';
      loginButton.setAttribute('aria-expanded', 'false');

      // Sign out from Firebase auth to fully clear session
      import('/ArisEdu Project Folder/firebase-config.js').then(function(mod) {
        if (mod.auth && mod.signOut) {
          return mod.signOut(mod.auth);
        }
      }).catch(function(e) {
        console.error('Firebase signOut error:', e);
      }).finally(function() {
        window.location.href = '/ArisEdu Project Folder/Login.html';
      });
    });

    // Account Information link
    var accountInfoLink = document.createElement('a');
    accountInfoLink.href = '/ArisEdu Project Folder/AccountInfo.html';
    accountInfoLink.textContent = 'Account Information';
    accountInfoLink.setAttribute('role', 'menuitem');
    accountInfoLink.style.display = 'block';
    accountInfoLink.style.width = '100%';
    accountInfoLink.style.background = 'transparent';
    accountInfoLink.style.border = 'none';
    accountInfoLink.style.textAlign = 'left';
    accountInfoLink.style.padding = '0.5rem 0.75rem';
    accountInfoLink.style.borderRadius = '0.4rem';
    accountInfoLink.style.cursor = 'pointer';
    accountInfoLink.style.fontWeight = '600';
    accountInfoLink.style.color = isDarkMode ? '#e2e8f0' : '#0f172a';
    accountInfoLink.style.textDecoration = 'none';
    accountInfoLink.style.boxSizing = 'border-box';

    accountInfoLink.addEventListener('mouseenter', function () {
      var dark = document.body.classList.contains('dark-mode');
      accountInfoLink.style.background = dark
        ? 'rgba(148, 163, 184, 0.2)'
        : 'rgba(15, 23, 42, 0.08)';
    });
    accountInfoLink.addEventListener('mouseleave', function () {
      accountInfoLink.style.background = 'transparent';
    });

    menu.appendChild(accountInfoLink);
    menu.appendChild(logoutButton);

    // Append to body so it's not clipped by taskbar overflow
    document.body.appendChild(menu);

    function closeMenu() {
      menu.style.display = 'none';
      loginButton.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-hidden', 'true');
    }

    function toggleMenu(event) {
      event.preventDefault();
      event.stopPropagation();
      var isOpen = menu.style.display === 'block';
      if (isOpen) {
        closeMenu();
      } else {
        var rect = loginButton.getBoundingClientRect();
        menu.style.top = rect.bottom + 4 + 'px';
        menu.style.left = rect.left + 'px';
        menu.style.display = 'block';
        menu.setAttribute('aria-hidden', 'false');
        loginButton.setAttribute('aria-expanded', 'true');
      }
    }

    loginButton.addEventListener('click', toggleMenu);

    document.addEventListener('click', function (event) {
      if (!menu.contains(event.target) && event.target !== loginButton) {
        closeMenu();
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        closeMenu();
      }
    });
  })();

  // --- Time Tracking ---
  // Track time spent on lesson pages and save to localStorage
  (function() {
    var path = decodeURIComponent(window.location.pathname);
    // Only track time on lesson pages (inside Lessons folders)
    if (path.indexOf('Lessons') === -1) return;
    
    var startTime = Date.now();
    var today = new Date().toISOString().slice(0, 10); // YYYY-MM-DD
    var storageKey = 'arisEdu_time_' + today;
    
    function saveTimeSpent() {
      var elapsed = Math.floor((Date.now() - startTime) / 1000 / 60); // minutes
      if (elapsed < 1) return; // Don't save if less than 1 minute
      
      var existing = parseInt(localStorage.getItem(storageKey)) || 0;
      localStorage.setItem(storageKey, existing + elapsed);
      startTime = Date.now(); // Reset for next interval
    }
    
    // Save on page unload
    window.addEventListener('beforeunload', saveTimeSpent);
    
    // Also save periodically (every 5 minutes) in case user doesn't close tab
    setInterval(saveTimeSpent, 5 * 60 * 1000);
    
    // Save on visibility change (tab switch)
    document.addEventListener('visibilitychange', function() {
      if (document.hidden) {
        saveTimeSpent();
      } else {
        startTime = Date.now(); // Reset when tab becomes visible again
      }
    });
  })();

  // --- Login Streak Logic ---
  (function() {
      // Use local date string to avoid timezone issues
      const date = new Date();
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      const today = `${year}-${month}-${day}`;
      
      const lastLogin = localStorage.getItem('arisEdu_last_login');
      let streak = parseInt(localStorage.getItem('arisEdu_streak') || '0');

      if (lastLogin !== today) {
          const yesterdayDate = new Date();
          yesterdayDate.setDate(yesterdayDate.getDate() - 1);
          const yYear = yesterdayDate.getFullYear();
          const yMonth = String(yesterdayDate.getMonth() + 1).padStart(2, '0');
          const yDay = String(yesterdayDate.getDate()).padStart(2, '0');
          const yesterdayStr = `${yYear}-${yMonth}-${yDay}`;

          if (lastLogin === yesterdayStr) {
              streak++; // Consecutive day
          } else {
              streak = 1; // Streak broken or new user
          }

          localStorage.setItem('arisEdu_last_login', today);
          localStorage.setItem('arisEdu_streak', streak);

          // Check streak badges
          if (window.BadgeSystem) {
              if (streak >= 3) window.BadgeSystem.award('streak_3');
              if (streak >= 7) window.BadgeSystem.award('streak_7');
              if (streak >= 30) window.BadgeSystem.award('streak_30');
          }
      }

      // Update Taskbar Button
      const streakBtn = document.getElementById('streak-button');
      if (streakBtn) {
          streakBtn.innerHTML = `🔥 ${streak}`;
          streakBtn.style.display = 'inline-block';
          
          // Enhanced Hover GUI (Tooltip)
          const tooltip = document.createElement('div');
          tooltip.id = 'streak-tooltip';
          const isDarkTooltip = document.body.classList.contains('dark-mode');
          tooltip.style.cssText = `
              position: absolute;
              top: 100%;
              left: 50%;
              transform: translateX(-50%);
              background: ${isDarkTooltip ? '#1e293b' : '#ffffff'};
              color: ${isDarkTooltip ? 'white' : '#0f172a'};
              padding: 0.5rem 1rem;
              border-radius: 0.5rem;
              font-size: 0.85rem;
              width: max-content;
              box-shadow: ${isDarkTooltip ? '0 4px 6px -1px rgba(0, 0, 0, 0.5)' : '0 4px 12px rgba(0, 0, 0, 0.15)'};
              z-index: 100;
              margin-top: 0.5rem;
              display: none;
              text-align: center;
              border: 1px solid ${isDarkTooltip ? '#334155' : '#e2e8f0'};
          `;
          tooltip.innerHTML = `
              <strong data-i18n="Current Streak">Current Streak</strong><br>
              ${streak} <span data-i18n="Day${streak === 1 ? '' : 's'}">Day${streak === 1 ? '' : 's'}</span> 🔥<br>
              <span style="font-size:0.75em; color:#9ca3af;" data-i18n="Come back tomorrow!">Come back tomorrow!</span>
          `;
          
          // Only append if not already there (though logic runs once)
          if (!streakBtn.querySelector('#streak-tooltip')) {
              streakBtn.style.position = 'relative'; // Ensure button is relative for absolute tooltip
              streakBtn.appendChild(tooltip);
              
              streakBtn.onmouseenter = () => tooltip.style.display = 'block';
              streakBtn.onmouseleave = () => tooltip.style.display = 'none';
          }
      }
  })();

  // --- Rewrite hardcoded "Back to [Subject]" buttons for middle school origin ---
  if (lessonFolder) {
    document.addEventListener('DOMContentLoaded', function() {
      var storedOrigin;
      try { storedOrigin = sessionStorage.getItem('courseOrigin_' + lessonFolder); } catch(e) {}
      if (!storedOrigin) return;

      // HS course filenames and their relative paths used in hardcoded buttons
      var hsFiles = ['chem.html', 'physics.html', 'bio.html', 'algebra1.html', 'algebra2.html', 'geometry.html'];

      var allClickables = document.querySelectorAll('button[onclick], a[onclick], a[href]');
      for (var i = 0; i < allClickables.length; i++) {
        var el = allClickables[i];
        var onclick = el.getAttribute('onclick') || '';
        var href = el.getAttribute('href') || '';

        for (var j = 0; j < hsFiles.length; j++) {
          var hsFile = hsFiles[j];
          var relPath = '../../' + hsFile;
          if (onclick.indexOf(relPath) !== -1) {
            el.setAttribute('onclick', onclick.replace(relPath, storedOrigin));
          }
          if (href.indexOf(relPath) !== -1) {
            el.setAttribute('href', href.replace(relPath, storedOrigin));
          }
        }
      }
    });
  }

  // End taskbar.js main IIFE
})();

// ========== MS ↔ HS Course Progress Sync ==========
// Ensures lesson progress is shared between middle school and high school course pages.
// Both versions link to the same lesson files; this syncs started/completed status bidirectionally.
(function() {
  document.addEventListener('DOMContentLoaded', function() {
    try {
      var pagePath = decodeURIComponent(window.location.pathname);
      var pageFile = pagePath.split('/').pop();

      // Course page pairings: MS prefix ↔ HS prefix
      var coursePairs = {
        'ms_chem.html':     { ms: 'ms_chem', hs: 'chem', folder: 'ChemistryLessons', isMS: true },
        'ms_bio.html':      { ms: 'ms_bio', hs: 'bio', folder: 'BiologyLessons', isMS: true },
        'ms_physics.html':  { ms: 'ms_phys', hs: 'physics', folder: 'PhysicsLessons', isMS: true },
        'ms_algebra1.html': { ms: 'ms_alg1', hs: 'alg1', folder: 'Algebra1Lessons', isMS: true },

        'ms_geometry.html': { ms: 'ms_geom', hs: 'geometry', folder: 'GeometryLessons', isMS: true },
        'chem.html':        { ms: 'ms_chem', hs: 'chem', folder: 'ChemistryLessons', isMS: false },
        'bio.html':         { ms: 'ms_bio', hs: 'bio', folder: 'BiologyLessons', isMS: false },
        'physics.html':     { ms: 'ms_phys', hs: 'physics', folder: 'PhysicsLessons', isMS: false },
        'algebra1.html':    { ms: 'ms_alg1', hs: 'alg1', folder: 'Algebra1Lessons', isMS: false },
        'algebra2.html':    { ms: 'ms_alg2', hs: 'alg2', folder: 'Algebra2Lessons', isMS: false },
        'geometry.html':    { ms: 'ms_geom', hs: 'geometry', folder: 'GeometryLessons', isMS: false }
      };

      var cfg = coursePairs[pageFile];
      if (!cfg) return;

      // HS unit test indices: the lesson index of the test item on the HS page for each unit
      var hsTestIdx = {
        'ChemistryLessons': {'1':9,'2':6,'3':9,'4':10,'5A':9,'5B':6,'6':8,'7':9,'8':10,'9':9,'10':11,'11':7,'12':6},
        'PhysicsLessons':   {'1':7,'2':7,'3':9,'4':7,'5':7,'6':7,'7':9,'8':7,'9':7,'10':10,'11':7},
        'BiologyLessons':   {'1':8,'2':8,'3':6,'4':7,'5':7,'6':7,'7':7,'8':6,'9':6,'10':7,'11':7,'12':7},
        'Algebra1Lessons':  {'1':8,'2':10,'3':8,'4':9,'5':11,'6':7,'7':9,'8':5,'9':5,'10':5,'11':4,'12':5},
        'Algebra2Lessons':  {'1':10,'2':8,'3':8,'4':7,'5':8,'6':6,'7':8,'8':7,'9':5},
        'GeometryLessons':  {'1':8,'2':10,'3':8,'4':9,'5':7,'6':8,'7':9,'8':9,'9':8,'10':10,'11':7,'12':10,'13':8}
      };
      var tMap = hsTestIdx[cfg.folder] || {};

      // Scan all lesson links to build local→HS index mapping
      var allLinks = document.querySelectorAll('a[onclick*="markLessonStarted"]');
      var localToHs = {}; // "localUnit_localIdx" → { hsU, hsL }

      allLinks.forEach(function(a) {
        var oc = a.getAttribute('onclick') || '';
        var m = oc.match(/markLessonStarted\(\s*'([^']+)'\s*,\s*(\d+)\s*\)/);
        if (!m) return;
        var lU = m[1], lI = m[2];
        var href = decodeURIComponent(a.getAttribute('href') || '');

        var hsU, hsL;
        // Regular lesson: "Lesson3.5_Video.html" or "Lesson 3.5_Video.html" or "Lesson 5A.2_Video.html"
        var lm = href.match(/Lesson\s*(\w+)\.(\d+)/);
        // Unit test: "Unit3_Test_Practice.html"
        var tm = href.match(/Unit(\w+)_Test/);

        if (lm) { hsU = lm[1]; hsL = lm[2]; }
        else if (tm) { hsU = tm[1]; hsL = tMap[tm[1]]; }

        if (hsU && hsL) {
          localToHs[lU + '_' + lI] = { hsU: String(hsU), hsL: String(hsL) };
        }
      });

      // MS pages: store reverse map (HS→MS) so HS pages can use it later
      if (cfg.isMS) {
        var reverseMap = {};
        for (var k in localToHs) {
          var v = localToHs[k];
          reverseMap[v.hsU + '_' + v.hsL] = k;
        }
        try { localStorage.setItem('_msMap_' + cfg.folder, JSON.stringify(reverseMap)); } catch(e) {}
      }

      // Helper: one-way sync HS → MS (completing HS also completes MS, but NOT vice-versa)
      function syncPair(msBase, hsBase) {
        ['_started', '_completed'].forEach(function(suf) {
          var mk = msBase + suf, hk = hsBase + suf;
          if (localStorage.getItem(hk) === 'true' && localStorage.getItem(mk) !== 'true')
            localStorage.setItem(mk, 'true');
        });
      }

      // === Sync existing progress on page load ===
      if (cfg.isMS) {
        // MS page: sync each local entry with its HS counterpart
        for (var key in localToHs) {
          var parts = key.split('_');
          var msU = parts[0], msI = parts.slice(1).join('_'); // Handle units like "5A"
          var hs = localToHs[key];
          syncPair(
            cfg.ms + '_u' + msU + '_l' + msI,
            cfg.hs + '_u' + hs.hsU + '_l' + hs.hsL
          );
        }
      } else {
        // HS page: load MS reverse map (stored when MS page was visited)
        var msMap = {};
        try { msMap = JSON.parse(localStorage.getItem('_msMap_' + cfg.folder) || '{}'); } catch(e) {}

        allLinks.forEach(function(a) {
          var oc = a.getAttribute('onclick') || '';
          var m = oc.match(/markLessonStarted\(\s*'([^']+)'\s*,\s*(\d+)\s*\)/);
          if (!m) return;
          var hsU = m[1], hsI = m[2];
          var msEntry = msMap[hsU + '_' + hsI];
          if (msEntry) {
            var mp = msEntry.split('_');
            var msU = mp[0], msI = mp.slice(1).join('_');
            syncPair(
              cfg.ms + '_u' + msU + '_l' + msI,
              cfg.hs + '_u' + hsU + '_l' + hsI
            );
          }
        });
      }

      // === Wrap markLessonStarted to sync in real-time on click ===
      if (typeof window.markLessonStarted === 'function') {
        var origMLS = window.markLessonStarted;
        window.markLessonStarted = function(unit, lesson) {
          origMLS(unit, lesson);

          if (cfg.isMS) {
            // MS click → do NOT write HS key (one-way: HS→MS only)
          } else {
            // HS click → also write MS started key (if reverse map exists)
            try {
              var ms = JSON.parse(localStorage.getItem('_msMap_' + cfg.folder) || '{}');
              var msK = ms[unit + '_' + lesson];
              if (msK) {
                var mp = msK.split('_');
                var msCompletedKey = cfg.ms + '_u' + mp[0] + '_l' + mp.slice(1).join('_') + '_completed';
                if (localStorage.getItem(msCompletedKey) !== 'true') {
                  localStorage.setItem(cfg.ms + '_u' + mp[0] + '_l' + mp.slice(1).join('_') + '_started', 'true');
                }
              }
            } catch(e) {}
          }
        };
      }

      // Re-apply progress colors after sync (the function is defined by the course page)
      if (typeof window.applyProgressColors === 'function') {
        setTimeout(function() { window.applyProgressColors(); }, 10);
      }

    } catch(e) { /* fail silently */ }
  });
})();

// ========== FONT PRECONNECT OPTIMIZATION ==========
(function() {
  var origins = ['https://fonts.googleapis.com', 'https://fonts.gstatic.com'];
  origins.forEach(function(origin) {
    if (!document.querySelector('link[rel="preconnect"][href="' + origin + '"]')) {
      var link = document.createElement('link');
      link.rel = 'preconnect';
      link.href = origin;
      if (origin.indexOf('gstatic') !== -1) link.crossOrigin = 'anonymous';
      document.head.appendChild(link);
    }
  });
})();

// ========== SCROLL REVEAL ANIMATIONS ==========
(function() {
  if (!('IntersectionObserver' in window)) return;

  // Content selectors to auto-reveal on scroll
  var REVEAL_SELECTORS = [
    '.lesson-notes',
    '.diagram-card',
    '.flashcard-box',
    '.course-box',
    '.rubric-card',
    '.video-embed',
    '.courses-section',
    '.summary-actions'
  ];
  // Parent containers that get stagger treatment on their children
  var STAGGER_SELECTORS = [
    '.courses-section'
  ];

  function tagElements() {
    REVEAL_SELECTORS.forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(el) {
        if (!el.classList.contains('aris-reveal')) {
          el.classList.add('aris-reveal');
        }
      });
    });
    STAGGER_SELECTORS.forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(el) {
        el.classList.add('aris-reveal-stagger');
      });
    });
  }

  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('aris-revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

  function init() {
    tagElements();
    document.querySelectorAll('.aris-reveal').forEach(function(el) {
      observer.observe(el);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() { setTimeout(init, 200); });
  } else {
    setTimeout(init, 200);
  }
})();
