#!/usr/bin/env python3
"""Generate real content for Statistics Unit 6: Sampling & Experimental Design (7 lessons)."""
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

# ── 6.1 Sampling Methods ──
k, v = build_lesson(6, 1, "Sampling Methods (systematic, stratified, cluster)",
    "<h3>Sampling Methods</h3>"
    "<p>Good sampling is essential for valid statistical inference. Different methods suit different situations.</p>"
    "<ul><li><b>Simple Random Sample (SRS):</b> Every individual has an equal chance of selection. Use a random number generator or table.</li>"
    "<li><b>Systematic sampling:</b> Select every k-th item from a list after a random start. Easy to implement but can be biased if the list has a periodic pattern.</li>"
    "<li><b>Stratified sampling:</b> Divide the population into homogeneous <b>strata</b> (e.g., age groups), then take an SRS from each stratum. Ensures representation of key subgroups.</li>"
    "<li><b>Cluster sampling:</b> Divide the population into <b>clusters</b> (e.g., schools, neighborhoods), randomly select some clusters, and sample ALL individuals in chosen clusters. Cost-effective for geographically spread populations.</li>"
    "<li><b>Convenience sampling:</b> Selecting whoever is easiest to reach — prone to bias; not recommended for formal studies.</li>"
    "<li><b>Multi-stage sampling:</b> Combines methods (e.g., cluster then SRS within clusters).</li></ul>",
    [
        ("Simple Random Sample (SRS)", "A sample where every individual in the population has an equal probability of being selected."),
        ("Stratified Sampling", "Dividing the population into homogeneous strata and taking an SRS from each to ensure subgroup representation."),
        ("Cluster Sampling", "Dividing the population into clusters, randomly selecting some clusters, and sampling all individuals within chosen clusters."),
        ("Systematic Sampling", "Selecting every k-th individual from a list after a random starting point."),
        ("Convenience Sampling", "Selecting individuals who are easiest to reach; highly prone to bias."),
    ],
    [
        ("In an SRS, every individual has:", ["*An equal chance of being selected", "A guaranteed spot", "No chance of selection", "A probability of 0"],
         "SRS gives each individual the same probability of selection."),
        ("Stratified sampling divides the population into:", ["Clusters", "*Strata (homogeneous groups)", "Random groups", "Paired samples"],
         "Strata are subgroups with similar characteristics."),
        ("In cluster sampling, you:", ["Sample one person per group", "Divide into similar groups", "*Randomly select whole clusters and sample everyone in them", "Select the first available person"],
         "Entire clusters are selected and all members are included."),
        ("Systematic sampling selects:", ["Random individuals", "*Every k-th individual from a list", "The first n individuals", "Only outliers"],
         "A fixed interval k is used after a random start."),
        ("Convenience sampling is problematic because:", ["It's expensive", "It's random", "*It introduces selection bias", "It requires stratification"],
         "Convenience samples over-represent easily accessible individuals."),
        ("Which method ensures representation of key subgroups?", ["SRS", "*Stratified sampling", "Convenience sampling", "Cluster sampling"],
         "Stratified sampling guarantees inclusion from each subgroup."),
        ("Cluster sampling is most cost-effective when:", ["The population is small", "*The population is geographically spread out", "Every individual is easy to reach", "The population is homogeneous"],
         "Clusters reduce travel and administrative costs for spread-out populations."),
        ("A researcher numbers all students and uses a random number generator. This is:", ["Stratified", "Systematic", "*Simple random sampling (SRS)", "Convenience"],
         "Random selection of individuals from the whole population = SRS."),
        ("Selecting every 10th person on a list is:", ["Cluster", "Stratified", "*Systematic", "SRS"],
         "Fixed interval = systematic sampling."),
        ("Multi-stage sampling:", ["Uses only one method", "Is the same as SRS", "*Combines multiple sampling methods in stages", "Is always biased"],
         "Multi-stage uses different methods at each stage (e.g., cluster then SRS)."),
        ("Surveying all students in 5 randomly chosen schools is:", ["SRS", "Stratified", "*Cluster sampling", "Convenience"],
         "Schools are the clusters; all students in selected schools are surveyed."),
        ("Stratified sampling produces more precise estimates when:", ["Strata are very different internally", "*Individuals within strata are similar (low within-stratum variability)", "Strata are randomly formed", "Only one stratum is used"],
         "Stratification works best when strata are internally homogeneous."),
        ("The main risk of systematic sampling is:", ["High cost", "Low sample size", "*Bias if the list has a periodic pattern matching the interval", "It requires stratification"],
         "If the list has a cycle matching k, bias can result."),
        ("A voluntary response sample is:", ["An SRS", "*A sample where people choose to participate, often producing biased results", "A stratified sample", "Always representative"],
         "Voluntary responses over-represent strong opinions."),
        ("Random digit dialing is a form of:", ["Stratified sampling", "Cluster sampling", "*Approximate SRS of households", "Convenience sampling"],
         "Random phone numbers approximate an SRS of phone-owning households."),
        ("To study income by region, a researcher takes SRS from each region. This is:", ["Cluster", "*Stratified (regions are strata)", "Systematic", "Convenience"],
         "Each region is a stratum, and an SRS is drawn from each."),
        ("The sampling frame is:", ["The sample itself", "*The list of all individuals from which the sample is drawn", "The population parameter", "The margin of error"],
         "A sampling frame should ideally include every member of the population."),
        ("Undercoverage occurs when:", ["Everyone is surveyed", "The sample is too large", "*Some members of the population are not represented in the sampling frame", "Too many strata are used"],
         "Undercoverage leaves out part of the population."),
        ("Which is NOT a probability sampling method?", ["SRS", "Stratified", "Cluster", "*Convenience"],
         "Convenience sampling doesn't use random selection — not a probability method."),
        ("The goal of good sampling is to:", ["Include everyone", "Be cheap", "*Obtain a representative sample to generalize to the population", "Avoid calculations"],
         "A representative sample leads to valid generalizations."),
    ]
)
lessons[k] = v

# ── 6.2 Bias in Sampling ──
k, v = build_lesson(6, 2, "Bias in Sampling",
    "<h3>Bias in Sampling</h3>"
    "<p><b>Bias</b> is a systematic error that causes sample results to consistently differ from the true population value.</p>"
    "<ul><li><b>Selection bias:</b> Certain groups are systematically excluded from the sample (e.g., undercoverage, convenience sampling).</li>"
    "<li><b>Response bias:</b> Respondents give inaccurate answers due to question wording, social desirability, or misunderstanding.</li>"
    "<li><b>Nonresponse bias:</b> People who don't respond may differ systematically from those who do.</li>"
    "<li><b>Voluntary response bias:</b> Only strongly opinionated people choose to participate.</li>"
    "<li><b>Leading questions:</b> Questions worded to push respondents toward a particular answer.</li>"
    "<li><b>Measurement bias:</b> Faulty instruments or procedures consistently produce inaccurate measurements.</li></ul>"
    "<p>Bias cannot be eliminated by increasing sample size — only by improving methodology.</p>",
    [
        ("Bias", "A systematic error that causes sample results to deviate from the true population value in a consistent direction."),
        ("Selection Bias", "Systematic exclusion of certain population groups from the sample, making the sample unrepresentative."),
        ("Nonresponse Bias", "Occurs when individuals who don't respond differ systematically from those who do, skewing results."),
        ("Response Bias", "Inaccurate answers caused by question wording, social desirability, or interviewer influence."),
        ("Voluntary Response Bias", "Bias from only strongly opinionated individuals choosing to participate in a survey."),
    ],
    [
        ("Bias is a:", ["Random error", "*Systematic error", "Rare event", "Calculation mistake"],
         "Bias is systematic — it consistently pushes results in one direction."),
        ("Increasing sample size eliminates bias:", ["True", "*False — only improved methodology reduces bias", "Only for large n", "Only for small n"],
         "A larger biased sample is still biased. Better methods are needed."),
        ("Selection bias occurs when:", ["Everyone is included", "*Some groups are systematically excluded", "The sample is too large", "Questions are confusing"],
         "Systematic exclusion = selection bias."),
        ("A survey only receives responses from people who feel strongly. This is:", ["Selection bias", "*Voluntary response bias", "Measurement bias", "Random error"],
         "Voluntary response means only extreme opinions are captured."),
        ("Nonresponse bias happens when:", ["Everyone responds", "Questions are neutral", "*Those who don't respond differ from those who do", "The sample is random"],
         "Nonrespondents may have different characteristics than respondents."),
        ("'Don't you agree that taxes are too high?' is an example of:", ["A neutral question", "*A leading question (response bias)", "A factual question", "A cluster"],
         "The wording pushes toward agreement — a leading question."),
        ("Measurement bias is caused by:", ["Random variation", "Small sample size", "*Faulty instruments or inconsistent procedures", "Perfect methodology"],
         "Systematic measurement errors produce biased results."),
        ("Social desirability bias means:", ["People answer honestly", "*People give answers they think are socially acceptable rather than truthful", "The survey is too popular", "Everyone wants to participate"],
         "Respondents may over-report positive behaviors and under-report negative ones."),
        ("A phone survey excludes people without phones. This is:", ["Nonresponse bias", "*Undercoverage (selection bias)", "Response bias", "Voluntary response"],
         "People without phones are systematically excluded from the sampling frame."),
        ("The wording of questions can cause:", ["Selection bias", "*Response bias", "Cluster bias", "Sampling error"],
         "Ambiguous or leading questions distort responses."),
        ("An online poll about a political issue attracts mostly supporters. This is:", ["Random sampling", "*Voluntary response bias", "Stratified sampling", "Measurement bias"],
         "Only motivated supporters are likely to respond."),
        ("To reduce nonresponse bias, researchers can:", ["Ignore nonrespondents", "Use a smaller sample", "*Follow up with nonrespondents and compare respondents to the population", "Only survey friends"],
         "Following up encourages responses and helps check for bias."),
        ("Interviewer bias occurs when:", ["The interviewer is absent", "*The interviewer's behavior or characteristics influence responses", "Responses are anonymous", "The sample is random"],
         "An interviewer's tone, appearance, or phrasing can affect answers."),
        ("Pilot testing a survey helps detect:", ["Sampling errors only", "*Confusing questions and potential response bias", "Nonresponse bias only", "Random errors"],
         "Testing the survey on a small group identifies problems before full deployment."),
        ("Random sampling helps reduce:", ["Response bias", "Measurement bias", "*Selection bias", "All bias types"],
         "Random sampling gives everyone a chance, reducing selection bias."),
        ("A survey at a gym about exercise habits would likely produce:", ["Unbiased results", "*Biased results (selection bias — gym-goers are not representative of all adults)", "Perfectly random data", "Cluster results"],
         "Gym-goers exercise more than the general population — selection bias."),
        ("Bias in one direction means the estimate is consistently:", ["*Too high or too low (but not both randomly)", "Perfectly accurate", "Random", "Variable"],
         "Systematic bias pushes estimates consistently in one direction."),
        ("Anonymous surveys help reduce:", ["Selection bias", "Sampling error", "*Response bias (especially social desirability)", "Cluster bias"],
         "Anonymity encourages honest answers."),
        ("The best defense against bias is:", ["Large sample sizes", "Expensive equipment", "*Careful study design and methodology", "Using only one sampling method"],
         "Thoughtful design is the primary weapon against bias."),
        ("Survivorship bias is:", ["Focusing on nonrespondents", "*Focusing only on those who survived a process, ignoring those who didn't", "A random error", "A calculation error"],
         "Survivorship bias ignores failures, leading to overly optimistic conclusions."),
    ]
)
lessons[k] = v

# ── 6.3 Designing Surveys & Experiments ──
k, v = build_lesson(6, 3, "Designing Surveys & Experiments",
    "<h3>Designing Surveys & Experiments</h3>"
    "<p>Proper study design determines whether conclusions are valid.</p>"
    "<ul><li><b>Observational study:</b> Researchers observe and measure without intervening. Can identify associations but NOT causation.</li>"
    "<li><b>Experiment:</b> Researchers actively impose treatments on subjects. Can establish <b>cause and effect</b> when properly designed.</li>"
    "<li><b>Key elements of an experiment:</b><ul>"
    "<li><b>Treatment:</b> The condition applied to experimental units.</li>"
    "<li><b>Control group:</b> Receives no treatment or a placebo for comparison.</li>"
    "<li><b>Random assignment:</b> Subjects are randomly assigned to treatment/control groups to balance confounding variables.</li>"
    "<li><b>Replication:</b> Using enough subjects for reliable results.</li>"
    "<li><b>Blinding:</b> Single-blind (subject doesn't know), double-blind (neither subject nor researcher knows).</li></ul></li>"
    "<li><b>Confounding variable:</b> A variable that influences both the explanatory and response variables, making it hard to determine the true cause.</li></ul>",
    [
        ("Observational Study", "A study where researchers observe subjects without imposing treatments; can show association but not causation."),
        ("Experiment", "A study where treatments are imposed on subjects; properly designed experiments can establish causation."),
        ("Confounding Variable", "A variable related to both the explanatory and response variables that can distort the apparent relationship."),
        ("Random Assignment", "Randomly assigning subjects to treatment groups to balance confounding variables."),
        ("Double-Blind Experiment", "Neither the subjects nor the researchers measuring outcomes know which group receives the treatment."),
    ],
    [
        ("An observational study:", ["Imposes treatments", "*Observes without intervention", "Always establishes causation", "Uses blinding"],
         "Observational studies collect data without manipulating variables."),
        ("Only experiments can establish:", ["Association", "Correlation", "*Cause and effect", "Observational results"],
         "Random assignment and treatment control allow causal conclusions."),
        ("A confounding variable:", ["*Affects both the explanatory and response variables", "Is always controlled", "Only exists in experiments", "Improves accuracy"],
         "Confounders distort the apparent relationship between variables."),
        ("Random assignment is used to:", ["Select the sample from the population", "*Balance confounding variables across treatment groups", "Increase sample size", "Eliminate all bias"],
         "Random assignment distributes confounders equally between groups."),
        ("In a double-blind experiment:", ["Only the subject is blind", "Only the researcher is blind", "*Neither subject nor researcher knows group assignments", "Everyone knows"],
         "Double-blind prevents both subject and researcher bias."),
        ("A placebo is:", ["An effective drug", "*An inactive treatment given to the control group", "A measurement tool", "A type of bias"],
         "Placebos allow comparison by mimicking the treatment experience without the active ingredient."),
        ("The placebo effect is:", ["A measurement error", "*An improvement caused by the subject's belief they're receiving treatment", "A type of sampling", "A confounding variable only"],
         "Believing one is being treated can produce real improvements."),
        ("Random sampling selects from the population; random assignment:", ["Does the same thing", "*Assigns subjects to treatment groups", "Is not needed", "Selects clusters"],
         "Random assignment divides the sample into treatment and control groups."),
        ("Replication in experiments means:", ["Repeating the entire study", "*Using enough subjects for reliable results", "Copying data", "Having one subject"],
         "More subjects increase the reliability and power of results."),
        ("A study finds that coffee drinkers live longer. Without random assignment, we:", ["Can conclude causation", "*Cannot conclude causation (confounders may exist)", "Should ignore the result", "Need a larger sample only"],
         "Without an experiment, lifestyle confounders may explain the association."),
        ("Lurking variables are:", ["Always measured", "*Unmeasured variables that may affect the results", "The treatment variable", "Only in experiments"],
         "Lurking variables are confounders that weren't measured or controlled."),
        ("In a matched-pairs design:", ["Two groups are compared", "*Each subject serves as their own control or is paired with a similar subject", "Clusters are used", "No control group exists"],
         "Matching ensures pairs are similar on key characteristics."),
        ("A randomized block design:", ["*Groups similar subjects into blocks, then randomly assigns treatments within blocks", "Ignores blocking factors", "Uses no randomization", "Is the same as cluster sampling"],
         "Blocking reduces variability by grouping similar subjects."),
        ("The response variable in an experiment:", ["Is imposed by the researcher", "Is a confounding variable", "*Is the outcome being measured", "Is the treatment"],
         "The response variable is what's measured to see the effect."),
        ("The explanatory variable is:", ["The outcome", "*The variable believed to cause or explain changes in the response", "The lurking variable", "The sample size"],
         "The explanatory variable (treatment) is what the researcher manipulates."),
        ("In a clinical trial, the treatment group receives:", ["*The drug or intervention being tested", "A placebo", "No treatment", "Both drug and placebo"],
         "The treatment group gets the active intervention."),
        ("Single-blind means:", ["*The subject doesn't know which group they're in", "The researcher doesn't know", "Everyone knows", "Nobody knows"],
         "In single-blind, subjects are kept unaware of their group assignment."),
        ("Why is blinding important?", ["It reduces cost", "*It prevents bias from expectations (subject or researcher)", "It increases sample size", "It eliminates confounders"],
         "Blinding prevents expectations from influencing the results."),
        ("An experiment with no control group:", ["Is perfectly valid", "*Cannot determine whether the treatment caused the observed effect", "Is better than a controlled one", "Is always biased"],
         "Without a control group, there's no baseline for comparison."),
        ("Informed consent in experiments means:", ["Subjects are told nothing", "*Subjects understand and agree to participate, knowing the study details and risks", "Only researchers are informed", "Consent is optional"],
         "Ethical research requires informed, voluntary participation."),
    ]
)
lessons[k] = v

# ── 6.4 Randomization & Control Groups ──
k, v = build_lesson(6, 4, "Randomization & Control Groups",
    "<h3>Randomization & Control Groups</h3>"
    "<p>Randomization and control groups are the twin pillars of good experimental design.</p>"
    "<ul><li><b>Randomization:</b> Assigning subjects to groups using a random process ensures that differences between groups are due to chance, not systematic factors.</li>"
    "<li><b>Why randomize?</b> Balances both known and unknown confounding variables across groups. Without randomization, groups may differ in ways that affect the outcome.</li>"
    "<li><b>Control group:</b> The group that does NOT receive the treatment, providing a baseline for comparison. May receive a placebo or standard treatment.</li>"
    "<li><b>Types of control:</b><ul>"
    "<li>Placebo control: receives an inactive look-alike treatment.</li>"
    "<li>Active control: receives the current standard treatment (common in medical trials).</li>"
    "<li>No-treatment control: receives nothing (when ethically appropriate).</li></ul></li>"
    "<li><b>Statistical significance</b> compares the observed effect to what could be expected by random chance alone.</li></ul>",
    [
        ("Randomization", "Using a random process to assign subjects to treatment groups, balancing confounders across groups."),
        ("Control Group", "The comparison group that does not receive the experimental treatment."),
        ("Placebo Control", "A control group that receives an inactive treatment designed to look like the real treatment."),
        ("Active Control", "A control group that receives the current standard treatment for comparison to the new treatment."),
        ("Statistical Significance", "Evidence that the observed effect is unlikely to be due to random chance alone."),
    ],
    [
        ("Randomization helps control:", ["Only known confounders", "Only unknown confounders", "*Both known and unknown confounders", "Nothing"],
         "Random assignment distributes all confounders (known and unknown) across groups."),
        ("Without a control group, you cannot:", ["Collect data", "Treat subjects", "*Determine if the treatment caused the observed effect", "Use randomization"],
         "The control group provides the baseline for comparison."),
        ("A placebo control receives:", ["The real treatment", "*An inactive substance that looks like the treatment", "No contact at all", "The standard treatment"],
         "Placebos mimic the treatment without the active ingredient."),
        ("An active control group receives:", ["Nothing", "A placebo", "*The current standard treatment", "A double dose"],
         "Active controls compare new treatments to existing ones."),
        ("Random assignment is different from random sampling because:", ["They're the same", "*Random sampling selects participants; random assignment divides them into groups", "Random assignment selects participants", "Neither uses randomness"],
         "Sampling = who is studied; assignment = who gets which treatment."),
        ("If treatment and control groups differ significantly, and randomization was used:", ["It's definitely a coincidence", "*The treatment likely caused the difference", "The study is flawed", "More data is always needed"],
         "Randomization justifies causal conclusions when differences are significant."),
        ("Why might a researcher use an active control instead of a placebo?", ["To save money", "To avoid randomization", "*When withholding effective treatment would be unethical", "To increase sample size"],
         "Ethical concerns may require giving all participants some form of treatment."),
        ("Randomization ensures that groups are:", ["Identical", "*Similar on average (balanced across confounders)", "Different in known ways", "Different in all ways"],
         "Groups will be approximately equal due to random distribution of characteristics."),
        ("A study without randomization is:", ["Always worthless", "Always valid", "*An observational study (cannot establish causation)", "Randomly controlled"],
         "Without random assignment, confounders may explain observed differences."),
        ("The purpose of a control group is:", ["To increase costs", "To add subjects", "*To provide a baseline for measuring the treatment effect", "To eliminate blinding"],
         "Controls show what happens without the treatment."),
        ("Statistical significance means:", ["The result is practically important", "*The result is unlikely due to chance alone", "The sample is large", "There is no error"],
         "Significance indicates the effect exceeds what chance alone would produce."),
        ("In a completely randomized design:", ["*All subjects are randomly assigned to one of the treatment groups", "Subjects choose their group", "No randomization occurs", "Only the control is random"],
         "Every subject has an equal chance of being in any group."),
        ("A coin flip or random number generator can be used for:", ["Stratification", "*Random assignment to groups", "Calculating p-values", "Measuring outcomes"],
         "Random devices ensure unbiased group assignment."),
        ("If groups are not balanced, the results may be:", ["More accurate", "*Confounded by the imbalance", "Perfectly valid", "Unaffected"],
         "Imbalanced groups make it hard to attribute effects to the treatment."),
        ("Block randomization:", ["*Ensures equal group sizes by randomizing within blocks", "Uses no randomization", "Creates biased groups", "Is the same as cluster sampling"],
         "Blocking by group size ensures treatment groups remain balanced."),
        ("Ethical concerns with control groups include:", ["*Withholding potentially beneficial treatment", "Making groups too similar", "Using too many subjects", "Random assignment itself"],
         "Denying treatment to a control group raises ethical issues, especially for serious conditions."),
        ("The term 'controlled experiment' means:", ["The researcher controls everything", "*There is a control group for comparison", "The experiment is outdoors", "No randomization is used"],
         "A controlled experiment has a comparison group."),
        ("An experiment with 3 treatments and a control has:", ["1 group", "3 groups", "*4 groups", "6 groups"],
         "3 treatment groups + 1 control group = 4 groups."),
        ("If a new drug is compared to both a placebo and the standard drug:", ["There are 2 groups", "*There are 3 groups (new drug, standard drug, placebo)", "It's observational", "Blinding is impossible"],
         "Three groups: new treatment, active control, placebo control."),
        ("The gold standard for establishing causation is:", ["An observational study", "A case study", "A voluntary survey", "*A randomized controlled experiment (RCT)"],
         "RCTs with random assignment and control groups are the gold standard."),
    ]
)
lessons[k] = v

# ── 6.5 Simulation Models ──
k, v = build_lesson(6, 5, "Simulation Models",
    "<h3>Simulation Models</h3>"
    "<p><b>Simulation</b> uses random number generation to model real-world processes and estimate probabilities or outcomes that are difficult to compute analytically.</p>"
    "<ul><li><b>Steps:</b> (1) Define the model and assumptions. (2) Generate random outcomes using a random number generator. (3) Repeat many times (trials). (4) Analyze the distribution of results.</li>"
    "<li><b>Monte Carlo simulation:</b> A general method using repeated random sampling. Named after casino randomness.</li>"
    "<li><b>Applications:</b> Estimating probabilities, modeling financial risk, testing statistical methods, understanding complex systems.</li>"
    "<li><b>Law of Large Numbers:</b> As the number of simulation trials increases, the estimated probability approaches the true probability.</li>"
    "<li><b>Random number tables and generators:</b> Sources of random digits used to simulate chance processes.</li></ul>"
    "<p>Simulations provide approximate answers when exact calculation is impractical.</p>",
    [
        ("Simulation", "Using random sampling to model a real-world process and estimate outcomes or probabilities."),
        ("Monte Carlo Method", "A simulation technique using repeated random sampling to approximate solutions to complex problems."),
        ("Random Number Generator", "A tool producing equally likely digits or values used to simulate random processes."),
        ("Trial (in simulation)", "One complete run of the simulated process, producing one outcome."),
        ("Law of Large Numbers (in simulation)", "As the number of trials increases, the simulation estimate converges to the true value."),
    ],
    [
        ("A simulation uses:", ["Exact formulas only", "*Random number generation to model a process", "No randomness", "Only theoretical calculations"],
         "Simulations rely on random sampling to approximate real outcomes."),
        ("The Monte Carlo method is named after:", ["A mountain", "A scientist", "*The famous casino (symbolizing randomness)", "A city in Italy"],
         "Monte Carlo, Monaco is known for its casinos — randomness."),
        ("The first step in a simulation is:", ["Collecting real data", "Running trials", "*Defining the model and assumptions", "Analyzing results"],
         "You must specify the model before generating random outcomes."),
        ("As the number of simulation trials increases:", ["Results become less accurate", "Results stay the same", "*Estimates converge to the true value", "Randomness increases"],
         "The law of large numbers ensures convergence with many trials."),
        ("A simulation with 10,000 trials is generally:", ["Less accurate than 100 trials", "*More accurate than 100 trials", "Exactly as accurate as 100 trials", "Always perfectly accurate"],
         "More trials reduce the variability of the estimate."),
        ("To simulate a coin flip, use:", ["Only a real coin", "*A random number generator (e.g., 0 = tails, 1 = heads)", "A formula", "A z-table"],
         "Random digits can simulate any chance process."),
        ("Monte Carlo simulation is used in:", ["Only gambling", "*Finance, engineering, science, and many other fields", "Only physics", "Only statistics courses"],
         "Monte Carlo methods have wide-ranging applications."),
        ("In a simulation to estimate P(at least one 6 in 4 dice rolls):", ["Roll dice once", "*Simulate 4 rolls thousands of times and count the proportion with at least one 6", "Use only the formula", "Roll real dice"],
         "Repeat the random process many times and track the results."),
        ("A random number table gives digits that are:", ["*Equally likely and independent", "In a pattern", "Always increasing", "Biased toward 5"],
         "Each digit (0-9) is equally likely and independent of others."),
        ("Simulation provides:", ["*Approximate answers based on random sampling", "Exact theoretical answers", "No useful information", "Answers only for discrete problems"],
         "Simulations provide approximations that improve with more trials."),
        ("To simulate drawing a card from a deck:", ["*Assign numbers 1-52 and use a random number generator", "Always use real cards", "Use a z-table", "Use a binomial formula"],
         "Map random numbers to the 52 cards."),
        ("The variability of simulation results decreases with:", ["Fewer trials", "*More trials", "Larger population", "Smaller population"],
         "More trials reduce the standard error of the estimate."),
        ("A simulation model can test:", ["Only proven theories", "Nothing useful", "*'What if' scenarios before implementing real changes", "Only historical data"],
         "Simulations allow exploration of scenarios without real-world costs."),
        ("Simulation is especially useful when:", ["The exact formula is simple", "Only 2 outcomes are possible", "*The analytical solution is too complex or doesn't exist", "The sample is small"],
         "Simulations handle complexity that formulas can't easily address."),
        ("To ensure reproducibility of a simulation:", ["Change random seeds each time", "*Use the same random seed", "Use fewer trials", "Avoid documentation"],
         "Setting the same seed produces the same random sequence."),
        ("Financial risk models often use:", ["Only mean values", "No simulation", "*Monte Carlo simulation to model uncertainty", "Only historical returns"],
         "Monte Carlo models thousands of possible market scenarios."),
        ("One trial in a simulation produces:", ["All possible outcomes", "*One outcome of the modeled process", "The average", "The exact probability"],
         "Each trial generates one result; many trials build the distribution."),
        ("A simulation to estimate π:", ["Cannot be done", "*Can randomly generate points in a square and check if they fall inside an inscribed circle", "Requires calculus only", "Uses dice"],
         "The ratio of points inside the circle to total points approximates π/4."),
        ("The main limitation of simulation is:", ["It uses randomness", "It requires computers", "*Results are approximate, not exact", "It cannot model complex systems"],
         "Simulations give approximations that improve with more trials but aren't exact."),
        ("Simulation can validate:", ["Nothing", "Only simple formulas", "*Statistical methods and theoretical results", "Only experimental data"],
         "Simulations can check whether theoretical methods work as expected."),
    ]
)
lessons[k] = v

# ── 6.6 Case Studies in Political Polling ──
k, v = build_lesson(6, 6, "Case Studies in Political Polling",
    "<h3>Case Studies in Political Polling</h3>"
    "<p>Political polling is one of the most visible applications of sampling and statistics.</p>"
    "<ul><li><b>1936 Literary Digest poll:</b> Surveyed 2.4 million people by mail but predicted the wrong winner. Cause: selection bias (wealthy readers, voluntary response) despite huge sample size.</li>"
    "<li><b>George Gallup</b> correctly predicted the winner with just 50,000 responses using better sampling methods — proving that methodology matters more than size.</li>"
    "<li><b>Margin of error:</b> Polls report results like '52% ± 3%' — the margin of error reflects sampling variability.</li>"
    "<li><b>Likely voter models:</b> Pollsters screen for people likely to actually vote, not just all adults.</li>"
    "<li><b>Response rates</b> have declined significantly (from >35% to <6% for phone polls), raising concerns about nonresponse bias.</li>"
    "<li><b>2016 election polls:</b> Underestimated support for certain candidates, partly due to late-deciding voters and difficulty reaching certain demographics.</li></ul>",
    [
        ("Literary Digest Poll (1936)", "A famous polling failure that surveyed 2.4 million people but predicted wrong due to selection bias and voluntary response."),
        ("Margin of Error", "The range within which the true population value likely falls; reflects sampling variability, typically ± a few percent."),
        ("Likely Voter Model", "A screening method to identify respondents who are actually expected to vote, improving poll accuracy."),
        ("Nonresponse Bias in Polling", "Systematic error from people who refuse to participate, whose opinions may differ from respondents."),
        ("Polling Aggregation", "Combining results from multiple polls to produce a more stable and accurate estimate."),
    ],
    [
        ("The 1936 Literary Digest poll failed because:", ["The sample was too small", "*Selection bias (wealthy, voluntary respondents) despite 2.4 million responses", "The margin of error was wrong", "Gallup interfered"],
         "A huge sample doesn't help if it's systematically biased."),
        ("Gallup succeeded in 1936 with:", ["More respondents", "*Better sampling methodology with only 50,000 responses", "More money", "A larger margin of error"],
         "Sound methodology beats sheer sample size."),
        ("A margin of error of ±3% for a 52% result means:", ["*The true value is likely between 49% and 55%", "Exactly 52%", "Between 50% and 52%", "The poll is wrong"],
         "52% ± 3% gives a range of 49% to 55%."),
        ("Likely voter models are important because:", ["All adults vote", "Voting is mandatory", "*Not everyone who is surveyed will actually vote", "Polls only call voters"],
         "Screening for likely voters makes predictions more accurate."),
        ("Declining response rates in phone polls increase the risk of:", ["Larger samples", "Perfect accuracy", "*Nonresponse bias", "Cost savings"],
         "Low response rates mean the sample may not represent the population."),
        ("The lesson of the 1936 poll is:", ["*Methodology matters more than sample size", "Larger samples always win", "Mail surveys are always wrong", "Polling doesn't work"],
         "A biased sample stays biased regardless of size."),
        ("Modern polling challenges include:", ["Too many respondents", "*Low response rates, reaching certain demographics, and late-deciding voters", "Excessive funding", "Too few polls"],
         "Multiple factors make modern polling difficult."),
        ("Poll aggregation works by:", ["Using only the newest poll", "*Combining multiple polls to reduce variability", "Ignoring outliers", "Using the largest poll only"],
         "Averaging many polls produces a more stable estimate."),
        ("A push poll is:", ["A legitimate survey", "A random sample", "*A disguised campaign tactic using biased questions to influence opinions rather than measure them", "A cluster sample"],
         "Push polls aim to influence, not measure."),
        ("Exit polls survey:", ["*Voters as they leave polling places", "Random households", "All registered voters", "Only politicians"],
         "Exit polls collect data from people who just voted."),
        ("The 2016 US election polls:", ["Were perfectly accurate", "*Underestimated certain candidates partly due to late deciders and hard-to-reach voters", "Used too small samples", "Didn't use margins of error"],
         "Several factors contributed to polling errors in 2016."),
        ("Weighting in polls adjusts for:", ["*Demographic imbalances in the sample compared to the population", "Financial costs", "Question length", "The number of polls"],
         "Weighting corrects when certain groups are over- or under-represented."),
        ("A tracking poll:", ["Is conducted once", "*Repeatedly surveys over time to detect changes in opinion", "Only uses one question", "Has no margin of error"],
         "Tracking polls follow trends by polling at regular intervals."),
        ("Cell-phone-only households created problems for early phone polls because:", ["Cell phones didn't exist", "*Traditional methods only called landlines, missing younger demographics", "Cell phone users don't vote", "It increased costs"],
         "Cell-phone-only households were excluded from landline polls."),
        ("Oversampling a subgroup is done to:", ["Bias the results", "*Get enough responses from a small group for analysis, then weight back", "Ignore other groups", "Reduce costs"],
         "Oversampling ensures adequate representation of small subgroups."),
        ("A confidence level of 95% with a ±3% margin means:", ["The poll is 95% correct", "3% of people lied", "*In 95% of similar polls, the true value falls within the margin", "5% of voters were excluded"],
         "Confidence level measures how often the method produces intervals containing the truth."),
        ("Online polls tend to suffer from:", ["Too much randomization", "*Self-selection (voluntary response) bias", "Too many respondents", "Perfect representation"],
         "Online polls attract only those motivated to participate."),
        ("The sample size needed for a national poll with ±3% margin is approximately:", ["100", "500", "*About 1,000–1,500", "1 million"],
         "Surprisingly, about 1,000-1,500 respondents achieve a ±3% margin nationally."),
        ("Polling is most accurate when:", ["Sample size is huge but biased", "*Sampling methodology is sound and response rates are high", "Only one poll is conducted", "Questions are leading"],
         "Good methodology and adequate participation produce the best results."),
        ("Voter enthusiasm can affect polls by:", ["Having no effect", "*Biasing who chooses to respond, as enthusiastic supporters are more likely to participate", "Making margins larger", "Reducing the sample size"],
         "Differential enthusiasm affects which views are captured."),
    ]
)
lessons[k] = v

# ── 6.7 Ethics in Data Collection ──
k, v = build_lesson(6, 7, "Ethics in Data Collection",
    "<h3>Ethics in Data Collection</h3>"
    "<p>Ethical considerations are fundamental to conducting responsible statistical research.</p>"
    "<ul><li><b>Informed consent:</b> Participants must understand the study's purpose, procedures, risks, and benefits before voluntarily agreeing to participate.</li>"
    "<li><b>Privacy and confidentiality:</b> Personal data must be protected. Researchers should anonymize data when possible.</li>"
    "<li><b>Institutional Review Board (IRB):</b> A committee that reviews research involving human subjects to ensure ethical standards are met.</li>"
    "<li><b>Do no harm:</b> Research should minimize physical and psychological risks to participants.</li>"
    "<li><b>Data integrity:</b> Researchers must report data honestly — fabrication, falsification, and selective reporting are serious ethical violations.</li>"
    "<li><b>Historical violations:</b> The Tuskegee Syphilis Study (1932–1972) denied treatment to Black men without consent — a landmark case leading to modern ethical guidelines.</li>"
    "<li><b>Vulnerable populations:</b> Children, prisoners, and others with limited autonomy require extra protections.</li></ul>",
    [
        ("Informed Consent", "A participant's voluntary agreement to participate after being fully informed about the study, its procedures, risks, and benefits."),
        ("Institutional Review Board (IRB)", "A committee that reviews and approves research involving human subjects to ensure ethical standards."),
        ("Confidentiality", "Protecting participants' personal information and ensuring their data cannot be traced back to them."),
        ("Data Integrity", "Honest and accurate reporting of data; fabrication, falsification, and selective reporting are ethical violations."),
        ("Tuskegee Syphilis Study", "A 1932–1972 study that denied treatment to Black men without consent, leading to modern ethical review requirements."),
    ],
    [
        ("Informed consent requires:", ["Participants know nothing", "*Participants understand the study's purpose, risks, and procedures before agreeing", "Only the researcher's consent", "No explanation"],
         "Full disclosure enables voluntary, informed participation."),
        ("An IRB:", ["Conducts research itself", "*Reviews and approves research to ensure ethical standards are met", "Publishes results", "Selects samples"],
         "IRBs protect human subjects by reviewing study designs."),
        ("Confidentiality means:", ["Sharing data publicly with names", "*Protecting participants' identities and personal information", "Hiding the results", "Not collecting data"],
         "Researchers must safeguard personal information."),
        ("The Tuskegee Syphilis Study is an example of:", ["Ethical research", "*A severe ethical violation that led to modern guidelines", "Proper informed consent", "Good study design"],
         "The study denied treatment without consent for decades."),
        ("Data fabrication is:", ["Acceptable in emergencies", "*A serious ethical violation — inventing data that was never collected", "Common practice", "The same as rounding"],
         "Fabricating data is scientific fraud."),
        ("Anonymizing data means:", ["Collecting names", "*Removing identifying information so participants cannot be traced", "Publishing personal details", "Using pseudonyms only"],
         "Anonymization protects participant privacy."),
        ("Vulnerable populations include:", ["Only adults", "Only researchers", "*Children, prisoners, and others with limited autonomy", "No one"],
         "Extra protections are required for those who cannot fully advocate for themselves."),
        ("Participants can withdraw from a study:", ["Never", "Only with permission", "*At any time without penalty", "Only before it starts"],
         "Voluntary participation includes the right to withdraw at any time."),
        ("Selective reporting (cherry-picking data) is:", ["Good practice", "Required", "*An ethical violation that misrepresents findings", "The same as analysis"],
         "Reporting only favorable results distorts the true findings."),
        ("Deception in research:", ["Is always acceptable", "Is never used", "*May be used in limited cases with IRB approval and debriefing", "Requires no review"],
         "Deception must be justified, reviewed, and followed by debriefing."),
        ("Researchers should minimize:", ["Data collection", "Sample size", "*Physical and psychological harm to participants", "Published results"],
         "The principle of beneficence requires minimizing risks."),
        ("IRB review is required:", ["Never", "Only for medical research", "*Before research involving human subjects begins", "After the study is published"],
         "IRB approval must be obtained before data collection starts."),
        ("P-hacking (trying many analyses until finding significance) is:", ["Good statistics", "*An ethical and methodological problem that inflates false positives", "Required by IRBs", "Always acceptable"],
         "P-hacking distorts results by exploiting random noise."),
        ("Data should be stored:", ["Publicly with names", "Without any security", "*Securely with restricted access to protect confidentiality", "On social media"],
         "Secure storage protects participant data."),
        ("The Belmont Report established:", ["Statistical formulas", "*Ethical principles for research with human subjects (respect, beneficence, justice)", "Sampling methods", "Control chart standards"],
         "The Belmont Report (1979) laid out fundamental ethical principles."),
        ("Justice in research ethics means:", ["*Benefits and risks are distributed fairly across groups", "Only studying wealthy populations", "Excluding minorities", "Always using placebos"],
         "No group should bear a disproportionate share of risks or be excluded from benefits."),
        ("Debriefing participants means:", ["Asking them to leave", "Hiding the purpose", "*Explaining the true nature and purpose of the study after participation", "Paying them more"],
         "Debriefing ensures participants understand what the study was truly about."),
        ("A conflict of interest in research:", ["Doesn't exist", "Improves objectivity", "*Can bias results and must be disclosed", "Is always criminal"],
         "Financial or personal interests should be transparently disclosed."),
        ("Reproducibility requires researchers to:", ["Keep methods secret", "*Share methods and data so others can verify results", "Never publish", "Destroy raw data"],
         "Open methods and data enable independent verification."),
        ("Ethical research ultimately:", ["Slows progress", "Is unnecessary", "*Protects participants and enhances the credibility of science", "Only applies to medicine"],
         "Ethics protect people and maintain public trust in science."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 6)")
