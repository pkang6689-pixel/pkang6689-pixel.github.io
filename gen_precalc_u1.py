#!/usr/bin/env python3
"""Generate real content for Precalculus Unit 1: Functions & Foundations (10 lessons)."""
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

# ── 1.1 Review of Algebra ──
k, v = build_lesson(1, 1, "Review of Algebra (factoring, radicals, rational expressions)",
    "<h3>Review of Algebra</h3>"
    "<p>A solid algebra foundation is essential for Precalculus.</p>"
    "<h4>Factoring</h4>"
    "<ul><li><b>GCF:</b> Always factor out the greatest common factor first.</li>"
    "<li><b>Difference of squares:</b> a² − b² = (a + b)(a − b).</li>"
    "<li><b>Perfect square trinomials:</b> a² ± 2ab + b² = (a ± b)².</li>"
    "<li><b>Trinomial factoring:</b> ax² + bx + c — find factors of ac that add to b.</li>"
    "<li><b>Grouping:</b> For four-term polynomials, group pairs and factor each group.</li></ul>"
    "<h4>Radicals</h4>"
    "<ul><li>√(ab) = √a · √b; √(a/b) = √a/√b.</li>"
    "<li>Rationalizing: Multiply by the conjugate to eliminate radicals from denominators.</li></ul>"
    "<h4>Rational Expressions</h4>"
    "<ul><li>Factor numerator and denominator, cancel common factors.</li>"
    "<li>Add/subtract: Find LCD, rewrite fractions, combine.</li>"
    "<li>Multiply/divide: Factor, cancel, and simplify.</li></ul>",
    [
        ("Greatest Common Factor (GCF)", "The largest factor shared by all terms; always factor it out first."),
        ("Difference of Squares", "a² − b² = (a + b)(a − b)."),
        ("Rationalizing the Denominator", "Multiplying numerator and denominator by the conjugate to eliminate radicals from the denominator."),
        ("Rational Expression", "A fraction where the numerator and/or denominator are polynomials."),
        ("Least Common Denominator (LCD)", "The smallest expression divisible by all denominators; used to add or subtract rational expressions."),
    ],
    [
        ("Factor: x² − 9 =", ["(x − 3)²", "(x + 9)(x − 1)", "*(x + 3)(x − 3)", "(x − 9)(x + 1)"],
         "Difference of squares: x² − 9 = x² − 3² = (x+3)(x−3)."),
        ("Factor: 2x² + 6x =", ["2x(x + 6)", "*2x(x + 3)", "x(2x + 6)", "2(x² + 3x)"],
         "GCF = 2x; 2x² + 6x = 2x(x + 3)."),
        ("Factor: x² + 5x + 6 =", ["(x + 1)(x + 6)", "*(x + 2)(x + 3)", "(x + 5)(x + 1)", "(x − 2)(x − 3)"],
         "Find factors of 6 that add to 5: 2 and 3."),
        ("Simplify: √50 =", ["5√10", "25√2", "*5√2", "√50"],
         "√50 = √(25·2) = 5√2."),
        ("Rationalize: 1/√3 =", ["1/3", "*√3/3", "3/√3", "√3"],
         "Multiply by √3/√3: 1/√3 = √3/3."),
        ("Simplify: (x² − 4)/(x + 2) =", ["x + 2", "x − 4", "*x − 2", "(x−4)/(x+2)"],
         "Factor: (x+2)(x−2)/(x+2) = x − 2 (x ≠ −2)."),
        ("Factor: x² − 2x + 1 =", ["(x + 1)²", "*(x − 1)²", "(x − 1)(x + 1)", "x(x − 2) + 1"],
         "Perfect square trinomial: x² − 2x + 1 = (x − 1)²."),
        ("The LCD of 1/(x+1) and 1/(x−1) is:", ["x² + 1", "x", "*(x+1)(x−1)", "x + 1"],
         "LCD is the product of the distinct denominators."),
        ("Simplify: (3/x) + (2/x) =", ["6/x²", "5/x²", "*5/x", "6/x"],
         "Same denominator: 3/x + 2/x = 5/x."),
        ("Factor: 6x² + 11x + 3 =", ["*(2x + 3)(3x + 1)", "(6x + 1)(x + 3)", "(3x + 3)(2x + 1)", "(2x + 1)(3x + 3)"],
         "6·3 = 18; factors of 18 that add to 11: 9 and 2. Split and group."),
        ("√a · √b equals:", ["√(a − b)", "√(a + b)", "*√(ab)", "a√b"],
         "The product rule for radicals: √a · √b = √(ab)."),
        ("Factor: x³ + 8 =", ["(x + 2)³", "*(x + 2)(x² − 2x + 4)", "(x − 2)(x² + 2x + 4)", "(x + 8)(x² − 1)"],
         "Sum of cubes: a³ + b³ = (a + b)(a² − ab + b²); 8 = 2³."),
        ("Factor by grouping: x³ + 2x² + 3x + 6 =", ["(x² + 2)(x + 3)", "*(x² + 3)(x + 2)", "(x + 6)(x² + 1)", "x(x² + 2x + 3) + 6"],
         "Group: x²(x+2) + 3(x+2) = (x²+3)(x+2)."),
        ("Simplify: (x²−1)/(x²+x) =", ["x − 1", "*(x−1)/x", "(x+1)/x", "1/(x+1)"],
         "(x+1)(x−1) / [x(x+1)] = (x−1)/x."),
        ("Divide: (2/x) ÷ (4/x²) =", ["8/x³", "1/2", "*x/2", "2x"],
         "Invert and multiply: (2/x) · (x²/4) = 2x²/(4x) = x/2."),
        ("The conjugate of (3 + √5) is:", ["3 − 5", "−3 + √5", "*(3 − √5)", "3 + √5"],
         "The conjugate changes the sign of the radical term."),
        ("√(a/b) equals:", ["a/√b", "√a + √b", "*√a / √b", "a/b"],
         "The quotient rule for radicals."),
        ("Factor: 4x² − 25 =", ["(4x − 25)(x + 1)", "*(2x + 5)(2x − 5)", "(2x − 5)²", "(4x + 5)(x − 5)"],
         "Difference of squares: (2x)² − 5² = (2x+5)(2x−5)."),
        ("To add 1/(x+2) + 3/(x−1), the LCD is:", ["x + 2", "*(x+2)(x−1)", "x − 1", "x² + x − 2"],
         "LCD = (x+2)(x−1). Note: x² + x − 2 = (x+2)(x−1) would also be correct as expanded form."),
        ("A rational expression is undefined when:", ["The numerator is 0", "*The denominator is 0", "Both are 0", "Neither is 0"],
         "Division by zero is undefined."),
    ]
)
lessons[k] = v

# ── 1.2 Order of Operations & Exponents ──
k, v = build_lesson(1, 2, "Order of Operations & Exponents",
    "<h3>Order of Operations & Exponents</h3>"
    "<p><b>PEMDAS:</b> Parentheses → Exponents → Multiplication/Division (left→right) → Addition/Subtraction (left→right).</p>"
    "<h4>Exponent Rules</h4>"
    "<ul><li>a<sup>m</sup> · a<sup>n</sup> = a<sup>m+n</sup></li>"
    "<li>a<sup>m</sup>/a<sup>n</sup> = a<sup>m−n</sup></li>"
    "<li>(a<sup>m</sup>)<sup>n</sup> = a<sup>mn</sup></li>"
    "<li>a⁰ = 1 (a ≠ 0)</li>"
    "<li>a<sup>−n</sup> = 1/a<sup>n</sup></li>"
    "<li>(ab)<sup>n</sup> = a<sup>n</sup>b<sup>n</sup></li>"
    "<li>a<sup>m/n</sup> = ⁿ√(a<sup>m</sup>) = (ⁿ√a)<sup>m</sup></li></ul>"
    "<p>These rules are used constantly throughout Precalculus and Calculus.</p>",
    [
        ("PEMDAS", "Order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction."),
        ("Product Rule for Exponents", "a^m · a^n = a^(m+n); when multiplying same bases, add exponents."),
        ("Power of a Power", "(a^m)^n = a^(mn); when raising a power to a power, multiply exponents."),
        ("Negative Exponent", "a^(−n) = 1/a^n; a negative exponent means the reciprocal."),
        ("Rational Exponent", "a^(m/n) = ⁿ√(a^m); the denominator is the root, the numerator is the power."),
    ],
    [
        ("Evaluate: 2 + 3 × 4 =", ["20", "*14", "24", "9"],
         "Multiply first: 3×4 = 12, then 2+12 = 14."),
        ("Simplify: x³ · x⁵ =", ["x¹⁵", "*x⁸", "x²", "2x⁸"],
         "Product rule: add exponents: 3+5 = 8."),
        ("Simplify: x⁷/x³ =", ["x²¹", "x³", "*x⁴", "x/3"],
         "Quotient rule: 7−3 = 4."),
        ("Simplify: (x²)⁴ =", ["x⁶", "*x⁸", "4x²", "x²⁴"],
         "Power of a power: 2×4 = 8."),
        ("Evaluate: 5⁰ =", ["0", "5", "*1", "Undefined"],
         "Any nonzero number to the zero power equals 1."),
        ("Simplify: x⁻³ =", ["−x³", "x³", "*1/x³", "−3x"],
         "Negative exponent: x⁻³ = 1/x³."),
        ("Simplify: (2x)³ =", ["2x³", "6x³", "*8x³", "2x⁹"],
         "(2x)³ = 2³ · x³ = 8x³."),
        ("Evaluate: 8^(2/3) =", ["*4", "8", "2", "16"],
         "8^(2/3) = (∛8)² = 2² = 4."),
        ("Simplify: 27^(1/3) =", ["9", "*3", "27", "1"],
         "27^(1/3) = ∛27 = 3."),
        ("Evaluate: 3 × (4 + 2)² =", ["108", "54", "*108", "36"],
         "Parentheses: 4+2=6; exponent: 6²=36; multiply: 3×36=108."),
        ("Simplify: (x⁴y²)³ =", ["x⁷y⁵", "*x¹²y⁶", "3x⁴y²", "x¹²y²"],
         "Distribute the exponent: x^(4·3)y^(2·3) = x¹²y⁶."),
        ("Simplify: x⁻² · x⁵ =", ["x⁻¹⁰", "*x³", "x⁻³", "x⁷"],
         "Add exponents: −2+5 = 3."),
        ("Evaluate: 16^(3/4) =", ["4", "12", "*8", "64"],
         "16^(3/4) = (⁴√16)³ = 2³ = 8."),
        ("Simplify: (x/y)⁻² =", ["x²/y²", "−x²/y²", "*y²/x²", "xy²"],
         "Negative exponent flips: (y/x)² = y²/x²."),
        ("Evaluate: 2³ + 2² =", ["2⁵", "32", "*12", "10"],
         "2³ = 8, 2² = 4, total = 12. Exponents don't add when bases are added."),
        ("Simplify: (3a²b)² =", ["6a⁴b²", "*9a⁴b²", "3a⁴b²", "9a²b²"],
         "3² · a^(2·2) · b² = 9a⁴b²."),
        ("Evaluate: (−2)⁴ =", ["−16", "*16", "−8", "8"],
         "Even exponent makes the result positive: (−2)⁴ = 16."),
        ("Evaluate: −2⁴ =", ["*−16", "16", "−8", "8"],
         "Exponent applies only to 2: −(2⁴) = −16."),
        ("Simplify: (x^(1/2))⁶ =", ["x^(1/12)", "x⁶", "*x³", "6√x"],
         "(x^(1/2))⁶ = x^(6/2) = x³."),
        ("0⁰ is:", ["0", "1", "*Typically considered indeterminate (though sometimes defined as 1 by convention)", "Undefined"],
         "0⁰ is an indeterminate form in most contexts."),
    ]
)
lessons[k] = v

# ── 1.3 Relations vs. Functions ──
k, v = build_lesson(1, 3, "Relations vs. Functions",
    "<h3>Relations vs. Functions</h3>"
    "<p>A <b>relation</b> is any set of ordered pairs (x, y). A <b>function</b> is a special relation where every input (x) has exactly one output (y).</p>"
    "<ul><li><b>Vertical Line Test:</b> If any vertical line crosses the graph more than once, it's NOT a function.</li>"
    "<li><b>Mapping diagrams:</b> No input should have more than one arrow pointing to an output.</li>"
    "<li><b>Function notation:</b> f(x) means 'the output of function f for input x.'</li>"
    "<li><b>One-to-one function:</b> Each output corresponds to exactly one input. Passes the horizontal line test.</li></ul>",
    [
        ("Relation", "Any set of ordered pairs (x, y)."),
        ("Function", "A relation where every input has exactly one output."),
        ("Vertical Line Test", "If any vertical line intersects a graph more than once, the graph is not a function."),
        ("One-to-One Function", "A function where each output corresponds to exactly one input; passes the horizontal line test."),
        ("Function Notation", "f(x) represents the output of function f for input x."),
    ],
    [
        ("A function is a relation where:", ["Every output has one input", "*Every input has exactly one output", "Inputs and outputs are equal", "There are no repeated values"],
         "The defining property: each x maps to exactly one y."),
        ("The vertical line test determines if a graph represents:", ["A relation", "*A function", "A one-to-one function", "An equation"],
         "If no vertical line hits the graph more than once, it's a function."),
        ("Which is NOT a function? {(1,2), (3,4), (1,5)}", ["*It is not a function (input 1 maps to both 2 and 5)", "It is a function", "It depends on the context", "It's one-to-one"],
         "Input 1 has two different outputs, violating the function definition."),
        ("A circle's graph fails the vertical line test because:", ["It's not a relation", "*Vertical lines cross it in two points", "It has no y-values", "It passes the test"],
         "At most x-values, there are two y-values on a circle."),
        ("f(x) = 2x + 3. f(4) = ?", ["7", "14", "*11", "5"],
         "f(4) = 2(4) + 3 = 8 + 3 = 11."),
        ("One-to-one functions pass:", ["Only the vertical line test", "Neither test", "*Both the vertical and horizontal line tests", "Only the horizontal line test"],
         "One-to-one means each output has one input (horizontal) and each input has one output (vertical)."),
        ("Which is a function? y = x², x = y², y = ±√x", ["x = y²", "y = ±√x", "*y = x²", "All of them"],
         "y = x² gives one y for each x. The others give two y-values for some x."),
        ("In f(x) = x² − 1, the input is:", ["f", "x² − 1", "*x", "−1"],
         "x is the input variable in function notation."),
        ("A mapping diagram shows a function if:", ["Every output has multiple inputs", "*No input has more than one arrow to different outputs", "All arrows go to the same output", "There are equal numbers of inputs and outputs"],
         "Each input must map to exactly one output."),
        ("Every function is a relation:", ["False", "*True", "Only sometimes", "Only for linear functions"],
         "Functions are a subset of relations — every function is a relation, but not vice versa."),
        ("{(2,3), (4,5), (6,3)} is:", ["Not a function", "*A function (every input is unique, even though outputs repeat)", "One-to-one", "Not a relation"],
         "Repeated outputs are fine; only repeated inputs with different outputs fail."),
        ("f(x) = 3x − 7. f(0) = ?", ["3", "0", "*−7", "7"],
         "f(0) = 3(0) − 7 = −7."),
        ("The horizontal line test checks if a function is:", ["A relation", "Continuous", "*One-to-one", "Increasing"],
         "If no horizontal line crosses the graph more than once, the function is one-to-one."),
        ("y = |x| is:", ["Not a function", "*A function (but not one-to-one)", "One-to-one", "Not a relation"],
         "Each x gives one y, but e.g. f(2) = f(−2) = 2, so not one-to-one."),
        ("The set of all inputs of a function is the:", ["Range", "*Domain", "Codomain", "Relation"],
         "Domain = set of all valid input values."),
        ("The set of all outputs of a function is the:", ["Domain", "Codomain", "*Range", "Relation"],
         "Range = set of all actual output values."),
        ("f(x) = 1/x is a function because:", ["It's defined for all x", "*Each input x (≠ 0) gives exactly one output", "It passes the horizontal line test only", "It's a polynomial"],
         "For every x ≠ 0, there is exactly one value of 1/x."),
        ("Is y² = x a function of x?", ["Yes", "*No — for positive x, there are two y-values (±√x)", "Only for x > 0", "Only for x = 0"],
         "y² = x gives y = ±√x, which is two outputs for each positive x."),
        ("f(x) = x³ is:", ["Not a function", "A function but not one-to-one", "*A function AND one-to-one", "Not a relation"],
         "Each input gives one output, and each output comes from one input."),
        ("A constant function f(x) = 5 is:", ["Not a function", "One-to-one", "*A function (every input gives the same output 5, but not one-to-one)", "A relation only"],
         "It's a valid function (one output per input) but not one-to-one."),
    ]
)
lessons[k] = v

# ── 1.4 Domain & Range ──
k, v = build_lesson(1, 4, "Domain & Range (interval notation)",
    "<h3>Domain & Range</h3>"
    "<p>The <b>domain</b> is the set of all valid inputs (x-values); the <b>range</b> is the set of all outputs (y-values).</p>"
    "<h4>Finding the Domain</h4>"
    "<ul><li><b>Polynomials:</b> Domain = (−∞, ∞).</li>"
    "<li><b>Rational functions:</b> Exclude values where the denominator = 0.</li>"
    "<li><b>Square roots:</b> The expression under the radical must be ≥ 0.</li>"
    "<li><b>Logarithms:</b> The argument must be > 0.</li></ul>"
    "<h4>Interval Notation</h4>"
    "<ul><li>( ) = open (endpoint not included); [ ] = closed (included).</li>"
    "<li>∞ and −∞ always use parentheses.</li>"
    "<li>Union (∪) combines disjoint intervals.</li></ul>",
    [
        ("Domain", "The set of all valid input values (x-values) for a function."),
        ("Range", "The set of all output values (y-values) produced by a function."),
        ("Interval Notation", "Uses parentheses (open) and brackets (closed) to describe sets: (a, b) excludes endpoints; [a, b] includes them."),
        ("Excluded Values", "Values that make a denominator zero or a radicand negative — they are not in the domain."),
        ("Union (∪)", "Combines two or more intervals: e.g., (−∞, 2) ∪ (2, ∞)."),
    ],
    [
        ("The domain of f(x) = x² is:", ["[0, ∞)", "*(−∞, ∞)", "(0, ∞)", "[−1, 1]"],
         "Polynomials have domain all real numbers."),
        ("The domain of f(x) = 1/(x−3) is:", ["(−∞, ∞)", "*All real numbers except x = 3", "[3, ∞)", "(−∞, 3)"],
         "The denominator x−3 = 0 when x = 3."),
        ("The domain of f(x) = √(x−2) is:", ["(−∞, ∞)", "(2, ∞)", "*[2, ∞)", "[−2, ∞)"],
         "x − 2 ≥ 0 → x ≥ 2."),
        ("In interval notation, [3, 7) means:", ["3 < x < 7", "*3 ≤ x < 7", "3 ≤ x ≤ 7", "3 < x ≤ 7"],
         "[ means included, ) means excluded."),
        ("The range of f(x) = x² is:", ["(−∞, ∞)", "*[0, ∞)", "(0, ∞)", "[−∞, 0]"],
         "x² is always ≥ 0; it achieves 0 at x = 0."),
        ("The domain of f(x) = ln(x) is:", ["(−∞, ∞)", "[0, ∞)", "*(0, ∞)", "(1, ∞)"],
         "The argument of ln must be strictly positive."),
        ("∞ always uses:", ["Brackets [ ]", "*Parentheses ( )", "Either", "Neither"],
         "Infinity is not a number, so it always gets parentheses."),
        ("The domain of f(x) = √(9 − x²) is:", ["(−∞, ∞)", "(−3, 3)", "*[−3, 3]", "[0, 3]"],
         "9 − x² ≥ 0 → x² ≤ 9 → −3 ≤ x ≤ 3."),
        ("Union (∪) is used for:", ["Intersecting intervals", "*Combining disjoint intervals", "Multiplying intervals", "Subtracting intervals"],
         "∪ combines separate pieces of the domain."),
        ("Domain of f(x) = 1/(x² − 4):", ["All real numbers", "*(−∞,−2) ∪ (−2,2) ∪ (2,∞)", "(−2, 2)", "x ≠ 0"],
         "x²−4 = 0 when x = ±2, so exclude both."),
        ("The range of f(x) = |x| is:", ["(−∞, ∞)", "(0, ∞)", "*[0, ∞)", "[−1, 1]"],
         "|x| ≥ 0 for all x."),
        ("The domain of f(x) = x/(x² + 1) is:", ["x ≠ 0", "x > 0", "*(−∞, ∞)", "[1, ∞)"],
         "x² + 1 > 0 for all real x — denominator never zero."),
        ("The range of f(x) = 1/x is:", ["*(−∞, 0) ∪ (0, ∞)", "(−∞, ∞)", "(0, ∞)", "[0, ∞)"],
         "1/x can be any real number except 0."),
        ("f(x) = √x + √(4−x). The domain is:", ["[0, ∞)", "*[0, 4]", "(−∞, 4]", "[−4, 4]"],
         "Need x ≥ 0 AND 4−x ≥ 0, so 0 ≤ x ≤ 4."),
        ("The range of f(x) = 3 is:", ["{0}", "*(−∞, ∞)? No — the range is just {3}", "[0, 3]", "(−∞, ∞)"],
         "A constant function outputs only one value: {3}."),
        ("Domain of f(x) = log₂(x − 5):", ["(−∞, ∞)", "[5, ∞)", "*(5, ∞)", "(0, ∞)"],
         "x − 5 > 0 → x > 5."),
        ("(−∞, 3] ∪ [5, ∞) represents:", ["3 < x < 5", "*x ≤ 3 or x ≥ 5", "All real numbers", "x = 3 or x = 5"],
         "Union of two intervals: everything ≤ 3 and everything ≥ 5."),
        ("Domain of f(x) = √(x)/(x − 1):", ["[0, ∞)", "(0, ∞)", "*[0, 1) ∪ (1, ∞)", "[0, 1]"],
         "Need x ≥ 0 for √x and x ≠ 1 for the denominator."),
        ("The range of f(x) = −x² + 4 is:", ["[4, ∞)", "[0, ∞)", "*(−∞, 4]", "(−∞, ∞)"],
         "The parabola opens down with vertex at (0, 4), so y ≤ 4."),
        ("To find the range of a function, you can:", ["Only look at the domain", "*Analyze the function's behavior, graph it, or solve for x in terms of y", "Always say (−∞, ∞)", "Use the vertical line test"],
         "Range requires understanding what y-values the function can produce."),
    ]
)
lessons[k] = v

# ── 1.5 Function Notation & Evaluation ──
k, v = build_lesson(1, 5, "Function Notation & Evaluation",
    "<h3>Function Notation & Evaluation</h3>"
    "<p><b>Function notation</b> f(x) names the function (f) and the input variable (x).</p>"
    "<ul><li><b>Evaluating:</b> Replace x with the given value and simplify.</li>"
    "<li><b>f(a + h):</b> Substitute (a + h) for every x in the formula.</li>"
    "<li><b>Difference quotient:</b> [f(x+h) − f(x)] / h — fundamental to calculus (measures average rate of change).</li>"
    "<li><b>Piecewise evaluation:</b> Determine which piece applies based on the input value.</li>"
    "<li><b>Reading function values from graphs:</b> f(a) is the y-value where x = a on the graph.</li></ul>",
    [
        ("f(x)", "Notation for a function named f with input variable x; f(3) means evaluate f at x = 3."),
        ("Evaluating a Function", "Substituting a value for the input variable and simplifying."),
        ("Difference Quotient", "[f(x+h) − f(x)] / h; measures the average rate of change over an interval of width h."),
        ("f(a + h)", "Substitute (a + h) for x in the function's formula; used in the difference quotient."),
        ("Piecewise Evaluation", "Check which condition the input satisfies, then use the corresponding formula."),
    ],
    [
        ("f(x) = 3x − 2. f(5) = ?", ["17", "8", "*13", "5"],
         "f(5) = 3(5) − 2 = 15 − 2 = 13."),
        ("g(x) = x² + 1. g(−3) = ?", ["−8", "8", "*10", "−10"],
         "g(−3) = (−3)² + 1 = 9 + 1 = 10."),
        ("f(x) = 2x. f(a + h) = ?", ["2a + h", "*2a + 2h (= 2(a+h))", "2ah", "2a − 2h"],
         "Replace x with (a+h): f(a+h) = 2(a+h) = 2a + 2h."),
        ("For f(x) = x², the difference quotient [f(x+h)−f(x)]/h simplifies to:", ["x + h", "x² + h", "*2x + h", "h"],
         "f(x+h) = (x+h)² = x²+2xh+h²; subtract x²: 2xh+h²; divide by h: 2x+h."),
        ("h(x) = √(x+4). h(5) = ?", ["√5", "*3", "√9 = 3", "7"],
         "h(5) = √(5+4) = √9 = 3."),
        ("If f(x) = {2x if x < 0; x² if x ≥ 0}, then f(−3) = ?", ["9", "*−6", "6", "−9"],
         "Since −3 < 0, use 2x: f(−3) = 2(−3) = −6."),
        ("If f(x) = {2x if x < 0; x² if x ≥ 0}, then f(4) = ?", ["8", "*16", "4", "2"],
         "Since 4 ≥ 0, use x²: f(4) = 4² = 16."),
        ("f(x) = 5x + 1. f(2) + f(3) = ?", ["26", "*27", "28", "30"],
         "f(2) = 11, f(3) = 16, total = 27."),
        ("f(x) = x³. f(−2) = ?", ["8", "*−8", "−6", "6"],
         "f(−2) = (−2)³ = −8."),
        ("Reading a graph: if the point (3, 7) is on the graph of f, then f(3) = ?", ["3", "*7", "10", "21"],
         "f(3) is the y-coordinate when x = 3."),
        ("f(x) = |2x − 6|. f(1) = ?", ["−4", "8", "*4", "−8"],
         "f(1) = |2(1)−6| = |−4| = 4."),
        ("The difference quotient measures:", ["The slope of a horizontal line", "The y-intercept", "*The average rate of change of f over an interval of width h", "The domain"],
         "It's the slope of the secant line between (x, f(x)) and (x+h, f(x+h))."),
        ("f(x) = 1/(x+2). f(0) = ?", ["0", "2", "*1/2", "Undefined"],
         "f(0) = 1/(0+2) = 1/2."),
        ("f(x) = 4. f(100) = ?", ["100", "400", "*4", "0"],
         "A constant function returns 4 for every input."),
        ("f(x) = 2ˣ. f(3) = ?", ["6", "*8", "9", "12"],
         "f(3) = 2³ = 8."),
        ("g(x) = x² − 3x. g(a) = ?", ["*a² − 3a", "x² − 3a", "2x − 3", "a² + 3a"],
         "Replace x with a: g(a) = a² − 3a."),
        ("If f(2) = 5 and g(5) = 10, then g(f(2)) = ?", ["5", "2", "*10", "15"],
         "f(2) = 5, so g(f(2)) = g(5) = 10."),
        ("f(x) = x + 1. [f(x+h)−f(x)]/h = ?", ["x + 1", "h", "*1", "x + h"],
         "f(x+h) = x+h+1; subtract f(x) = x+1: h; divide by h: 1."),
        ("f(x) = 3x² + 2x − 1. f(0) = ?", ["3", "2", "*−1", "0"],
         "f(0) = 0 + 0 − 1 = −1."),
        ("Function notation f(x) is read as:", ["f multiplied by x", "*f of x", "f to the power x", "fx"],
         "f(x) means 'the value of function f at input x.'"),
    ]
)
lessons[k] = v

# ── 1.6 Graphing Basics ──
k, v = build_lesson(1, 6, "Graphing Basics (intercepts, symmetry)",
    "<h3>Graphing Basics</h3>"
    "<p>Understanding graphs is fundamental to Precalculus.</p>"
    "<h4>Intercepts</h4>"
    "<ul><li><b>x-intercept:</b> Where y = 0. Set f(x) = 0 and solve for x.</li>"
    "<li><b>y-intercept:</b> Where x = 0. Evaluate f(0).</li></ul>"
    "<h4>Symmetry</h4>"
    "<ul><li><b>Even function:</b> f(−x) = f(x). Symmetric about the y-axis. Example: f(x) = x².</li>"
    "<li><b>Odd function:</b> f(−x) = −f(x). Symmetric about the origin. Example: f(x) = x³.</li>"
    "<li><b>Neither:</b> Most functions are neither even nor odd.</li></ul>"
    "<h4>Increasing/Decreasing</h4>"
    "<ul><li>A function is <b>increasing</b> on an interval if f(a) < f(b) whenever a < b.</li>"
    "<li>A function is <b>decreasing</b> on an interval if f(a) > f(b) whenever a < b.</li></ul>",
    [
        ("x-intercept", "The point where the graph crosses the x-axis; found by setting y = 0."),
        ("y-intercept", "The point where the graph crosses the y-axis; found by evaluating f(0)."),
        ("Even Function", "f(−x) = f(x); the graph is symmetric about the y-axis."),
        ("Odd Function", "f(−x) = −f(x); the graph is symmetric about the origin."),
        ("Increasing Function", "f(a) < f(b) whenever a < b on an interval; the graph rises from left to right."),
    ],
    [
        ("To find the y-intercept, set:", ["y = 0", "*x = 0", "x = y", "f(x) = x"],
         "The y-intercept occurs when x = 0."),
        ("The x-intercepts of f(x) = x² − 4 are:", ["(0, −4)", "*x = 2 and x = −2", "x = 4", "x = 0"],
         "Set x²−4 = 0: x² = 4, x = ±2."),
        ("f(x) = x² is an even function because:", ["*f(−x) = (−x)² = x² = f(x)", "f(−x) = −f(x)", "It's symmetric about the origin", "It's always increasing"],
         "f(−x) = f(x) for all x — y-axis symmetry."),
        ("f(x) = x³ is odd because:", ["f(−x) = f(x)", "*f(−x) = (−x)³ = −x³ = −f(x)", "It has no symmetry", "It's even"],
         "f(−x) = −f(x) — origin symmetry."),
        ("f(x) = x² + x. Is it even, odd, or neither?", ["Even", "Odd", "*Neither", "Both"],
         "f(−x) = x² − x ≠ f(x) and ≠ −f(x)."),
        ("The y-intercept of f(x) = 3x² − 5x + 2 is:", ["(3, 0)", "(0, 5)", "*(0, 2)", "(2, 0)"],
         "f(0) = 0 − 0 + 2 = 2."),
        ("A function is increasing on an interval if:", ["It goes down left to right", "f(a) = f(b)", "*f(a) < f(b) for a < b", "f(a) > f(b) for a < b"],
         "The graph rises as x increases."),
        ("Symmetric about the y-axis implies:", ["Odd function", "*Even function", "Neither", "Constant function"],
         "Y-axis symmetry ↔ even function."),
        ("Symmetric about the origin implies:", ["Even function", "*Odd function", "Neither", "Constant function"],
         "Origin symmetry ↔ odd function."),
        ("The x-intercepts of f(x) = x(x−3)(x+1) are:", ["0, 3", "*0, 3, −1", "−3, 1", "0, −3, 1"],
         "Set each factor = 0: x = 0, x = 3, x = −1."),
        ("f(x) = |x| is:", ["Odd", "*Even", "Neither", "One-to-one"],
         "f(−x) = |−x| = |x| = f(x)."),
        ("The graph of f(x) = 1/x is symmetric about:", ["The y-axis", "*The origin", "The x-axis", "No axis"],
         "f(−x) = −1/x = −f(x), so it's odd (origin symmetry)."),
        ("f(x) = 2x + 1. y-intercept:", ["(1, 0)", "*(0, 1)", "(0, 2)", "(−1/2, 0)"],
         "f(0) = 2(0) + 1 = 1."),
        ("A constant function f(x) = c is:", ["Odd", "*Even (since f(−x) = c = f(x))", "Neither", "Increasing"],
         "f(−x) = c = f(x) for all x."),
        ("f(x) = eˣ is:", ["Even", "Odd", "*Neither", "Both"],
         "f(−x) = e⁻ˣ ≠ eˣ and ≠ −eˣ."),
        ("A function can be both even and odd only if:", ["It's any polynomial", "*f(x) = 0 for all x", "It's a constant", "It has symmetry"],
         "The only function that is both even and odd is f(x) = 0."),
        ("To test if f is even: check if f(−x) equals:", ["−f(x)", "*f(x)", "f(x²)", "0"],
         "Even: f(−x) = f(x) for all x in the domain."),
        ("f(x) = sin(x) is:", ["Even", "*Odd", "Neither", "Both"],
         "sin(−x) = −sin(x), so it's odd."),
        ("The graph is decreasing when:", ["y stays constant", "y goes up as x increases", "*y goes down as x increases", "x stays constant"],
         "Decreasing: f(a) > f(b) when a < b."),
        ("The number of x-intercepts for f(x) = x² + 1 is:", ["2", "1", "*0", "Infinitely many"],
         "x² + 1 > 0 for all real x — the parabola never crosses the x-axis."),
    ]
)
lessons[k] = v

# ── 1.7 Transformations ──
k, v = build_lesson(1, 7, "Transformations (shifts, reflections, stretches)",
    "<h3>Transformations of Functions</h3>"
    "<p>Understanding transformations lets you graph functions by modifying parent functions.</p>"
    "<h4>Translations (Shifts)</h4>"
    "<ul><li>f(x) + c: Shift UP c units.</li>"
    "<li>f(x) − c: Shift DOWN c units.</li>"
    "<li>f(x − c): Shift RIGHT c units.</li>"
    "<li>f(x + c): Shift LEFT c units.</li></ul>"
    "<h4>Reflections</h4>"
    "<ul><li>−f(x): Reflect across the x-axis.</li>"
    "<li>f(−x): Reflect across the y-axis.</li></ul>"
    "<h4>Stretches & Compressions</h4>"
    "<ul><li>a·f(x) with |a| > 1: Vertical stretch.</li>"
    "<li>a·f(x) with 0 < |a| < 1: Vertical compression.</li>"
    "<li>f(bx) with |b| > 1: Horizontal compression.</li>"
    "<li>f(bx) with 0 < |b| < 1: Horizontal stretch.</li></ul>",
    [
        ("Vertical Shift", "f(x) + c shifts up; f(x) − c shifts down."),
        ("Horizontal Shift", "f(x − c) shifts right c units; f(x + c) shifts left c units."),
        ("Reflection over x-axis", "−f(x) reflects the graph across the x-axis (flip vertically)."),
        ("Reflection over y-axis", "f(−x) reflects the graph across the y-axis (flip horizontally)."),
        ("Vertical Stretch/Compression", "a·f(x): |a| > 1 stretches vertically; 0 < |a| < 1 compresses vertically."),
    ],
    [
        ("f(x) + 3 shifts the graph:", ["Down 3", "Left 3", "*Up 3", "Right 3"],
         "Adding a constant outside shifts vertically up."),
        ("f(x − 2) shifts the graph:", ["Left 2", "Up 2", "Down 2", "*Right 2"],
         "Subtracting inside shifts right (opposite of the sign)."),
        ("f(x + 4) shifts the graph:", ["Right 4", "*Left 4", "Up 4", "Down 4"],
         "Adding inside shifts left."),
        ("−f(x) reflects across:", ["The y-axis", "*The x-axis", "The origin", "The line y = x"],
         "Negating the output reflects over the x-axis."),
        ("f(−x) reflects across:", ["The x-axis", "*The y-axis", "The origin", "The line y = x"],
         "Negating the input reflects over the y-axis."),
        ("2f(x) is a:", ["Horizontal stretch", "Vertical compression", "*Vertical stretch by a factor of 2", "Horizontal compression"],
         "|a| = 2 > 1 → vertical stretch."),
        ("(1/3)f(x) is a:", ["Vertical stretch", "*Vertical compression by a factor of 1/3", "Horizontal stretch", "Horizontal compression"],
         "|a| = 1/3 < 1 → vertical compression."),
        ("f(2x) is a:", ["Horizontal stretch", "Vertical stretch", "Vertical compression", "*Horizontal compression by a factor of 1/2"],
         "|b| = 2 > 1 → horizontal compression (squeeze toward y-axis)."),
        ("f(x/2) = f(0.5x) is a:", ["*Horizontal stretch by a factor of 2", "Horizontal compression", "Vertical stretch", "Vertical compression"],
         "|b| = 0.5 < 1 → horizontal stretch."),
        ("The parent function of y = (x−3)² + 5 is:", ["y = x + 5", "*y = x²", "y = x³", "y = |x|"],
         "It's a transformed version of y = x²."),
        ("y = (x−3)² + 5 has its vertex at:", ["(0, 0)", "(5, 3)", "*(3, 5)", "(−3, 5)"],
         "Shifted right 3 and up 5 from the origin."),
        ("y = −|x| reflects y = |x| across:", ["The y-axis", "*The x-axis", "y = x", "The origin"],
         "The negative sign in front reflects vertically."),
        ("Order of transformations (recommended): horizontal shift, then:", ["Vertical shift first, then stretch", "*Stretch/compress, then reflect, then vertical shift", "Nothing else", "Only shift"],
         "A standard order: horizontal shift → stretch/compress → reflect → vertical shift."),
        ("y = f(x) − 7 shifts the graph:", ["Up 7", "Right 7", "*Down 7", "Left 7"],
         "Subtracting outside shifts down."),
        ("y = 3f(x − 1) + 2 involves:", ["Only shifts", "Only a stretch", "*A horizontal shift right 1, vertical stretch by 3, and vertical shift up 2", "Only a reflection"],
         "Multiple transformations can be combined."),
        ("If (2, 5) is on f(x), then on f(x) + 3 it becomes:", ["(5, 5)", "(2, 2)", "*(2, 8)", "(5, 3)"],
         "y-value increases by 3: (2, 5+3) = (2, 8)."),
        ("If (2, 5) is on f(x), then on f(x − 4) it becomes:", ["(−2, 5)", "*(6, 5)", "(2, 1)", "(2, 9)"],
         "x shifts right by 4: (2+4, 5) = (6, 5)."),
        ("If (2, 5) is on f(x), then on −f(x) it becomes:", ["(−2, 5)", "(2, 5)", "*(2, −5)", "(−2, −5)"],
         "Reflect y: (2, −5)."),
        ("If (2, 5) is on f(x), then on f(−x) it becomes:", ["(2, −5)", "*(−2, 5)", "(−2, −5)", "(2, 5)"],
         "Reflect x: (−2, 5)."),
        ("y = |x + 2| − 3 has its vertex at:", ["(2, −3)", "(2, 3)", "*(−2, −3)", "(−2, 3)"],
         "Shifted left 2 and down 3 from origin."),
    ]
)
lessons[k] = v

# ── 1.8 Inverse Functions & Composition ──
k, v = build_lesson(1, 8, "Inverse Functions & Composition",
    "<h3>Inverse Functions & Composition</h3>"
    "<h4>Composition</h4>"
    "<p><b>(f ∘ g)(x) = f(g(x)):</b> Apply g first, then f to the result.</p>"
    "<ul><li>The domain of f ∘ g is restricted to x-values where g(x) is in the domain of f.</li></ul>"
    "<h4>Inverse Functions</h4>"
    "<p>f⁻¹ undoes f: f(f⁻¹(x)) = x and f⁻¹(f(x)) = x.</p>"
    "<ul><li><b>Finding f⁻¹:</b> Replace f(x) with y, swap x and y, solve for y.</li>"
    "<li><b>Existence:</b> Only one-to-one functions have inverses.</li>"
    "<li><b>Graphically:</b> The graph of f⁻¹ is the reflection of f over the line y = x.</li>"
    "<li><b>Domain of f⁻¹ = Range of f;</b> Range of f⁻¹ = Domain of f.</li></ul>",
    [
        ("Composition f(g(x))", "Apply g first, then apply f to the result; written as (f ∘ g)(x)."),
        ("Inverse Function f⁻¹", "The function that undoes f: f(f⁻¹(x)) = x and f⁻¹(f(x)) = x."),
        ("Finding an Inverse", "Swap x and y in y = f(x), then solve for y."),
        ("One-to-One Requirement", "Only one-to-one functions (passing the horizontal line test) have inverses."),
        ("Inverse Graph", "The graph of f⁻¹ is the reflection of f's graph across the line y = x."),
    ],
    [
        ("(f ∘ g)(x) means:", ["f(x) · g(x)", "g(f(x))", "*f(g(x))", "f(x) + g(x)"],
         "f ∘ g means apply g first, then f."),
        ("If f(x) = 2x and g(x) = x + 3, then f(g(x)) = ?", ["*2(x+3) = 2x+6", "2x + 3", "x + 6", "(2x)(x+3)"],
         "f(g(x)) = f(x+3) = 2(x+3) = 2x+6."),
        ("If f(x) = 2x and g(x) = x + 3, then g(f(x)) = ?", ["2x + 6", "*2x + 3", "x + 6", "2(x+3)"],
         "g(f(x)) = g(2x) = 2x + 3."),
        ("f(g(x)) and g(f(x)) are generally:", ["Always equal", "*Not equal (composition is not commutative)", "Always zero", "Undefined"],
         "Composition order matters — usually f∘g ≠ g∘f."),
        ("To find f⁻¹(x) from f(x) = 3x − 6:", ["Replace x with y", "*Swap x and y (x = 3y−6), solve: y = (x+6)/3", "Set f(x) = 0", "Multiply by −1"],
         "f⁻¹(x) = (x+6)/3."),
        ("f⁻¹(x) exists only if f is:", ["Constant", "Even", "*One-to-one", "Quadratic"],
         "One-to-one ensures each output maps back to exactly one input."),
        ("The graph of f⁻¹ is the reflection of f across:", ["The x-axis", "The y-axis", "*The line y = x", "The origin"],
         "Swapping x and y reflects across y = x."),
        ("If f(3) = 7, then f⁻¹(7) = ?", ["7", "*3", "0", "21"],
         "Inverse undoes f: if f sends 3 to 7, then f⁻¹ sends 7 to 3."),
        ("f(f⁻¹(x)) = ?", ["f(x)", "f⁻¹(x)", "*x", "0"],
         "Applying f after its inverse returns the original input."),
        ("Domain of f⁻¹ equals:", ["Domain of f", "*Range of f", "Range of f⁻¹", "All real numbers"],
         "What f outputs becomes what f⁻¹ takes as input."),
        ("f(x) = x² (x ≥ 0). f⁻¹(x) = ?", ["x²", "−√x", "*√x", "x/2"],
         "Restricting to x ≥ 0 makes it one-to-one; inverse is √x."),
        ("f(x) = eˣ. f⁻¹(x) = ?", ["eˣ", "1/eˣ", "*ln(x)", "10ˣ"],
         "The natural log is the inverse of the natural exponential."),
        ("f(x) = log₁₀(x). f⁻¹(x) = ?", ["log(x)", "x¹⁰", "*10ˣ", "1/x"],
         "The exponential 10ˣ inverts the common logarithm."),
        ("If f(x) = (x−1)/2, then f⁻¹(x) = ?", ["(x+1)/2", "*2x + 1", "x/2 − 1", "(x−2)/1"],
         "Swap: x = (y−1)/2 → 2x = y−1 → y = 2x+1."),
        ("Composition with an inverse: if h = f ∘ g, then h's domain requires:", ["Only f's domain", "Only g's domain", "*g(x) must be in the domain of f", "Nothing special"],
         "The output of g must be a valid input for f."),
        ("f(x) = x³ and g(x) = ∛x. f(g(x)) = ?", ["x³", "∛x", "*x", "x⁹"],
         "f(∛x) = (∛x)³ = x. They are inverses."),
        ("The inverse of f(x) = x + 5 is:", ["x − 1/5", "*f⁻¹(x) = x − 5", "f⁻¹(x) = 5x", "f⁻¹(x) = x/5"],
         "Undo adding 5 by subtracting 5."),
        ("Composition is associative: f ∘ (g ∘ h) = (f ∘ g) ∘ h.", ["False", "*True", "Only for linear functions", "Only for polynomials"],
         "Composition is associative (but not commutative)."),
        ("If f and g are inverses, then (f ∘ g)(x) = ?", ["f(x)", "g(x)", "*x", "0"],
         "Composing a function with its inverse gives the identity."),
        ("f(x) = 5x. f⁻¹(x) = ?", ["5x", "*x/5", "x − 5", "x + 5"],
         "Undo multiplying by 5 by dividing by 5."),
    ]
)
lessons[k] = v

# ── 1.9 Piecewise Functions ──
k, v = build_lesson(1, 9, "Piecewise Functions",
    "<h3>Piecewise Functions</h3>"
    "<p>A <b>piecewise function</b> uses different formulas for different parts of its domain.</p>"
    "<ul><li><b>Notation:</b> f(x) = { formula₁ if condition₁; formula₂ if condition₂; … }.</li>"
    "<li><b>Evaluating:</b> Determine which condition the input satisfies, then use that formula.</li>"
    "<li><b>Graphing:</b> Graph each piece on its interval. Use open circles (○) for excluded endpoints, closed circles (●) for included endpoints.</li>"
    "<li><b>Continuity:</b> A piecewise function is continuous if the pieces connect without gaps or jumps.</li>"
    "<li><b>Common examples:</b> Absolute value f(x) = |x| = {x if x ≥ 0; −x if x < 0}; step functions; tax brackets.</li></ul>",
    [
        ("Piecewise Function", "A function defined by different formulas on different intervals of its domain."),
        ("Open Circle (○)", "On a graph, indicates the endpoint is NOT included in that piece."),
        ("Closed Circle (●)", "On a graph, indicates the endpoint IS included in that piece."),
        ("Continuity of Piecewise Functions", "The function is continuous if the pieces connect at each boundary without gaps."),
        ("Absolute Value as Piecewise", "|x| = x if x ≥ 0; −x if x < 0."),
    ],
    [
        ("A piecewise function uses:", ["One formula for all x", "*Different formulas for different parts of the domain", "No formulas", "Only graphs"],
         "Different rules apply on different intervals."),
        ("f(x) = {x² if x < 0; 2x+1 if x ≥ 0}. f(3) = ?", ["9", "*7", "6", "3"],
         "3 ≥ 0, so use 2x+1: 2(3)+1 = 7."),
        ("f(x) = {x² if x < 0; 2x+1 if x ≥ 0}. f(−2) = ?", ["−3", "3", "*4", "−4"],
         "−2 < 0, so use x²: (−2)² = 4."),
        ("Open circle on a graph means:", ["*The endpoint is NOT included", "The endpoint is included", "The function is undefined everywhere", "There is no boundary"],
         "○ = excluded endpoint; ● = included."),
        ("|x| written as a piecewise function:", ["x for all x", "*x if x ≥ 0; −x if x < 0", "x² for all x", "−x for all x"],
         "Absolute value splits into two linear pieces."),
        ("A piecewise function is continuous at a boundary if:", ["The formulas are different", "*The left and right pieces agree at the boundary point", "There is a jump", "The function is always continuous"],
         "The function values from both sides must match at the boundary."),
        ("f(x) = {3x if x ≤ 1; x+2 if x > 1}. Is f continuous at x = 1?", ["*Yes — both pieces give 3 at x = 1", "No", "Cannot determine", "Only from the left"],
         "Left: 3(1)=3; Right: 1+2=3. They match."),
        ("f(x) = {2 if x < 0; 5 if x ≥ 0}. Is f continuous at x = 0?", ["Yes", "*No — the left limit is 2 but the right value is 5 (jump discontinuity)", "Always continuous", "Undefined"],
         "The function jumps from 2 to 5."),
        ("Graph each piece:", ["On the entire domain", "Only at one point", "*Only on its specified interval", "Without endpoints"],
         "Each formula applies only to its interval."),
        ("f(x) = {x+1 if x < 2; 5 if x = 2; x² if x > 2}. f(2) = ?", ["3", "*5", "4", "Undefined"],
         "The condition x = 2 specifies f(2) = 5."),
        ("Step functions (like the greatest integer function ⌊x⌋) are:", ["Continuous", "*Piecewise constant with jumps at each integer", "Always increasing", "Undefined for non-integers"],
         "Step functions jump at integer boundaries."),
        ("Tax brackets are modeled by:", ["Linear functions", "*Piecewise functions with different rates for different income ranges", "Constant functions", "Quadratic functions"],
         "Different tax rates apply to different portions of income."),
        ("The domain of a piecewise function is:", ["Only the first piece", "Only the last piece", "*The union of all the individual domains", "Always (−∞, ∞)"],
         "Combine all intervals where a formula is defined."),
        ("At a boundary where pieces meet with different values:", ["The function is continuous", "*There is a discontinuity (gap or jump)", "The function is undefined", "Both values apply"],
         "A jump between pieces creates a discontinuity."),
        ("f(x) = {√x if x ≥ 0; x+1 if x < 0}. f(4) = ?", ["5", "3", "*2", "4"],
         "4 ≥ 0, so use √x: √4 = 2."),
        ("f(x) = {√x if x ≥ 0; x+1 if x < 0}. f(−3) = ?", ["√3", "4", "*−2", "−3"],
         "−3 < 0, so use x+1: −3+1 = −2."),
        ("When graphing, the boundary point is included in:", ["Both pieces", "Neither piece", "*The piece whose condition includes it (≤ or ≥)", "Always the left piece"],
         "Check which condition uses ≤ or ≥ vs. < or >."),
        ("A piecewise-linear function consists of:", ["Curves connected at points", "*Straight-line segments connected at boundary points", "Only one line", "No boundaries"],
         "Each piece is a linear function, creating a chain of line segments."),
        ("f(x) = {1/x if x ≠ 0; 0 if x = 0}. This is:", ["Continuous", "*Piecewise-defined; not continuous at x = 0 since 1/x → ±∞ near 0", "Always 0", "Always 1/x"],
         "The limit of 1/x as x→0 doesn't exist, so defining f(0)=0 doesn't create continuity."),
        ("Piecewise functions appear in:", ["Only math", "*Real-world contexts like shipping rates, taxes, and utility pricing", "Only calculus", "Nowhere practical"],
         "Many real costs and rates change at thresholds."),
    ]
)
lessons[k] = v

# ── 1.10 Applications in Modeling ──
k, v = build_lesson(1, 10, "Applications in Modeling",
    "<h3>Applications in Modeling</h3>"
    "<p>Functions model real-world situations by relating inputs to outputs.</p>"
    "<ul><li><b>Linear models:</b> y = mx + b — constant rate of change. Example: distance = rate × time.</li>"
    "<li><b>Quadratic models:</b> Parabolic paths. Example: projectile motion h(t) = −16t² + v₀t + h₀.</li>"
    "<li><b>Exponential models:</b> Compound growth/decay. Example: population growth P(t) = P₀e<sup>rt</sup>.</li>"
    "<li><b>Piecewise models:</b> Different rules for different conditions (tax brackets, tiered pricing).</li>"
    "<li><b>Steps for modeling:</b><ol><li>Identify variables and relationships.</li><li>Choose an appropriate function type.</li><li>Write the equation.</li><li>Solve and interpret in context.</li></ol></li></ul>",
    [
        ("Mathematical Model", "A function or equation that represents a real-world relationship between variables."),
        ("Linear Model", "y = mx + b; constant rate of change — used for steady growth, motion at constant speed, etc."),
        ("Quadratic Model", "y = ax² + bx + c; parabolic — models projectile motion, area problems, profit optimization."),
        ("Exponential Model", "y = ab^t or y = ae^(rt); models growth/decay: populations, investments, radioactive decay."),
        ("Modeling Steps", "1) Identify variables. 2) Choose function type. 3) Write equation. 4) Solve and interpret."),
    ],
    [
        ("A car travels at 60 mph. Distance as a function of time:", ["d = 60 + t", "*d = 60t", "d = t/60", "d = 60/t"],
         "Distance = rate × time = 60t."),
        ("Projectile height: h(t) = −16t² + 48t + 5. The initial height is:", ["48", "−16", "*5", "0"],
         "At t = 0: h(0) = 5 (the constant term)."),
        ("Projectile height: h(t) = −16t² + 48t + 5. When does it hit the ground?", ["When h = 5", "*When h(t) = 0 — solve −16t² + 48t + 5 = 0", "When t = 0", "When t = 48"],
         "The projectile hits the ground when h(t) = 0."),
        ("Population doubles every 3 years. This is modeled by:", ["A linear function", "*An exponential function", "A quadratic function", "A logarithmic function"],
         "Doubling = multiplicative growth = exponential."),
        ("A bacteria colony starts at 100 and triples each hour. N(t) = ?", ["*100 · 3^t", "100 + 3t", "300t", "100t³"],
         "Exponential: N(t) = initial × growth^t = 100·3^t."),
        ("A pool has 10,000 gallons and drains at 500 gal/hr. Model:", ["V = 10000 + 500t", "*V = 10000 − 500t", "V = 500t", "V = 10000/t"],
         "Linear decrease: V(t) = 10000 − 500t."),
        ("The vertex of h(t) = −16t² + 48t + 5 gives:", ["The initial height", "The time to hit the ground", "*The maximum height and the time it occurs", "The velocity"],
         "The vertex of a downward parabola gives the maximum."),
        ("Which model is best for compound interest?", ["Linear", "Quadratic", "*Exponential", "Piecewise"],
         "Compound interest grows multiplicatively: A = P(1+r/n)^(nt)."),
        ("A parking lot charges $5 for the first hour, $3 for each additional hour. This is:", ["Linear", "Quadratic", "Exponential", "*Piecewise"],
         "Different rates for different time intervals = piecewise."),
        ("Area of a square as a function of side length s:", ["A = 4s", "*A = s²", "A = 2s", "A = s + 4"],
         "Area = side² — a quadratic function."),
        ("Revenue R = price × quantity. If price = 50 − 2q, then R(q) = ?", ["*R = (50−2q)q = 50q − 2q²", "R = 50q", "R = 50/q", "R = 2q²"],
         "R = pq = (50−2q)q = 50q − 2q² (quadratic model)."),
        ("To maximize revenue in R = 50q − 2q², find:", ["R(0)", "R(50)", "*The vertex of the parabola (q = −b/(2a) = 50/4 = 12.5)", "The y-intercept"],
         "Vertex gives the maximum of a downward parabola."),
        ("Radioactive half-life models use:", ["Linear decay", "Quadratic decay", "*Exponential decay: N(t) = N₀(1/2)^(t/T)", "Logarithmic growth"],
         "Half-life is exponential: the amount halves every T time units."),
        ("Modeling tip: always define your:", ["*Variables (what x and y represent, including units)", "Favorite function", "Graph first", "Answer only"],
         "Clear variable definitions are essential for meaningful models."),
        ("A phone depreciates 20% per year. After t years, value = ?", ["1000 − 200t", "*1000(0.8)^t", "1000(1.2)^t", "1000/t"],
         "Declining by 20% means retaining 80% each year — exponential decay."),
        ("Which function type has a constant rate of change?", ["Exponential", "Quadratic", "*Linear", "Logarithmic"],
         "Linear functions have constant slope."),
        ("The break-even point is where:", ["Revenue = 0", "Cost = 0", "*Revenue = Cost", "Profit is maximized"],
         "Break-even: no profit, no loss (R = C)."),
        ("A function model should be checked by:", ["Using only one data point", "Never checking", "*Comparing predictions to actual data and assessing reasonableness", "Using aesthetic criteria"],
         "Models should be validated against real observations."),
        ("Choosing between models depends on:", ["Personal preference", "*The pattern in the data (constant change, multiplicative change, parabolic shape, etc.)", "The number of variables", "Nothing — one model fits all"],
         "Match the function type to the data's behavior."),
        ("In context, always interpret:", ["Raw numbers only", "*What the answer means in the real-world scenario (units, meaning)", "Nothing — just compute", "Only the formula"],
         "Context makes mathematics useful."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 1)")
