#!/usr/bin/env python3
"""
Cleanup Phase 3 - Remove remaining inline <style> blocks that are
already covered by main.css:
- flashcard-box dark mode CSS (Unit5A/5B Practice files)
- lesson-notes, diagram-card, summary-actions CSS
- Any remaining .mm-card or climb CSS that slipped through

Does NOT remove:
- @view-transition { navigation: auto; } (essential per-page)
- quiz-finish-screen CSS in Test files (unique/specific)
"""

import os
import re
import glob

CHEM_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "ArisEdu Project Folder", "ChemistryLessons"
)

# CSS rules that are already in main.css and can be removed from inline
MAIN_CSS_INDICATORS = [
    '.flashcard-box',
    '#shuffle-flashcard',
    '.lesson-notes',
    '.diagram-card',
    '.diagram-placeholder',
    '.summary-actions',
    '.mm-card',
    '.climb-option-btn',
    '@keyframes twinkle',
    '@keyframes floatPlanet',
    '@keyframes slideLadder',
]


def remove_redundant_styles(html):
    """Remove <style> blocks whose content is already in main.css."""
    style_pattern = re.compile(r'<style>(.*?)</style>', re.DOTALL)
    matches = list(style_pattern.finditer(html))

    removed = 0
    for m in reversed(matches):
        content = m.group(1).strip()

        # Keep @view-transition only blocks
        if content == '@view-transition { navigation: auto; }':
            continue

        # Keep blocks with @view-transition + whitespace only
        stripped = re.sub(r'@view-transition\s*\{[^}]*\}', '', content).strip()
        if not stripped:
            continue

        # Check if the block is covered by main.css
        is_redundant = any(ind in content for ind in MAIN_CSS_INDICATORS)

        if is_redundant:
            # If the block also has @view-transition, keep just that
            if '@view-transition' in content:
                html = html[:m.start()] + '<style>@view-transition { navigation: auto; }</style>' + html[m.end():]
            else:
                html = html[:m.start()] + html[m.end():]
            removed += 1

    return html, removed


def clean_blank_lines(html):
    """Reduce multiple consecutive blank lines to at most 2."""
    return re.sub(r'\n{4,}', '\n\n\n', html)


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    html = original
    changes = []

    html, count = remove_redundant_styles(html)
    if count > 0:
        changes.append(f"Removed {count} redundant <style> block(s)")

    html = clean_blank_lines(html)

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return changes
    return []


def main():
    files = sorted(glob.glob(os.path.join(CHEM_DIR, "Unit*", "*.html")))
    files = [f for f in files if 'Archive' not in f and '_Templates' not in f]

    total_changes = 0
    files_changed = 0

    for filepath in files:
        changes = process_file(filepath)
        if changes:
            rel = os.path.relpath(filepath, CHEM_DIR)
            print(f"{rel}: {', '.join(changes)}")
            total_changes += len(changes)
            files_changed += 1

    print(f"\n{'='*50}")
    print(f"Total: {total_changes} changes across {files_changed}/{len(files)} files")

    # Verify
    remaining = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        blocks = re.findall(r'<style>(.*?)</style>', html, re.DOTALL)
        for b in blocks:
            content = b.strip()
            if content == '@view-transition { navigation: auto; }':
                continue
            stripped = re.sub(r'@view-transition\s*\{[^}]*\}', '', content).strip()
            if not stripped:
                continue
            # Check if any remaining are covered by main.css
            is_redundant = any(ind in content for ind in MAIN_CSS_INDICATORS)
            if is_redundant:
                remaining += 1
                print(f"  STILL REMAINING: {os.path.basename(filepath)}")

    print(f"\nRemaining redundant styles: {remaining}")


if __name__ == "__main__":
    main()
