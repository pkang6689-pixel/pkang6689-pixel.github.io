#!/usr/bin/env python3
"""
Generate Algebra 2 lesson files from templates.
Creates Video, Summary, Practice, and Quiz HTML files for all lessons,
plus Unit Test files for each unit.
"""

import os
from pathlib import Path

# Algebra 2 Curriculum
ALGEBRA2_UNITS = {
    1: {
        "name": "Foundations & Linear Systems",
        "lessons": {
            1: "Review of Functions & Notation",
            2: "Linear Equations & Graphing",
            3: "Systems of Linear Equations",
            4: "Solving Systems by Substitution",
            5: "Solving Systems by Elimination",
            6: "Applications of Linear Systems",
            7: "Inequalities & System of Inequalities",
            8: "Linear Programming",
            9: "Advanced Linear Applications ⭐",
        }
    },
    2: {
        "name": "Quadratic Functions",
        "lessons": {
            1: "Quadratic Functions & Parabolas",
            2: "Transformations of Quadratics",
            3: "Completing the Square",
            4: "Quadratic Formula & Discriminant",
            5: "Graphing Quadratic Functions",
            6: "Applications of Quadratics",
            7: "Quadratic Inequalities ⭐",
        }
    },
    3: {
        "name": "Polynomials",
        "lessons": {
            1: "Polynomial Operations",
            2: "Factoring Polynomials",
            3: "Synthetic Division",
            4: "Polynomial Graphs & Zeros",
            5: "Remainder & Factor Theorems",
            6: "Complex Numbers & Polynomial Roots",
            7: "Higher-Degree Polynomials ⭐",
        }
    },
    4: {
        "name": "Rational Expressions & Functions",
        "lessons": {
            1: "Rational Expressions",
            2: "Operations on Rational Expressions",
            3: "Rational Equations",
            4: "Graphing Rational Functions",
            5: "Asymptotes & Discontinuities",
            6: "Applications of Rational Functions ⭐",
        }
    },
    5: {
        "name": "Exponential & Logarithmic Functions",
        "lessons": {
            1: "Exponential Functions & Growth",
            2: "Exponential Decay & Applications",
            3: "Logarithms & Properties",
            4: "Logarithmic Functions & Graphs",
            5: "Exponential & Logarithmic Equations",
            6: "Applications of Exponentials & Logs",
            7: "Natural Logarithms & e ⭐",
        }
    },
    6: {
        "name": "Sequences & Series",
        "lessons": {
            1: "Arithmetic Sequences",
            2: "Geometric Sequences",
            3: "Series & Summation Notation",
            4: "Infinite Geometric Series",
            5: "Applications & Mathematical Induction ⭐",
        }
    },
    7: {
        "name": "Probability & Statistics",
        "lessons": {
            1: "Counting Principles",
            2: "Permutations & Combinations",
            3: "Probability Basics & Events",
            4: "Conditional Probability",
            5: "Normal Distributions",
            6: "Hypothesis Testing & Confidence Intervals",
            7: "Correlation & Linear Regression ⭐",
        }
    },
    8: {
        "name": "Trigonometry Connections",
        "lessons": {
            1: "Angles & Angle Measures",
            2: "Unit Circle & Trigonometric Ratios",
            3: "Graphs of Trigonometric Functions",
            4: "Trigonometric Identities",
            5: "Solving Trigonometric Equations",
            6: "Applications of Trigonometry ⭐",
        }
    },
    9: {
        "name": "Advanced Topics",
        "lessons": {
            1: "Conic Sections ⭐",
            2: "Parametric Equations ⭐",
            3: "Vectors & Vector Operations ⭐",
            4: "Complex Numbers in Polar Form ⭐",
        }
    },
}

# Base paths
BASE_DIR = Path("/workspaces/ArisEdu/ArisEdu Project Folder")
ALGEBRA2_LESSONS_DIR = BASE_DIR / "Algebra2Lessons"

def create_video_file(unit_num, lesson_num, lesson_title):
    """Create a Video lesson file."""
    content = f"""<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {unit_num}.{lesson_num}: {lesson_title}</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=7.0"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
    <style>@view-transition {{ navigation: auto; }}</style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
    <script src="../../scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="lesson-content-view">
            <h2 class="page-title">Lesson {unit_num}.{lesson_num}: {lesson_title}</h2>
            <div class="courses-container">
                <div class="lesson-layout">
                    <div class="video-stack">
                        <div class="video-embed">
                            <!-- Video iframe placeholder -->
                        </div>
                        <div id="video-info-text" class="video-info-text" aria-live="polite"></div>
                    </div>
                    <div class="side-buttons">
                        <button type="button" class="side-button view-other-videos" onclick="toggleVideosPanel(this)">View other videos</button>
                        <div class="videos-panel" aria-hidden="true">
                            <div class="videos-panel-title">Lesson {unit_num}.{lesson_num} videos</div>
                            <div class="videos-panel-item">
                                <a href="#" data-video-src="" data-video-title="Video 1">Video 1</a>
                                <div class="mini-rubric" aria-hidden="true">
                                    <span style="background:#ccc"></span>
                                    <span style="background:#ccc"></span>
                                    <span style="background:#ccc"></span>
                                    <span style="background:#ccc"></span>
                                </div>
                            </div>
                        </div>
<a class="side-button" href="Lesson{unit_num}.{lesson_num}_Summary.html">Next Up: Summary</a>
</div>
                </div>
<div class="rubric-box">
<div class="rubric-hover-wrap">
<div aria-hidden="true" class="rubric-hover-dot"><span>i</span></div>
<div aria-hidden="true" class="rubric-hover-panel">
<p><strong>Difficulty:</strong> How hard topic is &amp; how well they explained it</p>
<p><strong>Detail:</strong> Depth of content covered</p>
<p><strong>Speed:</strong> How long the video is</p>
<p><strong>Pace:</strong> How fast the video runs</p>
</div>
</div>
<h2 class="page-title">Rubric</h2>
<div class="rubric-card">
<div class="rubric-grid">
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Difficulty</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Detail</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Speed</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
<div class="rubric-item" style="background:#e2e8f0">
<div class="rubric-text">
<span class="rubric-label">Pace</span>
<span class="rubric-rating">TBD</span>
</div>
</div>
</div>
</div>
</div>

            </div>
        </div>
    </main>
    <script src="../../scripts/lesson_video.js"></script>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
</body>
</html>
"""
    return content

def create_summary_file(unit_num, lesson_num, lesson_title):
    """Create a Summary lesson file."""
    content = f"""<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {unit_num}.{lesson_num}: {lesson_title} - Summary</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=7.0"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
    <style>@view-transition {{ navigation: auto; }}</style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
    <script src="../../scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="summary-content-view">
            <h2 class="page-title">Lesson {unit_num}.{lesson_num}: {lesson_title}</h2>
            <div class="diagram-card">
                <div class="lesson-notes">
<h3>Key Concepts: {lesson_title}</h3>
<p>This lesson covers the fundamental concepts related to {lesson_title.lower()}. Students will learn core skills and principles needed to understand and apply these ideas in problem-solving contexts.</p>

                </div>
                <div class="summary-actions">
<a class="side-button" href="Lesson{unit_num}.{lesson_num}_Practice.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Play</a>
</div>
            </div>
        </div>
    </main>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
</body>
</html>
"""
    return content

def create_practice_file(unit_num, lesson_num, lesson_title):
    """Create a Practice lesson file with flashcards."""
    flashcard_questions = [
        f"What is {lesson_title.lower()}?",
        f"How do you identify {lesson_title.lower()}?",
        f"What are the key properties of {lesson_title.lower()}?",
        f"When would you use {lesson_title.lower()}?",
        f"Can you give an example of {lesson_title.lower()}?",
    ]
    
    flashcard_answers = [
        f"A concept related to {lesson_title.lower()} that is fundamental to this unit.",
        "You can identify it by looking for the defining characteristics and patterns.",
        "Key properties include the foundational principles covered in this lesson.",
        f"You would use {lesson_title.lower()} in real-world applications and problem-solving.",
        f"An example would be a practical scenario that demonstrates {lesson_title.lower()}.",
    ]
    
    flashcard_js = "".join([
        f'          {{\n                    "question": "{flashcard_questions[i]}",\n                    "answer": "{flashcard_answers[i]}"\n          }},\n'
        for i in range(len(flashcard_questions))
    ])
    
    content = f"""<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {unit_num}.{lesson_num}: {lesson_title} - Practice</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=7.0"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
    <style>@view-transition {{ navigation: auto; }}</style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
    <main class="main-container">
        <div id="practice-content-view">
<h2 class="page-title">Lesson {unit_num}.{lesson_num}: {lesson_title}</h2>
<div class="diagram-card">
<div class="flashcard-game" id="flashcard-game" style="margin-top:2rem;display:flex;flex-direction:column;align-items:center;perspective:1000px;overflow:hidden;">
<div class="flashcard-box" id="flashcard" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">
<span id="flashcard-content" style="width:100%;display:block;"></span>
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
<button id="shuffle-flashcard" title="Shuffle flashcards">
<svg fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
<path d="M4 4h7l-1.5 1.5M20 20h-7l1.5-1.5M4 20l16-16" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"></path>
</svg>
              Shuffle
            </button>
<span id="flashcard-counter" style="display:flex;align-items:center;font-weight:600;font-size:1rem;color:#64748b;white-space:nowrap;"></span>
</div>
</div>
<div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">
<a class="side-button" href="Lesson{unit_num}.{lesson_num}_Quiz.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Quiz</a>
</div>
</div>
</main>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script src="../../scripts/lesson_video.js"></script>
<script>
        window.lessonFlashcards = [
{flashcard_js}        ];
    </script>
<script src="../../scripts/taskbar.js"></script>
<script src="../../scripts/practice_games.js"></script>
<script src="../../scripts/block_puzzle.js"></script>
</body>
</html>
"""
    return content

def create_quiz_file(unit_num, lesson_num, lesson_title):
    """Create a Quiz lesson file."""
    content = f"""<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {unit_num}.{lesson_num}: {lesson_title} - Quiz</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=7.0"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
    <style>@view-transition {{ navigation: auto; }}</style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="../../theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
    <script src="../../scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="quiz-content-view">
            <h2 class="page-title">Lesson {unit_num}.{lesson_num}: {lesson_title} - Quiz</h2>
            <div class="diagram-card">
                <div class="quiz-container" style="padding: 2rem; width: 100%; height: 75vh; overflow-y: auto;">
                    <form id="quiz-form">

            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">1. Question about {lesson_title}?</p>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q1" value="correct"> Correct Answer
                </label>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q1" value="wrong"> Incorrect Option 1
                </label>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q1" value="wrong"> Incorrect Option 2
                </label>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q1" value="wrong"> Incorrect Option 3
                </label>
                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('q1', 'correct', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>
                    </form>
                    <div id="quiz-results" style="margin-top: 2rem; font-weight: bold; display:none; padding: 1rem; border-radius: 0.5rem;"></div>
                    <div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                        <button type="button" class="side-button" onclick="window.location.href='../../algebra2.html'">Back to Algebra 2</button>
                        <button type="button" class="side-button" onclick="window.location.href='Lesson{unit_num}.{lesson_num + 1}_Video.html'" style="display:none;">Next Lesson: {unit_num}.{lesson_num + 1}</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
    <script src="../../scripts/quiz_ui.js"></script>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
    <script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
    <script>
        function markQuizComplete() {{
            localStorage.setItem('alg2_u{unit_num}_l{lesson_num}_completed', 'true');
        }}
    </script>
</body>
</html>
"""
    return content

def create_unit_test_file(unit_num, unit_name):
    """Create a Unit Test file."""
    content = f"""<!DOCTYPE html>
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
<h2 class="page-title">Unit {unit_num}: {unit_name} - Unit Test</h2>
<div class="diagram-card">
<div class="quiz-container">
<form id="quiz-form">
<div class="quiz-question" data-attempts="2" style="margin-bottom: 2rem;">
<div class="attempts-indicator">Attempts left: 2</div>
<p style="font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">1. Question about Unit {unit_num} concepts?</p>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q1" style="margin-right:0.5rem;" type="radio" value="a"/> Option A
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q1" style="margin-right:0.5rem;" type="radio" value="b"/> Option B
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q1" style="margin-right:0.5rem;" type="radio" value="c"/> Option C
</label>
<label style="display:block; margin-bottom:0.5rem; cursor:pointer;">
<input name="q1" style="margin-right:0.5rem;" type="radio" value="d"/> Option D
</label>
<button class="side-button" onclick="checkQuizAnswer('q1', 'a', this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto;" type="button">Check Answer</button>
<button class="side-button" onclick="getAnotherQuestion(this)" style="margin-top:0.5rem; font-size:1rem; padding:0.5rem 1rem; min-width:auto; margin-left:0.5rem; background: #64748b;" type="button">Get another question</button>
</div>
                </form>
                <div id="quiz-results" style="margin-top: 2rem; font-weight: bold; display:none; padding: 1rem; border-radius: 0.5rem;"></div>
                <div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                    <button type="button" class="side-button" onclick="window.location.href='../../algebra2.html'">Back to Algebra 2</button>
                </div>
            </div>
        </div>
    </div>
</main>
<script src="../../scripts/taskbar.js"></script>
<script src="../../scripts/quiz_ui.js"></script>
<script src="../../scripts/practice_games.js"></script>
<!-- ArisEdu Global Search -->
<script src="../../../search_data.js"></script>
<script src="../../../search_logic.js"></script>
<script>
        window.lessonFlashcards = [
          {{
                    "question": "What is a key concept from Unit {unit_num}?",
                    "answer": "This unit covers important foundational concepts in {unit_name.lower()}"
          }},
          {{
                    "question": "How would you apply Unit {unit_num} concepts?",
                    "answer": "These concepts are applied in problem-solving within the broader Algebra 2 curriculum"
          }}
];
    </script>
</body>
</html>
"""
    return content

def main():
    """Generate all Algebra 2 files."""
    print("Generating Algebra 2 course structure...")
    
    # Create main Algebra2Lessons directory
    ALGEBRA2_LESSONS_DIR.mkdir(exist_ok=True)
    print(f"Created: {ALGEBRA2_LESSONS_DIR}")
    
    total_files = 0
    
    for unit_num, unit_data in ALGEBRA2_UNITS.items():
        unit_name = unit_data["name"]
        lessons = unit_data["lessons"]
        
        # Create unit directory
        unit_dir = ALGEBRA2_LESSONS_DIR / f"Unit{unit_num}"
        unit_dir.mkdir(exist_ok=True)
        print(f"Created: {unit_dir}")
        
        # Create lesson files
        for lesson_num, lesson_title in lessons.items():
            lesson_title_clean = lesson_title.replace(" ⭐", "")
            
            # Video file
            video_path = unit_dir / f"Lesson{unit_num}.{lesson_num}_Video.html"
            video_path.write_text(create_video_file(unit_num, lesson_num, lesson_title_clean))
            total_files += 1
            
            # Summary file
            summary_path = unit_dir / f"Lesson{unit_num}.{lesson_num}_Summary.html"
            summary_path.write_text(create_summary_file(unit_num, lesson_num, lesson_title_clean))
            total_files += 1
            
            # Practice file
            practice_path = unit_dir / f"Lesson{unit_num}.{lesson_num}_Practice.html"
            practice_path.write_text(create_practice_file(unit_num, lesson_num, lesson_title_clean))
            total_files += 1
            
            # Quiz file
            quiz_path = unit_dir / f"Lesson{unit_num}.{lesson_num}_Quiz.html"
            quiz_path.write_text(create_quiz_file(unit_num, lesson_num, lesson_title_clean))
            total_files += 1
        
        # Create unit test file
        test_path = unit_dir / f"Unit{unit_num}_Test.html"
        test_path.write_text(create_unit_test_file(unit_num, unit_name))
        total_files += 1
        
        print(f"  Created {len(lessons) * 4 + 1} files for Unit {unit_num}: {unit_name}")
    
    print(f"\n✅ Successfully generated {total_files} files for Algebra 2!")
    print(f"Location: {ALGEBRA2_LESSONS_DIR}")

if __name__ == "__main__":
    main()
