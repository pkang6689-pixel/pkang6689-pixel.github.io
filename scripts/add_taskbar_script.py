#!/usr/bin/env python3
"""Add taskbar.js script tag to all HTML files that had their inline taskbar removed.

Inserts <script src="...taskbar.js"></script> just before the closing </body> or </html>,
or before the first existing <script> in the body if a better insertion point is available.
"""

import os
import glob
import re


def get_taskbar_script_path(filepath):
    """Determine the correct relative or absolute path to taskbar.js for a given file."""
    # Root-level files (e.g., /workspaces/ArisEdu/index.html)
    if '/ArisEdu/index.html' in filepath:
        return 'ArisEdu Project Folder/scripts/taskbar.js'
    
    # Top-level ArisEdu Project Folder files
    af = 'ArisEdu Project Folder/'
    if af in filepath:
        relpath = filepath.split(af, 1)[1]
        depth = relpath.count('/')
        if depth == 0:
            # e.g., Courses.html → scripts/taskbar.js
            return 'scripts/taskbar.js'
        elif depth == 1:
            # e.g., PhysicsLessons/PhysicsUnit1.html → ../scripts/taskbar.js
            return '../scripts/taskbar.js'
        elif depth == 2:
            # e.g., ChemistryLessons/Unit1/Lesson*.html → ../../scripts/taskbar.js
            return '../../scripts/taskbar.js'
    
    # Fallback absolute
    return '/ArisEdu Project Folder/scripts/taskbar.js'


def add_taskbar_script(filepath):
    """Add taskbar.js script tag to an HTML file if it doesn't already have it."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'taskbar.js' in content:
        return False  # Already has it
    
    if 'nav class="taskbar"' in content or "nav class='taskbar'" in content:
        return False  # Still has inline taskbar (shouldn't happen but skip)
    
    script_path = get_taskbar_script_path(filepath)
    script_tag = f'<script src="{script_path}"></script>\n'
    
    # Strategy: Insert right after <body...> tag
    # This ensures taskbar renders first
    body_match = re.search(r'(<body[^>]*>)(.*)', content, re.DOTALL)
    if body_match:
        # Insert after the <body> tag and any comment on same line
        body_tag = body_match.group(1)
        rest = body_match.group(2)
        
        # If there's a comment on the same line as <body>, keep it
        # e.g., <body class="dark-mode h-full"><!-- Taskbar -->
        lines_after = rest.split('\n', 1)
        first_line = lines_after[0]
        remaining = lines_after[1] if len(lines_after) > 1 else ''
        
        new_content = content[:body_match.start()] + body_tag + first_line + '\n' + script_tag + remaining
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False


def main():
    all_files = []
    
    # Chemistry lessons (non-Practice since those were already done)
    chem_root = "/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons"
    for f in sorted(glob.glob(os.path.join(chem_root, "**", "*.html"), recursive=True)):
        if 'Practice.html' in f:
            continue
        all_files.append(f)
    
    # Physics lessons
    phys_root = "/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons"
    for f in sorted(glob.glob(os.path.join(phys_root, "**", "*.html"), recursive=True)):
        all_files.append(f)
    
    # Top-level files
    top_dir = "/workspaces/ArisEdu/ArisEdu Project Folder"
    top_files = [
        "algebra1.html", "algebra2.html", "bio.html", "chem.html",
        "Courses.html", "geometry.html", "LoginSignup.html",
        "physics.html", "Play.html", "template.html",
        "GameBlocks.html", "GameMatch.html",
    ]
    for name in top_files:
        fp = os.path.join(top_dir, name)
        if os.path.isfile(fp):
            all_files.append(fp)
    
    # Root index.html
    root_index = "/workspaces/ArisEdu/index.html"
    if os.path.isfile(root_index):
        all_files.append(root_index)
    
    print(f"Checking {len(all_files)} files...")
    
    added = 0
    for f in all_files:
        if add_taskbar_script(f):
            short = f.replace("/workspaces/ArisEdu/", "")
            print(f"  Added: {short}")
            added += 1
    
    print(f"\nDone! Added taskbar.js to {added} files.")


if __name__ == '__main__':
    main()
