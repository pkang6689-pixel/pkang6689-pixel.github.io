(function() {
    // Badge System
    window.BadgeSystem = {
        badges: {
            'first_visit': { title: 'First Steps', desc: 'Visited your first lesson!' },
            'night_owl': { title: 'Night Owl', desc: 'Studying after 10 PM' },
            'early_bird': { title: 'Early Bird', desc: 'Studying before 7 AM' },
            'scholar': { title: 'Scholar', desc: 'Visited 5 different lessons' },
            'dedicated': { title: 'Dedicated', desc: 'Visited 20 pages' },
            'completionist': { title: 'Completionist', desc: 'Spent over an hour studying' },
            'quiz_master': { title: 'Quiz Master', desc: 'Completed a quiz' },
            'algebra_master': { title: 'Algebra Wizard', desc: 'Mastered Algebra concepts' },
            'physics_pro': { title: 'Physics Pro', desc: 'Excelled in Physics' },
            'chemistry_whiz': { title: 'Chem Whiz', desc: 'Ace in Chemistry' },
            'polyglot': { title: 'Polyglot', desc: 'Changed language settings' },
            
            // Streak Badges
            'streak_3': { title: 'Streak Starter', desc: 'Visited 3 days in a row' },
            'streak_7': { title: 'Week Warrior', desc: 'Visited 7 days in a row' },
            'streak_30': { title: 'Month Master', desc: 'Visited 30 days in a row' }
        },
        
        award: function(id) {
            try {
                const userBadges = JSON.parse(localStorage.getItem('arisEdu_badges') || '[]');
                if (userBadges.includes(id)) return; // Already awarded

                // Add to storage
                userBadges.push(id);
                localStorage.setItem('arisEdu_badges', JSON.stringify(userBadges));

                // Show Popup
                this.showPopup(this.badges[id]);
            } catch(e) {
                console.error("Error awarding badge:", e);
            }
        },

        showPopup: function(badge) {
            if (!badge) return;
            
            const popup = document.createElement('div');
            popup.style.cssText = `
                position: fixed;
                top: 20px;
                left: 50%;
                transform: translateX(-50%) translateY(-100px);
                background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
                color: #fff;
                padding: 1rem 2rem;
                border-radius: 50px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
                z-index: 10000;
                display: flex;
                align-items: center;
                gap: 1rem;
                transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                font-family: 'Poppins', sans-serif;
                min-width: 300px;
            `;

            popup.innerHTML = `
                <div style="font-size: 2rem;">🏆</div>
                <div>
                    <div style="font-weight: bold; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 1px;">Badge Unlocked!</div>
                    <div style="font-size: 1rem; font-weight: 600;">${badge.title}</div>
                    <div style="font-size: 0.8rem; opacity: 0.9;">${badge.desc}</div>
                </div>
            `;

            document.body.appendChild(popup);

            // Animate In
            requestAnimationFrame(() => {
                popup.style.transform = 'translateX(-50%) translateY(20px)';
            });

            // Animate Out
            setTimeout(() => {
                popup.style.transform = 'translateX(-50%) translateY(-200px)';
                setTimeout(() => popup.remove(), 500);
            }, 4000);
            
            // Play Sound
            const audio = new Audio('https://assets.mixkit.co/active_storage/sfx/2000/2000-preview.mp3'); // Success sound
            audio.volume = 0.5;
            audio.play().catch(e => {}); // Ignore autoplay errors
        },

        checkAll: function() {
            this.checkTimeBased();
            this.checkVisits();
            this.checkTimeSpent();
            this.checkSubjectMastery(); // Handles alg, phys, chem
            this.checkStreaks(); 
        },

        checkTimeBased: function() {
            const hour = new Date().getHours();
            if (hour >= 22) this.award('night_owl');
            if (hour >= 5 && hour < 7) this.award('early_bird');
        },

        checkVisits: function() {
            // Track unique pages visited
            let visits = JSON.parse(localStorage.getItem('arisEdu_visits') || '[]');
            
            // Add current page if not already present
            if (!visits.includes(window.location.pathname)) {
                visits.push(window.location.pathname);
                localStorage.setItem('arisEdu_visits', JSON.stringify(visits));
            }

            if (visits.length >= 1) this.award('first_visit');
            if (visits.length >= 5) this.award('scholar');
            if (visits.length >= 20) this.award('dedicated');
        },

        checkTimeSpent: function() {
            let totalMinutes = 0;
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                if (key && key.startsWith('arisEdu_time_')) {
                    const minutes = parseInt(localStorage.getItem(key)) || 0;
                    totalMinutes += minutes;
                }
            }
            if (totalMinutes >= 60) this.award('completionist');
        },

        checkSubjectMastery: function() {
            const counts = { alg1: 0, alg2: 0, physics: 0, chem: 0, bio: 0 };
            
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                if (!key) continue;
                // pattern: {subject}_u{unit}_l{lesson}_completed = 'true'
                const match = key.match(/^(alg1|alg2|physics|phys|chem|bio)_u\d+_l\d+_completed$/);
                if (match && localStorage.getItem(key) === 'true') {
                    let subj = match[1];
                    if (subj === 'phys') subj = 'physics';
                    if (counts[subj] !== undefined) counts[subj]++;
                }
            }

            if (counts.alg1 >= 5 || counts.alg2 >= 5) this.award('algebra_master');
            if (counts.physics >= 3) this.award('physics_pro'); // Lower threshold for physics
            if (counts.chem >= 3) this.award('chemistry_whiz');
        },

        checkStreaks: function() {
            const streak = parseInt(localStorage.getItem('arisEdu_streak') || '0');
            if (streak >= 3) this.award('streak_3');
            if (streak >= 7) this.award('streak_7');
            if (streak >= 30) this.award('streak_30');
        }
    };

    // Auto-check on load (checks everything!)
    window.addEventListener('load', () => {
        // Delay slightly to ensure page load performance and other scripts ready
        setTimeout(() => {
            if (window.BadgeSystem) {
                window.BadgeSystem.checkAll();
            }
        }, 1000);
    });

})();
