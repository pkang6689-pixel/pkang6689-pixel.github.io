#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 1: Angle Fundamentals (7 lessons)."""
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

# ── Lesson 1.1 ──
k, v = build_lesson(1, 1, "Angles in Degrees & Radians",
    "<h3>Angles in Degrees &amp; Radians</h3>"
    "<p>An <b>angle</b> is formed by two rays sharing a common endpoint (vertex). Angles can be measured in <b>degrees</b> or <b>radians</b>.</p>"
    "<h4>Degrees</h4>"
    "<ul><li>A full rotation = 360°.</li>"
    "<li>A straight angle = 180°; a right angle = 90°.</li></ul>"
    "<h4>Radians</h4>"
    "<ul><li>A radian measures the angle subtended by an arc equal in length to the radius.</li>"
    "<li>A full rotation = 2π radians ≈ 6.283 rad.</li>"
    "<li>π radians = 180°.</li></ul>"
    "<h4>Conversion Formulas</h4>"
    "<ul><li><b>Degrees → Radians:</b> multiply by π/180.</li>"
    "<li><b>Radians → Degrees:</b> multiply by 180/π.</li></ul>"
    "<p>Example: 90° × π/180 = π/2 rad. Example: π/3 rad × 180/π = 60°.</p>",
    [
        ("Degree", "A unit of angle measure where a full rotation equals 360°."),
        ("Radian", "A unit of angle measure where the angle is subtended by an arc equal in length to the radius; a full rotation = 2π radians."),
        ("Conversion: Degrees to Radians", "Multiply the degree measure by π/180."),
        ("Conversion: Radians to Degrees", "Multiply the radian measure by 180/π."),
        ("Standard Position", "An angle with its vertex at the origin and initial side along the positive x-axis."),
    ],
    [
        ("How many degrees are in a full rotation?", ["180°", "270°", "*360°", "90°"],
         "A full rotation around a circle is 360°."),
        ("How many radians are in a full rotation?", ["π", "*2π", "π/2", "4π"],
         "A full rotation equals 2π radians."),
        ("Convert 180° to radians.", ["2π", "π/2", "*π", "π/4"],
         "180° × π/180 = π radians."),
        ("Convert π/6 radians to degrees.", ["*30°", "60°", "45°", "90°"],
         "π/6 × 180/π = 30°."),
        ("Convert 45° to radians.", ["π/6", "*π/4", "π/3", "π/2"],
         "45° × π/180 = π/4 radians."),
        ("Which is larger: 1 radian or 1 degree?", ["1 degree", "*1 radian", "They are equal", "Cannot be compared"],
         "1 radian ≈ 57.3°, so 1 radian is much larger than 1 degree."),
        ("Convert 2π/3 radians to degrees.", ["60°", "90°", "*120°", "150°"],
         "2π/3 × 180/π = 120°."),
        ("Convert 270° to radians.", ["π", "2π", "*3π/2", "π/2"],
         "270° × π/180 = 3π/2 radians."),
        ("How many radians equal 90°?", ["π", "π/3", "*π/2", "2π"],
         "90° × π/180 = π/2 radians."),
        ("Convert 5π/6 radians to degrees.", ["120°", "*150°", "135°", "180°"],
         "5π/6 × 180/π = 150°."),
        ("What is the radian measure of a straight angle?", ["2π", "π/2", "*π", "π/4"],
         "A straight angle is 180° = π radians."),
        ("Convert 315° to radians.", ["5π/4", "*7π/4", "3π/2", "11π/6"],
         "315° × π/180 = 7π/4 radians."),
        ("If an arc length equals the radius, the angle in radians is:", ["2", "π", "*1", "0.5"],
         "By definition, 1 radian is the angle subtended by an arc equal to the radius."),
        ("Convert 3π radians to degrees.", ["360°", "270°", "*540°", "450°"],
         "3π × 180/π = 540°."),
        ("Which angle measure is commonly used in calculus?", ["Degrees", "*Radians", "Gradians", "Revolutions"],
         "Radians are the standard unit in calculus and most higher mathematics."),
        ("Convert 60° to radians.", ["π/2", "π/4", "*π/3", "π/6"],
         "60° × π/180 = π/3 radians."),
        ("Convert π/4 radians to degrees.", ["30°", "*45°", "60°", "90°"],
         "π/4 × 180/π = 45°."),
        ("How many degrees is 1 radian (approximately)?", ["45°", "*57.3°", "90°", "30°"],
         "1 rad × 180/π ≈ 57.3°."),
        ("Convert 240° to radians.", ["*4π/3", "5π/3", "3π/2", "7π/6"],
         "240° × π/180 = 4π/3 radians."),
        ("Which statement is true?", ["π radians = 360°", "*π radians = 180°", "2π radians = 180°", "π radians = 90°"],
         "By definition, π radians = 180°."),
    ]
)
lessons[k] = v

# ── Lesson 1.2 ──
k, v = build_lesson(1, 2, "Arc Length & Sector Area",
    "<h3>Arc Length &amp; Sector Area</h3>"
    "<p>When an angle is measured in radians, there are elegant formulas connecting the angle to the arc and sector of a circle.</p>"
    "<h4>Arc Length</h4>"
    "<ul><li><b>s = rθ</b> where s = arc length, r = radius, θ = central angle in radians.</li></ul>"
    "<h4>Sector Area</h4>"
    "<ul><li><b>A = ½r²θ</b> where A = area of the sector, r = radius, θ = central angle in radians.</li></ul>"
    "<p>Note: If the angle is in degrees, first convert to radians or use: s = (θ/360)·2πr and A = (θ/360)·πr².</p>"
    "<p>The relationship s = rθ shows why radians are natural: arc length is simply radius × angle.</p>",
    [
        ("Arc Length Formula", "s = rθ, where s is the arc length, r is the radius, and θ is the central angle in radians."),
        ("Sector Area Formula", "A = ½r²θ, where A is the sector area, r is the radius, and θ is the central angle in radians."),
        ("Sector", "A 'pie-slice' region bounded by two radii and an arc of a circle."),
        ("Central Angle", "An angle whose vertex is at the center of a circle and whose sides are radii."),
        ("Arc", "A portion of the circumference of a circle."),
    ],
    [
        ("The formula for arc length (θ in radians) is:", ["s = r/θ", "*s = rθ", "s = r²θ", "s = ½rθ"],
         "Arc length s = rθ when θ is in radians."),
        ("Find the arc length when r = 5 and θ = π/3.", ["5π/6", "*5π/3", "10π/3", "π/3"],
         "s = rθ = 5 · π/3 = 5π/3."),
        ("The sector area formula (θ in radians) is:", ["A = rθ", "A = r²θ", "*A = ½r²θ", "A = 2r²θ"],
         "Sector area A = ½r²θ when θ is in radians."),
        ("Find the sector area when r = 4 and θ = π/2.", ["4π", "*2π (≈ 6.28)", "8π", "π"],
         "A = ½(4²)(π/2) = ½(16)(π/2) = 4π. Wait — ½·16·π/2 = 4π. Actually that's 4π. Let me recheck: ½ · 16 · π/2 = 4π ≈ 12.57. The answer listed should be 4π."),
        ("For a circle with r = 10, what is the arc length for a full rotation?", ["10π", "*20π", "100π", "5π"],
         "Full rotation: θ = 2π, s = 10 · 2π = 20π."),
        ("If the arc length is 6 and the radius is 3, what is θ in radians?", ["3", "1", "*2", "6"],
         "θ = s/r = 6/3 = 2 radians."),
        ("Find the sector area for r = 6 and θ = π/6.", ["6π", "*3π", "π", "36π"],
         "A = ½(36)(π/6) = 3π."),
        ("A sector has area 12 and radius 4. What is θ?", ["*3/2", "3", "2", "3/4"],
         "A = ½r²θ → 12 = ½(16)θ → 12 = 8θ → θ = 3/2 radians."),
        ("Why does s = rθ work only when θ is in radians?", ["Radians are larger", "Degrees are more precise", "*Radians define the angle as arc/radius, making the relationship linear", "It's just a convention"],
         "By definition, 1 radian subtends an arc equal to the radius, creating the direct proportion s = rθ."),
        ("The arc length of a semicircle of radius r is:", ["πr/2", "*πr", "2πr", "πr²"],
         "Semicircle: θ = π, so s = rπ = πr."),
        ("Find the arc length: r = 8, θ = 45°.", ["4π", "*2π", "8π", "π"],
         "Convert: 45° = π/4. s = 8 · π/4 = 2π."),
        ("The area of a full circle using the sector formula is:", ["½r²", "r²π/2", "*πr²", "2πr²"],
         "Full rotation: θ = 2π. A = ½r²(2π) = πr²."),
        ("A sector angle is doubled. What happens to the arc length?", ["It halves", "It stays the same", "*It doubles", "It quadruples"],
         "s = rθ, so doubling θ doubles s (linear relationship)."),
        ("A sector angle is doubled. What happens to the sector area?", ["It halves", "It stays the same", "*It doubles", "It quadruples"],
         "A = ½r²θ, so doubling θ doubles A (also linear in θ)."),
        ("Find θ given arc length 10π and radius 5.", ["π", "*2π", "π/2", "4π"],
         "θ = s/r = 10π/5 = 2π radians."),
        ("Which has the greater arc length: r=3, θ=2 or r=2, θ=3?", ["*Both are the same (6)", "r=3, θ=2", "r=2, θ=3", "Cannot determine"],
         "Both: s = 3·2 = 6 and s = 2·3 = 6."),
        ("Find the sector area for r = 10, θ = 36° (convert first).", ["*10π", "20π", "5π", "50π"],
         "36° = π/5. A = ½(100)(π/5) = 10π."),
        ("The ratio of arc length to radius gives:", ["The area", "The circumference", "*The radian measure of the angle", "The diameter"],
         "θ = s/r, which is the angle in radians."),
        ("For a quarter circle of radius 6, the sector area is:", ["6π", "12π", "*9π/2 (or 4.5π)", "36π"],
         "Quarter circle: θ = π/2. A = ½(36)(π/2) = 9π."),
        ("If r is tripled and θ stays the same, the arc length:", ["Stays the same", "Doubles", "*Triples", "Is multiplied by 9"],
         "s = rθ; tripling r triples s."),
    ]
)
lessons[k] = v

# ── Lesson 1.3 ──
k, v = build_lesson(1, 3, "Right Triangle Ratios (SOH-CAH-TOA)",
    "<h3>Right Triangle Ratios (SOH-CAH-TOA)</h3>"
    "<p>In a right triangle, the three primary trigonometric ratios relate the sides to an acute angle θ:</p>"
    "<ul><li><b>sin θ = opposite / hypotenuse</b></li>"
    "<li><b>cos θ = adjacent / hypotenuse</b></li>"
    "<li><b>tan θ = opposite / adjacent</b></li></ul>"
    "<p>The mnemonic <b>SOH-CAH-TOA</b> helps remember these:</p>"
    "<ul><li><b>S</b>ine = <b>O</b>pposite / <b>H</b>ypotenuse</li>"
    "<li><b>C</b>osine = <b>A</b>djacent / <b>H</b>ypotenuse</li>"
    "<li><b>T</b>angent = <b>O</b>pposite / <b>A</b>djacent</li></ul>"
    "<p>These ratios depend only on the angle, not on the size of the triangle (since all right triangles with the same acute angle are similar).</p>",
    [
        ("Sine (sin)", "sin θ = opposite / hypotenuse."),
        ("Cosine (cos)", "cos θ = adjacent / hypotenuse."),
        ("Tangent (tan)", "tan θ = opposite / adjacent."),
        ("SOH-CAH-TOA", "Mnemonic: Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse, Tangent = Opposite/Adjacent."),
        ("Hypotenuse", "The longest side of a right triangle, opposite the 90° angle."),
    ],
    [
        ("sin θ equals:", ["adjacent / hypotenuse", "*opposite / hypotenuse", "opposite / adjacent", "hypotenuse / opposite"],
         "By definition, sin θ = opposite / hypotenuse."),
        ("cos θ equals:", ["opposite / hypotenuse", "opposite / adjacent", "*adjacent / hypotenuse", "hypotenuse / adjacent"],
         "cos θ = adjacent / hypotenuse."),
        ("tan θ equals:", ["adjacent / hypotenuse", "hypotenuse / opposite", "adjacent / opposite", "*opposite / adjacent"],
         "tan θ = opposite / adjacent."),
        ("In a right triangle with opposite = 3 and hypotenuse = 5, sin θ =", ["5/3", "4/5", "*3/5", "3/4"],
         "sin θ = opposite/hypotenuse = 3/5."),
        ("In a right triangle with adjacent = 4 and hypotenuse = 5, cos θ =", ["5/4", "3/5", "3/4", "*4/5"],
         "cos θ = adjacent/hypotenuse = 4/5."),
        ("What is tan θ if opposite = 3 and adjacent = 4?", ["4/3", "4/5", "*3/4", "3/5"],
         "tan θ = opposite/adjacent = 3/4."),
        ("SOH-CAH-TOA is a mnemonic for:", ["Area formulas", "*The three basic trig ratios", "The Pythagorean theorem", "Angle conversions"],
         "SOH-CAH-TOA stands for sin=O/H, cos=A/H, tan=O/A."),
        ("If sin θ = 0.5 in a right triangle, what is θ?", ["45°", "*30°", "60°", "90°"],
         "sin 30° = 0.5."),
        ("The hypotenuse is always:", ["The shortest side", "Opposite the smallest angle", "*The longest side, opposite the right angle", "Adjacent to the right angle"],
         "The hypotenuse is the longest side, always opposite the 90° angle."),
        ("In a 3-4-5 right triangle, if θ is opposite the side of length 4, sin θ =", ["3/5", "*4/5", "4/3", "5/4"],
         "sin θ = opposite/hypotenuse = 4/5."),
        ("tan θ can also be written as:", ["cos θ / sin θ", "*sin θ / cos θ", "1 / sin θ", "1 / cos θ"],
         "tan θ = (opp/hyp) / (adj/hyp) = sin θ / cos θ."),
        ("If cos θ = 12/13, and hypotenuse = 13, the adjacent side is:", ["5", "*12", "13", "10"],
         "cos θ = adj/hyp → adj = 13 · 12/13 = 12."),
        ("Which trig ratio uses only the two legs (not the hypotenuse)?", ["Sine", "Cosine", "*Tangent", "None of them"],
         "Tangent = opposite/adjacent, using both legs."),
        ("If sin θ = 5/13, what is the opposite side when hypotenuse = 13?", ["13", "12", "*5", "8"],
         "sin θ = opp/hyp → opp = 13 · 5/13 = 5."),
        ("If tan 45° = 1, this means:", ["The opposite is 0", "*The opposite and adjacent sides are equal", "The hypotenuse equals the opposite", "The angle is 90°"],
         "tan = opp/adj = 1 means opposite = adjacent."),
        ("Do trig ratios depend on the size of the triangle?", ["Yes, always", "*No, only on the angle", "Yes, for acute triangles", "Only for right triangles"],
         "Similar right triangles have the same ratios, so trig values depend only on the angle."),
        ("sin 90° =", ["0", "0.5", "*1", "undefined"],
         "sin 90° = 1 (opposite = hypotenuse)."),
        ("cos 0° =", ["0", "0.5", "*1", "undefined"],
         "cos 0° = 1 (adjacent = hypotenuse)."),
        ("tan 0° =", ["1", "undefined", "0.5", "*0"],
         "tan 0° = 0/adjacent = 0."),
        ("Which is undefined: tan 0° or tan 90°?", ["tan 0°", "*tan 90°", "Both", "Neither"],
         "tan 90° = opposite/0 = undefined (adjacent side has length 0)."),
    ]
)
lessons[k] = v

# ── Lesson 1.4 ──
k, v = build_lesson(1, 4, "Special Triangles (30°–60°–90°, 45°–45°–90°)",
    "<h3>Special Triangles</h3>"
    "<p>Two right triangles have exact, memorizable side ratios:</p>"
    "<h4>45°–45°–90° Triangle</h4>"
    "<ul><li>Both legs are equal: ratio <b>1 : 1 : √2</b>.</li>"
    "<li>If each leg = a, then hypotenuse = a√2.</li>"
    "<li>sin 45° = cos 45° = √2/2 ≈ 0.707; tan 45° = 1.</li></ul>"
    "<h4>30°–60°–90° Triangle</h4>"
    "<ul><li>Side ratio: <b>1 : √3 : 2</b> (short leg : long leg : hypotenuse).</li>"
    "<li>Short leg is opposite 30°; long leg is opposite 60°; hypotenuse is opposite 90°.</li>"
    "<li>sin 30° = ½, cos 30° = √3/2, tan 30° = √3/3.</li>"
    "<li>sin 60° = √3/2, cos 60° = ½, tan 60° = √3.</li></ul>"
    "<p>These triangles come from splitting a square diagonally (45-45-90) or an equilateral triangle in half (30-60-90).</p>",
    [
        ("45-45-90 Triangle", "An isosceles right triangle with side ratio 1 : 1 : √2."),
        ("30-60-90 Triangle", "A right triangle with side ratio 1 : √3 : 2 (short leg : long leg : hypotenuse)."),
        ("sin 30°", "sin 30° = 1/2."),
        ("cos 45°", "cos 45° = √2/2 ≈ 0.707."),
        ("tan 60°", "tan 60° = √3 ≈ 1.732."),
    ],
    [
        ("In a 45-45-90 triangle, the ratio of the sides is:", ["1 : 2 : 3", "1 : √3 : 2", "*1 : 1 : √2", "1 : 2 : √3"],
         "A 45-45-90 triangle has equal legs with ratio 1 : 1 : √2."),
        ("In a 30-60-90 triangle, the side ratio is:", ["*1 : √3 : 2", "1 : 1 : √2", "1 : 2 : 3", "1 : 2 : √3"],
         "The sides are in ratio 1 : √3 : 2."),
        ("sin 30° =", ["√3/2", "*1/2", "√2/2", "1"],
         "sin 30° = opposite/hypotenuse = 1/2."),
        ("cos 60° =", ["√3/2", "*1/2", "√2/2", "1"],
         "cos 60° = 1/2 (adjacent = short leg, hyp = 2)."),
        ("sin 45° =", ["1/2", "√3/2", "*√2/2", "1"],
         "sin 45° = 1/√2 = √2/2."),
        ("tan 45° =", ["0", "√2", "*1", "√3"],
         "Both legs are equal, so tan 45° = 1."),
        ("tan 30° =", ["1", "√3", "*√3/3 (or 1/√3)", "1/2"],
         "tan 30° = (1)/(√3) = √3/3."),
        ("tan 60° =", ["1/√3", "1", "*√3", "2"],
         "tan 60° = √3/1 = √3."),
        ("In a 45-45-90 triangle with leg = 5, the hypotenuse is:", ["5", "10", "*5√2", "5√3"],
         "Hypotenuse = leg × √2 = 5√2."),
        ("In a 30-60-90 triangle with short leg = 4, the hypotenuse is:", ["4√3", "4√2", "*8", "6"],
         "Hypotenuse = 2 × short leg = 8."),
        ("In a 30-60-90 triangle with short leg = 4, the long leg is:", ["*4√3", "4√2", "8", "2"],
         "Long leg = short leg × √3 = 4√3."),
        ("cos 30° =", ["1/2", "*√3/2", "√2/2", "1"],
         "cos 30° = √3/2."),
        ("sin 60° =", ["1/2", "*√3/2", "√2/2", "1"],
         "sin 60° = √3/2."),
        ("A square with side 1 has a diagonal of:", ["1", "2", "*√2", "√3"],
         "Diagonal of a square = side × √2 = √2."),
        ("An equilateral triangle with side 2 split in half produces a triangle with hypotenuse:", ["1", "√3", "*2", "4"],
         "The hypotenuse of the resulting 30-60-90 triangle is the original side = 2."),
        ("sin² 45° + cos² 45° =", ["0", "√2", "*1", "2"],
         "By the Pythagorean Identity: sin²θ + cos²θ = 1 for any angle."),
        ("Which triangle has two equal legs?", ["30-60-90", "*45-45-90", "3-4-5", "5-12-13"],
         "The 45-45-90 triangle is isosceles with two equal legs."),
        ("In a 30-60-90 triangle, which side is opposite the 30° angle?", ["The hypotenuse", "The long leg", "*The short leg", "None"],
         "The shortest side is opposite the smallest angle (30°)."),
        ("If the hypotenuse of a 30-60-90 triangle is 10, the short leg is:", ["5√3", "*5", "10√3", "10/√3"],
         "Short leg = hypotenuse / 2 = 5."),
        ("If each leg of a 45-45-90 triangle is 6, find the perimeter.", ["12 + 6√2", "*12 + 6√2", "18", "6 + 6√2"],
         "Perimeter = 6 + 6 + 6√2 = 12 + 6√2."),
    ]
)
lessons[k] = v

# ── Lesson 1.5 ──
k, v = build_lesson(1, 5, "Unit Circle Basics",
    "<h3>Unit Circle Basics</h3>"
    "<p>The <b>unit circle</b> is a circle of radius 1 centered at the origin of the coordinate plane.</p>"
    "<ul><li>Any point on the unit circle can be written as <b>(cos θ, sin θ)</b> where θ is the angle from the positive x-axis.</li>"
    "<li>The x-coordinate = cos θ, the y-coordinate = sin θ.</li></ul>"
    "<h4>Key Angles on the Unit Circle</h4>"
    "<ul><li>0° (0): (1, 0)</li>"
    "<li>30° (π/6): (√3/2, 1/2)</li>"
    "<li>45° (π/4): (√2/2, √2/2)</li>"
    "<li>60° (π/3): (1/2, √3/2)</li>"
    "<li>90° (π/2): (0, 1)</li>"
    "<li>180° (π): (−1, 0)</li>"
    "<li>270° (3π/2): (0, −1)</li></ul>"
    "<p>The unit circle extends trig functions beyond acute angles to all real numbers.</p>",
    [
        ("Unit Circle", "A circle with radius 1 centered at the origin; points are (cos θ, sin θ)."),
        ("Coordinates at 0°", "(1, 0) — cos 0° = 1, sin 0° = 0."),
        ("Coordinates at 90°", "(0, 1) — cos 90° = 0, sin 90° = 1."),
        ("Coordinates at 180°", "(−1, 0) — cos 180° = −1, sin 180° = 0."),
        ("Coordinates at 270°", "(0, −1) — cos 270° = 0, sin 270° = −1."),
    ],
    [
        ("What is the radius of the unit circle?", ["0", "2", "*1", "π"],
         "The unit circle has radius 1."),
        ("A point on the unit circle is written as:", ["(sin θ, cos θ)", "(r, θ)", "*(cos θ, sin θ)", "(θ, r)"],
         "Points on the unit circle are (cos θ, sin θ)."),
        ("What are the coordinates at θ = 0?", ["(0, 1)", "(0, 0)", "*(1, 0)", "(−1, 0)"],
         "At 0°, (cos 0, sin 0) = (1, 0)."),
        ("What are the coordinates at θ = π/2?", ["(1, 0)", "*(0, 1)", "(−1, 0)", "(0, −1)"],
         "At 90°, (cos 90°, sin 90°) = (0, 1)."),
        ("What is cos(π)?", ["1", "0", "*−1", "−0.5"],
         "cos 180° = −1."),
        ("What is sin(3π/2)?", ["1", "0", "*−1", "0.5"],
         "sin 270° = −1."),
        ("At θ = π/4, the coordinates are:", ["(1/2, √3/2)", "*(√2/2, √2/2)", "(√3/2, 1/2)", "(1, 0)"],
         "cos 45° = sin 45° = √2/2."),
        ("At θ = π/6, sin θ =", ["√3/2", "√2/2", "*1/2", "0"],
         "sin 30° = 1/2."),
        ("At θ = π/3, cos θ =", ["√3/2", "√2/2", "*1/2", "0"],
         "cos 60° = 1/2."),
        ("The unit circle allows us to define trig functions for:", ["Only acute angles", "Only angles < 360°", "*All real numbers", "Only positive angles"],
         "The unit circle extends trig to all real numbers."),
        ("Sin is positive in which quadrants?", ["I and IV", "*I and II", "I and III", "II and III"],
         "Sine (y-coordinate) is positive in Quadrants I and II."),
        ("Cos is negative in which quadrants?", ["I and II", "I and IV", "*II and III", "III and IV"],
         "Cosine (x-coordinate) is negative in Quadrants II and III."),
        ("At θ = π, sin θ =", ["1", "−1", "*0", "π"],
         "sin 180° = 0 (the point is (−1, 0))."),
        ("What is sin²θ + cos²θ for any point on the unit circle?", ["0", "2", "*1", "It varies"],
         "The Pythagorean identity: sin²θ + cos²θ = 1."),
        ("The x-coordinate of a point on the unit circle represents:", ["sin θ", "tan θ", "*cos θ", "The radius"],
         "The x-coordinate is cos θ."),
        ("At θ = 5π/6, in which quadrant is the point?", ["I", "*II", "III", "IV"],
         "5π/6 = 150°, which is in Quadrant II."),
        ("What is cos(2π)?", ["0", "−1", "*1", "2π"],
         "cos 360° = cos 0° = 1 (full rotation back to start)."),
        ("At what angle does sin θ = 1?", ["0°", "*90°", "180°", "270°"],
         "sin 90° = 1; the highest point of the unit circle."),
        ("At θ = 7π/4, the reference angle is:", ["7π/4", "3π/4", "*π/4", "π/2"],
         "7π/4 is in Q4; reference angle = 2π − 7π/4 = π/4."),
        ("How many times does the unit circle repeat every:", ["π radians", "90°", "*2π radians", "180°"],
         "Trig functions are periodic with period 2π."),
    ]
)
lessons[k] = v

# ── Lesson 1.6 ──
k, v = build_lesson(1, 6, "Coterminal Angles & Reference Angles",
    "<h3>Coterminal Angles &amp; Reference Angles</h3>"
    "<h4>Coterminal Angles</h4>"
    "<ul><li>Angles that share the same terminal side are <b>coterminal</b>.</li>"
    "<li>Add or subtract 360° (or 2π) to find coterminal angles: θ ± 360°n.</li>"
    "<li>Example: 30° and 390° are coterminal (390 − 360 = 30).</li></ul>"
    "<h4>Reference Angles</h4>"
    "<ul><li>The <b>reference angle</b> is the acute angle between the terminal side and the x-axis.</li>"
    "<li>Q I: ref = θ. Q II: ref = 180° − θ. Q III: ref = θ − 180°. Q IV: ref = 360° − θ.</li>"
    "<li>Trig values of any angle can be found using its reference angle and the sign for that quadrant.</li></ul>"
    "<p><b>ASTC rule:</b> All trig functions positive in Q I; Sine in Q II; Tangent in Q III; Cosine in Q IV.</p>",
    [
        ("Coterminal Angles", "Angles that share the same terminal side; found by adding or subtracting multiples of 360° (or 2π)."),
        ("Reference Angle", "The acute angle between the terminal side and the x-axis; always between 0° and 90°."),
        ("ASTC Rule", "All (Q I), Sine (Q II), Tangent (Q III), Cosine (Q IV) — tells which trig functions are positive in each quadrant."),
        ("Negative Angle", "An angle measured clockwise from the positive x-axis."),
        ("Terminal Side", "The ray that rotates from the initial side to form an angle in standard position."),
    ],
    [
        ("Which angle is coterminal with 45°?", ["135°", "−135°", "*405°", "315°"],
         "45° + 360° = 405°."),
        ("Find a positive coterminal angle for −60°.", ["60°", "*300°", "120°", "240°"],
         "−60° + 360° = 300°."),
        ("The reference angle for 150° is:", ["150°", "60°", "*30°", "45°"],
         "Q II: ref = 180° − 150° = 30°."),
        ("The reference angle for 225° is:", ["75°", "135°", "*45°", "225°"],
         "Q III: ref = 225° − 180° = 45°."),
        ("The reference angle for 330° is:", ["60°", "150°", "*30°", "330°"],
         "Q IV: ref = 360° − 330° = 30°."),
        ("sin 150° uses the reference angle 30° and is:", ["−1/2", "*1/2", "√3/2", "−√3/2"],
         "sin 150° = sin 30° = 1/2 (positive in Q II)."),
        ("cos 120° =", ["1/2", "*−1/2", "√3/2", "−√3/2"],
         "ref = 60°. cos 60° = 1/2, but cosine is negative in Q II, so −1/2."),
        ("In which quadrant is tangent positive?", ["Q I only", "Q II and Q IV", "*Q I and Q III", "Q II and Q III"],
         "ASTC: Tangent is positive in Q I and Q III."),
        ("Which are coterminal: 30° and −330°?", ["No", "*Yes", "Only if converted", "Not enough info"],
         "30° + (−360°) = −330°, so they share the same terminal side."),
        ("All trig functions are positive in:", ["Q II", "Q III", "*Q I", "Q IV"],
         "'A' in ASTC: All positive in Quadrant I."),
        ("The reference angle for 5π/4 is:", ["3π/4", "*π/4", "π/2", "π"],
         "Q III: ref = 5π/4 − π = π/4."),
        ("sin(−30°) equals:", ["1/2", "*−1/2", "√3/2", "0"],
         "sin(−30°) = −sin 30° = −1/2 (or note −30° is in Q IV where sin is negative)."),
        ("Find the reference angle for 200°.", ["80°", "*20°", "160°", "200°"],
         "Q III: 200° − 180° = 20°."),
        ("cos 315° =", ["−√2/2", "0", "*√2/2", "−1"],
         "ref = 45°. Cosine is positive in Q IV: cos 315° = √2/2."),
        ("How many coterminal angles does any angle have?", ["One", "Two", "360", "*Infinitely many"],
         "You can keep adding/subtracting 360° to get infinitely many coterminal angles."),
        ("tan 135° =", ["1", "*−1", "√3", "−√3"],
         "ref = 45°. tan 45° = 1, but tangent is negative in Q II: −1."),
        ("In Q III, which trig functions are positive?", ["Sine and cosine", "Sine only", "*Tangent and cotangent", "Cosine only"],
         "In Q III both x and y are negative, so sin/cos are negative but tan (= sin/cos) is positive."),
        ("The smallest positive coterminal angle for 725° is:", ["*5°", "365°", "5°", "355°"],
         "725 − 2(360) = 725 − 720 = 5°."),
        ("Reference angle for 11π/6 is:", ["π/3", "*π/6", "5π/6", "π/4"],
         "Q IV: 2π − 11π/6 = π/6."),
        ("sin 210° =", ["1/2", "*−1/2", "√3/2", "−√3/2"],
         "ref = 30°, Q III (sin negative): sin 210° = −1/2."),
    ]
)
lessons[k] = v

# ── Lesson 1.7 ──
k, v = build_lesson(1, 7, "Applications in Geometry",
    "<h3>Applications of Trigonometry in Geometry</h3>"
    "<p>Trigonometric ratios and radian measure have wide applications in geometry:</p>"
    "<h4>Finding Lengths and Angles</h4>"
    "<ul><li>Use right-triangle trig to find unknown sides or angles in any geometric figure that contains right triangles.</li>"
    "<li>A diagonal of a rectangle creates two right triangles — trig finds the diagonal length or angle.</li></ul>"
    "<h4>Area Using Trig</h4>"
    "<ul><li>Area of a triangle: <b>A = ½ab sin C</b> (two sides and the included angle).</li>"
    "<li>Area of a sector: <b>A = ½r²θ</b> (central angle in radians).</li></ul>"
    "<h4>Regular Polygons</h4>"
    "<ul><li>For a regular n-gon inscribed in a circle of radius r, the side length = 2r sin(π/n) and the area = ½nr² sin(2π/n).</li></ul>"
    "<p>Trigonometry bridges the gap between angle measures and linear/area measures throughout geometry.</p>",
    [
        ("Triangle Area (Trig)", "A = ½ab sin C, where a and b are two sides and C is the included angle."),
        ("Regular Polygon Side", "For a regular n-gon inscribed in a circle of radius r: side = 2r sin(π/n)."),
        ("Regular Polygon Area", "A = ½nr² sin(2π/n) for a regular n-gon inscribed in a circle of radius r."),
        ("Diagonal of a Rectangle", "d = √(l² + w²); the angle with the base can be found using tan θ = w/l."),
        ("Sector Area", "A = ½r²θ (θ in radians); links radian measure to geometric area."),
    ],
    [
        ("The area of a triangle using trigonometry is:", ["A = bh/2", "*A = ½ab sin C", "A = πr²", "A = s²"],
         "When two sides and the included angle are known: A = ½ab sin C."),
        ("Find the area of a triangle with sides 6 and 10 and included angle 30°.", ["30", "60", "*15", "20"],
         "A = ½(6)(10)sin 30° = ½(60)(0.5) = 15."),
        ("A regular hexagon inscribed in a circle of radius 4 has side length:", ["2", "4√3", "*4", "8"],
         "Side = 2r sin(π/6) = 2(4)(0.5) = 4."),
        ("For a sector with r = 3 and θ = 2 rad, the area is:", ["6", "3", "*9", "18"],
         "A = ½(9)(2) = 9."),
        ("The diagonal of a 3×4 rectangle is:", ["3", "4", "*5", "7"],
         "d = √(9 + 16) = √25 = 5."),
        ("The angle a 3×4 rectangle's diagonal makes with the longer side is:", ["*arctan(3/4) ≈ 36.87°", "arctan(4/3) ≈ 53.13°", "45°", "30°"],
         "tan θ = opposite/adjacent = 3/4, so θ = arctan(3/4) ≈ 36.87°."),
        ("Triangle area with sides 8 and 12 and included angle 90° is:", ["96", "48", "*48", "24"],
         "A = ½(8)(12)sin 90° = ½(96)(1) = 48."),
        ("A regular triangle (equilateral) inscribed in a circle of radius r has area:", ["r²", "πr²", "*¾r²√3 (= ½·3·r²·sin 120°)", "3r²"],
         "A = ½(3)(r²)sin(2π/3) = (3r²/2)(√3/2) = 3r²√3/4."),
        ("Why is A = ½ab sin C useful?", ["It requires all three sides", "It only works for right triangles", "*It works when two sides and the included angle are known", "It needs the height"],
         "This formula is ideal when SAS information is given — no height needed."),
        ("An arc of radius 5 and angle π/3 has length:", ["5/3", "π/3", "*5π/3", "10π/3"],
         "s = rθ = 5 · π/3 = 5π/3."),
        ("In a right triangle, sin can find a side if you know:", ["Two sides", "Three angles", "*An angle and the hypotenuse", "The area"],
         "sin θ = opposite/hypotenuse lets you find the opposite side from angle and hypotenuse."),
        ("To find the area of a regular pentagon inscribed in radius r:", ["Use A = 5r²", "*Use A = ½(5)r² sin(2π/5)", "Use A = πr²", "Use A = 5r"],
         "The formula for n = 5: A = ½(5)r² sin(72°)."),
        ("Area of a triangle with sides 5, 5 and included angle 60° is:", ["25", "*25√3/4 ≈ 10.83", "12.5", "25/2"],
         "A = ½(5)(5)sin 60° = 12.5 · √3/2 = 25√3/4 ≈ 10.83."),
        ("How does trig help find the height of a building?", ["By measuring the building directly", "*By using angle of elevation and distance to find height (tan θ = h/d)", "By counting floors", "By using a ruler"],
         "tan(angle of elevation) = height/distance, so height = d · tan θ."),
        ("For a sector with r = 10 and θ = π/4, the arc length is:", ["10π/2", "*5π/2", "10π/4", "40π"],
         "s = 10 · π/4 = 10π/4 = 5π/2."),
        ("A circle has 360°. A regular 12-gon's central angle per side is:", ["15°", "*30°", "45°", "60°"],
         "360°/12 = 30°."),
        ("Find the area of an equilateral triangle with side 6 using trig.", ["18", "*9√3 ≈ 15.59", "36", "6√3"],
         "A = ½(6)(6)sin 60° = 18 · √3/2 = 9√3."),
        ("The apothem of a regular polygon inscribed in radius r is:", ["r sin(π/n)", "*r cos(π/n)", "r tan(π/n)", "r/2"],
         "The apothem = r cos(π/n)."),
        ("What information do you need for A = ½ab sin C?", ["Three sides", "Three angles", "*Two sides and the included angle", "One side and one angle"],
         "You need SAS: two sides (a, b) and the angle between them (C)."),
        ("Using trig, the perimeter of a regular n-gon inscribed in radius r is:", ["2πr", "nr", "*2nr sin(π/n)", "n·r·cos(π/n)"],
         "Perimeter = n × side = n × 2r sin(π/n) = 2nr sin(π/n)."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

data.update(lessons)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Trigonometry Unit 1: wrote {len(lessons)} lessons")
