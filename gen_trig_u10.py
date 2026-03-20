#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 10: Advanced Topics & Review (6 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "trigonometry_lessons.json")
COURSE = "Trigonometry"

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

# ── 10.1 Trigonometric Proofs ──
k, v = build_lesson(10, 1, "Trigonometric Proofs & Verification",
    "<h3>Trigonometric Proofs &amp; Verification</h3>"
    "<p>Proving trig identities means showing the LHS equals the RHS through algebraic manipulation.</p>"
    "<h4>Strategies</h4>"
    "<ul><li>Work on one side only (usually the more complex one).</li>"
    "<li>Convert everything to sin and cos.</li>"
    "<li>Factor, combine fractions, or multiply by a conjugate.</li>"
    "<li>Use fundamental identities: Pythagorean, reciprocal, quotient.</li></ul>",
    [
        ("Identity vs. Equation", "An identity is true for ALL valid θ; an equation may be true only for specific θ."),
        ("Strategy: One Side", "Transform one side to match the other; never move terms across the equals sign."),
        ("Convert to sin/cos", "Replace tan, sec, csc, cot with sin θ and cos θ expressions."),
        ("Multiply by Conjugate", "Multiply numerator & denominator by (1 + sinθ) or (1 − cosθ) to simplify."),
        ("Factor", "Look for Pythagorean patterns, common factors, or difference of squares."),
    ],
    [
        ("In a trig proof, you should work on:", ["Both sides simultaneously", "*One side at a time", "Neither side", "Only the RHS"],
         "Transform one side to match the other."),
        ("The first step to prove tan θ cot θ = 1 is:", ["Square both sides", "*Rewrite: (sinθ/cosθ)(cosθ/sinθ) = 1 ✓", "Add 1", "Cross multiply"],
         "Convert to sin/cos and simplify."),
        ("To prove (1 − sin²θ) = cos²θ, use:", ["Sum formula", "*Pythagorean identity: sin²θ + cos²θ = 1", "Half-angle", "Product formula"],
         "Direct rearrangement of the Pythagorean identity."),
        ("Prove sin²θ(1 + cot²θ) = 1. The key identity is:", ["*1 + cot²θ = csc²θ, so sin²θ · csc²θ = sin²θ · (1/sin²θ) = 1", "sin2θ = 2sinθcosθ", "cos2θ formula", "tanθ = sinθ/cosθ"],
         "Use the Pythagorean identity for csc."),
        ("When you see 1 − cos²θ, think:", ["tanθ", "*sin²θ", "cos²θ", "1"],
         "Pythagorean rearrangement."),
        ("When you see sec²θ − 1, think:", ["sin²θ", "cos²θ", "*tan²θ", "1"],
         "sec²θ = 1 + tan²θ → sec²θ − 1 = tan²θ."),
        ("To simplify (1/(1−sinθ)) + (1/(1+sinθ)):", ["*Common denominator: (1+sinθ + 1−sinθ)/((1−sinθ)(1+sinθ)) = 2/cos²θ = 2sec²θ", "1", "2", "Cannot simplify"],
         "Combine fractions, use difference of squares."),
        ("Proving tan²θ + 1 = sec²θ is an example of:", ["An equation to solve", "*Verifying a fundamental identity", "A linear equation", "An inequality"],
         "It's the Pythagorean identity for tangent/secant."),
        ("Working on the more complex side is preferred because:", ["It's a rule", "*It's easier to simplify than to complicate", "You must", "Convention"],
         "Simplifying is generally more straightforward."),
        ("Never do this in a proof:", ["Factor", "Convert to sin/cos", "*Move terms from one side to the other (cross the equals)", "Multiply by conjugate"],
         "Treat the two sides independently; don't assume they're equal to manipulate."),
        ("Prove: cosθ/(1−sinθ) = (1+sinθ)/cosθ. Multiply LHS by (1+sinθ)/(1+sinθ):", ["Can't do this", "*cosθ(1+sinθ)/(1−sin²θ) = cosθ(1+sinθ)/cos²θ = (1+sinθ)/cosθ ✓", "It becomes 0", "cosθsinθ"],
         "Multiply by conjugate of the denominator."),
        ("The conjugate of (1 − sinθ) is:", ["(1 − sinθ)", "*(1 + sinθ)", "(sinθ − 1)", "cosθ"],
         "Change the sign of the trig term."),
        ("Factoring sin²θ − cos²θ:", ["Cannot factor", "*(sinθ − cosθ)(sinθ + cosθ)", "sin(θ−θ)", "−cos2θ only"],
         "Difference of squares pattern."),
        ("sin²θ − cos²θ = −cos(2θ) is another form of:", ["*The double angle identity cos2θ = cos²θ − sin²θ (negated)", "Nothing", "tanθ = sinθ/cosθ", "Pythagorean"],
         "cos2θ = cos²θ − sin²θ → −cos2θ = sin²θ − cos²θ."),
        ("To prove cscθ − sinθ = cosθ cotθ, start with LHS:", ["Add cotθ", "*1/sinθ − sinθ = (1−sin²θ)/sinθ = cos²θ/sinθ = cosθ · (cosθ/sinθ) = cosθ cotθ ✓", "Multiply by cosθ", "Cannot prove"],
         "Common denominator, then Pythagorean, then simplify."),
        ("The biggest challenge in trig proofs is:", ["Computation", "*Knowing which identity or technique to apply", "Finding θ", "Using a calculator"],
         "Strategy selection is the key skill."),
        ("If stuck, try converting everything to:", ["Tangent", "Secant", "*Sine and cosine", "Numbers"],
         "Sin/cos is the most fundamental form — everything simplifies from there."),
        ("Proofs appear on the AP exam as:", ["Never", "*Free-response identity verification problems", "Only multiple choice", "Only Calc AB"],
         "Standard AP precalc/trig topic."),
        ("After completing a proof, always:", ["Erase it", "*Read through to check each step is valid", "Start over", "Assume it's correct"],
         "Verify each algebraic manipulation."),
        ("Practice is the best way to master proofs because:", ["Memorization alone works", "*Recognition of patterns improves with experience", "There's only one type", "No shortcuts exist"],
         "Exposure to many proofs builds pattern recognition."),
    ]
)
lessons[k] = v

# ── 10.2 Trigonometric Substitution (Calculus Preview) ──
k, v = build_lesson(10, 2, "Trigonometric Substitution",
    "<h3>Trigonometric Substitution (Calculus Preview)</h3>"
    "<p>In calculus, trig substitution simplifies integrals involving √(a²−x²), √(a²+x²), or √(x²−a²).</p>"
    "<h4>The Three Cases</h4>"
    "<ul><li><b>√(a²−x²):</b> let x = a sinθ → √(a²−x²) = a cosθ.</li>"
    "<li><b>√(a²+x²):</b> let x = a tanθ → √(a²+x²) = a secθ.</li>"
    "<li><b>√(x²−a²):</b> let x = a secθ → √(x²−a²) = a tanθ.</li></ul>",
    [
        ("Trig Substitution", "Replacing x with a trig expression to eliminate a radical."),
        ("√(a²−x²)", "Use x = a sinθ; the radical becomes a cosθ."),
        ("√(a²+x²)", "Use x = a tanθ; the radical becomes a secθ."),
        ("√(x²−a²)", "Use x = a secθ; the radical becomes a tanθ."),
        ("Reference Triangle", "After substituting, draw a right triangle to convert back to x."),
    ],
    [
        ("To simplify √(9−x²), let:", ["x = 3 tanθ", "*x = 3 sinθ → √(9−9sin²θ) = 3cosθ", "x = 3 secθ", "x = 3 cosθ"],
         "Pattern √(a²−x²): use x = a sinθ."),
        ("With x = 3sinθ, dx =", ["3sinθ dθ", "*3cosθ dθ", "−3sinθ dθ", "3secθ dθ"],
         "dx = 3cosθ dθ."),
        ("To simplify √(x²+4), let:", ["x = 2 sinθ", "*x = 2 tanθ → √(4tan²θ+4) = 2secθ", "x = 2 cosθ", "x = 2 secθ"],
         "Pattern √(a²+x²): use x = a tanθ."),
        ("To simplify √(x²−16), let:", ["x = 4 sinθ", "x = 4 tanθ", "*x = 4 secθ → √(16sec²θ−16) = 4tanθ", "x = 16"],
         "Pattern √(x²−a²): use x = a secθ."),
        ("After trig substitution, the integral is in terms of:", ["x", "*θ (which you later convert back to x)", "Both x and θ", "Nothing"],
         "You integrate in θ, then use inverses to convert back."),
        ("Why does x = asinθ work for √(a²−x²)?", ["Random choice", "*Because a²−a²sin²θ = a²cos²θ and √(a²cos²θ) = a|cosθ|", "It doesn't work", "Just convention"],
         "Pythagorean identity eliminates the square root."),
        ("The reference triangle for x = 3sinθ has:", ["Hypotenuse x", "*Hypotenuse 3, opposite side x, adjacent side √(9−x²)", "No useful properties", "All sides equal to 3"],
         "sinθ = x/3 → opposite = x, hyp = 3, adj = √(9−x²)."),
        ("After integration and converting back to x, the answer is in terms of:", ["Only θ", "*x (using arcsin, arctan, or arcsec)", "Only trig functions", "Nothing useful"],
         "Use the triangle to convert all trig functions back to x expressions."),
        ("Trig substitution is a key technique in:", ["Algebra 1", "Geometry", "*AP Calculus BC", "Statistics"],
         "Standard integration technique in calculus."),
        ("Without trig substitution, integrals like ∫√(1−x²) dx are:", ["Easy", "*Very difficult to evaluate", "Impossible in all cases", "Trivial"],
         "Trig sub is often the only practical method."),
        ("∫√(1−x²) dx with x = sinθ becomes:", ["∫cosθ dθ", "*∫cos²θ dθ (since √(1−sin²θ) · cosθ dθ = cos²θ dθ)", "∫sinθ dθ", "∫θ dθ"],
         "The radical becomes cosθ, and dx = cosθ dθ."),
        ("∫cos²θ dθ can be evaluated using:", ["Nothing", "*The power-reduction formula: cos²θ = (1+cos2θ)/2", "Substitution again", "Integration by parts"],
         "Half-angle/power-reduction identity."),
        ("The result ∫cos²θ dθ = θ/2 + sin(2θ)/4 + C converts back using:", ["x = cosθ", "*θ = arcsin(x), and sin(2θ) = 2sinθcosθ = 2x√(1−x²)", "Nothing", "Tables only"],
         "Reference triangle gives all conversions."),
        ("Trig substitution works because trig identities:", ["Are random", "*Transform radical expressions into polynomial/trig expressions", "Don't help", "Only apply to angles"],
         "Pythagorean identities are the key."),
        ("This topic connects trig to calculus by showing:", ["They're unrelated", "*Trig identities are powerful tools for advanced math", "Trig is only for triangles", "Calculus doesn't use trig"],
         "Trig is deeply embedded in calculus techniques."),
        ("In physics, ∫√(a²−x²) dx arises in:", ["Cooking", "*Calculating arc lengths, work, and areas of circles/ellipses", "Only abstract math", "Not in physics"],
         "Many physical quantities involve such integrals."),
        ("The three substitutions cover all forms of:", ["Linear expressions", "*Quadratic expressions under square roots (after completing the square)", "Cubic expressions", "Quartic expressions"],
         "Any ax² + bx + c under a radical can be reduced to one of the three forms."),
        ("Before trig substitution, you may need to:", ["Factor", "*Complete the square to put the expression in standard form", "Simplify", "Nothing"],
         "E.g., √(−x² + 6x − 5) = √(4 − (x−3)²) → let x−3 = 2sinθ."),
        ("Trig substitution is one of three main integration techniques, along with:", ["Nothing", "*Integration by parts and partial fractions", "Only u-substitution", "Matrices"],
         "Core calculus integration toolkit."),
        ("Mastering trig identities in this course prepares you for:", ["Nothing beyond trig", "*Success in calculus, physics, and engineering math", "Only the AP exam", "Only proofs"],
         "Trig mastery is essential for all STEM fields."),
    ]
)
lessons[k] = v

# ── 10.3 Parametric Equations ──
k, v = build_lesson(10, 3, "Parametric Equations",
    "<h3>Parametric Equations</h3>"
    "<p>Instead of y = f(x), a curve is defined by <b>x = f(t), y = g(t)</b> with parameter t.</p>"
    "<h4>Key Skills</h4>"
    "<ul><li><b>Graphing:</b> Make a table of t → (x, y) and plot.</li>"
    "<li><b>Eliminating the parameter:</b> Express t in terms of x (or y) and substitute.</li>"
    "<li><b>Direction:</b> As t increases, trace the orientation of the curve.</li></ul>"
    "<h4>Examples</h4>"
    "<p>x = cosθ, y = sinθ → unit circle. x = t², y = t → parabola x = y².</p>",
    [
        ("Parametric Equations", "x = f(t), y = g(t); the curve is traced as t varies."),
        ("Eliminating the Parameter", "Solve one equation for t and substitute into the other."),
        ("Orientation", "The direction the curve is traced as t increases."),
        ("Parametric Circle", "x = r cosθ, y = r sinθ traces a circle of radius r."),
        ("Parametric Line", "x = x₀ + at, y = y₀ + bt traces a line through (x₀, y₀) with direction ⟨a, b⟩."),
    ],
    [
        ("In parametric form, a curve is defined by:", ["y = f(x)", "*x = f(t), y = g(t)", "r = f(θ)", "y = mx + b"],
         "Separate functions for x and y in terms of t."),
        ("x = 2t, y = t + 1. At t = 0:", ["(2, 0)", "*(0, 1)", "(0, 0)", "(2, 1)"],
         "x = 0, y = 1."),
        ("Same curve at t = 1:", ["(1, 2)", "*(2, 2)", "(3, 3)", "(1, 1)"],
         "x = 2, y = 2."),
        ("Eliminate t from x = 2t, y = t + 1:", ["y = 2x + 1", "*t = x/2 → y = x/2 + 1", "x = y − 1", "y = x²/4 + 1"],
         "t = x/2, substitute: y = x/2 + 1 (a line)."),
        ("x = cosθ, y = sinθ traces:", ["A line", "*A unit circle (CCW as θ increases)", "A parabola", "An ellipse"],
         "cos²θ + sin²θ = 1."),
        ("x = 3cosθ, y = 2sinθ traces:", ["A circle", "*An ellipse with semi-axes 3 (x) and 2 (y)", "A parabola", "A hyperbola"],
         "(x/3)² + (y/2)² = 1."),
        ("x = t², y = t. Eliminate t:", ["y = x²", "*x = y² (parabola opening right)", "x = y", "y = √x"],
         "t = y → x = y²."),
        ("x = 2 + 3t, y = 1 − t is a:", ["Circle", "*Line", "Parabola", "Ellipse"],
         "Parametric line through (2, 1) with direction ⟨3, −1⟩."),
        ("The orientation of x = cosθ, y = sinθ is:", ["Clockwise", "*Counter-clockwise", "Stationary", "Alternating"],
         "Standard trig convention: CCW as θ increases."),
        ("x = cos(−θ), y = sin(−θ) traces the same circle but:", ["CCW", "*Clockwise", "No difference", "Not a circle"],
         "Parametrizing with −θ reverses the direction."),
        ("Different parametrizations can trace:", ["Only different curves", "*The same curve with different orientations or speeds", "Nothing in common", "Only lines"],
         "How you parametrize affects direction and speed, not the shape."),
        ("x = t, y = t² for t ∈ [−2, 2] traces part of:", ["A circle", "*A parabola y = x²", "A line", "An ellipse"],
         "Eliminate t: y = x², x ∈ [−2, 2]."),
        ("Cycloid: x = t − sin t, y = 1 − cos t. At t = 0:", ["*(0, 0)", "(1, 1)", "(π, 2)", "(−1, 0)"],
         "x = 0 − 0 = 0, y = 1 − 1 = 0."),
        ("At t = π for the cycloid:", ["(0, 0)", "*(π, 2)", "(2π, 0)", "(π, 0)"],
         "x = π − 0 = π, y = 1 − (−1) = 2."),
        ("Parametric equations are useful for:", ["Only math class", "*Modeling motion (position at time t), animation, and physics", "Nothing practical", "Only circles"],
         "Time-dependent paths are natural in parametric form."),
        ("A projectile: x = v₀cosα · t, y = v₀sinα · t − ½gt². This is parametric because:", ["It has no parameter", "*Position depends on time t", "It's a standard equation", "It's polar"],
         "Both x and y are functions of t."),
        ("To find the Cartesian equation from parametric, you:", ["*Eliminate the parameter t (or θ)", "Add x and y", "Differentiate", "Integrate"],
         "Express the relationship directly between x and y."),
        ("Not all parametric curves have a single Cartesian equation because:", ["They always do", "*Some curves cross themselves or have complex shapes", "Math limitation", "No reason"],
         "Self-intersecting curves can't be represented as y = f(x)."),
        ("On the AP exam, you may be asked to:", ["Only graph", "*Convert parametric ↔ Cartesian, find tangent lines (dy/dx = y'/x'), and compute arc length", "Only eliminate t", "None of these"],
         "Conversion, tangents, and arc length are key AP topics."),
        ("Parametric equations bridge trig and calculus by:", ["Being unrelated", "*Providing a framework for motion, curves, and vector-valued functions", "Replacing trig", "Replacing calculus"],
         "Parametric → vector-valued → multivariable calculus."),
    ]
)
lessons[k] = v

# ── 10.4 Applications in Calculus ──
k, v = build_lesson(10, 4, "Calculus Connections & Applications",
    "<h3>Calculus Connections</h3>"
    "<h4>Derivatives of Trig Functions</h4>"
    "<ul><li>d/dx sin x = cos x</li>"
    "<li>d/dx cos x = −sin x</li>"
    "<li>d/dx tan x = sec²x</li></ul>"
    "<h4>Limits Involving Trig</h4>"
    "<p>lim (sin x)/x = 1 as x → 0 (fundamental limit).</p>"
    "<h4>Integration</h4>"
    "<p>∫sin x dx = −cos x + C, ∫cos x dx = sin x + C. Trig identities simplify complex integrals.</p>",
    [
        ("d/dx sin x = cos x", "The derivative of sine is cosine."),
        ("d/dx cos x = −sin x", "The derivative of cosine is negative sine."),
        ("lim sin(x)/x = 1", "Fundamental trigonometric limit (x in radians, x → 0)."),
        ("∫sin x dx = −cos x + C", "Antiderivative of sine."),
        ("Power-Reduction Formulas", "Used to integrate sin²x or cos²x: cos²x = (1+cos2x)/2."),
    ],
    [
        ("The derivative of sin x:", ["sin x", "*cos x", "−cos x", "−sin x"],
         "d/dx sin x = cos x."),
        ("The derivative of cos x:", ["cos x", "sin x", "*−sin x", "−cos x"],
         "d/dx cos x = −sin x."),
        ("The derivative of tan x:", ["cot x", "−cot x", "*sec²x", "csc²x"],
         "d/dx tan x = sec²x."),
        ("lim(x→0) sin(x)/x =", ["0", "*1", "∞", "Undefined"],
         "Fundamental trig limit, x in radians."),
        ("lim(x→0) (1 − cos x)/x =", ["1", "*0", "∞", "1/2"],
         "Standard limit; can be derived from the sine limit."),
        ("∫sin x dx =", ["cos x + C", "*−cos x + C", "sin x + C", "−sin x + C"],
         "The antiderivative of sin x is −cos x."),
        ("∫cos x dx =", ["−cos x + C", "cos x + C", "*sin x + C", "−sin x + C"],
         "The antiderivative of cos x is sin x."),
        ("∫sec²x dx =", ["sec x + C", "*tan x + C", "−tan x + C", "sin x + C"],
         "Since d/dx tan x = sec²x."),
        ("The fundamental limit lim sin(x)/x = 1 requires x in:", ["Degrees", "*Radians", "Either", "Neither"],
         "Radians are essential for this limit."),
        ("To integrate sin²x, use the identity:", ["sin²x = sinx · sinx", "*sin²x = (1 − cos 2x)/2", "sin²x = 1 − cos²x only", "No identity needed"],
         "Power-reduction formula makes it integrable."),
        ("∫sin²x dx = ∫(1 − cos2x)/2 dx =", ["sin x + C", "*x/2 − sin(2x)/4 + C", "cos x + C", "−x/2 + sin(2x)/4 + C"],
         "Integrate term by term."),
        ("d/dx sec x =", ["sec x", "*sec x tan x", "csc x cot x", "−csc x cot x"],
         "d/dx sec x = sec x tan x."),
        ("d/dx csc x =", ["csc x cot x", "*−csc x cot x", "sec x tan x", "csc²x"],
         "d/dx csc x = −csc x cot x."),
        ("The chain rule: d/dx sin(3x) =", ["sin(3x)", "*3cos(3x)", "cos(3x)", "3sin(3x)"],
         "d/dx sin(u) = cos(u) · u' = cos(3x) · 3."),
        ("d/dx cos(x²) =", ["−sin(x²)", "*−2x sin(x²)", "2x cos(x²)", "sin(x²)"],
         "Chain rule: −sin(x²) · 2x."),
        ("In physics, the derivative of position sin(ωt) is:", ["sin(ωt)", "*ω cos(ωt) (velocity)", "−sin(ωt)", "ω² sin(ωt)"],
         "Chain rule: ω cos(ωt)."),
        ("The second derivative of sin(ωt) is:", ["ω cos(ωt)", "*−ω² sin(ωt) (acceleration)", "sin(ωt)", "ω² cos(ωt)"],
         "d²/dt² sin(ωt) = −ω² sin(ωt). This is SHM!"),
        ("−ω² sin(ωt) = −ω² · x(t) shows that SHM satisfies:", ["x' = 0", "*x'' = −ω²x (the defining differential equation of SHM)", "x = constant", "x' = x"],
         "Trig functions naturally satisfy the SHM equation."),
        ("Trig identities in calculus are used for:", ["*Simplifying integrals, solving differential equations, and evaluating limits", "Only proofs", "Only in high school", "Nothing"],
         "Essential calculus toolkit."),
        ("Mastering trig prepares you for calculus because:", ["It doesn't", "*Derivatives, integrals, and differential equations all heavily involve trig", "Only for the AP exam", "Only for proofs"],
         "Trig is everywhere in calculus."),
    ]
)
lessons[k] = v

# ── 10.5 AP Review & Practice ──
k, v = build_lesson(10, 5, "AP Exam Review & Practice",
    "<h3>AP Exam Review &amp; Practice</h3>"
    "<p>This lesson consolidates all major topics from the course for AP-style exam preparation.</p>"
    "<h4>Key Topics to Review</h4>"
    "<ul><li>Unit circle values and reference angles</li>"
    "<li>Graphing sinusoidal functions (amplitude, period, phase, midline)</li>"
    "<li>Identities (Pythagorean, double-angle, sum/difference)</li>"
    "<li>Solving trig equations (including general solutions)</li>"
    "<li>Laws of Sines/Cosines and area</li>"
    "<li>Polar/rectangular conversion</li>"
    "<li>Vectors (dot/cross product, projections)</li></ul>",
    [
        ("Unit Circle Mastery", "Know exact values at 0°, 30°, 45°, 60°, 90° and all quadrants."),
        ("Graph Transformations", "y = A sin(Bx − C) + D: identify amplitude |A|, period 2π/B, phase C/B, midline D."),
        ("Identity Toolkit", "Pythagorean, reciprocal, quotient, double-angle, sum/difference, power-reduction."),
        ("Solving Strategy", "Isolate trig function → inverse → quadrant analysis → general solution if needed."),
        ("Cross-Topic Problems", "AP problems often combine multiple concepts in one question."),
    ],
    [
        ("sin(π/6) =", ["√3/2", "*1/2", "√2/2", "0"],
         "30° reference: sin 30° = 1/2."),
        ("cos(5π/4) =", ["√2/2", "*−√2/2", "−1/2", "1/2"],
         "Q III, reference 45°: cos = −√2/2."),
        ("tan(2π/3) =", ["√3", "*−√3", "1", "−1"],
         "Q II, reference 60°: tan = −√3."),
        ("Period of y = 3sin(2x − π) + 1:", ["2π", "*π (2π/2 = π)", "4π", "π/2"],
         "B = 2, period = 2π/B = π."),
        ("Phase shift of same function:", ["π", "−π", "*π/2 (to the right)", "−π/2"],
         "Phase shift = C/B = π/2."),
        ("cos(A+B) =", ["cosAcosB + sinAsinB", "*cosAcosB − sinAsinB", "sinAcosB + cosAsinB", "sinAcosB − cosAsinB"],
         "Cosine sum formula."),
        ("sin(2θ) =", ["sin²θ − cos²θ", "*2sinθcosθ", "2cos²θ − 1", "1 − 2sin²θ"],
         "Double-angle sine formula."),
        ("Solve 2sinθcosθ = cosθ in [0, 2π):", ["cosθ = 0 only", "*cosθ(2sinθ−1) = 0 → θ = π/2, 3π/2, π/6, 5π/6", "sinθ = 1/2 only", "θ = 0"],
         "Factor out cosθ."),
        ("Law of Cosines: c² = a² + b² − 2ab cos C. If a=5, b=8, C=60°:", ["c=3", "*c²=25+64−2(40)(0.5)=89−40=49 → c=7", "c=13", "c=√89"],
         "Compute step by step."),
        ("Area = ½(5)(8)sin60° =", ["20", "*½(40)(√3/2) = 10√3 ≈ 17.32", "40", "20√3"],
         "½ab sinC."),
        ("Convert (−3, 3) to polar:", ["(3, π/4)", "*(3√2, 3π/4)", "(3√2, π/4)", "(3, 3π/4)"],
         "r = √(9+9) = 3√2, Q II → θ = π − π/4 = 3π/4."),
        ("r = 4cosθ in rectangular:", ["x² + y² = 4x", "*x² + y² = 4x → (x−2)² + y² = 4", "x = 4", "r = 4"],
         "Multiply by r: r² = 4rcosθ → x²+y² = 4x."),
        ("⟨3, −1⟩ · ⟨2, 6⟩ =", ["12", "*0 (perpendicular!)", "−12", "6"],
         "6 + (−6) = 0."),
        ("|⟨5, 12⟩| =", ["17", "*13", "7", "60"],
         "√(25+144) = √169 = 13."),
        ("The projection of v = ⟨4, 3⟩ onto u = ⟨2, 0⟩:", ["⟨4, 3⟩", "*⟨4, 0⟩", "⟨2, 0⟩", "⟨0, 3⟩"],
         "proj = (v·u/|u|²)u = (8/4)⟨2,0⟩ = ⟨4, 0⟩."),
        ("General solution of cosθ = −1:", ["θ = 2nπ", "*θ = π + 2nπ", "θ = nπ", "θ = nπ/2"],
         "cos = −1 only at π, repeating every 2π."),
        ("De Moivre: [2cis30°]³ =", ["6cis30°", "*8cis90° = 8i", "2cis90°", "8cis30°"],
         "2³ = 8, 3×30° = 90°."),
        ("The ambiguous case arises from:", ["SAS", "AAS", "*SSA", "SSS"],
         "Only SSA can give 0, 1, or 2 solutions."),
        ("On the AP exam, the most important skill is:", ["Memorization", "*Understanding when and why to apply each formula/identity", "Speed", "Calculator use"],
         "Conceptual understanding trumps memorization."),
        ("Time management tip: if stuck for over 3 minutes, you should:", ["Keep trying indefinitely", "*Mark it and move on; return later if time permits", "Leave it blank", "Panic"],
         "Strategic skipping preserves time for other problems."),
    ]
)
lessons[k] = v

# ── 10.6 Capstone Project ──
k, v = build_lesson(10, 6, "Capstone: Comprehensive Review",
    "<h3>Capstone: Comprehensive Review</h3>"
    "<p>This final lesson ties together all major themes of the Trigonometry course.</p>"
    "<h4>Course Summary</h4>"
    "<ul><li><b>Foundations:</b> Angles, unit circle, trig functions & their graphs.</li>"
    "<li><b>Identities:</b> Fundamental, double-angle, sum/difference, inverse.</li>"
    "<li><b>Equations:</b> Solving linear/quadratic/multiple-angle trig equations.</li>"
    "<li><b>Applications:</b> Oblique triangles (Laws of Sines/Cosines), area, navigation.</li>"
    "<li><b>Advanced:</b> Polar coordinates, complex numbers, vectors, parametric equations.</li></ul>",
    [
        ("Unit Circle", "The foundation: exact values of sin, cos, tan at key angles."),
        ("Trig Identities", "Pythagorean, reciprocal, quotient, double-angle, sum/difference — the algebraic toolkit."),
        ("Solving Trig Equations", "Isolate, use inverses, analyze quadrants, give general solutions."),
        ("Laws of Sines/Cosines", "Solve any triangle: AAS/ASA/SSA use Law of Sines; SAS/SSS use Law of Cosines."),
        ("Vectors & Complex Numbers", "Dot/cross products, polar form, De Moivre's Theorem, parametric equations."),
    ],
    [
        ("The unit circle has radius:", ["2", "π", "*1", "0"],
         "By definition, radius = 1."),
        ("sin²θ + cos²θ =", ["0", "*1", "2", "sin θ"],
         "The fundamental Pythagorean identity."),
        ("tan θ =", ["cosθ/sinθ", "*sinθ/cosθ", "1/cosθ", "1/sinθ"],
         "Definition of tangent."),
        ("The period of sin(x):", ["π", "*2π", "4π", "1"],
         "Sine repeats every 2π."),
        ("The period of tan(x):", ["2π", "*π", "π/2", "4π"],
         "Tangent repeats every π."),
        ("cos(A − B) =", ["cosAcosB − sinAsinB", "*cosAcosB + sinAsinB", "sinAcosB − cosAsinB", "2cosAcosB"],
         "Cosine difference: plus sign."),
        ("sin(2θ) = 2sinθcosθ is the:", ["*Double-angle formula for sine", "Sum formula", "Pythagorean identity", "Reciprocal identity"],
         "Key double-angle identity."),
        ("Solve sinθ = √2/2 in [0, 2π):", ["π/4 only", "*π/4, 3π/4", "π/4, 5π/4", "π/3, 2π/3"],
         "Q I: π/4, Q II: 3π/4."),
        ("Law of Sines: a/sinA = b/sinB. Used when:", ["SSS", "SAS", "*AAS, ASA, SSA", "Only right triangles"],
         "When you have angle-side pairs."),
        ("Law of Cosines: c² = a²+b²−2abcosC. Used when:", ["AAS", "*SAS or SSS", "Only SSA", "Only ASA"],
         "Must have the included angle (SAS) or all sides (SSS)."),
        ("Area = ½absinC requires:", ["Three sides", "*Two sides and their included angle", "Three angles", "One side"],
         "SAS data."),
        ("x = rcosθ, y = rsinθ converts:", ["Cartesian → polar", "*Polar → Cartesian", "Degrees → radians", "Neither"],
         "Polar to rectangular conversion."),
        ("|z| for z = 3+4i:", ["7", "*5", "12", "1"],
         "√(9+16) = 5."),
        ("De Moivre's: [rcisθ]ⁿ =", ["rⁿcisθ", "rcis(nθ)", "*rⁿcis(nθ)", "nrcisθ"],
         "Raise modulus to n, multiply argument by n."),
        ("The dot product u·v = 0 implies:", ["u ∥ v", "*u ⊥ v", "u = v", "|u| = 0"],
         "Zero dot product = perpendicular."),
        ("|u × v| equals:", ["u · v", "*|u||v|sinθ (parallelogram area)", "|u||v|cosθ", "|u| + |v|"],
         "Cross product magnitude = area."),
        ("Parametric equations define a curve using:", ["y = f(x)", "*x = f(t), y = g(t) with parameter t", "r = f(θ)", "Only coordinates"],
         "Both x and y depend on parameter t."),
        ("The general solution of sinθ = k has the form:", ["θ = arcsin(k) only", "*θ = arcsin(k) + 2nπ or θ = π − arcsin(k) + 2nπ", "θ = k + nπ", "θ = arcsin(k) + nπ"],
         "Two families of solutions with period 2π."),
        ("Trigonometry connects to calculus through:", ["Nothing", "Only limits", "*Derivatives, integrals, parametric curves, polar curves, and trig substitution", "Only the AP exam"],
         "Trig is deeply embedded in calculus."),
        ("The most important takeaway from this course:", ["Memorize everything", "*Understanding WHY identities and formulas work enables flexible problem-solving", "Trig is useless", "Only calculators matter"],
         "Conceptual mastery enables application to new situations."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 10: wrote {len(lessons)} lessons")
