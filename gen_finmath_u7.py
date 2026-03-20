#!/usr/bin/env python3
"""Financial Math Unit 7 – Business & Entrepreneurship (8 lessons)."""
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

# 7.1
k,v = build_lesson(7,1,"Starting a Business",
    "<h3>Starting a Business</h3>"
    "<h4>Business Formation Basics</h4>"
    "<ul><li><b>Sole Proprietorship:</b> Simplest; owner = business. Unlimited personal liability.</li>"
    "<li><b>Partnership:</b> Two+ owners share profits, losses, and liability.</li>"
    "<li><b>LLC:</b> Limited liability protection; pass-through taxation. Most popular for small businesses.</li>"
    "<li><b>Corporation:</b> Separate legal entity. C-Corp: double taxation. S-Corp: pass-through.</li></ul>"
    "<h4>Start-up Costs</h4>"
    "<p>One-time costs (equipment, licenses, legal fees) vs. recurring costs (rent, utilities, payroll).</p>",
    [("Sole Proprietorship","Simplest business structure; owner has complete control but unlimited personal liability for all debts."),
     ("LLC (Limited Liability Company)","Business structure providing personal liability protection with pass-through taxation — combines benefits of corporation and sole proprietorship."),
     ("Start-up Costs","One-time expenses to launch a business: equipment, inventory, legal fees, licenses, marketing materials."),
     ("Business Plan","A formal document detailing business goals, strategies, market analysis, financial projections, and funding needs."),
     ("Fixed vs. Variable Costs","Fixed: don't change with output (rent, insurance). Variable: change with production volume (materials, labor per unit).")],
    [("A sole proprietorship's biggest disadvantage is:",["Complex formation","High taxes","*Unlimited personal liability (personal assets at risk for business debts)","Shared control"],"Liability risk."),
     ("An LLC provides:",["Double taxation","No liability protection","*Limited liability protection with pass-through taxation (profits taxed on personal return)","Unlimited personal liability"],"Best of both worlds."),
     ("A C-Corporation faces 'double taxation' because:",["It pays taxes twice a year","*Corporate profits are taxed at the corporate level, then dividends to shareholders are taxed again on personal returns","It pays state and federal","It files two returns"],"Corporate tax issue."),
     ("An S-Corporation avoids double taxation by:",["Not paying taxes","*Passing income through to shareholders' personal returns (like a partnership)","Only paying state taxes","Filing as sole proprietor"],"Pass-through."),
     ("Typical start-up costs for a small business range from:",["$0","$100","*$5,000 – $50,000+ depending on the business type","$1 million minimum"],"Varies widely."),
     ("A business plan is important because it:",["Is legally required","*Forces you to research the market, plan finances, and serves as the document lenders/investors need","Is optional for all businesses","Only matters for corporations"],"Planning tool."),
     ("Fixed costs include:",["Materials per unit","*Rent, insurance, salaries, loan payments (don't change regardless of production volume)","Shipping per order","Raw materials"],"Constant expenses."),
     ("Variable costs include:",["Rent","Insurance","*Raw materials, packaging, shipping per unit, hourly labor directly tied to production","Lease payments"],"Output-dependent."),
     ("The break-even point is when:",["Profits are maximized","Costs are minimized","*Total revenue = total costs (no profit, no loss — the minimum viable sales volume)","Sales are zero"],"Key threshold."),
     ("An entrepreneur investing $50,000 of personal savings uses _____ financing.",["Debt","*Equity (personal investment — no repayment required but owner bears the risk)","Grant","Crowdfunding"],"Self-financing."),
     ("A bank loan for a business is _____ financing.",["Equity","*Debt (must be repaid with interest regardless of business success)","Self-funding","Crowdfunding"],"Borrowed capital."),
     ("The SBA (Small Business Administration) helps by:",["Running your business","*Guaranteeing loans (reducing bank risk), providing resources, training, and counseling for small businesses","Giving free money","Setting prices"],"Government support."),
     ("A business license is typically required from:",["The federal government only","*Local and/or state government (requirements vary by location and business type)","No one","Only for corporations"],"Legal requirement."),
     ("Working capital is:",["Total assets","*The cash available for day-to-day operations (current assets − current liabilities)","Profit","Revenue"],"Operational funds."),
     ("Most small businesses fail in the first 5 years at a rate of approximately:",["10%","25%","*~50% (emphasizing the importance of financial planning and adequate capitalization)","90%"],"Failure rate."),
     ("An EIN (Employer Identification Number) is:",["Your social security number","*A federal tax ID number for your business (required for hiring employees, opening business accounts)","A state license","An insurance policy"],"Business identifier."),
     ("Franchise businesses have the advantage of:",["Complete independence","*Proven business model, brand recognition, training, and systems — but less creative freedom and ongoing franchise fees","No costs","No rules"],"Franchise model."),
     ("Franchise fees typically range from:",["$100","*$10,000 – $100,000+ (plus ongoing royalties of 4-8% of revenue)","$1 million","Zero"],"Franchise costs."),
     ("The opportunity cost of starting a business includes:",["Only the cash invested","*The salary you forgo from employment, the return you could earn investing the capital elsewhere, and your time","Only rent","Nothing if you succeed"],"Full cost picture."),
     ("For financial math, starting a business applies:",["No math concepts","*Break-even analysis, cost classification, capital budgeting, ROI projections, and risk assessment","Only addition","Only one formula"],"Comprehensive application.")]
)
lessons[k]=v

# 7.2
k,v = build_lesson(7,2,"Profit & Loss Analysis",
    "<h3>Profit &amp; Loss (Income Statement)</h3>"
    "<h4>Key Components</h4>"
    "<ul><li><b>Revenue:</b> Total income from sales.</li>"
    "<li><b>Cost of Goods Sold (COGS):</b> Direct costs of producing what was sold.</li>"
    "<li><b>Gross Profit:</b> Revenue − COGS.</li>"
    "<li><b>Operating Expenses:</b> Rent, utilities, marketing, salaries (not directly tied to production).</li>"
    "<li><b>Net Profit:</b> Revenue − COGS − Operating Expenses − Taxes.</li></ul>",
    [("Revenue","Total income from sales before any expenses are deducted (also called gross sales or top line)."),
     ("COGS (Cost of Goods Sold)","Direct costs of producing the goods/services sold: materials, direct labor, manufacturing overhead."),
     ("Gross Profit","Revenue minus COGS; shows profitability of core product/service before overhead."),
     ("Net Profit (Bottom Line)","Final profit after ALL expenses, including operating costs, interest, and taxes."),
     ("Profit Margin","Net profit ÷ Revenue × 100; shows what percentage of each revenue dollar becomes profit.")],
    [("Revenue is also called:",["Net profit","*Top line (the first line on an income statement)","Bottom line","Gross profit"],"Income statement position."),
     ("A bakery sells $200,000 in goods with $80,000 in COGS. Gross profit =",["$200,000","$80,000","*$120,000 (200000 − 80000)","$280,000"],"Revenue − COGS."),
     ("Gross profit margin for the bakery = ",["40%","80%","*60% (120000 ÷ 200000)","100%"],"Gross margin."),
     ("If operating expenses are $70,000, net profit before taxes =",["$120,000","$70,000","*$50,000 (120000 − 70000)","$200,000"],"After operating expenses."),
     ("Net profit margin = $50,000 ÷ $200,000 =",["50%","30%","*25%","10%"],"Net margin."),
     ("COGS for a service business includes:",["Raw materials","*Direct labor costs and supplies for delivering the service","Building rent","Marketing costs"],"Service COGS."),
     ("A positive net profit means the business:",["Broke even","*Earned more than it spent (profitable)","Lost money","Needs investment"],"Profitability indicator."),
     ("A negative net profit (net loss) means:",["The business is thriving","*Expenses exceeded revenue (the business lost money during the period)","Revenue was zero","Taxes were too high"],"Loss indicator."),
     ("Operating expenses include:",["Direct materials","*Rent, utilities, marketing, administrative salaries, insurance (overhead not directly tied to production)","Raw goods only","Only payroll"],"Overhead costs."),
     ("Depreciation expense represents:",["Cash spent","*The gradual allocation of a long-term asset's cost over its useful life (non-cash expense)","A tax payment","Revenue lost"],"Non-cash expense."),
     ("A business with $400K revenue, 45% gross margin, and $100K operating expenses has net income of approximately:",["$200K","$100K","*$80K (gross profit = $180K − operating expenses $100K = $80K, before taxes)","$300K"],"Multi-step calculation."),
     ("Break-even revenue = total fixed costs ÷ gross margin percentage:",["Revenue × costs","*If fixed costs = $90,000 and gross margin = 60%, break-even revenue = $150,000 (90000 ÷ 0.60)","Costs × margin","Revenue − costs"],"Break-even formula."),
     ("Contribution margin = selling price per unit − variable cost per unit. If price = $50 and variable cost = $30:",["$80","*$20 per unit","$30","$50"],"Unit contribution."),
     ("Units to break even = fixed costs ÷ contribution margin per unit. $90,000 fixed ÷ $20/unit =",["900","2,000","*4,500 units","9,000"],"Unit break-even."),
     ("A profit and loss statement covers:",["A single day only","*A specific time period (month, quarter, year) — shows performance over time","Only one transaction","The company's entire history"],"Time period."),
     ("Comparing P&L statements across periods helps identify:",["Nothing useful","*Trends in revenue growth, cost management, and profitability changes over time","Only taxes","Only COGS"],"Trend analysis."),
     ("A business with declining gross margin should examine:",["Revenue only","*Whether COGS are rising faster than revenue (pricing pressure, supply cost increases)","Only marketing","Only rent"],"Margin diagnosis."),
     ("Operating leverage: a business with high fixed costs and low variable costs will see profits _____ when revenue increases.",["Decrease","Stay flat","*Increase rapidly (each additional sale has low marginal cost, so more drops to profit)","Fluctuate randomly"],"High leverage."),
     ("For a subscription business, COGS is typically:",["Very high","*Relatively low (low marginal cost per subscriber), leading to high gross margins (often 70-90%)","Equal to revenue","Not applicable"],"SaaS economics."),
     ("For financial math, P&L analysis applies:",["No math","*Revenue calculations, margin percentages, break-even analysis, trend analysis, and cost classification","Only addition","Only accounting"],"Business math.")]
)
lessons[k]=v

# 7.3
k,v = build_lesson(7,3,"Break-Even Analysis",
    "<h3>Break-Even Analysis</h3>"
    "<h4>The Break-Even Point</h4>"
    "<p>Break-even (units) = Fixed Costs ÷ (Price per Unit − Variable Cost per Unit)</p>"
    "<p>Break-even (revenue) = Fixed Costs ÷ Contribution Margin Ratio</p>"
    "<h4>Graphical Representation</h4>"
    "<p>Total Revenue line crosses Total Cost line at the break-even point. Below = loss; above = profit.</p>",
    [("Break-Even Point","The sales volume where total revenue = total costs; no profit or loss. The minimum sales needed to survive."),
     ("Contribution Margin","Selling price minus variable cost per unit; the amount each unit 'contributes' toward covering fixed costs."),
     ("Contribution Margin Ratio","Contribution margin ÷ selling price; the percentage of each dollar of revenue available to cover fixed costs."),
     ("Fixed Costs","Costs that remain constant regardless of production volume: rent, insurance, salaries, loan payments."),
     ("Margin of Safety","Current sales minus break-even sales; how much sales can drop before the business loses money.")],
    [("Break-even units = Fixed Costs ÷ (Price − Variable Cost). With $60,000 fixed costs, $40 price, $15 variable cost:",["1,500","3,000","*2,400 (60000 ÷ 25)","4,000"],"BEP calculation."),
     ("Contribution margin per unit with $40 price and $15 variable cost =",["$15","$40","*$25","$55"],"Price − variable cost."),
     ("Contribution margin ratio = $25 ÷ $40 =",["50%","75%","*62.5%","40%"],"CM ratio."),
     ("Break-even revenue = $60,000 ÷ 0.625 =",["$60,000","$80,000","*$96,000","$120,000"],"Revenue BEP."),
     ("If selling 3,000 units (above BEP of 2,400), profit =",["$0","$25,000","*$15,000 (600 units × $25 CM per unit)","$60,000"],"Over BEP profit."),
     ("If fixed costs increase by $10,000, new BEP = $70,000 ÷ $25 =",["2,400","2,600","*2,800 units","3,000"],"Higher fixed costs → higher BEP."),
     ("If variable cost increases $5 (to $20), new CM = $20, new BEP = $60,000 ÷ $20 =",["2,000","2,500","*3,000 units","3,500"],"Higher variable costs → higher BEP."),
     ("Raising price to $50 (CM = $35), new BEP = $60,000 ÷ $35 ≈",["2,000","*~1,714 units","2,500","3,000"],"Higher price → lower BEP."),
     ("Margin of safety (selling 3,000 vs. BEP of 2,400) = ",["2,400 units","3,000 units","*600 units (or $24,000 in revenue, or 20% of current sales)","1,000 units"],"Safety buffer."),
     ("Margin of safety percentage = 600 ÷ 3,000 =",["10%","*20%","25%","30%"],"Safety %."),
     ("On the break-even graph, the area BELOW the BEP represents:",["Profit zone","*Loss zone (total costs exceed total revenue)","Neutral zone","Savings zone"],"Graph reading."),
     ("On the break-even graph, the area ABOVE the BEP represents:",["Loss zone","*Profit zone (total revenue exceeds total costs)","Neutral zone","Cost zone"],"Profit territory."),
     ("A business with high fixed costs has a _____ break-even point.",["Lower","*Higher (more units must be sold just to cover the large fixed costs)","Same","Unpredictable"],"Fixed cost impact."),
     ("DOL (Degree of Operating Leverage) = Contribution Margin ÷ Net Income. High DOL means:",["Stable profits","*Small changes in revenue cause LARGE changes in profit (high risk and high reward)","Low risk","No impact"],"Leverage sensitivity."),
     ("To achieve a TARGET profit of $20,000: units = (Fixed Costs + Target Profit) ÷ CM = ($60K + $20K) ÷ $25 =",["2,400","2,800","*3,200 units","4,000"],"Target profit BEP."),
     ("Multi-product break-even analysis requires:",["Analyzing separately","*Weighted-average contribution margin based on product sales mix (more complex but essential for multi-product businesses)","Ignoring one product","Only revenue data"],"Product mix."),
     ("Sensitivity analysis on break-even asks:",["One question","*'What happens to BEP if price changes 10%? If costs increase? If sales mix shifts?' — testing multiple scenarios","Nothing important","Only about revenue"],"What-if analysis."),
     ("A restaurant with $15,000 monthly fixed costs and $8 CM per meal breaks even at:",["1,000 meals","*1,875 meals/month (15000 ÷ 8)","2,000 meals","2,500 meals"],"Restaurant example."),
     ("Break-even analysis helps entrepreneurs decide:",["Nothing practical","*Whether a business idea is viable, what pricing strategy is needed, and how much volume is required to survive","Only what to sell","Only fixed costs"],"Viability tool."),
     ("For financial math, break-even analysis is foundational because it:",["Is too simple to matter","*Combines fixed/variable cost classification, contribution margin math, and algebraic equations in real business contexts","Only applies to manufacturing","Only applies to startups"],"Core business math.")]
)
lessons[k]=v

# 7.4
k,v = build_lesson(7,4,"Small Business Financing",
    "<h3>Small Business Financing</h3>"
    "<h4>Funding Sources</h4>"
    "<ul><li><b>Bootstrapping:</b> Self-funding from savings, revenue reinvestment.</li>"
    "<li><b>Bank loans:</b> Traditional debt with interest; requires collateral and good credit.</li>"
    "<li><b>SBA loans:</b> Government-backed; easier qualification, favorable terms.</li>"
    "<li><b>Angel investors:</b> Wealthy individuals investing for equity stake.</li>"
    "<li><b>Venture capital:</b> Firms investing large sums for significant equity in high-growth startups.</li>"
    "<li><b>Crowdfunding:</b> Small amounts from many people (Kickstarter, GoFundMe).</li></ul>",
    [("Bootstrapping","Self-funding a business using personal savings and reinvesting early profits; maintains full ownership and control."),
     ("SBA Loan","Small Business Administration-backed loan; government guarantee reduces bank risk, enabling favorable terms for small businesses."),
     ("Angel Investor","Wealthy individual who invests personal money in startups, typically $25,000-$500,000, in exchange for equity and mentorship."),
     ("Venture Capital","Professional investment firms providing $500K-$50M+ to high-growth startups in exchange for significant equity (20-50%+)."),
     ("Equity vs. Debt Financing","Equity: selling ownership shares (no repayment, but diluted control). Debt: borrowing money (repayment required, but you keep 100% ownership).")],
    [("Bootstrapping means funding a business by:",["Borrowing from banks","Selling stock","*Using personal savings and reinvesting business profits (self-funding)","Getting government grants"],"Self-funding."),
     ("The main advantage of bootstrapping is:",["Unlimited capital","*You maintain 100% ownership and control (no debt obligations or investors to answer to)","It's always enough","No risk"],"Full ownership."),
     ("SBA loans offer _____ compared to traditional bank loans.",["Higher interest rates","*Lower interest rates, longer repayment terms, and smaller down payments (government guarantee reduces bank risk)","No documentation","Instant approval"],"SBA advantage."),
     ("Angel investors typically invest:",["$100","*$25,000 – $500,000 (in exchange for equity and often mentorship/advice)","$10 million+","Only to corporations"],"Angel range."),
     ("Venture capital firms typically invest:",["$1,000","Under $25,000","*$500,000 – $50 million+ (in high-growth startups with huge market potential)","Only in real estate"],"VC scale."),
     ("The main downside of equity financing is:",["High interest payments","*Loss of ownership and control (investors get a share of the business and a say in decisions)","Required monthly payments","Simple to repay"],"Dilution."),
     ("The main downside of debt financing is:",["Loss of ownership","*Required repayment with interest regardless of business performance (adds fixed cost burden)","No cost","More shareholders"],"Repayment obligation."),
     ("A $100,000 SBA loan at 7% for 10 years costs approximately _____ per month.",["$500","$800","*~$1,161","$2,000"],"Loan payment."),
     ("Total interest paid on that SBA loan over 10 years ≈",["$7,000","$20,000","*~$39,300 ($1,161 × 120 − $100,000)","$70,000"],"Total interest cost."),
     ("Crowdfunding platforms like Kickstarter work by:",["Giving loans","*Collecting small contributions from many people; often donors receive the product or perks in exchange","Selling stock","Government funding"],"Many small backers."),
     ("The average success rate for Kickstarter campaigns is approximately:",["10%","25%","*~40% (varies by category; technology projects have lower rates)","80%"],"Crowdfunding reality."),
     ("A line of credit differs from a loan because:",["It's always cheaper","*You only pay interest on the amount you actually draw (like a credit card for the business)","It's the same thing","It requires equity"],"Flexible borrowing."),
     ("Factoring (selling receivables) provides:",["A Grant","*Immediate cash by selling unpaid invoices to a 3rd party at a discount (typically 80-90% of invoice value)","A loan","Investment capital"],"Cash flow solution."),
     ("Equipment leasing vs. buying: leasing advantages include:",["Ownership","*Lower upfront cost, tax deductions, and ability to upgrade — but higher total cost over time vs. buying","No payments","Building equity"],"Lease benefits."),
     ("The cost of equity (giving up 20% ownership) on a business worth $500K =",["$0","$20,000","*$100,000 (20% of $500,000 in value — and this grows as the business grows)","$500,000"],"Equity cost."),
     ("If that business grows to $5M, the 20% stake given up is now worth:",["$100,000","$500,000","*$1,000,000","$5,000,000"],"Dilution cost over time."),
     ("A business applying for a bank loan typically needs:",["Nothing","*A business plan, financial statements, collateral, good personal credit, and sometimes a personal guarantee","Only a request","Just good credit"],"Loan requirements."),
     ("Personal guarantee on a business loan means:",["The bank pays if you default","*The owner is personally responsible for repayment if the business can't pay (even with an LLC)","No risk to owner","The business guarantees itself"],"Personal risk."),
     ("The best financing strategy often combines:",["Only one source","*Multiple sources: bootstrapping + bank loan + possibly grants or angel investment (diversified funding)","Only equity","Only debt"],"Mixed approach."),
     ("For financial math, business financing involves:",["No calculations","*Loan amortization, interest cost comparison, equity dilution analysis, ROI on invested capital, and cost of capital","Only interest rates","Only one formula"],"Comprehensive finance math.")]
)
lessons[k]=v

# 7.5
k,v = build_lesson(7,5,"Entrepreneurship Case Studies",
    "<h3>Entrepreneurship Case Studies</h3>"
    "<h4>Case 1: Food Truck Startup</h4>"
    "<p>Start-up: $85,000 (truck $50K, equipment $20K, licenses/permits $5K, initial inventory $10K)."
    " Monthly fixed costs: $3,000 (parking fees, insurance, loan payment). Variable cost: $4/meal. "
    "Selling price: $12/meal. CM: $8/meal. BEP: 375 meals/month.</p>"
    "<h4>Case 2: Online Store</h4>"
    "<p>Start-up: $5,000 (website, initial inventory). Fixed: $500/month. Variable: 40% of revenue. "
    "CM ratio: 60%. BEP revenue: $833/month.</p>",
    [("Food Truck Economics","Typical startup $50-150K; lower overhead than restaurant; BEP often 300-500 meals/month depending on pricing and costs."),
     ("E-Commerce Economics","Low startup ($1-10K); very low fixed costs; variable costs include product COGS + shipping + platform fees."),
     ("Cash Flow vs. Profit","Cash flow = actual money moving in/out. Profit = accounting measure. A business can be profitable but cash-poor (or vice versa)."),
     ("Return on Investment (ROI)","(Net Profit ÷ Total Investment) × 100; measures how effectively invested capital generates profit."),
     ("Payback Period","Time to recover initial investment from profits; shorter = faster return of capital to the investor.")],
    [("Food truck BEP: $3,000 fixed ÷ $8 CM per meal =",["200","300","*375 meals/month","500"],"BEP calculation."),
     ("If the food truck sells 500 meals/month, monthly profit =",["$3,000","$2,000","*$1,000 ((500-375) × $8 = $1,000)","$500"],"Above BEP profit."),
     ("Annual profit at 500 meals/month =",["$6,000","$8,000","*$12,000 ($1,000 × 12)","$15,000"],"Annual projection."),
     ("ROI on $85,000 food truck investment with $12,000 annual profit =",["20%","18%","*~14.1% ($12,000 ÷ $85,000)","10%"],"ROI calculation."),
     ("Payback period = $85,000 ÷ $12,000/year ≈",["3 years","5 years","*~7.1 years","10 years"],"Recovery time."),
     ("Online store BEP revenue: $500 ÷ 0.60 =",["$500","$600","*~$833/month","$1,000"],"E-commerce BEP."),
     ("If the online store earns $3,000/month revenue, monthly profit =",["$833","$1,500","*$1,300 (($3,000 × 0.60) − $500 = $1,800 − $500)","$2,500"],"Note: corrected in quiz explanation."),
     ("Online store ROI: $1,300/month × 12 = $15,600/year on $5,000 investment =",["50%","100%","200%","*312% (15600 ÷ 5000)"],"High ROI, low investment."),
     ("The food truck has _____ startup costs but _____ ROI compared to the online store.",["Lower, higher","*Higher startup costs but lower ROI (percentage-wise)","Same, same","Lower, lower"],"Comparison."),
     ("Cash flow problems in a food truck might include:",["Too many customers","*Seasonality (slow winter months), unexpected repairs, and payment timing gaps","Never","Only in the first week"],"Cash flow challenges."),
     ("A food truck selling 600 meals/month needs to evaluate whether to:",["Close","*Hire help (increased labor cost but capacity to serve more customers — is the marginal revenue > marginal cost?)","Lower prices","Increase fixed costs"],"Growth decision."),
     ("Scaling the online store from $3K to $10K/month revenue primarily requires:",["A new building","*Marketing investment, inventory management, and possibly additional staff — variable costs scale proportionally","$100K investment","Physical location"],"E-commerce scaling."),
     ("A subscription-based online business has the advantage of:",["One-time sales","*Recurring predictable revenue (monthly), higher lifetime customer value, and easier cash flow forecasting","High COGS","Low margins"],"Subscription model."),
     ("Customer Acquisition Cost (CAC) = marketing spend ÷ new customers. $2,000 spent / 50 customers =",["$10","$20","*$40 per customer","$100"],"CAC calculation."),
     ("If average customer lifetime value (LTV) is $200 and CAC is $40, the LTV:CAC ratio =",["2:1","3:1","*5:1 (healthy — generally want 3:1 or higher)","10:1"],"LTV:CAC."),
     ("A business should expand if the marginal unit's:",["Price is low","*Marginal revenue exceeds marginal cost (each additional unit sold adds more to revenue than to cost)","Volume is high","Fixed costs increase"],"Expansion criterion."),
     ("Seasonality can be managed by:",["Closing in slow months","*Diversifying products, building cash reserves during peak months, and adjusting expenses","Ignoring it","Only raising prices"],"Seasonal strategies."),
     ("The food truck's variable cost increase from $4 to $5/meal (new CM = $7) changes BEP to:",["375","400","*~429 meals/month ($3,000 ÷ $7)","500"],"Cost sensitivity."),
     ("Both case studies demonstrate that entrepreneurship requires:",["Luck only","*Careful financial analysis: BEP, ROI, cash flow management, and continuous cost monitoring","Only passion","Only a good product"],"Math-driven decisions."),
     ("For financial math, case studies apply:",["Theory only","*BEP, ROI, payback period, cash flow, CAC/LTV, and profitability analysis to realistic scenarios","One formula","No calculation"],"Integrated analysis.")]
)
lessons[k]=v

# 7.6
k,v = build_lesson(7,6,"Marketing & Finance",
    "<h3>Marketing &amp; Finance</h3>"
    "<h4>Marketing Budget & ROI</h4>"
    "<p>Marketing budget is typically 5-10% of revenue for established businesses, 15-20% for startups.</p>"
    "<h4>Key Marketing Metrics</h4>"
    "<ul><li><b>CAC:</b> Customer Acquisition Cost = Marketing Spend ÷ New Customers.</li>"
    "<li><b>LTV:</b> Customer Lifetime Value = Avg Purchase × Frequency × Customer Lifespan.</li>"
    "<li><b>ROAS:</b> Return on Ad Spend = Revenue from Ads ÷ Cost of Ads.</li>"
    "<li><b>Conversion Rate:</b> Purchasers ÷ Visitors × 100.</li></ul>",
    [("CAC (Customer Acquisition Cost)","Total marketing spend ÷ number of new customers acquired; how much it costs to gain one customer."),
     ("LTV (Customer Lifetime Value)","Total revenue expected from a customer over the entire relationship; LTV should be ≥ 3× CAC for a healthy business."),
     ("ROAS (Return on Ad Spend)","Revenue generated ÷ advertising cost; a ROAS of 4:1 means $4 revenue per $1 spent on ads."),
     ("Conversion Rate","Percentage of visitors/leads who complete a desired action (purchase, sign-up); typically 2-5% for e-commerce."),
     ("Marketing ROI","(Revenue from Marketing − Marketing Cost) ÷ Marketing Cost × 100; measures overall marketing effectiveness.")],
    [("A startup spending $5,000/month on marketing to acquire 100 customers has a CAC of:",["$100","*$50","$500","$25"],"5000 ÷ 100."),
     ("If each customer spends $30/month for an average of 12 months, LTV =",["$30","$120","*$360 (30 × 12)","$600"],"LTV calculation."),
     ("LTV:CAC ratio = $360:$50 =",["2:1","5:1","*7.2:1 (excellent — well above the 3:1 minimum)","10:1"],"Healthy ratio."),
     ("A Google Ads campaign: $2,000 spent generates $10,000 revenue. ROAS =",["2:1","3:1","*5:1 ($10,000 ÷ $2,000 — every $1 in ads generates $5 in revenue)","10:1"],"ROAS calculation."),
     ("A website with 10,000 visitors and 250 purchases has a conversion rate of:",["1%","*2.5%","5%","10%"],"250 ÷ 10000 × 100."),
     ("To increase revenue, a business can optimize:",["Only prices","*Conversion rate (more buyers from same traffic), average order value, and customer retention — all cheaper than acquiring new customers","Only marketing spend","Only products"],"Growth levers."),
     ("Increasing conversion rate from 2.5% to 3.5% on 10,000 visitors adds _____ more customers.",["50","*100 (350 − 250)","200","500"],"Conversion impact."),
     ("Email marketing typically has the highest ROI of any channel at approximately:",["$5 per $1","$10 per $1","$20 per $1","*$36-40 per $1 spent (extremely high because the audience is already engaged)"],"Email ROI."),
     ("Social media marketing is most effective for:",["Direct sales only","*Brand awareness, community building, and customer engagement (conversion to sales often requires additional steps)","Nothing","Only large companies"],"Social media role."),
     ("A/B testing in marketing compares:",["Two companies","*Two versions of an ad, email, or webpage to determine which performs better (data-driven optimization)","Two products","Two prices"],"Split testing."),
     ("The marketing funnel stages are:",["Awareness only","*Awareness → Interest → Consideration → Conversion → Retention (guiding prospects to become loyal customers)","Only conversion","Only retention"],"Full funnel."),
     ("Retention marketing costs _____ as much as acquisition marketing.",["The same","*1/5 to 1/7 (retaining existing customers is 5-7× cheaper than acquiring new ones)","More","Double"],"Retention advantage."),
     ("Increasing customer retention by 5% can increase profits by:",["5%","10%","*25-95% (existing customers buy more often and refer others)","1%"],"Retention power."),
     ("Price elasticity measures:",["How flexible prices are","*How much demand changes when price changes (elastic: demand drops significantly; inelastic: demand barely changes)","Customer satisfaction","Product quality"],"Demand sensitivity."),
     ("A product with inelastic demand can:",["Never change price","*Increase price without losing many customers (necessities, unique products, strong brands)","Only decrease price","Change price freely"],"Pricing power."),
     ("Break-even on a marketing campaign: $3,000 spend needs to generate how much revenue at 30% margin?",["$3,000","$6,000","*$10,000 ($3,000 ÷ 0.30 — because each dollar of revenue only contributes $0.30 to cover the marketing cost)","$30,000"],"Marketing BEP."),
     ("Churn rate is:",["New customer rate","*Percentage of customers who stop buying in a given period (monthly/annually)","Revenue growth","Profit margin"],"Customer loss."),
     ("Reducing churn from 5% to 3% monthly on 1,000 customers saves _____ customers/month.",["10","*20","30","50"],"Churn reduction."),
     ("Marketing attribution determines:",["Who created the ad","*Which marketing channels (social, email, search, etc.) actually drove the conversion — critical for allocating budget","The total budget","Customer names"],"Channel effectiveness."),
     ("For financial math, marketing finance applies:",["No calculations","*CAC, LTV, ROAS, conversion rates, elasticity, and ROI — all percentage and ratio-based financial metrics","Only creativity","Only art"],"Quantitative marketing.")]
)
lessons[k]=v

# 7.7
k,v = build_lesson(7,7,"Business Risk Management",
    "<h3>Business Risk Management</h3>"
    "<h4>Types of Business Risk</h4>"
    "<ul><li><b>Market risk:</b> Demand changes, competition, economic downturns.</li>"
    "<li><b>Financial risk:</b> Cash flow problems, excessive debt, interest rate changes.</li>"
    "<li><b>Operational risk:</b> Supply chain disruptions, equipment failure, employee issues.</li>"
    "<li><b>Legal/Regulatory risk:</b> Lawsuits, regulation changes, compliance failures.</li></ul>",
    [("Market Risk","Risk from changing customer demand, new competitors, or economic conditions affecting sales."),
     ("Financial Risk","Risk from cash flow shortfalls, overleveraging (too much debt), or interest rate increases."),
     ("Operational Risk","Risk from internal processes: supply chain disruption, equipment failure, key employee departure."),
     ("Diversification (Business)","Spreading risk across multiple products, markets, or revenue streams to reduce dependence on any single source."),
     ("Business Insurance","Policies protecting against specific risks: liability, property, workers' comp, business interruption, cyber liability.")],
    [("Market risk includes:",["Only supply issues","*Demand changes, new competitors, economic downturns, and shifting consumer preferences","Only financial problems","Only legal issues"],"External market factors."),
     ("A business with one product and one customer has _____ risk.",["Low","Moderate","*Very high (single point of failure; loss of that customer or product = total revenue loss)","No"],"Concentration risk."),
     ("Diversification reduces risk by:",["Eliminating all risk","*Spreading revenue across multiple products/markets so one failure doesn't destroy the business","Increasing costs","Reducing revenue"],"Risk spreading."),
     ("Cash flow risk can be managed by:",["Spending more","*Maintaining cash reserves (3-6 months operating expenses), diversifying revenue, and monitoring receivables","Ignoring it","Only increasing sales"],"Cash management."),
     ("Excessive debt (overleveraging) is dangerous because:",["Debt is free","*Fixed debt payments must be made regardless of revenue — a sales downturn can cause default and bankruptcy","Debt builds wealth always","Interest rates never change"],"Leverage danger."),
     ("The debt-to-equity ratio measures:",["Revenue","Profit","*How much of the business is financed by debt vs. owner investment (high ratio = more financial risk)","Cash flow"],"Leverage metric."),
     ("A business with $200,000 debt and $100,000 equity has a debt-to-equity ratio of:",["0.5","1.0","*2.0 (200000 ÷ 100000 — relatively high leverage)","3.0"],"D/E calculation."),
     ("Business interruption insurance covers:",["Product defects","*Lost income and operating expenses when a covered event (fire, natural disaster) forces temporary closure","Employee injuries","Lawsuits only"],"Income protection."),
     ("Cyber liability insurance covers:",["Physical damage","Equipment breakdown","*Data breaches, hacking incidents, ransomware attacks, and customer data compromises","Vehicle accidents"],"Digital risk."),
     ("Workers' compensation insurance is _____ in most states.",["Optional","*Legally required (covers employee injuries/illness occurring during work)","Only for large companies","Free"],"Legal requirement."),
     ("Key person insurance protects a business if:",["Equipment breaks","*A critical employee (founder, top salesperson, key engineer) dies or becomes disabled","Rent increases","Customers leave"],"People risk."),
     ("Supply chain risk can be mitigated by:",["Using one supplier","*Using multiple suppliers, maintaining safety stock, and having backup sourcing plans","Reducing inventory to zero","Ignoring supply issues"],"Supply resilience."),
     ("A SWOT analysis examines:",["Only strengths","*Strengths, Weaknesses, Opportunities, and Threats — internal and external factors affecting the business","Only financial data","Only competitors"],"Strategic framework."),
     ("Scenario planning involves:",["Predicting the future exactly","*Creating multiple 'what if' scenarios (best case, worst case, most likely) to prepare for various outcomes","Only optimistic projections","Ignoring risks"],"Preparedness."),
     ("An emergency fund for a business should cover:",["1 week","1 month","*3-6 months of operating expenses (protects against temporary revenue disruptions)","1 year"],"Business reserves."),
     ("Professional liability (errors & omissions) insurance protects:",["Against fire","*Against claims that your professional service/advice caused financial harm to a client","Against theft","Against employee lawsuits"],"Professional risk."),
     ("The biggest risk to small businesses is often:",["Competition","Natural disasters","*Cash flow problems (running out of money before becoming profitable or during slow periods)","Too many employees"],"Cash is king."),
     ("Risk monitoring involves:",["Checking once, then forgetting","*Ongoing assessment: tracking KPIs, reviewing financial statements monthly, and updating risk plans regularly","Only annual reviews","No effort"],"Continuous process."),
     ("Business continuity planning ensures:",["No disruptions ever","*The business can continue operating (or recover quickly) after a disaster, cyberattack, or major disruption","Perfect operations","Zero risk"],"Recovery planning."),
     ("For financial math, business risk management uses:",["No quantitative tools","*Ratio analysis (D/E, current ratio), insurance cost-benefit, cash flow forecasting, and scenario modeling","Only qualitatives","Only gut feelings"],"Quantitative risk assessment.")]
)
lessons[k]=v

# 7.8
k,v = build_lesson(7,8,"Technology in Business Finance",
    "<h3>Technology in Business Finance</h3>"
    "<h4>Essential Business Finance Tools</h4>"
    "<ul><li><b>Accounting software:</b> QuickBooks, Xero, FreshBooks — automate bookkeeping.</li>"
    "<li><b>Payment processing:</b> Square, Stripe, PayPal — accept digital payments.</li>"
    "<li><b>Payroll services:</b> Gusto, ADP — automate payroll taxes and compliance.</li>"
    "<li><b>Spreadsheet modeling:</b> Excel/Google Sheets for financial projections and analysis.</li></ul>",
    [("QuickBooks","Leading small business accounting software; tracks income, expenses, invoicing, and generates financial reports automatically."),
     ("Payment Processing Fee","Typically 2.6-2.9% + $0.30 per transaction for credit card processing (Square, Stripe); a cost of doing business."),
     ("Financial Dashboard","Real-time visual display of key financial metrics (revenue, expenses, cash flow, profit) for quick business health assessment."),
     ("Cloud Accounting","Online-based accounting systems accessible from anywhere; automatic backups, real-time collaboration, and bank feed integration."),
     ("Fintech","Financial technology — innovations like digital payments, automated lending, blockchain, and AI-driven financial tools.")],
    [("QuickBooks and Xero are primarily used for:",["Marketing","*Business accounting: tracking income, expenses, invoicing, and financial reporting","Social media","Customer service"],"Accounting automation."),
     ("Credit card processing fees (Square, Stripe) are typically:",["0.5%","1%","*2.6-2.9% + $0.30 per transaction","5%"],"Transaction cost."),
     ("On a $100 transaction at 2.9% + $0.30, the processing fee is:",["$2.90","$3.00","*$3.20 (100 × 0.029 + 0.30)","$4.00"],"Fee calculation."),
     ("On 1,000 transactions averaging $50/month, monthly processing fees ≈",["$500","$1,000","*~$1,750 (1000 × ($50 × 0.029 + $0.30) = 1000 × $1.75)","$2,500"],"Monthly fee impact."),
     ("Payroll services automate:",["Only paychecks","*Calculating wages, withholding taxes, filing payroll tax returns, issuing paychecks/direct deposits, and year-end W-2s","Only hiring","Only scheduling"],"Payroll automation."),
     ("Payroll tax errors can result in:",["Nothing","*IRS penalties, interest charges, and potential legal issues (payroll compliance is strictly enforced)","Only warnings","Just refiling"],"Compliance risk."),
     ("Cloud accounting advantages include:",["Only cost savings","*Access from anywhere, automatic bank feeds, real-time collaboration, automatic backups, and integrated apps","Only local access","Only for large businesses"],"Cloud benefits."),
     ("A financial dashboard shows:",["Only revenue","*Key metrics at a glance: revenue, expenses, profit, cash flow, accounts receivable/payable — real-time business health","Only expenses","Only one number"],"Visual management."),
     ("Point-of-sale (POS) systems like Square provide:",["Only payments","*Payment processing + inventory tracking + sales analytics + receipt generation + customer data","Only receipts","Only inventory"],"Integrated POS."),
     ("Automated invoicing saves time by:",["Doing nothing","*Generating, sending, tracking, and following up on invoices automatically — reducing human error and speeding collections","Only printing invoices","Only tracking payments"],"AR automation."),
     ("Expense tracking apps categorize spending by:",["Doing nothing","*Automatically categorizing transactions, scanning receipts, and generating reports for tax preparation","Only one category","Only cash"],"Expense management."),
     ("Financial projections in Excel use _____ to model scenarios.",["Only SUM","*Formulas, charts, pivot tables, what-if analysis, Goal Seek, and Solver for complex financial modeling","Only graphs","Only text"],"Spreadsheet power."),
     ("The NPV function in Excel calculates:",["Simple interest","*Net Present Value of a series of future cash flows discounted to present — key for investment decisions","Compound interest","Only revenue"],"Excel NPV."),
     ("The PMT function in Excel calculates:",["Total cost","*Periodic loan payment based on interest rate, number of periods, and loan amount","Only interest","Only principal"],"Excel PMT."),
     ("Blockchain technology in business finance enables:",["Nothing yet","*Transparent, tamper-proof transaction records, smart contracts, and cryptocurrency payments","Only Bitcoin","Only mining"],"Blockchain applications."),
     ("AI in business finance helps with:",["Nothing","*Fraud detection, cash flow forecasting, automated bookkeeping, credit scoring, and financial pattern recognition","Only chatbots","Only marketing"],"AI finance applications."),
     ("Integration between accounting and banking software:",["Doesn't exist","*Automatically imports bank transactions into accounting records, reducing manual data entry and errors","Only exports data","Only works for large banks"],"Bank feed integration."),
     ("The cost of accounting software for small businesses is typically:",["$500/month","*$25-75/month (very affordable relative to the time saved and accuracy gained)","$1,000/month","Free always"],"Affordable tools."),
     ("Technology reduces business finance errors by:",["0%","*80-90% (automated calculations, bank reconciliation, and built-in error checks dramatically reduce mistakes)","10%","50%"],"Error reduction."),
     ("For financial math, business technology tools:",["Replace all learning","*Apply course concepts (NPV, PMT, break-even, projections) through software that professionals actually use daily","Are unnecessary","Only matter for CPAs"],"Real-world application.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 7: wrote {len(lessons)} lessons")
