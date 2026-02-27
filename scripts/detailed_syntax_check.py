#!/usr/bin/env python3
"""
Find exact syntax issues in the JavaScript file
"""

import re

def find_syntax_issues():
    filepath = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Check for incomplete strings or unmatched quotes
    in_string = False
    string_char = None
    escape = False
    issues = []
    
    for line_num, line in enumerate(lines, 1):
        for i, char in enumerate(line):
            if escape:
                escape = False
                continue
            if char == '\\':
                escape = True
                continue
            if not in_string:
                if char in ('"', "'"):
                    in_string = True
                    string_char = char
            else:
                if char == string_char:
                    in_string = False
        
        # Check if line ends with unclosed string
        if in_string and line_num < len(lines):
            print(f"Line {line_num}: Unclosed string: {line.strip()[:80]}")
            issues.append((line_num, "Unclosed string"))
    
    # Check the very end
    if in_string:
        print(f"\n❌ File ends with unclosed string!")
    
    # Look for suspicious patterns
    for line_num, line in enumerate(lines, 1):
        # Check for }; at the wrong place
        if '};' in line and line_num > 32940 and line_num < 32955:
            print(f"Line {line_num}: Found }}; - {line.strip()}")
    
    return len(issues)

if __name__ == "__main__":
    count = find_syntax_issues()
    print(f"\nFound {count} issues")
