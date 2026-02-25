#!/usr/bin/env python3
"""
Find flashcard strings that are missing translations
"""

import json

def main():
    # Read extracted flashcard strings
    with open('/workspaces/ArisEdu/algebra2_flashcard_strings.json', 'r', encoding='utf-8') as f:
        flashcard_strings = json.load(f)
    
    print(f"Loaded {len(flashcard_strings)} flashcard strings")
    
    # Read existing translations
    with open('/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js', 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    # Parse the translations from JavaScript
    # This is a rough check - count how many flashcard strings appear in the JS file
    found = 0
    missing = []
    
    for s in flashcard_strings:
        # Escape quotes for searching in JS
        search_str = s.replace('"', '\\"')
        if f'"{search_str}"' in js_content:
            found += 1
        else:
            missing.append(s)
    
    print(f"Found {found} flashcard strings in translations")
    print(f"Missing {len(missing)} flashcard strings")
    
    if missing:
        print(f"\nFirst 20 missing flashcard strings:")
        for s in missing[:20]:
            print(f"  - {s[:100]}")
    
    # Save missing
    with open('/workspaces/ArisEdu/algebra2_flashcard_missing.json', 'w', encoding='utf-8') as f:
        json.dump(missing, f, ensure_ascii=False, indent=2)
    
    return missing

if __name__ == "__main__":
    missing = main()
