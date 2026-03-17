#!/usr/bin/env python3
"""Generate real content for Statistics Unit 2: Data Representation (8 lessons)."""
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

# ── 2.1 Frequency Tables ──
k, v = build_lesson(2, 1, "Frequency Tables",
    "<h3>Frequency Tables</h3>"
    "<p>A <b>frequency table</b> organizes data by listing each value (or group of values) and the number of times it occurs.</p>"
    "<ul><li><b>Frequency (f):</b> The count of observations for a particular value or class.</li>"
    "<li><b>Relative frequency:</b> The proportion of the total that falls in each class: f / n.</li>"
    "<li><b>Cumulative frequency:</b> The running total of frequencies up to and including a given class.</li>"
    "<li><b>Class (bin):</b> A range of values grouped together (e.g., 60–69, 70–79).</li>"
    "<li><b>Class width:</b> The difference between the upper and lower boundaries of a class.</li></ul>"
    "<p>Frequency tables are foundational — they provide the data behind histograms and other charts. Choosing appropriate class widths is important: too few classes hide patterns; too many classes produce noise.</p>",
    [
        ("Frequency", "The number of times a particular value or class of values occurs in a dataset."),
        ("Relative Frequency", "The proportion (fraction or percentage) of observations in a particular class: frequency divided by total count."),
        ("Cumulative Frequency", "A running total of frequencies, showing how many observations fall at or below each class."),
        ("Class Width", "The difference between the upper and lower boundaries of a class interval in a frequency table."),
        ("Frequency Table", "A table that lists categories or class intervals alongside their corresponding frequencies."),
    ],
    [
        ("A frequency table shows:", ["Only the mean", "*How often each value or group of values occurs", "Just the highest value", "Only percentages"],
         "A frequency table lists values or classes with the count of observations for each."),
        ("Relative frequency is calculated as:", ["f × n", "*f / n (frequency divided by total)", "n / f", "f + n"],
         "Relative frequency equals the frequency of a class divided by the total number of observations."),
        ("Cumulative frequency:", ["Resets for each class", "*Is a running total of frequencies up to each class", "Equals the mean", "Only applies to nominal data"],
         "Cumulative frequency adds each class's frequency to the sum of all previous classes."),
        ("If 15 out of 60 students scored between 80 and 89, the relative frequency for that class is:", ["15", "60", "*0.25", "0.15"],
         "Relative frequency = 15 / 60 = 0.25 or 25%."),
        ("Class width is:", ["The frequency of a class", "The number of classes", "*The difference between the upper and lower class boundaries", "The total count"],
         "Class width = upper boundary − lower boundary of the interval."),
        ("Too few classes in a frequency table may:", ["Show every detail", "*Hide important patterns in the data", "Increase accuracy", "Create too many bars"],
         "Too few classes group data too broadly, potentially masking patterns."),
        ("Too many classes in a frequency table may:", ["*Produce noise and make patterns hard to see", "Always improve accuracy", "Hide data", "Reduce the sample size"],
         "Too many classes can fragment the data, creating noise rather than clarity."),
        ("The sum of all relative frequencies in a table should equal:", ["0", "The sample size", "The number of classes", "*1 (or 100%)"],
         "All proportions must add up to 1 (or 100%)."),
        ("A frequency table with classes 0–9, 10–19, 20–29 has a class width of:", ["9", "*10", "20", "29"],
         "Class width = 10 − 0 = 10 (or equivalently 19 − 9 = 10)."),
        ("Which column in a frequency table would help you determine the median class?", ["Frequency", "Relative frequency", "*Cumulative frequency", "Class boundaries"],
         "Cumulative frequency helps locate the class containing the median by showing how counts accumulate."),
        ("If the cumulative frequency reaches 50 at the class 70–79, and n = 100, what percentage of data falls at or below 79?", ["70%", "79%", "*50%", "100%"],
         "Cumulative frequency of 50 out of 100 means 50% of data is at or below that class."),
        ("Frequency tables are the basis for constructing:", ["Scatter plots", "Box plots", "*Histograms", "Line graphs"],
         "Histograms visualize the data organized in frequency tables."),
        ("A grouped frequency table is useful when:", ["*Data have many distinct values", "Data have only two categories", "You want to show exact values only", "The dataset is very small"],
         "When data have many unique values, grouping them into classes makes the table manageable."),
        ("The midpoint of a class 20–29 is:", ["20", "29", "*24.5", "25"],
         "Midpoint = (20 + 29) / 2 = 24.5."),
        ("If a class has frequency 0, it means:", ["The class doesn't exist", "*No observations fell in that class interval", "There's an error", "The data are missing"],
         "A frequency of 0 simply means no data points fell within that class."),
        ("Which is NOT typically part of a frequency table?", ["Frequency", "Relative frequency", "Class intervals", "*Standard deviation"],
         "Standard deviation is a summary statistic, not a column in a frequency table."),
        ("A relative frequency of 0.35 means:", ["35 observations", "35 classes", "*35% of the data falls in that class", "The mean is 0.35"],
         "A relative frequency of 0.35 indicates that 35% of all observations are in that class."),
        ("When constructing a frequency table, data should be:", ["*Mutually exclusive (each observation in only one class) and exhaustive (covering all values)", "Overlapping between classes", "Limited to 3 classes", "Only qualitative"],
         "Classes must be mutually exclusive and collectively exhaustive."),
        ("A cumulative relative frequency of 0.80 at class 60–69 means:", ["80 observations total", "80 classes", "*80% of data values are 69 or below", "20% are in that class"],
         "Cumulative relative frequency of 0.80 means 80% of data falls at or below the upper boundary of that class."),
        ("Frequency tables work for which type of data?", ["Only qualitative", "Only quantitative", "Only continuous", "*Both qualitative and quantitative data"],
         "Frequency tables can organize both categorical and numerical data."),
    ]
)
lessons[k] = v

# ── 2.2 Histograms & Bar Graphs ──
k, v = build_lesson(2, 2, "Histograms & Bar Graphs",
    "<h3>Histograms & Bar Graphs</h3>"
    "<p><b>Bar graphs</b> and <b>histograms</b> are two of the most common data visualizations, but they serve different purposes.</p>"
    "<ul><li><b>Bar graph:</b> Used for <b>categorical (qualitative)</b> data. Bars are separated by gaps. The height of each bar represents the frequency or relative frequency of each category.</li>"
    "<li><b>Histogram:</b> Used for <b>quantitative (numerical)</b> data. Bars are adjacent (no gaps) because they represent continuous intervals. The height shows frequency, and the width represents the class interval.</li></ul>"
    "<p>Key features to examine in a histogram:</p>"
    "<ul><li><b>Shape:</b> Symmetric, skewed left (tail on left), skewed right (tail on right), uniform, or bimodal.</li>"
    "<li><b>Center:</b> Where the 'middle' of the data lies.</li>"
    "<li><b>Spread:</b> How wide the distribution is.</li>"
    "<li><b>Outliers:</b> Unusual values far from the rest of the data.</li></ul>",
    [
        ("Bar Graph", "A chart using separated bars to display the frequency of categorical (qualitative) data."),
        ("Histogram", "A chart using adjacent bars to display the frequency distribution of quantitative data over continuous intervals."),
        ("Skewed Right", "A distribution with a long tail extending to the right; most data are clustered on the left."),
        ("Skewed Left", "A distribution with a long tail extending to the left; most data are clustered on the right."),
        ("Bimodal Distribution", "A distribution with two distinct peaks, suggesting two common values or groups within the data."),
    ],
    [
        ("Bar graphs are used for which type of data?", ["Quantitative only", "Continuous only", "*Categorical (qualitative) data", "Neither"],
         "Bar graphs display frequencies of categories — qualitative data."),
        ("Histograms differ from bar graphs in that histograms:", ["Have gaps between bars", "Are for categorical data", "*Have adjacent bars representing continuous intervals", "Always show percentages"],
         "Histogram bars touch because they represent consecutive numerical intervals."),
        ("A distribution with a long right tail is called:", ["Symmetric", "Skewed left", "*Skewed right", "Uniform"],
         "When the tail extends to the right, the distribution is skewed right (positively skewed)."),
        ("In a histogram, the height of each bar represents:", ["The class width", "The midpoint", "*The frequency of data in that interval", "The cumulative frequency"],
         "Each bar's height shows how many data points fall within that class interval."),
        ("A symmetric distribution:", ["Has one long tail", "*Looks roughly the same on both sides of the center", "Is always normal", "Has no center"],
         "In a symmetric distribution, the left side mirrors the right side."),
        ("A bimodal distribution has:", ["No peaks", "One peak", "*Two distinct peaks", "Three peaks"],
         "Bimodal means two modes — two values or intervals where data are most concentrated."),
        ("Which feature of a graph should you check first when analyzing a histogram?", ["Color", "*Shape (symmetric, skewed, uniform, bimodal)", "Title font", "Number of bars"],
         "Shape gives the most immediate insight into how data are distributed."),
        ("A uniform distribution in a histogram looks like:", ["One tall peak", "*Bars of roughly equal height across all classes", "A bell curve", "One bar only"],
         "A uniform distribution has approximately equal frequencies across all intervals."),
        ("Outliers in a histogram appear as:", ["*Bars isolated far from the main cluster of data", "The tallest bar", "Gaps between bars", "A symmetric pattern"],
         "Outliers show up as bars separated by gaps from the main body of the distribution."),
        ("Why should histogram bars have no gaps?", ["To save space", "For aesthetic reasons", "*Because the data are continuous and intervals are connected", "It doesn't matter"],
         "The absence of gaps reflects the continuous nature of the numerical data."),
        ("In a right-skewed distribution, the mean is typically:", ["Equal to the median", "Less than the median", "*Greater than the median", "Zero"],
         "The right tail pulls the mean to the right, making it larger than the median."),
        ("A bar graph should have gaps between bars because:", ["The data are continuous", "It's a rule for all charts", "*The categories are distinct and not connected", "It reduces bias"],
         "Gaps show that categories are separate — not part of a continuous scale."),
        ("Which is NOT a standard shape description for histograms?", ["Symmetric", "Skewed right", "Bimodal", "*Rectangular with no data"],
         "'Rectangular with no data' is not a standard distribution shape."),
        ("The spread of a histogram tells you:", ["The most common value", "The number of observations", "*How widely the data are dispersed", "The exact mean"],
         "Spread describes the range or variability in the data."),
        ("A histogram showing test scores with most students scoring high and a tail of low scores is:", ["Skewed right", "*Skewed left", "Symmetric", "Uniform"],
         "The tail of low scores extends to the left, making it left-skewed."),
        ("Which measure of center is most resistant to skew?", ["Mean", "*Median", "Mode", "Standard deviation"],
         "The median is resistant to extreme values and is preferred for skewed distributions."),
        ("If the bars of a histogram gradually decrease in height from left to right, the distribution is:", ["Symmetric", "Skewed left", "*Skewed right", "Uniform"],
         "A gradual decrease toward the right indicates a right-skewed distribution."),
        ("A bar graph showing favorite ice cream flavors should:", ["Use adjacent bars with no gaps", "*Use separated bars, one for each flavor", "Use a histogram", "Order bars by value"],
         "Ice cream flavors are categories, so a bar graph with gaps is appropriate."),
        ("To describe a distribution fully, you should mention:", ["Only the shape", "Only the center", "*Shape, center, spread, and any outliers", "Only the outliers"],
         "A complete description addresses shape, center, spread, and unusual features."),
        ("Relative frequency histograms show:", ["Raw counts", "*Proportions or percentages on the y-axis", "Cumulative totals", "Only the mode"],
         "Relative frequency histograms use proportions instead of raw counts on the vertical axis."),
    ]
)
lessons[k] = v

# ── 2.3 Stem-and-Leaf Plots ──
k, v = build_lesson(2, 3, "Stem-and-Leaf Plots",
    "<h3>Stem-and-Leaf Plots</h3>"
    "<p>A <b>stem-and-leaf plot</b> (stemplot) is a way to display quantitative data while preserving the individual data values. It combines features of a table and a histogram.</p>"
    "<ul><li><b>Stem:</b> The leading digit(s) of each data value (e.g., the tens digit for two-digit numbers).</li>"
    "<li><b>Leaf:</b> The trailing digit(s) (e.g., the ones digit).</li>"
    "<li>Example: For data values 23, 25, 31, 37, 38, the stems are 2 and 3; the leaves for stem 2 are 3, 5; for stem 3 are 1, 7, 8.</li></ul>"
    "<p>Advantages: Shows the shape of the distribution like a histogram, but retains the exact data values. Useful for small to moderate datasets.</p>"
    "<p>A <b>back-to-back stem-and-leaf plot</b> compares two datasets using a shared stem, with leaves extending in opposite directions.</p>"
    "<p>Limitations: Not practical for very large datasets or data with many decimal places.</p>",
    [
        ("Stem", "The leading digit(s) of a data value in a stem-and-leaf plot (e.g., the tens place for two-digit numbers)."),
        ("Leaf", "The trailing digit of a data value in a stem-and-leaf plot (e.g., the ones place)."),
        ("Stem-and-Leaf Plot", "A data display that organizes data by their leading digits (stems) and trailing digits (leaves), showing distribution shape while preserving exact values."),
        ("Back-to-Back Stemplot", "A stem-and-leaf plot that compares two datasets using a shared stem column with leaves extending in opposite directions."),
        ("Split Stems", "A technique that divides each stem into two (or more) rows to spread out the data for better visibility."),
    ],
    [
        ("In a stem-and-leaf plot, the stem represents:", ["The last digit", "*The leading digit(s) of each value", "The frequency", "The mean"],
         "The stem is formed by the leading digit(s) of each data value."),
        ("The leaf in a stemplot represents:", ["The leading digit", "The frequency", "*The trailing digit of each value", "The class width"],
         "The leaf is the final digit of the data value."),
        ("For the value 47, in a standard stemplot the stem is __ and the leaf is __:", ["4 and 47", "47 and 4", "*4 and 7", "7 and 4"],
         "For two-digit numbers, the stem is the tens digit (4) and the leaf is the ones digit (7)."),
        ("An advantage of stem-and-leaf plots over histograms is:", ["They work for large datasets", "They hide individual values", "*They preserve the exact data values", "They only work for categorical data"],
         "Stemplots show every individual data value unlike histograms which only show frequencies per class."),
        ("A back-to-back stemplot is used to:", ["Display three datasets", "*Compare two related datasets side by side", "Show cumulative frequencies", "Only display categorical data"],
         "Back-to-back stemplots use a shared stem to compare two distributions."),
        ("For the data set {32, 35, 41, 44, 48, 53}, stem 4 has leaves:", ["3, 5", "3", "*1, 4, 8", "5, 3"],
         "Values 41, 44, 48 all have stem 4, with leaves 1, 4, 8."),
        ("Stem-and-leaf plots are most practical for:", ["Very large datasets (thousands of values)", "*Small to moderate datasets", "Categorical data only", "Data with many decimal places"],
         "Stemplots become unwieldy with very large datasets; they are best for small to moderate sizes."),
        ("In a stemplot, leaves should be:", ["*Written in increasing order on each stem row", "Randomly ordered", "Written largest to smallest", "Grouped by color"],
         "Leaves are typically arranged in ascending order for easy reading."),
        ("Split stems are used when:", ["There are too few stems", "Data are categorical", "*Data are clustered on just a few stems and more detail is needed", "The dataset is very large"],
         "Splitting stems provides more rows and better reveals the distribution's shape."),
        ("A stemplot of test scores: Stem 7 | Leaves: 2 3 5 8 8 9. How many students scored in the 70s?", ["5", "*6", "7", "8"],
         "There are 6 leaves on stem 7, so 6 students scored in the 70s."),
        ("The shape of a stemplot's distribution can be seen by:", ["Reading the stems", "Counting the total leaves", "*Looking at the length of leaf rows, similar to a sideways histogram", "Checking the first leaf only"],
         "Longer rows of leaves correspond to taller bars in a histogram, revealing the shape."),
        ("For the value 108, a stemplot might use stem __ and leaf __:", ["1 and 08", "10 and 08", "*10 and 8", "108 and 0"],
         "For three-digit numbers, the stem is typically all digits except the last: stem = 10, leaf = 8."),
        ("Which cannot be determined from a stemplot?", ["Individual data values", "Shape of distribution", "Range of data", "*The exact mean at a glance"],
         "While you can calculate the mean from the values, it's not immediately visible from the plot."),
        ("A stemplot is similar to a histogram turned:", ["Upside down", "Into a table", "*On its side", "Into a pie chart"],
         "A stemplot looks like a sideways histogram, with rows instead of vertical bars."),
        ("If every leaf on stem 5 is a 0 (e.g., 50, 50, 50), this means:", ["There is an error", "*Three data values of 50 exist", "The stem is wrong", "Only one value exists"],
         "Repeated leaves indicate repeated data values."),
        ("An ordered stemplot shows:", ["Data in random order", "Only the stems", "*Leaves in sorted order within each stem", "Cumulative frequencies"],
         "In an ordered stemplot, leaves are sorted least to greatest on each stem row."),
        ("What is a limitation of stem-and-leaf plots?", ["They don't show individual values", "They can't show shape", "*They are impractical for very large datasets", "They only work for nominal data"],
         "With thousands of data points, stemplots become too long and cluttered."),
        ("How does a stemplot help identify outliers?", ["It highlights them in color", "*Values on isolated stems far from the rest stand out", "It calculates IQR", "It removes them automatically"],
         "Outliers appear on stems that are far from the bulk of the data, making them visible."),
        ("A stemplot of ages: Stem 1 | 5 6 7 8; Stem 2 | 0 1 3 5 8; Stem 3 | 2. The range is:", ["15", "*17", "32", "8"],
         "Range = largest value (32) – smallest value (15) = 17."),
        ("Stemplots are appropriate for which level of measurement?", ["Nominal", "Ordinal", "*Interval or Ratio", "All levels"],
         "Stemplots display numerical data, which requires at least interval-level measurement."),
    ]
)
lessons[k] = v

# ── 2.4 Boxplots & Quartiles ──
k, v = build_lesson(2, 4, "Boxplots & Quartiles",
    "<h3>Boxplots & Quartiles</h3>"
    "<p>A <b>boxplot</b> (box-and-whisker plot) displays the five-number summary of a dataset: minimum, Q1, median, Q3, and maximum.</p>"
    "<ul><li><b>Quartile 1 (Q1):</b> The 25th percentile — 25% of data fall below this value.</li>"
    "<li><b>Median (Q2):</b> The 50th percentile — the middle value of the ordered data.</li>"
    "<li><b>Quartile 3 (Q3):</b> The 75th percentile — 75% of data fall below this value.</li>"
    "<li><b>Interquartile Range (IQR):</b> Q3 − Q1, measuring the spread of the middle 50% of data.</li>"
    "<li><b>Outliers:</b> Values below Q1 − 1.5×IQR or above Q3 + 1.5×IQR are flagged as outliers.</li></ul>"
    "<p>The box spans from Q1 to Q3, with a line at the median. Whiskers extend to the smallest and largest non-outlier values. Outliers are plotted as individual points.</p>"
    "<p>Boxplots are excellent for comparing distributions across groups and for identifying skewness and outliers at a glance.</p>",
    [
        ("Five-Number Summary", "A summary of a dataset consisting of: minimum, Q1, median (Q2), Q3, and maximum."),
        ("Interquartile Range (IQR)", "The range of the middle 50% of data, calculated as Q3 − Q1."),
        ("Boxplot", "A graphical display showing the five-number summary, with a box from Q1 to Q3, a median line, whiskers, and outlier points."),
        ("Outlier (1.5×IQR Rule)", "A data point that falls more than 1.5 × IQR below Q1 or above Q3."),
        ("Whiskers", "The lines extending from the box of a boxplot to the smallest and largest non-outlier data values."),
    ],
    [
        ("The five-number summary includes:", ["Mean, median, mode, range, IQR", "*Minimum, Q1, median, Q3, maximum", "All data values", "Only the mean and standard deviation"],
         "The five-number summary consists of min, Q1, median, Q3, and max."),
        ("Q1 represents the:", ["Mean", "75th percentile", "*25th percentile", "100th percentile"],
         "Q1 is the first quartile, or the 25th percentile."),
        ("The IQR measures:", ["The total range", "The mean", "*The spread of the middle 50% of data", "The median"],
         "IQR = Q3 − Q1, capturing the range of the central half of the data."),
        ("In a boxplot, the box extends from:", ["Min to max", "*Q1 to Q3", "Mean − SD to mean + SD", "0 to the median"],
         "The box spans from the first quartile to the third quartile."),
        ("An outlier is identified using:", ["The mean", "*The 1.5 × IQR rule", "The mode", "The range only"],
         "Outliers fall below Q1 − 1.5×IQR or above Q3 + 1.5×IQR."),
        ("If Q1 = 20, Q3 = 40, the IQR is:", ["20 to 40", "60", "*20", "10"],
         "IQR = 40 − 20 = 20."),
        ("Using Q1 = 20, Q3 = 40, IQR = 20: the upper outlier boundary is:", ["50", "*70", "40", "60"],
         "Upper boundary = Q3 + 1.5×IQR = 40 + 30 = 70."),
        ("Whiskers in a boxplot extend to:", ["Always the min and max", "*The most extreme non-outlier values", "Q1 and Q3", "The mean"],
         "Whiskers extend from the box to the smallest and largest values that are not outliers."),
        ("A boxplot with a longer right whisker suggests:", ["*Right (positive) skew", "Left skew", "Symmetry", "No spread"],
         "A longer right whisker indicates data spread further to the right — right skew."),
        ("Boxplots are especially useful for:", ["Showing every data point", "*Comparing distributions across groups", "Displaying categorical data", "Calculating the mean"],
         "Side-by-side boxplots efficiently compare distributions of different groups."),
        ("The median in a boxplot is shown as:", ["The end of a whisker", "*A line inside the box", "A dot outside the box", "The midpoint of a whisker"],
         "A vertical or horizontal line inside the box marks the median."),
        ("If the median line is closer to Q1 than Q3, the distribution is likely:", ["Symmetric", "Skewed left", "*Skewed right", "Uniform"],
         "When the median is closer to Q1, there is more spread above the median — right skew."),
        ("Outliers in a boxplot are plotted as:", ["Part of the whisker", "Inside the box", "*Individual points beyond the whiskers", "Not shown"],
         "Outliers are shown as individual dots or asterisks beyond the whiskers."),
        ("For the data {2, 5, 7, 9, 11, 14, 18}, Q2 (median) is:", ["7", "*9", "11", "10"],
         "With 7 values, the median is the 4th value: 9."),
        ("Which gives more detail about a distribution: a boxplot or a histogram?", ["Boxplot", "*Histogram (it shows the full shape)", "They are identical", "Neither"],
         "Histograms show the full shape of the distribution; boxplots provide a summary."),
        ("Two boxplots side by side with one having a much wider box means:", ["*That dataset has greater variability in its middle 50%", "That dataset has more data points", "They are equivalent", "The wider box has a smaller IQR"],
         "A wider box means a larger IQR and greater variability in the central data."),
        ("A modified boxplot:", ["Does not show outliers", "*Shows outliers as individual points", "Removes the median", "Has no whiskers"],
         "A modified (standard) boxplot explicitly marks outliers as individual points."),
        ("If a dataset has no outliers, whiskers extend to:", ["*The minimum and maximum values", "Q1 and Q3", "The mean ± SD", "Arbitrary values"],
         "With no outliers, the whiskers reach the actual minimum and maximum."),
        ("The 50th percentile is the same as:", ["Q1", "*The median (Q2)", "Q3", "The mode"],
         "The median divides the data in half and is the 50th percentile."),
        ("Boxplots do NOT directly show:", ["*The exact shape of the distribution (e.g., bimodal)", "Outliers", "The median", "The IQR"],
         "Boxplots cannot reveal bimodality or other detailed shape features."),
    ]
)
lessons[k] = v

# ── 2.5 Scatterplots & Correlation ──
k, v = build_lesson(2, 5, "Scatterplots & Correlation",
    "<h3>Scatterplots & Correlation</h3>"
    "<p>A <b>scatterplot</b> displays the relationship between two quantitative variables. Each point represents one observation with coordinates (x, y).</p>"
    "<ul><li><b>Explanatory variable (x):</b> The independent variable, plotted on the horizontal axis.</li>"
    "<li><b>Response variable (y):</b> The dependent variable, plotted on the vertical axis.</li>"
    "<li>When examining a scatterplot, describe the <b>direction</b> (positive or negative), <b>form</b> (linear or nonlinear), and <b>strength</b> (strong, moderate, weak) of the relationship.</li></ul>"
    "<p>The <b>correlation coefficient (r)</b> measures the strength and direction of a linear relationship between two variables.</p>"
    "<ul><li>r ranges from −1 to +1.</li>"
    "<li>r = +1: perfect positive linear relationship.</li>"
    "<li>r = −1: perfect negative linear relationship.</li>"
    "<li>r = 0: no linear relationship.</li>"
    "<li>r is unitless and not affected by changes in units or which variable is x or y.</li></ul>"
    "<p><b>Caution:</b> Correlation does not imply causation. Also, r only measures <i>linear</i> relationships — a strong curved pattern may have r near 0.</p>",
    [
        ("Scatterplot", "A graph displaying the relationship between two quantitative variables, with each point representing one observation."),
        ("Correlation Coefficient (r)", "A numerical measure from −1 to +1 indicating the strength and direction of a linear relationship between two variables."),
        ("Positive Correlation", "A relationship where both variables increase together (as x increases, y increases)."),
        ("Negative Correlation", "A relationship where one variable increases as the other decreases (as x increases, y decreases)."),
        ("Explanatory Variable", "The independent variable (x) thought to influence or predict the response variable (y)."),
    ],
    [
        ("A scatterplot is used to display the relationship between:", ["Two categorical variables", "*Two quantitative variables", "A categorical and a quantitative variable", "Three variables"],
         "Scatterplots show how two numerical variables relate to each other."),
        ("The explanatory variable is typically plotted on:", ["The y-axis", "*The x-axis", "Either axis", "A separate chart"],
         "By convention, the explanatory (independent) variable is placed on the horizontal (x) axis."),
        ("A correlation coefficient of r = 0.95 indicates:", ["*A strong positive linear relationship", "A weak relationship", "No relationship", "A perfect relationship"],
         "r = 0.95 is close to +1, indicating a strong positive linear relationship."),
        ("If r = −0.85, the relationship is:", ["Strong and positive", "Weak and negative", "*Strong and negative", "No relationship"],
         "r = −0.85 indicates a strong negative linear relationship."),
        ("r = 0 means:", ["A strong relationship", "A perfect linear relationship", "*No linear relationship (though a nonlinear one may exist)", "The data are random"],
         "r = 0 means no linear association, but a curved relationship is still possible."),
        ("The range of r is:", ["0 to 1", "*−1 to +1", "−∞ to +∞", "0 to 100"],
         "The correlation coefficient r can only take values between −1 and +1."),
        ("In a scatterplot with a positive association:", ["*As x increases, y tends to increase", "As x increases, y tends to decrease", "Points form a horizontal line", "There is no pattern"],
         "Positive association means both variables tend to increase together."),
        ("Correlation measures only:", ["Any relationship", "*Linear relationships", "Curved relationships", "Categorical relationships"],
         "r quantifies the strength of a linear relationship only."),
        ("Even with r = 0.9, we cannot conclude causation because:", ["0.9 is not high enough", "Correlation is always wrong", "*Correlation does not imply causation; confounders may exist", "Scatterplots are unreliable"],
         "A strong correlation does not prove that one variable causes changes in the other."),
        ("Which scatterplot pattern would have r closest to 0?", ["Points along a steep upward line", "Points along a downward line", "*Points scattered randomly with no pattern", "A tight cluster"],
         "A random scatter with no discernible pattern has r near 0."),
        ("The correlation coefficient is:", ["Measured in the units of x", "Measured in the units of y", "*Unitless", "Measured in the units of x times y"],
         "r is a dimensionless number — it has no units."),
        ("A scatterplot shows points forming a clear U-shape. The value of r is likely:", ["Close to +1", "Close to −1", "*Close to 0", "Exactly −1"],
         "r only captures linear trends; a U-shape is nonlinear and r will be near 0."),
        ("If switching x and y variables, r:", ["Changes sign", "Becomes 0", "*Stays the same", "Doubles"],
         "The correlation coefficient doesn't depend on which variable is x and which is y."),
        ("Strength of a linear relationship is described as:", ["Only strong or weak", "*Strong, moderate, or weak based on how close |r| is to 1", "Always strong if r > 0", "Always the same"],
         "Strength is determined by how close the absolute value of r is to 1."),
        ("'Form' in a scatterplot description refers to:", ["The axis labels", "*Whether the relationship is linear or nonlinear", "The color of points", "The number of points"],
         "Form describes the overall pattern — linear (straight) or nonlinear (curved)."),
        ("A negative correlation means:", ["Bad data", "No relationship", "*As one variable increases, the other tends to decrease", "The variables are the same"],
         "Negative correlation means the variables move in opposite directions."),
        ("Outliers in a scatterplot:", ["*Can strongly affect the correlation coefficient", "Never affect r", "Always increase r", "Always decrease r"],
         "A single outlier can substantially raise or lower the value of r."),
        ("An r value of +1 means:", ["No relationship", "A weak relationship", "A strong nonlinear relationship", "*Every point falls exactly on a line with positive slope"],
         "r = +1 indicates a perfect positive linear relationship."),
        ("Which description is most complete for a scatterplot?", ["Just direction", "*Direction, form, strength, and any unusual features", "Just r", "Just the number of points"],
         "A full description includes direction, form, strength, and any outliers or unusual patterns."),
        ("Two variables with r = 0 might still be:", ["Linearly related", "*Related in a nonlinear way", "Perfectly correlated", "Identical"],
         "r only measures linear association; a strong curved relationship can have r ≈ 0."),
    ]
)
lessons[k] = v

# ── 2.6 Pie Charts & Circle Graphs ──
k, v = build_lesson(2, 6, "Pie Charts & Circle Graphs",
    "<h3>Pie Charts & Circle Graphs</h3>"
    "<p>A <b>pie chart</b> (circle graph) displays categorical data as slices of a circle, where each slice's size represents the proportion of the whole.</p>"
    "<ul><li>The entire circle represents 100% of the data.</li>"
    "<li>Each slice's central angle = (relative frequency) × 360°.</li>"
    "<li>Pie charts are best for showing parts of a whole when there are <b>few categories</b> (typically 2–6).</li></ul>"
    "<p><b>When to use pie charts:</b></p>"
    "<ul><li>Showing proportions or percentages of a total.</li>"
    "<li>Comparing a few categories to the whole.</li></ul>"
    "<p><b>When NOT to use pie charts:</b></p>"
    "<ul><li>When there are many categories (too many small slices).</li>"
    "<li>When comparing exact values between categories (bar charts are better).</li>"
    "<li>When displaying data that do not sum to a meaningful whole.</li></ul>"
    "<p>3D pie charts should generally be avoided because the perspective distorts slice sizes.</p>",
    [
        ("Pie Chart", "A circular graph divided into slices that represent the proportion or percentage each category contributes to the whole."),
        ("Central Angle", "The angle of a pie-chart slice, calculated as the category's relative frequency multiplied by 360°."),
        ("Relative Frequency", "The proportion of the total represented by each category, equal to the frequency divided by the total count."),
        ("Parts of a Whole", "The concept that all slices of a pie chart must sum to 100% of the data."),
        ("3D Pie Chart", "A pie chart with three-dimensional perspective that can distort the perceived sizes of slices; generally not recommended."),
    ],
    [
        ("A pie chart is best used for:", ["Quantitative data over time", "Comparing means", "*Showing parts of a whole for categorical data", "Displaying regression lines"],
         "Pie charts show how categorical data proportionally make up a total."),
        ("The central angle for a category representing 25% of the data is:", ["25°", "90°", "*90°", "180°"],
         "Central angle = 0.25 × 360° = 90°."),
        ("Pie charts work best with:", ["*A few categories (2–6)", "Many categories (20+)", "Only quantitative data", "Time-series data"],
         "With too many categories, slices become too small to read."),
        ("All slices of a pie chart must sum to:", ["50%", "360", "*100% (or 360°)", "The mean"],
         "The entire pie represents the complete dataset — 100%."),
        ("A category with a relative frequency of 0.10 has a central angle of:", ["10°", "*36°", "100°", "0.10°"],
         "0.10 × 360° = 36°."),
        ("Why should 3D pie charts be avoided?", ["They are too colorful", "*The 3D perspective distorts slice sizes", "They cannot show percentages", "They require more data"],
         "3D effects alter the visual appearance, making some slices look larger or smaller than they are."),
        ("When is a bar chart preferred over a pie chart?", ["Never", "When showing proportions", "*When comparing exact values across categories", "When data sum to 100%"],
         "Bar charts make it easier to compare precise values between categories."),
        ("If a dataset has 8 categories, a pie chart is:", ["Ideal", "The only option", "*Likely too crowded; a bar chart might be clearer", "Impossible to create"],
         "With many categories, pie charts become cluttered and hard to read."),
        ("A pie chart displaying data that does not sum to a meaningful whole is:", ["Fine", "*Misleading", "More accurate", "Required"],
         "Pie charts require that slices represent parts of a single meaningful total."),
        ("The largest slice in a pie chart represents:", ["The smallest frequency", "The median", "*The category with the highest relative frequency", "The outlier"],
         "Larger slices correspond to categories that make up a greater proportion of the whole."),
        ("In a survey of 200 people, 80 chose pizza. The slice for pizza is:", ["80°", "*144°", "200°", "40°"],
         "(80/200) × 360° = 0.40 × 360° = 144°."),
        ("Pie charts cannot show:", ["Proportions", "Percentages", "*Trends over time", "Parts of a whole"],
         "Pie charts are static — they don't demonstrate how data change over time."),
        ("If two categories each have 30% of the data, their slices:", ["Are different sizes", "Have a 60° angle each", "*Each have a 108° central angle", "Cannot be drawn"],
         "0.30 × 360° = 108° for each slice."),
        ("Labels in a pie chart typically show:", ["Only colors", "*Category names and percentages or values", "Only the total", "Nothing"],
         "Good pie charts label each slice with the category name and its percentage."),
        ("A pie chart with one dominant category (85%) and several small ones might be:", ["The best choice", "*Hard to read for the small categories", "Impossible", "Perfectly balanced"],
         "Very small slices are difficult to distinguish visually."),
        ("Exploded pie charts:", ["Are always better", "*Separate one or more slices for emphasis, but can distort perception", "Are the same as 3D", "Show time series"],
         "Pulling out slices can emphasize them but may also distort visual comparisons."),
        ("A pie chart is inappropriate when:", ["Data represent parts of a whole", "There are 3 categories", "All percentages sum to 100%", "*Categories do not sum to a meaningful total"],
         "If the data are not parts of one whole, a pie chart is misleading."),
        ("Pie charts are a type of:", ["Histogram", "Stemplot", "*Categorical data display", "Scatterplot"],
         "Pie charts are specifically designed for categorical (qualitative) data."),
        ("The percentage a slice represents can be found by:", ["Multiplying frequency by 360", "Dividing 360 by frequency", "*Dividing the frequency by the total and multiplying by 100", "Adding all frequencies"],
         "Percentage = (frequency / total) × 100%."),
        ("The best practice for pie charts is to:", ["Use 3D effects", "Include as many slices as possible", "*Limit categories, use clear labels, avoid 3D", "Never use them"],
         "Best practice: few categories, clear labels, and avoid 3D distortion."),
    ]
)
lessons[k] = v

# ── 2.7 Choosing Appropriate Graphs ──
k, v = build_lesson(2, 7, "Choosing Appropriate Graphs",
    "<h3>Choosing Appropriate Graphs</h3>"
    "<p>Selecting the right graph for your data is crucial for effective communication. The choice depends on the <b>type of data</b> and the <b>purpose</b> of the display.</p>"
    "<p><b>Categorical data:</b></p>"
    "<ul><li><b>Bar chart:</b> Compare frequencies or values across categories.</li>"
    "<li><b>Pie chart:</b> Show proportions of a whole (best with few categories).</li></ul>"
    "<p><b>Quantitative data – one variable:</b></p>"
    "<ul><li><b>Histogram:</b> Show the shape of a distribution.</li>"
    "<li><b>Stemplot:</b> Show distribution while preserving individual values (small datasets).</li>"
    "<li><b>Boxplot:</b> Summarize distribution and compare groups; highlight outliers.</li>"
    "<li><b>Dotplot:</b> Show individual values for small datasets.</li></ul>"
    "<p><b>Quantitative data – two variables:</b></p>"
    "<ul><li><b>Scatterplot:</b> Show the relationship between two quantitative variables.</li>"
    "<li><b>Line graph:</b> Show trends over time (time series).</li></ul>"
    "<p>Ask yourself: <i>What am I trying to show — distribution, comparison, relationship, or trend?</i></p>",
    [
        ("Bar Chart", "A graph that uses separated bars to compare frequencies or values across categories of qualitative data."),
        ("Histogram", "A graph with adjacent bars that displays the frequency distribution of a single quantitative variable."),
        ("Boxplot", "A graph summarizing a distribution with its five-number summary; ideal for comparing multiple groups."),
        ("Scatterplot", "A graph that plots pairs of quantitative data to show the relationship between two variables."),
        ("Line Graph", "A graph that connects data points with lines, primarily used to display trends over time."),
    ],
    [
        ("Which graph best compares frequencies of categorical data?", ["Histogram", "*Bar chart", "Scatterplot", "Boxplot"],
         "Bar charts are designed for comparing frequencies across categories."),
        ("Which graph shows the distribution shape of quantitative data?", ["Pie chart", "Bar chart", "*Histogram", "Line graph"],
         "Histograms display how quantitative data are distributed across intervals."),
        ("To compare distributions of test scores across three classes, use:", ["Three pie charts", "One scatterplot", "*Side-by-side boxplots", "A single bar chart"],
         "Side-by-side boxplots efficiently compare distributions across multiple groups."),
        ("A scatterplot is appropriate when you want to show:", ["Parts of a whole", "Trends over time only", "*The relationship between two quantitative variables", "Categorical frequencies"],
         "Scatterplots display relationships between paired quantitative variables."),
        ("Time series data are best displayed with:", ["A pie chart", "A boxplot", "A stemplot", "*A line graph"],
         "Line graphs connect data points over time, showing trends."),
        ("For a small dataset of 20 values where you want to see each value, use:", ["A pie chart", "*A stemplot or dotplot", "Only a boxplot", "A scatterplot"],
         "Stemplots and dotplots preserve individual data values and work well for small datasets."),
        ("Pie charts are appropriate for:", ["Two quantitative variables", "*Categorical data showing parts of a whole", "Distributions of numerical data", "Time trends"],
         "Pie charts show how categories proportionally make up a total."),
        ("Which graph cannot show bimodality?", ["Histogram", "Dotplot", "Stemplot", "*Boxplot"],
         "Boxplots only show the five-number summary and cannot reveal bimodal shapes."),
        ("When choosing a graph, the first question is:", ["What color to use", "How large to make it", "*What type of data do I have and what do I want to show?", "How many axes to include"],
         "The data type and purpose determine which graph is most appropriate."),
        ("A dotplot is best for:", ["Very large datasets", "*Small datasets where you want to see every data point", "Categorical data with many categories", "Two-variable relationships"],
         "Dotplots show each individual value and work best with small datasets."),
        ("To show proportions of a budget across 5 departments:", ["Use a scatterplot", "Use a histogram", "*Use a pie chart or bar chart", "Use a stemplot"],
         "Budget proportions across categories are well-suited for pie charts or bar charts."),
        ("A histogram should NOT be used for:", ["Continuous data", "Discrete data with many values", "Showing distribution shape", "*Categorical data like favorite colors"],
         "Histograms are for quantitative data; use bar charts for categorical data."),
        ("Which combination is incorrect?", ["Scatterplot – two quantitative variables", "Bar chart – categorical data", "Line graph – time series data", "*Pie chart – relationship between two variables"],
         "Pie charts show parts of a whole, not relationships between two variables."),
        ("To display how a stock price changed daily over a year:", ["Boxplot", "Pie chart", "Stemplot", "*Line graph"],
         "Daily price over time is a time series, best shown with a line graph."),
        ("For comparing medians and spreads of several groups:", ["Scatterplots", "Pie charts", "*Boxplots", "Stemplots"],
         "Boxplots concisely display the median, spread, and outliers for multiple groups."),
        ("Which graph is most versatile for quantitative data?", ["Pie chart", "Bar chart", "*Histogram", "Circle graph"],
         "Histograms are widely used for any quantitative distribution."),
        ("A back-to-back stemplot is used to:", ["Show time trends", "*Compare two related quantitative datasets", "Show categorical data", "Replace a pie chart"],
         "Back-to-back stemplots compare two distributions using a shared stem."),
        ("You have data on 500 students' test scores. Which graph is LEAST practical?", ["Histogram", "Boxplot", "*Stemplot", "Dotplot"],
         "Stemplots become unwieldy with 500 data points."),
        ("When data do not sum to a whole, which graph should you avoid?", ["Bar chart", "Histogram", "Scatterplot", "*Pie chart"],
         "Pie charts require data that represent parts of one complete total."),
        ("Graph choice can influence how an audience interprets data because:", ["Graphs are always misleading", "Graph choice doesn't matter", "*Different graphs highlight different aspects and some can exaggerate or obscure features", "All graphs show the same information"],
         "The choice of graph affects which patterns are visible and can shape interpretation."),
    ]
)
lessons[k] = v

# ── 2.8 Case Studies in Data Visualization ──
k, v = build_lesson(2, 8, "Case Studies in Data Visualization",
    "<h3>Case Studies in Data Visualization</h3>"
    "<p>Effective data visualization tells a clear story with data. History provides powerful examples — as well as cautionary tales.</p>"
    "<ul><li><b>Florence Nightingale's Rose Diagram (1858):</b> Used a polar area chart to demonstrate that most British soldiers in the Crimean War died from preventable disease rather than battle wounds. Her visualization changed military medical policy.</li>"
    "<li><b>John Snow's Cholera Map (1854):</b> Plotted cholera deaths on a London street map, revealing a cluster around the Broad Street water pump. This visualization helped identify contaminated water as the source and is a landmark in epidemiology.</li>"
    "<li><b>Charles Minard's Map (1869):</b> Depicted Napoleon's 1812 Russian campaign, combining army size, geographic location, direction of movement, and temperature in a single graphic. Considered one of the greatest statistical graphics ever produced.</li>"
    "<li><b>Modern misuse:</b> Truncated y-axes in news graphics, misleading scale choices, and cherry-picked timeframes continue to be common problems.</li></ul>"
    "<p>Good visualization principles: choose the right graph type, label axes clearly, avoid distortion, provide context, and let the data speak.</p>",
    [
        ("Florence Nightingale's Rose Diagram", "A polar area chart (1858) showing that preventable disease killed more soldiers than combat in the Crimean War, leading to medical reform."),
        ("John Snow's Cholera Map", "An 1854 map of cholera deaths in London that identified a contaminated water pump as the source, a landmark in epidemiology."),
        ("Minard's Map", "Charles Minard's 1869 graphic depicting Napoleon's Russian campaign, integrating army size, location, direction, and temperature — often called the greatest statistical graphic."),
        ("Data Visualization", "The graphical representation of data to communicate patterns, trends, and insights clearly and effectively."),
        ("Truncated Y-Axis", "A graph where the y-axis does not start at zero, potentially exaggerating small differences in data."),
    ],
    [
        ("Florence Nightingale used data visualization to show that:", ["Battle wounds were the main cause of death", "*Preventable disease killed more soldiers than combat", "Hospitals were unnecessary", "The war was short"],
         "Her Rose Diagram revealed that most military deaths were from preventable disease, driving medical reforms."),
        ("John Snow's cholera map is famous for:", ["*Identifying a contaminated water pump as the source of a cholera outbreak", "Showing Napoleon's army", "Displaying budget data", "Proving germ theory conclusively"],
         "Snow plotted deaths on a map, revealing the cluster around the Broad Street pump."),
        ("Minard's map of Napoleon's campaign is renowned because it:", ["Uses bright colors", "*Integrates multiple variables (army size, location, direction, temperature) in one graphic", "Is a pie chart", "Was the first bar chart"],
         "Minard's graphic combined six types of data into a single compelling image."),
        ("A truncated y-axis can:", ["Always improve a graph", "*Exaggerate small differences between data values", "Only reduce differences", "Never mislead"],
         "Not starting the y-axis at zero can make small differences look much larger."),
        ("Good data visualization should:", ["Use as many colors as possible", "Always use 3D effects", "*Choose the right graph, label clearly, avoid distortion, and provide context", "Hide the data source"],
         "Effective visualizations are clear, honest, well-labeled, and contextual."),
        ("John Snow's map is a landmark in which field?", ["Astronomy", "Physics", "*Epidemiology", "Economics"],
         "Snow's work mapping cholera deaths helped found modern epidemiology."),
        ("Nightingale's contribution changed:", ["*Military medical policy", "Fashion design", "Cooking standards", "Tax policy"],
         "Her data-driven arguments led to sanitation reforms saving thousands of soldiers' lives."),
        ("A key principle of ethical data visualization is:", ["Making data look dramatic", "Hiding unfavorable results", "*Presenting data honestly without distortion", "Using only pie charts"],
         "Ethical visualization avoids manipulation and presents data accurately."),
        ("Which is an example of modern visualization misuse?", ["*Cherry-picking a favorable time window in a line chart", "Using a bar chart for categorical data", "Labeling axes clearly", "Starting the y-axis at zero"],
         "Showing only a favorable time period while hiding the broader trend is misleading."),
        ("A well-designed graph should have:", ["No labels", "*Clear title, labeled axes, appropriate scale, and a legend if needed", "As many fonts as possible", "Only one color"],
         "Clarity, labeled axes, proper scale, and a legend (when necessary) are essential."),
        ("Minard's graphic included data on:", ["Only army size", "Only temperature", "*Army size, geographic location, direction of movement, and temperature", "Only location"],
         "The map combined six variables into a single powerful visualization."),
        ("The purpose of data visualization is to:", ["*Communicate patterns, trends, and insights clearly", "Replace all statistical analysis", "Eliminate the need for data", "Confuse the audience"],
         "Visualization enables efficient communication of data insights."),
        ("A misleading graph is most likely when:", ["Axes are clearly labeled", "The scale starts at zero", "*The scale is manipulated or key context is omitted", "Multiple variables are shown"],
         "Manipulation of scale or omission of context creates misleading impressions."),
        ("What made Snow's method innovative?", ["He used computers", "*He used geographic mapping of data to identify a pattern", "He ignoring the data", "He only used pie charts"],
         "Mapping individual cases geographically was innovative and revealed a spatial pattern."),
        ("'Let the data speak' means:", ["Add opinions to the chart", "Distort the graph to tell a story", "*Present data clearly and let the patterns be self-evident", "Only use words, not graphs"],
         "Good visualization presents data honestly so patterns are apparent without manipulation."),
        ("Which of these is a polar area chart?", ["A scatterplot", "A boxplot", "*Nightingale's Rose Diagram", "A stem-and-leaf plot"],
         "Nightingale's Rose Diagram is the most famous example of a polar area chart."),
        ("If a news graphic shows a 2% change looking like a 200% change, the most likely cause is:", ["Accurate labeling", "*A truncated or zoomed-in y-axis", "Too much data", "Correct scaling"],
         "A truncated y-axis exaggerates small differences."),
        ("Interactive data dashboards are a modern form of:", ["*Data visualization", "Data entry", "Statistical testing", "Random sampling"],
         "Modern dashboards use interactive visualizations to explore data."),
        ("A well-known rule: 'Above all else, show the data' was coined by:", ["Florence Nightingale", "John Snow", "*Edward Tufte", "Napoleon"],
         "Edward Tufte, a pioneer in data visualization, famously advocated for clarity and integrity."),
        ("Context in data visualization includes:", ["Nothing extra", "Only titles", "*Source of data, time period, units, and any relevant background", "Only colors"],
         "Context helps the audience understand what the data represent and how to interpret them."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 2)")
