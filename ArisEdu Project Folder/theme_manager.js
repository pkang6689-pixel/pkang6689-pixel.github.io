(function() {
    const gradients = {
        'blue-green': 'linear-gradient(135deg, #3b82f6 0%, #10b981 50%, #8b5cf6 100%)',
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

    let auroraTimeout = null;
    let sunsetTimeout = null;
    let coralTimeout = null;
    let autumnTimeout = null;
    let cyberTimeout = null;
    let lavenderTimeout = null;
    let sunriseTimeout = null;

    // --- Audio System (Web Audio API) ---
    const ArisAudio = {
        ctx: null,
        masterGain: null,
        activeNodes: [],
        enabled: false,
        currentTheme: null,

        init() {
            if (this.ctx) return;
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (AudioContext) {
                this.ctx = new AudioContext();
                this.masterGain = this.ctx.createGain();
                this.masterGain.connect(this.ctx.destination);
                this.masterGain.gain.value = 0.15; // Global Volume limit
            }
        },

        toggle(enable) {
            this.enabled = enable;
            if (enable) {
                this.init();
                if (this.ctx.state === 'suspended') this.ctx.resume();
                if (this.currentTheme) this.playTheme(this.currentTheme);
            } else {
                this.stopAll();
            }
            this.updateUI();
        },

        stopAll() {
            this.activeNodes.forEach(node => {
                try {
                    if (node.stop) node.stop();
                    node.disconnect();
                } catch (e) {}
            });
            this.activeNodes = [];
        },

        createNoise(type) {
            const bufferSize = this.ctx.sampleRate * 2;
            const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
            const data = buffer.getChannelData(0);
            for (let i = 0; i < bufferSize; i++) {
                if (type === 'white') data[i] = Math.random() * 2 - 1;
                else if (type === 'pink') {
                    // Pink noise approximation
                    let b0, b1, b2, b3, b4, b5, b6;
                    b0 = b1 = b2 = b3 = b4 = b5 = b6 = 0.0;
                    for (let j = 0; j < bufferSize; j++) {
                        const white = Math.random() * 2 - 1;
                        b0 = 0.99886 * b0 + white * 0.0555179;
                        b1 = 0.99332 * b1 + white * 0.0750759;
                        b2 = 0.96900 * b2 + white * 0.1538520;
                        b3 = 0.86650 * b3 + white * 0.3104856;
                        b4 = 0.55000 * b4 + white * 0.5329522;
                        b5 = -0.7616 * b5 - white * 0.0168980;
                        data[j] = b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362;
                        data[j] *= 0.11; // compensate gain
                        b6 = white * 0.115926;
                    }
                } else { // Brown
                    let lastOut = 0;
                    for (let j = 0; j < bufferSize; j++) {
                        const white = Math.random() * 2 - 1;
                        data[j] = (lastOut + (0.02 * white)) / 1.02;
                        lastOut = data[j];
                        data[j] *= 3.5; 
                    }
                }
            }
            const noise = this.ctx.createBufferSource();
            noise.buffer = buffer;
            noise.loop = true;
            return noise;
        },

        playTheme(theme) {
            this.currentTheme = theme;
            if (!this.enabled || !this.ctx) return;
            this.stopAll();

            const t = this.ctx.currentTime;
            
            // Common specialized generators
            const playDrone = (freqs, type='sine', detune=0) => {
                freqs.forEach(f => {
                    const osc = this.ctx.createOscillator();
                    osc.type = type;
                    osc.frequency.value = f;
                    if(detune) osc.detune.value = (Math.random()-0.5)*detune;
                    
                    const gain = this.ctx.createGain();
                    gain.gain.setValueAtTime(0, t);
                    gain.gain.linearRampToValueAtTime(0.05, t + 2); // Fade in
                    
                    osc.connect(gain);
                    gain.connect(this.masterGain);
                    osc.start();
                    this.activeNodes.push(osc, gain);
                });
            };

            const playAtmosphere = (noiseType, filterType, freq, q=1, lfoSpeed=0.1, lfoDepth=100) => {
                const noise = this.createNoise(noiseType);
                const filter = this.ctx.createBiquadFilter();
                filter.type = filterType;
                filter.frequency.value = freq;
                filter.Q.value = q;
                
                // LFO for movement
                const lfo = this.ctx.createOscillator();
                lfo.frequency.value = lfoSpeed;
                const lfoGain = this.ctx.createGain();
                lfoGain.gain.value = lfoDepth;
                lfo.connect(lfoGain);
                lfoGain.connect(filter.frequency);
                
                const gain = this.ctx.createGain();
                gain.gain.value = 0.3;

                noise.connect(filter);
                filter.connect(gain);
                gain.connect(this.masterGain);
                
                noise.start();
                lfo.start();
                this.activeNodes.push(noise, filter, gain, lfo, lfoGain);
            };

            switch (soundProfile) {
                case 'blue-green': // Aurora
                case 'aurora':
                    playDrone([110, 164.8, 196, 220], 'sine', 10); // A Major ish pad
                    playAtmosphere('pink', 'lowpass', 400, 0.5, 0.2, 200); // Wind
                    break;
                case 'sunset':
                    playAtmosphere('pink', 'lowpass', 300, 2, 0.15, 200); // Ocean Waves
                    playDrone([146.8], 'sine'); // Low D drone
                    break;
                case 'coral':
                    playAtmosphere('pink', 'lowpass', 200, 5, 0.1, 100); // Deep underwater (muffled)
                    // Bubbles?
                    break;
                case 'autumn':
                    playAtmosphere('brown', 'lowpass', 600, 0.5, 0.5, 300); // Rustling Wind
                    break;
                case 'rain': // Explicit Rain Mode (reuses Autumn base)
                     playAtmosphere('brown', 'lowpass', 800, 0.2, 0.8, 400); // Heavy Rain
                     break;
                case 'ocean': // Explicit Ocean Mode
                     playAtmosphere('pink', 'lowpass', 300, 2, 0.15, 200); 
                     playDrone([146.8], 'sine'); 
                     break;
                case 'white-noise': // Explicit White Noise
                     playAtmosphere('white', 'highpass', 8000, 1, 0.1, 0); 
                     break;
                case 'cyber':
                    playDrone([55, 110], 'sawtooth', 5); // Low drone
                    playAtmosphere('white', 'highpass', 8000, 1, 0.1, 0); // Hiss
                    // Filter the drone
                    const filter = this.ctx.createBiquadFilter();
                    filter.type = 'lowpass';
                    filter.frequency.value = 200;
                    this.activeNodes[1].connect(filter); // Hijack the drone gain
                    this.activeNodes[1].disconnect(this.masterGain);
                    filter.connect(this.masterGain);
                    this.activeNodes.push(filter);
                    break;
                case 'forest':
                    playAtmosphere('pink', 'lowpass', 800, 0.5, 0.1, 200); // Wind
                    playDrone([220, 261.6, 329.6], 'triangle', 5); // Light chord
                    break;
                case 'lavender':
                    playAtmosphere('white', 'lowpass', 500, 0.2, 0.2, 200); // Gentle breeze
                    playAtmosphere('brown', 'lowpass', 150, 0, 0.1, 50); // Background rumble
                    break;
                case 'sunrise':
                    playDrone([261.6, 329.6, 392], 'sine'); // C Major chord
                    playAtmosphere('pink', 'lowpass', 400, 1, 0.1, 100); // Morning air
                    break;
            }
        },
        
        updateUI() {
            // Update the Taskbar Button (if exists - deprecated)
            const btn = document.getElementById('audio-toggle-btn');
            if(btn) {
                btn.textContent = this.enabled ? '🔊 Sound: ON ' : '🔇 Sound: OFF';
                btn.style.opacity = this.enabled ? '1' : '0.7';
            }
            
            // Settings Menu Checkbox removed

        }
    };

    // Expose ArisAudio to window for Settings Menu access
    window.ArisAudio = ArisAudio;

    // Helper to clear other backgrounds
    window.clearAllBackgrounds = function(except) {
        if (except !== 'aurora') window.manageAuroraBackground(false);
        if (except !== 'sunset') window.manageSunsetBackground(false);
        if (except !== 'coral') window.manageCoralBackground(false);
        if (except !== 'autumn') window.manageAutumnBackground(false);
        if (except !== 'cyber') window.manageCyberBackground(false);
        if (except !== 'lavender') window.manageLavenderBackground(false);
        if (except !== 'sunrise') window.manageSunriseBackground(false);
    }
    
    // --- New Background Functions ---

    window.manageCoralBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('coral-bg');
        if (isEnabled) {
            if (coralTimeout) { clearTimeout(coralTimeout); coralTimeout = null; }
            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'coral-bg';
                bg.style.cssText = `position: fixed; inset: 0; z-index: -10; opacity: 0; transition: opacity 0.8s; pointer-events: none; overflow: hidden;`;
                
                // Bubbles
                const bubbles = document.createElement('div');
                for(let i=0; i<30; i++) {
                    const b = document.createElement('div');
                    const size = Math.random() * 20 + 5;
                    b.style.cssText = `
                        position: absolute; bottom: -20px; left: ${Math.random()*100}%;
                        width: ${size}px; height: ${size}px; border-radius: 50%;
                        background: rgba(255,255,255,0.2);
                        animation: coral-bubble ${Math.random()*5 + 5}s infinite linear;
                        animation-delay: ${Math.random()*5}s;
                    `;
                    bubbles.appendChild(b);
                }
                bg.appendChild(bubbles);

                // Colors components
                const mainColor = isDarkMode ? '#1e1b4b' : '#0d9488';
                const secColor = isDarkMode ? '#312e81' : '#155e75';

                // SVG Coral - Full Screen immersive
                bg.innerHTML += `
                <svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute; inset:0; width:100%; height:100%; z-index: -1;">
                    <defs>
                        <linearGradient id="coralGradient" x1="0%" y1="100%" x2="0%" y2="0%">
                            <stop offset="0%" style="stop-color:${mainColor};stop-opacity:0.6" />
                            <stop offset="60%" style="stop-color:${mainColor};stop-opacity:0.2" />
                            <stop offset="100%" style="stop-color:${mainColor};stop-opacity:0" />
                        </linearGradient>
                    </defs>
                    
                    <!-- Background Ridge (Far) -->
                    <path d="M0 100 L0 50 Q 25 40 50 60 T 100 55 L 100 100 Z" fill="${isDarkMode ? '#0f172a' : '#115e59'}" opacity="0.3" />

                    <!-- Tall Seaweed / Kelp Left -->
                    <path d="M5 100 Q 0 75 5 50 T 5 10" stroke="${secColor}" stroke-width="0.5" fill="none" stroke-linecap="round" class="seaweed-sway" />
                    <path d="M8 100 Q 12 70 8 40 T 12 15" stroke="${secColor}" stroke-width="0.8" fill="none" stroke-linecap="round" class="seaweed-sway" style="animation-delay: 1s;" />

                    <!-- Tall Seaweed / Kelp Right -->
                    <path d="M90 100 Q 95 70 90 40 T 95 10" stroke="${secColor}" stroke-width="0.8" fill="none" stroke-linecap="round" class="seaweed-sway" style="animation-delay: 0.5s;" />
                    <path d="M95 100 Q 90 75 95 50 T 92 20" stroke="${secColor}" stroke-width="0.5" fill="none" stroke-linecap="round" class="seaweed-sway" style="animation-delay: 1.5s;" />

                    <!-- Main Coral Structures (Bottom) - Stretched higher -->
                    <path d="M0 100 L0 80 Q 10 70 15 80 T 30 75 T 45 80 T 60 70 T 80 80 T 100 60 L 100 100 Z" fill="url(#coralGradient)" />
                             
                    <!-- Fish (Simple shapes) -->
                    <g class="fish-swim" style="transform:translate(110%, 40%);">
                        <path d="M0 0 L 8 4 L 0 8 L 2 4 Z" fill="${isDarkMode ? '#fbbf24' : '#fcd34d'}" opacity="0.6" />
                    </g>
                     <g class="fish-swim" style="transform:translate(110%, 60%); animation-duration: 18s; animation-delay: 2s;">
                        <path d="M0 0 L 10 5 L 0 10 L 3 5 Z" fill="${isDarkMode ? '#f87171' : '#fda4af'}" opacity="0.6" />
                    </g>
                </svg>
                <style>
                    .seaweed-sway { transform-origin: 50% 100%; animation: kelpSway 6s infinite ease-in-out alternate; vector-effect: non-scaling-stroke; }
                    @keyframes kelpSway { from { transform: scaleX(1) skewX(0deg); } to { transform: scaleX(0.9) skewX(2deg); } }
                    .fish-swim { animation: fishSwim 20s infinite linear; }
                    @keyframes fishSwim { from { transform: translateX(105vw) scale(1); } to { transform: translateX(-10vw) scale(1); } }
                </style>
                `;

                // Keyframes
                 if (!document.getElementById('coral-keyframes')) {
                    const s = document.createElement('style');
                    s.id = 'coral-keyframes';
                    s.textContent = `@keyframes coral-bubble { 0% { transform: translateY(0) translateX(0); opacity: 0; } 10% { opacity: 0.5; } 100% { transform: translateY(-120vh) translateX(${Math.random()*50-25}px); opacity: 0; } }`;
                    document.head.appendChild(s);
                 }

                document.body.appendChild(bg);
                void bg.offsetWidth;
            }

            // Colors
            if (isDarkMode) {
                 bg.style.background = 'linear-gradient(to bottom, #020617, #1e1b4b, #312e81)'; // Deep ocean
            } else {
                 bg.style.background = 'linear-gradient(to bottom, #67e8f9, #22d3ee, #0891b2)'; // Tropical water
            }
            requestAnimationFrame(() => bg.style.opacity = '1');

        } else if (bg) {
             bg.style.opacity = '0';
             if (coralTimeout) clearTimeout(coralTimeout);
             coralTimeout = setTimeout(() => { if(document.getElementById('coral-bg')) document.getElementById('coral-bg').remove(); }, 800);
        }
    };

    window.manageAutumnBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('autumn-bg');
        if (isEnabled) {
            if (autumnTimeout) { clearTimeout(autumnTimeout); autumnTimeout = null; }
            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'autumn-bg';
                bg.style.cssText = `position: fixed; inset: 0; z-index: -10; opacity: 0; transition: opacity 0.8s; pointer-events: none; overflow: hidden;`;
                
                // Falling leaves (Background)
                for(let i=0; i<20; i++) {
                    const leaf = document.createElement('div');
                    leaf.textContent = ['🍂','🍁'][Math.floor(Math.random()*2)];
                    leaf.style.cssText = `
                        position: absolute; top: -50px; left: ${Math.random()*100}%;
                        font-size: ${Math.random()*20 + 20}px;
                        opacity: 0.7;
                        animation: autumn-fall ${Math.random()*5 + 8}s infinite linear;
                        animation-delay: ${Math.random()*5}s;
                        z-index: 1;
                    `;
                    bg.appendChild(leaf);
                }

                // Big Corner Leaves (Foreground Frame)
                const cornerLeaves = [
                    // Top Left
                    { css: 'top: -10vh; left: -5vw; --base-rot: 135deg;', emoji: '🍁', delay: '0s' },
                    // Top Right
                    { css: 'top: -8vh; right: -5vw; --base-rot: -135deg;', emoji: '🍂', delay: '1.2s' },
                    // Bottom Left
                    { css: 'bottom: -10vh; left: -2vw; --base-rot: 45deg;', emoji: '🍂', delay: '0.5s' },
                    // Bottom Right
                    { css: 'bottom: -8vh; right: -5vw; --base-rot: -45deg;', emoji: '🍁', delay: '2.5s' }
                ];

                cornerLeaves.forEach(data => {
                    const cl = document.createElement('div');
                    cl.textContent = data.emoji;
                    // Use CSS Variable for base rotation to allow animation relative to it
                    cl.style.cssText = `
                        position: absolute; ${data.css}
                        font-size: 25vh;
                        opacity: 0.4;
                        z-index: 0;
                        filter: drop-shadow(0 0 10px rgba(0,0,0,0.1));
                        
                        transform: rotate(var(--base-rot));
                        animation: autumn-rustle 5s infinite ease-in-out alternate;
                        animation-delay: ${data.delay};
                    `;
                    bg.appendChild(cl);
                });

                 if (!document.getElementById('autumn-keyframes')) {
                    const s = document.createElement('style');
                    s.id = 'autumn-keyframes';
                    s.textContent = `
                        @keyframes autumn-fall { 
                             0% { transform: translateY(0) rotate(0deg); opacity: 0; } 
                             10% { opacity: 0.8; } 
                             100% { transform: translateY(110vh) rotate(360deg) translateX(30px); opacity: 0; } 
                        }
                        @keyframes autumn-rustle { 
                            from { transform: rotate(var(--base-rot)) scale(1); } 
                            to { transform: rotate(calc(var(--base-rot) + 8deg)) scale(1.05); } 
                        }
                    `;
                    document.head.appendChild(s);
                 }

                document.body.appendChild(bg);
                void bg.offsetWidth;
            }
            
            if (isDarkMode) {
                bg.style.background = 'linear-gradient(to bottom right, #451a03, #78350f)'; // Brown/Oak
            } else {
                 bg.style.background = 'linear-gradient(to bottom right, #fef3c7, #fb923c, #b45309)'; // Golden Hour
            }
            requestAnimationFrame(() => bg.style.opacity = '1');

        } else if (bg) {
             bg.style.opacity = '0';
             if (autumnTimeout) clearTimeout(autumnTimeout);
             autumnTimeout = setTimeout(() => { if(document.getElementById('autumn-bg')) document.getElementById('autumn-bg').remove(); }, 800);
        }
    };

    window.manageCyberBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('cyber-bg');
        if (isEnabled) {
            if (cyberTimeout) { clearTimeout(cyberTimeout); cyberTimeout = null; }
            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'cyber-bg';
                bg.style.cssText = `position: fixed; inset: 0; z-index: -10; opacity: 0; transition: opacity 0.8s; pointer-events: none; overflow: hidden;`;
                
                // Colors for Cyber Elements
                const neonOne = isDarkMode ? '#00FFFF' : '#0ea5e9'; // Cyan related
                const neonTwo = isDarkMode ? '#FF00FF' : '#8b5cf6'; // Magenta/Purple related
                const pipeColor = isDarkMode ? '#334155' : '#cbd5e1'; // Dark/Light Slate
                
                bg.innerHTML = `
                    <!-- Background Grid -->
                    <div id="cyber-grid" style="position: absolute; bottom: 0; left: 0; width: 200%; height: 100%; transform-origin: 50% 100%;"></div>

                    <!-- Tech SVG Overlay -->
                    <svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute; inset:0; width:100%; height:100%; opacity: 0.8; pointer-events:none;">
                         <defs>
                             <filter id="neon-glow" x="-50%" y="-50%" width="200%" height="200%">
                                <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
                                <feMerge>
                                    <feMergeNode in="coloredBlur"/>
                                    <feMergeNode in="SourceGraphic"/>
                                </feMerge>
                             </filter>
                             <pattern id="hex-pattern" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                                <path d="M10 0 L20 5 L20 15 L10 20 L0 15 L0 5 Z" fill="none" stroke="${pipeColor}" stroke-opacity="0.1" />
                             </pattern>
                         </defs>
                         
                         <!-- Geometric HUD Left -->
                         <path d="M0 0 L 20 0 L 25 5 L 25 30 L 20 35 L 0 35" fill="none" stroke="${neonOne}" stroke-width="0.5" opacity="0.5" />
                         <rect x="2" y="2" width="10" height="10" fill="none" stroke="${neonOne}" stroke-width="0.2" opacity="0.3" />
                         <text x="2" y="18" fill="${neonOne}" font-size="2" font-family="monospace" opacity="0.6">SYS.RDY</text>

                         <!-- Futuristic Circuit Pipes (Static) -->
                         <!-- Top Right Cluster -->
                         <path d="M60 0 V 10 L 70 20 H 100" fill="none" stroke="${pipeColor}" stroke-width="1.5" />
                         <circle cx="70" cy="20" r="1.5" fill="${neonTwo}" filter="url(#neon-glow)" opacity="0.8" />
                         <path d="M80 0 V 15 L 85 20 H 100" fill="none" stroke="${pipeColor}" stroke-width="0.8" />

                         <!-- Bottom Left Cluster -->
                         <path d="M0 80 H 10 L 20 90 V 100" fill="none" stroke="${pipeColor}" stroke-width="2" />
                         <path d="M0 85 H 15 L 25 95 V 100" fill="none" stroke="${pipeColor}" stroke-width="1" />
                         <circle cx="20" cy="90" r="2" fill="${neonOne}" filter="url(#neon-glow)" />

                         <!-- Center Detail -->
                         <rect x="40" y="45" width="20" height="10" rx="2" fill="none" stroke="${neonTwo}" stroke-width="0.5" opacity="0.4" />
                         <path d="M40 50 H 60" stroke="${neonTwo}" stroke-width="0.2" opacity="0.3" />
                         
                         <!-- Neon Accents -->
                         <circle cx="42" cy="50" r="1" fill="${neonOne}" class="neon-pulse" />
                         <circle cx="58" cy="50" r="1" fill="${neonOne}" class="neon-pulse" style="animation-delay: 0.5s;" />
                         
                         <!-- Random Data decorations (Right side) -->
                         <path d="M95 40 V 60" stroke="${pipeColor}" stroke-width="0.5" />
                         <rect x="92" y="42" width="6" height="1" fill="${neonOne}" opacity="0.5" />
                         <rect x="92" y="45" width="4" height="1" fill="${neonOne}" opacity="0.3" />
                         <rect x="92" y="55" width="6" height="1" fill="${neonTwo}" opacity="0.5" />
                    </svg>

                    <style>
                        .neon-pulse { animation: neonPulse 2s infinite ease-in-out alternate; }
                        @keyframes neonPulse { from { opacity: 0.3; transform: scale(0.8); } to { opacity: 1; transform: scale(1.2); filter: drop-shadow(0 0 2px currentColor); } }
                    </style>
                `;
                
                // Set Grid Style
                const gridDiv = bg.querySelector('#cyber-grid');
                gridDiv.style.cssText += `
                    background-image: 
                        linear-gradient(rgba(0, 255, 255, 0.3) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(0, 255, 255, 0.3) 1px, transparent 1px);
                    background-size: 50px 50px;
                    transform: perspective(500px) rotateX(60deg) translateY(10%);
                    animation: cyber-grid 20s infinite linear;
                `;

                 if (!document.getElementById('cyber-keyframes')) {
                    const s = document.createElement('style');
                    s.id = 'cyber-keyframes';
                    s.textContent = `@keyframes cyber-grid { from { transform: perspective(500px) rotateX(60deg) translateY(0); } to { transform: perspective(500px) rotateX(60deg) translateY(50px); } }`;
                    document.head.appendChild(s);
                 }

                document.body.appendChild(bg);
                void bg.offsetWidth;
            }

            if (isDarkMode) {
                bg.style.background = 'linear-gradient(to bottom, #000000, #1e1b4b)'; // Black space
                const gridDiv = bg.querySelector('#cyber-grid');
                if(gridDiv) gridDiv.style.backgroundImage = 'linear-gradient(rgba(255,20,147,0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(0,255,255,0.3) 1px, transparent 1px)'; // Neon grid
            } else {
                 bg.style.background = 'linear-gradient(to bottom, #f0f9ff, #e0f2fe)'; // White/Clean
                 const gridDiv = bg.querySelector('#cyber-grid');
                 if(gridDiv) gridDiv.style.backgroundImage = 'linear-gradient(rgba(14,165,233, 0.2) 1px, transparent 1px), linear-gradient(90deg, rgba(14,165,233, 0.2) 1px, transparent 1px)'; // Blue grid
            }
            requestAnimationFrame(() => bg.style.opacity = '1');

        } else if (bg) {
             bg.style.opacity = '0';
             if (cyberTimeout) clearTimeout(cyberTimeout);
             cyberTimeout = setTimeout(() => { if(document.getElementById('cyber-bg')) document.getElementById('cyber-bg').remove(); }, 800);
        }
    };

    window.manageSunriseBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('sunrise-bg');
        if (isEnabled) {
            if (sunriseTimeout) { clearTimeout(sunriseTimeout); sunriseTimeout = null; }
            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'sunrise-bg';
                bg.style.cssText = `position: fixed; inset: 0; z-index: -10; opacity: 0; transition: opacity 1.5s; pointer-events: none; overflow: hidden;`;
                
                // SVG Scene
                bg.innerHTML = `
                    <div id="sunrise-sky" style="position: absolute; inset: 0;"></div>
                    
                    <!-- Sun Rising -->
                    <div id="sunrise-sun" style="position: absolute; left: 50%; width: 15vh; height: 15vh; background: #fbbf24; border-radius: 50%; transform: translateX(-50%); box-shadow: 0 0 50px #f59e0b;"></div>
                    
                    <!-- Clouds -->
                    <div style="position: absolute; top: 20%; left: 10%; width: 120px; height: 40px; background: rgba(255,255,255,0.6); border-radius: 50px; filter: blur(5px); animation: cloud-float 40s linear infinite;"></div>
                    <div style="position: absolute; top: 15%; right: 20%; width: 180px; height: 60px; background: rgba(255,255,255,0.5); border-radius: 50px; filter: blur(8px); animation: cloud-float 50s linear infinite reverse;"></div>
                    
                    <!-- Mountains / Horizon -->
                     <svg viewBox="0 0 100 20" preserveAspectRatio="none" style="position:absolute; bottom:0; left:0; width:100%; height:25vh;">
                         <path d="M0 20 L20 10 L40 18 L60 5 L80 15 L100 8 L100 20 Z" fill="#334155" opacity="0.3" />
                         <path d="M0 20 L30 15 L60 20 L100 12 L100 20 Z" fill="#1e293b" opacity="0.5" />
                     </svg>

                     <style>
                        #sunrise-sun { bottom: -20vh; animation: sunrise-up 3s ease-out forwards 0.5s; }
                        @keyframes sunrise-up { 
                            from { bottom: -20vh; opacity: 0.5; } 
                            to { bottom: 30vh; opacity: 1; } 
                        }
                        @keyframes cloud-float { from { transform: translateX(0); } to { transform: translateX(20px); } }
                    </style>
                `;

                document.body.appendChild(bg);
                void bg.offsetWidth;
            }

            // Colors
             const sun = document.querySelector('#sunrise-sun');
             if (isDarkMode) {
                bg.querySelector('#sunrise-sky').style.background = 'linear-gradient(to bottom, #1e1b4b, #4c1d95, #c026d3)'; // Deep dawn
                if(sun) {
                     sun.style.background = '#fcd34d';
                     sun.style.boxShadow = '0 0 30px #d97706';
                }
            } else {
                 bg.querySelector('#sunrise-sky').style.background = 'linear-gradient(to bottom, #7dd3fc, #f472b6, #fb923c)'; // Bright morning
                  if(sun) {
                     sun.style.background = '#fbbf24';
                     sun.style.boxShadow = '0 0 60px #f59e0b';
                }
            }

            requestAnimationFrame(() => bg.style.opacity = '1');

        } else if (bg) {
             bg.style.opacity = '0';
             if (sunriseTimeout) clearTimeout(sunriseTimeout);
             sunriseTimeout = setTimeout(() => { if(document.getElementById('sunrise-bg')) document.getElementById('sunrise-bg').remove(); }, 1500);
        }
    };

    window.manageLavenderBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('lavender-bg');
        if (isEnabled) {
            if (lavenderTimeout) { clearTimeout(lavenderTimeout); lavenderTimeout = null; }
            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'lavender-bg';
                bg.style.cssText = `position: fixed; inset: 0; z-index: -10; opacity: 0; transition: opacity 0.8s; pointer-events: none; overflow: hidden;`;
                
                // Construct the Lavender Field Scene
                // 1. Sky/Atmosphere (Gradient) handled by bg styles
                // 2. Distant Hills
                // 3. Rolling Field Rows
                // 4. Foreground Plants (Procedural)
                // 5. Floating Pollen/Fireflies

                bg.innerHTML = `
                    <div id="lavender-sky" style="position: absolute; inset:0;"></div>
                    
                    <svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position: absolute; bottom: 0; left: 0; width: 100%; height: 60vh;">
                        <defs>
                             <filter id="windBlur">
                                <feGaussianBlur in="SourceGraphic" stdDeviation="0.3" />
                            </filter>
                        </defs>

                        <!-- Distant Hills -->
                        <path d="M0 40 Q 20 30 40 45 T 80 40 T 100 50 V 100 H 0 Z" fill="var(--hill-color)" opacity="0.6" />
                        
                        <!-- Field Row Back -->
                        <path d="M0 60 Q 30 50 60 65 T 100 60 V 100 H 0 Z" fill="var(--field-back)" />

                        <!-- Field Row Mid -->
                        <path d="M0 80 Q 40 70 70 85 T 100 80 V 100 H 0 Z" fill="var(--field-mid)" />

                        <!-- Foreground (Detailed Stems) -->
                        <g id="lavender-foreground" fill="none" stroke-width="0.8" stroke-linecap="round">
                             <!-- Simulating grass/stems -->
                             ${Array.from({length: 50}).map((_, i) => {
                                 const x = Math.random() * 105 - 2; // -2 to 103 width
                                 const h = 15 + Math.random() * 25; // Height%
                                 const delay = Math.random() * 2;
                                 return `
                                    <path d="M${x} 100 Q ${x - 1 + Math.random()*2} ${100 - h/2} ${x + (Math.random()-0.5)*4} ${100 - h}" stroke="var(--stem-color)" class="lavender-sway" style="animation-delay: -${delay}s" />
                                    <circle cx="${x + (Math.random()-0.5)*4}" cy="${100 - h}" r="1.5" fill="var(--flower-color)" class="lavender-sway" style="animation-delay: -${delay}s" opacity="0.9"/>
                                    <circle cx="${x + (Math.random()-0.5)*4}" cy="${100 - h + 2}" r="1.2" fill="var(--flower-color)" class="lavender-sway" style="animation-delay: -${delay}s" opacity="0.9"/>
                                    <circle cx="${x + (Math.random()-0.5)*4}" cy="${100 - h + 4}" r="1.0" fill="var(--flower-color)" class="lavender-sway" style="animation-delay: -${delay}s" opacity="0.9"/>
                                 `;
                             }).join('')}
                        </g>
                    </svg>

                    <!-- Fireflies / Pollen -->
                    <div id="lavender-particles"></div>

                    <style>
                        .lavender-sway { transform-origin: 50% 100%; animation: fieldSway 3s ease-in-out infinite alternate; vector-effect: non-scaling-stroke; }
                        @keyframes fieldSway { from { transform: skewX(-2deg) rotate(0.5deg); } to { transform: skewX(2deg) rotate(-0.5deg); } }
                    </style>
                `;

                // Add Particles
                const particleContainer = bg.querySelector('#lavender-particles');
                for(let i=0; i<30; i++) {
                    const p = document.createElement('div');
                    p.style.cssText = `
                        position: absolute; bottom: ${Math.random() * 50}%; left: ${Math.random() * 100}%;
                        width: 3px; height: 3px; background: white; border-radius: 50%;
                        opacity: 0.6; filter: blur(1px);
                        animation: floatParticle ${5 + Math.random() * 5}s linear infinite;
                         animation-delay: -${Math.random() * 5}s;
                    `;
                    particleContainer.appendChild(p);
                }
                
                 if (!document.getElementById('lavender-keyframes')) {
                    const s = document.createElement('style');
                    s.id = 'lavender-keyframes';
                    s.textContent = `@keyframes floatParticle { 0% { transform: translateY(0) translateX(0); opacity: 0; } 50% { opacity: 0.8; } 100% { transform: translateY(-30vh) translateX(${Math.random()*20 - 10}vw); opacity: 0; } }`;
                    document.head.appendChild(s);
                 }

                document.body.appendChild(bg);
                void bg.offsetWidth;
            }

            // Colors
            if (isDarkMode) {
                // Night Field (Moonlight)
                bg.style.setProperty('--hill-color', '#4c1d95');
                bg.style.setProperty('--field-back', '#5b21b6');
                bg.style.setProperty('--field-mid', '#6d28d9');
                bg.style.setProperty('--stem-color', '#14532d'); // Dark Green
                bg.style.setProperty('--flower-color', '#a78bfa'); // Light Purple
                bg.querySelector('#lavender-sky').style.background = 'linear-gradient(to bottom, #020617, #1e1b4b, #312e81)';
                // Fireflies check
                bg.querySelectorAll('#lavender-particles div').forEach(p => {
                    p.style.background = '#fef08a'; // Yellow firefly
                    p.style.boxShadow = '0 0 4px #facc15';
                });
            } else {
                // Day Field (Sunset/Day)
                bg.style.setProperty('--hill-color', '#c4b5fd');
                bg.style.setProperty('--field-back', '#a78bfa');
                bg.style.setProperty('--field-mid', '#8b5cf6');
                bg.style.setProperty('--stem-color', '#15803d'); // Green
                bg.style.setProperty('--flower-color', '#d8b4fe'); // Pinkish Purple
                bg.querySelector('#lavender-sky').style.background = 'linear-gradient(to bottom, #e0f2fe, #e9d5ff, #f3e8ff)';
                 bg.querySelectorAll('#lavender-particles div').forEach(p => {
                    p.style.background = '#fff'; // White pollen
                    p.style.boxShadow = 'none';
                });
            }
            requestAnimationFrame(() => bg.style.opacity = '1');

        } else if (bg) {
             bg.style.opacity = '0';
             if (lavenderTimeout) clearTimeout(lavenderTimeout);
             lavenderTimeout = setTimeout(() => { if(document.getElementById('lavender-bg')) document.getElementById('lavender-bg').remove(); }, 800);
        }
    };

    window.manageSunsetBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('sunset-bg');

        if (isEnabled) {
             if (sunsetTimeout) {
                clearTimeout(sunsetTimeout);
                sunsetTimeout = null;
            }

            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'sunset-bg';
                // Fixed position background
                bg.style.cssText = `
                    position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -10;
                    overflow: hidden; pointer-events: none; opacity: 0; transition: opacity 0.8s;
                `;
                
                // SVG Graphic for Sunset scene
                // 1. Sky Gradient (handled in JS based on mode)
                // 2. Sun (Circle)
                // 3. Ocean (Bottom Rect)
                // 4. Palm Tree (Path)

                bg.innerHTML = `
                    <div id="sunset-sky" style="position:absolute; inset:0; z-index:0;"></div>
                    <div id="sunset-sun" style="position:absolute; bottom: 25%; left: 50%; width: 15vh; height: 15vh; transform: translateX(-50%); background: #fbbf24; border-radius: 50%; box-shadow: 0 0 40px #f59e0b; z-index:1;"></div>
                    <div id="sunset-ocean" style="position:absolute; bottom:0; left:0; width:100%; height:25%; background: linear-gradient(to bottom, #1e3a8a, #0f172a); z-index:2;"></div>
                    <!-- Animated Palm Tree SVG -->
                    <svg viewBox="0 0 100 100" style="position:absolute; bottom:0; right:5%; height:60vh; width:auto; z-index:3; filter: drop-shadow(2px 2px 2px rgba(0,0,0,0.3));">
                         <g transform-origin="50 100">
                             <!-- Trunk -->
                             <path d="M50 100 Q 45 70 60 50 Q 65 45 60 40" stroke="#8B4513" stroke-width="3" fill="none" stroke-linecap="round" />
                             <!-- Leaves -->
                             <path d="M60 40 Q 40 30 30 50" stroke="#10b981" stroke-width="2" fill="none" class="palm-leaf" />
                             <path d="M60 40 Q 50 20 40 30" stroke="#10b981" stroke-width="2" fill="none" class="palm-leaf" />
                             <path d="M60 40 Q 70 10 60 20" stroke="#10b981" stroke-width="2" fill="none" class="palm-leaf" />
                             <path d="M60 40 Q 90 20 80 40" stroke="#10b981" stroke-width="2" fill="none" class="palm-leaf" />
                             <path d="M60 40 Q 90 50 85 70" stroke="#10b981" stroke-width="2" fill="none" class="palm-leaf" />
                         </g>
                    </svg>
                    
                    <style>
                        #sunset-sun { animation: sunset-glow 4s infinite alternate ease-in-out; }
                        @keyframes sunset-glow { from { box-shadow: 0 0 20px #f59e0b; } to { box-shadow: 0 0 60px #fbbf24; transform: translateX(-50%) scale(1.1); } }
                        .palm-leaf { transform-origin: 60px 40px; animation: palm-sway 3s infinite ease-in-out alternate; }
                        .palm-leaf:nth-child(2) { animation-delay: 0.5s; }
                        .palm-leaf:nth-child(3) { animation-delay: 1.0s; }
                        @keyframes palm-sway { from { transform: rotate(-2deg); } to { transform: rotate(2deg); } }
                    </style>
                `;
                document.body.appendChild(bg);
                void bg.offsetWidth; 
            }

            // Update Colors based on Mode
            const sky = document.getElementById('sunset-sky');
            const ocean = document.getElementById('sunset-ocean');
            const sun = document.getElementById('sunset-sun');
            
            if (isDarkMode) {
                // Twilight/Night Sunset
                if (sky) sky.style.background = 'linear-gradient(to bottom, #0f172a 0%, #312e81 60%, #c026d3 100%)'; // Dark Purple/Navy
                if (ocean) ocean.style.background = 'linear-gradient(to bottom, #1e1b4b, #020617)';
                if (sun) {
                     sun.style.background = '#fbbf24'; // Moon or dark sun? Let's keep it a setting sun
                     sun.style.boxShadow = '0 0 30px #d97706';
                     sun.style.opacity = '0.8';
                     sun.style.bottom = '20%'; // Lower
                }
            } else {
                // Bright Sunset
                if (sky) sky.style.background = 'linear-gradient(to bottom, #38bdf8 0%, #f472b6 60%, #fb923c 100%)'; // Blue to Pink to Orange
                if (ocean) ocean.style.background = 'linear-gradient(to bottom, #0ea5e9, #0369a1)';
                if (sun) {
                    sun.style.opacity = '1';
                    sun.style.bottom = '30%'; // Higher
                    sun.style.boxShadow = '0 0 50px #fbbf24';
                }
            }

            requestAnimationFrame(() => {
                 if(bg) bg.style.opacity = '1';
            });
        } else {
             // Disable
            if (bg) {
                bg.style.opacity = '0';
                if (sunsetTimeout) clearTimeout(sunsetTimeout);
                sunsetTimeout = setTimeout(() => { 
                    const el = document.getElementById('sunset-bg');
                    if (el) el.remove(); 
                    sunsetTimeout = null;
                }, 800);
            }
        }
    }

    window.manageAuroraBackground = function(isEnabled, isDarkMode) {
        let bg = document.getElementById('aurora-night-bg');
        
        if (isEnabled) {
            // Cancel any pending removal
            if (auroraTimeout) {
                clearTimeout(auroraTimeout);
                auroraTimeout = null;
            }

            if (!bg) {
                bg = document.createElement('div');
                bg.id = 'aurora-night-bg';
                bg.style.cssText = `
                    position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -10;
                    overflow: hidden; pointer-events: none; opacity: 0; transition: opacity 0.5s;
                `;
                
                // Container for stars
                const starsContainer = document.createElement('div');
                starsContainer.id = 'aurora-stars';
                bg.appendChild(starsContainer);

                // Stars
                for (let i = 0; i < 50; i++) {
                    const star = document.createElement('div');
                    const size = Math.random() * 2 + 1;
                    star.style.cssText = `
                        position: absolute;
                        top: ${Math.random() * 100}%;
                        left: ${Math.random() * 100}%;
                        width: ${size}px; height: ${size}px;
                        background: white;
                        border-radius: 50%;
                        opacity: ${Math.random() * 0.7 + 0.3};
                        animation: aurora-twinkle ${Math.random() * 3 + 2}s infinite alternate;
                        box-shadow: 0 0 ${size*2}px rgba(255,255,255,0.8);
                    `;
                    starsContainer.appendChild(star);
                }
                // Aurora Veil (Animation layer)
                const veil = document.createElement('div');
                veil.id = 'aurora-veil'; 
                veil.style.cssText = `
                    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                    background: linear-gradient(120deg, transparent 0%, rgba(52, 211, 153, 0.1) 40%, rgba(167, 139, 250, 0.1) 60%, transparent 100%);
                    filter: blur(40px); opacity: 0.6;
                    animation: aurora-shift 15s infinite ease-in-out alternate;
                `;
                bg.appendChild(veil);

                document.body.appendChild(bg);
                
                // Force reflow to ensure transition plays
                void bg.offsetWidth;

                // Add keyframes if not present
                if (!document.getElementById('aurora-keyframes')) {
                    const style = document.createElement('style');
                    style.id = 'aurora-keyframes';
                    style.textContent = `
                        @keyframes aurora-twinkle { 0% { opacity: 0.3; transform: scale(0.8); } 100% { opacity: 0.9; transform: scale(1.1); } }
                        @keyframes aurora-shift { 0% { transform: translateX(-10%) translateY(5%); } 100% { transform: translateX(10%) translateY(-5%); } }
                    `;
                    document.head.appendChild(style);
                }
            }
            
            // Update styles based on mode
            const starsContainer = document.getElementById('aurora-stars');
            const veil = document.getElementById('aurora-veil');

            if (isDarkMode) {
                bg.style.background = `
                    radial-gradient(circle at 50% 120%, rgba(16, 185, 129, 0.25), transparent 50%),
                    radial-gradient(ellipse at 20% 40%, rgba(59, 130, 246, 0.15), transparent 40%),
                    radial-gradient(ellipse at 80% 30%, rgba(139, 92, 246, 0.15), transparent 40%),
                    #0f172a
                `;
                if (starsContainer) {
                    starsContainer.style.display = 'block';
                    Array.from(starsContainer.children).forEach(star => {
                        const size = parseFloat(star.style.width);
                        star.style.background = 'white';
                        star.style.boxShadow = `0 0 ${size*2}px rgba(255,255,255,0.8)`;
                    });
                }
                if (veil) {
                    // Subtle veil for dark mode
                    veil.style.background = 'linear-gradient(120deg, transparent 0%, rgba(52, 211, 153, 0.1) 40%, rgba(167, 139, 250, 0.1) 60%, transparent 100%)';
                }
            } else {
                 // Bright Mode: Organic spots of color on light background
                 bg.style.background = `
                    radial-gradient(circle at 50% 120%, rgba(52, 211, 153, 0.4), transparent 60%),
                    radial-gradient(ellipse at 20% 40%, rgba(96, 165, 250, 0.3), transparent 50%),
                    radial-gradient(ellipse at 80% 30%, rgba(167, 139, 250, 0.3), transparent 50%),
                    #f8fafc
                 `;
                 
                 if (starsContainer) {
                    starsContainer.style.display = 'block';
                    // Gold/Amber stars for visibility on bright background
                    Array.from(starsContainer.children).forEach(star => {
                        const size = parseFloat(star.style.width);
                        star.style.background = '#fbbf24'; 
                        star.style.boxShadow = `0 0 ${size*2}px 2px rgba(245, 158, 11, 0.6)`; 
                    });
                }
                if (veil) {
                    // More vibrant veil for bright mode
                    veil.style.background = 'linear-gradient(120deg, transparent 0%, rgba(16, 185, 129, 0.4) 40%, rgba(139, 92, 246, 0.4) 60%, transparent 100%)';
                }
            }

            // Ensure fade in happens even if it existed but was fading out
            requestAnimationFrame(() => {
                 if(bg) bg.style.opacity = '1';
            });

        } else {
            // Disable
            if (bg) {
                bg.style.opacity = '0';
                // Debounce removal
                if (auroraTimeout) clearTimeout(auroraTimeout);
                auroraTimeout = setTimeout(() => { 
                    const el = document.getElementById('aurora-night-bg');
                    if (el) el.remove(); 
                    auroraTimeout = null;
                }, 500);
            }
        }
    };

    window.applyArisTheme = function() {
        const storedDarkMode = localStorage.getItem('arisEduDarkMode');
        const darkMode = storedDarkMode === null ? true : storedDarkMode === 'true';
        const colorTheme = localStorage.getItem('arisEduColorTheme') || 'blue-green';
        let activeGradient = gradients[colorTheme] || gradients['blue-green'];

        // --- Extract Colors for SVG Usage ---
        // Simple regex to extract hex or rgb colors from the gradient string
        const colorMatches = activeGradient.match(/#[0-9a-fA-F]{3,6}|rgba?\(.*?\)/g);
        if (colorMatches && colorMatches.length >= 2) {
            document.documentElement.style.setProperty('--theme-color-1', colorMatches[0]);
            document.documentElement.style.setProperty('--theme-color-2', colorMatches[1]);
            document.documentElement.style.setProperty('--theme-color-3', colorMatches[2] || colorMatches[1]);
        } else {
             // Fallback
            document.documentElement.style.setProperty('--theme-color-1', '#3b82f6');
            document.documentElement.style.setProperty('--theme-color-2', '#10b981');
            document.documentElement.style.setProperty('--theme-color-3', '#8b5cf6');
        }

        // Apply dark mode class
        document.body.classList.toggle('dark-mode', darkMode);

        // Special Themes List (Backgrounds that need transparency)
        const specialBackgrounds = ['aurora', 'sunset', 'coral', 'autumn', 'cyber', 'lavender', 'sunrise', 'blue-green'];
        
        // Determine effective background
        const storedBackground = localStorage.getItem('arisEduBackgroundTheme');
        let effectiveBackground = (storedBackground && storedBackground !== 'default') ? storedBackground : colorTheme;
        if (effectiveBackground === 'blue-green') effectiveBackground = 'aurora';
        
        const isSpecialBackground = specialBackgrounds.includes(effectiveBackground);

        // Background Logic
        if (isSpecialBackground) {
             document.body.style.background = 'transparent';
        } else {
             // Standard Themes
             if (darkMode) {
                 document.body.style.background = ''; // Default dark
             } else {
                 document.body.style.background = activeGradient;
             }
        }

        // Manage Interactive Backgrounds
        window.clearAllBackgrounds(effectiveBackground);

        if (effectiveBackground === 'aurora') window.manageAuroraBackground(true, darkMode);
        else if (effectiveBackground === 'sunset') window.manageSunsetBackground(true, darkMode);
        else if (effectiveBackground === 'coral') window.manageCoralBackground(true, darkMode);
        else if (effectiveBackground === 'autumn') window.manageAutumnBackground(true, darkMode);
        else if (effectiveBackground === 'cyber') window.manageCyberBackground(true, darkMode);
        else if (effectiveBackground === 'lavender') window.manageLavenderBackground(true, darkMode);
        else if (effectiveBackground === 'sunrise') window.manageSunriseBackground(true, darkMode);


        // Apply to taskbar if exists
        const taskbar = document.querySelector('.taskbar');
        if (taskbar) {
             taskbar.style.removeProperty('background'); 
             taskbar.style.backgroundImage = activeGradient;
             
             // Audio Button Injection - REMOVED (Moved to Settings Menu)
             /*
             if (!document.getElementById('audio-toggle-btn')) {
                 const btn = document.createElement('button');
                 btn.id = 'audio-toggle-btn';
                 btn.className = 'taskbar-button';
                 btn.textContent = '🔇 Sound: OFF';
                 btn.onclick = () => {
                     const isEnabled = !ArisAudio.enabled;
                     ArisAudio.toggle(isEnabled);
                 };
                 // Insert before Settings or Login
                 const settingsBtn = document.getElementById('settings-button');
                 if(settingsBtn && settingsBtn.parentNode) settingsBtn.parentNode.insertBefore(btn, settingsBtn);
                 else taskbar.appendChild(btn);
             }
             */

        }
        
        // Update Audio Theme if enabled
        if (ArisAudio.enabled) {
            ArisAudio.playTheme(colorTheme);
        } else {
            ArisAudio.currentTheme = colorTheme; // Just update tracker
        }

        // --- Preferences Page Specifics ---
        const settingsContainer = document.querySelector('.settings-container');
        const sidebar = document.querySelector('aside');
        const sidebarTitle = document.querySelector('aside h2');
        const settingsMenu = document.getElementById('settings-menu'); // The dropdown menu

        if (settingsContainer) {
             // In Dark Mode + Special Theme: Solid dark background to read text
             // In Light Mode + Special Theme: Glassy white
             
             if (darkMode) {
                 settingsContainer.style.background = '#1e293b'; // Slate-800 for container
                 settingsContainer.style.color = '#e2e8f0';
             } else {
                 // Light Mode
                 if (isSpecialBackground) {
                     // On special backgrounds, make container white glassy.
                     settingsContainer.style.background = 'rgba(255, 255, 255, 0.85)';
                     settingsContainer.style.backdropFilter = 'blur(10px)';
                     settingsContainer.style.color = '#0f172a';
                 } else {
                     // Other themes: Container takes the gradient.
                     settingsContainer.style.background = activeGradient;
                     settingsContainer.style.color = '#0f172a';
                 }
             }
        }

        if (sidebar) {
            if (darkMode) {
                sidebar.style.background = '#0f172a'; // Darker than container
                sidebar.style.color = '#cbd5e1';
            } else {
                sidebar.style.background = '#e0e7ef'; // Original Light Gray
                sidebar.style.color = '#0f172a';
            }
        }

        if (sidebarTitle) {
            sidebarTitle.style.backgroundImage = activeGradient;
            sidebarTitle.style.backgroundClip = 'text';
            sidebarTitle.style.webkitBackgroundClip = 'text';
            sidebarTitle.style.color = 'transparent';
        }

        if (settingsMenu) {
             // Dropdown menu styling
             settingsMenu.style.background = darkMode ? '#1e293b' : '#ffffff';
             settingsMenu.style.color = darkMode ? '#e2e8f0' : '#0f172a';
        }

        // --- Form Controls (Preferences Page) ---
        const inputs = document.querySelectorAll('select, .custom-select-trigger');
        inputs.forEach(input => {
             // Avoid affecting things that shouldn't be styled
             if(input.id === 'colorThemeSelect') return; // handled by custom select mostly, but native fallback
             
             if (darkMode) {
                 input.style.backgroundColor = '#273244';
                 input.style.color = '#e2e8f0';
                 input.style.borderColor = '#334155';
             } else {
                 input.style.backgroundColor = '#ffffff';
                 input.style.color = '#333333';
                 input.style.borderColor = '#e2e8f0';
             }
        });

        // Apply dark mode specific styling to any .settings-category buttons
        const categoryTimeouts = document.querySelectorAll('.settings-category');
        if (categoryTimeouts.length > 0) {
            categoryTimeouts.forEach(btn => {
               // Default (Inactive) State
               if(darkMode) {
                   btn.style.backgroundColor = '#273244'; // Dark Slate
                   btn.style.color = '#e2e8f0'; // Light text
               } else {
                   btn.style.backgroundColor = '#ffffff'; // White
                   btn.style.color = '#0f172a'; // Dark text
               }

               // Active State (if class is present)
               if (btn.classList.contains('active')) {
                   if (darkMode) {
                       btn.style.backgroundColor = '#334155'; // Slightly lighter dark slate
                       btn.style.color = '#fff';
                       btn.style.boxShadow = 'inset 0 0 0 1px rgba(255,255,255,0.1)';
                   } else {
                       btn.style.backgroundColor = '#dbeafe'; // Light Blue
                       btn.style.color = '#1e3a8a'; // Dark Blue text
                   }
               }
            });
        }
    };

    // Initialize
    window.applyGlobalTheme = window.applyArisTheme; // Alias for preferences
    document.addEventListener('DOMContentLoaded', () => {
        window.applyArisTheme();
    });
    
    // Listen for changes from other tabs
    window.addEventListener('storage', (e) => {
        if(e.key === 'arisEduDarkMode' || e.key === 'arisEduColorTheme') {
            window.applyArisTheme();
        }
    });

})();