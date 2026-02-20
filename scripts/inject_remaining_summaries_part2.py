import json
import os

TRANSLATIONS_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"
NEW_TRANSLATIONS_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\remaining_summary_translations_part2.json"

def main():
    print(f"Reading new translations from {NEW_TRANSLATIONS_FILE}...")
    with open(NEW_TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
        new_translations = json.load(f)
    
    print(f"Reading global translations from {TRANSLATIONS_FILE}...")
    with open(TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Find insertion point
    # Looking for the end of the translations object.
    # It usually ends before "// Expose translations globally"
    
    insert_index = -1
    for i, line in enumerate(lines):
        if "window.arisEduTranslations = translations;" in line:
            # The closing brace should be shortly before this
            # Scan backwards from i
            for j in range(i, -1, -1):
                if lines[j].strip() == "};":
                    insert_index = j
                    break
            break
    
    if insert_index == -1:
        print("Could not find insertion point.")
        return

    print(f"Insertion point found at line {insert_index + 1}.")
    
    # Prepare lines to insert
    new_lines = []
    new_lines.append("\n  /* Remaining Biology Summary Fragments Part 2 */\n")
    for key, value in new_translations.items():
        line = f'  "{key}": "{value}",\n'
        new_lines.append(line)
        
    # Insert
    lines[insert_index:insert_index] = new_lines
    
    print(f"Writing updated file with {len(new_translations)} new entries...")
    with open(TRANSLATIONS_FILE, "w", encoding="utf-8") as f:
        f.writelines(lines)
        
    print("Done.")

if __name__ == "__main__":
    main()
