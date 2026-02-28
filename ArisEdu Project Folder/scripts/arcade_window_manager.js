/**
 * Arcade Window Manager
 * Adds drag and resize functionality to arcade game windows
 */

document.addEventListener('DOMContentLoaded', () => {
    makeArcadeGameDraggableAndResizable();
});

function makeArcadeGameDraggableAndResizable() {
    const gameWrapper = document.getElementById('game-wrapper');
    const gameSidebar = document.getElementById('game-sidebar');
    
    if (!gameWrapper) return;

    // Create outer container to hold both game and sidebar
    const outerContainer = document.createElement('div');
    outerContainer.className = 'arcade-draggable-outer';
    outerContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9000;
        display: flex;
        gap: 1rem;
        backgroundColor: transparent;
        pointerEvents: none;
    `;

    // Create draggable window wrapper
    const windowWrapper = document.createElement('div');
    windowWrapper.className = 'arcade-draggable-window';
    
    // Preserve original position and size from gameWrapper
    const rect = gameWrapper.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    windowWrapper.style.cssText = `
        position: fixed;
        top: ${rect.top + scrollTop}px;
        left: ${rect.left}px;
        width: ${rect.width}px;
        height: ${rect.height}px;
        pointerEvents: auto;
        display: flex;
        flex-direction: column;
        backgroundColor: #1f2937;
        borderRadius: 0.75rem;
        boxShadow: 0 20px 50px rgba(0, 0, 0, 0.5);
        border: 2px solid rgba(55, 65, 81, 0.8);
        overflow: visible;
        minWidth: 300px;
        minHeight: 250px;
        resize: both;
    `;

    // Create header for dragging
    const header = document.createElement('div');
    header.className = 'arcade-window-header';
    header.style.cssText = `
        cursor: move;
        backgroundColor: #0f172a;
        color: white;
        padding: 0.75rem 1rem;
        display: flex;
        justifyContent: space-between;
        alignItems: center;
        borderBottom: 2px solid #334155;
        userSelect: none;
        flexShrink: 0;
        fontWeight: 600;
        fontSize: 0.95rem;
    `;

    // Get game title from the page
    const gameTitle = document.querySelector('h1')?.textContent || 'Game';
    const titleSpan = document.createElement('span');
    titleSpan.textContent = gameTitle;

    // Create close button
    const closeBtn = document.createElement('button');
    closeBtn.style.cssText = `
        background: none;
        border: none;
        color: white;
        fontSize: 24px;
        cursor: pointer;
        padding: 0;
        marginLeft: 1rem;
        transition: color 0.2s;
    `;
    closeBtn.textContent = '×';
    closeBtn.onmouseover = () => { closeBtn.style.color = '#ef4444'; };
    closeBtn.onmouseout = () => { closeBtn.style.color = 'white'; };
    closeBtn.onclick = () => {
        // Return to arcade
        sessionStorage.removeItem('validGameAccess');
        window.location.href = 'arcade.html';
    };

    header.appendChild(titleSpan);
    header.appendChild(closeBtn);

    // Create body container
    const body = document.createElement('div');
    body.className = 'arcade-window-body';
    body.style.cssText = `
        flex: 1;
        overflow: auto;
        position: relative;
        display: flex;
    `;

    // Create content wrapper (flex container for layout inside)
    const contentWrapper = document.createElement('div');
    contentWrapper.style.cssText = `
        flex: 1;
        overflow: auto;
        display: flex;
        flexDirection: column;
        justifyContent: center;
        alignItems: center;
        padding: 1rem;
    `;

    // Add resize handles
    const corners = ['nw', 'ne', 'sw', 'se'];
    corners.forEach(corner => {
        const handle = document.createElement('div');
        handle.className = `arcade-resize-handle ${corner}`;
        handle.style.cssText = `
            position: absolute;
            width: 12px;
            height: 12px;
            backgroundColor: #0f172a;
            cursor: ${corner === 'nw' || corner === 'se' ? 'nwse-resize' : 'nesw-resize'};
            zIndex: 10;
            ${corner === 'nw' ? 'top: -6px; left: -6px;' : ''}
            ${corner === 'ne' ? 'top: -6px; right: -6px;' : ''}
            ${corner === 'sw' ? 'bottom: -6px; left: -6px;' : ''}
            ${corner === 'se' ? 'bottom: -6px; right: -6px;' : ''}
        `;
        windowWrapper.appendChild(handle);
    });

    // Build structure
    windowWrapper.appendChild(header);
    body.appendChild(contentWrapper);
    windowWrapper.appendChild(body);
    outerContainer.appendChild(windowWrapper);

    // Move game wrapper into the body
    const originalParent = gameWrapper.parentNode;
    contentWrapper.appendChild(gameWrapper);
    gameWrapper.style.width = '100%';
    gameWrapper.style.height = '100%';
    gameWrapper.style.margin = '0';
    gameWrapper.style.position = 'relative';

    // Add sidebar if present
    if (gameSidebar) {
        const sidebarWrapper = document.createElement('div');
        sidebarWrapper.style.cssText = `
            pointerEvents: auto;
            backgroundColor: #1f2937;
            borderRadius: 0.75rem;
            boxShadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            border: 2px solid rgba(55, 65, 81, 0.8);
            overflow: hidden;
            minWidth: 350px;
            maxHeight: 70vh;
        `;
        sidebarWrapper.appendChild(gameSidebar);
        outerContainer.appendChild(sidebarWrapper);
        gameSidebar.style.width = '100%';
        gameSidebar.style.height = '100%';
        gameSidebar.style.margin = '0';
    }

    // Insert into document
    document.body.appendChild(outerContainer);

    // Setup dragging
    let isDragging = false;
    let dragOffsetX = 0;
    let dragOffsetY = 0;

    header.addEventListener('mousedown', (e) => {
        if (e.target === closeBtn || e.target.closest('button')) return;
        
        isDragging = true;
        dragOffsetX = e.clientX - windowWrapper.offsetLeft;
        dragOffsetY = e.clientY - windowWrapper.offsetTop;
        
        document.addEventListener('mousemove', dragWindow);
        document.addEventListener('mouseup', stopDragging);
        e.preventDefault();
    });

    function dragWindow(e) {
        if (!isDragging) return;
        let newLeft = e.clientX - dragOffsetX;
        let newTop = e.clientY - dragOffsetY;
        
        // Keep within bounds
        newLeft = Math.max(0, Math.min(newLeft, window.innerWidth - 100));
        newTop = Math.max(0, Math.min(newTop, window.innerHeight - 100));
        
        outerContainer.style.left = newLeft + 'px';
        outerContainer.style.top = newTop + 'px';
    }

    function stopDragging() {
        isDragging = false;
        document.removeEventListener('mousemove', dragWindow);
        document.removeEventListener('mouseup', stopDragging);
    }

    // Setup resizing
    function initResize(e) {
        e.preventDefault();
        const handle = e.target;
        const startX = e.clientX;
        const startY = e.clientY;
        const startWidth = windowWrapper.offsetWidth;
        const startHeight = windowWrapper.offsetHeight;
        const startTop = parseInt(outerContainer.style.top) || 0;
        const startLeft = parseInt(outerContainer.style.left) || 0;

        document.addEventListener('mousemove', resize);
        document.addEventListener('mouseup', stopResize);

        function resize(ev) {
            let newWidth = startWidth;
            let newHeight = startHeight;
            let newTop = startTop;
            let newLeft = startLeft;

            if (handle.classList.contains('se')) {
                newWidth = startWidth + (ev.clientX - startX);
                newHeight = startHeight + (ev.clientY - startY);
            } else if (handle.classList.contains('sw')) {
                newWidth = startWidth - (ev.clientX - startX);
                newLeft = startLeft + (ev.clientX - startX);
                newHeight = startHeight + (ev.clientY - startY);
            } else if (handle.classList.contains('ne')) {
                newWidth = startWidth + (ev.clientX - startX);
                newHeight = startHeight - (ev.clientY - startY);
                newTop = startTop + (ev.clientY - startY);
            } else if (handle.classList.contains('nw')) {
                newWidth = startWidth - (ev.clientX - startX);
                newLeft = startLeft + (ev.clientX - startX);
                newHeight = startHeight - (ev.clientY - startY);
                newTop = startTop + (ev.clientY - startY);
            }

            // Apply with minimum size constraints
            if (newWidth > 300) {
                windowWrapper.style.width = newWidth + 'px';
                outerContainer.style.left = newLeft + 'px';
            }
            if (newHeight > 250) {
                windowWrapper.style.height = newHeight + 'px';
                outerContainer.style.top = newTop + 'px';
            }
        }

        function stopResize() {
            document.removeEventListener('mousemove', resize);
            document.removeEventListener('mouseup', stopResize);
        }
    }

    const resizeHandles = windowWrapper.querySelectorAll('.arcade-resize-handle');
    resizeHandles.forEach(handle => {
        handle.addEventListener('mousedown', initResize);
    });
}
