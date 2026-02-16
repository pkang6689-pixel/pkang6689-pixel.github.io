import json
import re

translation_file = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"
popup_file = "extracted_popups.json"

try:
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content) or             re.search(r'window\.globalTranslations\s*=\s*({[\s\S]*?});', content)
            
    if not match:
        print("Error: Could not find translation object")
        exit(1)
        
    # parse existing keys
    raw_json = match.group(1)
    # simple regex key extraction
    existing_keys = set(re.findall(r'["\'](.*?)["\']\s*:', raw_json))
    
    # load popups
    with open(popup_file, 'r') as f:
        # Skip the first line "Found 109..."
        lines = f.readlines()
        json_line = lines[1] if len(lines) > 1 else lines[0]
        popups = json.loads(json_line)
        
    missing = []
    for p in popups:
        if p not in existing_keys:
            missing.append(p)
            
    print(f"Missing {len(missing)} popup translations:")
    for m in sorted(missing):
        print(f'"{m}": "{m}",') # Print as JSON entries for easy copy

except Exception as e:
    print(f"Error: {e}")
