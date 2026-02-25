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
            const userBadges = JSON.parse(localStorage.getItem('arisEdu_badges') || '[]');
            if (userBadges.includes(id)) return; // Already owed

            // Add to storage
            userBadges.push(id);
            localStorage.setItem('arisEdu_badges', JSON.stringify(userBadges));

            // Show Popup
            this.showPopup(this.badges[id]);
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
            audio.play().catch(e => console.log('Audio autoplay blocked', e));
        },

        checkTimeBased: function() {
            const hour = new Date().getHours();
            if (hour >= 22) this.award('night_owl');
            if (hour >= 5 && hour < 7) this.award('early_bird');
        },

        checkVisits: function() {
            // Track unique pages visited
            let visits = JSON.parse(localStorage.getItem('arisEdu_visits') || '[]');
            visits.push(window.location.pathname);
            visits = [...new Set(visits)];
            localStorage.setItem('arisEdu_visits', JSON.stringify(visits));

            if (visits.length >= 1) this.award('first_visit');
            if (visits.length >= 5) this.award('scholar');
        }
    };

    // Auto-check on load
    window.addEventListener('load', () => {
        window.BadgeSystem.checkTimeBased();
        window.BadgeSystem.checkVisits();
    });

})();
