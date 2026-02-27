#!/usr/bin/env python3
"""
Fix data-i18n attributes on lesson page titles to include the proper suffix 
(Summary, Quiz, Practice) based on the filename.
"""

import os
import re
from pathlib import Path

def fix_lesson_file(file_path):
    """Update data-i18n attribute on page-title to include page type suffix."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine page type from filename
        filename = os.path.basename(file_path)
        page_type = None
        
        if '_Summary.html' in filename:
            page_type = 'Summary'
        elif '_Quiz.html' in filename:
            page_type = 'Quiz'
        elif '_Practice.html' in filename:
            page_type = 'Practice'
        elif '_Video.html' in filename:
            page_type = None  # Video pages don't need a suffix
        else:
            return 'unknown_type'
        
        # Find and update the data-i18n attribute on the page-title h2
        # Using simpler non-regex approach to avoid special character issues
        lines = content.split('\n')
        modified = False
        new_lines = []
        
        for line in lines:
            if 'class="page-title" data-i18n=' in line:
                # Extract the data-i18n value
                match = re.search(r'data-i18n="([^"]*)"', line)
                if match:
                    title = match.group(1)
                    
                    # Check if title already has the page type suffix
                    if page_type and not (title.endswith(page_type) or 
                                         title.endswith(' - ' + page_type) or
                                         title.endswith(' Summary') or
                                         title.endswith(' - Quiz') or
                                         title.endswith(' Practice') or
                                         title.endswith(' - Practice')):
                        # Add appropriate suffix
                        if page_type == 'Quiz':
                            if ' - Quiz' not in title:
                                new_title = title + ' - Quiz'
                        elif page_type == 'Summary':
                            if not title.endswith('Summary'):
                                new_title = title + ' Summary'
                        elif page_type == 'Practice':
                            if ' - Practice' not in title and not title.endswith('Practice'):
                                new_title = title + ' Practice'
                        else:
                            new_title = title
                        
                        # Replace in the line
                        line = line.replace(f'data-i18n="{title}"', f'data-i18n="{new_title}"')
                        modified = True
            
            new_lines.append(line)
        
        new_content = '\n'.join(new_lines)
        
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'fixed'
        else:
            return 'no_change'
            
    except Exception as e:
        return f'error: {str(e)}'

def process_all_lessons(base_path):
    """Process all lesson folders."""
    lesson_folder_patterns = [
        'Algebra1Lessons',
        'Algebra2Lessons',
        'GeometryLessons',
        'PhysicsLessons',
        'BiologyLessons',
        'ChemistryLessons'
    ]
    
    stats = {
        'fixed': 0,
        'no_change': 0,
        'error': 0,
        'unknown_type': 0
    }
    
    arisEdu_path = os.path.join(base_path, 'ArisEdu Project Folder')
    
    for folder_pattern in lesson_folder_patterns:
        folder_path = os.path.join(arisEdu_path, folder_pattern)
        
        if not os.path.exists(folder_path):
            print(f"Folder not found: {folder_path}")
            continue
        
        print(f"\nProcessing {folder_pattern}...")
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    result = fix_lesson_file(file_path)
                    
                    if result == 'fixed':
                        stats['fixed'] += 1
                        print(f"  ✓ Fixed: {file}")
                    elif result == 'no_change':
                        stats['no_change'] += 1
                    elif result == 'unknown_type':
                        stats['unknown_type'] += 1
                    else:
                        stats['error'] += 1
                        print(f"  ✗ Error in {file}: {result}")
    
    return stats

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Starting from: {base_path}")
    
    stats = process_all_lessons(base_path)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Files fixed:                    {stats['fixed']}")
    print(f"Files with no changes needed:   {stats['no_change']}")
    print(f"Files with unknown type:        {stats['unknown_type']}")
    print(f"Files with errors:              {stats['error']}")
    print("="*60)
    
    if stats['fixed'] > 0:
        print(f"\n✓ Successfully fixed data-i18n attributes in {stats['fixed']} files!")
