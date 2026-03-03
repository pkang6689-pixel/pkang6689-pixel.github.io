#!/usr/bin/env python3
"""
Update AP course selector files to link to _Video.html instead of _Practice.html
"""

import os
from pathlib import Path

def update_ap_course_files():
    """Update all AP course HTML files to link to Video instead of Practice"""
    base_path = Path("ArisEdu Project Folder")
    
    ap_files = [
        "ap_biology.html",
        "ap_calculus.html",
        "ap_chemistry.html",
        "ap_environmental_science.html",
        "ap_hug.html",
        "ap_physics1.html",
        "ap_physics2.html",
        "ap_physics_mechanics.html",
        "ap_statistics.html"
    ]
    
    fixed_count = 0
    
    for ap_file in ap_files:
        ap_file_path = base_path / ap_file
        
        if not ap_file_path.exists():
            print(f"[SKIP] {ap_file} not found")
            continue
        
        try:
            with open(ap_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace _Practice.html with _Video.html in the lesson link
            # Look for pattern: APLessons/.../${lessonText} where lessonText includes _Practice.html
            original_content = content
            
            # Find the section where lessonText is constructed
            # It should be something like: let lessonText = `Lesson${unitNum}.${lessonNum}_Practice.html`;
            content = content.replace(
                '`Lesson${unitNum}.${lessonNum}_Practice.html`',
                '`Lesson${unitNum}.${lessonNum}_Video.html`'
            )
            
            if content != original_content:
                with open(ap_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"[OK] {ap_file} - Updated to link to _Video.html")
                fixed_count += 1
            else:
                print(f"[SKIP] {ap_file} - No changes needed")
        
        except Exception as e:
            print(f"[ERROR] {ap_file}: {e}")
    
    print(f"\n{'='*50}")
    print(f"Updated {fixed_count}/9 AP course files")
    print(f"{'='*50}")

def main():
    workspace_root = Path(__file__).parent
    os.chdir(workspace_root)
    update_ap_course_files()
    print("\nAP course lesson links have been updated to start with Video!")

if __name__ == "__main__":
    main()
