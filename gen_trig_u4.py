#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 4: Trig Identities (7 lessons)."""
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

# ── 4.1 ──
k, v = build_lesson(4, 1, "Pythagorean Identities",
    "<h3>Pythagorean Identities</h3>"
    "<p>Derived from <b>sin²θ + cos²θ = 1</b> (the unit circle equation x² + y² = 1).</p>"
    "<h4>Three Forms</h4>"
    "<ul><li><b>sin²θ + cos²θ = 1</b></li>"
    "<li>Divide by cos²θ: <b>tan²θ + 1 = sec²θ</b></li>"
    "<li>Divide by sin²θ: <b>1 + cot²θ = csc²θ</b></li></ul>"
    "<p>These identities are used to simplify expressions, verify other identities, and solve equations.</p>",
    [
        ("sin²θ + cos²θ = 1", "The fundamental Pythagorean identity, true for all θ."),
        ("tan²θ + 1 = sec²θ", "Obtained by dividing sin²θ + cos²θ = 1 by cos²θ."),
        ("1 + cot²θ = csc²θ", "Obtained by dividing sin²θ + cos²θ = 1 by sin²θ."),
        ("Deriving from Unit Circle", "On the unit circle, x = cos θ, y = sin θ, and x² + y² = 1 gives sin² + cos² = 1."),
        ("Using Pythagorean Identities", "Replace one trig function with another to simplify: e.g., sin²θ = 1 − cos²θ."),
    ],
    [
        ("sin²θ + cos²θ =", ["0", "*1", "2", "sin θ + cos θ"],
         "The fundamental Pythagorean identity."),
        ("tan²θ + 1 =", ["csc²θ", "*sec²θ", "cot²θ", "sin²θ"],
         "Divide sin²θ + cos²θ = 1 by cos²θ."),
        ("1 + cot²θ =", ["sec²θ", "*csc²θ", "tan²θ", "cos²θ"],
         "Divide sin²θ + cos²θ = 1 by sin²θ."),
        ("If sin θ = 3/5, then cos²θ =", ["9/25", "*16/25", "3/5", "4/5"],
         "cos²θ = 1 − sin²θ = 1 − 9/25 = 16/25."),
        ("If cos θ = 12/13, then sin θ (θ in Q I) =", ["12/13", "*5/13", "1/13", "13/12"],
         "sin²θ = 1 − 144/169 = 25/169, sin θ = 5/13."),
        ("sec²θ − tan²θ =", ["0", "*1", "2", "sec θ − tan θ"],
         "From tan²θ + 1 = sec²θ, rearrange: sec²θ − tan²θ = 1."),
        ("csc²θ − cot²θ =", ["0", "*1", "csc θ", "2"],
         "1 + cot²θ = csc²θ → csc²θ − cot²θ = 1."),
        ("sin²θ can be rewritten as:", ["1 + cos²θ", "*1 − cos²θ", "cos²θ − 1", "tan²θ"],
         "sin²θ = 1 − cos²θ."),
        ("Which identity is obtained by dividing by cos²θ?", ["1 + cot²θ = csc²θ", "*tan²θ + 1 = sec²θ", "sin²θ + cos²θ = 1", "None"],
         "Dividing each term by cos²θ gives tan²θ + 1 = sec²θ."),
        ("If tan θ = 2 and θ is in Q I, sec θ =", ["2", "3", "*√5", "4"],
         "sec²θ = 1 + tan²θ = 1 + 4 = 5, sec θ = √5."),
        ("If cot θ = 1, then csc²θ =", ["1", "*2", "√2", "0"],
         "csc²θ = 1 + cot²θ = 1 + 1 = 2."),
        ("Simplify: sin²θ · sec²θ + cos²θ · sec²θ", ["0", "*sec²θ", "1", "2"],
         "Factor: sec²θ(sin²θ + cos²θ) = sec²θ · 1 = sec²θ."),
        ("(1 − sin²θ)/cos θ =", ["sin θ", "*cos θ", "tan θ", "sec θ"],
         "(1 − sin²θ) = cos²θ. So cos²θ/cos θ = cos θ."),
        ("sin²θ/(1 − cos θ) can be simplified using 1 − cos²θ = sin²θ:", ["sin θ", "*Not directly — factor differently: sin²θ = (1−cosθ)(1+cosθ), so the result is 1 + cos θ", "cos θ", "tan θ"],
         "sin²θ/(1−cos θ) = (1−cos θ)(1+cos θ)/(1−cos θ) = 1 + cos θ."),
        ("The Pythagorean identity originates from:", ["The law of sines", "*The equation of the unit circle x² + y² = 1", "The quadratic formula", "Euler's formula"],
         "On the unit circle, (cos θ)² + (sin θ)² = 1."),
        ("If sec θ = 3, then tan²θ =", ["3", "9", "*8", "10"],
         "tan²θ = sec²θ − 1 = 9 − 1 = 8."),
        ("cos²θ/(1 + sin θ) =", ["cos θ", "*(1 − sin θ) (using cos²θ = (1−sinθ)(1+sinθ))", "1 + sin θ", "tan θ"],
         "cos²θ = 1 − sin²θ = (1−sinθ)(1+sinθ). Divided by (1+sinθ) = 1−sinθ."),
        ("sin²30° + cos²30° =", ["0.5", "*1", "√3/2", "1.5"],
         "The identity holds for all angles: always 1."),
        ("If sin θ = −4/5 and θ is in Q III, cos θ =", ["4/5", "*−3/5", "3/5", "−4/5"],
         "cos²θ = 1 − 16/25 = 9/25. In Q III, cos θ < 0, so cos θ = −3/5."),
        ("tan²θ + 1 = sec²θ is valid for:", ["Only acute angles", "Only Q I", "*All θ where cos θ ≠ 0", "Only 0 to 2π"],
         "The identity holds wherever tan and sec are defined (cos θ ≠ 0)."),
    ]
)
lessons[k] = v

# ── 4.2 ──
k, v = build_lesson(4, 2, "Reciprocal Identities",
    "<h3>Reciprocal Identities</h3>"
    "<p>Each trig function has a reciprocal partner:</p>"
    "<ul><li><b>csc θ = 1/sin θ</b> and <b>sin θ = 1/csc θ</b></li>"
    "<li><b>sec θ = 1/cos θ</b> and <b>cos θ = 1/sec θ</b></li>"
    "<li><b>cot θ = 1/tan θ</b> and <b>tan θ = 1/cot θ</b></li></ul>"
    "<p>These identities let you convert between any trig function and its reciprocal to simplify expressions.</p>"
    "<h4>Usage</h4>"
    "<p>Replace less common functions (csc, sec, cot) with familiar ones (sin, cos, tan) when simplifying or verifying identities.</p>",
    [
        ("csc θ = 1/sin θ", "Cosecant is the reciprocal of sine."),
        ("sec θ = 1/cos θ", "Secant is the reciprocal of cosine."),
        ("cot θ = 1/tan θ", "Cotangent is the reciprocal of tangent."),
        ("Reciprocal Pair", "Two functions f and g such that f(θ) · g(θ) = 1 (e.g., sin · csc = 1)."),
        ("Simplification Strategy", "Rewrite csc, sec, cot in terms of sin and cos, then simplify."),
    ],
    [
        ("csc θ · sin θ =", ["0", "*1", "csc θ", "sin θ"],
         "csc θ = 1/sin θ, so csc θ · sin θ = 1."),
        ("sec θ · cos θ =", ["0", "*1", "sec θ", "cos θ"],
         "sec θ = 1/cos θ, so sec · cos = 1."),
        ("cot θ · tan θ =", ["0", "*1", "cot θ", "tan θ"],
         "cot = 1/tan, so cot · tan = 1."),
        ("1/csc θ =", ["cos θ", "tan θ", "*sin θ", "sec θ"],
         "csc θ = 1/sin θ → 1/csc θ = sin θ."),
        ("1/sec θ =", ["sin θ", "*cos θ", "tan θ", "csc θ"],
         "sec θ = 1/cos θ → 1/sec θ = cos θ."),
        ("1/cot θ =", ["sin θ", "cos θ", "*tan θ", "csc θ"],
         "cot = 1/tan → 1/cot = tan."),
        ("sec θ/csc θ =", ["cos θ/sin θ", "1", "*tan θ", "cot θ"],
         "sec/csc = (1/cos)/(1/sin) = sin/cos = tan."),
        ("csc θ/sec θ =", ["tan θ", "1", "*cot θ", "sin θ"],
         "csc/sec = (1/sin)/(1/cos) = cos/sin = cot."),
        ("sin θ · csc θ + cos θ · sec θ =", ["0", "1", "*2", "sin θ + cos θ"],
         "1 + 1 = 2."),
        ("Simplify: (sin θ)(sec θ) =", ["cos θ", "csc θ", "*tan θ", "1"],
         "sin θ · (1/cos θ) = sin θ/cos θ = tan θ."),
        ("Simplify: (cos θ)(csc θ) =", ["sec θ", "tan θ", "*cot θ", "1"],
         "cos θ · (1/sin θ) = cos θ/sin θ = cot θ."),
        ("If sec θ = 5/4, then cos θ =", ["5/4", "*4/5", "3/5", "4/3"],
         "cos θ = 1/sec θ = 4/5."),
        ("If csc θ = 13/5, then sin θ =", ["13/5", "*5/13", "12/13", "5/12"],
         "sin θ = 1/csc θ = 5/13."),
        ("cot θ in terms of sin and cos:", ["sin θ/cos θ", "*cos θ/sin θ", "1/(sin θ cos θ)", "sin θ + cos θ"],
         "cot θ = 1/tan θ = cos θ/sin θ."),
        ("Simplify: sec²θ − 1 (using reciprocal + Pythagorean):", ["1", "*tan²θ", "csc²θ", "cos²θ"],
         "sec²θ = 1 + tan²θ → sec²θ − 1 = tan²θ."),
        ("(csc θ − sin θ) expressed with common denominator:", ["(1 − sin²θ)/sin θ", "*(cos²θ)/sin θ = cos θ · cot θ", "sin θ/cos θ", "1"],
         "csc θ − sin θ = (1 − sin²θ)/sin θ = cos²θ/sin θ = cos θ · cot θ."),
        ("sin θ + cos θ · cot θ =", ["sin θ + cos²θ", "*csc θ", "sec θ", "tan θ"],
         "cos θ · cot θ = cos²θ/sin θ. So sin θ + cos²θ/sin θ = (sin²θ + cos²θ)/sin θ = 1/sin θ = csc θ."),
        ("Reciprocal identities help convert to:", ["Polar form", "*Sine and cosine for easier simplification", "Degrees", "Radians"],
         "Rewriting in terms of sin and cos is the standard simplification approach."),
        ("tan θ · csc θ =", ["cos θ", "sin θ", "*sec θ", "cot θ"],
         "(sin θ/cos θ)(1/sin θ) = 1/cos θ = sec θ."),
        ("cot θ · sec θ =", ["sin θ", "*csc θ", "cos θ", "tan θ"],
         "(cos θ/sin θ)(1/cos θ) = 1/sin θ = csc θ."),
    ]
)
lessons[k] = v

# ── 4.3 ──
k, v = build_lesson(4, 3, "Quotient Identities",
    "<h3>Quotient Identities</h3>"
    "<ul><li><b>tan θ = sin θ / cos θ</b></li>"
    "<li><b>cot θ = cos θ / sin θ</b></li></ul>"
    "<p>These are the two <b>quotient identities</b>. They connect tangent and cotangent to sine and cosine.</p>"
    "<h4>Applications</h4>"
    "<ul><li>Rewrite complicated expressions in terms of sin and cos using the quotient identities.</li>"
    "<li>Combined with reciprocal and Pythagorean identities, quotient identities are powerful simplification tools.</li></ul>",
    [
        ("tan θ = sin θ / cos θ", "The quotient identity for tangent."),
        ("cot θ = cos θ / sin θ", "The quotient identity for cotangent."),
        ("Quotient Identity Usage", "Convert tan or cot into sin/cos to simplify or verify expressions."),
        ("Combining Identities", "Quotient + Pythagorean + reciprocal identities work together for simplification."),
        ("tan · cot = 1", "Since tan = sin/cos and cot = cos/sin, their product is 1."),
    ],
    [
        ("tan θ =", ["cos θ / sin θ", "*sin θ / cos θ", "1 / sin θ", "1 / cos θ"],
         "Quotient identity: tan θ = sin θ / cos θ."),
        ("cot θ =", ["sin θ / cos θ", "*cos θ / sin θ", "1 / cos θ", "1 / sin θ"],
         "Quotient identity: cot θ = cos θ / sin θ."),
        ("If sin θ = 3/5 and cos θ = 4/5, tan θ =", ["4/3", "*3/4", "5/3", "5/4"],
         "tan θ = sin θ / cos θ = (3/5)/(4/5) = 3/4."),
        ("If sin θ = 3/5 and cos θ = 4/5, cot θ =", ["3/4", "*4/3", "5/4", "5/3"],
         "cot θ = cos/sin = (4/5)/(3/5) = 4/3."),
        ("tan θ · cos θ =", ["cos θ", "*sin θ", "1", "tan θ"],
         "(sin θ/cos θ) · cos θ = sin θ."),
        ("cot θ · sin θ =", ["sin θ", "*cos θ", "1", "cot θ"],
         "(cos θ/sin θ) · sin θ = cos θ."),
        ("tan²θ =", ["cos²θ/sin²θ", "*sin²θ/cos²θ", "1/cos²θ", "1/sin²θ"],
         "tan²θ = (sin θ/cos θ)² = sin²θ/cos²θ."),
        ("Simplify: sin θ / (cos θ · tan θ)", ["tan θ", "cos θ", "*1", "sin θ"],
         "sin θ / (cos θ · sin θ/cos θ) = sin θ / sin θ = 1."),
        ("(1 + tan²θ) cos²θ =", ["tan²θ", "*1 (since 1 + tan²θ = sec²θ, and sec²θ cos²θ = 1)", "cos²θ", "sec²θ"],
         "sec²θ · cos²θ = 1."),
        ("tan θ + cot θ =", ["0", "2", "*sin θ/cos θ + cos θ/sin θ = 1/(sin θ cos θ)", "1"],
         "Common denominator: (sin²θ + cos²θ)/(sin θ cos θ) = 1/(sin θ cos θ)."),
        ("(tan θ − cot θ)/(tan θ + cot θ) simplifies to:", ["0", "1", "*sin²θ − cos²θ", "tan²θ"],
         "Numerator: (sin²θ − cos²θ)/(sinθ cosθ). Denominator: 1/(sinθ cosθ). Ratio = sin²θ − cos²θ."),
        ("sin θ · cot θ + cos θ =", ["sin θ", "2 cos θ", "*2 cos θ", "cos θ"],
         "sin θ · (cos θ/sin θ) + cos θ = cos θ + cos θ = 2 cos θ."),
        ("cos θ · tan θ + sin θ =", ["cos θ", "*2 sin θ", "sin θ", "0"],
         "cos θ · (sin θ/cos θ) + sin θ = sin θ + sin θ = 2 sin θ."),
        ("tan(π/4) using quotient identity:", ["cos(π/4)/sin(π/4)", "*sin(π/4)/cos(π/4) = 1", "1/cos(π/4)", "1/sin(π/4)"],
         "sin(π/4)/cos(π/4) = (√2/2)/(√2/2) = 1."),
        ("Simplify: sec θ · sin θ", ["cos θ", "csc θ", "*tan θ", "1"],
         "(1/cos θ) · sin θ = sin θ/cos θ = tan θ."),
        ("tan θ is undefined when cos θ = 0 because:", ["sin θ = 0 too", "*Division by zero in sin θ/cos θ", "tan is not a real function", "The identity fails"],
         "tan θ = sin θ/cos θ; division by zero is undefined."),
        ("Simplify: (1 − cos²θ)/sin θ", ["cos θ", "*sin θ", "tan θ", "1"],
         "(1 − cos²θ) = sin²θ. So sin²θ/sin θ = sin θ."),
        ("cot θ/csc θ =", ["sin θ", "*cos θ", "tan θ", "sec θ"],
         "(cos θ/sin θ)/(1/sin θ) = cos θ."),
        ("tan θ/sec θ =", ["cos θ", "*sin θ", "csc θ", "cot θ"],
         "(sin θ/cos θ)/(1/cos θ) = sin θ."),
        ("Which set of identities — quotient, reciprocal, or Pythagorean — lets you rewrite tan and cot in terms of sin and cos?", ["Reciprocal", "Pythagorean", "*Quotient", "None"],
         "Quotient identities: tan = sin/cos, cot = cos/sin."),
    ]
)
lessons[k] = v

# ── 4.4 ──
k, v = build_lesson(4, 4, "Cofunction Identities",
    "<h3>Cofunction Identities</h3>"
    "<p>Cofunctions of <b>complementary angles</b> (adding to π/2 or 90°) are equal:</p>"
    "<ul><li>sin(π/2 − θ) = cos θ &nbsp;&nbsp;and&nbsp;&nbsp; cos(π/2 − θ) = sin θ</li>"
    "<li>tan(π/2 − θ) = cot θ &nbsp;&nbsp;and&nbsp;&nbsp; cot(π/2 − θ) = tan θ</li>"
    "<li>sec(π/2 − θ) = csc θ &nbsp;&nbsp;and&nbsp;&nbsp; csc(π/2 − θ) = sec θ</li></ul>"
    "<p>The prefix <b>\"co-\"</b> means complement: co-sine, co-tangent, co-secant.</p>",
    [
        ("Cofunction", "A pair of trig functions whose values swap at complementary angles: sin/cos, tan/cot, sec/csc."),
        ("Complementary Angles", "Two angles that sum to 90° (or π/2 radians)."),
        ("sin(π/2 − θ) = cos θ", "The sine of the complement equals the cosine."),
        ("tan(π/2 − θ) = cot θ", "The tangent of the complement equals the cotangent."),
        ("sec(π/2 − θ) = csc θ", "The secant of the complement equals the cosecant."),
    ],
    [
        ("sin(π/2 − θ) =", ["sin θ", "*cos θ", "tan θ", "−sin θ"],
         "Cofunction identity: sin(π/2 − θ) = cos θ."),
        ("cos(π/2 − θ) =", ["cos θ", "*sin θ", "−cos θ", "tan θ"],
         "Cofunction identity: cos(π/2 − θ) = sin θ."),
        ("tan(π/2 − θ) =", ["tan θ", "*cot θ", "−tan θ", "sec θ"],
         "Cofunction identity: tan(π/2 − θ) = cot θ."),
        ("csc(π/2 − θ) =", ["csc θ", "*sec θ", "sin θ", "cos θ"],
         "Cofunction identity: csc(π/2 − θ) = sec θ."),
        ("sin 30° = cos ?", ["30°", "*60°", "45°", "90°"],
         "30° + 60° = 90°. sin 30° = cos 60° = 1/2."),
        ("cos 20° = sin ?", ["20°", "*70°", "80°", "10°"],
         "20° + 70° = 90°."),
        ("tan 15° = cot ?", ["15°", "*75°", "30°", "60°"],
         "15° + 75° = 90°."),
        ("The \"co\" in cosine means:", ["Complementary — *cosine = sine of the complement", "Negative", "Double", "Half"],
         "Co-sine = sine of the complementary angle."),
        ("If sin θ = 0.6, then cos(π/2 − θ) =", ["cos θ", "*0.6", "0.8", "0.4"],
         "cos(π/2 − θ) = sin θ = 0.6."),
        ("sec 25° = csc ?", ["25°", "*65°", "75°", "35°"],
         "25° + 65° = 90°."),
        ("sin(π/2 − π/3) = cos(π/3) =", ["√3/2", "*1/2", "√2/2", "0"],
         "cos(π/3) = 1/2."),
        ("Complementary angles sum to:", ["180°", "*90°", "360°", "45°"],
         "By definition, complementary angles add to 90°."),
        ("cot 45° = tan ?", ["0°", "*45°", "90°", "60°"],
         "45° + 45° = 90°. Also cot 45° = tan 45° = 1."),
        ("sin 90° = cos ?", ["90°", "*0°", "45°", "180°"],
         "90° + 0° = 90°."),
        ("Which pairs are cofunctions?", ["sin & tan", "*sin & cos, tan & cot, sec & csc", "sin & csc", "tan & sec"],
         "Cofunctions swap co- prefix: sin/cos, tan/cot, sec/csc."),
        ("cos(π/2 − π/6) =", ["cos(π/6)", "*sin(π/6) = 1/2", "tan(π/6)", "0"],
         "cos(π/2 − π/6) = sin(π/6) = 1/2."),
        ("If tan θ = 5, then cot(π/2 − θ) =", ["1/5", "*5", "0.2", "tan θ is undefined"],
         "cot(π/2 − θ) = tan θ = 5."),
        ("Cofunction identities are especially useful for:", ["Quadratic equations", "*Converting between trig functions at complementary angles", "Finding asymptotes", "Graphing"],
         "They let you switch between cofunctions when angles are complementary."),
        ("sin 50° + cos 40° =", ["1", "*2 sin 50° (since cos 40° = sin 50°)", "0", "sin 90°"],
         "cos 40° = sin 50° (cofunctions). So sin 50° + sin 50° = 2 sin 50°."),
        ("tan 60° · cot 30° =", ["1", "*3 (both equal √3)", "√3", "0"],
         "tan 60° = √3, cot 30° = √3. Product = 3."),
    ]
)
lessons[k] = v

# ── 4.5 ──
k, v = build_lesson(4, 5, "Verifying Identities",
    "<h3>Verifying Trig Identities</h3>"
    "<p>To <b>verify</b> (prove) an identity, transform one side until it equals the other. Key techniques:</p>"
    "<ul><li>Work on the more complex side.</li>"
    "<li>Convert everything to sin and cos.</li>"
    "<li>Factor, combine fractions, or multiply by a conjugate.</li>"
    "<li>Use Pythagorean, reciprocal, quotient, and cofunction identities.</li></ul>"
    "<p><b>Important:</b> Never cross-multiply or treat it as an equation — you're proving, not solving.</p>",
    [
        ("Verifying an Identity", "Showing that one side of the equation can be transformed into the other using known identities."),
        ("Work the Complex Side", "Start with the more complicated side — it's easier to simplify than to build up."),
        ("Convert to sin/cos", "Rewriting all trig functions as sin and cos often reveals simplifications."),
        ("Conjugate Multiplication", "Multiply by (1 + sin θ)/(1 + sin θ) or similar to create difference-of-squares patterns."),
        ("Never Cross-Multiply", "Identities are proven by transforming one side; treating both sides equally assumes the result."),
    ],
    [
        ("The first strategy for verifying identities is usually to:", ["Cross-multiply", "*Work on the more complex side", "Guess and check", "Use a calculator"],
         "Start with the complex side and simplify it."),
        ("Which is a valid technique?", ["Cross-multiply", "Square both sides", "*Convert csc, sec, cot to sin and cos", "Set both sides to 0"],
         "Converting to sin/cos is a standard verification technique."),
        ("Verify: sec θ cos θ = 1. Start with left side:", ["cos θ / sec θ", "*(1/cos θ)(cos θ) = 1 ✓", "sec θ + cos θ", "1/1"],
         "sec θ cos θ = (1/cos θ) cos θ = 1."),
        ("Verify: tan θ cot θ = 1:", ["Need complex algebra", "*(sin θ/cos θ)(cos θ/sin θ) = 1 ✓", "Impossible", "Only true sometimes"],
         "tan · cot = (sin/cos)(cos/sin) = 1."),
        ("To verify tan θ = sin θ sec θ, rewrite the right side:", ["sin θ / sec θ", "*sin θ · (1/cos θ) = sin θ/cos θ = tan θ ✓", "sin θ + sec θ", "cos θ/sin θ"],
         "sin θ · sec θ = sin θ/cos θ = tan θ."),
        ("Verify: (1 − sin²θ)/cos θ = cos θ:", ["Use quotient identity", "*Replace 1 − sin²θ with cos²θ: cos²θ/cos θ = cos θ ✓", "Cross-multiply", "Cannot be verified"],
         "Pythagorean identity gives cos²θ/cos θ = cos θ."),
        ("Why shouldn't you cross-multiply when verifying?", ["It's too slow", "*It assumes the identity is true — you'd be using what you're trying to prove", "It changes the identity", "It's always wrong"],
         "Cross-multiplying treats both sides as equal, which is what you're trying to show."),
        ("Multiplying by a conjugate is useful when the expression contains:", ["Only sines", "*Terms like (1 − sin θ) or (1 + cos θ)", "No fractions", "Only tangent"],
         "Conjugates create difference-of-squares, which work with Pythagorean identities."),
        ("Verify: sin²θ(1 + cot²θ) = 1:", ["Factor differently", "*sin²θ · csc²θ = sin²θ/sin²θ = 1 ✓", "Add cos²θ", "Invalid identity"],
         "1 + cot²θ = csc²θ. Then sin²θ · csc²θ = sin²θ · (1/sin²θ) = 1."),
        ("(sec θ − cos θ) =", ["1", "sin θ", "*sin θ tan θ", "cos θ tan θ"],
         "1/cos θ − cos θ = (1 − cos²θ)/cos θ = sin²θ/cos θ = sin θ · tan θ."),
        ("Verify: csc θ − sin θ = cos θ cot θ:", ["*LHS = 1/sinθ − sinθ = (1−sin²θ)/sinθ = cos²θ/sinθ = cosθ · (cosθ/sinθ) = cosθ cotθ ✓", "Cannot be verified", "Use cross-multiplication", "Only for acute angles"],
         "Convert to sin/cos and simplify."),
        ("When both sides look complex, you should:", ["Give up", "Cross-multiply", "*Simplify each side independently toward a common expression", "Guess"],
         "You can work both sides toward a common middle form."),
        ("Verify: cos θ/(1 + sin θ) = (1 − sin θ)/cos θ:", ["*Multiply LHS by (1−sinθ)/(1−sinθ): cos θ(1−sinθ)/(1−sin²θ) = cosθ(1−sinθ)/cos²θ = (1−sinθ)/cosθ ✓", "Cross-multiply", "Not an identity", "Use quotient identity"],
         "Using the conjugate 1 − sin θ and Pythagorean identity proves it."),
        ("Factoring is useful when expressions contain:", ["No trig functions", "*Common factors or difference of squares", "Only constants", "Logarithms"],
         "Factoring lets you cancel or simplify using known identities."),
        ("tan²θ − sin²θ = tan²θ sin²θ. Start with LHS:", ["*sin²θ/cos²θ − sin²θ = sin²θ(1/cos²θ − 1) = sin²θ(1−cos²θ)/cos²θ = sin²θ · sin²θ/cos²θ = sin²θ tan²θ ✓", "RHS first", "Not true", "Use cot"],
         "Factor out sin²θ and use Pythagorean identity."),
        ("The identity cos⁴θ − sin⁴θ = cos 2θ can be verified by factoring the LHS as:", ["(cos²θ + sin²θ)²", "*(cos²θ − sin²θ)(cos²θ + sin²θ) = cos²θ − sin²θ = cos 2θ", "cos²θ(cos²θ − sin²θ)", "Cannot factor"],
         "Difference of squares: a⁴ − b⁴ = (a² − b²)(a² + b²) = (cos²θ − sin²θ)(1)."),
        ("A common first step is to express everything in terms of:", ["Tangent", "Secant", "*Sine and cosine", "Logarithms"],
         "Sin and cos are the building blocks of all trig identities."),
        ("If stuck, try:", ["Giving up", "*A different identity or technique (conjugate, factoring, common denominator)", "Assuming it's not an identity", "Adding 0"],
         "Multiple strategies exist — try a different approach."),
        ("Verify: (1 + tan²θ) cos²θ = 1:", ["*sec²θ · cos²θ = (1/cos²θ)(cos²θ) = 1 ✓", "Not an identity", "Only for θ = 0", "Cross-multiply"],
         "1 + tan²θ = sec²θ, and sec²θ cos²θ = 1."),
        ("Verifying identities strengthens understanding of:", ["Calculus", "*Relationships between trig functions", "Geometry only", "Arithmetic"],
         "Verification practice reinforces all the fundamental trig identities."),
    ]
)
lessons[k] = v

# ── 4.6 ──
k, v = build_lesson(4, 6, "Simplifying Expressions – Applications",
    "<h3>Simplifying Trig Expressions — Applications</h3>"
    "<p>Combining Pythagorean, reciprocal, quotient, and cofunction identities to simplify real-world and mathematical expressions.</p>"
    "<h4>Strategy Summary</h4>"
    "<ul><li>1. Convert to sin/cos.</li>"
    "<li>2. Apply Pythagorean identities.</li>"
    "<li>3. Factor or combine fractions.</li>"
    "<li>4. Cancel common factors.</li></ul>"
    "<p>Simplified expressions are easier to evaluate, differentiate, and integrate — essential skills for calculus.</p>",
    [
        ("Step 1: Convert to sin/cos", "Replace csc, sec, tan, cot with sin and cos expressions."),
        ("Step 2: Pythagorean Substitution", "Use sin²θ + cos²θ = 1 or variants to reduce terms."),
        ("Step 3: Factor/Combine", "Factor common terms or get a common denominator for fractions."),
        ("Step 4: Cancel", "Cancel common factors in numerator and denominator."),
        ("Goal of Simplification", "Reach a simpler equivalent expression — fewer terms, simpler functions."),
    ],
    [
        ("Simplify sin²θ + cos²θ + tan²θ:", ["1", "2", "*sec²θ (= 1 + tan²θ)", "tan²θ"],
         "1 + tan²θ = sec²θ."),
        ("Simplify: (sin θ + cos θ)²:", ["1", "sin²θ + cos²θ", "*1 + 2 sin θ cos θ", "sin 2θ"],
         "sin²θ + 2 sin θ cos θ + cos²θ = 1 + 2 sin θ cos θ."),
        ("Simplify: sec θ − cos θ:", ["1", "*sin θ tan θ", "cos θ", "csc θ"],
         "1/cos θ − cos θ = (1 − cos²θ)/cos θ = sin²θ/cos θ = sin θ tan θ."),
        ("Simplify: csc²θ − cot²θ:", ["0", "*1", "2", "csc θ"],
         "Pythagorean identity: csc²θ − cot²θ = 1."),
        ("Simplify: (1 + cos θ)(1 − cos θ):", ["1 − cos θ", "cos²θ", "*sin²θ", "1"],
         "Difference of squares: 1 − cos²θ = sin²θ."),
        ("Simplify: sin θ csc θ:", ["sin²θ", "0", "*1", "csc²θ"],
         "sin θ · (1/sin θ) = 1."),
        ("Simplify: tan θ / sin θ:", ["cos θ", "1", "*sec θ", "csc θ"],
         "(sin θ/cos θ)/sin θ = 1/cos θ = sec θ."),
        ("Simplify: cos θ · tan θ + sin θ:", ["cos θ", "tan θ", "*2 sin θ", "1"],
         "cos θ · (sin θ/cos θ) + sin θ = sin θ + sin θ = 2 sin θ."),
        ("Simplify: (sec²θ)(1 − sin²θ):", ["cos²θ", "0", "*1", "sec²θ"],
         "1 − sin²θ = cos²θ. sec²θ · cos²θ = 1."),
        ("Simplify: sin⁴θ − cos⁴θ:", ["1", "0", "*(sin²θ − cos²θ)", "(sin²θ + cos²θ)²"],
         "Factor: (sin²θ − cos²θ)(sin²θ + cos²θ) = sin²θ − cos²θ."),
        ("Simplify: (tan θ + cot θ) sin θ cos θ:", ["0", "*1", "sin θ + cos θ", "tan θ"],
         "(sin/cos + cos/sin)(sin cos) = sin² + cos² = 1."),
        ("Simplify: 1/(1 − sin θ) + 1/(1 + sin θ):", ["2", "2 sin θ", "*2 sec²θ", "2 csc²θ"],
         "Common denominator: (1+sinθ+1−sinθ)/(1−sin²θ) = 2/cos²θ = 2sec²θ."),
        ("Simplify: cos²θ/(1 − sin θ):", ["cos θ", "*1 + sin θ", "1 − sin θ", "sec θ"],
         "cos²θ = 1 − sin²θ = (1−sinθ)(1+sinθ). Divided by (1−sinθ) = 1+sinθ."),
        ("Simplify: (sin θ − cos θ)² + (sin θ + cos θ)²:", ["0", "1", "*2", "4"],
         "Expand: (sin²−2sincos+cos²)+(sin²+2sincos+cos²) = 1+1 = 2."),
        ("Simplify: cot θ + tan θ:", ["0", "1", "*csc θ sec θ (= 1/(sinθ cosθ))", "2"],
         "cosθ/sinθ + sinθ/cosθ = (cos²θ+sin²θ)/(sinθcosθ) = 1/(sinθcosθ)."),
        ("Simplify: sin³θ + sin θ cos²θ:", ["sin²θ", "*sin θ", "cos θ", "1"],
         "Factor: sinθ(sin²θ + cos²θ) = sinθ · 1 = sinθ."),
        ("Simplify: (1 − cos²θ)/sin θ:", ["cos θ", "1", "*sin θ", "tan θ"],
         "(1 − cos²θ) = sin²θ. sin²θ/sinθ = sinθ."),
        ("Simplify: sec θ csc θ / (sec θ + csc θ):", ["1", "*sin θ cos θ / (sin θ + cos θ) · (1/(sinθcosθ)) — need more info; simplest form is 1/(sinθ + cosθ)", "sec θ", "csc θ"],
         "sec csc = 1/(sincos). sec+csc = (sin+cos)/(sincos). Ratio = 1/(sin+cos)."),
        ("Simplifying trig expressions is important for:", ["*Calculus (easier differentiation/integration), solving equations, and cleaner solutions", "Only homework", "Nothing practical", "Geometry only"],
         "Simplified forms are easier to work with in all mathematical contexts."),
        ("Which identity is most frequently used in simplification?", ["Cofunction", "Quotient", "*Pythagorean (sin²+cos²=1)", "None"],
         "sin²θ + cos²θ = 1 is the most versatile tool."),
    ]
)
lessons[k] = v

# ── 4.7 ──
k, v = build_lesson(4, 7, "Physics Cases – Identities in Action",
    "<h3>Trig Identities in Physics</h3>"
    "<h4>Wave Superposition</h4>"
    "<p>When two waves overlap: A sin(ωt) + B cos(ωt) = R sin(ωt + φ) where R = √(A² + B²) and φ = arctan(B/A).</p>"
    "<h4>Projectile Range</h4>"
    "<p>R = v₀² sin(2θ)/g. The identity <b>sin(2θ) = 2 sin θ cos θ</b> shows that max range occurs at θ = 45°.</p>"
    "<h4>Simple Harmonic Motion</h4>"
    "<p>x(t) = A cos(ωt + φ) can be rewritten using sum identities as A cos φ cos ωt − A sin φ sin ωt.</p>",
    [
        ("Wave Superposition", "A sin(ωt) + B cos(ωt) = R sin(ωt + φ) with R = √(A²+B²)."),
        ("Projectile Range Formula", "R = v₀² sin(2θ)/g; uses double-angle identity."),
        ("sin 2θ = 2 sin θ cos θ", "Double-angle identity; shows max at θ = 45° for projectile range."),
        ("Simple Harmonic Motion", "x(t) = A cos(ωt + φ); expanded using sum identity for analysis."),
        ("Phase Combination", "φ = arctan(B/A) when combining A sin + B cos into a single sinusoid."),
    ],
    [
        ("A sin(ωt) + B cos(ωt) can be rewritten as:", ["A + B", "AB sin(ωt)", "*R sin(ωt + φ) where R = √(A²+B²)", "(A+B) sin(ωt + ωt)"],
         "Sum of a sine and cosine at the same frequency equals a single sinusoid."),
        ("In the combined form, R =", ["A + B", "A − B", "*√(A² + B²)", "AB"],
         "R is the amplitude of the combined wave."),
        ("The phase angle φ in the combined form:", ["φ = A/B", "*φ = arctan(B/A)", "φ = A + B", "φ = π"],
         "φ = arctan(B/A)."),
        ("The projectile range formula uses:", ["cos²θ", "*sin(2θ) = 2 sin θ cos θ", "tan θ", "csc θ"],
         "R = v₀² sin(2θ)/g relies on the double-angle identity."),
        ("Max range occurs when sin(2θ) is maximized, i.e., 2θ =", ["0", "*90° (so θ = 45°)", "180°", "θ = 90°"],
         "sin 90° = 1 is the maximum; 2θ = 90° → θ = 45°."),
        ("At θ = 45°, sin(2·45°) =", ["0", "1/2", "*1", "√2/2"],
         "sin 90° = 1."),
        ("sin(2θ) = 0 when:", ["θ = 45°", "*θ = 0° or 90°", "θ = 30°", "θ = 60°"],
         "2θ = 0° or 180° → θ = 0° or 90°."),
        ("SHM: x(t) = A cos(ωt + φ) expanded:", ["A sin(ωt) + A cos(ωt)", "*A cosφ cos(ωt) − A sinφ sin(ωt)", "A(sin ωt + cos ωt)", "A cos ω cos t"],
         "Using cos(α + β) = cosα cosβ − sinα sinβ."),
        ("In physics, combining perpendicular oscillations with 90° phase difference creates:", ["A straight line", "*Circular motion", "No motion", "A square"],
         "x = A cos ωt, y = A sin ωt traces a circle."),
        ("The kinetic energy of SHM involves sin²(ωt), which can be rewritten using:", ["Quotient identity", "*cos(2ωt) = 1 − 2sin²(ωt) → sin² = (1−cos2ωt)/2", "Reciprocal identity", "No identity"],
         "The power-reduction identity simplifies energy calculations."),
        ("Two sound waves: 3sin(t) + 4cos(t). The combined amplitude is:", ["7", "1", "*5", "3.5"],
         "R = √(9 + 16) = √25 = 5."),
        ("For the combined wave 3sin(t) + 4cos(t), the phase φ =", ["arctan(3/4)", "*arctan(4/3)", "arctan(1)", "π/4"],
         "φ = arctan(B/A) = arctan(4/3)."),
        ("In electric circuits, V = V₀ sin(ωt) and I = I₀ sin(ωt + φ). The power uses:", ["No identity", "*Product-to-sum: sin α sin(α+φ) expansion", "Pythagorean", "Cofunction"],
         "P = VI involves products of sines, simplified with product-to-sum identities."),
        ("Trig identities help convert between displacement and velocity in SHM because:", ["They add constants", "*Derivatives of sin/cos produce the other, and identities relate their squares", "They eliminate trig", "They add amplitude"],
         "d/dt(cos ωt) = −ω sin ωt; identity sin²+cos² = 1 relates displacement and velocity."),
        ("If 5sin(ωt) + 5cos(ωt) = R sin(ωt + φ), then R =", ["10", "*5√2", "5", "25"],
         "R = √(25 + 25) = √50 = 5√2."),
        ("The φ for 5sin + 5cos is:", ["0", "*π/4 (= arctan(1))", "π/2", "π/3"],
         "arctan(5/5) = arctan(1) = π/4."),
        ("In optics, interference patterns use:", ["*Superposition with trig identities", "No math", "Only geometry", "Only algebra"],
         "Light wave interference is modeled using sine wave superposition and trig identities."),
        ("sin²θ + cos²θ = 1 in a physics context means:", ["Energy is zero", "*Total energy is conserved (kinetic + potential)", "No motion", "Infinite energy"],
         "In SHM, sin² corresponds to KE and cos² to PE; their sum is constant."),
        ("An engineer decomposes vibration data using trig identities to:", ["*Identify component frequencies and amplitudes", "Increase vibration", "Create noise", "Measure temperature"],
         "Decomposition via trig identities reveals the frequency content of vibrations."),
        ("Product-to-sum identities are used in physics for:", ["*Converting products of trig functions (e.g., in power calculations) to sums", "Adding vectors", "Measuring mass", "No purpose"],
         "Products of sinusoids appear in power and modulation; identities convert them to sums for analysis."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 4: wrote {len(lessons)} lessons")
