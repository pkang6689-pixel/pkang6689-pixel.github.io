#!/usr/bin/env python3
import os
import re

def fix_algebra2_files():
    """Remove incorrect game buttons and add proper Practices-menu to Algebra2 files"""
    
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
            file_path = os.path.join(unit_dir, lesson_file)
            total_files += 1
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if file has the incorrect lesson-games div
                if 'class="lesson-games"' not in content:
                    continue
                
                # Remove the incorrect lesson-games div
                updated_content = re.sub(
                    r'<div class="lesson-games"[^>]*>.*?</div>\s*\n\s*',
                    '',
                    content,
                    flags=re.DOTALL
                )
                
                # Check if this is a Practice file
                is_practice = 'Practice' in lesson_file
                
                if is_practice:
                    # For Practice files, add the Practices-menu inside Practice-actions div
                    if 'class="Practices-menu"' not in updated_content:
                        # Insert the menu button/panel inside Practice-actions, before the quiz link
                        menu_html = '''<div class="Practices-menu" style="position:relative; margin-right: 1rem;">
<button class="side-button view-other-Practices" onclick="togglePracticesPanel(this)" type="button">Other games</button>
<div aria-hidden="true" class="Practices-panel">
<div class="Practices-panel-item">
<a href="#flashcard-game">Flashcard Game</a>
</div>
<div class="Practices-panel-item">
<a href="#climb">Boost</a>
</div>
<div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div>
<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>
</div>
</div>
'''
                        updated_content = re.sub(
                            r'(<div class="Practice-actions"[^>]*>\n)',
                            r'\1' + menu_html,
                            updated_content
                        )
                else:
                    # For Summary/Quiz/Video files, add the menu before closing diagram-card
                    if 'class="Practices-menu"' not in updated_content:
                        menu_html = '''<div class="Practices-menu" style="position:relative; margin-right: 1rem;">
<button class="side-button view-other-Practices" onclick="togglePracticesPanel(this)" type="button">Other games</button>
<div aria-hidden="true" class="Practices-panel">
<div class="Practices-panel-item">
<a href="#flashcard-game">Flashcard Game</a>
</div>
<div class="Practices-panel-item">
<a href="#climb">Boost</a>
</div>
<div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div>
<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>
</div>
</div>
'''
                        # Add after the summary-actions/actions div
                        updated_content = re.sub(
                            r'(</div>\s*</div>\s*</main>)',
                            f'\n{menu_html}\n' + r'\1',
                            updated_content
                        )
                
                # Write back the corrected content
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                print(f"Fixed: {lesson_file}")
                updated_files += 1
                
            except Exception as e:
                print(f"Error processing {lesson_file}: {e}")
    
    print(f"\nSummary: {updated_files} out of {total_files} files updated")

if __name__ == '__main__':
    fix_algebra2_files()
