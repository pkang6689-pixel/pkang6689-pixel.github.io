#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 3: Inverse Trig Functions (6 lessons)."""
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

# ── 3.1 ──
k, v = build_lesson(3, 1, "Definition & Domains of Inverse Trig Functions",
    "<h3>Inverse Trigonometric Functions</h3>"
    "<p>Because trig functions are periodic (not one-to-one), we <b>restrict domains</b> to create invertible functions.</p>"
    "<h4>Principal Restrictions</h4>"
    "<ul><li><b>sin⁻¹ (arcsin):</b> domain [−1, 1], range [−π/2, π/2].</li>"
    "<li><b>cos⁻¹ (arccos):</b> domain [−1, 1], range [0, π].</li>"
    "<li><b>tan⁻¹ (arctan):</b> domain (−∞, ∞), range (−π/2, π/2).</li></ul>"
    "<p>Inverse trig functions answer the question: <i>\"What angle has this trig value?\"</i></p>"
    "<p>Notation: sin⁻¹ x = arcsin x (not the reciprocal 1/sin x).</p>",
    [
        ("arcsin (sin⁻¹)", "Inverse sine; domain [−1, 1], range [−π/2, π/2]."),
        ("arccos (cos⁻¹)", "Inverse cosine; domain [−1, 1], range [0, π]."),
        ("arctan (tan⁻¹)", "Inverse tangent; domain (−∞, ∞), range (−π/2, π/2)."),
        ("Principal Value", "The unique output of an inverse trig function within its restricted range."),
        ("Domain Restriction", "Limiting the domain of a trig function so it becomes one-to-one and thus invertible."),
    ],
    [
        ("The range of arcsin is:", ["[0, π]", "*[−π/2, π/2]", "(−∞, ∞)", "[0, 2π]"],
         "arcsin outputs angles in [−π/2, π/2]."),
        ("The range of arccos is:", ["[−π/2, π/2]", "*[0, π]", "(−∞, ∞)", "[0, 2π]"],
         "arccos outputs angles in [0, π]."),
        ("The range of arctan is:", ["[0, π]", "[−π/2, π/2] (closed)", "*(−π/2, π/2) (open)", "(−∞, ∞)"],
         "arctan outputs angles in the open interval (−π/2, π/2)."),
        ("The domain of arcsin is:", ["(−∞, ∞)", "*[−1, 1]", "[0, 1]", "[−π, π]"],
         "sin values only range from −1 to 1."),
        ("The domain of arctan is:", ["[−1, 1]", "[0, 1]", "*(−∞, ∞)", "[−π, π]"],
         "tan can produce any real number, so arctan accepts all reals."),
        ("sin⁻¹(1/2) =", ["π/3", "*π/6", "π/4", "π"],
         "sin(π/6) = 1/2, and π/6 is in [−π/2, π/2]."),
        ("cos⁻¹(0) =", ["0", "*π/2", "π", "2π"],
         "cos(π/2) = 0, and π/2 is in [0, π]."),
        ("tan⁻¹(1) =", ["π/2", "*π/4", "π/6", "0"],
         "tan(π/4) = 1, and π/4 is in (−π/2, π/2)."),
        ("arcsin(−1) =", ["π", "−π", "3π/2", "*−π/2"],
         "sin(−π/2) = −1."),
        ("arccos(−1) =", ["−π", "*π", "−π/2", "2π"],
         "cos(π) = −1, and π is in [0, π]."),
        ("sin⁻¹ x does NOT mean:", ["arcsin x", "Inverse sine of x", "*1/sin x", "The angle whose sine is x"],
         "sin⁻¹ x = arcsin x, not the reciprocal (which is csc x)."),
        ("Why do we restrict the domain of sine before inverting?", ["To get larger values", "*To make it one-to-one (pass horizontal line test)", "To make it continuous", "To change its period"],
         "A function must be one-to-one to have an inverse."),
        ("sin⁻¹(√2/2) =", ["π/3", "*π/4", "π/6", "π/2"],
         "sin(π/4) = √2/2."),
        ("cos⁻¹(1/2) =", ["π/6", "*π/3", "π/4", "π/2"],
         "cos(π/3) = 1/2."),
        ("arctan(0) =", ["π/2", "π", "*0", "−π/2"],
         "tan(0) = 0."),
        ("arcsin(sin(5π/6)) =", ["5π/6", "*π/6", "−π/6", "π/3"],
         "sin(5π/6) = 1/2. arcsin(1/2) = π/6 (principal value)."),
        ("arccos(cos(−π/3)) =", ["−π/3", "*π/3", "2π/3", "π"],
         "cos(−π/3) = 1/2. arccos(1/2) = π/3."),
        ("The output of an inverse trig function is:", ["A ratio", "*An angle", "A distance", "A frequency"],
         "Inverse trig functions return angles."),
        ("tan⁻¹(−1) =", ["π/4", "*−π/4", "3π/4", "−3π/4"],
         "tan(−π/4) = −1, and −π/4 ∈ (−π/2, π/2)."),
        ("sin(arcsin x) = ?", ["arcsin x", "1", "*x (for x ∈ [−1, 1])", "sin x"],
         "sin and arcsin are inverses: sin(arcsin x) = x for x in the domain."),
    ]
)
lessons[k] = v

# ── 3.2 ──
k, v = build_lesson(3, 2, "Graphs of Inverse Trig Functions",
    "<h3>Graphs of Inverse Trig Functions</h3>"
    "<h4>y = arcsin x</h4>"
    "<ul><li>Domain [−1, 1], range [−π/2, π/2]. S-shaped curve passing through the origin.</li>"
    "<li>Increasing. Endpoints: (−1, −π/2) and (1, π/2).</li></ul>"
    "<h4>y = arccos x</h4>"
    "<ul><li>Domain [−1, 1], range [0, π]. Decreasing curve.</li>"
    "<li>Endpoints: (−1, π) and (1, 0).</li></ul>"
    "<h4>y = arctan x</h4>"
    "<ul><li>Domain (−∞, ∞), range (−π/2, π/2). Increasing S-curve with horizontal asymptotes at y = ±π/2.</li></ul>"
    "<p>Each inverse trig graph is the reflection of the corresponding restricted trig graph over y = x.</p>",
    [
        ("arcsin Graph", "S-shaped, increasing from (−1, −π/2) to (1, π/2), passing through the origin."),
        ("arccos Graph", "Decreasing curve from (−1, π) to (1, 0)."),
        ("arctan Asymptotes", "Horizontal asymptotes at y = −π/2 (left) and y = π/2 (right)."),
        ("Reflection Principle", "The graph of f⁻¹ is the reflection of f over the line y = x."),
        ("arctan Graph", "Increasing S-curve from bottom-left to top-right, always between y = −π/2 and y = π/2."),
    ],
    [
        ("The graph of y = arcsin x passes through:", ["(0, 1)", "*(0, 0)", "(1, 1)", "(0, π)"],
         "arcsin(0) = 0."),
        ("y = arccos x at x = 1 gives:", ["π", "π/2", "*0", "1"],
         "arccos(1) = 0."),
        ("y = arccos x at x = −1 gives:", ["0", "*π", "−π", "2π"],
         "arccos(−1) = π."),
        ("y = arctan x has horizontal asymptotes at:", ["y = 0 and y = π", "*y = −π/2 and y = π/2", "y = −1 and y = 1", "y = 0 and y = 1"],
         "As x → ±∞, arctan x → ±π/2."),
        ("y = arcsin x is:", ["Decreasing", "*Increasing", "Constant", "Oscillating"],
         "arcsin is increasing over its domain."),
        ("y = arccos x is:", ["Increasing", "*Decreasing", "Constant", "Oscillating"],
         "arccos is decreasing over [−1, 1]."),
        ("y = arctan x is:", ["Decreasing", "*Increasing", "Constant", "Oscillating"],
         "arctan is increasing over all reals."),
        ("The graph of arcsin is a reflection of the restricted sine graph over:", ["The x-axis", "The y-axis", "*The line y = x", "The origin"],
         "Inverse function graphs are reflections over y = x."),
        ("arcsin has endpoints:", ["(0, 0) and (1, π)", "*(−1, −π/2) and (1, π/2)", "(−π/2, −1) and (π/2, 1)", "(0, −1) and (π, 1)"],
         "arcsin(−1) = −π/2, arcsin(1) = π/2."),
        ("Does arctan have endpoints?", ["Yes, (−1, −π/4) and (1, π/4)", "*No, the domain is all reals — it has asymptotes instead", "Yes, at (−∞, −π/2) and (∞, π/2)", "Yes, at 0 and π"],
         "arctan is defined for all reals and approaches (but never reaches) ±π/2."),
        ("arctan(0) =", ["π/2", "*0", "π", "−π/2"],
         "arctan(0) = 0."),
        ("As x → ∞, arctan x →", ["∞", "0", "*π/2", "1"],
         "arctan x approaches π/2 from below."),
        ("As x → −∞, arctan x →", ["−∞", "0", "*−π/2", "−1"],
         "arctan x approaches −π/2 from above."),
        ("arccos(0) =", ["0", "*π/2", "π", "−π/2"],
         "cos(π/2) = 0, so arccos(0) = π/2."),
        ("Where does y = arccos x cross the y-axis?", ["(0, 0)", "*(0, π/2)", "(0, π)", "(0, 1)"],
         "arccos(0) = π/2."),
        ("Which inverse trig graph has the widest domain?", ["arcsin", "arccos", "*arctan", "All same"],
         "arctan has domain (−∞, ∞); arcsin and arccos are limited to [−1, 1]."),
        ("The range of arcsin and arctan both contain:", ["π", "2π", "*0", "π/2 (only one contains it as closed)"],
         "Both domains contain 0 in their ranges (arcsin(0)=0, arctan(0)=0)."),
        ("arccos(√2/2) =", ["π/6", "*π/4", "π/3", "π/2"],
         "cos(π/4) = √2/2."),
        ("arcsin(−√3/2) =", ["−π/6", "*−π/3", "2π/3", "π/3"],
         "sin(−π/3) = −√3/2, and −π/3 ∈ [−π/2, π/2]."),
        ("Is the graph of y = arctan x symmetric about the origin?", ["*Yes, arctan is an odd function", "No", "It's symmetric about the y-axis", "It has no symmetry"],
         "arctan(−x) = −arctan(x), so it's odd with origin symmetry."),
    ]
)
lessons[k] = v

# ── 3.3 ──
k, v = build_lesson(3, 3, "Solving Equations with Inverse Trig",
    "<h3>Solving Equations with Inverse Trig Functions</h3>"
    "<p>To solve equations like sin θ = 0.6, use inverse trig functions to find θ.</p>"
    "<h4>Steps</h4>"
    "<ul><li>Step 1: Isolate the trig function.</li>"
    "<li>Step 2: Apply the inverse to get the <b>principal value</b>.</li>"
    "<li>Step 3: Find <b>all solutions</b> using symmetry and periodicity.</li></ul>"
    "<h4>Example</h4>"
    "<p>Solve sin θ = 0.5 for 0 ≤ θ ≤ 2π.</p>"
    "<ul><li>Principal: θ₁ = arcsin(0.5) = π/6.</li>"
    "<li>Sine is also positive in Q II: θ₂ = π − π/6 = 5π/6.</li>"
    "<li>Solutions: θ = π/6, 5π/6.</li></ul>",
    [
        ("Principal Value", "The first solution returned by an inverse trig function within its restricted range."),
        ("General Solution (sin)", "If sin θ = a, then θ = arcsin(a) + 2nπ or θ = π − arcsin(a) + 2nπ."),
        ("General Solution (cos)", "If cos θ = a, then θ = ±arccos(a) + 2nπ."),
        ("General Solution (tan)", "If tan θ = a, then θ = arctan(a) + nπ."),
        ("Isolate the Trig Function", "Rearrange the equation so the trig function is alone on one side before applying the inverse."),
    ],
    [
        ("To solve sin θ = 0.5, the first step is:", ["Divide by sin", "*Apply arcsin: θ = arcsin(0.5)", "Square both sides", "Add π"],
         "Take the inverse sine to get the principal value."),
        ("arcsin(0.5) =", ["π/4", "*π/6", "π/3", "π/2"],
         "sin(π/6) = 0.5."),
        ("All solutions of sin θ = 0.5 in [0, 2π] are:", ["π/6 only", "*π/6 and 5π/6", "π/6 and 7π/6", "π/3 and 2π/3"],
         "Sine is positive in Q I (π/6) and Q II (π − π/6 = 5π/6)."),
        ("cos θ = −√3/2, principal value:", ["π/6", "*5π/6", "7π/6", "11π/6"],
         "arccos(−√3/2) = 5π/6 (in [0, π])."),
        ("All solutions of cos θ = −√3/2 in [0, 2π]:", ["5π/6 only", "*5π/6 and 7π/6", "π/6 and 11π/6", "π/3 and 5π/3"],
         "Cosine is negative in Q II and Q III: 5π/6 and 2π − 5π/6 = 7π/6."),
        ("tan θ = √3, principal value:", ["π/6", "*π/3", "π/4", "π/2"],
         "arctan(√3) = π/3."),
        ("All solutions of tan θ = √3 in [0, 2π]:", ["π/3 only", "*π/3 and 4π/3", "π/6 and 7π/6", "π/3 and 2π/3"],
         "Tangent has period π: θ = π/3 and π/3 + π = 4π/3."),
        ("Solve 2 sin θ − 1 = 0 for θ (principal):", ["arcsin(2)", "*π/6", "π/3", "π/4"],
         "2 sin θ = 1 → sin θ = 1/2 → θ = π/6."),
        ("Solve cos θ = 0 for 0 ≤ θ < 2π:", ["0", "*π/2, 3π/2", "π", "π/2 only"],
         "cos θ = 0 at π/2 and 3π/2."),
        ("sin θ = −1; θ in [0, 2π]:", ["π", "*3π/2", "π/2", "0"],
         "sin(3π/2) = −1."),
        ("The general solution of sin θ = a includes nπ terms because:", ["Sine has period π", "*Sine has period 2π (add 2nπ) with a symmetric Q II solution", "Sine is odd", "Sine is even"],
         "The general solution accounts for periodicity (2nπ) and the Q II mirror."),
        ("The general solution of tan θ = a is:", ["θ = arctan(a) + 2nπ", "*θ = arctan(a) + nπ", "θ = ±arctan(a) + nπ", "θ = arctan(a) only"],
         "Tangent has period π, so add nπ."),
        ("Solve sin θ = 0 for θ in [0, 2π):", ["*0, π", "π/2, 3π/2", "0 only", "π only"],
         "sin θ = 0 at θ = 0 and π."),
        ("cos θ = 1 for θ in [0, 2π):", ["π", "π/2", "*0", "2π"],
         "cos(0) = 1. (2π not included in the half-open interval.)"),
        ("Solve √2 sin θ = 1 for θ = ?", ["π/6", "*π/4", "π/3", "π/2"],
         "sin θ = 1/√2 = √2/2 → θ = π/4."),
        ("If cos θ = 0.8, how many solutions in [0, 2π]?", ["0", "1", "*2", "4"],
         "Cosine positive in Q I and Q IV gives two solutions."),
        ("arctan(−√3) =", ["π/3", "*−π/3", "2π/3", "−π/6"],
         "tan(−π/3) = −√3, and −π/3 ∈ (−π/2, π/2)."),
        ("After finding a principal value, why check other quadrants?", ["Just convention", "*Trig functions repeat and can have the same value in multiple quadrants", "To verify the answer", "It's not necessary"],
         "Trig functions are positive in two quadrants each, so there's usually a second solution per period."),
        ("Solve 2 cos θ + 1 = 0 in [0, 2π]:", ["π/3 and 5π/3", "*2π/3 and 4π/3", "π/6 and 11π/6", "π and 2π"],
         "cos θ = −1/2 → arccos(−1/2) = 2π/3. Also 4π/3 in Q III."),
        ("Which inverse trig function has the simplest general solution (only nπ added)?", ["arcsin", "arccos", "*arctan", "None"],
         "tan has period π, so general solution is arctan(a) + nπ."),
    ]
)
lessons[k] = v

# ── 3.4 ──
k, v = build_lesson(3, 4, "Applications in Geometry & Physics",
    "<h3>Applications of Inverse Trig in Geometry &amp; Physics</h3>"
    "<h4>Geometry</h4>"
    "<ul><li><b>Finding angles</b> in right triangles: θ = arctan(opposite/adjacent).</li>"
    "<li><b>Angle of elevation/depression</b>: using trig ratios and inverses.</li>"
    "<li><b>Angle between vectors</b>: θ = arccos(u·v / (|u||v|)).</li></ul>"
    "<h4>Physics</h4>"
    "<ul><li><b>Projectile motion:</b> launch angle θ = arctan(v_y / v_x).</li>"
    "<li><b>Inclined planes:</b> component analysis using trig inverses.</li>"
    "<li><b>Optics:</b> Snell's law → θ₂ = arcsin((n₁ sin θ₁)/n₂).</li></ul>",
    [
        ("Angle of Elevation", "The angle above the horizontal line of sight, found with arctan(height/distance)."),
        ("Angle of Depression", "The angle below the horizontal line of sight to an object below the observer."),
        ("Vector Angle Formula", "θ = arccos(u·v / (|u||v|)) gives the angle between two vectors."),
        ("Snell's Law", "n₁ sin θ₁ = n₂ sin θ₂; solve for θ₂ using arcsin."),
        ("Launch Angle", "θ = arctan(v_y / v_x) for a projectile's initial velocity components."),
    ],
    [
        ("To find an angle in a right triangle given two sides, you use:", ["A trig function", "*An inverse trig function", "The Pythagorean theorem only", "A logarithm"],
         "If you know sides, inverse trig gives you the angle."),
        ("A ladder 10 m long reaches 8 m up a wall. The angle with the ground is:", ["arccos(8/10)", "*arcsin(8/10)", "arctan(8/10)", "arcsin(10/8)"],
         "sin θ = opposite/hypotenuse = 8/10, so θ = arcsin(0.8)."),
        ("arcsin(0.8) ≈", ["53.1°", "36.9°", "*53.1° (≈ 0.927 rad)", "45°"],
         "arcsin(0.8) ≈ 53.1°."),
        ("A ramp rises 3 m over a horizontal distance of 12 m. The angle is:", ["arcsin(3/12)", "arccos(3/12)", "*arctan(3/12) ≈ 14.0°", "arctan(12/3)"],
         "tan θ = rise/run = 3/12, so θ = arctan(1/4) ≈ 14.0°."),
        ("Angle of elevation from a point 50 m from a tower of height 30 m:", ["arcsin(30/50)", "arccos(30/50)", "*arctan(30/50) ≈ 31.0°", "arctan(50/30)"],
         "tan θ = 30/50, θ = arctan(0.6)."),
        ("The angle between vectors u and v is found using:", ["arcsin", "*arccos(u·v / |u||v|)", "arctan", "The cross product directly"],
         "θ = arccos(u·v / (|u||v|))."),
        ("If u·v = 0, the angle between u and v is:", ["0°", "*90°", "180°", "45°"],
         "arccos(0) = π/2 = 90°."),
        ("In projectile motion, if vy = 10 m/s and vx = 10 m/s, the launch angle is:", ["30°", "*45°", "60°", "90°"],
         "arctan(10/10) = arctan(1) = 45°."),
        ("Snell's law: n₁ sin θ₁ = n₂ sin θ₂. Solving for θ₂:", ["θ₂ = arccos((n₁ sin θ₁)/n₂)", "*θ₂ = arcsin((n₁ sin θ₁)/n₂)", "θ₂ = arctan((n₁ sin θ₁)/n₂)", "θ₂ = n₂/n₁"],
         "Isolate sin θ₂ = (n₁ sin θ₁)/n₂ and apply arcsin."),
        ("Light enters glass (n₂ = 1.5) from air (n₁ = 1) at 30°. Find θ₂:", ["30°", "45°", "*arcsin(sin 30°/1.5) ≈ 19.5°", "arcsin(1.5 sin 30°)"],
         "sin θ₂ = (1 × 0.5)/1.5 = 1/3. θ₂ = arcsin(1/3) ≈ 19.5°."),
        ("An airplane descends at a 3° angle of depression. This means:", ["The nose points 3° above horizontal", "*The flight path is 3° below horizontal", "The altitude is 3°", "The speed is 3 m/s"],
         "Angle of depression is measured below the horizontal."),
        ("On an inclined plane at 25°, the gravitational component along the slope is:", ["mg cos 25°", "*mg sin 25°", "mg tan 25°", "mg / sin 25°"],
         "The along-the-plane component is mg sin θ."),
        ("A surveyor stands 200 m from a building and measures a 32° angle of elevation. Building height ≈", ["200 sin 32°", "*200 tan 32° ≈ 125 m", "200 cos 32°", "200/tan 32°"],
         "tan 32° = h/200, so h = 200 tan 32° ≈ 125 m."),
        ("Inverse trig is needed when you know ____ and want ____.", ["An angle; a side", "*A ratio (or sides); an angle", "Both angles; nothing", "The hypotenuse; the area"],
         "Given side ratios, inverse trig yields the unknown angle."),
        ("arctan is most commonly used in which scenarios?", ["*Finding angles from opposite and adjacent sides", "Finding hypotenuse length", "Calculating area", "Finding midpoints"],
         "arctan(opp/adj) is the most common inverse trig application."),
        ("In computer graphics, arctan2(y, x) differs from arctan(y/x) by:", ["Nothing", "*Handling all four quadrants correctly", "Using degrees instead of radians", "Being faster"],
         "arctan2 considers the signs of x and y to place the angle in the correct quadrant."),
        ("A satellite dish points at 55° elevation. If the horizontal distance to the satellite's ground point is d, the altitude is:", ["d cos 55°", "*d tan 55°", "d sin 55°", "d / tan 55°"],
         "tan 55° = altitude/d → altitude = d tan 55°."),
        ("Total internal reflection occurs when arcsin(n₂/n₁) gives:", ["0°", "*An angle called the critical angle", "90°", "No output (ratio > 1 means TIR)"],
         "The critical angle is arcsin(n₂/n₁). Beyond it, total internal reflection occurs."),
        ("If two sides of a right triangle are 5 and 12, the acute angle opposite the side of length 5 is:", ["arctan(12/5)", "*arctan(5/12) ≈ 22.6°", "arcsin(12/13)", "arccos(5/13)"],
         "tan θ = 5/12, so θ = arctan(5/12)."),
        ("In a physics lab, measuring the angle θ of a pendulum from its rest position uses:", ["Direct measurement only", "No trig", "*arcsin or arctan of displacement ratios", "arccos of the mass"],
         "If you measure horizontal displacement x and string length L, θ = arcsin(x/L)."),
    ]
)
lessons[k] = v

# ── 3.5 ──
k, v = build_lesson(3, 5, "Restrictions & Principal Values",
    "<h3>Restrictions &amp; Principal Values</h3>"
    "<p>Because trig functions map many angles to the same value, inverse trig functions must use restricted ranges.</p>"
    "<h4>Key Identities for Composition</h4>"
    "<ul><li><b>sin(arcsin x) = x</b> for x ∈ [−1, 1].</li>"
    "<li><b>arcsin(sin θ) = θ</b> only if θ ∈ [−π/2, π/2].</li>"
    "<li><b>cos(arccos x) = x</b> for x ∈ [−1, 1].</li>"
    "<li><b>arccos(cos θ) = θ</b> only if θ ∈ [0, π].</li></ul>"
    "<h4>Common Pitfall</h4>"
    "<p>arcsin(sin(5π/6)) ≠ 5π/6 because 5π/6 ∉ [−π/2, π/2]. Answer: arcsin(1/2) = π/6.</p>",
    [
        ("sin(arcsin x)", "= x, for all x in [−1, 1]. The 'round trip' starting from a value."),
        ("arcsin(sin θ)", "= θ only if θ ∈ [−π/2, π/2]. Otherwise, the principal value is returned."),
        ("Principal Value Convention", "The unique angle in the restricted range that yields the given trig value."),
        ("Common Composition Pitfall", "arcsin(sin θ) ≠ θ when θ is outside [−π/2, π/2]; you must find the equivalent angle in range."),
        ("cos(arccos x)", "= x for x ∈ [−1, 1]."),
    ],
    [
        ("sin(arcsin(0.3)) =", ["arcsin(0.3)", "*0.3", "0.3π", "sin(0.3)"],
         "sin(arcsin(x)) = x for x ∈ [−1, 1]."),
        ("arcsin(sin(π/4)) =", ["sin(π/4)", "*π/4", "−π/4", "3π/4"],
         "π/4 ∈ [−π/2, π/2], so arcsin(sin(π/4)) = π/4."),
        ("arcsin(sin(3π/4)) =", ["3π/4", "*π/4", "−π/4", "−3π/4"],
         "sin(3π/4) = √2/2. arcsin(√2/2) = π/4 (the principal value)."),
        ("arccos(cos(π/3)) =", ["cos(π/3)", "*π/3", "2π/3", "−π/3"],
         "π/3 ∈ [0, π], so arccos(cos(π/3)) = π/3."),
        ("arccos(cos(5π/3)) =", ["5π/3", "2π/3", "*π/3", "−π/3"],
         "cos(5π/3) = 1/2. arccos(1/2) = π/3."),
        ("arctan(tan(π/6)) =", ["tan(π/6)", "*π/6", "−π/6", "5π/6"],
         "π/6 ∈ (−π/2, π/2), so result is π/6."),
        ("arctan(tan(3π/4)) =", ["3π/4", "*−π/4", "π/4", "−3π/4"],
         "tan(3π/4) = −1. arctan(−1) = −π/4."),
        ("cos(arccos(−0.5)) =", ["0.5", "*−0.5", "π/3", "2π/3"],
         "cos(arccos(x)) = x for x ∈ [−1, 1]."),
        ("arcsin(sin(−π/6)) =", ["π/6", "*−π/6", "11π/6", "5π/6"],
         "−π/6 ∈ [−π/2, π/2], so the answer is −π/6."),
        ("arcsin(sin(7π/6)) =", ["7π/6", "π/6", "*−π/6", "−7π/6"],
         "sin(7π/6) = −1/2. arcsin(−1/2) = −π/6."),
        ("arccos(cos(−π/4)) =", ["−π/4", "*π/4", "3π/4", "7π/4"],
         "cos(−π/4) = √2/2. arccos(√2/2) = π/4."),
        ("Is sin(arcsin(2)) defined?", ["Yes, it equals 2", "*No, 2 is outside the domain [−1, 1] of arcsin", "Yes, it equals π/2", "Yes, it equals 0"],
         "arcsin is only defined for inputs in [−1, 1]."),
        ("arcsin(sin x) = x is guaranteed when:", ["x ∈ [0, 2π]", "x ∈ (−∞, ∞)", "*x ∈ [−π/2, π/2]", "x ∈ [0, π]"],
         "arcsin returns values in [−π/2, π/2], so equality holds only there."),
        ("tan(arctan(100)) =", ["arctan(100)", "*100", "undefined", "π/2"],
         "tan(arctan(x)) = x for all real x."),
        ("arcsin(sin(2π/3)) =", ["2π/3", "*π/3", "−π/3", "−2π/3"],
         "sin(2π/3) = √3/2. arcsin(√3/2) = π/3."),
        ("arccos(cos(4π/3)) =", ["4π/3", "*2π/3", "π/3", "−2π/3"],
         "cos(4π/3) = −1/2. arccos(−1/2) = 2π/3."),
        ("The principal value convention ensures:", ["Multiple outputs", "*A unique output for each input", "Larger range", "Smaller domain"],
         "By restricting the range, each input maps to exactly one output."),
        ("sin⁻¹(sin(π)) =", ["π", "−π", "*0", "2π"],
         "sin(π) = 0. arcsin(0) = 0."),
        ("cos⁻¹(cos(2π)) =", ["2π", "*0", "π", "−π"],
         "cos(2π) = 1. arccos(1) = 0."),
        ("To evaluate arcsin(sin θ) when θ is outside the principal range, you:", ["Just use θ", "*Find the equivalent angle in [−π/2, π/2] with the same sine value", "Use arccos instead", "The answer is undefined"],
         "Find which angle in [−π/2, π/2] produces the same sine."),
    ]
)
lessons[k] = v

# ── 3.6 ──
k, v = build_lesson(3, 6, "Applications in Engineering",
    "<h3>Engineering Applications of Inverse Trig</h3>"
    "<h4>Signal Processing</h4>"
    "<ul><li><b>Phase detection:</b> arctan(Im/Re) extracts the phase angle of a complex signal.</li>"
    "<li><b>Beamforming:</b> arcsin(d sin θ / λ) determines antenna array steering angles.</li></ul>"
    "<h4>Mechanical Engineering</h4>"
    "<ul><li><b>Linkage analysis:</b> inverse trig finds joint angles from link lengths.</li>"
    "<li><b>Cam design:</b> follower position involves arctan and arccos of geometric ratios.</li></ul>"
    "<h4>Electrical Engineering</h4>"
    "<ul><li><b>Power factor angle:</b> θ = arccos(P/S) where P = real power, S = apparent power.</li>"
    "<li><b>Impedance angle:</b> θ = arctan(X_L / R) for an RL circuit.</li></ul>",
    [
        ("Phase Angle", "arctan(Im/Re); the angle of a complex number or signal in the complex plane."),
        ("Power Factor Angle", "θ = arccos(P/S); relates real power to apparent power in AC circuits."),
        ("Impedance Angle", "θ = arctan(reactance / resistance); describes the phase between voltage and current."),
        ("Beamforming", "Using arcsin to calculate steering angles for phased antenna arrays."),
        ("Linkage Analysis", "Using inverse trig to determine joint angles in mechanical linkages from known lengths."),
    ],
    [
        ("The phase angle of a complex signal is found using:", ["arcsin", "arccos", "*arctan(Im/Re)", "arctan(Re/Im)"],
         "Phase = arctan(imaginary part / real part)."),
        ("Power factor angle in AC circuits: θ =", ["arcsin(P/S)", "*arccos(P/S)", "arctan(P/S)", "arcsin(S/P)"],
         "Power factor = cos θ = P/S, so θ = arccos(P/S)."),
        ("If P = 300 W and S = 500 VA, the power factor angle is:", ["arcsin(0.6)", "*arccos(0.6) ≈ 53.1°", "arctan(0.6)", "arccos(500/300)"],
         "θ = arccos(300/500) = arccos(0.6) ≈ 53.1°."),
        ("For an RL circuit with R = 100 Ω and X_L = 100 Ω, impedance angle:", ["30°", "*45°", "60°", "90°"],
         "θ = arctan(100/100) = arctan(1) = 45°."),
        ("In beamforming, arcsin is used to find:", ["Signal strength", "*Steering angle for antenna arrays", "Power consumption", "Resistance"],
         "arcsin relates element spacing and wavelength to beam direction."),
        ("A four-bar linkage has links of known lengths. Joint angles are found using:", ["Calculus", "*Inverse trig functions applied to the geometry", "Linear algebra only", "Integration"],
         "Geometric relationships in linkages yield trig equations solved with inverse trig."),
        ("arctan2(y, x) is preferred over arctan(y/x) in engineering because:", ["It's faster", "*It handles all four quadrants correctly", "It gives radians", "It's more accurate"],
         "arctan2 uses both signs of x and y to determine the correct quadrant."),
        ("A robot arm with link length L needs to reach point (x, y). The joint angle is:", ["arcsin(L/x)", "*arctan(y/x) (simplified)", "arccos(x+y)", "π/4 always"],
         "The angle to the target is arctan(y/x) (simplified 2D case)."),
        ("In a cam mechanism, the follower position often involves:", ["Only linear equations", "*arccos or arctan of geometric ratios", "Exponentials", "Logarithms"],
         "The geometry of cam profiles leads to inverse trig expressions."),
        ("If a signal has Re = 3 and Im = 4, the phase angle is:", ["arctan(3/4)", "*arctan(4/3) ≈ 53.1°", "arcsin(4/5)", "arccos(3/5)"],
         "Phase = arctan(Im/Re) = arctan(4/3)."),
        ("An impedance angle of 0° means:", ["*Purely resistive circuit (no reactance)", "Purely capacitive", "Purely inductive", "Open circuit"],
         "θ = 0 → arctan(X/R) = 0 → X = 0, purely resistive."),
        ("An impedance angle of 90° means:", ["Purely resistive", "*Purely reactive (inductive or capacitive)", "Short circuit", "No current"],
         "θ = 90° → X/R = tan 90° → R ≈ 0, purely reactive."),
        ("In surveying, a transit measures angles then converts to distances using:", ["Only addition", "*Trig and inverse trig functions", "Multiplication only", "Subtraction"],
         "Surveying relies heavily on trig ratios and their inverses."),
        ("A solar panel's tilt angle for maximum output: θ ≈ latitude. This is related to:", ["arccos of productivity", "*arctan of sun elevation geometry", "Random choice", "arcsin of panel area"],
         "The optimal tilt relates to the sun's elevation angle, involving inverse trig."),
        ("Arccos appears in calculating:", ["Velocity", "Acceleration", "*Angles between force vectors", "Mass"],
         "θ = arccos(F₁·F₂ / |F₁||F₂|) gives the angle between forces."),
        ("In navigation, bearing angles involve:", ["arctan(latitude/longitude)", "*arctan(Δx/Δy) converted to compass bearing", "arccos of distance", "No trig"],
         "Bearings use arctan of coordinate differences."),
        ("Power factor cos θ = 1 means θ =", ["90°", "45°", "*0°", "180°"],
         "arccos(1) = 0°."),
        ("Power factor cos θ = 0 means θ =", ["0°", "45°", "*90°", "180°"],
         "arccos(0) = 90° — all reactive power."),
        ("A control system uses arctan to convert:", ["Digital to analog", "*Cartesian coordinates to polar angle", "Frequency to amplitude", "Voltage to current"],
         "arctan(y/x) gives the polar angle from Cartesian coordinates."),
        ("In robotics, inverse kinematics problems are solved using:", ["Only linear math", "*Inverse trig (arccos, arctan) to find joint angles", "Random search", "No computation"],
         "Finding arm joint angles from end-effector position requires inverse trig."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 3: wrote {len(lessons)} lessons")
