#!/usr/bin/env python3
"""
Update all quiz files with 7 multiple-choice questions for Units 4-9.
"""

import os
import re

# Quiz content for Units 4-9
QUIZ_CONTENT = {
    "4.1": [
        ("Simplify x²/(x²−1) · (x−1)/x", ["x/(x+1)", "(x−1)/x", "x/(x−1)", "1/(x+1)"], 0),
        ("Domain (x−3)/(x²−4)", ["all except x=2,−2", "all except x=3", "all x", "x > 0"], 0),
        ("Add 1/x + 1/(x+1) = ?", ["(2x+1)/(x²+x)", "(x+1)/(x²+x)", "2/(x²+x)", "(2x+1)/(x+1)"], 0),
        ("Subtract 2/(x−1) − 1/(x+1)", ["(x+3)/((x−1)(x+1))", "(x−3)/((x−1)(x+1))", "1/(x−1)", "(x+3)/(x²−1)"], 0),
        ("Multiply (x+2)/(x−1) · (x−1)/(x+3)", ["(x+2)/(x+3)", "1", "(x+2)/(x−3)", "x/(x+1)"], 0),
        ("Divide (x²−4)/(x+1) ÷ (x−2)/(x+1)", ["(x+2)", "(x−2)", "x+1", "1"], 0),
        ("Simplify (1 + 1/x)/(1 − 1/x)", ["(x+1)/(x−1)", "(x−1)/(x+1)", "1", "x"], 0),
    ],
    "4.2": [
        ("Asymptote of (2x+1)/(x−3)", ["x=3", "y=2x", "y=1/3", "y=0"], 0),
        ("Vertical asymptote f(x)=(x+1)/(x²−9)", ["x=3, x=−3", "x=3, x=1", "x=−1", "none"], 0),
        ("Horizontal asymptote (3x²−1)/(2x²+5)", ["y=3/2", "y=0", "y=1", "y=2/3"], 0),
        ("Degrees num > denom means", ["no horiz asymp", "horiz asymp y=0", "slant asymp", "x-asymp"], 2),
        ("Horiz asymp (x−2)/(x³+1)", ["y=0", "y=1", "y=−2", "none"], 0),
        ("Degree num < denom asymp", ["y=0", "y=undefined", "no asymp", "y=∞"], 0),
        ("Removable discontinuity (x²−1)/(x−1)", ["x=1", "x=0", "x=−1", "none"], 0),
    ],
    "4.3": [
        ("Solve 1/x = 1/(x+2)", ["x=−1 (no sol)", "x=1", "x=0", "x=−2"], 0),
        ("Solve 2/(x−1)=3/(x+1)", ["x=5", "x=1", "x=−1", "x=0"], 0),
        ("Solve (x+2)/(x) = 3", ["x=−1", "x=1", "x=2", "x=−2"], 0),
        ("Extraneous solution?", ["doesn't satisfy orig", "satisfies", "always valid", "none"], 0),
        ("Solve 5/x + 2 = 7", ["x=1", "x=2", "x=5/2", "x=5"], 0),
        ("Check simplify (x²−4)/(x−2)=x+2", ["valid if x≠2", "always valid", "never valid", "complex"], 0),
        ("Reciprocal equation 1/x = 2", ["x=1/2", "x=2", "x=−1/2", "no solution"], 0),
    ],
    "4.4": [
        ("Inequality 1/x > 0 solution?", ["x > 0", "x < 0", "all x", "no solution"], 0),
        ("Solve (x−2)/(x+1) ≥ 0", ["−1 < x ≤ 2", "x ≤ −1 or x ≥ 2", "x ≥ 2", "all x"], 1),
        ("Solve 1/(x−3) < 2", ["x < (7/2)", "x ∈ (3, 7/2)", "3 < x < 7/2 or x < 3", "no sol"], 2),
        ("Test point inequality?", ["between/outside zeros", "at zeros", "at asymp", "midpoint"], 0),
        ("Sign analysis (x+1)/(x−2)", ["(−∞,−1): pos, (−1,2): neg, (2,∞): pos", "all neg", "all pos", "mixed"], 0),
        ("Solve (2x)/(x−1) ≤ 1", ["x < 1 or x ≥ 2", "1 < x ≤ 2", "x ≤ 1 or x ≥ 2", "x ≥ 1"], 0),
        ("Boundary: included/excluded", ["undefined expr", "undefined value", "both possible", "none"], 0),
    ],
    "4.5": [
        ("Combine (x+1)/(x²−4) + 3/(x−2)", ["(4x+7)/((x−2)(x+2))", "1/(x−2)", "(x+1)/(x+2)", "(3x+7)/(x²−4)"], 0),
        ("LCD (x+1) and (x²−1)", ["(x−1)(x+1)²", "(x−1)(x+1)", "(x+1)²", "(x−1)(x+1)"], 1),
        ("Simplify (2−1/x)/(1+1/x)", ["(2x−1)/(x+1)", "(x−2)/(x+1)", "2", "(2x−1)/1"], 0),
        ("Complex fraction (1/(x+1))/(1/(x−1))", ["(x−1)/(x+1)", "(x+1)/(x−1)", "1", "x"], 0),
        ("Add rational 3/(x+2) + 2/(x−2)", ["(5x−2)/((x+2)(x−2))", "(5x)/(x²−4)", "(5x+2)/(x²−4)", "(5x−2)/(x−2)"], 0),
        ("Subtract 1/(x−1) − x/(x+1)", ["(−x²−2x+1)/((x−1)(x+1))", "−1", "(−x² + 1)/(x²−1)", "none"], 0),
        ("Multiply (x²−1)/(x) · x/(x+1)", ["(x−1)", "(x+1)", "x", "1"], 0),
    ],
    "4.6": [
        ("Work: A does 1/5, B does 1/4 per day. Combined?", ["1/9 per day", "9/20 per day", "5/9 per day", "4/5 per day"], 1),
        ("Pump A: 1/6 min, B: 1/9 min. Fill?", ["18/5 min", "15/18 min", "9 min", "2.5 min"], 0),
        ("Speed ratio 60 mph vs 40 mph, 30 mi. Time diff?", ["0.75 hrs", "0.5 hrs", "1 hr", "1.5 hrs"], 0),
        ("Work rate equation L work, t time", ["1/rate", "rate·t=L", "L/t = rate", "all above"], 2),
        ("Two workers complete 1 job: x days A, y days B", ["combined = 1/x + 1/y", "combined = xy", "combined = x/y", "combined = x+y"], 0),
        ("Concentration mixture", ["liters × % = amount", "liters + % = amount", "liters/% = amount", "none"], 0),
        ("Rate problem d=rt setup", ["adjust for direction", "add rates/subtract", "distance formula", "all"], 3),
    ],
    "5.1": [
        ("Evaluate f(x)=2^x at x=3", ["8", "6", "2", "12"], 0),
        ("Solve 3^x = 81", ["x=4", "x=3", "x=2", "x=5"], 0),
        ("Solve 2^x = 32", ["x=5", "x=4", "x=6", "x=3"], 0),
        ("Growth factor in A=P(1.05)^t", ["1.05", "0.05", "5%", "105%"], 0),
        ("Decay model C(t)=200(0.8)^t", ["decay rate 20%", "decay rate 80%", "growth 20%", "no decay"], 0),
        ("Domain of f(x)=2^(1/x)", ["all except 0", "x > 0", "all x", "x ≠ 1"], 0),
        ("Evaluate 5^(-x) at x=2", ["1/25", "25", "−1/25", "5/2"], 0),
    ],
    "5.2": [
        ("log₂ 32 = ?", ["5", "4", "6", "3"], 0),
        ("log₃ 27 = ?", ["3", "2", "4", "9"], 0),
        ("Solve log x = 2", ["x=100", "x=10", "x=2", "x=20"], 0),
        ("log_b x = y means", ["b^y = x", "x^y = b", "y^b = x", "b·y = x"], 0),
        ("Domain of ln(x−3)", ["x > 3", "x ≥ 3", "all x", "x ≠ 3"], 0),
        ("ln e = ?", ["1", "0", "e", "−1"], 0),
        ("log solution 10^x = 1000", ["x=3", "x=2", "x=1", "x=4"], 0),
    ],
    "5.3": [
        ("ln 2 + ln 3 = ?", ["ln 6", "ln 5", "ln 2/3", "ln 2·ln 3"], 0),
        ("ln 8 − ln 2 = ?", ["ln 4", "ln 6", "ln 3", "ln 16"], 0),
        ("3 ln x = ?", ["ln x³", "ln 3x", "(ln x)³", "3(ln x)"], 0),
        ("log_b x + log_b y = ?", ["log_b(xy)", "log_b(x+y)", "log_b(x/y)", "log_b x·log_b y"], 0),
        ("log_b(x/y) = ?", ["log_b x − log_b y", "log_b x + log_b y", "log_b x/log_b y", "(log_b x)−y"], 0),
        ("Change base log₂ 5 to ln", ["ln 5/ln 2", "ln 2/ln 5", "ln 5·ln 2", "ln(5/2)"], 0),
        ("ln(√x) = ?", ["(1/2)ln x", "(1/2)·(ln 1+ln x)", "ln x/2", "both equal"], 0),
    ],
    "5.4": [
        ("Solve 2^x = 50", ["x = log₂ 50", "x = log₅₀ 2", "x = 25", "x = 5"], 0),
        ("Solve e^x = 10", ["x = ln 10", "x = log 10", "x = log₁₀ e", "x = e/10"], 0),
        ("Solve log(2x+1)=1", ["x=4.5", "x=9", "x=5", "x=−0.5"], 0),
        ("Solve ln(x−2)=3", ["x=e³+2", "x=e³", "x=3e+2", "x=e+2"], 0),
        ("Solve 3^(x+1)=27", ["x=2", "x=1", "x=3", "x=−1"], 0),
        ("Check solution ln(x−1)=2", ["x = e²+1", "x = 2e+1", "x = e+1", "x = e²−1"], 0),
        ("Extraneous solution occurs in?", ["logarithmic eq", "always", "never", "same as others"], 0),
    ],
    "5.5": [
        ("Half-life model M(t)=500(0.5)^(t/10)", ["after 10s: 250", "after 10s: 375", "after 5s: 250", "after 20s: 250"], 0),
        ("Decay continuous: N=N₀e^(−λt)", ["λ > 0", "λ < 0", "λ = 0", "any λ"], 0),
        ("Carbon-14 half-life?", ["5730 yrs", "57300 yrs", "573 yrs", "10000 yrs"], 0),
        ("pH formula −log[H⁺]", ["logarithmic scale", "linear scale", "exponential", "none"], 0),
        ("Exponential growth A=P·e^(rt)", ["r > 0", "r < 0", "r = 0", "any r"], 0),
        ("Population 1000, grow 5% annually. After?", ["1000(1.05)^t", "1000·1.05·t", "1000·0.05·t", "1000+505t"], 0),
        ("Radioactive decay time?", ["increases with mass", "independent of mass", "depends on temp", "instantaneous"], 1),
    ],
    "5.6": [
        ("Solve 4^x = 2", ["x=1/2", "x=2", "x=1/4", "x=4"], 0),
        ("Solve log₄(x−1)=2", ["x=17", "x=16", "x=15", "x=9"], 0),
        ("Solve ln(2x)−ln(x)=ln 3", ["x=3", "x=1", "x=−3", "no solution"], 0),
        ("From 2^(x−1)=64 find x", ["x=7", "x=6", "x=8", "x=5"], 0),
        ("Check e^(ln x)=x true?", ["yes, x > 0", "no", "only x > 1", "x ≠ 0"], 0),
        ("Solve 10^x = 1/100", ["x=−2", "x=2", "x=−1/2", "x=−0.01"], 0),
        ("Mixed ln and exp? Both sides", ["take ln", "exponentiate", "separate", "varies"], 2),
    ],
    "6.1": [
        ("Find 5th term: 2, 5, 8, 11, ...", ["14", "17", "16", "15"], 0),
        ("Common difference of −3, −1, 1, 3", ["2", "−2", "4", "1"], 0),
        ("General term aₙ if a₁=3, d=4", ["aₙ=4n−1", "aₙ=3n+4", "aₙ=4n+3", "aₙ=3n−4"], 0),
        ("Arithmetic a₁=1, a₅=13. Find d", ["d=3", "d=2", "d=4", "d=5"], 0),
        ("Find a₁₀ if a₁=5, d=−2", ["−15", "−13", "−5", "25"], 0),
        ("20th term if pattern '+5': first 3", ["95", "100", "105", "110"], 0),
        ("Sequence with pattern?", ["arithmetic", "constant", "quadratic", "all linear"], 0),
    ],
    "6.2": [
        ("Sum of 1+2+3+...+10", ["55", "50", "45", "60"], 0),
        ("Arithmetic sum formula", ["S = n(a₁+aₙ)/2", "S = n·a₁·d", "S = n·aₙ", "S = a₁/(1−r)"], 0),
        ("Sum first 12 terms if a₁=3, d=2", ["168", "180", "192", "204"], 0),
        ("Sum 2+4+6+...+20 terms?", ["110", "100", "120", "140"], 0),
        ("Arithmetic series 5+10+15+...+100", ["1050", "1100", "1150", "1200"], 0),
        ("Find n if sum = 210, a₁=3, d=3", ["n=12", "n=10", "n=14", "n=15"], 0),
        ("Common diff 2, terms 15, sum?", ["S = 15a₁+210", "S = 15a₁+14d", "S = nS/2", "varies"], 0),
    ],
    "6.3": [
        ("Geometric: 1, 2, 4, 8. Ratio r = ?", ["2", "1", "4", "1/2"], 0),
        ("5th term r=3, a₁=2", ["162", "81", "243", "486"], 0),
        ("General term aₙ = ?", ["a₁·r^(n−1)", "a₁·r^n", "a₁+d(n−1)", "a₁/(1−r)"], 0),
        ("Geometric a₁=1, a₃=4. Find r", ["±2", "4", "3", "1/2"], 0),
        ("Sum ∞ geom |r| < 1: S = ?", ["a₁/(1−r)", "a₁·r", "a₁/(1+r)", "∞"], 0),
        ("Converges if", ["|r| < 1", "|r| > 1", "r = 1", "always"], 0),
        ("Sum 0.5 + 0.25 + 0.125 + ...?", ["1", "0.75", "2", "∞"], 0),
    ],
    "6.4": [
        ("∑(i=1 to 5) i² = ?", ["55", "35", "25", "15"], 0),
        ("Sigma ∑ notation means", ["summation", "product", "sequence", "difference"], 0),
        ("∑(i=1 to n) i = ?", ["n(n+1)/2", "n!", "2n", "n²"], 0),
        ("Express 1+4+9+16 as sum", ["∑i² from 1 to 4", "∑i from 1 to 4", "∑2i", "∑(i+1)²"], 0),
        ("∑(k=1 to 20) k³ = ?", ["44100", "41000", "42000", "45000"], 0),
        ("Index variable in ∑ is", ["dummy variable", "fixed", "constant", "limit"], 0),
        ("Summation upper index", ["inclusive", "exclusive", "depends", "none"], 0),
    ],
    "7.1": [
        ("Roll die, P(even) = ?", ["1/2", "1/3", "2/3", "1/6"], 0),
        ("Cards 52, P(red) = ?", ["1/2", "1/4", "1/13", "1/26"], 0),
        ("Complement P(not A) = ?", ["1 − P(A)", "P(A)", "1/P(A)", "−P(A)"], 0),
        ("Independent events P(both) = ?", ["P(A)·P(B)", "P(A)+P(B)", "P(A∪B)", "P(A|B)"], 0),
        ("Mutually exclusive P(A or B) = ?", ["P(A)+P(B)", "P(A)·P(B)", "1−P(A)+P(B)", "P(A)+P(B)−P(A∩B)"], 0),
        ("Sample space die", ["1,2,3,4,5,6", "0,1", "any", "1 to ∞"], 0),
        ("P(impossible event) = ?", ["0", "1", "0.5", "undefined"], 0),
    ],
    "7.2": [
        ("P(A and B) independent = ?", ["P(A)·P(B)", "P(A)+P(B)−P(A∩B)", "P(A|B)·P(B)", "1−P(A)·P(B)"], 0),
        ("Conditional P(A|B) = ?", ["P(A∩B)/P(B)", "P(A)·P(B)", "P(A)+P(B)", "P(B|A)"], 0),
        ("Deck: P(2nd ace|1st ace)?", ["3/51", "4/52", "4/51", "3/52"], 0),
        ("Dependent sample w/o replace", ["probability changes", "stays same", "→ 0", "→ 1"], 0),
        ("Tree diagram use", ["conditional prob", "all types", "independent", "none"], 0),
        ("Bayes theorem setup", ["P(A|B)=P(B|A)·P(A)/P(B)", "P(A)=P(B|A)", "direct only", "impossible"], 0),
        ("Medical test 95% accurate:", ["might be false pos", "always accurate", "impossible", "no calc"], 0),
    ],
    "7.3": [
        ("n! read as", ["n factorial", "n value", "n combinations", "n factorial inverse"], 0),
        ("5! = ?", ["120", "25", "15", "10"], 0),
        ("Permutations nPr = ?", ["n!/(n−r)!", "n!/r!", "n!/(r!·(n−r)!)", "n·r"], 0),
        ("Combinations nCr = ?", ["n!/[r!(n−r)!]", "n!/(n−r)!", "n!/r!", "n+r!"], 0),
        ("Choose 3 from 5", ["10", "20", "60", "15"], 0),
        ("Arrangements 5 people in line", ["120", "25", "5", "10"], 0),
        ("Order matters?", ["permutation", "combination", "both", "neither"], 0),
    ],
    "7.4": [
        ("Binomial P(X=k) = ?", ["C(n,k)p^k(1−p)^(n−k)", "n·p", "C(n,k)", "p^k"], 0),
        ("n=5, p=0.5, P(X=2)?", ["C(5,2)(0.5)⁵", "0.5²", "5·0.2", "0.1"], 0),
        ("Binomial mean μ = ?", ["n·p", "n·p·(1−p)", "√(n·p)", "p"], 0),
        ("Binomial variance σ² = ?", ["n·p·(1−p)", "n·p", "(1−p)", "p²"], 0),
        ("Standard dev σ = ?", ["√(n·p·(1−p))", "n·p", "n·p·(1−p)", "p(1−p)"], 0),
        ("Binomial requirement:", ["fixed n, p", "any dist", "order matters", "dependent"], 0),
        ("Success/failure independent?", ["yes important", "no", "depends", "undefined"], 0),
    ],
    "7.5": [
        ("Normal dist mean μ", ["center", "spread", "probability", "limit"], 0),
        ("Normal std dev σ", ["spread", "mean", "skew", "kurtosis"], 0),
        ("68-95-99.7 rule: 1 σ", ["≈68%", "≈95%", "≈99.7%", "≈50%"], 0),
        ("Z-score formula", ["(x−μ)/σ", "(μ−x)/σ", "σ/(x−μ)", "x/μ"], 0),
        ("Normal curve symmetric about", ["mean μ", "0", "σ", "1"], 0),
        ("P(Z < 0) in standard normal", ["0.5", "0.68", "0.95", "1"], 0),
        ("Standard normal μ", ["0", "1", "0.5", "varies"], 0),
    ],
    "7.6": [
        ("Margin error E = ?", ["z*·σ/√n", "z*·σ", "σ/√n", "z·n"], 0),
        ("Confidence interval estimate", ["point ± margin", "point", "only lower", "only upper"], 0),
        ("95% CI z* value", ["1.96", "1.645", "2.576", "1.28"], 0),
        ("Sample size increase", ["narrows CI", "widens CI", "no effect", "doubles"], 0),
        ("σ unknown use", ["t-distribution", "z-dist", "binomial", "none"], 0),
        ("Hypothesis test H₀", ["null hypothesis", "alternate", "both", "neither"], 0),
        ("P-value < α reject", ["H₀", "H₁", "both", "neither"], 0),
    ],
    "7.7": [
        ("Linear reg line best fits", ["least squares", "maximum", "average", "visual"], 0),
        ("Correlation r = ?", ["−1 to +1", "0 to 1", "−1 to 0", "0 to 100"], 0),
        ("r = 0.9 means", ["strong positive", "weak", "negative", "no relation"], 0),
        ("r² = coefficient", ["determination", "correlation", "regression", "fit"], 0),
        ("LSRL y = a + bx slope b", ["rise/run", "y-intercept", "correlation", "variance"], 0),
        ("Predict outside range called", ["extrapolation", "interpolation", "residual", "error"], 0),
        ("Slope interpretation", ["change in y per x", "y when x=0", "goodness fit", "correlation"], 0),
    ],
    "8.1": [
        ("Convert 120° to radians", ["2π/3", "π/3", "2π/6", "3π/2"], 0),
        ("Convert 3π/4 to degrees", ["135°", "90°", "180°", "45°"], 0),
        ("Radian unit circle circumference", ["2π", "π", "2πr", "πd"], 0),
        ("Arc length s = ?", ["r·θ", "r+θ", "r/θ", "θ²r"], 0),
        ("Central angle 2 rad, r=5", ["s=10", "s=2/5", "s=7", "s=25"], 0),
        ("Reference angle 135°", ["45°", "35°", "55°", "90°"], 0),
        ("Coterminal 30° angle", ["390°", "−330°", "both", "neither"], 2),
    ],
    "8.2": [
        ("sin(π/6) = ?", ["1/2", "√3/2", "√2/2", "1"], 0),
        ("cos(π/4) = ?", ["√2/2", "1/2", "√3/2", "1"], 0),
        ("tan(π/3) = ?", ["√3", "1", "√3/3", "1/2"], 0),
        ("Pythagorean sin²θ+cos²θ = ?", ["1", "0", "2", "π"], 0),
        ("Unit circle point (π/2)", ["(0,1)", "(1,0)", "(−1,0)", "(1,1)"], 0),
        ("Reciprocal sec θ = ?", ["1/cos θ", "cos θ", "sin θ", "1/sin θ"], 0),
        ("SOHCAHTOA: CAH means", ["cos = adj/hyp", "sin = opp/hyp", "tan = opp/adj", "all equal"], 0),
    ],
    "8.3": [
        ("Graph y = sin x period", ["2π", "π", "1", "∞"], 0),
        ("Amplitude |A| of 3sin x", ["3", "1", "−3", "1/3"], 0),
        ("Period of sin(2x)", ["π", "2π", "4π", "1"], 0),
        ("Phase shift y = sin(x−π/4)", ["right π/4", "left π/4", "up π/4", "down π/4"], 0),
        ("Vertical shift +2: y = sin x + 2", ["up 2", "down 2", "right 2", "left 2"], 0),
        ("y = −sin x reflect", ["x-axis", "y-axis", "origin", "none"], 0),
        ("Domain sin x", ["all real", "−1 to 1", "[−π,π]", "x ≠ 0"], 0),
    ],
    "8.4": [
        ("Verify sin²x + cos²x", ["= 1", "= 0", "= 2", "≠ const"], 0),
        ("sin 2x = ?", ["2sin x cos x", "2sin x", "sin²x", "sin x/2"], 0),
        ("cos 2x = ?", ["cos²x − sin²x", "cos x − sin x", "2cos²x − 1", "all true"], 3),
        ("Double angle tan", ["2tan x/(1−tan²x)", "2tan x", "tan²x", "none"], 0),
        ("Half angle formula", ["√((1−cos x)/2)", "sin x/2", "cos x/2", "(1−cos x)/sin x"], 0),
        ("Sum sin(A+B) = ?", ["sin A cos B + cos A sin B", "sin A + sin B", "sin(A·B)", "none"], 0),
        ("Difference cos(A−B) = ?", ["cos A cos B + sin A sin B", "cos A − cos B", "cos(A/B)", "none"], 0),
    ],
    "8.5": [
        ("Solve sin x = 1/2, [0,2π]", ["π/6, 5π/6", "0, π", "π/3, 2π/3", "π/2"], 0),
        ("Solve cos x = −1, [0,2π]", ["π", "π/2", "3π/2", "0, 2π"], 0),
        ("Solve tan x = 1, [0,2π]", ["π/4, 5π/4", "π/4", "π/2", "3π/4, 7π/4"], 0),
        ("sin x = 0.5 general solution", ["π/6 + 2πn", "5π/6 + 2πn", "both", "only first"], 2),
        ("Check sin(π/3) = √3/2", ["correct", "incorrect", "maybe", "undefined"], 0),
        ("Inverse sin range", ["[−π/2, π/2]", "[0, π]", "[0, 2π]", "[−π, π]"], 0),
        ("sin⁻¹(1/2) = ?", ["π/6", "π/3", "π/2", "π/4"], 0),
    ],
    "8.6": [
        ("Law of Sines a/sin A = ?", ["b/sin B = c/sin C", "same for all", "(a·b)/sin(A·B)", "none"], 1),
        ("Ambiguous case SSA", ["0, 1, or 2 solns", "always 1", "always 2", "always 0"], 0),
        ("Law of Cosines c² = ?", ["a² + b² − 2ab cos C", "a² + b²", "a² − b²", "(a+b)²"], 0),
        ("Use Cosines when", ["have SAS/SSS", "have SSA", "have AAS", "any config"], 0),
        ("Find C: a=5, b=7, c=8 type", ["SSS use Law Cos", "SAS", "AAS", "ASA"], 0),
        ("Area K = ?", ["(1/2)ab sin C", "ab sin C", "(1/2)ab", "√(ab)"], 0),
        ("Heron A = √[s(s−a)(s−b)(s−c)]", ["when have SSS", "any triangle", "right only", "acute only"], 0),
    ],
    "9.1": [
        ("Circle center (2,3), r=5 equation", ["(x−2)²+(y−3)²=25", "(x+2)²+(y+3)²=25", "x²+y²=25", "none"], 0),
        ("Expand (x−1)² + (y+2)² = 16", ["x² + y² − 2x + 4y = 11", "x² + y² = 16", "x² − 2x + y² + 4y = 11", "none"], 0),
        ("Center/radius from x² + y² − 6x + 8y = 0", ["(3,−4), r=5", "(6,8), r=0", "(3,4), r=5", "(−3,4), r=5"], 0),
        ("Parabola vertex (h,k) form", ["(x−h)² = 4p(y−k)", "x = ay² + by + c", "y² = 4px", "none"], 0),
        ("Ellipse equation standard", ["x²/a² + y²/b² = 1", "x²/a + y²/b = 1", "(x−h)²/a² + (y−k)²/b² = 1", "all"], 2),
        ("Hyperbola x²/a² − y²/b² = 1", ["opens L-R", "opens U-D", "circle", "ellipse"], 0),
        ("Eccentricity ellipse", ["0 < e < 1", "e = 1", "e > 1", "e = 0"], 0),
    ],
    "9.2": [
        ("Conic x²/4 + y²/9 = 1", ["ellipse", "hyperbola", "parabola", "circle"], 0),
        ("Conic y² = 8x", ["parabola", "ellipse", "hyperbola", "circle"], 0),
        ("Conic x² − y² = 4", ["hyperbola", "ellipse", "parabola", "circle"], 0),
        ("Discriminant test B² − 4AC", ["type conic", "foci", "vertices", "eccentricity"], 0),
        ("General 2nd degree equation", ["Ax² + Bxy + Cy² + Dx + Ey + F = 0", "linear combo", "both", "other"], 0),
        ("Rotation eliminate xy term", ["use tan 2α = B/(A−C)", "none exists", "impossible", "needs rotation"], 0),
        ("Standard position (h,k) → translate", ["shift to origin", "change a,b", "change e", "none"], 0),
    ],
    "9.3": [
        ("Parametric x = 3t, y = t², eliminate t", ["y = (x/3)²", "y = 3x²", "y = x²/9", "linear"], 0),
        ("Parametric line t ∈ [0,1]", ["segment", "ray", "line", "curve"], 0),
        ("Curve x = cos t, y = sin t", ["circle x²+y²=1", "ellipse", "line", "parabola"], 0),
        ("Domain x = 2+t, y = 3−2t", ["all t", "t ≥ 0", "t > 2", "none"], 0),
        ("Parametric motion direction", ["parameter direction", "derivative sign", "both", "neither"], 0),
        ("Cycloid curve point on circle", ["traces path", "distance", "velocity", "rotation"], 0),
        ("Convert parametric → rectangular", ["eliminate parameter", "add equations", "solve for t", "both"], 2),
    ],
    "9.4": [
        ("Vector initial/terminal points", ["displacement", "length/direction", "position", "none"], 0),
        ("Magnitude |⟨3,4⟩| = ?", ["5", "7", "1", "12"], 0),
        ("Unit vector ⟨3,4⟩/5 = ?", ["⟨0.6, 0.8⟩", "⟨3/5, 4/5⟩", "both", "neither"], 2),
        ("⟨1,2⟩ + ⟨3,4⟩ = ?", ["⟨4,6⟩", "⟨2,2⟩", "⟨−2,−2⟩", "⟨3,8⟩"], 0),
        ("Dot product ⟨1,2⟩·⟨3,4⟩ = ?", ["11", "7", "12", "3"], 0),
        ("Orthogonal vectors dot prod", ["= 0", "= 1", "= −1", "> 0"], 0),
        ("Angle between vectors", ["cos θ = (u·v)/(|u||v|)", "θ = u+v", "sin θ = u/v", "depends"], 0),
    ],
}

def create_quiz_html_questions(questions):
    """Generate HTML for quiz questions."""
    html_parts = []
    for i, (q_text, options, correct_idx) in enumerate(questions, 1):
        html = f'''            <div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="2">
                <p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{i}. {q_text}</p>
'''
        for j, option in enumerate(options):
            is_correct = "correct" if j == correct_idx else "wrong"
            html += f'''                <label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">
                    <input type="radio" name="q{i}" value="{is_correct}"> {option}
                </label>
'''
        html += f'''                <div class="attempts-indicator"></div>
                <div style="margin-top:1.5rem;">
                    <button type="button" class="action-button" onclick="window.checkQuizAnswer('q{i}', '{is_correct}', this)">Submit Answer</button>
                    <button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>
                </div>
            </div>
'''
        html_parts.append(html)
    return '\n'.join(html_parts)

def update_quiz_file(unit, lesson, questions):
    """Update a quiz file with questions."""
    base_path = "/workspaces/ArisEdu/ArisEdu Project Folder/Algebra2Lessons"
    file_path = f"{base_path}/Unit{unit}/Lesson{unit}.{lesson}_Quiz.html"
    
    if not os.path.exists(file_path):
        print(f"Missing: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Generate new quiz HTML
    quiz_html = create_quiz_html_questions(questions)
    
    # Replace old quiz-question divs (keep form tags)
    pattern = r'(<form id="quiz-form">\s*)(.*?)(\s*</form>)'
    replacement = f'\\1\n{quiz_html}\n                    \\3'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Updated: Unit {unit} Lesson {unit}.{lesson}")
    return True

# Main execution
if __name__ == "__main__":
    updated = 0
    
    for key, questions in QUIZ_CONTENT.items():
        unit = int(key.split('.')[0])
        lesson = int(key.split('.')[1])
        
        if update_quiz_file(unit, lesson, questions):
            updated += 1
    
    print(f"\nSummary: {updated} quiz files updated")
