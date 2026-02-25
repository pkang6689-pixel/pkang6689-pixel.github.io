#!/usr/bin/env python3
import os
import re

def remove_all_practices_menu():
    """Thoroughly remove all Practices-menu blocks from non-Practice files"""
    
    base_path = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons'
    
    updated_count = 0
    
    # Walk through all units
    for unit_num in range(1, 10):
        unit_dir = os.path.join(base_path, f'Unit{unit_num}')
        
        if not os.path.exists(unit_dir):
            continue
        
        # Find all lesson files
        lesson_files = [f for f in os.listdir(unit_dir) if f.endswith('.html')]
        
        for lesson_file in lesson_files:
            # Skip Practice files
            if 'Practice' in lesson_file:
                continue
            
            file_path = os.path.join(unit_dir, lesson_file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Remove the entire Practices-menu div block - multiple attempts with different patterns
                # Pattern 1: Multi-line with proper nesting
                content = re.sub(
                    r'<div class="Practices-menu"[^>]*>.*?</div>\s*(?=<)',
                    '',
                    content,
                    flags=re.DOTALL
                )
                
                # If content changed, write it back
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Cleaned: {lesson_file}")
                    updated_count += 1
                    
            except Exception as e:
                print(f"Error processing {lesson_file}: {e}")
    
    print(f"\nTotal files cleaned: {updated_count}")

if __name__ == '__main__':
    remove_all_practices_menu()
