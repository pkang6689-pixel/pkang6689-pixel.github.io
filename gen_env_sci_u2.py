#!/usr/bin/env python3
"""Environmental Science Unit 2 – Ecology (8 lessons)."""
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

# 2.1
k,v = build_lesson(2,1,"Energy Flow in Ecosystems",
    "<h3>Energy Flow in Ecosystems</h3>"
    "<p>Energy flows in <b>one direction</b> through ecosystems: Sun → producers → consumers → heat. It is not recycled.</p>"
    "<h4>Key Measures</h4>"
    "<ul><li><b>GPP (Gross Primary Productivity):</b> Total energy fixed by photosynthesis.</li>"
    "<li><b>NPP (Net Primary Productivity):</b> GPP minus plant respiration; energy available to consumers.</li>"
    "<li><b>1st Law of Thermodynamics:</b> Energy is conserved — transferred, not created or destroyed.</li>"
    "<li><b>2nd Law:</b> Energy conversions increase entropy; energy is lost as heat at each transfer.</li></ul>",
    [("GPP","Gross Primary Productivity; total amount of energy fixed by photosynthesis in an ecosystem."),
     ("NPP","Net Primary Productivity; GPP minus plant respiration (R); energy available to consumers. NPP = GPP - R."),
     ("First Law of Thermodynamics","Energy is conserved; it can be transformed but never created or destroyed."),
     ("Second Law of Thermodynamics","Every energy conversion increases entropy; energy is lost as heat (explains the 10% rule)."),
     ("Energy Flow","One-way movement of energy through trophic levels; unlike matter, energy is not recycled in ecosystems.")],
    [("Energy flows through ecosystems in:",["Cycles","*One direction (Sun → producers → consumers → heat; it is not recycled)","Reverse","Random patterns"],"One-way flow."),
     ("GPP equals:",["NPP only","*Total energy fixed by all photosynthesis in an ecosystem","Only animal energy","Only decomposer energy"],"Gross production."),
     ("NPP is calculated as:",["GPP + R","*GPP − R (gross primary productivity minus plant respiration)","Only R","GPP × R"],"Net energy available."),
     ("The 2nd law of thermodynamics explains why:",["Energy is created","*Energy is lost as heat at each trophic transfer (the 10% rule)","Matter cycles","Photosynthesis occurs"],"Entropy increases."),
     ("The 10% rule states that approximately _____ of energy transfers to the next trophic level.",["50%","90%","*10%","1%"],"Rest lost as heat."),
     ("If producers fix 20,000 kcal/m²/yr and respire 12,000, NPP is:",["32,000","*8,000 kcal/m²/yr","12,000","20,000"],"NPP = GPP − R."),
     ("Which biome has the highest NPP?",["Desert","Tundra","*Tropical rainforest","Taiga"],"High sunlight + water."),
     ("Which aquatic ecosystem has very high productivity?",["Open ocean (per unit area)","Deep sea","*Estuaries and coral reefs","Arctic waters"],"Nutrient-rich."),
     ("Open ocean has low NPP per unit area but high total NPP because:",["It's warm","*It covers the largest area on Earth","It's deep","It has no life"],"Area × low productivity = high total."),
     ("Energy available at the tertiary consumer level from 10,000 kcal at the producer level is approximately:",["1,000 kcal","100 kcal","*10 kcal","1 kcal"],"10,000 → 1,000 → 100 → 10."),
     ("Assimilation efficiency is the fraction of ingested energy that:",["Is excreted","*Is absorbed into the body (not lost as feces)","Is lost as heat","Is stored"],"Absorbed/ingested."),
     ("Production efficiency is the fraction of assimilated energy that:",["Is respired","*Is converted to new biomass (growth + reproduction)","Is excreted","Is lost"],"Biomass production."),
     ("Why are there rarely more than 5 trophic levels?",["Legal limits","*Insufficient energy remains to support higher levels after successive 90% losses","Space limitations","No species exist to fill them"],"Energy limitation."),
     ("An energy pyramid is always upright because:",["It's a rule","*Energy decreases at each higher trophic level (never increases due to thermodynamics)","Sometimes it's inverted","It's arbitrary"],"2nd law."),
     ("A biomass pyramid can sometimes be inverted in:",["Forests","*Aquatic systems where fast-reproducing phytoplankton are consumed quickly but have low standing biomass","Deserts","All biomes"],"Turnover rate matters."),
     ("Chemosynthetic bacteria contribute to energy flow in:",["Forests","Deserts","*Deep-sea hydrothermal vents and other dark environments","Grasslands"],"Chemical energy source."),
     ("Global NPP is roughly evenly split between:",["Forests and deserts","*Terrestrial and aquatic ecosystems","Animals and plants","Tundra and tropics"],"~50/50 land/ocean."),
     ("Climate change affects NPP by:",["Always increasing it","*Changing temperature, precipitation, CO₂ levels, and growing seasons — effects vary by region","Always decreasing it","Having no effect"],"Complex impacts."),
     ("Measuring NPP helps scientists:",["Nothing","*Assess ecosystem health, estimate food production capacity, and track global carbon cycling","Only count trees","Only count animals"],"Practical applications."),
     ("Understanding energy flow is essential for AP because it connects:",["Nothing","*Trophic levels, nutrient cycling, biodiversity, and human impacts on ecosystems","Only to biology","Only to chemistry"],"Foundation of ecology.")]
)
lessons[k]=v

# 2.2
k,v = build_lesson(2,2,"Food Chains & Food Webs",
    "<h3>Food Chains &amp; Food Webs</h3>"
    "<p><b>Food chain:</b> Linear sequence of who eats whom (grass → rabbit → fox → eagle). <b>Food web:</b> Complex, interconnected food chains showing multiple feeding relationships in an ecosystem.</p>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>Grazing food chain:</b> Starts with producers (most terrestrial/aquatic systems).</li>"
    "<li><b>Detrital food chain:</b> Starts with dead organic matter (decomposition-based).</li>"
    "<li><b>Keystone species:</b> Removal causes disproportionate ecosystem change.</li>"
    "<li><b>Trophic cascades:</b> Changes at one level ripple through the web.</li></ul>",
    [("Food Chain","Linear pathway showing energy/nutrient transfer from one organism to the next."),
     ("Food Web","Complex network of interconnected food chains in an ecosystem."),
     ("Keystone Species","Species whose removal causes disproportionately large changes in its ecosystem (e.g., sea otters, wolves)."),
     ("Trophic Cascade","Ecological process where changes at one trophic level cause reciprocal changes through the food web."),
     ("Detrital Food Chain","Energy pathway starting with dead organic matter processed by decomposers and detritivores.")],
    [("A food web differs from a food chain because it:",["Is simpler","*Shows the complex, interconnected feeding relationships (multiple chains linked together)","Has fewer organisms","Is linear"],"More realistic model."),
     ("A grazing food chain starts with:",["Dead matter","*Living producers (plants or algae)","Consumers","Bacteria"],"Photosynthesis-based."),
     ("A detrital food chain starts with:",["Living plants","*Dead organic matter (detritus)","Top predators","Sunlight directly"],"Decomposition-based."),
     ("A keystone species is one whose:",["Population is largest","*Removal causes disproportionate ecosystem change relative to its biomass or abundance","Color is distinctive","Size is largest"],"Disproportionate impact."),
     ("Sea otters are a keystone species because:",["They're cute","*They control sea urchin populations; without otters, urchins overgraze kelp forests, destroying the habitat","They're large","They're rare"],"Trophic cascade."),
     ("The reintroduction of wolves to Yellowstone caused:",["No change","*A trophic cascade: wolves reduced elk overgrazing → vegetation recovered → stream banks stabilized → biodiversity increased","Only elk decline","Only wolf increase"],"Classic trophic cascade."),
     ("In a food web, removing a species can cause:",["No effect","*Ripple effects through multiple trophic levels (trophic cascade)","Only one species to change","The web to repair instantly"],"Interconnected impacts."),
     ("Omnivores complicate food webs because they:",["Eat only plants","*Feed at multiple trophic levels, connecting different food chains","Eat nothing","Are rare"],"Multi-level feeding."),
     ("The detrital food chain processes approximately _____ of energy in most terrestrial ecosystems.",["10%","*Much more than the grazing chain (~80-90% of plant matter enters detrital pathways)","0%","Equal to grazing"],"Most matter decomposes."),
     ("Indicator species are organisms that:",["Indicate direction","*Reflect the health of an ecosystem (e.g., amphibians indicate water quality)","Are always rare","Always increase"],"Environmental health barometer."),
     ("Foundation species create habitat that:",["Destroys biodiversity","*Supports many other species (e.g., coral, kelp forests, mangroves)","Only supports one species","Has no effect"],"Habitat creators."),
     ("Invasive species often disrupt food webs by:",["Adding balance","*Outcompeting native species, having no natural predators, or altering habitat","Decreasing their own population","Helping natives"],"Ecological disruption."),
     ("An example of a invasive species disrupting a food web is:",["Native salmon","*Zebra mussels in the Great Lakes (filter water, outcompete natives, alter food web base)","Oak trees","Eagles"],"Altered ecosystem."),
     ("Bottom-up control of food webs means:",["Predators control everything","*Nutrient/producer availability controls populations up the food chain","Neither","Decomposers control"],"Resource-driven."),
     ("Top-down control means:",["Producers control everything","*Predators control populations of lower trophic levels (predator-prey regulation)","Neither","Decomposers control"],"Predator-driven."),
     ("Bioaccumulation refers to:",["Decreasing toxin levels","*Buildup of a persistent substance (e.g., mercury) within an organism over time","Toxin elimination","Nutrient cycling"],"Increasing body burden."),
     ("Biomagnification causes toxin concentrations to _____ at higher trophic levels.",["Decrease","*Increase (each predator accumulates toxins from many prey)","Stay the same","Disappear"],"DDT in eagles."),
     ("DDT biomagnification caused _____ in birds of prey.",["Stronger eggs","*Eggshell thinning (leading to reproductive failure in eagles, pelicans, etc.)","Larger populations","No effect"],"Rachel Carson's concern."),
     ("Understanding food webs helps manage:",["Nothing","*Fisheries, conservation, pest control, and pollution (tracing toxins through trophic levels)","Only farming","Only gardening"],"Applied ecology."),
     ("For the AP exam, students should be able to:",["Only name species","*Trace energy flow, predict trophic cascade effects, and analyze food web disruptions","Only draw webs","Only memorize examples"],"Applied reasoning.")]
)
lessons[k]=v

# 2.3
k,v = build_lesson(2,3,"Population Dynamics",
    "<h3>Population Dynamics</h3>"
    "<h4>Growth Models</h4>"
    "<ul><li><b>Exponential growth:</b> J-curve; unlimited resources; dN/dt = rN (r = birth rate − death rate).</li>"
    "<li><b>Logistic growth:</b> S-curve; limited resources; dN/dt = rN(1 − N/K) where K = carrying capacity.</li></ul>"
    "<h4>Strategies</h4>"
    "<ul><li><b>r-selected:</b> Many offspring, little parental care, rapid growth (bacteria, insects).</li>"
    "<li><b>K-selected:</b> Few offspring, extensive parental care, slow growth (elephants, whales).</li></ul>"
    "<h4>Regulation</h4>"
    "<p>Density-dependent (competition, predation, disease) and density-independent (weather, fire, flood) factors.</p>",
    [("Exponential Growth","J-curve; population grows without limit: dN/dt = rN; occurs with unlimited resources."),
     ("Logistic Growth","S-curve; growth slows as population approaches carrying capacity: dN/dt = rN(1 − N/K)."),
     ("Carrying Capacity (K)","Maximum population size an environment can sustain indefinitely given available resources."),
     ("r-Selected Species","Species producing many offspring with little parental care; rapid growth; short lifespan (insects, bacteria)."),
     ("K-Selected Species","Species producing few offspring with extensive parental care; slow growth; long lifespan (elephants, whales).")],
    [("Exponential growth produces a:",["S-curve","*J-curve (population increases without limit when resources are abundant)","Flat line","Declining curve"],"Unlimited growth phase."),
     ("The logistic growth equation is:",["dN/dt = rN","*dN/dt = rN(1 − N/K)","dN/dt = K","N = rK"],"Includes carrying capacity."),
     ("Carrying capacity (K) is defined as:",["Maximum birth rate","*The maximum population size an environment can sustain given available resources","Minimum population","Growth rate"],"Environmental limit."),
     ("As a population approaches K, growth rate:",["Stays the same","Increases","*Decreases (approaches zero at K)","Becomes negative"],"S-curve leveling off."),
     ("r-selected species are characterized by:",["Few offspring, long life","*Many offspring, little parental care, rapid maturation","Slow growth","Large body size"],"E.g., insects, bacteria."),
     ("K-selected species are characterized by:",["Many offspring, short life","*Few offspring, parental care, slow maturation, long lifespan","Rapid reproduction","Small body size"],"E.g., elephants, whales."),
     ("Density-dependent limiting factors include:",["Earthquakes","Fire","*Competition, predation, disease, and parasitism (intensify as population grows)","Hurricanes"],"Population-size related."),
     ("Density-independent limiting factors include:",["Competition","Disease","*Natural disasters (fire, flood, drought, extreme weather)","Predation"],"Regardless of population size."),
     ("If r = 0.05 and N = 200, exponential growth rate (dN/dt) is:",["10","*10 individuals/time period (0.05 × 200 = 10)","200","0.05"],"dN/dt = rN."),
     ("If r = 0.1, N = 500, and K = 1000, logistic growth rate is:",["50","*25 (0.1 × 500 × (1-500/1000) = 0.1 × 500 × 0.5 = 25)","100","0"],"dN/dt = rN(1-N/K)."),
     ("Maximum logistic growth rate occurs at:",["N = 0","N = K","*N = K/2 (halfway to carrying capacity)","Any N"],"Inflection point."),
     ("Overshoot occurs when a population:",["Never reaches K","*Temporarily exceeds K, often followed by a die-off","Stays at K","Is below K"],"Common in nature."),
     ("A population crash after overshoot can reduce the population:",["To exactly K","*Well below K (and sometimes below a sustainable level)","To zero always","Never happens"],"Boom-bust cycle."),
     ("Survivorship curves come in three types. Type I shows:",["High early mortality","*Low mortality until old age (humans, elephants — K-selected)","Constant mortality","No mortality"],"Long-lived species."),
     ("Type III survivorship shows:",["Low early mortality","*Very high early mortality with few survivors living long (fish, many invertebrates — r-selected)","Constant mortality","Increasing mortality"],"Many young die."),
     ("Lag phase in population growth occurs because:",["Populations grow instantly","*Small initial populations take time to reproduce and accumulate numbers","Nothing changes","Resources are absent"],"Slow start."),
     ("Biotic potential is:",["Always achieved","*The maximum rate of increase (rmax) under ideal conditions — rarely achieved in nature","The actual growth rate","Zero"],"Maximum theoretical growth."),
     ("Environmental resistance includes all factors that:",["Promote growth","*Limit population growth and keep it below biotic potential (predation, disease, competition, limited resources)","Have no effect","Only help populations"],"Reality check on growth."),
     ("Understanding population dynamics is essential for:",["Nothing","*Wildlife management, pest control, conservation biology, fisheries, and human population planning","Only counting animals","Only agriculture"],"Applied ecology."),
     ("For AP, students should calculate growth rates using:",["Only estimation","*Both exponential (dN/dt = rN) and logistic (dN/dt = rN(1-N/K)) equations","Only graphing","Only observation"],"Quantitative skills.")]
)
lessons[k]=v

# 2.4
k,v = build_lesson(2,4,"Community Interactions (Competition, Symbiosis)",
    "<h3>Community Interactions</h3>"
    "<h4>Types</h4>"
    "<ul><li><b>Competition:</b> Interspecific (between species) and intraspecific (within species). Competitive exclusion principle — two species can't occupy the same niche indefinitely.</li>"
    "<li><b>Predation:</b> One organism kills and eats another; drives coevolution (camouflage, warning coloration).</li>"
    "<li><b>Symbiosis:</b> Mutualism (+/+), commensalism (+/0), parasitism (+/−).</li>"
    "<li><b>Niche partitioning:</b> Species reduce competition by using different parts of the same resource.</li></ul>",
    [("Competitive Exclusion Principle","Two species competing for the same limited resource cannot coexist indefinitely; one will be eliminated."),
     ("Niche Partitioning","Species reduce competition by using different parts of a resource (e.g., different tree heights for feeding)."),
     ("Mutualism","Symbiotic relationship benefiting both species (+/+); e.g., bees and flowers."),
     ("Parasitism","Symbiotic relationship where one benefits at the other's expense (+/−); e.g., ticks on deer."),
     ("Coevolution","Reciprocal evolutionary change between interacting species; e.g., predator-prey arms race.")],
    [("Interspecific competition occurs between:",["Individuals of the same species","*Individuals of different species competing for the same resources","Plants only","Animals only"],"Between species."),
     ("The competitive exclusion principle states that:",["Two species always coexist","*Two species cannot occupy the same niche indefinitely — one will outcompete the other","Competition doesn't exist","All species compete equally"],"Gause's principle."),
     ("Niche partitioning allows species to coexist by:",["Eating the same thing","*Using different parts of a resource (e.g., feeding at different heights, times, or locations)","Ignoring each other","Leaving the area"],"Resource division."),
     ("An ecological niche includes:",["Only habitat","*An organism's role, habitat, feeding behavior, interactions, and all conditions for survival","Only food","Only location"],"Total environmental requirements."),
     ("A fundamental niche is _____ than a realized niche.",["Smaller","*Larger (the full range of conditions a species could occupy vs. what it actually occupies due to competition)","The same","Unrelated"],"Potential vs. actual."),
     ("Mutualism means:",["One benefits, one is harmed","*Both species benefit from the interaction (+/+)","Neither benefits","One benefits, one is unaffected"],"Win-win."),
     ("Example of mutualism:",["Tick on a dog","*Mycorrhizal fungi and plant roots (fungi provide nutrients, plant provides sugars)","Lion eating zebra","Barnacle on whale"],"Both gain."),
     ("Commensalism means:",["Both benefit","*One species benefits while the other is unaffected (+/0)","One is harmed","Both are harmed"],"One benefits."),
     ("Example of commensalism:",["Bee + flower","*Barnacles on a whale (barnacles benefit from transport/feeding; whale unaffected)","Tapeworm in intestine","Lion and zebra"],"Unaffected host."),
     ("Parasitism means:",["Both benefit","*One species benefits at the expense of the other (+/−)","One is unaffected","Both are harmed"],"One gains, one loses."),
     ("Coevolution between predators and prey results in:",["No change","*An evolutionary arms race (faster prey → faster predators → faster prey)","Only predator evolution","Only prey evolution"],"Reciprocal adaptation."),
     ("Mimicry is an example of:",["Symbiosis","*Predator-prey coevolution (Batesian: harmless mimics harmful; Müllerian: harmful species resemble each other)","Competition","Commensalism"],"Deception or shared warning."),
     ("Batesian mimicry is when a _____ species mimics a harmful one.",["Dangerous","*Harmless (it gains protection by looking like something predators avoid)","Invisible","Large"],"Fake warning."),
     ("Müllerian mimicry is when two _____ species resemble each other.",["Harmless","*Harmful (predators learn to avoid the shared warning pattern more quickly)","Unrelated","Different kingdoms"],"Reinforced warning."),
     ("Amensalism (0/−) occurs when:",["Both benefit","*One species is harmed while the other is unaffected (e.g., large tree shading out small plants)","Both are harmed","One benefits"],"No benefit to either."),
     ("Herbivory is a form of:",["Mutualism","*Predation (plant is harmed when consumed by an herbivore, though usually not killed)","Commensalism","Parasitism only"],"Plant-consumer interaction."),
     ("r-selected species typically experience _____ density-dependent regulation.",["Strong","*Weak (their populations often crash from density-independent factors before reaching K)","Equal","No"],"Boom-bust."),
     ("K-selected species are more affected by _____ factors.",["Density-independent","*Density-dependent (competition, disease become critical near carrying capacity)","No","Random"],"Near K regulation."),
     ("Understanding community interactions helps manage:",["Nothing","*Invasive species, conservation of endangered species, biological pest control, and ecosystem restoration","Only farming","Only zoos"],"Applied ecology."),
     ("For the AP exam, students should identify interaction types and predict outcomes of:",["Nothing","*Species additions, removals, and environmental changes on community structure","Only naming species","Only drawing diagrams"],"Prediction skills.")]
)
lessons[k]=v

# 2.5
k,v = build_lesson(2,5,"Succession (Primary & Secondary)",
    "<h3>Ecological Succession</h3>"
    "<h4>Primary Succession</h4>"
    "<p>Occurs on bare substrate with no soil (lava flows, retreating glaciers). Pioneer species (lichens, mosses) colonize first → soil develops → grasses → shrubs → trees → climax community. Takes centuries to millennia.</p>"
    "<h4>Secondary Succession</h4>"
    "<p>Occurs after disturbance that leaves soil intact (fire, logging, abandonment). Faster than primary — soil, seeds, and organisms remain. Grasses/weeds → shrubs → trees → climax community.</p>",
    [("Primary Succession","Ecological succession starting on bare substrate with no soil; very slow (centuries)."),
     ("Secondary Succession","Succession after disturbance that leaves soil intact; faster than primary (decades)."),
     ("Pioneer Species","First organisms to colonize bare substrate (lichens, mosses in primary; weeds/grasses in secondary)."),
     ("Climax Community","The relatively stable ecosystem that develops at the end of ecological succession."),
     ("Disturbance","An event that disrupts an ecosystem (fire, flood, storm, volcanic eruption, human activity).")],
    [("Primary succession begins on:",["Soil","*Bare rock or substrate with no soil (e.g., after volcanic eruption or glacier retreat)","Existing forest","Grassland"],"No soil present."),
     ("Pioneer species in primary succession are typically:",["Trees","*Lichens and mosses that can colonize bare rock and begin soil formation","Large animals","Grasses"],"First colonizers."),
     ("Secondary succession occurs after:",["All soil is removed","*A disturbance that leaves soil intact (fire, farming abandonment, logging)","Nothing changes","A volcano"],"Soil remains."),
     ("Secondary succession is _____ than primary succession.",["Slower","*Faster (soil, seeds, and root systems already present)","The same speed","Impossible"],"Head start."),
     ("A climax community is:",["The first stage","*A relatively stable, mature community that persists until the next major disturbance","Temporary","Always a forest"],"End stage."),
     ("Intermediate disturbance hypothesis states that:",["No disturbance is best","Maximum disturbance is best","*Moderate disturbance levels maintain highest biodiversity","Disturbance is irrelevant"],"Balance between extremes."),
     ("Facilitation in succession means:",["Species block others","*Early species modify the environment to make it more suitable for later species","Nothing changes","Species compete only"],"Preparing the way."),
     ("Inhibition in succession means:",["Early species help later ones","*Early species resist replacement by making conditions less favorable for newcomers","Nothing occurs","Succession stops"],"Competitive resistance."),
     ("Tolerance in succession means:",["Only early species survive","*Later species can grow regardless of early species' presence (they tolerate existing conditions)","Nothing grows","All species die"],"Indifferent to predecessors."),
     ("An example of primary succession is:",["After a forest fire","*Colonization of a newly formed volcanic island (e.g., Surtsey, Iceland)","After flooding","After farming"],"No prior soil."),
     ("An example of secondary succession is:",["After glaciation","*Regrowth of a forest after a wildfire","On a lava flow","On a new island"],"Soil remains."),
     ("Old-field succession (abandoned farmland) is a type of:",["Primary","*Secondary succession (soil exists; weeds → grasses → shrubs → trees over decades)","Neither","Both"],"Classic example."),
     ("Biodiversity typically _____ during succession until the climax stage.",["Decreases","*Increases (more species diversity as the community develops)","Stays the same","Fluctuates randomly"],"Community development."),
     ("In modern ecology, the concept of 'climax community' is considered:",["Absolute","*More of a general trend than a fixed endpoint — communities are dynamic and change continuously","Obsolete completely","Always precise"],"More nuanced view."),
     ("Fire-adapted ecosystems (chaparral, prairies) may depend on periodic fires because:",["Fire is always destructive","*Fire prevents woody plant encroachment, recycles nutrients, and stimulates seed germination","Fires are rare there","No species adapted"],"Fire ecology."),
     ("Invasive species can disrupt succession by:",["Aiding native species","*Outcompeting native colonizers and preventing normal community development","Having no effect","Leaving quickly"],"Altered trajectory."),
     ("Soil formation during primary succession involves:",["Nothing","*Physical weathering of rock, decomposition of pioneer organisms, and accumulation of organic matter","Only rain","Only wind"],"Slow process."),
     ("Nurse logs in forest succession help because:",["They block growth","*Decomposing logs provide nutrients, moisture, and elevated growing surfaces for seedlings","They're decorative","They attract predators"],"Facilitating growth."),
     ("Aquatic succession (e.g., lake filling in) can turn a lake into:",["An ocean","*A meadow or forest over long periods as sediment accumulates","A desert","A deeper lake"],"Terrestrialization."),
     ("Understanding succession is important for AP because it connects to:",["Nothing","*Biodiversity, disturbance ecology, conservation, restoration ecology, and ecosystem management","Only history","Only one unit"],"Broad applied concept.")]
)
lessons[k]=v

# 2.6
k,v = build_lesson(2,6,"Biodiversity & Conservation",
    "<h3>Biodiversity &amp; Conservation</h3>"
    "<h4>Levels of Biodiversity</h4>"
    "<ul><li><b>Genetic:</b> Variation within a species (allele diversity).</li>"
    "<li><b>Species:</b> Number of different species in an area.</li>"
    "<li><b>Ecosystem:</b> Variety of habitats, communities, and ecological processes.</li></ul>"
    "<h4>Threats</h4>"
    "<p>HIPPCO: Habitat destruction, Invasive species, Population growth, Pollution, Climate change, Overexploitation. Currently in the <b>6th mass extinction</b> (species loss rate 100–1,000× background).</p>",
    [("Biodiversity","Variety of life at genetic, species, and ecosystem levels."),
     ("HIPPCO","Threats to biodiversity: Habitat destruction, Invasive species, Population growth, Pollution, Climate change, Overexploitation."),
     ("Endangered Species","Species in danger of extinction throughout all or a significant portion of its range."),
     ("Habitat Fragmentation","Breaking continuous habitat into smaller, isolated patches; reduces biodiversity and gene flow."),
     ("Sixth Mass Extinction","Current ongoing extinction event driven by human activities; loss rate 100–1,000× the natural background rate.")],
    [("The three levels of biodiversity are:",["Only species","*Genetic, species, and ecosystem diversity","Only ecosystem","Only genetic"],"All three matter."),
     ("HIPPCO stands for:",["A hippo-related disease","*Habitat destruction, Invasive species, Population growth, Pollution, Climate change, Overexploitation","A conservation organization","A type of ecosystem"],"Threats to biodiversity."),
     ("The leading cause of biodiversity loss is:",["Pollution","*Habitat destruction (deforestation, urbanization, agriculture converting natural areas)","Climate change alone","Invasive species alone"],"Number one threat."),
     ("Habitat fragmentation harms species by:",["Creating more habitat","*Isolating populations, reducing genetic diversity, increasing edge effects, and limiting migration","Having no effect","Only affecting plants"],"Smaller, disconnected patches."),
     ("Edge effects in fragmented habitats include:",["No changes","*Increased exposure to wind, temperature changes, predators, and invasive species at habitat boundaries","Only positive effects","Only inside changes"],"Boundary impacts."),
     ("Invasive species threaten biodiversity because:",["They help natives","*They outcompete natives, have no natural predators, and can alter habitat (e.g., kudzu, cane toads)","They're always small","They only affect islands"],"Ecological disruption."),
     ("The current extinction rate is estimated at _____ times the natural background rate.",["2–5","10–50","*100–1,000","1"],"Sixth mass extinction."),
     ("Species richness refers to:",["Individual count only","*The total number of different species in an area","Only rare species","Only common species"],"Simplest diversity measure."),
     ("Species evenness refers to:",["Total species count","*How evenly individuals are distributed among species (high evenness = no single species dominates)","Only abundance","Only rarity"],"Distribution measure."),
     ("An endangered species is one that:",["Is already extinct","*Is in danger of extinction throughout all or a significant portion of its range","Has a large population","Is common"],"Legal designation."),
     ("The Endangered Species Act (1973, USA) protects:",["Only mammals","*Listed plant and animal species and their critical habitats","Only birds","Only in national parks"],"Legal protection."),
     ("Biodiversity hotspots are regions with:",["Low biodiversity","*High species richness AND high threat of habitat loss (>1,500 endemic plant species; >70% habitat lost)","Only one species","No threats"],"Conservation priority areas."),
     ("Genetic diversity is important because it:",["Doesn't matter","*Provides variation for adaptation and resilience; low genetic diversity increases extinction risk","Only affects appearance","Only affects size"],"Evolutionary potential."),
     ("In-situ conservation means:",["Zoos and seed banks","*Protecting species in their natural habitat (national parks, reserves, protected areas)","Moving species","Captive breeding only"],"On-site protection."),
     ("Ex-situ conservation means:",["Natural habitat protection","*Protecting species outside their natural habitat (zoos, botanical gardens, seed banks, gene banks)","Only research","Only education"],"Off-site protection."),
     ("Ecosystem services lost when biodiversity declines include:",["Nothing","*Pollination, water purification, carbon sequestration, pest control, and nutrient cycling","Only recreation","Only timber"],"Functional losses."),
     ("The economic value of ecosystem services is estimated at:",["Zero","A few million","*Trillions of dollars annually ($125+ trillion/year globally by some estimates)","Incalculable"],"Enormous economic value."),
     ("Wildlife corridors help biodiversity by:",["Blocking movement","*Connecting fragmented habitats, allowing gene flow, migration, and access to resources","Only for humans","Only for birds"],"Landscape connectivity."),
     ("The precautionary principle applied to biodiversity means:",["Wait until species go extinct","*Take protective action even before full science is complete if biodiversity is at risk","Never protect anything","Only protect popular species"],"Better safe than sorry."),
     ("Understanding biodiversity is essential for AP because:",["It's not tested","*It's a core theme connecting ecology, conservation, policy, and human well-being","Only one question","Only for extra credit"],"Fundamental topic.")]
)
lessons[k]=v

# 2.7
k,v = build_lesson(2,7,"Case Studies in Ecology",
    "<h3>Case Studies in Ecology</h3>"
    "<h4>Yellowstone Wolf Reintroduction (1995)</h4>"
    "<p>Wolves reintroduced → elk behavior changed → riparian vegetation recovered → streambank stability → beaver return → trophic cascade demonstrating top-down regulation.</p>"
    "<h4>Coral Reef Decline</h4>"
    "<p>Warming → coral bleaching (loss of zooxanthellae) → biodiversity collapse. 14% of world's coral lost 2009–2018.</p>"
    "<h4>Amazon Deforestation</h4>"
    "<p>~17% of Amazon cleared for cattle and soy; approaching tipping point where forest could convert to savanna, releasing massive CO₂.</p>",
    [("Yellowstone Trophic Cascade","Wolf reintroduction reduced elk overgrazing, allowing vegetation recovery and stream restoration."),
     ("Coral Bleaching","Corals expel symbiotic algae (zooxanthellae) under heat stress, turning white; can lead to death if prolonged."),
     ("Amazon Tipping Point","Theory that ~20-25% deforestation could trigger irreversible conversion of Amazon forest to savanna."),
     ("Zooxanthellae","Symbiotic algae living in coral tissue; provide up to 90% of the coral's energy through photosynthesis."),
     ("Biodiversity Hotspot","Region with exceptionally high species richness and endemism that is significantly threatened by human activities.")],
    [("The Yellowstone wolf reintroduction demonstrated:",["No ecological change","*A trophic cascade: wolves → changed elk behavior → vegetation recovery → stream restoration","Only wolf population increase","Only elk decline"],"Classic trophic cascade."),
     ("Coral bleaching occurs when:",["Coral grows","*Elevated water temperatures cause corals to expel their symbiotic zooxanthellae algae","Coral reproduces","Water cools"],"Thermal stress response."),
     ("Zooxanthellae provide corals with up to _____ of their energy.",["10%","50%","*~90% (through photosynthesis)","25%"],"Critical symbiosis."),
     ("If bleaching is prolonged, corals can:",["Recover immediately","*Die (without zooxanthellae, they starve)","Turn stronger","Change color permanently"],"Fatal if sustained."),
     ("Amazon deforestation is primarily driven by:",["Natural causes","*Cattle ranching and soybean agriculture","Urbanization only","Mining only"],"Agriculture is the main driver."),
     ("The Amazon tipping point concept suggests that at ~20-25% deforestation:",["Nothing changes","*The forest may irreversibly convert to savanna (reduced rainfall, increased fire susceptibility)","More forest grows","Biodiversity increases"],"Potentially catastrophic."),
     ("The Amazon rainforest produces approximately _____ of its own rainfall through transpiration.",["10%","*~50% (the forest recycles moisture)","90%","0%"],"Self-watering system."),
     ("The Great Barrier Reef has experienced mass bleaching events in:",["Only once","*Multiple times, including severe events in 2016, 2017, 2020, 2022, 2024","Never","Only in the 1990s"],"Increasing frequency."),
     ("Invasive lionfish in the Atlantic/Caribbean demonstrate:",["No impact","*How a species with no natural predators can devastate native reef fish populations","Only aesthetic changes","Improved biodiversity"],"Invasive species case."),
     ("The Chesapeake Bay has suffered from:",["Pristine condition","*Eutrophication due to agricultural runoff (nitrogen, phosphorus) causing dead zones","Only fishing","Only tourism"],"Nutrient pollution."),
     ("Dead zones in the Gulf of Mexico are caused by:",["Natural processes","*Agricultural fertilizer runoff from the Mississippi River causing algal blooms → oxygen depletion","Ocean currents","Volcanic activity"],"Hypoxia."),
     ("The passenger pigeon extinction teaches us that:",["Large populations are safe","*Even abundant species can be driven to extinction by overexploitation and habitat loss","Extinction is impossible","Only rare species go extinct"],"Went from billions to zero."),
     ("Northern white rhino conservation demonstrates:",["Success","*The difficulty of saving species once populations drop to critically low levels (only 2 females remain as of 2024)","Population growth","Easy recovery"],"Too little, too late."),
     ("The recovery of bald eagles in the US was aided by:",["DDT continued use","*Banning DDT (1972), Endangered Species Act protection, and habitat conservation","No action","Only captive breeding"],"Multi-factor recovery."),
     ("These ecology case studies share the lesson that:",["Ecosystems are simple","*Ecosystems are interconnected — human actions have cascading and often unexpected consequences","Only one species matters","Nothing changes"],"Complexity and consequence."),
     ("Conservation success stories show that:",["Nothing works","*Species and ecosystems can recover when human threats are reduced and habitats are protected","Only money helps","Only laws help"],"Recovery is possible."),
     ("Mangrove destruction increases coastal vulnerability because:",["Mangroves are ugly","*Mangroves protect coasts from storms, nursery habitat for fish, and sequester carbon","Mangroves cause flooding","No connection"],"Ecosystem service loss."),
     ("Prairie restoration in the US Midwest aims to:",["Build cities","*Restore native grassland ecosystems that support pollinators, store carbon, and prevent erosion","Remove all trees","Only grow crops"],"Ecosystem recovery."),
     ("These case studies demonstrate the importance of:",["Ignoring ecology","*Applying ecological principles to real-world conservation and management challenges","Only laboratory research","Only theory"],"Applied ecology."),
     ("For the AP exam, students should be able to analyze case studies by:",["Only memorizing facts","*Identifying ecological principles at work, tracing cause-and-effect, and evaluating management approaches","Only naming species","Only drawing diagrams"],"Analytical skills.")]
)
lessons[k]=v

# 2.8
k,v = build_lesson(2,8,"AP Prep: Population Models",
    "<h3>AP Prep: Population Models</h3>"
    "<h4>Calculations</h4>"
    "<ul><li><b>Growth rate (r):</b> r = (births − deaths) / N or r = birth rate − death rate.</li>"
    "<li><b>Doubling time:</b> t = 70/r (Rule of 70); r in percent.</li>"
    "<li><b>Exponential:</b> dN/dt = rN.</li>"
    "<li><b>Logistic:</b> dN/dt = rN(1 − N/K). Maximum growth at N = K/2.</li>"
    "<li><b>Population change:</b> ΔN = (births + immigration) − (deaths + emigration).</li></ul>",
    [("Rule of 70","Doubling time = 70 ÷ growth rate (in percent); quick estimation of how fast a population doubles."),
     ("Intrinsic Rate of Increase (r)","Per capita rate of population change; r = birth rate − death rate (for closed populations)."),
     ("Logistic Maximum Growth","Maximum population growth rate occurs at N = K/2 (inflection point of the S-curve)."),
     ("Population Change Equation","ΔN = (births + immigration) − (deaths + emigration); comprehensive population accounting."),
     ("Doubling Time","Time for a population to double in size; shorter doubling time = faster growth.")],
    [("If a population has r = 2% per year, doubling time is:",["35 years","*35 years (70/2 = 35)","70 years","100 years"],"Rule of 70."),
     ("If births = 500, deaths = 300, immigration = 50, emigration = 50, the population change is:",["100","*200 (500 + 50 − 300 − 50 = 200)","500","0"],"ΔN = (B+I) − (D+E)."),
     ("For a population of N = 1,000 with r = 0.03, exponential growth (dN/dt) is:",["3","*30 (0.03 × 1000 = 30 individuals/time period)","1,000","0.03"],"dN/dt = rN."),
     ("For logistic growth with r = 0.04, N = 400, K = 800, dN/dt is:",["16","*8 (0.04 × 400 × (1-400/800) = 0.04 × 400 × 0.5 = 8)","32","0"],"dN/dt = rN(1-N/K)."),
     ("At what population size is logistic growth rate maximized?",["N = 0","N = K","*N = K/2","Any N"],"Inflection point."),
     ("If K = 1,000 and N = 1,000, the logistic growth rate is:",["Maximum","*0 (1 − 1000/1000 = 0; population is at carrying capacity)","r","K"],"At K, growth stops."),
     ("The term (1 − N/K) in the logistic equation represents:",["Growth rate","*The fraction of carrying capacity still available (environmental resistance)","Population size","Carrying capacity"],"Unused capacity."),
     ("If a country has r = 3.5%, its doubling time is:",["35 years","*20 years (70/3.5 = 20)","7 years","70 years"],"Rule of 70."),
     ("Per capita growth rate (r) can be calculated as:",["N/t","*r = (births − deaths)/N or birth rate minus death rate","K/N","dN/dt only"],"Rate per individual."),
     ("A population in decline has r that is:",["Positive","Zero","*Negative (deaths exceed births)","Undefined"],"Shrinking population."),
     ("Crude birth rate is expressed as:",["Births per year","*Births per 1,000 individuals per year","Births per family","Births total"],"Standard demographic measure."),
     ("If crude birth rate = 25/1000 and crude death rate = 10/1000, r =:",["35/1000","*15/1000 = 1.5% (25-10 = 15 per 1000)","25/1000","10/1000"],"r = CBR − CDR."),
     ("Total fertility rate (TFR) of 2.1 is called:",["High fertility","*Replacement level fertility (population stabilizes over time)","Zero growth immediately","Declining"],"Replacement rate."),
     ("Age structure diagrams with wide bases indicate:",["Declining populations","*Rapidly growing populations (many young people who will enter reproductive age)","Stable populations","Old populations"],"Pyramid shape."),
     ("In an AP free-response question about population growth, you should:",["Only describe","*Show calculations, identify the model (exponential vs logistic), state assumptions, and interpret results","Only draw graphs","Only give the answer"],"Full solution."),
     ("If a population grows from 500 to 650 in one year with no migration, births were:",["150","*150 more than deaths (ΔN = B − D = 650 − 500 = 150)","500","650"],"Net births."),
     ("When N exceeds K temporarily (overshoot), the population will likely:",["Stay stable","*Decline due to resource depletion (die-off)","Continue growing","Always go to zero"],"Overshoot and crash."),
     ("Density-dependent mortality becomes _____ important as N approaches K.",["Less","*More (competition, disease, and stress intensify at high density)","Equally","Not"],"Near-K regulation."),
     ("The intrinsic rate of increase (rmax) represents:",["Actual growth","*Maximum possible growth rate under ideal conditions (no limiting factors)","Negative growth","Zero growth"],"Biotic potential."),
     ("Mastering population models for AP requires:",["Only memorization","*Fluency with equations (exponential, logistic), rule of 70, and interpreting growth curves and age structure diagrams","Only graphs","Only vocabulary"],"Quantitative + conceptual.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 2: wrote {len(lessons)} lessons")
