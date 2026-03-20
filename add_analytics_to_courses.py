#!/usr/bin/env python3
"""
Script to add analytics integration to all course homepage files
"""

import os
import json
from pathlib import Path

# Course ID mapping
COURSE_MAPPING = {
    "anatomy.html": "anatomy",
    "astronomy.html": "astronomy",
    "earth_science.html": "earth_science",
    "environmental_science.html": "environmental_science",
    "financial_math.html": "financial_math",
    "integrated_science.html": "integrated_science",
    "linear_algebra.html": "linear_algebra",
    "marine_science.html": "marine_science",
    "precalculus.html": "precalculus",
    "statistics.html": "statistics",
    "trigonometry.html": "trigonometry",
    "ap_biology.html": "ap_biology",
    "ap_calculus.html": "ap_calculus_ab",
    "ap_chemistry.html": "ap_chemistry",
    "ap_environmental_science.html": "ap_environmental_science",
    "ap_hug.html": "ap_human_geography",
    "ap_physics1.html": "ap_physics_2",
    "ap_physics2.html": "ap_physics_2",
    "ap_physics_mechanics.html": "ap_physics_c_-_mechanics",
    "ap_statistics.html": "ap_statistics",
    "ms_algebra1.html": "ms_algebra_1",
    "ms_algebra2.html": "ms_algebra_2",
    "ms_bio.html": "ms_biology",
    "ms_chem.html": "ms_chemistry",
    "ms_geometry.html": "ms_geometry",
    "ms_physics.html": "ms_physics",
}

# Already completed courses
COMPLETED = {"algebra1.html", "algebra2.html", "geometry.html", "bio.html", "chem.html", "physics.html"}

COURSE_HOMEPAGE_DIR = Path("C:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\CourseHomepage")

def get_analytics_script_tag():
    """Return the analytics helper script tag"""
    return '<script src="../scripts/analytics-helper.js"></script>'

def add_analytics_to_domevent(courseId, domevent_code):
    """
    Add analytics initialization to DOMContentLoaded event
    """
    analytics_template = f"""
    // Initialize analytics and track course visit
    if (typeof StudentAnalytics !== 'undefined') {{
      try {{
        const analytics = new StudentAnalytics();
        analytics.trackLessonView('{courseId}', 0, 0); // Track course visit
        analytics.updateLearningStreak(); // Update daily streak
      }} catch (e) {{
        console.warn('Analytics initialization failed:', e);
      }}
    }}"""
    
    # Insert analytics code at the beginning of DOMContentLoaded body
    # Find the opening brace and insert after it
    if "function()" in domevent_code:
        # Handle both: function() { and function() { on new lines
        insert_pos = domevent_code.find("{") + 1
        new_code = domevent_code[:insert_pos] + analytics_template + domevent_code[insert_pos:]
        return new_code
    return domevent_code

def process_file(filepath):
    """
    Add analytics to a course homepage file
    """
    filename = filepath.name
    course_id = COURSE_MAPPING.get(filename)
    
    if not course_id:
        print(f"❌ {filename}: No mapping found")
        return False
    
    if filename in COMPLETED:
        print(f"✅ {filename}: Already completed (skipped)")
        return True
    
    print(f"📝 Processing {filename} (courseId: {course_id})...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has analytics
        if "analytics-helper.js" in content:
            print(f"  ✓ Already has analytics-helper.js")
            return True
        
        # Add script tag after theme_manager.js in head
        script_tag = get_analytics_script_tag()
        if '<script src="../theme_manager.js"></script>' in content:
            content = content.replace(
                '<script src="../theme_manager.js"></script>',
                '<script src="../theme_manager.js"></script>\n' + script_tag
            )
            print(f"  ✓ Added analytics script tag")
        else:
            print(f"  ⚠ Could not find theme_manager.js script tag")
            return False
        
        # Add analytics code to DOMContentLoaded
        if "document.addEventListener('DOMContentLoaded'" in content:
            analytics_code = f"""
    // Initialize analytics and track course visit
    if (typeof StudentAnalytics !== 'undefined') {{
      try {{
        const analytics = new StudentAnalytics();
        analytics.trackLessonView('{course_id}', 0, 0); // Track course visit
        analytics.updateLearningStreak(); // Update daily streak
      }} catch (e) {{
        console.warn('Analytics initialization failed:', e);
      }}
    }}
"""
            
            # Try function() pattern first
            old_pattern = "document.addEventListener('DOMContentLoaded', function() {"
            if old_pattern in content:
                new_pattern = old_pattern + analytics_code
                content = content.replace(old_pattern, new_pattern)
                print(f"  ✓ Added analytics initialization (function syntax)")
            else:
                # Try arrow function pattern
                old_pattern_arrow = "document.addEventListener('DOMContentLoaded', () => {"
                if old_pattern_arrow in content:
                    new_pattern_arrow = old_pattern_arrow + analytics_code
                    content = content.replace(old_pattern_arrow, new_pattern_arrow)
                    print(f"  ✓ Added analytics initialization (arrow syntax)")
                else:
                    print(f"  ⚠ Could not find DOMContentLoaded pattern (function or arrow)")
                    return False
        else:
            print(f"  ⚠ No DOMContentLoaded found")
            return False
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ Successfully updated!")
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False

def main():
    """Main entry point"""
    if not COURSE_HOMEPAGE_DIR.exists():
        print(f"❌ Directory not found: {COURSE_HOMEPAGE_DIR}")
        return
    
    print(f"Starting analytics integration for {len(COURSE_MAPPING)} courses...")
    print(f"Already completed: {len(COMPLETED)}")
    print(f"Remaining to process: {len(COURSE_MAPPING) - len(COMPLETED)}")
    print("-" * 70)
    
    successful = 0
    failed = 0
    skipped = 0
    
    for filename in sorted(COURSE_MAPPING.keys()):
        filepath = COURSE_HOMEPAGE_DIR / filename
        
        if not filepath.exists():
            print(f"❌ {filename}: File not found at {filepath}")
            failed += 1
            continue
        
        if filename in COMPLETED:
            skipped += 1
            continue
        
        if process_file(filepath):
            successful += 1
        else:
            failed += 1
        
        print()
    
    print("-" * 70)
    print(f"Results: ✅ {successful} successful, ❌ {failed} failed, ⏭️ {skipped} skipped")
    print(f"Total processed: {successful + failed + skipped} / {len(COURSE_MAPPING)}")

if __name__ == "__main__":
    main()
