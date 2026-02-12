
import os
import re

root_dir = '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons'

# 1. Update Back Button Text
# <button class="taskbar-button" id="back-button">← Back to Unit X</button>
# to
# <button class="taskbar-button" id="back-button">← Back to Chemistry</button>
# Use regex to be flexible about whitespace and unit number.
pattern_btn_text = r'(<button\s+class="taskbar-button"\s+id="back-button">\s*← Back to Unit \d+\s*</button>)'
replacement_btn_text = r'<button class="taskbar-button" id="back-button">← Back to Chemistry</button>'

# 2. Update window.location.href logic
# matches: window.location.href = 'ChemistryUnitXXX.html';
# to: window.location.href = '../../chem.html';
pattern_href = r"(window\.location\.href\s*=\s*)'ChemistryUnit[^']+\.html'(\s*;)"
replacement_href = r"\1'../../chem.html'\2"

# 3. Update window.originalBackLink
pattern_orig_link = r"(window\.originalBackLink\s*=\s*)'ChemistryUnit[^']+\.html'(\s*;)"
replacement_orig_link = r"\1'../../chem.html'\2"

# 4. Update restoreBtn.innerText
pattern_restore = r'(restoreBtn\.innerText\s*=\s*)"← Back to Unit"(\s*;)'
replacement_restore = r'\1"← Back to Chemistry"\2'


count_files_changed = 0

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.html'):
            file_path = os.path.join(dirpath, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            
            # Apply replacements
            new_content = re.sub(pattern_btn_text, replacement_btn_text, new_content)
            new_content = re.sub(pattern_href, replacement_href, new_content)
            new_content = re.sub(pattern_orig_link, replacement_orig_link, new_content)
            new_content = re.sub(pattern_restore, replacement_restore, new_content)

            if new_content != content:
                print(f"Updating {filename}...")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count_files_changed += 1

print(f"Finished. Updated {count_files_changed} files.")
