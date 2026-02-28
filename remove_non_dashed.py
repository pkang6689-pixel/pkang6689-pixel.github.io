#!/usr/bin/env python3
"""
Remove non-dashed lesson entries like "Lesson X.Y: Name Summary"
Keep only the dashed versions like "Lesson X.Y: Name - Summary"
"""

import re

def remove_non_dashed_lessons(file_path):
    """Remove non-dashed lesson page-type entries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    removed_count = 0
    
    for line in lines:
        # Match lines like: "Lesson X.Y: Name Summary": "translation",
        # where Summary/Practice/Quiz/Video is NOT preceded by a dash
        match = re.match(r'(\s*)"(Lesson\s+\d+\.\d+:\s+[^"]+?)\s+(Summary|Practice|Quiz|Video)"\s*:\s*"([^"]*)"\s*,', line)
        
        if match:
            indent = match.group(1)
            lesson_key = match.group(2)
            page_type = match.group(3)
            
            # Check if this is truly a non-dashed entry (no " - " in the key)
            if ' - ' not in lesson_key:
                removed_count += 1
                print(f"  Removing: {lesson_key} {page_type}")
                continue  # Skip this line
        
        new_lines.append(line)
    
    return ''.join(new_lines), removed_count

# Process files
file_specs = [
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js', 'chinese'),
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js', 'spanish'),
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js', 'hindi'),
]

for file_path, lang in file_specs:
    print(f"\nProcessing {lang}: {file_path}")
    try:
        new_content, removed = remove_non_dashed_lessons(file_path)
        
        if removed > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Removed {removed} non-dashed lesson entries")
        else:
            print("✓ No non-dashed entries found")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Complete!")
