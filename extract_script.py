import re
import os

source_file = "ArisEdu Project Folder/ChemistryLessons/Unit1/Lesson 1.1 States_of_Matter.html"

with open(source_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Extract Video Logic
# Pattern: let videoStopTimer = null; ... up to the end of the script tag or specific marker?
# It seems to be inside a <script> tag.
# Let's look for the specific strings.
video_start_marker = "let videoStopTimer = null;"
video_end_marker = "const button = event.target.closest('.view-other-videos');"
# Use regex to capture the block
video_pattern = r"let videoStopTimer = null;[\s\S]*?document\.addEventListener\('click', \(event\) => \{\s+const button = event\.target\.closest\('\.view-other-videos'\);\s+if \(!button\) \{\s+return;\s+\}\s+\}\);"

# Let's try a broader capture based on structure if I can't match exact end
# It seems the video logic is in a <script> tag that MIGHT contain other things?
# In the read_file output, it looked like:
# <script>
#    let videoStopTimer = null;
#    ...
#    document.addEventListener('click', (event) => { ... });
# </script>

# I will try to find the start and scan for the end of the script tag or logical end.
start_idx = content.find(video_start_marker)
if start_idx != -1:
    # Find the closing </script> tag after this
    end_script_idx = content.find("</script>", start_idx)
    video_js_content = content[start_idx:end_script_idx].strip()
    
    # Save to file
    with open("scripts/lesson_video.js", "w", encoding="utf-8") as f:
        f.write(video_js_content)
    print("Extracted scripts/lesson_video.js")
else:
    print("Could not find Video JS start")

# 2. Extract Blocks Puzzle Logic
# Pattern: (function() { ... const BOARD_SIZE = 10; ... })();
puzzle_start_marker = "(function() {"
puzzle_inner_marker = "const BOARD_SIZE = 10;"
puzzle_end_marker = "})();"

# Find the IIFE that contains BOARD_SIZE
# We can use regex or just search
regex_puzzle = r"\(function\(\)\s*\{[\s\S]*?const BOARD_SIZE = \d+;[\s\S]*?\}\)\(\);"
match = re.search(regex_puzzle, content)

if match:
    puzzle_js_content = match.group(0)
    with open("scripts/blocks_puzzle.js", "w", encoding="utf-8") as f:
        f.write(puzzle_js_content)
    print("Extracted scripts/blocks_puzzle.js")
else:
    # Try finding via index
    p_start = content.find("const grid = Array(BOARD_SIZE).fill().map(() => Array(BOARD_SIZE).fill(0));")
    # This is inside.
    # Let's try to find the wrapping function
    print("Could not find Blocks Puzzle JS via regex")

# 3. Extract CSS
# Pattern: /* Fixed Practices Menu CSS */ ...
css_start_tag = "/* Fixed Practices Menu CSS */"
css_end_tag = ".Practices-panel a:hover {"
# We need to capture until the closing brace of the last rule
css_pattern = r"/\* Fixed Practices Menu CSS \*/[\s\S]*?\.Practices-panel a:hover\s*\{[\s\S]*?\}"

search_css = re.search(css_pattern, content)
if search_css:
    css_content = search_css.group(0)
    with open("temp_nav.css", "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Extracted temp_nav.css")
else:
    print("Could not find CSS")

