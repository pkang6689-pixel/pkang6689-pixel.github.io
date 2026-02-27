#!/usr/bin/env python3
"""
Fix malformed nested <span class="translatable"> tags in Geometry lesson HTML files.
Pattern: <span class="translatable" data-en="Equilateral <span class="translatable" data-en="Triangle">Triangle</span>">
Should become: <span class="translatable" data-en="Equilateral Triangle">
"""

import os, re

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"
GEO_DIR = os.path.join(BASE, "GeometryLessons")

# Step 1: Find files with nested translatable spans
issues = []
for root, dirs, files in os.walk(GEO_DIR):
    for fn in files:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            # Find nested translatable spans inside data-en attributes
            pattern = r'data-en="[^"]*<span class="translatable"'
            matches = re.findall(pattern, content)
            if matches:
                issues.append((fp, len(matches)))

print(f"Files with nested span issues: {len(issues)}")
for fp, count in sorted(issues):
    print(f"  {fp}: {count} occurrences")

# Step 2: Fix each file
fixed_count = 0
for fp, _ in issues:
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Pattern: data-en="TEXT <span class="translatable" data-en="INNERTEXT">INNERTEXT</span>"
    # Replace with: data-en="TEXT INNERTEXT"
    # This handles the nested span INSIDE the data-en attribute
    
    # First, fix data-en attributes that contain nested spans
    # The inner span pattern in data-en: <span class="translatable" data-en="X">X</span>
    def fix_data_en(match):
        attr_value = match.group(1)
        # Remove nested span tags from within data-en value
        fixed = re.sub(
            r'<span class="translatable" data-en="([^"]+)">([^<]+)</span>',
            r'\2',  # Keep just the visible text
            attr_value
        )
        return f'data-en="{fixed}"'
    
    content = re.sub(r'data-en="([^"]*<span[^"]*)"', fix_data_en, content)
    
    # Now fix the element content (between > and </span>) that has nested spans
    # The visible content also has nested spans that should be simplified
    # Pattern: >TEXT <span class="translatable" data-en="X">X</span></span>
    # Should become: >TEXT X</span>
    
    # This is trickier because we need to collapse nested translatable spans in content
    # Let's do it iteratively
    while True:
        # Find and replace innermost nested translatable spans
        new_content = re.sub(
            r'<span class="translatable" data-en="([^"]+)">([^<]+)</span>',
            r'\2',
            content,
            count=0
        )
        # But we only want to do this for spans INSIDE other translatable spans
        # Actually, let's be more careful: only remove if the span is nested inside another translatable span
        # For now, let's check if removing caused issues
        
        # Actually, we need a smarter approach. Let me check which spans are nested.
        break
    
    # Better approach: find <span class="translatable data-en="OUTER_TEXT">OUTER_TEXT</span>
    # where OUTER_TEXT itself contains <span class="translatable"...>
    
    # An outer translatable span whose content has a nested translatable span:
    def fix_outer_span(match):
        data_en = match.group(1)
        inner_content = match.group(2)
        
        # Clean the data-en attribute
        clean_data_en = re.sub(
            r'<span class="translatable" data-en="[^"]+">([^<]+)</span>',
            r'\1',
            data_en
        )
        
        # Clean the inner content  
        clean_content = re.sub(
            r'<span class="translatable" data-en="[^"]+">([^<]+)</span>',
            r'\1',
            inner_content
        )
        
        # Also handle <span> without attributes (residual from partial fix)
        clean_content = re.sub(r'<span>([^<]+)</span>', r'\1', clean_content)
        
        return f'<span class="translatable" data-en="{clean_data_en}">{clean_content}</span>'
    
    # Match outer translatable spans that contain nested translatable or bare spans
    content = re.sub(
        r'<span class="translatable" data-en="([^"]*(?:<span[^"]*)[^"]*)">(.*?)</span>',
        fix_outer_span,
        content
    )
    
    # Also handle cases where data-en was already fixed but content still has nested spans
    def fix_content_spans(match):
        full = match.group(0)
        if '<span' not in match.group(2):
            return full
        data_en = match.group(1)
        inner = match.group(2)
        clean_inner = re.sub(r'<span[^>]*>([^<]*)</span>', r'\1', inner)
        return f'<span class="translatable" data-en="{data_en}">{clean_inner}</span>'
    
    content = re.sub(
        r'<span class="translatable" data-en="([^"]+)">((?:(?!</span>).)*?<span(?:(?!</span>).)*?</span>(?:(?!</span>).)*?)</span>',
        fix_content_spans,
        content
    )
    
    if content != original:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1
        print(f"  FIXED: {fp}")

print(f"\nFixed {fixed_count} files")

# Step 3: Verify - check if any nested spans remain
remaining = 0
for root, dirs, files in os.walk(GEO_DIR):
    for fn in files:
        if fn.endswith('.html'):
            fp = os.path.join(root, fn)
            with open(fp, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = re.findall(r'data-en="[^"]*<span class="translatable"', content)
            if matches:
                remaining += len(matches)
                print(f"  REMAINING: {fp}: {len(matches)}")

if remaining == 0:
    print("All nested span issues resolved!")
else:
    print(f"\n{remaining} nested spans still remain")
