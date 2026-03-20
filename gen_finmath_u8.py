#!/usr/bin/env python3
"""Financial Math Unit 8 – Stock Market & Trading (8 lessons)."""
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

# 8.1
k,v = build_lesson(8,1,"Stock Market Basics",
    "<h3>Stock Market Basics</h3>"
    "<h4>What Is a Stock?</h4>"
    "<p>A stock represents fractional <b>ownership</b> of a company. Shareholders earn returns through price appreciation and dividends.</p>"
    "<h4>Major Exchanges</h4>"
    "<ul><li><b>NYSE:</b> New York Stock Exchange — largest by market capitalization.</li>"
    "<li><b>NASDAQ:</b> Technology-heavy electronic exchange.</li>"
    "<li><b>Market capitalization</b> = Share Price × Shares Outstanding.</li></ul>",
    [("Stock (Equity)","A share of ownership in a company; entitles the holder to a portion of profits (dividends) and voting rights."),
     ("Market Capitalization","Share price × total shares outstanding; classifies companies as large-cap (>$10B), mid-cap, or small-cap (<$2B)."),
     ("Dividend","A portion of company profits distributed to shareholders, usually quarterly; expressed as yield (annual dividend ÷ price)."),
     ("Bull Market","Period of rising stock prices (generally 20%+ sustained increase); associated with economic optimism."),
     ("Bear Market","Period of falling stock prices (20%+ decline from recent highs); associated with recession fears.")],
    [("A stock represents:",["A loan to a company","A guaranteed return","*Ownership (equity) in a company","A bond"],"Equity ownership."),
     ("Market capitalization of a company with 50 million shares at $80/share =",["$50 million","$80 million","*$4 billion","$400 million"],"50M × $80."),
     ("A large-cap stock has a market cap of:",["Under $2 billion","$2-10 billion","*Over $10 billion","Under $500 million"],"Large-cap threshold."),
     ("The NYSE is the world's largest exchange by:",["Number of companies listed","Age","*Market capitalization (total value of all listed companies)","Physical size"],"Exchange ranking."),
     ("NASDAQ is known for listing many:",["Banks only","*Technology companies (Apple, Microsoft, Google, Amazon, etc.)","Only small companies","Only foreign companies"],"Tech-heavy exchange."),
     ("A dividend yield of 3% on a $100 stock means annual dividends of:",["$100","$30","*$3 per share","$0.30"],"100 × 0.03."),
     ("A bull market is characterized by:",["Falling prices","Flat prices","*Rising prices (generally 20%+ sustained increase) with investor optimism","Extreme volatility"],"Upward trend."),
     ("A bear market occurs when prices fall:",["5%","10%","*20% or more from recent highs","50% exactly"],"Bear market threshold."),
     ("An IPO (Initial Public Offering) is when:",["A company goes bankrupt","*A private company sells shares to the public for the first time on a stock exchange","A company goes private","A stock splits"],"Going public."),
     ("Stock exchanges match:",["Lenders and borrowers","*Buyers and sellers of stocks (facilitating price discovery and trade execution)","Only large institutions","Only governments"],"Matching engine."),
     ("The S&P 500 tracks:",["All US stocks","50 stocks","*500 large US companies (a widely used benchmark for the overall US stock market)","Global stocks"],"Key index."),
     ("Buying 100 shares at $50/share requires an investment of:",["$50","$500","*$5,000","$50,000"],"100 × $50."),
     ("If the stock rises to $60, the gain is:",["$50","$500","*$1,000 (100 × ($60-$50))","$6,000"],"Return calculation."),
     ("Return on investment = $1,000 ÷ $5,000 =",["10%","15%","*20%","25%"],"ROI."),
     ("Broker commissions have dropped because:",["Regulations require it","*Competition and technology led most major brokers to offer $0 commission trades","Every broker charges the same","Brokers don't exist"],"Fee revolution."),
     ("A stock split (2-for-1) means:",["You lose half your shares","*Each share becomes 2 shares at half the price (total value unchanged; more affordable per share)","The stock doubled","The company split"],"Split mechanics."),
     ("Market orders execute:",["Only at a specific price","*Immediately at the current market price (fastest but price not guaranteed)","Never","Only after hours"],"Immediate execution."),
     ("Limit orders execute:",["Immediately at any price","*Only at your specified price or better (control over price but may not execute)","Never","Only on weekends"],"Price control."),
     ("The stock market has historically returned approximately _____ per year (long-term average, S&P 500).",["3%","5%","*~10% (~7% after inflation)","15%"],"Historical average."),
     ("For financial math, the stock market applies:",["No math","*Percentage returns, market cap calculations, dividend yields, and compound growth — core financial concepts","Only addition","Only for professionals"],"Market math.")]
)
lessons[k]=v

# 8.2
k,v = build_lesson(8,2,"Reading Financial Tables",
    "<h3>Reading Financial Tables &amp; Statements</h3>"
    "<h4>Stock Quote Components</h4>"
    "<ul><li><b>Ticker:</b> Abbreviated symbol (AAPL, MSFT).</li>"
    "<li><b>Open/Close:</b> Price at market open/close.</li>"
    "<li><b>High/Low:</b> Highest/lowest price during the trading day.</li>"
    "<li><b>Volume:</b> Number of shares traded.</li>"
    "<li><b>P/E Ratio:</b> Price ÷ Earnings Per Share — valuation metric.</li></ul>",
    [("Ticker Symbol","Short identifier for a publicly traded company (e.g., AAPL = Apple, MSFT = Microsoft, GOOGL = Alphabet)."),
     ("P/E Ratio","Price-to-Earnings ratio; stock price ÷ earnings per share. Higher P/E suggests higher growth expectations."),
     ("EPS (Earnings Per Share)","Net income ÷ shares outstanding; fundamental measure of company profitability on a per-share basis."),
     ("Volume","Number of shares traded in a given period; high volume = high interest/liquidity."),
     ("52-Week High/Low","Highest and lowest prices over the past year; provides context for current price level.")],
    [("A stock's ticker symbol is:",["Its full company name","*A short abbreviated identifier used on exchanges (e.g., AAPL for Apple)","A secret code","Its market cap"],"Quick identification."),
     ("If a stock opens at $150 and closes at $155, the day's change is:",["$150","*+$5 (+3.33%)","$155","-$5"],"Price change."),
     ("Volume of 10 million shares means:",["The stock is worth $10M","*10 million shares were bought/sold during that trading session","Only 10 million shares exist","The price moved $10M"],"Trading activity."),
     ("High volume with rising prices generally indicates:",["Weakness","*Strong buying interest and bullish sentiment","Selling pressure","Nothing"],"Volume analysis."),
     ("P/E ratio = Price $200 ÷ EPS $8 =",["$200","$8","*25 (investors pay $25 for every $1 of earnings)","16"],"P/E calculation."),
     ("A P/E of 25 vs. industry average of 15 suggests:",["The stock is undervalued","*The stock is relatively expensive (market expects higher growth than the industry average)","They're equal","The stock is worthless"],"Relative valuation."),
     ("EPS = Net income $500M ÷ 100M shares =",["$100","*$5.00 per share","$500","$0.50"],"EPS calculation."),
     ("A stock at $100 with EPS of $5 has a P/E of:",["$100","$5","*20","$500"],"P/E from data."),
     ("The 52-week high/low provides context for:",["Future prices","*Where the current price sits relative to its past year range (near highs vs. lows)","Dividend amounts","Volume levels"],"Price range context."),
     ("Day range: $148.50-$152.30 means:",["The stock split","*The lowest trade was $148.50 and highest was $152.30 during that session","Average was $148.50","Volume was 152.30"],"Intraday range."),
     ("Market cap on a quote page is calculated as:",["Revenue × profit","*Current price × total shares outstanding","Book value × shares","Only by the exchange"],"Real-time market cap."),
     ("Dividend yield = Annual dividends per share ÷ current stock price. $3.20 dividend ÷ $80 price =",["3.20%","*4.0%","$3.20","2.0%"],"Yield calculation."),
     ("PEG ratio = P/E ÷ earnings growth rate. P/E of 25 with 20% growth = PEG of:",["20","25","*1.25 (PEG < 1 is considered undervalued; > 1 may be overvalued relative to growth)","0.8"],"Growth-adjusted valuation."),
     ("Price-to-Book (P/B) ratio compares stock price to:",["Earnings","Revenue","*Book value per share (total assets minus liabilities ÷ shares outstanding)","Cash flow"],"Asset-based valuation."),
     ("A stock trading below book value (P/B < 1) may be:",["Always a buy","*Potentially undervalued (but could also indicate underlying problems — requires further analysis)","Always overvalued","Worthless"],"Value indicator."),
     ("Analyst ratings of 'Buy,' 'Hold,' 'Sell' are:",["Guaranteed outcomes","*Opinions based on analysis — not guarantees; always do your own research","Legal requirements","Always correct"],"Rating caveat."),
     ("An income statement shows:",["Only revenue","*Revenue, expenses, and net income over a period (profitability report)","Only assets","Only cash flow"],"Financial statement."),
     ("A balance sheet shows:",["Only profit","Only revenue","*Assets, liabilities, and equity at a point in time (financial position snapshot)","Only expenses"],"Snapshot of health."),
     ("Reading financial tables requires understanding:",["Only one number","*Multiple interconnected metrics: price, volume, P/E, EPS, yield, market cap, and how they relate","Only the price","Only the name"],"Multi-metric literacy."),
     ("For financial math, financial literacy includes:",["Memorizing stock prices","*Interpreting ratios, percentages, and financial statements to make informed investment decisions","Only buying stocks","Only selling stocks"],"Data-driven decisions.")]
)
lessons[k]=v

# 8.3
k,v = build_lesson(8,3,"Market Indices & Benchmarks",
    "<h3>Market Indices &amp; Benchmarks</h3>"
    "<h4>Major US Indices</h4>"
    "<ul><li><b>S&P 500:</b> 500 large US companies — the most-used US market benchmark.</li>"
    "<li><b>Dow Jones (DJIA):</b> 30 large industrial companies — price-weighted.</li>"
    "<li><b>NASDAQ Composite:</b> All NASDAQ-listed stocks — tech-heavy.</li>"
    "<li><b>Russell 2000:</b> 2,000 small-cap companies.</li></ul>"
    "<h4>Index Weighting</h4>"
    "<p>Market-cap weighted (S&P 500): larger companies have more influence. Price-weighted (DJIA): higher-priced stocks have more influence.</p>",
    [("S&P 500","Index of 500 large US companies weighted by market cap; covers ~80% of US stock market value; primary benchmark."),
     ("Dow Jones Industrial Average","Index of 30 large US companies weighted by stock price; oldest widely followed US index (since 1896)."),
     ("Index Fund","A fund that passively tracks an index (like S&P 500); low fees because no active stock picking is needed."),
     ("Benchmark","A standard for measuring investment performance (e.g., 'My fund returned 12% vs. S&P 500's 10%')."),
     ("Market-Cap Weighting","Index weighting method where larger companies (higher market cap) have proportionally greater influence on the index.")],
    [("The S&P 500 represents approximately _____ of the total US stock market value.",["50%","60%","*~80%","100%"],"Market coverage."),
     ("The Dow Jones tracks _____ companies and is _____ weighted.",["500, market-cap","*30, price-weighted","2000, equal","100, market-cap"],"DJIA structure."),
     ("In a price-weighted index, a stock at $300 has _____ influence than a stock at $50.",["Less","Equal","*More (price-weighted means higher-priced stocks move the index more, regardless of company size)","No"],"Price weighting."),
     ("In a market-cap weighted index (S&P 500), Apple at $3T market cap has _____ influence than a $30B company.",["Less","Equal","*Much more (100× larger market cap = 100× more influence on the index)","No"],"Cap weighting."),
     ("The NASDAQ Composite is heavily weighted toward:",["Banks","Energy","*Technology companies","Utilities"],"Tech dominance."),
     ("The Russell 2000 tracks:",["Large-cap stocks","*Small-cap stocks (the 2,000 smallest companies in the Russell 3000)","International stocks","Bonds"],"Small-cap index."),
     ("An index fund that tracks the S&P 500 holds:",["One stock","*~500 stocks in proportions matching the index (passive replication)","Only 30 stocks","Only tech stocks"],"Passive investing."),
     ("Index fund expense ratios are typically:",["1-2%","*0.03-0.20% (very low because no active management or stock picking is needed)","0.5-1%","2-3%"],"Low-cost investing."),
     ("Actively managed funds charge _____ than index funds.",["Less","The same","*More (typically 0.5-1.5% — they need to pay fund managers and research teams)","Nothing"],"Active vs. passive cost."),
     ("Over 20 years, approximately _____ of actively managed funds underperform their benchmark index.",["10%","30%","50%","*80-90% (this is why index investing has become so popular)"],"Active underperformance."),
     ("If the S&P 500 returns 10% and your fund returns 8%, the fund _____ the benchmark.",["Outperformed","Matched","*Underperformed by 2 percentage points","Can't be compared"],"Benchmark comparison."),
     ("Total Stock Market indices (like VTI) include:",["Only large caps","Only S&P 500","*Large, mid, small, and micro-cap stocks — the entire US stock market","Only international"],"Full market exposure."),
     ("International indices include:",["Only US stocks","*MSCI EAFE (developed international), MSCI Emerging Markets, and others tracking non-US stocks","Only bonds","Only commodities"],"Global diversification."),
     ("The Dow going from 30,000 to 33,000 represents a gain of:",["$3,000","3,000 points","*10% (3000 ÷ 30000 × 100)","33%"],"Percentage return."),
     ("Historical S&P 500 average annual return (1926-present) is approximately:",["5%","*~10% (nominal) or ~7% after inflation","15%","20%"],"Long-term average."),
     ("Dollar cost averaging into an S&P 500 index fund means:",["Buying once","*Investing a fixed dollar amount at regular intervals (buying more shares when prices are low, fewer when high)","Timing the market","Only buying dips"],"Systematic investing."),
     ("The volatility of the Russell 2000 (small-cap) is typically _____ than the S&P 500.",["Lower","The same","*Higher (small-cap stocks are more volatile but have historically provided higher long-term returns)","Much lower"],"Small-cap volatility."),
     ("Bond indices (like Bloomberg Aggregate) track:",["Stocks","*The bond market: government, corporate, and mortgage-backed bonds (used as a fixed-income benchmark)","Only treasuries","Only corporate bonds"],"Bond benchmark."),
     ("A balanced portfolio might use _____ as its benchmark.",["Only S&P 500","*A blended benchmark like 60% S&P 500 + 40% Bond Aggregate (matching the portfolio's asset allocation)","Only bonds","No benchmark"],"Blended benchmark."),
     ("For financial math, indices provide:",["Random numbers","*Percentage return calculations, benchmark comparison, and data for long-term compound growth analysis","Only news headlines","Only daily prices"],"Index math.")]
)
lessons[k]=v

# 8.4
k,v = build_lesson(8,4,"Trading Strategies",
    "<h3>Trading &amp; Investment Strategies</h3>"
    "<h4>Approaches to the Market</h4>"
    "<ul><li><b>Buy and Hold:</b> Long-term ownership; ignoring short-term fluctuations.</li>"
    "<li><b>Value Investing:</b> Buying undervalued stocks (low P/E, below book value).</li>"
    "<li><b>Growth Investing:</b> Buying companies with high earnings growth potential.</li>"
    "<li><b>Index Investing:</b> Passive; match the market through index funds.</li>"
    "<li><b>Dollar Cost Averaging:</b> Fixed amount at regular intervals.</li></ul>",
    [("Buy and Hold","Long-term strategy of purchasing quality investments and holding through market ups and downs; lowest cost, historically very effective."),
     ("Value Investing","Strategy of finding stocks trading below their intrinsic value (low P/E, P/B); pioneered by Benjamin Graham and Warren Buffett."),
     ("Growth Investing","Strategy focused on companies with high revenue/earnings growth, often with higher P/E ratios; accepts higher valuations for faster growth."),
     ("Dollar Cost Averaging (DCA)","Investing a fixed dollar amount at regular intervals regardless of price; reduces timing risk and emotional decision-making."),
     ("Asset Allocation","Dividing investments among asset classes (stocks, bonds, cash, real estate) based on risk tolerance, goals, and time horizon.")],
    [("Buy and hold works best over:",["Days","Weeks","*Long periods (10+ years) — time in the market beats timing the market","Months only"],"Long-term focus."),
     ("$10,000 invested in the S&P 500 in 1990 would be worth approximately _____ by 2024 (reinvesting dividends).",["$50,000","$100,000","*~$200,000+ (the power of long-term compounding at ~10% average annual returns)","$500,000"],"Buy and hold power."),
     ("Value investors look for stocks with:",["High P/E ratios","*Low P/E ratios, low price-to-book, and prices below estimated intrinsic value","Highest prices","Newest companies"],"Value criteria."),
     ("Warren Buffett's approach is primarily:",["Day trading","Growth investing","*Value investing (buying great companies at fair prices and holding forever)","Index investing"],"Oracle of Omaha."),
     ("Growth investors are willing to pay:",["Below book value","*Higher P/E ratios for companies with rapid revenue and earnings growth (betting on future expansion)","Only dividends","The lowest price"],"Growth premium."),
     ("Index investing involves:",["Picking individual stocks","Timing the market","*Buying funds that track entire market indices (passive, low-cost, highly diversified)","Only buying one stock"],"Passive approach."),
     ("Dollar cost averaging: investing $500/month when prices are $50, $40, and $60 buys:",["30 shares each month","*10, 12.5, and 8.33 shares (more shares when cheap, fewer when expensive — average cost < average price)","Equal shares","Only 10 shares"],"DCA mechanics."),
     ("The average cost per share with DCA ($1,500 total ÷ 30.83 total shares) ≈",["$50","*~$48.65 (lower than the average price of $50)","$40","$60"],"DCA advantage."),
     ("Asset allocation of 80/20 (stocks/bonds) is appropriate for:",["Retirees","*Young investors with a long time horizon (can weather stock volatility for higher returns)","Very conservative investors","All ages equally"],"Age-appropriate allocation."),
     ("Asset allocation of 40/60 (stocks/bonds) is appropriate for:",["Young investors","*Near-retirees or conservative investors who need stability and income over growth","Aggressive investors","Day traders"],"Conservative allocation."),
     ("Rebalancing a portfolio means:",["Selling everything","*Periodically adjusting back to target allocation (sell what grew above target, buy what fell below)","Never selling","Only buying"],"Maintain target."),
     ("Tax-efficient investing places _____ in taxable accounts and _____ in tax-advantaged accounts.",["Bonds, stocks","*Index funds/stocks (low turnover, capital gains), and bonds/REITs (high tax on income) in tax-advantaged","Cash only in both","It doesn't matter"],"Asset location."),
     ("Day trading (buying and selling within one day) is:",["Easy money","*Extremely risky — studies show 70-90% of day traders lose money; emotional decisions and transaction costs erode returns","A guaranteed strategy","Better than indexing"],"Day trading reality."),
     ("The EMH (Efficient Market Hypothesis) suggests:",["Markets are always wrong","*Stock prices reflect all available information — making it very difficult to consistently beat the market","Only insiders profit","Markets are perfectly predictable"],"Market efficiency."),
     ("Momentum investing buys stocks that are:",["Falling in price","*Rising in price (trend-following — betting that recent winners will continue to outperform near-term)","Unchanged","Newly listed"],"Trend following."),
     ("Contrarian investing does the opposite: buying when others are:",["Buying","*Selling/fearful (buying undervalued stocks during pessimism), and selling when others are greedy","Also buying","Holding"],"Be greedy when others are fearful."),
     ("A diversified portfolio of 60% US stocks, 25% international stocks, 15% bonds provides:",["No diversification","*Geographic diversification, asset class diversification, and reduced correlation for smoother long-term returns","Only US exposure","Only bond exposure"],"Broad diversification."),
     ("The most important factor in long-term investment success is:",["Stock picking","Market timing","*Asset allocation and consistent investing over time (staying the course through market cycles)","Luck"],"Key success factor."),
     ("Compound returns: $500/month at 10% for 30 years grows to approximately:",["$180,000","$300,000","*~$1.1 million (the power of consistent investing and compound growth)","$500,000"],"DCA + compounding."),
     ("For financial math, investment strategies apply:",["No math","*Compound interest, percentage returns, ratio analysis, and probability to building long-term wealth","Only stock prices","Only one formula"],"Strategy math.")]
)
lessons[k]=v

# 8.5
k,v = build_lesson(8,5,"Global Finance & Currency",
    "<h3>Global Finance &amp; Currency</h3>"
    "<h4>Foreign Exchange (Forex)</h4>"
    "<p>Currencies trade in pairs (USD/EUR). Exchange rates fluctuate based on supply/demand, interest rates, and economics.</p>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>Exchange rate:</b> Price of one currency in terms of another.</li>"
    "<li><b>Appreciation/Depreciation:</b> Currency gaining/losing value relative to another.</li>"
    "<li><b>Purchasing Power Parity:</b> Theory that exchange rates should equalize prices across countries.</li></ul>",
    [("Exchange Rate","The price of one currency expressed in another (e.g., 1 USD = 0.92 EUR means $1 buys €0.92)."),
     ("Currency Appreciation","When a currency gains value relative to another (stronger dollar means it buys more foreign currency)."),
     ("Currency Depreciation","When a currency loses value relative to another (weaker dollar means it buys less foreign currency)."),
     ("Purchasing Power Parity (PPP)","Theory that exchange rates should adjust so identical goods cost the same across countries in the long run."),
     ("Foreign Direct Investment (FDI)","Investment by a company or individual in one country into business interests in another country (factories, offices).")],
    [("An exchange rate of 1 USD = 110 JPY means:",["$1 = ¥1","$110 = ¥1","*$1 buys ¥110","¥1 buys $110"],"Rate interpretation."),
     ("Converting $500 to euros at 1 USD = 0.92 EUR:",["€500","€550","*€460 (500 × 0.92)","€92"],"USD to EUR."),
     ("Converting €200 to dollars at 1 EUR = 1.09 USD:",["$200","$92","*$218 (200 × 1.09)","$109"],"EUR to USD."),
     ("If the dollar strengthens (appreciates), American tourists abroad:",["Pay more","*Pay less (their dollars buy more foreign currency, making foreign goods cheaper)","Pay the same","Can't travel"],"Strong dollar effect."),
     ("If the dollar weakens (depreciates), US exports become:",["More expensive abroad","*Cheaper abroad (foreign buyers need less of their own currency to buy US goods)","The same price","Impossible to sell"],"Weak dollar + exports."),
     ("A strong dollar hurts US companies that:",["Import goods","*Export goods (their products become more expensive for foreign buyers — reducing competitiveness)","Only sell domestically","Have no foreign operations"],"Export impact."),
     ("The forex market trades approximately _____ per day.",["$1 billion","$100 billion","*$6-7 trillion (the largest financial market in the world)","$100 trillion"],"Massive market."),
     ("Interest rate increases by the Fed typically cause the dollar to:",["Weaken","*Strengthen (higher rates attract foreign capital seeking better returns — increasing demand for USD)","Stay the same","Collapse"],"Rate-currency link."),
     ("Inflation typically causes a currency to:",["Strengthen","*Weaken/depreciate (higher prices reduce purchasing power relative to other currencies)","Stay unchanged","Disappear"],"Inflation impact."),
     ("Purchasing Power Parity suggests a Big Mac should cost:",["The same in dollars everywhere","*Approximately the same (when converted) across countries, adjusted for exchange rates","Different everywhere","Only what McDonald's decides"],"PPP theory."),
     ("The 'Big Mac Index' is an informal measure of:",["Fast food quality","*Currency valuation — comparing Big Mac prices worldwide to assess whether currencies are over/undervalued","Restaurant popularity","Beef prices"],"Economist tool."),
     ("Currency hedging is used by companies to:",["Speculate on forex","*Protect against exchange rate changes that could reduce profits from international operations","Avoid all trade","Only increase profits"],"Risk management."),
     ("A US company expecting €1M payment in 3 months can hedge by:",["Doing nothing","*Buying a forward contract to lock in today's exchange rate (guaranteeing the dollar amount regardless of rate changes)","Canceling the contract","Only accepting dollars"],"Forward contract."),
     ("Trade deficit means a country:",["Exports more than imports","*Imports more than exports (buying more from other countries than selling to them)","Has balanced trade","Has no trade"],"Deficit definition."),
     ("The US trade deficit is approximately:",["$0","$50 billion","*$600-800 billion annually","$10 trillion"],"US trade balance."),
     ("GDP (Gross Domestic Product) measures:",["Only government spending","Only consumer spending","*The total value of all goods and services produced in a country during a specific period","Only exports"],"Economic output."),
     ("Emerging market investments offer:",["Lower returns, lower risk","*Potentially higher returns but with higher risk (political instability, currency volatility, less regulation)","Guaranteed returns","No risk"],"Risk-return tradeoff."),
     ("International diversification benefits investors because:",["All markets move together","*Different countries' markets don't perfectly correlate — when US markets decline, other markets may hold steady or rise","Foreign markets always beat US","It's required by law"],"Geographic diversification."),
     ("Cryptocurrency as a global currency is:",["Widely accepted everywhere","*Still evolving — used for some transactions but faces volatility, regulation, and adoption challenges","Fully replacing fiat","Illegal everywhere"],"Crypto status."),
     ("For financial math, global finance applies:",["No math","*Currency conversion, exchange rate calculations, and international pricing — essential for an increasingly global economy","Only for banks","Only for travelers"],"Global math.")]
)
lessons[k]=v

# 8.6
k,v = build_lesson(8,6,"Market Case Studies",
    "<h3>Market Case Studies</h3>"
    "<h4>Case 1: 2008 Financial Crisis</h4>"
    "<p>S&P 500 fell ~57% from Oct 2007 to Mar 2009. An investor who stayed invested recovered by Mar 2013 and gained ~400% by 2024. One who sold at the bottom locked in losses permanently.</p>"
    "<h4>Case 2: COVID Crash & Recovery (2020)</h4>"
    "<p>S&P 500 dropped 34% in 23 trading days (fastest bear market ever). Recovery: new highs within 5 months.</p>",
    [("Market Crash","A rapid, severe decline in stock prices (often 20%+ in days or weeks); caused by panic, economic shocks, or systemic failures."),
     ("Recovery Time","The period needed for markets to return to pre-crash levels; historically ranges from months to years."),
     ("Behavioral Finance","Study of psychological biases affecting financial decisions: panic selling, herd mentality, overconfidence, loss aversion."),
     ("Panic Selling","Emotionally driven selling during market drops; often locks in losses at or near the bottom — the worst time to sell."),
     ("Mean Reversion","Tendency of markets to return to long-term averages over time; crashes are typically followed by recoveries.")],
    [("During the 2008 crisis, the S&P 500 fell approximately:",["10%","25%","*57% from peak to trough (Oct 2007 – Mar 2009)","80%"],"Crash magnitude."),
     ("An investor who stayed invested through 2008 recovered fully by approximately:",["2009","2011","*March 2013 (about 4 years after the bottom)","2020"],"Recovery timeline."),
     ("$100,000 invested at the 2009 bottom grew to approximately _____ by 2024.",["$200,000","$300,000","*~$600,000+ (one of the greatest buying opportunities in history)","$100,000"],"Bottom-to-recovery."),
     ("The COVID crash of 2020 saw the S&P 500 drop _____ in just 23 trading days.",["10%","20%","*34%","50%"],"Fastest bear market."),
     ("The COVID recovery to new all-time highs took approximately:",["2 years","1 year","*~5 months (one of the fastest recoveries in history)","5 years"],"Rapid recovery."),
     ("The main lesson from both crashes for long-term investors is:",["Sell immediately at the first sign of trouble","*Stay invested — time in the market beats timing the market; panic selling locks in losses","Never invest in stocks","Only invest after crashes"],"Stay the course."),
     ("Panic selling during a crash is harmful because:",["It saves money","*You sell at low prices and typically miss the rebound (the best days often follow the worst days)","It locks in gains","It's always rational"],"Behavioral mistake."),
     ("Missing the 10 best days in the market over 20 years can cut returns by:",["10%","20%","*More than 50% (many of the best days occur immediately after the worst days, during recoveries)","5%"],"Timing cost."),
     ("Dollar cost averaging during a crash means:",["Losing more money","*Buying more shares at lower prices (DCA into falling markets = lower average cost = higher returns on recovery)","Stopping all investing","Selling at a loss"],"DCA through fear."),
     ("The dot-com bubble (2000) primarily affected:",["Banks","Real estate","*Technology stocks (NASDAQ fell ~78% from peak — speculative valuations collapsed)","Bond markets"],"Tech bubble."),
     ("The 2008 crisis was primarily caused by:",["Technology stocks","*Subprime mortgages, excessive leverage, credit default swaps, and inadequate regulation (housing bubble burst)","COVID-19","A single company"],"Root cause."),
     ("Diversification during the 2008 crisis helped because:",["All assets fell equally","*Bonds gained value as stocks fell — offsetting some losses in a balanced portfolio","Cash lost value","Nothing helped"],"Diversification benefit."),
     ("Recency bias causes investors to:",["Think long-term","*Overweight recent events (expect crashes after crashes, or endless gains after bull markets) — clouding rational judgment","Act rationally","Diversify more"],"Cognitive bias."),
     ("Loss aversion means:",["Loving losses","*The pain of losing $1 feels 2× worse than the pleasure of gaining $1 — leading to panic selling and missed opportunities","Neutral about losses","Seeking losses"],"Psychological asymmetry."),
     ("Herd mentality in investing means:",["Independent thinking","*Following the crowd — buying when everyone buys (FOMO) and selling when everyone sells (panic)","Contrarian thinking","Systematic investing"],"Group behavior."),
     ("The 1987 'Black Monday' crash saw the Dow fall _____ in ONE day.",["5%","10%","*~22% (the largest single-day percentage drop in history)","50%"],"Extreme single-day event."),
     ("Japan's Nikkei index peaked in 1989 and took _____ to recover to that level.",["5 years","15 years","*~34 years (2024) — a cautionary tale about concentration in a single country","Never recovered"],"Japan lesson."),
     ("The lesson from Japan for portfolio construction is:",["Only invest in Japan","*Diversify internationally — no single country's market is guaranteed to perform well over any given period","Avoid all international investing","Only invest in the US"],"Global diversification."),
     ("Market crashes happen on average every _____ years (declines of 20%+).",["1","*~3-5 (bear markets are a normal part of investing — you will experience several in a lifetime)","10","20"],"Normal occurrence."),
     ("For financial math, market history teaches:",["Nothing useful","*Compound growth, recovery math, the cost of emotional decisions, and the power of staying invested through volatility","Only fear","Only optimism"],"Historical lessons.")]
)
lessons[k]=v

# 8.7
k,v = build_lesson(8,7,"Technology in Markets",
    "<h3>Technology in Financial Markets</h3>"
    "<h4>Modern Trading Technology</h4>"
    "<ul><li><b>Online brokerages:</b> Fidelity, Schwab, Robinhood — $0 commission trades.</li>"
    "<li><b>Robo-advisors:</b> Betterment, Wealthfront — automated portfolio management.</li>"
    "<li><b>Trading apps:</b> Mobile access to real-time quotes, trading, and account management.</li>"
    "<li><b>Algorithmic trading:</b> Computer programs executing trades at high speed based on algorithms.</li></ul>",
    [("Online Brokerage","Digital platform for buying/selling stocks, ETFs, and other securities; most major brokers now offer $0 commissions."),
     ("Robo-Advisor","Automated investment platform that creates and manages a diversified portfolio based on your risk tolerance and goals; low fees (~0.25%)."),
     ("Algorithmic Trading","Computer programs executing trades based on mathematical rules at speeds impossible for humans."),
     ("Fractional Shares","Ability to buy a portion of a share (e.g., $50 worth of a $3,000 stock); makes expensive stocks accessible to all investors."),
     ("Fintech Disruption","Technology-driven innovation transforming financial services: mobile banking, peer-to-peer payments, cryptocurrency, automated investing.")],
    [("Major online brokerages now charge _____ per stock/ETF trade.",["$5.99","$9.99","*$0 (commission-free trading has become the industry standard)","$19.99"],"Zero commissions."),
     ("Robo-advisors typically charge:",["1-2%","*~0.25% annually (much less than traditional financial advisors' 1%+)","0%","3%"],"Low-cost management."),
     ("A robo-advisor with $50,000 at 0.25% charges _____ per year.",["$50","*$125","$250","$500"],"50000 × 0.0025."),
     ("A traditional advisor at 1% on $50,000 charges _____ per year.",["$125","$250","*$500","$1,000"],"Traditional cost."),
     ("The fee difference ($500 − $125 = $375/year) compounded over 30 years at 8% ≈",["$5,000","$15,000","*~$42,000+ in savings (fee differences compound dramatically over decades)","$100,000"],"Long-term fee impact."),
     ("Fractional shares allow investors to:",["Only buy whole shares","*Buy any dollar amount of any stock (e.g., $10 of Amazon or $25 of Berkshire Hathaway)","Trade for free","Avoid all risk"],"Accessibility."),
     ("ETFs (Exchange-Traded Funds) combine benefits of:",["Only stocks","Only bonds","*Mutual fund diversification with stock-like trading (buy/sell anytime during market hours, low fees)","Only cash"],"ETF advantages."),
     ("The most popular ETFs (SPY, VOO, VTI) track:",["Individual stocks","*Broad market indices (S&P 500 or Total Stock Market)","Only bonds","Only international stocks"],"Index ETFs."),
     ("Algorithmic trading accounts for approximately _____ of US stock market volume.",["10%","30%","*60-75%","99%"],"Algo dominance."),
     ("High-frequency trading (HFT) involves:",["Slow, deliberate trades","*Executing thousands of trades per second using algorithms to profit from tiny price differences","Manual trading","Only buying"],"Speed trading."),
     ("Mobile trading apps have _____ investor participation.",["Decreased","Not affected","*Dramatically increased (especially among younger investors who can invest from their phones)","Eliminated"],"Democratization."),
     ("A concern with easy mobile trading is:",["Too much information","*Gamification of investing leading to excessive trading, speculation, and emotional decisions","Too few options","Slow execution"],"Behavioral risk."),
     ("Social trading platforms (like eToro) allow:",["Only solo investing","*Copying the trades of experienced investors (but past performance doesn't guarantee future results)","Free money","Risk-free trading"],"Copy trading."),
     ("Cryptocurrency exchanges (Coinbase, Kraken) allow:",["Stock trading","*Buying, selling, and trading digital currencies (Bitcoin, Ethereum, etc.)","Only fiat currency","Only bank transfers"],"Crypto access."),
     ("Tax-loss harvesting is automated by robo-advisors to:",["Increase taxes","*Systematically sell losing positions to offset gains — potentially saving thousands in taxes annually","Avoid all trading","Only buy winners"],"Automated tax strategy."),
     ("Real-time market data and analysis tools give retail investors access to information that was once:",["Always available to everyone","*Only available to professional traders and institutions (leveling the playing field)","Never useful","Still unavailable"],"Information democratization."),
     ("Blockchain technology could revolutionize stock trading by:",["Slowing it down","*Enabling instant settlement (currently T+1), reducing intermediaries, and increasing transparency","Eliminating all trading","Making it more expensive"],"Blockchain potential."),
     ("AI-powered investment tools can:",["Replace all human judgment","*Analyze vast amounts of data, identify patterns, and assist with portfolio optimization — but can't predict the future","Guarantee profits","Eliminate risk"],"AI in finance."),
     ("The risks of fintech include:",["No risks","*Security breaches, algorithmic errors, overreliance on automation, and potential for flash crashes from algorithmic trading","Only privacy concerns","Only speed issues"],"Fintech risks."),
     ("For financial math, technology tools:",["Replace understanding math","*Make it easier to apply financial math concepts (compounding, diversification, tax optimization) but understanding the math behind the tools is still essential","Are unnecessary","Only help professionals"],"Tech + math literacy.")]
)
lessons[k]=v

# 8.8
k,v = build_lesson(8,8,"Behavioral Finance",
    "<h3>Behavioral Finance</h3>"
    "<h4>Common Cognitive Biases</h4>"
    "<ul><li><b>Loss aversion:</b> Pain of loss > pleasure of equal gain (2:1 ratio).</li>"
    "<li><b>Confirmation bias:</b> Seeking info that supports existing beliefs.</li>"
    "<li><b>Anchoring:</b> Over-relying on first piece of information (purchase price).</li>"
    "<li><b>Overconfidence:</b> Overestimating one's ability to pick stocks or time markets.</li>"
    "<li><b>Recency bias:</b> Overweighting recent events in predictions.</li></ul>",
    [("Loss Aversion","The psychological tendency where losses feel ~2× worse than equivalent gains feel good; leads to panic selling."),
     ("Confirmation Bias","Tendency to seek, interpret, and remember information that confirms pre-existing beliefs while ignoring contradictory evidence."),
     ("Anchoring","Fixating on a reference point (like purchase price) when making decisions, even when it's irrelevant to current value."),
     ("Overconfidence Bias","Overestimating one's ability to predict markets or pick winners; leads to excessive trading and concentrated positions."),
     ("FOMO (Fear of Missing Out)","Anxiety about missing profitable opportunities; drives buying at peaks (when 'everyone' is talking about a stock).")],
    [("Loss aversion means the pain of losing $100 feels equivalent to the pleasure of gaining approximately:",["$100","$150","*$200 (2× ratio — losses hurt twice as much as equivalent gains feel good)","$50"],"2:1 pain ratio."),
     ("Loss aversion leads investors to:",["Sell winners too soon","Hold losers too long","*Both — sell winners too early (to 'lock in' gains) and hold losers too long (hoping to break even)","Neither"],"Disposition effect."),
     ("Confirmation bias causes an investor who loves Tesla to:",["Research objectively","*Seek out positive Tesla news and dismiss negative data (selectively processing information)","Sell Tesla stock","Short Tesla"],"Selective information."),
     ("Anchoring on a purchase price of $100 might cause you to hold a stock worth $60 because:",["It's a good investment","*You're 'anchored' to $100 and waiting to 'get back to even' — but the market doesn't care what YOU paid","The price will definitely recover","Your purchase price determines value"],"Irrelevant anchor."),
     ("Overconfidence leads to:",["Better returns","*Excessive trading (which increases costs and taxes), concentrated positions, and failure to diversify","More diversification","Lower risk"],"Costly overtrading."),
     ("Studies show that investors who trade most frequently:",["Earn the highest returns","*Earn significantly lower returns than buy-and-hold investors (transaction costs and bad timing erode returns)","Break even","Always beat the market"],"Trading costs."),
     ("Recency bias after a market crash causes investors to:",["Buy aggressively","*Expect more declines and sell/avoid investing (recent bad experience dominates their outlook, even when recovery is likely)","Stay neutral","Think long-term"],"Extrapolating recent events."),
     ("FOMO during a bull market leads investors to:",["Sell everything","*Buy at high valuations because 'everyone else is making money' (often entering near market peaks)","Stay out of the market","Diversify carefully"],"Buying at peaks."),
     ("Herd mentality means:",["Independent analysis","*Following the crowd — buying when everyone buys, selling when everyone sells (amplifying market swings)","Contrarian investing","Systematic analysis"],"Group behavior."),
     ("The sunk cost fallacy in investing means:",["Ignoring past costs","*Continuing to hold a losing investment because you've 'already invested so much' (past costs shouldn't affect future decisions)","Selling at the right time","Never investing"],"Irreversible past costs."),
     ("Endowment effect causes people to:",["Undervalue what they own","*Overvalue what they already own (demanding a higher price to sell than they'd pay to buy the same thing)","Trade rationally","Sell easily"],"Ownership premium."),
     ("Mental accounting causes someone to treat:",["All money equally","*Money differently based on source (treating a $5,000 tax refund differently than $5,000 salary — but it's all money)","Only salary as real","Only bonuses as real"],"Irrational categorization."),
     ("Availability bias means:",["Using all available data","*Overestimating the probability of events that come easily to mind (recent crashes, headline-grabbing events)","Researching thoroughly","Ignoring data"],"Memorable = likely."),
     ("Framing effect: '90% success rate' vs. '10% failure rate' — same data, but people:",["Respond the same","*Respond more positively to '90% success' even though both convey identical information","Ignore both","Only see numbers"],"Presentation matters."),
     ("The antidote to most behavioral biases is:",["More analysis","*A written investment plan followed systematically (automation, rules-based investing, removing emotion from decisions)","More market watching","More trading"],"Systematic rules."),
     ("Dollar cost averaging combats behavioral biases by:",["Requiring timing skill","*Removing the decision of 'when to invest' — automated, consistent investing regardless of market conditions or emotions","Only buying dips","Only buying peaks"],"Automation beats emotion."),
     ("Index investing combats overconfidence by:",["Encouraging stock picking","*Acknowledging that most people can't beat the market — and matching market returns is a winning strategy","Requiring active trading","Maximizing turnover"],"Humility in investing."),
     ("Keeping an investment journal helps because:",["It's required","*It creates accountability and allows you to review past decisions objectively (identifying patterns of bias)","It's fun","Advisors require it"],"Self-awareness tool."),
     ("The efficient market hypothesis (EMH) relates to behavioral finance because:",["They agree completely","*EMH says markets are rational; behavioral finance shows individual investors often are NOT — creating both opportunities and risks","They're unrelated","EMH supports biases"],"Tension between theories."),
     ("For financial math, behavioral finance shows that:",["Math is irrelevant","*Understanding the math AND the psychology behind financial decisions is essential — knowing the right answer doesn't help if emotions override rational choices","Only emotions matter","Only math matters"],"Math + psychology.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 8: wrote {len(lessons)} lessons")
