#!/usr/bin/env python3
"""
For each lesson, ensure we have all 4 page types:
- Summary (with dash)
- Practice (with dash)
- Quiz (with dash)  
- Video (with dash)

If there's a base entry without page type, it should be renamed to include - Video
"""

import re

def fix_lesson_video_entries(file_path, lang='chinese'):
    """Rename base lesson entries to explicit - Video entries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    changed_count = 0
    
    for i, line in enumerate(lines):
        # Match: "Lesson X.Y: Name": "translation", (without page type)
        # But NOT if it's followed by other page types for that lesson
        match = re.match(r'(\s*)"(Lesson\s+\d+\.\d+:\s+[^"]+?)"\s*:\s*"([^"]*)"\s*,', line)
        
        if match and ' - ' not in match.group(2):  # No dash (no page type)
            indent = match.group(1)
            lesson_key = match.group(2)
            translation = match.group(3)
            
            # Check next line - if it has same lesson with page type, this should be Video
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                # Check if next line has this lesson with a page type (Summary/Practice/Quiz/Video)
                if re.search(rf'"{re.escape(lesson_key)}\s+-\s+(Summary|Practice|Quiz|Video)"', next_line):
                    # Current line is a base entry, rename to - Video
                    new_key = f"{lesson_key} - Video"
                    new_line = f'{indent}"{new_key}": "{translation}",\n'
                    new_lines.append(new_line)
                    changed_count += 1
                    print(f"  Renamed: {lesson_key}")
                    print(f"    TO: {new_key}")
                    continue
        
        new_lines.append(line)
    
    return ''.join(new_lines), changed_count

# Process files
file_specs = [
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js', 'chinese'),
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js', 'spanish'),
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js', 'hindi'),
]

for file_path, lang in file_specs:
    print(f"\nProcessing {lang}: {file_path}")
    try:
        new_content, changed = fix_lesson_video_entries(file_path, lang)
        
        if changed > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Renamed {changed} base entries to - Video")
        else:
            print("✓ No base entries need renaming")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Complete!")
