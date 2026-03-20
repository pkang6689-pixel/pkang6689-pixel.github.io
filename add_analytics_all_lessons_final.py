#!/usr/bin/env python3
"""
Add analytics to ALL lessons - v3 with MS and AP support
"""

import os
import re
import sys
from pathlib import Path

COURSE_LESSONS_DIR = Path("C:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\CourseFiles")

def get_lesson_info_from_path(filepath):
    """Extract course ID, unit, and lesson from file path"""
    path_str = str(filepath).replace("\\", "/")
    
    # Determine course from path patterns
    course_id = None
    
    # MS (Middle School) courses
    if "MS_Algebra1Lessons" in path_str:
        course_id = "ms_algebra_1"
    elif "MS_Algebra2Lessons" in path_str:
        course_id = "ms_algebra_2"
    elif "MS_BiologyLessons" in path_str:
        course_id = "ms_biology"
    elif "MS_ChemistryLessons" in path_str:
        course_id = "ms_chemistry"
    elif "MS_GeometryLessons" in path_str:
        course_id = "ms_geometry"
    elif "MS_PhysicsLessons" in path_str:
        course_id = "ms_physics"
    
    # AP courses (in APLessons folder)
    elif "/APLessons/AP Biology" in path_str or "/APLessons/AP%20Biology" in path_str:
        course_id = "ap_biology"
    elif "/APLessons/AP Calculus AB" in path_str or "/APLessons/AP%20Calculus%20AB" in path_str:
        course_id = "ap_calculus_ab"
    elif "/APLessons/AP Chemistry" in path_str or "/APLessons/AP%20Chemistry" in path_str:
        course_id = "ap_chemistry"
    elif "/APLessons/AP Environmental Science" in path_str or "/APLessons/AP%20Environmental%20Science" in path_str:
        course_id = "ap_environmental_science"
    elif "/APLessons/AP Human Geography" in path_str or "/APLessons/AP%20Human%20Geography" in path_str:
        course_id = "ap_human_geography"
    elif "/APLessons/AP Physics 2" in path_str or "/APLessons/AP%20Physics%202" in path_str or "/APLessons/AP Physics2" in path_str:
        course_id = "ap_physics_2"
    elif "/APLessons/AP Physics C - Mechanics" in path_str or "/APLessons/AP%20Physics%20C%20-%20Mechanics" in path_str or "/APLessons/APPhysicsCMechanics" in path_str:
        course_id = "ap_physics_c_-_mechanics"
    elif "/APLessons/AP Statistics" in path_str or "/APLessons/AP%20Statistics" in path_str:
        course_id = "ap_statistics"
    
    # Regular courses
    elif "Algebra1Lessons" in path_str:
        course_id = "algebra_1"
    elif "Algebra2Lessons" in path_str:
        course_id = "algebra_2"
    elif "BiologyLessons" in path_str:
        course_id = "biology"
    elif "ChemistryLessons" in path_str:
        course_id = "chemistry"
    elif "GeometryLessons" in path_str:
        course_id = "geometry"
    elif "PhysicsLessons" in path_str:
        course_id = "physics"
    elif "PrecalculusLessons" in path_str:
        course_id = "precalculus"
    elif "TrigonometryLessons" in path_str:
        course_id = "trigonometry"
    elif "StatisticsLessons" in path_str:
        course_id = "statistics"
    elif "LinearAlgebraLessons" in path_str:
        course_id = "linear_algebra"
    elif "FinancialMathLessons" in path_str:
        course_id = "financial_math"
    elif "EarthScienceLessons" in path_str:
        course_id = "earth_science"
    elif "EnvironmentalScienceLessons" in path_str:
        course_id = "environmental_science"
    elif "AstronomyLessons" in path_str:
        course_id = "astronomy"
    elif "AnatomyLessons" in path_str:
        course_id = "anatomy"
    elif "MarineScienceLessons" in path_str:
        course_id = "marine_science"
    elif "IntegratedScienceLessons" in path_str:
        course_id = "integrated_science"
    
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
    path_str = str(filepath).replace("\\", "/")
    
    if "/CourseFiles/" not in path_str:
        return None
    
    parts = path_str.split("/CourseFiles/")[1].split("/")
    depth = len(parts) - 1
    
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
        return False, "Read error"
    
    if "analytics-helper.js" in content:
        return True, "Already has"
    
    script_path = get_script_path(filepath)
    if not script_path:
        return False, "Path error"
    
    script_tag = f'<script src="{script_path}"></script>'
    
    if "</head>" in content:
        content = content.replace("</head>", f"{script_tag}\n</head>")
    else:
        return False, "No head"
    
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
        return True, "OK"
    except Exception as e:
        return False, "Write error"

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

if __name__ == "__main__":
    main()
