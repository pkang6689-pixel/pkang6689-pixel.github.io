#!/usr/bin/env python3
"""
Remove firebase-config.js from all quiz HTML files (we'll use dynamic import instead).
"""
import os
import re
from pathlib import Path

BASE = os.path.dirname(os.path.abspath(__file__))
ARISEDU = os.path.join(BASE, "ArisEdu Project Folder")
COURSE_FILES = os.path.join(ARISEDU, "CourseFiles")

def remove_firebase_script(filepath):
    """Remove firebase-config.js script tag from a quiz HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if firebase-config.js is present
    if 'firebase-config.js' not in content:
        return False
    
    # Remove the firebase-config.js script line
    pattern = r'\s*<script src="/ArisEdu Project Folder/firebase-config.js"></script>\n'
    new_content = re.sub(pattern, '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[REMOVED] firebase-config.js from: {filepath}")
    return True

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
                if remove_firebase_script(filepath):
                    updated += 1
    
    print(f"\n[DONE] Removed firebase-config.js from {updated}/{total} quiz files")

if __name__ == '__main__':
    main()
