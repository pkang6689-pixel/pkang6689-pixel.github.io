#!/usr/bin/env python3
"""Generate real content for Statistics Unit 4: Probability Foundations (8 lessons)."""
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

# ── 4.1 Basic Probability Rules ──
k, v = build_lesson(4, 1, "Basic Probability Rules",
    "<h3>Basic Probability Rules</h3>"
    "<p><b>Probability</b> measures the likelihood of an event occurring, expressed as a number from 0 (impossible) to 1 (certain).</p>"
    "<ul><li><b>Sample space (S):</b> The set of all possible outcomes.</li>"
    "<li><b>Event (E):</b> A subset of the sample space.</li>"
    "<li><b>P(E) = Number of favorable outcomes / Total number of outcomes</b> (for equally likely outcomes).</li>"
    "<li><b>Complement rule:</b> P(E') = 1 − P(E). The probability of an event NOT happening.</li>"
    "<li><b>Addition rule (mutually exclusive):</b> P(A or B) = P(A) + P(B) when A and B cannot both occur.</li>"
    "<li><b>General addition rule:</b> P(A or B) = P(A) + P(B) − P(A and B).</li>"
    "<li><b>Multiplication rule (independent):</b> P(A and B) = P(A) × P(B) when events are independent.</li></ul>"
    "<p>Probabilities can be expressed as fractions, decimals, or percentages. The sum of probabilities of all outcomes in a sample space is 1.</p>",
    [
        ("Sample Space", "The set of all possible outcomes of a random experiment (denoted S)."),
        ("Probability", "A number between 0 and 1 measuring the likelihood of an event, where 0 = impossible and 1 = certain."),
        ("Complement Rule", "P(E') = 1 − P(E); the probability of the event NOT occurring."),
        ("Addition Rule", "P(A or B) = P(A) + P(B) − P(A and B); for mutually exclusive events, P(A and B) = 0."),
        ("Multiplication Rule (Independent Events)", "P(A and B) = P(A) × P(B) when events A and B do not affect each other."),
    ],
    [
        ("Probability ranges from:", ["−1 to 1", "*0 to 1", "0 to 100", "1 to 10"],
         "Probability is always between 0 (impossible) and 1 (certain)."),
        ("The sample space for flipping a coin is:", ["*{Heads, Tails}", "{Heads}", "{1, 2, 3, 4, 5, 6}", "{True, False, Maybe}"],
         "The two possible outcomes are Heads and Tails."),
        ("P(rolling a 3 on a fair die) = ?", ["1/3", "*1/6", "3/6", "1/2"],
         "There is one favorable outcome (3) out of six equally likely outcomes."),
        ("P(E') if P(E) = 0.7 is:", ["0.7", "*0.3", "1.7", "0"],
         "P(E') = 1 − 0.7 = 0.3."),
        ("Two events are mutually exclusive when:", ["They always occur together", "*They cannot both occur at the same time", "Their probabilities add to 0.5", "They are independent"],
         "Mutually exclusive events have no overlap — P(A and B) = 0."),
        ("Using the general addition rule: P(A) = 0.4, P(B) = 0.3, P(A and B) = 0.1. P(A or B) = ?", ["0.7", "*0.6", "0.1", "0.8"],
         "P(A or B) = 0.4 + 0.3 − 0.1 = 0.6."),
        ("If A and B are mutually exclusive, P(A or B) = ?", ["P(A) × P(B)", "*P(A) + P(B)", "P(A) − P(B)", "0"],
         "For mutually exclusive events, P(A or B) = P(A) + P(B) since P(A and B) = 0."),
        ("P(flipping two heads in a row with a fair coin) = ?", ["1/2", "*1/4", "1/3", "1/8"],
         "P(H and H) = 1/2 × 1/2 = 1/4 (independent events)."),
        ("The sum of probabilities of all outcomes in a sample space equals:", ["0", "0.5", "*1", "Depends on the experiment"],
         "All possible outcomes must sum to 1."),
        ("An event with P = 0 is:", ["Certain", "Likely", "Unlikely", "*Impossible"],
         "P = 0 means the event cannot occur."),
        ("An event with P = 1 is:", ["*Certain", "Impossible", "Unlikely", "Rare"],
         "P = 1 means the event is guaranteed to occur."),
        ("P(drawing a red card from a standard deck) = ?", ["1/4", "*1/2", "13/52", "1/13"],
         "26 red cards out of 52 = 26/52 = 1/2."),
        ("If events A and B are independent, P(A and B) = ?", ["P(A) + P(B)", "P(A) − P(B)", "*P(A) × P(B)", "P(A or B)"],
         "Independence means P(A and B) = P(A) × P(B)."),
        ("P(rolling an even number on a fair die) = ?", ["1/6", "*3/6 = 1/2", "2/6", "4/6"],
         "Even numbers: {2, 4, 6} = 3 out of 6."),
        ("The complement of 'at least one' is:", ["*'None'", "'All'", "'Exactly one'", "'At most one'"],
         "P(at least one) = 1 − P(none)."),
        ("P(not rolling a 6) on a fair die = ?", ["1/6", "6/6", "*5/6", "1/3"],
         "P(not 6) = 1 − 1/6 = 5/6."),
        ("A probability of 0.001 means the event is:", ["Certain", "Likely", "*Very unlikely but possible", "Impossible"],
         "0.001 is very small but not zero, so the event is unlikely but can occur."),
        ("Mutually exclusive events have P(A and B) = ?", ["1", "P(A) + P(B)", "*0", "P(A) × P(B)"],
         "Mutually exclusive events cannot occur simultaneously."),
        ("If a bag has 3 red and 7 blue marbles, P(red) = ?", ["7/10", "*3/10", "3/7", "1/3"],
         "P(red) = 3/10."),
        ("The law of large numbers states that as the number of trials increases:", ["Probabilities become 0", "Results become random", "*The observed relative frequency approaches the theoretical probability", "Nothing changes"],
         "Over many trials, experimental probability converges to theoretical probability."),
    ]
)
lessons[k] = v

# ── 4.2 Counting Principles ──
k, v = build_lesson(4, 2, "Counting Principles (permutations, combinations)",
    "<h3>Counting Principles</h3>"
    "<p>Counting principles determine the number of ways to arrange or select items, which is essential for calculating probabilities.</p>"
    "<ul><li><b>Fundamental Counting Principle:</b> If event A can occur in m ways and event B in n ways, then A followed by B can occur in m × n ways.</li>"
    "<li><b>Permutation:</b> An ordered arrangement of objects. The number of permutations of n objects taken r at a time: P(n, r) = n! / (n − r)!</li>"
    "<li><b>Combination:</b> A selection where order does NOT matter. C(n, r) = n! / [r!(n − r)!]</li>"
    "<li><b>Factorial:</b> n! = n × (n−1) × (n−2) × … × 1. By definition, 0! = 1.</li></ul>"
    "<p><b>Key distinction:</b> Use permutations when order matters (e.g., rankings, codes), combinations when order doesn't matter (e.g., committees, groups).</p>",
    [
        ("Fundamental Counting Principle", "If one event can occur in m ways and a second in n ways, the events together can occur in m × n ways."),
        ("Permutation", "An ordered arrangement of objects; P(n,r) = n!/(n−r)!."),
        ("Combination", "A selection of objects where order does not matter; C(n,r) = n!/[r!(n−r)!]."),
        ("Factorial", "n! = n × (n−1) × … × 1; by definition 0! = 1."),
        ("With vs. Without Replacement", "With replacement: items can be chosen more than once. Without replacement: once chosen, an item is removed."),
    ],
    [
        ("5! = ?", ["25", "120", "60", "*120"],
         "5! = 5 × 4 × 3 × 2 × 1 = 120."),
        ("0! = ?", ["0", "Undefined", "*1", "−1"],
         "By definition, 0! = 1."),
        ("The Fundamental Counting Principle states that if you have 3 shirts and 4 pants, total outfits = ?", ["7", "*12", "3", "4"],
         "3 × 4 = 12 outfits."),
        ("Permutations are used when:", ["Order doesn't matter", "*Order matters", "Repetition is not allowed", "Items are identical"],
         "Permutations count ordered arrangements."),
        ("Combinations are used when:", ["*Order does not matter", "Order matters", "There is only one item", "Items must be ranked"],
         "Combinations count selections regardless of order."),
        ("P(5, 2) = ?", ["10", "*20", "25", "60"],
         "P(5,2) = 5!/(5−2)! = 120/6 = 20."),
        ("C(5, 2) = ?", ["20", "*10", "5", "60"],
         "C(5,2) = 5!/(2!×3!) = 120/(2×6) = 10."),
        ("How many 3-digit codes (using digits 0-9) with repetition allowed?", ["30", "720", "*1000", "100"],
         "10 × 10 × 10 = 1000."),
        ("Choosing a committee of 3 from 8 people uses:", ["Permutations", "*Combinations", "Factorial only", "The addition rule"],
         "A committee has no specific order — use combinations."),
        ("Ranking 1st, 2nd, 3rd place among 8 runners uses:", ["Combinations", "*Permutations", "The addition rule", "0!"],
         "Rankings have a specific order — use permutations."),
        ("C(n, 0) = ?", ["0", "n", "*1", "n!"],
         "C(n,0) = n!/(0!×n!) = 1. There's exactly one way to choose nothing."),
        ("C(n, n) = ?", ["0", "n", "*1", "n!"],
         "C(n,n) = n!/(n!×0!) = 1. There's one way to choose everything."),
        ("How many ways can 4 books be arranged on a shelf?", ["4", "8", "16", "*24"],
         "4! = 24 ways."),
        ("If a pizza offers 3 crust types, 4 sauces, and 5 toppings, total combinations = ?", ["12", "*60", "15", "35"],
         "3 × 4 × 5 = 60 (Fundamental Counting Principle)."),
        ("C(10, 3) = ?", ["30", "720", "*120", "1000"],
         "C(10,3) = 10!/(3!×7!) = 720/6 = 120."),
        ("P(n, 1) = ?", ["1", "0", "*n", "n!"],
         "P(n,1) = n!/(n−1)! = n."),
        ("A lock code has 4 digits and order matters. This is a:", ["Combination", "*Permutation", "Factorial", "Sample space"],
         "Since the order of digits matters (1234 ≠ 4321), it's a permutation."),
        ("With 6 people, how many different 2-person handshakes are possible?", ["12", "36", "*15", "6"],
         "C(6,2) = 6!/(2!×4!) = 15. Order doesn't matter in a handshake."),
        ("The key question to decide between permutation and combination is:", ["How many items are there?", "Is the sample large?", "*Does order matter?", "Are items replaced?"],
         "If order matters → permutation; if not → combination."),
        ("How many ways to arrange the letters in 'CAT'?", ["*6", "3", "9", "27"],
         "3! = 6 arrangements: CAT, CTA, ACT, ATC, TCA, TAC."),
    ]
)
lessons[k] = v

# ── 4.3 Independent & Dependent Events ──
k, v = build_lesson(4, 3, "Independent & Dependent Events",
    "<h3>Independent & Dependent Events</h3>"
    "<p>Understanding whether events are independent or dependent is critical for calculating probabilities correctly.</p>"
    "<ul><li><b>Independent events:</b> The occurrence of one event does NOT affect the probability of the other. Example: Flipping a coin twice — the outcome of the first flip doesn't affect the second.</li>"
    "<li><b>Dependent events:</b> The occurrence of one event DOES affect the probability of the other. Example: Drawing two cards from a deck without replacement — the first draw changes the remaining cards.</li></ul>"
    "<p><b>Test for independence:</b> Events A and B are independent if and only if P(A and B) = P(A) × P(B), or equivalently P(A|B) = P(A).</p>"
    "<p><b>Multiplication rule:</b></p>"
    "<ul><li>Independent: P(A and B) = P(A) × P(B)</li>"
    "<li>Dependent: P(A and B) = P(A) × P(B|A)</li></ul>"
    "<p><b>'With replacement'</b> typically makes events independent; <b>'without replacement'</b> makes them dependent.</p>",
    [
        ("Independent Events", "Two events where the occurrence of one does not affect the probability of the other: P(A and B) = P(A) × P(B)."),
        ("Dependent Events", "Two events where the occurrence of one changes the probability of the other."),
        ("With Replacement", "After an item is selected, it is returned to the pool before the next selection, maintaining independence."),
        ("Without Replacement", "After an item is selected, it is NOT returned, changing probabilities for subsequent selections."),
        ("Multiplication Rule (Dependent)", "P(A and B) = P(A) × P(B|A), where P(B|A) is the probability of B given A has occurred."),
    ],
    [
        ("Two events are independent if:", ["One always causes the other", "*The occurrence of one does not change the probability of the other", "They are mutually exclusive", "They never occur"],
         "Independence means one event's occurrence has no effect on the other's probability."),
        ("Flipping a coin and rolling a die are:", ["Dependent", "*Independent", "Mutually exclusive", "Complementary"],
         "The coin flip has no effect on the die roll — independent events."),
        ("Drawing two cards without replacement makes the draws:", ["Independent", "*Dependent", "Mutually exclusive", "Complementary"],
         "The first card drawn changes the composition of the remaining deck."),
        ("For independent events, P(A and B) = ?", ["P(A) + P(B)", "P(A) − P(B)", "*P(A) × P(B)", "P(A|B)"],
         "The multiplication rule for independent events: P(A and B) = P(A) × P(B)."),
        ("For dependent events, P(A and B) = ?", ["P(A) × P(B)", "*P(A) × P(B|A)", "P(A) + P(B|A)", "P(B) − P(A)"],
         "With dependent events: P(A and B) = P(A) × P(B given A)."),
        ("Drawing with replacement makes events:", ["Dependent", "*Independent", "Impossible", "Certain"],
         "Replacing the item restores the original conditions, maintaining independence."),
        ("P(A) = 0.5, P(B) = 0.3, A and B independent. P(A and B) = ?", ["0.8", "0.2", "*0.15", "0.35"],
         "P(A and B) = 0.5 × 0.3 = 0.15."),
        ("A bag has 5 red and 5 blue. P(2 red without replacement) = ?", ["25/100", "*20/90 = 2/9", "5/10 × 5/10", "1/4"],
         "P(first red) = 5/10; P(second red | first red) = 4/9; product = 20/90 = 2/9."),
        ("Which test confirms independence?", ["P(A) = P(B)", "*P(A and B) = P(A) × P(B)", "P(A or B) = 0", "P(A) + P(B) = 1"],
         "Events are independent if and only if P(A and B) = P(A) × P(B)."),
        ("Mutually exclusive events are:", ["Always independent", "*Never independent (if both have P > 0)", "The same as independent", "Always certain"],
         "If A and B are mutually exclusive, P(A and B) = 0, but P(A)×P(B) > 0, so they're NOT independent."),
        ("Tossing a coin 3 times — each toss is:", ["Dependent on the previous", "*Independent of the others", "Mutually exclusive", "Conditional"],
         "Each coin toss has no influence on any other."),
        ("A deck has 52 cards. P(drawing an ace, then a king, without replacement) = ?", ["(4/52)²", "*4/52 × 4/51", "4/52 × 4/52", "8/52"],
         "P(ace) = 4/52, then P(king|ace drawn) = 4/51."),
        ("'With replacement' means:", ["The item is discarded", "*The item is returned before the next selection", "Only one item is drawn", "Nothing changes"],
         "Returning the item before the next draw maintains the original probabilities."),
        ("If P(A|B) ≠ P(A), then A and B are:", ["*Dependent", "Independent", "Complementary", "Mutually exclusive"],
         "If knowing B changes the probability of A, the events are dependent."),
        ("P(rolling a 6 on a die, three times in a row) = ?", ["3/6", "3 × 1/6", "*(1/6)³ = 1/216", "1/18"],
         "Independent events: (1/6) × (1/6) × (1/6) = 1/216."),
        ("A weather forecast says P(rain Monday) = 0.4 and P(rain Tuesday) = 0.3. If independent, P(rain both days) = ?", ["0.7", "*0.12", "0.1", "0.4"],
         "P(both) = 0.4 × 0.3 = 0.12."),
        ("P(at least one head in two coin flips) can be found using:", ["0.5 × 0.5", "*1 − P(no heads) = 1 − 0.25 = 0.75", "0.5 + 0.5", "0.5"],
         "P(at least one) = 1 − P(none) = 1 − (0.5)² = 0.75."),
        ("Independence means:", ["Events can't happen together", "One event guarantees the other", "*One event's occurrence provides no information about the other", "Both events are certain"],
         "Independent events don't provide information about each other."),
        ("A class has 20 students, 8 wear glasses. Two students are chosen randomly without replacement. P(both wear glasses) = ?", ["(8/20)²", "*8/20 × 7/19", "8/20 + 7/19", "16/40"],
         "Without replacement: P = 8/20 × 7/19 = 56/380 = 14/95."),
        ("If events are independent, P(A|B) = ?", ["P(B)", "P(B|A)", "*P(A)", "0"],
         "If A and B are independent, knowing B doesn't change P(A), so P(A|B) = P(A)."),
    ]
)
lessons[k] = v

# ── 4.4 Conditional Probability ──
k, v = build_lesson(4, 4, "Conditional Probability",
    "<h3>Conditional Probability</h3>"
    "<p><b>Conditional probability</b> is the probability of an event occurring given that another event has already occurred.</p>"
    "<p><b>Formula:</b> P(A|B) = P(A and B) / P(B), where P(B) > 0.</p>"
    "<p>Read 'P(A|B)' as 'the probability of A given B.'</p>"
    "<ul><li>The '|' symbol means 'given that' — it restricts the sample space to only the outcomes where B occurred.</li>"
    "<li>P(A|B) ≠ P(B|A) in general — the order matters.</li>"
    "<li>P(A|B) = P(A) only if A and B are independent.</li></ul>"
    "<p><b>Bayes' Theorem:</b> P(A|B) = P(B|A) × P(A) / P(B). This allows you to reverse conditional probabilities.</p>"
    "<p><b>Example:</b> In a group of 100 students, 30 play sports and 20 of those also play music. P(music | sports) = 20/30 = 2/3.</p>",
    [
        ("Conditional Probability", "The probability of event A occurring given that event B has already occurred: P(A|B) = P(A and B)/P(B)."),
        ("Given That", "A condition that restricts the sample space to only those outcomes where the given event has occurred."),
        ("Bayes' Theorem", "P(A|B) = P(B|A) × P(A) / P(B); used to reverse conditional probabilities."),
        ("P(A|B) vs. P(B|A)", "These are generally NOT equal; the order in conditional probability matters."),
        ("Restricted Sample Space", "In conditional probability, the sample space shrinks to only the outcomes consistent with the given condition."),
    ],
    [
        ("P(A|B) is read as:", ["Probability of A and B", "*Probability of A given B", "Probability of A or B", "Probability of B given A"],
         "The vertical bar '|' means 'given that.'"),
        ("The formula for conditional probability is:", ["P(A|B) = P(A) + P(B)", "*P(A|B) = P(A and B) / P(B)", "P(A|B) = P(A) × P(B)", "P(A|B) = P(B) / P(A)"],
         "P(A|B) = P(A and B) / P(B)."),
        ("In a class, P(A and B) = 0.12, P(B) = 0.4. P(A|B) = ?", ["0.48", "0.52", "*0.3", "0.12"],
         "P(A|B) = 0.12 / 0.4 = 0.3."),
        ("P(A|B) = P(A) only when:", ["Always", "*A and B are independent", "A and B are mutually exclusive", "P(B) = 0"],
         "Independence means the condition doesn't change the probability."),
        ("Is P(A|B) always equal to P(B|A)?", ["Yes, always", "*No, they are generally different", "Only when P(A) = P(B)", "Only for independent events"],
         "Conditional probability is not symmetric; P(A|B) ≠ P(B|A) in general."),
        ("A survey: 60% of students study and 80% of those who study pass. P(study and pass) = ?", ["80%", "60%", "*48%", "14%"],
         "P(study and pass) = P(study) × P(pass|study) = 0.60 × 0.80 = 0.48."),
        ("Bayes' Theorem is used to:", ["Calculate the mean", "*Reverse conditional probabilities", "Find the median", "Compute standard deviation"],
         "Bayes' Theorem lets you find P(A|B) when you know P(B|A), P(A), and P(B)."),
        ("Of 200 adults, 120 exercise regularly. Of those, 90 have healthy BMI. P(healthy BMI | exercises) = ?", ["120/200", "90/200", "*90/120 = 3/4", "120/90"],
         "P(healthy BMI | exercises) = 90/120 = 0.75."),
        ("The '|' in conditional probability restricts:", ["Nothing", "The event", "*The sample space to outcomes where the condition occurred", "The probability to 0"],
         "The condition narrows the sample space to only outcomes where the given event happened."),
        ("If P(rain) = 0.3 and P(umbrella | rain) = 0.9, P(rain and umbrella) = ?", ["0.3", "0.9", "1.2", "*0.27"],
         "P(rain and umbrella) = P(rain) × P(umbrella | rain) = 0.3 × 0.9 = 0.27."),
        ("P(disease|positive test) is an example of:", ["*Conditional probability", "Marginal probability", "Joint probability", "Complementary probability"],
         "It's the probability of disease given that the test result is positive."),
        ("If 5% of a population has a disease and a test is 95% accurate, the probability of having the disease given a positive test:", ["Is 95%", "*Is much lower than 95% due to false positives (requires Bayes' Theorem)", "Is 5%", "Cannot be calculated"],
         "When prevalence is low, false positives dominate and P(disease|positive) can be surprisingly small."),
        ("P(A and B) = P(A) × P(B|A) is called:", ["The addition rule", "*The general multiplication rule", "Bayes' Theorem", "The complement rule"],
         "This is the general multiplication rule for any two events."),
        ("A two-way table can help calculate conditional probability by:", ["Ignoring columns", "*Restricting to a specific row or column and computing the proportion", "Adding all cells", "Using only the total"],
         "A two-way table lets you focus on the row/column representing the given condition."),
        ("P(female | dean's list) = 0.6 means:", ["60% of females are on the dean's list", "*60% of the dean's list students are female", "60% of students are female", "The dean's list is 60% full"],
         "Of those on the dean's list, 60% are female."),
        ("If A and B are mutually exclusive, P(A|B) = ?", ["P(A)", "1", "*0", "P(B)"],
         "If A and B can't both happen, then when B occurs, A definitely doesn't: P(A|B) = 0."),
        ("Bayes' Theorem states P(A|B) = ?", ["P(A) + P(B)", "P(A and B) + P(B)", "*P(B|A) × P(A) / P(B)", "P(A) × P(B)"],
         "Bayes' Theorem: P(A|B) = P(B|A) × P(A) / P(B)."),
        ("A card is drawn from a deck. P(King | Face card) = ?", ["4/52", "12/52", "*4/12 = 1/3", "1/13"],
         "There are 12 face cards (J, Q, K of each suit) and 4 Kings. P = 4/12 = 1/3."),
        ("Confusion between P(A|B) and P(B|A) is called:", ["Bayes' error", "*The prosecutor's fallacy (or confusion of the inverse)", "Selection bias", "Sampling error"],
         "Mistaking P(A|B) for P(B|A) is a common logical error."),
        ("In general, P(A|B) changes the probability of A by:", ["*Restricting consideration to only cases where B occurred", "Doubling P(A)", "Setting P(A) = P(B)", "Ignoring B"],
         "Conditioning on B updates the probability of A based on the new information that B occurred."),
    ]
)
lessons[k] = v

# ── 4.5 Probability Trees ──
k, v = build_lesson(4, 5, "Probability Trees",
    "<h3>Probability Trees</h3>"
    "<p>A <b>probability tree</b> (tree diagram) is a visual tool for organizing and computing probabilities of sequential events.</p>"
    "<ul><li>Each <b>branch</b> represents a possible outcome, labeled with its probability.</li>"
    "<li><b>Branches from the same node</b> must have probabilities that sum to 1.</li>"
    "<li>To find P(a specific sequence): <b>multiply</b> the probabilities along the path.</li>"
    "<li>To find P(an event that can occur via multiple paths): <b>add</b> the probabilities of all paths leading to that event.</li></ul>"
    "<p>Probability trees are especially helpful for:</p>"
    "<ul><li>Multi-stage experiments (e.g., drawing cards, flipping coins, medical testing).</li>"
    "<li>Problems involving conditional probability (branches after the first split may have updated probabilities).</li>"
    "<li>Visualizing all possible outcomes systematically.</li></ul>",
    [
        ("Probability Tree", "A diagram showing all possible outcomes and their probabilities in sequential events, using branches from nodes."),
        ("Branch", "A line in a tree diagram representing one possible outcome, labeled with its probability."),
        ("Multiply Along a Path", "To find the probability of a specific sequence, multiply the probabilities of each branch along that path."),
        ("Add Across Paths", "To find the total probability of an event occurring via multiple routes, add the probabilities of all paths leading to it."),
        ("Node", "A point in a tree diagram where branches split, representing a stage where an outcome occurs."),
    ],
    [
        ("In a probability tree, branches from the same node must sum to:", ["0", "0.5", "*1", "The sample size"],
         "All possible outcomes at each stage must have probabilities totaling 1."),
        ("To find the probability of a specific path in a tree:", ["Add the branch probabilities", "*Multiply the branch probabilities along the path", "Take the average", "Subtract them"],
         "The probability of a sequence is the product of probabilities along its path."),
        ("A tree has two stages: Stage 1 branches have P = 0.6 and 0.4; from the 0.6 branch, Stage 2 has 0.3 and 0.7. P(0.6 then 0.3) = ?", ["0.9", "0.3", "*0.18", "0.42"],
         "P = 0.6 × 0.3 = 0.18."),
        ("To find P(an event that occurs via multiple paths):", ["Multiply all paths together", "Take the longest path", "*Add the probabilities of all paths leading to the event", "Use only the first path"],
         "When an event can happen through different sequences, add their individual path probabilities."),
        ("A coin is flipped twice. How many total paths in the tree?", ["2", "*4", "6", "8"],
         "2 outcomes per flip × 2 flips = 4 paths: HH, HT, TH, TT."),
        ("Trees are especially useful for:", ["Simple one-step events", "*Multi-stage sequential events", "Finding the median", "Creating histograms"],
         "Trees organize and compute probabilities for experiments with multiple stages."),
        ("Each path through a tree represents:", ["*A specific sequence of outcomes", "A single event", "The sample mean", "A type of graph"],
         "A path traces one specific sequence from start to finish."),
        ("A bag has 3 red, 2 blue marbles. Draw 2 without replacement. The tree's first branches are:", ["P(R) = 3/5, P(B) = 3/5", "*P(R) = 3/5, P(B) = 2/5", "P(R) = 1/2, P(B) = 1/2", "P(R) = 3/2, P(B) = 2/3"],
         "First draw: 3 red out of 5, 2 blue out of 5."),
        ("After drawing a red marble (without replacement), the second branch for red is:", ["3/5", "3/4", "*2/4 = 1/2", "2/5"],
         "After removing 1 red: 2 red remain out of 4 total marbles."),
        ("P(two red, without replacement) using the tree = ?", ["9/25", "*6/20 = 3/10", "4/20", "3/5"],
         "P(RR) = 3/5 × 2/4 = 6/20 = 3/10."),
        ("Tree diagrams help avoid:", ["All calculations", "*Missing possible outcomes", "Using multiplication", "Using probability"],
         "Trees systematically list all possibilities, preventing omissions."),
        ("A medical test tree: P(disease) = 0.01, P(positive|disease) = 0.99, P(positive|no disease) = 0.05. P(positive) = ?", ["0.99", "0.05", "*0.01×0.99 + 0.99×0.05 = 0.0594", "0.01"],
         "P(+) = P(disease)×P(+|disease) + P(no disease)×P(+|no disease) = 0.0099 + 0.0495 = 0.0594."),
        ("Trees can represent:", ["Only coin flips", "Only card draws", "Only two stages", "*Any number of sequential stages"],
         "Trees can extend to as many stages as needed."),
        ("The total probability of all complete paths in a tree equals:", ["0", "0.5", "*1", "The number of paths"],
         "All possible complete sequences must sum to 1."),
        ("In a tree with conditional probabilities, branches after the first split:", ["Always have the same probabilities", "*May have different probabilities depending on the first outcome", "Are always 0.5", "Don't exist"],
         "Conditional probabilities updated after the first event create different branches."),
        ("A tree for flipping a coin 3 times has how many final paths?", ["3", "6", "*8", "12"],
         "2³ = 8 paths (all combinations of H and T over 3 flips)."),
        ("P(at least one head in 2 flips) using a tree:", ["Count paths with at least one H", "*Add P(HH) + P(HT) + P(TH) = 0.75", "P(HH) only", "1/4"],
         "Three of four paths contain at least one H: 0.25 + 0.25 + 0.25 = 0.75."),
        ("Trees visually show:", ["Only the final answer", "Only the first event", "*All stages, outcomes, and their probabilities", "Only the conditional probabilities"],
         "A tree diagram displays every stage and outcome with associated probabilities."),
        ("When drawing with replacement, the second branch probabilities:", ["Change", "Decrease", "*Stay the same as the first", "Double"],
         "Replacement restores the original conditions, keeping probabilities unchanged."),
        ("The main advantage of a probability tree is:", ["It eliminates calculation", "It only works for simple problems", "*It organizes complex multi-step probability problems visually", "It replaces all other methods"],
         "Trees provide a clear visual organization for sequential probability calculations."),
    ]
)
lessons[k] = v

# ── 4.6 Venn Diagrams ──
k, v = build_lesson(4, 6, "Venn Diagrams",
    "<h3>Venn Diagrams in Probability</h3>"
    "<p>A <b>Venn diagram</b> uses overlapping circles within a rectangle to display relationships between events.</p>"
    "<ul><li>The <b>rectangle</b> represents the entire sample space (S).</li>"
    "<li>Each <b>circle</b> represents an event.</li>"
    "<li>The <b>overlap</b> (intersection) represents outcomes in both events: A ∩ B.</li>"
    "<li>The <b>union</b> (everything in either circle) represents A ∪ B.</li></ul>"
    "<p><b>Using Venn diagrams to find probabilities:</b></p>"
    "<ul><li>P(A or B) = P(A) + P(B) − P(A and B) → corresponds to the total area of both circles.</li>"
    "<li>P(A only) = P(A) − P(A and B) → the part of A's circle not in the overlap.</li>"
    "<li>P(neither A nor B) = 1 − P(A or B) → the area outside both circles.</li></ul>"
    "<p>For <b>mutually exclusive</b> events, the circles do not overlap (intersection is empty).</p>",
    [
        ("Venn Diagram", "A diagram using overlapping circles within a rectangle to visually represent events and their relationships."),
        ("Intersection (A ∩ B)", "The set of outcomes common to both events A and B; the overlapping region in a Venn diagram."),
        ("Union (A ∪ B)", "The set of outcomes in event A, event B, or both; the total area covered by the circles."),
        ("Complement (A')", "All outcomes NOT in event A; the area outside A's circle."),
        ("Mutually Exclusive in Venn Diagrams", "Events whose circles do not overlap because they share no common outcomes."),
    ],
    [
        ("In a Venn diagram, the rectangle represents:", ["Event A", "The intersection", "*The entire sample space", "A single outcome"],
         "The rectangle encloses all possible outcomes."),
        ("The overlapping region of two circles represents:", ["A ∪ B", "A'", "*A ∩ B (intersection)", "The complement"],
         "The overlap shows outcomes that belong to both events."),
        ("P(A or B) in a Venn diagram corresponds to:", ["Only the overlap", "*The total shaded area of both circles", "Only circle A", "The rectangle minus both circles"],
         "The union covers everything inside either or both circles."),
        ("If P(A) = 0.5, P(B) = 0.4, P(A and B) = 0.2, then P(A or B) = ?", ["0.9", "*0.7", "0.2", "0.3"],
         "P(A or B) = 0.5 + 0.4 − 0.2 = 0.7."),
        ("P(A only) = ?", ["P(A) + P(A and B)", "*P(A) − P(A and B)", "P(B) − P(A and B)", "P(A or B)"],
         "P(A only) removes the intersection from A's probability."),
        ("P(neither A nor B) = ?", ["P(A and B)", "P(A) + P(B)", "*1 − P(A or B)", "P(A')"],
         "The region outside both circles = 1 − P(A ∪ B)."),
        ("Mutually exclusive events on a Venn diagram have:", ["*No overlapping region", "Complete overlap", "One circle inside the other", "No circles"],
         "No overlap means the events share no outcomes."),
        ("In a class of 40: 25 play basketball, 15 play soccer, 8 play both. How many play neither?", ["*8", "32", "0", "40"],
         "Play at least one = 25 + 15 − 8 = 32. Neither = 40 − 32 = 8."),
        ("The complement A' in a Venn diagram is:", ["Inside circle A", "*Everything outside circle A (but inside the rectangle)", "The intersection", "The union"],
         "A' is all outcomes in the sample space that are NOT in A."),
        ("Venn diagrams are useful for:", ["Only two events", "*Visualizing relationships between events and computing probabilities", "Only positive numbers", "Replacing all calculations"],
         "Venn diagrams clarify event relationships and help compute probabilities."),
        ("If A ⊂ B (A is a subset of B), on a Venn diagram:", ["The circles don't overlap", "B is inside A", "*A's circle is entirely inside B's circle", "They are the same size"],
         "When A is a subset of B, every outcome in A is also in B."),
        ("P(A ∩ B) = 0 means:", ["A and B always occur together", "*A and B are mutually exclusive", "A and B are independent", "A equals B"],
         "Zero intersection means the events cannot co-occur."),
        ("Using Venn diagrams with 3 events creates:", ["3 regions", "6 regions", "*8 regions", "4 regions"],
         "Three overlapping circles divide the rectangle into 8 distinct regions."),
        ("From a Venn diagram: A only = 20, B only = 15, A ∩ B = 10, neither = 5. Total = ?", ["45", "*50", "40", "35"],
         "Total = 20 + 15 + 10 + 5 = 50."),
        ("P(B|A) can be visualized in a Venn diagram by:", ["Looking at all of B", "*Focusing only on circle A and finding what proportion is in the intersection", "Ignoring A", "Shading the complement"],
         "P(B|A) = P(A∩B)/P(A): restrict to A's circle and find the intersection's proportion."),
        ("If two circles completely overlap, then:", ["*A = B (the events are the same)", "A and B are mutually exclusive", "P(A or B) = 0", "P(A and B) = 0"],
         "Complete overlap means both events contain exactly the same outcomes."),
        ("The union A ∪ B includes:", ["Only outcomes in A", "Only outcomes in B", "Only outcomes in both", "*All outcomes in A, B, or both"],
         "The union encompasses everything inside either circle."),
        ("A Venn diagram for mutually exclusive events A and B shows P(A or B) = ?", ["P(A) × P(B)", "*P(A) + P(B)", "P(A) − P(B)", "0"],
         "With no overlap, P(A or B) = P(A) + P(B)."),
        ("The 'Inclusion-Exclusion Principle' is represented by:", ["A stem-and-leaf plot", "A boxplot", "*The addition rule shown in a Venn diagram: P(A∪B) = P(A) + P(B) − P(A∩B)", "A histogram"],
         "The Venn diagram visually demonstrates why we subtract the intersection to avoid double-counting."),
        ("Venn diagrams are named after:", ["Isaac Newton", "*John Venn", "Karl Pearson", "Blaise Pascal"],
         "John Venn, a 19th-century mathematician, popularized these diagrams."),
    ]
)
lessons[k] = v

# ── 4.7 Applications in Games of Chance ──
k, v = build_lesson(4, 7, "Applications in Games of Chance",
    "<h3>Applications in Games of Chance</h3>"
    "<p>Probability theory originated from analyzing games of chance. Understanding these applications reinforces fundamental concepts.</p>"
    "<ul><li><b>Dice:</b> A fair six-sided die has P(any face) = 1/6. Two dice → 36 equally likely outcomes. P(sum = 7) = 6/36 = 1/6.</li>"
    "<li><b>Cards:</b> A standard deck has 52 cards (4 suits × 13 ranks). P(ace) = 4/52 = 1/13.</li>"
    "<li><b>Coins:</b> P(heads) = 1/2 for a fair coin. n flips → 2ⁿ total outcomes.</li>"
    "<li><b>Lottery:</b> Lotteries involve combinations — e.g., choosing 6 numbers from 49 → C(49,6) = 13,983,816 combinations. P(winning) ≈ 1 in 14 million.</li>"
    "<li><b>Expected value:</b> The long-run average outcome. E(X) = Σ[x · P(x)]. Casino games always have a negative expected value for the player (house edge).</li>"
    "<li><b>Gambler's fallacy:</b> The mistaken belief that past random outcomes affect future ones (e.g., 'the coin landed heads 5 times, so tails is due').</li></ul>",
    [
        ("Expected Value", "The long-run average outcome of a random variable: E(X) = Σ[x · P(x)]."),
        ("House Edge", "The mathematical advantage the casino has over players, ensuring the casino profits in the long run."),
        ("Gambler's Fallacy", "The incorrect belief that past outcomes of independent random events affect future outcomes."),
        ("Equally Likely Outcomes", "Outcomes that all have the same probability of occurring, such as each face of a fair die."),
        ("Standard Deck", "52 cards in 4 suits (hearts, diamonds, clubs, spades) with 13 ranks each (A, 2–10, J, Q, K)."),
    ],
    [
        ("P(rolling a sum of 7 with two dice) = ?", ["7/36", "*6/36 = 1/6", "7/12", "1/12"],
         "There are 6 ways to get sum 7 out of 36 total outcomes: (1,6)(2,5)(3,4)(4,3)(5,2)(6,1)."),
        ("A standard deck has how many cards?", ["48", "50", "*52", "54"],
         "52 cards: 4 suits × 13 ranks."),
        ("P(drawing a heart from a standard deck) = ?", ["1/52", "*13/52 = 1/4", "4/52", "1/2"],
         "There are 13 hearts in a 52-card deck."),
        ("The gambler's fallacy is:", ["A valid strategy", "*Believing past independent outcomes influence future ones", "A mathematical theorem", "A type of bias in surveys"],
         "Independent events have no memory — past results don't affect future probabilities."),
        ("Expected value represents:", ["The most likely single outcome", "The maximum possible outcome", "*The long-run average outcome", "The minimum outcome"],
         "E(X) is the average result you'd expect over many repetitions."),
        ("A game: win $10 with P = 0.2, lose $3 with P = 0.8. E(value) = ?", ["$10", "$3", "*−$0.40", "$7"],
         "E = 10(0.2) + (−3)(0.8) = 2 − 2.4 = −$0.40."),
        ("The house edge ensures that:", ["*The casino profits in the long run", "Players always lose every game", "The casino always breaks even", "Players have an advantage"],
         "The house edge means the expected value is negative for the player over time."),
        ("C(49, 6) for a lottery = ?", ["49 × 6", "294", "*13,983,816", "49!"],
         "C(49,6) = 49!/(6!×43!) = 13,983,816."),
        ("Two coins are flipped. P(both heads) = ?", ["1/2", "*1/4", "1/3", "2/4"],
         "P(HH) = (1/2)(1/2) = 1/4."),
        ("With two dice, total possible outcomes = ?", ["12", "6", "*36", "24"],
         "6 × 6 = 36 equally likely outcomes."),
        ("P(sum = 2 with two dice) = ?", ["2/36", "*1/36", "1/6", "2/12"],
         "Only one way: (1,1). P = 1/36."),
        ("A coin lands heads 10 times in a row. P(heads on the 11th flip) for a fair coin is:", ["Very small", "Greater than 1/2", "0", "*1/2"],
         "Each flip is independent; the probability remains 1/2 regardless of past results."),
        ("P(drawing a face card) from a standard deck = ?", ["4/52", "8/52", "*12/52 = 3/13", "16/52"],
         "12 face cards (J, Q, K in 4 suits) out of 52."),
        ("If E(X) = −$2 per game, after 100 games you expect to:", ["Win $200", "Break even", "*Lose about $200", "Win $2"],
         "Expected total = 100 × (−$2) = −$200."),
        ("Why do casinos always profit long-term?", ["They cheat", "They are lucky", "*Every game has a negative expected value for the player (house edge)", "They have more money"],
         "The mathematical structure of casino games ensures a positive expected profit for the house."),
        ("P(getting exactly 3 heads in 5 fair coin flips) uses:", ["Permutations only", "*Combinations (and binomial probability)", "Only the addition rule", "Only the complement rule"],
         "C(5,3) × (0.5)³ × (0.5)² = 10 × 1/32 = 10/32."),
        ("Two dice — P(sum > 10) = ?", ["*3/36 = 1/12", "2/36", "4/36", "1/6"],
         "Sum > 10: {11, 12}. Ways: (5,6)(6,5)(6,6) = 3 outcomes. P = 3/36."),
        ("A raffle has 500 tickets and 1 winner. P(winning) = ?", ["1/500 = 0.2%", "500", "*1/500 = 0.002", "0.5"],
         "P = 1/500 = 0.002 (or 0.2%)."),
        ("The law of large numbers says that over many games:", ["You will definitely win", "You will definitely lose", "*Your average outcome approaches the expected value", "Probability changes"],
         "Over many trials, the observed average converges to the theoretical expected value."),
        ("In poker, calculating odds of a flush requires:", ["Only the addition rule", "A Venn diagram", "*Combinatorics and conditional probability", "Only the complement rule"],
         "Poker hand probabilities use combinations to count favorable and total hands."),
    ]
)
lessons[k] = v

# ── 4.8 Probability in Genetics ──
k, v = build_lesson(4, 8, "Probability in Genetics",
    "<h3>Probability in Genetics</h3>"
    "<p>Genetics was one of the earliest applications of probability. <b>Gregor Mendel's</b> work in the 1860s used probability principles to explain inheritance patterns.</p>"
    "<ul><li><b>Punnett Square:</b> A grid used to predict genotype ratios of offspring. It is essentially a probability table based on the multiplication rule.</li>"
    "<li><b>Genotype:</b> The genetic composition (e.g., Bb = heterozygous). <b>Phenotype:</b> The observable trait (e.g., brown eyes).</li>"
    "<li><b>Dominant allele (B):</b> Expressed in both BB and Bb genotypes. <b>Recessive allele (b):</b> Only expressed in bb genotype.</li>"
    "<li><b>Monohybrid cross (Bb × Bb):</b> Probability of BB = 1/4, Bb = 1/2, bb = 1/4. Phenotype ratio: 3 dominant : 1 recessive.</li>"
    "<li><b>Independent assortment:</b> Genes on different chromosomes are inherited independently — allowing use of the multiplication rule.</li>"
    "<li><b>Hardy-Weinberg principle:</b> In a large population with no evolutionary forces, allele frequencies remain constant: p² + 2pq + q² = 1.</li></ul>",
    [
        ("Punnett Square", "A grid used to predict the probability of offspring genotypes by combining parent alleles."),
        ("Genotype vs. Phenotype", "Genotype is the genetic makeup (e.g., Bb); phenotype is the observable trait (e.g., brown eyes)."),
        ("Dominant Allele", "An allele expressed whenever present (in Bb or BB); represented by a capital letter."),
        ("Recessive Allele", "An allele expressed only when homozygous (bb); represented by a lowercase letter."),
        ("Hardy-Weinberg Equilibrium", "A principle stating that allele and genotype frequencies remain constant in a large, randomly mating population without evolutionary forces: p² + 2pq + q² = 1."),
    ],
    [
        ("A Punnett square is used to:", ["Measure traits directly", "Count chromosomes", "*Predict genotype probabilities of offspring", "Sequence DNA"],
         "Punnett squares organize parent alleles to predict offspring genotype ratios."),
        ("In a Bb × Bb cross, P(bb) = ?", ["1/2", "*1/4", "3/4", "1/3"],
         "The Punnett square shows: BB, Bb, Bb, bb → P(bb) = 1/4."),
        ("The phenotype ratio from Bb × Bb for a dominant trait is:", ["1:1", "1:2:1", "*3:1 (dominant:recessive)", "4:0"],
         "3 show the dominant trait (BB, Bb, Bb), 1 shows recessive (bb)."),
        ("The genotype ratio from Bb × Bb is:", ["*1:2:1 (BB:Bb:bb)", "3:1", "1:1", "4:0"],
         "1 BB : 2 Bb : 1 bb from the Punnett square."),
        ("A recessive trait is expressed only when:", ["One dominant allele is present", "*The genotype is homozygous recessive (bb)", "Both alleles are dominant", "The organism is male"],
         "Recessive traits require two copies of the recessive allele."),
        ("Mendel's work applied which probability rule?", ["Only the addition rule", "Bayes' Theorem", "*The multiplication rule (independent assortment)", "Only the complement rule"],
         "Mendel used the multiplication rule because genes on different chromosomes assort independently."),
        ("In Hardy-Weinberg, q² represents:", ["Dominant homozygotes", "Heterozygotes", "*Recessive homozygotes", "All genotypes"],
         "q² = frequency of homozygous recessive (aa) individuals."),
        ("P(carrier) in Hardy-Weinberg (heterozygous) = ?", ["p²", "q²", "*2pq", "p + q"],
         "2pq represents the proportion of heterozygous carriers."),
        ("If two carriers (Bb) have a child, P(child is a carrier) = ?", ["1/4", "*1/2", "3/4", "1"],
         "From Bb × Bb: P(Bb) = 2/4 = 1/2."),
        ("Independent assortment means:", ["Genes always travel together", "*Genes on different chromosomes are inherited independently", "All offspring are identical", "Probability doesn't apply"],
         "Genes on different chromosomes separate independently during meiosis."),
        ("A dihybrid cross (BbRr × BbRr) produces a phenotype ratio of:", ["3:1", "1:2:1", "*9:3:3:1", "1:1:1:1"],
         "Independent assortment of two genes gives the classic 9:3:3:1 ratio."),
        ("P(BBRr) in a dihybrid cross (BbRr × BbRr) = ?", ["1/4", "*2/16 = 1/8", "1/16", "3/16"],
         "P(BB) = 1/4, P(Rr) = 2/4 = 1/2; P(BBRr) = 1/4 × 1/2 = 1/8."),
        ("Genetic probability uses the multiplication rule because:", ["Genes are always linked", "*Genes on different chromosomes segregate independently", "All alleles are dominant", "Offspring are identical"],
         "Independent assortment allows use of the multiplication rule for traits on different chromosomes."),
        ("A test cross (Bb × bb) gives what ratio?", ["All Bb", "*1:1 (Bb:bb)", "3:1", "1:2:1"],
         "Bb × bb → Bb, Bb, bb, bb. Genotype ratio = 1:1 in expected proportions; actually 2 Bb : 2 bb = 1:1."),
        ("Genotype refers to:", ["The physical appearance", "*The genetic composition (allele combination)", "The environment", "The species"],
         "Genotype is the set of alleles an organism carries."),
        ("Phenotype refers to:", ["*The observable trait or characteristic", "The DNA sequence", "The allele letters", "The chromosome number"],
         "Phenotype is the outward expression of the genotype."),
        ("Probability helps geneticists:", ["Only study Mendel's peas", "Avoid doing experiments", "*Predict the likelihood of traits appearing in offspring", "Eliminate mutations"],
         "Probability quantifies the chance of specific genetic outcomes."),
        ("If q = 0.3 (recessive allele frequency), p = ?", ["0.3", "0.09", "*0.7", "0.91"],
         "p + q = 1, so p = 1 − 0.3 = 0.7."),
        ("P(at least one child with bb out of 3 children from Bb × Bb) is found using:", ["The mean", "*The complement: 1 − P(no bb children) = 1 − (3/4)³", "A stemplot", "Only a Punnett square"],
         "P(at least one bb) = 1 − P(all not bb) = 1 − (3/4)³ = 1 − 27/64 = 37/64."),
        ("The Punnett square is a visual application of:", ["Descriptive statistics", "*The multiplication rule of probability", "The Empirical Rule", "Regression analysis"],
         "Each cell in a Punnett square represents the product of two allele probabilities."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 4)")
