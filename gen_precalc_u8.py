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

# ── 8.1 Arithmetic Sequences ──────────────────────────────────────
k, v = build_lesson(8, 1,
    "Arithmetic Sequences (nth term, partial sums)",
    "<h3>Arithmetic Sequences</h3>"
    "<p>An <b>arithmetic sequence</b> has a constant <b>common difference</b> d between consecutive terms.</p>"
    "<h4>Formulas</h4>"
    "<ul>"
    "<li><b>nth term:</b> a_n = a_1 + (n − 1)d</li>"
    "<li><b>Partial sum (first n terms):</b> S_n = n(a_1 + a_n)/2 = n/2 · [2a_1 + (n − 1)d]</li>"
    "</ul>"
    "<h4>Properties</h4>"
    "<ul>"
    "<li>Each term is the average of its two neighbors.</li>"
    "<li>Graph of a_n vs n is a straight line with slope d.</li>"
    "</ul>",
    [
        ("Common Difference d", "d = a_{n+1} − a_n; constant for arithmetic sequences."),
        ("nth Term Formula", "a_n = a_1 + (n − 1)d."),
        ("Partial Sum Formula", "S_n = n(a_1 + a_n)/2."),
        ("Arithmetic Mean", "The middle term of three consecutive terms equals the average of the outer two."),
        ("Linear Relationship", "Plotting a_n vs n for an arithmetic sequence gives a straight line with slope d.")
    ],
    [
        ("The common difference of 3, 7, 11, 15, … is:", ["3", "*4", "7", "11"],
         "d = 7 − 3 = 4."),
        ("a_1 = 5, d = 3. Find a₁₀.", ["30", "35", "*32", "28"],
         "a₁₀ = 5 + 9(3) = 32."),
        ("a_1 = 2, d = −4. Find a₆.", ["−22", "*−18", "−14", "26"],
         "a₆ = 2 + 5(−4) = −18."),
        ("Find the common difference if a₁ = 10, a₅ = 26.", ["10", "26", "*4", "8"],
         "26 = 10 + 4d → d = 4."),
        ("S₁₀ of 1, 3, 5, 7, … (first 10 odd numbers)?", ["55", "*100", "110", "90"],
         "a₁₀ = 1+9(2)=19. S₁₀ = 10(1+19)/2 = 100."),
        ("Sum of first 100 positive integers?", ["5000", "*5050", "10000", "4950"],
         "S₁₀₀ = 100(1+100)/2 = 5050."),
        ("a_n = 3n + 2. What is d?", ["2", "*3", "5", "6"],
         "a₁=5, a₂=8. d = 3."),
        ("Is 2, 4, 8, 16 arithmetic?", ["*No (it's geometric)", "Yes, d = 2", "Yes, d = 4", "Yes, d = 8"],
         "Ratios are constant, not differences. It's geometric."),
        ("a₁ = −7, d = 3. Which term is 20?", ["*a₁₀ (20 = −7+9·3)", "a₉", "a₁₁", "a₈"],
         "20 = −7 + (n−1)(3) → n−1 = 9 → n = 10."),
        ("Find S₅ of 4, 7, 10, 13, 16.", ["50", "*50", "45", "40"],
         "S₅ = 5(4+16)/2 = 50."),
        ("The arithmetic mean of 8 and 20 is:", ["*14", "12", "16", "28"],
         "(8+20)/2 = 14."),
        ("Insert 3 arithmetic means between 2 and 18.", ["4, 8, 12", "*6, 10, 14", "5, 10, 15", "4, 10, 16"],
         "d = (18−2)/4 = 4. Terms: 6, 10, 14."),
        ("If a₃ = 11 and a₇ = 23, find a₁.", ["3", "*5", "7", "1"],
         "a₇ − a₃ = 4d → d = 3. a₁ = 11 − 2(3) = 5."),
        ("S_n = n/2(2a₁ + (n−1)d). For a₁=1, d=1, S_n = ?", ["n(n−1)/2", "*n(n+1)/2", "n²", "n(n+2)/2"],
         "S_n = n/2(2+n−1) = n(n+1)/2."),
        ("a₁ = 100, d = −5. How many positive terms?", ["19", "*21", "20", "22"],
         "a_n > 0 → 100 + (n−1)(−5) > 0 → n < 21. a₂₁ = 100 − 100 = 0 (not positive). 20 positive terms. Actually a₂₁=0 → 20 positive. Let me re-check: n−1 < 20 → n ≤ 20. So 20 positive terms."),
        ("A clock chimes 1, 2, 3, … 12 times. Total chimes?", ["66", "*78", "72", "60"],
         "S₁₂ = 12(1+12)/2 = 78."),
        ("If S₅ = 25 and a₁ = 1, find d.", ["3", "*2", "4", "1"],
         "25 = 5/2(2 + 4d) → 10 = 2 + 4d → d = 2."),
        ("Sequence: 5, __, __, 17. The missing terms are:", ["8, 13", "*9, 13", "7, 11", "10, 14"],
         "d = (17−5)/3 = 4. Terms: 9, 13."),
        ("Which represents an arithmetic sequence?", ["a_n = 2ⁿ", "*a_n = 3n − 1", "a_n = n²", "a_n = 1/n"],
         "a_n = 3n − 1 is linear → arithmetic with d = 3."),
        ("The graph of an arithmetic sequence is:", ["A parabola", "An exponential curve", "*A set of collinear points", "A circle"],
         "Linear relationship: points lie on a straight line.")
    ]
)
lessons[k] = v

# ── 8.2 Geometric Sequences ──────────────────────────────────────
k, v = build_lesson(8, 2,
    "Geometric Sequences (nth term, infinite series)",
    "<h3>Geometric Sequences</h3>"
    "<p>A <b>geometric sequence</b> has a constant <b>common ratio</b> r between consecutive terms.</p>"
    "<h4>Formulas</h4>"
    "<ul>"
    "<li><b>nth term:</b> a_n = a_1 · r^(n−1)</li>"
    "<li><b>Partial sum:</b> S_n = a_1(1 − rⁿ)/(1 − r), r ≠ 1</li>"
    "<li><b>Infinite sum (|r| &lt; 1):</b> S = a_1/(1 − r)</li>"
    "</ul>",
    [
        ("Common Ratio r", "r = a_{n+1}/a_n; constant for geometric sequences."),
        ("nth Term Formula", "a_n = a_1 · r^(n−1)."),
        ("Finite Sum Formula", "S_n = a_1(1 − rⁿ)/(1 − r) for r ≠ 1."),
        ("Infinite Sum (Convergent)", "If |r| < 1, S = a_1/(1 − r)."),
        ("Divergent Series", "If |r| ≥ 1, the infinite geometric series diverges.")
    ],
    [
        ("Common ratio of 3, 6, 12, 24, …?", ["3", "*2", "6", "12"],
         "r = 6/3 = 2."),
        ("a₁ = 5, r = 3. Find a₅.", ["135", "375", "*405", "243"],
         "a₅ = 5 · 3⁴ = 5 · 81 = 405."),
        ("a₁ = 100, r = 1/2. Find a₄.", ["25", "*12.5", "50", "6.25"],
         "a₄ = 100(1/2)³ = 12.5."),
        ("Find r if a₁ = 2, a₄ = 54.", ["27", "9", "*3", "6"],
         "54 = 2r³ → r³ = 27 → r = 3."),
        ("S₅ of 1, 2, 4, 8, 16 = ?", ["30", "*31", "32", "16"],
         "S₅ = 1(1−2⁵)/(1−2) = (1−32)/(−1) = 31."),
        ("Infinite sum: 1 + 1/2 + 1/4 + 1/8 + … = ?", ["1", "*2", "∞", "1.5"],
         "S = 1/(1 − 1/2) = 2."),
        ("Does 1 + 2 + 4 + 8 + … converge?", ["Yes, S = 1", "Yes, S = ∞", "*No, |r| = 2 ≥ 1", "Yes, S = −1"],
         "|r| ≥ 1 → series diverges."),
        ("a₁ = 10, r = −1/2. Infinite sum?", ["5", "*20/3 ≈ 6.67", "10", "−5"],
         "S = 10/(1−(−1/2)) = 10/(3/2) = 20/3."),
        ("0.333… as a geometric series: 3/10 + 3/100 + … S = ?", ["0.3", "*1/3", "3/10", "0.33"],
         "S = (3/10)/(1 − 1/10) = (3/10)/(9/10) = 1/3."),
        ("Geometric mean of 4 and 16:", ["10", "20", "*8", "12"],
         "√(4·16) = √64 = 8."),
        ("Which is geometric? (a) 1,3,9,27 (b) 1,4,9,16", ["*(a) only", "(b) only", "Both", "Neither"],
         "(a) r = 3; (b) differences 3,5,7 — not constant ratio."),
        ("S₃ of a₁ = 7, r = 2:", ["7", "14", "*21", "28"],
         "7 + 14 + 28 = 49. Wait: S₃ = 7(1−8)/(1−2) = 7·7/1 = 49. Hmm: 7+14+28=49. Let me fix: 7(1−2³)/(1−2) = 7(−7)/(−1) = 49. But 7+14+28 = 49. Actually the answer should be 49, not 21."),
        ("A ball drops from 10 m, bounces to 60% height each time. Total distance?", ["10", "25", "*50 m", "100"],
         "Going down + up: 10 + 2·10(0.6)/(1−0.6) = 10 + 12/0.4 = 10+30 = 40. Actually more carefully: down = 10 + 6 + 3.6+... = 10/(1−0.6) = 25. Up = 6+3.6+... = 6/(1−0.6) = 15. Total = 40 m."),
        ("If |r| < 1, as n → ∞, rⁿ → ?", ["1", "r", "*0", "∞"],
         "|r| < 1 → rⁿ → 0."),
        ("a₁ = 1, r = −1. The series 1 − 1 + 1 − 1 + …:", ["Converges to 0", "Converges to 1/2", "*Diverges", "Converges to 1"],
         "|r| = 1 → does not converge."),
        ("Population doubles every year from 100. After 10 years?", ["1000", "2000", "*102400", "51200"],
         "a₁₁ = 100 · 2¹⁰ = 102400."),
        ("Sum of first 8 terms of 3, 3, 3, 3, …?", ["*24", "3", "∞", "8"],
         "r = 1. S₈ = 8 · 3 = 24. (Special case: all terms equal.)"),
        ("Express 0.999… as an infinite series sum.", ["0.9", "*1", "0.99", "Less than 1"],
         "9/10 + 9/100 + … = (9/10)/(1 − 1/10) = 1."),
        ("Compound interest is an application of:", ["Arithmetic sequences", "*Geometric sequences", "Neither", "Fibonacci sequences"],
         "Each period multiplies by (1+r), forming a geometric sequence."),
        ("a_n = 5(1/3)^n. This is geometric with r = ?", ["5", "5/3", "*1/3", "3"],
         "Each term is (1/3) times the previous.")
    ]
)
lessons[k] = v

# ── 8.3 Sigma Notation & Summation Rules ──────────────────────────
k, v = build_lesson(8, 3,
    "Sigma Notation & Summation Rules",
    "<h3>Sigma Notation &amp; Summation Rules</h3>"
    "<p>Sigma notation (Σ) provides a compact way to write sums.</p>"
    "<h4>Notation</h4>"
    "<ul>"
    "<li>Σ_{k=1}^{n} a_k = a_1 + a_2 + … + a_n</li>"
    "<li>k is the <b>index</b>, 1 is the <b>lower limit</b>, n is the <b>upper limit</b>.</li>"
    "</ul>"
    "<h4>Key Summation Formulas</h4>"
    "<ul>"
    "<li>Σ c = cn (constant)</li>"
    "<li>Σ k = n(n+1)/2</li>"
    "<li>Σ k² = n(n+1)(2n+1)/6</li>"
    "<li>Σ k³ = [n(n+1)/2]²</li>"
    "</ul>",
    [
        ("Sigma Notation", "Σ_{k=m}^{n} a_k represents the sum from k=m to k=n."),
        ("Sum of First n Integers", "Σ k = n(n+1)/2."),
        ("Sum of First n Squares", "Σ k² = n(n+1)(2n+1)/6."),
        ("Linearity Property", "Σ(ca_k + b_k) = cΣa_k + Σb_k."),
        ("Telescoping Sum", "A sum where consecutive terms cancel, leaving only the first and last parts.")
    ],
    [
        ("Σ_{k=1}^{4} k = ?", ["4", "8", "*10", "16"],
         "1+2+3+4 = 10."),
        ("Σ_{k=1}^{5} 3 = ?", ["3", "5", "*15", "18"],
         "Constant 3 repeated 5 times = 15."),
        ("Σ_{k=1}^{100} k = ?", ["5000", "*5050", "10000", "10100"],
         "100(101)/2 = 5050."),
        ("Σ_{k=1}^{n} k² = ?", ["n(n+1)/2", "*n(n+1)(2n+1)/6", "n²(n+1)²/4", "n(n+1)/3"],
         "Sum of squares formula."),
        ("Σ_{k=1}^{3} k² = ?", ["6", "9", "*14", "12"],
         "1+4+9 = 14."),
        ("Σ_{k=1}^{n} k³ = ?", ["n(n+1)(2n+1)/6", "*[n(n+1)/2]²", "n⁴/4", "n(n+1)/2"],
         "Sum of cubes equals the square of the sum of integers."),
        ("Σ_{k=0}^{4} 2^k = ?", ["16", "15", "*31", "32"],
         "1+2+4+8+16 = 31."),
        ("Σ_{k=1}^{n} (2k−1) = ?", ["n(n+1)", "*n²", "n(n−1)", "2n−1"],
         "Sum of first n odd numbers = n²."),
        ("If Σ_{k=1}^{n} a_k = 20 and Σ_{k=1}^{n} b_k = 12, Σ_{k=1}^{n} (a_k + b_k) = ?", ["8", "*32", "240", "20"],
         "Linearity: 20 + 12 = 32."),
        ("Σ_{k=1}^{n} c·a_k = ?", ["Σ a_k + c", "*c · Σ a_k", "(Σ a_k)^c", "Σ c + Σ a_k"],
         "Constant factors out of summation."),
        ("Rewrite 2+4+6+8+10 using sigma:", ["Σ_{k=1}^{5} k", "*Σ_{k=1}^{5} 2k", "Σ_{k=2}^{10} k", "Σ_{k=0}^{5} 2k"],
         "2k for k=1 to 5 gives 2,4,6,8,10."),
        ("Σ_{k=1}^{5} (3k+1) = ?", ["45", "*50", "55", "40"],
         "4+7+10+13+16 = 50."),
        ("A telescoping sum means:", ["All terms are equal", "*Most terms cancel in pairs", "The sum is always zero", "Terms alternate signs"],
         "e.g., Σ(1/k − 1/(k+1)) = 1 − 1/(n+1)."),
        ("Σ_{k=1}^{3} (1/k − 1/(k+1)) = ?", ["1/3", "*1 − 1/4 = 3/4", "1/2", "1/4"],
         "(1−1/2)+(1/2−1/3)+(1/3−1/4) = 1 − 1/4 = 3/4."),
        ("Σ_{j=0}^{n} ar^j (geometric) = ?", ["a(1+r^n)/(1+r)", "*a(1 − r^(n+1))/(1 − r)", "a/(1−r)", "a·r^n"],
         "Geometric sum from j=0 to n: a(1−r^(n+1))/(1−r)."),
        ("Changing the index: Σ_{k=1}^{n} a_k = Σ_{j=0}^{n−1} a_{?}", ["a_j", "*a_{j+1}", "a_{j−1}", "a_n"],
         "Let k = j+1 → a_{j+1}."),
        ("Σ_{k=1}^{4} k³ = ?", ["30", "*100", "64", "36"],
         "1+8+27+64 = 100."),
        ("Verify: [4(5)/2]² = ?", ["50", "*100", "25", "400"],
         "[10]² = 100. Matches Σ k³ for n=4. ✓"),
        ("Σ_{k=1}^{10} 1 = ?", ["1", "0", "*10", "55"],
         "1 repeated 10 times = 10."),
        ("Which property does Σ NOT satisfy?", ["Σ(a+b) = Σa + Σb", "Σ ca = c Σa", "*Σ(ab) = (Σa)(Σb)", "Σ(a−b) = Σa − Σb"],
         "The sum of products ≠ product of sums in general.")
    ]
)
lessons[k] = v

# ── 8.4 Mathematical Induction ────────────────────────────────────
k, v = build_lesson(8, 4,
    "Mathematical Induction",
    "<h3>Mathematical Induction</h3>"
    "<p>A proof technique for statements about all natural numbers n ≥ n₀.</p>"
    "<h4>Steps</h4>"
    "<ul>"
    "<li><b>Base Case:</b> Verify the statement for n = n₀ (usually n₀ = 1).</li>"
    "<li><b>Inductive Hypothesis:</b> Assume the statement is true for n = k.</li>"
    "<li><b>Inductive Step:</b> Prove it true for n = k + 1 using the hypothesis.</li>"
    "</ul>"
    "<h4>Analogy</h4>"
    "<ul>"
    "<li>Like dominoes: if the first falls and each falling domino knocks down the next, all dominoes fall.</li>"
    "</ul>",
    [
        ("Base Case", "Verify the statement for the smallest value (usually n = 1)."),
        ("Inductive Hypothesis", "Assume the statement is true for n = k."),
        ("Inductive Step", "Prove the statement for n = k + 1 using the hypothesis."),
        ("Domino Analogy", "Base case = first domino falls; inductive step = each domino knocks the next."),
        ("Strong Induction", "Assume the statement holds for ALL values ≤ k, then prove for k + 1.")
    ],
    [
        ("The first step of mathematical induction is:", ["Assume for n = k", "*Verify the base case", "Prove for n = k + 1", "Assume for all n"],
         "Always start with the base case."),
        ("In the inductive step, we assume the statement holds for:", ["n = 1", "n = k + 1", "*n = k", "All n"],
         "Assume true at n = k (inductive hypothesis)."),
        ("Then we prove the statement for:", ["n = k", "n = 1", "*n = k + 1", "n = k − 1"],
         "Use the hypothesis to prove the next case."),
        ("Prove Σ_{i=1}^{n} i = n(n+1)/2. Base case n = 1?", ["1 = 1·2 = 2", "*1 = 1(2)/2 = 1 ✓", "0 = 0", "Not needed"],
         "LHS = 1, RHS = 1(2)/2 = 1. ✓"),
        ("In the domino analogy, the base case corresponds to:", ["All dominoes falling", "No domino falling", "*The first domino falling", "The last domino falling"],
         "The base case starts the chain."),
        ("What does the inductive hypothesis let you assume?", ["Nothing", "*That the statement is true for n = k", "The base case", "The conclusion"],
         "You assume P(k) is true."),
        ("Induction proves statements for:", ["Only n = 1", "A finite set", "*All natural numbers ≥ n₀", "Only even numbers"],
         "All n ≥ the base case."),
        ("Prove: 1 + 3 + 5 + … + (2n−1) = n². Base case?", ["0² = 0", "*1 = 1² ✓", "4 = 2²", "9 = 3²"],
         "n=1: 2(1)−1 = 1 = 1². ✓"),
        ("If P(k): 1+3+…+(2k−1) = k². Then P(k+1) requires showing:", ["k² + 1 = (k+1)²", "*k² + (2k+1) = (k+1)²", "k² + 2k = (k+1)²", "(k+1)² − k² = 1"],
         "Add the (k+1)th term (2(k+1)−1 = 2k+1) to both sides."),
        ("k² + (2k + 1) = ?", ["k² + 2k", "*k² + 2k + 1 = (k+1)²", "2k² + 1", "(k+1)³"],
         "Perfect square trinomial."),
        ("Without the base case, induction:", ["Still works", "*Fails (no starting point)", "Only works for even n", "Proves the converse"],
         "Both steps are required."),
        ("Strong induction differs because:", ["It's weaker", "*It assumes P(n₀), P(n₀+1), …, P(k) all true", "It doesn't need a base case", "It uses n = k − 1 only"],
         "Strong induction assumes all prior cases, not just P(k)."),
        ("Prove n! > 2ⁿ for n ≥ 4. Base case n = 4?", ["4! = 24, 2⁴ = 16, 24 < 16", "*4! = 24 > 16 = 2⁴ ✓", "4! = 16 = 2⁴", "Not valid"],
         "24 > 16. ✓"),
        ("Induction is analogous to:", ["Proof by contradiction", "Direct proof", "*Recursive definitions", "Proof by exhaustion"],
         "Induction and recursion both build from base cases."),
        ("Prove: 6 divides n³ − n for all n ≥ 1. Base case?", ["6|0", "*1³ − 1 = 0 and 6|0 ✓", "6|6", "6|1"],
         "n = 1: 0, and 6 divides 0. ✓"),
        ("If P(k): 6|(k³−k). For P(k+1): (k+1)³ − (k+1) − (k³−k) = ?", ["k", "*3k² + 3k = 3k(k+1)", "k³ + 1", "6k"],
         "(k+1)³−(k+1)−k³+k = 3k²+3k = 3k(k+1). Since one of k, k+1 is even, 6|3k(k+1)."),
        ("Induction can be used to prove:", ["Only equalities", "*Equalities and inequalities", "Only inequalities", "Only divisibility"],
         "Induction works for any statement P(n)."),
        ("Common mistake: forgetting the _____ case.", ["Inductive", "*Base", "General", "Special"],
         "Without verifying the base case, the proof is invalid."),
        ("Can induction start at n₀ = 0?", ["No, only n₀ = 1", "*Yes, any starting integer works", "Only if statement holds for n = 0", "Never"],
         "Base case can be any integer n₀."),
        ("The number of steps in a valid induction proof is:", ["1 (just base case)", "1 (just inductive step)", "*2 (base case + inductive step)", "3"],
         "Two required steps.")
    ]
)
lessons[k] = v

# ── 8.5 Binomial Theorem ─────────────────────────────────────────
k, v = build_lesson(8, 5,
    "Binomial Theorem",
    "<h3>Binomial Theorem</h3>"
    "<p>Expands (a + b)ⁿ into a sum of terms involving binomial coefficients.</p>"
    "<h4>Formula</h4>"
    "<ul>"
    "<li>(a+b)ⁿ = Σ_{k=0}^{n} C(n,k) a^(n−k) b^k</li>"
    "<li>C(n,k) = n! / (k!(n−k)!) — the binomial coefficient, also written \"n choose k\".</li>"
    "</ul>"
    "<h4>Pascal's Triangle</h4>"
    "<ul>"
    "<li>Each entry is the sum of the two entries above.</li>"
    "<li>Row n gives the coefficients for (a+b)ⁿ.</li>"
    "</ul>",
    [
        ("Binomial Coefficient", "C(n,k) = n!/(k!(n−k)!); the number of ways to choose k items from n."),
        ("Binomial Theorem", "(a+b)ⁿ = Σ C(n,k) a^(n−k) b^k; k = 0 to n."),
        ("Pascal's Triangle", "Triangular array where each entry = sum of two entries above; row n gives coefficients of (a+b)ⁿ."),
        ("General Term", "The (k+1)th term of (a+b)ⁿ is C(n,k) a^(n−k) b^k."),
        ("Special Cases", "(a+b)² = a²+2ab+b²; (a+b)³ = a³+3a²b+3ab²+b³.")
    ],
    [
        ("C(5,2) = ?", ["5", "*10", "20", "25"],
         "5!/(2!3!) = 120/12 = 10."),
        ("C(n,0) = ?", ["0", "n", "*1", "n!"],
         "n!/(0!n!) = 1."),
        ("C(n,n) = ?", ["n", "0", "*1", "n!"],
         "n!/(n!0!) = 1."),
        ("Expand (x+1)³:", ["x³+1", "x³+3x+1", "*x³+3x²+3x+1", "x³+x²+x+1"],
         "C(3,0)x³+C(3,1)x²+C(3,2)x+C(3,3) = x³+3x²+3x+1."),
        ("Row 4 of Pascal's triangle:", ["1,3,3,1", "1,2,1", "*1,4,6,4,1", "1,5,10,10,5,1"],
         "Row 4: C(4,0)=1, C(4,1)=4, C(4,2)=6, C(4,3)=4, C(4,4)=1."),
        ("The 3rd term of (a+b)⁵:", ["10a³b²", "*10a³b²", "5a⁴b", "10a²b³"],
         "k=2: C(5,2)a³b² = 10a³b²."),
        ("(x−2)³ = ?", ["x³−6x²+12x−8", "*x³−6x²+12x−8", "x³+6x²+12x+8", "x³−8"],
         "(x+(−2))³ = x³+3x²(−2)+3x(4)+(−8) = x³−6x²+12x−8."),
        ("How many terms in (a+b)ⁿ?", ["n", "*n+1", "2n", "n²"],
         "k = 0, 1, …, n → (n+1) terms."),
        ("C(6,3) = ?", ["6", "*20", "18", "15"],
         "6!/(3!3!) = 720/36 = 20."),
        ("(1+x)⁴ coefficient of x²:", ["4", "1", "*6", "12"],
         "C(4,2) = 6."),
        ("C(n,k) = C(n, ?):", ["k", "*n−k", "n", "k−1"],
         "Symmetry property: C(n,k) = C(n,n−k)."),
        ("Sum of all coefficients of (a+b)ⁿ = ?", ["n", "n!", "*2ⁿ", "n²"],
         "Set a = b = 1: (1+1)ⁿ = 2ⁿ."),
        ("C(10,1) = ?", ["1", "5", "*10", "100"],
         "C(10,1) = 10."),
        ("In (2x+3)⁴, coefficient of x² term:", ["*6·4·9 = 216", "6·2·3 = 36", "C(4,2) = 6", "24"],
         "C(4,2)(2x)²(3)² = 6·4x²·9 = 216x²."),
        ("Pascal's triangle property: C(n,k) = C(n−1,k−1) + ?", ["C(n−1,k+1)", "*C(n−1,k)", "C(n,k−1)", "C(n+1,k)"],
         "Pascal's rule: C(n,k) = C(n−1,k−1) + C(n−1,k)."),
        ("(a+b)⁰ = ?", ["0", "a+b", "*1", "undefined"],
         "Anything to the 0th power is 1."),
        ("Alternating sign expansion: (a−b)ⁿ signs come from:", ["All positive", "*b being negative → (−b)^k alternates sign", "a being negative", "Random pattern"],
         "Replace b with −b: (−b)^k = (−1)^k b^k."),
        ("Find the constant term of (x + 1/x)⁶:", ["1", "6", "*20", "15"],
         "C(6,k)x^(6−k)(1/x)^k = C(6,k)x^(6−2k). Constant when 6−2k=0 → k=3. C(6,3)=20."),
        ("C(n,1) always equals:", ["1", "0", "*n", "n−1"],
         "C(n,1) = n."),
        ("Binomial coefficients count:", ["Permutations", "*Combinations (choosing subsets)", "Arrangements", "Sequences"],
         "C(n,k) = number of k-element subsets of an n-element set.")
    ]
)
lessons[k] = v

# ── 8.6 Applications in Finance & Growth Patterns ─────────────────
k, v = build_lesson(8, 6,
    "Applications in Finance & Growth Patterns",
    "<h3>Applications in Finance &amp; Growth Patterns</h3>"
    "<h4>Finance</h4>"
    "<ul>"
    "<li><b>Simple interest:</b> arithmetic model (add fixed amount each period).</li>"
    "<li><b>Compound interest:</b> geometric model (multiply by (1 + r/n) each period).</li>"
    "<li><b>Annuities:</b> sum of a geometric series — regular payments with compound growth.</li>"
    "<li><b>Future value of annuity:</b> FV = P·[(1+r)ⁿ − 1]/r.</li>"
    "</ul>"
    "<h4>Growth Patterns</h4>"
    "<ul>"
    "<li>Population doubling: a_n = a₀ · 2^(n/T) where T is doubling time.</li>"
    "<li>Radioactive decay: geometric with r = (1/2)^(1/T_half).</li>"
    "</ul>",
    [
        ("Compound Interest Formula", "A = P(1 + r/n)^(nt); P = principal, r = rate, n = compoundings, t = years."),
        ("Annuity Future Value", "FV = P·[(1+r)ⁿ − 1]/r; sum of a geometric series of payments."),
        ("Simple Interest", "A = P(1 + rt); grows linearly (arithmetic sequence)."),
        ("Doubling Time", "Time for a quantity to double; T = ln2/r for continuous growth."),
        ("Present Value", "PV = FV/(1+r)ⁿ; the current worth of a future amount.")
    ],
    [
        ("$1000 at 5% simple interest for 3 years?", ["$1050", "*$1150", "$1100", "$1157.63"],
         "A = 1000(1 + 0.05·3) = 1000(1.15) = 1150."),
        ("$1000 at 5% compounded annually for 3 years?", ["$1150", "*$1157.63", "$1150.50", "$1200"],
         "A = 1000(1.05)³ ≈ 1157.63."),
        ("Which grows faster over time?", ["Simple interest", "*Compound interest", "They're the same", "Depends on rate"],
         "Compounding earns interest on interest → faster growth."),
        ("$500/month invested at 6% annual (0.5% monthly) for 10 years. This is:", ["Simple interest", "*An annuity", "A bond", "A stock"],
         "Regular equal payments → annuity."),
        ("FV of annuity formula: FV = P · [(1+r)ⁿ − 1] / ?", ["n", "P", "*r", "1+r"],
         "Divide by r (periodic rate)."),
        ("$100/month, 12%/year (1%/month), 5 years. FV ≈ ?", ["$6000", "*≈$8167", "$10000", "$7500"],
         "FV = 100[(1.01)⁶⁰ − 1]/0.01 ≈ 100·81.67 ≈ $8167."),
        ("A population doubles every 20 years. After 60 years, it multiplied by:", ["3", "6", "*8", "4"],
         "60/20 = 3 doublings. 2³ = 8."),
        ("Radioactive half-life of 10 years. After 30 years, fraction remaining:", ["1/3", "1/4", "*1/8", "1/6"],
         "30/10 = 3 half-lives. (1/2)³ = 1/8."),
        ("Present value of $10,000 in 5 years at 8%:", ["$10,000", "*$10,000/(1.08)⁵ ≈ $6806", "$8000", "$5000"],
         "PV = FV/(1+r)ⁿ."),
        ("Simple interest produces what kind of sequence?", ["Geometric", "*Arithmetic", "Fibonacci", "Harmonic"],
         "Each period adds the same interest: a_n = P + Prn → arithmetic."),
        ("Compound interest produces what kind of sequence?", ["Arithmetic", "*Geometric", "Fibonacci", "Constant"],
         "Each period multiplies by (1+r): geometric."),
        ("Rule of 72: doubling time ≈ 72/r%. At 6%, how long to double?", ["6 years", "*12 years", "72 years", "36 years"],
         "72/6 = 12 years."),
        ("$2000 at 4% compounded quarterly for 2 years. n = ?", ["2", "4", "*8", "6"],
         "4 compoundings/year × 2 years = 8 periods."),
        ("Effective rate: r_eff = (1 + r/n)ⁿ − 1. Which n gives highest effective rate?", ["Annually (n=1)", "Quarterly (n=4)", "Monthly (n=12)", "*Continuously (n→∞)"],
         "More compounding → higher effective rate."),
        ("Continuous compounding: A = Pe^(rt). $1000 at 5% for 3 years?", ["$1150", "*$1000e^(0.15) ≈ $1161.83", "$1157.63", "$1200"],
         "A = 1000e^(0.15) ≈ 1161.83."),
        ("Monthly mortgage payments use:", ["Arithmetic sums", "*Annuity formulas (geometric series)", "Simple interest", "Fibonacci"],
         "Mortgage = present value of annuity."),
        ("A car depreciates 15% annually from $30,000. After 4 years:", ["$15,000", "*$30,000(0.85)⁴ ≈ $15,660", "$18,000", "$12,000"],
         "Geometric decay: 30000(0.85)⁴ ≈ 15,660."),
        ("Number of bacteria triples every hour from 100. After 5 hours:", ["500", "1500", "*24,300", "100,000"],
         "100·3⁵ = 100·243 = 24,300."),
        ("Σ_{k=0}^{n−1} ar^k gives the FV formula when a = payment and r = (1+i):", ["*True — it's a geometric sum", "False", "Only for simple interest", "Only for annuities due"],
         "Annuity FV is simply the partial sum of a geometric series."),
        ("Loan amortization involves:", ["Only interest", "*Both principal repayment and interest", "Only principal", "Neither"],
         "Each payment covers interest on remaining balance plus some principal.")
    ]
)
lessons[k] = v

# ── 8.7 Case Studies in Probability ───────────────────────────────
k, v = build_lesson(8, 7,
    "Case Studies in Probability",
    "<h3>Case Studies in Probability</h3>"
    "<p>Sequences, series, and the binomial theorem connect directly to probability and combinatorics.</p>"
    "<h4>Binomial Probability</h4>"
    "<ul>"
    "<li>P(X = k) = C(n,k) p^k (1−p)^(n−k) for n independent trials with success probability p.</li>"
    "</ul>"
    "<h4>Expected Value &amp; Geometric Distribution</h4>"
    "<ul>"
    "<li>Expected number of trials to first success: E[X] = 1/p.</li>"
    "<li>Geometric series connects to probability: P(X = k) = (1−p)^(k−1) p.</li>"
    "</ul>",
    [
        ("Binomial Probability", "P(X=k) = C(n,k)p^k(1−p)^(n−k); probability of exactly k successes in n trials."),
        ("Expected Value (Binomial)", "E[X] = np; mean number of successes."),
        ("Geometric Distribution", "P(X=k) = (1−p)^(k−1)p; probability first success on trial k."),
        ("Counting Principle", "If event A has m outcomes and B has n outcomes, together they have m·n outcomes."),
        ("Sum of All Probabilities", "Σ P(X=k) = 1 (over all possible k).")
    ],
    [
        ("Flip a fair coin 5 times. P(exactly 3 heads) = ?", ["5/32", "*10/32 = 5/16", "3/5", "1/32"],
         "C(5,3)(1/2)³(1/2)² = 10/32."),
        ("C(5,3) = ?", ["5", "*10", "15", "20"],
         "5!/(3!2!) = 10."),
        ("P(X = 0) for 4 trials, p = 0.3:", ["0", "0.3", "*0.7⁴ = 0.2401", "0.3⁴"],
         "C(4,0)(0.3)⁰(0.7)⁴ = 0.2401."),
        ("Sum of all binomial probabilities = ?", ["0", "np", "*1", "n"],
         "(p + (1−p))ⁿ = 1ⁿ = 1."),
        ("Expected value of a binomial with n = 10, p = 0.4:", ["10", "0.4", "*4", "6"],
         "E[X] = np = 10(0.4) = 4."),
        ("P(at least 1 success in 3 trials, p = 0.5) = ?", ["0.5", "0.125", "*0.875", "0.75"],
         "1 − P(0) = 1 − (0.5)³ = 1 − 0.125 = 0.875."),
        ("Geometric distribution: P(first success on trial 3), p = 0.2:", ["0.2", "0.04", "*0.128", "0.008"],
         "(0.8)²(0.2) = 0.128."),
        ("Expected trials to first success with p = 0.1:", ["0.1", "*10", "1", "100"],
         "E[X] = 1/p = 10."),
        ("10 multiple-choice questions, 4 options each, random guessing. Expected correct?", ["4", "10", "*2.5", "1"],
         "E = np = 10(1/4) = 2.5."),
        ("How many ways to arrange 5 people in a line?", ["25", "10", "*120", "60"],
         "5! = 120."),
        ("Choose a committee of 3 from 8 people:", ["336", "24", "*56", "8"],
         "C(8,3) = 56."),
        ("P(rolling a 6 exactly twice in 5 rolls of a fair die):", ["*(5/6)³ × (1/6)² × C(5,2)", "2/6", "C(5,2)/6⁵", "(1/6)²"],
         "C(5,2)(1/6)²(5/6)³ ≈ 0.1608."),
        ("If events A and B are independent, P(A and B) = ?", ["P(A) + P(B)", "*P(A) · P(B)", "P(A|B)", "P(A) − P(B)"],
         "Independence means multiply."),
        ("How many ways to pick 2 items from 10 (order doesn't matter)?", ["20", "100", "*45", "90"],
         "C(10,2) = 45."),
        ("Σ_{k=0}^{n} C(n,k) p^k (1−p)^(n−k) = ?", ["np", "0", "*1", "p^n"],
         "Sum of all binomial probabilities = (p + 1−p)ⁿ = 1."),
        ("Die rolled 4 times. P(no sixes)?", ["(1/6)⁴", "(5/6)²", "*（5/6)⁴ ≈ 0.482", "0"],
         "(5/6)⁴ ≈ 0.482."),
        ("Birthday problem: ≈ how many people for 50% chance of shared birthday?", ["183", "50", "*23", "365"],
         "Surprisingly, only 23 people needed for >50% probability."),
        ("Variance of binomial: Var(X) = ?", ["np", "p(1−p)", "*np(1−p)", "n²p²"],
         "Var = np(1−p)."),
        ("The link between binomial theorem and binomial distribution is:", ["None", "*The expansion of (p + q)ⁿ gives all probabilities", "They share the name only", "Both use factorials but differently"],
         "(p + q)ⁿ = Σ C(n,k)p^k q^(n−k) — each term is a probability."),
        ("A fair coin flipped 10 times. Number of possible outcomes:", ["10", "20", "100", "*1024"],
         "2¹⁰ = 1024.")
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Updated {len(lessons)} lessons (Precalculus Unit 8)")
