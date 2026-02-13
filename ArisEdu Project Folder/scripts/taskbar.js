// taskbar.js — Shared taskbar injection + logic for all pages
(function () {
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

  // Map lesson folders → course pages
  var courseMap = {
    ChemistryLessons: '/ArisEdu Project Folder/chem.html',
    PhysicsLessons:   '/ArisEdu Project Folder/physics.html',
    BiologyLessons:   '/ArisEdu Project Folder/bio.html',
    Algebra1Lessons:  '/ArisEdu Project Folder/algebra1.html',
    Algebra2Lessons:  '/ArisEdu Project Folder/algebra2.html',
    GeometryLessons:  '/ArisEdu Project Folder/geometry.html'
  };

  // --- Chemistry lesson files (underscore suffixes) ---
  if (filename.indexOf('_Practice') !== -1) {
    backText = '\u2190 Back to Summary';
    backUrl = filename.replace('_Practice.html', '_Summary.html');
  } else if (filename.indexOf('_Summary') !== -1) {
    backText = '\u2190 Back to Lesson';
    backUrl = filename.replace('_Summary.html', '_Video.html');
  } else if (filename.indexOf('_Quiz') !== -1) {
    backText = '\u2190 Back to Practice';
    backUrl = filename.replace('_Quiz.html', '_Practice.html');
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
  // --- Physics lesson files (camelCase, no spaces) ---
  else if (/^PhysicsLesson[\d]/.test(filename) && /Summary\.html$/.test(filename)) {
    backText = '\u2190 Back to Lesson';
    backUrl = filename.replace('Summary.html', '.html');
  }
  else if (/^PhysicsLesson[\d]/.test(filename) && !/Summary\.html$/.test(filename)) {
    // Main Physics lesson → back to PhysicsUnit overview
    backText = '\u2190 Back to Unit';
    var unitMatch = filename.match(/PhysicsLesson(\d+)\./);
    if (unitMatch) backUrl = '/ArisEdu Project Folder/PhysicsLessons/PhysicsUnit' + unitMatch[1] + '.html';
    else backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
  }
  // --- PhysicsUnit overview pages ---
  else if (/^PhysicsUnit\d+\.html$/.test(filename)) {
    backText = '\u2190 Back to Physics';
    backUrl = '/ArisEdu Project Folder/physics.html';
  }
  // --- Chemistry/other main lesson files (inside a Unit folder) ---
  else if (lessonFolder && /^Lesson\s/.test(filename)) {
    backText = '\u2190 Back to Course';
    backUrl = courseMap[lessonFolder] || '/ArisEdu Project Folder/Courses.html';
  }
  // --- Course pages (chem.html, physics.html, etc.) —→ back to Courses ---
  else if (/^(chem|physics|bio|algebra1|algebra2|geometry)\.html$/.test(filename)) {
    backText = '\u2190 Back to Courses';
    backUrl = '/ArisEdu Project Folder/Courses.html';
  }
  // --- Top-level pages without a back button ---
  else {
    showBack = false;
  }

  // Only inject HTML if it doesn't already exist
  if (!document.querySelector('nav.taskbar')) {
    var backBtnHtml = showBack
      ? '<button class="taskbar-button" id="back-button">' + backText + '</button>'
      : '';
    var nav = document.createElement('nav');
    nav.className = 'taskbar';
    nav.innerHTML =
      '<div class="taskbar-container">' +
        backBtnHtml +
        '<button class="taskbar-button" id="search-button">\uD83D\uDD0D Search</button>' +
        '<a class="taskbar-button" href="/index.html" id="homepage-button">\uD83C\uDFE0 Homepage</a>' +
        '<a class="taskbar-button" href="/ArisEdu Project Folder/Courses.html" id="course-button">\uD83D\uDCDA Courses</a>' +
        '<button class="taskbar-button" id="settings-button">\u2699\uFE0F Settings</button>' +
        '<a class="taskbar-button" href="/ArisEdu Project Folder/LoginSignup.html" id="login-signup-button">\uD83D\uDD10 Login/Signup</a>' +
      '</div>' +
      '<div aria-hidden="true" class="settings-menu" id="settings-menu">' +
        '<div class="settings-item">' +
          '<label style="display:flex;align-items:center;gap:0.5rem;cursor:pointer;">' +
            '<input checked id="dark-mode-checkbox" type="checkbox"/>' +
            '<span>Dark Mode</span>' +
          '</label>' +
        '</div>' +
        '<a class="settings-item" href="/ArisEdu Project Folder/Preferences.html">Preferences</a>' +
      '</div>';
    document.body.insertBefore(nav, document.body.firstChild);
  }

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
    settingsBtn.addEventListener('click', function () {
      var menu = document.getElementById('settings-menu');
      if (!menu) return;
      var isHidden = menu.getAttribute('aria-hidden') === 'true';
      menu.setAttribute('aria-hidden', String(!isHidden));
      if (isHidden) {
        menu.style.visibility = 'visible';
        menu.style.opacity = '1';
        menu.style.transform = 'translateY(0)';
      } else {
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

  // --- Settings menu alignment ---
  (function () {
    var sBtn = document.getElementById('settings-button');
    var sMenu = document.getElementById('settings-menu');
    if (!sBtn || !sMenu) return;
    var wrapper = document.createElement('span');
    wrapper.style.position = 'relative';
    wrapper.style.display = 'inline-flex';
    sBtn.parentElement.insertBefore(wrapper, sBtn);
    wrapper.appendChild(sBtn);
    wrapper.appendChild(sMenu);
    sMenu.style.position = 'absolute';
    sMenu.style.top = '100%';
    sMenu.style.left = '0';
    sMenu.style.right = 'auto';
    sMenu.style.marginTop = '0.35rem';
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
    menu.style.position = 'absolute';
    menu.style.top = '100%';
    menu.style.left = '0';
    menu.style.right = 'auto';
    menu.style.minWidth = '160px';
    menu.style.marginTop = '0.35rem';
    menu.style.background = isDarkMode ? '#0f172a' : 'white';
    menu.style.border = isDarkMode ? '1px solid #1f2937' : '1px solid #e2e8f0';
    menu.style.borderRadius = '0.5rem';
    menu.style.boxShadow = isDarkMode
      ? '0 12px 24px rgba(2, 6, 23, 0.6)'
      : '0 10px 20px rgba(2, 6, 23, 0.15)';
    menu.style.padding = '0.4rem';
    menu.style.display = 'none';
    menu.style.zIndex = '2000';

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
      logoutButton.style.background = isDarkMode
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
      window.location.href = '/ArisEdu Project Folder/LoginSignup.html';
    });

    menu.appendChild(logoutButton);

    var parent = loginButton.parentElement;
    if (parent) {
      var wrapper = document.createElement('span');
      wrapper.style.position = 'relative';
      wrapper.style.display = 'inline-flex';
      parent.insertBefore(wrapper, loginButton);
      wrapper.appendChild(loginButton);
      wrapper.appendChild(menu);
    }

    function closeMenu() {
      menu.style.display = 'none';
      loginButton.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-hidden', 'true');
    }

    function toggleMenu(event) {
      event.preventDefault();
      var isOpen = menu.style.display === 'block';
      if (isOpen) {
        closeMenu();
      } else {
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
})();
