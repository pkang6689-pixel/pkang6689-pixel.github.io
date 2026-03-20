#!/usr/bin/env python3
"""Financial Math Unit 1 – Financial Literacy Fundamentals (8 lessons)."""
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

# 1.1
k,v = build_lesson(1,1,"Importance of Financial Literacy",
    "<h3>Importance of Financial Literacy</h3>"
    "<p><b>Financial literacy</b> is the ability to understand and effectively manage personal finances. It includes budgeting, investing, debt management, and planning for the future.</p>"
    "<h4>Why It Matters</h4>"
    "<ul><li>~56% of Americans cannot cover a $1,000 emergency expense from savings.</li>"
    "<li>Average US household credit card debt: ~$6,500.</li>"
    "<li>Financial stress is the #1 source of stress for adults.</li>"
    "<li>Financially literate individuals save more, invest better, and retire earlier.</li></ul>",
    [("Financial Literacy","The ability to understand and effectively use financial skills including budgeting, investing, and debt management."),
     ("Personal Finance","Managing individual or family financial activities: income, spending, saving, investing, and protection."),
     ("Compound Interest","Interest earned on both principal and accumulated interest — Einstein reportedly called it the 'eighth wonder of the world.'"),
     ("Inflation","The rate at which prices increase over time, reducing the purchasing power of money (~2-3% annually on average)."),
     ("Net Worth","Total assets minus total liabilities — the fundamental measure of financial health.")],
    [("Financial literacy includes the ability to:",["Only save money","Only spend wisely","*Understand and effectively manage budgeting, investing, debt, and financial planning","Only balance a checkbook"],"Comprehensive skill set."),
     ("Approximately _____ of Americans cannot cover a $1,000 emergency expense from savings.",["10%","25%","*~56%","90%"],"Widespread financial vulnerability."),
     ("Compound interest is powerful because it:",["Only applies to savings","*Earns returns on both principal AND previously earned interest, creating exponential growth","Only applies to debt","Only works for the wealthy"],"Growth on growth."),
     ("Inflation at 3% means that $100 today will buy only _____ worth of goods in 10 years.",["$100","$90","*~$74 (purchasing power erodes over time)","$50"],"Purchasing power erosion."),
     ("Net worth is calculated as:",["Income minus expenses","*Total assets minus total liabilities","Only savings account balance","Only investment value"],"Assets − liabilities."),
     ("The #1 source of stress for American adults is:",["Health","Relationships","Work","*Financial stress"],"Money worries dominate."),
     ("Financial literacy education leads to:",["No measurable improvement","*Higher savings rates, better investment returns, less debt, and earlier retirement","Only higher income","Only less spending"],"Measurable benefits."),
     ("The time value of money means:",["Money loses value in banks","*A dollar today is worth more than a dollar in the future (because today's dollar can be invested to grow)","Time doesn't affect money","Only inflation matters"],"Core financial concept."),
     ("People with higher financial literacy tend to:",["Take more unnecessary risks","*Plan better for retirement, carry less debt, and build larger emergency funds","Earn higher salaries automatically","Avoid investing entirely"],"Better outcomes."),
     ("Which is NOT a component of personal finance?",["Budgeting","Investing","*Meteorology","Insurance"],"Not finance-related."),
     ("The Rule of 72 estimates:",["Monthly expenses","*How long it takes money to double at a given interest rate (72 ÷ rate = years)","Tax obligations","Insurance premiums"],"Quick doubling estimate."),
     ("At 6% annual return, money doubles in approximately:",["6 years","*12 years (72 ÷ 6)","18 years","24 years"],"Rule of 72 applied."),
     ("Financial decisions should be based on:",["Emotions only","Only what friends do","*Informed analysis of costs, benefits, risks, and personal goals","Only impulse"],"Rational decision-making."),
     ("A financially literate person understands the difference between:",["Only checking and savings","*Assets (things you own that increase in value) and liabilities (debts that cost you money)","Only cash and credit","Only stocks and bonds"],"Asset vs. liability."),
     ("The FDIC insures bank deposits up to:",["$10,000","$100,000","*$250,000 per depositor per institution","$1,000,000"],"Deposit insurance limit."),
     ("Delayed gratification in finance means:",["Never spending money","*Choosing to wait for a larger future reward rather than taking a smaller immediate reward","Only saving for retirement","Avoiding all purchases"],"Patience pays."),
     ("Financial literacy should be taught because:",["Schools already cover it thoroughly","*Many people make costly financial mistakes due to lack of knowledge, and outcomes can be dramatically improved","It's only for business majors","It's too complex for most people"],"Education = empowerment."),
     ("The pay-yourself-first strategy means:",["Paying bills first","*Automatically saving/investing a portion of income BEFORE spending on anything else","Paying off debt first","Spending first, saving what's left"],"Savings priority."),
     ("Financial illiteracy costs the average American approximately _____ per year in fees and poor decisions.",["$100","*~$1,500+","$50","$10,000"],"Real cost of ignorance."),
     ("The most important financial habit to develop is:",["Making more money","*Living below your means (spending less than you earn) and investing the difference","Avoiding all risk","Only using cash"],"Foundational habit.")]
)
lessons[k]=v

# 1.2
k,v = build_lesson(1,2,"Sources of Income (wages, salaries, investments)",
    "<h3>Sources of Income</h3>"
    "<h4>Types</h4>"
    "<ul><li><b>Earned income:</b> Wages (hourly), salaries (annual), tips, commissions, bonuses.</li>"
    "<li><b>Investment income:</b> Dividends, interest, capital gains, rental income.</li>"
    "<li><b>Passive income:</b> Income requiring minimal ongoing effort (royalties, rental, business ownership).</li>"
    "<li><b>Transfer payments:</b> Government benefits (Social Security, unemployment, disability).</li></ul>"
    "<h4>Gross vs. Net Income</h4>"
    "<p><b>Gross income</b> = total earnings before deductions. <b>Net income</b> = take-home pay after taxes, insurance, retirement contributions.</p>",
    [("Earned Income","Money received from labor: wages, salary, tips, commissions, and bonuses."),
     ("Passive Income","Income requiring little active effort: rental income, royalties, dividends from investments."),
     ("Gross Income","Total earnings before any deductions (taxes, insurance, retirement contributions)."),
     ("Net Income","Take-home pay after all deductions — the money actually available to spend or save."),
     ("Capital Gains","Profit from selling an asset (stock, property) for more than you paid for it.")],
    [("Wages are typically paid on a(n) _____ basis.",["Annual","*Hourly","Monthly only","One-time"],"Per hour worked."),
     ("Salary differs from wages in that salary is:",["Paid hourly","*A fixed annual amount paid in regular installments regardless of hours worked","Always higher","Only for executives"],"Fixed annual compensation."),
     ("Gross income minus deductions equals:",["Gross pay","Total earnings","*Net income (take-home pay)","Bonus pay"],"After deductions."),
     ("Common paycheck deductions include:",["Only taxes","*Federal/state income taxes, FICA (Social Security + Medicare), health insurance, and retirement contributions","Only insurance","Only retirement"],"Multiple deductions."),
     ("FICA taxes fund:",["Only income tax","*Social Security (6.2%) and Medicare (1.45%) — totaling 7.65% of gross wages","Only state programs","Only military"],"Payroll taxes."),
     ("Investment income includes:",["Only wages","*Dividends, interest, capital gains, and rental income","Only tips","Only salary"],"Returns on capital."),
     ("A capital gain occurs when you:",["Receive your paycheck","*Sell an asset for more than you paid for it","Lose money on a stock","Receive dividends"],"Profit from sale."),
     ("Passive income is income that:",["Requires no initial effort","*Requires minimal ongoing effort after initial setup (e.g., rental property, royalties, dividend stocks)","Is tax-free","Is only for businesses"],"Reduced ongoing effort."),
     ("If someone earns $50,000 gross salary and takes home $38,000, their effective tax/deduction rate is:",["50%","38%","*24% (($50,000 − $38,000) ÷ $50,000)","12%"],"Effective rate calculation."),
     ("Diversified income sources are important because:",["One source is sufficient","*Multiple income streams reduce financial risk if one source is lost","It's required by law","Only wealthy people need this"],"Risk reduction."),
     ("Commission-based income is common in:",["Education","*Sales (real estate, car sales, financial services) — typically a percentage of sales made","Government","Healthcare"],"Sales-based pay."),
     ("Transfer payments include:",["Only wages","*Government benefits: Social Security, unemployment insurance, disability, welfare, veterans' benefits","Only investment income","Only gifts"],"Government transfers."),
     ("A W-2 form shows:",["Only your tax liability","*Your total earnings and taxes withheld from employment for the year","Only your net worth","Only state taxes"],"Annual earnings statement."),
     ("A 1099 form is issued for:",["Regular employment","*Independent contractor income, interest, dividends, and other non-employment income","Only wages","Only salary"],"Non-employment income."),
     ("Overtime pay (for hourly workers) is typically:",["Regular rate","*1.5× the regular hourly rate for hours exceeding 40 per week (under FLSA)","Double the rate","No extra pay"],"Time and a half."),
     ("The federal minimum wage (2024) is:",["$10.00/hr","$5.00/hr","*$7.25/hr (though many states have higher minimums)","$15.00/hr"],"Federal floor."),
     ("Benefits like health insurance and 401(k) matching are considered:",["Not income","*Part of total compensation (valuable beyond base salary — can add 20-30% to total comp)","Only for executives","Guaranteed by law"],"Total compensation."),
     ("Side income or 'gig' economy work:",["Is not taxable","*Is taxable income that must be reported, even if no W-2 is issued","Is always passive","Doesn't count as income"],"All income is taxable."),
     ("Interest income from a savings account is an example of:",["Earned income","*Investment income (money your money earns)","Passive income only","Transfer payment"],"Return on deposits."),
     ("Understanding income sources matters because:",["Income is automatic","*Knowing how income is earned, taxed, and diversified is essential for financial planning and wealth building","Only one source matters","All income is the same"],"Income literacy.")]
)
lessons[k]=v

# 1.3
k,v = build_lesson(1,3,"Budgeting Basics",
    "<h3>Budgeting Basics</h3>"
    "<p>A <b>budget</b> is a plan for how to allocate income to expenses, savings, and investments.</p>"
    "<h4>The 50/30/20 Rule</h4>"
    "<ul><li><b>50%</b> Needs: housing, food, utilities, insurance, minimum debt payments.</li>"
    "<li><b>30%</b> Wants: entertainment, dining out, hobbies, subscriptions.</li>"
    "<li><b>20%</b> Savings/Debt repayment: emergency fund, retirement, extra debt payments.</li></ul>"
    "<h4>Zero-Based Budgeting</h4>"
    "<p>Every dollar is assigned a purpose: Income − All allocations = $0. Forces intentional spending.</p>",
    [("Budget","A financial plan allocating income to expenses, savings, and investments over a specific period."),
     ("50/30/20 Rule","Budget guideline: 50% needs, 30% wants, 20% savings and debt repayment."),
     ("Zero-Based Budget","Budget where every dollar of income is assigned a specific purpose (income minus all allocations = $0)."),
     ("Fixed Expenses","Costs that stay the same each period: rent/mortgage, car payment, insurance premiums."),
     ("Variable Expenses","Costs that fluctuate: groceries, utilities, entertainment, clothing.")],
    [("The 50/30/20 rule allocates _____ to needs, _____ to wants, and _____ to savings.",["40/40/20","60/20/20","*50/30/20","70/20/10"],"Standard guideline."),
     ("In the 50/30/20 rule, 'needs' include:",["Only food","*Housing, utilities, groceries, insurance, transportation, and minimum debt payments","Only rent","Entertainment"],"Essential expenses."),
     ("Zero-based budgeting means:",["Spending zero dollars","Having zero savings","*Assigning every dollar of income a specific purpose so income minus allocations equals zero","Only saving money"],"Every dollar planned."),
     ("Fixed expenses differ from variable expenses in that they:",["Change monthly","*Remain the same each billing period (rent, car payment, insurance)","Are always larger","Are optional"],"Predictable costs."),
     ("If someone earns $4,000/month and follows the 50/30/20 rule, savings should be:",["$400","$600","*$800 (20% × $4,000)","$1,200"],"20% savings."),
     ("The first step in creating a budget is:",["Cutting all spending","*Tracking current income and expenses to understand where money actually goes","Opening a savings account","Setting investment goals"],"Know your baseline."),
     ("A budget surplus occurs when:",["Expenses exceed income","*Income exceeds expenses (positive cash flow — money left over for savings/investing)","Income equals expenses","You have debt"],"Positive cash flow."),
     ("A budget deficit means:",["You have savings","*Expenses exceed income (negative cash flow — you're spending more than you earn)","Income equals expenses","You're debt-free"],"Spending more than earning."),
     ("Discretionary spending refers to:",["Bills and taxes","*Non-essential purchases you choose to make (entertainment, dining out, hobbies)","Fixed expenses","Debt payments"],"Optional spending."),
     ("An envelope budgeting system works by:",["Using electronic payments only","*Putting cash for each spending category in separate envelopes — when an envelope is empty, that category is done for the month","Only tracking expenses","Only saving money"],"Physical cash limits."),
     ("The biggest budgeting mistake most people make is:",["Saving too much","*Not tracking their spending (most people significantly underestimate what they spend)","Having a budget at all","Being too strict"],"Awareness gap."),
     ("Housing costs should ideally not exceed _____ of gross income.",["50%","*~28-30% (common lending guideline; lower is better)","10%","45%"],"Housing affordability."),
     ("A budget should be reviewed and adjusted:",["Never","Annually","*Monthly (at minimum) to account for changing circumstances","Only when income changes"],"Regular review."),
     ("Budgeting apps and spreadsheets help by:",["Making more money","*Automating tracking, categorizing expenses, showing trends, and alerting to overspending","Investing for you","Only for wealthy people"],"Technology assists."),
     ("An effective budget balances:",["Only savings","Only spending","*Current needs, future goals, and enjoyment of life (sustainable balance)","Only debt repayment"],"Balanced approach."),
     ("The pay-yourself-first approach to budgeting means:",["Pay bills first","*Automatically transfer savings/investments BEFORE spending on anything else","Save what's left","Skip savings when tight"],"Priority saving."),
     ("Budget categories should include:",["Only bills","*All expenses: housing, food, transport, insurance, debt, entertainment, clothing, personal care, savings, and giving","Only big items","Only monthly bills"],"Comprehensive categories."),
     ("Irregular expenses (car repair, holidays) should be budgeted by:",["Ignoring them until they occur","*Setting aside money monthly in a sinking fund for expected irregular costs","Only using credit cards","Reducing other categories temporarily"],"Sinking funds."),
     ("The purpose of a budget is NOT to:",["Track spending","Plan savings","*Restrict all enjoyment of life (it's a tool for intentional spending, not deprivation)","Manage debt"],"Tool, not punishment."),
     ("For financial math, budgeting connects to:",["Nothing else","*All other topics: interest, debt management, investing, taxes, and long-term financial planning","Only savings","Only spending"],"Foundation for everything.")]
)
lessons[k]=v

# 1.4
k,v = build_lesson(1,4,"Needs vs. Wants",
    "<h3>Needs vs. Wants</h3>"
    "<p><b>Needs</b> are essential for survival and basic functioning: food, shelter, clothing, healthcare, transportation to work.</p>"
    "<p><b>Wants</b> are things that improve quality of life but aren't essential: dining out, streaming services, designer clothing, vacations.</p>"
    "<h4>Gray Areas</h4>"
    "<p>Many expenses fall between needs and wants. A smartphone may be a need (for work) but the latest model is a want. Basic transportation is a need; a luxury car is a want.</p>",
    [("Needs","Essential expenses required for survival and basic functioning: food, shelter, healthcare, basic clothing, transportation."),
     ("Wants","Non-essential expenses that enhance quality of life: entertainment, dining out, luxury items, vacations."),
     ("Opportunity Cost","The value of the next-best alternative given up when making a choice."),
     ("Lifestyle Inflation","Increasing spending as income rises — upgrading wants to feel like needs."),
     ("Delayed Gratification","Choosing to wait for a better outcome rather than taking an immediate, smaller reward.")],
    [("Basic groceries for home cooking are classified as a:",["Want","*Need (food is essential for survival)","Luxury","Neither"],"Essential expense."),
     ("A streaming subscription (Netflix) is classified as a:",["Need","*Want (entertainment that enhances life but isn't essential)","Necessity","Basic requirement"],"Non-essential."),
     ("The distinction between needs and wants is important for budgeting because:",["All expenses are equal","*Needs should be prioritized; wants can be reduced or eliminated when money is tight","Wants are always bad","Needs never change"],"Priority setting."),
     ("Lifestyle inflation occurs when:",["Income decreases","*Spending increases proportionally with income, preventing wealth building despite earning more","Prices remain stable","Savings increase"],"Spending rises with income."),
     ("A smartphone for someone who needs it for work is:",["Only a want","*A need (the device) but the latest premium model may be a want (basic phone would suffice)","Neither need nor want","Always a luxury"],"Context matters."),
     ("Opportunity cost of buying a $1,000 designer bag is:",["Nothing","$1,000","*The value of what else that $1,000 could have been used for (e.g., invested, saving, emergency fund)","Only the bag"],"What you give up."),
     ("Which is generally a need?",["Concert tickets","Latest gaming console","*Health insurance","Designer clothing"],"Essential protection."),
     ("The 'latte factor' illustrates how:",["Coffee is essential","*Small daily expenses ($5 coffee × 365 days = $1,825/year) add up significantly over time","Only big purchases matter","Budgets are unnecessary"],"Small amounts compound."),
     ("A practical approach to needs vs. wants is:",["Never buy wants","Buy everything you want","*Cover all needs first, then allocate remaining funds to wants based on priorities","Ignore the distinction"],"Prioritize, then enjoy."),
     ("Basic transportation to work is a _____, while a brand-new luxury car is a _____.",["Want; need","*Need; want","Both needs","Both wants"],"Function vs. luxury."),
     ("When distinguishing needs from wants, consider:",["Only price","*Whether you could survive and function without it — and if a less expensive alternative would serve the same purpose","Only brand","Only convenience"],"Essential function test."),
     ("Impulse purchases are often:",["Well-planned needs","*Wants bought on emotion without considering budget impact or opportunity cost","Always bad","Always small"],"Emotional spending."),
     ("Housing is a need, but _____ is often a want.",["Any apartment","*The size, location, or luxury level beyond basic adequate shelter","Any shelter","Renting"],"Basic vs. premium."),
     ("Utilities (electricity, water) are needs, but:",["They can't be reduced","*Usage levels can vary — running AC at 68°F vs. 75°F represents the need/want spectrum","All utility costs are fixed","They're actually wants"],"Efficiency matters."),
     ("Healthcare is a need, and health insurance is:",["Optional","*Also a need (one medical emergency without insurance can cause financial ruin — average ER visit: ~$2,200)","Only for the sick","Too expensive to be a need"],"Essential protection."),
     ("Children's basic needs include:",["Only food","*Food, shelter, clothing, healthcare, and education","Only toys","Only entertainment"],"Comprehensive child needs."),
     ("The 'wants' category in budgeting should be:",["Eliminated entirely","*Maintained in moderation — a budget that allows no enjoyment is unsustainable","All discretionary income","More than 50%"],"Sustainable balance."),
     ("Peer pressure often leads to spending on _____ disguised as _____.",["Needs; wants","*Wants disguised as needs ('everyone has one; I need it too')","Only needs","Only necessities"],"Social pressure."),
     ("A financially healthy approach is:",["Never buying wants","Buying everything","*Consciously choosing which wants bring the most value and joy after all needs are met","Ignoring money"],"Intentional spending."),
     ("Understanding needs vs. wants helps with all of these EXCEPT:",["Budget creation","Spending priorities","*Predicting stock market performance","Debt reduction"],"Not related to investing performance.")]
)
lessons[k]=v

# 1.5
k,v = build_lesson(1,5,"Opportunity Cost in Financial Decisions",
    "<h3>Opportunity Cost</h3>"
    "<p><b>Opportunity cost</b> is the value of the best alternative forgone when making a choice. Every financial decision has an opportunity cost.</p>"
    "<h4>Examples</h4>"
    "<ul><li>Spending $5,000 on vacation vs. investing it (at 8% for 30 years: ~$50,000).</li>"
    "<li>Attending college: tuition + 4 years of potential wages vs. higher lifetime earnings.</li>"
    "<li>Buying a car with cash vs. investing and financing at low interest.</li></ul>",
    [("Opportunity Cost","The value of the next-best alternative given up when a choice is made."),
     ("Trade-Off","A situation where gaining something requires giving up something else."),
     ("Sunk Cost","Money already spent that cannot be recovered — should NOT influence future decisions."),
     ("Marginal Analysis","Comparing the additional benefit vs. additional cost of a decision."),
     ("Cost-Benefit Analysis","Systematic comparison of all costs and benefits of a decision to determine the best option.")],
    [("Opportunity cost is defined as:",["The price of a product","*The value of the best alternative you give up when making a choice","Only monetary cost","The worst possible outcome"],"What you forgo."),
     ("If you invest $5,000 at 8% for 30 years instead of spending it on vacation, it grows to approximately:",["$10,000","$25,000","*~$50,000","$100,000"],"Power of investing."),
     ("The opportunity cost of attending 4-year college includes:",["Only tuition","*Tuition + lost wages during those 4 years (though lifetime earnings are typically much higher with a degree)","Only lost wages","No cost since college is an investment"],"Full cost analysis."),
     ("A sunk cost is:",["A future expense","*Money already spent that cannot be recovered and should not influence future decisions","A savings opportunity","An investment"],"Don't throw good money after bad."),
     ("Continuing to watch a bad movie you paid $15 for because 'you already paid' is an example of:",["Good decision-making","*Sunk cost fallacy (the $15 is gone regardless; staying wastes your time too)","Opportunity cost","Marginal analysis"],"Sunk cost fallacy."),
     ("Every financial decision involves opportunity cost because:",["Money is infinite","*Resources (money, time) are limited — choosing one option means giving up another","Only expensive purchases do","Only investment decisions do"],"Scarcity forces choices."),
     ("The opportunity cost of keeping $10,000 in a checking account (0% interest) vs. investing at 7% is:",["$0","*~$700 per year in lost investment returns (growing larger each year due to compounding)","$10,000","$100"],"Idle money has a cost."),
     ("Marginal analysis asks:",["What's the total cost?","*Does the additional benefit of one more unit exceed the additional cost?","What's the average cost?","What's the opportunity cost?"],"At the margin."),
     ("A trade-off differs from opportunity cost in that:",["They're identical","*A trade-off is the general concept of giving something up; opportunity cost is the VALUE of the specific best alternative forgone","Trade-offs are worse","Opportunity cost is broader"],"Value of the specific forgone alternative."),
     ("Renting vs. buying a house involves opportunity costs such as:",["Only the monthly payment difference","*Down payment investment returns, maintenance costs, flexibility, equity building, and tax implications","No opportunity costs","Only one factor"],"Multi-factor decision."),
     ("Making a financial decision without considering opportunity cost leads to:",["Better decisions","*Potentially suboptimal choices because you haven't evaluated what you're giving up","The same result","No consequence"],"Incomplete analysis."),
     ("The opportunity cost of paying off a 4% mortgage early instead of investing at 8% is:",["0%","*~4% return differential (you earn 4% less than you could have by investing instead)","4%","8%"],"Interest rate comparison."),
     ("Time has opportunity cost because:",["Time is unlimited","*Hours spent on one activity can't be spent on another — time spent commuting is time not spent working, learning, or with family","Only money has opportunity cost","Time is free"],"Most valuable resource."),
     ("A cost-benefit analysis helps with financial decisions by:",["Only listing costs","Only listing benefits","*Systematically comparing ALL costs against ALL benefits to identify the best option","Only using math"],"Structured decision-making."),
     ("When choosing between investing in stocks vs. bonds, opportunity cost is:",["Always zero","*The return you give up on the option you don't choose (choose bonds = give up potentially higher stock returns, but with less risk)","Only for stocks","Only for bonds"],"Return trade-off."),
     ("The concept of 'nothing is free' in economics relates to opportunity cost because:",["Everything costs money","*Even 'free' things cost time and attention — every choice has an opportunity cost","Only paid items have cost","Free items have zero cost"],"Even free has a cost."),
     ("Calculated opportunity cost helps avoid:",["All risk","*Impulsive decisions by forcing consideration of alternatives before committing resources","All spending","All investing"],"Better decision quality."),
     ("For a business, the opportunity cost of using retained earnings for expansion is:",["Nothing","*The returns those funds could have earned in alternative investments or as dividends to shareholders","Only the expansion cost","Only one factor"],"Capital allocation."),
     ("Opportunity cost is a _____ concept in financial math.",["Minor","*Fundamental (it underlies nearly every financial decision from spending to investing to career choices)","Optional","Advanced only"],"Core principle."),
     ("The best financial decisions are made by:",["Ignoring alternatives","*Explicitly considering opportunity costs of each option and choosing the one with the greatest net benefit","Only looking at price","Going with gut feeling"],"Informed comparison.")]
)
lessons[k]=v

# 1.6
k,v = build_lesson(1,6,"Short-Term vs. Long-Term Goals",
    "<h3>Financial Goals</h3>"
    "<h4>Short-Term Goals (< 1 year)</h4>"
    "<ul><li>Build emergency fund ($500–$1,000 starter).</li>"
    "<li>Pay off a specific credit card.</li>"
    "<li>Save for a vacation or purchase.</li></ul>"
    "<h4>Medium-Term Goals (1–5 years)</h4>"
    "<ul><li>Build full emergency fund (3–6 months expenses).</li>"
    "<li>Save for down payment on house or car.</li>"
    "<li>Pay off student loans.</li></ul>"
    "<h4>Long-Term Goals (5+ years)</h4>"
    "<ul><li>Retirement savings (start early: compound interest!).</li>"
    "<li>College fund for children.</li>"
    "<li>Achieve financial independence.</li></ul>",
    [("SMART Goals","Financial goals that are Specific, Measurable, Achievable, Relevant, and Time-bound."),
     ("Emergency Fund","Savings covering 3–6 months of essential expenses for unexpected events (job loss, medical emergency)."),
     ("Financial Independence","Having sufficient passive income or savings to cover living expenses without active employment."),
     ("Down Payment","Initial upfront payment when purchasing an asset (typically 3–20% for a home)."),
     ("Dollar-Cost Averaging","Investing fixed amounts at regular intervals regardless of market price — reduces timing risk.")],
    [("A short-term financial goal is typically achieved within:",["10 years","5 years","*Less than 1 year","Just one day"],"Near-term targets."),
     ("An emergency fund should cover:",["1 week of expenses","*3–6 months of essential living expenses","1 year of expenses","Only one emergency"],"Financial safety net."),
     ("SMART goals are:",["Only for businesses","*Specific, Measurable, Achievable, Relevant, and Time-bound","Only for investments","Optional for finance"],"Goal-setting framework."),
     ("'Save $5,000 for a car down payment by December 2025' is an example of:",["A vague goal","*A SMART goal (specific amount, measurable, achievable, relevant, time-bound)","An impossible goal","A long-term goal"],"Well-defined target."),
     ("Starting retirement savings at age 25 vs. 35 makes a huge difference because:",["10 years doesn't matter","*Compound interest has 10 extra years to work — starting at 25 can result in nearly DOUBLE the retirement savings as starting at 35","Only small accounts grow","Savings rates are the same"],"Time is the biggest advantage."),
     ("If you invest $200/month starting at age 25 (at 8% return), by age 65 you'd have approximately:",["$96,000","*~$700,000","$200,000","$2,000,000"],"Compound growth over 40 years."),
     ("If you start the same $200/month at age 35 (10 years later), by 65 you'd have approximately:",["$700,000","*~$300,000 (less than half despite only starting 10 years later)","$500,000","$100,000"],"10 years costs ~$400,000."),
     ("Medium-term financial goals (1–5 years) include:",["Only retirement","*Saving for a down payment, paying off student loans, building full emergency fund","Only emergency fund","Only daily expenses"],"1–5 year targets."),
     ("Financial goal prioritization should typically start with:",["Investing in stocks","*Building a starter emergency fund, then paying off high-interest debt, then building full emergency fund","Buying a home","Saving for vacation"],"Foundation first."),
     ("Automating savings helps achieve goals because:",["It's required by law","*It removes the temptation to spend first (pay-yourself-first becomes automatic)","It earns more interest","Banks require it"],"Remove human weakness."),
     ("A sinking fund is:",["A failed investment","*Regular savings set aside for a specific planned future expense (vacation, new car, annual insurance premium)","An emergency fund","A retirement account"],"Planned savings."),
     ("Dollar-cost averaging works by:",["Timing the market perfectly","*Investing a fixed amount regularly regardless of market price, which averages out the cost per share over time","Only buying at low prices","Only investing large sums"],"Disciplined investing."),
     ("The biggest obstacle to achieving financial goals is usually:",["Low income","*Lack of a specific plan and follow-through (most people have vague goals rather than SMART goals)","Bad luck","High taxes"],"Plan + action."),
     ("Financial independence means:",["Being wealthy","*Having enough passive income or savings to cover living expenses without needing to work for money","Never spending money","Only having investments"],"Freedom from paycheck dependence."),
     ("The FIRE movement (Financial Independence, Retire Early) focuses on:",["Spending more","*Extreme savings rates (50–70% of income) and investing to achieve early financial independence","Only earning more","Only reducing taxes"],"Aggressive savings."),
     ("Short-term savings should be kept in _____ accounts; long-term in _____ accounts.",["Stocks; bonds","*High-yield savings/CDs (safe, liquid); retirement and investment accounts (growth potential)","Checking; savings","Only one type"],"Match timeline to vehicle."),
     ("Adjusting financial goals over time is:",["A sign of failure","*Normal and necessary — life circumstances change, so goals should be reviewed and updated regularly","Unnecessary","Cheating"],"Flexible planning."),
     ("Competing financial goals (e.g., save vs. pay debt) should be handled by:",["Ignoring one","*Prioritizing based on interest rates and urgency, potentially doing both at reduced levels","Only focusing on one","Doing neither until you can afford both"],"Balanced approach."),
     ("Writing down financial goals increases the chance of achieving them because:",["It doesn't help","*It creates commitment, clarity, and accountability — studies show written goals are significantly more likely to be achieved","Only contracts matter","It's just paperwork"],"Written commitment."),
     ("For financial math, goal-setting connects to:",["Nothing else","*Interest calculations, investment planning, debt repayment schedules, and time-value-of-money concepts","Only budgeting","Only one topic"],"Foundation for calculations.")]
)
lessons[k]=v

# 1.7
k,v = build_lesson(1,7,"Case Studies in Personal Finance",
    "<h3>Case Studies in Personal Finance</h3>"
    "<h4>Case 1: The Power of Starting Early</h4>"
    "<p>Investor A saves $200/month from age 22–32 (10 years, $24,000 total) then stops. Investor B saves $200/month from age 32–62 (30 years, $72,000 total). At 8% return, Investor A has MORE at 62 (~$470,000 vs. ~$300,000) despite investing less, because of compound interest and time.</p>"
    "<h4>Case 2: Debt Spiral</h4>"
    "<p>$5,000 credit card balance at 20% APR, paying only minimums: takes ~20 years to pay off, total paid: ~$12,000 (more than double the original debt).</p>",
    [("Early Investing Advantage","Starting to invest 10 years earlier with less total money can yield MORE than investing 3× more starting later, due to compound interest."),
     ("Debt Spiral","When minimum payments mostly cover interest, causing debt to take decades to pay off and cost multiples of the original amount."),
     ("Minimum Payment Trap","Making only minimum credit card payments extends debt repayment for decades and dramatically increases total cost."),
     ("Pay-Off Strategies","Debt avalanche (highest interest first) saves the most money; debt snowball (smallest balance first) provides psychological wins."),
     ("Compounding Frequency","The more frequently interest compounds (daily vs. monthly vs. annually), the more total interest accumulated.")],
    [("In the early vs. late investor case, the early investor wins despite investing LESS because:",["They had better investments","*Compound interest had more time to work — 10 extra years of compounding outweighs 20 extra years of contributions","They were luckier","They had a higher return rate"],"Time > amount."),
     ("A $5,000 credit card balance at 20% APR with minimum payments takes approximately _____ to pay off.",["2 years","5 years","10 years","*~20+ years"],"Minimum payment trap."),
     ("The total amount paid on that $5,000 credit card debt with minimums is approximately:",["$5,000","$7,500","*~$12,000+ (more than doubling the original debt)","$50,000"],"Interest costs."),
     ("The debt snowball method pays off:",["Highest interest first","*Smallest balance first (for psychological motivation from quick wins)","All debts equally","Randomly"],"Motivation-based."),
     ("The debt avalanche method pays off:",["Smallest balance first","*Highest interest rate first (mathematically optimal — saves the most in total interest)","All debts equally","Newest debt first"],"Math-optimal."),
     ("A person earning $60,000 who saves 15% ($9,000/year) at 8% return for 30 years accumulates approximately:",["$270,000","*~$1,000,000","$500,000","$2,000,000"],"Consistent saving builds wealth."),
     ("The key lesson from the early investor case study is:",["It doesn't matter when you start","*Start investing as early as possible — even small amounts benefit enormously from time and compound interest","Only large amounts matter","Waiting for higher income is better"],"Time is the most valuable asset."),
     ("Credit card debt is particularly dangerous because:",["Interest rates are low","*Interest rates are very high (15-25%+ APR), and interest compounds on unpaid balances including previous interest","Minimum payments pay it off fast","It's not real debt"],"High-interest compounding."),
     ("The '30-year mortgage vs. 15-year mortgage' case shows:",["No difference","*A 30-year mortgage has lower monthly payments but total interest paid is often DOUBLE that of a 15-year mortgage","15-year is always worse","Only monthly payment matters"],"Duration affects total cost."),
     ("A case study comparing renting vs. buying shows the decision depends on:",["Only monthly cost","*How long you stay (break-even typically 5-7 years), local prices, maintenance costs, opportunity cost of down payment, and tax benefits","Buying is always better","Renting is always better"],"Context-dependent."),
     ("Emergency fund case studies show that unexpected expenses occur:",["Rarely","*Frequently (car repair, medical bill, job loss) — most people face a significant unexpected expense at least annually","Only to some people","Never to prepared people"],"Expect the unexpected."),
     ("A case study of lottery winners shows that many end up bankrupt because:",["They were unlucky","*Financial literacy is more important than income — without money management skills, even large sums are quickly depleted","Lotteries are rigged","Taxes take everything"],"Skills > windfall."),
     ("Case studies of successful savers show common habits:",["Only high income","*Pay-yourself-first, live below means, avoid high-interest debt, invest consistently, and have a written plan","Only lucky investments","Only inheritance"],"Habits, not luck."),
     ("The 'millionaire next door' research found that most millionaires:",["Earn millions","Are flashy spenders","*Live modestly, save consistently, and avoid lifestyle inflation (most are first-generation wealthy)","Inherited wealth"],"Stealth wealth."),
     ("Case studies in financial math apply concepts to:",["Only theoretical scenarios","*Real-world situations that demonstrate how interest, time, decisions, and behavior affect financial outcomes","Only textbook problems","Only simple examples"],"Practical application."),
     ("The behavioral finance lesson from case studies is:",["Behavior doesn't matter","*Human psychology (fear, greed, instant gratification) often undermines financial success — awareness helps overcome these tendencies","Only math matters","Only income matters"],"Behavior > knowledge."),
     ("A case study comparing 8% returns vs. 10% returns over 40 years shows that:",["The difference is small","*Even 2% difference in returns multiplies into huge wealth differences over decades (over 2× difference at 40 years)","Returns don't matter","Only short-term matters"],"Small differences compound."),
     ("Insurance case studies illustrate that going without insurance:",["Saves money overall","*Is a gamble — one serious event (accident, illness, natural disaster) can cause financial devastation","Always works out","Only affects the unlucky"],"Risk management essential."),
     ("For financial math, case studies demonstrate that:",["Math is irrelevant to real life","*Formulas and concepts directly apply to real-world financial decisions with enormous long-term impact","Only professionals need this","Theory doesn't match practice"],"Math shapes real outcomes."),
     ("The most important takeaway from personal finance case studies is:",["Income determines everything","*Financial behavior and consistent good habits matter more than income level for building long-term wealth","Only one factor matters","Luck determines outcomes"],"Habits determine outcomes.")]
)
lessons[k]=v

# 1.8
k,v = build_lesson(1,8,"Financial Decision-Making Models",
    "<h3>Financial Decision-Making Models</h3>"
    "<h4>Rational Decision-Making Process</h4>"
    "<ul><li><b>Step 1:</b> Identify the decision (e.g., buy vs. lease a car).</li>"
    "<li><b>Step 2:</b> Gather information (costs, terms, alternatives).</li>"
    "<li><b>Step 3:</b> Identify alternatives and their opportunity costs.</li>"
    "<li><b>Step 4:</b> Evaluate using criteria (cost, risk, time, alignment with goals).</li>"
    "<li><b>Step 5:</b> Make and implement the decision.</li>"
    "<li><b>Step 6:</b> Review and learn from the outcome.</li></ul>",
    [("Rational Decision Model","Systematic approach: identify → gather info → list alternatives → evaluate → decide → review."),
     ("Behavioral Finance","Study of how psychological biases affect financial decisions (overconfidence, loss aversion, herd behavior)."),
     ("Loss Aversion","The tendency to feel losses more strongly than equivalent gains — losing $100 hurts more than gaining $100 feels good."),
     ("Anchoring Bias","Over-relying on the first piece of information encountered when making decisions (e.g., original price as anchor)."),
     ("Decision Matrix","Tool for comparing options by scoring each against weighted criteria to identify the best choice.")],
    [("The first step in rational financial decision-making is:",["Making a quick choice","*Clearly identifying the decision to be made","Gathering data","Asking friends"],"Define the problem."),
     ("Behavioral finance studies how _____ affects financial decisions.",["Only math","Only income","*Psychological biases and emotions","Only market conditions"],"Psychology of money."),
     ("Loss aversion means people:",["Love taking risks","*Feel losses about 2× more intensely than equivalent gains","Are always rational","Ignore losses"],"Asymmetric emotional response."),
     ("Anchoring bias in shopping occurs when:",["You compare carefully","*The original 'sale' price (often inflated) makes the discounted price seem like a great deal even if it's not","You always buy the cheapest","You ignore prices"],"Reference point manipulation."),
     ("A decision matrix helps by:",["Making decisions random","*Scoring alternatives against weighted criteria to systematically identify the best option","Only listing options","Only considering price"],"Structured evaluation."),
     ("The sunk cost fallacy affects decisions when people:",["Ignore past costs","*Continue investing in something because of what they've already spent, even when quitting would be better","Always make rational choices","Consider only future costs"],"Throwing good money after bad."),
     ("Herd behavior in finance means:",["Being a leader","*Following what others are doing (buying/selling) without independent analysis — amplifies market bubbles and crashes","Only professionals herd","It doesn't affect individuals"],"Following the crowd."),
     ("Confirmation bias causes investors to:",["Seek diverse opinions","*Only seek information that confirms their existing beliefs while ignoring contradictory evidence","Be more rational","Always diversify"],"Selective information processing."),
     ("Overconfidence bias leads to:",["Better returns","*Excessive trading, under-diversification, and underestimation of risk — overconfident investors often underperform","More careful decisions","Always positive outcomes"],"Too much confidence hurts."),
     ("Mental accounting (Thaler) is the tendency to:",["Combine all money rationally","*Treat money differently based on its source or intended use (e.g., treating a tax refund as 'found money' and spending it)","Only save earnings","Always invest windfalls"],"Money is fungible."),
     ("The 'FOMO' (Fear of Missing Out) effect in investing leads to:",["Careful research","*Buying into investments at high prices because 'everyone else is making money' — often near market peaks","Better returns","Disciplined investing"],"Emotional buying."),
     ("Delayed gratification research (marshmallow experiment) shows that people who delay:",["Are unhappy","*Tend to have better financial outcomes, higher earnings, and more wealth long-term","Don't enjoy life","Are always wealthy"],"Patience correlates with success."),
     ("A cooling-off period helps financial decisions by:",["Wasting time","*Allowing emotions to subside so rational evaluation can occur before major purchases or investments","Only for large purchases","Having no benefit"],"Time reduces impulse."),
     ("The 24-hour rule for purchases means:",["Buy everything immediately","*Wait 24 hours before making non-essential purchases to determine if you truly want/need the item","Only for online shopping","Only for expensive items"],"Impulse control strategy."),
     ("Framing effect means the same information presented differently:",["Has no impact","*Can lead to different decisions (e.g., '90% survival rate' vs. '10% death rate' — same data, different reactions)","Always leads to rational choices","Only affects uninformed people"],"Presentation affects choice."),
     ("Present bias causes people to:",["Plan well for the future","*Overvalue immediate rewards and undervalue future benefits (procrastinating on saving/investing)","Always choose long-term","Ignore the present"],"Now > later bias."),
     ("Status quo bias means:",["Always changing investments","*Preferring to do nothing or maintain current decisions even when change would be beneficial (e.g., staying in bad investments)","Only choosing new options","Maximizing returns"],"Inertia resistance."),
     ("Choice overload (paradox of choice) can cause:",["Better decisions","*Decision paralysis or worse choices when too many options are available (e.g., too many 401k fund options)","Always more satisfaction","Only one option preference"],"Too many choices."),
     ("Nudges (Thaler & Sunstein) improve financial decisions by:",["Eliminating choice","*Designing default options that guide people toward better outcomes without restricting freedom (e.g., auto-enrollment in 401k)","Only through punishment","Forcing specific choices"],"Choice architecture."),
     ("For financial math, understanding decision biases helps because:",["Math alone is sufficient","*Even people who know the math can make poor financial decisions due to psychological biases — awareness improves outcomes","Biases don't affect math","Only professionals need this"],"Knowledge + awareness.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 1: wrote {len(lessons)} lessons")
