#!/usr/bin/env python3
"""
Fix dash variants to use correct page-type translations.
For example, if "Lesson X: Title Practice" has "练习" in translation,
then "Lesson X: Title - Practice" should have the same "练习" translation.
"""

import re

def fix_translations(file_path):
    """Fix dashed lesson translations to match their page types"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Strategy: For each dashed entry, check if there's a non-dashed counterpart
    # and copy its translation
    
    # First, build a map of non-dashed translations
    non_dash_pattern = r'"(Lesson\s+\d+\.\d+:\s+[^"]+?)\s+(Practice|Quiz|Video)"\s*:\s*"([^"]*)"\s*,'
    non_dash_map = {}
    
    for match in re.finditer(non_dash_pattern, content):
        lesson_name = match.group(1)
        page_type = match.group(2)
        translation = match.group(3)
        non_dash_map[f"{lesson_name}|{page_type}"] = translation
    
    # Now fix all dashed entries
    dash_pattern = r'"(Lesson\s+\d+\.\d+:\s+[^"]+?)\s+-\s+(Practice|Quiz|Video)"\s*:\s*"([^"]*)"\s*,'
    
    def replacer(match):
        lesson_name = match.group(1)
        page_type = match.group(2)
        current_translation = match.group(3)
        
        # Look for non-dashed version
        key = f"{lesson_name}|{page_type}"
        if key in non_dash_map:
            correct_translation = non_dash_map[key]
            if current_translation != correct_translation:
                print(f"  Fixing: {lesson_name} - {page_type}")
                print(f"    FROM: {current_translation}")
                print(f"    TO:   {correct_translation}")
                return f'"{lesson_name} - {page_type}": "{correct_translation}",'
        
        return match.group(0)
    
    new_content = re.sub(dash_pattern, replacer, content)
    
    return new_content, new_content != original_content

# Process all three files
files = [
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js',
]

for file_path in files:
    print(f"\nProcessing: {file_path}")
    try:
        new_content, changed = fix_translations(file_path)
        
        if changed:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed dash variant translations")
        else:
            print("✓ All dash variants already correct")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Complete!")
