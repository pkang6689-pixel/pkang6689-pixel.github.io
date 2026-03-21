#!/usr/bin/env python3
"""Expand Algebra 1 Units 9-12 (15 lessons) from 7 to 20 quiz questions each."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "algebra_1_lessons.json")

def add_qs(data, key, new_questions):
    lesson = data[key]
    existing = lesson.get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(new_questions):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        existing.append({"question_number": start + i, "question_text": qt, "attempted": 2,
                         "data_i18n": None, "options": options, "explanation": exp})
    lesson["quiz_questions"] = existing

with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# ── U9 L9.1: Simplifying Rational Expressions ──
add_qs(data, "u9_l9.1", [
    ("Simplify: (x^2 - 9)/(x + 3)", ["x + 3", "x + 9", "*x - 3", "x^2 - 3"], "Factor numerator: (x+3)(x-3)/(x+3) = x-3."),
    ("Simplify: (2x^2 + 6x)/(4x)", ["(x+3)/2","*x+3)/2 ... wait let me fix: (2x(x+3))/(4x) = (x+3)/2","(x+3)/4","2x+6"], "Nope, let me redo."),
])
# Actually let me do this properly with a cleaner approach

data2 = data  # reset

# I'll rebuild this properly
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

def add_questions(key, questions):
    lesson = data[key]
    existing = lesson.get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(questions):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        existing.append({"question_number": start + i, "question_text": qt, "attempted": 2,
                         "data_i18n": None, "options": options, "explanation": exp})
    lesson["quiz_questions"] = existing

# ── U9 L9.1: Simplifying Rational Expressions ──
add_questions("u9_l9.1", [
    ("Simplify: (x^2 - 9)/(x + 3)", ["x + 3", "x + 9", "*x - 3", "x^2 - 3"], "Factor: (x+3)(x-3)/(x+3) = x - 3."),
    ("Simplify: (2x^2 + 6x)/(4x)", ["(x + 3)/4", "2x + 6", "*( x + 3)/2", "x/2"], "Factor: 2x(x+3)/(4x) = (x+3)/2."),
    ("What values must be excluded from (5)/(x - 2)?", ["x = 5", "x = 0", "*x = 2", "x = -2"], "Denominator cannot be zero."),
    ("Simplify: (x^2 - 4x)/(x^2 - 16)", ["x/(x+4)", "x/(x-4)", "*x/(x + 4)", "(x-4)/(x+4)"], "x(x-4)/((x-4)(x+4)) = x/(x+4)."),
    ("Simplify: (3x + 12)/(x^2 + 4x)", ["3/x^2", "3x", "*3/x", "(3+12)/(x+4)"], "3(x+4)/(x(x+4)) = 3/x."),
    ("Which is NOT a rational expression?", ["x/5", "(x+1)/(x-1)", "3/(2x)", "*sqrt(x)/2"], "Rational expressions have polynomial numerator and denominator."),
    ("Simplify: (x^2 + 5x + 6)/(x^2 + 3x + 2)", ["(x+3)/(x+2)", "(x+2)/(x+1)", "*(x + 3)/(x + 1)", "(x+6)/(x+2)"], "Factor: (x+2)(x+3)/((x+1)(x+2)) = (x+3)/(x+1)."),
    ("The domain of 7/(x^2 - 1) excludes:", ["x = 0", "*x = 1 and x = -1", "x = 7", "All negative numbers"], "x^2 - 1 = 0 when x = 1 or x = -1."),
    ("Simplify: (6x^3)/(2x)", ["6x^3", "6x^2", "*3x^2", "3x^3"], "6x^3/(2x) = 3x^2."),
    ("Simplify: (x^2 - x - 6)/(x^2 - 9)", ["(x+2)/(x-3)", "(x-3)/(x+3)", "*(x + 2)/(x + 3)", "(x-6)/(x-9)"], "Factor: (x-3)(x+2)/((x-3)(x+3)) = (x+2)/(x+3)."),
    ("Simplify: (-x - 3)/(x + 3)", ["1", "0", "*-1", "x"], "-(x+3)/(x+3) = -1."),
    ("For (x+1)/(x^2-1), the simplified form is:", ["x+1", "1/(x+1)", "*1/(x - 1)", "x-1"], "(x+1)/((x+1)(x-1)) = 1/(x-1)."),
    ("Simplify: (4x^2 - 1)/(2x + 1)", ["4x - 1", "2x + 1", "*2x - 1", "4x^2"], "(2x+1)(2x-1)/(2x+1) = 2x - 1."),
])

# ── U9 L9.2: Multiplying & Dividing Rational Expressions ──
add_questions("u9_l9.2", [
    ("Multiply: (x/3) * (9/x^2)", ["9/x", "x/3", "*3/x", "3x"], "(x * 9)/(3 * x^2) = 9/(3x) = 3/x."),
    ("Divide: (x^2/4) / (x/8)", ["x/32", "x^2/32", "*2x", "x/2"], "(x^2/4) * (8/x) = 8x^2/(4x) = 2x."),
    ("Multiply: ((x+2)/(x-1)) * ((x-1)/(x+5))", ["(x-1)/(x+5)", "1", "*(x + 2)/(x + 5)", "(x+2)(x-1)"], "Cancel (x-1): (x+2)/(x+5)."),
    ("To divide rational expressions, you:", ["Cross multiply", "Add denominators", "*Multiply by the reciprocal of the divisor", "Subtract numerators"], "Division = multiply by reciprocal."),
    ("Multiply: (2x/(x+3)) * ((x+3)/(4))", ["2x/4", "8x", "*x/2", "2x(x+3)/4"], "Cancel (x+3): 2x/4 = x/2."),
    ("Divide: (5/(x-2)) / (10/(x-2))", ["50/(x-2)^2", "2", "*1/2", "10/5"], "(5/(x-2)) * ((x-2)/10) = 5/10 = 1/2."),
    ("Multiply: ((x^2-4)/(x)) * ((x^2)/(x+2))", ["x^2-4", "x(x-2)", "*x(x - 2)", "(x^2-4)x"], "(x+2)(x-2)/x * x^2/(x+2) = x(x-2)."),
    ("Before multiplying rational expressions, you should first:", ["Add them", "*Factor all numerators and denominators to find common factors to cancel", "Find LCD", "Cross multiply"], "Factor first, then cancel."),
    ("Divide: ((x^2-9)/(x+1)) / ((x+3)/1)", ["x^2-9", "(x+3)/(x+1)", "*(x - 3)/(x + 1)", "(x-9)/(x+1)"], "((x+3)(x-3)/(x+1)) * (1/(x+3)) = (x-3)/(x+1)."),
    ("Multiply: (3/(x-5)) * ((x^2-25)/6)", ["(x-25)/2", "3(x^2-25)/6", "*(x + 5)/2", "x^2/2"], "3 * (x-5)(x+5) / ((x-5) * 6) = (x+5)/2."),
    ("The product of (a/b) * (b/a) equals:", ["a^2/b^2", "0", "*1", "a + b"], "ab/(ba) = 1."),
    ("Divide: (4x^2)/(3y) / (2x)/(9y)", ["8x^3/(27y^2)", "2x/(3y)", "*6x", "4x/3"], "(4x^2/3y) * (9y/2x) = 36x^2y/(6xy) = 6x."),
    ("When multiplying, (x-3)/(x-3) simplifies to:", ["0", "x-3", "*1 (as long as x is not 3)", "undefined"], "Any nonzero expression divided by itself equals 1."),
])

# ── U9 L9.3: Adding & Subtracting Rational Expressions ──
add_questions("u9_l9.3", [
    ("Add: 3/x + 5/x", ["8/x^2", "15/x", "*8/x", "8/2x"], "Same denominator: (3+5)/x = 8/x."),
    ("Subtract: 7/(x+1) - 3/(x+1)", ["10/(x+1)", "4/(2x+2)", "*4/(x + 1)", "4/2"], "Same denominator: (7-3)/(x+1) = 4/(x+1)."),
    ("The LCD of 1/(2x) and 1/(3x) is:", ["6x^2", "x", "*6x", "5x"], "LCM of 2x and 3x is 6x."),
    ("Add: 1/(2x) + 1/(3x)", ["2/(5x)", "1/(6x)", "*5/(6x)", "2/(6x^2)"], "LCD=6x: 3/(6x) + 2/(6x) = 5/(6x)."),
    ("Subtract: x/(x-2) - 2/(x-2)", ["(x-2)/(x-2)", "x/2", "*1 (since (x-2)/(x-2) = 1, when x is not 2)", "0"], "(x-2)/(x-2) = 1."),
    ("The LCD of 1/(x+1) and 1/(x-1) is:", ["x^2 - 1", "(x+1)(x-1)", "*Both A and B are correct: (x+1)(x-1) = x^2-1", "x"], "LCD = (x+1)(x-1)."),
    ("Add: 2/(x+1) + 3/(x-1)", ["5/(x^2-1)", "5/(2x)", "*(5x - 1)/((x+1)(x-1))", "(2x+3)/(x^2-1)"], "LCD=(x+1)(x-1): [2(x-1)+3(x+1)]/LCD = (2x-2+3x+3)/LCD = (5x+1)/LCD."),
    ("The LCD of 1/x and 1/x^2 is:", ["x", "2x^2", "*x^2", "x^3"], "x^2 contains both x and x^2 as factors."),
    ("Add: 4/x + 1/x^2", ["5/x^2", "4/x^3", "*(4x + 1)/x^2", "5/x^3"], "LCD=x^2: 4x/x^2 + 1/x^2 = (4x+1)/x^2."),
    ("Subtract: 5/(x+3) - 5/(x+3)", ["10/(x+3)", "5", "*0", "undefined"], "Same terms cancel to 0."),
    ("When adding rational expressions with different denominators, the first step is:", ["Cross multiply", "Add denominators", "*Find the LCD (Least Common Denominator)", "Simplify numerators"], "Find LCD first."),
    ("Add: x/(x-4) + 4/(4-x)", ["(x+4)/(x-4)", "x+4", "*(x - 4)/(x - 4) = 1", "2x/(x-4)"], "Note 4-x = -(x-4), so 4/(4-x) = -4/(x-4). Then x/(x-4) - 4/(x-4) = (x-4)/(x-4) = 1."),
    ("Subtract: (3x+1)/(x+2) - (x-1)/(x+2)", ["(4x)/(x+2)", "(2x)/(x+2)", "*(2x + 2)/(x + 2)", "(3x+1-x+1)/(2x+4)"], "(3x+1-(x-1))/(x+2) = (3x+1-x+1)/(x+2) = (2x+2)/(x+2)."),
])

# ── U9 L9.4: Solving Rational Equations ──
add_questions("u9_l9.4", [
    ("Solve: x/3 = 4", ["x = 3", "x = 4/3", "*x = 12", "x = 7"], "Multiply both sides by 3: x = 12."),
    ("Solve: 5/x = 1/3", ["x = 1/15", "x = 3/5", "*x = 15", "x = 5/3"], "Cross multiply: 15 = x."),
    ("An extraneous solution is:", ["The correct answer", "*A solution that makes a denominator zero and must be rejected", "An extra solution", "An imaginary number"], "It satisfies the equation algebraically but is undefined in the original."),
    ("Solve: 1/x + 1/2 = 3/4. The LCD is:", ["x", "2", "*4x", "8"], "LCD of x, 2, 4 is 4x."),
    ("Using LCD = 4x for 1/x + 1/2 = 3/4: multiply through to get:", ["4 + 4x = 3x", "4 + 2x = 3", "*4 + 2x = 3x", "1 + 2x = 3x"], "4x(1/x) + 4x(1/2) = 4x(3/4) gives 4 + 2x = 3x, so x = 4."),
    ("Solve: (x+1)/(x-1) = 2. Multiply both sides by (x-1):", ["x + 1 = 2", "x = 1", "*x + 1 = 2(x - 1) = 2x - 2, so x = 3", "x = -1"], "x+1 = 2x-2, so 3 = x."),
    ("Solve: 3/(x-2) = 3/(x-2). How many solutions?", ["One", "None", "*All real numbers except x = 2 (identity, but x = 2 excluded)", "x = 2"], "Identity equation, but x = 2 makes denominator 0."),
    ("Solve: 2/(x+1) + 1/(x-1) = 1. First step:", ["Add fractions", "Divide by x", "*Multiply all terms by the LCD: (x+1)(x-1)", "Subtract 1"], "Clear denominators with LCD."),
    ("When solving rational equations, always check for:", ["Imaginary solutions", "Negative solutions", "*Extraneous solutions (values that make any denominator zero)", "Decimal solutions"], "Must verify answers don't make denominators 0."),
    ("Solve: 6/(x^2-4) = 1/(x-2). Note x^2-4 = (x-2)(x+2):", ["x = 6", "x = 2", "*x = 4", "x = -2"], "6/((x-2)(x+2)) = 1/(x-2). Multiply by (x-2)(x+2): 6 = x+2, x = 4."),
    ("Solve: x/(x-3) = 3/(x-3) + 1:", ["x = 3", "No solution", "*x = 3, but check: x=3 makes denominator 0, so NO SOLUTION", "x = 0"], "x = 3 is extraneous."),
    ("A work problem: Worker A takes 6 hours, Worker B takes 4 hours. Together:", ["10 hours", "5 hours", "*2.4 hours (1/6 + 1/4 = 5/12, so 12/5 = 2.4)", "3 hours"], "Combined rate: 1/6 + 1/4 = 5/12 of the job per hour."),
    ("Solve: (x+2)/5 = (x-1)/3:", ["x = 11/2", "x = 13/2", "*x = 11/2", "x = -11/2"], "Cross multiply: 3(x+2) = 5(x-1), 3x+6=5x-5, 11=2x, x=11/2."),
])

# ── U10 L10.1: Simplifying Radicals ──
add_questions("u10_l10.1", [
    ("Simplify: sqrt(75)", ["5sqrt(5)", "3sqrt(5)", "*5sqrt(3)", "25sqrt(3)"], "sqrt(75) = sqrt(25*3) = 5sqrt(3)."),
    ("Simplify: sqrt(48)", ["6sqrt(2)", "2sqrt(12)", "*4sqrt(3)", "8sqrt(3)"], "sqrt(48) = sqrt(16*3) = 4sqrt(3)."),
    ("Simplify: sqrt(200)", ["20sqrt(2)", "10sqrt(20)", "*10sqrt(2)", "2sqrt(100)"], "sqrt(200) = sqrt(100*2) = 10sqrt(2)."),
    ("Simplify: sqrt(x^6)", ["x^3", "x^6", "*x^3 (assuming x >= 0)", "x^2"], "sqrt(x^6) = x^3."),
    ("Simplify: 3sqrt(12)", ["6sqrt(2)", "3sqrt(4)", "*6sqrt(3)", "36sqrt(3)"], "3sqrt(12) = 3*2sqrt(3) = 6sqrt(3)."),
    ("Simplify: sqrt(18/2)", ["sqrt(18)/sqrt(2)", "3sqrt(2)/sqrt(2)", "*3", "9"], "sqrt(18/2) = sqrt(9) = 3."),
    ("Which is in simplest radical form?", ["sqrt(8)", "sqrt(12)", "*sqrt(7)", "sqrt(18)"], "7 has no perfect square factors."),
    ("Simplify: sqrt(50) + sqrt(32)", ["sqrt(82)", "7sqrt(2)+4sqrt(2)", "*9sqrt(2)", "82"], "5sqrt(2) + 4sqrt(2) = 9sqrt(2)."),
    ("Like radicals can be combined because:", ["They look similar", "*They have the same radicand (number under the radical), like combining like terms", "All radicals combine", "They have the same coefficient"], "Same radicand = like radicals."),
    ("Simplify: 2sqrt(27) - sqrt(12)", ["2sqrt(15)", "5sqrt(3)", "*4sqrt(3)", "sqrt(15)"], "2*3sqrt(3) - 2sqrt(3) = 6sqrt(3) - 2sqrt(3) = 4sqrt(3)."),
    ("Simplify: sqrt(x^2 * y^4)", ["xy^2", "x^2y^4", "*xy^2 (for x >= 0)", "x^2y^2"], "sqrt(x^2)*sqrt(y^4) = x*y^2."),
    ("The index of a square root is:", ["0", "1", "*2", "3"], "Square root = 2nd root."),
    ("Simplify: cube root of 54", ["3*cbrt(6)", "6*cbrt(3)", "*3*cbrt(2)", "9*cbrt(6)"], "54 = 27*2, cbrt(27) = 3, so 3*cbrt(2)."),
])

# ── U10 L10.2: Operations with Radicals ──
add_questions("u10_l10.2", [
    ("Multiply: sqrt(3) * sqrt(12)", ["sqrt(15)", "sqrt(36)", "*6", "3sqrt(4)"], "sqrt(3*12) = sqrt(36) = 6."),
    ("Multiply: (2sqrt(5))(3sqrt(5))", ["6sqrt(5)", "5sqrt(6)", "*30", "6sqrt(25)"], "2*3*sqrt(25) = 6*5 = 30."),
    ("Expand: (sqrt(3) + 1)^2", ["4", "3 + 1", "*4 + 2sqrt(3)", "3 + 2sqrt(3)"], "(sqrt(3))^2 + 2sqrt(3) + 1 = 3 + 2sqrt(3) + 1 = 4 + 2sqrt(3)."),
    ("Rationalize: 5/sqrt(3)", ["5sqrt(3)/3", "5/3", "*5sqrt(3)/3", "sqrt(15)/3"], "Multiply by sqrt(3)/sqrt(3): 5sqrt(3)/3."),
    ("Rationalize: 1/(sqrt(5) - sqrt(2))", ["(sqrt(5)+sqrt(2))/7", "(sqrt(5)-sqrt(2))/3", "*(sqrt(5) + sqrt(2))/3", "1/3"], "Multiply by conjugate: (sqrt(5)+sqrt(2))/((5-2)) = (sqrt(5)+sqrt(2))/3."),
    ("The conjugate of (sqrt(7) + 3) is:", ["sqrt(7) + 3", "3 - sqrt(7)", "*sqrt(7) - 3", "-sqrt(7) - 3"], "Change the sign between terms."),
    ("Divide: sqrt(50)/sqrt(2)", ["sqrt(48)", "sqrt(52)", "*5", "25"], "sqrt(50/2) = sqrt(25) = 5."),
    ("Multiply: sqrt(2)(sqrt(8) + sqrt(2))", ["sqrt(16) + 2", "4 + 2", "*6", "sqrt(10)"], "sqrt(16) + sqrt(4) = 4 + 2 = 6."),
    ("Expand: (sqrt(x) + 3)(sqrt(x) - 3)", ["x + 9", "x + 6sqrt(x)", "*x - 9", "x - 6"], "Difference of squares: x - 9."),
    ("Simplify: sqrt(3) * sqrt(3) * sqrt(3)", ["9", "3", "*3sqrt(3)", "sqrt(27)"], "3 * sqrt(3) = 3sqrt(3). Also sqrt(27) = 3sqrt(3)."),
    ("Why do we rationalize denominators?", ["It changes the value", "*Convention: it makes expressions easier to compare and combine; no irrational numbers in denominators", "It's required by law", "It simplifies the numerator"], "Standard mathematical convention."),
    ("Distribute: 2sqrt(3)(sqrt(6) - sqrt(3))", ["2sqrt(18) - 2*3", "6sqrt(2) - 6", "*6sqrt(2) - 6", "2sqrt(9)"], "2sqrt(18) - 2sqrt(9) = 2*3sqrt(2) - 2*3 = 6sqrt(2) - 6."),
    ("FOIL: (1 + sqrt(2))(3 - sqrt(2))", ["3 - sqrt(2) + 3sqrt(2) - 2", "1 + 2sqrt(2)", "*1 + 2sqrt(2)", "3 + 2sqrt(2)"], "3 - sqrt(2) + 3sqrt(2) - 2 = 1 + 2sqrt(2)."),
])

# ── U10 L10.3: Rational Exponents ──
add_questions("u10_l10.3", [
    ("Rewrite x^(1/2) as a radical:", ["x/2", "2x", "*sqrt(x)", "x^2"], "x^(1/n) = nth root of x."),
    ("Rewrite x^(2/3) as a radical:", ["sqrt(x^3)", "cbrt(x^2)", "*cbrt(x^2) or (cbrt(x))^2", "x^(3/2)"], "x^(m/n) = nth root of x^m."),
    ("Simplify: 8^(2/3)", ["16", "2", "*4", "6"], "cbrt(8)^2 = 2^2 = 4."),
    ("Simplify: 27^(1/3)", ["9", "27", "*3", "81"], "Cube root of 27 = 3."),
    ("Simplify: 16^(3/4)", ["4", "12", "*8", "64"], "4th root of 16 = 2, then 2^3 = 8."),
    ("x^(-1/2) equals:", ["-sqrt(x)", "x/2", "*1/sqrt(x)", "-x/2"], "Negative exponent = reciprocal."),
    ("Simplify: (x^(1/3))(x^(1/6))", ["x^(1/18)", "x^(2/9)", "*x^(1/2)", "x^(1/9)"], "Add exponents: 1/3 + 1/6 = 2/6 + 1/6 = 3/6 = 1/2."),
    ("Simplify: x^(3/4) / x^(1/4)", ["x^(3/16)", "x^3", "*x^(1/2)", "x^(2/4)"], "Subtract exponents: 3/4 - 1/4 = 2/4 = 1/2."),
    ("Rewrite sqrt(x^5) with rational exponents:", ["x^(5/3)", "x^(2/5)", "*x^(5/2)", "x^5/2"], "sqrt(x^5) = x^(5/2)."),
    ("Simplify: (x^4)^(1/2)", ["x^(1/2)", "x^4", "*x^2", "x^8"], "Multiply exponents: 4 * 1/2 = 2."),
    ("Which property is used: (ab)^(1/n) = a^(1/n) * b^(1/n)?", ["Power of a power", "Quotient rule", "*Product rule for radicals/exponents", "Addition rule"], "Product property of exponents."),
    ("Simplify: 4^(5/2)", ["10", "20", "*32", "8"], "sqrt(4)^5 = 2^5 = 32."),
    ("Simplify: (x^(1/2))^4", ["x^(1/8)", "x^(4/8)", "*x^2", "x^(1/2)"], "(1/2)*4 = 2."),
])

# ── U10 L10.4: Solving Radical Equations ──
add_questions("u10_l10.4", [
    ("Solve: sqrt(x) = 5", ["x = sqrt(5)", "x = 5", "*x = 25", "x = 10"], "Square both sides: x = 25."),
    ("Solve: sqrt(x + 3) = 7", ["x = 4", "x = 10", "*x = 46", "x = 52"], "Square: x + 3 = 49, x = 46."),
    ("Why must you check solutions to radical equations?", ["To practice", "*Squaring both sides can introduce extraneous solutions that don't satisfy the original equation", "Solutions are always correct", "For partial credit"], "Squaring is not an equivalent operation."),
    ("Solve: sqrt(2x - 1) = 3", ["x = 4", "x = 1", "*x = 5", "x = 2"], "Square: 2x - 1 = 9, 2x = 10, x = 5."),
    ("Solve: sqrt(x) = -3", ["x = 9", "x = -9", "x = -3", "*No solution (square root cannot equal a negative number)"], "Principal square root is always non-negative."),
    ("Solve: sqrt(x + 5) = x - 1. Square both sides:", ["x + 5 = x - 1", "x + 5 = x^2 + 1", "*x + 5 = x^2 - 2x + 1", "x + 5 = 2x - 1"], "Right side: (x-1)^2 = x^2 - 2x + 1."),
    ("Continuing: x + 5 = x^2 - 2x + 1, rearrange:", ["x^2 = 4", "x = 4", "*x^2 - 3x - 4 = 0, so (x-4)(x+1) = 0", "x^2 + 3x + 4 = 0"], "x = 4 or x = -1. Check both in original."),
    ("Check x = 4 in sqrt(x+5) = x-1: sqrt(9) = 3 and 4-1 = 3.", ["Reject", "*Valid (3 = 3)", "Extraneous", "Undefined"], "Both sides equal 3."),
    ("Check x = -1 in sqrt(x+5) = x-1: sqrt(4) = 2 and -1-1 = -2.", ["Valid", "*Extraneous (2 does not equal -2, reject x = -1)", "Both are correct", "Neither works"], "2 is not -2, so reject."),
    ("Solve: cbrt(x) = -2", ["x = -4", "No solution", "*x = -8", "x = 8"], "Cube both sides: x = (-2)^3 = -8."),
    ("Solve: sqrt(3x + 1) - 2 = 0", ["x = 3", "x = -1/3", "*x = 1", "x = 5/3"], "sqrt(3x+1) = 2, square: 3x+1 = 4, x = 1."),
    ("For equations with two radicals like sqrt(x+7) = sqrt(2x+1):", ["Add the radicals", "*Square both sides: x + 7 = 2x + 1, so x = 6", "Cube both sides", "Cannot be solved"], "Square to eliminate both radicals at once."),
    ("Solve: x = sqrt(x + 2). Square: x^2 = x + 2, so:", ["x = 2 only", "x = -1 only", "*x = 2 (x = -1 is extraneous since sqrt(1) = 1 but not -1)", "Both x = 2 and x = -1"], "Check: sqrt(4) = 2 works. sqrt(1) = 1, not -1."),
])

# ── U11 L11.1: Arithmetic & Geometric Sequences Review ──
add_questions("u11_l11.1", [
    ("In an arithmetic sequence, the common difference d for 3, 7, 11, 15 is:", ["3", "7", "*4", "15"], "7 - 3 = 4."),
    ("The nth term of an arithmetic sequence: a_n = a_1 + (n-1)d. Find a_10 for a_1=5, d=3:", ["35", "33", "*32", "30"], "5 + 9(3) = 5 + 27 = 32."),
    ("In a geometric sequence, the common ratio r for 2, 6, 18, 54 is:", ["2", "4", "*3", "6"], "6/2 = 3."),
    ("The nth term of a geometric sequence: a_n = a_1 * r^(n-1). Find a_5 for a_1=3, r=2:", ["24", "32", "*48", "96"], "3 * 2^4 = 3 * 16 = 48."),
    ("3, 8, 13, 18, 23 is:", ["Geometric", "*Arithmetic (d = 5)", "Neither", "Both"], "Constant difference of 5."),
    ("4, 12, 36, 108 is:", ["Arithmetic", "*Geometric (r = 3)", "Neither", "Both"], "Constant ratio of 3."),
    ("Find the 20th term: a_1 = 2, d = -3:", ["58", "-58", "*-55", "-60"], "2 + 19(-3) = 2 - 57 = -55."),
    ("Find a_6 for a_1 = 1, r = -2:", ["32", "64", "*-32", "-64"], "1 * (-2)^5 = -32."),
    ("An arithmetic sequence can have:", ["Only positive terms", "*Positive, negative, or mixed terms depending on a_1 and d", "Only integers", "Only whole numbers"], "Any real number values."),
    ("A geometric sequence with r between -1 and 1 (exclusive) will:", ["Diverge to infinity", "Stay constant", "*Converge toward 0 (terms get smaller and smaller)", "Alternate forever"], "Values approach 0."),
    ("The sequence 1, 1, 1, 1, 1 is:", ["Only arithmetic", "Only geometric", "*Both arithmetic (d=0) and geometric (r=1)", "Neither"], "Constant sequence satisfies both definitions."),
    ("Which grows faster as n increases: arithmetic (d=5) or geometric (r=2)?", ["Arithmetic", "*Geometric (exponential growth always overtakes linear growth)", "They grow equally", "Depends on starting value"], "Exponential dominates linear."),
    ("Identify: 5, -10, 20, -40, 80", ["Arithmetic", "*Geometric with r = -2", "Neither", "Fibonacci"], "Each term multiplied by -2."),
])

# ── U11 L11.2: Recursive & Explicit Formulas ──
add_questions("u11_l11.2", [
    ("A recursive formula defines each term using:", ["Only n", "*The previous term(s)", "Only the first term", "A constant"], "a_n depends on a_(n-1)."),
    ("An explicit formula gives the nth term:", ["From the previous term", "*Directly as a function of n (no previous terms needed)", "From a table", "Only for small n"], "Plug in n, get the term."),
    ("Recursive formula for 2, 5, 8, 11: a_1 = 2, a_n = ?", ["a_(n-1) * 3", "*a_(n-1) + 3", "2n + 3", "3n - 1"], "Each term is previous + 3."),
    ("Explicit formula for 2, 5, 8, 11:", ["2 + 3n", "5n - 3", "*3n - 1", "2(3)^n"], "a_n = 2 + (n-1)(3) = 3n - 1."),
    ("Recursive formula for 3, 6, 12, 24: a_1 = 3, a_n = ?", ["a_(n-1) + 3", "*2 * a_(n-1)", "3n", "a_(n-1) + 6"], "Each term is previous times 2."),
    ("Explicit formula for 3, 6, 12, 24:", ["6n", "3 + 2n", "*3(2)^(n-1)", "2(3)^n"], "a_n = 3 * 2^(n-1)."),
    ("The advantage of an explicit formula is:", ["It uses less memory.", "*You can find any term directly without computing all previous terms.", "It's always simpler.", "It works for all sequences."], "Direct computation."),
    ("The advantage of a recursive formula is:", ["It's always faster", "*It shows the pattern between consecutive terms clearly", "It never needs initial conditions", "It works without a first term"], "Shows relationship."),
    ("Given a_1 = 10, a_n = a_(n-1) - 4, find a_4:", ["10", "6", "2", "*-2"], "a_2=6, a_3=2, a_4=-2."),
    ("Convert recursive a_1=5, a_n = a_(n-1) + 7 to explicit:", ["5 + 7n", "7n + 5", "*5 + 7(n - 1) = 7n - 2", "12n"], "Arithmetic: a_n = 5 + (n-1)(7) = 7n - 2."),
    ("The Fibonacci sequence uses a recursive formula where:", ["a_n = 2*a_(n-1)", "a_n = a_(n-1) + 1", "*a_n = a_(n-1) + a_(n-2) (each term is sum of two previous)", "a_n = n * a_(n-1)"], "Famous recursive sequence."),
    ("Given a_n = 4n + 1, find a_1 and the common difference:", ["a_1 = 4, d = 1", "a_1 = 1, d = 1", "*a_1 = 5, d = 4", "a_1 = 4, d = 4"], "a_1 = 4(1)+1 = 5. Difference between terms = 4."),
    ("Given a_n = 2(3)^(n-1), what type of sequence?", ["Arithmetic", "*Geometric with a_1 = 2, r = 3", "Linear", "Quadratic"], "Exponential form = geometric."),
])

# ── U11 L11.3: Introduction to Series ──
add_questions("u11_l11.3", [
    ("A series is:", ["A sequence", "A pattern", "*The SUM of the terms of a sequence", "A product of terms"], "Series = sum."),
    ("Sigma notation (summation) uses the symbol:", ["Pi", "Delta", "*Sigma (the Greek capital letter that looks like a sideways M)", "Omega"], "Sigma means sum."),
    ("Find: sum from i=1 to 4 of (2i) = ?", ["8", "16", "*20 (2+4+6+8)", "24"], "2(1)+2(2)+2(3)+2(4) = 2+4+6+8 = 20."),
    ("Arithmetic series sum formula: S_n = n(a_1 + a_n)/2. Find S_10 for 1+2+3+...+10:", ["50", "45", "*55", "100"], "10(1+10)/2 = 10(11)/2 = 55."),
    ("Geometric series sum formula: S_n = a_1(1 - r^n)/(1 - r). Find S_5 for a_1=2, r=3:", ["162", "200", "*242", "364"], "2(1-243)/(1-3) = 2(-242)/(-2) = 242."),
    ("Sum of first 20 terms of 3 + 7 + 11 + 15 +... (d=4):", ["400", "830", "*820", "860"], "S_20 = 20(3 + (3+19*4))/2 = 20(3+79)/2 = 20(82)/2 = 820."),
    ("An infinite geometric series converges when:", ["r > 1", "r = 1", "*|r| < 1 (the absolute value of the common ratio is less than 1)", "Always"], "Must have |r| < 1."),
    ("Sum of infinite geometric series: S = a_1/(1-r). For a_1=10, r=1/2:", ["5", "15", "*20", "10"], "10/(1-0.5) = 10/0.5 = 20."),
    ("Sum of first 100 positive integers = ?", ["5000", "10000", "*5050", "10100"], "100(101)/2 = 5050. Gauss's famous result."),
    ("Partial sum S_4 of 1 + 3 + 9 + 27 = ?", ["30", "36", "*40", "81"], "1(1-81)/(1-3) = (-80)/(-2) = 40."),
    ("Write in sigma notation: 1 + 4 + 9 + 16 + 25", ["Sum of i, i=1 to 5", "*Sum of i^2, i = 1 to 5", "Sum of 2i, i=1 to 5", "Sum of i+3, i=1 to 5"], "These are perfect squares: 1^2 through 5^2."),
    ("The sum 0.333... = 3/10 + 3/100 + 3/1000 +... is an infinite geometric series with sum:", ["0.3", "0.33", "*1/3", "3/10"], "a_1 = 3/10, r = 1/10: (3/10)/(1-1/10) = (3/10)/(9/10) = 1/3."),
    ("For a divergent geometric series (|r| >= 1), the sum:", ["Equals zero", "Equals a_1", "*Does not exist (the partial sums grow without bound)", "Equals infinity exactly"], "No finite sum exists."),
])

# ── U12 L12.1: Sample Spaces & Basic Probability ──
add_questions("u12_l12.1", [
    ("The probability of an event ranges from:", ["-1 to 1", "0 to infinity", "*0 to 1 (0 = impossible, 1 = certain)", "1 to 100"], "Probability bounds."),
    ("A fair coin flip: P(heads) =", ["0", "1", "*0.5 or 1/2", "0.25"], "Equal likelihood."),
    ("The sample space for rolling a die is:", ["{1,2,3,4,5}", "{1,6}", "*{1, 2, 3, 4, 5, 6}", "{2,4,6}"], "All possible outcomes."),
    ("P(rolling a 3 on a fair die) =", ["1/3", "3/6", "*1/6", "1/2"], "1 favorable out of 6."),
    ("P(rolling an even number) =", ["1/6", "1/3", "*3/6 = 1/2", "2/3"], "Even: 2, 4, 6 = 3 out of 6."),
    ("Complementary events: P(A) + P(not A) =", ["0", "0.5", "*1", "2"], "Event and complement always sum to 1."),
    ("P(not rolling a 6) =", ["1/6", "1/3", "*5/6", "1"], "1 - 1/6 = 5/6."),
    ("Flipping two coins: the sample space has _____ outcomes.", ["2", "3", "*4 (HH, HT, TH, TT)", "8"], "2 x 2 = 4 outcomes."),
    ("P(at least one head in two coin flips) =", ["1/2", "1/4", "*3/4", "1"], "1 - P(no heads) = 1 - 1/4 = 3/4."),
    ("A bag has 3 red, 5 blue, 2 green marbles. P(blue) =", ["3/10", "2/10", "*5/10 = 1/2", "1/3"], "5 blue out of 10 total."),
    ("Theoretical probability is based on:", ["Experiments", "*What SHOULD happen mathematically (using counting and logic)", "Past data only", "Guessing"], "Mathematical expectation."),
    ("Experimental probability is based on:", ["Mathematical formulas", "*Actual trial results (observed frequency / total trials)", "Theoretical models", "Predictions"], "Observed outcomes."),
    ("Law of large numbers states that as trials increase:", ["Probability changes", "Results become random", "*Experimental probability approaches theoretical probability", "Outcomes become predictable"], "More trials = closer to expected."),
])

# ── U12 L12.2: Independent & Dependent Events ──
add_questions("u12_l12.2", [
    ("Independent events: the outcome of one _____ the probability of the other.", ["Changes", "Determines", "*Does not affect", "Doubles"], "No influence."),
    ("For independent events A and B: P(A and B) =", ["P(A) + P(B)", "P(A) - P(B)", "*P(A) * P(B)", "P(A) / P(B)"], "Multiplication rule for independent events."),
    ("Flipping a coin then rolling a die: P(heads AND 6) =", ["1/2 + 1/6", "2/12", "*1/12 (1/2 * 1/6)", "1/8"], "Independent: multiply."),
    ("Drawing a card, replacing it, then drawing again is:", ["Dependent", "*Independent (replacement restores original probabilities)", "Neither", "Conditional"], "With replacement = independent."),
    ("Drawing without replacement makes events:", ["Independent", "*Dependent (removing a card changes probabilities for the second draw)", "Random", "Impossible"], "Probabilities change."),
    ("Bag: 4 red, 6 blue. P(red then blue) WITHOUT replacement:", ["4/10 * 6/10", "4/10 * 6/9", "*4/10 * 6/9 = 24/90 = 4/15", "10/10"], "After removing red: 6 blue out of 9 remaining."),
    ("P(red then red) WITHOUT replacement (4 red out of 10):", ["16/100", "4/10 * 4/10", "*4/10 * 3/9 = 12/90 = 2/15", "8/20"], "After first red: 3 red out of 9."),
    ("Two dice: P(both show 6) =", ["1/6", "2/36", "*1/36", "1/12"], "1/6 * 1/6 = 1/36."),
    ("Are these independent: drawing a heart from deck 1 and a spade from deck 2?", ["No", "*Yes (separate decks don't affect each other)", "Depends", "Cannot tell"], "Different decks = independent."),
    ("P(rolling 4 three times in a row) on a fair die:", ["3/6", "1/216", "*1/216 = (1/6)^3", "1/18"], "(1/6)(1/6)(1/6)."),
    ("If P(A) = 0.3 and P(B) = 0.5, and A and B are independent, P(A and B) =", ["0.8", "0.2", "*0.15", "0.35"], "0.3 * 0.5."),
    ("A test for independence: P(A and B) = P(A)*P(B). If P(A)=0.4, P(B)=0.5, P(A and B)=0.2:", ["Dependent", "*Independent (0.4 * 0.5 = 0.2 matches)", "Cannot determine", "Always independent"], "Product matches joint probability."),
    ("If P(A)=0.4, P(B)=0.5, but P(A and B)=0.3:", ["Independent", "*Dependent (0.4*0.5=0.2, not 0.3, so they influence each other)", "Cannot determine", "Complementary"], "Product doesn't match."),
])

# ── U12 L12.3: Conditional Probability ──
add_questions("u12_l12.3", [
    ("P(A|B) reads as:", ["P of A or B", "P of A times B", "*Probability of A GIVEN that B has occurred", "P of A and B"], "Conditional notation."),
    ("Formula: P(A|B) =", ["P(A) * P(B)", "P(A) + P(B)", "*P(A and B) / P(B)", "P(A) / P(A and B)"], "Joint divided by condition."),
    ("Given P(A and B) = 0.12, P(B) = 0.4: P(A|B) =", ["0.48", "0.52", "*0.3", "0.12"], "0.12 / 0.4 = 0.3."),
    ("If events are independent, then P(A|B) = ?", ["0", "P(B)", "*P(A) (knowing B doesn't change A's probability)", "P(A and B)"], "No influence means conditional equals unconditional."),
    ("A class: 60% study, 80% of studiers pass, 30% of non-studiers pass. P(pass|study) =", ["0.6", "0.3", "*0.8", "0.5"], "Given directly: 80% of studiers pass."),
    ("From the class: P(study AND pass) =", ["0.8", "0.6", "*0.48 (0.6 * 0.8)", "0.3"], "P(study) * P(pass|study) = 0.6 * 0.8."),
    ("P(not study AND pass) =", ["0.3", "*0.12 (0.4 * 0.3)", "0.4", "0.7"], "P(not study) * P(pass|not study) = 0.4 * 0.3."),
    ("Total P(pass) in the class:", ["0.48", "0.12", "*0.60 (0.48 + 0.12)", "0.80"], "P(pass) = P(pass and study) + P(pass and not study)."),
    ("Two-way tables help calculate conditional probability by:", ["Showing graphs", "*Organizing joint frequencies so you can easily find P(A|B) by looking at the B row/column", "Listing all probabilities", "Only showing totals"], "Organized frequency data."),
    ("P(study|pass) using Bayes' theorem = P(pass|study)*P(study)/P(pass) =", ["0.6", "0.5", "*0.8 (0.48/0.60)", "0.48"], "0.48/0.60 = 0.8."),
    ("Bayes' theorem reverses conditional probability, finding P(B|A) from:", ["P(A) only", "*P(A|B), P(B), and P(A)", "P(B) only", "Nothing"], "Reverses the condition."),
    ("A medical test: P(positive|disease) = 0.95, P(positive|no disease) = 0.05, P(disease) = 0.01. P(disease|positive) is:", ["0.95", "0.50", "*Approximately 0.16 (much lower than 0.95 due to low base rate)", "0.01"], "Bayes: 0.95*0.01/(0.95*0.01 + 0.05*0.99) = 0.0095/0.059 ≈ 0.16."),
    ("The base rate fallacy occurs when people:", ["Ignore conditional probability", "*Overestimate P(disease|positive) because they ignore the low base rate of the disease", "Multiply incorrectly", "Don't use Bayes"], "Common probability mistake."),
])

# ── U12 L12.4: Probability with Combinatorics ──
add_questions("u12_l12.4", [
    ("The fundamental counting principle: if event A has m outcomes and event B has n outcomes, total outcomes =", ["m + n", "m - n", "*m * n", "m / n"], "Multiply choices."),
    ("How many 3-digit codes (0-9 each digit)?", ["30", "100", "*1,000 (10 * 10 * 10)", "999"], "10^3 possibilities."),
    ("Permutation (order matters): P(n,r) = n!/(n-r)!. P(5,3) =", ["10", "15", "*60", "125"], "5!/(5-3)! = 120/2 = 60."),
    ("Combination (order doesn't matter): C(n,r) = n!/(r!(n-r)!). C(5,3) =", ["60", "15", "*10", "5"], "5!/(3!*2!) = 120/(6*2) = 10."),
    ("Choosing a committee of 3 from 8 people uses:", ["Permutations", "*Combinations (order of selection doesn't matter)", "Addition", "Neither"], "Committee = unordered."),
    ("Arranging 3 books on a shelf from 8 uses:", ["Combinations", "*Permutations (order/arrangement matters)", "Addition", "Neither"], "Arrangement = ordered."),
    ("C(10,2) = ", ["20", "90", "*45", "100"], "10!/(2!*8!) = 90/2 = 45."),
    ("How many ways to arrange all 5 letters of ABCDE?", ["25", "5", "*120 (5! = 120)", "60"], "5 factorial."),
    ("P(winning lottery: choose 6 from 49) = 1/C(49,6) =", ["1/49", "1/294", "*1/13,983,816", "1/720"], "C(49,6) = 13,983,816."),
    ("Probability of being dealt a pair in 5-card poker uses:", ["Only permutations", "Only addition", "*Combinations to count favorable outcomes divided by total possible hands", "Only multiplication"], "C(13,1)*C(4,2)*C(12,3)*4^3 / C(52,5)."),
    ("How many ways to choose 2 boys and 3 girls from 5 boys and 7 girls?", ["12", "35", "*350 (C(5,2)*C(7,3) = 10*35)", "70"], "Multiply independent combinations."),
    ("0! (zero factorial) equals:", ["0", "Undefined", "*1 (by definition)", "Does not exist"], "Convention: 0! = 1."),
    ("P(all 4 aces in a 5-card hand) = C(4,4)*C(48,1)/C(52,5) =", ["1/52", "4/52", "*48/2,598,960 (very small)", "1/13"], "Only 48 possible hands contain all 4 aces."),
])

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
for k in sorted(data.keys(), key=lambda x: (data[x]['unit'], x)):
    n = len(data[k].get('quiz_questions', []))
    if n < 20:
        print(f"STILL SHORT: {k} has {n}")
ct = sum(1 for v in data.values() if len(v.get('quiz_questions',[])) >= 20)
print(f"✅ Algebra 1: {ct}/{len(data)} lessons at 20+ questions")
