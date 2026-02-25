#!/usr/bin/env python3
"""
Inject the 679 translated summary strings into global_translations.js
"""

import json

def main():
    # Read the summary translations
    with open('/workspaces/ArisEdu/algebra2_summary_translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    print(f"Loading {len(translations)} summary translations...")
    
    # Read the current global_translations.js
    js_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the closing brace of the translations object
    lines = content.split('\n')
    closing_line_idx = None
    
    # Search backwards from end for the closing brace
    for i in range(len(lines)-1, 0, -1):
        if lines[i].strip() == '};':
            # Check if this is likely the translations closing
            # by counting braces backwards
            found_translation = False
            for j in range(i-1, max(0, i-100), -1):
                if '": "' in lines[j] and (',' in lines[j] or ':' in lines[j]):
                    found_translation = True
                    break
            if found_translation:
                closing_line_idx = i
                break
    
    if closing_line_idx is None:
        print("ERROR: Could not find the closing brace of translations object!")
        return False
    
    print(f"Found closing brace at line {closing_line_idx + 1}")
    
    # Generate the new translation entries in JavaScript format
    new_entries = []
    entries_list = list(translations.items())
    
    for i, (english, chinese) in enumerate(entries_list):
        # Escape quotes in the strings
        eng_escaped = english.replace('"', '\\"').replace('\n', '\\n')
        chi_escaped = chinese.replace('"', '\\"').replace('\n', '\\n')
        
        # Format as JavaScript object entry
        entry = f'    "{eng_escaped}": "{chi_escaped}"'
        new_entries.append(entry)
    
    # Join all entries with commas
    new_entries_str = ',\n'.join(new_entries)
    
    # Insert the new entries before the closing brace
    lines.insert(closing_line_idx, new_entries_str + ',')
    
    # Write back
    new_content = '\n'.join(lines)
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Added {len(translations)} summary translations to global_translations.js")
    print("✓ Successfully injected translations!")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
