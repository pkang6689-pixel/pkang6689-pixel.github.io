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
