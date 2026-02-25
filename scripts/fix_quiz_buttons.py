#!/usr/bin/env python3
"""
Fix all quiz files - correct the button onclick handlers to always use 'correct'
"""

import os
import re

def fix_quiz_file(file_path):
    """Fix the button onclick handlers in a quiz file."""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix: replace button onclick that has 'wrong' or other values with 'correct'
    # Pattern: onclick="window.checkQuizAnswer('q#', 'wrong', this)"
    # Replace with: onclick="window.checkQuizAnswer('q#', 'correct', this)"
    pattern = r'onclick="window\.checkQuizAnswer\(\'(q\d+)\',\s*\'wrong\',\s*this\)"'
    replacement = r'onclick="window.checkQuizAnswer(\'\1\', \'correct\', this)"'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        return True
    return False

# Scan all quiz files in Units 1-9
base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
fixed = 0
checked = 0

for unit in range(1, 10):
    unit_path = f"{base_path}/Unit{unit}"
    if not os.path.isdir(unit_path):
        continue
    
    # Get all lesson files in this unit
    for file in os.listdir(unit_path):
        if file.endswith('_Quiz.html'):
            file_path = os.path.join(unit_path, file)
            checked += 1
            if fix_quiz_file(file_path):
                fixed += 1
                lesson_id = file.replace('_Quiz.html', '').replace('Lesson', '')
                print(f"Fixed: {lesson_id}")

print(f"\nSummary: {fixed} quiz files fixed out of {checked} checked")
