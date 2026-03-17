#!/usr/bin/env python3
"""Generate real content for Statistics Unit 1: Introduction to Statistics (7 lessons)."""
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

# ── Lesson 1.1: What is Statistics? ──
k, v = build_lesson(1, 1, "What is Statistics?",
    "<h3>What is Statistics?</h3>"
    "<p><b>Statistics</b> is the science of collecting, organizing, analyzing, interpreting, and presenting data. It provides tools to make sense of large amounts of information and to draw conclusions about the world.</p>"
    "<ul><li><b>Descriptive statistics</b> summarize and organize data (e.g., mean, median, charts).</li>"
    "<li><b>Inferential statistics</b> use sample data to make predictions or generalizations about a larger population.</li>"
    "<li><b>Data</b> are facts or observations collected for analysis.</li></ul>"
    "<p>Statistics is used in virtually every field: medicine, business, government, sports, science, and more. Understanding statistics helps you critically evaluate claims and make better decisions.</p>"
    "<p><b>Key terminology:</b> A <b>variable</b> is any characteristic that can be measured or counted. An <b>observation</b> is a single data point. A <b>dataset</b> is a collection of observations.</p>",
    [
        ("Statistics", "The science of collecting, organizing, analyzing, interpreting, and presenting data."),
        ("Descriptive Statistics", "Branch of statistics concerned with summarizing and organizing data using measures like mean, median, and graphs."),
        ("Inferential Statistics", "Branch of statistics that uses sample data to make predictions or generalizations about a larger population."),
        ("Variable", "Any characteristic or quantity that can be measured or counted, such as height, temperature, or test scores."),
        ("Dataset", "A structured collection of data points or observations used for analysis."),
    ],
    [
        ("What is the main purpose of statistics?", ["To memorize formulas", "*To collect, analyze, and interpret data", "To solve algebraic equations", "To study chemical reactions"],
         "Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data."),
        ("Which branch of statistics involves summarizing data with measures like the mean?", ["*Descriptive statistics", "Inferential statistics", "Predictive statistics", "Computational statistics"],
         "Descriptive statistics summarizes and organizes data using measures such as the mean, median, and graphs."),
        ("Inferential statistics is used to:", ["Organize data into tables", "Create graphs", "*Make predictions about a population from a sample", "Calculate exact population values"],
         "Inferential statistics uses sample data to draw conclusions or make predictions about a larger population."),
        ("A variable in statistics is:", ["A fixed number", "A type of graph", "*Any characteristic that can be measured or counted", "A sample size"],
         "A variable is any characteristic or quantity that can be measured or counted."),
        ("Which of the following is an example of a dataset?", ["A single test score", "*A table of 100 students' test scores", "A pencil", "A textbook chapter"],
         "A dataset is a collection of data points or observations, like a table of many students' scores."),
        ("Statistics is commonly applied in which field?", ["Only medicine", "Only business", "Only sports", "*Virtually every field including medicine, business, sports, and science"],
         "Statistics is used in virtually every field for making evidence-based decisions."),
        ("What does an observation represent in statistics?", ["A guess about data", "A statistical formula", "*A single data point collected for analysis", "A branch of mathematics"],
         "An observation is a single data point within a dataset."),
        ("Which of the following best describes descriptive statistics?", ["Making predictions beyond the data", "*Summarizing and describing features of a dataset", "Designing experiments", "Testing hypotheses"],
         "Descriptive statistics focuses on summarizing and describing key features of a dataset."),
        ("A researcher surveys 500 people and uses the results to estimate the opinion of the entire country. This is an example of:", ["Descriptive statistics", "*Inferential statistics", "Data visualization", "Data entry"],
         "Using sample data to generalize about a larger population is inferential statistics."),
        ("Which term refers to a structured collection of observations?", ["Variable", "Statistic", "Parameter", "*Dataset"],
         "A dataset is a structured collection of observations used for analysis."),
        ("Why is understanding statistics important?", ["It guarantees correct predictions", "It replaces scientific experiments", "*It helps critically evaluate claims and make better decisions", "It eliminates uncertainty"],
         "Statistics helps people critically evaluate claims and make evidence-based decisions."),
        ("The number of goals scored in a soccer game is an example of:", ["A parameter", "A constant", "A dataset", "*A variable"],
         "The number of goals can vary from game to game, making it a variable."),
        ("Which best distinguishes inferential from descriptive statistics?", ["Inferential uses graphs; descriptive uses numbers", "*Inferential generalizes beyond the data; descriptive summarizes the data", "They are the same thing", "Descriptive predicts future outcomes"],
         "Inferential statistics goes beyond the data to make generalizations, while descriptive statistics summarizes data."),
        ("A teacher calculates the class average on an exam. This is an example of:", ["Inferential statistics", "*Descriptive statistics", "Probability theory", "Experimental design"],
         "Calculating the class average is summarizing data, which is descriptive statistics."),
        ("What is NOT a goal of statistics?", ["Interpreting data", "Organizing data", "*Guaranteeing outcomes with certainty", "Analyzing data"],
         "Statistics helps analyze and interpret data but cannot guarantee outcomes with absolute certainty."),
        ("An observation in a dataset might be:", ["A formula for the mean", "*A single patient's blood pressure reading", "An entire hospital's records", "A statistical law"],
         "An observation is a single data point, such as one patient's blood pressure reading."),
        ("Which of the following is a quantitative variable?", ["Eye color", "Favorite food", "*Height in centimeters", "Country of birth"],
         "Height in centimeters is a numerical measurement, making it a quantitative variable."),
        ("'The average rainfall in Seattle is 37 inches per year.' This statement uses:", ["Inferential statistics", "*Descriptive statistics", "Probability", "Bayesian analysis"],
         "Reporting an average is summarizing data, a key task of descriptive statistics."),
        ("Which scenario uses inferential statistics?", ["*A poll of 1,000 voters used to predict the election outcome", "A chart showing last month's sales", "A table of students' grades", "A pie chart of favorite colors"],
         "Using a sample (1,000 voters) to predict a larger outcome (election) is inferential statistics."),
        ("The field of statistics helps ensure that conclusions are:", ["Always perfect", "Based on opinions", "*Supported by data and evidence", "Purely theoretical"],
         "Statistics provides tools to draw conclusions that are supported by data and evidence."),
    ]
)
lessons[k] = v

# ── Lesson 1.2: Populations vs. Samples ──
k, v = build_lesson(1, 2, "Populations vs. Samples",
    "<h3>Populations vs. Samples</h3>"
    "<p>In statistics, a <b>population</b> is the entire group of individuals or items that we want to study. A <b>sample</b> is a subset of the population selected for analysis.</p>"
    "<ul><li><b>Population:</b> All members of a defined group (e.g., all high-school students in the U.S.).</li>"
    "<li><b>Sample:</b> A smaller group drawn from the population (e.g., 500 randomly selected high-school students).</li>"
    "<li><b>Parameter:</b> A numerical value describing a characteristic of a population (e.g., the true average height of all students).</li>"
    "<li><b>Statistic:</b> A numerical value describing a characteristic of a sample (e.g., the average height of the 500 selected students).</li></ul>"
    "<p>Since studying an entire population is usually impractical, we use samples and then apply inferential statistics to draw conclusions about the population. The quality of our conclusions depends on how well the sample represents the population.</p>"
    "<p><b>Census</b> – a study that collects data from every member of the population. Censuses are expensive and time-consuming, which is why sampling is preferred in most studies.</p>",
    [
        ("Population", "The entire group of individuals or items of interest in a statistical study."),
        ("Sample", "A subset of the population selected for observation or analysis."),
        ("Parameter", "A numerical measurement describing a characteristic of a population (e.g., population mean μ)."),
        ("Statistic", "A numerical measurement describing a characteristic of a sample (e.g., sample mean x̄)."),
        ("Census", "A study in which data are collected from every member of the population."),
    ],
    [
        ("A population in statistics refers to:", ["A sample of data", "A single data point", "*The entire group of interest", "A statistical formula"],
         "A population is the complete set of individuals or items that we want to study."),
        ("A sample is:", ["The entire group being studied", "*A subset of the population selected for analysis", "A parameter of the population", "A type of graph"],
         "A sample is a smaller group drawn from the population for the purpose of study."),
        ("A parameter describes a characteristic of:", ["A sample", "*A population", "A graph", "An experiment"],
         "A parameter is a numerical value that describes a characteristic of the entire population."),
        ("A statistic describes a characteristic of:", ["*A sample", "A population", "A census", "A textbook"],
         "A statistic is a numerical value computed from sample data."),
        ("Why do researchers typically study samples rather than populations?", ["Samples are always more accurate", "Populations don't exist", "*Studying the entire population is usually impractical or too expensive", "Samples contain more data"],
         "It is usually impractical, costly, or impossible to collect data from every member of a population."),
        ("A census is:", ["A sample survey", "*A study collecting data from every member of the population", "A type of bar graph", "A random selection method"],
         "A census collects data from every individual in the population."),
        ("The average GPA of ALL students at a university is an example of:", ["A statistic", "*A parameter", "A sample", "A variable"],
         "Because it describes the entire population (all students), it is a parameter."),
        ("If you survey 200 out of 5,000 employees about job satisfaction, the 200 employees are:", ["The population", "*The sample", "A parameter", "A census"],
         "The 200 employees selected for the survey are the sample drawn from the population of 5,000."),
        ("The sample mean is denoted by:", ["μ (mu)", "*x̄ (x-bar)", "σ (sigma)", "N"],
         "The sample mean is commonly denoted x̄, while the population mean is denoted μ."),
        ("Which symbol represents the population mean?", ["x̄", "s", "*μ", "n"],
         "μ (mu) is the standard symbol for the population mean."),
        ("A study examines the heights of every student in a school of 800. This is a:", ["Sample survey", "Biased study", "*Census", "Stratified sample"],
         "Since data is collected from every member of the school population, it is a census."),
        ("Which of the following is a key reason samples must be representative?", ["To save paper", "To make data look better", "*So conclusions about the population are valid", "To reduce the number of variables"],
         "A representative sample ensures that inferences drawn about the population are accurate."),
        ("If a researcher measures the blood pressure of 50 patients at a hospital with 2,000 patients, the population is:", ["The 50 patients", "*All 2,000 patients at the hospital", "All hospitals", "The researcher"],
         "The population is the entire group of interest — all 2,000 patients at that hospital."),
        ("Which is true about parameters and statistics?", ["Parameters come from samples", "Statistics describe populations", "*Parameters describe populations; statistics describe samples", "They are the same thing"],
         "Parameters describe population characteristics; statistics describe sample characteristics."),
        ("Why are censuses rare?", ["*They are expensive, time-consuming, and often impractical", "They are less accurate than samples", "They require small groups", "They only work for animals"],
         "Censuses require data from every member of the population, making them expensive and impractical for large populations."),
        ("A marketing firm surveys 1,000 consumers to estimate buying habits of all Americans. The population is:", ["The 1,000 consumers", "The marketing firm", "The survey questions", "*All American consumers"],
         "The population is the larger group about which the firm wants to draw conclusions — all American consumers."),
        ("A statistic is sometimes called a:", ["Constant", "Census", "*Point estimate", "Perfect value"],
         "A sample statistic is often used as a point estimate of the corresponding population parameter."),
        ("Which could lead to a sample that does NOT represent the population well?", ["Random selection", "*Surveying only people at a luxury mall to represent all shoppers", "Using a large sample size", "Stratified sampling"],
         "Surveying only people at a luxury mall introduces bias, making the sample unrepresentative of all shoppers."),
        ("The proportion of defective items in a shipment of 10,000 is a:", ["Statistic", "*Parameter", "Sample", "Variable"],
         "If it refers to the entire shipment (the population), it is a parameter."),
        ("Inferential statistics bridges the gap between:", ["Two samples", "Two graphs", "*A sample and the population", "Two censuses"],
         "Inferential statistics uses sample data to draw conclusions about the larger population."),
    ]
)
lessons[k] = v

# ── Lesson 1.3: Experimental Design & Bias ──
k, v = build_lesson(1, 3, "Experimental Design & Bias",
    "<h3>Experimental Design & Bias</h3>"
    "<p>Good statistical studies require careful <b>experimental design</b> to produce reliable results. A poorly designed study can introduce <b>bias</b>, leading to conclusions that are misleading or wrong.</p>"
    "<ul><li><b>Observational study:</b> Researchers observe subjects without manipulating any variables. Example: tracking diet and health outcomes.</li>"
    "<li><b>Experiment:</b> Researchers deliberately impose a treatment on subjects and measure the response. Example: testing a new drug vs. a placebo.</li>"
    "<li><b>Bias:</b> A systematic error that causes results to deviate from the truth. Common types include selection bias, response bias, and measurement bias.</li>"
    "<li><b>Control group:</b> The group that does not receive the treatment, used for comparison.</li>"
    "<li><b>Placebo:</b> An inactive treatment given to the control group to account for psychological effects.</li>"
    "<li><b>Blinding:</b> Subjects (single-blind) or both subjects and researchers (double-blind) do not know who is in the treatment or control group, reducing bias.</li>"
    "<li><b>Confounding variable:</b> An outside variable that affects both the explanatory and response variables, making it hard to determine cause and effect.</li></ul>"
    "<p>The gold standard in experimental design is the <b>randomized controlled double-blind experiment</b>, which minimizes bias and confounding.</p>",
    [
        ("Observational Study", "A study where researchers observe and collect data without manipulating any variables."),
        ("Experiment", "A study where researchers deliberately apply a treatment and observe its effect on subjects."),
        ("Bias", "A systematic error in a study that causes results to be consistently skewed in one direction."),
        ("Confounding Variable", "An unmeasured variable that influences both the explanatory variable and the response variable, distorting the results."),
        ("Double-Blind Study", "An experiment where neither the subjects nor the researchers know who is in the treatment or control group, minimizing bias."),
    ],
    [
        ("In an experiment, the researcher:", ["Only observes subjects", "*Deliberately imposes a treatment", "Avoids collecting data", "Uses only surveys"],
         "In an experiment, a treatment is deliberately applied to subjects to measure its effect."),
        ("An observational study:", ["Manipulates variables", "*Collects data without imposing treatments", "Always involves a placebo", "Is the same as a census"],
         "In an observational study, researchers observe and record data without manipulating any variables."),
        ("Bias in a study refers to:", ["Random variation", "A large sample size", "*A systematic error that skews results in one direction", "Perfect accuracy"],
         "Bias is a systematic error that consistently pushes results away from the true value."),
        ("A confounding variable:", ["Is always controlled for", "Is the same as the response variable", "*Affects both the explanatory and response variables", "Only appears in observational studies"],
         "A confounding variable influences both the explanatory and response variables, making it difficult to isolate cause and effect."),
        ("What is the purpose of a control group?", ["To introduce bias", "To receive the highest dose", "*To provide a baseline for comparison", "To observe only"],
         "The control group does not receive the treatment and serves as a baseline to compare with the treatment group."),
        ("A placebo is:", ["A real treatment", "*An inactive treatment given to the control group", "A type of bias", "A sampling method"],
         "A placebo is an inactive treatment (like a sugar pill) given to control group subjects."),
        ("In a double-blind study:", ["Only subjects are unaware of group assignments", "Only researchers are unaware", "*Neither subjects nor researchers know group assignments", "Everyone knows the group assignments"],
         "In a double-blind study, both subjects and researchers are kept unaware of who receives the treatment."),
        ("Selection bias occurs when:", ["The sample is perfectly random", "*Certain groups are more likely to be included in the study than others", "The study has too many participants", "The placebo works"],
         "Selection bias means the sample is not representative because some groups are systematically over- or under-represented."),
        ("Which study design is considered the gold standard?", ["Observational study", "Case study", "Survey", "*Randomized controlled double-blind experiment"],
         "The randomized controlled double-blind experiment minimizes bias and confounding."),
        ("Response bias can occur when:", ["Data is collected randomly", "*Participants give inaccurate answers (e.g., due to social pressure)", "The sample is too large", "A census is conducted"],
         "Response bias happens when participants provide inaccurate or dishonest answers."),
        ("An example of a confounding variable: Researchers find ice cream sales and drowning rates both rise in summer. The confound is:", ["Ice cream causes drowning", "Drowning causes ice cream sales", "*Hot weather increases both ice cream sales and swimming (and thus drowning)", "There is no confound"],
         "Hot weather is a confounding variable that drives both ice cream sales and swimming-related drowning."),
        ("Why is randomization important in experiments?", ["It's not important", "It makes the study observational", "*It helps ensure that treatment and control groups are comparable", "It increases bias"],
         "Randomization distributes potential confounders equally across groups, making them comparable."),
        ("Which is NOT a type of bias?", ["Selection bias", "Response bias", "Measurement bias", "*Randomization bias"],
         "Randomization is a tool used to reduce bias, not a type of bias itself."),
        ("A researcher studying a drug knows which patients got the drug and subtly treats them differently. This is an example of:", ["Selection bias", "*Researcher bias (observer bias)", "Placebo effect", "Confounding"],
         "When the researcher's knowledge of group assignments affects their behavior, it's researcher/observer bias."),
        ("The placebo effect is:", ["A proven medical treatment", "*An improvement in patients who believe they are receiving treatment, even though they are not", "A statistical error", "A sampling method"],
         "The placebo effect occurs when subjects experience real changes simply because they believe they are being treated."),
        ("Which of the following is an observational study?", ["*Tracking the eating habits and weight of 1,000 people over 5 years", "Giving half the participants a new diet pill and the other half a placebo", "Assigning students to different study methods", "Testing fertilizer on crops"],
         "Tracking without manipulating variables is observational."),
        ("Blinding helps reduce:", ["Sample size", "The number of variables", "*Bias from subjects' or researchers' expectations", "The cost of the study"],
         "Blinding prevents expectations and knowledge of group assignments from influencing results."),
        ("An experiment without a control group is problematic because:", ["Control groups are expensive", "It makes the sample larger", "*There is no baseline to compare the treatment's effect against", "Control groups add bias"],
         "Without a control group, researchers cannot determine whether the treatment caused the observed effect."),
        ("Which variable does the researcher manipulate in an experiment?", ["Response variable", "Confounding variable", "*Explanatory (independent) variable", "Lurking variable"],
         "The explanatory or independent variable is the one manipulated by the researcher."),
        ("A study finds that people who exercise more tend to be happier. Can we conclude exercise causes happiness?", ["Yes, definitely", "*Not from an observational study alone; confounders may exist", "Only if the sample is large", "Only if a graph is provided"],
         "Observational studies show associations but cannot establish causation due to possible confounding variables."),
    ]
)
lessons[k] = v

# ── Lesson 1.4: Types of Data ──
k, v = build_lesson(1, 4, "Types of Data (qualitative vs. quantitative)",
    "<h3>Types of Data</h3>"
    "<p>Data can be classified into two broad categories based on the nature of the information they represent.</p>"
    "<ul><li><b>Qualitative (categorical) data</b> describe qualities or categories that cannot be measured numerically. Examples: eye color, gender, favorite food, zip code.</li>"
    "<li><b>Quantitative (numerical) data</b> represent measurable quantities expressed as numbers. Examples: height, weight, temperature, income.</li></ul>"
    "<p>Quantitative data are further divided into:</p>"
    "<ul><li><b>Discrete data:</b> Values that can be counted and are typically whole numbers (e.g., number of students in a class, number of cars in a parking lot).</li>"
    "<li><b>Continuous data:</b> Values that can take any number within a range, often involving measurements (e.g., height = 5.7 feet, temperature = 72.3°F).</li></ul>"
    "<p>Correctly classifying data is essential because different types require different statistical methods and visualizations. For instance, bar charts suit categorical data, while histograms suit quantitative data.</p>",
    [
        ("Qualitative Data", "Data that describe qualities or categories, such as color, gender, or brand preference; also called categorical data."),
        ("Quantitative Data", "Data that represent measurable quantities expressed as numbers, such as height, weight, or temperature; also called numerical data."),
        ("Discrete Data", "Quantitative data that can only take specific, countable values, typically whole numbers (e.g., number of pets)."),
        ("Continuous Data", "Quantitative data that can take any value within a range, often the result of measurement (e.g., height, weight)."),
        ("Categorical Variable", "A variable whose values represent groups or categories rather than numerical quantities."),
    ],
    [
        ("Qualitative data are also called:", ["Numerical data", "Discrete data", "*Categorical data", "Continuous data"],
         "Qualitative data describes categories or qualities and is also known as categorical data."),
        ("Which is an example of quantitative data?", ["*A student's height of 5 feet 9 inches", "A student's favorite color", "A student's ethnic background", "A student's zip code"],
         "Height is a measurable numerical value, making it quantitative data."),
        ("Discrete data are best described as:", ["Data from surveys", "*Countable values, usually whole numbers", "Any measured value", "Non-numeric data"],
         "Discrete data take specific, countable values such as the number of students in a room."),
        ("Which is an example of continuous data?", ["Number of siblings", "Number of textbooks", "Shoe size (whole numbers only)", "*Temperature recorded as 72.3°F"],
         "Temperature can take any value within a range, making it continuous data."),
        ("Eye color is an example of:", ["Quantitative data", "Continuous data", "Discrete data", "*Qualitative data"],
         "Eye color describes a category, not a numerical measurement, so it is qualitative."),
        ("The number of cars in a parking lot is:", ["Continuous", "Qualitative", "*Discrete", "Categorical"],
         "The number of cars is countable and takes whole number values, making it discrete."),
        ("Which chart type is most appropriate for categorical data?", ["Histogram", "Scatterplot", "*Bar chart", "Line graph"],
         "Bar charts display frequencies of categories, making them ideal for categorical data."),
        ("Why is classifying data important?", ["It isn't important", "*Different data types require different statistical methods", "All data are treated the same way", "Only for making graphs"],
         "The type of data determines which statistical methods and visualizations are appropriate."),
        ("Weight measured in pounds is:", ["Qualitative", "Discrete", "*Continuous", "Categorical"],
         "Weight can take any value within a range and is measured, making it continuous."),
        ("A survey asks respondents to choose their favorite genre of music. The responses are:", ["*Qualitative (categorical)", "Quantitative (discrete)", "Quantitative (continuous)", "Both qualitative and quantitative"],
         "Music genre is a category, not a number, so responses are qualitative/categorical."),
        ("Zip codes are:", ["Quantitative because they are numbers", "*Qualitative because they represent categories (locations), not meaningful quantities", "Continuous", "Discrete"],
         "Although zip codes are written as numbers, they represent categories (locations) and have no numerical meaning."),
        ("Number of goals scored in a soccer match is:", ["Continuous", "Qualitative", "*Discrete", "Nominal"],
         "Goals are countable whole numbers, making the data discrete."),
        ("A thermometer reading of 98.6°F is:", ["Discrete", "Qualitative", "Nominal", "*Continuous"],
         "Temperature can take any value in a range and is measured, making it continuous data."),
        ("Which of the following is NOT an example of qualitative data?", ["Hair color", "Brand of car", "Type of pet", "*Number of pets"],
         "Number of pets is a count — a quantitative (discrete) value."),
        ("Histograms are most appropriate for:", ["Categorical data", "*Quantitative data", "Ordinal data only", "Qualitative data"],
         "Histograms display the distribution of quantitative data using bins."),
        ("A variable that categorizes data into groups is called:", ["Discrete", "Continuous", "*Categorical", "Statistical"],
         "A categorical variable assigns observations to groups or categories."),
        ("Income measured in dollars is:", ["Qualitative", "*Quantitative (continuous)", "Always discrete", "Categorical"],
         "Income is a measurable numerical value that can take many possible values, making it continuous."),
        ("The key difference between discrete and continuous data is:", ["Discrete is qualitative; continuous is quantitative", "*Discrete data are countable; continuous data can take any value in a range", "There is no difference", "Continuous data are always whole numbers"],
         "Discrete values are countable (often integers), while continuous values can be any number within a range."),
        ("An ID number assigned to each employee is:", ["Quantitative", "*Qualitative (it labels individuals, not a meaningful quantity)", "Continuous", "Discrete"],
         "ID numbers label individuals and do not represent meaningful numerical quantities, so they are qualitative."),
        ("Blood type (A, B, AB, O) is:", ["Quantitative", "Discrete", "*Qualitative", "Continuous"],
         "Blood type represents a category, making it qualitative data."),
    ]
)
lessons[k] = v

# ── Lesson 1.5: Levels of Measurement ──
k, v = build_lesson(1, 5, "Levels of Measurement (nominal, ordinal, interval, ratio)",
    "<h3>Levels of Measurement</h3>"
    "<p>Data can be classified into four levels of measurement, each with increasing mathematical properties.</p>"
    "<ul><li><b>Nominal:</b> Data are labels or names with no inherent order. Examples: eye color, gender, country. You can only check equality (same or different).</li>"
    "<li><b>Ordinal:</b> Data have a meaningful order, but the differences between values are not consistent or meaningful. Examples: letter grades (A, B, C), rankings (1st, 2nd, 3rd), satisfaction ratings (low, medium, high).</li>"
    "<li><b>Interval:</b> Data have a meaningful order and consistent intervals between values, but there is no true zero point. Examples: temperature in °C or °F (0°C ≠ absence of temperature), calendar years.</li>"
    "<li><b>Ratio:</b> Data have a meaningful order, consistent intervals, and a true zero point (zero means the absence of the quantity). Examples: height, weight, age, income, distance.</li></ul>"
    "<p>The level of measurement determines which statistical operations are appropriate. You can compute a mean for interval and ratio data but not meaningfully for nominal or ordinal data.</p>",
    [
        ("Nominal Scale", "The lowest level of measurement where data are categorized by name or label with no inherent order (e.g., eye color, gender)."),
        ("Ordinal Scale", "A level of measurement where data can be ranked or ordered, but the differences between values are not uniform (e.g., letter grades, rankings)."),
        ("Interval Scale", "A level of measurement with ordered data and equal intervals between values, but no true zero point (e.g., temperature in Celsius)."),
        ("Ratio Scale", "The highest level of measurement with ordered data, equal intervals, and a true zero point meaning the absence of the quantity (e.g., weight, height)."),
        ("True Zero", "A zero point that represents the complete absence of the measured quantity, present only in ratio-level data."),
    ],
    [
        ("Which level of measurement has no inherent order?", ["Ordinal", "Interval", "Ratio", "*Nominal"],
         "Nominal data are simply labels or categories with no meaningful order."),
        ("Letter grades (A, B, C, D, F) represent which level of measurement?", ["Nominal", "*Ordinal", "Interval", "Ratio"],
         "Letter grades can be ranked but the differences between grades are not necessarily equal."),
        ("Temperature measured in Fahrenheit is an example of:", ["Nominal", "Ordinal", "*Interval", "Ratio"],
         "Fahrenheit temperature has equal intervals but no true zero (0°F does not mean no temperature)."),
        ("Height in centimeters is measured on which scale?", ["Nominal", "Ordinal", "Interval", "*Ratio"],
         "Height has order, equal intervals, and a true zero (0 cm = no height), making it ratio."),
        ("What distinguishes ratio from interval data?", ["Order", "Equal intervals", "*A true zero point", "The use of numbers"],
         "Ratio data have a true zero point, meaning zero indicates the absence of the quantity."),
        ("Eye color (blue, brown, green) is measured at which level?", ["*Nominal", "Ordinal", "Interval", "Ratio"],
         "Eye color is a category with no inherent ranking, making it nominal."),
        ("Which operations are meaningful for nominal data?", ["Addition and subtraction", "Computing the mean", "*Counting frequencies and checking equality", "All mathematical operations"],
         "For nominal data, you can only count how often each category occurs and check if values are the same or different."),
        ("A marathon finish order (1st, 2nd, 3rd) is:", ["Nominal", "*Ordinal", "Interval", "Ratio"],
         "Rankings have a meaningful order but the time gaps between finishers may not be equal, so it's ordinal."),
        ("Why can't you compute a meaningful average of nominal data?", ["You can", "*The categories have no numerical value or order", "Nominal data are always numbers", "The mean only works for ordinal data"],
         "Nominal data are labels without numerical meaning, so averaging them is nonsensical."),
        ("Calendar year (2020, 2021, 2022) is best classified as:", ["Ratio", "Nominal", "Ordinal", "*Interval"],
         "Calendar years have equal intervals but no true zero (year 0 does not mean absence of time)."),
        ("Which level of measurement allows meaningful ratios (e.g., 'twice as much')?", ["Nominal", "Ordinal", "Interval", "*Ratio"],
         "Only ratio data have a true zero, allowing statements like '10 kg is twice as heavy as 5 kg.'"),
        ("Weight in kilograms has:", ["No order", "Order but unequal intervals", "Equal intervals but no true zero", "*Order, equal intervals, and a true zero"],
         "Weight is ratio-level data with all four properties."),
        ("Satisfaction ratings (very dissatisfied, dissatisfied, neutral, satisfied, very satisfied) are:", ["Nominal", "*Ordinal", "Interval", "Ratio"],
         "These ratings have a meaningful order but the differences between categories may not be equal."),
        ("The key property of interval data that nominal and ordinal lack is:", ["A true zero", "Categories", "Rankings", "*Equal intervals between values"],
         "Interval data have equal, measurable gaps between values."),
        ("A patient's ID number is which level of measurement?", ["*Nominal", "Ordinal", "Interval", "Ratio"],
         "ID numbers are labels identifying patients; they have no order or numerical meaning."),
        ("Temperature in Kelvin (where 0 K = absolute zero) is:", ["Interval", "*Ratio", "Ordinal", "Nominal"],
         "Kelvin has a true zero (absolute zero), making it ratio-level."),
        ("Which statement is correct?", ["*Ratio data can be meaningfully added, subtracted, multiplied, and divided", "Nominal data can be averaged", "Ordinal data always have equal intervals", "Interval data have a true zero"],
         "Ratio data support all arithmetic operations because they have order, equal intervals, and a true zero."),
        ("GPA on a 4.0 scale is typically treated as:", ["Nominal", "Ratio", "*Interval (or ordinal, debate exists)", "It cannot be measured"],
         "GPA has ordered values with roughly equal intervals but no true zero, so it is often treated as interval."),
        ("Ranking movies from best to worst is:", ["*Ordinal", "Nominal", "Interval", "Ratio"],
         "Rankings have a meaningful order but the differences between ranks may not be equal."),
        ("Which level of measurement is the most informative?", ["Nominal", "Ordinal", "Interval", "*Ratio"],
         "Ratio is the highest level — it has all properties: categories, order, equal intervals, and a true zero."),
    ]
)
lessons[k] = v

# ── Lesson 1.6: Random Sampling & Randomization ──
k, v = build_lesson(1, 6, "Random Sampling & Randomization",
    "<h3>Random Sampling & Randomization</h3>"
    "<p><b>Random sampling</b> is a method of selecting participants for a study so that every member of the population has a known, non-zero chance of being selected. This is the foundation of unbiased statistical inference.</p>"
    "<p>Types of random sampling methods:</p>"
    "<ul><li><b>Simple random sample (SRS):</b> Every possible sample of size n has an equal chance of being chosen. Like drawing names from a hat.</li>"
    "<li><b>Systematic sampling:</b> Selecting every k-th individual from a list after a random starting point.</li>"
    "<li><b>Stratified sampling:</b> Dividing the population into groups (strata) and randomly sampling from each stratum.</li>"
    "<li><b>Cluster sampling:</b> Dividing the population into clusters, randomly selecting some clusters, and including all members of those clusters.</li></ul>"
    "<p><b>Randomization</b> in experiments refers to randomly assigning subjects to treatment and control groups. This helps ensure the groups are similar in all respects except the treatment, reducing the impact of confounding variables.</p>"
    "<p>Random sampling gives us a <b>representative sample</b>; randomization in experiments allows us to establish <b>cause and effect</b>.</p>",
    [
        ("Simple Random Sample", "A sample in which every possible group of n individuals from the population has an equal chance of being selected."),
        ("Systematic Sampling", "A sampling method where every k-th individual is selected from a list after a random starting point."),
        ("Stratified Sampling", "A sampling method where the population is divided into subgroups (strata) and random samples are drawn from each stratum."),
        ("Cluster Sampling", "A method where the population is divided into clusters, some clusters are randomly selected, and all members of chosen clusters are included."),
        ("Randomization", "The process of randomly assigning subjects to treatment or control groups in an experiment to reduce confounding."),
    ],
    [
        ("A simple random sample means:", ["Only simple people are selected", "The first people available are chosen", "*Every possible sample of size n has an equal chance of being selected", "Only volunteers participate"],
         "In an SRS, every combination of n individuals from the population has the same probability of selection."),
        ("In systematic sampling, you:", ["Choose people by convenience", "*Select every k-th person from a list after a random start", "Divide the population into strata", "Include everyone in the population"],
         "Systematic sampling selects every k-th individual from a list, starting from a randomly chosen point."),
        ("Stratified sampling involves:", ["Randomly selecting clusters", "*Dividing the population into subgroups and sampling from each", "Choosing every 10th person", "Voluntary response"],
         "In stratified sampling, the population is divided into strata and a random sample is taken from each stratum."),
        ("Cluster sampling involves:", ["Sampling from each stratum", "Selecting every k-th person", "*Randomly selecting some clusters and including all members of chosen clusters", "Using only volunteers"],
         "In cluster sampling, entire clusters are randomly selected, and all individuals within those clusters are studied."),
        ("The main purpose of randomization in experiments is to:", ["Increase sample size", "Make the study observational", "*Ensure treatment and control groups are comparable, reducing confounding", "Eliminate the need for a control group"],
         "Randomization distributes confounding variables equally across groups."),
        ("Which sampling method is MOST likely to produce a representative sample?", ["Convenience sampling", "Voluntary response", "*Simple random sample", "Asking friends"],
         "A simple random sample gives every individual an equal chance, minimizing selection bias."),
        ("A researcher numbers all 10,000 employees and uses a random number generator to select 500. This is:", ["Systematic sampling", "Cluster sampling", "*Simple random sampling", "Stratified sampling"],
         "Using a random number generator to select individuals is a simple random sample."),
        ("Convenience sampling is:", ["A type of random sampling", "*Selecting whoever is easiest to reach, often producing biased results", "The same as systematic sampling", "A perfect method"],
         "Convenience sampling selects participants based on ease of access, which often introduces bias."),
        ("A school divides students by grade level and randomly selects students from each grade. This is:", ["Cluster sampling", "Simple random sampling", "*Stratified sampling", "Systematic sampling"],
         "Dividing by grade (strata) and sampling from each is stratified sampling."),
        ("A health department randomly selects 10 neighborhoods and surveys all households in those neighborhoods. This is:", ["Stratified sampling", "Simple random sampling", "*Cluster sampling", "Systematic sampling"],
         "Neighborhoods are clusters; selecting whole clusters is cluster sampling."),
        ("Why does random sampling matter for inference?", ["It doesn't matter", "It makes the sample smaller", "*It allows us to generalize results from the sample to the population", "It guarantees perfect accuracy"],
         "Random sampling ensures the sample is representative, making population inferences valid."),
        ("Voluntary response sampling tends to:", ["Produce representative samples", "Eliminate bias", "*Over-represent people with strong opinions", "Be the same as SRS"],
         "People who volunteer tend to have strong opinions, making results biased."),
        ("What distinguishes stratified from cluster sampling?", ["They are the same", "*In stratified, you sample from every subgroup; in cluster, you select entire subgroups", "Stratified is simpler", "Cluster sampling requires strata"],
         "Stratified samples from all strata; cluster randomly selects whole clusters."),
        ("A gym selects every 20th member from an alphabetical list starting at a random position. This is:", ["Simple random sampling", "Stratified sampling", "*Systematic sampling", "Cluster sampling"],
         "Selecting every k-th person from a list is systematic sampling."),
        ("Random assignment in an experiment helps establish:", ["Association only", "*Cause and effect", "The sample size", "The number of variables"],
         "Random assignment allows researchers to determine causation, not just correlation."),
        ("Which is NOT a probability sampling method?", ["Simple random sampling", "Stratified sampling", "Systematic sampling", "*Convenience sampling"],
         "Convenience sampling does not give every individual a known chance of selection."),
        ("A potential issue with systematic sampling is:", ["*If the list has a periodic pattern, the sample may be biased", "It requires dividing into strata", "It is too random", "It always requires clustering"],
         "If the list has a hidden pattern matching the sampling interval, the sample may not be representative."),
        ("Under-coverage occurs when:", ["Too many people are sampled", "*Some groups in the population are inadequately represented in the sample", "The sample is too random", "A census is conducted"],
         "Under-coverage means certain groups are left out or under-represented in the sampling frame."),
        ("Randomization helps reduce the effect of:", ["Sample size", "Data collection", "*Confounding variables", "Graphs"],
         "By randomly assigning subjects, confounders are distributed evenly across groups."),
        ("Which best describes why random sampling and randomization are both important?", ["They serve the same purpose", "Only one is needed", "*Random sampling ensures representativeness; randomization in experiments ensures valid causal conclusions", "Neither is necessary with large samples"],
         "Random sampling generalizes to the population; randomization establishes cause and effect."),
    ]
)
lessons[k] = v

# ── Lesson 1.7: Case Studies in Statistical Misuse ──
k, v = build_lesson(1, 7, "Case Studies in Statistical Misuse",
    "<h3>Case Studies in Statistical Misuse</h3>"
    "<p>Statistics can be a powerful tool, but they can also be misused — intentionally or accidentally — to mislead. Understanding common pitfalls helps you become a critical consumer of data.</p>"
    "<ul><li><b>Cherry-picking data:</b> Selecting only data that supports a desired conclusion while ignoring contradictory evidence.</li>"
    "<li><b>Misleading graphs:</b> Manipulating axis scales, using truncated axes, or choosing inappropriate graph types to distort the visual impression of data.</li>"
    "<li><b>Correlation vs. causation:</b> Assuming that because two variables are correlated, one must cause the other. Example: ice cream sales and drowning rates both rise in summer, but ice cream doesn't cause drowning — hot weather drives both.</li>"
    "<li><b>Small or biased samples:</b> Drawing sweeping conclusions from tiny or unrepresentative samples.</li>"
    "<li><b>Loaded questions:</b> Wording survey questions to encourage a particular response.</li>"
    "<li><b>Simpson's Paradox:</b> A trend that appears in several groups of data reverses when the groups are combined.</li></ul>"
    "<p>Always ask: Who collected the data? How was the sample selected? What is the sample size? Are the graphs scaled honestly? Could there be confounding variables?</p>",
    [
        ("Cherry-Picking", "Selectively presenting only data that supports a desired conclusion while hiding contradictory evidence."),
        ("Misleading Graphs", "Graphs that distort the visual impression of data through manipulated scales, truncated axes, or inappropriate chart types."),
        ("Correlation vs. Causation", "The common error of assuming that because two variables are correlated, one must cause the other."),
        ("Loaded Question", "A survey question worded in a way that encourages or guides respondents toward a particular answer."),
        ("Simpson's Paradox", "A phenomenon where a trend that appears in several groups of data reverses or disappears when the groups are combined."),
    ],
    [
        ("Cherry-picking data means:", ["Including all data", "*Selecting only data that supports a desired conclusion", "Randomly sampling data", "Organizing data fairly"],
         "Cherry-picking ignores data that contradicts the desired narrative, presenting only supporting evidence."),
        ("A graph with a y-axis starting at 95 instead of 0 might:", ["Show data more accurately", "*Exaggerate small differences to mislead the viewer", "Be the standard practice", "Reduce bias"],
         "A truncated y-axis magnifies differences, potentially misleading the viewer about the actual magnitude."),
        ("'People who eat breakfast earn more money' implies eating breakfast causes wealth. This is an example of:", ["Valid reasoning", "*Confusing correlation with causation", "A loaded question", "Cherry-picking"],
         "Just because breakfast eating correlates with income doesn't mean one causes the other; confounders exist."),
        ("A loaded question is designed to:", ["Gather unbiased data", "*Influence the respondent toward a particular answer", "Increase sample size", "Eliminate confounding variables"],
         "Loaded questions use biased wording to steer respondents toward a desired response."),
        ("Simpson's Paradox occurs when:", ["Data are always consistent", "*A trend seen in groups reverses when the groups are combined", "Graphs are misleading", "Sample size is too small"],
         "Simpson's Paradox is when aggregate data show a different trend than the individual group data."),
        ("A company claims '90% of dentists recommend our toothpaste.' How might this be misleading?", ["It can't be misleading", "*The sample may be small, biased, or dentists may recommend many brands", "90% is always accurate", "Dentists always agree"],
         "The claim may come from a tiny or biased sample, and dentists may recommend several brands, not exclusively one."),
        ("Which is a critical question to ask about any statistical claim?", ["Is the graph colorful?", "*How was the sample selected and what is the sample size?", "Was the study expensive?", "Did the researcher have a PhD?"],
         "The sample selection method and size are crucial for evaluating the reliability of a claim."),
        ("A news headline states 'Chocolate prevents heart disease' based on one small study. This is problematic because:", ["Chocolate is healthy", "*One small study cannot establish causation or be generalized broadly", "All foods prevent disease", "Headlines are always accurate"],
         "A single small study cannot prove causation, and results may not generalize."),
        ("Using a 3D pie chart that makes one slice look larger than it is demonstrates:", ["Good design", "*Misleading visualization", "Accurate data representation", "Statistical significance"],
         "3D effects in pie charts distort the visual proportions, making some slices appear larger."),
        ("A politician shows only the last 6 months of job growth while ignoring a 2-year decline. This is:", ["Fair reporting", "*Cherry-picking data", "A census", "Random sampling"],
         "Showing only a favorable slice of the data while hiding the broader picture is cherry-picking."),
        ("Correlation between two variables means:", ["One definitely causes the other", "They have nothing in common", "*They tend to change together, but one doesn't necessarily cause the other", "The data are invalid"],
         "Correlation indicates a relationship but does not prove causation."),
        ("A pharmaceutical company funds a study that finds only positive results for its drug. A critical reader should consider:", ["Nothing — the results are fine", "*Potential bias from the funding source", "That all drugs work", "That the study must be a census"],
         "Funding sources can introduce bias; published results may be selectively positive."),
        ("A survey asks: 'Don't you agree that taxes are too high?' This is an example of:", ["A well-designed question", "Random sampling", "*A loaded/leading question", "A statistical parameter"],
         "The phrasing pushes the respondent toward agreeing that taxes are too high."),
        ("To avoid being misled by graphs, you should:", ["Trust all visual representations", "Only look at the title", "*Check the axis scales, labels, and whether the graph type is appropriate", "Ignore graphs entirely"],
         "Checking scales, labels, and chart types helps identify misleading visualizations."),
        ("A study concludes that countries with more TVs per capita have higher life expectancy. A confounding variable might be:", ["TVs improve health", "*Wealthier countries can afford both more TVs and better healthcare", "Life expectancy causes TV sales", "There is no confound"],
         "National wealth is a confounder that drives both TV ownership and healthcare quality."),
        ("An advertisement reports 'our product is 50% more effective!' Without knowing what it's more effective than, this is:", ["Conclusive evidence", "*A potentially misleading claim lacking context", "Always true", "A census result"],
         "Without a clear benchmark, '50% more effective' is meaningless and potentially misleading."),
        ("What is the best defense against statistical misuse?", ["Avoiding all statistics", "Only trusting experts", "*Statistical literacy — understanding methods, biases, and common pitfalls", "Larger font sizes on graphs"],
         "Statistical literacy allows individuals to critically evaluate claims and detect misuse."),
        ("A study with only 15 participants claims a treatment cures a disease. This is problematic because:", ["15 is always enough", "*The sample is too small to draw reliable conclusions", "Small samples are always biased", "The treatment must work"],
         "Very small samples may not be representative and produce unreliable results."),
        ("An example of Simpson's Paradox: Hospital A has a better survival rate for each type of surgery, but Hospital B has a better overall rate. This can happen because:", ["The data are wrong", "*Hospital B may handle easier cases overall, masking Hospital A's advantage on each type", "Statistics are unreliable", "The paradox is impossible"],
         "Simpson's Paradox occurs when the mix of case types differs between groups, reversing the overall trend."),
        ("Which of the following is NOT a form of statistical misuse?", ["Cherry-picking", "Misleading graphs", "Loaded questions", "*Using a large random sample and transparent methods"],
         "Using a large random sample with transparent methods is good statistical practice, not misuse."),
    ]
)
lessons[k] = v

# ── Write unit 1 into the existing file ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

data.update(lessons)

with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {len(lessons)} lessons in statistics_lessons.json (Unit 1)")
