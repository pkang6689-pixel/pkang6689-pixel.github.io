
// Auto-adjust body padding based on Taskbar height (handling wrap)
(function() {
    function adjustPadding() {
        const taskbar = document.querySelector('.taskbar');
        if (taskbar) {
            const height = taskbar.offsetHeight;
            // Add some buffer
            document.body.style.paddingTop = (height + 20) + 'px';
        }
    }

    // Run on load and resize
    window.addEventListener('load', adjustPadding);
    window.addEventListener('resize', adjustPadding);
    
    // Also use ResizeObserver if available for more robust detection
    if (window.ResizeObserver) {
        const ro = new ResizeObserver(entries => {
            adjustPadding();
        });
        const tb = document.querySelector('.taskbar');
        if (tb) ro.observe(tb);
        // Wait for taskbar to exist if not yet
        else {
            const observer = new MutationObserver((mutations) => {
                const tb = document.querySelector('.taskbar');
                if (tb) {
                    ro.observe(tb);
                    adjustPadding();
                    observer.disconnect();
                }
            });
            observer.observe(document.body, { childList: true, subtree: true });
        }
    }
})();
