#!/usr/bin/env python3
"""
Update all unit test HTML files to include Firebase progress tracking
"""
import os
from pathlib import Path

# Path to unit tests directory
UNIT_TESTS_DIR = Path("ArisEdu Project Folder/AP_Unit_Tests")

# Script tag to add - inserted before closing </head> tag
FIREBASE_SCRIPT = '''    <script type="module" src="../../../../scripts/course-progress-firebase.js"></script>
'''

def update_unit_test_html(file_path):
    """Update a single unit test HTML file to include Firebase script"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has Firebase script
        if 'course-progress-firebase.js' in content:
            print(f"  [SKIP] {file_path.name} - already has Firebase script")
            return False
        
        # Check if has theme_manager.js script (marker for where to add our script)
        if 'theme_manager.js' in content:
            # Add Firebase script after theme_manager
            old_pattern = '<script src="/ArisEdu%20Project%20Folder/theme_manager.js"></script>'
            new_content = old_pattern + '\n' + FIREBASE_SCRIPT
            updated_content = content.replace(old_pattern, new_content)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"  [OK] {file_path.name}")
            return True
        else:
            print(f"  [WARN] {file_path.name} - theme_manager.js marker not found")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {file_path.name}: {e}")
        return False

def main():
    """Update all unit test HTML files"""
    print("\n[DEV] Updating Unit Test HTML Files with Firebase Integration\n")
    
    if not UNIT_TESTS_DIR.exists():
        print(f"Error: {UNIT_TESTS_DIR} not found")
        return
    
    html_files = list(UNIT_TESTS_DIR.rglob('unit_tests.html'))
    print(f"Found {len(html_files)} unit test files\n")
    
    updated = 0
    for html_file in sorted(html_files):
        # Show course/unit context
        parts = html_file.parts
        course = parts[parts.index('AP_Unit_Tests') + 1]
        unit = parts[parts.index('AP_Unit_Tests') + 2]
        print(f"Updating {course}/{unit}:")
        
        if update_unit_test_html(html_file):
            updated += 1
    
    print(f"\n{'='*60}")
    print(f"Updated {updated}/{len(html_files)} files")
    print(f"{'='*60}\n")
    print("All unit test files now include Firebase progress tracking!")
    print("Progress will be saved to Firebase when students complete tests.\n")

if __name__ == '__main__':
    main()
