#!/usr/bin/env python3
"""Generate real content for Precalculus Unit 2: Linear & Quadratic Functions (9 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "precalculus_lessons.json")
COURSE = "Precalculus"

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for qi, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2, "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": COURSE,
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# ── 2.1 Linear Equations & Graphs ──
k, v = build_lesson(2, 1, "Linear Equations & Graphs",
    "<h3>Linear Equations & Graphs</h3>"
    "<p>A <b>linear equation</b> in two variables has the form Ax + By = C (standard form) or y = mx + b (slope-intercept form).</p>"
    "<ul><li><b>Slope-intercept form:</b> y = mx + b. m = slope, b = y-intercept.</li>"
    "<li><b>Point-slope form:</b> y − y₁ = m(x − x₁). Useful when you know a point and the slope.</li>"
    "<li><b>Standard form:</b> Ax + By = C. A, B, C are integers, A ≥ 0.</li>"
    "<li><b>Slope:</b> m = (y₂ − y₁)/(x₂ − x₁) — the rate of change.</li>"
    "<li><b>Horizontal line:</b> y = c (slope = 0). <b>Vertical line:</b> x = c (slope undefined).</li></ul>",
    [
        ("Slope-Intercept Form", "y = mx + b; m is the slope and b is the y-intercept."),
        ("Point-Slope Form", "y − y₁ = m(x − x₁); used when a point (x₁, y₁) and slope m are known."),
        ("Slope Formula", "m = (y₂ − y₁)/(x₂ − x₁); measures the steepness and direction of a line."),
        ("Standard Form", "Ax + By = C; A, B, C are integers with A ≥ 0."),
        ("Horizontal vs. Vertical Lines", "y = c is horizontal (slope 0); x = c is vertical (slope undefined)."),
    ],
    [
        ("The slope of the line through (1,3) and (4,9) is:", ["3", "*2", "6", "1"],
         "m = (9−3)/(4−1) = 6/3 = 2."),
        ("y = 3x − 7 has slope:", ["−7", "7", "*3", "−3"],
         "In y = mx + b, m = 3."),
        ("y = 3x − 7 has y-intercept:", ["3", "*(0, −7)", "(−7, 0)", "7"],
         "b = −7, so the y-intercept is (0, −7)."),
        ("A horizontal line has slope:", ["Undefined", "1", "*0", "∞"],
         "Horizontal lines have zero slope (no vertical change)."),
        ("A vertical line has slope:", ["0", "1", "*Undefined", "∞"],
         "Vertical lines have undefined slope (zero horizontal change)."),
        ("Point-slope form for slope 4 through (2, 5):", ["y = 4x + 5", "y − 5 = 2(x − 4)", "*y − 5 = 4(x − 2)", "y − 2 = 4(x − 5)"],
         "y − y₁ = m(x − x₁) → y − 5 = 4(x − 2)."),
        ("Convert y = 2x + 3 to standard form:", ["2x + y = 3", "*2x − y = −3 or equivalently −2x + y = 3", "x − 2y = 3", "y − 2x = −3"],
         "Rearrange: −2x + y = 3 or 2x − y = −3."),
        ("The x-intercept of y = 2x − 6 is:", ["(0, −6)", "*( 3, 0)", "(−6, 0)", "(6, 0)"],
         "Set y = 0: 0 = 2x − 6 → x = 3."),
        ("Two points determine:", ["*Exactly one line (if distinct)", "No line", "Infinitely many lines", "A parabola"],
         "Two distinct points define a unique line."),
        ("Slope represents:", ["The y-intercept", "The x-intercept", "*The rate of change (rise over run)", "The midpoint"],
         "m = rise/run = change in y / change in x."),
        ("y = −x + 4 has slope:", ["4", "1", "*−1", "0"],
         "The coefficient of x is −1."),
        ("Parallel to y = 3x + 1 through (0, 5):", ["y = 5x + 3", "*y = 3x + 5", "y = −(1/3)x + 5", "y = 3x + 1"],
         "Same slope (3), different intercept: y = 3x + 5."),
        ("Perpendicular to y = 2x has slope:", ["2", "*−1/2", "1/2", "−2"],
         "Perpendicular slope = negative reciprocal: −1/2."),
        ("The line y = 4 is:", ["*Horizontal", "Vertical", "Diagonal", "Undefined"],
         "y = constant → horizontal line."),
        ("The line x = −3 is:", ["Horizontal", "*Vertical", "Has slope 0", "Has slope −3"],
         "x = constant → vertical line."),
        ("Find the equation through (1, 2) and (3, 8):", ["y = 2x", "*y = 3x − 1", "y = 3x + 1", "y = x + 1"],
         "m = (8−2)/(3−1) = 3. y − 2 = 3(x−1) → y = 3x − 1."),
        ("Lines with the same slope are:", ["Perpendicular", "*Parallel (or identical)", "Always intersecting", "Vertical"],
         "Same slope, different intercepts → parallel."),
        ("The midpoint of (2, 4) and (6, 10) is:", ["(4, 7)", "*(4, 7)", "(8, 14)", "(2, 3)"],
         "Midpoint = ((2+6)/2, (4+10)/2) = (4, 7)."),
        ("A line with m > 0 goes:", ["Down from left to right", "*Up from left to right", "Horizontal", "Vertical"],
         "Positive slope means the line rises."),
        ("A line with m < 0 goes:", ["*Down from left to right", "Up from left to right", "Horizontal", "Vertical"],
         "Negative slope means the line falls."),
    ]
)
lessons[k] = v

# ── 2.2 Slope, Intercepts, Parallel/Perpendicular ──
k, v = build_lesson(2, 2, "Slope, Intercepts, and Parallel/Perpendicular Lines",
    "<h3>Slope, Intercepts, and Parallel/Perpendicular Lines</h3>"
    "<p>Understanding slope relationships is key for many Precalculus topics.</p>"
    "<ul><li><b>Parallel lines:</b> Same slope: m₁ = m₂.</li>"
    "<li><b>Perpendicular lines:</b> Slopes are negative reciprocals: m₁ · m₂ = −1.</li>"
    "<li><b>Finding intercepts:</b> x-intercept: set y = 0. y-intercept: set x = 0.</li>"
    "<li><b>Slope from standard form:</b> Ax + By = C → m = −A/B.</li></ul>",
    [
        ("Parallel Lines", "Lines with equal slopes: m₁ = m₂ (and different y-intercepts)."),
        ("Perpendicular Lines", "Lines whose slopes are negative reciprocals: m₁ · m₂ = −1."),
        ("x-intercept", "The point where the line crosses the x-axis; found by setting y = 0."),
        ("y-intercept", "The point where the line crosses the y-axis; found by setting x = 0."),
        ("Slope from Standard Form", "For Ax + By = C, the slope is m = −A/B."),
    ],
    [
        ("Two lines are parallel if:", ["Their slopes multiply to −1", "*Their slopes are equal", "They share the same y-intercept", "One is horizontal and one is vertical"],
         "Parallel lines never intersect and have the same slope."),
        ("Two lines are perpendicular if:", ["Their slopes are equal", "*Their slopes multiply to −1 (negative reciprocals)", "They are parallel", "Both are vertical"],
         "Perpendicular lines meet at 90°; m₁·m₂ = −1."),
        ("The negative reciprocal of 3 is:", ["3", "1/3", "*−1/3", "−3"],
         "Flip and negate: 3 → −1/3."),
        ("The negative reciprocal of −2/5 is:", ["2/5", "−5/2", "*5/2", "−2/5"],
         "Flip −2/5 to −5/2, then negate: 5/2."),
        ("3x + 4y = 12. The slope is:", ["3/4", "*−3/4", "4/3", "−4/3"],
         "m = −A/B = −3/4."),
        ("3x + 4y = 12. The y-intercept is:", ["(4, 0)", "*(0, 3)", "(0, 12)", "(12, 0)"],
         "Set x = 0: 4y = 12 → y = 3."),
        ("3x + 4y = 12. The x-intercept is:", ["*(4, 0)", "(0, 4)", "(3, 0)", "(12, 0)"],
         "Set y = 0: 3x = 12 → x = 4."),
        ("Line parallel to y = −2x + 5 through (1, 3):", ["y = (1/2)x + 5/2", "*y = −2x + 5... wait: y − 3 = −2(x−1) → y = −2x + 5", "y = 2x + 1", "y = −2x + 3"],
         "Same slope −2: y − 3 = −2(x−1) → y = −2x + 5."),
        ("Line perpendicular to y = (1/3)x + 2 through (0, 0):", ["y = (1/3)x", "*y = −3x", "y = 3x", "y = (−1/3)x"],
         "Perpendicular slope = −3. Through origin: y = −3x."),
        ("A horizontal line and a vertical line are:", ["Parallel", "*Perpendicular", "Neither", "Undefined"],
         "They meet at a right angle."),
        ("Lines y = 5x + 1 and y = 5x − 7 are:", ["*Parallel", "Perpendicular", "Identical", "Intersecting at one point"],
         "Same slope (5), different y-intercepts → parallel."),
        ("Lines y = 2x + 3 and y = −(1/2)x + 1 are:", ["Parallel", "*Perpendicular", "Identical", "Neither"],
         "2 × (−1/2) = −1 → perpendicular."),
        ("Can two vertical lines be perpendicular?", ["Yes", "*No — both are vertical (undefined slope), so they're parallel", "Sometimes", "Always"],
         "Two vertical lines are parallel (or identical)."),
        ("Find the slope of the line through (−1, 4) and (3, −8):", ["3", "*−3", "−1/3", "1/3"],
         "m = (−8−4)/(3−(−1)) = −12/4 = −3."),
        ("If two lines have slopes 4 and −1/4, they are:", ["Parallel", "*Perpendicular", "Neither", "Identical"],
         "4 × (−1/4) = −1 → perpendicular."),
        ("The equation of a vertical line through (5, −2) is:", ["y = −2", "y = 5", "*x = 5", "x = −2"],
         "Vertical lines have the form x = constant."),
        ("The equation of a horizontal line through (5, −2) is:", ["*y = −2", "x = 5", "y = 5", "x = −2"],
         "Horizontal lines have the form y = constant."),
        ("Slope between (a, b) and (a, c) where b ≠ c:", ["0", "1", "*Undefined (vertical line)", "(c−b)/0"],
         "Same x-value, different y-values → vertical → undefined slope."),
        ("Two distinct lines with the same slope and same y-intercept are:", ["Parallel", "Perpendicular", "*Identical (the same line)", "Impossible"],
         "Same m and same b → same line."),
        ("The slope of any line parallel to the x-axis is:", ["Undefined", "1", "*0", "−1"],
         "Parallel to x-axis = horizontal = slope 0."),
    ]
)
lessons[k] = v

# ── 2.3 Quadratic Functions ──
k, v = build_lesson(2, 3, "Quadratic Functions (vertex form, standard form)",
    "<h3>Quadratic Functions</h3>"
    "<p>A quadratic function has the form f(x) = ax² + bx + c (standard form) or f(x) = a(x − h)² + k (vertex form).</p>"
    "<ul><li><b>Standard form:</b> f(x) = ax² + bx + c. Vertex at x = −b/(2a).</li>"
    "<li><b>Vertex form:</b> f(x) = a(x − h)² + k. Vertex at (h, k).</li>"
    "<li><b>Direction:</b> a > 0 → opens up (minimum); a < 0 → opens down (maximum).</li>"
    "<li><b>Axis of symmetry:</b> x = h (vertical line through the vertex).</li>"
    "<li><b>Converting:</b> Complete the square to go from standard to vertex form.</li></ul>",
    [
        ("Standard Form", "f(x) = ax² + bx + c; vertex at x = −b/(2a)."),
        ("Vertex Form", "f(x) = a(x − h)² + k; vertex at (h, k)."),
        ("Axis of Symmetry", "The vertical line x = h that passes through the vertex."),
        ("Opens Up/Down", "a > 0: parabola opens up (minimum); a < 0: opens down (maximum)."),
        ("Width of Parabola", "|a| large → narrow; |a| small → wide."),
    ],
    [
        ("The vertex form of a quadratic is:", ["ax² + bx + c", "*a(x−h)² + k", "mx + b", "a/x"],
         "Vertex form directly shows the vertex (h, k)."),
        ("f(x) = 2(x−3)² + 5. The vertex is:", ["(−3, 5)", "*(3, 5)", "(3, −5)", "(5, 3)"],
         "Vertex form: (h, k) = (3, 5)."),
        ("f(x) = −x² + 4x − 1. The parabola opens:", ["Up", "*Down", "Left", "Right"],
         "a = −1 < 0 → opens down."),
        ("Vertex of f(x) = x² − 6x + 8. x-coordinate:", ["6", "−6", "*3", "−3"],
         "x = −b/(2a) = −(−6)/(2·1) = 3."),
        ("f(x) = x² − 6x + 8. Vertex y-coordinate when x = 3:", ["8", "0", "*−1", "5"],
         "f(3) = 9 − 18 + 8 = −1. Vertex: (3, −1)."),
        ("The axis of symmetry for f(x) = 2(x+1)² − 4 is:", ["x = 1", "*x = −1", "x = −4", "y = −1"],
         "h = −1, so the axis is x = −1."),
        ("If a > 0, the vertex is a:", ["Maximum", "*Minimum", "Zero", "Inflection point"],
         "Opens up → the lowest point is the vertex (minimum)."),
        ("If a < 0, the vertex is a:", ["Minimum", "*Maximum", "Zero", "Inflection point"],
         "Opens down → the highest point is the vertex (maximum)."),
        ("|a| = 5 vs. |a| = 1/2 — which parabola is narrower?", ["*|a| = 5 (larger |a| = narrower)", "|a| = 1/2", "Both are the same", "Cannot tell"],
         "Larger |a| means the parabola is narrower (steeper)."),
        ("Convert f(x) = x² + 4x + 7 to vertex form:", ["(x+4)² + 7", "(x+2)² + 7", "*(x+2)² + 3", "(x−2)² + 3"],
         "Complete the square: x²+4x+4+3 = (x+2)²+3."),
        ("The y-intercept of f(x) = 3x² − 2x + 5 is:", ["3", "−2", "*5", "−5"],
         "Set x = 0: f(0) = 5."),
        ("f(x) = −(x−4)² + 9. Maximum value:", ["4", "−9", "*9", "−4"],
         "Opens down; vertex (4, 9); maximum is k = 9."),
        ("How many x-intercepts can a quadratic have?", ["Only 2", "Only 1", "Only 0", "*0, 1, or 2"],
         "Depending on the discriminant, a parabola can cross the x-axis 0, 1, or 2 times."),
        ("f(x) = (x−1)(x−5). The x-intercepts are:", ["*1 and 5", "−1 and −5", "1 and −5", "−1 and 5"],
         "Set each factor = 0."),
        ("f(x) = (x−1)(x−5). The axis of symmetry is:", ["x = 1", "x = 5", "*x = 3", "x = −3"],
         "Midpoint of the roots: (1+5)/2 = 3."),
        ("Completing the square for x² − 10x: add and subtract:", ["5", "100", "*25", "10"],
         "Half of −10 = −5; (−5)² = 25."),
        ("f(x) = 4x² has its vertex at:", ["(4, 0)", "*(0, 0)", "(0, 4)", "(2, 0)"],
         "f(x) = 4(x−0)² + 0; vertex (0, 0)."),
        ("A quadratic that opens up with vertex below the x-axis has:", ["0 x-intercepts", "1 x-intercept", "*2 x-intercepts", "Cannot determine"],
         "Opens up and vertex below axis → the parabola must cross the axis twice."),
        ("The discriminant b²−4ac determines:", ["The vertex", "The y-intercept", "*The number and type of x-intercepts", "The axis of symmetry"],
         "b²−4ac > 0: 2 real; = 0: 1 real; < 0: 0 real (complex roots)."),
        ("f(x) = a(x−h)² + k with vertex (2, −3) and passing through (0, 5). Find a:", ["−3", "5", "*2", "1"],
         "5 = a(0−2)² + (−3) → 5 = 4a − 3 → 4a = 8 → a = 2."),
    ]
)
lessons[k] = v

# ── 2.4 Completing the Square ──
k, v = build_lesson(2, 4, "Completing the Square",
    "<h3>Completing the Square</h3>"
    "<p>Completing the square converts ax² + bx + c into a(x − h)² + k form.</p>"
    "<h4>Steps</h4>"
    "<ol><li>Factor out a from the x² and x terms: a(x² + (b/a)x) + c.</li>"
    "<li>Take half of the coefficient of x: (b/(2a)).</li>"
    "<li>Square it: (b/(2a))².</li>"
    "<li>Add and subtract this value inside the parentheses.</li>"
    "<li>Factor the perfect square trinomial and simplify.</li></ol>"
    "<p><b>Applications:</b> Converting to vertex form, deriving the quadratic formula, graphing parabolas, and solving equations.</p>",
    [
        ("Completing the Square", "A technique to rewrite ax² + bx + c as a(x − h)² + k."),
        ("Perfect Square Trinomial", "An expression of the form x² ± 2px + p² = (x ± p)²."),
        ("Half the Coefficient of x", "The key step: take b/(2a), square it, add and subtract."),
        ("Vertex Form from Completing the Square", "The result a(x − h)² + k reveals the vertex (h, k)."),
        ("Deriving the Quadratic Formula", "Completing the square on ax² + bx + c = 0 yields x = (−b ± √(b²−4ac))/(2a)."),
    ],
    [
        ("To complete the square for x² + 6x, add:", ["6", "3", "*9", "36"],
         "Half of 6 = 3; 3² = 9. x² + 6x + 9 = (x+3)²."),
        ("x² + 6x + 9 = ?", ["(x + 6)²", "(x − 3)²", "*(x + 3)²", "(x + 9)²"],
         "Perfect square: (x + 3)² = x² + 6x + 9."),
        ("Complete the square: x² − 8x + __ = (x − __)²", ["*16 and 4 → x² − 8x + 16 = (x−4)²", "8 and 4", "64 and 8", "4 and 2"],
         "Half of −8 = −4; (−4)² = 16."),
        ("Convert x² + 4x + 1 to vertex form:", ["(x+4)² − 15", "(x+2)² + 1", "*(x+2)² − 3", "(x−2)² + 3"],
         "x² + 4x + 4 − 4 + 1 = (x+2)² − 3."),
        ("Convert 2x² + 12x + 5 to vertex form:", ["2(x+3)² − 13", "*2(x+3)² − 13", "(x+6)² + 5", "2(x+6)² − 67"],
         "Factor out 2: 2(x²+6x)+5 = 2(x²+6x+9−9)+5 = 2(x+3)²−18+5 = 2(x+3)²−13."),
        ("The vertex of f(x) = x² − 10x + 21 is:", ["(5, 21)", "(−5, −4)", "*(5, −4)", "(10, 21)"],
         "Complete: (x²−10x+25)−25+21 = (x−5)²−4. Vertex (5,−4)."),
        ("To derive the quadratic formula, complete the square on:", ["x² + bx", "*ax² + bx + c = 0", "x² = 0", "x + b = 0"],
         "The quadratic formula comes from completing the square on the general quadratic equation."),
        ("Completing the square for x² − 2x − 3 = 0:", ["(x−1)² = 1", "*(x−1)² = 4 → x = 3 or x = −1", "(x+1)² = 4", "(x−2)² = 3"],
         "(x²−2x+1)−1−3 = 0 → (x−1)² = 4 → x−1 = ±2."),
        ("Complete: x² + 3x + __ = (x + __)²", ["*9/4 and 3/2", "3 and 3/2", "9 and 3", "6 and 3"],
         "Half of 3 = 3/2; (3/2)² = 9/4."),
        ("When a ≠ 1, the first step is to:", ["Set the equation = 0", "Take the square root", "*Factor out a from the x² and x terms", "Add b to both sides"],
         "Dividing or factoring out a makes the leading coefficient 1."),
        ("3x² − 12x + 7 in vertex form:", ["3(x−4)² + 7", "*3(x−2)² − 5", "3(x−2)² + 7", "(x−4)² − 5"],
         "3(x²−4x)+7 = 3(x²−4x+4−4)+7 = 3(x−2)²−12+7 = 3(x−2)²−5."),
        ("The method works because (x + p)² = ?", ["x² + p²", "*x² + 2px + p²", "x² − 2px + p²", "2x + p"],
         "The expanded form of a perfect square trinomial."),
        ("x² − 14x + 49 = ?", ["(x − 14)²", "(x + 7)²", "*(x − 7)²", "(x − 49)²"],
         "Half of −14 = −7; (−7)² = 49. Check: (x−7)² = x²−14x+49. ✓"),
        ("Convert f(x) = −x² + 6x − 2 to vertex form:", ["−(x+3)² + 7", "*−(x−3)² + 7", "−(x−3)² − 7", "(x−3)² + 7"],
         "−(x²−6x)−2 = −(x²−6x+9−9)−2 = −(x−3)²+9−2 = −(x−3)²+7."),
        ("Completing the square can solve:", ["Only linear equations", "*Quadratic equations", "Only cubic equations", "No equations"],
         "It's a method for solving any quadratic equation."),
        ("After completing the square: (x − 5)² = 16 → x = ?", ["5 ± 4 → x = 9 or 1", "*5 ± 4 → x = 9 or x = 1", "5 + 16 = 21", "Only x = 9"],
         "Take the square root: x − 5 = ±4 → x = 9 or x = 1."),
        ("Complete: x² + x + __ = (x + __)²", ["*1/4 and 1/2", "1 and 1", "1/2 and 1/4", "2 and 1"],
         "Half of 1 = 1/2; (1/2)² = 1/4."),
        ("Why is completing the square useful beyond vertex form?", ["It's not", "*It's used to derive the quadratic formula, analyze conics, and solve optimization problems", "Only for graphing", "Only in calculus"],
         "The technique appears in many areas of algebra and beyond."),
        ("x² + 2bx + b² = ?", ["(x + 2b)²", "*(x + b)²", "x² + b²", "(x − b)²"],
         "This is the general perfect square pattern."),
        ("For x² − 20x, completing the square requires adding:", ["20", "400", "10", "*100"],
         "Half of −20 = −10; (−10)² = 100."),
    ]
)
lessons[k] = v

# ── 2.5 Quadratic Formula & Complex Solutions ──
k, v = build_lesson(2, 5, "Quadratic Formula & Complex Solutions",
    "<h3>Quadratic Formula & Complex Solutions</h3>"
    "<p><b>Quadratic Formula:</b> x = (−b ± √(b²−4ac)) / (2a)</p>"
    "<h4>Discriminant: Δ = b² − 4ac</h4>"
    "<ul><li>Δ > 0: Two distinct real solutions.</li>"
    "<li>Δ = 0: One repeated real solution.</li>"
    "<li>Δ < 0: Two complex (imaginary) solutions.</li></ul>"
    "<h4>Complex Numbers</h4>"
    "<ul><li>i = √(−1); i² = −1.</li>"
    "<li>Complex solutions come in conjugate pairs: a + bi and a − bi.</li>"
    "<li>Example: x² + 1 = 0 → x = ±i.</li></ul>",
    [
        ("Quadratic Formula", "x = (−b ± √(b²−4ac))/(2a); solves any quadratic equation ax² + bx + c = 0."),
        ("Discriminant (Δ)", "Δ = b²−4ac; determines the number and type of solutions."),
        ("Imaginary Unit i", "i = √(−1); i² = −1. Used when the discriminant is negative."),
        ("Complex Conjugate Pair", "If a + bi is a solution, then a − bi is also a solution."),
        ("Two Real, One Repeated, or Two Complex", "Δ > 0: two real; Δ = 0: one repeated; Δ < 0: two complex."),
    ],
    [
        ("Solve x² − 5x + 6 = 0 using the quadratic formula:", ["x = 1, 6", "*x = 2, 3", "x = −2, −3", "x = 5, 6"],
         "x = (5 ± √(25−24))/2 = (5±1)/2 → x = 3 or x = 2."),
        ("The discriminant of x² + 4x + 4 = 0 is:", ["*0", "8", "16", "−4"],
         "Δ = 16 − 16 = 0 → one repeated root."),
        ("If Δ = 0, the quadratic has:", ["Two real solutions", "*One repeated real solution", "No solutions", "Two complex solutions"],
         "Δ = 0 means the parabola touches the x-axis at exactly one point."),
        ("If Δ < 0, the solutions are:", ["Two real numbers", "One real number", "*Two complex conjugate numbers", "No numbers"],
         "Negative discriminant → square root of a negative number → complex solutions."),
        ("Solve x² + 1 = 0:", ["x = 1", "x = −1", "*x = ±i", "No solution"],
         "x² = −1 → x = ±√(−1) = ±i."),
        ("i² = ?", ["1", "i", "*−1", "−i"],
         "By definition, i² = −1."),
        ("i³ = ?", ["1", "i", "−1", "*−i"],
         "i³ = i² · i = (−1)(i) = −i."),
        ("i⁴ = ?", ["−1", "i", "−i", "*1"],
         "i⁴ = (i²)² = (−1)² = 1."),
        ("The discriminant of 2x² − 3x + 5 = 0:", ["*9 − 40 = −31 (negative → complex solutions)", "9 + 40 = 49", "−31 + 3 = −28", "0"],
         "Δ = (−3)² − 4(2)(5) = 9 − 40 = −31."),
        ("Complex solutions always come in:", ["Identical pairs", "*Conjugate pairs (a+bi and a−bi)", "Real pairs", "Single solutions"],
         "When coefficients are real, complex roots come in conjugate pairs."),
        ("The conjugate of 3 + 2i is:", ["3 + 2i", "−3 + 2i", "*3 − 2i", "−3 − 2i"],
         "Change the sign of the imaginary part."),
        ("(2 + 3i) + (1 − 5i) = ?", ["3 + 8i", "*3 − 2i", "3 − 8i", "1 + 2i"],
         "Add reals: 2+1=3; add imaginaries: 3i+(−5i)=−2i."),
        ("(2 + i)(2 − i) = ?", ["4 + i²", "3", "*5", "4 − 1"],
         "(a+bi)(a−bi) = a² + b² = 4 + 1 = 5."),
        ("Solve x² − 6x + 13 = 0:", ["x = 3 ± 4", "*x = 3 ± 2i", "x = 6 ± i", "x = −3 ± 2i"],
         "Δ = 36−52 = −16; x = (6±√(−16))/2 = (6±4i)/2 = 3±2i."),
        ("If Δ > 0 and a perfect square, then the roots are:", ["Complex", "Repeated", "*Two distinct rational numbers", "Irrational"],
         "Positive perfect square discriminant → two rational roots."),
        ("If Δ > 0 and NOT a perfect square, the roots are:", ["Rational", "Complex", "*Two distinct irrational numbers", "Repeated"],
         "Positive non-perfect-square Δ → irrational roots (like 3 ± √5)."),
        ("Sum of roots of ax² + bx + c = 0 is:", ["b/a", "*−b/a", "c/a", "−c/a"],
         "By Vieta's formulas: r₁ + r₂ = −b/a."),
        ("Product of roots of ax² + bx + c = 0 is:", ["−b/a", "b/a", "*c/a", "−c/a"],
         "By Vieta's formulas: r₁ · r₂ = c/a."),
        ("3x² + 2x − 8 = 0. Discriminant:", ["*4 + 96 = 100", "4 − 96 = −92", "0", "−100"],
         "Δ = 4 − 4(3)(−8) = 4 + 96 = 100. Two rational roots."),
        ("Solve 3x² + 2x − 8 = 0:", ["x = −2, 4/3", "*x = (−2±10)/6 → x = 4/3 or x = −2", "x = 2, −4/3", "x = −4/3, 2"],
         "x = (−2±√100)/6 = (−2±10)/6 → x = 8/6 = 4/3 or x = −12/6 = −2."),
    ]
)
lessons[k] = v

# ── 2.6 Graphing Quadratic Functions ──
k, v = build_lesson(2, 6, "Graphing Quadratic Functions",
    "<h3>Graphing Quadratic Functions</h3>"
    "<p>To graph a parabola, identify key features:</p>"
    "<ol><li><b>Vertex:</b> (h, k) from vertex form or x = −b/(2a).</li>"
    "<li><b>Direction:</b> a > 0 (up), a < 0 (down).</li>"
    "<li><b>Axis of symmetry:</b> x = h.</li>"
    "<li><b>y-intercept:</b> f(0) = c.</li>"
    "<li><b>x-intercepts:</b> Solve f(x) = 0 (use factoring, quadratic formula, or completing the square).</li>"
    "<li><b>Additional points:</b> Choose x-values near the vertex and use symmetry.</li></ol>"
    "<p>The <b>focus</b> and <b>directrix</b> of a parabola play a role in conic sections (covered in later units).</p>",
    [
        ("Vertex", "The highest or lowest point of a parabola; (h, k) in vertex form."),
        ("Axis of Symmetry", "The vertical line x = h through the vertex; the parabola is symmetric about it."),
        ("y-intercept of a Quadratic", "f(0) = c in standard form; the point where the parabola crosses the y-axis."),
        ("x-intercepts (Zeros)", "Solutions to f(x) = 0; where the parabola crosses the x-axis."),
        ("Symmetry in Graphing", "Points equidistant from the axis of symmetry have the same y-value."),
    ],
    [
        ("f(x) = (x−2)² − 1. Vertex:", ["(−2, −1)", "*(2, −1)", "(2, 1)", "(−2, 1)"],
         "Vertex form: (h, k) = (2, −1)."),
        ("f(x) = (x−2)² − 1 opens:", ["*Up (a = 1 > 0)", "Down", "Left", "Right"],
         "a = 1 > 0, so it opens up."),
        ("f(x) = (x−2)² − 1. y-intercept:", ["−1", "2", "*3", "−3"],
         "f(0) = (0−2)² − 1 = 4 − 1 = 3."),
        ("f(x) = (x−2)² − 1. x-intercepts:", ["*x = 1 and x = 3", "x = 2", "x = −1 and 3", "None"],
         "Set (x−2)²−1 = 0 → (x−2)² = 1 → x−2 = ±1 → x = 1 or 3."),
        ("The axis of symmetry for f(x) = −3(x+1)² + 4:", ["x = 1", "*x = −1", "x = 4", "x = −4"],
         "h = −1, so the axis is x = −1."),
        ("f(x) = −3(x+1)² + 4 has a maximum of:", ["−1", "−3", "*4", "1"],
         "Opens down (a = −3 < 0); vertex at (−1, 4); max is k = 4."),
        ("To graph a quadratic, the minimum information needed is:", ["Just the y-intercept", "Just the x-intercepts", "*Vertex and direction (plus a few additional points for accuracy)", "None"],
         "Vertex, direction, and a couple of points give a good graph."),
        ("If f(a) = f(b) for a quadratic, then the axis of symmetry is at:", ["a", "b", "*x = (a+b)/2", "x = a − b"],
         "Symmetric points are equidistant from the axis: x = (a+b)/2."),
        ("f(x) = x² − 4x + 3. Factor to find x-intercepts:", ["(x−4)(x+3)", "*(x−1)(x−3)", "(x+1)(x+3)", "(x−2)(x−6)"],
         "x² − 4x + 3 = (x−1)(x−3). Zeros at x = 1 and x = 3."),
        ("f(x) = 2x² + 8x + 6. Vertex x-coordinate:", ["4", "*−2", "2", "−4"],
         "x = −b/(2a) = −8/(4) = −2."),
        ("f(x) = 2x² + 8x + 6. Vertex y-coordinate:", ["6", "0", "*−2", "2"],
         "f(−2) = 2(4)+8(−2)+6 = 8−16+6 = −2."),
        ("A parabola with vertex (0, 0) and a = 1 is the parent function:", ["y = x", "*y = x²", "y = |x|", "y = √x"],
         "The simplest quadratic is y = x²."),
        ("The graph of f(x) = −2x² compared to y = x² is:", ["Wider and opens up", "*Narrower and opens down", "Same shape but shifted", "Wider and opens down"],
         "|−2| > 1 → narrower; a < 0 → opens down."),
        ("To graph f(x) = x² + 2, take y = x² and:", ["Shift right 2", "Shift left 2", "*Shift up 2", "Shift down 2"],
         "+2 outside = vertical shift up 2."),
        ("The range of f(x) = (x−1)² + 3 is:", ["(−∞, ∞)", "(3, ∞)", "*[3, ∞)", "[1, ∞)"],
         "Opens up, vertex at y = 3, so y ≥ 3."),
        ("How many x-intercepts does f(x) = x² + 2 have?", ["2", "1", "*0", "Infinitely many"],
         "x² + 2 > 0 for all x — never crosses the x-axis."),
        ("The graph of f(x) = (x−4)² is y = x² shifted:", ["Left 4", "Up 4", "*Right 4", "Down 4"],
         "−4 inside = shift right 4."),
        ("Two quadratics can intersect at most:", ["1 point", "3 points", "*2 points", "0 points"],
         "Two parabolas can cross at 0, 1, or 2 points."),
        ("f(x) = −x² + 6x − 5. Vertex:", ["(6, −5)", "(−3, 4)", "*(3, 4)", "(3, −4)"],
         "x = −6/(−2) = 3; f(3) = −9+18−5 = 4. Vertex (3, 4)."),
        ("The focus and directrix of a parabola are related to:", ["The x-intercepts", "The slope", "*The geometric definition of a parabola (set of points equidistant from focus and directrix)", "The y-intercept"],
         "A parabola is the locus of points equidistant from the focus and directrix."),
    ]
)
lessons[k] = v

# ── 2.7 Applications of Linear & Quadratic Models ──
k, v = build_lesson(2, 7, "Applications of Linear & Quadratic Models",
    "<h3>Applications of Linear & Quadratic Models</h3>"
    "<p>Linear and quadratic functions model many real-world situations.</p>"
    "<ul><li><b>Linear:</b> Constant rate of change — distance-rate-time, cost functions, depreciation.</li>"
    "<li><b>Quadratic:</b> Parabolic behavior — projectile motion, area optimization, revenue/profit models.</li>"
    "<li><b>Revenue:</b> R(x) = (price)(quantity) = (p₀ − mx)x = p₀x − mx² — quadratic.</li>"
    "<li><b>Profit:</b> P(x) = R(x) − C(x).</li>"
    "<li><b>Optimization:</b> Find the vertex to maximize/minimize quadratic models.</li></ul>",
    [
        ("Revenue Function", "R(x) = price × quantity; often quadratic when price varies linearly with demand."),
        ("Profit Function", "P(x) = Revenue − Cost = R(x) − C(x)."),
        ("Optimization", "Finding the maximum or minimum of a function; for quadratics, use the vertex."),
        ("Projectile Motion", "h(t) = −16t² + v₀t + h₀ (in feet); the vertex gives maximum height."),
        ("Break-Even Point", "Where profit = 0 (revenue equals cost)."),
    ],
    [
        ("A ball is thrown up: h(t) = −16t² + 64t + 5. Max height:", ["64 ft", "5 ft", "*69 ft", "80 ft"],
         "t = −64/(−32) = 2; h(2) = −64+128+5 = 69 ft."),
        ("The ball hits the ground when:", ["t = 0", "h = 64", "*h(t) = 0 (solve for positive t)", "t = 2"],
         "Set h(t) = 0 and solve for the positive value of t."),
        ("Revenue R(x) = 100x − 2x². Maximum revenue occurs at x = ?", ["100", "50", "*25", "0"],
         "x = −100/(2·(−2)) = 100/4 = 25."),
        ("R(25) = 100(25) − 2(625) = ?", ["*1250", "1500", "2500", "625"],
         "R(25) = 2500 − 1250 = 1250."),
        ("Cost C(x) = 200 + 30x. Revenue R(x) = 50x. Break-even:", ["x = 5", "*x = 10", "x = 20", "x = 200"],
         "50x = 200 + 30x → 20x = 200 → x = 10."),
        ("A fence encloses a rectangular area with 100 ft of fencing. Maximize area:", ["A = 100", "A = 2500", "*Maximum area = 625 sq ft (25×25 square)", "A = 500"],
         "A = x(50−x) = 50x−x²; max at x = 25: A = 625."),
        ("Linear depreciation: a $20,000 car loses $3,000/yr. Value after t years:", ["V = 20000 + 3000t", "*V = 20000 − 3000t", "V = 3000t", "V = 20000/t"],
         "Constant rate of decrease → linear function."),
        ("Profit = Revenue − Cost. If R(x) = 75x and C(x) = 500 + 25x:", ["P(x) = 100x + 500", "*P(x) = 50x − 500", "P(x) = 75x", "P(x) = −25x + 500"],
         "P(x) = 75x − (500+25x) = 50x − 500."),
        ("Break-even for P(x) = 50x − 500:", ["x = 50", "*x = 10", "x = 500", "x = 5"],
         "50x − 500 = 0 → x = 10."),
        ("A quadratic revenue model suggests price increases eventually:", ["Always increase revenue", "*Decrease revenue (because demand falls too much)", "Have no effect", "Make profit negative"],
         "The downward-opening parabola means revenue declines past the optimal point."),
        ("d = rt. A car travels 300 miles at r mph. Time:", ["t = 300 + r", "t = 300r", "*t = 300/r", "t = r/300"],
         "t = d/r = 300/r."),
        ("Two cars heading toward each other at 40 and 60 mph, 200 miles apart. Time to meet:", ["*2 hours", "3 hours", "4 hours", "5 hours"],
         "Combined speed = 100 mph. t = 200/100 = 2 hours."),
        ("A launched object follows a parabolic path because:", ["Air resistance", "*Gravity provides constant downward acceleration", "It's random", "There's no friction"],
         "Constant gravitational acceleration creates a quadratic height function."),
        ("Maximize the area of a rectangle inscribed under y = 12 − x² with base on the x-axis:", ["The answer requires calculus or completing the square on A(x)", "*A(x) = 2x(12−x²) — find the vertex or critical point", "A = 144", "Not possible"],
         "This is a classic optimization problem (exact answer requires techniques from Unit 10)."),
        ("Average rate of change of f(x) = x² from x = 1 to x = 3:", ["4", "8", "*4 (Δy/Δx = (9−1)/(3−1) = 8/2 = 4)", "2"],
         "Average rate of change = [f(3)−f(1)]/(3−1) = (9−1)/2 = 4."),
        ("A linear model is appropriate when the rate of change is:", ["Increasing", "Decreasing", "*Constant", "Zero"],
         "Constant rate of change = linear function."),
        ("A quadratic model is appropriate when the rate of change:", ["Is constant", "*Changes at a constant rate (constant second differences)", "Is zero", "Is random"],
         "Linear first differences → quadratic function."),
        ("Vertex of a profit function P(x) = −2x² + 40x − 100:", ["(10, 200)", "*(10, 100)", "(20, 100)", "(5, 50)"],
         "x = −40/(−4) = 10; P(10) = −200+400−100 = 100."),
        ("Maximum profit from P(x) = −2x² + 40x − 100:", ["200", "40", "*100", "50"],
         "P(10) = 100 (the y-coordinate of the vertex)."),
        ("When solving application problems, always:", ["Skip units", "Guess the model", "*Define variables, write the model, solve, and interpret in context", "Use only the answer"],
         "Context and interpretation are essential."),
    ]
)
lessons[k] = v

# ── 2.8 Absolute Value Functions ──
k, v = build_lesson(2, 8, "Absolute Value Functions",
    "<h3>Absolute Value Functions</h3>"
    "<p>f(x) = |x| creates a V-shape. The general form is f(x) = a|x − h| + k.</p>"
    "<ul><li><b>Vertex:</b> (h, k).</li>"
    "<li><b>Opening:</b> a > 0 opens up (V); a < 0 opens down (inverted V).</li>"
    "<li><b>Slope of the arms:</b> +a on the right side, −a on the left side.</li>"
    "<li><b>Solving |x| = c:</b> If c > 0: x = c or x = −c. If c = 0: x = 0. If c < 0: no solution.</li>"
    "<li><b>Solving |expression| < c:</b> −c < expression < c (compound inequality).</li>"
    "<li><b>Solving |expression| > c:</b> expression > c OR expression < −c.</li></ul>",
    [
        ("Absolute Value Function", "f(x) = a|x − h| + k; V-shaped graph with vertex at (h, k)."),
        ("Solving |x| = c", "If c > 0: x = c or x = −c; if c = 0: x = 0; if c < 0: no solution."),
        ("|expression| < c", "Becomes −c < expression < c; a compound inequality."),
        ("|expression| > c", "Becomes expression > c OR expression < −c."),
        ("Vertex of Absolute Value", "(h, k) in f(x) = a|x − h| + k; the point where the V changes direction."),
    ],
    [
        ("f(x) = |x − 3| + 2 has vertex:", ["(−3, 2)", "*(3, 2)", "(3, −2)", "(2, 3)"],
         "Vertex (h, k) = (3, 2)."),
        ("f(x) = −2|x + 1| has vertex:", ["(1, 0)", "*(−1, 0)", "(−1, −2)", "(0, −1)"],
         "h = −1, k = 0. Opens down since a = −2 < 0."),
        ("Solve |x| = 5:", ["x = 5 only", "*x = 5 or x = −5", "x = 25", "No solution"],
         "|x| = 5 means x = 5 or x = −5."),
        ("Solve |x| = −3:", ["x = 3 or −3", "x = 3", "*No solution", "x = −3"],
         "Absolute value is always ≥ 0; it can never equal −3."),
        ("Solve |2x − 1| = 7:", ["x = 3 only", "x = −3 only", "*x = 4 or x = −3", "x = 4 or x = 3"],
         "2x−1 = 7 → x = 4; or 2x−1 = −7 → x = −3."),
        ("Solve |x − 2| < 5:", ["x < 7", "x > −3", "*−3 < x < 7", "x < −3 or x > 7"],
         "|x−2| < 5 → −5 < x−2 < 5 → −3 < x < 7."),
        ("Solve |x + 1| > 3:", ["−4 < x < 2", "*x > 2 or x < −4", "x > 3", "x < −3"],
         "x+1 > 3 → x > 2; or x+1 < −3 → x < −4."),
        ("The graph of y = |x| is:", ["A straight line", "A parabola", "*A V-shape (two linear pieces meeting at the origin)", "A curve"],
         "|x| creates a V with vertex at (0, 0)."),
        ("f(x) = |x| + 3 shifts the parent up 3. Range:", ["(−∞, ∞)", "(3, ∞)", "*[3, ∞)", "[0, ∞)"],
         "The lowest point is at y = 3."),
        ("f(x) = 2|x| compared to f(x) = |x| is:", ["Wider", "*Narrower (steeper V)", "The same", "Shifted"],
         "|a| = 2 > 1 → steeper arms."),
        ("Solve |3x + 6| = 0:", ["x = 6", "*x = −2", "x = 0", "No solution"],
         "3x + 6 = 0 → x = −2. |something| = 0 means the expression inside equals 0."),
        ("Solve |x − 4| ≤ 0:", ["x = 0", "−4 ≤ x ≤ 4", "*x = 4 (the only value where |x−4| = 0)", "No solution"],
         "|x−4| ≥ 0 always; it equals 0 only when x = 4."),
        ("The domain of f(x) = |x| is:", ["[0, ∞)", "(0, ∞)", "*(−∞, ∞)", "[−1, 1]"],
         "Absolute value is defined for all real numbers."),
        ("f(x) = −|x| + 5. Maximum value:", ["−5", "0", "*5", "Undefined"],
         "Opens down; vertex at (0, 5); max = 5."),
        ("f(x) = |x² − 9|. This is V-shaped?", ["Yes", "*No — it's a modified parabola (absolute value of a quadratic), not a simple V", "Always V", "Always parabola"],
         "Absolute value of a quadratic reflects the negative part above the x-axis."),
        ("|x| = x when:", ["x < 0", "*x ≥ 0", "Always", "Never"],
         "For x ≥ 0, |x| = x (the non-negative case)."),
        ("|x| = −x when:", ["*x ≤ 0", "x > 0", "Always", "Never"],
         "For x ≤ 0, |x| = −x (negating a negative gives a positive)."),
        ("Solve |2x| > 8:", ["−4 < x < 4", "*x > 4 or x < −4", "x = 4", "x > 8"],
         "|2x| > 8 → 2|x| > 8 → |x| > 4 → x > 4 or x < −4."),
        ("The transformation y = |x − 5| − 3 moves the V to vertex:", ["(−5, −3)", "*(5, −3)", "(5, 3)", "(−5, 3)"],
         "Right 5, down 3."),
        ("Absolute value equations can have 0, 1, or 2 solutions because:", ["*The V-shape can intersect a horizontal line at 0, 1, or 2 points", "It always has 2 solutions", "It never has 0 solutions", "It depends on the coefficient"],
         "Depending on the height of the V and the value, there are 0, 1, or 2 intersections."),
    ]
)
lessons[k] = v

# ── 2.9 Inequalities ──
k, v = build_lesson(2, 9, "Inequalities (linear & quadratic)",
    "<h3>Inequalities</h3>"
    "<h4>Linear Inequalities</h4>"
    "<ul><li>Solve like equations. <b>Flip the inequality</b> when multiplying/dividing by a negative.</li>"
    "<li>Graph on a number line: open circle for < or >, closed for ≤ or ≥.</li></ul>"
    "<h4>Quadratic Inequalities</h4>"
    "<ol><li>Solve the equality ax² + bx + c = 0 to find critical values.</li>"
    "<li>Test intervals between and beyond the critical values.</li>"
    "<li>Determine which intervals satisfy the inequality.</li></ol>"
    "<p><b>Sign chart method:</b> Factor the quadratic, determine sign of each factor in each interval, combine.</p>",
    [
        ("Flip the Inequality", "When multiplying or dividing both sides by a negative number, reverse the inequality sign."),
        ("Quadratic Inequality", "Solve ax² + bx + c > 0 (or <, ≥, ≤) by finding zeros and testing intervals."),
        ("Critical Values", "The solutions to the corresponding equality; they divide the number line into intervals."),
        ("Sign Chart", "A tool that tracks the sign (+/−) of each factor in each interval to determine the overall sign."),
        ("Interval Notation for Inequalities", "Express solutions using unions and intervals: e.g., (−∞, 2) ∪ (5, ∞)."),
    ],
    [
        ("Solve 3x − 6 > 0:", ["x > 6", "x < 2", "*x > 2", "x > 0"],
         "3x > 6 → x > 2."),
        ("Solve −2x ≥ 8:", ["x ≥ 4", "x ≥ −4", "*x ≤ −4", "x ≤ 4"],
         "Divide by −2 and flip: x ≤ −4."),
        ("Solve x² − 4 > 0:", ["−2 < x < 2", "*(−∞, −2) ∪ (2, ∞)", "x > 4", "x ≤ −2"],
         "Factor: (x−2)(x+2) > 0. Positive when x < −2 or x > 2."),
        ("Solve x² − 4 ≤ 0:", ["*(−∞, −2) ∪ [2, ∞)? No — [−2, 2]", "x ≤ −4", "x ≥ 4", "(−2, 2)"],
         "(x−2)(x+2) ≤ 0 when −2 ≤ x ≤ 2."),
        ("When dividing by a negative number, the inequality sign:", ["Stays the same", "*Flips (reverses)", "Disappears", "Becomes ="],
         "This is the key rule for solving inequalities."),
        ("Solve x² + 3x − 10 > 0:", ["(−5, 2)", "*x < −5 or x > 2", "x = −5 or 2", "(−∞, ∞)"],
         "Factor: (x+5)(x−2) > 0. Test intervals: positive when x < −5 or x > 2."),
        ("The critical values for x² − x − 6 = 0 are:", ["−2 and 3", "*−2 and 3", "2 and −3", "1 and −6"],
         "Factor: (x−3)(x+2) = 0 → x = 3 or x = −2."),
        ("For x² − x − 6 ≤ 0:", ["x ≤ −2 or x ≥ 3", "*−2 ≤ x ≤ 3", "x < −2 or x > 3", "All real numbers"],
         "(x−3)(x+2) ≤ 0 between the roots: −2 ≤ x ≤ 3."),
        ("A sign chart tracks:", ["The value of x", "*The sign (+/−) of each factor in each interval", "The graph", "The slope"],
         "Sign charts help determine where expressions are positive or negative."),
        ("Solve 5 − x ≤ 3:", ["x ≤ 2", "*x ≥ 2", "x ≤ 8", "x ≥ 8"],
         "−x ≤ −2 → x ≥ 2 (flip when dividing by −1)."),
        ("For a quadratic that opens up (a > 0), it's negative (< 0) between:", ["The y-intercepts", "*The two x-intercepts (roots)", "Below the vertex only", "Never"],
         "Opens up → negative between the roots."),
        ("For a quadratic that opens up, it's positive (> 0):", ["Between the roots", "*Outside the roots (x < smaller root or x > larger root)", "Everywhere", "Nowhere"],
         "Opens up → positive outside the roots."),
        ("Solve (x − 1)(x − 4) > 0:", ["1 < x < 4", "*(−∞, 1) ∪ (4, ∞)", "x = 1 or x = 4", "x > 4 only"],
         "Product of two factors is positive outside the roots."),
        ("Solve (x − 1)(x − 4) ≤ 0:", ["x ≤ 1 or x ≥ 4", "*1 ≤ x ≤ 4 (inclusive of endpoints since ≤ 0)", "(−∞, 1) ∪ (4, ∞)", "x = 2.5"],
         "Product is ≤ 0 between roots (including the endpoints)."),
        ("Compound inequality: −3 < 2x + 1 < 7:", ["*−2 < x < 3", "x < −3 or x > 7", "−3 < x < 7", "x = 2"],
         "Subtract 1: −4 < 2x < 6; divide by 2: −2 < x < 3."),
        ("Solve x² > 0:", ["*All real numbers except x = 0: (−∞, 0) ∪ (0, ∞)", "All real numbers", "x > 0 only", "No solution"],
         "x² > 0 for all x except x = 0 (where x² = 0)."),
        ("Solve x² ≤ 0:", ["All real numbers", "(−∞, 0) ∪ (0, ∞)", "*x = 0 (the only value where x² = 0)", "No solution"],
         "x² ≥ 0 always; it equals 0 only at x = 0."),
        ("Solve x² + 1 > 0:", ["x > 0", "x > −1", "*All real numbers (x² + 1 > 0 always)", "No solution"],
         "x² ≥ 0, so x² + 1 ≥ 1 > 0 for all x."),
        ("Solve x² + 1 < 0:", ["All real numbers", "x < −1", "x = 0", "*No solution (x² + 1 is always positive)"],
         "x² + 1 ≥ 1 > 0 for all real x."),
        ("Graphing linear inequalities on a number line: x > 3 uses:", ["*Open circle at 3, shade right", "Closed circle at 3, shade right", "Open circle at 3, shade left", "Closed circle at 3, shade left"],
         "Open circle = not included (strict inequality); shade right for >."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 2)")
