#!/usr/bin/env python3
import os
import re

def extract_flashcards_from_practice(file_path):
    """Extract flashcards from a practice file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the window.lessonFlashcards array
        match = re.search(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', content, re.DOTALL)
        if not match:
            return []
        
        flashcard_text = match.group(1)
        flashcards = []
        
        # Parse each flashcard object
        card_pattern = r'\{\s*"question":\s*"([^"]*(?:\\"[^"]*)*)",\s*"answer":\s*"([^"]*(?:\\"[^"]*)*)"\s*\}'
        for card_match in re.finditer(card_pattern, flashcard_text, re.DOTALL):
            question = card_match.group(1).replace('\\"', '"')
            answer = card_match.group(2).replace('\\"', '"')
            flashcards.append({"question": question, "answer": answer})
        
        return flashcards
    except Exception as e:
        print(f"Error extracting flashcards from {file_path}: {e}")
        return []

def extract_questions_from_quiz(file_path):
    """Extract quiz questions from a quiz file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        questions = []
        
        # Find all quiz-question divs
        question_pattern = r'<div class="quiz-question"[^>]*>.*?<p[^>]*>(.*?)</p>(.*?)</div>\s*</div>'
        
        for match in re.finditer(question_pattern, content, re.DOTALL):
            question_text = match.group(1).strip()
            # Remove question number
            question_text = re.sub(r'^\d+\.\s*', '', question_text)
            
            options_block = match.group(2)
            
            # Extract all options with their correct/wrong values
            options = []
            for opt_match in re.finditer(r'<label[^>]*>.*?<input[^>]*name="[^"]*"[^>]*value="([^"]*)"[^>]*>\s*([^<]*)', options_block, re.DOTALL):
                value = opt_match.group(1)
                option_text = opt_match.group(2).strip()
                options.append({"text": option_text, "is_correct": value == "correct"})
            
            if options and question_text:
                questions.append({
                    "text": question_text,
                    "options": options
                })
        
        return questions
    except Exception as e:
        print(f"Error extracting questions from {file_path}: {e}")
        return []

def create_unit_test_html(unit_num, flashcards, questions):
    """Create HTML for unit test with flashcards and questions"""
    
    html = f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Unit {unit_num}: Unit Test</title>
<script src="/_sdk/element_sdk.js"></script>
<script src="../../scripts/global_translations.js?v=7.0"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;family=Playfair+Display:wght@700&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
<style>@view-transition {{ navigation: auto; }}</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
<script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
<script src="../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="practice-content-view">
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
</div>

<div id="quiz-content-view">
<h2 class="page-title">Unit {unit_num}: Unit Test</h2>
<div class="diagram-card">
<div class="quiz-container">
<form id="quiz-form">
'''
    
    # Add questions
    for i, q in enumerate(questions, 1):
        html += f'''<div class="quiz-question" data-attempts="2" style="margin-bottom: 2rem;">
<div class="attempts-indicator">Attempts left: 2</div>
<p style="font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">{i}. {q['text']}</p>
'''
        letter_map = ['a', 'b', 'c', 'd']
        correct_answer = None
        
        for j, opt in enumerate(q['options'][:4]):  # Limit to 4 options
            letter = letter_map[j]
            if opt['is_correct']:
                correct_answer = letter
            html += f'''<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q{i}" style="margin-right:0.5rem;" type="radio" value="{letter}"/> {opt['text']}
</label>
'''
        
        html += f'''<button class="side-button" onclick="checkQuizAnswer('q{i}', '{correct_answer}', this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto;" type="button">Check Answer</button>
</div>
'''
    
    html += '''</form>
</div>
</div>
</main>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script src="../../scripts/taskbar.js"></script>
<script src="../../scripts/practice_games.js"></script>
<script src="../../scripts/quiz_ui.js"></script>
<script>
        window.lessonFlashcards = [
'''
    
    # Add flashcards
    for i, fc in enumerate(flashcards):
        question_escaped = fc['question'].replace('"', '\\"').replace('\n', '\\n')
        answer_escaped = fc['answer'].replace('"', '\\"').replace('\n', '\\n')
        html += f'''          {{
                    "question": "{question_escaped}",
                    "answer": "{answer_escaped}"
          }},
'''
    
    html += '''        ];
    </script>
</body>
</html>
'''
    return html

def generate_unit_tests():
    """Generate unit tests for all Algebra2 units"""
    base_path = '/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons'
    
    for unit_num in range(1, 10):
        unit_dir = os.path.join(base_path, f'Unit{unit_num}')
        
        if not os.path.exists(unit_dir):
            continue
        
        # Collect all practice and quiz files
        practice_files = sorted([f for f in os.listdir(unit_dir) if '_Practice.html' in f])
        quiz_files = sorted([f for f in os.listdir(unit_dir) if '_Quiz.html' in f])
        
        # Extract all flashcards
        all_flashcards = []
        for pfile in practice_files:
            ppath = os.path.join(unit_dir, pfile)
            cards = extract_flashcards_from_practice(ppath)
            all_flashcards.extend(cards)
        
        # Extract questions (up to 28)
        all_questions = []
        for qfile in quiz_files:
            if len(all_questions) >= 28:
                break
            qpath = os.path.join(unit_dir, qfile)
            questions = extract_questions_from_quiz(qpath)
            for q in questions:
                if len(all_questions) < 28:
                    all_questions.append(q)
        
        # Create HTML
        html_content = create_unit_test_html(unit_num, all_flashcards, all_questions)
        
        # Write to Unit test file
        test_file = os.path.join(unit_dir, f'Unit{unit_num}_Test.html')
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Created Unit {unit_num}_Test.html with {len(all_flashcards)} flashcards and {len(all_questions)} questions")

if __name__ == '__main__':
    generate_unit_tests()
