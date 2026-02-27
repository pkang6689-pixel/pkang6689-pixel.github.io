#!/usr/bin/env python3
"""
Smart script to fix data-i18n attributes - only add suffixes if translations exist.
"""

import os
import re
import json
from pathlib import Path

def load_all_translation_keys():
    """Load all keys from translation dictionaries."""
    keys = set()
    
    # Load from both Spanish and Hindi files
    for trans_file in ['spanish_translations.js', 'hindi_translations.js']:
        trans_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'ArisEdu Project Folder', 'scripts', trans_file
        )
        
        if not os.path.exists(trans_path):
            continue
        
        try:
            with open(trans_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract all keys like: "Lesson 1.1: ..." or "Key Concepts: ..."
            pattern = r'"([^"]*(?:Lesson|Unit|Key Concepts|Quiz|Practice|Summary)[^"]*)"\s*:'
            matches = re.findall(pattern, content)
            keys.update(matches)
        except Exception as e:
            print(f"Error loading {trans_file}: {e}")
    
    return keys

def check_translation_exists(title, keys_set):
    """Check if a title or any of its variants exists in translation keys."""
    # Try exact match
    if title in keys_set:
        return title
    
    # Try with " - Quiz" suffix
    if (title + ' - Quiz') in keys_set:
        return title + ' - Quiz'
    
    # Try with " Summary" suffix  
    if (title + ' Summary') in keys_set:
        return title + ' Summary'
    
    # Try with " - Summary" suffix
    if (title + ' - Summary') in keys_set:
        return title + ' - Summary'
    
    # Try with " Practice" suffix
    if (title + ' Practice') in keys_set:
        return title + ' Practice'
    
    # Try with " - Practice" suffix
    if (title + ' - Practice') in keys_set:
        return title + ' - Practice'
    
    # No match found
    return None

def fix_lesson_file(file_path, translation_keys):
    """Update data-i18n attribute to use the best matching translation."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Determine page type from filename
        filename = os.path.basename(file_path)
        
        # Skip if no data-i18n attribute
        if 'data-i18n="' not in content or 'page-title' not in content:
            return 'skip'
        
        lines = content.split('\n')
        modified = False
        new_lines = []
        
        for line in lines:
            if 'class="page-title" data-i18n=' in line:
                # Extract the data-i18n value
                match = re.search(r'data-i18n="([^"]*)"', line)
                if match:
                    current_title = match.group(1)
                    
                    # Check if translations exist for this or any variant
                    best_match = check_translation_exists(current_title, translation_keys)
                    
                    # If we found a better match (with suffix), use it
                    if best_match and best_match != current_title:
                        line = line.replace(f'data-i18n="{current_title}"', f'data-i18n="{best_match}"')
                        modified = True
                        print(f"  ✓ Updated: {filename} -> {best_match}")
            
            new_lines.append(line)
        
        if modified:
            new_content = '\n'.join(new_lines)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return 'fixed'
        else:
            return 'no_change'
            
    except Exception as e:
        return f'error: {str(e)}'

def process_all_lessons(base_path, translation_keys):
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
        'skip': 0
    }
    
    arisEdu_path = os.path.join(base_path, 'ArisEdu Project Folder')
    
    for folder_pattern in lesson_folder_patterns:
        folder_path = os.path.join(arisEdu_path, folder_pattern)
        
        if not os.path.exists(folder_path):
            continue
        
        print(f"\nProcessing {folder_pattern}...")
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    result = fix_lesson_file(file_path, translation_keys)
                    
                    if result == 'fixed':
                        stats['fixed'] += 1
                    elif result == 'no_change':
                        stats['no_change'] += 1
                    elif result == 'skip':
                        stats['skip'] += 1
                    else:
                        stats['error'] += 1
                        print(f"  ✗ Error in {file}: {result}")
    
    return stats

if __name__ == '__main__':
    print("Loading translation keys...")
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    translation_keys = load_all_translation_keys()
    print(f"Loaded {len(translation_keys)} translation keys")
    
    print(f"\nStarting from: {base_path}")
    stats = process_all_lessons(base_path, translation_keys)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Files fixed (with better match):   {stats['fixed']}")
    print(f"Files already optimal:             {stats['no_change']}")
    print(f"Files skipped:                     {stats['skip']}")
    print(f"Files with errors:                 {stats['error']}")
    print("="*60)
    
    if stats['fixed'] > 0:
        print(f"\n✓ Successfully updated {stats['fixed']} files with better translation matches!")
