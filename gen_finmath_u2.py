#!/usr/bin/env python3
"""Financial Math Unit 2 – Interest & Banking (8 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "financial_math_lessons.json")
COURSE = "Financial Math"

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for qi, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2,
                    "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": COURSE,
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# 2.1
k,v = build_lesson(2,1,"Simple Interest Formula",
    "<h3>Simple Interest</h3>"
    "<p>Simple interest is calculated <b>only</b> on the original principal.</p>"
    "<h4>Formula</h4>"
    "<p><b>I = P × r × t</b></p>"
    "<ul><li><b>I</b> = interest earned (or owed)</li>"
    "<li><b>P</b> = principal (initial amount)</li>"
    "<li><b>r</b> = annual interest rate (as decimal)</li>"
    "<li><b>t</b> = time in years</li></ul>"
    "<p>Total amount: <b>A = P + I = P(1 + rt)</b></p>"
    "<p>Example: $1,000 at 5% for 3 years → I = $1,000 × 0.05 × 3 = $150. Total = $1,150.</p>",
    [("Simple Interest","Interest calculated only on the original principal: I = P × r × t."),
     ("Principal (P)","The original amount of money deposited or borrowed before interest."),
     ("Interest Rate (r)","The percentage charged or earned per year, expressed as a decimal in formulas (e.g., 5% = 0.05)."),
     ("Time (t)","Duration in years for the interest calculation (convert months with t = months ÷ 12)."),
     ("Total Amount (A)","Principal plus interest: A = P(1 + rt) for simple interest.")],
    [("The simple interest formula is:",["I = Prt²","*I = Prt","I = P(1+r)^t","I = Pe^rt"],"Basic formula."),
     ("Simple interest is calculated on:",["Principal plus interest","*Only the original principal (not on previously earned interest)","Compound amounts","Only for the first year"],"On principal only."),
     ("$2,000 at 6% simple interest for 4 years earns:",["$240","$360","*$480 (I = 2000 × 0.06 × 4)","$600"],"2000 × 0.06 × 4."),
     ("The total amount after $2,000 at 6% for 4 years (simple) is:",["$2,360","*$2,480 (A = 2000 + 480)","$2,600","$2,240"],"P + I."),
     ("To convert 8% to a decimal for the formula:",["Multiply by 100","Leave as 8","*Divide by 100 → 0.08","Divide by 10"],"Rate conversion."),
     ("$5,000 at 3% for 6 months earns _____ in simple interest.",["$150","$300","*$75 (I = 5000 × 0.03 × 0.5)","$90"],"t = 0.5 years."),
     ("If you borrow $10,000 at 7% simple interest for 2 years, you owe:",["$10,700","$11,000","*$11,400 (A = 10000(1 + 0.07×2))","$12,000"],"A = P(1+rt)."),
     ("Simple interest grows:",["Exponentially","*Linearly (same amount of interest each period)","Logarithmically","Randomly"],"Constant growth."),
     ("If $800 earns $120 in simple interest at 5%, the time was:",["2 years","*3 years (t = I/(Pr) = 120/(800×0.05))","4 years","5 years"],"Solve for t."),
     ("If $1,500 earns $225 in 3 years of simple interest, the rate is:",["3%","4%","*5% (r = I/(Pt) = 225/(1500×3) = 0.05)","6%"],"Solve for r."),
     ("What principal earns $400 at 8% simple interest in 2 years?",["$1,600","$2,000","*$2,500 (P = I/(rt) = 400/(0.08×2))","$3,200"],"Solve for P."),
     ("Simple interest is commonly used for:",["Savings accounts","*Short-term loans, car loans, and some bonds (Treasury bills, some corporate bonds)","Mortgages","Credit cards"],"Short-term applications."),
     ("The maturity value of a simple interest loan is:",["Only the principal","Only the interest","*The principal plus total interest (the final amount due at the end of the loan term)","The monthly payment"],"Total amount due."),
     ("$3,000 at 4.5% simple interest for 18 months equals:",["$3,135","*$3,202.50 (I = 3000 × 0.045 × 1.5 = $202.50)","$3,270","$3,405"],"Convert months to years."),
     ("Simple interest is _____ favorable for borrowers compared to compound interest.",["Less","*More (you pay less total interest with simple since it doesn't compound)","Equally","Never"],"Borrower advantage."),
     ("The graph of simple interest over time is a:",["Curve","*Straight line (linear growth)","Parabola","Exponential curve"],"Linear relationship."),
     ("If two loans have the same rate and principal but one is simple and one is compound, the compound loan costs:",["Less","The same","*More (because interest earns interest in compound)","Depends on time only"],"Compound costs more."),
     ("Treasury bills (T-bills) use simple interest because they:",["Are risky","*Are short-term investments (usually < 1 year) where simple interest is standard","Pay high interest","Are compound"],"Short-term standard."),
     ("The formula rearranged to find rate is:",["r = PIt","*r = I / (P × t)","r = P / (I × t)","r = t / (P × I)"],"Algebra rearrangement."),
     ("Understanding simple interest is important because it:",["Is the only interest type","*Provides the foundation for understanding compound interest and all other financial calculations","Is used everywhere","Applies only to savings"],"Foundation concept.")]
)
lessons[k]=v

# 2.2
k,v = build_lesson(2,2,"Compound Interest Formula",
    "<h3>Compound Interest</h3>"
    "<p>Compound interest is calculated on the principal <b>plus</b> accumulated interest.</p>"
    "<h4>Formula</h4>"
    "<p><b>A = P(1 + r/n)^(nt)</b></p>"
    "<ul><li><b>A</b> = final amount</li>"
    "<li><b>P</b> = principal</li>"
    "<li><b>r</b> = annual rate (decimal)</li>"
    "<li><b>n</b> = compounding periods per year</li>"
    "<li><b>t</b> = time in years</li></ul>"
    "<p>Example: $1,000 at 5% compounded monthly for 3 years → A = 1000(1 + 0.05/12)^(12×3) = $1,161.62</p>",
    [("Compound Interest","Interest calculated on principal plus all previously accumulated interest: A = P(1 + r/n)^(nt)."),
     ("Compounding Frequency (n)","How often interest is calculated per year: annually (1), semi-annually (2), quarterly (4), monthly (12), daily (365)."),
     ("APY (Annual Percentage Yield)","The effective annual rate accounting for compounding — always ≥ APR for the same nominal rate."),
     ("Compounding Period","Each interval after which interest is calculated and added to the balance."),
     ("Future Value","The value of an investment at a specific future date, accounting for compound interest growth.")],
    [("The compound interest formula is:",["A = Prt","*A = P(1 + r/n)^(nt)","A = Pe^rt","A = P + Prt"],"Key formula."),
     ("Compound interest earns interest on:",["Only principal","*Both principal AND previously earned interest","Only the first year's interest","Only new deposits"],"Growth on growth."),
     ("$1,000 at 6% compounded annually for 5 years gives:",["$1,300","*$1,338.23 (A = 1000(1.06)^5)","$1,060","$1,250"],"Annual compounding."),
     ("$1,000 at 6% compounded monthly for 5 years gives:",["$1,338.23","*$1,348.85 (A = 1000(1+0.06/12)^60)","$1,300","$1,060"],"Monthly compounding."),
     ("For quarterly compounding, n equals:",["1","2","*4","12"],"4 quarters per year."),
     ("More frequent compounding results in:",["Less interest","The same interest","*More total interest (though with diminishing additional benefit as frequency increases)","Less principal"],"Higher frequency = more growth."),
     ("$5,000 at 4% compounded semi-annually for 3 years equals:",["$5,600","*$5,630.81 (A = 5000(1+0.02)^6)","$5,612","$5,650"],"n=2, nt=6."),
     ("APY (Annual Percentage Yield) is always _____ APR when compounding more than once per year.",["Less than","Equal to","*Greater than or equal to","Double"],"Effective rate ≥ nominal rate."),
     ("APY for 12% compounded monthly is:",["12%","*12.68% (APY = (1+0.12/12)^12 − 1)","13%","11%"],"Effective rate calculation."),
     ("The total interest earned on $1,000 at 5% compounded annually for 10 years is:",["$500","*$628.89 (A = 1000(1.05)^10 = 1628.89; I = 628.89)","$550","$750"],"Compound interest earned."),
     ("Compound interest compared to simple interest over the same period gives:",["The same amount","Less money","*More money (the difference grows dramatically over longer periods)","Depends on the rate only"],"Compound > simple."),
     ("$10,000 at 8% compounded quarterly for 10 years equals approximately:",["$18,000","$20,000","*$21,911 (A = 10000(1+0.02)^40)","$25,000"],"Quarterly compounding."),
     ("If A = $15,000 and P = $10,000 at 5% compounded annually, the time is approximately:",["5 years","*~8.3 years (solve 1.5 = 1.05^t → t = ln(1.5)/ln(1.05))","10 years","15 years"],"Solve for t using logs."),
     ("The Rule of 72 approximates doubling time as:",["72 × r","*72 ÷ r (where r is the annual rate as a percentage)","72 + r","72 − r"],"Quick estimate."),
     ("At 6% annual return, money doubles in approximately:",["6 years","*12 years (72 ÷ 6)","18 years","72 years"],"Rule of 72 applied."),
     ("$2,000 at 3% compounded daily for 1 year gives approximately:",["$2,060","*$2,060.90 (very close to continuous compounding at this rate)","$2,030","$2,090"],"Daily compounding."),
     ("The difference between annual and daily compounding matters most when:",["Interest rate is low","Time is short","*Interest rate is high AND time is long","It never matters"],"Rate × time amplifies difference."),
     ("To find the principal needed to reach $50,000 in 20 years at 6% compounded monthly:",["Multiply","*P = A/(1+r/n)^(nt) = 50000/(1.005)^240 ≈ $15,128","Divide by 20","Subtract interest"],"Solve for P (present value)."),
     ("Compound interest is used in:",["Only savings accounts","*Savings accounts, investments, loans, credit cards, mortgages, and retirement accounts","Only loans","Only investments"],"Everywhere in finance."),
     ("The most important variable in compound interest is often:",["The rate alone","The principal alone","*Time (because exponential growth accelerates dramatically over longer periods)","The compounding frequency alone"],"Time is the multiplier.")]
)
lessons[k]=v

# 2.3
k,v = build_lesson(2,3,"Continuous Compounding",
    "<h3>Continuous Compounding</h3>"
    "<p>When interest compounds infinitely often, we use the continuous compounding formula:</p>"
    "<p><b>A = Pe^(rt)</b></p>"
    "<ul><li><b>e</b> ≈ 2.71828 (Euler's number)</li>"
    "<li>This is the mathematical limit of (1 + r/n)^(nt) as n → ∞</li></ul>"
    "<p>Example: $1,000 at 5% continuously for 3 years → A = 1000e^(0.05×3) = 1000e^0.15 = $1,161.83</p>",
    [("Continuous Compounding","Interest compounded infinitely often: A = Pe^(rt), where e ≈ 2.71828."),
     ("Euler's Number (e)","Mathematical constant ≈ 2.71828; base of the natural logarithm; limit of (1+1/n)^n as n→∞."),
     ("Natural Logarithm (ln)","The inverse of e^x; used to solve for time or rate in continuous compounding: t = ln(A/P)/r."),
     ("Continuous Growth Rate","The rate at which a quantity grows when modeled with continuous compounding."),
     ("Limit of Compounding","As compounding frequency n→∞, A = P(1+r/n)^(nt) approaches A = Pe^(rt).")],
    [("The continuous compounding formula is:",["A = Prt","A = P(1+r/n)^nt","*A = Pe^(rt)","A = P + Prt"],"Exponential formula."),
     ("Euler's number e is approximately:",["3.14159","1.41421","*2.71828","2.00000"],"Mathematical constant."),
     ("$2,000 at 4% compounded continuously for 5 years equals:",["$2,400","*$2,442.81 (A = 2000e^(0.04×5) = 2000e^0.2)","$2,500","$2,300"],"Continuous compounding."),
     ("Continuous compounding yields _____ than daily compounding.",["Significantly more","Less","*Slightly more (the difference is very small in practice)","Exactly the same"],"Marginal difference."),
     ("The natural log (ln) is used in continuous compounding to:",["Calculate principal","Find interest","*Solve for time or rate [e.g., t = ln(A/P)/r]","Convert to simple interest"],"Solving equations."),
     ("How long to double money at 6% continuous compounding?",["10 years","*~11.55 years (t = ln(2)/0.06 = 0.6931/0.06)","12 years","15 years"],"ln(2)/r."),
     ("$10,000 at 7% continuous compounding for 10 years equals:",["$17,000","$19,000","*$20,137.53 (10000 × e^0.7)","$22,000"],"e^0.7 ≈ 2.01375."),
     ("Continuous compounding is the mathematical limit of increasing:",["Principal","Rate","*Compounding frequency (n → ∞)","Time"],"Infinite compounding."),
     ("In practice, continuous compounding is used in:",["All bank accounts","*Mathematical modeling, some bonds, and theoretical finance (academic and pricing models)","Only savings","Only loans"],"Theoretical and specialized use."),
     ("The effective annual rate for 5% continuous compounding is:",["5%","*5.127% (e^0.05 − 1 = 0.05127)","5.25%","4.88%"],"e^r − 1."),
     ("If A = $3,000 and P = $2,000 at continuous 8%, time is:",["3 years","4 years","*~5.07 years (t = ln(1.5)/0.08)","6 years"],"Solve with ln."),
     ("What rate doubles money in 10 years with continuous compounding?",["5%","6%","*~6.93% (r = ln(2)/10)","8%"],"r = ln(2)/t."),
     ("Compared to annual compounding, continuous compounding at the same rate gives:",["Much more","Less","*Slightly more (the maximum possible for that rate)","The same"],"Upper bound of compounding."),
     ("$500 at 3% continuous for 20 years gives:",["$800","*$911.06 (500e^0.6)","$1,000","$750"],"500 × e^0.6."),
     ("The graph of continuous compounding is:",["A straight line","*A smooth exponential curve","A step function","A parabola"],"Smooth growth."),
     ("Population growth models often use continuous compounding because:",["It's simpler","*Growth occurs at every moment, not at discrete intervals — continuous models better represent biological growth","It's more accurate for finance","All populations grow continuously"],"Natural modeling."),
     ("For investment comparison, the key is APY because it:",["Ignores compounding","*Accounts for compounding frequency — allowing fair comparison between different compounding schedules","Is always the same as APR","Only matters for continuous"],"Standardized comparison."),
     ("The formula A = Pe^rt assumes:",["Interest stops compounding","*Interest compounds instantaneously and continuously, with no interruption","Only annual compounding","Simple interest"],"Continuous assumption."),
     ("If a bank offers 4.9% compounded daily vs. 5% compounded annually, the better deal is:",["5% annual definitely","*4.9% daily (APY ≈ 5.02% vs. 5.00% — daily compounding overcomes the lower nominal rate)","They're identical","Cannot determine"],"APY comparison."),
     ("Understanding continuous compounding is valuable because it:",["Is only for advanced math","*Connects financial math to calculus, modeling, and pricing theory (Black-Scholes), and represents the upper bound of compounding","Has no practical use","Only matters in physics"],"Mathematical + practical significance.")]
)
lessons[k]=v

# 2.4
k,v = build_lesson(2,4,"Growth vs. Decay Models",
    "<h3>Exponential Growth &amp; Decay in Finance</h3>"
    "<h4>Growth: A = P(1 + r)^t</h4>"
    "<p>Investments, savings, economic growth — amount <b>increases</b> over time.</p>"
    "<h4>Decay: A = P(1 − r)^t</h4>"
    "<p>Depreciation, inflation erosion, declining values — amount <b>decreases</b> over time.</p>"
    "<p>Example (depreciation): Car purchased for $30,000 depreciating at 15%/year → After 5 years: 30000(1−0.15)^5 = $13,312</p>",
    [("Exponential Growth","Amount increases by a fixed percentage each period: A = P(1+r)^t (investments, savings)."),
     ("Exponential Decay","Amount decreases by a fixed percentage each period: A = P(1−r)^t (depreciation, purchasing power)."),
     ("Depreciation","The decrease in value of an asset over time (cars, equipment, buildings) — typically modeled as exponential decay."),
     ("Purchasing Power","What a dollar can actually buy — decreases over time due to inflation (decay of money's value)."),
     ("Half-Life (Financial)","Time for an asset to lose half its value: t = ln(0.5)/ln(1−r).")],
    [("Exponential growth uses the formula:",["A = P(1−r)^t","*A = P(1+r)^t","A = Prt","A = P−rt"],"Increasing over time."),
     ("Exponential decay uses the formula:",["A = P(1+r)^t","*A = P(1−r)^t","A = Prt","A = P+rt"],"Decreasing over time."),
     ("A car purchased for $30,000 depreciating at 15% annually is worth _____ after 5 years.",["$15,000","*~$13,312 (30000 × 0.85^5)","$22,500","$7,500"],"Depreciation calculation."),
     ("$50,000 investment growing at 7% annually for 10 years becomes:",["$57,000","$85,000","*~$98,358 (50000 × 1.07^10)","$100,000"],"Growth calculation."),
     ("Inflation at 3% means $100 of purchasing power becomes _____ after 10 years.",["$97","$85","*~$74.41 (100 × 0.97^10)","$70"],"Purchasing power decay."),
     ("A computer purchased for $2,000 depreciating at 30%/year is worth _____ after 3 years.",["$600","$980","*$686 (2000 × 0.70^3)","$1,400"],"Rapid depreciation."),
     ("The key difference between growth and decay formulas is:",["The exponent","*The sign inside the parentheses: (1+r) for growth, (1−r) for decay","The principal","The time"],"Plus vs. minus."),
     ("Doubling time for growth at rate r is approximately:",["r/72","72 × r","*72/r (Rule of 72)","r × t"],"Quick estimate."),
     ("Half-life for decay at rate r of 10% is approximately:",["72/10 = 7.2 years","*~6.6 years (ln(0.5)/ln(0.9))","10 years","5 years"],"Decay halving time."),
     ("A painting appreciating at 5% annually from $10,000 is worth _____ after 20 years.",["$20,000","*~$26,533 (10000 × 1.05^20)","$30,000","$15,000"],"Art appreciation."),
     ("Negative interest rates (rare but real) would cause savings to:",["Grow","*Decay (your bank actually charges you to hold money — A = P(1−|r|)^t)","Stay the same","Double"],"Value erosion."),
     ("Which asset typically depreciates?",["Real estate","*Cars (new cars lose ~20% in the first year, ~60% over 5 years)","Gold","Stocks long-term"],"Cars depreciate."),
     ("Which asset typically appreciates over time?",["Cars","Electronics","*Real estate (historically, though not guaranteed)","Clothing"],"Property typically gains value."),
     ("A population of bacteria doubling every hour (growth rate 100%) from 100 bacteria reaches _____ after 8 hours.",["800","*25,600 (100 × 2^8)","1,600","51,200"],"Doubling calculation."),
     ("Radioactive decay and financial depreciation share the pattern of:",["Linear decrease","*Exponential decrease (same mathematical model, different contexts)","Constant loss","No pattern"],"Same math, different domains."),
     ("If an item loses half its value every 5 years, after 10 years it's worth _____ of the original.",["50%","*25% (halved twice)","10%","75%"],"Two half-lives."),
     ("Inflation is an example of:",["Growth of money","*Decay of purchasing power (prices grow, but your money's buying power shrinks)","Neither growth nor decay","Only in economics"],"Value erosion."),
     ("A savings account earning 2% with inflation at 3% has a real return of:",["2%","3%","*−1% (your purchasing power is actually decreasing)","5%"],"Nominal − inflation."),
     ("Modeling financial growth and decay requires understanding:",["Only linear functions","*Exponential functions: both growth and decay follow A = P(1±r)^t patterns","Only simple interest","Only compound interest"],"Exponential modeling."),
     ("For financial math, growth vs. decay models apply to:",["Only investments","*Investments (growth), depreciation (decay), inflation (decay of value), and population/economic modeling","Only one application","Only textbook problems"],"Wide application.")]
)
lessons[k]=v

# 2.5
k,v = build_lesson(2,5,"Applications in Savings Accounts",
    "<h3>Savings Account Applications</h3>"
    "<h4>Types of Savings Vehicles</h4>"
    "<ul><li><b>Regular savings:</b> Low interest (~0.01–0.5% at traditional banks).</li>"
    "<li><b>High-yield savings:</b> ~4–5% APY (online banks, 2024).</li>"
    "<li><b>Certificates of Deposit (CDs):</b> Fixed rate for fixed term; higher rate for longer terms.</li>"
    "<li><b>Money market accounts:</b> Higher rates than regular savings; may have check-writing privileges.</li></ul>"
    "<h4>FDIC Insurance</h4>"
    "<p>US bank deposits insured up to $250,000 per depositor per institution.</p>",
    [("High-Yield Savings Account","Online savings accounts offering significantly higher APY (~4–5%) than traditional bank accounts."),
     ("Certificate of Deposit (CD)","Time deposit earning a fixed interest rate for a fixed term; early withdrawal incurs a penalty."),
     ("Money Market Account","Savings account offering higher interest than regular savings, often with limited check-writing."),
     ("FDIC Insurance","Federal Deposit Insurance Corporation protects bank deposits up to $250,000 per depositor per institution."),
     ("APY vs. APR","APY includes compounding (what you earn); APR does not (what you're charged on loans).")],
    [("Regular savings accounts at traditional banks typically earn:",["5%","*~0.01–0.5% APY (significantly below inflation)","10%","3%"],"Very low rates."),
     ("High-yield savings accounts (2024) offer approximately:",["0.5%","2%","*~4–5% APY","10%"],"Much higher online rates."),
     ("A CD differs from a savings account in that it:",["Can be withdrawn anytime","*Locks money for a fixed term at a fixed rate; early withdrawal incurs a penalty","Always earns less","Has no FDIC insurance"],"Fixed term commitment."),
     ("FDIC insurance covers up to _____ per depositor per institution.",["$100,000","*$250,000","$500,000","$1,000,000"],"Deposit protection limit."),
     ("$10,000 in a high-yield savings at 4.5% APY earns approximately _____ in one year.",["$45","$145","*$450","$4,500"],"10000 × 0.045."),
     ("$10,000 in a regular savings at 0.05% APY earns approximately _____ in one year.",["$50","$25","$10","*$5"],"10000 × 0.0005."),
     ("CD laddering involves:",["Buying one long-term CD","*Spreading money across CDs with different maturity dates to balance higher rates with regular access","Only short-term CDs","Never using CDs"],"Balanced strategy."),
     ("Money market accounts typically offer:",["The lowest rates","*Higher rates than regular savings with some check-writing ability, often with higher minimum balances","The highest rates","No interest"],"Middle-ground option."),
     ("The opportunity cost of keeping $20,000 in a 0.05% savings vs. 4.5% high-yield is approximately:",["$100/year","*~$890/year in lost interest","$45/year","$2,000/year"],"20000 × (0.045−0.0005)."),
     ("If inflation is 3% and your savings earns 4.5%, your real return is:",["4.5%","3%","*~1.5% (nominal rate − inflation rate)","−1.5%"],"Real return after inflation."),
     ("If inflation is 3% and your savings earns 0.5%, your real return is:",["0.5%","3%","*−2.5% (your money loses purchasing power)","3.5%"],"Losing to inflation."),
     ("$5,000 in a 2-year CD at 5% compounded monthly becomes:",["$5,500","*$5,524.70 (5000(1+0.05/12)^24)","$5,250","$5,100"],"CD calculation."),
     ("The early withdrawal penalty for a CD typically equals:",["Nothing","*Several months of interest (varies: 3–12 months depending on CD term)","The entire principal","Half the principal"],"Penalty for breaking term."),
     ("Treasury I-bonds are attractive because they:",["Are risky","*Adjust for inflation (composite rate = fixed rate + inflation rate), protecting purchasing power","Have no interest","Are only for institutions"],"Inflation protection."),
     ("For emergency funds, the best savings vehicle is usually:",["Long-term CD","*High-yield savings account (liquid, FDIC-insured, decent return, no penalty for withdrawal)","Stocks","Crypto"],"Accessible + earning."),
     ("Compound interest on savings is typically calculated:",["Annually only","*Daily (most banks compound daily and pay monthly)","Weekly","Quarterly only"],"Common compounding."),
     ("When comparing savings accounts, the most important metric is:",["The bank's reputation","*APY (Annual Percentage Yield — includes compounding frequency for accurate comparison)","The bank's location","Minimum balance only"],"APY for comparison."),
     ("Savings accounts at credit unions:",["Are not insured","*Are insured by NCUA (similar to FDIC, up to $250,000) and often offer competitive rates","Don't earn interest","Are for businesses only"],"NCUA-insured."),
     ("The purpose of saving in these accounts is:",["Maximum growth","*Safety and liquidity — protecting principal and earning some return while keeping money accessible","High-risk/high-return","Only for emergencies"],"Safe and accessible."),
     ("For financial math, savings applications demonstrate:",["Only one formula","*Simple and compound interest formulas applied to real products with real-world considerations (FDIC, inflation, liquidity)","Only theoretical concepts","Only for wealthy people"],"Theory meets practice.")]
)
lessons[k]=v

# 2.6
k,v = build_lesson(2,6,"Comparing Interest Scenarios",
    "<h3>Comparing Interest Scenarios</h3>"
    "<h4>Key Comparisons</h4>"
    "<ul><li><b>Simple vs. compound:</b> $10,000 at 5% for 20 years: Simple = $20,000; Compound (annual) = $26,533; Compound (monthly) = $27,126.</li>"
    "<li><b>Different rates:</b> $10,000 for 30 years: at 6% = $57,435; at 8% = $100,627; at 10% = $174,494.</li>"
    "<li><b>Starting early vs. late:</b> $100/month at 8% for 40 years = $349,101; for 20 years = $58,902.</li></ul>",
    [("Annual vs. Monthly Compounding","Monthly compounding yields more than annual at the same nominal rate; difference grows with time and rate."),
     ("Rate Sensitivity","Small differences in interest rates create enormous differences in outcomes over long periods."),
     ("Time Sensitivity","More time dramatically increases compound interest — the most powerful variable in wealth building."),
     ("Effective Annual Rate","The actual annual rate after accounting for compounding; used to compare different compounding frequencies."),
     ("Present Value vs. Future Value","Present value: what a future amount is worth today; Future value: what today's money will be worth in the future.")],
    [("$10,000 at 5% simple interest for 20 years yields:",["$15,000","*$20,000 (I = 10000 × 0.05 × 20 = $10,000; A = $20,000)","$25,000","$30,000"],"Simple interest total."),
     ("$10,000 at 5% compound (annual) for 20 years yields approximately:",["$20,000","*$26,533","$30,000","$35,000"],"Compound annual total."),
     ("The difference between simple and compound at 5% for 20 years on $10,000 is:",["$0","*~$6,533 (compound earns 33% more)","$1,000","$10,000"],"Compound advantage."),
     ("$10,000 at 6% for 30 years vs. 8% for 30 years: the 2% difference means:",["About $10,000 more","*$100,627 vs. $57,435 — the 8% is nearly double (2% difference = ~$43,000 more over 30 years)","No significant difference","Triple the amount"],"Rate sensitivity."),
     ("$100/month at 8% for 40 years accumulates approximately:",["$48,000","$100,000","$200,000","*~$349,101"],"Long-term regular investing."),
     ("$100/month at 8% for 20 years (half the time) accumulates:",["$175,000","*~$58,902 (less than 1/6 of the 40-year amount despite contributing half as much)","$100,000","$24,000"],"Time's dramatic effect."),
     ("Comparing 4% compounded daily vs. 4.1% compounded annually, the better option is:",["Always 4.1% annual","*4.1% annual (APY ≈ 4.1%) beats 4% daily (APY ≈ 4.08%) — rate matters more than frequency at similar rates","Always daily","They're identical"],"Rate usually dominates."),
     ("Present value of $100,000 needed in 20 years at 7% annually is:",["$100,000","$50,000","*~$25,842 (PV = FV/(1+r)^t)","$75,000"],"Today's equivalent."),
     ("The 'Rule of 72' says money at 9% doubles in:",["9 years","*8 years (72/9)","12 years","6 years"],"Quick estimate."),
     ("$1,000 at 12% for 30 years vs. $10,000 at 6% for 30 years:",["$10,000 always wins","*$1,000 at 12% wins ($29,960 vs. $17,449) — rate beats initial amount given enough time","They're equal","Cannot determine"],"Rate × time vs. principal."),
     ("Monthly compounding vs. annual compounding matters most when:",["Rate is very low","Time is very short","*Rate is high AND time is long (both amplify compounding frequency effects)","It never matters"],"Amplification conditions."),
     ("The '10× rule' shows that 10% compounded annual return turns $10,000 into _____ in ~24 years.",["$50,000","*~$100,000 (doubles approximately every 7.2 years; 24/7.2 ≈ 3.3 doublings)","$200,000","$30,000"],"Exponential growth."),
     ("If Bank A offers 4.5% APY and Bank B offers 4.4% compounded daily:",["Bank B is definitely better","*Bank A (APY already accounts for compounding; 4.5% APY > 4.4% compounded daily, which has APY ≈ 4.497%)","They're equal","Cannot compare"],"APY is the standard."),
     ("The total contributed in $100/month for 40 years is:",["$100,000","$24,000","*$48,000 (but it grew to ~$349,101 — compound interest earned ~$301,000!)","$349,101"],"Contributions vs. growth."),
     ("Starting with $0 and saving $500/month at 7% for 30 years yields approximately:",["$180,000","$350,000","*~$567,000","$1,000,000"],"Consistent saving."),
     ("The most important lesson from interest comparisons is:",["All rates are equal","All time periods are equal","*Small differences in rate and time create enormous differences in outcomes due to exponential growth","Only large amounts matter"],"Exponential sensitivity."),
     ("When choosing between investments, the most relevant comparison metric is:",["Nominal rate","*APY or effective annual rate (accounts for compounding so you compare apples to apples)","Bank name","Account type"],"Standardized metric."),
     ("Tax-advantaged accounts (IRA, 401k) amplify compounding because:",["They earn more interest","*Growth is tax-deferred or tax-free, so the full return compounds (no drag from annual taxes on gains)","They have special rates","They're risk-free"],"Tax-free compounding."),
     ("Inflation-adjusted returns are important because:",["Inflation doesn't matter","*A 10% return with 3% inflation is really ~7% real growth in purchasing power","Inflation helps investors","Only nominal returns matter"],"Real vs. nominal."),
     ("For financial math tests, comparison problems require:",["Only one calculation","*Computing multiple scenarios and clearly explaining which option is better and why","Only plugging in formulas","Only naming formulas"],"Calculate and compare.")]
)
lessons[k]=v

# 2.7
k,v = build_lesson(2,7,"Case Studies in Banking",
    "<h3>Case Studies in Banking</h3>"
    "<h4>Case 1: Traditional vs. Online Banking</h4>"
    "<p>Sarah has $25,000 in emergency savings. Traditional bank: 0.05% APY = $12.50/year. Online high-yield: 4.5% APY = $1,125/year. Difference: $1,112/year for the same FDIC-insured money.</p>"
    "<h4>Case 2: CD Strategy</h4>"
    "<p>Mike uses a CD ladder: $10,000 split into 5 CDs (1-5 year terms). As each matures, he reinvests at the longest term. Balances access with higher rates.</p>",
    [("Online vs. Traditional Banking","Online banks offer 10-100× higher savings rates than traditional banks due to lower overhead costs."),
     ("CD Ladder","Strategy of dividing deposits across CDs with staggered maturity dates to balance rate and access."),
     ("Opportunity Cost of Low-Rate Savings","Keeping money in a 0.05% account vs. 4.5% on $25,000 costs ~$1,112/year in lost earnings."),
     ("Bank Fees","Maintenance fees, overdraft fees, ATM fees — can erode returns if not managed (choose fee-free options)."),
     ("Compound Growth Over a Lifetime","Consistent savings + compound interest over 40+ years builds substantial wealth from modest contributions.")],
    [("Sarah's $25,000 in a 0.05% traditional savings earns _____ per year.",["$125","$1,250","*$12.50","$0.50"],"Nearly nothing."),
     ("The same $25,000 in a 4.5% high-yield savings earns _____ per year.",["$112.50","$450","*$1,125","$2,500"],"Significant difference."),
     ("By switching to the high-yield account, Sarah gains approximately _____ per year.",["$100","$500","*~$1,112","$2,500"],"1125 − 12.50."),
     ("Over 10 years, SarahÕs switching decision saves her approximately:",["$1,112","$5,000","*~$12,000+(with compounding, even more)","$100"],"Compounding amplifies."),
     ("A CD ladder with $10,000 across 5 CDs of 1-5 year terms provides:",["Only the highest rate","*Regular access (one CD matures each year) while earning higher long-term CD rates","Only short-term rates","No access"],"Best of both worlds."),
     ("Overdraft fees average _____ per occurrence at major banks.",["$5","$15","*~$35","$100"],"Expensive penalty."),
     ("Monthly bank maintenance fees of $12/month cost _____ per year.",["$12","$72","*$144","$240"],"Fee awareness."),
     ("If monthly fees of $12 are invested at 8% instead for 30 years, they'd grow to:",["$4,320","*~$17,700 (144/yr invested monthly at 8%)","$10,000","$50,000"],"Opportunity cost of fees."),
     ("The FDIC insures deposits at both traditional and online banks, so moving to a high-yield account:",["Increases risk","Decreases safety","*Carries the same safety as a traditional bank (both FDIC-insured to $250,000)","Voids protection"],"Same safety, better return."),
     ("A case study of someone keeping $50,000 in checking at 0% vs. splitting to $5,000 checking and $45,000 high-yield at 4.5% shows:",["No benefit","*~$2,025/year in additional earnings with minimal inconvenience","Only $100 more","Too much hassle"],"Optimize idle cash."),
     ("Compound interest on a $500/month savings habit at 4.5% for 5 years totals:",["$30,000","*~$33,400 ($3,400 in interest on $30,000 in contributions)","$35,000","$40,000"],"Regular savings + interest."),
     ("A case study of someone who saved $300/month starting at age 25 vs. age 35 (at 7%) by age 65 shows:",["Similar amounts","*$25: ~$720,000 vs. $35: ~$340,000 — the 10-year head start more than doubled the result","Only $50,000 difference","Starting age doesn't matter"],"Early start advantage."),
     ("Promotional bank rates (e.g., 'earn 5% for 6 months') should be evaluated based on:",["Only the promo rate","*What happens AFTER the promotional period (rate often drops significantly)","Only the bank's name","Only the sign-up bonus"],"Read the fine print."),
     ("Savings account interest is taxed as:",["Tax-free","Capital gains","*Ordinary income (at your marginal tax rate — reported on 1099-INT)","Only if over $10,000"],"Taxable income."),
     ("A comparison of checking, savings, money market, and CD shows that:",["All are equal","*Each serves a different purpose: checking for daily use, savings for emergency, money market for higher-rate liquid savings, CDs for fixed-term higher rates","Only one type is needed","CDs are always best"],"Right tool for purpose."),
     ("Automatic transfers from checking to savings help because:",["They're required","*They enforce the pay-yourself-first habit without relying on willpower","They earn more interest","The bank requires them"],"Automation wins."),
     ("Choosing the right bank depends on:",["Only location","Only rates","*Rates, fees, access (ATMs, mobile banking), customer service, FDIC/NCUA insurance, and account features","Only reputation"],"Multi-factor decision."),
     ("Case studies in banking illustrate that small rate differences:",["Don't matter","*Compound into significant money over time — being intentional about where you bank has real financial impact","Only matter for the wealthy","Only matter for large sums"],"Details matter."),
     ("The overall lesson from banking case studies is:",["All banks are the same","*Where you keep your money matters — choosing wisely and managing fees can be worth thousands of dollars per year","Only interest rates matter","Only fees matter"],"Intentional banking."),
     ("For financial math, these case studies apply _____ to real banking decisions.",["Only theory","*Compound interest formulas, APY comparisons, and opportunity cost analysis","Only simple interest","Nothing practical"],"Math meets real life.")]
)
lessons[k]=v

# 2.8
k,v = build_lesson(2,8,"Technology Tools for Interest Calculations",
    "<h3>Technology for Interest Calculations</h3>"
    "<h4>Tools</h4>"
    "<ul><li><b>Spreadsheets (Excel/Sheets):</b> FV(), PV(), RATE(), NPER(), PMT() functions built-in.</li>"
    "<li><b>Financial calculators:</b> TI BA II Plus, HP 12C — input N, I/Y, PV, PMT, FV.</li>"
    "<li><b>Online calculators:</b> Bankrate, NerdWallet, Investor.gov compound interest calculators.</li>"
    "<li><b>Programming:</b> Python, JavaScript for custom financial modeling.</li></ul>",
    [("FV() Function","Spreadsheet function calculating future value: =FV(rate, nper, pmt, pv) — returns future value of investment."),
     ("PV() Function","Spreadsheet function calculating present value: =PV(rate, nper, pmt, fv) — what a future amount is worth today."),
     ("PMT() Function","Spreadsheet function calculating payment: =PMT(rate, nper, pv) — regular payment needed to reach a goal."),
     ("TVM Variables","Time Value of Money: N (periods), I/Y (interest/year), PV (present value), PMT (payment), FV (future value)."),
     ("Financial Modeling","Using technology to build what-if scenarios comparing different financial options and assumptions.")],
    [("The Excel function for future value is:",["=INTEREST()","=COMPOUND()","*=FV(rate, nper, pmt, [pv])","=GROWTH()"],"Built-in FV function."),
     ("In =FV(0.005, 120, -200, -5000), the 0.005 represents:",["The annual rate","*The monthly rate (6%/12 = 0.005)","The total interest","The number of periods"],"Rate per period."),
     ("The PMT payment is entered as a negative number in Excel because it represents:",["An error","*A cash outflow (money leaving your account)","A discount","A tax"],"Cash flow convention."),
     ("To find how much you need to save monthly to reach $100,000 in 20 years at 7%, use:",["=FV()","=PV()","*=PMT(0.07/12, 240, 0, -100000)","=RATE()"],"Payment function."),
     ("The NPER() function calculates:",["Number of payments made","*The number of periods needed to reach a goal (how long it will take)","The interest rate","The amount per period"],"Time to goal."),
     ("The RATE() function calculates:",["Payments","Time","*The interest rate per period needed to achieve a goal","Future value"],"Required rate."),
     ("On a financial calculator, the five TVM keys are:",["Only P and I","*N, I/Y, PV, PMT, FV","Only FV and PV","A, B, C, D, E"],"Standard TVM keys."),
     ("What-if analysis in spreadsheets allows you to:",["Only see one scenario","*Change assumptions (rate, time, contribution) and instantly see how outcomes change","Only graph results","Only format cells"],"Scenario comparison."),
     ("A sensitivity analysis shows how:",["Nothing changes","*Changing one variable (e.g., interest rate from 5% to 10%) affects the outcome across a range of values","Only totals change","Only one answer exists"],"Variable impact testing."),
     ("Data tables in Excel can show:",["Only one calculation","*Multiple scenarios simultaneously (e.g., outcomes for 5%, 6%, 7%, 8% across 10, 20, 30 years)","Only text","Only charts"],"Multi-variable comparison."),
     ("Amortization schedules in spreadsheets show:",["Only the final payment","*Each payment broken down into principal and interest components over the life of a loan","Only the total cost","Only the monthly payment"],"Detailed payment breakdown."),
     ("Goal Seek in Excel can find:",["Only formatting","*The input value needed to achieve a specific result (e.g., what rate is needed to reach $500,000 in 25 years)","Only graphs","Only totals"],"Reverse engineering."),
     ("Online compound interest calculators are useful because they:",["Replace all other tools","*Provide quick, visual calculations without needing spreadsheet skills — good for basic comparisons","Are always the most accurate","Are the only option"],"Quick accessibility."),
     ("Python for financial modeling allows:",["Nothing Excel can't do","*Custom calculations, complex simulations, Monte Carlo analysis, and automation beyond basic spreadsheet capabilities","Only simple interest","Only one calculation"],"Advanced modeling."),
     ("When using technology tools, it's important to:",["Trust every result blindly","*Verify results with manual calculations or estimates to catch input errors","Only use one tool","Avoid manual calculations entirely"],"Verify outputs."),
     ("The most common error in financial calculator use is:",["Pressing wrong buttons","*Forgetting to clear previous values (leftover inputs from prior calculations give wrong answers)","Using the wrong calculator","Entering the rate correctly"],"Clear before new calculations."),
     ("Graphing compound interest in spreadsheets helps visualize:",["Only a number","*The 'hockey stick' shape of exponential growth — slow at first, accelerating dramatically over time","Only linear growth","Only short-term results"],"Visual understanding."),
     ("Cloud-based financial tools (Google Sheets) offer the advantage of:",["Lower accuracy","*Accessibility from anywhere, real-time collaboration, and automatic saving","Only working offline","Only for businesses"],"Modern accessibility."),
     ("Financial technology literacy means:",["Knowing every app","*Being able to use spreadsheets, calculators, and online tools to model and compare financial scenarios","Only using apps","Avoiding technology"],"Applied digital skills."),
     ("For financial math courses, technology tools connect formulas to:",["Only theoretical problems","*Real-world applications by enabling quick comparison of multiple scenarios and sensitivity analysis","Only grades","Only one topic"],"Theory → practice.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 2: wrote {len(lessons)} lessons")
