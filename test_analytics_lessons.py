#!/usr/bin/env python3
"""
Test script: Add analytics to lessons in one course only
"""

import os
import re
from pathlib import Path

COURSE_LESSONS_DIR = Path("C:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\CourseFiles")

def get_lesson_info_from_path(filepath):
    """Extract course ID, unit, and lesson from file path"""
    path_str = str(filepath).replace("\\", "/")
    
    if "Algebra1Lessons" not in path_str:
        return None
    
    match = re.search(r'Unit(\d+)[/\\]Lesson(\d+(?:\.\d+)?)_', path_str)
    if match:
        unit = int(match.group(1))
        lesson = match.group(2)
        return "algebra_1", unit, lesson
    return None

def add_analytics_to_lesson(filepath):
    """Add analytics tracking to a lesson video file"""
    lesson_info = get_lesson_info_from_path(filepath)
    if not lesson_info:
        return False, "Not an Algebra 1 lesson"
    
    course_id, unit, lesson = lesson_info
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Could not read: {str(e)}"
    
    if "analytics-helper.js" in content:
        return True, "Already has"
    
    # Calculate correct path
    script_path = "../../../scripts/analytics-helper.js"
    script_tag = f'<script src="{script_path}"></script>'
    
    # Add to head
    if "</head>" in content:
        content = content.replace("</head>", f"{script_tag}\n</head>")
    else:
        return False, "No head tag"
    
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
        return False, "No body tag"
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, f"Updated U{unit}L{lesson}"
    except Exception as e:
        return False, f"Could not write: {str(e)}"

def main():
    """Test on Algebra 1 lessons only"""
    lesson_files = list(COURSE_LESSONS_DIR.glob("**/Algebra1Lessons/**/Lesson*_Video.html"))
    print(f"Found {len(lesson_files)} Algebra 1 lesson files to process")
    
    successful = 0
    skipped = 0
    failed = 0
    
    for i, filepath in enumerate(sorted(lesson_files), 1):
        success, msg = add_analytics_to_lesson(filepath)
        
        if success:
            if "Already has" in msg:
                skipped += 1
            else:
                successful += 1
                print(f"[{i:3d}] OK algebra_1/{msg}: {filepath.name}")
        else:
            failed += 1
            print(f"[{i:3d}] FAIL {msg}: {filepath.name}")
    
    print(f"\n--- Results for Algebra 1 ---")
    print(f"Updated: {successful}")
    print(f"Already had: {skipped}")
    print(f"Failed: {failed}")
    
    if successful > 0:
        print(f"\nPattern verified! Can apply to all lessons")

if __name__ == "__main__":
    main()
