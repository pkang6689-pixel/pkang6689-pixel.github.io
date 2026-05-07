
// Auto-adjust body padding based on Taskbar height (handling wrap on small screens)
(function() {
    let lastHeight = 0;
    function adjustPadding() {
        const taskbar = document.querySelector('.taskbar');
        if (!taskbar) return;
        const height = taskbar.offsetHeight;
        if (height === lastHeight) return; // avoid redundant reflows
        lastHeight = height;
        document.body.style.paddingTop = height + 'px';
    }

    // Run as early as possible, then again on DOM ready / load / resize
    adjustPadding();
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', adjustPadding);
    }
    window.addEventListener('load', adjustPadding);
    window.addEventListener('resize', adjustPadding);

    // Track taskbar size changes (e.g. wrap on small viewports)
    if (window.ResizeObserver) {
        const ro = new ResizeObserver(adjustPadding);
        const tb = document.querySelector('.taskbar');
        if (tb) {
            ro.observe(tb);
        } else {
            // Wait for taskbar to be injected by taskbar.js
            const observer = new MutationObserver(() => {
                const t = document.querySelector('.taskbar');
                if (t) {
                    ro.observe(t);
                    adjustPadding();
                    observer.disconnect();
                }
            });
            observer.observe(document.documentElement, { childList: true, subtree: true });
        }
    }
})();
