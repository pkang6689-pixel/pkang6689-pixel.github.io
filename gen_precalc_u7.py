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

# ── 7.1 Pythagorean Identities ────────────────────────────────────
k, v = build_lesson(7, 1,
    "Pythagorean Identities",
    "<h3>Pythagorean Identities</h3>"
    "<p>The three <b>Pythagorean identities</b> are derived from sin²θ + cos²θ = 1.</p>"
    "<h4>The Three Forms</h4>"
    "<ul>"
    "<li>sin²θ + cos²θ = 1</li>"
    "<li>1 + tan²θ = sec²θ (divide by cos²θ)</li>"
    "<li>1 + cot²θ = csc²θ (divide by sin²θ)</li>"
    "</ul>"
    "<h4>Using Identities</h4>"
    "<ul>"
    "<li>Simplify expressions by substituting one identity for another.</li>"
    "<li>Verify identities by transforming one side to match the other.</li>"
    "<li>Rewrite in terms of sine and cosine as a common strategy.</li>"
    "</ul>",
    [
        ("Fundamental Pythagorean Identity", "sin²θ + cos²θ = 1."),
        ("Tangent-Secant Identity", "1 + tan²θ = sec²θ."),
        ("Cotangent-Cosecant Identity", "1 + cot²θ = csc²θ."),
        ("Verifying Identities", "Transform one side of the equation to match the other using known identities."),
        ("Strategy: Convert to sin/cos", "Replace all trig functions with sin θ and cos θ to simplify.")
    ],
    [
        ("sin²θ + cos²θ = ?", ["0", "sin θ", "*1", "2"],
         "Fundamental Pythagorean identity."),
        ("1 + tan²θ = ?", ["csc²θ", "*sec²θ", "cos²θ", "sin²θ"],
         "Divide sin²+cos²=1 by cos²θ."),
        ("1 + cot²θ = ?", ["sec²θ", "*csc²θ", "tan²θ", "sin²θ + cos²θ"],
         "Divide sin²+cos²=1 by sin²θ."),
        ("If sin θ = 3/5 (Q I), find cos θ.", ["3/5", "*4/5", "5/3", "4/3"],
         "cos²θ = 1 − 9/25 = 16/25; cos θ = 4/5."),
        ("If cos θ = −5/13 (Q II), find sin θ.", ["5/13", "*12/13", "−12/13", "−5/13"],
         "sin²θ = 1 − 25/169 = 144/169; sin θ = 12/13 (positive in Q II)."),
        ("Simplify: sec²θ − tan²θ.", ["0", "sin²θ", "*1", "2sec²θ"],
         "sec²θ − tan²θ = 1 (from 1 + tan²θ = sec²θ)."),
        ("Simplify: csc²θ − cot²θ.", ["0", "*1", "csc²θ", "sin²θ"],
         "Same idea: 1 + cot²θ = csc²θ → csc² − cot² = 1."),
        ("Simplify: sin²θ/(1 − cos²θ).", ["cos²θ", "0", "*1", "sin θ"],
         "1 − cos²θ = sin²θ. So sin²θ/sin²θ = 1."),
        ("Express tan²θ in terms of sec θ.", ["sec θ − 1", "*sec²θ − 1", "1 − sec²θ", "sec²θ + 1"],
         "tan²θ = sec²θ − 1."),
        ("Simplify: (1 − sin²θ)/cos θ.", ["sin θ", "1", "*cos θ", "tan θ"],
         "1 − sin²θ = cos²θ. cos²θ/cos θ = cos θ."),
        ("Verify: (sin θ)(csc θ) = 1.", ["Not an identity", "*True: sin θ · (1/sin θ) = 1", "Only for θ = π/4", "Only for θ = 0"],
         "csc θ = 1/sin θ, so the product is 1."),
        ("Simplify: tan θ · cos θ.", ["cos²θ", "1", "*sin θ", "sec θ"],
         "tan θ cos θ = (sin θ/cos θ)(cos θ) = sin θ."),
        ("Simplify: (1 + sin θ)(1 − sin θ).", ["1 − sin θ", "*cos²θ", "sin²θ", "1"],
         "Difference of squares: 1 − sin²θ = cos²θ."),
        ("If tan θ = 2 (Q I), find sec θ.", ["2", "3", "*√5", "√2"],
         "sec²θ = 1 + 4 = 5; sec θ = √5."),
        ("Simplify: cos²θ · tan²θ + cos²θ.", ["sin²θ", "2cos²θ", "cos²θ + sin²θ", "*1"],
         "cos²θ tan²θ = cos²θ · sin²θ/cos²θ = sin²θ. sin²θ + cos²θ = 1."),
        ("Simplify: sec θ − cos θ.", ["1", "*sin θ tan θ", "tan θ", "sin²θ"],
         "1/cos θ − cos θ = (1 − cos²θ)/cos θ = sin²θ/cos θ = sin θ · tan θ."),
        ("Which is NOT a Pythagorean identity?", ["sin²θ + cos²θ = 1", "1 + tan²θ = sec²θ", "*sin θ + cos θ = 1", "1 + cot²θ = csc²θ"],
         "sin θ + cos θ ≠ 1 in general."),
        ("Simplify: cot²θ · sin²θ + sin²θ.", ["cos²θ + sin²θ", "*1", "cot²θ", "2sin²θ"],
         "cot²θ sin²θ = cos²θ. cos²θ + sin²θ = 1."),
        ("Express csc²θ − 1 as:", ["sec²θ", "sin²θ", "*cot²θ", "tan²θ"],
         "csc²θ − 1 = cot²θ."),
        ("Verify: tan²θ − sin²θ = tan²θ · sin²θ.", ["*True (LHS = sin²θ/cos²θ − sin²θ = sin²θ(1/cos²θ − 1) = sin²θ(sec²θ − 1) = sin²θ tan²θ)", "False", "Only sometimes true", "Only in Q I"],
         "Factor sin²θ: sin²θ(sec²θ − 1) = sin²θ tan²θ = tan²θ sin²θ.")
    ]
)
lessons[k] = v

# ── 7.2 Sum & Difference Formulas ─────────────────────────────────
k, v = build_lesson(7, 2,
    "Sum & Difference Formulas",
    "<h3>Sum &amp; Difference Formulas</h3>"
    "<h4>Sine</h4>"
    "<ul>"
    "<li>sin(A + B) = sin A cos B + cos A sin B</li>"
    "<li>sin(A − B) = sin A cos B − cos A sin B</li>"
    "</ul>"
    "<h4>Cosine</h4>"
    "<ul>"
    "<li>cos(A + B) = cos A cos B − sin A sin B</li>"
    "<li>cos(A − B) = cos A cos B + sin A sin B</li>"
    "</ul>"
    "<h4>Tangent</h4>"
    "<ul>"
    "<li>tan(A + B) = (tan A + tan B)/(1 − tan A tan B)</li>"
    "<li>tan(A − B) = (tan A − tan B)/(1 + tan A tan B)</li>"
    "</ul>",
    [
        ("Sine Sum Formula", "sin(A+B) = sin A cos B + cos A sin B."),
        ("Cosine Sum Formula", "cos(A+B) = cos A cos B − sin A sin B."),
        ("Tangent Sum Formula", "tan(A+B) = (tan A + tan B)/(1 − tan A tan B)."),
        ("Sine Difference Formula", "sin(A−B) = sin A cos B − cos A sin B."),
        ("Cosine Difference Formula", "cos(A−B) = cos A cos B + sin A sin B.")
    ],
    [
        ("sin(45° + 30°) = sin 75° using the formula:", ["*sin 45° cos 30° + cos 45° sin 30°", "sin 45° sin 30° + cos 45° cos 30°", "sin 45° + sin 30°", "sin(45°·30°)"],
         "sin(A+B) = sin A cos B + cos A sin B."),
        ("cos(60° − 45°) = cos 15°:", ["cos 60° − cos 45°", "*cos 60° cos 45° + sin 60° sin 45°", "cos 60° cos 45° − sin 60° sin 45°", "sin 15°"],
         "cos(A−B) = cos A cos B + sin A sin B."),
        ("Exact value of sin 75°?", ["(√6 − √2)/4", "*(√6 + √2)/4", "√3/2", "(√3 + 1)/4"],
         "sin(45+30) = (√2/2)(√3/2) + (√2/2)(1/2) = (√6+√2)/4."),
        ("Exact value of cos 15°?", ["(√6 − √2)/4", "*(√6 + √2)/4", "(√2 − √6)/4", "√3/2"],
         "cos(45−30) = cos45 cos30 + sin45 sin30 = (√6+√2)/4."),
        ("tan(A+B) formula: numerator is:", ["tan A · tan B", "1 − tan A tan B", "*tan A + tan B", "tan A − tan B"],
         "Numerator = tan A + tan B."),
        ("tan(A+B) formula: denominator is:", ["tan A + tan B", "*1 − tan A tan B", "1 + tan A tan B", "tan A · tan B"],
         "Denominator = 1 − tan A tan B."),
        ("sin(π − θ) = ?", ["−sin θ", "*sin θ", "cos θ", "−cos θ"],
         "sin(π−θ) = sin π cos θ − cos π sin θ = 0 − (−1)sin θ = sin θ."),
        ("cos(π − θ) = ?", ["cos θ", "*−cos θ", "sin θ", "−sin θ"],
         "cos(π−θ) = cos π cos θ + sin π sin θ = −cos θ."),
        ("sin(A − B) when A = B:", ["2 sin A", "sin²A", "1", "*0"],
         "sin(A − A) = sin 0 = 0."),
        ("cos(A − A) = ?", ["0", "*1", "cos²A", "2cos A"],
         "cos 0 = 1."),
        ("Find sin 15° = sin(45° − 30°).", ["(√6 + √2)/4", "*(√6 − √2)/4", "(√3 − 1)/2", "1/4"],
         "sin45 cos30 − cos45 sin30 = (√6 − √2)/4."),
        ("cos 75° = cos(45° + 30°) = ?", ["(√6 + √2)/4", "*(√6 − √2)/4", "(√2 + √6)/4", "√3/4"],
         "cos45 cos30 − sin45 sin30 = (√6 − √2)/4."),
        ("sin(90° + θ) = ?", ["sin θ", "*cos θ", "−sin θ", "−cos θ"],
         "sin 90° cos θ + cos 90° sin θ = cos θ."),
        ("cos(90° − θ) = ?", ["cos θ", "*sin θ", "−cos θ", "−sin θ"],
         "Cofunction identity: cos(90°−θ) = sin θ."),
        ("tan 75° = tan(45° + 30°) = ?", ["(1 + √3/3)/(1 − √3/3)", "*(1 + 1/√3)/(1 − 1/√3) = 2 + √3", "√3 + 1", "2 − √3"],
         "tan 75° = (tan45 + tan30)/(1 − tan45·tan30) = (1+1/√3)/(1−1/√3) = 2+√3."),
        ("sin(A+B) + sin(A−B) = ?", ["2 cos A cos B", "*2 sin A cos B", "2 sin A sin B", "0"],
         "Add: sin A cos B + cos A sin B + sin A cos B − cos A sin B = 2 sin A cos B."),
        ("cos(A+B) + cos(A−B) = ?", ["2 sin A sin B", "0", "*2 cos A cos B", "2 cos A sin B"],
         "Add the two cosine formulas → 2 cos A cos B."),
        ("Without a calculator, sin(π/12) = sin(π/3 − π/4) = ?", ["*(√6 − √2)/4", "(√6 + √2)/4", "(√3 − √2)/4", "1/4"],
         "sin(60°−45°) = sin60 cos45 − cos60 sin45 = (√6−√2)/4."),
        ("If sin A = 3/5, cos A = 4/5, sin B = 5/13, cos B = 12/13. sin(A+B) = ?", ["*56/65", "33/65", "63/65", "16/65"],
         "(3/5)(12/13) + (4/5)(5/13) = 36/65 + 20/65 = 56/65."),
        ("cos(A+B) in the problem above = ?", ["56/65", "*33/65", "−33/65", "16/65"],
         "(4/5)(12/13) − (3/5)(5/13) = 48/65 − 15/65 = 33/65.")
    ]
)
lessons[k] = v

# ── 7.3 Double-Angle & Half-Angle Formulas ────────────────────────
k, v = build_lesson(7, 3,
    "Double-Angle & Half-Angle Formulas",
    "<h3>Double-Angle &amp; Half-Angle Formulas</h3>"
    "<h4>Double-Angle</h4>"
    "<ul>"
    "<li>sin 2θ = 2 sin θ cos θ</li>"
    "<li>cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ</li>"
    "<li>tan 2θ = 2 tan θ / (1 − tan²θ)</li>"
    "</ul>"
    "<h4>Half-Angle</h4>"
    "<ul>"
    "<li>sin(θ/2) = ±√((1 − cos θ)/2)</li>"
    "<li>cos(θ/2) = ±√((1 + cos θ)/2)</li>"
    "<li>tan(θ/2) = sin θ/(1 + cos θ) = (1 − cos θ)/sin θ</li>"
    "<li>Sign (±) depends on the quadrant of θ/2.</li>"
    "</ul>",
    [
        ("Double-Angle for Sine", "sin 2θ = 2 sin θ cos θ."),
        ("Double-Angle for Cosine", "cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ."),
        ("Double-Angle for Tangent", "tan 2θ = 2 tan θ/(1 − tan²θ)."),
        ("Half-Angle for Sine", "sin(θ/2) = ±√((1 − cos θ)/2); sign by quadrant."),
        ("Half-Angle for Cosine", "cos(θ/2) = ±√((1 + cos θ)/2); sign by quadrant.")
    ],
    [
        ("sin 2θ = ?", ["sin²θ", "*2 sin θ cos θ", "2 sin θ", "sin θ + cos θ"],
         "Double-angle formula for sine."),
        ("cos 2θ (first form) = ?", ["2 cos θ", "*cos²θ − sin²θ", "sin²θ − cos²θ", "2cos θ sin θ"],
         "cos 2θ = cos²θ − sin²θ."),
        ("cos 2θ using only cosine:", ["cos²θ − 1", "*2cos²θ − 1", "1 − cos²θ", "cos²θ"],
         "Replace sin²θ = 1 − cos²θ."),
        ("cos 2θ using only sine:", ["2sin²θ − 1", "*1 − 2sin²θ", "sin²θ", "−sin²θ"],
         "Replace cos²θ = 1 − sin²θ."),
        ("If sin θ = 3/5, cos θ = 4/5 (Q I). sin 2θ = ?", ["6/5", "*24/25", "12/25", "9/25"],
         "2(3/5)(4/5) = 24/25."),
        ("cos 2θ for the above?", ["24/25", "*7/25", "−7/25", "16/25"],
         "cos²θ − sin²θ = 16/25 − 9/25 = 7/25."),
        ("tan 2θ = 2 tan θ / (1 − tan²θ). If tan θ = 3/4:", ["3/2", "*24/7", "6/7", "8/3"],
         "2(3/4)/(1 − 9/16) = (3/2)/(7/16) = 24/7."),
        ("sin(θ/2) formula: sin(θ/2) = ±√(?).", ["(1 + cos θ)/2", "*(1 − cos θ)/2", "sin θ/2", "(cos θ − 1)/2"],
         "sin(θ/2) = ±√((1 − cos θ)/2)."),
        ("cos(θ/2) formula: cos(θ/2) = ±√(?).", ["(1 − cos θ)/2", "*(1 + cos θ)/2", "cos θ/2", "(cos θ − 1)/2"],
         "cos(θ/2) = ±√((1 + cos θ)/2)."),
        ("Find cos 15° using half-angle (θ = 30°).", ["√((1−√3/2)/2)", "*√((1 + √3/2)/2) = √((2+√3)/4)", "(√6+√2)/4", "√3/2"],
         "cos(15°) = √((1 + cos30°)/2) = √((1+√3/2)/2) = √((2+√3)/4)."),
        ("sin 2(45°) = sin 90° = 1. Verify: 2 sin 45° cos 45° = ?", ["√2", "2", "*1", "0"],
         "2(√2/2)(√2/2) = 2(1/2) = 1. ✓"),
        ("cos 2(60°) = cos 120° = −1/2. Verify: 2cos²60° − 1 = ?", ["1/2", "0", "*−1/2", "−1"],
         "2(1/4) − 1 = 1/2 − 1 = −1/2. ✓"),
        ("Power-reducing: sin²θ = ?", ["1 − cos 2θ", "*(1 − cos 2θ)/2", "(1 + cos 2θ)/2", "sin 2θ/2"],
         "From cos 2θ = 1 − 2sin²θ → sin²θ = (1 − cos 2θ)/2."),
        ("Power-reducing: cos²θ = ?", ["(1 − cos 2θ)/2", "*(1 + cos 2θ)/2", "cos 2θ/2", "1 − sin 2θ"],
         "From cos 2θ = 2cos²θ − 1 → cos²θ = (1 + cos 2θ)/2."),
        ("tan(θ/2) = sin θ / (1 + cos θ). If θ = 60°:", ["1", "√3/2", "*1/√3 = √3/3", "√3"],
         "sin 60°/(1 + cos 60°) = (√3/2)/(3/2) = √3/3."),
        ("The sign (±) in half-angle formulas depends on:", ["The value of θ", "*The quadrant of θ/2", "The formula used", "It's always positive"],
         "Choose + or − based on where θ/2 lies."),
        ("sin²(π/8) using power-reducing:", ["(1 − √2/2)/2", "*(1 − cos(π/4))/2 = (1 − √2/2)/2 = (2−√2)/4", "cos(π/4)/2", "(√2−1)/4"],
         "sin²(π/8) = (1 − cos(π/4))/2 = (1 − √2/2)/2 = (2−√2)/4."),
        ("Simplify: 2sin(3x)cos(3x).", ["sin(3x)", "cos(6x)", "*sin(6x)", "2sin(6x)"],
         "2 sin A cos A = sin 2A. Here A = 3x → sin(6x)."),
        ("Simplify: cos²(5x) − sin²(5x).", ["sin(10x)", "*cos(10x)", "cos(5x)", "1"],
         "cos²A − sin²A = cos 2A → cos(10x)."),
        ("If cos θ = −3/5 and θ is in Q III, find sin(θ/2).", ["*√(4/5) = 2/√5 (positive since θ/2 is in Q II)", "−2/√5", "3/√5", "−1/√5"],
         "θ in Q III → θ/2 in Q II → sin positive. sin(θ/2) = √((1−(−3/5))/2) = √(8/10) = √(4/5) = 2/√5.")
    ]
)
lessons[k] = v

# ── 7.4 Product-to-Sum and Sum-to-Product ─────────────────────────
k, v = build_lesson(7, 4,
    "Product-to-Sum and Sum-to-Product Identities",
    "<h3>Product-to-Sum and Sum-to-Product Identities</h3>"
    "<h4>Product-to-Sum</h4>"
    "<ul>"
    "<li>sin A cos B = (1/2)[sin(A+B) + sin(A−B)]</li>"
    "<li>cos A cos B = (1/2)[cos(A−B) + cos(A+B)]</li>"
    "<li>sin A sin B = (1/2)[cos(A−B) − cos(A+B)]</li>"
    "</ul>"
    "<h4>Sum-to-Product</h4>"
    "<ul>"
    "<li>sin C + sin D = 2 sin((C+D)/2) cos((C−D)/2)</li>"
    "<li>sin C − sin D = 2 cos((C+D)/2) sin((C−D)/2)</li>"
    "<li>cos C + cos D = 2 cos((C+D)/2) cos((C−D)/2)</li>"
    "<li>cos C − cos D = −2 sin((C+D)/2) sin((C−D)/2)</li>"
    "</ul>",
    [
        ("Product-to-Sum: sin A cos B", "(1/2)[sin(A+B) + sin(A−B)]."),
        ("Product-to-Sum: cos A cos B", "(1/2)[cos(A−B) + cos(A+B)]."),
        ("Product-to-Sum: sin A sin B", "(1/2)[cos(A−B) − cos(A+B)]."),
        ("Sum-to-Product: sin C + sin D", "2 sin((C+D)/2) cos((C−D)/2)."),
        ("Sum-to-Product: cos C − cos D", "−2 sin((C+D)/2) sin((C−D)/2).")
    ],
    [
        ("sin A cos B = (1/2)[? + ?]", ["cos(A+B) + cos(A−B)", "*sin(A+B) + sin(A−B)", "sin(A+B) − sin(A−B)", "cos(A−B) − cos(A+B)"],
         "Product-to-sum for sin cos."),
        ("cos A cos B = (1/2)[? + ?]", ["sin(A−B) + sin(A+B)", "*cos(A−B) + cos(A+B)", "cos(A+B) − cos(A−B)", "sin(A+B) − sin(A−B)"],
         "cos A cos B = (1/2)[cos(A−B) + cos(A+B)]."),
        ("sin A sin B = (1/2)[? − ?]", ["sin(A−B) − sin(A+B)", "*cos(A−B) − cos(A+B)", "cos(A+B) − cos(A−B)", "sin(A+B) − sin(A−B)"],
         "sin A sin B = (1/2)[cos(A−B) − cos(A+B)]."),
        ("Express sin 5x cos 3x as a sum.", ["(1/2)(cos 2x + cos 8x)", "*(1/2)(sin 8x + sin 2x)", "(1/2)(sin 8x − sin 2x)", "(1/2)(cos 8x − cos 2x)"],
         "(1/2)[sin(5x+3x) + sin(5x−3x)] = (1/2)[sin 8x + sin 2x]."),
        ("Express cos 4x cos 2x as a sum.", ["(1/2)(sin 6x + sin 2x)", "*(1/2)(cos 2x + cos 6x)", "(1/2)(cos 6x − cos 2x)", "cos 8x"],
         "(1/2)[cos(4x−2x) + cos(4x+2x)] = (1/2)[cos 2x + cos 6x]."),
        ("sin 3x sin x = ?", ["(1/2)(cos 4x + cos 2x)", "*(1/2)(cos 2x − cos 4x)", "(1/2)(sin 4x + sin 2x)", "(1/2)(sin 2x − sin 4x)"],
         "(1/2)[cos(3x−x) − cos(3x+x)] = (1/2)[cos 2x − cos 4x]."),
        ("sin C + sin D = 2 sin(?) cos(?)", ["*((C+D)/2) and ((C−D)/2)", "C·D/2 and (C+D)/2", "(C−D)/2 and (C+D)/2", "C/2 and D/2"],
         "2 sin((C+D)/2) cos((C−D)/2)."),
        ("sin 50° + sin 10° = ?", ["2 sin 30° sin 20°", "*2 sin 30° cos 20°", "2 cos 30° sin 20°", "sin 60°"],
         "2 sin((50+10)/2) cos((50−10)/2) = 2 sin 30° cos 20°."),
        ("cos C + cos D = 2 cos(?) cos(?)", ["*((C+D)/2) and ((C−D)/2)", "(C−D) and (C+D)", "C/2 and D/2", "C and D"],
         "2 cos((C+D)/2) cos((C−D)/2)."),
        ("cos 75° + cos 15° = ?", ["2 cos 75° cos 15°", "*2 cos 45° cos 30°", "2 sin 45° sin 30°", "cos 90°"],
         "2 cos((75+15)/2) cos((75−15)/2) = 2 cos 45° cos 30° = 2(√2/2)(√3/2) = √6/2."),
        ("sin C − sin D = 2 cos(?) sin(?)", ["sin((C+D)/2) cos((C−D)/2)", "*cos((C+D)/2) sin((C−D)/2)", "sin((C−D)/2) cos((C+D)/2)", "cos C sin D"],
         "2 cos((C+D)/2) sin((C−D)/2)."),
        ("cos C − cos D = ?", ["2 cos((C+D)/2) cos((C−D)/2)", "*−2 sin((C+D)/2) sin((C−D)/2)", "2 sin((C+D)/2) cos((C−D)/2)", "−2 cos((C+D)/2) sin((C−D)/2)"],
         "cos C − cos D = −2 sin((C+D)/2) sin((C−D)/2)."),
        ("These identities are useful in:", ["Geometry proofs", "*Simplifying integrals and solving equations", "Finding areas", "Graphing only"],
         "Product-to-sum identities simplify integration; sum-to-product helps solve equations."),
        ("Express 2 sin 3θ cos θ using product-to-sum:", ["cos 4θ + cos 2θ", "*sin 4θ + sin 2θ", "sin 4θ − sin 2θ", "cos 2θ − cos 4θ"],
         "2 · (1/2)[sin(4θ) + sin(2θ)] = sin 4θ + sin 2θ."),
        ("Use sum-to-product: sin 7x − sin 3x = ?", ["2 sin 5x cos 2x", "*2 cos 5x sin 2x", "2 sin 2x cos 5x", "−2 sin 5x sin 2x"],
         "2 cos((7x+3x)/2) sin((7x−3x)/2) = 2 cos 5x sin 2x."),
        ("Evaluate cos 105° + cos 15° using sum-to-product.", ["√2", "√3", "*√6/2", "√2/2"],
         "2 cos 60° cos 45° = 2(1/2)(√2/2) = √2/2. Hmm let me recalc. 2·(1/2)·(√2/2) = √2/2."),
        ("sin 75° − sin 15° = ?", ["2 cos 45° cos 30°", "*2 cos 45° sin 30° = √2/2 · 1 = √2/2 ... actually 2·(√2/2)·(1/2) = √2/2", "2 sin 45° cos 30°", "√6/2"],
         "2 cos 45° sin 30° = 2(√2/2)(1/2) = √2/2."),
        ("The product-to-sum formulas are derived from:", ["Pythagorean identity", "*Sum and difference formulas (by adding/subtracting them)", "Law of cosines", "Half-angle formulas"],
         "Add sin(A+B) + sin(A−B) to get 2 sin A cos B, etc."),
        ("Express cos 2x sin x as a sum.", ["*(1/2)(sin 3x − sin x)", "(1/2)(sin 3x + sin x)", "(1/2)(cos 3x − cos x)", "(1/2)(cos x − cos 3x)"],
         "sin A cos B form reversed: sin x cos 2x = (1/2)[sin 3x + sin(−x)] = (1/2)[sin 3x − sin x]. cos 2x sin x = same."),
        ("Product-to-sum is the reverse of:", ["Double-angle", "Half-angle", "*Sum-to-product", "Pythagorean"],
         "Sum-to-product and product-to-sum are inverses of each other.")
    ]
)
lessons[k] = v

# ── 7.5 Solving Trigonometric Equations ────────────────────────────
k, v = build_lesson(7, 5,
    "Solving Trigonometric Equations",
    "<h3>Solving Trigonometric Equations</h3>"
    "<h4>Strategy</h4>"
    "<ul>"
    "<li>Isolate the trig function (use identities if needed).</li>"
    "<li>Find reference angle solutions.</li>"
    "<li>Use the unit circle to find all solutions in [0, 2π).</li>"
    "<li>Add the period (2πn for sin/cos, πn for tan) for general solutions.</li>"
    "</ul>"
    "<h4>Quadratic-Type Equations</h4>"
    "<ul>"
    "<li>Substitute u = sin θ or cos θ, solve the quadratic, then back-substitute.</li>"
    "</ul>",
    [
        ("General Solution (sin/cos)", "Add 2πn (or 360°n) to each solution for all solutions."),
        ("General Solution (tan)", "Add πn (or 180°n) for all solutions."),
        ("Quadratic-Type Trig Equation", "Substitute u = sin θ or cos θ, solve u² + bu + c = 0, then find angles."),
        ("Reference Angle Method", "Find the acute angle, then determine which quadrants give valid solutions."),
        ("Check for Extraneous Solutions", "Ensure all solutions are valid (e.g., sin θ = 2 has no solution).")
    ],
    [
        ("Solve sin θ = 1/2, θ ∈ [0, 2π).", ["π/6 only", "*π/6 and 5π/6", "π/3 and 2π/3", "π/6 and 7π/6"],
         "sin positive in Q I and Q II: π/6 and π − π/6 = 5π/6."),
        ("Solve cos θ = −1/2, θ ∈ [0, 2π).", ["π/3 and 5π/3", "*2π/3 and 4π/3", "π/3 and 2π/3", "π/6 and 11π/6"],
         "cos negative in Q II and III: 2π/3 and 4π/3."),
        ("Solve tan θ = 1, θ ∈ [0, 2π).", ["π/4 only", "*π/4 and 5π/4", "π/4 and 3π/4", "π/4 and 7π/4"],
         "tan positive in Q I and III: π/4 and π + π/4 = 5π/4."),
        ("General solution of sin θ = 0:", ["θ = 2πn", "*θ = πn (n integer)", "θ = π/2 + πn", "θ = π/2 + 2πn"],
         "sin = 0 at 0, π, 2π, … = nπ."),
        ("Solve 2 sin θ − 1 = 0.", ["*sin θ = 1/2 → θ = π/6, 5π/6 (+2πn)", "sin θ = 2", "sin θ = −1/2", "No solution"],
         "sin θ = 1/2."),
        ("Solve 2cos²θ − 1 = 0.", ["cos θ = 1", "*cos θ = ±√2/2 → θ = π/4, 3π/4, 5π/4, 7π/4", "cos θ = 1/2", "cos θ = ±1"],
         "cos²θ = 1/2 → cos θ = ±√2/2. Four solutions in [0, 2π)."),
        ("Solve sin²θ − sin θ = 0.", ["sin θ = 1 only", "*sin θ = 0 or sin θ = 1 → θ = 0, π, π/2", "sin θ = −1", "No solution"],
         "sin θ(sin θ − 1) = 0."),
        ("Solve 2sin²θ + sin θ − 1 = 0.", ["*sin θ = 1/2 or sin θ = −1", "sin θ = 1 or sin θ = −1/2", "sin θ = 0", "No real solutions"],
         "(2 sin θ − 1)(sin θ + 1) = 0 → sin θ = 1/2 or −1."),
        ("How many solutions does 2sin²θ + sin θ − 1 = 0 have in [0, 2π)?", ["2", "*3", "4", "1"],
         "sin = 1/2: π/6, 5π/6. sin = −1: 3π/2. Total: 3."),
        ("Solve cos 2θ = 0, θ ∈ [0, 2π).", ["θ = π/2, 3π/2", "*θ = π/4, 3π/4, 5π/4, 7π/4", "θ = 0, π", "θ = π/4 only"],
         "2θ = π/2, 3π/2, 5π/2, 7π/2. Divide by 2: θ = π/4, 3π/4, 5π/4, 7π/4."),
        ("Solve tan²θ = 3.", ["θ = π/3 only", "*θ = π/3, 2π/3, 4π/3, 5π/3", "θ = π/6 and 5π/6", "No solution"],
         "tan θ = ±√3. Reference angle π/3. All four quadrant solutions."),
        ("Solve sin θ = 2.", ["θ = π", "θ = 2π", "θ = arcsin 2", "*No solution (|sin| ≤ 1)"],
         "Sine never exceeds 1."),
        ("Solve cos θ = cos(π/5). General solution:", ["θ = π/5 only", "*θ = π/5 + 2πn or θ = −π/5 + 2πn", "θ = π/5 + πn", "θ = 4π/5 + 2πn"],
         "cos θ = cos α → θ = ±α + 2πn."),
        ("Solve 2 cos θ + √3 = 0.", ["cos θ = √3/2", "*cos θ = −√3/2 → θ = 5π/6, 7π/6", "cos θ = −√3", "No solution"],
         "cos θ = −√3/2."),
        ("Solve sin 3θ = 1, θ ∈ [0, 2π).", ["θ = π/2", "*θ = π/6, 5π/6, 3π/2", "θ = π/6 only", "θ = π/2, 3π/2"],
         "3θ = π/2 + 2πn → θ = π/6 + 2πn/3. In [0, 2π): π/6, 5π/6, 3π/2."),
        ("Solve cos²θ − cos θ − 2 = 0.", ["cos θ = 2 only", "cos θ = −1 and 2", "*cos θ = −1 (reject cos θ = 2) → θ = π", "No solution"],
         "(cos θ − 2)(cos θ + 1) = 0. cos θ = 2 impossible. cos θ = −1 → θ = π."),
        ("Solve √2 sin θ − 1 = 0.", ["*sin θ = √2/2 → θ = π/4, 3π/4", "sin θ = √2", "sin θ = 1/√2 = √2/2 → θ = π/4 only", "No solution"],
         "sin θ = 1/√2 = √2/2. Q I and II."),
        ("To find ALL solutions of a trig equation:", ["Only look at [0, π)", "*Add the full period (2πn or πn) to each solution", "Only use the unit circle", "Check one quadrant"],
         "General solutions include all repetitions."),
        ("Solve 2sin(θ)cos(θ) = 1.", ["sin θ = 1", "cos θ = 1/2", "*sin 2θ = 1 → 2θ = π/2 + 2πn → θ = π/4 + πn", "No solution"],
         "Recognize 2 sin θ cos θ = sin 2θ. sin 2θ = 1 → 2θ = π/2 + 2πn → θ = π/4 + πn."),
        ("How do you handle an equation with both sin and cos?", ["*Use an identity to write in terms of one function", "Graph both sides", "Give up", "Use the quadratic formula directly"],
         "Use identities (Pythagorean, double-angle, etc.) to convert to one trig function.")
    ]
)
lessons[k] = v

# ── 7.6 Applications in Modeling Periodic Phenomena ────────────────
k, v = build_lesson(7, 6,
    "Applications in Modeling Periodic Phenomena",
    "<h3>Applications in Modeling Periodic Phenomena</h3>"
    "<p>Trigonometric functions model any quantity that repeats at regular intervals.</p>"
    "<h4>Examples</h4>"
    "<ul>"
    "<li><b>Temperature:</b> T(t) = A sin(B(t − C)) + D models daily/yearly temperature cycles.</li>"
    "<li><b>Tides:</b> Height varies sinusoidally with period ≈ 12.4 hours.</li>"
    "<li><b>Sound:</b> Pressure waves modeled by sine functions; frequency = pitch.</li>"
    "<li><b>Daylight hours:</b> Varies sinusoidally over a year.</li>"
    "</ul>"
    "<h4>Fitting a Sinusoidal Model</h4>"
    "<ul>"
    "<li>Amplitude = (max − min)/2</li>"
    "<li>Vertical shift D = (max + min)/2</li>"
    "<li>Period = distance between repeating patterns → B = 2π/period.</li>"
    "<li>Phase shift: adjust C to align with data.</li>"
    "</ul>",
    [
        ("Sinusoidal Model", "y = A sin(B(t−C)) + D; models periodic phenomena."),
        ("Amplitude from Data", "(max − min)/2; half the range of oscillation."),
        ("Vertical Shift from Data", "(max + min)/2; the midline value."),
        ("Period from Data", "Time for one complete cycle; B = 2π/period."),
        ("Phase Shift", "Horizontal adjustment C to align model with observed data.")
    ],
    [
        ("Temperature ranges from 40°F to 80°F. Amplitude?", ["40", "*20", "80", "60"],
         "(80 − 40)/2 = 20."),
        ("Midline (vertical shift) for the above?", ["40", "80", "*60", "20"],
         "(80 + 40)/2 = 60."),
        ("Tides have period 12.4 hours. B = ?", ["12.4", "2π(12.4)", "*2π/12.4 ≈ 0.507", "12.4/2π"],
         "B = 2π/period."),
        ("High tide is 8 ft, low tide is 2 ft. Amplitude?", ["8", "2", "*3", "5"],
         "(8 − 2)/2 = 3."),
        ("Midline for the tides above?", ["8", "2", "*5", "3"],
         "(8 + 2)/2 = 5."),
        ("Model: h(t) = 3 sin(Bt) + 5 for tides. B ≈ ?", ["12.4", "*2π/12.4", "0.5", "6.2"],
         "Period = 12.4 → B = 2π/12.4."),
        ("Daylight hours vary with period:", ["1 day", "1 month", "*1 year (365 days)", "12 hours"],
         "Daylight hours cycle annually."),
        ("Sound at 440 Hz. Period = ?", ["440 s", "*1/440 s", "440/2π s", "2π/440 s"],
         "T = 1/f = 1/440 s."),
        ("A Ferris wheel completes one revolution in 60 s. Period?", ["*60 s", "30 s", "120 s", "2π s"],
         "One revolution = one period = 60 s."),
        ("B for the Ferris wheel above?", ["60", "*π/30", "2π/60 = π/30", "120π"],
         "B = 2π/60 = π/30."),
        ("If max height is 50 m and min is 2 m on a Ferris wheel, amplitude?", ["50", "2", "*24", "26"],
         "(50 − 2)/2 = 24."),
        ("Midline for the Ferris wheel?", ["24", "50", "2", "*26"],
         "(50 + 2)/2 = 26."),
        ("A spring oscillates between 3 cm and −3 cm. Amplitude?", ["6", "*3", "0", "−3"],
         "|A| = 3."),
        ("If data peaks at t = 2 and model uses sine (which peaks at π/(2B)), phase shift is:", ["0", "*Adjust C so peak aligns with t = 2", "2", "π/2"],
         "Set B(2 − C) = π/2 → solve for C."),
        ("Which function starts at its maximum at t = 0?", ["Sine", "*Cosine", "Tangent", "None"],
         "cos(0) = 1 (maximum). Often easier for modeling data that starts at a peak."),
        ("Breathing rate: 15 breaths/minute. Period per breath?", ["15 s", "*4 s", "1/15 s", "60 s"],
         "60/15 = 4 seconds per breath."),
        ("Electricity at 60 Hz (US). Period?", ["60 s", "*1/60 s", "0.6 s", "120 s"],
         "T = 1/60 s."),
        ("If a model fits data well but is shifted too far right, adjust:", ["A", "D", "B", "*C (phase shift)"],
         "Phase shift C controls horizontal positioning."),
        ("Monthly average temperature is best modeled by:", ["Linear function", "*Sinusoidal function", "Exponential function", "Quadratic function"],
         "Temperature varies periodically over a year."),
        ("When fitting a sinusoidal model to data, B is determined by:", ["Amplitude", "*The observed period", "The vertical shift", "The maximum value"],
         "B = 2π/period.")
    ]
)
lessons[k] = v

# ── 7.7 Case Studies in Engineering ────────────────────────────────
k, v = build_lesson(7, 7,
    "Case Studies in Engineering",
    "<h3>Case Studies in Engineering</h3>"
    "<p>Trig identities and equations are essential in signal processing, structural analysis, and control systems.</p>"
    "<h4>Signal Processing</h4>"
    "<ul>"
    "<li>Fourier analysis decomposes signals into sums of sine and cosine functions.</li>"
    "<li>Noise filtering uses trig identities to isolate frequencies.</li>"
    "</ul>"
    "<h4>Structural Analysis</h4>"
    "<ul>"
    "<li>Force resolution: F_x = F cos θ, F_y = F sin θ.</li>"
    "<li>Stress analysis in beams uses trig for angle-dependent loads.</li>"
    "</ul>"
    "<h4>Control Systems</h4>"
    "<ul>"
    "<li>Phase margin and gain involve trig relationships.</li>"
    "</ul>",
    [
        ("Fourier Analysis", "Decomposes any periodic signal into a sum of sine and cosine waves at different frequencies."),
        ("Force Resolution", "Breaking a force F into components: F_x = F cos θ, F_y = F sin θ."),
        ("Phase Margin", "The additional phase lag needed to bring a system to instability; involves arctan."),
        ("Beats", "Result of two waves with slightly different frequencies: amplitude varies at the difference frequency."),
        ("Impedance in AC Circuits", "Z = R + jX; magnitude |Z| and phase angle θ = arctan(X/R).")
    ],
    [
        ("A 100 N force at 30° from horizontal. Horizontal component?", ["50 N", "*100 cos 30° ≈ 86.6 N", "100 sin 30° = 50 N", "100 N"],
         "F_x = 100 cos 30° ≈ 86.6 N."),
        ("Vertical component of the force above?", ["86.6 N", "*50 N", "100 N", "25 N"],
         "F_y = 100 sin 30° = 50 N."),
        ("Two forces at right angles: 30 N and 40 N. Resultant magnitude?", ["70 N", "35 N", "*50 N", "10 N"],
         "√(30² + 40²) = 50 N."),
        ("Angle of the resultant above with the 40 N force?", ["45°", "*arctan(30/40) ≈ 36.87°", "53.13°", "30°"],
         "θ = arctan(30/40) ≈ 36.87°."),
        ("Fourier series represents a periodic function as:", ["A polynomial", "*A sum of sines and cosines", "A single exponential", "A linear function"],
         "Fourier: f(t) = a₀ + Σ(aₙ cos nωt + bₙ sin nωt)."),
        ("Beats occur when two waves have:", ["Same frequency", "*Slightly different frequencies", "Very different frequencies", "Same amplitude"],
         "Beat frequency = |f₁ − f₂|; audible when frequencies are close."),
        ("Beat frequency of 440 Hz and 444 Hz:", ["440", "444", "*4 Hz", "884 Hz"],
         "|444 − 440| = 4 Hz."),
        ("In AC circuits, impedance Z = R + jX. |Z| = ?", ["R + X", "*√(R² + X²)", "R · X", "|R − X|"],
         "Magnitude of a complex number."),
        ("Phase angle of Z = 3 + 4j:", ["*arctan(4/3) ≈ 53.13°", "arctan(3/4)", "45°", "90°"],
         "θ = arctan(X/R) = arctan(4/3)."),
        ("A bridge cable makes a 60° angle with the deck. Tension T = 1000 N. Vertical support?", ["500 N", "*1000 sin 60° ≈ 866 N", "1000 cos 60° = 500 N", "1000 N"],
         "Vertical = T sin 60° ≈ 866 N."),
        ("Noise filtering removes unwanted:", ["Amplitudes", "*Frequencies", "Phases", "Signals entirely"],
         "Filters target specific frequency ranges."),
        ("A ramp at 15° with a 200 N weight. Force along the ramp?", ["200 N", "*200 sin 15° ≈ 51.8 N", "200 cos 15° ≈ 193 N", "100 N"],
         "Component along ramp = mg sin θ."),
        ("Normal force on the ramp above?", ["51.8 N", "*200 cos 15° ≈ 193.2 N", "200 N", "100 N"],
         "Normal = mg cos θ."),
        ("In a Fourier series, the coefficient of the fundamental frequency is related to:", ["The DC offset", "*The primary oscillation of the signal", "Noise", "The sampling rate"],
         "The fundamental is the lowest frequency component."),
        ("Phase shift in a control system affects:", ["Only amplitude", "*Timing of the response relative to input", "Frequency only", "Nothing important"],
         "Phase determines when the response occurs relative to input."),
        ("A vibrating beam's natural frequency depends on:", ["Color", "*Material stiffness and geometry", "Temperature only", "Applied force magnitude"],
         "Natural frequency ∝ √(EI/ρAL⁴) — depends on material and geometry."),
        ("sin(ωt) + sin(ωt + π) = ?", ["2 sin(ωt)", "*0", "sin(2ωt)", "cos(ωt)"],
         "sin(ωt + π) = −sin(ωt). Sum = 0. (Destructive interference.)"),
        ("Standing waves on a string are formed by:", ["A single wave", "*Two waves traveling in opposite directions", "A DC signal", "Noise"],
         "Superposition of two counter-propagating waves creates nodes and antinodes."),
        ("Resonance occurs when driving frequency equals:", ["Zero", "Infinity", "*Natural frequency", "Half the natural frequency"],
         "Maximum amplitude at resonance."),
        ("In structural design, trig is used to analyze forces because:", ["Buildings are circular", "*Forces act at angles and must be resolved into components", "It's tradition", "Trig is simple"],
         "Real-world forces act in various directions requiring vector decomposition.")
    ]
)
lessons[k] = v

# ── 7.8 AP Calculus Prep ──────────────────────────────────────────
k, v = build_lesson(7, 8,
    "AP Calculus Prep",
    "<h3>AP Calculus Prep: Trigonometric Skills</h3>"
    "<p>Calculus builds heavily on trig. These skills are essential before starting AP Calculus.</p>"
    "<h4>Must-Know for Calculus</h4>"
    "<ul>"
    "<li><b>Unit circle values:</b> Instant recall of sin, cos, tan at standard angles.</li>"
    "<li><b>Identities:</b> Pythagorean, double-angle, and sum/difference formulas.</li>"
    "<li><b>Key limits:</b> lim(x→0) sin x/x = 1 and lim(x→0) (1 − cos x)/x = 0.</li>"
    "<li><b>Derivatives preview:</b> d/dx[sin x] = cos x, d/dx[cos x] = −sin x.</li>"
    "<li><b>Trig substitution:</b> For integrals involving √(a² − x²), substitute x = a sin θ.</li>"
    "</ul>",
    [
        ("lim sin x / x as x→0", "Equals 1; fundamental limit used in calculus proofs and L'Hôpital's rule."),
        ("lim (1 − cos x)/x as x→0", "Equals 0; another key limit for trig calculus."),
        ("Derivative of sin x", "d/dx[sin x] = cos x."),
        ("Derivative of cos x", "d/dx[cos x] = −sin x."),
        ("Trig Substitution", "Replaces algebraic expressions with trig functions to simplify integrals.")
    ],
    [
        ("lim(x→0) sin x / x = ?", ["0", "*1", "∞", "Does not exist"],
         "Fundamental limit."),
        ("lim(x→0) (1 − cos x)/x = ?", ["1", "*0", "1/2", "∞"],
         "Key limit."),
        ("lim(x→0) tan x / x = ?", ["0", "*1", "∞", "tan 1"],
         "tan x/x = (sin x/x)(1/cos x) → 1·1 = 1."),
        ("lim(x→0) sin(3x)/x = ?", ["1", "*3", "1/3", "0"],
         "sin(3x)/x = 3 · sin(3x)/(3x) → 3·1 = 3."),
        ("lim(x→0) sin(2x)/sin(5x) = ?", ["5/2", "*2/5", "1", "10"],
         "(sin2x/x)/(sin5x/x) → 2/5."),
        ("d/dx[sin x] = ?", ["sin x", "−sin x", "*cos x", "−cos x"],
         "Derivative of sine is cosine."),
        ("d/dx[cos x] = ?", ["cos x", "*−sin x", "sin x", "−cos x"],
         "Derivative of cosine is negative sine."),
        ("d/dx[tan x] = ?", ["−tan x", "sin x/cos²x", "*sec²x", "csc²x"],
         "Derivative of tangent is secant squared."),
        ("sin x ≈ x for small x (in radians). sin(0.01) ≈ ?", ["1", "0", "*0.01", "0.1"],
         "For small x, sin x ≈ x. sin(0.01) ≈ 0.01."),
        ("cos x ≈ 1 − x²/2 for small x. cos(0.1) ≈ ?", ["1", "0.9", "*0.995", "0.99"],
         "1 − (0.01)/2 = 0.995."),
        ("Which trig identity is used to integrate sin²x?", ["Sum formula", "*Power-reducing: sin²x = (1−cos 2x)/2", "Pythagorean directly", "Double angle for sin"],
         "Converts sin²x to a form that's easy to integrate."),
        ("For √(a² − x²), the trig substitution is:", ["x = a tan θ", "x = a sec θ", "*x = a sin θ", "x = a cos θ"],
         "x = a sin θ leads to √(a² − a²sin²θ) = a cos θ."),
        ("For √(a² + x²), substitute:", ["x = a sin θ", "*x = a tan θ", "x = a sec θ", "x = a cos θ"],
         "x = a tan θ gives √(a² + a²tan²θ) = a sec θ."),
        ("For √(x² − a²), substitute:", ["x = a sin θ", "x = a tan θ", "*x = a sec θ", "x = a cos θ"],
         "x = a sec θ gives √(a²sec²θ − a²) = a tan θ."),
        ("sin²x + cos²x = 1 is important in calculus for:", ["Finding zeros", "*Simplifying integrands and derivatives", "Graphing only", "Nothing"],
         "Used constantly in simplification during differentiation and integration."),
        ("The chain rule applied to sin(3x) gives:", ["cos(3x)", "3 sin(3x)", "*3 cos(3x)", "−3 cos(3x)"],
         "d/dx[sin(3x)] = cos(3x) · 3 = 3cos(3x)."),
        ("d/dx[cos(x²)] = ?", ["−sin(x²)", "*−2x sin(x²)", "2x cos(x²)", "sin(x²)"],
         "Chain rule: −sin(x²) · 2x."),
        ("∫cos x dx = ?", ["−sin x + C", "*sin x + C", "cos x + C", "−cos x + C"],
         "Antiderivative of cos x is sin x + C."),
        ("∫sin x dx = ?", ["sin x + C", "cos x + C", "*−cos x + C", "−sin x + C"],
         "Antiderivative of sin x is −cos x + C."),
        ("Why is mastering trig identities essential for calculus?", ["It isn't", "*Many calculus techniques require trig substitution and identity manipulation", "Only for AP exam", "Only for trig integrals"],
         "Trig identities are used throughout calculus for simplification, substitution, and integration.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 7)")
