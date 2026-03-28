import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

base = 'content_data/StatisticsLessons/Unit4'

replacements = {
    "Lesson4.1_Quiz.json": {
        15: [
            "An impossible outcome that can never occur in any trial of the experiment",
            "The entire sample space, which includes every single possible outcome at once",
            "A social gathering that has no connection to probability or statistical concepts"
        ],
        17: [
            "Probability that can only be proven in a laboratory setting under controlled conditions",
            "Probability derived from survey data collected from a sample of the population",
            "Probability based on personal belief or subjective assessment of the situation"
        ],
        19: [
            "A probability calculated from a sample space using mathematical formulas and known properties",
            "A probability that equals 50% regardless of the situation or context",
            "A probability that is always correct because it relies on expert knowledge"
        ]
    },
    "Lesson4.2_Quiz.json": {
        14: [
            "The total number of outcomes is always m + n, because events are combined by addition",
            "Counting always starts at zero, so the total outcomes must be adjusted accordingly",
            "Only permutations use multiplication, while combinations always rely on addition"
        ],
        19: [
            "An arrangement of objects in a straight line, following the standard permutation rules",
            "A combination arranged in a circle, where order does not matter among the elements",
            "The same as a standard permutation, with no adjustments needed for circular layout"
        ]
    },
    "Lesson4.3_Quiz.json": {
        13: [
            "Always multiply all probabilities together regardless of whether events are independent or dependent",
            "P(A and B) = P(A) + P(B), which combines probabilities using the addition rule instead",
            "P(A or B) = P(A) x P(B), which confuses the multiplication rule with the addition rule"
        ],
        15: [
            "It makes events dependent because the composition of the pool changes after each draw",
            "Replacement is only used in experiments, not in surveys or observational study designs",
            "It has no effect on independence, since the events are determined by other factors entirely"
        ],
        16: [
            "Without replacement means events are mutually exclusive, so they cannot occur at the same time",
            "It keeps events independent because removing items does not change the overall pool",
            "It only matters for coins and dice, not for other types of probability experiments"
        ],
        20: [
            "P(A) + P(B) - P(A and B), the addition rule used for calculating union probabilities",
            "Always P(A) x P(B) regardless of whether events are independent or dependent",
            "P(A or B) = P(A) x P(B), which confuses the union probability with joint probability"
        ],
        24: [
            "0.10, which is the probability of exactly one success in the sequence",
            "0.0003, which would represent a much rarer event than what is described",
            "0.90, which rounds down and does not account for the full probability calculation"
        ]
    },
    "Lesson4.4_Quiz.json": {
        13: [
            "A table of z-scores used to look up probabilities under the standard normal distribution curve",
            "A table with only two rows, used for comparing binary categories or outcomes in a study",
            "A multiplication table that organizes the products of numbers for quick arithmetic reference"
        ]
    },
    "Lesson4.5_Quiz.json": {
        11: [
            "A table of probabilities listing each possible outcome alongside its calculated likelihood",
            "A picture of a tree with probability labels attached to the trunk and branches decoratively",
            "A bar chart showing probabilities for each outcome as vertical bars of varying heights"
        ],
        12: [
            "A decorative element added to the diagram for visual appeal without conveying any data",
            "The final outcome at the very end of the complete path through the sequential diagram",
            "The root of the tree, which is the initial starting point of the entire probability diagram"
        ],
        13: [
            "The endpoint of all branches, representing the final outcomes of the entire experiment",
            "The root only, which is the single starting point at the very top of the tree diagram",
            "A probability value that is assigned to each branch of the diagram independently"
        ],
        14: [
            "The starting point of the tree, where the first stage of the experiment begins",
            "A branch with probability 0, meaning the event at that branch is impossible to occur",
            "Any intermediate node that connects two stages in the middle of the probability tree"
        ],
        19: [
            "The branches must be rebalanced to ensure each outcome receives equal probability weight",
            "The experiment is invalid because probability trees require equally likely outcomes always",
            "The tree is incorrectly drawn and must be redrawn with equal-length branches throughout"
        ],
        20: [
            "Reversing all branch probabilities so that each path reads from outcome back to root",
            "Deleting the root and starting from endpoints, then working inward toward the center",
            "Drawing the tree upside down with the outcomes at the top and the root at the bottom"
        ]
    },
    "Lesson4.6_Quiz.json": {
        1: [
            "Individual data points collected during a statistical experiment or survey",
            "The mean and median of a quantitative data set computed from observations",
            "Time series data that tracks changes in a variable over successive periods"
        ],
        5: [
            "The sample space, which includes every possible outcome of the experiment",
            "A intersection B, the set of elements belonging to both A and B simultaneously",
            "A union B, the set of elements that belong to either A or B or both sets"
        ],
        11: [
            "A bar chart showing set sizes as vertical bars for easy comparison between groups",
            "A pie chart for probabilities that displays proportions as slices of a whole circle",
            "A scatter plot of two variables showing the relationship between paired data points"
        ],
        13: [
            "The empty set that contains no elements whatsoever from either set",
            "Only the elements in both sets, which is the intersection rather than the union",
            "A labor organization that advocates for the rights and interests of workers"
        ],
        14: [
            "An infinitely large set with no defined boundaries or constraints on its elements",
            "The intersection of all sets, which includes only the elements common to every set",
            "The empty set, which contains no elements and represents an impossible event"
        ],
        17: [
            "A method for drawing Venn diagrams that specifies the correct size and positioning",
            "A rule for computing probabilities using the addition or multiplication principles",
            "A law about sample sizes that determines the minimum number needed for a study"
        ],
        18: [
            "A set that is smaller than another set in terms of the number of elements it contains",
            "A set that never overlaps with B, meaning A and B share no common elements at all",
            "A set below another set in a hierarchical arrangement of data from top to bottom"
        ]
    },
    "Lesson4.7_Quiz.json": {
        11: [
            "The most likely single outcome, which is the value with the highest individual probability",
            "The median outcome, found by ordering all possible results from smallest to largest",
            "The maximum possible outcome, which represents the best result that could ever occur"
        ],
        14: [
            "The payout amount in a gambling game, which determines how much money a player receives",
            "Only numbers that are not even, which is a definition of odd numbers in mathematics",
            "The same as probability, since both describe how likely an event is to occur"
        ],
        15: [
            "Large bets always win because the house edge only applies to small wagers over time",
            "Every individual bet will match the expected value, guaranteeing a predictable result",
            "Casinos only profit from large bettors, while small bettors always break even overall"
        ],
        19: [
            "A physical device in slot machines that spins reels to determine each game outcome",
            "A person who picks random numbers by choosing selections manually without any system",
            "A tool for generating lottery numbers only, and not used in any other gaming context"
        ],
        20: [
            "The number of games played in a session, which tracks the total rounds completed",
            "The house edge of the game, representing the built-in mathematical advantage",
            "A different version of the game that offers alternative rules or payouts to players"
        ]
    },
    "Lesson4.8_Quiz.json": {
        4: [
            "aa (homozygous recessive, showing the recessive trait phenotype)",
            "50% AA and 50% aa (a half-and-half split of homozygous genotypes)",
            "AA (homozygous dominant, showing the dominant trait phenotype)"
        ],
        11: [
            "A type of histogram for genetic data that displays allele frequencies in a population",
            "A statistical test for genetics that evaluates whether observed ratios match expected",
            "A square-shaped gene that determines the physical structure of traits in organisms"
        ],
        16: [
            "A protein produced by a gene that performs a specific function in the cell",
            "An entire genome, which is the complete set of all genetic material",
            "A complete chromosome carrying many genes from one end to the other"
        ],
        19: [
            "A blending of two traits resulting in an intermediate phenotype between both parents",
            "Neither allele is expressed in the heterozygous individual, producing no visible trait",
            "One allele dominates the other completely, masking the recessive allele expression"
        ],
        20: [
            "A method for drawing Punnett squares to predict genotype ratios in genetic crosses",
            "A law requiring genetic testing for all populations to monitor public health outcomes",
            "A formula for calculating mutation rates in a population across successive generations"
        ],
        21: [
            "100%, because both parents carry the recessive allele and all offspring will be affected",
            "50%, because half of the offspring inherit the recessive allele from each parent",
            "0% because neither parent is affected, so they cannot pass on the recessive condition"
        ],
        24: [
            "Only O, because the parental genotypes can only produce homozygous recessive offspring",
            "Only AB, because one parent contributes A and the other contributes B exclusively",
            "Only A or B, because the offspring must inherit one allele from each parent only"
        ],
        25: [
            "1/256, which represents the probability of all four children having the recessive trait",
            "3/4, which is the probability that a single offspring shows the dominant phenotype",
            "1/4, which is the probability for one child only, not for three out of four children"
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

print('Done with Unit 4')
