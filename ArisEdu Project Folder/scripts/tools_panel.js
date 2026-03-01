// ═══════════════════════════════════════════════════════════
// 🛠️  ArisEdu Tools Panel – dropdown + draggable/resizable windows
// ═══════════════════════════════════════════════════════════
(function () {
    'use strict';

    // ─── helpers ───────────────────────────────────────────
    const _t = window._t || (k => k);
    const isDark = () => document.body.classList.contains('dark-mode');

    // ─── theme tokens (dynamic) ────────────────────────────
    function T() {
        const d = isDark();
        return {
            bg:       d ? '#1e293b' : '#ffffff',
            bgAlt:    d ? '#0f172a' : '#f8fafc',
            border:   d ? '#334155' : '#e2e8f0',
            text:     d ? '#e2e8f0' : '#1e293b',
            textMuted:d ? '#94a3b8' : '#64748b',
            accent:   '#3b82f6',
            handle:   d ? 'linear-gradient(135deg,#3b82f6 0%,#10b981 100%)'
                        : 'linear-gradient(135deg,#3b82f6 0%,#10b981 100%)',
            inputBg:  d ? '#1e293b' : '#ffffff',
            inputBdr: d ? '#475569' : '#cbd5e1',
            btnBg:    d ? '#334155' : '#e2e8f0',
            btnHover: d ? '#475569' : '#cbd5e1',
            displayBg:d ? '#0f172a' : '#f1f5f9',
        };
    }

    // ─── CSS (injected once) ──────────────────────────────
    const STYLE = document.createElement('style');
    STYLE.textContent = `
    /* ─ tools dropdown ─ */
    #tools-dropdown-btn{position:relative;}
    #tools-dropdown-menu{
        display:none;position:absolute;top:calc(100% + 6px);left:50%;transform:translateX(-50%);
        min-width:180px;border-radius:0.6rem;overflow:hidden;z-index:10001;
        box-shadow:0 8px 24px rgba(0,0,0,0.22);
    }
    #tools-dropdown-menu.show{display:block;}
    .tools-dd-item{
        display:flex;align-items:center;gap:0.5rem;width:100%;padding:0.55rem 1rem;
        border:none;cursor:pointer;font-size:0.88rem;font-family:inherit;text-align:left;
        transition:background 0.15s;
    }
    .tools-dd-item:hover{filter:brightness(0.92);}
    .tools-dd-footer{padding:0.5rem 0.75rem;font-size:0.7rem;opacity:0.55;line-height:1.35;border-top:1px solid rgba(128,128,128,0.2);text-align:center;cursor:default;}

    /* ─ generic tool window ─ */
    .tool-window{
        position:fixed;z-index:9998;display:flex;flex-direction:column;
        border-radius:0.75rem;overflow:hidden;
        box-shadow:0 10px 30px rgba(0,0,0,0.25);
        min-width:200px;min-height:160px;
    }
    .tool-window .tw-handle{
        display:flex;align-items:center;justify-content:space-between;
        padding:0.55rem 0.75rem;cursor:grab;user-select:none;color:#fff;font-weight:600;font-size:0.85rem;
    }
    .tool-window .tw-handle.grabbing{cursor:grabbing;}
    .tool-window .tw-body{flex:1;overflow:auto;padding:0.75rem;display:flex;flex-direction:column;}
    .tool-window .tw-close{background:none;border:none;color:#fff;cursor:pointer;font-size:1rem;padding:0 0.25rem;}
    /* resize handle */
    .tool-window .tw-resize{
        position:absolute;right:0;bottom:0;width:18px;height:18px;cursor:nwse-resize;z-index:2;
        background:linear-gradient(135deg,transparent 50%,rgba(148,163,184,0.45) 50%);
        border-radius:0 0 0.75rem 0;
    }

    /* ─ calculator ─ */
    .calc-display{width:100%;text-align:right;font-size:1.2rem;padding:0.5rem 0.6rem;border-radius:0.4rem;border:1px solid;margin-bottom:0.25rem;font-family:monospace;overflow-x:auto;cursor:text;outline:none;}
    .calc-display:focus{box-shadow:0 0 0 2px rgba(99,102,241,0.45);}
    .calc-result{width:100%;text-align:right;font-size:0.8rem;padding:0 0.6rem 0.35rem;font-family:monospace;opacity:0.6;min-height:1.1em;}
    .calc-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:3px;}
    .calc-btn{padding:0.4rem 0.1rem;border:none;border-radius:0.35rem;cursor:pointer;font-size:0.82rem;font-family:inherit;font-weight:600;transition:filter 0.12s;white-space:nowrap;}
    .calc-btn:hover{filter:brightness(0.88);}
    .calc-btn.op{font-weight:700;}
    .calc-btn.wide{grid-column:span 2;}
    .calc-btn.fn{font-size:0.75rem;}

    /* ─ graphing calculator ─ */
    .graph-input-row{display:flex;gap:4px;margin-bottom:6px;}
    .graph-input-row input{flex:1;padding:0.35rem 0.5rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;font-family:monospace;}
    .graph-input-row button{padding:0.35rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.85rem;}

    /* ─ timer ─ */
    .timer-display{font-size:2.2rem;font-weight:700;text-align:center;font-family:monospace;letter-spacing:2px;margin:0.6rem 0;}
    .timer-btns{display:flex;gap:6px;justify-content:center;}
    .timer-btns button{padding:0.4rem 1rem;border:none;border-radius:0.35rem;cursor:pointer;font-weight:600;font-size:0.85rem;}

    /* ─ notepad ─ */
    .notepad-area{flex:1;width:100%;resize:none;border-radius:0.35rem;border:1px solid;padding:0.5rem;font-size:0.9rem;font-family:'Segoe UI',system-ui,sans-serif;min-height:120px;}

    /* ─ unit converter ─ */
    .uc-row{display:flex;gap:6px;align-items:center;margin-bottom:6px;}
    .uc-row select,.uc-row input{padding:0.35rem 0.5rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;flex:1;}
    .uc-result{font-size:1.1rem;font-weight:700;text-align:center;padding:0.6rem;border-radius:0.4rem;margin-top:4px;}
    .uc-swap{background:none;border:none;font-size:1.1rem;cursor:pointer;padding:0 4px;}

    /* ─ formula sheet ─ */
    .fs-tabs{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:8px;}
    .fs-tab{padding:0.3rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.78rem;font-weight:600;transition:filter 0.12s;}
    .fs-tab.active{box-shadow:0 0 0 2px rgba(59,130,246,0.5);}
    .fs-card{padding:0.5rem 0.7rem;border-radius:0.4rem;margin-bottom:4px;font-size:0.82rem;line-height:1.5;font-family:monospace;}

    /* ─ flashcards ─ */
    .fc-card{width:100%;min-height:140px;border-radius:0.6rem;display:flex;align-items:center;justify-content:center;text-align:center;cursor:pointer;padding:1rem;font-size:1rem;font-weight:600;transition:transform 0.35s;position:relative;user-select:none;}
    .fc-card .fc-hint{position:absolute;bottom:6px;font-size:0.65rem;opacity:0.5;font-weight:400;}
    .fc-nav{display:flex;gap:6px;justify-content:center;align-items:center;margin-top:8px;}
    .fc-nav button{padding:0.35rem 0.8rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.85rem;}
    .fc-input-row{display:flex;gap:4px;margin-bottom:4px;}
    .fc-input-row input{flex:1;padding:0.3rem 0.5rem;border-radius:0.3rem;border:1px solid;font-size:0.82rem;}
    .fc-input-row button{padding:0.3rem 0.6rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.82rem;}
    .fc-count{font-size:0.75rem;opacity:0.6;text-align:center;}

    /* ─ whiteboard ─ */
    .wb-toolbar{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:4px;align-items:center;}
    .wb-toolbar button,.wb-toolbar input,.wb-toolbar select{padding:0.25rem 0.5rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.78rem;font-weight:600;}
    .wb-toolbar input[type="color"]{width:28px;height:28px;padding:0;border:none;cursor:pointer;}
    .wb-toolbar input[type="range"]{width:60px;cursor:pointer;}
    .wb-canvas{width:100%;flex:1;border-radius:0.4rem;cursor:crosshair;display:block;}

    /* ─ todo list ─ */
    .td-input-row{display:flex;gap:4px;margin-bottom:8px;}
    .td-input-row input{flex:1;padding:0.35rem 0.5rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;}
    .td-input-row button{padding:0.35rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.85rem;}
    .td-item{display:flex;align-items:center;gap:6px;padding:0.4rem 0.5rem;border-radius:0.35rem;margin-bottom:3px;font-size:0.85rem;}
    .td-item.done span{text-decoration:line-through;opacity:0.5;}
    .td-item input[type="checkbox"]{cursor:pointer;}
    .td-item span{flex:1;}
    .td-item button{background:none;border:none;cursor:pointer;font-size:0.85rem;opacity:0.5;}
    .td-item button:hover{opacity:1;}
    .td-filter{display:flex;gap:4px;margin-bottom:6px;}
    .td-filter button{padding:0.2rem 0.6rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.75rem;font-weight:600;}

    /* ─ pomodoro timer ─ */
    .pomo-display{font-size:3rem;font-weight:700;text-align:center;font-family:monospace;letter-spacing:2px;margin:0.5rem 0;}
    .pomo-label{text-align:center;font-size:0.85rem;font-weight:600;margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:1px;}
    .pomo-btns{display:flex;gap:6px;justify-content:center;margin-bottom:0.5rem;}
    .pomo-btns button{padding:0.4rem 1rem;border:none;border-radius:0.35rem;cursor:pointer;font-weight:600;font-size:0.85rem;}
    .pomo-stats{display:flex;gap:12px;justify-content:center;font-size:0.8rem;opacity:0.7;}

    /* ─ study planner ─ */
    .sp-week{display:grid;grid-template-columns:repeat(7,1fr);gap:3px;flex:1;overflow-y:auto;}
    .sp-day{display:flex;flex-direction:column;gap:2px;min-height:80px;border-radius:0.35rem;padding:4px;font-size:0.7rem;}
    .sp-day-header{font-weight:700;font-size:0.72rem;text-align:center;margin-bottom:2px;text-transform:uppercase;letter-spacing:0.5px;}
    .sp-block{padding:3px 4px;border-radius:3px;font-size:0.65rem;font-weight:600;cursor:pointer;position:relative;line-height:1.3;}
    .sp-block .sp-del{position:absolute;top:0;right:2px;cursor:pointer;font-size:0.6rem;opacity:0;transition:opacity 0.15s;}
    .sp-block:hover .sp-del{opacity:1;}
    .sp-add-row{display:flex;gap:4px;margin-bottom:6px;flex-wrap:wrap;}
    .sp-add-row select,.sp-add-row input,.sp-add-row button{padding:0.3rem 0.5rem;border-radius:0.3rem;font-size:0.78rem;border:1px solid;}
    .sp-add-row button{border:none;cursor:pointer;font-weight:600;}

    /* ─ grade calculator ─ */
    .gc-table{width:100%;border-collapse:collapse;font-size:0.82rem;margin-bottom:6px;}
    .gc-table th{text-align:left;padding:4px 6px;font-size:0.75rem;opacity:0.7;border-bottom:1px solid;}
    .gc-table td{padding:3px 4px;}
    .gc-table input{width:100%;padding:0.3rem;border-radius:0.25rem;border:1px solid;font-size:0.82rem;box-sizing:border-box;}
    .gc-result{font-size:1rem;font-weight:700;text-align:center;padding:0.5rem;border-radius:0.4rem;margin-top:4px;}
    .gc-final{margin-top:6px;padding:0.5rem;border-radius:0.4rem;font-size:0.85rem;}

    /* ─ statistics calculator ─ */
    .stat-input{width:100%;padding:0.4rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;font-family:monospace;resize:vertical;min-height:50px;}
    .stat-results{display:grid;grid-template-columns:1fr 1fr;gap:4px;font-size:0.82rem;}
    .stat-item{padding:0.35rem 0.5rem;border-radius:0.3rem;display:flex;justify-content:space-between;}
    .stat-item .stat-label{opacity:0.7;font-size:0.75rem;}
    .stat-item .stat-val{font-weight:700;font-family:monospace;}
    .stat-hist{height:80px;display:flex;align-items:flex-end;gap:2px;margin-top:6px;padding:4px;border-radius:0.3rem;}
    .stat-bar{flex:1;border-radius:2px 2px 0 0;min-width:6px;transition:height 0.3s;}

    /* ─ matrix calculator ─ */
    .mx-controls{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:6px;align-items:center;}
    .mx-controls select,.mx-controls button{padding:0.3rem 0.5rem;border-radius:0.3rem;font-size:0.8rem;border:1px solid;cursor:pointer;}
    .mx-controls button{border:none;font-weight:600;}
    .mx-area{display:flex;gap:8px;align-items:center;justify-content:center;flex-wrap:wrap;margin-bottom:6px;}
    .mx-grid{display:inline-grid;gap:2px;}
    .mx-grid input{width:48px;padding:0.25rem;text-align:center;border-radius:0.25rem;border:1px solid;font-size:0.82rem;font-family:monospace;}
    .mx-op-label{font-size:1.2rem;font-weight:700;padding:0 6px;}
    .mx-result-grid{display:inline-grid;gap:2px;}
    .mx-result-grid span{width:52px;padding:0.25rem;text-align:center;border-radius:0.25rem;font-size:0.82rem;font-family:monospace;font-weight:600;}

    /* ─ equation balancer ─ */
    .eb-input-row{display:flex;gap:4px;margin-bottom:8px;}
    .eb-input-row input{flex:1;padding:0.45rem;border-radius:0.3rem;border:1px solid;font-size:0.9rem;font-family:monospace;}
    .eb-input-row button{padding:0.4rem 0.8rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.85rem;}
    .eb-result{padding:0.7rem;border-radius:0.4rem;font-family:monospace;font-size:1rem;text-align:center;line-height:1.6;margin-bottom:6px;min-height:2rem;}
    .eb-examples{font-size:0.75rem;opacity:0.6;line-height:1.6;}

    /* ─ data plotter ─ */
    .dp-controls{display:flex;gap:4px;flex-wrap:wrap;margin-bottom:4px;align-items:center;}
    .dp-controls input,.dp-controls select,.dp-controls button{padding:0.3rem 0.5rem;border-radius:0.3rem;font-size:0.8rem;border:1px solid;}
    .dp-controls button{border:none;cursor:pointer;font-weight:600;}
    .dp-canvas{width:100%;flex:1;border-radius:0.4rem;display:block;min-height:180px;}
    .dp-data{width:100%;resize:vertical;min-height:50px;padding:0.4rem;border-radius:0.3rem;border:1px solid;font-size:0.8rem;font-family:monospace;margin-bottom:4px;}

    /* ─ citation generator ─ */
    .cg-form{display:flex;flex-direction:column;gap:6px;margin-bottom:8px;}
    .cg-form input,.cg-form select{padding:0.4rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;}
    .cg-form label{font-size:0.75rem;font-weight:600;opacity:0.7;margin-bottom:-4px;}
    .cg-result{padding:0.6rem;border-radius:0.4rem;font-size:0.85rem;line-height:1.5;font-family:Georgia,serif;min-height:2rem;cursor:pointer;}
    .cg-tabs{display:flex;gap:4px;margin-bottom:6px;}
    .cg-tabs button{padding:0.25rem 0.6rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.8rem;font-weight:600;}

    /* ─ essay outliner ─ */
    .eo-section{margin-bottom:8px;}
    .eo-section-title{font-weight:700;font-size:0.8rem;margin-bottom:4px;display:flex;align-items:center;gap:4px;}
    .eo-section textarea{width:100%;padding:0.35rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;resize:vertical;min-height:40px;box-sizing:border-box;}
    .eo-body-par{margin-bottom:6px;padding:6px;border-radius:0.3rem;}
    .eo-body-par textarea{width:100%;padding:0.3rem;border-radius:0.25rem;border:1px solid;font-size:0.82rem;resize:vertical;min-height:32px;box-sizing:border-box;margin-top:3px;}
    .eo-btns{display:flex;gap:6px;margin-top:4px;}
    .eo-btns button{padding:0.3rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.8rem;}

    /* ─ text tools ─ */
    .tt-area{width:100%;flex:1;resize:none;padding:0.5rem;border-radius:0.35rem;border:1px solid;font-size:0.9rem;min-height:80px;box-sizing:border-box;}
    .tt-stats{display:flex;gap:10px;font-size:0.78rem;opacity:0.7;margin-bottom:4px;}
    .tt-btns{display:flex;gap:4px;flex-wrap:wrap;margin-top:6px;}
    .tt-btns button{padding:0.3rem 0.6rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.75rem;}
    .tt-find-row{display:flex;gap:4px;margin-top:4px;align-items:center;}
    .tt-find-row input{flex:1;padding:0.3rem;border-radius:0.25rem;border:1px solid;font-size:0.8rem;}
    .tt-find-row button{padding:0.3rem 0.5rem;border:none;border-radius:0.25rem;cursor:pointer;font-size:0.75rem;font-weight:600;}

    /* ─ focus sounds ─ */
    .fs-sounds-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:6px;margin-bottom:8px;}
    .fs-sound-btn{padding:0.7rem 0.5rem;border:2px solid transparent;border-radius:0.5rem;cursor:pointer;text-align:center;font-size:0.85rem;font-weight:600;transition:all 0.2s;}
    .fs-sound-btn.active{border-color:currentColor;transform:scale(1.03);}
    .fs-sound-btn .fs-emoji{font-size:1.5rem;display:block;margin-bottom:4px;}
    .fs-vol-row{display:flex;gap:8px;align-items:center;font-size:0.8rem;}
    .fs-vol-row input[type="range"]{flex:1;}

    /* ─ random generator ─ */
    .rg-tabs{display:flex;gap:4px;margin-bottom:8px;flex-wrap:wrap;}
    .rg-tabs button{padding:0.3rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.8rem;font-weight:600;}
    .rg-panel{flex:1;display:flex;flex-direction:column;gap:6px;}
    .rg-result{font-size:1.8rem;font-weight:700;text-align:center;padding:1rem;border-radius:0.5rem;min-height:2rem;margin-bottom:4px;}
    .rg-row{display:flex;gap:4px;align-items:center;}
    .rg-row input,.rg-row button{padding:0.35rem 0.5rem;border-radius:0.3rem;font-size:0.85rem;border:1px solid;}
    .rg-row button{border:none;cursor:pointer;font-weight:600;}
    .rg-list-area{width:100%;min-height:50px;padding:0.4rem;border-radius:0.3rem;border:1px solid;font-size:0.85rem;resize:vertical;}

    /* ─ periodic table ─ */
    .pt-grid{display:grid;grid-template-columns:repeat(18,1fr);gap:1px;width:100%;}
    .pt-cell{display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:3px;cursor:pointer;padding:2px 1px;min-height:0;transition:transform 0.12s,box-shadow 0.12s;line-height:1.15;position:relative;overflow:hidden;}
    .pt-cell:hover{transform:scale(1.35);z-index:5;box-shadow:0 2px 10px rgba(0,0,0,0.35);}
    .pt-cell .pt-num{font-size:0.4em;opacity:0.7;}
    .pt-cell .pt-sym{font-size:0.75em;font-weight:700;}
    .pt-cell .pt-name{font-size:0.32em;opacity:0.6;display:none;}
    .pt-cell.show-name .pt-name{display:block;}
    .pt-spacer{visibility:hidden;}
    .pt-detail{margin-top:8px;padding:8px 10px;border-radius:0.5rem;font-size:0.78rem;line-height:1.5;display:none;}
    .pt-detail.active{display:block;}
    .pt-legend{display:flex;flex-wrap:wrap;gap:4px 8px;margin-bottom:6px;font-size:0.6rem;align-items:center;}
    .pt-legend-swatch{width:10px;height:10px;border-radius:2px;display:inline-block;}
    .pt-search{width:100%;padding:0.3rem 0.5rem;border-radius:0.3rem;border:1px solid;font-size:0.8rem;margin-bottom:6px;}

    /* ─ dark-mode refresh hook (class observer) ─ */
    `;
    document.head.appendChild(STYLE);

    // ─── window registry ──────────────────────────────────
    const openWindows = {};
    let zCounter = 9998;

    // ─── create a tool window ─────────────────────────────
    function createWindow(id, title, emoji, defaultW, defaultH, buildBodyFn) {
        if (openWindows[id]) { openWindows[id].focus(); return; }

        const t = T();
        const vw = window.innerWidth, vh = window.innerHeight;
        const w = Math.round(vw / 6) < defaultW ? defaultW : Math.round(vw / 6);
        const h = Math.round(vh / 6) < defaultH ? defaultH : Math.round(vh / 3);

        const win = document.createElement('div');
        win.className = 'tool-window';
        win.id = 'tool-win-' + id;
        win.style.width  = w + 'px';
        win.style.height = h + 'px';
        // centre on screen offset a bit randomly so multiple don't stack exactly
        win.style.left = Math.max(20, Math.round((vw - w) / 2 + (Math.random() - 0.5) * 120)) + 'px';
        win.style.top  = Math.max(60, Math.round((vh - h) / 2 + (Math.random() - 0.5) * 80)) + 'px';
        win.style.background = t.bg;
        win.style.border = '1px solid ' + t.border;
        zCounter++;
        win.style.zIndex = zCounter;

        // handle
        const handle = document.createElement('div');
        handle.className = 'tw-handle';
        handle.style.background = t.handle;
        handle.innerHTML = `<span>${emoji} ${_t(title)}</span>`;
        const closeBtn = document.createElement('button');
        closeBtn.className = 'tw-close';
        closeBtn.textContent = '✕';
        closeBtn.onclick = () => destroyWindow(id);
        handle.appendChild(closeBtn);
        win.appendChild(handle);

        // body
        const body = document.createElement('div');
        body.className = 'tw-body';
        body.style.background = t.bgAlt;
        body.style.color = t.text;
        win.appendChild(body);

        // resize grip
        const grip = document.createElement('div');
        grip.className = 'tw-resize';
        win.appendChild(grip);

        document.body.appendChild(win);
        openWindows[id] = win;

        // bring to front on click
        win.addEventListener('mousedown', () => { zCounter++; win.style.zIndex = zCounter; });

        // build content
        buildBodyFn(body, t);

        // dragging
        initWindowDrag(win, handle);
        // resizing
        initWindowResize(win, grip);

        // close dropdown
        closeDropdown();
    }

    function destroyWindow(id) {
        const w = openWindows[id];
        if (w) { w.remove(); delete openWindows[id]; }
    }

    // ─── drag logic ───────────────────────────────────────
    function initWindowDrag(win, handle) {
        let dragging = false, ox = 0, oy = 0;
        function start(cx, cy, e) {
            if (e && e.target.closest('.tw-close')) return;
            dragging = true;
            const r = win.getBoundingClientRect();
            ox = cx - r.left; oy = cy - r.top;
            handle.classList.add('grabbing');
        }
        function move(cx, cy) {
            if (!dragging) return;
            let nl = cx - ox, nt = cy - oy;
            nl = Math.max(0, Math.min(nl, window.innerWidth  - win.offsetWidth));
            nt = Math.max(0, Math.min(nt, window.innerHeight - win.offsetHeight));
            win.style.left = nl + 'px'; win.style.top = nt + 'px';
        }
        function stop() { dragging = false; handle.classList.remove('grabbing'); }

        handle.addEventListener('mousedown',  e => start(e.clientX, e.clientY, e));
        handle.addEventListener('touchstart', e => { const t = e.touches[0]; start(t.clientX, t.clientY, e); }, {passive:true});
        document.addEventListener('mousemove', e => move(e.clientX, e.clientY));
        document.addEventListener('touchmove', e => { const t = e.touches[0]; move(t.clientX, t.clientY); }, {passive:true});
        document.addEventListener('mouseup', stop);
        document.addEventListener('touchend', stop);
    }

    // ─── resize logic ─────────────────────────────────────
    function initWindowResize(win, grip) {
        let resizing = false, startX, startY, startW, startH;
        function start(cx, cy) {
            resizing = true;
            startX = cx; startY = cy;
            startW = win.offsetWidth; startH = win.offsetHeight;
        }
        function move(cx, cy) {
            if (!resizing) return;
            let nw = startW + (cx - startX), nh = startH + (cy - startY);
            nw = Math.max(200, nw); nh = Math.max(160, nh);
            win.style.width = nw + 'px'; win.style.height = nh + 'px';
            // dispatch so graph canvas can resize
            win.dispatchEvent(new Event('tool-resize'));
        }
        function stop() { resizing = false; }
        grip.addEventListener('mousedown',  e => { e.preventDefault(); start(e.clientX, e.clientY); });
        grip.addEventListener('touchstart', e => { start(e.touches[0].clientX, e.touches[0].clientY); }, {passive:true});
        document.addEventListener('mousemove', e => move(e.clientX, e.clientY));
        document.addEventListener('touchmove', e => { const t = e.touches[0]; move(t.clientX, t.clientY); }, {passive:true});
        document.addEventListener('mouseup', stop);
        document.addEventListener('touchend', stop);
    }

    // ─── theme refresh for open windows ───────────────────
    function refreshTheme() {
        const t = T();
        Object.values(openWindows).forEach(win => {
            win.style.background = t.bg;
            win.style.borderColor = t.border;
            const body = win.querySelector('.tw-body');
            if (body) { body.style.background = t.bgAlt; body.style.color = t.text; }
        });
        // refresh dropdown too
        const menu = document.getElementById('tools-dropdown-menu');
        if (menu) {
            menu.style.background = t.bg;
            menu.style.borderColor = t.border;
            menu.querySelectorAll('.tools-dd-item').forEach(b => {
                b.style.background = t.bg;
                b.style.color = t.text;
            });
        }
    }
    // observe body class changes for dark-mode toggling
    new MutationObserver(refreshTheme).observe(document.body, { attributes: true, attributeFilter: ['class'] });

    // ═══════════════════════════════════════════════════════
    // TOOL BUILDERS
    // ═══════════════════════════════════════════════════════

    // ── 1. Calculator (Scientific) ──────────────────────────
    function buildCalculator(body, t) {
        // Expression display
        const display = document.createElement('input');
        display.className = 'calc-display';
        display.value = '';
        display.style.background = t.displayBg;
        display.style.color = t.text;
        display.style.borderColor = t.inputBdr;
        display.spellcheck = false;
        display.autocomplete = 'off';
        body.appendChild(display);

        // Sync expr when user types directly in the display
        display.addEventListener('input', () => {
            expr = display.value === '0' ? '' : display.value;
            const val = safeEval(expr);
            resultLine.textContent = expr && !isNaN(val) ? '= ' + val : '';
        });

        // Live result preview
        const resultLine = document.createElement('div');
        resultLine.className = 'calc-result';
        resultLine.style.color = t.textMuted;
        body.appendChild(resultLine);

        const grid = document.createElement('div');
        grid.className = 'calc-grid';
        body.appendChild(grid);

        let expr = '';   // raw expression string
        let lastAns = 0; // last answer for ANS key

        function safeEval(raw) {
            try {
                let s = raw
                    .replace(/×/g, '*').replace(/÷/g, '/')
                    .replace(/\^/g, '**')
                    .replace(/π/g, 'Math.PI').replace(/e(?![xp])/g, 'Math.E')
                    .replace(/\bsin\(/g, 'Math.sin(').replace(/\bcos\(/g, 'Math.cos(')
                    .replace(/\btan\(/g, 'Math.tan(').replace(/\basin\(/g, 'Math.asin(')
                    .replace(/\bacos\(/g, 'Math.acos(').replace(/\batan\(/g, 'Math.atan(')
                    .replace(/\bsqrt\(/g, 'Math.sqrt(').replace(/\bcbrt\(/g, 'Math.cbrt(')
                    .replace(/\babs\(/g, 'Math.abs(').replace(/\blog\(/g, 'Math.log10(')
                    .replace(/\bln\(/g, 'Math.log(').replace(/\bexp\(/g, 'Math.exp(')
                    .replace(/\bfloor\(/g, 'Math.floor(').replace(/\bceil\(/g, 'Math.ceil(')
                    .replace(/\bround\(/g, 'Math.round(')
                    .replace(/ANS/g, String(lastAns))
                    .replace(/(\d+)!/g, '(function f(n){return n<=1?1:n*f(n-1)})($1)');
                const res = new Function('return ' + s)();
                if (!isFinite(res)) return NaN;
                return Math.round(res * 1e12) / 1e12;
            } catch { return NaN; }
        }

        function render(cursorPos) {
            display.value = expr || '0';
            const val = safeEval(expr);
            resultLine.textContent = expr && !isNaN(val) ? '= ' + val : '';
            if (cursorPos != null) {
                display.setSelectionRange(cursorPos, cursorPos);
            } else if (document.activeElement !== display) {
                display.scrollLeft = display.scrollWidth;
            }
        }

        function appendToExpr(text) {
            const start = display.selectionStart ?? expr.length;
            const end = display.selectionEnd ?? expr.length;
            // If display shows '0' placeholder, treat as empty
            if (display.value === '0' && expr === '') {
                expr = text;
                render(text.length);
            } else {
                expr = expr.slice(0, start) + text + expr.slice(end);
                render(start + text.length);
            }
            display.focus();
        }

        function calculate() {
            const val = safeEval(expr);
            if (!isNaN(val)) {
                lastAns = val;
                expr = String(val);
            } else {
                expr = 'Error';
            }
            render(expr.length);
            display.focus();
        }

        // Button layout — 5 columns
        //   label, cssClass, action
        const BTNS = [
            // Row 1: advanced functions
            { l: 'sin',   cls: 'fn', a: () => appendToExpr('sin(') },
            { l: 'cos',   cls: 'fn', a: () => appendToExpr('cos(') },
            { l: 'tan',   cls: 'fn', a: () => appendToExpr('tan(') },
            { l: '(',     cls: 'op', a: () => appendToExpr('(') },
            { l: ')',     cls: 'op', a: () => appendToExpr(')') },
            // Row 2
            { l: 'asin',  cls: 'fn', a: () => appendToExpr('asin(') },
            { l: 'acos',  cls: 'fn', a: () => appendToExpr('acos(') },
            { l: 'atan',  cls: 'fn', a: () => appendToExpr('atan(') },
            { l: '^',     cls: 'op', a: () => appendToExpr('^') },
            { l: '√',     cls: 'op', a: () => appendToExpr('sqrt(') },
            // Row 3
            { l: 'log',   cls: 'fn', a: () => appendToExpr('log(') },
            { l: 'ln',    cls: 'fn', a: () => appendToExpr('ln(') },
            { l: 'exp',   cls: 'fn', a: () => appendToExpr('exp(') },
            { l: 'π',     cls: 'fn', a: () => appendToExpr('π') },
            { l: 'e',     cls: 'fn', a: () => appendToExpr('e') },
            // Row 4
            { l: 'C',     cls: 'op', a: () => { expr = ''; render(); display.focus(); } },
            { l: '⌫',    cls: 'op', a: () => {
                const s = display.selectionStart ?? expr.length;
                const e = display.selectionEnd ?? expr.length;
                if (s !== e) { expr = expr.slice(0, s) + expr.slice(e); render(s); }
                else if (s > 0) { expr = expr.slice(0, s - 1) + expr.slice(s); render(s - 1); }
                display.focus();
            } },
            { l: '%',     cls: 'op', a: () => appendToExpr('%') },
            { l: '!',     cls: 'op', a: () => appendToExpr('!') },
            { l: '÷',     cls: 'op accent', a: () => appendToExpr('÷') },
            // Row 5
            { l: '7', a: () => appendToExpr('7') },
            { l: '8', a: () => appendToExpr('8') },
            { l: '9', a: () => appendToExpr('9') },
            { l: 'ANS', cls: 'fn', a: () => appendToExpr('ANS') },
            { l: '×',     cls: 'op accent', a: () => appendToExpr('×') },
            // Row 6
            { l: '4', a: () => appendToExpr('4') },
            { l: '5', a: () => appendToExpr('5') },
            { l: '6', a: () => appendToExpr('6') },
            { l: '±',     cls: 'op', a: () => { expr = expr ? '(-' + expr + ')' : '-'; render(expr.length); display.focus(); } },
            { l: '-',     cls: 'op accent', a: () => appendToExpr('-') },
            // Row 7
            { l: '1', a: () => appendToExpr('1') },
            { l: '2', a: () => appendToExpr('2') },
            { l: '3', a: () => appendToExpr('3') },
            { l: 'abs',  cls: 'fn', a: () => appendToExpr('abs(') },
            { l: '+',     cls: 'op accent', a: () => appendToExpr('+') },
            // Row 8
            { l: '0', wide: true, a: () => appendToExpr('0') },
            { l: '.', a: () => appendToExpr('.') },
            { l: '=', wide: true, cls: 'op accent', a: calculate },
        ];

        BTNS.forEach(({ l, cls, a, wide }) => {
            const btn = document.createElement('button');
            btn.className = 'calc-btn' + (cls ? ' ' + cls.split(' ').map(c => c === 'accent' ? '' : c).join(' ').trim() : '');
            btn.textContent = l;
            if (wide) btn.classList.add('wide');
            const isAccent = cls && cls.includes('accent');
            const isOp = cls && cls.includes('op');
            btn.style.background = isAccent ? t.accent : isOp ? (isDark() ? '#475569' : '#d1d5db') : t.btnBg;
            btn.style.color = isAccent ? '#fff' : t.text;
            btn.addEventListener('click', a);
            grid.appendChild(btn);
        });

        // ── Keyboard input support ──
        function pressBtn(label) {
            const btn = Array.from(grid.querySelectorAll('.calc-btn')).find(b => b.textContent === label);
            if (btn) { btn.click(); btn.style.filter = 'brightness(0.75)'; setTimeout(() => btn.style.filter = '', 120); }
        }
        const keyMap = {
            '0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9',
            '.':'.', '+':'+', '-':'-', '*':'×', '/':'÷', 'x':'×', 'X':'×',
            '^':'^', '(':' (', ')':')',
            'Enter':'=', '=':'=', 'Escape':'C', 'Delete':'C', '%':'%',
        };

        function handleCalcKey(e) {
            const win = body.closest('.tool-window');
            if (!win || (!win.offsetParent && win.style.display === 'none')) return;

            // When display is focused, let the input handle most keys natively
            if (document.activeElement === display) {
                if (e.key === 'Enter' || (e.key === '=' && !e.shiftKey)) {
                    e.preventDefault();
                    calculate();
                    display.focus();
                    display.setSelectionRange(display.value.length, display.value.length);
                    return;
                }
                if (e.key === 'Escape') { e.preventDefault(); expr = ''; render(); display.focus(); return; }
                // Let arrows, backspace, delete, home, end, selection etc. work naturally
                return;
            }

            // Display is NOT focused — original global shortcut behavior
            const tag = document.activeElement && document.activeElement.tagName;
            if (tag === 'INPUT' || tag === 'TEXTAREA') return;
            const mapped = keyMap[e.key];
            if (mapped) {
                e.preventDefault();
                pressBtn(mapped.trim());
                return;
            }
            if (e.key === 'Backspace') {
                e.preventDefault();
                pressBtn('⌫');
            }
        }
        document.addEventListener('keydown', handleCalcKey);

        // ── Responsive scaling on window resize ──
        const BASE_W = 340; // default calculator width
        function scaleCalc() {
            const win = body.closest('.tool-window');
            if (!win) return;
            const w = win.offsetWidth;
            const s = Math.max(0.65, Math.min(w / BASE_W, 2.0)); // clamp scale between 0.65x and 2x
            display.style.fontSize = (1.2 * s) + 'rem';
            display.style.padding = (0.5 * s) + 'rem ' + (0.6 * s) + 'rem';
            resultLine.style.fontSize = (0.8 * s) + 'rem';
            grid.style.gap = (3 * s) + 'px';
            grid.querySelectorAll('.calc-btn').forEach(btn => {
                const isFn = btn.classList.contains('fn');
                btn.style.fontSize = ((isFn ? 0.75 : 0.82) * s) + 'rem';
                btn.style.padding = (0.4 * s) + 'rem ' + (0.1 * s) + 'rem';
                btn.style.borderRadius = (0.35 * s) + 'rem';
            });
        }
        const win = body.closest('.tool-window');
        if (win) win.addEventListener('tool-resize', scaleCalc);

        // Clean up listener when window is destroyed
        const observer = new MutationObserver(() => {
            if (!document.contains(body)) { document.removeEventListener('keydown', handleCalcKey); observer.disconnect(); }
        });
        observer.observe(document.body, { childList: true, subtree: true });
    }

    // ── 2. Graphing Calculator ────────────────────────────
    function buildGraph(body, t) {
        const row = document.createElement('div');
        row.className = 'graph-input-row';
        const input = document.createElement('input');
        input.placeholder = 'y = sin(x)';
        input.value = 'sin(x)';
        input.style.background = t.inputBg; input.style.color = t.text; input.style.borderColor = t.inputBdr;
        const plotBtn = document.createElement('button');
        plotBtn.textContent = _t('Plot');
        plotBtn.style.background = t.accent; plotBtn.style.color = '#fff';
        row.appendChild(input); row.appendChild(plotBtn);
        body.appendChild(row);

        const info = document.createElement('div');
        info.style.cssText = 'font-size:0.75rem;margin-bottom:4px;color:' + t.textMuted;
        info.textContent = 'Supports: sin, cos, tan, abs, sqrt, log, exp, pi, e, ^';
        body.appendChild(info);

        const canvas = document.createElement('canvas');
        canvas.style.cssText = 'width:100%;flex:1;border-radius:0.3rem;border:1px solid ' + t.border + ';background:' + t.displayBg;
        body.appendChild(canvas);

        function draw() {
            const ctx = canvas.getContext('2d');
            const rect = canvas.getBoundingClientRect();
            canvas.width = rect.width * (window.devicePixelRatio || 1);
            canvas.height = rect.height * (window.devicePixelRatio || 1);
            ctx.setTransform(window.devicePixelRatio || 1, 0, 0, window.devicePixelRatio || 1, 0, 0);
            const W = rect.width, H = rect.height;

            // clear
            ctx.fillStyle = t.displayBg;
            ctx.fillRect(0, 0, W, H);

            // ranges
            const xMin = -10, xMax = 10, yMin = -6, yMax = 6;
            const toX = x => (x - xMin) / (xMax - xMin) * W;
            const toY = y => H - (y - yMin) / (yMax - yMin) * H;

            // grid
            ctx.strokeStyle = isDark() ? 'rgba(148,163,184,0.15)' : 'rgba(0,0,0,0.08)';
            ctx.lineWidth = 1;
            for (let gx = Math.ceil(xMin); gx <= Math.floor(xMax); gx++) {
                ctx.beginPath(); ctx.moveTo(toX(gx), 0); ctx.lineTo(toX(gx), H); ctx.stroke();
            }
            for (let gy = Math.ceil(yMin); gy <= Math.floor(yMax); gy++) {
                ctx.beginPath(); ctx.moveTo(0, toY(gy)); ctx.lineTo(W, toY(gy)); ctx.stroke();
            }

            // axes
            ctx.strokeStyle = isDark() ? '#94a3b8' : '#64748b';
            ctx.lineWidth = 1.5;
            ctx.beginPath(); ctx.moveTo(toX(xMin), toY(0)); ctx.lineTo(toX(xMax), toY(0)); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(toX(0), toY(yMin)); ctx.lineTo(toX(0), toY(yMax)); ctx.stroke();

            // axis labels
            ctx.fillStyle = t.textMuted;
            ctx.font = '10px monospace';
            for (let gx = Math.ceil(xMin); gx <= Math.floor(xMax); gx++) {
                if (gx === 0) continue;
                ctx.fillText(gx, toX(gx) - 4, toY(0) + 12);
            }
            for (let gy = Math.ceil(yMin); gy <= Math.floor(yMax); gy++) {
                if (gy === 0) continue;
                ctx.fillText(gy, toX(0) + 4, toY(gy) + 4);
            }

            // parse & plot
            let expr = input.value.trim();
            try {
                // sanitize: allow math tokens
                const safe = expr
                    .replace(/\^/g, '**')
                    .replace(/\bsin\b/g, 'Math.sin')
                    .replace(/\bcos\b/g, 'Math.cos')
                    .replace(/\btan\b/g, 'Math.tan')
                    .replace(/\babs\b/g, 'Math.abs')
                    .replace(/\bsqrt\b/g, 'Math.sqrt')
                    .replace(/\blog\b/g, 'Math.log')
                    .replace(/\bexp\b/g, 'Math.exp')
                    .replace(/\bpi\b/g, 'Math.PI')
                    .replace(/\be\b/g, 'Math.E');
                const fn = new Function('x', 'return ' + safe);

                ctx.strokeStyle = '#3b82f6';
                ctx.lineWidth = 2;
                ctx.beginPath();
                let started = false;
                const steps = Math.max(400, W * 2);
                for (let i = 0; i <= steps; i++) {
                    const x = xMin + (xMax - xMin) * i / steps;
                    const y = fn(x);
                    if (!isFinite(y) || Math.abs(y) > 1e6) { started = false; continue; }
                    const px = toX(x), py = toY(y);
                    if (!started) { ctx.moveTo(px, py); started = true; } else { ctx.lineTo(px, py); }
                }
                ctx.stroke();
            } catch (e) { /* ignore parse errors */ }
        }

        plotBtn.addEventListener('click', draw);
        input.addEventListener('keypress', e => { if (e.key === 'Enter') draw(); });

        // redraw on resize
        const win = body.closest('.tool-window');
        if (win) win.addEventListener('tool-resize', () => requestAnimationFrame(draw));

        // initial draw after layout
        requestAnimationFrame(() => requestAnimationFrame(draw));
    }

    // ── 3. AI Agent (opens existing AI overlay) ───────────
    function openAIAgent() {
        // If the existing AI assistant overlay exists, toggle it
        const overlay = document.getElementById('ai-chat-overlay');
        if (overlay) {
            overlay.style.display = overlay.style.display === 'none' ? 'flex' : 'none';
            closeDropdown();
            return;
        }
        // If AI button exists, click it to trigger ai_assistant.js init
        const aiBtn = document.getElementById('ai-assistant-button');
        if (aiBtn) { aiBtn.click(); closeDropdown(); return; }
        // fallback: open as a tool window with a message
        createWindow('ai-agent', 'AI Agent', '🤖', 360, 320, (body, t) => {
            body.innerHTML = `<div style="text-align:center;padding:2rem;color:${t.textMuted};">
                <div style="font-size:3rem;margin-bottom:1rem;">🤖</div>
                <p>${_t('AI Agent is loading…')}</p>
                <p style="font-size:0.8rem;margin-top:0.5rem;">${_t('The AI tutor will be available once the page fully loads.')}</p>
            </div>`;
        });
    }

    // ── 4. Timer ──────────────────────────────────────────
    function buildTimer(body, t) {
        let seconds = 0, running = false, interval = null, mode = 'stopwatch';  // 'stopwatch' | 'countdown'
        let countdownTarget = 0;

        const modeRow = document.createElement('div');
        modeRow.style.cssText = 'display:flex;gap:4px;margin-bottom:8px;justify-content:center;';
        ['Stopwatch','Countdown'].forEach(m => {
            const b = document.createElement('button');
            b.textContent = _t(m);
            b.style.cssText = `padding:0.3rem 0.8rem;border:1px solid ${t.inputBdr};border-radius:0.3rem;cursor:pointer;font-size:0.8rem;background:${m==='Stopwatch'?t.accent:t.btnBg};color:${m==='Stopwatch'?'#fff':t.text};font-weight:600;`;
            b.addEventListener('click', () => {
                reset();
                mode = m.toLowerCase();
                modeRow.querySelectorAll('button').forEach(x => {
                    x.style.background = x === b ? t.accent : t.btnBg;
                    x.style.color = x === b ? '#fff' : t.text;
                });
                cdRow.style.display = mode === 'countdown' ? 'flex' : 'none';
            });
            modeRow.appendChild(b);
        });
        body.appendChild(modeRow);

        // countdown input row
        const cdRow = document.createElement('div');
        cdRow.style.cssText = 'display:none;gap:4px;margin-bottom:8px;justify-content:center;align-items:center;';
        const cdInput = document.createElement('input');
        cdInput.type = 'number'; cdInput.min = 1; cdInput.value = 60; cdInput.placeholder = 'sec';
        cdInput.style.cssText = `width:80px;padding:0.3rem 0.5rem;border-radius:0.3rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:0.85rem;text-align:center;`;
        const cdLabel = document.createElement('span');
        cdLabel.textContent = _t('seconds');
        cdLabel.style.fontSize = '0.8rem';
        cdRow.appendChild(cdInput); cdRow.appendChild(cdLabel);
        body.appendChild(cdRow);

        const disp = document.createElement('div');
        disp.className = 'timer-display';
        disp.textContent = '00:00:00';
        disp.style.color = t.text;
        body.appendChild(disp);

        function fmtTime(s) {
            const h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
            return [h,m,sec].map(v => String(v).padStart(2,'0')).join(':');
        }
        function render() { disp.textContent = fmtTime(seconds); }

        function tick() {
            if (mode === 'stopwatch') { seconds++; render(); }
            else {
                seconds--;
                if (seconds <= 0) {
                    seconds = 0; render(); stop();
                    disp.style.color = '#ef4444';
                    // brief flash / alert
                    try { new Audio('data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEAESsAABErAAABAAgAZGF0YQAAAAA=').play(); } catch(e){}
                    setTimeout(() => { disp.style.color = t.text; }, 2000);
                    return;
                }
                render();
            }
        }

        function startTimer() {
            if (running) return;
            if (mode === 'countdown' && seconds === 0) {
                seconds = Math.max(1, parseInt(cdInput.value) || 60);
                render();
            }
            running = true;
            interval = setInterval(tick, 1000);
        }
        function stop() { running = false; clearInterval(interval); interval = null; }
        function reset() { stop(); seconds = mode === 'countdown' ? 0 : 0; render(); disp.style.color = t.text; }

        const btns = document.createElement('div');
        btns.className = 'timer-btns';
        [
            { label: '▶ ' + _t('Start'), fn: startTimer, accent: true },
            { label: '⏸ ' + _t('Pause'), fn: stop },
            { label: '↺ ' + _t('Reset'), fn: reset }
        ].forEach(({ label, fn, accent }) => {
            const b = document.createElement('button');
            b.textContent = label;
            b.style.background = accent ? t.accent : t.btnBg;
            b.style.color = accent ? '#fff' : t.text;
            b.addEventListener('click', fn);
            btns.appendChild(b);
        });
        body.appendChild(btns);
    }

    // ── 5. Notepad ────────────────────────────────────────
    function buildNotepad(body, t) {
        const STORAGE_KEY = 'arisEdu-notepad';

        const header = document.createElement('div');
        header.style.cssText = 'display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;';
        const title = document.createElement('span');
        title.textContent = '📝 ' + _t('Quick Notes');
        title.style.cssText = 'font-weight:600;font-size:0.85rem;';
        const charCount = document.createElement('span');
        charCount.style.cssText = 'font-size:0.75rem;color:' + t.textMuted;
        header.appendChild(title);
        header.appendChild(charCount);
        body.appendChild(header);

        const area = document.createElement('textarea');
        area.className = 'notepad-area';
        area.placeholder = _t('Type your notes here…');
        area.style.background = t.inputBg;
        area.style.color = t.text;
        area.style.borderColor = t.inputBdr;
        area.value = localStorage.getItem(STORAGE_KEY) || '';
        body.appendChild(area);

        function updateCount() { charCount.textContent = area.value.length + ' chars'; }
        updateCount();

        area.addEventListener('input', () => {
            localStorage.setItem(STORAGE_KEY, area.value);
            updateCount();
        });

        const btnRow = document.createElement('div');
        btnRow.style.cssText = 'display:flex;gap:6px;margin-top:6px;';
        
        const clearBtn = document.createElement('button');
        clearBtn.textContent = _t('Clear');
        clearBtn.style.cssText = `padding:0.3rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.8rem;background:${t.btnBg};color:${t.text};font-weight:600;`;
        clearBtn.addEventListener('click', () => { area.value = ''; localStorage.removeItem(STORAGE_KEY); updateCount(); });

        const copyBtn = document.createElement('button');
        copyBtn.textContent = _t('Copy All');
        copyBtn.style.cssText = `padding:0.3rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-size:0.8rem;background:${t.accent};color:#fff;font-weight:600;`;
        copyBtn.addEventListener('click', () => {
            navigator.clipboard.writeText(area.value).then(() => {
                copyBtn.textContent = '✓ Copied!';
                setTimeout(() => { copyBtn.textContent = _t('Copy All'); }, 1200);
            });
        });

        btnRow.appendChild(clearBtn);
        btnRow.appendChild(copyBtn);
        body.appendChild(btnRow);
    }

    // ── 6. Unit Converter ─────────────────────────────────
    function buildUnitConverter(body, t) {
        const UNITS = {
            Length: {
                m:1, km:1000, cm:0.01, mm:0.001, mi:1609.344, yd:0.9144, ft:0.3048, in_:0.0254
            },
            Mass: {
                kg:1, g:0.001, mg:0.000001, lb:0.453592, oz:0.0283495, ton:907.185
            },
            Temperature: { '°C':'C', '°F':'F', K:'K' },
            Volume: {
                L:1, mL:0.001, gal:3.78541, qt:0.946353, cup:0.236588, fl_oz:0.0295735
            },
            Speed: {
                'm/s':1, 'km/h':0.277778, 'mph':0.44704, 'ft/s':0.3048, knot:0.514444
            },
            Energy: {
                J:1, kJ:1000, cal:4.184, kcal:4184, eV:1.602e-19, kWh:3.6e6
            }
        };

        const catSel = document.createElement('select');
        catSel.style.cssText = `width:100%;padding:0.45rem;border-radius:0.4rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:0.9rem;margin-bottom:8px;`;
        Object.keys(UNITS).forEach(c => { const o = document.createElement('option'); o.textContent = c; o.value = c; catSel.appendChild(o); });
        body.appendChild(catSel);

        const row = document.createElement('div');
        row.className = 'uc-row';
        body.appendChild(row);

        const fromSel = document.createElement('select');
        const toSel = document.createElement('select');
        [fromSel, toSel].forEach(s => {
            s.style.cssText = `flex:1;padding:0.4rem;border-radius:0.4rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:0.85rem;`;
        });
        const swapBtn = document.createElement('button');
        swapBtn.className = 'uc-swap';
        swapBtn.textContent = '⇄';
        swapBtn.style.background = t.accent;
        swapBtn.style.color = '#fff';
        row.appendChild(fromSel);
        row.appendChild(swapBtn);
        row.appendChild(toSel);

        const valInput = document.createElement('input');
        valInput.type = 'number';
        valInput.value = '1';
        valInput.style.cssText = `width:100%;padding:0.5rem;border-radius:0.4rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:1rem;margin-top:8px;box-sizing:border-box;`;
        body.appendChild(valInput);

        const result = document.createElement('div');
        result.className = 'uc-result';
        result.style.background = isDark() ? '#1e293b' : '#f0f9ff';
        result.style.color = t.text;
        result.style.borderColor = t.accent;
        body.appendChild(result);

        function populateUnits() {
            const cat = catSel.value;
            const keys = Object.keys(UNITS[cat]);
            [fromSel, toSel].forEach((s, i) => {
                s.innerHTML = '';
                keys.forEach((k, j) => {
                    const o = document.createElement('option');
                    o.value = k; o.textContent = k.replace('in_', 'in').replace('fl_oz', 'fl oz');
                    s.appendChild(o);
                });
                if (keys.length > 1 && i === 1) s.selectedIndex = 1;
            });
        }

        function convertTemp(val, from, to) {
            if (from === to) return val;
            // Convert to Celsius first
            let c = val;
            if (from === '°F') c = (val - 32) * 5 / 9;
            else if (from === 'K') c = val - 273.15;
            // Convert from Celsius to target
            if (to === '°F') return c * 9 / 5 + 32;
            if (to === 'K') return c + 273.15;
            return c;
        }

        function convert() {
            const cat = catSel.value;
            const val = parseFloat(valInput.value);
            if (isNaN(val)) { result.textContent = '—'; return; }
            let res;
            if (cat === 'Temperature') {
                res = convertTemp(val, fromSel.value, toSel.value);
            } else {
                const fromFactor = UNITS[cat][fromSel.value];
                const toFactor = UNITS[cat][toSel.value];
                res = val * fromFactor / toFactor;
            }
            const display = (Math.abs(res) > 1e6 || (Math.abs(res) < 0.001 && res !== 0))
                ? res.toExponential(4) : parseFloat(res.toPrecision(8));
            result.innerHTML = `<strong style="font-size:1.3rem;">${display}</strong> <span style="opacity:0.7;">${toSel.value.replace('in_','in').replace('fl_oz','fl oz')}</span>`;
        }

        catSel.addEventListener('change', () => { populateUnits(); convert(); });
        fromSel.addEventListener('change', convert);
        toSel.addEventListener('change', convert);
        valInput.addEventListener('input', convert);
        swapBtn.addEventListener('click', () => {
            const tmp = fromSel.selectedIndex;
            fromSel.selectedIndex = toSel.selectedIndex;
            toSel.selectedIndex = tmp;
            convert();
        });

        populateUnits();
        convert();
    }

    // ── 7. Formula Sheet ──────────────────────────────────
    function buildFormulaSheet(body, t) {
        const FORMULAS = {
            Algebra: [
                { title: 'Quadratic Formula', formula: 'x = (-b ± √(b²-4ac)) / 2a' },
                { title: 'Slope', formula: 'm = (y₂ - y₁) / (x₂ - x₁)' },
                { title: 'Slope-Intercept', formula: 'y = mx + b' },
                { title: 'Point-Slope', formula: 'y - y₁ = m(x - x₁)' },
                { title: 'Distance', formula: 'd = √((x₂-x₁)² + (y₂-y₁)²)' },
                { title: 'Midpoint', formula: 'M = ((x₁+x₂)/2, (y₁+y₂)/2)' },
                { title: 'Exponent Rule', formula: 'aⁿ · aᵐ = aⁿ⁺ᵐ' },
                { title: 'Log Rule', formula: 'log_b(xy) = log_b(x) + log_b(y)' },
            ],
            Geometry: [
                { title: 'Area of Circle', formula: 'A = πr²' },
                { title: 'Circumference', formula: 'C = 2πr' },
                { title: 'Area of Triangle', formula: 'A = ½ · b · h' },
                { title: 'Pythagorean', formula: 'a² + b² = c²' },
                { title: 'Area of Rect', formula: 'A = l × w' },
                { title: 'Vol of Sphere', formula: 'V = (4/3)πr³' },
                { title: 'Vol of Cylinder', formula: 'V = πr²h' },
                { title: 'Surface Area Sphere', formula: 'SA = 4πr²' },
            ],
            Trig: [
                { title: 'SOH-CAH-TOA', formula: 'sin=O/H  cos=A/H  tan=O/A' },
                { title: 'Pythagorean Identity', formula: 'sin²θ + cos²θ = 1' },
                { title: 'Law of Sines', formula: 'a/sinA = b/sinB = c/sinC' },
                { title: 'Law of Cosines', formula: 'c² = a² + b² - 2ab·cosC' },
                { title: 'Double Angle (sin)', formula: 'sin2θ = 2sinθcosθ' },
                { title: 'Double Angle (cos)', formula: 'cos2θ = cos²θ - sin²θ' },
                { title: 'Unit Circle 30°', formula: 'sin30°=½  cos30°=√3/2' },
                { title: 'Unit Circle 45°', formula: 'sin45°=√2/2  cos45°=√2/2' },
            ],
            Physics: [
                { title: 'Velocity', formula: 'v = d / t' },
                { title: 'Acceleration', formula: 'a = Δv / Δt' },
                { title: 'Newton\'s 2nd', formula: 'F = ma' },
                { title: 'Kinetic Energy', formula: 'KE = ½mv²' },
                { title: 'Potential Energy', formula: 'PE = mgh' },
                { title: 'Work', formula: 'W = F · d · cosθ' },
                { title: 'Ohm\'s Law', formula: 'V = IR' },
                { title: 'Power', formula: 'P = IV = W/t' },
            ],
            Chemistry: [
                { title: 'Ideal Gas', formula: 'PV = nRT' },
                { title: 'Density', formula: 'ρ = m / V' },
                { title: 'Molarity', formula: 'M = mol / L' },
                { title: 'pH', formula: 'pH = -log[H⁺]' },
                { title: 'Dilution', formula: 'M₁V₁ = M₂V₂' },
                { title: 'Avogadro\'s #', formula: 'N_A = 6.022 × 10²³' },
                { title: 'Speed of Light', formula: 'c = 3.0 × 10⁸ m/s' },
                { title: 'E = mc²', formula: 'Energy = mass × c²' },
            ]
        };

        const tabs = document.createElement('div');
        tabs.className = 'fs-tabs';
        body.appendChild(tabs);

        const content = document.createElement('div');
        content.style.cssText = 'flex:1;overflow-y:auto;';
        body.appendChild(content);

        let activeTab = null;

        function renderTab(cat) {
            activeTab = cat;
            tabs.querySelectorAll('.fs-tab').forEach(tb => tb.classList.toggle('active', tb.dataset.cat === cat));
            content.innerHTML = '';
            FORMULAS[cat].forEach(f => {
                const card = document.createElement('div');
                card.className = 'fs-card';
                card.style.background = isDark() ? '#1e293b' : '#f8fafc';
                card.style.borderColor = t.border;
                card.style.color = t.text;
                card.innerHTML = `<div style="font-weight:600;font-size:0.8rem;opacity:0.7;margin-bottom:2px;">${f.title}</div><div style="font-size:0.95rem;font-family:monospace;letter-spacing:0.3px;">${f.formula}</div>`;
                content.appendChild(card);
            });
        }

        Object.keys(FORMULAS).forEach((cat, i) => {
            const tb = document.createElement('button');
            tb.className = 'fs-tab';
            tb.dataset.cat = cat;
            tb.textContent = cat;
            tb.style.color = t.text;
            tb.addEventListener('click', () => renderTab(cat));
            tabs.appendChild(tb);
        });

        renderTab('Algebra');
    }

    // ── 8. Flashcard Maker ────────────────────────────────
    function buildFlashcards(body, t) {
        const STORAGE_KEY = 'arisEdu-flashcards';
        let cards = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
        let idx = 0;
        let flipped = false;

        // Input row
        const inputRow = document.createElement('div');
        inputRow.className = 'fc-input-row';
        const frontIn = document.createElement('input');
        frontIn.placeholder = _t('Front (question)');
        const backIn = document.createElement('input');
        backIn.placeholder = _t('Back (answer)');
        [frontIn, backIn].forEach(inp => {
            inp.style.cssText = `flex:1;padding:0.4rem;border-radius:0.3rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:0.85rem;`;
        });
        const addBtn = document.createElement('button');
        addBtn.textContent = '+';
        addBtn.style.cssText = `padding:0.4rem 0.7rem;border:none;border-radius:0.3rem;background:${t.accent};color:#fff;font-weight:700;font-size:1rem;cursor:pointer;`;
        inputRow.appendChild(frontIn);
        inputRow.appendChild(backIn);
        inputRow.appendChild(addBtn);
        body.appendChild(inputRow);

        // Card display area
        const cardArea = document.createElement('div');
        cardArea.style.cssText = 'flex:1;display:flex;align-items:center;justify-content:center;position:relative;';
        body.appendChild(cardArea);

        const card = document.createElement('div');
        card.className = 'fc-card';
        card.style.background = isDark() ? '#1e293b' : '#f0f9ff';
        card.style.color = t.text;
        card.style.borderColor = t.accent;
        cardArea.appendChild(card);

        // Navigation
        const nav = document.createElement('div');
        nav.className = 'fc-nav';
        const prevBtn = document.createElement('button');
        prevBtn.textContent = '◀';
        const counter = document.createElement('span');
        counter.className = 'fc-count';
        counter.style.color = t.textMuted;
        const nextBtn = document.createElement('button');
        nextBtn.textContent = '▶';
        const delBtn = document.createElement('button');
        delBtn.textContent = '🗑️';
        delBtn.title = 'Delete card';
        [prevBtn, nextBtn, delBtn].forEach(b => {
            b.style.cssText = `padding:0.35rem 0.7rem;border:none;border-radius:0.3rem;background:${t.btnBg};color:${t.text};cursor:pointer;font-size:0.9rem;`;
        });
        nav.appendChild(prevBtn);
        nav.appendChild(counter);
        nav.appendChild(nextBtn);
        nav.appendChild(delBtn);
        body.appendChild(nav);

        function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(cards)); }

        function render() {
            if (cards.length === 0) {
                card.innerHTML = `<div style="opacity:0.5;font-size:0.9rem;">No cards yet.<br>Add one above!</div>`;
                counter.textContent = '0 / 0';
                return;
            }
            idx = Math.max(0, Math.min(idx, cards.length - 1));
            flipped = false;
            card.innerHTML = `<div style="font-size:0.75rem;opacity:0.5;margin-bottom:6px;">FRONT — click to flip</div><div style="font-size:1.1rem;font-weight:600;">${cards[idx].front}</div>`;
            counter.textContent = (idx + 1) + ' / ' + cards.length;
        }

        card.addEventListener('click', () => {
            if (cards.length === 0) return;
            flipped = !flipped;
            if (flipped) {
                card.innerHTML = `<div style="font-size:0.75rem;opacity:0.5;margin-bottom:6px;">BACK — click to flip</div><div style="font-size:1.1rem;font-weight:600;">${cards[idx].back}</div>`;
            } else {
                card.innerHTML = `<div style="font-size:0.75rem;opacity:0.5;margin-bottom:6px;">FRONT — click to flip</div><div style="font-size:1.1rem;font-weight:600;">${cards[idx].front}</div>`;
            }
        });

        addBtn.addEventListener('click', () => {
            const f = frontIn.value.trim(), b = backIn.value.trim();
            if (!f || !b) return;
            cards.push({ front: f, back: b });
            save();
            idx = cards.length - 1;
            frontIn.value = ''; backIn.value = '';
            render();
        });
        frontIn.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); backIn.focus(); } });
        backIn.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); addBtn.click(); } });
        prevBtn.addEventListener('click', () => { if (idx > 0) { idx--; render(); } });
        nextBtn.addEventListener('click', () => { if (idx < cards.length - 1) { idx++; render(); } });
        delBtn.addEventListener('click', () => {
            if (cards.length === 0) return;
            cards.splice(idx, 1);
            save();
            if (idx >= cards.length) idx = cards.length - 1;
            render();
        });

        render();
    }

    // ── 9. Whiteboard ─────────────────────────────────────
    function buildWhiteboard(body, t) {
        body.style.display = 'flex';
        body.style.flexDirection = 'column';

        // Toolbar
        const toolbar = document.createElement('div');
        toolbar.className = 'wb-toolbar';
        body.appendChild(toolbar);

        const colorPicker = document.createElement('input');
        colorPicker.type = 'color';
        colorPicker.value = isDark() ? '#ffffff' : '#000000';
        colorPicker.style.cssText = 'width:32px;height:28px;border:none;cursor:pointer;background:none;';
        toolbar.appendChild(colorPicker);

        const sizeLabel = document.createElement('span');
        sizeLabel.style.cssText = 'font-size:0.75rem;opacity:0.7;color:' + t.text;
        sizeLabel.textContent = '3px';
        const sizeSlider = document.createElement('input');
        sizeSlider.type = 'range';
        sizeSlider.min = '1'; sizeSlider.max = '20'; sizeSlider.value = '3';
        sizeSlider.style.cssText = 'width:70px;';
        sizeSlider.addEventListener('input', () => { sizeLabel.textContent = sizeSlider.value + 'px'; });
        toolbar.appendChild(sizeSlider);
        toolbar.appendChild(sizeLabel);

        const eraserBtn = document.createElement('button');
        eraserBtn.textContent = '🧹';
        eraserBtn.title = 'Eraser';
        eraserBtn.style.cssText = `padding:0.25rem 0.5rem;border:1px solid ${t.border};border-radius:0.3rem;background:${t.btnBg};color:${t.text};cursor:pointer;font-size:0.85rem;`;
        let erasing = false;
        eraserBtn.addEventListener('click', () => {
            erasing = !erasing;
            eraserBtn.style.background = erasing ? t.accent : t.btnBg;
            eraserBtn.style.color = erasing ? '#fff' : t.text;
        });
        toolbar.appendChild(eraserBtn);

        const clearBtn = document.createElement('button');
        clearBtn.textContent = _t('Clear');
        clearBtn.style.cssText = `padding:0.25rem 0.5rem;border:none;border-radius:0.3rem;background:${t.accent};color:#fff;cursor:pointer;font-size:0.8rem;font-weight:600;`;
        toolbar.appendChild(clearBtn);

        const saveBtn = document.createElement('button');
        saveBtn.textContent = '💾';
        saveBtn.title = 'Save as image';
        saveBtn.style.cssText = `padding:0.25rem 0.5rem;border:1px solid ${t.border};border-radius:0.3rem;background:${t.btnBg};color:${t.text};cursor:pointer;font-size:0.85rem;`;
        toolbar.appendChild(saveBtn);

        // Canvas
        const canvasWrap = document.createElement('div');
        canvasWrap.style.cssText = 'flex:1;position:relative;overflow:hidden;border-radius:0.3rem;';
        body.appendChild(canvasWrap);

        const canvas = document.createElement('canvas');
        canvas.className = 'wb-canvas';
        canvas.style.background = isDark() ? '#1a2332' : '#ffffff';
        canvasWrap.appendChild(canvas);
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            const saved = canvas.toDataURL();
            canvas.width = canvasWrap.offsetWidth;
            canvas.height = canvasWrap.offsetHeight;
            const img = new Image();
            img.onload = () => { ctx.drawImage(img, 0, 0); };
            img.src = saved;
        }
        setTimeout(resizeCanvas, 50);
        const win = body.closest('.tool-window');
        if (win) win.addEventListener('tool-resize', () => setTimeout(resizeCanvas, 30));

        let drawing = false;
        let lastX = 0, lastY = 0;

        function getPos(e) {
            const r = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            return [clientX - r.left, clientY - r.top];
        }

        function startDraw(e) {
            drawing = true;
            [lastX, lastY] = getPos(e);
        }
        function draw(e) {
            if (!drawing) return;
            e.preventDefault();
            const [x, y] = getPos(e);
            ctx.beginPath();
            ctx.moveTo(lastX, lastY);
            ctx.lineTo(x, y);
            ctx.strokeStyle = erasing ? (isDark() ? '#1a2332' : '#ffffff') : colorPicker.value;
            ctx.lineWidth = parseInt(sizeSlider.value);
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';
            ctx.stroke();
            [lastX, lastY] = [x, y];
        }
        function stopDraw() { drawing = false; }

        canvas.addEventListener('mousedown', startDraw);
        canvas.addEventListener('mousemove', draw);
        canvas.addEventListener('mouseup', stopDraw);
        canvas.addEventListener('mouseleave', stopDraw);
        canvas.addEventListener('touchstart', startDraw, { passive: false });
        canvas.addEventListener('touchmove', draw, { passive: false });
        canvas.addEventListener('touchend', stopDraw);

        clearBtn.addEventListener('click', () => {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
        });
        saveBtn.addEventListener('click', () => {
            const a = document.createElement('a');
            a.download = 'whiteboard.png';
            a.href = canvas.toDataURL('image/png');
            a.click();
        });
    }

    // ── 10. To-Do List ────────────────────────────────────
    function buildTodoList(body, t) {
        const STORAGE_KEY = 'arisEdu-todolist';
        let items = JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');

        // Input row
        const inputRow = document.createElement('div');
        inputRow.className = 'td-input-row';
        const input = document.createElement('input');
        input.placeholder = _t('Add a task…');
        input.style.cssText = `flex:1;padding:0.45rem;border-radius:0.3rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:0.9rem;`;
        const addBtn = document.createElement('button');
        addBtn.textContent = '+';
        addBtn.style.cssText = `padding:0.4rem 0.7rem;border:none;border-radius:0.3rem;background:${t.accent};color:#fff;font-weight:700;font-size:1rem;cursor:pointer;`;
        inputRow.appendChild(input);
        inputRow.appendChild(addBtn);
        body.appendChild(inputRow);

        // Filter tabs
        const filterRow = document.createElement('div');
        filterRow.className = 'td-filter';
        ['All', 'Active', 'Done'].forEach(f => {
            const btn = document.createElement('button');
            btn.textContent = _t(f);
            btn.dataset.filter = f;
            btn.style.cssText = `padding:0.25rem 0.6rem;border:1px solid ${t.border};border-radius:0.3rem;background:${t.btnBg};color:${t.text};cursor:pointer;font-size:0.8rem;`;
            btn.addEventListener('click', () => { activeFilter = f; render(); });
            filterRow.appendChild(btn);
        });
        body.appendChild(filterRow);

        // List container
        const list = document.createElement('div');
        list.style.cssText = 'flex:1;overflow-y:auto;display:flex;flex-direction:column;gap:4px;';
        body.appendChild(list);

        // Counter
        const counter = document.createElement('div');
        counter.style.cssText = `font-size:0.8rem;opacity:0.6;text-align:center;padding-top:4px;color:${t.textMuted};`;
        body.appendChild(counter);

        let activeFilter = 'All';

        function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(items)); }

        function render() {
            list.innerHTML = '';
            // Update filter buttons
            filterRow.querySelectorAll('button').forEach(b => {
                const active = b.dataset.filter === activeFilter;
                b.style.background = active ? t.accent : t.btnBg;
                b.style.color = active ? '#fff' : t.text;
            });

            const filtered = items.filter(it => {
                if (activeFilter === 'Active') return !it.done;
                if (activeFilter === 'Done') return it.done;
                return true;
            });

            if (filtered.length === 0) {
                const em = document.createElement('div');
                em.style.cssText = 'text-align:center;opacity:0.5;padding:2rem 0;font-size:0.9rem;';
                em.textContent = activeFilter === 'All' ? 'No tasks yet!' : 'No ' + activeFilter.toLowerCase() + ' tasks';
                list.appendChild(em);
            }

            filtered.forEach(it => {
                const row = document.createElement('div');
                row.className = 'td-item';
                row.style.background = isDark() ? '#1e293b' : '#f8fafc';
                row.style.borderColor = t.border;

                const cb = document.createElement('input');
                cb.type = 'checkbox';
                cb.checked = it.done;
                cb.style.cursor = 'pointer';
                cb.addEventListener('change', () => {
                    it.done = cb.checked;
                    save();
                    render();
                });

                const label = document.createElement('span');
                label.textContent = it.text;
                label.style.cssText = `flex:1;font-size:0.9rem;${it.done ? 'text-decoration:line-through;opacity:0.5;' : ''}color:${t.text};`;

                const del = document.createElement('button');
                del.textContent = '×';
                del.style.cssText = `border:none;background:none;color:#ef4444;font-size:1.1rem;cursor:pointer;padding:0 4px;font-weight:700;`;
                del.addEventListener('click', () => {
                    items = items.filter(x => x !== it);
                    save();
                    render();
                });

                row.appendChild(cb);
                row.appendChild(label);
                row.appendChild(del);
                list.appendChild(row);
            });

            const doneCount = items.filter(i => i.done).length;
            counter.textContent = doneCount + '/' + items.length + ' completed';
        }

        function addItem() {
            const text = input.value.trim();
            if (!text) return;
            items.push({ text, done: false, id: Date.now() });
            save();
            input.value = '';
            render();
        }

        addBtn.addEventListener('click', addItem);
        input.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); addItem(); } });

        render();
    }

    // ── 12. Pomodoro Timer ────────────────────────────────
    function buildPomodoro(body, t) {
        const WORK = 25 * 60, SHORT = 5 * 60, LONG = 15 * 60;
        let timeLeft = WORK, running = false, mode = 'work', sessions = 0, interval = null;

        const label = document.createElement('div');
        label.className = 'pomo-label';
        label.style.color = t.accent;
        body.appendChild(label);

        const display = document.createElement('div');
        display.className = 'pomo-display';
        display.style.color = t.text;
        body.appendChild(display);

        const btns = document.createElement('div');
        btns.className = 'pomo-btns';
        const startBtn = document.createElement('button');
        const resetBtn = document.createElement('button');
        const skipBtn = document.createElement('button');
        [startBtn, resetBtn, skipBtn].forEach(b => {
            b.style.cssText = `padding:0.4rem 1rem;border:none;border-radius:0.35rem;cursor:pointer;font-weight:600;font-size:0.85rem;background:${t.btnBg};color:${t.text};`;
        });
        startBtn.style.background = t.accent; startBtn.style.color = '#fff';
        btns.appendChild(startBtn); btns.appendChild(resetBtn); btns.appendChild(skipBtn);
        body.appendChild(btns);

        const stats = document.createElement('div');
        stats.className = 'pomo-stats';
        stats.style.color = t.textMuted;
        body.appendChild(stats);

        function fmt(s) { return String(Math.floor(s/60)).padStart(2,'0') + ':' + String(s%60).padStart(2,'0'); }
        function render() {
            display.textContent = fmt(timeLeft);
            label.textContent = mode === 'work' ? '🍅 FOCUS TIME' : mode === 'short' ? '☕ SHORT BREAK' : '🌴 LONG BREAK';
            startBtn.textContent = running ? '⏸ Pause' : '▶ Start';
            resetBtn.textContent = '↺ Reset';
            skipBtn.textContent = '⏭ Skip';
            stats.innerHTML = `<span>Sessions: <strong>${sessions}</strong></span><span>Streak: <strong>${Math.floor(sessions/4)}</strong> cycles</span>`;
        }

        function tick() {
            timeLeft--;
            if (timeLeft <= 0) {
                clearInterval(interval); running = false;
                if (mode === 'work') {
                    sessions++;
                    mode = (sessions % 4 === 0) ? 'long' : 'short';
                    timeLeft = mode === 'long' ? LONG : SHORT;
                } else {
                    mode = 'work'; timeLeft = WORK;
                }
                try { new Audio('data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdG+Jk5eBc2Z1gIyUi3xsZXiCkJOLfG5meICPk4t+cGl6gI6Si31wanmBjpKLfXBpeYGOkot9cGp5gY6Si31wanmBjpKLfXBqeYGOkYt9cGp5gY6Ri31wanmBjpGLfXBqeYGOkYt9cGp5gY6Ri31wanmBjpGLfQ==').play(); } catch(e){}
            }
            render();
        }

        startBtn.addEventListener('click', () => {
            if (running) { clearInterval(interval); running = false; }
            else { interval = setInterval(tick, 1000); running = true; }
            render();
        });
        resetBtn.addEventListener('click', () => {
            clearInterval(interval); running = false;
            timeLeft = mode === 'work' ? WORK : mode === 'short' ? SHORT : LONG;
            render();
        });
        skipBtn.addEventListener('click', () => {
            clearInterval(interval); running = false;
            if (mode === 'work') { sessions++; mode = (sessions % 4 === 0) ? 'long' : 'short'; timeLeft = mode === 'long' ? LONG : SHORT; }
            else { mode = 'work'; timeLeft = WORK; }
            render();
        });

        render();
    }

    // ── 13. Study Planner ─────────────────────────────────
    function buildStudyPlanner(body, t) {
        const STORAGE_KEY = 'arisEdu-studyPlanner';
        const DAYS = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
        const COLORS = ['#3b82f6','#ef4444','#22c55e','#f59e0b','#8b5cf6','#ec4899','#14b8a6','#f97316'];
        let plan = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
        DAYS.forEach(d => { if (!plan[d]) plan[d] = []; });

        // Add row
        const addRow = document.createElement('div');
        addRow.className = 'sp-add-row';
        const subjInput = document.createElement('input');
        subjInput.placeholder = 'Subject';
        subjInput.style.cssText = `flex:1;min-width:70px;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
        const timeInput = document.createElement('input');
        timeInput.placeholder = 'Time (e.g. 3pm)';
        timeInput.style.cssText = `width:80px;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
        const daySel = document.createElement('select');
        daySel.style.cssText = `background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
        DAYS.forEach(d => { const o = document.createElement('option'); o.value = d; o.textContent = d; daySel.appendChild(o); });
        const addBtn = document.createElement('button');
        addBtn.textContent = '+ Add';
        addBtn.style.cssText = `background:${t.accent};color:#fff;`;
        addRow.appendChild(subjInput); addRow.appendChild(timeInput); addRow.appendChild(daySel); addRow.appendChild(addBtn);
        body.appendChild(addRow);

        // Week grid
        const week = document.createElement('div');
        week.className = 'sp-week';
        body.appendChild(week);

        function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(plan)); }
        function getColor(subj) {
            let hash = 0;
            for (let i = 0; i < subj.length; i++) hash = subj.charCodeAt(i) + ((hash << 5) - hash);
            return COLORS[Math.abs(hash) % COLORS.length];
        }

        function render() {
            week.innerHTML = '';
            DAYS.forEach(day => {
                const col = document.createElement('div');
                col.className = 'sp-day';
                col.style.background = isDark() ? '#1e293b' : '#f8fafc';
                col.style.borderRadius = '0.35rem';
                const hdr = document.createElement('div');
                hdr.className = 'sp-day-header';
                hdr.textContent = day;
                hdr.style.color = t.text;
                col.appendChild(hdr);
                (plan[day] || []).forEach((item, idx) => {
                    const block = document.createElement('div');
                    block.className = 'sp-block';
                    const c = getColor(item.subj);
                    block.style.background = c + '22';
                    block.style.color = c;
                    block.style.borderLeft = '3px solid ' + c;
                    block.innerHTML = `<span>${item.time ? item.time + ' ' : ''}${item.subj}</span><span class="sp-del" title="Remove">✕</span>`;
                    block.querySelector('.sp-del').addEventListener('click', () => {
                        plan[day].splice(idx, 1); save(); render();
                    });
                    col.appendChild(block);
                });
                week.appendChild(col);
            });
        }

        addBtn.addEventListener('click', () => {
            const subj = subjInput.value.trim();
            if (!subj) return;
            plan[daySel.value].push({ subj, time: timeInput.value.trim() });
            save(); subjInput.value = ''; timeInput.value = ''; render();
        });
        subjInput.addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); addBtn.click(); } });

        render();
    }

    // ── 14. Grade Calculator ──────────────────────────────
    function buildGradeCalc(body, t) {
        let rows = [{ name: 'Homework', weight: 20, score: '' }, { name: 'Midterm', weight: 30, score: '' }, { name: 'Final', weight: 50, score: '' }];

        const tableWrap = document.createElement('div');
        tableWrap.style.cssText = 'overflow-x:auto;flex:1;';
        body.appendChild(tableWrap);

        const result = document.createElement('div');
        result.className = 'gc-result';
        result.style.background = isDark() ? '#1e293b' : '#f0f9ff';
        result.style.color = t.text;
        body.appendChild(result);

        const finalDiv = document.createElement('div');
        finalDiv.className = 'gc-final';
        finalDiv.style.background = isDark() ? '#1e293b' : '#fffbeb';
        finalDiv.style.color = t.text;
        finalDiv.style.border = '1px solid ' + t.border;
        body.appendChild(finalDiv);

        const btnRow = document.createElement('div');
        btnRow.style.cssText = 'display:flex;gap:6px;margin-top:6px;';
        const addBtn = document.createElement('button');
        addBtn.textContent = '+ Add Row';
        addBtn.style.cssText = `padding:0.3rem 0.7rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.8rem;background:${t.accent};color:#fff;`;
        btnRow.appendChild(addBtn);
        body.appendChild(btnRow);

        function calc() {
            let totalW = 0, totalS = 0;
            rows.forEach(r => {
                const w = parseFloat(r.weight) || 0;
                const s = parseFloat(r.score);
                if (!isNaN(s)) { totalW += w; totalS += w * s / 100; }
            });
            const avg = totalW > 0 ? (totalS / totalW * 100) : 0;
            let grade = 'F';
            if (avg >= 93) grade = 'A'; else if (avg >= 90) grade = 'A-';
            else if (avg >= 87) grade = 'B+'; else if (avg >= 83) grade = 'B'; else if (avg >= 80) grade = 'B-';
            else if (avg >= 77) grade = 'C+'; else if (avg >= 73) grade = 'C'; else if (avg >= 70) grade = 'C-';
            else if (avg >= 67) grade = 'D+'; else if (avg >= 60) grade = 'D';
            result.innerHTML = `<span style="font-size:0.75rem;opacity:0.6;">Weighted Average</span><br><strong style="font-size:1.4rem;">${totalW > 0 ? avg.toFixed(1) : '—'}%</strong> <span style="font-size:1.1rem;opacity:0.8;">(${grade})</span>`;

            // "What do I need on final?" calc
            const lastRow = rows[rows.length - 1];
            const lw = parseFloat(lastRow.weight) || 0;
            const currentW = totalW - (isNaN(parseFloat(lastRow.score)) ? 0 : lw);
            const currentS = totalS - (isNaN(parseFloat(lastRow.score)) ? 0 : lw * parseFloat(lastRow.score) / 100);
            if (lw > 0 && currentW > 0) {
                const needA = ((90 * (currentW + lw) / 100 - currentS) / lw * 100);
                const needB = ((80 * (currentW + lw) / 100 - currentS) / lw * 100);
                const needC = ((70 * (currentW + lw) / 100 - currentS) / lw * 100);
                finalDiv.innerHTML = `<div style="font-size:0.8rem;font-weight:600;margin-bottom:3px;">📝 What do I need on "${lastRow.name}"?</div>`
                    + `<span style="font-size:0.82rem;">For an A: <strong>${needA.toFixed(1)}%</strong> · B: <strong>${needB.toFixed(1)}%</strong> · C: <strong>${needC.toFixed(1)}%</strong></span>`;
            } else { finalDiv.innerHTML = ''; }
        }

        function render() {
            tableWrap.innerHTML = '';
            const table = document.createElement('table');
            table.className = 'gc-table';
            table.style.borderColor = t.border;
            const thead = document.createElement('thead');
            thead.innerHTML = `<tr><th style="border-color:${t.border}">Category</th><th style="border-color:${t.border};width:60px;">Weight %</th><th style="border-color:${t.border};width:60px;">Score %</th><th style="width:30px;"></th></tr>`;
            table.appendChild(thead);
            const tbody = document.createElement('tbody');
            rows.forEach((r, i) => {
                const tr = document.createElement('tr');
                ['name', 'weight', 'score'].forEach(field => {
                    const td = document.createElement('td');
                    const inp = document.createElement('input');
                    inp.value = r[field]; inp.placeholder = field === 'score' ? '—' : '';
                    inp.style.background = t.inputBg; inp.style.color = t.text; inp.style.borderColor = t.inputBdr;
                    inp.addEventListener('input', () => { r[field] = inp.value; calc(); });
                    td.appendChild(inp); tr.appendChild(td);
                });
                const delTd = document.createElement('td');
                const del = document.createElement('button');
                del.textContent = '×'; del.style.cssText = 'border:none;background:none;color:#ef4444;cursor:pointer;font-weight:700;font-size:1rem;';
                del.addEventListener('click', () => { rows.splice(i, 1); render(); calc(); });
                delTd.appendChild(del); tr.appendChild(delTd);
                tbody.appendChild(tr);
            });
            table.appendChild(tbody);
            tableWrap.appendChild(table);
            calc();
        }

        addBtn.addEventListener('click', () => { rows.push({ name: '', weight: '', score: '' }); render(); });
        render();
    }

    // ── 15. Statistics Calculator ─────────────────────────
    function buildStatCalc(body, t) {
        const label = document.createElement('div');
        label.style.cssText = 'font-size:0.8rem;opacity:0.7;margin-bottom:3px;';
        label.textContent = 'Enter numbers separated by commas or spaces:';
        label.style.color = t.textMuted;
        body.appendChild(label);

        const input = document.createElement('textarea');
        input.className = 'stat-input';
        input.placeholder = 'e.g. 85, 92, 78, 95, 88, 76, 90';
        input.style.background = t.inputBg; input.style.color = t.text; input.style.borderColor = t.inputBdr;
        body.appendChild(input);

        const calcBtn = document.createElement('button');
        calcBtn.textContent = '📊 Calculate';
        calcBtn.style.cssText = `padding:0.4rem 0.8rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;font-size:0.85rem;background:${t.accent};color:#fff;margin:6px 0;`;
        body.appendChild(calcBtn);

        const results = document.createElement('div');
        results.className = 'stat-results';
        body.appendChild(results);

        const histWrap = document.createElement('div');
        histWrap.className = 'stat-hist';
        histWrap.style.background = isDark() ? '#1e293b' : '#f8fafc';
        body.appendChild(histWrap);

        function calculate() {
            const nums = input.value.split(/[,\s]+/).map(Number).filter(n => !isNaN(n));
            if (nums.length === 0) { results.innerHTML = '<div style="grid-column:span 2;text-align:center;opacity:0.5;">Enter numbers above</div>'; histWrap.innerHTML = ''; return; }
            const sorted = [...nums].sort((a,b) => a - b);
            const n = nums.length;
            const sum = nums.reduce((a,b) => a + b, 0);
            const mean = sum / n;
            const median = n % 2 === 0 ? (sorted[n/2-1] + sorted[n/2]) / 2 : sorted[Math.floor(n/2)];
            const freq = {}; nums.forEach(v => freq[v] = (freq[v]||0) + 1);
            const maxFreq = Math.max(...Object.values(freq));
            const modes = Object.keys(freq).filter(k => freq[k] === maxFreq).map(Number);
            const modeStr = maxFreq === 1 ? 'None' : modes.join(', ');
            const variance = nums.reduce((s,v) => s + (v - mean) ** 2, 0) / n;
            const stdDev = Math.sqrt(variance);
            const q1 = sorted[Math.floor(n * 0.25)];
            const q3 = sorted[Math.floor(n * 0.75)];
            const min = sorted[0], max = sorted[n-1];
            const range = max - min;

            const items = [
                ['Count', n], ['Sum', sum.toFixed(2)], ['Mean', mean.toFixed(2)], ['Median', median.toFixed(2)],
                ['Mode', modeStr], ['Std Dev', stdDev.toFixed(2)], ['Q1', q1], ['Q3', q3],
                ['Min', min], ['Max', max], ['Range', range.toFixed(2)], ['Variance', variance.toFixed(2)]
            ];
            results.innerHTML = '';
            items.forEach(([lbl, val]) => {
                const d = document.createElement('div');
                d.className = 'stat-item';
                d.style.background = isDark() ? '#1e293b' : '#f8fafc';
                d.innerHTML = `<span class="stat-label">${lbl}</span><span class="stat-val">${val}</span>`;
                results.appendChild(d);
            });

            // Histogram
            const bins = 8;
            const binW = range / bins || 1;
            const binCounts = new Array(bins).fill(0);
            nums.forEach(v => { const idx = Math.min(Math.floor((v - min) / binW), bins - 1); binCounts[idx]++; });
            const maxBin = Math.max(...binCounts, 1);
            histWrap.innerHTML = '';
            binCounts.forEach(c => {
                const bar = document.createElement('div');
                bar.className = 'stat-bar';
                bar.style.height = (c / maxBin * 100) + '%';
                bar.style.background = t.accent;
                bar.title = c + ' values';
                histWrap.appendChild(bar);
            });
        }

        calcBtn.addEventListener('click', calculate);
        input.addEventListener('keydown', e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); calculate(); } });
    }

    // ── 16. Matrix Calculator ─────────────────────────────
    function buildMatrixCalc(body, t) {
        let sizeA = 2, sizeB = 2, op = 'add';

        const controls = document.createElement('div');
        controls.className = 'mx-controls';
        const sizeSelA = document.createElement('select');
        const opSel = document.createElement('select');
        const sizeSelB = document.createElement('select');
        const goBtn = document.createElement('button');
        [sizeSelA, sizeSelB].forEach(s => {
            [2,3,4].forEach(n => { const o = document.createElement('option'); o.value = n; o.textContent = n+'×'+n; s.appendChild(o); });
            s.style.background = t.inputBg; s.style.color = t.text; s.style.borderColor = t.inputBdr;
        });
        ['add','subtract','multiply','transpose A','determinant A','inverse A'].forEach(v => {
            const o = document.createElement('option'); o.value = v; o.textContent = v.charAt(0).toUpperCase() + v.slice(1); opSel.appendChild(o);
        });
        opSel.style.background = t.inputBg; opSel.style.color = t.text; opSel.style.borderColor = t.inputBdr;
        goBtn.textContent = '= Calculate';
        goBtn.style.background = t.accent; goBtn.style.color = '#fff';
        const lbl1 = document.createElement('span'); lbl1.textContent = 'A:'; lbl1.style.cssText = 'font-weight:600;font-size:0.8rem;color:'+t.text;
        const lbl2 = document.createElement('span'); lbl2.textContent = 'B:'; lbl2.style.cssText = 'font-weight:600;font-size:0.8rem;color:'+t.text;
        controls.appendChild(lbl1); controls.appendChild(sizeSelA); controls.appendChild(opSel);
        controls.appendChild(lbl2); controls.appendChild(sizeSelB); controls.appendChild(goBtn);
        body.appendChild(controls);

        const area = document.createElement('div');
        area.className = 'mx-area';
        body.appendChild(area);

        const resultArea = document.createElement('div');
        resultArea.style.cssText = 'text-align:center;';
        body.appendChild(resultArea);

        function makeGrid(sz, label) {
            const wrap = document.createElement('div');
            const lbl = document.createElement('div');
            lbl.textContent = label;
            lbl.style.cssText = 'text-align:center;font-weight:600;font-size:0.75rem;margin-bottom:2px;color:'+t.textMuted;
            wrap.appendChild(lbl);
            const g = document.createElement('div');
            g.className = 'mx-grid';
            g.style.gridTemplateColumns = `repeat(${sz},1fr)`;
            for (let i = 0; i < sz * sz; i++) {
                const inp = document.createElement('input');
                inp.value = '0';
                inp.style.background = t.inputBg; inp.style.color = t.text; inp.style.borderColor = t.inputBdr;
                g.appendChild(inp);
            }
            wrap.appendChild(g);
            return { el: wrap, grid: g, size: sz };
        }

        function getMatrix(g, sz) {
            const m = [];
            const inputs = g.querySelectorAll('input');
            for (let r = 0; r < sz; r++) {
                m[r] = [];
                for (let c = 0; c < sz; c++) m[r][c] = parseFloat(inputs[r * sz + c].value) || 0;
            }
            return m;
        }

        function showResult(m) {
            resultArea.innerHTML = '<div style="font-weight:600;font-size:0.75rem;margin-bottom:2px;color:'+t.textMuted+'">Result</div>';
            if (typeof m === 'number') { resultArea.innerHTML += `<div style="font-size:1.2rem;font-weight:700;color:${t.text};">${m.toFixed(4)}</div>`; return; }
            const g = document.createElement('div');
            g.className = 'mx-result-grid';
            g.style.gridTemplateColumns = `repeat(${m[0].length},1fr)`;
            m.forEach(row => row.forEach(v => {
                const s = document.createElement('span');
                s.textContent = Number.isInteger(v) ? v : v.toFixed(3);
                s.style.background = isDark() ? '#1e293b' : '#f0f9ff';
                s.style.color = t.text;
                g.appendChild(s);
            }));
            resultArea.appendChild(g);
        }

        let gridA, gridB;

        function buildGrids() {
            area.innerHTML = '';
            gridA = makeGrid(parseInt(sizeSelA.value), 'Matrix A');
            area.appendChild(gridA.el);
            const needB = ['add','subtract','multiply'].includes(opSel.value);
            if (needB) {
                const opLabel = document.createElement('div');
                opLabel.className = 'mx-op-label';
                opLabel.textContent = opSel.value === 'add' ? '+' : opSel.value === 'subtract' ? '−' : '×';
                opLabel.style.color = t.accent;
                area.appendChild(opLabel);
                gridB = makeGrid(parseInt(sizeSelB.value), 'Matrix B');
                area.appendChild(gridB.el);
            } else { gridB = null; }
            resultArea.innerHTML = '';
        }

        function det(m) {
            const n = m.length;
            if (n === 1) return m[0][0];
            if (n === 2) return m[0][0]*m[1][1] - m[0][1]*m[1][0];
            let d = 0;
            for (let c = 0; c < n; c++) {
                const sub = m.slice(1).map(r => [...r.slice(0,c), ...r.slice(c+1)]);
                d += (c % 2 === 0 ? 1 : -1) * m[0][c] * det(sub);
            }
            return d;
        }

        function transpose(m) { return m[0].map((_, c) => m.map(r => r[c])); }

        function inverse(m) {
            const n = m.length;
            const d = det(m);
            if (Math.abs(d) < 1e-10) { resultArea.innerHTML = '<div style="color:#ef4444;font-weight:600;">Matrix is singular (no inverse)</div>'; return null; }
            // Cofactor matrix
            const cof = [];
            for (let r = 0; r < n; r++) {
                cof[r] = [];
                for (let c = 0; c < n; c++) {
                    const sub = m.filter((_,i)=>i!==r).map(row => row.filter((_,j)=>j!==c));
                    cof[r][c] = ((r+c)%2===0?1:-1) * det(sub);
                }
            }
            const adj = transpose(cof);
            return adj.map(row => row.map(v => v / d));
        }

        function calculate() {
            const szA = parseInt(sizeSelA.value);
            const A = getMatrix(gridA.grid, szA);
            const operation = opSel.value;

            if (operation === 'transpose A') { showResult(transpose(A)); return; }
            if (operation === 'determinant A') { showResult(det(A)); return; }
            if (operation === 'inverse A') { const inv = inverse(A); if (inv) showResult(inv); return; }

            if (!gridB) return;
            const szB = parseInt(sizeSelB.value);
            const B = getMatrix(gridB.grid, szB);

            if (operation === 'add' || operation === 'subtract') {
                if (szA !== szB) { resultArea.innerHTML = '<div style="color:#ef4444;font-weight:600;">Matrices must be same size</div>'; return; }
                const res = A.map((row, r) => row.map((v, c) => operation === 'add' ? v + B[r][c] : v - B[r][c]));
                showResult(res);
            } else if (operation === 'multiply') {
                if (szA !== szB) { resultArea.innerHTML = '<div style="color:#ef4444;font-weight:600;">Matrices must be compatible</div>'; return; }
                const res = [];
                for (let r = 0; r < szA; r++) { res[r] = []; for (let c = 0; c < szB; c++) { let s = 0; for (let k = 0; k < szA; k++) s += A[r][k] * B[k][c]; res[r][c] = s; } }
                showResult(res);
            }
        }

        sizeSelA.addEventListener('change', buildGrids);
        sizeSelB.addEventListener('change', buildGrids);
        opSel.addEventListener('change', buildGrids);
        goBtn.addEventListener('click', calculate);
        buildGrids();
    }

    // ── 17. Equation Balancer ─────────────────────────────
    function buildEqBalancer(body, t) {
        const inputRow = document.createElement('div');
        inputRow.className = 'eb-input-row';
        const input = document.createElement('input');
        input.placeholder = 'e.g. Fe + O2 -> Fe2O3';
        input.style.background = t.inputBg; input.style.color = t.text; input.style.borderColor = t.inputBdr;
        const goBtn = document.createElement('button');
        goBtn.textContent = '⚖️ Balance';
        goBtn.style.background = t.accent; goBtn.style.color = '#fff';
        inputRow.appendChild(input); inputRow.appendChild(goBtn);
        body.appendChild(inputRow);

        const result = document.createElement('div');
        result.className = 'eb-result';
        result.style.background = isDark() ? '#1e293b' : '#f0f9ff';
        result.style.color = t.text;
        result.style.border = '1px solid ' + t.border;
        body.appendChild(result);

        const examples = document.createElement('div');
        examples.className = 'eb-examples';
        examples.style.color = t.textMuted;
        examples.innerHTML = '<strong>Examples:</strong><br>H2 + O2 → H2O<br>Fe + O2 → Fe2O3<br>CH4 + O2 → CO2 + H2O<br>Na + Cl2 → NaCl';
        body.appendChild(examples);

        function parseCompound(s) {
            const elems = {};
            const re = /([A-Z][a-z]?)(\d*)/g;
            let m;
            while ((m = re.exec(s)) !== null) {
                if (!m[1]) continue;
                elems[m[1]] = (elems[m[1]] || 0) + (parseInt(m[2]) || 1);
            }
            return elems;
        }

        function balance(eq) {
            const sides = eq.replace(/→/g, '->').split('->').map(s => s.trim());
            if (sides.length !== 2) return null;
            const lhs = sides[0].split('+').map(s => s.trim()).filter(Boolean);
            const rhs = sides[1].split('+').map(s => s.trim()).filter(Boolean);
            const compounds = [...lhs, ...rhs];
            const n = compounds.length;
            const parsed = compounds.map(parseCompound);

            // Get all elements
            const allElems = new Set();
            parsed.forEach(p => Object.keys(p).forEach(e => allElems.add(e)));
            const elemList = [...allElems];

            // Brute force small coefficients (1-10)
            const maxCoeff = 10;
            function tryCoeffs(coeffs, idx) {
                if (idx === n) {
                    // Check balance
                    for (const elem of elemList) {
                        let left = 0, right = 0;
                        for (let i = 0; i < lhs.length; i++) left += coeffs[i] * (parsed[i][elem] || 0);
                        for (let i = 0; i < rhs.length; i++) right += coeffs[lhs.length + i] * (parsed[lhs.length + i][elem] || 0);
                        if (left !== right) return null;
                    }
                    return [...coeffs];
                }
                for (let c = 1; c <= maxCoeff; c++) {
                    coeffs[idx] = c;
                    const r = tryCoeffs(coeffs, idx + 1);
                    if (r) return r;
                }
                return null;
            }

            const coeffs = tryCoeffs(new Array(n).fill(1), 0);
            if (!coeffs) return null;

            // Format result
            const fmtSide = (cmpds, startIdx) => cmpds.map((c, i) => {
                const coeff = coeffs[startIdx + i];
                return (coeff > 1 ? coeff : '') + c;
            }).join(' + ');

            return fmtSide(lhs, 0) + ' → ' + fmtSide(rhs, lhs.length);
        }

        goBtn.addEventListener('click', () => {
            const eq = input.value.trim();
            if (!eq) return;
            const balanced = balance(eq);
            if (balanced) {
                result.innerHTML = `<div style="font-size:0.7rem;opacity:0.5;margin-bottom:4px;">BALANCED</div><div style="font-size:1.1rem;font-weight:700;">${balanced}</div>`;
            } else {
                result.innerHTML = `<div style="color:#ef4444;font-weight:600;">Could not balance. Check format.</div>`;
            }
        });
        input.addEventListener('keydown', e => { if (e.key === 'Enter') goBtn.click(); });
    }

    // ── 18. Data Plotter ──────────────────────────────────
    function buildDataPlotter(body, t) {
        body.style.display = 'flex'; body.style.flexDirection = 'column';

        const dataArea = document.createElement('textarea');
        dataArea.className = 'dp-data';
        dataArea.placeholder = 'Enter x,y pairs (one per line):\n1, 2\n2, 4\n3, 5\n4, 7';
        dataArea.style.background = t.inputBg; dataArea.style.color = t.text; dataArea.style.borderColor = t.inputBdr;
        body.appendChild(dataArea);

        const controls = document.createElement('div');
        controls.className = 'dp-controls';
        const typeSel = document.createElement('select');
        ['scatter','line','bar'].forEach(v => { const o = document.createElement('option'); o.value = v; o.textContent = v.charAt(0).toUpperCase()+v.slice(1); typeSel.appendChild(o); });
        typeSel.style.background = t.inputBg; typeSel.style.color = t.text; typeSel.style.borderColor = t.inputBdr;
        const plotBtn = document.createElement('button');
        plotBtn.textContent = '📉 Plot';
        plotBtn.style.background = t.accent; plotBtn.style.color = '#fff';
        const xlbl = document.createElement('input'); xlbl.placeholder = 'X label';
        xlbl.style.cssText = `width:60px;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
        const ylbl = document.createElement('input'); ylbl.placeholder = 'Y label';
        ylbl.style.cssText = `width:60px;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
        controls.appendChild(typeSel); controls.appendChild(xlbl); controls.appendChild(ylbl); controls.appendChild(plotBtn);
        body.appendChild(controls);

        const canvasWrap = document.createElement('div');
        canvasWrap.style.cssText = 'flex:1;position:relative;min-height:180px;';
        body.appendChild(canvasWrap);
        const canvas = document.createElement('canvas');
        canvas.className = 'dp-canvas';
        canvas.style.background = isDark() ? '#1a2332' : '#ffffff';
        canvas.style.border = '1px solid ' + t.border;
        canvasWrap.appendChild(canvas);
        const ctx = canvas.getContext('2d');

        function resizeCanvas() { canvas.width = canvasWrap.offsetWidth; canvas.height = canvasWrap.offsetHeight; }
        setTimeout(resizeCanvas, 50);
        const win = body.closest('.tool-window');
        if (win) win.addEventListener('tool-resize', () => { setTimeout(resizeCanvas, 30); });

        function plot() {
            resizeCanvas();
            const lines = dataArea.value.trim().split('\n').filter(Boolean);
            const data = lines.map(l => { const p = l.split(/[,\t\s]+/).map(Number); return { x: p[0], y: p[1] }; }).filter(d => !isNaN(d.x) && !isNaN(d.y));
            if (data.length === 0) return;

            const W = canvas.width, H = canvas.height;
            const pad = { l: 45, r: 15, t: 15, b: 35 };
            const pw = W - pad.l - pad.r, ph = H - pad.t - pad.b;
            const xMin = Math.min(...data.map(d=>d.x)), xMax = Math.max(...data.map(d=>d.x));
            const yMin = Math.min(...data.map(d=>d.y)), yMax = Math.max(...data.map(d=>d.y));
            const xRange = xMax - xMin || 1, yRange = yMax - yMin || 1;

            ctx.clearRect(0, 0, W, H);
            ctx.fillStyle = t.textMuted; ctx.font = '10px monospace';

            // Axes
            ctx.strokeStyle = t.border; ctx.lineWidth = 1;
            ctx.beginPath(); ctx.moveTo(pad.l, pad.t); ctx.lineTo(pad.l, H - pad.b); ctx.lineTo(W - pad.r, H - pad.b); ctx.stroke();

            // Grid + labels
            for (let i = 0; i <= 5; i++) {
                const y = pad.t + (ph * i / 5);
                const val = yMax - (yRange * i / 5);
                ctx.fillText(val.toFixed(1), 2, y + 3);
                ctx.strokeStyle = t.border + '44'; ctx.beginPath(); ctx.moveTo(pad.l, y); ctx.lineTo(W - pad.r, y); ctx.stroke();
            }
            for (let i = 0; i <= 5; i++) {
                const x = pad.l + (pw * i / 5);
                const val = xMin + (xRange * i / 5);
                ctx.fillText(val.toFixed(1), x - 12, H - pad.b + 14);
            }

            // Axis labels
            if (xlbl.value) { ctx.fillText(xlbl.value, W / 2 - 15, H - 4); }
            if (ylbl.value) { ctx.save(); ctx.translate(10, H / 2); ctx.rotate(-Math.PI/2); ctx.fillText(ylbl.value, -15, 0); ctx.restore(); }

            const toX = d => pad.l + ((d.x - xMin) / xRange) * pw;
            const toY = d => pad.t + ((yMax - d.y) / yRange) * ph;
            const type = typeSel.value;

            ctx.fillStyle = t.accent; ctx.strokeStyle = t.accent; ctx.lineWidth = 2;

            if (type === 'bar') {
                const barW = Math.max(4, pw / data.length - 2);
                data.forEach(d => {
                    const x = toX(d) - barW / 2;
                    const y = toY(d);
                    const h = (H - pad.b) - y;
                    ctx.fillRect(x, y, barW, h);
                });
            } else {
                if (type === 'line') {
                    ctx.beginPath();
                    data.forEach((d, i) => { const x = toX(d), y = toY(d); i === 0 ? ctx.moveTo(x, y) : ctx.lineTo(x, y); });
                    ctx.stroke();
                }
                data.forEach(d => {
                    ctx.beginPath(); ctx.arc(toX(d), toY(d), 4, 0, Math.PI * 2); ctx.fill();
                });
            }
        }

        plotBtn.addEventListener('click', plot);
    }

    // ── 19. Citation Generator ────────────────────────────
    function buildCitationGen(body, t) {
        let format = 'MLA';

        const tabs = document.createElement('div');
        tabs.className = 'cg-tabs';
        ['MLA','APA','Chicago'].forEach(f => {
            const btn = document.createElement('button');
            btn.textContent = f;
            btn.dataset.fmt = f;
            btn.style.background = f === format ? t.accent : t.btnBg;
            btn.style.color = f === format ? '#fff' : t.text;
            btn.addEventListener('click', () => { format = f; updateTabs(); generate(); });
            tabs.appendChild(btn);
        });
        body.appendChild(tabs);

        function updateTabs() {
            tabs.querySelectorAll('button').forEach(b => {
                const active = b.dataset.fmt === format;
                b.style.background = active ? t.accent : t.btnBg;
                b.style.color = active ? '#fff' : t.text;
            });
        }

        const form = document.createElement('div');
        form.className = 'cg-form';
        const fields = [
            { id: 'author', label: 'Author(s)', placeholder: 'Last, First' },
            { id: 'title', label: 'Title', placeholder: 'Article or Book Title' },
            { id: 'source', label: 'Source / Publisher', placeholder: 'Journal, Publisher, or Website' },
            { id: 'year', label: 'Year', placeholder: '2024' },
            { id: 'url', label: 'URL (optional)', placeholder: 'https://...' },
            { id: 'pages', label: 'Pages (optional)', placeholder: 'pp. 1-10' },
        ];
        const inputs = {};
        fields.forEach(f => {
            const lbl = document.createElement('label');
            lbl.textContent = f.label;
            lbl.style.color = t.textMuted;
            form.appendChild(lbl);
            const inp = document.createElement('input');
            inp.placeholder = f.placeholder;
            inp.style.background = t.inputBg; inp.style.color = t.text; inp.style.borderColor = t.inputBdr;
            inp.addEventListener('input', generate);
            form.appendChild(inp);
            inputs[f.id] = inp;
        });
        body.appendChild(form);

        const result = document.createElement('div');
        result.className = 'cg-result';
        result.style.background = isDark() ? '#1e293b' : '#fffff5';
        result.style.color = t.text;
        result.style.border = '1px solid ' + t.border;
        result.title = 'Click to copy';
        result.addEventListener('click', () => {
            navigator.clipboard.writeText(result.textContent).then(() => {
                const og = result.style.borderColor;
                result.style.borderColor = '#22c55e';
                setTimeout(() => { result.style.borderColor = og; }, 800);
            });
        });
        body.appendChild(result);

        function v(id) { return inputs[id].value.trim(); }

        function generate() {
            const author = v('author'), title = v('title'), source = v('source'), year = v('year'), url = v('url'), pages = v('pages');
            if (!author && !title) { result.innerHTML = '<span style="opacity:0.5;">Fill in fields above…</span>'; return; }

            let cite = '';
            if (format === 'MLA') {
                cite = `${author || 'Author'}. "${title || 'Title'}." <em>${source || 'Source'}</em>, ${year || 'Year'}`;
                if (pages) cite += `, ${pages}`;
                cite += '.';
                if (url) cite += ` ${url}.`;
            } else if (format === 'APA') {
                cite = `${author || 'Author'} (${year || 'n.d.'}). ${title || 'Title'}. <em>${source || 'Source'}</em>`;
                if (pages) cite += `, ${pages}`;
                cite += '.';
                if (url) cite += ` ${url}`;
            } else {
                cite = `${author || 'Author'}. "${title || 'Title'}." <em>${source || 'Source'}</em>`;
                if (pages) cite += `, ${pages}`;
                cite += ` (${year || 'Year'}).`;
                if (url) cite += ` ${url}.`;
            }
            result.innerHTML = cite;
        }

        generate();
    }

    // ── 20. Essay Outliner ────────────────────────────────
    function buildEssayOutliner(body, t) {
        const STORAGE_KEY = 'arisEdu-essayOutline';
        let outline = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null') || {
            thesis: '', bodyPars: [{ topic: '', evidence: '', analysis: '' }], conclusion: ''
        };

        const scrollWrap = document.createElement('div');
        scrollWrap.style.cssText = 'flex:1;overflow-y:auto;';
        body.appendChild(scrollWrap);

        function save() { localStorage.setItem(STORAGE_KEY, JSON.stringify(outline)); }

        function makeSection(parentEl, label, icon, value, onChange) {
            const sec = document.createElement('div');
            sec.className = 'eo-section';
            const title = document.createElement('div');
            title.className = 'eo-section-title';
            title.style.color = t.accent;
            title.textContent = icon + ' ' + label;
            sec.appendChild(title);
            const ta = document.createElement('textarea');
            ta.className = 'eo-section textarea';
            ta.value = value;
            ta.placeholder = 'Write your ' + label.toLowerCase() + '...';
            ta.style.background = t.inputBg; ta.style.color = t.text; ta.style.borderColor = t.inputBdr;
            ta.addEventListener('input', () => { onChange(ta.value); save(); });
            sec.appendChild(ta);
            parentEl.appendChild(sec);
        }

        function render() {
            scrollWrap.innerHTML = '';
            makeSection(scrollWrap, 'Thesis Statement', '🎯', outline.thesis, v => { outline.thesis = v; });

            outline.bodyPars.forEach((par, i) => {
                const wrapper = document.createElement('div');
                wrapper.className = 'eo-body-par';
                wrapper.style.background = isDark() ? '#1e293b' : '#f8fafc';
                wrapper.style.border = '1px solid ' + t.border;

                const header = document.createElement('div');
                header.style.cssText = 'display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;';
                const lbl = document.createElement('span');
                lbl.style.cssText = 'font-weight:700;font-size:0.8rem;color:' + t.accent;
                lbl.textContent = `📝 Body Paragraph ${i + 1}`;
                const delBtn = document.createElement('button');
                delBtn.textContent = '×';
                delBtn.style.cssText = 'border:none;background:none;color:#ef4444;cursor:pointer;font-weight:700;font-size:1rem;';
                delBtn.addEventListener('click', () => { outline.bodyPars.splice(i, 1); if (outline.bodyPars.length === 0) outline.bodyPars.push({ topic: '', evidence: '', analysis: '' }); save(); render(); });
                header.appendChild(lbl); header.appendChild(delBtn);
                wrapper.appendChild(header);

                ['Topic Sentence', 'Evidence / Quote', 'Analysis'].forEach((field, fi) => {
                    const key = ['topic', 'evidence', 'analysis'][fi];
                    const lbl2 = document.createElement('div');
                    lbl2.style.cssText = 'font-size:0.72rem;font-weight:600;opacity:0.6;color:'+t.text;
                    lbl2.textContent = field;
                    wrapper.appendChild(lbl2);
                    const ta = document.createElement('textarea');
                    ta.value = par[key] || '';
                    ta.placeholder = field + '...';
                    ta.style.cssText = `width:100%;padding:0.3rem;border-radius:0.25rem;border:1px solid ${t.inputBdr};background:${t.inputBg};color:${t.text};font-size:0.82rem;resize:vertical;min-height:32px;box-sizing:border-box;margin-top:3px;`;
                    ta.addEventListener('input', () => { par[key] = ta.value; save(); });
                    wrapper.appendChild(ta);
                });

                scrollWrap.appendChild(wrapper);
            });

            makeSection(scrollWrap, 'Conclusion', '🏁', outline.conclusion, v => { outline.conclusion = v; });
        }

        const btns = document.createElement('div');
        btns.className = 'eo-btns';
        const addParBtn = document.createElement('button');
        addParBtn.textContent = '+ Body Paragraph';
        addParBtn.style.background = t.accent; addParBtn.style.color = '#fff';
        addParBtn.addEventListener('click', () => { outline.bodyPars.push({ topic: '', evidence: '', analysis: '' }); save(); render(); });

        const copyBtn = document.createElement('button');
        copyBtn.textContent = '📋 Copy Outline';
        copyBtn.style.background = t.btnBg; copyBtn.style.color = t.text;
        copyBtn.addEventListener('click', () => {
            let text = 'THESIS: ' + outline.thesis + '\n\n';
            outline.bodyPars.forEach((p, i) => {
                text += `BODY ${i+1}:\n  Topic: ${p.topic}\n  Evidence: ${p.evidence}\n  Analysis: ${p.analysis}\n\n`;
            });
            text += 'CONCLUSION: ' + outline.conclusion;
            navigator.clipboard.writeText(text).then(() => { copyBtn.textContent = '✓ Copied!'; setTimeout(() => { copyBtn.textContent = '📋 Copy Outline'; }, 1200); });
        });

        const clearBtn = document.createElement('button');
        clearBtn.textContent = '🗑️ Clear';
        clearBtn.style.background = t.btnBg; clearBtn.style.color = t.text;
        clearBtn.addEventListener('click', () => {
            outline = { thesis: '', bodyPars: [{ topic: '', evidence: '', analysis: '' }], conclusion: '' };
            save(); render();
        });

        btns.appendChild(addParBtn); btns.appendChild(copyBtn); btns.appendChild(clearBtn);
        body.appendChild(btns);

        render();
    }

    // ── 21. Text Tools ────────────────────────────────────
    function buildTextTools(body, t) {
        const statsRow = document.createElement('div');
        statsRow.className = 'tt-stats';
        statsRow.style.color = t.textMuted;
        body.appendChild(statsRow);

        const area = document.createElement('textarea');
        area.className = 'tt-area';
        area.placeholder = 'Paste or type text here…';
        area.style.background = t.inputBg; area.style.color = t.text; area.style.borderColor = t.inputBdr;
        body.appendChild(area);

        function updateStats() {
            const txt = area.value;
            const words = txt.trim() ? txt.trim().split(/\s+/).length : 0;
            const chars = txt.length;
            const sentences = txt.split(/[.!?]+/).filter(s => s.trim()).length;
            const lines = txt.split('\n').length;
            statsRow.innerHTML = `<span>Words: <strong>${words}</strong></span><span>Chars: <strong>${chars}</strong></span><span>Sentences: <strong>${sentences}</strong></span><span>Lines: <strong>${lines}</strong></span>`;
        }
        area.addEventListener('input', updateStats);
        updateStats();

        const btns = document.createElement('div');
        btns.className = 'tt-btns';
        const actions = [
            ['UPPERCASE', () => area.value = area.value.toUpperCase()],
            ['lowercase', () => area.value = area.value.toLowerCase()],
            ['Title Case', () => area.value = area.value.replace(/\w\S*/g, w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())],
            ['Sentence case', () => area.value = area.value.charAt(0).toUpperCase() + area.value.slice(1).toLowerCase()],
            ['Remove Duplicates', () => { area.value = [...new Set(area.value.split('\n'))].join('\n'); }],
            ['Sort Lines', () => { area.value = area.value.split('\n').sort().join('\n'); }],
            ['Reverse', () => { area.value = area.value.split('').reverse().join(''); }],
            ['Trim Lines', () => { area.value = area.value.split('\n').map(l => l.trim()).join('\n'); }],
            ['Copy', () => { navigator.clipboard.writeText(area.value); }],
        ];
        actions.forEach(([label, fn]) => {
            const btn = document.createElement('button');
            btn.textContent = label;
            btn.style.background = t.btnBg; btn.style.color = t.text;
            btn.addEventListener('click', () => { fn(); updateStats(); });
            btns.appendChild(btn);
        });
        body.appendChild(btns);

        // Find & Replace
        const findRow = document.createElement('div');
        findRow.className = 'tt-find-row';
        const findIn = document.createElement('input');
        findIn.placeholder = 'Find';
        findIn.style.background = t.inputBg; findIn.style.color = t.text; findIn.style.borderColor = t.inputBdr;
        const replIn = document.createElement('input');
        replIn.placeholder = 'Replace';
        replIn.style.background = t.inputBg; replIn.style.color = t.text; replIn.style.borderColor = t.inputBdr;
        const replBtn = document.createElement('button');
        replBtn.textContent = 'Replace All';
        replBtn.style.background = t.accent; replBtn.style.color = '#fff';
        replBtn.addEventListener('click', () => {
            if (!findIn.value) return;
            area.value = area.value.split(findIn.value).join(replIn.value);
            updateStats();
        });
        findRow.appendChild(findIn); findRow.appendChild(replIn); findRow.appendChild(replBtn);
        body.appendChild(findRow);
    }

    // ── 22. Focus Sounds ──────────────────────────────────
    function buildFocusSounds(body, t) {
        const SOUNDS = [
            { id: 'rain', emoji: '🌧️', label: 'Rain', freq: [200, 300, 400], type: 'noise' },
            { id: 'whitenoise', emoji: '📻', label: 'White Noise', freq: [0], type: 'noise' },
            { id: 'waves', emoji: '🌊', label: 'Ocean Waves', freq: [120, 180], type: 'wave' },
            { id: 'fire', emoji: '🔥', label: 'Fireplace', freq: [80, 150, 250], type: 'noise' },
            { id: 'forest', emoji: '🌿', label: 'Forest', freq: [2000, 3000, 4000], type: 'chirp' },
            { id: 'cafe', emoji: '☕', label: 'Café', freq: [200, 400, 600], type: 'noise' },
        ];

        let audioCtx = null, activeNodes = [], activeId = null, volume = 0.3;

        const grid = document.createElement('div');
        grid.className = 'fs-sounds-grid';
        body.appendChild(grid);

        SOUNDS.forEach(s => {
            const btn = document.createElement('button');
            btn.className = 'fs-sound-btn';
            btn.style.background = isDark() ? '#1e293b' : '#f8fafc';
            btn.style.color = t.text;
            btn.innerHTML = `<span class="fs-emoji">${s.emoji}</span>${s.label}`;
            btn.dataset.id = s.id;
            btn.addEventListener('click', () => toggleSound(s, btn));
            grid.appendChild(btn);
        });

        const volRow = document.createElement('div');
        volRow.className = 'fs-vol-row';
        volRow.style.color = t.text;
        volRow.innerHTML = `<span>🔈</span>`;
        const volSlider = document.createElement('input');
        volSlider.type = 'range'; volSlider.min = '0'; volSlider.max = '100'; volSlider.value = '30';
        volSlider.addEventListener('input', () => {
            volume = volSlider.value / 100;
            activeNodes.forEach(n => { if (n.gain) n.gain.gain.setValueAtTime(volume, audioCtx.currentTime); });
        });
        const volLabel = document.createElement('span');
        volLabel.textContent = '🔊';
        volRow.appendChild(volSlider); volRow.appendChild(volLabel);
        body.appendChild(volRow);

        const status = document.createElement('div');
        status.style.cssText = 'text-align:center;font-size:0.85rem;margin-top:8px;';
        status.style.color = t.textMuted;
        status.textContent = 'Click a sound to start';
        body.appendChild(status);

        function stopAll() {
            activeNodes.forEach(n => {
                try { n.source.stop(); } catch(e){}
                try { n.source.disconnect(); } catch(e){}
                try { n.gain.disconnect(); } catch(e){}
            });
            activeNodes = [];
            grid.querySelectorAll('.fs-sound-btn').forEach(b => b.classList.remove('active'));
            activeId = null;
            status.textContent = 'Click a sound to start';
        }

        function toggleSound(s, btn) {
            if (activeId === s.id) { stopAll(); return; }
            stopAll();

            if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();

            activeId = s.id;
            btn.classList.add('active');
            status.textContent = `▶ Playing: ${s.label}`;

            // Generate ambient noise using oscillators and filters
            s.freq.forEach(f => {
                const osc = audioCtx.createOscillator();
                const gainNode = audioCtx.createGain();
                const filter = audioCtx.createBiquadFilter();

                if (s.type === 'noise') {
                    // Brown noise via filtered oscillator
                    const bufferSize = 2 * audioCtx.sampleRate;
                    const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                    const data = buffer.getChannelData(0);
                    let lastOut = 0;
                    for (let i = 0; i < bufferSize; i++) {
                        const white = Math.random() * 2 - 1;
                        data[i] = (lastOut + (0.02 * white)) / 1.02;
                        lastOut = data[i];
                        data[i] *= 3.5;
                    }
                    const source = audioCtx.createBufferSource();
                    source.buffer = buffer;
                    source.loop = true;
                    filter.type = 'lowpass';
                    filter.frequency.value = f || 600;
                    gainNode.gain.value = volume;
                    source.connect(filter);
                    filter.connect(gainNode);
                    gainNode.connect(audioCtx.destination);
                    source.start();
                    activeNodes.push({ source, gain: gainNode });
                } else {
                    osc.type = 'sine';
                    osc.frequency.value = f;
                    gainNode.gain.value = volume * 0.15;
                    // Gentle LFO modulation
                    const lfo = audioCtx.createOscillator();
                    const lfoGain = audioCtx.createGain();
                    lfo.frequency.value = 0.1 + Math.random() * 0.3;
                    lfoGain.gain.value = f * 0.1;
                    lfo.connect(lfoGain);
                    lfoGain.connect(osc.frequency);
                    lfo.start();
                    osc.connect(gainNode);
                    gainNode.connect(audioCtx.destination);
                    osc.start();
                    activeNodes.push({ source: osc, gain: gainNode });
                    activeNodes.push({ source: lfo, gain: lfoGain });
                }
            });
        }

        // Cleanup on window close
        const win = body.closest('.tool-window');
        if (win) {
            const origClose = win.querySelector('.tw-close');
            if (origClose) {
                const origHandler = origClose.onclick;
                origClose.onclick = () => { stopAll(); if (origHandler) origHandler(); };
            }
        }
    }

    // ── 23. Random Generator ──────────────────────────────
    function buildRandomGen(body, t) {
        let mode = 'number';

        const tabs = document.createElement('div');
        tabs.className = 'rg-tabs';
        const modes = [
            { id: 'number', label: '🔢 Number' },
            { id: 'coin', label: '🪙 Coin' },
            { id: 'dice', label: '🎲 Dice' },
            { id: 'picker', label: '🎯 Picker' },
            { id: 'shuffle', label: '🔀 Shuffle' },
        ];
        modes.forEach(m => {
            const btn = document.createElement('button');
            btn.textContent = m.label;
            btn.dataset.mode = m.id;
            btn.addEventListener('click', () => { mode = m.id; renderPanel(); });
            tabs.appendChild(btn);
        });
        body.appendChild(tabs);

        const result = document.createElement('div');
        result.className = 'rg-result';
        result.style.background = isDark() ? '#1e293b' : '#f0f9ff';
        result.style.color = t.text;
        body.appendChild(result);

        const panel = document.createElement('div');
        panel.className = 'rg-panel';
        body.appendChild(panel);

        function updateTabs() {
            tabs.querySelectorAll('button').forEach(b => {
                const active = b.dataset.mode === mode;
                b.style.background = active ? t.accent : t.btnBg;
                b.style.color = active ? '#fff' : t.text;
            });
        }

        function renderPanel() {
            updateTabs();
            panel.innerHTML = '';
            result.textContent = '—';

            if (mode === 'number') {
                const row = document.createElement('div');
                row.className = 'rg-row';
                const minIn = document.createElement('input');
                minIn.type = 'number'; minIn.value = '1'; minIn.placeholder = 'Min';
                minIn.style.cssText = `flex:1;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
                const lbl = document.createElement('span');
                lbl.textContent = 'to'; lbl.style.cssText = 'font-size:0.85rem;color:'+t.textMuted;
                const maxIn = document.createElement('input');
                maxIn.type = 'number'; maxIn.value = '100'; maxIn.placeholder = 'Max';
                maxIn.style.cssText = `flex:1;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
                const goBtn = document.createElement('button');
                goBtn.textContent = 'Generate';
                goBtn.style.background = t.accent; goBtn.style.color = '#fff';
                goBtn.addEventListener('click', () => {
                    const min = parseInt(minIn.value) || 0, max = parseInt(maxIn.value) || 100;
                    result.textContent = Math.floor(Math.random() * (max - min + 1)) + min;
                });
                row.appendChild(minIn); row.appendChild(lbl); row.appendChild(maxIn); row.appendChild(goBtn);
                panel.appendChild(row);
            } else if (mode === 'coin') {
                const goBtn = document.createElement('button');
                goBtn.textContent = '🪙 Flip Coin';
                goBtn.style.cssText = `padding:0.5rem 1.2rem;border:none;border-radius:0.4rem;cursor:pointer;font-weight:600;font-size:1rem;background:${t.accent};color:#fff;margin:0 auto;display:block;`;
                goBtn.addEventListener('click', () => {
                    result.textContent = '🪙';
                    setTimeout(() => { result.textContent = Math.random() < 0.5 ? '🪙 HEADS' : '🪙 TAILS'; }, 300);
                });
                panel.appendChild(goBtn);
            } else if (mode === 'dice') {
                const row = document.createElement('div');
                row.className = 'rg-row';
                row.style.justifyContent = 'center';
                const countIn = document.createElement('input');
                countIn.type = 'number'; countIn.value = '1'; countIn.min = '1'; countIn.max = '10'; countIn.placeholder = '# dice';
                countIn.style.cssText = `width:50px;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
                const lbl = document.createElement('span');
                lbl.textContent = '× d'; lbl.style.cssText = 'font-size:0.85rem;color:'+t.textMuted;
                const sidesSel = document.createElement('select');
                [4,6,8,10,12,20].forEach(n => { const o = document.createElement('option'); o.value = n; o.textContent = n; if (n===6) o.selected = true; sidesSel.appendChild(o); });
                sidesSel.style.cssText = `background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;
                const rollBtn = document.createElement('button');
                rollBtn.textContent = '🎲 Roll';
                rollBtn.style.background = t.accent; rollBtn.style.color = '#fff';
                rollBtn.addEventListener('click', () => {
                    const count = Math.min(10, Math.max(1, parseInt(countIn.value) || 1));
                    const sides = parseInt(sidesSel.value);
                    const rolls = [];
                    for (let i = 0; i < count; i++) rolls.push(Math.floor(Math.random() * sides) + 1);
                    const sum = rolls.reduce((a,b) => a+b, 0);
                    result.innerHTML = `<div>${rolls.join(' + ')}</div><div style="font-size:1rem;opacity:0.6;margin-top:4px;">= ${sum}</div>`;
                });
                row.appendChild(countIn); row.appendChild(lbl); row.appendChild(sidesSel); row.appendChild(rollBtn);
                panel.appendChild(row);
            } else if (mode === 'picker') {
                const textarea = document.createElement('textarea');
                textarea.className = 'rg-list-area';
                textarea.placeholder = 'Enter names/items (one per line):\nAlice\nBob\nCharlie\nDiana';
                textarea.style.background = t.inputBg; textarea.style.color = t.text; textarea.style.borderColor = t.inputBdr;
                panel.appendChild(textarea);
                const pickBtn = document.createElement('button');
                pickBtn.textContent = '🎯 Pick One';
                pickBtn.style.cssText = `padding:0.4rem 1rem;border:none;border-radius:0.3rem;cursor:pointer;font-weight:600;background:${t.accent};color:#fff;margin-top:4px;`;
                pickBtn.addEventListener('click', () => {
                    const items = textarea.value.split('\n').map(s=>s.trim()).filter(Boolean);
                    if (items.length === 0) return;
                    result.textContent = '🎯 ' + items[Math.floor(Math.random() * items.length)];
                });
                panel.appendChild(pickBtn);
            } else if (mode === 'shuffle') {
                const textarea = document.createElement('textarea');
                textarea.className = 'rg-list-area';
                textarea.placeholder = 'Enter names to shuffle (one per line):\nAlice\nBob\nCharlie\nDiana';
                textarea.style.background = t.inputBg; textarea.style.color = t.text; textarea.style.borderColor = t.inputBdr;
                panel.appendChild(textarea);
                const row = document.createElement('div');
                row.className = 'rg-row';
                const shuffleBtn = document.createElement('button');
                shuffleBtn.textContent = '🔀 Shuffle';
                shuffleBtn.style.background = t.accent; shuffleBtn.style.color = '#fff';
                const groupBtn = document.createElement('button');
                groupBtn.textContent = '👥 Make Groups';
                groupBtn.style.background = t.btnBg; groupBtn.style.color = t.text;
                const groupSize = document.createElement('input');
                groupSize.type = 'number'; groupSize.value = '2'; groupSize.min = '2'; groupSize.placeholder = 'Size';
                groupSize.style.cssText = `width:50px;background:${t.inputBg};color:${t.text};border-color:${t.inputBdr};`;

                shuffleBtn.addEventListener('click', () => {
                    const items = textarea.value.split('\n').map(s=>s.trim()).filter(Boolean);
                    for (let i = items.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [items[i], items[j]] = [items[j], items[i]]; }
                    textarea.value = items.join('\n');
                    result.textContent = '✅ Shuffled ' + items.length + ' items';
                });
                groupBtn.addEventListener('click', () => {
                    const items = textarea.value.split('\n').map(s=>s.trim()).filter(Boolean);
                    for (let i = items.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [items[i], items[j]] = [items[j], items[i]]; }
                    const sz = Math.max(2, parseInt(groupSize.value) || 2);
                    const groups = [];
                    for (let i = 0; i < items.length; i += sz) groups.push(items.slice(i, i + sz));
                    result.innerHTML = groups.map((g, i) => `<div style="font-size:0.9rem;"><strong>Group ${i+1}:</strong> ${g.join(', ')}</div>`).join('');
                });

                row.appendChild(shuffleBtn); row.appendChild(groupBtn); row.appendChild(groupSize);
                panel.appendChild(row);
            }
        }

        renderPanel();
    }

    // ── 24. Periodic Table ────────────────────────────────
    function buildPeriodicTable(body, t) {
        // Category colors
        const CAT_COLORS = {
            'alkali':      {bg:'#ef4444',fg:'#fff'},  'alkaline':    {bg:'#f97316',fg:'#fff'},
            'transition':  {bg:'#eab308',fg:'#000'},  'post-trans':  {bg:'#22c55e',fg:'#fff'},
            'metalloid':   {bg:'#14b8a6',fg:'#fff'},  'nonmetal':    {bg:'#3b82f6',fg:'#fff'},
            'halogen':     {bg:'#8b5cf6',fg:'#fff'},  'noble':       {bg:'#ec4899',fg:'#fff'},
            'lanthanide':  {bg:'#f59e0b',fg:'#000'},  'actinide':    {bg:'#d946ef',fg:'#fff'},
        };
        const CAT_LABELS = {
            'alkali':'Alkali Metal','alkaline':'Alkaline Earth','transition':'Transition Metal',
            'post-trans':'Post-Transition','metalloid':'Metalloid','nonmetal':'Nonmetal',
            'halogen':'Halogen','noble':'Noble Gas','lanthanide':'Lanthanide','actinide':'Actinide'
        };

        // Compact element data: [atomicNum, symbol, name, category, mass, row, col]
        const EL = [
            [1,'H','Hydrogen','nonmetal','1.008',1,1],[2,'He','Helium','noble','4.003',1,18],
            [3,'Li','Lithium','alkali','6.941',2,1],[4,'Be','Beryllium','alkaline','9.012',2,2],
            [5,'B','Boron','metalloid','10.81',2,13],[6,'C','Carbon','nonmetal','12.01',2,14],
            [7,'N','Nitrogen','nonmetal','14.01',2,15],[8,'O','Oxygen','nonmetal','16.00',2,16],
            [9,'F','Fluorine','halogen','19.00',2,17],[10,'Ne','Neon','noble','20.18',2,18],
            [11,'Na','Sodium','alkali','22.99',3,1],[12,'Mg','Magnesium','alkaline','24.31',3,2],
            [13,'Al','Aluminium','post-trans','26.98',3,13],[14,'Si','Silicon','metalloid','28.09',3,14],
            [15,'P','Phosphorus','nonmetal','30.97',3,15],[16,'S','Sulfur','nonmetal','32.07',3,16],
            [17,'Cl','Chlorine','halogen','35.45',3,17],[18,'Ar','Argon','noble','39.95',3,18],
            [19,'K','Potassium','alkali','39.10',4,1],[20,'Ca','Calcium','alkaline','40.08',4,2],
            [21,'Sc','Scandium','transition','44.96',4,3],[22,'Ti','Titanium','transition','47.87',4,4],
            [23,'V','Vanadium','transition','50.94',4,5],[24,'Cr','Chromium','transition','52.00',4,6],
            [25,'Mn','Manganese','transition','54.94',4,7],[26,'Fe','Iron','transition','55.85',4,8],
            [27,'Co','Cobalt','transition','58.93',4,9],[28,'Ni','Nickel','transition','58.69',4,10],
            [29,'Cu','Copper','transition','63.55',4,11],[30,'Zn','Zinc','transition','65.38',4,12],
            [31,'Ga','Gallium','post-trans','69.72',4,13],[32,'Ge','Germanium','metalloid','72.63',4,14],
            [33,'As','Arsenic','metalloid','74.92',4,15],[34,'Se','Selenium','nonmetal','78.97',4,16],
            [35,'Br','Bromine','halogen','79.90',4,17],[36,'Kr','Krypton','noble','83.80',4,18],
            [37,'Rb','Rubidium','alkali','85.47',5,1],[38,'Sr','Strontium','alkaline','87.62',5,2],
            [39,'Y','Yttrium','transition','88.91',5,3],[40,'Zr','Zirconium','transition','91.22',5,4],
            [41,'Nb','Niobium','transition','92.91',5,5],[42,'Mo','Molybdenum','transition','95.95',5,6],
            [43,'Tc','Technetium','transition','[98]',5,7],[44,'Ru','Ruthenium','transition','101.1',5,8],
            [45,'Rh','Rhodium','transition','102.9',5,9],[46,'Pd','Palladium','transition','106.4',5,10],
            [47,'Ag','Silver','transition','107.9',5,11],[48,'Cd','Cadmium','transition','112.4',5,12],
            [49,'In','Indium','post-trans','114.8',5,13],[50,'Sn','Tin','post-trans','118.7',5,14],
            [51,'Sb','Antimony','metalloid','121.8',5,15],[52,'Te','Tellurium','metalloid','127.6',5,16],
            [53,'I','Iodine','halogen','126.9',5,17],[54,'Xe','Xenon','noble','131.3',5,18],
            [55,'Cs','Caesium','alkali','132.9',6,1],[56,'Ba','Barium','alkaline','137.3',6,2],
            [57,'La','Lanthanum','lanthanide','138.9',6,3],
            [72,'Hf','Hafnium','transition','178.5',6,4],[73,'Ta','Tantalum','transition','180.9',6,5],
            [74,'W','Tungsten','transition','183.8',6,6],[75,'Re','Rhenium','transition','186.2',6,7],
            [76,'Os','Osmium','transition','190.2',6,8],[77,'Ir','Iridium','transition','192.2',6,9],
            [78,'Pt','Platinum','transition','195.1',6,10],[79,'Au','Gold','transition','197.0',6,11],
            [80,'Hg','Mercury','transition','200.6',6,12],[81,'Tl','Thallium','post-trans','204.4',6,13],
            [82,'Pb','Lead','post-trans','207.2',6,14],[83,'Bi','Bismuth','post-trans','209.0',6,15],
            [84,'Po','Polonium','post-trans','[209]',6,16],[85,'At','Astatine','halogen','[210]',6,17],
            [86,'Rn','Radon','noble','[222]',6,18],
            [87,'Fr','Francium','alkali','[223]',7,1],[88,'Ra','Radium','alkaline','[226]',7,2],
            [89,'Ac','Actinium','actinide','[227]',7,3],
            [104,'Rf','Rutherfordium','transition','[267]',7,4],[105,'Db','Dubnium','transition','[268]',7,5],
            [106,'Sg','Seaborgium','transition','[269]',7,6],[107,'Bh','Bohrium','transition','[270]',7,7],
            [108,'Hs','Hassium','transition','[277]',7,8],[109,'Mt','Meitnerium','transition','[278]',7,9],
            [110,'Ds','Darmstadtium','transition','[281]',7,10],[111,'Rg','Roentgenium','transition','[282]',7,11],
            [112,'Cn','Copernicium','transition','[285]',7,12],[113,'Nh','Nihonium','post-trans','[286]',7,13],
            [114,'Fl','Flerovium','post-trans','[289]',7,14],[115,'Mc','Moscovium','post-trans','[290]',7,15],
            [116,'Lv','Livermorium','post-trans','[293]',7,16],[117,'Ts','Tennessine','halogen','[294]',7,17],
            [118,'Og','Oganesson','noble','[294]',7,18],
            // Lanthanides row 9
            [58,'Ce','Cerium','lanthanide','140.1',9,4],[59,'Pr','Praseodymium','lanthanide','140.9',9,5],
            [60,'Nd','Neodymium','lanthanide','144.2',9,6],[61,'Pm','Promethium','lanthanide','[145]',9,7],
            [62,'Sm','Samarium','lanthanide','150.4',9,8],[63,'Eu','Europium','lanthanide','152.0',9,9],
            [64,'Gd','Gadolinium','lanthanide','157.3',9,10],[65,'Tb','Terbium','lanthanide','158.9',9,11],
            [66,'Dy','Dysprosium','lanthanide','162.5',9,12],[67,'Ho','Holmium','lanthanide','164.9',9,13],
            [68,'Er','Erbium','lanthanide','167.3',9,14],[69,'Tm','Thulium','lanthanide','168.9',9,15],
            [70,'Yb','Ytterbium','lanthanide','173.0',9,16],[71,'Lu','Lutetium','lanthanide','175.0',9,17],
            // Actinides row 10
            [90,'Th','Thorium','actinide','232.0',10,4],[91,'Pa','Protactinium','actinide','231.0',10,5],
            [92,'U','Uranium','actinide','238.0',10,6],[93,'Np','Neptunium','actinide','[237]',10,7],
            [94,'Pu','Plutonium','actinide','[244]',10,8],[95,'Am','Americium','actinide','[243]',10,9],
            [96,'Cm','Curium','actinide','[247]',10,10],[97,'Bk','Berkelium','actinide','[247]',10,11],
            [98,'Cf','Californium','actinide','[251]',10,12],[99,'Es','Einsteinium','actinide','[252]',10,13],
            [100,'Fm','Fermium','actinide','[257]',10,14],[101,'Md','Mendelevium','actinide','[258]',10,15],
            [102,'No','Nobelium','actinide','[259]',10,16],[103,'Lr','Lawrencium','actinide','[266]',10,17],
        ];

        // Build lookup grid  (row 1-7 + 9-10, col 1-18)
        const grid = {};
        EL.forEach(el => { grid[el[5] + ',' + el[6]] = el; });

        // Search bar
        const search = document.createElement('input');
        search.className = 'pt-search';
        search.placeholder = 'Search elements...';
        search.style.background = t.inputBg;
        search.style.color = t.text;
        search.style.borderColor = t.inputBdr;
        body.appendChild(search);

        // Legend
        const legend = document.createElement('div');
        legend.className = 'pt-legend';
        Object.entries(CAT_LABELS).forEach(([key, label]) => {
            const c = CAT_COLORS[key];
            legend.innerHTML += `<span style="display:inline-flex;align-items:center;gap:2px;"><span class="pt-legend-swatch" style="background:${c.bg}"></span>${label}</span>`;
        });
        body.appendChild(legend);

        // Table container
        const tableWrap = document.createElement('div');
        tableWrap.className = 'pt-grid';
        body.appendChild(tableWrap);

        // Detail panel
        const detail = document.createElement('div');
        detail.className = 'pt-detail';
        detail.style.background = isDark() ? '#1e293b' : '#f1f5f9';
        detail.style.color = t.text;
        detail.style.border = '1px solid ' + t.border;
        body.appendChild(detail);

        const ROWS = [1,2,3,4,5,6,7,8,9,10]; // 8 = gap row
        const COLS = 18;

        ROWS.forEach(r => {
            if (r === 8) {
                // Spacer row between main table and lanthanides/actinides
                for (let c = 1; c <= COLS; c++) {
                    const sp = document.createElement('div');
                    sp.style.height = '4px';
                    tableWrap.appendChild(sp);
                }
                return;
            }
            for (let c = 1; c <= COLS; c++) {
                const el = grid[r + ',' + c];
                if (!el) {
                    // Lanthanide/actinide indicators
                    if (r === 6 && c === 3) {
                        const ind = document.createElement('div');
                        ind.className = 'pt-cell';
                        ind.style.background = CAT_COLORS['lanthanide'].bg;
                        ind.style.color = CAT_COLORS['lanthanide'].fg;
                        ind.style.fontSize = '0.45em';
                        ind.style.fontWeight = '600';
                        ind.textContent = '57-71';
                        tableWrap.appendChild(ind);
                        continue;
                    }
                    if (r === 7 && c === 3) {
                        const ind = document.createElement('div');
                        ind.className = 'pt-cell';
                        ind.style.background = CAT_COLORS['actinide'].bg;
                        ind.style.color = CAT_COLORS['actinide'].fg;
                        ind.style.fontSize = '0.45em';
                        ind.style.fontWeight = '600';
                        ind.textContent = '89-103';
                        tableWrap.appendChild(ind);
                        continue;
                    }
                    // Labels for Lan/Act rows
                    if (r === 9 && c >= 1 && c <= 3) {
                        const lb = document.createElement('div');
                        if (c === 3) { lb.style.fontSize = '0.4em'; lb.style.fontWeight = '600'; lb.textContent = 'Lan'; lb.style.display='flex';lb.style.alignItems='center';lb.style.justifyContent='center';lb.style.color=t.textMuted; }
                        tableWrap.appendChild(lb);
                        continue;
                    }
                    if (r === 10 && c >= 1 && c <= 3) {
                        const lb = document.createElement('div');
                        if (c === 3) { lb.style.fontSize = '0.4em'; lb.style.fontWeight = '600'; lb.textContent = 'Act'; lb.style.display='flex';lb.style.alignItems='center';lb.style.justifyContent='center';lb.style.color=t.textMuted; }
                        tableWrap.appendChild(lb);
                        continue;
                    }
                    const sp = document.createElement('div');
                    sp.className = 'pt-spacer';
                    tableWrap.appendChild(sp);
                    continue;
                }
                const [num, sym, name, cat, mass] = el;
                const cc = CAT_COLORS[cat] || {bg:'#64748b',fg:'#fff'};
                const cell = document.createElement('div');
                cell.className = 'pt-cell';
                cell.dataset.num = num;
                cell.dataset.sym = sym.toLowerCase();
                cell.dataset.name = name.toLowerCase();
                cell.dataset.cat = cat;
                cell.style.background = cc.bg;
                cell.style.color = cc.fg;
                cell.innerHTML = `<span class="pt-num">${num}</span><span class="pt-sym">${sym}</span><span class="pt-name">${name}</span>`;
                cell.addEventListener('click', () => {
                    detail.classList.add('active');
                    detail.innerHTML = `<strong style="font-size:1.1rem;">${sym} — ${name}</strong><br>`
                        + `<span style="opacity:0.7;">Atomic #:</span> ${num}<br>`
                        + `<span style="opacity:0.7;">Mass:</span> ${mass}<br>`
                        + `<span style="opacity:0.7;">Category:</span> <span style="color:${cc.bg};font-weight:600;">${CAT_LABELS[cat]}</span>`;
                });
                tableWrap.appendChild(cell);
            }
        });

        // Search filter
        search.addEventListener('input', () => {
            const q = search.value.trim().toLowerCase();
            tableWrap.querySelectorAll('.pt-cell').forEach(cell => {
                if (!cell.dataset.num) return;
                const match = !q || cell.dataset.sym.includes(q) || cell.dataset.name.includes(q) || cell.dataset.num === q;
                cell.style.opacity = match ? '1' : '0.15';
            });
        });

        // Responsive scaling on resize
        const BASE_W = 650;
        function scalePT() {
            const win = body.closest('.tool-window');
            if (!win) return;
            const w = win.offsetWidth;
            const s = Math.max(0.5, Math.min(w / BASE_W, 2.5));
            tableWrap.style.gap = Math.max(1, Math.round(1 * s)) + 'px';
            tableWrap.querySelectorAll('.pt-cell').forEach(cell => {
                cell.style.fontSize = (s * 14) + 'px';
                cell.style.padding = Math.round(2 * s) + 'px ' + Math.round(1 * s) + 'px';
            });
            // Show element names when large enough
            tableWrap.querySelectorAll('.pt-cell').forEach(cell => {
                if (s > 1.2) cell.classList.add('show-name'); else cell.classList.remove('show-name');
            });
        }
        const win = body.closest('.tool-window');
        if (win) { win.addEventListener('tool-resize', scalePT); setTimeout(scalePT, 50); }
    }

    // ═══════════════════════════════════════════════════════
    // DROPDOWN MENU
    // ═══════════════════════════════════════════════════════

    const TOOLS = [
        { id: 'calc',      emoji: '🧮', label: 'Calculator',          w: 340, h: 440, builder: buildCalculator },
        { id: 'graph',     emoji: '📈', label: 'Graphing Calculator', w: 400, h: 420, builder: buildGraph },
        { id: 'ai',        emoji: '🤖', label: 'AI Agent',            w: 0,   h: 0,   action: openAIAgent, hideOnQuiz: true },
        { id: 'timer',     emoji: '⏱️', label: 'Timer',               w: 280, h: 280, builder: buildTimer },
        { id: 'notepad',   emoji: '📝', label: 'Notepad',             w: 320, h: 360, builder: buildNotepad },
        { id: 'ptable',    emoji: '⚛️', label: 'Periodic Table',      w: 680, h: 520, builder: buildPeriodicTable, hidden: true },
        { id: 'unitconv',  emoji: '📏', label: 'Unit Converter',      w: 340, h: 380, builder: buildUnitConverter, hidden: true },
        { id: 'formulas',  emoji: '📐', label: 'Formula Sheet',       w: 380, h: 440, builder: buildFormulaSheet, hidden: true },
        { id: 'flashcard', emoji: '🗂️', label: 'Flashcards',          w: 360, h: 380, builder: buildFlashcards, hidden: true },
        { id: 'whiteboard',emoji: '🎨', label: 'Whiteboard',          w: 500, h: 420, builder: buildWhiteboard, hidden: true },
        { id: 'todolist',  emoji: '✅', label: 'To-Do List',          w: 320, h: 400, builder: buildTodoList, hidden: true },
        { id: 'pomodoro',  emoji: '🍅', label: 'Pomodoro Timer',      w: 300, h: 300, builder: buildPomodoro, hidden: true },
        { id: 'planner',   emoji: '📅', label: 'Study Planner',       w: 520, h: 380, builder: buildStudyPlanner, hidden: true },
        { id: 'gradecalc', emoji: '📊', label: 'Grade Calculator',    w: 400, h: 440, builder: buildGradeCalc, hidden: true },
        { id: 'statcalc',  emoji: '📊', label: 'Statistics Calc',     w: 380, h: 480, builder: buildStatCalc, hidden: true },
        { id: 'matrix',    emoji: '🔢', label: 'Matrix Calculator',   w: 440, h: 440, builder: buildMatrixCalc, hidden: true },
        { id: 'eqbalance', emoji: '🧪', label: 'Equation Balancer',   w: 380, h: 380, builder: buildEqBalancer, hidden: true },
        { id: 'dataplotter',emoji:'📉', label: 'Data Plotter',        w: 480, h: 420, builder: buildDataPlotter, hidden: true },
        { id: 'citation',  emoji: '💡', label: 'Citation Generator',  w: 380, h: 520, builder: buildCitationGen, hidden: true },
        { id: 'essay',     emoji: '📝', label: 'Essay Outliner',      w: 400, h: 480, builder: buildEssayOutliner, hidden: true },
        { id: 'texttools', emoji: '🔤', label: 'Text Tools',          w: 380, h: 440, builder: buildTextTools, hidden: true },
        { id: 'focussound',emoji: '🎵', label: 'Focus Sounds',        w: 320, h: 380, builder: buildFocusSounds, hidden: true },
        { id: 'randomgen', emoji: '🎲', label: 'Random Generator',    w: 360, h: 420, builder: buildRandomGen, hidden: true },
    ];

    function buildDropdown(button) {
        const t = T();
        let menu = document.getElementById('tools-dropdown-menu');
        if (menu) { menu.remove(); }

        menu = document.createElement('div');
        menu.id = 'tools-dropdown-menu';
        menu.style.background = t.bg;
        menu.style.border = '1px solid ' + t.border;

        const toolSettings = JSON.parse(localStorage.getItem('arisEduToolsSettings') || '{}');
        TOOLS.forEach(tool => {
            // Hide AI Agent on quiz/test pages
            if (tool.hideOnQuiz && window._arisAiHidden) return;
            // Hidden-by-default tools must be explicitly enabled; default tools can be disabled
            if (tool.hidden && toolSettings[tool.id] !== true) return;
            if (!tool.hidden && toolSettings[tool.id] === false) return;

            const item = document.createElement('button');
            item.className = 'tools-dd-item';
            item.style.background = t.bg;
            item.style.color = t.text;
            item.innerHTML = `<span>${tool.emoji}</span> ${_t(tool.label)}`;
            item.addEventListener('click', () => {
                if (tool.action) { tool.action(); return; }
                createWindow(tool.id, tool.label, tool.emoji, tool.w, tool.h, tool.builder);
            });
            menu.appendChild(item);
        });

        // Disclaimer footer
        const footer = document.createElement('div');
        footer.className = 'tools-dd-footer';
        footer.style.color = t.textMuted;
        footer.textContent = '5 tools shown by default. 18 more available in Settings → Tools.';
        menu.appendChild(footer);

        button.style.position = 'relative';
        button.appendChild(menu);
    }

    function toggleDropdown() {
        const menu = document.getElementById('tools-dropdown-menu');
        if (!menu) return;
        menu.classList.toggle('show');
    }

    function closeDropdown() {
        const menu = document.getElementById('tools-dropdown-menu');
        if (menu) menu.classList.remove('show');
    }

    // close dropdown when clicking outside
    document.addEventListener('click', e => {
        if (!e.target.closest('#tools-dropdown-btn')) closeDropdown();
    });

    // ═══════════════════════════════════════════════════════
    // INIT – convert AI button → Tools button
    // ═══════════════════════════════════════════════════════
    function init() {
        const aiBtn = document.getElementById('ai-assistant-button');
        if (!aiBtn) return;

        // Morph into Tools dropdown trigger
        aiBtn.id = 'tools-dropdown-btn';
        aiBtn.textContent = '';
        aiBtn.innerHTML = '🛠️ Tools';
        aiBtn.removeAttribute('onclick');
        // Remove old click handlers by cloning
        const fresh = aiBtn.cloneNode(true);
        aiBtn.parentNode.replaceChild(fresh, aiBtn);

        fresh.addEventListener('click', (e) => {
            e.stopPropagation();
            if (!document.getElementById('tools-dropdown-menu')) buildDropdown(fresh);
            toggleDropdown();
        });

        // If the AI assistant script already bound to the old button, keep it hidden
        // The AI overlay will be triggered via the dropdown's AI Agent item instead
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
