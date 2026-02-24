#!/usr/bin/env python3
"""
Fix lesson file titles to show the actual lesson name (from physics.html)
instead of just "Lesson X.Y".

For each lesson, updates:
  - <title> tag
  - <h2 class="page-title"> (first one = main heading)
  
In _Video files, also preserves other page-title headings (Rubric, Summary, Practice, Quiz sections).
"""

import os
import re
import glob

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder"
PHYSICS_DIR = os.path.join(BASE, "PhysicsLessons")

# Step 1: Extract lesson titles from physics.html
with open(os.path.join(BASE, "physics.html"), "r", encoding="utf-8") as f:
    physics_content = f.read()

# Pattern: showLessonPopup(event, 'X.Y Title Here')
# The title includes the lesson number prefix like "1.6 Measurement Uncertainty & Error Analysis"
raw_titles = re.findall(r"showLessonPopup\(event,\s*'([^']+)'\)", physics_content)

# Build mapping: lesson_num -> title (without the number prefix)
lesson_titles = {}
for raw in raw_titles:
    if "Unit" in raw and "Test" in raw:
        continue  # Skip unit tests
    m = re.match(r'^(\d+\.\d+)\s+(.+)$', raw)
    if m:
        lesson_num = m.group(1)
        title = m.group(2)
        # Remove star emoji if present
        title = title.lstrip('⭐').strip()
        lesson_titles[lesson_num] = title

print(f"Extracted {len(lesson_titles)} lesson titles from physics.html")
for num in sorted(lesson_titles.keys(), key=lambda x: [int(p) for p in x.split('.')])[:5]:
    print(f"  {num}: {lesson_titles[num]}")
print("  ...")

# Step 2: Update all lesson files
updated = 0
for unit_dir in sorted(glob.glob(os.path.join(PHYSICS_DIR, "Unit*"))):
    for filepath in sorted(glob.glob(os.path.join(unit_dir, "Lesson *.html"))):
        filename = os.path.basename(filepath)
        
        # Skip unit tests
        if "Test" in filename:
            continue
        
        # Parse lesson number and type
        m = re.match(r'^Lesson (\d+\.\d+)_(Video|Summary|Practice|Quiz)\.html$', filename)
        if not m:
            print(f"WARNING: Could not parse: {filename}")
            continue
        
        lesson_num = m.group(1)
        file_type = m.group(2)
        
        if lesson_num not in lesson_titles:
            print(f"WARNING: No title found for lesson {lesson_num}")
            continue
        
        title = lesson_titles[lesson_num]
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Build the display title based on file type
        if file_type == "Video":
            display_title = f"Lesson {lesson_num}: {title}"
            page_heading = f"Lesson {lesson_num}: {title}"
        elif file_type == "Summary":
            display_title = f"Lesson {lesson_num}: {title} - Summary"
            page_heading = f"Lesson {lesson_num}: {title} - Summary"
        elif file_type == "Practice":
            display_title = f"Lesson {lesson_num}: {title} - Practice"
            page_heading = f"Lesson {lesson_num}: {title} - Practice"
        elif file_type == "Quiz":
            display_title = f"Lesson {lesson_num}: {title} - Quiz"
            page_heading = f"Lesson {lesson_num}: {title} - Quiz"
        
        # Update <title> tag
        content = re.sub(r'<title>.*?</title>', f'<title>{display_title}</title>', content)
        
        # Update the FIRST <h2 class="page-title"> only
        # We use re.sub with count=1 to only replace the first occurrence
        content = re.sub(
            r'(<h2 class="page-title">).*?(</h2>)',
            rf'\g<1>{page_heading}\g<2>',
            content,
            count=1
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1

print(f"\nUpdated {updated} files")

# Step 3: Verify a sample
print("\n--- Sample verification ---")
samples = [
    os.path.join(PHYSICS_DIR, "Unit2", "Lesson 2.1_Video.html"),
    os.path.join(PHYSICS_DIR, "Unit2", "Lesson 2.1_Summary.html"),
    os.path.join(PHYSICS_DIR, "Unit2", "Lesson 2.1_Practice.html"),
    os.path.join(PHYSICS_DIR, "Unit2", "Lesson 2.1_Quiz.html"),
    os.path.join(PHYSICS_DIR, "Unit3", "Lesson 3.3_Summary.html"),
]
for sample in samples:
    if os.path.exists(sample):
        with open(sample, 'r') as f:
            for line in f:
                if '<title>' in line:
                    print(f"  {os.path.basename(sample)}: {line.strip()}")
                    break
