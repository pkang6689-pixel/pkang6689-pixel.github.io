#!/usr/bin/env python3
"""Generate real educational content for all Geometry lesson files."""
import os, html

BASE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\GeometryLessons"

def esc(s):
    return html.escape(s, quote=True)

def summary_html(lesson_id, title, body_html, next_practice):
    return f'''<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {lesson_id}: {esc(title)} - Summary</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=3.2"></script>
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
            <h2 class="page-title">Lesson {lesson_id}: {esc(title)}</h2>
            <div class="diagram-card">
                {body_html}
                
                <div class="summary-actions" style="margin-top: 2rem; display: flex; justify-content: center;">
                  <button class="action-button" onclick="window.location.href='{next_practice}'">Go to Practice</button>
                </div>
            </div>
        </div>
    </main>
</body>
</html>'''

def quiz_question_html(qnum, question, correct, wrong1, wrong2, wrong3):
    return f'''
            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{qnum}. {esc(question)}</p>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{qnum}" value="correct"> {esc(correct)}
                </label>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{qnum}" value="wrong"> {esc(wrong1)}
                </label>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{qnum}" value="wrong"> {esc(wrong2)}
                </label>
                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{qnum}" value="wrong"> {esc(wrong3)}
                </label>
                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('q{qnum}', 'correct', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>'''

def quiz_html(lesson_id, title, questions, unit_num, next_lesson_id):
    qs = ""
    for i, q in enumerate(questions, 1):
        qs += quiz_question_html(i, q[0], q[1], q[2], q[3], q[4])
    
    next_btn = f'<button type="button" class="side-button" onclick="window.location.href=\'Lesson{next_lesson_id}_Video.html\'">Next Lesson: {next_lesson_id}</button>' if next_lesson_id else ''
    
    return f'''<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {lesson_id}: {esc(title)} - Quiz</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=3.2"></script>
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
            <h2 class="page-title">Lesson {lesson_id}: {esc(title)} - Quiz</h2>
            <div class="diagram-card">
                <div class="quiz-container" style="padding: 2rem; width: 100%; height: 75vh; overflow-y: auto;">
                    <form id="quiz-form">
{qs}
                    </form>
                    <div id="quiz-results" style="margin-top: 2rem; font-weight: bold; display:none; padding: 1rem; border-radius: 0.5rem;"></div>
                    <div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                        <button type="button" class="side-button" onclick="window.location.href='../../geometry.html'">Back to Geometry</button>
                        {next_btn}
                    </div>
                </div>
            </div>
        </div>
    </main>
    <script src="../../scripts/quiz_ui.js"></script>
    <script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
    <script>
        function markQuizComplete() {{
            localStorage.setItem('geometry_l{lesson_id.replace(".", "_")}_completed', 'true');
        }}
    </script>
</body>
</html>'''

def practice_html(lesson_id, title, flashcards):
    fc_js = "[\n"
    for fc in flashcards:
        q = fc[0].replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')
        a = fc[1].replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')
        fc_js += f"          {{ question: '{q}', answer: '{a}' }},\n"
    fc_js += "      ]"
    
    return f'''<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lesson {lesson_id}: {esc(title)} - Practice</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=3.2"></script>
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
        <div id="practice-content-view">
            <h2 class="page-title">Lesson {lesson_id}: {esc(title)}</h2>
            <div class="game-hub-container fade-in">
                <!-- Flashcards Game -->
                <div class="game-tile" onclick="openFlashcardGame()">
                    <div class="game-icon">&#x1F5C2;&#xFE0F;</div>
                    <h3>Flashcards</h3>
                    <p>Review key terms and definitions.</p>
                </div>

                <!-- Climb the Leaderboard -->
                <div class="game-tile" onclick="openClimbGame()">
                    <div class="game-icon">&#x1F3C6;</div>
                    <h3>Climb the Leaderboard</h3>
                    <p>Answer questions to climb the ranks.</p>
                </div>

                <!-- Mix & Match -->
                <div class="game-tile" onclick="openMixMatchGame()">
                    <div class="game-icon">&#x1F9E9;</div>
                    <h3>Mix &amp; Match</h3>
                    <p>Match concepts with their definitions.</p>
                </div>
                
                 <!-- Block Puzzle -->
                <div class="game-tile" onclick="openBlockPuzzleGame()">
                    <div class="game-icon">&#x1F9F1;</div>
                    <h3>Block Puzzle</h3>
                    <p>Fit the blocks to solve the puzzle.</p>
                </div>
            </div>
            
            <!-- Game Containers -->
            <div id="flashcard-game-container" class="game-container" style="display: none;">
                 <!-- Flashcards content injected by JS -->
                 <button class="close-game-btn" onclick="closeGame()">Close</button>
            </div>
            
            <div id="climb-game-container" class="game-container" style="display: none;">
                 <!-- Climb content injected by JS -->
                 <button class="close-game-btn" onclick="closeGame()">Close</button>
            </div>
            
            <div id="mixmatch-container" class="game-container" style="display: none;">
                 <!-- MixMatch content injected by JS -->
                 <button class="close-game-btn" onclick="closeGame()">Close</button>
            </div>
            
            <div id="blockpuzzle-container" class="game-container" style="display: none;">
                 <!-- Block Puzzle content injected by JS -->
                 <button class="close-game-btn" onclick="closeGame()">Close</button>
            </div>
        </div>
    </main>
    <script>
        window.lessonFlashcards = {fc_js};
    </script>
    <script src="../../scripts/practice_games.js"></script>
    <script src="../../scripts/blocks_puzzle.js"></script>
    <script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
</body>
</html>'''

def write_lesson(unit_num, lesson_id, title, summary_body, questions, flashcards, next_lesson_id=None):
    unit_dir = os.path.join(BASE, f"Unit{unit_num}")
    os.makedirs(unit_dir, exist_ok=True)
    
    # Summary
    practice_link = f"Lesson{lesson_id}_Practice.html"
    s = summary_html(lesson_id, title, summary_body, practice_link)
    with open(os.path.join(unit_dir, f"Lesson{lesson_id}_Summary.html"), 'w', encoding='utf-8') as f:
        f.write(s)
    
    # Quiz
    q = quiz_html(lesson_id, title, questions, unit_num, next_lesson_id)
    with open(os.path.join(unit_dir, f"Lesson{lesson_id}_Quiz.html"), 'w', encoding='utf-8') as f:
        f.write(q)
    
    # Practice
    p = practice_html(lesson_id, title, flashcards)
    with open(os.path.join(unit_dir, f"Lesson{lesson_id}_Practice.html"), 'w', encoding='utf-8') as f:
        f.write(p)
    
    print(f"  Generated Lesson {lesson_id}: {title}")


# ============================================================================
# UNIT 1 – Foundations of Geometry
# ============================================================================
def generate_unit_1():
    print("Unit 1 – Foundations of Geometry")
    
    # Lesson 1.1: Points, Lines, and Planes
    write_lesson(1, "1.1", "Points, Lines, and Planes",
        summary_body="""
<h3>Key Concepts: Points, Lines, and Planes</h3>
<p><b>Point</b></p>
<p>A point is the most basic building block of geometry. It represents a <b>location in space</b> with no size, no width, no length, and no depth. Points are named with capital letters (e.g., point A).</p>

<p><b>Line</b></p>
<p>A line is a straight path that extends <b>infinitely in both directions</b>. It has no thickness and contains infinitely many points. A line is named by any two points on it (e.g., line AB, written &#x2190;&#x2192; AB) or by a lowercase letter.</p>
<ul>
<li><b>Collinear points</b>: Points that lie on the same line.</li>
<li><b>Non-collinear points</b>: Points that do NOT lie on the same line.</li>
</ul>

<p><b>Plane</b></p>
<p>A plane is a flat surface that extends <b>infinitely in all directions</b>. It has length and width but no thickness. A plane is named by three non-collinear points (e.g., plane ABC) or by a capital letter.</p>
<ul>
<li><b>Coplanar points</b>: Points that lie in the same plane.</li>
<li><b>Non-coplanar points</b>: Points that do NOT all lie in the same plane.</li>
</ul>

<p><b>Key Postulates</b></p>
<ul>
<li>Through any two points, there is exactly <b>one line</b>.</li>
<li>Through any three non-collinear points, there is exactly <b>one plane</b>.</li>
<li>A line contains at least <b>two points</b>.</li>
<li>A plane contains at least <b>three non-collinear points</b>.</li>
<li>If two points lie in a plane, the entire line containing them lies in the plane.</li>
<li>If two planes intersect, their intersection is a <b>line</b>.</li>
</ul>
""",
        questions=[
            ("What is a point in geometry?", "A location in space with no size or dimension", "A flat surface extending infinitely", "A straight path with two endpoints", "A measurement of distance"),
            ("How many points are needed to define a unique line?", "Two", "One", "Three", "Four"),
            ("What are collinear points?", "Points that lie on the same line", "Points that lie in the same plane", "Points that are equidistant from each other", "Points at the corners of a triangle"),
            ("Through any three non-collinear points, how many planes exist?", "Exactly one", "Exactly two", "Infinitely many", "None"),
            ("If two planes intersect, their intersection is always a:", "Line", "Point", "Plane", "Ray"),
            ("What does it mean for points to be coplanar?", "They lie in the same plane", "They lie on the same line", "They are the same distance apart", "They form a right angle"),
            ("A plane has which of the following properties?", "It extends infinitely and has no thickness", "It has length but no width", "It curves in three dimensions", "It contains exactly three points"),
        ],
        flashcards=[
            ("What is a point?", "A location in space with no size, width, length, or depth — named with a capital letter"),
            ("What is a line?", "A straight path extending infinitely in both directions with no thickness"),
            ("What is a plane?", "A flat surface extending infinitely in all directions with no thickness"),
            ("What are collinear points?", "Points that lie on the same line"),
            ("What are coplanar points?", "Points that lie in the same plane"),
            ("How many points define a unique line?", "Two points"),
            ("How many non-collinear points define a unique plane?", "Three non-collinear points"),
            ("If two planes intersect, what is their intersection?", "A line"),
            ("How is a line named?", "By two points on it (line AB) or by a lowercase letter"),
            ("How is a plane named?", "By three non-collinear points (plane ABC) or by a capital letter"),
        ],
        next_lesson_id="1.2"
    )
    
    # Lesson 1.2: Linear Measure and Precision
    write_lesson(1, "1.2", "Linear Measure and Precision",
        summary_body="""
<h3>Key Concepts: Linear Measure and Precision</h3>
<p><b>Line Segments</b></p>
<p>A <b>line segment</b> is a part of a line bounded by two endpoints. Unlike a line, a segment has a definite <b>length</b>. The length of segment AB is written as AB (without the bar above).</p>

<p><b>Measuring Segments</b></p>
<ul>
<li>Use a ruler to find the distance between two points.</li>
<li>The <b>precision</b> of a measurement depends on the smallest unit on the measuring tool.</li>
<li>All measurements are <b>approximations</b> — the true value lies within a range determined by the precision.</li>
</ul>

<p><b>Betweenness of Points</b></p>
<p>Point B is <b>between</b> points A and C if A, B, and C are collinear and AB + BC = AC. This is called the <b>Segment Addition Postulate</b>.</p>

<p><b>Congruent Segments</b></p>
<p>Two segments are <b>congruent</b> (&#x2245;) if they have the same length. Notation: AB &#x2245; CD means segment AB is congruent to segment CD.</p>
""",
        questions=[
            ("What is a line segment?", "A part of a line with two endpoints", "A line extending infinitely in one direction", "A curved path between two points", "An angle formed by two rays"),
            ("What does the Segment Addition Postulate state?", "If B is between A and C, then AB + BC = AC", "Any two segments are congruent", "A segment has infinite length", "All points on a segment are equidistant"),
            ("What does it mean for two segments to be congruent?", "They have the same length", "They are parallel", "They share an endpoint", "They lie in the same plane"),
            ("What is precision in measurement?", "The smallest unit available on the measuring tool", "The exact true value of a measurement", "The largest possible measurement", "The average of multiple measurements"),
            ("The symbol ≅ means:", "Congruent to", "Equal to", "Similar to", "Perpendicular to"),
            ("If AB = 5 and BC = 8, and B is between A and C, what is AC?", "13", "3", "40", "8"),
            ("Why are all measurements approximations?", "Because measuring tools have limited precision", "Because lines are infinite", "Because numbers are irrational", "Because geometry is theoretical"),
        ],
        flashcards=[
            ("What is a line segment?", "A part of a line bounded by two endpoints with a definite length"),
            ("State the Segment Addition Postulate.", "If B is between A and C, then AB + BC = AC"),
            ("What does congruent mean for segments?", "They have the same length (symbol: ≅)"),
            ("What is the precision of a measurement?", "The smallest unit on the measuring instrument"),
            ("What is a ray?", "A part of a line that has one endpoint and extends infinitely in one direction"),
            ("How do you denote the length of segment AB?", "AB (without a bar) represents the numerical length"),
            ("What is betweenness of points?", "B is between A and C if they are collinear and AB + BC = AC"),
            ("What is a ruler postulate?", "Points on a line can be paired with real numbers so that distances can be measured"),
            ("Are measurements ever exact?", "No — all measurements are approximations limited by precision"),
            ("If PQ ≅ RS, what do we know?", "PQ and RS have equal lengths"),
        ],
        next_lesson_id="1.3"
    )
    
    # Lesson 1.3: Distance and Midpoints
    write_lesson(1, "1.3", "Distance and Midpoints",
        summary_body="""
<h3>Key Concepts: Distance and Midpoints</h3>
<p><b>Distance Formula</b></p>
<p>The distance between two points (x&#x2081;, y&#x2081;) and (x&#x2082;, y&#x2082;) in the coordinate plane is:</p>
<p style="text-align:center; font-size:1.2rem;"><b>d = &#x221A;[(x&#x2082; &#x2212; x&#x2081;)&#xB2; + (y&#x2082; &#x2212; y&#x2081;)&#xB2;]</b></p>
<p>This formula comes from the <b>Pythagorean Theorem</b>.</p>

<p><b>Midpoint</b></p>
<p>The <b>midpoint</b> of a segment is the point that divides the segment into two <b>congruent</b> parts.</p>

<p><b>Midpoint Formula</b></p>
<p>The midpoint M of a segment with endpoints (x&#x2081;, y&#x2081;) and (x&#x2082;, y&#x2082;) is:</p>
<p style="text-align:center; font-size:1.2rem;"><b>M = ((x&#x2081; + x&#x2082;)/2, (y&#x2081; + y&#x2082;)/2)</b></p>

<p><b>Segment Bisector</b></p>
<p>A <b>segment bisector</b> is any segment, line, or ray that passes through the midpoint of a segment, dividing it into two congruent halves.</p>
""",
        questions=[
            ("What is the distance formula?", "d = √[(x₂−x₁)² + (y₂−y₁)²]", "d = (x₂+x₁)/2", "d = |x₂ − x₁|", "d = (x₂−x₁)(y₂−y₁)"),
            ("What is a midpoint?", "The point that divides a segment into two congruent parts", "The endpoint of a segment", "Any point on a segment", "The longest point on a line"),
            ("What is the midpoint of (2, 4) and (6, 8)?", "(4, 6)", "(8, 12)", "(2, 2)", "(3, 5)"),
            ("What is a segment bisector?", "A line, segment, or ray that passes through the midpoint", "A line perpendicular to another line", "A segment with equal endpoints", "A ray extending from the midpoint"),
            ("The distance formula is derived from which theorem?", "The Pythagorean Theorem", "The Triangle Inequality", "The Midpoint Theorem", "Euclid's First Postulate"),
            ("What is the distance between (0,0) and (3,4)?", "5", "7", "12", "25"),
            ("If M is the midpoint of AB, then AM = ?", "MB", "2AB", "AB/4", "AB"),
        ],
        flashcards=[
            ("State the distance formula.", "d = √[(x₂−x₁)² + (y₂−y₁)²]"),
            ("State the midpoint formula.", "M = ((x₁+x₂)/2, (y₁+y₂)/2)"),
            ("What is a midpoint?", "The point that divides a segment into two congruent parts"),
            ("What is a segment bisector?", "Any segment, line, or ray that passes through the midpoint of a segment"),
            ("What theorem is the distance formula based on?", "The Pythagorean Theorem"),
            ("Find the distance between (0,0) and (3,4).", "5 (since √(9+16) = √25 = 5)"),
            ("Find the midpoint of (1,3) and (5,7).", "(3, 5)"),
            ("If M is the midpoint of AB, what is true?", "AM = MB = AB/2"),
            ("What does bisect mean?", "To divide into two equal (congruent) parts"),
            ("Can a segment have more than one midpoint?", "No — every segment has exactly one midpoint"),
        ],
        next_lesson_id="1.4"
    )
    
    # Lesson 1.4: Angle Measure
    write_lesson(1, "1.4", "Angle Measure",
        summary_body="""
<h3>Key Concepts: Angle Measure</h3>
<p><b>Angles</b></p>
<p>An <b>angle</b> is formed by two rays with a common endpoint called the <b>vertex</b>. The rays are called the <b>sides</b> of the angle. Angles are measured in <b>degrees (°)</b>.</p>

<p><b>Types of Angles</b></p>
<ul>
<li><b>Acute angle</b>: An angle measuring between 0° and 90°.</li>
<li><b>Right angle</b>: An angle measuring exactly 90°.</li>
<li><b>Obtuse angle</b>: An angle measuring between 90° and 180°.</li>
<li><b>Straight angle</b>: An angle measuring exactly 180°.</li>
</ul>

<p><b>Angle Addition Postulate</b></p>
<p>If point D is in the interior of &#x2220;ABC, then m&#x2220;ABD + m&#x2220;DBC = m&#x2220;ABC.</p>

<p><b>Congruent Angles</b></p>
<p>Two angles are <b>congruent</b> if they have the same measure. Notation: &#x2220;A &#x2245; &#x2220;B.</p>

<p><b>Angle Bisector</b></p>
<p>An <b>angle bisector</b> is a ray that divides an angle into two congruent angles.</p>
""",
        questions=[
            ("What forms an angle?", "Two rays sharing a common endpoint (vertex)", "Two parallel lines", "A single line segment", "Two planes intersecting"),
            ("An angle measuring 47° is classified as:", "Acute", "Right", "Obtuse", "Straight"),
            ("What is a right angle?", "An angle measuring exactly 90°", "An angle measuring exactly 180°", "Any angle less than 90°", "An angle formed by perpendicular planes"),
            ("State the Angle Addition Postulate.", "If D is interior to ∠ABC, then m∠ABD + m∠DBC = m∠ABC", "All angles in a triangle sum to 180°", "Vertical angles are congruent", "Adjacent angles are supplementary"),
            ("What is an angle bisector?", "A ray that divides an angle into two congruent angles", "A line perpendicular to a side", "A segment connecting two vertices", "A line parallel to one side of an angle"),
            ("An angle measuring 135° is classified as:", "Obtuse", "Acute", "Right", "Reflex"),
            ("What is the vertex of an angle?", "The common endpoint of the two rays forming the angle", "The midpoint of the angle", "The point farthest from the angle", "Any point on either ray"),
        ],
        flashcards=[
            ("What is an angle?", "A figure formed by two rays with a common endpoint (vertex)"),
            ("What is an acute angle?", "An angle measuring between 0° and 90°"),
            ("What is a right angle?", "An angle measuring exactly 90°"),
            ("What is an obtuse angle?", "An angle measuring between 90° and 180°"),
            ("What is a straight angle?", "An angle measuring exactly 180°"),
            ("State the Angle Addition Postulate.", "If D is interior to ∠ABC, then m∠ABD + m∠DBC = m∠ABC"),
            ("What is an angle bisector?", "A ray that divides an angle into two congruent angles"),
            ("What are congruent angles?", "Angles that have the same measure"),
            ("What is the vertex of an angle?", "The common endpoint where the two rays meet"),
            ("How are angles measured?", "In degrees (°), using a protractor"),
        ],
        next_lesson_id="1.5"
    )
    
    # Lesson 1.5: Angle Relationships
    write_lesson(1, "1.5", "Angle Relationships",
        summary_body="""
<h3>Key Concepts: Angle Relationships</h3>
<p><b>Adjacent Angles</b></p>
<p><b>Adjacent angles</b> are two angles that share a common vertex and a common side but have no interior points in common.</p>

<p><b>Vertical Angles</b></p>
<p><b>Vertical angles</b> are two non-adjacent angles formed by two intersecting lines. Vertical angles are always <b>congruent</b>.</p>

<p><b>Complementary Angles</b></p>
<p>Two angles are <b>complementary</b> if the sum of their measures is <b>90°</b>.</p>

<p><b>Supplementary Angles</b></p>
<p>Two angles are <b>supplementary</b> if the sum of their measures is <b>180°</b>.</p>

<p><b>Linear Pair</b></p>
<p>A <b>linear pair</b> is a pair of adjacent angles whose non-common sides form a straight line. Linear pairs are always supplementary (sum to 180°).</p>

<p><b>Perpendicular Lines</b></p>
<p>Two lines are <b>perpendicular</b> (&#x22A5;) if they intersect to form right angles (90°).</p>
""",
        questions=[
            ("What are vertical angles?", "Non-adjacent angles formed by two intersecting lines", "Angles that share a common side", "Angles that sum to 90°", "Angles formed by parallel lines"),
            ("Two angles are complementary if their sum is:", "90°", "180°", "360°", "45°"),
            ("Two angles are supplementary if their sum is:", "180°", "90°", "360°", "270°"),
            ("What is a linear pair?", "Adjacent angles whose non-common sides form a straight line", "Two vertical angles", "Two angles that are both acute", "Angles on opposite sides of a transversal"),
            ("Vertical angles are always:", "Congruent", "Complementary", "Supplementary", "Adjacent"),
            ("If one angle of a linear pair measures 65°, what is the other?", "115°", "25°", "65°", "90°"),
            ("What does perpendicular mean?", "Lines that intersect at 90° angles", "Lines that never intersect", "Lines in the same plane", "Lines that intersect at 45°"),
        ],
        flashcards=[
            ("What are adjacent angles?", "Two angles sharing a common vertex and side with no interior points in common"),
            ("What are vertical angles?", "Non-adjacent angles formed by two intersecting lines — always congruent"),
            ("What are complementary angles?", "Two angles whose measures sum to 90°"),
            ("What are supplementary angles?", "Two angles whose measures sum to 180°"),
            ("What is a linear pair?", "Adjacent angles whose non-common sides form a straight line (they sum to 180°)"),
            ("Are vertical angles ever supplementary?", "Only if each measures 90° (both right angles)"),
            ("What are perpendicular lines?", "Lines that intersect to form right angles (90°)"),
            ("If ∠A = 35°, what is its complement?", "55° (because 90° − 35° = 55°)"),
            ("If ∠B = 120°, what is its supplement?", "60° (because 180° − 120° = 60°)"),
            ("Symbol for perpendicular?", "⊥"),
        ],
        next_lesson_id="1.6"
    )
    
    # Lesson 1.6: Two-Dimensional Figures
    write_lesson(1, "1.6", "Two-Dimensional Figures",
        summary_body="""
<h3>Key Concepts: Two-Dimensional Figures</h3>
<p><b>Polygons</b></p>
<p>A <b>polygon</b> is a closed figure formed by three or more line segments (sides) that meet at their endpoints (vertices). Key properties:</p>
<ul>
<li>Each side intersects exactly two other sides at their endpoints.</li>
<li>No two sides with a common endpoint are collinear.</li>
</ul>

<p><b>Classifying Polygons by Sides</b></p>
<ul>
<li><b>Triangle</b>: 3 sides</li>
<li><b>Quadrilateral</b>: 4 sides</li>
<li><b>Pentagon</b>: 5 sides</li>
<li><b>Hexagon</b>: 6 sides</li>
<li><b>Heptagon</b>: 7 sides</li>
<li><b>Octagon</b>: 8 sides</li>
<li><b>Nonagon</b>: 9 sides | <b>Decagon</b>: 10 sides | <b>Dodecagon</b>: 12 sides</li>
</ul>

<p><b>Convex vs. Concave</b></p>
<ul>
<li><b>Convex polygon</b>: All interior angles are less than 180°. Any line segment connecting two interior points lies entirely inside.</li>
<li><b>Concave polygon</b>: At least one interior angle is greater than 180°.</li>
</ul>

<p><b>Regular Polygon</b></p>
<p>A <b>regular polygon</b> is both equilateral (all sides congruent) and equiangular (all angles congruent).</p>

<p><b>Perimeter</b></p>
<p>The <b>perimeter</b> of a polygon is the sum of the lengths of its sides.</p>
""",
        questions=[
            ("What is a polygon?", "A closed figure formed by three or more line segments", "Any curved shape", "A figure with exactly two sides", "An open figure made of rays"),
            ("How many sides does a hexagon have?", "6", "5", "7", "8"),
            ("What is a regular polygon?", "A polygon that is both equilateral and equiangular", "Any polygon with all sides equal", "A polygon with all right angles", "A polygon with at least 6 sides"),
            ("A concave polygon has:", "At least one interior angle greater than 180°", "All interior angles less than 180°", "No vertices", "All sides of different lengths"),
            ("What is the perimeter of a polygon?", "The sum of the lengths of all its sides", "The area enclosed by the polygon", "The longest diagonal", "The number of sides"),
            ("How many sides does a decagon have?", "10", "12", "8", "9"),
            ("Which polygon has 4 sides?", "Quadrilateral", "Triangle", "Pentagon", "Hexagon"),
        ],
        flashcards=[
            ("What is a polygon?", "A closed figure formed by 3 or more line segments meeting at endpoints"),
            ("What is a convex polygon?", "A polygon where all interior angles are less than 180°"),
            ("What is a concave polygon?", "A polygon with at least one interior angle greater than 180°"),
            ("What is a regular polygon?", "A polygon that is both equilateral and equiangular"),
            ("How many sides does a pentagon have?", "5"),
            ("How many sides does an octagon have?", "8"),
            ("What is perimeter?", "The sum of the lengths of all sides of a polygon"),
            ("What is a diagonal?", "A segment connecting two non-adjacent vertices of a polygon"),
            ("Name a polygon with 12 sides.", "Dodecagon"),
            ("What makes a polygon irregular?", "Its sides or angles are not all congruent"),
        ],
        next_lesson_id="1.7"
    )
    
    # Lesson 1.7: Three-Dimensional Figures
    write_lesson(1, "1.7", "Three-Dimensional Figures",
        summary_body="""
<h3>Key Concepts: Three-Dimensional Figures</h3>
<p><b>Polyhedra</b></p>
<p>A <b>polyhedron</b> (plural: polyhedra) is a solid bounded by polygons called <b>faces</b>. The segments where faces meet are <b>edges</b>, and the points where edges meet are <b>vertices</b>.</p>

<p><b>Common 3D Figures</b></p>
<ul>
<li><b>Prism</b>: Two congruent, parallel polygonal bases connected by rectangular faces. Named by the shape of the base (triangular prism, rectangular prism, etc.).</li>
<li><b>Pyramid</b>: One polygonal base with triangular faces meeting at a single point (apex).</li>
<li><b>Cylinder</b>: Two congruent, parallel circular bases connected by a curved surface.</li>
<li><b>Cone</b>: One circular base tapering to a point (apex).</li>
<li><b>Sphere</b>: The set of all points equidistant from a center point.</li>
</ul>

<p><b>Euler's Formula</b></p>
<p>For any convex polyhedron: <b>V &#x2212; E + F = 2</b>, where V = vertices, E = edges, F = faces.</p>

<p><b>Cross Sections</b></p>
<p>A <b>cross section</b> is the shape formed when a plane intersects a solid figure.</p>
""",
        questions=[
            ("What is a polyhedron?", "A solid bounded by polygons (faces)", "Any three-dimensional object", "A circle in 3D space", "A curved surface enclosing a volume"),
            ("What does Euler's formula state for polyhedra?", "V − E + F = 2", "V + E + F = 2", "V × E = F", "V − E = F"),
            ("What is a prism?", "A solid with two congruent, parallel polygonal bases connected by rectangles", "A solid with one triangular base", "A solid with no flat faces", "A sphere with flat sides"),
            ("What is a cross section?", "The shape formed when a plane intersects a solid", "The bottom face of a polyhedron", "The outline of a 3D figure", "A diagonal of a polyhedron"),
            ("A cube has how many faces?", "6", "4", "8", "12"),
            ("What is the difference between a cylinder and a prism?", "A cylinder has circular bases; a prism has polygonal bases", "They are the same shape", "A cylinder has more faces", "A prism has curved surfaces"),
            ("What is the apex of a cone?", "The point at the top where the surface converges", "The circular base", "The center of the base", "The midpoint of the height"),
        ],
        flashcards=[
            ("What is a polyhedron?", "A solid bounded by polygonal faces"),
            ("State Euler's Formula.", "V − E + F = 2 (vertices minus edges plus faces equals 2)"),
            ("What is a prism?", "A solid with two congruent, parallel polygonal bases connected by rectangles"),
            ("What is a pyramid?", "A solid with one polygonal base and triangular faces meeting at an apex"),
            ("What is a cylinder?", "A solid with two congruent, parallel circular bases and a curved surface"),
            ("What is a cone?", "A solid with one circular base that tapers to a point (apex)"),
            ("What is a sphere?", "The set of all points equidistant from a center point"),
            ("What is a cross section?", "The intersection of a plane and a solid figure"),
            ("A cube has how many edges?", "12"),
            ("What are the faces of a polyhedron?", "The flat polygonal surfaces that bound the solid"),
        ],
        next_lesson_id=None  # End of unit
    )

# ============================================================================
# UNIT 2 – Reasoning and Proof
# ============================================================================
def generate_unit_2():
    print("Unit 2 – Reasoning and Proof")
    
    write_lesson(2, "2.1", "Inductive Reasoning and Conjecture",
        summary_body="""
<h3>Key Concepts: Inductive Reasoning and Conjecture</h3>
<p><b>Inductive Reasoning</b></p>
<p>Inductive reasoning uses <b>patterns and observations</b> to form a general conclusion called a <b>conjecture</b>. You look at specific cases and make an educated guess about what is always true.</p>
<ul>
<li>Example: 2, 4, 6, 8, ... → Conjecture: the next number is 10.</li>
<li>Inductive reasoning does NOT prove something is true — it only suggests it might be.</li>
</ul>

<p><b>Conjecture</b></p>
<p>A conjecture is an unproven statement based on observations. A conjecture remains unproven until it is shown to be either true (via a proof) or false (via a counterexample).</p>

<p><b>Counterexample</b></p>
<p>A <b>counterexample</b> is a single example that disproves a conjecture. You only need ONE counterexample to prove a conjecture is false.</p>
<ul>
<li>Conjecture: "All prime numbers are odd." Counterexample: 2 is prime and even.</li>
</ul>
""",
        questions=[
            ("What is inductive reasoning?", "Reasoning based on patterns to form a conjecture", "Reasoning from general to specific", "Reasoning that always proves a statement", "Reasoning based on definitions only"),
            ("What is a conjecture?", "An unproven statement based on observations", "A proven theorem", "A definition in geometry", "A postulate that is assumed true"),
            ("How many counterexamples are needed to disprove a conjecture?", "One", "Two", "Three", "It depends on the conjecture"),
            ("Which is an example of inductive reasoning?", "Noticing a pattern in several cases and predicting the next one", "Using a theorem to prove a statement", "Starting with axioms to derive a conclusion", "Using logic rules to form a proof"),
            ("The sequence 1, 4, 9, 16 suggests the next number is:", "25", "20", "32", "36"),
            ("A counterexample to 'all rectangles are squares' is:", "A rectangle with unequal length and width", "A square with sides of 5", "A circle", "A rhombus"),
            ("Does inductive reasoning guarantee truth?", "No, it only suggests a pattern", "Yes, it proves the statement", "Yes, if there are enough examples", "Only for numerical patterns"),
        ],
        flashcards=[
            ("What is inductive reasoning?", "Using patterns and observations to form a general conclusion (conjecture)"),
            ("What is a conjecture?", "An unproven statement based on observations"),
            ("What is a counterexample?", "A single example that disproves a conjecture"),
            ("How many counterexamples are needed to disprove a conjecture?", "Just one"),
            ("Does inductive reasoning prove anything?", "No — it only suggests something might be true"),
            ("Give an example of a conjecture.", "All prime numbers greater than 2 are odd"),
            ("What is the next number in 3, 6, 9, 12?", "15 (pattern: add 3)"),
            ("True or false: A conjecture is always true.", "False — it is unproven until demonstrated"),
            ("How do you prove a conjecture is false?", "Find a single counterexample"),
            ("Can a conjecture be proven true?", "Yes, through formal mathematical proof"),
        ],
        next_lesson_id="2.2"
    )
    
    write_lesson(2, "2.2", "Logic",
        summary_body="""
<h3>Key Concepts: Logic &#x2B50;</h3>
<p><b>Statements and Truth Values</b></p>
<p>A <b>statement</b> (or proposition) is a sentence that is either <b>true (T)</b> or <b>false (F)</b>, but not both.</p>

<p><b>Negation</b></p>
<p>The <b>negation</b> of a statement p (written ~p or ¬p) has the opposite truth value. If p is true, then ~p is false, and vice versa.</p>

<p><b>Compound Statements</b></p>
<ul>
<li><b>Conjunction (p &#x2227; q)</b>: "p AND q" — true only when BOTH p and q are true.</li>
<li><b>Disjunction (p &#x2228; q)</b>: "p OR q" — true when AT LEAST ONE of p or q is true.</li>
</ul>

<p><b>Truth Tables</b></p>
<p>A truth table shows all possible combinations of truth values for a compound statement. For two statements p and q, there are 4 possible combinations (TT, TF, FT, FF).</p>
""",
        questions=[
            ("What is a statement in logic?", "A sentence that is either true or false", "Any sentence in English", "A question about math", "An unproven conjecture"),
            ("What is the negation of a true statement?", "False", "True", "Unknown", "Undefined"),
            ("A conjunction (p ∧ q) is true when:", "Both p and q are true", "At least one is true", "Both are false", "p is true and q is false"),
            ("A disjunction (p ∨ q) is true when:", "At least one of p or q is true", "Both p and q are true", "Both are false", "Neither is true"),
            ("How many rows does a truth table for two variables have?", "4", "2", "8", "6"),
            ("What symbol represents negation?", "~ or ¬", "∧", "∨", "→"),
            ("If p is 'It is raining' and p is true, what is ~p?", "'It is not raining' and it is false", "'It is raining' and it is true", "'It might rain' and it is unknown", "'It is sunny' and it is true"),
        ],
        flashcards=[
            ("What is a statement in logic?", "A sentence that is definitively true or false"),
            ("What is negation?", "The opposite truth value of a statement (~p)"),
            ("What is a conjunction?", "p ∧ q: true only when BOTH p and q are true"),
            ("What is a disjunction?", "p ∨ q: true when AT LEAST ONE of p or q is true"),
            ("How many rows in a truth table for 2 variables?", "4 (TT, TF, FT, FF)"),
            ("What is a truth table?", "A table showing all possible truth value combinations for compound statements"),
            ("Symbol for conjunction?", "∧ (AND)"),
            ("Symbol for disjunction?", "∨ (OR)"),
            ("If p is false and q is true, what is p ∧ q?", "False (both must be true for conjunction)"),
            ("If p is false and q is true, what is p ∨ q?", "True (at least one is true for disjunction)"),
        ],
        next_lesson_id="2.3"
    )
    
    write_lesson(2, "2.3", "Conditional Statements",
        summary_body="""
<h3>Key Concepts: Conditional Statements</h3>
<p><b>Conditional Statement</b></p>
<p>A conditional statement has the form <b>"If p, then q"</b> (written p &#x2192; q). The <b>hypothesis</b> is p and the <b>conclusion</b> is q.</p>
<ul>
<li>A conditional is false ONLY when the hypothesis is true and the conclusion is false.</li>
</ul>

<p><b>Related Conditionals</b></p>
<ul>
<li><b>Converse</b>: If q, then p (q &#x2192; p) — swap hypothesis and conclusion.</li>
<li><b>Inverse</b>: If not p, then not q (~p &#x2192; ~q) — negate both.</li>
<li><b>Contrapositive</b>: If not q, then not p (~q &#x2192; ~p) — swap AND negate.</li>
</ul>

<p><b>Key Fact</b></p>
<p>A conditional and its <b>contrapositive</b> always have the <b>same truth value</b>. The converse and inverse also share the same truth value (but may differ from the original).</p>

<p><b>Biconditional</b></p>
<p>A biconditional statement (p &#x2194; q) means "p if and only if q." It is true when both p and q have the <b>same truth value</b>.</p>
""",
        questions=[
            ("In 'If p, then q,' what is p called?", "The hypothesis", "The conclusion", "The converse", "The inverse"),
            ("When is a conditional statement false?", "When the hypothesis is true and the conclusion is false", "When both parts are false", "When the conclusion is true", "When the hypothesis is false"),
            ("What is the contrapositive of 'If p, then q'?", "If not q, then not p", "If q, then p", "If not p, then not q", "If p, then not q"),
            ("What is the converse of 'If it rains, then the ground is wet'?", "If the ground is wet, then it rains", "If it does not rain, the ground is not wet", "If the ground is not wet, then it does not rain", "It rains and the ground is wet"),
            ("A conditional and its contrapositive:", "Always have the same truth value", "Always have opposite truth values", "Are unrelated", "Are always both true"),
            ("A biconditional is true when:", "p and q have the same truth value", "p is true regardless of q", "At least one is true", "Both are false"),
            ("What is the inverse of 'If p, then q'?", "If not p, then not q", "If q, then p", "If not q, then not p", "If p, then not q"),
        ],
        flashcards=[
            ("What is a conditional statement?", "If p, then q (p → q)"),
            ("What is the hypothesis?", "The 'if' part (p) of a conditional statement"),
            ("What is the conclusion?", "The 'then' part (q) of a conditional statement"),
            ("What is the converse?", "If q, then p (swap hypothesis and conclusion)"),
            ("What is the inverse?", "If not p, then not q (negate both parts)"),
            ("What is the contrapositive?", "If not q, then not p (swap and negate)"),
            ("What shares the same truth value as the original conditional?", "The contrapositive"),
            ("What is a biconditional?", "p if and only if q (p ↔ q) — true when both have the same truth value"),
            ("When is a conditional false?", "Only when the hypothesis is true and the conclusion is false"),
            ("Symbol for conditional?", "→"),
        ],
        next_lesson_id="2.4"
    )
    
    write_lesson(2, "2.4", "Deductive Reasoning",
        summary_body="""
<h3>Key Concepts: Deductive Reasoning &#x2B50;</h3>
<p><b>Deductive Reasoning</b></p>
<p>Deductive reasoning uses <b>facts, rules, definitions, or properties</b> to reach a logical conclusion. Unlike inductive reasoning, valid deductive reasoning <b>guarantees</b> a true conclusion if the premises are true.</p>

<p><b>Law of Detachment</b></p>
<p>If p &#x2192; q is true and p is true, then q must be true.</p>
<ul><li>Example: If a figure is a square, then it is a rectangle. Figure ABCD is a square. Therefore, ABCD is a rectangle.</li></ul>

<p><b>Law of Syllogism</b></p>
<p>If p &#x2192; q is true and q &#x2192; r is true, then p &#x2192; r is true.</p>
<ul><li>Example: If it rains, the ground gets wet. If the ground gets wet, the flowers grow. Therefore, if it rains, the flowers grow.</li></ul>
""",
        questions=[
            ("What is deductive reasoning?", "Using facts and rules to reach a guaranteed logical conclusion", "Using patterns to make a guess", "Making predictions based on observations", "Reasoning backwards from a conclusion"),
            ("The Law of Detachment states:", "If p→q is true and p is true, then q is true", "If p→q is true and q is true, then p is true", "If p→q and q→r, then p→r", "All conjectures can be proven"),
            ("The Law of Syllogism states:", "If p→q and q→r, then p→r", "If p→q and p is true, then q is true", "If p is false, then q is false", "All conditionals are biconditionals"),
            ("How is deductive reasoning different from inductive?", "Deductive guarantees truth; inductive only suggests it", "Both guarantee truth", "Inductive is more reliable", "They are the same process"),
            ("If 'All dogs are mammals' and 'Rex is a dog,' then:", "Rex is a mammal (Law of Detachment)", "All mammals are dogs", "Rex might be a mammal", "We cannot conclude anything"),
            ("If A→B and B→C, we can conclude:", "A→C", "C→A", "A→B only", "Nothing new"),
            ("Deductive reasoning starts with:", "General rules or known facts", "Specific observations", "A pattern of numbers", "An unproven conjecture"),
        ],
        flashcards=[
            ("What is deductive reasoning?", "Using facts, rules, and logic to reach a guaranteed conclusion"),
            ("State the Law of Detachment.", "If p→q is true and p is true, then q must be true"),
            ("State the Law of Syllogism.", "If p→q and q→r are both true, then p→r is true"),
            ("How is deductive different from inductive?", "Deductive guarantees truth from true premises; inductive only suggests patterns"),
            ("Give an example of the Law of Detachment.", "If it rains, I bring an umbrella. It rains. Therefore, I bring an umbrella."),
            ("Give an example of the Law of Syllogism.", "If A→B and B→C, then A→C"),
            ("Can deductive reasoning lead to a false conclusion?", "Only if a premise is false"),
            ("What type of reasoning do proofs use?", "Deductive reasoning"),
            ("Is a counterexample part of inductive or deductive reasoning?", "It is used to disprove conjectures (related to inductive reasoning)"),
            ("What makes deductive reasoning valid?", "The logical structure, not the content, determines validity"),
        ],
        next_lesson_id="2.5"
    )
    
    write_lesson(2, "2.5", "Postulates and Paragraph Proofs",
        summary_body="""
<h3>Key Concepts: Postulates and Paragraph Proofs</h3>
<p><b>Postulates (Axioms)</b></p>
<p>A <b>postulate</b> is a statement accepted as true <b>without proof</b>. Postulates serve as the foundation for building theorems through logical reasoning.</p>

<p><b>Theorems</b></p>
<p>A <b>theorem</b> is a statement that has been <b>proven true</b> using postulates, definitions, and previously proven theorems.</p>

<p><b>Paragraph Proof</b></p>
<p>A <b>paragraph proof</b> (informal proof) presents a logical argument in paragraph form, where each statement is backed by a reason (definition, postulate, or theorem).</p>
<ul>
<li>State what is given and what you need to prove.</li>
<li>Write a series of statements, each justified by a reason.</li>
<li>Conclude with what you set out to prove.</li>
</ul>
""",
        questions=[
            ("What is a postulate?", "A statement accepted as true without proof", "A statement that has been proven", "A conjecture based on observations", "A false statement used for testing"),
            ("What is a theorem?", "A statement proven true using logic", "A statement accepted without proof", "An unproven conjecture", "A definition of a geometric term"),
            ("What is a paragraph proof?", "A logical argument written in paragraph form with justified statements", "A list of formulas", "A diagram proving a conjecture", "An informal guess about geometric relationships"),
            ("What is needed to justify each step in a proof?", "A definition, postulate, or previously proven theorem", "Personal opinion", "A diagram only", "A calculator"),
            ("How does a postulate differ from a theorem?", "A postulate is assumed true; a theorem is proven", "Both are proven", "A theorem is assumed; a postulate is proven", "They are the same thing"),
            ("What should a proof always begin with?", "The given information and what needs to be proved", "The conclusion", "A counterexample", "A conjecture"),
            ("Why are postulates important?", "They form the foundation for proving theorems", "They disprove conjectures", "They are always false", "They replace definitions"),
        ],
        flashcards=[
            ("What is a postulate?", "A statement accepted as true without proof (also called an axiom)"),
            ("What is a theorem?", "A statement that has been proven true using logical reasoning"),
            ("What is a paragraph proof?", "A proof written in paragraph form where each statement is justified"),
            ("What is a proof?", "A logical argument showing that a statement is true"),
            ("Name one key postulate.", "Through any two points, there is exactly one line"),
            ("What is needed to justify a step in a proof?", "A definition, postulate, or previously proven theorem"),
            ("What is given information in a proof?", "The facts stated at the beginning that are assumed true"),
            ("What is the 'prove' statement?", "What you need to demonstrate is true by the end of the proof"),
            ("Can a theorem be used in other proofs?", "Yes — once proven, a theorem can justify later steps"),
            ("What is deductive reasoning's role in proofs?", "It ensures each step logically follows from the previous one"),
        ],
        next_lesson_id="2.6"
    )
    
    write_lesson(2, "2.6", "Algebraic Proof",
        summary_body="""
<h3>Key Concepts: Algebraic Proof</h3>
<p><b>Properties of Equality</b></p>
<p>These algebraic properties are used to justify steps in proofs:</p>
<ul>
<li><b>Reflexive Property</b>: a = a</li>
<li><b>Symmetric Property</b>: If a = b, then b = a</li>
<li><b>Transitive Property</b>: If a = b and b = c, then a = c</li>
<li><b>Addition Property</b>: If a = b, then a + c = b + c</li>
<li><b>Subtraction Property</b>: If a = b, then a − c = b − c</li>
<li><b>Multiplication Property</b>: If a = b, then ac = bc</li>
<li><b>Division Property</b>: If a = b and c ≠ 0, then a/c = b/c</li>
<li><b>Substitution Property</b>: If a = b, then a may replace b in any expression</li>
<li><b>Distributive Property</b>: a(b + c) = ab + ac</li>
</ul>
""",
        questions=[
            ("The Reflexive Property states:", "a = a", "If a = b, then b = a", "If a = b and b = c, then a = c", "a + 0 = a"),
            ("The Symmetric Property states:", "If a = b, then b = a", "a = a", "If a = b and b = c, then a = c", "a × 1 = a"),
            ("The Transitive Property states:", "If a = b and b = c, then a = c", "a = a", "If a = b, then b = a", "a + b = b + a"),
            ("Which property justifies: If x + 3 = 7, then x = 4?", "Subtraction Property of Equality", "Addition Property of Equality", "Reflexive Property", "Distributive Property"),
            ("The Distributive Property states:", "a(b+c) = ab + ac", "a + b = b + a", "a(bc) = (ab)c", "(a+b)² = a² + b²"),
            ("The Substitution Property allows you to:", "Replace a quantity with an equal quantity in any expression", "Add the same number to both sides", "Multiply both sides by the same number", "Reverse the order of an equation"),
            ("If 2x = 10, the Division Property gives:", "x = 5", "x = 20", "x = 10", "x = 2"),
        ],
        flashcards=[
            ("Reflexive Property", "a = a (any number equals itself)"),
            ("Symmetric Property", "If a = b, then b = a"),
            ("Transitive Property", "If a = b and b = c, then a = c"),
            ("Addition Property of Equality", "If a = b, then a + c = b + c"),
            ("Subtraction Property of Equality", "If a = b, then a − c = b − c"),
            ("Multiplication Property of Equality", "If a = b, then ac = bc"),
            ("Division Property of Equality", "If a = b and c ≠ 0, then a/c = b/c"),
            ("Substitution Property", "If a = b, then a can replace b in any expression"),
            ("Distributive Property", "a(b + c) = ab + ac"),
            ("What is an algebraic proof?", "A proof that uses algebraic properties to justify each step of solving an equation"),
        ],
        next_lesson_id="2.7"
    )
    
    write_lesson(2, "2.7", "Proving Segment Relationships",
        summary_body="""
<h3>Key Concepts: Proving Segment Relationships</h3>
<p><b>Properties of Segment Congruence</b></p>
<ul>
<li><b>Reflexive</b>: AB &#x2245; AB</li>
<li><b>Symmetric</b>: If AB &#x2245; CD, then CD &#x2245; AB</li>
<li><b>Transitive</b>: If AB &#x2245; CD and CD &#x2245; EF, then AB &#x2245; EF</li>
</ul>

<p><b>Two-Column Proof</b></p>
<p>A <b>two-column proof</b> organizes statements and reasons side by side:</p>
<ul>
<li><b>Left column</b>: Statements (what is true)</li>
<li><b>Right column</b>: Reasons (why it is true — definitions, postulates, theorems, properties)</li>
</ul>

<p><b>Segment Addition Postulate in Proofs</b></p>
<p>The Segment Addition Postulate (If B is between A and C, then AB + BC = AC) is frequently used to prove segment relationships.</p>
""",
        questions=[
            ("The Reflexive Property of Segment Congruence states:", "AB ≅ AB", "If AB ≅ CD then CD ≅ AB", "If AB ≅ CD and CD ≅ EF then AB ≅ EF", "AB + BC = AC"),
            ("In a two-column proof, the left column contains:", "Statements", "Reasons", "Diagrams", "Definitions only"),
            ("Which property states: If AB ≅ CD, then CD ≅ AB?", "Symmetric Property", "Reflexive Property", "Transitive Property", "Substitution Property"),
            ("The Segment Addition Postulate says:", "If B is between A and C, then AB + BC = AC", "AB = BA", "All segments are congruent", "A midpoint divides a segment in a 1:2 ratio"),
            ("In a proof, what justifies each statement?", "A definition, postulate, property, or theorem", "A guess", "The statement itself", "A counterexample"),
            ("If AB ≅ CD and CD ≅ EF, then:", "AB ≅ EF by the Transitive Property", "AB ≅ CD only", "EF ≅ CD only", "No conclusion can be drawn"),
            ("A two-column proof has how many columns?", "Two — statements and reasons", "Three — given, prove, diagram", "One — reasons only", "Four — hypothesis, proof, conclusion, diagram"),
        ],
        flashcards=[
            ("Reflexive Property of Congruence (segments)", "AB ≅ AB"),
            ("Symmetric Property of Congruence (segments)", "If AB ≅ CD, then CD ≅ AB"),
            ("Transitive Property of Congruence (segments)", "If AB ≅ CD and CD ≅ EF, then AB ≅ EF"),
            ("What is a two-column proof?", "A proof with statements in the left column and reasons in the right"),
            ("What goes in the 'Reasons' column?", "Definitions, postulates, theorems, or properties"),
            ("What is the Segment Addition Postulate?", "If B is between A and C, then AB + BC = AC"),
            ("What is the first step in a two-column proof?", "State the Given information"),
            ("What is the last step in a two-column proof?", "State what you wanted to Prove"),
            ("Can algebraic properties be used in geometric proofs?", "Yes — properties of equality apply to segment lengths"),
            ("Why are proofs important?", "They establish that geometric statements are always true, not just sometimes"),
        ],
        next_lesson_id="2.8"
    )
    
    write_lesson(2, "2.8", "Proving Angle Relationships",
        summary_body="""
<h3>Key Concepts: Proving Angle Relationships</h3>
<p><b>Properties of Angle Congruence</b></p>
<ul>
<li><b>Reflexive</b>: &#x2220;A &#x2245; &#x2220;A</li>
<li><b>Symmetric</b>: If &#x2220;A &#x2245; &#x2220;B, then &#x2220;B &#x2245; &#x2220;A</li>
<li><b>Transitive</b>: If &#x2220;A &#x2245; &#x2220;B and &#x2220;B &#x2245; &#x2220;C, then &#x2220;A &#x2245; &#x2220;C</li>
</ul>

<p><b>Key Theorems</b></p>
<ul>
<li><b>Supplement Theorem</b>: If two angles form a linear pair, they are supplementary.</li>
<li><b>Complement Theorem</b>: If the non-common sides of two adjacent angles form a right angle, the angles are complementary.</li>
<li><b>Vertical Angles Theorem</b>: Vertical angles are congruent.</li>
<li><b>Congruent Supplements Theorem</b>: If two angles are supplementary to the same angle (or congruent angles), they are congruent.</li>
<li><b>Congruent Complements Theorem</b>: If two angles are complementary to the same angle (or congruent angles), they are congruent.</li>
<li><b>Right Angle Theorems</b>: All right angles are congruent. Perpendicular lines form congruent adjacent angles.</li>
</ul>
""",
        questions=[
            ("The Vertical Angles Theorem states:", "Vertical angles are congruent", "Vertical angles are supplementary", "Vertical angles are complementary", "Vertical angles sum to 360°"),
            ("The Supplement Theorem states:", "Linear pair angles are supplementary", "All angles are supplementary", "Vertical angles are supplementary", "Complementary angles form a linear pair"),
            ("If ∠A and ∠B are both supplementary to ∠C, then:", "∠A ≅ ∠B", "∠A + ∠B = 180°", "∠A = 90°", "∠B = ∠C"),
            ("All right angles are:", "Congruent", "Supplementary", "Complementary", "Obtuse"),
            ("The Congruent Complements Theorem says:", "Two angles complementary to the same angle are congruent", "Complements are always 90°", "All complements are equal", "Complementary angles are vertical"),
            ("If perpendicular lines form 4 angles, each measures:", "90°", "45°", "180°", "60°"),
            ("Reflexive Property of Angle Congruence:", "∠A ≅ ∠A", "∠A + ∠B = 180°", "∠A ≅ ∠B implies ∠B ≅ ∠A", "∠A ≅ ∠B and ∠B ≅ ∠C implies ∠A ≅ ∠C"),
        ],
        flashcards=[
            ("Vertical Angles Theorem", "Vertical angles are congruent"),
            ("Supplement Theorem", "If two angles form a linear pair, they are supplementary"),
            ("Congruent Supplements Theorem", "Angles supplementary to the same angle are congruent to each other"),
            ("Congruent Complements Theorem", "Angles complementary to the same angle are congruent to each other"),
            ("Are all right angles congruent?", "Yes — every right angle measures exactly 90°"),
            ("Reflexive Property of Angle Congruence", "∠A ≅ ∠A"),
            ("Symmetric Property of Angle Congruence", "If ∠A ≅ ∠B, then ∠B ≅ ∠A"),
            ("Transitive Property of Angle Congruence", "If ∠A ≅ ∠B and ∠B ≅ ∠C, then ∠A ≅ ∠C"),
            ("What do perpendicular lines form?", "Four congruent right angles"),
            ("How do you prove angles are congruent in a proof?", "Use definitions, theorems, and properties of angle congruence"),
        ],
        next_lesson_id="2.9"
    )
    
    write_lesson(2, "2.9", "Proofs in Coordinate Geometry",
        summary_body="""
<h3>Key Concepts: Proofs in Coordinate Geometry &#x2B50;</h3>
<p><b>Coordinate Proofs</b></p>
<p>A <b>coordinate proof</b> uses the coordinate plane and algebraic methods (distance formula, midpoint formula, slope) to prove geometric theorems.</p>

<p><b>Steps for Coordinate Proofs</b></p>
<ol>
<li>Place the figure in the coordinate plane (choose convenient coordinates).</li>
<li>Use the <b>Distance Formula</b> to find lengths.</li>
<li>Use the <b>Midpoint Formula</b> to find midpoints.</li>
<li>Use the <b>Slope Formula</b> (rise/run) to determine parallelism or perpendicularity.</li>
<li>Draw conclusions based on the calculations.</li>
</ol>

<p><b>Slope</b></p>
<p>slope = (y&#x2082; &#x2212; y&#x2081;) / (x&#x2082; &#x2212; x&#x2081;)</p>
<ul>
<li>Parallel lines have <b>equal slopes</b>.</li>
<li>Perpendicular lines have slopes that are <b>negative reciprocals</b> (product = &#x2212;1).</li>
</ul>
""",
        questions=[
            ("What is a coordinate proof?", "A proof using the coordinate plane and algebraic formulas", "A proof using only diagrams", "A proof with no calculations", "A proof using inductive reasoning"),
            ("What formula determines if two segments are equal in length?", "The Distance Formula", "The Slope Formula", "The Quadratic Formula", "The Area Formula"),
            ("Parallel lines have:", "Equal slopes", "Perpendicular slopes", "Zero slopes", "Undefined slopes"),
            ("Perpendicular lines have slopes that are:", "Negative reciprocals", "Equal", "Both zero", "Both positive"),
            ("The slope formula is:", "(y₂−y₁)/(x₂−x₁)", "(x₂+x₁)/2", "√[(x₂−x₁)²+(y₂−y₁)²]", "x₂·y₂ − x₁·y₁"),
            ("Why place a figure at the origin in a coordinate proof?", "To simplify the calculations", "It is required by the postulates", "The origin has special properties", "All proofs must start there"),
            ("If line m has slope 2/3, a perpendicular line has slope:", "−3/2", "2/3", "3/2", "−2/3"),
        ],
        flashcards=[
            ("What is a coordinate proof?", "A proof using algebra and the coordinate plane to verify geometric properties"),
            ("What tools are used in coordinate proofs?", "Distance Formula, Midpoint Formula, and Slope Formula"),
            ("State the Slope Formula.", "m = (y₂−y₁)/(x₂−x₁)"),
            ("What slopes do parallel lines have?", "Equal slopes"),
            ("What slopes do perpendicular lines have?", "Negative reciprocals (their product is −1)"),
            ("Why place a figure at the origin?", "To simplify coordinates and calculations"),
            ("How to prove a quadrilateral is a rectangle using coordinates?", "Show all angles are 90° (adjacent sides have perpendicular slopes)"),
            ("How to prove segments are congruent using coordinates?", "Show they have equal lengths using the Distance Formula"),
            ("What is the slope of a horizontal line?", "0"),
            ("What is the slope of a vertical line?", "Undefined"),
        ],
        next_lesson_id=None
    )

# ============================================================================
# UNIT 3 – Parallel and Perpendicular Lines
# ============================================================================
def generate_unit_3():
    print("Unit 3 – Parallel and Perpendicular Lines")
    
    write_lesson(3, "3.1", "Parallel Lines and Transversals",
        summary_body="""
<h3>Key Concepts: Parallel Lines and Transversals</h3>
<p><b>Parallel Lines</b></p>
<p><b>Parallel lines</b> are coplanar lines that never intersect. Symbol: &#x2225; (e.g., line l &#x2225; line m).</p>

<p><b>Transversal</b></p>
<p>A <b>transversal</b> is a line that intersects two or more coplanar lines at different points. When a transversal crosses two lines, it creates 8 angles.</p>

<p><b>Angle Pairs Formed by a Transversal</b></p>
<ul>
<li><b>Corresponding angles</b>: Same position at each intersection (e.g., both upper-left). &#x2220;1 and &#x2220;5.</li>
<li><b>Alternate interior angles</b>: On opposite sides of the transversal, between the lines. &#x2220;3 and &#x2220;6.</li>
<li><b>Alternate exterior angles</b>: On opposite sides of the transversal, outside the lines. &#x2220;1 and &#x2220;8.</li>
<li><b>Consecutive interior angles</b> (co-interior / same-side interior): Same side of transversal, between the lines. &#x2220;3 and &#x2220;5.</li>
</ul>
""",
        questions=[
            ("What are parallel lines?", "Coplanar lines that never intersect", "Lines that intersect at 90°", "Lines in different planes", "Lines that meet at one point"),
            ("What is a transversal?", "A line that intersects two or more lines at different points", "A line parallel to two other lines", "A line segment with two endpoints", "A ray that bisects an angle"),
            ("How many angles does a transversal create when crossing two lines?", "8", "4", "6", "2"),
            ("Corresponding angles are:", "In the same position at each intersection", "On opposite sides between the lines", "On the same side between the lines", "Outside both lines on opposite sides"),
            ("Alternate interior angles are:", "On opposite sides of the transversal, between the lines", "In the same position at each intersection", "On the same side outside the lines", "Adjacent to each other"),
            ("Consecutive interior angles are also called:", "Same-side interior angles", "Alternate exterior angles", "Corresponding angles", "Vertical angles"),
            ("The symbol ∥ means:", "Parallel", "Perpendicular", "Congruent", "Similar"),
        ],
        flashcards=[
            ("What are parallel lines?", "Coplanar lines that never intersect (symbol: ∥)"),
            ("What is a transversal?", "A line that intersects two or more coplanar lines at different points"),
            ("What are corresponding angles?", "Angles in the same position at each intersection of the transversal"),
            ("What are alternate interior angles?", "Angles on opposite sides of the transversal, between the two lines"),
            ("What are alternate exterior angles?", "Angles on opposite sides of the transversal, outside the two lines"),
            ("What are consecutive interior angles?", "Angles on the same side of the transversal, between the two lines"),
            ("How many angles form when a transversal crosses 2 lines?", "8 angles"),
            ("What is a skew line?", "Lines that are not coplanar — they do not intersect and are not parallel"),
            ("Can parallel lines be in different planes?", "No — parallel lines must be coplanar"),
            ("What does coplanar mean?", "Lying in the same plane"),
        ],
        next_lesson_id="3.2"
    )
    
    write_lesson(3, "3.2", "Angles and Parallel Lines",
        summary_body="""
<h3>Key Concepts: Angles and Parallel Lines</h3>
<p><b>Postulate and Theorems (when lines ARE parallel)</b></p>
<ul>
<li><b>Corresponding Angles Postulate</b>: If two parallel lines are cut by a transversal, then corresponding angles are <b>congruent</b>.</li>
<li><b>Alternate Interior Angles Theorem</b>: If two parallel lines are cut by a transversal, then alternate interior angles are <b>congruent</b>.</li>
<li><b>Alternate Exterior Angles Theorem</b>: If two parallel lines are cut by a transversal, then alternate exterior angles are <b>congruent</b>.</li>
<li><b>Consecutive Interior Angles Theorem</b>: If two parallel lines are cut by a transversal, then consecutive interior angles are <b>supplementary</b> (sum to 180°).</li>
</ul>

<p><b>Key Idea</b></p>
<p>When lines are parallel, the angle relationships become predictable. These theorems are used extensively in proofs involving parallel lines.</p>
""",
        questions=[
            ("When parallel lines are cut by a transversal, corresponding angles are:", "Congruent", "Supplementary", "Complementary", "Unrelated"),
            ("Alternate interior angles formed by parallel lines are:", "Congruent", "Supplementary", "Complementary", "Right angles"),
            ("Consecutive interior angles formed by parallel lines are:", "Supplementary (sum to 180°)", "Congruent", "Complementary (sum to 90°)", "Equal to 90°"),
            ("Alternate exterior angles formed by parallel lines are:", "Congruent", "Supplementary", "Complementary", "Vertical"),
            ("If ∠1 = 70° and ∠1 corresponds to ∠5 with parallel lines, then ∠5 =", "70°", "110°", "20°", "90°"),
            ("If two parallel lines are cut by a transversal and one angle is 120°, its consecutive interior angle is:", "60°", "120°", "90°", "30°"),
            ("These angle relationships only hold when the lines are:", "Parallel", "Perpendicular", "Skew", "Intersecting at any angle"),
        ],
        flashcards=[
            ("Corresponding Angles Postulate", "If parallel lines are cut by a transversal, corresponding angles are congruent"),
            ("Alternate Interior Angles Theorem", "If parallel lines are cut by a transversal, alternate interior angles are congruent"),
            ("Alternate Exterior Angles Theorem", "If parallel lines are cut by a transversal, alternate exterior angles are congruent"),
            ("Consecutive Interior Angles Theorem", "If parallel lines are cut by a transversal, consecutive interior angles are supplementary"),
            ("If ∠1 = 55° (corresponding), what is ∠5?", "55° (congruent)"),
            ("If ∠3 = 80° (consecutive interior), what is ∠5?", "100° (supplementary: 180° − 80°)"),
            ("Do these theorems work for non-parallel lines?", "No — the lines must be parallel"),
            ("What is the converse of these theorems used for?", "To prove that lines are parallel"),
            ("What type of angles sum to 180° with parallel lines?", "Consecutive interior (same-side interior) angles"),
            ("What type of angles are congruent with parallel lines?", "Corresponding, alternate interior, and alternate exterior angles"),
        ],
        next_lesson_id="3.3"
    )
    
    write_lesson(3, "3.3", "Slopes of Lines",
        summary_body="""
<h3>Key Concepts: Slopes of Lines</h3>
<p><b>Slope</b></p>
<p>The <b>slope</b> of a line measures its steepness and direction. Given two points (x&#x2081;, y&#x2081;) and (x&#x2082;, y&#x2082;):</p>
<p style="text-align:center; font-size:1.2rem;"><b>m = (y&#x2082; &#x2212; y&#x2081;) / (x&#x2082; &#x2212; x&#x2081;)</b></p>

<p><b>Types of Slope</b></p>
<ul>
<li><b>Positive slope</b>: Line rises from left to right.</li>
<li><b>Negative slope</b>: Line falls from left to right.</li>
<li><b>Zero slope</b>: Horizontal line (y values constant).</li>
<li><b>Undefined slope</b>: Vertical line (x values constant, division by zero).</li>
</ul>

<p><b>Parallel and Perpendicular Slopes</b></p>
<ul>
<li><b>Parallel lines</b>: Same slope (m&#x2081; = m&#x2082;).</li>
<li><b>Perpendicular lines</b>: Slopes are negative reciprocals (m&#x2081; &#xD7; m&#x2082; = &#x2212;1).</li>
</ul>
""",
        questions=[
            ("What is the slope of a line through (1,2) and (3,6)?", "2", "4", "1/2", "3"),
            ("A horizontal line has a slope of:", "0", "Undefined", "1", "−1"),
            ("A vertical line has a slope that is:", "Undefined", "0", "1", "Infinite"),
            ("Parallel lines have:", "The same slope", "Perpendicular slopes", "Opposite slopes", "Zero slopes"),
            ("If one line has slope 3, a perpendicular line has slope:", "−1/3", "3", "−3", "1/3"),
            ("A line with negative slope:", "Falls from left to right", "Rises from left to right", "Is horizontal", "Is vertical"),
            ("The slope of a line through (0,0) and (4,4) is:", "1", "0", "4", "8"),
        ],
        flashcards=[
            ("Slope formula", "m = (y₂−y₁)/(x₂−x₁)"),
            ("Positive slope", "Line rises from left to right"),
            ("Negative slope", "Line falls from left to right"),
            ("Zero slope", "Horizontal line"),
            ("Undefined slope", "Vertical line"),
            ("Parallel lines have what slopes?", "Equal slopes (m₁ = m₂)"),
            ("Perpendicular lines have what slopes?", "Negative reciprocals (m₁ × m₂ = −1)"),
            ("Slope of line through (2,1) and (4,5)?", "2 — rise is 4, run is 2"),
            ("What does slope measure?", "The steepness and direction of a line (rise over run)"),
            ("Can two different lines have the same slope?", "Yes — they are parallel (or the same line if y-intercept also matches)"),
        ],
        next_lesson_id="3.4"
    )
    
    write_lesson(3, "3.4", "Equations of Lines",
        summary_body="""
<h3>Key Concepts: Equations of Lines</h3>
<p><b>Slope-Intercept Form</b></p>
<p style="text-align:center; font-size:1.2rem;"><b>y = mx + b</b></p>
<p>where m is the slope and b is the y-intercept.</p>

<p><b>Point-Slope Form</b></p>
<p style="text-align:center; font-size:1.2rem;"><b>y &#x2212; y&#x2081; = m(x &#x2212; x&#x2081;)</b></p>
<p>where m is the slope and (x&#x2081;, y&#x2081;) is a known point on the line.</p>

<p><b>Standard Form</b></p>
<p style="text-align:center; font-size:1.2rem;"><b>Ax + By = C</b></p>
<p>where A, B, and C are integers and A &#x2265; 0.</p>

<p><b>Writing Equations</b></p>
<ul>
<li>Given slope and y-intercept → use slope-intercept form.</li>
<li>Given slope and a point → use point-slope form.</li>
<li>Given two points → find slope first, then use point-slope form.</li>
<li>Parallel to a given line → same slope, different intercept.</li>
<li>Perpendicular to a given line → use negative reciprocal slope.</li>
</ul>
""",
        questions=[
            ("Slope-intercept form is:", "y = mx + b", "Ax + By = C", "y − y₁ = m(x − x₁)", "y = ax² + bx + c"),
            ("In y = mx + b, what does b represent?", "The y-intercept", "The slope", "The x-intercept", "A point on the line"),
            ("Point-slope form is:", "y − y₁ = m(x − x₁)", "y = mx + b", "Ax + By = C", "m = (y₂−y₁)/(x₂−x₁)"),
            ("What is the equation of a line with slope 2 passing through (1,3)?", "y − 3 = 2(x − 1)", "y = 3x + 2", "y − 1 = 2(x − 3)", "y = 2x − 3"),
            ("A line parallel to y = 3x + 1 has slope:", "3", "−1/3", "1", "−3"),
            ("A line perpendicular to y = 2x − 5 has slope:", "−1/2", "2", "1/2", "−2"),
            ("Standard form of a linear equation is:", "Ax + By = C", "y = mx + b", "y − y₁ = m(x − x₁)", "y = ax²"),
        ],
        flashcards=[
            ("Slope-intercept form", "y = mx + b (m = slope, b = y-intercept)"),
            ("Point-slope form", "y − y₁ = m(x − x₁) (m = slope, (x₁,y₁) = point)"),
            ("Standard form", "Ax + By = C (A, B, C are integers, A ≥ 0)"),
            ("How to write an equation from two points?", "Find slope first, then use point-slope form"),
            ("Equation parallel to y = 4x + 1 through (0,3)?", "y = 4x + 3 (same slope, different intercept)"),
            ("Equation perpendicular to y = 2x through (0,0)?", "y = −½x (negative reciprocal slope)"),
            ("What is the y-intercept?", "The point where the line crosses the y-axis (x = 0)"),
            ("What is the x-intercept?", "The point where the line crosses the x-axis (y = 0)"),
            ("How to convert point-slope to slope-intercept?", "Distribute and solve for y"),
            ("Can every line be written in slope-intercept form?", "No — vertical lines (x = a) cannot be written as y = mx + b"),
        ],
        next_lesson_id="3.5"
    )
    
    write_lesson(3, "3.5", "Proving Lines Parallel",
        summary_body="""
<h3>Key Concepts: Proving Lines Parallel</h3>
<p><b>Converses of Parallel Line Theorems</b></p>
<p>To <b>prove</b> lines are parallel, we use the converses of our earlier theorems:</p>
<ul>
<li><b>Converse of Corresponding Angles Postulate</b>: If corresponding angles are congruent, then the lines are parallel.</li>
<li><b>Converse of Alternate Interior Angles Theorem</b>: If alternate interior angles are congruent, then the lines are parallel.</li>
<li><b>Converse of Alternate Exterior Angles Theorem</b>: If alternate exterior angles are congruent, then the lines are parallel.</li>
<li><b>Converse of Consecutive Interior Angles Theorem</b>: If consecutive interior angles are supplementary, then the lines are parallel.</li>
</ul>

<p><b>Other Ways to Prove Lines Parallel</b></p>
<ul>
<li>If two lines are perpendicular to the same line, they are parallel.</li>
<li>If two lines have the same slope (in coordinate geometry), they are parallel.</li>
</ul>
""",
        questions=[
            ("How can you prove two lines are parallel using corresponding angles?", "Show that corresponding angles are congruent", "Show that corresponding angles are supplementary", "Show they have different slopes", "Show they intersect"),
            ("If alternate interior angles are congruent, the lines are:", "Parallel", "Perpendicular", "Skew", "Intersecting"),
            ("If consecutive interior angles are supplementary, the lines are:", "Parallel", "Perpendicular", "Congruent", "Collinear"),
            ("Two lines perpendicular to the same line are:", "Parallel to each other", "Perpendicular to each other", "Skew", "The same line"),
            ("What is the converse of a theorem?", "The statement formed by swapping hypothesis and conclusion", "The negation of the theorem", "The same theorem restated", "A counterexample to the theorem"),
            ("In coordinate geometry, parallel lines have:", "Equal slopes", "Negative reciprocal slopes", "Slopes that multiply to -1", "Undefined slopes"),
            ("If ∠3 ≅ ∠6 (alternate interior), lines l and m are:", "Parallel", "Perpendicular", "The same line", "Not related"),
        ],
        flashcards=[
            ("How to prove lines parallel with corresponding angles?", "Show corresponding angles are congruent"),
            ("How to prove lines parallel with alternate interior angles?", "Show alternate interior angles are congruent"),
            ("How to prove lines parallel with consecutive interior angles?", "Show consecutive interior angles are supplementary (sum to 180°)"),
            ("How to prove lines parallel with slopes?", "Show the lines have equal slopes"),
            ("If two lines are ⊥ to the same line, they are...", "Parallel to each other"),
            ("Converse of Corresponding Angles Postulate", "If corresponding angles are congruent, the lines are parallel"),
            ("Converse of Alternate Interior Angles Theorem", "If alt. interior angles are congruent, the lines are parallel"),
            ("Converse of Consecutive Interior Angles Theorem", "If consecutive interior angles are supplementary, lines are parallel"),
            ("What is a converse?", "Swapping the hypothesis and conclusion of a conditional statement"),
            ("Is the converse of a true theorem always true?", "Not necessarily — it must be proven separately"),
        ],
        next_lesson_id="3.6"
    )
    
    write_lesson(3, "3.6", "Perpendiculars and Distance",
        summary_body="""
<h3>Key Concepts: Perpendiculars and Distance</h3>
<p><b>Perpendicular Lines</b></p>
<p>Two lines are <b>perpendicular</b> if they intersect at right angles (90°). The shortest distance from a point to a line is always along the <b>perpendicular</b> segment.</p>

<p><b>Distance from a Point to a Line</b></p>
<p>The distance from a point to a line is measured along the perpendicular segment from the point to the line. This is the <b>shortest</b> distance.</p>

<p><b>Distance Between Parallel Lines</b></p>
<p>The distance between two parallel lines is the length of the perpendicular segment between them. This distance is <b>constant</b> everywhere.</p>

<p><b>Perpendicular Bisector</b></p>
<p>A <b>perpendicular bisector</b> of a segment is a line perpendicular to the segment at its midpoint. Any point on the perpendicular bisector is equidistant from the endpoints.</p>
""",
        questions=[
            ("The shortest distance from a point to a line is measured along:", "The perpendicular segment", "Any segment to the line", "A diagonal line", "A parallel line"),
            ("The distance between parallel lines is:", "Constant everywhere", "Different at every point", "Zero", "Undefined"),
            ("A perpendicular bisector passes through the:", "Midpoint of a segment, at 90°", "Endpoint of a segment", "Vertex of an angle", "Center of a circle"),
            ("Any point on the perpendicular bisector is:", "Equidistant from both endpoints", "Closer to one endpoint", "On the segment itself", "At the midpoint"),
            ("The distance from point P to line l is measured along what?", "The segment from P perpendicular to l", "The longest segment from P to l", "Any line from P to l", "A parallel line through P"),
            ("If two parallel lines are 5 units apart, every perpendicular segment between them measures:", "5 units", "More than 5 units", "Less than 5 units", "It varies"),
            ("Perpendicular lines form angles of:", "90°", "45°", "180°", "60°"),
        ],
        flashcards=[
            ("What is the shortest distance from a point to a line?", "The length of the perpendicular segment from the point to the line"),
            ("Distance between parallel lines", "The length of any perpendicular segment between them — always constant"),
            ("What is a perpendicular bisector?", "A line perpendicular to a segment at its midpoint"),
            ("Perpendicular Bisector Theorem", "Any point on the perpendicular bisector is equidistant from the endpoints"),
            ("How do perpendicular lines intersect?", "At right angles (90°)"),
            ("Can two parallel lines have different distances?", "No — the perpendicular distance is the same everywhere"),
            ("What is equidistant?", "Being the same distance from two or more objects"),
            ("How to find distance between parallel lines ax+by=c₁ and ax+by=c₂?", "|c₂−c₁|/√(a²+b²)"),
            ("What angle does a perpendicular segment make with a line?", "90°"),
            ("Is the perpendicular distance always the minimum?", "Yes — it is always the shortest path from a point to a line"),
        ],
        next_lesson_id="3.7"
    )
    
    write_lesson(3, "3.7", "Analytic Geometry Applications",
        summary_body="""
<h3>Key Concepts: Analytic Geometry Applications &#x2B50;</h3>
<p><b>Analytic (Coordinate) Geometry</b></p>
<p>Analytic geometry uses <b>coordinates and algebra</b> to study geometric figures. Key formulas:</p>
<ul>
<li><b>Distance Formula</b>: d = &#x221A;[(x&#x2082;&#x2212;x&#x2081;)&#xB2; + (y&#x2082;&#x2212;y&#x2081;)&#xB2;]</li>
<li><b>Midpoint Formula</b>: M = ((x&#x2081;+x&#x2082;)/2, (y&#x2081;+y&#x2082;)/2)</li>
<li><b>Slope Formula</b>: m = (y&#x2082;&#x2212;y&#x2081;)/(x&#x2082;&#x2212;x&#x2081;)</li>
</ul>

<p><b>Applications</b></p>
<ul>
<li><b>Classify shapes</b>: Use distance to verify side lengths, slope to check parallel/perpendicular sides.</li>
<li><b>Prove properties</b>: Show a quadrilateral is a parallelogram by proving opposite sides have equal slopes.</li>
<li><b>Find areas</b>: Use coordinates to calculate areas of triangles and polygons.</li>
<li><b>Verify geometric theorems</b>: Place figures on a coordinate plane and use algebra to confirm relationships.</li>
</ul>
""",
        questions=[
            ("Analytic geometry combines:", "Algebra and geometry on the coordinate plane", "Only shapes without coordinates", "Trigonometry and calculus", "Pure logic and definitions"),
            ("To prove a quadrilateral is a parallelogram using coordinates, show:", "Opposite sides have equal slopes", "All sides are equal", "All angles are 90°", "Diagonals are equal"),
            ("To verify a triangle is isosceles using coordinates:", "Show two sides have equal length using the distance formula", "Show all three angles are equal", "Show all sides are different", "Show it has a right angle"),
            ("The area of a triangle with vertices can be found using:", "The coordinate area formula: ½|x₁(y₂−y₃)+x₂(y₃−y₁)+x₃(y₁−y₂)|", "Only base × height", "Slope calculations only", "The midpoint formula"),
            ("To show sides are perpendicular, show their slopes:", "Multiply to −1", "Are equal", "Sum to 0", "Are both positive"),
            ("Why is coordinate geometry useful?", "It provides algebraic certainty for geometric relationships", "It replaces all other proof methods", "It only works for circles", "It eliminates the need for formulas"),
            ("To classify a quadrilateral as a rectangle, show:", "It is a parallelogram with at least one right angle", "All sides are equal", "It has one pair of parallel sides", "Diagonals are unequal"),
        ],
        flashcards=[
            ("What is analytic geometry?", "The study of geometry using coordinates and algebraic methods"),
            ("Three key formulas in analytic geometry?", "Distance, Midpoint, and Slope formulas"),
            ("How to prove sides are parallel?", "Show they have equal slopes"),
            ("How to prove sides are perpendicular?", "Show slopes multiply to −1 (negative reciprocals)"),
            ("How to prove sides are congruent?", "Show they have equal lengths using the distance formula"),
            ("Area of triangle from coordinates?", "½|x₁(y₂−y₃)+x₂(y₃−y₁)+x₃(y₁−y₂)|"),
            ("How to prove a shape is a square?", "Show all sides equal and all angles 90°"),
            ("How to prove a shape is a rhombus?", "Show all four sides are equal using distance formula"),
            ("What makes coordinate proof powerful?", "You can use algebra to prove general geometric statements"),
            ("How to find the perimeter of a polygon from coordinates?", "Sum the distances between consecutive vertices"),
        ],
        next_lesson_id=None
    )


# ============================================================================
# UNIT 4 – Triangles
# ============================================================================
def generate_unit_4():
    print("Unit 4 – Triangles")
    
    write_lesson(4, "4.1", "Classifying Triangles",
        summary_body="""
<h3>Key Concepts: Classifying Triangles</h3>
<p><b>Classifying by Sides</b></p>
<ul>
<li><b>Scalene triangle</b>: No sides are congruent.</li>
<li><b>Isosceles triangle</b>: At least two sides are congruent.</li>
<li><b>Equilateral triangle</b>: All three sides are congruent.</li>
</ul>

<p><b>Classifying by Angles</b></p>
<ul>
<li><b>Acute triangle</b>: All angles are less than 90°.</li>
<li><b>Right triangle</b>: One angle is exactly 90°.</li>
<li><b>Obtuse triangle</b>: One angle is greater than 90°.</li>
<li><b>Equiangular triangle</b>: All angles are equal (each is 60°).</li>
</ul>

<p><b>Key Facts</b></p>
<ul>
<li>Every equilateral triangle is also equiangular (and vice versa).</li>
<li>An isosceles triangle has a vertex angle (between the congruent sides) and two base angles (which are congruent).</li>
</ul>
""",
        questions=[
            ("A triangle with no congruent sides is:", "Scalene", "Isosceles", "Equilateral", "Right"),
            ("A triangle with all sides congruent is:", "Equilateral", "Scalene", "Isosceles", "Obtuse"),
            ("A triangle with one 90° angle is:", "Right", "Acute", "Obtuse", "Equiangular"),
            ("An equiangular triangle has angle measures of:", "60°, 60°, 60°", "90°, 45°, 45°", "120°, 30°, 30°", "90°, 90°, 0°"),
            ("Every equilateral triangle is also:", "Equiangular", "Right", "Scalene", "Obtuse"),
            ("An isosceles triangle has:", "At least two congruent sides", "No congruent sides", "All sides different", "One right angle always"),
            ("A triangle with one angle of 120° is:", "Obtuse", "Acute", "Right", "Equiangular"),
        ],
        flashcards=[
            ("Scalene triangle", "A triangle with no congruent sides"),
            ("Isosceles triangle", "A triangle with at least two congruent sides"),
            ("Equilateral triangle", "A triangle with all three sides congruent"),
            ("Acute triangle", "A triangle where all angles are less than 90°"),
            ("Right triangle", "A triangle with one angle equal to 90°"),
            ("Obtuse triangle", "A triangle with one angle greater than 90°"),
            ("Equiangular triangle", "A triangle with all angles equal (each 60°)"),
            ("Are equilateral triangles also equiangular?", "Yes — and vice versa"),
            ("What are the base angles of an isosceles triangle?", "The two congruent angles opposite the congruent sides"),
            ("Can a triangle be both right and obtuse?", "No — a triangle can only have one angle ≥ 90°"),
        ],
        next_lesson_id="4.2"
    )
    
    write_lesson(4, "4.2", "Angles of Triangles",
        summary_body="""
<h3>Key Concepts: Angles of Triangles</h3>
<p><b>Triangle Angle Sum Theorem</b></p>
<p>The sum of the measures of the interior angles of a triangle is <b>180°</b>.</p>
<p style="text-align:center; font-size:1.2rem;">m&#x2220;A + m&#x2220;B + m&#x2220;C = 180°</p>

<p><b>Exterior Angle Theorem</b></p>
<p>The measure of an <b>exterior angle</b> of a triangle equals the sum of the two <b>non-adjacent interior angles</b> (remote interior angles).</p>

<p><b>Corollaries</b></p>
<ul>
<li>The acute angles of a right triangle are <b>complementary</b> (sum to 90°).</li>
<li>A triangle can have <b>at most one</b> right angle or obtuse angle.</li>
</ul>
""",
        questions=[
            ("The sum of interior angles of a triangle is:", "180°", "360°", "90°", "270°"),
            ("An exterior angle of a triangle equals:", "The sum of the two remote interior angles", "The adjacent interior angle", "180° minus all three angles", "Half the largest interior angle"),
            ("In a right triangle, the two acute angles sum to:", "90°", "180°", "45°", "60°"),
            ("If two angles of a triangle are 50° and 60°, the third is:", "70°", "80°", "50°", "90°"),
            ("A triangle can have at most how many obtuse angles?", "One", "Two", "Three", "Zero"),
            ("The exterior angle of a triangle is always:", "Greater than either remote interior angle", "Less than any interior angle", "Equal to 90°", "Equal to the adjacent angle"),
            ("If an exterior angle is 130°, the sum of the remote interior angles is:", "130°", "50°", "180°", "260°"),
        ],
        flashcards=[
            ("Triangle Angle Sum Theorem", "The interior angles of a triangle sum to 180°"),
            ("Exterior Angle Theorem", "An exterior angle equals the sum of the two remote interior angles"),
            ("In a right triangle, what do the acute angles sum to?", "90° (complementary)"),
            ("Can a triangle have two obtuse angles?", "No — the sum would exceed 180°"),
            ("What is an exterior angle?", "An angle formed by one side of a triangle and the extension of an adjacent side"),
            ("What are remote interior angles?", "The two interior angles not adjacent to the exterior angle"),
            ("If angles are 45°, 45°, what is the third?", "90° (it is a right triangle)"),
            ("If angles are 60°, 60°, what is the third?", "60° (it is equiangular)"),
            ("What is a corollary?", "A statement that follows directly from a theorem"),
            ("Sum of exterior angles of any polygon?", "360°"),
        ],
        next_lesson_id="4.3"
    )
    
    write_lesson(4, "4.3", "Congruent Triangles",
        summary_body="""
<h3>Key Concepts: Congruent Triangles</h3>
<p><b>Congruent Triangles</b></p>
<p>Two triangles are <b>congruent</b> if all their corresponding sides and corresponding angles are congruent. When listing congruent triangles, the <b>order of vertices matters</b> — it shows which parts correspond.</p>

<p><b>CPCTC</b></p>
<p><b>Corresponding Parts of Congruent Triangles are Congruent</b> (CPCTC). Once two triangles are proven congruent, ALL corresponding parts are congruent.</p>

<p><b>Third Angles Theorem</b></p>
<p>If two angles of one triangle are congruent to two angles of another triangle, then the <b>third angles</b> are also congruent.</p>
""",
        questions=[
            ("Two triangles are congruent if:", "All corresponding sides and angles are congruent", "They have the same area", "They look similar", "They share one side"),
            ("CPCTC stands for:", "Corresponding Parts of Congruent Triangles are Congruent", "Central Point Creates Two Circles", "Complementary Parts Create Triangle Congruence", "Congruent Polygons Create Three Copies"),
            ("In △ABC ≅ △DEF, which side corresponds to AB?", "DE", "EF", "DF", "FD"),
            ("The Third Angles Theorem states:", "If two pairs of angles are congruent, the third pair is too", "All triangles have three angles", "Third angles are always 60°", "The largest angle is opposite the longest side"),
            ("Why does vertex order matter in congruence statements?", "It shows which parts correspond", "It determines the area", "It affects angle measures", "It is only for labeling"),
            ("If △PQR ≅ △XYZ, then ∠Q ≅:", "∠Y", "∠X", "∠Z", "∠P"),
            ("CPCTC is used after:", "Proving triangles are congruent", "Finding the area", "Measuring angles", "Drawing an altitude"),
        ],
        flashcards=[
            ("When are two triangles congruent?", "When all corresponding sides and angles are congruent"),
            ("What is CPCTC?", "Corresponding Parts of Congruent Triangles are Congruent"),
            ("Third Angles Theorem", "If two angles of one triangle equal two angles of another, the third angles are also equal"),
            ("In △ABC ≅ △DEF, AB corresponds to?", "DE"),
            ("In △ABC ≅ △DEF, ∠C corresponds to?", "∠F"),
            ("Why does vertex order matter?", "It establishes which sides and angles correspond"),
            ("When can you use CPCTC?", "After proving two triangles are congruent"),
            ("What must be true for all parts of congruent triangles?", "Every corresponding side and angle is congruent"),
            ("Is AAA enough to prove congruence?", "No — it only proves similarity, not congruence"),
            ("What is a congruence transformation?", "A transformation that preserves size and shape (reflection, rotation, translation)"),
        ],
        next_lesson_id="4.4"
    )
    
    write_lesson(4, "4.4", "Proving Congruence: SSS, SAS",
        summary_body="""
<h3>Key Concepts: Proving Congruence — SSS, SAS</h3>
<p><b>SSS (Side-Side-Side) Postulate</b></p>
<p>If three sides of one triangle are congruent to three sides of another triangle, the triangles are <b>congruent</b>.</p>

<p><b>SAS (Side-Angle-Side) Postulate</b></p>
<p>If two sides and the <b>included angle</b> of one triangle are congruent to two sides and the included angle of another triangle, the triangles are <b>congruent</b>.</p>
<ul>
<li>The <b>included angle</b> is the angle formed between the two given sides.</li>
</ul>

<p><b>Using SSS and SAS in Proofs</b></p>
<ol>
<li>Identify corresponding sides and angles from the given information.</li>
<li>Look for shared sides (Reflexive Property) or vertical angles.</li>
<li>Match three pairs: SSS or SAS.</li>
<li>State the congruence, then use CPCTC for further conclusions.</li>
</ol>
""",
        questions=[
            ("SSS requires how many pairs of congruent sides?", "Three", "Two", "One", "Four"),
            ("SAS requires:", "Two sides and the included angle to be congruent", "Two sides and any angle", "Three angles", "One side and two angles"),
            ("The included angle in SAS is:", "The angle between the two given sides", "Any angle of the triangle", "The largest angle", "The angle opposite the longest side"),
            ("If AB ≅ DE, BC ≅ EF, and AC ≅ DF, the triangles are congruent by:", "SSS", "SAS", "ASA", "AAS"),
            ("A shared side between two triangles is justified by:", "The Reflexive Property", "The Symmetric Property", "CPCTC", "The Transitive Property"),
            ("Can SSA (Side-Side-Angle) prove congruence?", "No — SSA is not a valid congruence method", "Yes always", "Only for right triangles", "Only for equilateral triangles"),
            ("After proving △ABC ≅ △DEF by SAS, you can conclude ∠C ≅ ∠F by:", "CPCTC", "SSS", "Reflexive Property", "The Triangle Angle Sum"),
        ],
        flashcards=[
            ("SSS Postulate", "If all 3 sides of one triangle ≅ all 3 sides of another, the triangles are congruent"),
            ("SAS Postulate", "If 2 sides and their included angle are congruent, the triangles are congruent"),
            ("What is an included angle?", "The angle formed between two given sides"),
            ("Is SSA a valid proof method?", "No — SSA (or ASS) does not prove congruence"),
            ("Reflexive Property in triangle proofs", "A shared side is congruent to itself (AB ≅ AB)"),
            ("After proving congruence, what allows further conclusions?", "CPCTC — Corresponding Parts of Congruent Triangles are Congruent"),
            ("How many pairs do you need for SSS?", "Three pairs of congruent sides"),
            ("How many pairs do you need for SAS?", "Two pairs of congruent sides + one pair of congruent included angles"),
            ("What should you look for in overlapping triangles?", "Shared sides (Reflexive Property) and vertical angles"),
            ("Does order matter when writing SSS or SAS?", "Yes — S's and A's must match the specific configuration shown"),
        ],
        next_lesson_id="4.5"
    )
    
    write_lesson(4, "4.5", "Proving Congruence: ASA, AAS",
        summary_body="""
<h3>Key Concepts: Proving Congruence — ASA, AAS</h3>
<p><b>ASA (Angle-Side-Angle) Postulate</b></p>
<p>If two angles and the <b>included side</b> of one triangle are congruent to two angles and the included side of another triangle, the triangles are <b>congruent</b>.</p>

<p><b>AAS (Angle-Angle-Side) Theorem</b></p>
<p>If two angles and a <b>non-included side</b> of one triangle are congruent to the corresponding parts of another triangle, the triangles are <b>congruent</b>.</p>

<p><b>Summary of Congruence Methods</b></p>
<ul>
<li>&#x2705; <b>SSS</b> — 3 sides</li>
<li>&#x2705; <b>SAS</b> — 2 sides + included angle</li>
<li>&#x2705; <b>ASA</b> — 2 angles + included side</li>
<li>&#x2705; <b>AAS</b> — 2 angles + non-included side</li>
<li>&#x274C; <b>SSA</b> — NOT valid</li>
<li>&#x274C; <b>AAA</b> — NOT valid (proves similarity only)</li>
</ul>
""",
        questions=[
            ("ASA requires:", "Two angles and the included side congruent", "Two angles and any side", "Three sides", "Two sides and the included angle"),
            ("AAS requires:", "Two angles and a non-included side congruent", "Two angles and the included side", "Three angles", "Two sides and any angle"),
            ("The included side in ASA is:", "The side between the two given angles", "The longest side", "Any side", "The hypotenuse"),
            ("Which is NOT a valid congruence method?", "AAA", "SSS", "SAS", "ASA"),
            ("How many valid triangle congruence postulates/theorems are there?", "Four (SSS, SAS, ASA, AAS)", "Three", "Five", "Six"),
            ("If ∠A ≅ ∠D, AB ≅ DE, and ∠B ≅ ∠E, the triangles are congruent by:", "ASA", "SAS", "SSS", "AAS"),
            ("Why does AAA not prove congruence?", "Triangles can have the same angles but different sizes", "Angles cannot be measured", "There are only two angles", "AAA only works for right triangles"),
        ],
        flashcards=[
            ("ASA Postulate", "Two angles and their included side congruent → triangles congruent"),
            ("AAS Theorem", "Two angles and a non-included side congruent → triangles congruent"),
            ("What is the included side?", "The side between the two given angles"),
            ("List all valid congruence methods.", "SSS, SAS, ASA, AAS (and HL for right triangles)"),
            ("Why is AAA not valid for congruence?", "Same angles can have different side lengths (similarity, not congruence)"),
            ("Why is SSA not valid?", "It can produce two different triangles (ambiguous case)"),
            ("Difference between ASA and AAS?", "ASA: side is between the angles; AAS: side is not between them"),
            ("What is HL?", "Hypotenuse-Leg: for right triangles, if hypotenuse and one leg are congruent"),
            ("After proving congruence with ASA, what follows?", "CPCTC — all other corresponding parts are congruent"),
            ("Can you use a mix of methods in one proof?", "Yes — you might use SAS in one step and CPCTC for the rest"),
        ],
        next_lesson_id="4.6"
    )
    
    write_lesson(4, "4.6", "Isosceles and Equilateral Triangles",
        summary_body="""
<h3>Key Concepts: Isosceles and Equilateral Triangles</h3>
<p><b>Isosceles Triangle Theorem</b></p>
<p>If two sides of a triangle are congruent, then the <b>angles opposite those sides</b> (base angles) are congruent.</p>

<p><b>Converse of Isosceles Triangle Theorem</b></p>
<p>If two angles of a triangle are congruent, then the <b>sides opposite those angles</b> are congruent.</p>

<p><b>Equilateral Triangle Corollaries</b></p>
<ul>
<li>A triangle is equilateral <b>if and only if</b> it is equiangular.</li>
<li>Each angle of an equilateral triangle measures <b>60°</b>.</li>
</ul>

<p><b>Parts of an Isosceles Triangle</b></p>
<ul>
<li><b>Legs</b>: The two congruent sides.</li>
<li><b>Base</b>: The non-congruent side.</li>
<li><b>Vertex angle</b>: The angle between the two legs.</li>
<li><b>Base angles</b>: The angles opposite the legs (always congruent).</li>
</ul>
""",
        questions=[
            ("The Isosceles Triangle Theorem states:", "Base angles of an isosceles triangle are congruent", "All angles are 60°", "The longest side is opposite the largest angle", "An isosceles triangle has no congruent sides"),
            ("If two angles of a triangle are congruent, the triangle is:", "Isosceles", "Scalene", "Obtuse", "Right"),
            ("Each angle of an equilateral triangle measures:", "60°", "90°", "45°", "120°"),
            ("The vertex angle of an isosceles triangle is:", "The angle between the two congruent sides", "Always 90°", "The smallest angle", "One of the base angles"),
            ("An equilateral triangle is also:", "Equiangular", "Scalene", "Obtuse", "Right"),
            ("The base of an isosceles triangle is:", "The non-congruent side", "The longest side always", "Either of the congruent sides", "The shortest side always"),
            ("If a triangle has angles of 70°, 70°, and 40°, it is:", "Isosceles", "Equilateral", "Scalene", "Right"),
        ],
        flashcards=[
            ("Isosceles Triangle Theorem", "If two sides are congruent, the angles opposite them are congruent"),
            ("Converse of Isosceles Triangle Theorem", "If two angles are congruent, the sides opposite them are congruent"),
            ("Angle measure of equilateral triangle", "60° for each angle"),
            ("Legs of an isosceles triangle", "The two congruent sides"),
            ("Base of an isosceles triangle", "The non-congruent side"),
            ("Vertex angle", "The angle formed between the two congruent legs"),
            ("Base angles", "The two congruent angles opposite the legs"),
            ("Equilateral ↔ Equiangular", "A triangle is equilateral if and only if it is equiangular"),
            ("If vertex angle = 40°, what are the base angles?", "Each is 70° (since 180° − 40° = 140°, divided by 2)"),
            ("Can an isosceles triangle be right?", "Yes — with angles 90°, 45°, 45°"),
        ],
        next_lesson_id="4.7"
    )
    
    write_lesson(4, "4.7", "Congruence Transformations",
        summary_body="""
<h3>Key Concepts: Congruence Transformations</h3>
<p><b>Rigid Motions (Isometries)</b></p>
<p>A transformation that preserves <b>distance and angle measure</b> is called a <b>rigid motion</b> or <b>isometry</b>. Rigid motions produce congruent figures.</p>

<p><b>Three Types of Rigid Motions</b></p>
<ul>
<li><b>Translation</b>: Slides a figure in a given direction by a given distance. Every point moves the same distance.</li>
<li><b>Reflection</b>: Flips a figure over a line (line of reflection). Each point is the same distance from the line on the opposite side.</li>
<li><b>Rotation</b>: Turns a figure around a fixed point (center of rotation) by a given angle.</li>
</ul>

<p><b>Key Properties</b></p>
<ul>
<li>All three rigid motions preserve side lengths, angle measures, and parallelism.</li>
<li>The pre-image and image are always <b>congruent</b>.</li>
<li>Compositions of rigid motions (doing two or more in sequence) also produce congruent figures.</li>
</ul>
""",
        questions=[
            ("A transformation that preserves distance and angle measure is called:", "A rigid motion (isometry)", "A dilation", "A projection", "A shear"),
            ("A translation:", "Slides every point the same distance in the same direction", "Flips a figure over a line", "Rotates a figure around a point", "Changes the size of a figure"),
            ("A reflection:", "Flips a figure over a line of reflection", "Slides a figure", "Enlarges a figure", "Rotates a figure"),
            ("A rotation:", "Turns a figure around a center point by an angle", "Slides a figure", "Flips a figure", "Stretches a figure"),
            ("Do rigid motions change the size of a figure?", "No — they preserve all distances", "Yes, they double the size", "Only rotations change size", "Only reflections change size"),
            ("The pre-image and image of a rigid motion are:", "Congruent", "Similar but not congruent", "Different in shape", "Always bigger"),
            ("Which is NOT a rigid motion?", "Dilation", "Translation", "Reflection", "Rotation"),
        ],
        flashcards=[
            ("What is a rigid motion?", "A transformation that preserves distance and angle measure (also called an isometry)"),
            ("What is a translation?", "A slide — every point moves the same distance in the same direction"),
            ("What is a reflection?", "A flip over a line of reflection"),
            ("What is a rotation?", "A turn around a center point by a given angle"),
            ("Do rigid motions preserve congruence?", "Yes — the image is always congruent to the pre-image"),
            ("What is preserved in a rigid motion?", "Side lengths, angle measures, and parallelism"),
            ("What is a composition of transformations?", "Performing two or more transformations in sequence"),
            ("Is a dilation a rigid motion?", "No — it changes the size of the figure"),
            ("What is the line of reflection?", "The line over which a figure is flipped — each point has a mirror image"),
            ("What is the center of rotation?", "The fixed point around which the figure is turned"),
        ],
        next_lesson_id="4.8"
    )
    
    write_lesson(4, "4.8", "Triangles and Coordinate Proof",
        summary_body="""
<h3>Key Concepts: Triangles and Coordinate Proof &#x2B50;</h3>
<p><b>Coordinate Proofs with Triangles</b></p>
<p>In a coordinate proof involving triangles, you place the triangle on the coordinate plane and use formulas to prove properties.</p>

<p><b>Strategies for Placing Triangles</b></p>
<ul>
<li>Place one vertex at the <b>origin (0, 0)</b>.</li>
<li>Align one side along the <b>x-axis or y-axis</b>.</li>
<li>Use variables (a, b, c) for coordinates to prove general results.</li>
<li>For isosceles triangles, use the y-axis as the line of symmetry.</li>
</ul>

<p><b>Common Proofs</b></p>
<ul>
<li><b>Prove a triangle is isosceles</b>: Show two sides have equal length using the Distance Formula.</li>
<li><b>Prove a triangle is right</b>: Show two sides have perpendicular slopes (product = &#x2212;1).</li>
<li><b>Find the centroid</b>: Average the coordinates: ((x&#x2081;+x&#x2082;+x&#x2083;)/3, (y&#x2081;+y&#x2082;+y&#x2083;)/3).</li>
</ul>
""",
        questions=[
            ("When placing a triangle for a coordinate proof, a good strategy is:", "Put one vertex at the origin and a side on an axis", "Use random coordinates", "Avoid the axes entirely", "Place all vertices at the same y-coordinate"),
            ("To prove a triangle is isosceles using coordinates:", "Show two sides have equal length with the distance formula", "Show all angles are 60°", "Show it has a right angle", "Show the perimeter is even"),
            ("The centroid of a triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃) is:", "((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)", "((x₁+x₂)/2, (y₁+y₂)/2)", "The origin", "(x₁, y₁)"),
            ("To prove a triangle is right using coordinates:", "Show two sides have slopes that multiply to −1", "Show all sides are equal", "Find the perimeter", "Show it has three acute angles"),
            ("Why use variables instead of numbers in coordinate proofs?", "To prove the result is true for ALL triangles, not just one example", "Variables are easier to calculate", "Numbers are not allowed", "Variables look more professional"),
            ("For an isosceles triangle coordinate proof, place the axis of symmetry along:", "The y-axis", "The x-axis only", "A diagonal", "No axis"),
            ("The centroid of (0,0), (6,0), (3,6) is:", "(3, 2)", "(3, 3)", "(6, 6)", "(0, 6)"),
        ],
        flashcards=[
            ("Best strategy for placing a triangle in a coordinate proof?", "Put one vertex at origin and one side along an axis"),
            ("How to prove a triangle is isosceles with coordinates?", "Use distance formula to show two sides are equal"),
            ("How to prove a triangle is right with coordinates?", "Show two sides have slopes whose product is −1"),
            ("Centroid formula", "((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3)"),
            ("What is the centroid?", "The point where the three medians of a triangle intersect"),
            ("Why use variable coordinates?", "To prove results that are true in general, not for specific cases"),
            ("What tools do you use in coordinate proofs?", "Distance formula, slope formula, midpoint formula"),
            ("Where is the centroid relative to the triangle?", "Always inside the triangle, 2/3 of the way from each vertex to the opposite midpoint"),
            ("Can coordinate proofs replace two-column proofs?", "They complement each other — some results are easier to prove one way"),
            ("What is the advantage of coordinate proofs?", "They use algebra to produce exact, systematic verification of geometric properties"),
        ],
        next_lesson_id=None
    )


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================
def main():
    generate_unit_1()
    generate_unit_2()
    generate_unit_3()
    generate_unit_4()
    print("\nDone! Units 1-4 generated successfully.")

if __name__ == "__main__":
    main()
