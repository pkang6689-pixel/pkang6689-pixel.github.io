#!/usr/bin/env python3
"""
Cleanup script for ALL ChemistryLessons files across all units.
Fixes remaining issues:
1. Removes duplicate .mm-card <style> blocks (86 files: 75 Practice + 11 Test)
2. Removes any remaining inline script blocks (script-blockpuzzle, script-mixmatch, script-switcher)
3. Cleans up excessive blank lines
"""

import os
import re
import glob
import sys

CHEM_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ArisEdu Project Folder", "ChemistryLessons"
)


def remove_script_block(html, script_id):
    """Remove an entire <script id="SCRIPT_ID">...</script> block."""
    pattern = re.compile(
        r'<script\s+id=["\']' + re.escape(script_id) + r'["\'][^>]*>.*?</script>',
        re.DOTALL
    )
    new_html, count = pattern.subn('', html)
    return new_html, count


def remove_duplicate_mm_style(html):
    """Find <style> blocks with .mm-card and remove all duplicates (keep only first)."""
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    style_blocks = list(style_pattern.finditer(html))

    # Find which ones contain .mm-card
    mm_style_blocks = [m for m in style_blocks if '.mm-card' in m.group()]

    if len(mm_style_blocks) <= 1:
        return html, 0

    # Remove all after the first (process in reverse to preserve positions)
    removed = 0
    for m in reversed(mm_style_blocks[1:]):
        html = html[:m.start()] + html[m.end():]
        removed += 1

    return html, removed


def clean_blank_lines(html):
    """Reduce multiple consecutive blank lines to at most 2."""
    return re.sub(r'\n{4,}', '\n\n\n', html)


def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    html = original
    changes = []

    # 1. Remove any remaining inline script blocks
    for script_id in ['script-blockpuzzle', 'script-mixmatch', 'script-switcher']:
        html, count = remove_script_block(html, script_id)
        if count > 0:
            changes.append(f"  Removed <script id=\"{script_id}\"> ({count})")

    # 2. Remove duplicate .mm-card style blocks
    html, count = remove_duplicate_mm_style(html)
    if count > 0:
        changes.append(f"  Removed {count} duplicate .mm-card <style> block(s)")

    # 3. Clean up excessive blank lines
    html = clean_blank_lines(html)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return changes
    return []


def main():
    # Find ALL HTML files across all units (exclude Archive and Templates)
    files = sorted(glob.glob(os.path.join(CHEM_DIR, "Unit*", "*.html")))
    files = [f for f in files if 'Archive' not in f and '_Templates' not in f]

    if not files:
        print("No HTML files found!")
        return

    total_changes = 0
    files_changed = 0

    for filepath in files:
        changes = process_file(filepath)
        if changes:
            rel = os.path.relpath(filepath, CHEM_DIR)
            print(f"\n{rel}:")
            for c in changes:
                print(c)
            total_changes += len(changes)
            files_changed += 1

    print(f"\n{'='*50}")
    print(f"Total: {total_changes} changes across {files_changed}/{len(files)} files")

    # Verify: count remaining issues
    print(f"\n--- Verification ---")
    remaining_dup = 0
    remaining_inline = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        style_blocks = re.findall(r'<style>.*?</style>', html, re.DOTALL)
        mm_styles = [s for s in style_blocks if '.mm-card' in s]
        if len(mm_styles) > 1:
            remaining_dup += 1
        
        for sid in ['script-blockpuzzle', 'script-mixmatch', 'script-switcher']:
            if f'id="{sid}"' in html or f"id='{sid}'" in html:
                remaining_inline += 1

    print(f"Remaining duplicate .mm-card CSS: {remaining_dup} files")
    print(f"Remaining inline scripts: {remaining_inline} files")


if __name__ == "__main__":
    main()
