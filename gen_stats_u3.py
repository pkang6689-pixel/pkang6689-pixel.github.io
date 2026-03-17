#!/usr/bin/env python3
"""Generate real content for Statistics Unit 3: Descriptive Statistics (7 lessons)."""
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

# ── 3.1 Measures of Central Tendency ──
k, v = build_lesson(3, 1, "Measures of Central Tendency (mean, median, mode)",
    "<h3>Measures of Central Tendency</h3>"
    "<p>Central tendency measures identify a single value that best represents the 'center' of a dataset.</p>"
    "<ul><li><b>Mean (x̄):</b> The arithmetic average — sum of all values divided by the number of values. Sensitive to outliers.</li>"
    "<li><b>Median:</b> The middle value when data are ordered. If n is even, it is the average of the two middle values. Resistant to outliers.</li>"
    "<li><b>Mode:</b> The most frequently occurring value. A dataset can be unimodal (one mode), bimodal (two modes), multimodal, or have no mode.</li></ul>"
    "<p><b>Choosing the right measure:</b></p>"
    "<ul><li>Use the <b>mean</b> for roughly symmetric distributions without extreme outliers.</li>"
    "<li>Use the <b>median</b> for skewed distributions or when outliers are present (e.g., income data).</li>"
    "<li>Use the <b>mode</b> for categorical data or to identify the most common category.</li></ul>"
    "<p>In a <b>right-skewed</b> distribution: mean > median. In a <b>left-skewed</b> distribution: mean < median. In a <b>symmetric</b> distribution: mean ≈ median.</p>",
    [
        ("Mean", "The arithmetic average of a dataset, calculated as the sum of all values divided by the number of values (x̄ = Σx / n)."),
        ("Median", "The middle value of an ordered dataset; if n is even, it is the average of the two middle values."),
        ("Mode", "The value that occurs most frequently in a dataset; a dataset may have no mode, one mode, or multiple modes."),
        ("Resistant Measure", "A statistic not greatly affected by extreme values (outliers); the median is resistant, the mean is not."),
        ("Skewness and Central Tendency", "In right-skewed distributions, mean > median; in left-skewed, mean < median; in symmetric, mean ≈ median."),
    ],
    [
        ("The mean of {4, 8, 10, 12, 16} is:", ["8", "10", "12", "*10"],
         "Mean = (4+8+10+12+16)/5 = 50/5 = 10."),
        ("The median of {3, 7, 9, 15, 20} is:", ["7", "*9", "15", "10.8"],
         "With 5 values, the median is the 3rd value: 9."),
        ("The median of {2, 5, 8, 11} is:", ["5", "8", "*6.5", "7"],
         "With even n, median = (5+8)/2 = 6.5."),
        ("The mode of {3, 5, 5, 7, 9, 9, 9} is:", ["3", "5", "*9", "7"],
         "9 appears 3 times, more than any other value."),
        ("Which measure is most affected by outliers?", ["Median", "Mode", "*Mean", "Range"],
         "The mean is pulled toward extreme values because it uses every data point."),
        ("For right-skewed data, the best measure of center is usually:", ["Mean", "*Median", "Mode", "Range"],
         "The median is resistant to the pull of the long right tail."),
        ("In a symmetric distribution:", ["Mean > median", "Mean < median", "*Mean ≈ median", "Median = mode only"],
         "In symmetric data, the mean and median are approximately equal."),
        ("A dataset of incomes (with a few billionaires) is best summarized by:", ["Mean", "*Median", "Mode", "Maximum"],
         "Income data is typically right-skewed; the median better represents the typical income."),
        ("The mode is useful for:", ["Only quantitative data", "Only continuous data", "*Categorical data (finding the most common category)", "Calculating the mean"],
         "The mode identifies the most frequent category, making it ideal for categorical data."),
        ("A dataset with two modes is called:", ["Unimodal", "*Bimodal", "No modal", "Trimodal"],
         "Two modes = bimodal."),
        ("For the data {1, 1, 2, 3, 100}, the mean is __ and the median is __:", ["1 and 2", "*21.4 and 2", "2 and 21.4", "100 and 3"],
         "Mean = (1+1+2+3+100)/5 = 21.4; Median = 2 (3rd value). The outlier (100) inflates the mean."),
        ("A 'resistant' measure means:", ["It never changes", "*It is not greatly affected by extreme values", "It equals the mode", "It requires a large sample"],
         "Resistant measures (like the median) are stable even when outliers are present."),
        ("If all values in a dataset are the same (e.g., {5, 5, 5, 5}), the mean, median, and mode are:", ["All different", "*All equal to 5", "Undefined", "Zero"],
         "When all values are the same, mean = median = mode = that value."),
        ("In left-skewed data:", ["*Mean < median", "Mean > median", "Mean = median", "Mode > mean"],
         "The left tail pulls the mean to the left, making it smaller than the median."),
        ("The weighted mean is used when:", ["All values are equal", "No weights matter", "*Different values have different levels of importance (weights)", "Only for ordinal data"],
         "A weighted mean assigns different weights to reflect varying importance."),
        ("If a student scores 80, 90, 70, and 100 on four tests, the mean is:", ["80", "90", "70", "*85"],
         "Mean = (80+90+70+100)/4 = 340/4 = 85."),
        ("The mean of a frequency distribution is found by:", ["Adding all classes", "Counting frequencies", "*Σ(f·x)/n where f is frequency and x is the class midpoint", "Taking the middle class"],
         "For grouped data, multiply each midpoint by its frequency, sum, and divide by n."),
        ("A dataset has no mode when:", ["It has one peak", "It is bimodal", "*No value repeats more than once", "It has outliers"],
         "If every value occurs exactly once, there is no mode."),
        ("Which measure of center can be used for both qualitative and quantitative data?", ["Mean", "Median", "*Mode", "Standard deviation"],
         "The mode applies to any type of data — it identifies the most frequent category or value."),
        ("Adding a large outlier to a dataset will:", ["*Increase the mean significantly while barely changing the median", "Decrease both the mean and median", "Not affect any measure", "Change the mode"],
         "The mean shifts toward the outlier; the median remains relatively stable."),
    ]
)
lessons[k] = v

# ── 3.2 Measures of Spread ──
k, v = build_lesson(3, 2, "Measures of Spread (range, variance, standard deviation)",
    "<h3>Measures of Spread</h3>"
    "<p>Spread (variability) measures describe how spread out or dispersed data values are around the center.</p>"
    "<ul><li><b>Range:</b> Maximum − Minimum. Simple but sensitive to outliers.</li>"
    "<li><b>Variance (s²):</b> The average of the squared deviations from the mean. Uses n−1 in the denominator for sample variance (Bessel's correction).</li>"
    "<li><b>Standard Deviation (s):</b> The square root of the variance. It is in the same units as the data and measures typical distance from the mean.</li>"
    "<li><b>IQR (Interquartile Range):</b> Q3 − Q1. Resistant to outliers; measures spread of the middle 50%.</li></ul>"
    "<p>A <b>low standard deviation</b> means data are clustered near the mean; a <b>high standard deviation</b> means data are widely spread.</p>"
    "<p>The <b>Empirical Rule</b> (68-95-99.7 rule) for approximately normal distributions: about 68% of data fall within 1 SD of the mean, 95% within 2 SD, and 99.7% within 3 SD.</p>",
    [
        ("Range", "The difference between the maximum and minimum values in a dataset: Range = Max − Min."),
        ("Variance (s²)", "The average of squared deviations from the mean; for a sample, divide by n − 1."),
        ("Standard Deviation (s)", "The square root of the variance; measures the typical distance of data points from the mean, in the same units as the data."),
        ("Empirical Rule", "For approximately normal distributions: ~68% of data within 1 SD, ~95% within 2 SD, ~99.7% within 3 SD of the mean."),
        ("Bessel's Correction", "Using n − 1 instead of n in the denominator of sample variance to produce an unbiased estimate of the population variance."),
    ],
    [
        ("The range of {5, 12, 8, 3, 20} is:", ["5", "8", "12", "*17"],
         "Range = 20 − 3 = 17."),
        ("Standard deviation measures:", ["The middle value", "The most common value", "*The typical distance of data points from the mean", "The total of all values"],
         "Standard deviation quantifies how spread out data are around the mean."),
        ("Variance is the:", ["Square root of the standard deviation", "Mean divided by n", "*Average of squared deviations from the mean", "Range divided by 2"],
         "Variance = Σ(x − x̄)² / (n − 1) for a sample."),
        ("Why do we use n−1 in sample variance?", ["To make the calculation simpler", "*To produce an unbiased estimate of the population variance (Bessel's correction)", "It doesn't matter", "Because n is always wrong"],
         "Dividing by n−1 corrects for the bias that arises from estimating the mean from the sample itself."),
        ("A low standard deviation means:", ["Data are widely spread", "*Data are clustered close to the mean", "The mean is low", "There are many outliers"],
         "A small SD indicates that most data points are near the mean."),
        ("According to the Empirical Rule, about 95% of data fall within:", ["1 SD of the mean", "*2 SD of the mean", "3 SD of the mean", "The IQR"],
         "The Empirical Rule states approximately 95% of data lie within 2 standard deviations of the mean."),
        ("The Empirical Rule applies to:", ["All distributions", "Only skewed distributions", "*Approximately normal (bell-shaped) distributions", "Only uniform distributions"],
         "The 68-95-99.7 rule is specifically for approximately normal distributions."),
        ("The IQR is resistant to outliers because:", ["It uses the range", "*It only considers the middle 50% of data (Q1 to Q3)", "It uses the mean", "It ignores all data"],
         "The IQR measures spread between the 25th and 75th percentiles, unaffected by extreme values."),
        ("If the mean is 50 and the SD is 5, approximately 68% of data lie between:", ["40 and 60", "45 and 50", "*45 and 55", "50 and 55"],
         "68% within 1 SD: 50 − 5 = 45 to 50 + 5 = 55."),
        ("The range is sensitive to outliers because:", ["*It depends only on the maximum and minimum values", "It uses all values", "It ignores extremes", "It uses the median"],
         "One extreme value can dramatically change the range."),
        ("For the data {10, 10, 10, 10, 10}, the standard deviation is:", ["10", "5", "1", "*0"],
         "When all values are the same, there is no spread — SD = 0."),
        ("Which has a larger standard deviation: {1, 2, 3, 4, 5} or {1, 1, 3, 5, 5}?", ["The first set", "*The second set", "They're equal", "Cannot determine"],
         "The second set has values further from the mean (3), producing a larger SD."),
        ("Population standard deviation uses __ in the denominator:", ["n − 1", "n + 1", "*N (the population size)", "n − 2"],
         "Population SD divides by N; sample SD divides by n − 1."),
        ("If you add a constant to every value in a dataset, the standard deviation:", ["Increases", "Decreases", "*Stays the same", "Doubles"],
         "Adding a constant shifts all values equally, leaving spread unchanged."),
        ("If you multiply every value by 2, the standard deviation:", ["Stays the same", "Halves", "*Doubles", "Quadruples"],
         "Multiplying by a constant scales the SD by the same factor."),
        ("The variance of a dataset is always:", ["Negative", "Equal to the mean", "*Non-negative (≥ 0)", "Equal to the SD"],
         "Variance is a sum of squared deviations, so it is always ≥ 0."),
        ("Which measure of spread is in the same units as the data?", ["Variance", "*Standard deviation", "Squared deviation", "Coefficient of variation"],
         "SD is the square root of variance, returning to the original units."),
        ("Within 3 standard deviations of the mean, approximately what percentage of data fall (Empirical Rule)?", ["68%", "95%", "*99.7%", "100%"],
         "The Empirical Rule says ~99.7% of data fall within 3 SDs of the mean."),
        ("To compare spreads of two datasets with different units, use:", ["Range", "Standard deviation alone", "*Coefficient of variation (CV = s/x̄ × 100%)", "IQR"],
         "The CV expresses SD as a percentage of the mean, allowing unit-free comparison."),
        ("If a teacher's test scores have SD = 0, this means:", ["The test was hard", "The scores were high", "*Every student scored the same", "There were no students"],
         "SD = 0 means zero variability — all values are identical."),
    ]
)
lessons[k] = v

# ── 3.3 Percentiles & Quartiles ──
k, v = build_lesson(3, 3, "Percentiles & Quartiles",
    "<h3>Percentiles & Quartiles</h3>"
    "<p><b>Percentiles</b> divide a dataset into 100 equal parts. The k-th percentile is the value below which k% of the data fall.</p>"
    "<ul><li><b>25th percentile (Q1):</b> 25% of data fall below this value.</li>"
    "<li><b>50th percentile (Q2 / Median):</b> 50% of data fall below.</li>"
    "<li><b>75th percentile (Q3):</b> 75% of data fall below.</li></ul>"
    "<p><b>Quartiles</b> divide data into four quarters:</p>"
    "<ul><li>Q1 separates the lowest 25%.</li><li>Q2 (median) separates the lower and upper halves.</li><li>Q3 separates the lowest 75%.</li></ul>"
    "<p>Percentiles are widely used in standardized testing (e.g., 'You scored in the 90th percentile means you scored higher than 90% of test-takers'), growth charts, and income reporting.</p>"
    "<p>The <b>percentile rank</b> of a value tells you what percentage of data falls at or below that value.</p>",
    [
        ("Percentile", "A value below which a given percentage of data falls; the k-th percentile has k% of data below it."),
        ("Quartile", "One of three values (Q1, Q2, Q3) that divide an ordered dataset into four equal parts."),
        ("Q1 (First Quartile)", "The 25th percentile; 25% of the data fall below this value."),
        ("Q3 (Third Quartile)", "The 75th percentile; 75% of the data fall below this value."),
        ("Percentile Rank", "The percentage of values in a dataset that fall at or below a given value."),
    ],
    [
        ("The 50th percentile is the same as:", ["Q1", "*The median", "Q3", "The mean"],
         "The 50th percentile divides the data in half, which defines the median."),
        ("If a test score is at the 85th percentile, the student scored higher than:", ["85 students", "15% of test-takers", "*85% of test-takers", "All test-takers"],
         "The 85th percentile means 85% of scores fall below that value."),
        ("Q1 is the:", ["50th percentile", "75th percentile", "*25th percentile", "100th percentile"],
         "Q1 corresponds to the 25th percentile."),
        ("Q3 is the:", ["25th percentile", "50th percentile", "*75th percentile", "90th percentile"],
         "Q3 is the 75th percentile."),
        ("The IQR equals:", ["Q1 − Q3", "Q3 + Q1", "*Q3 − Q1", "Max − Min"],
         "IQR = Q3 − Q1, the range of the middle 50% of data."),
        ("A baby at the 60th percentile for weight:", ["Is overweight", "Is underweight", "*Weighs more than 60% of babies the same age", "Weighs exactly 60 pounds"],
         "The 60th percentile means the baby is heavier than 60% of peers."),
        ("Percentiles divide data into:", ["4 parts", "10 parts", "*100 parts", "2 parts"],
         "Percentiles create 100 equal divisions of the data."),
        ("The percentile rank of a value is:", ["The value itself", "*The percentage of data at or below that value", "The z-score", "The frequency"],
         "Percentile rank tells you what portion of the data is at or below a given value."),
        ("If n = 20 and a value is greater than 15 of the 20 observations, its approximate percentile rank is:", ["15%", "20%", "*75%", "80%"],
         "Percentile rank ≈ (15/20) × 100 = 75%."),
        ("Quartiles divide data into:", ["2 parts", "*4 parts", "10 parts", "100 parts"],
         "The three quartiles split data into four equal quarters."),
        ("A student scoring at the 99th percentile:", ["Got 99%", "Answered 99 questions right", "*Scored higher than 99% of all test-takers", "Is the lowest scorer"],
         "99th percentile means 99% of scores are at or below that student's score."),
        ("Which percentile is Q2?", ["25th", "*50th", "75th", "100th"],
         "Q2 is the median, which is the 50th percentile."),
        ("Deciles divide data into:", ["4 parts", "*10 parts", "100 parts", "2 parts"],
         "Deciles create 10 equal groups: 10th, 20th, …, 90th percentiles."),
        ("If Q1 = 30 and Q3 = 70, the IQR is:", ["30", "70", "*40", "100"],
         "IQR = 70 − 30 = 40."),
        ("The 0th percentile would be:", ["The mean", "The highest value", "*The minimum or below all data", "Q1"],
         "The 0th percentile represents the lowest possible position — at or below all data."),
        ("Standardized test reports often use percentiles because:", ["They show raw scores", "They are simpler than means", "*They show how a student compares to all test-takers", "They equal letter grades"],
         "Percentiles communicate relative standing among all test-takers."),
        ("If two students are at the 80th and 90th percentiles, you can say:", ["The difference in their scores is exactly 10 points", "*The second student outperformed a higher proportion of test-takers", "Their raw scores differ by 10%", "Both scored above average"],
         "Percentiles indicate relative position, not exact score differences."),
        ("A value at the 100th percentile:", ["Doesn't exist", "*Is at or above all values in the dataset", "Is the median", "Equals zero"],
         "The 100th percentile is the maximum value."),
        ("Growth charts for children use percentiles to:", ["Measure intelligence", "*Track physical growth relative to peers of the same age", "Assign grades", "Determine income"],
         "Pediatric growth charts use percentiles to compare a child's growth to a reference population."),
        ("If your salary is at the 40th percentile, this means:", ["You earn 40% of the maximum salary", "*40% of people earn the same or less than you", "You earn $40,000", "60% earn less than you"],
         "40th percentile means 40% of the comparison group earns at or below your level."),
    ]
)
lessons[k] = v

# ── 3.4 Z-Scores & Standardization ──
k, v = build_lesson(3, 4, "Z-Scores & Standardization",
    "<h3>Z-Scores & Standardization</h3>"
    "<p>A <b>z-score</b> (standard score) tells you how many standard deviations a data value is from the mean.</p>"
    "<p><b>Formula:</b> z = (x − x̄) / s</p>"
    "<ul><li>z = 0 means the value equals the mean.</li>"
    "<li>z > 0 means the value is above the mean.</li>"
    "<li>z < 0 means the value is below the mean.</li>"
    "<li>z = 2 means the value is 2 standard deviations above the mean.</li></ul>"
    "<p><b>Standardization</b> converts data to z-scores, creating a distribution with mean 0 and standard deviation 1. This allows comparison of values from different datasets with different units or scales.</p>"
    "<p>Example: Who performed better — a student with a score of 85 (class mean 75, SD 5) or a score of 90 (class mean 82, SD 6)? Their z-scores: (85−75)/5 = 2.0 vs. (90−82)/6 ≈ 1.33. The first student is relatively higher.</p>"
    "<p>Z-scores are also used to identify <b>unusual values</b>: typically, |z| > 2 is considered unusual, and |z| > 3 is very unusual (potential outlier).</p>",
    [
        ("Z-Score", "The number of standard deviations a data value is from the mean: z = (x − x̄) / s."),
        ("Standardization", "Converting data values to z-scores, producing a distribution with mean 0 and standard deviation 1."),
        ("Standard Normal Distribution", "A normal distribution with mean 0 and standard deviation 1, resulting from standardizing data."),
        ("Unusual Value", "A data point with |z| > 2, meaning it lies more than 2 standard deviations from the mean."),
        ("Comparing Across Datasets", "Z-scores allow fair comparison of values from different distributions by putting them on the same scale."),
    ],
    [
        ("The z-score formula is:", ["z = x̄ / s", "z = x + x̄", "*z = (x − x̄) / s", "z = s / x"],
         "z = (x − mean) / standard deviation."),
        ("A z-score of 0 means:", ["The value is an outlier", "*The value equals the mean", "The SD is 0", "The data are missing"],
         "z = 0 indicates that the value is exactly at the mean."),
        ("A z-score of −1.5 means the value is:", ["1.5 above the mean", "*1.5 standard deviations below the mean", "1.5 times the mean", "Negative"],
         "A negative z-score means the value is below the mean by that many SDs."),
        ("If x̄ = 100 and s = 10, what is the z-score for x = 120?", ["10", "20", "*2", "1"],
         "z = (120 − 100) / 10 = 2."),
        ("A z-score of 2.5 is considered:", ["Normal", "Average", "*Unusual (more than 2 SDs from the mean)", "The mean"],
         "|z| > 2 is generally considered unusual."),
        ("Standardization produces a distribution with:", ["Mean = x̄ and SD = s", "*Mean = 0 and SD = 1", "Mean = 1 and SD = 0", "Mean = 100 and SD = 15"],
         "Standardized data always have mean 0 and standard deviation 1."),
        ("Z-scores allow you to:", ["Only analyze one dataset", "Ignore the mean", "*Compare values from different distributions on a common scale", "Calculate the mode"],
         "Z-scores put different datasets on the same scale for fair comparison."),
        ("Student A: score 88, mean 80, SD 4. Student B: score 92, mean 86, SD 3. Who performed better relative to their class?", ["Student B", "*Student A (z = 2.0 vs. z = 2.0 — both the same!)", "Cannot determine", "Neither"],
         "z_A = (88−80)/4 = 2.0; z_B = (92−86)/3 = 2.0. They performed equally well relative to their classes."),
        ("If z = 3, about what percentage of data in a normal distribution lies above this value?", ["3%", "5%", "1%", "*About 0.15%"],
         "By the Empirical Rule, 99.7% lies within 3 SDs, so only about 0.15% lies above z = 3."),
        ("Converting all data values to z-scores changes the:", ["Data values but not their relative positions", "*Scale (units) but keeps relative positions and shape", "Shape of the distribution", "Number of data points"],
         "Standardization rescales data but preserves the shape and relative positions."),
        ("A negative z-score always means:", ["An error", "The data are wrong", "*The value is below the mean", "The SD is negative"],
         "Negative z-scores indicate values that are less than the mean."),
        ("The z-score is unitless because:", ["It's always zero", "*Subtracting and dividing by values in the same units cancels the units", "Statistics has no units", "It uses percentages"],
         "The units cancel when you subtract the mean and divide by the SD."),
        ("If x̄ = 70 and s = 8, what value has a z-score of −2?", ["86", "62", "*54", "78"],
         "x = x̄ + z·s = 70 + (−2)(8) = 54."),
        ("For a normal distribution, approximately what percentage of z-scores fall between −1 and 1?", ["50%", "95%", "*68%", "99.7%"],
         "By the Empirical Rule, about 68% of data fall within 1 SD (z between −1 and 1)."),
        ("An observation with z = 0.5 is:", ["*Slightly above average", "At the mean", "An outlier", "Below average"],
         "z = 0.5 means half a standard deviation above the mean — slightly above average."),
        ("Two students take different exams. The ONLY way to fairly compare their performances is by using:", ["Raw scores", "Percentages", "*Z-scores (or percentiles)", "The highest score"],
         "Z-scores account for different means and SDs across exams."),
        ("If s = 0, z-scores:", ["Are all 1", "Are all positive", "*Are undefined (division by zero)", "Equal the mean"],
         "If SD = 0, all values are identical and z-scores can't be computed."),
        ("The z-score corresponding to the mean is always:", ["1", "−1", "*0", "Undefined"],
         "z = (x̄ − x̄) / s = 0."),
        ("In a standard normal distribution:", ["*Mean = 0 and SD = 1", "Mean = 100 and SD = 15", "Mean = 50 and SD = 10", "Mean = 1 and SD = 0"],
         "The standard normal has mean 0 and SD 1 by definition."),
        ("A z-score of −3 would suggest the observation is:", ["Typical", "Slightly below average", "*Very unusual — far below the mean", "Above the mean"],
         "|z| = 3 is very unusual, lying in the extreme tail of the distribution."),
    ]
)
lessons[k] = v

# ── 3.5 Coefficient of Variation ──
k, v = build_lesson(3, 5, "Coefficient of Variation",
    "<h3>Coefficient of Variation</h3>"
    "<p>The <b>Coefficient of Variation (CV)</b> expresses the standard deviation as a percentage of the mean, allowing comparison of variability between datasets with different units or scales.</p>"
    "<p><b>Formula:</b> CV = (s / x̄) × 100%</p>"
    "<ul><li>A <b>higher CV</b> indicates greater relative variability.</li>"
    "<li>A <b>lower CV</b> indicates less relative variability (more consistent data).</li>"
    "<li>The CV is <b>unitless</b>, making it ideal for comparing variability across datasets measured in different units.</li></ul>"
    "<p><b>Example:</b> Dataset A has mean 50, SD 10 → CV = 20%. Dataset B has mean 200, SD 30 → CV = 15%. Although B has a larger SD, it has less relative variability.</p>"
    "<p><b>Limitations:</b> The CV is not meaningful when the mean is zero or near zero, or for data measured on an interval scale (like temperature in °C, where 0 is not a true zero).</p>",
    [
        ("Coefficient of Variation (CV)", "The ratio of the standard deviation to the mean, expressed as a percentage: CV = (s / x̄) × 100%."),
        ("Relative Variability", "Variability expressed in proportion to the mean, allowing fair comparisons between datasets of different scales."),
        ("Unit-Free Measure", "A statistic with no units, enabling comparison across datasets measured in different units."),
        ("High CV", "Indicates greater relative spread or inconsistency in the data relative to its mean."),
        ("Low CV", "Indicates less relative spread — data are more consistent relative to their mean."),
    ],
    [
        ("The CV formula is:", ["s × x̄", "x̄ / s", "*(s / x̄) × 100%", "s − x̄"],
         "CV = (standard deviation / mean) × 100%."),
        ("The CV is useful when comparing:", ["Datasets with the same units and scale", "Only categorical data", "*Datasets with different units or scales", "Only z-scores"],
         "The CV's unitless ratio allows comparisons across different scales."),
        ("Dataset A: mean 40, SD 8. CV = ?", ["8%", "40%", "*20%", "5%"],
         "CV = (8/40) × 100% = 20%."),
        ("Dataset B: mean 200, SD 20. CV = ?", ["200%", "20%", "*10%", "0.1%"],
         "CV = (20/200) × 100% = 10%."),
        ("Between Dataset A (CV=20%) and Dataset B (CV=10%), which is more consistent?", ["Dataset A", "*Dataset B", "They're equal", "Cannot determine"],
         "A lower CV means less relative variability — Dataset B is more consistent."),
        ("The CV is unitless because:", ["It uses the mean", "*The units cancel when dividing SD by the mean", "It always equals a percentage", "It ignores units"],
         "Since SD and mean have the same units, dividing cancels them out."),
        ("When is the CV NOT meaningful?", ["When the dataset is large", "When data are quantitative", "*When the mean is zero or near zero", "When comparing two datasets"],
         "Division by zero (or near zero) makes the CV undefined or misleadingly large."),
        ("A quality control team finds CV = 2% for product weights. This suggests:", ["High variability", "*Very consistent weights", "The mean is 2", "The SD is high"],
         "A CV of 2% indicates that the SD is only 2% of the mean — very consistent."),
        ("If two machines produce bolts — Machine X (CV = 5%) vs. Machine Y (CV = 12%):", ["Machine Y is more consistent", "*Machine X is more consistent", "They are equally consistent", "CV doesn't apply"],
         "A lower CV (Machine X) means less relative variability."),
        ("The CV should not be used with interval-scale data like temperature in °C because:", ["Celsius is not a number", "*0°C is not a true zero; the ratio SD/mean isn't meaningful", "Temperature has no variability", "The CV formula doesn't accept negatives"],
         "The CV requires a ratio-level scale with a true zero for the ratio to be meaningful."),
        ("Company A has mean revenue $1M, SD $200K. Company B has mean $10M, SD $500K. Which has more relative variability?", ["*Company A (CV = 20%)", "Company B (CV = 5%)", "They're equal", "Cannot compare"],
         "CV_A = 200K/1M = 20%; CV_B = 500K/10M = 5%. Company A has more relative variability."),
        ("The CV can be compared across datasets because:", ["It uses the same units", "*It is a unitless ratio", "It always equals the SD", "It is always a whole number"],
         "Being unitless allows the CV to compare variability across any pair of datasets."),
        ("A high CV in test scores suggests:", ["All students scored the same", "The mean is high", "*Large relative variation in scores", "The test was easy"],
         "A high CV indicates scores are widely spread relative to the mean."),
        ("If every value in a dataset is multiplied by 5, the CV:", ["*Stays the same", "Increases by 5", "Decreases by 5", "Becomes 0"],
         "Both the mean and SD multiply by 5, so their ratio (CV) stays the same."),
        ("CV is expressed as:", ["A z-score", "A raw number", "*A percentage", "A frequency"],
         "The CV is reported as a percentage."),
        ("For comparing the spread of heights (cm) and weights (kg), you should use:", ["Range of each", "SD of each", "Variance of each", "*CV of each"],
         "Since heights and weights have different units, the CV enables a fair comparison."),
        ("If x̄ = 0 and s = 5, the CV is:", ["0%", "500%", "5%", "*Undefined"],
         "CV = s/x̄ = 5/0, which is undefined."),
        ("Why might you prefer the CV over just comparing standard deviations?", ["The CV is always smaller", "SD is outdated", "*SD alone doesn't account for differences in the magnitude of the mean", "The CV is easier to compute"],
         "Two datasets may have different SDs simply because their means differ; the CV normalizes for scale."),
        ("A CV of 0% means:", ["The mean is 0", "The dataset is empty", "*There is no variability — all values are identical", "The data are perfectly normal"],
         "CV = 0 when SD = 0, meaning every value equals the mean."),
        ("The population CV uses:", ["s and x̄", "*σ and μ", "Range and median", "n and k"],
         "The population CV uses the population SD (σ) and population mean (μ)."),
    ]
)
lessons[k] = v

# ── 3.6 Interpreting Data in Context ──
k, v = build_lesson(3, 6, "Interpreting Data in Context",
    "<h3>Interpreting Data in Context</h3>"
    "<p>Statistical values are meaningless without context. Interpreting data means connecting numerical results back to the real-world situation they describe.</p>"
    "<ul><li><b>Context includes:</b> Who or what was studied, what was measured, when and where the data were collected, and why the study was done.</li>"
    "<li><b>Interpreting the mean:</b> 'The average commute time for employees at Company X is 28 minutes' — not just 'x̄ = 28.'</li>"
    "<li><b>Interpreting the SD:</b> 'Commute times typically vary by about 12 minutes from the average' — not just 's = 12.'</li>"
    "<li><b>Interpreting a z-score:</b> 'A commute of 52 minutes is 2 SDs above the mean, which is unusually long compared to peers.'</li></ul>"
    "<p>Always answer in <b>complete sentences</b> that reference the variable, units, and context. Avoid naked numbers.</p>"
    "<p><b>Common interpretations on AP exams:</b></p>"
    "<ul><li>Mean: 'On average, [variable] is [value] [units].'</li>"
    "<li>SD: '[Variable] values typically differ from the mean by about [value] [units].'</li>"
    "<li>Percentile: '[Value] is at the [k]th percentile, meaning [k]% of [subjects] have a [variable] at or below [value].'</li></ul>",
    [
        ("Context in Statistics", "The real-world background (who, what, when, where, why) that gives meaning to numerical results."),
        ("Interpretation", "Explaining a statistical result in plain language that connects the number to its real-world meaning, including variable names and units."),
        ("Units", "The measurement context (e.g., minutes, dollars, kilograms) that must be included when interpreting statistics."),
        ("Naked Number", "A statistical result presented without context or explanation — to be avoided."),
        ("AP-Style Interpretation", "A complete sentence connecting a statistic to its context: 'On average, [variable] is [value] [units].'"),
    ],
    [
        ("Why must statistics be interpreted in context?", ["Numbers are always self-explanatory", "Context makes numbers bigger", "*Numbers alone are meaningless without knowing what they represent", "Context is only for presentations"],
         "Without knowing what was measured, numbers carry no real-world meaning."),
        ("A complete interpretation of x̄ = 72 should include:", ["Only the number 72", "*What was measured, the units, and who was studied", "Just the formula", "Only the sample size"],
         "A full interpretation references the variable, units, and subjects."),
        ("'s = 4.5 inches' for student heights means:", ["All students are 4.5 inches tall", "*Heights typically differ from the mean by about 4.5 inches", "The average height is 4.5 inches", "4.5% of students were measured"],
         "The SD measures typical deviation from the mean."),
        ("'The median household income is $58,000' tells us:", ["Everyone earns $58,000", "*Half of households earn less than $58,000 and half earn more", "The mean is $58,000", "The mode is $58,000"],
         "The median splits the income distribution in half."),
        ("On an AP exam, a 'naked number' answer would be:", ["A complete sentence", "*Just writing '72' without context", "A labeled graph", "A detailed explanation"],
         "A naked number lacks context and will not receive full credit on AP exams."),
        ("'A z-score of 1.8 for this exam score' should be interpreted as:", ["The score is 1.8", "*The score is 1.8 standard deviations above the class mean", "1.8 is the grade", "1.8% of students scored higher"],
         "Z-scores express distance from the mean in standard-deviation units."),
        ("'The IQR of commute times is 15 minutes' means:", ["All commutes are 15 minutes", "The range is 15 minutes", "*The middle 50% of commute times span 15 minutes", "The SD is 15"],
         "The IQR is the range of the middle 50% of the data."),
        ("Which interpretation is best? 'r = 0.85':", ["'r is 0.85'", "'It's positive'", "*'There is a strong positive linear relationship between study hours and exam scores'", "'0.85 is close to 1'"],
         "Interpretation must name the variables and describe the relationship."),
        ("Context answers which questions?", ["Only 'what'", "Only 'who'", "*Who, what, when, where, and why", "Only 'how many'"],
         "Full context addresses all relevant aspects of the study."),
        ("'95% confidence interval for the mean is (48, 52)' should be interpreted as:", ["The mean is exactly 50", "*We are 95% confident the true population mean lies between 48 and 52", "95% of data lie between 48 and 52", "The interval is 4"],
         "Confidence intervals estimate the range likely containing the population parameter."),
        ("If a report states 'SD = 3.2,' a reader should ask:", ["Nothing", "*'3.2 of what? What variable? What units?'", "'Is 3.2 a good number?'", "'Is SD the right formula?'"],
         "Without context, 3.2 is meaningless — the variable and units are essential."),
        ("'The percentage of adults who exercise daily is 23%' is interpretable because:", ["23 is a nice number", "*It specifies who (adults), what (exercise daily), and the finding (23%)", "Percentages are always clear", "It uses a formula"],
         "The sentence provides context: the group, the behavior, and the result."),
        ("When interpreting a boxplot comparison, mention:", ["Only which box is wider", "Only the median", "*Differences in center (median), spread (IQR), and any outliers, in context", "Only the outliers"],
         "A complete comparison references center, spread, outliers, and what the data represent."),
        ("Describing a distribution requires noting:", ["Only the shape", "Only outliers", "*Shape, center, spread, and unusual features — all in context", "Only the mean"],
         "A thorough description addresses all aspects and connects them to the real-world variable."),
        ("'The correlation is −0.72' should be stated as:", ["'It's negative'", "'−0.72'", "*'There is a moderately strong negative linear relationship between [x] and [y]'", "'Correlation is bad'"],
         "Interpretation must name the variables and describe the nature of the relationship."),
        ("An AP exam grader looks for:", ["Only formulas", "Only numbers", "*Correct computations AND interpretations in context", "Only context without numbers"],
         "AP scoring requires both correct numerical answers and contextual interpretation."),
        ("'On average, customers wait 7.5 minutes for service' is:", ["A naked number", "*A properly contextualized mean", "Missing information", "An outlier"],
         "It states the variable (wait time), the subjects (customers), and the result (7.5 min)."),
        ("Why is including units important?", ["It isn't", "Units are optional on exams", "*Units specify the scale of measurement, making the number meaningful", "Units are only decorative"],
         "Units tell the reader what was measured and in what scale."),
        ("Which is a better AP-style answer for a percentile?", ["'P90 = 650'", "*'A score of 650 is at the 90th percentile, meaning the student scored higher than 90% of test-takers'", "'90%' ", "'Percentile is 90'"],
         "The full sentence names the variable, the percentile, and its meaning."),
        ("Interpreting data in context is important because:", ["It makes answers longer", "It impresses the teacher", "*It connects statistical results to real-world meaning, enabling informed decisions", "It is optional"],
         "Context transforms numbers into actionable insights."),
    ]
)
lessons[k] = v

# ── 3.7 Case Studies in Sports & Medicine ──
k, v = build_lesson(3, 7, "Case Studies in Sports & Medicine",
    "<h3>Case Studies in Sports & Medicine</h3>"
    "<p>Descriptive statistics play a critical role in both sports analytics and medical research.</p>"
    "<p><b>Sports Analytics:</b></p>"
    "<ul><li><b>Batting averages, ERA, player efficiency ratings</b> are all descriptive statistics used to evaluate performance.</li>"
    "<li><b>Moneyball:</b> The Oakland A's used statistical analysis (OBP, SLG) rather than traditional scouting to build a competitive team on a small budget. This revolutionized baseball and spread to other sports.</li>"
    "<li>Modern sports use <b>tracking data</b> (player movement, speed, distance covered) to optimize training and strategy.</li></ul>"
    "<p><b>Medical Research:</b></p>"
    "<ul><li><b>Clinical trials</b> use means, medians, and survival rates to compare treatments.</li>"
    "<li><b>Vital statistics:</b> Life expectancy, infant mortality rate, and disease prevalence are descriptive measures reported by public health agencies.</li>"
    "<li><b>BMI (Body Mass Index):</b> A widely used (though debated) descriptive measure: weight(kg) / height(m)².</li>"
    "<li><b>Epidemiological studies:</b> Track disease incidence (new cases) and prevalence (total cases) to guide public health policy.</li></ul>",
    [
        ("Moneyball", "The use of advanced statistical analysis (sabermetrics) by the Oakland A's to evaluate players and build a competitive team on a limited budget."),
        ("Batting Average", "A descriptive statistic in baseball: the number of hits divided by the number of at-bats."),
        ("Clinical Trial", "A controlled medical experiment comparing treatments using descriptive and inferential statistics."),
        ("BMI (Body Mass Index)", "A descriptive measure of body composition: weight (kg) / height (m)², used in health screening."),
        ("Incidence vs. Prevalence", "Incidence: the rate of new disease cases. Prevalence: the total proportion of a population with the disease at a given time."),
    ],
    [
        ("In the Moneyball approach, the Oakland A's relied on:", ["Traditional scouting only", "The most expensive players", "*Statistical analysis to find undervalued players", "Luck"],
         "Moneyball used statistics (OBP, SLG) to identify players others overlooked."),
        ("A batting average is calculated as:", ["Runs / games", "*Hits / at-bats", "Home runs / games", "Walks / at-bats"],
         "Batting average = total hits divided by total at-bats."),
        ("In clinical trials, the median survival time is preferred over the mean because:", ["Medians are always larger", "*Survival data are often right-skewed with outliers", "Means are not allowed", "Medians are easier to say"],
         "Survival data often have a long right tail, making the median more representative."),
        ("BMI is calculated as:", ["Height / weight", "Weight × height", "*Weight (kg) / height (m)²", "Weight + height"],
         "BMI = mass in kilograms divided by the square of height in meters."),
        ("Disease incidence refers to:", ["Total current cases", "*The rate of new cases occurring in a population over a time period", "The cure rate", "The number of hospitals"],
         "Incidence measures how many new cases arise."),
        ("Disease prevalence refers to:", ["Only new cases", "The death rate", "*The total proportion of a population with the disease at a given time", "The vaccination rate"],
         "Prevalence counts all existing cases, both new and ongoing."),
        ("Player efficiency rating (PER) in basketball is a type of:", ["Inferential statistic", "*Descriptive statistic summarizing overall player performance", "Probability", "Hypothesis test"],
         "PER summarizes a player's contributions — a descriptive measure."),
        ("Modern sports analytics use tracking data to:", ["Replace all statistics", "*Optimize training, strategy, and injury prevention", "Eliminate competition", "Make games longer"],
         "Tracking data help teams fine-tune performance and reduce injuries."),
        ("In a study comparing Drug A vs. placebo, the mean blood pressure reduction in each group is an example of:", ["A hypothesis test", "*A descriptive statistic used to compare groups", "A p-value", "A confounding variable"],
         "The mean reduction summarizes each group's response — descriptive statistics."),
        ("Life expectancy is a descriptive statistic reported by:", ["Sports teams", "Banks", "*Public health agencies", "Private companies only"],
         "Life expectancy is a population-level descriptive measure tracked by public health agencies."),
        ("Why is BMI considered debated?", ["It's too accurate", "*It doesn't distinguish between muscle and fat, and may misclassify fit individuals", "It uses the wrong formula", "Nobody uses it"],
         "BMI doesn't account for body composition — muscular individuals may be classified as overweight."),
        ("OBP (On-Base Percentage) measures:", ["How fast a player runs", "*How frequently a batter reaches base", "A pitcher's effectiveness", "Fielding accuracy"],
         "OBP = (hits + walks + HBP) / (at-bats + walks + HBP + sac flies)."),
        ("In medical research, a control group that receives a placebo helps:", ["Increase sample size", "*Provide a baseline to measure the drug's actual effect", "Reduce costs", "Bias the results"],
         "The control group's response provides a comparison for the treatment group."),
        ("The infant mortality rate is a:", ["*Descriptive statistic measuring deaths of infants per 1,000 live births", "Inferential statistic", "A graph", "A p-value"],
         "It's a descriptive measure of infant deaths relative to births."),
        ("Sports analytics became mainstream after:", ["The invention of television", "The internet", "*The Moneyball era (early 2000s)", "The 1960s Olympics"],
         "Moneyball popularized the use of statistical analysis in sports decision-making."),
        ("Sabermetrics is:", ["A type of batting average", "A medical term", "*The empirical analysis of baseball through statistics", "A training method"],
         "Sabermetrics applies statistical methods to analyze baseball performance."),
        ("A study reports 'mean cholesterol decreased by 15 mg/dL in the treatment group.' This is:", ["*A descriptive result interpreted in medical context", "An hypothesis", "A raw number", "A p-value"],
         "The mean decrease summarizes the treatment effect in meaningful units."),
        ("Tracking player distance covered per game helps teams:", ["Score more goals automatically", "*Assess fitness levels and manage workload to prevent injury", "Win every game", "Eliminate the need for practice"],
         "Workload tracking informs training decisions and injury prevention."),
        ("Why should medical studies report both mean and median?", ["They're always equal", "*They provide different perspectives; the median is resistant to outliers in skewed data", "Only the mean matters", "The median replaces the mode"],
         "Reporting both gives a fuller picture, especially when data are skewed."),
        ("Statistics in sports and medicine share the goal of:", ["Entertainment only", "Eliminating all uncertainty", "*Using data to make better decisions", "Replacing human judgment entirely"],
         "In both fields, statistics inform evidence-based decisions."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 3)")
