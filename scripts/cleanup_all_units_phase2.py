#!/usr/bin/env python3
"""
Cleanup script for ALL ChemistryLessons files - Phase 2.
Removes ALL remaining inline .mm-card <style> blocks since main.css already
has these styles.

Also removes inline climb game CSS from Practice files since it's 
duplicated across all of them.
"""

import os
import re
import glob

CHEM_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ArisEdu Project Folder", "ChemistryLessons"
)


def remove_all_mm_styles(html):
    """Remove ALL <style> blocks containing .mm-card CSS (already in main.css)."""
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    style_blocks = list(style_pattern.finditer(html))

    mm_style_blocks = [m for m in style_blocks if '.mm-card' in m.group()]

    if not mm_style_blocks:
        return html, 0

    removed = 0
    for m in reversed(mm_style_blocks):
        html = html[:m.start()] + html[m.end():]
        removed += 1

    return html, removed


def remove_climb_css(html):
    """Remove inline <style> blocks containing climb game CSS (twinkle, floatPlanet, slideLadder, climb-option-btn)."""
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    style_blocks = list(style_pattern.finditer(html))

    climb_indicators = ['climb-option-btn', 'floatPlanet', 'slideLadder', '@keyframes twinkle']
    climb_blocks = [m for m in style_blocks if any(ind in m.group() for ind in climb_indicators)]

    if not climb_blocks:
        return html, 0

    removed = 0
    for m in reversed(climb_blocks):
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

    # 1. Remove ALL .mm-card style blocks (already in main.css)
    html, count = remove_all_mm_styles(html)
    if count > 0:
        changes.append(f"  Removed {count} .mm-card <style> block(s)")

    # 2. Remove climb game CSS (duplicated in every Practice file)
    html, count = remove_climb_css(html)
    if count > 0:
        changes.append(f"  Removed {count} climb game <style> block(s)")

    # 3. Clean up excessive blank lines
    html = clean_blank_lines(html)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return changes
    return []


def main():
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
            print(f"{rel}: {', '.join(c.strip() for c in changes)}")
            total_changes += len(changes)
            files_changed += 1

    print(f"\n{'='*50}")
    print(f"Total: {total_changes} changes across {files_changed}/{len(files)} files")

    # Verify
    remaining_mm = 0
    remaining_climb = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        style_blocks = re.findall(r'<style>.*?</style>', html, re.DOTALL)
        for s in style_blocks:
            if '.mm-card' in s:
                remaining_mm += 1
            if 'climb-option-btn' in s:
                remaining_climb += 1

    print(f"\n--- Verification ---")
    print(f"Remaining inline .mm-card CSS: {remaining_mm}")
    print(f"Remaining inline climb CSS: {remaining_climb}")


if __name__ == "__main__":
    main()
