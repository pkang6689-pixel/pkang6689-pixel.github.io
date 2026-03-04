(function() {
    const TIERS = [
        { id: 'bronze', name: 'Bronze', icon: '' },
        { id: 'silver', name: 'Silver', icon: '' },
        { id: 'gold', name: 'Gold', icon: '' },
        { id: 'diamond', name: 'Diamond', icon: '' },
        { id: 'amethyst', name: 'Amethyst', icon: '' }
    ];

    const BADGE_DEFS = {
        'night_owl': { title: 'Night Owl', desc: t => "Studied after 10 PM on " + t + " days", icon: '', thresholds: [1, 5, 15, 30, 50] },
        'early_bird': { title: 'Early Bird', desc: t => "Studied before 7 AM on " + t + " days", icon: '', thresholds: [1, 5, 15, 30, 50] },
        'quiz_master': { title: 'Quiz Master', desc: t => "Completed " + t + " quizzes", icon: '', thresholds: [1, 5, 15, 30, 50] },
        
        // High School (Legacy + New)
        'algebra': { title: 'Algebra Wizard', desc: t => "Completed " + t + "% of Algebra (HS)", icon: '', thresholds: [10, 30, 50, 80, 100], max: 186 }, // A1(119)+A2(67)
        'hs_alg1': { title: 'Algebra 1 Mastery', desc: t => "Completed " + t + "% of Algebra 1", icon: '', thresholds: [10, 30, 50, 80, 100], max: 119 },
        'hs_alg2': { title: 'Algebra 2 Mastery', desc: t => "Completed " + t + "% of Algebra 2", icon: '', thresholds: [10, 30, 50, 80, 100], max: 67 },
        'geometry': { title: 'Geometry Expert', desc: t => "Completed " + t + "% of Geometry (HS)", icon: '', thresholds: [10, 30, 50, 80, 100], max: 111 },
        'physics': { title: 'Physics Pro', desc: t => "Completed " + t + "% of Physics (HS)", icon: '', thresholds: [10, 30, 50, 80, 100], max: 84 },
        'chemistry': { title: 'Chem Whiz', desc: t => "Completed " + t + "% of Chemistry (HS)", icon: '', thresholds: [10, 30, 50, 80, 100], max: 109 },
        'biology': { title: 'Biology Guru', desc: t => "Completed " + t + "% of Biology (HS)", icon: '', thresholds: [10, 30, 50, 80, 100], max: 83 },

        // Middle School
        'ms_pre_alg': { title: 'Pre-Algebra Pro', desc: t => "Completed " + t + "% of MS Pre-Algebra", icon: '', thresholds: [10, 30, 50, 80, 100], max: 59 },
        'ms_alg_found': { title: 'Algebra Foundations', desc: t => "Completed " + t + "% of MS Alg Foundations", icon: '', thresholds: [10, 30, 50, 80, 100], max: 20 },
        'ms_geom': { title: 'MS Geometry Star', desc: t => "Completed " + t + "% of MS Geometry", icon: '', thresholds: [10, 30, 50, 80, 100], max: 60 },
        'ms_phys': { title: 'MS Physics Explorer', desc: t => "Completed " + t + "% of MS Physics", icon: '', thresholds: [10, 30, 50, 80, 100], max: 52 },
        'ms_chem': { title: 'MS Chemistry Spark', desc: t => "Completed " + t + "% of MS Chemistry", icon: '', thresholds: [10, 30, 50, 80, 100], max: 54 }, // Shared keys with HS Chem
        'ms_life_sci': { title: 'Life Science Badge', desc: t => "Completed " + t + "% of MS Life Science", icon: '', thresholds: [10, 30, 50, 80, 100], max: 34 }, // Shared keys with HS Bio

        // AP Courses
        'ap_bio': { title: 'AP Bio Scholar', desc: t => "Completed " + t + "% of AP Biology", icon: '', thresholds: [10, 30, 50, 80, 100], max: 40 },
        'ap_chem': { title: 'AP Chem Scholar', desc: t => "Completed " + t + "% of AP Chemistry", icon: '', thresholds: [10, 30, 50, 80, 100], max: 41 },
        'ap_env_sci': { title: 'AP Enviro Scholar', desc: t => "Completed " + t + "% of AP Env Science", icon: '', thresholds: [10, 30, 50, 80, 100], max: 45 },
        'ap_hug': { title: 'AP HUG Scholar', desc: t => "Completed " + t + "% of AP Human Geo", icon: '', thresholds: [10, 30, 50, 80, 100], max: 41 },
        'ap_calc_ab': { title: 'AP Calc AB Scholar', desc: t => "Completed " + t + "% of AP Calculus AB", icon: '', thresholds: [10, 30, 50, 80, 100], max: 76 },
        'ap_stats': { title: 'AP Stats Scholar', desc: t => "Completed " + t + "% of AP Statistics", icon: '', thresholds: [10, 30, 50, 80, 100], max: 56 },
        'ap_phys1': { title: 'AP Phys 1 Scholar', desc: t => "Completed " + t + "% of AP Physics 1", icon: '', thresholds: [10, 30, 50, 80, 100], max: 64 },
        'ap_phys2': { title: 'AP Phys 2 Scholar', desc: t => "Completed " + t + "% of AP Physics 2", icon: '', thresholds: [10, 30, 50, 80, 100], max: 35 },
        'ap_phys_mech': { title: 'AP Mechanics Scholar', desc: t => "Completed " + t + "% of AP Physics C", icon: '', thresholds: [10, 30, 50, 80, 100], max: 28 },

        // Aggregates
        'master_hs': { title: 'High School Master', desc: t => "Completed " + t + "% of High School Content", icon: '', thresholds: [10, 30, 50, 80, 100], max: 573 },
        'master_ms': { title: 'Middle School Master', desc: t => "Completed " + t + "% of Middle School Content", icon: '', thresholds: [10, 30, 50, 80, 100], max: 279 },
        'master_ap': { title: 'AP Scholar Distinction', desc: t => "Completed " + t + "% of AP Content", icon: '', thresholds: [10, 30, 50, 80, 100], max: 426 },

        'streak': { title: 'Streak Master', desc: t => "Reached a " + t + "-day streak", icon: '', thresholds: [3, 7, 14, 30, 60] },
        'game_2048': { title: '2048 Master', desc: t => "Reached the " + t + " tile!", icon: '', thresholds: [128, 256, 512, 1024, 2048], max: 2048 }
    };

    const generatedBadges = {
        'polyglot': { title: 'Polyglot', desc: 'Changed language settings', icon: '' }
    };

    for (const [id, def] of Object.entries(BADGE_DEFS)) {
        def.thresholds.forEach((thresh, i) => {
            const tier = TIERS[i];
            generatedBadges[id + '_' + tier.id] = {
                title: def.title + ' (' + tier.name + ')',
                desc: eval(def.desc)(thresh),
                icon: def.icon + tier.icon
            };
        });
    }

    // Badge System
    window.BadgeSystem = {
        badges: generatedBadges,
        
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
                <div style="font-size: 2rem;">${badge.icon || '🏆'}</div>
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
        },

        evaluateTieredBadge: function(baseId, currentValue) {
            const def = BADGE_DEFS[baseId];
            if (!def) return;
            
            for (let i = 0; i < def.thresholds.length; i++) {
                if (currentValue >= def.thresholds[i]) {
                    this.award(baseId + '_' + TIERS[i].id);
                }
            }
        },

        updateStat: function(statKey, dateStr) {
            const dates = JSON.parse(localStorage.getItem('arisEdu_stats_' + statKey) || '[]');
            if (!dates.includes(dateStr)) {
                dates.push(dateStr);
                localStorage.setItem('arisEdu_stats_' + statKey, JSON.stringify(dates));
            }
            return dates.length;
        },

        getStatArrayLength: function(statKey) {
            return JSON.parse(localStorage.getItem('arisEdu_stats_' + statKey) || '[]').length;
        },

        checkAll: function() {
            this.checkTimeBased();
            this.checkTimeSpent();
            this.checkSubjectMastery();
            this.checkStreaks();
            this.checkGames();
        },

        checkGames: function() {
            // 2048 Logic
            let maxTile = parseInt(localStorage.getItem('2048_max_tile') || '0');
            
            // Migration: if user has legacy badge, assume they reached 2048
            const badges = JSON.parse(localStorage.getItem('arisEdu_badges') || '[]');
            if (maxTile < 2048 && badges.includes('2048_tile')) {
                 maxTile = 2048;
                 localStorage.setItem('2048_max_tile', '2048');
            }
            
            this.evaluateTieredBadge('game_2048', maxTile);
        },

        checkTimeBased: function() {
            const todayStr = new Date().toISOString().split('T')[0];
            const hour = new Date().getHours();
            
            if (hour >= 22) {
                this.updateStat('night_owl_days', todayStr);
            }
            if (hour >= 5 && hour < 7) {
                this.updateStat('early_bird_days', todayStr);
            }
            
            this.evaluateTieredBadge('night_owl', this.getStatArrayLength('night_owl_days'));
            this.evaluateTieredBadge('early_bird', this.getStatArrayLength('early_bird_days'));
        },

        checkTimeSpent: function() {
            // Evaluated elsewhere or deprecated for tiers
        },

        checkSubjectMastery: function() {
            const counts = {};
            
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                if (!key) continue;
                // pattern extension: {subject}_u{unit}_l{lesson}_completed = 'true'
                const match = key.match(/^(.+)_u\d+_l\d+_completed$/);
                if (match && localStorage.getItem(key) === 'true') {
                    const subj = match[1];
                    counts[subj] = (counts[subj] || 0) + 1;
                }
            }

            // Normalizer for legacy keys
            if (counts['phys']) counts['physics'] = (counts['physics'] || 0) + counts['phys'];

            const calcPct = (count, max) => Math.min(100, Math.floor(((count || 0) / max) * 100));

            // High School
            this.evaluateTieredBadge('hs_alg1', calcPct(counts['alg1'], 119));
            this.evaluateTieredBadge('hs_alg2', calcPct(counts['alg2'], 67));
            this.evaluateTieredBadge('geometry', calcPct(counts['geometry'], 111));
            this.evaluateTieredBadge('physics', calcPct(counts['physics'], 84));
            this.evaluateTieredBadge('chemistry', calcPct(counts['chem'], 109));
            this.evaluateTieredBadge('biology', calcPct(counts['bio'], 83));

            // Legacy Algebra Aggregate
            const algTotal = (counts['alg1'] || 0) + (counts['alg2'] || 0);
            this.evaluateTieredBadge('algebra', calcPct(algTotal, 186));

            // Middle School
            // Note: Some keys shared with HS (alg1, alg2, chem, bio) due to file configuration
            this.evaluateTieredBadge('ms_pre_alg', calcPct(counts['alg1'], 59));
            this.evaluateTieredBadge('ms_alg_found', calcPct(counts['alg2'], 20));
            this.evaluateTieredBadge('ms_geom', calcPct(counts['ms_geom'], 60));
            this.evaluateTieredBadge('ms_phys', calcPct(counts['ms_phys'], 52));
            this.evaluateTieredBadge('ms_chem', calcPct(counts['chem'], 54));
            this.evaluateTieredBadge('ms_life_sci', calcPct(counts['bio'], 34));

            // AP Courses
            this.evaluateTieredBadge('ap_bio', calcPct(counts['ap_bio'], 40));
            this.evaluateTieredBadge('ap_chem', calcPct(counts['ap_chem'], 41));
            this.evaluateTieredBadge('ap_env_sci', calcPct(counts['ap_env_sci'], 45));
            this.evaluateTieredBadge('ap_hug', calcPct(counts['ap_hug'], 41));
            this.evaluateTieredBadge('ap_calc_ab', calcPct(counts['ap_calc_ab'], 76));
            this.evaluateTieredBadge('ap_stats', calcPct(counts['ap_stats'], 56));
            this.evaluateTieredBadge('ap_phys1', calcPct(counts['apphys1'], 64));
            this.evaluateTieredBadge('ap_phys2', calcPct(counts['ap_phys2'], 35));
            this.evaluateTieredBadge('ap_phys_mech', calcPct(counts['ap_phys_mech'], 28));

            // Master Aggregates
            const safeC = (k) => counts[k] || 0;
            const totalHS = safeC('alg1') + safeC('alg2') + safeC('geometry') + safeC('physics') + safeC('chem') + safeC('bio');
            this.evaluateTieredBadge('master_hs', calcPct(totalHS, 573));

            const totalMS = safeC('alg1') + safeC('alg2') + safeC('ms_geom') + safeC('ms_phys') + safeC('chem') + safeC('bio');
            this.evaluateTieredBadge('master_ms', calcPct(totalMS, 279)); 

            const totalAP = safeC('ap_bio') + safeC('ap_chem') + safeC('ap_env_sci') + safeC('ap_hug') + safeC('ap_calc_ab') + safeC('ap_stats') + safeC('apphys1') + safeC('ap_phys2') + safeC('ap_phys_mech');
            this.evaluateTieredBadge('master_ap', calcPct(totalAP, 426));
        },

        checkStreaks: function() {
            const streak = parseInt(localStorage.getItem('arisEdu_streak') || '0');
            this.evaluateTieredBadge('streak', streak);
        }
    };

    // Auto-check on load (checks everything!)
    window.addEventListener('load', () => {
        setTimeout(() => {
            if (window.BadgeSystem) {
                window.BadgeSystem.checkAll();
            }
        }, 1000);
    });

})();
