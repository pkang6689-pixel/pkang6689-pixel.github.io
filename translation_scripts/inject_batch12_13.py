
import json
import os

TRANSLATIONS_FILE = "../scripts/quiz_translations_batch12_13.json"
TARGET_FILE = "../ArisEdu Project Folder/scripts/global_translations.js"

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
        if line.startswith("};"):
            insertion_index = i
            break
            
    if insertion_index == -1:
        print("Error: Could not find closing brace of translations object.")
        return

    print(f"Found insertion point at line {insertion_index + 1}")
    
    # Prepare lines to insert
    # We need to make sure we add a comma to the previous last element if it doesn't have one
    # But usually it's cleaner to just append keys.
    # The '};' is the closing brace. We should insert before it.
    # Also need to check if the previous line has a comma.
    
    # Check previous non-empty line
    prev_line_index = insertion_index - 1
    while prev_line_index >= 0 and not lines[prev_line_index].strip():
        prev_line_index -= 1
        
    if prev_line_index >= 0:
        prev_line = lines[prev_line_index].strip()
        # If the last line is not a comment and doesn't end with comma, add comma
        if not prev_line.endswith(",") and not prev_line.startswith("//") and not prev_line.startswith("/*"):
             # modify the line in memory
             lines[prev_line_index] = lines[prev_line_index].rstrip() + ",\n"

    new_lines = []
    new_lines.append("\n  /* Batch 12-13 Quiz Strings */\n")
    for key, value in new_translations.items():
        # Escape quotes in key and value
        safe_key = key.replace('"', '\\"').replace('\n', ' ')
        safe_value = value.replace('"', '\\"').replace('\n', ' ')
        new_lines.append(f'  "{safe_key}": "{safe_value}",\n')
        
    # Insert new lines
    lines[insertion_index:insertion_index] = new_lines
    
    print(f"Injecting {len(new_translations)} translations...")
    with open(TARGET_FILE, "w") as f:
        f.writelines(lines)
        
    print("Done.")

if __name__ == "__main__":
    main()
