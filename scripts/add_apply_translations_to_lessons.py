#!/usr/bin/env python3
"""
Add applyTranslations() initialization to all lesson HTML files.
This ensures translations are applied when lesson pages load.
"""

import os
import re
from pathlib import Path

# Template for the translation initialization code
TRANSLATION_INIT_CODE = '''    <script>
        // Apply translations when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {
            if (window.applyTranslations) {
                setTimeout(function() {
                    window.applyTranslations();
                }, 50);
            }
        });
    </script>'''

def add_translations_to_file(file_path):
    """Add applyTranslations() code to a lesson file if it doesn't have it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has applyTranslations or initialization code
        if 'applyTranslations()' in content or 'DOMContentLoaded' in content:
            return 'already_has'
        
        # Find the position to insert the code (after the theme_manager.js script)
        # We want to insert it right before </head>
        head_close_match = re.search(r'</head>', content)
        if not head_close_match:
            return 'no_head_tag'
        
        insert_pos = head_close_match.start()
        
        # Insert the code
        new_content = content[:insert_pos] + TRANSLATION_INIT_CODE + '\n    ' + content[insert_pos:]
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return 'added'
    except Exception as e:
        return f'error: {str(e)}'

def process_lesson_folders(base_path):
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
        'added': 0,
        'already_has': 0,
        'error': 0,
        'no_head': 0,
        'files_processed': []
    }
    
    arisEdu_path = os.path.join(base_path, 'ArisEdu Project Folder')
    
    for folder_pattern in lesson_folder_patterns:
        folder_path = os.path.join(arisEdu_path, folder_pattern)
        
        if not os.path.exists(folder_path):
            print(f"Folder not found: {folder_path}")
            continue
        
        print(f"\nProcessing {folder_pattern}...")
        
        # Find all HTML files in this folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.html'):
                    file_path = os.path.join(root, file)
                    result = add_translations_to_file(file_path)
                    
                    if result == 'added':
                        stats['added'] += 1
                        stats['files_processed'].append((file_path, 'added'))
                        print(f"  ✓ Added: {file}")
                    elif result == 'already_has':
                        stats['already_has'] += 1
                    elif result == 'no_head_tag':
                        stats['no_head'] += 1
                        print(f"  ⚠ No </head> tag: {file}")
                    else:
                        stats['error'] += 1
                        print(f"  ✗ Error in {file}: {result}")
    
    return stats

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Starting from: {base_path}")
    
    stats = process_lesson_folders(base_path)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Files processed successfully:    {stats['added']}")
    print(f"Files already had code:          {stats['already_has']}")
    print(f"Files with no </head> tag:       {stats['no_head']}")
    print(f"Files with errors:               {stats['error']}")
    print("="*60)
    
    if stats['added'] > 0:
        print(f"\n✓ Successfully added translations to {stats['added']} files!")
    else:
        print("\nNo files needed to be updated.")
