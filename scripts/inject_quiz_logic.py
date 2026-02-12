import glob
import os

ROOT_DIR = "ArisEdu Project Folder/ChemistryLessons"
INJECT_TAG = '<script src="/quiz_logic.js"></script>'
TARGET_MARKER = '<script src="/global_translations.js"></script>'

def inject_logic():
    files = glob.glob(os.path.join(ROOT_DIR, "Unit*", "*_Test.html"))
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if INJECT_TAG in content:
            print(f"Skipping {file_path}, already has logic.")
            continue
            
        if TARGET_MARKER in content:
            # Insert after the target marker
            new_content = content.replace(TARGET_MARKER, TARGET_MARKER + '\n' + INJECT_TAG)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected quiz logic into {file_path}")
        else:
            print(f"Warning: Marker not found in {file_path}")

if __name__ == "__main__":
    inject_logic()
