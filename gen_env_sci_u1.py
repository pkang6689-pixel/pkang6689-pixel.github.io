#!/usr/bin/env python3
"""Environmental Science Unit 1 – Intro & Ecosystems (7 lessons)."""
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

# 1.1
k,v = build_lesson(1,1,"What is Environmental Science?",
    "<h3>What is Environmental Science?</h3>"
    "<p>Environmental science is the interdisciplinary study of how humans interact with the environment. It integrates biology, chemistry, physics, geology, economics, and social sciences to understand and solve environmental problems.</p>"
    "<h4>Key Themes</h4>"
    "<ul><li><b>Science and the environment:</b> Using the scientific method to study natural systems.</li>"
    "<li><b>Human impact:</b> Agriculture, industry, urbanization, and resource consumption alter ecosystems.</li>"
    "<li><b>Sustainability:</b> Meeting present needs without compromising future generations' ability to meet theirs.</li></ul>",
    [("Environmental Science","Interdisciplinary study of how humans interact with the natural environment."),
     ("Sustainability","Meeting present needs without compromising future generations' ability to meet theirs (Brundtland definition)."),
     ("Anthropogenic","Caused or influenced by human activity (e.g., anthropogenic climate change)."),
     ("Ecosystem","A community of organisms interacting with their physical environment as a functional unit."),
     ("Scientific Method","Systematic process: observation → hypothesis → experiment → analysis → conclusion.")],
    [("Environmental science is best described as:",["A single discipline","*An interdisciplinary field integrating biology, chemistry, physics, geology, and social sciences","Only biology","Only chemistry"],"Broad integration."),
     ("The Brundtland definition of sustainability states:",["Use all resources now","*Meet present needs without compromising future generations' ability to meet theirs","Sustainability is impossible","Only save endangered species"],"1987 UN report."),
     ("'Anthropogenic' means:",["Natural","*Caused by human activity","Animal-related","Ancient"],"Human-caused."),
     ("Environmental science differs from ecology because it:",["Is the same","*Includes social, economic, and political dimensions in addition to ecological study","Ignores biology","Only studies animals"],"Broader scope."),
     ("The scientific method in environmental science begins with:",["A conclusion","*An observation or question about an environmental phenomenon","A guess","A law"],"First step."),
     ("Which is an example of a renewable resource?",["Coal","Oil","*Solar energy","Natural gas"],"Inexhaustible on human timescales."),
     ("Nonrenewable resources:",["Regenerate quickly","*Are consumed faster than they can be replenished (e.g., fossil fuels, minerals)","Are unlimited","Include sunlight"],"Finite supply."),
     ("An ecosystem includes:",["Only animals","Only plants","*All living organisms AND their physical environment interacting as a system","Only water"],"Biotic + abiotic."),
     ("The tragedy of the commons describes:",["Conservation success","*The depletion of shared resources when individuals act in self-interest (Garrett Hardin, 1968)","A fictional story","Property rights"],"Overexploitation of shared resources."),
     ("Ecological footprint measures:",["Shoe size","*The amount of biologically productive land and water needed to support a person or population","Building size","Carbon only"],"Resource demand metric."),
     ("Environmental science emerged as a field largely in response to:",["Industrial revolution only","*Growing environmental crises (pollution, habitat loss, resource depletion) in the 20th century","One event","Political campaigns"],"Driven by problems."),
     ("Rachel Carson's 'Silent Spring' (1962) focused on:",["Air pollution","*The harmful effects of pesticides (DDT) on ecosystems and human health","Water scarcity","Deforestation"],"Landmark publication."),
     ("A hypothesis must be:",["Proven true","*Testable and falsifiable","A fact","A law"],"Scientific requirement."),
     ("Controlled experiments in environmental science are often difficult because:",["They're easy","*Environmental systems are complex with many interacting variables difficult to isolate","Equipment is lacking","No one tries"],"Field complexity."),
     ("Environmental indicators include:",["Only temperature","*Biodiversity indices, water quality metrics, air quality indices, and carbon emissions","Only one measure","Only opinion"],"Multiple measures."),
     ("The precautionary principle states that:",["Always wait for proof","*If an action could cause harm, take preventive measures even without complete scientific certainty","Never act","Ignore risk"],"Better safe than sorry."),
     ("Peer review in environmental science ensures:",["Publication speed","*Quality control — other experts evaluate research methods, data, and conclusions before publication","No publication","Only agreement"],"Scientific rigor."),
     ("Environmental science addresses problems at _____ scale(s).",["Only local","Only global","*Local, regional, national, and global scales","Only national"],"Multi-scale."),
     ("An environmental worldview is:",["Irrelevant","*A person's set of assumptions about the world that shapes their relationship with the environment","Always the same for everyone","Only scientific"],"Influences behavior."),
     ("Understanding environmental science is important because:",["It's not","*Human survival depends on maintaining functional ecosystems, clean air/water, and sustainable resource use","Only for scientists","Only for politicians"],"Essential for everyone.")]
)
lessons[k]=v

# 1.2
k,v = build_lesson(1,2,"Interdisciplinary Nature of the Field",
    "<h3>Interdisciplinary Nature of the Field</h3>"
    "<p>Environmental science draws on multiple disciplines:</p>"
    "<ul><li><b>Biology/Ecology:</b> Species interactions, ecosystems, biodiversity.</li>"
    "<li><b>Chemistry:</b> Pollutant behavior, biogeochemical cycles, water chemistry.</li>"
    "<li><b>Physics:</b> Energy flow, thermodynamics, climate dynamics.</li>"
    "<li><b>Geology:</b> Soil science, mineral resources, natural hazards.</li>"
    "<li><b>Social Sciences:</b> Economics (cost-benefit), policy, ethics, demographics.</li>"
    "<li><b>Engineering:</b> Pollution control, renewable energy technology, sustainable design.</li></ul>",
    [("Ecology","Study of interactions between organisms and their environment; a foundational discipline of environmental science."),
     ("Toxicology","Study of harmful effects of chemicals on organisms; key for pollution assessment."),
     ("Environmental Economics","Applies economic principles to environmental issues (cost-benefit analysis, externalities, valuation)."),
     ("Environmental Ethics","Philosophical examination of moral relationships between humans and the natural world."),
     ("GIS","Geographic Information Systems; spatial analysis tools for mapping and analyzing environmental data.")],
    [("Environmental science integrates at least _____ major disciplines.",["1","2","*Multiple (biology, chemistry, physics, geology, social sciences, engineering)","Only one"],"Inherently interdisciplinary."),
     ("Ecology contributes to environmental science by:",["Studying economics","*Understanding species interactions, energy flow, and ecosystem dynamics","Only naming species","Only studying soil"],"Ecological foundation."),
     ("Chemistry is essential for understanding:",["Only cooking","*Pollutant behavior, biogeochemical cycles, water quality, and atmospheric chemistry","Only labs","Only explosions"],"Chemical processes."),
     ("Environmental economics addresses:",["Only profit","*Externalities (hidden costs of pollution), cost-benefit analysis, and ecosystem services valuation","Only trade","Only taxes"],"Economic dimension."),
     ("An externality is:",["A hidden benefit","*A cost or benefit that affects parties not directly involved in a transaction (e.g., factory pollution affecting neighbors)","A tax","A subsidy"],"Market failure."),
     ("Environmental ethics asks questions like:",["How to make money","*Do other species have intrinsic value? What responsibilities do we have to future generations?","Who owns nature?","Only legal questions"],"Moral dimension."),
     ("GIS is used in environmental science to:",["Play games","*Map habitats, track pollution, model land use, analyze spatial patterns, and plan conservation","Only make pretty maps","Only for military"],"Spatial analysis."),
     ("Toxicology helps environmental scientists:",["Create poisons","*Assess the harmful effects of chemicals on organisms and determine safe exposure levels","Only treat patients","Only study animals"],"Dose makes the poison."),
     ("LD50 is a toxicology measure representing:",["50% survival","*The dose at which 50% of test organisms die — a standard measure of acute toxicity","50 lectures","A perfect score"],"Lethal dose 50%."),
     ("Bioaccumulation occurs when:",["Toxins decrease","*An organism absorbs a substance faster than it can eliminate it, building up concentration over time","Nothing changes","Toxins are harmless"],"Increasing concentration."),
     ("Biomagnification refers to:",["Decreasing toxin levels","*Increasing concentration of toxins at higher trophic levels in a food chain","Magnifying glasses","Microscopy"],"DDT in eagles."),
     ("Environmental policy draws on:",["Only science","*Science, economics, law, ethics, and public opinion to create regulations and incentives","Only politics","Only emotion"],"Multi-factor."),
     ("Remote sensing helps environmental scientists by:",["Nothing","*Providing satellite and aerial data on land use, deforestation, ocean health, and atmospheric conditions","Only astronomy","Only weather"],"Earth observation."),
     ("Environmental engineering designs:",["Only buildings","*Solutions to environmental problems: water treatment, pollution control, waste management, renewable energy systems","Only roads","Only bridges"],"Applied solutions."),
     ("Demographic data is important because:",["It's not","*Population size, growth, and distribution directly affect resource use, pollution, and habitat destruction","Only for census","Only for marketing"],"Population-environment link."),
     ("Soil science (pedology) is critical for:",["Only farming","*Understanding agriculture, erosion, nutrient cycling, water filtration, and carbon storage","Only construction","Only geology"],"Foundation of terrestrial ecosystems."),
     ("The interdisciplinary approach is necessary because:",["Simple problems only need one field","*Environmental problems are complex, with interconnected ecological, economic, and social dimensions","It's trendy","Only for degrees"],"Real-world complexity."),
     ("Environmental justice combines:",["Only law","*Social science, ethics, and environmental science to address disproportionate environmental burdens on marginalized communities","Only charity","Only politics"],"Equity issue."),
     ("Systems thinking in environmental science means:",["Linear thinking","*Understanding interconnections, feedback loops, and emergent properties of complex environmental systems","Only part analysis","Simple solutions"],"Holistic approach."),
     ("The value of interdisciplinary study is demonstrated by:",["It having no value","*Complex problems like climate change requiring expertise from ALL disciplines to understand and solve","Only one example","Only theory"],"Climate change is the ultimate interdisciplinary challenge.")]
)
lessons[k]=v

# 1.3
k,v = build_lesson(1,3,"Ecosystem Basics (Producers, Consumers, Decomposers)",
    "<h3>Ecosystem Basics</h3>"
    "<h4>Trophic Levels</h4>"
    "<ul><li><b>Producers (autotrophs):</b> Photosynthesizers (plants, algae, cyanobacteria) and chemosynthesizers.</li>"
    "<li><b>Primary consumers (herbivores):</b> Eat producers (deer, grasshoppers, zooplankton).</li>"
    "<li><b>Secondary consumers:</b> Eat primary consumers (frogs, small fish).</li>"
    "<li><b>Tertiary consumers:</b> Top predators (hawks, sharks, lions).</li>"
    "<li><b>Decomposers:</b> Bacteria and fungi break down dead matter, recycling nutrients.</li></ul>"
    "<p><b>10% Rule:</b> Approximately 10% of energy transfers between trophic levels; ~90% lost as heat.</p>",
    [("Producer (Autotroph)","Organisms that make their own food from inorganic matter (photosynthesis or chemosynthesis)."),
     ("Consumer (Heterotroph)","Organisms that obtain energy by eating other organisms."),
     ("Decomposer","Organisms (bacteria, fungi) that break down dead organic matter, recycling nutrients back to the ecosystem."),
     ("Trophic Level","A feeding position in a food chain (producer = level 1, primary consumer = level 2, etc.)."),
     ("10% Rule","Approximately 10% of energy is transferred from one trophic level to the next; ~90% lost as metabolic heat.")],
    [("Producers are also called:",["Heterotrophs","*Autotrophs (they make their own food)","Decomposers","Consumers"],"Self-feeders."),
     ("Photosynthesis converts:",["Organic matter to CO₂","*CO₂ + H₂O + sunlight → glucose + O₂","O₂ to CO₂","Heat to light"],"6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂."),
     ("Primary consumers are:",["Carnivores","*Herbivores (they eat producers)","Omnivores only","Decomposers"],"First consumer level."),
     ("A food chain typically has _____ trophic levels because of energy loss.",["1–2","*3–5 (limited by the 10% rule)","10–20","Unlimited"],"Energy limits chain length."),
     ("If a producer has 10,000 kcal of energy, how much is available to tertiary consumers?",["1,000","100","*10 kcal (10,000 → 1,000 → 100 → 10)","1"],"Three 10% transfers."),
     ("Decomposers are essential because they:",["Eat living organisms","*Recycle nutrients from dead matter back into the soil and atmosphere for reuse","Produce oxygen","Create energy"],"Nutrient recycling."),
     ("An example of a decomposer is:",["A hawk","A deer","*Fungi (mushrooms) and bacteria","A grass plant"],"Break down dead matter."),
     ("Detritivores differ from decomposers in that they:",["Are the same","*Physically break down dead material by consuming it (e.g., earthworms, millipedes) while decomposers chemically break it down","Only eat plants","Produce food"],"Physical vs. chemical breakdown."),
     ("In a food web, organisms can occupy:",["Only one trophic level","*Multiple trophic levels (omnivores eat at different levels)","No levels","Level 0"],"Omnivores span levels."),
     ("Net primary productivity (NPP) is:",["Total photosynthesis","*Gross primary productivity minus plant respiration — the energy available to consumers","Only animal energy","Energy in soil"],"GPP - R = NPP."),
     ("Which biome has the highest NPP?",["Desert","Tundra","*Tropical rainforest (and estuaries/coral reefs in aquatic systems)","Arctic"],"High sunlight, water, and nutrients."),
     ("Energy enters most ecosystems through:",["Geology","*Sunlight (captured by photosynthetic producers)","Wind","Water"],"Solar energy drives ecosystems."),
     ("Chemosynthesis occurs in:",["Forests","*Deep-sea hydrothermal vents and other light-deprived environments","Deserts","Grasslands"],"Chemical energy source."),
     ("An apex predator is:",["A primary consumer","*A top predator with no natural predators (e.g., wolves, great white sharks, eagles)","A producer","A decomposer"],"Top of the food chain."),
     ("Keystone species have disproportionately large effects because:",["They're big","*Removing them causes significant ecosystem changes despite their relatively small population","They're common","They decompose matter"],"E.g., sea otters, wolves."),
     ("Trophic cascades occur when:",["Nothing changes","*Changes at one trophic level ripple through the food web (e.g., removing wolves affects elk affects vegetation)","Only one species is affected","Energy increases"],"Top-down effects."),
     ("Biomass pyramids are usually widest at the _____ level.",["Top","*Bottom (producers have the most biomass in most ecosystems)","Middle","It varies randomly"],"Energy ↔ biomass relationship."),
     ("In aquatic ecosystems, phytoplankton serve as:",["Consumers","*The primary producers (photosynthesizers forming the base of oceanic food webs)","Decomposers","Top predators"],"Microscopic autotrophs."),
     ("The 10% rule means food chains are energy-_____ systems.",["Efficient","*Inefficient (90% of energy is lost as heat at each transfer)","Closed","Perfect"],"Second law of thermodynamics."),
     ("Understanding trophic structure is essential for:",["Nothing","*Conservation planning, fisheries management, pollution assessment, and ecosystem health evaluation","Only farming","Only cooking"],"Applied ecology.")]
)
lessons[k]=v

# 1.4
k,v = build_lesson(1,4,"Biogeochemical Cycles (Carbon, Nitrogen, Water)",
    "<h3>Biogeochemical Cycles</h3>"
    "<h4>Carbon Cycle</h4>"
    "<p>Photosynthesis (removes CO₂), respiration/decomposition (releases CO₂), fossil fuel combustion, ocean absorption. Human burning of fossil fuels accelerates atmospheric CO₂ (pre-industrial ~280 ppm → 2024 ~425 ppm).</p>"
    "<h4>Nitrogen Cycle</h4>"
    "<p>N₂ (78% of atmosphere) → fixed by bacteria/lightning → NH₃ → NO₂⁻ → NO₃⁻ (usable by plants) → consumed by animals → decomposition/denitrification returns N₂. Haber-Bosch process produces synthetic fertilizer.</p>"
    "<h4>Water Cycle</h4>"
    "<p>Evaporation → condensation → precipitation → runoff/infiltration → groundwater → transpiration. Human impacts: damming, irrigation, groundwater depletion, pollution.</p>",
    [("Carbon Cycle","Movement of carbon through atmosphere, biosphere, oceans, and lithosphere; photosynthesis and respiration are key processes."),
     ("Nitrogen Fixation","Conversion of atmospheric N₂ into usable forms (NH₃) by bacteria or the Haber-Bosch process."),
     ("Denitrification","Conversion of nitrates back to N₂ gas by bacteria; returns nitrogen to the atmosphere."),
     ("Water Cycle (Hydrologic Cycle)","Continuous movement of water: evaporation, condensation, precipitation, runoff, infiltration, transpiration."),
     ("Haber-Bosch Process","Industrial process converting N₂ + H₂ into ammonia (NH₃) for fertilizer; doubled global food production.")],
    [("The carbon cycle includes all EXCEPT:",["Photosynthesis","Respiration","Fossil fuel combustion","*Nitrogen fixation (that's the nitrogen cycle)"],"Carbon-specific processes."),
     ("Photosynthesis removes _____ from the atmosphere.",["O₂","Nitrogen","*CO₂ (converted to glucose using sunlight)","Water"],"Carbon sink."),
     ("Burning fossil fuels releases carbon that was stored:",["Last year","*Millions of years ago (ancient organisms converted to coal, oil, gas)","Yesterday","In the ocean only"],"Geological carbon."),
     ("Pre-industrial CO₂ was ~280 ppm. Current levels are approximately:",["280 ppm","*~425 ppm (as of 2024)","100 ppm","1,000 ppm"],"~50% increase."),
     ("The largest carbon reservoir on Earth is:",["The atmosphere","Forests","*The ocean (dissolved CO₂ and carbonate) and sedimentary rocks","Animals"],"Deep storage."),
     ("In the nitrogen cycle, nitrogen fixation converts:",["NO₃⁻ to N₂","*N₂ (atmospheric gas) to NH₃ (ammonia, usable by organisms)","NH₃ to N₂","Nothing"],"Making N available."),
     ("The Haber-Bosch process is significant because:",["It's old","*It produces synthetic ammonia fertilizer, enabling modern agriculture to feed billions","It's natural","It removes nitrogen"],"Revolutionary for food production."),
     ("Excess nitrogen fertilizer in waterways causes:",["Clean water","*Eutrophication (algal blooms → oxygen depletion → dead zones)","Drought","Cleaner air"],"Nutrient pollution."),
     ("Denitrification returns nitrogen to the atmosphere as:",["NH₃","*N₂ gas (and some N₂O, a greenhouse gas)","NO₃⁻","Protein"],"Completing the cycle."),
     ("In the water cycle, transpiration is:",["Rain","*Water vapor released by plants through their leaves (stomata)","Condensation","Erosion"],"Plant contribution."),
     ("Groundwater is accessed by:",["Evaporation","*Wells that tap aquifers (underground water-bearing layers)","Condensation","Sublimation"],"Subsurface water."),
     ("Aquifer depletion occurs when:",["Rain increases","*Groundwater is pumped out faster than it's recharged","Rivers flood","Nothing changes"],"Ogallala Aquifer example."),
     ("The phosphorus cycle differs from carbon and nitrogen because:",["It's the same","*Phosphorus has no significant atmospheric phase — it cycles through rocks, soil, water, and organisms","It only involves air","It's not a cycle"],"No gas phase."),
     ("Ocean acidification is caused by:",["Nitrogen","*CO₂ dissolving in seawater forming carbonic acid (lowering pH)","Phosphorus","Sulfur"],"CO₂ + H₂O → H₂CO₃."),
     ("Carbon sinks include:",["Factories","*Forests, oceans, and soil (they absorb more carbon than they release)","Volcanoes only","Cars"],"Net carbon absorption."),
     ("Carbon sources include:",["Forests absorbing CO₂","*Fossil fuel combustion, deforestation, and volcanic eruptions (net CO₂ release)","Oceans absorbing CO₂","Photosynthesis"],"Net carbon release."),
     ("Nitrification is the conversion of:",["N₂ to NH₃","*NH₃ (ammonia) to NO₂⁻ then NO₃⁻ (nitrate) by bacteria","NO₃⁻ to N₂","Protein to NH₃"],"Bacterial oxidation step."),
     ("Human impacts on the water cycle include:",["Nothing","*Damming rivers, irrigation, groundwater depletion, deforestation, and pollution","Only rainfall","Only evaporation"],"Multiple disruptions."),
     ("Biogeochemical cycles are called 'cycles' because:",["They happen once","*Matter is continuously recycled through different forms and reservoirs — it's not created or destroyed","They go in circles geographically","Only water cycles"],"Conservation of matter."),
     ("Understanding biogeochemical cycles is critical for AP because:",["It's not tested","*They underpin pollution, climate change, agriculture, and ecosystem health — core AP topics","Only for extra credit","Only for lab work"],"Fundamental concepts.")]
)
lessons[k]=v

# 1.5
k,v = build_lesson(1,5,"Sustainability Concepts",
    "<h3>Sustainability Concepts</h3>"
    "<h4>Three Pillars</h4>"
    "<ul><li><b>Environmental:</b> Maintaining healthy ecosystems, biodiversity, and natural resources.</li>"
    "<li><b>Economic:</b> Long-term economic viability without depleting natural capital.</li>"
    "<li><b>Social:</b> Equity, justice, health, education, and community well-being.</li></ul>"
    "<h4>Key Metrics</h4>"
    "<ul><li>Ecological footprint, carbon footprint, IPAT equation (Impact = Population × Affluence × Technology).</li>"
    "<li>Sustainable Development Goals (SDGs): 17 UN goals for 2030.</li></ul>",
    [("Three Pillars of Sustainability","Environmental, economic, and social dimensions — all must be balanced for true sustainability."),
     ("Ecological Footprint","Measure of how much biologically productive land and water is needed to support a population's consumption."),
     ("IPAT Equation","Impact = Population × Affluence × Technology; framework for understanding human environmental impact."),
     ("SDGs","United Nations Sustainable Development Goals; 17 goals for 2030 addressing poverty, health, environment, and more."),
     ("Natural Capital","The world's stock of natural resources (air, water, soil, biodiversity) that provide ecosystem services.")],
    [("The three pillars of sustainability are:",["Air, water, soil","*Environmental, economic, and social","Past, present, future","Local, national, global"],"Triple bottom line."),
     ("The IPAT equation states that environmental impact equals:",["Only population","*Population × Affluence × Technology","Only technology","Only consumption"],"I = P × A × T."),
     ("Ecological footprint measures:",["Land area","*The biologically productive area needed to support a given population's resource consumption and waste absorption","Carbon only","Water only"],"Comprehensive metric."),
     ("If humanity's ecological footprint exceeds Earth's biocapacity, we are in:",["Balance","*Ecological overshoot (using resources faster than they regenerate)","Surplus","Equilibrium"],"Currently >1.7 Earths."),
     ("Earth Overshoot Day marks when:",["New Year begins","*Humanity has used all the biological resources Earth regenerates in that year","Summer solstice","A holiday"],"Getting earlier each year."),
     ("The UN's Sustainable Development Goals include _____ goals.",["5","10","*17","50"],"Adopted 2015, target 2030."),
     ("Natural capital refers to:",["Money in a bank","*Earth's stock of natural resources that provide valuable ecosystem services","Man-made goods","Technology"],"Nature as asset."),
     ("Ecosystem services include:",["Only food","*Pollination, water purification, carbon sequestration, flood control, and recreation","Only wood","Only minerals"],"Nature's benefits to humans."),
     ("A carbon footprint measures:",["Weight","*Total greenhouse gas emissions caused by an individual, organization, or product (in CO₂ equivalents)","Height","Area"],"Climate metric."),
     ("The 'T' in IPAT can reduce impact when:",["Technology increases consumption","*Technology improves efficiency (e.g., more food per acre, cleaner energy per unit)","Technology is ignored","Technology doesn't matter"],"Technology can help or hurt."),
     ("Cradle-to-cradle design means:",["Disposing after use","*Products are designed so all materials can be recycled or composted — no waste","Only production matters","Use once then discard"],"Circular economy."),
     ("The circular economy contrasts with the linear economy by:",["Being the same","*Reusing, repairing, and recycling materials instead of the 'take-make-dispose' model","Only recycling","Only reducing"],"Waste = food."),
     ("Life cycle assessment (LCA) evaluates:",["Only production","*Environmental impact of a product from raw material extraction through disposal (cradle to grave)","Only disposal","Only packaging"],"Full lifecycle analysis."),
     ("Greenwashing is:",["Genuine sustainability","*Misleading marketing that makes products appear more environmentally friendly than they are","Washing with green soap","A type of recycling"],"Consumer awareness issue."),
     ("Per capita ecological footprint is highest in:",["Developing countries","*High-income countries (US, Australia, Gulf states) due to high consumption","All countries equally","No country"],"Consumption-driven."),
     ("Carrying capacity relates to sustainability because:",["It doesn't","*Exceeding carrying capacity leads to resource depletion, ecosystem degradation, and population decline","It's only about animals","It's theoretical only"],"Population limits."),
     ("Triple bottom line accounting considers:",["Only profit","*Profit, people, and planet (economic, social, environmental performance)","Only environmental cost","Only social cost"],"Holistic business metric."),
     ("Renewable resources are sustainable only if:",["Always sustainable","*They are used at or below their rate of regeneration","Never sustainable","Used in any amount"],"Harvest ≤ regeneration."),
     ("Intergenerational equity means:",["Only helping current people","*Ensuring future generations have access to the same or better resources and environmental quality","Ignoring the future","Only economic equality"],"Fairness across time."),
     ("Sustainability concepts are foundational to AP Environmental Science because:",["They're not tested","*Nearly every AP topic connects back to sustainable resource use and human-environment interactions","Only one unit covers them","They're too simple"],"Overarching theme.")]
)
lessons[k]=v

# 1.6
k,v = build_lesson(1,6,"Case Studies in Environmental Issues",
    "<h3>Case Studies in Environmental Issues</h3>"
    "<h4>Dust Bowl (1930s)</h4>"
    "<p>Overplowing Great Plains → topsoil loss → massive dust storms. Led to soil conservation practices and the Soil Conservation Service.</p>"
    "<h4>Aral Sea Shrinkage</h4>"
    "<p>Soviet-era irrigation diverted rivers → Aral Sea shrank ~90%. Fisheries collapsed, salt/dust storms, health crises.</p>"
    "<h4>Ozone Hole</h4>"
    "<p>CFCs destroyed stratospheric ozone → UV radiation risk. Montreal Protocol (1987) phased out CFCs; ozone recovering.</p>",
    [("Dust Bowl","1930s ecological disaster caused by drought and overplowing; massive topsoil erosion on the Great Plains."),
     ("Aral Sea","Once the 4th-largest lake; shrank ~90% due to Soviet irrigation diversions; ecological and health disaster."),
     ("Ozone Hole","Seasonal thinning of stratospheric ozone over Antarctica caused by CFCs; allows harmful UV radiation."),
     ("Montreal Protocol","1987 international agreement phasing out ozone-depleting substances (CFCs); widely considered a success."),
     ("CFCs","Chlorofluorocarbons; industrial chemicals that destroy stratospheric ozone; banned under the Montreal Protocol.")],
    [("The Dust Bowl was primarily caused by:",["Natural drought alone","*A combination of severe drought and human overplowing that destroyed native grassland","Flooding","Volcanic eruption"],"Human + natural factors."),
     ("The Dust Bowl led to creation of the:",["EPA","*Soil Conservation Service (now NRCS) and conservation farming practices","NASA","FDA"],"Policy response."),
     ("The Aral Sea shrank because:",["Climate change alone","*Soviet irrigation projects diverted the rivers feeding it","Natural evaporation","Earthquake"],"Human water diversion."),
     ("Consequences of the Aral Sea's shrinkage include:",["Improved fishing","*Fishery collapse, toxic dust storms (pesticides in exposed seabed), and severe health problems","Better climate","No consequences"],"Multiple disasters."),
     ("Stratospheric ozone depletion is caused primarily by:",["CO₂","*CFCs (chlorofluorocarbons) and related halogenated compounds","Methane","Water vapor"],"Catalytic destruction."),
     ("The Montreal Protocol (1987) is considered successful because:",["It failed","*CFC production dropped dramatically and the ozone layer is showing signs of recovery","Only a few countries signed","It was never implemented"],"Model international agreement."),
     ("The ozone hole is most severe over:",["The equator","North America","*Antarctica (due to polar vortex conditions that concentrate ozone-depleting reactions)","Europe"],"Polar stratospheric clouds."),
     ("Love Canal (1970s) was a case of:",["Natural disaster","*Hazardous chemical waste buried underground contaminating a residential neighborhood in New York","Successful cleanup","A canal for transportation"],"Led to CERCLA/Superfund."),
     ("The Cuyahoga River (Cleveland) caught fire in 1969 due to:",["Natural causes","*Severe industrial pollution (oil and chemical contamination)","Lightning","Arson"],"Catalyzed Clean Water Act."),
     ("Bhopal disaster (1984, India) involved:",["A nuclear accident","*A toxic gas leak (methyl isocyanate) from a Union Carbide pesticide plant — thousands died","An oil spill","A flood"],"Worst industrial accident."),
     ("Chernobyl (1986) demonstrated:",["Nuclear safety","*The catastrophic potential of nuclear accidents — radiation contaminated large areas of Europe","Nothing","Only local effects"],"Nuclear risk."),
     ("The Deepwater Horizon spill (2010) released ~4.9 million barrels of oil into:",["The Pacific Ocean","*The Gulf of Mexico","The Atlantic Ocean","The Mediterranean"],"Largest marine oil spill."),
     ("These case studies share the common lesson that:",["Environmental problems solve themselves","*Prevention is far more effective and cheaper than cleanup after environmental damage occurs","Technology always fixes problems","Problems are inevitable"],"Prevention > cleanup."),
     ("The success of the Montreal Protocol suggests that:",["International agreements don't work","*When there is clear scientific evidence and political will, international environmental agreements can succeed","Nothing","Only unilateral action works"],"Proof of concept."),
     ("Environmental impact assessments (EIAs) were developed to:",["Speed up projects","*Evaluate potential environmental effects BEFORE major projects proceed","Only delay projects","Increase costs"],"Preventive tool."),
     ("The Flint water crisis (2014–2019) involved:",["Air pollution","*Lead contamination of drinking water due to cost-cutting measures that corroded old pipes","Flooding","Drought"],"Environmental justice issue."),
     ("The Amazon deforestation case shows:",["Forests are expanding","*Clearing for agriculture and cattle ranching destroys biodiversity, carbon storage, and indigenous communities","Only local effects","No consequences"],"Global implications."),
     ("The Great Pacific Garbage Patch illustrates:",["Clean oceans","*The accumulation of plastic waste in ocean gyres — a growing pollution crisis","A myth","Only near shores"],"Marine plastic pollution."),
     ("Learning from case studies helps because:",["History doesn't repeat","*Understanding past successes and failures guides better environmental policy and decision-making","Only for historians","Case studies are outdated"],"Evidence-based policy."),
     ("These case studies demonstrate the importance of:",["Ignoring warning signs","*Early action, scientific evidence, international cooperation, and holding polluters accountable","Only technology","Only economics"],"Integrated response.")]
)
lessons[k]=v

# 1.7
k,v = build_lesson(1,7,"AP Prep: Systems Thinking",
    "<h3>AP Prep: Systems Thinking</h3>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>Open vs. closed systems:</b> Open exchange matter and energy (most ecosystems); closed exchange only energy (Earth for matter, approximately).</li>"
    "<li><b>Feedback loops:</b> Positive (amplifying: ice melt → less reflection → more warming) and negative (stabilizing: predator-prey cycles).</li>"
    "<li><b>Inputs, outputs, throughputs:</b> Energy and matter flow through systems.</li>"
    "<li><b>Emergent properties:</b> Properties arising from system interactions that individual components don't possess.</li></ul>",
    [("Open System","System that exchanges both matter and energy with its surroundings (e.g., an ecosystem)."),
     ("Closed System","System that exchanges energy but not matter with its surroundings (Earth, approximately)."),
     ("Positive Feedback Loop","Amplifying loop: output reinforces the change (e.g., ice-albedo feedback accelerating warming)."),
     ("Negative Feedback Loop","Stabilizing loop: output counteracts the change (e.g., predator-prey regulation)."),
     ("Emergent Properties","Properties of a system that arise from interactions of its parts and don't exist in individual components.")],
    [("An open system exchanges:",["Only energy","Only matter","*Both matter and energy with its surroundings","Neither"],"Most ecosystems are open."),
     ("Earth is approximately a closed system for:",["Energy","*Matter (very little matter enters or leaves; energy from Sun enters, heat radiates out)","Both","Neither"],"Sunlight in, heat out; matter stays."),
     ("A positive feedback loop:",["Stabilizes a system","*Amplifies a change — the output reinforces the initial change (e.g., more warming → more ice melt → more warming)","Has no effect","Is always beneficial"],"Runaway effect."),
     ("A negative feedback loop:",["Amplifies change","*Counteracts a change — the output opposes the initial change, stabilizing the system","Destroys the system","Is always harmful"],"Self-regulating."),
     ("The ice-albedo feedback is a _____ feedback loop.",["Negative","*Positive (ice melts → darker surface → absorbs more heat → more ice melts)","Neutral","Unrelated"],"Amplifying effect."),
     ("Predator-prey dynamics are an example of _____ feedback.",["Positive","*Negative (more prey → more predators → fewer prey → fewer predators → more prey)","No feedback","Random"],"Stabilizing oscillation."),
     ("If CO₂ increases temperature, which causes more CO₂ release from oceans, this is:",["Negative feedback","*Positive feedback (warming → more CO₂ → more warming)","No feedback","A closed system"],"Amplifying."),
     ("Thermoregulation in the human body (sweating when hot) is:",["Positive feedback","*Negative feedback (body temperature rises → sweating cools body → temperature decreases)","No regulation","Random"],"Homeostasis."),
     ("Emergent properties means:",["Parts have all properties","*The whole system has properties that individual components lack (e.g., a forest is more than individual trees)","Properties disappear","Nothing special"],"Systems-level characteristics."),
     ("In the AP exam, systems thinking questions may involve:",["Only memorization","*Identifying feedback loops, predicting system behavior, and analyzing inputs/outputs","Only calculations","Only vocabulary"],"Applied reasoning."),
     ("A tipping point in an environmental system is:",["Gradual change","*A threshold beyond which a system shifts to a new state and may not easily return","Normal variation","Predictable"],"Irreversible change."),
     ("The Earth system includes interconnected _____ (spheres).",["2","*4 main spheres: atmosphere, hydrosphere, geosphere, and biosphere","1","10"],"Interacting subsystems."),
     ("Steady state in a system means:",["No energy flows","*Inputs balance outputs — the system appears stable even though matter/energy flow continuously","Nothing moves","It's dead"],"Dynamic equilibrium."),
     ("Lag time in environmental systems means:",["Immediate response","*There is a delay between a cause and its full effect (e.g., CO₂ emissions today → warming for decades)","No delay","Only in seconds"],"Delayed consequences."),
     ("Resilience is a system's ability to:",["Never change","*Absorb disturbance and return to its original state","Always collapse","Resist all change"],"Bounce back."),
     ("Resistance is a system's ability to:",["Change easily","*Withstand disturbance without changing","Never recover","Always change"],"Resist change."),
     ("A systems diagram typically shows:",["Only text","*Boxes (components), arrows (flows), and feedback loops connecting parts of the system","Only numbers","Only photographs"],"Visual representation."),
     ("For AP quantitative problems, students may need to:",["Only describe","*Calculate changes in inputs/outputs, trace matter/energy through systems, and predict feedback effects","Only memorize","Only observe"],"Quantitative reasoning."),
     ("The concept of 'thresholds' is important because:",["Changes are always gradual","*Small changes can trigger abrupt, often irreversible shifts when a threshold is crossed","Thresholds don't exist","Only theory"],"Non-linear dynamics."),
     ("Systems thinking is the foundation of APES because:",["It's simple","*Every environmental topic involves interconnected systems, feedback loops, and complex cause-effect relationships","Only one topic uses it","It's optional"],"Unifying framework.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 1: wrote {len(lessons)} lessons")
