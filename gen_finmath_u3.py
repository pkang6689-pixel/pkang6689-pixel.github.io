#!/usr/bin/env python3
"""Financial Math Unit 3 – Loans & Debt (8 lessons)."""
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

# 3.1
k,v = build_lesson(3,1,"Loan Terminology & Concepts",
    "<h3>Loan Fundamentals</h3>"
    "<ul><li><b>Principal:</b> Amount borrowed.</li>"
    "<li><b>Interest rate:</b> Cost of borrowing, expressed as APR (Annual Percentage Rate).</li>"
    "<li><b>Term:</b> Loan duration (e.g., 30-year mortgage, 5-year auto loan).</li>"
    "<li><b>Collateral:</b> Asset pledged to secure a loan (home for mortgage, car for auto).</li>"
    "<li><b>Secured vs. unsecured:</b> Secured has collateral (lower rate); unsecured does not (higher rate).</li></ul>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>APR:</b> Total annual cost of borrowing including fees.</li>"
    "<li><b>Down payment:</b> Upfront portion paid to reduce principal borrowed.</li>"
    "<li><b>Amortization:</b> Gradual repayment through scheduled payments.</li></ul>",
    [("Principal","The original amount of money borrowed in a loan."),
     ("APR (Annual Percentage Rate)","The true annual cost of a loan, including interest and fees — required by law for disclosure."),
     ("Collateral","An asset pledged to secure a loan; lender can seize it if you default (e.g., home, car)."),
     ("Secured Loan","A loan backed by collateral — typically lower interest rates because the lender has less risk."),
     ("Amortization","The process of paying off a loan through regular scheduled payments over time (principal + interest).")],
    [("The principal of a loan is:",["The interest owed","*The original amount borrowed","The monthly payment","The total cost"],"Amount borrowed."),
     ("APR includes:",["Only interest","*Interest rate PLUS fees and other costs, expressed as an annual percentage","Only fees","Only the monthly payment"],"Total borrowing cost."),
     ("A secured loan requires:",["Good credit only","*Collateral (an asset the lender can seize if you default)","No application","A co-signer always"],"Collateral requirement."),
     ("Unsecured loans typically have _____ interest rates than secured loans.",["Lower","The same","*Higher (more risk to lender since there's no collateral)","No"],"Risk-based pricing."),
     ("Examples of secured loans include:",["Credit cards","Personal lines of credit","*Mortgages (house), auto loans (car)","Payday loans"],"Collateral-backed."),
     ("A down payment on a $200,000 home of 20% equals:",["$20,000","$10,000","*$40,000","$60,000"],"200000 × 0.20."),
     ("A larger down payment results in:",["Higher monthly payments","*Lower monthly payments and less total interest paid (smaller principal to finance)","No change","Higher interest rate"],"Less to borrow."),
     ("Amortization means:",["Paying all at once","*Gradually paying off a loan through regular scheduled payments that include both principal and interest","Never paying off the loan","Only paying interest"],"Gradual repayment."),
     ("The term of a loan refers to:",["The interest rate","*The length of time to repay the loan (e.g., 15-year or 30-year mortgage)","The monthly payment amount","The down payment"],"Loan duration."),
     ("Shorter loan terms mean:",["Lower monthly payments","*Higher monthly payments but less total interest paid over the life of the loan","More interest overall","The same total cost"],"Trade-off: payment vs. total cost."),
     ("PMI (Private Mortgage Insurance) is required when:",["You put 30% down","*You put less than 20% down on a conventional mortgage (protects the lender)","You have perfect credit","You pay cash"],"<20% down."),
     ("The debt-to-income ratio (DTI) measures:",["How much you earn","*Your total monthly debt payments divided by your gross monthly income (lenders use this for approval)","How much you spend","Your credit score"],"Affordability metric."),
     ("A co-signer on a loan:",["Earns interest","*Agrees to repay if the primary borrower defaults (shares legal responsibility)","Has no responsibility","Reduces the principal"],"Shared liability."),
     ("Default on a loan means:",["Paying early","*Failing to make required payments — triggers penalties, credit damage, and potential seizure of collateral","Making extra payments","Refinancing"],"Failure to pay."),
     ("Fixed-rate loans have:",["Rates that change","*An interest rate that stays the same for the entire loan term","Variable monthly payments","No interest"],"Constant rate."),
     ("Variable-rate loans (ARMs) have:",["Fixed rates","*Rates that can change based on market conditions (often start lower, may increase)","No rates","Always lower total cost"],"Rate can change."),
     ("Origination fees are:",["Monthly charges","*One-time fees charged by the lender to process a new loan (part of closing costs)","Interest charges","Late fees"],"Upfront loan cost."),
     ("Prepayment penalties mean:",["You earn extra","*The lender charges a fee if you pay off the loan early (check before signing!)","You save money","Payments are late"],"Early payoff fee."),
     ("Grace period on a loan is:",["Extra interest time","*A period after the due date where no late fee is charged (but interest may still accrue)","Free money period","No payment required"],"Payment buffer."),
     ("Understanding loan terminology is crucial because:",["It's just vocabulary","*It helps you compare options, understand true costs, and avoid predatory lending practices","Only for bankers","Only for tests"],"Informed borrowing.")]
)
lessons[k]=v

# 3.2
k,v = build_lesson(3,2,"Amortization Schedules",
    "<h3>Amortization Schedules</h3>"
    "<p>An amortization schedule shows the breakdown of each payment into <b>principal</b> and <b>interest</b>.</p>"
    "<h4>Monthly Payment Formula</h4>"
    "<p><b>PMT = P × r(1+r)^n / [(1+r)^n − 1]</b></p>"
    "<ul><li><b>P</b> = loan principal</li>"
    "<li><b>r</b> = monthly rate (annual rate ÷ 12)</li>"
    "<li><b>n</b> = total number of monthly payments</li></ul>"
    "<p>Early payments are mostly interest; later payments are mostly principal.</p>",
    [("Amortization Schedule","Table showing each payment's split between principal reduction and interest expense over the life of a loan."),
     ("Monthly Payment Formula","PMT = P × r(1+r)^n / [(1+r)^n − 1] where r = monthly rate and n = total payments."),
     ("Front-Loaded Interest","Early loan payments go mostly toward interest; principal reduction accelerates in later payments."),
     ("Extra Principal Payments","Additional payments applied to principal reduce total interest and shorten the loan term significantly."),
     ("Remaining Balance","After each payment, the outstanding principal = previous balance − principal portion of that payment.")],
    [("The loan payment formula PMT = P × r(1+r)^n / [(1+r)^n − 1] gives:",["Total interest","*The fixed monthly payment amount that amortizes the loan over n periods","The principal only","The down payment"],"Monthly payment calculation."),
     ("For a $200,000 mortgage at 6% for 30 years, the monthly rate r is:",["6%","0.6%","*0.5% (6%/12 = 0.005)","0.06%"],"Annual → monthly."),
     ("The total number of payments (n) for a 30-year mortgage is:",["30","120","*360","300"],"30 × 12."),
     ("$200,000 at 6% for 30 years has a monthly payment of approximately:",["$1,000","*$1,199.10","$1,500","$2,000"],"Standard mortgage payment."),
     ("In early mortgage payments, the majority goes toward:",["Principal","*Interest (early payments are interest-heavy because the balance is largest)","Taxes","Insurance"],"Front-loaded interest."),
     ("On a $200,000 loan at 6%, the first month's interest is:",["$100","$500","*$1,000 (200000 × 0.005)","$1,200"],"Balance × monthly rate."),
     ("If the monthly payment is $1,199.10 and first month's interest is $1,000, the principal paid is:",["$1,199.10","$1,000","*$199.10","$0"],"Payment − interest."),
     ("Over 30 years, total payments on $200,000 at 6% equal:",["$200,000","$300,000","*$431,676 (1199.10 × 360)","$500,000"],"Total cost of mortgage."),
     ("Total interest paid on this 30-year mortgage is approximately:",["$100,000","*$231,676 (431,676 − 200,000 — more interest than principal!)","$50,000","$200,000"],"Interest exceeds principal."),
     ("Extra $100/month toward principal on this mortgage saves approximately:",["$5,000","$20,000","*~$45,000 in interest and ~5 years off the term","$100,000"],"Extra payments impact."),
     ("An amortization schedule is useful because it shows:",["Only the monthly payment","*How each payment splits between principal and interest and the declining balance over time","Only the total cost","Only the interest"],"Detailed breakdown."),
     ("Halfway through a 30-year mortgage at 6%, you've paid off approximately _____ of the principal.",["50%","*~30% (due to front-loaded interest structure, principal paydown is slow early on)","75%","10%"],"Non-linear paydown."),
     ("Biweekly payments (26 half-payments per year) effectively make _____ monthly payments per year.",["12","*13 (26 ÷ 2 = 13 — one extra payment per year)","14","11"],"Extra payment strategy."),
     ("A 15-year mortgage vs. 30-year at the same rate has:",["Lower payments","*Higher payments but MUCH less total interest (often less than half the interest cost)","The same total cost","No advantage"],"Shorter = cheaper total."),
     ("$200,000 at 6% for 15 years: monthly payment ≈ $1,688. Total interest ≈:",["$200,000","$100,000","*~$103,788 (vs. $231,676 for 30-year — saving ~$128,000!)","$150,000"],"15-year savings."),
     ("Refinancing makes sense when:",["Rates go up","*Rates drop significantly AND you plan to stay long enough to recoup closing costs","You just got the loan","Never"],"Lower rate opportunity."),
     ("In the formula, the monthly rate r for 4.5% annual is:",["4.5%","0.45%","0.045","*0.00375 (4.5%/12)"],"Rate division."),
     ("Negative amortization occurs when:",["You pay extra","*Payments don't cover the interest, so the balance actually grows (dangerous loan feature)","You pay on time","You refinance"],"Balance increases."),
     ("Spreadsheets can generate amortization schedules using:",["Only FV()","*PPMT() for principal and IPMT() for interest portions of each payment","Only graphs","Only manual entry"],"Excel functions."),
     ("Understanding amortization is essential because it reveals:",["Only one number","*The TRUE cost of borrowing over time and why extra payments are so powerful early in a loan","Only the payment","Only the rate"],"Hidden cost awareness.")]
)
lessons[k]=v

# 3.3
k,v = build_lesson(3,3,"Mortgage Calculations",
    "<h3>Mortgage Calculations</h3>"
    "<h4>Key Numbers</h4>"
    "<ul><li><b>Home price − down payment = loan amount</b></li>"
    "<li><b>Total monthly cost = PITI</b> (Principal + Interest + Taxes + Insurance)</li>"
    "<li><b>Affordability rule:</b> Housing should be ≤ 28% of gross monthly income.</li></ul>"
    "<h4>Example</h4>"
    "<p>Home: $350,000. Down: $70,000 (20%). Loan: $280,000 at 6.5% for 30 years.</p>"
    "<p>Monthly P&amp;I: ~$1,770. Taxes: ~$365. Insurance: ~$150. Total PITI: ~$2,285.</p>",
    [("PITI","Total monthly mortgage cost: Principal + Interest + Taxes + Insurance."),
     ("28% Rule","Housing costs should not exceed 28% of gross monthly income for affordability."),
     ("Closing Costs","One-time fees at purchase: typically 2–5% of loan amount (appraisal, title, origination, etc.)."),
     ("Escrow Account","Account held by lender to pay property taxes and insurance from your monthly payment."),
     ("Points (Discount Points)","Upfront fees paid to reduce the interest rate; 1 point = 1% of the loan amount.")],
    [("If a home costs $350,000 and the down payment is 20%, the loan amount is:",["$350,000","$300,000","*$280,000","$250,000"],"350000 × 0.80."),
     ("PITI stands for:",["Principal, Income, Tax, Investment","*Principal, Interest, Taxes, Insurance","Payment, Interest, Term, Income","Principal, Interest, Term, Income"],"Total monthly housing cost."),
     ("The 28% rule says housing costs should not exceed _____ of gross monthly income.",["20%","*28%","33%","40%"],"Affordability guideline."),
     ("With $8,000 gross monthly income, maximum PITI under the 28% rule is:",["$1,600","$2,000","*$2,240","$2,800"],"8000 × 0.28."),
     ("Closing costs on a $300,000 home at 3% equal:",["$3,000","$6,000","*$9,000","$15,000"],"300000 × 0.03."),
     ("One discount point on a $280,000 mortgage costs:",["$280","$1,400","*$2,800","$28,000"],"1% of loan amount."),
     ("Paying points is worthwhile when:",["You plan to sell quickly","*You plan to stay long enough to recoup the upfront cost through lower monthly payments","You have bad credit","Always"],"Break-even analysis."),
     ("$280,000 at 6.5% for 30 years has a monthly P&I of approximately:",["$1,500","*~$1,770","$2,000","$2,500"],"Mortgage payment."),
     ("Total interest on $280,000 at 6.5% for 30 years is approximately:",["$200,000","$280,000","*~$357,200 (total payments ~$637,200 − $280,000)","$500,000"],"More interest than principal."),
     ("Property taxes vary by location but average roughly _____ of home value annually.",["0.1%","0.5%","*1–2%","5%"],"Tax variation."),
     ("Annual property tax on a $350,000 home at 1.25% is approximately:",["$2,500","$3,500","*$4,375","$5,000"],"350000 × 0.0125."),
     ("Homeowner's insurance covers:",["Only fire","*Damage to the property, liability, and personal belongings (varies by policy and exclusions)","Only flooding","Only theft"],"Property protection."),
     ("An escrow account is used to:",["Earn you interest","*Collect a portion of each monthly payment for taxes and insurance, paid by the lender on your behalf","Store your down payment","Pay closing costs"],"Managed payments."),
     ("A 15-year mortgage at 5.8% vs. 30-year at 6.5% on $280,000:",["30-year costs less total","*15-year saves over $200,000 in interest despite higher monthly payments","They cost the same","15-year payment is the same"],"Dramatic savings."),
     ("ARM (Adjustable Rate Mortgage) initial rates are typically:",["Higher than fixed","*Lower than fixed-rate initially, but can increase after the introductory period","The same","Always better"],"Teaser rate."),
     ("A 5/1 ARM means:",["5% rate for 1 year","*Fixed rate for 5 years, then adjusts annually based on market conditions","5 payments, 1 year","Pay 5, skip 1"],"ARM structure."),
     ("The total cost of homeownership includes:",["Only mortgage","*Mortgage + taxes + insurance + maintenance + repairs + HOA fees + utilities","Only PITI","Only the purchase price"],"Full ownership cost."),
     ("Pre-approval for a mortgage:",["Guarantees a loan","*Shows sellers you're a serious buyer and gives you a price range based on your financial profile","Is the same as pre-qualification","Costs nothing"],"Buying preparation."),
     ("Refinancing from 6.5% to 5% on $280,000 (remaining 25 years) saves approximately:",["$100/month","*~$270/month (from ~$1,770 to ~$1,500) = ~$81,000 over remaining term","$50/month","$500/month"],"Refinance savings."),
     ("For financial math, mortgage calculations combine:",["Only one formula","*Compound interest, amortization, budgeting, tax considerations, and opportunity cost analysis","Only simple interest","Only algebra"],"Multi-concept application.")]
)
lessons[k]=v

# 3.4
k,v = build_lesson(3,4,"Credit Card Mathematics",
    "<h3>Credit Card Mathematics</h3>"
    "<h4>Key Features</h4>"
    "<ul><li><b>APR:</b> Typical credit card APR ranges from 15–25%.</li>"
    "<li><b>Daily rate:</b> APR ÷ 365 (used for daily balance calculations).</li>"
    "<li><b>Minimum payment:</b> Often 1–3% of balance or $25 (whichever is greater).</li>"
    "<li><b>Grace period:</b> ~25 days to pay in full before interest accrues on purchases.</li></ul>"
    "<p>Example: $5,000 balance at 20% APR with minimum payments only → takes ~25 years and costs ~$8,400 in interest!</p>",
    [("Credit Card APR","Annual Percentage Rate on a credit card, typically 15–25%; applied daily to the outstanding balance."),
     ("Minimum Payment Trap","Paying only the minimum extends repayment to decades and costs many times the original purchase."),
     ("Grace Period","~25 days after the billing cycle ends where no interest accrues if you pay in full each month."),
     ("Balance Transfer","Moving debt from one card to another (often at a promotional 0% rate) to save on interest."),
     ("Credit Utilization","The percentage of your available credit that you're using; keeping it < 30% helps your credit score.")],
    [("Typical credit card APR ranges from:",["1–5%","5–10%","*15–25%","50–75%"],"High-interest debt."),
     ("The daily periodic rate for a 20% APR card is approximately:",["0.2%","2%","*0.0548% (20%/365)","0.02%"],"Daily rate."),
     ("A $5,000 balance at 20% APR with minimum payments only costs approximately _____ in total interest.",["$2,000","$5,000","*~$8,400","$1,000"],"Minimum payment catastrophe."),
     ("Paying only minimums on $5,000 at 20% APR takes approximately _____ to repay.",["5 years","10 years","*~25 years","2 years"],"Decades of debt."),
     ("The grace period on credit cards:",["Always applies","*Only applies if you pay the FULL statement balance each month (carry a balance = no grace period)","Never applies","Applies to cash advances"],"Crucial distinction."),
     ("Paying the full statement balance each month means you pay _____ in interest.",["Some interest","The minimum","*$0 (the grace period protects you — this is using credit cards optimally)","Late fees"],"Zero interest strategy."),
     ("A $3,000 purchase at 22% APR paid over 3 years with $100/month payments costs approximately _____ in interest.",["$300","$600","*~$1,080 (total paid ~$4,080)","$3,000"],"Significant cost."),
     ("Cash advances on credit cards:",["Have a grace period","*Have NO grace period AND typically a higher interest rate + upfront fee (avoid these!)","Are free","Have lower rates"],"Worst card feature."),
     ("Credit utilization should ideally be kept below:",["50%","75%","*30% (of total available credit — lower is better for credit score)","100%"],"Credit score factor."),
     ("A balance transfer to a 0% APR card for 18 months saves money IF:",["You transfer and forget about it","*You pay off the balance before the promotional period ends (otherwise the rate jumps to full APR)","You make minimum payments","You use the old card more"],"Strategic use."),
     ("The Credit CARD Act of 2009 requires:",["Free credit","*Clear disclosure of how long minimum payments take to repay and what paying more would save (on statements)","No interest charges","Free transfers"],"Consumer protection."),
     ("If your credit card statement shows: 'Minimum payment: 25 years to pay off' you should:",["Ignore it","*Pay significantly more than the minimum or develop a payoff plan — this is a warning sign","Make the minimum","Get another card"],"Heed the warning."),
     ("$10,000 in credit card debt at 22% vs. $10,000 mortgage at 6%: the credit card costs:",["The same amount","*Roughly 3.7× more in annual interest ($2,200 vs. $600 — cards are most expensive debt)","Less","Slightly more"],"Worst debt type."),
     ("The avalanche method of debt payoff:",["Pays smallest debt first","*Pays highest interest rate debt first while making minimums on others — saves the most money","Ignores all debt","Pays all equally"],"Mathematically optimal."),
     ("The snowball method of debt payoff:",["Pays highest rate first","*Pays smallest balance first for psychological wins — motivates continued progress","Ignores small debts","Pays all equally"],"Behavioral approach."),
     ("A $500 impulse purchase on a 20% card paid over 2 years actually costs:",["$500","*~$611 (over $111 in interest — a 22% surcharge on the purchase)","$520","$450"],"True cost of credit."),
     ("Introductory 0% APR offers are designed to:",["Give free money","*Attract customers — after the intro period (12-21 months), rates jump to standard high APR","Lower credit scores","Help everyone"],"Marketing strategy."),
     ("Rewards cards (cashback, points) are only beneficial if:",["You carry a balance","*You ALWAYS pay the full balance — otherwise interest charges far exceed any rewards earned","You spend more to earn more","You have many cards"],"Rewards vs. interest."),
     ("The best mathematical strategy for credit cards is:",["Pay minimum","Carry a balance for credit history","*Pay the full statement balance every month — use the grace period, earn rewards, pay $0 interest","Only use cash"],"Optimal usage."),
     ("Credit card math is important because:",["Cards are simple","*High APRs and minimum payment traps can turn small purchases into years of debt — understanding the math protects you","Everyone carries balances","It's required by law"],"Financial protection.")]
)
lessons[k]=v

# 3.5
k,v = build_lesson(3,5,"Student Loan Analysis",
    "<h3>Student Loan Analysis</h3>"
    "<h4>Types</h4>"
    "<ul><li><b>Federal subsidized:</b> Government pays interest while in school.</li>"
    "<li><b>Federal unsubsidized:</b> Interest accrues while in school.</li>"
    "<li><b>Private loans:</b> From banks/lenders; usually higher rates, fewer protections.</li></ul>"
    "<h4>Repayment Plans</h4>"
    "<ul><li><b>Standard (10-year):</b> Fixed payments, least total interest.</li>"
    "<li><b>Income-driven:</b> Payments based on income (IBR, PAYE, REPAYE).</li>"
    "<li><b>Extended (25-year):</b> Lower payments but more total interest.</li></ul>",
    [("Subsidized Loan","Federal student loan where the government pays interest while you're in school at least half-time."),
     ("Unsubsidized Loan","Federal student loan where interest accrues from disbursement — even while in school."),
     ("Capitalization","Unpaid interest that is added to the principal balance, increasing the amount on which future interest is calculated."),
     ("Income-Driven Repayment","Plans that cap monthly payments at a percentage (10-20%) of discretionary income."),
     ("Loan Forgiveness","Programs that cancel remaining student loan balance after meeting certain conditions (e.g., PSLF after 10 years of public service).")],
    [("Federal subsidized student loans:",["Charge interest while in school","*Have the government pay interest while you're enrolled at least half-time","Have higher rates","Are from private banks"],"Government benefit."),
     ("Interest capitalization on student loans means:",["Interest is forgiven","*Unpaid interest is added to the principal, increasing the balance you owe and future interest charges","Interest decreases","Principal is reduced"],"Compound growth of debt."),
     ("$30,000 in unsubsidized loans at 5% accruing for 4 years in school capitalizes to approximately:",["$30,000","*~$36,465 (30000 × 1.05^4)","$32,000","$40,000"],"Interest during school."),
     ("Standard repayment on $30,000 at 5% for 10 years: monthly payment ≈:",["$200","*~$318","$500","$150"],"Standard plan."),
     ("Total payments on $30,000 at 5% over 10 years (standard) ≈:",["$30,000","$33,000","*~$38,184 (318 × 120)","$45,000"],"Total cost."),
     ("Extended repayment (25 years) on $30,000 at 5%: monthly ≈ $175. Total ≈:",["$40,000","$45,000","*~$52,689 (175 × 300) — $14,500 more than standard!","$60,000"],"Lower payment = more total."),
     ("Income-driven repayment caps payments at:",["50% of income","*10–20% of discretionary income (income above 150% of poverty line)","5% of income","A fixed amount"],"Percentage of discretion."),
     ("PSLF (Public Service Loan Forgiveness) forgives remaining balance after:",["5 years","*10 years (120 qualifying payments while working full-time for a qualifying public service employer)","15 years","20 years"],"Public service benefit."),
     ("Private student loans compared to federal loans typically have:",["Better protections","*Higher interest rates, fewer repayment options, and fewer consumer protections","Lower rates always","Income-driven plans"],"Federal is usually preferred."),
     ("$50,000 in student loans at 6% on standard 10-year plan: monthly ≈ $555, total interest ≈:",["$5,000","*~$16,613","$25,000","$50,000"],"Substantial interest."),
     ("Paying $100/month extra on $50,000 at 6%:",["Makes no difference","*Saves ~$5,500 in interest and pays off ~2 years early","Costs more overall","Only saves $100"],"Extra payment power."),
     ("Refinancing student loans from 6% to 4% on $50,000 saves approximately:",["$500 total","*~$6,000+ over the life of the loan","Nothing","$100/month"],"Refinancing savings."),
     ("The break-even analysis for student loans considers:",["Only loan cost","*Expected salary increase from education vs. total cost of education (loan + opportunity cost)","Only graduation rate","Only interest rate"],"Investment analysis."),
     ("If a degree increases salary by $20,000/year and loans cost $50,000 total, the payback period is approximately:",["5 years","*~2.5 years (not accounting for taxes — the degree 'paid for itself')","10 years","Never"],"ROI of education."),
     ("Student loan interest may be tax-deductible up to:",["$5,000","*$2,500 per year (subject to income limits)","$1,000","$10,000"],"Tax benefit."),
     ("Deferment and forbearance:",["Eliminate loans","*Temporarily pause or reduce payments — but interest often still accrues, increasing total cost","Forgive debt","Lower the rate"],"Temporary relief."),
     ("The debt-to-income ratio after graduation is important because:",["It's just a number","*It affects ability to qualify for mortgages, car loans, and other credit — high student debt can limit future opportunities","It doesn't matter","Only employers check it"],"Future financial impact."),
     ("For financial math, student loans demonstrate:",["Only simple interest","*Amortization, capitalization, present value of education, and the long-term cost of borrowing decisions","Only one formula","Nothing important"],"Multi-concept lesson."),
     ("The most cost-effective repayment strategy (mathematically) is:",["Minimum payments for 25 years","*Standard or accelerated payments — pay as much as possible as soon as possible to minimize interest","Income-driven always","Only make payments when convenient"],"Minimize total interest."),
     ("Average student loan debt for a bachelor's degree graduate (2024) is approximately:",["$10,000","$20,000","*~$30,000–$35,000","$100,000"],"Current reality.")]
)
lessons[k]=v

# 3.6
k,v = build_lesson(3,6,"Real Estate & Auto Loan Math",
    "<h3>Real Estate &amp; Auto Loan Math</h3>"
    "<h4>Auto Loans</h4>"
    "<ul><li>Typical terms: 36, 48, 60, or 72 months.</li>"
    "<li>New car: ~5–7% APR; Used car: ~7–10% APR (2024).</li>"
    "<li>Cars depreciate ~20% in year 1, ~60% over 5 years.</li></ul>"
    "<h4>Real Estate Investment</h4>"
    "<ul><li>Rental income − expenses = cash flow</li>"
    "<li>Cap rate = Net Operating Income / Property Value</li>"
    "<li>ROI considers appreciation, cash flow, tax benefits, and equity building.</li></ul>",
    [("Auto Loan Term","Duration of car financing; longer terms = lower payments but more interest + risk of being underwater."),
     ("Underwater (Upside Down)","Owing more on a loan than the asset is worth — common with long auto loans due to rapid depreciation."),
     ("Cap Rate","Capitalization Rate = Net Operating Income / Property Value; measures investment property return."),
     ("Cash Flow (Real Estate)","Rental income minus all expenses (mortgage, taxes, insurance, maintenance, vacancy)."),
     ("Equity","The portion of the property you own: market value − remaining mortgage balance.")],
    [("A $30,000 car at 6% for 60 months has a monthly payment of approximately:",["$400","$500","*~$580","$700"],"Auto payment calculation."),
     ("Total interest on $30,000 at 6% for 60 months is approximately:",["$2,000","*~$4,800 (580 × 60 = $34,800 − $30,000)","$6,000","$10,000"],"Auto loan total interest."),
     ("A car depreciates ~20% in its first year, so a $30,000 car is worth approximately _____ after year 1.",["$28,000","$27,000","*$24,000","$20,000"],"First-year depreciation."),
     ("Being 'underwater' on a car loan means:",["The car was in a flood","*You owe more on the loan than the car is currently worth","You paid cash","Your payment is late"],"Negative equity."),
     ("A 72-month auto loan vs. a 48-month loan:",["Costs less overall","*Has lower monthly payments but much more total interest AND higher risk of going underwater","Is always better","Is the same total cost"],"Longer = riskier."),
     ("$30,000 car at 6% for 72 months: total interest ≈ $5,800 vs. 48 months: ≈ $3,800. Difference:",["$500","*~$2,000 more for the longer loan","No difference","$5,000"],"Time cost comparison."),
     ("The 20/4/10 rule for car buying says:",["Buy any car you want","*20% down, no more than 4-year loan, total car costs ≤ 10% of gross income","20% APR is acceptable","Buy every 4 years"],"Affordability guideline."),
     ("A rental property purchased for $200,000 with $25,000 annual rent and $15,000 expenses has a cap rate of:",["12.5%","*5% (NOI = $10,000; $10,000/$200,000)","10%","7.5%"],"Return metric."),
     ("Cash-on-cash return considers:",["Total property value","*Your actual cash invested (down payment + closing costs) vs. annual cash flow — not the total property value","Only appreciation","Only rental income"],"Investor's return."),
     ("$40,000 down on a $200,000 property generating $4,000/year cash flow = _____ cash-on-cash return.",["2%","5%","*10% ($4,000/$40,000)","20%"],"Return on investment."),
     ("Leverage in real estate means:",["Paying cash","*Using borrowed money (mortgage) to control a larger asset — amplifies both gains AND losses","Selling quickly","Avoiding debt"],"Magnified returns."),
     ("A $200,000 property appreciating 3%/year is worth _____ after 10 years.",["$230,000","$250,000","*~$268,783 (200000 × 1.03^10)","$300,000"],"Property appreciation."),
     ("The 1% rule for rental properties says monthly rent should be at least:",["0.5% of purchase price","*1% of purchase price ($200,000 property = $2,000/month rent)","2% of purchase price","5% of purchase price"],"Quick screening."),
     ("Vacancy rate of 10% on $2,000/month rent means effective income is:",["$2,000","*$1,800/month ($2,000 × 0.90)","$1,600","$2,200"],"Realistic income."),
     ("Total return on real estate includes:",["Only cash flow","Only appreciation","*Cash flow + appreciation + equity buildup + tax benefits (depreciation deduction)","Only purchase price"],"Multi-factor return."),
     ("Leasing vs. buying a car: leasing typically means:",["You own it","*Lower monthly payments but you don't build equity and have mileage restrictions; buying costs more monthly but you own the asset","Free car","Same as buying"],"Ownership vs. access."),
     ("Gap insurance covers:",["Routine maintenance","*The difference between what you owe on a loan and the car's actual cash value if totaled (important when underwater)","Parking tickets","Oil changes"],"Underwater protection."),
     ("For a real estate investment to be worthwhile, it generally should:",["Just cover the mortgage","*Generate positive cash flow after ALL expenses and provide a return above what you'd earn in other investments","Always appreciate","Be in a major city"],"Investment threshold."),
     ("The tax benefit of mortgage interest deduction means:",["Free interest","*You can deduct mortgage interest from taxable income, effectively reducing the net cost of homeownership","No taxes on the home","Free mortgage"],"Tax advantage."),
     ("Auto and real estate math combines concepts of:",["Only one formula","*Compound interest, depreciation, amortization, cash flow analysis, ROI, and tax considerations","Only simple interest","Only budgeting"],"Comprehensive application.")]
)
lessons[k]=v

# 3.7
k,v = build_lesson(3,7,"Case Studies in Debt Management",
    "<h3>Case Studies in Debt Management</h3>"
    "<h4>Case 1: Debt Avalanche</h4>"
    "<p>Maria has 3 debts: Credit card ($5,000 at 22%), Student loan ($20,000 at 6%), Car loan ($15,000 at 5%). Extra $300/month. Avalanche: Pay minimums on all; put extra toward 22% card first. Saves the most interest.</p>"
    "<h4>Case 2: Debt Consolidation</h4>"
    "<p>James consolidates $25,000 in credit card debt at 20% average into a personal loan at 10%. Monthly savings: ~$200. Total savings: ~$8,000.</p>",
    [("Debt Avalanche","Pay off highest-interest debt first while making minimum payments on others — mathematically optimal strategy."),
     ("Debt Snowball","Pay off smallest balance first for psychological wins; mathematically costs more but motivates many people."),
     ("Debt Consolidation","Combining multiple debts into a single loan at a lower interest rate to simplify and reduce cost."),
     ("Debt-to-Income Ratio","Total monthly debt payments ÷ gross monthly income; lenders use this to assess borrowing capacity."),
     ("Financial Recovery Plan","Structured approach to eliminating debt: assess all debts, choose a strategy, automate payments, build emergency fund.")],
    [("The debt avalanche method prioritizes paying off:",["Smallest balance first","*Highest interest rate first","Oldest debt first","Newest debt first"],"Mathematically optimal."),
     ("Maria's three debts total _____ in principal.",["$30,000","$35,000","*$40,000 (5000+20000+15000)","$45,000"],"Total debt."),
     ("Maria should pay extra toward _____ first using the avalanche method.",["Student loan (6%)","Car loan (5%)","*Credit card (22%) — the highest interest rate","All equally"],"Target highest rate."),
     ("The debt snowball method prioritizes:",["Highest rate","*Smallest balance first (psychological wins through quick eliminations motivate continued effort)","Largest balance","Oldest debt"],"Behavioral approach."),
     ("Consolidating $25,000 from 20% to 10% saves approximately _____ per year in interest.",["$500","$1,000","*~$2,500 (25000 × 0.10 = $2,500 less)","$5,000"],"Rate reduction savings."),
     ("Debt consolidation is only effective if:",["You always consolidate","*You don't accumulate new debt on the now-empty credit cards — otherwise you're in worse shape","You pay minimums","You close the loan early"],"Behavioral discipline."),
     ("A DTI ratio above _____ is considered risky by most lenders.",["20%","30%","*43% (Qualified Mortgage threshold — many prefer < 36%)","50%"],"Lender threshold."),
     ("Balance transfer cards with 0% intro APR for 18 months are useful if:",["You make minimum payments","*You can pay off the entire balance before the promo ends — otherwise the rate jumps to 20%+","You transfer and forget","You keep spending"],"Strategic use."),
     ("For Maria, the credit card minimum is ~$125, student loan $222, car $283. Total minimums =",["$500","*$630","$700","$800"],"Total minimum payments."),
     ("With $300 extra + $125 minimum on the card, Maria pays _____ per month on the 22% card.",["$125","$300","*$425","$630"],"Accelerated payoff."),
     ("At $425/month on $5,000 at 22%, the card is paid off in approximately:",["24 months","*~14 months","6 months","36 months"],"Faster than minimum."),
     ("After the card is paid off, Maria redirects the $425 to her _____ next.",["Savings","Car (5%)","*Car loan (5%) — next highest after card, or student loan (6%) if using strict avalanche","Shopping"],"No — strict avalanche targets 6% student loan next."),
     ("The psychological benefit of the snowball method is:",["Saving money","*Quick wins from eliminating small debts first, which builds momentum and motivation","Higher returns","Lower rates"],"Motivation factor."),
     ("Which costs less in total interest: avalanche or snowball?",["Snowball","*Avalanche (targeting highest rates first minimizes total interest — the math always favors avalanche)","They're equal","Depends on balance"],"Math vs. behavior."),
     ("Chapter 7 bankruptcy:",["Is always better","*Discharges most unsecured debt but has severe consequences (credit impact for 10 years, loss of some assets)","Has no consequences","Only for businesses"],"Last resort."),
     ("A debt management plan (DMP) through a nonprofit credit counselor:",["Is a scam","*Negotiates lower rates and consolidates payments; takes 3-5 years; less damaging than bankruptcy","Is free always","Eliminates all debt instantly"],"Professional help."),
     ("The total cost of carrying $10,000 in credit card debt at 20% for 10 years (minimum payments) is approximately:",["$12,000","$15,000","*~$20,000+ (you may pay more in interest than the original balance)","$10,500"],"Decade of debt."),
     ("Creating an emergency fund while paying off debt is important because:",["It slows debt payoff","*Without one, unexpected expenses go on credit cards, creating new debt and a vicious cycle","It's not important","Only wealthy people need one"],"Break the cycle."),
     ("Lifestyle inflation (spending more as income rises) contributes to debt because:",["It doesn't","*Increased income goes to upgraded expenses rather than debt payoff or savings, keeping you in the same position","It only affects wealthy people","It helps the economy"],"Behavioral trap."),
     ("The key lesson from debt management case studies is:",["Debt is unavoidable","*A structured mathematical approach — assessing all debts, choosing a strategy, and consistently executing — is essential for financial health","Only avoid debt completely","Declare bankruptcy"],"Disciplined approach.")]
)
lessons[k]=v

# 3.8
k,v = build_lesson(3,8,"Loan Comparison & Decision-Making",
    "<h3>Loan Comparison &amp; Decision-Making</h3>"
    "<h4>Comparing Loan Offers</h4>"
    "<ul><li><b>Compare total cost:</b> Not just monthly payment — calculate total payments over life of loan.</li>"
    "<li><b>APR vs. interest rate:</b> APR includes fees; same interest rate can have different APRs.</li>"
    "<li><b>Opportunity cost:</b> Could the money earn more invested than the interest saved?</li></ul>"
    "<h4>Decision Framework</h4>"
    "<p>1. Calculate total cost of each option. 2. Consider flexibility and risks. 3. Account for opportunity costs. 4. Choose based on complete analysis.</p>",
    [("Total Cost of a Loan","Sum of all payments − principal = total interest; the true measure of borrowing cost."),
     ("APR Comparison","Compare loans by APR (not just interest rate) because APR includes fees for a more complete picture."),
     ("Opportunity Cost of Prepaymnt","If loan rate < potential investment return, extra money may be better invested than used for extra payments."),
     ("Loan-to-Value Ratio (LTV)","Loan amount ÷ property value; lower LTV = less risk = better terms from lenders."),
     ("Break-Even Analysis","Calculate how long it takes for savings from a financial decision (e.g., refinancing) to exceed the costs.")],
    [("The most important metric when comparing loans is:",["Monthly payment","*Total cost (total payments over the life of the loan — not just the monthly payment)","Interest rate only","Loan term only"],"Total cost matters."),
     ("Two loans: A) $200K at 6% for 30 years; B) $200K at 5.75% with $6,000 in fees. The better deal:",["Always A","Always B","*Requires calculating total cost of each (fees add to B but lower rate saves over time)","They're identical"],"Full cost comparison."),
     ("Refinancing costs $4,000 and saves $150/month. Break-even point:",["1 year","*~27 months ($4,000 ÷ $150/month) — worth it if you stay longer than ~2.25 years","5 years","Never"],"Break-even calculation."),
     ("If your mortgage rate is 4% and investments return 8%, extra money is mathematically better:",["Paying the mortgage","*Investing (8% return > 4% loan cost, though this assumes consistent returns and ignores risk)","In a savings account","Under the mattress"],"Opportunity cost."),
     ("However, paying off a 4% mortgage gives a _____ return vs. uncertain 8% investment return.",["0% return","*Guaranteed 4% (risk-free — the emotional value of being debt-free also matters)","8% return","Negative return"],"Guaranteed vs. uncertain."),
     ("A 0% auto loan vs. $3,000 cash discount on $30,000: the better choice depends on:",["Always take 0%","Always take discount","*What rate you'd get otherwise and what you can earn on the $3,000 if investing it","They're equal"],"NPV comparison."),
     ("Loan A: 36 months at 3%, payment $291, total $10,476. Loan B: 60 months at 5%, payment $189, total $11,340. Best:",["Loan B (lower payment)","*Loan A (less total cost — saves $864 despite higher payment)","They cost the same","Neither"],"Total cost wins."),
     ("The Loan Estimate form (required by law) shows:",["Only the interest rate","*APR, monthly payment, closing costs, total interest, and other key terms for comparison","Only the payment","Only the term"],"Consumer protection."),
     ("When comparing adjustable vs. fixed-rate mortgages, consider:",["Only the initial rate","*The worst-case scenario (how high could the ARM go?), how long you'll own the home, and rate environment","Only the current market","Only the lender's recommendation"],"Risk analysis."),
     ("Paying 'points' (each = 1% of loan) to lower the rate makes sense if:",["Always","Never","*You stay long enough to recoup the upfront cost through lower monthly payments (calculate the break-even)","Only for large loans"],"Break-even analysis."),
     ("$10,000 personal loan: Bank A offers 8% for 3 years; Bank B offers 7% for 5 years. Total interest:",["A is always more","*A: ~$1,280 (total ~$11,280); B: ~$1,880 (total ~$11,880) — A costs less despite higher rate","B is less","They're equal"],"Term impacts total cost."),
     ("Federal student loans vs. private for the same amount:",["Private is always better","*Federal usually offers better protections (income-driven plans, forgiveness, forbearance) even if rates are similar","They're identical","Federal is always cheaper"],"Protections matter."),
     ("When choosing between investing extra money vs. paying down debt, a key consideration is:",["Only the rates","*Tax implications (mortgage interest deduction, tax-advantaged investment accounts), risk tolerance, and behavioral factors","Only the monthly budget","It doesn't matter"],"Holistic analysis."),
     ("Biweekly mortgage payments vs. monthly: making 26 half-payments = 13 full payments/year saves:",["Nothing","*Thousands in interest over the life of the loan AND several years off the term","Only a few dollars","The same amount"],"Simple acceleration."),
     ("HELOC (Home Equity Line of Credit) is typically:",["A fixed loan","*A revolving credit line secured by your home — variable rate, interest-only option, tax-deductible interest (with limits)","An unsecured loan","A credit card"],"Home-secured credit."),
     ("Consolidation loan at 10% for $25,000 cards at 22% average: annual interest savings ≈:",["$500","*$3,000 ($5,500 → $2,500 annual interest)","$1,000","No savings"],"Rate reduction."),
     ("The cognitive bias of 'payment anchoring' means people:",["Always choose wisely","*Focus on monthly payment instead of total cost — a lower payment can cost far more over a longer term","Ignore all loans","Only care about rates"],"Behavioral finance."),
     ("A comprehensive loan decision should consider:",["Only the payment","*Total cost, APR, term flexibility, prepayment options, fees, opportunity cost, and personal financial situation","Only the lender","Only the rate"],"Multi-factor analysis."),
     ("Good-faith estimate replaced by Loan Estimate and Closing Disclosure under _____ regulations.",["No regulations","*TRID (TILA-RESPA Integrated Disclosure) rules — designed to help consumers compare offers","State-only rules","Bank-only rules"],"Regulatory protection."),
     ("For financial math, loan comparison requires:",["Only one formula","*Combining amortization, present/future value, break-even analysis, and opportunity cost into comprehensive decision-making","Only simple addition","Only rates"],"Integrated analysis.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 3: wrote {len(lessons)} lessons")
