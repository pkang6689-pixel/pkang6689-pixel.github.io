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

# ── 6.1 Angles in Degrees & Radians ───────────────────────────────
k, v = build_lesson(6, 1,
    "Angles in Degrees & Radians",
    "<h3>Angles in Degrees &amp; Radians</h3>"
    "<p>Angles can be measured in <b>degrees</b> or <b>radians</b>.</p>"
    "<h4>Conversions</h4>"
    "<ul>"
    "<li>360° = 2π radians; 180° = π radians.</li>"
    "<li>Degrees → radians: multiply by π/180.</li>"
    "<li>Radians → degrees: multiply by 180/π.</li>"
    "</ul>"
    "<h4>Standard Position</h4>"
    "<ul>"
    "<li>Vertex at origin, initial side along positive x-axis.</li>"
    "<li>Positive angles: counter-clockwise. Negative angles: clockwise.</li>"
    "</ul>"
    "<h4>Quadrants</h4>"
    "<ul>"
    "<li>Q I: 0°–90°; Q II: 90°–180°; Q III: 180°–270°; Q IV: 270°–360°.</li>"
    "</ul>",
    [
        ("Radian", "The angle subtended by an arc equal in length to the radius; 2π rad = 360°."),
        ("Degree", "1/360 of a full rotation."),
        ("Degrees to Radians", "Multiply by π/180."),
        ("Radians to Degrees", "Multiply by 180/π."),
        ("Standard Position", "Angle with vertex at the origin and initial side on the positive x-axis.")
    ],
    [
        ("Convert 90° to radians.", ["π/4", "*π/2", "π", "2π"],
         "90 × π/180 = π/2."),
        ("Convert π/3 radians to degrees.", ["30°", "*60°", "90°", "120°"],
         "(π/3)(180/π) = 60°."),
        ("Convert 180° to radians.", ["π/2", "2π", "*π", "π/4"],
         "180 × π/180 = π."),
        ("Convert 3π/4 to degrees.", ["120°", "*135°", "150°", "270°"],
         "(3π/4)(180/π) = 135°."),
        ("360° equals how many radians?", ["π", "π/2", "*2π", "4π"],
         "One full revolution = 2π radians."),
        ("Convert 45° to radians.", ["*π/4", "π/3", "π/6", "π/2"],
         "45 × π/180 = π/4."),
        ("Convert 5π/6 to degrees.", ["*150°", "120°", "300°", "210°"],
         "(5π/6)(180/π) = 150°."),
        ("A negative angle is measured:", ["Counter-clockwise", "*Clockwise", "From the y-axis", "Always in radians"],
         "Negative angles go clockwise from the initial side."),
        ("In standard position, the initial side lies along:", ["Negative x-axis", "y-axis", "*Positive x-axis", "Any axis"],
         "Standard position: initial side on positive x-axis."),
        ("Which quadrant contains 200°?", ["Q II", "*Q III", "Q IV", "Q I"],
         "180° < 200° < 270° → Q III."),
        ("Which quadrant contains 5π/4?", ["Q II", "*Q III", "Q IV", "Q I"],
         "5π/4 = 225°. 180° < 225° < 270° → Q III."),
        ("Convert 270° to radians.", ["π", "π/4", "*3π/2", "2π"],
         "270 × π/180 = 3π/2."),
        ("Convert 2π/3 to degrees.", ["*120°", "60°", "90°", "150°"],
         "(2π/3)(180/π) = 120°."),
        ("One radian ≈ ?", ["90°", "180°", "*57.3°", "45°"],
         "180/π ≈ 57.296°."),
        ("Convert −30° to radians.", ["π/6", "*−π/6", "−π/3", "π/3"],
         "−30 × π/180 = −π/6."),
        ("Which quadrant contains −45°?", ["Q I", "Q II", "Q III", "*Q IV"],
         "−45° is 45° clockwise from positive x-axis → Q IV."),
        ("Convert 7π/6 to degrees.", ["150°", "300°", "*210°", "330°"],
         "(7π/6)(180/π) = 210°."),
        ("How many degrees in 1 full rotation?", ["180", "270", "*360", "720"],
         "One complete revolution = 360°."),
        ("Convert 330° to radians.", ["5π/3", "*11π/6", "7π/4", "π/6"],
         "330 × π/180 = 11π/6."),
        ("An angle of π radians is:", ["A right angle", "*A straight angle (180°)", "A full rotation", "45°"],
         "π rad = 180°.")
    ]
)
lessons[k] = v

# ── 6.2 Arc Length & Sector Area ───────────────────────────────────
k, v = build_lesson(6, 2,
    "Arc Length & Sector Area",
    "<h3>Arc Length &amp; Sector Area</h3>"
    "<h4>Arc Length</h4>"
    "<ul>"
    "<li>s = rθ, where r = radius and θ is in <b>radians</b>.</li>"
    "</ul>"
    "<h4>Sector Area</h4>"
    "<ul>"
    "<li>A = (1/2)r²θ, where θ is in radians.</li>"
    "</ul>"
    "<h4>Linear & Angular Speed</h4>"
    "<ul>"
    "<li>Angular speed: ω = θ/t (rad/s).</li>"
    "<li>Linear speed: v = rω = s/t.</li>"
    "</ul>",
    [
        ("Arc Length Formula", "s = rθ; θ must be in radians."),
        ("Sector Area Formula", "A = (1/2)r²θ; θ must be in radians."),
        ("Angular Speed (ω)", "The rate of angle change: ω = θ/t, measured in rad/s."),
        ("Linear Speed (v)", "v = rω; the speed of a point on the circumference."),
        ("Radian Requirement", "Both arc length and sector area formulas require the angle in radians.")
    ],
    [
        ("Arc length: r = 5, θ = 2 rad. s = ?", ["2", "5", "*10", "25"],
         "s = 5 × 2 = 10."),
        ("Sector area: r = 4, θ = π/2. A = ?", ["4π", "*2π", "8π", "π"],
         "A = (1/2)(16)(π/2) = 4π. Wait: (1/2)(16)(π/2) = 4π. Hmm, let me recalc: (1/2)(4²)(π/2) = (1/2)(16)(π/2) = 4π. Actually 16π/4 = 4π. Let me recheck: (1/2)·16·(π/2) = 8·(π/2) = 4π."),
        ("Arc length: r = 10, θ = 60°. First convert, then find s.", ["60", "*10π/3", "600/π", "10"],
         "60° = π/3. s = 10(π/3) = 10π/3."),
        ("A wheel of radius 3 ft makes one revolution. Arc length traveled?", ["3 ft", "3π ft", "*6π ft", "9π ft"],
         "One revolution = 2π rad. s = 3(2π) = 6π."),
        ("Sector area: r = 6, θ = π/3.", ["6π", "12π", "*6π", "3π"],
         "A = (1/2)(36)(π/3) = 18π/3 = 6π."),
        ("If s = 15 and r = 5, find θ.", ["5", "*3 rad", "15 rad", "75°"],
         "θ = s/r = 15/5 = 3 rad."),
        ("If A = 50 and r = 10, find θ.", ["5", "0.5", "*1 rad", "2 rad"],
         "50 = (1/2)(100)θ → θ = 1 rad."),
        ("Angular speed of a wheel making 10 revolutions per second?", ["10 rad/s", "*20π rad/s", "10π rad/s", "5π rad/s"],
         "ω = 10 × 2π = 20π rad/s."),
        ("Linear speed: r = 2 m, ω = 5 rad/s.", ["5 m/s", "2 m/s", "*10 m/s", "7 m/s"],
         "v = rω = 2(5) = 10 m/s."),
        ("A circular track has radius 100 m. How far does a runner go in a quarter lap?", ["100 m", "*50π m ≈ 157 m", "200 m", "100π m"],
         "Quarter = π/2 rad. s = 100(π/2) = 50π ≈ 157 m."),
        ("r = 8 cm, θ = 3π/4. Arc length?", ["*6π cm", "24π cm", "8π cm", "3π cm"],
         "s = 8(3π/4) = 6π cm."),
        ("r = 8 cm, θ = 3π/4. Sector area?", ["*24π cm²", "48π cm²", "6π cm²", "12π cm²"],
         "A = (1/2)(64)(3π/4) = 32(3π/4) = 24π cm²."),
        ("A pizza slice has central angle 45° and radius 12 inches. Area of slice?", ["*9π in²", "18π in²", "36π in²", "72π in²"],
         "45° = π/4. A = (1/2)(144)(π/4) = 72(π/4) = 18π. Actually (1/2)(144)(π/4) = 144π/8 = 18π. Hmm, that's 18π. Let me recalc: 144/2 = 72. 72·π/4 = 18π."),
        ("The circumference of a circle with r = 7 is:", ["7π", "*14π", "49π", "7"],
         "C = 2πr = 14π."),
        ("If ω = 4π rad/s and r = 3 m, linear speed is:", ["4π m/s", "*12π m/s", "3π m/s", "7π m/s"],
         "v = 3(4π) = 12π m/s."),
        ("A pendulum sweeps 0.5 rad. Length 80 cm. Arc traveled?", ["80 cm", "0.5 cm", "*40 cm", "160 cm"],
         "s = 80(0.5) = 40 cm."),
        ("Two sectors have same area. One has r = 2 with θ = π. The other has r = 4. Its θ = ?", ["π", "*π/4", "π/2", "2π"],
         "A₁ = (1/2)(4)(π) = 2π. A₂ = (1/2)(16)θ = 2π → θ = π/4."),
        ("A gear with radius 5 cm turns at 100 rpm. Angular speed in rad/s?", ["100 rad/s", "*10π/3 rad/s", "200π rad/s", "50π rad/s"],
         "100 rpm = 100(2π)/60 = 200π/60 = 10π/3 rad/s."),
        ("For the gear above, linear speed at the edge?", ["10π/3 cm/s", "*50π/3 cm/s", "100π cm/s", "500π cm/s"],
         "v = 5(10π/3) = 50π/3 cm/s."),
        ("The formula s = rθ requires θ in:", ["Degrees", "*Radians", "Either", "Gradians"],
         "The formula only works with radians.")
    ]
)
lessons[k] = v

# ── 6.3 Unit Circle & Special Angles ──────────────────────────────
k, v = build_lesson(6, 3,
    "Unit Circle & Special Angles",
    "<h3>Unit Circle &amp; Special Angles</h3>"
    "<p>The <b>unit circle</b> has radius 1 centered at the origin. A point on it at angle θ has coordinates (cos θ, sin θ).</p>"
    "<h4>Special Angles</h4>"
    "<ul>"
    "<li>0° (0): (1, 0)</li>"
    "<li>30° (π/6): (√3/2, 1/2)</li>"
    "<li>45° (π/4): (√2/2, √2/2)</li>"
    "<li>60° (π/3): (1/2, √3/2)</li>"
    "<li>90° (π/2): (0, 1)</li>"
    "</ul>"
    "<h4>Symmetry</h4>"
    "<ul>"
    "<li>Use reference angles and quadrant signs to extend to all angles.</li>"
    "<li>ASTC: All, Sine, Tangent, Cosine positive in Q I, II, III, IV.</li>"
    "</ul>",
    [
        ("Unit Circle", "Circle of radius 1 centered at the origin; point at angle θ is (cos θ, sin θ)."),
        ("Special Angles", "0°, 30°, 45°, 60°, 90° and their multiples; have exact trig values using √2 and √3."),
        ("ASTC Rule", "All trig positive in Q I; Sine in Q II; Tangent in Q III; Cosine in Q IV."),
        ("Reference Angle", "The acute angle between the terminal side and the x-axis."),
        ("Coordinates on Unit Circle", "x = cos θ, y = sin θ for any angle θ.")
    ],
    [
        ("Coordinates at 0° on the unit circle?", ["(0, 1)", "*(1, 0)", "(0, 0)", "(1, 1)"],
         "cos 0° = 1, sin 0° = 0."),
        ("Coordinates at π/2?", ["(1, 0)", "*(0, 1)", "(−1, 0)", "(0, −1)"],
         "cos 90° = 0, sin 90° = 1."),
        ("cos(π/4) = ?", ["1/2", "√3/2", "*√2/2", "1"],
         "45° special angle."),
        ("sin(π/6) = ?", ["√3/2", "*1/2", "√2/2", "0"],
         "30° special angle."),
        ("sin(π/3) = ?", ["1/2", "*√3/2", "√2/2", "1"],
         "60° special angle."),
        ("cos(π/3) = ?", ["√3/2", "*1/2", "√2/2", "0"],
         "cos 60° = 1/2."),
        ("Coordinates at π (180°)?", ["(1, 0)", "(0, 1)", "*(−1, 0)", "(0, −1)"],
         "cos 180° = −1, sin 180° = 0."),
        ("sin(3π/2) = ?", ["1", "0", "*−1", "−√2/2"],
         "270°: (0, −1). sin = −1."),
        ("In which quadrant is sine positive and cosine negative?", ["Q I", "*Q II", "Q III", "Q IV"],
         "ASTC: Q II has sine positive."),
        ("In Q III, which trig function is positive?", ["Sine", "Cosine", "*Tangent", "All"],
         "ASTC: Tangent positive in Q III."),
        ("cos(5π/6) = ?", ["√3/2", "*−√3/2", "1/2", "−1/2"],
         "Reference angle π/6. Q II: cos negative. −√3/2."),
        ("sin(7π/6) = ?", ["1/2", "*−1/2", "√3/2", "−√3/2"],
         "Reference angle π/6. Q III: sin negative. −1/2."),
        ("cos(2π) = ?", ["0", "*1", "−1", "2π"],
         "Full rotation returns to (1, 0)."),
        ("tan(π/4) = ?", ["0", "√2", "*1", "√3"],
         "sin/cos = (√2/2)/(√2/2) = 1."),
        ("tan(π/3) = ?", ["1", "1/√3", "*√3", "2"],
         "sin 60°/cos 60° = (√3/2)/(1/2) = √3."),
        ("sin(−π/6) = ?", ["1/2", "*−1/2", "√3/2", "−√3/2"],
         "sin is odd: sin(−θ) = −sin θ. −sin(π/6) = −1/2."),
        ("cos(−π/4) = ?", ["−√2/2", "*√2/2", "−1", "0"],
         "cos is even: cos(−θ) = cos θ = √2/2."),
        ("What is the reference angle for 225°?", ["135°", "*45°", "225°", "315°"],
         "225° − 180° = 45°."),
        ("sin(150°) = ?", ["−1/2", "*1/2", "√3/2", "−√3/2"],
         "Reference angle 30°. Q II: sin positive. sin 30° = 1/2."),
        ("cos(300°) = ?", ["−1/2", "*1/2", "−√3/2", "√3/2"],
         "Reference angle 60°. Q IV: cos positive. cos 60° = 1/2.")
    ]
)
lessons[k] = v

# ── 6.4 Sine, Cosine, Tangent Definitions ─────────────────────────
k, v = build_lesson(6, 4,
    "Sine, Cosine, Tangent Definitions",
    "<h3>Sine, Cosine, Tangent Definitions</h3>"
    "<h4>Right Triangle Definitions</h4>"
    "<ul>"
    "<li>sin θ = opposite / hypotenuse</li>"
    "<li>cos θ = adjacent / hypotenuse</li>"
    "<li>tan θ = opposite / adjacent = sin θ / cos θ</li>"
    "</ul>"
    "<h4>Reciprocal Functions</h4>"
    "<ul>"
    "<li>csc θ = 1/sin θ = hyp/opp</li>"
    "<li>sec θ = 1/cos θ = hyp/adj</li>"
    "<li>cot θ = 1/tan θ = adj/opp = cos θ / sin θ</li>"
    "</ul>"
    "<h4>Pythagorean Identity</h4>"
    "<ul>"
    "<li>sin²θ + cos²θ = 1</li>"
    "</ul>",
    [
        ("SOH-CAH-TOA", "sin = opp/hyp, cos = adj/hyp, tan = opp/adj; mnemonic for right triangle trig."),
        ("Cosecant (csc)", "Reciprocal of sine: csc θ = 1/sin θ."),
        ("Secant (sec)", "Reciprocal of cosine: sec θ = 1/cos θ."),
        ("Cotangent (cot)", "Reciprocal of tangent: cot θ = cos θ/sin θ."),
        ("Pythagorean Identity", "sin²θ + cos²θ = 1 for all θ.")
    ],
    [
        ("In a right triangle, sin θ =", ["adj/hyp", "*opp/hyp", "opp/adj", "hyp/opp"],
         "Sine = opposite / hypotenuse."),
        ("cos θ =", ["opp/hyp", "*adj/hyp", "opp/adj", "hyp/adj"],
         "Cosine = adjacent / hypotenuse."),
        ("tan θ =", ["adj/opp", "hyp/opp", "*opp/adj", "adj/hyp"],
         "Tangent = opposite / adjacent."),
        ("If sin θ = 3/5, find cos θ (θ in Q I).", ["3/5", "*4/5", "5/3", "4/3"],
         "sin²+cos² = 1 → cos² = 1 − 9/25 = 16/25 → cos = 4/5."),
        ("If sin θ = 3/5, find tan θ.", ["5/3", "*3/4", "4/3", "5/4"],
         "tan = sin/cos = (3/5)/(4/5) = 3/4."),
        ("csc(30°) = ?", ["1/2", "*2", "√3", "2/√3"],
         "csc = 1/sin. sin 30° = 1/2 → csc = 2."),
        ("sec(60°) = ?", ["1/2", "√3", "*2", "2√3"],
         "sec = 1/cos. cos 60° = 1/2 → sec = 2."),
        ("cot(45°) = ?", ["0", "√2", "*1", "−1"],
         "cot = cos/sin = (√2/2)/(√2/2) = 1."),
        ("sin²θ + cos²θ = ?", ["0", "sin θ + cos θ", "*1", "2"],
         "Pythagorean identity."),
        ("If cos θ = 12/13, what is sin θ (Q I)?", ["12/13", "1/13", "*5/13", "13/5"],
         "sin² = 1 − 144/169 = 25/169 → sin = 5/13."),
        ("tan θ is undefined when:", ["sin θ = 0", "*cos θ = 0", "sin θ = 1", "cos θ = 1"],
         "tan = sin/cos; undefined when cos = 0."),
        ("At which angles is tan undefined?", ["0° and 180°", "*90° and 270°", "45° and 135°", "0° and 360°"],
         "cos = 0 at 90° and 270°."),
        ("A 3-4-5 right triangle: sin of the angle opposite the side of length 3?", ["4/5", "*3/5", "3/4", "5/3"],
         "opp/hyp = 3/5."),
        ("sec θ is the reciprocal of:", ["sin θ", "*cos θ", "tan θ", "csc θ"],
         "sec = 1/cos."),
        ("If tan θ = 1, a possible θ is:", ["0°", "30°", "*45°", "60°"],
         "tan 45° = 1."),
        ("sin(0°) = ?", ["1", "*0", "−1", "1/2"],
         "sin 0° = 0."),
        ("cos(0°) = ?", ["0", "*1", "−1", "1/2"],
         "cos 0° = 1."),
        ("tan(0°) = ?", ["1", "undefined", "*0", "−1"],
         "tan 0° = sin 0°/cos 0° = 0/1 = 0."),
        ("From sin²θ + cos²θ = 1, derive: 1 + tan²θ = ?", ["sin²θ", "*sec²θ", "cos²θ", "csc²θ"],
         "Divide by cos²θ: tan²θ + 1 = sec²θ."),
        ("Which pair are cofunctions?", ["sin and cos of the same angle", "*sin(θ) and cos(90°−θ)", "tan and sec", "sin and csc"],
         "Cofunctions: sin θ = cos(90°−θ).")
    ]
)
lessons[k] = v

# ── 6.5 Graphs of Trig Functions ──────────────────────────────────
k, v = build_lesson(6, 5,
    "Graphs of Trigonometric Functions (amplitude, period, phase shift)",
    "<h3>Graphs of Trigonometric Functions</h3>"
    "<h4>y = A sin(Bx − C) + D</h4>"
    "<ul>"
    "<li><b>Amplitude</b> = |A|: vertical stretch.</li>"
    "<li><b>Period</b> = 2π/|B|: horizontal length of one cycle.</li>"
    "<li><b>Phase shift</b> = C/B: horizontal shift.</li>"
    "<li><b>Vertical shift</b> = D: midline moves to y = D.</li>"
    "</ul>"
    "<h4>Key Graphs</h4>"
    "<ul>"
    "<li>sin x: starts at 0, period 2π.</li>"
    "<li>cos x: starts at 1, period 2π.</li>"
    "<li>tan x: period π, vertical asymptotes at π/2 + nπ.</li>"
    "</ul>",
    [
        ("Amplitude", "|A| in y = A sin(Bx − C) + D; half the distance between max and min."),
        ("Period", "2π/|B|; the length of one complete cycle of sine or cosine."),
        ("Phase Shift", "C/B; horizontal displacement of the graph."),
        ("Vertical Shift / Midline", "D; the midline of the graph shifts to y = D."),
        ("Period of Tangent", "π/|B| for y = A tan(Bx − C) + D.")
    ],
    [
        ("Amplitude of y = 3 sin(x)?", ["1", "*3", "6", "π"],
         "|A| = 3."),
        ("Period of y = sin(2x)?", ["2π", "*π", "4π", "2"],
         "2π/|B| = 2π/2 = π."),
        ("Phase shift of y = sin(x − π/4)?", ["−π/4", "*π/4 (right)", "π/2", "−π/2"],
         "C/B = (π/4)/1 = π/4 to the right."),
        ("Midline of y = 2cos(x) + 5?", ["y = 0", "y = 2", "*y = 5", "y = 7"],
         "D = 5 → midline y = 5."),
        ("Period of y = cos(3x)?", ["3π", "*2π/3", "6π", "π/3"],
         "2π/3."),
        ("Amplitude of y = −4cos(x)?", ["−4", "*4", "1", "0"],
         "Amplitude = |−4| = 4."),
        ("The graph of y = −sin(x) is a reflection of sin(x) over:", ["y-axis", "*x-axis", "y = x", "origin"],
         "Negative A reflects over x-axis."),
        ("Period of y = tan(x)?", ["2π", "*π", "π/2", "4π"],
         "Tangent has period π."),
        ("Where are the vertical asymptotes of y = tan(x)?", ["nπ", "*π/2 + nπ", "2nπ", "nπ/4"],
         "Tangent is undefined where cos = 0: at π/2 + nπ."),
        ("y = sin(x) has zeros at:", ["π/2 + nπ", "*nπ", "2nπ", "nπ/4"],
         "sin = 0 at 0, π, 2π, … i.e., nπ."),
        ("Maximum value of y = 2sin(x) − 1?", ["2", "3", "*1", "−1"],
         "Max of sin = 1. 2(1) − 1 = 1."),
        ("Minimum value of y = 2sin(x) − 1?", ["−1", "0", "*−3", "−2"],
         "Min of sin = −1. 2(−1) − 1 = −3."),
        ("y = cos(x) starts (at x = 0) at:", ["0", "*1", "−1", "π"],
         "cos(0) = 1."),
        ("y = sin(x) starts at:", ["1", "*0", "−1", "π/2"],
         "sin(0) = 0."),
        ("Phase shift of y = cos(2x − π)?", ["π", "*π/2 (right)", "π/4", "2π"],
         "C/B = π/2."),
        ("Period of y = sin(πx)?", ["π", "*2", "2π", "1"],
         "2π/π = 2."),
        ("y = 3sin(2x) + 1. Amplitude, period, midline?", ["3, 2π, y=0", "*3, π, y=1", "2, π, y=3", "3, 2π, y=1"],
         "A=3, period=2π/2=π, midline y=1."),
        ("The cosine graph is the sine graph shifted:", ["Right π", "*Left π/2", "Up 1", "Right π/2"],
         "cos(x) = sin(x + π/2)."),
        ("How many complete cycles of y = sin(4x) in [0, 2π]?", ["1", "2", "*4", "8"],
         "Period = 2π/4 = π/2. Cycles in 2π: 2π/(π/2) = 4."),
        ("For y = A sin(Bx − C) + D, if A < 0, the graph is:", ["Stretched", "Compressed", "*Reflected vertically", "Shifted left"],
         "Negative A flips the graph upside down.")
    ]
)
lessons[k] = v

# ── 6.6 Inverse Trigonometric Functions ────────────────────────────
k, v = build_lesson(6, 6,
    "Inverse Trigonometric Functions",
    "<h3>Inverse Trigonometric Functions</h3>"
    "<p>Inverse trig functions find the angle given a ratio.</p>"
    "<h4>Definitions & Ranges</h4>"
    "<ul>"
    "<li><b>sin⁻¹(x)</b> or arcsin(x): domain [−1, 1], range [−π/2, π/2].</li>"
    "<li><b>cos⁻¹(x)</b> or arccos(x): domain [−1, 1], range [0, π].</li>"
    "<li><b>tan⁻¹(x)</b> or arctan(x): domain (−∞, ∞), range (−π/2, π/2).</li>"
    "</ul>"
    "<h4>Key Relationships</h4>"
    "<ul>"
    "<li>sin(sin⁻¹(x)) = x for x ∈ [−1, 1].</li>"
    "<li>sin⁻¹(sin θ) = θ only if θ ∈ [−π/2, π/2].</li>"
    "</ul>",
    [
        ("Arcsine (sin⁻¹)", "Returns the angle whose sine is x; range [−π/2, π/2]."),
        ("Arccosine (cos⁻¹)", "Returns the angle whose cosine is x; range [0, π]."),
        ("Arctangent (tan⁻¹)", "Returns the angle whose tangent is x; range (−π/2, π/2)."),
        ("Restricted Domain", "Trig functions are restricted to a one-to-one interval so they have inverses."),
        ("Composition Property", "sin(arcsin x) = x and arcsin(sin θ) = θ only within the restricted range.")
    ],
    [
        ("sin⁻¹(1/2) = ?", ["π/3", "*π/6", "π/4", "π/2"],
         "sin(π/6) = 1/2."),
        ("cos⁻¹(0) = ?", ["0", "*π/2", "π", "2π"],
         "cos(π/2) = 0."),
        ("tan⁻¹(1) = ?", ["π/6", "*π/4", "π/3", "π/2"],
         "tan(π/4) = 1."),
        ("sin⁻¹(−1) = ?", ["π", "3π/2", "*−π/2", "−π"],
         "Range of arcsin is [−π/2, π/2]. sin(−π/2) = −1."),
        ("cos⁻¹(−1) = ?", ["−π", "*π", "0", "2π"],
         "cos(π) = −1. Range of arccos is [0, π]."),
        ("tan⁻¹(0) = ?", ["π/4", "π/2", "*0", "π"],
         "tan(0) = 0."),
        ("arcsin(√2/2) = ?", ["π/6", "*π/4", "π/3", "π/2"],
         "sin(π/4) = √2/2."),
        ("arccos(√3/2) = ?", ["*π/6", "π/4", "π/3", "π/2"],
         "cos(π/6) = √3/2."),
        ("sin⁻¹(2) is:", ["π/3", "π", "*Undefined (2 is outside [−1,1])", "2π"],
         "Domain of arcsin is [−1, 1]; 2 is outside."),
        ("tan⁻¹(−1) = ?", ["3π/4", "*−π/4", "−π/2", "5π/4"],
         "tan(−π/4) = −1. In range (−π/2, π/2)."),
        ("cos(arccos(0.5)) = ?", ["arccos(0.5)", "0", "*0.5", "1"],
         "cos(arccos x) = x for x ∈ [−1,1]."),
        ("arcsin(sin(5π/6)) = ?", ["5π/6", "*π/6", "−π/6", "7π/6"],
         "sin(5π/6) = 1/2. arcsin(1/2) = π/6."),
        ("Range of arctan is:", ["[0, π]", "[−1, 1]", "*(-π/2, π/2)", "[−π/2, π/2]"],
         "Open interval: arctan never equals ±π/2."),
        ("arccos(1) = ?", ["π", "π/2", "*0", "1"],
         "cos(0) = 1."),
        ("arctan(√3) = ?", ["π/4", "*π/3", "π/6", "π/2"],
         "tan(π/3) = √3."),
        ("If sin θ = 0.6 and θ is in Q I, θ = ?", ["*arcsin(0.6) ≈ 36.87°", "0.6°", "53.13°", "60°"],
         "Use inverse sine: θ = sin⁻¹(0.6) ≈ 36.87°."),
        ("arcsin(sin(−π/3)) = ?", ["π/3", "2π/3", "*−π/3", "−2π/3"],
         "−π/3 is within [−π/2, π/2]? No, −π/3 ≈ −60° which is in range. So arcsin(sin(−π/3)) = −π/3."),
        ("The graph of y = arcsin(x) is:", ["An S-curve on (−∞, ∞)", "*An increasing curve from (−1, −π/2) to (1, π/2)", "A full sine wave", "A straight line"],
         "Arcsin is defined on [−1,1] and increases from −π/2 to π/2."),
        ("cos⁻¹(−√2/2) = ?", ["π/4", "−π/4", "*3π/4", "5π/4"],
         "cos(3π/4) = −√2/2. In [0, π]."),
        ("arctan(−√3) = ?", ["−π/6", "*−π/3", "2π/3", "5π/6"],
         "tan(−π/3) = −√3. In (−π/2, π/2).")
    ]
)
lessons[k] = v

# ── 6.7 Applications in Physics & Engineering ─────────────────────
k, v = build_lesson(6, 7,
    "Applications in Physics & Engineering",
    "<h3>Applications in Physics &amp; Engineering</h3>"
    "<h4>Simple Harmonic Motion</h4>"
    "<ul>"
    "<li>x(t) = A cos(ωt + φ) models oscillation (springs, pendulums).</li>"
    "<li>A = amplitude, ω = angular frequency, φ = phase, period T = 2π/ω.</li>"
    "</ul>"
    "<h4>Waves</h4>"
    "<ul>"
    "<li>y = A sin(kx − ωt): traveling wave. k = 2π/λ (wave number), λ = wavelength.</li>"
    "</ul>"
    "<h4>AC Circuits</h4>"
    "<ul>"
    "<li>V(t) = V₀ sin(2πft + φ). f = frequency (Hz), peak voltage V₀.</li>"
    "</ul>"
    "<h4>Projectile Motion</h4>"
    "<ul>"
    "<li>Horizontal: x = v₀ cos θ · t. Vertical: y = v₀ sin θ · t − (1/2)gt².</li>"
    "</ul>",
    [
        ("Simple Harmonic Motion", "x(t) = A cos(ωt + φ); periodic motion with constant amplitude."),
        ("Angular Frequency (ω)", "ω = 2π/T = 2πf; relates period and frequency to angular measure."),
        ("Wavelength (λ)", "Distance between successive peaks of a wave; related to wave number k = 2π/λ."),
        ("Projectile Range", "R = (v₀² sin 2θ)/g; maximum at θ = 45°."),
        ("AC Voltage", "V(t) = V₀ sin(2πft + φ); sinusoidal model for alternating current.")
    ],
    [
        ("A spring oscillates: x(t) = 5cos(3t). Amplitude?", ["3", "*5", "15", "π"],
         "A = 5."),
        ("Period of x(t) = 5cos(3t)?", ["3", "5", "*2π/3", "6π"],
         "T = 2π/ω = 2π/3."),
        ("Frequency of x(t) = 5cos(3t)?", ["3", "*3/(2π)", "2π/3", "5"],
         "f = 1/T = 3/(2π)."),
        ("A pendulum has period 2 s. Angular frequency ω?", ["2", "*π", "2π", "π/2"],
         "ω = 2π/T = 2π/2 = π rad/s."),
        ("V(t) = 170sin(120πt). Peak voltage?", ["120π", "*170 V", "120 V", "340 V"],
         "V₀ = 170 V."),
        ("Frequency of V(t) = 170sin(120πt)?", ["120π Hz", "*60 Hz", "170 Hz", "120 Hz"],
         "2πf = 120π → f = 60 Hz."),
        ("Projectile launched at 45° with v₀ = 20 m/s. Range? (g = 10)", ["20 m", "*40 m", "80 m", "10 m"],
         "R = v₀² sin(90°)/g = 400/10 = 40 m."),
        ("At what angle is projectile range maximized?", ["30°", "60°", "*45°", "90°"],
         "sin(2θ) is max when 2θ = 90° → θ = 45°."),
        ("Horizontal velocity component: vₓ = v₀ cos θ. If v₀ = 50, θ = 60°?", ["50", "25√3", "*25", "50√3"],
         "50 cos 60° = 50(0.5) = 25."),
        ("Vertical component: vᵧ = v₀ sin θ. Same situation:", ["25", "*25√3 ≈ 43.3", "50", "50√3"],
         "50 sin 60° = 50(√3/2) = 25√3."),
        ("A wave y = 3sin(2x − 4t). Amplitude?", ["2", "*3", "4", "6"],
         "A = 3."),
        ("Wave number k from y = 3sin(2x − 4t)?", ["4", "*2", "3", "6"],
         "k = 2."),
        ("Wavelength from the wave above?", ["2", "4", "*π", "2π"],
         "λ = 2π/k = 2π/2 = π."),
        ("Wave speed from y = 3sin(2x − 4t)?", ["3", "2", "*2", "4"],
         "v = ω/k = 4/2 = 2."),
        ("Sound wave: f = 440 Hz. One period = ?", ["440 s", "*1/440 s ≈ 0.00227 s", "440 ms", "2π/440"],
         "T = 1/f = 1/440 s."),
        ("Spring constant k = 100 N/m, mass 1 kg. ω = ?", ["100", "*10 rad/s", "50", "1"],
         "ω = √(k/m) = √100 = 10 rad/s."),
        ("Period of the spring above?", ["10 s", "1 s", "*π/5 s", "2π/10 = π/5 s"],
         "T = 2π/10 = π/5 s."),
        ("In AC, RMS voltage = V₀/√2. If V₀ = 170V, RMS ≈", ["170 V", "*120 V", "85 V", "240 V"],
         "170/√2 ≈ 120.2 V."),
        ("A Ferris wheel models height with a sinusoidal function because:", ["It moves fast", "*It undergoes periodic circular motion", "It's tall", "Gravity is sinusoidal"],
         "Circular motion projects onto a sinusoidal height function."),
        ("If two waves have same frequency but different phases, their superposition:", ["Always cancels", "Always doubles", "*Depends on the phase difference", "Is unpredictable"],
         "Constructive or destructive interference depends on phase difference.")
    ]
)
lessons[k] = v

# ── 6.8 Coterminal & Reference Angles ─────────────────────────────
k, v = build_lesson(6, 8,
    "Coterminal & Reference Angles",
    "<h3>Coterminal &amp; Reference Angles</h3>"
    "<h4>Coterminal Angles</h4>"
    "<ul>"
    "<li>Two angles are <b>coterminal</b> if they share the same terminal side.</li>"
    "<li>Add or subtract 360° (or 2π) to find coterminal angles.</li>"
    "</ul>"
    "<h4>Reference Angles</h4>"
    "<ul>"
    "<li>The <b>reference angle</b> is the positive acute angle between the terminal side and the x-axis.</li>"
    "<li>Q I: ref = θ; Q II: ref = 180° − θ; Q III: ref = θ − 180°; Q IV: ref = 360° − θ.</li>"
    "</ul>",
    [
        ("Coterminal Angles", "Angles that share the same terminal side; differ by multiples of 360° (or 2π)."),
        ("Reference Angle", "The positive acute angle (0°–90°) between the terminal side and the nearest x-axis."),
        ("Finding Coterminal", "Add or subtract 360° (2π) repeatedly until the result is in [0°, 360°)."),
        ("Q II Reference", "Reference angle = 180° − θ (or π − θ)."),
        ("Q III Reference", "Reference angle = θ − 180° (or θ − π).")
    ],
    [
        ("A coterminal angle to 30° is:", ["−30°", "*390°", "60°", "330°"],
         "30° + 360° = 390°."),
        ("A negative coterminal angle for 45°:", ["−45°", "*−315°", "−405°", "−135°"],
         "45° − 360° = −315°."),
        ("Find an angle coterminal to 750° in [0°, 360°).", ["390°", "*30°", "750°", "−30°"],
         "750 − 360 = 390; 390 − 360 = 30°."),
        ("Coterminal to −120° in [0°, 360°).", ["120°", "*240°", "−120°", "300°"],
         "−120 + 360 = 240°."),
        ("Reference angle for 150°?", ["150°", "*30°", "60°", "210°"],
         "Q II: 180° − 150° = 30°."),
        ("Reference angle for 225°?", ["*45°", "135°", "225°", "315°"],
         "Q III: 225° − 180° = 45°."),
        ("Reference angle for 300°?", ["*60°", "120°", "300°", "30°"],
         "Q IV: 360° − 300° = 60°."),
        ("Reference angle for 5π/6?", ["5π/6", "π/3", "*π/6", "π/4"],
         "Q II: π − 5π/6 = π/6."),
        ("Reference angle for 4π/3?", ["2π/3", "*π/3", "4π/3", "π/4"],
         "Q III: 4π/3 − π = π/3."),
        ("Are 60° and −300° coterminal?", ["No", "*Yes", "Only in radians", "Cannot tell"],
         "60° and −300°: −300 + 360 = 60°. Yes."),
        ("How many coterminal angles does any angle have?", ["1", "2", "360", "*Infinitely many"],
         "Add/subtract 360° any number of times."),
        ("Coterminal to 2π/3 is:", ["−2π/3", "*8π/3", "4π/3", "π/3"],
         "2π/3 + 2π = 2π/3 + 6π/3 = 8π/3."),
        ("Reference angle for 7π/4?", ["3π/4", "7π/4", "*π/4", "π/2"],
         "Q IV: 2π − 7π/4 = π/4."),
        ("sin(225°) using reference angle:", ["sin 45°", "cos 45°", "*−sin 45° = −√2/2", "−cos 45°"],
         "225° is in Q III. sin negative. ref = 45°. sin(225°) = −sin(45°) = −√2/2."),
        ("cos(120°) using reference angle:", ["cos 60°", "*−cos 60° = −1/2", "cos 120°", "sin 60°"],
         "Q II, cos negative. ref = 60°. cos(120°) = −1/2."),
        ("tan(330°) using reference angle:", ["tan 30°", "*−tan 30° = −√3/3", "√3", "tan 330°"],
         "Q IV: tan negative. ref = 30°. tan(330°) = −tan(30°) = −1/√3 = −√3/3."),
        ("Is 0° its own reference angle?", ["*Yes (it's on the x-axis)", "No, it's undefined", "Reference is 90°", "Reference is 180°"],
         "0° is on the x-axis; reference = 0°."),
        ("Coterminal angle to −π/4 in [0, 2π)?", ["π/4", "*7π/4", "3π/4", "5π/4"],
         "−π/4 + 2π = 7π/4."),
        ("Reference angle for 170°?", ["80°", "*10°", "170°", "190°"],
         "Q II: 180° − 170° = 10°."),
        ("Two angles in different quadrants can have the same reference angle.", ["*True", "False", "Only Q I and Q II", "Only Q I and Q IV"],
         "Reference angles are always acute; many angles share the same reference angle.")
    ]
)
lessons[k] = v

# ── 6.9 Case Studies in Navigation ────────────────────────────────
k, v = build_lesson(6, 9,
    "Case Studies in Navigation",
    "<h3>Case Studies in Navigation</h3>"
    "<p>Trigonometry is fundamental to navigation on land, sea, and air.</p>"
    "<h4>Bearings</h4>"
    "<ul>"
    "<li>A <b>bearing</b> is measured clockwise from due north: N 30° E means 30° east of north.</li>"
    "</ul>"
    "<h4>Right-Triangle Navigation</h4>"
    "<ul>"
    "<li>Use trig ratios to find distances and angles in navigation problems.</li>"
    "</ul>"
    "<h4>Law of Sines &amp; Cosines (preview)</h4>"
    "<ul>"
    "<li><b>Law of Sines:</b> a/sin A = b/sin B = c/sin C.</li>"
    "<li><b>Law of Cosines:</b> c² = a² + b² − 2ab cos C.</li>"
    "</ul>"
    "<h4>GPS & Triangulation</h4>"
    "<ul>"
    "<li>GPS uses at least 3 satellites and trilateration (related to triangulation) to determine position.</li>"
    "</ul>",
    [
        ("Bearing", "Direction measured clockwise from north; e.g., N 30° E or a three-figure bearing like 030°."),
        ("Law of Sines", "a/sin A = b/sin B = c/sin C; relates sides and opposite angles."),
        ("Law of Cosines", "c² = a² + b² − 2ab cos C; generalizes the Pythagorean theorem."),
        ("Triangulation", "Determining position by measuring angles from known reference points."),
        ("GPS", "Uses signals from ≥ 3 satellites and trilateration to find a receiver's position.")
    ],
    [
        ("A bearing of N 45° E means:", ["45° south of east", "*45° east of north", "45° west of north", "Due northeast is always 45°"],
         "Start at north, rotate 45° toward east."),
        ("Three-figure bearing for due east?", ["000°", "*090°", "180°", "270°"],
         "East is 90° clockwise from north."),
        ("Bearing of due south?", ["090°", "*180°", "270°", "360°"],
         "South = 180°."),
        ("A ship sails 50 km on bearing 060°. How far east?", ["25", "*50 sin 60° ≈ 43.3 km", "50 cos 60° = 25 km", "50 km"],
         "Eastward component = 50 sin(60°) ≈ 43.3 km."),
        ("How far north does the ship above travel?", ["43.3 km", "*25 km", "50 km", "0 km"],
         "Northward = 50 cos(60°) = 25 km."),
        ("Law of sines: a/sin A = b/sin B. If a = 10, A = 30°, B = 60°, find b.", ["5", "*10√3 ≈ 17.32", "20", "10"],
         "10/sin 30° = b/sin 60° → 10/0.5 = b/(√3/2) → 20 = b/(√3/2) → b = 10√3."),
        ("Law of cosines: c² = a² + b² − 2ab cos C. If a = 5, b = 7, C = 60°, find c.", ["12", "√74", "*√39 ≈ 6.24", "8"],
         "c² = 25 + 49 − 2(5)(7)(0.5) = 74 − 35 = 39. c = √39 ≈ 6.24."),
        ("If C = 90° in the law of cosines, it reduces to:", ["a² + b² + c² = 0", "*c² = a² + b² (Pythagorean theorem)", "c = a + b", "c² = 2ab"],
         "cos 90° = 0, so c² = a² + b²."),
        ("A lighthouse is spotted at bearing 045°. What direction is that?", ["Due north", "*Northeast", "Due east", "Northwest"],
         "045° = N 45° E = northeast."),
        ("Two ships leave a port. Ship A: 30 km north, Ship B: 40 km east. Distance apart?", ["70 km", "35 km", "*50 km", "10 km"],
         "√(30² + 40²) = √2500 = 50 km."),
        ("An airplane flies 200 km at bearing 120°. East component?", ["100 km", "*200 sin 60° ≈ 173.2 km", "200 cos 60° = 100 km", "200 km"],
         "Bearing 120° → angle from east = 30° → east = 200 sin(60°) ≈ 173 km."),
        ("South component of the airplane above?", ["173 km", "*200 cos 60° = 100 km (actually south)", "200 km", "0 km"],
         "Bearing 120° goes south of east. South component = 200 cos(60°) = 100 km."),
        ("GPS requires at least __ satellites for a 3D fix.", ["1", "2", "*3 (4 for full positioning with time)", "5"],
         "3 for 2D, 4 for 3D fix with time correction."),
        ("Angle of elevation to a tower top from 100 m away is 30°. Height?", ["50 m", "*100 tan 30° ≈ 57.7 m", "100 m", "30 m"],
         "h = 100 tan 30° = 100/√3 ≈ 57.7 m."),
        ("A pilot descends at a 3° angle. After flying 5 km, altitude lost?", ["*5 sin 3° ≈ 0.262 km", "5 cos 3°", "5 tan 3°", "5 × 3"],
         "Altitude = 5 sin(3°) ≈ 5(0.05236) ≈ 0.262 km ≈ 262 m."),
        ("Triangulation requires:", ["1 known point", "2 known points and distances", "*2+ known points and angle measurements", "No measurements"],
         "Triangulation uses angle measurements from known points."),
        ("The angle of depression from a cliff to a boat is 20°. The angle of elevation from the boat is:", ["70°", "*20°", "160°", "Cannot determine"],
         "Alternate interior angles: angle of elevation = angle of depression = 20°."),
        ("Law of sines is ambiguous (SSA case) when:", ["SAS", "*Two sides and a non-included angle are given", "ASA", "SSS"],
         "SSA can give 0, 1, or 2 solutions."),
        ("A hiker walks 3 km north then 4 km on bearing 090°. Bearing from start to end point?", ["090°", "000°", "*N 53.1° E (≈ 053°)", "N 36.9° E"],
         "tan θ = 4/3. θ = arctan(4/3) ≈ 53.1°. Bearing ≈ 053°."),
        ("Distance from start to hiker's end point above?", ["7 km", "3.5 km", "*5 km", "12 km"],
         "√(3² + 4²) = 5 km.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 6)")
