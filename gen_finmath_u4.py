#!/usr/bin/env python3
"""Financial Math Unit 4 – Investments & Retirement (8 lessons)."""
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

# 4.1
k,v = build_lesson(4,1,"Stocks, Bonds, & Mutual Funds",
    "<h3>Core Investment Types</h3>"
    "<h4>Stocks</h4>"
    "<ul><li>Shares of ownership in a company.</li>"
    "<li>Returns: dividends + capital gains (price increase).</li>"
    "<li>Higher risk, higher potential return.</li></ul>"
    "<h4>Bonds</h4>"
    "<ul><li>Loans to a government or corporation.</li>"
    "<li>Returns: regular interest (coupon) payments + face value at maturity.</li>"
    "<li>Lower risk, lower return.</li></ul>"
    "<h4>Mutual Funds &amp; ETFs</h4>"
    "<ul><li>Pooled investments holding many stocks/bonds.</li>"
    "<li>Instant diversification; managed (mutual funds) or passive (index ETFs).</li></ul>",
    [("Stock","A share of ownership in a company; returns come from dividends and price appreciation (capital gains)."),
     ("Bond","A loan to a government or corporation; pays regular interest (coupon) and returns face value at maturity."),
     ("Mutual Fund","A pooled investment fund managed by a professional that holds a diversified portfolio of stocks, bonds, or both."),
     ("ETF (Exchange-Traded Fund)","Similar to a mutual fund but trades on an exchange like a stock; often tracks an index with low fees."),
     ("Dividend","A portion of a company's profits distributed to shareholders, typically quarterly.")],
    [("A stock represents:",["A loan to a company","*Ownership (equity) in a company","A government bond","A savings deposit"],"Ownership share."),
     ("A bond represents:",["Ownership in a company","*A loan to a government or corporation","A stock share","A mutual fund"],"Debt instrument."),
     ("Stocks generally offer _____ risk and _____ potential return than bonds.",["Lower, lower","*Higher, higher","The same, the same","Lower, higher"],"Risk-return tradeoff."),
     ("Average annual return of the S&P 500 (historically) is approximately:",["3%","5%","*~10% (before inflation; ~7% after inflation)","15%"],"Historical average."),
     ("The coupon rate on a bond is:",["The purchase price","*The annual interest payment as a percentage of face value","The maturity date","The credit rating"],"Bond interest rate."),
     ("A $1,000 bond with a 5% coupon pays _____ per year in interest.",["$100","*$50","$500","$5"],"1000 × 0.05."),
     ("Mutual funds provide _____ through holding many different investments.",["Concentration","*Diversification","Leverage","Insurance"],"Spread risk."),
     ("Index funds track a market index (like S&P 500) and have:",["High fees","*Very low fees (since they're passively managed, not actively picked)","No returns","Guaranteed returns"],"Low-cost investing."),
     ("The expense ratio of a mutual fund represents:",["Your return","*The annual fee charged as a percentage of your investment (e.g., 0.03% for index funds vs. 1%+ for active)","The tax rate","The dividend"],"Fund cost."),
     ("A 1% expense ratio on $100,000 costs _____ per year.",["$100","*$1,000","$10,000","$10"],"Fee impact."),
     ("$100,000 over 30 years at 7%: with 0.1% fees = $740K vs. 1% fees = $574K. Lost to fees:",["$10,000","$50,000","*~$166,000","$200,000"],"Fees compound enormously."),
     ("Dividends can be:",["Only spent","*Reinvested (DRIP) to buy more shares, accelerating compound growth","Only taxed","Only in bonds"],"Dividend reinvestment."),
     ("Capital gains occur when:",["A stock pays dividends","*You sell an investment for more than you paid for it","You hold stocks","You buy bonds"],"Profit on sale."),
     ("Bond prices and interest rates move:",["In the same direction","*Inversely (when rates rise, bond prices fall; when rates fall, bond prices rise)","Independently","Unpredictably"],"Inverse relationship."),
     ("A bond's credit rating (AAA, AA, etc.) indicates:",["Its return","*The likelihood the issuer will repay (higher rating = lower risk = lower yield)","Its maturity","Its coupon"],"Creditworthiness."),
     ("Government bonds are considered low-risk because:",["They pay high interest","*They're backed by the government's ability to tax (virtually no default risk for US Treasuries)","They're popular","They're short-term only"],"Government backing."),
     ("ETFs differ from mutual funds in that they:",["Are safer","*Trade throughout the day like stocks (mutual funds only trade at end of day) and often have lower fees","Are riskier","Don't diversify"],"Trading flexibility."),
     ("Dollar-cost averaging means:",["Buying at the lowest price","*Investing a fixed amount regularly regardless of price (automatically buying more shares when prices are low)","Only buying in dollars","Timing the market"],"Disciplined investing."),
     ("For a young investor with a 40-year horizon, the recommended allocation is typically:",["100% bonds","*Mostly stocks (aggressive growth — time to recover from market drops)","50/50 stocks and bonds","100% cash"],"Time horizon allocation."),
     ("Understanding stocks, bonds, and funds is essential for:",["Only the wealthy","*Everyone — retirement savings, college funds, and financial security depend on investment knowledge","Only financial advisors","Only day traders"],"Universal importance.")]
)
lessons[k]=v

# 4.2
k,v = build_lesson(4,2,"Risk vs. Return",
    "<h3>Risk vs. Return</h3>"
    "<h4>Core Principle</h4>"
    "<p>Higher potential returns come with higher risk. The key is finding the right balance for your situation.</p>"
    "<h4>Risk Spectrum</h4>"
    "<ul><li><b>Low risk:</b> Savings accounts, CDs, T-bills (1–5% return).</li>"
    "<li><b>Medium risk:</b> Bonds, balanced funds (4–8% return).</li>"
    "<li><b>High risk:</b> Stocks, real estate, crypto (8–12%+ return, with volatility).</li></ul>"
    "<h4>Measuring Risk</h4>"
    "<p><b>Standard deviation</b> measures how much returns vary from the average.</p>",
    [("Risk-Return Tradeoff","Higher expected returns require accepting higher risk — there is no free lunch in investing."),
     ("Standard Deviation","Statistical measure of volatility; higher SD = wider range of possible outcomes (more risk)."),
     ("Volatility","The degree of variation in investment returns — high volatility means large price swings."),
     ("Risk Tolerance","An individual's ability and willingness to endure investment losses; depends on time horizon, income, and temperament."),
     ("Beta","Measure of a stock's volatility relative to the overall market; beta > 1 means more volatile than the market.")],
    [("The risk-return tradeoff means:",["Higher risk always loses money","*Higher potential returns require accepting higher risk","Low risk investments earn the most","Risk doesn't matter"],"Fundamental principle."),
     ("Which has the lowest risk?",["Individual stocks","*US Treasury bills (essentially risk-free — backed by the full faith and credit of the US government)","Cryptocurrency","Small-cap stocks"],"Risk spectrum."),
     ("Which has the highest expected return over 30+ years?",["Bonds","Savings accounts","*A diversified stock portfolio (historically ~10% annually)","CDs"],"Long-term best."),
     ("Standard deviation measures:",["Average return","*How much returns vary from their average (higher SD = more unpredictable outcomes)","The minimum return","The maximum return"],"Volatility measure."),
     ("An investment with returns of 8%, 12%, 6%, 14% has _____ risk than one with 9%, 10%, 9.5%, 10.5%.",["Less","The same","*More (wider variation in returns = higher standard deviation)","Cannot tell"],"Consistency matters."),
     ("Beta of 1.5 means a stock is:",["Less volatile than the market","*50% more volatile than the market (if market drops 10%, this stock might drop 15%)","The same as the market","Risk-free"],"Relative volatility."),
     ("Risk tolerance is influenced by:",["Only age","Only income","*Age, time horizon, income stability, financial goals, family situation, and personal temperament","Only the market"],"Multi-factor personal assessment."),
     ("A 25-year-old saving for retirement in 40 years can tolerate _____ risk than a 60-year-old retiring in 5 years.",["Less","The same","*More (more time to recover from market downturns)","No"],"Time horizon effect."),
     ("Diversification reduces risk by:",["Eliminating all risk","*Spreading investments across different assets so poor performance in one is offset by better performance in others","Concentrating in one stock","Avoiding the market"],"Don't put all eggs in one basket."),
     ("Systematic risk (market risk) is:",["Eliminable through diversification","*Risk affecting the entire market that CANNOT be diversified away (recession, inflation, war)","Only in one stock","Avoidable"],"Undiversifiable."),
     ("Unsystematic risk (specific risk) is:",["Market-wide","*Risk specific to a company or industry that CAN be reduced through diversification","Never reducible","Only in bonds"],"Diversifiable."),
     ("The Sharpe ratio measures:",["Total return","*Risk-adjusted return (return above risk-free rate per unit of risk — higher is better)","Only risk","Only fees"],"Performance per unit of risk."),
     ("A portfolio with 12% return and 15% SD vs. 10% return and 8% SD: risk-adjusted, the second is _____ risky per unit of return.",["More","*Less (lower SD relative to return = better risk-adjusted performance)","Equally","Cannot compare"],"Efficiency comparison."),
     ("Inflation risk means:",["Prices decrease","*Your investment returns may not keep up with rising prices, reducing purchasing power","There is no inflation","Only affects cash"],"Purchasing power risk."),
     ("Keeping all savings in cash carries _____ risk.",["No","*Inflation risk (your money loses purchasing power over time even though the nominal amount stays the same)","Market risk","Investment risk"],"Cash loses value."),
     ("Liquidity risk is:",["Having too much cash","*The risk of not being able to sell an investment quickly without significant loss of value (e.g., real estate)","Having too many stocks","Never important"],"Can you sell it?"),
     ("The efficient frontier shows:",["Only one portfolio","*The set of portfolios offering the highest expected return for each level of risk (optimal portfolios)","Only stocks","Only bonds"],"Optimal portfolios."),
     ("Asset allocation (stocks vs. bonds vs. cash mix) accounts for approximately _____ of portfolio performance variation.",["10%","50%","*~90% (much more important than individual stock picking or market timing)","100%"],"Allocation dominates."),
     ("Modern Portfolio Theory suggests:",["Own one stock","*Combining assets with different correlations (that don't move together) reduces overall portfolio risk","Avoid all risk","Only bonds are safe"],"Correlation-based diversification."),
     ("Understanding risk vs. return helps you:",["Avoid all investments","*Make informed decisions aligned with your goals, time horizon, and comfort level — not react emotionally to markets","Only buy safe assets","Time the market"],"Informed decision-making.")]
)
lessons[k]=v

# 4.3
k,v = build_lesson(4,3,"Annuities & Pension Calculations",
    "<h3>Annuities</h3>"
    "<h4>Future Value of an Annuity</h4>"
    "<p><b>FV = PMT × [(1+r)^n − 1] / r</b></p>"
    "<p>Calculates what regular payments grow to over time.</p>"
    "<h4>Present Value of an Annuity</h4>"
    "<p><b>PV = PMT × [1 − (1+r)^(−n)] / r</b></p>"
    "<p>Calculates the lump sum value of a stream of future payments.</p>"
    "<h4>Example</h4>"
    "<p>$500/month at 7%/12 for 30 years: FV = 500 × [(1.00583)^360 − 1]/0.00583 ≈ $566,765</p>",
    [("Annuity","A series of equal payments made at regular intervals (monthly, quarterly, annually)."),
     ("FV of Annuity","Future value of regular payments: FV = PMT × [(1+r)^n − 1] / r."),
     ("PV of Annuity","Present value of future payment stream: PV = PMT × [1 − (1+r)^(−n)] / r."),
     ("Annuity Due","Payments made at the BEGINNING of each period (vs. ordinary annuity at end); FV is slightly higher."),
     ("Pension","Regular retirement income guaranteed by an employer; value calculated as present value of future annuity payments.")],
    [("The future value of an annuity formula is:",["FV = Prt","*FV = PMT × [(1+r)^n − 1] / r","FV = Pe^rt","FV = PV + PMT"],"Annuity FV formula."),
     ("$500/month at 7% annual (0.583%/month) for 30 years grows to approximately:",["$180,000","$300,000","*~$566,765","$1,000,000"],"Annuity future value."),
     ("The total contributed in $500/month for 30 years is:",["$180,000","$200,000","*$180,000 (500 × 360)","$360,000"],"Contributions only."),
     ("Interest earned on the $500/month annuity above is approximately:",["$100,000","$200,000","*~$386,765 ($566,765 − $180,000)","$500,000"],"Growth from compound interest."),
     ("The present value of an annuity formula calculates:",["Future growth","*The lump sum equivalent today of a series of future payments","Monthly payments","Interest rate"],"Today's value."),
     ("A pension paying $3,000/month for 25 years at 5% discount rate has a present value of approximately:",["$300,000","$500,000","*~$512,000 (PV = 3000 × [1−(1.00417)^−300]/0.00417)","$900,000"],"Lump sum equivalent."),
     ("An annuity due differs from an ordinary annuity because payments are:",["At the end","*At the beginning of each period (slightly more valuable due to one extra period of compounding)","Variable","Random"],"Timing difference."),
     ("$200/month for 40 years at 8% grows to approximately:",["$96,000","$300,000","*~$698,202","$1,000,000"],"Long-term annuity."),
     ("To accumulate $1,000,000 in 30 years at 8%: required monthly payment ≈:",["$500","*~$671","$1,000","$2,000"],"Solve for PMT."),
     ("$1,000/month at 6% for 20 years grows to:",["$240,000","$350,000","*~$462,041","$600,000"],"20-year annuity."),
     ("The present value of $50,000/year for 20 years at 4% is approximately:",["$500,000","$800,000","*~$679,516","$1,000,000"],"PV of income stream."),
     ("Choosing between a $500,000 lump sum vs. $3,500/month pension for 25 years (at 5%):",["Lump sum always better","*Calculate PV of pension (~$597,000) and compare — the pension is worth more in this case","Pension always better","Cannot determine"],"Quantitative comparison."),
     ("Deferred annuities:",["Start payments immediately","*Delay payments until a future date (e.g., start paying at age 65); money compounds during the deferral period","Have no growth","Are the same as immediate"],"Delayed start."),
     ("The risk of a pension is:",["No risk","*The employer may not fully fund the pension (underfunding) or the company may go bankrupt","Only inflation","Only taxes"],"Employer solvency risk."),
     ("PBGC (Pension Benefit Guaranty Corporation) protects:",["All pension amounts","*Some pension benefits if an employer's defined benefit pension plan fails (up to limits)","Only government pensions","Only 401(k)s"],"Federal safety net."),
     ("Increasing the payment by _____ dramatically increases the final FV of an annuity.",["$1","$5","*Even small increases ($50 extra/month can add $100K+ over 30 years at 7%)","$1,000"],"Marginal payments compound."),
     ("An annuity in insurance context means:",["An investment only","*An insurance product that converts a lump sum into a guaranteed income stream (often for retirement)","A loan","A savings account"],"Insurance product."),
     ("The biggest weakness of fixed annuity products is:",["They're too risky","*Fees (often 2-3%+ annually in variable annuities) and limited liquidity — may not be best for most people","They pay too much","They're tax-free"],"Fee awareness."),
     ("Social Security payments are essentially:",["A savings account","*A government annuity — lifetime monthly payments based on your earnings history","A stock investment","A bond"],"Government annuity."),
     ("Annuity calculations in financial math demonstrate:",["Only one formula","*Time value of money, compound interest, and how regular small contributions grow into substantial sums","Only insurance","Only pensions"],"Core TVM concept.")]
)
lessons[k]=v

# 4.4
k,v = build_lesson(4,4,"Retirement Account Planning",
    "<h3>Retirement Account Planning</h3>"
    "<h4>Account Types</h4>"
    "<ul><li><b>401(k)/403(b):</b> Employer-sponsored; pre-tax contributions; employer match = free money.</li>"
    "<li><b>Traditional IRA:</b> Tax-deductible contributions; taxed on withdrawal.</li>"
    "<li><b>Roth IRA:</b> After-tax contributions; tax-FREE growth and withdrawals.</li></ul>"
    "<h4>Key Numbers (2024)</h4>"
    "<ul><li>401(k) max: $23,000/year ($30,500 if 50+).</li>"
    "<li>IRA max: $7,000/year ($8,000 if 50+).</li>"
    "<li>Full Social Security age: 67 for those born after 1960.</li></ul>",
    [("401(k)","Employer-sponsored retirement plan with pre-tax contributions; many employers offer matching contributions."),
     ("Roth IRA","Individual retirement account funded with after-tax dollars; all growth and qualified withdrawals are tax-free."),
     ("Traditional IRA","Individual retirement account with tax-deductible contributions; withdrawals in retirement are taxed as income."),
     ("Employer Match","Employer contributes to your 401(k) based on your contributions (e.g., 50% match up to 6% = instant 50% return)."),
     ("Required Minimum Distribution (RMD)","Mandatory annual withdrawals from traditional retirement accounts starting at age 73.")],
    [("A 401(k) uses _____ contributions.",["After-tax","*Pre-tax (reduces your taxable income now; you pay taxes when you withdraw in retirement)","Tax-free","Penalty-free"],"Pre-tax advantage."),
     ("A Roth IRA uses _____ contributions.",["Pre-tax","*After-tax (you pay taxes now, but all growth and qualified withdrawals are completely tax-free)","Tax-deductible","Employer-matched"],"After-tax → tax-free growth."),
     ("An employer match of 50% up to 6% of salary on a $60,000 salary means the employer contributes:",["$500","$1,000","*$1,800/year (50% of 6% of $60,000 = 0.50 × 0.06 × 60000)","$3,600"],"Free money calculation."),
     ("Not contributing enough to get the full employer match is:",["Smart","*Leaving free money on the table (the match is an instant 50-100% return on your contribution)","Normal","Recommended"],"Always get the match."),
     ("The 2024 401(k) contribution limit is:",["$6,000","$19,500","*$23,000 ($30,500 if age 50+)","$50,000"],"Current limits."),
     ("$500/month into a 401(k) from age 25 to 65 at 8% grows to approximately:",["$250,000","$500,000","*~$1,745,504","$3,000,000"],"40 years of compounding."),
     ("The tax advantage of a Roth IRA for a young person is:",["Immediate tax deduction","*Tax-free growth for decades — contributions are taxed now (lower bracket) but all growth is NEVER taxed","Higher contribution limits","Employer match"],"Tax-free compounding."),
     ("$7,000/year Roth IRA from age 22 to 67 at 8% grows to approximately:",["$200,000","*~$2,680,000 (all tax-free!)","$500,000","$1,000,000"],"45 years of tax-free growth."),
     ("Traditional IRA vs. Roth IRA choice depends primarily on:",["Account size","*Whether you expect to be in a higher tax bracket now or in retirement","Account provider","Market conditions"],"Tax bracket comparison."),
     ("The general rule of thumb for retirement savings rate is:",["5% of income","*10–15% of income (including employer match)","1% of income","20% of income"],"Savings target."),
     ("The 4% rule suggests retirees can withdraw _____ annually from savings.",["1%","10%","*4% of initial portfolio (adjusted for inflation) with low risk of running out over 30 years","20%"],"Withdrawal rate."),
     ("A $1,000,000 retirement portfolio with the 4% rule provides approximately _____ per year.",["$10,000","$20,000","*$40,000","$100,000"],"Income from savings."),
     ("Social Security replaces approximately _____ of pre-retirement income for average earners.",["10%","25%","*~40% (not enough alone — personal savings are critical)","80%"],"Gap to fill."),
     ("Required Minimum Distributions (RMDs) from traditional accounts start at age:",["59½","65","*73 (as of 2023 SECURE 2.0 Act)","80"],"Mandatory withdrawals."),
     ("A Roth IRA has _____ required minimum distributions.",["Annual RMDs at 73","*No RMDs (Roth IRAs do not require withdrawals at any age during your lifetime)","RMDs at 59½","RMDs at 65"],"Roth advantage."),
     ("Catch-up contributions for those 50+ allow:",["Lower limits","*Additional contributions above the standard limit ($7,500 extra for 401(k), $1,000 extra for IRA in 2024)","No changes","Penalty-free early withdrawal"],"Accelerated saving."),
     ("Early withdrawal from a 401(k) before 59½ incurs:",["No penalty","*10% penalty PLUS income taxes on the withdrawal (few exceptions apply)","Only taxes","5% penalty"],"Expensive mistake."),
     ("Target-date funds automatically:",["Pick individual stocks","*Adjust allocation from aggressive (more stocks) to conservative (more bonds) as the target retirement date approaches","Guarantee returns","Avoid all risk"],"Autopilot investing."),
     ("The biggest factor in retirement savings is:",["Investment selection","Market timing","*Starting early — time for compounding is irreplaceable (20s vs. 30s can mean doubling your final amount)","Picking the right fund"],"Time is dominant."),
     ("Retirement planning combines concepts of:",["Only savings","*Compound interest, annuities, tax optimization, risk management, and inflation protection","Only investing","Only Social Security"],"Comprehensive planning.")]
)
lessons[k]=v

# 4.5
k,v = build_lesson(4,5,"Long-Term Investment Strategies",
    "<h3>Long-Term Investment Strategies</h3>"
    "<h4>Core Strategies</h4>"
    "<ul><li><b>Buy and hold:</b> Invest consistently; ignore short-term fluctuations.</li>"
    "<li><b>Dollar-cost averaging:</b> Fixed amount invested regularly captures market dips.</li>"
    "<li><b>Rebalancing:</b> Periodically adjust portfolio to maintain target allocation.</li>"
    "<li><b>Tax-loss harvesting:</b> Sell losers to offset gains and reduce tax burden.</li></ul>"
    "<p>Key insight: Time in the market beats timing the market.</p>",
    [("Buy and Hold","Strategy of purchasing and holding investments long-term regardless of short-term market volatility."),
     ("Dollar-Cost Averaging","Investing a fixed dollar amount at regular intervals; automatically buys more shares when prices are low."),
     ("Rebalancing","Periodically selling winners and buying laggards to maintain your target asset allocation."),
     ("Tax-Loss Harvesting","Selling investments at a loss to offset capital gains, reducing your tax bill."),
     ("Asset Allocation","The percentage split between stocks, bonds, and cash — the most important investment decision.")],
    [("'Time in the market beats timing the market' means:",["Buy at the bottom","*Staying invested consistently outperforms trying to predict market highs and lows","Only invest when market drops","Wait for perfect conditions"],"Consistency over prediction."),
     ("Dollar-cost averaging helps by:",["Guaranteeing profit","*Buying more shares when prices are low and fewer when high, resulting in a lower average cost per share","Eliminating risk","Only working in up markets"],"Automatic advantage."),
     ("If you invest $500/month and miss the 10 best market days over 20 years, your return drops by roughly:",["5%","*~50% or more (missing just a few key days dramatically hurts long-term returns)","10%","1%"],"Stay invested."),
     ("Rebalancing a 60/40 stock/bond portfolio means:",["Never trading","*Selling some of the outperforming asset and buying the underperforming one to restore 60/40 (sell high, buy low automatically)","Always buying stocks","Always buying bonds"],"Maintain targets."),
     ("Tax-loss harvesting is useful because:",["You want losers","*Selling at a loss offsets capital gains, reducing your tax bill while reinvesting in similar (but not identical) assets","You avoid all taxes","You always profit"],"Tax optimization."),
     ("The S&P 500 has had a positive return over every _____ rolling period in history.",["1-year","5-year","*20-year (no 20-year period has ever lost money — patience is rewarded)","50-year"],"Long-term reliability."),
     ("Asset allocation should shift toward more bonds as you:",["Start investing","Get a raise","*Approach retirement (reducing risk as your time horizon shortens)","Earn more"],"Age-based adjustment."),
     ("A common age-based allocation rule is:",["100% stocks always","*Stock % = 110 − your age (so a 30-year-old: 80% stocks, 20% bonds)","100% bonds always","50/50 always"],"Rule of thumb."),
     ("Compound annual growth rate (CAGR) measures:",["Daily returns","*The smoothed annual return over a period (as if growth were constant each year)","Total return","Only one year"],"Annualized performance."),
     ("$10,000 growing to $40,000 over 20 years has a CAGR of:",["10%","*~7.18% ((40000/10000)^(1/20) − 1)","5%","15%"],"CAGR calculation."),
     ("The impact of inflation on long-term investments means:",["It doesn't matter","*You need real returns (above inflation) — a 10% return with 3% inflation is really ~7% growth","Only cash is affected","Only bonds are affected"],"Real vs. nominal."),
     ("Index fund investing follows the philosophy that:",["Active managers always win","*Most actively managed funds underperform the index over time after fees — so just match the market cheaply","Markets are predictable","Only experts should invest"],"Passive beats active."),
     ("Automatic investment plans help because:",["They pick stocks","*They remove emotion from investing decisions and ensure consistent contributions regardless of market conditions","They time the market","They guarantee returns"],"Remove emotion."),
     ("The biggest enemy of long-term investing is:",["The market","Fees alone","*Emotional decision-making (selling during crashes, chasing hot stocks, stopping contributions during downturns)","Diversification"],"Behavioral risk."),
     ("Value investing means buying:",["Popular stocks","*Stocks trading below their intrinsic value (undervalued by the market) — buy good companies at a discount","Only tech stocks","Only new companies"],"Warren Buffett approach."),
     ("Growth investing focuses on:",["Cheap stocks","*Companies with above-average growth potential (may look expensive but expected to grow into valuation)","Only dividends","Only bonds"],"Future growth potential."),
     ("Dividend reinvestment (DRIP) accelerates growth because:",["Dividends are tax-free","*Automatically buying more shares with dividends creates compound growth on your growth","It reduces risk","It guarantees returns"],"Compounding dividends."),
     ("$10,000 invested at 7% with dividends reinvested vs. not, after 30 years:",["No difference","*Reinvested: ~$76,100 vs. Not reinvested: ~$40,000 + dividends spent (reinvestment nearly doubles outcomes)","Less than 10% difference","Only works for bonds"],"Reinvestment power."),
     ("The three keys to long-term investment success are:",["Market timing, stock picking, leverage","*Start early, invest consistently, stay the course (time + discipline + patience)","Only saving, never investing","Only picking winners"],"Simple but powerful."),
     ("Long-term strategies in financial math emphasize:",["Short-term trading","*The mathematical power of compound interest, consistent contributions, and time as the dominant wealth-building factors","Market prediction","Complexity"],"Math-driven approach.")]
)
lessons[k]=v

# 4.6
k,v = build_lesson(4,6,"Diversification & Portfolio Theory",
    "<h3>Diversification &amp; Portfolio Theory</h3>"
    "<h4>Core Concepts</h4>"
    "<ul><li><b>Diversification:</b> Spreading investments across different assets to reduce risk without sacrificing return.</li>"
    "<li><b>Correlation:</b> How assets move relative to each other. Low or negative correlation provides the best diversification.</li>"
    "<li><b>Modern Portfolio Theory (MPT):</b> Optimal portfolios maximize return for a given level of risk.</li></ul>",
    [("Diversification","Spreading investments across asset classes, sectors, and geographies to reduce risk."),
     ("Correlation","Statistical measure (−1 to +1) of how two assets move relative to each other; lower = better diversification."),
     ("Modern Portfolio Theory","Framework showing how to construct portfolios that maximize expected return for a given risk level."),
     ("Efficient Frontier","Curve showing optimal portfolios that offer the best expected return for each level of risk."),
     ("Systematic vs. Unsystematic Risk","Market risk (can't be diversified away) vs. company-specific risk (can be diversified away).")],
    [("Diversification reduces:",["All risk","*Unsystematic (company-specific) risk — but not systematic (market-wide) risk","No risk","Only stock risk"],"Risk reduction."),
     ("Correlation of +1 between two assets means:",["They're unrelated","They move opposite","*They move exactly together (no diversification benefit)","They double returns"],"Perfect positive."),
     ("Correlation of −1 between two assets means:",["They move together","*They move exactly opposite (perfect diversification — one's loss is the other's gain)","They're unrelated","Both decline"],"Perfect negative."),
     ("For diversification, you want assets with _____ correlation.",["High positive","*Low or negative (they don't move in the same direction at the same time)","Exactly +1","Exactly 0 only"],"Optimal mixing."),
     ("A portfolio of 30 stocks from one sector vs. 30 stocks from different sectors:",["Same diversification","*Different sectors provide much better diversification (sector-specific risks are reduced)","One sector is safer","Number is all that matters"],"Sector diversification."),
     ("International diversification helps because:",["Foreign stocks always gain","*Different economies/markets don't perfectly correlate with US markets, reducing overall portfolio risk","It's required by law","International is safer"],"Geographic spread."),
     ("The efficient frontier shows portfolios that:",["Lose the least","*Offer the highest expected return for each level of risk (or lowest risk for each expected return)","Are only stocks","Are risk-free"],"Optimal combinations."),
     ("A portfolio below the efficient frontier is:",["Optimal","*Sub-optimal (could achieve higher return for the same risk, or same return with less risk)","Impossible","The safest"],"Improvement possible."),
     ("How many stocks are needed to diversify away most unsystematic risk?",["5","10","*~20–30 stocks across different sectors and sizes","100+"],"Practical diversification."),
     ("Adding bonds to a stock portfolio typically:",["Increases risk","*Reduces overall risk while modestly reducing expected return (bonds and stocks have low correlation)","Has no effect","Increases return"],"Traditional diversification."),
     ("A 60% stock / 40% bond portfolio is considered:",["Very aggressive","*Moderate (balances growth potential with stability; suitable for many investors)","Very conservative","Only for retirees"],"Balanced approach."),
     ("During the 2008 financial crisis, diversification across stocks:",["Worked perfectly","*Was limited because ALL stock sectors declined together (systematic risk can't be diversified away)","Was unnecessary","Eliminated all losses"],"Market risk reality."),
     ("REITs (Real Estate Investment Trusts) add diversification because:",["They're stocks","*They provide real estate exposure with different return drivers than traditional stocks and bonds","They're bonds","They're risk-free"],"Alternative asset class."),
     ("Commodities (gold, oil) can diversify a portfolio because:",["They always increase","*They often have low or negative correlation with stocks — gold especially tends to rise during market stress","They're risk-free","They replace stocks"],"Alternative correlation."),
     ("Over-diversification (diworsification) can occur when:",["You own too few stocks","*Adding investments doesn't reduce risk further but increases complexity and fees","You're too diverse","It never occurs"],"Diminishing returns."),
     ("The capital asset pricing model (CAPM) says expected return depends on:",["Only the company","Only diversification","*Beta (systematic risk) — the market rewards bearing systematic risk, not unsystematic risk","Only the market average"],"Risk pricing."),
     ("Index funds automatically provide diversification because they:",["Pick the best stocks","*Hold hundreds or thousands of stocks matching an index, spreading risk broadly at very low cost","Avoid all risk","Guarantee returns"],"Built-in diversification."),
     ("Target-date funds diversify across:",["Only US stocks","*US stocks, international stocks, bonds, and sometimes other assets — automatically rebalancing over time","Only bonds","Only one asset class"],"Comprehensive auto-diversification."),
     ("The key takeaway of portfolio theory is:",["Own one stock","*The whole portfolio's risk and return matter more than any individual investment — diversification improves the risk/return profile","Pick the best stock","Avoid the market"],"Portfolio perspective."),
     ("For financial math, portfolio theory uses:",["Only basic addition","*Statistics (correlation, standard deviation), optimization (efficient frontier), and probability to make better investment decisions","Only guessing","Only one formula"],"Mathematical foundations.")]
)
lessons[k]=v

# 4.7
k,v = build_lesson(4,7,"Case Studies in Investing",
    "<h3>Case Studies in Investing</h3>"
    "<h4>Case 1: Dollar-Cost Averaging vs. Lump Sum</h4>"
    "<p>Alex inherits $60,000. Option A: Invest all now. Option B: $5,000/month for 12 months. Historically, lump sum wins ~66% of the time (market tends to go up), but DCA reduces regret risk.</p>"
    "<h4>Case 2: The Power of Starting Early</h4>"
    "<p>Emily saves $300/month from age 22-32 (10 years, $36,000 total). Mark saves $300/month from age 32-62 (30 years, $108,000 total). At 8%: Emily has $478,000; Mark has $440,000.</p>",
    [("Lump Sum vs. DCA","Investing all at once (lump sum) historically beats DCA ~66% of the time, but DCA reduces timing risk."),
     ("Early Start Advantage","Starting 10 years earlier can outperform even 3× longer investing periods due to compounding."),
     ("Behavioral Investing","Emotional reactions (panic selling, FOMO buying) are the biggest destroyers of investment returns."),
     ("Market Recovery","Markets have recovered from every crash in history; staying invested during downturns is critical."),
     ("Fees Compounded","Even 1% in annual fees can cost hundreds of thousands over a career due to compounding.")],
    [("Historically, lump sum investing beats DCA approximately:",["90% of the time","50% of the time","*~66% of the time","100% of the time"],"Statistical advantage."),
     ("DCA is psychologically beneficial because:",["It always earns more","*It reduces the regret of investing everything right before a market drop","It's risk-free","It eliminates losses"],"Behavioral comfort."),
     ("Emily invests $300/month for 10 years (age 22-32) at 8%. Her contributions total:",["$18,000","$24,000","*$36,000","$48,000"],"Contribution total."),
     ("Mark invests $300/month for 30 years (age 32-62) at 8%. His contributions total:",["$36,000","$72,000","*$108,000","$150,000"],"3× more contributed."),
     ("At age 62, Emily has ~$478K and Mark ~$440K. Emily invested _____ less but has more.",["$10,000","$50,000","*$72,000 (Emily: $36K, Mark: $108K — Emily contributed 1/3 as much!)","$100,000"],"Stunning compounding."),
     ("This case study demonstrates that _____ matters more than _____ in investing.",["Amount, timing","Returns, fees","*Starting early (time), the amount contributed","Stocks, bonds"],"Time dominance."),
     ("Someone who panics and sells during a 30% market crash and buys back after recovery:",["Saves money","Breaks even","*Locks in losses and misses the recovery (selling low and buying high — the worst possible behavior)","Gains more"],"Worst behavior."),
     ("$100,000 at 7% return vs. 6% return over 30 years: difference ≈:",["$10,000","$50,000","*~$225,000 ($761K vs. $574K)","$100,000"],"1% matters enormously."),
     ("An investor paying 1.5% in fund fees vs. 0.1% on $500,000 over 25 years loses approximately:",["$10,000","$50,000","*~$200,000+ to fees","$500,000"],"Fee erosion."),
     ("Warren Buffett famously bet that an index fund would beat hand-picked hedge funds over 10 years. He:",["Lost","Tied","*Won decisively (S&P 500 index fund: 125.8% return vs. hedge funds: ~36%)","Didn't participate"],"Index funds won."),
     ("During the 2008 crash, the S&P 500 dropped ~50%. By 2013 it:",["Was still down","*Had fully recovered and hit new all-time highs (patience was rewarded)","Dropped more","Stayed flat"],"Recovery reality."),
     ("The 'coffee cup' example: $5/day invested at 8% for 40 years grows to:",["$50,000","$100,000","*~$530,000","$1,000,000"],"Small daily savings."),
     ("A couple earning $100K, saving 15%, with employer match 50% up to 6%:",["Saves $15K/year","*Saves $15K + $3K match = $18K/year; after 30 years at 7% ≈ $1.7 million","Saves $10K/year","Cannot determine"],"Realistic scenario."),
     ("Tax-advantaged accounts (Roth IRA) vs. taxable accounts at the same return:",["Same outcome","*Roth grows much more because gains are tax-free (no annual tax drag on dividends/gains)","Taxable is better","Doesn't matter"],"Tax-free compounding."),
     ("The 'lost decade' (2000-2010) for US large-cap stocks:",["Proved indexing doesn't work","*Was recovered by 2013; international diversification helped during that period","Ended investing","Was permanent"],"Diversification + patience."),
     ("Cryptocurrency as an investment:",["Is guaranteed to grow","*Is highly volatile and speculative; should only be a small portion (if any) of a diversified portfolio","Is risk-free","Should be 100% of portfolio"],"High-risk allocation."),
     ("Real estate investment: buying a home to live in is _____ a pure investment.",["Always","Never","*Often not comparable to a pure investment (maintenance, taxes, illiquidity — but provides housing value)","The best"],"Nuanced view."),
     ("The biggest lesson from investing case studies is:",["Timing the market","Picking stocks","*Start early, invest consistently, keep costs low, diversify, and stay the course through ups and downs","Avoiding the market"],"Discipline wins."),
     ("For financial math exams, investment case studies test:",["Only recall","*Calculation of future values, comparison of scenarios, understanding of compound interest, and critical analysis of strategies","Only vocabulary","Only definitions"],"Applied mathematics."),
     ("The fundamental equation of wealth building is:",["Spend more, earn more","*Earn − Spend = Savings → Invest wisely over time → Compound interest builds wealth","Invest everything","Borrow to invest"],"Wealth equation.")]
)
lessons[k]=v

# 4.8
k,v = build_lesson(4,8,"Technology in Investment Analysis",
    "<h3>Technology in Investment Analysis</h3>"
    "<h4>Tools</h4>"
    "<ul><li><b>Robo-advisors:</b> Automated portfolio management (Betterment, Wealthfront). Low cost, diversified.</li>"
    "<li><b>Brokerage platforms:</b> Fidelity, Schwab, Vanguard — research tools, screening, charting.</li>"
    "<li><b>Spreadsheets:</b> Custom modeling, what-if analysis, portfolio tracking.</li>"
    "<li><b>Apps:</b> Mint (budgeting), Personal Capital (net worth), Morningstar (fund research).</li></ul>",
    [("Robo-Advisor","Automated investment platform that builds and manages a diversified portfolio based on your goals and risk tolerance."),
     ("Stock Screener","Tool for filtering stocks based on criteria: market cap, P/E ratio, dividend yield, sector, etc."),
     ("Monte Carlo Simulation","Computer model running thousands of random scenarios to estimate the probability of investment outcomes."),
     ("Backtest","Testing an investment strategy against historical data to see how it would have performed in the past."),
     ("API (Financial Data)","Application Programming Interface for accessing real-time and historical financial data programmatically.")],
    [("Robo-advisors like Betterment and Wealthfront typically charge:",["2%","*~0.25% annually","0%","1.5%"],"Low-cost automated."),
     ("Robo-advisors are best for:",["Day trading","*Beginners or those who want automated, diversified, low-cost portfolio management without active involvement","Only wealthy investors","Only experienced traders"],"Hands-off investing."),
     ("Stock screeners help investors:",["Buy random stocks","*Filter thousands of stocks based on specific criteria (P/E ratio, dividend yield, market cap, sector)","Avoid all stocks","Time the market"],"Research tool."),
     ("P/E ratio (Price-to-Earnings) measures:",["Total return","*How much investors pay per dollar of earnings (lower P/E may indicate undervaluation, but context matters)","Dividend amount","Company size"],"Valuation metric."),
     ("Morningstar ratings (1-5 stars) are based on:",["Popularity","*Past risk-adjusted performance relative to peers (helpful but past performance doesn't guarantee future results)","Future predictions","Only fees"],"Research rating."),
     ("Monte Carlo simulations help investors by:",["Predicting exact outcomes","*Showing the probability distribution of outcomes under various scenarios (e.g., 90% chance of not running out of money)","Guaranteeing returns","Eliminating risk"],"Probability modeling."),
     ("Backtesting a strategy shows:",["Future returns","*How a strategy would have performed using historical data (useful but not predictive)","Guaranteed performance","Nothing useful"],"Historical analysis."),
     ("The limitation of backtesting is:",["It's too expensive","*Past performance doesn't guarantee future results — market conditions change","It's too complex","It always fails"],"Key caveat."),
     ("Excel/Sheets for investment analysis can:",["Only add numbers","*Build custom models, track portfolios, run scenarios, calculate returns, and create amortization tables","Only display data","Only chart prices"],"Versatile tool."),
     ("The XIRR function in Excel calculates:",["Simple interest","*The internal rate of return for cash flows at irregular intervals (true return of investments with varying timing)","Only annual returns","Only bond yields"],"Accurate return calculation."),
     ("Financial news aggregators (Bloomberg, Yahoo Finance) should be used:",["To make every trade","*As information sources, but with awareness that news creates emotional reactions that can harm investment decisions","As the only investment tool","To time the market"],"Information, not action."),
     ("Commission-free trading (Robinhood, Schwab) has:",["No downsides","*Made investing more accessible but can encourage excessive trading (overtrading hurts returns)","Made everyone wealthy","Eliminated all costs"],"Accessibility vs. behavior."),
     ("Fractional shares allow:",["Only full share purchases","*Buying a portion of an expensive stock (e.g., $100 of a $3,000 stock) — making diversification accessible to small investors","Only bond purchases","Only mutual funds"],"Accessibility improvement."),
     ("Personal finance apps like Mint and YNAB help with:",["Stock trading","*Budgeting, expense tracking, and net worth monitoring — the foundation of financial planning","Only taxes","Only investing"],"Financial awareness."),
     ("Financial calculators online (Bankrate, NerdWallet) are useful for:",["Professional trading","*Quick calculations: mortgage payments, retirement projections, debt payoff timelines — accessible to everyone","Only for experts","Only for entertainment"],"Accessible tools."),
     ("Python/R for financial analysis offers:",["Basic calculations only","*Advanced capabilities: data analysis, custom models, Monte Carlo simulations, machine learning for pattern recognition","Nothing beyond Excel","Only for professionals"],"Advanced modeling."),
     ("The key risk of fintech apps that gamify investing is:",["They're too boring","*They can encourage impulsive, frequent trading which typically hurts long-term returns","They charge too much","They're too secure"],"Gamification danger."),
     ("Automated rebalancing by robo-advisors:",["Is unnecessary","*Maintains your target allocation and implements tax-loss harvesting automatically — both improving outcomes","Increases risk","Costs too much"],"Passive optimization."),
     ("For financial math, technology tools enable:",["Only basic calculations","*Complex scenario modeling, real-time analysis, and applying formulas to actual market data — bridging theory and practice","Only theoretical work","Nothing useful"],"Theory to practice."),
     ("The best technology tool for investing is:",["The most expensive","*The one you actually use consistently — simple, low-cost tools used diligently beat complex tools used sporadically","The newest","The most complex"],"Consistency over complexity.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Financial Math Unit 4: wrote {len(lessons)} lessons")
