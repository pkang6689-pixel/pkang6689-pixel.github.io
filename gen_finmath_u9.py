#!/usr/bin/env python3
"""Financial Math Unit 9 – Advanced Financial Concepts (8 lessons)."""
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

# 9.1
k,v = build_lesson(9,1,"Time Value of Money",
    "<h3>Time Value of Money (TVM)</h3>"
    "<h4>Core Principle</h4>"
    "<p>A dollar today is worth more than a dollar tomorrow because it can be invested to earn a return.</p>"
    "<h4>Key Formulas</h4>"
    "<ul><li><b>Future Value:</b> FV = PV × (1 + r)^n</li>"
    "<li><b>Present Value:</b> PV = FV / (1 + r)^n</li>"
    "<li><b>FV of Annuity:</b> FV = PMT × [((1+r)^n − 1) / r]</li>"
    "<li><b>PV of Annuity:</b> PV = PMT × [(1 − (1+r)^−n) / r]</li></ul>",
    [("Time Value of Money","Core finance principle: money available now is worth more than the same amount in the future due to its earning potential."),
     ("Present Value (PV)","The current worth of a future sum of money discounted at a given rate; answers 'What is $X in N years worth today?'"),
     ("Future Value (FV)","The value of a current amount after earning interest for N periods; FV = PV × (1+r)^n."),
     ("Discount Rate","The interest rate used to determine present value; reflects opportunity cost and risk."),
     ("Annuity","A series of equal payments made at regular intervals (mortgage payments, retirement withdrawals, insurance premiums).")],
    [("The time value of money means:",["Money loses value","Money is worthless tomorrow","*A dollar today is worth more than a dollar in the future because it can earn a return","All money is equal"],"Core principle."),
     ("FV of $10,000 at 8% for 10 years = $10,000 × (1.08)^10 ≈",["$15,000","$18,000","*$21,589","$25,000"],"FV calculation."),
     ("PV of $50,000 needed in 15 years at 7% discount rate = $50,000 / (1.07)^15 ≈",["$30,000","$25,000","*$18,125","$15,000"],"PV calculation."),
     ("The Rule of 72 estimates doubling time: 72 ÷ rate. At 8%, money doubles in approximately:",["6 years","*9 years","12 years","15 years"],"72 ÷ 8 = 9."),
     ("At 6%, money doubles in approximately _____ years.",["6","8","10","*12"],"72 ÷ 6 = 12."),
     ("FV of an annuity: $500/month at 8% annually (0.667%/month) for 30 years ≈",["$180,000","$350,000","*~$745,000","$1,000,000"],"Annuity FV."),
     ("The same $500/month at 10% for 30 years ≈",["$500,000","$750,000","*~$1,130,000","$2,000,000"],"Higher rate impact."),
     ("The difference between 8% and 10% over 30 years on $500/month is ≈",["$50,000","$200,000","*~$385,000 (rate differences compound enormously over long periods)","$500,000"],"Rate sensitivity."),
     ("PV of an annuity: $2,000/month for 25 years at 5% annual rate ≈",["$200,000","$400,000","*~$342,000","$600,000"],"PV annuity."),
     ("This PV is useful for determining:",["Future savings","*How much you need TODAY to fund $2,000/month withdrawals for 25 years of retirement","Monthly payments","Investment returns"],"Retirement planning."),
     ("A lottery choice: $1M now vs. $50,000/year for 30 years. At 5% discount, PV of annuity ≈",["$1,500,000","$1,000,000","*~$769,000 (lump sum of $1M now is worth more in present value terms)","$500,000"],"Lump sum vs. annuity."),
     ("The discount rate reflects:",["Only inflation","Only bank rates","*Opportunity cost — the return you could earn if you invested the money alternatively","Only the prime rate"],"Opportunity cost."),
     ("Higher discount rates make future cash flows worth _____ today.",["More","The same","*Less (future money is 'discounted' more heavily when alternative returns are higher)","Nothing"],"Rate-PV relationship."),
     ("Continuous compounding: FV = PV × e^(rt). $10,000 at 8% for 10 years ≈",["$18,000","$20,000","*$22,255 (slightly more than discrete compounding: $21,589)","$25,000"],"Continuous vs. discrete."),
     ("A perpetuity (infinite annuity) has PV = PMT / r. $1,000/year at 5% =",["$5,000","$10,000","*$20,000 ($1,000 ÷ 0.05)","$50,000"],"Perpetuity formula."),
     ("Growing annuity: payments that increase annually (like salary). PV formula includes:",["Only payment amount","*Both the discount rate AND the growth rate of payments","Only the growth rate","Only the number of periods"],"Growing cash flows."),
     ("Real vs. nominal rates: nominal 8% with 3% inflation gives real return of approximately:",["8%","3%","*~5% (nominal − inflation ≈ real return; more precisely: (1.08/1.03)−1 = 4.85%)","11%"],"Inflation adjustment."),
     ("TVM is the foundation of:",["Only savings accounts","*Nearly all financial decision-making: loans, investments, retirement planning, business valuation, insurance","Only bond pricing","Only one formula"],"Universal application."),
     ("A $200,000 home purchased in 1995 at 3% annual appreciation is worth approximately _____ in 2025.",["$300,000","$400,000","*~$485,000 ($200K × 1.03^30)","$600,000"],"Real estate TVM."),
     ("For financial math, TVM is:",["An optional topic","A minor concept","*THE most important concept — understanding present and future value is essential for every financial decision","Only for accountants"],"Foundational concept.")]
)
lessons[k]=v

# 9.2
k,v = build_lesson(9,2,"Net Present Value (NPV)",
    "<h3>Net Present Value</h3>"
    "<h4>NPV Formula</h4>"
    "<p>NPV = −Initial Investment + Σ (Cash Flow_t / (1+r)^t)</p>"
    "<p>If NPV > 0, the investment adds value. If NPV < 0, it destroys value.</p>"
    "<h4>Decision Rule</h4>"
    "<p>Accept projects with NPV > 0. Among multiple projects, choose the highest NPV.</p>",
    [("Net Present Value (NPV)","Sum of all discounted future cash flows minus the initial investment; measures whether an investment creates value."),
     ("Discount Rate (for NPV)","The required rate of return used to discount future cash flows; often the cost of capital or opportunity cost."),
     ("Cash Flow","The net money flowing in or out during each period; includes revenue minus expenses."),
     ("NPV Decision Rule","NPV > 0: accept (creates value). NPV < 0: reject (destroys value). NPV = 0: break-even return."),
     ("Capital Budgeting","The process of evaluating and selecting long-term investments using NPV, IRR, and payback period.")],
    [("NPV measures:",["Total revenue","Total costs","*The net value created (or destroyed) by an investment in today's dollars","Future revenue only"],"Value creation."),
     ("A $50,000 investment generating $15,000/year for 5 years at 10% discount rate: Year 1 PV =",["$15,000","$14,000","*$13,636 ($15,000 / 1.10)","$12,000"],"Year 1 discounting."),
     ("Year 2 PV = $15,000 / (1.10)^2 =",["$13,636","$13,000","*$12,397","$11,000"],"Year 2 discounting."),
     ("Year 3 PV = $15,000 / (1.10)^3 ≈",["$12,397","$12,000","*$11,270","$10,000"],"Year 3 discounting."),
     ("Sum of all 5 years' PV ≈ $13,636 + $12,397 + $11,270 + $10,245 + $9,314 =",["$50,000","$55,000","*$56,862","$60,000"],"Total PV of cash flows."),
     ("NPV = $56,862 − $50,000 =",["$0","$50,000","*$6,862 (positive: the investment creates value)","−$6,862"],"NPV result."),
     ("Since NPV > 0, the investor should:",["Reject the project","Wait","*Accept the project (it earns more than the 10% required return)","Negotiate"],"Decision."),
     ("If the discount rate were 15% instead, NPV would be:",["Higher","The same","*Lower (higher discount rate reduces the PV of future cash flows)","Unchanged"],"Rate sensitivity."),
     ("At 15% discount, NPV of the same project ≈ $50,281 − $50,000 =",["$6,862","$3,000","*~$281 (barely positive — much less attractive at higher required return)","−$5,000"],"Higher rate NPV."),
     ("At 20% discount, NPV would likely be:",["Positive","Zero","*Negative (the cash flows discounted at 20% are worth less than the $50,000 investment)","Very positive"],"Rejection threshold."),
     ("Choosing between Project A (NPV = $10,000) and Project B (NPV = $7,000):",["Choose B","Choose either","*Choose A (higher NPV = more value created for the investor)","Reject both"],"Ranking projects."),
     ("NPV assumes cash flows are reinvested at:",["0%","A different rate","*The discount rate (this is a key assumption of the NPV method)","The highest available rate"],"Reinvestment assumption."),
     ("A real estate investment: $200,000 purchase, $1,500/month rent, $2,500/month expenses. Annual net cash flow =",["$18,000","$30,000","*−$12,000 loss (($1,500 − $2,500) × 12 = −$12,000 — but may have appreciation)","$12,000"],"Cash flow analysis."),
     ("Including 3% annual appreciation, the property value after 10 years ≈",["$200,000","$250,000","*~$269,000 ($200K × 1.03^10)","$300,000"],"Appreciation value."),
     ("Total NPV for the property must include:",["Only rent","Only appreciation","*Both annual cash flows (possibly negative) AND terminal sale value, all discounted to present","Only purchase price"],"Complete analysis."),
     ("Sensitivity analysis on NPV varies:",["Nothing","*Discount rate, cash flow estimates, and timing to see how NPV changes under different scenarios","Only one variable","Only the investment amount"],"Stress testing."),
     ("NPV in Excel uses the formula =NPV(rate, cash_flows) + initial_investment where initial investment is:",["Positive","*Negative (cash outflow at time zero — note: Excel's NPV function starts at period 1)","Zero","The discount rate"],"Excel NPV."),
     ("The WACC (Weighted Average Cost of Capital) is often used as the discount rate because it represents:",["The highest return","*The blended cost of all funding sources (debt and equity) — the minimum return the company needs to create value","The lowest return","Only debt cost"],"Corporate discount rate."),
     ("Standalone NPV ignores:",["Revenue","*Strategic value, synergies, learning effects, and options the project creates for future opportunities","All cash flows","The discount rate"],"Real options."),
     ("For financial math, NPV is:",["A minor concept","Too complex","*One of the most important tools in finance — used for business investments, real estate, and any decision involving future cash flows","Only for corporations"],"Essential decision tool.")]
)
lessons[k]=v

# 9.3
k,v = build_lesson(9,3,"Internal Rate of Return (IRR)",
    "<h3>Internal Rate of Return</h3>"
    "<h4>IRR Definition</h4>"
    "<p>The discount rate that makes NPV = 0. It's the project's effective annual return.</p>"
    "<h4>Decision Rule</h4>"
    "<p>If IRR > required return (hurdle rate): accept. If IRR < hurdle rate: reject.</p>",
    [("IRR (Internal Rate of Return)","The discount rate that makes NPV exactly zero; represents the project's annualized effective return rate."),
     ("Hurdle Rate","The minimum acceptable rate of return for an investment; IRR must exceed this for the project to be accepted."),
     ("IRR vs. NPV","IRR gives a rate of return (percentage); NPV gives a dollar value. NPV is generally preferred for conflicting projects."),
     ("MIRR (Modified IRR)","Modified IRR that assumes reinvestment at the cost of capital (more realistic than IRR's reinvestment assumption)."),
     ("Trial and Error / Interpolation","Traditional method for finding IRR by testing discount rates until NPV ≈ 0; modern tools (Excel) calculate instantly.")],
    [("IRR is the discount rate that makes NPV equal to:",["The initial investment","Infinity","*Zero (the rate at which the project breaks even in present value terms)","The highest possible value"],"IRR definition."),
     ("If a project's IRR is 15% and the required return is 10%, you should:",["Reject it","Wait","*Accept it (IRR exceeds the hurdle rate by 5 percentage points)","Request more data"],"Decision rule."),
     ("If IRR is 8% and the hurdle rate is 12%, you should:",["Accept it","*Reject it (the project doesn't meet the minimum required return)","Accept at a lower amount","Wait for rates to change"],"Below hurdle."),
     ("For the earlier example ($50K investment, $15K/year for 5 years), IRR ≈",["10%","12%","*~15.2% (the rate where NPV of these cash flows = $50,000)","20%"],"Example IRR."),
     ("Excel calculates IRR using:",["NPV function","PMT function","*=IRR(range_of_cash_flows) — starting with the negative initial investment","RATE function"],"Excel IRR."),
     ("IRR assumes reinvestment of intermediate cash flows at:",["0%","The risk-free rate","*The IRR itself (which may be unrealistically high — a key limitation)","The cost of capital"],"Reinvestment assumption."),
     ("MIRR (Modified IRR) addresses this by assuming reinvestment at:",["The IRR","0%","*The cost of capital (a more realistic assumption)","The risk-free rate"],"MIRR improvement."),
     ("When comparing two mutually exclusive projects, _____ is more reliable.",["IRR","Both equally","*NPV (it measures absolute value created; IRR can give conflicting rankings for different-sized projects)","Neither"],"NPV preferred."),
     ("Project A: $10K investment, IRR 25%. Project B: $100K investment, IRR 18%. Which creates more value?",["A (higher IRR)","*B likely creates more dollar value (NPV) despite lower IRR — $100K × 18% > $10K × 25% in absolute terms","They're equal","Can't determine"],"Scale matters."),
     ("Multiple IRRs can occur when:",["Cash flows are all positive","Cash flows are all negative","*Cash flows switch signs more than once (e.g., large initial investment, positive cash flows, then large terminal cost)","Never"],"Non-conventional cash flows."),
     ("A project with alternating positive and negative cash flows may have:",["One IRR","*Multiple IRRs or no real IRR (making NPV the better decision tool)","Zero IRR","Negative IRR only"],"IRR limitations."),
     ("IRR of a bond held to maturity equals its:",["Coupon rate","*Yield to Maturity (YTM) — the rate that equates the PV of all coupon payments + face value to current price","Face value","Market price"],"Bond IRR."),
     ("Startup investors use IRR to evaluate:",["Only revenue","*The annualized return on their investment based on the exit value relative to the entry price and holding period","Only expenses","Only market share"],"VC perspective."),
     ("A VC investing $1M for a $5M return in 5 years has an IRR of:",["100%","25%","*~38% ((5/1)^(1/5) − 1 = 0.38)","50%"],"VC IRR calculation."),
     ("A VC investing $1M for a $10M return in 7 years has an IRR of:",["100%","25%","*~39% ((10/1)^(1/7) − 1 = 0.389)","50%"],"Higher return, longer period."),
     ("Real estate IRR includes:",["Only rent","Only appreciation","*All cash flows: purchase cost, rental income, expenses, tax benefits, and final sale price","Only tax benefits"],"Comprehensive real estate returns."),
     ("Payback period is simpler than IRR because:",["It's more accurate","*It only measures how quickly you get your money back (ignoring time value and cash flows beyond payback)","It considers all cash flows","It uses discounting"],"Simpler but limited."),
     ("Discounted payback period improves payback by:",["Using larger cash flows","*Discounting each year's cash flow before calculating when cumulative PV = initial investment","Ignoring time value","Using lower rates"],"Better payback."),
     ("Together, NPV, IRR, and payback period provide:",["Redundant information","*Complementary perspectives: dollar value (NPV), percentage return (IRR), and time to recovery (payback)","Only one useful metric","Conflicting answers always"],"Multiple tools."),
     ("For financial math, IRR is essential for:",["Only academics","*Evaluating any investment where you invest now and receive returns over time — from business projects to personal investments","Only large corporations","Only banking"],"Universal return metric.")]
)
lessons[k]=v

# 9.4
k,v = build_lesson(9,4,"Financial Modeling",
    "<h3>Financial Modeling</h3>"
    "<h4>Building Financial Models</h4>"
    "<ul><li><b>Inputs:</b> Assumptions (growth rate, costs, discount rate).</li>"
    "<li><b>Calculations:</b> Revenue projections, expense forecasts, cash flows.</li>"
    "<li><b>Outputs:</b> NPV, IRR, break-even, financial statements.</li></ul>"
    "<h4>Scenario Analysis</h4>"
    "<p>Best case, base case, worst case — testing how changes in assumptions affect outcomes.</p>",
    [("Financial Model","A spreadsheet-based tool that projects financial performance using assumptions, formulas, and scenarios."),
     ("Scenario Analysis","Testing best case, base case, and worst case assumptions to understand the range of possible outcomes."),
     ("Sensitivity Analysis","Changing ONE variable at a time to see its impact on the output (e.g., how does profit change if revenue drops 10%?)."),
     ("Pro Forma Statements","Projected/forecasted financial statements (income statement, balance sheet, cash flow) based on assumptions."),
     ("Monte Carlo Simulation","Advanced modeling using thousands of random scenarios to produce probability distributions of outcomes.")],
    [("A financial model takes _____ and produces _____.",["Outputs, inputs","*Assumptions (inputs) and produces projections/decisions (outputs)","Random data, random results","Only one number, one result"],"Model structure."),
     ("The three essential financial statements in a model are:",["Only income statement","*Income statement, balance sheet, and cash flow statement (all interconnected)","Only balance sheet","Only cash flow"],"Three statements."),
     ("Scenario analysis tests:",["One outcome","*Multiple outcomes: best case, base case, and worst case scenarios with different assumptions","Only the best outcome","Only the worst outcome"],"Range of outcomes."),
     ("In a base case: revenue grows 10%, costs grow 5%. In worst case: revenue grows 2%, costs grow 8%. The model shows:",["No difference","*Dramatically different profitability — the worst case may show losses, guiding risk management decisions","Identical results","Only base case matters"],"Scenario comparison."),
     ("Sensitivity analysis differs from scenario analysis because it:",["Changes nothing","*Changes ONE variable at a time (holding all others constant) to isolate each factor's impact","Changes everything simultaneously","Is less useful"],"Single-variable testing."),
     ("A 'data table' in Excel performs sensitivity analysis by:",["Only displaying data","*Automatically calculating outputs across a range of input values (e.g., NPV for discount rates from 5% to 15%)","Only formatting cells","Only charting"],"Excel tool."),
     ("Revenue projection: Year 1 = $100,000 growing at 15% annually. Year 3 revenue =",["$115,000","$130,000","*$132,250 ($100K × 1.15^2)","$145,000"],"Growth projection."),
     ("If COGS is 40% of revenue, Year 3 COGS =",["$40,000","$48,000","*$52,900 (132250 × 0.40)","$60,000"],"Cost percentage."),
     ("Year 3 gross profit = $132,250 − $52,900 =",["$52,900","$70,000","*$79,350","$132,250"],"Gross profit."),
     ("A 5-year DCF model discounts projected free cash flows to find:",["Revenue","*Enterprise value (the present value of all future cash flows the business is expected to generate)","Only expenses","Market price"],"Business valuation."),
     ("Terminal value in a DCF model represents:",["Year 1 value","*The value of all cash flows beyond the explicit forecast period (often 60-80% of total enterprise value)","Only the last year","The purchase price"],"Beyond forecast horizon."),
     ("Terminal value using the perpetuity growth method: TV = FCF × (1+g) / (r−g). If FCF = $1M, g = 3%, r = 10%:",["$10M","$12M","*$14.7M ($1M × 1.03 / 0.07)","$20M"],"Terminal value calculation."),
     ("Monte Carlo simulation:",["Uses one scenario","*Runs thousands of random scenarios based on probability distributions to produce a range of likely outcomes","Is purely theoretical","Required exact inputs"],"Probabilistic modeling."),
     ("The output of Monte Carlo simulation is:",["A single number","*A probability distribution showing the likelihood of various outcomes (e.g., 'there's a 90% chance NPV > $0')","A perfect prediction","Only the average"],"Distribution of outcomes."),
     ("Model validation involves:",["Never checking","*Comparing model outputs to historical data, industry benchmarks, and logical sense-checks","Only checking formulas","Only running once"],"Quality assurance."),
     ("Garbage in, garbage out (GIGO) means:",["Models are worthless","*Model outputs are only as good as the assumptions — unrealistic inputs produce unrealistic results","All models are perfect","Only use default values"],"Assumption quality."),
     ("Key assumptions to document in any model include:",["Nothing","*Growth rates, margins, discount rate, tax rate, capital expenditures, and working capital needs","Only revenue","Only expenses"],"Transparent assumptions."),
     ("Break-even analysis in a financial model shows:",["Only revenue needed","*The combination of price, volume, and costs where the business achieves zero profit — a critical viability threshold","Only costs","Only the best case"],"Viability analysis."),
     ("Professional financial models follow best practices:",["No standards exist","*Color coding (blue = inputs, black = formulas), clear structure, documentation, and error checking","Any format works","Only aesthetics matter"],"Model standards."),
     ("For financial math, financial modeling integrates:",["Only one concept","*TVM, NPV, IRR, break-even, growth projections, and scenario analysis — the culmination of all financial math skills","Only technology","Only spreadsheets"],"Comprehensive application.")]
)
lessons[k]=v

# 9.5
k,v = build_lesson(9,5,"Corporate Finance Fundamentals",
    "<h3>Corporate Finance</h3>"
    "<h4>Capital Structure</h4>"
    "<p>The mix of <b>debt</b> (loans, bonds) and <b>equity</b> (stock, retained earnings) used to finance a company.</p>"
    "<h4>Cost of Capital</h4>"
    "<ul><li><b>Cost of Debt:</b> Interest rate on borrowing × (1 − tax rate) — interest is tax-deductible.</li>"
    "<li><b>Cost of Equity:</b> Return required by shareholders (typically estimated via CAPM).</li>"
    "<li><b>WACC:</b> Weighted average of debt and equity costs.</li></ul>",
    [("Capital Structure","The proportion of debt vs. equity a company uses for financing; affects risk, cost of capital, and returns."),
     ("WACC (Weighted Average Cost of Capital)","The blended rate: (% debt × cost of debt after tax) + (% equity × cost of equity); the minimum return for new projects."),
     ("CAPM (Capital Asset Pricing Model)","Cost of equity = Risk-free rate + Beta × (Market return − Risk-free rate); relates required return to risk."),
     ("Beta","Measure of a stock's volatility relative to the market; β=1 moves with market, β>1 more volatile, β<1 less volatile."),
     ("Leverage","Using debt to amplify returns (and risks); measured by debt-to-equity ratio.")],
    [("Capital structure refers to:",["Only cash on hand","*The mix of debt and equity financing a company uses","Only stock price","Only bond payments"],"Financing mix."),
     ("Debt financing has a tax advantage because:",["Interest is not deductible","*Interest payments are tax-deductible (reducing the effective cost of debt)","Dividends are deductible","There is no advantage"],"Tax shield."),
     ("Cost of debt: 6% interest rate × (1 − 25% tax rate) = after-tax cost of:",["6%","5%","*4.5% (0.06 × 0.75)","3%"],"After-tax cost."),
     ("CAPM: Risk-free rate 3% + Beta 1.2 × (Market return 10% − Risk-free 3%). Cost of equity =",["10%","8.4%","*11.4% (3% + 1.2 × 7%)","12%"],"CAPM calculation."),
     ("A beta of 1.5 means the stock is approximately _____ as volatile as the market.",["Equal","*50% more volatile","50% less volatile","Twice"],"Beta interpretation."),
     ("A beta of 0.7 means the stock is approximately _____ as volatile as the market.",["More","*30% less volatile (moves less than the market in either direction)","Equal","Twice"],"Low beta."),
     ("WACC with 40% debt at 4.5% after-tax, 60% equity at 11.4%:",["4.5%","8%","*8.64% (0.40×4.5% + 0.60×11.4% = 1.8% + 6.84%)","11.4%"],"WACC calculation."),
     ("A new project should be accepted if its expected return exceeds:",["0%","The risk-free rate","*WACC (the project must earn at least the blended cost of financing it)","The highest available rate"],"Hurdle rate."),
     ("Too much debt (overleveraging) increases:",["Nothing","*Financial risk: interest payments are fixed obligations that must be paid regardless of revenue","Only equity returns","Only stock price"],"Leverage risk."),
     ("Optimal capital structure balances:",["Only debt","Only equity","*The tax benefits of debt against the increased bankruptcy risk of too much debt","Revenue and expenses"],"Tradeoff theory."),
     ("Modigliani-Miller theorem (with taxes) states:",["Debt doesn't matter","*The value of a company increases with debt (due to tax shields) — up to the point where bankruptcy risk offsets the tax benefit","All debt is bad","All equity is best"],"MM theorem."),
     ("Retained earnings are:",["External equity","Debt","*Internal equity — profits reinvested in the business rather than paid as dividends (cheapest form of equity)","Cash only"],"Internal financing."),
     ("Dividend policy decisions involve:",["Only paying dividends","*Whether to pay profits as dividends (returning cash to shareholders) or retain them for growth and reinvestment","Only retaining profits","Only stock buybacks"],"Payout decisions."),
     ("Stock buybacks reduce:",["Revenue","Debt","*Shares outstanding (increasing EPS and often stock price — an alternative to dividends)","Expenses"],"Share repurchase."),
     ("Free Cash Flow (FCF) = Operating cash flow minus:",["Revenue","*Capital expenditures (the cash available to pay debt holders and equity holders)","Dividends","Stock price"],"FCF definition."),
     ("Enterprise Value = Market Cap + Debt − Cash. If market cap = $500M, debt = $100M, cash = $50M:",["$500M","$600M","*$550M","$450M"],"EV calculation."),
     ("EV/EBITDA ratio is used to:",["Calculate revenue","*Value and compare companies (a lower ratio may indicate undervaluation)","Only measure debt","Only measure cash flow"],"Valuation multiple."),
     ("Financial leverage ratio = Total Assets / Total Equity. $10M assets / $4M equity =",["0.4","1.0","*2.5 (for every $1 of equity, the company has $2.50 in assets)","10"],"Leverage measure."),
     ("Working capital management focuses on:",["Long-term investments","*Short-term assets and liabilities: inventory, receivables, payables — ensuring adequate cash flow for daily operations","Only stock price","Only dividends"],"Operational finance."),
     ("For financial math, corporate finance applies:",["No math","*WACC, CAPM, leverage ratios, and capital budgeting — quantitative tools used by finance professionals worldwide","Only theory","Only for CFOs"],"Professional-grade math.")]
)
lessons[k]=v

# 9.6
k,v = build_lesson(9,6,"Risk Analysis & Quantification",
    "<h3>Risk Analysis</h3>"
    "<h4>Measuring Risk</h4>"
    "<ul><li><b>Standard Deviation:</b> Measures volatility of returns (higher = more risk).</li>"
    "<li><b>Sharpe Ratio:</b> (Return − Risk-free Rate) / Standard Deviation — risk-adjusted return.</li>"
    "<li><b>Value at Risk (VaR):</b> Maximum expected loss at a given confidence level.</li></ul>",
    [("Standard Deviation (Finance)","A measure of investment return volatility; higher σ = more dispersion around the average return = more risk."),
     ("Sharpe Ratio","(Portfolio return − risk-free rate) ÷ standard deviation; measures excess return per unit of risk. Higher is better."),
     ("Value at Risk (VaR)","The maximum expected loss over a given period at a specified confidence level (e.g., '95% VaR of $50,000' means 95% chance of losing less than $50K)."),
     ("Correlation","Measure of how two investments move relative to each other; −1 (opposite) to +1 (perfectly together). Low correlation = better diversification."),
     ("Risk-Adjusted Return","Return compared to the risk taken; two investments with the same return but different risk levels have different risk-adjusted returns.")],
    [("Standard deviation in finance measures:",["Average return","Total return","*Volatility — how much returns deviate from the average (higher σ = more uncertainty)","Only losses"],"Dispersion of returns."),
     ("Investment A: 10% avg return, 15% std dev. Investment B: 10% avg return, 5% std dev. Which is riskier?",["B","They're equal","*A (same return but 3× the volatility — wider range of possible outcomes)","Neither"],"Same return, different risk."),
     ("The Sharpe ratio for A (10% return, 3% risk-free, 15% std dev) =",["0.67","*0.47 ((10−3)/15)","0.33","1.0"],"Sharpe A."),
     ("The Sharpe ratio for B (10% return, 3% risk-free, 5% std dev) =",["0.47","1.0","*1.4 ((10−3)/5)","2.0"],"Sharpe B."),
     ("Investor should choose _____ because it has a higher Sharpe ratio.",["A","*B (same return with much less risk — more efficient risk-adjusted return)","Either","Neither"],"Risk-adjusted choice."),
     ("A Sharpe ratio above 1.0 is generally considered:",["Poor","Average","*Good (the investment's excess return exceeds its risk)","Impossible"],"Sharpe benchmark."),
     ("VaR at 95% confidence of $100,000 means:",["You'll lose exactly $100K","You'll definitely lose","*There's a 95% chance you'll lose LESS than $100K in the specified period (5% chance of losing more)","You'll gain $100K"],"VaR interpretation."),
     ("Correlation of +1 between two stocks means:",["They're unrelated","*They move perfectly together (no diversification benefit)","They move oppositely","They're uncorrelated"],"Perfect positive."),
     ("Correlation of −1 means:",["They move together","*They move in exactly opposite directions (maximum diversification benefit)","They're unrelated","Correlation is zero"],"Perfect negative."),
     ("A portfolio of stocks with low correlation to each other has:",["Higher total risk","*Lower total risk than the average of individual risks (diversification effect)","Same total risk","No return"],"Diversification benefit."),
     ("The efficient frontier shows:",["One perfect portfolio","*The set of portfolios offering maximum return for each level of risk (or minimum risk for each return level)","All possible portfolios","Only high-risk portfolios"],"Optimal portfolios."),
     ("Modern Portfolio Theory (MPT) was developed by:",["Warren Buffett","Benjamin Graham","*Harry Markowitz (1952) — foundational theory that diversification reduces portfolio risk","John Bogle"],"MPT originator."),
     ("Portfolio A: 12% return, 18% std dev. Portfolio B: 10% return, 10% std dev. If risk-free = 3%:",["A is clearly better","*A Sharpe = 0.50, B Sharpe = 0.70 — B is better risk-adjusted despite lower absolute return","B is clearly worse","They're equal"],"Comparing portfolios."),
     ("Systematic risk (market risk) can _____ be diversified away.",["Always","*Never (it affects the entire market: interest rates, recessions, geopolitical events)","Sometimes","Only with bonds"],"Non-diversifiable."),
     ("Unsystematic risk (company-specific) can _____ be diversified away.",["Never","*Usually (holding 20-30 diversified stocks eliminates most company-specific risk)","Partially, but requires 1000+ stocks","Only with options"],"Diversifiable."),
     ("Beta measures only _____ risk.",["Total","Unsystematic","*Systematic (market-related volatility that cannot be diversified away)","No"],"Beta and systematic risk."),
     ("The risk-return tradeoff states:",["Higher risk, lower return","*Higher risk investments must offer higher EXPECTED returns to attract investors (compensation for bearing risk)","Risk and return are unrelated","Lower risk, higher return"],"Fundamental tradeoff."),
     ("Stress testing a portfolio involves:",["Normal conditions only","*Simulating extreme scenarios (market crash, interest rate spike, pandemic) to see how the portfolio performs under stress","Only past performance","Only one scenario"],"Extreme scenario analysis."),
     ("Maximum drawdown measures:",["Average loss","*The largest peak-to-trough decline in portfolio value (how bad the worst period was)","Daily volatility","Only single-day losses"],"Worst decline."),
     ("For financial math, risk analysis provides:",["Subjective judgment","*Quantitative tools (σ, Sharpe, VaR, correlation) to objectively compare investments and construct optimal portfolios","Only qualitative assessment","Only intuition"],"Quantitative risk assessment.")]
)
lessons[k]=v

# 9.7
k,v = build_lesson(9,7,"AP Economics & Finance Connections",
    "<h3>AP Economics &amp; Finance Connections</h3>"
    "<h4>Macro Concepts in Finance</h4>"
    "<ul><li><b>GDP:</b> Total economic output — impacts corporate earnings and stock market.</li>"
    "<li><b>Inflation:</b> Erodes purchasing power; affects interest rates and investment decisions.</li>"
    "<li><b>Federal Reserve:</b> Sets monetary policy (interest rates, money supply) affecting all financial markets.</li>"
    "<li><b>Fiscal Policy:</b> Government spending and taxation affecting economic growth.</li></ul>",
    [("GDP and Finance","GDP growth drives corporate earnings; recessions (negative GDP) trigger bear markets. Strong GDP = bullish for stocks."),
     ("Inflation Impact on Investments","Inflation erodes real returns. At 3% inflation, a 7% nominal return yields only ~4% real return."),
     ("Federal Reserve (The Fed)","US central bank controlling monetary policy: setting interest rates (federal funds rate) and managing money supply."),
     ("Monetary Policy","Fed actions to control money supply and interest rates: raising rates slows economy/inflation; lowering rates stimulates growth."),
     ("Supply and Demand in Markets","Stock prices are determined by supply/demand: more buyers than sellers = price rises; more sellers = price falls.")],
    [("When GDP grows, stock markets tend to:",["Fall","*Rise (economic growth means higher corporate earnings, which drives stock prices up)","Stay flat","Become unpredictable"],"GDP-market link."),
     ("During a recession (negative GDP growth), stocks typically:",["Rise sharply","*Fall (reduced economic activity means lower corporate profits and investor pessimism)","Stay the same","Always crash 50%"],"Recession impact."),
     ("Inflation at 3% reduces the purchasing power of $100 to approximately _____ after 10 years.",["$97","$85","*~$74 ($100 × 0.97^10)","$70"],"Inflation erosion."),
     ("If your investment returns 8% and inflation is 3%, your real return is approximately:",["8%","3%","*~5% (nominal return minus inflation ≈ real return)","11%"],"Real return."),
     ("The Federal Reserve raises interest rates to:",["Stimulate growth","*Combat inflation (higher rates reduce borrowing, slow spending, and cool the economy)","Increase stock prices","Help borrowers"],"Contractionary policy."),
     ("The Federal Reserve lowers interest rates to:",["*Stimulate economic growth (cheaper borrowing encourages spending and investment)","Fight inflation","Strengthen the dollar","Reduce bank profits"],"Expansionary policy."),
     ("When the Fed raises rates, bond prices:",["Rise","Stay the same","*Fall (existing bonds with lower rates become less attractive; their prices must drop to offer competitive yields)","Double"],"Rate-bond relationship."),
     ("When the Fed raises rates, stock prices tend to:",["Always rise","*Often fall (higher rates increase borrowing costs, reduce future earnings, and make bonds more competitive)","Always stay flat","Always double"],"Rate-stock relationship."),
     ("Fiscal policy involves:",["Only the Fed","*Government spending and taxation decisions (Congress/President) — stimulus spending, tax cuts, infrastructure investment","Only banks","Only corporations"],"Government economic tools."),
     ("Expansionary fiscal policy (more spending, lower taxes) tends to:",["Slow the economy","*Stimulate economic growth (but may increase deficits and future inflation)","Have no effect","Only help banks"],"Stimulative policy."),
     ("The national debt impacts finance because:",["It doesn't","*Large debt may lead to higher future taxes, inflation, or crowding out private investment as government competes for borrowing","It's irrelevant","Only affects government"],"Debt implications."),
     ("Supply and demand determines stock prices because:",["Prices are fixed","*When more people want to buy (demand) than sell (supply), the price rises; when more want to sell, the price falls","Only the company sets the price","The exchange sets all prices"],"Market price discovery."),
     ("Opportunity cost in investment decisions means:",["No cost","*The return on the next best alternative you give up (investing in Stock A means giving up potential returns from Stock B)","Only explicit costs","Only dollar costs"],"True cost of a decision."),
     ("Comparative advantage applies to:",["Only countries","*Both countries (trade) and individuals/businesses (specializing in what you do most efficiently)","Only individuals","Only investors"],"Specialization."),
     ("The yield curve (plotting bond yields by maturity) normally slopes:",["Downward","*Upward (longer-term bonds yield more because they carry more risk from inflation and uncertainty)","Flat always","Randomly"],"Normal yield curve."),
     ("An inverted yield curve (short-term rates > long-term) often predicts:",["Economic boom","*Recession (historically one of the most reliable recession indicators)","Higher stock prices","No change"],"Recession predictor."),
     ("The Consumer Price Index (CPI) measures:",["GDP","Stock prices","*The average change in prices paid by consumers for goods and services (the primary inflation measure)","Bond yields"],"Inflation gauge."),
     ("Understanding macroeconomics helps investors because:",["It doesn't help","*Economic conditions (GDP, inflation, rates, fiscal policy) drive market performance and should inform investment strategy","Only economists need this","Only for professional traders"],"Macro awareness."),
     ("The business cycle (expansion → peak → contraction → trough) means:",["Markets only go up","*Different investment strategies work better in different phases (cyclical vs. defensive stocks, bonds vs. stocks)","Markets only go down","The economy never changes"],"Cycle awareness."),
     ("For the AP exam and financial math, economics-finance connections show:",["They're unrelated fields","*How macroeconomic forces directly drive financial markets — connecting classroom economic theory to real-world investment implications","Only theory matters","Only math matters"],"Integrated understanding.")]
)
lessons[k]=v

# 9.8
k,v = build_lesson(9,8,"International Finance Case Studies",
    "<h3>International Finance Case Studies</h3>"
    "<h4>Case 1: Currency Impact on Investment Returns</h4>"
    "<p>A US investor buys European stock at €100 when 1 EUR = 1.10 USD (cost: $110). Stock rises 10% to €110. "
    "If EUR weakens to 1 EUR = 1.05 USD: $110 × 1.05 = $115.50 return on $110 cost = 5% return (vs. 10% in euros).</p>"
    "<h4>Case 2: Emerging Market Opportunities</h4>"
    "<p>Higher growth potential (7-8% GDP) vs. developed markets (2-3%), but with currency risk, political risk, and volatility.</p>",
    [("Currency Risk (FX Risk)","The risk that exchange rate changes will reduce the value of international investments when converted back to the investor's home currency."),
     ("Hedging Currency Risk","Using forward contracts, options, or currency-hedged ETFs to protect against unfavorable exchange rate movements."),
     ("Emerging Markets","Developing countries with rapidly growing economies (China, India, Brazil); higher potential returns but higher risk."),
     ("Carry Trade","Borrowing in a low-interest-rate currency and investing in a high-interest-rate currency; profitable until rates or exchange rates shift."),
     ("Sovereign Risk","The risk that a foreign government defaults on debt, imposes capital controls, or makes policy changes that harm investments.")],
    [("A US investor buying European stock must consider:",["Only stock performance","*Both stock performance AND currency exchange rate changes (returns can be enhanced or reduced by FX moves)","Only economic data","Only US markets"],"Dual return components."),
     ("€100 stock bought at 1 EUR = 1.10 USD. Cost in dollars =",["$100","*$110 (100 × 1.10)","$90","$111"],"Purchase cost."),
     ("Stock rises 10% to €110. EUR weakens to 1.05 USD. Value in dollars =",["$121","$110","*$115.50 (110 × 1.05)","$105"],"FX-adjusted value."),
     ("Dollar return = ($115.50 − $110) / $110 =",["10%","*~5% (currency weakness eroded half the stock gain)","0%","−5%"],"Reduced return."),
     ("If EUR instead strengthened to 1.15 USD, the dollar value would be:",["$110","$121","*$126.50 (110 × 1.15) — a 15% return thanks to both stock gains and currency gains","$115.50"],"Currency boost."),
     ("Currency-hedged ETFs attempt to:",["Maximize currency exposure","*Eliminate currency fluctuation effects so returns more closely match the underlying foreign stock performance","Only invest in USD","Avoid all foreign stocks"],"Hedging strategy."),
     ("Emerging market GDP growth rates are typically _____ than developed markets.",["Lower","The same","*Higher (5-8% vs. 2-3% in developed markets — faster economic growth)","Negative"],"Growth differential."),
     ("Emerging market risks include:",["Only currency risk","*Currency volatility, political instability, less regulation, lower liquidity, and corporate governance concerns","No additional risks","Only small risks"],"Multiple risk factors."),
     ("The MSCI Emerging Markets index includes stocks from:",["Only China","Only India","*Multiple countries: China, India, Brazil, Taiwan, South Korea, South Africa, and more","Only US companies abroad"],"Broad EM exposure."),
     ("A carry trade borrowing yen at 0.1% to invest in Brazil at 10% earns approximately:",["0.1%","10%","*~9.9% spread (but highly risky if the yen strengthens or Brazilian real weakens)","5%"],"Carry return."),
     ("The 1997 Asian Financial Crisis demonstrated:",["Emerging markets always succeed","*The risks of currency pegs, excessive borrowing, and lack of financial regulation in emerging markets","Asia has no risk","Only political risk"],"Crisis lesson."),
     ("The 2001 Argentine debt crisis showed:",["Sovereign default never happens","*Countries can default on debt, devalue currency, and impose capital controls — devastating for foreign investors","Argentina is risk-free","Only small countries default"],"Sovereign risk reality."),
     ("International diversification benefits US investors because:",["All markets move identically","*Different countries' economic cycles don't perfectly correlate — international stocks may zig when US stocks zag","It's required by law","Only for large portfolios"],"Correlation benefit."),
     ("The optimal allocation to international stocks is often cited as:",["0%","10%","*20-40% of equity allocation (significant international exposure for diversification)","100%"],"Recommended allocation."),
     ("ADRs (American Depositary Receipts) allow US investors to:",["Only buy US stocks","*Buy foreign stocks on US exchanges (traded in USD, eliminating some — but not all — complexity of foreign investing)","Avoid all foreign risk","Only buy bonds"],"Easy international access."),
     ("Transfer pricing and tax treaties affect:",["Only domestic companies","*Multinational corporations' tax obligations across countries (complex international tax planning)","Only small businesses","Nothing financial"],"International tax."),
     ("The World Bank and IMF help:",["Only wealthy nations","*Developing countries with loans, economic advice, and crisis support (promoting global economic stability)","Only US companies","Only banks"],"Global institutions."),
     ("Global supply chains mean that even domestic companies face:",["No international risk","*International risks (currency fluctuations, trade policies, and geopolitical disruptions affect supply costs and availability)","Only domestic risks","Complete isolation"],"Indirect global exposure."),
     ("Trade wars and tariffs affect investments by:",["Having no impact","*Increasing costs, disrupting supply chains, and creating uncertainty that can reduce stock prices and economic growth","Only helping domestic companies","Only affecting imports"],"Trade policy impact."),
     ("For financial math, international finance adds:",["No complexity","*Currency conversion math, exchange rate risk analysis, and diversification calculations to the broader financial math toolkit","Only language barriers","Only travel costs"],"Global math skills.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 9: wrote {len(lessons)} lessons")
