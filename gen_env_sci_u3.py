#!/usr/bin/env python3
"""Environmental Science Unit 3 – Human Population (7 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "environmental_science_lessons.json")
COURSE = "Environmental Science"

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
k,v = build_lesson(3,1,"Human Population Growth",
    "<h3>Human Population Growth</h3>"
    "<p>World population ~8 billion (2024). Grew slowly for millennia then exponentially after the Industrial Revolution (better agriculture, sanitation, medicine). Current growth rate ~1.0%/yr.</p>"
    "<h4>Key Milestones</h4>"
    "<ul><li>1 billion: ~1800</li><li>2 billion: 1927</li><li>4 billion: 1974</li><li>8 billion: 2022</li></ul>"
    "<p><b>Total Fertility Rate (TFR):</b> Average children per woman. Replacement level ≈ 2.1. TFR varies: Sub-Saharan Africa ~4.5; Europe ~1.5.</p>",
    [("Total Fertility Rate (TFR)","Average number of children born per woman during her lifetime."),
     ("Replacement Level Fertility","TFR of ~2.1 needed to maintain population size without migration."),
     ("Exponential Human Growth","Human population grew slowly for millennia, then surged exponentially after ~1800 due to the Industrial Revolution."),
     ("Demographic Momentum","Tendency for population to continue growing even after fertility drops to replacement, because large young cohorts enter reproductive age."),
     ("Zero Population Growth (ZPG)","When birth rate equals death rate and population size stabilizes.")],
    [("The world population reached 8 billion in approximately:",["2010","*2022","2030","2000"],"Recent milestone."),
     ("Human population grew exponentially starting around:",["5000 BCE","*1800 (Industrial Revolution — improved agriculture, sanitation, and medicine)","500 CE","100 BCE"],"Tech and health advances."),
     ("Replacement level fertility is approximately:",["1.0","*2.1 children per woman","3.0","4.0"],"Accounts for mortality."),
     ("Sub-Saharan Africa's TFR is approximately:",["1.5","2.1","*4.5 (much higher than replacement level)","7.0"],"High fertility region."),
     ("Europe's average TFR is approximately:",["2.1","3.0","*1.5 (below replacement level)","4.5"],"Low fertility region."),
     ("The time it took to go from 1 billion to 2 billion was ~_____ years.",["10","*127 years (1800 to 1927)","50","200"],"First doubling."),
     ("Demographic momentum means:",["Instant population stop","*Population continues growing even after fertility drops because large young cohorts haven't reproduced yet","Population declines immediately","No growth ever"],"Age structure lag."),
     ("Which factor most contributed to the population explosion?",["War","*Improved public health (sanitation, vaccines, antibiotics) and agricultural advances","Education alone","Migration alone"],"Reduced death rates."),
     ("Current global growth rate is approximately:",["3%","0.5%","*~1.0% per year","5%"],"Declining from peak."),
     ("The peak global growth rate (~2.2%) occurred in:",["2020","*~1963","1800","1900"],"Then declining."),
     ("Using the Rule of 70, a 1% growth rate means doubling in:",["35 years","100 years","*70 years","140 years"],"70/1 = 70."),
     ("China's one-child policy (1980–2015) aimed to:",["Increase population","*Slow population growth by limiting families to one child","Double population","No demographic effect"],"Controversial but reduced growth."),
     ("India overtook China as the most populous country in:",["2010","2000","*~2023","2030"],"Recent shift."),
     ("The demographic transition is driven by:",["Only migration","*Industrialization, urbanization, education (especially women's), and improved healthcare","Only war","Only natural disasters"],"Socioeconomic development."),
     ("Population projections for 2100 range from about:",["5–7 billion","*~8.5–10.4 billion (medium estimates ~9.7 billion)","15–20 billion","2–3 billion"],"Depends on TFR trends."),
     ("Thomas Malthus (1798) warned that:",["Food would always be abundant","*Population grows exponentially while food grows arithmetically (leading to inevitable famine)","Population would decline","Technology would solve everything"],"Early population concern."),
     ("Neo-Malthusians argue that:",["Resources are infinite","*Finite resources limit population growth; without controls, famine and conflict will result","Technology solves all problems","Population decline is the threat"],"Modern Malthusian view."),
     ("Cornucopians argue that:",["Resources will always run out","*Technological innovation and market forces will provide solutions to resource scarcity","Population should shrink","Malthus was completely right"],"Optimistic counter-view."),
     ("IPAT equation (I = P × A × T) states that environmental impact depends on:",["Only population","*Population × Affluence × Technology (all three factors)","Only technology","Only affluence"],"Comprehensive model."),
     ("Understanding human population is critical for AP because it underlies:",["Nothing","*Resource use, pollution, habitat loss, energy demand, and virtually every environmental issue","Only one topic","Only demographics"],"Root cause analysis.")]
)
lessons[k]=v

# 3.2
k,v = build_lesson(3,2,"Demographic Transition Model",
    "<h3>Demographic Transition Model (DTM)</h3>"
    "<h4>Four Stages</h4>"
    "<ul><li><b>Stage 1 – Pre-industrial:</b> High birth and death rates → slow/no growth.</li>"
    "<li><b>Stage 2 – Transitional:</b> Death rates drop (better health care); birth rates remain high → rapid growth.</li>"
    "<li><b>Stage 3 – Industrial:</b> Birth rates decline (urbanization, education, family planning) → growth slows.</li>"
    "<li><b>Stage 4 – Post-industrial:</b> Low birth and death rates → slow/zero growth.</li></ul>"
    "<p>Some add <b>Stage 5:</b> Birth rate falls below death rate → population decline (Japan, parts of Europe).</p>",
    [("Demographic Transition Model","Four-stage model showing how populations shift from high birth/death rates to low rates with economic development."),
     ("Stage 1 (Pre-Industrial)","High birth rate + high death rate → little or no population growth."),
     ("Stage 2 (Transitional)","Death rate drops while birth rate stays high → rapid population growth."),
     ("Stage 3 (Industrial)","Birth rate declining; death rate low → growth rate slowing."),
     ("Stage 4 (Post-Industrial)","Low birth + low death rates → slow or zero population growth.")],
    [("In Stage 1 of the DTM, population grows:",["Rapidly","*Slowly or not at all (high birth and death rates largely cancel out)","Negatively","Exponentially"],"Pre-industrial balance."),
     ("Stage 2 sees rapid growth because:",["Both rates drop","*Death rate drops sharply while birth rate remains high","Birth rate increases","Death rate increases"],"Health improvements."),
     ("What causes the death rate drop in Stage 2?",["War","*Improved sanitation, medicine, nutrition, and public health","Fewer births","Education"],"Health revolution."),
     ("In Stage 3, birth rates decline due to:",["Government bans","*Urbanization, education (especially women's), contraception, and economic changes","Higher death rates","Natural causes"],"Modernization effects."),
     ("Stage 4 is characterized by:",["High birth and death rates","*Low birth and low death rates → slow or zero population growth","Rapid growth","High death rate only"],"Developed nations."),
     ("A proposed Stage 5 describes:",["Rapid growth","*Population decline as birth rates fall below death rates (e.g., Japan, Italy, South Korea)","Return to Stage 1","Explosion"],"Below replacement."),
     ("Most of Sub-Saharan Africa is currently in:",["Stage 1","*Stage 2 or early Stage 3 (high birth rates, declining death rates)","Stage 4","Stage 5"],"Transitional phase."),
     ("Most of Western Europe is in:",["Stage 2","Stage 3","*Stage 4 or proposed Stage 5","Stage 1"],"Post-industrial."),
     ("The DTM suggests that economic development leads to:",["Higher birth rates","*Lower birth and death rates (population stabilization)","No change","Higher death rates"],"Development = stability."),
     ("The 'bulge' in population growth (demographic gap) occurs in:",["Stage 1","*Stage 2 (large gap between declining death rate and still-high birth rate)","Stage 4","Stage 5"],"Maximum growth."),
     ("Women's education is strongly correlated with:",["Higher fertility","*Lower fertility rates (educated women tend to have fewer, healthier children)","No fertility change","Male education only"],"Key demographic factor."),
     ("Family planning programs help by:",["Increasing births","*Providing access to contraception and reproductive health education, lowering TFR","Only in cities","Only in some cultures"],"Voluntary fertility reduction."),
     ("The DTM has been criticized because:",["It's never been observed","*It assumes all nations follow the same path; many nations don't fit neatly into the model","It's too simple","All of the above are valid"],"Not universally applicable."),
     ("Some countries have 'stalled' in Stage 2/3 due to:",["Wealth","*Poverty, lack of education, political instability, and limited healthcare access","Being too developed","Climate alone"],"Development barriers."),
     ("Japan's population is declining because:",["High death rate","*TFR (~1.2) is far below replacement (2.1) with aging population","Immigration","High birth rate"],"Stage 5 example."),
     ("An aging population (like Japan) faces challenges including:",["Youth unemployment only","*Labor shortages, increased healthcare costs, pension burdens, and reduced economic productivity","No challenges","Only environmental benefits"],"Dependency ratio rises."),
     ("The dependency ratio compares:",["Birth and death rates","*Non-working-age people (young + old) to working-age population","Only elderly to youth","Immigration to emigration"],"Economic productivity measure."),
     ("Pronatalist policies (encouraging births) have been adopted by:",["Only developing nations","*Countries with declining populations like France, Sweden, and South Korea (through incentives, childcare, parental leave)","Only large nations","No nations"],"Addressing Stage 5."),
     ("The DTM is useful for AP because it:",["Is just theory","*Connects industrialization, public health, urbanization, education, and population dynamics in a testable framework","Only applies to Europe","Is outdated"],"Integrative model."),
     ("Understanding the DTM helps predict:",["Nothing","*Future population trends, resource needs, and environmental impacts for countries at different stages","Only birth rates","Only death rates"],"Planning tool.")]
)
lessons[k]=v

# 3.3
k,v = build_lesson(3,3,"Age Structure Diagrams",
    "<h3>Age Structure Diagrams</h3>"
    "<p>Population pyramids show age and sex distribution. Shape predicts future growth:</p>"
    "<ul><li><b>Expansive (wide base):</b> Rapid growth — many young people (Nigeria, Ethiopia).</li>"
    "<li><b>Stationary (column-shaped):</b> Stable — roughly equal numbers at each age (US, Australia).</li>"
    "<li><b>Constrictive (narrow base):</b> Declining — fewer young than middle-aged (Japan, Germany, Italy).</li></ul>"
    "<p>Diagrams reveal <b>dependency ratio</b> and <b>demographic momentum</b> — critical for policy planning.</p>",
    [("Age Structure Diagram","Graph showing population distribution by age and sex; also called population pyramid."),
     ("Expansive Pyramid","Wide base (many young); indicates rapid population growth."),
     ("Stationary Pyramid","Column shape (equal ages); indicates stable population."),
     ("Constrictive Pyramid","Narrow base (fewer young); indicates declining population."),
     ("Dependency Ratio","Ratio of dependents (age 0–14 and 65+) to working-age population (15–64).")],
    [("An expansive (pyramid-shaped) age structure indicates:",["Declining population","*Rapid population growth (large proportion of young people)","Stable population","No growth"],"Wide base."),
     ("A constrictive (urn-shaped) age structure indicates:",["Rapid growth","*Declining population (fewer young than middle-aged)","Stable","Unchanged"],"Narrow base."),
     ("A stationary (column-shaped) age structure indicates:",["Rapid growth","Rapid decline","*Relatively stable population (approximately equal numbers at each age)","Explosion"],"Near-equal bars."),
     ("Nigeria's age structure is typically:",["Column-shaped","*Expansive/pyramid-shaped (very wide base; high proportion of youth)","Constrictive","Inverted"],"Young, rapidly growing."),
     ("Japan's age structure is typically:",["Expansive","*Constrictive (narrow base; aging population; more elderly than young)","Stationary exactly","Wide at base"],"Aging, declining."),
     ("Age structure diagrams are split by:",["Income","*Sex (males on one side, females on the other, with age groups on the vertical axis)","Education","Ethnicity"],"Standard format."),
     ("The dependency ratio includes people aged:",["Only 20–60","*0–14 and 65+ (dependents) compared to 15–64 (working age)","Only 0–14","Only 65+"],"Non-working / working."),
     ("A high dependency ratio means:",["More workers","*Fewer working-age people supporting more dependents → economic strain","No change","Fewer dependents"],"Economic challenge."),
     ("Demographic momentum is visible in pyramids with:",["Narrow bases","*Wide bases (large young cohorts will grow into reproductive age even if TFR drops)","Very old populations","No pattern"],"Built-in future growth."),
     ("A country with 40% of its population under age 15:",["Will shrink soon","*Has significant demographic momentum and likely continued growth even with declining fertility","Is in Stage 4","Is in Stage 5"],"Growth pipeline."),
     ("The baby boom (1946–1964 in the US) appears on a pyramid as:",["Nothing","*A bulge in the middle to upper age groups (now in their 60s–80s)","A wide base","A narrow top"],"Generational effect."),
     ("Reading age structure diagrams for AP requires noting:",["Colors only","*Shape (expansive/stationary/constrictive), dependency ratio, and demographic momentum implications","Only total number","Only gender ratio"],"Multiple interpretations."),
     ("China's one-child policy is visible in its pyramid as:",["Wider base","*A narrowing in younger cohorts (smaller generations born after 1980)","No visible effect","Larger elderly population only"],"Policy imprint."),
     ("Aging populations face pandemic vulnerability because:",["Young people are at risk only","*Elderly are more susceptible to disease; higher healthcare demand (COVID-19 illustrated this)","Aging is healthy","No connection"],"Health system stress."),
     ("A country planning for education needs should examine:",["Only the top of the pyramid","*The base (ages 0–14) to project student enrollment and school infrastructure needs","Only the middle","Only the sides"],"Education planning."),
     ("For retirement planning, analysts focus on:",["The base","*The proportion approaching age 65+ compared to the working-age population (pension sustainability)","Only youth","Only immigrants"],"Economic planning."),
     ("Urbanization tends to _____ the base of the pyramid.",["Widen","*Narrow (urban populations have lower fertility rates than rural populations)","Not change","Separate"],"Urban fertility effect."),
     ("Immigration can alter a host country's pyramid by:",["Not changing it","*Adding working-age adults (often widening the middle of the pyramid)","Only adding elderly","Only adding children"],"Selective migration."),
     ("Which data source is used to construct age structure diagrams?",["Guessing","*Census data and demographic surveys (counting population by age and sex)","Only birth records","Only death records"],"Census-based."),
     ("For the AP exam, you may be asked to:",["Only name shapes","*Interpret a given pyramid, predict future growth, and recommend policy based on demographic data","Only calculate growth rate","Only describe Stage 2"],"Applied analysis.")]
)
lessons[k]=v

# 3.4
k,v = build_lesson(3,4,"Carrying Capacity",
    "<h3>Carrying Capacity &amp; Human Population</h3>"
    "<p>Earth's carrying capacity for humans is debated. Estimates range from 4 to 16 billion depending on consumption levels and technology.</p>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>Ecological footprint:</b> Area of productive land/water needed to sustain a person's lifestyle.</li>"
    "<li><b>Overshoot:</b> Humanity currently uses ~1.7 Earths' worth of resources per year.</li>"
    "<li><b>Earth Overshoot Day:</b> Date humanity has used more resources than Earth can regenerate that year (moves earlier each decade).</li></ul>",
    [("Ecological Footprint","Total area of productive land and water required to support a person's resource consumption and waste."),
     ("Earth Overshoot Day","Annual date when humanity has consumed more resources than Earth can regenerate in a year."),
     ("Biocapacity","Earth's biological ability to regenerate resources and absorb waste in a given year."),
     ("Overshoot","When resource consumption exceeds biocapacity; humanity currently uses ~1.7 Earths of resources."),
     ("Per Capita Ecological Footprint","Average footprint per person; varies enormously by country (US ~8 gha vs. India ~1.2 gha).")],
    [("Earth's carrying capacity for humans is estimated between:",["1–2 billion","*4–16 billion (widely debated; depends on consumption and technology assumptions)","50–100 billion","Exactly 10 billion"],"No agreed number."),
     ("Ecological footprint measures:",["Only land area","*Total productive land and water needed to sustain a person's lifestyle and absorb waste","Only carbon","Only food"],"Comprehensive resource demand."),
     ("Earth Overshoot Day occurs when:",["Resources increase","*Humanity has consumed more resources than Earth can regenerate that year","Resources are abundant","The year ends"],"We're in debt."),
     ("In recent years, Earth Overshoot Day has fallen in approximately:",["December","*Late July to early August (meaning we use ~1.7 Earths/year)","January","Never"],"Moves earlier."),
     ("If everyone lived like the average American, we would need approximately:",["1 Earth","*~5 Earths of resources","2 Earths","10 Earths"],"High consumption."),
     ("If everyone lived like the average Indian, we would need:",["5 Earths","*Less than 1 Earth (~0.7 Earths)","2 Earths","3 Earths"],"Low per-capita footprint."),
     ("Biocapacity is the ability of ecosystems to:",["Only grow crops","*Regenerate resources and absorb waste (measured in global hectares)","Only produce energy","Only clean water"],"Earth's regenerative capacity."),
     ("The US per capita ecological footprint is approximately:",["1 gha","3 gha","*~8 gha (global hectares)","0.5 gha"],"High consumption."),
     ("Factors determining carrying capacity include:",["Only food","*Food, water, energy, waste absorption capacity, technology, and per-capita consumption","Only water","Only space"],"Multiple limitations."),
     ("Technology can increase carrying capacity by:",["Magic","*Improving agricultural yields, water efficiency, renewable energy, and resource recycling","Eliminating all limits","Having no effect"],"Extends but doesn't remove limits."),
     ("The Green Revolution increased food production through:",["No change","*High-yield crop varieties, irrigation, fertilizers, and pesticides","Reducing farming","Only organic methods"],"Agricultural intensification."),
     ("Critics of the Green Revolution note it:",["Was perfect","*Increased environmental degradation (soil depletion, water use, pesticide pollution, biodiversity loss)","Had no downsides","Only helped the rich"],"Trade-offs."),
     ("The IPAT model assesses human impact using:",["Only population","*I = P × A × T (Population × Affluence × Technology)","Only technology","Only affluence"],"Comprehensive framework."),
     ("Reducing ecological footprint can be achieved by:",["Only population reduction","*Lower consumption, renewable energy, sustainable agriculture, reduced waste, and efficient technology","Only moving to cities","Only education"],"Multiple strategies."),
     ("Water scarcity affects approximately _____ of the world's population seasonally.",["10%","*~4 billion people (about half)","1%","Nobody"],"Major global challenge."),
     ("The concept of 'limits to growth' was popularized by a _____ report.",["2020","*1972 Club of Rome (Meadows et al.) 'The Limits to Growth' study","1800","1950"],"Influential model."),
     ("Ecological debt occurs when a country's footprint exceeds its:",["GDP","*Biocapacity (it consumes more resources than its ecosystems can regenerate)","Population","Carbon credits"],"Living beyond means."),
     ("Reducing food waste would help because roughly _____ of food produced is wasted globally.",["5%","*~30-40%","1%","90%"],"Enormous inefficiency."),
     ("Carrying capacity is not fixed because:",["It's a law","*Technology, climate, resource depletion, and consumption patterns all change it over time","It never changes","It only increases"],"Dynamic concept."),
     ("For the AP exam, students should connect carrying capacity to:",["Nothing","*Resource use, ecological footprint, sustainability, population policy, and environmental impact","Only vocabulary","Only one unit"],"Integrative concept.")]
)
lessons[k]=v

# 3.5
k,v = build_lesson(3,5,"Urbanization & Land Use",
    "<h3>Urbanization &amp; Land Use</h3>"
    "<p>Over 56% of the world's population lives in cities (projected 68% by 2050). Urbanization concentrates consumption but can also create efficiencies.</p>"
    "<h4>Impacts</h4>"
    "<ul><li><b>Urban heat island:</b> Cities are warmer than surroundings (concrete + less vegetation + waste heat).</li>"
    "<li><b>Sprawl:</b> Low-density, car-dependent expansion converts farmland/habitat.</li>"
    "<li><b>Smart growth:</b> Compact, mixed-use, transit-oriented development to reduce sprawl.</li></ul>",
    [("Urban Heat Island","Urban areas being warmer than surrounding rural areas due to concrete, asphalt, reduced vegetation, and waste heat."),
     ("Urban Sprawl","Low-density, car-dependent suburban expansion that converts farmland and natural habitat."),
     ("Smart Growth","Urban planning strategy: compact, walkable, mixed-use, transit-oriented development to reduce sprawl."),
     ("Impervious Surfaces","Roads, rooftops, and pavement that prevent water infiltration → increased runoff and flooding."),
     ("Urbanization","Movement of people from rural to urban areas; >56% of the world's population now lives in cities.")],
    [("What percentage of the world's population currently lives in cities?",["25%","*>56% (projected to reach 68% by 2050)","10%","90%"],"Majority are urban."),
     ("Urban heat island effect is caused by:",["Natural processes","*Dark surfaces (asphalt, concrete), reduced vegetation, waste heat from buildings/vehicles, and less evapotranspiration","Ocean currents","Forest cover"],"Concrete jungle."),
     ("Urban sprawl is characterized by:",["Dense cities","*Low-density, car-dependent, single-use suburban expansion","Compact development","Transit-oriented growth"],"Inefficient land use."),
     ("Environmental impacts of urban sprawl include:",["Only noise","*Habitat loss, increased car emissions, higher energy use, loss of agricultural land, and increased runoff","Only traffic","No impacts"],"Multiple harms."),
     ("Smart growth principles include:",["More highways","*Compact development, mixed land use, public transit, walkability, and open space preservation","Only suburban expansion","Only industrial zones"],"Sustainable urban planning."),
     ("Impervious surfaces increase:",["Water infiltration","*Stormwater runoff, flooding, and non-point-source water pollution","Groundwater recharge","Vegetation growth"],"Water flows over, not into ground."),
     ("Green infrastructure in cities includes:",["More concrete","*Green roofs, permeable pavements, rain gardens, urban forests, and bioswales","More highways","More parking"],"Nature-based solutions."),
     ("Urbanization can be beneficial because cities:",["Always harm environment","*Can be more energy-efficient per capita — higher density reduces transportation needs and enables shared services","Use more resources always","Have no advantages"],"Efficiency of density."),
     ("Transportation accounts for approximately _____ of US greenhouse gas emissions.",["5%","*~29% (the largest sector)","50%","1%"],"Major emission source."),
     ("Transit-oriented development centers housing and services around:",["Highways","*Public transit stations (reducing car dependency)","Airports only","Industrial zones"],"Walkable transit hubs."),
     ("Agricultural land loss to urbanization threatens:",["Nothing","*Food security and local food production (prime farmland is often near cities)","Only aesthetics","Only wildlife"],"Paving over farms."),
     ("Brownfields are:",["Green spaces","*Abandoned or underused industrial/commercial sites, often contaminated, that can be redeveloped","Agricultural land","Parking lots only"],"Urban redevelopment opportunity."),
     ("Infill development (building on vacant urban lots) helps by:",["Increasing sprawl","*Reducing sprawl by using existing urban land more efficiently","Decreasing density","Increasing highways"],"Building inward."),
     ("Urban parks and green spaces provide:",["No benefits","*Improved air quality, reduced heat island, mental health benefits, stormwater management, and biodiversity habitat","Only recreation","Only aesthetics"],"Ecosystem services."),
     ("Megacities (>10 million people) face challenges including:",["No challenges","*Water supply, waste management, air quality, transportation, and housing affordability","Only water","Only traffic"],"Scale of urban issues."),
     ("The concept of 'walkability' promotes:",["Car dependence","*Mixed-use neighborhoods where daily needs are within walking distance, reducing emissions and improving health","Only suburban living","Only highway expansion"],"Healthy, low-carbon living."),
     ("Land use zoning can reduce environmental impact by:",["Mixing pollution sources","*Separating incompatible uses, protecting open space, and directing growth to appropriate areas","Having no rules","Only industrial expansion"],"Planning tool."),
     ("Heat-related illness in cities is worsened by:",["Green spaces","*Urban heat island effect, especially during heat waves (concrete retains heat; lack of shade)","Trees","Parks"],"Health impact."),
     ("Sustainable urban planning for AP connects to:",["Nothing","*Energy use, water management, air quality, biodiversity, transportation, and environmental justice","Only one topic","Only building codes"],"Integrative concept."),
     ("Cities that successfully reduce their environmental footprint often:",["Expand highways","*Invest in public transit, green buildings, renewable energy, waste reduction, and urban green spaces","Only build taller","Only restrict growth"],"Multi-strategy approach.")]
)
lessons[k]=v

# 3.6
k,v = build_lesson(3,6,"Case Studies: Population Policy",
    "<h3>Case Studies: Population Policy</h3>"
    "<h4>China's One-Child Policy (1980–2015)</h4>"
    "<p>Reduced TFR from ~6 to ~1.7. Now facing aging crisis; shifted to two-child (2016) then three-child (2021) policy.</p>"
    "<h4>India</h4>"
    "<p>Voluntary family planning, women's education. TFR dropped from ~6 (1960) to ~2.0 (2023). Now world's most populous country.</p>"
    "<h4>Kerala Model</h4>"
    "<p>Indian state achieved low TFR (~1.6) through high female literacy (97%), good healthcare, without coercion.</p>",
    [("China One-Child Policy","1980–2015 policy limiting most families to one child; reduced TFR but caused demographic imbalance."),
     ("Kerala Model","Indian state that achieved low fertility (~1.6 TFR) through female education and healthcare, without coercion."),
     ("Pronatalist Policy","Government policies encouraging higher birth rates (e.g., France, Sweden, South Korea offering incentives)."),
     ("Antinatalist Policy","Government policies discouraging births/reducing population growth (e.g., China's one-child policy)."),
     ("Empowerment of Women","Education, economic opportunities, and reproductive rights for women — the most effective way to reduce fertility.")],
    [("China's one-child policy was in effect from:",["1960–1990","*1980–2015","2000–2020","1950–1980"],"35-year policy."),
     ("China's TFR dropped from ~6 to approximately _____ under the one-child policy.",["3.0","*~1.7 (well below replacement)","2.1","4.0"],"Dramatic decline."),
     ("A major consequence of China's one-child policy was:",["Population explosion","*Aging population, gender imbalance (preference for boys), and a shrinking workforce","No demographic change","Higher birth rates"],"Unintended consequences."),
     ("China shifted to a three-child policy in _____ to address demographic challenges.",["2010","*2021","2000","2025"],"Policy reversal."),
     ("India's approach to population control has been primarily:",["Forced sterilization only","*Voluntary family planning, women's education, and healthcare improvements","No policy at all","One-child policy"],"Democratic approach."),
     ("India's TFR dropped from ~6 (1960) to approximately _____ by 2023.",["4.0","*~2.0 (near replacement level)","3.5","1.0"],"Significant decline."),
     ("The Kerala model demonstrates that low fertility can be achieved through:",["Coercive policy","*High female literacy (~97%), good healthcare, and women's empowerment — without coercive measures","War","Poverty"],"Education-based approach."),
     ("Kerala's TFR is approximately:",["3.0","*~1.6 (well below India's national average and below replacement)","2.5","4.0"],"Remarkably low."),
     ("Pronatalist policies in France include:",["Birth restrictions","*Generous parental leave, childcare subsidies, tax benefits for families, and family allowances","Anti-immigration policy","No incentives"],"Encouraging births."),
     ("South Korea's TFR has dropped to ~0.7, which is:",["Average globally","*One of the lowest in the world and far below replacement","Above replacement","Normal for Asia"],"Demographic crisis."),
     ("Singapore shifted from anti-natalist to pro-natalist policies because:",["Population was too large","*TFR dropped below replacement; concerns about aging workforce and economic sustainability","Immigration was too high","No reason"],"Policy reversal."),
     ("The most effective way to reduce fertility rates globally is:",["Forced sterilization","*Educating and empowering women (girls' education, economic opportunities, reproductive choice)","Only contraception distribution","Only economic growth"],"Research consensus."),
     ("Unmet need for family planning means:",["Everyone has access","*Women who want to delay or prevent pregnancy but lack access to contraception (~218 million women globally)","No one wants contraception","Only in developed nations"],"Access gap."),
     ("Coercive population policies raise ethical concerns about:",["Nothing","*Individual rights, reproductive freedom, gender equality, and human rights","Only economics","Only demographics"],"Rights-based critique."),
     ("Iran's population policy shifted from:",["Pro-natalist to pro-natalist","*Encouraging large families (1980s) to one of the most successful family planning programs, then back to pro-natalist","No changes ever","Anti-natalist always"],"Policy swings."),
     ("Japan addresses population decline through:",["Encouraging immigration aggressively","*Automation/robotics, modest pro-natalist incentives, and cautious immigration reform","Forced births","No action"],"Technology-focused."),
     ("Population policies are most successful when they:",["Use force","*Are voluntary, culturally sensitive, include women's empowerment, and address economic factors","Ignore culture","Focus only on men"],"Comprehensive approach."),
     ("The relationship between population policy and environment is:",["Unrelated","*Direct: lower population growth → less resource demand, pollution, and habitat loss → reduced environmental impact","Only indirect","Irrelevant"],"Core connection."),
     ("For AP, population policy case studies test understanding of:",["Only China","*Demographic transitions, policy approaches (voluntary vs. coercive), social impacts, and environmental connections","Only India","Only developed nations"],"Broad analysis."),
     ("A lesson from all these case studies is that:",["One policy fits all","*Context matters — effective population policy must account for culture, economics, education, and women's rights","Only coercion works","Only wealth matters"],"Nuanced understanding.")]
)
lessons[k]=v

# 3.7
k,v = build_lesson(3,7,"AP Prep: Demographic Calculations",
    "<h3>AP Prep: Demographic Calculations</h3>"
    "<h4>Key Formulas</h4>"
    "<ul><li><b>Growth rate (r):</b> r = (CBR − CDR) / 10 (gives %; CBR and CDR per 1,000).</li>"
    "<li><b>Doubling time:</b> t = 70 / r (Rule of 70).</li>"
    "<li><b>Rate of natural increase:</b> (births − deaths) / total population × 100.</li>"
    "<li><b>Net migration rate:</b> (immigration − emigration) / population × 1,000.</li>"
    "<li><b>Crude birth rate / Crude death rate:</b> births or deaths per 1,000 people per year.</li></ul>",
    [("Crude Birth Rate (CBR)","Number of live births per 1,000 people per year."),
     ("Crude Death Rate (CDR)","Number of deaths per 1,000 people per year."),
     ("Rate of Natural Increase","(CBR − CDR) / 10 → expressed as a percentage. Does not include migration."),
     ("Net Migration Rate","(Immigration − Emigration) per 1,000 people per year."),
     ("Infant Mortality Rate","Number of infant deaths (<1 year old) per 1,000 live births; key indicator of development.")],
    [("If CBR = 30 and CDR = 10 (both per 1,000), the rate of natural increase is:",["40%","*2.0% ((30-10)/10 = 2.0%)","20/1000","0.2"],"(CBR-CDR)/10."),
     ("Using Rule of 70 with r = 2%, doubling time is:",["140 years","*35 years (70/2)","70 years","20 years"],"Quick calculation."),
     ("If CBR = 45/1000 and CDR = 15/1000, doubling time is:",["70 years","35 years","*~23 years (r = 3%; 70/3 ≈ 23.3)","10 years"],"r = (45-15)/10 = 3%."),
     ("Net migration rate is calculated as:",["CBR − CDR","*(Immigration − Emigration) / population × 1,000","Birth rate only","Death rate only"],"Migration contribution."),
     ("A country with CBR=12, CDR=11, and net migration=+3/1000 has total growth rate of:",["1/1000","*4/1000 = 0.4% (natural increase 1/1000 + migration 3/1000)","12/1000","3/1000"],"Natural + migration."),
     ("Infant mortality rate is:",["Deaths per 1,000 people","*Deaths of infants under age 1 per 1,000 live births","Birth rate of infants","Child mortality only"],"Infant-specific measure."),
     ("A high infant mortality rate (>50/1000) typically indicates:",["High development","*Low development, poor healthcare, and inadequate nutrition/sanitation","No correlation","High education"],"Development indicator."),
     ("Life expectancy at birth in developed nations is typically:",["40–50 years","*75–85+ years","60–65 years","90–100 years"],"High healthcare access."),
     ("Life expectancy at birth in least developed nations may be:",["80+ years","*50–65 years (lower due to disease, poverty, limited healthcare)","90 years","Same as developed"],"Development gap."),
     ("If a country has 500,000 births, 200,000 deaths in a population of 25 million, CBR is:",["500","*20/1000 (500,000/25,000,000 × 1000 = 20)","200","50"],"CBR calculation."),
     ("In the same country (500K births, 200K deaths, 25M pop), CDR is:",["500","20","*8/1000 (200,000/25,000,000 × 1000 = 8)","200"],"CDR calculation."),
     ("And the rate of natural increase would be:",["28%","*1.2% ((20-8)/10 = 1.2%)","20%","8%"],"RNI calculation."),
     ("TFR measures:",["Births per year","*Average number of children per woman during her lifetime","Deaths per year","Population per area"],"Fertility measure."),
     ("A TFR of 6 means on average each woman has:",["2 children","*6 children during her lifetime","106 children","6 per year"],"Lifetime total."),
     ("Population density is:",["Total population","*People per unit area (e.g., per km²)","Birth rate","Growth rate"],"Spatial measure."),
     ("Arithmetic population density differs from physiological density because physiological uses only:",["Total area","*Arable (farmable) land area — a better indicator of population pressure on food production","Water area","Urban area"],"Agricultural pressure."),
     ("A population pyramid with equal-width bars at all ages predicts:",["Rapid growth","Rapid decline","*Stable population (zero or near-zero growth)","Explosion"],"Column shape."),
     ("If a population of 1 million grows at 3% per year, next year it will be approximately:",["1,300,000","*1,030,000 (1,000,000 × 1.03)","1,003,000","2,000,000"],"3% of 1M = 30,000."),
     ("For AP free-response questions on demographics, students should:",["Only state facts","*Show all calculations, label formulas, interpret results, and connect to environmental impacts","Only draw diagrams","Only give final answers"],"Full analysis required."),
     ("Mastering demographic calculations is essential because they appear in:",["No AP questions","*Multiple-choice and free-response questions across several AP Environmental Science units","Only one question","Only extra credit"],"High-frequency topic.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 3: wrote {len(lessons)} lessons")
