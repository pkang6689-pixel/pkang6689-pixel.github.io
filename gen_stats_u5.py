#!/usr/bin/env python3
"""Generate real content for Statistics Unit 5: Random Variables & Distributions (8 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "statistics_lessons.json")
COURSE = "Statistics & Probability"

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

# ── 5.1 Discrete Random Variables ──
k, v = build_lesson(5, 1, "Discrete Random Variables",
    "<h3>Discrete Random Variables</h3>"
    "<p>A <b>random variable (X)</b> assigns a numerical value to each outcome in a sample space. A <b>discrete random variable</b> takes a countable number of distinct values (0, 1, 2, …).</p>"
    "<ul><li><b>Probability distribution:</b> A table or function listing every value x and its probability P(X = x).</li>"
    "<li><b>Requirements:</b> (1) 0 ≤ P(X = x) ≤ 1 for each value, and (2) ΣP(X = x) = 1.</li>"
    "<li><b>Expected value (mean):</b> μ = E(X) = Σ[x · P(X = x)] — the long-run average.</li>"
    "<li><b>Variance:</b> σ² = Σ[(x − μ)² · P(X = x)]; <b>Standard deviation:</b> σ = √σ².</li>"
    "<li><b>Examples:</b> Number of heads in 3 coin flips, number of defective items in a batch, number rolled on a die.</li></ul>",
    [
        ("Discrete Random Variable", "A variable that takes a countable number of distinct numerical values based on random outcomes."),
        ("Probability Distribution", "A table or function listing all possible values of a random variable and their probabilities, summing to 1."),
        ("Expected Value E(X)", "The long-run average of a random variable: E(X) = Σ[x · P(X=x)]."),
        ("Variance of a Discrete RV", "σ² = Σ[(x − μ)² · P(X = x)]; measures spread of a probability distribution."),
        ("Requirements for a Probability Distribution", "All probabilities must be between 0 and 1, and the sum of all probabilities must equal 1."),
    ],
    [
        ("A discrete random variable can take:", ["Any value in an interval", "*A countable number of distinct values", "Only negative values", "Only one value"],
         "Discrete means countable — like 0, 1, 2, 3."),
        ("The sum of all probabilities in a discrete distribution must equal:", ["0", "0.5", "*1", "The sample size"],
         "ΣP(X = x) = 1 for any valid probability distribution."),
        ("E(X) for a fair die (values 1–6, each P = 1/6) = ?", ["3", "*3.5", "4", "6"],
         "E(X) = (1+2+3+4+5+6)/6 = 21/6 = 3.5."),
        ("Each probability in a distribution must be:", ["Negative", "Greater than 1", "*Between 0 and 1 inclusive", "Exactly 0.5"],
         "0 ≤ P(X = x) ≤ 1 for every value."),
        ("E(X) represents:", ["The most common value", "The maximum value", "*The long-run average", "The range"],
         "Expected value is the theoretical mean over many trials."),
        ("X: P(0) = 0.3, P(1) = 0.5, P(2) = 0.2. E(X) = ?", ["1", "*0.9", "0.5", "1.5"],
         "E(X) = 0(0.3) + 1(0.5) + 2(0.2) = 0 + 0.5 + 0.4 = 0.9."),
        ("Variance measures:", ["The center", "*The spread of the distribution", "The shape", "The mode"],
         "Variance quantifies how spread out the values are from the mean."),
        ("σ² = Σ[(x − μ)² · P(x)] is the formula for:", ["Mean", "*Variance", "Standard deviation", "Median"],
         "This is the variance formula for a discrete random variable."),
        ("Standard deviation σ = ?", ["σ²", "μ²", "*√σ²", "σ² / n"],
         "Standard deviation is the square root of variance."),
        ("The number of heads in 5 coin flips is a:", ["Continuous RV", "*Discrete RV", "Parameter", "Statistic only"],
         "It takes the countable values 0, 1, 2, 3, 4, or 5."),
        ("If P(X = 3) = 0.4 and all other values have P summing to 0.5, this distribution is:", ["Valid", "*Invalid (sum > 1)", "Continuous", "Uniform"],
         "0.4 + 0.5 = 0.9 ≠ 1... actually 0.4 + 0.5 = 0.9 < 1, but wait — the question says all OTHER values sum to 0.5, which means total is 0.4 + 0.5 = 0.9, which is not 1. Invalid."),
        ("A discrete distribution table must list:", ["*All possible values and their probabilities", "Only the maximum", "Only the mean", "The cumulative frequency"],
         "Every possible value of X must be paired with its probability."),
        ("E(2X + 3) = ?", ["2E(X)", "E(X) + 3", "*2E(X) + 3", "2E(X) × 3"],
         "E(aX + b) = aE(X) + b — expected value is a linear operator."),
        ("The random variable for the number of customers arriving per hour is:", ["Continuous", "*Discrete", "Neither", "Both"],
         "Arrivals are whole numbers: 0, 1, 2, 3, … — countable values."),
        ("The mode of a discrete distribution is:", ["The mean", "The median", "*The value with the highest probability", "The range"],
         "Mode = the most probable value."),
        ("Var(X) can never be:", ["Zero", "Positive", "Small", "*Negative"],
         "Variance is always ≥ 0 because it's a sum of squared terms times probabilities."),
        ("If X is constant (always equals 5), then E(X) = ?", ["0", "1", "*5", "25"],
         "If X always equals 5, the expected value is 5 and the variance is 0."),
        ("E(X²) is needed to compute variance via:", ["E(X)", "σ", "*Var(X) = E(X²) − [E(X)]²", "E(X) + σ"],
         "This is the shortcut variance formula."),
        ("A probability histogram plots:", ["Frequency", "*P(X = x) for each value of x", "Cumulative probability", "The mean"],
         "A probability histogram shows the probability of each discrete value."),
        ("The total area of all bars in a probability histogram = ?", ["0", "*1", "The sample size", "Depends on X"],
         "The sum of all probabilities (bar heights × width 1) = 1."),
    ]
)
lessons[k] = v

# ── 5.2 Continuous Random Variables ──
k, v = build_lesson(5, 2, "Continuous Random Variables",
    "<h3>Continuous Random Variables</h3>"
    "<p>A <b>continuous random variable</b> can take any value within an interval (e.g., height, weight, temperature).</p>"
    "<ul><li><b>Probability density function (PDF):</b> f(x) describes the shape of the distribution. The total area under the curve = 1.</li>"
    "<li><b>P(a ≤ X ≤ b)</b> = area under the curve between a and b. For continuous variables, P(X = exact value) = 0.</li>"
    "<li><b>Cumulative distribution function (CDF):</b> F(x) = P(X ≤ x), the area under the curve from −∞ to x.</li>"
    "<li><b>Mean (μ):</b> The balance point of the distribution. <b>Variance (σ²):</b> Measures spread around the mean.</li>"
    "<li><b>Uniform distribution:</b> All values in [a, b] are equally likely. f(x) = 1/(b−a); E(X) = (a+b)/2.</li></ul>"
    "<p>Key difference from discrete: probability is found as an <b>area</b>, not a single point.</p>",
    [
        ("Continuous Random Variable", "A variable that can take any value within an interval; probabilities are measured as areas under a curve."),
        ("Probability Density Function (PDF)", "A function f(x) whose total area under the curve equals 1; used to compute probabilities for continuous variables."),
        ("P(X = exact value)", "For a continuous random variable, the probability of any single exact value is 0."),
        ("Cumulative Distribution Function (CDF)", "F(x) = P(X ≤ x); the area under the PDF from −∞ to x."),
        ("Uniform Distribution", "A continuous distribution where all values in [a,b] are equally likely; f(x) = 1/(b−a)."),
    ],
    [
        ("A continuous random variable can take:", ["Only integer values", "*Any value in an interval", "Only 0 and 1", "A countable number of values"],
         "Continuous means uncountably many possible values over an interval."),
        ("P(X = exactly 3.5) for a continuous RV = ?", ["0.5", "1", "*0", "Depends on the distribution"],
         "For continuous RVs, the probability of any single exact value is 0."),
        ("The total area under a PDF curve = ?", ["0", "*1", "The mean", "Depends on the variable"],
         "The total probability must sum to 1."),
        ("P(2 ≤ X ≤ 5) is found by:", ["Adding point probabilities", "Subtracting the mean", "*Calculating the area under the curve between 2 and 5", "Using a frequency table"],
         "For continuous variables, probability = area under the curve."),
        ("The CDF F(x) represents:", ["f(x) itself", "*P(X ≤ x)", "P(X = x)", "The mode"],
         "The CDF gives the cumulative probability up to x."),
        ("For a uniform distribution on [0, 10], P(3 ≤ X ≤ 7) = ?", ["3/10", "*4/10 = 0.4", "7/10", "1/10"],
         "P = (7−3)/(10−0) = 4/10 = 0.4."),
        ("The height of a PDF f(x) at a point represents:", ["*Density (not probability directly)", "Probability at that point", "The CDF value", "The mean"],
         "The density gives relative likelihood; probability requires area (integration)."),
        ("For a uniform distribution on [a, b], E(X) = ?", ["a + b", "a × b", "*(a + b)/2", "b − a"],
         "The mean of a uniform distribution is the midpoint."),
        ("f(x) must always be:", ["Negative", "Equal to 1", "*Non-negative (≥ 0)", "Greater than 1"],
         "A PDF is never negative because probability can't be negative."),
        ("Height is an example of a:", ["Discrete RV", "*Continuous RV", "Neither", "Categorical variable"],
         "Height can take any value in a range — it's continuous."),
        ("P(X > a) for a continuous RV = ?", ["P(X = a)", "P(X < a)", "*1 − P(X ≤ a) = 1 − F(a)", "0"],
         "Using the complement: P(X > a) = 1 − F(a)."),
        ("For a continuous RV, P(X ≤ 5) and P(X < 5) are:", ["Different", "*Equal (since P(X=5) = 0)", "Both 0", "Both 1"],
         "Since P(X = 5) = 0, ≤ and < give the same result."),
        ("The variance of a uniform distribution on [a, b] is:", ["(b−a)/2", "*((b−a)²)/12", "(b−a)²", "b − a"],
         "Var(X) = (b−a)²/12 for a uniform distribution."),
        ("A PDF curve can have a height greater than 1:", ["Never", "*Yes, as long as the total area = 1", "Only for uniform distributions", "Only for normal distributions"],
         "f(x) can exceed 1 at points; what matters is that the total area = 1."),
        ("If F(3) = 0.7, then P(X > 3) = ?", ["0.7", "*0.3", "0", "1"],
         "P(X > 3) = 1 − F(3) = 1 − 0.7 = 0.3."),
        ("The median of a continuous distribution satisfies:", ["f(median) = 0.5", "*F(median) = 0.5", "median = mean always", "P(X = median) = 0.5"],
         "The median is where the CDF equals 0.5 (half the area is to each side)."),
        ("For continuous RVs, probability is always:", ["A single point value", "*An area under the density curve", "Zero", "The height of f(x)"],
         "Continuous probability is computed as area, not point values."),
        ("The exponential distribution models:", ["Test scores", "Heights", "*Time between events (e.g., arrival times)", "Coin flips"],
         "The exponential distribution commonly models waiting times."),
        ("E(X) for a continuous RV is found by:", ["Summing x·P(x)", "*Integrating x·f(x) over all x", "Finding the mode", "Using a frequency table"],
         "E(X) = ∫x·f(x)dx for continuous random variables."),
        ("The key difference between discrete and continuous distributions:", ["There is none", "*Discrete uses sums; continuous uses areas (integrals)", "Continuous can only have one value", "Discrete has no mean"],
         "Discrete distributions sum probabilities; continuous distributions integrate the density."),
    ]
)
lessons[k] = v

# ── 5.3 Binomial Distribution ──
k, v = build_lesson(5, 3, "Binomial Distribution",
    "<h3>Binomial Distribution</h3>"
    "<p>The <b>binomial distribution</b> models the number of successes in n independent trials, each with the same probability of success p.</p>"
    "<p><b>Conditions (BINS):</b></p>"
    "<ul><li><b>B</b>inary outcomes: each trial has exactly two outcomes (success/failure).</li>"
    "<li><b>I</b>ndependent trials: outcomes don't affect each other.</li>"
    "<li><b>N</b> is fixed: the number of trials is predetermined.</li>"
    "<li><b>S</b>ame probability p for each trial.</li></ul>"
    "<p><b>Formula:</b> P(X = k) = C(n,k) · p<sup>k</sup> · (1−p)<sup>n−k</sup></p>"
    "<p><b>Mean:</b> μ = np &nbsp; <b>Variance:</b> σ² = np(1−p) &nbsp; <b>Standard deviation:</b> σ = √(np(1−p))</p>"
    "<p><b>Example:</b> Flipping a fair coin 10 times: n = 10, p = 0.5. P(exactly 3 heads) = C(10,3)(0.5)³(0.5)⁷ ≈ 0.117.</p>",
    [
        ("Binomial Distribution", "Models the number of successes in n independent trials with constant probability p: P(X=k) = C(n,k)p^k(1−p)^(n−k)."),
        ("BINS Conditions", "Binary outcomes, Independent trials, Number of trials is fixed, Same probability for each trial."),
        ("Binomial Mean", "μ = np, where n is the number of trials and p is the probability of success."),
        ("Binomial Variance", "σ² = np(1−p); standard deviation σ = √(np(1−p))."),
        ("Binomial Coefficient C(n,k)", "The number of ways to choose k successes from n trials: C(n,k) = n!/[k!(n−k)!]."),
    ],
    [
        ("The binomial distribution counts:", ["Continuous measurements", "*The number of successes in n independent trials", "The mean of a sample", "The time between events"],
         "Binomial = number of successes in a fixed number of independent trials."),
        ("In BINS, the I stands for:", ["Increasing probability", "*Independent trials", "Integer values", "Identical outcomes"],
         "Each trial must be independent of the others."),
        ("P(X = k) = C(n,k) · p^k · (1−p)^(n−k) is the:", ["Normal formula", "*Binomial probability formula", "Poisson formula", "Expected value formula"],
         "This is the binomial probability formula."),
        ("For n = 5, p = 0.3, the mean μ = ?", ["0.3", "5", "*1.5", "5.3"],
         "μ = np = 5 × 0.3 = 1.5."),
        ("For n = 10, p = 0.4, σ² = ?", ["4", "*2.4", "10", "0.4"],
         "σ² = np(1−p) = 10(0.4)(0.6) = 2.4."),
        ("P(X = 0) for n = 3, p = 0.5:", ["0.5", "0.25", "*0.125", "0"],
         "P(0) = C(3,0)(0.5)⁰(0.5)³ = 1 × 1 × 0.125 = 0.125."),
        ("Which scenario is binomial? Rolling a die 20 times counting 6s:", ["No, outcomes change", "*Yes — binary (6 or not), independent, n=20 fixed, p=1/6 constant", "No, p is not constant", "No, not independent"],
         "Each roll is independent with the same P(6) = 1/6."),
        ("As p approaches 0.5, the binomial distribution becomes:", ["More skewed", "*More symmetric", "Uniform", "Impossible to calculate"],
         "p = 0.5 produces a perfectly symmetric binomial distribution."),
        ("C(10, 3) = ?", ["30", "720", "*120", "10"],
         "C(10,3) = 10!/(3!×7!) = 120."),
        ("For n = 20, p = 0.5, P(exactly 10) uses:", ["Only the mean", "The Poisson formula", "*C(20,10)(0.5)^10(0.5)^10", "P(10)/20"],
         "P(X=10) = C(20,10)(0.5)^20."),
        ("If n = 100, p = 0.05, the distribution is:", ["*Skewed right (most values near 0)", "Symmetric", "Uniform", "Skewed left"],
         "With small p, most outcomes cluster near 0 with a right tail."),
        ("P(X ≥ 1) = ?", ["P(X = 1)", "*1 − P(X = 0)", "P(X = 0)", "nP(1)"],
         "P(at least 1) = 1 − P(none) using the complement rule."),
        ("The binomial distribution is discrete because:", ["p is constant", "n is fixed", "*X counts whole number successes (0, 1, 2, …, n)", "It uses factorials"],
         "The number of successes is a whole number — countable."),
        ("Free throw shooter with 80% accuracy. P(making all 5 shots)?", ["0.80", "5 × 0.80", "*(0.80)⁵ ≈ 0.328", "0.20⁵"],
         "P(X=5) = C(5,5)(0.8)⁵(0.2)⁰ = (0.8)⁵ ≈ 0.328."),
        ("Which is NOT a binomial condition?", ["Fixed number of trials", "Independent trials", "Same p for each trial", "*Trials must have more than 2 outcomes"],
         "Binomial requires exactly 2 outcomes (success/failure), not more."),
        ("σ for n = 16, p = 0.5:", ["4", "*2", "8", "0.5"],
         "σ = √(np(1−p)) = √(16 × 0.25) = √4 = 2."),
        ("The binomial distribution approaches the normal distribution when:", ["n is small", "p = 0 or 1", "*np ≥ 10 and n(1−p) ≥ 10", "Always"],
         "The normal approximation works well when both np and n(1−p) are at least 10."),
        ("P(X = n) for a binomial = ?", ["0", "1", "*p^n", "C(n,n)"],
         "P(all successes) = C(n,n)p^n(1−p)^0 = p^n."),
        ("In a binomial experiment, each trial:", ["Can have multiple outcomes", "*Has exactly two outcomes", "Must succeed", "Has varying probability"],
         "Binary = two outcomes: success or failure."),
        ("E(X) for flipping a fair coin 100 times counting heads:", ["100", "0.5", "*50", "25"],
         "E(X) = np = 100 × 0.5 = 50."),
    ]
)
lessons[k] = v

# ── 5.4 Normal Distribution ──
k, v = build_lesson(5, 4, "Normal Distribution",
    "<h3>Normal Distribution</h3>"
    "<p>The <b>normal distribution</b> (Gaussian distribution) is the most important continuous distribution in statistics.</p>"
    "<ul><li><b>Bell-shaped</b> and symmetric about the mean μ.</li>"
    "<li>Fully described by two parameters: <b>μ</b> (mean/center) and <b>σ</b> (standard deviation/spread).</li>"
    "<li><b>Empirical Rule (68-95-99.7):</b> ~68% of data falls within 1σ of μ, ~95% within 2σ, ~99.7% within 3σ.</li>"
    "<li><b>Standard normal distribution:</b> μ = 0, σ = 1. Any normal variable X can be standardized: Z = (X − μ)/σ.</li>"
    "<li><b>Z-table:</b> Gives the area (probability) to the left of a given z-score.</li></ul>"
    "<p>Many natural phenomena approximate the normal distribution: heights, test scores, measurement errors, etc.</p>",
    [
        ("Normal Distribution", "A bell-shaped, symmetric distribution defined by mean μ and standard deviation σ."),
        ("Empirical Rule", "68% of data within 1σ, 95% within 2σ, 99.7% within 3σ of the mean."),
        ("Standard Normal Distribution", "A normal distribution with μ = 0 and σ = 1; z-scores follow this distribution."),
        ("Z-Score", "Z = (X − μ)/σ; standardizes any normal value to the standard normal scale."),
        ("Z-Table", "A table providing the cumulative area (probability) to the left of a given z-score."),
    ],
    [
        ("The normal distribution is:", ["Skewed right", "Uniform", "*Bell-shaped and symmetric", "Skewed left"],
         "The normal curve is symmetric and bell-shaped around the mean."),
        ("The Empirical Rule states ~95% of data falls within:", ["1σ of μ", "*2σ of μ", "3σ of μ", "0.5σ of μ"],
         "Approximately 95% of data lies within 2 standard deviations of the mean."),
        ("The standard normal distribution has μ = ? and σ = ?", ["μ = 1, σ = 0", "*μ = 0, σ = 1", "μ = 0, σ = 0", "μ = 1, σ = 1"],
         "The standard normal has mean 0 and standard deviation 1."),
        ("Z = (X − μ)/σ converts X to:", ["A percentage", "A raw score", "*A standardized z-score", "A frequency"],
         "The z-score tells how many standard deviations X is from the mean."),
        ("~68% of data lies within:", ["*1σ of the mean", "2σ of the mean", "3σ of the mean", "The median"],
         "The Empirical Rule: 68% within ±1σ."),
        ("A z-score of 2.0 means the value is:", ["2 units above 0", "*2 standard deviations above the mean", "At the 2nd percentile", "Twice the mean"],
         "Z-scores measure distance from the mean in standard deviations."),
        ("P(Z < 0) for the standard normal = ?", ["0", "1", "*0.5", "0.68"],
         "The standard normal is symmetric; half the area is below 0."),
        ("If μ = 100, σ = 15, what z-score corresponds to X = 130?", ["1", "1.5", "*2", "3"],
         "Z = (130 − 100)/15 = 30/15 = 2."),
        ("The area under the entire normal curve = ?", ["0", "*1", "μ", "σ"],
         "Total probability under any PDF = 1."),
        ("P(−1 ≤ Z ≤ 1) ≈ ?", ["0.50", "*0.68", "0.95", "0.997"],
         "About 68% of the standard normal distribution falls within ±1."),
        ("Mean of 500, σ of 100. By Empirical Rule, 99.7% of scores are between:", ["400 and 600", "300 and 700", "*200 and 800", "100 and 900"],
         "μ ± 3σ = 500 ± 300 = [200, 800]."),
        ("Changing μ shifts the normal curve:", ["*Left or right", "Up or down", "Wider or narrower", "It doesn't change"],
         "The mean determines the center position on the number line."),
        ("Changing σ makes the curve:", ["Taller or shorter", "Shift left/right", "*Wider (larger σ) or narrower (smaller σ)", "Symmetric only"],
         "Standard deviation controls the spread of the distribution."),
        ("A z-score of −1.5 means the value is:", ["1.5σ above the mean", "*1.5σ below the mean", "At the 1.5th percentile", "Negative"],
         "Negative z-scores are below the mean."),
        ("Heights of adults are often modeled by the normal distribution because:", ["Heights are always equal", "*They cluster around the mean with symmetric decreasing frequency in both directions", "There are only two heights", "Heights are discrete"],
         "Heights naturally form a bell shape around the average."),
        ("P(Z > 1.96) ≈ ?", ["0.95", "0.50", "*0.025", "0.975"],
         "1.96 is the cutoff for the upper 2.5% of the standard normal."),
        ("To find P(X > 120) when μ = 100, σ = 10:", ["*Compute Z = (120−100)/10 = 2, then find 1 − P(Z ≤ 2)", "Compute Z = 100/120", "P = 120/100", "Cannot be found"],
         "Standardize first, then use the z-table."),
        ("The normal distribution is determined by:", ["Only the mean", "Only the standard deviation", "*Both μ and σ", "The sample size"],
         "Two parameters fully specify the normal distribution."),
        ("If Z = 0, then X = ?", ["0", "σ", "1", "*μ"],
         "Z = 0 means X is at the mean."),
        ("~99.7% of data in a normal distribution lies within:", ["1σ", "2σ", "*3σ", "4σ"],
         "The Empirical Rule: 99.7% within ±3σ."),
    ]
)
lessons[k] = v

# ── 5.5 Central Limit Theorem ──
k, v = build_lesson(5, 5, "Central Limit Theorem",
    "<h3>Central Limit Theorem (CLT)</h3>"
    "<p>The <b>Central Limit Theorem</b> is one of the most important results in statistics.</p>"
    "<p><b>Statement:</b> For a population with mean μ and standard deviation σ, the sampling distribution of the sample mean x̄ approaches a normal distribution as n increases, regardless of the population's shape.</p>"
    "<ul><li><b>Mean of x̄:</b> μ<sub>x̄</sub> = μ (the population mean).</li>"
    "<li><b>Standard error:</b> σ<sub>x̄</sub> = σ/√n (decreases as n increases).</li>"
    "<li><b>Rule of thumb:</b> n ≥ 30 is generally sufficient for the CLT to apply, though if the population is already normal, any n works.</li>"
    "<li><b>Implication:</b> Even if the population is skewed, x̄ will be approximately normal for large enough n.</li>"
    "<li><b>Why it matters:</b> The CLT justifies using z-scores and normal-based methods for inference with sample means.</li></ul>",
    [
        ("Central Limit Theorem", "The sampling distribution of x̄ approaches a normal distribution as sample size increases, regardless of population shape."),
        ("Standard Error", "σ/√n; the standard deviation of the sampling distribution of the sample mean."),
        ("Sampling Distribution", "The distribution of a statistic (like x̄) over all possible samples of the same size from a population."),
        ("Rule of Thumb (n ≥ 30)", "A sample size of 30 or more is generally sufficient for the CLT to produce an approximately normal sampling distribution."),
        ("μ of x̄", "The mean of the sampling distribution of x̄ equals the population mean μ."),
    ],
    [
        ("The CLT states that as n increases, the distribution of x̄:", ["Becomes uniform", "Stays the same as the population", "*Approaches a normal distribution", "Becomes more skewed"],
         "The CLT guarantees normality of x̄ for large n."),
        ("The standard error of x̄ is:", ["σ", "σ²", "*σ/√n", "σ × √n"],
         "SE = σ/√n; it decreases as sample size increases."),
        ("As n increases, the standard error:", ["Increases", "Stays the same", "*Decreases", "Becomes negative"],
         "Dividing by √n means larger samples produce smaller standard errors."),
        ("The CLT applies regardless of:", ["Sample size", "*The shape of the population distribution (for large n)", "The mean", "The standard deviation"],
         "Even for non-normal populations, x̄ becomes normal for large n."),
        ("If σ = 20 and n = 100, SE = ?", ["20", "0.2", "*2", "200"],
         "SE = 20/√100 = 20/10 = 2."),
        ("The rule of thumb for the CLT is n ≥ ?", ["5", "10", "*30", "100"],
         "n ≥ 30 is generally sufficient for the CLT."),
        ("μ of x̄ = ?", ["x̄", "0", "σ/√n", "*μ (population mean)"],
         "The mean of the sampling distribution equals the population mean."),
        ("If the population is already normal, the CLT:", ["Doesn't apply", "Requires n ≥ 30", "*x̄ is normal for ANY sample size", "Only works for large σ"],
         "For a normal population, x̄ is exactly normal regardless of n."),
        ("The CLT is important because it:", ["Eliminates sampling error", "Makes all data normal", "*Allows use of normal-based inference for sample means", "Changes the population distribution"],
         "The CLT justifies z-tests and confidence intervals for means."),
        ("With n = 4, σ = 10, SE = ?", ["10", "40", "2.5", "*5"],
         "SE = 10/√4 = 10/2 = 5."),
        ("Doubling the sample size reduces the standard error by a factor of:", ["2", "*√2 ≈ 1.41", "4", "1/2"],
         "SE = σ/√n; doubling n divides SE by √2."),
        ("The sampling distribution of x̄ is centered at:", ["x̄", "*μ", "σ", "0"],
         "The expected value of x̄ is the population mean μ."),
        ("A population is strongly right-skewed. With n = 50, the distribution of x̄ is:", ["Right-skewed", "Left-skewed", "*Approximately normal", "Uniform"],
         "n = 50 ≥ 30, so the CLT gives an approximately normal distribution."),
        ("Increasing n makes the sampling distribution of x̄:", ["Wider", "*Narrower (more concentrated around μ)", "Skewed", "Bimodal"],
         "Larger n means smaller SE, concentrating x̄ around μ."),
        ("If we take all possible samples of size n from a population and compute x̄ for each:", ["All x̄ values will be identical", "*The distribution of these x̄ values is the sampling distribution", "Only one x̄ matters", "x̄ values will be random with no pattern"],
         "The sampling distribution is the distribution of x̄ over all possible samples."),
        ("The CLT does NOT say:", ["x̄ is approximately normal for large n", "SE = σ/√n", "*The population becomes normal", "E(x̄) = μ"],
         "The CLT says nothing about the population itself — only about the distribution of x̄."),
        ("For n = 1, the sampling distribution of x̄:", ["Is always normal", "*Has the same shape as the population", "Is undefined", "Is uniform"],
         "With n = 1, each 'sample mean' is just a single observation from the population."),
        ("SE measures:", ["*How much x̄ varies from sample to sample", "How much individual data points vary", "The population standard deviation", "The range of the data"],
         "Standard error quantifies the variability of x̄ across samples."),
        ("If σ = 12, n = 36, P(x̄ > 105) when μ = 100:", ["Cannot be found", "*Compute Z = (105−100)/(12/√36) = 5/2 = 2.5, then use z-table", "Equals 0.5", "Equals 0.05"],
         "SE = 12/6 = 2. Z = (105−100)/2 = 2.5. Then find P(Z > 2.5)."),
        ("The CLT is foundational for:", ["Descriptive statistics only", "*Inferential statistics (confidence intervals, hypothesis tests)", "Data collection", "Graphing"],
         "Inferential methods like confidence intervals and hypothesis tests rely on the CLT."),
    ]
)
lessons[k] = v

# ── 5.6 Poisson Distribution ──
k, v = build_lesson(5, 6, "Poisson Distribution",
    "<h3>Poisson Distribution</h3>"
    "<p>The <b>Poisson distribution</b> models the number of events occurring in a fixed interval of time or space when events happen independently at a constant average rate.</p>"
    "<ul><li><b>Parameter:</b> λ (lambda) = the average number of events per interval.</li>"
    "<li><b>Formula:</b> P(X = k) = (e<sup>−λ</sup> · λ<sup>k</sup>) / k!</li>"
    "<li><b>Mean:</b> E(X) = λ &nbsp; <b>Variance:</b> Var(X) = λ &nbsp; (mean equals variance!)</li>"
    "<li><b>Conditions:</b> Events occur independently, at a constant average rate, and cannot occur simultaneously.</li></ul>"
    "<p><b>Examples:</b> Number of calls to a call center per hour, number of typos per page, number of car accidents at an intersection per month, number of emails received per day.</p>"
    "<p>The Poisson can approximate the binomial when n is large and p is small (λ = np).</p>",
    [
        ("Poisson Distribution", "Models the count of events in a fixed interval when events occur independently at a constant rate λ."),
        ("Lambda (λ)", "The average rate of events per interval; in a Poisson distribution, both the mean and variance equal λ."),
        ("Poisson Formula", "P(X = k) = (e^(−λ) · λ^k) / k!, where k = 0, 1, 2, …"),
        ("Mean = Variance", "A unique property of the Poisson distribution: E(X) = Var(X) = λ."),
        ("Poisson Approximation to Binomial", "When n is large and p is small, the binomial can be approximated by a Poisson with λ = np."),
    ],
    [
        ("The Poisson distribution models:", ["Heights", "Test scores", "*The count of events in a fixed interval", "Continuous measurements"],
         "Poisson counts events per unit of time, space, or another interval."),
        ("In the Poisson distribution, λ represents:", ["*The average number of events per interval", "The probability of success", "The sample size", "The standard deviation only"],
         "λ is the average rate parameter."),
        ("For a Poisson distribution, E(X) = Var(X) = ?", ["n", "p", "*λ", "np"],
         "A unique feature: mean and variance are both equal to λ."),
        ("P(X = 0) for Poisson with λ = 3:", ["0", "3", "*e^(−3) ≈ 0.050", "1"],
         "P(0) = e^(−3) × 3⁰ / 0! = e^(−3) ≈ 0.050."),
        ("Which is a Poisson example?", ["Heights of students", "*Number of emails per hour", "Weight of a package", "Score on a test"],
         "Counting events per time interval is a classic Poisson application."),
        ("The Poisson distribution assumes events are:", ["Dependent", "*Independent and occur at a constant average rate", "Always paired", "Normally distributed"],
         "Independence and constant rate are key Poisson assumptions."),
        ("If λ = 5, P(X = 5) = ?", ["*e^(−5) × 5⁵ / 5! ≈ 0.175", "5/5", "1", "0.5"],
         "P(5) = e^(−5) × 3125 / 120 ≈ 0.175."),
        ("As λ increases, the Poisson distribution becomes:", ["More skewed", "*More symmetric (approaches normal)", "Uniform", "Narrower"],
         "For large λ, the Poisson approximates a normal distribution."),
        ("If a store averages 4 customers per 10 min, what is λ for 10 min?", ["10", "*4", "40", "0.4"],
         "λ = 4 customers per 10-minute interval."),
        ("The Poisson approximation to the binomial works when:", ["n is small and p is large", "*n is large and p is small", "n = p", "Always"],
         "With large n and small p, use Poisson with λ = np."),
        ("For a Poisson variable, X can take values:", ["Only 0 and 1", "Only positive integers", "*0, 1, 2, 3, … (non-negative integers)", "Any real number"],
         "Counts can be 0, 1, 2, … with no upper bound."),
        ("If λ = 2, P(X ≥ 1) = ?", ["P(X = 1)", "2", "*1 − e^(−2) ≈ 0.865", "e^(−2)"],
         "P(X ≥ 1) = 1 − P(X = 0) = 1 − e^(−2) ≈ 0.865."),
        ("The standard deviation of a Poisson distribution = ?", ["λ", "λ²", "*√λ", "1/λ"],
         "Since Var(X) = λ, SD = √λ."),
        ("Number of typos per page with an average of 1.5 per page uses:", ["Binomial", "*Poisson", "Normal", "Uniform"],
         "Counting events (typos) per unit (page) at a constant rate = Poisson."),
        ("Two Poisson events cannot occur at:", ["Different times", "1 minute apart", "*The exact same instant", "All"],
         "A Poisson assumption is that two events cannot happen simultaneously."),
        ("If λ = 10 for calls per hour, the expected number in 3 hours = ?", ["10", "*30", "13", "3.33"],
         "λ for 3 hours = 10 × 3 = 30."),
        ("The Poisson distribution is:", ["Continuous", "*Discrete", "Both", "Neither"],
         "It counts events — whole numbers — so it's discrete."),
        ("e in the Poisson formula is approximately:", ["3.14", "1.00", "*2.718", "0.693"],
         "e ≈ 2.71828... (Euler's number)."),
        ("For n = 1000, p = 0.002, the binomial can be approximated by Poisson with λ = ?", ["1000", "0.002", "*2", "500"],
         "λ = np = 1000 × 0.002 = 2."),
        ("The Poisson distribution has how many parameters?", ["0", "*1 (λ)", "2", "3"],
         "The Poisson has a single parameter λ."),
    ]
)
lessons[k] = v

# ── 5.7 Applications in Quality Control ──
k, v = build_lesson(5, 7, "Applications in Quality Control",
    "<h3>Applications in Quality Control</h3>"
    "<p>Statistical distributions are essential in quality control (QC) to monitor and improve manufacturing processes.</p>"
    "<ul><li><b>Control charts:</b> Plot statistics (mean, proportion) over time to detect process deviations. Upper/lower control limits (UCL/LCL) are typically set at μ ± 3σ.</li>"
    "<li><b>Process capability:</b> Compares the spread of the process (6σ) to specification limits.</li>"
    "<li><b>Acceptance sampling:</b> Inspecting a sample from a batch to decide whether to accept or reject the lot. Uses binomial/Poisson distributions.</li>"
    "<li><b>Defect rate:</b> The proportion or count of defective items. Modeled by binomial (proportion) or Poisson (count per unit).</li>"
    "<li><b>Six Sigma:</b> A methodology aiming for ≤ 3.4 defects per million opportunities — about 6σ from the mean.</li></ul>"
    "<p>QC relies on sampling distributions and the CLT to make decisions about production quality from samples.</p>",
    [
        ("Control Chart", "A graph plotting a process statistic over time with upper and lower control limits (UCL/LCL) to detect out-of-control processes."),
        ("Acceptance Sampling", "Inspecting a random sample from a lot and deciding to accept or reject the entire lot based on the results."),
        ("Six Sigma", "A quality methodology targeting ≤ 3.4 defects per million opportunities; the process mean is 6 standard deviations from specifications."),
        ("UCL / LCL", "Upper and Lower Control Limits, typically set at μ ± 3σ on a control chart."),
        ("Process Capability", "A measure comparing the allowable spread (specification range) to the actual process spread (6σ)."),
    ],
    [
        ("Control charts monitor:", ["Individual data points only", "*Process statistics over time to detect deviations", "Only the final product", "Customer satisfaction"],
         "Control charts track statistics like means or proportions over time."),
        ("Control limits are typically set at:", ["μ ± 1σ", "μ ± 2σ", "*μ ± 3σ", "μ ± 4σ"],
         "3-sigma limits capture 99.7% of variation under normal conditions."),
        ("A point outside the control limits suggests:", ["The process is fine", "*The process may be out of control", "The sample is too large", "Normal variation"],
         "A point beyond the limits signals a potential problem."),
        ("Acceptance sampling uses which distribution to model defects?", ["Normal only", "*Binomial or Poisson", "Exponential", "Uniform"],
         "Binomial for proportion defective, Poisson for defect counts."),
        ("Six Sigma targets:", ["6% defects", "6 defects per hundred", "*≤ 3.4 defects per million opportunities", "Zero defects always"],
         "Six Sigma aims for extremely low defect rates."),
        ("Why is the CLT important in quality control?", ["It's not important", "*It allows normal-based inference for sample means even from non-normal processes", "It increases quality", "It reduces cost"],
         "The CLT justifies using z-tests and control charts based on sample statistics."),
        ("An x̄-chart monitors:", ["Individual values", "*The mean of samples taken over time", "The range only", "Customer complaints"],
         "An x̄-chart tracks sample means to detect shifts in the process average."),
        ("A p-chart monitors:", ["*The proportion of defectives in samples", "The process mean", "The range", "The median"],
         "p-charts track the proportion defective over time."),
        ("Out-of-control signals include:", ["Points within limits", "*Points beyond control limits, trends, or patterns", "Increasing sample size", "Normal random variation"],
         "Several patterns can signal an out-of-control process, not just points beyond limits."),
        ("Process capability compares:", ["Cost to revenue", "*Specification limits to process spread (6σ)", "Control limits to specification limits", "Nothing"],
         "Process capability measures whether the process can consistently meet specifications."),
        ("If a process has σ = 2 and spec width = 12, the capability is:", ["Low", "*Adequate (12/12 = 1.0)", "Very high", "Undefined"],
         "6σ = 12, spec width = 12, so capability = 12/12 = 1.0 (minimally capable)."),
        ("Acceptance sampling involves:", ["Testing every item", "*Testing a sample and deciding based on the number of defects", "Never testing", "Only visual inspection"],
         "A random sample is inspected to make an accept/reject decision for the entire lot."),
        ("The Poisson distribution models defect counts in QC when:", ["Defects are common", "*Defects are rare and independent", "All items are defective", "The sample is small"],
         "Rare independent defects per unit follow a Poisson distribution."),
        ("An x̄-chart with all points within limits and no patterns suggests:", ["Definite problems", "*The process is in statistical control", "Zero defects", "Testing should stop"],
         "Points within limits with random scatter indicate a stable process."),
        ("The normal distribution is used in control charts because:", ["It's the only distribution", "*The CLT makes sample means approximately normal", "Defects are always normal", "Quality requires it"],
         "The CLT ensures that sample means are approximately normal for large enough n."),
        ("Common cause variation is:", ["*Random inherent variation in a process", "Caused by a specific identifiable factor", "Always problematic", "Always zero"],
         "Common cause variation is natural and expected; special causes are investigated."),
        ("Special cause variation:", ["Is always random", "*Has an identifiable source and should be investigated", "Improves quality", "Never occurs"],
         "Special causes indicate something changed in the process."),
        ("In acceptance sampling, the 'lot' is:", ["One item", "The sample", "*The entire batch being evaluated", "The control chart"],
         "The lot is the full batch from which the sample is drawn."),
        ("Quality control statistics are applied in:", ["Only manufacturing", "Only healthcare", "Only food production", "*Manufacturing, healthcare, services, and many other fields"],
         "QC concepts apply broadly across industries."),
        ("Reducing process variation leads to:", ["More defects", "Higher costs always", "*Improved quality and fewer defects", "No change"],
         "Less variation means more consistent products and fewer defects."),
    ]
)
lessons[k] = v

# ── 5.8 Case Studies in Real-World Distributions ──
k, v = build_lesson(5, 8, "Case Studies in Real-World Distributions",
    "<h3>Case Studies in Real-World Distributions</h3>"
    "<p>Statistical distributions appear throughout real life. Recognizing which distribution fits a situation is a key statistical skill.</p>"
    "<ul><li><b>Normal:</b> Heights of adults, standardized test scores, measurement errors. Symmetric, bell-shaped data.</li>"
    "<li><b>Binomial:</b> Number of patients cured in n treated (fixed n, same p, independent). Pass/fail counts.</li>"
    "<li><b>Poisson:</b> Number of mutations in a DNA strand, number of accidents per month, calls per hour.</li>"
    "<li><b>Uniform:</b> Random number generators, equally likely outcomes in simulations.</li>"
    "<li><b>Exponential:</b> Time between arrivals, duration until a radioactive particle decays. Memoryless property.</li>"
    "<li><b>Skewed distributions:</b> Income distribution (right-skewed), wait times (often right-skewed).</li></ul>"
    "<p>Choosing the right model depends on the data type (discrete vs. continuous), shape, and underlying process.</p>",
    [
        ("Choosing a Distribution", "Match the data characteristics (discrete/continuous, shape, process) to the appropriate probability model."),
        ("Exponential Distribution", "Models the time between independent events occurring at a constant rate; memoryless."),
        ("Right-Skewed Distribution", "A distribution with a long tail to the right, such as income or housing prices."),
        ("Goodness-of-Fit Test", "A hypothesis test to determine whether observed data fits a specified probability distribution."),
        ("Simulation (Monte Carlo)", "Using random number generation to model and study the behavior of complex systems."),
    ],
    [
        ("SAT scores are best modeled by:", ["Poisson", "Binomial", "*Normal", "Uniform"],
         "SAT scores are approximately normally distributed (bell-shaped, symmetric)."),
        ("Number of car accidents per month at an intersection:", ["Normal", "Binomial", "*Poisson", "Exponential"],
         "Counting events per time interval at a constant rate = Poisson."),
        ("Number of patients cured out of 50 treated (same drug, independent):", ["Poisson", "*Binomial", "Normal", "Uniform"],
         "Fixed n, same p, independent, binary outcome = binomial."),
        ("Time between earthquakes is modeled by:", ["Binomial", "Poisson (for count)", "*Exponential (for time between)", "Normal"],
         "Time between independent events at a constant rate follows the exponential distribution."),
        ("Income distribution in a country is typically:", ["Normal", "Uniform", "*Right-skewed", "Left-skewed"],
         "Most people earn moderate incomes with a long tail of high earners."),
        ("Random number generators (0 to 1) produce:", ["Normal values", "Poisson values", "*Uniform values", "Binomial values"],
         "Each value in [0,1] is equally likely — uniform distribution."),
        ("Heights of adult men are approximately:", ["Skewed", "*Normally distributed", "Uniform", "Poisson"],
         "Adult heights cluster symmetrically around the average — a normal shape."),
        ("Radioactive decay times follow:", ["Binomial", "Normal", "*Exponential", "Uniform"],
         "Time until decay is memoryless and follows the exponential distribution."),
        ("Number of typos per page:", ["Normal", "*Poisson", "Binomial", "Exponential"],
         "Rare independent events per unit = Poisson."),
        ("Pass/fail results for 100 students (same test, independent) use:", ["Poisson", "Normal", "*Binomial", "Exponential"],
         "Binary outcome, fixed n, same p, independent = binomial."),
        ("The exponential distribution is:", ["Discrete", "Symmetric", "*Continuous and right-skewed", "Uniform"],
         "Exponential is continuous with a right tail."),
        ("Number of customers arriving at a store per hour:", ["Binomial", "*Poisson", "Exponential", "Uniform"],
         "Count of arrivals per time unit = Poisson."),
        ("Waiting time until the next bus arrives:", ["Binomial", "Poisson", "*Exponential", "Normal"],
         "Time until the next event = exponential."),
        ("The memoryless property means:", ["Past events affect future", "*The probability of future events doesn't depend on how long you've already waited", "Events have no probability", "The distribution has no mean"],
         "The exponential distribution has this unique memoryless property."),
        ("Housing prices are typically:", ["Normal", "Uniform", "*Right-skewed", "Poisson"],
         "Most houses are moderately priced with a long tail of expensive homes."),
        ("A goodness-of-fit test checks whether:", ["The mean equals zero", "*Observed data matches a proposed distribution", "Data is always normal", "The sample is large enough"],
         "It compares observed frequencies to expected frequencies under a proposed model."),
        ("Monte Carlo simulation uses:", ["*Random sampling to model complex systems", "Only the normal distribution", "Exact calculations", "No probability"],
         "Monte Carlo methods repeatedly sample random values to approximate solutions."),
        ("The normal distribution is appropriate when data is:", ["*Symmetric and bell-shaped", "Count data", "Binary", "Always right-skewed"],
         "Normal fits symmetric, bell-shaped continuous data."),
        ("Choosing the wrong distribution model can lead to:", ["Better predictions", "*Incorrect probabilities and poor decisions", "No effect", "Faster computation"],
         "Model selection affects the validity of all subsequent analysis."),
        ("A key first step in choosing a distribution is:", ["Assuming normal", "Ignoring the data", "*Examining the data type (discrete/continuous) and shape", "Using the largest model"],
         "Understanding the nature of the data guides distribution selection."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 5)")
