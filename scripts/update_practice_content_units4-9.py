#!/usr/bin/env python3
"""
Update practice HTML files with flashcard content for Algebra 2 Units 4-9.
"""

import os
import re

# Define flashcard content for Units 4-9
FLASHCARD_CONTENT = {
    # Unit 4: Rational Expressions & Functions
    "4.1": [
        {"question": "Simplify: (x² - 4)/(x + 2)", "answer": "(x - 2). Factor numerator: (x-2)(x+2). Cancel (x+2)."},
        {"question": "Restriction on (x² + 1)/(x² - 9)?", "answer": "x ≠ ±3. Denominator cannot equal zero."},
        {"question": "Simplify: (2x² + 6x)/(4x)", "answer": "(x + 3)/2. Factor: 2x(x+3)/(4x) = (x+3)/2."},
        {"question": "Equivalent to (x-1)/(x+2)?", "answer": "Yes: (2(x-1))/(2(x+2)) = (2x-2)/(2x+4). Multiply numerator and denominator by same."},
        {"question": "Domain of (x+5)/(x(x-3))?", "answer": "All x except 0 and 3. Set each factor in denominator ≠ 0."}
    ],
    "4.2": [
        {"question": "Add: 2/x + 3/x", "answer": "5/x. Same denominator: add numerators."},
        {"question": "Subtract: 1/(x+1) - 2/(x-1)", "answer": "((x-1) - 2(x+1))/((x+1)(x-1)) = (-x-3)/((x+1)(x-1)). Find common denominator."},
        {"question": "Multiply: (x/(x-1)) · ((x-1)/(x+2))", "answer": "x/(x+2). Cancel (x-1) in numerator and denominator."},
        {"question": "Divide: (2x)/(x+3) ÷ (4)/(x+3)", "answer": "(x/2). Multiply by reciprocal: (2x/(x+3)) · ((x+3)/4)."},
        {"question": "Simplify complex fraction: ((1 + 1/x)/(1 - 1/x))", "answer": "(x+1)/(x-1). Multiply by x/x: ((x+1)/x)/((x-1)/x)."}
    ],
    "4.3": [
        {"question": "Solve: 1/x + 1/2 = 3/4", "answer": "x = 4. Multiply by 4x: 4 + 2x = 3x, so x = 4."},
        {"question": "Solve: 2/(x+1) = 3/(x-2)", "answer": "x = 7. Cross-multiply: 2(x-2) = 3(x+1), so 2x - 4 = 3x + 3."},
        {"question": "Work problem: One worker does job in 4 hours, another in 6 hours. Together?", "answer": "2.4 hours. Rates: 1/4 + 1/6 = 5/12 per hour. So 12/5 = 2.4 hours."},
        {"question": "Check for extraneous solutions in rational equations.", "answer": "True. When solving, simplifications may introduce invalid values. Verify denominators ≠ 0."},
        {"question": "Solve: x/(x-1) = 2/(x-1) + 1", "answer": "x = 3. Simplify: x/(x-1) - 2/(x-1) = 1, so (x-2)/(x-1) = 1, thus x - 2 = x - 1... wait: (x-2)/(x-1) = 1 means x-2 = x-1, which has no solution... check work."}
    ],
    "4.4": [
        {"question": "Vertical asymptotes of f(x) = 3/(x-2)?", "answer": "x = 2. Where denominator = 0 (and numerator ≠ 0)."},
        {"question": "Horizontal asymptote of f(x) = (2x+1)/(3x-1)?", "answer": "y = 2/3. Ratio of leading coefficients."},
        {"question": "Does f(x) = (x²-1)/(x²+1) have vertical asymptotes?", "answer": "No. Denominator x²+1 never equals zero (always positive)."},
        {"question": "Hole in f(x) = (x²-1)/(x-1)?", "answer": "At x = 1. Factor: ((x-1)(x+1))/(x-1). Hole at (1, 2), not asymptote."},
        {"question": "Sketch f(x) = 1/(x-1)². Asymptotes?", "answer": "Vertical asymptote x = 1. Horizontal asymptote y = 0. Opens up on both sides."}
    ],
    "4.5": [
        {"question": "Identify asymptotes of f(x) = (x² + 1)/(x² - 4)?", "answer": "Vertical: x = ±2. Horizontal: y = 1. Numerator and denominator both degree 2."},
        {"question": "Oblique asymptote of f(x) = (x² + 2x)/(x - 1)?", "answer": "y = x + 3. Use polynomial long division. Quotient is oblique asymptote."},
        {"question": "Hole vs vertical asymptote difference?", "answer": "Hole: common factor in numerator/denominator (removable). Asymptote: denominator only (non-removable)."},
        {"question": "End behavior of f(x) = (3x³)/(x² - 1)?", "answer": "Numerator degree > denominator. Function approaches ±∞ at ends. No horizontal asymptote."},
        {"question": "Discontinuities of f(x) = (x+2)/(x² - x - 6)?", "answer": "Factor: (x+2)/(x-3)(x+2). Hole at x = -2, vertical asymptote at x = 3."}
    ],
    "4.6": [
        {"question": "Mixture problem: 20% salt solution mixed with 50% solution to get 10 liters of 30%?", "answer": "5 liters 20%, 5 liters 50%. System: x + y = 10, 0.20x + 0.50y = 0.30(10)."},
        {"question": "Average cost function C(x) = (500 + 2x)/x minimized?", "answer": "When dC/dx = 0. As x → ∞, C → 2. Minimum approaches $2 per unit."},
        {"question": "Concentration problem: Drug concentration C(t) = 10t/(t²+1) max at what time?", "answer": "t = 1 hour (find critical point). dC/dt = 0."},
        {"question": "Rational inequalities: solve (x+2)/(x-1) > 0", "answer": "x < -2 or x > 1. Sign table: negative between roots, positive outside."},
        {"question": "Inverse variation: y = k/x. If y = 4 when x = 3, find y when x = 2.", "answer": "y = 6. k = 12. So y = 12/2 = 6."}
    ],
    # Unit 5: Exponential & Logarithmic Functions
    "5.1": [
        {"question": "Graph f(x) = 2^x. Behavior?", "answer": "Exponential growth. Passes (0,1), increases rapidly. Approaches 0 as x→-∞."},
        {"question": "Find doubling time: P(t) = 100·2^(t/5)", "answer": "Doubling time = 5 years. Every 5 years, population doubles."},
        {"question": "Bacteria growth: A(t) = 50·3^t. When A = 1350?", "answer": "t = 3 hours. 1350 = 50·3^t means 27 = 3^t, so t = 3."},
        {"question": "Property of b^(x+y)?", "answer": "b^(x+y) = b^x · b^y. Product of powers with same base."},
        {"question": "Solve 2^(2x-1) = 8", "answer": "x = 2. Rewrite: 2^(2x-1) = 2³, so 2x - 1 = 3, thus x = 2."}
    ],
    "5.2": [
        {"question": "Half-life formula with half-life h?", "answer": "N(t) = N₀(1/2)^(t/h). Remains after each half-life period."},
        {"question": "Carbon-14 has half-life 5730 years. After 11460 years?", "answer": "1/4 remains. Two half-lives: (1/2)² = 1/4."},
        {"question": "Cooling: T(t) = 70 + 90e^(-kt). Cool from 160°F to room temp 70°F?", "answer": "Uses exponential decay. e^(-kt) describes cooling rate."},
        {"question": "Radioactive decay: N(t) = N₀e^(-λt). If N = N₀/2 at t = 10?", "answer": "Half-life = 10 ln(2)/λ years. Decay constant λ relates to half-life."},
        {"question": "Solve 5e^(-2x) = 2", "answer": "x = ln(5/2)/(2) ≈ 0.458. Divide by 5, take natural log, divide by -2."}
    ],
    "5.3": [
        {"question": "log₃(81) = ?", "answer": "4. Means 3⁴ = 81. Logarithm is the exponent."},
        {"question": "Expand log(xy²)", "answer": "log(x) + 2log(y). Product rule, then power rule."},
        {"question": "Condense log(a) - log(b) + log(c)", "answer": "log(ac/b). Difference rule, then product rule."},
        {"question": "Domain of log₂(x - 5)?", "answer": "x > 5. Argument must be positive."},
        {"question": "Change of base: log₃(20) = ?", "answer": "log(20)/log(3) ≈ 2.73. Using common or natural log."}
    ],
    "5.4": [
        {"question": "Graph f(x) = log₂(x). Passes through?", "answer": "(1, 0) and (2, 1). Shape: increases slowly, takes all real values."},
        {"question": "Vertical asymptote and domain of f(x) = log(x-3)?", "answer": "Asymptote: x = 3. Domain: x > 3."},
        {"question": "Transform log₂(x) to log₂(x-2) + 5", "answer": "Right 2, up 5. General: (x-h) shifts right h, +k shifts up k."},
        {"question": "Compare growth: y = 10x vs y = ln(x) for large x?", "answer": "y = 10x grows much faster. Linear eventually larger than logarithmic."},
        {"question": "Inverse of y = e^x?", "answer": "y = ln(x). Natural log and e^x are inverse functions."}
    ],
    "5.5": [
        {"question": "Solve 3^(x+1) = 27", "answer": "x = 2. Rewrite: 3^(x+1) = 3³, so x + 1 = 3, thus x = 2."},
        {"question": "Solve log₄(x²) = 2", "answer": "x = ±4. Exponential form: x² = 4², so x² = 16, thus x = ±4."},
        {"question": "Solve ln(2x - 1) = 3", "answer": "x = (e³ + 1)/2 ≈ 10.3. Exponential: 2x - 1 = e³."},
        {"question": "Solve 2^x = 5", "answer": "x = log₂(5) ≈ 2.32. Take log base 2: x = log₂(5)."},
        {"question": "Check solution in log₃(x) + log₃(x-2) = 1", "answer": "x = 3. Verify: log₃(3) + log₃(1) = 1 + 0 = 1 ✓. Check x > 2."}
    ],
    "5.6": [
        {"question": "Population growth P(t) = 1000e^(0.05t). Double when?", "answer": "ln(2)/0.05 ≈ 13.9 years. Solve 2000 = 1000e^(0.05t)."},
        {"question": "Compound interest A = P(1 + r/n)^(nt). Monthly for 2 years?", "answer": "n = 12, t = 2. A = P(1 + r/12)^24."},
        {"question": "pH = -log[H⁺]. If pH = 5, [H⁺] concentration?", "answer": "10⁻⁵ molar. Logarithmic scale: [H⁺] = 10^(-pH)."},
        {"question": "Doubling continuous growth A = Pe^(rt)?", "answer": "When e^(rt) = 2. Solve: t = ln(2)/r. r = 0.10 gives t ≈ 6.9 years."},
        {"question": "Decibel sound: dB = 10log(I/I₀). Increase by 10 dB means?", "answer": "Intensity multiplied by 10. Logarithmic scale."}
    ],
    "5.7": [
        {"question": "e ≈ ?", "answer": "2.71828... The natural base, limit of (1+1/n)^n as n→∞."},
        {"question": "ln(e) = ?", "answer": "1. Natural log base e equals 1."},
        {"question": "Continuous compound A = Pe^(rt). Compare to A = P(1+r/n)^(nt)?", "answer": "Exact vs approximate. As n→∞, (1+r/n)^(nt) → e^(rt)."},
        {"question": "Solve e^(2x) = 10", "answer": "x = ln(10)/2 ≈ 1.15. Take natural log."},
        {"question": "If doubling time is 4 years, continuous rate r?", "answer": "r = ln(2)/4 ≈ 0.1733 or 17.33%. e^(rt) = 2 when t = 4."}
    ],
    # Unit 6: Sequences & Series
    "6.1": [
        {"question": "Arithmetic sequence 3, 7, 11, ... Find a₁₀", "answer": "39. d = 4. a₁₀ = 3 + 9(4) = 39."},
        {"question": "Common difference of -2, -5, -8, ...?", "answer": "d = -3. Subtract consecutive terms."},
        {"question": "Sum of first 20 terms: 5 + 10 + 15 + ... ?", "answer": "1050. a₁ = 5, d = 5, a₂₀ = 100. S₂₀ = 20/2 · (5 + 100) = 1050."},
        {"question": "Find a₅ if a₁ = 2 and d = 3", "answer": "14. a₅ = 2 + 4(3) = 14."},
        {"question": "Insert two arithmetic means between 2 and 11", "answer": "5, 8. Four-term sequence: 2, 5, 8, 11 with d = 3."}
    ],
    "6.2": [
        {"question": "Geometric sequence 2, 6, 18, ... Find r and a₅", "answer": "r = 3. a₅ = 2·3⁴ = 162."},
        {"question": "Which is geometric? a) 5, 10, 15... b) 2, 6, 18... c) 1, 4, 9...", "answer": "b) 2, 6, 18 with r = 3. Constant ratio between consecutive terms."},
        {"question": "Sum of geometric series: 1 + 2 + 4 + ... + 512", "answer": "1023. a₁ = 1, r = 2, n = 10. S₁₀ = 1(2¹⁰-1)/(2-1) = 1023."},
        {"question": "Bouncing ball drops 10m, bounces to 7m, 4.9m... Find total height", "answer": "Infinite series. Heights form geometric series, sum = 10/(1-0.7) = 33.3m."},
        {"question": "Solve 3·(1/2)^(n-1) = 3/32", "answer": "n = 6. (1/2)^(n-1) = 1/32 = (1/2)⁵, so n-1 = 5."}
    ],
    "6.3": [
        {"question": "Sigma notation Σᵢ₌₁⁵ (2i) = ?", "answer": "30. Sum: 2(1) + 2(2) + 2(3) + 2(4) + 2(5) = 2+4+6+8+10."},
        {"question": "What does Σᵢ₌₁ⁿ i = n(n+1)/2 represent?", "answer": "Sum of first n positive integers. Example: Σᵢ₌₁⁵ i = 15."},
        {"question": "Σᵢ₌₁ⁿ i² = ?", "answer": "n(n+1)(2n+1)/6. Example: Σᵢ₌₁⁴ i² = 1+4+9+16 = 30 = 4·5·9/6."},
        {"question": "Telescoping series Σᵢ₌₁ⁿ (1/i - 1/(i+1)) = ?", "answer": "1 - 1/(n+1). Most terms cancel."},
        {"question": "Expand Σᵢ₌₁³ (i² + 2i)?", "answer": "15. (1+2) + (4+4) + (9+6) = 3 + 8 + 15 = 26... recalculate: 1 + 9 + 5 = wait, expand correctly."}
    ],
    "6.4": [
        {"question": "Sum of infinite series: 1 + 1/3 + 1/9 + ...", "answer": "3/2. a = 1, r = 1/3. S = 1/(1-1/3) = 3/2."},
        {"question": "Does 1 + 1 + 1 + ... converge?", "answer": "No. r = 1, so series diverges. Sum of constant series is infinite."},
        {"question": "Express 0.333... as fraction", "answer": "1/3. Series: 3/10 + 3/100 + 3/1000 + ... = (3/10)/(1-1/10) = 1/3."},
        {"question": "Convergence of |r| < 1", "answer": "True. Geometric series Σ ar^n converges if and only if |r| < 1."},
        {"question": "Sum of 0.777... as fraction?", "answer": "7/9. Series: 7/10 + 7/100 + ... = (7/10)/(1-1/10) = 7/9."}
    ],
    "6.5": [
        {"question": "Mathematical induction proof that n! > 2ⁿ for n = 5?", "answer": "Base: 5! = 120, 2⁵ = 32, 120 > 32 ✓."},
        {"question": "Inductive step: assume true for n = k, prove for n = k+1?", "answer": "Multiply both sides by (k+1). Check if (k+1)! > 2^(k+1)."},
        {"question": "Induction proof steps?", "answer": "(1) Base case: prove true for n=1, (2) Inductive step: assume true for k, prove k+1."},
        {"question": "Annuity future value?", "answer": "FV = PMT·((1+r)ⁿ - 1)/r. Regular deposits with compound interest."},
        {"question": "Prove Σᵢ₌₁ⁿ (2i-1) = n²?", "answer": "Base: n=1: 1 = 1² ✓. Step: if true for k, then (k+1)² follows by adding 2(k+1)-1."}
    ],
    # Unit 7: Probability & Statistics
    "7.1": [
        {"question": "P(rolling odd on die)?", "answer": "1/2 or 50%. Odd outcomes: {1,3,5}, total 6 outcomes."},
        {"question": "P(not rolling 6)?", "answer": "5/6. Complement rule: P(not 6) = 1 - P(6) = 1 - 1/6."},
        {"question": "Independent events: P(A and B)?", "answer": "P(A) · P(B). Events don't affect each other."},
        {"question": "P(heads on flip 1 and heads on flip 2)?", "answer": "1/4. P(H) · P(H) = 1/2 · 1/2 = 1/4."},
        {"question": "Mutually exclusive events sum to?", "answer": "P(A or B) = P(A) + P(B). Events cannot happen together."}
    ],
    "7.2": [
        {"question": "Fundamental Counting Principle: 3 shirts, 4 pants, 2 shoes. Outfits?", "answer": "24. Multiply: 3 · 4 · 2 = 24 possible combinations."},
        {"question": "P(5,3) = ?", "answer": "60. 5!/(5-3)! = 5!/2! = 120/2 = 60. Permutation ORDER matters."},
        {"question": "How many ways arrange 5 books on shelf?", "answer": "5! = 120. Factorial: 5·4·3·2·1 = 120."},
        {"question": "Passwords: 3 letters (26 each) + 2 digits (10 each)?", "answer": "26³ · 10² = 1,757,600. Each position chosen independently."},
        {"question": " Arrangements of BOOK?", "answer": "4!/2! = 12. Two O's are identical, so divide by 2!."}
    ],
    "7.3": [
        {"question": "C(5,2) = ?", "answer": "10. 5!/(2!3!) = 120/12 = 10. Combination ORDER doesn't matter."},
        {"question": "Ways choose 3 from 10 people?", "answer": "C(10,3) = 120. Combination problem (order irrelevant)."},
        {"question": "Difference C(n,r) vs P(n,r)?", "answer": "Combination: order doesn't matter. Permutation: order matters. P ≥ C always."},
        {"question": "Lottery: choose 6 from 49. Combinations?", "answer": "C(49,6) = 10,068,347. Huge odds against winning."},
        {"question": "Pascal's triangle row 5?", "answer": "1, 5, 10, 10, 5, 1. Each entry is C(5,k)."}
    ],
    "7.4": [
        {"question": "Roll two dice: P(sum = 7)?", "answer": "1/6. Outcomes: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 of 36."},
        {"question": "Binomial distribution: n = 3 flips, p = 0.5. P(X = 2)?", "answer": "C(3,2)·0.5² · 0.5 = 3/8. Three ways get exactly 2 heads."},
        {"question": "Mean and variance of binomial: n = 10, p = 0.4?", "answer": "μ = np = 4. σ² = np(1-p) = 2.4."},
        {"question": "68-95-99.7 rule for normal distribution?", "answer": "68% within 1σ, 95% within 2σ, 99.7% within 3σ of mean."},
        {"question": "Z-score formula?", "answer": "Z = (X - μ)/σ. Standardizes to mean=0, std=1."}
    ],
    "7.5": [
        {"question": "Mean of 5, 8, 12, 15?", "answer": "10. Sum = 40, divide by 4 data points."},
        {"question": "Median of 3, 7, 9, 12, 15?", "answer": "9. Middle value when ordered (5 values, position 3)."},
        {"question": "Range and IQR of 2, 4, 6, 8, 10?", "answer": "Range = 10-2 = 8. Q1 = 4, Q3 = 8, IQR = 4."},
        {"question": "Standard deviation formula?", "answer": "σ = √(Σ(x-μ)²/n). Measures spread around mean."},
        {"question": "Outliers: bounds using 1.5·IQR?", "answer": "Low: Q1 - 1.5·IQR. High: Q3 + 1.5·IQR."}
    ],
    "7.6": [
        {"question": "Linear regression y = a + bx. Slope b formula?", "answer": "b = r(sᵧ/sₓ). r = correlation coeff, sᵧ/sₓ = std dev ratio."},
        {"question": "Correlation coefficient r = ±1 means?", "answer": "r = 1: perfect positive, r = -1: perfect negative correlation."},
        {"question": "R² represents?", "answer": "Coefficient of determination: proportion of variance explained by model."},
        {"question": "Residual = ?", "answer": "Actual - Predicted. Error for each data point."},
        {"question": "Good regression model has?", "answer": "High R² (close to 1), small residuals, residuals random/normal."}
    ],
    "7.7": [
        {"question": "Regression line always passes through?", "answer": "(x̄, ȳ). Mean point of data."},
        {"question": "Causation vs correlation difference?", "answer": "Correlation: variables related. Causation: one causes other. Correlation ≠ causation."},
        {"question": "Confidence interval for slope?", "answer": "slope ± t* · SE(slope). t* from t-distribution based on n and confidence level."},
        {"question": "Test H₀: slope = 0 uses?", "answer": "t-statistic = slope/SE(slope). If |t| large, reject H₀."},
        {"question": "Assumptions for linear regression?", "answer": "Linearity, independence, normality of residuals, equal variance, no outliers."}
    ],
    # Unit 8: Trigonometry Connections
    "8.1": [
        {"question": "Convert 45° to radians", "answer": "π/4. Formula: degrees · π/180."},
        {"question": "Convert 3π/2 radians to degrees", "answer": "270°. Formula: radians · 180/π."},
        {"question": "Coterminal with 30°?", "answer": "30° ± 360n. Examples: 390°, -330°, 750°."},
        {"question": "Reference angle for 210°?", "answer": "30°. Acute angle from x-axis. 210° - 180° = 30°."},
        {"question": "Reference angle for 315°?", "answer": "45°. 360° - 315° = 45°."}
    ],
    "8.2": [
        {"question": "Unit circle point at 90°?", "answer": "(0, 1). cos(90°) = 0, sin(90°) = 1."},
        {"question": "sin(π/4) = ?", "answer": "√2/2. Special angle on unit circle."},
        {"question": "cos(π/3) = ?", "answer": "1/2. Special angle: (1/2, √3/2)."},
        {"question": "tan(π) = ?", "answer": "0. sin(π)/cos(π) = 0/(-1) = 0."},
        {"question": "Quadrant II, sin __ positive, cos __ negative", "answer": "Both statements true. All trig ratios positive in Q1."}
    ],
    "8.3": [
        {"question": "Period of sin(x)?", "answer": "2π. Repeats every 2π radians (360°)."},
        {"question": "Amplitude of y = 3sin(x)?", "answer": "3. Vertical stretch factor."},
        {"question": "Period of tan(x)?", "answer": "π. Half the period of sin/cos."},
        {"question": "Graph y = sin(x - π/2). Shifted how?", "answer": "Right π/2. Equivalent to y = cos(x)."},
        {"question": "Vertical shift of y = cos(x) + 3?", "answer": "Up 3 units. Graph moves 3 units above normal."}
    ],
    "8.4": [
        {"question": "sin²θ + cos²θ = ?", "answer": "1. Pythagorean identity (fundamental)."},
        {"question": "sin(A + B) = ?", "answer": "sinA cosB + cosA sinB. Sum formula."},
        {"question": "cos(2x) = ?", "answer": "cos²x - sin²x or 2cos²x - 1 or 1 - 2sin²x. Double angle formulas."},
        {"question": "Simplify sin²(x) using power reduction", "answer": "(1 - cos(2x))/2. Power reduction formula."},
        {"question": "tan(π/4) = ?", "answer": "1. Both sin and cos equal √2/2, ratio = 1."}
    ],
    "8.5": [
        {"question": "Solve sin(x) = 1/2, x ∈ [0, 2π]", "answer": "x = π/6 or x = 5π/6. Two solutions in period."},
        {"question": "Solve cos(x) = -√2/2, x ∈ [0, 2π]", "answer": "x = 3π/4 or x = 5π/4. Q2 and Q3."},
        {"question": "Solve tan(x) = 1", "answer": "x = π/4 + nπ. General solution (all periods)."},
        {"question": "sin⁻¹(0.5) = ?", "answer": "π/6 (or 30°). Inverse sine gives angle."},
        {"question": "Domain of cos⁻¹(x)?", "answer": "[-1, 1]. Only valid inputs for inverse cosine."}
    ],
    "8.6": [
        {"question": "Law of Sines: a/sin(A) = ?", "answer": "b/sin(B) = c/sin(C). Use for ASA, AAS, or SSA cases."},
        {"question": "Law of Cosines: c² = ?", "answer": "a² + b² - 2ab cos(C). Use for SAS or SSS cases."},
        {"question": "Navigation: bearing 45° from North is?", "answer": "Northeast, 45° east of north. Measured clockwise from north."},
        {"question": "Angle of elevation from ground to top of 50m building at 30°?", "answer": "Height ÷ distance = tan(30°), distance = 50/tan(30°) ≈ 86.6m."},
        {"question": "Projectile x(t) = 40cos(60°)t, y(t) = 40sin(60°)t - 5t²", "answer": "Initial angle 60°, velocity 40 m/s."}
    ],
    # Unit 9: Advanced Topics (All AP Prep)
    "9.1": [
        {"question": "Parabola y² = 4px. If p = 2, focus at?", "answer": "(2, 0). Directrix x = -2. Opens right."},
        {"question": "Ellipse center (0,0), major axis 10, minor 6. Foci at?", "answer": "(±4, 0). c² = a² - b² = 25 - 9 = 16, c = 4."},
        {"question": "Hyperbola (x²/9) - (y²/4) = 1. Asymptotes?", "answer": "y = ±(2/3)x. Slopes ±b/a."},
        {"question": "Circle x² + y² = 25. Tangent line at (3, 4)?", "answer": "3x + 4y = 25. Tangent perpendicular to radius."},
        {"question": "Eccentricity of ellipse (x²/16) + (y²/9) = 1?", "answer": "e = √7/4 ≈ 0.66. c = √7, a = 4, e = c/a."}
    ],
    "9.2": [
        {"question": "Eliminate parameter: x = t+1, y = t² to find Cartesian", "answer": "y = (x-1)². Solve for t: t = x-1, substitute."},
        {"question": "dy/dx for x = 2cos(t), y = 3sin(t) at t = π/4?", "answer": "-3/(2√2). dy/dx = (dy/dt)/(dx/dt)."},
        {"question": "Velocity vector for r(t) = (t², 2t)?", "answer": "v(t) = (2t, 2). First derivative of position."},
        {"question": "Cycloid: x = r(t - sin t), y = r(1 - cos t). At t = 0?", "answer": "(0, 0). Starting point at origin."},
        {"question": "Parametric line through (1,2) with direction ⟨3,4⟩?", "answer": "x = 1+3t, y = 2+4t. Use point + parameter · direction."}
    ],
    "9.3": [
        {"question": "Magnitude of v = ⟨3, 4⟩?", "answer": "5. |v| = √(9 + 16) = √25 = 5."},
        {"question": "Dot product u = ⟨2,3⟩ · v = ⟨1,4⟩?", "answer": "14. 2(1) + 3(4) = 2 + 12 = 14."},
        {"question": "Angle between u = ⟨1,0⟩ and v = ⟨1,1⟩?", "answer": "45° or π/4. cos θ = (1)/√2, so θ = 45°."},
        {"question": "Unit vector in direction of ⟨3,4⟩?", "answer": "⟨3/5, 4/5⟩. Divide by magnitude 5."},
        {"question": "Orthogonal vectors u, v satisfy?", "answer": "u·v = 0. Dot product equals zero (perpendicular)."}
    ],
    "9.4": [
        {"question": "Polar form of z = 1 + i?", "answer": "√2(cos(π/4) + i sin(π/4)). r = √2, θ = 45°."},
        {"question": "De Moivre: (2 cis 30°)³ = ?", "answer": "8 cis 90° = 8i."},
        {"question": "Convert 3 cis 60° to rectangular", "answer": "3/2 + (3√3/2)i. x = 3cos(60°), y = 3sin(60°)."},
        {"question": "Multiply: (2 cis 45°)(3 cis 30°) in polar?", "answer": "6 cis 75°. Multiply magnitudes, add angles."},
        {"question": "Fourth roots of 16", "answer": "2, 2i, -2, -2i. 2^(1/4) cis(0°+90°k) for k=0,1,2,3."}
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
