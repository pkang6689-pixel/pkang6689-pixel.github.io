#!/usr/bin/env python3
"""
Update AP lesson files to:
1. Add taskbar to Summary, Practice, and Quiz files
2. Add proper navigation between files (Video -> Summary -> Practice -> Quiz)
"""

import os
from pathlib import Path

# Updated templates with taskbar and navigation
UPDATED_TEMPLATES = {
    "_Practice.html": '''<!DOCTYPE html>

<html class="h-full" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} - Practice</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../../scripts/global_translations.js?v=7.2"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.0"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.0"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
<style>@view-transition {{ navigation: auto; }}
    

</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../../theme_manager.js"></script>
    <script>
        // Apply translations when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{
                    window.applyTranslations();
                }}, 50);
            }}
        }});
    </script>
    </head>
<body class="dark-mode h-full">
<script src="../../../scripts/taskbar.js"></script>
<main class="main-container">
<!-- Embedded Practice View -->
<div id="practice-content-view">
<h2 class="page-title" data-i18n="{title} - Practice">{title} - Practice</h2>
<div class="diagram-card">
<div class="flashcard-game" id="flashcard-game" style="margin-top:2rem;display:flex;flex-direction:column;align-items:center;perspective:1000px;overflow:hidden;">
<div class="flashcard-box" id="flashcard" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">
<span id="flashcard-content" style="width:100%;display:block;">Practice content coming soon...</span>
</div>
<div style="display:flex;gap:1rem;">
<button id="prev-flashcard" style="background:#ef4444;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
<svg fill="none" height="28" viewbox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
<path d="M15 6l-6 6 6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
</svg>
</button>
<button id="next-flashcard" style="background:#10b981;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
<svg fill="none" height="28" viewbox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
<path d="M9 6l6 6-6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
</svg>
</button>
</div>
</div>
<div class="side-buttons">
<a class="side-button" href="{base_lesson}_Quiz.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Quiz</a>
</div>
</div>
</main>
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
</body>
</html>
''',
    "_Summary.html": '''<!DOCTYPE html>

<html class="h-full" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} - Summary</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../../scripts/global_translations.js?v=7.2"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.0"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.0"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
<style>@view-transition {{ navigation: auto; }}
    

</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../../theme_manager.js"></script>
    <script>
        // Apply translations when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{
                    window.applyTranslations();
                }}, 50);
            }}
        }});
    </script>
    </head>
<body class="dark-mode h-full">
<script src="../../../scripts/taskbar.js"></script>
<main class="main-container">
<!-- Embedded Summary View -->
<div id="summary-content-view">
<h2 class="page-title" data-i18n="{title} - Summary">{title} - Summary</h2>
<div class="diagram-card">
<div class="lesson-notes">
<h3>Key Concepts</h3>
<p>Summary content coming soon...</p>
</div>
<div class="summary-actions">
<a class="side-button" href="{base_lesson}_Practice.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Play</a>
</div>
</div>
</div>
</main>
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
</body>
</html>
''',
    "_Quiz.html": '''<!DOCTYPE html>

<html class="h-full" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} - Quiz</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../../scripts/global_translations.js?v=7.2"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.0"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.0"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
<style>@view-transition {{ navigation: auto; }}
    

</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../../theme_manager.js"></script>
    <script>
        // Apply translations when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{
                    window.applyTranslations();
                }}, 50);
            }}
        }});
    </script>
    </head>
<body class="dark-mode h-full">
<script src="../../../scripts/taskbar.js"></script>
<main class="main-container">
<!-- Embedded Quiz View -->
<div id="quiz-content-view">
<h2 class="page-title" data-i18n="{title} - Quiz">{title} - Quiz</h2>
<div class="diagram-card">
<div class="quiz-container">
<p>Quiz content coming soon...</p>
</div>
</div>
</div>
</main>
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
</body>
</html>
''',
    "_Video.html": '''<!DOCTYPE html>

<html class="h-full" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title}</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../../scripts/global_translations.js?v=7.2"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.0"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.0"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
<style>@view-transition {{ navigation: auto; }}
    

</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../../theme_manager.js"></script>
    <script>
        // Apply translations when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{
                    window.applyTranslations();
                }}, 50);
            }}
        }});
    </script>
    </head>
<body class="dark-mode h-full">
<script src="../../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="lesson-content-view">
<h2 class="page-title" data-i18n="{title}">{title}</h2>
<div class="courses-container">
<div class="lesson-layout">
<div class="video-stack">
<div class="video-embed">
</div>
<div aria-live="polite" class="video-info-text" id="video-info-text"></div>
</div>
<div class="side-buttons">
<button class="side-button" onclick="toggleVideosPanel(this)" type="button">View other videos</button>
<div aria-hidden="true" class="videos-panel">
<div class="videos-panel-title">Lesson Videos</div>
<div class="videos-panel-item">
<a href="#">Video coming soon</a>
</div>
</div>
<a class="side-button" href="{base_lesson}_Summary.html">Next Up: Summary</a>
</div>
</div>
</div>
</main>
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
</body>
</html>
'''
}

class APLessonUpdater:
    def __init__(self, base_path: str = "ArisEdu Project Folder/APLessons"):
        self.base_path = Path(base_path)
    
    def process_all_lessons(self):
        """Update all AP lesson files"""
        total_files = 0
        fixed_files = 0
        
        for course_dir in sorted(self.base_path.iterdir()):
            if not course_dir.is_dir() or course_dir.name.startswith('.'):
                continue
            
            course_name = course_dir.name
            print(f"\nUpdating {course_name}...")
            
            for unit_dir in sorted(course_dir.iterdir()):
                if not unit_dir.is_dir() or unit_dir.name.startswith('.'):
                    continue
                
                for lesson_file in sorted(unit_dir.glob("Lesson*.html")):
                    total_files += 1
                    if self.update_lesson_file(lesson_file):
                        fixed_files += 1
        
        print(f"\n{'='*50}")
        print(f"Updated {fixed_files}/{total_files} AP lesson files")
        print(f"{'='*50}")
    
    def update_lesson_file(self, lesson_file: Path) -> bool:
        """Update a single lesson file with taskbar and navigation"""
        try:
            filename = lesson_file.name
            
            # Determine file type
            file_type = None
            for typ in ["_Practice.html", "_Summary.html", "_Quiz.html", "_Video.html"]:
                if filename.endswith(typ):
                    file_type = typ
                    break
            
            if not file_type:
                return False
            
            # Extract lesson identifier
            base_name = filename.replace(file_type, "")
            lesson_num = base_name.replace("Lesson", "")
            
            # Get course and unit from path
            course_name = lesson_file.parent.parent.name
            unit_name = lesson_file.parent.name
            
            # Create title
            title = f"{course_name} - {unit_name} - Lesson {lesson_num}"
            base_lesson = f"Lesson{lesson_num}"
            
            # Get the template
            template = UPDATED_TEMPLATES[file_type]
            
            # Format the template
            content = template.format(
                title=title,
                base_lesson=base_lesson
            )
            
            # Write the file
            with open(lesson_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        except Exception as e:
            print(f"    Error: {e}")
            return False

def main():
    workspace_root = Path(__file__).parent
    os.chdir(workspace_root)
    
    updater = APLessonUpdater()
    updater.process_all_lessons()
    print("\nAP lesson files have been updated with taskbars and navigation!")

if __name__ == "__main__":
    main()
