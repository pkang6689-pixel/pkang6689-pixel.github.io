import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = 'content_data/StatisticsLessons/Unit5'

replacements = {
    "Lesson5.1_Quiz.json": {
        3: [
            "3 (the most common value in the distribution)",
            "4 (the largest single outcome possible)",
            "6 (the sum of all face values on the die)"
        ]
    },
    "Lesson5.2_Quiz.json": {
        10: [
            "Both 1, since a continuous variable always has full probability at each point",
            "Both 0, because continuous random variables assign zero to every possible value",
            "Different, because continuous and discrete functions behave differently at points"
        ],
        13: [
            "It measures the number of observations within each interval of continuous data",
            "It is the same as the CDF value at that particular point in the distribution",
            "It is the exact probability at a point, read directly from the curve height"
        ]
    },
    "Lesson5.3_Quiz.json": {
        14: [
            "The binomial is always normal, regardless of sample size or probability values",
            "It only applies when p = 0.5, so the distribution is perfectly symmetric",
            "The binomial is replaced by the Poisson distribution when n becomes large"
        ]
    },
    "Lesson5.4_Quiz.json": {
        9: [
            "Shift left or right along the horizontal axis depending on sigma",
            "Symmetric only, without any change in width or height of the curve",
            "Taller only, increasing the peak height without affecting the spread"
        ],
        12: [
            "The raw data value itself, before any transformation or standardization is applied",
            "The sample size used in the study, denoted by n in statistical formulas",
            "The probability of a value occurring in the normal distribution curve"
        ],
        18: [
            "A table of sample sizes needed for various statistical tests and power levels",
            "A table of frequencies showing how often each value occurs in a data set",
            "A table of raw data values organized by magnitude for easy lookup"
        ]
    },
    "Lesson5.5_Quiz.json": {
        9: [
            "4, because the variance doubles along with the sample size increasing",
            "1/2, because doubling the sample size halves the standard deviation",
            "2, because the standard deviation scales linearly with sample size"
        ],
        11: [
            "A rule that eliminates sampling error from all statistical estimates",
            "A theorem that says all populations are naturally normally distributed",
            "A theorem that only applies to symmetric populations and not skewed ones"
        ],
        12: [
            "The distribution of a single sample that has been collected from a population",
            "A histogram of raw data from the original population observations",
            "The distribution of the population from which samples are drawn"
        ],
        13: [
            "The standard deviation of the population, which measures the overall spread",
            "The range of the data, which is the difference between maximum and minimum",
            "The error in the measurement device used to collect the observations"
        ],
        18: [
            "The population spread decreases as sample size grows larger over time",
            "Fewer samples can be taken from a larger population overall",
            "The sample mean always equals mu regardless of sample size"
        ],
        20: [
            "The population shape does not matter even for n = 1 because the CLT applies universally",
            "The population must be normal for the sampling distribution to be normal as well",
            "Only symmetric populations qualify for the Central Limit Theorem to take effect"
        ]
    },
    "Lesson5.6_Quiz.json": {
        3: [
            "n (the number of independent trials in the experiment)",
            "np (the product of sample size and success probability)",
            "p (the probability of success on each individual trial)"
        ],
        4: [
            "3 (the value of the mean parameter itself, not the probability)",
            "0 (because zero events is impossible when the mean is positive)",
            "1 (since the probability of exactly zero events must equal one)"
        ],
        6: [
            "Narrower, with values concentrating in a smaller range around the center",
            "More skewed toward the right, with an increasingly long tail to the right",
            "Uniform, with all outcomes becoming equally likely as lambda increases"
        ],
        7: [
            "P(X = 1), which gives only the probability of exactly one event occurring",
            "e^(-2), which is the probability of observing exactly zero events in the interval",
            "2, which is the value of the mean parameter and not a probability at all"
        ],
        12: [
            "The number of trials conducted in the experiment or sampling process",
            "The probability that an event occurs on any single given trial",
            "The maximum number of events possible within the given time interval"
        ],
        13: [
            "Pi (3.14159), the ratio of a circle's circumference to its diameter in geometry",
            "An error term that accounts for variability in statistical estimation models",
            "The expected value of the distribution, also known as the mean parameter"
        ],
        15: [
            "Only 0 and 1, since the Poisson distribution is a binary outcome model",
            "Any real number, including fractions and negative values on the number line",
            "Only positive integers starting from 1, because zero events is not possible"
        ]
    },
    "Lesson5.7_Quiz.json": {
        6: [
            "The median of the sampled measurements over time",
            "The process mean of the individual observations",
            "The range of values within each sample group"
        ],
        13: [
            "Someone is physically controlling the machine at all times during production",
            "The process never changes under any circumstances or conditions whatsoever",
            "The process produces zero defects and every item meets all specifications"
        ],
        14: [
            "Testing every single item in a shipment before any of them are released",
            "Only inspecting items that look defective based on a visual examination",
            "Accepting all items without inspection and relying on the supplier guarantee"
        ],
        15: [
            "The cost per defect, which quantifies the financial impact of each nonconforming unit produced",
            "The average defect rate, computed by dividing total defects by total items inspected over time",
            "The sample size needed for control charts, determined by the desired level of statistical precision"
        ],
        16: [
            "It eliminates all variation from the manufacturing process entirely and permanently",
            "It is not used in quality control because it applies only to academic statistics",
            "It increases production speed by reducing the time needed for quality inspections"
        ],
        20: [
            "Only healthcare settings, where patient safety requires rigorous monitoring",
            "Only manufacturing plants, where physical products must meet exact tolerances",
            "Only food production facilities, where safety regulations mandate inspections"
        ],
        23: [
            "0 to 0.50, a very wide interval that would accept almost any defect rate",
            "0.04 +/- 0.04 = 0 to 0.08, using the proportion itself as the margin of error",
            "0.04 +/- 3 x 0.04 = -0.08 to 0.16, using the proportion instead of the standard error"
        ]
    },
    "Lesson5.8_Quiz.json": {
        8: [
            "Skewed, with a long tail extending in one direction away from center",
            "Poisson, where events occur independently at a constant average rate",
            "Uniform, with all values equally likely across the entire range"
        ],
        10: [
            "Assuming normal distribution without checking whether it fits the data",
            "Ignoring the data entirely and selecting a model based on convenience",
            "Using the largest model with the most parameters to capture every detail"
        ],
        15: [
            "Always picking the normal distribution since it is the most commonly used model",
            "Choosing between mean and median as the best summary measure for the data",
            "Selecting the largest sample size to ensure the most precise estimates"
        ],
        28: [
            "Binomial with p = 0.5, since wait times can be modeled as success/failure outcomes",
            "Uniform on [0, 16] minutes, assuming each wait time value is equally likely to occur",
            "Normal, since there are many data points and the central limit theorem applies here"
        ]
    }
}

for fname, qfixes in replacements.items():
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data['quiz_questions']:
        qnum = q['question_number']
        if qnum not in qfixes:
            continue
        new_wrongs = qfixes[qnum]
        wrong_idx = 0
        for opt in q['options']:
            if not opt['is_correct']:
                if wrong_idx < len(new_wrongs):
                    opt['text'] = new_wrongs[wrong_idx]
                    wrong_idx += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f'Fixed {fname}: {list(qfixes.keys())}')

print('Done with Unit 5')
