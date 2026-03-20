#!/usr/bin/env python3
"""Environmental Science Unit 9 – Sustainability (6 lessons)."""
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

# 9.1
k,v = build_lesson(9,1,"Principles of Sustainability",
    "<h3>Principles of Sustainability</h3>"
    "<p><b>Sustainability</b> means meeting the needs of the present without compromising the ability of future generations to meet their own needs (Brundtland Commission, 1987).</p>"
    "<h4>Three Pillars</h4>"
    "<ul><li><b>Environmental:</b> Maintaining ecosystem health and biodiversity.</li>"
    "<li><b>Economic:</b> Supporting livelihoods and economic viability long-term.</li>"
    "<li><b>Social:</b> Ensuring equity, well-being, and community resilience.</li></ul>"
    "<h4>Key Frameworks</h4>"
    "<p>UN Sustainable Development Goals (17 SDGs, 2015–2030). Ecological footprint analysis. Circular economy.</p>",
    [("Sustainability","Meeting present needs without compromising future generations' ability to meet their needs (Brundtland definition)."),
     ("Three Pillars","Environmental, economic, and social sustainability — all three must be balanced for true sustainability."),
     ("UN SDGs","17 Sustainable Development Goals (2015–2030) addressing poverty, inequality, environment, and prosperity."),
     ("Ecological Footprint","Measure of human demand on Earth's ecosystems in terms of area needed to produce resources and absorb waste."),
     ("Circular Economy","Economic model that eliminates waste by redesigning products for reuse, repair, remanufacturing, and recycling.")],
    [("The Brundtland definition of sustainability is:",["Using all resources now","*Meeting the needs of the present without compromising the ability of future generations to meet their own needs","Only about environment","Only about economy"],"Foundational definition."),
     ("The three pillars of sustainability are:",["Only environmental","*Environmental, economic, and social (all three must be balanced)","Only economic","Environmental and economic only"],"Triple bottom line."),
     ("The UN SDGs include _____ goals for 2015–2030.",["5","10","*17","25"],"Comprehensive global agenda."),
     ("Ecological footprint measures:",["Only CO₂ emissions","*Total human demand on ecosystems in terms of biologically productive land and water area needed","Only water use","Only waste production"],"Demand on nature."),
     ("If everyone lived like the average American, we would need approximately _____ Earths.",["1","2","*~5 (far exceeding Earth's biocapacity)","10"],"Unsustainable consumption."),
     ("A circular economy differs from a linear economy in that it:",["Produces more waste","*Designs out waste: products are made to be reused, repaired, remanufactured, or recycled (no 'take-make-dispose')","Is less efficient","Only recycles"],"Closed-loop system."),
     ("Intergenerational equity means:",["Only current generation matters","*Future generations have equal rights to a healthy environment and natural resources","Only past matters","Equity isn't part of sustainability"],"Cross-generational fairness."),
     ("Carrying capacity in sustainability refers to:",["Unlimited growth","*The maximum population an environment can sustain indefinitely without degradation","Only food capacity","Only one species"],"Ecological limit."),
     ("Renewable resources can be sustainable if:",["Always used maximally","*Harvested at or below their rate of regeneration (sustainable yield)","Never used","Used without limits"],"Harvest ≤ regeneration."),
     ("The precautionary principle in sustainability states:",["Wait for proof","*Take preventive action when there is risk of harm, even without full scientific certainty","Only act when certain","Never take risks"],"Act cautiously."),
     ("Life Cycle Assessment (LCA) evaluates:",["Only production costs","*Environmental impacts of a product from raw material extraction through manufacturing, use, and disposal (cradle to grave)","Only disposal impacts","Only energy use"],"Full product impact."),
     ("Greenwashing refers to:",["Genuine sustainability efforts","*Misleading claims about a product's or company's environmental practices (appearing green without substance)","Only government policies","Only small companies"],"False green claims."),
     ("The concept of 'planetary boundaries' identifies:",["Only one limit","*Nine Earth system processes with thresholds that, if crossed, could trigger irreversible environmental change","Unlimited boundaries","No boundaries"],"Safe operating space."),
     ("Some planetary boundaries already exceeded include:",["None","*Climate change, biodiversity loss, nitrogen/phosphorus cycles, and land-system change","All nine","Only climate"],"Already in danger zone."),
     ("Equity within sustainability means:",["Equal consumption","*Fair access to resources and opportunities for all people, with particular attention to marginalized communities","Only economic equality","Only environmental equality"],"Justice dimension."),
     ("Sustainable development integrates:",["Only growth","*Environmental protection, economic development, and social equity into a unified approach","Only conservation","Only technology"],"Integrated approach."),
     ("Natural capital refers to:",["Only money from nature","*Earth's stocks of natural resources (water, minerals, ecosystems, biodiversity) that provide services essential for human well-being","Only financial value","Only timber and fish"],"Nature's assets."),
     ("Ecosystem services include:",["Only food","*Provisioning (food, water), regulating (climate, floods), supporting (nutrient cycling), and cultural (recreation, spiritual) services","Only clean air","Only one type"],"Nature's contributions."),
     ("For the AP exam, sustainability questions require understanding:",["Only the definition","*The three pillars, their interactions, trade-offs, and how sustainability applies to specific environmental issues","Only one pillar","Only environmental sustainability"],"Integrated understanding."),
     ("True sustainability requires:",["Only technological solutions","*Systems thinking — addressing environmental, economic, and social dimensions together, because they are interconnected","Only individual action","Only government action"],"Holistic approach.")]
)
lessons[k]=v

# 9.2
k,v = build_lesson(9,2,"Sustainable Agriculture",
    "<h3>Sustainable Agriculture</h3>"
    "<h4>Problems with Industrial Agriculture</h4>"
    "<ul><li>Soil degradation, erosion, and loss of topsoil.</li>"
    "<li>Water pollution from fertilizer runoff (dead zones).</li>"
    "<li>Pesticide impacts on pollinators and human health.</li>"
    "<li>~25% of global greenhouse gas emissions from food systems.</li></ul>"
    "<h4>Sustainable Practices</h4>"
    "<ul><li><b>Crop rotation and cover crops:</b> Maintain soil health, reduce erosion.</li>"
    "<li><b>Integrated Pest Management (IPM):</b> Minimize pesticide use through biological and cultural controls.</li>"
    "<li><b>No-till farming:</b> Reduces soil disturbance, maintains carbon in soil.</li>"
    "<li><b>Agroforestry:</b> Integrating trees with crops and livestock.</li></ul>",
    [("Integrated Pest Management (IPM)","Approach minimizing pesticide use through biological controls, crop rotation, resistant varieties, and targeted chemical use as last resort."),
     ("Cover Crops","Plants grown between cash crop seasons to prevent erosion, build soil health, and sequester carbon."),
     ("No-Till Farming","Planting without plowing to reduce soil erosion, maintain soil structure, and keep carbon in the soil."),
     ("Agroforestry","Practice of integrating trees with crop or livestock systems for environmental and economic benefits."),
     ("Dead Zones","Hypoxic areas in water bodies caused by excess nutrient runoff (fertilizers) leading to algal blooms and oxygen depletion.")],
    [("Industrial agriculture contributes approximately _____ of global greenhouse gas emissions.",["5%","10%","*~25% (from food production, land use change, transport, processing, and waste)","50%"],"Major emission source."),
     ("Dead zones are caused primarily by:",["Only industrial waste","*Excess nitrogen and phosphorus from agricultural fertilizer runoff causing algal blooms → oxygen depletion","Only sewage","Only natural processes"],"Nutrient pollution."),
     ("The Gulf of Mexico dead zone is linked to:",["Ocean currents only","*Fertilizer runoff from the Mississippi River watershed (agricultural Midwest)","Only industrial pollution","Only natural variation"],"Agricultural runoff."),
     ("Integrated Pest Management (IPM) prioritizes:",["Maximum pesticide use","*Biological controls, habitat manipulation, and resistant varieties first; chemical pesticides as last resort","Only chemical control","Only organic methods"],"Least-toxic first."),
     ("Cover crops are planted primarily to:",["Sell at market","*Prevent erosion, build soil organic matter, suppress weeds, and sequester carbon between cash crop seasons","Only look nice","Only feed livestock"],"Soil protection."),
     ("No-till farming benefits include:",["More erosion","*Reduced soil erosion, maintained soil structure and carbon, less fuel use, and better water retention","Only cost savings","Only less work"],"Multiple benefits."),
     ("Crop rotation improves sustainability by:",["Growing one crop forever","*Breaking pest and disease cycles, improving soil nutrients (legumes fix nitrogen), and reducing need for inputs","Only adding variety","Only reducing work"],"Soil and pest management."),
     ("Agroforestry integrates trees with agriculture to provide:",["Only shade","*Multiple benefits: carbon sequestration, biodiversity habitat, windbreaks, reduced erosion, additional income from tree products","Only timber","Only aesthetics"],"Multi-benefit system."),
     ("Organic farming differs from conventional by:",["Being identical","*Prohibiting synthetic pesticides and fertilizers — relying on biological pest control, composting, and crop rotation","Only marketing","Having no standards"],"Chemical-free approach."),
     ("Precision agriculture uses _____ to reduce inputs.",["Nothing special","*GPS, sensors, drones, and data analysis to apply water, fertilizer, and pesticides only where and when needed","Only manual labor","Only organic methods"],"Technology-driven efficiency."),
     ("Polyculture (growing multiple crop species together) improves sustainability because:",["It's less productive","*It increases biodiversity, reduces pest outbreaks, improves soil health, and reduces risk of total crop failure","Only adds work","It's identical to monoculture"],"Diversity = resilience."),
     ("Soil health is fundamental to sustainability because:",["Soil doesn't matter","*Healthy soil supports plant growth, filters water, stores carbon, cycles nutrients, and supports biodiversity","Only for farming","Only for one generation"],"Foundation of food systems."),
     ("Composting converts organic waste into:",["Pollution","*Nutrient-rich soil amendment that improves soil structure, adds nutrients, and diverts waste from landfills","Nothing useful","Only methane"],"Waste to resource."),
     ("The food waste problem is significant because approximately _____ of food produced globally is wasted.",["5%","*~30-40% (wasted at production, retail, and consumer levels — enormous resources and emissions for nothing)","10%","1%"],"Massive waste."),
     ("Reducing meat consumption is an environmental strategy because:",["It has no impact","*Livestock requires far more land, water, and energy per calorie than plant foods and produces significant methane","Only for health","Only affects one resource"],"Resource-intensive production."),
     ("Aquaponics combines:",["Only fishing","*Aquaculture (fish farming) with hydroponics (soilless plant growing) in a recirculating system — fish waste feeds plants","Only gardening","Only composting"],"Integrated system."),
     ("Genetically modified organisms (GMOs) in agriculture are debated because:",["There's no debate","*Potential benefits (pest resistance, yield) vs. concerns (biodiversity, corporate control, unintended effects)","Only positive","Only negative"],"Complex trade-offs."),
     ("Sustainable agriculture must feed _____ billion people by 2050.",["5","7","*~10 (while using less land, water, and chemicals — an enormous challenge)","20"],"Grand challenge."),
     ("For AP, sustainable agriculture questions combine:",["Only farming techniques","*Ecology (soil, water, biodiversity), economics (viability, cost), social (food security, equity), and policy (subsidies, regulation)","Only economics","Only one dimension"],"Multi-dimensional analysis."),
     ("The key principle of sustainable agriculture is:",["Maximize short-term yield","*Produce food while maintaining environmental health, economic viability, and social equity for current and future generations","Only reduce chemicals","Only raise profits"],"Long-term viability.")]
)
lessons[k]=v

# 9.3
k,v = build_lesson(9,3,"Sustainable Energy",
    "<h3>Sustainable Energy</h3>"
    "<h4>Transition to Renewables</h4>"
    "<ul><li><b>Solar:</b> Fastest-growing energy source; costs dropped ~90% since 2010.</li>"
    "<li><b>Wind:</b> Competitive with fossil fuels; onshore and expanding offshore.</li>"
    "<li><b>Hydropower:</b> Largest renewable source but limited growth potential and ecological impacts.</li>"
    "<li><b>Energy storage:</b> Battery technology (lithium-ion) crucial for variable renewables.</li></ul>"
    "<h4>Energy Efficiency</h4>"
    "<p>The cheapest and cleanest energy is the energy we don't use. Building standards, LED lighting, efficient appliances, and industrial optimization can reduce demand 30-50%.</p>",
    [("Levelized Cost of Energy","Total cost of building and operating a power source divided by total energy output — renewables now cheapest in most places."),
     ("Grid-Scale Storage","Large battery systems that store renewable energy for use when sun isn't shining or wind isn't blowing."),
     ("Energy Efficiency","Using less energy to provide the same service — the cheapest, cleanest form of 'energy production.'"),
     ("Electrification","Replacing fossil fuel use with electricity (EVs, heat pumps) so renewable electricity can power everything."),
     ("Net Metering","Policy allowing solar panel owners to sell excess electricity back to the grid, credited on their bill.")],
    [("Solar energy costs have dropped approximately _____ since 2010.",["10%","50%","*~90% (making it the cheapest new electricity source in most of the world)","25%"],"Dramatic cost reduction."),
     ("Wind energy is now cost-competitive with:",["Nothing","*Fossil fuels (onshore wind is among the cheapest sources of new electricity globally)","Only solar","Only nuclear"],"Economic competitiveness."),
     ("The main challenge with solar and wind energy is:",["They're too expensive","*Intermittency — they only generate when the sun shines or wind blows, requiring storage or backup","They pollute too much","They take too much space"],"Variable generation."),
     ("Energy storage (batteries) addresses intermittency by:",["Wasting energy","*Storing excess renewable energy during high production and releasing it during low production or high demand","Only for phones","Only small-scale"],"Balancing supply/demand."),
     ("Energy efficiency is considered the 'first fuel' because:",["It's an actual fuel","*Reducing energy demand is cheaper and cleaner than building any new energy supply (a 'negawatt' is cheaper than a megawatt)","It produces energy","Only a metaphor"],"Cheapest resource."),
     ("LED lighting uses approximately _____ less energy than incandescent bulbs.",["10%","50%","*~75-80% (and lasts 25× longer)","25%"],"Dramatic efficiency gain."),
     ("Building standards like LEED certification promote:",["Only aesthetics","*Energy efficiency, water conservation, sustainable materials, and reduced environmental impact in construction","Only cost savings","Only one benefit"],"Green building."),
     ("Heat pumps are significant for sustainability because they:",["Only heat","*Move heat rather than generating it — 3-5× more efficient than furnaces; can be powered by renewable electricity","Only cool","Are less efficient than furnaces"],"Efficient heating/cooling."),
     ("Electric vehicles (EVs) reduce emissions especially when:",["Always, regardless of source","*Charged with renewable electricity (lifecycle emissions far lower than gasoline vehicles)","Only with gasoline","Never"],"Clean electricity + EVs."),
     ("Hydropower is the largest renewable energy source but faces limitations:",["None","*Ecological impacts (fish migration, altered river flows), limited suitable sites for new dams, and vulnerability to drought","Only cost","Only noise"],"Environmental trade-offs."),
     ("Nuclear energy is debated in sustainability because:",["It's renewable","*Low carbon emissions during operation, but concerns about waste disposal, safety (meltdown risk), proliferation, and high construction costs","Only positive","Only negative"],"Complex trade-offs."),
     ("Smart grids improve sustainability by:",["Only saving money","*Optimizing electricity distribution, integrating variable renewables, reducing waste, and enabling demand response","Only for large utilities","Only theoretical"],"Intelligent grid management."),
     ("The 'duck curve' in energy planning shows:",["No pattern","*Midday solar overproduction followed by rapid ramp-up needed at sunset — a challenge for grid operators managing renewable variability","Only nighttime demand","Only flat demand"],"Solar integration challenge."),
     ("Distributed energy (rooftop solar, small wind) contributes to sustainability by:",["Being too small to matter","*Reducing transmission losses, increasing resilience, democratizing energy production, and empowering communities","Only for wealthy homeowners","Only in rural areas"],"Decentralized power."),
     ("Green hydrogen is produced by:",["Burning fossil fuels","*Using renewable electricity to electrolyze water (splitting H₂O into H₂ and O₂) — zero-carbon fuel","Only natural gas reformation","Only nuclear power"],"Clean fuel production."),
     ("The global transition to sustainable energy requires:",["Only solar panels","*Massive investment in renewables, storage, grid infrastructure, efficiency, electrification, AND policies that phase out fossil fuel subsidies","Only one technology","Only voluntary action"],"System-wide transformation."),
     ("Energy poverty (lack of access) is a sustainability issue because:",["Everyone has energy","*~800 million people lack electricity; ~2.6 billion lack clean cooking fuel — sustainable energy must address access equity","Only in one continent","Not a real problem"],"Energy access."),
     ("The 'energy trilemma' balances:",["Only cost","*Affordability, reliability, and environmental sustainability (all three must be achieved)","Only environment","Only two factors"],"Triple challenge."),
     ("For AP, sustainable energy questions require analyzing:",["Only technology","*Energy sources' environmental impacts, economic viability, social equity, and policy frameworks — comparing trade-offs","Only costs","Only emissions"],"Multi-factor analysis."),
     ("The key insight for sustainable energy is:",["One technology will solve everything","*No single solution — a portfolio of renewables, efficiency, storage, electrification, and smart policies is needed","Only conservation matters","Technology alone is enough"],"Portfolio approach.")]
)
lessons[k]=v

# 9.4
k,v = build_lesson(9,4,"Green Building & Urban Planning",
    "<h3>Green Building &amp; Urban Planning</h3>"
    "<h4>Sustainable Buildings</h4>"
    "<ul><li>Energy-efficient design: passive solar, insulation, LED lighting, smart systems.</li>"
    "<li>Green materials: recycled content, sustainably sourced wood, low-VOC paints.</li>"
    "<li>LEED certification: Leadership in Energy and Environmental Design.</li></ul>"
    "<h4>Sustainable Urban Planning</h4>"
    "<ul><li><b>Smart growth:</b> Compact, mixed-use development reducing sprawl.</li>"
    "<li><b>Public transit:</b> Reducing car dependence and emissions.</li>"
    "<li><b>Green infrastructure:</b> Parks, green roofs, bioswales, urban forests for cooling and stormwater.</li></ul>",
    [("LEED Certification","Leadership in Energy and Environmental Design: green building rating system evaluating energy, water, materials, and indoor quality."),
     ("Smart Growth","Urban planning approach promoting compact, walkable, mixed-use development that reduces sprawl and car dependence."),
     ("Urban Heat Island","Cities are warmer than surrounding rural areas due to pavement, buildings, and reduced vegetation."),
     ("Green Infrastructure","Vegetation-based systems (green roofs, rain gardens, bioswales, urban forests) managing stormwater and reducing heat."),
     ("Passive Solar Design","Building design using sun orientation, thermal mass, and natural ventilation to heat/cool without mechanical systems.")],
    [("LEED certification evaluates buildings on:",["Only aesthetics","*Energy performance, water efficiency, materials, indoor environmental quality, and site sustainability","Only energy use","Only cost"],"Comprehensive green rating."),
     ("Passive solar design reduces energy use by:",["Adding more machines","*Using building orientation, window placement, thermal mass, and insulation to heat and cool naturally","Only insulation","Only south-facing windows"],"Design with nature."),
     ("Smart growth urban planning promotes:",["More sprawl","*Compact, walkable, mixed-use communities with public transit access — reducing car dependence and land consumption","Only suburban development","Only tall buildings"],"Anti-sprawl approach."),
     ("Urban heat islands are caused by:",["Trees","*Dark pavement and buildings absorbing heat, reduced vegetation, waste heat from energy use, and reduced air flow","Cold air","Only cars"],"Cities are warmer."),
     ("Green roofs reduce urban heat by:",["Adding weight only","*Evapotranspiration cooling, reflecting sunlight, insulating buildings, and reducing stormwater runoff","Only looking nice","Only one mechanism"],"Multi-benefit."),
     ("Bioswales and rain gardens manage stormwater by:",["Channeling to sewers","*Filtering and absorbing runoff through vegetation and soil — reducing flooding and pollutant transport to waterways","Only decoration","Only in dry areas"],"Natural filtration."),
     ("Transit-oriented development (TOD) clusters housing and businesses near:",["Highways only","*Public transit stations to reduce car trips, promote walking/biking, and create vibrant mixed-use communities","Only parking lots","Only in suburbs"],"Mobility + community."),
     ("Urban sprawl is unsustainable because it:",["Has no downsides","*Consumes farmland, increases car dependence and emissions, costs more for infrastructure, and fragments habitat","Only affects cities","Only is an aesthetic issue"],"Multi-dimensional harm."),
     ("Net-zero energy buildings:",["Use no energy","*Produce as much renewable energy as they consume annually (through solar, efficiency, and design)","Are impossible","Only in warm climates"],"Energy balance."),
     ("Low-impact development (LID) in urban areas mimics:",["Industrial systems","*Natural hydrology by managing stormwater at the source through green infrastructure","Only piped systems","Only concrete channels"],"Nature-based drainage."),
     ("Complete streets are designed for:",["Only cars","*All users: pedestrians, cyclists, public transit, and cars — safe and accessible for everyone","Only buses","Only bikes"],"Multi-modal access."),
     ("Urban forests and tree canopy provide:",["Only shade","*Cooling (reduced heat island), air quality improvement, carbon sequestration, stormwater management, and mental health benefits","Only aesthetics","Only one benefit"],"Multiple ecosystem services."),
     ("Mixed-use zoning promotes sustainability by:",["Separating all uses","*Combining residential, commercial, and recreational uses in one area — reducing travel distances and enabling walkability","Only commercial areas","Only housing"],"Proximity = less driving."),
     ("Building retrofit programs are important because:",["All buildings are new","*Existing buildings are the majority of building stock — retrofitting insulation, windows, HVAC, and lighting dramatically reduces energy use","Only new buildings matter","Retrofitting is impossible"],"Existing stock matters."),
     ("The '15-minute city' concept means:",["Only 15 minutes of work","*All essential services (shops, schools, healthcare, parks, work) accessible within a 15-minute walk or bike from home","Only one neighborhood","Only in small towns"],"Proximity planning."),
     ("Permeable pavement reduces environmental impact by:",["Being weaker","*Allowing rainwater to infiltrate the ground — reducing runoff, recharging groundwater, and filtering pollutants","Only in parking lots","Only looks different"],"Reduce impervious surface."),
     ("Embodied carbon in buildings refers to:",["Only operational energy","*Carbon emissions from manufacturing, transporting, and installing building materials (significant portion of building's total carbon footprint)","Only demolition","Only cement"],"Construction emissions."),
     ("Circular economy principles in construction include:",["Only demolition","*Designing for disassembly, using recycled materials, adaptive reuse of buildings, and minimizing construction waste","Only new materials","Only one principle"],"Waste reduction."),
     ("For AP, green building and urban planning questions connect:",["Only architecture","*Energy, water, land use, transportation, air quality, biodiversity, and social equity in an integrated systems approach","Only one discipline","Only zoning"],"Systems thinking."),
     ("The key principle of sustainable urban design is:",["Build more roads","*Create compact, connected, mixed-use communities with green infrastructure — reducing resource consumption while improving quality of life","Only reduce traffic","Only plant trees"],"Quality of life + sustainability.")]
)
lessons[k]=v

# 9.5
k,v = build_lesson(9,5,"Case Studies: Sustainable Practices",
    "<h3>Case Studies: Sustainable Practices</h3>"
    "<h4>Freiburg, Germany — Green City</h4>"
    "<p>Solar capital of Europe. 40% of trips by bike or transit. Vauban district: car-free, passive solar housing, district heating.</p>"
    "<h4>Costa Rica — Conservation Leader</h4>"
    "<p>~99% electricity from renewables. Reversed deforestation (forest cover 25% → 52%). Payment for Ecosystem Services (PES) program.</p>"
    "<h4>Bhutan — Gross National Happiness</h4>"
    "<p>Carbon-negative country. Measures progress by well-being, not GDP. Constitutional mandate: 60%+ forest cover forever.</p>",
    [("Freiburg, Germany","Model green city: solar energy leader, car-free districts, 40%+ trips by bike/transit, passive solar buildings."),
     ("Costa Rica PES","Payment for Ecosystem Services: farmers paid to protect forests for carbon, water, biodiversity and scenic services."),
     ("Bhutan's GNH","Gross National Happiness: national development philosophy prioritizing well-being and environmental conservation over GDP."),
     ("Vauban District","Car-free sustainable neighborhood in Freiburg: passive solar housing, district heating, community design."),
     ("Carbon-Negative","Absorbing more CO₂ than emitting — Bhutan achieves this through extensive forest cover and low emissions.")],
    [("Freiburg, Germany is known as a green city because:",["Only solar panels","*Comprehensive sustainability: solar energy leadership, 40%+ trips by bike/transit, car-free districts, and passive solar buildings","Only one policy","Only recycling"],"Integrated approach."),
     ("The Vauban district in Freiburg is notable for:",["Normal suburban design","*Car-free living, passive solar housing, district heating, and community-centered design — a model sustainable neighborhood","Only one feature","Only solar panels"],"Living laboratory."),
     ("Costa Rica generates approximately _____ of its electricity from renewables.",["50%","75%","*~99% (primarily hydropower, with wind, geothermal, and solar)","25%"],"Near-100% clean electricity."),
     ("Costa Rica reversed deforestation, increasing forest cover from:",["90% to 100%","*~25% (1980s) to ~52% (today) through Payment for Ecosystem Services and protected areas","40% to 45%","10% to 12%"],"Remarkable recovery."),
     ("Payment for Ecosystem Services (PES) in Costa Rica pays landowners to:",["Cut down forests","*Protect and restore forests in exchange for the services they provide (carbon storage, water filtration, biodiversity)","Only plant coffee","Only raise cattle"],"Value nature's services."),
     ("Bhutan measures national progress using:",["Only GDP","*Gross National Happiness (GNH): a holistic measure including psychological well-being, health, education, ecology, and governance","Only income","Only economic growth"],"Beyond GDP."),
     ("Bhutan is carbon-negative because:",["It has no people","*Its extensive forests (mandate: 60%+ coverage) absorb more CO₂ than its small, low-emission economy produces","It uses nuclear power","It doesn't measure emissions"],"Net carbon absorber."),
     ("Bhutan's constitution mandates that _____ of the country remain forested.",["10%","30%","50%","*60% (minimum, forever — a constitutional environmental guarantee)"],"Constitutional conservation."),
     ("Singapore's approach to sustainability includes:",["Only water recycling","*NEWater (recycled water), vertical gardens, integrated urban planning, and world-leading green building standards","Only one innovation","Only public transit"],"City-state sustainability."),
     ("Denmark's wind energy success includes:",["Only a few turbines","*~50% of electricity from wind, world-leading wind technology industry, and strong community ownership of wind projects","Only government projects","Only offshore"],"Wind energy leader."),
     ("Curitiba, Brazil pioneered:",["Nothing sustainable","*Bus Rapid Transit (BRT), green space integration, innovative waste management, and sustainable urban planning","Only recycling","Only parks"],"Urban sustainability pioneer."),
     ("Iceland uses its geothermal resources for:",["Only tourism","*Nearly 100% of heating and ~70% of total energy — plus aluminum smelting powered by renewables","Only electricity","Only hot springs"],"Geothermal leader."),
     ("Rwanda's plastic bag ban (2008) demonstrates:",["Only restriction","*How a developing nation can lead on environmental policy — cleanest country in Africa, with strong enforcement and innovation","Only punishment","Only one policy"],"Developing nation leadership."),
     ("These case studies show that sustainability is achievable when:",["Only in rich countries","*Political will, community engagement, innovative policy, and long-term vision align — applicable across different contexts and income levels","Only with technology","Only in small countries"],"Universal applicability."),
     ("A common thread across successful case studies is:",["Top-down control only","*Integration — combining environmental, economic, and social goals rather than treating them separately","Only one solution","Only government action"],"Integrated approaches work."),
     ("Challenges in scaling sustainable practices include:",["No challenges","*Political opposition, economic costs of transition, cultural resistance, and the need for context-appropriate solutions","Only money","Only politics"],"Real-world barriers."),
     ("Indigenous sustainability practices offer lessons because:",["They're outdated","*Many indigenous communities have sustained ecosystems for thousands of years using traditional ecological knowledge","Only for one region","Only historical interest"],"Proven long-term approaches."),
     ("The role of technology in these case studies is:",["Everything","*Important but always combined with policy, community engagement, and cultural change — technology alone is insufficient","Irrelevant","Only for rich nations"],"Necessary but not sufficient."),
     ("For AP, case studies should be used to:",["Only memorize facts","*Illustrate principles, compare approaches, analyze what makes sustainability succeed or fail, and apply lessons broadly","Only name countries","Only list technologies"],"Applied learning."),
     ("The overarching lesson from sustainability case studies is:",["Sustainability is impossible","*Sustainability is achievable at multiple scales with vision, policy, investment, and community engagement — no single model fits all","Only one model works","Only small countries can do it"],"Hope with realism.")]
)
lessons[k]=v

# 9.6
k,v = build_lesson(9,6,"AP Prep: Sustainability Metrics",
    "<h3>AP Prep: Sustainability Metrics</h3>"
    "<h4>Key Metrics</h4>"
    "<ul><li><b>Ecological footprint:</b> Demand on ecosystems in global hectares (gha).</li>"
    "<li><b>Carbon footprint:</b> Total GHG emissions from an activity, product, or entity.</li>"
    "<li><b>IPAT equation:</b> Impact = Population × Affluence × Technology.</li>"
    "<li><b>HDI (Human Development Index):</b> Life expectancy + education + income → well-being measure.</li>"
    "<li><b>Genuine Progress Indicator:</b> GDP adjusted for environmental and social costs.</li></ul>",
    [("IPAT Equation","I = P × A × T : Environmental Impact = Population × Affluence (consumption per capita) × Technology (impact per unit of consumption)."),
     ("Carbon Footprint","Total greenhouse gas emissions (in CO₂ equivalents) caused by an individual, event, product, or organization."),
     ("HDI","Human Development Index: composite measure of health (life expectancy), education, and standard of living."),
     ("Genuine Progress Indicator (GPI)","Alternative to GDP that adds value of positive non-market activities and subtracts costs of environmental degradation and social problems."),
     ("Biocapacity","The capacity of ecosystems to produce biological materials and absorb waste — compared to ecological footprint.")],
    [("The IPAT equation states that environmental impact equals:",["Only population","*Population × Affluence × Technology (all three factors interact to determine impact)","Only technology","Only affluence"],"Three-factor model."),
     ("Ecological footprint is measured in:",["Square miles","Tons of CO₂","*Global hectares (gha) — area of biologically productive land and water needed","Dollars"],"Land area equivalent."),
     ("A country's ecological footprint exceeding its biocapacity means:",["It's self-sufficient","*It is consuming more resources than its ecosystems can regenerate (ecological deficit, relying on imports or depleting stocks)","Nothing significant","It's perfectly balanced"],"Living beyond means."),
     ("Carbon footprint is measured in:",["Global hectares","*Tons (or kilograms) of CO₂ equivalent (CO₂e)","Dollars","Gallons"],"Emission equivalents."),
     ("The IPAT equation helps explain why _____ sometimes have the highest impact.",["Developing nations","*Wealthy nations with high consumption (high A and T) even with moderate population","Only large countries","Only small countries"],"Consumption matters."),
     ("Technology (T) in IPAT can _____ or _____ environmental impact.",["Only increase","Only decrease","*Either increase (dirty technology) or decrease (clean technology) — it's a variable","Have no effect on"],"Double-edged factor."),
     ("GDP as a measure of well-being is criticized because it:",["Is always accurate","*Doesn't account for environmental degradation, inequality, unpaid work, or factors that reduce quality of life","Measures sustainability","Is comprehensive"],"Incomplete measure."),
     ("The Genuine Progress Indicator (GPI) improves on GDP by:",["Being identical","*Adding positive non-market activities (volunteering, household work) and subtracting costs (pollution, crime, resource depletion)","Only measuring money","Ignoring the economy"],"Better well-being measure."),
     ("The Human Development Index (HDI) measures:",["Only income","*Life expectancy (health), education (years of schooling), and income (GNI per capita) — a broader measure than GDP alone","Only GDP","Only employment"],"Three dimensions."),
     ("Sustainability indicators should measure:",["Only one dimension","*Environmental health, economic viability, and social well-being together (reflecting the three pillars)","Only economic growth","Only environmental quality"],"All three pillars."),
     ("Earth Overshoot Day marks when:",["Nothing special","*Humanity has used more from nature than the planet can renew in the entire year (moving earlier each decade — currently late July)","The year ends","Seasons change"],"Annual deficit date."),
     ("Water footprint measures:",["Only drinking water","*Total volume of freshwater used to produce goods and services consumed by an individual, business, or nation","Only irrigation","Only rainfall"],"Hidden water use."),
     ("Per capita ecological footprint is highest in:",["Most populated countries","*High-income countries (US, Australia, UAE) due to high consumption levels","Only one country","Equally distributed"],"Consumption inequality."),
     ("The concept of 'decoupling' refers to:",["Linking growth and impact","*Achieving economic growth while reducing environmental impact (absolute decoupling = growing GDP while total impact decreases)","Only theoretical","Impossible in practice"],"Growth without degradation."),
     ("Material footprint tracks:",["Only weight","*Total raw materials extracted to meet a country's consumption needs (including materials embedded in imports)","Only local resources","Only waste"],"Hidden material flow."),
     ("Social sustainability metrics include:",["Only income","*Gini coefficient (inequality), access to education and healthcare, gender equity, and community well-being","Only employment","Only one measure"],"Social dimension."),
     ("For AP calculations, students may need to convert between:",["Only one metric","*Per capita and total values (multiply per capita × population), and compare footprints to biocapacity","Only per capita","Only total values"],"Quantitative skills."),
     ("The Environmental Performance Index (EPI) ranks countries on:",["Only one factor","*Environmental health (air quality, water, sanitation) and ecosystem vitality (climate, biodiversity, fisheries) — over 40 indicators","Only GDP","Only emissions"],"National comparison."),
     ("Sustainable development metrics should track progress toward:",["Only economic growth","*Specific, measurable goals (like the 17 SDGs) across environmental, social, and economic dimensions","Only one goal","Only environmental restoration"],"Goal-oriented measurement."),
     ("For the AP exam, sustainability metrics require:",["Only definitions","*Ability to calculate, interpret, compare, and critically evaluate metrics — understanding what each measures and its limitations","Only memorization","Only one formula"],"Analytical application.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 9: wrote {len(lessons)} lessons")
