import os
import re

# Logic to calculate relative path to scripts folder
# Base path of scripts: ArisEdu Project Folder/scripts
# Root of content: ArisEdu Project Folder/

root_dir = "."
target_files = []

# Scan for HTML files
for dirpath, dirnames, filenames in os.walk(root_dir):
    if "node_modules" in dirpath or ".git" in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".html"):
            target_files.append(os.path.join(dirpath, filename))

# Regex Patterns
# 1. CSS Pattern (internal content only)
# Matches starts with /* Fixed Practices Menu CSS */ and ends with } (last rule)
CSS_PATTERN = re.compile(r"/\* Fixed Practices Menu CSS \*/[\s\S]*?\.Practices-panel a:hover\s*\{[\s\S]*?\}" , re.MULTILINE)

# 2. Video JS Pattern (Whole script tag)
# Starts with <script> then optional whitespace then let videoStopTimer
VIDEO_SCRIPT_PATTERN = re.compile(r"<script>\s*let videoStopTimer = null;[\s\S]*?</script>", re.MULTILINE)

# 3. Blocks Puzzle Loop Pattern (Whole script tag)
# Starts with <script> then optional whitespace then (function() {
# Contains known unique string "const BOARD_SIZE =" just to be safe
# Ends with })(); then optional whitespace then </script>
PUZZLE_SCRIPT_PATTERN = re.compile(r"<script>\s*\(function\(\)\s*\{[\s\S]*?const BOARD_SIZE = \d+;[\s\S]*?\}\)\(\);\s*</script>", re.MULTILINE)

def get_script_rel_path(file_path):
    # file_path is relative to CWD (root of repo)
    # Target: ArisEdu Project Folder/scripts
    
    abs_file = os.path.abspath(file_path)
    target_dir = os.path.abspath("ArisEdu Project Folder/scripts")
    file_dir = os.path.dirname(abs_file)
    rel_path = os.path.relpath(target_dir, file_dir)
    return rel_path.replace("\\", "/") # Ensure forward slashes

count_css = 0
count_video = 0
count_puzzle = 0

for file_path in target_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        rel_path = get_script_rel_path(file_path)
        
        # 1. CSS Removal
        if CSS_PATTERN.search(content):
            content = CSS_PATTERN.sub("", content)
            count_css += 1
            
        # 2. Video JS Replacement
        if VIDEO_SCRIPT_PATTERN.search(content):
            replacement = f'<script src="{rel_path}/lesson_video.js"></script>'
            content = VIDEO_SCRIPT_PATTERN.sub(replacement, content)
            count_video += 1
            
        # 3. Puzzle JS Replacement
        if PUZZLE_SCRIPT_PATTERN.search(content):
            replacement = f'<script src="{rel_path}/blocks_puzzle.js"></script>'
            content = PUZZLE_SCRIPT_PATTERN.sub(replacement, content)
            count_puzzle += 1
            
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            # print(f"Updated {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"Summary: CSS removed in {count_css} files.")
print(f"Summary: Video JS replaced in {count_video} files.")
print(f"Summary: Puzzle JS replaced in {count_puzzle} files.")
