#!/usr/bin/env python3
"""
Inject all 1,941 other course translations into global_translations.js
"""

import json

def main():
    # Read translations
    with open('/workspaces/ArisEdu/other_courses_translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    print(f"Injecting {len(translations)} translations...")
    
    # Read JS file
    js_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    with open(js_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find closing brace from the end
    closing_idx = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip() == '};':
            # Verify this is translations closing
            found_translation = False
            for j in range(i-1, max(0, i-100), -1):
                if '": "' in lines[j]:
                    found_translation = True
                    break
            if found_translation:
                closing_idx = i
                break
    
    if closing_idx is None:
        print("ERROR: Could not find closing brace!")
        return False
    
    print(f"Found closing brace at line {closing_idx + 1}")
    
    # Generate entries
    entries = []
    for eng, chi in list(translations.items()):
        eng_escaped = eng.replace('"', '\\"').replace('\n', '\\n')
        chi_escaped = chi.replace('"', '\\"').replace('\n', '\\n')
        entry = f'    "{eng_escaped}": "{chi_escaped}",'
        entries.append(entry)
    
    # Insert before closing brace
    for entry in reversed(entries):
        lines.insert(closing_idx, entry + '\n')
    
    # Write back
    with open(js_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✓ Added {len(translations)} translations to global_translations.js!")
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
