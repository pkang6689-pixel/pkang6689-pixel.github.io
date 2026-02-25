#!/usr/bin/env python3
"""
Inject the generated Algebra 2 translations into global_translations.js
"""

import json

def main():
    # Read the generated translations
    with open('/workspaces/ArisEdu/algebra2_translations_generated.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    print(f"Loading {len(translations)} translations...")
    
    # Read the current global_translations.js
    js_file = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the closing of the translations object (line 30593 has "    };")
    lines = content.split('\n')
    closing_line_idx = None
    
    # Find the line with "    };" that closes the translations object
    for i, line in enumerate(lines):
        if line.strip() == '};':
            # Check if this is likely the translations closing by looking backwards
            # for the last translation entry (should have quotes and colon)
            found_translation_before = False
            for j in range(i-1, max(0, i-50), -1):
                if '": "' in lines[j] or (lines[j].strip().endswith(',') and '": "' in lines[j]):
                    found_translation_before = True
                    break
            if found_translation_before:
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
    
    # The last entry in the translations object should NOT have a trailing comma
    # So we need to add a comma after the last existing entry
    # Insert the new entries before the closing brace
    lines.insert(closing_line_idx, new_entries_str + ',')
    
    # Write back
    new_content = '\n'.join(lines)
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Added {len(translations)} translations to global_translations.js")
    print("✓ Successfully injected translations!")
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
