import json
import re

def filter_strings():
    # Load existing translations
    existing_keys = set()
    with open("../ArisEdu Project Folder/scripts/global_translations.js", "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract keys using regex:  "Key": "Value"
    # Handling nested quotes might be tricky, but keys are usually simple strings.
    # Regex: \s*"(.+?)":\s*".*",?
    matches = re.finditer(r'^\s*"(.+?)":\s*".*",?$', content, re.MULTILINE)
    for match in matches:
        existing_keys.add(match.group(1))
        
    print(f"Loaded {len(existing_keys)} existing translation keys.")
    
    # Load extracted quiz strings
    with open("../quiz_strings.json", "r", encoding="utf-8") as f:
        quiz_strings = json.load(f)
        
    print(f"Loaded {len(quiz_strings)} quiz strings.")
    
    new_strings = []
    skipped_count = 0
    numeric_count = 0
    
    for s in quiz_strings:
        # Skip if already translated
        if s in existing_keys:
            skipped_count += 1
            continue
            
        # Skip if pure number or simple math (e.g. "1.5", "100", "x + y")
        # Check if contains at least one letter
        if not re.search(r'[a-zA-Z]', s):
            numeric_count += 1
            continue
            
        # Skip very short strings? No, "Fe" (Iron) is short but needs translation context (usually keys are English).
        # Actually "Fe" is universal symbol.
        if len(s) < 2:
            numeric_count += 1
            continue
            
        new_strings.append(s)
        
    print(f"Skipped {skipped_count} existing translations.")
    print(f"Skipped {numeric_count} numeric/simple strings.")
    print(f"Remaining strings to translate: {len(new_strings)}")
    
    with open("../remaining_quiz_strings.json", "w", encoding="utf-8") as f:
        json.dump(new_strings, f, indent=4)

if __name__ == "__main__":
    filter_strings()
