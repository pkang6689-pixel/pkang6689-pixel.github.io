#!/usr/bin/env python3
"""
Diagnose which lesson patterns are failing
"""

import os
import re
from pathlib import Path

COURSE_LESSONS_DIR = Path("C:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\CourseFiles")

# Get ALL .html files under CourseFiles (not just _Video)
all_files = list(COURSE_LESSONS_DIR.glob("**/*.html"))
video_files = list(COURSE_LESSONS_DIR.glob("**/Lesson*_Video.html"))

print(f"Total HTML files in CourseFiles: {len(all_files)}")
print(f"Video lesson files (_Video.html): {len(video_files)}")
print(f"\nAnalyzing file patterns...")

# Categorize files
patterns = {}
for f in all_files:
    if "_Video.html" in f.name:
        cat = "_Video"
    elif "_Quiz.html" in f.name:
        cat = "_Quiz"
    elif "_Practice.html" in f.name:
        cat = "_Practice"
    elif "_Summary.html" in f.name:
        cat = "_Summary"
    elif "_Test.html" in f.name:
        cat = "_Test"
    else:
        cat = "Other"
    
    if cat not in patterns:
        patterns[cat] = 0
    patterns[cat] += 1

print("\nFile breakdown:")
for pattern, count in sorted(patterns.items(), key=lambda x: -x[1]):
    print(f"  {pattern:15s}: {count:5d} files")

# Check for non-Lesson files
print("\nNon-Lesson files sample:")
non_lesson_files = [f for f in all_files if not f.name.startswith("Lesson")]
print(f"Total non-Lesson files: {len(non_lesson_files)}")
if non_lesson_files:
    for f in non_lesson_files[:10]:
        print(f"  - {f.relative_to(COURSE_LESSONS_DIR)}")
