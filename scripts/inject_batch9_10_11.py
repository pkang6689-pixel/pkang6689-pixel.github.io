
import json
import os

TRANSLATIONS_FILE = "scripts/quiz_translations_batch9_10_11.json"
TARGET_FILE = "ArisEdu Project Folder/scripts/global_translations.js"

def main():
    if not os.path.exists(TRANSLATIONS_FILE):
        print(f"Error: {TRANSLATIONS_FILE} not found. Wait for translation to finish.")
        return

    print(f"Reading translations from {TRANSLATIONS_FILE}...")
    with open(TRANSLATIONS_FILE, "r") as f:
        new_translations = json.load(f)
    
    print(f"Reading target file {TARGET_FILE}...")
    with open(TARGET_FILE, "r") as f:
        lines = f.readlines()
    
    # improved mechanism to find insertion point
    insertion_index = -1
    for i in range(len(lines) - 1, -1, -1):
        line = lines[i].strip()
        if line == "};" or line.startswith("};"):
            insertion_index = i
            break
            
    if insertion_index == -1:
        print("Error: Could not find closing brace of translations object.")
        return
        
    print(f"Found insertion point at line {insertion_index + 1}")
    
    # Check if previous line has a comma
    prev_line_idx = insertion_index - 1
    while prev_line_idx >= 0 and not lines[prev_line_idx].strip():
        prev_line_idx -= 1
        
    if prev_line_idx >= 0:
        prev_line = lines[prev_line_idx].rstrip()
        if not prev_line.endswith(",") and not prev_line.endswith("{"):
            print(f"Adding comma to line {prev_line_idx + 1}")
            lines[prev_line_idx] = prev_line + ",\n"

    # Prepare new lines
    new_lines = []
    keys = sorted(new_translations.keys())
    for key in keys:
        val = new_translations[key]
        # properly escape quotes
        safe_key = key.replace('"', '\\"')
        safe_val = val.replace('"', '\\"')
        # Use json.dumps to handle escaping automatically if preferred, but manual control is fine
        # We'll use ensure_ascii=False format generally, or just string interpolation
        line = f'  "{safe_key}": "{safe_val}",\n'
        new_lines.append(line)
        
    # Insert
    lines[insertion_index:insertion_index] = new_lines
    
    print(f"Injecting {len(new_lines)} translations...")
    with open(TARGET_FILE, "w") as f:
        f.writelines(lines)
        
    print("Done.")

if __name__ == "__main__":
    main()
