#!/usr/bin/env python3
"""Environmental Science Unit 5 – Energy (6 lessons)."""
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

# 5.1
k,v = build_lesson(5,1,"Fossil Fuels",
    "<h3>Fossil Fuels</h3>"
    "<p>Coal, oil (petroleum), and natural gas supply ~80% of global energy. Formed from ancient organic matter over millions of years.</p>"
    "<h4>Impacts</h4>"
    "<ul><li><b>CO₂ emissions:</b> Leading cause of climate change.</li>"
    "<li><b>Air pollution:</b> SO₂, NOₓ, particulates → smog, acid rain, respiratory illness.</li>"
    "<li><b>Extraction damage:</b> Mountaintop removal, oil spills, fracking (hydrofracturing) → water contamination.</li></ul>"
    "<p>Coal is dirtiest per unit energy; natural gas cleanest fossil fuel (~50% less CO₂ than coal). Oil used mostly for transportation.</p>",
    [("Fossil Fuels","Coal, oil, and natural gas; nonrenewable energy sources formed from ancient organic matter over millions of years."),
     ("Coal","Solid fossil fuel; dirtiest per unit energy; used mainly for electricity generation; produces more CO₂, SO₂, and particulates."),
     ("Natural Gas","Cleanest-burning fossil fuel (~50% less CO₂ than coal); primarily methane (CH₄); growing share of energy."),
     ("Fracking (Hydraulic Fracturing)","Injecting high-pressure fluid into rock to fracture it and release oil/gas; concerns about water contamination and earthquakes."),
     ("Acid Rain","Precipitation with pH < 5.6 caused by SO₂ and NOₓ from fossil fuel combustion reacting with atmospheric water.")],
    [("Fossil fuels currently supply approximately _____ of global energy.",["50%","*~80%","25%","10%"],"Dominant energy source."),
     ("Coal is the _____ fossil fuel in terms of CO₂ emissions per unit of energy.",["Cleanest","*Dirtiest (highest CO₂, SO₂, and particulate emissions per unit energy)","Same as others","Only fuel used"],"Most polluting."),
     ("Natural gas produces approximately _____ less CO₂ than coal per unit energy.",["10%","25%","*~50%","90%"],"Cleaner but still fossil."),
     ("Oil (petroleum) is primarily used for:",["Electricity generation","*Transportation (gasoline, diesel, jet fuel; ~90% of transport fuel)","Heating only","Only plastics"],"Transport fuel."),
     ("Fracking involves:",["Surface mining","*Injecting high-pressure fluid underground to fracture rock and release trapped oil and gas","Only drilling","Solar energy"],"Extraction technique."),
     ("Environmental concerns about fracking include:",["None","*Water contamination (chemicals in fracking fluid), induced seismicity (earthquakes), methane leakage, and water use","Only noise","Only cost"],"Multiple issues."),
     ("Mountaintop removal mining for coal:",["Is harmless","*Blasts off mountain peaks to access coal seams, destroying ecosystems, filling valleys with debris","Only affects summits","Is rare"],"Destructive extraction."),
     ("SO₂ and NOₓ from fossil fuel combustion cause:",["No problems","*Acid rain, smog, respiratory disease, and damage to ecosystems and buildings","Only good smells","Only local effects"],"Air pollution."),
     ("Acid rain has a pH below:",["7.0","*5.6 (normal rain is ~5.6 due to dissolved CO₂; acid rain is more acidic)","4.0","Neutral"],"Definition threshold."),
     ("Particulate matter (PM2.5) from fossil fuels causes:",["Nothing","*Respiratory and cardiovascular disease (particles small enough to enter lungs and bloodstream)","Only dust","Only visibility reduction"],"Health danger."),
     ("The greenhouse effect is enhanced by fossil fuel CO₂ because:",["CO₂ blocks sunlight","*CO₂ traps infrared radiation (heat) re-emitted from Earth's surface, warming the atmosphere","CO₂ is cooling","No connection"],"Climate mechanism."),
     ("Carbon capture and storage (CCS) aims to:",["Release more CO₂","*Capture CO₂ from power plants and store it underground, preventing atmospheric release","Only at small scale","Increase emissions"],"Mitigation technology."),
     ("Limitations of CCS include:",["None","*High cost, energy penalty (reduces plant efficiency), limited storage capacity, and potential leakage","It's free","It's widely deployed"],"Not yet viable at scale."),
     ("Methane (CH₄) from natural gas is a potent greenhouse gas because it:",["Is not a greenhouse gas","*Traps ~80× more heat than CO₂ over 20 years (though shorter-lived)","Is identical to CO₂","Only affects ozone"],"Short-lived but powerful."),
     ("Oil spills devastate marine ecosystems by:",["Having no effect","*Coating organisms, poisoning food chains, destroying habitats (e.g., Deepwater Horizon, Exxon Valdez)","Only affecting surface","Only for a day"],"Long-lasting damage."),
     ("Coal ash (fly ash) contains:",["Nothing harmful","*Heavy metals (arsenic, mercury, lead) that can contaminate water and soil if improperly stored","Only calcium","Only minerals"],"Toxic waste."),
     ("Mercury emissions from coal plants are dangerous because mercury:",["Is harmless","*Bioaccumulates and biomagnifies in food chains, causing neurological damage (especially in fish → humans)","Only affects fish","Decomposes quickly"],"Persistent neurotoxin."),
     ("The concept of 'stranded assets' refers to:",["Lost valuables","*Fossil fuel reserves that may never be extracted if climate policies limit emissions (financially devalued)","Only abandoned mines","Only empty wells"],"Economic risk."),
     ("Transitioning from fossil fuels is challenging because:",["Alternatives don't exist","*Fossil fuels are deeply embedded in infrastructure, economies, and political systems (energy inertia)","No one wants to change","Alternatives are worse"],"Systemic lock-in."),
     ("For the AP exam, students should evaluate fossil fuels in terms of:",["Only energy output","*Environmental impacts (air, water, climate), extraction methods, alternatives, and policy options","Only cost","Only history"],"Comprehensive analysis.")]
)
lessons[k]=v

# 5.2
k,v = build_lesson(5,2,"Nuclear Energy",
    "<h3>Nuclear Energy</h3>"
    "<p><b>Fission:</b> Splitting heavy atoms (uranium-235, plutonium-239) releases enormous energy. Provides ~10% of global electricity with near-zero CO₂ during operation.</p>"
    "<h4>Pros &amp; Cons</h4>"
    "<ul><li><b>Pros:</b> High energy density, low carbon, reliable baseload power.</li>"
    "<li><b>Cons:</b> Radioactive waste (remains hazardous for thousands of years), meltdown risk (Chernobyl, Fukushima), high construction costs, uranium mining impacts.</li></ul>",
    [("Nuclear Fission","Splitting heavy nuclei (U-235, Pu-239) to release energy; used in current nuclear power plants."),
     ("Radioactive Waste","Spent nuclear fuel and contaminated materials; high-level waste remains hazardous for thousands of years."),
     ("Half-Life","Time for half of a radioactive substance to decay; Pu-239 has a half-life of ~24,000 years."),
     ("Nuclear Meltdown","Uncontrolled reactor core overheating; e.g., Chernobyl (1986), Fukushima (2011)."),
     ("Nuclear Fusion","Combining light nuclei (hydrogen) to release energy; powers the sun but not yet commercially viable on Earth.")],
    [("Nuclear fission involves:",["Combining atoms","*Splitting heavy atoms (uranium-235) to release enormous energy","Burning fuel","Solar collection"],"Splitting atoms."),
     ("Nuclear power provides approximately _____ of global electricity.",["50%","1%","*~10%","25%"],"Significant share."),
     ("CO₂ emissions from nuclear power during operation are:",["Very high","Moderate","*Near zero (no fossil fuel combustion during electricity generation)","The same as coal"],"Low-carbon energy."),
     ("The main challenge of nuclear waste is:",["It's not radioactive","*It remains hazardous for thousands to hundreds of thousands of years (no permanent disposal solution exists)","It's easy to store","It decomposes quickly"],"Long-lasting hazard."),
     ("Half-life of plutonium-239 is approximately:",["10 years","100 years","*~24,000 years","1 year"],"Very long decay."),
     ("The Chernobyl disaster (1986) was caused by:",["Earthquake","*A flawed reactor design and operator error during a safety test, leading to a steam explosion and fire","Flooding","Terrorism"],"Design + human error."),
     ("The Fukushima disaster (2011) was triggered by:",["Operator error","*A massive earthquake and tsunami that knocked out cooling systems, causing meltdowns in three reactors","A design flaw only","Lightning"],"Natural disaster trigger."),
     ("Uranium mining can cause:",["No environmental damage","*Habitat destruction, water contamination, radioactive tailings, and health risks for miners","Only minor dust","Only aesthetic damage"],"Extraction impacts."),
     ("Energy density of nuclear fuel compared to fossil fuels is:",["Much lower","About the same","*Much higher (one kg of uranium has ~2 million times the energy of one kg of coal)","Slightly higher"],"Enormous energy per mass."),
     ("Nuclear power plants provide _____ power.",["Intermittent","Peak-only","*Reliable baseload (operate 24/7 regardless of weather)","Only seasonal"],"Constant output."),
     ("Spent nuclear fuel is currently stored primarily in:",["Landfills","The ocean","*On-site cooling pools and dry cask storage at reactor sites (no permanent geological repository operating in US)","Underground permanently"],"Temporary storage."),
     ("Yucca Mountain (Nevada) was proposed as a:",["Tourist attraction","*Permanent geological repository for US high-level nuclear waste (project stalled politically)","Power plant","Mining site"],"Controversial storage plan."),
     ("Nuclear proliferation risk refers to:",["Power plant construction","*The potential for nuclear technology/materials to be diverted for weapons production","Waste management","Energy pricing"],"Security concern."),
     ("Small Modular Reactors (SMRs) are being developed to:",["Replace all energy","*Reduce construction costs and time, improve safety through passive systems, and provide flexible deployment","Only for submarines","Only for research"],"Next-generation technology."),
     ("Nuclear fusion, if achieved, would provide:",["No benefits","*Virtually unlimited energy with minimal waste (fuel is hydrogen isotopes; byproduct is helium)","The same as fission","Only small amounts"],"Future possibility."),
     ("France generates approximately _____ of its electricity from nuclear power.",["10%","25%","*~70% (one of the highest proportions in the world)","90%"],"Nuclear-dependent nation."),
     ("The capacity factor of nuclear plants is typically:",["Low (~30%)","Moderate (~50%)","*High (~90%+ — among the most reliable energy sources)","Variable"],"Very reliable."),
     ("Thermal pollution from nuclear (and fossil) plants occurs when:",["Plants are cold","*Heated cooling water is discharged into waterways, raising water temperature and reducing dissolved oxygen","No cooling is used","Only in winter"],"Ecological impact."),
     ("The debate over nuclear energy centers on:",["Only cost","*Balancing its low-carbon benefits against waste, safety, cost, and proliferation risks","Only safety","Only waste"],"Complex trade-offs."),
     ("For the AP exam, students should be able to:",["Only list pros","*Compare nuclear with fossil fuels and renewables, analyze risks, and evaluate its role in climate solutions","Only list cons","Only describe accidents"],"Balanced analysis.")]
)
lessons[k]=v

# 5.3
k,v = build_lesson(5,3,"Renewable Energy (Solar, Wind, Hydro, Geothermal)",
    "<h3>Renewable Energy Sources</h3>"
    "<h4>Solar</h4><p>Photovoltaic (PV) cells convert sunlight directly to electricity. Fastest-growing energy source; costs dropped ~90% since 2010.</p>"
    "<h4>Wind</h4><p>Turbines convert kinetic energy of wind. 2nd-fastest growing; concerns include bird/bat mortality and visual impact.</p>"
    "<h4>Hydroelectric</h4><p>Largest renewable source (~16% of global electricity). Dams displace communities and alter ecosystems.</p>"
    "<h4>Geothermal</h4><p>Heat from Earth's interior. Limited to tectonically active areas but very reliable.</p>",
    [("Photovoltaic (PV) Cell","Semiconductor device that converts sunlight directly into electricity."),
     ("Wind Turbine","Device converting kinetic energy of wind into electrical energy."),
     ("Hydroelectric Power","Electricity generated by flowing water through turbines in dams; largest renewable source globally."),
     ("Geothermal Energy","Heat energy from Earth's interior used for electricity generation or direct heating."),
     ("Intermittency","Challenge of solar and wind: output varies with weather and time of day; requires storage or backup.")],
    [("The fastest-growing energy source globally is:",["Coal","Nuclear","*Solar (costs dropped ~90% since 2010; exponential deployment growth)","Natural gas"],"Rapid expansion."),
     ("Solar PV cells convert sunlight to electricity through:",["Burning","*The photovoltaic effect (photons excite electrons in semiconductor materials)","Heat only","Chemical reaction"],"Direct conversion."),
     ("Wind energy's main environmental concerns include:",["CO₂ emissions","*Bird and bat mortality, visual/noise impact, and land use (though impacts are much less than fossil fuels)","Water pollution","Deforestation"],"Relatively minor impacts."),
     ("Hydroelectric power is the _____ source of renewable electricity globally.",["Smallest","*Largest (~16% of global electricity)","Newest","Most expensive"],"Dominant renewable."),
     ("Negative impacts of large hydroelectric dams include:",["None","*Displacing communities, blocking fish migration, flooding habitats, altering sediment flow, and methane from reservoirs","Only fish impacts","Only visual effects"],"Significant trade-offs."),
     ("Geothermal energy is most available in:",["Everywhere equally","*Tectonically active areas (plate boundaries, volcanic regions — Iceland, western US, East Africa)","Only at the equator","Only in deserts"],"Geological requirement."),
     ("Advantages of geothermal energy include:",["Only heating","*Very reliable (24/7), small footprint, near-zero emissions, and not intermittent","High cost always","Only in cold climates"],"Base-load renewable."),
     ("Solar and wind are called intermittent because:",["They never work","*Output varies with weather, time of day, and season — they require storage or backup","They are unreliable per se","They're expensive"],"Variable output."),
     ("Solutions to intermittency include:",["Only fossil fuel backup","*Battery storage, pumped hydro, grid interconnection, demand response, and overbuilding capacity","Giving up","Only nuclear backup"],"Multiple strategies."),
     ("Battery storage costs have _____ in the last decade.",["Increased","Stayed the same","*Dropped dramatically (~90% decline for lithium-ion batteries)","Only slightly decreased"],"Enabling renewables."),
     ("Net metering allows homeowners with solar panels to:",["Waste energy","*Sell excess electricity back to the grid, offsetting their electricity costs","Only use energy at night","Pay more"],"Consumer empowerment."),
     ("Concentrated Solar Power (CSP) differs from PV because it:",["Uses photovoltaic cells","*Uses mirrors to focus sunlight to heat fluid → steam → turbine (can include thermal storage)","Is less efficient","Only works at night"],"Heat-based solar."),
     ("Offshore wind farms offer advantages of:",["Lower wind speeds","*Stronger, more consistent winds and reduced visual/noise impact on communities","Only higher costs","Less energy"],"Better wind resource."),
     ("Run-of-river hydro is more environmentally friendly than dams because it:",["Builds bigger dams","*Doesn't require a large reservoir; diverts part of the river flow through turbines with minimal ecological disruption","Uses no water","Only serves one home"],"Lower impact hydro."),
     ("The levelized cost of energy (LCOE) for solar and wind is now:",["Higher than all fossil fuels","*Competitive with or cheaper than new fossil fuel plants in most markets worldwide","Always expensive","Only cheaper with subsidies"],"Economic tipping point."),
     ("Solar energy limitations include:",["Only cost","*Intermittency, land use for large-scale farms, manufacturing impacts (energy and materials), and recycling panels","No limitations","Only visual impact"],"Balanced assessment."),
     ("A smart grid helps integrate renewables by:",["Reducing electricity use only","*Dynamically managing electricity supply and demand using digital technology, improving efficiency and reliability","Having no technology","Only storing energy"],"Intelligent distribution."),
     ("The energy payback time for solar panels (time to generate as much energy as it took to make them) is:",["10+ years","*~1-3 years (then they produce clean energy for 25-30+ years)","Never pays back","50 years"],"Positive energy balance."),
     ("Hybrid systems combine multiple renewable sources to:",["Increase cost","*Improve reliability (e.g., solar + wind + storage; when one is low, others may be producing)","Reduce output","Only look impressive"],"Complementary sources."),
     ("For the AP exam, students should compare renewable sources by:",["Only naming them","*Analyzing energy output, environmental impacts, costs, reliability, geographic constraints, and scalability","Only calculating LCOE","Only listing pros"],"Comparative analysis.")]
)
lessons[k]=v

# 5.4
k,v = build_lesson(5,4,"Energy Efficiency & Conservation",
    "<h3>Energy Efficiency &amp; Conservation</h3>"
    "<p><b>Efficiency:</b> Getting more useful work from less energy input. <b>Conservation:</b> Using less energy through behavioral changes.</p>"
    "<h4>Key Strategies</h4>"
    "<ul><li>LED lighting uses ~75% less energy than incandescent.</li>"
    "<li>Building insulation, efficient appliances, ENERGY STAR standards.</li>"
    "<li>Cogeneration (CHP): Uses waste heat from electricity generation for heating (~80% efficiency vs. ~33% for conventional plants).</li>"
    "<li>Transportation: EVs, public transit, fuel economy standards.</li></ul>",
    [("Energy Efficiency","Getting more useful output from less energy input (e.g., LED vs. incandescent bulbs)."),
     ("Energy Conservation","Reducing energy use through behavioral changes (e.g., turning off lights, lowering thermostat)."),
     ("Cogeneration (CHP)","Combined Heat and Power — using waste heat from electricity production for heating; ~80% total efficiency."),
     ("ENERGY STAR","US EPA/DOE program certifying energy-efficient appliances and buildings."),
     ("Negawatt","A unit of energy saved through efficiency; often cheaper than generating new energy.")],
    [("Energy efficiency means:",["Using more energy","*Getting more useful work from less energy input","Using no energy","Only renewable energy"],"Do more with less."),
     ("Energy conservation means:",["Building more power plants","*Reducing energy use through behavioral changes (turning off lights, carpooling)","Only insulation","Only solar panels"],"Use less overall."),
     ("LED bulbs use approximately _____ less energy than incandescent bulbs.",["25%","50%","*~75% (and last much longer)","10%"],"Major efficiency gain."),
     ("Cogeneration (CHP) achieves ~_____ total efficiency by using waste heat.",["33%","50%","*~80% (compared to ~33% for conventional electricity-only plants)","100%"],"Waste heat recovered."),
     ("The most cost-effective way to reduce energy demand is typically:",["Building new power plants","*Improving energy efficiency in existing buildings, appliances, and vehicles","Only solar panels","Only nuclear power"],"Cheapest energy is energy not used."),
     ("A negawatt represents:",["A new energy source","*A unit of energy saved through efficiency measures (often cheaper than generating new energy)","Extra power","Negative electricity"],"Conservation concept."),
     ("ENERGY STAR labels indicate:",["High energy use","*Products that meet or exceed federal energy efficiency standards","Only US products","Only heating products"],"Consumer guide."),
     ("Building insulation reduces energy use by:",["Increasing heat loss","*Slowing heat transfer, reducing heating and cooling energy demand","Only in cold climates","Having no effect"],"Thermal barrier."),
     ("Transportation accounts for ~_____ of US energy consumption.",["10%","*~28-29%","50%","5%"],"Major sector."),
     ("Electric vehicles (EVs) are more efficient than gasoline cars because:",["They use more fuel","*Electric motors convert ~85-90% of electrical energy to motion vs. ~20-40% for internal combustion engines","They're heavier","They're slower"],"Higher conversion efficiency."),
     ("CAFE (Corporate Average Fuel Economy) standards require:",["No fuel standards","*Automakers to meet minimum fuel efficiency averages across their vehicle fleet","Only diesel standards","Only truck standards"],"US fuel economy law."),
     ("Green building standards (LEED) promote:",["Maximum energy use","*Energy efficiency, sustainable materials, water conservation, and indoor air quality in construction","Only aesthetics","Only cost reduction"],"Holistic building design."),
     ("Passive solar design uses:",["Solar panels only","*Building orientation, windows, thermal mass, and insulation to naturally heat and cool buildings without active systems","Active pumps","Only in deserts"],"Architectural efficiency."),
     ("Smart thermostats save energy by:",["Always running","*Learning usage patterns and automatically adjusting temperature when occupants are away or asleep","Only manual control","Increasing temperature"],"Intelligent control."),
     ("Industrial energy efficiency can be improved through:",["Only new factories","*Process optimization, waste heat recovery, variable speed motors, and better controls","Only downsizing","Only moving overseas"],"Manufacturing improvements."),
     ("Jevons Paradox (rebound effect) suggests that:",["Efficiency always saves energy","*Increased efficiency can lead to increased total consumption because lower cost per unit encourages more use","Efficiency is bad","Conservation is impossible"],"Counter-intuitive effect."),
     ("Combined cycle gas turbines achieve higher efficiency by:",["Burning more gas","*Using waste heat from the gas turbine to generate steam for a second turbine (~60% efficiency vs. ~33%)","Only one turbine","Cooling more"],"Two-stage generation."),
     ("Energy audits help identify:",["Nothing","*Where a building or facility is wasting energy, prioritizing the most cost-effective efficiency improvements","Only high energy use","Only insulation needs"],"Diagnostic tool."),
     ("Behavioral change programs (like eco-driving) can reduce fuel use by:",["0%","*5-15% (proper tire pressure, smooth acceleration, reduced idling — easy, free savings)","50%","Only 1%"],"Low-cost impact."),
     ("For the AP exam, understand that energy efficiency is important because:",["It's just about cost","*It reduces environmental impact, saves money, improves energy security, and is the fastest way to cut emissions","Only for homes","Only for industry"],"Multiple benefits.")]
)
lessons[k]=v

# 5.5
k,v = build_lesson(5,5,"Case Studies: Energy Policy",
    "<h3>Case Studies: Energy Policy</h3>"
    "<h4>Germany's Energiewende</h4>"
    "<p>Ambitious transition to renewables. ~50% of electricity from renewables (2023). Also phased out nuclear. Higher costs; criticized for coal persistence during transition.</p>"
    "<h4>Iceland</h4>"
    "<p>~100% of electricity from renewables (geothermal + hydro), thanks to abundant volcanic activity. Model for renewable-powered society.</p>"
    "<h4>US Energy Policy</h4>"
    "<p>Mix of federal/state policies: clean energy tax credits, CAFE standards, state renewable portfolio standards. Inflation Reduction Act (2022) largest US climate investment.</p>",
    [("Energiewende","Germany's energy transition policy: ambitious shift from fossil fuels and nuclear to renewable energy."),
     ("Renewable Portfolio Standard (RPS)","State-level US policy requiring utilities to source a minimum percentage of electricity from renewables."),
     ("Feed-in Tariff","Policy guaranteeing renewable energy producers a fixed price per kWh, incentivizing investment."),
     ("Carbon Tax","Tax on fossil fuel carbon content designed to internalize the cost of CO₂ emissions."),
     ("Inflation Reduction Act (2022)","Largest US climate investment: ~$370 billion in clean energy tax credits and incentives.")],
    [("Germany's Energiewende aims to:",["Increase coal use","*Transition from fossil fuels and nuclear to renewable energy sources","Only reduce imports","Maintain current mix"],"Green transition."),
     ("Germany generates approximately _____ of its electricity from renewables (2023).",["10%","25%","*~50%","90%"],"Significant progress."),
     ("A criticism of Germany's Energiewende is:",["Too much solar","*Increased reliance on coal during the nuclear phase-out, partially offsetting emission reductions","Too cheap","Too fast"],"Unintended fossil use."),
     ("Iceland generates ~100% of its electricity from:",["Fossil fuels","*Renewable sources (geothermal ~30% and hydroelectric ~70%)","Nuclear","Wind"],"Volcanic advantage."),
     ("Iceland's renewable success is largely due to:",["Government mandate only","*Abundant geothermal resources from volcanic activity and glacial rivers for hydropower","Solar energy","Wind energy"],"Geological advantage."),
     ("A renewable portfolio standard (RPS) requires:",["100% renewables immediately","*Utilities to source a minimum percentage of electricity from renewable sources by a target date","Only fossil fuels","No standards"],"State-level mandate."),
     ("Feed-in tariffs encourage renewable investment by:",["Taxing renewables","*Guaranteeing producers a fixed, above-market price per kWh of renewable electricity","Reducing energy prices","Only helping fossil fuels"],"Revenue certainty."),
     ("A carbon tax works by:",["Subsidizing carbon","*Making fossil fuels more expensive by taxing their carbon content → incentivizing clean alternatives","Reducing alternatives","Only affecting industry"],"Price signal."),
     ("The Inflation Reduction Act (2022) includes approximately:",["No climate funding","*~$370 billion in clean energy tax credits, incentives, and climate investments","Only $1 billion","Only fossil fuel subsidies"],"Historic US climate law."),
     ("Denmark aims for _____ of its electricity from wind by 2030.",["10%","*~80%+ (already a global leader in wind energy)","25%","50%"],"Wind energy leader."),
     ("China leads the world in:",["Only fossil fuels","*Total installed renewable energy capacity (largest solar, wind, and hydropower capacity globally) — though also largest coal user","Only nuclear","Only geothermal"],"Dual energy leader."),
     ("India's solar ambitions include:",["No solar plans","*Massive solar park construction (e.g., Bhadla Solar Park) and a target of 500 GW renewable capacity by 2030","Only wind","Only nuclear"],"Ambitious targets."),
     ("Costa Rica generates ~98% of electricity from renewables, primarily:",["Solar","*Hydroelectric, with geothermal and wind supplementing","Nuclear","Coal"],"Small-nation success."),
     ("Texas leads the US in wind energy production because of:",["Government mandates only","*Abundant wind resources, early RPS policy, deregulated energy market, and transmission infrastructure investment","Only federal money","Only one company"],"Multiple factors."),
     ("California's clean energy policies include:",["No climate policy","*100% clean electricity target by 2045, cap-and-trade, EV mandates, and building efficiency standards","Only fossil fuel support","Only nuclear"],"Comprehensive approach."),
     ("Energy subsidies globally favor fossil fuels over renewables by approximately:",["Equal amounts","*Several times more ($7+ trillion/year in fossil fuel subsidies including health costs vs. much less for renewables)","Less for fossil fuels","No subsidies exist"],"Uneven playing field."),
     ("The concept of a 'just transition' means:",["Only speed matters","*Ensuring workers and communities dependent on fossil fuel industries are supported during the energy transition","No transition needed","Only corporate profits matter"],"Equity in change."),
     ("Energy independence through renewables reduces:",["Nothing","*Dependence on imported fossil fuels, geopolitical risk, and price volatility","Only cost","Only emissions"],"Energy security benefit."),
     ("For the AP exam, energy policy questions require:",["Only naming policies","*Comparing policy approaches (taxes, standards, subsidies), evaluating trade-offs, and analyzing real-world outcomes","Only listing countries","Only memorizing dates"],"Policy analysis skills."),
     ("The key lesson from these case studies is:",["One policy fits all","*Successful energy transitions require multiple policies, geography-specific strategies, and long-term commitment","Only technology matters","Only cost matters"],"Context-dependent success.")]
)
lessons[k]=v

# 5.6
k,v = build_lesson(5,6,"AP Prep: Energy Calculations",
    "<h3>AP Prep: Energy Calculations</h3>"
    "<h4>Key Formulas</h4>"
    "<ul><li><b>Efficiency:</b> η = (useful energy output / total energy input) × 100%</li>"
    "<li><b>Power:</b> P = Energy / Time (watts = joules/seconds)</li>"
    "<li><b>Electrical energy:</b> E = P × t (kWh = kW × hours)</li>"
    "<li><b>Cost:</b> Cost = kWh × price per kWh</li>"
    "<li><b>1 kWh = 3.6 × 10⁶ J</b></li></ul>",
    [("Efficiency (η)","Useful energy output ÷ total energy input × 100%; always < 100% due to second law of thermodynamics."),
     ("Kilowatt-hour (kWh)","Unit of energy: 1 kW of power used for 1 hour; equals 3.6 × 10⁶ joules."),
     ("Power (Watts)","Rate of energy use: 1 watt = 1 joule per second; 1 kilowatt = 1,000 watts."),
     ("Capacity Factor","Actual energy output / maximum possible output × 100% (e.g., solar ~25%, nuclear ~90%, wind ~35%)."),
     ("Energy Return on Investment (EROI)","Ratio of energy delivered by a source to energy invested to produce it; higher is better.")],
    [("Energy efficiency is calculated as:",["Input ÷ Output","*Useful energy output ÷ Total energy input × 100%","Output × Input","Input × 100"],"Standard formula."),
     ("A power plant converts 1,000 MW of heat into 330 MW of electricity. Efficiency is:",["100%","*33% (330/1000 × 100%)","50%","330%"],"Typical thermal plant."),
     ("1 kWh equals:",["1,000 watts","3,600 joules","*3.6 × 10⁶ joules (3,600 seconds × 1,000 joules/second)","1 joule"],"Energy conversion."),
     ("A 100-watt bulb on for 10 hours uses:",["100 kWh","10 kWh","*1 kWh (100W × 10h = 1,000 Wh = 1 kWh)","0.1 kWh"],"E = P × t."),
     ("If electricity costs $0.12/kWh, running a 2,000W heater for 5 hours costs:",["$0.12","*$1.20 (2kW × 5h = 10 kWh × $0.12 = $1.20)","$12.00","$10.00"],"Cost = kWh × rate."),
     ("A 5 kW solar panel system with 25% capacity factor produces annually:",["5 kW","*~10,950 kWh (5 kW × 8,760 hours × 0.25 = 10,950 kWh)","43,800 kWh","1,000 kWh"],"Capacity factor applied."),
     ("The capacity factor of nuclear power is typically ~____%.",["25","35","*90","50"],"Very reliable output."),
     ("The capacity factor of solar PV is typically ~____%.",["*~25% (varies by location; higher in sunny areas like Arizona)","90%","50%","80%"],"Weather-dependent."),
     ("If a coal plant has EROI of 30:1, it means:",["It loses energy","*For every 1 unit of energy invested, it delivers 30 units (positive net energy)","30% efficient","1:30 loss"],"Energy profit."),
     ("Replacing a 60W incandescent with a 10W LED saves _____ watts.",["10W","*50W (same light output at 10W vs. 60W)","60W","70W"],"Efficiency comparison."),
     ("If you replace 20 incandescent bulbs (60W each) with LEDs (10W each), daily savings (8 hrs) are:",["1 kWh","*8 kWh/day (20 × 50W × 8h = 8,000 Wh = 8 kWh)","80 kWh","0.8 kWh"],"Bulk savings."),
     ("A home uses 30 kWh/day. Annual consumption is:",["30 kWh","365 kWh","*10,950 kWh (30 × 365)","3,000 kWh"],"Daily × 365."),
     ("At $0.15/kWh, annual cost for the 30 kWh/day home is:",["$450","*$1,642.50 (10,950 × $0.15)","$150","$5,000"],"Annual cost."),
     ("Second law efficiency considers:",["Only first law","*How close a process comes to the theoretical maximum efficiency (thermodynamic limit)","Only cost","Only output"],"Theoretical vs. actual."),
     ("A heat pump with COP (coefficient of performance) of 3 means it:",["Uses 3× more energy","*Delivers 3 units of heat for every 1 unit of electricity consumed","Is 300% efficient conventional sense","Only heats water"],"Energy multiplier."),
     ("To convert 500 MW power plant output to kWh per year:",["500 × 365","*500,000 kW × 8,760 hours × capacity factor (e.g., × 0.90 = 3,942,000,000 kWh for nuclear)","500 × 24","Only multiply by 1000"],"Annual energy calculation."),
     ("Per-capita energy consumption is highest in:",["India","Sub-Saharan Africa","*Countries like Iceland, Qatar, and the US (high development + energy-intensive lifestyles)","China"],"Consumption disparity."),
     ("The Sankey diagram shows:",["Only heat flow","*Energy flow and losses through a system (width of arrows proportional to energy)","Only efficiency","Only cost"],"Visual energy accounting."),
     ("For AP free-response energy calculation questions, students must:",["Only give a number","*Show all work with labeled formulas, correct units, and interpret results in environmental context","Only estimate","Only draw diagrams"],"Full solution required."),
     ("Understanding energy units and calculations is essential because:",["AP doesn't test math","*Quantitative reasoning about energy is a core AP skill — calculation questions appear in both MC and FRQ sections","Only for physics","Only for one question"],"High-frequency AP topic.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 5: wrote {len(lessons)} lessons")
