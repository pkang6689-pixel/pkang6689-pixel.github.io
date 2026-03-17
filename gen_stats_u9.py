#!/usr/bin/env python3
"""Generate real content for Statistics Unit 9: Advanced Probability & Statistics (7 lessons)."""
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

# ── 9.1 Law of Large Numbers ──
k, v = build_lesson(9, 1, "Law of Large Numbers",
    "<h3>Law of Large Numbers (LLN)</h3>"
    "<p>The <b>Law of Large Numbers</b> states that as the number of trials of a random experiment increases, the sample mean converges to the expected value (population mean).</p>"
    "<ul><li><b>Informal statement:</b> The more you repeat an experiment, the closer the average of the results gets to the true expected value.</li>"
    "<li><b>Example:</b> Flipping a fair coin many times — the proportion of heads approaches 0.5 as the number of flips grows.</li>"
    "<li><b>Weak LLN:</b> The sample mean converges in probability to the population mean.</li>"
    "<li><b>Strong LLN:</b> The sample mean converges almost surely to the population mean.</li>"
    "<li><b>Gambler's Fallacy:</b> The mistaken belief that past outcomes affect future independent trials. The LLN says nothing about individual trials, only about long-run averages.</li>"
    "<li><b>Applications:</b> Insurance (actuarial predictions), casinos (house edge realized over many bets), polling (larger samples → more accurate estimates).</li></ul>",
    [
        ("Law of Large Numbers", "As the number of trials increases, the sample mean converges to the population mean (expected value)."),
        ("Gambler's Fallacy", "The mistaken belief that past outcomes influence future independent trials (e.g., 'I'm due for a win')."),
        ("Weak LLN", "The sample mean converges in probability to the population mean."),
        ("Strong LLN", "The sample mean converges almost surely (with probability 1) to the population mean."),
        ("Convergence", "In the context of LLN, the long-run average approaches a fixed value as the number of observations increases."),
    ],
    [
        ("The Law of Large Numbers states that as trial count increases:", ["Each trial becomes more predictable", "*The sample mean approaches the population mean", "Variance increases", "Outcomes become less random"],
         "LLN is about the convergence of the average, not individual outcomes."),
        ("Flipping a fair coin 10,000 times, the proportion of heads should be close to:", ["Exactly 0.5", "1.0", "*Approximately 0.5", "0 or 1"],
         "LLN says the proportion converges to the true probability (0.5) as trials increase."),
        ("The Gambler's Fallacy is:", ["A correct belief about probability", "*The false belief that past independent outcomes affect future ones", "A theorem in statistics", "The same as LLN"],
         "Each coin flip is independent — past results don't change future probabilities."),
        ("LLN applies to:", ["Only coin flips", "Only dice", "*Any repeated random experiment with a defined expected value", "Only normal distributions"],
         "LLN is general — it applies to any random variable with a finite mean."),
        ("If you roll a fair die many times, the average roll approaches:", ["1", "6", "*3.5", "4"],
         "The expected value of a fair die is (1+2+3+4+5+6)/6 = 3.5."),
        ("LLN guarantees convergence for:", ["Small samples", "*Large samples (as n → ∞)", "Any sample size", "Only n > 100"],
         "LLN is an asymptotic result — it describes behavior as n grows large."),
        ("Casinos rely on LLN because:", ["They always win every bet", "*Over many bets the house edge is reliably realized", "Each bet is guaranteed", "Gamblers always lose"],
         "Individual bets are random, but the average profit per bet converges to the house advantage."),
        ("Insurance companies use LLN to:", ["Avoid all risk", "*Predict average claims accurately when insuring many people", "Set individual claim amounts", "Eliminate variance"],
         "With many policies, the average claim cost becomes predictable."),
        ("A sample mean of 5 based on 10 observations vs. 10,000 observations — which is more reliable?", ["10 observations", "*10,000 observations", "Both are equal", "Neither is reliable"],
         "LLN says larger samples give means closer to the true mean."),
        ("LLN says nothing about:", ["Long-run averages", "Population means", "*Individual trial outcomes", "Sample means"],
         "LLN concerns averages, not single events."),
        ("The Weak LLN says the sample mean converges in:", ["Certainty", "*Probability", "Distribution only", "Variance"],
         "Weak LLN uses convergence in probability."),
        ("The Strong LLN says the sample mean converges:", ["In distribution", "In probability", "*Almost surely (with probability 1)", "Never"],
         "Almost sure convergence is stronger than convergence in probability."),
        ("LLN requires the random variable to have:", ["*A finite expected value (mean)", "A normal distribution", "A known variance", "At least 30 observations"],
         "The expected value must exist for LLN to apply."),
        ("After 3 heads in a row on a fair coin, the probability of the next flip being heads is:", ["Less than 0.5", "Greater than 0.5", "*Still 0.5", "0"],
         "Flips are independent — past outcomes don't change probabilities."),
        ("LLN is fundamental to:", ["Only theoretical math", "*Statistics, insurance, gambling theory, quality control, and many applied fields", "Only coin flipping", "Computer science only"],
         "LLN is one of the most widely applied principles in probability."),
        ("If a sample of 50 gives x̄ = 12, and a sample of 5,000 gives x̄ = 10.2, which is likely closer to μ?", ["50-sample mean", "*5,000-sample mean", "Both equally close", "Cannot determine"],
         "LLN: larger sample means are more reliable estimators."),
        ("LLN is NOT about:", ["Averages", "Expected values", "*Guaranteeing a specific outcome in any single trial", "Long-run behavior"],
         "Individual outcomes remain random — LLN is about the average."),
        ("In polling, larger samples are preferred because of:", ["Lower cost", "Faster results", "*LLN — larger samples give estimates closer to the true population value", "Smaller margins"],
         "Larger random samples yield more accurate estimates."),
        ("LLN and the Central Limit Theorem (CLT) are:", ["The same theorem", "*Related but different — LLN is about convergence of the mean, CLT is about its distribution", "Contradictory", "Unrelated"],
         "LLN says the mean converges; CLT says the distribution of the mean is approximately normal."),
        ("Without LLN, statistics would be unreliable because:", ["We couldn't collect data", "*Sample averages wouldn't reliably estimate population parameters", "Probability wouldn't exist", "Variance would be zero"],
         "LLN justifies using sample statistics to estimate population parameters."),
    ]
)
lessons[k] = v

# ── 9.2 Expected Value ──
k, v = build_lesson(9, 2, "Expected Value",
    "<h3>Expected Value</h3>"
    "<p>The <b>expected value</b> (E(X) or μ) of a random variable is the long-run average value after many repetitions.</p>"
    "<ul><li><b>Discrete:</b> E(X) = Σ xᵢ · P(xᵢ) — the sum of each value times its probability.</li>"
    "<li><b>Continuous:</b> E(X) = ∫ x · f(x) dx over the range of X.</li>"
    "<li><b>Properties:</b><ul>"
    "<li>E(aX + b) = aE(X) + b (linearity).</li>"
    "<li>E(X + Y) = E(X) + E(Y) (always, regardless of independence).</li>"
    "<li>If X and Y are independent: E(XY) = E(X) · E(Y).</li></ul></li>"
    "<li><b>Variance:</b> Var(X) = E(X²) − [E(X)]².</li>"
    "<li><b>Decision making:</b> Expected value helps compare options (e.g., insurance, lottery, business decisions).</li></ul>",
    [
        ("Expected Value E(X)", "The long-run average of a random variable; for discrete X: E(X) = Σ xᵢ · P(xᵢ)."),
        ("Linearity of Expectation", "E(aX + b) = aE(X) + b; E(X + Y) = E(X) + E(Y) regardless of independence."),
        ("Variance from Expectation", "Var(X) = E(X²) − [E(X)]²; measures spread around the mean."),
        ("Fair Game", "A game where the expected value of winnings is zero — neither side has an advantage on average."),
        ("Expected Monetary Value", "In decision analysis, the weighted average of possible payoffs, used to compare alternatives."),
    ],
    [
        ("E(X) for a fair 6-sided die:", ["3", "6", "*3.5", "1"],
         "E(X) = (1+2+3+4+5+6)/6 = 21/6 = 3.5."),
        ("E(X) = Σ xᵢ · P(xᵢ) applies to:", ["Continuous variables", "Normal distributions only", "*Discrete random variables", "All functions"],
         "This formula sums each value times its probability for discrete distributions."),
        ("E(2X + 5) when E(X) = 10:", ["20", "15", "*25", "10"],
         "E(2X + 5) = 2·10 + 5 = 25."),
        ("E(X + Y) = E(X) + E(Y) requires:", ["Independence", "Same distribution", "*Nothing — it's always true", "Equal variances"],
         "Linearity of expectation holds without any conditions."),
        ("If X and Y are independent, E(XY) = ?", ["E(X) + E(Y)", "E(X) − E(Y)", "*E(X) · E(Y)", "0"],
         "Independence allows the product of expectations."),
        ("A lottery ticket costs $2 and has a 1/1000 chance of winning $500. E(profit) = ?", ["$500", "$2", "*−$1.50", "$0.50"],
         "E(profit) = (1/1000)(500) + (999/1000)(0) − 2 = 0.50 − 2 = −$1.50."),
        ("A fair game has expected value:", ["Greater than 0", "Less than 0", "*Equal to 0", "Equal to 1"],
         "In a fair game, neither player has an expected advantage."),
        ("Var(X) = E(X²) − [E(X)]². If E(X) = 4 and E(X²) = 20, then Var(X) = ?", ["4", "20", "*4", "16"],
         "Var(X) = 20 − 16 = 4."),
        ("Expected value helps in decision making by:", ["Guaranteeing outcomes", "*Comparing the average long-run payoff of different options", "Eliminating risk", "Predicting exact outcomes"],
         "E(X) provides a basis for comparing alternatives on average."),
        ("If P(X=1) = 0.3, P(X=2) = 0.5, P(X=3) = 0.2, E(X) = ?", ["2", "*1.9", "1.5", "2.5"],
         "E(X) = 1(0.3) + 2(0.5) + 3(0.2) = 0.3 + 1.0 + 0.6 = 1.9."),
        ("E(X) can be:", ["Only a whole number", "Only positive", "*Any real number (including non-integers and negatives)", "Only between 0 and 1"],
         "The expected value can be any real number."),
        ("For a continuous variable, E(X) uses:", ["Summation", "*Integration ∫ x·f(x)dx", "Multiplication only", "No formula exists"],
         "Continuous expected value replaces summation with integration."),
        ("The expected number of heads in 100 fair coin flips:", ["100", "0", "*50", "25"],
         "E = np = 100(0.5) = 50."),
        ("Adding a constant c to X changes E(X) by:", ["0", "c²", "*c", "−c"],
         "E(X + c) = E(X) + c."),
        ("Multiplying X by constant a changes E(X) to:", ["E(X) + a", "*a · E(X)", "E(X)/a", "E(X)²"],
         "E(aX) = a · E(X)."),
        ("In insurance, expected value helps:", ["Guarantee no claims", "*Set premiums by estimating average claim costs", "Prevent all losses", "Eliminate risk entirely"],
         "Insurers use expected values to price policies so premiums cover expected claims plus margin."),
        ("E(X) does NOT tell you:", ["The long-run average", "The mean", "*What will happen in a single trial", "The center of the distribution"],
         "E(X) is about averages over many repetitions, not single events."),
        ("The expected value of a constant c is:", ["0", "1", "undefined", "*c"],
         "E(c) = c since a constant has no randomness."),
        ("Var(X) is always:", ["Negative", "Zero", "*Non-negative (≥ 0)", "Equal to E(X)"],
         "Variance can never be negative — it's the expected squared deviation."),
        ("In game theory, players choose strategies to maximize:", ["Minimum payoff always", "*Expected payoff (expected value)", "Single-trial outcomes", "The opponent's loss"],
         "Expected value is central to strategic decision-making."),
    ]
)
lessons[k] = v

# ── 9.3 Probability Distributions in Real Life ──
k, v = build_lesson(9, 3, "Probability Distributions in Real Life",
    "<h3>Probability Distributions in Real Life</h3>"
    "<p>Probability distributions model uncertainty in the real world.</p>"
    "<ul><li><b>Normal distribution:</b> Heights, test scores, measurement errors, blood pressure — the bell curve appears when many small, independent factors combine.</li>"
    "<li><b>Binomial distribution:</b> Number of successes in fixed trials — e.g., defective items in a batch, correct answers on a multiple-choice test.</li>"
    "<li><b>Poisson distribution:</b> Rare events in a fixed interval — customer arrivals, typos per page, traffic accidents per day.</li>"
    "<li><b>Exponential distribution:</b> Time between events — time between customer arrivals, lifetimes of products.</li>"
    "<li><b>Uniform distribution:</b> All outcomes equally likely — random number generators, lottery draws.</li>"
    "<li><b>Choosing the right distribution:</b> Match the real-world scenario to the distribution's assumptions — fixed trials (binomial), rare events (Poisson), continuous measurements (normal), etc.</li></ul>",
    [
        ("Normal Distribution in Real Life", "Models continuous data influenced by many small factors: heights, IQ scores, measurement errors."),
        ("Binomial in Real Life", "Counts successes in a fixed number of independent trials: defective products, correct guesses, pass/fail."),
        ("Poisson in Real Life", "Models the count of rare events in a fixed interval: calls per hour, accidents per month."),
        ("Exponential Distribution", "Models the time between independent events occurring at a constant rate."),
        ("Choosing a Distribution", "Match scenario characteristics (fixed trials, rare events, continuous data) to distribution assumptions."),
    ],
    [
        ("Heights in a large population follow approximately a:", ["Binomial distribution", "Uniform distribution", "*Normal distribution", "Poisson distribution"],
         "Heights result from many small genetic and environmental factors → normal."),
        ("The number of defective items in 100 sampled products follows a:", ["Normal distribution", "*Binomial distribution", "Exponential distribution", "Poisson distribution"],
         "Fixed trials, each defective or not → binomial."),
        ("Typos per page in a long manuscript follow a:", ["Normal distribution", "Binomial distribution", "*Poisson distribution", "Uniform distribution"],
         "Rare events in a fixed interval (page) → Poisson."),
        ("Time between customer arrivals at a store follows a:", ["Normal distribution", "Binomial distribution", "Poisson distribution", "*Exponential distribution"],
         "Continuous time between events occurring at a rate → exponential."),
        ("A random number generator producing values between 0 and 1 follows a:", ["Normal distribution", "Binomial distribution", "*Uniform distribution", "Poisson distribution"],
         "All values equally likely in the interval → uniform."),
        ("Test scores often follow a normal distribution because:", ["Teachers make them normal", "*Many independent factors (study, aptitude, conditions) combine additively", "All tests are curved", "The Central Limit Theorem requires it"],
         "Many small, independent influences create approximately normal distributions."),
        ("Phone calls arriving at a call center per hour follow a:", ["Binomial", "Normal", "*Poisson distribution", "Exponential"],
         "Count of events in a fixed interval with constant average rate → Poisson."),
        ("Product lifetimes (time until failure) often follow:", ["Binomial", "Poisson", "*Exponential or Weibull distribution", "Uniform"],
         "Time until an event (failure) is modeled by exponential or related distributions."),
        ("Blood pressure measurements in a population follow approximately:", ["Poisson", "Binomial", "*Normal distribution", "Exponential"],
         "Continuous biological measurements influenced by many factors → normal."),
        ("Choosing a probability distribution requires:", ["Guessing randomly", "*Matching the scenario to the distribution's assumptions", "Always using normal", "Always using binomial"],
         "Each distribution has specific conditions that the data scenario should satisfy."),
        ("The binomial distribution requires:", ["*Fixed number of independent trials, each with the same probability of success", "Events in a time interval", "Continuous outcomes", "A bell-shaped curve"],
         "Binomial: fixed n, independent trials, constant p."),
        ("The Poisson distribution assumes:", ["Fixed trials", "*Events occur independently at a constant average rate in a fixed interval", "Continuous data", "Equal probabilities"],
         "Poisson: count of independent events in a fixed region of time/space."),
        ("Measurement errors (e.g., in lab equipment) typically follow:", ["Poisson", "Binomial", "*Normal distribution", "Uniform"],
         "Random measurement errors from many small sources tend to be normally distributed."),
        ("If events follow a Poisson process, the time between events follows:", ["A Poisson distribution", "A binomial distribution", "*An exponential distribution", "A normal distribution"],
         "Poisson counts and exponential waiting times are mathematically linked."),
        ("Insurance claims per month might follow:", ["Normal", "Binomial", "*Poisson distribution", "Uniform"],
         "Rare events (claims) in a fixed interval → Poisson."),
        ("The uniform distribution is appropriate when:", ["Some outcomes are more likely", "*All outcomes in a range are equally likely", "Data is bell-shaped", "Events are rare"],
         "Uniform means equal probability for all values in the interval."),
        ("Traffic accidents per week in a city might follow:", ["Normal", "Binomial", "*Poisson distribution", "Exponential"],
         "Count of relatively rare events in a fixed time → Poisson."),
        ("Coin flips (number of heads in 20 flips) follow:", ["Normal", "*Binomial distribution", "Poisson", "Exponential"],
         "Fixed trials (20), two outcomes, constant p = 0.5 → binomial."),
        ("A very large binomial (large n, moderate p) can be approximated by:", ["Poisson", "Exponential", "*Normal distribution", "Uniform"],
         "By the CLT, binomial with large n and np ≥ 10, nq ≥ 10 approximates normal."),
        ("Using the wrong distribution leads to:", ["Better predictions", "*Inaccurate probabilities and wrong conclusions", "No effect", "Simpler calculations only"],
         "Distribution assumptions must match the data-generating process for valid results."),
    ]
)
lessons[k] = v

# ── 9.4 Chi-Square Tests ──
k, v = build_lesson(9, 4, "Chi-Square Tests",
    "<h3>Chi-Square Tests</h3>"
    "<p>The <b>chi-square (χ²) test</b> is used for categorical data.</p>"
    "<ul><li><b>Goodness-of-fit test:</b> Tests whether observed frequencies match an expected distribution. χ² = Σ (O − E)²/E.</li>"
    "<li><b>Test of independence:</b> Tests whether two categorical variables are independent using a contingency table.</li>"
    "<li><b>Test of homogeneity:</b> Tests whether the distribution of a categorical variable is the same across different populations.</li>"
    "<li><b>Degrees of freedom:</b><ul>"
    "<li>Goodness-of-fit: df = k − 1 (k = number of categories).</li>"
    "<li>Independence/homogeneity: df = (r − 1)(c − 1) (r rows, c columns).</li></ul></li>"
    "<li><b>Conditions:</b> All expected counts should be ≥ 5. Observations must be independent.</li>"
    "<li><b>χ² is always ≥ 0:</b> Large χ² values suggest the observed data differ significantly from the expected.</li></ul>",
    [
        ("Chi-Square Statistic", "χ² = Σ (O − E)²/E, where O = observed frequency and E = expected frequency."),
        ("Goodness-of-Fit Test", "Tests whether observed categorical data match a hypothesized distribution."),
        ("Test of Independence", "Uses a contingency table to test whether two categorical variables are independent."),
        ("Degrees of Freedom (χ²)", "Goodness-of-fit: df = k−1; independence/homogeneity: df = (r−1)(c−1)."),
        ("Expected Count Condition", "All expected frequencies should be at least 5 for the chi-square approximation to be valid."),
    ],
    [
        ("The chi-square statistic is:", ["*Σ (O − E)²/E", "Σ (O + E)", "Σ (O − E)", "(O − E)/E"],
         "Chi-square sums the squared differences between observed and expected, divided by expected."),
        ("A goodness-of-fit test checks:", ["If data are normal", "*If observed frequencies match a hypothesized distribution", "If two means are equal", "If r = 0"],
         "Goodness-of-fit compares observed vs. expected category counts."),
        ("A test of independence uses:", ["One variable", "*A two-way contingency table with two categorical variables", "Continuous data", "A single sample mean"],
         "Independence tests examine the association between two categorical variables."),
        ("df for a goodness-of-fit test with 5 categories:", ["5", "6", "*4", "3"],
         "df = k − 1 = 5 − 1 = 4."),
        ("df for a 3 × 4 contingency table:", ["12", "7", "*6", "11"],
         "df = (3−1)(4−1) = 2·3 = 6."),
        ("The χ² distribution is always:", ["Symmetric", "Negative", "*Non-negative (≥ 0)", "Normal"],
         "χ² values are sums of squared terms and are always ≥ 0."),
        ("A large χ² value suggests:", ["Good fit", "*The observed data differ significantly from expected", "No association", "Small sample size"],
         "Large χ² = large discrepancies between observed and expected frequencies."),
        ("Expected counts should all be at least:", ["1", "3", "*5", "10"],
         "The chi-square approximation requires expected counts ≥ 5."),
        ("If χ² = 0:", ["Maximum discrepancy", "The test is invalid", "*Observed counts match expected counts exactly", "The p-value is 0"],
         "χ² = 0 means perfect agreement between observed and expected."),
        ("The null hypothesis for a test of independence:", ["Variables are dependent", "Means are equal", "*The two variables are independent (no association)", "Proportions differ"],
         "H₀ states no association between the categorical variables."),
        ("The null hypothesis for goodness-of-fit:", ["Data are skewed", "*The observed distribution matches the expected distribution", "Means are unequal", "Variables are dependent"],
         "H₀ says the data fit the hypothesized distribution."),
        ("Expected frequency for a cell in an independence test:", ["O", "Row total × Column total", "*Row total × Column total / Grand total", "Grand total / cells"],
         "E = (row total × column total) / grand total."),
        ("Rejecting H₀ in a test of independence means:", ["Variables are certainly dependent", "H₀ is true", "*There is sufficient evidence that the variables are associated", "The test is wrong"],
         "Rejection means the data provide evidence of association (at the chosen significance level)."),
        ("Chi-square tests are for:", ["Continuous data", "*Categorical (count) data", "Mean comparisons", "Regression analysis"],
         "Chi-square tests analyze frequencies of categorical variables."),
        ("Test of homogeneity checks:", ["If the mean is the same", "*If the distribution of a categorical variable is the same across populations", "If data is normal", "If variance is equal"],
         "Homogeneity compares categorical distributions across groups."),
        ("Independence and homogeneity tests use the same formula but differ in:", ["Calculation", "df", "*The structure of the study (one sample vs. multiple populations)", "The statistic"],
         "Same χ² calculation, different study designs and hypotheses."),
        ("If expected counts are too small:", ["Use χ² anyway", "*Consider Fisher's exact test or combine categories", "Increase α", "Remove data"],
         "Small expected counts make the χ² approximation unreliable."),
        ("A p-value of 0.02 from a χ² test at α = 0.05 means:", ["Fail to reject H₀", "*Reject H₀ (evidence against the null hypothesis)", "Accept H₀", "The data are normal"],
         "p = 0.02 < α = 0.05, so we reject H₀."),
        ("χ² tests do NOT tell you:", ["Whether there's an association", "*The direction or strength of association — only that one exists", "Whether to reject H₀", "Whether expected counts are met"],
         "χ² detects association but doesn't measure direction or effect size."),
        ("The chi-square distribution is:", ["Symmetric", "Flat", "*Right-skewed for small df, approaching symmetric for large df", "Always bell-shaped"],
         "The χ² distribution is right-skewed, becoming more symmetric as df increases."),
    ]
)
lessons[k] = v

# ── 9.5 ANOVA (Analysis of Variance) ──
k, v = build_lesson(9, 5, "ANOVA (Analysis of Variance)",
    "<h3>ANOVA (Analysis of Variance)</h3>"
    "<p><b>ANOVA</b> tests whether the means of three or more groups are all equal.</p>"
    "<ul><li><b>H₀:</b> μ₁ = μ₂ = … = μₖ (all group means are equal).</li>"
    "<li><b>Hₐ:</b> At least one mean differs.</li>"
    "<li><b>F-statistic:</b> F = (Between-group variability) / (Within-group variability) = MSB / MSW.</li>"
    "<li><b>MSB (Mean Square Between):</b> Measures how much the group means differ from the overall mean.</li>"
    "<li><b>MSW (Mean Square Within):</b> Measures the average variability within each group.</li>"
    "<li><b>If F is large:</b> Between-group differences are large relative to within-group variability → evidence against H₀.</li>"
    "<li><b>Conditions:</b> Independent random samples, approximately normal populations, equal variances across groups.</li>"
    "<li><b>Post-hoc tests:</b> If ANOVA rejects H₀, use follow-up tests (e.g., Tukey's HSD) to identify which means differ.</li></ul>",
    [
        ("ANOVA", "A test comparing means of three or more groups; H₀: all group means are equal."),
        ("F-Statistic", "F = MSB/MSW; a large F suggests group means differ significantly."),
        ("MSB (Mean Square Between)", "Measures variability among the group means (between-group variation)."),
        ("MSW (Mean Square Within)", "Measures average variability within each group (within-group or error variation)."),
        ("Tukey's HSD", "A post-hoc test that identifies which specific pairs of group means differ after ANOVA rejects H₀."),
    ],
    [
        ("ANOVA is used to compare:", ["Two proportions", "*Three or more group means", "Two means only", "Variances only"],
         "ANOVA extends the two-sample t-test to three or more groups."),
        ("H₀ in one-way ANOVA states:", ["All means are different", "*All group means are equal", "Variances differ", "At least one mean differs"],
         "The null hypothesis is that all population means are the same."),
        ("The F-statistic is:", ["MSW/MSB", "*MSB/MSW", "SSB + SSW", "n − 1"],
         "F = between-group variability / within-group variability."),
        ("A large F-value indicates:", ["All means are equal", "*Between-group differences are large relative to within-group variability", "The model is wrong", "Sample size is small"],
         "Large F means group means differ more than expected from random within-group variation."),
        ("MSB measures:", ["Individual data spread", "*How much group means differ from the overall mean", "The residuals", "The total variation"],
         "MSB quantifies between-group variability."),
        ("MSW measures:", ["Group mean differences", "Total variation", "*Average variability within each group", "Between-group spread"],
         "MSW is the pooled within-group variance."),
        ("ANOVA assumes:", ["Non-normal data", "Dependent samples", "*Independent samples, approximate normality, and equal variances", "No assumptions"],
         "Standard ANOVA requires these three conditions."),
        ("If F is close to 1:", ["Reject H₀", "*Within-group and between-group variability are similar — little evidence against H₀", "The test failed", "Means are all different"],
         "F ≈ 1 suggests the groups don't differ more than expected by chance."),
        ("Post-hoc tests are used when:", ["ANOVA fails to reject H₀", "*ANOVA rejects H₀ — to find which specific pairs of means differ", "Before running ANOVA", "To check normality"],
         "Post-hoc tests pinpoint which groups differ."),
        ("Tukey's HSD:", ["Replaces ANOVA", "*Provides pairwise comparisons of group means while controlling the family-wise error rate", "Tests normality", "Tests equal variance"],
         "Tukey's test compares all pairs of means after a significant ANOVA result."),
        ("Why not just do multiple t-tests instead of ANOVA?", ["It's the same thing", "*Multiple t-tests inflate the Type I error rate", "t-tests are more powerful", "ANOVA is less accurate"],
         "Doing many pairwise tests increases the chance of a false rejection."),
        ("SST = SSB + SSW means:", ["*Total variation = Between-group + Within-group variation", "Sum of means", "F = SSB/SSW", "Degrees of freedom add up"],
         "Total variability is partitioned into between and within components."),
        ("df for MSB in one-way ANOVA with k groups:", ["k", "*k − 1", "n − k", "n − 1"],
         "Between-group df = number of groups − 1."),
        ("df for MSW in one-way ANOVA with k groups and n total observations:", ["k − 1", "n − 1", "*n − k", "k"],
         "Within-group df = total observations − number of groups."),
        ("If ANOVA p-value = 0.001:", ["Fail to reject H₀", "*Strong evidence that at least one group mean differs", "All means are identical", "The F-statistic is 0"],
         "Very small p-value = strong evidence against equal means."),
        ("ANOVA is robust to:", ["Any violation", "*Mild departures from normality, especially with large samples", "All assumptions", "Unequal sample sizes only"],
         "ANOVA's F-test is fairly robust to non-normality when samples are large."),
        ("Two-way ANOVA tests:", ["One factor", "*Two factors and their interaction", "Three means", "Only within-group variation"],
         "Two-way ANOVA examines two factors simultaneously and whether they interact."),
        ("An interaction in two-way ANOVA means:", ["Factors are independent", "*The effect of one factor depends on the level of the other", "No main effects exist", "The model is wrong"],
         "Interaction means the combined effect differs from the sum of individual effects."),
        ("The ANOVA table displays:", ["Only the p-value", "*SS, df, MS, F-statistic, and p-value for each source of variation", "Only means", "Only the intercept"],
         "The ANOVA table organizes all key statistics."),
        ("ANOVA originated from the work of:", ["Gauss", "Bayes", "*Sir Ronald Fisher", "Pearson"],
         "Fisher developed ANOVA in the early 20th century."),
    ]
)
lessons[k] = v

# ── 9.6 Nonparametric Tests ──
k, v = build_lesson(9, 6, "Nonparametric Tests",
    "<h3>Nonparametric Tests</h3>"
    "<p><b>Nonparametric tests</b> make fewer assumptions about the population distribution — they don't require normality.</p>"
    "<ul><li><b>When to use:</b> Small samples, ordinal data, heavily skewed distributions, or when normality assumptions are clearly violated.</li>"
    "<li><b>Wilcoxon Signed-Rank Test:</b> Nonparametric alternative to the paired t-test. Uses ranks of differences.</li>"
    "<li><b>Mann-Whitney U Test:</b> Nonparametric alternative to the two-sample t-test. Compares ranks between two independent groups.</li>"
    "<li><b>Kruskal-Wallis Test:</b> Nonparametric alternative to one-way ANOVA. Compares medians of three or more groups.</li>"
    "<li><b>Spearman's Rank Correlation (rₛ):</b> Measures monotonic (not necessarily linear) association between two variables.</li>"
    "<li><b>Trade-off:</b> Nonparametric tests are more flexible but generally have less statistical power than parametric tests when assumptions are met.</li></ul>",
    [
        ("Nonparametric Test", "A test that does not assume a specific population distribution (e.g., normality)."),
        ("Wilcoxon Signed-Rank Test", "Nonparametric alternative to the paired t-test; uses ranks of differences."),
        ("Mann-Whitney U Test", "Nonparametric alternative to the independent two-sample t-test; compares rank sums."),
        ("Kruskal-Wallis Test", "Nonparametric alternative to one-way ANOVA; compares medians across three or more groups."),
        ("Spearman's rₛ", "A rank-based correlation measuring monotonic association — robust to outliers and non-normality."),
    ],
    [
        ("Nonparametric tests are used when:", ["Data is always normal", "*Normality assumptions are violated, data is ordinal, or samples are small", "Parametric tests are unavailable", "The sample size is very large"],
         "They're chosen when parametric assumptions don't hold."),
        ("The Wilcoxon Signed-Rank Test is an alternative to:", ["ANOVA", "Chi-square", "*The paired t-test", "The z-test"],
         "It tests paired differences without assuming normality."),
        ("The Mann-Whitney U Test compares:", ["Means of three groups", "Paired observations", "*Two independent groups using ranks", "Variances"],
         "It compares rank distributions between two independent samples."),
        ("Kruskal-Wallis is the nonparametric alternative to:", ["Paired t-test", "Chi-square test", "*One-way ANOVA", "Two-sample t-test"],
         "It compares medians of three or more groups without normality."),
        ("Spearman's rₛ measures:", ["Only linear association", "*Monotonic association (consistently increasing or decreasing)", "Causation", "Only positive relationships"],
         "rₛ captures any consistent increasing or decreasing trend, not just linear."),
        ("The main trade-off with nonparametric tests:", ["They're always better", "*Less statistical power than parametric tests when assumptions are met", "They require more assumptions", "They can't handle ordinal data"],
         "When parametric assumptions hold, parametric tests are more powerful."),
        ("Statistical power is:", ["The probability of a Type I error", "*The probability of correctly rejecting a false H₀", "Always 1", "The sample size"],
         "Power = 1 − P(Type II error)."),
        ("Nonparametric tests use __ instead of raw data:", ["Means", "Variances", "*Ranks", "Medians only"],
         "Most nonparametric tests are based on ranking the data."),
        ("Ordinal data (ranked categories) is best analyzed with:", ["t-tests", "Regression", "*Nonparametric tests", "Only bar charts"],
         "Ordinal data doesn't meet the assumptions of most parametric tests."),
        ("If a distribution is heavily right-skewed with a small sample:", ["Use a t-test anyway", "*Consider a nonparametric test", "Assume normality", "Increase the mean"],
         "With small n and clear non-normality, nonparametric methods are preferred."),
        ("The sign test is one of the simplest nonparametric tests. It considers:", ["All data values", "Standard deviations", "*Only the signs (+ or −) of differences", "The correlation"],
         "The sign test uses only direction, not magnitude, of differences."),
        ("Nonparametric tests are also called:", ["Normal tests", "*Distribution-free tests", "High-power tests", "Assumption-heavy tests"],
         "They're 'distribution-free' because they don't require specific distributional assumptions."),
        ("Mann-Whitney U and the independent t-test both compare two groups, but Mann-Whitney:", ["Assumes normality", "*Does not assume normality; uses ranks", "Is less appropriate for non-normal data", "Requires equal sample sizes"],
         "Mann-Whitney relaxes the normality assumption."),
        ("If data are normally distributed and the sample is large:", ["Use nonparametric tests", "*Parametric tests are generally preferred (more powerful)", "Both tests give identical results", "Neither test works"],
         "When assumptions are met, parametric tests detect effects better."),
        ("Spearman's rₛ is computed by:", ["Using raw x and y values", "*Ranking both x and y, then computing the Pearson correlation on the ranks", "Squaring Pearson's r", "Taking the absolute value of r"],
         "rₛ = Pearson r applied to the ranked data."),
        ("Nonparametric tests are robust to:", ["Nothing", "*Outliers and non-normal distributions", "Only large samples", "Only continuous data"],
         "Using ranks makes them less sensitive to extreme values and distributional shape."),
        ("For very large samples, the Central Limit Theorem makes parametric tests:", ["Impossible", "*More robust even if the population isn't normal", "Less accurate", "Unnecessary"],
         "CLT guarantees the sampling distribution of the mean is approximately normal for large n."),
        ("The Friedman test is the nonparametric alternative to:", ["One-way ANOVA", "The z-test", "*Repeated-measures ANOVA (within-subjects)", "Regression"],
         "Friedman handles ranked data from repeated measures."),
        ("The efficiency of a nonparametric test relative to its parametric counterpart:", ["Is always 100%", "*Is typically 90–95% for large samples under normal conditions", "Is always 50%", "Is unknown"],
         "Nonparametric tests are nearly as efficient as parametric ones, even when normality holds."),
        ("Bootstrapping is a modern nonparametric approach that:", ["Uses theoretical distributions", "*Resamples from the observed data to estimate the sampling distribution", "Requires normality", "Is the same as the t-test"],
         "Bootstrapping builds an empirical sampling distribution by resampling."),
    ]
)
lessons[k] = v

# ── 9.7 Case Studies in Psychology & Biology ──
k, v = build_lesson(9, 7, "Case Studies in Psychology & Biology",
    "<h3>Case Studies in Psychology & Biology</h3>"
    "<p>Statistics is essential in psychology and biology research.</p>"
    "<ul><li><b>Clinical trials:</b> Randomized controlled trials (RCTs) use hypothesis testing to determine if treatments work. Phases I–IV test safety, efficacy, and long-term effects. Statistics handles placebo effects, double-blinding, and intent-to-treat analysis.</li>"
    "<li><b>Psychology experiments:</b> ANOVA compares groups (e.g., different therapy types). Effect sizes (Cohen's d) measure practical significance beyond p-values.</li>"
    "<li><b>Genetics:</b> Chi-square tests verify if observed genetic ratios match Mendelian predictions. Hardy-Weinberg equilibrium testing uses χ² goodness-of-fit.</li>"
    "<li><b>Ecology:</b> Regression models species abundance vs. environmental factors. Mark-recapture methods estimate population size using the Lincoln-Petersen formula: N̂ = (M × C)/R.</li>"
    "<li><b>Replication crisis:</b> Many published results have failed to replicate, highlighting the importance of proper statistical methods, effect sizes, and pre-registration.</li></ul>",
    [
        ("Randomized Controlled Trial (RCT)", "The gold standard for testing treatments — subjects randomly assigned to treatment or control groups."),
        ("Effect Size (Cohen's d)", "A standardized measure of the magnitude of a difference; d = (x̄₁ − x̄₂)/s_pooled."),
        ("Chi-Square in Genetics", "Used to test if observed genetic ratios match expected Mendelian ratios."),
        ("Mark-Recapture", "A method to estimate population size: N̂ = (M × C)/R, where M = marked, C = captured, R = recaptured marked."),
        ("Replication Crisis", "The finding that many published studies fail to reproduce, emphasizing the need for rigorous statistical practices."),
    ],
    [
        ("The gold standard for testing medical treatments is:", ["Observational study", "*Randomized controlled trial (RCT)", "Case study", "Survey"],
         "RCTs with random assignment and controls provide the strongest causal evidence."),
        ("Double-blinding in a clinical trial means:", ["Only the doctor knows the treatment", "Only the patient knows", "*Neither the patient nor the researcher knows who gets treatment vs. placebo", "Everyone knows"],
         "Double-blinding reduces bias from both patients and researchers."),
        ("Cohen's d measures:", ["p-value", "Sample size", "*The standardized effect size (practical significance)", "Type I error rate"],
         "Cohen's d quantifies how large the difference is in standardized units."),
        ("Cohen's d = 0.8 is generally considered:", ["Small", "Medium", "*Large", "Negligible"],
         "Conventional benchmarks: 0.2 = small, 0.5 = medium, 0.8 = large."),
        ("Chi-square tests in genetics check if observed ratios match:", ["Random expectations", "*Expected Mendelian ratios (e.g., 3:1, 9:3:3:1)", "Normal distribution", "Hardy-Weinberg always"],
         "χ² goodness-of-fit compares observed vs. Mendelian expected frequencies."),
        ("Hardy-Weinberg equilibrium is tested using:", ["ANOVA", "t-test", "*Chi-square goodness-of-fit", "Regression"],
         "χ² checks if observed genotype frequencies match HW expected proportions."),
        ("In mark-recapture, N̂ = (M × C)/R. If M = 100, C = 80, R = 20, then N̂ = ?", ["200", "100", "*400", "500"],
         "N̂ = (100 × 80)/20 = 8000/20 = 400."),
        ("ANOVA is used in psychology to:", ["Study one individual", "*Compare mean outcomes across multiple treatment or therapy groups", "Test genetic ratios", "Calculate effect sizes"],
         "ANOVA compares group means such as different therapy types."),
        ("A p-value of 0.04 with α = 0.05:", ["Fails to reject H₀", "*Rejects H₀ at the 0.05 significance level", "Proves the treatment works", "Is not meaningful"],
         "p < α → reject H₀, providing evidence of a treatment effect."),
        ("The replication crisis refers to:", ["Too many replications", "*Many published findings failing to reproduce in new studies", "Perfect reproducibility", "Excess data"],
         "Numerous studies across psychology and other fields failed to replicate."),
        ("Pre-registration of studies helps combat the replication crisis by:", ["Publishing after data collection", "*Specifying hypotheses and methods before data collection, reducing selective reporting", "Using larger p-values", "Eliminating statistics"],
         "Pre-registration prevents researchers from adjusting hypotheses after seeing data."),
        ("P-hacking refers to:", ["Calculating correct p-values", "*Manipulating data or analyses to obtain significant p-values", "Ignoring statistics", "Publishing null results"],
         "P-hacking inflates false positive rates through selective analysis."),
        ("Clinical trial Phase I primarily tests:", ["Efficacy", "Long-term effects", "*Safety and dosing", "Comparative effectiveness"],
         "Phase I uses small groups to test safety and determine dosage."),
        ("Intent-to-treat analysis includes:", ["Only successful participants", "*All participants as originally assigned, regardless of compliance", "Only the control group", "Only those who completed treatment"],
         "ITT preserves the benefits of randomization."),
        ("An ecological regression might model:", ["Only human behavior", "*Species abundance as a function of temperature, rainfall, and habitat", "Only laboratory data", "Genetic frequencies"],
         "Ecology uses regression to relate environmental factors to biodiversity."),
        ("The placebo effect occurs when:", ["*Patients improve because they believe they're receiving treatment, even if it's inactive", "The drug works perfectly", "Statistics are misused", "The control group receives no treatment"],
         "Placebos can produce real perceived improvements through psychological mechanisms."),
        ("Statistical power in biology experiments is improved by:", ["Smaller samples", "*Larger samples and stronger effect sizes", "Ignoring assumptions", "Using p = 0.10"],
         "Larger n and bigger effects increase the chance of detecting a true effect."),
        ("Multiple comparisons in psychological studies require adjustment because:", ["*Testing many hypotheses inflates the overall Type I error rate", "There are too few participants", "ANOVA is unnecessary", "Adjustments always help"],
         "Bonferroni or other corrections maintain the family-wise error rate."),
        ("Biological data often violates normality, so researchers may use:", ["Only t-tests", "*Nonparametric tests or data transformations", "No statistics", "Only descriptive statistics"],
         "Non-normal biological data benefits from nonparametric methods."),
        ("The importance of effect size in addition to p-values is that:", ["p-values are sufficient alone", "*Effect size shows practical significance — a small p can come from a trivially small effect in a large sample", "Effect size replaces all tests", "They are the same thing"],
         "p-value shows statistical significance; effect size shows how meaningful the finding is."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 9)")
