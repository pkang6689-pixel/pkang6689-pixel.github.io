#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 7: Oblique Triangles & Applications (7 lessons)."""
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

# ── 7.1 Law of Sines ──
k, v = build_lesson(7, 1, "Law of Sines",
    "<h3>Law of Sines</h3>"
    "<p>For any triangle with sides a, b, c opposite angles A, B, C:</p>"
    "<p><b>a/sin A = b/sin B = c/sin C</b></p>"
    "<h4>When to Use</h4>"
    "<ul><li><b>AAS:</b> Two angles and a non-included side.</li>"
    "<li><b>ASA:</b> Two angles and the included side.</li>"
    "<li><b>SSA:</b> Two sides and a non-included angle (ambiguous case).</li></ul>"
    "<h4>Derivation</h4>"
    "<p>Drop an altitude h from vertex C: h = a sin B = b sin A → a/sin A = b/sin B.</p>",
    [
        ("Law of Sines", "a/sin A = b/sin B = c/sin C for any triangle."),
        ("AAS / ASA", "Cases where the Law of Sines is directly applicable."),
        ("Oblique Triangle", "A triangle with no right angle."),
        ("Solving a Triangle", "Finding all unknown sides and angles."),
        ("Third Angle", "C = 180° − A − B; always find the missing angle first."),
    ],
    [
        ("The Law of Sines states:", ["a² = b² + c² − 2bc cos A", "*a/sin A = b/sin B = c/sin C", "sin A + sin B = sin C", "a sin A = b sin B"],
         "Equal ratios of side to sine of opposite angle."),
        ("Given A = 40°, B = 60°, a = 10. Find b:", ["b = 10", "*b = 10 sin 60° / sin 40° ≈ 13.47", "b = 10 cos 60°", "b = 10 tan 60°"],
         "b/sin B = a/sin A → b = a sin B / sin A."),
        ("The same triangle: angle C =", ["100°", "20°", "*80°", "60°"],
         "C = 180° − 40° − 60° = 80°."),
        ("Find side c:", ["c = 10 sin 40°/sin 80°", "*c = 10 sin 80° / sin 40° ≈ 15.32", "c = 10", "c = 10 cos 80°"],
         "c = a sin C / sin A."),
        ("The Law of Sines works for:", ["Only right triangles", "Only acute triangles", "Only obtuse triangles", "*All triangles"],
         "It applies universally to any triangle."),
        ("In an ASA case (A = 50°, c = 12, B = 70°), the first step is:", ["*Find C = 180° − 50° − 70° = 60°", "Find side a directly", "Use Law of Cosines", "Guess C"],
         "Find the third angle first."),
        ("After finding C = 60°, find a using:", ["a = 12 cos 50°", "*a/sin 50° = 12/sin 60° → a = 12 sin 50° / sin 60°", "a = c − 12", "a = b + c"],
         "Apply the Law of Sines ratio."),
        ("If two angles are known, how many solutions exist?", ["0", "*Exactly 1", "2", "Infinite"],
         "AAS/ASA always gives a unique triangle."),
        ("The derivation uses:", ["The Pythagorean theorem directly", "*An altitude dropped to create right triangles", "Coordinate geometry", "Calculus"],
         "Altitude h = a sin B = b sin A leads to the law."),
        ("In navigation, the Law of Sines helps find:", ["Speed only", "*Distances when two bearings and a baseline are known", "Only angles", "Temperature"],
         "Common in surveying and navigation."),
        ("Given B = 30°, C = 105°, b = 8. Find A:", ["30°", "105°", "*45°", "75°"],
         "A = 180° − 30° − 105° = 45°."),
        ("Same triangle: find c:", ["*c = 8 sin 105° / sin 30° ≈ 15.45", "c = 8", "c = 8 cos 105°", "c = 16"],
         "c = b sin C / sin B."),
        ("If A = 90°, the Law of Sines becomes:", ["Invalid", "*a/sin 90° = a/1 = a, reducing to basic right-triangle ratios", "a = b = c", "Undefined"],
         "sin 90° = 1, so a/1 = b/sin B = c/sin C."),
        ("Which is NOT a case for applying the Law of Sines directly?", ["AAS", "ASA", "SSA", "*SAS (use Law of Cosines instead)"],
         "SAS requires the Law of Cosines."),
        ("Law of Sines can also find angles via:", ["*sin A = a sin B / b", "cos A = a/b", "tan A = a/b", "A = arctan(a/b)"],
         "Rearrange: sin A = a sin B / b, then A = arcsin(…)."),
        ("Given a = 7, b = 10, B = 80°. Find A:", ["80°", "*sin A = 7 sin 80° / 10 ≈ 0.689 → A ≈ 43.5°", "A = 100°", "A = 7°"],
         "sin A = a sin B / b."),
        ("The Law of Sines can be written equivalently as:", ["sin A / a = a / sin A", "*sin A / a = sin B / b = sin C / c", "sin A · a = sin B · b", "a + b = c"],
         "Reciprocal form: sin/side = sin/side."),
        ("For a triangle with A = 30°, a = 5, B = 45°:", ["b = 5", "*b = 5 sin 45° / sin 30° = 5(√2/2)/(1/2) = 5√2 ≈ 7.07", "b = 2.5", "b = 5√2/2"],
         "b = a sin B / sin A."),
        ("A triangle has only one solution when given:", ["SSA", "SSS", "*AAS or ASA", "AAA"],
         "AAS/ASA guarantee a unique triangle."),
        ("The Law of Sines is insufficient when given:", ["Two angles", "Two angles and a side", "*Three sides (SSS) — need Law of Cosines", "One angle and the opposite side"],
         "SSS requires the Law of Cosines."),
    ]
)
lessons[k] = v

# ── 7.2 The Ambiguous Case (SSA) ──
k, v = build_lesson(7, 2, "The Ambiguous Case (SSA)",
    "<h3>The Ambiguous Case (SSA)</h3>"
    "<p>When two sides and a non-included angle are given (SSA), there may be <b>0, 1, or 2</b> triangles.</p>"
    "<h4>Analysis (Given a, b, A)</h4>"
    "<ul><li>Compute sin B = b sin A / a.</li>"
    "<li>If sin B > 1 → <b>no triangle.</b></li>"
    "<li>If sin B = 1 → <b>one triangle</b> (right angle at B).</li>"
    "<li>If sin B < 1 → B = arcsin(…) gives one acute angle; B' = 180° − B is the other. Check if A + B' < 180° → if yes, <b>two triangles</b>; if not, <b>one triangle.</b></li></ul>",
    [
        ("Ambiguous Case", "SSA configuration; may yield 0, 1, or 2 valid triangles."),
        ("No Triangle", "sin B > 1 → the given side is too short to form a triangle."),
        ("One Triangle", "sin B = 1 (right triangle) or the supplement B' makes A + B' ≥ 180°."),
        ("Two Triangles", "Both B and B' = 180° − B produce valid triangles (A + B' < 180°)."),
        ("Height Test", "h = b sin A. If a < h → 0 triangles; a = h → 1; h < a < b → 2; a ≥ b → 1."),
    ],
    [
        ("The SSA case is called 'ambiguous' because:", ["It always has 2 solutions", "*It can yield 0, 1, or 2 triangles", "It never has a solution", "It's identical to SAS"],
         "The number of solutions depends on the measurements."),
        ("Given a = 3, b = 8, A = 30°. sin B = 8 sin 30° / 3 = 8(0.5)/3 ≈ 1.33. Conclusion:", ["One triangle", "Two triangles", "*No triangle (sin B > 1)", "Right triangle"],
         "sin B > 1 is impossible → no solution."),
        ("Given a = 10, b = 8, A = 40°. sin B = 8 sin 40° / 10 ≈ 0.514. How many triangles?", ["0", "1", "*Check: B ≈ 31°, B' = 149°. A + B' = 189° > 180° → only 1 triangle", "Not enough info"],
         "B' = 149° makes A + B' too large → one triangle only."),
        ("Given a = 6, b = 8, A = 30°. sin B = 8(0.5)/6 ≈ 0.667. B ≈ 41.8°, B' ≈ 138.2°:", ["0 triangles", "1 triangle", "*2 triangles (A + B' = 168.2° < 180°)", "3 triangles"],
         "Both B and B' yield valid triangles."),
        ("The height test: h = b sin A. If a < h:", ["2 triangles", "1 triangle", "*0 triangles (side too short)", "Infinite"],
         "The side doesn't reach the opposite side."),
        ("If a = h exactly:", ["0 triangles", "*1 right triangle", "2 triangles", "Depends"],
         "The side just barely reaches → a right angle at B."),
        ("If h < a < b:", ["0", "1", "*2 triangles", "Cannot determine"],
         "The 'swing' can land on either side of the foot of the altitude."),
        ("If a ≥ b (and A is acute):", ["0", "*1 triangle", "2", "Impossible"],
         "The longer side opposite the given angle guarantees a unique triangle."),
        ("In the two-triangle case, the two solutions have:", ["Same angles", "*Different angle B (acute vs. obtuse) and therefore different shapes", "Same side c", "Identical triangles"],
         "B₁ is acute, B₂ is obtuse; the triangles differ."),
        ("Given a = 12, b = 10, A = 50°. Since a > b:", ["*Exactly 1 triangle", "2 triangles", "0 triangles", "Need more info"],
         "When the side opposite the given angle is longer, there's exactly one solution."),
        ("If A is obtuse and a ≤ b:", ["1 triangle", "2 triangles", "*0 triangles", "Right triangle"],
         "When A > 90° and a ≤ b, no triangle is possible."),
        ("If A is obtuse and a > b:", ["0", "*1 triangle", "2", "Depends"],
         "One valid triangle when A is obtuse and a > b."),
        ("How to find side c after determining B:", ["c = a + b", "*C = 180° − A − B, then c = a sin C / sin A", "c = b − a", "c = √(a² + b²)"],
         "Find C, then use Law of Sines."),
        ("In the two-triangle case, you must solve for c:", ["Once", "*Twice (once for each valid B)", "Not needed", "Three times"],
         "Each B gives a different C and therefore a different c."),
        ("The ambiguous case only arises with:", ["SAS", "AAS", "*SSA", "SSS"],
         "SSA is the only configuration with ambiguity."),
        ("A surveyor uses SSA when:", ["They know all three sides", "*They know two distances and a bearing angle", "They know two angles", "They use a protractor only"],
         "Common in field measurements."),
        ("To avoid errors in the ambiguous case:", ["Skip the check", "*Always test if 180° − B produces a valid second triangle", "Assume 1 solution", "Use Law of Cosines"],
         "Must check the supplement."),
        ("If sin B = 1 exactly:", ["No solution", "*B = 90°; one right triangle", "Two solutions", "B = 0°"],
         "sin B = 1 means B is a right angle."),
        ("Given a = 5, b = 3, A = 60°. sin B = 3 sin 60°/5 ≈ 0.52. Number of triangles:", ["0", "*1 (since a > b)", "2", "3"],
         "a > b guarantees one triangle."),
        ("The ambiguous case is tested on the AP exam as:", ["Never", "Rarely", "*A common free-response and multiple-choice topic", "Only in Calc AB"],
         "SSA/ambiguous case appears regularly."),
    ]
)
lessons[k] = v

# ── 7.3 Law of Cosines ──
k, v = build_lesson(7, 3, "Law of Cosines",
    "<h3>Law of Cosines</h3>"
    "<p><b>c² = a² + b² − 2ab cos C</b></p>"
    "<p>Generalizes the Pythagorean theorem (when C = 90°, cos C = 0).</p>"
    "<h4>When to Use</h4>"
    "<ul><li><b>SAS:</b> Two sides and the included angle → find the third side.</li>"
    "<li><b>SSS:</b> Three sides → find each angle.</li></ul>"
    "<h4>Finding Angles from SSS</h4>"
    "<p>cos C = (a² + b² − c²) / (2ab). Then C = arccos(…).</p>",
    [
        ("Law of Cosines", "c² = a² + b² − 2ab cos C; generalizes the Pythagorean theorem."),
        ("SAS Case", "Two sides and the included angle → use Law of Cosines to find the third side."),
        ("SSS Case", "Three sides → rearrange to find each angle: cos C = (a²+b²−c²)/(2ab)."),
        ("Generalization", "When C = 90°, cos C = 0 and the Law of Cosines reduces to c² = a² + b²."),
        ("Solving SSS", "Find the largest angle first (opposite the longest side) to determine if the triangle is obtuse."),
    ],
    [
        ("The Law of Cosines: c² =", ["a² + b²", "*a² + b² − 2ab cos C", "a² − b² + 2ab cos C", "a + b − 2ab"],
         "c² = a² + b² − 2ab cos C."),
        ("Given a = 5, b = 7, C = 60°. Find c:", ["12", "*c² = 25 + 49 − 2(5)(7)cos60° = 74 − 35 = 39 → c ≈ 6.24", "c = 2", "c = √74"],
         "cos 60° = 0.5 → c² = 39."),
        ("If C = 90°, the Law of Cosines becomes:", ["c² = a² + b² − 2ab", "*c² = a² + b² (Pythagorean theorem)", "c² = 2ab", "c² = a² − b²"],
         "cos 90° = 0 eliminates the last term."),
        ("Given a = 8, b = 6, c = 10. Find angle C:", ["60°", "*cos C = (64+36−100)/(2·8·6) = 0/96 = 0 → C = 90°", "45°", "30°"],
         "cos C = 0 → C = 90°. It's a right triangle!"),
        ("Given a = 3, b = 5, c = 7. Find C:", ["*cos C = (9+25−49)/(2·3·5) = −15/30 = −0.5 → C = 120°", "C = 60°", "C = 90°", "C = 150°"],
         "Negative cosine means obtuse angle."),
        ("After finding one angle with Law of Cosines, find the others using:", ["Law of Cosines again (works but slower)", "*Law of Sines (faster) or subtract from 180°", "Guessing", "Only Law of Cosines"],
         "Law of Sines is typically faster for remaining angles."),
        ("SAS is guaranteed to have:", ["0 solutions", "*Exactly 1 solution", "2 solutions", "It depends"],
         "SAS always determines a unique triangle."),
        ("SSS is guaranteed to have:", ["0 solutions always", "*Exactly 1 solution (if triangle inequality holds)", "2 solutions", "Infinite solutions"],
         "Three positive sides satisfying triangle inequality give one unique triangle."),
        ("The triangle inequality states:", ["a + b = c", "*a + b > c (sum of any two sides > third)", "a + b < c", "a² + b² > c²"],
         "If violated, no triangle can be formed."),
        ("Given a = 2, b = 3, c = 10. Can a triangle be formed?", ["Yes", "*No (2 + 3 = 5 < 10)", "Maybe", "Only if right"],
         "Fails triangle inequality."),
        ("In the SAS case, which formula do you use?", ["*c² = a² + b² − 2ab cos C (with the included angle)", "Law of Sines", "cos C = (a²+b²−c²)/(2ab)", "Heron's formula"],
         "Use the version with the known included angle."),
        ("In the SSS case, which formula do you use?", ["c² = a² + b² − 2ab cos C", "*cos C = (a²+b²−c²)/(2ab) (rearranged to find angle)", "a/sin A = b/sin B", "Heron's formula only"],
         "Rearrange to solve for the unknown angle."),
        ("Given a = 10, b = 12, C = 45°. Find c:", ["22", "*c² = 100+144−2(10)(12)cos45° = 244−120√2 ≈ 74.5 → c ≈ 8.63", "c = √244", "c = 2"],
         "Compute: 2(10)(12)(√2/2) = 120√2 ≈ 169.7. c² ≈ 244 − 169.7."),
        ("When solving SSS, it's wise to find the largest angle first because:", ["*If it's obtuse, the other two must be acute (avoids ambiguity with arcsin)", "It's easiest", "Convention", "Doesn't matter"],
         "arccos gives a unique angle in [0°, 180°], avoiding ambiguity."),
        ("The Law of Cosines is related to:", ["Only algebra", "*Vector dot product: c²=|a−b|² and coordinate geometry", "Logarithms", "Only right triangles"],
         "In vectors: |a⃗ − b⃗|² = |a⃗|² + |b⃗|² − 2a⃗·b⃗."),
        ("Given a = 6, b = 6, C = 120°. Find c:", ["6", "12", "*c² = 36+36−2(36)cos120° = 72+36 = 108 → c = 6√3", "c = 36"],
         "cos 120° = −1/2. c² = 72 − 2(36)(−0.5) = 72 + 36 = 108."),
        ("Can the Law of Cosines handle right triangles?", ["No", "*Yes — it reduces to the Pythagorean theorem", "Only with special angles", "Only with isosceles"],
         "It's a generalization that works for all triangles."),
        ("A construction worker knows two wall lengths and the angle between them. Which law?", ["Law of Sines", "*Law of Cosines (SAS)", "Neither", "Pythagorean only"],
         "SAS → Law of Cosines."),
        ("Given a = 4, b = 5, C = 0°. c =", ["9", "√41", "*c = |a − b| = 1 (degenerate)", "c = 0"],
         "cos 0° = 1 → c² = 16 + 25 − 40 = 1 → c = 1. Degenerate (collinear)."),
        ("Given a = 4, b = 5, C = 180°. c =", ["1", "*c = a + b = 9 (degenerate)", "c = √41", "c = 0"],
         "cos 180° = −1 → c² = 16 + 25 + 40 = 81 → c = 9."),
    ]
)
lessons[k] = v

# ── 7.4 Area of Triangles (Heron's & Sine) ──
k, v = build_lesson(7, 4, "Area of Triangles",
    "<h3>Area of Triangles</h3>"
    "<h4>Sine Area Formula</h4>"
    "<p><b>Area = ½ ab sin C</b> — uses two sides and the included angle.</p>"
    "<h4>Heron's Formula</h4>"
    "<p>Given all three sides a, b, c: compute <b>s = (a+b+c)/2</b>, then</p>"
    "<p><b>Area = √(s(s−a)(s−b)(s−c))</b></p>",
    [
        ("Sine Area Formula", "Area = ½ ab sin C; efficient with SAS data."),
        ("Heron's Formula", "Area = √(s(s−a)(s−b)(s−c)) where s = (a+b+c)/2."),
        ("Semi-perimeter (s)", "s = (a + b + c) / 2; used in Heron's formula."),
        ("When to Use Sine Formula", "When two sides and their included angle are known (SAS)."),
        ("When to Use Heron's", "When all three sides are known (SSS)."),
    ],
    [
        ("Area = ½ ab sin C. Given a=8, b=10, C=30°:", ["40", "*½(8)(10)sin30° = ½(80)(0.5) = 20", "80", "10"],
         "½(8)(10)(0.5) = 20 square units."),
        ("The sine area formula requires:", ["Three sides", "*Two sides and the included angle", "One side and two angles", "Three angles"],
         "SAS data."),
        ("If C = 90°, then Area = ½ ab sin 90° =", ["0", "*½ ab (standard right triangle formula)", "ab", "½ a² b²"],
         "sin 90° = 1."),
        ("If C = 0° or 180°, the area equals:", ["1", "ab", "*0 (degenerate triangle)", "½ ab"],
         "sin 0 = sin 180° = 0."),
        ("Maximum area for fixed a and b occurs when C =", ["0°", "60°", "*90°", "180°"],
         "sin C is maximized at C = 90° → Area = ½ ab."),
        ("Heron's formula: a=3, b=4, c=5. s =", ["12", "*6", "5", "7"],
         "s = (3+4+5)/2 = 6."),
        ("Same triangle: Area = √(6·3·2·1) =", ["12", "*6", "√36 = 6", "36"],
         "√(6)(3)(2)(1) = √36 = 6."),
        ("Check with right-triangle formula: ½(3)(4) =", ["12", "*6 ✓", "7", "24"],
         "Both formulas give 6. Consistent!"),
        ("For an equilateral triangle with side s, the area is:", ["s²", "*s²√3/4", "s²/2", "s√3"],
         "Apply Heron's or the sine formula with C = 60°."),
        ("Equilateral triangle s = 6: Area =", ["36", "*36√3/4 = 9√3 ≈ 15.59", "18", "6√3"],
         "(6²)(√3)/4 = 9√3."),
        ("Heron's formula is useful when:", ["You know two angles", "*You know all three sides but no angles", "You know one side", "Always"],
         "SSS data → Heron's."),
        ("Given a=7, b=8, c=9. s = 12. Area:", ["√(12·5·4·3) = √720 ≈ 26.83", "*√(12·5·4·3) = √720 = 12√5 ≈ 26.83", "12", "720"],
         "s−a=5, s−b=4, s−c=3. Area = √720 ≈ 26.83."),
        ("The sine rule Area = ½ ab sin C can also be written as:", ["½ bc sin A or ½ ac sin B", "Only ½ ab sin C", "*All three: ½ ab sin C = ½ bc sin A = ½ ac sin B", "None"],
         "You can use any pair of sides with their included angle."),
        ("A field has vertices forming a triangle with sides 100m, 150m, 200m. Semi-perimeter:", ["225", "*225 m", "450 m", "150 m"],
         "s = (100+150+200)/2 = 225."),
        ("Same field: Area = √(225 · 125 · 75 · 25):", ["225", "*√(225·125·75·25) = √52734375 ≈ 7261.8 m²", "52734375", "100"],
         "Compute step by step or use a calculator."),
        ("A parallelogram has sides a, b and included angle θ. Its area is:", ["ab", "½ ab sin θ", "*ab sin θ", "2ab sin θ"],
         "A parallelogram is two triangles: 2 × ½ ab sin θ = ab sin θ."),
        ("In navigation, the area formula helps calculate:", ["Speed", "*The area enclosed by a triangular route", "Only distance", "Time"],
         "Useful for land area and maritime zone computations."),
        ("If a = 5, b = 5, C = 120°. Area:", ["12.5", "*½(5)(5)sin120° = ½(25)(√3/2) = 25√3/4 ≈ 10.83", "25", "25√3"],
         "sin 120° = √3/2."),
        ("Heron's formula fails if the three sides don't satisfy:", ["a + b = c", "*Triangle inequality (s−a, s−b, s−c must all be positive)", "a² + b² = c²", "All sides equal"],
         "If any s−x ≤ 0, no triangle exists."),
        ("Both area formulas produce:", ["Different results", "*The same area (just different input requirements)", "Only approximations", "Exact only for right triangles"],
         "Same triangle → same area regardless of formula used."),
    ]
)
lessons[k] = v

# ── 7.5 Navigation Applications ──
k, v = build_lesson(7, 5, "Navigation & Bearing Applications",
    "<h3>Navigation &amp; Bearing Applications</h3>"
    "<p>Bearings give direction as an angle from north (clockwise). Trig laws solve real navigation problems.</p>"
    "<h4>Typical Problems</h4>"
    "<ul><li>Two observers measure bearings to a target → find the distance using Law of Sines.</li>"
    "<li>A ship travels on two bearings and known distances → find displacement using Law of Cosines.</li>"
    "<li>Pilots correct for wind drift using vector addition and trig.</li></ul>",
    [
        ("Bearing", "Direction measured clockwise from north, e.g., N30°E or simply 030°."),
        ("Baseline", "A known distance between two observation points."),
        ("Triangulation", "Using angles from two known points to determine the position of a third."),
        ("Course vs. Heading", "Course = intended path; heading = direction the craft points (may differ due to wind/current)."),
        ("Displacement", "Straight-line distance and direction from start to end."),
    ],
    [
        ("A bearing of N40°E means:", ["40° south of east", "*40° east of north (= 040° compass)", "40° west of north", "Due north"],
         "Start from north, rotate 40° clockwise toward east."),
        ("A bearing of S30°W converts to:", ["30°", "150°", "*210° (180° + 30°)", "330°"],
         "South(180°) + 30° west = 210° compass."),
        ("Two lighthouses 10 km apart. From A, the ship is at bearing 060°. From B, it's at bearing 330°. To find the ship's distance:", ["*Use the Law of Sines with the triangle formed by A, B, and the ship", "Multiply bearings", "Use Pythagorean theorem", "Cannot determine"],
         "The bearings and baseline form a triangle; use Law of Sines."),
        ("A ship sails 20 km on bearing 040°, then 15 km on bearing 120°. The angle between the legs:", ["40°", "*80° (120° − 40°)", "160°", "120°"],
         "Difference in bearings = 120° − 40° = 80°."),
        ("To find the straight-line displacement after two legs:", ["Add 20 + 15 = 35 km", "*Use Law of Cosines with the two legs and included angle", "Subtract 20 − 15", "Use Law of Sines"],
         "SAS → Law of Cosines."),
        ("Displacement² = 20² + 15² − 2(20)(15)cos80° ≈:", ["625", "*400 + 225 − 600(0.174) ≈ 520.6 → displacement ≈ 22.8 km", "35", "5"],
         "cos 80° ≈ 0.174. d² ≈ 520.6."),
        ("A pilot needs to fly due east but wind blows from the north. The heading must be:", ["Due east", "*Slightly north of east (to counter the southward drift)", "Due north", "Slightly south"],
         "Point into the wind component."),
        ("In pilot wind correction, the calculation uses:", ["Only addition", "*Vector addition and trig (Law of Sines/Cosines)", "Only subtraction", "No math"],
         "Wind vector + airspeed vector = ground velocity."),
        ("A search-and-rescue team takes bearings from two stations to a lost hiker. This is called:", ["Parallax", "*Triangulation", "GPS", "Dead reckoning"],
         "Two bearings from known points → triangulation."),
        ("Dead reckoning uses:", ["*Speed, time, and bearing to estimate position", "Satellites", "Only a compass", "Stars"],
         "Before GPS, sailors used DR."),
        ("If a boat travels due north 8 km, then due east 6 km, displacement =", ["14 km", "2 km", "*10 km (right triangle: √(64+36)=10)", "8 km"],
         "Pythagorean theorem: 8-6-10 right triangle."),
        ("The bearing from start to end in the above problem:", ["N0°E", "N90°E", "*N36.87°E (arctan(6/8) ≈ 36.87° east of north)", "S53.13°W"],
         "tan θ = 6/8 → θ ≈ 36.87°."),
        ("In coastal surveying, the Law of Sines finds:", ["Only angles", "*Distances to inaccessible points (like offshore rocks)", "Only bearings", "Temperature"],
         "Measure angles from two points on shore to compute distance."),
        ("If two legs make an angle of 180° (straight line), the displacement equals:", ["0", "*|leg₁ + leg₂| or |leg₁ − leg₂| depending on direction", "leg₁ × leg₂", "Undefined"],
         "Same/opposite direction: add or subtract."),
        ("A plane flies 300 km at bearing 060°, then 400 km at bearing 150°. The included angle:", ["60°", "*90° (150° − 60°)", "150°", "210°"],
         "Included angle = 150° − 60° = 90°."),
        ("Displacement = √(300² + 400²) =", ["700 km", "100 km", "*500 km", "350 km"],
         "Right triangle: √(90000 + 160000) = √250000 = 500 km."),
        ("Navigation problems almost always require:", ["Only memorization", "*Drawing a diagram first", "Only a calculator", "No diagram"],
         "A diagram clarifies the triangle and angles."),
        ("Modern GPS uses trilateration, but the math is based on:", ["No math", "*Distance measurements and trig/geometry", "Only computers", "Guessing"],
         "GPS fundamentally uses geometric principles."),
        ("A common AP exam navigation question involves:", ["Only bearings", "*Two observers, a baseline, and finding a distance using Law of Sines", "No trig", "Only right triangles"],
         "Classic triangulation setup."),
        ("In all navigation problems, converting bearings to triangle angles requires:", ["Ignoring direction", "*Careful analysis of the geometry (draw it!)", "Always subtracting from 90°", "Adding 180°"],
         "Triangle interior angles ≠ bearings directly; diagram-based analysis is essential."),
    ]
)
lessons[k] = v

# ── 7.6 Engineering & Surveying Cases ──
k, v = build_lesson(7, 6, "Engineering & Surveying Cases",
    "<h3>Engineering &amp; Surveying Cases</h3>"
    "<h4>Structural Engineering</h4>"
    "<p>Forces in trusses are resolved using oblique triangles and the Laws of Sines/Cosines.</p>"
    "<h4>Land Surveying</h4>"
    "<p>Measuring irregular plots requires breaking them into triangles and computing areas.</p>"
    "<h4>Architecture</h4>"
    "<p>Roof pitches, arch spans, and beam angles involve trig law calculations.</p>",
    [
        ("Truss Analysis", "Forces along members are found by resolving force triangles using Laws of Sines/Cosines."),
        ("Surveying Traverse", "A closed loop of measured angles and distances; areas computed by breaking into triangles."),
        ("Roof Pitch", "Rise over run; the angle is found using tan⁻¹(rise/run)."),
        ("Vector Resolution", "Breaking a force into components along and perpendicular to a direction."),
        ("Irregular Plot Area", "Divide into triangles, compute each area (½ab sin C), and sum."),
    ],
    [
        ("A truss member is in tension at 500 N at 30° to horizontal. Horizontal component:", ["500 N", "*500 cos 30° ≈ 433 N", "500 sin 30° = 250 N", "500 tan 30°"],
         "Horizontal = F cos θ."),
        ("Same member: vertical component:", ["500 N", "433 N", "*500 sin 30° = 250 N", "500 cos 30°"],
         "Vertical = F sin θ."),
        ("Two forces of 100 N and 150 N act at 60° apart. Resultant magnitude:", ["250 N", "50 N", "*√(100²+150²+2·100·150·cos60°) = √(10000+22500+15000) = √47500 ≈ 217.9 N", "100 N"],
         "Law of Cosines for vector addition."),
        ("A surveyor measures two sides of a field: 80m, 120m, with included angle 75°. Area:", ["9600 m²", "*½(80)(120)sin75° ≈ 4636 m²", "4800 m²", "2400 m²"],
         "½ ab sin C."),
        ("A roof has a 6:12 pitch. The angle of elevation:", ["30°", "45°", "*arctan(6/12) = arctan(0.5) ≈ 26.57°", "60°"],
         "6:12 means rise 6, run 12."),
        ("An arch spans 20 m with a rise of 5 m. The radius of a circular arch:", ["5 m", "20 m", "*R = (s²/(8h)) + h/2 = (400/40) + 2.5 = 12.5 m", "10 m"],
         "Using the sagitta formula: R = s²/(8h) + h/2."),
        ("A bridge cable makes angles of 25° and 35° with the towers. If the span is 100 m:", ["*Use Law of Sines with the triangle (angles 25°, 35°, 120°) to find cable lengths", "Cable = 100 m", "Use Pythagorean theorem", "Not enough info"],
         "The remaining angle = 180° − 25° − 35° = 120°."),
        ("A surveyor at point A sights point C at 40° from the baseline AB. At B, C is at 60° from BA. AB = 200 m. Find AC:", ["200 m", "*Using Law of Sines: angle C = 80°, AC = 200 sin 60° / sin 80° ≈ 175.9 m", "200 sin 40°", "300 m"],
         "C = 180°−40°−60° = 80°. AC/sinB = AB/sinC."),
        ("Breaking an irregular plot into triangles is a standard technique in:", ["Physics only", "*Land surveying and cartography", "Only astronomy", "Cooking"],
         "Triangulation is fundamental to surveying."),
        ("For a quadrilateral plot, the minimum number of triangles needed:", ["1", "*2", "3", "4"],
         "A quadrilateral can always be split into 2 triangles by one diagonal."),
        ("The total area of the plot equals:", ["*Sum of the areas of all constituent triangles", "Product of diagonals", "Perimeter × height", "Only the largest triangle"],
         "Add up all triangle areas."),
        ("A crane boom is 30 m long at 55° from horizontal. Its tip height:", ["30 m", "*30 sin 55° ≈ 24.57 m", "30 cos 55° ≈ 17.21 m", "30 tan 55°"],
         "Height = length × sin(angle)."),
        ("The horizontal reach of the same boom:", ["30 m", "24.57 m", "*30 cos 55° ≈ 17.21 m", "30 tan 55°"],
         "Horizontal = length × cos(angle)."),
        ("Two walls meet at 110°. A diagonal brace across the gap (walls 6m and 8m) has length:", ["14 m", "2 m", "*√(36+64−2(6)(8)cos110°) ≈ √(100+32.8) ≈ 11.53 m", "10 m"],
         "Law of Cosines: cos 110° ≈ −0.342 → c² ≈ 132.8."),
        ("Surveying accuracy depends on:", ["Only equipment", "Only skill", "*Both instrument precision and correct application of trig laws", "Weather only"],
         "Both measurement quality and mathematical accuracy matter."),
        ("A tunnel must be drilled from both ends. Engineers use:", ["Guessing", "*Trilateral and angular measurements to ensure alignment", "Only one drill", "No math"],
         "Precise trigonometric surveying ensures the tunnels meet."),
        ("The bearing from A to B is 045°. The bearing from A to C is 120°. Angle BAC:", ["165°", "45°", "*75° (120° − 45°)", "120°"],
         "Angle between bearings."),
        ("In structural design, force triangles help determine:", ["*Magnitudes and directions of forces in members", "Only aesthetics", "Only cost", "Color"],
         "Forces are resolved using vector triangles."),
        ("A terrain profile has peaks and valleys. Determining line-of-sight uses:", ["Only addition", "*Elevation data with trig (angles of elevation/depression)", "Only multiplication", "No math"],
         "Lines of sight from one point to another require trig with elevation angles."),
        ("Modern surveying uses total stations that measure:", ["Only distance", "*Both distance and angle electronically, then compute using trig", "Only angles", "Color"],
         "Electronic measurement followed by trig computation."),
    ]
)
lessons[k] = v

# ── 7.7 Astronomy Applications ──
k, v = build_lesson(7, 7, "Astronomy Applications",
    "<h3>Astronomy Applications</h3>"
    "<h4>Stellar Parallax</h4>"
    "<p>The distance to nearby stars is found using Earth's orbital diameter as a baseline and measuring the tiny angle of parallax — a direct application of the Law of Sines.</p>"
    "<h4>Orbital Calculations</h4>"
    "<p>Planetary positions, satellite orbits, and lunar distance calculations all involve oblique triangles.</p>"
    "<h4>Angular Separation</h4>"
    "<p>The angle between two celestial objects as seen from Earth.</p>",
    [
        ("Stellar Parallax", "The apparent shift of a nearby star against distant stars as Earth orbits — used to find distance."),
        ("Parsec", "Distance at which a star has a parallax of 1 arcsecond; ≈ 3.26 light-years."),
        ("Astronomical Unit (AU)", "Mean Earth–Sun distance ≈ 1.496 × 10⁸ km; used as the baseline for parallax."),
        ("Angular Separation", "The angle between two objects as seen from an observer."),
        ("Lunar Distance", "Historically calculated using triangulation from two points on Earth's surface."),
    ],
    [
        ("Stellar parallax uses Earth's orbit as:", ["A telescope", "*A baseline (diameter ≈ 2 AU)", "A magnifier", "A filter"],
         "The baseline is the diameter of Earth's orbit."),
        ("If a star has a parallax angle of 0.5 arcseconds, its distance is:", ["0.5 parsecs", "*2 parsecs", "1 parsec", "5 parsecs"],
         "Distance (pc) = 1 / parallax (arcsec) = 1/0.5 = 2 pc."),
        ("1 parsec ≈", ["1 light-year", "*3.26 light-years", "10 light-years", "0.1 light-years"],
         "1 pc ≈ 3.26 ly."),
        ("The parallax method uses which trig law?", ["Only Pythagorean theorem", "Law of Cosines", "*Law of Sines (very thin triangle)", "No trig"],
         "The triangle is extremely elongated; Law of Sines is used with small angles."),
        ("For very small angles, sin θ ≈", ["cos θ", "tan θ", "*θ (in radians)", "1"],
         "Small-angle approximation: sin θ ≈ θ."),
        ("The Moon's distance from Earth was first calculated using:", ["Radar", "*Triangulation from two cities (different viewing angles)", "GPS", "Starlight"],
         "Different observation points on Earth give slightly different angles → distance."),
        ("Two observers 1000 km apart see the Moon at slightly different positions. This is:", ["An illusion", "*Lunar parallax", "A phase change", "An eclipse"],
         "Different baselines give different apparent positions."),
        ("In the Sun-Earth-Mars triangle during opposition:", ["All angles are 90°", "*The Sun-Earth-Mars angle can be measured, and Kepler's laws give distances", "No triangle exists", "Only the Earth-Mars distance matters"],
         "Orbital mechanics + trig determine planetary distances."),
        ("The angular separation between two stars as seen from Earth is measured in:", ["Meters", "Light-years", "*Degrees or arcminutes/arcseconds", "Kilograms"],
         "Angles on the sky."),
        ("A satellite at altitude h is seen at elevation angle θ from the ground. The slant range R:", ["R = h", "*R = h / sin θ (simplified; exact formula uses Earth's curvature)", "R = h cos θ", "R = h tan θ"],
         "For flat-Earth approx, R = h / sin θ."),
        ("If the Moon subtends an angle of about 0.5° and its distance is 384,400 km, its diameter is:", ["*384400 × tan(0.5°) ≈ 384400 × 0.00873 ≈ 3,356 km", "3,474 km (exact)", "500 km", "1 km"],
         "d = D × tan(angular size). Actual ≈ 3,474 km."),
        ("Kepler's equation relates orbital position to time using:", ["Only algebra", "*An equation involving sine (M = E − e sin E)", "No trig", "Only logarithms"],
         "Kepler's equation: M = E − e sin E (transcendental equation requiring numerical methods)."),
        ("The ecliptic is tilted 23.5° relative to the celestial equator because:", ["The Moon orbits at 23.5°", "*Earth's axis is tilted 23.5° from perpendicular to its orbital plane", "The Sun rotates", "Stars move"],
         "Earth's axial tilt causes the ecliptic–equator offset."),
        ("To find the distance between two planets at known orbital radii and angular separation:", ["Add the radii", "*Use the Law of Cosines with the two radii and the angle between them", "Subtract the radii", "Multiply"],
         "SAS triangle: two radii and the angle at the Sun."),
        ("Mars orbits at ~1.52 AU, Earth at 1 AU. When 60° apart from the Sun:", ["d = 2.52 AU", "*d² = 1² + 1.52² − 2(1)(1.52)cos60° = 1 + 2.31 − 1.52 = 1.79 → d ≈ 1.34 AU", "d = 0.52 AU", "d = 1 AU"],
         "Law of Cosines."),
        ("The transit of Venus was historically used to determine:", ["Venus's color", "Earth's mass", "*The Earth-Sun distance (1 AU)", "Venus's atmosphere"],
         "Timing transits from different locations → solar parallax → AU."),
        ("Radio telescopes measure angular position to determine:", ["Color", "*Precise coordinates and separation of celestial objects", "Mass", "Temperature directly"],
         "Angular resolution and position measurement."),
        ("The small-angle formula d = Dθ assumes:", ["θ in degrees", "*θ in radians and very small", "θ in arcminutes", "D is small"],
         "d = Dθ for θ in radians, θ << 1."),
        ("Astronomers use trig to compute:", ["*Distances, sizes, orbits, and positions of celestial objects", "Only brightness", "Only color", "Only mass"],
         "Trigonometry is foundational to astrometry."),
        ("The nearest star (Proxima Centauri) has a parallax of about 0.77 arcseconds. Distance:", ["0.77 pc", "*1/0.77 ≈ 1.30 parsecs ≈ 4.24 ly", "0.77 ly", "7.7 pc"],
         "d = 1/p = 1/0.77 ≈ 1.30 pc."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 7: wrote {len(lessons)} lessons")
