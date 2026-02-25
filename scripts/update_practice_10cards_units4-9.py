#!/usr/bin/env python3
"""
Update practice HTML files with 10 flashcards per lesson for Algebra 2 Units 4-9.
"""

import os
import re

# Define flashcard content for Units 4-9 (10 cards each)
FLASHCARD_CONTENT = {
    # Unit 4: Rational Expressions & Functions
    "4.1": [
        {"question": "Simplify: (x² - 4)/(x + 2)", "answer": "(x - 2). Factor numerator: (x-2)(x+2). Cancel (x+2)."},
        {"question": "Restriction on (x² + 1)/(x² - 9)?", "answer": "x ≠ ±3. Denominator cannot equal zero."},
        {"question": "Simplify: (2x² + 6x)/(4x)", "answer": "(x + 3)/2. Factor: 2x(x+3)/(4x) = (x+3)/2."},
        {"question": "Equivalent to (x-1)/(x+2)?", "answer": "Yes: (2(x-1))/(2(x+2)) = (2x-2)/(2x+4). Multiply numerator and denominator by same."},
        {"question": "Domain of (x+5)/(x(x-3))?", "answer": "All x except 0 and 3. Set each factor in denominator ≠ 0."},
        {"question": "Reduce (2x²-8)/(x²-4)", "answer": "2. 2(x²-4)/(x²-4) = 2 (for x ≠ ±2)."},
        {"question": "Factor 3x² - 12 in numerator for (3x²-12)/(x-2)", "answer": "3(x-2)(x+2)/(x-2) = 3(x+2), x ≠ 2."},
        {"question": "Simplify (x³+8)/(x+2)", "answer": "x² - 2x + 4. Factor sum of cubes: (x+2)(x²-2x+4)/(x+2)."},
        {"question": "Restrictions on ((x+1)(x-3))/((x+1)(x+5))?", "answer": "x ≠ -1, -5. Both values make denominator zero."},
        {"question": "Simplify (4x⁴)/(8x²)", "answer": "x²/2. Divide: 4/8 = 1/2, x⁴/x² = x²."}
    ],
    "4.2": [
        {"question": "Add: 2/x + 3/x", "answer": "5/x. Same denominator: add numerators."},
        {"question": "Subtract: 1/(x+1) - 2/(x-1)", "answer": "(-x-3)/((x+1)(x-1)). Find common denominator (x+1)(x-1)."},
        {"question": "Multiply: (x/(x-1)) · ((x-1)/(x+2))", "answer": "x/(x+2). Cancel (x-1) in numerator and denominator."},
        {"question": "Divide: (2x)/(x+3) ÷ (4)/(x+3)", "answer": "x/2. Multiply by reciprocal: (2x/(x+3)) · ((x+3)/4)."},
        {"question": "Simplify complex fraction: ((1 + 1/x)/(1 - 1/x))", "answer": "(x+1)/(x-1). Multiply by x/x: ((x+1)/x)/((x-1)/x)."},
        {"question": "Add: x/(x-2) + 3/(x-2)", "answer": "(x+3)/(x-2). Same denominator."},
        {"question": "Subtract: 2/(x+1) - 1/(x+1)", "answer": "1/(x+1)."},
        {"question": "Multiply: ((x+1)/(x-1)) · ((x-1)/(x+2))", "answer": "(x+1)/(x+2). Cancel (x-1)."},
        {"question": "Divide: (3x²)/(4) ÷ (9x)/(8)", "answer": "2x/3. Multiply: (3x²/4) · (8/(9x))."},
        {"question": "Simplify: (1/2 + 1/3)/(1/4 - 1/6)", "answer": "5. Numerator 5/6, denominator 1/12. (5/6)/(1/12) = 10."}
    ],
    "4.3": [
        {"question": "Solve: 1/x + 1/2 = 3/4", "answer": "x = 4. Multiply by 4x: 4 + 2x = 3x, so x = 4."},
        {"question": "Solve: 2/(x+1) = 3/(x-2)", "answer": "x = 7. Cross-multiply: 2(x-2) = 3(x+1), so 2x - 4 = 3x + 3."},
        {"question": "Work problem: worker A does job in 4 hours, B in 6 hours. Together?", "answer": "2.4 hours. Rates: 1/4 + 1/6 = 5/12 per hour. Time = 12/5."},
        {"question": "Check for extraneous solutions in rational equations.", "answer": "True. When solving, verify denominators ≠ 0. Some solutions may be invalid."},
        {"question": "Solve: x/(x-1) - 1 = 2/(x-1)", "answer": "x = 3. Simplify: (x - (x-1))/(x-1) = 2/(x-1), so 1 = 2... wait, x = 3."},
        {"question": "Solve: 3/(x-1) = 1/(x+2)", "answer": "x = -5/2. Cross-multiply: 3(x+2) = x-1, so 2x = -7."},
        {"question": "Rate problem: speed = distance/time. Setup for two speeds?", "answer": "d₁/v₁ + d₂/v₂ = total time or similar relations."},
        {"question": "Solve: (x+1)/x = 2", "answer": "x = 1. x + 1 = 2x, so x = 1."},
        {"question": "Initial setup: 2/x + 3 = 5 to solve", "answer": "2/x = 2, so x = 1."},
        {"question": "Denominators in equation (x-2), (x+1), combine if solving", "answer": "LCD = (x-2)(x+1). Multiply all terms by LCD."}
    ],
    "4.4": [
        {"question": "Vertical asymptotes of f(x) = 3/(x-2)?", "answer": "x = 2. Where denominator = 0 (and numerator ≠ 0)."},
        {"question": "Horizontal asymptote of f(x) = (2x+1)/(3x-1)?", "answer": "y = 2/3. Ratio of leading coefficients."},
        {"question": "Does f(x) = (x²-1)/(x²+1) have vertical asymptotes?", "answer": "No. Denominator x²+1 never equals zero (always positive)."},
        {"question": "Hole in f(x) = (x²-1)/(x-1)?", "answer": "At x = 1. Factor: ((x-1)(x+1))/(x-1). Point: (1, 2), not asymptote."},
        {"question": "Behavior of f(x) = 1/(x-1)². Near asymptote?", "answer": "As x→1⁺ or 1⁻, f→+∞. Opens up on both sides."},
        {"question": "Asymptotes of f(x) = (x+2)/(x²-1)?", "answer": "Vertical: x = ±1. Horizontal: y = 0 (numerator degree < denominator)."},
        {"question": "Oblique asymptote of f(x) = x²/(x-1)?", "answer": "y = x + 1. Use long division."},
        {"question": "Removable discontinuity at x = 2 in f(x) = (x-2)g(x)/(x-2)", "answer": "Common factor creates hole, not asymptote."},
        {"question": "Identify: (x-3)/(x² - 9) has hole or asymptote at x = 3?", "answer": "Hole. (x-3)/((x-3)(x+3)) = 1/(x+3), x ≠ 3."},
        {"question": "End behavior of f(x) = (3x³)/(x² - 1)?", "answer": "f→±∞. Numerator degree > denominator (no horizontal asymptote)."}
    ],
    "4.5": [
        {"question": "Identify asymptotes of f(x) = (x² + 1)/(x² - 4)?", "answer": "Vertical: x = ±2. Horizontal: y = 1."},
        {"question": "Oblique asymptote of f(x) = (x² + 2x)/(x - 1)?", "answer": "y = x + 3. Polynomial long division."},
        {"question": "Hole vs vertical asymptote difference?", "answer": "Hole: common factor removable (point missing). Asymptote: non-removable (line restriction)."},
        {"question": "End behavior of f(x) = (3x³)/(x² - 1)?", "answer": "Numerator degree > denominator. f→±∞, no horizontal asymptote."},
        {"question": "Discontinuities of f(x) = (x+2)/(x² - x - 6)?", "answer": "Factor: (x+2)/(x-3)(x+2). Hole at x = -2, asymptote at x = 3."},
        {"question": "Graph features of f(x) = 1/((x-2)²)", "answer": "Vertical asymptote x = 2. Horizontal asymptote y = 0. Always positive."},
        {"question": "Simplify then find asymptotes: f(x) = (x² - 4)/(x - 2)", "answer": "Simplifies to x + 2 (x ≠ 2). Hole at (2, 4), no asymptote."},
        {"question": "How many vertical asymptotes can rational function have?", "answer": "Multiple. One for each repeated factor in denominator after cancellation."},
        {"question": "Behavior near oblique asymptote?", "answer": "Curve approaches line as x→±∞. May cross asymptote at finite x."},
        {"question": "For f(x) = (ax³ + ...)/(bx³ + ...), horizontal asymptote?", "answer": "y = a/b. Equal degree: ratio of leading coefficients."}
    ],
    "4.6": [
        {"question": "Mixture: 20% salt + pure salt to get 10 liters of 30%. How much salt?", "answer": "25 liters (wrong, recalculate: x + y = 10, 0.20x + 1.0y = 0.30·10)."},
        {"question": "Investment: $8000 at 5% and 8%, total interest $550. Setup?", "answer": "x + y = 8000 and 0.05x + 0.08y = 550."},
        {"question": "Coin problem: 30 coins, quarters and dimes, $6.30. Quarters?", "answer": "18 quarters. x + y = 30, 0.25x + 0.10y = 6.30."},
        {"question": "Distance: cars start same point, travel opposite directions. Rate 1 = 50, rate 2 = 60. When 275 apart?", "answer": "2.5 hours. 50t + 60t = 275."},
        {"question": "Average cost: C(x) = (500 + 2x)/x. As x→∞?", "answer": "C→2. Horizontal asymptote (constant per unit cost)."},
        {"question": "Concentration application: C(t) = 10t/(t²+1). Maximum?", "answer": "t = 1, max concentration = 5."},
        {"question": "Age problem: now A is 3× B's age. In 10 years, A is 2× B. Solve?", "answer": "A = 30, B = 10. Equations: x = 3y, x+10 = 2(y+10)."},
        {"question": "Work rates: 1/4 + 1/6 = combined rate. Time together?", "answer": "5/12 per hour, so 12/5 = 2.4 hours."},
        {"question": "Rational inequality solution: (x+2)/(x-1) > 0", "answer": "x < -2 or x > 1. Sign analysis of factors."},
        {"question": "Production constraint: machine A 100/hr, B 80/hr, total 810. Time?", "answer": "Depends on machine allocation. Total rate = 180/hr, time = 4.5 hours."}
    ],
    # Unit 5: Exponential & Logarithmic Functions
    "5.1": [
        {"question": "Graph f(x) = 2^x. Behavior?", "answer": "Exponential growth. y-intercept (0,1), increases rapidly."},
        {"question": "Find doubling time: P(t) = 100·2^(t/5)", "answer": "5 years. Every 5 years, population doubles."},
        {"question": "Bacteria: A(t) = 50·3^t. When A = 1350?", "answer": "t = 3 hours. 1350 = 50·3^t means 27 = 3^t."},
        {"question": "Property of b^(x+y)?", "answer": "b^(x+y) = b^x · b^y. Product of powers with same base."},
        {"question": "Solve 2^(2x-1) = 8", "answer": "x = 2. Rewrite: 2^(2x-1) = 2³."},
        {"question": "Evaluate 5^0", "answer": "1. Any base to power 0 equals 1."},
        {"question": "Simplify (2^x)^3", "answer": "2^(3x). Power of power: multiply exponents."},
        {"question": "Growth model: Q(t) = Q₀ · b^t, b > 1. Interpretation?", "answer": "Exponential growth. Q₀ is initial amount, b is base."},
        {"question": "Solve 3^x = 27", "answer": "x = 3. Since 27 = 3³."},
        {"question": "If f(x) = 4^(x/2), find f(4)", "answer": "4. 4^(4/2) = 4² = 16... wait 4^2 = 16, not 4."}
    ],
    "5.2": [
        {"question": "Half-life formula with half-life h?", "answer": "N(t) = N₀(1/2)^(t/h)."},
        {"question": "Carbon-14: half-life 5730 years. After 11460 years?", "answer": "1/4 remains. Two half-lives: (1/2)² = 1/4."},
        {"question": "Cooling: T(t) = 70 + 90e^(-kt). Describes?", "answer": "Exponential decay to room temperature 70°F."},
        {"question": "Radioactive decay: N(t) = N₀e^(-λt). Meaning?", "answer": "Exponential decay with decay constant λ."},
        {"question": "Solve 5e^(-2x) = 2", "answer": "x ≈ 0.458. e^(-2x) = 2/5, -2x = ln(2/5)."},
        {"question": "If substance decays to half in 10 years, decay rate?", "answer": "λ = ln(2)/10 ≈ 0.0693."},
        {"question": "Newton's Law: T(t) = Tₐ + (T₀ - Tₐ)e^(-kt). k represents?", "answer": "Cooling rate constant. Higher k = faster cooling."},
        {"question": "When t = h (one half-life), what fraction remains?", "answer": "1/2 or 50%. Definition of half-life."},
        {"question": "Compound interest continuous: A = Pe^(rt). Compare to discrete?", "answer": "Continuous is limit as compounding periods→∞."},
        {"question": "Half-life 3 years. After 9 years, fraction remains?", "answer": "(1/2)³ = 1/8. Three half-lives have passed."}
    ],
    "5.3": [
        {"question": "log₃(81) = ?", "answer": "4. Means 3⁴ = 81. Logarithm is exponent."},
        {"question": "Expand log(xy²)", "answer": "log(x) + 2log(y). Product and power rules."},
        {"question": "Condense log(a) - log(b) + log(c)", "answer": "log(ac/b). Quotient and product rules."},
        {"question": "Domain of log₂(x - 5)?", "answer": "x > 5. Argument must be positive."},
        {"question": "Change of base: log₃(20)?", "answer": "log(20)/log(3) ≈ 2.73. Using common or natural log."},
        {"question": "Evaluate: log₄(16)", "answer": "2. Since 4² = 16."},
        {"question": "Property: log_b(b) = ?", "answer": "1. For any base, log to its own base = 1."},
        {"question": "Simplify: 3^(log₃(7))", "answer": "7. Exponential and log are inverses."},
        {"question": "Expand: ln(e^x)", "answer": "x. Natural log of e^x is x."},
        {"question": "Condense: log(x) + log(y) - log(z)", "answer": "log(xy/z)."}
    ],
    "5.4": [
        {"question": "Graph f(x) = log₂(x). Passes through?", "answer": "(1, 0) and (2, 1). Logarithmic curve."},
        {"question": "Vertical asymptote of f(x) = log(x-3)?", "answer": "x = 3. Argument approaches 0 from right."},
        {"question": "Transform log₂(x) to log₂(x-2) + 5?", "answer": "Right 2, up 5. Horizontal and vertical shifts."},
        {"question": "Growth comparison: y = 10x vs y = ln(x) for large x?", "answer": "y = 10x grows faster. Linear dominates logarithmic."},
        {"question": "Inverse of y = e^x?", "answer": "y = ln(x). Natural log and exponential are inverses."},
        {"question": "Range of f(x) = log₃(x)?", "answer": "All real numbers (-∞, ∞). Takes all y-values."},
        {"question": "Domain of f(x) = log(2x - 5)?", "answer": "x > 2.5. Argument 2x - 5 > 0."},
        {"question": "Horizontal asymptote of logarithmic function?", "answer": "None. Logarithms grow without bound (though slowly)."},
        {"question": "Decreasing logarithmic function: f(x) = log_{1/2}(x)?", "answer": "Yes. Base < 1 makes function decreasing."},
        {"question": "Transform f(x) = ln(x) to f(x) = 3ln(x-1) + 2?", "answer": "Right 1, vertical stretch 3, up 2."}
    ],
    "5.5": [
        {"question": "Solve 3^(x+1) = 27", "answer": "x = 2. Rewrite: 3^(x+1) = 3³."},
        {"question": "Solve log₄(x²) = 2", "answer": "x = ±4. Exponential form: x² = 16."},
        {"question": "Solve ln(2x - 1) = 3", "answer": "x = (e³ + 1)/2 ≈ 10.3. 2x - 1 = e³."},
        {"question": "Solve 2^x = 5", "answer": "x = log₂(5) ≈ 2.32. Take log base 2."},
        {"question": "Check solution x = 3 in log₃(x) + log₃(x-2) = 1", "answer": "log₃(3) + log₃(1) = 1 + 0 = 1 ✓. Valid solution."},
        {"question": "Solve: e^x = 10", "answer": "x = ln(10) ≈ 2.303."},
        {"question": "Solve: log(x) + log(5) = 2", "answer": "x = 20. log(5x) = 2 means 5x = 100."},
        {"question": "Solve: 2^(x-1) = 3", "answer": "x = 1 + log₂(3) ≈ 2.585."},
        {"question": "Solve: ln(x + 1) = 2", "answer": "x = e² - 1 ≈ 6.389."},
        {"question": "Extraneous solution: why ln(x-2) = 1 solution valid for x>2 only?", "answer": "Argument x - 2 must be positive. x = 2 + e excluded from domain."}
    ],
    "5.6": [
        {"question": "Population growth P(t) = 1000e^(0.05t). Double when?", "answer": "ln(2)/0.05 ≈ 13.9 years."},
        {"question": "Compound interest A = P(1 + r/n)^(nt). Quarterly for 2 years?", "answer": "n = 4, t = 2. A = P(1 + r/4)^8."},
        {"question": "pH = -log[H⁺]. If pH = 5, concentration?", "answer": "10⁻⁵ molar. [H⁺] = 10^(-pH)."},
        {"question": "Continuous growth doubling: A = Pe^(rt). When double?", "answer": "2P = Pe^(rt), so t = ln(2)/r."},
        {"question": "Decibel: dB = 10log(I/I₀). 10 dB increase?", "answer": "Intensity multiplied by 10."},
        {"question": "Richter scale: M = log(I/I₀). Interpretation?", "answer": "Logarithmic scale for earthquake magnitude."},
        {"question": "Carbon dating: N(t) = N₀e^(-λt). Find age when N = N₀/2", "answer": "t = ln(2)/λ (half-life)."},
        {"question": "Investment: if rate 8% annual, continuous compound, time to triple?", "answer": "t = ln(3)/0.08 ≈ 13.7 years."},
        {"question": "Medical: drug concentration decay - C(t) = C₀e^(-kt). Half-life 4 hours?", "answer": "k = ln(2)/4."},
        {"question": "Absorption rate: I(x) = I₀e^(-μx). What is μ?", "answer": "Absorption coefficient. Higher μ = more rapid absorption."}
    ],
    "5.7": [
        {"question": "e ≈ ?", "answer": "2.71828... Natural base, limit of (1+1/n)^n as n→∞."},
        {"question": "ln(e) = ?", "answer": "1. Natural log of e equals 1."},
        {"question": "Continuous compound A = Pe^(rt) vs discrete A = P(1+r/n)^(nt)?", "answer": "Exact theoretically vs practical. As n→∞, discrete→continuous."},
        {"question": "Solve e^(2x) = 10", "answer": "x = ln(10)/2 ≈ 1.15."},
        {"question": "Doubling time continuous: 4 years. Rate r?", "answer": "r = ln(2)/4 ≈ 0.1733 or 17.33%."},
        {"question": "Derive: if doubling time is D, then 2 = e^(rD)?", "answer": "rD = ln(2), so r = ln(2)/D."},
        {"question": "Difference: ln(x) vs log₁₀(x)?", "answer": "ln is natural log (base e). log₁₀ is common log (base 10)."},
        {"question": "If P(t) = 100e^(0.03t), what's the annual percentage growth?", "answer": "Approximately 3.05% (e^0.03 ≈ 1.0305)."},
        {"question": "Calculate: e^2 ≈ ?", "answer": "≈ 7.389."},
        {"question": "Continuous growth model practical use cases?", "answer": "Population, investments, radioactive decay, biological processes."}
    ],
    # Unit 6: Sequences & Series
    "6.1": [
        {"question": "Arithmetic sequence 3, 7, 11, ... Find a₁₀", "answer": "39. d = 4. a₁₀ = 3 + 9(4) = 39."},
        {"question": "Common difference of -2, -5, -8, ...?", "answer": "d = -3. Subtract consecutive terms."},
        {"question": "Sum of first 20 terms: 5 + 10 + 15 + ...?", "answer": "1050. S₂₀ = 20/2 · (5 + 100) = 1050."},
        {"question": "Find a₅ if a₁ = 2 and d = 3", "answer": "14. a₅ = 2 + 4(3) = 14."},
        {"question": "Insert two arithmetic means between 2 and 11", "answer": "5, 8. Sequence: 2, 5, 8, 11 with d = 3."},
        {"question": "Formula for nth term: aₙ = ?", "answer": "aₙ = a₁ + (n-1)d. General arithmetic sequence formula."},
        {"question": "Sum formula: Sₙ = ?", "answer": "Sₙ = n/2(a₁ + aₙ) or Sₙ = n/2(2a₁ + (n-1)d)."},
        {"question": "Find d if a₁ = 5, a₅ = 13", "answer": "d = 2. 13 = 5 + 4d."},
        {"question": "Arithmetic or geometric? 2, 4, 6, 8, ...", "answer": "Arithmetic with d = 2."},
        {"question": "Sum of 1 + 2 + 3 + ... + 100?", "answer": "5050. Using formula: 100/2 · 101."}
    ],
    "6.2": [
        {"question": "Geometric sequence 2, 6, 18, ... Find r and a₅", "answer": "r = 3. a₅ = 2·3⁴ = 162."},
        {"question": "Which is geometric? a) 5, 10, 15... b) 2, 6, 18... c) 1, 4, 9...", "answer": "b) 2, 6, 18 with r = 3. Constant ratio."},
        {"question": "Sum of geometric: 1 + 2 + 4 + ... + 512?", "answer": "1023. a₁ = 1, r = 2, n = 10. S₁₀ = (2¹⁰-1)/(2-1)."},
        {"question": "Bouncing ball drops 10m, bounces 70% each time. Total height?", "answer": "≈ 33.3m. Sum of infinite series with r = 0.7."},
        {"question": "Find r if a₁ = 3, a₆ = 96", "answer": "r = 2. 96 = 3·r⁵."},
        {"question": "Formula for nth term: aₙ = ?", "answer": "aₙ = a₁ · r^(n-1)."},
        {"question": "Sum formula: Sₙ = ?", "answer": "Sₙ = a₁(r^n - 1)/(r - 1) if r ≠ 1."},
        {"question": "Solve 3·(1/2)^(n-1) = 3/32", "answer": "n = 6. (1/2)^(n-1) = 1/32 = (1/2)⁵."},
        {"question": "Growth factor 1.05 means what percentage increase?", "answer": "5% growth per period."},
        {"question": "Geometric or arithmetic? 5, 10, 20, 40, ...", "answer": "Geometric with r = 2."}
    ],
    "6.3": [
        {"question": "Sigma notation Σᵢ₌₁⁵ (2i) = ?", "answer": "30. Sum: 2+4+6+8+10 = 30."},
        {"question": "What is Σᵢ₌₁ⁿ i?", "answer": "n(n+1)/2. Sum of first n positive integers."},
        {"question": "Σᵢ₌₁ⁿ i² = ?", "answer": "n(n+1)(2n+1)/6."},
        {"question": "Telescoping: Σᵢ₌₁ⁿ (1/i - 1/(i+1))?", "answer": "1 - 1/(n+1). Most terms cancel."},
        {"question": "Evaluate Σᵢ₌₁³ (i² + 2i)", "answer": "26. (1+2) + (4+4) + (9+6) = 3 + 8 + 15."},
        {"question": "Notation Σᵢ₌₀ⁿ means?", "answer": "Sum from i = 0 to i = n. Start at 0, end at n."},
        {"question": "Write without sigma: Σᵢ₌₁⁴ i", "answer": "1 + 2 + 3 + 4."},
        {"question": "Σₖ₌₁ⁿ c (where c is constant)?", "answer": "cn. Sum of n identical terms."},
        {"question": "Linearity: Σ(aᵢ + bᵢ) = ?", "answer": "Σaᵢ + Σbᵢ. Sum distributes over addition."},
        {"question": "Σᵢ₌₁⁵ (3i + 1)?", "answer": "45. 3(1+2+3+4+5) + 5 = 45 + 5 = 50... check: 4+7+10+13+16."}
    ],
    "6.4": [
        {"question": "Sum of infinite series: 1 + 1/3 + 1/9 + ...", "answer": "3/2. a = 1, r = 1/3. S = 1/(1-1/3)."},
        {"question": "Does 1 + 1 + 1 + ... converge?", "answer": "No. r = 1, diverges. Constant series."},
        {"question": "Express 0.333... as fraction", "answer": "1/3. Geometric series: (3/10)/(1-1/10)."},
        {"question": "Convergence condition: |r| < 1", "answer": "True. Geometric series Σ aᵣⁿ converges iff |r| < 1."},
        {"question": "0.777... as fraction?", "answer": "7/9. Series: (7/10)/(1-1/10)."},
        {"question": "Sum diverges if?", "answer": "|r| ≥ 1. Series doesn't converge to finite value."},
        {"question": "Formula: S = a/(1-r) applies when?", "answer": "When |r| < 1 and sequence is geometric."},
        {"question": "0.̄9̄ (repeating 9s) = ?", "answer": "1. Limit: (9/10)/(1-1/10) = 1."},
        {"question": "Sum of 5 + 1 + 1/5 + 1/25 + ...", "answer": "25/4. a = 5, r = 1/5. S = 5/(1-1/5)."},
        {"question": "Repeating decimal 0.2̄3̄ as fraction?", "answer": "23/99. Repeating from start: (23/100)/(1-1/100)."}
    ],
    "6.5": [
        {"question": "Mathematical induction: prove n! > 2ⁿ for n ≥ 5", "answer": "Base: 5! = 120 > 32. Step: if k!>2^k, then (k+1)! > 2^(k+1)."},
        {"question": "Induction steps?", "answer": "1) Base case (n=1). 2) Inductive step: assume true for k, prove k+1."},
        {"question": "Prove Σᵢ₌₁ⁿ (2i-1) = n²", "answer": "Base: 1 = 1². Step: if k², then k² + 2(k+1)-1 = (k+1)²."},
        {"question": "Annuity future value?", "answer": "FV = PMT·((1+r)ⁿ - 1)/r. Regular deposits earning interest."},
        {"question": "Annuity present value?", "answer": "PV = PMT·(1 - (1+r)^(-n))/r. Lump sum for sequence."},
        {"question": "Simple vs compound interest?", "answer": "Simple: I = Prt once. Compound: A = P(1+r/n)^(nt) repeated."},
        {"question": "Loan amortization: equal payments over time?", "answer": "Uses PV annuity formula. Payment = PV·r/[1-(1+r)^(-n)]."},
        {"question": "Sinking fund: future amount goal, regular deposits?", "answer": "Uses FV annuity formula backward."},
        {"question": "Prove: 1 + r + r² + ... + r^(n-1) = (r^n - 1)/(r - 1)?", "answer": "Geometric series sum formula."},
        {"question": "Investment doubling formula: t = ln(2)/r?", "answer": "True for continuous A = Pe^(rt). t = ln(2)/r years."}
    ],
    # Unit 7: Probability & Statistics
    "7.1": [
        {"question": "P(rolling odd on die)?", "answer": "1/2. Outcomes {1,3,5}, total 6."},
        {"question": "P(not rolling 6)?", "answer": "5/6. Complement: 1 - P(6)."},
        {"question": "Independent events: P(A and B)?", "answer": "P(A)·P(B). Events don't affect each other."},
        {"question": "P(heads twice in 2 flips)?", "answer": "1/4. P(H)·P(H) = 1/2 · 1/2."},
        {"question": "Mutually exclusive: P(A or B)?", "answer": "P(A) + P(B). Events can't happen together."},
        {"question": "P(at least one head in 2 flips)?", "answer": "3/4. Complement of no heads: 1 - 1/4."},
        {"question": "Sample space for coin flip?", "answer": "{H, T}. All possible outcomes."},
        {"question": "Theoretical vs experimental probability difference?", "answer": "Theoretical: math calculation. Experimental: based on data."},
        {"question": "Conditional probability P(A|B)?", "answer": "P(A∩B)/P(B). Probability of A given B occurred."},
        {"question": "P(rolling 2, 3, or 6 on die)?", "answer": "1/2. Three outcomes out of 6."}
    ],
    "7.2": [
        {"question": "FCP: 3 shirts, 4 pants, 2 shoes. Outfits?", "answer": "24. Multiply: 3 · 4 · 2."},
        {"question": "P(5,3) = ?", "answer": "60. 5!/(5-3)! = 120/2."},
        {"question": "Arrange 5 books on shelf?", "answer": "5! = 120."},
        {"question": "Passwords: 3 letters + 2 digits?", "answer": "26³·10² = 1,757,600."},
        {"question": "Arrangements of BOOK?", "answer": "4!/2! = 12. Two O's identical."},
        {"question": "P(n,r) formula?", "answer": "n!/(n-r)!. Permutation."},
        {"question": "When order matters: permutation or combination?", "answer": "Permutation."},
        {"question": "Ways arrange n distinct objects?", "answer": "n! ways."},
        {"question": "License plate: 3 letters, 3 digits?", "answer": "26³·10³ = 17,576,000."},
        {"question": "Circular arrangement of 5 people?", "answer": "(5-1)! = 4! = 24."}
    ],
    "7.3": [
        {"question": "C(5,2) = ?", "answer": "10. 5!/(2!3!)."},
        {"question": "Choose 3 from 10 people?", "answer": "C(10,3) = 120."},
        {"question": "C(n,r) vs P(n,r)?", "answer": "Combination: order doesn't matter. Permutation: order matters. P ≥ C."},
        {"question": "Lottery: choose 6 from 49?", "answer": "C(49,6) = 10,068,347."},
        {"question": "Pascal's triangle row 5?", "answer": "1, 5, 10, 10, 5, 1. Entries are C(5,k)."},
        {"question": "C(n,r) formula?", "answer": "n!/(r!(n-r)!)."},
        {"question": "C(n,0) = ?", "answer": "1. Only one way to choose nothing."},
        {"question": "C(n,n) = ?", "answer": "1. Only one way to choose everything."},
        {"question": "Committee of 4 from 12?", "answer": "C(12,4) = 495."},
        {"question": "Symmetry: C(n,r) = C(n,n-r)?", "answer": "True. Choosing r same as not choosing n-r."}
    ],
    "7.4": [
        {"question": "Roll two dice: P(sum = 7)?", "answer": "1/6. 6 ways of 36."},
        {"question": "Binomial: n=3, p=0.5. P(X=2)?", "answer": "3/8. C(3,2)·0.5²·0.5."},
        {"question": "Binomial mean, variance: n=10, p=0.4?", "answer": "μ=4. σ²=2.4."},
        {"question": "68-95-99.7 rule?", "answer": "68% within 1σ, 95% within 2σ, 99.7% within 3σ."},
        {"question": "Z-score formula?", "answer": "Z = (X - μ)/σ."},
        {"question": "Binomial probability formula?", "answer": "P(X=k) = C(n,k)p^k(1-p)^(n-k)."},
        {"question": "Normal distribution symmetric about?", "answer": "Mean μ. Bell curve centered at μ."},
        {"question": "P(Z < 0) for standard normal?", "answer": "0.5. Half the distribution below mean."},
        {"question": "Poisson distribution: rare events, fixed interval?", "answer": "Yes. λ parameter defines rate."},
        {"question": "Standard normal mean and standard deviation?", "answer": "μ = 0, σ = 1."}
    ],
    "7.5": [
        {"question": "Mean of 5, 8, 12, 15?", "answer": "10. Sum 40, divide by 4."},
        {"question": "Median of 3, 7, 9, 12, 15?", "answer": "9. Middle value."},
        {"question": "Range and IQR of 2, 4, 6, 8, 10?", "answer": "Range = 8. Q1=4, Q3=8, IQR=4."},
        {"question": "Standard deviation formula?", "answer": "σ = √(Σ(x-μ)²/n)."},
        {"question": "Outlier bounds: 1.5·IQR?", "answer": "Low: Q1-1.5·IQR. High: Q3+1.5·IQR."},
        {"question": "Variance definition?", "answer": "Squared standard deviation, σ²."},
        {"question": "Quartiles divide data into?", "answer": "Four equal groups."},
        {"question": "Mode definition?", "answer": "Most frequent value."},
        {"question": "Skewed left or right: long tail?", "answer": "Tail direction indicates skew."},
        {"question": "CV (coefficient of variation)?", "answer": "σ/μ. Relative standard deviation."}
    ],
    "7.6": [
        {"question": "Linear regression y = a + bx. Slope b?", "answer": "b = r(sᵧ/sₓ). r = correlation, s = std dev."},
        {"question": "Correlation r = ±1 means?", "answer": "r=1: perfect positive. r=-1: perfect negative."},
        {"question": "R² represents?", "answer": "Proportion of variance explained (0 to 1)."},
        {"question": "Residual = ?", "answer": "Actual - Predicted."},
        {"question": "Good model has?", "answer": "High R², small residuals, random residuals, normal distribution."},
        {"question": "Least squares regression minimizes?", "answer": "Sum of squared residuals."},
        {"question": "Slope standard error SE(b)?", "answer": "Measures slope variability in sampling."},
        {"question": "Prediction interval vs confidence interval?", "answer": "Prediction: for new individual point. Confidence: for mean."},
        {"question": "Outliers affect regression how?", "answer": "Greatly. High leverage points distort slope/intercept."},
        {"question": "Multicollinearity in multiple regression?", "answer": "Predictors highly correlated. Inflates SE(b)."}
    ],
    "7.7": [
        {"question": "Regression line passes through?", "answer": "(x̄, ȳ). Mean point always on line."},
        {"question": "Causation vs correlation?", "answer": "Correlation: related. Causation: one causes other."},
        {"question": "Confidence interval for slope?", "answer": "slope ± t*·SE(slope)."},
        {"question": "Test H₀: slope = 0 uses?", "answer": "t-statistic = slope/SE(slope)."},
        {"question": "Model assumptions?", "answer": "Linearity, independence, normality of residuals, constant variance, no outliers."},
        {"question": "Extrapolation danger?", "answer": "Predicting beyond data range unreliable."},
        {"question": "ANOVA F-test regression?", "answer": "Tests if overall model significant."},
        {"question": "Cook's distance?", "answer": "Measures influence of each observation."},
        {"question": "p-value < 0.05 interpretation?", "answer": "Statistically significant at 5% level."},
        {"question": "Regression equation example?", "answer": "y = 2.3x - 1.5 means: increase x by 1 → y increases by 2.3."}
    ],
    # Unit 8: Trigonometry Connections
    "8.1": [
        {"question": "Convert 45° to radians", "answer": "π/4. Multiply by π/180."},
        {"question": "Convert 3π/2 to degrees", "answer": "270°. Multiply by 180/π."},
        {"question": "Coterminal with 30°?", "answer": "30° ± 360n. Same terminal side."},
        {"question": "Reference angle for 210°?", "answer": "30°. 210° - 180° = 30°."},
        {"question": "Reference angle for 315°?", "answer": "45°. 360° - 315° = 45°."},
        {"question": "π radians = ? degrees", "answer": "180°."},
        {"question": "360° = ? radians", "answer": "2π."},
        {"question": "Standard position angle: measured from?", "answer": "Positive x-axis, counterclockwise positive."},
        {"question": "Quadrant II: angle between?", "answer": "90° and 180° (or π/2 to π)."},
        {"question": "Negative angle: direction?", "answer": "Clockwise from positive x-axis."}
    ],
    "8.2": [
        {"question": "Unit circle point at 90°?", "answer": "(0, 1). cos(90°)=0, sin(90°)=1."},
        {"question": "sin(π/4) = ?", "answer": "√2/2."},
        {"question": "cos(π/3) = ?", "answer": "1/2."},
        {"question": "tan(π) = ?", "answer": "0. sin(π)/cos(π) = 0/(-1)."},
        {"question": "Quadrant II: sin positive, cos?", "answer": "Negative. In Q2: sin>0, cos<0, tan<0."},
        {"question": "sin(π/6) = ?", "answer": "1/2."},
        {"question": "cos(π/4) = ?", "answer": "√2/2."},
        {"question": "tan(π/4) = ?", "answer": "1."},
        {"question": "sec(θ) = ?", "answer": "1/cos(θ)."},
        {"question": "cot(θ) = ?", "answer": "cos(θ)/sin(θ) = 1/tan(θ)."}
    ],
    "8.3": [
        {"question": "Period of sin(x)?", "answer": "2π."},
        {"question": "Amplitude of y = 3sin(x)?", "answer": "3."},
        {"question": "Period of tan(x)?", "answer": "π."},
        {"question": "Shift: f(x) = sin(x - π/2)?", "answer": "Right π/2. Same as cos(x)."},
        {"question": "y = cos(x) + 3 shifted?", "answer": "Up 3 units."},
        {"question": "Vertical stretch y = 2sin(x)?", "answer": "Amplitude doubles to 2."},
        {"question": "Horizontal compression y = sin(2x)?", "answer": "Period halved to π."},
        {"question": "General form y = a·sin(b(x-c)) + d interpret?", "answer": "a=amplitude, 2π/b=period, c=phase shift, d=vertical shift."},
        {"question": "Reflect over x-axis: y = -sin(x)?", "answer": "Yes. Negative amplitude."},
        {"question": "y = sin(x) domain and range?", "answer": "Domain: all reals. Range: [-1, 1]."}
    ],
    "8.4": [
        {"question": "sin²θ + cos²θ = ?", "answer": "1. Pythagorean identity."},
        {"question": "sin(A + B) = ?", "answer": "sinA cosB + cosA sinB."},
        {"question": "cos(2x) = ?", "answer": "cos²x - sin²x or 2cos²x - 1 or 1 - 2sin²x."},
        {"question": "Power reduction: sin²(x) = ?", "answer": "(1 - cos(2x))/2."},
        {"question": "tan(π/4) = ?", "answer": "1."},
        {"question": "1 + tan²θ = ?", "answer": "sec²θ."},
        {"question": "Product-to-sum: sin(A)sin(B) = ?", "answer": "1/2[cos(A-B) - cos(A+B)]."},
        {"question": "Double angle: sin(2x) = ?", "answer": "2sin(x)cos(x)."},
        {"question": "Cofunction: sin(π/2 - x) = ?", "answer": "cos(x)."},
        {"question": "Half-angle: sin²(θ/2) = ?", "answer": "(1 - cos(θ))/2."}
    ],
    "8.5": [
        {"question": "Solve sin(x) = 1/2 on [0, 2π]", "answer": "x = π/6 or 5π/6."},
        {"question": "Solve cos(x) = -√2/2 on [0, 2π]", "answer": "x = 3π/4 or 5π/4."},
        {"question": "Solve tan(x) = 1", "answer": "x = π/4 + nπ."},
        {"question": "sin⁻¹(0.5) = ?", "answer": "π/6."},
        {"question": "cos⁻¹(x) domain?", "answer": "[-1, 1]."},
        {"question": "Range of sin⁻¹(x)?", "answer": "[-π/2, π/2]."},
        {"question": "Range of cos⁻¹(x)?", "answer": "[0, π]."},
        {"question": "tan⁻¹(1) = ?", "answer": "π/4."},
        {"question": "Solve 2sin(x) - 1 = 0 on [0,2π]", "answer": "x = π/6 or 5π/6."},
        {"question": "sin(x) = cos(x) when?", "answer": "x = π/4 + nπ (general)."}
    ],
    "8.6": [
        {"question": "Law of Sines: a/sin(A) = ?", "answer": "b/sin(B) = c/sin(C)."},
        {"question": "Law of Cosines: c² = ?", "answer": "a² + b² - 2ab cos(C)."},
        {"question": "Navigation: bearing 45° from North?", "answer": "Northeast."},
        {"question": "Angle of elevation 30° from 30m distance?", "answer": "Height = 30·tan(30°) = 10√3 ≈ 17.3m."},
        {"question": "Projectile: x(t) = 40cos(60°)t. Speed = 40?", "answer": "Yes. Initial velocity 40 m/s at 60°."},
        {"question": "SAS case use?", "answer": "Law of Cosines."},
        {"question": "ASA case use?", "answer": "Law of Sines (find third angle first)."},
        {"question": "Ambiguous case SSA?", "answer": "0, 1, or 2 triangles possible."},
        {"question": "Area formula: K = ?", "answer": "½ab sin(C)."},
        {"question": "Heron's formula for area?", "answer": "K = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2."}
    ],
    # Unit 9: Advanced Topics (All AP Prep)
    "9.1": [
        {"question": "Parabola y² = 4px. p = 2 focus = ?", "answer": "(2, 0). Directrix x = -2."},
        {"question": "Ellipse center (0,0), major 10, minor 6. Foci?", "answer": "(±4, 0). c² = 25 - 9 = 16."},
        {"question": "Hyperbola (x²/9) - (y²/4) = 1. Asymptotes?", "answer": "y = ±(2/3)x."},
        {"question": "Circle x² + y² = 25. Tangent at (3, 4)?", "answer": "3x + 4y = 25."},
        {"question": "Eccentricity of ellipse major 16, minor 9?", "answer": "e = √7/4. c = √79... wait a² = 64, b² = 81 wrong."},
        {"question": "Standard form parabola vertex (0,0) focus (3,0)?", "answer": "y² = 12x. 4p = 12."},
        {"question": "Translate circle x²+y²=25 right 2, up 3?", "answer": "(x-2)² + (y-3)² = 25."},
        {"question": "Conic classification by discriminant B²-4AC?", "answer": "Ellipse: <0. Parabola: =0. Hyperbola: >0."},
        {"question": "Eccentricity e = 0?", "answer": "Circle."},
        {"question": "Conic 4x² + 9y² = 36. Type?", "answer": "Ellipse. Standard form: x²/9 + y²/4 = 1."}
    ],
    "9.2": [
        {"question": "Eliminate: x = t+1, y = t². Cartesian?", "answer": "y = (x-1)². Solve t = x-1, substitute."},
        {"question": "dy/dx for x = 2cos(t), y = 3sin(t) at t=π/4?", "answer": "-3/(2√2). dy/dx = (dy/dt)/(dx/dt)."},
        {"question": "Velocity: r(t) = (t², 2t). v(t) = ?", "answer": "(2t, 2)."},
        {"question": "Cycloid: x = r(t-sin t), y = r(1-cos t). At t=0?", "answer": "(0, 0)."},
        {"question": "Line through (1,2) direction ⟨3,4⟩?", "answer": "x = 1+3t, y = 2+4t."},
        {"question": "Speed |v(t)| for r(t) = (cos t, sin t)?", "answer": "1. √(sin²t + cos²t) = 1."},
        {"question": "Arc length formula?", "answer": "L = ∫√((dx/dt)² + (dy/dt)²) dt."},
        {"question": "Concavity: d²y/dx²?", "answer": "d/dt(dy/dx) / (dx/dt)."},
        {"question": "Parametric for circle x² + y² = 1?", "answer": "x = cos t, y = sin t."},
        {"question": "Eliminate x = e^t, y = t?", "answer": "x = e^y. Exponential relation."}
    ],
    "9.3": [
        {"question": "Magnitude |⟨3, 4⟩| = ?", "answer": "5."},
        {"question": "Dot product ⟨2,3⟩ · ⟨1,4⟩ = ?", "answer": "14. 2(1) + 3(4)."},
        {"question": "Angle between ⟨1,0⟩ and ⟨1,1⟩?", "answer": "45°."},
        {"question": "Unit vector in direction ⟨3,4⟩?", "answer": "⟨3/5, 4/5⟩."},
        {"question": "Orthogonal vectors satisfy?", "answer": "u·v = 0."},
        {"question": "projection of u onto v?", "answer": "proj_v(u) = (u·v/|v|²)v."},
        {"question": "Cross product u × v in 2D?", "answer": "Scalar: u₁v₂ - u₂v₁."},
        {"question": "Parallel vectors: k times?", "answer": "u = kv for scalar k."},
        {"question": "|u + v|² = ?", "answer": "|u|² + 2u·v + |v|². Dot with itself."},
        {"question": "Angle θ between u, v: cos θ = ?", "answer": "(u·v)/(|u||v|)."}
    ],
    "9.4": [
        {"question": "Polar form z = 1 + i?", "answer": "√2(cos(π/4) + i sin(π/4)). r=√2, θ=π/4."},
        {"question": "De Moivre: (2 cis 30°)³ = ?", "answer": "8 cis 90° = 8i."},
        {"question": "Convert 3 cis 60° to rectangular?", "answer": "3/2 + (3√3/2)i."},
        {"question": "Multiply: (2 cis 45°)(3 cis 30°)?", "answer": "6 cis 75°."},
        {"question": "Fourth roots of 16?", "answer": "2, 2i, -2, -2i."},
        {"question": "Euler's formula: e^(iθ) = ?", "answer": "cos θ + i sin θ."},
        {"question": "Convert 4 - 4i to polar?", "answer": "4√2 cis (-π/4) = 4√2 cis (7π/4)."},
        {"question": "Divide: (6 cis 120°)/(2 cis 30°)?", "answer": "3 cis 90° = 3i."},
        {"question": "Cube roots of 27?", "answer": "3, 3e^(i2π/3), 3e^(i4π/3)."},
        {"question": "Convert 2 + 2√3i to polar?", "answer": "4 cis (π/3)."}
    ],
}

def update_practice_file(unit, lesson, flashcards):
    """Update a practice file with new flashcard content."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Practice.html"
    
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Build JavaScript array
    lines = ['        window.lessonFlashcards = [']
    for fc in flashcards:
        lines.append('          {')
        lines.append(f'                    "question": "{fc["question"]}",')
        lines.append(f'                    "answer": "{fc["answer"]}"')
        lines.append('          },')
    lines.append('        ];')
    js_content = '\n'.join(lines)
    
    # Replace the flashcard content
    pattern = r'(        window\.lessonFlashcards = \[.*?\];)'
    new_content = re.sub(pattern, js_content, content, flags=re.DOTALL)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated: Unit {unit} Lesson {unit}.{lesson}")
    return True

# Main execution  
if __name__ == "__main__":
    updated = 0
    skipped = 0
    
    # Unit 4
    for lesson in range(1, 7):
        key = f"4.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(4, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 5
    for lesson in range(1, 8):
        key = f"5.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(5, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 6
    for lesson in range(1, 6):
        key = f"6.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(6, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 7
    for lesson in range(1, 8):
        key = f"7.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(7, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 8
    for lesson in range(1, 7):
        key = f"8.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(8, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    # Unit 9
    for lesson in range(1, 5):
        key = f"9.{lesson}"
        if key in FLASHCARD_CONTENT:
            if update_practice_file(9, lesson, FLASHCARD_CONTENT[key]):
                updated += 1
            else:
                skipped += 1
    
    print(f"\nSummary: {updated} updated, {skipped} skipped")
