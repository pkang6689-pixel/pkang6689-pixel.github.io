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

# ── 5.1 Exponential Growth & Decay Models ─────────────────────────
k, v = build_lesson(5, 1,
    "Exponential Growth & Decay Models",
    "<h3>Exponential Growth &amp; Decay Models</h3>"
    "<p>An <b>exponential function</b> has the form f(x) = a · bˣ, where a ≠ 0 and b > 0, b ≠ 1.</p>"
    "<h4>Growth vs. Decay</h4>"
    "<ul>"
    "<li><b>Growth:</b> b > 1. The function increases rapidly.</li>"
    "<li><b>Decay:</b> 0 < b < 1. The function decreases toward zero.</li>"
    "</ul>"
    "<h4>Natural Exponential</h4>"
    "<ul>"
    "<li>f(x) = eˣ, where e ≈ 2.71828 (Euler's number).</li>"
    "<li>Continuous model: A(t) = A₀ · eᵏᵗ, k > 0 for growth, k < 0 for decay.</li>"
    "</ul>"
    "<h4>Half-Life & Doubling Time</h4>"
    "<ul>"
    "<li>Half-life: time for quantity to halve. A(t) = A₀ · (1/2)^(t/h).</li>"
    "<li>Doubling time: time for quantity to double. 2 = e^(k·T_d) → T_d = ln 2 / k.</li>"
    "</ul>",
    [
        ("Exponential Function", "f(x) = a · bˣ with a ≠ 0, b > 0, b ≠ 1; grows if b > 1, decays if 0 < b < 1."),
        ("Euler's Number (e)", "The irrational constant ≈ 2.71828; base of the natural exponential function."),
        ("Half-Life", "The time required for a quantity undergoing exponential decay to reduce by half."),
        ("Doubling Time", "The time required for a quantity undergoing exponential growth to double: T_d = ln 2 / k."),
        ("Continuous Growth/Decay Model", "A(t) = A₀ · eᵏᵗ; k > 0 is growth, k < 0 is decay.")
    ],
    [
        ("Which is an exponential growth function?", ["f(x) = 3x²", "*f(x) = 3 · 2ˣ", "f(x) = 3 · 0.5ˣ", "f(x) = x³"],
         "b = 2 > 1 → growth."),
        ("Which is exponential decay?", ["f(x) = eˣ", "f(x) = 5ˣ", "*f(x) = 4 · (0.3)ˣ", "f(x) = x⁰·³"],
         "b = 0.3, and 0 < 0.3 < 1 → decay."),
        ("f(x) = 100 · eˣ. f(0) = ?", ["0", "e", "1", "*100"],
         "f(0) = 100 · e⁰ = 100 · 1 = 100."),
        ("A population of 500 grows at 3% per year. Model?", ["*P(t) = 500(1.03)ᵗ", "P(t) = 500(0.03)ᵗ", "P(t) = 500 + 3t", "P(t) = 500(0.97)ᵗ"],
         "3% growth → multiply by 1.03 each year."),
        ("Half-life of 10 years. After 30 years, fraction remaining?", ["1/2", "1/4", "*1/8", "1/16"],
         "30/10 = 3 half-lives. (1/2)³ = 1/8."),
        ("Doubling time formula: T_d = ?", ["ln 2 · k", "k / ln 2", "*ln 2 / k", "2 / k"],
         "From 2 = eᵏᵀ → kT = ln 2 → T = ln 2/k."),
        ("If k = 0.05, doubling time ≈ ?", ["*13.86 years", "20 years", "10 years", "5 years"],
         "ln 2 / 0.05 ≈ 0.693/0.05 ≈ 13.86."),
        ("A(t) = 200e^(−0.1t). What is this?", ["Growth", "*Decay", "Linear", "Quadratic"],
         "k = −0.1 < 0 → decay."),
        ("A(t) = 200e^(−0.1t). Value at t = 10?", ["200", "200/e", "*200/e ≈ 73.6", "0"],
         "A(10) = 200e⁻¹ ≈ 200(0.368) ≈ 73.6."),
        ("The horizontal asymptote of f(x) = 5 · 2ˣ is:", ["y = 5", "y = 2", "*y = 0", "y = 1"],
         "As x → −∞, 2ˣ → 0, so f → 0."),
        ("Domain of f(x) = 3ˣ?", ["x > 0", "x ≥ 0", "*All real numbers", "x ≠ 0"],
         "Exponential functions are defined for all real x."),
        ("Range of f(x) = 3ˣ?", ["All reals", "*y > 0", "y ≥ 0", "y ≥ 1"],
         "3ˣ is always positive, never zero."),
        ("A substance decays from 80 g to 10 g. How many half-lives?", ["2", "*3", "4", "8"],
         "80 → 40 → 20 → 10. Three half-lives."),
        ("e⁰ = ?", ["0", "e", "*1", "∞"],
         "Any non-zero number raised to the 0 power is 1."),
        ("Which grows faster for large x: 2ˣ or x²?", ["x²", "*2ˣ", "Same rate", "Depends on x"],
         "Exponential growth always eventually outpaces polynomial growth."),
        ("If f(x) = 10 · 3ˣ, then f(2) = ?", ["30", "60", "*90", "100"],
         "10 · 3² = 10 · 9 = 90."),
        ("Continuous decay with k = −0.02. After 50 units of time, fraction remaining?", ["e⁻⁵⁰", "*e⁻¹ ≈ 0.368", "0.02", "0.5"],
         "e^(−0.02·50) = e⁻¹ ≈ 0.368."),
        ("The y-intercept of f(x) = a · bˣ is always:", ["b", "0", "1", "*a"],
         "f(0) = a · b⁰ = a."),
        ("A bacteria culture doubles every 4 hours. Starting with 100, after 12 hours:", ["200", "400", "*800", "1600"],
         "12/4 = 3 doublings. 100 · 2³ = 800."),
        ("Exponential functions have a constant:", ["Slope", "Second derivative", "*Ratio between successive values", "Sum"],
         "f(x+1)/f(x) = b, a constant ratio.")
    ]
)
lessons[k] = v

# ── 5.2 Compound Interest & Continuous Growth ─────────────────────
k, v = build_lesson(5, 2,
    "Compound Interest & Continuous Growth",
    "<h3>Compound Interest &amp; Continuous Growth</h3>"
    "<h4>Compound Interest</h4>"
    "<ul>"
    "<li>A = P(1 + r/n)^(nt), where P = principal, r = annual rate, n = compoundings per year, t = years.</li>"
    "<li>More frequent compounding yields more interest.</li>"
    "</ul>"
    "<h4>Continuous Compounding</h4>"
    "<ul>"
    "<li>As n → ∞: A = Peʳᵗ.</li>"
    "<li>This is the maximum possible growth for a given rate r.</li>"
    "</ul>"
    "<h4>APY (Annual Percentage Yield)</h4>"
    "<ul>"
    "<li>Effective annual rate: APY = (1 + r/n)ⁿ − 1.</li>"
    "<li>For continuous compounding: APY = eʳ − 1.</li>"
    "</ul>",
    [
        ("Compound Interest Formula", "A = P(1 + r/n)^(nt); P = principal, r = rate, n = compoundings/yr, t = years."),
        ("Continuous Compounding", "A = Peʳᵗ; the limit of compound interest as compounding frequency → ∞."),
        ("Principal", "The initial amount of money invested or borrowed."),
        ("APY (Annual Percentage Yield)", "Effective annual rate accounting for compounding: (1 + r/n)ⁿ − 1."),
        ("Rule of 72", "Approximate doubling time ≈ 72/r (where r is the percentage rate).")
    ],
    [
        ("$1000 at 5% compounded annually for 2 years:", ["$1050", "*$1102.50", "$1100", "$1105"],
         "A = 1000(1.05)² = 1000(1.1025) = $1102.50."),
        ("$1000 at 6% compounded monthly for 1 year:", ["$1060", "$1061.68", "*$1061.68", "$1066.00"],
         "A = 1000(1 + 0.06/12)^12 = 1000(1.005)^12 ≈ $1061.68."),
        ("$500 compounded continuously at 4% for 5 years:", ["$600", "*$610.70", "$620", "$608.33"],
         "A = 500e^(0.04·5) = 500e^0.2 ≈ 500(1.2214) ≈ $610.70."),
        ("Which yields more: 5% compounded quarterly or 4.9% compounded continuously?", ["*5% quarterly", "4.9% continuous", "They're equal", "Cannot determine"],
         "APY of 5% quarterly: (1.0125)⁴ − 1 ≈ 5.095%. APY of 4.9% continuous: e^0.049 − 1 ≈ 5.022%. 5% quarterly wins."),
        ("As n → ∞ in (1 + r/n)^(nt), the expression approaches:", ["0", "*(Peʳᵗ)/P factor, i.e., eʳᵗ", "1", "rnt"],
         "By definition of e: lim(1 + r/n)^(nt) = eʳᵗ."),
        ("Rule of 72: at 8%, doubling time ≈ ?", ["*9 years", "8 years", "72 years", "12 years"],
         "72/8 = 9 years."),
        ("APY when r = 10%, compounded semi-annually?", ["10%", "*10.25%", "10.5%", "11%"],
         "(1 + 0.10/2)² − 1 = (1.05)² − 1 = 0.1025 = 10.25%."),
        ("With continuous compounding, $1000 at 100% rate for 1 year:", ["$2000", "$2500", "*$2718.28", "$3000"],
         "A = 1000e¹ ≈ $2718.28."),
        ("Compounding more frequently always:", ["Decreases the yield", "*Increases the yield (for same nominal rate)", "Has no effect", "Doubles the yield"],
         "More compounding → more interest earned on interest."),
        ("$2000 at 3% compounded quarterly for 10 years. n = ?", ["3", "10", "*4", "40"],
         "Quarterly → n = 4 (compoundings per year)."),
        ("In the formula A = P(1+r/n)^(nt), nt represents:", ["The rate per period", "*Total number of compounding periods", "The annual yield", "The principal after t years"],
         "n periods per year × t years = total periods."),
        ("$5000 invested. After 10 years it's worth $8000. If compounded annually, approximate rate?", ["*About 4.8%", "About 6%", "About 3%", "About 10%"],
         "8000 = 5000(1+r)^10 → (1+r)^10 = 1.6 → r ≈ 1.6^(1/10) − 1 ≈ 0.048."),
        ("Continuous compounding APY for r = 5%:", ["5%", "*5.127%", "5.25%", "4.9%"],
         "APY = e^0.05 − 1 ≈ 0.05127 = 5.127%."),
        ("If you double your money in 6 years (continuous), the rate is approximately:", ["12%", "6%", "*11.55%", "10%"],
         "2 = e^(6r) → r = ln2/6 ≈ 0.1155 = 11.55%."),
        ("$1000 at 5% simple interest for 3 years vs compound annually for 3 years:", ["Simple gives more", "*Compound gives more", "Equal", "Depends on the bank"],
         "Simple: 1000(1+0.15) = 1150. Compound: 1000(1.05)³ ≈ 1157.63. Compound wins."),
        ("The difference between APR and APY is:", ["APR is always higher", "*APY accounts for compounding, APR does not", "They are the same", "APY is the simple rate"],
         "APR is the nominal rate; APY is the effective rate after compounding."),
        ("$10,000 loan at 6% compounded monthly. Monthly payment factor involves:", ["6%", "0.06", "*0.06/12 = 0.005", "0.6"],
         "Monthly rate = annual rate / 12 = 0.005."),
        ("Present value formula (compound): P = A / (1 + r/n)^(nt). If A = $5000, r = 4%, n = 1, t = 10:", ["$5000", "*$3377.82", "$4000", "$3500"],
         "P = 5000/(1.04)^10 ≈ 5000/1.4802 ≈ $3377.82."),
        ("Which function models continuous compound interest?", ["Linear", "Polynomial", "Power", "*Exponential"],
         "A = Peʳᵗ is an exponential function of t."),
        ("Effective rate is always ≥ nominal rate when:", ["Compounded less than annually", "*Compounded more than once per year", "Never", "Always"],
         "Multiple compoundings per year → effective > nominal.")
    ]
)
lessons[k] = v

# ── 5.3 Properties of Logarithms ──────────────────────────────────
k, v = build_lesson(5, 3,
    "Properties of Logarithms",
    "<h3>Properties of Logarithms</h3>"
    "<p>A <b>logarithm</b> is the inverse of an exponential: if bˣ = y, then log_b(y) = x.</p>"
    "<h4>Key Properties</h4>"
    "<ul>"
    "<li><b>Product Rule:</b> log_b(MN) = log_b(M) + log_b(N).</li>"
    "<li><b>Quotient Rule:</b> log_b(M/N) = log_b(M) − log_b(N).</li>"
    "<li><b>Power Rule:</b> log_b(Mⁿ) = n · log_b(M).</li>"
    "<li>log_b(1) = 0 and log_b(b) = 1.</li>"
    "<li>b^(log_b(x)) = x and log_b(bˣ) = x (inverse properties).</li>"
    "</ul>"
    "<h4>Common & Natural Logarithms</h4>"
    "<ul>"
    "<li><b>Common:</b> log(x) = log₁₀(x).</li>"
    "<li><b>Natural:</b> ln(x) = logₑ(x).</li>"
    "</ul>",
    [
        ("Logarithm", "The inverse of exponentiation: log_b(y) = x means bˣ = y."),
        ("Product Rule", "log_b(MN) = log_b(M) + log_b(N)."),
        ("Quotient Rule", "log_b(M/N) = log_b(M) − log_b(N)."),
        ("Power Rule", "log_b(Mⁿ) = n · log_b(M)."),
        ("Natural Logarithm (ln)", "log base e; ln(x) = logₑ(x). Inverse of eˣ.")
    ],
    [
        ("log₂(8) = ?", ["2", "*3", "4", "8"],
         "2³ = 8 → log₂(8) = 3."),
        ("log₁₀(1000) = ?", ["*3", "10", "100", "2"],
         "10³ = 1000."),
        ("ln(e) = ?", ["e", "0", "*1", "2.718"],
         "logₑ(e) = 1."),
        ("ln(1) = ?", ["1", "e", "*0", "−1"],
         "logₑ(1) = 0 because e⁰ = 1."),
        ("log₃(81) = ?", ["3", "*4", "9", "27"],
         "3⁴ = 81."),
        ("Expand: log(xy).", ["log(x) · log(y)", "*log(x) + log(y)", "log(x)/log(y)", "log(x+y)"],
         "Product rule."),
        ("Expand: ln(x/y).", ["ln(x) · ln(y)", "*ln(x) − ln(y)", "ln(x) / ln(y)", "ln(x + y)"],
         "Quotient rule."),
        ("Expand: log(x⁵).", ["log(5x)", "5 + log(x)", "*5 log(x)", "log(x)/5"],
         "Power rule."),
        ("Condense: 2 ln(x) + ln(y).", ["ln(2x + y)", "*ln(x²y)", "ln(2xy)", "2 ln(xy)"],
         "2 ln(x) = ln(x²), then product rule: ln(x²y)."),
        ("Condense: log(a) − 3 log(b).", ["log(a − 3b)", "log(a/3b)", "*log(a/b³)", "log(a) · log(b³)"],
         "3 log(b) = log(b³), then quotient rule: log(a/b³)."),
        ("Simplify: 10^(log 5).", ["10", "log 5", "*5", "50"],
         "Inverse property: b^(log_b(x)) = x."),
        ("Simplify: ln(e⁷).", ["e⁷", "7e", "*7", "1/7"],
         "log_b(bˣ) = x → ln(e⁷) = 7."),
        ("log₅(1/25) = ?", ["2", "−1", "1/2", "*−2"],
         "1/25 = 5⁻² → log₅(5⁻²) = −2."),
        ("Domain of f(x) = ln(x)?", ["All reals", "x ≥ 0", "*x > 0", "x ≠ 0"],
         "Logarithm is only defined for positive inputs."),
        ("log₂(1) = ?", ["2", "1", "*0", "−1"],
         "Any base: log_b(1) = 0."),
        ("Expand: log₃(9x²/y).", ["*2 + 2 log₃(x) − log₃(y)", "2 log₃(x)/log₃(y)", "log₃(9) + log₃(x²) + log₃(y)", "2 + 2 log₃(x) + log₃(y)"],
         "log₃(9) + log₃(x²) − log₃(y) = 2 + 2 log₃(x) − log₃(y)."),
        ("Which is NOT a valid log property?", ["log(ab) = log a + log b", "log(a/b) = log a − log b", "*log(a + b) = log a · log b", "log(aⁿ) = n log a"],
         "There is no log rule for log(a + b)."),
        ("Condense: (1/2) ln(x) − ln(3).", ["ln(x/6)", "*ln(√x / 3)", "ln(x²/3)", "(ln x − ln 3)/2"],
         "(1/2)ln(x) = ln(√x). Then quotient: ln(√x / 3)."),
        ("If log(x) = 2, then x = ?", ["2", "20", "*100", "e²"],
         "log₁₀(x) = 2 → x = 10² = 100."),
        ("If ln(x) = 0, then x = ?", ["0", "e", "*1", "−1"],
         "e⁰ = 1 → x = 1.")
    ]
)
lessons[k] = v

# ── 5.4 Change of Base Formula ────────────────────────────────────
k, v = build_lesson(5, 4,
    "Change of Base Formula",
    "<h3>Change of Base Formula</h3>"
    "<p>Calculators typically only have log (base 10) and ln (base e). To evaluate log_b(x) for other bases, use the <b>change of base formula</b>.</p>"
    "<h4>Formula</h4>"
    "<ul>"
    "<li>log_b(x) = log(x) / log(b) = ln(x) / ln(b).</li>"
    "<li>More generally: log_b(x) = log_a(x) / log_a(b) for any valid base a.</li>"
    "</ul>"
    "<h4>Applications</h4>"
    "<ul>"
    "<li>Evaluate log₅(20) on a calculator: ln(20)/ln(5).</li>"
    "<li>Compare logarithms in different bases.</li>"
    "<li>Solve equations involving different bases.</li>"
    "</ul>",
    [
        ("Change of Base Formula", "log_b(x) = log(x)/log(b) = ln(x)/ln(b); converts any log to base 10 or base e."),
        ("Why It's Needed", "Most calculators only have log (base 10) and ln (base e); other bases require conversion."),
        ("General Form", "log_b(x) = log_a(x) / log_a(b) for any valid base a > 0, a ≠ 1."),
        ("Reciprocal Property", "log_b(a) = 1 / log_a(b)."),
        ("Calculator Evaluation", "To find log₃(7): type ln(7)/ln(3) or log(7)/log(3).")
    ],
    [
        ("Change of base: log₅(25) using ln:", ["ln(5)/ln(25)", "*ln(25)/ln(5)", "ln(25·5)", "25/5"],
         "log₅(25) = ln(25)/ln(5) = 2."),
        ("log₃(81) using the change of base formula:", ["log(3)/log(81)", "*log(81)/log(3)", "log(81 − 3)", "81/3"],
         "log₃(81) = log(81)/log(3) = 4."),
        ("Evaluate log₂(10) ≈ ?", ["2", "*3.322", "5", "10"],
         "log(10)/log(2) = 1/0.301 ≈ 3.322."),
        ("log₇(1) using any method:", ["7", "1/7", "*0", "1"],
         "log of 1 in any base is 0."),
        ("Which is equivalent to log₄(x)?", ["*ln(x)/ln(4)", "ln(4)/ln(x)", "4 ln(x)", "ln(x) − ln(4)"],
         "Change of base: log₄(x) = ln(x)/ln(4)."),
        ("log₂(8) = ln(8)/ln(2). Calculate:", ["2", "4", "*3", "8"],
         "ln(8)/ln(2) = ln(2³)/ln(2) = 3 ln(2)/ln(2) = 3."),
        ("Reciprocal: log₃(5) · log₅(3) = ?", ["0", "3", "5", "*1"],
         "log₃(5) = 1/log₅(3), so their product = 1."),
        ("Which two forms of change of base give the same result?", ["*log(x)/log(b) and ln(x)/ln(b)", "log(x)/ln(b) and ln(x)/log(b)", "log(b)/log(x) and ln(x)/ln(b)", "None are equal"],
         "Both use the same base consistently, yielding the same ratio."),
        ("Evaluate log₆(36):", ["3", "6", "*2", "1"],
         "6² = 36 → log₆(36) = 2."),
        ("log₂(32) − log₂(4) = ?", ["8", "28", "*3", "5"],
         "log₂(32) = 5, log₂(4) = 2. 5 − 2 = 3. (Or log₂(32/4) = log₂(8) = 3.)"),
        ("If log₅(x) = 2.5, then x = ?", ["*5^2.5 ≈ 55.9", "2.5⁵", "12.5", "25"],
         "x = 5^2.5 = 5² · 5^0.5 = 25√5 ≈ 55.9."),
        ("log₁₀(x) = log(x). True or false?", ["*True", "False", "Only for x > 1", "Only for integers"],
         "log without a base conventionally means base 10."),
        ("Using change of base, log₉(27) = ?", ["2", "*3/2", "3", "9/27"],
         "log(27)/log(9) = (3 log 3)/(2 log 3) = 3/2."),
        ("log₈(2) = ?", ["2", "8", "*1/3", "3"],
         "8^(1/3) = 2 → log₈(2) = 1/3."),
        ("If log₂(x) = 4, then log₄(x) = ?", ["4", "*2", "8", "16"],
         "x = 16. log₄(16) = 2."),
        ("log_b(b²) = ?", ["b", "b²", "1", "*2"],
         "log_b(b²) = 2."),
        ("log₅(125) = ?", ["5", "25", "*3", "2"],
         "5³ = 125."),
        ("log₁/₂(4) = ?", ["2", "1/2", "*−2", "4"],
         "(1/2)⁻² = 4 → log₁/₂(4) = −2."),
        ("Change of base allows us to graph y = log₃(x) on a calculator by entering:", ["y = 3ˣ", "y = x/3", "*y = ln(x)/ln(3)", "y = ln(3x)"],
         "Change of base: ln(x)/ln(3)."),
        ("Which base gives the steepest log graph near x = 1?", ["Base 10", "Base e", "*Base 2 (smallest base > 1)", "They're all the same"],
         "Smaller bases grow faster: the graph of log₂(x) is steeper than log₁₀(x).")
    ]
)
lessons[k] = v

# ── 5.5 Solving Exponential & Logarithmic Equations ───────────────
k, v = build_lesson(5, 5,
    "Solving Exponential & Logarithmic Equations",
    "<h3>Solving Exponential &amp; Logarithmic Equations</h3>"
    "<h4>Exponential Equations</h4>"
    "<ul>"
    "<li>If same base: bˣ = bʸ → x = y.</li>"
    "<li>Otherwise: take log or ln of both sides → x · ln(b) = ln(result) → solve for x.</li>"
    "</ul>"
    "<h4>Logarithmic Equations</h4>"
    "<ul>"
    "<li>Isolate the log expression, then convert to exponential form.</li>"
    "<li>Combine logs using properties first, if needed.</li>"
    "</ul>"
    "<h4>Extraneous Solutions</h4>"
    "<ul>"
    "<li>Always check solutions in the original equation.</li>"
    "<li>Reject any solution that makes a log argument ≤ 0.</li>"
    "</ul>",
    [
        ("One-to-One Property", "If bˣ = bʸ and b > 0, b ≠ 1, then x = y."),
        ("Taking Logarithms", "To solve bˣ = c: x = ln(c)/ln(b) or x = log(c)/log(b)."),
        ("Exponentiate Both Sides", "If log_b(x) = k, then x = bᵏ. Converts log form to exponential form."),
        ("Extraneous Solution", "A solution from algebraic steps that doesn't satisfy the original equation."),
        ("Check Domain of Logarithm", "log_b(x) requires x > 0; reject solutions that violate this.")
    ],
    [
        ("Solve 2ˣ = 16.", ["*x = 4", "x = 8", "x = 2", "x = 3"],
         "2⁴ = 16."),
        ("Solve 3ˣ = 20.", ["x = 20/3", "x = log 20", "*x = ln(20)/ln(3) ≈ 2.727", "x = 3.33"],
         "x = ln(20)/ln(3)."),
        ("Solve e²ˣ = 7.", ["x = 7/2", "*x = ln(7)/2", "x = 2 ln(7)", "x = e^(7/2)"],
         "2x = ln(7) → x = ln(7)/2."),
        ("Solve 5^(x−1) = 125.", ["*x = 4", "x = 3", "x = 25", "x = 5"],
         "125 = 5³ → x − 1 = 3 → x = 4."),
        ("Solve log(x) = 3.", ["x = 3", "x = 30", "*x = 1000", "x = 10/3"],
         "x = 10³ = 1000."),
        ("Solve ln(x) = −1.", ["x = −1", "x = −e", "*x = 1/e", "x = e"],
         "x = e⁻¹ = 1/e."),
        ("Solve log₂(x − 3) = 5.", ["x = 8", "x = 32", "*x = 35", "x = 29"],
         "x − 3 = 2⁵ = 32 → x = 35."),
        ("Solve log(x) + log(x − 3) = 1.", ["*x = 5", "x = 10", "x = −2 and 5", "x = 3"],
         "log(x(x−3)) = 1 → x² − 3x = 10 → x² − 3x − 10 = 0 → (x−5)(x+2) = 0. x = 5 (reject −2)."),
        ("Solve 2^(2x) − 5·2ˣ + 4 = 0.", ["x = 1 only", "x = 2 only", "*x = 0 and x = 2", "x = 4"],
         "Let u = 2ˣ: u² − 5u + 4 = 0 → (u−1)(u−4) = 0 → u = 1 or 4 → x = 0 or 2."),
        ("Solve 4ˣ = 8.", ["x = 2", "*x = 3/2", "x = 8/4", "x = 1"],
         "4ˣ = 2^(2x) = 8 = 2³ → 2x = 3 → x = 3/2."),
        ("Solve ln(2x + 1) = 0.", ["x = 1", "x = −1", "*x = 0", "x = 1/2"],
         "2x + 1 = e⁰ = 1 → 2x = 0 → x = 0."),
        ("Solve log₃(x) = log₃(7).", ["x = 3", "x = 21", "*x = 7", "x = 7/3"],
         "One-to-one: x = 7."),
        ("Solve eˣ = −2.", ["x = ln(−2)", "x = −ln(2)", "*No solution", "x = −2"],
         "eˣ > 0 always; no solution."),
        ("Solve log(x − 1) + log(x + 1) = log(8).", ["x = 4", "*x = 3", "x = 8", "x = 2"],
         "log((x−1)(x+1)) = log(8) → x² − 1 = 8 → x² = 9 → x = 3 (reject −3)."),
        ("Solve 10^(2x−1) = 100.", ["x = 2", "x = 1", "*x = 3/2", "x = 10"],
         "100 = 10² → 2x − 1 = 2 → x = 3/2."),
        ("Solve ln(x²) = 4.", ["x = 4", "*x = e² (also x = −e², but check domain)", "x = 2", "x = e⁴"],
         "2 ln|x| = 4 → ln|x| = 2 → |x| = e² → x = ±e²."),
        ("Solve 3·2ˣ = 48.", ["*x = 4", "x = 16", "x = 3", "x = 8"],
         "2ˣ = 16 = 2⁴ → x = 4."),
        ("In log equations, you must always check:", ["The base", "The coefficient", "*That log arguments are positive (domain)", "Nothing"],
         "Solutions making any log argument ≤ 0 are extraneous."),
        ("Solve 5ˣ⁺¹ = 5³ˣ⁻².", ["x = 1", "*x = 3/2", "x = −1", "x = 2"],
         "x + 1 = 3x − 2 → 3 = 2x → x = 3/2."),
        ("Solve log₂(x) + log₂(x + 2) = 3.", ["*x = 2", "x = 4", "x = −4 and 2", "x = 8"],
         "log₂(x(x+2)) = 3 → x² + 2x = 8 → x² + 2x − 8 = 0 → (x+4)(x−2) = 0. x = 2 (reject −4).")
    ]
)
lessons[k] = v

# ── 5.6 Applications: pH, Richter Scale, Population Growth ────────
k, v = build_lesson(5, 6,
    "Applications: pH, Richter Scale, Population Growth",
    "<h3>Applications: pH, Richter Scale, Population Growth</h3>"
    "<h4>pH Scale</h4>"
    "<ul>"
    "<li>pH = −log[H⁺], where [H⁺] is the hydrogen ion concentration.</li>"
    "<li>pH < 7: acidic; pH = 7: neutral; pH > 7: basic.</li>"
    "</ul>"
    "<h4>Richter Scale</h4>"
    "<ul>"
    "<li>M = log(I/I₀), where I is the intensity and I₀ is a reference.</li>"
    "<li>Each whole number increase represents a 10× increase in amplitude.</li>"
    "</ul>"
    "<h4>Decibels</h4>"
    "<ul>"
    "<li>dB = 10 log(I/I₀). A 10 dB increase means 10× the intensity.</li>"
    "</ul>"
    "<h4>Population Growth</h4>"
    "<ul>"
    "<li>P(t) = P₀ · eᵏᵗ (exponential model).</li>"
    "<li>Use ln to solve for t given a target population.</li>"
    "</ul>",
    [
        ("pH Formula", "pH = −log[H⁺]; measures acidity/basicity of a solution."),
        ("Richter Scale", "M = log(I/I₀); each integer increase = 10× amplitude increase."),
        ("Decibel Scale", "dB = 10 log(I/I₀); a logarithmic measure of sound intensity."),
        ("Population Model", "P(t) = P₀eᵏᵗ; solve for t using ln to find when population reaches a target."),
        ("Logarithmic Scales", "Convert multiplicative relationships to additive ones for easier comparison.")
    ],
    [
        ("[H⁺] = 10⁻⁵ M. pH = ?", ["−5", "5 × 10", "*5", "10"],
         "pH = −log(10⁻⁵) = 5."),
        ("A solution has pH = 3. [H⁺] = ?", ["10⁻¹", "3", "*10⁻³", "10³"],
         "[H⁺] = 10⁻ᵖᴴ = 10⁻³."),
        ("pH of pure water?", ["0", "1", "*7", "14"],
         "Neutral water has [H⁺] = 10⁻⁷ → pH = 7."),
        ("A substance with pH 2 is __ times more acidic than pH 4.", ["2", "20", "*100", "4"],
         "Each pH unit = 10× difference. 2 units → 10² = 100×."),
        ("Richter 6 vs Richter 4: amplitude ratio?", ["2", "20", "*100", "10"],
         "2 units = 10² = 100× amplitude."),
        ("Earthquake I = 10⁶ I₀. Magnitude?", ["5", "*6", "10", "60"],
         "M = log(10⁶) = 6."),
        ("If M₁ = 7 and M₂ = 5, the amplitude ratio is:", ["2", "14", "*100", "10"],
         "10^(7−5) = 10² = 100."),
        ("Sound at 80 dB vs 60 dB: intensity ratio?", ["2", "20", "*100", "10"],
         "20 dB difference: 10^(20/10) = 100."),
        ("A whisper is about 20 dB. Normal conversation is 60 dB. Intensity ratio?", ["40", "*10,000", "4", "400"],
         "40 dB difference: 10^(40/10) = 10⁴ = 10,000."),
        ("P₀ = 1000, k = 0.02. When does population reach 5000?", ["50", "100", "*ln(5)/0.02 ≈ 80.5", "250"],
         "5000 = 1000e^(0.02t) → e^(0.02t) = 5 → t = ln(5)/0.02."),
        ("Population doubles every 15 years. Growth rate k?", ["0.15", "2/15", "*ln(2)/15 ≈ 0.0462", "0.0667"],
         "k = ln(2)/T_d = ln(2)/15."),
        ("Carbon-14 half-life ≈ 5730 years. Decay constant k?", ["*−ln(2)/5730 ≈ −0.000121", "−5730", "0.5/5730", "ln(5730)"],
         "k = −ln(2)/5730 ≈ −0.000121."),
        ("A fossil has 25% of original C-14. Age?", ["5730", "*11,460", "17,190", "2865"],
         "25% = (1/2)² → 2 half-lives = 2(5730) = 11,460 years."),
        ("pH of [H⁺] = 3.16 × 10⁻⁸?", ["8", "7", "*7.5", "3.16"],
         "pH = −log(3.16 × 10⁻⁸) = −(log 3.16 + log 10⁻⁸) = −(0.5 − 8) = 7.5."),
        ("A sound measures 0 dB. This means:", ["No sound", "*Intensity equals the reference I₀", "Maximum volume", "Negative intensity"],
         "0 = 10 log(I/I₀) → I = I₀."),
        ("Newton's law of cooling: T(t) = Tₛ + (T₀ − Tₛ)e⁻ᵏᵗ. As t → ∞, T →", ["T₀", "0", "*Tₛ (surrounding temp)", "∞"],
         "e⁻ᵏᵗ → 0, so T → Tₛ."),
        ("Blood pH is normally about:", ["*7.4", "7.0", "6.0", "8.5"],
         "Blood pH ≈ 7.35–7.45."),
        ("Richter magnitude increases linearly but amplitude increases:", ["Linearly", "*Exponentially (×10 per unit)", "Quadratically", "Logarithmically"],
         "The Richter scale is logarithmic; each unit = 10× amplitude."),
        ("A city's population is modeled by P(t) = 50000e^(0.03t). Population after 10 years?", ["53,000", "65,000", "*67,493", "80,000"],
         "50000e^(0.3) ≈ 50000(1.3499) ≈ 67,493."),
        ("Log scales are useful because they compress:", ["Small ranges", "*Large ranges of data", "Negative numbers", "Only integers"],
         "Logarithmic scales turn multiplicative data spanning many orders of magnitude into manageable additive ranges.")
    ]
)
lessons[k] = v

# ── 5.7 Graphing Exponential & Logarithmic Functions ──────────────
k, v = build_lesson(5, 7,
    "Graphing Exponential & Logarithmic Functions",
    "<h3>Graphing Exponential &amp; Logarithmic Functions</h3>"
    "<h4>Exponential Graphs y = bˣ</h4>"
    "<ul>"
    "<li>Passes through (0, 1). HA: y = 0.</li>"
    "<li>b > 1: increasing; 0 < b < 1: decreasing.</li>"
    "</ul>"
    "<h4>Transformations</h4>"
    "<ul>"
    "<li>y = a · b^(x − h) + k shifts the graph right h, up k, and stretches vertically by a.</li>"
    "<li>HA shifts to y = k.</li>"
    "</ul>"
    "<h4>Logarithmic Graphs y = log_b(x)</h4>"
    "<ul>"
    "<li>Passes through (1, 0). VA: x = 0.</li>"
    "<li>Reflection of y = bˣ over the line y = x.</li>"
    "<li>b > 1: increasing; 0 < b < 1: decreasing.</li>"
    "</ul>"
    "<h4>Transformations of Log</h4>"
    "<ul>"
    "<li>y = a · log_b(x − h) + k: VA shifts to x = h.</li>"
    "</ul>",
    [
        ("Parent Exponential Graph", "y = bˣ passes through (0, 1) with HA y = 0."),
        ("Parent Log Graph", "y = log_b(x) passes through (1, 0) with VA x = 0."),
        ("Inverse Relationship", "The exponential and log with the same base are reflections over y = x."),
        ("Horizontal Asymptote Shift", "For y = a·b^(x−h) + k, the HA becomes y = k."),
        ("Vertical Asymptote Shift", "For y = a·log_b(x−h) + k, the VA becomes x = h.")
    ],
    [
        ("y = 2ˣ passes through which point?", ["(1, 0)", "*(0, 1)", "(2, 0)", "(0, 2)"],
         "2⁰ = 1 → (0, 1)."),
        ("HA of y = 2ˣ?", ["y = 1", "y = 2", "*y = 0", "x = 0"],
         "As x → −∞, 2ˣ → 0."),
        ("y = 3ˣ − 2. HA?", ["y = 0", "y = 3", "*y = −2", "y = 2"],
         "Shifted down 2: HA → y = −2."),
        ("y = 2^(x+1). This shifts the parent graph:", ["Right 1", "*Left 1", "Up 1", "Down 1"],
         "x + 1 = x − (−1); horizontal shift left 1."),
        ("y = log₃(x) passes through:", ["(0, 1)", "*(1, 0)", "(3, 0)", "(0, 3)"],
         "log₃(1) = 0 → (1, 0)."),
        ("VA of y = log(x)?", ["y = 0", "*x = 0", "x = 1", "y = 1"],
         "log is undefined for x ≤ 0; VA at x = 0."),
        ("y = ln(x − 3). Domain?", ["x > 0", "*x > 3", "x ≥ 3", "All reals"],
         "x − 3 > 0 → x > 3."),
        ("VA of y = ln(x − 3)?", ["x = 0", "*x = 3", "x = −3", "y = 3"],
         "VA shifts to x = 3."),
        ("y = −2ˣ reflects the parent graph over:", ["y-axis", "*x-axis", "y = x", "No reflection"],
         "Negative coefficient → reflection over x-axis."),
        ("y = 2⁻ˣ is equivalent to:", ["y = −2ˣ", "y = 1/2ˣ", "*y = (1/2)ˣ", "y = 2ˣ − 1"],
         "2⁻ˣ = (2⁻¹)ˣ = (1/2)ˣ. This is a reflection over the y-axis."),
        ("Range of y = log₂(x)?", ["x > 0", "y > 0", "*All real numbers", "y ≥ 0"],
         "Logarithmic functions have range (−∞, ∞)."),
        ("Range of y = 3ˣ?", ["All reals", "*y > 0", "y ≥ 1", "y ≥ 0"],
         "Exponential is always positive."),
        ("y = log(x) and y = 10ˣ are:", ["Parallel", "Perpendicular", "*Inverse functions (reflections over y = x)", "The same"],
         "log₁₀ and 10ˣ are inverses."),
        ("y = 5 · 2ˣ. y-intercept?", ["2", "1", "*5", "10"],
         "At x = 0: 5 · 1 = 5."),
        ("y = log₂(x) + 3. Describe the transformation:", ["Left 3", "*Up 3", "Right 3", "Stretch by 3"],
         "Adding 3 outside shifts the graph up 3 units."),
        ("y = log₅(x − 1) + 2. VA and key point?", ["VA x = 0, passes through (1, 2)", "*VA x = 1, passes through (2, 2)", "VA x = 2, passes through (1, 0)", "VA x = 1, passes through (6, 3)"],
         "VA at x = 1. When x = 2: log₅(1) + 2 = 0 + 2 = 2. Passes through (2, 2)."),
        ("y = e^(x) + 1. As x → −∞:", ["y → −∞", "y → 0", "*y → 1", "y → e"],
         "eˣ → 0, so y → 0 + 1 = 1. HA at y = 1."),
        ("y = −ln(x). Compared to ln(x), this is:", ["Shifted down", "*Reflected over the x-axis", "Reflected over y-axis", "Compressed"],
         "Negative sign reflects over x-axis."),
        ("The graph of y = log(10x) compared to y = log(x):", ["Same graph", "*Shifted up by 1", "Shifted right by 10", "Stretched by 10"],
         "log(10x) = log(10) + log(x) = 1 + log(x). Shifted up 1."),
        ("y = 2^(x−3) + 1. Describe all transformations:", ["*Right 3, up 1", "Left 3, up 1", "Right 3, down 1", "Right 1, up 3"],
         "h = 3 (right), k = 1 (up).")
    ]
)
lessons[k] = v

# ── 5.8 Logistic Growth Models ────────────────────────────────────
k, v = build_lesson(5, 8,
    "Logistic Growth Models",
    "<h3>Logistic Growth Models</h3>"
    "<p>The <b>logistic model</b> accounts for a carrying capacity that limits exponential growth.</p>"
    "<h4>Formula</h4>"
    "<ul>"
    "<li>P(t) = L / (1 + be⁻ᵏᵗ), where L = carrying capacity, b and k are positive constants.</li>"
    "</ul>"
    "<h4>Characteristics</h4>"
    "<ul>"
    "<li>S-shaped (sigmoid) curve.</li>"
    "<li>Initially grows roughly exponentially.</li>"
    "<li>Growth rate slows as P approaches L.</li>"
    "<li>Horizontal asymptotes: y = 0 (as t → −∞) and y = L (as t → ∞).</li>"
    "<li>Inflection point at P = L/2 (fastest growth occurs here).</li>"
    "</ul>",
    [
        ("Logistic Model", "P(t) = L/(1 + be⁻ᵏᵗ); models growth limited by carrying capacity L."),
        ("Carrying Capacity (L)", "The maximum sustainable population; upper horizontal asymptote."),
        ("Sigmoid (S-shaped) Curve", "The characteristic shape of a logistic graph: slow start, fast middle, slow finish."),
        ("Inflection Point", "Occurs at P = L/2; the point where growth rate is maximum."),
        ("Initial Value", "P(0) = L/(1 + b); set t = 0 to find the starting population.")
    ],
    [
        ("In logistic growth, the carrying capacity is:", ["The initial population", "*The maximum sustainable population", "The growth rate", "Half the population"],
         "L is the upper limit."),
        ("P(t) = 1000/(1 + 9e⁻⁰·⁵ᵗ). Carrying capacity?", ["9", "0.5", "*1000", "100"],
         "L = 1000."),
        ("P(0) for the function above?", ["1000", "9", "*100", "0"],
         "P(0) = 1000/(1 + 9) = 1000/10 = 100."),
        ("As t → ∞ in the logistic model, P(t) →", ["0", "∞", "*L (carrying capacity)", "b"],
         "e⁻ᵏᵗ → 0, so P → L/(1+0) = L."),
        ("The inflection point of logistic growth occurs at P =", ["L", "0", "*L/2", "L/4"],
         "Growth rate is maximum at half the carrying capacity."),
        ("The logistic curve is shaped like:", ["A straight line", "A parabola", "*An S (sigmoid)", "A hyperbola"],
         "Slow → fast → slow = S-shaped."),
        ("Early in logistic growth, the behavior resembles:", ["*Exponential growth", "Linear growth", "Constant function", "Decay"],
         "When P is small relative to L, growth is approximately exponential."),
        ("P(t) = 500/(1 + 24e⁻⁰·³ᵗ). P(0) = ?", ["500", "24", "*20", "25"],
         "500/(1+24) = 500/25 = 20."),
        ("For the model above, what is the inflection point population?", ["500", "20", "*250", "100"],
         "L/2 = 500/2 = 250."),
        ("Which real-world scenario fits logistic growth?", ["Free-falling object", "*Spread of a rumor in a fixed population", "Compound interest", "Linear depreciation"],
         "A rumor spreads fast initially, then slows as most people already know it—bounded by population size."),
        ("P(t) = 800/(1 + 3e⁻⁰·²ᵗ). Find P when P is at inflection.", ["800", "200", "*400", "None"],
         "Inflection at L/2 = 400."),
        ("What happens to growth rate as P → L?", ["It increases", "*It approaches 0", "It stays constant", "It becomes negative"],
         "Growth slows as the population nears the carrying capacity."),
        ("If b is large in the logistic model, then P(0) is:", ["*Small relative to L", "Close to L", "Equal to L", "Negative"],
         "P(0) = L/(1+b). Large b → small P(0)."),
        ("A logistic model has two horizontal asymptotes:", ["y = 0 and y = b", "y = k and y = L", "*y = 0 and y = L", "y = −L and y = L"],
         "As t → −∞, P → 0; as t → ∞, P → L."),
        ("In biology, carrying capacity is determined by:", ["The organism's genes", "*Available resources and environmental limits", "The initial population", "The growth rate k"],
         "Resources, space, and competition set the carrying capacity."),
        ("P(t) = 1000/(1 + 49e⁻⁰·¹ᵗ). How long to reach 500?", ["*t = ln(49)/0.1 ≈ 38.9", "t = 50", "t = 49", "t = 100"],
         "500 = 1000/(1+49e⁻⁰·¹ᵗ) → 1+49e⁻⁰·¹ᵗ = 2 → 49e⁻⁰·¹ᵗ = 1 → e⁻⁰·¹ᵗ = 1/49 → t = ln(49)/0.1."),
        ("Compared to exponential, logistic growth is more realistic because:", ["It's simpler", "*It accounts for limited resources", "It always increases", "It decreases"],
         "Real populations can't grow forever; resources are finite."),
        ("The parameter k in the logistic model affects:", ["Carrying capacity", "*How quickly the population reaches L", "The initial population", "The final population"],
         "Larger k → faster approach to carrying capacity."),
        ("If L = 5000 and P(0) = 500, find b.", ["10", "*9", "5000", "500"],
         "500 = 5000/(1+b) → 1+b = 10 → b = 9."),
        ("A logistic model is appropriate when:", ["Growth is unbounded", "Decay is constant", "*There is a maximum capacity", "The rate is linear"],
         "Logistic = bounded growth with a maximum (carrying capacity).")
    ]
)
lessons[k] = v

# ── 5.9 Case Studies in Biology & Finance ─────────────────────────
k, v = build_lesson(5, 9,
    "Case Studies in Biology & Finance",
    "<h3>Case Studies in Biology &amp; Finance</h3>"
    "<p>Exponential and logarithmic functions are widely used in both biological and financial modeling.</p>"
    "<h4>Biology</h4>"
    "<ul>"
    "<li><b>Bacterial growth:</b> N(t) = N₀ · 2^(t/d) where d = doubling time.</li>"
    "<li><b>Drug elimination:</b> C(t) = C₀ · e⁻ᵏᵗ (first-order kinetics).</li>"
    "<li><b>Carbon dating:</b> A(t) = A₀ · e^(−0.000121t).</li>"
    "</ul>"
    "<h4>Finance</h4>"
    "<ul>"
    "<li><b>Compound interest:</b> A = P(1 + r/n)^(nt).</li>"
    "<li><b>Present value:</b> P = A · e⁻ʳᵗ (continuous discounting).</li>"
    "<li><b>Depreciation:</b> V(t) = V₀(1 − r)ᵗ.</li>"
    "</ul>",
    [
        ("Bacterial Growth Model", "N(t) = N₀ · 2^(t/d); population doubles every d time units."),
        ("Drug Elimination (Half-Life)", "C(t) = C₀ · e⁻ᵏᵗ; drug concentration decreases exponentially."),
        ("Carbon-14 Dating", "Uses the known half-life (~5730 yr) to estimate the age of organic material."),
        ("Present Value", "P = Ae⁻ʳᵗ; the current worth of a future sum under continuous discounting."),
        ("Depreciation", "V(t) = V₀(1 − r)ᵗ; models the declining value of an asset over time.")
    ],
    [
        ("Bacteria double every 20 min. Starting with 500, count after 1 hour?", ["1000", "2000", "*4000", "1500"],
         "60/20 = 3 doublings. 500 · 2³ = 4000."),
        ("Drug half-life is 6 hours. After 18 hours, fraction remaining?", ["1/2", "1/4", "*1/8", "1/16"],
         "18/6 = 3 half-lives. (1/2)³ = 1/8."),
        ("C₀ = 200 mg, half-life 4 hrs. C(t) = 200e⁻ᵏᵗ. k = ?", ["0.25", "4", "*ln(2)/4 ≈ 0.1733", "0.5"],
         "k = ln(2)/half-life = ln(2)/4."),
        ("A fossil has 12.5% of original C-14. Approximate age?", ["5730 yr", "11,460 yr", "*17,190 yr", "22,920 yr"],
         "12.5% = (1/2)³ → 3 half-lives = 3(5730) = 17,190 years."),
        ("$10,000 at 5% continuous. Value after 20 years?", ["$20,000", "$25,000", "*$27,183", "$30,000"],
         "10000e^(0.05·20) = 10000e¹ ≈ $27,183."),
        ("Present value of $50,000 in 10 years at 3% continuous:", ["*$37,041", "$50,000", "$45,000", "$40,000"],
         "P = 50000e^(−0.03·10) = 50000e⁻⁰·³ ≈ 50000(0.7408) ≈ $37,041."),
        ("A car worth $30,000 depreciates 15% per year. Value after 3 years?", ["$22,500", "*$18,402", "$15,000", "$20,000"],
         "30000(0.85)³ = 30000(0.6141) ≈ $18,402."),
        ("When does the car above reach $10,000?", ["*About 6.8 years", "10 years", "5 years", "8 years"],
         "10000 = 30000(0.85)ᵗ → (0.85)ᵗ = 1/3 → t = ln(1/3)/ln(0.85) ≈ 6.76."),
        ("Bacteria: N₀ = 100, doubling time 30 min. N(2 hrs) = ?", ["200", "400", "*1600", "800"],
         "2 hrs = 120 min. 120/30 = 4 doublings. 100 · 2⁴ = 1600."),
        ("A drug's therapeutic range requires C ≥ 50 mg. C₀ = 400 mg, half-life 8 hrs. How long until C = 50?", ["16 hrs", "*24 hrs", "8 hrs", "32 hrs"],
         "50 = 400(1/2)^(t/8) → (1/2)^(t/8) = 1/8 = (1/2)³ → t/8 = 3 → t = 24."),
        ("An investment doubles in 12 years (continuous). Rate?", ["12%", "6%", "*5.78%", "8.33%"],
         "r = ln(2)/12 ≈ 0.0578."),
        ("$5000 grows to $8000 in 5 years (annual compounding). Rate?", ["10%", "*9.86%", "12%", "8%"],
         "(1+r)⁵ = 8/5 = 1.6 → r = 1.6^(1/5) − 1 ≈ 0.0986."),
        ("Radioactive decay: 40% remains. If half-life is 10 yr, how old?", ["10 yr", "*About 13.2 yr", "20 yr", "15 yr"],
         "0.4 = (1/2)^(t/10) → t = 10 · ln(0.4)/ln(0.5) ≈ 10(1.322) ≈ 13.2 yr."),
        ("In finance, 'time value of money' means:", ["Money is worthless over time", "*A dollar today is worth more than a dollar in the future", "Interest doesn't matter", "Prices never change"],
         "Due to earning potential (interest), money now is more valuable."),
        ("A culture starts at 1000 and reaches 8000 in 6 hours. Doubling time?", ["*2 hours", "3 hours", "1 hour", "6 hours"],
         "8000/1000 = 8 = 2³ → 3 doublings in 6 hrs → doubling time = 2 hrs."),
        ("Depreciation differs from exponential decay because:", ["It's linear", "It increases", "*It uses a discrete rate (1−r)ᵗ rather than continuous", "There's no difference"],
         "Depreciation typically uses a discrete annual rate."),
        ("A $500 bond matures to $1000 in 20 years. Continuous rate?", ["5%", "2.5%", "*3.47%", "10%"],
         "r = ln(2)/20 ≈ 0.0347."),
        ("Blood alcohol content decays with half-life ≈ 1.5 hrs. After 4.5 hrs of no drinking, BAC is __ of initial.", ["1/2", "1/4", "*1/8", "1/16"],
         "4.5/1.5 = 3 half-lives. (1/2)³ = 1/8."),
        ("Which grows faster: $1000 at 5% compounded continuously, or $1000 at 5.1% compounded annually?", ["Continuous 5%", "*Annual 5.1%", "They're equal", "Depends on time"],
         "APY of 5% continuous = e^0.05 − 1 ≈ 5.127%. 5.1% annual = 5.1%. 5.127% > 5.1%, so continuous 5% is slightly better."),
        ("The key advantage of logarithmic models is:", ["They always increase", "They're linear", "*They handle data spanning many orders of magnitude", "They're exact"],
         "Logarithms compress large ranges into manageable scales.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 5)")
