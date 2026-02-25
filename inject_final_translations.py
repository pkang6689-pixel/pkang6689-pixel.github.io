#!/usr/bin/env python3
"""
Add the 10 final missing translations to global_translations.js
"""

import json

def main():
    # Read the final missing translations
    with open('/workspaces/ArisEdu/algebra2_final_missing_translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    print(f"Injecting {len(translations)} final translations...")
    
    # Read global_translations.js
    js_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    with open(js_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the line with the closing brace }; for translations (searching from end)
    closing_idx = None
    for i in range(len(lines)-1, -1, -1):
        if lines[i].strip() == '};':
            # Make sure we're in the translations object
            # by checking if there are translation entries before
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
    
    # Generate new entries
    new_entries = []
    for eng, chi in translations.items():
        eng_escaped = eng.replace('"', '\\"')
        chi_escaped = chi.replace('"', '\\"')
        entry = f'    "{eng_escaped}": "{chi_escaped}",'
        new_entries.append(entry)
    
    # Insert before closing brace
    for entry in reversed(new_entries):
        lines.insert(closing_idx, entry + '\n')
    
    # Write back
    with open(js_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"✓ Added {len(translations)} final translations!")
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
