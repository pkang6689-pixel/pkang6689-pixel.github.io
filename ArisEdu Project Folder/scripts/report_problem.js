// Report a Problem modal — opens a private email to a placeholder support address.
// Exposes window.showReportProblem() for the taskbar's "More" menu and mobile drawer.
(function () {
    // Placeholder support address — change later to the real inbox.
    const SUPPORT_EMAIL = 'pkang6689@gmail.com';
    const MODAL_ID = 'aris-report-modal';

    function buildModal() {
        if (document.getElementById(MODAL_ID)) return document.getElementById(MODAL_ID);
        const isDark = document.body.classList.contains('dark-mode');
        const wrap = document.createElement('div');
        wrap.id = MODAL_ID;
        wrap.setAttribute('role', 'dialog');
        wrap.setAttribute('aria-modal', 'true');
        wrap.setAttribute('aria-labelledby', 'aris-report-title');
        wrap.style.cssText =
            'position:fixed;inset:0;z-index:10001;display:none;' +
            'align-items:center;justify-content:center;' +
            'background:rgba(15,23,42,0.55);backdrop-filter:blur(4px);';

        wrap.innerHTML =
            '<div class="aris-report-card" style="' +
                'width:min(480px,92vw);max-height:90vh;overflow:auto;' +
                'background:' + (isDark ? '#0f172a' : '#ffffff') + ';' +
                'color:' + (isDark ? '#e2e8f0' : '#0f172a') + ';' +
                'border-radius:1rem;padding:1.5rem 1.5rem 1.25rem;' +
                'box-shadow:0 20px 50px rgba(0,0,0,0.4);' +
                'font-family:ui-sans-serif,system-ui,sans-serif;">' +

                '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.75rem;">' +
                    '<h2 id="aris-report-title" style="margin:0;font-size:1.25rem;font-weight:700;">🚩 Report a Problem</h2>' +
                    '<button type="button" id="aris-report-close" aria-label="Close" style="background:none;border:none;font-size:1.5rem;line-height:1;cursor:pointer;color:inherit;">&times;</button>' +
                '</div>' +

                '<p style="margin:0 0 1rem;font-size:0.9rem;opacity:0.85;">' +
                    'Found a bug or have feedback? This sends a private email — it is not posted publicly like the forums.' +
                '</p>' +

                '<form id="aris-report-form" style="display:flex;flex-direction:column;gap:0.75rem;">' +
                    '<label style="display:flex;flex-direction:column;gap:0.25rem;font-size:0.85rem;font-weight:600;">' +
                        'Subject' +
                        '<input type="text" id="aris-report-subject" required maxlength="120" placeholder="Short summary" ' +
                            'style="padding:0.5rem 0.75rem;border-radius:0.5rem;border:1px solid ' + (isDark ? '#334155' : '#cbd5e1') + ';' +
                            'background:' + (isDark ? '#1e293b' : '#f8fafc') + ';color:inherit;font-size:0.95rem;font-weight:400;">' +
                    '</label>' +

                    '<label style="display:flex;flex-direction:column;gap:0.25rem;font-size:0.85rem;font-weight:600;">' +
                        'Description' +
                        '<textarea id="aris-report-body" required rows="6" maxlength="4000" placeholder="What happened? What were you trying to do?" ' +
                            'style="padding:0.5rem 0.75rem;border-radius:0.5rem;border:1px solid ' + (isDark ? '#334155' : '#cbd5e1') + ';' +
                            'background:' + (isDark ? '#1e293b' : '#f8fafc') + ';color:inherit;font-size:0.95rem;font-weight:400;resize:vertical;font-family:inherit;"></textarea>' +
                    '</label>' +

                    '<div style="display:flex;gap:0.5rem;justify-content:flex-end;margin-top:0.25rem;">' +
                        '<button type="button" id="aris-report-cancel" style="padding:0.5rem 1rem;border-radius:0.5rem;border:1px solid ' + (isDark ? '#475569' : '#cbd5e1') + ';background:transparent;color:inherit;cursor:pointer;font-weight:600;">Cancel</button>' +
                        '<button type="submit" style="padding:0.5rem 1.1rem;border-radius:0.5rem;border:none;background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:#fff;cursor:pointer;font-weight:700;">Send Report</button>' +
                    '</div>' +
                '</form>' +
            '</div>';

        document.body.appendChild(wrap);

        function close() {
            wrap.style.display = 'none';
            document.removeEventListener('keydown', onKey);
        }
        function onKey(e) { if (e.key === 'Escape') close(); }
        wrap.addEventListener('click', function (e) { if (e.target === wrap) close(); });
        wrap.querySelector('#aris-report-close').addEventListener('click', close);
        wrap.querySelector('#aris-report-cancel').addEventListener('click', close);

        wrap.querySelector('#aris-report-form').addEventListener('submit', function (e) {
            e.preventDefault();
            const subject = wrap.querySelector('#aris-report-subject').value.trim();
            const description = wrap.querySelector('#aris-report-body').value.trim();
            if (!subject || !description) return;

            const userEmail = (window.auth && window.auth.currentUser && window.auth.currentUser.email) || 'anonymous';
            const meta =
                '\n\n---\nPage: ' + window.location.href +
                '\nUser-Agent: ' + navigator.userAgent +
                '\nReporter: ' + userEmail;

            const mailto = 'mailto:' + encodeURIComponent(SUPPORT_EMAIL) +
                '?subject=' + encodeURIComponent('[ArisEdu Report] ' + subject) +
                '&body=' + encodeURIComponent(description + meta);

            window.location.href = mailto;
            close();
        });

        wrap._showReport = function () {
            wrap.style.display = 'flex';
            document.addEventListener('keydown', onKey);
            setTimeout(function () { wrap.querySelector('#aris-report-subject').focus(); }, 50);
        };

        return wrap;
    }

    window.showReportProblem = function () {
        const m = buildModal();
        m._showReport();
    };
})();
