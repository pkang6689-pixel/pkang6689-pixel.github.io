#!/usr/bin/env python3
"""
Fix translation file consistency issues:
1. Remove duplicate page types (e.g., "Summary Summary")
2. Maintain proper formatting across all three languages
"""

import re
from pathlib import Path

def fix_duplicate_page_types(file_path):
    """Remove duplicate page type suffixes like 'Summary Summary'"""
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # Pattern: find lesson entries with duplicate page types
    # Match: "Lesson X.Y: ... Summary Summary": or similar
    # Replace with single page type
    
    patterns_to_fix = [
        (r'("Lesson \d+\.\d+: [^"]+?) Summary Summary":', r'\1 Summary":'),
        (r'("Lesson \d+\.\d+: [^"]+?) Practice Practice":', r'\1 Practice":'),
        (r'("Lesson \d+\.\d+: [^"]+?) Quiz Quiz":', r'\1 Quiz":'),
        (r'("Lesson \d+\.\d+: [^"]+?) Video Video":', r'\1 Video":'),
    ]
    
    count_fixed = 0
    for pattern, replacement in patterns_to_fix:
        matches = re.findall(pattern, content)
        count = len(matches)
        if count > 0:
            content = re.sub(pattern, replacement, content)
            count_fixed += count
            print(f"  Fixed {count} duplicate page types: {pattern}")
    
    was_modified = content != original_content
    return content, count_fixed, was_modified

def main():
    base_path = Path("ArisEdu Project Folder/scripts")
    files_to_fix = [
        ("Chinese", base_path / "global_translations.js"),
        ("Spanish", base_path / "spanish_translations.js"),
        ("Hindi", base_path / "hindi_translations.js"),
    ]
    
    print("=" * 80)
    print("FIXING TRANSLATION FILE CONSISTENCY")
    print("=" * 80)
    
    total_fixed = 0
    total_files_modified = 0
    
    for lang_name, file_path in files_to_fix:
        if not file_path.exists():
            print(f"\n[{lang_name.upper()}] SKIP - File not found: {file_path}")
            continue
        
        print(f"\n[{lang_name.upper()}] {file_path.name}")
        
        try:
            content, count_fixed, was_modified = fix_duplicate_page_types(file_path)
            
            if was_modified:
                # Write back the fixed content
                file_path.write_text(content, encoding='utf-8')
                print(f"  ✓ Wrote fixed file ({count_fixed} duplicates removed)")
                total_fixed += count_fixed
                total_files_modified += 1
            else:
                print(f"  ✓ No issues found")
                
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Fixed {total_fixed} duplicate entries in {total_files_modified} files")
    print("=" * 80)

if __name__ == "__main__":
    main()
