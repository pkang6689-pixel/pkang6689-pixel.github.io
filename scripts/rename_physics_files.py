#!/usr/bin/env python3
"""
Rename physics lesson files to match chemistry naming convention:
  PhysicsLessonX.YTopicName.html         -> Lesson X.Y_Video.html
  PhysicsLessonX.YTopicNameSummary.html  -> Lesson X.Y_Summary.html
  PhysicsLessonX.YTopicName_Practice.html -> Lesson X.Y_Practice.html
  PhysicsLessonX.YTopicName_Quiz.html    -> Lesson X.Y_Quiz.html

Also updates:
  - physics.html references
  - Internal file content (titles, headings)
  - practice_games.js _getLessonBase() and toggleToSummary()
"""

import os
import re
import glob

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder"
PHYSICS_DIR = os.path.join(BASE, "PhysicsLessons")

# Step 1: Build rename mapping
rename_map = {}  # old_full_path -> new_full_path
old_to_new_filename = {}  # old_filename -> new_filename (for updating references)

for unit_dir in sorted(glob.glob(os.path.join(PHYSICS_DIR, "Unit*"))):
    for filepath in sorted(glob.glob(os.path.join(unit_dir, "*.html"))):
        filename = os.path.basename(filepath)
        
        # Parse the filename
        # Patterns: 
        #   PhysicsLesson{num}{topic}_Practice.html
        #   Lesson{num}_Practice.html
        #   PhysicsLesson{num}{topic}_Quiz.html
        #   Lesson{num}_Quiz.html
        #   PhysicsLesson{num}{topic}Summary.html
        #   Lesson{num}_Summary.html
        #   PhysicsLesson{num}{topic}.html
        #   Lesson{num}_Video.html
        
        # Also handle already renamed files to ensure space is present
        
        m_prac = re.match(r'^(?:PhysicsLesson|Lesson)(\d+\.\d+).*?_Practice\.html$', filename)
        if m_prac:
            lesson_num = m_prac.group(1)
            new_name = f"Lesson {lesson_num}_Practice.html"
            rename_map[filepath] = os.path.join(unit_dir, new_name)
            old_to_new_filename[filename] = new_name
            continue
        
        m_quiz = re.match(r'^(?:PhysicsLesson|Lesson)(\d+\.\d+).*?_Quiz\.html$', filename)
        if m_quiz:
            lesson_num = m_quiz.group(1)
            new_name = f"Lesson {lesson_num}_Quiz.html"
            rename_map[filepath] = os.path.join(unit_dir, new_name)
            old_to_new_filename[filename] = new_name
            continue
        
        m_summ = re.match(r'^(?:PhysicsLesson|Lesson)(\d+\.\d+).*?Summary\.html$', filename)
        if m_summ:
            lesson_num = m_summ.group(1)
            new_name = f"Lesson {lesson_num}_Summary.html"
            rename_map[filepath] = os.path.join(unit_dir, new_name)
            old_to_new_filename[filename] = new_name
            continue
        
        m_vid = re.match(r'^(?:PhysicsLesson|Lesson)(\d+\.\d+).*?\.html$', filename)
        if m_vid and not any(x in filename for x in ["Summary", "Practice", "Quiz", "Test"]):
            lesson_num = m_vid.group(1)
            new_name = f"Lesson {lesson_num}_Video.html"
            rename_map[filepath] = os.path.join(unit_dir, new_name)
            old_to_new_filename[filename] = new_name
            continue
        
        print(f"WARNING: Could not parse filename: {filename}")

print(f"Found {len(rename_map)} files to rename")

# Show a sample
for old, new in sorted(rename_map.items())[:12]:
    print(f"  {os.path.basename(old)}  ->  {os.path.basename(new)}")
print("  ...")

# Step 2: Update file content before renaming
print("\n--- Updating file content ---")
for old_path, new_path in sorted(rename_map.items()):
    old_filename = os.path.basename(old_path)
    new_filename = os.path.basename(new_path)
    
    # Determine lesson number and type
    m = re.match(r'^Lesson (\d+\.\d+)_(Video|Summary|Practice|Quiz)\.html$', new_filename)
    if not m:
        print(f"WARNING: Could not parse new filename: {new_filename}")
        continue
    lesson_num = m.group(1)
    file_type = m.group(2)
    
    with open(old_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update <title> tag - remove topic names, use clean format
    # Match existing title patterns like "Lesson 2.1: Distance Displacement Speed Velocity"
    # or "Lesson 2.1: Distance Displacement Speed Velocity Summary"
    if file_type == "Video":
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>Lesson {lesson_num}</title>',
            content
        )
    else:
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>Lesson {lesson_num} {file_type}</title>',
            content
        )
    
    # Update page-title headings
    # Video files have: Lesson X.Y: Topic Name
    # Summary files have: PhysicsLesson X.Y: Topic Summary or Lesson X.Y: Topic Summary
    # Practice files have: Lesson {LESSON_NUM}: {LESSON_TITLE} Practice
    # Quiz files have: Lesson {LESSON_NUM}: Quiz
    
    if file_type == "Video":
        content = re.sub(
            r'(<h2 class="page-title">).*?(</h2>)',
            rf'\1Lesson {lesson_num}\2',
            content
        )
    elif file_type == "Summary":
        content = re.sub(
            r'(<h2 class="page-title">).*?(</h2>)',
            rf'\1Lesson {lesson_num} Summary\2',
            content
        )
    elif file_type == "Practice":
        content = re.sub(
            r'(<h2 class="page-title">).*?(</h2>)',
            rf'\1Lesson {lesson_num} Practice\2',
            content
        )
    elif file_type == "Quiz":
        content = re.sub(
            r'(<h2 class="page-title">).*?(</h2>)',
            rf'\1Lesson {lesson_num} Quiz\2',
            content
        )
    
    if content != original_content:
        with open(old_path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Updated content in {len(rename_map)} files")

# Step 3: Actually rename the files
print("\n--- Renaming files ---")
renamed_count = 0
for old_path, new_path in sorted(rename_map.items()):
    if os.path.exists(new_path):
        print(f"WARNING: Target already exists: {new_path}")
        continue
    os.rename(old_path, new_path)
    renamed_count += 1

print(f"Renamed {renamed_count} files")

# Step 4: Update physics.html references
print("\n--- Updating physics.html ---")
physics_html = os.path.join(BASE, "physics.html")
with open(physics_html, 'r', encoding='utf-8') as f:
    content = f.read()

original = content
for old_filename, new_filename in old_to_new_filename.items():
    # References in physics.html are like: PhysicsLessons/Unit2/PhysicsLesson2.1...html
    # We need to replace the filename part
    content = content.replace(old_filename, new_filename)

if content != original:
    with open(physics_html, 'w', encoding='utf-8') as f:
        f.write(content)
    replacements = sum(1 for old in old_to_new_filename if old in original)
    print(f"Updated {replacements} references in physics.html")
else:
    print("No changes needed in physics.html")

# Step 5: Verify
print("\n--- Verification ---")
remaining_old = []
for unit_dir in sorted(glob.glob(os.path.join(PHYSICS_DIR, "Unit*"))):
    for f in os.listdir(unit_dir):
        if f.startswith("PhysicsLesson"):
            remaining_old.append(f)

if remaining_old:
    print(f"WARNING: {len(remaining_old)} files still have old naming:")
    for f in remaining_old[:10]:
        print(f"  {f}")
else:
    print("All files renamed successfully!")

# Count new files
new_files = []
for unit_dir in sorted(glob.glob(os.path.join(PHYSICS_DIR, "Unit*"))):
    for f in sorted(os.listdir(unit_dir)):
        if f.startswith("Lesson "):
            new_files.append(f)

print(f"New lesson files: {len(new_files)}")
for f in new_files[:12]:
    print(f"  {f}")
print("  ...")

# Check physics.html for any remaining old references
with open(physics_html, 'r', encoding='utf-8') as f:
    content = f.read()
old_refs = re.findall(r'PhysicsLesson\d+\.\d+\w+\.html', content)
if old_refs:
    print(f"\nWARNING: {len(old_refs)} old references remain in physics.html:")
    for ref in old_refs[:5]:
        print(f"  {ref}")
else:
    print("physics.html: All references updated!")
