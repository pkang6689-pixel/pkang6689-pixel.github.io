#!/usr/bin/env python3
"""
Fix quiz answer checking and add game navigation buttons to all lesson files.
"""

import os
import re

def fix_quiz_files():
    """Fix the quiz onclick handlers in all quiz files."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    
    # Fix onclick handlers to check actual selected value instead of hardcoded 'wrong'
    for unit in range(1, 10):
        if unit == 2:
            lesson_count = 7
        elif unit == 4:
            lesson_count = 6
        elif unit == 6:
            lesson_count = 5
        elif unit == 7:
            lesson_count = 7
        elif unit == 8:
            lesson_count = 6
        elif unit == 9:
            lesson_count = 4
        else:
            lesson_count = 9
        
        for lesson in range(1, lesson_count + 1):
            file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Quiz.html"
            
            if not os.path.exists(file_path):
                continue
            
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Replace onclick handlers: onclick="window.checkQuizAnswer('qX', 'wrong', this)"
            # with proper function that gets the selected value
            pattern = r'onclick="window\.checkQuizAnswer\(\'(q\d+)\', \'wrong\', this\)"'
            
            def replace_onclick(match):
                q_id = match.group(1)
                return f'onclick="window.checkQuiz(\'{q_id}\')"'
            
            new_content = re.sub(pattern, replace_onclick, content)
            
            with open(file_path, 'w') as f:
                f.write(new_content)
            
            print(f"Fixed: Unit {unit} Lesson {unit}.{lesson}")

def add_game_buttons():
    """Add game navigation buttons to all lesson files."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    
    game_buttons_html = '''
<div class="lesson-games" style="margin-top: 2rem; padding: 1rem; background: #1e293b; border-radius: 0.5rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1rem;">
    <a href="../../GameBlocks.html" class="action-button" style="text-align: center; text-decoration: none; display: flex; align-items: center; justify-content: center;">Block Puzzle</a>
    <a href="../../GameMatch.html" class="action-button" style="text-align: center; text-decoration: none; display: flex; align-items: center; justify-content: center;">Memory Match</a>
    <a href="../../Play.html" class="action-button" style="text-align: center; text-decoration: none; display: flex; align-items: center; justify-content: center;">Unit Tests</a>
</div>
'''
    
    for unit in range(1, 10):
        if unit == 2:
            lesson_count = 7
        elif unit == 4:
            lesson_count = 6
        elif unit == 6:
            lesson_count = 5
        elif unit == 7:
            lesson_count = 7
        elif unit == 8:
            lesson_count = 6
        elif unit == 9:
            lesson_count = 4
        else:
            lesson_count = 9
        
        for lesson in range(1, lesson_count + 1):
            # Update all 4 file types for each lesson
            for file_type in ['Summary', 'Practice', 'Quiz', 'Video']:
                file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_{file_type}.html"
                
                if not os.path.exists(file_path):
                    continue
                
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Check if game buttons already exist
                if 'class="lesson-games"' in content:
                    print(f"Skipped (already has buttons): Unit {unit} Lesson {unit}.{lesson} {file_type}")
                    continue
                
                # Add game buttons before closing actions div
                # Find the last actions div and insert after it
                pattern = r'(<div class="(?:summary|Practice|quiz)-actions"[^>]*>.*?</div>)'
                
                if re.search(pattern, content, re.DOTALL):
                    new_content = re.sub(
                        pattern,
                        lambda m: m.group(1) + game_buttons_html,
                        content,
                        count=1,
                        flags=re.DOTALL
                    )
                else:
                    # If no actions div found, add before closing main
                    new_content = content.replace(
                        '</main>',
                        game_buttons_html + '\n    </main>'
                    )
                
                with open(file_path, 'w') as f:
                    f.write(new_content)
                
                print(f"Updated: Unit {unit} Lesson {unit}.{lesson} {file_type}")

if __name__ == "__main__":
    print("Fixing quiz answer checking...")
    fix_quiz_files()
    print("\nAdding game navigation buttons...")
    add_game_buttons()
    print("\nDone!")
