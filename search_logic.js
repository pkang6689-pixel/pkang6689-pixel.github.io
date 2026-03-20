function initializeSearch() {
    // 1. Check if Search Button exists
    const searchBtn = document.getElementById('search-button');
    if (!searchBtn) {
        setTimeout(initializeSearch, 500);
        return;
    }

    // Helper
    function _t(key) {
        if (window.arisTranslate) return window.arisTranslate(key);
        if (window.globalTranslations && window.globalTranslations[key]) return window.globalTranslations[key];
        return key;
    }

    // 2. Create Modal HTML
    const modalHTML = `
        <style>
            /* ── Search result items ─────────────────────────── */
            .aris-search-result-item {
                display: flex; align-items: center; gap: 0.75rem;
                padding: 0.75rem 1rem; border-bottom: 1px solid #f1f5f9;
                text-decoration: none; color: inherit;
                transition: background 0.15s;
            }
            .aris-search-result-item:hover { background: #f8fafc; }
            .aris-search-result-text { flex: 1; min-width: 0; }
            .aris-search-result-title { font-weight: 600; color: #334155; font-size: 0.95rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
            .aris-search-result-subtitle { font-size: 0.8rem; color: #64748b; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
            .aris-search-type-badge {
                flex-shrink: 0; font-size: 0.65rem; font-weight: 600;
                padding: 0.2rem 0.5rem; border-radius: 999px;
                background: #e0f2fe; color: #0369a1;
                text-transform: uppercase; letter-spacing: 0.03em;
            }

            /* ── Filter chips ────────────────────────────────── */
            .aris-filter-row {
                display: flex; gap: 0.35rem; padding: 0.5rem 1rem;
                overflow-x: auto; scrollbar-width: none;
                border-bottom: 1px solid #e2e8f0;
            }
            .aris-filter-row::-webkit-scrollbar { display: none; }
            .aris-filter-chip {
                flex-shrink: 0; padding: 0.3rem 0.65rem;
                font-size: 0.75rem; font-weight: 500;
                border-radius: 999px; border: 1.5px solid #cbd5e1;
                background: transparent; color: #475569;
                cursor: pointer; transition: all 0.15s;
                white-space: nowrap; font-family: inherit;
            }
            .aris-filter-chip:hover { border-color: #3b82f6; color: #3b82f6; }
            .aris-filter-chip.active { background: #3b82f6; color: white; border-color: #3b82f6; }

            /* ── Load-more button ─────────────────────────────── */
            .aris-load-more {
                display: block; width: 100%; padding: 0.65rem;
                font-size: 0.85rem; font-weight: 600;
                background: transparent; border: none; border-top: 1px solid #e2e8f0;
                color: #3b82f6; cursor: pointer; font-family: inherit;
                transition: background 0.15s;
            }
            .aris-load-more:hover { background: #f0f9ff; }

            /* ── Scrollbar ───────────────────────────────────── */
            #aris-search-results::-webkit-scrollbar { width: 6px; }
            #aris-search-results::-webkit-scrollbar-track { background: #f1f5f9; }
            #aris-search-results::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
            #aris-search-results::-webkit-scrollbar-thumb:hover { background: #94a3b8; }

            /* ── Dark mode ───────────────────────────────────── */
            body.dark-mode #aris-search-content { background: #1e293b !important; color: #e2e8f0 !important; }
            body.dark-mode #aris-search-input { background: #0f172a !important; color: white !important; border-color: #334155 !important; }
            body.dark-mode #aris-search-footer { background: #0f172a !important; border-color: #334155 !important; color: #94a3b8 !important; }
            body.dark-mode #aris-search-close { color: #e2e8f0 !important; }
            body.dark-mode .aris-search-result-item { background: transparent !important; border-bottom-color: #334155 !important; }
            body.dark-mode .aris-search-result-item:hover { background: #334155 !important; }
            body.dark-mode .aris-search-result-title { color: #e2e8f0 !important; }
            body.dark-mode .aris-search-result-subtitle { color: #cbd5e1 !important; }
            body.dark-mode .aris-filter-row { border-color: #334155 !important; }
            body.dark-mode .aris-filter-chip { border-color: #475569; color: #94a3b8; }
            body.dark-mode .aris-filter-chip:hover { border-color: #60a5fa; color: #60a5fa; }
            body.dark-mode .aris-filter-chip.active { background: #2563eb; border-color: #2563eb; color: white; }
            body.dark-mode .aris-load-more { color: #60a5fa; border-color: #334155; }
            body.dark-mode .aris-load-more:hover { background: rgba(59,130,246,0.1); }
            body.dark-mode .aris-search-type-badge { background: #1e3a5f; color: #93c5fd; }
            body.dark-mode #aris-search-results::-webkit-scrollbar-track { background: #0f172a; }
            body.dark-mode #aris-search-results::-webkit-scrollbar-thumb { background: #475569; }
        </style>
        <div id="aris-search-modal" style="display:none; visibility:hidden; opacity:0; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.8); z-index:99999; backdrop-filter:blur(4px); align-items:flex-start; justify-content:center; padding-top:5rem; transition:opacity 0.2s ease;">
            <div id="aris-search-content" style="background:white; width:90%; max-width:620px; border-radius:1rem; box-shadow:0 25px 50px -12px rgba(0,0,0,0.25); overflow:hidden; display:flex; flex-direction:column; max-height:80vh;">
                <!-- Header -->
                <div style="padding:0.75rem 1rem; border-bottom:1px solid #e2e8f0; display:flex; align-items:center; gap:0.5rem;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                    <input type="text" id="aris-search-input" placeholder="${_t('Search lessons, courses, quizzes...')}" style="flex:1; padding:0.6rem; font-size:1rem; border:2px solid #e2e8f0; border-radius:0.5rem; outline:none; transition:border 0.2s; font-family:inherit;">
                    <kbd style="font-size:0.65rem; padding:0.15rem 0.4rem; border:1px solid #cbd5e1; border-radius:0.25rem; color:#94a3b8; font-family:inherit;">ESC</kbd>
                    <button id="aris-search-close" style="background:none; border:none; font-size:1.4rem; cursor:pointer; color:#64748b; line-height:1;">&times;</button>
                </div>
                <!-- Filter chips: type -->
                <div class="aris-filter-row" id="aris-type-filters"></div>
                <!-- Filter chips: category -->
                <div class="aris-filter-row" id="aris-cat-filters" style="padding-top:0;"></div>
                <!-- Results -->
                <div id="aris-search-results" style="padding:0; overflow-y:auto; flex:1; min-height:150px; max-height:400px; scrollbar-width:thin; scrollbar-color:#cbd5e1 #f1f5f9;">
                    <div style="padding:2rem; text-align:center; color:#94a3b8; font-size:0.9rem;">${_t('Type to start searching...')}</div>
                </div>
                <!-- Footer -->
                <div id="aris-search-footer" style="padding:0.6rem 1rem; background:#f8fafc; border-top:1px solid #e2e8f0; font-size:0.75rem; color:#64748b; text-align:right;">
                    ${_t('ArisEdu Search')}
                </div>
            </div>
        </div>
    `;

    // 3. Inject Modal into Body
    document.body.insertAdjacentHTML('beforeend', modalHTML);

    // 4. DOM refs
    const modal = document.getElementById('aris-search-modal');
    const input = document.getElementById('aris-search-input');
    const resultsContainer = document.getElementById('aris-search-results');
    const closeBtn = document.getElementById('aris-search-close');
    const footerDiv = document.getElementById('aris-search-footer');
    const typeFiltersRow = document.getElementById('aris-type-filters');
    const catFiltersRow = document.getElementById('aris-cat-filters');

    // 5. State
    const PAGE_SIZE = 12;
    let allMatches = [];
    let displayedCount = 0;
    let activeTypeFilter = null;   // null = all
    let activeCatFilter = null;    // null = all

    // ── Build filter chips from index ───────────────────────────────
    const TYPE_ORDER = ['Summary', 'Video', 'Practice', 'Quiz', 'Test', 'Test Practice', 'Course', 'Practice Exam', 'Page'];
    const TYPE_BADGE_COLORS = {
        Summary:        { bg: '#dbeafe', fg: '#1e40af' },
        Video:          { bg: '#fef3c7', fg: '#92400e' },
        Practice:       { bg: '#d1fae5', fg: '#065f46' },
        Quiz:           { bg: '#ede9fe', fg: '#5b21b6' },
        Test:           { bg: '#fce7f3', fg: '#9d174d' },
        'Test Practice':{ bg: '#fce7f3', fg: '#9d174d' },
        Course:         { bg: '#e0f2fe', fg: '#0369a1' },
        'Practice Exam':{ bg: '#fef3c7', fg: '#92400e' },
        Page:           { bg: '#f1f5f9', fg: '#475569' },
    };

    function buildFilterChips() {
        if (typeof ARIS_EDU_SEARCH_INDEX === 'undefined') return;

        // Type chips
        const typesInIndex = new Set(ARIS_EDU_SEARCH_INDEX.map(i => i.type).filter(Boolean));
        let typeHTML = `<button class="aris-filter-chip active" data-type="">All Types</button>`;
        TYPE_ORDER.forEach(t => {
            if (typesInIndex.has(t)) typeHTML += `<button class="aris-filter-chip" data-type="${t}">${t}</button>`;
        });
        typeFiltersRow.innerHTML = typeHTML;

        // Category chips — group by subject area
        const catsInIndex = new Set(ARIS_EDU_SEARCH_INDEX.map(i => i.category).filter(Boolean));
        const groups = { Math: [], Science: [], AP: [], 'Middle School': [] };
        const GROUP_LABELS = { Math: '📐', Science: '🔬', AP: '🎓', 'Middle School': '📚' };

        // Build category → group map
        const catGroup = {};
        ARIS_EDU_SEARCH_INDEX.forEach(item => {
            if (!item.category) return;
            const sub = item.subtitle || '';
            if (item.category.startsWith('AP ')) catGroup[item.category] = 'AP';
            else if (item.category.startsWith('MS ')) catGroup[item.category] = 'Middle School';
            else if (sub.includes('Math') || ['Algebra 1','Algebra 2','Geometry','Precalculus','Trigonometry','Statistics','Financial Math','Linear Algebra'].includes(item.category)) catGroup[item.category] = 'Math';
            else if (sub.includes('Science') || ['Chemistry','Physics','Biology','Anatomy','Astronomy','Earth Science','Environmental Science','Integrated Science','Marine Science'].includes(item.category)) catGroup[item.category] = 'Science';
        });

        Object.entries(catGroup).forEach(([cat, grp]) => {
            if (groups[grp] && catsInIndex.has(cat)) groups[grp].push(cat);
        });
        Object.values(groups).forEach(arr => arr.sort());

        let catHTML = `<button class="aris-filter-chip active" data-cat="">All Courses</button>`;
        Object.entries(groups).forEach(([grp, cats]) => {
            if (cats.length === 0) return;
            cats.forEach(c => { catHTML += `<button class="aris-filter-chip" data-cat="${c}">${c}</button>`; });
        });
        catFiltersRow.innerHTML = catHTML;

        // Chip click handlers
        typeFiltersRow.addEventListener('click', e => {
            const chip = e.target.closest('.aris-filter-chip');
            if (!chip) return;
            typeFiltersRow.querySelectorAll('.aris-filter-chip').forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            activeTypeFilter = chip.dataset.type || null;
            performSearch(input.value);
        });
        catFiltersRow.addEventListener('click', e => {
            const chip = e.target.closest('.aris-filter-chip');
            if (!chip) return;
            catFiltersRow.querySelectorAll('.aris-filter-chip').forEach(c => c.classList.remove('active'));
            chip.classList.add('active');
            activeCatFilter = chip.dataset.cat || null;
            performSearch(input.value);
        });
    }

    // ── Search & render ─────────────────────────────────────────────
    function openSearch() {
        modal.style.setProperty('display', 'flex', 'important');
        modal.style.visibility = 'visible';
        modal.style.opacity = '1';
        input.value = '';
        activeTypeFilter = null;
        activeCatFilter = null;
        // Reset chips
        typeFiltersRow.querySelectorAll('.aris-filter-chip').forEach((c, i) => c.classList.toggle('active', i === 0));
        catFiltersRow.querySelectorAll('.aris-filter-chip').forEach((c, i) => c.classList.toggle('active', i === 0));
        setTimeout(() => input.focus(), 50);
        allMatches = [];
        displayedCount = 0;
        resultsContainer.innerHTML = `<div style="padding:2rem; text-align:center; color:#94a3b8; font-size:0.9rem;">${_t('Type to start searching...')}</div>`;
        footerDiv.textContent = _t('ArisEdu Search');
    }

    function closeSearch() {
        modal.style.opacity = '0';
        setTimeout(() => { modal.style.display = 'none'; modal.style.visibility = 'hidden'; }, 200);
    }

    function escapeRegex(str) {
        return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function performSearch(query) {
        if (!query || query.length < 2) {
            resultsContainer.innerHTML = `<div style="padding:2rem; text-align:center; color:#94a3b8; font-size:0.9rem;">${_t('Type at least 2 characters...')}</div>`;
            footerDiv.textContent = _t('ArisEdu Search');
            allMatches = [];
            displayedCount = 0;
            return;
        }
        if (typeof ARIS_EDU_SEARCH_INDEX === 'undefined') {
            resultsContainer.innerHTML = `<div style="padding:1rem; color:#ef4444;">${_t('Search index not loaded.')}</div>`;
            return;
        }

        const q = query.toLowerCase();
        allMatches = ARIS_EDU_SEARCH_INDEX.filter(item => {
            // Text match
            const textMatch = (item.title && item.title.toLowerCase().includes(q)) ||
                              (item.subtitle && item.subtitle.toLowerCase().includes(q)) ||
                              (item.content && item.content.toLowerCase().includes(q));
            if (!textMatch) return false;
            // Filter by type
            if (activeTypeFilter && item.type !== activeTypeFilter) return false;
            // Filter by category
            if (activeCatFilter && item.category !== activeCatFilter) return false;
            return true;
        });

        displayedCount = 0;
        renderPage(true);
    }

    function renderPage(fresh) {
        const slice = allMatches.slice(displayedCount, displayedCount + PAGE_SIZE);
        displayedCount += slice.length;

        if (allMatches.length === 0) {
            resultsContainer.innerHTML = `<div style="padding:2rem; text-align:center; color:#94a3b8; font-size:0.9rem;">${_t('No results found.')}</div>`;
            footerDiv.textContent = _t('ArisEdu Search');
            return;
        }

        let html = '';
        slice.forEach(item => {
            const badge = TYPE_BADGE_COLORS[item.type] || TYPE_BADGE_COLORS.Page;
            html += `
                <a href="${item.url}" class="aris-search-result-item">
                    <div class="aris-search-result-text">
                        <div class="aris-search-result-title">${highlight(item.title, input.value)}</div>
                        <div class="aris-search-result-subtitle">${highlight(item.subtitle, input.value)}</div>
                    </div>
                    <span class="aris-search-type-badge" style="background:${badge.bg};color:${badge.fg};">${item.type}</span>
                </a>`;
        });

        // Load-more button
        if (displayedCount < allMatches.length) {
            const remaining = allMatches.length - displayedCount;
            html += `<button class="aris-load-more" id="aris-load-more">${_t('Show more')} (${remaining} ${_t('remaining')})</button>`;
        }

        if (fresh) {
            resultsContainer.innerHTML = html;
        } else {
            // Remove old load-more button, append new items
            const oldBtn = resultsContainer.querySelector('.aris-load-more');
            if (oldBtn) oldBtn.remove();
            resultsContainer.insertAdjacentHTML('beforeend', html);
        }

        // Bind load-more
        const loadMoreBtn = resultsContainer.querySelector('#aris-load-more');
        if (loadMoreBtn) {
            loadMoreBtn.addEventListener('click', (e) => {
                e.preventDefault();
                renderPage(false);
            });
        }

        footerDiv.textContent = displayedCount === allMatches.length
            ? `${_t('Showing all')} ${allMatches.length} ${_t('results')}`
            : `${_t('Showing')} ${displayedCount} ${_t('of')} ${allMatches.length} ${_t('results')}`;
    }

    function highlight(text, query) {
        if (!text || !query) return text || '';
        const safe = escapeRegex(query);
        return text.replace(new RegExp(`(${safe})`, 'gi'), '<span style="background:#fef08a;color:#854d0e;">$1</span>');
    }

    // ── Build chips once index is ready ─────────────────────────────
    buildFilterChips();

    // 6. Event Listeners
    searchBtn.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); openSearch(); });
    document.addEventListener('click', (e) => {
        const btn = e.target.closest('#search-button');
        if (!btn) return;
        e.preventDefault(); e.stopPropagation(); openSearch();
    });
    closeBtn.addEventListener('click', closeSearch);
    modal.addEventListener('click', (e) => { if (e.target === modal) closeSearch(); });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.style.display !== 'none' && modal.style.visibility !== 'hidden') closeSearch();
    });

    let _searchTimer;
    input.addEventListener('input', () => {
        clearTimeout(_searchTimer);
        _searchTimer = setTimeout(() => performSearch(input.value), 150);
    });


    // 7. Global Theme Application (Enhanced for Full Site Coverage)
    function applyGlobalTheme() {
        try {
            const theme = localStorage.getItem('arisEduColorTheme') || 'blue-green';
            
            // Define Gradients
            const AURORA_GRADIENT = 'linear-gradient(135deg, #3b82f6 0%, #10b981 50%, #8b5cf6 100%)';
            const AURORA_GRADIENT_NO_ANGLE = 'linear-gradient(#3b82f6 0%, #10b981 50%, #8b5cf6 100%)';
            const AURORA_GRADIENT_REVERSED = 'linear-gradient(135deg, #8b5cf6 0%, #10b981 50%, #3b82f6 100%)';
            
            const themes = {
                'blue-green': AURORA_GRADIENT,
                'sunset': 'linear-gradient(to right, #FF7E5F, #00C9A7, #1A2A6C)',
                'forest': 'linear-gradient(to right, #228B22, #87CEEB, #E6E6FA)',
                'aurora-veil': 'linear-gradient(to right, #32CD32, #00FFFF, #8A2BE2)',
                'coral': 'linear-gradient(to right, #FF6F61, #40E0D0, #4B0082)',
                'twilight': 'linear-gradient(to right, #50C878, #0F52BA, #FF00FF)',
                'solar': 'linear-gradient(to right, #FFD700, #DC143C, #2E0854)',
                'autumn': 'linear-gradient(to right, #CC5500, #DAA520, #8B4513)',
                'crimson': 'linear-gradient(to right, #FFC0CB, #C21E56, #420D09)',
                'sunrise': 'linear-gradient(to right, #FFDAB9, #FF7F50, #FFFACD)',
                'ocean-mist': 'linear-gradient(to right, #001F3F, #3D9970, #E0FFFF)',
                'lavender': 'linear-gradient(to right, #C8A2C8, #9DC183, #FFFDD0)',
                'monochrome': 'linear-gradient(to right, #2C2C2C, #C0C0C0, #FFFFFF)',
                'cyber': 'linear-gradient(to right, #000000, #00FFFF)',
                'horizon': 'linear-gradient(to right, #708090, #4682B4, #FFFFF0)'
            };

            const activeGradient = themes[theme];

            if (activeGradient) {
                document.documentElement.style.setProperty('--rubric-border-gradient', activeGradient);
                
                // 1. Taskbar
                const taskbar = document.querySelector('.taskbar');
                if (taskbar) taskbar.style.background = activeGradient;

                // 2. Headings and other elements with explicit gradient class or inline style
                const elements = document.querySelectorAll('*');
                elements.forEach(el => {
                    // Prevent modifying the theme selector options themselves
                    if (el.classList.contains('custom-option')) return;

                    const style = el.getAttribute('style');
                    if (!style) return;

                    // Handle standard Aurora (with 135deg)
                    if (style.includes(AURORA_GRADIENT) || style.includes('linear-gradient(135deg, #3b82f6 0%, #10b981 50%, #8b5cf6 100%)')) {
                       // Replace exact string in style attribute to preserve other properties
                       let newStyle = style.replace(/linear-gradient\(135deg, #3b82f6 0%, #10b981 50%, #8b5cf6 100%\)/g, activeGradient);
                       el.setAttribute('style', newStyle);
                    }

                    // Handle standard Aurora (NO angle specified - used in course boxes)
                    if (style.includes(AURORA_GRADIENT_NO_ANGLE) || style.includes('linear-gradient(#3b82f6 0%, #10b981 50%, #8b5cf6 100%)')) {
                        let newStyle = style.replace(/linear-gradient\(#3b82f6 0%, #10b981 50%, #8b5cf6 100%\)/g, activeGradient);
                        el.setAttribute('style', newStyle);
                     }

                    // Handle reversed Aurora (often used in buttons like .side-button)
                    if (style.includes(AURORA_GRADIENT_REVERSED) || style.includes('linear-gradient(135deg, #8b5cf6 0%, #10b981 50%, #3b82f6 100%)')) {
                        let newStyle = style.replace(/linear-gradient\(135deg, #8b5cf6 0%, #10b981 50%, #3b82f6 100%\)/g, activeGradient);
                        el.setAttribute('style', newStyle);
                     }
                    
                    // Fallback for background shorthand with hex codes if exact string doesn't match
                    // This is aggressive but necessary if formatting differs slightly (spaces etc)
                     if (style.includes('background:') && style.includes('#3b82f6') && style.includes('#10b981')) {
                        if (style.includes('gradient')) {
                             // Attempt to replace the gradient part
                             el.style.backgroundImage = activeGradient;
                        }
                    }
                });

                // 3. Handle CSS Classes via Injection
                const css = `
                    /* Text Gradients */
                    .page-title, 
                    .rubric-title, 
                    .company-title,
                    .rubric-hover-dot span {
                        background-image: ${activeGradient} !important;
                        background: ${activeGradient} !important;
                        -webkit-background-clip: text !important;
                        background-clip: text !important;
                        -webkit-text-fill-color: transparent; 
                    }

                    /* Background Gradients */
                    .taskbar,
                    .side-button,
                    .action-button, 
                    .nav-button,
                    .course-box,
                    .cta-button {
                        background: ${activeGradient} !important;
                        background-image: ${activeGradient} !important;
                    }

                    /* Border Gradients (Rubric Box) */
                    .rubric-card {
                        --rubric-border-gradient: ${activeGradient} !important;
                    }
                `;

                 const head = document.head || document.getElementsByTagName('head')[0];
                 const style = document.createElement('style');
                 style.type = 'text/css';
                 style.appendChild(document.createTextNode(css));
                 head.appendChild(style);

            } else {
                 // Reset if needed (though page reload usually handles this naturally)
            }

        } catch (e) {
            console.error("ArisEdu Theme Error:", e);
        }
    }
    
    // Run immediately
    applyGlobalTheme();
    
    // Expose to window for dynamic updates
    window.applyGlobalTheme = applyGlobalTheme;
}

// Initialize search functionality
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeSearch);
} else {
    // DOM is already loaded
    initializeSearch();
}
