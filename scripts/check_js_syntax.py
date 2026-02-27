#!/usr/bin/env python3
"""
Check JavaScript file for basic syntax errors
"""

import re

def check_syntax():
    filepath = "ArisEdu Project Folder/scripts/global_translations.js"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    errors = []
    
    # Check for unmatched braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces != close_braces:
        errors.append(f"Brace mismatch: {open_braces} open, {close_braces} close")
    
    # Check for unmatched parentheses
    open_parens = content.count('(')
    close_parens = content.count(')')
    if open_parens != close_parens:
        errors.append(f"Paren mismatch: {open_parens} open, {close_parens} close")
    
    # Check for unmatched brackets
    open_brackets = content.count('[')
    close_brackets = content.count(']')
    if open_brackets != close_brackets:
        errors.append(f"Bracket mismatch: {open_brackets} open, {close_brackets} close")
    
    # Check for quotes mismatch in translation dictionary
    # Count "key": "value" patterns
    translation_lines = re.findall(r'    "[^"]*":\s*"[^"]*"', content)
    if not translation_lines:
        errors.append("No valid translation pairs found")
    
    # Check the end of the file
    last_lines = content[-500:]
    if '});' not in last_lines:
        errors.append("File doesn't appear to end with });")
    
    if errors:
        print("❌ Syntax issues found:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("✅ File syntax appears valid:")
        print(f"  - Braces: {open_braces} pairs")
        print(f"  - Parentheses: {open_parens} pairs")
        print(f"  - Brackets: {open_brackets} pairs")
        print(f"  - Translation pairs found: {len(translation_lines)}")
        return True

if __name__ == "__main__":
    check_syntax()
