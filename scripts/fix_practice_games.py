"""
Fix practice games: add initFlashcards() on page load.

The core issue: initFlashcards() only gets called when navigating from a parent
Lesson file via toggleToPractice(). When Practice.html, Summary.html, Quiz.html,
or the main Lesson file is loaded directly, initFlashcards() never fires.
Since all games (Boost, Mix & Match, Block Puzzle) depend on window.lessonFlashcards
which is set by initFlashcards(), they all break.

Fix: Add a script block before </body> that calls initFlashcards on DOMContentLoaded.
The function itself already has a flashcardsInitialized guard, so double-calls are safe.
"""

import os

directories = [
    "ArisEdu Project Folder/ChemistryLessons",
    "ArisEdu Project Folder/PhysicsLessons"
]

INIT_SCRIPT = """<script>
// Auto-initialize flashcards on direct page load
document.addEventListener('DOMContentLoaded', function() {
    if (typeof window.initFlashcards === 'function') {
        window.initFlashcards();
    }
});
</script>
"""

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Only process files that define initFlashcards
    if 'window.initFlashcards = function()' not in content:
        return False
    
    # Skip if already patched
    if 'Auto-initialize flashcards on direct page load' in content:
        return False
    
    # Insert init script before </body>
    content = content.replace('</body>', INIT_SCRIPT + '</body>')
    
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {os.path.basename(file_path)}")
        return True
    return False

def main():
    base_path = os.getcwd()
    fixed_count = 0
    total_count = 0
    
    for directory in directories:
        full_dir = os.path.join(base_path, directory)
        if not os.path.exists(full_dir):
            continue
            
        for root, dirs, files in os.walk(full_dir):
            for file in files:
                if not file.endswith(".html"):
                    continue
                
                total_count += 1
                file_path = os.path.join(root, file)
                if fix_file(file_path):
                    fixed_count += 1
    
    print(f"\nDone. Fixed {fixed_count} of {total_count} files.")

if __name__ == "__main__":
    main()
