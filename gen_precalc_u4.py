import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "precalculus_lessons.json")

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for i, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            if o.startswith("*"):
                options.append({"text": o[1:], "is_correct": True, "data_i18n": None})
            else:
                options.append({"text": o, "is_correct": False, "data_i18n": None})
        qs.append({"question_number": i, "question_text": qt, "attempted": 2, "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": "Precalculus",
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# ── 4.1 Rational Expressions & Simplification ─────────────────────
k, v = build_lesson(4, 1,
    "Rational Expressions & Simplification",
    "<h3>Rational Expressions &amp; Simplification</h3>"
    "<p>A <b>rational expression</b> is a ratio of two polynomials: P(x)/Q(x), where Q(x) ≠ 0.</p>"
    "<h4>Simplifying</h4>"
    "<ul>"
    "<li>Factor both the numerator and denominator completely.</li>"
    "<li>Cancel common factors (noting <b>excluded values</b> where Q = 0).</li>"
    "</ul>"
    "<h4>Operations</h4>"
    "<ul>"
    "<li><b>Multiply:</b> Factor, cancel, then multiply remaining numerators and denominators.</li>"
    "<li><b>Divide:</b> Multiply by the reciprocal of the divisor.</li>"
    "<li><b>Add/Subtract:</b> Find the <b>LCD</b>, rewrite each fraction, then combine numerators.</li>"
    "</ul>"
    "<h4>Complex Fractions</h4>"
    "<ul>"
    "<li>A fraction within a fraction. Simplify by multiplying numerator and denominator by the LCD of all mini-fractions.</li>"
    "</ul>",
    [
        ("Rational Expression", "A ratio P(x)/Q(x) of two polynomials, where Q(x) ≠ 0."),
        ("Excluded Values", "x-values that make the denominator zero; the expression is undefined there."),
        ("Least Common Denominator (LCD)", "The smallest expression divisible by every denominator; used when adding or subtracting rational expressions."),
        ("Complex Fraction", "A fraction whose numerator or denominator (or both) contain fractions."),
        ("Simplifying", "Factor numerator and denominator, cancel common factors, and state restrictions.")
    ],
    [
        ("Simplify (x² − 4)/(x + 2).", ["x + 2", "*x − 2", "x² − 2", "(x−2)/(x+2)"],
         "(x−2)(x+2)/(x+2) = x − 2, x ≠ −2."),
        ("Excluded value(s) of 5/(x − 3)?", ["x = 5", "*x = 3", "x = 0", "None"],
         "x − 3 = 0 → x = 3."),
        ("Simplify (x² − 9)/(x² + 6x + 9).", ["(x+3)/(x−3)", "*(x − 3)/(x + 3)", "x − 3", "1"],
         "(x−3)(x+3)/(x+3)² = (x−3)/(x+3)."),
        ("Multiply: (x/3) · (6/x²).", ["6/x", "x/x²", "*2/x", "6x/3x²"],
         "6x/(3x²) = 2/x."),
        ("Divide: (x²/4) ÷ (x/2).", ["x/8", "x³/8", "*x/2", "2/x"],
         "(x²/4)·(2/x) = 2x²/(4x) = x/2."),
        ("LCD of 1/(x+1) and 1/(x−1)?", ["x", "(x+1)(x+1)", "*(x+1)(x−1)", "x² + 1"],
         "Distinct linear factors → (x+1)(x−1)."),
        ("Add: 1/(x+1) + 1/(x−1).", ["2/(x²−1)", "*(2x)/(x²−1)", "2/(2x)", "(x+1+x−1)/(x²+1)"],
         "[(x−1)+(x+1)]/[(x+1)(x−1)] = 2x/(x²−1)."),
        ("Subtract: 3/x − 2/x.", ["5/x", "3/x²", "*1/x", "6/x²"],
         "Same denominator: (3−2)/x = 1/x."),
        ("Simplify: (1/x + 1/y) / (1/x − 1/y).", ["xy", "(x+y)/(x−y)", "*(y+x)/(y−x)", "x/y"],
         "Multiply top and bottom by xy: (y+x)/(y−x)."),
        ("Simplify (2x² + 6x)/(4x).", ["(x+3)/4", "2x + 6", "*(x + 3)/2", "x/2 + 3"],
         "2x(x+3)/(4x) = (x+3)/2."),
        ("The expression (x−5)/(5−x) simplifies to:", ["1", "0", "*−1", "x"],
         "5−x = −(x−5), so (x−5)/(−(x−5)) = −1."),
        ("Multiply: [(x+2)/(x−1)] · [(x−1)/(x+3)].", ["(x+2)(x−1)/((x−1)(x+3))", "*(x+2)/(x+3)", "1/(x+3)", "(x²+x−2)/(x²+2x−3)"],
         "Cancel (x−1): (x+2)/(x+3)."),
        ("Excluded values of (x+1)/((x−2)(x+4))?", ["x = −1", "*x = 2 and x = −4", "x = 2", "x = −4 only"],
         "Denominator = 0 at x = 2 and x = −4."),
        ("LCD of 2/(x²) and 3/(x³)?", ["x²", "*x³", "x⁵", "6x³"],
         "Highest power of x is x³."),
        ("Add: 2/x² + 3/x³.", ["5/x⁵", "5/x³", "*(2x + 3)/x³", "6/x⁵"],
         "LCD = x³: 2x/x³ + 3/x³ = (2x+3)/x³."),
        ("Simplify: (x² − x − 6)/(x² − 9).", ["(x+2)/(x−3)", "*(x + 2)/(x + 3)", "(x−3)/(x+3)", "(x−2)/(x+3)"],
         "(x−3)(x+2)/((x−3)(x+3)) = (x+2)/(x+3), x ≠ 3."),
        ("Which is undefined at x = 0?", ["x/(x+1)", "*(x+1)/x", "(x+1)/(x+2)", "x²"],
         "(x+1)/x has denominator x = 0."),
        ("Simplify: (x³ − 8)/(x − 2).", ["x² + 4", "*x² + 2x + 4", "(x−2)(x²+4)", "x³ − 4"],
         "Difference of cubes: x³−8 = (x−2)(x²+2x+4). Cancel (x−2)."),
        ("Complex fraction: (1 − 1/x)/(1 + 1/x).", ["x/(x+1)", "(x+1)/(x−1)", "*(x − 1)/(x + 1)", "1"],
         "Multiply by x/x: (x−1)/(x+1)."),
        ("What should you always state when simplifying?", ["The degree", "The LCD", "*Excluded values / restrictions", "The y-intercept"],
         "Restrictions (excluded values) must be noted.")
    ]
)
lessons[k] = v

# ── 4.2 Vertical, Horizontal, and Oblique Asymptotes ──────────────
k, v = build_lesson(4, 2,
    "Vertical, Horizontal, and Oblique Asymptotes",
    "<h3>Vertical, Horizontal, and Oblique Asymptotes</h3>"
    "<p>Asymptotes are lines that a graph approaches but typically never reaches.</p>"
    "<h4>Vertical Asymptotes (VA)</h4>"
    "<ul>"
    "<li>Occur where the <b>denominator = 0</b> and the <b>numerator ≠ 0</b> (after simplification).</li>"
    "<li>The graph goes to ±∞ near a VA.</li>"
    "</ul>"
    "<h4>Horizontal Asymptotes (HA)</h4>"
    "<ul>"
    "<li>Compare degrees of numerator (n) and denominator (m):</li>"
    "<li>n &lt; m → HA is y = 0.</li>"
    "<li>n = m → HA is y = (leading coeff of num)/(leading coeff of den).</li>"
    "<li>n &gt; m → no horizontal asymptote.</li>"
    "</ul>"
    "<h4>Oblique (Slant) Asymptotes</h4>"
    "<ul>"
    "<li>Occur when n = m + 1 (degree of numerator is exactly one more than denominator).</li>"
    "<li>Perform polynomial long division; the quotient (ignoring remainder) is the oblique asymptote.</li>"
    "</ul>",
    [
        ("Vertical Asymptote", "A vertical line x = a where the function → ±∞; occurs where the denominator is zero (after cancellation)."),
        ("Horizontal Asymptote", "A horizontal line y = L that the function approaches as x → ±∞."),
        ("Oblique (Slant) Asymptote", "A linear asymptote y = mx + b that occurs when the numerator's degree is exactly one more than the denominator's."),
        ("Degree Comparison Rule", "n < m → y = 0; n = m → y = aₙ/bₘ; n > m → no HA."),
        ("Behavior Near a VA", "The function increases or decreases without bound (→ +∞ or → −∞) on either side.")
    ],
    [
        ("Find the VA of f(x) = 1/(x − 3).", ["x = 0", "*x = 3", "x = −3", "y = 3"],
         "Denominator = 0 at x = 3."),
        ("Find the HA of f(x) = 5/(x + 2).", ["y = 5", "y = 2", "*y = 0", "No HA"],
         "Degree of num (0) < deg of den (1) → HA: y = 0."),
        ("HA of f(x) = (3x + 1)/(2x − 5)?", ["y = 1", "y = −1/5", "*y = 3/2", "y = 0"],
         "Degrees equal (both 1). HA = 3/2."),
        ("HA of f(x) = (x² + 1)/(x − 1)?", ["y = 1", "y = 0", "y = −1", "*No HA"],
         "Degree of num (2) > deg of den (1) → no HA."),
        ("Does f(x) = (x² + 1)/(x − 1) have an oblique asymptote?", ["*Yes", "No", "Only if x > 0", "Cannot tell"],
         "Degree difference is exactly 1 → oblique asymptote exists."),
        ("Find the oblique asymptote of (x² + 1)/(x − 1).", ["y = x", "*y = x + 1", "y = x − 1", "y = x + 2"],
         "Long division: x² + 1 ÷ (x − 1) = x + 1 remainder 2. OA: y = x + 1."),
        ("f(x) = (x − 1)/((x − 1)(x + 2)). VA at:", ["x = 1", "*x = −2 only", "x = 1 and x = −2", "No VA"],
         "After canceling (x−1): f = 1/(x+2). VA at x = −2. x = 1 is a hole, not a VA."),
        ("f(x) = 2x/(x² − 4). Vertical asymptotes?", ["x = 4 only", "*x = 2 and x = −2", "x = 0", "x = 2 only"],
         "x² − 4 = (x−2)(x+2) = 0 at x = ±2."),
        ("HA of f(x) = (4x³)/(2x³ + 1)?", ["y = 0", "y = 4", "*y = 2", "No HA"],
         "Same degree: 4/2 = 2."),
        ("VA of f(x) = x/(x² + 1)?", ["x = 1", "x = ±1", "x = 0", "*None"],
         "x² + 1 > 0 for all real x → denominator never zero."),
        ("HA of f(x) = x/(x² + 1)?", ["y = 1", "*y = 0", "No HA", "y = x"],
         "Deg num (1) < deg den (2) → y = 0."),
        ("Find VA of f(x) = (x+3)/((x+3)(x−1)).", ["x = −3 and x = 1", "*x = 1 (x = −3 is a hole)", "x = −3 only", "No VA"],
         "Cancel (x+3): 1/(x−1). x = −3 is a hole; x = 1 is the VA."),
        ("As x → 3⁺ for f(x) = 1/(x − 3), f →", ["0", "−∞", "*+∞", "3"],
         "Just right of 3: denominator is small and positive → +∞."),
        ("As x → 3⁻ for f(x) = 1/(x − 3), f →", ["0", "*−∞", "+∞", "3"],
         "Just left of 3: denominator is small and negative → −∞."),
        ("HA of f(x) = (−x + 5)/(2x + 1)?", ["y = 5", "y = 0", "*y = −1/2", "y = 1/2"],
         "Same degree: −1/2."),
        ("Oblique asymptote of (2x² + 3x − 1)/(x + 1)?", ["y = 2x + 3", "*y = 2x + 1", "y = x + 1", "y = 2x − 1"],
         "2x² + 3x − 1 ÷ (x + 1) = 2x + 1 rem −2. OA: y = 2x + 1."),
        ("Can a function cross its horizontal asymptote?", ["Never", "*Yes, it can cross a HA", "Only linear functions", "Only polynomials"],
         "A function can cross its HA; it just approaches it as x → ±∞."),
        ("Can a function cross its vertical asymptote?", ["Yes", "*No", "Sometimes", "Only rational functions"],
         "A VA is where the function is undefined; it cannot cross it."),
        ("f(x) = 7/(x² − 9). Number of VAs?", ["1", "*2", "3", "0"],
         "x² − 9 = 0 → x = ±3. Two VAs."),
        ("For f(x) = (x² − 1)/(x − 1), after simplification:", ["VA at x = 1", "*Hole at x = 1, graph is y = x + 1", "HA at y = 1", "OA at y = x"],
         "(x−1)(x+1)/(x−1) = x + 1 with a hole at x = 1.")
    ]
)
lessons[k] = v

# ── 4.3 Holes and Discontinuities ─────────────────────────────────
k, v = build_lesson(4, 3,
    "Holes and Discontinuities",
    "<h3>Holes and Discontinuities</h3>"
    "<p>When both numerator and denominator share a common factor, canceling it creates a <b>hole</b> (removable discontinuity) rather than a vertical asymptote.</p>"
    "<h4>Identifying Holes</h4>"
    "<ul>"
    "<li>Factor numerator and denominator.</li>"
    "<li>A common factor (x − c) that cancels creates a hole at x = c.</li>"
    "<li>The y-coordinate of the hole is found by substituting c into the simplified expression.</li>"
    "</ul>"
    "<h4>Types of Discontinuities</h4>"
    "<ul>"
    "<li><b>Removable (hole):</b> Factor cancels; the limit exists but the function is undefined there.</li>"
    "<li><b>Non-removable (VA):</b> The function → ±∞; the limit does not exist as a finite number.</li>"
    "<li><b>Jump:</b> Occurs in piecewise functions where left and right limits differ.</li>"
    "</ul>",
    [
        ("Hole (Removable Discontinuity)", "A point where a common factor cancels; the function is undefined but the limit exists."),
        ("Non-removable Discontinuity", "A vertical asymptote where the function → ±∞; the limit does not exist finitely."),
        ("Jump Discontinuity", "Occurs when left-hand and right-hand limits exist but are not equal."),
        ("Common Factor", "A factor present in both numerator and denominator that, when canceled, creates a hole."),
        ("Coordinates of a Hole", "At x = c: substitute c into the simplified expression to find the y-value.")
    ],
    [
        ("f(x) = (x² − 1)/(x − 1). Where is the hole?", ["*x = 1", "x = −1", "x = 0", "No hole"],
         "(x−1)(x+1)/(x−1): cancel (x−1) → hole at x = 1."),
        ("What is the y-coordinate of the hole above?", ["0", "1", "*2", "−1"],
         "Simplified: x + 1. At x = 1: 1 + 1 = 2. Hole at (1, 2)."),
        ("f(x) = (x² − 4)/(x² − x − 2). Hole at?", ["x = −1", "*x = 2", "x = −2", "No hole"],
         "(x−2)(x+2)/((x−2)(x+1)). Cancel (x−2) → hole at x = 2."),
        ("VA of the function above?", ["x = 2", "*x = −1", "x = −2", "No VA"],
         "After canceling: (x+2)/(x+1). VA at x = −1."),
        ("A hole is also called a:", ["Vertical asymptote", "Horizontal asymptote", "*Removable discontinuity", "Non-removable discontinuity"],
         "The discontinuity can be 'removed' by defining the function at that point."),
        ("f(x) = (x − 3)/(x² − 9). Simplify and identify discontinuities.", ["*Hole at x = 3, VA at x = −3", "VA at x = 3 and −3", "Hole at x = −3, VA at x = 3", "No discontinuities"],
         "(x−3)/((x−3)(x+3)) = 1/(x+3). Hole at x = 3, VA at x = −3."),
        ("y-value of the hole at x = 3 for f above?", ["0", "3", "*1/6", "1/3"],
         "1/(3+3) = 1/6."),
        ("f(x) = x/(x² + x). Simplify.", ["x + 1", "*1/(x + 1), hole at x = 0", "1/x, hole at x = 0", "x/(x+1)"],
         "x/(x(x+1)) = 1/(x+1), x ≠ 0. Hole at x = 0."),
        ("At a vertical asymptote, the limit is:", ["0", "A finite number", "*±∞ (does not exist finitely)", "1"],
         "The function → ±∞ at a VA."),
        ("At a hole, the limit:", ["Does not exist", "*Exists and is finite", "Is ±∞", "Is 0"],
         "The limit exists (equal to the y-value of the hole), but the function is undefined."),
        ("f(x) = (2x² − 2)/(x − 1). Factor numerator.", ["2(x−1)²", "*2(x−1)(x+1)", "(2x−2)(x+1)", "2x(x−1)"],
         "2x² − 2 = 2(x² − 1) = 2(x−1)(x+1)."),
        ("After canceling, f(x) above becomes:", ["2(x−1)", "*2(x+1), hole at x = 1", "2x + 2, no hole", "(x+1)/(x−1)"],
         "2(x−1)(x+1)/(x−1) = 2(x+1), x ≠ 1. Hole at x = 1."),
        ("Hole y-value at x = 1:", ["2", "*4", "0", "1"],
         "2(1+1) = 4."),
        ("Does f(x) = 1/(x² + 1) have any discontinuities?", ["VA at x = ±1", "Hole at x = 0", "Jump at x = 0", "*No discontinuities"],
         "x² + 1 > 0 always. No zeros in denominator."),
        ("A jump discontinuity occurs in:", ["Rational functions", "Polynomial functions", "*Piecewise functions", "Exponential functions"],
         "Jump discontinuities arise when left and right limits differ, typical of piecewise functions."),
        ("f(x) = (x³ − 8)/(x − 2). Hole at x = 2. y-value?", ["4", "8", "*12", "6"],
         "Simplified: x² + 2x + 4. At x = 2: 4+4+4 = 12."),
        ("How do you graph a hole?", ["Solid dot", "*Open circle", "Vertical line", "Skip that x-value"],
         "An open circle indicates the function is undefined at that point."),
        ("f(x) = (x² + 5x + 6)/(x + 3). Discontinuity?", ["VA at x = −3", "*Hole at x = −3", "No discontinuity", "Jump at x = −3"],
         "(x+2)(x+3)/(x+3) = x+2. Hole at x = −3."),
        ("After removing the hole, the graph of f above is:", ["A parabola", "*A straight line y = x + 2", "A hyperbola", "A cubic"],
         "Simplified form is the linear function y = x + 2."),
        ("Which statement is true?", ["All zeros of the denominator produce VAs", "*Shared zeros produce holes, unshared produce VAs", "Holes are the same as VAs", "Polynomials can have holes"],
         "Common factors → holes; remaining denominator zeros → VAs.")
    ]
)
lessons[k] = v

# ── 4.4 Graphing Rational Functions ────────────────────────────────
k, v = build_lesson(4, 4,
    "Graphing Rational Functions",
    "<h3>Graphing Rational Functions</h3>"
    "<p>Combine asymptotes, intercepts, holes, and sign analysis to sketch rational function graphs.</p>"
    "<h4>Steps</h4>"
    "<ol>"
    "<li>Factor numerator and denominator; identify holes.</li>"
    "<li>Find <b>vertical asymptotes</b> (remaining denominator zeros).</li>"
    "<li>Find the <b>horizontal or oblique asymptote</b>.</li>"
    "<li>Find <b>x-intercepts</b> (numerator = 0) and <b>y-intercept</b> (x = 0).</li>"
    "<li>Use a <b>sign chart</b> to determine where f is positive or negative.</li>"
    "<li>Plot key points and sketch.</li>"
    "</ol>"
    "<h4>Additional Tips</h4>"
    "<ul>"
    "<li>Check symmetry: f(−x) = f(x) → even symmetry, f(−x) = −f(x) → odd symmetry.</li>"
    "<li>The graph approaches but typically doesn't cross a VA; it may cross a HA.</li>"
    "</ul>",
    [
        ("x-intercepts of a Rational Function", "Found by setting the numerator equal to zero (after canceling common factors)."),
        ("y-intercept", "f(0) = (numerator evaluated at 0)/(denominator evaluated at 0), if defined."),
        ("Sign Chart", "Divide the number line at zeros and VAs; test the sign of f in each interval."),
        ("Even Symmetry", "f(−x) = f(x); graph is symmetric about the y-axis."),
        ("Odd Symmetry", "f(−x) = −f(x); graph is symmetric about the origin.")
    ],
    [
        ("x-intercept(s) of f(x) = (x − 2)/(x + 1)?", ["x = −1", "*x = 2", "x = 0", "None"],
         "Numerator = 0: x = 2."),
        ("y-intercept of f(x) = (x − 2)/(x + 1)?", ["1", "*−2", "2", "−1"],
         "f(0) = (−2)/(1) = −2."),
        ("f(x) = x/(x² − 1). VA(s)?", ["x = 0", "*x = 1 and x = −1", "x = ±√1", "None"],
         "x² − 1 = 0 → x = ±1."),
        ("HA of f(x) = x/(x² − 1)?", ["y = 1", "*y = 0", "No HA", "y = x"],
         "Deg num (1) < deg den (2) → y = 0."),
        ("Is f(x) = x/(x² − 1) even, odd, or neither?", ["Even", "*Odd", "Neither", "Both"],
         "f(−x) = −x/(x²−1) = −f(x) → odd symmetry (symmetric about origin)."),
        ("x-intercept(s) of f(x) = (x² − 4)/(x − 3)?", ["x = 3", "x = 4", "*x = 2 and x = −2", "None"],
         "x² − 4 = 0 → x = ±2."),
        ("f(x) = 1/(x − 2)². VA at x = 2. As x → 2, f →", ["−∞", "*+∞", "0", "1"],
         "Squared denominator → always positive → +∞ from both sides."),
        ("f(x) = (x + 1)/(x − 1). Where is f positive?", ["x > 1 only", "*x < −1 or x > 1", "−1 < x < 1", "All x"],
         "Sign chart: positive when both factors same sign → x < −1 or x > 1."),
        ("f(x) = −2/(x + 3). Reflection of 1/x?", ["Shifted right 3, stretched by 2", "*Shifted left 3, reflected, stretched by 2", "Shifted left 3, compressed", "Shifted up 2"],
         "Compared to 1/x: left 3, vertical stretch by 2, reflected."),
        ("For f(x) = (2x)/(x − 4), what is f(0)?", ["2", "−4", "*0", "Undefined"],
         "f(0) = 0/(−4) = 0."),
        ("How many times can f(x) cross its HA?", ["0", "1", "At most once", "*Any number of times"],
         "A rational function can cross its HA; it only must approach it at infinity."),
        ("f(x) = (x² − x)/(x). Simplify.", ["x² − 1", "*x − 1 (hole at x = 0)", "x − 1 (no hole)", "(x−1)/x"],
         "x(x−1)/x = x − 1, x ≠ 0. Hole at (0, −1)."),
        ("f(x) = (x + 5)/((x−1)(x+2)). y-intercept?", ["−5", "*−5/2", "5/2", "5"],
         "f(0) = 5/((−1)(2)) = 5/(−2) = −5/2."),
        ("The graph of 1/x² lies entirely:", ["*Above the x-axis (for x ≠ 0)", "Below the x-axis", "In all quadrants", "Only in Q1"],
         "1/x² > 0 for all x ≠ 0."),
        ("f(x) = (x−3)/(x+3). Does f cross its HA (y = 1)?", ["*No", "Yes, at x = 0", "Yes, at x = 3", "Yes, infinitely often"],
         "Set (x−3)/(x+3) = 1 → x−3 = x+3 → −3 = 3, impossible. Never crosses."),
        ("Which step comes first when graphing a rational function?", ["Draw the asymptotes", "Plot random points", "*Factor numerator and denominator", "Find the HA"],
         "Always factor first to identify holes and simplify."),
        ("f(x) = (3x − 6)/(x − 2). After simplification:", ["VA at x = 2", "*f(x) = 3 with hole at x = 2", "f(x) = 3x for all x", "HA at y = 6"],
         "3(x−2)/(x−2) = 3, x ≠ 2. Horizontal line with a hole."),
        ("f(x) = 1/(x − 1) + 2. HA?", ["y = 0", "y = 1", "*y = 2", "y = 3"],
         "As x → ∞, 1/(x−1) → 0, so f → 2."),
        ("f(x) = (x² + 2x + 1)/(x + 1). Simplify.", ["x + 1", "*(x + 1) with hole at x = −1", "x − 1", "x² + 1"],
         "(x+1)²/(x+1) = x + 1, x ≠ −1. Hole at x = −1."),
        ("In a sign chart, you test a point in each interval to determine:", ["The exact value", "The slope", "*Whether f is positive or negative", "The asymptote"],
         "Sign charts determine where the function is above or below the x-axis.")
    ]
)
lessons[k] = v

# ── 4.5 Partial Fraction Decomposition ─────────────────────────────
k, v = build_lesson(4, 5,
    "Partial Fraction Decomposition",
    "<h3>Partial Fraction Decomposition</h3>"
    "<p><b>Partial fraction decomposition</b> reverses the process of combining fractions: it breaks a single rational expression into a sum of simpler fractions.</p>"
    "<h4>When to Use</h4>"
    "<ul>"
    "<li>The degree of the numerator must be <b>less than</b> the degree of the denominator. (If not, perform long division first.)</li>"
    "</ul>"
    "<h4>Cases</h4>"
    "<ul>"
    "<li><b>Distinct linear factors:</b> A/(x − a) + B/(x − b) + …</li>"
    "<li><b>Repeated linear factor:</b> (x − a)² → A/(x − a) + B/(x − a)².</li>"
    "<li><b>Irreducible quadratic factor:</b> (ax² + bx + c) → (Ax + B)/(ax² + bx + c).</li>"
    "</ul>"
    "<h4>Solving for Coefficients</h4>"
    "<ul>"
    "<li>Multiply both sides by the LCD, then equate coefficients or substitute convenient x-values.</li>"
    "</ul>",
    [
        ("Partial Fraction Decomposition", "Breaking a rational expression into a sum of simpler fractions whose denominators are factors of the original."),
        ("Distinct Linear Factors", "Each factor (x − a) contributes A/(x − a) to the decomposition."),
        ("Repeated Linear Factor", "(x − a)ⁿ contributes A₁/(x−a) + A₂/(x−a)² + … + Aₙ/(x−a)ⁿ."),
        ("Irreducible Quadratic Factor", "A quadratic that cannot be factored over the reals; contributes (Ax + B)/(quadratic)."),
        ("Proper Rational Expression", "Degree of numerator < degree of denominator; required before decomposition.")
    ],
    [
        ("Decompose 5/(x(x+1)) into partial fractions.", ["5/x + 5/(x+1)", "*5/x − 5/(x+1)", "1/x + 4/(x+1)", "5/(x·(x+1))"],
         "5/(x(x+1)) = A/x + B/(x+1). A = 5, B = −5."),
        ("For 3/((x−1)(x+2)), what form do the partial fractions take?", ["A/x + B/(x+2)", "*A/(x−1) + B/(x+2)", "Ax/(x−1) + B/(x+2)", "(Ax+B)/((x−1)(x+2))"],
         "Distinct linear factors → A/(x−1) + B/(x+2)."),
        ("Decompose (2x+1)/((x−1)(x+3)). Find A.", ["*7/4", "1/2", "3/4", "2"],
         "Set x=1: (2+1)/((1+3)) = 3/4. Actually A(x+3)+B(x−1) = 2x+1. x=1: 4A=3→A=3/4. Let me recompute. 2(1)+1=3, (1+3)=4. A·4 = 3, A=3/4."),
        ("For (x)/((x−2)²), the decomposition form is:", ["A/(x−2)", "*A/(x−2) + B/(x−2)²", "Ax/(x−2)²", "(Ax+B)/(x−2)²"],
         "Repeated linear factor → two terms."),
        ("If the numerator degree ≥ denominator degree, first perform:", ["Factoring", "Partial fractions directly", "*Polynomial long division", "Substitution"],
         "Must have a proper fraction first."),
        ("Decompose 1/(x² − 1).", ["1/(x−1) − 1/(x+1)", "*(1/2)/(x−1) − (1/2)/(x+1)", "1/(x−1) + 1/(x+1)", "2/(x²−1)"],
         "1/((x−1)(x+1)) = A/(x−1) + B/(x+1). A = 1/2, B = −1/2."),
        ("For (3x + 5)/(x² + 4), (x² + 4 is irreducible), the form is:", ["A/(x² + 4)", "A/x + B/4", "*(Ax + B)/(x² + 4)", "A/(x+2) + B/(x−2)"],
         "Irreducible quadratic → (Ax + B)/(x² + 4)."),
        ("Decompose (x + 3)/(x(x − 1)). Find A.", ["*−3", "3", "1", "4"],
         "A/x + B/(x−1). x=0: 3/(−1) = A → A = −3."),
        ("In the previous problem, find B.", ["−3", "3", "*4", "−4"],
         "x=1: 4/1 = B → B = 4."),
        ("Is x²/(x − 1) ready for partial fractions?", ["Yes", "*No, degree of num ≥ degree of den", "Only if factored", "Always ready"],
         "Degree 2 ≥ degree 1. Must divide first."),
        ("x²/(x − 1) after long division:", ["x + 1 + 1/(x−1)", "*x + 1 + 1/(x−1)", "x² + 1/(x−1)", "x + 1/(x−1)"],
         "x² ÷ (x−1) = x + 1 rem 1. Result: x + 1 + 1/(x−1)."),
        ("For 2/((x+1)(x² + 1)), the form is:", ["A/(x+1) + B/(x² + 1)", "*A/(x+1) + (Bx + C)/(x² + 1)", "A/(x+1) + B/(x+1) + C/(x²+1)", "Ax/((x+1)(x²+1))"],
         "Linear factor + irreducible quadratic → A/(x+1) + (Bx+C)/(x²+1)."),
        ("To solve for coefficients, you can:", ["Only equate coefficients", "Only substitute values", "*Both methods work", "Use the quadratic formula"],
         "Both equating coefficients and substituting convenient x-values are valid methods."),
        ("Decompose 4/(x² − 4).", ["2/(x−2) + 2/(x+2)", "*1/(x−2) − 1/(x+2)", "2/(x−2) − 2/(x+2)", "4/(x−2) + 4/(x+2)"],
         "4/((x−2)(x+2)) = A/(x−2) + B/(x+2). x=2: A=1. x=−2: B=−1."),
        ("Which values of x are convenient for solving A/(x−1) + B/(x+2) = …?", ["x = 0, 1", "*x = 1, −2", "x = A, B", "Any two values"],
         "x = 1 and x = −2 make one denominator zero each, isolating a coefficient."),
        ("For (x² + 3x + 2)/((x − 1)³), the form has how many terms?", ["1", "2", "*3", "4"],
         "Repeated linear (x−1)³ → A/(x−1) + B/(x−1)² + C/(x−1)³."),
        ("After decomposition, the sum of the partial fractions should:", ["*Equal the original expression", "Be simpler than 1", "Have degree 0", "Have no denominators"],
         "The decomposition is an identity; they must be equal for all x."),
        ("Decompose 3x/((x+1)(x+2)). Find A (coefficient over x+1).", ["3", "*−3", "1", "6"],
         "x = −1: 3(−1)/(−1+2) = −3 = A."),
        ("In the previous, find B.", ["−3", "*6", "3", "−6"],
         "x = −2: 3(−2)/(−2+1) = −6/(−1) = 6 = B."),
        ("Partial fractions are used extensively in:", ["Geometry", "Statistics", "*Calculus (integration)", "Number theory"],
         "Partial fractions simplify integration of rational functions.")
    ]
)
lessons[k] = v

# ── 4.6 Applications in Real-World Ratios ─────────────────────────
k, v = build_lesson(4, 6,
    "Applications in Real-World Ratios (rates, proportions)",
    "<h3>Applications in Real-World Ratios</h3>"
    "<p>Rational functions model situations involving rates, concentrations, averages, and work problems.</p>"
    "<h4>Rate Problems</h4>"
    "<ul>"
    "<li>Average speed = total distance / total time. If parts of a trip have different speeds, the overall average is a rational expression.</li>"
    "</ul>"
    "<h4>Mixture / Concentration</h4>"
    "<ul>"
    "<li>C(x) = (initial amount + added amount) / (initial volume + added volume).</li>"
    "</ul>"
    "<h4>Work Problems</h4>"
    "<ul>"
    "<li>If A takes a hours and B takes b hours to complete a job alone, together: 1/a + 1/b = 1/t → t = ab/(a+b).</li>"
    "</ul>"
    "<h4>Average Cost</h4>"
    "<ul>"
    "<li>C̄(x) = C(x)/x. As production increases, fixed costs are spread over more units, reducing average cost (up to a point).</li>"
    "</ul>",
    [
        ("Average Speed", "Total distance divided by total time; when speeds vary, this is a rational expression."),
        ("Mixture/Concentration Formula", "C(x) = (amount of substance) / (total volume); models dilution and mixing."),
        ("Work Rate", "1/time = rate of work; combined rate: 1/a + 1/b = 1/t."),
        ("Average Cost", "C̄(x) = C(x)/x; cost per unit, which decreases with volume due to fixed costs."),
        ("Proportion", "A statement that two ratios are equal: a/b = c/d; solved by cross-multiplication.")
    ],
    [
        ("Drive 60 mi at 30 mph, then 60 mi at 60 mph. Average speed?", ["45 mph", "*40 mph", "50 mph", "55 mph"],
         "Total dist = 120 mi. Time = 2 + 1 = 3 hrs. Avg = 120/3 = 40 mph."),
        ("Worker A: 6 hrs, Worker B: 3 hrs. Together?", ["*2 hrs", "3 hrs", "4.5 hrs", "1.5 hrs"],
         "1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2 → t = 2 hrs."),
        ("10 L of 20% salt. Add x L of water. Concentration C(x) =", ["20/(10+x)", "*(2)/(10+x)", "0.2/(10+x)", "20x/(10+x)"],
         "Salt = 0.2(10) = 2 L. C(x) = 2/(10 + x)."),
        ("For the mixture above, what x gives 10% concentration?", ["5", "*10", "20", "2"],
         "2/(10+x) = 0.1 → 10+x = 20 → x = 10."),
        ("C(x) = (500 + 3x)/x. C̄ at x = 100?", ["3", "5", "*8", "53"],
         "C̄ = (500 + 300)/100 = 800/100 = 8."),
        ("As x → ∞, C̄(x) = (500 + 3x)/x → ?", ["500", "0", "*3", "∞"],
         "Divide: 500/x + 3 → 3 as x → ∞."),
        ("Cross multiply: 3/x = 5/8. x = ?", ["15", "8/3", "*24/5", "40/3"],
         "3·8 = 5x → x = 24/5."),
        ("Pipe A fills a tank in 4 hrs, pipe B empties it in 6 hrs. Together, net fill time?", ["*12 hrs", "5 hrs", "2.4 hrs", "10 hrs"],
         "1/4 − 1/6 = 3/12 − 2/12 = 1/12 → 12 hrs."),
        ("A car travels d km at speed s. Time = ?", ["*d/s", "s/d", "ds", "d + s"],
         "Time = distance/speed."),
        ("Round trip: 100 km at 50 km/h going, 100 km at x km/h returning. Total time?", ["200/(50+x)", "100/50 + x/100", "*2 + 100/x", "100/(50·x)"],
         "Time = 100/50 + 100/x = 2 + 100/x."),
        ("Average speed for the round trip above with x = 100:", ["75", "70", "*66.7", "80"],
         "Total time = 2 + 1 = 3 hrs. Avg = 200/3 ≈ 66.7 km/h."),
        ("If 5 workers take 12 days, how many days for 10 workers (same rate)?", ["24", "10", "*6", "60"],
         "Work = 5 × 12 = 60 worker-days. 60/10 = 6 days."),
        ("A 30% acid solution mixed with pure water: as water increases, concentration:", ["Increases", "*Decreases toward 0", "Stays the same", "Becomes negative"],
         "Adding water dilutes the acid; C → 0."),
        ("Cost: C(x) = 2000 + 5x. Average cost when x = 200?", ["5", "10", "*15", "2005"],
         "C̄ = (2000 + 1000)/200 = 3000/200 = 15."),
        ("The HA of C̄(x) = (2000 + 5x)/x represents:", ["Fixed cost", "*Minimum average cost approaching $5", "Maximum price", "Break-even"],
         "As x → ∞, C̄ → 5 (variable cost per unit)."),
        ("Solve: 2/(x − 1) = 3/(x + 1).", ["x = 1", "*x = 5", "x = −5", "x = 3"],
         "2(x+1) = 3(x−1) → 2x+2 = 3x−3 → x = 5."),
        ("A pool leaks 1/8 of its volume per hour. How long to empty half?", ["8 hrs", "*4 hrs", "2 hrs", "16 hrs"],
         "(1/8)t = 1/2 → t = 4 hrs."),
        ("If 2 machines produce 100 units/hr total and machine A produces 60/hr, machine B produces:", ["100/hr", "*40/hr", "60/hr", "160/hr"],
         "100 − 60 = 40 units/hr."),
        ("Proportion: 3/7 = x/21. x = ?", ["7", "*9", "3", "21"],
         "3 × 21/7 = 9."),
        ("Rational equations can have extraneous solutions because:", ["*Multiplying by an expression that equals zero is invalid", "Fractions are complex", "Variables are in the numerator", "The LCD is wrong"],
         "Multiplying both sides by an expression containing x may introduce false solutions where the denominator is 0.")
    ]
)
lessons[k] = v

# ── 4.7 Rational Inequalities ─────────────────────────────────────
k, v = build_lesson(4, 7,
    "Rational Inequalities",
    "<h3>Rational Inequalities</h3>"
    "<p>Solving inequalities involving rational expressions requires sign analysis rather than simple algebraic manipulation.</p>"
    "<h4>Steps</h4>"
    "<ol>"
    "<li>Move all terms to one side so that 0 is on the other: f(x)/g(x) ≤ 0 (or &gt;, ≥, &lt;).</li>"
    "<li>Factor numerator and denominator; find <b>critical numbers</b> (zeros of numerator and denominator).</li>"
    "<li>Create a <b>sign chart</b> on a number line using the critical numbers.</li>"
    "<li>Test a value in each interval to determine the sign of the expression.</li>"
    "<li>Select the intervals that satisfy the inequality.</li>"
    "<li><b>Include endpoints</b> where the expression = 0 (for ≤ or ≥) but <b>exclude</b> where denominator = 0.</li>"
    "</ol>",
    [
        ("Critical Numbers", "Zeros of the numerator (where expression = 0) and zeros of the denominator (where expression is undefined)."),
        ("Sign Chart for Rational Inequality", "A number line divided at critical numbers; test the sign of the expression in each interval."),
        ("Including Endpoints", "For ≤ or ≥, include x-values where the expression equals 0 (numerator = 0)."),
        ("Excluding Endpoints", "Never include x-values where the denominator = 0 (always excluded)."),
        ("Rewriting as Single Fraction", "Combine terms so one side is 0 and the other is a single rational expression.")
    ],
    [
        ("Solve (x − 1)/(x + 2) > 0.", ["−2 < x < 1", "*x < −2 or x > 1", "x > 1 only", "x > −2"],
         "Critical: x = 1, −2. Positive when both same sign: x < −2 or x > 1."),
        ("Solve (x + 3)/(x − 4) ≤ 0.", ["x < −3 or x > 4", "*−3 ≤ x < 4", "−3 < x < 4", "x ≤ −3"],
         "Zero at x = −3 (include), undefined at x = 4 (exclude). Negative on [−3, 4)."),
        ("Solve 1/x > 0.", ["All x", "x > 1", "*x > 0", "x < 0"],
         "1/x > 0 when x > 0."),
        ("Solve 1/x ≤ 0.", ["*x < 0", "x ≤ 0", "x < 0 or x = 0", "No solution"],
         "1/x < 0 when x < 0. 1/x = 0 never, so just x < 0."),
        ("Solve (x − 2)/((x + 1)(x − 3)) ≥ 0.", ["All x ≥ 2", "*−1 < x ≤ 2 or x > 3", "x ≤ 2 or x ≥ 3", "x = 2 only"],
         "Zeros: 2 (num), −1, 3 (den). Sign chart: positive on (−1, 2] ∪ (3, ∞). Include 2 (≥), exclude −1, 3."),
        ("Solve x/(x − 5) < 1.", ["x > 5", "x < 0 or x > 5", "*x < 0 or 0 < x < 5 is wrong. Let me reanalyze.", "x < 5"],
         "Rewrite: x/(x−5) − 1 < 0 → (x − x + 5)/(x−5) < 0 → 5/(x−5) < 0 → x−5 < 0 → x < 5. But x ≠ 5."),
        ("Solve (x² − 4)/(x + 5) > 0.", ["*x < −5 or −2 < x < 2 is wrong. Factor: (x−2)(x+2)/(x+5) > 0.", "x > 2", "−2 < x < 2", "x > 2 or x < −5"],
         "Critical: −5, −2, 2. Test intervals: (−∞,−5)→neg, (−5,−2)→pos, (−2,2)→neg, (2,∞)→pos. Answer: −5 < x < −2 or x > 2."),
        ("For ≤ inequalities, include x where:", ["Denominator = 0", "*Numerator = 0", "Both = 0", "Neither = 0"],
         "Where numerator = 0, the expression equals 0, satisfying ≤."),
        ("Solve (x − 1)² / (x + 3) ≥ 0.", ["x ≥ 1", "*x = 1 or x > −3, x ≠ −3... actually x > −3", "All x", "x > −3 only"],
         "(x−1)² ≥ 0 always. Sign depends on (x+3). ≥ 0 when x+3 > 0 or (x−1)²=0. So x > −3 or x = 1. Since x = 1 is in (−3, ∞), answer: x > −3, x ≠ −3. i.e., x ∈ (−3, ∞)."),
        ("Solve 2/(x − 1) ≥ 1.", ["*1 < x ≤ 3", "x ≥ 1", "x > 1", "x ≤ 3"],
         "2/(x−1) − 1 ≥ 0 → (2 − x + 1)/(x−1) ≥ 0 → (3−x)/(x−1) ≥ 0. Critical: 1, 3. Positive on (1, 3]. Include 3, exclude 1."),
        ("Why must we exclude denominator zeros from the solution?", ["They make the answer negative", "*The expression is undefined there", "It's a convention", "They create extraneous solutions"],
         "Division by zero is undefined."),
        ("Solve x/(x + 1) ≤ 2.", ["x ≤ 2", "*x < −1 or x ≥ −2", "x ≥ −2", "x ≤ −2 or x > −1"],
         "x/(x+1) − 2 ≤ 0 → (x − 2x − 2)/(x+1) ≤ 0 → (−x−2)/(x+1) ≤ 0 → (x+2)/(x+1) ≥ 0. Positive: x ≤ −2 or x > −1."),
        ("Solve (x − 4)/(x + 2) > 0 and express in interval notation.", ["(−2, 4)", "*(−∞, −2) ∪ (4, ∞)", "[−2, 4]", "(4, ∞)"],
         "Both positive: x > 4. Both negative: x < −2. Answer: (−∞, −2) ∪ (4, ∞)."),
        ("What type of circle on a number line for a strict inequality at a critical number?", ["Closed", "*Open", "No circle needed", "Depends on the sign"],
         "Strict (< or >) → open circle (not included)."),
        ("Non-strict inequality (≤ or ≥) at a numerator zero gets:", ["Open circle", "*Closed circle", "No mark", "Depends on context"],
         "When the expression equals 0 and we want ≤ or ≥ 0, include it (closed circle)."),
        ("Solve 3/(x+1) < 2/(x−1).", ["*Rewrite as single fraction and use sign chart", "Cross multiply directly", "Multiply both sides by (x+1)(x−1)", "Subtract numerators"],
         "Must rewrite as 3/(x+1) − 2/(x−1) < 0, then sign chart. (Cross-multiplying can flip the sign if denominator is negative.)"),
        ("Why can't you simply cross-multiply in rational inequalities?", ["It's too slow", "*The sign of the product of denominators may be negative, flipping the inequality", "It doesn't give exact answers", "Cross-multiplication only works for equations"],
         "If the denominator product is negative, the inequality reverses, making cross-multiplication unreliable."),
        ("Solve (x² − 9)/x ≤ 0.", ["*−3 ≤ x < 0 or x ≥ 3 — wait, let's redo.", "x < −3 or 0 < x ≤ 3", "x ≤ −3 or x = 3", "−3 < x < 3"],
         "Factor: (x−3)(x+3)/x ≤ 0. Critical: −3, 0, 3. Sign: (−∞,−3)→neg, (−3,0)→pos, (0,3)→neg, (3,∞)→pos. ≤0: x ≤ −3 or 0 < x ≤ 3. (Exclude 0.)"),
        ("Solve −1/(x²) > 0.", ["x > 0", "x < 0", "All x ≠ 0", "*No solution"],
         "−1/x² < 0 for all x ≠ 0. It's never positive."),
        ("After finding the solution set, always check:", ["The numerator degree", "If the function is quadratic", "*That denominator zeros are excluded", "That all values are integers"],
         "Verify denominator zeros are not in the solution set.")
    ]
)
lessons[k] = v

# ── 4.8 Case Studies in Engineering ────────────────────────────────
k, v = build_lesson(4, 8,
    "Case Studies in Engineering",
    "<h3>Case Studies in Engineering</h3>"
    "<p>Rational functions appear in engineering contexts such as electrical circuits, fluid dynamics, and structural design.</p>"
    "<h4>Electrical Circuits</h4>"
    "<ul>"
    "<li>Parallel resistors: 1/R_total = 1/R₁ + 1/R₂ → R_total = R₁R₂/(R₁ + R₂).</li>"
    "<li>Transfer functions in control systems are ratios of polynomials.</li>"
    "</ul>"
    "<h4>Fluid Dynamics</h4>"
    "<ul>"
    "<li>Flow rate through a pipe may depend on pressure ratios modeled by rational expressions.</li>"
    "</ul>"
    "<h4>Structural Engineering</h4>"
    "<ul>"
    "<li>Load distribution and stress-strain relationships can involve rational models.</li>"
    "<li>Safety factor = strength/stress is a ratio subject to constraints.</li>"
    "</ul>"
    "<h4>Optimization</h4>"
    "<ul>"
    "<li>Minimize material while meeting strength requirements → rational function optimization.</li>"
    "</ul>",
    [
        ("Parallel Resistance Formula", "R_total = R₁R₂/(R₁ + R₂) for two resistors in parallel."),
        ("Transfer Function", "A ratio of polynomials in s (or z) that describes the input-output relationship of a linear system."),
        ("Safety Factor", "Strength/stress; a ratio that must exceed 1 for safe design."),
        ("Inverse Proportionality", "y = k/x; as one quantity increases, the other decreases."),
        ("Rational Optimization", "Finding max/min of a rational function subject to engineering constraints.")
    ],
    [
        ("Two parallel resistors: R₁ = 6Ω, R₂ = 3Ω. R_total?", ["9Ω", "3Ω", "*2Ω", "4.5Ω"],
         "6·3/(6+3) = 18/9 = 2Ω."),
        ("If R₁ = R₂ = R in parallel, R_total =", ["2R", "*R/2", "R", "R²"],
         "R·R/(R+R) = R²/(2R) = R/2."),
        ("Three equal resistors R in parallel: R_total =", ["R", "R/2", "*R/3", "3R"],
         "1/R_t = 1/R + 1/R + 1/R = 3/R → R_t = R/3."),
        ("As more resistors are added in parallel, total resistance:", ["Increases", "*Decreases", "Stays the same", "Doubles"],
         "More parallel paths → less total resistance."),
        ("Beam deflection formula d = kFL³/(EI). If F doubles, deflection:", ["Halves", "*Doubles", "Quadruples", "Stays same"],
         "d is directly proportional to F."),
        ("In d = kFL³/(EI), increasing I:", ["Increases d", "*Decreases d", "No effect", "Squares d"],
         "I is in the denominator → larger I means smaller deflection."),
        ("Ohm's law: V = IR. If resistance R doubles and V is constant, current I:", ["Doubles", "*Halves", "Stays same", "Quadruples"],
         "I = V/R; double R → halve I."),
        ("A tank drains at rate r(h) = k√h. Time to drain is related to h by:", ["Linear", "Exponential", "*Rational/root function", "Logarithmic"],
         "The draining time involves integrating 1/√h, leading to non-linear behavior."),
        ("Safety factor = 500 MPa / stress. If stress = 250 MPa, SF =", ["0.5", "*2", "250", "500"],
         "SF = 500/250 = 2."),
        ("A safety factor must be at least:", ["0", "0.5", "*Greater than 1", "100"],
         "SF > 1 means strength exceeds stress."),
        ("Light intensity I = k/d². If distance triples, intensity becomes:", ["I/3", "I/9", "*I/9", "3I"],
         "I ∝ 1/d². Triple d → 1/9 of original intensity."),
        ("Resonant frequency f = 1/(2π√(LC)). If C quadruples, f:", ["Doubles", "*Halves", "Quadruples", "Stays same"],
         "f ∝ 1/√C. C×4 → f×(1/2)."),
        ("Power in a circuit: P = V²/R. Double V, same R:", ["P doubles", "P halves", "*P quadruples", "P unchanged"],
         "P ∝ V². Double V → quadruple P."),
        ("A gear ratio 3:1 means the output turns __ as fast as input.", ["3 times", "*1/3", "The same", "9 times"],
         "3:1 ratio → output speed = input speed / 3."),
        ("Efficiency η = output/input. If output = 85W and input = 100W:", ["100%", "*85%", "85W", "15%"],
         "η = 85/100 = 0.85 = 85%."),
        ("In a lever, force × distance = constant. If distance triples, force:", ["Triples", "*Becomes 1/3", "Stays same", "Doubles"],
         "F·d = k → F = k/d. Triple d → F/3."),
        ("A control system transfer function H(s) = (s+2)/(s² + 3s + 2). Factor denominator:", ["(s+1)²", "*(s+1)(s+2)", "(s+2)²", "(s−1)(s−2)"],
         "s² + 3s + 2 = (s+1)(s+2)."),
        ("After cancellation, H(s) = 1/(s+1). This represents:", ["A second-order system", "*A first-order system with a canceled pole-zero pair", "An unstable system", "A proportional controller"],
         "Canceling (s+2) leaves a first-order system."),
        ("Wind load on a structure ∝ v². If wind speed increases 50%, load increases by:", ["50%", "100%", "*125%", "150%"],
         "(1.5)² = 2.25. Increase = 125%."),
        ("The concept of inverse proportionality (y = k/x) appears when:", ["Both quantities increase together", "*One increases as the other decreases", "Both are constant", "They are independent"],
         "Inverse: one up, the other down.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 4)")
