(function() {
    // Ambience Controller - Multi-Track Version
    console.log("Ambience Controller Loaded");
    
    // Sound Library
    const sounds = {
        'rain': {
            name: 'Heavy Rain',
            url: 'https://actions.google.com/sounds/v1/weather/rain_heavy_loud.ogg',
            icon: '🌧️'
        },
        'forest': {
            name: 'Forest Day',
            url: 'https://actions.google.com/sounds/v1/ambiences/daytime_forrest_bonfire.ogg',
            icon: '🌲'
        },
        'coffee': {
            name: 'Coffee Shop',
            url: 'https://actions.google.com/sounds/v1/ambiences/coffee_shop.ogg',
            icon: '☕'
        },
        'ocean': {
            name: 'Ocean Waves',
            url: 'https://actions.google.com/sounds/v1/water/waves_crashing_on_rock_beach.ogg',
            icon: '🌊'
        }
    };

    // State
    let currentSound = localStorage.getItem('arisAmbienceTrack') || 'rain';
    let currentVolume = parseFloat(localStorage.getItem('arisAmbienceVolume') || '0.3');
    let isPlaying = localStorage.getItem('arisAmbiencePlaying') === 'true';
    let audio = new Audio();
    audio.crossOrigin = "anonymous";
    audio.loop = true;

    // Load Initial Sound
    function loadSound(key) {
        if (sounds[key]) {
            audio.src = sounds[key].url;
            audio.volume = currentVolume;
            currentSound = key;
            localStorage.setItem('arisAmbienceTrack', key);
            
            // Update UI if exists
            const btn = document.getElementById('ambience-toggle-btn');
            if(btn) btn.innerHTML = sounds[key].icon;
        }
    }

    // Create UI
    const container = document.createElement('div');
    container.id = 'ambience-controls';
    container.style.cssText = `
        position: fixed;
        bottom: 20px;
        left: 20px;
        z-index: 9999;
        display: flex;
        align-items: center;
        gap: 8px;
        background: rgba(15, 23, 42, 0.85); /* Slate 900 */
        backdrop-filter: blur(8px);
        padding: 6px 10px;
        border-radius: 999px;
        color: white;
        transition: all 0.3s ease;
        opacity: 0.6;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        max-width: 42px; /* Collapsed state */
        overflow: hidden;
    `;
    
    // Hover Effects
    container.onmouseenter = () => {
        container.style.opacity = '1';
        container.style.maxWidth = '300px'; // Expand
    };
    container.onmouseleave = () => {
        if(!isPlaying) {
            container.style.opacity = '0.6';
            container.style.maxWidth = '42px'; // Collapse
        } else {
             container.style.opacity = '0.9'; 
             container.style.maxWidth = '42px';
        }
    };

    // 1. Play/Pause Button
    const btn = document.createElement('button');
    btn.id = 'ambience-toggle-btn';
    btn.innerHTML = sounds[currentSound] ? sounds[currentSound].icon : '🌧️';
    btn.style.cssText = `
        background:none; border:none; font-size: 1.2rem; cursor: pointer; padding: 0; color: white;
        min-width: 24px; display: flex; align-items: center; justify-content: center;
    `;
    btn.title = 'Toggle Ambience';

    // 2. Sound Selector
    const select = document.createElement('select');
    select.id = 'ambience-selector';
    select.style.cssText = `
        background: transparent;
        border: none;
        color: white; 
        font-size: 0.8rem;
        padding: 2px 4px;
        border-radius: 4px;
        cursor: pointer;
        outline: none;
        max-width: 100px;
        text-align: right;
    `;
    
    // Create a style element for the options to ensure they are visible
    if (!document.getElementById('ambience-styles')) {
        const style = document.createElement('style');
        style.id = 'ambience-styles';
        style.textContent = `
            #ambience-selector option {
                background-color: #0f172a; 
                color: #cbd5e1; 
            }
        `;
        document.head.appendChild(style);
    }

    Object.keys(sounds).forEach(key => {
        const opt = document.createElement('option');
        opt.value = key;
        opt.textContent = sounds[key].name;
        if(key === currentSound) opt.selected = true;
        select.appendChild(opt);
    });

    // 3. Volume Slider
    const slider = document.createElement('input');
    slider.type = 'range';
    slider.min = 0;
    slider.max = 1;
    slider.step = 0.05;
    slider.value = currentVolume;
    slider.style.cssText = `
        width: 60px;
        cursor: pointer;
        accent-color: #3b82f6;
        margin-left: 5px;
    `;

    // Logic
    btn.onclick = () => {
        if (isPlaying) {
            audio.pause();
            btn.style.opacity = '0.7';
            isPlaying = false;
            localStorage.setItem('arisAmbiencePlaying', 'false');
        } else {
            // Ensure audio src is loaded
            if(!audio.src || audio.src === '') loadSound(currentSound);
            
            const playPromise = audio.play();
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    btn.style.opacity = '1';
                    isPlaying = true;
                    localStorage.setItem('arisAmbiencePlaying', 'true');
                }).catch(error => {
                    console.error("Ambience: Play failed", error);
                    isPlaying = false;
                    localStorage.setItem('arisAmbiencePlaying', 'false');
                });
            }
        }
    };

    select.onchange = (e) => {
        const key = e.target.value;
        const wasPlaying = isPlaying;
        loadSound(key);
        if (wasPlaying) {
             const p = audio.play();
             if (p !== undefined) {
                 p.catch(e => {
                     console.error(e);
                     // If switching track fails to play (rare), update state?
                     // Probably fine to leave as is, since user initiated action.
                 });
             }
             isPlaying = true;
             btn.style.opacity = '1';
             // No change to localStorage needed as it remains playing
        }
    };

    slider.oninput = (e) => {
        currentVolume = e.target.value;
        audio.volume = currentVolume;
        localStorage.setItem('arisAmbienceVolume', currentVolume);
    };

    container.appendChild(btn);
    container.appendChild(select);
    container.appendChild(slider);
    
    // Initial Load
    loadSound(currentSound);

    if (isPlaying) {
        const p = audio.play();
        if (p !== undefined) {
            p.then(() => {
                btn.style.opacity = '1';
            }).catch(e => {
                // Autoplay policy might block this
                console.log("Autoplay prevented:", e);
                isPlaying = false;
                localStorage.setItem('arisAmbiencePlaying', 'false');
                btn.style.opacity = '0.7';
            });
        }
    } else {
        btn.style.opacity = '0.7';
    }
    
    // Ensure body exists before appending
    if(document.body) {
        document.body.appendChild(container);
    } else {
        window.addEventListener('DOMContentLoaded', () => document.body.appendChild(container));
    }

})();
