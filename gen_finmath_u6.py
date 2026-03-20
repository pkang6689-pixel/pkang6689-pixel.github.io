#!/usr/bin/env python3
"""Financial Math Unit 6 – Taxes & Insurance (8 lessons)."""
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

# 6.1
k,v = build_lesson(6,1,"Understanding Income Tax",
    "<h3>Income Tax Fundamentals</h3>"
    "<h4>How Income Tax Works</h4>"
    "<ul><li><b>Gross income:</b> All taxable income (wages, interest, dividends, etc.).</li>"
    "<li><b>Adjusted Gross Income (AGI):</b> Gross income minus above-the-line deductions.</li>"
    "<li><b>Taxable income:</b> AGI minus standard/itemized deductions and exemptions.</li>"
    "<li><b>Tax owed:</b> Calculated by applying tax brackets to taxable income.</li></ul>"
    "<p>The US uses a <b>progressive</b> tax system — higher income is taxed at higher rates.</p>",
    [("Progressive Tax","System where higher income portions are taxed at higher rates; everyone pays the same rate on the same levels."),
     ("Gross Income","All taxable income before deductions: wages, salaries, interest, dividends, business income."),
     ("AGI (Adjusted Gross Income)","Gross income minus specific above-the-line deductions (student loan interest, IRA contributions, etc.)."),
     ("Standard Deduction","A fixed amount subtracted from AGI before calculating tax ($14,600 single / $29,200 married filing jointly, 2024)."),
     ("Taxable Income","The amount actually subject to tax: AGI minus deductions (standard or itemized).")],
    [("The US federal income tax system is:",["Flat","Regressive","*Progressive (higher portions of income taxed at increasingly higher rates)","Optional"],"Tax structure."),
     ("In a progressive system, moving to a higher tax bracket means:",["ALL your income is taxed at the higher rate","*Only the income ABOVE the bracket threshold is taxed at the higher rate","You pay less","No change"],"Marginal rate."),
     ("With $80,000 taxable income (2024 single), the tax is calculated by:",["$80,000 × 22%","*Applying 10% to first $11,600, 12% to next $35,550, and 22% to the remainder — layered brackets","$80,000 × 12%","$80,000 × 10%"],"Bracket application."),
     ("The standard deduction for a single filer in 2024 is approximately:",["$6,000","$10,000","*$14,600","$20,000"],"Current standard deduction."),
     ("Taxable income = AGI minus:",["All expenses","Gross income","*Standard deduction (or itemized deductions, whichever is larger)","Nothing"],"Deduction step."),
     ("A person earning $50,000 with $14,600 standard deduction has taxable income of:",["$50,000","*$35,400","$14,600","$64,600"],"50000 − 14600."),
     ("Marginal tax rate vs. effective tax rate: marginal is _____, effective is _____.",["Lower, higher","*The rate on the LAST dollar earned, the AVERAGE rate on ALL income","The same thing","Higher, lower"],"Two different rates."),
     ("Someone in the '22% bracket' probably pays an effective rate of:",["22%","25%","*Less than 22% (because lower brackets tax the first portions of income at 10% and 12%)","30%"],"Effective < marginal."),
     ("W-2 employees have taxes withheld from:",["Annual tax return","Bank accounts","*Each paycheck by their employer (estimated tax payments throughout the year)","Only at year-end"],"Withholding."),
     ("Self-employed workers must pay:",["No taxes","Only income tax","*Income tax PLUS self-employment tax (15.3% for Social Security/Medicare — both employee and employer portions)","Only state tax"],"SE tax burden."),
     ("FICA taxes include:",["Only income tax","*Social Security (6.2%) and Medicare (1.45%) = 7.65% from employee, matched by employer","Only state tax","Only federal tax"],"Payroll taxes."),
     ("A W-4 form determines:",["Your tax return","*How much federal tax your employer withholds from each paycheck","Your tax rate","Your refund amount"],"Withholding form."),
     ("Filing status options include:",["Only single","*Single, Married Filing Jointly, Married Filing Separately, Head of Household, Qualifying Widow(er)","Only married","Only one option"],"Multiple statuses."),
     ("Married Filing Jointly typically results in _____ tax than filing separately.",["Higher","*Lower (wider brackets and higher standard deduction benefit most couples)","The same","Double"],"MFJ advantage."),
     ("Tax-exempt income includes:",["Wages","Dividends","*Municipal bond interest, Roth IRA qualified withdrawals, gifts (under annual exclusion)","All investment income"],"Not all income is taxed."),
     ("The tax filing deadline is typically:",["January 1","*April 15 (can be extended with Form 4868, but taxes owed are still due April 15)","December 31","June 1"],"Annual deadline."),
     ("Penalties for underpaying estimated taxes apply to:",["W-2 employees only","*Self-employed and others who owe more than $1,000 at filing and didn't pay enough quarterly","No one","Only corporations"],"Estimated tax requirement."),
     ("State income taxes:",["Don't exist","Are the same everywhere","*Vary dramatically — from 0% (TX, FL, WA, etc.) to over 13% (California, at highest bracket)","Are always 5%"],"State variation."),
     ("Understanding tax brackets helps you:",["Avoid all taxes","*Plan income timing, maximize deductions, and make informed decisions about retirement contributions and investments","Only file returns","Only compute refunds"],"Strategic planning."),
     ("For financial math, income tax calculations apply:",["No math","*Percentage calculations, progressive bracket math, and deduction analysis to one of life's largest expenses","Only addition","Only multiplication"],"Tax as math.")]
)
lessons[k]=v

# 6.2
k,v = build_lesson(6,2,"Tax Brackets & Marginal Rates",
    "<h3>Tax Brackets &amp; Marginal Rates</h3>"
    "<h4>2024 Federal Tax Brackets (Single)</h4>"
    "<ul><li>10%: $0 – $11,600</li>"
    "<li>12%: $11,601 – $47,150</li>"
    "<li>22%: $47,151 – $100,525</li>"
    "<li>24%: $100,526 – $191,950</li>"
    "<li>32%: $191,951 – $243,725</li>"
    "<li>35%: $243,726 – $609,350</li>"
    "<li>37%: Over $609,350</li></ul>",
    [("Tax Bracket","A range of income taxed at a specific rate in the progressive system."),
     ("Marginal Tax Rate","The tax rate applied to the LAST dollar of income — the rate of the highest bracket you reach."),
     ("Effective Tax Rate","Total tax paid ÷ total income — the average rate actually paid across all brackets."),
     ("Tax Liability","The total amount of federal (and state) income tax you owe for the year."),
     ("Bracket Creep","When inflation pushes income into higher brackets; brackets are adjusted annually for inflation to offset this.")],
    [("On $50,000 taxable income (single, 2024), the first $11,600 is taxed at:",["22%","12%","*10%","0%"],"First bracket."),
     ("Tax on the first $11,600 = ",["$2,320","*$1,160 (11600 × 0.10)","$580","$0"],"First bracket tax."),
     ("Income from $11,601 to $47,150 is taxed at _____ in the second bracket.",["10%","*12%","22%","24%"],"Second bracket rate."),
     ("Tax on income from $11,601 to $47,150 ($35,550) =",["$3,555","*$4,266 (35550 × 0.12)","$7,110","$5,333"],"Second bracket tax."),
     ("On $50,000 taxable, the amount in the 22% bracket is:",["$50,000","$47,150","*$2,850 ($50,000 − $47,150)","$11,600"],"Third bracket portion."),
     ("Tax on the 22% bracket portion ($2,850) =",["$285","*$627 (2850 × 0.22)","$570","$855"],"Third bracket tax."),
     ("Total federal tax on $50,000 taxable income ≈",["$11,000","$5,000","*~$6,053 ($1,160 + $4,266 + $627)","$8,000"],"Total computed."),
     ("Effective tax rate on $50,000 taxable income ≈",["22%","15%","*~12.1% ($6,053 ÷ $50,000)","10%"],"Average rate."),
     ("The marginal rate for someone with $50,000 taxable income is:",["10%","12%","*22% (the bracket of the last dollar earned)","24%"],"Highest bracket."),
     ("A common misconception: 'If I earn $1 more and enter a higher bracket, I lose money.' This is:",["True","*False — only the income ABOVE the bracket threshold is taxed at the higher rate; you always net more","Sometimes true","Depends"],"Bracket myth busted."),
     ("On $100,000 taxable income (single), total tax ≈",["$22,000","$15,000","*~$17,400 (10% + 12% + 22% brackets)","$10,000"],"$100K tax."),
     ("Effective rate on $100,000 taxable ≈",["22%","20%","*~17.4%","15%"],"Effective rate."),
     ("On $200,000 taxable income, the marginal rate is:",["22%","24%","*32%","35%"],"Higher income bracket."),
     ("Capital gains (long-term, held >1 year) are taxed at _____ rates than ordinary income.",["Higher","The same","*Lower (0%, 15%, or 20% depending on income — preferential treatment for long-term investments)","10% flat"],"Investment tax advantage."),
     ("Qualified dividends are taxed at:",["Ordinary rates","50%","*Long-term capital gains rates (0%, 15%, or 20% — lower than ordinary income rates)","0% always"],"Dividend tax treatment."),
     ("Tax planning strategies include:",["Earning less to avoid taxes","*Maximizing deductions, contributing to retirement accounts, timing income, and harvesting losses","Only itemizing","Never investing"],"Legal tax minimization."),
     ("Contributing $5,000 to a traditional IRA in the 22% bracket saves _____ in taxes.",["$500","$750","*$1,100 (5000 × 0.22)","$5,000"],"Deduction value."),
     ("The alternative minimum tax (AMT) ensures:",["Everyone pays the same","*High-income taxpayers with many deductions pay at least a minimum amount of tax","No one pays tax","Low earners pay more"],"Minimum tax floor."),
     ("Tax bracket calculations in financial math require:",["Only multiplication","*Multi-step progressive calculation: applying different rates to different portions of income","Only one rate","Only subtraction"],"Layered math."),
     ("Understanding brackets helps with:",["Nothing practical","*Deciding between Traditional vs. Roth contributions, timing bonuses, and making investment decisions","Only filing taxes","Only accountants"],"Strategic decisions.")]
)
lessons[k]=v

# 6.3
k,v = build_lesson(6,3,"Property, Sales, & Other Taxes",
    "<h3>Property, Sales, &amp; Other Taxes</h3>"
    "<h4>Property Tax</h4>"
    "<p>Based on assessed value of property. Rate varies by location (0.3% to 2.5%+).</p>"
    "<h4>Sales Tax</h4>"
    "<p>Percentage added to purchases. Varies by state (0% to 7.25%+) plus local additions.</p>"
    "<h4>Other Taxes</h4>"
    "<ul><li><b>Estate/Inheritance tax:</b> On transfers at death (federal exemption: $13.6M in 2024).</li>"
    "<li><b>Excise tax:</b> On specific goods (gas, alcohol, tobacco).</li>"
    "<li><b>Payroll tax:</b> FICA (Social Security + Medicare).</li></ul>",
    [("Property Tax","Annual tax on real estate based on assessed value; funds local services (schools, fire, police, roads)."),
     ("Assessed Value","The value assigned to a property by the tax assessor for property tax calculation (may differ from market value)."),
     ("Sales Tax","Tax added to retail purchases at point of sale; varies by state and locality."),
     ("Estate Tax","Federal tax on the transfer of assets at death; applies only above the exemption ($13.6M in 2024)."),
     ("Excise Tax","Tax on specific goods: gasoline (~$0.18/gallon federal + state), alcohol, tobacco, luxury items.")],
    [("Property tax is calculated as:",["Market value × income","*Assessed value × tax rate (e.g., $300,000 assessed × 1.5% = $4,500/year)","Purchase price × 10%","Fixed amount per house"],"Assessment × rate."),
     ("A home assessed at $250,000 with a 1.8% property tax rate owes:",["$2,500","$3,600","*$4,500 (250000 × 0.018)","$5,000"],"Property tax calculation."),
     ("Property taxes primarily fund:",["Federal government","State government","*Local services: schools, fire departments, police, roads, and infrastructure","Military"],"Local funding."),
     ("States with NO state income tax include:",["California, New York","*Texas, Florida, Washington, Nevada, Wyoming, among others","All states","No states"],"Tax-free states."),
     ("States with no income tax often have ____ as compensation.",["Lower sales/property taxes","*Higher sales or property taxes (states need revenue from somewhere)","No taxes at all","Higher income"],"Revenue balance."),
     ("A $100 purchase with 8.5% sales tax costs:",["$100","$108","*$108.50","$185"],"100 × 1.085."),
     ("Annual sales tax paid by an average household spending $50,000 with 7% sales tax rate (on taxable goods ≈ 60%) is:",["$3,500","$5,000","*~$2,100 (50000 × 0.60 × 0.07 — not all purchases are taxable)","$1,000"],"Estimated sales tax."),
     ("The federal estate tax exemption in 2024 is approximately:",["$1 million","$5 million","*$13.6 million ($27.2 million for married couples)","$100,000"],"Very high threshold."),
     ("Excise tax on gasoline is approximately _____ per gallon federally.",["$0.01","*$0.184 (plus state taxes averaging ~$0.30+)","$1.00","$0.50"],"Gas tax."),
     ("FICA payroll tax total (employee share) is:",["5%","10%","*7.65% (6.2% Social Security + 1.45% Medicare)","15.3%"],"Employee payroll tax."),
     ("Self-employed people pay _____ in FICA because they pay both employee and employer portions.",["7.65%","10%","*15.3%","20%"],"Double FICA."),
     ("The Social Security tax wage base in 2024 is approximately:",["$100,000","*$168,600 (income above this is NOT subject to Social Security tax; Medicare has no cap)","$250,000","No limit"],"SS wage cap."),
     ("Capital gains tax rates (long-term) are:",["The same as income tax","Higher than income tax","*0%, 15%, or 20% depending on income (lower than ordinary income rates)","50%"],"Preferential rates."),
     ("Tax-loss harvesting saves money by:",["Creating losses","*Using investment losses to offset gains, reducing the capital gains tax owed","Avoiding all taxes","Only working for businesses"],"Tax strategy."),
     ("Property tax protests/appeals can reduce taxes if:",["Never","*The assessed value is higher than fair market value (homeowners can challenge assessments)","The rate changes","You disagree with all taxes"],"Challenge assessments."),
     ("Homestead exemption reduces property tax by:",["Eliminating it","*Reducing the taxable assessed value for owner-occupied primary residences (varies by state)","Increasing the rate","Only for farmers"],"Homeowner benefit."),
     ("Gift tax exemption (2024) allows giving _____ per person per year tax-free.",["$1,000","$10,000","*$18,000","$100,000"],"Annual exclusion."),
     ("The total tax burden (income + payroll + sales + property) for a middle-income family is often:",["10%","20%","*30-40%+ of gross income (when ALL types of taxes are combined)","50%"],"Total tax picture."),
     ("Tax incidence refers to:",["Who writes the check","*Who actually bears the economic burden of a tax (e.g., who 'pays' for higher gas taxes — producers or consumers?)","Who benefits from taxes","Who sets tax rates"],"Economic burden."),
     ("For financial math, understanding various taxes helps calculate:",["Nothing","*True cost of purchases, real estate ownership costs, investment returns, and overall financial planning accuracy","Only one type of tax","Only income"],"Comprehensive tax awareness.")]
)
lessons[k]=v

# 6.4
k,v = build_lesson(6,4,"Types of Insurance",
    "<h3>Types of Insurance</h3>"
    "<h4>Core Insurance Types</h4>"
    "<ul><li><b>Health insurance:</b> Covers medical expenses (deductible, copay, coinsurance, out-of-pocket max).</li>"
    "<li><b>Auto insurance:</b> Liability, collision, comprehensive.</li>"
    "<li><b>Homeowner's/Renter's:</b> Property damage, liability, personal belongings.</li>"
    "<li><b>Life insurance:</b> Term (pure protection) vs. Whole (protection + cash value).</li>"
    "<li><b>Disability insurance:</b> Replaces income if you can't work.</li></ul>",
    [("Premium","The regular payment (monthly/annually) you make to maintain insurance coverage."),
     ("Deductible","The amount you pay out-of-pocket before insurance begins covering costs."),
     ("Copay","A fixed amount you pay for a covered service (e.g., $30 doctor visit, $10 prescription)."),
     ("Term Life Insurance","Pure death benefit for a specific term (10-30 years); no cash value; most affordable protection."),
     ("Disability Insurance","Replaces 60-70% of income if you're unable to work due to illness or injury — often the most overlooked coverage.")],
    [("An insurance premium is:",["The amount of coverage","The deductible","*The regular payment you make to keep your insurance policy active","The copay"],"Cost of coverage."),
     ("A deductible is:",["The monthly payment","*The amount you pay out-of-pocket before insurance starts covering costs","The maximum coverage","The copay amount"],"Initial cost-sharing."),
     ("Higher deductible plans typically have:",["Higher premiums","*Lower premiums (you accept more risk in exchange for lower regular payments)","The same premiums","No coverage"],"Premium-deductible tradeoff."),
     ("Health insurance coinsurance of 80/20 means:",["You pay 80%","*Insurance pays 80%, you pay 20% of covered costs (after deductible)","You pay 20% of premium","Insurance pays 100%"],"Cost-sharing ratio."),
     ("The out-of-pocket maximum is:",["The premium","The deductible","*The most you'll pay in a year for covered services — after reaching this, insurance pays 100%","The copay total"],"Financial protection cap."),
     ("Auto liability insurance covers:",["Your car's damage","*Damage you cause to OTHER people and their property in an accident","Your injuries only","Car theft"],"Others' damages."),
     ("Collision coverage pays for:",["Other driver's car","*Your car's repair after an accident (regardless of fault)","Only stolen cars","Only medical bills"],"Your car + accident."),
     ("Comprehensive auto coverage pays for:",["Only collisions","*Non-collision damage: theft, weather, vandalism, animal collisions, falling objects","Only liability","Only medical"],"Non-crash damage."),
     ("Term life insurance provides:",["Investment + insurance","Lifetime coverage","*Pure death benefit for a specific time period (10-30 years) — most affordable type","Cash value"],"Pure protection."),
     ("Whole life insurance differs from term because it:",["Is cheaper","*Has a cash value component that grows over time PLUS a death benefit; costs 5-15× more than term","Has a limited term","Doesn't pay claims"],"Cash value + premium cost."),
     ("Most financial advisors recommend _____ life insurance for typical families.",["Whole life","Universal life","*Term (much cheaper; invest the premium difference for better returns)","Variable life"],"Term + invest the difference."),
     ("The recommended amount of life insurance is typically:",["$100,000","*10–12× annual income (enough to replace income for the family if the earner dies)","Equal to the mortgage","$1 million for everyone"],"Income replacement."),
     ("Renter's insurance covers:",["The building","*Your personal belongings, liability, and additional living expenses if your rental is uninhabitable","The landlord's property","Nothing for renters"],"Renter protection."),
     ("Renter's insurance costs approximately:",["$500/month","*$15-30/month (very affordable and highly recommended)","$100/month","$200/month"],"Low cost."),
     ("Disability insurance is critical because:",["Disability is rare","*You're more likely to become disabled than die during working years; it protects your greatest asset: your income","Only for dangerous jobs","It's mandatory"],"Income protection."),
     ("Long-term disability insurance typically replaces _____ of income.",["100%","*60-70%","30%","90%"],"Partial income replacement."),
     ("An umbrella insurance policy provides:",["Weather protection","*Extra liability coverage beyond what auto and homeowner's policies cover (e.g., $1-5 million additional)","Only auto coverage","Only home coverage"],"Extended liability."),
     ("Insurance is based on the concept of:",["Gambling","*Risk pooling (many people pay premiums; the few who have claims are covered — spreading risk across the group)","Guaranteed profit","Investing"],"Risk pooling."),
     ("The most important purpose of insurance is:",["Making money","Building wealth","*Protecting against catastrophic financial loss that you couldn't afford to pay on your own","Everyday expenses"],"Catastrophic protection."),
     ("For financial math, insurance involves:",["No calculations","*Premium comparison, deductible/premium tradeoff analysis, coverage needs calculations, and expected value","Only premium payment","Only one number"],"Risk math.")]
)
lessons[k]=v

# 6.5
k,v = build_lesson(6,5,"Risk Management Basics",
    "<h3>Risk Management</h3>"
    "<h4>Risk Management Strategies</h4>"
    "<ul><li><b>Avoid:</b> Don't do the risky activity (don't own a pool).</li>"
    "<li><b>Reduce:</b> Take precautions (smoke detectors, safe driving).</li>"
    "<li><b>Transfer:</b> Insurance shifts financial risk to the insurer.</li>"
    "<li><b>Retain:</b> Accept the risk and self-insure (high deductible, emergency fund).</li></ul>"
    "<h4>Expected Value</h4>"
    "<p>E(X) = Probability × Impact. Used to evaluate whether insurance is worthwhile.</p>",
    [("Risk Avoidance","Eliminating a risk entirely by not engaging in the activity (don't own a boat = no boat liability)."),
     ("Risk Reduction","Taking steps to decrease the probability or impact of a risk (security system, healthy habits)."),
     ("Risk Transfer","Shifting financial risk to another party, typically through insurance (pay premium → insurer absorbs loss)."),
     ("Risk Retention","Accepting a risk and self-insuring — viable for small, manageable risks (choosing a high deductible)."),
     ("Expected Value","Probability of an event × its financial impact; used to decide whether to insure against a risk.")],
    [("The four risk management strategies are:",["Buy, sell, hold, trade","*Avoid, reduce, transfer, retain","Save, spend, invest, donate","Ignore, accept, insure, pray"],"Core strategies."),
     ("Insurance is an example of risk:",["Avoidance","Reduction","*Transfer (you pay a premium; the insurer assumes the financial risk)","Retention"],"Risk transfer."),
     ("Self-insuring (high deductible + emergency fund) is an example of risk:",["Avoidance","Transfer","*Retention (you accept the risk and would pay smaller losses yourself)","Reduction"],"Self-insurance."),
     ("Expected value of a risk: 2% chance of $50,000 loss per year =",["$50,000","$2,000","*$1,000/year expected loss (0.02 × $50,000)","$500"],"EV calculation."),
     ("If insurance against a $50,000 loss (2% probability) costs $1,200/year:",["It's a terrible deal","*The premium ($1,200) exceeds expected value ($1,000) — but it provides certainty and prevents catastrophe","It's free money","Expected value is irrelevant"],"Premium vs. EV."),
     ("People buy insurance even when premium > expected value because:",["They don't understand math","*Catastrophic losses would be devastating — the peace of mind and protection from financial ruin is worth the 'overpayment'","Insurance is always profitable","They're required to"],"Behavioral rationale."),
     ("You should insure against risks that are:",["Low probability, low impact","*Low probability but HIGH impact (where a loss would devastate your finances)","High probability, low impact","Common daily expenses"],"Insure the catastrophic."),
     ("You should self-insure (retain) risks that are:",["Catastrophic","All risks","*Low impact (losses you can absorb from savings/emergency fund without hardship)","Extremely rare"],"Retain the manageable."),
     ("A smoke detector is an example of risk:",["Avoidance","Transfer","*Reduction (decreases the probability/severity of fire damage)","Retention"],"Mitigation."),
     ("Wearing a seatbelt is risk _____ for car accident injuries.",["Transfer","Avoidance","*Reduction","Retention"],"Reduce severity."),
     ("Not owning a motorcycle is risk _____ for motorcycle accidents.",["Reduction","Transfer","*Avoidance (eliminating the risk entirely)","Retention"],"Complete elimination."),
     ("An emergency fund serves as self-insurance for:",["Only job loss","*Small to medium unexpected expenses that would otherwise go on credit cards (car repair, appliance replacement)","Nothing","Only medical bills"],"Financial buffer."),
     ("The purpose of deductibles in insurance is:",["To profit the company","*To share risk — the insured retains small losses (deductible) while the insurer covers large losses","To discourage claims","To increase premiums"],"Risk sharing."),
     ("Higher deductibles make sense for people with:",["No savings","*Healthy emergency funds who can afford to pay smaller losses out-of-pocket for lower premiums","Low income","No assets"],"Self-insurance capacity."),
     ("Diversification in investing is a form of risk:",["Transfer","Avoidance","*Reduction (spreading across many investments reduces the impact of any single loss)","Retention"],"Investment risk reduction."),
     ("A business liability umbrella policy is risk _____ for lawsuit damages.",["Reduction","Avoidance","*Transfer (the insurance company bears the financial risk of a large lawsuit)","Retention"],"Business protection."),
     ("Risk management order of preference (general):",["Buy insurance for everything","*First avoid unnecessary risks, then reduce remaining risks, transfer catastrophic ones, retain manageable ones","Ignore all risks","Only buy insurance"],"Hierarchy."),
     ("Cost-benefit analysis of insurance: $2,400/year for coverage vs. $500,000 potential liability:",["Not worth it","*Worth it — the potential loss far exceeds the premium; this is catastrophic risk you can't self-insure","Break even","Depends on luck"],"Rational decision."),
     ("The law of large numbers in insurance means:",["Companies lose money","*With many policyholders, actual losses approach expected losses (predictable for the insurer, making the business model work)","Everyone files claims","Premiums always decrease"],"Insurance math."),
     ("For financial math, risk management uses:",["No math","*Expected value, probability, cost-benefit analysis, and present value to make rational decisions about protecting assets","Only insurance terms","Only intuition"],"Quantitative decisions.")]
)
lessons[k]=v

# 6.6
k,v = build_lesson(6,6,"Tax Planning Case Studies",
    "<h3>Tax Planning Case Studies</h3>"
    "<h4>Case 1: Traditional vs. Roth IRA</h4>"
    "<p>Alex (22% bracket): $6,500 Traditional IRA deduction saves $1,430 in taxes NOW. In retirement (12% bracket), withdrawals are taxed less — Traditional wins. But if Alex expects HIGHER bracket in retirement, Roth wins.</p>"
    "<h4>Case 2: Tax-Loss Harvesting</h4>"
    "<p>Beth has $10,000 gains and $4,000 losses. Net taxable gain = $6,000. At 15% capital gains rate, she saves $600 in taxes by harvesting the loss.</p>",
    [("Traditional vs. Roth Decision","If current tax rate > retirement rate: Traditional IRA wins. If current rate < retirement rate: Roth wins."),
     ("Tax-Loss Harvesting","Selling investments at a loss to offset gains, reducing taxes. Net loss up to $3,000 can offset ordinary income."),
     ("Tax-Deferred Growth","Investments in Traditional IRA/401(k) grow without annual taxes; taxes owed on withdrawal (vs. taxable accounts)."),
     ("Capital Gain Offset","Using realized losses to reduce or eliminate taxes on realized gains in the same year."),
     ("Marginal Benefit of Deductions","The tax savings from a deduction = deduction amount × marginal tax rate (e.g., $5,000 deduction at 22% saves $1,100).")],
    [("A $6,500 Traditional IRA contribution in the 22% bracket saves _____ in current-year taxes.",["$650","$1,000","*$1,430 (6500 × 0.22)","$2,000"],"Deduction value."),
     ("If Alex expects to be in the 12% bracket in retirement, Traditional IRA saves _____ per $6,500 vs. Roth.",["$0","*$650 (1430 − 6500×0.12=780; net savings = $650 per contribution)","$1,430","$780"],"Bracket comparison."),
     ("A Roth IRA is better when you expect _____ tax rates in retirement.",["Lower","Same","*Higher (pay lower taxes now; avoid higher taxes on withdrawals later)","It never matters"],"Roth advantage scenario."),
     ("Beth's $10,000 gain offset by $4,000 loss results in net taxable gain of:",["$10,000","*$6,000","$4,000","$14,000"],"Loss offsets gain."),
     ("Beth saves _____ in taxes from harvesting the $4,000 loss at 15% capital gains rate.",["$150","$300","*$600 (4000 × 0.15)","$1,500"],"Tax savings."),
     ("Net capital losses above gains can offset ordinary income up to _____ per year.",["$1,000","*$3,000 ($3,000 limit; remainder carries forward to future years)","$5,000","Unlimited"],"Loss deduction limit."),
     ("$10,000 in a traditional 401(k) at 22% bracket saves _____ in current taxes.",["$1,000","$1,500","*$2,200 (10000 × 0.22)","$3,000"],"401(k) tax benefit."),
     ("Tax-deferred growth means the investment:",["Pays no tax ever","*Grows without annual taxes on dividends/gains — all money stays invested and compounds (taxes due at withdrawal)","Is taxed annually","Loses value"],"Growth advantage."),
     ("$100,000 growing at 7% for 20 years: taxable (losing 1% to annual taxes) vs. tax-deferred:",["Same outcome","*Tax-deferred: ~$387K vs. Taxable: ~$320K — tax deferral adds ~$67K through more efficient compounding","Taxable is better","Only $5K difference"],"Deferral power."),
     ("Bunching deductions means:",["Always itemizing","*Combining multiple years of deductions into one year to exceed the standard deduction threshold, then taking standard the other year","Spreading deductions evenly","Avoiding deductions"],"Strategic timing."),
     ("Charitable giving in a high-income year saves more because:",["Charities get more","*Higher marginal rate means each dollar donated saves more in taxes (32% bracket: $1,000 donation saves $320 vs. 12% saves $120)","Lower rates apply","It doesn't matter"],"Bracket optimization."),
     ("Health Savings Account (HSA) is 'triple tax-advantaged' because:",["Three people save","*Contributions are pre-tax, growth is tax-free, AND qualified withdrawals are tax-free","You get three deductions","Three accounts needed"],"Best tax vehicle."),
     ("If both spouses work and one earns much more, _____ filing status usually provides the least tax.",["Both filing separately","Single","*Married Filing Jointly (wider brackets and higher standard deduction reduce combined tax)","Head of Household"],"MFJ benefit."),
     ("Timing a year-end bonus: deferring $10,000 to January moves income to a potentially:",["Higher bracket","*Lower bracket year (if income varies), saving taxes on that $10,000","Same bracket","It doesn't affect taxes"],"Income timing."),
     ("Municipal bond interest is _____ from federal income tax.",["Fully taxed","*Exempt (and often state tax-exempt if the bond is from your state — valuable for high-bracket investors)","Partially exempt","Taxed at 50%"],"Muni bond advantage."),
     ("A Roth conversion ($50,000 from Traditional to Roth in the 22% bracket) costs:",["$0","$5,000","*$11,000 in current taxes (50000 × 0.22) — but future growth and withdrawals are then tax-free forever","$50,000"],"Conversion cost."),
     ("Roth conversions are best done in:",["High-income years","*Low-income years (when your marginal rate is low, the conversion tax is minimized)","Any year equally","Only at retirement"],"Low-bracket opportunity."),
     ("For a business owner, choosing between S-corp and sole proprietorship affects:",["Nothing","*Self-employment tax liability — S-corp can save thousands in FICA on reasonable salary/distribution split","Only state taxes","Only income taxes"],"Entity selection."),
     ("The wash-sale rule prevents you from:",["Selling stocks","*Claiming a loss if you buy the same or 'substantially identical' stock within 30 days (before or after the sale)","Buying stocks","Trading any securities"],"Loss deduction rule."),
     ("Tax planning case studies show that tax optimization:",["Is tax evasion","*Is legal and prudent use of tax code provisions — potentially saving thousands per year through informed decisions","Only benefits the wealthy","Is too complex"],"Legal optimization.")]
)
lessons[k]=v

# 6.7
k,v = build_lesson(6,7,"Insurance in Real Life",
    "<h3>Insurance in Real Life</h3>"
    "<h4>Case 1: Health Insurance Plan Comparison</h4>"
    "<p>Plan A: Premium $300/month, $1,000 deductible, 80/20 coinsurance, $5,000 max OOP.<br>"
    "Plan B: Premium $200/month, $3,000 deductible, 70/30 coinsurance, $8,000 max OOP.<br>"
    "For healthy year: Plan B saves $1,200. For major illness: Plan A saves up to $3,000.</p>"
    "<h4>Case 2: Life Insurance Needs</h4>"
    "<p>Couple with $80K income, $200K mortgage, 2 young kids. Need: ~$800K-1M coverage (10-12× income).</p>",
    [("Plan Comparison","Analyzing total costs across scenarios (healthy year vs. major illness) for different insurance options."),
     ("HSA-Eligible Plan","High-deductible health plan (HDHP) that qualifies for a Health Savings Account — triple tax advantage."),
     ("Needs Analysis (Life Insurance)","Calculating coverage amount based on income replacement, debts, education costs, and final expenses."),
     ("Claims Process","Steps to file and receive insurance benefits: document, report, file claim, adjuster review, settlement/payment."),
     ("Coverage Gap","Period without insurance coverage, or a situation not covered by your policy — identify and address gaps.")],
    [("Plan A ($300/month premium, $1,000 deductible) costs _____ in premiums per year.",["$1,200","$2,400","*$3,600","$6,000"],"300 × 12."),
     ("Plan B ($200/month premium, $3,000 deductible) costs _____ in premiums per year.",["$1,200","*$2,400","$3,600","$6,000"],"200 × 12."),
     ("In a healthy year (no claims), Plan B saves _____ vs. Plan A.",["$600","*$1,200 ($3,600 − $2,400 in premiums alone)","$2,000","$3,000"],"Premium savings."),
     ("In a major illness year, Plan A's better coverage means max OOP of $5,000 + $3,600 premiums = $8,600 total. Plan B:",["Costs the same","*$8,000 max OOP + $2,400 premiums = $10,400 total — Plan A saves $1,800 in a bad year","Costs less","No difference"],"Worst-case comparison."),
     ("An HSA-eligible HDHP has a minimum deductible of _____ (individual, 2024).",["$500","*$1,600","$3,000","$5,000"],"HDHP threshold."),
     ("The HSA contribution limit (individual, 2024) is approximately:",["$2,000","*$4,150","$7,000","$10,000"],"HSA limit."),
     ("HSA funds roll over _____ (unlike FSA).",["Until December 31","For one year","*Indefinitely — there is no 'use it or lose it' rule for HSA funds","Until age 65"],"Rollover advantage."),
     ("Life insurance needs for $80K/income family with mortgage: 10× income =",["$400,000","$600,000","*$800,000","$1,000,000"],"Income replacement."),
     ("A 30-year-old can get a 20-year $500,000 term life policy for approximately:",["$500/month","$100/month","*$25-40/month","$5/month"],"Very affordable."),
     ("Whole life insurance for the same coverage would cost approximately:",["The same","*$300-500+/month (10-15× more than term)","$50/month","$1,000/month"],"Term vs. whole cost."),
     ("For most families, the best life insurance strategy is:",["Buy whole life","*Buy affordable term insurance and invest the premium difference in index funds","Avoid all insurance","Buy the most expensive policy"],"Term + invest."),
     ("Auto insurance: $100,000/$300,000/$100,000 coverage means:",["$100K total","*$100K per person bodily injury / $300K per accident total / $100K property damage","100% coverage","$300K deductible"],"Liability limits."),
     ("Uninsured/underinsured motorist coverage protects you if:",["Your car breaks down","*The other driver has no insurance or not enough to cover your damages","You cause the accident","You don't have insurance"],"Protection from others."),
     ("Renter's insurance at $20/month provides approximately _____ in personal property coverage.",["$5,000","$10,000","*$20,000-30,000","$100,000"],"Affordable protection."),
     ("Flood insurance is _____ included in standard homeowner's policies.",["Always","*NOT (separate policy needed, often through NFIP — critical in flood-prone areas)","Sometimes","Included for free"],"Common gap."),
     ("Long-term care insurance covers:",["Short hospital stays","*Extended care needs: nursing homes, assisted living, in-home care (average cost: $60,000-100,000+/year)","Only medications","Only doctor visits"],"Major retirement risk."),
     ("The $#1 reason insurance claims are denied is:",["Bad luck","*Policy exclusions (the event isn't covered) or insufficient documentation — always READ your policy","Fraud","The company is corrupt"],"Read the policy."),
     ("Annual insurance review is important because:",["Nothing changes","*Life changes (marriage, baby, home, health, assets) require coverage updates to avoid gaps or overpaying","Rates never change","It's required by law"],"Update coverage."),
     ("Bundling insurance (auto + home with same company) typically saves:",["Nothing","*10-25% on premiums (loyalty discounts)","50%","The policies are free"],"Bundling discount."),
     ("For financial math, insurance decisions use:",["No calculations","*Expected value, cost-benefit, scenario analysis, and present value to make optimal protection decisions","Only feelings","Only agent recommendations"],"Math-driven protection.")]
)
lessons[k]=v

# 6.8
k,v = build_lesson(6,8,"Tax Software & Filing Tools",
    "<h3>Tax Software &amp; Filing Tools</h3>"
    "<h4>Tax Preparation Options</h4>"
    "<ul><li><b>Free File:</b> IRS Free File for income ≤ $79,000 (2024).</li>"
    "<li><b>Tax software:</b> TurboTax, H&R Block, TaxAct — guided interviews.</li>"
    "<li><b>CPA/Tax professional:</b> For complex situations (business, rental, investments).</li>"
    "<li><b>DIY:</b> Form 1040 — good for understanding the math behind software.</li></ul>",
    [("IRS Free File","Free tax preparation software available for income ≤ $79,000; accesses IRS-approved software at no cost."),
     ("Form W-2","Employer-provided form showing annual wages and tax withholdings; needed for tax filing."),
     ("Form 1099","Various forms reporting non-wage income: 1099-INT (interest), 1099-DIV (dividends), 1099-NEC (freelance)."),
     ("Form 1040","The main US individual income tax return form; all filers use this form."),
     ("Tax Refund","The difference when you've overpaid taxes through withholding — it's YOUR money being returned, not a gift from the government.")],
    [("IRS Free File is available for income up to:",["$50,000","*$79,000 (2024) — multiple software options available for free","$100,000","All incomes"],"Free option."),
     ("A W-2 form is provided by:",["The IRS","*Your employer (showing wages earned and taxes withheld during the year)","Your bank","Your accountant"],"Employer form."),
     ("1099-INT reports:",["Wages","*Interest income from banks and investments","Dividends","Self-employment income"],"Interest reporting."),
     ("1099-NEC (replacing 1099-MISC for payments) reports:",["Employee wages","*Non-employee compensation (freelance/contract income of $600+)","Bank interest","Dividends"],"Freelance reporting."),
     ("A tax refund means:",["The government gave you money","*You overpaid taxes during the year and are getting YOUR money back (not a bonus)","You owe nothing","You paid extra"],"Refund reality."),
     ("A large tax refund ($3,000+) means:",["You're doing great","*You've been giving the government a free loan — adjust withholding to keep more in each paycheck","You earned more","You should celebrate"],"Optimize withholding."),
     ("TurboTax and H&R Block software guide filing through:",["Filling forms manually","*Step-by-step interview questions that translate your answers into the correct forms automatically","Only professional help","Random guessing"],"Guided filing."),
     ("When should you hire a CPA/tax professional?",["Always","Never","*When you have complex situations: business income, rental property, stock options, multi-state filing, major life changes","Only if wealthy"],"Professional help trigger."),
     ("Average cost of professional tax preparation is:",["Free","$50","*$200-500+ (varies with complexity)","$5,000"],"Professional cost."),
     ("E-filing has _____ advantages over paper filing.",["No","*Multiple: faster refund (21 days vs. 6+ weeks), fewer errors, automatic calculations, confirmation of receipt","Only speed","Only for professionals"],"Electronic benefits."),
     ("The standard deduction vs. itemizing: take itemized if deductions exceed:",["$0","$5,000","*The standard deduction ($14,600 single / $29,200 MFJ in 2024)","$50,000"],"Deduction decision."),
     ("Common itemized deductions include:",["Only mortgage interest","*Mortgage interest, state/local taxes (SALT up to $10,000), charitable donations, and medical expenses (above 7.5% of AGI)","Only state taxes","Only charity"],"Itemization categories."),
     ("The SALT deduction cap is _____ per tax return.",["$5,000","*$10,000","$20,000","Unlimited"],"Current cap."),
     ("Tax extensions (Form 4868) give extra time to:",["Pay taxes","*File your return (6 more months) — but estimated taxes are still due by April 15","Avoid all taxes","Skip filing"],"Extension clarification."),
     ("Direct deposit of refund is:",["Optional and slow","*The fastest way to receive your refund (~21 days for e-filed returns with direct deposit)","Only for large refunds","Not available"],"Fastest refund."),
     ("Amended returns (Form 1040-X) are filed when:",["Every year","*You discover errors or omitted information on a previously filed return","Only if audited","Only for refunds"],"Correcting mistakes."),
     ("The IRS Free File Fillable Forms (for any income) provide:",["Full guidance","*Electronic blank tax forms with basic calculations — no guided interview (for those who know how to fill out forms)","No help","Only printable forms"],"DIY electronic option."),
     ("Identity theft protection for tax filing includes:",["Nothing needed","*Filing early, using secure software, protecting your SSN, and using an IP PIN (Identity Protection PIN) from the IRS","Only antivirus","Only a VPN"],"Security measures."),
     ("For students filing taxes for the first time, the best starting point is:",["A CPA","*IRS Free File or free software (simple W-2 income + standard deduction = straightforward first filing)","Paper forms","Ignoring it"],"First-time filing."),
     ("For financial math, tax filing applies:",["No course concepts","*Income calculations, deduction analysis, bracket math, and technology tools directly to a real annual obligation everyone faces","Only addition","Only for professionals"],"Math meets obligation.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 6: wrote {len(lessons)} lessons")
