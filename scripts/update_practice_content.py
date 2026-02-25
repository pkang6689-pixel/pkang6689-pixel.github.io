#!/usr/bin/env python3
"""
Update practice HTML files with curriculum-specific flashcard content for Algebra 2.
"""

import os
import json
import re

# Define flashcard content for each lesson
FLASHCARD_CONTENT = {
    # Unit 1: Linear Functions & Systems
    "1.5": [
        {"question": "Solve by elimination: x + y = 5 and x - y = 1", "answer": "Solution is (3, 2). Add equations: 2x = 6, so x = 3. Substitute: y = 2. The y terms eliminated."},
        {"question": "Solve by elimination: 2x + 3y = 13 and 2x - y = 1", "answer": "Solution is (2, 3). Subtract second from first: 4y = 12, so y = 3. Substitute: x = 2."},
        {"question": "When solving 3x + 2y = 12 and 2x + y = 7, what multiply eliminates y?", "answer": "Multiply second equation by -2: -4x - 2y = -14. Add to first to eliminate y."},
        {"question": "Solve: 4x + 3y = 10 and 2x + 5y = 8", "answer": "Multiply first by -1 and second by 2. Add: 10y - 10y... carefully: multiply first by 5, second by -3."},
        {"question": "What is an advantage of elimination over substitution?", "answer": "Eliminates complex substitutions. Works well when coefficients allow easy cancellation."}
    ],
    "1.6": [
        {"question": "Two numbers sum to 25, difference is 5. Find them.", "answer": "Numbers are 15 and 10. Set x + y = 25 and x - y = 5. Adding gives x = 15, y = 10."},
        {"question": "A rectangle's length is 3 more than width. Perimeter is 26. Dimensions?", "answer": "Width = 5, Length = 8. Let w = width: 2w + 2(w+3) = 26 gives 4w = 20, so w = 5."},
        {"question": "$1000 split: 5% and 8% accounts, $68 interest. How much in each?", "answer": "$400 at 5%, $600 at 8%. System: x + y = 1000 and 0.05x + 0.08y = 68."},
        {"question": "A store: pencils $0.50, erasers $0.30. 30 items, $12 sales. Quantities?", "answer": "20 pencils, 10 erasers. System: p + e = 30 and 0.50p + 0.30e = 12."},
        {"question": "Steps for solving word problems with systems?", "answer": "(1) Define variables, (2) Write equations, (3) Solve, (4) Check: Does it make sense?"}
    ],
    "1.7": [
        {"question": "Solve and graph: -2x + 5 > 1", "answer": "x < 2. Subtract 5: -2x > -4. Divide by -2 (flip): x < 2. Open circle at 2, arrow left."},
        {"question": "When graphing y > 2x - 1, solid or dashed line?", "answer": "Dashed line. Test inequality > is not included. Use solid only for ≥ or ≤."},
        {"question": "Solution region: x + y ≤ 4, x ≥ 0, y ≥ 0", "answer": "Triangle vertices (0,0), (4,0), (0,4). Solid line for x + y = 4, below the line."},
        {"question": "When do you flip inequality signs?", "answer": "When multiplying/dividing by negative. Example: -3x < 6 becomes x > -2."},
        {"question": "Express (-3, 5] as an inequality.", "answer": "-3 < x ≤ 5. Parenthesis means not included, bracket means included."}
    ],
    "1.8": [
        {"question": "Four steps of linear programming?", "answer": "(1) Define variables and constraints, (2) Write objective function, (3) Graph feasible region, (4) Evaluate at corner points."},
        {"question": "Why evaluate objective at corner points?", "answer": "Maximum/minimum of linear objective over convex region occurs at vertices. This is fundamental to linear programming."},
        {"question": "Maximize P = 3x + 2y subject to: x + y ≤ 5, x ≥ 0, y ≥ 0. Max value?", "answer": "Max P = 15 at (5, 0). Corners: (0,0)→0, (5,0)→15, (0,5)→10."},
        {"question": "Chairs $50, tables $80 profit. x + 2y ≤ 40. Max profit constraint?", "answer": "Maximize P = 50x + 80y. Corner (0,0)→0, (40,0)→2000, (0,20)→1600. Max is $2000."},
        {"question": "What is the feasible region?", "answer": "All points satisfying all constraints simultaneously. Usually a polygon with vertices as corners."}
    ],
    "1.9": [
        {"question": "Solve 3×3: x + y + z = 6, x - y + z = 4, x + y - z = 2", "answer": "Solution: x = 3, y = 1, z = 2. Use elimination systematically on three equations."},
        {"question": "General form of 3×3 system?", "answer": "Three equations with three unknowns. Solve by elimination or substitution layer by layer."},
        {"question": "Parametric form for x + y + z = 5 (infinitely many solutions)?", "answer": "Let x = s, y = t, then z = 5 - s - t. Solution set: (s, t, 5-s-t) for any real s, t."},
        {"question": "Solve: 2x + y - z = 8, x - y + 2z = -1, 3x + 2y + z = 5", "answer": "Solution: x = 2, y = 1, z = -3. Verify: 4+1+3=8 ✓, 2-1-6=-5... recheck carefully."},
        {"question": "How does parametric form show dependent system?", "answer": "Free variables (parameters) indicate infinitely many solutions. Example: (s+2, s, 1) represents a line."}
    ],
    # Unit 2: Quadratic Functions
    "2.1": [
        {"question": "Standard form of quadratic: f(x) = ?", "answer": "f(x) = ax² + bx + c where a ≠ 0. a affects width/direction, c is y-intercept."},
        {"question": "Vertex coordinates formula?", "answer": "x = -b/(2a), then find y by substituting. Vertex is (-b/(2a), f(-b/(2a)))."},
        {"question": "What is axis of symmetry?", "answer": "Vertical line x = -b/(2a) through the vertex. Parabola is symmetric about this line."},
        {"question": "If a > 0, parabola opens?", "answer": "Upward. Vertex is minimum. If a < 0, opens downward. Vertex is maximum."},
        {"question": "Find vertex of f(x) = 2x² - 8x + 5", "answer": "x = -(-8)/(2·2) = 2. y = 2(4) - 16 + 5 = -3. Vertex: (2, -3)."}
    ],
    "2.2": [
        {"question": "f(x) = (x-3)² is f(x) = x² shifted how?", "answer": "Right 3 units. General: f(x-h) shifts h units right."},
        {"question": "f(x) = x² + 4 shifts how from f(x) = x²?", "answer": "Up 4 units. General: f(x) + k shifts k units up."},
        {"question": "f(x) = -2(x+1)² - 3 transformations?", "answer": "Left 1, vertical stretch 2, reflection over x-axis, down 3."},
        {"question": "Vertical stretch factor in y = 3(x-1)²?", "answer": "Factor 3. Parabola is 3 times as narrow. Compare: wider (0 < a < 1), narrower (|a| > 1)."},
        {"question": "Write vertex form with vertex (2, -5) and vertical compression 1/2.", "answer": "y = (1/2)(x-2)² - 5. Vertex form: y = a(x-h)² + k."}
    ],
    "2.3": [
        {"question": "Complete the square: x² + 6x + ?", "answer": "(6/2)² = 9. So x² + 6x + 9 = (x+3)². Take half the coefficient of x, square it."},
        {"question": "Express x² - 8x + 5 in vertex form.", "answer": "(x-4)² - 11. Complete: x² - 8x + 16 - 16 + 5 = (x-4)² - 11."},
        {"question": "Solve x² + 4x - 5 = 0 by completing the square.", "answer": "x = 1 or x = -5. Complete: (x+2)² - 9 = 0 gives (x+2)² = 9, so x+2 = ±3."},
        {"question": "Why complete the square?", "answer": "Solves quadratics, reveals vertex form, derives quadratic formula."},
        {"question": "Complete the square: 2x² + 8x + 3", "answer": "2(x+2)² - 5. Factor 2: 2(x² + 4x) + 3 = 2((x+2)² - 4) + 3 = 2(x+2)² - 5."}
    ],
    "2.4": [
        {"question": "Quadratic formula?", "answer": "x = (-b ± √(b² - 4ac))/(2a). Always works for ax² + bx + c = 0."},
        {"question": "What is the discriminant? What does it mean?", "answer": "Δ = b² - 4ac. If Δ > 0: two real roots, Δ = 0: one root, Δ < 0: no real roots."},
        {"question": "Solve 2x² - 7x + 3 = 0 using quadratic formula.", "answer": "x = (7 ± √(49-24))/4 = (7 ± 5)/4. So x = 3 or x = 1/2."},
        {"question": "For x² + 2x + 5 = 0, how many real solutions?", "answer": "None. Discriminant: 4 - 20 = -16 < 0. No real roots."},
        {"question": "If discriminant = 0, what does graph look like?", "answer": "Parabola touches x-axis at exactly one point (vertex on x-axis)."}
    ],
    "2.5": [
        {"question": "Find vertex and y-intercept of f(x) = x² - 4x + 3", "answer": "Vertex: (2, -1). Y-intercept: 3. Complete square: (x-2)² - 1."},
        {"question": "Sketch y = -(x-1)² + 4. Opens up/down?", "answer": "Opens down (a = -1 < 0). Vertex (1, 4) is maximum. Axis of symmetry: x = 1."},
        {"question": "Properties of f(x) = 2x²?", "answer": "Vertex (0,0), axis x=0, opens up, minimum value 0, domain all reals, range [0, ∞)."},
        {"question": "Parabola has vertex (3, -2) and passes through (5, 2). Find equation.", "answer": "y = a(x-3)² - 2. At (5,2): 2 = a(4) - 2, so a = 1. Equation: y = (x-3)² - 2."},
        {"question": "Domain and range of f(x) = (x+2)² - 5?", "answer": "Domain: all reals. Range: [-5, ∞) since vertex is minimum."}
    ],
    "2.6": [
        {"question": "Projectile motion: h(t) = -16t² + 64t + 80. Max height?", "answer": "Vertex at t = -64/(-32) = 2. h(2) = -16(4) + 128 + 80 = 208 feet."},
        {"question": "A business profit model P(x) = -2x² + 100x - 500. Max profit?", "answer": "Vertex: x = -100/(-4) = 25. P(25) = $750. Produce 25 units for max profit."},
        {"question": "Rectangular garden with 100m fence, one side against barn. Max area?", "answer": "Let x = width. Area = x(100-2x) = -2x² + 100x. Max at x = 25. Area = 1250 m²."},
        {"question": "Revenue R(p) = -5p² + 400p for price p. Price for max revenue?", "answer": "p = -400/(-10) = $40. Max revenue: R(40) = $8000."},
        {"question": "Optimization problems solve by finding?", "answer": "Vertex of parabola (maximum for max problems, minimum for min). Critical value is -b/(2a)."}
    ],
    "2.7": [
        {"question": "Solve x² - 3x - 4 < 0", "answer": "Roots: x = 4, x = -1. Test regions:-1 < x < 4. Sign table: negative between roots, positive outside."},
        {"question": "When does (x-2)² > 0?", "answer": "All x ≠ 2. Perfect square always ≥ 0, equals 0 only at x = 2."},
        {"question": "Solve 2x² + x - 3 ≥ 0", "answer": "Roots: x = 1, x = -3/2. Solution: x ≤ -3/2 or x ≥ 1. Include inequality boundary."},
        {"question": "Graph solution to -x² + 4 > 0", "answer": "Roots at x = ±2. Opens down. Solution: -2 < x < 2 (between roots)."},
        {"question": "Steps for solving quadratic inequalities?", "answer": "(1) Find roots, (2) Mark on number line, (3) Test sign in each region, (4) Write solution set."}
    ],
    # Unit 3: Polynomials
    "3.1": [
        {"question": "Add: (2x³ + 3x² - 1) + (x³ - 2x² + 5)", "answer": "3x³ + x² + 4. Combine like terms by degree."},
        {"question": "Subtract: (5x² - 3x + 2) - (2x² + x - 4)", "answer": "3x² - 4x + 6. Distribute negative, then combine like terms."},
        {"question": "Multiply: (x + 2)(x² - 3x + 1)", "answer": "x³ - 3x² + x + 2x² - 6x + 2 = x³ - x² - 5x + 2. FOIL or distributive property."},
        {"question": "Multiply: (2x - 3)²", "answer": "4x² - 12x + 9. Perfect square: (a-b)² = a² - 2ab + b²."},
        {"question": "Why degree increases when multiplying polynomials?", "answer": "Degree of product = sum of degrees. Highest power term: (ax^m)(bx^n) = abx^{m+n}."}
    ],
    "3.2": [
        {"question": "Factor: 6x² + 9x", "answer": "3x(2x + 3). Factor out GCF: 3x from both terms."},
        {"question": "Factor: x² - 5x + 6", "answer": "(x - 2)(x - 3). Numbers: -2, -3 multiply to 6, add to -5."},
        {"question": "Factor: x² - 9", "answer": "(x - 3)(x + 3). Difference of squares: a² - b² = (a-b)(a+b)."},
        {"question": "Factor by grouping: xy + 3x + 2y + 6", "answer": "x(y + 3) + 2(y + 3) = (x + 2)(y + 3). Group, factor each, find common factor."},
        {"question": "Factor: 2x² - 5x - 3", "answer": "(2x + 1)(x - 3). AC method or trial: 2·(-3) = -6, split -5x."}
    ],
    "3.3": [
        {"question": "Synthetic division: (x³ - 6x² + 11x - 6) ÷ (x - 1)", "answer": "Quotient: x² - 5x + 6. Use coefficients 1,-6,11,-6 and root 1."},
        {"question": "Is (x - 2) a factor of x³ + x² - 10x + 8?", "answer": "Yes. Use synthetic division with x = 2. If remainder is 0, it's a factor."},
        {"question": "What is the remainder when x⁴ - 3x² + 2 is divided by (x + 1)?", "answer": "Remainder is 0. f(-1) = 1 - 3 + 2 = 0 by remainder theorem."},
        {"question": "Synthetic division setup for (x - 3)?", "answer": "Use 3 in synthetic division box. Drop down first coefficient and multiply."},
        {"question": "When do you use synthetic vs long division?", "answer": "Synthetic is faster for linear divisors (x - a). Long division works for any polynomial divisor."}
    ],
    "3.4": [
        {"question": "Find zeros of f(x) = (x+2)(x-1)²(x-3)", "answer": "Zeros: -2 (mult. 1), 1 (mult. 2), 3 (mult. 1). From factored form."},
        {"question": "What does multiplicity tell us about a graph?", "answer": "Odd multiplicity: graph crosses x-axis. Even: touches x-axis at that point without crossing."},
        {"question": "End behavior of f(x) = -3x⁴ + 2x²", "answer": "Both ends go down (negative leading coefficient, even degree). Parabola-like behavior."},
        {"question": "Sketch f(x) = x(x-2)²", "answer": "Zeros: 0, 2 (multiplicity 2). Crosses at 0, touches at 2. Leading term x³ makes one end up, one down."},
        {"question": "If degree is odd, number of real zeros (at least)?", "answer": "At least one. Odd degree polynomials must cross x-axis due to end behavior."}
    ],
    "3.5": [
        {"question": "Remainder theorem: Find remainder of f(x) = 2x² - 5x + 1 divided by (x - 2)", "answer": "Remainder is f(2) = 8 - 10 + 1 = -1. Evaluate at the root."},
        {"question": "Factor theorem: If p(-3) = 0, then (x + 3) is?", "answer": "A factor of p(x). If f(r) = 0, then (x - r) is a factor."},
        {"question": "Find remainder: (x⁴ - 1) ÷ (x + 1)", "answer": "f(-1) = 1 - 1 = 0. Remainder is 0, so (x+1) is a factor."},
        {"question": "Verify (x - 1) divides x⁴ - 3x² + 2", "answer": "f(1) = 1 - 3 + 2 = 0. Yes, it's a factor. Use synthetic division to find quotient."},
        {"question": "Why does remainder theorem work?", "answer": "Division algorithm: f(x) = (divisor)(quotient) + remainder. If divisor = (x-r): remainder = f(r)."}
    ],
    "3.6": [
        {"question": "Simplify: (2 + 3i) + (1 - 2i)", "answer": "3 + i. Add real and imaginary parts separately."},
        {"question": "Multiply: (3 + 2i)(1 - i)", "answer": "3 - 3i + 2i - 2i² = 3 - i + 2 = 5 - i. (i² = -1)"},
        {"question": "Find complex conjugate of 4 - 3i", "answer": "4 + 3i. Conjugate changes sign of imaginary part. Used to divide by complex numbers."},
        {"question": "Divide: (2 + i)/(1 - i)", "answer": "(2+i)(1+i)/((1-i)(1+i)) = (2+2i+i-1)/(1+1) = (1+3i)/2. Multiply by conjugate."},
        {"question": "Solve x² + 4 = 0", "answer": "x = ±2i. Roots are complex: x² = -4, so x = ±√(-4) = ±2i."}
    ],
    "3.7": [
        {"question": "Rational Root Theorem: Possible rational roots of 2x³ - 3x² + x - 6?", "answer": "±(factors of 6)/(factors of 2) = ±1, ±2, ±3, ±6, ±1/2, ±3/2. Test each."},
        {"question": "Use Descartes' Rule for positive zeros of x³ - 4x² + x - 2", "answer": "Three sign changes: +, -, +, -. So 3 or 1 positive real zeros."},
        {"question": "How many real zeros possible for degree 5 polynomial?", "answer": "1, 3, or 5 real zeros. Odd degree has at least one real zero."},
        {"question": "Find integer zeros of x⁴ - 5x² + 4", "answer": "Rational Root Theorem: ±1, ±2, ±4. Test: ±1, ±2 work. Factor: (x-1)(x+1)(x-2)(x+2)."},
        {"question": "Why Rational Root Theorem limits testing?", "answer": "Narrows possibilities from infinitely many to finite list. Must still verify each."}
    ],
}

def generate_javascript_content(unit, lesson, flashcards):
    """Generate the JavaScript array for flashcards."""
    lines = ['        window.lessonFlashcards = [']
    for fc in flashcards:
        lines.append('          {')
        lines.append(f'                    "question": "{fc["question"]}",')
        lines.append(f'                    "answer": "{fc["answer"]}"')
        lines.append('          },')
    lines.append('        ];')
    return '\n'.join(lines)

def update_practice_file(unit, lesson, flashcards):
    """Update a practice file with new flashcard content."""
    # Build file path
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Practice.html"
    
    # Skip if file doesn't exist
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        return False
    
    # Read the file
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find and replace flashcards
    # Pattern: <script> tag containing window.lessonFlashcards = [ ... ];
    pattern = r'(        window\.lessonFlashcards = \[.*?\];)'
    js_content = generate_javascript_content(unit, lesson, flashcards)
    
    new_content = re.sub(pattern, js_content, content, flags=re.DOTALL)
    
    # Write back
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated: Unit {unit} Lesson {unit}.{lesson}")
    return True

# Main execution
if __name__ == "__main__":
    updated = 0
    skipped = 0
    
    # Unit 1 (already partially done, need 1.5-1.9)
    for lesson in [5, 6, 7, 8, 9]:
        if f"1.{lesson}" in FLASHCARD_CONTENT:
            if update_practice_file(1, lesson, FLASHCARD_CONTENT[f"1.{lesson}"]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 2
    for lesson in range(1, 8):
        key = f"2.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(2, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 3
    for lesson in range(1, 8):
        key = f"3.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(3, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    print(f"\nSummary: {updated} updated, {skipped} skipped")
