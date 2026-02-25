import re
import json

def extract_keys():
    js_file = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"
    output_file = r"c:\Users\Peter\pkang6689-pixel.github.io\scripts\english_keys.json"
    
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex to find "Key": "Value" pattern
    # Assuming standard JSON-like format within the JS object
    # pattern = r'"([^"]+)":\s*"[^"]*",'
    
    # Better approach might be to find the start of the object and parse it, but it's JS, not JSON.
    # It starts with `const translations = {` and ends with `};`
    
    start_marker = "const translations = {"
    end_marker = "};"
    
    start_index = content.find(start_marker)
    if start_index == -1:
        print("Could not find start of translations object.")
        return

    # approximate extraction
    # We will look for lines that look like "key": "value",
    
    keys = []
    
    # iterate line by line to be safe against complex parsing without a JS parser
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        # Match "Key": "Value", or 'Key': 'Value',
        match = re.search(r'^["\'](.+?)["\']\s*:\s*["\'].+?["\'],?$', line)
        if match:
            keys.append(match.group(1))
            
    print(f"Found {len(keys)} keys.")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(keys, f, indent=4)

if __name__ == "__main__":
    extract_keys()
