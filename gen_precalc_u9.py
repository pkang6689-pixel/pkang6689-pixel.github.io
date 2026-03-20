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

# ── 9.1 Concept of Limits ─────────────────────────────────────────
k, v = build_lesson(9, 1,
    "Concept of Limits (graphical, numerical approaches)",
    "<h3>Concept of Limits</h3>"
    "<p>The <b>limit</b> of f(x) as x approaches c, written lim_{x→c} f(x) = L, means f(x) gets arbitrarily close to L as x gets close to c.</p>"
    "<h4>Approaches</h4>"
    "<ul>"
    "<li><b>Graphical:</b> Read the y-value the graph approaches as x → c.</li>"
    "<li><b>Numerical:</b> Make a table of x-values approaching c from both sides.</li>"
    "<li>The limit may exist even if f(c) is undefined (e.g., holes).</li>"
    "</ul>"
    "<h4>When Limits Don't Exist</h4>"
    "<ul>"
    "<li>Left-hand and right-hand limits disagree.</li>"
    "<li>Function oscillates without settling.</li>"
    "<li>Function increases/decreases without bound.</li>"
    "</ul>",
    [
        ("Limit Definition", "lim_{x→c} f(x) = L means f(x) → L as x → c."),
        ("Left-Hand Limit", "lim_{x→c⁻} f(x); the limit as x approaches c from the left."),
        ("Right-Hand Limit", "lim_{x→c⁺} f(x); the limit as x approaches c from the right."),
        ("Limit Exists Condition", "The limit exists iff left-hand limit = right-hand limit."),
        ("Limit vs Function Value", "lim_{x→c} f(x) can differ from f(c); the limit depends only on nearby values.")
    ],
    [
        ("lim_{x→2} (3x + 1) = ?", ["3", "*7", "6", "5"],
         "Direct substitution: 3(2)+1 = 7."),
        ("If f(x) = (x²−4)/(x−2), lim_{x→2} f(x) = ?", ["0", "Undefined", "*4", "2"],
         "Factor: (x+2)(x−2)/(x−2) = x+2. Limit = 4."),
        ("f(2) in the above example is:", ["4", "0", "*Undefined (0/0)", "2"],
         "Direct substitution gives 0/0 — undefined."),
        ("A limit exists only if:", ["f(c) exists", "*Left and right limits are equal", "The function is differentiable", "The function is continuous"],
         "Limit exists ⟺ left-hand = right-hand limit."),
        ("Graphically, a hole at (2, 4) means:", ["No limit", "*lim_{x→2} f(x) = 4 but f(2) ≠ 4", "f(2) = 4", "The graph is broken"],
         "The limit can exist at a hole; only f(c) is missing or different."),
        ("lim_{x→0} |x|/x:", ["1", "0", "*Does not exist (left = −1, right = 1)", "−1"],
         "From right: 1. From left: −1. They disagree."),
        ("lim_{x→0} sin(1/x):", ["0", "1", "*Does not exist (oscillates)", "∞"],
         "sin(1/x) oscillates faster and faster near 0."),
        ("Numerically estimate lim_{x→1} (x²−1)/(x−1). Try x = 0.9, 0.99, 1.01, 1.1:", ["Values approach 1", "*Values approach 2", "Values approach 0", "Values diverge"],
         "(x²−1)/(x−1) = x+1. As x → 1, value → 2."),
        ("lim_{x→3} 5 = ?", ["3", "0", "*5", "15"],
         "Limit of a constant is that constant."),
        ("lim_{x→∞} 1/x = ?", ["1", "∞", "*0", "−∞"],
         "As x grows, 1/x shrinks to 0."),
        ("If lim_{x→c⁻} f(x) = 3 and lim_{x→c⁺} f(x) = 5, lim_{x→c} f(x) = ?", ["3", "5", "4", "*Does not exist"],
         "Left ≠ right → limit DNE."),
        ("lim_{x→0⁺} 1/x = ?", ["0", "−∞", "*+∞", "1"],
         "Approaching 0 from the right, 1/x → +∞."),
        ("lim_{x→0⁻} 1/x = ?", ["0", "+∞", "*−∞", "−1"],
         "From the left, 1/x → −∞."),
        ("Which is NOT needed for a limit to exist at x = c?", ["Left-hand limit exists", "Right-hand limit exists", "Left = Right limit", "*f(c) must be defined"],
         "f(c) need not exist for the limit to exist."),
        ("lim_{x→4} √x = ?", ["4", "16", "*2", "√4"],
         "√4 = 2."),
        ("If f(x) = {x+1 for x<2, x² for x≥2}. lim_{x→2} f(x) = ?", ["*Does not exist (left=3, right=4)", "3", "4", "2"],
         "Left: 2+1=3. Right: 2²=4. 3≠4 → DNE."),
        ("lim_{x→π} cos x = ?", ["0", "1", "*−1", "π"],
         "cos π = −1."),
        ("A function is continuous at c if (i) f(c) exists, (ii) lim exists, and (iii):", ["f is differentiable", "*lim_{x→c} f(x) = f(c)", "f(c) = 0", "f is bounded"],
         "Three conditions for continuity."),
        ("Table: x = 1.9, 1.99, 1.999, 2.001, 2.01, 2.1; f(x) ≈ 3.9, 3.99, 3.999, 4.001, 4.01, 4.1. Limit ≈ ?", ["3.9", "*4", "4.1", "DNE"],
         "Values approach 4 from both sides."),
        ("The notation lim_{x→c} is read:", ["x equals c", "*x approaches c", "x is greater than c", "x is at c"],
         "The arrow means 'approaches.'")
    ]
)
lessons[k] = v

# ── 9.2 Evaluating Limits Algebraically ───────────────────────────
k, v = build_lesson(9, 2,
    "Evaluating Limits Algebraically",
    "<h3>Evaluating Limits Algebraically</h3>"
    "<h4>Techniques</h4>"
    "<ul>"
    "<li><b>Direct substitution:</b> Try plugging in c first.</li>"
    "<li><b>Factoring:</b> If 0/0, factor and cancel common factors.</li>"
    "<li><b>Rationalizing:</b> Multiply by conjugate for radical expressions.</li>"
    "<li><b>Common factor:</b> Simplify complex fractions.</li>"
    "</ul>"
    "<h4>Limit Laws</h4>"
    "<ul>"
    "<li>Sum: lim(f+g) = lim f + lim g</li>"
    "<li>Product: lim(f·g) = lim f · lim g</li>"
    "<li>Quotient: lim(f/g) = lim f / lim g (if lim g ≠ 0)</li>"
    "</ul>",
    [
        ("Direct Substitution", "If f is continuous at c, lim_{x→c} f(x) = f(c)."),
        ("Factoring Technique", "For 0/0 forms, factor numerator/denominator and cancel."),
        ("Rationalizing Technique", "Multiply by conjugate to eliminate radicals (e.g., √a − √b)."),
        ("Sum Law", "lim(f + g) = lim f + lim g."),
        ("Squeeze Theorem", "If g(x) ≤ f(x) ≤ h(x) and lim g = lim h = L, then lim f = L.")
    ],
    [
        ("lim_{x→3} (x² + 2x) = ?", ["9", "15", "*15", "12"],
         "Direct: 9 + 6 = 15."),
        ("lim_{x→1} (x³ − 1)/(x − 1) = ?", ["0", "1", "*3", "Undefined"],
         "Factor: (x−1)(x²+x+1)/(x−1) = x²+x+1. At x=1: 3."),
        ("lim_{x→4} (x − 4)/(√x − 2) = ?", ["0", "2", "*4", "Undefined"],
         "Rationalize: multiply by (√x+2)/(√x+2). (x−4)/((√x−2)(√x+2)) · ... = (√x+2)(x−4)/(x−4) = √x+2. At x=4: 4."),
        ("lim_{x→0} (√(x+9) − 3)/x = ?", ["0", "3", "*1/6", "Undefined"],
         "Rationalize: multiply by (√(x+9)+3)/(√(x+9)+3). = x/(x(√(x+9)+3)) = 1/(√(x+9)+3). At 0: 1/6."),
        ("lim_{x→2} (x² − 4)/(x² − x − 2) = ?", ["1", "0", "*4/3", "2/3"],
         "(x−2)(x+2)/((x−2)(x+1)) = (x+2)/(x+1). At x=2: 4/3."),
        ("lim_{x→−1} (x² + 3x + 2)/(x + 1) = ?", ["0", "*1", "Undefined", "−1"],
         "(x+1)(x+2)/(x+1) = x+2. At −1: 1."),
        ("lim_{x→0} sin x / x = ?", ["0", "*1", "Undefined", "∞"],
         "Fundamental trig limit."),
        ("lim_{x→0} (1 − cos x)/x = ?", ["1", "*0", "1/2", "−1"],
         "Standard limit."),
        ("Sum law: lim_{x→c} [f(x) + g(x)] = ?", ["lim f · lim g", "*lim f + lim g", "lim(f/g)", "Cannot split"],
         "Limit of sum = sum of limits."),
        ("Product law: lim_{x→c} [f(x)·g(x)] = ?", ["lim f + lim g", "*lim f · lim g", "lim f − lim g", "1"],
         "Limit of product = product of limits."),
        ("lim_{x→5} (x² − 25)/(x − 5) = ?", ["0", "5", "*10", "25"],
         "(x−5)(x+5)/(x−5)=x+5. At 5: 10."),
        ("lim_{x→0} x sin(1/x) = ?", ["1", "Undefined", "*0", "∞"],
         "Squeeze: −|x| ≤ x sin(1/x) ≤ |x|, and |x| → 0."),
        ("lim_{x→0} (2x)/tan x = ?", ["0", "1", "*2", "∞"],
         "2x/tan x = 2x cos x/sin x = 2(x/sin x) cos x → 2·1·1 = 2."),
        ("lim_{x→0} tan x / x = ?", ["0", "*1", "∞", "1/2"],
         "tan x/x = (sin x/x)(1/cos x) → 1·1 = 1."),
        ("For the form 0/0, always try:", ["Giving up", "*Factoring, rationalizing, or L'Hôpital's rule", "Setting limit = 0", "Direct substitution again"],
         "Indeterminate form requires algebraic manipulation."),
        ("lim_{x→∞} (3x² + x)/(x² − 2) = ?", ["∞", "0", "1", "*3"],
         "Divide top and bottom by x²: (3 + 1/x)/(1 − 2/x²) → 3."),
        ("lim_{x→∞} (5x)/(x² + 1) = ?", ["5", "∞", "*0", "1"],
         "Degree of denominator > numerator → 0."),
        ("lim_{x→∞} (2x³ + 1)/(x² − 3) = ?", ["2", "0", "*∞", "−3"],
         "Degree of numerator > denominator → ∞."),
        ("Squeeze theorem: if −x² ≤ f(x) ≤ x² and x → 0, lim f(x) = ?", ["x²", "−x²", "*0", "Undefined"],
         "Both bounds → 0, so f(x) → 0."),
        ("lim_{x→3} √(x² + 7) = ?", ["3", "7", "*4", "16"],
         "√(9+7) = √16 = 4.")
    ]
)
lessons[k] = v

# ── 9.3 One-Sided Limits ──────────────────────────────────────────
k, v = build_lesson(9, 3,
    "One-Sided Limits",
    "<h3>One-Sided Limits</h3>"
    "<p>One-sided limits consider the behavior of f(x) as x approaches c from one direction only.</p>"
    "<h4>Notation</h4>"
    "<ul>"
    "<li>lim_{x→c⁻} f(x): approach from the left (x &lt; c).</li>"
    "<li>lim_{x→c⁺} f(x): approach from the right (x &gt; c).</li>"
    "</ul>"
    "<h4>Key Principle</h4>"
    "<ul>"
    "<li>lim_{x→c} f(x) exists ⟺ lim_{x→c⁻} f(x) = lim_{x→c⁺} f(x).</li>"
    "</ul>",
    [
        ("Left-Hand Limit", "lim_{x→c⁻} f(x): value f approaches as x → c from below."),
        ("Right-Hand Limit", "lim_{x→c⁺} f(x): value f approaches as x → c from above."),
        ("Two-Sided Limit Exists", "Iff left-hand = right-hand limit (and both exist)."),
        ("Jump Discontinuity", "Occurs when left-hand and right-hand limits exist but are unequal."),
        ("Endpoint Limit", "At the boundary of a domain, only one one-sided limit is relevant.")
    ],
    [
        ("lim_{x→0⁺} √x = ?", ["−1", "Undefined", "*0", "∞"],
         "√x → 0 as x → 0⁺."),
        ("lim_{x→0⁻} √x:", ["0", "*Does not exist (√x undefined for x < 0 in reals)", "−∞", "Undefined"],
         "√x requires x ≥ 0 in real numbers."),
        ("f(x) = {x+1, x<2; x², x≥2}. lim_{x→2⁻} f(x) = ?", ["4", "*3", "2", "5"],
         "Use x+1: 2+1 = 3 (approaching from left)."),
        ("For the above, lim_{x→2⁺} f(x) = ?", ["3", "*4", "2", "5"],
         "Use x²: 2² = 4 (approaching from right)."),
        ("Does lim_{x→2} f(x) exist for the above?", ["Yes, it's 3", "Yes, it's 4", "*No, left ≠ right (3 ≠ 4)", "Yes, it's 3.5"],
         "Left = 3, right = 4. Not equal → DNE."),
        ("lim_{x→1⁺} 1/(x−1) = ?", ["0", "−∞", "*+∞", "1"],
         "x → 1⁺: denominator tiny positive → +∞."),
        ("lim_{x→1⁻} 1/(x−1) = ?", ["0", "+∞", "*−∞", "−1"],
         "x → 1⁻: denominator tiny negative → −∞."),
        ("Floor function ⌊x⌋: lim_{x→3⁻} ⌊x⌋ = ?", ["3", "*2", "2.99", "Undefined"],
         "Just below 3, ⌊x⌋ = 2."),
        ("lim_{x→3⁺} ⌊x⌋ = ?", ["2", "*3", "4", "Undefined"],
         "Just above 3, ⌊x⌋ = 3."),
        ("The floor function at integers has what type of discontinuity?", ["Removable", "*Jump", "Infinite", "Oscillating"],
         "Left and right limits differ → jump discontinuity."),
        ("f(x) = |x−5|/(x−5). lim_{x→5⁺} f(x) = ?", ["−1", "*1", "0", "5"],
         "x > 5: |x−5| = x−5. So f(x) = 1."),
        ("lim_{x→5⁻} |x−5|/(x−5) = ?", ["1", "*−1", "0", "Undefined"],
         "x < 5: |x−5| = −(x−5). So f(x) = −1."),
        ("lim_{x→0⁺} ln x = ?", ["0", "1", "*−∞", "+∞"],
         "Natural log approaches −∞ as x → 0⁺."),
        ("lim_{x→∞} arctan x = ?", ["∞", "0", "*π/2", "1"],
         "arctan x → π/2 as x → ∞."),
        ("lim_{x→−∞} arctan x = ?", ["−∞", "0", "*−π/2", "π/2"],
         "arctan x → −π/2 as x → −∞."),
        ("g(x) = {sin x/x, x≠0; 1, x=0}. lim_{x→0} g(x) = ?", ["0", "*1", "Undefined", "sin 1"],
         "lim sin x/x = 1, and g(0) = 1. (Continuous at 0.)"),
        ("One-sided limits are essential for analyzing:", ["Polynomials", "*Piecewise and discontinuous functions", "Linear functions", "Constants"],
         "Piecewise functions often have different formulas on each side."),
        ("If lim_{x→c⁻} f(x) = L and lim_{x→c⁺} f(x) = L, then:", ["lim DNE", "*lim_{x→c} f(x) = L", "f(c) = L", "f is differentiable"],
         "Equal one-sided limits → two-sided limit exists."),
        ("lim_{x→0⁺} e^(−1/x) = ?", ["1", "e", "*0", "∞"],
         "As x → 0⁺, −1/x → −∞, so e^(−∞) = 0."),
        ("At a vertical asymptote x = a, one-sided limits are:", ["Both finite", "Both zero", "*±∞", "Both equal"],
         "Function blows up near vertical asymptotes.")
    ]
)
lessons[k] = v

# ── 9.4 Continuity & Types of Discontinuities ─────────────────────
k, v = build_lesson(9, 4,
    "Continuity & Types of Discontinuities",
    "<h3>Continuity &amp; Discontinuities</h3>"
    "<h4>Continuity at a Point</h4>"
    "<ul>"
    "<li>f is continuous at c if: (1) f(c) is defined, (2) lim_{x→c} f(x) exists, (3) lim_{x→c} f(x) = f(c).</li>"
    "</ul>"
    "<h4>Types of Discontinuities</h4>"
    "<ul>"
    "<li><b>Removable (hole):</b> limit exists but f(c) is missing or different.</li>"
    "<li><b>Jump:</b> left and right limits both exist but differ.</li>"
    "<li><b>Infinite:</b> function approaches ±∞ (vertical asymptote).</li>"
    "<li><b>Oscillating:</b> function oscillates without settling (e.g., sin(1/x) at 0).</li>"
    "</ul>",
    [
        ("Continuous at a Point", "f(c) defined, lim exists, and lim = f(c)."),
        ("Removable Discontinuity", "Limit exists but ≠ f(c) (or f(c) undefined); can be 'fixed' by redefining f(c)."),
        ("Jump Discontinuity", "Left and right limits both exist but are unequal."),
        ("Infinite Discontinuity", "lim_{x→c} f(x) = ±∞; vertical asymptote at x = c."),
        ("Intermediate Value Theorem", "If f is continuous on [a,b] and N is between f(a) and f(b), then f(c)=N for some c in (a,b).")
    ],
    [
        ("f is continuous at c requires how many conditions?", ["1", "2", "*3", "4"],
         "f(c) defined, limit exists, limit = f(c)."),
        ("f(x) = (x²−9)/(x−3) at x = 3 has what type of discontinuity?", ["Jump", "*Removable (hole)", "Infinite", "None"],
         "Limit = 6, but f(3) undefined. Can be fixed by defining f(3) = 6."),
        ("f(x) = 1/(x−2) at x = 2 has what type of discontinuity?", ["Removable", "Jump", "*Infinite (vertical asymptote)", "None"],
         "lim → ±∞."),
        ("f(x) = {1, x<0; 2, x≥0} at x = 0:", ["Removable", "*Jump", "Infinite", "Continuous"],
         "Left limit = 1, right limit = 2. Jump."),
        ("f(x) = sin(1/x) at x = 0:", ["Jump", "Removable", "Infinite", "*Oscillating"],
         "Oscillates infinitely without settling."),
        ("All polynomials are:", ["Discontinuous somewhere", "*Continuous everywhere", "Only continuous at 0", "Continuous except at roots"],
         "Polynomials are continuous for all real x."),
        ("f(x) = √x is continuous on:", ["(−∞, ∞)", "*[0, ∞)", "(0, ∞)", "[−∞, ∞]"],
         "Defined and continuous for x ≥ 0."),
        ("Which can be 'fixed' by redefining one point?", ["Jump", "Infinite", "*Removable", "Oscillating"],
         "Removable = define/redefine f(c) = limit."),
        ("IVT: If f is continuous on [1, 5], f(1)=−2, f(5)=6, then:", ["f has no zeros", "*f(c)=0 for some c in (1,5)", "f(3)=2", "f is increasing"],
         "0 is between −2 and 6 → by IVT, f(c)=0 for some c."),
        ("f(x) = |x| at x = 0 is:", ["Discontinuous", "*Continuous but not differentiable", "Differentiable", "Undefined"],
         "|0| = 0, limit = 0. Continuous. (Corner → not differentiable.)"),
        ("Rational functions are continuous wherever:", ["Always", "*The denominator ≠ 0", "The numerator = 0", "Both are positive"],
         "Rational = polynomial/polynomial, continuous where denominator ≠ 0."),
        ("f(x) = ln x is continuous on:", ["(−∞, ∞)", "*（0, ∞)", "[0, ∞)", "[1, ∞)"],
         "ln x defined for x > 0."),
        ("Composition: if f continuous at c and g continuous at f(c), then g∘f is:", ["Discontinuous", "*Continuous at c", "Undefined", "Only sometimes continuous"],
         "Composition of continuous functions is continuous."),
        ("f(x) = {(x²−1)/(x−1), x≠1; 3, x=1}. At x = 1:", ["Continuous", "*Removable discontinuity (limit=2 ≠ f(1)=3)", "Jump", "Infinite"],
         "lim = (x+1) at 1 = 2. f(1) = 3 ≠ 2."),
        ("To make the above continuous, redefine f(1) = ?", ["3", "1", "*2", "0"],
         "Set f(1) = limit = 2."),
        ("e^x is continuous on:", ["(0, ∞)", "[0, ∞)", "*（−∞, ∞)", "[1, ∞)"],
         "Exponential is continuous everywhere."),
        ("tan x has infinite discontinuities at:", ["x = nπ", "*x = π/2 + nπ", "x = 2nπ", "Nowhere"],
         "tan x = sin x/cos x; undefined where cos x = 0."),
        ("Continuity on a closed interval [a,b] requires:", ["Only interior continuity", "*Continuity on (a,b) plus correct one-sided limits at endpoints", "f(a) = f(b)", "Differentiability"],
         "Continuous on interior, right-continuous at a, left-continuous at b."),
        ("The IVT guarantees existence of a root but not:", ["The root itself", "Continuity", "*Uniqueness or location of the root", "The function"],
         "IVT says 'there exists c' but doesn't specify how many or where exactly."),
        ("f(x) = 1/x² at x = 0:", ["Removable", "Jump", "*Infinite (both sides → +∞)", "Continuous"],
         "1/x² → +∞ from both sides. Infinite discontinuity.")
    ]
)
lessons[k] = v

# ── 9.5 Infinite Limits & Asymptotic Behavior ─────────────────────
k, v = build_lesson(9, 5,
    "Infinite Limits & Asymptotic Behavior",
    "<h3>Infinite Limits &amp; Asymptotic Behavior</h3>"
    "<h4>Infinite Limits</h4>"
    "<ul>"
    "<li>lim_{x→c} f(x) = ∞ means f(x) grows without bound near c.</li>"
    "<li>Corresponds to a <b>vertical asymptote</b> at x = c.</li>"
    "</ul>"
    "<h4>Limits at Infinity</h4>"
    "<ul>"
    "<li>lim_{x→∞} f(x) = L means f(x) → L as x grows large.</li>"
    "<li>Corresponds to a <b>horizontal asymptote</b> y = L.</li>"
    "</ul>"
    "<h4>End Behavior of Rationals</h4>"
    "<ul>"
    "<li>degree(num) &lt; degree(denom): HA at y = 0.</li>"
    "<li>degree(num) = degree(denom): HA at y = ratio of leading coefficients.</li>"
    "<li>degree(num) &gt; degree(denom): no HA (oblique or grows without bound).</li>"
    "</ul>",
    [
        ("Vertical Asymptote", "x = c where lim_{x→c} f(x) = ±∞."),
        ("Horizontal Asymptote", "y = L where lim_{x→±∞} f(x) = L."),
        ("End Behavior of Rationals", "Compare degrees of numerator and denominator to find HA."),
        ("Oblique Asymptote", "Occurs when numerator degree = denominator degree + 1; found by polynomial division."),
        ("Limit at Infinity", "lim_{x→∞} f(x) describes the long-run behavior of f.")
    ],
    [
        ("lim_{x→0} 1/x² = ?", ["0", "−∞", "*+∞", "Undefined"],
         "1/x² → +∞ from both sides."),
        ("lim_{x→∞} (3x+1)/(x−2) = ?", ["1", "0", "*3", "∞"],
         "Leading coefficients: 3/1 = 3."),
        ("lim_{x→∞} 5/(x²+1) = ?", ["5", "∞", "*0", "1"],
         "Degree denom > num → 0."),
        ("lim_{x→∞} (x³+2)/(2x²−1) = ?", ["3/2", "0", "1/2", "*∞"],
         "Degree num > denom → grows without bound."),
        ("f(x) = 1/(x−3): vertical asymptote at:", ["x = 0", "*x = 3", "x = −3", "No VA"],
         "Denominator = 0 at x = 3."),
        ("f(x) = (2x)/(x+5): horizontal asymptote:", ["y = 0", "y = 5", "*y = 2", "No HA"],
         "2x/x → 2."),
        ("f(x) = (x²+1)/(x−1): type of asymptote beyond vertical?", ["Horizontal", "*Oblique (slant)", "None", "Parabolic"],
         "Degree num = degree denom + 1 → oblique asymptote."),
        ("Find the oblique asymptote of (x²+1)/(x−1):", ["y = x", "*y = x + 1", "y = x − 1", "y = x²"],
         "Divide: x² + 1 = (x−1)(x+1) + 2. Asymptote: y = x+1."),
        ("lim_{x→−∞} e^x = ?", ["∞", "1", "*0", "−∞"],
         "e^x → 0 as x → −∞."),
        ("lim_{x→∞} e^x = ?", ["0", "1", "*∞", "e"],
         "e^x grows without bound."),
        ("An HA at y = L means:", ["f(x) never equals L", "*f(x) gets closer to L as x → ±∞", "f(x) = L always", "x = L is an asymptote"],
         "HA describes end behavior."),
        ("Can a function cross its HA?", ["Never", "*Yes, it can cross a HA", "Only once", "Only at x = 0"],
         "HA only governs behavior as x → ±∞. Function can cross it elsewhere."),
        ("lim_{x→∞} sin x/x = ?", ["1", "sin 1", "*0", "DNE"],
         "−1/x ≤ sin x/x ≤ 1/x → 0 (squeeze)."),
        ("f(x) = (x²−4)/(x²−1): vertical asymptotes at:", ["x = ±2", "*x = ±1", "x = 0", "No VA"],
         "Denom = 0 at x = ±1."),
        ("Same function: horizontal asymptote:", ["y = 0", "y = 4", "*y = 1", "y = −4"],
         "Same degree, lead coefficients 1/1 = 1."),
        ("lim_{x→2⁺} 1/(x−2) = ?", ["−∞", "0", "*+∞", "1/2"],
         "Tiny positive denominator → +∞."),
        ("lim_{x→2⁻} 1/(x−2) = ?", ["+∞", "0", "*−∞", "−1/2"],
         "Tiny negative denominator → −∞."),
        ("f(x) = (3x² − x)/(6x² + 2): HA at y = ?", ["3", "0", "*1/2", "6"],
         "3/6 = 1/2."),
        ("lim_{x→∞} x/(√(x²+1)) = ?", ["0", "∞", "*1", "1/2"],
         "x/√(x²+1) = x/(|x|√(1+1/x²)). For x>0: 1/√(1+1/x²) → 1."),
        ("f(x) = 2^x − 5. Horizontal asymptote as x → −∞:", ["y = 0", "y = 2", "*y = −5", "y = −∞"],
         "2^x → 0 as x → −∞. So 2^x − 5 → −5.")
    ]
)
lessons[k] = v

# ── 9.6 Applications: Instantaneous Rate of Change ────────────────
k, v = build_lesson(9, 6,
    "Applications: Instantaneous Rate of Change",
    "<h3>Instantaneous Rate of Change</h3>"
    "<p>The <b>instantaneous rate of change</b> of f at x = a is the limit of the average rate of change over shrinking intervals.</p>"
    "<h4>Formula</h4>"
    "<ul>"
    "<li>Instantaneous rate = lim_{h→0} [f(a+h) − f(a)] / h</li>"
    "<li>This equals the <b>derivative</b> f'(a) — the slope of the tangent line at x = a.</li>"
    "</ul>"
    "<h4>Average vs Instantaneous</h4>"
    "<ul>"
    "<li>Average rate = Δy/Δx = [f(b)−f(a)]/(b−a) (secant line).</li>"
    "<li>Instantaneous rate = limit of average rate as interval shrinks to zero (tangent line).</li>"
    "</ul>",
    [
        ("Average Rate of Change", "[f(b)−f(a)]/(b−a); slope of the secant line between (a,f(a)) and (b,f(b))."),
        ("Instantaneous Rate of Change", "lim_{h→0} [f(a+h)−f(a)]/h; slope of the tangent line at x = a."),
        ("Difference Quotient", "[f(a+h)−f(a)]/h; the expression whose limit gives the derivative."),
        ("Secant Line", "A line through two points on a curve; slope = average rate."),
        ("Tangent Line", "Touches the curve at one point; slope = instantaneous rate = derivative.")
    ],
    [
        ("Average rate of f(x) = x² from x=1 to x=3:", ["2", "8", "*4", "6"],
         "(9−1)/(3−1) = 8/2 = 4."),
        ("f(x) = x². Difference quotient at a=2:", ["*((2+h)²−4)/h = (4+4h+h²−4)/h = 4+h", "4", "2h", "h²"],
         "Simplify to 4 + h."),
        ("Instantaneous rate of f(x)=x² at x=2:", ["2", "*4", "8", "0"],
         "lim_{h→0} (4+h) = 4."),
        ("The difference quotient is:", ["f(a)/h", "*[f(a+h)−f(a)]/h", "f(a+h)·h", "[f(a)−f(h)]/a"],
         "Standard definition."),
        ("As h → 0, the secant line becomes:", ["A horizontal line", "A vertical line", "*The tangent line", "Undefined"],
         "Secant → tangent as the two points merge."),
        ("Velocity is the instantaneous rate of change of:", ["Acceleration", "Force", "*Position", "Time"],
         "v = ds/dt = limit of Δs/Δt."),
        ("f(x) = 3x + 5. Instantaneous rate at any x:", ["5", "*3", "3x", "8"],
         "Linear function: rate = slope = 3 everywhere."),
        ("f(x) = x³. Difference quotient at a:", ["3a²", "*(3a²+3ah+h²)", "a³", "3a"],
         "[(a+h)³−a³]/h = 3a²+3ah+h². Limit = 3a²."),
        ("f(x) = x³. Instantaneous rate at x = 1:", ["1", "*3", "0", "6"],
         "3(1)² = 3."),
        ("The tangent line to f(x)=x² at x=3 has slope:", ["3", "9", "*6", "2"],
         "f'(x)=2x. f'(3)=6."),
        ("Equation of tangent to f(x)=x² at (3,9):", ["y = 3x", "y = 9x − 18", "*y = 6x − 9", "y = 6x + 9"],
         "y − 9 = 6(x − 3) → y = 6x − 9."),
        ("Average speed from t=0 to t=4, s(t)=t²:", ["4", "16", "*4", "8"],
         "(16−0)/4 = 4."),
        ("Instantaneous speed at t=4, s(t)=t²:", ["4", "*8", "16", "2"],
         "s'(t)=2t. s'(4)=8."),
        ("The difference quotient is also called:", ["The derivative", "*The Newton quotient", "The integral", "The limit"],
         "Also known as Newton's difference quotient."),
        ("f(x)=1/x. Difference quotient at a:", ["−1/a²", "*(−1)/(a(a+h))", "1/(a+h)", "h/a"],
         "[1/(a+h)−1/a]/h = [a−(a+h)]/(a(a+h)h) = −1/(a(a+h))."),
        ("f(x)=1/x. Instantaneous rate at x=2:", ["1/2", "−1/2", "1/4", "*−1/4"],
         "lim −1/(2(2+h)) = −1/4."),
        ("A ball at height h(t) = −16t²+64t. Instantaneous velocity at t=1:", ["64", "48", "*32", "0"],
         "h'(t)=−32t+64. h'(1)=32."),
        ("The word 'instantaneous' means at a single:", ["Interval", "*Moment", "Period", "Average"],
         "Rate at one specific instant, not over an interval."),
        ("A car's speedometer shows:", ["Average speed", "*Instantaneous speed", "Total distance", "Acceleration"],
         "The speedometer reads the speed at that instant."),
        ("If f'(a) > 0, the function is ___ at x = a:", ["Decreasing", "*Increasing", "Constant", "Undefined"],
         "Positive derivative → function increasing.")
    ]
)
lessons[k] = v

# ── 9.7 Piecewise Functions & Limits ──────────────────────────────
k, v = build_lesson(9, 7,
    "Piecewise Functions & Limits",
    "<h3>Piecewise Functions &amp; Limits</h3>"
    "<p>A <b>piecewise function</b> is defined by different formulas on different intervals.</p>"
    "<h4>Evaluating Limits</h4>"
    "<ul>"
    "<li>At a boundary point c between pieces, compute both one-sided limits.</li>"
    "<li>lim_{x→c⁻}: use the formula for x &lt; c.</li>"
    "<li>lim_{x→c⁺}: use the formula for x &gt; c (or x ≥ c).</li>"
    "<li>Limit exists only if both one-sided limits agree.</li>"
    "</ul>"
    "<h4>Making Piecewise Functions Continuous</h4>"
    "<ul>"
    "<li>Choose parameters so that the pieces 'meet' at boundary points.</li>"
    "</ul>",
    [
        ("Piecewise Function", "A function defined by different formulas on different intervals of its domain."),
        ("Boundary Point", "A point where the defining formula changes; check one-sided limits here."),
        ("Continuity Check", "At each boundary, verify left limit = right limit = function value."),
        ("Making Continuous", "Set parameters (like a, b) so pieces connect: left limit = right limit."),
        ("Piecewise Examples", "Absolute value |x| = {x, x≥0; −x, x<0} is a classic piecewise function.")
    ],
    [
        ("f(x) = {2x, x<1; x²+1, x≥1}. f(1) = ?", ["2", "*2", "1", "3"],
         "x=1: use x²+1 = 1+1 = 2."),
        ("lim_{x→1⁻} f(x) for the above?", ["*2", "1", "0", "3"],
         "Use 2x: 2(1) = 2."),
        ("lim_{x→1⁺} f(x) for the above?", ["*2", "1", "3", "0"],
         "Use x²+1: 1+1 = 2."),
        ("Is f continuous at x = 1?", ["*Yes (left = right = f(1) = 2)", "No", "Only from the left", "Only from the right"],
         "All three conditions met."),
        ("g(x) = {x+3, x<2; 2x, x≥2}. lim_{x→2⁻} g(x) = ?", ["4", "*5", "2", "7"],
         "x+3 at 2: 5."),
        ("lim_{x→2⁺} g(x) = ?", ["5", "2", "*4", "6"],
         "2x at 2: 4."),
        ("Is g continuous at x = 2?", ["Yes", "*No (5 ≠ 4)", "Only from right", "Only from left"],
         "Jump discontinuity."),
        ("h(x) = {ax+1, x<3; 10, x=3; x²+b, x>3}. For continuity at x=3, left limit = ?", ["10", "*3a+1", "9+b", "a+3"],
         "lim_{x→3⁻} (ax+1) = 3a+1."),
        ("Right limit = ?", ["3a+1", "10", "*9+b", "3b+9"],
         "lim_{x→3⁺} (x²+b) = 9+b."),
        ("For continuity: 3a+1 = 10 and 9+b = 10. So a = ?, b = ?", ["a=2, b=2", "*a=3, b=1", "a=1, b=3", "a=3, b=0"],
         "3a+1=10 → a=3. 9+b=10 → b=1."),
        ("|x| = {x, x≥0; −x, x<0}. lim_{x→0} |x| = ?", ["DNE", "−0", "*0", "Undefined"],
         "Left: −x → 0. Right: x → 0. Both = 0."),
        ("f(x) = {1/x, x≠0; 0, x=0}. lim_{x→0} f(x) = ?", ["0", "1", "*DNE (±∞)", "Undefined"],
         "Left → −∞, right → +∞. DNE."),
        ("For piecewise functions, where should you check continuity?", ["Everywhere", "*At boundary points where the formula changes", "Only at x=0", "Only at endpoints"],
         "Boundary points are where potential discontinuities occur."),
        ("f(x) = {x², x≤1; 2x−1, x>1}. Continuous at x=1?", ["*Yes (left=1, right=1, f(1)=1)", "No", "Jump", "Removable"],
         "All equal to 1."),
        ("f(x) = {(x²−4)/(x−2), x≠2; k, x=2}. For continuity, k = ?", ["2", "0", "*4", "Undefined"],
         "lim = (x+2) at 2 = 4. Set k = 4."),
        ("Signum function sgn(x) = {1,x>0; 0,x=0; −1,x<0}. Continuous at 0?", ["Yes", "*No (left = −1, right = 1)", "Only from right", "Only from left"],
         "Jump discontinuity."),
        ("f(x) = {sin(πx)/x, x≠0; π, x=0}. Continuous at 0?", ["No", "*Yes (lim = π = f(0))", "Removable", "Jump"],
         "lim_{x→0} sin(πx)/x = π · lim sin(πx)/(πx) = π·1 = π = f(0)."),
        ("The greatest integer function ⌊x⌋ is continuous at x = 2.5?", ["*Yes (no formula change within (2,3))", "No", "Jump", "Removable"],
         "⌊x⌋ = 2 for all x in [2,3). Constant → continuous within."),
        ("A piecewise function can have at most ___ discontinuities per boundary:", ["0", "*1", "2", "Infinite"],
         "Each boundary point can create at most one discontinuity."),
        ("To sketch a piecewise function, sketch each piece on its:", ["Entire domain", "*Specified interval, noting open/closed endpoints", "Only at boundary", "Same formula"],
         "Each piece applies only on its interval; mark endpoints accordingly.")
    ]
)
lessons[k] = v

# ── 9.8 AP Calculus Prep ──────────────────────────────────────────
k, v = build_lesson(9, 8,
    "AP Calculus Prep",
    "<h3>AP Calculus Prep: Limits &amp; Continuity</h3>"
    "<p>Limits and continuity form the foundation of AP Calculus AB/BC. Mastery of these precalculus skills is essential.</p>"
    "<h4>AP-Essential Skills</h4>"
    "<ul>"
    "<li>Evaluate limits (direct substitution, factoring, rationalizing, squeeze theorem).</li>"
    "<li>Analyze one-sided limits and determine when the two-sided limit exists.</li>"
    "<li>Classify discontinuities (removable, jump, infinite).</li>"
    "<li>Apply the Intermediate Value Theorem.</li>"
    "<li>Know that continuity implies integrability and is needed for the Mean Value Theorem.</li>"
    "<li>Understand lim sin x/x = 1 and lim (1−cos x)/x = 0.</li>"
    "</ul>",
    [
        ("Indeterminate Form 0/0", "Requires algebraic manipulation (factoring, rationalizing) before the limit can be evaluated."),
        ("IVT Application", "If f continuous on [a,b] with f(a) and f(b) of opposite sign, then f has a zero in (a,b)."),
        ("Squeeze Theorem", "If g ≤ f ≤ h and lim g = lim h = L, then lim f = L."),
        ("Continuity Implies Integrability", "Continuous functions on [a,b] are Riemann integrable — used in the Fundamental Theorem of Calculus."),
        ("Mean Value Theorem Preview", "If f continuous on [a,b] and differentiable on (a,b), then f'(c) = [f(b)−f(a)]/(b−a) for some c.")
    ],
    [
        ("lim_{x→2} (x²−4)/(x−2) = ?", ["0", "2", "*4", "Undefined"],
         "Factor: (x+2)(x−2)/(x−2) → x+2 → 4."),
        ("lim_{x→0} sin(5x)/(3x) = ?", ["0", "1", "3/5", "*5/3"],
         "(5/3)·[sin(5x)/(5x)] → 5/3."),
        ("lim_{x→∞} (2x²+3)/(5x²−1) = ?", ["∞", "0", "*2/5", "5/2"],
         "Same degree: 2/5."),
        ("f(x) = (x−1)/(x²−1) at x=1:", ["Infinite", "*Removable (limit = 1/2)", "Jump", "Continuous"],
         "= 1/((x+1)) for x≠1. Limit = 1/2."),
        ("lim_{x→0⁺} x ln x = ?", ["−∞", "∞", "*0", "1"],
         "L'Hôpital or analysis: x ln x → 0."),
        ("lim_{x→0} (1 − cos x)/x² = ?", ["0", "1", "*1/2", "∞"],
         "Standard limit (often shown via Taylor: cos x ≈ 1 − x²/2)."),
        ("IVT: f(x) = x³ − 4x + 1. f(0) = 1, f(1) = −2. Conclusion?", ["No root", "*Root exists in (0, 1)", "Root at x = 0.5", "f is not continuous"],
         "f continuous, f(0)>0, f(1)<0 → zero in (0,1) by IVT."),
        ("lim_{x→3} (√(x+1) − 2)/(x − 3) = ?", ["0", "2", "*1/4", "Undefined"],
         "Rationalize: multiply by (√(x+1)+2)/(√(x+1)+2). = (x+1−4)/((x−3)(√(x+1)+2)) = 1/(√(x+1)+2). At 3: 1/4."),
        ("lim_{x→∞} sin x:", ["1", "0", "*Does not exist (oscillates)", "∞"],
         "sin x oscillates between −1 and 1 forever."),
        ("Classify: f(x) = tan x at x = π/2:", ["Removable", "Jump", "*Infinite", "Continuous"],
         "tan x → ±∞ at π/2."),
        ("If lim_{x→c} f(x) = f(c), then f is ___ at c.", ["Differentiable", "*Continuous", "Bounded", "Integrable"],
         "Definition of continuity at a point."),
        ("The squeeze theorem requires:", ["Only f between g and h", "*g ≤ f ≤ h AND lim g = lim h = L", "f = g = h", "lim f = lim g"],
         "Both bounding functions must have the same limit."),
        ("lim_{x→4} (x − 4)/(√x − 2) = ?", ["0", "2", "*4", "Undefined"],
         "Rationalize: (x−4)(√x+2)/((√x−2)(√x+2)) = (x−4)(√x+2)/(x−4) = √x+2. At 4: 4."),
        ("For AP Calc, which limit is fundamental?", ["lim x/sin x = π", "*lim sin x/x = 1 as x→0", "lim sin x = 0 as x→∞", "lim cos x/x = 1"],
         "lim_{x→0} sin x/x = 1 is used extensively."),
        ("A function continuous on [a,b] must have:", ["A maximum only", "A minimum only", "*Both a maximum and minimum (Extreme Value Theorem)", "Neither"],
         "EVT guarantees both extreme values on a closed interval."),
        ("lim_{x→0} (e^x − 1)/x = ?", ["0", "*1", "e", "∞"],
         "Fundamental limit. (e^x = 1 + x + x²/2 + … → (e^x−1)/x → 1.)"),
        ("The Mean Value Theorem requires f to be:", ["Only differentiable", "*Continuous on [a,b] and differentiable on (a,b)", "Continuous everywhere", "Polynomial"],
         "Both conditions are needed."),
        ("lim_{h→0} [(3+h)² − 9]/h = ?", ["9", "3", "*6", "0"],
         "(9+6h+h²−9)/h = 6+h → 6. (This is f'(3) for f(x)=x².)"),
        ("AP multiple choice: lim_{x→2} (x³−8)/(x−2) = ?", ["8", "6", "*12", "4"],
         "Factor: (x−2)(x²+2x+4)/(x−2) = x²+2x+4. At 2: 12."),
        ("Mastering limits is essential because:", ["They're only used in precalculus", "They're optional in calculus", "*Derivatives and integrals are both defined as limits", "They're easy"],
         "Calculus = limits applied to rates (derivatives) and accumulation (integrals).")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 9)")
