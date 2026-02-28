#!/usr/bin/env python3
"""
Standardize lesson entry formats across translation files.
Ensures all lessons follow the pattern: "Lesson X.Y: Title - PageType"
with consistent dashes and page type names.
"""

import re
from pathlib import Path
from collections import defaultdict

def standardize_translations(file_path):
    """Standardize lesson entry formats in translation file"""
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # Pattern to find non-standardized lesson entries
    # We want to ensure all lesson entries use dashes
    # Standard format: "Lesson X.Y: Title - PageType"
    
    changes = {
        'normalized_to_dashed': 0,
        'fixed_spacing': 0,
    }
    
    # 1. Convert entries like "Lesson 1.1: Title Summary" -> "Lesson 1.1: Title - Summary"
    #    (for lesson entries without dashes but with page types)
    pattern1 = r'"(Lesson \d+\.\d+: [^-"]+)\s+(Summary|Practice|Quiz|Video)":'
    matches = list(re.finditer(pattern1, content))
    if matches:
        def replace_func(match):
            lesson_part = match.group(1)
            page_type = match.group(2)
            # Check if it already has a dash at the end
            if lesson_part.rstrip().endswith('-'):
                return f'"{lesson_part.rstrip()} {page_type}":'
            else:
                return f'"{lesson_part.rstrip()} - {page_type}":'
        
        content = re.sub(pattern1, replace_func, content)
        changes['normalized_to_dashed'] = len(matches)
    
    # 2. Fix spacing around dashes: "Title-PageType" -> "Title - PageType"
    pattern2 = r'"(Lesson \d+\.\d+: [^"]+?)(-)([A-Z])'
    matches = list(re.finditer(pattern2, content))
    if matches:
        content = re.sub(pattern2, r'"\1 - \3', content)
        changes['fixed_spacing'] = len(matches)
    
    # 3. Remove trailing spaces before page types
    pattern3 = r'"(Lesson \d+\.\d+: [^"]+?)\s+-\s+(Summary|Practice|Quiz|Video)":'
    matches = list(re.finditer(pattern3, content))
    if matches:
        content = re.sub(pattern3, r'"\1 - \2":', content)
    
    was_modified = content != original_content
    return content, changes, was_modified

def main():
    base_path = Path("ArisEdu Project Folder/scripts")
    files_to_standardize = [
        ("Chinese", base_path / "global_translations.js"),
        ("Spanish", base_path / "spanish_translations.js"),
        ("Hindi", base_path / "hindi_translations.js"),
    ]
    
    print("=" * 80)
    print("STANDARDIZING LESSON ENTRY FORMATS")
    print("=" * 80)
    
    total_changes = defaultdict(int)
    total_files_modified = 0
    
    for lang_name, file_path in files_to_standardize:
        if not file_path.exists():
            print(f"\n[{lang_name.upper()}] SKIP - File not found: {file_path}")
            continue
        
        print(f"\n[{lang_name.upper()}] {file_path.name}")
        
        try:
            content, changes, was_modified = standardize_translations(file_path)
            
            if was_modified:
                file_path.write_text(content, encoding='utf-8')
                print(f"  ✓ Normalized to dashed format: {changes['normalized_to_dashed']}")
                print(f"  ✓ Fixed dash spacing: {changes['fixed_spacing']}")
                for key in changes:
                    total_changes[key] += changes[key]
                total_files_modified += 1
            else:
                print(f"  ✓ Already standardized")
                
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Standardized {total_files_modified} translation files")
    for change_type, count in total_changes.items():
        if count > 0:
            print(f"  • {change_type}: {count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
