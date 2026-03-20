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

# ── 3.1 Characteristics of Polynomials ─────────────────────────────
k, v = build_lesson(3, 1,
    "Characteristics of Polynomials (degree, leading coefficient)",
    "<h3>Characteristics of Polynomials</h3>"
    "<p>A <b>polynomial function</b> has the form f(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + … + a₁x + a₀, where the exponents are non-negative integers and the coefficients are real numbers.</p>"
    "<h4>Key Vocabulary</h4>"
    "<ul>"
    "<li><b>Degree:</b> The highest exponent. It determines the overall shape and maximum number of turning points (≤ n − 1).</li>"
    "<li><b>Leading coefficient (aₙ):</b> The coefficient of the highest-degree term. Its sign determines end behavior.</li>"
    "<li><b>Constant term (a₀):</b> The y-intercept when x = 0.</li>"
    "</ul>"
    "<h4>Classification by Degree</h4>"
    "<ul>"
    "<li>Degree 0 → constant, Degree 1 → linear, Degree 2 → quadratic, Degree 3 → cubic, Degree 4 → quartic, Degree 5 → quintic.</li>"
    "</ul>"
    "<h4>Number of Zeros</h4>"
    "<ul>"
    "<li>A polynomial of degree n has <b>at most n real zeros</b> (Fundamental Theorem of Algebra: exactly n zeros counting multiplicity over the complex numbers).</li>"
    "</ul>",
    [
        ("Degree of a Polynomial", "The highest exponent of x in the polynomial; determines the function's overall behavior."),
        ("Leading Coefficient", "The coefficient of the term with the highest degree; its sign affects end behavior."),
        ("Polynomial", "A function of the form aₙxⁿ + … + a₁x + a₀ with non-negative integer exponents."),
        ("Turning Point", "A point where the graph changes direction; a degree-n polynomial has at most n − 1 turning points."),
        ("Fundamental Theorem of Algebra", "Every polynomial of degree n ≥ 1 has exactly n zeros (real or complex, counting multiplicity).")
    ],
    [
        ("What is the degree of f(x) = 4x³ − 2x + 7?", ["1", "2", "*3", "4"],
         "The highest exponent is 3."),
        ("What is the leading coefficient of f(x) = −5x⁴ + 3x² − 1?", ["3", "1", "5", "*−5"],
         "The term with the highest degree is −5x⁴; leading coefficient is −5."),
        ("How many turning points can a degree-5 polynomial have at most?", ["5", "*4", "3", "6"],
         "At most n − 1 = 4 turning points."),
        ("A cubic polynomial has at most how many real zeros?", ["1", "2", "*3", "4"],
         "A degree-3 polynomial has at most 3 real zeros."),
        ("Classify: f(x) = 6x² − x + 2.", ["Linear", "*Quadratic", "Cubic", "Quartic"],
         "Highest degree is 2 → quadratic."),
        ("The y-intercept of f(x) = 3x⁴ − x² + 5 is:", ["3", "−1", "*5", "0"],
         "f(0) = 5."),
        ("Which is NOT a polynomial?", ["x³ + 2x", "7", "*x⁻¹ + 3", "x⁵ − x"],
         "x⁻¹ has a negative exponent, so it's not a polynomial."),
        ("What is the degree of a constant function f(x) = 8?", ["*0", "1", "8", "Undefined"],
         "A nonzero constant has degree 0."),
        ("How many complex zeros does x⁴ + 1 have?", ["0", "2", "*4", "1"],
         "By the Fundamental Theorem of Algebra, a degree-4 polynomial has exactly 4 complex zeros."),
        ("The leading term of f(x) = 2x − 9x³ + x⁵ is:", ["2x", "−9x³", "*x⁵", "−9"],
         "Rewrite in standard form: x⁵ − 9x³ + 2x. Leading term is x⁵."),
        ("A polynomial of degree 6 has at most __ x-intercepts.", ["5", "*6", "7", "12"],
         "At most n = 6 real zeros, so at most 6 x-intercepts."),
        ("What type of polynomial has degree 4?", ["Cubic", "*Quartic", "Quintic", "Linear"],
         "Degree 4 is called quartic."),
        ("If f(x) = (x − 1)(x + 2)(x − 3), the degree is:", ["2", "*3", "4", "6"],
         "Three linear factors multiplied → degree 3."),
        ("The leading coefficient of f(x) = −x⁷ + 4x³ is:", ["1", "4", "*−1", "7"],
         "The leading term −x⁷ has coefficient −1."),
        ("A polynomial f(x) of degree 3 must cross the x-axis:", ["0 times", "2 times", "*At least 1 time", "Exactly 3 times"],
         "Odd-degree polynomials always have at least one real zero."),
        ("Which can be a polynomial?", ["f(x) = √x + 1", "f(x) = 1/x", "*f(x) = x⁴ − πx + 2", "f(x) = 2ˣ"],
         "x⁴ − πx + 2 has non-negative integer exponents and real coefficients."),
        ("The minimum number of real zeros of a degree-4 polynomial is:", ["*0", "1", "2", "4"],
         "An even-degree polynomial can have 0 real zeros (e.g., x⁴ + 1)."),
        ("f(x) = 5x³ − 2x² + x − 4. What is f(0)?", ["5", "−2", "1", "*−4"],
         "f(0) = −4 (constant term)."),
        ("The number of terms in f(x) = x³ + 2x is:", ["1", "*2", "3", "4"],
         "There are 2 terms: x³ and 2x."),
        ("Is f(x) = x² + 2x + 1 a polynomial?", ["*Yes", "No", "Only if x > 0", "Only if factored"],
         "It has non-negative integer exponents and real coefficients.")
    ]
)
lessons[k] = v

# ── 3.2 End Behavior & Graph Shapes ────────────────────────────────
k, v = build_lesson(3, 2,
    "End Behavior & Graph Shapes",
    "<h3>End Behavior &amp; Graph Shapes</h3>"
    "<p><b>End behavior</b> describes what happens to f(x) as x → +∞ and x → −∞. It depends on the <b>degree</b> and the <b>sign of the leading coefficient</b>.</p>"
    "<h4>Rules</h4>"
    "<ul>"
    "<li><b>Even degree, positive leading coeff:</b> ↑ left and ↑ right (both ends rise).</li>"
    "<li><b>Even degree, negative leading coeff:</b> ↓ left and ↓ right (both ends fall).</li>"
    "<li><b>Odd degree, positive leading coeff:</b> ↓ left and ↑ right.</li>"
    "<li><b>Odd degree, negative leading coeff:</b> ↑ left and ↓ right.</li>"
    "</ul>"
    "<h4>Graph Shape Clues</h4>"
    "<ul>"
    "<li>Degree 2 (quadratic): parabola shape.</li>"
    "<li>Degree 3 (cubic): S-shaped curve.</li>"
    "<li>Degree 4 (quartic): W- or M-shaped (up to 3 turning points).</li>"
    "<li>The number of turning points is at most n − 1.</li>"
    "</ul>",
    [
        ("End Behavior", "The direction f(x) heads as x → +∞ and x → −∞; determined by degree and leading coefficient."),
        ("Even Degree, Positive Lead", "Both ends rise: as x → ±∞, f(x) → +∞."),
        ("Even Degree, Negative Lead", "Both ends fall: as x → ±∞, f(x) → −∞."),
        ("Odd Degree, Positive Lead", "Falls left, rises right: as x → −∞ f(x) → −∞; as x → +∞ f(x) → +∞."),
        ("Odd Degree, Negative Lead", "Rises left, falls right: as x → −∞ f(x) → +∞; as x → +∞ f(x) → −∞.")
    ],
    [
        ("As x → ∞, f(x) = x³ →", ["−∞", "*+∞", "0", "1"],
         "Odd degree, positive leading coeff → rises to +∞."),
        ("As x → −∞, f(x) = x³ →", ["*−∞", "+∞", "0", "1"],
         "Odd degree, positive lead → falls to −∞ on left."),
        ("As x → ∞, f(x) = −x⁴ →", ["*−∞", "+∞", "0", "Undefined"],
         "Even degree, negative lead → both ends fall."),
        ("As x → −∞, f(x) = −x⁴ →", ["*−∞", "+∞", "0", "1"],
         "Even degree, negative lead → both ends fall."),
        ("f(x) = 2x⁵ − x²: as x → +∞, f(x) →", ["−∞", "*+∞", "0", "2"],
         "Odd degree (5), positive lead (2) → rises right."),
        ("Describe the end behavior of f(x) = −3x³ + x.", ["Falls left, rises right", "*Rises left, falls right", "Both rise", "Both fall"],
         "Odd degree, negative lead → rises left, falls right."),
        ("How many turning points can f(x) = x⁴ − 3x² have at most?", ["2", "*3", "4", "1"],
         "Degree 4 → at most 3 turning points."),
        ("Which could be the graph of a degree-3 polynomial?", ["Parabola", "*S-curve", "W-shape", "Straight line"],
         "Cubic functions have an S-shaped curve."),
        ("f(x) = x² + 1: both ends go to:", ["+∞ and −∞", "*+∞ and +∞", "−∞ and −∞", "0 and 0"],
         "Even degree, positive lead → both ends rise."),
        ("f(x) = −x⁶ + 5x: end behavior?", ["Both rise", "*Both fall", "Falls left, rises right", "Rises left, falls right"],
         "Even degree, negative lead → both ends fall."),
        ("Which degree always crosses the x-axis at least once?", ["2", "4", "*3", "6"],
         "Odd-degree polynomials must have at least one real zero."),
        ("f(x) = −2x⁵: as x → −∞, f →", ["−∞", "*+∞", "0", "−2"],
         "Odd degree, negative lead → rises left."),
        ("A degree-2 polynomial has at most __ turning points.", ["0", "*1", "2", "3"],
         "At most n − 1 = 1 turning point (the vertex)."),
        ("If the leading term is −7x⁸, the ends:", ["Both rise", "*Both fall", "Rise/fall", "Fall/rise"],
         "Even degree (8), negative lead → both ends fall."),
        ("f(x) = 0.5x³: end behavior same as:", ["*x³", "−x³", "x²", "−x²"],
         "Same sign leading coeff, same odd degree → same end behavior as x³."),
        ("A polynomial graph with both ends rising has:", ["*Even degree, positive lead", "Odd degree, positive lead", "Even degree, negative lead", "Odd degree, negative lead"],
         "Both ends up → even degree with positive leading coefficient."),
        ("f(x) = x(x − 1)(x + 2): degree?", ["2", "*3", "4", "1"],
         "Product of three linear factors → degree 3."),
        ("f(x) = x(x − 1)(x + 2): end behavior?", ["Both rise", "Both fall", "*Falls left, rises right", "Rises left, falls right"],
         "Degree 3, positive leading coeff (1) → falls left, rises right."),
        ("Maximum turning points of a quintic (degree 5)?", ["3", "*4", "5", "6"],
         "At most n − 1 = 4."),
        ("Which has end behavior: rises left, falls right?", ["x⁴", "*−x³", "x³", "−x⁴"],
         "Odd degree with negative lead → rises left, falls right.")
    ]
)
lessons[k] = v

# ── 3.3 Factoring Techniques (synthetic division, long division) ───
k, v = build_lesson(3, 3,
    "Factoring Techniques (synthetic division, long division)",
    "<h3>Factoring Techniques</h3>"
    "<p>Dividing polynomials is essential for finding factors and zeros of higher-degree polynomials.</p>"
    "<h4>Polynomial Long Division</h4>"
    "<ul>"
    "<li>Works exactly like numerical long division.</li>"
    "<li>Divide the leading term of the dividend by the leading term of the divisor, multiply, subtract, bring down, and repeat.</li>"
    "<li>Result: f(x) = d(x)·q(x) + r(x), where r has lower degree than d.</li>"
    "</ul>"
    "<h4>Synthetic Division</h4>"
    "<ul>"
    "<li>A shortcut when dividing by (x − c).</li>"
    "<li>Use only the coefficients; bring down, multiply by c, add, repeat.</li>"
    "<li>The last number is the remainder (also equals f(c) by the Remainder Theorem).</li>"
    "</ul>"
    "<h4>Remainder &amp; Factor Theorems</h4>"
    "<ul>"
    "<li><b>Remainder Theorem:</b> When f(x) is divided by (x − c), the remainder is f(c).</li>"
    "<li><b>Factor Theorem:</b> (x − c) is a factor of f(x) if and only if f(c) = 0.</li>"
    "</ul>",
    [
        ("Polynomial Long Division", "Divide leading terms, multiply, subtract, bring down, repeat; works for any polynomial divisor."),
        ("Synthetic Division", "A shortcut for dividing by (x − c) using only coefficients; faster than long division."),
        ("Remainder Theorem", "When f(x) is divided by (x − c), the remainder equals f(c)."),
        ("Factor Theorem", "(x − c) is a factor of f(x) if and only if f(c) = 0."),
        ("Quotient and Remainder", "f(x) = d(x)·q(x) + r(x); q is the quotient and r is the remainder.")
    ],
    [
        ("Divide x³ − 1 by x − 1. Quotient?", ["x − 1", "*x² + x + 1", "x² − x + 1", "x² + 1"],
         "x³ − 1 = (x − 1)(x² + x + 1)."),
        ("Use the Remainder Theorem: f(x) = x³ − 4x + 2. Find f(2).", ["0", "*2", "4", "−2"],
         "f(2) = 8 − 8 + 2 = 2, which is the remainder when dividing by (x − 2)."),
        ("Is (x − 3) a factor of x³ − 27?", ["*Yes", "No", "Only if x > 0", "Cannot tell"],
         "f(3) = 27 − 27 = 0, so (x − 3) is a factor."),
        ("Divide 2x² + 5x + 3 by x + 1. Quotient?", ["2x + 5", "*2x + 3", "2x − 3", "2x + 1"],
         "Long division or synthetic: quotient is 2x + 3, remainder 0."),
        ("Synthetic division of x³ + 2x² − 5x − 6 by (x − 2): remainder?", ["−6", "*0", "2", "4"],
         "f(2) = 8 + 8 − 10 − 6 = 0."),
        ("What does a remainder of 0 tell you?", ["The division is undefined", "*The divisor is a factor", "The polynomial is prime", "There's an error"],
         "Remainder 0 means the divisor divides evenly → it's a factor."),
        ("Divide x⁴ − 16 by x − 2. The remainder is:", ["*0", "16", "−16", "2"],
         "f(2) = 16 − 16 = 0."),
        ("In synthetic division by (x + 3), what value do you use?", ["3", "*−3", "1/3", "−1/3"],
         "x + 3 = x − (−3), so use c = −3."),
        ("f(x) = x³ − 6x² + 11x − 6. f(1) = ?", ["1", "*0", "−1", "6"],
         "1 − 6 + 11 − 6 = 0."),
        ("Since f(1) = 0 above, factor out:", ["(x + 1)", "*(x − 1)", "x", "(x − 6)"],
         "f(1) = 0 means (x − 1) is a factor."),
        ("After removing (x − 1), the remaining factor of x³ − 6x² + 11x − 6 is:", ["x² − 4x + 6", "*x² − 5x + 6", "x² − 6x + 6", "x² + 5x − 6"],
         "Synthetic division gives x² − 5x + 6 = (x − 2)(x − 3)."),
        ("Divide 3x³ + 5x² − 2x by x. Quotient?", ["3x³ + 5x² − 2", "*3x² + 5x − 2", "3x² + 5x", "x²"],
         "Each term divided by x: 3x² + 5x − 2."),
        ("The Factor Theorem says (x − c) is a factor iff:", ["f(x) = c", "*f(c) = 0", "f(0) = c", "c = 0"],
         "f(c) = 0 means (x − c) divides f(x) evenly."),
        ("Use synthetic division: x⁴ − 3x³ + x − 3 ÷ (x − 3). Remainder?", ["3", "−3", "*0", "1"],
         "f(3) = 81 − 81 + 3 − 3 = 0."),
        ("What is the degree of the quotient when dividing degree 5 by degree 2?", ["2", "*3", "5", "7"],
         "deg(quotient) = deg(dividend) − deg(divisor) = 5 − 2 = 3."),
        ("Divide x² + 3x + 2 by x + 2. Quotient and remainder?", ["*q = x + 1, r = 0", "q = x + 2, r = 0", "q = x − 1, r = 4", "q = x, r = 2"],
         "(x + 2)(x + 1) = x² + 3x + 2 → quotient x + 1, remainder 0."),
        ("Synthetic division: coefficients of x³ + 0x² + 0x − 8 divided by (x − 2).", ["1, 0, −8", "*1, 0, 0, −8", "1, −8", "1, 2, 0, −8"],
         "Include 0 placeholders for missing terms: 1, 0, 0, −8."),
        ("f(x) = 2x³ − 3x² + x − 5. Find f(−1).", ["−1", "−3", "*−11", "1"],
         "2(−1) − 3(1) + (−1) − 5 = −2 − 3 − 1 − 5 = −11."),
        ("When can synthetic division be used?", ["Any divisor", "Degree-2 divisors only", "*Only when dividing by (x − c)", "Only for degree-3 polynomials"],
         "Synthetic division is a shortcut specifically for linear divisors of the form (x − c)."),
        ("Divide x³ + 8 by x + 2. Quotient?", ["x² + 4", "x² − 4x + 4", "*x² − 2x + 4", "x² + 2x + 4"],
         "x³ + 8 = (x + 2)(x² − 2x + 4) (sum of cubes).")
    ]
)
lessons[k] = v

# ── 3.4 Roots, Zeros, and Multiplicity ─────────────────────────────
k, v = build_lesson(3, 4,
    "Roots, Zeros, and Multiplicity",
    "<h3>Roots, Zeros, and Multiplicity</h3>"
    "<p>The <b>zeros</b> (roots) of a polynomial f(x) are the x-values where f(x) = 0. They correspond to x-intercepts of the graph.</p>"
    "<h4>Multiplicity</h4>"
    "<ul>"
    "<li>If (x − c)ᵏ is a factor and k ≥ 1, then c is a zero of <b>multiplicity k</b>.</li>"
    "<li><b>Odd multiplicity:</b> the graph <b>crosses</b> the x-axis at x = c.</li>"
    "<li><b>Even multiplicity:</b> the graph <b>touches (bounces off)</b> the x-axis at x = c.</li>"
    "</ul>"
    "<h4>Finding Zeros</h4>"
    "<ul>"
    "<li>Factor the polynomial completely.</li>"
    "<li>Set each factor equal to zero.</li>"
    "<li>Use the quadratic formula for irreducible quadratic factors.</li>"
    "</ul>"
    "<h4>Writing a Polynomial from Zeros</h4>"
    "<ul>"
    "<li>If zeros are c₁, c₂, …, cₙ, then f(x) = a(x − c₁)(x − c₂)…(x − cₙ).</li>"
    "<li>Use a given point to find the leading coefficient a.</li>"
    "</ul>",
    [
        ("Zero / Root", "A value c where f(c) = 0; corresponds to an x-intercept."),
        ("Multiplicity", "The number of times a factor (x − c) appears; affects how the graph behaves at x = c."),
        ("Odd Multiplicity", "The graph crosses the x-axis at that zero."),
        ("Even Multiplicity", "The graph touches (bounces off) the x-axis at that zero without crossing."),
        ("Fundamental Theorem of Algebra", "A degree-n polynomial has exactly n zeros (real or complex, counting multiplicity).")
    ],
    [
        ("Find the zeros of f(x) = (x − 2)(x + 5).", ["2 and 5", "*2 and −5", "−2 and 5", "−2 and −5"],
         "Set each factor = 0: x = 2, x = −5."),
        ("What is the multiplicity of x = 3 in f(x) = (x − 3)²(x + 1)?", ["1", "*2", "3", "4"],
         "(x − 3) appears twice → multiplicity 2."),
        ("At a zero with even multiplicity, the graph:", ["*Touches and bounces", "Crosses", "Has a hole", "Is undefined"],
         "Even multiplicity → the graph touches but doesn't cross."),
        ("At a zero with odd multiplicity, the graph:", ["Bounces", "*Crosses", "Is tangent", "Has an asymptote"],
         "Odd multiplicity → the graph crosses the x-axis."),
        ("f(x) = x(x − 1)³(x + 2)². List the zeros and multiplicities.", ["*0(m=1), 1(m=3), −2(m=2)", "0(m=1), 1(m=2), −2(m=3)", "1(m=3), 2(m=2)", "0(m=1), −1(m=3), 2(m=2)"],
         "x: m=1, (x−1)³: m=3, (x+2)²: m=2."),
        ("What is the degree of f(x) = x(x − 1)³(x + 2)²?", ["3", "5", "*6", "4"],
         "1 + 3 + 2 = 6."),
        ("f(x) = (x − 4)². Does the graph cross or touch at x = 4?", ["Cross", "*Touch", "Neither", "Depends on other factors"],
         "Multiplicity 2 (even) → touches."),
        ("Write a polynomial with zeros at x = 1, 2, 3 (all multiplicity 1).", ["*f(x) = (x−1)(x−2)(x−3)", "f(x) = (x+1)(x+2)(x+3)", "f(x) = x(x−1)(x−2)", "f(x) = (x−1)²(x−2)"],
         "Each zero c gives a factor (x − c)."),
        ("f(x) = x⁴ − 5x² + 4. Factor completely.", ["(x−1)(x−4)", "*(x−1)(x+1)(x−2)(x+2)", "(x²−1)(x²+4)", "(x−2)²(x+2)²"],
         "x⁴ − 5x² + 4 = (x² − 1)(x² − 4) = (x−1)(x+1)(x−2)(x+2)."),
        ("How many zeros does the polynomial above have?", ["2", "3", "*4", "5"],
         "Four distinct real zeros: ±1, ±2."),
        ("f(x) = (x − 2)³. At x = 2 the graph:", ["Touches", "*Crosses (with flattening)", "Has a sharp turn", "Is undefined"],
         "Odd multiplicity 3 → crosses, but with a flattened shape near the zero."),
        ("Find a polynomial of degree 2 with zero at x = 5 of multiplicity 2.", ["(x + 5)²", "*(x − 5)²", "x² − 25", "x² − 5x"],
         "(x − 5)² is degree 2 with a double root at 5."),
        ("If f(x) is degree 4 and has zeros 1, −1, 2, −2, all multiplicity 1, the sum of zeros is:", ["4", "2", "*0", "−4"],
         "1 + (−1) + 2 + (−2) = 0."),
        ("f(x) = x³ − 3x² + 3x − 1. Factor.", ["(x − 1)(x² + 1)", "(x + 1)³", "*(x − 1)³", "(x − 1)(x² − 2x + 1)"],
         "x³ − 3x² + 3x − 1 = (x − 1)³. Zero x = 1 with multiplicity 3."),
        ("The graph of (x − 1)³ flattens near x = 1 because:", ["Even multiplicity", "*Higher odd multiplicity", "The leading coefficient is 1", "It has only one zero"],
         "A zero of multiplicity 3 creates an inflection-like flattening at the crossing point."),
        ("f(x) = (x + 3)²(x − 1). What are the x-intercepts?", ["−3 only", "1 only", "*−3 and 1", "3 and −1"],
         "Zeros: x = −3 (mult 2) and x = 1 (mult 1)."),
        ("At which intercept does f(x) above bounce?", ["x = 1", "*x = −3", "Both", "Neither"],
         "x = −3 has even multiplicity 2 → bounce."),
        ("How many times does f(x) = (x − 1)²(x + 2)³ cross the x-axis?", ["2", "*1", "3", "0"],
         "Only x = −2 (odd mult 3) crosses; x = 1 (even mult 2) bounces."),
        ("If f(x) has real coefficients and 2 + i is a zero, what else must be a zero?", ["−2 + i", "2 + i again", "*2 − i", "−2 − i"],
         "Complex zeros come in conjugate pairs: 2 − i."),
        ("Write a degree-3 polynomial with a double root at 0 and a root at 5.", ["x²(x − 5)", "*x²(x − 5)", "x(x − 5)²", "(x − 5)³"],
         "Double root at 0: x² factor. Root at 5: (x − 5). f(x) = x²(x − 5).")
    ]
)
lessons[k] = v

# ── 3.5 Intermediate Value Theorem ─────────────────────────────────
k, v = build_lesson(3, 5,
    "Intermediate Value Theorem",
    "<h3>Intermediate Value Theorem (IVT)</h3>"
    "<p>The <b>Intermediate Value Theorem</b> states: if f is continuous on [a, b] and N is any number between f(a) and f(b), then there exists at least one c in (a, b) such that f(c) = N.</p>"
    "<h4>Key Points</h4>"
    "<ul>"
    "<li>All polynomials are continuous everywhere, so IVT always applies to polynomials.</li>"
    "<li>Most commonly used with N = 0 to guarantee the existence of a <b>real zero</b> between a and b when f(a) and f(b) have <b>opposite signs</b>.</li>"
    "</ul>"
    "<h4>Applying the IVT</h4>"
    "<ol>"
    "<li>Evaluate f(a) and f(b).</li>"
    "<li>If f(a) and f(b) have opposite signs, the IVT guarantees at least one zero in (a, b).</li>"
    "<li>The theorem does NOT tell you the exact value of the zero—only that it exists.</li>"
    "</ol>"
    "<h4>Limitations</h4>"
    "<ul>"
    "<li>IVT requires <b>continuity</b>; it does not apply to functions with discontinuities on [a, b].</li>"
    "<li>A sign change is sufficient but not necessary—a zero can exist even without a sign change (e.g., touching the axis).</li>"
    "</ul>",
    [
        ("Intermediate Value Theorem", "If f is continuous on [a, b] and N is between f(a) and f(b), then f(c) = N for some c in (a, b)."),
        ("Continuous Function", "A function with no breaks, holes, or jumps; polynomials are continuous everywhere."),
        ("Sign Change", "When f(a) and f(b) have opposite signs, indicating a zero must exist between a and b."),
        ("Existence vs. Location", "IVT guarantees a zero exists in an interval but does not give its exact location."),
        ("Bisection Method", "A numerical technique using IVT repeatedly to narrow down the location of a zero.")
    ],
    [
        ("If f(1) = −3 and f(4) = 5, and f is continuous, IVT guarantees:", ["f has no zeros", "*f has at least one zero in (1, 4)", "f(2.5) = 0", "f has exactly one zero"],
         "Opposite signs → at least one zero in (1, 4)."),
        ("The IVT requires the function to be:", ["Differentiable", "*Continuous", "Polynomial", "Increasing"],
         "Continuity on the closed interval is the key requirement."),
        ("f(x) = x³ − 2. f(1) = −1 and f(2) = 6. A zero exists between:", ["0 and 1", "*1 and 2", "2 and 3", "−1 and 0"],
         "Sign change from negative to positive on [1, 2]."),
        ("Does IVT give the exact zero?", ["Yes", "*No, only existence", "Only for polynomials", "Only for linear functions"],
         "IVT guarantees existence but not the exact value."),
        ("f(x) = x² − 5. f(2) = −1, f(3) = 4. A root is between:", ["0 and 2", "*2 and 3", "3 and 4", "−2 and 2"],
         "Sign change: f(2) < 0, f(3) > 0."),
        ("Which type of function is always continuous on all reals?", ["Rational", "*Polynomial", "Piecewise", "Step function"],
         "Polynomials have no breaks, holes, or asymptotes."),
        ("f(0) = 2 and f(3) = 7. Is a zero guaranteed in (0, 3)?", ["Yes", "*Not necessarily", "Only if f is polynomial", "Only if f is linear"],
         "Both values are positive—no sign change. A zero is not guaranteed."),
        ("f(x) = x⁵ − x − 1. f(1) = −1, f(2) = 29. Conclusion?", ["No zero exists", "*At least one zero in (1, 2)", "Zero at x = 1.5", "Two zeros in (1, 2)"],
         "Sign change: f(1) < 0, f(2) > 0."),
        ("IVT can be used to show that f(c) = N for any N between f(a) and f(b), not just N = 0.", ["*True", "False"],
         "IVT applies to any intermediate value N, not just zero."),
        ("f(x) = x² has f(−1) = 1 and f(1) = 1. Does IVT guarantee a zero in (−1, 1)?", ["Yes", "*No sign change, so no guarantee", "Only at x = 0", "IVT doesn't apply"],
         "Both positive → no sign change → IVT doesn't guarantee a zero (though x = 0 is a zero, IVT can't detect it here)."),
        ("To use the bisection method, first you need:", ["The exact root", "A graph", "*An interval with a sign change", "The derivative"],
         "Bisection starts with an interval where f changes sign."),
        ("f(x) = x³ + x + 1. f(−1) = −1, f(0) = 1. Using bisection, check f(−0.5):", ["Need more info", "*f(−0.5) = 0.375 > 0, so zero is in (−1, −0.5)", "f(−0.5) < 0", "Zero is at −0.5"],
         "(−0.5)³ + (−0.5) + 1 = −0.125 − 0.5 + 1 = 0.375 > 0. Zero in (−1, −0.5)."),
        ("Can IVT guarantee how many zeros are in an interval?", ["*No, only at least one", "Yes, exactly one", "Yes, if polynomial", "No, it can't guarantee any"],
         "IVT only guarantees at least one—there could be more."),
        ("f(x) = sin(x) is continuous. f(3) ≈ 0.14, f(4) ≈ −0.76. Conclusion?", ["*At least one zero in (3, 4)", "No conclusion", "Zero at π", "Two zeros"],
         "Sign change on a continuous function → IVT applies."),
        ("Which statement is FALSE about IVT?", ["It requires continuity", "It guarantees existence of a value", "*It finds the exact root", "It applies to polynomials"],
         "IVT does not find the exact root."),
        ("f(x) = 1/(x − 2). f(1) = −1, f(3) = 1. Is a zero guaranteed in (1, 3)?", ["Yes, by IVT", "*No, f is not continuous on [1, 3]", "Yes, at x = 2", "Cannot determine"],
         "f has a discontinuity at x = 2, so IVT doesn't apply."),
        ("A polynomial of odd degree always has at least one real zero because of:", ["Factor Theorem", "*IVT (and end behavior)", "Quadratic formula", "Synthetic division"],
         "Odd degree → opposite end behaviors → sign change → IVT guarantees a zero."),
        ("f(x) = x⁴ + 2. Does it have a real zero?", ["Yes", "*No", "Maybe", "Only complex zeros"],
         "x⁴ ≥ 0 always, so x⁴ + 2 ≥ 2 > 0. No real zeros."),
        ("IVT is about __ not __.", ["Derivatives, values", "*Existence, location", "Limits, continuity", "Graphs, equations"],
         "IVT tells us a zero exists, not where it is exactly."),
        ("If f(a) < 0 < f(b) and f is continuous, there is a c in (a, b) with f(c) =", ["f(a)", "f(b)", "*0", "1"],
         "0 is between f(a) < 0 and f(b) > 0, so IVT gives f(c) = 0.")
    ]
)
lessons[k] = v

# ── 3.6 Graphing Polynomial Functions ──────────────────────────────
k, v = build_lesson(3, 6,
    "Graphing Polynomial Functions",
    "<h3>Graphing Polynomial Functions</h3>"
    "<p>To sketch the graph of a polynomial, combine what you know about zeros, multiplicity, end behavior, and turning points.</p>"
    "<h4>Step-by-Step Graphing</h4>"
    "<ol>"
    "<li><b>Find the y-intercept:</b> evaluate f(0).</li>"
    "<li><b>Find the zeros:</b> factor and solve f(x) = 0. Note multiplicity.</li>"
    "<li><b>Determine end behavior:</b> use degree and leading coefficient.</li>"
    "<li><b>Plot key points:</b> vertex (for quadratics), turning points, intercepts.</li>"
    "<li><b>Sketch:</b> connect points smoothly, respecting multiplicity behavior (cross or bounce).</li>"
    "</ol>"
    "<h4>Using Technology</h4>"
    "<ul>"
    "<li>Graphing calculators or software can verify your sketch.</li>"
    "<li>Use the table feature to find approximate turning-point coordinates.</li>"
    "</ul>",
    [
        ("Graphing Strategy", "Find intercepts, determine end behavior, note multiplicity at zeros, plot key points, sketch smoothly."),
        ("y-intercept", "The point (0, f(0)); found by evaluating the polynomial at x = 0."),
        ("x-intercepts", "Points where f(x) = 0; found by factoring or using the quadratic formula."),
        ("Turning Points", "Local maxima or minima where the graph changes direction; at most n − 1 for degree n."),
        ("Smooth Curve", "Polynomial graphs are continuous with no sharp corners, cusps, or breaks.")
    ],
    [
        ("f(x) = (x − 1)(x + 3). y-intercept?", ["1", "*−3", "3", "−1"],
         "f(0) = (−1)(3) = −3."),
        ("f(x) = x(x − 2)(x + 1). Zeros?", ["0, −2, 1", "*0, 2, −1", "0, 2, 1", "−2, 1"],
         "Set each factor = 0: x = 0, 2, −1."),
        ("f(x) = −x³ + 3x. End behavior?", ["Both rise", "Both fall", "Falls left, rises right", "*Rises left, falls right"],
         "Odd degree, negative lead → rises left, falls right."),
        ("f(x) = (x − 2)²(x + 1). At x = 2, the graph:", ["Crosses", "*Bounces", "Has a hole", "Is undefined"],
         "Even multiplicity 2 → bounces."),
        ("f(x) = (x − 2)²(x + 1). At x = −1, the graph:", ["Bounces", "*Crosses", "Flattens", "Is tangent"],
         "Odd multiplicity 1 → crosses."),
        ("How many turning points does f(x) = x³ − 3x have?", ["0", "1", "*2", "3"],
         "Degree 3 → at most 2. f'(x) = 3x² − 3 = 0 → x = ±1 → 2 turning points."),
        ("f(x) = x⁴ − 4x². y-intercept?", ["4", "−4", "*0", "1"],
         "f(0) = 0."),
        ("f(x) = x⁴ − 4x². Find the zeros.", ["0, 4", "*0, 2, −2", "0, ±4", "±1, ±2"],
         "x²(x² − 4) = x²(x−2)(x+2) → x = 0, 2, −2."),
        ("What is the multiplicity of x = 0 in x⁴ − 4x²?", ["1", "*2", "3", "4"],
         "x²(x−2)(x+2): x = 0 has multiplicity 2."),
        ("At x = 0, the graph of x⁴ − 4x²:", ["Crosses", "*Bounces", "Has a cusp", "Is linear"],
         "Multiplicity 2 → bounces at x = 0."),
        ("f(x) = −2(x + 1)(x − 3). Opens:", ["*Downward", "Upward", "Left", "Right"],
         "Leading coefficient −2 < 0, degree 2 → opens downward."),
        ("Sketching f(x) = (x + 2)(x − 1)(x − 4): how many x-intercepts?", ["2", "*3", "4", "1"],
         "Three distinct linear factors → 3 x-intercepts."),
        ("Between consecutive zeros, a polynomial graph stays:", ["At zero", "*Entirely above or below the x-axis", "Linear", "Constant"],
         "It cannot cross the x-axis between zeros (no additional zeros)."),
        ("f(x) = x³ has a zero at x = 0 with multiplicity:", ["1", "2", "*3", "0"],
         "x³ = (x − 0)³ → multiplicity 3."),
        ("At x = 0, the graph of x³:", ["Bounces", "*Crosses with flattening", "Is linear", "Has a cusp"],
         "Odd multiplicity 3 → crosses, but with a flattened S-shape."),
        ("f(x) = (x − 1)²(x − 3)². Degree?", ["2", "3", "*4", "6"],
         "2 + 2 = 4."),
        ("f(x) = (x − 1)²(x − 3)². How many times does the graph cross the x-axis?", ["2", "1", "*0", "4"],
         "Both zeros have even multiplicity → bounces at both, never crosses."),
        ("When graphing, the first step is usually to find:", ["Turning points", "*y-intercept and zeros", "The derivative", "Asymptotes"],
         "Start with intercepts as anchor points for the sketch."),
        ("A degree-4 polynomial with 3 turning points has shape like:", ["A line", "A parabola", "An S-curve", "*A W or M shape"],
         "Degree 4 with 3 turning points creates a W or M shape."),
        ("Can a polynomial graph have a sharp corner?", ["Yes", "*No", "Only cubics", "Only at zeros"],
         "Polynomials are smooth (infinitely differentiable), so no sharp corners.")
    ]
)
lessons[k] = v

# ── 3.7 Rational Root Theorem ──────────────────────────────────────
k, v = build_lesson(3, 7,
    "Rational Root Theorem",
    "<h3>Rational Root Theorem</h3>"
    "<p>The <b>Rational Root Theorem</b> helps find <b>possible rational zeros</b> of a polynomial with integer coefficients.</p>"
    "<h4>Statement</h4>"
    "<ul>"
    "<li>If f(x) = aₙxⁿ + … + a₀ has integer coefficients, then any rational zero p/q (in lowest terms) satisfies:</li>"
    "<li><b>p divides a₀</b> (the constant term) and <b>q divides aₙ</b> (the leading coefficient).</li>"
    "</ul>"
    "<h4>Using the Theorem</h4>"
    "<ol>"
    "<li>List all factors of the constant term (±).</li>"
    "<li>List all factors of the leading coefficient (±).</li>"
    "<li>Form all possible fractions p/q.</li>"
    "<li>Test each candidate using direct substitution or synthetic division.</li>"
    "<li>Once a zero is found, factor it out and repeat with the reduced polynomial.</li>"
    "</ol>"
    "<h4>Limitations</h4>"
    "<ul>"
    "<li>Only identifies <b>possible rational</b> zeros; irrational and complex zeros are not found this way.</li>"
    "<li>Not all candidates will be actual zeros—you must test them.</li>"
    "</ul>",
    [
        ("Rational Root Theorem", "Possible rational zeros p/q: p divides the constant term, q divides the leading coefficient."),
        ("Constant Term (a₀)", "The term with no x; its factors provide the numerators of possible rational zeros."),
        ("Leading Coefficient (aₙ)", "The coefficient of the highest-degree term; its factors provide the denominators."),
        ("Testing Candidates", "Use substitution or synthetic division to check if a candidate p/q is actually a zero."),
        ("Reducing the Polynomial", "After finding one zero, divide it out and apply the theorem to the quotient.")
    ],
    [
        ("For f(x) = x³ − 3x + 2, possible rational zeros are:", ["±1, ±3", "*±1, ±2", "±2, ±3", "±1, ±6"],
         "a₀ = 2 (factors ±1, ±2), aₙ = 1 (factor ±1). p/q: ±1, ±2."),
        ("For f(x) = 2x³ + 3x − 6, the denominators q divide:", ["−6", "3", "*2", "1"],
         "q divides the leading coefficient 2."),
        ("Possible rational zeros of 3x² − 5x + 2:", ["Only integers", "*±1, ±2, ±1/3, ±2/3", "±1, ±2, ±3", "±5, ±2"],
         "p: ±1, ±2 (from a₀=2). q: ±1, ±3 (from aₙ=3). p/q: ±1, ±2, ±1/3, ±2/3."),
        ("Test x = 1 in f(x) = x³ − 3x + 2.", ["f(1) = 1", "*f(1) = 0", "f(1) = −2", "f(1) = 2"],
         "1 − 3 + 2 = 0. So x = 1 is a zero."),
        ("After finding x = 1 is a zero of x³ − 3x + 2, the quotient is:", ["x² + x + 2", "x² − x + 2", "*x² + x − 2", "x² − x − 2"],
         "Synthetic division: x³ − 3x + 2 ÷ (x − 1) = x² + x − 2."),
        ("Factor x² + x − 2.", ["(x + 2)(x + 1)", "(x − 2)(x − 1)", "*(x + 2)(x − 1)", "(x − 2)(x + 1)"],
         "Factors to (x + 2)(x − 1)."),
        ("All zeros of x³ − 3x + 2:", ["1, −2", "1, 2", "*1 (double), −2", "−1, 2"],
         "(x − 1)²(x + 2): zeros are x = 1 (mult 2) and x = −2."),
        ("For 2x⁴ − x + 6, possible numerators p come from:", ["2", "−1", "*6", "4"],
         "p divides the constant term 6."),
        ("How many possible rational zeros does x⁵ − 1 have?", ["5", "1", "*2", "10"],
         "p: ±1 (from a₀ = −1). q: ±1 (from aₙ = 1). Candidates: ±1."),
        ("Test x = −1 in x⁵ − 1.", ["0", "*−2", "2", "1"],
         "(−1)⁵ − 1 = −1 − 1 = −2 ≠ 0. Not a zero."),
        ("The Rational Root Theorem does NOT find:", ["Rational zeros", "Integer zeros", "*Irrational zeros", "The constant term"],
         "It only identifies possible rational zeros, not irrational ones like √2."),
        ("For f(x) = x³ + 2x² − x − 2, test x = 1:", ["f(1) = 2", "*f(1) = 0", "f(1) = −1", "f(1) = 1"],
         "1 + 2 − 1 − 2 = 0. x = 1 is a zero."),
        ("Factor x³ + 2x² − x − 2 completely.", ["(x−1)(x²+3x+2)", "*(x−1)(x+1)(x+2)", "(x−1)(x−1)(x+2)", "(x+1)(x−2)(x+1)"],
         "(x−1)(x²+3x+2) = (x−1)(x+1)(x+2)."),
        ("For 6x³ + x − 1, possible values of q:", ["±1", "±1, ±6", "*±1, ±2, ±3, ±6", "±6"],
         "q divides 6: ±1, ±2, ±3, ±6."),
        ("If no rational candidate works, the polynomial has:", ["*No rational zeros", "No zeros at all", "Only imaginary zeros", "A mistake"],
         "It may have irrational or complex zeros, but no rational ones."),
        ("f(x) = 4x² − 9. Rational zeros?", ["±3", "±9/4", "*±3/2", "±4/9"],
         "4x² − 9 = (2x−3)(2x+3) → x = ±3/2."),
        ("Are the rational root candidates always actual roots?", ["Yes", "*No, they must be tested", "Only for cubics", "Only for degree 2"],
         "They are only candidates; substitute to verify."),
        ("f(x) = x³ − 7x + 6. f(1) = 0. Factor:", ["(x−1)(x²−x−6)", "*(x−1)(x²+x−6)", "(x−1)(x²+7x−6)", "(x+1)(x²−x+6)"],
         "Synthetic: x³ − 7x + 6 ÷ (x−1) = x² + x − 6."),
        ("x² + x − 6 factors as:", ["(x+3)(x+2)", "(x−3)(x−2)", "*(x+3)(x−2)", "(x−3)(x+2)"],
         "(x+3)(x−2) = x² + x − 6."),
        ("All rational zeros of x³ − 7x + 6:", ["*1, 2, −3", "1, −2, 3", "−1, 2, −3", "1, 7, 6"],
         "Zeros: x = 1, x = 2, x = −3.")
    ]
)
lessons[k] = v

# ── 3.8 Applications of Polynomial Models ─────────────────────────
k, v = build_lesson(3, 8,
    "Applications of Polynomial Models",
    "<h3>Applications of Polynomial Models</h3>"
    "<p>Polynomials model many real-world phenomena: volumes, areas, projectile paths, revenue/cost functions, and data fitting.</p>"
    "<h4>Common Applications</h4>"
    "<ul>"
    "<li><b>Volume problems:</b> Building an open-top box by cutting squares from a sheet → cubic model.</li>"
    "<li><b>Revenue/Profit:</b> R(x) or P(x) often modeled by quadratic or higher-degree polynomials.</li>"
    "<li><b>Curve fitting:</b> Using data points to determine a polynomial model (regression).</li>"
    "</ul>"
    "<h4>Setting Up a Model</h4>"
    "<ol>"
    "<li>Define the variable and its realistic domain.</li>"
    "<li>Write the polynomial expression relating the quantities.</li>"
    "<li>Find the desired quantity: maximum, minimum, zero, or specific value.</li>"
    "</ol>"
    "<h4>Interpreting Results</h4>"
    "<ul>"
    "<li>Always check that answers fall within the <b>practical domain</b> (e.g., lengths must be positive).</li>"
    "<li>Zeros represent break-even points; the vertex (for quadratics) gives max/min; critical points (for higher degrees) need calculus or technology to find.</li>"
    "</ul>",
    [
        ("Open-Box Problem", "Cutting equal squares from corners of a flat sheet and folding up to form a box; volume is a polynomial in the cut size."),
        ("Practical Domain", "The set of x-values that make physical sense in a real-world model (e.g., positive lengths)."),
        ("Revenue Function", "R(x) = price × quantity; often modeled as a polynomial when price depends on quantity."),
        ("Polynomial Regression", "Fitting a polynomial to data points to model trends; degree chosen to balance accuracy and simplicity."),
        ("Optimization with Polynomials", "Finding the maximum or minimum value of a polynomial model, using the vertex, critical points, or technology.")
    ],
    [
        ("A 20×16 sheet has squares of side x cut from each corner. Volume V(x) =", ["*x(20−2x)(16−2x)", "x(20−x)(16−x)", "20·16·x", "(20−2x)(16−2x)"],
         "Length = 20−2x, width = 16−2x, height = x."),
        ("For the box above, the domain of x is:", ["0 < x < 20", "0 < x < 16", "*0 < x < 8", "0 < x < 10"],
         "16−2x > 0 → x < 8. Also x > 0."),
        ("What degree polynomial is V(x) = x(20−2x)(16−2x)?", ["2", "*3", "4", "1"],
         "Product of three linear factors → degree 3."),
        ("A demand function is D(p) = 100 − 2p. Revenue R(p) = p·D(p) =", ["100p − 2", "*100p − 2p²", "100 − 2p²", "p² − 100p"],
         "R = p(100 − 2p) = 100p − 2p²."),
        ("The revenue above is maximized at p =", ["100", "50", "*25", "10"],
         "p = −100/(2·(−2)) = 25."),
        ("Maximum revenue from R(p) = 100p − 2p²:", ["$2500", "$625", "*$1250", "$1000"],
         "R(25) = 100(25) − 2(625) = 2500 − 1250 = 1250."),
        ("A ball follows h(t) = −4.9t² + 20t + 1.5. What is the initial height?", ["0 m", "20 m", "*1.5 m", "4.9 m"],
         "h(0) = 1.5 m."),
        ("For the ball above, when does it reach max height?", ["*t ≈ 2.04 s", "t = 4.08 s", "t = 1 s", "t = 20 s"],
         "t = −20/(2·(−4.9)) ≈ 2.04 s."),
        ("If a polynomial model gives a negative length, you should:", ["*Discard that solution (outside practical domain)", "Use absolute value", "Change the model", "Accept it"],
         "Negative lengths are not physically meaningful."),
        ("Fitting a polynomial to 5 data points exactly requires at most degree:", ["3", "*4", "5", "6"],
         "n points → at most degree n−1 = 4."),
        ("A company's cost C(x) = 0.01x³ − 0.6x² + 15x + 200. What does 200 represent?", ["Variable cost", "*Fixed cost", "Revenue", "Profit"],
         "C(0) = 200 is the cost when producing 0 units → fixed cost."),
        ("The box V(x) = x(20−2x)(16−2x) is zero when x =", ["*0, 8, or 10", "0, 10, 16", "0, 8, 16", "0 only"],
         "x = 0, 20−2x = 0 → x = 10, 16−2x = 0 → x = 8. Within domain: x = 0 or 8 (boundaries)."),
        ("Polynomial regression gives a better fit as degree increases, but may:", ["Always improve predictions", "*Overfit the data", "Simplify the model", "Reduce all errors"],
         "Higher degree can overfit, capturing noise rather than the trend."),
        ("A population model P(t) = −t³ + 12t² + 100t + 500 for 0 ≤ t ≤ 10. At t = 0, P =", ["100", "*500", "612", "0"],
         "P(0) = 500."),
        ("To find when the population reaches 1000, solve:", ["P(t) = 0", "P'(t) = 0", "*P(t) = 1000", "P(t) = 500"],
         "Set P(t) = 1000 and solve for t."),
        ("A rectangular field with 3 sides fenced (one side is a wall): perimeter P = 2w + l = 100. Area A(w) =", ["100w − w²", "*100w − 2w²", "w(100 − w)", "50w − w²"],
         "l = 100 − 2w. A = w·l = w(100 − 2w) = 100w − 2w²."),
        ("Max area of the field above:", ["2500 m²", "*1250 m²", "5000 m²", "625 m²"],
         "w = −100/(−4) = 25. A(25) = 100(25) − 2(625) = 1250 m²."),
        ("A quartic model can have at most how many real zeros?", ["3", "*4", "5", "2"],
         "A degree-4 polynomial has at most 4 real zeros."),
        ("When interpreting a polynomial model, always verify the answer is:", ["The largest value", "An integer", "*Within the practical domain", "A perfect square"],
         "Solutions must be physically meaningful."),
        ("The leading term of V(x) = x(20−2x)(16−2x) is:", ["x³", "20x", "*4x³", "−4x³"],
         "Expand leading terms: x · (−2x) · (−2x) = 4x³.")
    ]
)
lessons[k] = v

# ── 3.9 Case Studies in Economics & Physics ────────────────────────
k, v = build_lesson(3, 9,
    "Case Studies in Economics & Physics",
    "<h3>Case Studies in Economics &amp; Physics</h3>"
    "<p>Polynomials appear naturally in both economics and physics. This lesson explores real-world examples that connect polynomial theory to practice.</p>"
    "<h4>Economics Applications</h4>"
    "<ul>"
    "<li><b>Cost functions:</b> C(x) = aₙxⁿ + … + a₁x + a₀ models total cost of producing x units.</li>"
    "<li><b>Demand &amp; Revenue:</b> When price depends linearly on quantity, revenue is quadratic. Higher-order demand models yield cubic or quartic revenue.</li>"
    "<li><b>Marginal cost/revenue:</b> The derivative of cost or revenue, foreshadowing calculus.</li>"
    "</ul>"
    "<h4>Physics Applications</h4>"
    "<ul>"
    "<li><b>Kinematics:</b> Position as a polynomial in time: s(t) = s₀ + v₀t + ½at² (quadratic for constant acceleration).</li>"
    "<li><b>Work &amp; Energy:</b> Work done by a variable force can involve polynomial integration.</li>"
    "<li><b>Optics:</b> Polynomial approximations (e.g., Snell's law corrections) appear in lens design.</li>"
    "</ul>"
    "<h4>Strategy</h4>"
    "<ul>"
    "<li>Identify the polynomial model, determine the domain, and use zeros, vertices, or technology to answer the question.</li>"
    "</ul>",
    [
        ("Cost Function", "C(x) = fixed cost + variable cost terms; a polynomial in units produced x."),
        ("Marginal Cost", "The additional cost to produce one more unit; approximated by the derivative of the cost function."),
        ("Kinematic Equation", "s(t) = s₀ + v₀t + ½at²; a degree-2 polynomial when acceleration is constant."),
        ("Break-Even Analysis", "Finding the point(s) where revenue equals cost: R(x) = C(x)."),
        ("Average Cost", "C̄(x) = C(x)/x; the cost per unit, which decreases then increases (economies of scale).")
    ],
    [
        ("A firm's cost is C(x) = 0.5x² + 10x + 100. Fixed cost?", ["0.5", "10", "*100", "110.5"],
         "C(0) = 100."),
        ("Variable cost for 10 units [C(10) − C(0)]:", ["*200", "100", "150", "250"],
         "C(10) = 0.5(100) + 100 + 100 = 250. Variable = 250 − 100 = 150. Wait: 0.5(100)+10(10) = 50 + 100 = 150. So 150."),
        ("Revenue R(x) = 50x − 0.5x². Profit P(x) = R(x) − C(x) = ?", ["50x − x² − 10x − 100", "*−x² + 40x − 100", "−x² + 60x − 100", "40x − 100"],
         "P = (50x − 0.5x²) − (0.5x² + 10x + 100) = −x² + 40x − 100."),
        ("Maximum profit above occurs at x =", ["40", "*20", "10", "100"],
         "x = −40/(2·(−1)) = 20."),
        ("Maximum profit value:", ["$400", "$300", "*$300", "$200"],
         "P(20) = −400 + 800 − 100 = 300."),
        ("Break-even: P(x) = 0 → −x² + 40x − 100 = 0. Solutions:", ["*x ≈ 2.68 and x ≈ 37.32", "x = 10, 30", "x = 20", "x = 0, 40"],
         "x = (40 ± √(1600−400))/2 = (40 ± √1200)/2 ≈ 2.68, 37.32."),
        ("A car's position: s(t) = 4t² + 2t (meters). Distance at t = 3?", ["12", "18", "*42", "36"],
         "s(3) = 4(9) + 2(3) = 36 + 6 = 42 m."),
        ("Velocity from s(t) = 4t² + 2t is v(t) = s'(t) =", ["4t + 2", "*8t + 2", "8t² + 2", "2t + 4"],
         "Derivative: 8t + 2."),
        ("At t = 0, the initial velocity is:", ["0 m/s", "8 m/s", "*2 m/s", "4 m/s"],
         "v(0) = 8(0) + 2 = 2 m/s."),
        ("Average cost C̄(x) = C(x)/x = (0.5x² + 10x + 100)/x =", ["0.5x² + 10 + 100/x", "*0.5x + 10 + 100/x", "0.5x + 10x", "50/x + 10"],
         "Divide each term by x."),
        ("As x → ∞, C̄(x) ≈", ["100/x", "10", "*0.5x + 10 (grows)", "0"],
         "The 100/x vanishes; the dominant terms give 0.5x + 10."),
        ("A projectile: h(t) = −16t² + 80t. Max height?", ["80 ft", "*100 ft", "160 ft", "64 ft"],
         "t = 80/32 = 2.5 s. h(2.5) = −16(6.25) + 200 = −100 + 200 = 100 ft."),
        ("A demand model: D(x) = 200 − 0.1x². At x = 10:", ["100", "190", "*190", "200"],
         "D(10) = 200 − 0.1(100) = 200 − 10 = 190."),
        ("Revenue R = x·D(x) = 200x − 0.1x³. This is a __ degree polynomial.", ["2", "*3", "4", "1"],
         "Highest power is x³ → degree 3."),
        ("For R = 200x − 0.1x³, R'(x) = 200 − 0.3x². Set to 0: x ≈", ["10", "*25.8", "100", "200"],
         "0.3x² = 200 → x² = 666.7 → x ≈ 25.8."),
        ("Marginal cost from C(x) = 0.5x² + 10x + 100 is C'(x) =", ["0.5x + 100", "*x + 10", "0.5x² + 10", "10"],
         "C'(x) = x + 10."),
        ("At x = 30, marginal cost =", ["30", "*40", "50", "10"],
         "C'(30) = 30 + 10 = 40."),
        ("In physics, polynomial models are exact for:", ["All motion", "*Constant acceleration", "Circular motion", "Wave motion"],
         "s(t) = s₀ + v₀t + ½at² is exact when acceleration is constant."),
        ("A spring force F(x) = −kx. Work W = ∫F dx from 0 to d gives:", ["−kd", "kd", "*−kd²/2 (or kd²/2 stored energy)", "kd²"],
         "W = ½kd² (stored elastic potential energy)."),
        ("A polynomial model for stock price over 4 quarters requires at most degree:", ["1", "2", "*3", "4"],
         "4 data points → at most degree 3 for exact fit.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 3)")
