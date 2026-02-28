/**
 * Migration Script: Mirror HS Completed Lessons to MS
 * 
 * This script updates all existing localStorage data so that whenever an HS lesson was
 * marked as completed, the corresponding MS lesson is also marked as completed.
 * 
 * One-way sync: HS→MS only (MS students completing lessons does NOT affect HS)
 * 
 * HOW TO USE:
 * 1. Open the browser console (F12 or Ctrl+Shift+I)
 * 2. Copy and paste the entire content of this file into the console
 * 3. The script will run automatically and update all localStorage data
 * 4. You'll see detailed output about what was migrated
 * 
 * SAFETY: This script only reads localStorage, never deletes it
 */

(function() {
    console.log('🔄 Starting HS to MS Completion Migration...');
    
    // Define course prefixes and their mappings
    const courses = [
        { hs: 'alg1', ms: 'ms_alg1', folder: 'Algebra1Lessons' },
        { hs: 'alg2', ms: 'ms_alg2', folder: 'Algebra2Lessons' },
        { hs: 'geometry', ms: 'ms_geom', folder: 'GeometryLessons' },
        { hs: 'physics', ms: 'ms_phys', folder: 'PhysicsLessons' },
        { hs: 'chem', ms: 'ms_chem', folder: 'ChemistryLessons' },
        { hs: 'bio', ms: 'ms_bio', folder: 'BiologyLessons' }
    ];

    let totalMigrated = 0;
    const migrationReport = {};

    // Process each course
    courses.forEach(course => {
        migrationReport[course.hs] = {
            title: `${course.hs.toUpperCase()}`,
            mapped: 0,
            failed: 0,
            details: []
        };

        // Load the MS mapping for this course (created when MS pages were visited)
        let msMap = {};
        try {
            msMap = JSON.parse(localStorage.getItem('_msMap_' + course.folder) || '{}');
        } catch (e) {
            console.warn(`⚠️  Could not load _msMap_${course.folder}:`, e);
            migrationReport[course.hs].failed++;
            return;
        }

        if (Object.keys(msMap).length === 0) {
            console.log(`📝 No mapping found for ${course.folder}. This is OK if MS has not been visited yet.`);
            return;
        }

        // Find all HS completed lessons
        const completedPattern = new RegExp(`^${course.hs}_u(.+?)_l(.+?)_completed$`);
        
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            const match = key.match(completedPattern);
            
            if (match && localStorage.getItem(key) === 'true') {
                const unit = match[1];
                const lesson = match[2];
                const hsKey = `${unit}_${lesson}`;
                const msEntry = msMap[hsKey];

                if (msEntry) {
                    // Parse MS unit and lesson (handle units like "5A" with underscores)
                    const parts = msEntry.split('_');
                    const msUnit = parts[0];
                    const msLesson = parts.slice(1).join('_');
                    const msKey = `${course.ms}_u${msUnit}_l${msLesson}_completed`;

                    try {
                        localStorage.setItem(msKey, 'true');
                        totalMigrated++;
                        migrationReport[course.hs].mapped++;
                        migrationReport[course.hs].details.push(
                            `  ✓ ${key} → ${msKey}`
                        );
                        console.log(`✅ Migrated: ${key} → ${msKey}`);
                    } catch (e) {
                        migrationReport[course.hs].failed++;
                        console.error(`❌ Failed to set ${msKey}:`, e);
                    }
                } else {
                    console.log(`⚠️  No mapping found for ${hsKey} in ${course.folder}`);
                    migrationReport[course.hs].failed++;
                }
            }
        }
    });

    // Print migration report
    console.log('\n' + '='.repeat(70));
    console.log('📊 MIGRATION REPORT');
    console.log('='.repeat(70));

    Object.entries(migrationReport).forEach(([course, report]) => {
        if (report.mapped > 0 || report.failed > 0) {
            console.log(`\n${report.title}:`);
            console.log(`  ✓ Mapped: ${report.mapped}`);
            console.log(`  ❌ Failed: ${report.failed}`);
            if (report.details.length > 0 && report.details.length <= 10) {
                console.log('  Details:');
                report.details.forEach(detail => console.log(detail));
            }
        }
    });

    console.log('\n' + '='.repeat(70));
    console.log(`🎉 Migration Complete! Total lessons mirrored: ${totalMigrated}`);
    console.log('='.repeat(70));
    console.log('\n💡 Tips:');
    console.log('  • HS completion will now automatically mirror to MS');
    console.log('  • MS completion will NOT affect HS (one-way sync)');
    console.log('  • All updated data is in localStorage');
    console.log('\n✨ Run this again in the future if you add new HS→MS mappings');
})();
