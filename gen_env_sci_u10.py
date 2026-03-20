#!/usr/bin/env python3
"""Environmental Science Unit 10 – Review & AP Prep (6 lessons)."""
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

# 10.1
k,v = build_lesson(10,1,"Review: Key Concepts",
    "<h3>Review: Key Concepts Across Environmental Science</h3>"
    "<h4>Core Themes</h4>"
    "<ul><li><b>Ecosystems &amp; Biodiversity:</b> Energy flow, nutrient cycling, species interactions, biomes, biodiversity value.</li>"
    "<li><b>Population &amp; Resources:</b> Carrying capacity, demographic transition, renewable vs. nonrenewable resources.</li>"
    "<li><b>Pollution &amp; Health:</b> Air, water, soil pollution sources and effects; bioaccumulation; environmental health.</li>"
    "<li><b>Climate Change:</b> Greenhouse effect, evidence, impacts, mitigation, adaptation, international agreements.</li>"
    "<li><b>Sustainability:</b> Three pillars, IPAT, ecological footprint, sustainable practices.</li>"
    "<li><b>Policy &amp; Law:</b> Major US laws, international treaties, environmental justice.</li></ul>",
    [("Energy Flow","Energy moves through ecosystems in one direction: sun → producers → consumers → decomposers; 10% rule between trophic levels."),
     ("Biogeochemical Cycles","Carbon, nitrogen, phosphorus, and water cycles — human activities have disrupted all of them."),
     ("Carrying Capacity","Maximum population an environment can sustain; influenced by resources, space, disease, and predation."),
     ("Bioaccumulation/Biomagnification","Toxins concentrate in organisms (bioaccumulation) and increase at each trophic level (biomagnification)."),
     ("The Three Pillars","Environmental, economic, and social sustainability must all be addressed for true sustainability.")],
    [("The 10% rule states that approximately _____ of energy transfers between trophic levels.",["100%","50%","25%","*~10% (the rest is lost as heat through cellular respiration)"],"Energy loss at each level."),
     ("Primary productivity is highest in:",["Deserts","*Tropical rainforests and estuaries (high sunlight, water, and nutrients)","Tundra","Open ocean per area"],"Most productive ecosystems."),
     ("The water cycle is driven primarily by:",["Gravity alone","*Solar energy (evaporation) and gravity (precipitation, runoff)","Only human activity","Only wind"],"Solar-powered cycle."),
     ("The nitrogen cycle requires _____ to convert N₂ gas into usable forms.",["Photosynthesis","*Nitrogen-fixing bacteria (and human-made processes like Haber-Bosch)","Only lightning","Only decomposition"],"Biological fixation."),
     ("Phosphorus differs from other nutrient cycles because it:",["Has a gas phase","*Has no significant atmospheric component — cycles through rocks, water, soil, and organisms","Is not essential","Cycles fastest"],"No gas phase."),
     ("Demographic transition describes how:",["Population always grows","*Countries move from high birth/death rates to low birth/death rates as they develop economically","Population always declines","Nothing changes"],"Population pattern with development."),
     ("The greatest threat to biodiversity globally is:",["Pollution alone","*Habitat loss and degradation (followed by overexploitation, invasive species, pollution, and climate change)","Only climate change","Only hunting"],"#1 threat: habitat loss."),
     ("Eutrophication is caused by:",["Clean water","*Excess nutrients (N and P) in water bodies → algal blooms → decomposition → oxygen depletion → aquatic dead zones","Only temperature","Only sediment"],"Nutrient overload."),
     ("The ozone layer protects life by:",["Trapping heat","*Absorbing harmful UV-B and UV-C radiation from the sun (preventing skin cancer, cataracts, and ecosystem damage)","Reflecting visible light","Producing oxygen"],"UV shield."),
     ("Acid rain is caused by emissions of:",["Only CO₂","*SO₂ and NOₓ (from fossil fuel combustion) reacting with water vapor to form sulfuric and nitric acid","Only natural gases","Only methane"],"Acidic deposition."),
     ("The tragedy of the commons occurs when:",["Resources are privately owned","*Individuals overuse shared resources because each person's benefit outweighs their share of the cost","Resources are unlimited","Everyone cooperates"],"Overuse of shared resources."),
     ("Keystone species are important because they:",["Are the most numerous","*Have a disproportionately large impact on ecosystem structure and function relative to their abundance","Only affect one species","Are always predators"],"Outsized importance."),
     ("R-selected species vs. K-selected species differ in:",["Nothing","*Reproductive strategy: r-selected = many offspring, little care, rapid growth; K-selected = few offspring, much care, slow growth","Only size","Only habitat"],"Life history strategies."),
     ("Human ecological footprint exceeds Earth's biocapacity, meaning:",["We're fine","*We are using resources faster than Earth can regenerate them (ecological deficit since the 1970s)","We're under-consuming","Balance is maintained"],"Overshoot."),
     ("Environmental Impact Assessments are required by:",["No law","*NEPA (National Environmental Policy Act) — for major federal actions significantly affecting the environment","Only state law","Only for businesses"],"Federal requirement."),
     ("The Clean Air Act, Clean Water Act, and ESA are all enforced primarily by:",["States only","*The EPA (Environmental Protection Agency) and relevant agencies (USFWS for ESA)","Only courts","Only local government"],"Federal enforcement."),
     ("Environmental justice means that:",["Only wealthy areas are protected","*All communities receive fair treatment and meaningful involvement in environmental decisions, regardless of race or income","Only environmental issues matter","Justice and environment are separate"],"Equity in environment."),
     ("The Paris Agreement asks each nation to set _____ for emission reductions.",["Binding targets","*Nationally Determined Contributions (NDCs) — voluntary, updated every 5 years with increasing ambition","No targets","Only one-time goals"],"Bottom-up pledges."),
     ("For AP review, the most important skill is:",["Only memorizing facts","*Connecting concepts across topics — e.g., linking agriculture to water pollution to dead zones to policy solutions","Only calculations","Only definitions"],"Systems thinking."),
     ("The central message of environmental science is:",["Nature is separate from humans","*Human well-being depends on the health of Earth's systems — understanding these connections enables better decisions","Nothing can be done","Only technology matters"],"Interdependence.")]
)
lessons[k]=v

# 10.2
k,v = build_lesson(10,2,"AP-Style Practice",
    "<h3>AP-Style Practice Questions</h3>"
    "<p>This lesson focuses on practice with the types of questions found on the AP Environmental Science (APES) exam: multiple choice and free-response, covering all major topics.</p>"
    "<h4>Exam Format</h4>"
    "<ul><li>80 multiple-choice questions (90 minutes) — 60% of score.</li>"
    "<li>3 free-response questions (70 minutes) — 40% of score.</li>"
    "<li>FRQ types: Design an Investigation, Analyze an Environmental Problem, Propose a Solution.</li></ul>",
    [("APES Exam Format","80 MC questions (90 min, 60% of score) + 3 FRQs (70 min, 40% of score)."),
     ("FRQ Types","Design an Investigation, Analyze an Environmental Problem, and Propose a Solution."),
     ("Claim-Evidence-Reasoning","AP response structure: make a claim → support with specific evidence → explain reasoning connecting evidence to claim."),
     ("Quantitative Skills","APES requires calculations: per capita rates, percent change, population growth, energy conversions."),
     ("AP Scoring","FRQs scored on point-based rubrics rewarding specific, correct answers")],
    [("The APES exam has _____ multiple-choice questions.",["40","60","*80","100"],"Section I format."),
     ("The three FRQ types on APES are:",["Only essays","*Design an Investigation, Analyze an Environmental Problem, and Propose a Solution","Only calculations","Only short answers"],"FRQ categories."),
     ("A well-constructed FRQ response uses:",["Only opinions","*Claim-Evidence-Reasoning: clear claims backed by specific scientific evidence with logical reasoning","Only vocabulary","Only diagrams"],"Response structure."),
     ("If a city of 500,000 produces 2 kg of waste per person per day, total daily waste is:",["500,000 kg","*1,000,000 kg (1,000 metric tons)","100,000 kg","10,000,000 kg"],"Per capita calculation."),
     ("A population of 10 million with birth rate 15/1000 and death rate 8/1000 has a growth rate of:",["15‰","8‰","*7‰ (0.7% per year)","23‰"],"Birth rate − death rate."),
     ("Using the Rule of 70, a population growing at 2% will double in:",["20 years","*35 years (70 ÷ 2)","70 years","140 years"],"Doubling time calculation."),
     ("If a coal plant emits 0.9 kg CO₂ per kWh and a solar farm emits 0.05 kg, switching 1,000,000 kWh saves:",["50,000 kg","*850,000 kg of CO₂ (0.9 − 0.05 = 0.85 per kWh × 1,000,000)","900,000 kg","100,000 kg"],"Emission reduction calculation."),
     ("When designing an investigation for AP, include:",["Only a hypothesis","*Hypothesis, independent/dependent variables, control, procedure, and how you'd analyze data","Only the question","Only the conclusion"],"Complete experimental design."),
     ("'Analyze an Environmental Problem' FRQs require:",["Only describing the problem","*Identifying causes, describing effects on ecosystems AND humans, and explaining the science behind the connections","Only solutions","Only one paragraph"],"Multi-part analysis."),
     ("'Propose a Solution' FRQs require:",["Only naming one solution","*Describing the solution, explaining how it addresses the problem, identifying trade-offs, and justifying why it's effective","Only technology","Only government action"],"Complete solution proposal."),
     ("AP scoring rubrics award points for:",["Length of response","*Specific, correct, relevant information — each point has clear earning criteria","Good handwriting","Vocabulary use only"],"Precision matters."),
     ("To maximize AP FRQ scores, students should:",["Write everything they know","*Answer exactly what is asked, be specific, provide evidence, and address all parts of the question","Write short answers","Only use bullet points"],"Targeted responses."),
     ("Energy efficiency calculations may ask: if a car gets 25 mpg and drives 12,000 mi/year, annual fuel use is:",["250 gallons","*480 gallons (12,000 ÷ 25)","1,200 gallons","120 gallons"],"Division."),
     ("If electricity costs $0.12/kWh and a household uses 900 kWh/month, monthly cost is:",["$90","*$108 (900 × $0.12)","$120","$900"],"Multiplication."),
     ("Percent change formula is:",["New − old","*(New − Old) ÷ Old × 100%","Old − new","New ÷ old"],"Standard formula."),
     ("If species count drops from 50 to 35 in a habitat, percent decline is:",["15%","25%","*30% ((50−35) ÷ 50 × 100)","35%"],"Percent change."),
     ("AP questions about LD50 (lethal dose 50%) test understanding of:",["Only chemistry","*Toxicology: the dose at which 50% of test organisms die — key for evaluating chemical hazards","Only ecology","Only one concept"],"Dose-response."),
     ("When time is limited on FRQs, prioritize:",["Writing introductions","*Answering the easiest parts first to secure points; returning to harder parts with remaining time","Perfect grammar","Long conclusions"],"Strategic time use."),
     ("Common AP mistakes include:",["Being too specific","*Not answering all parts of the question, being too vague, and not connecting evidence to claims","Only calculation errors","Only vocabulary errors"],"Avoid vagueness."),
     ("The best AP preparation strategy is:",["Memorize everything","*Practice with past exam questions, understand concepts deeply, connect topics across units, and practice calculations","Only read the textbook","Only make flashcards"],"Active practice.")]
)
lessons[k]=v

# 10.3
k,v = build_lesson(10,3,"Case Studies: AP APES",
    "<h3>Case Studies for AP APES</h3>"
    "<p>The AP exam frequently uses case studies to test application of environmental concepts to real-world situations.</p>"
    "<h4>Classic APES Case Studies</h4>"
    "<ul><li><b>Chesapeake Bay:</b> Nutrient pollution, dead zones, multi-state management.</li>"
    "<li><b>Aral Sea:</b> Water diversion for irrigation → ecological disaster.</li>"
    "<li><b>Easter Island:</b> Resource depletion and societal collapse.</li>"
    "<li><b>Three Gorges Dam:</b> Hydropower benefits vs. displacement and ecological costs.</li>"
    "<li><b>Ogallala Aquifer:</b> Groundwater depletion from agricultural irrigation.</li></ul>",
    [("Chesapeake Bay","Largest US estuary; impaired by nutrient runoff from agriculture and development; multi-state cleanup effort."),
     ("Aral Sea","Central Asian lake shrunk ~90% due to Soviet-era irrigation diversions — one of the worst environmental disasters."),
     ("Easter Island (Rapa Nui)","Example of societal collapse from overexploitation of resources (deforestation → soil erosion → population decline)."),
     ("Three Gorges Dam","World's largest hydroelectric dam (China): 22.5 GW capacity but displaced 1.3 million people and caused ecological damage."),
     ("Ogallala Aquifer","Massive US aquifer underlying 8 Great Plains states; being depleted faster than recharge for irrigation (~30% depleted).")],
    [("The Chesapeake Bay has dead zones caused by:",["Only industrial discharge","*Agricultural runoff (nitrogen and phosphorus) from farms across 6 states + DC, causing algal blooms and oxygen depletion","Only one source","Only natural processes"],"Multi-source nutrient pollution."),
     ("The Chesapeake Bay cleanup illustrates the difficulty of:",["Point-source pollution","*Managing non-point source pollution across multiple jurisdictions (6 states, complex watershed)","Single-source issues","Only local problems"],"Governance challenge."),
     ("The Aral Sea disaster was caused by:",["Climate change","*Soviet-era diversion of rivers (Amu Darya and Syr Darya) for cotton irrigation in Central Asia","Natural evaporation","Tectonic activity"],"Human-caused disaster."),
     ("The Aral Sea has shrunk by approximately:",["10%","50%","*~90% of its original volume (one of the planet's worst environmental disasters)","25%"],"Catastrophic shrinkage."),
     ("Consequences of the Aral Sea disaster include:",["Only less water","*Fisheries collapse, dust storms from exposed toxic seabed, climate changes, health crises, and economic devastation","Only one effect","Nothing significant"],"Multi-dimensional impacts."),
     ("Easter Island illustrates:",["Sustainable living","*Resource depletion and societal collapse — deforestation led to soil erosion, food decline, and population crash","Only isolation effects","Only cultural change"],"Cautionary tale."),
     ("Easter Island is often used as a metaphor for:",["Successful management","*Earth as a whole — an isolated system with finite resources that can be depleted if mismanaged","Only Polynesian culture","Only archaeology"],"Earth as an island."),
     ("The Three Gorges Dam produces _____ GW of hydroelectric capacity.",["5 GW","10 GW","*~22.5 GW (world's largest hydroelectric facility)","50 GW"],"Massive energy output."),
     ("Costs of the Three Gorges Dam include:",["Only financial costs","*Displacement of 1.3 million people, submerged archaeological sites, increased earthquake risk, disrupted river ecology, and sediment trapping","Only one cost","No significant costs"],"High social and environmental costs."),
     ("The Ogallala Aquifer is being depleted because:",["It recharges quickly","*Agricultural irrigation withdraws water far faster than the ~2,500-year natural recharge rate","It's not used much","Only industry uses it"],"Unsustainable withdrawal."),
     ("The Ogallala underlies _____ Great Plains states.",["2","4","*8 (supporting ~30% of US irrigated agriculture)","All 50"],"Regional importance."),
     ("The Deepwater Horizon spill (2010) demonstrated:",["Perfect safety","*Risks of deep-sea drilling: 4.9 million barrels of oil released, devastating Gulf ecosystems and fishing communities","Only minor damage","Only financial costs"],"Catastrophic spill."),
     ("Bhopal (1984) is relevant to APES because it illustrates:",["Safe industry","*The intersection of industrial pollution, environmental justice, and the disproportionate impact on vulnerable populations in developing countries","Only one issue","Only Indian problems"],"Industrial + equity."),
     ("Chernobyl (1986) and Fukushima (2011) demonstrate:",["Nuclear is perfectly safe","*Risks of nuclear energy: potential for catastrophic accidents with long-lasting environmental and health consequences","Only one incident","Only historical interest"],"Nuclear risk."),
     ("The Dust Bowl (1930s) was caused by:",["Only drought","*Over-plowing of Great Plains grasslands combined with severe drought → massive soil erosion and ecological disaster","Only farming","Only wind"],"Agricultural + climate."),
     ("For AP case study questions, students should:",["Only describe what happened","*Identify the environmental issue, explain causes, describe impacts on ecosystems AND humans, and evaluate solutions","Only list facts","Only give opinions"],"Full analysis required."),
     ("Case studies test ability to:",["Memorize events","*Apply environmental science concepts to real-world situations and analyze complex, multi-factor problems","Only name locations","Only cite dates"],"Applied knowledge."),
     ("The common thread in environmental case studies is:",["Problems are simple","*Environmental problems involve complex interactions between human activities and natural systems, often with unintended consequences","All problems are the same","Only technology fails"],"Complexity and interconnection."),
     ("Successful environmental case studies (e.g., ozone recovery) show that:",["Nothing works","*With scientific understanding, political will, and international cooperation, environmental problems CAN be solved","Only technology works","Only economics drives change"],"Hope for action."),
     ("For APES, be prepared to discuss _____ case studies in detail.",["Only one","*Multiple case studies across different topics (water, energy, pollution, biodiversity, climate, policy)","Only US examples","Only recent ones"],"Broad preparation.")]
)
lessons[k]=v

# 10.4
k,v = build_lesson(10,4,"Real-World Applications",
    "<h3>Environmental Science: Real-World Applications</h3>"
    "<h4>Connecting Science to Action</h4>"
    "<ul><li><b>Personal choices:</b> Energy use, transportation, diet, consumption, waste reduction.</li>"
    "<li><b>Community action:</b> Local environmental organizations, citizen science, city council advocacy.</li>"
    "<li><b>Career paths:</b> Environmental engineering, conservation biology, policy analysis, urban planning, renewable energy, environmental law.</li>"
    "<li><b>Technology solutions:</b> Remote sensing, GIS mapping, water treatment, carbon capture, precision agriculture.</li></ul>",
    [("Citizen Science","Public participation in scientific research: monitoring species, measuring air quality, reporting pollution."),
     ("GIS (Geographic Information Systems)","Computer-based tools for mapping, analyzing, and visualizing environmental data spatially."),
     ("Environmental Engineering","Designing solutions for environmental problems: water treatment, waste management, pollution control."),
     ("Remote Sensing","Using satellites and sensors to monitor environmental changes: deforestation, ice melt, water quality, and land use."),
     ("Environmental Careers","Growing fields: conservation biology, sustainability consulting, renewable energy, policy analysis, urban planning, environmental law.")],
    [("Individual actions that most reduce carbon footprint include:",["Only recycling","*Reducing flying, driving less or going electric, eating less meat, and choosing renewable energy","Only turning off lights","Only one action"],"High-impact personal choices."),
     ("Citizen science contributes to environmental research by:",["Replacing professional scientists","*Engaging the public in data collection at scales impossible for researchers alone (bird counts, water quality, phenology)","Only educating participants","Having no scientific value"],"Scalable data collection."),
     ("GIS technology helps environmental science by:",["Only making maps","*Visualizing and analyzing spatial patterns: habitat mapping, pollution tracking, land use change, climate modeling","Only for geography class","Only government use"],"Spatial analysis."),
     ("Remote sensing from satellites can monitor:",["Only weather","*Deforestation, sea level, ice extent, land use, ocean temperature, air quality, crop health, and urban growth","Only one variable","Only in rich countries"],"Global monitoring."),
     ("Environmental Impact Assessment (EIA) is used in real-world projects to:",["Delay projects only","*Evaluate potential environmental effects BEFORE construction begins, allowing mitigation measures to be incorporated","Only after construction","Only for large projects"],"Preventive evaluation."),
     ("Water treatment technology ensures safe drinking water through:",["Only filtering","*Multiple steps: coagulation, sedimentation, filtration, disinfection (chlorination, UV), and monitoring","Only chlorination","Only one step"],"Multi-barrier approach."),
     ("Precision agriculture uses technology to:",["Increase chemical use","*Apply water, fertilizer, and pesticides precisely where needed using GPS, sensors, and data — reducing waste and environmental impact","Only reduce labor","Only in large farms"],"Targeted inputs."),
     ("Carbon capture technology aims to:",["Only study CO₂","*Remove CO₂ from industrial emissions or the atmosphere and store it permanently (underground or in products)","Only from one source","Replace renewables"],"Emission removal."),
     ("Bioremediation uses _____ to clean up contaminated sites.",["Only chemicals","*Microorganisms and plants (bacteria, fungi, phytoremediation) that naturally break down or absorb pollutants","Only heat","Only excavation"],"Biological cleanup."),
     ("Phytoremediation specifically uses:",["Animals","*Plants to absorb, concentrate, or break down contaminants from soil and water","Only bacteria","Only fungi"],"Plant-based cleanup."),
     ("Environmental law careers involve:",["Only litigation","*Drafting legislation, enforcement, compliance advising, advocacy, international treaties, and environmental justice","Only one specialty","Only government work"],"Diverse legal roles."),
     ("Sustainability consulting helps organizations:",["Only save money","*Reduce environmental impact, comply with regulations, improve efficiency, and communicate sustainability to stakeholders","Only write reports","Only get certifications"],"Organizational sustainability."),
     ("Renewable energy engineers design and build:",["Only solar panels","*Solar, wind, geothermal, hydropower, and energy storage systems — rapidly growing career field","Only one technology","Only small systems"],"Clean energy systems."),
     ("Urban planners contribute to sustainability by:",["Only zoning","*Designing communities that are walkable, transit-connected, green, equitable, and resilient to climate change","Only on paper","Only for large cities"],"Community design."),
     ("Conservation biologists work to:",["Only study species","*Protect and restore biodiversity through research, habitat management, species recovery plans, and policy advocacy","Only in labs","Only in national parks"],"Applied biodiversity protection."),
     ("Environmental education is important because:",["Only for experts","*Informed citizens make better environmental decisions — from personal choices to voting for environmental policies","Only in school","Only for activists"],"Knowledge → action."),
     ("The environmental field is growing because:",["It's a passing trend","*Environmental challenges are intensifying (climate, biodiversity, pollution) and demand for solutions is rising across every sector","Only government-driven","Only in developed countries"],"Expanding need."),
     ("Interdisciplinary skills are essential in environmental careers because:",["Only one skill matters","*Environmental problems span science, policy, economics, communication, technology, and social justice — requiring diverse expertise","Only science matters","Only policy matters"],"Cross-disciplinary work."),
     ("For AP and beyond, the most important environmental skill is:",["Memorizing facts","*Systems thinking — understanding how environmental, economic, and social systems interact and affect each other","Only calculations","Only lab skills"],"Connecting the dots."),
     ("Environmental science empowers students to:",["Only pass the exam","*Understand the science behind environmental challenges AND become informed, engaged citizens who can make a difference","Only worry about problems","Only pursue careers"],"Knowledge + agency.")]
)
lessons[k]=v

# 10.5
k,v = build_lesson(10,5,"Capstone: Environmental Impact Study",
    "<h3>Capstone: Environmental Impact Study</h3>"
    "<p>This lesson guides students through conducting their own environmental impact analysis, integrating concepts from all units.</p>"
    "<h4>Steps for an Environmental Impact Study</h4>"
    "<ul><li><b>Step 1:</b> Define the project or action being assessed.</li>"
    "<li><b>Step 2:</b> Identify affected environmental components (air, water, soil, biodiversity, communities).</li>"
    "<li><b>Step 3:</b> Predict impacts (positive and negative, short-term and long-term).</li>"
    "<li><b>Step 4:</b> Evaluate significance and propose mitigation measures.</li>"
    "<li><b>Step 5:</b> Consider alternatives, including the 'no-action' alternative.</li>"
    "<li><b>Step 6:</b> Communicate findings with data, evidence, and recommendations.</li></ul>",
    [("Environmental Impact Statement (EIS)","Detailed document assessing the environmental effects of a proposed federal action, required under NEPA."),
     ("Baseline Assessment","Description of the current state of the environment before the proposed project (the 'before' picture)."),
     ("Mitigation Measures","Actions to avoid, minimize, or compensate for negative environmental impacts of a project."),
     ("No-Action Alternative","What happens if the proposed project is NOT undertaken — required comparison in all EIS documents."),
     ("Cumulative Impact Assessment","Evaluation of combined effects of a project along with other past, present, and reasonably foreseeable future actions.")],
    [("An Environmental Impact Statement (EIS) is required for:",["All projects","*Major federal actions significantly affecting the quality of the human environment (NEPA requirement)","Only private projects","Only state projects"],"Federal trigger."),
     ("A baseline assessment establishes:",["Future conditions","*Current environmental conditions before the project — the 'before' comparison for measuring impacts","Only one variable","Only human impacts"],"Starting point."),
     ("Scoping in an EIS process determines:",["Only cost","*Which environmental issues and alternatives should be studied in detail — narrowing focus to the most significant concerns","Only the timeline","Only public participation"],"Focus the analysis."),
     ("Public participation in the EIS process is important because:",["It's not important","*Affected communities have knowledge of local conditions and concerns that improve the analysis and legitimacy of decisions","Only a legal requirement","Only for activists"],"Community knowledge."),
     ("The 'no-action alternative' is required because it:",["Wastes time","*Provides a baseline comparison — what happens if we don't proceed? Sometimes the best option is no action","Only for formality","Is always the worst option"],"Comparison baseline."),
     ("Mitigation measures in an EIS follow a hierarchy:",["Only compensation","*Avoid → minimize → restore → compensate (avoid the impact first; compensation is the last resort)","Only avoidance","Only restoration"],"Mitigation hierarchy."),
     ("Cumulative impact assessment considers:",["Only the project alone","*The combined effects of the project PLUS other past, present, and foreseeable future actions in the area","Only one project","Only present conditions"],"Broader context."),
     ("Secondary (indirect) impacts include:",["Only direct construction damage","*Effects that are caused by the project but occur later or farther away (e.g., new road → development → habitat fragmentation)","Only on-site effects","Only immediate effects"],"Ripple effects."),
     ("Air quality impacts might be assessed through:",["Only observation","*Dispersion modeling, emission inventories, monitoring data, and comparison to NAAQS standards","Only one method","Only lab tests"],"Multi-method assessment."),
     ("Water impact assessment includes:",["Only one factor","*Quantity (flow, drainage), quality (pollutants, sediment, temperature), habitat (aquatic species, wetlands), and groundwater","Only surface water","Only drinking water"],"Comprehensive water analysis."),
     ("Biodiversity impact assessment examines:",["Only one species","*Habitat loss, fragmentation, species displacement, impacts on threatened/endangered species, and connectivity","Only mammals","Only rare species"],"Ecosystem-level review."),
     ("Social impact assessment evaluates:",["Only jobs","*Effects on communities: displacement, environmental justice, traffic, noise, visual impact, cultural resources, and economic changes","Only one factor","Only property values"],"Human community effects."),
     ("When conducting a student environmental impact study, the project could be:",["Only a real construction project","*Any proposed action: school renovation, local development proposal, park expansion, energy project, or even a hypothetical scenario","Only federal projects","Only large projects"],"Flexible scope."),
     ("Data collection for an impact study might include:",["Only library research","*Field observations, water/soil/air sampling, species surveys, community interviews, GIS analysis, and existing data review","Only one source","Only internet research"],"Multiple data sources."),
     ("Significance criteria for impacts consider:",["Only one factor","*Magnitude, duration, reversibility, spatial extent, and probability of the impact occurring","Only severity","Only cost"],"Multi-factor evaluation."),
     ("Alternatives analysis requires examining:",["Only the proposed action","*Multiple alternatives (including no-action) to compare trade-offs and identify the least-damaging feasible option","Only two options","Only the cheapest option"],"Options comparison."),
     ("Communicating EIS findings effectively requires:",["Only technical language","*Clear writing, visual aids (maps, graphs), executive summary, and accessible language for both experts and public audiences","Only charts","Only verbal presentations"],"Clear communication."),
     ("This capstone integrates knowledge from all units because environmental impacts involve:",["Only one discipline","*Ecosystems, pollution, resources, climate, policy, sustainability, and social justice — all interconnected","Only environmental science","Only policy"],"Full course integration."),
     ("The most valuable outcome of an environmental impact study is:",["The document itself","*Better-informed decision-making that considers environmental, social, and economic consequences before committing resources","Only compliance","Only a grade"],"Informed decisions."),
     ("For AP and career preparation, understanding EIS demonstrates:",["Only one skill","*Ability to apply environmental science to real-world decisions, analyze complex systems, and communicate findings clearly","Only academic knowledge","Only test preparation"],"Professional competency.")]
)
lessons[k]=v

# 10.6
k,v = build_lesson(10,6,"Comprehensive Review & AP Prep",
    "<h3>Comprehensive Review &amp; AP Prep</h3>"
    "<h4>Final Review Strategy</h4>"
    "<ul><li><b>Content mastery:</b> Review key concepts from all 9 units systematically.</li>"
    "<li><b>Connections:</b> Practice linking topics (e.g., agriculture → water pollution → dead zones → policy).</li>"
    "<li><b>Calculations:</b> Practice IPAT, percent change, per capita, Rule of 70, energy calculations.</li>"
    "<li><b>FRQ practice:</b> Write timed responses using Claim-Evidence-Reasoning format.</li>"
    "<li><b>Vocabulary:</b> Ensure all key terms can be defined AND applied in context.</li></ul>"
    "<h4>Top 10 APES Topics</h4>"
    "<p>Energy, water resources, air/water pollution, climate change, biodiversity, soil/agriculture, population, environmental law, sustainability, and environmental justice.</p>",
    [("Systems Thinking","Understanding how environmental, economic, and social systems interact — the core skill of environmental science."),
     ("Claim-Evidence-Reasoning","AP response framework: State a claim → Support with evidence → Explain reasoning connecting them."),
     ("Rule of 70","Doubling time = 70 ÷ growth rate (%). Quick estimate for population or economic doubling."),
     ("Per Capita Calculation","Total ÷ population = per capita rate. Used for footprint, waste, water, energy comparisons."),
     ("Interconnected Topics","Environmental science concepts are deeply connected: population → consumption → pollution → health → policy → sustainability.")],
    [("The most important strategy for the AP exam is:",["Memorizing everything","*Understanding concepts AND being able to apply them to novel situations with specific evidence","Only practicing FRQs","Only making flashcards"],"Applied understanding."),
     ("The Rule of 70 is used for:",["Only money","*Estimating doubling time: 70 ÷ growth rate (%) = years to double (works for population, investments, etc.)","Only population","Only energy"],"Quick estimation."),
     ("If world population is 8 billion and growing at 1%, doubling time is:",["10 years","35 years","*70 years (70 ÷ 1)","700 years"],"Rule of 70."),
     ("Per capita CO₂ calculations require:",["Only total emissions","*Dividing total national CO₂ emissions by population (important for comparing countries of different sizes)","Only population","Only one country's data"],"Total ÷ population."),
     ("Connecting agriculture to dead zones requires understanding:",["Only farming","*Fertilizer application → nutrient runoff → eutrophication → algal blooms → oxygen depletion → dead zone (cause-effect chain)","Only water pollution","Only one link"],"Full cause-effect chain."),
     ("For FRQs about proposing solutions, always include:",["Only one idea","*The solution, how it works, evidence it's effective, potential trade-offs, and why it's the best option","Only a description","Only costs"],"Complete analysis."),
     ("The difference between primary succession and secondary succession is:",["No difference","*Primary: colonization of bare substrate (no prior soil); Secondary: recovery after disturbance where soil remains","Only time","Only location"],"Starting conditions differ."),
     ("Competitive exclusion principle states:",["All species coexist","*Two species competing for the same limited resource cannot coexist — one will outcompete the other","Species never compete","Only predators compete"],"Niche separation."),
     ("The carbon cycle connects to climate change through:",["No connection","*Fossil fuel burning releases stored carbon as CO₂ → enhanced greenhouse effect → global warming → climate impacts","Only photosynthesis","Only decomposition"],"Carbon → climate."),
     ("Indicator species are useful because they:",["Are the most common","*Signal environmental conditions — their presence, absence, or health reflects ecosystem quality (e.g., amphibians for water quality)","Only indicate one thing","Are the most visible"],"Environmental signals."),
     ("Point-source pollution differs from non-point in that it:",["Is worse","*Comes from a single identifiable source (pipe, smokestack) vs. diffuse sources (runoff from land, atmospheric deposition)","Is always industrial","Cannot be regulated"],"Identifiable vs. diffuse."),
     ("For AP, always identify trade-offs when discussing solutions because:",["There are no trade-offs","*Every environmental solution involves trade-offs (economic costs, other environmental impacts, social effects) — acknowledging them shows sophistication","Only science matters","Only one perspective matters"],"Balanced analysis."),
     ("The relationship between biodiversity and ecosystem stability is:",["No relationship","*Greater biodiversity generally increases ecosystem resilience (more species = more functional redundancy and adaptive capacity)","Inverse","Only for forests"],"Diversity promotes stability."),
     ("Genetic diversity within species is important because:",["Only for breeding","*It provides raw material for adaptation to changing conditions — low genetic diversity = vulnerability to disease, environmental change","Only matters for rare species","Only for agriculture"],"Adaptive capacity."),
     ("When comparing developed and developing nations, remember:",["They're the same","*Different per capita impacts, historical responsibility, vulnerability to climate change, and capacity to adapt — equity matters","Only GDP differences","Only population differences"],"Equity in analysis."),
     ("Feedback loops in environmental systems:",["Don't exist","*Can amplify change (positive feedback: ice melt → less reflection → more warming) or stabilize (negative feedback: predator-prey balance)","Only amplify","Only stabilize"],"System dynamics."),
     ("For quantitative AP questions, show all work because:",["Partial credit doesn't exist","*Correct process with an arithmetic error can still earn most points — and showing reasoning demonstrates understanding","Only final answers matter","It's faster to skip"],"Process earns points."),
     ("The AP exam tests environmental science as:",["Isolated facts","*An integrated, interdisciplinary science where concepts connect across topics — the exam rewards systems thinking","Only biology","Only chemistry"],"Integrated science."),
     ("A final study tip: focus on understanding _____ rather than memorizing facts.",["Vocabulary","*Cause-and-effect relationships and connections between topics (WHY things happen and HOW they connect)","Dates and names","Only definitions"],"Understanding over memorization."),
     ("Environmental science ultimately teaches that:",["Nature is boring","*Human choices shape Earth's future — informed, engaged citizens who understand environmental systems can create positive change","Nothing matters","Only scientists can help"],"Empowerment through knowledge.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 10: wrote {len(lessons)} lessons")
