#!/usr/bin/env python3
"""
Add dash variants to all lesson translations.
For example, if "Lesson 2.2: Acceleration Summary" exists,
add "Lesson 2.2: Acceleration - Summary" right after it.
"""

import re
import json

def add_dash_variants(file_path):
    """Add dash variants to lesson translations in a file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match lesson entries without dashes
    # Matches: "Lesson X.Y: Title Summary/Practice/Quiz/Video": "translation"
    pattern = r'"(Lesson\s+\d+\.\d+:\s+[^"]+?)\s+(Summary|Practice|Quiz|Video)(?:\s+Summary)?"\s*:\s*"([^"]*)"\s*,'
    
    def replacer(match):
        prefix = match.group(1)
        page_type = match.group(2)
        translation = match.group(3)
        original = match.group(0)
        
        # Create the dash variant
        dash_key = f'"{prefix} - {page_type}"'
        dash_entry = f'{dash_key}: "{translation}",'
        
        # Return original + dash variant on new line
        return original + '\n    ' + dash_entry
    
    # Apply the replacer
    new_content = re.sub(pattern, replacer, content)
    
    # Count how many changes were made
    changes = len(re.findall(pattern, content))
    
    return new_content, changes

# Process all three files
files = [
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js',
    'c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js',
]

for file_path in files:
    print(f"\nProcessing: {file_path}")
    try:
        new_content, changes = add_dash_variants(file_path)
        
        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Added {changes} dash variants")
        else:
            print("✓ No changes needed (all dash variants already present)")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Complete!")
