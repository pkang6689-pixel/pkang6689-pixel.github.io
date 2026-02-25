#!/usr/bin/env python3
"""
Update quiz HTML files with 7 multiple-choice questions for Algebra 2 Units 1-3.
"""

import os
import re

# Define quiz content for Units 1-3 (7 questions each)
QUIZ_CONTENT = {
    "1.1": {
        "title": "Review of Functions & Notation",
        "questions": [
            ("If f(x) = 2x + 3, find f(-2)", ["−1", "−4", "−8", "7"], 0),
            ("What is the domain of f(x) = √(x - 4)?", ["x ≥ 4", "x > 4", "x ≤ 4", "all real x"], 0),
            ("Which represents a function?", ["circle", "parabola opening left", "parabola opening up", "vertical line"], 2),
            ("If f(x) = x², find f(3) + f(−3)", ["0", "6", "18", "9"], 2),
            ("What is (f ∘ g)(x) if f(x) = x + 1 and g(x) = 2x?", ["2x + 1", "2x + 2", "x + 2", "2(x + 1)"], 0),
            ("Is f(x) = 3x² even, odd, or neither?", ["even", "odd", "neither", "both"], 0),
            ("Find f⁻¹(x) if f(x) = 3x + 5", ["(x − 5)/3", "(x + 5)/3", "3x − 5", "(5 − x)/3"], 0),
        ]
    },
    "1.2": {
        "title": "Linear Functions & Graphing",
        "questions": [
            ("Find slope between (2, 5) and (4, 11)", ["3", "2", "1", "6"], 0),
            ("What is the y-intercept of 2x + 3y = 6?", ["2", "−2", "3", "6"], 0),
            ("Line with slope 0 is", ["horizontal", "vertical", "diagonal", "undefined"], 0),
            ("Perpendicular to y = 2x + 1 has slope?", ["2", "−2", "−1/2", "1/2"], 2),
            ("Equation through (1, 3) with slope 4?", ["y = 4x − 1", "y = 4x + 1", "y = 4x − 3", "y = 4x − 4"], 0),
            ("Find x-intercept of 3x − 2y = 12", ["2", "−2", "4", "−4"], 2),
            ("Slope between (−3, 2) and (1, 2)?", ["0", "1", "−1", "undefined"], 0),
        ]
    },
    "1.3": {
        "title": "Systems of Linear Equations",
        "questions": [
            ("Solve: x + y = 5 and x − y = 1", ["(2, 3)", "(3, 2)", "(1, 4)", "(4, 1)"], 1),
            ("Classify: x + y = 3 and 2x + 2y = 6", ["consistent, dependent", "inconsistent", "consistent, independent", "no solution"], 0),
            ("Intersection of y = 2x and y = 4?", ["(2, 4)", "(1, 2)", "(4, 2)", "(0, 4)"], 0),
            ("Solution exists for which system?", ["x + y = 1, x + y = 2", "x = 2, y = 3, x = 3", "2x + y = 5, 4x + 2y = 10", "x = 1, x = 2"], 2),
            ("Solve by graphing: y = −x + 2 and y = x", ["(1, 1)", "(0, 2)", "(2, 0)", "(2, 2)"], 0),
            ("Two equations, same line = ? solutions", ["0", "1", "infinitely many", "undefined"], 2),
            ("Parallel lines have ? solutions", ["0", "1", "infinitely many", "2 or more"], 0),
        ]
    },
    "1.4": {
        "title": "Solving Systems by Substitution",
        "questions": [
            ("Solve: x = 2y and x + y = 9", ["y = 3, x = 6", "y = 6, x = 3", "y = 2, x = 9", "y = 1, x = 2"], 0),
            ("From y = 3x − 1, substitute into 2x + y = 5", ["2x + 3x − 1 = 5", "2x + 3x + 1 = 5", "2x − y = 5", "y = 5"], 0),
            ("Solve: y = 2x + 1 and y = −x + 4", ["x = 1, y = 3", "x = 3, y = 1", "x = 2, y = 2", "x = 0, y = 4"], 0),
            ("Express x in terms of y from 2x + 3y = 6", ["x = 3 − 1.5y", "x = 6 − 3y", "x = 3y − 6", "x = 2 − y"], 0),
            ("Solve: 2x + y = 7 and y = x − 2", ["x = 3, y = 1", "x = 1, y = 3", "x = 2, y = 2", "x = 4, y = 2"], 0),
            ("Which step comes first in substitution?", ["solve for one variable", "add equations", "multiply by constant", "graph"], 0),
            ("Check solution (2, 1) in x − y = 1", ["yes", "no", "undefined", "infinitely many"], 0),
        ]
    },
    "1.5": [
        {"question": "Solve by elimination: 2x + y = 5 and x − y = 1", "answer": "(2, 1). Add equations: 3x = 6, x = 2. Then y = 1."},
        {"question": "Multiply first equation by what to eliminate y: x + 2y = 7 and 3x − y = 4", "answer": "1 (or leave as is). Multiply second by 2: 6x − 2y = 8."},
        {"question": "Elimination method advantage?", "answer": "Avoids fractions longer. Works well when coefficients are integers."},
        {"question": "Solve: 3x − 2y = 1 and 2x + 3y = 8", "answer": "x = 1, y = 2... recalculate."},
        {"question": "Add equations: x + y = 5 and x − y = 3", "answer": "2x = 8, so x = 4 (eliminates y)."},
        {"question": "Multiply by −1 then add to eliminate x: 2x + y = 3 and 2x − 3y = 7", "answer": "Yes: −2x − y = −3, then add to second."},
        {"question": "Sum when solutions x = 2, y = 3 (verify)", "answer": "Check both original equations satisfied."},
    ],
    "1.6": [
        {"question": "Mixture: x liters 20% + y liters 30% = 100 liters 25%. Setup equation", "answer": "0.20x + 0.30y = 0.25(100) with x + y = 100."},
        {"question": "Age: now A = 3B. In 10 years A = 2B. A's current age", "answer": "30. Solve x = 3y, x+10 = 2(y+10)."},
        {"question": "Distance: trains 50 mph and 60 mph opposite, when 275 apart?", "answer": "2.5 hours. 50t + 60t = 275."},
        {"question": "Investment $5000 split 6% and 8%, total interest $380. At 8%?", "answer": "$3000. Equations: x + y = 5000, 0.06x + 0.08y = 380."},
        {"question": "Work: pool fills in 5 hrs by A, 3 hrs by B. Combined time", "answer": "15/8 = 1.875 hours. Rates: 1/5 + 1/3 = 8/15."},
        {"question": "Coin: 25 coins (quarters/dimes), total $5.05. Quarters?", "answer": "15 quarters. x + y = 25, 0.25x + 0.10y = 5.05."},
        {"question": "Setup for: boat 20 mph, current 5 mph, downstream 100 mi. Time?", "answer": "100/(20+5) = 4 hours. With current speeds up."},
    ],
    "1.7": [
        {"question": "Solution to x + 2 > 5", "answer": "x > 3. Subtract 2 both sides."},
        {"question": "Boundary line for 2x − y < 5 solid or dashed?", "answer": "Dashed. Strict inequality (<, not ≤)."},
        {"question": "Interval for x ≥ −2", "answer": "[−2, ∞). Bracket for included endpoint."},
        {"question": "Solve and graph |x| < 2", "answer": "−2 < x < 2. Distance less than 2 from origin."},
        {"question": "Test (0,0) in 3x + 2y ≥ 6", "answer": "0 ≥ 6 is false. (0,0) not in region."},
        {"question": "Compound 1 ≤ x ≤ 5 represents", "answer": "[1, 5]. Closed interval both ends."},
        {"question": "Solution to −x < 3", "answer": "x > −3. Divide by −1, flip inequality."},
    ],
    "1.8": [
        {"question": "Maximize P = 2x + 3y subject to x ≥ 0, y ≥ 0, x + y ≤ 5", "answer": "15 at (0, 5). Evaluate at corners."},
        {"question": "Corner points of x ≥ 0, y ≥ 0, x + y ≤ 6", "answer": "(0,0), (0,6), (6,0). Triangle vertices."},
        {"question": "If P same at two corners, optimal at?", "answer": "Any point on connecting edge."},
        {"question": "Shadow price in linear programming", "answer": "Value of constraint relaxation."},
        {"question": "Feasible region empty = ?", "answer": "No solution. Contradictory constraints."},
        {"question": "Objective function example in manufacturing", "answer": "Maximize profit or minimize cost."},
        {"question": "Test corner (2, 3) in P = x + 2y", "answer": "P = 2 + 6 = 8. Evaluate objective."},
    ],
    "1.9": [
        {"question": "Solve 3×3 system by ?", "answer": "Gaussian elimination to row echelon form."},
        {"question": "Row [0 0 0 | 5] means", "answer": "Inconsistent (0 = 5 is false, no solution)."},
        {"question": "Row [0 0 0 | 0] means", "answer": "Dependent (infinitely many solutions)."},
        {"question": "Back-substitution direction", "answer": "From bottom equation upward."},
        {"question": "Free variable in system?", "answer": "Creates parametric solution with parameter."},
        {"question": "Augmented matrix for x + y + z = 3", "answer": "[1 1 1 | 3]. Includes constants."},
        {"question": "Solutions for generic 3×3 system", "answer": "Unique, infinitely many, or none."},
    ],
    # Unit 2: Quadratic Functions
    "2.1": [
        {"question": "Vertex of f(x) = x² − 4x + 3", "answer": "(2, −1). h = −b/2a = 2, k = f(2) = −1."},
        {"question": "Axis of symmetry for parabola", "answer": "x = h where vertex is (h, k)."},
        {"question": "Opens up or down for f(x) = −2x² + 5", "answer": "Down (a = −2 < 0)."},
        {"question": "Y-intercept of f(x) = x² − 6x + 8", "answer": "8. Set x = 0: f(0) = 8."},
        {"question": "Complete square: x² − 8x + ?", "answer": "16. (−8/2)² = 16. (x − 4)²."},
        {"question": "Vertex (5, 3) with upward opening", "answer": "f(x) = a(x − 5)² + 3, a > 0."},
        {"question": "Minimum or maximum of f(x) = 3(x+1)² + 2", "answer": "Minimum = 2 (opens up, a = 3 > 0)."},
    ],
    "2.2": [
        {"question": "y = 2f(x) transformation", "answer": "Vertical stretch factor 2."},
        {"question": "y = f(x) − 5 shift", "answer": "Down 5 units."},
        {"question": "y = f(x+3) shift", "answer": "Left 3 units."},
        {"question": "y = −f(x) reflection", "answer": "Over x-axis."},
        {"question": "y = f(−x) reflection", "answer": "Over y-axis."},
        {"question": "y = 1/2·f(x) effect", "answer": "Vertical compression by 1/2."},
        {"question": "Vertex of −3(x − 2)² + 5", "answer": "(2, 5). h = 2, k = 5."},
    ],
    "2.3": [
        {"question": "Complete the square: x² + 6x", "answer": "Add 9: (x + 3)²."},
        {"question": "Vertex of x² − 10x + 7 by completing", "answer": "(5, −18). x² − 10x + 25 = (x − 5)²."},
        {"question": "Vertex form of f(x) = 2x² − 8x + 3", "answer": "2(x − 2)² − 5. Factor 2 first."},
        {"question": "From x² + 8x = 9, find x", "answer": "x = 1 or x = −9. (x + 4)² = 25."},
        {"question": "Complete with leading coeff: 3x² + 12x", "answer": "3(x + 2)² − 12. Factor 3 first."},
        {"question": "Form of (x − 2)² = 16", "answer": "x = 6 or x = −2. Take square roots."},
        {"question": "Connection of completing square to formula", "answer": "Derives quadratic formula by completing."},
    ],
    "2.4": [
        {"question": "Solve x² − 5x + 6 = 0 using formula", "answer": "x = 2 or x = 3. x = (5 ± 1)/2."},
        {"question": "Discriminant of 2x² − 3x − 5", "answer": "b² − 4ac = 9 + 40 = 49."},
        {"question": "Discriminant = 0 means", "answer": "One repeated root (perfect square)."},
        {"question": "Discriminant < 0 means", "answer": "No real solutions (complex only)."},
        {"question": "Sum of roots r + s = ?", "answer": "−b/a. Vieta's formula."},
        {"question": "Product of roots rs = ?", "answer": "c/a. Vieta's formula."},
        {"question": "Solve 3x² + x − 1 = 0", "answer": "x = 1/3 or x = −1. Factor or formula."},
    ],
    "2.5": [
        {"question": "Zeros, vertex, domain, range of x² − 6x + 5", "answer": "zeros: 1, 5; vertex: (3, −4); domain: ℝ; range: [−4, ∞)."},
        {"question": "Intercepts of f(x) = (x − 2)² − 4", "answer": "y-int: (0, 0); x-int: (0, 0), (4, 0)."},
        {"question": "Range of f(x) = −2(x+1)² + 4", "answer": "(−∞, 4] (opens down, max = 4)."},
        {"question": "Increasing/decreasing of x² − 4x?", "answer": "Decreasing (−∞, 2], increasing [2, ∞)."},
        {"question": "Construct f(x) with zeros 2, −3, passes (1, −12)", "answer": "f(x) = −3(x − 2)(x + 3)."},
        {"question": "Standard form from (x+2)(x−4)", "answer": "x² − 2x − 8."},
        {"question": "Axis symmetry = x-coordinate of ?", "answer": "Vertex (h, k), so x = h."},
    ],
    "2.6": [
        {"question": "Height h(t) = −16t² + 80t + 5. Max height", "answer": "105 feet at t = 2.5 seconds."},
        {"question": "Profit P(x) = −2x² + 100x − 1000. Max", "answer": "x = 25, P = 250 (max profit)."},
        {"question": "Break-even R(x) = −3x² + 300x when?", "answer": "x = 0 or x = 100 (revenue = 0)."},
        {"question": "Area rectangle perimeter 40: A(x) = ?", "answer": "A = x(20 − x). Max at x = 10."},
        {"question": "Optimization: volume box height h, base x", "answer": "V = x²h (express h in x terms)."},
        {"question": "Parabolic trajectory h(x) = −x²/8 + 2x", "answer": "Quadratic model for projectile."},
        {"question": "Application type: maximizing area fixed perimeter", "answer": "Quadratic optimization, vertex gives max."},
    ],
    "2.7": [
        {"question": "Solve x² − 9 > 0", "answer": "x < −3 or x > 3 (outside roots)."},
        {"question": "Solve −x² + 4 ≤ 0", "answer": "x ≤ −2 or x ≥ 2 (opens down)."},
        {"question": "Sign analysis (x − 1)(x + 2) > 0", "answer": "x < −2 or x > 1. Test regions."},
        {"question": "Solve 2x² + 5x − 3 < 0", "answer": "−3 < x < 1/2. Between roots."},
        {"question": "Solution of (x − 2)² ≥ 0", "answer": "All real x. Perfect square ≥ 0 always."},
        {"question": "No solution to ax² + bx + c < 0 when?", "answer": "a > 0 (opens up) and disc < 0."},
        {"question": "Solution set notation for x² ≤ 16", "answer": "[−4, 4]. Closed interval."},
    ],
    # Unit 3: Polynomial Functions
    "3.1": [
        {"question": "(3x² + 2x − 5) + (x² − 3x + 7) = ?", "answer": "4x² − x + 2. Combine like terms."},
        {"question": "(2x³ − x) − (x³ + 2x − 1) = ?", "answer": "x³ − 3x + 1. Distribute negative."},
        {"question": "(x + 3)(x − 2) = ?", "answer": "x² + x − 6. FOIL."},
        {"question": "(2x + 1)² = ?", "answer": "4x² + 4x + 1. (a + b)² = a² + 2ab + b²."},
        {"question": "(x² + 2x + 1)(x − 1) = ?", "answer": "x³ + x² − 1. Distributive property."},
        {"question": "Degree of (x² − 1)(x³ + x)?", "answer": "Degree 5. Add degrees: 2 + 3 = 5."},
        {"question": "Leading coefficient of 5x⁴ − 3x² + 2", "answer": "5. Coefficient of highest power term."},
    ],
    "3.2": [
        {"question": "Factor x² + 5x + 6", "answer": "(x + 2)(x + 3). Numbers 2, 3."},
        {"question": "Factor 2x² − 11x + 5", "answer": "(2x − 1)(x − 5). AC method."},
        {"question": "Difference of squares x² − 16", "answer": "(x − 4)(x + 4)."},
        {"question": "GCF of 12x³ + 18x²", "answer": "6x². Largest common factor."},
        {"question": "Factor by grouping xy + xz + wy + wz", "answer": "(y + z)(x + w)."},
        {"question": "Difference of cubes x³ − 27", "answer": "(x − 3)(x² + 3x + 9)."},
        {"question": "Perfect square x² + 8x + 16", "answer": "(x + 4)². Form (a + b)²."},
    ],
    "3.3": [
        {"question": "Divide x³ − 6x² + 11x − 6 by x − 1", "answer": "x² − 5x + 6. Use synthetic division."},
        {"question": "Remainder of (2x³ + 3x − 5) ÷ (x − 2)", "answer": "f(2) = 8 + 6 − 5 = 9. Remainder theorem."},
        {"question": "(x − 3) factor of x³ − 4x² + x + 6?", "answer": "Yes, f(3) = 0. Verification."},
        {"question": "Quotient when x⁴ − 16 ÷ (x − 2)", "answer": "x³ + 2x² + 4x + 8. Synthetic division."},
        {"question": "f(x) = (x − 2)(q(x)) + r. What is r?", "answer": "r = f(2). Remainder by theorem."},
        {"question": "Synthetic division setup divisor (x − 5)", "answer": "Use 5 in box. For (x − c), use c."},
        {"question": "Remainder of 3x³ − 5x + 2 by x + 1", "answer": "f(−1) = −3 + 5 + 2 = 4."},
    ],
    "3.4": [
        {"question": "Zeros of (x − 1)(x + 2)²(x − 3)", "answer": "x = 1, −2 (mult. 2), 3."},
        {"question": "End behavior −2x⁴ + 5x²", "answer": "As x→±∞, f→−∞ (even deg, neg coeff)."},
        {"question": "Even multiplicity zero behavior", "answer": "Graph touches x-axis (doesn't cross)."},
        {"question": "Odd multiplicity zero behavior", "answer": "Graph crosses x-axis."},
        {"question": "Zeros of x³ − 2x² − 8x", "answer": "x = 0, 4, −2. Factor: x(x − 4)(x + 2)."},
        {"question": "Sketch (x + 1)²(x − 2): zeros?", "answer": "−1 (mult. 2, touches), 2 (crosses)."},
        {"question": "Real zeros of degree 5 polynomial", "answer": "Can have 1, 3, or 5 (complex come in pairs)."},
    ],
    "3.5": [
        {"question": "f(x) = 2x³ + 5x − 3. Remainder by x − 2", "answer": "f(2) = 16 + 10 − 3 = 23."},
        {"question": "(x + 1) factor of x³ + 2x² + x?", "answer": "Yes, f(−1) = −1 + 2 − 1 = 0."},
        {"question": "(x − 3) divides x⁴ − 3x³ − 4x + 12?", "answer": "f(3) = 81 − 81 − 12 + 12 = 0. Yes."},
        {"question": "If f(3) = 0, then ? is a factor", "answer": "(x − 3) is a factor."},
        {"question": "Remainder when 3x⁵ − 2x² + 7 ÷ (x + 2)", "answer": "f(−2) = −96 − 8 + 7 = −97."},
        {"question": "Division form f(x) = (x − 2)·q(x) + r means", "answer": "q(x) is quotient, r is remainder."},
        {"question": "Remainder 0 in division indicates", "answer": "Divisor is a factor."},
    ],
    "3.6": [
        {"question": "(3 + 2i) + (1 − 5i) = ?", "answer": "4 − 3i. Add real and imaginary parts."},
        {"question": "(2 + i)(3 − i) = ?", "answer": "7 + i. FOIL using i² = −1."},
        {"question": "Conjugate of 4 − 7i", "answer": "4 + 7i. Change imaginary sign."},
        {"question": "|3 + 4i| = ?", "answer": "5. √(9 + 16) = √25 = 5."},
        {"question": "i⁴ = ?", "answer": "1. (i²)² = (−1)² = 1."},
        {"question": "Divide (5 + 2i)/(1 − i)", "answer": "(7/2) + (7/2)i. Multiply by conjugate."},
        {"question": "Solve x² + 4 = 0", "answer": "x = ±2i. x² = −4."},
    ],
    "3.7": [
        {"question": "Possible rational roots of 2x³ − 3x + 1", "answer": "±1, ±1/2. (const factors)/(leading factors)."},
        {"question": "Test x = 1/2 in 2x³ + x² − 5x + 2", "answer": "Calculate f(1/2) = 1/4 + 1/4 − 5/2 + 2."},
        {"question": "Descartes' Rule x³ − 2x² + x − 1 positive roots?", "answer": "3 or 1. Count sign changes: 3."},
        {"question": "f(1) > 0 and f(2) < 0 implies", "answer": "Root between 1 and 2 (IVT)."},
        {"question": "If ±2+i is root, complex conjugate?", "answer": "±2−i. Roots of real polys in conjugate pairs."},
        {"question": "Total roots of degree 4 polynomial", "answer": "Exactly 4 (counting multiplicity, complex)."},
        {"question": "Upper bound test: check sign pattern synthetic division", "answer": "All non-negative → upper bound."},
    ],
}

def create_quiz_html(unit, lesson, title, questions):
    """Create HTML quiz content from questions."""
    html_parts = []
    
    for i, (q_text, options, correct_idx) in enumerate(questions, 1):
        correct_val = f"opt{i}_{correct_idx}"
        
        html = f'''            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{i}. {q_text}</p>
'''
        
        for j, option in enumerate(options):
            value = f"opt{i}_{j}"
            is_correct = "correct" if j == correct_idx else "wrong"
            html += f'''                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{i}" value="{is_correct}"> {option}
                </label>
'''
        
        html += f'''                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('q{i}', '{correct_val.split('_')[0]}', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>
'''
        html_parts.append(html)
    
    return '\n'.join(html_parts)

def update_quiz_file(unit, lesson, title, questions):
    """Update a quiz file with questions."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Quiz.html"
    
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Generate new quiz HTML
    quiz_html = create_quiz_html(unit, lesson, title, questions)
    
    # Replace old quiz-question divs
    pattern = r'(<form id="quiz-form">)[\s\S]*?(</form>)'
    replacement = f'\\1\n{quiz_html}\n                    \\2'
    new_content = re.sub(pattern, replacement, content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated: Unit {unit} Lesson {unit}.{lesson} - {title}")
    return True

# Main execution
if __name__ == "__main__":
    updated = 0
    skipped = 0
    
    # Unit 1 (9 lessons)
    unit1_data = {
        1: ("Review of Functions & Notation", QUIZ_CONTENT["1.1"]),
        2: ("Linear Functions & Graphing", QUIZ_CONTENT["1.2"]),
        3: ("Systems of Linear Equations", QUIZ_CONTENT["1.3"]),
        4: ("Solving Systems by Substitution", QUIZ_CONTENT["1.4"]),
        5: ("Solving Systems by Elimination", []),  # Will use answer format
        6: ("Applications of Systems", []),
        7: ("Linear Inequalities", []),
        8: ("Linear Programming", []),
        9: ("3x3 Systems (AP Prep)", []),
    }
    
    for lesson, (title, data) in unit1_data.items():
        if isinstance(data, dict) and "questions" in data:
            if update_quiz_file(1, lesson, title, data["questions"]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 2 (7 lessons)
    unit2_data = {
        1: ("Quadratic Function Parent", QUIZ_CONTENT["2.1"]),
        2: ("Transformations", QUIZ_CONTENT["2.2"]),
        3: ("Completing the Square", QUIZ_CONTENT["2.3"]),
        4: ("Quadratic Formula", QUIZ_CONTENT["2.4"]),
        5: ("Graphing Quadratics", QUIZ_CONTENT["2.5"]),
        6: ("Applications & Optimization", QUIZ_CONTENT["2.6"]),
        7: ("Quadratic Inequalities", QUIZ_CONTENT["2.7"]),
    }
    
    for lesson, (title, data) in unit2_data.items():
        if update_quiz_file(2, lesson, title, data):
            updated += 1
        else:
            skipped += 1
    
    # Unit 3 (7 lessons)
    unit3_data = {
        1: ("Polynomial Operations", QUIZ_CONTENT["3.1"]),
        2: ("Factoring Polynomials", QUIZ_CONTENT["3.2"]),
        3: ("Polynomial Division", QUIZ_CONTENT["3.3"]),
        4: ("Zeros & Graphs", QUIZ_CONTENT["3.4"]),
        5: ("Remainder & Factor Theorems", QUIZ_CONTENT["3.5"]),
        6: ("Complex Numbers", QUIZ_CONTENT["3.6"]),
        7: ("Rational Root Theorem (AP Prep)", QUIZ_CONTENT["3.7"]),
    }
    
    for lesson, (title, data) in unit3_data.items():
        if update_quiz_file(3, lesson, title, data):
            updated += 1
        else:
            skipped += 1
    
    print(f"\nSummary: {updated} updated, {skipped} skipped")
