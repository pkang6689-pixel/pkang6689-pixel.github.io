import os
import re

base_dir = "ArisEdu Project Folder/ChemistryLessons"

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Update button text in HTML
    # Matches <button ...>← Back to Unit 1</button>
    content = re.sub(r'(<button[^>]*id="back-button"[^>]*>)\s*← Back to Unit \d+\s*(</button>)', r'\1Back to Chemistry\2', content)
    
    # 2. Update window.originalBackLink
    content = re.sub(r"window\.originalBackLink\s*=\s*['\"]ChemistryUnit[^'\"]+\.html['\"];", "window.originalBackLink = '../../chem.html';", content)
    
    # 3. Update hardcoded event listener
    # document.getElementById('back-button').addEventListener... window.location.href = 'ChemistryUnit1Matter.html';
    content = re.sub(r"(window\.location\.href\s*=\s*)['\"]ChemistryUnit[^'\"]+\.html['\"];", r"\1'../../chem.html';", content)
    
    # 4. Update restoreBtn text
    content = content.replace('restoreBtn.innerText = "← Back to Unit";', 'restoreBtn.innerText = "Back to Chemistry";')
    
    # 5. Also catch "← Back to " + lessonName logic which might overwrite the text temporarily?
    # No, that logic changes it when going TO a sub-view (Summary). We want the restore logic (Step 4) to be correct.
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes for {file_path}")

def main():
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".html") and not file.startswith("ChemistryUnit"):
                # Avoid processing non-lesson files if any exist (though we deleted unit homepages)
                update_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
