#!/usr/bin/env python3
"""
Split every Unit*_Test.html into two files:
  - Unit*_Test_Practice.html  (flashcards + link to test)
  - Unit*_Test.html           (quiz only, visible by default)

The original file is overwritten with the quiz-only version.
"""

import os
import re
import glob

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder"

def detect_course_info(filepath):
    """Detect course name and back URL from file path."""
    fp = filepath.replace("\\", "/")
    if "Algebra1Lessons" in fp:
        return "Algebra 1", "../../algebra1.html", "algebra1"
    elif "Algebra2Lessons" in fp:
        return "Algebra 2", "../../algebra2.html", "algebra2"
    elif "GeometryLessons" in fp:
        return "Geometry", "../../geometry.html", "geometry"
    elif "PhysicsLessons" in fp:
        return "Physics", "../../physics.html", "physics"
    elif "ChemistryLessons" in fp:
        return "Chemistry", "../../chem.html", "chemistry"
    elif "BiologyLessons" in fp:
        return "Biology", "../../bio.html", "biology"
    return "Course", "../../index.html", "course"

def extract_unit_number(filepath):
    """Extract unit number from filename."""
    m = re.search(r'Unit(\w+)_Test\.html$', os.path.basename(filepath))
    return m.group(1) if m else "?"

def find_flashcard_data(content):
    """Extract the window.lessonFlashcards script block."""
    # Match the script tag containing lessonFlashcards
    pattern = r'<script>\s*\n?\s*window\.lessonFlashcards\s*=\s*\[.*?\];\s*\n?\s*</script>'
    m = re.search(pattern, content, re.DOTALL)
    if m:
        return m.group(0)
    
    # Try alternate pattern with leading whitespace
    pattern2 = r'<script>\s*\n\s*window\.lessonFlashcards\s*=\s*\[[\s\S]*?\];\s*\n\s*</script>'
    m2 = re.search(pattern2, content, re.DOTALL)
    if m2:
        return m2.group(0)
    
    return None

def find_head_section(content):
    """Extract the <head> section content."""
    m = re.search(r'<head[^>]*>(.*?)</head>', content, re.DOTALL)
    return m.group(1) if m else ""

def find_practice_view(content):
    """Extract the practice-content-view div."""
    # Find <div id="practice-content-view"> ... </div> (before quiz-content-view)
    start_marker = '<div id="practice-content-view">'
    idx = content.find(start_marker)
    if idx == -1:
        return None, -1, -1
    
    # Find the matching closing </div> by tracking nesting
    # The practice view ends right before quiz-content-view starts
    quiz_marker = '<div id="quiz-content-view"'
    quiz_idx = content.find(quiz_marker, idx)
    if quiz_idx == -1:
        return None, -1, -1
    
    # The practice div content is between idx and quiz_idx
    # We need to find where the practice div actually closes
    # Walk backwards from quiz_idx to find the closing tag
    practice_html = content[idx:quiz_idx].rstrip()
    
    return practice_html, idx, quiz_idx

def find_quiz_view(content):
    """Extract the quiz-content-view div and everything in <main> after it."""
    quiz_marker_patterns = [
        '<div id="quiz-content-view">',
        '<div id="quiz-content-view" style="display:none;">',
        '<div id="quiz-content-view" style="display: none;">',
    ]
    
    for pattern in quiz_marker_patterns:
        idx = content.find(pattern)
        if idx != -1:
            # Find </main> to get the extent
            main_end = content.find('</main>', idx)
            if main_end != -1:
                return content[idx:main_end], idx
    
    return None, -1

def extract_bottom_scripts(content):
    """Extract all script tags after </main>."""
    main_end = content.find('</main>')
    if main_end == -1:
        return []
    
    after_main = content[main_end + len('</main>'):]
    # Find all script tags
    scripts = re.findall(r'<script[^>]*>.*?</script>', after_main, re.DOTALL)
    # Also find standalone script src tags
    script_srcs = re.findall(r'<script\s+src="[^"]*"></script>', after_main)
    
    # Return the raw text after </main> up to </body>
    body_end = after_main.find('</body>')
    if body_end != -1:
        return after_main[:body_end].strip()
    return after_main.strip()

def get_head_scripts(head_content):
    """Get just the scripts and links from head."""
    return head_content

def build_practice_file(filepath, content, unit_num, course_name, back_url):
    """Build the practice-only HTML file."""
    head_content = find_head_section(content)
    practice_html, _, _ = find_practice_view(content)
    flashcard_data = find_flashcard_data(content)
    
    if not practice_html:
        print(f"  WARNING: No practice-content-view found in {filepath}")
        return None
    
    test_filename = os.path.basename(filepath)  # e.g., Unit1_Test.html
    
    # Fix the "Start Unit Test" button to link to the test file instead of toggling views
    # Replace any inline JS that toggles views with a link to the test file
    practice_html = re.sub(
        r'''onclick="document\.getElementById\('practice-content-view'\)\.style\.display='none';document\.getElementById\('quiz-content-view'\)\.style\.display='block';"''',
        f'''onclick="window.location.href='{test_filename}'"''',
        practice_html
    )
    # Also handle showQuiz() onclick
    practice_html = re.sub(
        r'''onclick="showQuiz\(\)"''',
        f'''onclick="window.location.href='{test_filename}'"''',
        practice_html
    )

    # Update the title
    title = f"Unit {unit_num}: Unit Test Practice"
    
    # Determine script paths based on what exists in the original
    # Check for ../../scripts/ pattern vs /ArisEdu Project Folder/scripts/
    uses_relative = '../../scripts/' in content
    
    # Build script section - need practice_games for flashcards
    scripts_section = ""
    if flashcard_data:
        scripts_section += flashcard_data + "\n"
    
    # Add necessary scripts
    script_tags_in_original = re.findall(r'<script\s+src="([^"]*)"[^>]*></script>', content)
    
    practice_scripts = []
    for src in script_tags_in_original:
        if any(x in src for x in ['practice_games', 'block_puzzle', 'blocks_puzzle', 'game_utils', 'dev_tools']):
            practice_scripts.append(f'<script src="{src}"></script>')
    
    # Also need search scripts
    for src in script_tags_in_original:
        if any(x in src for x in ['search_data', 'search_logic']):
            practice_scripts.append(f'<script src="{src}"></script>')

    scripts_section += "\n".join(practice_scripts)

    # Build the page - reuse head from original
    html = f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
{head_content.strip()}
</head>
<body class="dark-mode h-full">
<script src="../../scripts/taskbar.js"></script>
<main class="main-container">
{practice_html}
</main>
{scripts_section}
</body>
</html>
'''
    return html

def build_test_file(filepath, content, unit_num, course_name, back_url, course_key):
    """Build the test-only HTML file."""
    head_content = find_head_section(content)
    quiz_html, _ = find_quiz_view(content)
    
    if not quiz_html:
        print(f"  WARNING: No quiz-content-view found in {filepath}")
        return None
    
    # Make quiz visible by default (remove display:none)
    quiz_html = quiz_html.replace('style="display:none;"', '')
    quiz_html = quiz_html.replace('style="display: none;"', '')
    quiz_html = quiz_html.replace("style='display:none;'", '')
    
    # Get the title
    title = f"Unit {unit_num}: Unit Test"
    
    # Get script tags from original (exclude practice-specific ones and flashcard data)
    after_main = content[content.find('</main>'):] if '</main>' in content else ''
    body_end_idx = after_main.find('</body>')
    if body_end_idx != -1:
        scripts_raw = after_main[len('</main>'):body_end_idx].strip()
    else:
        scripts_raw = after_main[len('</main>'):].strip()
    
    # Remove the lessonFlashcards script block from scripts
    scripts_raw = re.sub(
        r'<script>\s*\n?\s*window\.lessonFlashcards\s*=\s*\[[\s\S]*?\];\s*\n?\s*</script>',
        '',
        scripts_raw
    ).strip()
    
    # Remove practice_games script (not needed for test-only)
    scripts_raw = re.sub(r'<script\s+src="[^"]*practice_games[^"]*"></script>\s*', '', scripts_raw)
    scripts_raw = re.sub(r'<script\s+src="[^"]*block_puzzle[^"]*"></script>\s*', '', scripts_raw)
    scripts_raw = re.sub(r'<script\s+src="[^"]*blocks_puzzle[^"]*"></script>\s*', '', scripts_raw)
    
    # Add a "Back to Practice" button at the top of quiz
    practice_filename = os.path.basename(filepath).replace('_Test.html', '_Test_Practice.html')
    
    # Add navigation button at the top
    nav_bar = f'''<div style="display:flex;gap:1rem;margin-bottom:1rem;flex-wrap:wrap;">
  <button class="side-button" onclick="window.location.href='{practice_filename}'" style="font-size:0.9rem;padding:0.5rem 1rem;">← Back to Practice</button>
  <button class="side-button" onclick="window.location.href='{back_url}'" style="font-size:0.9rem;padding:0.5rem 1rem;">Back to {course_name}</button>
</div>'''
    
    # Insert nav bar after the page-title h2
    quiz_html_modified = re.sub(
        r'(<h2 class="page-title">[^<]*</h2>)',
        r'\1\n' + nav_bar,
        quiz_html,
        count=1
    )
    
    html = f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
{head_content.strip()}
</head>
<body class="dark-mode h-full">
<script src="../../scripts/taskbar.js"></script>
<main class="main-container">
{quiz_html_modified}
</main>
{scripts_raw}
</body>
</html>
'''
    return html


def process_file(filepath):
    """Process a single unit test file."""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    unit_num = extract_unit_number(filepath)
    course_name, back_url, course_key = detect_course_info(filepath)
    
    # Build practice file
    practice_html = build_practice_file(filepath, content, unit_num, course_name, back_url)
    if practice_html is None:
        print(f"  SKIPPED: Could not build practice file")
        return False
    
    # Build test file
    test_html = build_test_file(filepath, content, unit_num, course_name, back_url, course_key)
    if test_html is None:
        print(f"  SKIPPED: Could not build test file")
        return False
    
    # Write practice file
    practice_path = filepath.replace('_Test.html', '_Test_Practice.html')
    with open(practice_path, 'w', encoding='utf-8') as f:
        f.write(practice_html)
    print(f"  Created: {os.path.basename(practice_path)}")
    
    # Overwrite original with test-only version
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(test_html)
    print(f"  Updated: {os.path.basename(filepath)} (quiz only)")
    
    return True


def main():
    pattern = os.path.join(BASE, "**", "Unit*_Test.html")
    files = sorted(glob.glob(pattern, recursive=True))
    
    print(f"Found {len(files)} unit test files to split.\n")
    
    success = 0
    failed = 0
    
    for f in files:
        if process_file(f):
            success += 1
        else:
            failed += 1
    
    print(f"\nDone! Success: {success}, Failed: {failed}")


if __name__ == "__main__":
    main()
