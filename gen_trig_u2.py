#!/usr/bin/env python3
"""Generate real content for Trigonometry Unit 2: Trig Functions & Graphs (7 lessons)."""
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

# ── 2.1 ──
k, v = build_lesson(2, 1, "Definition of Sine, Cosine, Tangent",
    "<h3>Definition of Sine, Cosine, Tangent</h3>"
    "<p>Using the unit circle, trig functions are defined for <b>all</b> real numbers, not just acute angles.</p>"
    "<h4>Unit-Circle Definitions</h4>"
    "<ul><li><b>sin θ</b> = y-coordinate of the point on the unit circle.</li>"
    "<li><b>cos θ</b> = x-coordinate of the point on the unit circle.</li>"
    "<li><b>tan θ</b> = sin θ / cos θ = y/x (undefined when cos θ = 0).</li></ul>"
    "<h4>Domain &amp; Range</h4>"
    "<ul><li>sin θ: domain = all reals, range = [−1, 1].</li>"
    "<li>cos θ: domain = all reals, range = [−1, 1].</li>"
    "<li>tan θ: domain = all reals except θ = π/2 + nπ, range = (−∞, ∞).</li></ul>"
    "<p>These definitions are consistent with SOH-CAH-TOA for acute angles but extend to all quadrants.</p>",
    [
        ("sin θ (unit circle)", "The y-coordinate of the point where the terminal side meets the unit circle."),
        ("cos θ (unit circle)", "The x-coordinate of the point where the terminal side meets the unit circle."),
        ("tan θ", "sin θ / cos θ; undefined when cos θ = 0."),
        ("Range of sin and cos", "[−1, 1]; both functions output values between −1 and 1."),
        ("Domain of tan", "All real numbers except π/2 + nπ (where cos θ = 0)."),
    ],
    [
        ("On the unit circle, sin θ corresponds to which coordinate?", ["x", "*y", "r", "θ"],
         "sin θ is the y-coordinate on the unit circle."),
        ("cos θ corresponds to which coordinate on the unit circle?", ["y", "*x", "r", "θ"],
         "cos θ is the x-coordinate."),
        ("tan θ is defined as:", ["cos θ / sin θ", "*sin θ / cos θ", "1 / sin θ", "1 / cos θ"],
         "tan θ = sin θ / cos θ."),
        ("The range of sin θ is:", ["(−∞, ∞)", "[0, 1]", "*[−1, 1]", "[−π, π]"],
         "sin θ outputs values between −1 and 1 inclusive."),
        ("tan θ is undefined when:", ["sin θ = 0", "*cos θ = 0", "tan θ = 0", "sin θ = 1"],
         "tan θ = sin θ / cos θ is undefined when cos θ = 0."),
        ("At θ = π/2, tan θ is:", ["0", "1", "*undefined", "−1"],
         "cos(π/2) = 0, so tan(π/2) is undefined."),
        ("The domain of sin θ and cos θ is:", ["[−1, 1]", "[0, 2π]", "*All real numbers", "[−π, π]"],
         "Both sin and cos are defined for all real numbers."),
        ("If the point on the unit circle is (−0.6, 0.8), cos θ =", ["0.8", "*−0.6", "0.6", "−0.8"],
         "cos θ = x-coordinate = −0.6."),
        ("If the point on the unit circle is (−0.6, 0.8), sin θ =", ["−0.6", "*0.8", "0.6", "−0.8"],
         "sin θ = y-coordinate = 0.8."),
        ("If the point on the unit circle is (−0.6, 0.8), tan θ =", ["−0.6/0.8", "*0.8/(−0.6) = −4/3", "−0.8/0.6", "0.6/0.8"],
         "tan θ = sin θ / cos θ = 0.8/(−0.6) = −4/3."),
        ("Which quadrants have sin θ > 0?", ["I and IV", "*I and II", "I and III", "II and IV"],
         "sin θ (y-coordinate) is positive when y > 0: Q I and Q II."),
        ("Which quadrants have cos θ < 0?", ["I and II", "III and IV", "*II and III", "I and IV"],
         "cos θ (x-coordinate) is negative in Q II and Q III."),
        ("sin(−θ) =", ["sin θ", "*−sin θ", "cos θ", "−cos θ"],
         "Sine is an odd function: sin(−θ) = −sin θ."),
        ("cos(−θ) =", ["−cos θ", "sin θ", "*cos θ", "−sin θ"],
         "Cosine is an even function: cos(−θ) = cos θ."),
        ("The maximum value of sin θ is:", ["2", "π", "*1", "∞"],
         "The maximum y-coordinate on the unit circle is 1."),
        ("sin θ = 0 at θ =", ["π/2", "*0, π, 2π, …", "π/4", "π/6"],
         "sin θ = 0 when the point crosses the x-axis: θ = nπ."),
        ("cos θ = 0 at θ =", ["0, π, 2π", "*π/2, 3π/2, …", "π/4", "π/3"],
         "cos θ = 0 at θ = π/2 + nπ."),
        ("tan θ = 0 when:", ["cos θ = 0", "*sin θ = 0 (and cos θ ≠ 0)", "Both sin and cos are 0", "Never"],
         "tan θ = sin θ/cos θ = 0 when sin θ = 0."),
        ("For the general point (x, y) on a circle radius r, sin θ =", ["x/r", "*y/r", "y/x", "r/y"],
         "sin θ = y/r, which reduces to y when r = 1."),
        ("Why does the unit circle definition extend SOH-CAH-TOA?", ["It doesn't", "*It works for all angles (not just acute) by using coordinates instead of triangle sides", "It uses degrees instead of radians", "It replaces the tangent function"],
         "The unit circle assigns sin and cos to any angle via coordinates, not limited to acute angles in triangles."),
    ]
)
lessons[k] = v

# ── 2.2 ──
k, v = build_lesson(2, 2, "Reciprocal Functions (csc, sec, cot)",
    "<h3>Reciprocal Trigonometric Functions</h3>"
    "<p>Three additional trig functions are defined as reciprocals of the primary three:</p>"
    "<ul><li><b>csc θ = 1/sin θ</b> (cosecant) — undefined when sin θ = 0.</li>"
    "<li><b>sec θ = 1/cos θ</b> (secant) — undefined when cos θ = 0.</li>"
    "<li><b>cot θ = 1/tan θ = cos θ/sin θ</b> (cotangent) — undefined when sin θ = 0.</li></ul>"
    "<h4>Domains</h4>"
    "<ul><li>csc θ: all reals except nπ.</li>"
    "<li>sec θ: all reals except π/2 + nπ.</li>"
    "<li>cot θ: all reals except nπ.</li></ul>"
    "<h4>Ranges</h4>"
    "<ul><li>csc θ and sec θ: (−∞, −1] ∪ [1, ∞).</li>"
    "<li>cot θ: (−∞, ∞).</li></ul>",
    [
        ("Cosecant (csc)", "csc θ = 1/sin θ; undefined when sin θ = 0."),
        ("Secant (sec)", "sec θ = 1/cos θ; undefined when cos θ = 0."),
        ("Cotangent (cot)", "cot θ = cos θ/sin θ = 1/tan θ; undefined when sin θ = 0."),
        ("Range of csc and sec", "(−∞, −1] ∪ [1, ∞); they never have values between −1 and 1."),
        ("Domain of cot", "All real numbers except nπ (where sin θ = 0)."),
    ],
    [
        ("csc θ is defined as:", ["*1/sin θ", "1/cos θ", "sin θ/cos θ", "cos θ/sin θ"],
         "Cosecant is the reciprocal of sine."),
        ("sec θ is defined as:", ["1/sin θ", "*1/cos θ", "cos θ/sin θ", "sin θ/cos θ"],
         "Secant is the reciprocal of cosine."),
        ("cot θ is defined as:", ["sin θ/cos θ", "1/cos θ", "1/sin θ", "*cos θ/sin θ"],
         "Cotangent = cos θ/sin θ = 1/tan θ."),
        ("csc θ is undefined when:", ["cos θ = 0", "*sin θ = 0", "tan θ = 0", "cot θ = 0"],
         "csc θ = 1/sin θ, so it's undefined when sin θ = 0."),
        ("If sin θ = 1/2, then csc θ =", ["1/2", "*2", "√3", "√2"],
         "csc θ = 1/sin θ = 1/(1/2) = 2."),
        ("If cos θ = √3/2, then sec θ =", ["√3/2", "*2/√3 = 2√3/3", "√3", "2"],
         "sec θ = 1/cos θ = 1/(√3/2) = 2/√3 = 2√3/3."),
        ("sec θ is undefined at:", ["θ = 0", "θ = π", "*θ = π/2", "θ = 2π"],
         "sec θ = 1/cos θ; cos(π/2) = 0, so sec(π/2) is undefined."),
        ("The range of csc θ is:", ["[−1, 1]", "(−∞, ∞)", "*(-∞, −1] ∪ [1, ∞)", "[0, ∞)"],
         "Since |sin θ| ≤ 1, |csc θ| ≥ 1."),
        ("cot 45° =", ["√3", "0", "*1", "undefined"],
         "cot 45° = cos 45°/sin 45° = 1."),
        ("csc 90° =", ["0", "undefined", "*1", "−1"],
         "csc 90° = 1/sin 90° = 1/1 = 1."),
        ("sec 0° =", ["0", "undefined", "*1", "−1"],
         "sec 0° = 1/cos 0° = 1/1 = 1."),
        ("cot 0° is:", ["0", "1", "*undefined", "−1"],
         "cot 0° = cos 0°/sin 0° = 1/0 = undefined."),
        ("If tan θ = 3, then cot θ =", ["3", "*1/3", "−3", "−1/3"],
         "cot θ = 1/tan θ = 1/3."),
        ("csc 30° =", ["1/2", "*2", "√2", "√3"],
         "csc 30° = 1/sin 30° = 1/(1/2) = 2."),
        ("sec 60° =", ["1/2", "√3/2", "*2", "√3"],
         "sec 60° = 1/cos 60° = 1/(1/2) = 2."),
        ("cot 90° =", ["undefined", "1", "*0", "−1"],
         "cot 90° = cos 90°/sin 90° = 0/1 = 0."),
        ("Which reciprocal function has the same domain restrictions as tan?", ["csc", "*sec", "cot", "None"],
         "Both tangent and secant are undefined when cos θ = 0: at π/2 + nπ."),
        ("csc and sec can never take values between:", ["0 and 1", "*−1 and 1", "−2 and 2", "0 and 2"],
         "The reciprocal of a number with |value| ≤ 1 must have |value| ≥ 1."),
        ("If csc θ = −2, then sin θ =", ["2", "*−1/2", "−2", "1/2"],
         "sin θ = 1/csc θ = 1/(−2) = −1/2."),
        ("cot θ can be rewritten as:", ["*cos θ / sin θ", "sin θ / cos θ", "1 / cos θ", "1 / sin θ"],
         "cot θ = 1/tan θ = cos θ/sin θ."),
    ]
)
lessons[k] = v

# ── 2.3 ──
k, v = build_lesson(2, 3, "Graphs of Sine & Cosine",
    "<h3>Graphs of Sine &amp; Cosine</h3>"
    "<h4>The Sine Graph: y = sin x</h4>"
    "<ul><li>Starts at (0, 0), rises to 1 at π/2, returns to 0 at π, drops to −1 at 3π/2, returns to 0 at 2π.</li>"
    "<li><b>Period:</b> 2π (one full cycle). <b>Amplitude:</b> 1. <b>Midline:</b> y = 0.</li></ul>"
    "<h4>The Cosine Graph: y = cos x</h4>"
    "<ul><li>Starts at (0, 1), drops to 0 at π/2, reaches −1 at π, returns to 0 at 3π/2, back to 1 at 2π.</li>"
    "<li>Same period, amplitude, and midline as sine.</li></ul>"
    "<p>cos x is a <b>phase-shifted sine</b>: cos x = sin(x + π/2).</p>"
    "<p>Both graphs are smooth, continuous waves called <b>sinusoidal curves</b>.</p>",
    [
        ("Period", "The length of one full cycle; for y = sin x and y = cos x, period = 2π."),
        ("Amplitude", "Half the distance between max and min values; for basic sin/cos, amplitude = 1."),
        ("Midline", "The horizontal line halfway between max and min; for basic sin/cos, midline = y = 0."),
        ("Sinusoidal", "Having the shape of a sine or cosine wave."),
        ("Phase Shift", "A horizontal translation; cos x = sin(x + π/2) is sine shifted left by π/2."),
    ],
    [
        ("The period of y = sin x is:", ["π", "*2π", "π/2", "4π"],
         "One full cycle of sine takes 2π radians."),
        ("The amplitude of y = cos x is:", ["2", "0", "*1", "π"],
         "The amplitude is 1 — the graph oscillates between −1 and 1."),
        ("sin 0 =", ["1", "*0", "−1", "0.5"],
         "The sine graph starts at (0, 0)."),
        ("cos 0 =", ["0", "*1", "−1", "0.5"],
         "The cosine graph starts at (0, 1)."),
        ("At what x value does sin x first reach its maximum of 1?", ["0", "π", "*π/2", "2π"],
         "sin(π/2) = 1."),
        ("At what x value does cos x first reach its minimum of −1?", ["π/2", "*π", "3π/2", "2π"],
         "cos(π) = −1."),
        ("The midline of y = sin x is:", ["y = 1", "y = −1", "*y = 0", "y = π"],
         "The average of max (1) and min (−1) is 0."),
        ("cos x = sin( ? )", ["x + π", "x − π/2", "*x + π/2", "x − π"],
         "cos x = sin(x + π/2) — cosine is a left-shifted sine."),
        ("sin x and cos x are both:", ["Periodic with period π", "*Periodic with period 2π", "Never equal", "Linear"],
         "Both have period 2π."),
        ("At x = π, sin x =", ["1", "*0", "−1", "0.5"],
         "sin(π) = 0."),
        ("At x = 3π/2, cos x =", ["1", "−1", "*0", "0.5"],
         "cos(3π/2) = 0."),
        ("At x = 3π/2, sin x =", ["1", "0", "*−1", "0.5"],
         "sin(3π/2) = −1."),
        ("How many complete cycles does y = sin x make from 0 to 4π?", ["1", "*2", "4", "3"],
         "Period = 2π, so 4π/2π = 2 cycles."),
        ("The sine function is:", ["Even", "*Odd", "Neither", "Both"],
         "sin(−x) = −sin x, so sine is odd."),
        ("The cosine function is:", ["*Even", "Odd", "Neither", "Both"],
         "cos(−x) = cos x, so cosine is even."),
        ("sin x = cos x at x =", ["0", "π/2", "*π/4", "π"],
         "At π/4: sin(π/4) = cos(π/4) = √2/2."),
        ("A sinusoidal curve is:", ["A straight line", "A parabola", "*A smooth wave shaped like sine or cosine", "An exponential"],
         "Sinusoidal means shaped like a sine/cosine wave."),
        ("Where is sin x increasing?", ["(π/2, 3π/2)", "*(−π/2, π/2)", "(0, π)", "(π, 2π)"],
         "sin x increases from its minimum to its maximum: from −π/2 to π/2 (and repeating)."),
        ("The zero crossings of y = cos x occur at:", ["nπ", "*π/2 + nπ", "nπ/2", "2nπ"],
         "cos x = 0 at x = π/2 + nπ."),
        ("If two waves have the same period and amplitude but different phase shifts, they are:", ["Identical", "*Sinusoidal with different starting points", "Perpendicular", "Inverse"],
         "Same shape, just shifted horizontally."),
    ]
)
lessons[k] = v

# ── 2.4 ──
k, v = build_lesson(2, 4, "Graphs of Tangent, Cotangent, Secant, Cosecant",
    "<h3>Graphs of the Other Four Trig Functions</h3>"
    "<h4>y = tan x</h4>"
    "<ul><li>Period = π. Vertical asymptotes at x = π/2 + nπ (where cos x = 0).</li>"
    "<li>Passes through the origin. Increasing throughout each period. Range = (−∞, ∞).</li></ul>"
    "<h4>y = cot x</h4>"
    "<ul><li>Period = π. Vertical asymptotes at x = nπ (where sin x = 0).</li>"
    "<li>Decreasing throughout each period.</li></ul>"
    "<h4>y = sec x</h4>"
    "<ul><li>Period = 2π. Vertical asymptotes where cos x = 0. Range: (−∞, −1] ∪ [1, ∞).</li>"
    "<li>U-shaped curves between asymptotes: above 1 or below −1.</li></ul>"
    "<h4>y = csc x</h4>"
    "<ul><li>Period = 2π. Vertical asymptotes where sin x = 0. Same range as sec.</li></ul>",
    [
        ("Period of tan/cot", "π — tangent and cotangent repeat every π radians."),
        ("Asymptotes of tan x", "Vertical asymptotes at x = π/2 + nπ (where cos x = 0)."),
        ("Asymptotes of csc x", "Vertical asymptotes at x = nπ (where sin x = 0)."),
        ("Range of sec x", "(−∞, −1] ∪ [1, ∞); no values between −1 and 1."),
        ("Tangent Graph Shape", "An increasing S-curve between asymptotes, passing through the origin in each period."),
    ],
    [
        ("The period of y = tan x is:", ["2π", "*π", "π/2", "4π"],
         "Tangent repeats every π radians."),
        ("Vertical asymptotes of tan x occur at:", ["x = nπ", "*x = π/2 + nπ", "x = 2nπ", "x = nπ/4"],
         "tan x is undefined where cos x = 0: x = π/2 + nπ."),
        ("The period of y = cot x is:", ["2π", "*π", "π/2", "4π"],
         "Cotangent also has period π."),
        ("Vertical asymptotes of cot x occur at:", ["x = π/2 + nπ", "*x = nπ", "x = 2nπ", "x = nπ/4"],
         "cot x is undefined where sin x = 0: x = nπ."),
        ("The range of y = tan x is:", ["[−1, 1]", "*(-∞, ∞)", "(−∞, −1] ∪ [1, ∞)", "[0, ∞)"],
         "Tangent can take any real value."),
        ("The period of y = sec x is:", ["π", "*2π", "π/2", "4π"],
         "Secant has the same period as cosine: 2π."),
        ("The period of y = csc x is:", ["π", "*2π", "π/2", "4π"],
         "Cosecant has the same period as sine: 2π."),
        ("y = sec x has vertical asymptotes where:", ["sin x = 0", "*cos x = 0", "tan x = 0", "cot x = 0"],
         "sec x = 1/cos x is undefined when cos x = 0."),
        ("The range of y = csc x is:", ["[−1, 1]", "(−∞, ∞)", "*(-∞, −1] ∪ [1, ∞)", "[0, ∞)"],
         "|csc x| ≥ 1 always."),
        ("tan 0 =", ["undefined", "1", "*0", "−1"],
         "tan 0 = sin 0/cos 0 = 0/1 = 0."),
        ("cot(π/4) =", ["0", "*1", "undefined", "√3"],
         "cot 45° = cos 45°/sin 45° = 1."),
        ("sec 0 =", ["0", "undefined", "*1", "−1"],
         "sec 0 = 1/cos 0 = 1."),
        ("csc(π/6) =", ["√3", "1/2", "*2", "√2"],
         "csc 30° = 1/sin 30° = 1/(1/2) = 2."),
        ("Is the tangent function increasing or decreasing in each period?", ["Decreasing", "*Increasing", "Both", "Neither"],
         "Tangent is strictly increasing between its vertical asymptotes."),
        ("Is the cotangent function increasing or decreasing?", ["Increasing", "*Decreasing", "Both", "Neither"],
         "Cotangent is strictly decreasing between asymptotes."),
        ("The graph of sec x consists of:", ["A single wave", "*U-shaped curves opening up and down between asymptotes", "Straight line segments", "Circles"],
         "Each piece of sec x is a U-shape (parabola-like curve) between consecutive asymptotes."),
        ("Between asymptotes, csc x looks like:", ["A straight line", "A wave", "*Inverted U or upright U shapes", "A circle"],
         "csc x forms U-shaped branches between its asymptotes."),
        ("tan(π/4) =", ["0", "−1", "*1", "undefined"],
         "tan 45° = 1."),
        ("How does the graph of cot x relate to tan x?", ["They are identical", "*cot x is a reflected and shifted version of tan x", "They have different periods", "They have the same asymptotes"],
         "cot x = cos x/sin x can be seen as a reflected, shifted tangent with the same period π."),
        ("Which function has x-intercepts at x = nπ?", ["cos x", "csc x", "cot x", "*tan x (and sin x)"],
         "tan x = 0 where sin x = 0, i.e., at x = nπ."),
    ]
)
lessons[k] = v

# ── 2.5 ──
k, v = build_lesson(2, 5, "Transformations of Trig Graphs (amplitude, period, phase shift)",
    "<h3>Transformations of Trig Graphs</h3>"
    "<p>The general sinusoidal form is <b>y = A sin(Bx − C) + D</b> (or cosine).</p>"
    "<h4>Parameters</h4>"
    "<ul><li><b>A (amplitude):</b> |A| = vertical stretch/compression. If A &lt; 0, the graph is reflected over the x-axis.</li>"
    "<li><b>B (period change):</b> Period = 2π/|B|. Larger |B| → shorter period.</li>"
    "<li><b>C/B (phase shift):</b> Horizontal shift = C/B to the right.</li>"
    "<li><b>D (vertical shift):</b> The midline moves to y = D.</li></ul>"
    "<p>Example: y = 3 sin(2x − π) + 1 has amplitude 3, period π, phase shift π/2 right, midline y = 1.</p>",
    [
        ("Amplitude", "|A| in y = A sin(Bx − C) + D; the maximum displacement from the midline."),
        ("Period", "2π/|B|; the horizontal length of one complete cycle."),
        ("Phase Shift", "C/B; the horizontal shift of the graph (right if positive)."),
        ("Vertical Shift (D)", "Moves the midline from y = 0 to y = D."),
        ("Reflection", "If A < 0, the graph is flipped over the x-axis."),
    ],
    [
        ("In y = A sin(Bx − C) + D, amplitude is:", ["|B|", "D", "*|A|", "C/B"],
         "Amplitude = |A|."),
        ("The period of y = sin(3x) is:", ["3π", "6π", "*2π/3", "π/3"],
         "Period = 2π/|B| = 2π/3."),
        ("The phase shift of y = sin(x − π/4) is:", ["π/4 left", "*π/4 right", "π/2 right", "π/4 up"],
         "Phase shift = C/B = (π/4)/1 = π/4 to the right."),
        ("y = 2 cos x has amplitude:", ["1", "*2", "4", "1/2"],
         "|A| = 2."),
        ("The midline of y = sin x + 3 is:", ["y = 0", "y = 1", "*y = 3", "y = −3"],
         "D = 3, so the midline is y = 3."),
        ("y = −sin x is a __ of y = sin x.", ["Vertical shift", "*Reflection over the x-axis", "Phase shift", "Period change"],
         "A = −1 reflects the curve over the x-axis."),
        ("The period of y = cos(πx) is:", ["π", "*2", "2π", "1"],
         "Period = 2π/|B| = 2π/π = 2."),
        ("For y = 3 sin(2x − π) + 1, the phase shift is:", ["π", "π/4", "*π/2 right", "1"],
         "Phase shift = C/B = π/2 to the right."),
        ("For y = 3 sin(2x − π) + 1, the amplitude is:", ["1", "2", "*3", "π"],
         "Amplitude = |A| = 3."),
        ("For y = 3 sin(2x − π) + 1, the period is:", ["2π", "*π", "3", "2"],
         "Period = 2π/2 = π."),
        ("For y = 3 sin(2x − π) + 1, the midline is:", ["*y = 1", "y = 3", "y = 0", "y = π"],
         "D = 1, so midline is y = 1."),
        ("Increasing |B| in y = sin(Bx) causes the period to:", ["Increase", "*Decrease", "Stay the same", "Double"],
         "Period = 2π/|B|; larger |B| → smaller period."),
        ("y = 4 cos(x/2) has period:", ["π", "2π", "*4π", "π/2"],
         "Period = 2π/(1/2) = 4π."),
        ("y = sin(x) + 5 shifts the graph:", ["Down 5", "*Up 5", "Left 5", "Right 5"],
         "D = 5 raises the midline to y = 5."),
        ("y = cos(x + π/3) has phase shift:", ["π/3 right", "*π/3 left", "π/6 left", "π/6 right"],
         "y = cos(x − (−π/3)), so shift is π/3 to the left."),
        ("The maximum value of y = 2 sin x + 3 is:", ["2", "3", "*5", "1"],
         "Max = A + D = 2 + 3 = 5."),
        ("The minimum value of y = 2 sin x + 3 is:", ["−2", "*1", "3", "0"],
         "Min = −A + D = −2 + 3 = 1."),
        ("y = −3 cos(2x) is reflected because:", ["B < 0", "*A < 0", "D < 0", "The period is negative"],
         "A = −3 < 0, so the graph is reflected over the x-axis."),
        ("The range of y = 4 sin x − 2 is:", ["[−4, 4]", "[−2, 2]", "*[−6, 2]", "[−4, 2]"],
         "Range: [D − |A|, D + |A|] = [−2 − 4, −2 + 4] = [−6, 2]."),
        ("To find A from a graph, compute:", ["Max + Min", "(Max − Min)/2", "*|Max − Min| / 2 = |A|", "Max × Min"],
         "Amplitude = (Max − Min) / 2."),
    ]
)
lessons[k] = v

# ── 2.6 ──
k, v = build_lesson(2, 6, "Symmetry & Periodicity",
    "<h3>Symmetry &amp; Periodicity</h3>"
    "<h4>Even and Odd Functions</h4>"
    "<ul><li><b>Cosine is even:</b> cos(−θ) = cos θ. Graph is symmetric about the y-axis.</li>"
    "<li><b>Sine is odd:</b> sin(−θ) = −sin θ. Graph is symmetric about the origin.</li>"
    "<li><b>Tangent is odd:</b> tan(−θ) = −tan θ.</li></ul>"
    "<h4>Periodicity</h4>"
    "<ul><li>sin and cos have period 2π: f(θ + 2π) = f(θ).</li>"
    "<li>tan and cot have period π: f(θ + π) = f(θ).</li>"
    "<li>Periodicity means you only need one cycle to know all values.</li></ul>"
    "<p>Symmetry and periodicity together reduce calculations: use reference angles and sign rules.</p>",
    [
        ("Even Function", "f(−x) = f(x); symmetric about the y-axis. Cosine is even."),
        ("Odd Function", "f(−x) = −f(x); symmetric about the origin. Sine and tangent are odd."),
        ("Periodicity", "The property that a function repeats at regular intervals: f(x + P) = f(x)."),
        ("Period of sin/cos", "2π — the smallest interval after which the function repeats."),
        ("Period of tan/cot", "π — tangent and cotangent repeat every π radians."),
    ],
    [
        ("cos(−θ) =", ["−cos θ", "sin θ", "*cos θ", "−sin θ"],
         "Cosine is even: cos(−θ) = cos θ."),
        ("sin(−θ) =", ["sin θ", "*−sin θ", "cos θ", "−cos θ"],
         "Sine is odd: sin(−θ) = −sin θ."),
        ("tan(−θ) =", ["tan θ", "cot θ", "*−tan θ", "−cot θ"],
         "Tangent is odd: tan(−θ) = −tan θ."),
        ("Which function is even?", ["sin", "tan", "*cos", "csc"],
         "Cosine is even."),
        ("An even function has symmetry about:", ["The origin", "*The y-axis", "The x-axis", "No axis"],
         "Even: f(−x) = f(x) → y-axis symmetry."),
        ("An odd function has symmetry about:", ["The y-axis", "The x-axis", "*The origin", "No axis"],
         "Odd: f(−x) = −f(x) → origin symmetry."),
        ("sin(θ + 2π) =", ["−sin θ", "0", "*sin θ", "cos θ"],
         "Sine is periodic with period 2π."),
        ("tan(θ + π) =", ["−tan θ", "0", "*tan θ", "cot θ"],
         "Tangent has period π."),
        ("The smallest positive period of cos x is:", ["π", "π/2", "*2π", "4π"],
         "Cosine repeats every 2π."),
        ("Is csc an even or odd function?", ["Even", "*Odd", "Neither", "Both"],
         "csc(−θ) = 1/sin(−θ) = −1/sin θ = −csc θ. Odd."),
        ("Is sec even or odd?", ["*Even", "Odd", "Neither", "Both"],
         "sec(−θ) = 1/cos(−θ) = 1/cos θ = sec θ. Even."),
        ("cos(θ + 2π) =", ["−cos θ", "sin θ", "*cos θ", "0"],
         "Cosine has period 2π."),
        ("sin(−π/3) =", ["√3/2", "*−√3/2", "1/2", "−1/2"],
         "sin(−π/3) = −sin(π/3) = −√3/2."),
        ("cos(−π/4) =", ["−√2/2", "*√2/2", "1/2", "0"],
         "cos(−π/4) = cos(π/4) = √2/2."),
        ("tan(θ + π) = tan θ shows tan has period:", ["2π", "π/2", "*π", "4π"],
         "Repeat interval of π means period = π."),
        ("If f(x) = sin x + cos x, is f even, odd, or neither?", ["Even", "Odd", "*Neither", "Both"],
         "f(−x) = −sin x + cos x ≠ f(x) and ≠ −f(x), so neither."),
        ("cot(−θ) =", ["cot θ", "*−cot θ", "tan θ", "−tan θ"],
         "cot is odd: cot(−θ) = −cot θ."),
        ("Period of cot x is:", ["2π", "*π", "π/2", "4π"],
         "Cotangent has period π."),
        ("Knowing one full period of a trig function means you know:", ["Only that period", "Half the function", "*All values of the function (by repeating)", "Nothing about other periods"],
         "Periodicity means the same pattern repeats forever."),
        ("sin(5π/6) can be evaluated using the reference angle:", ["π/6 in Q I", "*π/6 in Q II (sin is positive)", "π/3 in Q II", "5π/6 directly"],
         "ref = π − 5π/6 = π/6. Q II → sin is positive: sin(5π/6) = sin(π/6) = 1/2."),
    ]
)
lessons[k] = v

# ── 2.7 ──
k, v = build_lesson(2, 7, "Applications in Sound Waves",
    "<h3>Applications in Sound Waves</h3>"
    "<p>Sound waves are modeled by sinusoidal functions because they involve periodic oscillations of air pressure.</p>"
    "<h4>Modeling Sound</h4>"
    "<ul><li>A basic sound wave: <b>y = A sin(2πft)</b> where A = amplitude (loudness), f = frequency (pitch), t = time.</li>"
    "<li><b>Frequency</b> is measured in hertz (Hz): cycles per second. Higher frequency → higher pitch.</li>"
    "<li><b>Period</b> = 1/f: time for one complete cycle.</li></ul>"
    "<h4>Musical Concepts</h4>"
    "<ul><li>Standard tuning: A4 = 440 Hz.</li>"
    "<li>An octave doubles the frequency: A5 = 880 Hz.</li>"
    "<li>Overlapping sound waves create <b>beats</b> — periodic fluctuations in loudness.</li></ul>"
    "<p>Understanding sinusoidal functions helps in acoustics, audio engineering, and music theory.</p>",
    [
        ("Frequency (f)", "Number of complete cycles per second; measured in hertz (Hz)."),
        ("Amplitude (sound)", "The maximum pressure variation; corresponds to loudness or volume."),
        ("Period (sound)", "T = 1/f; the time for one complete vibration cycle."),
        ("Hertz (Hz)", "Unit of frequency: 1 Hz = 1 cycle per second."),
        ("Beats", "Periodic loudness fluctuations caused by two overlapping waves of slightly different frequencies."),
    ],
    [
        ("A sound wave can be modeled by:", ["A linear function", "An exponential function", "*A sinusoidal function", "A polynomial"],
         "Sound involves periodic air pressure oscillations → sinusoidal model."),
        ("In y = A sin(2πft), A represents:", ["Frequency", "Period", "*Amplitude (loudness)", "Pitch"],
         "A is the amplitude."),
        ("In y = A sin(2πft), f represents:", ["Amplitude", "*Frequency", "Period", "Phase shift"],
         "f is the frequency in Hz."),
        ("Frequency is measured in:", ["Decibels", "Seconds", "*Hertz (Hz)", "Meters"],
         "Hz = cycles per second."),
        ("The period of a 440 Hz sound wave is:", ["440 s", "*1/440 ≈ 0.00227 s", "440π s", "2π/440 s"],
         "Period = 1/f = 1/440 s."),
        ("Higher frequency means:", ["Louder sound", "*Higher pitch", "Longer period", "Larger amplitude"],
         "Frequency determines pitch: higher frequency → higher pitch."),
        ("Greater amplitude means:", ["Higher pitch", "*Louder sound", "Shorter period", "Higher frequency"],
         "Amplitude corresponds to loudness."),
        ("A4 = 440 Hz. What is A5?", ["220 Hz", "*880 Hz", "660 Hz", "440 Hz"],
         "One octave up doubles the frequency: 880 Hz."),
        ("A4 = 440 Hz. What is A3?", ["*220 Hz", "880 Hz", "330 Hz", "110 Hz"],
         "One octave down halves the frequency: 220 Hz."),
        ("Period and frequency are related by:", ["T = f", "T = 2πf", "*T = 1/f", "T = f²"],
         "Period is the reciprocal of frequency."),
        ("Beats occur when two waves have:", ["The same frequency", "*Slightly different frequencies", "Very different frequencies", "The same amplitude"],
         "Beats come from interference of two close frequencies."),
        ("Beat frequency =", ["f₁ + f₂", "f₁ × f₂", "*|f₁ − f₂|", "f₁ / f₂"],
         "Beat frequency equals the absolute difference of the two frequencies."),
        ("Two tuning forks vibrate at 440 Hz and 442 Hz. The beat frequency is:", ["882 Hz", "440 Hz", "*2 Hz", "442 Hz"],
         "|442 − 440| = 2 Hz."),
        ("A guitar string vibrating at 330 Hz produces a:", ["Noise", "Straight line on a graph", "*Sinusoidal sound wave", "Random wave"],
         "The vibration creates a periodic, sinusoidal pressure wave."),
        ("If a sound has period 0.005 s, its frequency is:", ["0.005 Hz", "5 Hz", "*200 Hz", "2000 Hz"],
         "f = 1/T = 1/0.005 = 200 Hz."),
        ("Which changes if you turn up the volume of a speaker?", ["Frequency", "Period", "*Amplitude", "Wavelength"],
         "Volume corresponds to amplitude."),
        ("Middle C has frequency ≈ 262 Hz. Its period is approximately:", ["262 s", "*0.00382 s", "0.262 s", "3.82 s"],
         "T = 1/262 ≈ 0.00382 s."),
        ("In audio engineering, sinusoidal analysis is used for:", ["Color mixing", "*Analyzing and synthesizing sounds", "Chemical reactions", "Measuring distances"],
         "Sound engineering relies on sinusoidal models for analysis and synthesis."),
        ("A pure tone is modeled by which type of function?", ["Cosine only", "Square wave", "*A single sine (or cosine) function", "A random function"],
         "A pure tone is a single-frequency sinusoidal wave."),
        ("Complex sounds can be decomposed into sine waves using:", ["Integration", "Differentiation", "*Fourier analysis", "Factoring"],
         "Fourier analysis breaks complex waveforms into sums of sine and cosine components."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

data.update(lessons)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Trigonometry Unit 2: wrote {len(lessons)} lessons")
