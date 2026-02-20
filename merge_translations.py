import json
import re
import os

def load_js_translations(file_path):
    keys = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                # Regex for double quoted key followed by colon, handling escaped quotes
                m = re.match(r'^("(?:\\[\s\S]|[^"\\])*")\s*:', line)
                if m:
                    key_str = m.group(1)
                    try:
                        key = json.loads(key_str)
                        keys.add(key)
                    except json.JSONDecodeError as e:
                        print(f"Warning: JSON decode error on line {i+1}: {e}")
                        pass
                    continue
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return keys

def main():
    base_path = r"c:\Users\Peter\pkang6689-pixel.github.io"
    js_path = os.path.join(base_path, "ArisEdu Project Folder", "scripts", "global_translations.js")
    json1_path = os.path.join(base_path, "remaining_summary_translations.json")
    json2_path = os.path.join(base_path, "remaining_summary_translations_part2.json")

    existing_keys = load_js_translations(js_path)
    print(f"Loaded {len(existing_keys)} keys from global_translations.js")

    new_translations = {}

    for json_path in [json1_path, json2_path]:
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for key, value in data.items():
                        if key not in existing_keys:
                            new_translations[key] = value
            except Exception as e:
                print(f"Error processing {json_path}: {e}")

    # Check for specific keys known to be problematic
    prob_keys = [
        ': The organism\'s role in its ecosystem (its "job")',
        'Define key terms related to aquatic ecosystems'
    ]
    for pk in prob_keys:
        if pk in existing_keys:
            print(f"Key '{pk}' found in JS file.")
        else:
            print(f"Key '{pk}' NOT found in JS file.")

    sorted_keys = sorted(new_translations.keys())

    if not new_translations:
        print("No new unique translations found.")
    else:
        print(f"Found {len(new_translations)} new unique translations.")
        print("-" * 20)
        for key in sorted_keys:
            value = new_translations[key]
            line = json.dumps({key: value}, ensure_ascii=False)
            line = line[1:-1].strip() + ","
            print(f"  {line}")
        print("-" * 20)

if __name__ == "__main__":
    main()