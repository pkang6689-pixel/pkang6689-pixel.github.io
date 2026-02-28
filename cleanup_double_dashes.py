#!/usr/bin/env python3
"""
Remove duplicate entries with double dashes (e.g., "- - Summary")
These were accidentally created when the script processed already-dashed entries.
"""

import re

def cleanup_double_dashes(file_path):
    """Remove lines with double-dash lesson entries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    removed_count = 0
    
    for line in lines:
        # Match pattern: "Lesson X.Y: ... - - (Summary|Practice|Quiz|Video)"
        if re.search(r'"Lesson\s+\d+\.\d+:[^"]*\s+-\s+-\s+(Summary|Practice|Quiz|Video)', line):
            removed_count += 1
            continue  # Skip this line
        new_lines.append(line)
    
    return ''.join(new_lines), removed_count

# Process all three files
files = [
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js',
]

for file_path in files:
    print(f"\nCleaning: {file_path}")
    try:
        new_content, removed = cleanup_double_dashes(file_path)
        
        if removed > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Removed {removed} double-dash entries")
        else:
            print("✓ No double-dash entries found")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Cleanup complete!")
