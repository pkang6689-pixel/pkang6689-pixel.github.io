#!/usr/bin/env python3
"""Financial Math Unit 5 – Budgeting & Financial Planning (8 lessons)."""
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

# 5.1
k,v = build_lesson(5,1,"Creating a Personal Budget",
    "<h3>Creating a Personal Budget</h3>"
    "<h4>The 50/30/20 Rule</h4>"
    "<ul><li><b>50% — Needs:</b> Housing, food, utilities, transportation, insurance.</li>"
    "<li><b>30% — Wants:</b> Entertainment, dining out, hobbies, subscriptions.</li>"
    "<li><b>20% — Savings &amp; debt:</b> Retirement, emergency fund, extra debt payments.</li></ul>"
    "<h4>Budget Equation</h4>"
    "<p><b>Income − Expenses = Surplus (or Deficit)</b></p>",
    [("Budget","A plan for how income will be spent, saved, and invested over a specific time period."),
     ("50/30/20 Rule","Budgeting guideline: 50% needs, 30% wants, 20% savings/debt repayment."),
     ("Fixed Expenses","Costs that stay the same each month (rent, loan payments, insurance premiums)."),
     ("Variable Expenses","Costs that fluctuate monthly (groceries, utilities, entertainment)."),
     ("Budget Surplus/Deficit","Income minus expenses: positive = surplus (save/invest); negative = deficit (spending more than earning).")],
    [("The 50/30/20 rule allocates 50% of income to:",["Savings","Wants","*Needs (essential expenses: housing, food, utilities, transportation)","Investments"],"Essential spending category."),
     ("The 20% in the 50/30/20 rule goes toward:",["Entertainment","Housing","*Savings and debt repayment (retirement, emergency fund, extra debt payments)","Food"],"Wealth-building."),
     ("With $4,000 monthly take-home pay under 50/30/20: needs budget is:",["$1,200","$1,600","*$2,000","$2,400"],"4000 × 0.50."),
     ("The budget equation is:",["Income × Expenses","*Income − Expenses = Surplus or Deficit","Income + Expenses","Expenses ÷ Income"],"Basic formula."),
     ("Fixed expenses include:",["Dining out","Concert tickets","*Rent/mortgage, car payment, insurance premiums","Vacation spending"],"Consistent costs."),
     ("Variable expenses include:",["Rent","Car payment","*Groceries, utilities, entertainment (amounts change month to month)","Student loan payment"],"Fluctuating costs."),
     ("If income is $5,000 and expenses are $5,500, the budget shows a:",["$500 surplus","*$500 deficit (spending more than earning — unsustainable)","$5,000 surplus","Balanced budget"],"Deficit."),
     ("The first step in budgeting is:",["Cutting all spending","*Tracking current income and expenses to understand where money actually goes","Opening a savings account","Canceling subscriptions"],"Awareness first."),
     ("Zero-based budgeting means:",["$0 income","*Every dollar of income is assigned a job (spending, saving, or investing) — income minus all allocations = $0","Spending nothing","Having no budget"],"Every dollar allocated."),
     ("Pay yourself first means:",["Pay bills first","*Automatically save/invest before spending on wants — treat savings as a non-negotiable 'expense'","Pay debts first","Spend first, save later"],"Savings priority."),
     ("A budget review should happen:",["Once a year","*Monthly (at minimum) to track against plan and adjust for changes","Only when broke","Never"],"Regular monitoring."),
     ("The envelope system involves:",["Writing letters","*Putting cash in labeled envelopes for each budget category — when an envelope is empty, spending stops","Using only checks","Online banking only"],"Physical budgeting method."),
     ("Discretionary spending is:",["Required expenses","*Spending on non-essential items you CHOOSE to buy (dining out, entertainment, shopping)","Fixed costs","Bill payments"],"Optional spending."),
     ("If a person earns $60,000/year, the 50/30/20 rule suggests saving _____ per year.",["$6,000","*$12,000 (20% of $60,000)","$18,000","$30,000"],"Savings target."),
     ("The biggest budgeting mistake is:",["Being too strict","*Not having a budget at all (most people don't know where their money goes)","Overspending on one category","Saving too much"],"Awareness gap."),
     ("A sinking fund is:",["A bad investment","*Money set aside regularly for a planned future expense (car repair, vacation, holiday gifts)","An emergency fund","A checking account"],"Planned saving."),
     ("Needs vs. wants: a smartphone is typically a:",["Pure want","*A need (communication tool) but the latest model at $1,200 is a want (a cheaper phone fulfills the need)","Pure need","Neither"],"Nuanced distinction."),
     ("Budgets should be _____ to be sustainable.",["Extremely restrictive","*Realistic and flexible — including some fun spending to avoid burnout and budget abandonment","Impossible to follow","Only for saving"],"Practical approach."),
     ("Tracking expenses reveals that many people:",["Spend perfectly","*Significantly underestimate spending on small recurring purchases (coffee, subscriptions, impulse buys)","Don't need a budget","Save naturally"],"Spending awareness."),
     ("For financial math, budgeting applies:",["No math","*Arithmetic, percentages, and planning skills to real-world money management — the foundation of all personal finance","Only algebra","Only calculus"],"Foundational skill.")]
)
lessons[k]=v

# 5.2
k,v = build_lesson(5,2,"Tracking Income & Expenses",
    "<h3>Tracking Income &amp; Expenses</h3>"
    "<h4>Income Sources</h4>"
    "<ul><li><b>Gross income:</b> Total earnings before deductions.</li>"
    "<li><b>Net income:</b> Take-home pay after taxes and deductions.</li></ul>"
    "<h4>Expense Categories</h4>"
    "<ul><li><b>Essential:</b> Housing (25-35%), food (10-15%), transportation (10-15%), insurance/health.</li>"
    "<li><b>Discretionary:</b> Entertainment, subscriptions, dining, shopping.</li>"
    "<li><b>Financial:</b> Savings, investments, debt payments.</li></ul>",
    [("Gross Income","Total earnings before any deductions (taxes, insurance, retirement contributions)."),
     ("Net Income","Take-home pay after all deductions — the actual amount available for budgeting."),
     ("Expense Ratio (Personal)","The percentage of income spent on each category; helps identify areas for adjustment."),
     ("Recurring Expenses","Regular, predictable expenses (subscriptions, memberships, loan payments)."),
     ("Expense Tracking","Recording all spending to compare actual vs. budgeted amounts and identify patterns.")],
    [("Gross income is:",["Take-home pay","*Total earnings BEFORE taxes and deductions","After-tax income","Investment returns"],"Pre-deduction total."),
     ("Net income is:",["Total earnings","Gross income","*Take-home pay AFTER taxes and all deductions","Investment income"],"What you actually receive."),
     ("If gross income is $70,000 and deductions total 30%, net income is approximately:",["$70,000","*$49,000 (70000 × 0.70)","$21,000","$60,000"],"Net calculation."),
     ("Housing should typically not exceed _____ of take-home pay.",["50%","*25-35%","10%","40%"],"Housing guideline."),
     ("On $4,500/month net income, maximum housing at 30% is:",["$900","*$1,350","$1,800","$2,250"],"4500 × 0.30."),
     ("The best way to track expenses is:",["Guessing","*Systematically recording every expenditure (app, spreadsheet, or bank categorization)","Only big purchases","Monthly estimate only"],"Consistent tracking."),
     ("'Latte factor' spending (small daily purchases) of $7/day totals _____ per year.",["$1,000","$1,500","*~$2,555 (7 × 365)","$3,000"],"Small amounts add up."),
     ("That $2,555/year invested at 8% for 30 years would grow to approximately:",["$25,000","$50,000","*~$286,000","$500,000"],"Opportunity cost."),
     ("Subscription audit reveals the average American spends _____ per month on subscriptions.",["$50","$100","*~$200-300+ (streaming, apps, gym, services — often more than estimated)","$500"],"Subscription creep."),
     ("Income tracking should include:",["Only salary","*ALL income: salary, freelance, side jobs, investment returns, tax refunds","Only major sources","Only taxable income"],"Complete picture."),
     ("A common expense leak is:",["Rent","Groceries","*Unused subscriptions and memberships (people often forget recurring charges)","Utilities"],"Forgotten charges."),
     ("Categorizing expenses helps by:",["Making accounting harder","*Identifying where money actually goes vs. where you THINK it goes — often revealing surprises","Only for tax purposes","Nothing useful"],"Pattern recognition."),
     ("Cash flow analysis shows:",["Only income","Only expenses","*When money comes in and goes out during the month — timing matters for avoiding overdrafts","Only savings"],"Timing awareness."),
     ("An irregular expense like car insurance paid every 6 months should be:",["Ignored","*Divided by 6 and included as a monthly budget item (set aside 1/6 each month in a sinking fund)","Paid last","Skipped"],"Spread out planning."),
     ("Annual expenses that people often forget to budget for:",["Rent","*Holiday gifts, car registration, home maintenance, medical copays, clothing","Daily coffee","Groceries"],"Periodic costs."),
     ("Income stability (W-2 employee) vs. income variability (freelancer) affects budgeting because:",["It doesn't","*Variable income requires budgeting based on minimum expected income and saving extra during good months","Only employees need budgets","Only freelancers need budgets"],"Income uncertainty."),
     ("Financial ratios: Savings rate = savings ÷ income. 20% savings rate on $50,000 =",["$5,000","*$10,000","$15,000","$20,000"],"Savings calculation."),
     ("Expense tracking apps (Mint, YNAB, Copilot) help by:",["Spending more","*Automatically categorizing transactions, showing trends, and alerting when you exceed budget categories","Only tracking income","Only for taxes"],"Automated tracking."),
     ("A spending journal for 30 days typically reveals that people:",["Spend as expected","*Spend 10-30% more than they think — awareness alone changes behavior","Spend less than expected","Save naturally"],"Awareness effect."),
     ("For financial math, expense tracking provides:",["No useful data","*Real data for calculations: ratios, percentages, projections, and optimization of personal finances","Only historical info","Only for accountants"],"Data-driven decisions.")]
)
lessons[k]=v

# 5.3
k,v = build_lesson(5,3,"Emergency Funds & Savings Goals",
    "<h3>Emergency Funds &amp; Savings Goals</h3>"
    "<h4>Emergency Fund</h4>"
    "<ul><li><b>Target:</b> 3–6 months of essential expenses.</li>"
    "<li><b>Where:</b> High-yield savings (liquid, FDIC-insured).</li>"
    "<li><b>Purpose:</b> Job loss, medical emergency, major car repair, home emergency.</li></ul>"
    "<h4>Savings Goals</h4>"
    "<p>Use the formula: <b>Monthly savings = Goal amount ÷ Months until deadline</b> (or use FV/PV for interest).</p>",
    [("Emergency Fund","3–6 months of essential expenses saved in a liquid, accessible account for unexpected major expenses."),
     ("Savings Goal","A specific financial target with a timeline and required monthly contribution to achieve it."),
     ("Liquidity","How quickly an asset can be converted to cash without significant loss — emergency funds need high liquidity."),
     ("Sinking Fund","Money saved incrementally for a specific planned future expense (vacation, car down payment, wedding)."),
     ("Financial Buffer","Cash reserve that prevents small emergencies from becoming financial disasters or debt spirals.")],
    [("The recommended emergency fund size is:",["1 month of expenses","*3–6 months of essential expenses","1 year of income","$500"],"Standard guideline."),
     ("If monthly essential expenses are $3,000, a 6-month emergency fund should be:",["$6,000","$15,000","*$18,000","$30,000"],"3000 × 6."),
     ("The emergency fund should be kept in:",["Stocks","CDs","*High-yield savings account (liquid + FDIC-insured + earns some interest)","Under the mattress"],"Accessible and safe."),
     ("An emergency fund protects against:",["Planned expenses","*Job loss, medical emergencies, major car/home repairs — unexpected events that could otherwise create debt","Normal spending","Investment losses"],"Unexpected protection."),
     ("Without an emergency fund, unexpected expenses often go on:",["Savings","*Credit cards (at 20%+ interest — creating expensive debt from a temporary problem)","Investment accounts","Nowhere"],"Debt cycle."),
     ("To save $12,000 in 12 months (no interest), monthly savings needed:",["$500","$800","*$1,000","$1,200"],"12000 ÷ 12."),
     ("To save $20,000 for a car down payment in 3 years with 4% APY, monthly savings ≈:",["$600","*~$524 (PMT calculation with interest reduces the required amount)","$556","$700"],"Interest helps."),
     ("Building an emergency fund should start:",["After all debts are paid","*Immediately — even $500-$1,000 provides a starter buffer while paying off debt","After retirement saving","Only if extra income exists"],"Start now, even small."),
     ("The concept of 'financial runway' means:",["How fast you spend","*How many months you can survive without income using your savings and emergency fund","How quickly you get paid","Your credit limit"],"Months of security."),
     ("A common mistake is using the emergency fund for:",["True emergencies","*Non-emergencies (vacation, holiday shopping, sale items) — depleting the fund for wants, not needs","Medical bills","Car repairs"],"Discipline required."),
     ("$500/month into a high-yield savings at 4.5% for 2 years grows to approximately:",["$12,000","*~$12,540 (savings + modest interest)","$13,000","$15,000"],"Emergency fund building."),
     ("For irregular income earners, an emergency fund of _____ months is more appropriate.",["3","*6-9 months (more cushion needed due to income uncertainty)","1","12"],"Variable income buffer."),
     ("Savings goals should be SMART:",["Simple, minimal, average, reduced, tiny","*Specific, Measurable, Achievable, Relevant, Time-bound","Short, maximum, all, ready, tall","Easy, quick, simple"],"Goal framework."),
     ("Short-term savings goals (< 3 years) should be in:",["Stocks","*Savings accounts or CDs (low risk — you need the money soon and can't afford a market drop)","Crypto","Real estate"],"Appropriate vehicle."),
     ("Long-term savings goals (5+ years) can include:",["Only savings accounts","*Investment accounts (time horizon allows recovery from market dips, earning higher returns)","Only CDs","Only bonds"],"Growth potential."),
     ("Automatic transfers to savings help because:",["Banks require them","*They remove the temptation to spend first — saving becomes a habit, not a decision each month","They earn more interest","They are tax-deductible"],"Automation advantage."),
     ("The psychological benefit of separate savings accounts for each goal is:",["More fees","*Visual progress tracking for each goal motivates continued saving (wedding fund, vacation fund, etc.)","No benefit","Less organization"],"Goal-specific motivation."),
     ("If rent increases $200/month, the emergency fund should be:",["Decreased","Kept the same","*Increased ($200 × 6 = $1,200 more needed for the same 6-month buffer)","Eliminated"],"Adjust to expenses."),
     ("The 'pay yourself first' approach to emergency fund building means:",["Pay after all bills","*Automatically transfer to emergency fund BEFORE paying discretionary expenses","Pay only when extra exists","Pay last"],"Priority savings."),
     ("For financial math, savings goals use:",["No formulas","*Future value, present value, and annuity formulas to calculate required monthly contributions for any target","Only addition","Only subtraction"],"Applied TVM.")]
)
lessons[k]=v

# 5.4
k,v = build_lesson(5,4,"Short- & Long-Term Financial Planning",
    "<h3>Short- &amp; Long-Term Financial Planning</h3>"
    "<h4>Time Horizons</h4>"
    "<ul><li><b>Short-term (0–3 years):</b> Emergency fund, vacation, minor purchases.</li>"
    "<li><b>Medium-term (3–10 years):</b> Home down payment, car, graduate school.</li>"
    "<li><b>Long-term (10+ years):</b> Retirement, children's college, wealth building.</li></ul>"
    "<h4>Planning Framework</h4>"
    "<p>1. Define goals. 2. Set timelines. 3. Calculate required savings. 4. Choose appropriate accounts. 5. Automate. 6. Review and adjust.</p>",
    [("Financial Planning","The process of setting goals, assessing resources, and creating strategies to achieve financial objectives."),
     ("Time Horizon","The expected time period until a financial goal is needed; determines risk tolerance and investment choices."),
     ("Net Worth","Total assets minus total liabilities; the comprehensive measure of financial health."),
     ("Financial Milestone","Key target on the path to a larger goal (e.g., paying off credit cards before attacking student loans)."),
     ("Opportunity Cost","What you give up when choosing one option over another (e.g., spending now vs. investing for later).")],
    [("Short-term financial goals have a time horizon of:",["10+ years","5-10 years","*0–3 years","20+ years"],"Near-term goals."),
     ("Short-term goals should be funded with:",["Stocks","*Low-risk vehicles like savings accounts and CDs (money is needed soon)","Crypto","Long-term bonds"],"Safety first."),
     ("Medium-term goals (3-10 years) can include:",["Daily expenses","*Home down payment, car purchase, graduate school tuition","Only retirement","Only emergency fund"],"Mid-range planning."),
     ("Long-term goals (10+ years) typically include:",["Vacation","Emergency fund","*Retirement savings and children's college funds","This month's rent"],"Distant targets."),
     ("Net worth = ",["Income − Expenses","*Assets − Liabilities","Savings × Interest","Income × Time"],"Wealth measure."),
     ("If you have $50K in assets (savings, investments, property equity) and $30K liabilities (loans), net worth is:",["$30,000","$50,000","*$20,000","$80,000"],"50000 − 30000."),
     ("The financial planning lifecycle goes from _____ to _____.",["Spending to saving","*Accumulation (working years) to distribution (retirement years)","Borrowing to lending","Investing to saving"],"Lifecycle stages."),
     ("A 25-year-old's primary financial priorities should typically be:",["100% spending","*Build emergency fund → pay off high-interest debt → start retirement saving → invest for growth","Only retirement","Only debt"],"Priority order."),
     ("The Rule of 72 for doubling money at 7%: ≈ _____ years.",["7","*~10.3 years","15","20"],"72/7 ≈ 10.3."),
     ("Inflation of 3% means $100,000 in 20 years has the purchasing power of approximately:",["$100,000","$80,000","*~$55,368 (100000 × 0.97^20)","$40,000"],"Purchasing power erosion."),
     ("Planning for education: a 529 plan offers:",["No tax benefits","*Tax-free growth for qualified education expenses (state tax deductions in many states too)","Only for K-12","Only federal tax benefits"],"Education savings vehicle."),
     ("The cost of a 4-year public university (2024) averages approximately _____ total.",["$20,000","$50,000","*$100,000-$120,000 (tuition + room/board + fees)","$200,000"],"Current education cost."),
     ("Starting to save for a newborn's college ($120K in 18 years at 7%) requires approximately:",["$200/month","*~$278/month","$500/month","$700/month"],"College savings."),
     ("Life insurance needs are calculated based on:",["Only age","*Income replacement, outstanding debts, future education costs, and final expenses for dependents","Only health","Only assets"],"Protection planning."),
     ("A financial plan should be reviewed and updated:",["Never","Once in a lifetime","*At least annually and after major life events (marriage, baby, job change, etc.)","Only when losing money"],"Regular review."),
     ("Estate planning includes:",["Only a will","*Will, power of attorney, healthcare directive, beneficiary designations, and potentially a trust","Only life insurance","Nothing for young people"],"Comprehensive protection."),
     ("The 'financial independence' concept means:",["Having a job","*Having enough passive income or savings that working is optional — often calculated as 25× annual expenses","Being debt-free only","Having a high salary"],"FI number."),
     ("If annual expenses are $40,000, financial independence requires approximately:",["$400,000","$600,000","*$1,000,000 (25 × $40,000 using the 4% withdrawal rule)","$2,000,000"],"FI calculation."),
     ("Lifestyle creep is:",["Living below means","*Increasing spending as income rises, preventing savings rate from improving despite higher earnings","A budget strategy","A savings method"],"Wealth destroyer."),
     ("For financial math, financial planning integrates:",["Only one topic","*ALL previous concepts: compound interest, loans, investments, budgeting, taxes, and risk management into a comprehensive strategy","Only savings","Only investing"],"Comprehensive integration.")]
)
lessons[k]=v

# 5.5
k,v = build_lesson(5,5,"Budget Case Studies",
    "<h3>Budget Case Studies</h3>"
    "<h4>Case 1: Recent College Graduate</h4>"
    "<p>Income: $45,000/year ($3,200/month net). Budget: Rent $1,050, food $400, transport $350, loans $350, insurance $200, savings $400, discretionary $450.</p>"
    "<h4>Case 2: Young Family</h4>"
    "<p>Income: $85,000/year ($5,500/month net). Budget: Mortgage $1,650, childcare $1,200, food $600, utilities $250, insurance $350, cars $400, savings $550, discretionary $500.</p>",
    [("Budget Allocation","How income is distributed across expense categories — reveals financial priorities and potential imbalances."),
     ("Savings Rate","Percentage of income saved: a 12-15% rate is healthy; 20%+ accelerates wealth building."),
     ("Housing Cost Ratio","Housing expenses ÷ income; should stay below 30% for financial stability."),
     ("Lifestyle Design","Intentionally choosing spending priorities based on values, not defaults or social pressure."),
     ("Budget Flexibility","Building in 'flex' or buffer money for unexpected expenses within the budget framework.")],
    [("A recent graduate earning $3,200/month net with $1,050 rent spends _____ of income on housing.",["25%","*~33% (slightly above 30% guideline but common for new graduates in high-cost areas)","40%","50%"],"Housing ratio."),
     ("The graduate's $400 savings represents a savings rate of:",["10%","*12.5% ($400/$3,200) — a good start, with room to increase","15%","20%"],"Savings rate."),
     ("The graduate can increase savings by:",["Eliminating all fun","Quitting their job","*Finding a roommate to reduce rent, cooking more, or increasing income through side work","Borrowing more"],"Practical adjustments."),
     ("The young family spends $1,200/month on childcare, which is _____ of income.",["10%","15%","*~22% ($1,200/$5,500) — childcare is often the second-largest expense after housing","30%"],"Major family expense."),
     ("The family's combined housing + childcare is _____ of income.",["30%","40%","*~52% ($1,650+$1,200 = $2,850/$5,500) — very tight budget","60%"],"Budget pressure."),
     ("The family saves $550/month (10%). To reach 15%, they need to save:",["$250 more","*$275 more ($825 total = 15% of $5,500)","$500 more","$100 more"],"Savings target increase."),
     ("A single person earning $75,000 ($4,800/month net) following 50/30/20 should allocate:",["$3,000/$1,200/$600","*$2,400/$1,440/$960","$4,000/$500/$300","$3,500/$1,000/$300"],"50/30/20 applied."),
     ("If the graduate gets a $5,000 raise, the BEST use is:",["All new spending","*Split: increase savings rate + small lifestyle improvement (avoid full lifestyle creep)","All savings","All debt"],"Balanced approach."),
     ("A dual-income couple earning $120,000 total should build their budget on:",["Both full incomes","*Primarily one income — using the second for accelerated savings and debt payoff provides enormous security","Only the higher income","Only the lower income"],"Conservative planning."),
     ("The 'latte factor' in Case 1: the graduate's $5/day coffee habit costs _____ per year.",["$500","$1,000","*$1,825 (or 38% of their annual discretionary spending of $5,400)","$2,500"],"Small habit, big impact."),
     ("Case study analysis: which expense is easiest to reduce?",["Rent (locked in)","Student loans (fixed)","*Discretionary spending (food out, entertainment, subscriptions — most flexibility)","Insurance"],"Flexible category."),
     ("A budget that allocates 0% to savings is:",["Normal","Fine temporarily","*A crisis-level situation that will lead to debt when any unexpected expense occurs","Standard for young people"],"No buffer = vulnerability."),
     ("For both case studies, automated transfers for savings help because:",["Banks require it","It reduces income","*It removes the temptation to spend savings money — what you don't see, you don't spend","It increases taxes"],"Behavioral tool."),
     ("The family could reduce childcare costs by:",["Not having children","*Exploring subsidized programs, employer benefits, nanny shares, or FSA (Dependent Care FSA saves ~30% in taxes)","Eliminating childcare","Working less"],"Practical options."),
     ("Dependent Care FSA saves _____ on $5,000 of childcare expenses (25% tax bracket).",["$500","*$1,250 (pre-tax contribution saves ~25% in taxes on $5,000)","$2,500","$5,000"],"Tax savings."),
     ("Budget case studies help students understand:",["Only theory","*How real financial decisions involve trade-offs, priorities, and the math learned in class applied to actual scenarios","Only one formula","Nothing practical"],"Theory meets reality."),
     ("If the graduate increases savings from $400 to $600/month at 8% for 30 years, the additional $200/month adds:",["$72,000","$100,000","*~$298,000 (the extra $200 alone grows to ~$298K with compound interest!)","$500,000"],"Marginal savings power."),
     ("The most critical budget line for long-term wealth is:",["Entertainment","Food","*Savings/investments (consistently funding this category creates compound growth that builds wealth)","Housing"],"Savings priority."),
     ("Budget case studies demonstrate that financial math is:",["Only for class","*Directly applicable to daily life decisions that compound into major financial outcomes over years and decades","Only theoretical","Only for accountants"],"Real-world relevance."),
     ("The common thread in all successful budgets is:",["Earning more","*Spending intentionally: knowing where money goes and making conscious choices aligned with goals","Spending nothing","Avoiding all debt"],"Intentional spending.")]
)
lessons[k]=v

# 5.6
k,v = build_lesson(5,6,"Budgeting Technology Tools",
    "<h3>Budgeting Technology Tools</h3>"
    "<h4>Popular Tools</h4>"
    "<ul><li><b>YNAB (You Need A Budget):</b> Zero-based; every dollar assigned a job. ~$99/year.</li>"
    "<li><b>Mint/Credit Karma:</b> Free; auto-categorization from linked accounts.</li>"
    "<li><b>Spreadsheets:</b> Full customization; templates widely available.</li>"
    "<li><b>Bank apps:</b> Built-in spending trackers; round-up savings features.</li></ul>",
    [("YNAB","You Need A Budget — zero-based budgeting app that assigns every dollar a specific purpose."),
     ("Automated Categorization","Technology that automatically classifies transactions into spending categories (food, transport, etc.)."),
     ("Round-Up Savings","Feature that rounds purchases to the nearest dollar and saves the difference (e.g., $3.75 purchase → $0.25 saved)."),
     ("Spending Alerts","Notifications triggered when approaching or exceeding budget category limits."),
     ("Projected Cash Flow","Technology-generated forecast of future income and expenses based on historical patterns.")],
    [("YNAB's budgeting approach is:",["Percentage-based","*Zero-based (every dollar gets a job before it's spent — income minus all allocations = $0)","Envelope-only","Savings-first"],"Zero-based philosophy."),
     ("Mint/Credit Karma helps by:",["Picking investments","*Automatically categorizing spending from linked bank/credit accounts and showing trends","Creating budgets automatically","Lending money"],"Auto-tracking."),
     ("Round-up savings on $4.50 purchase with a $5 round-up:",["Saves $4.50","*Saves $0.50 (rounds to $5, difference goes to savings)","Saves $5","Saves nothing"],"Micro-savings."),
     ("If round-ups average $0.50 per transaction and you make 40 transactions/month:",["$10/month saved","*$20/month saved ($240/year — painless micro-savings)","$40/month saved","$200/month saved"],"Accumulated micro-savings."),
     ("Spending alerts are useful because:",["They're annoying","*They provide real-time awareness when approaching budget limits, preventing overspending","They block purchases","They reduce income"],"Real-time feedback."),
     ("The advantage of spreadsheets for budgeting is:",["They're required","Automatic categorization","*Full customization — you can build exactly the budget model you want with custom formulas and charts","They're simplest"],"Flexibility."),
     ("A disadvantage of spreadsheets is:",["Too expensive","Too rigid","*Require manual data entry (unless connected to bank APIs) and discipline to maintain","Too accurate"],"Manual work."),
     ("Bank apps with built-in budgeting features are good for:",["Replacing all budgeting tools","*Basic spending tracking — convenient since data is already there, but often limited in customization","Only checking balances","Only transfers"],"Convenience."),
     ("The best budgeting tool is:",["Always YNAB","Always Excel","Always Mint","*The one you actually use consistently (the tool matters less than the habit)"],"Consistency wins."),
     ("Financial dashboard tools (Personal Capital) combine:",["Only bank accounts","*Bank accounts, investments, credit cards, and loans into one view showing net worth and cash flow","Only investments","Only credit cards"],"Holistic view."),
     ("AI-powered budgeting insights can:",["Replace human judgment","*Identify spending patterns, predict upcoming expenses, and suggest optimization opportunities","Guarantee savings","Make all decisions"],"Smart assistance."),
     ("Automated bill pay reduces:",["Income","Savings","*Late payment fees and credit score damage from missed payments","Spending"],"Payment reliability."),
     ("Subscription management apps (Truebill/Rocket Money) help by:",["Adding subscriptions","*Identifying all recurring charges, highlighting unused services, and even canceling them for you","Only tracking income","Only for phones"],"Subscription control."),
     ("Couples should use budgeting tools that:",["Only one person uses","Track only one account","*Both partners can access and contribute to — transparency and alignment are key to financial harmony","Are the most expensive"],"Shared visibility."),
     ("For students, free tools like Mint are ideal because:",["They're the most powerful","*They provide adequate tracking at no cost while building the budgeting habit early","They're required by schools","They have no limitations"],"Accessible starting point."),
     ("Gamification in budgeting apps (progress bars, streaks, badges):",["Is meaningless","*Can make budgeting more engaging and help build consistent tracking habits","Replaces actual money management","Is only for kids"],"Behavioral motivation."),
     ("API connections to bank accounts in budgeting apps are:",["Risky to use","*Generally secure (using bank-level encryption and read-only access through official APIs)","Always dangerous","Never encrypted"],"Reasonable security."),
     ("Exporting budget data to CSV/Excel allows:",["Nothing useful","*Custom analysis, historical trend research, and integration with other financial planning tools","Only printing","Only sharing"],"Data portability."),
     ("The 2024 trend in budgeting technology is:",["Less automation","*AI-powered insights, automatic categorization improvement, and integration across all financial accounts","Fewer apps","Return to paper"],"Tech evolution."),
     ("For financial math, budgeting tools apply _____ to real money management.",["No math concepts","*Percentages, tracking, categorization, and visualization — making abstract financial math tangible and actionable","Only addition","Only one concept"],"Math made practical.")]
)
lessons[k]=v

# 5.7
k,v = build_lesson(5,7,"Lifestyle Choices & Financial Impact",
    "<h3>Lifestyle Choices &amp; Financial Impact</h3>"
    "<h4>Major Financial Decisions</h4>"
    "<ul><li><b>Housing:</b> Rent vs. buy; city vs. suburb. Can differ by $500-1,500/month.</li>"
    "<li><b>Transportation:</b> New car vs. used vs. public transit. $400-900/month range.</li>"
    "<li><b>Education:</b> Community college → university (save $30,000+) vs. 4-year private.</li>"
    "<li><b>Career:</b> High-cost city + high salary vs. low-cost area + lower salary.</li></ul>",
    [("Cost of Living","The amount needed to cover basic expenses in a particular area; varies dramatically by region."),
     ("Rent vs. Buy Decision","Financial comparison of renting vs. purchasing a home, considering down payment, maintenance, equity, and market conditions."),
     ("Total Cost of Ownership (Car)","Purchase price + insurance + fuel + maintenance + depreciation + registration — the TRUE cost of car ownership."),
     ("Opportunity Cost of Choices","The financial return foregone by choosing one lifestyle option over another."),
     ("Geographic Arbitrage","Living in a lower-cost area while earning income at higher-cost area rates (e.g., remote work).")],
    [("The difference between living in a high-cost vs. low-cost city can be _____ per year.",["$5,000","$10,000","*$20,000-$30,000+ (housing alone can differ by $1,000-2,000/month)","$1,000"],"Geographic impact."),
     ("A new car costs approximately _____ more per year in depreciation than a 3-year-old used car.",["$500","$1,000","*$3,000-5,000 (new cars lose 20% in year 1; used cars depreciate much less)","$10,000"],"New vs. used depreciation."),
     ("Total cost of car ownership includes:",["Only the payment","Only gas and insurance","*Payment + insurance + fuel + maintenance + depreciation + registration + parking","Only depreciation"],"Full TCO."),
     ("Average annual total cost of car ownership is approximately:",["$3,000","$6,000","*~$10,000-12,000 (AAA estimates for average sedan)","$2,000"],"True car cost."),
     ("Switching from a $10K/year car to a $3K/year transit pass saves $7,000/year. Invested at 8% for 30 years:",["$100,000","$200,000","*~$817,000","$1,000,000"],"Transportation wealth."),
     ("Community college for 2 years then university vs. 4-year university saves approximately:",["$5,000","$15,000","*$30,000-50,000+ (community college averages $4,000/year vs. $12,000-25,000/year at state university)","$100,000"],"Education strategy."),
     ("Renting vs. buying a home depends on:",["Always buy","Always rent","*Length of stay, local market conditions, opportunity cost of down payment, and lifestyle flexibility needs","Only location"],"Context-dependent."),
     ("The 'rent vs. buy' break-even is typically:",["Immediate","*5-7 years (if staying shorter, renting is often cheaper when factoring in closing costs, maintenance, and opportunity cost)","20 years","Never"],"Time-dependent."),
     ("A salary of $100K in NYC vs. $70K in Dallas (with cost-of-living adjustment) results in:",["NYC being much better","*Similar or better lifestyle in Dallas (lower housing, taxes, and general expenses can make $70K go further)","Exactly equal","Dallas always worse"],"COL context."),
     ("Cooking at home vs. eating out saves approximately _____ per person per month.",["$50","$100","*$200-400 (average restaurant meal costs 3-5× the home-cooked equivalent)","$1,000"],"Food spending."),
     ("$300/month saved by cooking, invested at 7% for 30 years:",["$100,000","*~$340,000","$500,000","$30,000"],"Kitchen wealth."),
     ("Subscription creep (adding streaming, gym, apps over years) can cost:",["Almost nothing","*$200-400+/month ($2,400-$4,800/year) — often more than people realize","$50/month maximum","$1,000/month"],"Creeping costs."),
     ("'Keeping up with the Joneses' (spending to match peers) leads to:",["Financial success","*Overspending, undersaving, and financial stress — spending based on appearance rather than values","Better relationships","Higher income"],"Social spending trap."),
     ("The concept of 'enough' in lifestyle design means:",["Deprivation","*Identifying the level of spending that maximizes happiness without sacrificing financial security","Spending everything","Extreme frugality"],"Optimal spending."),
     ("Research shows happiness increases with income up to about _____; after that, the effect plateaus.",["$30,000","$50,000","*~$75,000-100,000 (varies by region and family size)","$1,000,000"],"Happiness research."),
     ("The biggest lifestyle choice affecting long-term wealth is:",["Car brand","Restaurant frequency","*Housing choice (it's the largest expense — getting this right/wrong impacts everything else)","Clothing brand"],"Dominant expense."),
     ("Remote work enables 'geographic arbitrage' because you can:",["Work less","*Earn a high-cost-city salary while living in a lower-cost area, saving the difference","Avoid taxes","Work from anywhere for free"],"Modern advantage."),
     ("A frugal lifestyle that saves an extra $1,000/month at 8% for 30 years creates:",["$360,000","$500,000","*~$1,469,000 (compound interest on consistent savings)","$2,000,000"],"Frugality → wealth."),
     ("Lifestyle inflation (increasing spending with income) is the #1 reason:",["People save more","*High earners can still be financially stressed — earning more doesn't help if spending more too","People get rich","Investing works"],"Income ≠ wealth."),
     ("For financial math, lifestyle analysis applies:",["No math","*Compound interest, opportunity cost, NPV, and cost-benefit analysis to real decisions that span decades","Only simple addition","Only budgeting"],"Life-changing math.")]
)
lessons[k]=v

# 5.8
k,v = build_lesson(5,8,"Budget Adjustments & Life Changes",
    "<h3>Budget Adjustments &amp; Life Changes</h3>"
    "<h4>Triggers for Budget Revision</h4>"
    "<ul><li><b>Income changes:</b> Raise, job loss, side income, retirement.</li>"
    "<li><b>Life events:</b> Marriage, baby, home purchase, health crisis.</li>"
    "<li><b>Goal changes:</b> New priorities, completed goals, shifting timelines.</li></ul>"
    "<h4>Adjustment Strategy</h4>"
    "<p>1. Reassess income. 2. Re-prioritize goals. 3. Adjust allocations. 4. Implement and monitor.</p>",
    [("Budget Revision","Updating a budget to reflect changed circumstances — income, expenses, goals, or life events."),
     ("Income Adjustment","Recalculating budget allocations when income increases (raise/new job) or decreases (job loss/retirement)."),
     ("Life Event Budgeting","Adjusting finances for major changes: marriage (combined income), baby ($15K+/year), divorce, etc."),
     ("Financial Resilience","The ability to adapt financially to unexpected changes without crisis or excessive debt."),
     ("Windfall Management","Strategy for handling large one-time income (inheritance, bonus, tax refund, lottery): save, invest, or pay debt.")],
    [("A 10% raise on $50,000 gives $5,000 more. The smartest allocation is:",["Spend it all","*Split: increase savings rate + modest lifestyle improvement (e.g., 50% to savings, 50% to enjoyment)","Save 100%","Ignore it"],"Balanced approach."),
     ("Job loss requires immediately:",["Panic","*Cutting discretionary spending, filing for unemployment, assessing emergency fund runway, and seeking new income","Nothing","Increasing spending"],"Crisis response."),
     ("A baby adds approximately _____ per year in expenses.",["$2,000","$5,000","*$15,000-20,000 (childcare, diapers, food, healthcare, clothing, gear)","$50,000"],"Child cost reality."),
     ("Marriage affects budgets because:",["Nothing changes","*Combined income, shared expenses (potential savings), and aligned financial goals (or conflicts) change the entire picture","Only taxes change","Only housing changes"],"Partnership finance."),
     ("Buying a home changes the budget by adding:",["Only the mortgage payment","*Mortgage + property taxes + insurance + maintenance (1-3% of home value/year) + utilities increase","Only property taxes","No new expenses"],"Full homeownership cost."),
     ("A $3,000 bonus or tax refund should be:",["Spent immediately on wants","*Applied strategically: emergency fund (if not full) → high-interest debt → savings/investments","Ignored","All to checking"],"Intentional windfall use."),
     ("Retirement budget adjustments include:",["No changes needed","*Potentially lower income, no commute costs, higher healthcare costs, and shifting from saving to spending mode","Only more travel","Only less spending"],"Retirement transition."),
     ("Health crisis financial impact can include:",["No cost impact","*Medical bills + reduced income + increased insurance + potential disability — emergency fund and insurance are critical","Only emotional impact","Only small copays"],"Health + money."),
     ("When transitioning from two incomes to one (e.g., parental leave):",["Continue same spending","*Budget BEFORE the change: test living on one income for 3-6 months while saving the second income","Borrow to maintain lifestyle","Wait and see"],"Proactive planning."),
     ("Divorce typically reduces household wealth by _____ due to splitting assets and maintaining two households.",["10%","25%","*40-50%+","75%"],"Financial impact."),
     ("Moving to a higher-cost city requires:",["No budget changes","*Recalculating ALL budget categories: housing (+30-100%), transportation, food, and adjusting savings goals","Only rent adjustment","Earning the same"],"Comprehensive recalculation."),
     ("Annual inflation of 3% means budgets must increase by _____ per year just to maintain the same lifestyle.",["0%","1%","*3% (expenses naturally rise — budget must account for this)","10%"],"Inflation adjustment."),
     ("A car accident requiring $5,000 in repairs (with $1,000 deductible) affects your budget for _____ months if absorbing from monthly budget.",["1","*2-4 months (depending on how much 'flex' money exists monthly — this is why emergency funds matter)","10","0"],"Unplanned expense."),
     ("After paying off a $300/month student loan, the freed-up money should:",["Go to spending","*Be redirected to the next financial priority (invest, next debt, or increase savings — don't let it leak into spending)","Be ignored","Go to a new loan"],"Debt payoff redirect."),
     ("Periodic budget reviews should check:",["Only income","Only expenses","*Income, expenses, savings rate, debt progress, goal alignment, and any upcoming life changes","Only net worth"],"Comprehensive review."),
     ("A promotion bringing $10,000 more annually creates the most wealth if _____ is saved/invested.",["0%","25%","50%","*At least 50% — ideally even more, since you were already living on less before the raise"],"Savings first."),
     ("Having a child ages 0-17 costs approximately _____ total (2024, middle-income family).",["$100,000","*~$310,000 (USDA estimate, NOT including college)","$50,000","$500,000"],"Total child cost."),
     ("A financial buffer in the budget (5-10% unassigned) helps because:",["It wastes money","*It absorbs small unexpected expenses without derailing the entire budget — reducing stress and maintaining consistency","It earns interest","It's required"],"Built-in flexibility."),
     ("The most successful long-term budgeters:",["Never adjust","*Regularly review and adjust their budget as life changes — flexibility keeps the plan relevant and motivating","Use the same budget forever","Don't track anything"],"Adaptive planning."),
     ("For financial math, budget adjustments demonstrate that personal finance is:",["A one-time calculation","*A dynamic, ongoing process requiring regular application of financial math concepts to changing real-world circumstances","Only theoretical","Only about formulas"],"Living mathematics.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 5: wrote {len(lessons)} lessons")
