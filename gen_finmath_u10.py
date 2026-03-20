#!/usr/bin/env python3
"""Financial Math Unit 10 – Review & AP Prep (7 lessons)."""
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

# 10.1
k,v = build_lesson(10,1,"Review of Key Formulas",
    "<h3>Key Financial Math Formulas</h3>"
    "<h4>Time Value of Money</h4>"
    "<ul><li>FV = PV × (1 + r)^n</li>"
    "<li>PV = FV / (1 + r)^n</li>"
    "<li>Rule of 72: Years to double ≈ 72 / rate</li></ul>"
    "<h4>Business Math</h4>"
    "<ul><li>Break-even (units) = Fixed Costs / (Price − Variable Cost)</li>"
    "<li>Profit Margin = Net Profit / Revenue × 100</li>"
    "<li>ROI = (Gain − Cost) / Cost × 100</li></ul>"
    "<h4>Investment Math</h4>"
    "<ul><li>NPV = −Investment + Σ(CF_t / (1+r)^t)</li>"
    "<li>Sharpe Ratio = (Return − Risk-free) / Std Dev</li>"
    "<li>WACC = (% Debt × Cost of Debt × (1−Tax)) + (% Equity × Cost of Equity)</li></ul>",
    [("FV = PV(1+r)^n","Future value formula: how much a present sum grows with compound interest over n periods at rate r."),
     ("PV = FV/(1+r)^n","Present value formula: today's equivalent of a future sum, discounted at rate r for n periods."),
     ("Break-Even = FC / CM","Break-even units = Fixed Costs ÷ Contribution Margin per unit (Price minus Variable Cost)."),
     ("NPV = −I₀ + Σ CF/(1+r)^t","Net Present Value: sum of all discounted future cash flows minus the initial investment."),
     ("Sharpe = (R−Rf)/σ","Sharpe ratio: excess return per unit of risk; higher = better risk-adjusted performance.")],
    [("FV of $5,000 at 6% for 20 years =",["$10,000","$12,000","*$16,036 (5000 × 1.06^20)","$20,000"],"FV calculation."),
     ("PV of $100,000 in 25 years at 8% =",["$50,000","$20,000","*$14,602 (100000 / 1.08^25)","$10,000"],"PV calculation."),
     ("Rule of 72: at 9%, money doubles in _____ years.",["6","*8 (72/9)","10","12"],"Rule of 72."),
     ("Simple interest: $20,000 at 5% for 3 years = $20,000 + ($20,000 × 0.05 × 3) =",["$21,000","$22,000","*$23,000","$24,000"],"SI = PRT."),
     ("Compound interest on same ($20K, 5%, 3yr) = $20,000 × (1.05)^3 =",["$23,000","*$23,153","$23,500","$24,000"],"CI > SI."),
     ("Break-even: Fixed $50K, price $80, variable $30. Units = 50000/(80−30) =",["500","*1,000","1,500","2,000"],"BEP."),
     ("Profit margin: $200K revenue, $150K expenses. Margin = $50K/$200K =",["30%","20%","*25%","35%"],"Margin calculation."),
     ("ROI: bought for $10K, sold for $15K. ROI = ($15K−$10K)/$10K =",["25%","*50%","75%","100%"],"ROI."),
     ("Monthly mortgage payment: use PMT formula. $300K, 6.5%, 30yr ≈",["$1,500","*~$1,896","$2,100","$2,500"],"PMT calculation."),
     ("Total interest on that mortgage: ($1,896 × 360) − $300,000 =",["$100,000","$250,000","*~$382,560","$500,000"],"Total interest."),
     ("NPV: −$100K investment + $30K/yr for 5 years at 10%. PV of annuity ≈ $113,724. NPV =",["$0","*$13,724","$30,000","$100,000"],"NPV calculation."),
     ("IRR is the rate where NPV = 0. If NPV is positive at 10%, IRR is _____ 10%.",["Below","Exactly","*Above (positive NPV means actual return exceeds the discount rate)","Unrelated to"],"IRR inference."),
     ("Effective annual rate of 12% compounded monthly = (1 + 0.01)^12 − 1 ≈",["12%","12.5%","*12.68%","13%"],"EAR."),
     ("Tax savings: $10,000 deduction in 24% bracket saves =",["$1,000","$1,200","*$2,400","$10,000"],"Tax deduction value."),
     ("Sharpe ratio: 12% return, 3% risk-free, 15% std dev = (12−3)/15 =",["0.4","0.5","*0.6","0.9"],"Sharpe calculation."),
     ("WACC: 40% debt at 4% after-tax, 60% equity at 12% = 0.40(4) + 0.60(12) =",["4%","6%","*8.8%","12%"],"WACC."),
     ("Contribution margin ratio: price $100, variable cost $40. CM ratio =",["40%","*60% ((100−40)/100)","80%","100%"],"CM ratio."),
     ("Expected value: 80% chance of $10K gain, 20% chance of $5K loss = (0.8×10000) + (0.2×−5000) =",["$8,000","$5,000","*$7,000","$10,000"],"EV calculation."),
     ("Dividend yield: $2.40 annual dividend / $60 stock price =",["2.4%","3%","*4%","6%"],"Yield."),
     ("Mastering these formulas is essential because they:",["Are only for tests","Apply to only one area","*Form the quantitative foundation for every personal and professional financial decision you'll make","Are too complex to use"],"Practical mastery.")]
)
lessons[k]=v

# 10.2
k,v = build_lesson(10,2,"AP Exam Practice",
    "<h3>AP-Style Practice Problems</h3>"
    "<h4>Multi-Step Calculations</h4>"
    "<p>AP problems require combining multiple concepts: TVM, tax effects, risk analysis, and economic reasoning.</p>"
    "<h4>Free Response Strategy</h4>"
    "<ul><li>Show ALL work and calculations.</li>"
    "<li>Label formulas before plugging in numbers.</li>"
    "<li>Explain economic reasoning, not just math.</li></ul>",
    [("AP Free Response Strategy","Show all work, label formulas, state assumptions, explain reasoning, and connect math to economic principles."),
     ("Multi-Step Problem","A problem requiring sequential application of multiple concepts (e.g., calculate after-tax return, then find PV, then compare NPV)."),
     ("Unit Conversion in Finance","Converting between annual/monthly/daily rates and periods: monthly rate = annual rate ÷ 12; periods = years × 12."),
     ("Reasonableness Check","After calculating, verify the answer makes sense (e.g., PV should be less than FV; higher risk should mean higher return)."),
     ("Economic Reasoning","Connecting mathematical results to real-world economic implications and decision-making in AP responses.")],
    [("Convert 8% annual rate to monthly: 8% ÷ 12 =",["0.8%","*0.667% (0.00667 as a decimal)","1%","6.67%"],"Rate conversion."),
     ("$250,000 mortgage at 7.2% annual (0.6%/month) for 360 months. PMT ≈",["$1,200","$1,500","*~$1,698","$2,000"],"Mortgage PMT."),
     ("After paying for 10 years (120 payments), remaining balance is approximately:",["$150,000","$180,000","*~$218,000 (early payments are mostly interest — slow principal reduction)","$250,000"],"Amortization reality."),
     ("Tax bracket question: $75,000 taxable income (single, 2024). In which bracket?",["12%","*22%","24%","32%"],"Bracket identification."),
     ("Effective tax rate on $75,000 (approx $11,843 tax) ≈",["10%","12%","*~15.8%","22%"],"Effective rate."),
     ("A 401(k) contribution of $23,000 in the 22% bracket saves _____ in taxes.",["$2,300","$3,000","*$5,060 (23000 × 0.22)","$23,000"],"Pre-tax contribution."),
     ("That $23,000/year invested at 8% for 25 years (FV of annuity) ≈",["$575,000","$1,000,000","*~$1,674,000","$2,000,000"],"Retirement accumulation."),
     ("If that account is taxed at 15% effective rate in retirement, after-tax value ≈",["$1,000,000","$1,200,000","*~$1,423,000 ($1,674K × 0.85)","$1,674,000"],"After-tax retirement."),
     ("Compare: Roth (post-tax $17,940/yr = $23K × (1−0.22)) invested at 8% for 25 yrs ≈",["$1,000,000","*~$1,306,000 (lower contribution but NO tax on withdrawal)","$1,500,000","$1,674,000"],"Roth comparison."),
     ("In this case, Traditional wins because the _____ rate exceeds the _____ rate.",["Retirement, current","*Current (22%), retirement (15%) — Traditional is better when current marginal rate > retirement rate","They're equal","Roth rate, Traditional rate"],"Rate comparison."),
     ("NPV problem: Machine costs $200K, saves $55K/yr for 5 years, 10% discount. Accept?",["Reject","*Accept (PV of $55K annuity at 10% for 5yr ≈ $208,493; NPV ≈ +$8,493)","Break even","Need more data"],"NPV decision."),
     ("If the machine also has $20K salvage value at year 5, PV of salvage = $20K/1.10^5 ≈",["$20,000","$15,000","*$12,418","$10,000"],"Salvage PV."),
     ("New NPV = $8,493 + $12,418 =",["$8,493","$12,418","*$20,911 (even stronger accept — salvage value improves the project)","$200,000"],"Enhanced NPV."),
     ("Portfolio problem: 60% stocks (10% return, 16% std dev), 40% bonds (5% return, 6% std dev). Portfolio return =",["10%","5%","*8% (0.60×10 + 0.40×5)","7.5%"],"Portfolio return."),
     ("Risk comparison: which ratio shows stock A (15% return, 20% σ) vs stock B (10% return, 8% σ) risk-adjusted?",["P/E ratio","*Sharpe ratio — A: (15−3)/20 = 0.60, B: (10−3)/8 = 0.875 — B is better risk-adjusted","Only return","Only std dev"],"Sharpe comparison."),
     ("International question: $10,000 invested in Japan at ¥150/$ (buying ¥1,500,000). Stock gains 12% to ¥1,680,000. Yen weakens to ¥155/$:",["$12,000","$11,200","*$10,839 (¥1,680,000 ÷ 155 — only 8.4% return in dollars despite 12% gain in yen)","$10,000"],"FX impact."),
     ("Break-even across two products: A ($20 CM, 60% of sales), B ($10 CM, 40%). Weighted CM =",["$20","$10","*$16 (0.60×20 + 0.40×10)","$15"],"Weighted CM."),
     ("With $80K fixed costs, BEP in weighted units = $80K ÷ $16 =",["4,000","*5,000 units total (3,000 of A + 2,000 of B based on sales mix)","6,000","8,000"],"Multi-product BEP."),
     ("AP scoring rewards:",["Only the final answer","Only showing formulas","*Clear work, correct formulas, accurate calculations, AND economic reasoning/interpretation","Only definitions"],"Scoring criteria."),
     ("The key to AP financial math success is:",["Memorizing everything","*Understanding WHY each formula works and WHEN to apply it — connecting math to real-world financial decision-making","Only practice problems","Only reading the textbook"],"Deep understanding.")]
)
lessons[k]=v

# 10.3
k,v = build_lesson(10,3,"AP Economics Context",
    "<h3>AP Economics Connections</h3>"
    "<h4>Microeconomics Connections</h4>"
    "<p>Supply/demand curves → market price → stock pricing. Elasticity → pricing strategy. Marginal analysis → optimal decisions.</p>"
    "<h4>Macroeconomics Connections</h4>"
    "<p>GDP → corporate earnings → market returns. Inflation → interest rates → bond prices. Fed policy → all financial markets.</p>",
    [("Marginal Analysis","Making decisions by comparing marginal benefit to marginal cost — a core principle unifying economics and finance."),
     ("Elasticity and Pricing","Price elasticity of demand determines pricing power: inelastic goods (necessities) can bear price increases; elastic goods cannot."),
     ("Monetary vs. Fiscal Policy","Monetary: Fed controls rates/money supply. Fiscal: Congress controls spending/taxes. Both impact financial markets."),
     ("Market Efficiency","The degree to which market prices reflect all available information — connected to both micro and macro analysis."),
     ("Economic Indicators","GDP, unemployment, CPI, consumer confidence — data that drives financial market movements and investment decisions.")],
    [("In microeconomics, the equilibrium price is where:",["Supply is zero","Demand is zero","*Supply equals demand (similar to how stock prices find equilibrium between buyers and sellers)","Government sets it"],"Market equilibrium."),
     ("Marginal cost = marginal revenue at the:",["Minimum cost","*Profit-maximizing output level (the same principle applies to business financial decisions)","Maximum revenue","Break-even point only"],"Optimal decision."),
     ("Price elasticity of demand: if a 10% price increase causes only 3% demand drop, the product is:",["Elastic","*Inelastic (% change in quantity < % change in price — the company has pricing power)","Unitary elastic","Perfectly elastic"],"Inelastic demand."),
     ("Companies with inelastic demand can raise prices because:",["Everyone must buy","*Consumers don't reduce purchases much (necessities, drugs, unique products) — revenue increases with price","It's required by law","Competitors set prices"],"Pricing power."),
     ("GDP growth of 3% typically corresponds to stock returns that are:",["Negative","Zero","*Positive (economic growth drives corporate earnings growth, which drives stock prices)","Exactly 3%"],"GDP-stock correlation."),
     ("When unemployment rises, consumer spending:",["Increases","Stays the same","*Decreases (less income = less spending = lower corporate revenue = lower stock prices)","Is unrelated"],"Spending cascade."),
     ("The Phillips Curve relates:",["GDP and stocks","*Inflation and unemployment (historically, lower unemployment tends to coincide with higher inflation)","Bonds and stocks","Interest rates and GDP"],"Phillips Curve."),
     ("Quantitative easing (QE) is when the Fed:",["Raises rates","*Buys bonds to inject money into the economy and lower long-term interest rates (stimulating borrowing and investment)","Sells all bonds","Issues new currency"],"Unconventional policy."),
     ("QE generally leads to _____ stock prices.",["Lower","*Higher (lower rates push investors toward stocks; abundant liquidity inflates asset prices)","Unchanged","Unpredictable"],"QE market impact."),
     ("Trade deficits affect currency because:",["They don't","*Importing more than exporting creates selling pressure on the domestic currency (more dollars flowing out to pay for imports)","They strengthen currency","Only tariffs matter"],"Trade-currency link."),
     ("Comparative advantage explains why countries trade because:",["Trade is optional","*Countries benefit by specializing in what they produce most efficiently and trading for other goods","All countries are equal","Only large countries trade"],"Trade rationale."),
     ("Monopolies vs. competitive markets: monopolies earn _____ profits.",["Zero","Normal","*Above-normal (no competition forces prices down — relevant for evaluating companies' competitive positions)","Below normal"],"Market structure."),
     ("Consumer surplus in financial markets represents:",["Producer profit","*The difference between what investors are willing to pay and what they actually pay (getting stocks 'below' their perceived value)","Government revenue","Market fees"],"Buyer advantage."),
     ("Information asymmetry (one party knows more) in markets causes:",["Perfect pricing","*Adverse selection and moral hazard (e.g., insider trading, used car 'lemons problem' — drives regulation)","Better outcomes","Lower prices"],"Information problems."),
     ("Game theory applies to business decisions because:",["It doesn't","*Companies must consider competitors' reactions: pricing, market entry, advertising — strategy depends on others' actions","Only for games","Only for board games"],"Strategic interaction."),
     ("The tragedy of the commons applies to:",["Only farmland","*Shared resources including financial markets (short-term individual greed can destroy long-term collective value)","Nothing in finance","Only government"],"Common resource problem."),
     ("Behavioral economics + finance shows:",["People are rational","*People systematically deviate from rational decision-making — understanding biases improves financial outcomes","Emotions don't matter","Only math matters"],"Behavioral insights."),
     ("The AD-AS (Aggregate Demand/Supply) model shows:",["Individual product prices","*Overall price level and output — shifts in AD or AS affect inflation, GDP, and financial markets broadly","Only one market","Only labor markets"],"Macro model."),
     ("Understanding AP economics strengthens financial math because:",["They're unrelated","*Economics provides the WHY behind financial math formulas — understanding incentives, markets, and policy makes financial decisions more informed","Only one matters","Economics replaces math"],"Complementary knowledge."),
     ("The integration of economics and financial math is tested on the AP exam through:",["Only multiple choice","*Problems requiring both quantitative calculation AND qualitative economic reasoning and interpretation","Only essays","Only definitions"],"Exam integration.")]
)
lessons[k]=v

# 10.4
k,v = build_lesson(10,4,"Real-World Applications",
    "<h3>Real-World Financial Math Applications</h3>"
    "<h4>Everyday Decisions</h4>"
    "<ul><li><b>Renting vs. Buying:</b> Comparing total costs including opportunity cost of down payment.</li>"
    "<li><b>Car Buying:</b> Lease vs. buy analysis; total cost of ownership.</li>"
    "<li><b>College ROI:</b> Tuition cost vs. lifetime earnings increase.</li>"
    "<li><b>Retirement Planning:</b> How much to save monthly to reach a goal.</li></ul>",
    [("Rent vs. Buy Analysis","Comparing total cost of renting (rent + renter's insurance) vs. buying (mortgage, taxes, insurance, maintenance, opportunity cost of down payment) over time."),
     ("Total Cost of Ownership (Car)","Purchase price + insurance + gas + maintenance + depreciation − resale value = true cost of a vehicle over ownership period."),
     ("College ROI","(Lifetime earnings with degree − lifetime earnings without − total college cost) / total college cost × 100."),
     ("Retirement Savings Goal","Using FV of annuity formula to determine monthly savings needed to reach a target retirement nest egg."),
     ("The 4% Rule","Guideline that retirees can withdraw 4% of their portfolio in year 1 (adjusting for inflation) with high probability of money lasting 30+ years.")],
    [("Rent at $1,500/month vs. mortgage at $1,800/month: the comparison is NOT just $300/month because:",["Rent is always worse","*Buying includes tax benefits, equity building, and appreciation BUT also taxes, insurance, maintenance, and opportunity cost of down payment","The numbers are obvious","Buying always wins"],"Full cost comparison."),
     ("$60,000 down payment invested at 8% instead of used for a home would grow to _____ in 10 years.",["$80,000","$100,000","*~$129,500 (the opportunity cost of the down payment)","$60,000"],"Opportunity cost."),
     ("Car lease: $400/month for 36 months = $14,400. Buy: $500/month for 60 months, car worth $12K at end. Total buy cost =",["$30,000","*$18,000 ($30,000 payments − $12,000 resale value)","$12,000","$42,000"],"Lease vs. buy."),
     ("Average car depreciation: a $35,000 car is worth approximately _____ after 5 years.",["$25,000","$20,000","*~$14,000 (cars typically lose ~60% of value in the first 5 years)","$35,000"],"Depreciation reality."),
     ("College ROI: $100K tuition for a degree increasing lifetime earnings by $900K. ROI =",["100%","500%","*800% ((900K−100K)/100K)","900%"],"Education ROI."),
     ("However, the opportunity cost of 4 years not earning $35K/year = _____ in foregone earnings.",["$35,000","$70,000","*$140,000","$200,000"],"Foregone earnings."),
     ("Adjusted college ROI: ($900K − $100K − $140K) / ($100K + $140K) =",["800%","500%","*~275% (still excellent but lower than the simple calculation)","100%"],"Adjusted ROI."),
     ("Retirement goal: $1.5M by age 65. Starting at 25 (40 years), 8% return. Monthly savings needed ≈",["$200","*~$430","$800","$1,500"],"Savings target."),
     ("Starting the same savings at 35 (30 years to go), monthly needed jumps to ≈",["$430","$800","*~$1,000","$2,000"],"Delay cost."),
     ("Starting at 45 (20 years), monthly needed ≈",["$1,000","$1,500","*~$2,500","$4,000"],"10 more years of delay."),
     ("The 4% withdrawal rule: to have $60K/year income in retirement, you need:",["$500,000","$1,000,000","*$1,500,000 ($60,000 ÷ 0.04)","$2,000,000"],"4% rule."),
     ("Social Security replaces approximately _____ of pre-retirement income for average earners.",["20%","*~40%","60%","100%"],"SS replacement."),
     ("The 'savings gap' = $60K needed − ~$24K from SS = _____ to fund from personal savings.",["$24,000","$30,000","*$36,000/year","$60,000"],"Personal responsibility."),
     ("Emergency fund recommendation: 3-6 months of expenses. At $4,000/month expenses =",["$4,000","$8,000","*$12,000-$24,000","$48,000"],"Emergency fund."),
     ("Paying off a credit card at 22% APR vs. investing at 8%: you should:",["Invest (higher potential)","Split 50/50","*Pay off the credit card (guaranteed 22% 'return' by eliminating debt vs. uncertain 8% investment return)","Neither"],"Debt vs. invest."),
     ("Student loan at 5% vs. investing at historical 10%: the math suggests:",["Always pay loan first","*Invest while making minimum loan payments (expected investment return exceeds loan rate — but consider risk tolerance)","Always invest everything","Neither"],"Low-rate debt strategy."),
     ("High-yield savings at 4.5% vs. CDs at 4.8%: the 0.3% difference on $10,000 =",["$300","*$30/year (often not worth the CD's liquidity restriction for such a small difference)","$3","$3,000"],"Marginal difference."),
     ("The most valuable personal finance habit is:",["Day trading","Market timing","*Consistently saving/investing 15-20% of income starting as early as possible (time + compound interest = wealth)","Getting lucky"],"Consistency."),
     ("Financial math is relevant to EVERY adult because:",["Only for finance careers","Only for wealthy people","*Everyone earns income, pays taxes, borrows money, saves for goals, and needs insurance — financial literacy is universal","Only for AP exams"],"Universal relevance."),
     ("The single most powerful concept in this course is:",["Stock picking","Tax avoidance","Market timing","*Compound interest — Einstein reportedly called it the 'eighth wonder of the world'"],"Course cornerstone.")]
)
lessons[k]=v

# 10.5
k,v = build_lesson(10,5,"Capstone: Personal Financial Plan",
    "<h3>Capstone: Build Your Personal Financial Plan</h3>"
    "<h4>Plan Components</h4>"
    "<ul><li><b>1. Net Worth Statement:</b> Assets − Liabilities = Net Worth.</li>"
    "<li><b>2. Budget:</b> Income − Expenses = Surplus (invest) or Deficit (cut spending).</li>"
    "<li><b>3. Emergency Fund:</b> 3-6 months expenses in savings.</li>"
    "<li><b>4. Debt Payoff Plan:</b> Priority: high-interest first (avalanche method).</li>"
    "<li><b>5. Investment Plan:</b> Retirement contributions, asset allocation by age.</li>"
    "<li><b>6. Insurance Review:</b> Adequate coverage for health, auto, life, disability.</li>"
    "<li><b>7. Estate Planning:</b> Will, beneficiary designations, power of attorney.</li></ul>",
    [("Net Worth","Total assets minus total liabilities; your financial 'score' — track it quarterly to measure progress."),
     ("50/30/20 Budget Rule","50% needs (rent, food, insurance), 30% wants (entertainment, dining), 20% savings/debt payoff."),
     ("Avalanche Method","Debt payoff strategy: pay minimums on all debts, put extra money toward the HIGHEST interest rate debt first."),
     ("Snowball Method","Debt payoff strategy: pay off smallest balances first for psychological wins (higher total interest cost than avalanche)."),
     ("Estate Plan","Legal documents ensuring your assets are distributed according to your wishes: will, beneficiaries, POA, healthcare directive.")],
    [("Net worth = Assets − Liabilities. $50K savings + $20K car − $30K student loans − $5K credit card =",["$50,000","*$35,000","$105,000","$20,000"],"Net worth calculation."),
     ("The 50/30/20 rule on $4,000/month take-home: needs budget =",["$1,200","*$2,000","$2,500","$4,000"],"50% needs."),
     ("Savings/debt payoff (20%) on $4,000/month =",["$400","$600","*$800","$1,200"],"20% savings."),
     ("The avalanche method prioritizes:",["Smallest balance","Largest balance","*Highest interest rate debt (mathematically optimal — saves the most money on interest)","Newest debt"],"Optimal payoff."),
     ("The snowball method prioritizes:",["Highest interest rate","*Smallest balance (quick wins for motivation — but costs more in total interest than avalanche)","Largest balance","Oldest debt"],"Psychological payoff."),
     ("Emergency fund: $4K monthly expenses × 6 months =",["$4,000","$12,000","*$24,000","$48,000"],"Safety net."),
     ("Where to keep an emergency fund:",["Stock market","CDs only","*High-yield savings account (accessible within 1-2 days, FDIC insured, earning some interest)","Under the mattress"],"Liquidity + safety."),
     ("Recommended retirement savings rate is at minimum:",["5%","10%","*15% of gross income (including employer match)","25%"],"Savings rate."),
     ("Asset allocation for a 25-year-old with 40 years to retirement:",["20/80 stocks/bonds","50/50","*90/10 or 80/20 stocks/bonds (long time horizon can weather volatility for higher returns)","100% bonds"],"Age-appropriate allocation."),
     ("Asset allocation for a 60-year-old approaching retirement:",["90/10 stocks/bonds","80/20","*50/50 or 40/60 stocks/bonds (protecting accumulated wealth is more important than growth)","100% stocks"],"Conservative at retirement."),
     ("Employer 401(k) match of 50% up to 6% means: on $60K salary, contributing 6% ($3,600), employer adds:",["$3,600","$600","*$1,800 (50% of $3,600)","$6,000"],"Free money."),
     ("NOT contributing enough to get the full employer match means:",["Smart saving","*Leaving free money on the table — always contribute at least enough to get the full match (immediate 50% return!)","Wise budgeting","Reducing risk"],"Match = free return."),
     ("Life insurance needs: $70K income × 10 = _____ coverage recommended.",["$350,000","$500,000","*$700,000","$1,000,000"],"Coverage amount."),
     ("A 30-year, $750K term life policy costs approximately:",["$200/month","*$25-50/month (very affordable for the protection it provides)","$100/month","$5/month"],"Term life cost."),
     ("A will ensures:",["Nothing happens","You pay less tax","*Your assets are distributed according to YOUR wishes (without a will, the state decides — intestate succession)","Only lawyers benefit"],"Will importance."),
     ("Beneficiary designations on retirement accounts and insurance:",["Don't matter","*Override the will (they pass directly to the named beneficiary — keep them updated after life changes)","Are the same as a will","Only matter for large accounts"],"Beneficiary priority."),
     ("The financial plan should be reviewed:",["Once in a lifetime","Only when problems arise","*At least annually and after major life events (marriage, baby, job change, home purchase)","Never"],"Regular review."),
     ("The most expensive mistake in personal finance is:",["A bad stock pick","A high fee fund","*Not starting early enough — every year of delay costs significantly more in catch-up contributions","One bad purchase"],"Time cost."),
     ("$500/month starting at 22 vs. 32 (both at 8% to age 65): the 10-year head start adds approximately:",["$50,000","$200,000","$300,000","*~$500,000+ more at retirement (the power of the first decade of compounding)"],"Early start advantage."),
     ("The purpose of a personal financial plan is to:",["Get rich quick","Beat the market","Avoid all taxes","*Provide a structured, math-backed roadmap for achieving your financial goals throughout life"],"Plan purpose.")]
)
lessons[k]=v

# 10.6
k,v = build_lesson(10,6,"Comprehensive Review",
    "<h3>Comprehensive Course Review</h3>"
    "<h4>Course Journey</h4>"
    "<ul><li><b>Units 1-2:</b> Financial literacy fundamentals, interest, and banking.</li>"
    "<li><b>Units 3-4:</b> Loans, debt, investments, and retirement planning.</li>"
    "<li><b>Units 5-6:</b> Budgeting, taxes, and insurance.</li>"
    "<li><b>Units 7-8:</b> Business finance and stock markets.</li>"
    "<li><b>Unit 9:</b> Advanced concepts: TVM, NPV, IRR, corporate finance, risk analysis.</li></ul>",
    [("Financial Literacy","The ability to understand and effectively use financial skills: budgeting, investing, borrowing, taxation, and personal financial management."),
     ("Compound Interest","Interest calculated on both the initial principal AND accumulated interest — the most powerful force in finance."),
     ("Diversification","Spreading investments across asset classes, sectors, and geographies to reduce risk without proportionally reducing expected returns."),
     ("Tax Efficiency","Structuring financial activities to legally minimize taxes: retirement accounts, asset location, loss harvesting, and strategic deductions."),
     ("Financial Planning Process","Assess current position → set goals → create strategy → implement plan → monitor and adjust — continuous cycle.")],
    [("The foundation of all financial math is:",["Stock markets","Tax code","*The time value of money (a dollar today > a dollar tomorrow)","Insurance"],"Core foundation."),
     ("Simple interest I = PRT. Compound interest uses:",["Addition","Subtraction","*Exponential growth: FV = PV(1+r)^n (interest on interest)","Division only"],"Compound power."),
     ("$1 invested at 10% for 100 years becomes:",["$100","$1,000","*~$13,781 (the exponential nature of compound interest over long periods)","$10"],"Long-term compounding."),
     ("The most important personal finance habit is:",["Market timing","Stock picking","*Spending less than you earn and consistently investing the difference","Avoiding all risk"],"Foundational habit."),
     ("Debt with interest rates above _____ should generally be paid off before investing.",["2%","4%","*6-8% (if investment returns average ~8-10%, high-interest debt reduces net worth faster than investments grow it)","12%"],"Debt priority threshold."),
     ("Credit score affects:",["Only credit cards","*Loan rates, insurance premiums, rental applications, and even some employment decisions","Only mortgages","Nothing financial"],"Score impact."),
     ("The three types of income are:",["Only wages","*Earned (wages), portfolio (investments), and passive (rental, royalties) — each taxed differently","Only investment","Only passive"],"Income types."),
     ("The progressive tax system means:",["Everyone pays the same rate","*Higher income portions are taxed at higher rates — but effective rate is always less than marginal rate","The rich pay nothing","Taxes decrease with income"],"Tax structure."),
     ("Insurance protects against:",["All losses","Daily expenses","*Catastrophic losses that would devastate your finances (transfer risk to the insurer via premium)","Nothing important"],"Risk transfer."),
     ("Break-even analysis is critical because it shows:",["Maximum profit","*The minimum sales needed to cover costs — below this, the business loses money","Revenue only","Only fixed costs"],"Viability threshold."),
     ("NPV > 0 means:",["Break even","Loss","*The investment earns more than the required return — it creates value (accept)","The same as IRR"],"Value creation."),
     ("For comparing risk-adjusted returns, use the:",["P/E ratio","*Sharpe ratio (excess return per unit of risk)","Only return","Only risk"],"Risk-adjusted metric."),
     ("Asset allocation should be based on:",["Friend's advice","Latest news","*Your time horizon, risk tolerance, and financial goals","Only age"],"Personal factors."),
     ("The efficient market hypothesis suggests that the best strategy for most investors is:",["Day trading","Active stock picking","*Low-cost index fund investing (matching the market is a winning strategy over time)","Timing the market"],"Evidence-based investing."),
     ("Behavioral finance teaches that the biggest threat to investment returns is:",["Market crashes","High fees","*Your own emotional reactions (panic selling, FOMO buying, overconfidence)","Low interest rates"],"Behavior gap."),
     ("Global diversification matters because:",["All markets are the same","*Different economies and markets don't move in perfect lockstep — reducing overall portfolio volatility","International markets are better","US market is insufficient"],"Geographic spread."),
     ("Corporate finance uses WACC as the hurdle rate because it represents:",["The highest possible return","*The blended minimum return needed to satisfy both debt holders and equity investors","Only debt cost","Only equity cost"],"Minimum acceptable return."),
     ("The personal financial plan integrates:",["Only investment advice","Only tax planning","Only budgeting","*All course concepts: budgeting, tax planning, insurance, investing, debt management, and estate planning"],"Holistic planning."),
     ("The goal of financial math education is:",["Passing a test","Getting rich quick","*Developing the quantitative skills and financial literacy to make informed decisions that improve your financial life","Only for finance careers"],"Education purpose."),
     ("Financial math is unique because it is:",["Abstract and theoretical","Only for professionals","*Directly applicable to decisions EVERY person makes — from the first paycheck to retirement and beyond","Only for the wealthy"],"Universal applicability.")]
)
lessons[k]=v

# 10.7
k,v = build_lesson(10,7,"AP Financial Math Scenarios",
    "<h3>AP-Style Integrated Scenarios</h3>"
    "<h4>Scenario: Life After Graduation</h4>"
    "<p>Recent graduate: $45K salary, $28K student loans at 5.5%, needs apartment, car, insurance, and retirement savings. "
    "Apply ALL course concepts to make optimal decisions.</p>",
    [("Scenario-Based Problem Solving","Applying multiple financial concepts simultaneously to a realistic life situation requiring integrated analysis."),
     ("Financial Decision Framework","1. Identify the decision. 2. Gather data. 3. Calculate options. 4. Compare quantitatively. 5. Consider qualitative factors. 6. Decide."),
     ("Optimization vs. Satisficing","Optimization: finding the mathematically best solution. Satisficing: finding a 'good enough' solution that meets all constraints."),
     ("Holistic Financial Analysis","Considering all financial dimensions — income, taxes, debt, savings, insurance, and opportunity costs — simultaneously."),
     ("Lifetime Financial Impact","Small decisions compound dramatically: a $100/month savings difference at 22 vs. not starting = ~$350K+ difference by retirement.")],
    [("Starting salary $45K. Monthly gross pay =",["$2,500","$3,000","*$3,750 ($45,000 ÷ 12)","$4,500"],"Monthly gross."),
     ("Estimated take-home after taxes and deductions (~25% effective rate) ≈",["$2,000","$2,500","*~$2,813 ($3,750 × 0.75)","$3,750"],"Net pay."),
     ("50/30/20 budget: needs ≤ $1,407, wants ≤ $844, savings/debt ≥",["$400","*$563","$750","$1,000"],"Budget allocation."),
     ("$28K student loans at 5.5% with standard 10-year repayment. Monthly payment ≈",["$200","*~$304","$400","$500"],"Student loan payment."),
     ("Total interest paid over 10 years: ($304 × 120) − $28,000 ≈",["$5,000","*~$8,480","$12,000","$28,000"],"Total loan cost."),
     ("After student loan payment ($304), remaining savings/debt budget = $563 − $304 =",["$100","$200","*$259","$563"],"Remaining for savings."),
     ("If employer offers 401(k) with 50% match up to 6% of salary: 6% of $45K =",["$1,350","*$2,700/year ($225/month) — employer adds $1,350","$4,050","$5,400"],"401(k) contribution."),
     ("The employer match ($1,350/year) is a guaranteed _____ return on your contribution.",["25%","*50% (instant, risk-free return — always get the full match)","100%","10%"],"Free money return."),
     ("Contributing $225/month to 401(k) leaves $259 − $225 = $34/month for additional savings. The first priority is:",["A vacation fund","*Building an emergency fund ($12,000-18,000 target at $34/month will take a while — consider ways to increase income)","A car upgrade","Stock trading"],"Emergency fund priority."),
     ("Renter's insurance at ~$20/month provides _____ protection.",["Unnecessary","*Essential (covers $20K+ in personal property, liability, and additional living expenses for just $240/year)","Expensive","Minimal"],"Cheap essential."),
     ("Health insurance through employer at $150/month is likely:",["Optional","Too expensive","*A necessity — medical debt is the leading cause of bankruptcy (always maintain health coverage)","Unnecessary for young people"],"Health coverage."),
     ("The $225/month 401(k) contribution at 8% for 43 years (until 65) grows to approximately:",["$500,000","$750,000","*~$1,000,000+","$2,000,000"],"Early start retirement."),
     ("Adding the employer match ($1,350/yr at 8% for 43 yrs) adds another ≈",["$100,000","$200,000","*~$500,000+","$1,000,000"],"Match growth."),
     ("Total estimated retirement account at 65: $1M + $500K ≈",["$500,000","$1,000,000","*~$1,500,000","$3,000,000"],"Combined retirement."),
     ("At the 4% rule, $1.5M supports annual income of:",["$30,000","$40,000","*$60,000/year (plus Social Security — potentially a comfortable retirement)","$75,000"],"Retirement income."),
     ("Should the graduate pay extra on student loans (5.5%) or invest more (expected 8%)?",["Always extra on loans","*Mathematically, investing at 8% > paying 5.5% debt — but ensure emergency fund exists first and consider risk tolerance","Always invest","Neither"],"Optimal allocation."),
     ("Buying vs. leasing a car: a reliable used car at $15K financed at 5% for 5 years costs ~$283/month. Lease at $250/month for 3 years, then:",["Own the car","*Return it with nothing (leasing costs more long-term; buying builds equity in the vehicle)","Get paid","Get a discount"],"Car decision."),
     ("Credit score optimization: the graduate should:",["Apply for many cards","*Pay all bills on time, keep credit utilization below 30%, maintain oldest accounts — builds score for future mortgage rates","Close all accounts","Avoid all credit"],"Credit building."),
     ("The $45K salary with proper financial planning can lead to:",["Nothing significant","*Millionaire status by retirement through consistent saving, employer match, and compound interest — financial literacy is the key","Immediate wealth","Financial stress"],"Financial planning power."),
     ("The most important takeaway from this entire course:",["Memorize formulas","*Start early, be consistent, understand the math behind your decisions, and let compound interest work for you over decades","Get rich quick","Avoid all financial decisions"],"Course takeaway.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 10: wrote {len(lessons)} lessons")
