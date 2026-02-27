#!/usr/bin/env python3
"""Fix nested translatable spans in Geometry HTML files."""
import os, re

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
GEO_DIR = os.path.join(BASE, "GeometryLessons")

# Known nested inner span patterns (inner spans that appear inside outer spans)
# Pattern: <span class="translatable" data-en="X">X</span>
INNER_SPANS = [
    'Triangle',
    'Collinear points', 
    'Coplanar points',
]

def flatten_nested_spans(content):
    """Replace nested translatable spans with flat ones."""
    changed = False
    
    for inner_text in INNER_SPANS:
        inner_span = f'<span class="translatable" data-en="{inner_text}">{inner_text}</span>'
        
        # Pattern 1: Outer span wrapping PREFIX + inner span
        # <span class="translatable" data-en="PREFIX<inner_span>">PREFIX<inner_span></span>
        # The data-en contains the inner span HTML literally
        # We want: <span class="translatable" data-en="PREFIX INNER_TEXT">PREFIX INNER_TEXT</span>
        
        # Find all occurrences where this inner span is embedded in another data-en
        # The data-en attribute: data-en="SOME_PREFIX<span class="translatable" data-en="INNER_TEXT">INNER_TEXT</span>"
        
        # Since quotes inside data-en break normal parsing, look for the specific pattern
        search = f'data-en="{inner_text}">{inner_text}</span>'
        
        # Check if this inner span appears inside an outer span's data-en
        # Look for: data-en="PREFIX <span class="translatable" data-en="INNER">INNER</span>">PREFIX <span...
        # The key signature: the inner span's closing </span>" is followed by ">PREFIX" (content start)
        
        pass
    
    # More direct approach: find and replace the full nested pattern
    # Type A: "Isosceles Triangle", "Equilateral Triangle", "Scalene Triangle" 
    for prefix in ['Isosceles', 'Equilateral', 'Scalene']:
        inner = 'Triangle'
        # The full nested outer span pattern in the source:
        old = (f'<span class="translatable" data-en="{prefix} '
               f'<span class="translatable" data-en="{inner}">{inner}</span>">'
               f'{prefix} <span class="translatable" data-en="{inner}">{inner}</span></span>')
        new = f'<span class="translatable" data-en="{prefix} {inner}">{prefix} {inner}</span>'
        if old in content:
            content = content.replace(old, new)
            changed = True
            print(f"    Fixed: {prefix} {inner}")
    
    # Type B: "Non-Collinear points", "Non-Coplanar points"
    for inner in ['Collinear points', 'Coplanar points']:
        prefix = 'Non-'
        old = (f'<span class="translatable" data-en="{prefix}'
               f'<span class="translatable" data-en="{inner}">{inner}</span>">'
               f'{prefix}<span class="translatable" data-en="{inner}">{inner}</span></span>')
        new = f'<span class="translatable" data-en="{prefix}{inner}">{prefix}{inner}</span>'
        if old in content:
            content = content.replace(old, new)
            changed = True
            print(f"    Fixed: {prefix}{inner}")
    
    return content, changed

# Process all geometry files
total_fixed = 0
for root, dirs, files in os.walk(GEO_DIR):
    for fn in sorted(files):
        if not fn.endswith('.html'):
            continue
        fp = os.path.join(root, fn)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changed = flatten_nested_spans(content)
        if changed:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_content)
            total_fixed += 1
            print(f"  FIXED: {fp}")

print(f"\nTotal files fixed: {total_fixed}")

# Verify
remaining = 0
for root, dirs, files in os.walk(GEO_DIR):
    for fn in files:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            # Check for nested translatable spans
            for line_num, line in enumerate(content.split('\n'), 1):
                if line.count('<span class="translatable"') >= 2:
                    idx = line.find('<span class="translatable"')
                    if idx >= 0:
                        rest = line[idx+len('<span class="translatable"'):]
                        if '<span class="translatable"' in rest:
                            # Check if it's truly nested (inside data-en)
                            if 'data-en="' in line:
                                parts = line.split('data-en="')
                                for part in parts[1:]:
                                    if '<span class="translatable"' in part.split('"')[0] if '"' in part else part:
                                        remaining += 1
                                        print(f"  REMAINING: {fp} line {line_num}")
                                        break

if remaining == 0:
    print("\nAll nested span issues resolved!")
else:
    print(f"\n{remaining} nested spans still remain")
