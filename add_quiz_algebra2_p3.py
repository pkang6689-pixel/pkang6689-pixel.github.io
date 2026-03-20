#!/usr/bin/env python3
"""Add quiz questions to Algebra 2 lessons (→20 each). Units 7-9."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "algebra_2_lessons.json")

def mq(qt, opts, exp):
    options = []
    for o in opts:
        c = o.startswith("*")
        options.append({"text": o.lstrip("*"), "is_correct": c, "data_i18n": None})
    return {"question_number": 0, "question_text": qt, "attempted": 2,
            "data_i18n": None, "options": options, "explanation": exp}

EXTRA = {}

# ── U7 L7.1 Counting Principles ──
EXTRA["u7_l7.1"] = [
    ("The Fundamental Counting Principle says: if task A has m ways and task B has n ways, both together have:",["m + n","m − n","*m × n","m/n"],"Multiply independent choices."),
    ("A license plate has 3 letters then 4 digits. The number of possible plates is:",["26 + 10","26³ + 10⁴","*26³ × 10⁴","26⁴ × 10³"],"Multiply choices."),
    ("How many 3-digit numbers can be formed from {1,2,3,4,5} with repetition?",["15","60","*125","243"],"5×5×5=125."),
    ("How many 3-digit numbers from {1,2,3,4,5} WITHOUT repetition?",["125","*60","120","15"],"5×4×3=60."),
    ("A restaurant offers 3 appetizers, 5 entrees, and 2 desserts. How many meals?",["10","15","*30","52"],"3×5×2=30."),
    ("How many ways to arrange the letters A, B, C?",["3","*6","9","27"],"3!=6."),
    ("n! (n factorial) equals:",["n × n","*n × (n−1) × (n−2) × ... × 1","2ⁿ","n²"],"Product of all positive integers up to n."),
    ("5! = ",["25","*120","60","600"],"5×4×3×2×1=120."),
    ("0! = ",["0","Undefined","*1","−1"],"By definition."),
    ("A PIN has 4 digits (0-9). With repetition allowed, total PINs:",["40","1000","*10,000","10⁶"],"10⁴=10000."),
    ("A coin is flipped 8 times. The number of possible outcomes is:",["16","64","*256","8"],"2⁸=256."),
    ("The Addition Principle: if task can be done in m ways OR n ways (no overlap), total = :",["m × n","*m + n","m!","mn/2"],"OR → add."),
    ("How many ways to choose a president and VP from 10 people?",["20","50","*90","100"],"10×9=90 (order matters)."),
]

# ── U7 L7.2 Permutations & Combinations ──
EXTRA["u7_l7.2"] = [
    ("A permutation is an arrangement where _____ matters.",["Size","*Order","Color","Count"],"Arrangement matters."),
    ("P(n, r) = ",["n!/(n−r)!r!","*n!/(n−r)!","n!/r!","nʳ"],"Permutation formula."),
    ("P(5, 3) = ",["10","*60","125","15"],"5!/2!=120/2=60."),
    ("A combination is a selection where _____ does NOT matter.",["Size","Time","*Order","Position"],"Grouping only."),
    ("C(n, r) = ",["n!/(n−r)!","nʳ","*n!/(r!(n−r)!)","n!/r!"],"Combination formula."),
    ("C(5, 3) = ",["60","15","*10","5"],"5!/(3!2!)=10."),
    ("Choosing a committee of 3 from 8 people: P or C?",["Permutation","*Combination (order doesn't matter for a committee)","Neither","Both"],"No ordering."),
    ("Ranking the top 3 from 8 contestants: P or C?",["Combination","*Permutation (the ranking implies order)","Neither","Both"],"1st/2nd/3rd matter."),
    ("C(n, 0) = ",["0","n","*1","Undefined"],"One way to choose nothing."),
    ("C(n, n) = ",["0","n","*1","n!"],"One way to choose all."),
    ("C(n, r) = C(n, ___) — symmetry property.",["r","*n−r","r+1","n"],"Choose r = leave n−r."),
    ("How many ways to form a 5-card hand from a 52-card deck?",["52⁵","*C(52,5) = 2,598,960","52!/5!","P(52,5)"],"Combination."),
    ("Permutations with identical items: arrangements of MISSISSIPPI = 11!/(4!4!2!):",["*34,650","11!","39,916,800","1"],"Divide by repeated factorials."),
]

# ── U7 L7.3 Probability Basics ──
EXTRA["u7_l7.3"] = [
    ("The probability of an event is always between:",["−1 and 1","*0 and 1 (inclusive)","0 and ∞","−∞ and ∞"],"0 ≤ P(E) ≤ 1."),
    ("P(sure thing) = ",["0","*1","0.5","∞"],"Certain event."),
    ("P(impossible event) = ",["1","*0","−1","0.5"],"Cannot happen."),
    ("P(rolling a 3 on a fair die) = ",["1/3","3/6","*1/6","1/2"],"1 out of 6."),
    ("The complement P(not A) = ",["P(A)","P(A)²","*1 − P(A)","P(A) + 1"],"Complement rule."),
    ("P(heads OR tails on a fair coin) = ",["0.5","0","*1","0.25"],"All outcomes."),
    ("Two events are mutually exclusive if they:",["Always happen together","Are independent","*Cannot happen at the same time","Have equal probability"],"No overlap."),
    ("P(A or B) for mutually exclusive events = ",["P(A) × P(B)","*P(A) + P(B)","P(A) − P(B)","1"],"Addition rule (no overlap)."),
    ("P(A or B) general = P(A) + P(B) − ___.",["P(A)P(B)","P(A)","*P(A and B)","0"],"Inclusion-exclusion."),
    ("In a standard deck, P(King or Heart) = ",["4/52 + 13/52","*4/52 + 13/52 − 1/52 = 16/52 = 4/13","17/52","4/52"],"One king is a heart."),
    ("The sample space is the set of all _____ outcomes.",["Favorable","*Possible","Impossible","Zero"],"Complete list."),
    ("An event is a _____ of the sample space.",["Complement","*Subset","Product","Sum"],"Some outcomes."),
    ("Experimental probability is based on _____, while theoretical is based on _____.",["Theory, data","*Data (actual trials), mathematical reasoning","Guessing, experiments","Neither"],"Two types."),
]

# ── U7 L7.4 Conditional Probability ──
EXTRA["u7_l7.4"] = [
    ("P(A|B) means the probability of A _____ B has occurred.",["Before","Instead of","*Given that","Or"],"Conditional."),
    ("P(A|B) = P(A and B) / ___.",["P(A)","P(A or B)","*P(B)","P(not B)"],"Conditional formula."),
    ("Two events are independent if P(A|B) = ",["0","P(B)","*P(A)","1"],"B doesn't affect A."),
    ("For independent events, P(A and B) = ",["P(A) + P(B)","P(A|B)","*P(A) × P(B)","P(A)/P(B)"],"Multiplication rule."),
    ("A bag has 3 red, 2 blue. Draw one, don't replace, then draw another. These draws are:",["Independent","*Dependent (first draw changes the pool)","Mutually exclusive","Complementary"],"Without replacement."),
    ("P(2nd red | 1st red) from 3R, 2B bag (no replacement) = ",["3/5","1/5","*2/4 = 1/2","3/4"],"After removing 1 red: 2R in 4."),
    ("Bayes' Theorem is used to:",["Calculate permutations","*Update probabilities based on new evidence (reverse conditional probability)","Find combinations","Sum probabilities"],"Updating beliefs."),
    ("If P(A)=0.6 and P(B)=0.3 and they're independent, P(A and B)=",["0.9","0.3","*0.18","0.6"],"0.6×0.3=0.18."),
    ("If P(A)=0.6 and P(B)=0.3 independent, P(A or B)=",["0.9","0.18","*0.72","0.6"],"0.6+0.3−0.18=0.72."),
    ("A tree diagram helps visualize:",["Only sums","*Sequential outcomes and their probabilities","Only products","Graphs"],"Branch probabilities."),
    ("In a two-way table, P(A and B) is found in the _____ of row A and column B.",["Sum","Margin","*Intersection (cell)","Diagonal"],"Joint probability."),
    ("Marginal probabilities are found in the _____ of a two-way table.",["Center cells","Diagonal","*Row/column totals (margins)","Title"],"Edge totals."),
    ("If drawing cards WITH replacement, each draw is:",["Dependent","Conditional","*Independent","Mutually exclusive"],"Pool unchanged."),
]

# ── U7 L7.5 Normal Distributions ──
EXTRA["u7_l7.5"] = [
    ("A normal distribution is _____ shaped.",["Skewed","Uniform","*Bell (symmetric, unimodal)","Rectangular"],"Bell curve."),
    ("In a normal distribution, mean = median = _____.",["Standard deviation","Variance","*Mode","Range"],"All equal at center."),
    ("The Empirical Rule: about 68% of data falls within _____ standard deviation(s) of the mean.",["2","3","*1","0.5"],"68-95-99.7 rule."),
    ("About 95% of data falls within _____ standard deviations.",["1","*2","3","4"],"Second tier."),
    ("About 99.7% falls within _____ standard deviations.",["1","2","*3","4"],"Nearly all."),
    ("The standard normal distribution has mean = _____ and σ = _____.",["1 and 0","*0 and 1","0 and 0","1 and 1"],"Z-distribution."),
    ("A z-score represents the number of _____ a value is from the mean.",["Means","Ranges","*Standard deviations","Quartiles"],"Standardized distance."),
    ("z = (x − μ) / ___.",["μ","x","*σ","n"],"Z-score formula."),
    ("A z-score of 2.0 means the value is _____ standard deviations above the mean.",["1","*2","3","0"],"Directly interpreted."),
    ("A negative z-score means the value is _____ the mean.",["Above","Equal to","*Below","Undefined"],"Below average."),
    ("The total area under a normal curve = _____.",["0","0.5","*1","μ"],"Total probability."),
    ("P(z < 0) in a standard normal distribution = _____.",["0","1","*0.5","0.68"],"Symmetric, half below."),
    ("The inflection points of a normal curve are at x = μ ± ___.",["2σ","μ","*σ","3σ"],"Where curvature changes."),
]

# ── U7 L7.6 Hypothesis Testing ──
EXTRA["u7_l7.6"] = [
    ("The null hypothesis (H₀) typically states:",["There is an effect","*There is no effect or no difference (status quo)","The alternative","The conclusion"],"Default assumption."),
    ("The alternative hypothesis (H₁) states:",["No change","*There IS an effect or difference","The null is true","Nothing"],"What we want to show."),
    ("A p-value represents:",["The probability H₁ is true","The probability H₀ is true","*The probability of observing results as extreme (or more) if H₀ is true","The average"],"Extremeness measure."),
    ("If p-value < significance level (α), we _____ H₀.",["Accept","Prove","*Reject","Ignore"],"Statistically significant."),
    ("A common significance level is α = ",["1","0.5","*0.05","0.95"],"5%."),
    ("A Type I error is:",["Failing to reject a false H₀","*Rejecting a true H₀ (false positive)","Correct decision","Type II error"],"False alarm."),
    ("A Type II error is:",["Rejecting a true H₀","*Failing to reject a false H₀ (false negative)","Correct decision","Type I error"],"Missing a real effect."),
    ("Increasing sample size generally _____ the power of a test.",["Decreases","*Increases","Has no effect","Doubles"],"More data → better detection."),
    ("A one-tailed test checks for an effect in _____ direction(s).",["Two","*One","No","All"],"Directional."),
    ("A two-tailed test checks for an effect in _____ direction(s).",["One","*Two (either above or below)","No","All"],"Non-directional."),
    ("Statistical significance does NOT necessarily mean:",["The math is right","H₀ was rejected","*Practical significance (a real-world important effect)","A p-value exists"],"Significance ≠ importance."),
    ("The significance level α is the maximum acceptable probability of a _____ error.",["Type II","Any","*Type I","Both"],"False positive threshold."),
    ("A confidence interval provides a range of _____ values for a parameter.",["Impossible","*Plausible (likely to contain the true value)","Exact","Single"],"Range estimate."),
]

# ── U7 L7.7 Correlation & Regression ──
EXTRA["u7_l7.7"] = [
    ("The correlation coefficient r ranges from:",["0 to 1","−∞ to ∞","*−1 to 1","0 to ∞"],"Bounded."),
    ("r = 1 indicates a perfect _____ linear relationship.",["Negative","No","*Positive","Curved"],"Perfect positive."),
    ("r = −1 indicates a perfect _____ linear relationship.",["Positive","No","*Negative","Curved"],"Perfect negative."),
    ("r ≈ 0 indicates:",["Strong relationship","*Little or no LINEAR relationship (could still be nonlinear)","Perfect correlation","Causation"],"Weak linear."),
    ("Correlation does NOT imply:",["Association","Relationship","*Causation","r-value"],"Classic principle."),
    ("The line of best fit (regression line) minimizes the sum of squared:",["x-values","slopes","*Residuals (vertical distances from points to line)","y-intercepts"],"Least squares."),
    ("The regression equation is typically written as ŷ = ",["*a + bx (where b is slope, a is y-intercept)","ax²+bx+c","mx+b only","y=x"],"Linear form."),
    ("A residual is defined as:",["Predicted − slope","*Observed − Predicted (actual minus model)","Mean − median","x − y"],"Error measurement."),
    ("If the residual plot shows a pattern, the linear model may be:",["Good","*Inappropriate (suggesting a nonlinear relationship)","Perfect","Exact"],"Random residuals = good fit."),
    ("r² (coefficient of determination) represents the _____ of variation in y explained by x.",["Sum","Mean","*Proportion (percentage)","Product"],"Explanatory power."),
    ("If r = 0.8, then r² = :",["0.8","*0.64","0.4","1.6"],"Square it."),
    ("Extrapolation (predicting beyond the data range) is _____ than interpolation.",["Safer","Equally safe","*Riskier (less reliable, as pattern may not continue)","Always wrong"],"Beyond known range."),
    ("An outlier in regression can _____ the correlation and slope.",["Never affect","*Strongly influence (especially if it has high leverage)","Slightly affect","Eliminate"],"Influential points."),
]

# ── U8 L8.1 Angles & Radian Measure ──
EXTRA["u8_l8.1"] = [
    ("One full revolution = _____ radians.",["π","*2π","4π","π/2"],"360° = 2π."),
    ("π radians = _____ degrees.",["90","360","*180","270"],"Half revolution."),
    ("To convert degrees to radians, multiply by:",["180/π","*π/180","2π","360"],"Conversion factor."),
    ("90° = _____ radians.",["π","2π","*π/2","π/4"],"90·π/180."),
    ("60° = _____ radians.",["π/2","*π/3","π/4","π/6"],"60·π/180."),
    ("1 radian ≈ _____ degrees.",["90","*57.3","45","180"],"180/π≈57.3."),
    ("An angle in standard position has its vertex at the _____ and initial side along the _____.",["(1,0), y-axis","*Origin, positive x-axis","(0,1), x-axis","Origin, negative x-axis"],"Standard position."),
    ("A positive angle rotates _____.",["Clockwise","*Counterclockwise","Neither","Both"],"Convention."),
    ("Coterminal angles differ by multiples of:",["180°","90°","*360°","45°"],"Same terminal side."),
    ("An angle of 405° is coterminal with:",["90°","180°","*45°","315°"],"405−360=45."),
    ("Arc length s = rθ where θ is in:",["Degrees","*Radians","Revolutions","Gradians"],"Radian measure required."),
    ("A sector area = (1/2)r²θ. For r=6 and θ=π/3, area = :",["6π","*6π (½·36·π/3 = 6π)","12π","18π"],"6π."),
    ("The reference angle for 225° is:",["45°","135°","*45° (225−180=45)","225°"],"Third quadrant: subtract 180."),
]

# ── U8 L8.2 Unit Circle & Trig Functions ──
EXTRA["u8_l8.2"] = [
    ("On the unit circle, x = _____ and y = _____.",["tan θ, sec θ","*cos θ, sin θ","sin θ, cos θ","1, 0"],"Coordinate relationship."),
    ("sin(0) = ",["1","*0","−1","1/2"],"y-coordinate at 0."),
    ("cos(0) = ",["0","*1","−1","1/2"],"x-coordinate at 0."),
    ("sin(π/2) = ",["0","*1","−1","1/2"],"Top of circle."),
    ("cos(π/2) = ",["1","*0","−1","1/2"],"Top of circle, x=0."),
    ("sin(π/6) = cos(π/3) = ",["√3/2","√2/2","*1/2","1"],"30° sine = 60° cosine."),
    ("sin(π/4) = cos(π/4) = ",["1/2","*√2/2","√3/2","1"],"45° values."),
    ("sin(π/3) = cos(π/6) = ",["1/2","√2/2","*√3/2","1"],"60° sine."),
    ("tan θ = ",["cos θ/sin θ","*sin θ/cos θ","sin θ + cos θ","1/sin θ"],"Tangent ratio."),
    ("In Quadrant II: sin is _____, cos is _____.",["negative, positive","*positive, negative","positive, positive","negative, negative"],"All Students Take Calculus."),
    ("In Quadrant III: both sin and cos are:",["Positive","*Negative","Sin positive","Cos positive"],"Third quadrant."),
    ("sin²θ + cos²θ = ",["0","2","*1","sin θ + cos θ"],"Pythagorean identity."),
    ("The reciprocal of sin θ is:",["cos θ","tan θ","*csc θ","sec θ"],"Cosecant."),
]

# ── U8 L8.3 Graphs of Trigonometric Functions ──
EXTRA["u8_l8.3"] = [
    ("The period of y = sin x is:",["π","*2π","4π","π/2"],"One full cycle."),
    ("The amplitude of y = sin x is:",["2π","0","*1","π"],"Maximum displacement."),
    ("For y = A sin(Bx), the amplitude is |A| and the period is:",["2π/A","*2π/B","2πB","A/B"],"Period formula."),
    ("The amplitude of y = 3 sin(x) is:",["1","*3","6","π"],"Coefficient of sine."),
    ("The period of y = sin(2x) is:",["2π","4π","*π","π/2"],"2π/2=π."),
    ("The graph of y = cos x is the same as y = sin x shifted _____ by π/2.",["Down","Up","*Left","Right"],"cos x = sin(x + π/2)."),
    ("y = sin(x − π/4) is the graph of y = sin x shifted _____ by π/4.",["Left","Up","*Right","Down"],"Phase shift right."),
    ("y = sin(x) + 3 shifts the graph _____ by 3.",["Down","Left","*Up","Right"],"Vertical shift (midline at y=3)."),
    ("The midline of y = 2 sin(x) + 5 is y = ",["2","*5","7","3"],"Vertical shift."),
    ("The period of y = tan x is:",["2π","*π","π/2","4π"],"Tangent repeats at π."),
    ("The graph of y = tan x has vertical asymptotes where _____ = 0.",["sin x","*cos x","tan x","x"],"Division by zero."),
    ("y = −sin(x) reflects the sine graph over the:",["y-axis","*x-axis","origin","line y=x"],"Negative flips vertically."),
    ("For y = A sin(Bx − C) + D, the phase shift is:",["C","*C/B","B/C","−C"],"Phase shift formula."),
]

# ── U8 L8.4 Trigonometric Identities ──
EXTRA["u8_l8.4"] = [
    ("The Pythagorean identity: sin²θ + cos²θ = ",["sin θ","cos θ","*1","2"],"Fundamental identity."),
    ("Dividing the Pythagorean identity by cos²θ gives:",["sin²θ + 1 = sec²θ","*tan²θ + 1 = sec²θ","1 + cot²θ = csc²θ","sin²θ = 1"],"Tangent-secant form."),
    ("Dividing by sin²θ gives:",["tan²θ + 1 = sec²θ","*1 + cot²θ = csc²θ","sin²θ + cos²θ = 1","cot²θ = 1"],"Cotangent-cosecant form."),
    ("sin(A + B) = ",["sin A sin B + cos A cos B","*sin A cos B + cos A sin B","cos A cos B − sin A sin B","sin A + sin B"],"Sum formula."),
    ("cos(A + B) = ",["cos A cos B + sin A sin B","*cos A cos B − sin A sin B","sin A cos B + cos A sin B","cos A + cos B"],"Sum formula."),
    ("sin(2θ) = ",["sin²θ + cos²θ","2 sin θ","*2 sin θ cos θ","sin θ + cos θ"],"Double angle."),
    ("cos(2θ) can equal:",["2cos²θ − 1 only","1 − 2sin²θ only","*cos²θ − sin²θ, or 2cos²θ − 1, or 1 − 2sin²θ (all three forms)","sin²θ − cos²θ"],"Three equivalent forms."),
    ("tan(A + B) = (tan A + tan B) / :",["tan A + tan B","*1 − tan A tan B","1 + tan A tan B","tan A − tan B"],"Sum formula."),
    ("To verify an identity, work on _____ side to make it match the other.",["Both simultaneously","*One (usually the more complex)","Neither","Create a new equation"],"Proof strategy."),
    ("sin(−θ) = ",["sin θ","*−sin θ","cos θ","1"],"Sine is odd."),
    ("cos(−θ) = ",["−cos θ","*cos θ","sin θ","−sin θ"],"Cosine is even."),
    ("Simplify: sin θ · csc θ = ",["sin²θ","0","*1","2 sin θ"],"sin θ · (1/sin θ) = 1."),
    ("The identity (1 − cos 2θ)/2 = ",["cos²θ","*sin²θ","tan θ","1"],"Half-angle/power-reducing."),
]

# ── U8 L8.5 Solving Trigonometric Equations ──
EXTRA["u8_l8.5"] = [
    ("Solve sin θ = 1/2 for 0 ≤ θ < 2π:",["θ = π/6 only","θ = π/3 only","*θ = π/6 and θ = 5π/6","θ = π/6 and θ = 7π/6"],"Q1 and Q2."),
    ("Solve cos θ = 0 for 0 ≤ θ < 2π:",["θ = 0","*θ = π/2 and θ = 3π/2","θ = π","θ = π/2 only"],"Top and bottom."),
    ("Solve tan θ = 1 for 0 ≤ θ < 2π:",["θ = π/4 only","*θ = π/4 and θ = 5π/4","θ = π/4 and θ = 3π/4","θ = 0"],"Q1 and Q3."),
    ("For the general solution of sin θ = 1/2: θ = π/6 + 2nπ or θ = _____ + 2nπ.",["7π/6","11π/6","*5π/6","π/3"],"Both solutions."),
    ("Solve 2sin²θ − 1 = 0 → sin²θ = 1/2 → sin θ = :",["1/2","*±√2/2","±1","±1/4"],"Square root."),
    ("Solve 2cos²θ − cos θ − 1 = 0. Factor:",["(cos θ − 1)²","*(2cos θ + 1)(cos θ − 1) = 0","(cos θ + 1)(2cos θ − 1)","Cannot factor"],"cos θ = −1/2 or 1."),
    ("When solving trig equations, always consider _____ in each period.",["One solution","*All possible solutions (check each quadrant where the trig value holds)","No solutions","Extra solutions"],"Don't miss solutions."),
    ("Solve sin 2θ = 0 for 0 ≤ θ < 2π. Number of solutions:",["2","*4 (θ = 0, π/2, π, 3π/2)","1","8"],"2θ = 0, π, 2π, 3π."),
    ("Using identities to solve: if sin²θ + sinθ − 2 = 0, factor:",["(sin θ + 2)(sin θ − 1)","*(sin θ + 2)(sin θ − 1) = 0 → sin θ = 1 only (sin θ = −2 impossible)","(sin θ − 2)(sin θ + 1)","Cannot factor"],"Domain: −1 ≤ sin ≤ 1."),
    ("If cos θ = −√3/2 in [0, 2π), solutions are in quadrants:",["I and II","*II and III","III and IV","I and IV"],"Cos negative in Q2, Q3."),
    ("Solve tan²θ = 3 → tan θ = ±√3. In [0, 2π), how many solutions?",["2","*4","6","3"],"π/3, 2π/3, 4π/3, 5π/3."),
    ("When squaring both sides of a trig equation, you must check for:",["Symmetry","*Extraneous solutions (squaring can introduce false answers)","Identities","Periodicity"],"Verify all solutions."),
    ("Inverse trig functions restrict the _____ to give a unique answer.",["Period","*Domain (or range, depending on perspective)","Amplitude","Equation"],"Principal value."),
]

# ── U8 L8.6 Applications of Trigonometry ──
EXTRA["u8_l8.6"] = [
    ("The Law of Sines: a/sin A = b/sin B = _____.",["c/cos C","a·b","*c/sin C","a+b+c"],"Ratio equality."),
    ("The Law of Cosines: c² = a² + b² − _____.",["2ab","c²","*2ab cos C","a²b²"],"Generalized Pythagorean."),
    ("The Law of Sines is used when you know:",["Three sides (SSS)","*AAS, ASA, or SSA (angle-side combinations)","Three angles","SAS only"],"Angle-side pairs."),
    ("The Law of Cosines is used when you know:",["AAS","*SAS or SSS","ASA only","Only angles"],"Side-angle-side or three sides."),
    ("In the ambiguous case (SSA), there can be _____ triangle solution(s).",["Only 1","Only 0","*0, 1, or 2","3"],"Ambiguous case."),
    ("The area of a triangle with sides a, b and included angle C: Area = :",["ab cos C","a + b + C","*½ ab sin C","ab/sin C"],"Trig area formula."),
    ("A bearing of N30°E means _____ degrees from north toward east.",["60","*30","90","120"],"Navigation bearing."),
    ("Heron's formula uses the _____ to find area from three sides.",["Law of Sines","*Semi-perimeter s = (a+b+c)/2 → Area = √(s(s−a)(s−b)(s−c))","Cosine rule","Pythagorean theorem"],"Three-side area."),
    ("In surveying, angles of elevation look _____.",["Down","Horizontal","*Up","Sideways"],"Upward angle."),
    ("Angles of depression look _____.",["Up","*Down (from horizontal)","Horizontal","Behind"],"Downward angle."),
    ("The angle of elevation from point A to the top of a 50m tower is 30°. Distance from A to the base:",["50m","25m","*50√3 ≈ 86.6m","100m"],"tan 30° = 50/d → d = 50/tan 30°."),
    ("Harmonic motion (springs, pendulums) is modeled by _____ functions.",["Linear","Exponential","*Sinusoidal (sine or cosine)","Logarithmic"],"Periodic motion."),
    ("Simple harmonic motion: y = A cos(ωt). The frequency f = :",["2π/ω","*ω/(2π)","Aω","1/A"],"Cycles per unit time."),
]

# ── U9 L9.1 Conic Sections ──
EXTRA["u9_l9.1"] = [
    ("The four conic sections are:",["Lines, circles, squares, triangles","*Circle, ellipse, parabola, hyperbola","Circle, oval, line, point","Square, rectangle, triangle, circle"],"Slicing a cone."),
    ("A circle is the set of all points equidistant from a fixed point called the:",["Focus","Vertex","*Center","Directrix"],"Circle definition."),
    ("Circle equation: (x−h)² + (y−k)² = r². The center is:",["(r, r)","(0, 0) always","*(h, k)","(x, y)"],"Standard form."),
    ("An ellipse has _____ foci.",["1","*2","3","4"],"Definition."),
    ("For an ellipse, the sum of distances from any point to the two foci is:",["Variable","*Constant (equals 2a, the major axis length)","The semi-minor axis","Zero"],"Ellipse definition."),
    ("The standard form of an ellipse centered at origin: x²/a² + y²/b² = 1. If a > b, the major axis is:",["Vertical","*Horizontal","Diagonal","Circular"],"Longer axis."),
    ("A parabola is the set of points equidistant from a focus and a:",["Center","Second focus","*Directrix (a line)","Vertex"],"Parabola definition."),
    ("The vertex of a parabola y = a(x−h)²+k is at:",["(0, 0)","(a, k)","*(h, k)","(x, y)"],"Vertex form."),
    ("A hyperbola has the equation x²/a² − y²/b² = 1. It has _____ branches.",["1","*2","3","4"],"Two curves."),
    ("The asymptotes of x²/a² − y²/b² = 1 are y = :",["a/b","*±(b/a)x","±(a/b)x","±1"],"Asymptote slopes."),
    ("The eccentricity of a circle is:",["1","*0","Greater than 1","Undefined"],"Perfect symmetry."),
    ("As eccentricity increases from 0 toward 1, an ellipse becomes more:",["Circular","*Elongated (more stretched out)","Square","Triangular"],"Approaching parabolic."),
    ("A parabola has eccentricity = :",["0","*1","2","0.5"],"Exactly 1."),
]

# ── U9 L9.2 Parametric Equations ──
EXTRA["u9_l9.2"] = [
    ("Parametric equations express x and y each as a function of a third variable called the:",["Slope","Intercept","*Parameter (usually t)","Constant"],"Parameter."),
    ("To eliminate the parameter from x = 2t and y = t², substitute:",["t = y","t = x","*t = x/2 → y = (x/2)² = x²/4","Cannot eliminate"],"Substitution."),
    ("The parametric equations x = cos t, y = sin t trace a:",["Line","Parabola","*Circle (unit circle)","Hyperbola"],"Trig parametric."),
    ("An advantage of parametric equations is they can describe:",["Only lines","Only circles","*Curves that fail the vertical line test, and direction/timing of motion","Only functions"],"Non-function curves."),
    ("x = 3cos t, y = 2sin t traces an:",["Circle","*Ellipse","Parabola","Hyperbola"],"Scaled circle = ellipse."),
    ("The parameter t often represents:",["Slope","*Time","Amplitude","Frequency"],"Physical meaning."),
    ("To find the slope of a parametric curve: dy/dx = :",["dx/dt","dt/dy","*(dy/dt)/(dx/dt)","dy + dx"],"Chain rule."),
    ("The direction of motion along x = t, y = t² as t increases is from _____ to _____.",["Right to left","*Left to right (x increases with t)","Top to bottom","Random"],"Arrows show direction."),
    ("Eliminating t from x = t + 1, y = 2t − 3 gives:",["y = x − 4","y = 2x + 3","*y = 2(x−1) − 3 = 2x − 5","y = x + 1"],"t = x−1, y = 2(x−1) − 3."),
    ("x = sec t, y = tan t satisfies which identity?",["x²+y²=1","*x²−y²=1 (since sec²−tan²=1)","y²−x²=1","xy=1"],"Hyperbola."),
    ("A cycloid is the curve traced by a point on a _____ as it rolls.",["Square","Ellipse","*Circle (rolling along a line)","Spiral"],"Classic curve."),
    ("Parametric form of a line through (x₁,y₁) with direction (a,b): x = x₁+at, y = :",["y₁ + at","*y₁ + bt","y₁/t","y₁ − at"],"Point + direction·t."),
    ("Converting parametric to rectangular is called _____ the parameter.",["Adding","*Eliminating","Multiplying","Differentiating"],"Remove t."),
]

# ── U9 L9.3 Vectors ──
EXTRA["u9_l9.3"] = [
    ("A vector has both _____ and direction.",["Speed","Length only","*Magnitude (size)","None"],"Two properties."),
    ("The magnitude of vector ⟨3, 4⟩ is:",["7","25","*5","1"],"√(9+16)=5."),
    ("The zero vector ⟨0, 0⟩ has magnitude:",["1","∞","*0","Undefined"],"Zero length."),
    ("Vector addition: ⟨a,b⟩ + ⟨c,d⟩ = :",["⟨ac, bd⟩","*⟨a+c, b+d⟩","⟨a−c, b−d⟩","⟨a/c, b/d⟩"],"Component-wise."),
    ("Scalar multiplication: 3⟨2, −1⟩ = :",["⟨5, 2⟩","⟨2/3, −1/3⟩","*⟨6, −3⟩","⟨3, 3⟩"],"Multiply each component."),
    ("A unit vector has magnitude:",["0","*1","2","The same as the original"],"Normalized."),
    ("To find the unit vector of ⟨3,4⟩: divide by its magnitude:",["⟨3,4⟩/25","*⟨3/5, 4/5⟩","⟨1,1⟩","⟨4/5,3/5⟩"],"Divide by 5."),
    ("The dot product ⟨a,b⟩ · ⟨c,d⟩ = :",["⟨ac, bd⟩","*ac + bd","ad + bc","ad − bc"],"Sum of products."),
    ("If the dot product of two vectors is 0, they are:",["Parallel","Equal","*Perpendicular (orthogonal)","Opposite"],"Zero dot product."),
    ("⟨1,2⟩ · ⟨3,4⟩ = ",["⟨3,8⟩","7","*11","−1"],"1·3+2·4=11."),
    ("The direction angle θ of vector ⟨a,b⟩ satisfies tan θ = :",["a/b","*b/a","a+b","ab"],"arctan(b/a)."),
    ("Two vectors are parallel if one is a _____ of the other.",["Sum","Dot product","*Scalar multiple","Difference"],"Same direction (or opposite)."),
    ("The resultant of two forces is found by _____ addition.",["Scalar","*Vector","Matrix","Complex"],"Add force vectors."),
]

# ── U9 L9.4 Complex Numbers in Polar Form ──
EXTRA["u9_l9.4"] = [
    ("A complex number a + bi can be written in polar form as:",["a cos θ + b sin θ","*r(cos θ + i sin θ) where r = |a+bi|","r²(cos θ − i sin θ)","a/r + b/r"],"Polar form."),
    ("The modulus (absolute value) of 3 + 4i is:",["7","25","*5","1"],"√(9+16)=5."),
    ("The argument (angle) of a complex number is the angle measured from the:",["y-axis","imaginary axis","*positive real axis (x-axis)","origin"],"Argument definition."),
    ("Convert 1 + i to polar: r = _____, θ = _____.",["1, 0","*√2, π/4","2, π/2","1, π"],"r=√2, θ=arctan(1/1)=π/4."),
    ("To multiply two complex numbers in polar form, _____ their moduli and _____ their arguments.",["Add, multiply","*Multiply moduli, add arguments","Subtract, divide","Divide, subtract"],"Multiplication rule."),
    ("To divide complex numbers in polar form, _____ moduli and _____ arguments.",["Multiply, add","*Divide moduli, subtract arguments","Add, multiply","Subtract, divide"],"Division rule."),
    ("De Moivre's Theorem: [r(cos θ + i sin θ)]ⁿ = :",["rⁿ(cos θ + i sin θ)","*rⁿ(cos nθ + i sin nθ)","nr(cos θ + i sin θ)","r(cos nθ + i sin nθ)"],"Power rule."),
    ("Using De Moivre's: (cos π/6 + i sin π/6)⁶ = cos ___ + i sin ___ = ",["6π/6","*cos π + i sin π = −1","cos 36 + i sin 36","6"],"6·π/6=π."),
    ("The nth roots of a complex number give _____ equally spaced points on a circle.",["2","*n","n²","1"],"n roots, evenly spaced."),
    ("The cube roots of 1 are:",["Only 1","1 and −1","*1, (−1+i√3)/2, (−1−i√3)/2","0, 1, 2"],"Three roots of unity."),
    ("The polar form of −1 is:",["1(cos 0 + i sin 0)","*1(cos π + i sin π)","1(cos π/2 + i sin π/2)","−1(cos 0 + i sin 0)"],"On negative real axis."),
    ("Euler's formula: e^(iθ) = ",["cos θ − i sin θ","iθ","*cos θ + i sin θ","e^θ"],"Famous formula."),
    ("The complex number 2i in polar form has r = _____ and θ = _____.",["2, 0","*2, π/2","2, π","1, π/2"],"On positive imaginary axis."),
]

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, tuples in EXTRA.items():
    if key not in data:
        print(f"⚠️  {key} not found"); continue
    existing = data[key].get("quiz_questions", [])
    start = len(existing) + 1
    for i, (qt, opts, exp) in enumerate(tuples):
        q = mq(qt, opts, exp)
        q["question_number"] = start + i
        existing.append(q)
    data[key]["quiz_questions"] = existing
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Algebra 2 U7-U9: added questions to {count} lessons")
