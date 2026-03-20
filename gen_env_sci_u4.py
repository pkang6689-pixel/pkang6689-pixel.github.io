#!/usr/bin/env python3
"""Environmental Science Unit 4 – Natural Resources (7 lessons)."""
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

# 4.1
k,v = build_lesson(4,1,"Renewable vs. Nonrenewable Resources",
    "<h3>Renewable vs. Nonrenewable Resources</h3>"
    "<p><b>Renewable:</b> Replenished on a human timescale — solar, wind, water, biomass, geothermal. Sustainable if used at or below replacement rate.</p>"
    "<p><b>Nonrenewable:</b> Formed over millions of years — fossil fuels, minerals, metals. Finite; extraction degrades the environment.</p>"
    "<h4>Key Distinction</h4>"
    "<p>Even renewables can become depleted if overexploited (e.g., overfishing, deforestation faster than regrowth).</p>",
    [("Renewable Resource","Resource replenished naturally on a human timescale (solar, wind, water, biomass)."),
     ("Nonrenewable Resource","Resource formed over geological time; finite supply (fossil fuels, minerals, metals)."),
     ("Sustainable Yield","Maximum amount of a renewable resource that can be harvested without depleting stock."),
     ("Depletion","Using a resource faster than it can be replaced, leading to decline or exhaustion."),
     ("Perpetual Resource","Resource that is virtually inexhaustible on any human timescale (e.g., solar energy, tidal energy).")],
    [("Renewable resources are those that:",["Take millions of years to form","*Are replenished naturally on a human timescale (e.g., solar, wind, biomass)","Can never be depleted","Are always cheaper"],"Replenishable."),
     ("Nonrenewable resources include:",["Solar and wind","*Fossil fuels (coal, oil, natural gas) and minerals/metals","Only water","Only wood"],"Geological timescale."),
     ("A perpetual resource like solar energy differs from renewable because it:",["Can run out","*Is virtually inexhaustible (available as long as the sun shines, regardless of human use)","Requires mining","Is more expensive always"],"Never depleted."),
     ("A renewable resource can become depleted if:",["It's never used","*It's harvested faster than it regenerates (e.g., overfishing, deforestation)","Only nonrenewables deplete","It's protected"],"Overexploitation."),
     ("Sustainable yield is the:",["Maximum ever taken","*Largest harvest that can be taken indefinitely without reducing the resource base","Minimum harvest","Total resource amount"],"Balance point."),
     ("Which is nonrenewable?",["Wind","Solar","Biomass","*Coal (formed over millions of years from ancient plant matter)"],"Fossil fuel."),
     ("Which is considered renewable?",["Natural gas","Uranium","*Wind energy","Coal"],"Naturally replenished."),
     ("Fossil fuels formed from:",["Recent plants","*Ancient organic matter compressed and heated over millions of years","Volcanic activity","Ocean currents"],"Geological process."),
     ("Peak oil theory suggests:",["Oil will last forever","*Oil production will reach a maximum and then decline as reserves are depleted","Oil is renewable","We already ran out"],"Supply limit."),
     ("The tragedy of the commons describes:",["Private property success","*Overexploitation of shared resources when individuals act in self-interest (Garrett Hardin, 1968)","Government regulation success","Conservation always working"],"Shared resource dilemma."),
     ("Solutions to the tragedy of the commons include:",["More overuse","*Regulation, privatization, community management, and international agreements","Ignoring the problem","Only government ownership"],"Multiple approaches."),
     ("Minerals and metals are nonrenewable but can be extended through:",["Only new mining","*Recycling, reuse, substitution, and improved extraction efficiency","Planting","Waiting"],"Extending supply."),
     ("Rare earth elements are critical for:",["Nothing","*Electronics, renewable energy tech (wind turbines, EV batteries), and defense systems","Only jewelry","Only construction"],"Modern technology."),
     ("Phosphorus is a critical nonrenewable resource for:",["Energy production","*Agriculture (essential fertilizer nutrient); reserves are concentrated in few countries","Transportation","Construction"],"Food security concern."),
     ("The concept of 'resource curse' describes how:",["Resource wealth always helps","*Countries rich in natural resources often struggle with corruption, conflict, and poor economic outcomes","Resources prevent poverty","Mining solves all problems"],"Paradox of plenty."),
     ("Substitution can help with resource depletion by:",["Using more of the same","*Replacing a scarce resource with an abundant alternative (e.g., fiber optics replacing copper wire)","Never works","Only for energy"],"Technology adaptation."),
     ("Lifecycle analysis (LCA) evaluates:",["Only production","*Environmental impact of a product from extraction → manufacturing → use → disposal (cradle to grave)","Only disposal","Only use"],"Full impact assessment."),
     ("The circular economy model aims to:",["Use and discard","Maximize waste","*Eliminate waste by designing products for reuse, repair, and recycling (closed-loop system)","Increase extraction"],"Zero waste goal."),
     ("Understanding resource types is essential for AP because it connects to:",["Nothing","*Energy policy, pollution, land use, sustainability, economic development, and environmental degradation","Only one topic","Only economics"],"Foundation concept."),
     ("For the AP exam, students should be able to:",["Only classify resources","*Compare renewable vs. nonrenewable, evaluate sustainability, and propose management strategies","Only memorize definitions","Only list examples"],"Applied analysis.")]
)
lessons[k]=v

# 4.2
k,v = build_lesson(4,2,"Water Resources & Management",
    "<h3>Water Resources &amp; Management</h3>"
    "<p>Only ~2.5% of Earth's water is fresh; ~69% of that is in glaciers/ice caps. Available fresh water (<1%) comes from groundwater, rivers, and lakes.</p>"
    "<h4>Key Issues</h4>"
    "<ul><li><b>Aquifer depletion:</b> Ogallala Aquifer depleting faster than recharge (irrigation in Great Plains).</li>"
    "<li><b>Water pollution:</b> Point source (factory pipe) vs. Non-point source (agricultural runoff).</li>"
    "<li><b>Water stress:</b> ~4 billion people face severe water scarcity at least one month per year.</li></ul>",
    [("Aquifer","Underground layer of permeable rock or sediment that holds and transmits groundwater."),
     ("Ogallala Aquifer","Massive US aquifer underlying the Great Plains; being depleted by irrigation faster than it recharges."),
     ("Point Source Pollution","Pollution from a single identifiable source (e.g., factory pipe, sewage outfall)."),
     ("Non-Point Source Pollution","Pollution from diffuse sources (e.g., agricultural runoff, urban stormwater)."),
     ("Water Table","Upper surface of the zone of saturation in an aquifer; drops when pumping exceeds recharge.")],
    [("What percentage of Earth's water is fresh?",["25%","10%","*~2.5%","50%"],"Most is saltwater."),
     ("Of all fresh water, approximately _____ is locked in glaciers and ice caps.",["10%","30%","*~69%","90%"],"Mostly inaccessible."),
     ("Available fresh water for human use (rivers, lakes, accessible groundwater) is:",["25%","10%","*Less than 1% of total water","50%"],"Very limited."),
     ("An aquifer is:",["A surface lake","*An underground layer of rock/sediment that holds and transmits groundwater","A river","A glacier"],"Subsurface water storage."),
     ("The Ogallala Aquifer is being depleted because:",["It rains too much","*Irrigation withdrawals far exceed the very slow natural recharge rate","It's not being used","Earthquakes"],"Unsustainable use."),
     ("Point source pollution comes from:",["Everywhere","*A single, identifiable location (e.g., a factory discharge pipe or sewage outfall)","Only farms","Only nature"],"Identifiable source."),
     ("Non-point source pollution comes from:",["A single pipe","*Diffuse sources spread over a large area (e.g., agricultural runoff, urban stormwater, atmospheric deposition)","Only one factory","Only sewage"],"Widespread sources."),
     ("The leading cause of water pollution in the US is:",["Factories","*Agricultural runoff (fertilizers, pesticides, animal waste — the largest non-point source)","Power plants","Mining"],"Farm runoff."),
     ("Eutrophication occurs when excess _____ enters waterways.",["Oxygen","*Nutrients (nitrogen and phosphorus) causing algal blooms → oxygen depletion","Salt","Acid"],"Nutrient overload."),
     ("A dead zone is an area of water with:",["High oxygen","*Very low dissolved oxygen (hypoxia) — organisms can't survive","High biodiversity","Normal conditions"],"Oxygen-depleted."),
     ("Water table depletion can cause:",["Rising sea levels","*Land subsidence (sinking), saltwater intrusion in coastal areas, and dried-up wells","Earthquakes only","Flooding"],"Multiple impacts."),
     ("Desalination converts saltwater to freshwater using:",["Sunlight only","*Reverse osmosis or distillation (energy-intensive process)","Filtering with sand","Evaporation only"],"Technology solution."),
     ("Limitations of desalination include:",["None","*High energy cost, brine waste disposal, and expense — not economically feasible everywhere","It doesn't work","Only taste"],"Not a silver bullet."),
     ("Water conservation strategies include:",["Only new dams","*Drip irrigation, low-flow fixtures, water recycling, xeriscaping, and fixing leaks","Only desalination","Only rain collection"],"Multiple approaches."),
     ("Drip irrigation is more efficient than flood irrigation because it:",["Uses more water","*Delivers water directly to plant roots, reducing evaporation and runoff (up to 95% efficient vs. 60%)","Is cheaper always","Requires no technology"],"Targeted delivery."),
     ("Dams provide benefits including:",["No benefits","*Water storage, hydropower, flood control, and irrigation — but also displace communities and alter ecosystems","Only power","Only recreation"],"Benefits and costs."),
     ("The Clean Water Act (1972, US) regulates:",["Only drinking water","*Discharge of pollutants into surface waters and sets quality standards for surface waters","Only groundwater","Only ocean water"],"Key US water law."),
     ("The Safe Drinking Water Act regulates:",["Surface water discharge","*Public drinking water quality standards and groundwater protection","Only rivers","Only oceans"],"Drinking water protection."),
     ("Watershed management takes a _____ approach to water quality.",["Narrow","*Holistic (managing the entire drainage area that feeds a water body)","Local only","Single-source"],"Ecosystem-level approach."),
     ("For the AP exam, water resource questions often involve:",["Only definitions","*Identifying pollution sources (point vs. non-point), evaluating management strategies, and water budget calculations","Only diagrams","Only vocabulary"],"Applied analysis.")]
)
lessons[k]=v

# 4.3
k,v = build_lesson(4,3,"Soil & Agriculture",
    "<h3>Soil &amp; Agriculture</h3>"
    "<p>Soil forms from weathered rock + organic matter over centuries. Soil horizons: O (organic litter), A (topsoil), B (subsoil), C (weathered parent material), R (bedrock).</p>"
    "<h4>Agricultural Impacts</h4>"
    "<ul><li><b>Erosion:</b> Wind and water remove topsoil; ~24 billion tons lost annually.</li>"
    "<li><b>Salinization:</b> Salt buildup from irrigation in arid regions.</li>"
    "<li><b>Green Revolution:</b> High-yield crops + fertilizers + irrigation; fed billions but increased environmental costs.</li></ul>",
    [("Soil Horizons","Layers of soil: O (organic), A (topsoil), B (subsoil), C (weathered parent material), R (bedrock)."),
     ("Topsoil (A Horizon)","Uppermost mineral layer; richest in organic matter and nutrients; essential for agriculture."),
     ("Erosion","Removal of topsoil by wind and water; accelerated by deforestation, overgrazing, and poor farming practices."),
     ("Salinization","Buildup of salts in soil from evaporation of irrigation water; reduces soil fertility."),
     ("Green Revolution","1960s–70s agricultural transformation using high-yield varieties, fertilizers, pesticides, and irrigation.")],
    [("The correct order of soil horizons from top to bottom is:",["R, C, B, A, O","*O, A, B, C, R (organic, topsoil, subsoil, parent material, bedrock)","A, B, C, O, R","C, B, A, O, R"],"Standard profile."),
     ("Topsoil (A horizon) is critical because it:",["Has no importance","*Contains the most organic matter, nutrients, and organisms — essential for plant growth","Is the deepest layer","Is mostly rock"],"Agricultural foundation."),
     ("Approximately _____ billion tons of topsoil are lost to erosion annually.",["1","5","*~24 billion tons","100"],"Massive global loss."),
     ("Soil erosion is accelerated by:",["Planting trees","*Deforestation, overgrazing, poor farming practices, and leaving soil bare","Mulching","Cover cropping"],"Human causes."),
     ("Salinization occurs when:",["Soil gets too wet","*Irrigation water evaporates in arid regions, leaving dissolved salts behind in the soil","Rain falls","Snow melts"],"Arid region problem."),
     ("The Green Revolution increased food production through:",["No technology","*High-yield crop varieties, synthetic fertilizers, pesticides, and irrigation","Organic farming only","Reducing farmland"],"Agricultural intensification."),
     ("Negative impacts of the Green Revolution include:",["None","*Soil degradation, water pollution from fertilizers/pesticides, aquifer depletion, biodiversity loss, and fossil fuel dependence","Only positive effects","Only minor issues"],"Environmental costs."),
     ("No-till agriculture reduces erosion by:",["Plowing more","*Not disturbing soil between plantings — crop residue protects against wind and water erosion","Removing all plants","Increasing irrigation"],"Conservation practice."),
     ("Contour plowing involves:",["Plowing straight downhill","*Plowing along the contour (same elevation) of a slope to reduce water runoff and erosion","Plowing in circles","No plowing"],"Reduces runoff."),
     ("Terracing creates stepped fields on hillsides to:",["Increase erosion","*Reduce water runoff speed and soil erosion on steep slopes","Flatten hills","Only look nice"],"Ancient technique."),
     ("Cover crops protect soil by:",["Removing nutrients","*Covering bare soil between planting seasons to prevent erosion, add nutrients, and improve soil structure","Increasing erosion","Blocking sunlight"],"Soil armor."),
     ("Crop rotation benefits soil by:",["Depleting same nutrients","*Alternating crops to prevent nutrient depletion, break pest cycles, and improve soil health","Using one crop always","Increasing pests"],"Nutrient management."),
     ("Monoculture (planting one crop) increases vulnerability to:",["Nothing","*Pests, diseases, and soil nutrient depletion (no diversity to buffer problems)","Drought only","Only weeds"],"Lack of resilience."),
     ("Organic farming avoids:",["All technology","*Synthetic pesticides and fertilizers — relies on natural pest control, composting, and crop rotation","All irrigation","All machinery"],"Reduced chemical inputs."),
     ("Desertification is the process of:",["Creating forests","*Productive land becoming desert-like due to overgrazing, deforestation, drought, and poor farming practices","Flooding land","Only natural processes"],"Land degradation."),
     ("The Dust Bowl (1930s, US Great Plains) was caused by:",["Only drought","*A combination of poor farming practices (removing native grasses) and severe drought → massive topsoil loss","Only wind","Only farming"],"Human + natural disaster."),
     ("Soil compaction from heavy machinery reduces:",["Nothing","*Pore space, water infiltration, root growth, and aeration — harming soil productivity","Crop yields never","Only appearance"],"Structural damage."),
     ("Soil pH affects plant growth because it determines:",["Nothing","*Nutrient availability (most crops prefer pH 6.0–7.0; acidic or alkaline soils lock up nutrients)","Only color","Only texture"],"Chemical availability."),
     ("Integrated Pest Management (IPM) combines:",["Only chemicals","*Biological control, crop rotation, resistant varieties, and minimal pesticide use","Only organic methods","No pest control"],"Balanced approach."),
     ("For the AP exam, students should connect soil to:",["Nothing","*Agriculture, erosion, water quality, food security, and sustainability (soil is the foundation of terrestrial ecosystems)","Only farming","Only chemistry"],"Integrative topic.")]
)
lessons[k]=v

# 4.4
k,v = build_lesson(4,4,"Forests & Deforestation",
    "<h3>Forests &amp; Deforestation</h3>"
    "<p>Forests cover ~31% of Earth's land. They provide ecosystem services: carbon storage, biodiversity habitat, water cycling, soil protection, timber, and recreation.</p>"
    "<h4>Deforestation</h4>"
    "<p>~10 million hectares/year lost (2015–2020). Main drivers: cattle ranching, soy/palm oil farming, logging, and urbanization. Tropical forests are most threatened.</p>",
    [("Deforestation","Permanent clearing of forests for other land uses (agriculture, ranching, urban development)."),
     ("Carbon Sink","Forests absorb more CO₂ than they release; loss converts them to carbon sources."),
     ("Old-Growth Forest","Mature forest that has not been significantly disturbed; highest biodiversity and carbon storage."),
     ("Reforestation","Replanting trees on previously forested land."),
     ("Sustainable Forestry","Managing forests to meet current timber needs without compromising future forest health or biodiversity.")],
    [("Forests cover approximately _____ of Earth's land surface.",["10%","50%","*~31%","75%"],"Nearly a third."),
     ("The leading cause of tropical deforestation is:",["Logging","*Agriculture (cattle ranching, soy, and palm oil plantations)","Urbanization","Mining"],"Agricultural conversion."),
     ("Approximately _____ hectares of forest are lost per year (2015–2020).",["1 million","*~10 million (roughly the size of Iceland annually)","100 million","500,000"],"Massive annual loss."),
     ("Forests are carbon sinks because they:",["Release CO₂","*Absorb more CO₂ through photosynthesis than they release through respiration","Have no carbon role","Only produce oxygen"],"Net carbon uptake."),
     ("Deforestation converts forests from carbon sinks to:",["Bigger sinks","*Carbon sources (stored carbon is released as CO₂ when trees are burned or decompose)","Neutral","Nothing changes"],"Climate impact."),
     ("Old-growth forests are ecologically valuable because they:",["Have no biodiversity","*Have the highest biodiversity, most carbon storage, and complex ecosystem structures developed over centuries","Are easy to replace","Grow fast"],"Irreplaceable."),
     ("The Amazon rainforest produces approximately _____ of Earth's oxygen.",["50%","*~6% (though its role in carbon cycling is much larger)","1%","0%"],"Often overstated; CO₂ absorption is key."),
     ("Slash-and-burn agriculture involves:",["Only cutting","*Cutting and burning forest to clear land for farming; nutrients are quickly depleted from tropical soils","Only burning","Sustainable logging"],"Shifting cultivation."),
     ("Tropical soils are often nutrient-poor because:",["Rain doesn't reach them","*Most nutrients are in the biomass (living organisms), not the soil; rapid decomposition and leaching","They're too deep","They're always fertile"],"Fragile nutrient cycle."),
     ("Palm oil production is linked to deforestation in:",["Only Africa","*Southeast Asia (Indonesia, Malaysia) and increasingly in tropical regions worldwide","Only South America","Only North America"],"Major driver."),
     ("Reforestation means:",["Cutting more trees","*Replanting trees on previously forested land","Building cities","Mining land"],"Restoring forest cover."),
     ("Afforestation means:",["Removing trees","*Planting trees on land that was not previously forested","Reforestation","Deforestation"],"New forest creation."),
     ("Selective logging is less destructive than clear-cutting because it:",["Removes all trees","*Removes only targeted trees, maintaining forest structure and biodiversity","Is never used","Removes the most valuable trees only"],"Sustainable practice."),
     ("Clear-cutting removes all trees in an area, causing:",["No environmental damage","*Erosion, habitat loss, sedimentation of streams, and loss of ecosystem services","Only aesthetic damage","Only noise"],"Maximum disturbance."),
     ("Certification programs like FSC (Forest Stewardship Council) promote:",["Maximum logging","*Sustainable forestry practices verified by independent audits","Only planting","Only protection"],"Consumer choice tool."),
     ("REDD+ is an international program that:",["Encourages deforestation","*Provides financial incentives to developing countries for Reducing Emissions from Deforestation and forest Degradation","Has no funding","Only affects Europe"],"Climate-forest finance."),
     ("Deforestation contributes approximately _____ of global CO₂ emissions.",["1%","*~10-12% (a significant contributor to climate change)","50%","0%"],"Major emission source."),
     ("Mangrove forests are particularly important because they:",["Have no value","*Protect coastlines, serve as fish nurseries, and store carbon at 3-5× the rate of terrestrial forests","Only look nice","Are easy to replace"],"Disproportionate value."),
     ("Urban deforestation contributes to:",["Better air quality","*Heat island effects, increased flooding, reduced air quality, and loss of urban biodiversity","Cooler cities","No impacts"],"Urban ecosystem loss."),
     ("For the AP exam, deforestation connects to:",["Only logging","*Climate change, biodiversity loss, soil erosion, water cycling, and indigenous rights — a multi-dimensional issue","Only one topic","Only economics"],"Integrative concept.")]
)
lessons[k]=v

# 4.5
k,v = build_lesson(4,5,"Fisheries & Ocean Resources",
    "<h3>Fisheries &amp; Ocean Resources</h3>"
    "<p>Fish provide ~17% of animal protein consumed globally. ~34% of fish stocks are overfished; ~60% are fished at maximum sustained yield.</p>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>Maximum Sustainable Yield (MSY):</b> Largest catch that can be taken indefinitely.</li>"
    "<li><b>Bycatch:</b> Unintended species caught and often discarded (dolphins, turtles, sharks).</li>"
    "<li><b>Aquaculture:</b> Farmed fish; now supplies >50% of fish consumed but has environmental impacts.</li></ul>",
    [("Maximum Sustainable Yield (MSY)","Largest harvest that can be taken from a fish stock indefinitely without depleting it."),
     ("Overfishing","Harvesting fish faster than they can reproduce, leading to population decline."),
     ("Bycatch","Unintended capture of non-target species (dolphins, sea turtles, sharks) in fishing operations."),
     ("Aquaculture","Farming of fish, shellfish, or aquatic plants; provides >50% of fish consumed globally."),
     ("Bottom Trawling","Destructive fishing method dragging heavy nets along the ocean floor, damaging seafloor habitats.")],
    [("Approximately _____ of global fish stocks are overfished.",["5%","*~34% (with ~60% fished at maximum capacity)","75%","0%"],"Major sustainability concern."),
     ("Maximum Sustainable Yield (MSY) is:",["The most ever caught","*The largest catch that can be taken indefinitely without depleting the stock","Zero catch","Minimum catch"],"Sustainable limit."),
     ("Bycatch includes:",["Only target fish","*Unintended species caught during fishing operations (dolphins, sea turtles, juvenile fish, sharks)","Only jellyfish","Only seaweed"],"Collateral damage."),
     ("Aquaculture now provides _____ of fish consumed globally.",["10%","25%","*Over 50%","5%"],"Major food source."),
     ("Environmental impacts of aquaculture include:",["None","*Water pollution (waste, antibiotics, chemicals), habitat destruction (mangrove clearing), disease spread to wild fish, and escape of non-native species","Only positive effects","Only in freshwater"],"Not impact-free."),
     ("Bottom trawling is destructive because it:",["Only catches target species","*Drags heavy nets across the seafloor, destroying coral, sponges, and benthic habitats — like bulldozing a forest to catch deer","Is very selective","Only happens in deep water"],"Habitat destruction."),
     ("Fishing down the food web means:",["Catching more top predators","*Progressively targeting smaller, lower-trophic-level species as larger predatory fish are depleted","Adding fish","Farming more fish"],"Indicator of overfishing."),
     ("Individual Transferable Quotas (ITQs) help manage fisheries by:",["Allowing unlimited catch","*Giving fishers tradable shares of the total allowable catch — economic incentive to conserve","Banning fishing","Only restricting gear"],"Market-based conservation."),
     ("Marine Protected Areas (MPAs) help fisheries by:",["Destroying habitat","*Providing refuges where fish can reproduce and grow, replenishing surrounding fishing areas (spillover effect)","Increasing fishing","Removing all fish"],"No-take zones work."),
     ("The collapse of Atlantic cod fisheries off Newfoundland (1992) demonstrated:",["Sustainable fishing","*That even abundant species can collapse from overfishing — the moratorium put 40,000 out of work; stocks still haven't fully recovered","Natural recovery","No consequences"],"Cautionary tale."),
     ("Ghost fishing occurs when:",["Fishers see ghosts","*Abandoned or lost fishing gear (nets, traps) continues to catch and kill marine organisms","Fishing at night","Virtual fishing"],"Ongoing mortality."),
     ("Illegal, Unreported, and Unregulated (IUU) fishing accounts for up to:",["1% of catch","*~30% of global catch in some fisheries","0%","50%"],"Major enforcement challenge."),
     ("Shark finning (removing fins and discarding the body) has caused:",["No decline","*Dramatic declines in shark populations worldwide (~71% decline in oceanic sharks since 1970)","Only minor impacts","Shark increases"],"Conservation crisis."),
     ("Sustainable fishing practices include:",["Bottom trawling everywhere","*Catch limits, gear restrictions (e.g., turtle excluder devices), seasonal closures, and size limits","No regulations","Maximum harvest always"],"Conservation tools."),
     ("Pole-and-line fishing is more sustainable than trawling because it:",["Catches more","*Is highly selective (targets specific species, minimal bycatch)","Is cheaper","Uses larger nets"],"Selective method."),
     ("Ecosystem-based fisheries management considers:",["Only target species","*The entire marine ecosystem including food web interactions, habitat, and non-target species","Only economics","Only one species"],"Holistic approach."),
     ("Subsidies that encourage overfishing should be:",["Increased","*Reformed or eliminated (many governments subsidize fuel, gear, and boat building that enable overcapacity)","Maintained","Doubled"],"Perverse incentives."),
     ("Coral reef destruction threatens fisheries because reefs:",["Have no fish","*Support ~25% of all marine species and serve as nursery habitat for many commercially important fish","Only look pretty","Only affect tourism"],"Biodiversity hotspots."),
     ("For the AP exam, fisheries management connects to:",["Nothing","*Population dynamics, carrying capacity, tragedy of the commons, international policy, and marine ecology","Only biology","Only economics"],"Multi-concept topic."),
     ("The precautionary approach to fisheries means:",["Fish until stocks collapse","*Setting conservative catch limits when scientific uncertainty exists — erring on the side of caution","Ignoring data","Maximum exploitation"],"Better safe than sorry.")]
)
lessons[k]=v

# 4.6
k,v = build_lesson(4,6,"Case Studies: Resource Use",
    "<h3>Case Studies: Resource Use</h3>"
    "<h4>Aral Sea Disaster</h4>"
    "<p>Soviet irrigation diverted rivers feeding the Aral Sea → lost 90% of volume by 2010. Desertification, salt storms, fishery collapse, health crises. Partial recovery in North Aral with dam.</p>"
    "<h4>Three Gorges Dam (China)</h4>"
    "<p>World's largest hydroelectric dam. Generates ~100 TWh/year. But: displaced 1.3 million people, causes erosion, sedimentation, and reduced biodiversity downstream.</p>",
    [("Aral Sea Disaster","Soviet-era irrigation diversions caused one of the worst environmental disasters; Aral Sea lost ~90% volume."),
     ("Three Gorges Dam","World's largest hydroelectric dam on China's Yangtze River; enormous power but major social and environmental costs."),
     ("Ogallala Aquifer Depletion","US Great Plains aquifer being drained for irrigation faster than recharge; threatens food production."),
     ("Conflict Minerals","Minerals mined in conflict zones (coltan, tin, tungsten, gold) whose trade funds armed groups."),
     ("Resource Curse","Paradox where countries rich in natural resources often have poor economic outcomes and governance.")],
    [("The Aral Sea shrank primarily because:",["Climate change","*Soviet irrigation projects diverted the two rivers (Amu Darya and Syr Darya) that fed it","Evaporation increased","An earthquake"],"Human diversion."),
     ("The Aral Sea lost approximately _____ of its volume by 2010.",["10%","50%","*~90%","25%"],"Catastrophic loss."),
     ("Consequences of the Aral Sea disaster include:",["Only water loss","*Desertification, toxic salt/dust storms, fishery collapse, health crises, and economic devastation","Only fishing decline","No consequences"],"Multi-dimensional disaster."),
     ("The North Aral Sea has partially recovered due to:",["Nothing","*Construction of the Kok-Aral Dam (2005) by Kazakhstan, which retained water in the northern section","Rainfall","Soviet restoration"],"Engineering intervention."),
     ("Three Gorges Dam generates approximately _____ TWh of electricity per year.",["10","50","*~100 (making it the world's largest power station by installed capacity)","500"],"Enormous output."),
     ("Three Gorges Dam displaced approximately:",["10,000 people","100,000","*~1.3 million people","10 million"],"Massive relocation."),
     ("Environmental impacts of Three Gorges Dam include:",["None","*Downstream erosion, sediment trapping, reduced biodiversity, landslide risk, and water quality changes","Only positive effects","Only fish impacts"],"Significant environmental costs."),
     ("The Ogallala Aquifer is critical because it:",["Is not used","*Provides ~30% of US irrigation water; supports billions of dollars in agriculture in the Great Plains","Only serves one state","Is unlimited"],"Agricultural lifeline."),
     ("The Ogallala Aquifer is being depleted because:",["It's renewable","*Pumping rates far exceed the very slow natural recharge (~0.5-2.5 cm/year)","It has too much water","No one uses it"],"Unsustainable withdrawal."),
     ("Coltan mining in the Democratic Republic of Congo is linked to:",["No problems","*Armed conflict, human rights abuses, environmental destruction, and funding of militia groups","Only economic growth","Only technology"],"Conflict mineral."),
     ("The concept of 'resource curse' applies to countries like:",["Switzerland","*Nigeria (oil), DRC (minerals), Venezuela (oil) — resource wealth + poor governance = conflict and poverty","Japan","Singapore"],"Wealth without development."),
     ("Chile's Atacama Desert is important for mining:",["Gold only","*Lithium and copper (critical for batteries, electronics, and renewable energy technology)","Only salt","Nothing"],"Green energy minerals."),
     ("Mining environmental impacts include:",["None","*Habitat destruction, water contamination (acid mine drainage), air pollution, soil degradation, and waste piles","Only dust","Only noise"],"Multi-dimensional damage."),
     ("Acid mine drainage occurs when:",["Normal rain falls","*Exposed sulfide minerals in mine waste react with water and air to produce sulfuric acid, contaminating waterways","Mines are closed properly","Only in specific mines"],"Persistent toxic pollution."),
     ("The Deepwater Horizon oil spill (2010) released:",["A small amount","*~4.9 million barrels of oil into the Gulf of Mexico (largest marine oil spill in US history)","Only gasoline","Only in deep water"],"Catastrophic spill."),
     ("These case studies share common themes of:",["Unlimited resources","*Trade-offs between resource use and environmental/social costs; unintended consequences of large-scale projects","No problems","Only benefits"],"Recurring pattern."),
     ("Lessons from these cases suggest that resource management needs:",["No planning","*Environmental impact assessments, long-term thinking, stakeholder input, and precautionary approaches","Only short-term profit focus","Only government control"],"Balanced planning."),
     ("Environmental Impact Assessments (EIAs) are important because they:",["Waste time","*Evaluate potential environmental consequences before a project begins, allowing informed decision-making","Only delay projects","Have no legal standing"],"Preventive tool."),
     ("International cooperation is needed for resource management because:",["Resources are only local","*Many resources cross borders (water, fish, atmosphere), and global trade connects distant impacts","Only one country matters","There's no need"],"Shared resources."),
     ("For the AP exam, case studies test the ability to:",["Only memorize facts","*Analyze complex trade-offs, identify stakeholders, evaluate policies, and propose sustainable alternatives","Only name places","Only describe disasters"],"Applied critical thinking.")]
)
lessons[k]=v

# 4.7
k,v = build_lesson(4,7,"AP Prep: Resource Management Models",
    "<h3>AP Prep: Resource Management Models</h3>"
    "<h4>Key Models &amp; Concepts</h4>"
    "<ul><li><b>Tragedy of the commons:</b> Shared resources depleted by self-interest (Hardin, 1968). Solutions: regulation, privatization, community management.</li>"
    "<li><b>Maximum Sustainable Yield (MSY):</b> Largest harvest sustainable indefinitely. Applied to fisheries, forestry.</li>"
    "<li><b>Cost-benefit analysis:</b> Weighing economic costs vs. benefits of a resource decision; externalities often excluded.</li>"
    "<li><b>Precautionary principle:</b> When uncertain, err on the side of protection.</li></ul>",
    [("Tragedy of the Commons","Shared resources depleted when individuals act in self-interest; solutions include regulation, privatization, and community management."),
     ("Cost-Benefit Analysis","Economic tool comparing costs and benefits of a project or policy; often fails to account for environmental externalities."),
     ("Externality","A cost or benefit not reflected in market prices (e.g., pollution costs borne by society, not the polluter)."),
     ("Precautionary Principle","When potential for harm exists but science is uncertain, take preventive action to avoid environmental damage."),
     ("Adaptive Management","Flexible resource management approach that adjusts strategies based on monitoring and new data.")],
    [("The tragedy of the commons describes:",["Private property problems","*Overuse of shared resources when individuals maximize personal gain at collective expense","Government failure only","Only historical events"],"Shared resource dilemma."),
     ("Garrett Hardin proposed solutions including:",["More exploitation","*Privatization (assigning ownership) or regulation (government-enforced limits)","Ignoring the problem","Only education"],"Institutional solutions."),
     ("Elinor Ostrom's research showed that:",["Only government can manage commons","*Communities can successfully self-manage common resources through local rules and cooperation (Nobel Prize 2009)","Commons always fail","Privatization always works"],"Community governance."),
     ("MSY assumes population growth follows:",["Exponential growth only","*Logistic growth — maximum reproduction occurs at N = K/2","No growth","Linear growth"],"Population ecology basis."),
     ("Cost-benefit analysis often underestimates environmental damage because:",["It's perfect","*Externalities (pollution costs, ecosystem service losses) are difficult to monetize and often excluded","Everything is counted","Damage is minor"],"Incomplete accounting."),
     ("An externality is:",["An internal cost","*A cost or benefit not reflected in market prices (e.g., factory pollution harming neighbors)","A profit","A subsidy"],"Uncaptured impact."),
     ("The precautionary principle states:",["Wait for certainty","*Take protective action when there's potential for serious harm, even without full scientific certainty","Ignore risk","Only act after damage"],"Better safe than sorry."),
     ("Adaptive management involves:",["Setting fixed rules forever","*Monitoring outcomes and adjusting management strategies based on new data and results","Never changing plans","Only one approach"],"Learn and adjust."),
     ("A discount rate in resource economics:",["Increases future value","*Reduces the present value of future costs and benefits — high discount rates favor short-term exploitation","Has no effect","Only applies to money"],"Time preference."),
     ("High discount rates lead to:",["More conservation","*More resource exploitation now (future resources are valued less than current ones)","Balanced management","No economic change"],"Short-term bias."),
     ("Natural capital refers to:",["Only money","*The stock of natural resources and ecosystem services that provide value to humans","Man-made capital","Only living things"],"Nature as asset."),
     ("Ecosystem services include:",["Only timber","*Provisioning (food, water), regulating (climate, flood control), supporting (nutrient cycles), and cultural (recreation, aesthetics)","Only recreation","Nothing measurable"],"Four categories (MEA)."),
     ("Payments for Ecosystem Services (PES) programs:",["Charge nature","*Compensate landowners for maintaining ecosystem services (e.g., paying farmers to protect watersheds)","Only tax polluters","Have never been tried"],"Market-based conservation."),
     ("Cap-and-trade systems for managing resources:",["Set no limits","*Set an overall cap on resource use/pollution and allow trading of permits — market finds efficient allocation","Only regulate","Only tax"],"Market + regulation."),
     ("Subsidies can be harmful when they:",["Always help conservation","*Encourage overexploitation of resources (e.g., fossil fuel subsidies, fishing subsidies that enable overcapacity)","Never cause problems","Are always transparent"],"Perverse incentives."),
     ("The safe minimum standard approach says we should:",["Maximize extraction","*Maintain the minimum viable population/resource level unless the costs of doing so are unacceptably high","Ignore all standards","Only protect charismatic species"],"Conservation threshold."),
     ("Intergenerational equity in resource management means:",["Only current needs matter","*Ensuring future generations have access to resources and a healthy environment (sustainability principle)","Future needs don't count","Only economic growth matters"],"Sustainable development cornerstone."),
     ("The 'triple bottom line' evaluates projects on:",["Only profit","*Environmental, social, and economic outcomes (planet, people, profit)","Only environmental impact","Only social justice"],"Comprehensive evaluation."),
     ("For AP free-response on resource management, students should:",["Only describe one model","*Compare models (tragedy of commons, MSY, CBA), evaluate trade-offs, and apply the precautionary principle","Only memorize definitions","Only give opinions"],"Analytical framework."),
     ("Effective resource management requires integrating:",["Only economics","*Ecological science, economics, social equity, technology, and policy — no single approach is sufficient","Only science","Only politics"],"Interdisciplinary approach.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 4: wrote {len(lessons)} lessons")
