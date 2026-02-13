#!/usr/bin/env python3
"""Remove inline taskbar HTML and JS from ALL lesson HTML files.

Removes:
1. <nav class="taskbar">...</nav> HTML block
2. Taskbar Button Handlers + dark mode init from inline <script> blocks
3. Standalone <script> blocks: login-signup-account-display, settings-menu-align, dark-mode-sync
"""

import os
import glob


ROOTS = [
    "/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons",
    "/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons",
]

# Top-level files (not Preferences.html)
TOP_LEVEL_DIR = "/workspaces/ArisEdu/ArisEdu Project Folder"
TOP_LEVEL_FILES = [
    "algebra1.html", "algebra2.html", "bio.html", "chem.html",
    "Courses.html", "geometry.html", "LoginSignup.html",
    "physics.html", "Play.html", "template.html",
    "GameBlocks.html", "GameMatch.html",
]

ROOT_FILES = ["/workspaces/ArisEdu/index.html"]


def remove_nav_block(lines):
    """Remove <nav class='taskbar'>...</nav> block (handles both self-closing and nested)."""
    out = []
    inside_nav = False
    for line in lines:
        if '<nav class="taskbar">' in line or "<nav class='taskbar'>" in line:
            inside_nav = True
            # Check if the line before this was just a comment like <!-- Taskbar -->
            if out and '<!-- Taskbar -->' in out[-1]:
                out.pop()
            continue
        if inside_nav:
            if '</nav>' in line:
                inside_nav = False
                continue
            continue
        out.append(line)
    return out


def remove_standalone_script_blocks(lines):
    """Remove the three standalone <script> IIFEs: login-signup-account-display, settings-menu-align, dark-mode-sync."""
    markers = [
        '// login-signup-account-display',
        '// settings-menu-align',
        '// dark-mode-sync',
    ]
    out = []
    skip_block = False
    for line in lines:
        stripped = line.strip()
        if not skip_block:
            for marker in markers:
                if marker in stripped:
                    # Remove preceding <script> tag that's already in out
                    while out and out[-1].strip() == '':
                        out.pop()
                    if out and '<script>' in out[-1]:
                        out.pop()
                    skip_block = True
                    break
            if not skip_block:
                out.append(line)
        else:
            if '</script>' in stripped:
                skip_block = False
    return out


def remove_taskbar_handlers_from_domready(lines):
    """Remove taskbar handler code from inside inline <script> blocks.
    
    Removes everything from '// Ensure dark mode on load' or '// Taskbar Button Handlers'
    through the end of the <script> block (keeping the closing </script>).
    """
    out = []
    skip_section = False
    
    for line in lines:
        stripped = line.strip()
        
        if ('// Ensure dark mode on load' in stripped or 
            '// Taskbar Button Handlers' in stripped):
            skip_section = True
            continue
        
        if skip_section:
            if '</script>' in stripped:
                skip_section = False
                out.append(line)
                continue
            continue
        
        out.append(line)
    
    return out


def clean_empty_script_blocks(lines):
    """Remove <script>...</script> blocks that are now empty."""
    out = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == '<script>':
            block = [lines[i]]
            j = i + 1
            while j < len(lines) and '</script>' not in lines[j].strip():
                block.append(lines[j])
                j += 1
            if j < len(lines):
                block.append(lines[j])
                j += 1
            inner = ''.join(block[1:-1]).strip()
            if inner == '':
                i = j
                continue
        out.append(lines[i])
        i += 1
    return out


def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_count = len(lines)
    
    # Check if file actually has taskbar
    content = ''.join(lines)
    if 'nav class="taskbar"' not in content and "nav class='taskbar'" not in content:
        return 0  # Nothing to do
    
    lines = remove_nav_block(lines)
    lines = remove_taskbar_handlers_from_domready(lines)
    lines = remove_standalone_script_blocks(lines)
    lines = clean_empty_script_blocks(lines)
    
    removed = original_count - len(lines)
    
    if removed > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    return removed


def main():
    all_files = []
    
    # Lesson files (recursive)
    for root in ROOTS:
        # Exclude Practice.html files since they were already processed
        for f in sorted(glob.glob(os.path.join(root, "**", "*.html"), recursive=True)):
            if 'Practice.html' in f:
                continue  # Already processed
            all_files.append(f)
    
    # Top-level files
    for name in TOP_LEVEL_FILES:
        fp = os.path.join(TOP_LEVEL_DIR, name)
        if os.path.isfile(fp):
            all_files.append(fp)
    
    # Root files  
    for fp in ROOT_FILES:
        if os.path.isfile(fp):
            all_files.append(fp)
    
    print(f"Found {len(all_files)} files to process")
    
    total_removed = 0
    processed = 0
    for f in all_files:
        removed = process_file(f)
        if removed > 0:
            short = f.replace("/workspaces/ArisEdu/", "")
            print(f"  {short}: removed {removed} lines")
            total_removed += removed
            processed += 1
    
    print(f"\nDone! Removed {total_removed} total lines across {processed} files.")


if __name__ == '__main__':
    main()
