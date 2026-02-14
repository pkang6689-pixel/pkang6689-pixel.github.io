#!/usr/bin/env python3
"""
Cleanup script for Unit1 ChemistryLessons files.
Removes inline script blocks that duplicate shared JS files:
- <script id="script-blockpuzzle">...</script>  (~500 lines each)
- <script id="script-mixmatch">...</script>      (~77 lines each)
- <script id="script-switcher">...</script>       (~60 lines each)

Also removes game HTML containers from Summary/Quiz files
(mixmatch-container, blockpuzzle-container) since those page types
shouldn't have games (matching cleanup already done in Units 2-12).

Also removes duplicate <style> blocks with .mm-card CSS in Practice files.
"""

import os
import re
import glob

CHEM_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ArisEdu Project Folder", "ChemistryLessons"
)

def remove_script_block(html, script_id):
    """Remove an entire <script id="SCRIPT_ID">...</script> block."""
    # Match <script id="script_id"> or <script id="script_id" ...>
    pattern = re.compile(
        r'<script\s+id=["\']' + re.escape(script_id) + r'["\'][^>]*>.*?</script>',
        re.DOTALL
    )
    new_html, count = pattern.subn('', html)
    return new_html, count


def remove_div_container(html, container_id):
    """Remove a <div id="container_id" ...>...</div> block, handling nested divs."""
    # Find the opening tag
    pattern = re.compile(
        r'<div\s+id=["\']' + re.escape(container_id) + r'["\']',
        re.IGNORECASE
    )
    match = pattern.search(html)
    if not match:
        return html, 0

    start_pos = match.start()

    # Now we need to find the matching closing </div>
    # Track nesting depth
    pos = match.end()
    depth = 1
    div_open = re.compile(r'<div[\s>]', re.IGNORECASE)
    div_close = re.compile(r'</div\s*>', re.IGNORECASE)

    while depth > 0 and pos < len(html):
        next_open = div_open.search(html, pos)
        next_close = div_close.search(html, pos)

        if next_close is None:
            break

        if next_open and next_open.start() < next_close.start():
            depth += 1
            pos = next_open.end()
        else:
            depth -= 1
            pos = next_close.end()

    if depth == 0:
        # Remove the entire block
        end_pos = pos
        new_html = html[:start_pos] + html[end_pos:]
        return new_html, 1

    return html, 0


def remove_duplicate_mm_style(html):
    """Remove the second duplicate <style> block containing .mm-card CSS."""
    # Find all <style>...</style> blocks that contain .mm-card
    pattern = re.compile(r'<style>\s*(/\*.*?\*/)?\s*\.mm-card\s*\{.*?</style>', re.DOTALL)
    matches = list(pattern.finditer(html))

    if len(matches) <= 1:
        return html, 0

    # Remove all but the first
    removed = 0
    for m in reversed(matches[1:]):
        html = html[:m.start()] + html[m.end():]
        removed += 1

    return html, removed


def remove_duplicate_mm_style_v2(html):
    """More robust: find <style> blocks with .mm-card and remove duplicates."""
    # Find all style blocks
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    style_blocks = list(style_pattern.finditer(html))

    # Find which ones contain .mm-card
    mm_style_blocks = [m for m in style_blocks if '.mm-card' in m.group()]

    if len(mm_style_blocks) <= 1:
        return html, 0

    # Remove all after the first
    removed = 0
    for m in reversed(mm_style_blocks[1:]):
        html = html[:m.start()] + html[m.end():]
        removed += 1

    return html, removed


def clean_blank_lines(html):
    """Reduce multiple consecutive blank lines to at most 2."""
    return re.sub(r'\n{4,}', '\n\n\n', html)


def process_file(filepath):
    """Process a single HTML file and remove inline duplicated code."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    html = original
    changes = []

    # Determine file type
    basename = os.path.basename(filepath)
    is_practice = '_Practice.html' in basename
    is_video = '_Video.html' in basename
    is_summary = '_Summary.html' in basename
    is_quiz = '_Quiz.html' in basename

    # 1. Remove inline script blocks (all file types)
    for script_id in ['script-blockpuzzle', 'script-mixmatch', 'script-switcher']:
        html, count = remove_script_block(html, script_id)
        if count > 0:
            changes.append(f"  Removed <script id=\"{script_id}\"> ({count} block(s))")

    # 2. For Summary/Quiz/Video files: remove game HTML containers
    if is_summary or is_quiz:
        for container_id in ['mixmatch-container', 'blockpuzzle-container']:
            html, count = remove_div_container(html, container_id)
            if count > 0:
                changes.append(f"  Removed <div id=\"{container_id}\">")

    # 3. For Practice files: remove duplicate .mm-card style blocks
    if is_practice:
        html, count = remove_duplicate_mm_style_v2(html)
        if count > 0:
            changes.append(f"  Removed {count} duplicate .mm-card <style> block(s)")

    # Clean up excessive blank lines
    html = clean_blank_lines(html)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return changes
    return []


def main():
    # Find all Unit1 HTML files (the only ones with inline scripts)
    unit1_dir = os.path.join(CHEM_DIR, "Unit1")
    files = sorted(glob.glob(os.path.join(unit1_dir, "*.html")))

    if not files:
        print("No HTML files found in Unit1!")
        return

    total_changes = 0
    for filepath in files:
        changes = process_file(filepath)
        if changes:
            print(f"\n{os.path.basename(filepath)}:")
            for c in changes:
                print(c)
            total_changes += len(changes)
        else:
            print(f"{os.path.basename(filepath)}: No changes needed")

    print(f"\n{'='*50}")
    print(f"Total: {total_changes} changes across {len(files)} files")

    # Show before/after line counts
    print(f"\nLine counts after cleanup:")
    for filepath in files:
        with open(filepath, 'r') as f:
            lines = len(f.readlines())
        print(f"  {os.path.basename(filepath)}: {lines} lines")


if __name__ == "__main__":
    main()
