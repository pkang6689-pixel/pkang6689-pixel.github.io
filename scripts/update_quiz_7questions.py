#!/usr/bin/env python3
"""
Update all quiz files with 7 multiple-choice questions.
"""

import os
import re

# Quiz content: (7 questions per lesson, each is (question_text, [4_options], correct_index))
QUIZ_CONTENT = {
    "1.1": [
        ("If f(x) = 2x + 3, find f(-2)", ["-1", "-4", "-8", "7"], 0),
        ("What is the domain of f(x) = √(x - 4)?", ["x ≥ 4", "x > 4", "x ≤ 4", "all real x"], 0),
        ("Which represents a function?", ["circle", "parabola opening left", "parabola opening up", "vertical line"], 2),
        ("If f(x) = x², find f(3) + f(−3)", ["0", "6", "18", "9"], 2),
        ("What is (f ∘ g)(x) if f(x) = x + 1 and g(x) = 2x?", ["2x + 1", "2x + 2", "x + 2", "2(x + 1)"], 0),
        ("Is f(x) = 3x² even, odd, or neither?", ["even", "odd", "neither", "both"], 0),
        ("Find f⁻¹(x) if f(x) = 3x + 5", ["(x − 5)/3", "(x + 5)/3", "3x − 5", "(5 − x)/3"], 0),
    ],
    "1.2": [
        ("Find slope between (2, 5) and (4, 11)", ["3", "2", "1", "6"], 0),
        ("What is the y-intercept of 2x + 3y = 6?", ["2", "−2", "3", "6"], 0),
        ("Line with slope 0 is", ["horizontal", "vertical", "diagonal", "undefined"], 0),
        ("Perpendicular to y = 2x + 1 has slope?", ["2", "−2", "−1/2", "1/2"], 2),
        ("Equation through (1, 3) with slope 4?", ["y = 4x − 1", "y = 4x + 1", "y = 4x − 3", "y = 4x − 4"], 0),
        ("Find x-intercept of 3x − 2y = 12", ["2", "−2", "4", "−4"], 2),
        ("Slope between (−3, 2) and (1, 2)?", ["0", "1", "−1", "undefined"], 0),
    ],
    "1.3": [
        ("Solve: x + y = 5 and x − y = 1", ["(2, 3)", "(3, 2)", "(1, 4)", "(4, 1)"], 1),
        ("Classify: x + y = 3 and 2x + 2y = 6", ["consistent, dependent", "inconsistent", "consistent, independent", "no solution"], 0),
        ("Intersection of y = 2x and y = 4?", ["(2, 4)", "(1, 2)", "(4, 2)", "(0, 4)"], 0),
        ("Solution exists for which system?", ["x + y = 1, x + y = 2", "x = 2, y = 3, x = 3", "2x + y = 5, 4x + 2y = 10", "x = 1, x = 2"], 2),
        ("Solve by graphing: y = −x + 2 and y = x", ["(1, 1)", "(0, 2)", "(2, 0)", "(2, 2)"], 0),
        ("Two equations, same line = ? solutions", ["0", "1", "infinitely many", "undefined"], 2),
        ("Parallel lines have ? solutions", ["0", "1", "infinitely many", "2 or more"], 0),
    ],
    "1.4": [
        ("Solve: x = 2y and x + y = 9", ["y = 3, x = 6", "y = 6, x = 3", "y = 2, x = 9", "y = 1, x = 2"], 0),
        ("From y = 3x − 1, substitute into 2x + y = 5", ["2x + 3x − 1 = 5", "2x + 3x + 1 = 5", "2x − y = 5", "y = 5"], 0),
        ("Solve: y = 2x + 1 and y = −x + 4", ["x = 1, y = 3", "x = 3, y = 1", "x = 2, y = 2", "x = 0, y = 4"], 0),
        ("Express x in terms of y from 2x + 3y = 6", ["x = 3 − 1.5y", "x = 6 − 3y", "x = 3y − 6", "x = 2 − y"], 0),
        ("Solve: 2x + y = 7 and y = x − 2", ["x = 3, y = 1", "x = 1, y = 3", "x = 2, y = 2", "x = 4, y = 2"], 0),
        ("Which step comes first in substitution?", ["solve for one variable", "add equations", "multiply by constant", "graph"], 0),
        ("Check solution (2, 1) in x − y = 1", ["yes", "no", "undefined", "infinitely many"], 0),
    ],
    "1.5": [
        ("Solve by elimination: 2x + y = 5 and x − y = 1", ["(2, 1)", "(1, 2)", "(3, 0)", "(0, 3)"], 0),
        ("Multiply first equation by what: x + 2y = 7 and 3x − y = 4", ["2", "3", "−1", "1"], 0),
        ("Which is advantage of elimination?", ["avoids fractions", "faster with integers", "simpler graphically", "works for all systems"], 1),
        ("Solve: 3x − 2y = 1 and 2x + 3y = 8", ["(1, 1)", "(1, 2)", "(-1, 2)", "(2, 1)"], 1),
        ("Add equations: x + y = 5 and x − y = 3", ["2x = 8", "2x = 2", "2y = 8", "x + y = 8"], 0),
        ("Multiply second by −1 then add eliminates x: 2x + y = 3 and 2x − 3y = 7", ["yes", "no", "maybe", "need more info"], 0),
        ("For solution (2, 3) in 2x − y = 1", ["correct", "incorrect", "need both equations", "parallel"], 0),
    ],
    "1.6": [
        ("Mixture of 20% + 30% = 25% setup", ["0.20x + 0.30y = 0.25(100)", "0.20x + 0.30y = 25", "x + y = 100", "0.20 + 0.30 = 0.25"], 0),
        ("Age: A = 3B, in 10 years A = 2B. Current A?", ["30", "20", "40", "50"], 0),
        ("Trains 50&60 mph apart, when 275 apart?", ["2.5 hours", "2 hours", "3 hours", "1.5 hours"], 0),
        ("$5000 at 6% and 8%, total interest $380. At 8%?", ["$3000", "$2000", "$1500", "$2500"], 0),
        ("Pool A fills in 5 hrs, B in 3 hrs. Combined?", ["1.875 hours", "2 hours", "3 hours", "4 hours"], 0),
        ("25 coins (quarters/dimes), $5.05 total. Quarters?", ["15", "10", "20", "5"], 0),
        ("Boat 20 mph, current 5 mph, 100 mi downstream. Time?", ["4 hours", "5 hours", "3 hours", "6 hours"], 0),
    ],
    "1.7": [
        ("Solution to x + 2 > 5", ["x > 3", "x < 3", "x ≥ 3", "x ≤ 3"], 0),
        ("Boundary line for 2x − y < 5", ["dashed", "solid", "dotted", "removed"], 0),
        ("Interval for x ≥ −2", ["[−2, ∞)", "(−2, ∞)", "(−∞, −2]", "[−2, −1]"], 0),
        ("Solve and graph |x| < 2", ["−2 < x < 2", "−2 ≤ x ≤ 2", "x > −2", "x < 2"], 0),
        ("Test (0,0) in 3x + 2y ≥ 6", ["false", "true", "undefined", "impossible"], 0),
        ("Compound 1 ≤ x ≤ 5", ["[1, 5]", "(1, 5)", "[1, 5)", "(1,5]"], 0),
        ("Solution to −x < 3", ["x > −3", "x < −3", "x > 3", "x < 3"], 0),
    ],
    "1.8": [
        ("Max P = 2x + 3y subject to x≥0, y≥0, x+y≤5", ["15", "10", "8", "12"], 0),
        ("Corner points: x≥0, y≥0, x+y≤6", ["(0,0)(0,6)(6,0)", "(0,6)(6,0)(3,3)", "(0,0)(1,6)", "(6,6)(0,0)"], 0),
        ("Max at two corners then optimal at", ["edge connecting", "weighted average", "one corner", "no solution"], 0),
        ("Linear programming objective example", ["maximize profit", "minimize cost", "both", "optimize area"], 2),
        ("Feasible region empty means", ["no solution", "one solution", "many solutions", "unbounded"], 0),
        ("Test corner (2, 3) in P = x + 2y", ["8", "7", "5", "6"], 0),
        ("Optimal value in LP found at", ["vertices only", "anywhere in region", "center", "boundary lines"], 0),
    ],
    "1.9": [
        ("Solve 3×3 system by", ["row reduction", "substitution", "elimination", "all"], 3),
        ("Row [0 0 0 | 5] means", ["inconsistent", "dependent", "unique", "parametric"], 0),
        ("Row [0 0 0 | 0] means", ["inconsistent", "dependent", "unique", "impossible"], 1),
        ("Back-substitution goes", ["bottom to top", "top to bottom", "randomly", "sideways"], 0),
        ("Free variable creates", ["unique solution", "parametric form", "no solution", "none"], 1),
        ("Generic 3×3 system has", ["unique sol", "infinitely many", "no solution", "all three possible"], 3),
        ("Augmented matrix for x + y + z = 3", ["[1 1 1|3]", "[1 1 1]", "[3 3 3|3]", "[1 1 1|1]"], 0),
    ],
    "2.1": [
        ("Vertex of f(x) = x² − 4x + 3", ["(2, −1)", "(1, 0)", "(3, −1)", "(0, 3)"], 0),
        ("Axis of symmetry formula", ["x = −b/2a", "y = −b/2a", "x = b/2a", "x = a/b"], 0),
        ("Opens up or down: f(x) = −2x² + 5", ["down", "up", "sideways", "parabola doesn't open"], 0),
        ("Y-intercept of f(x) = x² − 6x + 8", ["8", "−6", "−8", "6"], 0),
        ("Complete square x² − 8x + ?", ["16", "4", "64", "8"], 0),
        ("Max/min of f(x) = 3(x+1)² + 2", ["max = 2", "min = 2", "none", "max = 3"], 1),
        ("Vertex (5, 3) with upward", ["f(x) = a(x−5)²+3, a>0", "f(x) = a(x+5)²−3", "f(x) = a(x−3)²+5", "none"], 0),
    ],
    "2.2": [
        ("y = 2f(x) transformation", ["stretch 2", "shift 2", "compress 2", "reflect"], 0),
        ("y = f(x) − 5 shift", ["down 5", "up 5", "left 5", "right 5"], 0),
        ("y = f(x+3) shift", ["left 3", "right 3", "up 3", "down 3"], 0),
        ("y = −f(x) reflection", ["x-axis", "y-axis", "origin", "none"], 0),
        ("y = f(−x) reflection", ["y-axis", "x-axis", "origin", "diagonal"], 0),
        ("y = 0.5f(x) effect", ["compress", "stretch", "shift", "reflect"], 0),
        ("Vertex of −3(x−2)²+5", ["(2, 5)", "(−2, 5)", "(5, 2)", "(−5, −2)"], 0),
    ],
    "2.3": [
        ("Complete: x² + 6x + ?", ["9", "3", "36", "6"], 0),
        ("Vertex of x² − 10x + 7", ["(5, −18)", "(−5, 18)", "(10, 7)", "(0, 7)"], 0),
        ("Vertex form of 2x² − 8x + 3", ["2(x−2)²−5", "2(x+2)²+3", "(x−4)²−1", "2(x−4)²+3"], 0),
        ("Solve x² + 8x = 9", ["x = 1 or −9", "x = 3 or 3", "x = −4 or 4", "x = 0"], 0),
        ("Complete with coeff: 3x² + 12x", ["3(x+2)²−12", "3(x+2)²", "3x(x+4)", "none"], 0),
        ("From (x−2)² = 16", ["x = 6 or −2", "x = 4 or 0", "x = 4", "x = −2"], 0),
        ("Completing square derives", ["quadratic formula", "slope", "vertex", "roots"], 2),
    ],
    "2.4": [
        ("Solve x² − 5x + 6 = 0", ["x = 2 or 3", "x = 1 or 6", "x = −2 or −3", "no real"], 0),
        ("Discriminant of 2x² − 3x − 5", ["49", "1", "−49", "9"], 0),
        ("Discriminant = 0 means", ["one root", "two roots", "no roots", "undefined"], 0),
        ("Discriminant < 0 means", ["complex roots", "real roots", "one root", "no roots"], 0),
        ("Sum of roots r + s = ?", ["−b/a", "c/a", "b/a", "a/c"], 0),
        ("Product of roots rs = ?", ["c/a", "−b/a", "b/a", "a/b"], 0),
        ("Solve 3x² + x − 1 = 0", ["x = 1/3 or −1", "x = 1 or 3", "x = −1/3 or 1", "x = 3 or 1"], 0),
    ],
    "2.5": [
        ("Zeros and vertex of x² − 6x + 5", ["zeros: 1,5; vertex: (3,−4)", "zeros: 2,3; vertex: (3,5)", "zeros: 0,5; vertex: (1,4)", "none"], 0),
        ("Y-intercept of (x−2)² − 4", ["0", "−4", "4", "2"], 0),
        ("Range of f(x) = −2(x+1)²+4", ["(−∞, 4]", "[4, ∞)", "(−∞, −2]", "[0, ∞)"], 0),
        ("Increasing/decreasing of x² − 4x", ["dec (−∞,2], inc [2,∞)", "inc all", "dec all", "neither"], 0),
        ("Zeros 2, −3, passes (1,−12)", ["f(x)=−3(x−2)(x+3)", "f(x)=(x−2)(x+3)", "f(x)=3(x+2)(x−3)", "none"], 0),
        ("Standard form (x+2)(x−4)", ["x² − 2x − 8", "x² + 2x − 8", "x² − 6x + 8", "x² + 6x − 8"], 0),
        ("Axis of symmetry = vertex", ["x-coordinate", "y-coordinate", "slope", "distance"], 0),
    ],
    "2.6": [
        ("Height h(t) = −16t² + 80t + 5. Max?", ["105 ft at t=2.5s", "80 ft at t=3s", "100 ft at t=2s", "5 ft at t=0"], 0),
        ("Profit P(x) = −2x² + 100x − 1000. Max?", ["x = 25, P = 250", "x = 50, P = 150", "x = 25, P = 1250", "x = 100, P = 0"], 0),
        ("Break-even R(x) = −3x² + 300x", ["x = 0 or 100", "x = 50 or 100", "x = 0 or 50", "never"], 0),
        ("Area rect, perim 40: max area", ["100", "80", "40", "160"], 0),
        ("Optimization steps", ["set up equation", "find max/min", "interpret", "all above"], 3),
        ("Optimization parabola vertex", ["maximum/minimum", "x-intercept", "slope", "asymptote"], 0),
        ("Application type fixed perim", ["maximize area", "minimize time", "maximize profit", "none"], 0),
    ],
    "2.7": [
        ("Solve x² − 9 > 0", ["x < −3 or x > 3", "−3 < x < 3", "always true", "no solution"], 0),
        ("Solve −x² + 4 ≤ 0", ["x ≤ −2 or x ≥ 2", "−2 ≤ x ≤ 2", "all x", "no solution"], 0),
        ("Sign analysis (x−1)(x+2) > 0", ["x < −2 or x > 1", "−2 < x < 1", "all x", "no solution"], 0),
        ("Solve 2x² + 5x − 3 < 0", ["−3 < x < 1/2", "x < −3 or x > 1/2", "all x", "no solution"], 0),
        ("Solution (x−2)² ≥ 0", ["all real x", "x ≥ 2", "x ≤ 2", "x = 2"], 0),
        ("No solution to ax²+bx+c < 0 when", ["a > 0 and disc < 0", "a < 0 and disc > 0", "disc = 0", "none"], 0),
        ("Solution x² ≤ 16 interval", ["[−4, 4]", "(−4, 4)", "(−∞, 4]", "[4, ∞)"], 0),
    ],
    "3.1": [
        ("(3x²+2x−5)+(x²−3x+7) = ?", ["4x²−x+2", "4x²+5x−12", "2x²−x−2", "4x²−x−2"], 0),
        ("(2x³−x)−(x³+2x−1) = ?", ["x³−3x+1", "x³−x−1", "3x³−3x", "x³−3x"], 0),
        ("(x+3)(x−2) = ?", ["x²+x−6", "x²−6", "x²+5x−6", "x²−x+6"], 0),
        ("(2x+1)² = ?", ["4x²+4x+1", "4x²+1", "4x²+2x+1", "4x²−4x+1"], 0),
        ("(x²+2x+1)(x−1) = ?", ["x³+x²−1", "x³−1", "x³+x−1", "x³+2x²+x"], 0),
        ("Degree of (x²−1)(x³+x)", ["degree 5", "degree 3", "degree 2", "degree 6"], 0),
        ("Leading coeff of 5x⁴−3x²+2", ["5", "−3", "2", "1"], 0),
    ],
    "3.2": [
        ("Factor x² + 5x + 6", ["(x+2)(x+3)", "(x+1)(x+6)", "(x+2)(x+2)", "(x+3)²"], 0),
        ("Factor 2x² − 11x + 5", ["(2x−1)(x−5)", "(2x−5)(x−1)", "(2x+1)(x+5)", "(x−1)(x−5)"], 0),
        ("Difference x² − 16", ["(x−4)(x+4)", "(x−4)²", "(x+4)²", "prime"], 0),
        ("GCF of 12x³ + 18x²", ["6x²", "6x", "2x²", "3x"], 0),
        ("Factor by grouping xy+xz+wy+wz", ["(y+z)(x+w)", "(x+w)(y+z)", "(x+y)(z+w)", "prime"], 0),
        ("Difference cubes x³ − 27", ["(x−3)(x²+3x+9)", "(x−3)³", "(x−3)(x²−3x+9)", "prime"], 0),
        ("Perfect square x² + 8x + 16", ["(x+4)²", "(x+8)²", "(x+2)²", "(x+16)"], 0),
    ],
    "3.3": [
        ("Divide x³−6x²+11x−6 by x−1", ["x²−5x+6", "x²−6x+11", "x²−7x+4", "x²+5x−6"], 0),
        ("Remainder (2x³+3x−5)÷(x−2)", ["9", "8", "11", "−3"], 0),
        ("(x−3) factor of x³−4x²+x+6?", ["yes", "no", "maybe", "undefined"], 0),
        ("Quotient x⁴−16÷(x−2)", ["x³+2x²+4x+8", "x³−2x²+4x−8", "x³+4x+8", "x³−4x"], 0),
        ("f(x)=(x−2)q(x)+r, then r = ?", ["f(2)", "f(−2)", "q(2)", "q(−2)"], 0),
        ("Synthetic div divisor (x−5)", ["use 5", "use −5", "use 1/5", "use 5x"], 0),
        ("Remainder 3x³−5x+2 by x+1", ["4", "0", "−6", "2"], 0),
    ],
    "3.4": [
        ("Zeros of (x−1)(x+2)²(x−3)", ["1, −2(m2), 3", "1, 2, 3", "−1, −2, −3", "0, 1, 2"], 0),
        ("End behavior −2x⁴+5x²", ["both →−∞", "both →+∞", "mixed", "undefined"], 0),
        ("Even multiplicity zero", ["touches", "crosses", "undefined", "skips"], 0),
        ("Odd multiplicity zero", ["crosses", "touches", "undefined", "skips"], 0),
        ("Zeros of x³−2x²−8x", ["0, 4, −2", "0, 2, 4", "1, 2, −4", "−1, 2, 3"], 0),
        ("Sketch (x+1)²(x−2): mult?", ["−1: mult 2", "−1: mult 1", "2: mult 2", "both 1"], 0),
        ("Degree 5 polynomial zeros", ["1, 3, or 5", "exactly 5", "2 or 4", "1 or 2"], 0),
    ],
    "3.5": [
        ("f(x)=2x³+5x−3. Remainder by x−2", ["23", "21", "25", "19"], 0),
        ("(x+1) factor of x³+2x²+x?", ["yes", "no", "maybe", "both"], 0),
        ("(x−3) divides x⁴−3x³−4x+12?", ["yes", "no", "maybe", "both"], 0),
        ("If f(3) = 0, then (x−3) is", ["factor", "not factor", "maybe", "asymptote"], 0),
        ("Remainder 3x⁵−2x²+7 by x+2", ["−97", "97", "−89", "89"], 0),
        ("Division f(x)=(x−2)q(x)+r", ["quotient q, remainder r", "only quotient", "only remainder", "neither"], 0),
        ("Remainder 0 in division", ["divisor is factor", "no divison", "error", "undefined"], 0),
    ],
    "3.6": [
        ("(3+2i)+(1−5i) = ?", ["4−3i", "2+7i", "4−7i", "0+0i"], 0),
        ("(2+i)(3−i) = ?", ["7+i", "5−i", "6−2i", "7+5i"], 0),
        ("Conjugate of 4−7i", ["4+7i", "−4−7i", "7−4i", "−4+7i"], 0),
        ("|3+4i| = ?", ["5", "7", "1", "12"], 0),
        ("i⁴ = ?", ["1", "−1", "i", "−i"], 0),
        ("Divide (5+2i)/(1−i)", ["7/2 + 7i/2", "3 + 2i", "2 + 7i/2", "7 + 3i"], 0),
        ("Solve x² + 4 = 0", ["x = ±2i", "x = ±2", "x = ±4i", "no solution"], 0),
    ],
    "3.7": [
        ("Rational roots of 2x³−3x+1", ["±1, ±1/2", "±1, ±2", "±1/2, ±1/3", "±2, ±3"], 0),
        ("Test x=1/2 in 2x³+x²−5x+2", ["equals 0", "positive", "negative", "undefined"], 0),
        ("Descartes' x³−2x²+x−1 positive", ["3 or 1", "2 or 0", "4 or 2", "5 or 3"], 0),
        ("f(1) > 0 and f(2) < 0", ["root bet 1&2", "no root", "root at 0", "undefined"], 0),
        ("If ±2+i root, conjugate", ["±2−i", "2±i", "∓2+i", "2±3i"], 0),
        ("Total roots degree 4", ["exactly 4", "2 to 4", "0 to 4", "at least 4"], 0),
        ("Upper bound test", ["all nonneg", "all neg", "mixed", "any pattern"], 0),
    ],
}

def create_quiz_html_questions(questions):
    """Generate HTML for quiz questions."""
    html_parts = []
    for i, (q_text, options, correct_idx) in enumerate(questions, 1):
        html = f'''            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{i}. {q_text}</p>
'''
        for j, option in enumerate(options):
            is_correct = "correct" if j == correct_idx else "wrong"
            html += f'''                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{i}" value="{is_correct}"> {option}
                </label>
'''
        html += f'''                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('q{i}', '{is_correct}', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>
'''
        html_parts.append(html)
    return '\n'.join(html_parts)

def update_quiz_file(unit, lesson, questions):
    """Update a quiz file with questions."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Quiz.html"
    
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Generate new quiz HTML
    quiz_html = create_quiz_html_questions(questions)
    
    # Replace old quiz-question divs (keep form tags)
    pattern = r'(<form id="quiz-form">\s*)(.*?)(\s*</form>)'
    replacement = f'\\1\n{quiz_html}\n                    \\3'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated: Unit {unit} Lesson {unit}.{lesson}")
    return True

# Main execution
if __name__ == "__main__":
    updated = 0
    
    for key, questions in QUIZ_CONTENT.items():
        unit = int(key.split('.')[0])
        lesson = int(key.split('.')[1])
        
        if update_quiz_file(unit, lesson, questions):
            updated += 1
    
    print(f"\nSummary: {updated} quiz files updated")
