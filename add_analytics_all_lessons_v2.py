#!/usr/bin/env python3
"""
Add analytics tracking to ALL lesson video files
2000+ lessons across all courses
"""

import os
import re
import sys
from pathlib import Path

COURSE_LESSONS_DIR = Path("C:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\CourseFiles")

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
    """Extract course ID, unit, and lesson from file path"""
    path_str = str(filepath).replace("\\", "/")
    
    # Find course from folder names
    course_id = None
    for folder_name, course in FOLDER_TO_COURSE_ID.items():
        if folder_name in path_str:
            course_id = course
            break
    
    if not course_id:
        return None
    
    # Extract unit and lesson
    match = re.search(r'Unit(\d+)[/\\]Lesson(\d+(?:\.\d+)?)_', path_str)
    if match:
        unit = int(match.group(1))
        lesson = match.group(2)
        return course_id, unit, lesson
    
    return None

def get_script_path(filepath):
    """Calculate relative path to analytics-helper.js"""
    # All lesson files are at: CourseFiles/{CourseLessons}/Unit{X}/Lesson{X.X}_*.html
    # We need to go: up 3 levels to CourseFiles, then up 1 more to ArisEdu Project Folder, then scripts
    # Actually: up 2 levels ../../ gets us to CourseFiles, then ../scripts
    # But we might go: ../../scripts or ../../../scripts depending on nesting
    
    # Check depth: count how many slashes after "CourseFiles"
    path_str = str(filepath).replace("\\", "/")
    if "/CourseFiles/" not in path_str:
        return None
    
    parts = path_str.split("/CourseFiles/")[1].split("/")
    #Count folder depth under CourseFiles
    depth = len(parts) - 1  # -1 for the filename
    
    # Each level up = ../
    # We need to reach CourseFiles/.. which is scripts location
    return "/".join([".."] * (depth + 1)) + "/scripts/analytics-helper.js"

def add_analytics_to_lesson(filepath):
    """Add analytics to a lesson file"""
    lesson_info = get_lesson_info_from_path(filepath)
    if not lesson_info:
        return False, "Unknown course"
    
    course_id, unit, lesson = lesson_info
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Read error"
    
    if "analytics-helper.js" in content:
        return True, "Already has"
    
    # Get correct script path
    script_path = get_script_path(filepath)
    if not script_path:
        return False, "Path error"
    
    script_tag = f'<script src="{script_path}"></script>'
    
    # Add to head
    if "</head>" in content:
        content = content.replace("</head>", f"{script_tag}\n</head>")
    else:
        return False, "No head"
    
    # Add tracking code
    tracking_code = f"""
<script>
  document.addEventListener('DOMContentLoaded', () => {{
    if (typeof StudentAnalytics !== 'undefined') {{
      try {{
        const analytics = new StudentAnalytics();
        analytics.trackLessonView('{course_id}', {unit}, {lesson});
        analytics.updateLearningStreak();
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
        return False, "No body"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, f"OK"
    except Exception as e:
        return False, f"Write error"

def main():
    """Main: process all lessons"""
    lesson_files = list(COURSE_LESSONS_DIR.glob("**/Lesson*_Video.html"))
    print(f"Found {len(lesson_files)} lesson video files")
    sys.stdout.flush()
    
    successful = 0
    skipped = 0
    failed = 0
    errors = {}
    
    for i, filepath in enumerate(sorted(lesson_files), 1):
        success, msg = add_analytics_to_lesson(filepath)
        
        if success:
            if "Already has" in msg:
                skipped += 1
            else:
                successful += 1
        else:
            failed += 1
            if msg not in errors:
                errors[msg] = []
            errors[msg].append(filepath.name)
        
        # Print progress
        if i % 200 == 0 or i == len(lesson_files):
            pct = int((i / len(lesson_files)) * 100)
            print(f"[{pct:3d}%] {i:4d}/{len(lesson_files)} - Updated: {successful:4d}, Skipped: {skipped:4d}, Failed: {failed:3d}")
            sys.stdout.flush()
    
    print("\n" + "="*70)
    print(f"FINAL RESULTS:")
    print(f"  Updated:  {successful:5d} files")
    print(f"  Skipped:  {skipped:5d} files (already had analytics)")
    print(f"  Failed:   {failed:5d} files")
    print(f"  Total:    {successful + skipped + failed:5d} files")
    print("="*70)
    
    if errors:
        print("\nError summary:")
        for error_type, files in sorted(errors.items(), key=lambda x: -len(x[1]))[:5]:
            print(f"  {error_type}: {len(files)} files")
    
    return successful, skipped, failed

if __name__ == "__main__":
    main()
