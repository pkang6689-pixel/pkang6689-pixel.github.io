#!/usr/bin/env python3
"""
Fix incorrect dash variants.
For example, if we have:
  "Lesson X.Y: Title Practice": "translation"
  "Lesson X.Y: Title - Summary": "translation"

The second should be:
  "Lesson X.Y: Title - Practice": "translation"

This script finds the non-dashed version, extracts the page type (Practice/Quiz/Video),
and ensures the dashed version uses the correct page type.
"""

import re

def fix_dash_variants(file_path):
    """Fix dash variants to match their non-dashed counterparts"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Find all lesson patterns
    # Match: "Lesson X.Y: Name PageType": "translation",
    non_dash_pattern = r'"(Lesson\s+\d+\.\d+:\s+[^"]+?)\s+(Practice|Quiz|Video)"\s*:\s*"([^"]*)"\s*,'
    
    matches = re.finditer(non_dash_pattern, content)
    
    replacements = 0
    for match in matches:
        lesson_name = match.group(1)
        page_type = match.group(2)
        translation = match.group(3)
        
        # Build the incorrect dash variant (with - Summary)
        incorrect_dash = f'"Lesson {lesson_name} - Summary"'
        
        # Build the correct dash variant (with proper page type)
        correct_dash = f'"Lesson {lesson_name} - {page_type}"'
        correct_entry = f'{correct_dash}: "{translation}",'
        
        # Find and replace the incorrect variant
        incorrect_pattern = f'"{lesson_name} - Summary": "{translation}",'
        if incorrect_pattern in content:
            content = content.replace(incorrect_pattern, correct_entry)
            replacements += 1
            print(f"  Fixed: {lesson_name}")
            print(f"    FROM: {lesson_name} - Summary")
            print(f"    TO:   {lesson_name} - {page_type}")
    
    return content, replacements, content != original_content

# Process all three files
files = [
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js',
]

for file_path in files:
    print(f"\nProcessing: {file_path}")
    try:
        new_content, replacements, changed = fix_dash_variants(file_path)
        
        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed {replacements} incorrect dash variants")
        else:
            print("✓ All dash variants are correct")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Complete!")
