#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 8: Polar Coordinates & Complex Numbers (7 lessons)."""
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

# ── 8.1 Polar Coordinate System ──
k, v = build_lesson(8, 1, "The Polar Coordinate System",
    "<h3>The Polar Coordinate System</h3>"
    "<p>A point is represented as <b>(r, θ)</b> where r is the distance from the origin (pole) and θ is the angle from the positive x-axis (polar axis).</p>"
    "<h4>Key Facts</h4>"
    "<ul><li>Unlike Cartesian coordinates, polar representations are <b>not unique</b>: (r, θ) = (r, θ+2nπ) = (−r, θ+π).</li>"
    "<li>Negative r means the point is in the opposite direction.</li>"
    "<li>The origin has r = 0 for any θ.</li></ul>",
    [
        ("Pole", "The origin of the polar coordinate system."),
        ("Polar Axis", "The ray from the pole in the direction of the positive x-axis."),
        ("r (Radial Coordinate)", "The directed distance from the pole to the point."),
        ("θ (Angular Coordinate)", "The angle measured counter-clockwise from the polar axis."),
        ("Non-Uniqueness", "The same point has infinitely many polar representations: (r, θ+2nπ) and (−r, θ+π+2nπ)."),
    ],
    [
        ("In polar coordinates, a point is given as:", ["(x, y)", "*(r, θ)", "(θ, r)", "(d, h)"],
         "(r, θ): distance and angle."),
        ("The pole corresponds to:", ["(1, 0)", "*(0, θ) for any θ", "(0, 0) only", "(r, 0) for any r"],
         "At the origin, r = 0 regardless of θ."),
        ("The point (3, π/4) is at distance __ from the origin at angle __ from the polar axis:", ["3, 45°", "*3, π/4 (= 45°)", "π/4, 3", "45, 3"],
         "r = 3, θ = π/4 = 45°."),
        ("(−3, π/4) represents a point:", ["Same as (3, π/4)", "*At distance 3 in the direction opposite to π/4, equivalent to (3, 5π/4)", "At the origin", "Undefined"],
         "Negative r: go opposite → (3, π/4 + π) = (3, 5π/4)."),
        ("How many polar representations does a point have?", ["Exactly 1", "Exactly 2", "*Infinitely many", "None"],
         "Add 2nπ or flip sign and add π — infinite options."),
        ("(5, 0) in polar means:", ["x = 0, y = 5", "*The point (5, 0) in Cartesian (on the positive x-axis)", "The origin", "y-axis point"],
         "r = 5, θ = 0 → directly right of the origin."),
        ("(2, π) represents:", ["(2, 0) in Cartesian", "*The point (−2, 0) in Cartesian", "(0, 2)", "(0, −2)"],
         "r=2, θ=π → 2 units in the negative x direction."),
        ("(4, π/2) converts to Cartesian:", ["(4, 0)", "(0, −4)", "*(0, 4)", "(4, 4)"],
         "x = 4cos(π/2) = 0, y = 4sin(π/2) = 4."),
        ("The polar axis is typically:", ["The y-axis", "*The positive x-axis", "The negative x-axis", "Any direction"],
         "By convention, the polar axis aligns with the positive x-axis."),
        ("Angles in polar coordinates are positive when measured:", ["Clockwise", "*Counter-clockwise", "Along the x-axis", "It doesn't matter"],
         "Standard mathematical convention: CCW is positive."),
        ("(r, θ) = (r, θ + 2π) because:", ["Convention", "*Adding a full rotation returns to the same direction", "r changes", "θ is irrelevant"],
         "A full 2π rotation is the same direction."),
        ("Which is NOT a valid representation of (2, π/3)?", ["(2, π/3 + 2π)", "(−2, π/3 + π)", "*(2, −π/3) (different point unless r is negative)", "(2, π/3 + 4π)"],
         "(2, −π/3) is a different point: it's at angle −60°, not +60°."),
        ("The point (0, 5π) is:", ["On the x-axis at distance 5π", "*The origin (r = 0)", "Undefined", "(5π, 0)"],
         "r = 0 → always the origin."),
        ("Polar coordinates are especially useful for:", ["Linear functions", "*Curves with rotational symmetry (circles, spirals, roses)", "Only right triangles", "Cartesian grids"],
         "Symmetry about the pole is natural in polar form."),
        ("In polar graph paper, the concentric circles represent:", ["Angles", "*Constant r values (fixed distances)", "x-values", "y-values"],
         "Each circle is a set of points equidistant from the pole."),
        ("The rays from the pole represent:", ["Distances", "*Constant θ values (fixed directions)", "Parabolas", "Circles"],
         "Each ray is a fixed angle."),
        ("(3, 2π/3) is in which Cartesian quadrant?", ["I", "*II", "III", "IV"],
         "θ = 2π/3 = 120° → Quadrant II."),
        ("(−2, 0) in polar equals which Cartesian point?", ["(2, 0)", "*(−2, 0) — wait, that's (−2, 0) in Cartesian: x = −2cos0 = −2, y = −2sin0 = 0", "(0, −2)", "(2, π)"],
         "x = (−2)cos 0 = −2, y = (−2)sin 0 = 0. Also representable as (2, π)."),
        ("The relationship between polar and Cartesian is:", ["Unrelated", "*x = r cos θ, y = r sin θ", "x = r sin θ, y = r cos θ", "x = θ, y = r"],
         "Conversion formulas."),
        ("r² = x² + y² and tan θ = y/x connect:", ["Nothing", "*Polar and Cartesian coordinates", "Two polar systems", "Only angles"],
         "These are the inverse conversion formulas."),
    ]
)
lessons[k] = v

# ── 8.2 Graphing Polar Equations ──
k, v = build_lesson(8, 2, "Graphing Polar Equations",
    "<h3>Graphing Polar Equations</h3>"
    "<h4>Common Polar Curves</h4>"
    "<ul><li><b>Circle:</b> r = a (constant), r = a cos θ, r = a sin θ.</li>"
    "<li><b>Cardioid:</b> r = a ± a cos θ or r = a ± a sin θ.</li>"
    "<li><b>Limaçon:</b> r = a ± b cos θ (different a, b).</li>"
    "<li><b>Rose:</b> r = a cos(nθ) — n petals if n odd, 2n petals if n even.</li>"
    "<li><b>Spiral:</b> r = aθ (Archimedean).</li></ul>",
    [
        ("Cardioid", "Heart-shaped curve; r = a(1 ± cosθ) or r = a(1 ± sinθ)."),
        ("Rose Curve", "r = a cos(nθ); has n petals (n odd) or 2n petals (n even)."),
        ("Limaçon", "r = a + b cos θ; shape depends on ratio a/b (with/without inner loop)."),
        ("Archimedean Spiral", "r = aθ; distance from origin increases linearly with angle."),
        ("Symmetry Tests", "Replace θ → −θ (x-axis sym), θ → π−θ (y-axis sym), r → −r (origin sym)."),
    ],
    [
        ("r = 3 graphs as:", ["A line", "*A circle of radius 3 centered at the origin", "A spiral", "A rose"],
         "Constant r = circle."),
        ("r = 4 cos θ is a circle of diameter:", ["2", "*4", "8", "16"],
         "r = a cos θ is a circle of diameter |a|, tangent to the origin."),
        ("r = 4 cos θ has its center at:", ["Origin", "*(2, 0) in Cartesian", "(0, 2)", "(4, 0)"],
         "Center at (a/2, 0) = (2, 0)."),
        ("r = 2(1 + cos θ) is a:", ["Circle", "*Cardioid", "Rose", "Spiral"],
         "Form r = a(1 + cos θ) → cardioid."),
        ("A cardioid passes through the origin when:", ["Never", "*When cos θ = −1 (or sin θ = −1), i.e., r = 0", "Always", "θ = 0"],
         "At θ = π for the (1 + cos θ) form, r = 0."),
        ("r = cos(3θ) is a rose with how many petals?", ["6", "*3", "9", "12"],
         "n = 3 (odd) → 3 petals."),
        ("r = cos(4θ) is a rose with how many petals?", ["4", "*8", "16", "2"],
         "n = 4 (even) → 2n = 8 petals."),
        ("r = cos(2θ) has:", ["2 petals", "*4 petals", "8 petals", "1 petal"],
         "n = 2 (even) → 4 petals."),
        ("r = θ (for θ ≥ 0) graphs as:", ["A circle", "*An Archimedean spiral", "A line", "A rose"],
         "r increases with θ → spiral."),
        ("r = 1 + 2cos θ is a limaçon with:", ["No inner loop", "*An inner loop (since b > a: 2 > 1)", "A dimple", "It's a cardioid"],
         "When |b| > |a|, the limaçon has an inner loop."),
        ("r = 3 + 2cos θ is a limaçon:", ["With inner loop", "*Without inner loop (convex, since a > b)", "Cardioid", "Circle"],
         "a > b: convex limaçon (no loop)."),
        ("r = 2 + 2cos θ is:", ["A limaçon with loop", "*A cardioid (a = b)", "A circle", "A rose"],
         "When a = b, the limaçon becomes a cardioid."),
        ("To test for x-axis symmetry:", ["Replace r with −r", "*Replace θ with −θ; if equation unchanged, symmetric", "Replace θ with π − θ", "Replace θ with θ + π"],
         "cos(−θ) = cos θ, so r = f(cos θ) has x-axis symmetry."),
        ("To test for y-axis symmetry:", ["Replace θ with −θ", "*Replace θ with π − θ; if equation unchanged, symmetric", "Replace r with −r", "No test exists"],
         "Equations in sin θ typically have y-axis symmetry."),
        ("r = sin θ is a circle tangent to the origin with center at:", ["(0.5, 0)", "*(0, 0.5) in Cartesian", "Origin", "(1, π/2)"],
         "r = a sin θ has center at (0, a/2)."),
        ("r = −2 cos θ is a circle with center at:", ["(1, 0)", "*(−1, 0)", "(0, −1)", "(2, 0)"],
         "r = a cos θ center at (a/2, 0); here a = −2 → center (−1, 0)."),
        ("A lemniscate has the form:", ["r = a cos θ", "*r² = a² cos(2θ) (figure-eight shape)", "r = a + b cos θ", "r = aθ"],
         "r² = a² cos(2θ) or r² = a² sin(2θ)."),
        ("To plot a polar curve by hand, you:", ["Plot x vs. y directly", "*Make a table of θ vs. r, then plot (r, θ) points on polar grid", "Only use a calculator", "Guess the shape"],
         "Table of values, then plot on polar paper."),
        ("The maximum r of the cardioid r = 3(1 + cos θ) is:", ["3", "*6 (at θ = 0)", "0", "9"],
         "Max when cos θ = 1: r = 3(2) = 6."),
        ("Polar curve identification is a common AP topic. r = 5sin(2θ) is:", ["Spiral", "Cardioid", "*Rose with 4 petals", "Circle"],
         "sin(nθ) with n = 2 (even) → 4 petals."),
    ]
)
lessons[k] = v

# ── 8.3 Converting Between Polar & Rectangular ──
k, v = build_lesson(8, 3, "Converting Polar & Rectangular Coordinates",
    "<h3>Converting Between Polar &amp; Rectangular</h3>"
    "<h4>Polar → Rectangular</h4>"
    "<p><b>x = r cos θ, y = r sin θ</b></p>"
    "<h4>Rectangular → Polar</h4>"
    "<p><b>r = √(x² + y²), θ = arctan(y/x)</b> (adjusted for quadrant).</p>"
    "<h4>Equation Conversion</h4>"
    "<p>Substitute x = r cos θ, y = r sin θ, x²+y² = r² to convert equations between systems.</p>",
    [
        ("Polar → Rectangular", "x = r cos θ, y = r sin θ."),
        ("Rectangular → Polar", "r = √(x²+y²), θ = arctan(y/x) (with quadrant adjustment)."),
        ("r² = x² + y²", "Links the radial distance to Cartesian coordinates."),
        ("Equation Conversion", "Replace r², r cos θ, r sin θ with x²+y², x, y (or vice versa)."),
        ("Quadrant Adjustment", "arctan gives values in (−π/2, π/2); add π for Q II/III points."),
    ],
    [
        ("Convert (3, π/6) to rectangular:", ["(3, 0.5)", "*(3cos(π/6), 3sin(π/6)) = (3√3/2, 3/2)", "(3/2, 3√3/2)", "(√3, 3)"],
         "x = 3cos30° = 3√3/2, y = 3sin30° = 3/2."),
        ("Convert (4, π/2) to rectangular:", ["(4, 0)", "*(0, 4)", "(0, −4)", "(4, 4)"],
         "x = 4cos(π/2) = 0, y = 4sin(π/2) = 4."),
        ("Convert the Cartesian point (1, 1) to polar:", ["(1, π/4)", "*(√2, π/4)", "(2, π/4)", "(1, 45)"],
         "r = √(1+1) = √2, θ = arctan(1/1) = π/4."),
        ("Convert (−1, √3) to polar:", ["(2, π/3)", "*(2, 2π/3)", "(√2, π/3)", "(2, −π/3)"],
         "r = √(1+3) = 2. arctan(√3/(−1)): point in Q II → θ = π − π/3 = 2π/3."),
        ("Convert (0, −5) to polar:", ["(5, 0)", "(5, π)", "*(5, 3π/2) or (5, −π/2)", "(−5, π/2)"],
         "r = 5, point on negative y-axis → θ = 3π/2."),
        ("The equation x² + y² = 16 in polar:", ["r = 4 cos θ", "*r = 4", "r² = 16 cos θ", "r = 16"],
         "x²+y² = r² → r² = 16 → r = 4."),
        ("The equation y = x in polar:", ["r = 1", "*tan θ = 1 → θ = π/4 (a ray)", "r = sin θ / cos θ", "r = θ"],
         "y/x = tan θ = 1 → θ = π/4 (and θ = 5π/4 for the other half)."),
        ("The equation x = 3 in polar:", ["r = 3", "*r cos θ = 3 → r = 3/cos θ = 3 sec θ", "θ = 3", "r = 3 sin θ"],
         "x = r cos θ = 3 → r = 3 sec θ."),
        ("The equation r = 6 sin θ in rectangular:", ["x² + y² = 6y", "*x² + y² = 6y (multiply r·r = 6·r sin θ → r² = 6y)", "x = 6y", "x² + y² = 36"],
         "Multiply both sides by r: r² = 6r sinθ → x²+y² = 6y."),
        ("Simplify x²+y²=6y to standard circle form:", ["(x−3)² + y² = 9", "*x² + (y−3)² = 9", "x² + y² = 9", "(x+3)² + y² = 9"],
         "x² + y² − 6y = 0 → x² + (y²−6y+9) = 9 → x² + (y−3)² = 9."),
        ("So r = 6 sin θ is a circle centered at:", ["(3, 0)", "(0, 6)", "*(0, 3) with radius 3", "Origin"],
         "Center (0, 3), radius 3."),
        ("r = 2 cos θ + 2 sin θ in rectangular:", ["x² + y² = 2x + 2y", "*x² + y² = 2x + 2y (multiply by r: r² = 2r cosθ + 2r sinθ)", "x + y = 2", "r = 2"],
         "r² = 2x + 2y → x²+y² = 2x + 2y."),
        ("Convert r = 1/(1 − cos θ) to rectangular (this is a parabola):", ["y² = 2x + 1", "*r − r cos θ = 1 → √(x²+y²) − x = 1 → x²+y² = (x+1)² → y² = 2x+1", "x = y²", "x² = y"],
         "Multiply: r − rcosθ = 1. Then r = x+1, so r² = (x+1)² → y² = 2x + 1."),
        ("The equation r = 4/(1 + sin θ) represents:", ["A circle", "*A conic section (parabola: eccentricity 1)", "A rose", "A spiral"],
         "r = ed/(1 + e sinθ) with e = 1 → parabola."),
        ("When converting rectangular → polar, always check the:", ["r value only", "*Quadrant of the point (arctan alone may give wrong angle)", "Sign of x only", "Nothing"],
         "arctan(y/x) is in (−π/2, π/2); adjust for Q II, III."),
        ("Convert x² + y² + 4x = 0 to polar:", ["r = −4 cos θ", "*r² + 4r cos θ = 0 → r(r + 4cos θ) = 0 → r = −4 cos θ", "r = 4 cos θ", "r = 4 sin θ"],
         "r ≠ 0 → r = −4 cos θ."),
        ("That's a circle centered at:", ["(0, −2)", "*(−2, 0) with radius 2", "(2, 0)", "(0, 2)"],
         "x²+4x+y² = 0 → (x+2)²+y² = 4. Center (−2, 0), r = 2."),
        ("In general, r = a cos θ + b sin θ converts to a circle with center:", ["(a, b)", "*(a/2, b/2)", "(a, 0)", "(0, b)"],
         "Center (a/2, b/2) and radius √(a²+b²)/2."),
        ("Why learn both coordinate systems?", ["Only for exams", "*Some curves and problems are much simpler in one system than the other", "Tradition", "They're identical"],
         "Polar simplifies circular/rotational problems; rectangular simplifies linear ones."),
        ("On the AP exam, you may be asked to:", ["Only plot points", "*Convert equations between polar and rectangular and identify curves", "Only use rectangular", "Ignore polar"],
         "Conversion and curve identification are standard AP topics."),
    ]
)
lessons[k] = v

# ── 8.4 Complex Numbers in Polar Form ──
k, v = build_lesson(8, 4, "Complex Numbers in Polar Form",
    "<h3>Complex Numbers in Polar Form</h3>"
    "<p>Any complex number z = a + bi can be written as:</p>"
    "<p><b>z = r(cos θ + i sin θ) = r · cis θ</b></p>"
    "<p>where r = |z| = √(a²+b²) is the <b>modulus</b> and θ = arg(z) is the <b>argument</b>.</p>"
    "<h4>Multiplication &amp; Division</h4>"
    "<ul><li>z₁z₂ = r₁r₂ · cis(θ₁+θ₂) — multiply moduli, add arguments.</li>"
    "<li>z₁/z₂ = (r₁/r₂) · cis(θ₁−θ₂) — divide moduli, subtract arguments.</li></ul>",
    [
        ("Modulus |z|", "r = √(a²+b²); the distance from z to the origin in the complex plane."),
        ("Argument arg(z)", "The angle θ from the positive real axis to z."),
        ("Polar (Trigonometric) Form", "z = r(cosθ + i sinθ) = r cis θ."),
        ("Multiplication Rule", "Multiply moduli and add arguments: z₁z₂ = r₁r₂ cis(θ₁+θ₂)."),
        ("Division Rule", "Divide moduli and subtract arguments: z₁/z₂ = (r₁/r₂) cis(θ₁−θ₂)."),
    ],
    [
        ("The modulus of z = 3 + 4i:", ["7", "5i", "*5", "1"],
         "|z| = √(9+16) = 5."),
        ("The argument of z = 1 + i:", ["90°", "*45° (π/4)", "0°", "180°"],
         "arctan(1/1) = 45°."),
        ("z = 3 + 4i in polar form:", ["*5(cos 53.13° + i sin 53.13°)", "5 cis 45°", "7 cis 30°", "5 cis 90°"],
         "r = 5, θ = arctan(4/3) ≈ 53.13°."),
        ("z = 2(cos 60° + i sin 60°) in rectangular:", ["2 + 2i", "*(2)(0.5) + (2)(√3/2)i = 1 + √3 i", "√3 + i", "1 + i"],
         "a = 2cos60° = 1, b = 2sin60° = √3."),
        ("If z₁ = 3 cis 30° and z₂ = 2 cis 45°, then z₁z₂ =", ["5 cis 75°", "*6 cis 75°", "6 cis 30°", "1.5 cis 75°"],
         "r₁r₂ = 6, θ₁+θ₂ = 75°."),
        ("z₁/z₂ using the same values:", ["6 cis 75°", "*1.5 cis(−15°)", "1.5 cis 75°", "6 cis(−15°)"],
         "3/2 = 1.5, 30°−45° = −15°."),
        ("The cis notation means:", ["cosine inverse sine", "*cos θ + i sin θ", "cos θ − i sin θ", "sin θ + i cos θ"],
         "Abbreviation: cis θ = cos θ + i sin θ."),
        ("|z| = 0 means:", ["z = 1", "z = i", "*z = 0", "z is undefined"],
         "The only complex number with modulus 0 is z = 0."),
        ("The argument of z = −1:", ["0°", "90°", "*180° (π)", "270°"],
         "On the negative real axis."),
        ("The argument of z = −i:", ["0°", "90°", "180°", "*270° (3π/2) or equivalently −90°"],
         "On the negative imaginary axis."),
        ("Polar form makes multiplication easier because:", ["*You multiply magnitudes and add angles instead of expanding (a+bi)(c+di)", "It's harder", "It eliminates i", "It's the same difficulty"],
         "Modulus multiplication + argument addition is simpler."),
        ("z = 4 cis 0°:", ["4i", "*4 (purely real)", "0", "4 + 4i"],
         "cos 0° = 1, sin 0° = 0 → z = 4."),
        ("z = 2 cis 90°:", ["2", "*2i", "−2", "−2i"],
         "cos 90° = 0, sin 90° = 1 → z = 2i."),
        ("z = 2 cis 180°:", ["2", "2i", "*−2", "−2i"],
         "cos 180° = −1, sin 180° = 0 → z = −2."),
        ("z = 2 cis 270°:", ["2", "2i", "−2", "*−2i"],
         "cos 270° = 0, sin 270° = −1 → z = −2i."),
        ("The complex conjugate of r cis θ is:", ["r cis θ", "*r cis(−θ)", "(1/r) cis θ", "r cis(θ+π)"],
         "Conjugate reflects across real axis: negate the argument."),
        ("|z₁z₂| = ?", ["|z₁| + |z₂|", "*|z₁| · |z₂|", "|z₁| − |z₂|", "|z₁|²|z₂|²"],
         "Modulus of product = product of moduli."),
        ("arg(z₁z₂) = ?", ["arg(z₁) · arg(z₂)", "*arg(z₁) + arg(z₂)", "arg(z₁) − arg(z₂)", "0"],
         "Argument of product = sum of arguments."),
        ("Euler's formula connects polar form to:", ["*e^(iθ) = cos θ + i sin θ", "e^θ = cos θ", "ln θ = sin θ", "Nothing"],
         "z = r · e^(iθ) is the exponential form."),
        ("Polar form is essential for De Moivre's Theorem because:", ["It avoids trig", "*Powers and roots are simple: just multiply/divide the argument", "It eliminates complex numbers", "It's not essential"],
         "De Moivre's uses polar form directly."),
    ]
)
lessons[k] = v

# ── 8.5 De Moivre's Theorem ──
k, v = build_lesson(8, 5, "De Moivre's Theorem",
    "<h3>De Moivre's Theorem</h3>"
    "<p><b>[r(cos θ + i sin θ)]ⁿ = rⁿ(cos nθ + i sin nθ)</b></p>"
    "<h4>Powers</h4><p>Raise modulus to the nth power and multiply the argument by n.</p>"
    "<h4>Roots</h4>"
    "<p>The nth roots of z = r cis θ are: <b>r^(1/n) · cis((θ + 2kπ)/n)</b> for k = 0, 1, …, n−1.</p>"
    "<p>The n roots are equally spaced around a circle of radius r^(1/n).</p>",
    [
        ("De Moivre's Theorem", "[r cis θ]ⁿ = rⁿ cis(nθ); powers of complex numbers in polar form."),
        ("nth Power", "Raise r to the n and multiply θ by n."),
        ("nth Roots", "r^(1/n) cis((θ+2kπ)/n) for k = 0, 1, …, n−1."),
        ("Equally Spaced Roots", "The n roots form a regular n-gon on a circle of radius r^(1/n)."),
        ("Cube Roots of Unity", "1, cis(2π/3), cis(4π/3): three equally spaced points on the unit circle."),
    ],
    [
        ("De Moivre's Theorem states [r cis θ]ⁿ =", ["rⁿ cis θ", "*rⁿ cis(nθ)", "r cis(nθ)", "nrⁿ cis θ"],
         "Raise r to n, multiply argument by n."),
        ("(2 cis 30°)³ =", ["2 cis 90°", "*8 cis 90° = 8i", "6 cis 90°", "8 cis 30°"],
         "2³ = 8, 3 × 30° = 90°. 8 cis 90° = 8i."),
        ("(1 + i)⁴: First convert to polar. |1+i| = √2, arg = 45°. Then:", ["4√2 cis 180°", "*(√2)⁴ cis(4×45°) = 4 cis 180° = −4", "2 cis 90°", "4"],
         "(√2)⁴ = 4, 4 × 45° = 180°. 4 cis 180° = −4."),
        ("(cis 60°)⁶ =", ["cis 60°", "*cis 360° = 1", "cis 180°", "6 cis 60°"],
         "r = 1, arg = 6 × 60° = 360° → cis 360° = 1."),
        ("The cube roots of 8 (= 8 cis 0°) are:", ["Only 2", "*2 cis 0°, 2 cis 120°, 2 cis 240° (i.e., 2, −1+√3i, −1−√3i)", "8, −8, 8i", "2, 4, 8"],
         "r^(1/3) = 2. Arguments: 0°, 120°, 240°."),
        ("How many cube roots does any nonzero complex number have?", ["1", "2", "*3", "Infinitely many"],
         "An nth root gives exactly n distinct roots."),
        ("The 4th roots of 16 = 16 cis 0° have modulus:", ["16", "*2 (= 16^(1/4))", "4", "1"],
         "16^(1/4) = 2."),
        ("The 4th roots of 16: arguments are:", ["0°, 45°, 90°, 135°", "*0°, 90°, 180°, 270°", "0°, 60°, 120°, 180°", "0°, 180° only"],
         "360°/4 = 90° spacing. Arguments: 0°, 90°, 180°, 270°."),
        ("So the 4th roots of 16 are:", ["2, 2i, −2, −2i", "*2, 2i, −2, −2i", "4, −4, 4i, −4i", "2, −2 only"],
         "2 cis 0° = 2, 2 cis 90° = 2i, 2 cis 180° = −2, 2 cis 270° = −2i."),
        ("The nth roots of any number are equally spaced on a circle, forming:", ["*A regular n-gon", "A line", "An ellipse", "Random positions"],
         "They form a regular polygon inscribed in a circle."),
        ("The square roots of i = cis 90°:", ["i and −i", "*cis 45° and cis 225° = (√2/2 + √2/2 i) and (−√2/2 − √2/2 i)", "1 and −1", "i only"],
         "r = 1, args: 45° and 225°."),
        ("The cube roots of unity (1) are:", ["*1, cis 120°, cis 240° (= 1, −½+√3/2 i, −½−√3/2 i)", "1, −1, i", "1 only", "1, i, −i"],
         "Arguments: 0°, 120°, 240°."),
        ("The sum of all nth roots of unity equals:", ["n", "*0", "1", "n − 1"],
         "The roots form a regular polygon centered at the origin; their sum is 0."),
        ("De Moivre's Theorem can prove trig identities by expanding:", ["Nothing", "*cos nθ and sin nθ in terms of cos θ and sin θ", "ex = sin x", "Only for n = 2"],
         "Expand [cosθ + i sinθ]ⁿ using binomial theorem and equate real/imaginary parts."),
        ("(cis θ)⁻¹ =", ["cis θ", "*cis(−θ)", "0", "i cis θ"],
         "Raise to power −1: argument becomes −θ. Same as the complex conjugate for unit modulus."),
        ("Find (−1)^(1/3) using De Moivre's:", ["−1 only", "*cis 60°, cis 180° = −1, cis 300° (three cube roots)", "1 and −1", "i"],
         "−1 = cis 180°. Roots: cis 60°, cis 180°, cis 300°."),
        ("What is (√3 + i)⁵? |z| = 2, arg = 30°. By De Moivre:", ["32 cis 30°", "*2⁵ cis 150° = 32 cis 150° = −16√3 + 16i", "32 cis 0°", "10 cis 150°"],
         "2⁵ = 32, 5×30° = 150°. 32 cis 150° = 32(−√3/2 + i/2)."),
        ("De Moivre's Theorem requires:", ["Rectangular form", "*Polar (trigonometric) form", "Only real numbers", "Matrix form"],
         "The theorem is stated and applied in polar form."),
        ("On the AP exam, you might be asked to find:", ["0th roots", "*All cube or 4th roots of a complex number", "Infinite roots", "No roots"],
         "Finding nth roots is a standard problem."),
        ("The practical application of nth roots of complex numbers includes:", ["*Signal processing, electrical engineering (phasors)", "Only pure math", "Cooking", "Only theoretical proofs"],
         "Phasors in EE, filter design, and quantum mechanics all use complex roots."),
    ]
)
lessons[k] = v

# ── 8.6 Electrical Engineering Applications ──
k, v = build_lesson(8, 6, "Electrical Engineering Applications",
    "<h3>Electrical Engineering: Phasors &amp; AC Circuits</h3>"
    "<h4>Phasors</h4>"
    "<p>AC voltages and currents are sinusoidal: v(t) = V₀ cos(ωt + φ). Each is represented by a <b>phasor</b> V = V₀ cis φ in the complex plane.</p>"
    "<h4>Impedance</h4>"
    "<p>Z = R + jX (j = i in EE). |Z| = √(R²+X²), θ_Z = arctan(X/R).</p>"
    "<h4>Ohm's Law for AC</h4>"
    "<p>V = I · Z (phasor multiplication: multiply magnitudes, add phases).</p>",
    [
        ("Phasor", "A complex number representing the amplitude and phase of a sinusoidal signal."),
        ("Impedance (Z)", "Z = R + jX; complex resistance combining resistance (R) and reactance (X)."),
        ("j = √(−1)", "Engineers use j instead of i (since i denotes current)."),
        ("Ohm's Law (AC)", "V = IZ; phasor voltage = phasor current × impedance."),
        ("Phase Angle", "θ = arctan(X/R); the angle between voltage and current."),
    ],
    [
        ("In electrical engineering, the imaginary unit is denoted:", ["i", "*j", "k", "e"],
         "To avoid confusion with current i."),
        ("A phasor represents:", ["DC voltage", "*The amplitude and phase of an AC sinusoidal signal", "Only resistance", "Only frequency"],
         "Phasor = V₀ cis φ."),
        ("V = 120 cis 0° and I = 10 cis(−30°). Impedance Z = V/I:", ["12 cis 30°", "*12 cis 30° (divide magnitudes, subtract angles: 0°−(−30°) = 30°)", "1200 cis(−30°)", "12 cis(−30°)"],
         "Z = 120/10 cis(0° − (−30°)) = 12 cis 30°."),
        ("|Z| = 12, θ = 30°. R component:", ["12", "6", "*12 cos 30° = 6√3 ≈ 10.39 Ω", "12 sin 30° = 6"],
         "R = |Z| cos θ."),
        ("X (reactance) component:", ["12 cos 30°", "*12 sin 30° = 6 Ω", "0", "12"],
         "X = |Z| sin θ = 6 Ω."),
        ("Since X > 0, the circuit is:", ["Purely resistive", "*Inductive (positive reactance)", "Capacitive (negative reactance)", "Short circuit"],
         "Positive X = inductance dominates."),
        ("In a purely resistive circuit (X = 0), voltage and current are:", ["90° out of phase", "*In phase (φ = 0°)", "180° out of phase", "At random phase"],
         "No reactance → no phase shift."),
        ("In a purely inductive circuit, current lags voltage by:", ["0°", "*90°", "180°", "45°"],
         "V leads I by 90° in a pure inductor."),
        ("In a purely capacitive circuit, current leads voltage by:", ["0°", "*90°", "180°", "45°"],
         "I leads V by 90° in a pure capacitor."),
        ("Adding impedances in series uses:", ["Division", "*Z_total = Z₁ + Z₂ (complex addition)", "Multiplication", "Only magnitudes"],
         "Series: add phasor impedances."),
        ("For parallel impedances: 1/Z_total =", ["Z₁ + Z₂", "*1/Z₁ + 1/Z₂", "Z₁Z₂", "Z₁ − Z₂"],
         "Reciprocal sum, like parallel resistors."),
        ("Power in AC: P = |V||I| cos φ. The cos φ factor is the:", ["Reactance factor", "*Power factor", "Phase factor", "Loss factor"],
         "Power factor = cos(phase angle between V and I)."),
        ("A power factor of 1 means:", ["All reactive power", "*All real power (V and I in phase)", "No power", "Infinite power"],
         "cos 0° = 1 → purely resistive."),
        ("Why are complex numbers useful in EE?", ["They aren't", "*They simplify AC circuit analysis by converting differential equations to algebraic ones", "Only for appearance", "Tradition"],
         "Phasors turn calculus problems into algebra."),
        ("Three-phase power uses phasors separated by:", ["90°", "*120°", "180°", "60°"],
         "Three voltages 120° apart."),
        ("The impedance of a capacitor: Z_C =", ["jωC", "*1/(jωC) = −j/(ωC)", "R", "jωL"],
         "Capacitive impedance is 1/(jωC)."),
        ("The impedance of an inductor: Z_L =", ["1/(jωL)", "*jωL", "R", "−jωL"],
         "Inductive impedance is jωL."),
        ("RLC circuit: Z = R + j(ωL − 1/(ωC)). Resonance when:", ["R = 0", "*ωL = 1/(ωC) (reactances cancel)", "ω = 0", "L = C"],
         "At resonance, imaginary part vanishes → purely resistive."),
        ("At resonance frequency ω₀:", ["ω₀ = R/L", "*ω₀ = 1/√(LC)", "ω₀ = LC", "ω₀ = R"],
         "ωL = 1/(ωC) → ω² = 1/(LC) → ω = 1/√(LC)."),
        ("Complex numbers in polar form are used in EE for:", ["*Circuit analysis, filter design, signal processing, power systems", "Only in textbooks", "Only in theory", "Nothing practical"],
         "Ubiquitous in all of electrical engineering."),
    ]
)
lessons[k] = v

# ── 8.7 Physics Cases – Waves & Quantum ──
k, v = build_lesson(8, 7, "Physics Cases – Waves & Quantum Mechanics",
    "<h3>Physics: Waves &amp; Quantum Mechanics</h3>"
    "<h4>Wave Superposition</h4>"
    "<p>Adding sinusoidal waves with different phases is simplified by converting to phasors (complex exponentials) and adding the complex numbers.</p>"
    "<h4>Quantum Mechanics</h4>"
    "<p>The wave function ψ is complex-valued. Born's rule: P = |ψ|² gives the probability density, using the modulus squared of a complex number.</p>",
    [
        ("Superposition via Phasors", "Add complex exponentials instead of trig functions; the resultant's magnitude and phase follow directly."),
        ("Wave Function (ψ)", "A complex-valued function; its modulus squared |ψ|² gives probability density."),
        ("Born's Rule", "P(x) = |ψ(x)|²; probability from the modulus of a complex wave function."),
        ("Interference Pattern", "Results from adding wave phasors: constructive when in phase, destructive when π out of phase."),
        ("Euler's Formula", "e^(iθ) = cosθ + i sinθ; connects exponential and trig representations."),
    ],
    [
        ("Two waves y₁ = A cos(kx − ωt) and y₂ = A cos(kx − ωt + φ) add to:", ["2A cos(kx − ωt)", "*2A cos(φ/2) cos(kx − ωt + φ/2)", "0", "A cos(kx − ωt + φ/2)"],
         "Sum formula: resultant amplitude = 2A cos(φ/2)."),
        ("Complete constructive interference occurs when φ =", ["π", "*0 (or 2nπ)", "π/2", "3π/2"],
         "In phase → amplitudes add directly."),
        ("Complete destructive interference occurs when φ =", ["0", "*π (or (2n+1)π)", "π/2", "2π"],
         "Opposite phases → amplitudes cancel."),
        ("Phasor addition converts wave addition to:", ["Subtraction", "*Complex number addition (add amplitudes as vectors)", "Multiplication", "Division"],
         "Each wave is a phasor; add the complex numbers."),
        ("Euler's formula: e^(iθ) =", ["cosθ − i sinθ", "*cosθ + i sinθ", "sinθ + i cosθ", "1"],
         "Euler's fundamental identity."),
        ("A plane wave can be written as Ae^(i(kx−ωt)). The real part is:", ["A", "Ae^(ikx)", "*A cos(kx − ωt)", "A sin(kx − ωt)"],
         "Re[Ae^(iθ)] = A cos θ."),
        ("In quantum mechanics, the probability of finding a particle at x is:", ["ψ(x)", "|ψ(x)|", "*|ψ(x)|²", "ψ(x)²"],
         "Born's rule: P = |ψ|²."),
        ("If ψ = 3 + 4i, then |ψ|² =", ["7", "*25", "5", "49"],
         "|ψ|² = 3² + 4² = 25."),
        ("|ψ|² can also be computed as:", ["ψ²", "*ψ · ψ* (ψ times its complex conjugate)", "ψ + ψ*", "Re(ψ)²"],
         "|z|² = z · z̄."),
        ("The wave function of a particle in a box includes:", ["Only real numbers", "*sin(nπx/L) — real, but normalization can involve complex exponentials", "Only exponentials", "No math"],
         "Standing wave: ψₙ(x) = √(2/L) sin(nπx/L)."),
        ("In the double-slit experiment, the interference pattern is explained by:", ["Particle paths", "*Superposition of complex wave amplitudes and |sum|²", "Only classical physics", "Gravity"],
         "Add complex amplitudes, then take modulus squared."),
        ("The Fourier transform decomposes a signal into:", ["Real parts only", "*Complex exponentials (sinusoidal components with amplitude and phase)", "Integers", "Matrices"],
         "F(ω) = ∫ f(t) e^(−iωt) dt."),
        ("Phase velocity of a wave:", ["ω/k²", "*v_p = ω/k", "k/ω", "ω + k"],
         "v_p = ω/k."),
        ("Group velocity (for wave packets):", ["ω/k", "*v_g = dω/dk", "k/ω", "ω · k"],
         "v_g = dω/dk; the speed of the envelope."),
        ("Complex exponentials simplify wave math because:", ["They're harder", "*Differentiation of e^(iθ) is simple: d/dθ = i · e^(iθ)", "They eliminate imaginary parts", "No reason"],
         "Working with exponentials avoids trig identities."),
        ("In optics, thin film interference uses:", ["Only geometry", "*Phase differences expressed as complex amplitudes → |sum|²", "No physics", "Only algebra"],
         "Reflected waves from thin films add with phase differences."),
        ("The Schrödinger equation is written with:", ["Only real numbers", "*Complex numbers (i appears explicitly: iℏ ∂ψ/∂t = Ĥψ)", "Only matrices", "No math"],
         "Quantum mechanics is inherently complex-valued."),
        ("Adding N equal phasors, each shifted by δ from the next, gives resultant:", ["NA", "*sin(Nδ/2)/sin(δ/2) · A", "0 always", "A/N"],
         "Geometric series of phasors with common ratio e^(iδ)."),
        ("X-ray diffraction patterns are calculated using:", ["Only geometry", "*Complex structure factors (sum of atomic phasors)", "Only algebra", "No computation"],
         "F(hkl) = Σ fⱼ e^(2πi(hxⱼ+kyⱼ+lzⱼ))."),
        ("Polar form of complex numbers in physics is essential for:", ["*AC circuits, wave optics, quantum mechanics, signal processing", "Nothing practical", "Only pure math", "Only EE"],
         "Ubiquitous across physics and engineering."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 8: wrote {len(lessons)} lessons")
