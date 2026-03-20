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

# ── 10.1 Derivative as Slope of Tangent Line ──────────────────────
k, v = build_lesson(10, 1,
    "Derivative as Slope of Tangent Line",
    "<h3>Derivative as Slope of Tangent Line</h3>"
    "<p>The <b>derivative</b> of f at x = a is defined as the limit of the difference quotient:</p>"
    "<ul>"
    "<li>f'(a) = lim_{h→0} [f(a+h) − f(a)] / h</li>"
    "</ul>"
    "<h4>Geometric Interpretation</h4>"
    "<ul>"
    "<li>f'(a) = slope of the <b>tangent line</b> to y = f(x) at x = a.</li>"
    "<li>The tangent line is the best linear approximation of f near x = a.</li>"
    "<li>Equation: y − f(a) = f'(a)(x − a).</li>"
    "</ul>",
    [
        ("Derivative Definition", "f'(a) = lim_{h→0} [f(a+h)−f(a)]/h; the instantaneous rate of change at a."),
        ("Tangent Line", "A line touching the curve at one point with slope equal to the derivative."),
        ("Tangent Line Equation", "y − f(a) = f'(a)(x − a); point-slope form using the derivative."),
        ("Secant to Tangent", "As h → 0, the secant line through two nearby points becomes the tangent line."),
        ("Differentiable", "A function is differentiable at a if f'(a) exists (the limit exists).")
    ],
    [
        ("f(x) = x². f'(x) using the limit definition:", ["x", "x²", "*2x", "2"],
         "lim_{h→0} [(x+h)²−x²]/h = lim (2x+h) = 2x."),
        ("f'(3) for f(x) = x²:", ["3", "9", "*6", "12"],
         "f'(x) = 2x → f'(3) = 6."),
        ("Tangent line to y = x² at (3, 9):", ["y = 3x", "*y = 6x − 9", "y = 6x + 9", "y = 9x − 18"],
         "y − 9 = 6(x − 3) → y = 6x − 9."),
        ("f(x) = 5x + 2. f'(x) = ?", ["5x", "2", "*5", "7"],
         "Linear function: derivative = slope = 5."),
        ("f(x) = 7 (constant). f'(x) = ?", ["7", "1", "*0", "Undefined"],
         "Derivative of a constant is 0."),
        ("f(x) = x³. Using limit: f'(x) = ?", ["x²", "x³", "*3x²", "3x"],
         "[(x+h)³−x³]/h → 3x²."),
        ("Where is f(x) = |x| NOT differentiable?", ["Everywhere", "*At x = 0 (corner)", "At x = 1", "Nowhere"],
         "Sharp corner at 0; left derivative = −1, right = 1."),
        ("If f'(a) > 0, the tangent line at a:", ["Is horizontal", "*Slopes upward (positive slope)", "Slopes downward", "Is vertical"],
         "Positive derivative → positive slope."),
        ("If f'(a) = 0, the tangent line is:", ["Vertical", "Undefined", "*Horizontal", "Diagonal"],
         "Zero slope = horizontal."),
        ("Tangent line gives the best ___ approximation near a:", ["Quadratic", "Exponential", "*Linear", "Logarithmic"],
         "Tangent line = linear approximation."),
        ("f(x) = √x. f'(x) = ?", ["√x", "1/x", "*1/(2√x)", "2√x"],
         "lim [(√(x+h)−√x)/h] = 1/(2√x)."),
        ("f'(4) for f(x) = √x:", ["2", "1/2", "*1/4", "4"],
         "1/(2·2) = 1/4."),
        ("Tangent to y = √x at (4, 2):", ["y = x/2", "*y = (1/4)x + 1", "y = x/4 + 2", "y = 2x − 6"],
         "y − 2 = (1/4)(x − 4) → y = x/4 + 1."),
        ("f(x) = 1/x. f'(x) = ?", ["1/x²", "*−1/x²", "−1/x", "x"],
         "lim [1/(x+h)−1/x]/h = −1/x²."),
        ("f'(2) for f(x) = 1/x:", ["1/2", "−1/2", "1/4", "*−1/4"],
         "−1/4."),
        ("Which function is NOT differentiable at x = 0?", ["x²", "x³", "*|x|", "sin x"],
         "|x| has a corner at 0."),
        ("Differentiability implies:", ["Nothing about continuity", "*Continuity", "Discontinuity", "f(x) = 0"],
         "If f is differentiable at a, then f is continuous at a."),
        ("Continuity implies differentiability:", ["Always", "*Not necessarily (e.g., |x| at 0)", "Never", "Only for polynomials"],
         "Continuous but not differentiable at corners, cusps."),
        ("The derivative tells us:", ["The y-value", "*The rate of change/slope at a point", "The x-intercept", "The area"],
         "Derivative = instantaneous rate of change."),
        ("Normal line at a point is ___ to the tangent:", ["Parallel", "*Perpendicular", "Equal", "Tangential"],
         "Normal line has slope = −1/f'(a).")
    ]
)
lessons[k] = v

# ── 10.2 Derivative Rules (power rule basics) ─────────────────────
k, v = build_lesson(10, 2,
    "Derivative Rules (power rule basics)",
    "<h3>Derivative Rules</h3>"
    "<h4>Basic Rules</h4>"
    "<ul>"
    "<li><b>Constant Rule:</b> d/dx[c] = 0</li>"
    "<li><b>Power Rule:</b> d/dx[xⁿ] = nxⁿ⁻¹</li>"
    "<li><b>Constant Multiple:</b> d/dx[cf(x)] = c · f'(x)</li>"
    "<li><b>Sum/Difference:</b> d/dx[f ± g] = f' ± g'</li>"
    "</ul>"
    "<h4>Common Derivatives</h4>"
    "<ul>"
    "<li>d/dx[sin x] = cos x, d/dx[cos x] = −sin x</li>"
    "<li>d/dx[eˣ] = eˣ, d/dx[ln x] = 1/x</li>"
    "</ul>",
    [
        ("Power Rule", "d/dx[xⁿ] = nxⁿ⁻¹; bring down the exponent, subtract 1."),
        ("Constant Rule", "d/dx[c] = 0; the derivative of any constant is zero."),
        ("Sum Rule", "d/dx[f + g] = f' + g'; differentiate term by term."),
        ("Constant Multiple Rule", "d/dx[cf(x)] = c·f'(x); constants factor out."),
        ("Derivative of eˣ", "d/dx[eˣ] = eˣ; the exponential function is its own derivative.")
    ],
    [
        ("d/dx[x⁵] = ?", ["x⁴", "5x⁵", "*5x⁴", "x⁵/5"],
         "Power rule: 5x⁴."),
        ("d/dx[x] = ?", ["x", "0", "*1", "1/2"],
         "x¹ → 1·x⁰ = 1."),
        ("d/dx[x⁰] = d/dx[1] = ?", ["1", "x⁻¹", "*0", "Undefined"],
         "Constant → 0."),
        ("d/dx[3x⁴] = ?", ["3x³", "4x³", "*12x³", "12x⁴"],
         "3·4x³ = 12x³."),
        ("d/dx[x² + 5x − 3] = ?", ["x² + 5", "2x + 5x", "*2x + 5", "2x − 3"],
         "Term by term: 2x + 5 + 0."),
        ("d/dx[x⁻¹] = ?", ["x⁻²", "*−x⁻²", "−1", "1/x"],
         "−1·x⁻² = −1/x²."),
        ("d/dx[√x] = d/dx[x^(1/2)] = ?", ["x^(1/2)", "*x^(−1/2)/2 = 1/(2√x)", "2√x", "√x/2"],
         "(1/2)x^(−1/2)."),
        ("d/dx[x³ − 2x² + 7x] = ?", ["3x² − 2x + 7", "x² − 4x + 7", "*3x² − 4x + 7", "3x² − 4x"],
         "3x² − 4x + 7."),
        ("d/dx[sin x] = ?", ["sin x", "−sin x", "*cos x", "−cos x"],
         "Derivative of sine is cosine."),
        ("d/dx[cos x] = ?", ["cos x", "*−sin x", "sin x", "−cos x"],
         "Derivative of cosine is negative sine."),
        ("d/dx[eˣ] = ?", ["xeˣ⁻¹", "e", "*eˣ", "eˣ/x"],
         "eˣ is its own derivative."),
        ("d/dx[ln x] = ?", ["ln x", "x", "*1/x", "eˣ"],
         "Derivative of natural log is 1/x."),
        ("d/dx[4eˣ + 3sin x] = ?", ["4eˣ + 3cos x", "4eˣ − 3sin x", "*4eˣ + 3cos x", "4x + 3cos x"],
         "4eˣ + 3cos x."),
        ("d/dx[x^(−2)] = ?", ["2x⁻³", "*−2x⁻³", "−2x⁻¹", "x⁻³"],
         "−2x⁻³ = −2/x³."),
        ("d/dx[x² − π] = ?", ["2x − π", "*2x", "2x − 1", "x²"],
         "π is a constant → derivative is 0. Answer: 2x."),
        ("Rewrite 1/x³ before differentiating:", ["x³", "*x⁻³", "x^(1/3)", "3x⁻¹"],
         "1/x³ = x⁻³. Then d/dx = −3x⁻⁴."),
        ("d/dx[x⁴/4] = ?", ["x⁴", "x³/4", "*x³", "4x³"],
         "(1/4)·4x³ = x³."),
        ("d/dx[2x³ − 6x + 1] at x = 1:", ["6", "0", "*0", "−4"],
         "f'(x) = 6x² − 6. f'(1) = 6 − 6 = 0."),
        ("The power rule works for:", ["Only positive integer exponents", "*Any real exponent n", "Only n ≥ 1", "Only integers"],
         "d/dx[xⁿ] = nxⁿ⁻¹ for any real n."),
        ("d/dx[x^(2/3)] = ?", ["(2/3)x^(2/3)", "*（2/3)x^(−1/3)", "(3/2)x^(1/3)", "x^(−1/3)"],
         "(2/3)x^(2/3 − 1) = (2/3)x^(−1/3).")
    ]
)
lessons[k] = v

# ── 10.3 Applications in Optimization ─────────────────────────────
k, v = build_lesson(10, 3,
    "Applications in Optimization",
    "<h3>Optimization with Derivatives</h3>"
    "<p>Derivatives help find <b>maximum</b> and <b>minimum</b> values of functions.</p>"
    "<h4>Process</h4>"
    "<ul>"
    "<li>1. Find f'(x) and set f'(x) = 0 to find <b>critical points</b>.</li>"
    "<li>2. Use the <b>first derivative test</b> (sign changes) or <b>second derivative test</b> (f''(x) > 0 for min, < 0 for max).</li>"
    "<li>3. On a closed interval, also check endpoints.</li>"
    "</ul>"
    "<h4>Real-World Optimization</h4>"
    "<ul>"
    "<li>Maximize profit/area/volume or minimize cost/distance.</li>"
    "<li>Write a function for the quantity to optimize, set its derivative to zero.</li>"
    "</ul>",
    [
        ("Critical Point", "A point where f'(x) = 0 or f'(x) is undefined; candidates for extrema."),
        ("First Derivative Test", "If f' changes from + to − at c, local max. From − to +, local min."),
        ("Second Derivative Test", "If f'(c)=0 and f''(c)>0, local min. If f''(c)<0, local max."),
        ("Optimization Process", "1) Model the problem. 2) Find f'. 3) Set f'=0. 4) Check endpoints if closed interval."),
        ("Closed Interval Method", "On [a,b]: evaluate f at critical points and endpoints, compare values.")
    ],
    [
        ("f(x) = x² − 6x + 5. f'(x) = 0 when x = ?", ["5", "6", "*3", "1"],
         "f'(x) = 2x − 6 = 0 → x = 3."),
        ("Is x = 3 a max or min for the above?", ["Max", "*Min (f''=2 > 0)", "Neither", "Saddle"],
         "f''(x) = 2 > 0 → concave up → min."),
        ("f(3) = ?", ["5", "0", "*−4", "3"],
         "9 − 18 + 5 = −4."),
        ("f(x) = −x² + 4x + 1. Critical point at x = ?", ["4", "1", "*2", "0"],
         "f'(x) = −2x + 4 = 0 → x = 2."),
        ("Max or min at x = 2?", ["Min", "*Max (f'' = −2 < 0)", "Neither", "Inflection"],
         "f'' = −2 < 0 → concave down → max."),
        ("f(2) = ?", ["1", "4", "*5", "9"],
         "−4 + 8 + 1 = 5."),
        ("Maximize the area of a rectangle with perimeter 20:", ["25", "20", "*25 (square: 5 × 5)", "100"],
         "A = x(10−x). A'= 10−2x = 0 → x = 5. A = 25."),
        ("Critical points of f(x) = x³ − 3x:", ["x = 0 only", "*x = −1 and x = 1", "x = 3", "x = ±√3"],
         "f' = 3x² − 3 = 0 → x² = 1 → x = ±1."),
        ("Classify x = −1 for f(x) = x³ − 3x:", ["Min", "*Local max (f''(−1)=−6 < 0)", "Neither", "Inflection"],
         "f'' = 6x. f''(−1) = −6 < 0 → local max."),
        ("Classify x = 1:", ["Max", "*Local min (f''(1)=6 > 0)", "Neither", "Inflection"],
         "f''(1) = 6 > 0 → local min."),
        ("On [0, 4], f(x) = x³ − 3x. Check f(0), f(1), f(−1 not in [0,4]), f(4):", ["*f(0)=0, f(1)=−2, f(4)=52. Max=52, Min=−2", "Max=0, Min=−2", "Max=52, Min=0", "Max=4, Min=0"],
         "Closed interval: check endpoints + critical points in [0,4]."),
        ("A farmer has 200 ft of fence. Maximize area with one side along a wall.", ["*2500 ft² (50 × 50 → wait: three sides. A=x(200−2x). Max at x=50, A=50·100=5000)", "5000 ft²", "10000 ft²", "2500 ft²"],
         "Three sides of fencing: A = x(200−2x). A' = 200−4x=0 → x=50. A=5000 ft²."),
        ("Revenue R(x) = 100x − x². Maximum revenue:", ["100", "50", "*2500", "10000"],
         "R'=100−2x=0 → x=50. R(50)=5000−2500=2500."),
        ("f(x) = x⁴ − 4x³. f'(x) = 4x³ − 12x² = 4x²(x − 3). Critical points:", ["x = 3 only", "*x = 0 and x = 3", "x = 0 only", "x = −3 and 3"],
         "f' = 0 at x = 0 and x = 3."),
        ("At x = 0, f' doesn't change sign (0→0→negative). So x = 0 is:", ["Max", "Min", "*Neither (inflection)", "Saddle"],
         "f' = 4x²(x−3): negative on both sides of 0 (for small |x| with x ≠ 0 near 0, x−3 < 0). Sign: no change → neither."),
        ("At x = 3: f' goes from negative to positive → ?", ["Max", "*Local min", "Neither", "Inflection"],
         "Sign change − to + → local min."),
        ("Volume of open-top box from 12×12 sheet, cutting squares of side x:", ["*V = x(12−2x)², maximize V'=0", "V = 12x²", "V = x³", "V = 144x"],
         "V = x(12−2x)². Find V' and set = 0."),
        ("In optimization problems, always check:", ["Only critical points", "Only endpoints", "*Both critical points and endpoints (if domain is closed)", "Nothing"],
         "Extreme values can occur at either."),
        ("If f''(c) = 0, the second derivative test:", ["Says min", "Says max", "*Is inconclusive", "Says inflection"],
         "Must use another method (like first derivative test)."),
        ("The absolute maximum of f on [a,b] is:", ["Always at a critical point", "*The largest value among f(a), f(b), and f at critical points", "Always at an endpoint", "At x where f' is largest"],
         "Compare all candidates.")
    ]
)
lessons[k] = v

# ── 10.4 Area Under Curves (intro to integration) ─────────────────
k, v = build_lesson(10, 4,
    "Area Under Curves (intro to integration)",
    "<h3>Area Under Curves</h3>"
    "<p>The area under a curve y = f(x) from x = a to x = b is found using integration.</p>"
    "<h4>Riemann Sums</h4>"
    "<ul>"
    "<li>Divide [a, b] into n subintervals of width Δx = (b−a)/n.</li>"
    "<li>Approximate area: Σ f(x_i) · Δx.</li>"
    "<li>As n → ∞, the Riemann sum → definite integral ∫ₐᵇ f(x) dx.</li>"
    "</ul>"
    "<h4>Key Idea</h4>"
    "<ul>"
    "<li>Integration is the 'reverse' of differentiation.</li>"
    "<li>The Fundamental Theorem of Calculus connects derivatives and integrals.</li>"
    "</ul>",
    [
        ("Riemann Sum", "Approximation of area using rectangles: Σ f(xᵢ)Δx."),
        ("Definite Integral", "∫ₐᵇ f(x) dx = lim_{n→∞} Σ f(xᵢ)Δx; exact area under curve."),
        ("Fundamental Theorem of Calculus", "If F is an antiderivative of f, then ∫ₐᵇ f(x)dx = F(b) − F(a)."),
        ("Antiderivative", "A function F such that F'(x) = f(x)."),
        ("Left/Right Riemann Sums", "Use left or right endpoints of subintervals to evaluate f.")
    ],
    [
        ("Area under f(x) = 2 from x=0 to x=5:", ["2", "5", "*10", "7"],
         "Rectangle: 2 × 5 = 10. Or ∫₀⁵ 2 dx = 2(5) = 10."),
        ("Δx for [0, 4] with n = 4 subintervals:", ["4", "2", "*1", "0.5"],
         "(4−0)/4 = 1."),
        ("Left Riemann sum of f(x) = x on [0, 4], n = 4:", ["10", "16", "*6", "8"],
         "f(0)·1 + f(1)·1 + f(2)·1 + f(3)·1 = 0+1+2+3 = 6."),
        ("Right Riemann sum for the same:", ["6", "*10", "8", "16"],
         "f(1)+f(2)+f(3)+f(4) = 1+2+3+4 = 10."),
        ("Exact area under f(x) = x from 0 to 4:", ["6", "10", "*8", "16"],
         "∫₀⁴ x dx = x²/2 |₀⁴ = 8. (Triangle: (1/2)(4)(4) = 8.)"),
        ("Antiderivative of x²:", ["2x", "x²/3", "*x³/3 + C", "3x²"],
         "d/dx[x³/3] = x²."),
        ("∫₀² x² dx = ?", ["4", "2", "*8/3", "4/3"],
         "[x³/3]₀² = 8/3 − 0 = 8/3."),
        ("Antiderivative of cos x:", ["−sin x", "*sin x + C", "cos x + C", "−cos x"],
         "d/dx[sin x] = cos x."),
        ("∫₀^π sin x dx = ?", ["0", "1", "*2", "π"],
         "[−cos x]₀^π = −cos π − (−cos 0) = 1 + 1 = 2."),
        ("As n increases, Riemann sum becomes:", ["Less accurate", "Zero", "*More accurate (approaches the integral)", "Larger"],
         "More rectangles → better approximation."),
        ("The integral ∫ₐᵇ f(x) dx represents:", ["The derivative", "*The net signed area under f from a to b", "The average value", "The maximum"],
         "Area above x-axis counts positive, below counts negative."),
        ("∫₁³ 2x dx = ?", ["6", "4", "*8", "12"],
         "[x²]₁³ = 9 − 1 = 8."),
        ("Antiderivative of 1/x:", ["x", "*ln|x| + C", "−1/x²", "eˣ"],
         "d/dx[ln|x|] = 1/x."),
        ("Antiderivative of eˣ:", ["xeˣ", "*eˣ + C", "eˣ/x", "ln x"],
         "eˣ is its own antiderivative."),
        ("∫₀¹ 3x² dx = ?", ["3", "3/2", "*1", "2"],
         "[x³]₀¹ = 1 − 0 = 1."),
        ("If F'(x) = f(x), then ∫ₐᵇ f(x) dx = ?", ["F'(b) − F'(a)", "*F(b) − F(a)", "F(a) − F(b)", "F(b) + F(a)"],
         "Fundamental Theorem of Calculus."),
        ("Area under f(x) = x from 0 to 3 (triangle):", ["3", "9", "*4.5", "6"],
         "(1/2)(3)(3) = 4.5."),
        ("Midpoint Riemann sum uses:", ["Left endpoints", "Right endpoints", "*Midpoints of subintervals", "Random points"],
         "Evaluate f at the center of each subinterval."),
        ("∫₂² f(x) dx = ?", ["f(2)", "Undefined", "*0", "2"],
         "Integral with same upper and lower limit = 0."),
        ("Integration is sometimes called:", ["Differentiation", "Optimization", "*Anti-differentiation", "Simplification"],
         "Finding antiderivatives = anti-differentiation.")
    ]
)
lessons[k] = v

# ── 10.5 Connecting Precalculus to Calculus ────────────────────────
k, v = build_lesson(10, 5,
    "Connecting Precalculus to Calculus",
    "<h3>Connecting Precalculus to Calculus</h3>"
    "<p>Every major precalculus topic directly supports calculus concepts.</p>"
    "<h4>Connections</h4>"
    "<ul>"
    "<li><b>Functions & graphs:</b> Needed for reading and interpreting derivative/integral graphs.</li>"
    "<li><b>Polynomial/rational functions:</b> Easiest functions for differentiation and integration.</li>"
    "<li><b>Trigonometry:</b> Trig functions and identities are used constantly in calculus.</li>"
    "<li><b>Exponentials & logs:</b> Model growth/decay; have elegant derivatives.</li>"
    "<li><b>Limits:</b> Define derivatives and integrals.</li>"
    "<li><b>Sequences & series:</b> Lead to Taylor series, the backbone of approximation.</li>"
    "</ul>",
    [
        ("Functions → Calculus", "All calculus operations (diff, integration) are applied to functions."),
        ("Trig → Calculus", "d/dx[sin x]=cos x, ∫sin x dx = −cos x; identities simplify expressions."),
        ("Exp/Log → Calculus", "d/dx[eˣ]=eˣ, d/dx[ln x]=1/x; model growth and decay."),
        ("Limits → Derivatives", "f'(a) = lim_{h→0}[f(a+h)−f(a)]/h; limits define the derivative."),
        ("Series → Taylor Series", "Approximating functions as infinite polynomials uses sequences and series skills.")
    ],
    [
        ("The derivative is defined using:", ["Algebra only", "Geometry only", "*Limits", "Series"],
         "f'(x) = lim of difference quotient."),
        ("Which precalculus topic is needed for ∫sin²x dx?", ["Sequences", "Polynomial division", "*Trig identities (power-reducing)", "Logarithms"],
         "sin²x = (1 − cos 2x)/2."),
        ("Polynomial long division helps in calculus when:", ["Never", "*The integrand is an improper rational function", "Only for derivatives", "Only for graphing"],
         "Divide before integrating if degree numerator ≥ degree denominator."),
        ("Exponential growth model: dP/dt = kP. Solution uses:", ["Trig", "Polynomials", "*Exponential functions (P = P₀eᵏᵗ)", "Sequences"],
         "Separable ODE → exponential solution."),
        ("Taylor series for eˣ:", ["1 + x", "*1 + x + x²/2! + x³/3! + …", "eˣ = x + 1", "x + x²"],
         "Infinite polynomial approximation requiring series knowledge."),
        ("Factoring is used in calculus for:", ["Nothing", "*Simplifying limits and partial fractions", "Only in precalculus", "Graphing only"],
         "Factoring is needed for limit evaluation and partial fraction decomposition."),
        ("Domain restrictions in precalculus become important in calculus for:", ["Nothing", "Only graphing", "*Determining where derivatives/integrals exist", "Style"],
         "Functions must be defined and continuous for most calculus operations."),
        ("Composition of functions leads to which calculus rule?", ["Power rule", "*Chain rule", "Sum rule", "Product rule"],
         "d/dx[f(g(x))] = f'(g(x))·g'(x)."),
        ("Inverses of functions lead to:", ["Nothing in calculus", "*Derivative of inverse functions and integration techniques", "Only graphing", "Only algebra"],
         "d/dx[f⁻¹(x)] = 1/f'(f⁻¹(x))."),
        ("Asymptotic behavior (limits at ∞) connects to:", ["Only precalculus", "*End behavior analysis and convergence of improper integrals", "Nothing", "Only graphing"],
         "lim_{x→∞} f(x) determines convergence of ∫ₐ^∞ f(x) dx."),
        ("Why learn trig identities?", ["For fun", "*They're essential for simplifying calculus expressions", "They're not needed", "Only for geometry"],
         "Used in integration (trig substitution, simplification) and solving differential equations."),
        ("Sequences lead to:", ["Only statistics", "*Series, Taylor approximations, numerical methods", "Only algebra", "Graphing"],
         "Sequences → series → Taylor series, a cornerstone of advanced calculus."),
        ("The unit circle is important in calculus because:", ["It's decorative", "*Quick recall of trig values speeds up derivative/integral evaluation", "It's only for precalc", "It defines π"],
         "Fast trig evaluation is critical for efficiency in calculus."),
        ("Logarithmic differentiation uses:", ["Only power rule", "*Properties of logarithms", "Trig only", "Sequences"],
         "Take ln of both sides, use log properties, then differentiate."),
        ("Rational functions require ___ for integration.", ["Trig only", "Guessing", "*Partial fraction decomposition", "Nothing special"],
         "Break into simpler fractions, then integrate each."),
        ("Graphing skills help in calculus because:", ["Calculus doesn't use graphs", "*Interpreting derivative and integral graphs is essential", "Only for precalculus", "Graphs are optional"],
         "Graphical interpretation is a major part of AP Calculus."),
        ("The binomial theorem extends to:", ["Only integer n", "*Newton's generalized binomial series (any real exponent)", "Only positive n", "Nothing in calculus"],
         "(1+x)^α = Σ C(α,k)x^k for any real α (|x|<1)."),
        ("Systems of equations arise in calculus when:", ["Never", "*Finding Taylor coefficients, partial fractions, etc.", "Only in linear algebra", "Only in precalculus"],
         "Setting up and solving systems is needed in many calculus techniques."),
        ("Overall, precalculus provides:", ["Everything for calculus", "Nothing useful", "*The function toolkit and algebraic skills calculus builds upon", "Only graphing skills"],
         "Precalculus = the foundation; calculus = the structure built on it."),
        ("The best way to prepare for AP Calculus:", ["Memorize formulas", "Skip precalculus", "*Master precalculus concepts deeply — especially limits, trig, and function analysis", "Only practice integrals"],
         "Strong precalculus skills make calculus significantly easier.")
    ]
)
lessons[k] = v

# ── 10.6 AP-Style Practice Problems ───────────────────────────────
k, v = build_lesson(10, 6,
    "AP-Style Practice Problems",
    "<h3>AP-Style Practice Problems</h3>"
    "<p>These problems mirror the format and difficulty of AP Calculus AB free-response and multiple-choice questions, drawing on precalculus skills.</p>"
    "<h4>Focus Areas</h4>"
    "<ul>"
    "<li>Limits and continuity</li>"
    "<li>Derivatives and rates of change</li>"
    "<li>Function analysis (increasing/decreasing, concavity)</li>"
    "<li>Trig and exponential functions</li>"
    "</ul>",
    [
        ("AP Calculus Format", "Multiple choice (45 questions, 105 min) + Free response (6 questions, 90 min)."),
        ("Calculator vs Non-Calculator", "Some sections allow graphing calculators; others require algebraic/analytic methods."),
        ("Justify Your Answer", "AP free response requires written justification; 'because f'(x) changes sign' type reasoning."),
        ("Read Graphs Carefully", "Many AP questions give graphs of f, f', or f'' and ask about the others."),
        ("Units and Context", "AP often gives real-world context; answers should include appropriate units.")
    ],
    [
        ("lim_{x→3} (x²−9)/(x−3) = ?", ["0", "3", "*6", "9"],
         "(x−3)(x+3)/(x−3) = x+3 → 6."),
        ("lim_{x→0} sin(4x)/(2x) = ?", ["4", "1/2", "*2", "0"],
         "(4/2)·sin(4x)/(4x) → 2."),
        ("f(x)=x³−3x²+2. Find all x where f'(x)=0.", ["x=0 only", "x=2 only", "*x=0 and x=2", "x=1"],
         "f'=3x²−6x=3x(x−2)=0 → x=0, 2."),
        ("At x=0, f''(0)=−6<0 → ?", ["Min", "*Local max", "Neither", "Inflection"],
         "f''<0 → concave down → local max."),
        ("At x=2, f''(2)=6>0 → ?", ["Max", "*Local min", "Neither", "Inflection"],
         "f''> 0 → concave down up → local min."),
        ("f(x)=eˣ−x. Critical point at x=?", ["e", "1", "*0", "−1"],
         "f'=eˣ−1=0 → eˣ=1 → x=0."),
        ("Is x=0 a min or max for f(x)=eˣ−x?", ["Max", "*Min (f''=eˣ=1>0)", "Neither", "Inflection"],
         "f''(0)=e⁰=1>0 → local min."),
        ("∫₀¹ (3x² + 2x) dx = ?", ["2", "3", "*2", "5"],
         "[x³+x²]₀¹ = 1+1 = 2."),
        ("lim_{x→∞} (5x−3)/(2x+1) = ?", ["∞", "0", "*5/2", "3"],
         "Same degree: 5/2."),
        ("If f is continuous on [1,4] and f(1)=−3, f(4)=5, by IVT:", ["*f(c)=0 for some c in (1,4)", "f(c)=0 for no c", "f is constant", "f(2)=1"],
         "0 is between −3 and 5."),
        ("Tangent to y=x² at x=−1: slope?", ["1", "*−2", "2", "−1"],
         "f'(−1) = 2(−1) = −2."),
        ("Equation of the tangent:", ["y=−x+1", "*y=−2x−1", "y=−2x+1", "y=x−2"],
         "y−1=−2(x+1) → y=−2x−1."),
        ("f(x)=ln x. ∫₁ᵉ (1/x) dx = ?", ["0", "e", "*1", "1/e"],
         "[ln x]₁ᵉ = ln e − ln 1 = 1."),
        ("d/dx[x sin x] using product rule:", ["sin x + cos x", "*sin x + x cos x", "x cos x", "x sin x + cos x"],
         "(x)'sin x + x(sin x)' = sin x + x cos x."),
        ("f(x)=x⁴−4x². Inflection points where f''=0:", ["x=0", "*x=±√(2/3)", "x=±2", "x=±1"],
         "f''=12x²−8=0 → x²=2/3 → x=±√(2/3)."),
        ("A particle's position: s(t)=t³−6t². Velocity v(t)=s'(t)=:", ["t²−12t", "*3t²−12t", "3t−12", "t³−6t"],
         "s'(t) = 3t² − 12t."),
        ("When is the particle at rest?", ["t=0 only", "t=4 only", "*t=0 and t=4", "Never"],
         "v(t)=3t(t−4)=0 → t=0, 4."),
        ("Acceleration a(t)=v'(t)=6t−12=0 when t=?", ["0", "4", "*2", "6"],
         "6t−12=0 → t=2."),
        ("∫₀^(π/2) cos x dx = ?", ["0", "*1", "π/2", "−1"],
         "[sin x]₀^(π/2) = 1 − 0 = 1."),
        ("On AP exams, showing your work means:", ["Optional", "Writing the answer only", "*Showing mathematical steps and justifying claims", "Drawing graphs only"],
         "Full justification earns full credit on free response.")
    ]
)
lessons[k] = v

# ── 10.7 Capstone Project: Modeling with Functions ────────────────
k, v = build_lesson(10, 7,
    "Capstone Project: Modeling with Functions",
    "<h3>Capstone Project: Modeling with Functions</h3>"
    "<p>This capstone integrates all precalculus skills: building a mathematical model from data, analyzing it, and making predictions.</p>"
    "<h4>Modeling Process</h4>"
    "<ul>"
    "<li>1. <b>Collect/identify</b> real-world data or a scenario.</li>"
    "<li>2. <b>Choose</b> an appropriate function type (linear, quadratic, exponential, trig, logistic).</li>"
    "<li>3. <b>Fit</b> the model to data (regression or algebraic methods).</li>"
    "<li>4. <b>Analyze:</b> find key features (max, min, zeros, asymptotes, rates of change).</li>"
    "<li>5. <b>Predict</b> and validate: use the model for forecasting, check reasonableness.</li>"
    "</ul>",
    [
        ("Mathematical Model", "A function or equation that describes a real-world phenomenon."),
        ("Regression", "Statistical technique to find the best-fit curve for data (linear, quadratic, exponential, etc.)."),
        ("Model Selection", "Choose the function type based on data shape: linear (constant rate), quadratic (parabolic), exponential (growth/decay), trig (periodic)."),
        ("Residual Analysis", "Compare predicted vs actual values to assess model quality."),
        ("Extrapolation Warning", "Models may not be reliable far beyond the range of data used to build them.")
    ],
    [
        ("Data shows constant rate of change. Best model:", ["Quadratic", "Exponential", "*Linear", "Sinusoidal"],
         "Constant Δy/Δx → linear."),
        ("Data shows accelerating growth (constant ratio). Best model:", ["Linear", "*Exponential", "Quadratic", "Logarithmic"],
         "Constant ratio → geometric/exponential."),
        ("Data shows repeated cycles. Best model:", ["Exponential", "Linear", "Polynomial", "*Sinusoidal (trigonometric)"],
         "Periodic → sinusoidal."),
        ("Data rises then falls (parabolic shape). Best model:", ["Linear", "Exponential", "*Quadratic", "Logarithmic"],
         "Parabolic shape → quadratic."),
        ("Population that levels off (carrying capacity). Best model:", ["Exponential", "*Logistic", "Linear", "Quadratic"],
         "Logistic model: P = K/(1 + Ae⁻ᵏᵗ)."),
        ("First step in modeling:", ["Choose the function", "Graph the data", "*Understand the problem and collect data", "Find the derivative"],
         "Start with the real-world context and data."),
        ("R² = 0.98 means:", ["Bad fit", "*98% of variance explained — excellent fit", "The slope is 0.98", "The model is wrong"],
         "R² close to 1 → strong fit."),
        ("Residuals should ideally be:", ["All positive", "All negative", "*Randomly scattered around zero", "Increasing"],
         "Systematic patterns in residuals suggest a wrong model type."),
        ("Extrapolating far from data range is:", ["Always accurate", "*Risky and potentially unreliable", "Better than interpolation", "Required"],
         "Models are most reliable within the data range."),
        ("A linear model y = 2.5x + 10 predicts y(20) = ?", ["50", "52.5", "*60", "70"],
         "2.5(20) + 10 = 60."),
        ("Exponential model P = 100(1.05)ᵗ. P(10) ≈ ?", ["150", "*≈162.89", "200", "105"],
         "100(1.05)¹⁰ ≈ 162.89."),
        ("Doubling time for the model above:", ["10 years", "*≈14.2 years (72/5)", "20 years", "5 years"],
         "Rule of 72: 72/5 ≈ 14.2 years."),
        ("Trig model T = 15 sin(2π/365 · t) + 55. Max temperature:", ["55", "15", "*70", "40"],
         "Max when sin = 1: 15 + 55 = 70."),
        ("Min temperature for the model above:", ["55", "15", "0", "*40"],
         "Min when sin = −1: −15 + 55 = 40."),
        ("Quadratic model h = −16t² + 64t. When does object hit ground?", ["*t = 4 s", "t = 2 s", "t = 8 s", "t = 16 s"],
         "−16t(t−4) = 0 → t = 4."),
        ("Maximum height in the model above:", ["128 ft", "32 ft", "*64 ft", "256 ft"],
         "Vertex at t = 2: h(2) = −64 + 128 = 64 ft."),
        ("Logistic model levels off at:", ["0", "∞", "*The carrying capacity K", "The initial value"],
         "As t → ∞, P → K."),
        ("When choosing between models, use:", ["The simplest one always", "*R² value, residual patterns, and domain knowledge", "The most complex one", "Only the linear model"],
         "Balance fit quality with simplicity and context."),
        ("A model should be validated by:", ["Assuming it's correct", "*Comparing predictions to new data", "Ignoring outliers", "Making it more complex"],
         "Test predictions against data not used in fitting."),
        ("The capstone project demonstrates that precalculus is:", ["Purely theoretical", "Only for solving equations", "*A powerful toolkit for understanding and modeling the real world", "Unnecessary for STEM"],
         "Precalculus connects math to real-world applications.")
    ]
)
lessons[k] = v

# ── 10.8 Comprehensive Review & AP Exam Prep ──────────────────────
k, v = build_lesson(10, 8,
    "Comprehensive Review & AP Exam Prep",
    "<h3>Comprehensive Review &amp; AP Exam Prep</h3>"
    "<p>A final review covering all major precalculus topics needed for AP Calculus success.</p>"
    "<h4>Key Topics to Master</h4>"
    "<ul>"
    "<li>Function types: polynomial, rational, exponential, logarithmic, trigonometric</li>"
    "<li>Transformations, compositions, and inverses</li>"
    "<li>Limits, continuity, and asymptotic behavior</li>"
    "<li>Sequences, series, and the binomial theorem</li>"
    "<li>Trig identities and equations</li>"
    "<li>Derivatives and integrals (preview)</li>"
    "</ul>",
    [
        ("Polynomial Properties", "Continuous everywhere, smooth graphs, degree determines end behavior and max number of zeros."),
        ("Rational Function Analysis", "Find asymptotes, holes, intercepts; domain excludes zeros of denominator."),
        ("Exponential vs Logarithmic", "Exponential: rapid growth/decay. Logarithmic: its inverse. Both critical in calculus."),
        ("Trig Function Toolkit", "Unit circle values, identities, and solving equations — all used extensively in calculus."),
        ("Calculus Readiness", "Limits → derivatives → integrals. Strong precalculus skills make calculus manageable.")
    ],
    [
        ("Factor completely: x³ − 8 = ?", ["(x−2)³", "*(x−2)(x²+2x+4)", "(x−8)(x+1)", "(x−2)(x²−2x+4)"],
         "Difference of cubes: a³−b³ = (a−b)(a²+ab+b²)."),
        ("Simplify: (x²−1)/(x²−x) = ?", ["(x+1)/x", "*(x+1)/x", "x−1", "(x−1)/x"],
         "(x-1)(x+1) / (x(x-1)) = (x+1)/x."),
        ("Solve: 2^x = 32.", ["*x = 5", "x = 16", "x = 6", "x = 4"],
         "2⁵ = 32."),
        ("log₂ 64 = ?", ["4", "5", "*6", "8"],
         "2⁶ = 64."),
        ("sin²(π/4) + cos²(π/4) = ?", ["1/2", "√2", "*1", "0"],
         "Pythagorean identity: always 1."),
        ("Exact value of cos(5π/6):", ["√3/2", "1/2", "*−√3/2", "−1/2"],
         "5π/6 in Q II: cos = −cos(π/6) = −√3/2."),
        ("lim_{x→2} (x²−4)/(x−2) = ?", ["0", "2", "*4", "∞"],
         "Factor and cancel: x+2 → 4."),
        ("Solve: ln x = 3.", ["3", "*e³", "ln 3", "3e"],
         "x = e³."),
        ("Geometric series: 1 + 1/3 + 1/9 + … = ?", ["1", "*3/2", "∞", "1/3"],
         "S = 1/(1−1/3) = 3/2."),
        ("d/dx[x⁴ − 3x² + 2] = ?", ["4x³ − 6x + 2", "x³ − 6x", "*4x³ − 6x", "4x − 6"],
         "Power rule term by term."),
        ("Inverse of f(x) = 2x + 3:", ["2x − 3", "*f⁻¹(x) = (x−3)/2", "(x+3)/2", "3x + 2"],
         "y = 2x+3 → x = (y−3)/2."),
        ("Period of y = sin(3x):", ["3", "π", "*2π/3", "3π"],
         "Period = 2π/B = 2π/3."),
        ("C(8, 3) = ?", ["24", "*56", "336", "8"],
         "8!/(3!5!) = 56."),
        ("Horizontal asymptote of (3x+1)/(x−2):", ["x = 2", "*y = 3", "y = 1", "y = −2"],
         "Same degree: 3/1 = 3."),
        ("Sum of first 10 positive integers:", ["50", "*55", "100", "45"],
         "10(11)/2 = 55."),
        ("tan(π/4) = ?", ["0", "√3", "1/2", "*1"],
         "sin/cos = (√2/2)/(√2/2) = 1."),
        ("∫₀² 3x dx = ?", ["3", "*6", "12", "2"],
         "[3x²/2]₀² = 6."),
        ("Solve: 2sin x − 1 = 0, x ∈ [0, 2π).", ["π/6 only", "*π/6 and 5π/6", "π/3 and 2π/3", "No solution"],
         "sin x = 1/2 → π/6 and 5π/6."),
        ("f(x)=eˣ is always:", ["Negative", "Zero at x = 0", "*Positive", "Oscillating"],
         "eˣ > 0 for all real x."),
        ("Being well-prepared for AP Calculus means:", ["Knowing only limits", "Memorizing everything", "*Having fluent skills in all precalculus topics plus basic limit/derivative concepts", "Just doing practice tests"],
         "Broad, deep precalculus mastery is the strongest preparation for calculus success.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 10)")
