#!/usr/bin/env python3
"""Generate real content for Statistics Unit 7: Statistical Inference (7 lessons)."""
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

# ── 7.1 Confidence Intervals (mean, proportion) ──
k, v = build_lesson(7, 1, "Confidence Intervals (mean, proportion)",
    "<h3>Confidence Intervals</h3>"
    "<p>A <b>confidence interval (CI)</b> provides a range of plausible values for a population parameter based on sample data.</p>"
    "<p><b>General form:</b> point estimate ± margin of error</p>"
    "<ul><li><b>CI for a mean (σ known):</b> x̄ ± z* · (σ/√n)</li>"
    "<li><b>CI for a mean (σ unknown):</b> x̄ ± t* · (s/√n) using the t-distribution with n−1 degrees of freedom.</li>"
    "<li><b>CI for a proportion:</b> p̂ ± z* · √(p̂(1−p̂)/n)</li>"
    "<li><b>Confidence level (e.g., 95%):</b> In repeated sampling, 95% of such intervals would contain the true parameter.</li>"
    "<li><b>Common z* values:</b> 90% → 1.645, 95% → 1.960, 99% → 2.576.</li>"
    "<li><b>Conditions:</b> Random sample, independence, normality (or large n via CLT), and for proportions: np̂ ≥ 10 and n(1−p̂) ≥ 10.</li></ul>",
    [
        ("Confidence Interval", "A range of values (point estimate ± margin of error) likely to contain the true population parameter at a given confidence level."),
        ("Confidence Level", "The proportion of intervals (e.g., 95%) that would contain the true parameter in repeated sampling."),
        ("Margin of Error", "The maximum expected difference between the sample statistic and the true parameter; half the width of the CI."),
        ("t-Distribution", "A bell-shaped distribution used when σ is unknown; wider than normal, with n−1 degrees of freedom."),
        ("Conditions for CI", "Random sample, independence, and normality checks (or large n); for proportions: np̂ ≥ 10 and n(1−p̂) ≥ 10."),
    ],
    [
        ("A confidence interval gives:", ["The exact parameter value", "*A range of plausible values for the parameter", "A single point estimate", "The probability the parameter is in the range"],
         "CIs provide a range, not a single value."),
        ("The general form of a CI is:", ["*Point estimate ± margin of error", "Sample size ± standard deviation", "Mean ± variance", "p-value ± z*"],
         "CI = estimate ± margin of error."),
        ("A 95% confidence level means:", ["There's a 95% chance the parameter is in THIS interval", "*In 95% of repeated samples, the interval would contain the true parameter", "95% of the data is in the interval", "The margin of error is 95%"],
         "95% refers to the method's long-run success rate, not to any single interval."),
        ("z* for a 95% CI ≈ ?", ["1.645", "*1.960", "2.576", "1.282"],
         "The common z* critical value for 95% confidence is 1.96."),
        ("When σ is unknown, the CI for a mean uses:", ["The z-distribution", "*The t-distribution", "No distribution", "The Poisson distribution"],
         "With σ unknown and estimated by s, we use the t-distribution."),
        ("The t-distribution has __ degrees of freedom for a one-sample CI:", ["n", "n + 1", "*n − 1", "2n"],
         "df = n − 1 for a one-sample t-interval."),
        ("Increasing the confidence level (e.g., from 95% to 99%) makes the interval:", ["Narrower", "*Wider", "The same width", "More precise"],
         "Higher confidence requires a wider interval to be more sure of capturing the parameter."),
        ("Increasing sample size makes the CI:", ["Wider", "*Narrower", "The same", "Invalid"],
         "Larger n reduces the margin of error (σ/√n decreases)."),
        ("The CI for a proportion is p̂ ± z*√(p̂(1−p̂)/n). The check requires:", ["n ≥ 30", "p̂ = 0.5", "*np̂ ≥ 10 and n(1−p̂) ≥ 10", "σ is known"],
         "These conditions ensure the sampling distribution is approximately normal."),
        ("If x̄ = 50, s = 10, n = 25, t* = 2.064 for 95% CI, the interval is:", ["50 ± 10", "50 ± 20.64", "*50 ± 2.064(10/5) = 50 ± 4.128", "50 ± 2.064"],
         "CI = 50 ± 2.064 × (10/√25) = 50 ± 2.064 × 2 = 50 ± 4.128."),
        ("A CI does NOT tell us:", ["*The probability the true parameter is in this specific interval", "A range of plausible values", "The margin of error", "The confidence level"],
         "Once computed, the parameter is either in the interval or not — probability applies to the method."),
        ("For a 90% CI, z* ≈ ?", ["1.960", "*1.645", "2.576", "1.282"],
         "z* = 1.645 for 90% confidence."),
        ("The margin of error for a proportion depends on:", ["Only n", "Only p̂", "*Both p̂ and n (and the confidence level)", "The population size"],
         "ME = z*√(p̂(1−p̂)/n) involves p̂, n, and z*."),
        ("To halve the margin of error, you need to __ the sample size:", ["Double", "Halve", "*Quadruple (multiply by 4)", "Keep the same"],
         "ME is proportional to 1/√n. To halve ME, n must increase by a factor of 4."),
        ("If a 95% CI for a mean is (42, 58), the point estimate is:", ["42", "58", "*50", "16"],
         "The point estimate is the midpoint: (42 + 58)/2 = 50."),
        ("A random sample is required for a valid CI because:", ["It increases the mean", "*It ensures the sample is representative, making the CI reliable", "It guarantees an exact answer", "It reduces the confidence level"],
         "Random sampling makes the statistical theory underlying CIs valid."),
        ("The width of a CI is:", ["The point estimate", "The margin of error", "*Twice the margin of error", "The confidence level"],
         "Width = upper bound − lower bound = 2 × ME."),
        ("The t-distribution is __ than the normal distribution:", ["*Wider (heavier tails) but approaches normal as n increases", "Narrower", "Identical for all n", "Taller"],
         "The t has fatter tails to account for the additional uncertainty from estimating σ."),
        ("A CI for a mean requires:", ["*A random sample, independence, and checking normality (or n ≥ 30)", "Only a large sample", "Only a random sample", "No conditions"],
         "All conditions must be checked before constructing a CI."),
        ("p̂ = 0.6, n = 200, 95% CI for the proportion:", ["*0.6 ± 1.96√(0.6×0.4/200) ≈ 0.6 ± 0.068", "0.6 ± 0.02", "0.6 ± 0.3", "0.6 ± 1.96"],
         "ME = 1.96 × √(0.24/200) = 1.96 × 0.0346 ≈ 0.068."),
    ]
)
lessons[k] = v

# ── 7.2 Margin of Error ──
k, v = build_lesson(7, 2, "Margin of Error",
    "<h3>Margin of Error</h3>"
    "<p>The <b>margin of error (ME)</b> quantifies the precision of a sample estimate.</p>"
    "<ul><li><b>For a mean:</b> ME = z* · (σ/√n) or t* · (s/√n).</li>"
    "<li><b>For a proportion:</b> ME = z* · √(p̂(1−p̂)/n).</li>"
    "<li><b>Interpretation:</b> We are [confidence level]% confident that the true parameter is within ME of our estimate.</li></ul>"
    "<p><b>Factors affecting ME:</b></p>"
    "<ul><li>↑ Confidence level → ↑ ME (wider interval).</li>"
    "<li>↑ Sample size (n) → ↓ ME (more precise).</li>"
    "<li>↑ Variability (σ or s) → ↑ ME (less precise).</li></ul>"
    "<p><b>Sample size determination:</b> To achieve a desired ME, solve for n. For a proportion: n = (z*/ME)² · p̂(1−p̂). When p̂ is unknown, use p̂ = 0.5 (maximum variability, most conservative).</p>",
    [
        ("Margin of Error", "The maximum expected distance between the sample estimate and the true population parameter."),
        ("Factors Increasing ME", "Higher confidence level, smaller sample size, and greater variability all increase the margin of error."),
        ("Sample Size for Desired ME", "n = (z*/ME)² · p̂(1−p̂) for proportions; use p̂ = 0.5 when the proportion is unknown."),
        ("Precision", "A smaller margin of error means greater precision — the estimate is closer to the true value."),
        ("Conservative Estimate", "Using p̂ = 0.5 when planning sample size gives the largest required n, ensuring adequate precision."),
    ],
    [
        ("A smaller margin of error means:", ["Less precision", "*Greater precision", "Higher confidence", "A larger sample is not needed"],
         "Smaller ME = the estimate is closer to the true value."),
        ("Increasing the sample size:", ["*Decreases the margin of error", "Increases the margin of error", "Has no effect", "Changes the confidence level"],
         "ME decreases as n increases (ME ∝ 1/√n)."),
        ("Increasing the confidence level:", ["Decreases ME", "*Increases ME", "Has no effect on ME", "Reduces sample size needed"],
         "Higher confidence requires a wider interval (larger z*)."),
        ("Greater variability (larger σ):", ["*Increases ME", "Decreases ME", "Has no effect", "Eliminates ME"],
         "More spread in the data leads to less precise estimates."),
        ("ME for a proportion with p̂ = 0.5 is the __ margin for a given n and confidence:", ["Smallest", "*Largest", "Average", "Zero"],
         "p̂(1−p̂) is maximized at p̂ = 0.5, giving the largest possible ME."),
        ("To find the sample size needed for ME = 0.03 at 95% confidence with p̂ = 0.5:", ["n = 30", "n = 100", "*n = (1.96/0.03)² × 0.25 ≈ 1068", "n = 500"],
         "n = (1.96/0.03)² × 0.25 = 4268.44 × 0.25 ≈ 1068."),
        ("The margin of error only accounts for:", ["All errors", "Bias", "*Sampling variability (random error)", "Nonresponse bias"],
         "ME reflects random sampling error, not systematic biases."),
        ("A poll reports 60% ± 4%. The 4% is the:", ["Confidence level", "p-value", "*Margin of error", "Standard deviation"],
         "The ± value in poll results is the margin of error."),
        ("ME = z* · σ/√n — doubling n reduces ME by a factor of:", ["2", "*√2 ≈ 1.41", "4", "1/2"],
         "Since ME ∝ 1/√n, doubling n divides ME by √2."),
        ("To cut ME in half, you need to multiply n by:", ["2", "*4", "1/2", "8"],
         "ME ∝ 1/√n, so halving ME requires quadrupling n."),
        ("If σ = 15, n = 100, z* = 1.96, ME = ?", ["15", "1.96", "*2.94", "0.15"],
         "ME = 1.96 × 15/√100 = 1.96 × 1.5 = 2.94."),
        ("A larger ME indicates:", ["A more precise estimate", "*A less precise estimate", "A higher sample size", "A lower confidence level"],
         "Larger ME means less certainty about where the true parameter lies."),
        ("The margin of error does NOT account for:", ["Random sampling error", "Sample size effects", "*Biases like selection bias or response bias", "Confidence level"],
         "ME only captures random sampling variability, not systematic errors."),
        ("When p̂ is unknown and you're planning sample size:", ["Use p̂ = 0", "Use p̂ = 1", "*Use p̂ = 0.5 (conservative)", "Don't plan at all"],
         "p̂ = 0.5 maximizes the required sample size, ensuring adequate precision."),
        ("ME for a mean with unknown σ uses __ instead of z*:", ["A normal distribution", "*t* (t critical value)", "A chi-square value", "F value"],
         "When σ is estimated by s, the t-distribution accounts for extra uncertainty."),
        ("A 99% CI has a __ ME than a 95% CI (same n and σ):", ["Smaller", "*Larger", "Same", "Zero"],
         "Higher confidence → larger z* → larger ME."),
        ("In news polls, the reported ME usually assumes:", ["A biased sample", "p = 0", "*p = 0.5 and 95% confidence", "No margin at all"],
         "Most reported MEs assume maximum variability (p = 0.5) with 95% confidence."),
        ("If a CI is (45, 55), the ME is:", ["45", "55", "100", "*5"],
         "ME = (55 − 45)/2 = 5."),
        ("Non-sampling errors (bias) __ by increasing n:", ["Are reduced", "*Are NOT reduced", "Disappear", "Double"],
         "Only random sampling error decreases with n; biases require methodological fixes."),
        ("The ideal ME for an important study is:", ["As large as possible", "*As small as practical (high precision)", "Always zero", "Always 5%"],
         "Smaller ME provides more useful information, though cost and feasibility matter."),
    ]
)
lessons[k] = v

# ── 7.3 Hypothesis Testing ──
k, v = build_lesson(7, 3, "Hypothesis Testing (null vs. alternative)",
    "<h3>Hypothesis Testing</h3>"
    "<p><b>Hypothesis testing</b> is a formal procedure for using data to evaluate a claim about a population parameter.</p>"
    "<ul><li><b>Null hypothesis (H₀):</b> The default claim — often 'no effect' or 'no difference.' Assumed true until evidence suggests otherwise.</li>"
    "<li><b>Alternative hypothesis (Hₐ):</b> The claim that contradicts H₀ — what the researcher believes or wants to show.</li>"
    "<li><b>Test statistic:</b> A z-score or t-score computed from the sample data measuring how far the sample result is from H₀.</li>"
    "<li><b>P-value:</b> The probability of obtaining results as extreme (or more extreme) than observed, assuming H₀ is true.</li>"
    "<li><b>Decision:</b> If p-value ≤ α, reject H₀ (statistically significant). If p-value > α, fail to reject H₀.</li>"
    "<li><b>Significance level (α):</b> The threshold (usually 0.05) for deciding statistical significance.</li></ul>"
    "<p><b>Steps:</b> (1) State H₀ and Hₐ. (2) Choose α. (3) Compute the test statistic. (4) Find the p-value. (5) Make a decision and state a conclusion in context.</p>",
    [
        ("Null Hypothesis (H₀)", "The default claim of no effect or no difference; assumed true until evidence suggests otherwise."),
        ("Alternative Hypothesis (Hₐ)", "The claim the researcher wants to support; contradicts H₀."),
        ("P-value", "The probability of observing results as extreme or more extreme than the sample, assuming H₀ is true."),
        ("Significance Level (α)", "The threshold for rejecting H₀; commonly set at 0.05."),
        ("Test Statistic", "A standardized value (z or t) measuring how far the sample result is from what H₀ predicts."),
    ],
    [
        ("The null hypothesis typically states:", ["The research claim", "*No effect or no difference", "The alternative is true", "The sample is normal"],
         "H₀ is the status quo — no effect, no difference."),
        ("The alternative hypothesis is:", ["Always H₀", "*What the researcher wants to show (contradicts H₀)", "Always two-sided", "The null reversed"],
         "Hₐ is the claim supported by evidence against H₀."),
        ("A small p-value provides:", ["Evidence FOR H₀", "*Evidence AGAINST H₀", "No information", "Proof H₀ is true"],
         "Small p-values mean the observed data is unlikely under H₀."),
        ("If p-value = 0.03 and α = 0.05:", ["Fail to reject H₀", "*Reject H₀ (statistically significant)", "Accept H₀", "Increase α"],
         "0.03 < 0.05, so we reject H₀."),
        ("If p-value = 0.12 and α = 0.05:", ["*Fail to reject H₀", "Reject H₀", "Accept Hₐ", "The test is invalid"],
         "0.12 > 0.05, so we fail to reject H₀."),
        ("The significance level α is set:", ["*Before conducting the test", "After seeing the p-value", "After collecting data", "It doesn't matter when"],
         "α must be predetermined to avoid bias."),
        ("'Fail to reject H₀' means:", ["H₀ is proven true", "*There is insufficient evidence to reject H₀", "Hₐ is false", "The test failed"],
         "We never prove H₀ true — we simply lack enough evidence against it."),
        ("The test statistic measures:", ["The sample size", "The confidence level", "*How far the sample result is from H₀'s predicted value, in standard errors", "The margin of error"],
         "The test statistic standardizes the distance between the observed and expected values."),
        ("A two-tailed test is used when Hₐ states:", ["Parameter > value", "Parameter < value", "*Parameter ≠ value (different in either direction)", "Parameter = value"],
         "Two-tailed tests look for differences in both directions."),
        ("A one-tailed test is used when Hₐ states:", ["Parameter ≠ value", "*Parameter > value or parameter < value (one direction)", "Parameter = value", "Nothing specific"],
         "One-tailed tests look for an effect in a specific direction."),
        ("Statistical significance means:", ["The result is practically important", "*The result is unlikely to have occurred by chance alone (p ≤ α)", "The null is true", "The sample is large"],
         "Statistical significance = unlikely under H₀, not necessarily practically important."),
        ("The common α level in statistics is:", ["0.10", "*0.05", "0.50", "0.01"],
         "α = 0.05 is the most widely used significance level."),
        ("Rejecting H₀ when it is actually true is:", ["Correct", "*A Type I error", "A Type II error", "Impossible"],
         "Rejecting a true H₀ is a Type I error."),
        ("The p-value is NOT:", ["A probability", "Dependent on the data", "*The probability that H₀ is true", "Used to make a decision"],
         "The p-value is the probability of data this extreme given H₀, not the probability that H₀ is true."),
        ("Steps of a hypothesis test (in order):", ["*State hypotheses → choose α → compute test statistic → find p-value → conclude", "Find p-value → state hypotheses → conclude", "Choose α → reject H₀ → state hypotheses", "Collect data → make conclusion → state H₀"],
         "The formal steps must be followed in order."),
        ("A z-test for proportions uses the formula:", ["z = x̄/s", "*z = (p̂ − p₀) / √(p₀(1−p₀)/n)", "z = (x̄ − μ) / σ", "z = n/p"],
         "The z-statistic for a proportion compares p̂ to the hypothesized p₀."),
        ("H₀: μ = 50, Hₐ: μ > 50 is a:", ["Two-tailed test", "*One-tailed (right-tailed) test", "Left-tailed test", "No test"],
         "Hₐ: μ > 50 specifies a direction — right-tailed."),
        ("The conclusion of a hypothesis test should be stated:", ["In statistical jargon only", "*In the context of the problem", "Using only numbers", "Without reference to H₀"],
         "Always interpret results in the real-world context."),
        ("A hypothesis test begins with:", ["Collecting data", "Computing the p-value", "*Stating H₀ and Hₐ", "Making a decision"],
         "Hypotheses are formulated before data analysis."),
        ("'Statistically significant' does NOT necessarily mean:", ["The p-value is small", "H₀ was rejected", "*The result is large or practically important", "The test was conducted properly"],
         "Statistical significance and practical significance are different concepts."),
    ]
)
lessons[k] = v

# ── 7.4 Type I & Type II Errors ──
k, v = build_lesson(7, 4, "Type I & Type II Errors",
    "<h3>Type I & Type II Errors</h3>"
    "<p>When making decisions based on hypothesis tests, two types of errors can occur.</p>"
    "<ul><li><b>Type I error (false positive):</b> Rejecting H₀ when H₀ is actually true. Probability = α (significance level).</li>"
    "<li><b>Type II error (false negative):</b> Failing to reject H₀ when H₀ is actually false (Hₐ is true). Probability = β.</li>"
    "<li><b>Power = 1 − β:</b> The probability of correctly rejecting a false H₀. Higher power = better ability to detect a real effect.</li></ul>"
    "<p><b>Trade-offs:</b></p>"
    "<ul><li>Decreasing α → decreases Type I error but increases Type II error (harder to reject H₀).</li>"
    "<li>Increasing sample size → increases power (reduces β) without changing α.</li>"
    "<li>Larger true effect size → easier to detect → higher power.</li></ul>"
    "<table><tr><th></th><th>H₀ True</th><th>H₀ False</th></tr>"
    "<tr><td>Reject H₀</td><td>Type I error (α)</td><td>Correct (Power = 1−β)</td></tr>"
    "<tr><td>Fail to reject H₀</td><td>Correct</td><td>Type II error (β)</td></tr></table>",
    [
        ("Type I Error", "Rejecting H₀ when it is actually true (false positive); probability = α."),
        ("Type II Error", "Failing to reject H₀ when it is actually false (false negative); probability = β."),
        ("Power", "1 − β; the probability of correctly rejecting a false H₀."),
        ("Alpha (α)", "The probability of a Type I error; also the significance level."),
        ("Effect Size", "The magnitude of the true difference from H₀; larger effects are easier to detect (higher power)."),
    ],
    [
        ("A Type I error occurs when:", ["You fail to reject a false H₀", "*You reject a true H₀", "You correctly reject H₀", "You correctly fail to reject H₀"],
         "Type I = false positive = rejecting H₀ when it's true."),
        ("A Type II error occurs when:", ["You reject a true H₀", "*You fail to reject a false H₀", "You correctly reject H₀", "You correctly fail to reject H₀"],
         "Type II = false negative = missing a real effect."),
        ("P(Type I error) = ?", ["β", "1 − α", "*α", "Power"],
         "The probability of a Type I error is the significance level α."),
        ("P(Type II error) = ?", ["α", "1 − α", "*β", "Power"],
         "β is the probability of failing to detect a real effect."),
        ("Power = ?", ["α", "β", "*1 − β", "1 − α"],
         "Power = 1 − β = probability of correctly rejecting a false H₀."),
        ("Decreasing α:", ["*Reduces Type I error but increases Type II error", "Reduces both errors", "Increases Type I error", "Has no effect on errors"],
         "Lowering α makes it harder to reject H₀, reducing false positives but increasing false negatives."),
        ("Increasing the sample size:", ["Increases both errors", "Has no effect", "*Increases power (reduces β) without changing α", "Increases α"],
         "Larger samples provide more information, improving the ability to detect real effects."),
        ("A medical test falsely says a healthy person has a disease. This is a:", ["*Type I error (false positive)", "Type II error", "Correct decision", "Not an error"],
         "Saying someone has a disease when they don't = false positive = Type I."),
        ("A medical test fails to detect an actual disease. This is a:", ["Type I error", "*Type II error (false negative)", "Correct decision", "Not an error"],
         "Missing a real disease = false negative = Type II."),
        ("Higher power means:", ["*Better ability to detect a real effect", "More Type I errors", "Lower sample size needed", "Higher β"],
         "Power is the probability of finding a real effect when it exists."),
        ("A larger effect size makes it:", ["*Easier to detect (higher power)", "Harder to detect", "Impossible to detect", "Unrelated to power"],
         "Bigger effects produce larger test statistics, making detection easier."),
        ("In a jury trial, a Type I error is:", ["*Convicting an innocent person", "Acquitting a guilty person", "A correct verdict", "Declaring a mistrial"],
         "H₀ = innocent. Rejecting H₀ when true = convicting an innocent person."),
        ("In a jury trial, a Type II error is:", ["Convicting an innocent person", "*Acquitting a guilty person", "A correct verdict", "Declaring a mistrial"],
         "Failing to reject H₀ when false = letting a guilty person go free."),
        ("Power increases with:", ["Smaller sample size", "Smaller effect size", "Smaller α", "*Larger sample size, larger effect size, or larger α"],
         "All three factors increase the ability to detect real effects."),
        ("α = 0.01 instead of 0.05 means:", ["*Less chance of Type I error but more chance of Type II error", "More chance of Type I error", "No change in errors", "Both errors decrease"],
         "Stricter α reduces false positives but makes false negatives more likely."),
        ("The ideal study has:", ["Low power", "High α and high β", "*Low α, low β (high power)", "No hypothesis"],
         "Minimizing both error types is the goal of good study design."),
        ("If power = 0.80, β = ?", ["0.80", "*0.20", "0.05", "0.95"],
         "β = 1 − power = 1 − 0.80 = 0.20."),
        ("You can never make a Type I error if:", ["*You never reject H₀", "You always reject H₀", "n is large", "α = 0.05"],
         "If you never reject H₀, you can't falsely reject it (but you risk Type II errors)."),
        ("A study with n = 10 vs. n = 1000 (same α): which has more power?", ["n = 10", "*n = 1000", "They're equal", "Cannot determine"],
         "Larger samples have more power to detect effects."),
        ("The consequences of errors should influence:", ["Nothing", "*The choice of α (e.g., lower α for more serious Type I consequences)", "Only sample size", "Only the alternative hypothesis"],
         "When false positives are especially costly, use a smaller α."),
    ]
)
lessons[k] = v

# ── 7.5 P-values & Significance Levels ──
k, v = build_lesson(7, 5, "P-values & Significance Levels",
    "<h3>P-values & Significance Levels</h3>"
    "<p>The <b>p-value</b> is the probability of obtaining a test statistic as extreme (or more extreme) than the one observed, assuming H₀ is true.</p>"
    "<ul><li><b>Small p-value:</b> The observed data is unlikely under H₀ → evidence against H₀.</li>"
    "<li><b>Large p-value:</b> The observed data is consistent with H₀ → insufficient evidence against H₀.</li>"
    "<li><b>Decision rule:</b> If p-value ≤ α, reject H₀. If p-value > α, fail to reject H₀.</li></ul>"
    "<p><b>Common misconceptions:</b></p>"
    "<ul><li>The p-value is NOT the probability that H₀ is true.</li>"
    "<li>The p-value is NOT the probability of making an error.</li>"
    "<li>A statistically significant result is not necessarily practically important.</li>"
    "<li>A non-significant result does not prove H₀ is true.</li></ul>"
    "<p><b>Effect size</b> and <b>confidence intervals</b> should accompany p-values to provide a fuller picture.</p>",
    [
        ("P-value Definition", "The probability of observing data as extreme or more extreme than what was observed, assuming H₀ is true."),
        ("Significance Level (α)", "The pre-set threshold for p-value comparison; typically 0.05. If p ≤ α, reject H₀."),
        ("Statistical vs. Practical Significance", "A result can be statistically significant (small p) but not practically meaningful (small effect)."),
        ("P-value Misconception", "The p-value is NOT the probability that H₀ is true—it's the probability of the data given H₀."),
        ("Effect Size", "A measure of the magnitude of a difference or relationship, complementing the p-value."),
    ],
    [
        ("The p-value measures:", ["The probability H₀ is true", "*The probability of data this extreme, assuming H₀ is true", "The probability of the sample", "The Type I error rate"],
         "The p-value is calculated under the assumption that H₀ is true."),
        ("If p = 0.001:", ["*Strong evidence against H₀", "Strong evidence for H₀", "No evidence either way", "H₀ is proven true"],
         "A very small p-value provides strong evidence against H₀."),
        ("If p = 0.45:", ["*Insufficient evidence to reject H₀", "Strong evidence against H₀", "H₀ is proven true", "Hₐ is proven false"],
         "A large p-value means the data is consistent with H₀."),
        ("Statistical significance is achieved when:", ["p > α", "*p ≤ α", "p = 1", "p = α/2"],
         "We reject H₀ when the p-value is at or below α."),
        ("A p-value of 0.05 at α = 0.05:", ["Fails to reject H₀", "*Rejects H₀ (borderline significant)", "Proves H₀", "Is invalid"],
         "p ≤ α, so we (barely) reject H₀."),
        ("The p-value is NOT:", ["A probability", "Dependent on data", "*The probability that H₀ is true", "Used in decision making"],
         "This is the most common misconception about p-values."),
        ("A small p-value with a tiny effect size suggests:", ["A large practical effect", "*Statistical significance but questionable practical importance", "H₀ is true", "The sample is too small"],
         "Large samples can detect tiny, practically meaningless differences."),
        ("p = 0.06 at α = 0.05 means:", ["Reject H₀", "*Fail to reject H₀ (not statistically significant at this α)", "H₀ is false", "Increase α"],
         "0.06 > 0.05, so we don't reject H₀."),
        ("Two-tailed p-value is __ a one-tailed p-value for the same test statistic:", ["Half", "*Double", "Equal to", "Unrelated to"],
         "A two-tailed test considers both directions, so p is doubled."),
        ("Reporting only significant results (publication bias) can:", ["Improve science", "*Distort the literature by hiding non-significant findings", "Reduce Type I errors", "Increase power"],
         "Publishing only significant results gives a misleading picture."),
        ("A confidence interval of (−0.5, 3.2) for a difference includes 0, suggesting:", ["*The difference is not statistically significant at that confidence level", "The difference is significant", "The data is invalid", "The CI is wrong"],
         "If 0 is in the CI for a difference, we can't reject H₀: no difference."),
        ("'The p-value is the probability of making a Type I error' is:", ["Correct", "*Incorrect — α is the Type I error rate, not the p-value", "Sometimes true", "Always true"],
         "α is the fixed Type I error rate; the p-value is a measure from the data."),
        ("Effect size measures:", ["*The magnitude of the observed effect", "The p-value", "The sample size", "The significance level"],
         "Effect size quantifies how large the difference or relationship is."),
        ("A very large sample can produce a small p-value for:", ["Only large effects", "*Even trivially small effects", "Nothing", "Only meaningful differences"],
         "Statistical power increases with n, so even tiny effects become 'significant.'"),
        ("Failing to reject H₀ proves:", ["H₀ is true", "*Nothing — there may not be enough evidence to detect a real effect", "Hₐ is true", "The test was wrong"],
         "Absence of evidence is not evidence of absence."),
        ("The p-value depends on:", ["Only α", "Only the sample size", "*The sample data, sample size, and the test used", "Nothing — it's always 0.05"],
         "The p-value is computed from the data and methodology."),
        ("Cohen's d is a measure of:", ["P-value", "Significance", "*Effect size for means (difference in standard deviations)", "Sample size"],
         "Cohen's d = (x̄₁ − x̄₂)/pooled SD; it quantifies the size of the difference."),
        ("If α = 0.01, you need __ evidence to reject H₀ compared to α = 0.05:", ["Less", "*Stronger (smaller p-value)", "The same", "No"],
         "A smaller α requires more convincing evidence."),
        ("Best practice: report both the p-value and:", ["Only the sample size", "Only the hypothesis", "*Effect size and confidence intervals", "Nothing else"],
         "P-values alone don't tell the full story."),
        ("The American Statistical Association warns against:", ["Using statistics", "Collecting data", "*Using p-values as the sole basis for decisions or as a measure of evidence of a model", "Reporting confidence intervals"],
         "The ASA's 2016 statement emphasized p-values require context and complementary analysis."),
    ]
)
lessons[k] = v

# ── 7.6 Interpreting Statistical Results ──
k, v = build_lesson(7, 6, "Interpreting Statistical Results",
    "<h3>Interpreting Statistical Results</h3>"
    "<p>Correct interpretation of statistical results is just as important as the calculations themselves.</p>"
    "<ul><li><b>Context:</b> Always state conclusions in the context of the problem, not just 'reject H₀.'</li>"
    "<li><b>Statistical vs. practical significance:</b> A statistically significant result (small p) may have a trivially small effect. Always check effect size.</li>"
    "<li><b>Confidence interval interpretation:</b> 'We are 95% confident that the true [parameter] is between [a] and [b].'</li>"
    "<li><b>Association vs. causation:</b> Observational studies can show association but not cause-and-effect. Only randomized experiments establish causation.</li>"
    "<li><b>Generalizability:</b> Results generalize only to the population from which the sample was drawn.</li>"
    "<li><b>Limitations:</b> Acknowledge assumptions, potential biases, and the scope of conclusions.</li></ul>"
    "<p><b>Common mistakes:</b> Confusing correlation with causation, misinterpreting p-values, ignoring assumptions, and overgeneralizing results.</p>",
    [
        ("Contextual Interpretation", "Stating statistical conclusions in terms of the real-world problem, not just statistical jargon."),
        ("Association vs. Causation", "Association (correlation) means variables are related; causation means one variable causes changes in another."),
        ("Practical Significance", "Whether a statistically significant result is large enough to matter in the real world."),
        ("Generalizability", "The extent to which results from a sample can be applied to the broader population."),
        ("Limitations", "Acknowledged weaknesses of a study, including assumptions, potential biases, and scope of conclusions."),
    ],
    [
        ("Statistical results should always be interpreted:", ["In abstract terms", "*In the context of the problem", "Without reference to the data", "Using only numbers"],
         "Context makes results meaningful and understandable."),
        ("'Correlation does not imply causation' means:", ["Correlation is useless", "Causation implies correlation", "*An observed association doesn't prove one variable causes changes in the other", "All correlations are zero"],
         "Other factors (confounders) may explain the relationship."),
        ("A statistically significant result:", ["Is always practically important", "*May not be practically meaningful — check effect size", "Proves the theory", "Means H₀ is true"],
         "Statistical significance relates to the p-value; practical significance relates to the effect size."),
        ("Results from a sample of college students generalize to:", ["All humans", "All college students worldwide", "*The population from which the sample was drawn", "No one"],
         "Generalizability depends on how the sample was selected."),
        ("A study finds r = 0.95 between ice cream sales and drowning. This means:", ["*The variables are correlated but likely share a common cause (hot weather)", "Ice cream causes drowning", "Drowning causes ice cream sales", "The data is wrong"],
         "A lurking variable (temperature) explains both increases."),
        ("'We are 95% confident the true mean is between 40 and 60' means:", ["There's a 95% chance μ is in this interval", "*In 95% of repeated samples, the method would produce an interval containing μ", "95% of the data is between 40 and 60", "μ is definitely between 40 and 60"],
         "Confidence refers to the method's long-run performance."),
        ("Acknowledging limitations:", ["Weakens the study", "*Strengthens credibility and helps readers evaluate the findings", "Is unnecessary", "Should be avoided"],
         "Transparency about limitations builds trust in the results."),
        ("Overgeneralizing results means:", ["*Applying findings beyond the population actually studied", "Being too cautious", "Having a large sample", "Using a 99% CI"],
         "Results should only be applied to the relevant population."),
        ("A CI containing 0 for a treatment difference suggests:", ["The treatment works", "*The treatment may have no effect", "The data is invalid", "The CI is wrong"],
         "Zero in the CI means we can't conclusively say there's a difference."),
        ("The best conclusion from a hypothesis test includes:", ["*Decision, p-value, effect size, and context", "Only 'reject' or 'fail to reject'", "Only the p-value", "Only the test statistic"],
         "A complete conclusion uses all relevant information."),
        ("A study with p = 0.04 and a very tiny effect size should be interpreted as:", ["Very important", "*Statistically significant but questionable practical importance", "Proof of a large effect", "Invalid"],
         "A tiny effect, even if significant, may not matter in practice."),
        ("Randomized experiments can establish:", ["Only association", "*Causation (cause-and-effect)", "Only correlation", "Nothing useful"],
         "Random assignment and control groups allow causal conclusions."),
        ("Observational studies can establish:", ["Causation", "*Association (but not causation)", "Nothing", "Both causation and randomization"],
         "Without random assignment, confounders prevent causal conclusions."),
        ("If assumptions of a test are violated:", ["Results are always correct", "*Results may be unreliable", "Nothing changes", "Assumptions don't matter"],
         "Violated assumptions can invalidate statistical conclusions."),
        ("Multiple comparisons (testing many hypotheses at once) increase the risk of:", ["*Type I errors (false positives)", "Type II errors only", "No errors", "Practical significance"],
         "More tests mean more chances for false positives."),
        ("The Bonferroni correction:", ["*Adjusts α to account for multiple comparisons (divides by number of tests)", "Ignores multiple testing", "Only applies to CIs", "Doubles the p-value"],
         "Bonferroni uses α/k to control the overall Type I error rate."),
        ("A forest plot in a meta-analysis shows:", ["A single study's result", "*Effect sizes and confidence intervals from multiple studies", "Data trees", "Sampling distributions"],
         "Forest plots visually summarize multiple studies."),
        ("When reporting results, researchers should:", ["Hide negative results", "*Report all findings, including those that don't support their hypothesis", "Only report significant results", "Exaggerate effects"],
         "Complete reporting maintains scientific integrity."),
        ("'Statistically significant' ≠:", ["*'Important' or 'meaningful'", "'Calculated correctly'", "'Based on data'", "'Involving a p-value'"],
         "Significance reflects the p-value, not the practical importance."),
        ("The best studies include:", ["Only p-values", "No limitations section", "*Effect sizes, confidence intervals, context, and acknowledged limitations", "Only graphs"],
         "Complete reporting helps readers fully evaluate the findings."),
    ]
)
lessons[k] = v

# ── 7.7 Case Studies in Medical Trials ──
k, v = build_lesson(7, 7, "Case Studies in Medical Trials",
    "<h3>Case Studies in Medical Trials</h3>"
    "<p>Medical trials (clinical trials) are among the most rigorous applications of statistical inference.</p>"
    "<ul><li><b>Phases:</b><ul>"
    "<li>Phase I: Safety and dosage (small group).</li>"
    "<li>Phase II: Efficacy and side effects (larger group).</li>"
    "<li>Phase III: Compared to standard treatment or placebo (large RCT).</li>"
    "<li>Phase IV: Post-market surveillance.</li></ul></li>"
    "<li><b>Randomized Controlled Trials (RCTs):</b> The gold standard. Random assignment + control group + blinding.</li>"
    "<li><b>Intention-to-treat (ITT):</b> Analyzing participants in their originally assigned groups regardless of compliance — prevents bias.</li>"
    "<li><b>Key examples:</b><ul>"
    "<li>Salk polio vaccine trial (1954): 1.8 million children, double-blind, proved vaccine efficacy.</li>"
    "<li>Framingham Heart Study: Long-running observational study identifying heart disease risk factors.</li>"
    "<li>COVID-19 vaccine trials: Phase III RCTs with 30,000+ participants establishing safety and efficacy.</li></ul></li></ul>",
    [
        ("Clinical Trial Phases", "Phase I (safety), Phase II (efficacy), Phase III (large RCT comparison), Phase IV (post-market surveillance)."),
        ("Randomized Controlled Trial (RCT)", "The gold standard study design using random assignment, control groups, and often blinding."),
        ("Intention-to-Treat (ITT)", "Analyzing all participants in their originally assigned groups regardless of adherence to maintain randomization benefits."),
        ("Double-Blind Trial", "Neither participants nor researchers know group assignments, minimizing bias from expectations."),
        ("Placebo Effect", "Improvement in patients receiving an inactive treatment, due to their belief that they are receiving real therapy."),
    ],
    [
        ("The gold standard for clinical research is:", ["Observational study", "Case study", "*Randomized controlled trial (RCT)", "Expert opinion"],
         "RCTs with random assignment and controls provide the strongest causal evidence."),
        ("Phase I trials focus on:", ["*Safety and dosage in a small group", "Large-scale efficacy", "Post-market effects", "Marketing"],
         "Phase I establishes safety and tolerable dose ranges."),
        ("Phase III trials:", ["Use only 10 people", "*Compare the treatment to a placebo or standard in a large RCT", "Focus only on safety", "Are optional"],
         "Phase III is the large-scale comparative efficacy trial."),
        ("The Salk polio vaccine trial (1954) was landmark because:", ["It used no control", "*It was a massive double-blind RCT with 1.8 million children", "It failed", "It was observational"],
         "The Salk trial set the standard for large-scale clinical trials."),
        ("Intention-to-treat analysis:", ["Includes only compliant patients", "*Includes all participants in their original groups regardless of compliance", "Excludes dropouts", "Is biased by design"],
         "ITT preserves the benefits of randomization."),
        ("Double-blinding prevents bias from:", ["Large sample sizes", "*Both participants' and researchers' expectations", "Random assignment", "Data collection only"],
         "Neither party's expectations can influence the outcome."),
        ("The placebo effect shows that:", ["Placebos are real treatments", "*Belief in treatment can produce real improvements", "All treatments work equally", "Placebos are always used"],
         "The mind's expectation of improvement can cause measurable changes."),
        ("The Framingham Heart Study is:", ["A clinical trial", "*A long-running observational study of heart disease risk factors", "A genetics study only", "A Phase III trial"],
         "Framingham has followed participants for decades identifying risks like smoking and high cholesterol."),
        ("Phase IV trials occur:", ["Before Phase I", "In a lab only", "*After the drug is on the market (post-market surveillance)", "Never"],
         "Phase IV monitors long-term effects in the general population."),
        ("A control group in a clinical trial:", ["*Provides the baseline for comparison", "Always receives the drug", "Is unnecessary", "Is the same as the treatment group"],
         "Controls show what happens without (or with standard) treatment."),
        ("COVID-19 vaccine trials enrolled 30,000+ participants to:", ["Make the trial longer", "*Ensure sufficient statistical power to detect efficacy and rare side effects", "Increase costs", "Complicate analysis"],
         "Large samples provide power to detect effects and identify uncommon adverse events."),
        ("Efficacy is measured by comparing:", ["*Outcomes in treatment vs. control groups", "Only treatment group outcomes", "Only side effects", "Lab results"],
         "Comparing groups shows whether the treatment improves outcomes."),
        ("Adverse event reporting in trials:", ["Is optional", "*Is mandatory to ensure safety", "Only applies to Phase I", "Is done only if effects are severe"],
         "All adverse events must be recorded and reported."),
        ("A per-protocol analysis includes only:", ["All randomized patients", "*Patients who completed the study per the protocol", "Only the control group", "Patients who dropped out"],
         "Per-protocol analysis can complement ITT but may introduce bias."),
        ("Randomization in trials ensures:", ["All patients recover", "The drug works", "*Groups are comparable, reducing confounding", "No side effects"],
         "Random assignment balances known and unknown confounders."),
        ("Informed consent in clinical trials requires:", ["No explanation", "*Full disclosure of risks, benefits, procedures, and the right to withdraw", "Only a signature", "Payment"],
         "Ethical trials require voluntary, fully informed participation."),
        ("A non-inferiority trial tests whether:", ["The new drug is superior", "*The new drug is at least as effective as the standard", "The standard drug fails", "No treatment works"],
         "Non-inferiority trials demonstrate that a new treatment is not worse than existing therapy."),
        ("Number Needed to Treat (NNT) is:", ["The total number of patients", "*The number of patients you need to treat for one to benefit compared to the control", "The number of trials needed", "Always 1"],
         "NNT = 1/absolute risk reduction; lower NNT means more effective treatment."),
        ("Meta-analyses of multiple trials:", ["Replace individual trials", "*Combine results to increase statistical power and provide more reliable estimates", "Are always biased", "Use no statistics"],
         "Meta-analyses pool data from multiple studies for stronger conclusions."),
        ("The hierarchy of evidence places RCTs:", ["At the bottom", "In the middle", "*Near the top (below systematic reviews/meta-analyses)", "Irrelevant"],
         "RCTs are the gold standard; only systematic reviews of RCTs rank higher."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 7)")
