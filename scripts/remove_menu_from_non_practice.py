#!/usr/bin/env python3
import os
import re

def remove_practices_menu_from_non_practice_files():
    """Remove Practices-menu from Summary/Quiz/Video files"""
    
    base_path = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons'
    
    total_files = 0
    updated_files = 0
    
    # Walk through all units
    for unit_num in range(1, 10):
        unit_dir = os.path.join(base_path, f'Unit{unit_num}')
        
        if not os.path.exists(unit_dir):
            continue
        
        # Find all lesson files
        lesson_files = [f for f in os.listdir(unit_dir) if f.endswith('.html')]
        
        for lesson_file in lesson_files:
            # Skip Practice files - we want to KEEP the menu in those
            if 'Practice' in lesson_file:
                continue
            
            file_path = os.path.join(unit_dir, lesson_file)
            total_files += 1
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if file has the Practices-menu
                if 'class="Practices-menu"' not in content:
                    continue
                
                # Remove the entire Practices-menu block
                updated_content = re.sub(
                    r'\n<div class="Practices-menu"[^>]*>.*?</div>\s*\n',
                    '\n',
                    content,
                    flags=re.DOTALL
                )
                
                # Write back the corrected content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                print(f"Removed menu from: {lesson_file}")
                updated_files += 1
                
            except Exception as e:
                print(f"Error processing {lesson_file}: {e}")
    
    print(f"\nSummary: {updated_files} out of {total_files} non-Practice files updated")

if __name__ == '__main__':
    remove_practices_menu_from_non_practice_files()
