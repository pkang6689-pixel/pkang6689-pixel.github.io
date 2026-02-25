let videoStopTimer = null;

    function appendVideoParam(src, key, value) {
      if (!src || src.includes(`${key}=`)) {
        return src;
      }
      const joiner = src.includes('?') ? '&' : '?';
      return `${src}${joiner}${key}=${value}`;
    }

    function buildVideoSrc(videoSrc, videoId) {
      const baseSrc = videoSrc || (videoId ? `https://www.youtube.com/embed/${videoId}` : '');
      if (!baseSrc) {
        return '';
      }
      if (!baseSrc.includes('youtube.com/embed/')) {
        return baseSrc;
      }
      let nextSrc = appendVideoParam(baseSrc, 'enablejsapi', '1');
      if (window.location && window.location.origin) {
        nextSrc = appendVideoParam(nextSrc, 'origin', encodeURIComponent(window.location.origin));
      }
      return nextSrc;
    }

    function scheduleVideoStop(iframe, link) {
      if (videoStopTimer) {
        window.clearTimeout(videoStopTimer);
        videoStopTimer = null;
      }
      if (!iframe || !link) {
        return;
      }
      const endValue = Number.parseInt(link.getAttribute('data-video-end'), 10);
      if (!Number.isFinite(endValue)) {
        return;
      }
      const startValue = Number.parseInt(link.getAttribute('data-video-start'), 10);
      const start = Number.isFinite(startValue) ? startValue : 0;
      if (endValue <= start) {
        return;
      }
      videoStopTimer = window.setTimeout(() => {
        if (iframe.contentWindow) {
          iframe.contentWindow.postMessage(JSON.stringify({
            event: 'command',
            func: 'stopVideo',
            args: [],
          }), '*');
        }
        const currentSrc = iframe.src;
        window.setTimeout(() => {
          if (iframe.src === currentSrc) {
            iframe.src = 'about:blank';
          }
        }, 500);
      }, (endValue - start) * 1000);
    }

    const videoInfoText = document.getElementById('video-info-text');
    let videoInfoTimer = null;

    function updateVideoInfo(link) {
      if (!videoInfoText) {
        return;
      }
      const message = link ? link.getAttribute('data-info-message') : null;
      if (message) {
        videoInfoText.textContent = message;
        videoInfoText.classList.remove('is-fading');
        videoInfoText.classList.add('is-visible');
      } else {
        videoInfoText.textContent = '';
        videoInfoText.classList.remove('is-visible');
        videoInfoText.classList.remove('is-fading');
      }
    }

    function toggleVideosPanel(button) {
      if (!button) {
        return;
      }
      const container = button.closest('.side-buttons');
      if (!container) {
        return;
      }
      const panel = container.querySelector('.videos-panel');
      if (!panel) {
        return;
      }
      const isOpen = panel.classList.toggle('is-open');
      container.classList.toggle('videos-open', isOpen);
      panel.setAttribute('aria-hidden', (!isOpen).toString());
    }

    document.querySelectorAll('.view-other-videos').forEach((button) => {
      button.addEventListener('click', (event) => {
        event.preventDefault();
        toggleVideosPanel(button);
      });
    });

    document.addEventListener('click', (event) => {
      const button = event.target.closest('.view-other-videos');
      if (!button) {
        return;
      }
      event.preventDefault();
      toggleVideosPanel(button);
    }, true);

    document.querySelectorAll('.videos-panel a[data-video-id], .videos-panel a[data-video-src]').forEach((link) => {
      link.addEventListener('click', (event) => {
        event.preventDefault();
        const videoSrc = link.getAttribute('data-video-src');
        const videoId = link.getAttribute('data-video-id');
        const videoTitle = link.getAttribute('data-video-title') || 'Lesson video';
        const iframe = document.querySelector('.video-embed iframe');
        const nextSrc = buildVideoSrc(videoSrc, videoId);
        if (!nextSrc || !iframe) {
          return;
        }
        iframe.src = nextSrc;
        iframe.title = videoTitle;
        scheduleVideoStop(iframe, link);
        updateVideoInfo(link);

        const panel = link.closest('.videos-panel');
        const container = link.closest('.side-buttons');
        if (panel) {
          panel.classList.remove('is-open');
          panel.setAttribute('aria-hidden', 'true');
        }
        if (container) {
          container.classList.remove('videos-open');
        }
      });

    });

    // videos-panel overrides
    function updateRubricFromLink(link) {
      if (!link) {
        return;
      }
      const rubricBox = document.querySelector('.rubric-box');
      if (!rubricBox) {
        return;
      }
      const keyMap = {
        Difficulty: 'difficulty',
        Detail: 'detail',
        Speed: 'speed',
        Pace: 'pace',
      };
      rubricBox.querySelectorAll('.rubric-item').forEach((item) => {
        const labelEl = item.querySelector('.rubric-label');
        const ratingEl = item.querySelector('.rubric-rating');
        if (!labelEl || !ratingEl) {
          return;
        }
        const label = labelEl.textContent.trim();
        const key = keyMap[label];
        if (!key) {
          return;
        }
        const rating = link.getAttribute(`data-rating-${key}`) || label;
        const color = link.getAttribute(`data-color-${key}`) || '#334155';
        ratingEl.textContent = rating;
        item.style.background = color;
      });
    }

    function toggleVideosPanel(button) {
      if (!button) {
        return;
      }
      const container = button.closest('.side-buttons');
      if (!container) {
        return;
      }
      const panel = container.querySelector('.videos-panel');
      if (!panel) {
        return;
      }
      const isOpen = panel.classList.toggle('is-open');
      container.classList.toggle('videos-open', isOpen);
      panel.setAttribute('aria-hidden', (!isOpen).toString());
    }

    document.querySelectorAll('.view-other-videos').forEach((button) => {
      button.addEventListener('click', (event) => {
        event.preventDefault();
        toggleVideosPanel(button);
      });
    });

    document.addEventListener('click', (event) => {
      const button = event.target.closest('.view-other-videos');
      if (!button) {
        return;
      }
      event.preventDefault();
      toggleVideosPanel(button);
    }, true);

    document.querySelectorAll('.videos-panel a').forEach((link) => {
      link.addEventListener('click', (event) => {
        event.preventDefault();
        const videoSrc = link.getAttribute('data-video-src');
        const videoId = link.getAttribute('data-video-id');
        const videoTitle = link.getAttribute('data-video-title') || 'Lesson video';
        const iframe = document.querySelector('.video-embed iframe');
        const nextSrc = buildVideoSrc(videoSrc, videoId);
        if (!nextSrc || !iframe) {
          updateRubricFromLink(link);
          updateVideoInfo(link);
          return;
        }
        iframe.src = nextSrc;
        iframe.title = videoTitle;
        scheduleVideoStop(iframe, link);
        updateRubricFromLink(link);
        updateVideoInfo(link);

        const panel = link.closest('.videos-panel');
        const container = link.closest('.side-buttons');
        if (panel) {
          panel.classList.remove('is-open');
          panel.setAttribute('aria-hidden', 'true');
        }
        if (container) {
          container.classList.remove('videos-open');
        }
      });
    });
// Auto-Render Rubric from Data Attributes
document.addEventListener('DOMContentLoaded', () => {
    const rubricData = document.querySelector('.rubric-data');
    if (rubricData) {
        const createItem = (label, key) => {
            const rating = rubricData.getAttribute(`data-${key}`) || 'TBD';
            const color = rubricData.getAttribute(`data-${key}-color`) || '#e2e8f0';
            return `
                <div class="rubric-item" style="background:${color}">
                    <div class="rubric-text">
                        <span class="rubric-label">${label}</span>
                        <span class="rubric-rating">${rating}</span>
                    </div>
                </div>`;
        };

        const html = `
            <div class="rubric-hover-wrap">
                <div aria-hidden="true" class="rubric-hover-dot"><span>i</span></div>
                <div aria-hidden="true" class="rubric-hover-panel">
                    <p><strong>Difficulty:</strong> How hard topic is & how well they explained it</p>
                    <p><strong>Detail:</strong> Depth of content covered</p>
                    <p><strong>Speed:</strong> How long the video is</p>
                    <p><strong>Pace:</strong> How fast the video runs</p>
                </div>
            </div>
            <h2 class="page-title">Rubric</h2>
            <div class="rubric-card">
                <div class="rubric-grid">
                    ${createItem('Difficulty', 'difficulty')}
                    ${createItem('Detail', 'detail')}
                    ${createItem('Speed', 'speed')}
                    ${createItem('Pace', 'pace')}
                </div>
            </div>
        `;
        
        const wrapper = document.createElement('div');
        wrapper.className = 'rubric-box';
        wrapper.innerHTML = html;
        rubricData.replaceWith(wrapper);
    }
});

    // --- Discussion / Help Section Injection ---
    (function() {
        // Wait for DOM
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initHelpSection);
        } else {
            // Slight delay to ensure layout is ready
            setTimeout(initHelpSection, 100);
        }

        function initHelpSection() {
            // Target the lesson-layout or main-container
            const layout = document.querySelector('.lesson-layout') || document.querySelector('.main-container');
            if (!layout) return;
            
            // Check if already injected
            if (document.getElementById('help-section')) return;

            const helpSection = document.createElement('div');
            helpSection.id = 'help-section';
            helpSection.className = 'help-section';
            
            // Flex column to append at bottom
            // If inside lesson-layout (which is flex-row usually or grid), we might need to be outside or handle placement carefully
            // The user asked for "scroll down to on the bottom of video files"
            // Appending to main-container is safest fallback if lesson-layout structure varies
            
            // Improved Container style
            helpSection.classList.add('discussion-container');
            helpSection.style.cssText = `
                margin-top: 3rem; 
                margin-bottom: 3rem; 
                padding: 2rem; 
                background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%); 
                border-radius: 1.5rem; 
                border: 1px solid rgba(255, 255, 255, 0.1); 
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
                width: 100%; 
                max-width: 1000px; 
                margin-left: auto; 
                margin-right: auto;
                color: white;
            `;
            
            helpSection.innerHTML = `
                <div style="display:flex; align-items:center; gap:1rem; margin-bottom:1.5rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:1rem;">
                    <div style="font-size:2rem;">💬</div>
                    <div>
                        <h3 style="font-size: 1.5rem; font-weight: 700; color:white; margin:0;">Discussion & Help</h3>
                        <p style="margin:0; font-size:0.9rem; color:#94a3b8;">Ask questions or share tips with other students.</p>
                    </div>
                </div>

                <div id="comments-list" style="
                    margin-bottom: 2rem; 
                    max-height: 500px; 
                    overflow-y: auto; 
                    display: flex; 
                    flex-direction: column; 
                    gap: 1rem;
                    padding-right: 0.5rem;
                ">
                    <!-- Comments go here -->
                </div>
                
                <form id="comment-form" style="display: flex; flex-direction: column; gap: 1rem; background:rgba(255,255,255,0.05); padding:1.5rem; border-radius:1rem;">
                    <label for="comment-input" style="font-weight:600; color:#e2e8f0;">Post a Question</label>
                    <textarea id="comment-input" rows="3" placeholder="What part of the lesson is confusing?" style="
                        width: 100%; 
                        padding: 1rem; 
                        border-radius: 0.8rem; 
                        border: 1px solid #475569; 
                        background: rgba(30, 41, 59, 0.8); 
                        font-family: inherit; 
                        color: #f1f5f9;
                        resize: vertical;
                    " required></textarea>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-size:0.8rem; color:#64748b;">Visible to everyone</span>
                        <button type="submit" style="
                            padding: 0.8rem 2rem; 
                            background: #3b82f6; 
                            color: white; 
                            border: none; 
                            border-radius: 0.8rem; 
                            cursor: pointer; 
                            font-weight: 600; 
                            transition: background 0.2s;
                        ">Post</button>
                    </div>
                </form>
            `;
            
            // If main-container exists, append there to be at bottom
            if(document.querySelector('.main-container')) {
                 document.querySelector('.main-container').appendChild(helpSection);
            } else {
                 layout.appendChild(helpSection);
            }

            // Logic
            const list = document.getElementById('comments-list');
            const fileKey = window.location.pathname.split('/').pop().replace('.html', ''); // Unique key per file
            const storageKey = 'comments_' + fileKey;

            function renderComments() {
                const comments = JSON.parse(localStorage.getItem(storageKey) || '[]');
                if (comments.length === 0) {
                    list.innerHTML = '<p style="color: #94a3b8; font-style: italic;">No questions yet.</p>';
                    return;
                }
                
                list.innerHTML = comments.map(c => `
                    <div style="padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 0.5rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem; align-items: center;">
                            <span style="font-weight: 600; color: #3b82f6;">${c.user}</span>
                            <span style="font-size: 0.8rem; color: #94a3b8;">${new Date(c.date).toLocaleDateString()}</span>
                        </div>
                        <div style="color: inherit; line-height: 1.5;">${c.text}</div>
                    </div>
                `).join('');
                list.scrollTop = list.scrollHeight;
            }

            document.getElementById('comment-form').addEventListener('submit', (e) => {
                e.preventDefault();
                const input = document.getElementById('comment-input');
                const text = input.value;
                if (!text.trim()) return;

                const userJson = localStorage.getItem('user');
                let user = 'Guest';
                if (userJson) { try { user = JSON.parse(userJson).name || 'User'; } catch(e){} }
                
                const comments = JSON.parse(localStorage.getItem(storageKey) || '[]');
                comments.push({ user, text, date: new Date().toISOString() });
                localStorage.setItem(storageKey, JSON.stringify(comments));
                
                input.value = '';
                renderComments();
            });

            renderComments();
        }
    })();
