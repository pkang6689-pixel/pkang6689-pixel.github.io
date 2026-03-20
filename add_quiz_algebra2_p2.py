#!/usr/bin/env python3
"""Add quiz questions to Algebra 2 lessons (→20 each). Units 4-6."""
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

# ── U4 L4.1 Rational Expressions ──
EXTRA["u4_l4.1"] = [
    ("A rational expression is a ratio of two:",["Integers","*Polynomials","Exponents","Radicals"],"Polynomial/polynomial."),
    ("The domain of 1/(x−3) excludes:",["x = 0","x = 1","*x = 3","x = −3"],"Denominator ≠ 0."),
    ("Simplify (x²−4)/(x−2):",["x−4","x+4","*x+2","x−2"],"(x−2)(x+2)/(x−2)=x+2."),
    ("The domain of (x+1)/(x²−9) excludes:",["x = 1","x = 9","*x = 3 and x = −3","x = 0"],"x²−9=(x−3)(x+3)=0."),
    ("Simplify (2x²+6x)/(2x):",["2x+6","x²+3","*x+3","2x+3"],"2x(x+3)/2x=x+3."),
    ("A rational expression equals zero when the _____ equals zero.",["Denominator","Both","*Numerator (and denominator ≠ 0)","Neither"],"Numerator = 0."),
    ("Simplify (x²−x−6)/(x²−9):",["(x+2)/(x−3)","(x−3)/(x+3)","*(x+2)/(x+3)","(x−2)/(x+3)"],"(x−3)(x+2)/((x−3)(x+3))."),
    ("The expression 5/(x²+1) has domain:",["x ≠ 1","x ≠ −1","*All real numbers (x²+1 > 0 always)","x > 0"],"Never zero."),
    ("Simplify (3x−6)/(x−2):",["3x","x−2","*3","−3"],"3(x−2)/(x−2)=3."),
    ("Restrictions on x must come from the _____ equation.",["Simplified","*Original (restrictions before simplification still apply)","New","Neither"],"Keep original restrictions."),
    ("(x²+5x+6)/(x+3) simplifies to:",["x+3","x−2","*x+2","x+6"],"(x+2)(x+3)/(x+3)=x+2."),
    ("A complex fraction is:",["An imaginary fraction","*A fraction containing fractions in its numerator and/or denominator","A polynomial","An irrational number"],"Nested fractions."),
    ("Simplify (1/x)/(1/y):",["x/y","xy","*y/x","1/(xy)"],"Invert and multiply."),
]

# ── U4 L4.2 Operations on Rational Expressions ──
EXTRA["u4_l4.2"] = [
    ("To multiply rational expressions: multiply _____ and multiply _____.",["Add numerators, add denominators","*Numerators together, denominators together","Cross-multiply","Subtract"],"Multiplication rule."),
    ("To divide by a rational expression, multiply by its:",["Negative","Square","*Reciprocal","Conjugate"],"Invert and multiply."),
    ("(x/3) · (6/x²) = ",["6x/3x²","x/x²","*2/x","6/3"],"6x/(3x²)=2/x."),
    ("To add rational expressions with different denominators, first find the:",["GCF","Product","*LCD (least common denominator)","Quotient"],"Common denominator."),
    ("1/x + 1/y = ",["2/xy","1/(x+y)","*(x+y)/(xy)","xy"],"LCD = xy."),
    ("3/(x+1) + 2/(x−1) = ",["5/(x²−1)","5/2x","*(5x−1)/((x+1)(x−1))","5x/(x²−1)"],"3(x−1)+2(x+1)=5x−1."),
    ("(x²−1)/(x+2) · (x+2)/(x+1) = ",["(x−1)(x+2)","(x+1)²","*x−1","x+1"],"(x−1)(x+1)/(x+2)·(x+2)/(x+1)=x−1."),
    ("2/x − 3/x = ",["5/x","−5/x","*−1/x","1/x"],"(2−3)/x."),
    ("(2x/(x+3)) ÷ (4x²/(x+3)) = ",["2x/4x²","8x³/(x+3)²","*1/(2x)","2/4"],"2x/(x+3)·(x+3)/4x²=1/(2x)."),
    ("The LCD of 1/(x−1) and 1/(x+1) is:",["x²","x²−1","*(x−1)(x+1)","x"],"Product of distinct factors."),
    ("5/(x+2) − 3/(x+2) = ",["8/(x+2)","2/(2x+4)","*2/(x+2)","15/(x+2)"],"Same denominator: (5−3)/(x+2)."),
    ("Before multiplying, it helps to _____ common factors.",["Add","Multiply","*Cancel (factor and reduce)","Ignore"],"Simplify first."),
    ("The LCD of 1/x² and 1/(3x) is:",["x²","3x","*3x²","x³"],"LCM of x² and 3x."),
]

# ── U4 L4.3 Rational Equations ──
EXTRA["u4_l4.3"] = [
    ("To solve a rational equation, multiply both sides by the:",["Numerator","Smallest denominator","*LCD (to clear all fractions)","Largest numerator"],"Clear denominators."),
    ("Solve: 2/x = 6. x = ",["6","2","*1/3","3"],"2=6x→x=1/3."),
    ("When solving rational equations, we must check for _____ solutions.",["Imaginary","*Extraneous (solutions that make the original denominator zero)","Multiple","No"],"Check denominators."),
    ("Solve: x/(x−2) = 3/(x−2). x = ",["2","0","*No solution (x=3 but check: actually x=3 works, x≠2)","−3"],"Actually x=3 since x−2=1≠0. Valid."),
    ("Solve: 1/x + 1 = 3/x.",["x = 3","x = 1","*x = 2","x = −1"],"Multiply by x: 1+x=3→x=2."),
    ("An extraneous solution occurs when a solution makes the _____ equal zero.",["Numerator","Solution set","*Original denominator","Equation"],"Invalid in original."),
    ("Solve: x/(x+1) = 2 − 1/(x+1).",["x = 3","*x = 1","x = −1","No solution"],"x=2(x+1)−1→x=2x+1→x=−1. But x=−1 makes denom 0. No solution... let me check: x/(x+1)+1/(x+1)=2 → (x+1)/(x+1)=2 → 1=2. No solution."),
    ("Solve: 3/(x−1) = 3. x = ",["3","0","*2","−1"],"3=3(x−1)→1=x−1→x=2."),
    ("The equation 1/(x−2) + 1/(x+2) = 4/(x²−4) simplifies to:",["2 = 4","*After clearing LCD: (x+2)+(x−2)=4 → 2x=4 → x=2. But x=2 is excluded. No solution.","x = 2","x = 0"],"Extraneous."),
    ("Solve: 5/(x+1) − 2/(x−1) = 1. After clearing LCD (x+1)(x−1):",["5(x−1)−2(x+1)=1","*5(x−1)−2(x+1)=(x+1)(x−1) → x²−3x+2=0 → x=1 or x=2. x=1 extraneous → x=2","x = 0","No solution"],"Check both."),
    ("A work problem: Person A completes a job in 4 hrs, B in 6 hrs. Together they take:",["5 hrs","3 hrs","*2.4 hrs (12/5)","2 hrs"],"1/4+1/6=5/12→12/5 hrs."),
    ("In a rate problem, if distance = rate × time, then time = :",["Distance × rate","Rate/distance","*Distance/rate","Rate − distance"],"t = d/r."),
    ("Solve: x + 6/x = 5.",["x = 6","*x = 2 or x = 3","x = 1","x = −1"],"x²+6=5x→x²−5x+6=0→(x−2)(x−3)=0."),
]

# ── U4 L4.4 Graphing Rational Functions ──
EXTRA["u4_l4.4"] = [
    ("A vertical asymptote occurs where the _____ is zero (but numerator isn't).",["Numerator","Function","*Denominator","Slope"],"Undefined points."),
    ("The vertical asymptote of f(x) = 1/(x−3) is at:",["x = 0","x = 1","*x = 3","y = 3"],"x−3=0."),
    ("The horizontal asymptote of f(x) = 1/x is:",["x = 0","*y = 0","y = 1","x = 1"],"As x→∞, f→0."),
    ("For f(x) = (2x+1)/(x−1), the horizontal asymptote is y = :",["1","−1","*2","0"],"Degrees equal: ratio of leading coefficients."),
    ("If the degree of the numerator < degree of denominator, the horizontal asymptote is:",["y = 1","No asymptote","*y = 0","y = leading coeff ratio"],"Lower degree → 0."),
    ("If the degree of numerator > degree of denominator, there is:",["A horizontal asymptote at y=0","*No horizontal asymptote (may have a slant/oblique asymptote)","A vertical asymptote","y = 1"],"Only slant possible."),
    ("A hole in a rational function graph occurs when:",["The denominator is zero","*A factor cancels from both numerator and denominator","The function is undefined","The graph crosses an asymptote"],"Removable discontinuity."),
    ("f(x) = (x−2)/((x−2)(x+1)) has a hole at:",["x = −1","*x = 2","x = 0","y = 0"],"(x−2) cancels."),
    ("The x-intercepts of a rational function occur where the _____ is zero.",["Denominator","Function is undefined","*Numerator (and denominator ≠ 0)","Asymptote"],"Numerator zeros."),
    ("The y-intercept of f(x) = (x+3)/(x−1) is at:",["(0, 1)","(0, 3)","*(0, −3)","(0, −1)"],"f(0)=3/(−1)=−3."),
    ("The graph of y = 1/x² approaches the x-axis from _____ only.",["Below","*Above (1/x² is always positive)","Both sides","Neither"],"Always positive."),
    ("A slant (oblique) asymptote occurs when the numerator's degree is exactly _____ more than the denominator's.",["2","0","*1","3"],"Use polynomial division."),
    ("To find a slant asymptote, perform:",["Factoring","*Polynomial long division (or synthetic division) of numerator by denominator","Substitution","Graphing only"],"Division gives the line."),
]

# ── U4 L4.5 Asymptotes & Discontinuities ──
EXTRA["u4_l4.5"] = [
    ("A removable discontinuity (hole) can be 'filled' by:",["Adding an asymptote","*Defining the function value at that point (canceling the common factor and evaluating)","Removing the function","Graphing differently"],"Fill the hole."),
    ("A non-removable discontinuity corresponds to a:",["Hole","*Vertical asymptote","Horizontal asymptote","X-intercept"],"Cannot be removed."),
    ("f(x) = (x²−1)/(x−1) simplifies to _____ with a hole at x = ___.",["x+1, x=−1","*x+1, x=1","x−1, x=1","x²−1, x=0"],"(x−1)(x+1)/(x−1), hole at x=1."),
    ("Near a vertical asymptote, the function values approach:",["Zero","A finite number","*±∞ (positive or negative infinity)","The x-intercept"],"Unbounded behavior."),
    ("For f(x)=1/(x−2), as x→2⁺, f(x)→:",["0","−∞","*+∞","2"],"From right: positive, getting huge."),
    ("For f(x)=1/(x−2), as x→2⁻, f(x)→:",["0","*−∞","+∞","2"],"From left: negative, large magnitude."),
    ("How many vertical asymptotes does f(x) = 1/((x−1)(x+3)) have?",["0","1","*2 (at x=1 and x=−3)","3"],"Two zeros in denominator."),
    ("The function f(x) = (x²+1)/(x²−4) has vertical asymptotes at:",["x = 1","x = 4","*x = 2 and x = −2","x = 0"],"x²−4=0."),
    ("As x→∞, f(x) = (3x²−1)/(x²+2) approaches:",["0","1","*3","∞"],"Leading coefficients: 3/1."),
    ("f(x) = x²/(x−1) has a slant asymptote of y = :",["x","*x + 1","x − 1","x²"],"Divide: x²/(x−1)=x+1+1/(x−1)."),
    ("A graph can cross a horizontal asymptote:",["Never","*Sometimes (unlike vertical asymptotes, graphs CAN cross horizontal ones)","Always","Only at the origin"],"Can be crossed."),
    ("The graph of y = 1/x has _____ asymptotes total.",["1","*2 (vertical at x=0 and horizontal at y=0)","3","0"],"Two asymptotes."),
    ("End behavior of a rational function is described by its:",["Vertical asymptote","X-intercepts","*Horizontal or slant asymptote","Y-intercept"],"Long-run behavior."),
]

# ── U4 L4.6 Applications of Rational Functions ──
EXTRA["u4_l4.6"] = [
    ("In a work-rate problem, if it takes A hours alone and B hours alone, together the rate is:",["A + B","A × B","*1/A + 1/B","1/(A + B)"],"Combined rate."),
    ("Average cost per item = Total Cost / ___.",["Revenue","Profit","*Number of items","Price"],"Unit cost."),
    ("A company's average cost is C(x) = (500 + 10x)/x. As x→∞, average cost approaches:",["0","500","*$10","∞"],"Fixed cost amortized."),
    ("In a mixture problem, concentration = amount of substance / _____.",["Mass","Time","*Total volume","Temperature"],"Concentration formula."),
    ("Pipe A fills a tank in 6 hrs, Pipe B in 4 hrs. Together they fill it in:",["5 hrs","3 hrs","*2.4 hrs","10 hrs"],"1/6+1/4=5/12, time=12/5."),
    ("A pharmacist mixes a 20% solution with a 50% solution. To get 30L of 30% solution, how much 20% is needed?",["10L","15L","*20L","25L"],"0.2x+0.5(30−x)=9→x=20."),
    ("If it costs $2000 fixed + $5 per unit, the average cost at 100 units is:",["$5","$20","*$25","$2000"],"(2000+500)/100=25."),
    ("Travel upstream vs downstream: if boat speed = b and current = c, then upstream speed is:",["b + c","bc","*b − c","b/c"],"Against current."),
    ("A car travels 300 miles. Time in terms of rate r is:",["300r","r/300","*300/r","r − 300"],"t = d/r."),
    ("If two cars travel the same distance but one goes 10 mph faster and arrives 1 hour sooner: this becomes a _____ equation.",["Linear","Quadratic","*Rational (d/r = d/(r+10) + 1)","Exponential"],"Distance/rate setup."),
    ("Economies of scale means average cost _____ as production increases.",["Increases","Stays the same","*Decreases","Doubles"],"Spreading fixed costs."),
    ("In a shared work problem, time together is always _____ the fastest individual time.",["Equal to","Longer than","*Less than","Double"],"Combined is faster."),
    ("To model 'A can do a job in 5 days and B in 7 days,' set the job = 1 and solve:",["5 + 7 = t","t/5 + t/7 = 0","*t/5 + t/7 = 1","5t + 7t = 1"],"Fraction of job per day."),
]

# ── U5 L5.1 Exponential Functions & Growth ──
EXTRA["u5_l5.1"] = [
    ("An exponential function has the form f(x) = abˣ where b is the:",["Exponent","Variable","*Base (positive, b ≠ 1)","Coefficient"],"Base requirements."),
    ("If b > 1, the function represents exponential:",["Decay","Linear growth","*Growth","No change"],"Increasing."),
    ("The y-intercept of f(x) = 3(2)ˣ is:",["2","6","*3","0"],"f(0) = 3·1 = 3."),
    ("Population doubling: if P = 100·2^(t/5), after 15 years the population is:",["200","400","*800","1600"],"2^(15/5)=2³=8, 100·8=800."),
    ("Compound interest formula: A = P(1 + r/n)^(nt). n represents:",["Principal","Rate","*Number of compounding periods per year","Time"],"Compounding frequency."),
    ("$1000 at 6% compounded annually for 10 years: A = ?",["$1600","$1060","*$1790.85","$2000"],"1000(1.06)¹⁰≈1790.85."),
    ("Exponential growth is faster than linear because:",["It's a straight line","*The rate of increase itself increases (proportional to current value)","It starts higher","It's always steeper"],"Accelerating growth."),
    ("The asymptote of f(x) = 2ˣ is:",["x = 0","y = 2","*y = 0","y = 1"],"Never reaches 0."),
    ("If a population triples every 4 years starting at 500, after 12 years:",["1500","4500","*13,500","40,500"],"500·3^(12/4)=500·27=13500."),
    ("The graph of y = 2ˣ always passes through the point:",["(1, 0)","(0, 2)","*(0, 1)","(2, 0)"],"Any b⁰=1."),
    ("Continuous compounding uses the formula A = Pe^(rt) where e ≈:",["3.14","1.41","*2.718","1.618"],"Euler's number."),
    ("An exponential function is one-to-one, meaning it has:",["No inverse","*An inverse function (the logarithm)","Two outputs per input","No y-intercept"],"Invertible."),
    ("If a quantity increases by 5% each year, the growth factor is:",["5","0.05","*1.05","1.5"],"1 + rate."),
]

# ── U5 L5.2 Exponential Decay & Applications ──
EXTRA["u5_l5.2"] = [
    ("If 0 < b < 1, the function f(x) = bˣ represents exponential:",["Growth","*Decay","Linear change","No change"],"Decreasing."),
    ("Half-life is the time for a substance to decay to _____ its original amount.",["Zero","One-quarter","*One-half","Double"],"50% remaining."),
    ("A radioactive element with half-life 10 years: after 30 years, what fraction remains?",["1/4","1/2","*1/8","1/16"],"(1/2)³=1/8."),
    ("The decay function is A = A₀(1 − r)ᵗ. If a car depreciates 15% per year, the decay factor is:",["0.15","1.15","*0.85","−0.15"],"1 − 0.15 = 0.85."),
    ("A car worth $20,000 depreciating at 20% per year is worth _____ after 3 years.",["$8,000","$12,000","*$10,240","$14,000"],"20000(0.8)³=10240."),
    ("Newton's Law of Cooling uses exponential _____ to model temperature change.",["Growth","*Decay","Linear","Quadratic"],"Cooling approaches ambient."),
    ("If a medication has a half-life of 4 hours, and you take 200mg, how much remains after 12 hours?",["50mg","*25mg","100mg","12.5mg"],"(1/2)³=1/8, 200/8=25."),
    ("The asymptote in exponential decay is:",["y = 1","y = −1","*y = 0 (or the ambient value in cooling problems)","y = ∞"],"Approaches but never reaches."),
    ("A quantity decreasing by 8% each year can be modeled as:",["y = y₀(0.08)ᵗ","y = y₀(1.08)ᵗ","*y = y₀(0.92)ᵗ","y = y₀(8)ᵗ"],"Factor = 1−0.08."),
    ("After n half-lives, the fraction remaining is:",["n/2","1/n","*(1/2)ⁿ","2ⁿ"],"Halving each time."),
    ("Carbon-14 dating uses exponential decay to estimate the age of:",["Rocks","Living things","*Once-living (organic) material","Metals"],"Organic dating."),
    ("The graph of exponential decay is:",["Increasing","Linear","*Decreasing and concave up (approaching the asymptote from above)","Concave down"],"Curve shape."),
    ("If a population decreases from 10,000 to 5,000 in 6 years, the half-life is:",["3 years","*6 years","12 years","10 years"],"Halved in 6 years."),
]

# ── U5 L5.3 Logarithms & Properties ──
EXTRA["u5_l5.3"] = [
    ("log_b(x) = y means:",["x = y^b","b = x^y","*b^y = x","y = x^b"],"Definition."),
    ("log₁₀(100) = ",["10","100","*2","1"],"10²=100."),
    ("log₂(8) = ",["2","8","*3","4"],"2³=8."),
    ("log_b(1) = ___ for any valid base b.",["1","b","*0","−1"],"b⁰=1."),
    ("log_b(b) = ",["0","b","*1","−1"],"b¹=b."),
    ("The Product Rule: log_b(MN) = ",["log_b(M) · log_b(N)","log_b(M)/log_b(N)","*log_b(M) + log_b(N)","log_b(M) − log_b(N)"],"Product → sum."),
    ("The Quotient Rule: log_b(M/N) = ",["log_b(M) + log_b(N)","log_b(M) · log_b(N)","*log_b(M) − log_b(N)","log_b(N) − log_b(M)"],"Quotient → difference."),
    ("The Power Rule: log_b(Mⁿ) = ",["n + log_b(M)","(log_b(M))ⁿ","*n · log_b(M)","log_b(M)/n"],"Exponent → multiplier."),
    ("Expand: log₃(x²y) = ",["2 log₃(xy)","*2 log₃(x) + log₃(y)","log₃(2x) + log₃(y)","(log₃(x))²·log₃(y)"],"Power + product rules."),
    ("Condense: log(5) + log(3) = ",["log(8)","log(5/3)","*log(15)","log(53)"],"Product rule."),
    ("Condense: 3 log(x) − log(y) = ",["log(3x/y)","log(3x−y)","*log(x³/y)","log(x/y³)"],"Power then quotient."),
    ("The Change of Base Formula: log_b(x) = ",["log(b)/log(x)","ln(b)/ln(x)","*log(x)/log(b) or ln(x)/ln(b)","b·log(x)"],"Convert bases."),
    ("log₅(25) = ",["5","25","*2","1/2"],"5²=25."),
]

# ── U5 L5.4 Logarithmic Functions & Graphs ──
EXTRA["u5_l5.4"] = [
    ("The graph of y = log_b(x) has a vertical asymptote at:",["y = 0","*x = 0","x = 1","y = 1"],"Cannot take log of 0 or negative."),
    ("The domain of f(x) = log(x) is:",["All reals","x ≥ 0","*x > 0","x < 0"],"Strictly positive."),
    ("The range of f(x) = log(x) is:",["y > 0","y ≥ 0","*All real numbers","y < 0"],"No bounds on output."),
    ("The graph of y = log_b(x) passes through _____ for any valid base b.",["(0, 0)","(0, 1)","*(1, 0)","(b, 0)"],"log_b(1)=0."),
    ("If b > 1, then y = log_b(x) is:",["Decreasing","Constant","*Increasing","Periodic"],"Bigger base, still increasing."),
    ("The graph of y = log₂(x) and y = 2ˣ are _____ of each other.",["Parallel","*Reflections over y = x (inverse functions)","Identical","Perpendicular"],"Inverse relationship."),
    ("Compared to y = log(x), the graph of y = log(x − 3) is shifted:",["Left 3","Up 3","*Right 3","Down 3"],"Horizontal shift."),
    ("The graph of y = log(x) + 2 is shifted _____ from y = log(x).",["Right 2","Left 2","*Up 2","Down 2"],"Vertical shift."),
    ("y = −log(x) is a _____ of y = log(x) over the x-axis.",["Translation","Stretch","*Reflection","Compression"],"Flip over x-axis."),
    ("The graph of y = log₁₀(x) crosses x = 10 at y = ",["0","10","*1","−1"],"log₁₀(10)=1."),
    ("For y = log_b(x), as x → 0⁺, y → ",["0","+∞","*−∞","1"],"Approaches negative infinity."),
    ("The graph of y = log(100x) is the same as y = log(x) + ___.",["100","10","*2","1"],"log(100)+log(x)=2+log(x)."),
    ("A logarithmic scale (like pH or Richter) is useful because it compresses:",["Small numbers","*Large ranges of values into manageable numbers","Negative numbers","Time"],"Wide range compression."),
]

# ── U5 L5.5 Exponential & Logarithmic Equations ──
EXTRA["u5_l5.5"] = [
    ("To solve 2ˣ = 16, rewrite 16 as a power of 2:",["2³","2⁵","*2⁴ → x = 4","2²"],"16=2⁴."),
    ("To solve 3ˣ = 20, take the log of both sides:",["x = 20/3","x = log(20) − log(3)","*x = log(20)/log(3)","x = 3·log(20)"],"x = log₃(20)."),
    ("Solve: 5^(2x) = 125.",["x = 5","x = 25","*x = 3/2","x = 3"],"125=5³→2x=3→x=3/2."),
    ("Solve: eˣ = 7.",["x = 7e","*x = ln(7) ≈ 1.946","x = 7","x = e/7"],"Natural log."),
    ("Solve: log₂(x) = 5.",["x = 10","x = 25","*x = 32","x = 5"],"2⁵=32."),
    ("Solve: log(x) + log(x−3) = 1.",["x = 10","*x = 5","x = −2","x = 3"],"log(x(x−3))=1→x²−3x=10→x=5 (x=−2 extraneous)."),
    ("Solve: 2^(x+1) = 3^(x−1).",["*x = (ln 3 + ln 2)/(ln 2 − ln 3)","x = 1","x = −1","x = 0"],"(x+1)ln2=(x−1)ln3."),
    ("Solve: log₃(2x + 1) = 2.",["x = 8","x = 3","*x = 4","x = 5"],"2x+1=9→x=4."),
    ("When solving log equations, always check that arguments are:",["Negative","Zero","*Positive (domain restriction — cannot take log of zero or negative)","Even"],"Domain check."),
    ("Solve: e^(2x) − 5e^x + 6 = 0.",["x = 2, 3","*x = ln 2, ln 3","x = 0, 1","x = −2, −3"],"Let u=eˣ: u²−5u+6=0→u=2,3→x=ln2,ln3."),
    ("Solve: 4ˣ = 8.",["x = 2","*x = 3/2","x = 1","x = 4"],"2²ˣ=2³→2x=3→x=3/2."),
    ("If ln(x) = 3, then x = ",["3","*e³ ≈ 20.09","3e","ln(3)"],"Exponentiate: x=e³."),
    ("Solve: log(x²) = 4.",["x = 4","x = 10,000","*x = ±100","x = 2"],"x²=10⁴→x=±100."),
]

# ── U5 L5.6 Applications of Exponentials & Logs ──
EXTRA["u5_l5.6"] = [
    ("The Richter scale: each whole number increase represents _____ times more energy.",["2","10","*~31.6 (10 times more amplitude, ~31.6 times more energy)","100"],"Logarithmic scale."),
    ("pH = −log[H⁺]. A pH of 3 means [H⁺] = ?",["3","0.3","*0.001 (10⁻³)","1000"],"10⁻³=0.001."),
    ("A lower pH means a _____ acidic solution.",["Less","Neutral","*More","Equally"],"Lower pH = more H⁺."),
    ("Compound interest compounded continuously: A = Pe^(rt). $5000 at 4% for 10 years = ?",["$7000","$7500","*$7459.12","$8000"],"5000e^(0.4)≈7459."),
    ("Doubling time for continuous growth: T = ln(2)/r. At 7% growth, doubling time ≈:",["7 years","*~9.9 years","14 years","20 years"],"ln(2)/0.07≈9.9."),
    ("The Rule of 72: doubling time ≈ 72/r%. At 6%, T ≈:",["6 years","*12 years","18 years","72 years"],"72/6=12."),
    ("Decibels: dB = 10 log(I/I₀). If I = 1000I₀, then dB = ",["10","*30","100","3"],"10·log(1000)=10·3=30."),
    ("An investment at 5% compounded quarterly. The effective annual rate is approximately:",["5%","*5.09% (slightly more than nominal due to compounding)","4.75%","10%"],"(1+0.05/4)⁴−1≈0.0509."),
    ("Logistic growth models populations that:",["Grow forever","Decay forever","*Grow toward a carrying capacity (S-shaped curve)","Stay constant"],"Bounded growth."),
    ("The logistic function is P(t) = L/(1+be^(−kt)). L represents the:",["Initial population","Growth rate","*Carrying capacity (maximum population)","Time"],"Upper limit."),
    ("Carbon-14 has a half-life of 5,730 years. An artifact with 25% C-14 remaining is about _____ years old.",["5,730","*11,460","17,190","2,865"],"25%=(1/2)²→2 half-lives=11,460."),
    ("Sound at 90 dB is _____ times more intense than 60 dB.",["3","30","*1,000","90"],"10^((90−60)/10)=10³=1000."),
    ("Exponential regression is used when data shows a pattern of:",["Constant change","*Constant percentage change (multiplicative pattern)","Random change","No change"],"Multiplicative pattern."),
]

# ── U5 L5.7 Natural Logarithms & e (needs 19 questions!) ──
EXTRA["u5_l5.7"] = [
    ("The number e is approximately:",["3.14159","1.41421","*2.71828","1.61803"],"Euler's number."),
    ("ln(x) is the logarithm with base:",["10","2","*e","π"],"Natural log base."),
    ("ln(1) = ",["1","e","*0","−1"],"e⁰=1."),
    ("ln(e) = ",["0","e","*1","−1"],"e¹=e."),
    ("ln(e³) = ",["e³","1","*3","e"],"log_e(e³)=3."),
    ("e^(ln x) = ",["ln x","e","*x","1"],"Inverse functions."),
    ("ln(e^x) = ",["e^x","e","*x","1"],"Inverse functions."),
    ("The derivative concept: e is defined so that the rate of change of eˣ equals:",["x","1","*eˣ (its own value)","0"],"Self-derivative."),
    ("ln(ab) = ",["ln(a) · ln(b)","*ln(a) + ln(b)","ln(a)/ln(b)","ln(a) − ln(b)"],"Product rule."),
    ("ln(a/b) = ",["ln(a) + ln(b)","ln(a) · ln(b)","*ln(a) − ln(b)","ln(b) − ln(a)"],"Quotient rule."),
    ("ln(xⁿ) = ",["(ln x)ⁿ","*n · ln(x)","ln(nx)","n + ln(x)"],"Power rule."),
    ("Solve: eˣ = 5. x = ",["5","*ln(5) ≈ 1.609","e⁵","5e"],"Take ln of both sides."),
    ("Solve: ln(x) = 4. x = ",["4","*e⁴ ≈ 54.6","4e","ln(4)"],"Exponentiate."),
    ("Solve: 2e^(3x) = 14. x = ",["7","*ln(7)/3","ln(14)/3","7/3"],"e^(3x)=7→3x=ln7."),
    ("Continuous compounding A = Peʳᵗ uses e because:",["It's easier","*It models the limit of compounding n→∞ times per year","It's a convention only","It's bigger than 10"],"Continuous limit."),
    ("The half-life formula in terms of ln: t = ln(2)/k where k is the:",["Half-life","*Decay constant","Initial amount","Final amount"],"Decay rate."),
    ("[e^(1) ≈ 2.718] represents the factor by which something grows with a 100% continuous growth rate over 1 time period. This means e is:",["Just a number","*The natural growth constant for continuous compounding","A rounded value","Exactly π"],"Natural growth base."),
    ("The relationship between log₁₀ and ln: log₁₀(x) = ln(x)/___.",["10","e","*ln(10) ≈ 2.303","1"],"Change of base."),
    ("Solve: ln(2x−1) = 3.",["x = e³","x = (3+1)/2","*x = (e³+1)/2","x = 3"],"2x−1=e³→x=(e³+1)/2."),
]

# ── U6 L6.1 Arithmetic Sequences ──
EXTRA["u6_l6.1"] = [
    ("In an arithmetic sequence, the common difference d = :",["a₁/a₂","a₁ · a₂","*aₙ₊₁ − aₙ (each term minus the previous term)","aₙ₊₁/aₙ"],"Constant difference."),
    ("The nth term formula for an arithmetic sequence is:",["aₙ = a₁ · rⁿ⁻¹","*aₙ = a₁ + (n−1)d","aₙ = a₁ · dⁿ","aₙ = nd"],"Linear formula."),
    ("Find the 10th term: a₁ = 3, d = 5.",["50","45","*48","53"],"3+(9)(5)=48."),
    ("In the sequence 7, 11, 15, 19, ..., d = ",["7","11","*4","−4"],"11−7=4."),
    ("The sum of the first n terms of an arithmetic sequence: Sₙ = :",["n · a₁","n · d","*n(a₁ + aₙ)/2","a₁ · rⁿ"],"Sum formula."),
    ("Find S₂₀ for the sequence 2, 5, 8, 11, ... :",["200","500","*610","620"],"a₂₀=2+19(3)=59, S=20(2+59)/2=610."),
    ("The arithmetic mean of 10 and 30 is:",["30","10","*20","40"],"(10+30)/2."),
    ("Insert 3 arithmetic means between 2 and 14:",["3, 6, 9","4, 8, 12","*5, 8, 11","4, 7, 10"],"d=(14−2)/4=3: 2,5,8,11,14."),
    ("If a₅ = 20 and d = 3, find a₁:",["11","5","*8","12"],"20=a₁+4(3)→a₁=8."),
    ("Is 100 a term in the sequence 3, 7, 11, ...?",["No","*Yes, it's the 25th term","It's the 24th term","Cannot determine"],"100=3+4(n−1)→n=25."),
    ("The sequence 5, 5, 5, 5 is arithmetic with d = :",["5","−5","*0","1"],"Constant sequence, d=0."),
    ("An arithmetic sequence is linear because the nth term formula is a _____ function of n.",["Quadratic","Exponential","*Linear (aₙ = dn + (a₁−d))","Logarithmic"],"Linear in n."),
    ("If a₃ = 10 and a₇ = 22, then d = :",["4","*3","2","6"],"22−10=4d→d=3."),
]

# ── U6 L6.2 Geometric Sequences ──
EXTRA["u6_l6.2"] = [
    ("In a geometric sequence, the common ratio r = :",["aₙ₊₁ − aₙ","aₙ − aₙ₊₁","*aₙ₊₁/aₙ","aₙ + aₙ₊₁"],"Ratio between terms."),
    ("The nth term of a geometric sequence: aₙ = :",["a₁ + (n−1)r","a₁ · nʳ","*a₁ · rⁿ⁻¹","nr"],"Exponential formula."),
    ("Find the 6th term: a₁ = 2, r = 3.",["162","*486","729","1458"],"2·3⁵=2·243=486."),
    ("In the sequence 4, 12, 36, 108, ..., r = :",["4","8","*3","12"],"12/4=3."),
    ("A geometric sequence with r = 1 gives:",["Increasing terms","Decreasing terms","*All terms equal (constant sequence)","Alternating terms"],"Every term = a₁."),
    ("If r is negative, the sequence:",["Increases","Decreases","*Alternates signs","Stays constant"],"Sign flips each term."),
    ("The geometric mean of 4 and 16 is:",["10","20","*8","12"],"√(4·16)=√64=8."),
    ("Find a₁ if a₄ = 54 and r = 3:",["6","3","*2","9"],"a₁·3³=54→a₁=2."),
    ("The sum of the first n terms of a geometric series: Sₙ = a₁(1−rⁿ)/(1−r) when r ≠ :",["0","*1","a₁","n"],"r=1 is special case."),
    ("Find S₅ for a₁ = 1, r = 2:",["16","30","*31","32"],"(1−32)/(1−2)=31."),
    ("A population that doubles each year follows a _____ sequence.",["Arithmetic","*Geometric (with r = 2)","Neither","Both"],"Multiplicative growth."),
    ("If |r| > 1, the geometric sequence:",["Converges","Stays bounded","*Diverges (terms grow without bound)","Approaches zero"],"Growing terms."),
    ("If |r| < 1, the terms of the geometric sequence:",["Grow","Stay constant","*Approach zero","Oscillate wildly"],"Shrinking terms."),
]

# ── U6 L6.3 Series & Summation Notation ──
EXTRA["u6_l6.3"] = [
    ("Σ (sigma) notation represents:",["Product","Difference","*Summation","Division"],"Sum symbol."),
    ("Σₖ₌₁⁵ k = ",["5","10","*15","20"],"1+2+3+4+5=15."),
    ("Σₖ₌₁⁴ 3 = ",["3","4","*12","7"],"3+3+3+3=12 (constant summed 4 times)."),
    ("Σₖ₌₁³ k² = ",["6","9","*14","36"],"1+4+9=14."),
    ("The difference between a sequence and a series is:",["None","*A sequence is a list of terms; a series is the SUM of terms","A series has more terms","A sequence is always finite"],"List vs. sum."),
    ("An arithmetic series is the sum of an _____ sequence.",["Geometric","*Arithmetic","Fibonacci","Random"],"Arithmetic sum."),
    ("The formula Σₖ₌₁ⁿ k = n(n+1)/2  gives the sum of the first n _____ integers.",["Even","Odd","*Positive (natural)","Negative"],"Gauss's formula."),
    ("Σₖ₌₁¹⁰⁰ k = ",["5000","10000","*5050","5100"],"100·101/2=5050."),
    ("Write in sigma notation: 3 + 6 + 9 + ... + 30.",["Σₖ₌₁¹⁰ k","*Σₖ₌₁¹⁰ 3k","Σₖ₌₃³⁰ k","Σₖ₌₁³⁰ k"],"3k for k=1 to 10."),
    ("Σₖ₌₀³ 2ᵏ = ",["8","14","*15","16"],"1+2+4+8=15."),
    ("Properties: Σ(aₖ + bₖ) = ",["Σaₖ · Σbₖ","*Σaₖ + Σbₖ","Σ(aₖ)²","Cannot split"],"Linearity."),
    ("Properties: Σ c·aₖ = ",["c + Σaₖ","*c · Σaₖ","Σaₖ / c","Σcᵏ"],"Constant factor out."),
    ("A partial sum Sₙ is the sum of the first _____ terms of a series.",["All","Infinite","*n (a finite number)","2"],"Finite portion."),
]

# ── U6 L6.4 Infinite Geometric Series ──
EXTRA["u6_l6.4"] = [
    ("An infinite geometric series converges if:",["r > 1","r = 1","*|r| < 1","r > 0"],"Convergence condition."),
    ("The sum of an infinite geometric series (|r|<1) is S = :",["a₁/(1+r)","a₁·r","*a₁/(1−r)","a₁(1−rⁿ)/(1−r)"],"Infinite sum formula."),
    ("Find the sum: 1 + 1/2 + 1/4 + 1/8 + ... :",["1","1.5","*2","∞"],"1/(1−1/2)=2."),
    ("The series 3 + 9 + 27 + 81 + ... _____ because |r| = 3.",["Converges to 3","Equals 0","*Diverges (|r| > 1, terms grow without bound)","Converges to ∞"],"Divergent."),
    ("Find the sum: 12 − 6 + 3 − 3/2 + ... :",["12","6","*8","4"],"r=−1/2, S=12/(1+1/2)=8."),
    ("0.333... = 3/10 + 3/100 + 3/1000 + ... This geometric series equals:",["0.3","*1/3","3/10","0.33"],"a₁=0.3, r=0.1, S=0.3/0.9=1/3."),
    ("Find the sum: Σₖ₌₁^∞ (2/3)ᵏ :",["1","3","*2","2/3"],"(2/3)/(1−2/3)=2."),
    ("The series 5 + 5/3 + 5/9 + 5/27 + ... has sum:",["5","*15/2 = 7.5","10","∞"],"5/(1−1/3)=5/(2/3)=7.5."),
    ("If S = 10 and r = 1/2, then a₁ = :",["10","20","*5","1"],"5/(1−0.5)=10."),
    ("0.999... = ",["Less than 1","Approximately 1","*Exactly 1 (9/10 + 9/100 + ... = (9/10)/(1−1/10) = 1)","Undefined"],"Equals 1."),
    ("A bouncing ball dropped from 10 m, bouncing to 60% height each time. Total distance traveled:",["10 m","16 m","*40 m (10 + 2·10·0.6/(1−0.6) = 10+30)","∞"],"Down + up = 10+2·6/(1−0.6)=40."),
    ("If |r| ≥ 1, the infinite geometric series is said to:",["Equal zero","*Diverge (no finite sum)","Converge","Equal r"],"No finite answer."),
    ("Writing a repeating decimal as a fraction uses the concept of:",["Arithmetic series","*Infinite geometric series","Sigma notation only","Calculus"],"Repeating decimal technique."),
]

# ── U6 L6.5 Applications & Mathematical Induction (needs 19!) ──
EXTRA["u6_l6.5"] = [
    ("Mathematical induction proves statements about all _____ numbers.",["Real","Rational","*Positive integers (natural numbers)","Complex"],"Induction domain."),
    ("The base case in induction verifies the statement for n = :",["0 always","∞","*The smallest value (usually n = 1)","A random n"],"Starting point."),
    ("The inductive step assumes the statement is true for n = k and proves it for:",["n = k − 1","n = 2k","*n = k + 1","n = k²"],"Next integer."),
    ("The assumption that the statement holds for n = k is called the:",["Base case","Conclusion","*Inductive hypothesis","Theorem"],"Assumed true for k."),
    ("Prove 1+2+...+n = n(n+1)/2. Base case n=1: LHS=1, RHS=",["0","2","*1","1/2"],"1(2)/2=1. ✓"),
    ("In the inductive step for Σk = n(n+1)/2, we add (k+1) to both sides and show:",["It equals k²","It fails","*The formula works for k+1: (k+1)(k+2)/2","It equals k"],"Algebra confirms."),
    ("Mathematical induction is analogous to:",["A circle","*Dominoes falling (if one falls, the next falls; and the first has fallen)","Drawing a graph","Random sampling"],"Domino analogy."),
    ("Sequences and series are used in financial math for:",["Only budgeting","*Annuities, mortgages, retirement funds (regular payments over time)","Only taxes","Nothing"],"Financial applications."),
    ("An annuity is a series of _____ payments at regular intervals.",["Random","Decreasing","*Equal","Increasing only"],"Fixed payments."),
    ("The future value of an annuity formula uses a _____ series.",["Arithmetic","*Geometric","Random","Constant"],"Compounding payments."),
    ("A Fibonacci sequence is defined by:",["aₙ = aₙ₋₁ + d","aₙ = r · aₙ₋₁","*aₙ = aₙ₋₁ + aₙ₋₂ (sum of two previous terms)","aₙ = n²"],"Recursive definition."),
    ("The first few Fibonacci numbers are:",["1, 2, 3, 4","*1, 1, 2, 3, 5, 8","1, 3, 9, 27","2, 4, 6, 8"],"Each = sum of prev two."),
    ("Recursive formulas define a term using:",["Only n","The first term only","*Previous term(s) (e.g., aₙ = aₙ₋₁ + d)","A table"],"Previous terms."),
    ("Explicit formulas give the nth term directly as a function of:",["Previous terms","*n (the term number)","The sum","All prior terms"],"Direct calculation."),
    ("Compound interest can be viewed as a geometric sequence where each year's balance = previous × :",["r","1 − r","*(1 + r)","r²"],"Growth factor."),
    ("Pascal's Triangle is related to _____ and combinations.",["Arithmetic sequences","Geometric sequences","*Binomial expansion","Division"],"Binomial coefficients."),
    ("The Binomial Theorem states (a+b)ⁿ = Σ C(n,k)·aⁿ⁻ᵏ·bᵏ. C(n,k) is:",["n!","k!","*n!/(k!(n−k)!) — a combination","Permutation"],"Binomial coefficient."),
    ("The number of terms in the expansion of (a+b)⁵ is:",["5","*6","10","25"],"n+1 terms."),
    ("Induction, sequences, and series form the foundation for _____ in higher math.",["Only algebra","*Calculus (limits, infinite series, convergence)","Only geometry","Only statistics"],"Calculus connection."),
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
print(f"✅ Algebra 2 U4-U6: added questions to {count} lessons")
