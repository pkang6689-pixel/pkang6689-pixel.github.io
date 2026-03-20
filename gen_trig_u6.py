#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 6: Solving Trig Equations (7 lessons)."""
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

# ── 6.1 ──
k, v = build_lesson(6, 1, "Solving Linear Trig Equations",
    "<h3>Solving Linear Trig Equations</h3>"
    "<p>A linear trig equation has the form <b>a · trig(θ) + b = 0</b>.</p>"
    "<h4>Steps</h4>"
    "<ul><li>1. Isolate the trig function.</li>"
    "<li>2. Use inverse trig to find the principal solution.</li>"
    "<li>3. Identify all solutions in the given interval using quadrant analysis.</li></ul>"
    "<h4>Example</h4>"
    "<p>2 sin θ − 1 = 0 → sin θ = 1/2 → θ = π/6, 5π/6 (in [0, 2π)).</p>",
    [
        ("Isolate the Trig Function", "Rearrange so sin θ = k, cos θ = k, or tan θ = k."),
        ("Principal Solution", "The first answer from the inverse trig function."),
        ("Quadrant Analysis", "Determine which quadrants yield the correct sign to find all solutions."),
        ("General Solution", "Add full-period multiples (2nπ or nπ) to cover all solutions."),
        ("Linear Trig Equation", "Equation with trig function raised to the first power, e.g., 2cosθ + 1 = 0."),
    ],
    [
        ("Solve 2 sin θ − 1 = 0:", ["sin θ = 2", "*sin θ = 1/2", "sin θ = −1/2", "sin θ = 1"],
         "Isolate: sin θ = 1/2."),
        ("Solutions of sin θ = 1/2 in [0, 2π):", ["π/6 only", "*π/6 and 5π/6", "π/3 and 2π/3", "π/6 and 7π/6"],
         "Sine positive in Q I and Q II: π/6 and π − π/6 = 5π/6."),
        ("Solve cos θ = −1/2 in [0, 2π):", ["π/3 and 5π/3", "*2π/3 and 4π/3", "π/6 and 11π/6", "π and 2π"],
         "cos negative in Q II and Q III: 2π/3 and 4π/3."),
        ("Solve tan θ = 1 in [0, 2π):", ["π/4 only", "*π/4 and 5π/4", "π/4 and 3π/4", "π/4 and 7π/4"],
         "tan positive in Q I and Q III: π/4 and π/4 + π = 5π/4."),
        ("Solve 3 cos θ + 3 = 0:", ["cos θ = 3", "cos θ = 0", "*cos θ = −1, so θ = π", "cos θ = 1"],
         "3cosθ = −3 → cosθ = −1 → θ = π."),
        ("Solve √2 sin θ = 1 in [0, 2π):", ["*π/4 and 3π/4", "π/4 only", "π/3 and 2π/3", "π/6 and 5π/6"],
         "sinθ = 1/√2 = √2/2. Q I: π/4, Q II: 3π/4."),
        ("Solve 2 cos θ − √3 = 0 in [0, 2π):", ["π/3 only", "*π/6 and 11π/6", "π/6 only", "5π/6 and 7π/6"],
         "cosθ = √3/2. Positive in Q I (π/6) and Q IV (11π/6)."),
        ("The general solution of sin θ = 1/2:", ["θ = π/6 + nπ", "*θ = π/6 + 2nπ or θ = 5π/6 + 2nπ", "θ = π/6 only", "θ = nπ/6"],
         "Both solutions repeat every 2π."),
        ("Solve tan θ = −√3 in [0, 2π):", ["π/3 and 4π/3", "*2π/3 and 5π/3", "π/6 and 7π/6", "π/3 and 2π/3"],
         "ref = π/3. tan negative in Q II (π−π/3 = 2π/3) and Q IV (2π−π/3 = 5π/3)."),
        ("Solve sin θ = 0 in [0, 2π):", ["0 only", "*0 and π", "π/2 and 3π/2", "0, π/2, π, 3π/2"],
         "sin θ = 0 at θ = 0 and π."),
        ("Solve cos θ = 1 in [0, 2π):", ["0 and 2π", "π", "*0", "π/2"],
         "cos(0) = 1. (2π is excluded from [0, 2π).)"),
        ("Solve 4 sin θ + 2 = 0:", ["sin θ = 2", "sin θ = −2", "*sin θ = −1/2 → θ = 7π/6, 11π/6", "sin θ = 1/2"],
         "sinθ = −1/2. Negative in Q III and Q IV."),
        ("When solving, always isolate the trig function:", ["After applying inverse", "Never", "*First, before using inverse trig", "Last"],
         "Isolate first, then apply the inverse."),
        ("Solve sec θ = 2 in [0, 2π):", ["θ = 2", "*cos θ = 1/2 → θ = π/3, 5π/3", "θ = π/2", "θ = 0"],
         "sec θ = 2 → cos θ = 1/2."),
        ("Solve csc θ = −2 in [0, 2π):", ["π/6, 5π/6", "*7π/6, 11π/6", "π/3, 2π/3", "0, π"],
         "sinθ = −1/2 → Q III (7π/6) and Q IV (11π/6)."),
        ("How many solutions does cos θ = 0.5 have in [0, 2π)?", ["1", "*2", "0", "4"],
         "cos positive in Q I and Q IV → 2 solutions."),
        ("How many solutions does sin θ = 2 have?", ["1", "2", "*0 (no solution: |sin θ| ≤ 1)", "Infinite"],
         "sin θ cannot exceed 1."),
        ("Solve 5 tan θ = 5:", ["θ = 5", "*tan θ = 1 → θ = π/4 + nπ", "θ = π", "No solution"],
         "tanθ = 1, general solution θ = π/4 + nπ."),
        ("The number of solutions in [0, 2π) for sin θ = k (where −1 < k < 1, k ≠ 0) is always:", ["1", "*2", "0", "3"],
         "Two solutions: one in Q I/II and one in Q III/IV (or similar)."),
        ("Check: does θ = 5π/6 satisfy sin θ = 1/2?", ["No", "*Yes: sin(5π/6) = sin(π − π/6) = sin(π/6) = 1/2", "Only approximately", "Only in degrees"],
         "sin(5π/6) = 1/2 ✓."),
    ]
)
lessons[k] = v

# ── 6.2 ──
k, v = build_lesson(6, 2, "Solving Quadratic Trig Equations",
    "<h3>Solving Quadratic Trig Equations</h3>"
    "<p>Equations like 2sin²θ − sinθ − 1 = 0 are quadratic in the trig function.</p>"
    "<h4>Strategy</h4>"
    "<ul><li>Let u = sin θ (or cos θ, tan θ) to get a standard quadratic: au² + bu + c = 0.</li>"
    "<li>Factor or use the quadratic formula.</li>"
    "<li>Solve each factor: u = k₁ or u = k₂ → trig θ = k → find θ.</li>"
    "<li>Reject solutions outside the trig function's range.</li></ul>",
    [
        ("Substitution Method", "Let u = sinθ (or cosθ) to convert to au²+bu+c = 0."),
        ("Factoring", "Factor the quadratic, then set each factor to zero."),
        ("Quadratic Formula", "u = (−b ± √(b²−4ac)) / 2a when factoring is difficult."),
        ("Reject Extraneous Solutions", "Discard u values outside [−1,1] for sin/cos."),
        ("Back-Substitute", "Replace u with the trig function and solve for θ."),
    ],
    [
        ("2sin²θ − sinθ − 1 = 0. Let u = sinθ:", ["2u² − u + 1 = 0", "*2u² − u − 1 = 0", "u² − 2u − 1 = 0", "2u + 1 = 0"],
         "Direct substitution gives 2u² − u − 1 = 0."),
        ("Factor 2u² − u − 1:", ["(u−1)(2u+1)", "*(2u+1)(u−1) = 0", "(2u−1)(u+1)", "(u+1)(2u−1)"],
         "(2u+1)(u−1) = 0 → u = −1/2 or u = 1."),
        ("sin θ = 1 gives θ =", ["0", "*π/2", "π", "3π/2"],
         "Sin equals 1 only at π/2."),
        ("sin θ = −1/2 in [0, 2π) gives:", ["π/6, 5π/6", "*7π/6, 11π/6", "π/3, 2π/3", "0, π"],
         "Sine negative in Q III and Q IV: 7π/6 and 11π/6."),
        ("So 2sin²θ − sinθ − 1 = 0 has solutions in [0, 2π):", ["π/2 only", "*π/2, 7π/6, 11π/6", "7π/6, 11π/6 only", "π/6, 5π/6, π/2"],
         "Three solutions: from sinθ = 1 and sinθ = −1/2."),
        ("Solve cos²θ − cos θ = 0:", ["cos θ = 1 only", "*cos θ(cos θ − 1) = 0 → cos θ = 0 or cos θ = 1", "cos θ = −1 or 1", "No solution"],
         "Factor: cosθ(cosθ − 1) = 0."),
        ("cos θ = 0 in [0, 2π): θ =", ["0", "*π/2, 3π/2", "π", "0, π"],
         "cos θ = 0 at π/2 and 3π/2."),
        ("cos θ = 1 in [0, 2π): θ =", ["π", "π/2", "*0", "2π"],
         "cos 0 = 1."),
        ("Solve 2cos²θ + cosθ − 1 = 0:", ["*Factor: (2cosθ − 1)(cosθ + 1) = 0 → cosθ = 1/2 or cosθ = −1", "cosθ = 2", "(cosθ−1)(2cosθ+1)=0", "No factoring possible"],
         "cosθ = 1/2: θ = π/3, 5π/3. cosθ = −1: θ = π."),
        ("If the quadratic formula gives sinθ = 1.5:", ["θ = arcsin(1.5)", "θ = 90°", "*No solution (|sinθ| ≤ 1)", "θ = 56.4°"],
         "1.5 is outside the range of sine; reject it."),
        ("Solve tan²θ − 3 = 0:", ["tanθ = 3", "*tanθ = ±√3 → θ = π/3, 2π/3, 4π/3, 5π/3", "tanθ = 3 or −3", "No solution"],
         "tan²θ = 3 → tanθ = ±√3."),
        ("2sin²θ + sinθ = 0 factors as:", ["sinθ(2sinθ − 1) = 0", "*sinθ(2sinθ + 1) = 0", "(sinθ + 1)(2sinθ) = 0", "Cannot factor"],
         "sinθ(2sinθ + 1) = 0 → sinθ = 0 or sinθ = −1/2."),
        ("Solve 4cos²θ − 1 = 0:", ["cosθ = 4", "*cosθ = ±1/2 → θ = π/3, 2π/3, 4π/3, 5π/3", "cosθ = 2", "cosθ = 1/4"],
         "cos²θ = 1/4 → cosθ = ±1/2."),
        ("When you can't easily factor, use:", ["Guess and check", "*The quadratic formula", "Only graphing", "Trial and error"],
         "The quadratic formula works for any quadratic, including trig quadratics."),
        ("Solve sin²θ − 1 = 0 in [0, 2π):", ["0 and π", "*π/2 and 3π/2", "π only", "0, π/2, π, 3π/2"],
         "sin²θ = 1 → sinθ = ±1 → θ = π/2, 3π/2."),
        ("Some quadratic trig equations can also be solved using:", ["*Pythagorean identity (replace sin²θ with 1−cos²θ)", "Logarithms", "Matrices", "Nothing else"],
         "Replacing sin² with 1−cos² (or vice versa) can reduce to one trig function."),
        ("Solve 2sin²θ − cosθ − 1 = 0 by using sin²θ = 1 − cos²θ:", ["Keep sinθ", "*2(1−cos²θ) − cosθ − 1 = 0 → −2cos²θ − cosθ + 1 = 0 → 2cos²θ + cosθ − 1 = 0", "Add sin²θ", "Can't be done"],
         "Substitute, then solve the resulting quadratic in cosθ."),
        ("In the equation from above, 2cos²θ + cosθ − 1 = 0 gives:", ["cosθ = 1 or −1/2", "*cosθ = 1/2 or cosθ = −1", "cosθ = 2", "cosθ = 0"],
         "(2cosθ−1)(cosθ+1)=0 → cosθ = 1/2 or −1."),
        ("Always check your solutions by:", ["Guessing", "Asking someone", "*Substituting back into the original equation", "Moving on"],
         "Plug θ values back in to verify."),
        ("How many solutions can a quadratic trig equation have in [0, 2π)?", ["Always 2", "Always 4", "*0 to 4 (or more, depending on the equation)", "Exactly 1"],
         "Each factor can give 0, 1, or 2 solutions in [0, 2π)."),
    ]
)
lessons[k] = v

# ── 6.3 ──
k, v = build_lesson(6, 3, "Solving Multiple-Angle Equations",
    "<h3>Solving Multiple-Angle Equations</h3>"
    "<p>Equations like sin(2θ) = √3/2 or cos(3θ) = −1/2 involve a <b>multiple of the angle</b>.</p>"
    "<h4>Method</h4>"
    "<ul><li>Let u = 2θ (or 3θ, etc.).</li>"
    "<li>Solve for u in the expanded interval: if θ ∈ [0, 2π), then u ∈ [0, 4π) for 2θ.</li>"
    "<li>Find all u values in the expanded interval.</li>"
    "<li>Divide by the multiplier to get θ.</li></ul>",
    [
        ("Multiple-Angle Equation", "An equation where the argument of the trig function is nθ (e.g., 2θ, 3θ)."),
        ("Expanded Interval", "If θ ∈ [0, 2π) and argument is nθ, solve for nθ ∈ [0, 2nπ)."),
        ("Substitution u = nθ", "Simplifies the equation to a standard form in u."),
        ("Divide by n", "After finding all u values, θ = u/n gives the final answers."),
        ("More Solutions", "Multiple-angle equations typically have more solutions than single-angle ones in a given interval."),
    ],
    [
        ("To solve sin(2θ) = √3/2, first let:", ["θ = √3/2", "*u = 2θ, then solve sin u = √3/2", "sin θ = √3/4", "2 sinθ = √3/2"],
         "Substitute u = 2θ and solve sin u = √3/2."),
        ("If θ ∈ [0, 2π), then 2θ ∈:", ["[0, 2π)", "[0, π)", "*[0, 4π)", "[0, π/2)"],
         "2θ ranges over [0, 4π)."),
        ("sin u = √3/2 has solutions u = π/3, 2π/3 in [0, 2π). In [0, 4π):", ["π/3, 2π/3 only", "*π/3, 2π/3, 7π/3, 8π/3", "π/3, 2π/3, π/3+4π, 2π/3+4π", "4 more solutions"],
         "Add 2π: π/3+2π = 7π/3, 2π/3+2π = 8π/3."),
        ("So θ = u/2 gives:", ["π/3, 2π/3", "*π/6, π/3, 7π/6, 4π/3", "π/6, π/3 only", "π/6, 2π/3, 7π/6, 8π/3"],
         "Divide each u by 2: π/6, π/3, 7π/6, 4π/3."),
        ("Solve cos(3θ) = 0 for θ ∈ [0, 2π):", ["θ = π/2, 3π/2", "*Let u = 3θ ∈ [0, 6π). cos u = 0 at π/2, 3π/2, 5π/2, 7π/2, 9π/2, 11π/2. θ = u/3.", "Only 2 solutions", "θ = 0, π"],
         "6 values of u give 6 values of θ."),
        ("How many solutions does sin(2θ) = 0 have in [0, 2π)?", ["2", "*4", "1", "8"],
         "2θ = 0, π, 2π, 3π → θ = 0, π/2, π, 3π/2."),
        ("Solve tan(2θ) = 1 in [0, 2π):", ["π/4, 5π/4 only", "*π/8, 5π/8, 9π/8, 13π/8", "π/4 only", "4 solutions at π/4 intervals"],
         "u = 2θ: tan u = 1 → u = π/4 + nπ. In [0,4π): π/4, 5π/4, 9π/4, 13π/4. Divide by 2."),
        ("When the multiple is 3 and θ ∈ [0, 2π), you solve in:", ["[0, 2π)", "[0, 4π)", "*[0, 6π)", "[0, π)"],
         "3θ ranges over [0, 6π)."),
        ("Solve sin(θ/2) = 1/2 for θ ∈ [0, 2π):", ["θ = π/6 or 5π/6", "*u = θ/2 ∈ [0, π). sin u = 1/2 → u = π/6. So θ = π/3.", "θ = π/3, 5π/3", "θ = π/12"],
         "θ/2 ∈ [0, π). sin u = 1/2 at u = π/6 and 5π/6. θ = π/3 and 5π/3."),
        ("For sin(θ/2) = 1/2, u = 5π/6 gives θ =", ["5π/6", "*5π/3", "5π/12", "10π/6"],
         "θ = 2u = 2(5π/6) = 5π/3."),
        ("Solve cos(2θ) = −1 in [0, 2π):", ["θ = π", "*θ = π/2, 3π/2", "θ = 0", "θ = π/4"],
         "2θ = π or 3π → θ = π/2 or 3π/2."),
        ("sin(4θ) = 0 in [0, 2π) has how many solutions?", ["4", "6", "*8", "2"],
         "4θ = 0, π, 2π, 3π, 4π, 5π, 6π, 7π → 8 values of θ."),
        ("Solve 2sin(3θ) − 1 = 0, θ ∈ [0, 2π):", ["2 solutions", "3 solutions", "*6 solutions", "1 solution"],
         "sin(3θ) = 1/2. In [0,6π) there are 6 solutions for u, giving 6 for θ."),
        ("The key insight for multiple-angle equations is:", ["Ignore the multiple", "*Expand the interval proportionally to the multiplier", "Only use the unit circle once", "Use calculus"],
         "If the angle is nθ, solve in [0, 2nπ) for u, then divide."),
        ("cos(2θ) = 1/2 in [0, 2π). How many solutions?", ["2", "*4", "1", "3"],
         "u = 2θ: cos u = 1/2 at u = π/3, 5π/3, 7π/3, 11π/3 in [0,4π). Divide by 2."),
        ("For the problem above, θ values are:", ["π/3, 5π/3", "*π/6, 5π/6, 7π/6, 11π/6", "π/3, 2π/3, 4π/3, 5π/3", "π/4, 3π/4, 5π/4, 7π/4"],
         "θ = π/6, 5π/6, 7π/6, 11π/6."),
        ("tan(3θ) = 0 in [0, 2π) has:", ["3", "2", "*6", "9"],
         "u = 3θ ∈ [0,6π). tan u = 0 at u = 0, π, 2π, 3π, 4π, 5π → 6 values → θ = 0, π/3, 2π/3, π, 4π/3, 5π/3."),
        ("Always remember to check that final θ values are in:", ["(−∞, ∞)", "*(0, 2π) or the specified interval", "[0, 6π)", "No interval"],
         "Discard any θ outside the original interval."),
        ("sin(2θ) = sin θ can be rewritten as:", ["sin θ = 0", "*2sinθcosθ − sinθ = 0 → sinθ(2cosθ − 1) = 0", "sinθ = 2cosθ", "cosθ = 1/2 only"],
         "Use sin2θ = 2sinθcosθ, then factor."),
        ("From sinθ(2cosθ − 1) = 0: sinθ = 0 or cosθ = 1/2, giving in [0, 2π):", ["0, π, π/3", "*0, π, π/3, 5π/3", "π/3, 5π/3 only", "0, π only"],
         "4 solutions total."),
    ]
)
lessons[k] = v

# ── 6.4 ──
k, v = build_lesson(6, 4, "General Solutions & Periodicity",
    "<h3>General Solutions &amp; Periodicity</h3>"
    "<p>When no interval is specified, express <b>all</b> solutions using the period:</p>"
    "<ul><li><b>sin θ = k:</b> θ = arcsin(k) + 2nπ or θ = (π − arcsin(k)) + 2nπ.</li>"
    "<li><b>cos θ = k:</b> θ = ±arccos(k) + 2nπ.</li>"
    "<li><b>tan θ = k:</b> θ = arctan(k) + nπ.</li></ul>"
    "<p>Here n is any integer. These formulas capture every solution by exploiting periodicity.</p>",
    [
        ("General Solution (sin)", "θ = arcsin(k) + 2nπ or θ = π − arcsin(k) + 2nπ, n ∈ ℤ."),
        ("General Solution (cos)", "θ = ±arccos(k) + 2nπ, n ∈ ℤ."),
        ("General Solution (tan)", "θ = arctan(k) + nπ, n ∈ ℤ (period π)."),
        ("n ∈ ℤ", "n is any integer: …, −2, −1, 0, 1, 2, …"),
        ("Why Use General Solutions", "When the domain is all reals, there are infinitely many solutions — general form captures them all."),
    ],
    [
        ("The general solution of sin θ = 0 is:", ["θ = 0", "θ = 2nπ", "*θ = nπ", "θ = π/2 + nπ"],
         "sin θ = 0 at 0, π, 2π, 3π, … = nπ."),
        ("The general solution of cos θ = 0 is:", ["θ = nπ", "*θ = π/2 + nπ", "θ = 2nπ", "θ = nπ/2"],
         "cos θ = 0 at π/2, 3π/2, 5π/2, … = π/2 + nπ."),
        ("The general solution of tan θ = 0 is:", ["θ = π/2 + nπ", "*θ = nπ", "θ = 2nπ", "θ = π/4 + nπ"],
         "tan θ = 0 when sin θ = 0: θ = nπ."),
        ("General solution of sin θ = 1:", ["θ = nπ", "*θ = π/2 + 2nπ", "θ = 2nπ", "θ = π + 2nπ"],
         "sin θ = 1 only at π/2, repeating every 2π."),
        ("General solution of cos θ = −1:", ["θ = 2nπ", "θ = nπ", "*θ = π + 2nπ (= (2n+1)π)", "θ = 3π/2 + 2nπ"],
         "cos θ = −1 at θ = π + 2nπ."),
        ("General solution of tan θ = 1:", ["θ = π/4 + 2nπ", "*θ = π/4 + nπ", "θ = nπ/4", "θ = 2nπ"],
         "tan has period π: arctan(1) = π/4, so θ = π/4 + nπ."),
        ("General solution of sin θ = 1/2:", ["θ = π/6 + nπ", "*θ = π/6 + 2nπ or θ = 5π/6 + 2nπ", "θ = π/6 + 2nπ only", "θ = nπ/6"],
         "Two families of solutions from Q I and Q II."),
        ("General solution of cos θ = 1/2:", ["θ = π/3 + nπ", "*θ = π/3 + 2nπ or θ = −π/3 + 2nπ (i.e., ±π/3 + 2nπ)", "θ = π/6 + 2nπ", "θ = nπ/3"],
         "cos gives ±arccos(k) + 2nπ."),
        ("Why does tan use nπ while sin/cos use 2nπ?", ["Convention", "*tan has period π; sin/cos have period 2π", "tan is simpler", "No reason"],
         "The period determines how often solutions repeat."),
        ("Express all solutions of sin θ = −√3/2:", ["θ = −π/3 + 2nπ", "*θ = −π/3 + 2nπ or θ = π + π/3 + 2nπ = 4π/3 + 2nπ", "θ = 4π/3 + nπ", "θ = π/3 + 2nπ"],
         "arcsin(−√3/2) = −π/3. Other family: π − (−π/3) = 4π/3."),
        ("For cos θ = −√2/2, general solution:", ["θ = π/4 + 2nπ", "*θ = ±3π/4 + 2nπ", "θ = 3π/4 + nπ", "θ = nπ/4"],
         "arccos(−√2/2) = 3π/4. θ = ±3π/4 + 2nπ."),
        ("How many solutions does sin θ = 0.3 have on (−∞, ∞)?", ["2", "1", "*Infinitely many", "0"],
         "Adding 2nπ gives infinitely many solutions."),
        ("n = 0 in the general solution gives:", ["No solution", "*The principal (base) solutions", "The negative solutions", "All solutions"],
         "n = 0 returns the solutions in one base period."),
        ("General solution of 2 cos θ + 1 = 0:", ["θ = π/3 + 2nπ", "*θ = ±2π/3 + 2nπ", "θ = 2π/3 + nπ", "θ = nπ/3"],
         "cosθ = −1/2 → arccos(−1/2) = 2π/3. θ = ±2π/3 + 2nπ."),
        ("If a problem says 'find all solutions,' you must give:", ["Only solutions in [0, 2π)", "*The general solution with n ∈ ℤ", "One solution", "Two solutions"],
         "'All solutions' means the general form."),
        ("To get solutions in [0, 2π) from general form, substitute:", ["n = 0 only", "*Various integer n values and keep θ ∈ [0, 2π)", "n = 1 always", "n = −1"],
         "Plug in n = 0, ±1, ±2, … and keep those in the interval."),
        ("General solution of tan θ = −1:", ["θ = π/4 + nπ", "*θ = −π/4 + nπ = 3π/4 + nπ", "θ = −π/4 + 2nπ", "θ = π/4 + 2nπ"],
         "arctan(−1) = −π/4. Add nπ."),
        ("The general solution combines:", ["Guessing", "*The principal value and the function's period to express all solutions", "Only positive angles", "Calculus"],
         "Principal value + periodicity = all solutions."),
        ("sin θ = sin α has general solution:", ["θ = α", "*θ = α + 2nπ or θ = π − α + 2nπ", "θ = α + nπ", "θ = −α + 2nπ"],
         "Both θ = α and θ = π − α give the same sine value."),
        ("cos θ = cos α has general solution:", ["θ = α + nπ", "*θ = ±α + 2nπ", "θ = α + 2nπ only", "θ = π − α + 2nπ"],
         "cos is even: cos(α) = cos(−α), and periodic with 2π."),
    ]
)
lessons[k] = v

# ── 6.5 ──
k, v = build_lesson(6, 5, "Modeling with Trig Equations",
    "<h3>Modeling with Trig Equations</h3>"
    "<p>Many real-world phenomena are periodic and modeled by sinusoidal equations:</p>"
    "<h4>Examples</h4>"
    "<ul><li><b>Temperature:</b> T(t) = A sin(Bt − C) + D models seasonal temperature variation.</li>"
    "<li><b>Tides:</b> h(t) = A cos(Bt − C) + D models water height over time.</li>"
    "<li><b>Daylight hours:</b> periodic with a 365-day cycle.</li>"
    "<li>Setting the model equal to a value and solving gives the time(s) when that value occurs.</li></ul>",
    [
        ("Sinusoidal Model", "y = A sin(Bt − C) + D or y = A cos(Bt − C) + D for periodic phenomena."),
        ("A = Amplitude", "(max − min)/2; the intensity of variation."),
        ("B = Frequency Factor", "B = 2π/period; controls how fast the cycle repeats."),
        ("D = Vertical Shift", "(max + min)/2; the average value."),
        ("C/B = Phase Shift", "Horizontal shift aligning the model with data."),
    ],
    [
        ("A sinusoidal model has the form:", ["y = mx + b", "*y = A sin(Bt − C) + D", "y = ax² + bx + c", "y = eˣ"],
         "Sinusoidal: amplitude, frequency, phase shift, midline."),
        ("Temperature max = 85°F, min = 35°F. Amplitude A =", ["85", "35", "60", "*25"],
         "A = (85 − 35)/2 = 25."),
        ("Same data: midline D =", ["85", "35", "*60", "25"],
         "D = (85 + 35)/2 = 60."),
        ("If the period is 12 months, B =", ["12", "*2π/12 = π/6", "π/12", "24π"],
         "B = 2π/period = 2π/12 = π/6."),
        ("Tide model: h(t) = 3cos(πt/6) + 5. The amplitude (tide range/2) is:", ["5", "*3", "8", "6"],
         "A = 3 (coefficient of cosine)."),
        ("In h(t) = 3cos(πt/6) + 5, mean water level is:", ["3", "8", "*5", "2"],
         "D = 5."),
        ("The period of h(t) = 3cos(πt/6) + 5:", ["6", "*12 hours", "π/6", "3"],
         "Period = 2π/(π/6) = 12."),
        ("When is h(t) = 8? Solve 3cos(πt/6) + 5 = 8:", ["t = 0 only", "*cos(πt/6) = 1 → πt/6 = 0 → t = 0, 12, 24, …", "t = 6", "No solution"],
         "cos = 1 at argument = 0, 2π, 4π, … → t = 0, 12, 24, …."),
        ("When is h(t) = 5? (at the midline)", ["*cos(πt/6) = 0 → πt/6 = π/2, 3π/2, … → t = 3, 9, 15, …", "Never", "t = 6", "t = 0"],
         "cos = 0 → t = 3, 9, 15, …."),
        ("When is h(t) = 2? (minimum)", ["t = 3", "*cos(πt/6) = −1 → t = 6, 18, …", "Never", "t = 12"],
         "h_min = D − A = 5 − 3 = 2. cos = −1 at πt/6 = π → t = 6."),
        ("Daylight model: D(t) = 2.5sin(2πt/365 − 1.4) + 12. Max daylight ≈", ["12", "*14.5 hours", "2.5", "15"],
         "Max = D + A = 12 + 2.5 = 14.5."),
        ("When does the model predict 13 hours? Solve 2.5sin(2πt/365 − 1.4) + 12 = 13:", ["t = 0", "*sin(2πt/365 − 1.4) = 0.4 → t = (365/2π)(arcsin(0.4) + 1.4) ≈ day 105 and ≈ day 240", "No solution", "t = 182"],
         "Two times per year when daylight crosses 13 hours."),
        ("Creating a model requires knowing:", ["Only the maximum", "*Period, amplitude, vertical shift, and sometimes phase shift", "Only the phase shift", "The slope"],
         "All four parameters define the sinusoidal model."),
        ("Ferris wheel: height h(t) = −20cos(πt/30) + 25. Diameter:", ["25 m", "20 m", "*40 m", "30 m"],
         "Amplitude = 20, so diameter = 2A = 40 m."),
        ("Same Ferris wheel: center height =", ["20 m", "*25 m", "40 m", "30 m"],
         "D = 25 m (midline = center height)."),
        ("Lowest point on the Ferris wheel:", ["0 m", "*5 m", "25 m", "20 m"],
         "Min = D − A = 25 − 20 = 5 m."),
        ("Period of the Ferris wheel:", ["30 s", "15 s", "*60 s", "π/30 s"],
         "Period = 2π/(π/30) = 60 seconds."),
        ("When is the rider at 45 m? Solve −20cos(πt/30) + 25 = 45:", ["Always", "*cos(πt/30) = −1 → t = 30 s (and 30 + 60n)", "Never", "t = 0"],
         "−20cos = 20 → cos = −1 → πt/30 = π → t = 30."),
        ("In modeling, the phase shift C/B adjusts:", ["Amplitude", "Period", "*Where in the cycle the model starts", "Midline"],
         "Phase shift horizontally shifts the curve to match observed data."),
        ("Solving sinusoidal models combines:", ["Only algebra", "*Trig identities, inverse trig, and periodicity", "Only graphing", "Guessing"],
         "All the tools from this unit come together in modeling."),
    ]
)
lessons[k] = v

# ── 6.6 ──
k, v = build_lesson(6, 6, "Physics Cases – Oscillations & Waves",
    "<h3>Physics Cases: Oscillations &amp; Waves</h3>"
    "<h4>Simple Harmonic Motion</h4>"
    "<p>x(t) = A cos(ωt + φ). Setting x = x₀ and solving for t gives the time(s) the object reaches position x₀.</p>"
    "<h4>Resonance</h4>"
    "<p>When driving frequency matches natural frequency, amplitude increases dramatically — found by solving ω_d = ω₀.</p>"
    "<h4>Standing Waves</h4>"
    "<p>Nodes occur where sin(nπx/L) = 0, i.e., at x = kL/n for integer k.</p>",
    [
        ("SHM Equation", "x(t) = A cos(ωt + φ); solving for t when x = x₀ requires inverse trig."),
        ("Resonance", "Occurs when the driving frequency equals the natural frequency, maximizing amplitude."),
        ("Standing Wave Nodes", "Points where displacement is always zero: sin(nπx/L) = 0 → x = kL/n."),
        ("Angular Frequency (ω)", "ω = 2πf; relates to the period by T = 2π/ω."),
        ("Phase Constant (φ)", "Determines the initial position of the oscillator at t = 0."),
    ],
    [
        ("In SHM, x(t) = A cos(ωt + φ). To find when x = 0:", ["t = 0 always", "*cos(ωt + φ) = 0 → ωt + φ = π/2 + nπ", "Solve sin = 0", "t = A"],
         "Set x = 0 and solve the resulting trig equation."),
        ("For x(t) = 5cos(2t), when does x = 5?", ["t = π", "*cos(2t) = 1 → 2t = 2nπ → t = nπ", "t = 5/2", "Never"],
         "cos = 1 at 2t = 2nπ → t = nπ (n = 0, 1, 2, …)."),
        ("For x(t) = 5cos(2t), when does x = 0?", ["t = nπ", "*2t = π/2 + nπ → t = π/4 + nπ/2", "t = 0", "t = 5"],
         "cos = 0 at π/2 + nπ."),
        ("For x(t) = 5cos(2t), when does x = −5?", ["t = 0", "*cos(2t) = −1 → 2t = π + 2nπ → t = π/2 + nπ", "Never", "t = 5"],
         "cos = −1 at π + 2nπ."),
        ("Resonance occurs when ωd =", ["0", "2ω₀", "*ω₀ (natural frequency)", "ω₀/2"],
         "Driving frequency equals natural frequency for resonance."),
        ("Standing waves on a string of length L have nodes where:", ["cos(nπx/L) = 0", "*sin(nπx/L) = 0 → x = kL/n", "The string is vibrating most", "x = L/2 always"],
         "sin = 0 at nπx/L = kπ → x = kL/n."),
        ("For the fundamental mode (n = 1), nodes are at:", ["x = L/2", "*x = 0 and x = L (endpoints only)", "No nodes", "x = L/4 and 3L/4"],
         "sin(πx/L) = 0 at x = 0 and x = L."),
        ("For n = 2 (second harmonic), nodes at:", ["0 and L only", "*0, L/2, and L", "L/4 and 3L/4", "No nodes"],
         "sin(2πx/L) = 0 at x = 0, L/2, L."),
        ("The period of oscillation T relates to ω by:", ["T = ω", "*T = 2π/ω", "T = ω/2π", "T = πω"],
         "T = 2π/ω."),
        ("If ω = 4π rad/s, the period T =", ["4π", "π/2", "*1/2 s", "2 s"],
         "T = 2π/(4π) = 1/2."),
        ("A spring oscillates with x(t) = 3cos(πt). At time t = 1/2:", ["x = 3", "*x = 3cos(π/2) = 0", "x = −3", "x = 1.5"],
         "cos(π/2) = 0."),
        ("Velocity v(t) = −Aω sin(ωt + φ). v = 0 when:", ["x = 0", "*sin(ωt + φ) = 0 → at maximum displacement", "Always", "Never"],
         "Velocity is zero at the turning points (max displacement)."),
        ("The velocity is maximum when:", ["x is maximum", "*x = 0 (equilibrium)", "t = 0 always", "ω = 0"],
         "At equilibrium, all energy is kinetic → max velocity."),
        ("A pendulum swings with θ(t) = 0.1cos(√(g/L)·t). Small-angle approximation uses:", ["tan θ ≈ θ", "*sin θ ≈ θ (for small θ in radians)", "cos θ ≈ θ", "sin θ = 1"],
         "For small angles, sin θ ≈ θ enables the SHM approximation."),
        ("Damped oscillation: x(t) = Ae^(−bt)cos(ωt). To find when x = 0:", ["e^(−bt) = 0", "*cos(ωt) = 0 → t = π/(2ω) + nπ/ω", "Never reaches 0", "t = b"],
         "The exponential never reaches 0, but cosine does."),
        ("In wave interference, sin(kx − ωt) + sin(kx + ωt) =", ["2sin(kx)sin(ωt)", "*2sin(kx)cos(ωt)", "sin(2kx)", "0"],
         "Sum-to-product: 2sin(kx)cos(ωt). This is a standing wave."),
        ("A sonar ping returns in 0.02 s. If v = 1500 m/s:", ["Distance = 30 m", "*Distance = 1500 × 0.02 / 2 = 15 m (round trip)", "Distance = 0.02 m", "Distance = 1500 m"],
         "Sound travels both ways: d = vt/2."),
        ("Electromagnetic wave frequency and wavelength: c = fλ. If f = 100 MHz:", ["λ = 100 m", "*λ = c/f = 3×10⁸/10⁸ = 3 m", "λ = 300 m", "λ = 0.3 m"],
         "λ = 3 × 10⁸ / 10⁸ = 3 m."),
        ("Solving physics trig equations requires:", ["Only basic algebra", "Only graphing", "*Isolating trig functions, applying inverses, and using periodicity", "No math"],
         "Physics applications combine all the solving techniques from this unit."),
        ("The LC circuit oscillation equation is the same form as SHM:", ["No relation", "*Yes: Q(t) = Q₀cos(ωt + φ) where ω = 1/√(LC)", "Only in DC circuits", "Only for resistors"],
         "LC circuits oscillate exactly like mechanical SHM."),
    ]
)
lessons[k] = v

# ── 6.7 ──
k, v = build_lesson(6, 7, "AP Exam Preparation",
    "<h3>AP Exam Preparation: Solving Trig Equations</h3>"
    "<p>AP-style problems combine multiple skills:</p>"
    "<h4>Common AP Question Types</h4>"
    "<ul><li>Find all solutions in [0, 2π) — requires quadrant analysis.</li>"
    "<li>Give general solutions — requires period knowledge.</li>"
    "<li>Application problems — set up and solve sinusoidal models.</li>"
    "<li>Equations requiring identities — use Pythagorean/double-angle before solving.</li></ul>",
    [
        ("AP Strategy: Isolate First", "Get the trig function alone before applying inverse."),
        ("AP Strategy: Check All Quadrants", "Don't miss second solutions from quadrant symmetry."),
        ("AP Strategy: Use Identities", "If the equation has mixed trig functions, convert using identities."),
        ("AP Strategy: Multiple Angles", "Expand the interval proportionally, find all solutions, then divide."),
        ("AP Strategy: Verify", "Plug solutions back in to catch errors."),
    ],
    [
        ("Solve 2sin²θ − 1 = 0 in [0, 2π):", ["π/4 and 3π/4", "π/4, 3π/4, 5π/4, 7π/4", "*π/4, 3π/4, 5π/4, 7π/4", "π/4 only"],
         "sin²θ = 1/2 → sinθ = ±√2/2 → 4 solutions."),
        ("Solve cos(2θ) + cosθ + 1 = 0 in [0, 2π):", ["θ = π only", "*Use cos2θ = 2cos²θ − 1: 2cos²θ + cosθ = 0 → cosθ(2cosθ+1) = 0 → θ = π/2, 3π/2, 2π/3, 4π/3", "No solution", "θ = 0"],
         "Substitute double-angle, factor, solve."),
        ("Solve sin θ + cos θ = 1:", ["*Square both sides: 1 + 2sinθcosθ = 1 → sin2θ = 0 → 2θ = nπ → θ = 0, π/2, π, 3π/2. Check: θ = 0 ✓, π/2 ✓, π ✗, 3π/2 ✗", "θ = π/4", "No solution", "θ = 0 only"],
         "After squaring, check all candidates — squaring can introduce extraneous solutions."),
        ("When you square both sides, you must:", ["Accept all solutions", "*Check each candidate in the original equation", "Only keep positive solutions", "Ignore results"],
         "Squaring can create extraneous roots."),
        ("Solve tan²θ = 3 in [0, 2π):", ["π/3 and 4π/3", "*π/3, 2π/3, 4π/3, 5π/3", "π/3 only", "No solution"],
         "tanθ = ±√3 → 4 solutions."),
        ("Solve sin θ = cos θ:", ["*Divide: tanθ = 1 → θ = π/4 + nπ", "θ = 0", "sinθ − cosθ = 0 only at π/4", "No solution"],
         "tanθ = 1 → θ = π/4 + nπ."),
        ("On the AP exam, 'find all solutions on [0, 2π)' means:", ["General solution", "*List every θ in [0, 2π) that satisfies the equation", "Just one solution", "Approximate to nearest degree"],
         "Specific interval — list all."),
        ("Solve 2cos²θ − cosθ − 1 = 0. Factor:", ["(cosθ − 1)(2cosθ − 1)", "*(2cosθ + 1)(cosθ − 1) = 0", "(cosθ + 1)(2cosθ + 1)", "Can't factor"],
         "cosθ = 1 or cosθ = −1/2. Check by expanding."),
        ("cosθ = 1 → θ = 0. cosθ = −1/2 → θ =", ["π/3, 5π/3", "*2π/3, 4π/3", "0, π", "π/6, 11π/6"],
         "cos negative in Q II and Q III."),
        ("Total solutions for 2cos²θ − cosθ − 1 = 0 in [0, 2π):", ["1", "2", "*3 (θ = 0, 2π/3, 4π/3)", "4"],
         "Three solutions."),
        ("If an equation simplifies to sin θ = 2, then:", ["θ = arcsin(2)", "*No real solution", "θ = π/2", "θ = 90°"],
         "|sinθ| ≤ 1, so sinθ = 2 has no solution."),
        ("Use the identity sin²θ = 1 − cos²θ to convert a mixed equation to:", ["*A single-variable equation (all cosθ or all sinθ)", "Two variables", "No trig", "An exponential"],
         "Converting to one function enables quadratic solving."),
        ("On the AP, you might set up h(t) = 0 where h models height. This requires:", ["Setting time to 0", "*Solving a trig equation for the time variable", "No computation", "Only estimation"],
         "Set the model equal to the target value and solve."),
        ("Solve sin 2θ = cos θ in [0, 2π):", ["*2sinθcosθ − cosθ = 0 → cosθ(2sinθ − 1) = 0 → θ = π/2, 3π/2, π/6, 5π/6", "θ = π/4 only", "θ = 0", "No solution"],
         "Use sin2θ = 2sinθcosθ, factor out cosθ."),
        ("How many solutions: cosθ(2sinθ − 1) = 0 gives:", ["2", "3", "*4", "1"],
         "cosθ = 0: π/2, 3π/2. sinθ = 1/2: π/6, 5π/6. Total: 4."),
        ("On AP free-response, always:", ["*Show all algebraic steps and justify quadrant choices", "Just give the answers", "Use a calculator only", "Guess"],
         "AP scoring requires showing work."),
        ("A common mistake on trig equations:", ["Solving correctly", "*Forgetting the second solution from the other quadrant", "Using identities", "Checking work"],
         "Many students find only one solution per period."),
        ("Solve sec²θ − 2 = 0:", ["secθ = 2", "*sec²θ = 2 → cos²θ = 1/2 → cosθ = ±√2/2 → θ = π/4, 3π/4, 5π/4, 7π/4", "cosθ = √2", "No solution"],
         "Convert to cosine, then solve."),
        ("Time management on AP: trig equation problems should take:", ["20 minutes", "1 minute", "*3–5 minutes (standard difficulty)", "No time if you use a calculator"],
         "Typical AP trig equation problems are 3–5 minutes."),
        ("Final tip: always verify solutions by:", ["Graphing only", "Estimation", "*Substituting back into the original equation", "Asking a friend"],
         "Substitution catches algebraic errors and extraneous solutions."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Trigonometry Unit 6: wrote {len(lessons)} lessons")
