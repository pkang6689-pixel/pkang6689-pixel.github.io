#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 5: Sum, Difference, Double & Half-Angle Formulas (7 lessons)."""
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

# ── 5.1 ──
k, v = build_lesson(5, 1, "Sum & Difference Formulas for Sine & Cosine",
    "<h3>Sum &amp; Difference Formulas</h3>"
    "<h4>Sine</h4>"
    "<ul><li><b>sin(A + B) = sin A cos B + cos A sin B</b></li>"
    "<li><b>sin(A − B) = sin A cos B − cos A sin B</b></li></ul>"
    "<h4>Cosine</h4>"
    "<ul><li><b>cos(A + B) = cos A cos B − sin A sin B</b></li>"
    "<li><b>cos(A − B) = cos A cos B + sin A sin B</b></li></ul>"
    "<p>These formulas let you compute exact values for non-standard angles: e.g., sin 75° = sin(45° + 30°).</p>",
    [
        ("sin(A+B)", "sin A cos B + cos A sin B."),
        ("sin(A−B)", "sin A cos B − cos A sin B."),
        ("cos(A+B)", "cos A cos B − sin A sin B."),
        ("cos(A−B)", "cos A cos B + sin A sin B."),
        ("Exact Values", "Sum/difference formulas express trig of non-standard angles in terms of known special angles."),
    ],
    [
        ("sin(A + B) =", ["sin A + sin B", "sin A sin B + cos A cos B", "*sin A cos B + cos A sin B", "cos A cos B − sin A sin B"],
         "Standard sum formula for sine."),
        ("cos(A + B) =", ["cos A + cos B", "*cos A cos B − sin A sin B", "cos A sin B + sin A cos B", "sin A sin B + cos A cos B"],
         "Standard sum formula for cosine."),
        ("sin(A − B) =", ["sin A cos B + cos A sin B", "*sin A cos B − cos A sin B", "cos A cos B − sin A sin B", "sin A − sin B"],
         "Difference formula for sine."),
        ("cos(A − B) =", ["cos A cos B − sin A sin B", "*cos A cos B + sin A sin B", "cos A − cos B", "sin A sin B − cos A cos B"],
         "Difference formula for cosine."),
        ("sin 75° = sin(45° + 30°) =", ["sin 45° + sin 30°", "*sin45°cos30° + cos45°sin30° = (√6+√2)/4", "(√2+√3)/4", "sin 75°"],
         "Apply the sum formula with exact values."),
        ("cos 75° = cos(45° + 30°) =", ["cos 45° + cos 30°", "*cos45°cos30° − sin45°sin30° = (√6−√2)/4", "−(√6+√2)/4", "0"],
         "Apply the sum formula for cosine."),
        ("sin 15° = sin(45° − 30°) =", ["(√6+√2)/4", "*(√6−√2)/4", "sin 45° − sin 30°", "1/4"],
         "sin45cos30 − cos45sin30 = (√6−√2)/4."),
        ("cos 15° = cos(45° − 30°) =", ["(√6−√2)/4", "*(√6+√2)/4", "cos 45° − cos 30°", "1/2"],
         "cos45cos30 + sin45sin30 = (√6+√2)/4."),
        ("sin(π/2 + θ) using the sum formula:", ["−sin θ", "sin θ", "*cos θ", "−cos θ"],
         "sin(π/2)cosθ + cos(π/2)sinθ = 1·cosθ + 0·sinθ = cosθ."),
        ("cos(π + θ) =", ["cos θ", "*−cos θ", "sin θ", "−sin θ"],
         "cosπ cosθ − sinπ sinθ = −cosθ."),
        ("sin(π − θ) =", ["−sin θ", "*sin θ", "cos θ", "−cos θ"],
         "sinπ cosθ − cosπ sinθ = 0 + sinθ = sinθ."),
        ("These formulas are derived from:", ["Taylor series", "*Geometric arguments on the unit circle", "The quadratic formula", "Calculus"],
         "The proof uses unit circle geometry or distance formulas."),
        ("sin(A+B) + sin(A−B) =", ["2 cos A cos B", "*2 sin A cos B", "0", "sin 2A"],
         "Adding: sinAcosB+cosAsinB + sinAcosB−cosAsinB = 2sinAcosB."),
        ("cos(A+B) + cos(A−B) =", ["*2 cos A cos B", "2 sin A sin B", "0", "cos 2A"],
         "Adding: cosAcosB−sinAsinB + cosAcosB+sinAsinB = 2cosAcosB."),
        ("sin(0 + B) by the formula =", ["0", "*sin B", "cos B", "1"],
         "sin0·cosB + cos0·sinB = 0+sinB = sinB. Confirms the formula."),
        ("cos(A + 0) =", ["0", "sin A", "*cos A", "1"],
         "cosA·1 − sinA·0 = cosA."),
        ("sin(π/3 + π/6) = sin(π/2) =", ["0", "*1", "1/2", "√3/2"],
         "sin(π/2) = 1. The formula confirms: sin60·cos30 + cos60·sin30 = (√3/2)(√3/2)+(1/2)(1/2) = 3/4+1/4 = 1."),
        ("These formulas are essential for:", ["Only computing exact values", "*Computing exact values, deriving double-angle formulas, simplifying expressions", "Nothing practical", "Graphing only"],
         "They are the foundation for many other identities and applications."),
        ("sin(−B) = sin(0 − B) =", ["sin B", "*−sin B", "cos B", "0"],
         "sin0·cosB − cos0·sinB = −sinB. Confirms sine is odd."),
        ("cos(−B) = cos(0 − B) =", ["−cos B", "sin B", "*cos B", "0"],
         "cos0·cosB + sin0·sinB = cosB. Confirms cosine is even."),
    ]
)
lessons[k] = v

# ── 5.2 ──
k, v = build_lesson(5, 2, "Double-Angle Formulas",
    "<h3>Double-Angle Formulas</h3>"
    "<p>Setting B = A in the sum formulas:</p>"
    "<ul><li><b>sin 2A = 2 sin A cos A</b></li>"
    "<li><b>cos 2A = cos²A − sin²A = 2cos²A − 1 = 1 − 2sin²A</b></li>"
    "<li><b>tan 2A = 2 tan A / (1 − tan²A)</b></li></ul>"
    "<p>There are three equivalent forms for cos 2A, chosen based on what's most convenient.</p>",
    [
        ("sin 2A", "2 sin A cos A."),
        ("cos 2A (form 1)", "cos²A − sin²A."),
        ("cos 2A (form 2)", "2 cos²A − 1."),
        ("cos 2A (form 3)", "1 − 2 sin²A."),
        ("tan 2A", "2 tan A / (1 − tan²A)."),
    ],
    [
        ("sin 2A =", ["sin²A + cos²A", "*2 sin A cos A", "sin A + cos A", "2 sin A"],
         "Double-angle sine formula."),
        ("cos 2A = cos²A − sin²A is derived from:", ["Pythagorean identity", "*cos(A+A) = cosAcosA − sinAsinA", "sin²A + cos²A = 1", "None"],
         "Set B = A in cos(A+B)."),
        ("Which is NOT a form of cos 2A?", ["cos²A − sin²A", "2cos²A − 1", "1 − 2sin²A", "*2cosA − 1"],
         "2cosA − 1 is not a double-angle formula."),
        ("tan 2A =", ["2 tan A", "tan²A", "*2 tan A / (1 − tan²A)", "tan A / 2"],
         "Double-angle tangent formula."),
        ("sin 2(30°) = sin 60° =", ["1/2", "*√3/2", "√2/2", "1"],
         "sin 60° = √3/2. Also: 2 sin 30° cos 30° = 2(1/2)(√3/2) = √3/2. ✓"),
        ("cos 2(45°) = cos 90° =", ["1", "√2/2", "*0", "−1"],
         "cos²45° − sin²45° = 1/2 − 1/2 = 0."),
        ("If sin A = 3/5 and cos A = 4/5, sin 2A =", ["12/25", "*24/25", "7/25", "6/5"],
         "2(3/5)(4/5) = 24/25."),
        ("If sin A = 3/5 and cos A = 4/5, cos 2A =", ["24/25", "*7/25", "−7/25", "0"],
         "cos²A − sin²A = 16/25 − 9/25 = 7/25."),
        ("From cos 2A = 2cos²A − 1, solve for cos²A:", ["(cos 2A − 1)/2", "*(1 + cos 2A)/2", "cos 2A + 1", "2 cos 2A − 1"],
         "cos²A = (1 + cos 2A)/2. This is the power-reduction formula."),
        ("From cos 2A = 1 − 2sin²A, solve for sin²A:", ["(1 + cos 2A)/2", "*(1 − cos 2A)/2", "cos 2A/2", "1 − cos 2A"],
         "sin²A = (1 − cos 2A)/2. Power-reduction formula."),
        ("sin 2A = 1 when 2A = ?", ["0°", "*90°", "180°", "270°"],
         "sin 90° = 1, so A = 45°."),
        ("If tan A = 1 (A in Q I), tan 2A =", ["2", "1", "*undefined (1 − 1 = 0)", "0"],
         "2(1)/(1−1) = 2/0, undefined. (2A = 90°)"),
        ("cos 2A can help simplify cos²A by replacing it with:", ["cos 2A", "*(1 + cos 2A)/2", "sin²A", "1"],
         "This power-reduction is used extensively in calculus."),
        ("sin⁴A = (sin²A)² = ?", ["((1−cos2A)/2)²", "*((1−cos2A)/2)² = (1−2cos2A+cos²2A)/4", "(1+cos2A)²/4", "sin²2A/4"],
         "Applying power reduction twice simplifies higher powers."),
        ("sin 2(π/6) = sin(π/3) =", ["1/2", "*√3/2", "√2/2", "0"],
         "2 sin(π/6) cos(π/6) = 2(1/2)(√3/2) = √3/2."),
        ("cos 120° = cos 2(60°) =", ["1/2", "*−1/2", "0", "√3/2"],
         "2cos²60° − 1 = 2(1/4) − 1 = −1/2."),
        ("The double-angle formulas are special cases of:", ["Pythagorean identities", "*Sum formulas (with B = A)", "Cofunction identities", "Reciprocal identities"],
         "Set B = A in sin(A+B) and cos(A+B)."),
        ("In projectile range R = v₀²sin(2θ)/g, the 2θ uses:", ["Sum formula", "*Double-angle identity", "Half-angle formula", "No identity"],
         "sin(2θ) = 2sinθcosθ is the double-angle formula."),
        ("cos 2A = −1 when 2A =", ["0°", "90°", "*180° (so A = 90°)", "270°"],
         "cos 180° = −1."),
        ("2sinAcosA is another way to write:", ["cos 2A", "*sin 2A", "tan 2A", "sin A + cos A"],
         "sin 2A = 2sinAcosA."),
    ]
)
lessons[k] = v

# ── 5.3 ──
k, v = build_lesson(5, 3, "Half-Angle Formulas",
    "<h3>Half-Angle Formulas</h3>"
    "<p>Derived from the double-angle cosine formulas by replacing A with A/2:</p>"
    "<ul><li><b>sin(A/2) = ±√((1 − cos A)/2)</b></li>"
    "<li><b>cos(A/2) = ±√((1 + cos A)/2)</b></li>"
    "<li><b>tan(A/2) = sin A/(1 + cos A) = (1 − cos A)/sin A</b></li></ul>"
    "<p>The ± sign depends on the quadrant of A/2.</p>",
    [
        ("sin(A/2)", "±√((1 − cos A)/2); sign determined by the quadrant of A/2."),
        ("cos(A/2)", "±√((1 + cos A)/2); sign determined by the quadrant of A/2."),
        ("tan(A/2) — form 1", "sin A / (1 + cos A)."),
        ("tan(A/2) — form 2", "(1 − cos A) / sin A."),
        ("Choosing the Sign", "Determine which quadrant A/2 is in to decide + or −."),
    ],
    [
        ("sin(A/2) =", ["±√((1 + cos A)/2)", "*±√((1 − cos A)/2)", "sin A / 2", "√(sin A)/2"],
         "Half-angle formula for sine."),
        ("cos(A/2) =", ["*±√((1 + cos A)/2)", "±√((1 − cos A)/2)", "cos A / 2", "√(cos A)/2"],
         "Half-angle formula for cosine."),
        ("The ± in half-angle formulas is determined by:", ["The value of A", "*The quadrant that A/2 lies in", "Whether A is positive", "Calculator convention"],
         "If A/2 is in Q I or Q II, sin(A/2) > 0; if Q III or Q IV, sin(A/2) < 0, etc."),
        ("sin 15° = sin(30°/2) =", ["√((1+cos30°)/2)", "*√((1−cos30°)/2) = √((1−√3/2)/2) = √((2−√3)/4)", "sin 30°/2", "1/4"],
         "Half-angle formula with A = 30°. 15° is in Q I, so positive."),
        ("cos 15° =", ["sin 15°", "*√((1+cos30°)/2) = √((2+√3)/4)", "cos 30°/2", "√3/4"],
         "Half-angle formula: √((1+√3/2)/2)."),
        ("tan(A/2) = sin A / (1 + cos A) is useful because:", ["It avoids square roots", "It's always positive", "*It gives a single-valued expression without ±", "It's simpler than the other form"],
         "The ratio form avoids the ± ambiguity."),
        ("tan(A/2) = (1 − cos A) / sin A is equivalent because:", ["They are not equivalent", "*Multiplying num and denom of sinA/(1+cosA) by (1−cosA) yields (1−cosA)(sinA)/sin²A variants", "cos A = sin A always", "It's an approximation"],
         "Both forms derive from the same identity; they are algebraically equivalent."),
        ("sin(π/8) = sin(45°/2) = sin(π/4 ÷ 1) using A = π/4:", ["√((1+√2/2)/2)", "*√((1−√2/2)/2) = √((2−√2)/4)", "sin(π/4)/2", "1/√8"],
         "sin(π/8) = √((1−cos(π/4))/2) = √((2−√2)/4)."),
        ("cos(π/8) =", ["sin(π/8)", "*√((1+cos(π/4))/2) = √((2+√2)/4)", "cos(π/4)/2", "1/4"],
         "cos(π/8) = √((1+√2/2)/2) = √((2+√2)/4)."),
        ("If A = 120°, A/2 = 60°. Verify: cos 60° = √((1+cos120°)/2):", ["Doesn't work", "*√((1+(−1/2))/2) = √(1/4) = 1/2 ✓", "√(3/4)", "cos 60° ≠ 1/2"],
         "cos 120° = −1/2. √((1−1/2)/2) = √(1/4) = 1/2 = cos 60°. ✓"),
        ("If A = 240°, then A/2 = 120°. Is sin(120°) positive or negative?", ["*Positive (Q II)", "Negative", "Zero", "Undefined"],
         "120° is in Q II where sine is positive."),
        ("sin(A/2) when A = 240°: sin 120° =", ["−√3/2", "*√3/2", "1/2", "−1/2"],
         "In Q II, sin is positive: √((1−cos240°)/2) = √((1+1/2)/2) = √(3/4) = √3/2."),
        ("Half-angle formulas are derived from:", ["Sum formulas", "*Double-angle cosine formulas solved for sin²(A/2) or cos²(A/2)", "Pythagorean identity alone", "Reciprocal identities"],
         "cos 2α = 1 − 2sin²α → sin²α = (1−cos2α)/2; let α = A/2."),
        ("Computing sin 22.5° requires:", ["Only sin 45° / 2 (wrong)", "*Half-angle: √((1−cos45°)/2)", "Sum formula with 10° + 12.5°", "A calculator only"],
         "22.5° = 45°/2, so use the half-angle formula with A = 45°."),
        ("tan(π/12) using tan half-angle (A = π/6):", ["tan(π/6)/2", "*sin(π/6)/(1+cos(π/6)) = (1/2)/(1+√3/2) = 1/(2+√3)", "cos(π/6)/sin(π/6)", "2"],
         "tan(π/12) = sin(π/6)/(1+cos(π/6)) = (1/2)/(1+√3/2)."),
        ("cos(3π/8) = cos(3π/4 ÷ 2). Since 3π/8 is in Q I, we take:", ["*Positive root", "Negative root", "Either", "Zero"],
         "3π/8 ≈ 67.5° is in Q I, so cosine is positive."),
        ("Half-angle formulas help compute exact values for angles that are:", ["Multiples of 30°", "*Half of known special angles (e.g., 22.5° = 45°/2)", "Only acute", "Only in Q I"],
         "They extend exact-value computation to finer angle divisions."),
        ("sin²(A/2) = (1 − cos A)/2 is also called a:", ["Double-angle formula", "*Power-reduction formula (with substitution)", "Sum formula", "Reciprocal identity"],
         "It reduces the power of sin from 2 to 0 (in terms of cos 2α)."),
        ("If cos A = 0.6 and A is in Q I (so A/2 in Q I), cos(A/2) =", ["0.3", "√0.8", "*√(0.8) = √(4/5) = 2/√5 ≈ 0.894", "0.6/2"],
         "cos(A/2) = √((1+0.6)/2) = √(0.8) ≈ 0.894."),
        ("Half-angle formulas are important in calculus for:", ["*Integrating sin²x and cos²x (power reduction)", "Only graphing", "Finding limits", "Nothing"],
         "∫ sin²x dx requires cos 2x substitution, which comes from half/double angle ideas."),
    ]
)
lessons[k] = v

# ── 5.4 ──
k, v = build_lesson(5, 4, "Product-to-Sum & Sum-to-Product Formulas",
    "<h3>Product-to-Sum &amp; Sum-to-Product Formulas</h3>"
    "<h4>Product-to-Sum</h4>"
    "<ul><li>sin A cos B = ½[sin(A+B) + sin(A−B)]</li>"
    "<li>cos A sin B = ½[sin(A+B) − sin(A−B)]</li>"
    "<li>cos A cos B = ½[cos(A−B) + cos(A+B)]</li>"
    "<li>sin A sin B = ½[cos(A−B) − cos(A+B)]</li></ul>"
    "<h4>Sum-to-Product</h4>"
    "<ul><li>sin A + sin B = 2 sin((A+B)/2) cos((A−B)/2)</li>"
    "<li>sin A − sin B = 2 cos((A+B)/2) sin((A−B)/2)</li>"
    "<li>cos A + cos B = 2 cos((A+B)/2) cos((A−B)/2)</li>"
    "<li>cos A − cos B = −2 sin((A+B)/2) sin((A−B)/2)</li></ul>",
    [
        ("Product-to-Sum (sin·cos)", "sin A cos B = ½[sin(A+B) + sin(A−B)]."),
        ("Product-to-Sum (cos·cos)", "cos A cos B = ½[cos(A−B) + cos(A+B)]."),
        ("Sum-to-Product (sin+sin)", "sin A + sin B = 2 sin((A+B)/2) cos((A−B)/2)."),
        ("Sum-to-Product (cos+cos)", "cos A + cos B = 2 cos((A+B)/2) cos((A−B)/2)."),
        ("Usage", "Product-to-sum simplifies integration; sum-to-product helps solve equations."),
    ],
    [
        ("sin A cos B =", ["sin(A+B)", "*½[sin(A+B) + sin(A−B)]", "½[cos(A−B) − cos(A+B)]", "sin A + cos B"],
         "Product-to-sum formula for sinAcosB."),
        ("cos A cos B =", ["½[sin(A+B) + sin(A−B)]", "*½[cos(A−B) + cos(A+B)]", "cos(A+B)", "cos A + cos B"],
         "Product-to-sum for cosAcosB."),
        ("sin A sin B =", ["½[cos(A+B) + cos(A−B)]", "*½[cos(A−B) − cos(A+B)]", "sin(A)sin(B)", "0"],
         "Product-to-sum for sinAsinB."),
        ("sin A + sin B =", ["*2 sin((A+B)/2) cos((A−B)/2)", "sin(A+B)", "2 cos((A+B)/2) sin((A−B)/2)", "sin A · sin B"],
         "Sum-to-product for two sines."),
        ("cos A + cos B =", ["2 sin((A+B)/2) cos((A−B)/2)", "*2 cos((A+B)/2) cos((A−B)/2)", "cos(A+B)", "0"],
         "Sum-to-product for two cosines."),
        ("cos A − cos B =", ["2 cos((A+B)/2) cos((A−B)/2)", "*−2 sin((A+B)/2) sin((A−B)/2)", "cos(A−B)", "0"],
         "Sum-to-product for cosA − cosB."),
        ("sin 3x cos x using product-to-sum:", ["sin 4x", "*½[sin 4x + sin 2x]", "½[cos 2x + cos 4x]", "sin 2x"],
         "½[sin(3x+x) + sin(3x−x)] = ½[sin4x + sin2x]."),
        ("cos 5x cos 3x =", ["*½[cos 2x + cos 8x]", "½[sin 8x + sin 2x]", "cos 8x", "cos 15x"],
         "½[cos(5x−3x) + cos(5x+3x)] = ½[cos2x + cos8x]."),
        ("sin 50° + sin 10° using sum-to-product:", ["sin 60°", "*2 sin 30° cos 20°", "2 cos 30° sin 20°", "sin 40°"],
         "2 sin((50+10)/2) cos((50−10)/2) = 2 sin30° cos20°."),
        ("sin 50° − sin 10° =", ["*2 cos 30° sin 20°", "2 sin 30° cos 20°", "0", "sin 40°"],
         "sinA−sinB = 2cos((A+B)/2)sin((A−B)/2) = 2cos30°sin20°."),
        ("cos 70° + cos 30° =", ["cos 100°", "*2 cos 50° cos 20°", "2 sin 50° cos 20°", "0"],
         "2cos((70+30)/2)cos((70−30)/2) = 2cos50°cos20°."),
        ("Product-to-sum formulas are derived from:", ["Half-angle formulas", "*Adding/subtracting sum and difference formulas", "Pythagorean identities", "None"],
         "Add sin(A+B)+sin(A−B) to get 2sinAcosB, etc."),
        ("These formulas are useful in calculus for:", ["*Integrating products of trig functions", "Differentiating only", "Nothing", "Graphing only"],
         "∫sinAcosBdx is easier after converting to a sum."),
        ("sin 75° cos 15° =", ["sin 90°", "*½[sin 90° + sin 60°] = ½[1 + √3/2] = (2+√3)/4", "½[cos60° + cos90°]", "sin 60°"],
         "½[sin(75+15) + sin(75−15)] = ½[sin90 + sin60]."),
        ("Sum-to-product is useful for solving equations like sin 3x + sin x = 0:", ["Set each to 0", "*2 sin 2x cos x = 0, then sin 2x = 0 or cos x = 0", "Square both sides", "Divide by sin x"],
         "Convert to product form and set each factor to 0."),
        ("cos 3x − cos x = 0 becomes:", ["cos 2x = 0", "*−2 sin 2x sin x = 0, so sin 2x = 0 or sin x = 0", "cos 4x = 0", "2 cos 2x cos x = 0"],
         "cosA−cosB = −2sin((A+B)/2)sin((A−B)/2)."),
        ("In signal processing, product-to-sum relates to:", ["*Amplitude modulation (AM) produces sum and difference frequencies", "Nothing", "Only digital signals", "Voltage measurement"],
         "Multiplying a carrier with a signal produces sum and difference frequencies."),
        ("sin A sin B = 0 can sometimes be solved using:", ["Sum-to-product", "*Setting each factor to 0 after product form", "Only graphing", "Calculus"],
         "If a product = 0, at least one factor = 0."),
        ("½[cos(A−B) − cos(A+B)] is the product-to-sum for:", ["cosAcosB", "*sinAsinB", "sinAcosB", "cosAsinB"],
         "sinAsinB = ½[cos(A−B) − cos(A+B)]."),
        ("These 8 formulas (4 product-to-sum + 4 sum-to-product) all derive from:", ["8 separate proofs", "*The 4 sum/difference formulas for sin and cos", "Half-angle formulas", "Pythagorean identity"],
         "All are algebraic rearrangements of the sum and difference formulas."),
    ]
)
lessons[k] = v

# ── 5.5 ──
k, v = build_lesson(5, 5, "Simplifying Expressions with These Formulas",
    "<h3>Simplifying Expressions with Sum, Double, &amp; Half-Angle Formulas</h3>"
    "<p>Combine all the identities learned so far to simplify complex expressions.</p>"
    "<h4>Common Simplifications</h4>"
    "<ul><li>sin²x = (1 − cos 2x)/2 (power reduction).</li>"
    "<li>cos²x = (1 + cos 2x)/2.</li>"
    "<li>sin x cos x = sin(2x)/2.</li>"
    "<li>Products of different-frequency trig → sums via product-to-sum.</li></ul>",
    [
        ("Power Reduction (sin²)", "sin²x = (1 − cos 2x)/2."),
        ("Power Reduction (cos²)", "cos²x = (1 + cos 2x)/2."),
        ("sin x cos x", "= sin(2x)/2 by the double-angle formula."),
        ("Simplification Goal", "Reduce powers, convert products to sums, or consolidate into simpler forms."),
        ("Strategy", "Choose the identity that eliminates the most complex part of the expression."),
    ],
    [
        ("sin²x simplified:", ["1 − cos x", "*（1 − cos 2x)/2", "sin 2x / 2", "cos²x"],
         "Power reduction: sin²x = (1 − cos 2x)/2."),
        ("cos²x simplified:", ["(1 − cos 2x)/2", "*(1 + cos 2x)/2", "cos 2x / 2", "1 + sin 2x"],
         "Power reduction: cos²x = (1 + cos 2x)/2."),
        ("sin x cos x =", ["sin 2x", "*sin(2x)/2", "cos(2x)/2", "sin x + cos x"],
         "sin(2x) = 2sinxcosx, so sinxcosx = sin(2x)/2."),
        ("sin²x cos²x =", ["sin²(2x)", "*(1 − cos 4x)/8", "sin(4x)/4", "1/4"],
         "(sinxcosx)² = (sin2x/2)² = sin²(2x)/4 = (1−cos4x)/8."),
        ("cos⁴x =", ["(1+cos2x)²/4", "*(3 + 4cos2x + cos4x)/8", "(1+cos2x)/2", "cos²(2x)"],
         "cos⁴x = (cos²x)² = ((1+cos2x)/2)² = (1+2cos2x+cos²2x)/4 = (3+4cos2x+cos4x)/8."),
        ("4 sin x cos x = 2 · 2sinxcosx =", ["4sinxcosx", "*2 sin 2x", "sin 4x", "cos 2x"],
         "2(2sinxcosx) = 2sin(2x)."),
        ("Simplify sin(x + π/3) + sin(x − π/3):", ["2 sin x cos(π/3)", "*2 sin x · cos(π/3) = 2sinx · (1/2) = sin x", "sin 2x", "0"],
         "Sum-to-product: 2sin(x)cos(π/3) = 2sinx(1/2) = sinx."),
        ("cos(x + π/4) − cos(x − π/4):", ["2cos x cos(π/4)", "*−2sin(x)sin(π/4) = −√2 sin x", "0", "cos 2x"],
         "cosA−cosB = −2sin((A+B)/2)sin((A−B)/2) = −2sinx sin(π/4)."),
        ("sin 2x / (2 cos x) =", ["cos x", "*sin x", "tan x", "2"],
         "2sinxcosx/(2cosx) = sinx."),
        ("(1 + cos 2x)/(2) =", ["sin²x", "*cos²x", "cos 2x", "1"],
         "Power reduction: cos²x = (1+cos2x)/2."),
        ("cos² 3x simplified:", ["(1+cos3x)/2", "*(1+cos6x)/2", "cos 6x", "(1−cos6x)/2"],
         "cos²(3x) = (1+cos(2·3x))/2 = (1+cos6x)/2."),
        ("2cos²x − 1 =", ["*cos 2x", "sin 2x", "1", "2 sin x"],
         "This is one form of the double-angle formula for cos 2x."),
        ("1 − 2sin²x =", ["sin 2x", "*cos 2x", "−cos 2x", "−sin 2x"],
         "Another form of cos 2x."),
        ("sin 3x can be expanded using sin(2x + x) =", ["3 sin x", "*sin2xcosx + cos2xsinx = 2sinxcos²x + sinx − 2sin³x = 3sinx − 4sin³x", "sin x cos 2x", "None"],
         "Using sum and double-angle formulas: sin3x = 3sinx − 4sin³x."),
        ("cos 3x = cos(2x + x) =", ["3cosx", "*cos2xcosx − sin2xsinx = 4cos³x − 3cosx", "cosx − sinx", "None"],
         "cos3x = 4cos³x − 3cosx."),
        ("These simplifications are critical for:", ["*Calculus integration of trig powers", "Only algebra", "Cooking", "Geography"],
         "∫sin²xdx and similar integrals require power reduction."),
        ("sin(A+B) sin(A−B) =", ["sin²A + sin²B", "*sin²A − sin²B", "cos²A − cos²B", "sin²A cos²B"],
         "Using product-to-sum then Pythagorean: ½[cos2B−cos2A] simplifies to sin²A−sin²B."),
        ("cos²x − sin²x simplifies to:", ["1", "0", "*cos 2x", "sin 2x"],
         "cos 2x = cos²x − sin²x."),
        ("If you see sin⁶x, the first step to simplify is often:", ["Factor out sin x", "*Write (sin²x)³ = ((1−cos2x)/2)³ and expand", "Use sum formula", "Give up"],
         "Power reduction brings the powers down to manageable levels."),
        ("Mastering these formulas makes which calculus topic easier?", ["Limits", "Derivatives of polynomials", "*Integration of trigonometric functions", "Sequences"],
         "Trig integrals heavily rely on these simplification formulas."),
    ]
)
lessons[k] = v

# ── 5.6 ──
k, v = build_lesson(5, 6, "Engineering Cases",
    "<h3>Engineering Applications of Sum/Double/Half-Angle Formulas</h3>"
    "<h4>Electrical Engineering</h4>"
    "<ul><li><b>AC power:</b> P(t) = V₀I₀ sin(ωt) sin(ωt+φ). Use product-to-sum → P = (V₀I₀/2)[cos φ − cos(2ωt+φ)].</li>"
    "<li><b>Average power</b> = V₀I₀ cos φ / 2 (the constant term; the oscillating term averages to 0).</li></ul>"
    "<h4>Mechanical Vibrations</h4>"
    "<p>Two vibrations at close frequencies create <b>beats</b>: sin ω₁t + sin ω₂t = 2 cos((ω₁−ω₂)t/2) sin((ω₁+ω₂)t/2).</p>"
    "<h4>Signal Processing</h4>"
    "<p>AM radio multiplies a carrier by a signal; frequency shifting uses product-to-sum conversions.</p>",
    [
        ("AC Power Formula", "P(t) = (V₀I₀/2)[cosφ − cos(2ωt+φ)]; constant part = average power."),
        ("Average Power", "P_avg = V₀I₀ cosφ / 2; the oscillating term averages to zero."),
        ("Beat Frequency", "Sum-to-product: sinω₁t + sinω₂t = 2cos(Δωt/2)sin(ω_avg t)."),
        ("AM Radio", "Carrier × signal uses product-to-sum to produce sum and difference frequencies."),
        ("Fourier Analysis", "Decomposing signals into sine and cosine components using these identities."),
    ],
    [
        ("In AC power, V(t)I(t) = V₀I₀ sin(ωt)sin(ωt+φ). Which identity simplifies this?", ["Sum formula", "*Product-to-sum: sinAsinB = ½[cos(A−B)−cos(A+B)]", "Double-angle", "Half-angle"],
         "Product-to-sum converts the product of two sines into a sum of cosines."),
        ("The average AC power depends on:", ["Frequency only", "Amplitude only", "*cos φ (the power factor)", "sin φ"],
         "P_avg = V₀I₀ cos φ / 2."),
        ("If φ = 0 (voltage and current in phase), power factor =", ["0", "*1", "−1", "0.5"],
         "cos(0) = 1, maximum power transfer."),
        ("If φ = 90°, average power =", ["Maximum", "*0 (all reactive, no real power)", "V₀I₀/2", "Negative"],
         "cos 90° = 0, so no average power delivered."),
        ("Beats arise from:", ["Product of same-frequency signals", "*Sum of two close-frequency signals → sum-to-product", "Double-angle formula", "Half-angle formula"],
         "sinω₁t + sinω₂t = 2cos(Δω/2·t)sin(ω_avg·t)."),
        ("The beat frequency is:", ["ω₁ + ω₂", "ω₁ · ω₂", "*|ω₁ − ω₂|/2 (or |f₁ − f₂| for audible beats)", "2(ω₁ + ω₂)"],
         "The modulation envelope oscillates at (ω₁−ω₂)/2."),
        ("In AM radio, multiplying signal s(t) by carrier cos(ωc t):", ["Adds frequencies", "*Creates sum and difference frequencies: s(t)cos(ωct) → ½[cos((ωc−ωs)t) + cos((ωc+ωs)t)]", "Removes frequencies", "Does nothing"],
         "Product-to-sum shows that modulation shifts the signal to sideband frequencies."),
        ("Double-angle formulas appear in calculating:", ["*Projectile range (sin2θ) and power oscillation frequency (2ω)", "Only theoretical math", "Nothing practical", "Temperature"],
         "sin(2θ) in range formula and cos(2ωt) in power are both double-angle applications."),
        ("Half-angle formulas help in:", ["*Computing exact trig values for non-standard angles in fabrication/machining", "No engineering applications", "Only physics", "Music only"],
         "When precise angles like 22.5° or 67.5° are needed in manufacturing."),
        ("In structural engineering, load angles use:", ["No trig", "*Sum/difference formulas to decompose forces at compound angles", "Only Pythagorean theorem", "Matrices only"],
         "Forces at non-standard angles decompose using trig identities."),
        ("cos²(ωt) in RMS calculations is replaced by:", ["cosωt", "*(1 + cos2ωt)/2", "sin²ωt", "1"],
         "Power-reduction formula simplifies RMS (root-mean-square) calculations."),
        ("The RMS voltage = V₀/√2 comes from averaging:", ["V₀", "*sin²(ωt) over one cycle, which averages to 1/2", "V₀²", "cos ωt"],
         "⟨sin²(ωt)⟩ = 1/2, so V_rms = V₀√(1/2) = V₀/√2."),
        ("Fourier series represents periodic signals as sums of:", ["Polynomials", "Exponentials", "*Sine and cosine functions at integer multiples of a fundamental frequency", "Logarithms"],
         "Fourier analysis is built on trig identities."),
        ("When combining two antenna signals with phase difference δ:", ["Add amplitudes", "*Use sum formulas: cos(ωt) + cos(ωt+δ) = 2cos(δ/2)cos(ωt+δ/2)", "Multiply", "Subtract"],
         "Sum-to-product reveals the combined amplitude depends on cos(δ/2)."),
        ("Constructive interference (max signal) occurs when δ =", ["π", "*0 (or 2nπ)", "π/2", "3π/2"],
         "cos(0/2) = 1 gives maximum combined amplitude."),
        ("Destructive interference occurs when δ =", ["0", "*π (or (2n+1)π)", "2π", "π/4"],
         "cos(π/2) = 0; the signals cancel."),
        ("In telecommunications, frequency mixing relies on:", ["Addition", "Subtraction", "*Product-to-sum identities", "Half-angle formulas"],
         "Mixing (multiplication) of signals produces sum/difference frequencies."),
        ("The double-angle identity makes computing sin(2θ) easier by:", ["Doubling sin θ", "*Using 2sinθcosθ — only requiring sin θ and cos θ", "Squaring sin θ", "Adding θ to itself"],
         "If you know sinθ and cosθ, you can find sin(2θ) directly."),
        ("Which formula is used in vibration analysis when two close frequencies combine?", ["Double-angle", "Half-angle", "*Sum-to-product (beat analysis)", "Product-to-sum"],
         "sinω₁t + sinω₂t → 2cos(Δω/2·t)sin(ω_avg·t)."),
        ("These identities are indispensable across all engineering disciplines because:", ["They replace calculus", "*They convert complex trig expressions into simpler, analyzable forms", "They are required by law", "They save money"],
         "Simplification is essential for analysis, design, and computation."),
    ]
)
lessons[k] = v

# ── 5.7 ──
k, v = build_lesson(5, 7, "AP Calculus Connections",
    "<h3>AP Calculus Connections</h3>"
    "<p>Many calculus problems rely on the identities from this unit:</p>"
    "<h4>Integration</h4>"
    "<ul><li>∫ sin²x dx uses power reduction: (1 − cos 2x)/2.</li>"
    "<li>∫ sin mx cos nx dx uses product-to-sum.</li>"
    "<li>∫ sec²x dx = tan x + C (from tan²x + 1 = sec²x).</li></ul>"
    "<h4>Limits &amp; Derivatives</h4>"
    "<ul><li>lim(x→0) sin x / x = 1 (used with double-angle rearrangements).</li>"
    "<li>d/dx[sin 2x] = 2 cos 2x (chain rule + double angle).</li></ul>",
    [
        ("∫ sin²x dx", "Use sin²x = (1−cos2x)/2, then integrate: x/2 − sin(2x)/4 + C."),
        ("∫ sinmx cosnx dx", "Product-to-sum converts to integrable sums of sin/cos."),
        ("d/dx[sin 2x]", "= 2 cos 2x by the chain rule."),
        ("lim sin x / x", "= 1 as x → 0; fundamental limit in calculus."),
        ("Trig Substitution", "In integrals like ∫√(1−x²)dx, let x = sinθ; uses sin²+cos²=1."),
    ],
    [
        ("∫ sin²x dx is simplified by using:", ["Double-angle for sin", "*Power reduction: sin²x = (1−cos2x)/2", "Sum-to-product", "No identity needed"],
         "Power reduction makes the integrand a simple cosine."),
        ("∫ sin²x dx =", ["sin³x/3 + C", "*x/2 − sin(2x)/4 + C", "−cos²x + C", "sin x − cos x + C"],
         "∫(1−cos2x)/2 dx = x/2 − sin(2x)/4 + C."),
        ("∫ cos²x dx =", ["*x/2 + sin(2x)/4 + C", "cos³x/3 + C", "x/2 − sin(2x)/4 + C", "sin²x + C"],
         "cos²x = (1+cos2x)/2. ∫ = x/2 + sin(2x)/4 + C."),
        ("∫ sin x cos x dx can use:", ["*sin x cos x = sin(2x)/2, so ∫ = −cos(2x)/4 + C", "No identity", "Power reduction", "Sum-to-product"],
         "Or use u-substitution. Both work."),
        ("∫ sin 3x cos 2x dx uses:", ["Double-angle", "Half-angle", "*Product-to-sum: ½[sin5x + sinx]", "No identity"],
         "Product-to-sum converts to ½∫sin5x + sinx dx."),
        ("d/dx[sin 2x] =", ["sin 2x", "*2 cos 2x", "cos 2x", "2 sin 2x"],
         "Chain rule: cos(2x) · 2 = 2cos2x."),
        ("d/dx[cos²x] =", ["*−sin 2x (= −2sinxcosx)", "2 cos x", "−2 cos x sin x + 1", "cos 2x"],
         "d/dx[cos²x] = 2cosx(−sinx) = −2sinxcosx = −sin2x."),
        ("The limit lim(x→0) sin x / x =", ["0", "*1", "∞", "Does not exist"],
         "Fundamental limit, proved geometrically or by series."),
        ("lim(x→0) sin(2x)/x = ?", ["1", "*2", "0", "1/2"],
         "sin(2x)/x = 2 · sin(2x)/(2x) → 2 · 1 = 2."),
        ("Trig substitution x = sin θ transforms √(1−x²) into:", ["sin θ", "*cos θ (or |cos θ|)", "tan θ", "1"],
         "√(1−sin²θ) = √(cos²θ) = |cos θ|."),
        ("In ∫√(1−x²) dx, after x = sinθ, dx =", ["dθ", "*cos θ dθ", "sin θ dθ", "−sin θ dθ"],
         "dx = cosθ dθ."),
        ("∫ sec²x dx =", ["sec x + C", "*tan x + C", "ln|sec x| + C", "−cot x + C"],
         "Direct antiderivative: d/dx[tanx] = sec²x."),
        ("∫ tan²x dx uses:", ["*tan²x = sec²x − 1, so ∫ = tanx − x + C", "No identity", "Product-to-sum", "Half-angle"],
         "Rewrite using Pythagorean identity."),
        ("d/dx[tan x] =", ["tan²x", "*sec²x", "csc²x", "1 + tan x"],
         "d/dx[tanx] = sec²x."),
        ("d/dx[sec x] =", ["sec x", "*sec x tan x", "csc x cot x", "−sec x"],
         "Standard derivative."),
        ("∫ sin⁴x dx requires:", ["One power reduction", "*Two rounds of power reduction (sin⁴x = (sin²x)²)", "No identity", "Sum formula"],
         "sin⁴x → ((1−cos2x)/2)² → expand and reduce again."),
        ("In Fourier series, ∫ sin(mx)cos(nx)dx over a period =", ["Always 1", "Always π", "*0 (orthogonality, when m ≠ n)", "π/2"],
         "Product-to-sum shows the integral of different-frequency sin·cos over a full period is 0."),
        ("cos(2x) = 1 − 2sin²x is most useful in calculus for:", ["*Replacing sin²x in integrands", "Graphing", "Finding limits of cos", "No use"],
         "It's the power-reduction formula."),
        ("Which of these integrals does NOT need a trig identity?", ["∫sin²xdx", "∫sin3xcos2xdx", "*∫sinxdx", "∫tan²xdx"],
         "∫sinxdx = −cosx + C — no identity needed."),
        ("Mastery of trig identities is essential for AP Calculus because:", ["*Many integration techniques require identity-based simplification", "The AP exam only has trig questions", "Trig is all of calculus", "It's not essential"],
         "Trig integrals, substitutions, and simplifications appear throughout calculus."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 5: wrote {len(lessons)} lessons")
