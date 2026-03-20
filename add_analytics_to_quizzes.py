#!/usr/bin/env python3
"""
Add analytics and firebase scripts to all quiz HTML files.
"""
import os
import re
from pathlib import Path

BASE = os.path.dirname(os.path.abspath(__file__))
ARISEDU = os.path.join(BASE, "ArisEdu Project Folder")
COURSE_FILES = os.path.join(ARISEDU, "CourseFiles")

# Scripts to add (before quiz_loader.js)
SCRIPTS_TO_ADD = '''    <script src="/ArisEdu Project Folder/firebase-config.js"></script>
    <script src="/ArisEdu Project Folder/scripts/analytics-helper.js"></script>'''

def add_analytics_to_quiz(filepath):
    """Add analytics scripts to a quiz HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if scripts already added
    if 'analytics-helper.js' in content:
        print(f"[OK] Already has analytics: {filepath}")
        return False
    
    # Find and replace the quiz_loader.js line
    pattern = r'(\s*)<script src="/scripts/quiz_loader.js"></script>'
    if re.search(pattern, content):
        replacement = f'{SCRIPTS_TO_ADD}\n    <script src="/scripts/quiz_loader.js"></script>'
        new_content = re.sub(pattern, replacement, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[+] Updated: {filepath}")
        return True
    else:
        print(f"[-] No quiz_loader.js found: {filepath}")
        return False

def main():
    """Process all quiz files."""
    updated = 0
    total = 0
    
    # Walk through all CourseFiles subdirectories
    for root, dirs, files in os.walk(COURSE_FILES):
        for file in files:
            if file.endswith('_Quiz.html'):
                total += 1
                filepath = os.path.join(root, file)
                if add_analytics_to_quiz(filepath):
                    updated += 1
    
    print(f"\n[DONE] Updated {updated}/{total} quiz files")

if __name__ == '__main__':
    main()
