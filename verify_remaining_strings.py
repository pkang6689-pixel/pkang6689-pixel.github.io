import json
import os
import re

def load_global_translations(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract the JS object inside const translations = { ... };
    # We can use regex or just basic parsing if it's consistently formatted.
    # It might be safer to extract keys using regex: "Key": or 'Key':
    
    # Regex for keys:  "String": "Translation" or 'String': 'Translation'
    # Wait, keys might contain quotes.
    # A simpler approach: Just check if the string exists in the file content as a key.
    # Pattern: \s*["'](.*?)["']\s*:\s*["'].*?["']
    
    keys = set()
    matches = re.findall(r'^\s*["\'](.*?)["\']\s*:', content, re.MULTILINE)
    keys.update(matches)
    return keys

def main():
    try:
        with open("quiz_dataset.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("quiz_dataset.json not found in current directory.")
        return

    questions = set(data.get("questions", []))
    answers = set(data.get("answers", []))
    
    all_strings = questions.union(answers)
    print(f"Total Unique Strings from Source: {len(all_strings)}")

    global_path = "ArisEdu Project Folder/scripts/global_translations.js"
    translated_keys = load_global_translations(global_path)
    print(f"Total Keys in Global Translations: {len(translated_keys)}")

    missing = []
    for s in all_strings:
        if s not in translated_keys:
            # Maybe some normalization?
            # JS keys might be escaped.
            # But let's assume exact match first.
            missing.append(s)

    # Sort alphabet
    missing.sort()

    print(f"Missing Strings: {len(missing)}")
    
    # Check specifically for "Select..."
    select_strings = [s for s in missing if "Select the definition" in s]
    print(f"Found {len(select_strings)} 'Select the definition' strings in missing list.")
    
    with open("true_remaining_strings.json", "w", encoding="utf-8") as f:
        json.dump(missing, f, indent=4)
        print("Saved to true_remaining_strings.json")

    # Also save missing by starting letter distribution
    dist = {}
    for s in missing:
        if s:
            first = s[0].upper()
            dist[first] = dist.get(first, 0) + 1
    
    print("\nMissing Count by First Letter:")
    for k in sorted(dist.keys()):
        print(f"{k}: {dist[k]}")

if __name__ == "__main__":
    main()
