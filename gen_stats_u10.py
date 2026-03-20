#!/usr/bin/env python3
"""Generate real content for Statistics Unit 10: AP Prep & Applications (6 lessons)."""
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

# ── 10.1 Review of Key Formulas ──
k, v = build_lesson(10, 1, "Review of Key Formulas",
    "<h3>Review of Key Formulas</h3>"
    "<p>A comprehensive review of the essential formulas used throughout AP Statistics.</p>"
    "<h4>Descriptive Statistics</h4>"
    "<ul><li>Mean: x̄ = Σxᵢ/n</li>"
    "<li>Standard deviation: s = √[Σ(xᵢ − x̄)²/(n−1)]</li>"
    "<li>z-score: z = (x − μ)/σ</li>"
    "<li>IQR = Q₃ − Q₁; Outlier fences: Q₁ − 1.5·IQR, Q₃ + 1.5·IQR</li></ul>"
    "<h4>Probability</h4>"
    "<ul><li>P(A or B) = P(A) + P(B) − P(A and B)</li>"
    "<li>P(A|B) = P(A and B)/P(B)</li>"
    "<li>Binomial: P(X=k) = C(n,k)p<sup>k</sup>(1−p)<sup>n−k</sup>, μ = np, σ = √(np(1−p))</li></ul>"
    "<h4>Inference</h4>"
    "<ul><li>Confidence interval: statistic ± (critical value)(SE)</li>"
    "<li>SE of mean: s/√n; SE of proportion: √(p̂(1−p̂)/n)</li>"
    "<li>t-statistic: t = (x̄ − μ₀)/(s/√n)</li>"
    "<li>z-statistic for proportion: z = (p̂ − p₀)/√(p₀(1−p₀)/n)</li>"
    "<li>Chi-square: χ² = Σ(O−E)²/E</li>"
    "<li>Regression slope: b = r(sᵧ/sₓ); r² = proportion of variation explained</li></ul>",
    [
        ("z-score Formula", "z = (x − μ)/σ; measures how many standard deviations a value is from the mean."),
        ("Standard Error of the Mean", "SE = s/√n; estimates the standard deviation of the sampling distribution of x̄."),
        ("Confidence Interval Formula", "statistic ± (critical value)(standard error); captures the parameter with stated confidence."),
        ("Binomial Probability Formula", "P(X=k) = C(n,k)p^k(1−p)^(n−k); probability of exactly k successes in n trials."),
        ("Chi-Square Statistic", "χ² = Σ(O−E)²/E; measures discrepancy between observed and expected frequencies."),
    ],
    [
        ("The formula for population z-score is:", ["z = (x − s)/n", "*z = (x − μ)/σ", "z = μ/σ", "z = σ/x"],
         "z-score standardizes a value relative to the mean and standard deviation."),
        ("Sample standard deviation uses n − 1 because:", ["It's simpler", "*It corrects bias in estimating the population standard deviation (Bessel's correction)", "n − 1 is always larger", "It's a convention with no reason"],
         "Bessel's correction gives an unbiased estimator of population variance."),
        ("The addition rule P(A or B) = P(A) + P(B) − P(A and B) prevents:", ["Underestimating", "*Double-counting the overlap", "Ignoring P(B)", "Negative probabilities"],
         "Subtracting the intersection corrects for events counted twice."),
        ("The SE of a sample mean is:", ["s × n", "s × √n", "*s/√n", "σ/n"],
         "SE = s/√n estimates how much x̄ varies from sample to sample."),
        ("The SE of a sample proportion p̂ is:", ["p̂/n", "p̂ × n", "*√(p̂(1−p̂)/n)", "p̂/√n"],
         "The standard error of a proportion involves p̂(1−p̂) divided by n."),
        ("A confidence interval has the form:", ["Statistic × SE", "*Statistic ± (critical value)(SE)", "SE ± critical value", "Parameter ± statistic"],
         "CI = point estimate ± margin of error."),
        ("The t-statistic for a one-sample mean test is:", ["*t = (x̄ − μ₀)/(s/√n)", "t = μ₀/s", "t = n/s", "t = x̄ × s"],
         "t measures how far x̄ is from μ₀ in standard-error units."),
        ("For binomial, μ = np gives:", ["The variance", "The standard deviation", "*The expected number of successes", "The probability"],
         "The mean of a binomial is the number of trials times the probability of success."),
        ("For binomial, σ = √(np(1−p)) gives:", ["The mean", "*The standard deviation", "The variance", "The range"],
         "σ measures the typical spread of the number of successes."),
        ("The regression slope b = r(sᵧ/sₓ) depends on:", ["Only r", "Only the standard deviations", "*Both the correlation r and the ratio of standard deviations", "Only the means"],
         "b combines the strength of association (r) with the relative scales (sᵧ/sₓ)."),
        ("r² represents:", ["The correlation", "*The proportion of variation in y explained by the linear relationship with x", "The slope squared", "The residual sum"],
         "r² = coefficient of determination."),
        ("The chi-square statistic sums:", ["Observed frequencies", "Expected frequencies", "*Squared differences between observed and expected, divided by expected", "Raw data"],
         "χ² = Σ(O−E)²/E."),
        ("P(A|B) = P(A and B)/P(B) is the formula for:", ["Independence", "The addition rule", "*Conditional probability", "Bayes' theorem"],
         "Conditional probability gives the probability of A given that B has occurred."),
        ("The IQR is calculated as:", ["Q₂ − Q₁", "*Q₃ − Q₁", "Max − Min", "Mean − Median"],
         "IQR spans the middle 50% of the data."),
        ("A value is a suspected outlier if it falls:", ["Within the IQR", "On the median", "*Below Q₁ − 1.5·IQR or above Q₃ + 1.5·IQR", "Within 1 SD of the mean"],
         "The 1.5·IQR rule identifies potential outliers."),
        ("The z-statistic for testing a proportion is:", ["z = (p̂ − p₀)/p₀", "*z = (p̂ − p₀)/√(p₀(1−p₀)/n)", "z = p₀/√n", "z = p̂/p₀"],
         "The z-test for proportions uses p₀ in the standard error (under H₀)."),
        ("Degrees of freedom for a one-sample t-test:", ["n", "*n − 1", "n + 1", "2n"],
         "df = n − 1 for a single sample."),
        ("The critical value z* = 1.96 corresponds to:", ["90% confidence", "*95% confidence", "99% confidence", "80% confidence"],
         "For a 95% CI, the two-tailed z* is 1.96."),
        ("C(n,k) in the binomial formula counts:", ["Probabilities", "*The number of ways to choose k successes from n trials", "The mean", "The variance"],
         "C(n,k) = n!/(k!(n−k)!) is the combination formula."),
        ("Knowing these formulas matters because:", ["They are arbitrary", "Memorization is the goal", "*They are the tools used to analyze data, make inferences, and solve AP problems", "They only appear on tests"],
         "Formulas connect concepts to calculations in every part of statistics."),
    ]
)
lessons[k] = v

# ── 10.2 AP-Style Practice Problems ──
k, v = build_lesson(10, 2, "AP-Style Practice Problems",
    "<h3>AP-Style Practice Problems</h3>"
    "<p>Success on the AP Statistics exam requires applying concepts to multi-step problems under timed conditions.</p>"
    "<h4>Problem-Solving Strategy</h4>"
    "<ul><li><b>Read carefully</b> — identify whether the problem involves inference, probability, regression, or experimental design.</li>"
    "<li><b>State hypotheses clearly</b> — for inference questions, always write H₀ and Hₐ in context.</li>"
    "<li><b>Check conditions</b> — randomness, normality, independence. State them explicitly.</li>"
    "<li><b>Show your work</b> — name the procedure, show the formula, plug in values, compute.</li>"
    "<li><b>Conclude in context</b> — always relate your answer back to the real-world situation described.</li></ul>"
    "<h4>Common Free-Response Topics</h4>"
    "<ul><li>Designing an experiment or survey with proper randomization.</li>"
    "<li>Performing and interpreting a hypothesis test (one/two-sample, proportions, χ²).</li>"
    "<li>Constructing and interpreting confidence intervals.</li>"
    "<li>Analyzing residual plots and regression output.</li>"
    "<li>Probability calculations including conditional probability and expected value.</li></ul>",
    [
        ("AP Problem-Solving Framework", "Read → Plan (identify procedure) → Check conditions → Calculate → Conclude in context."),
        ("State Hypotheses", "Always write H₀ and Hₐ using proper notation and in the context of the problem."),
        ("Check Conditions", "Verify randomness, normality (or large sample), and independence before inference."),
        ("Conclude in Context", "State the decision (reject/fail to reject H₀) and interpret it in terms of the real-world scenario."),
        ("Free-Response Scoring", "Points awarded for correct identification of procedure, condition checking, computation, and contextual interpretation."),
    ],
    [
        ("The first step in an AP statistics problem is:", ["Calculate immediately", "*Read carefully and identify the type of problem", "Guess the answer", "Look at the formula sheet"],
         "Understanding the problem type guides the entire solution."),
        ("For inference problems, always begin by:", ["Running the test", "*Stating H₀ and Hₐ in context", "Computing the mean", "Drawing a histogram"],
         "Clear hypotheses set up the rest of the procedure."),
        ("Conditions for a one-sample t-test include:", ["Only normality", "*Random sample (or randomized experiment), independence, and approximately normal population (or n ≥ 30)", "Only n > 30", "Only independence"],
         "All three conditions must be verified."),
        ("'Conclude in context' means:", ["Just state the p-value", "*Relate the statistical conclusion to the real-world situation described", "Say 'reject' or 'fail to reject' only", "Restate the formula"],
         "AP scoring requires connecting statistics to the context."),
        ("If a free-response asks you to 'justify your answer':", ["*Provide statistical evidence, cite conditions, and explain your reasoning", "Just give a number", "Say 'because it's significant'", "Repeat the question"],
         "Justification requires evidence, conditions, and reasoning."),
        ("When performing a hypothesis test, the procedure should be:", ["*Named (e.g., 'one-sample t-test for a mean')", "Left unnamed", "Always chi-square", "Always z-test"],
         "Naming the procedure shows you know which test to use."),
        ("A common mistake on the AP exam is:", ["Checking conditions", "Naming the procedure", "*Forgetting to interpret results in context", "Using formulas"],
         "Many students lose points by not connecting conclusions to the scenario."),
        ("For a two-sample proportion z-test, the pooled proportion is used under:", ["Hₐ", "*H₀ (which assumes the proportions are equal)", "Neither hypothesis", "Both hypotheses"],
         "Under H₀: p₁ = p₂, we pool the samples to estimate the common proportion."),
        ("The 10% condition checks that:", ["n > 10", "*The sample is less than 10% of the population (for independence)", "p > 0.10", "α = 10%"],
         "When sampling without replacement, n < 0.10N ensures approximate independence."),
        ("On the AP exam, partial credit is awarded for:", ["Only correct final answers", "*Each step: hypotheses, conditions, calculations, and interpretation", "Only the p-value", "Only the test statistic"],
         "AP rubrics give points at each stage of the solution."),
        ("If you get an unexpected result, you should:", ["Erase everything", "Change your hypotheses", "*Present your work honestly and interpret what you found", "Leave it blank"],
         "Full credit is possible even with unusual results if the process is correct."),
        ("Which is the correct interpretation of a 95% CI (14.2, 18.6) for a mean?", ["The mean is definitely between 14.2 and 18.6", "*We are 95% confident that the true population mean is between 14.2 and 18.6", "95% of data is in this range", "The probability the mean is here is 95%"],
         "CIs express confidence in the method, not probability about a fixed parameter."),
        ("When asked to design an experiment, your answer should include:", ["*Random assignment, control group, treatments, and response variable", "Only sample size", "Only the hypothesis", "Only the conclusion"],
         "A complete design specifies randomization, treatments, control, and what's measured."),
        ("For chi-square problems, expected counts must be:", ["At least 1", "At least 3", "*At least 5", "At least 10"],
         "The chi-square approximation requires all expected counts ≥ 5."),
        ("When interpreting slope in context: b = 2.3 for SAT prep hours vs. score:", ["*'For each additional hour of SAT prep, the predicted score increases by 2.3 points on average'", "'The score is 2.3'", "'2.3 is the y-intercept'", "'r = 2.3'"],
         "Slope interpretation must reference both variables and say 'on average' or 'predicted.'"),
        ("The AP exam formula sheet provides:", ["All answers", "*Key formulas for reference, but you must know when and how to use them", "Nothing useful", "Only normal table values"],
         "The formula sheet helps with recall but not with choosing and applying the right procedure."),
        ("Time management on the AP exam:", ["Spend all time on multiple choice", "Spend all time on free response", "*Allocate time proportionally and move on if stuck", "Skip the hardest questions entirely"],
         "Balanced time management maximizes your total score."),
        ("A residual plot from a regression problem on the AP exam should be checked for:", ["Only normality", "*Patterns (curvature, fan shapes) that suggest the model doesn't fit", "Only r²", "Nothing"],
         "Residual analysis is frequently tested and expected."),
        ("The AP Statistics exam consists of:", ["Only multiple choice", "Only free response", "*Both multiple choice (40 questions) and free response (6 questions)", "Only projects"],
         "The exam has two sections of equal weight."),
        ("The investigative task (question 6) on the AP exam:", ["Is the easiest question", "Can be skipped", "*Is a multi-part problem requiring integrated statistical thinking", "Has only one step"],
         "The investigative task tests your ability to combine multiple concepts."),
    ]
)
lessons[k] = v

# ── 10.3 Interpreting Graphical Data in AP Exams ──
k, v = build_lesson(10, 3, "Interpreting Graphical Data in AP Exams",
    "<h3>Interpreting Graphical Data in AP Exams</h3>"
    "<p>The AP exam frequently presents data in graphical form. You must be able to read, interpret, and draw conclusions from graphs.</p>"
    "<ul><li><b>Histograms:</b> Identify shape (symmetric, skewed, bimodal), center, spread, and outliers. Don't confuse frequency with value.</li>"
    "<li><b>Boxplots:</b> Read the five-number summary (min, Q₁, median, Q₃, max). Compare distributions across groups. Identify outliers (dots beyond whiskers).</li>"
    "<li><b>Scatterplots:</b> Describe direction, form, strength, and unusual points. Use the regression line and r/r² if given.</li>"
    "<li><b>Residual plots:</b> Random scatter = good fit; patterns = model problems.</li>"
    "<li><b>Normal probability plots (Q-Q plots):</b> Points roughly on a straight line = approximately normal.</li>"
    "<li><b>Dotplots and stemplots:</b> Good for small datasets. Show individual values and distributional shape.</li>"
    "<li><b>Bar charts and pie charts:</b> For categorical data. Compare relative frequencies, not just heights.</li></ul>",
    [
        ("Histogram Interpretation", "Describe shape, center, spread, and outliers; shape can be symmetric, right-skewed, left-skewed, or bimodal."),
        ("Boxplot", "Displays the five-number summary; compare distributions and identify outliers."),
        ("Residual Plot Interpretation", "Random scatter around 0 = good model; patterns indicate model inadequacy."),
        ("Normal Probability Plot", "If points fall roughly on a straight line, the data are approximately normal."),
        ("Describing a Scatterplot", "Use direction (positive/negative), form (linear/curved), strength (strong/weak), and note unusual points."),
    ],
    [
        ("When describing a histogram, mention:", ["Only the shape", "Only the center", "*Shape, center, spread, and any outliers or unusual features", "Only the mode"],
         "A complete description covers all four characteristics."),
        ("A right-skewed histogram has:", ["*A long tail to the right", "A long tail to the left", "Symmetry", "No tail"],
         "Right-skewed = most data on the left with a tail extending to the right."),
        ("In a boxplot, the box spans:", ["Min to max", "*Q₁ to Q₃ (the IQR)", "Mean to median", "0 to 100"],
         "The box represents the middle 50% of the data."),
        ("Dots beyond the whiskers in a boxplot represent:", ["Normal data", "The mean", "*Potential outliers", "The mode"],
         "Individual dots beyond whiskers flag suspected outliers."),
        ("Comparing two boxplots involves looking at:", ["Only medians", "Only IQRs", "*Center, spread, shape, and outliers for both distributions", "Only the means"],
         "Compare all aspects when describing distributions side by side."),
        ("A scatterplot should be described using:", ["*Direction, form, strength, and unusual points", "Only r", "Only the slope", "Only whether it's positive"],
         "A thorough scatterplot description covers all four characteristics."),
        ("A residual plot with a clear U-shape indicates:", ["A perfect fit", "*The linear model misses a curved pattern in the data", "No relationship", "Random scatter"],
         "A curved residual pattern means a linear model is inappropriate."),
        ("In a normal probability plot, approximate normality is indicated by:", ["A curved pattern", "Random scatter", "*Points falling roughly along a straight line", "Points forming a circle"],
         "A straight line on a Q-Q plot supports the normality assumption."),
        ("A stemplot is best for:", ["Large datasets", "*Small to moderate datasets where individual values matter", "Categorical data", "Regression analysis"],
         "Stemplots show individual data values and distributional shape."),
        ("Bar chart heights represent:", ["Quantitative values", "*Frequency or relative frequency of categories", "Mean values", "Standard deviations"],
         "Bar charts display counts or proportions for categorical variables."),
        ("Comparing bar charts across groups, use:", ["Raw counts if groups differ in size", "*Relative frequencies (proportions) for fair comparison", "Only the tallest bar", "Only the mode"],
         "Different group sizes require proportions for valid comparison."),
        ("A bimodal histogram suggests:", ["Normality", "*Possibly two distinct subgroups in the data", "A symmetric distribution", "An error in data collection"],
         "Two peaks may indicate a mixture of two populations."),
        ("The median in a histogram is located where:", ["The tallest bar is", "*Approximately half the area is to the left and half to the right", "The first bar is", "The mean is"],
         "The median splits the distribution into two equal areas."),
        ("If a histogram is symmetric, the mean is approximately:", ["Greater than the median", "Less than the median", "*Equal to the median", "Zero"],
         "Symmetry implies mean ≈ median."),
        ("If a histogram is right-skewed, the mean is typically:", ["*Greater than the median (pulled right by the tail)", "Less than the median", "Equal to the median", "Zero"],
         "The long right tail pulls the mean above the median."),
        ("Parallel boxplots are useful for:", ["Showing individual data points", "*Comparing distributions across groups side by side", "Showing correlation", "Displaying scatter"],
         "Parallel boxplots allow quick visual comparison of center and spread."),
        ("On the AP exam, when given a graph, you should:", ["*Describe what you see in context, citing specific values when possible", "Ignore it", "Only compute statistics", "Redraw it"],
         "Graphical interpretation should be specific and contextual."),
        ("A fan-shaped residual plot suggests:", ["Perfect fit", "*Non-constant variance (heteroscedasticity)", "A linear relationship", "Normal residuals"],
         "Increasing spread means prediction accuracy varies with x."),
        ("Dotplots are especially useful for:", ["Categorical comparisons", "Regression", "*Small quantitative datasets where you can see every value", "Only proportions"],
         "Dotplots give a clear view of individual values and their distribution."),
        ("In a pie chart, each slice represents:", ["A mean", "*A category's proportion of the whole", "A standard deviation", "A quantitative variable"],
         "Pie charts show parts of a whole for categorical data."),
    ]
)
lessons[k] = v

# ── 10.4 Real-World Applications (medicine, economics, sports) ──
k, v = build_lesson(10, 4, "Real-World Applications (medicine, economics, sports)",
    "<h3>Real-World Applications</h3>"
    "<p>Statistics is applied across virtually every field. This lesson surveys major applications.</p>"
    "<h4>Medicine & Public Health</h4>"
    "<ul><li>Clinical trials test drug efficacy with hypothesis tests and confidence intervals.</li>"
    "<li>Epidemiology uses regression and relative risk to study disease patterns.</li>"
    "<li>Survival analysis tracks time-to-event data (e.g., cancer survival rates).</li></ul>"
    "<h4>Economics & Business</h4>"
    "<ul><li>Econometrics applies regression to model supply, demand, GDP, and inflation.</li>"
    "<li>A/B testing compares marketing strategies using proportion tests.</li>"
    "<li>Quality control uses control charts and process capability analysis.</li></ul>"
    "<h4>Sports</h4>"
    "<ul><li>Sabermetrics and advanced analytics evaluate player value (WAR, OPS, xG).</li>"
    "<li>Expected goals (xG) in soccer uses logistic regression to estimate scoring probability from shot data.</li>"
    "<li>Draft predictions use regression models based on combine and college performance metrics.</li></ul>",
    [
        ("Clinical Trial", "A controlled experiment testing a medical treatment — the gold standard for evidence-based medicine."),
        ("Epidemiology", "The study of disease distribution and determinants in populations, using statistics to identify risk factors."),
        ("A/B Testing", "Comparing two versions (A vs. B) to determine which performs better, using hypothesis testing."),
        ("Sabermetrics", "Statistical analysis in baseball (and sports generally) to evaluate performance and make decisions."),
        ("Control Chart", "A quality-control tool plotting measurements over time with control limits to detect process changes."),
    ],
    [
        ("In medicine, hypothesis tests are used to:", ["Guarantee drug safety", "*Determine if a treatment is more effective than placebo or current standard", "Replace clinical judgment", "Eliminate all risk"],
         "Hypothesis tests provide evidence about treatment effects."),
        ("Relative risk in epidemiology compares:", ["Means", "Standard deviations", "*The probability of disease in an exposed group vs. an unexposed group", "IQRs"],
         "RR = P(disease|exposed) / P(disease|unexposed)."),
        ("A/B testing in marketing compares:", ["Only colors", "*Two versions of a product, ad, or feature to see which performs better", "Identical versions", "Colors and fonts only"],
         "A/B testing uses statistical tests to determine the better-performing option."),
        ("WAR (Wins Above Replacement) in baseball:", ["Is a pitching stat only", "*Estimates a player's total contribution compared to a replacement-level player", "Measures speed only", "Is subjective"],
         "WAR is a comprehensive stat combining multiple performance dimensions."),
        ("Expected goals (xG) in soccer uses:", ["Only shot count", "Only assists", "*Logistic regression on shot location, angle, and other features to estimate scoring probability", "Random guessing"],
         "xG models the probability of scoring from each shot."),
        ("Control charts in quality control:", ["Guarantee zero defects", "*Monitor a process over time to detect shifts or unusual variation", "Replace inspection", "Increase production speed"],
         "Control charts flag when a process may be out of control."),
        ("Survival analysis in medicine examines:", ["Only fatal diseases", "*Time until an event (death, relapse, recovery) and factors that affect it", "Drug prices", "Insurance costs"],
         "Survival analysis models time-to-event data."),
        ("Econometrics is:", ["*The application of statistical methods to economic data and theory", "Pure economic theory", "Only about GDP", "A branch of mathematics only"],
         "Econometrics bridges statistics and economics."),
        ("A p-value < 0.05 in a drug trial means:", ["The drug definitely works", "The drug is safe", "*There is statistically significant evidence that the drug's effect is not due to chance alone", "The trial failed"],
         "Significance means the observed effect is unlikely under the null hypothesis."),
        ("Sports analytics have changed how teams:", ["Play less", "*Draft, trade, and develop players using data-driven decisions", "Ignore statistics", "Use only traditional scouting"],
         "Analytics complement traditional methods with statistical evidence."),
        ("Process capability analysis measures:", ["The mean only", "*Whether a manufacturing process produces output within specified tolerances", "Only variance", "Worker productivity"],
         "Process capability compares process variation to specification limits."),
        ("Regression is used in economics to model:", ["Nothing", "Only stock prices", "*Supply/demand curves, wage determinants, GDP growth, and more", "Only unemployment"],
         "Regression is the primary tool in empirical economics."),
        ("In a clinical trial, double-blinding:", ["*Prevents both patient and researcher bias from influencing results", "Is optional", "Means two trials are combined", "Is unethical"],
         "Double-blinding is an important design feature for objectivity."),
        ("Confidence intervals in medical studies help:", ["*Quantify the precision of estimated treatment effects", "Prove causation", "Eliminate uncertainty", "Replace p-values"],
         "CIs show the range of plausible values for the true effect."),
        ("In business, A/B testing typically uses:", ["*Two-proportion z-tests or chi-square tests to compare conversion rates", "No statistics", "Only visual inspection", "ANOVA always"],
         "A/B tests compare proportions (e.g., click-through rates) between groups."),
        ("The placebo group in a clinical trial serves as:", ["The treatment group", "*The baseline comparison to measure the treatment's effect", "An unethical requirement", "A group that always improves"],
         "Comparing treatment to placebo isolates the drug's true effect."),
        ("Draft models in sports predict:", ["Nothing", "*Future performance based on measurable attributes like speed, strength, and college stats", "Only physical traits", "Only personality"],
         "Statistical models estimate how prospects will perform professionally."),
        ("Statistics helps identify disease outbreaks through:", ["Guessing", "*Monitoring unusual clusters of cases using statistical surveillance methods", "Only news reports", "Only hospital counts"],
         "Statistical methods detect anomalies in case counts."),
        ("The integration of statistics into every field shows that:", ["Statistics is only academic", "*Statistical literacy is essential for professionals across all disciplines", "Only statisticians use statistics", "Statistics is obsolete"],
         "Data-driven decision-making permeates modern professional life."),
        ("The most important skill for AP Statistics is:", ["Memorizing formulas", "Speed", "*Understanding when and why to use each method and interpreting results in context", "Calculator proficiency"],
         "Conceptual understanding and contextual interpretation are valued most."),
    ]
)
lessons[k] = v

# ── 10.5 Capstone Project: Statistical Analysis of a Dataset ──
k, v = build_lesson(10, 5, "Capstone Project: Statistical Analysis of a Dataset",
    "<h3>Capstone Project: Statistical Analysis of a Dataset</h3>"
    "<p>A capstone project integrates all statistical skills by analyzing a real dataset from start to finish.</p>"
    "<h4>Project Steps</h4>"
    "<ol><li><b>Choose a question:</b> What are you investigating? State a clear research question.</li>"
    "<li><b>Collect or obtain data:</b> Use a reputable source (government databases, academic datasets, surveys with proper sampling).</li>"
    "<li><b>Explore the data:</b> Compute descriptive statistics (mean, SD, median, IQR). Create graphs (histograms, boxplots, scatterplots).</li>"
    "<li><b>State hypotheses:</b> Based on your question, formulate H₀ and Hₐ.</li>"
    "<li><b>Check conditions:</b> Verify independence, normality, and sample size requirements.</li>"
    "<li><b>Perform analysis:</b> Run the appropriate test (t-test, χ², regression, ANOVA) or construct confidence intervals.</li>"
    "<li><b>Interpret results:</b> State conclusions in context. Discuss limitations and potential confounding variables.</li>"
    "<li><b>Present findings:</b> Create a clear report or presentation summarizing your work.</li></ol>",
    [
        ("Research Question", "A specific, focused question that guides the entire statistical investigation."),
        ("Exploratory Data Analysis (EDA)", "The initial phase of summarizing data with statistics and visualizations before formal testing."),
        ("Confounding Variable", "An outside variable that affects both the explanatory and response variables, potentially distorting the relationship."),
        ("Statistical Report", "A structured document presenting the research question, data, methods, results, and interpretation."),
        ("Limitations", "Acknowledging weaknesses in the study design, data quality, or scope that affect the conclusions."),
    ],
    [
        ("The first step in a statistical capstone project is:", ["Run a test", "Collect data", "*Define a clear research question", "Write the conclusion"],
         "A focused question directs every subsequent step."),
        ("Good data sources for a project include:", ["Wikipedia edits", "Personal opinions", "*Government databases, academic datasets, and properly conducted surveys", "Social media posts"],
         "Reputable, systematic data sources produce reliable analyses."),
        ("Exploratory data analysis (EDA) involves:", ["*Computing summary statistics and creating visualizations to understand the data", "Only running hypothesis tests", "Skipping to conclusions", "Only collecting more data"],
         "EDA helps you understand patterns, outliers, and distributions before formal analysis."),
        ("Before performing a hypothesis test, you must:", ["Skip assumptions", "Always use z-tests", "*Check that the conditions for the test are met", "Assume normality without checking"],
         "Condition-checking validates that the test's conclusions are reliable."),
        ("A confounding variable:", ["*Affects both the explanatory and response variables, distorting the relationship", "Is the same as the response variable", "Is never present", "Improves the analysis"],
         "Confounders create spurious associations or hide true effects."),
        ("Describing the shape of data in a capstone typically uses:", ["*Histograms, boxplots, and descriptive language (symmetric, skewed, etc.)", "Only numbers", "Only t-tests", "Only the mean"],
         "Visual and verbal descriptions of shape are part of EDA."),
        ("Choosing the right statistical test depends on:", ["Random choice", "*The type of data (categorical vs. quantitative), number of groups, and research question", "Only sample size", "Only the hypothesis"],
         "Test selection follows from the data type and question."),
        ("A confidence interval in a capstone project provides:", ["The exact parameter value", "*A range of plausible values for the population parameter with stated confidence", "Proof of causation", "Zero uncertainty"],
         "CIs quantify the precision of your estimate."),
        ("Discussing limitations is important because:", ["It weakens your project", "It's unnecessary", "*It shows critical thinking about potential biases and generalizability", "It reduces your grade"],
         "Honest discussion of limitations strengthens a project's credibility."),
        ("A well-structured statistical report includes:", ["Only the conclusion", "*Introduction, methods, results, and discussion sections", "Only graphs", "Only p-values"],
         "A complete report covers every stage of the analysis."),
        ("Proper sampling in a capstone project ensures:", ["*Results can generalize to the population of interest", "The sample is biased", "Only certain people are included", "The sample is small"],
         "Representative sampling is key to valid inference."),
        ("When presenting findings, visualizations should:", ["Be as complex as possible", "*Clearly communicate key patterns and support your conclusions", "Use as many colors as possible", "Be optional"],
         "Effective graphs highlight important patterns without clutter."),
        ("If your hypothesis test fails to reject H₀:", ["The project failed", "H₀ is proven true", "*It means there wasn't sufficient evidence to support Hₐ — still a valid result", "You should change your data"],
         "Failing to reject is a legitimate statistical outcome."),
        ("Ethical data collection in a capstone means:", ["Collecting data from anyone without consent", "*Obtaining informed consent, protecting privacy, and reporting results honestly", "Manipulating data for significance", "Using only online sources"],
         "Ethics in research are mandatory, even for class projects."),
        ("A scatter plot in a capstone project might show:", ["Only the mean", "*The relationship between two quantitative variables", "Only one variable", "Categorical proportions"],
         "Scatterplots display bivariate quantitative relationships."),
        ("Including a regression equation in a capstone report:", ["Is never useful", "*Allows prediction and quantifies the relationship between variables", "Replaces all other analysis", "Is required even for categorical data"],
         "Regression quantifies and predicts based on the data relationship."),
        ("The discussion section of a report should:", ["*Interpret results in context, compare to expectations, and note limitations", "Only restate numbers", "Avoid interpretation", "Only list p-values"],
         "Discussion connects statistics to meaning."),
        ("Reproducibility in a capstone means:", ["Hiding your methods", "*Documenting your methods so someone else could repeat the analysis", "Using proprietary data", "Never sharing your data"],
         "Transparency is a core scientific principle."),
        ("A strong capstone project demonstrates:", ["Memorization only", "Only one statistical technique", "*Integration of descriptive statistics, inference, graphical analysis, and contextual interpretation", "Speed"],
         "Capstones showcase comprehensive statistical thinking."),
        ("After completing the project, reflection on what you learned:", ["Is a waste of time", "*Helps solidify your understanding and identifies areas for growth", "Is only for the teacher", "Doesn't matter"],
         "Reflection deepens learning and improves future analyses."),
    ]
)
lessons[k] = v

# ── 10.6 Comprehensive Review & AP Exam Practice ──
k, v = build_lesson(10, 6, "Comprehensive Review & AP Exam Practice",
    "<h3>Comprehensive Review & AP Exam Practice</h3>"
    "<p>This lesson brings everything together in preparation for the AP Statistics exam.</p>"
    "<h4>Key Topics to Master</h4>"
    "<ol><li><b>Exploring Data:</b> Distributions, summary statistics, graphical displays, comparisons.</li>"
    "<li><b>Sampling & Experiments:</b> Sampling methods, bias, experiments vs. observational studies, randomization.</li>"
    "<li><b>Probability:</b> Rules, random variables, binomial, geometric, normal distributions.</li>"
    "<li><b>Statistical Inference:</b> Confidence intervals and hypothesis tests for means, proportions, and slopes. Chi-square tests.</li></ol>"
    "<h4>Exam Tips</h4>"
    "<ul><li>Always check conditions and state them.</li>"
    "<li>Write in complete sentences for free response — communication matters.</li>"
    "<li>Use context: refer to the specific variables and scenario in the problem.</li>"
    "<li>Manage your time: about 2.5 minutes per MC question, 12 minutes per short FR, 25 minutes for the investigative task.</li>"
    "<li>Don't leave free response blank — partial credit is awarded.</li></ul>",
    [
        ("Four Major AP Topics", "Exploring Data, Sampling & Experiments, Probability, Statistical Inference."),
        ("Communication on AP Exam", "Free-response answers should be in complete sentences, in context, with clear statistical reasoning."),
        ("Time Management", "~2.5 min/MC, ~12 min/short FR (Q1–Q5), ~25 min for Q6 (investigative task)."),
        ("Partial Credit", "Free-response questions award points for each correct component — never leave a question blank."),
        ("Conditions for Inference", "Random, Normal (or large n), Independent — must be stated and verified on every inference question."),
    ],
    [
        ("The four main topics on the AP Statistics exam are:", ["*Exploring Data, Sampling & Experiments, Probability, Statistical Inference", "Algebra, Geometry, Trigonometry, Calculus", "Mean, Median, Mode, Range", "Only Inference and Probability"],
         "The AP framework covers these four broad content areas."),
        ("To earn full credit on a free-response question:", ["*State hypotheses, check conditions, show calculations, and conclude in context", "Just write the answer", "Only compute the test statistic", "Only state the conclusion"],
         "Each component earns points on the rubric."),
        ("The difference between an experiment and an observational study is:", ["No difference", "*Experiments impose treatments; observational studies only observe without intervention", "Observational studies are better", "Experiments are always unethical"],
         "Random assignment of treatments is what makes a study an experiment."),
        ("Why is randomization important?", ["It's not important", "It increases bias", "*It reduces bias and allows causal conclusions (in experiments) or representative sampling", "It makes calculations easier"],
         "Randomization is the foundation of valid inference."),
        ("The normal condition for proportions is:", ["np ≥ 5", "*np ≥ 10 AND n(1−p) ≥ 10", "n ≥ 30", "p ≥ 0.5"],
         "Both np and n(1−p) ≥ 10 ensures the normal approximation is adequate."),
        ("On the AP exam, 'interpret the confidence level' means:", ["The parameter is in the interval", "*If we repeated this process many times, about C% of the intervals would capture the true parameter", "C% of the data is in the interval", "We're C% sure the sample statistic is right"],
         "Confidence level refers to the long-run capture rate of the procedure."),
        ("A Type I error occurs when:", ["We fail to reject a false H₀", "*We reject H₀ when it is actually true (false positive)", "The p-value is correct", "The CI is too wide"],
         "Type I error = incorrectly rejecting a true null hypothesis."),
        ("A Type II error occurs when:", ["*We fail to reject H₀ when it is actually false (false negative)", "We reject a true H₀", "α is too high", "The sample is too large"],
         "Type II error = missing a real effect."),
        ("Increasing sample size:", ["Increases Type I error", "*Decreases the margin of error and increases power", "Has no effect", "Increases bias"],
         "Larger samples give more precise estimates and better power."),
        ("On a free-response question about regression, you should:", ["*Interpret slope and r² in context, check residual plot, and discuss conditions", "Only state the equation", "Only give r", "Skip the residual plot"],
         "Complete regression answers include interpretation, conditions, and residual analysis."),
        ("The purpose of a random sample is:", ["To ensure large n", "*To reduce bias and allow generalization to the population", "To guarantee perfect results", "To avoid statistics"],
         "Random sampling is the basis for extending conclusions from sample to population."),
        ("Stratified sampling:", ["Is always biased", "*Divides the population into strata and samples from each, improving representation", "Is the same as convenience sampling", "Uses only one group"],
         "Stratification ensures all important subgroups are represented."),
        ("The investigative task (Q6) on the AP exam typically:", ["Is only one part", "*Has multiple parts requiring you to integrate concepts and think critically", "Is optional", "Has no partial credit"],
         "Q6 tests deeper understanding across multiple topics."),
        ("When there is a contradiction between the p-value and your expectation:", ["*Report your findings honestly and discuss possible explanations", "Change the data", "Ignore the p-value", "Redo the test until it works"],
         "Statistical integrity requires honest reporting regardless of expectations."),
        ("On multiple choice questions, eliminating wrong answers:", ["Is a waste of time", "*Can improve your score even when you're not sure of the right answer", "Is cheating", "Reduces your score"],
         "Process of elimination is a valuable strategy."),
        ("For a two-sample t-test, degrees of freedom:", ["Always equal n₁ + n₂", "*Are calculated using a formula (or use the smaller of n₁−1 and n₂−1 as a conservative estimate)", "Are always 30", "Don't matter"],
         "df for two-sample t-tests use the Welch approximation or a conservative estimate."),
        ("Writing 'We reject H₀' is incomplete unless you:", ["Also write the p-value", "State the test statistic", "*Also state what rejecting H₀ means in the context of the problem", "Draw a graph"],
         "AP graders require contextual interpretation."),
        ("The formula sheet is most useful when you:", ["Memorize it entirely", "Ignore it", "*Know the concepts and use it as a reference for specific formulas during the exam", "Copy it verbatim"],
         "Understanding when to use each formula is more important than pure memorization."),
        ("A complete AP Statistics preparation includes:", ["Only practice tests", "Only formula review", "*Conceptual understanding, formula fluency, practice problems, and time management skills", "Only reading the textbook"],
         "Well-rounded preparation covers all aspects."),
        ("The most important takeaway from AP Statistics:", ["*Statistical reasoning and data literacy are essential life skills for making informed decisions", "Only formulas matter", "Statistics is only for math class", "Always trust the data without question"],
         "AP Statistics teaches critical thinking about data that applies to every field and everyday life."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 10)")
