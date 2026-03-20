#!/usr/bin/env python3
"""
Script to add analytics lesson tracking to all lesson video files
Handles 200+ lesson files across all courses
"""

import os
import re
from pathlib import Path

COURSE_LESSONS_DIR = Path("C:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\CourseFiles")

# Map lesson folder names to course IDs
FOLDER_TO_COURSE_ID = {
    "Algebra1Lessons": "algebra_1",
    "Algebra2Lessons": "algebra_2",
    "BiologyLessons": "biology",
    "ChemistryLessons": "chemistry",
    "GeometryLessons": "geometry",
    "PhysicsLessons": "physics",
    "PrecalculusLessons": "precalculus",
    "TrigonometryLessons": "trigonometry",
    "StatisticsLessons": "statistics",
    "LinearAlgebraLessons": "linear_algebra",
    "FinancialMathLessons": "financial_math",
    "EarthScienceLessons": "earth_science",
    "EnvironmentalScienceLessons": "environmental_science",
    "AstronomyLessons": "astronomy",
    "AnatomyLessons": "anatomy",
    "MarineScienceLessons": "marine_science",
    "IntegratedScienceLessons": "integrated_science",
    # AP Courses
    "APBiology": "ap_biology",
    "APCalculus": "ap_calculus_ab",
    "APChemistry": "ap_chemistry",
    "APEnvironmentalScience": "ap_environmental_science",
    "APHumanGeography": "ap_human_geography",
    "APPhysics2": "ap_physics_2",
    "APPhysicsCMechanics": "ap_physics_c_-_mechanics",
    "APPhys1": "ap_physics_2",
    "APPhysics1": "ap_physics_2",
    "APStatistics": "ap_statistics",
}

def get_lesson_info_from_path(filepath):
    """
    Extract course ID, unit, and lesson from file path
    Example: .../Algebra1Lessons/Unit2/Lesson2.3_Video.html -> (algebra_1, 2, 2.3)
    """
    path_str = str(filepath).replace("\\", "/")
    
    # Find course folder match
    course_id = None
    for folder_name, course in FOLDER_TO_COURSE_ID.items():
        if folder_name in path_str:
            course_id = course
            break
    
    if not course_id:
        return None
    
    # Extract unit and lesson from path
    # Pattern: /Unit(\d+)/Lesson(\d+\.\d+)_
    match = re.search(r'Unit(\d+)[/\\]Lesson(\d+(?:\.\d+)?)_', path_str)
    if match:
        unit = int(match.group(1))
        lesson = match.group(2)
        return course_id, unit, lesson
    
    return None

def add_analytics_to_lesson(filepath):
    """
    Add analytics tracking to a lesson video file
    """
    lesson_info = get_lesson_info_from_path(filepath)
    if not lesson_info:
        return False, "Could not extract lesson info from path"
    
    course_id, unit, lesson = lesson_info
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Could not read file: {str(e)}"
    
    # Check if already has analytics
    if "analytics-helper.js" in content:
        return True, "Already has analytics"
    
    # Count relative path depth to scripts folder
    depth = str(filepath).count("\\") - str(COURSE_LESSONS_DIR).count("\\")
    script_path = "../" * (depth - 1) + "scripts/analytics-helper.js"
    # Normalize the path
    script_path = script_path.replace("\\", "/")
    while "../" * 2 in script_path:
        script_path = script_path.replace("../" * 2, "../" * 1 + "../")
    
    script_tag = f'<script src="{script_path}"></script>'
    
    # Add script tag to head if head exists
    if "</head>" in content:
        content = content.replace("</head>", f"{script_tag}\n</head>")
    else:
        return False, "No </head> tag found"
    
    # Add tracking code before closing body tag
    tracking_code = f"""
<script>
  document.addEventListener('DOMContentLoaded', () => {{
    if (typeof StudentAnalytics !== 'undefined') {{
      try {{
        const analytics = new StudentAnalytics();
        analytics.trackLessonView('{course_id}', {unit}, {lesson}); // Track lesson view
        analytics.updateLearningStreak(); // Update daily streak
      }} catch (e) {{
        console.warn('Analytics tracking failed:', e);
      }}
    }}
  }});
</script>
"""
    
    if "</body>" in content:
        content = content.replace("</body>", tracking_code + "\n</body>")
    else:
        return False, "No </body> tag found"
    
    # Write back
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, f"Updated: {course_id} U{unit} L{lesson}"
    except Exception as e:
        return False, f"Could not write file: {str(e)}"

def main():
    """Main entry point"""
    if not COURSE_LESSONS_DIR.exists():
        print(f"❌ Directory not found: {COURSE_LESSONS_DIR}")
        return
    
    # Find all _Video.html lesson files
    lesson_files = list(COURSE_LESSONS_DIR.glob("**/Lesson*_Video.html"))
    print(f"Found {len(lesson_files)} lesson video files")
    print(f"Starting analytics integration...", flush=True)
    print("-" * 70)
    
    successful = 0
    failed = 0
    skipped = 0
    
    for i, filepath in enumerate(sorted(lesson_files), 1):
        success, msg = add_analytics_to_lesson(filepath)
        
        if success:
            if "Already has" in msg:
                skipped += 1
            else:
                successful += 1
        else:
            failed += 1
        
        # Print progress every 100 files or on first/last file
        if i % 100 == 0 or i == 1 or i == len(lesson_files):
            print(f"Progress: [{i}/{len(lesson_files)}] ✅{successful} ⏭️{skipped} ❌{failed}", flush=True)
        
        # Print failures as they occur
        if not success and failed <= 10:
            print(f"  ❌ {filepath.name}: {msg}", flush=True)
    
    print("-" * 70)
    print(f"Results:")
    print(f"  ✅ Updated: {successful}")
    print(f"  ⏭️ Already had analytics: {skipped}")
    print(f"  ❌ Failed: {failed}")
    print(f"  Total processed: {successful + skipped + failed} / {len(lesson_files)}")
    
    if successful > 0:
        print(f"\n🎉 Successfully added analytics to {successful} lesson files!")
    
    return successful, skipped, failed

if __name__ == "__main__":
    main()
