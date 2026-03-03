#!/usr/bin/env python3
"""
Update ap_physics1.html to link to _Video.html files
"""

import re
from pathlib import Path

def update_physics1_links():
    """Update all lesson links in ap_physics1.html to use _Video.html"""
    file_path = Path("ArisEdu Project Folder/ap_physics1.html")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace all patterns like 'APPhys1_Lessons/Unit#/Lesson#.#.html' with '_Video.html'
    # Pattern: 'APPhys1_Lessons/Unit(\d+)/Lesson(\d+\.\d+)\.html'
    content = re.sub(
        r"'APPhys1_Lessons/Unit(\d+)/Lesson(\d+\.\d+)\.html'",
        r"'APPhys1_Lessons/Unit\1/Lesson\2_Video.html'",
        content
    )
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("[OK] ap_physics1.html updated - all lesson links now point to _Video.html")
    else:
        print("[SKIP] ap_physics1.html - no changes needed")

def main():
    update_physics1_links()

if __name__ == "__main__":
    main()
