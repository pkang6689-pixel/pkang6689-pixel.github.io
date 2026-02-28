#!/usr/bin/env python3
"""
Fix dashed lesson entries where translation has wrong page type.
For example, "Lesson X: Title - Practice" shouldn't have "总结" (summary) in it.
"""

import re

def fix_page_type_translations(file_path, lang='chinese'):
    """Fix dashed entries with wrong page type in translation"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    changed_count = 0
    
    # Map of page type replacements based on language
    if lang == 'chinese':
        replacements = {
            'Practice': ('总结', '练习'),
            'Quiz': ('总结', '测验'),
            'Video': ('总结', '视频'),
        }
    elif lang == 'spanish':
        replacements = {
            'Practice': ('Resumen', 'Práctica'),
            'Quiz': ('Resumen', 'Cuestionario'),
            'Video': ('Resumen', 'Video'),
        }
    elif lang == 'hindi':
        replacements = {
            'Practice': ('सारांश', 'अभ्यास'),
            'Quiz': ('सारांश', 'प्रश्नोत्तरी'),
            'Video': ('सारांश', 'वीडियो'),
        }
    else:
        return content, 0
    
    # For each page type (Practice, Quiz, Video)
    for page_type, (wrong_word, right_word) in replacements.items():
        # Find all dashed entries for this page type
        pattern = rf'"(Lesson\s+\d+\.\d+:\s+[^"]+?)\s+-\s+{page_type}"\s*:\s*"([^"]*)"\s*,'
        
        def replacer(match):
            nonlocal changed_count
            lesson_name = match.group(1)
            translation = match.group(2)
            
            # Check if translation has the wrong word
            if wrong_word in translation:
                new_translation = translation.replace(wrong_word, right_word, 1)
                if new_translation != translation:
                    changed_count += 1
                    print(f"  {page_type}: {lesson_name}")
                    print(f"    {translation} → {new_translation}")
                    return f'"{lesson_name} - {page_type}": "{new_translation}",'
            
            return match.group(0)
        
        content = re.sub(pattern, replacer, content)
    
    return content, changed_count

# Process files for each language
file_specs = [
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\global_translations.js', 'chinese'),
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\spanish_translations.js', 'spanish'),
    ('c:\\Users\\Peter\\pkang6689-pixel.github.io\\ArisEdu Project Folder\\scripts\\hindi_translations.js', 'hindi'),
]

for file_path, lang in file_specs:
    print(f"\nProcessing {lang}: {file_path}")
    try:
        new_content, changed = fix_page_type_translations(file_path, lang)
        
        if changed > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Fixed {changed} entries")
        else:
            print("✓ No fixes needed")
    except Exception as e:
        print(f"✗ Error: {e}")

print("\n✓ Complete!")
