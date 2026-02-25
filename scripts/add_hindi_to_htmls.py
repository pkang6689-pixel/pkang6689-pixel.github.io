import os
import re

# Find all HTML files and add hindi_translations.js if not already present

root_dir = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder"

def should_add_script(filepath):
    """Check if we should add hindi_translations.js to this file"""
    if not filepath.endswith('.html'):
        return False
    
    # Exclude files that don't have user-facing content
    if 'template' in filepath.lower():
        return False
    
    return True

def add_hindi_script(filepath):
    """Add hindi_translations.js script tag if not present"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if hindi_translations.js is already there
    if 'hindi_translations.js' in content:
        print(f"✓ {filepath}: hindi_translations.js already present")
        return False
    
    # Check if spanish_translations.js is there to find where to insert
    if 'spanish_translations.js' in content:
        # Insert after spanish_translations.js
        match = re.search(r'<script src="[^"]*spanish_translations\.js[^"]*"></script>', content)
        if match:
            insertion_point = match.end()
            # Determine relative path
            relative_path = os.path.relpath(
                os.path.join(root_dir, 'scripts/hindi_translations.js'),
                os.path.dirname(filepath)
            )
            # Normalize path for web (use forward slashes)
            relative_path = relative_path.replace('\\', '/')
            
            script_tag = f'\n    <script src="{relative_path}?v=1.0"></script>'
            content = content[:insertion_point] + script_tag + content[insertion_point:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filepath}: Added hindi_translations.js")
            return True
    
    print(f"⚠ {filepath}: No spanish_translations.js found to use as reference")
    return False

# Walk through all HTML files
count = 0
added_count = 0

for root, dirs, files in os.walk(root_dir):
    for file in files:
        filepath = os.path.join(root, file)
        if should_add_script(filepath):
            count += 1
            if add_hindi_script(filepath):
                added_count += 1

# Also check the root index.html
root_index = r"c:\Users\Peter\pkang6689-pixel.github.io\index.html"
if os.path.exists(root_index):
    count += 1
    if add_hindi_script(root_index):
        added_count += 1

print(f"\nTotal: Processed {count} HTML files, added hindi_translations.js to {added_count} files")
