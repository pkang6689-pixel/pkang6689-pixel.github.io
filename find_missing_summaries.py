#!/usr/bin/env python3
"""
Find and translate missing summary strings
"""

import json
from pathlib import Path

def main():
    # Read extracted summary strings
    with open('/workspaces/ArisEdu/algebra2_summary_strings.json', 'r', encoding='utf-8') as f:
        summary_strings = json.load(f)
    
    print(f"Loaded {len(summary_strings)} summary strings")
    
    # Read existing translations from the generated translations file
    with open('/workspaces/ArisEdu/algebra2_translations_generated.json', 'r', encoding='utf-8') as f:
        existing_translations = json.load(f)
    
    print(f"Found {len(existing_translations)} existing translations")
    
    # Find which summary strings are NOT yet translated
    missing_strings = []
    for s in summary_strings:
        if s not in existing_translations:
            missing_strings.append(s)
    
    print(f"Missing translations: {len(missing_strings)}")
    
    if missing_strings:
        print("\nFirst 20 missing strings:")
        for s in missing_strings[:20]:
            print(f"  - {s[:80]}")
    
    # Save missing strings for translation
    with open('/workspaces/ArisEdu/algebra2_summary_missing.json', 'w', encoding='utf-8') as f:
        json.dump(missing_strings, f, ensure_ascii=False, indent=2)
    
    return missing_strings

if __name__ == "__main__":
    missing = main()
