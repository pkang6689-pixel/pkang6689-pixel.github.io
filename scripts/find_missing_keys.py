import os
import re
import json

def generate_missing_translations(): # This script will generate English-Chinese pairs for missing keys
    # 1. Collect all data-i18n keys from HTML files
    base_dirs = [
        "Algebra1Lessons", "Algebra2Lessons", "GeometryLessons",
        "BiologyLessons", "ChemistryLessons", "PhysicsLessons"
    ]
    root_path = "ArisEdu Project Folder"
    
    found_keys = set()
    
    # Regex to find data-i18n="..."
    i18n_pattern = re.compile(r'data-i18n="([^"]+)"')
    
    print("Scanning HTML files for keys...")
    for course_dir in base_dirs:
        full_path = os.path.join(root_path, course_dir)
        if not os.path.exists(full_path):
            continue
            
        for root, dirs, files in os.walk(full_path):
            for file in files:
                if file.endswith(".html"):
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            content = f.read()
                        matches = i18n_pattern.findall(content)
                        for m in matches:
                            if m.startswith("Lesson"): # Only care about Lesson titles for now
                                found_keys.add(m)
                    except:
                        pass
    
    print(f"Found {len(found_keys)} unique lesson keys.")
    
    # 2. Load existing keys from global_translations.js
    # This is tricky because it's a JS file, not JSON.
    # We'll validly read it as text and check for key presence.
    try:
        with open(os.path.join(root_path, "scripts/global_translations.js"), "r", encoding="utf-8") as f:
            js_content = f.read()
    except FileNotFoundError:
        print("global_translations.js not found!")
        return

    missing_keys = []
    for key in found_keys:
        # Check if key is in the file (simple string check is usually enough for existence)
        # We quote it to be sure we match the key, not some value
        if f'"{key}"' not in js_content and f"'{key}'" not in js_content:
            missing_keys.append(key)
            
    print(f"Found {len(missing_keys)} missing keys.")
    
    # 3. Generate translations (Mocking translation logic here)
    # Save to JSON file
    output_file = os.path.join(root_path, "../scripts/missing_translations.json")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(missing_keys, f, indent=4, ensure_ascii=False)
        print(f"Saved {len(missing_keys)} missing keys to {output_file}")
    except Exception as e:
        print(f"Error saving to file: {e}")

if __name__ == "__main__":
    generate_missing_translations()
