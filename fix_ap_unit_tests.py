#!/usr/bin/env python3
"""
Fix AP unit test HTML files to include proper taskbar, styling, and structure.
"""

import os
from pathlib import Path

UNIT_TEST_TEMPLATE = """<!DOCTYPE html>

<html class="h-full" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../../../scripts/global_translations.js?v=7.2"></script>
    <script src="../../../../scripts/spanish_translations.js?v=1.0"></script>
    <script src="../../../../scripts/hindi_translations.js?v=1.0"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
<style>@view-transition {{ navigation: auto; }}
    

</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../../../theme_manager.js"></script>
    <script>
        // Apply translations when DOM is ready
        document.addEventListener("DOMContentLoaded", function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{
                    window.applyTranslations();
                }}, 50);
            }}
        }});
    </script>
    </head>
<body class="dark-mode h-full">
<script src="../../../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="test-content-view">
<h2 class="page-title" data-i18n="{title}">{title}</h2>
<div class="diagram-card">
<div class="lesson-notes">
<h3 data-i18n="{unit_name} Unit Tests">{unit_name} Unit Tests</h3>
<p>Unit tests for {course_name} {unit_name}.</p>
<p>Comprehensive assessment and practice materials coming soon.</p>
</div>
</div>
</div>
</main>
<script src="../../../../search_data.js"></script>
<script src="../../../../search_logic.js"></script>
</body>
</html>
"""

class APUnitTestFixer:
    def __init__(self, base_path: str = "ArisEdu Project Folder/AP_Unit_Tests"):
        self.base_path = Path(base_path)
        
    def process_all_tests(self):
        """Process all unit test files"""
        total_files = 0
        fixed_files = 0
        
        # Iterate through course folders
        for course_dir in sorted(self.base_path.iterdir()):
            if not course_dir.is_dir() or course_dir.name.startswith('.'):
                continue
            
            course_name = course_dir.name
            print(f"\nProcessing {course_name}...")
            
            # Iterate through unit folders within each course
            for unit_dir in sorted(course_dir.iterdir()):
                if not unit_dir.is_dir() or unit_dir.name.startswith('.'):
                    continue
                
                unit_name = unit_dir.name  # e.g., "Unit1", "Unit2"
                
                # Find unit_tests.html file
                unit_test_file = unit_dir / "unit_tests.html"
                if unit_test_file.exists():
                    total_files += 1
                    if self.fix_unit_test_file(unit_test_file, course_name, unit_name):
                        fixed_files += 1
                        print(f"  [OK] Fixed: {unit_name}/unit_tests.html")
                    else:
                        print(f"  [ERROR] {unit_name}/unit_tests.html")
        
        print(f"\n{'='*50}")
        print(f"Summary: Fixed {fixed_files}/{total_files} AP unit test files")
        print(f"{'='*50}")
    
    def fix_unit_test_file(self, file_path: Path, course_name: str, unit_name: str) -> bool:
        """Fix a single unit test file"""
        try:
            title = f"{course_name} - {unit_name} - Unit Tests"
            
            content = UNIT_TEST_TEMPLATE.format(
                title=title,
                course_name=course_name,
                unit_name=unit_name
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"Error fixing {file_path}: {e}")
            return False

def main():
    # Change to the workspace root
    workspace_root = Path(__file__).parent
    os.chdir(workspace_root)
    
    fixer = APUnitTestFixer()
    fixer.process_all_tests()
    print("\nAP unit test files have been fixed!")

if __name__ == "__main__":
    main()
