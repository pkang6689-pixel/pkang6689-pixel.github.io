#!/usr/bin/env python3
"""Environmental Science Unit 7 – Climate Change (7 lessons)."""
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

# 7.1
k,v = build_lesson(7,1,"Greenhouse Effect & Global Warming",
    "<h3>Greenhouse Effect &amp; Global Warming</h3>"
    "<p>The <b>natural greenhouse effect</b> keeps Earth ~33°C warmer than it would be without an atmosphere (−18°C → +15°C). Greenhouse gases (CO₂, CH₄, N₂O, H₂O, CFCs) absorb and re-emit infrared radiation.</p>"
    "<h4>Enhanced Greenhouse Effect</h4>"
    "<p>Human activities (fossil fuels, deforestation, agriculture) have increased CO₂ from ~280 ppm (pre-industrial) to ~424 ppm (2024). Global temperature has risen ~1.1°C above pre-industrial levels.</p>",
    [("Greenhouse Effect","Natural process: greenhouse gases trap infrared radiation, warming Earth ~33°C above what it would be without an atmosphere."),
     ("Enhanced Greenhouse Effect","Human-caused increase in greenhouse gas concentrations intensifying the natural greenhouse effect → global warming."),
     ("CO₂ Concentration","Pre-industrial: ~280 ppm; 2024: ~424 ppm — a 50%+ increase primarily from fossil fuel burning and deforestation."),
     ("Radiative Forcing","Change in net energy balance at the top of the atmosphere; positive forcing warms, negative cools."),
     ("Global Warming Potential (GWP)","Measure comparing a greenhouse gas's heat-trapping ability to CO₂ over a set period (e.g., CH₄ GWP ≈ 80 over 20 years).")],
    [("The natural greenhouse effect makes Earth approximately _____ warmer than it would be otherwise.",["5°C","10°C","*~33°C (from −18°C to +15°C average)","50°C"],"Essential for life."),
     ("The primary greenhouse gases are:",["Only CO₂","*CO₂, CH₄, N₂O, water vapor, and CFCs","Only methane","Only water vapor"],"Multiple gases."),
     ("Pre-industrial CO₂ concentration was approximately:",["100 ppm","*~280 ppm","400 ppm","500 ppm"],"Baseline level."),
     ("Current CO₂ concentration (2024) is approximately:",["280 ppm","350 ppm","*~424 ppm","500 ppm"],"50%+ increase."),
     ("The largest source of anthropogenic CO₂ is:",["Agriculture","Deforestation","*Fossil fuel combustion (coal, oil, natural gas for energy and transport)","Volcanoes"],"~75% of human CO₂."),
     ("Methane (CH₄) is a more potent greenhouse gas than CO₂ because it:",["Is more abundant","*Traps ~80× more heat per molecule over 20 years (though it's shorter-lived in the atmosphere)","Lasts longer","Is less potent"],"Powerful but shorter-lived."),
     ("Sources of anthropogenic methane include:",["Only fossil fuels","*Livestock (enteric fermentation), rice paddies, landfills, fossil fuel extraction, and wetland changes","Only wetlands","Only termites"],"Multiple sources."),
     ("N₂O (nitrous oxide) comes primarily from:",["Transportation","*Agricultural fertilizers and soil management (nitrogen cycle disruption)","Buildings","Oceans only"],"Agricultural source."),
     ("CFCs are greenhouse gases AND they also:",["Promote ozone","*Destroy stratospheric ozone (the ozone layer)","Are natural","Are harmless"],"Double threat."),
     ("Water vapor is the most abundant greenhouse gas but is not directly controlled because:",["It's not a greenhouse gas","*Its concentration is determined by temperature (it amplifies warming as a feedback, not a driver)","It's decreasing","Humans produce none"],"Feedback amplifier."),
     ("Global average temperature has risen approximately _____ above pre-industrial levels.",["0.1°C","0.5°C","*~1.1°C (and accelerating)","5°C"],"Observed warming."),
     ("The Keeling Curve shows:",["Temperature history","*The continuous rise of atmospheric CO₂ since 1958 (measured at Mauna Loa, Hawaii)","Sea level rise","Population growth"],"Iconic CO₂ record."),
     ("Positive feedback loops in climate include:",["Only cooling effects","*Ice-albedo feedback (melting ice → less reflection → more warming → more melting) and water vapor amplification","Only stabilizing effects","No feedbacks"],"Amplifying change."),
     ("The albedo effect refers to:",["Heat absorption","*Reflectivity of a surface (ice/snow have high albedo; dark ocean has low albedo)","Greenhouse gases","Ozone depletion"],"Surface reflectivity."),
     ("Carbon sinks include:",["Only the atmosphere","*Oceans, forests, and soils (they absorb more CO₂ than they release)","Only volcanoes","Only human systems"],"CO₂ removal."),
     ("Radiative forcing is positive when it _____ Earth's energy balance.",["Decreases","*Increases (more energy retained than lost → warming)","Balances","Has no effect on"],"Energy imbalance."),
     ("The greenhouse effect is essential for life because without it:",["Earth would be too hot","*Earth's average temperature would be ~−18°C (too cold for liquid water and most life)","Nothing would change","Only nights would be cold"],"Life-sustaining process."),
     ("CO₂ remains in the atmosphere for approximately:",["1 year","10 years","*Centuries to millennia (a significant portion persists for 300-1,000+ years)","1 week"],"Long atmospheric lifetime."),
     ("The relationship between CO₂ and temperature over geological time is:",["No correlation","*Strongly correlated — ice core records show CO₂ and temperature have risen and fallen together for 800,000+ years","Inverse correlation","Random"],"Ice core evidence."),
     ("For AP, students must understand that the greenhouse effect is:",["Entirely bad","*A natural, essential process that has been enhanced by human activities to dangerous levels","Only natural","Only human-caused"],"Natural + enhanced.")]
)
lessons[k]=v

# 7.2
k,v = build_lesson(7,2,"Evidence of Climate Change",
    "<h3>Evidence of Climate Change</h3>"
    "<h4>Multiple Lines of Evidence</h4>"
    "<ul><li><b>Temperature records:</b> Instrumental records since 1850; 10 warmest years all since 2010.</li>"
    "<li><b>Ice cores:</b> Trapped air bubbles show CO₂/temperature correlation over 800,000 years.</li>"
    "<li><b>Sea level rise:</b> ~20 cm since 1900; accelerating (~3.6 mm/year now).</li>"
    "<li><b>Arctic ice decline:</b> Summer Arctic sea ice volume down ~75% since 1979.</li>"
    "<li><b>Ocean warming &amp; acidification:</b> Oceans absorbed ~90% of excess heat and ~30% of CO₂.</li></ul>",
    [("Ice Cores","Cylinders of ice drilled from glaciers that contain trapped air bubbles recording past atmospheric composition."),
     ("Sea Level Rise","Global sea levels have risen ~20 cm since 1900; caused by thermal expansion and ice sheet melting."),
     ("Thermal Expansion","Water expands as it warms; accounts for ~50% of observed sea level rise."),
     ("Ocean Acidification","Oceans absorb CO₂, forming carbonic acid; pH has dropped ~0.1 units (30% more acidic) since pre-industrial times."),
     ("Proxy Data","Indirect evidence of past climate from tree rings, ice cores, coral, and sediment (before instrument records).")],
    [("The 10 warmest years on record have all occurred since:",["1990","2000","*2010","1980"],"Recent accelerating trend."),
     ("Ice cores provide climate data going back approximately:",["1,000 years","10,000 years","*800,000+ years","10 million years"],"Deep time record."),
     ("Ice cores contain _____ that reveal past atmospheric composition.",["Fossils","*Trapped air bubbles","Minerals","Water only"],"Tiny time capsules."),
     ("Global sea level has risen approximately _____ since 1900.",["5 cm","10 cm","*~20 cm (about 8 inches)","50 cm"],"Accelerating rise."),
     ("Current rate of sea level rise is approximately:",["1 mm/year","*~3.6 mm/year (and accelerating)","10 mm/year","0.1 mm/year"],"Faster each decade."),
     ("Sea level rise is caused primarily by:",["More rain","*Thermal expansion of warming ocean water AND melting of land-based ice (glaciers, ice sheets)","River flow","Only ice melting"],"Two main causes."),
     ("Summer Arctic sea ice volume has declined approximately _____ since 1979.",["10%","25%","50%","*~75%"],"Dramatic decline."),
     ("Oceans have absorbed approximately _____ of the excess heat from global warming.",["10%","50%","*~90% (oceans are a massive heat sink, masking atmospheric warming)","100%"],"Heat buffer."),
     ("Ocean acidification occurs because:",["Acid rain","*The ocean absorbs CO₂, which reacts with water to form carbonic acid, lowering pH","Volcanic activity","Only temperature"],"CO₂ absorption."),
     ("Ocean pH has decreased by approximately _____ since pre-industrial times.",["1 unit","*~0.1 units (which represents a ~30% increase in acidity — pH is logarithmic)","0.001 units","3 units"],"Significant on log scale."),
     ("Coral bleaching is intensifying due to:",["Cold water","*Warming ocean temperatures causing corals to expel symbiotic algae (zooxanthellae)","Less sunlight","More nutrients"],"Thermal stress."),
     ("Glacier retreat worldwide is evidence of warming because:",["Glaciers are growing","*Nearly all glaciers globally are losing mass, consistent with rising temperatures","Only some are shrinking","It's a natural cycle only"],"Global pattern."),
     ("Permafrost thawing in the Arctic is concerning because it:",["Has no effect","*Releases stored methane and CO₂ (a positive feedback that accelerates warming)","Only affects buildings","Only local impact"],"Carbon bomb."),
     ("Tree ring data (dendrochronology) provides evidence of:",["Only tree age","*Past temperature and precipitation patterns (wider rings = favorable growth; narrower = stress)","Only forest fires","Only rainfall"],"Proxy climate record."),
     ("The scientific consensus on climate change is supported by:",["Only a few scientists","*~97%+ of climate scientists and every major scientific organization worldwide","Only the IPCC","Only one country"],"Overwhelming agreement."),
     ("The IPCC (Intergovernmental Panel on Climate Change) concluded that:",["Climate isn't changing","*It is unequivocal that human activities have warmed the atmosphere, ocean, and land","Only natural causes","Science is uncertain"],"Definitive statement."),
     ("Phenological changes (earlier spring events) are evidence because:",["Nothing is changing","*Plants flowering, birds migrating, and insects emerging earlier indicate warming temperatures","Only one species changes","It's random"],"Biological indicators."),
     ("Satellite data since 1979 confirms:",["Cooling","*Arctic ice decline, sea level rise, shifting precipitation patterns, and global temperature increases","No changes","Only partial warming"],"Space-based evidence."),
     ("Attribution science can now determine:",["Nothing about causes","*The human contribution to specific extreme weather events (e.g., heatwave likelihood multiplied by climate change)","Only natural causes","Only future events"],"Connecting events to causes."),
     ("For the AP exam, students should cite _____ lines of evidence for climate change.",["One","*Multiple independent lines (temperature records, ice cores, sea level, ice decline, ocean changes, biological changes)","Only computer models","Only one source"],"Convergent evidence.")]
)
lessons[k]=v

# 7.3
k,v = build_lesson(7,3,"Impacts on Ecosystems & Humans",
    "<h3>Climate Change Impacts</h3>"
    "<h4>Ecosystems</h4>"
    "<ul><li>Range shifts: species moving poleward and to higher elevations.</li>"
    "<li>Coral bleaching: 14% of coral lost 2009–2018.</li>"
    "<li>Phenology disruption: mismatches between species (pollinators arriving at wrong time).</li></ul>"
    "<h4>Humans</h4>"
    "<ul><li>Extreme weather: more intense heat waves, droughts, hurricanes, and floods.</li>"
    "<li>Food security: crop yield declines; fisheries shifting.</li>"
    "<li>Health: heat-related illness, vector-borne diseases expanding range, air quality worsening.</li>"
    "<li>Climate refugees: displacement from sea level rise, drought, and extreme weather.</li></ul>",
    [("Range Shift","Species moving to higher latitudes or elevations in response to warming temperatures."),
     ("Phenological Mismatch","When timing of ecological events (flowering, migration) becomes out of sync between interdependent species."),
     ("Climate Refugee","Person displaced by climate-related environmental changes (sea level rise, drought, extreme weather)."),
     ("Food Security","Reliable access to sufficient, safe, nutritious food; threatened by changing precipitation, temperature, and extreme events."),
     ("Vector-Borne Disease","Diseases transmitted by organisms like mosquitoes and ticks; expanding range as warm areas expand (malaria, dengue, Lyme).")],
    [("Species responding to warming are generally moving:",["Toward the equator","*Poleward and to higher elevations (tracking their climate envelope)","Deeper underground","Into cities"],"Tracking temperature."),
     ("Phenological mismatch means:",["Everything syncs perfectly","*The timing of ecological events (e.g., flowering vs. pollinator arrival) becomes out of sync due to differential responses to warming","Nothing changes","Only plants are affected"],"Timing disruption."),
     ("Coral bleaching has led to loss of approximately _____ of the world's coral since 2009.",["1%","*~14%","50%","None"],"Massive reef decline."),
     ("Climate change is expected to _____ the frequency and intensity of extreme weather events.",["Decrease","*Increase (more intense heat waves, droughts, hurricanes, heavy rainfall, and flooding)","Not change","Only affect some events"],"Amplified extremes."),
     ("Sea level rise threatens approximately _____ of the world's population living in low-lying coastal areas.",["1%","*~10% (~800 million people)","50%","0.1%"],"Massive displacement risk."),
     ("Climate change affects food security through:",["Only one mechanism","*Changing precipitation, increased heat stress on crops, more extreme weather, shifting pest ranges, and water scarcity","No mechanisms","Only flooding"],"Multi-pathway threat."),
     ("Vector-borne diseases are expanding because:",["Vectors are shrinking","*Warmer temperatures expand the range of mosquitoes and ticks (malaria, dengue, Lyme disease moving to new areas)","Cold kills disease","Only in tropics"],"Range expansion."),
     ("Climate refugees are people displaced by:",["Only war","*Climate-related events: sea level rise, desertification, extreme weather, and water scarcity","Only earthquakes","Only poverty"],"Environmental displacement."),
     ("Small island nations face existential threats from:",["Drought only","*Sea level rise that could submerge entire countries (e.g., Tuvalu, Marshall Islands, Maldives)","Only storms","Temperature alone"],"National survival."),
     ("Arctic ecosystems are warming _____ the global average.",["Slower than","*About 2–4× faster than (Arctic amplification)","At the same rate as","Not at all compared to"],"Amplified warming."),
     ("Polar bears are threatened because:",["They're hunted","*Declining Arctic sea ice reduces their hunting platform for seals (their primary food)","They're too warm","Their prey is increasing"],"Ice-dependent species."),
     ("Ocean warming reduces fishery productivity because:",["Fish prefer warm water","*Warmer water holds less oxygen and disrupts nutrient upwelling → reduced fish populations and range shifts","Fish are more active","Nothing changes"],"Marine food web impact."),
     ("Heat-related mortality is increasing, especially among:",["Young athletes","*Elderly, outdoor workers, urban poor, and people with pre-existing health conditions","Only in tropics","Only in winter"],"Vulnerable populations."),
     ("Climate change worsens air quality because:",["It cleans the air","*Higher temperatures increase ground-level ozone formation, and wildfires (more frequent) produce PM2.5","No connection","Only indoors"],"Health pathway."),
     ("Mountain glaciers melting threatens water supply for:",["Nobody","*Billions of people who depend on glacial meltwater for drinking, irrigation, and hydropower (Himalayas, Andes, Alps)","Only mountaineers","Only one continent"],"Water security."),
     ("The economic cost of climate change includes:",["Only adaptation costs","*Damage from extreme weather, agriculture losses, health costs, infrastructure damage, and productivity loss (trillions of dollars projected)","No measurable cost","Only insurance costs"],"Enormous economic impact."),
     ("Climate change disproportionately affects:",["Rich nations","*Developing nations and vulnerable communities who contributed least to emissions (environmental injustice)","Only cold regions","All nations equally"],"Unequal burden."),
     ("Tipping points in climate systems are:",["Impossible","*Thresholds beyond which change becomes irreversible and self-reinforcing (e.g., ice sheet collapse, Amazon dieback)","Already passed all of them","Not scientifically real"],"Points of no return."),
     ("Biodiversity loss from climate change is compounded by:",["Nothing","*Habitat destruction, pollution, and overexploitation — climate change adds pressure to already stressed ecosystems","Climate alone","Only one factor"],"Multiple stressors."),
     ("For the AP exam, impact questions require connecting:",["Only temperatures","*Climate change to specific ecological, social, economic, and health outcomes with cause-and-effect reasoning","Only to one sector","Only to predictions"],"Systems thinking.")]
)
lessons[k]=v

# 7.4
k,v = build_lesson(7,4,"Mitigation & Adaptation",
    "<h3>Mitigation &amp; Adaptation</h3>"
    "<h4>Mitigation (reducing causes)</h4>"
    "<ul><li>Transition to renewable energy.</li>"
    "<li>Energy efficiency improvements.</li>"
    "<li>Carbon pricing (tax or cap-and-trade).</li>"
    "<li>Reforestation and soil carbon sequestration.</li></ul>"
    "<h4>Adaptation (adjusting to impacts)</h4>"
    "<ul><li>Sea walls and flood barriers.</li>"
    "<li>Drought-resistant crops.</li>"
    "<li>Urban cooling (green infrastructure, reflective surfaces).</li>"
    "<li>Early warning systems for extreme weather.</li></ul>",
    [("Mitigation","Actions that reduce the sources or enhance the sinks of greenhouse gases (addressing the cause)."),
     ("Adaptation","Actions that adjust to current or expected climate change impacts (addressing the effects)."),
     ("Carbon Sequestration","Capturing and storing CO₂ from the atmosphere (forests, soils, carbon capture technology)."),
     ("Carbon Pricing","Making fossil fuels more expensive through taxes or cap-and-trade to reflect their climate costs."),
     ("Climate Resilience","The ability of a system (ecosystem, community) to withstand and recover from climate impacts.")],
    [("Mitigation addresses climate change by:",["Adapting to impacts","*Reducing greenhouse gas emissions or increasing carbon sinks (tackling the root cause)","Only building barriers","Only planting trees"],"Address the cause."),
     ("Adaptation addresses climate change by:",["Reducing emissions","*Adjusting human and natural systems to cope with current and expected climate impacts","Only cutting CO₂","Only using solar"],"Cope with effects."),
     ("Both mitigation and adaptation are needed because:",["Only one works","*Some warming is already locked in (requiring adaptation), but limiting future warming requires emission reductions (mitigation)","Neither works","They're the same"],"Complementary strategies."),
     ("Examples of mitigation include:",["Sea walls","*Transitioning to renewable energy, improving efficiency, carbon pricing, and reforestation","Only flood barriers","Only drought-resistant crops"],"Emission reduction."),
     ("Examples of adaptation include:",["Reducing emissions","*Sea walls, drought-resistant crops, urban cooling, wildfire management, and early warning systems","Only solar panels","Only wind turbines"],"Impact management."),
     ("Carbon sequestration includes:",["Only burning fossil fuels","*Reforestation, soil carbon management, ocean fertilization, and engineered carbon capture and storage (CCS)","Only one method","Nothing effective"],"CO₂ removal."),
     ("A carbon tax works by:",["Subsidizing emissions","*Putting a price on CO₂ emissions, making fossil fuels more expensive and clean alternatives more competitive","Only affecting consumers","Having no effect"],"Market signal."),
     ("Cap-and-trade differs from a carbon tax by:",["Being identical","*Setting a cap on total emissions and allowing companies to trade emission allowances (the market sets the price)","Being less effective","Only taxing heavy polluters"],"Quantity vs. price approach."),
     ("Nature-based solutions for climate include:",["Only technology","*Protecting and restoring forests, wetlands, mangroves, and grasslands (which naturally absorb CO₂)","Only geo-engineering","Only nuclear power"],"Ecosystem-based mitigation."),
     ("Green infrastructure for urban adaptation includes:",["More concrete","*Green roofs, urban forests, permeable pavements, and reflective surfaces to reduce heat island effect and flooding","Only air conditioning","Only moving people"],"Cool cities."),
     ("Drought-resistant crop development is a form of:",["Mitigation","*Adaptation (adjusting agricultural systems to cope with changing precipitation patterns)","Neither","Both equally"],"Adjusting to change."),
     ("Early warning systems for extreme weather are:",["Mitigation","*Adaptation (protecting lives through advance preparation and evacuation for anticipated climate events)","Neither","Only for rich countries"],"Life-saving adaptation."),
     ("Carbon Capture and Storage (CCS) captures CO₂ from:",["The ocean","*Power plant emissions or directly from the atmosphere, then stores it underground","Only trees","Only soil"],"Technology-based solution."),
     ("Direct Air Capture (DAC) is a technology that:",["Is science fiction","*Removes CO₂ directly from ambient air using chemical processes (currently expensive but scaling)","Only works in labs","Only theoretical"],"Emerging technology."),
     ("Managed retreat involves:",["Fighting the ocean","*Relocating communities and infrastructure away from areas threatened by sea level rise or other climate hazards","Only building walls","Only raising houses"],"Strategic withdrawal."),
     ("Climate-smart agriculture includes:",["Only conventional farming","*Practices that increase productivity, enhance resilience, and reduce emissions (cover crops, no-till, efficient irrigation)","Only organic farming","Only livestock reduction"],"Triple-win approach."),
     ("Geoengineering proposals include:",["Only proven methods","*Solar radiation management (reflecting sunlight) and carbon dioxide removal — controversial due to risks and unintended consequences","Only safe methods","Only natural approaches"],"High-risk, high-stakes."),
     ("The Paris Agreement goal implies limiting warming to:",["5°C","3°C","*Well below 2°C, preferably 1.5°C above pre-industrial levels","No specific target"],"Global target."),
     ("Individual actions for mitigation include:",["Nothing individuals can do","*Reducing energy use, eating less meat, driving less, flying less, and voting for climate policy","Only protesting","Only recycling"],"Personal + political."),
     ("For AP, students should distinguish between and give examples of:",["Only mitigation","Only adaptation","*Both mitigation (reducing causes) and adaptation (adjusting to effects) strategies","Neither"],"Both are tested.")]
)
lessons[k]=v

# 7.5
k,v = build_lesson(7,5,"International Agreements (Kyoto, Paris)",
    "<h3>International Climate Agreements</h3>"
    "<h4>Kyoto Protocol (1997)</h4>"
    "<p>First binding agreement to reduce GHG emissions. Required developed nations to reduce emissions ~5% below 1990 levels. US never ratified. Mixed results.</p>"
    "<h4>Paris Agreement (2015)</h4>"
    "<p>Nearly every nation (196 parties). Goal: limit warming to well below 2°C, preferably 1.5°C. Countries set own targets (NDCs — Nationally Determined Contributions). Not legally binding. Updated every 5 years.</p>",
    [("Kyoto Protocol","1997 international treaty requiring developed nations to reduce greenhouse gas emissions ~5% below 1990 levels."),
     ("Paris Agreement","2015 global climate accord: nearly all nations committed to limiting warming to well below 2°C, preferably 1.5°C."),
     ("NDCs","Nationally Determined Contributions: each country's self-set climate targets under the Paris Agreement."),
     ("UNFCCC","United Nations Framework Convention on Climate Change: the parent treaty for Kyoto and Paris agreements."),
     ("Common but Differentiated Responsibilities","Principle that all nations share climate responsibility but developed nations bear greater obligation due to historical emissions.")],
    [("The Kyoto Protocol (1997) was the first binding treaty to:",["Address ozone","*Reduce greenhouse gas emissions (required developed nations to cut emissions ~5% below 1990 levels)","Ban nuclear weapons","Address biodiversity"],"First binding climate treaty."),
     ("The US _____ the Kyoto Protocol.",["Ratified","*Never ratified (signed but never approved by the Senate)","Proposed","Led"],"US non-participation."),
     ("A key limitation of Kyoto was that it:",["Applied to all nations","*Only required emission reductions from developed nations; excluded developing nations like China and India","Was too strict","Had no targets"],"Partial coverage."),
     ("The Paris Agreement (2015) was signed by:",["Only a few nations","*Nearly every nation in the world (196 parties)","Only developed nations","Only the US and EU"],"Near-universal."),
     ("The Paris Agreement's temperature goal is:",["No specific target","Below 5°C","*Well below 2°C, preferably 1.5°C above pre-industrial levels","Exactly 1°C"],"Ambitious target."),
     ("NDCs (Nationally Determined Contributions) are:",["Mandatory emission cuts","*Each country's self-set climate targets under Paris — voluntary and updated every 5 years","UN-imposed limits","Only for developed nations"],"Bottom-up approach."),
     ("The Paris Agreement is different from Kyoto because it:",["Is identical","*Includes all nations (not just developed), uses voluntary NDCs rather than binding targets, and updates every 5 years","Excludes all nations","Only covers CO₂"],"More inclusive, less binding."),
     ("A criticism of the Paris Agreement is that:",["It's too binding","*Current NDCs are insufficient to limit warming to 1.5°C or even 2°C; voluntary nature means no enforcement mechanism","It's too strict","No nations signed"],"Ambition gap."),
     ("The 'ratchet mechanism' in the Paris Agreement means:",["Going backward","*Countries are expected to increase their climate ambition over time (each successive NDC should be stronger)","Staying the same","Only decreasing targets"],"Increasing ambition."),
     ("Common but Differentiated Responsibilities (CBDR) means:",["All nations are equal","*All nations share climate responsibility, but developed nations bear greater obligation due to historical emissions and greater capacity","Only developing nations act","Only the US acts"],"Equity principle."),
     ("Climate finance ($100 billion/year goal) is meant to help:",["Rich nations adapt","*Developing nations mitigate emissions and adapt to climate impacts","Only research","Only technology transfer"],"North-South finance."),
     ("The Green Climate Fund was established to:",["Fund fossil fuels","*Channel climate finance to developing countries for mitigation and adaptation projects","Only research","Only one country"],"Climate finance mechanism."),
     ("The US withdrew from the Paris Agreement under _____ and rejoined under _____.",["Obama; Biden","*Trump (2020); Biden (2021)","Bush; Obama","Clinton; Bush"],"US policy shifts."),
     ("COP (Conference of the Parties) refers to:",["A police conference","*Annual UN climate negotiations where nations discuss climate action (e.g., COP28 in Dubai, 2023)","Corporation meetings","Only one meeting"],"Annual climate summit."),
     ("The Montreal Protocol (1987) on ozone shows that:",["International agreements don't work","*Global environmental treaties can be highly successful (CFC reduction → ozone layer recovery on track)","Only small problems can be solved","Ozone was never at risk"],"Success model."),
     ("Carbon markets created under international agreements allow:",["Unlimited emissions","*Countries or companies to trade emission credits, theoretically reducing costs of emission reductions","Only one country to act","No trading"],"Market mechanism."),
     ("Article 6 of the Paris Agreement deals with:",["Only forests","*International carbon markets and cooperative approaches to emission reductions","Only technology","Only finance"],"Carbon trading rules."),
     ("Loss and Damage refers to:",["Insurance costs","*Impacts of climate change that go beyond what can be adapted to, especially in vulnerable nations","Only property damage","Only flooding"],"Beyond adaptation."),
     ("For AP, students should compare Kyoto and Paris in terms of:",["Only dates","*Scope (who participates), binding vs. voluntary, targets, mechanisms, and effectiveness","Only names","Only temperature goals"],"Comparative analysis."),
     ("The ultimate success of climate agreements depends on:",["Signatures alone","*Whether nations actually implement their commitments and increase ambition fast enough to limit warming","Only technology","Only finance"],"Implementation is key.")]
)
lessons[k]=v

# 7.6
k,v = build_lesson(7,6,"Case Studies: Climate Policy",
    "<h3>Case Studies: Climate Policy</h3>"
    "<h4>EU Emissions Trading System (EU ETS)</h4>"
    "<p>World's largest carbon market. Cap-and-trade covering ~40% of EU emissions. Reduced covered emissions ~35% since 2005.</p>"
    "<h4>California's Climate Programs</h4>"
    "<p>State-level action: cap-and-trade, 100% clean electricity by 2045, EV mandates, building codes. Often ahead of federal policy.</p>"
    "<h4>China's Dual Role</h4>"
    "<p>Largest emitter (~30% of global CO₂) but also largest renewable energy investor. Launched world's largest ETS in 2021.</p>",
    [("EU ETS","European Union Emissions Trading System: world's largest cap-and-trade carbon market since 2005."),
     ("California Climate Action","Comprehensive state-level climate policy including cap-and-trade, 100% clean electricity target, and EV mandates."),
     ("China's Climate Role","Largest global emitter (~30% of CO₂) but also the world's largest investor in renewable energy."),
     ("Carbon Border Adjustment","Tax on imports from countries with weaker climate policies to prevent 'carbon leakage' (EU CBAM)."),
     ("Subnational Climate Action","Climate policies by states, cities, and regions — often more ambitious than national governments.")],
    [("The EU ETS is the world's largest:",["Carbon tax","*Cap-and-trade carbon market (covering ~40% of EU emissions since 2005)","Renewable energy program","Nuclear program"],"Market leader."),
     ("The EU ETS has reduced covered emissions by approximately _____ since 2005.",["5%","*~35%","75%","0%"],"Significant reduction."),
     ("An early challenge for the EU ETS was:",["Too few allowances","*Over-allocation of free allowances, which kept carbon prices too low to drive significant change","It was too expensive","No one participated"],"Price collapse."),
     ("California has set a goal of _____ clean electricity by 2045.",["50%","75%","*100%","25%"],"Ambitious state target."),
     ("California's climate policy is significant because it:",["Only affects one state","*Demonstrates that aggressive climate action and economic growth can coexist (5th largest economy globally)","Has failed","Mimics federal policy"],"Proving ground."),
     ("China emits approximately _____ of global CO₂.",["10%","*~30% (the largest single country emitter)","50%","5%"],"Dominant emitter."),
     ("Despite being the largest emitter, China leads in:",["Only coal","*Renewable energy investment and deployment (largest solar, wind, and EV capacity globally)","Only nuclear","Only hydropower"],"Dual identity."),
     ("China launched the world's largest ETS in 2021 covering:",["All sectors","*The power sector initially (then expanding to other sectors)","Only transportation","Only buildings"],"Phased approach."),
     ("Carbon leakage occurs when:",["Carbon is lost from soil","*Industries relocate to countries with weaker climate policies to avoid carbon costs","Carbon disappears","Carbon is captured"],"Policy evasion."),
     ("The EU's Carbon Border Adjustment Mechanism (CBAM) addresses leakage by:",["Banning imports","*Taxing imports based on their carbon content — equalizing costs for domestic and foreign producers","Only subsidizing exports","Ignoring the issue"],"Border carbon tax."),
     ("India's International Solar Alliance promotes:",["Only Indian solar","*Global cooperation to mobilize investment in solar energy, especially in developing countries","Only fossil fuels","Only nuclear"],"South-South cooperation."),
     ("The UK's Climate Change Act (2008) was significant because it:",["Had no targets","*Legally mandated 80% emission reduction by 2050 (later amended to net-zero), with five-year carbon budgets","Only advisory","Only covered energy"],"Legally binding domestic law."),
     ("Cities signing the C40 coalition pledge to:",["Ignore climate change","*Meet the most ambitious goals of the Paris Agreement through urban climate action","Only count emissions","Only adapt"],"City-level commitment."),
     ("New Zealand included _____ in its ETS, a first for any country.",["Only energy","*Agricultural emissions (including methane from livestock)","Only transport","Only industry"],"Comprehensive coverage."),
     ("Costa Rica aims to be carbon-neutral by:",["2100","*2050 (with a plan centered on renewable electricity, reforestation, and green transport)","2030","Never"],"National ambition."),
     ("The effectiveness of climate policy depends most on:",["Good intentions","*Implementation, enforcement, adequate ambition, and political will to maintain long-term commitments","Only technology","Only money"],"Actions, not promises."),
     ("Fossil fuel subsidy reform is critical because:",["Subsidies are small","*Global fossil fuel subsidies ($7+ trillion/year including externalities) undermine climate policy by making dirty energy artificially cheap","Subsidies help the climate","Reform is impossible"],"Perverse incentives."),
     ("These case studies demonstrate that:",["Only one approach works","*Multiple policy approaches (carbon pricing, regulations, investment, cooperation) are needed at all levels","Only international action matters","Only national action matters"],"Multi-level action."),
     ("For AP, climate policy questions test ability to:",["Only name agreements","*Evaluate policy effectiveness, compare approaches, analyze trade-offs, and connect policies to emission outcomes","Only list countries","Only cite dates"],"Policy analysis."),
     ("The key takeaway from climate policy case studies is:",["Policies don't matter","*Policy design matters enormously — ambition, enforcement, coverage, and equity determine whether agreements translate to real emission reductions","Only price matters","Only technology matters"],"Quality of design.")]
)
lessons[k]=v

# 7.7
k,v = build_lesson(7,7,"AP Prep: Climate Models",
    "<h3>AP Prep: Climate Models</h3>"
    "<h4>Key Concepts</h4>"
    "<ul><li><b>Climate models (GCMs):</b> Computer simulations of Earth's climate system using physics equations. Multiple models run for different emission scenarios.</li>"
    "<li><b>Emission scenarios (RCPs/SSPs):</b> RCP 2.6 (aggressive mitigation) to RCP 8.5 (business as usual). SSPs update these.</li>"
    "<li><b>Model outputs:</b> Temperature projections range from +1.5°C to +4.5°C+ by 2100 depending on emissions.</li>"
    "<li><b>Carbon budget:</b> Total CO₂ that can still be emitted to stay below a temperature target (~400 Gt CO₂ remaining for 1.5°C).</li></ul>",
    [("General Circulation Model (GCM)","Computer simulation of Earth's climate system using physical equations for atmosphere, ocean, land, and ice."),
     ("RCP (Representative Concentration Pathway)","Scenarios of future greenhouse gas concentrations used in climate modeling: 2.6 (low) to 8.5 (high)."),
     ("SSP (Shared Socioeconomic Pathway)","Updated scenarios combining socioeconomic development with emission pathways for climate projections."),
     ("Climate Sensitivity","Temperature increase expected from doubling atmospheric CO₂; estimated 2.5–4.0°C."),
     ("Carbon Budget","Total remaining CO₂ emissions allowed to stay below a specific temperature target.")],
    [("Climate models (GCMs) simulate Earth's climate using:",["Guessing","*Physical equations governing atmosphere, ocean, land surface, and ice interactions","Only one equation","Only temperature data"],"Physics-based simulation."),
     ("RCP 2.6 represents a scenario with:",["No action","*Aggressive mitigation — emissions peak soon and decline, limiting warming to ~1.5-2°C by 2100","Business as usual","Only one country acting"],"Best-case pathway."),
     ("RCP 8.5 represents:",["Aggressive mitigation","*Business as usual (high emissions continue, leading to ~4-5°C+ warming by 2100)","Moderate action","Carbon neutrality"],"Worst-case pathway."),
     ("Temperature projections for 2100 range from:",["0–0.5°C","*+1.5°C to +4.5°C+ above pre-industrial (depending on emission scenario)","Only +2°C exactly","No change"],"Wide range based on choices."),
     ("Climate sensitivity is defined as the warming from:",["Any CO₂ increase","*Doubling of atmospheric CO₂ concentration (from 280 to 560 ppm); estimated at 2.5–4.0°C","Halving CO₂","Triple CO₂"],"Fundamental parameter."),
     ("The remaining carbon budget for 1.5°C is approximately:",["Unlimited","*~400 Gt CO₂ (at current emission rates, ~10 years' worth)","1,000 Gt","Already exhausted"],"Rapidly shrinking."),
     ("At current emission rates (~40 Gt CO₂/year), the 1.5°C budget runs out in about:",["50 years","*~10 years","100 years","1 year"],"Urgent deadline."),
     ("Climate models are validated by:",["Guessing","*Comparing model predictions against observed historical climate data (hindcasting)","Only one test","Never validated"],"Tested against reality."),
     ("Climate models have accurately predicted:",["Nothing","*Global temperature trends since the 1970s; models from the 1990s align well with observed warming","Only cooling","Only one variable"],"Track record."),
     ("Uncertainty in climate models comes from:",["Models being wrong","*Unknown future emissions, natural variability, and incomplete understanding of some feedback mechanisms","Only computer limitations","Having too little data"],"Multiple sources."),
     ("SSPs (Shared Socioeconomic Pathways) differ from RCPs by including:",["Only emissions","*Socioeconomic factors (population, GDP, governance, technology) that affect both emissions and adaptive capacity","Only temperature","Only one scenario"],"More comprehensive."),
     ("Positive feedback in climate models amplifies warming through:",["Cooling only","*Ice-albedo feedback, water vapor amplification, permafrost methane release, and cloud changes","Only one mechanism","No feedbacks exist"],"Amplification loops."),
     ("Tipping points in models represent:",["Gradual change","*Thresholds where small additional warming triggers large, irreversible changes (ice sheet collapse, Amazon dieback)","No change","Only local effects"],"Non-linear responses."),
     ("The IPCC uses _____ models from research groups worldwide to improve reliability.",["1","5","*Dozens of independent models (ensemble approach reduces uncertainty)","100"],"Multi-model consensus."),
     ("Downscaling refers to:",["Making models smaller","*Converting global model outputs to regional/local scale projections (necessary for local adaptation planning)","Reducing accuracy","Only simplifying"],"Local relevance."),
     ("Net-zero emissions means:",["No emissions at all","*Emissions produced are balanced by an equal amount of CO₂ removal (net effect = zero addition to atmosphere)","Only reducing slightly","Only for CO₂"],"Balance, not elimination."),
     ("To stay below 1.5°C, global emissions must reach net-zero by approximately:",["2100","*~2050 (with significant reductions starting immediately)","2080","2030 completely"],"Tight timeline."),
     ("Climate models show that even with aggressive mitigation:",["No warming occurs","*Some additional warming is locked in due to past emissions and heat already in the ocean (adaptation will be needed regardless)","Cooling happens","Temperature drops instantly"],"Committed warming."),
     ("For AP FRQ involving climate models, students should:",["Only describe scenarios","*Interpret model outputs, compare scenarios, explain uncertainty, and connect projections to policy decisions","Only list numbers","Only draw graphs"],"Analytical skills."),
     ("Understanding climate models is essential because they:",["Are just academic","*Provide the scientific basis for policy decisions affecting 8 billion people and every ecosystem on Earth","Only for scientists","Don't matter for policy"],"Foundation of action.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 7: wrote {len(lessons)} lessons")
