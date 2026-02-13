#!/usr/bin/env python3
"""Remove inline taskbar HTML and JS from Practice.html files.

Removes:
1. <nav class="taskbar">...</nav> HTML block
2. Taskbar Button Handlers + dark mode init inside the DOMContentLoaded <script>
3. Standalone <script> blocks: login-signup-account-display, settings-menu-align, dark-mode-sync
"""

import os
import re
import glob

ROOT = "/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons"


def remove_nav_block(lines):
    """Remove <nav class='taskbar'>...</nav> block."""
    out = []
    inside_nav = False
    for line in lines:
        if '<nav class="taskbar">' in line:
            inside_nav = True
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
    depth = 0  # track script open/close tags
    for line in lines:
        stripped = line.strip()
        if not skip_block:
            # Check if this is a <script> line before one of our marker comments
            if stripped == '<script>':
                # Peek ahead: is the next non-empty line one of our markers?
                idx = len(out)  # current position in output
                # We need to look ahead in the original lines
                orig_idx = lines.index(line, len(lines) - len(lines) + sum(1 for _ in out) if False else 0)
                # Simpler: just buffer and check
                out.append(line)
                continue
            for marker in markers:
                if marker in stripped:
                    # Found a marker - remove this entire <script>...</script> block
                    # First, remove the preceding <script> tag that's already in out
                    while out and out[-1].strip() == '':
                        out.pop()  # remove blank lines
                    if out and '<script>' in out[-1]:
                        out.pop()  # remove the <script> tag
                    skip_block = True
                    break
            if not skip_block:
                out.append(line)
        else:
            # We're inside a block to skip - look for closing </script>
            if '</script>' in stripped:
                skip_block = False
            # Don't append anything while skipping
    return out


def remove_taskbar_handlers_from_domready(lines):
    """Remove taskbar handler code from inside the DOMContentLoaded <script> block.
    
    Removes everything from '// Ensure dark mode on load' through
    '// Set dark mode active by default' + its body, up to the closing </script>.
    """
    out = []
    skip_taskbar_section = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Start skipping at "// Ensure dark mode on load"
        if '// Ensure dark mode on load' in stripped:
            skip_taskbar_section = True
            continue
        
        # Also catch "// Taskbar Button Handlers" in case Ensure dark mode isn't present
        if '// Taskbar Button Handlers' in stripped and not skip_taskbar_section:
            skip_taskbar_section = True
            continue
        
        if skip_taskbar_section:
            # Stop skipping when we hit the closing </script> for this block
            if '</script>' in stripped:
                skip_taskbar_section = False
                out.append(line)  # Keep the </script> tag
                continue
            # Skip all taskbar handler lines
            continue
        
        out.append(line)
    
    return out


def clean_empty_script_blocks(lines):
    """Remove <script>...</script> blocks that are now empty (only whitespace)."""
    out = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped == '<script>':
            # Collect everything until </script>
            block = [lines[i]]
            j = i + 1
            while j < len(lines) and '</script>' not in lines[j].strip():
                block.append(lines[j])
                j += 1
            if j < len(lines):
                block.append(lines[j])
                j += 1
            # Check if inner content is empty/whitespace only
            inner = ''.join(block[1:-1]).strip()
            if inner == '':
                # Skip this empty block
                i = j
                continue
        out.append(lines[i])
        i += 1
    return out


def process_file(filepath):
    """Process a single Practice.html file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    original_count = len(lines)
    
    # Step 1: Remove <nav class="taskbar">...</nav>
    lines = remove_nav_block(lines)
    
    # Step 2: Remove taskbar handlers from DOMContentLoaded script
    lines = remove_taskbar_handlers_from_domready(lines)
    
    # Step 3: Remove standalone script blocks
    lines = remove_standalone_script_blocks(lines)
    
    # Step 4: Clean up any now-empty script blocks
    lines = clean_empty_script_blocks(lines)
    
    removed = original_count - len(lines)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return removed


def main():
    # Find all Practice.html files
    pattern = os.path.join(ROOT, "**", "*Practice.html")
    files = sorted(glob.glob(pattern, recursive=True))
    
    print(f"Found {len(files)} Practice.html files")
    
    total_removed = 0
    for f in files:
        removed = process_file(f)
        short = f.replace(ROOT + "/", "")
        print(f"  {short}: removed {removed} lines")
        total_removed += removed
    
    print(f"\nDone! Removed {total_removed} total lines across {len(files)} files.")


if __name__ == '__main__':
    main()
