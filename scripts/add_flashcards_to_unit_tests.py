#!/usr/bin/env python3
"""Add flashcards to Biology Unit Tests by aggregating from lesson practice files."""

import os
import re
import json

BASE_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons"

# Lesson counts per unit (from bio.html)
UNIT_LESSONS = {
    1: 7,   # Lessons 1.1-1.7
    2: 7,   # Lessons 2.1-2.7
    3: 5,   # Lessons 3.1-3.5
    4: 6,   # Lessons 4.1-4.6 (but HTML shows up to 4.6)
    5: 6,   # Lessons 5.1-5.6
    6: 6,   # Lessons 6.1-6.6
    7: 6,   # Lessons 7.1-7.6 (HTML shows 7.6)
    8: 5,   # Lessons 8.1-8.5
    9: 5,   # Lessons 9.1-9.5
    10: 6,  # Lessons 10.1-10.6
    11: 6,  # Lessons 11.1-11.6
    12: 5,  # Lessons 12.1-12.5 (based on actual files, not HTML which shows 12.6)
}

def extract_flashcards_from_practice(filepath):
    """Extract flashcards array from a practice HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the lessonFlashcards array
        match = re.search(r'window\.lessonFlashcards\s*=\s*\[([\s\S]*?)\];', content)
        if not match:
            print(f"  Warning: No flashcards found in {filepath}")
            return []
        
        flashcard_content = match.group(1)
        # Parse the flashcards - they're in format { question: "...", answer: "..." }
        flashcards = []
        pattern = r'\{\s*question:\s*"([^"]+)",\s*answer:\s*"([^"]+)"\s*\}'
        for m in re.finditer(pattern, flashcard_content):
            flashcards.append({
                "question": m.group(1),
                "answer": m.group(2)
            })
        
        return flashcards
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return []

def get_unit_flashcards(unit_num):
    """Get all flashcards for a unit from its lesson practice files."""
    unit_folder = os.path.join(BASE_PATH, f"Unit{unit_num}")
    all_flashcards = []
    
    lesson_count = UNIT_LESSONS.get(unit_num, 6)
    
    for lesson in range(1, lesson_count + 1):
        practice_file = os.path.join(unit_folder, f"Lesson{unit_num}.{lesson}_Practice.html")
        if os.path.exists(practice_file):
            flashcards = extract_flashcards_from_practice(practice_file)
            all_flashcards.extend(flashcards)
            print(f"  Lesson {unit_num}.{lesson}: {len(flashcards)} flashcards")
        else:
            print(f"  Warning: {practice_file} not found")
    
    return all_flashcards

def format_flashcards_js(flashcards):
    """Format flashcards array as JavaScript."""
    lines = []
    for fc in flashcards:
        q = fc['question'].replace('"', '\\"').replace("'", "\\'")
        a = fc['answer'].replace('"', '\\"').replace("'", "\\'")
        lines.append(f'        {{ question: "{q}", answer: "{a}" }}')
    return ',\n'.join(lines)

def update_unit_test(unit_num, flashcards):
    """Update the unit test HTML to include flashcards."""
    test_file = os.path.join(BASE_PATH, f"Unit{unit_num}", f"Unit{unit_num}_Test.html")
    
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build the practice content view with flashcards
    flashcards_js = format_flashcards_js(flashcards)
    
    practice_html = f'''<div id="practice-content-view">
<h2 class="page-title">Unit {unit_num} Review Flashcards</h2>
<div class="diagram-card">
<div class="flashcard-game" id="flashcard-game" style="margin-top:2rem;display:flex;flex-direction:column;align-items:center;perspective:1000px;overflow:hidden;">
<div class="flashcard-box" id="flashcard" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">
<span id="flashcard-content" style="width:100%;display:block;"></span>
</div>
<div style="display:flex;gap:1rem;">
<button id="prev-flashcard" style="background:#ef4444;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
<svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
<path d="M15 6l-6 6 6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
</svg>
</button>
<button id="next-flashcard" style="background:#10b981;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
<svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
<path d="M9 6l6 6-6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
</svg>
</button>
<button id="shuffle-flashcard" title="Shuffle flashcards">
<svg fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
<path d="M4 4h7l-1.5 1.5M20 20h-7l1.5-1.5M4 20l16-16" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path>
</svg>
Shuffle
</button>
<span id="flashcard-counter" style="display:flex;align-items:center;font-weight:600;font-size:1rem;color:#64748b;white-space:nowrap;"></span>
</div>
</div>
<div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">
<button class="side-button" onclick="document.getElementById('practice-content-view').style.display='none';document.getElementById('quiz-content-view').style.display='block';" style="text-align:center;">Start Unit Test</button>
</div>
</div>
</div>'''
    
    # Replacethe empty practice-content-view placeholder
    old_practice = re.search(r'<div id="practice-content-view"[^>]*>[\s\S]*?</div>\s*\n\s*<div id="quiz-content-view"', content)
    if old_practice:
        content = content.replace(old_practice.group(0), practice_html + '\n\n<div id="quiz-content-view"')
    
    # Add flashcards script before closing body tag
    flashcards_script = f'''
<script>
    window.lessonFlashcards = [
{flashcards_js}
    ];
</script>
<script src="../../scripts/practice_games.js"></script>
<script src="../../scripts/block_puzzle.js"></script>
'''
    
    # Insert the script before </body>
    if 'window.lessonFlashcards' not in content:
        content = content.replace('</body>', flashcards_script + '</body>')
    
    # Add the review flashcards button to the quiz actions
    back_btn = '<button type="button" class="side-button" onclick="window.location.href=\'../../bio.html\'">Back to Biology</button>'
    review_btn = '<button type="button" class="side-button" onclick="document.getElementById(\'quiz-content-view\').style.display=\'none\';document.getElementById(\'practice-content-view\').style.display=\'block\';" style="background: #64748b;">Review Flashcards</button>\n'
    if '>Review Flashcards</button>' not in content:
        content = content.replace(back_btn, review_btn + back_btn)
    
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Updated {test_file}")

def main():
    for unit_num in range(1, 13):
        print(f"\nProcessing Unit {unit_num}...")
        flashcards = get_unit_flashcards(unit_num)
        print(f"  Total flashcards: {len(flashcards)}")
        update_unit_test(unit_num, flashcards)
    
    print("\nDone! All unit tests now have flashcards.")

if __name__ == "__main__":
    main()
