#!/usr/bin/env python3
"""Integrated Science Unit 3 – Hydrosphere (9 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "integrated_science_lessons.json")
COURSE = "Integrated Science"

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
k,v = build_lesson(3,1,"Hydrologic Cycle (Evaporation, Condensation, Precipitation)",
    "<h3>The Hydrologic (Water) Cycle</h3>"
    "<h4>Key Processes</h4>"
    "<ul><li><b>Evaporation:</b> Liquid water → water vapor (solar energy driven). Transpiration adds plant water.</li>"
    "<li><b>Condensation:</b> Water vapor → liquid droplets (forms clouds when air cools to dew point).</li>"
    "<li><b>Precipitation:</b> Water falls as rain, snow, sleet, or hail when cloud droplets grow large enough.</li>"
    "<li><b>Infiltration:</b> Water soaks into soil and rock, recharging groundwater.</li>"
    "<li><b>Runoff:</b> Water flows over the surface into streams, rivers, lakes, and oceans.</li></ul>"
    "<h4>Water Budget</h4>"
    "<p>Earth's water is constant — the cycle redistributes it. ~97.5% salt water, ~2.5% fresh (most locked in ice).</p>",
    [("Evaporation","Conversion of liquid water to water vapor using solar energy; primary input of water to the atmosphere."),
     ("Transpiration","Release of water vapor from plant leaves; combined with evaporation as evapotranspiration."),
     ("Condensation","Conversion of water vapor to liquid droplets; occurs when air cools to its dew point; forms clouds."),
     ("Infiltration","Process by which water soaks into soil and rock, replenishing groundwater supplies."),
     ("Water Table","The upper surface of the zone of saturation where all pore spaces in rock/soil are filled with water.")],
    [("The primary energy source driving the water cycle is:",["Gravity","Wind","*The Sun (solar radiation provides energy for evaporation)","Earth's core"],"Solar driver."),
     ("Approximately _____ of Earth's water is fresh water.",["50%","10%","*~2.5%","0.5%"],"Fresh water fraction."),
     ("Most of Earth's fresh water is stored in:",["Rivers and lakes","The atmosphere","*Glaciers and ice caps (~69% of fresh water)","Groundwater"],"Ice storage."),
     ("Transpiration is water released by:",["Oceans","Rocks","*Plants (through stomata in leaves)","Animals"],"Transpiration."),
     ("Evapotranspiration is greatest in regions with:",["Cold temperatures and cloud cover","*High temperatures, lots of vegetation, and abundant water","Low humidity only","No plants"],"High ET."),
     ("The dew point is the temperature at which:",["Water boils","Ice melts","*Air becomes saturated and water vapor condenses","Rain stops"],"Dew point."),
     ("Infiltration rate is highest in:",["Clay soils","Paved surfaces","*Sandy soils (large pore spaces allow water to pass through quickly)","Frozen ground"],"Infiltration rate."),
     ("Runoff increases when:",["Soil is dry and porous","Vegetation is dense","*Surfaces are impervious (pavement), soil is saturated, or precipitation exceeds infiltration capacity","Evaporation is high"],"Runoff factors."),
     ("Groundwater is stored in _____, which are underground layers of permeable rock.",["Caves only","*Aquifers","Rivers","Clouds"],"Aquifers."),
     ("The water table can be lowered by:",["Rainfall","*Excessive pumping (withdrawing groundwater faster than it recharges)","Evaporation only","Planting trees"],"Water table decline."),
     ("An artesian well occurs when:",["Water is pumped uphill","*Groundwater is under pressure between impermeable layers and rises naturally when a well is drilled","A spring dries up","Rain fills a hole"],"Artesian wells."),
     ("Watersheds (drainage basins) are defined by:",["Political boundaries","*Topographic divides — all water within the area drains to a common outlet (river/lake/ocean)","Random selection","Rainfall amounts"],"Watershed."),
     ("Urbanization affects the water cycle by:",["Increasing infiltration","*Increasing runoff and decreasing infiltration (impervious surfaces prevent water from soaking in)","Increasing groundwater","Having no effect"],"Urban hydrology."),
     ("The residence time of water in the atmosphere is approximately:",["1 year","*~9-10 days (water cycles rapidly through the atmosphere)","100 days","1 day"],"Atmospheric residence."),
     ("Permeability describes a material's ability to:",["Hold water","Reflect water","*Allow water to flow through it (dependent on pore connectivity)","Dissolve in water"],"Permeability."),
     ("Porosity measures the _____ space in soil or rock.",["Solid","*Pore (empty space that can hold water or air)","Total","Crystal"],"Porosity."),
     ("Springs occur where:",["Water evaporates","*The water table intersects the ground surface, allowing groundwater to flow out naturally","Runoff stops","Clouds form"],"Springs."),
     ("Climate change affects the water cycle by:",["Having no effect","*Intensifying evaporation, altering precipitation patterns, and changing snowmelt timing","Stopping evaporation","Creating new water"],"Climate-water link."),
     ("The concept of 'virtual water' refers to:",["Imaginary water","*The total water used in producing a product (e.g., ~2,500 liters to produce 1 kg of beef)","Desalinated water","Recycled water"],"Virtual water."),
     ("Understanding the water cycle is critical because:",["Water is unimportant","*It governs water availability for drinking, agriculture, ecosystems, and industry — and climate change is altering it","Only for scientists","Only for farmers"],"Water cycle importance.")]
)
lessons[k]=v

# 3.2
k,v = build_lesson(3,2,"Oceans (Currents, Salinity, Temperature Layers)",
    "<h3>Ocean Properties</h3>"
    "<h4>Salinity</h4>"
    "<ul><li>Average ocean salinity ~35 ppt (parts per thousand). Higher near evaporative regions, lower near river mouths and rain.</li></ul>"
    "<h4>Temperature Layers</h4>"
    "<ul><li><b>Surface (mixed) layer:</b> Warm, well-mixed by waves and wind (0-200 m).</li>"
    "<li><b>Thermocline:</b> Rapid temperature decrease with depth (200-1,000 m).</li>"
    "<li><b>Deep ocean:</b> Cold and nearly uniform (~1-4°C) below 1,000 m.</li></ul>"
    "<h4>Currents</h4>"
    "<ul><li><b>Surface currents:</b> Wind-driven; form gyres (clockwise NH, counterclockwise SH).</li>"
    "<li><b>Deep currents:</b> Thermohaline circulation driven by density differences (temperature + salinity).</li></ul>",
    [("Salinity","Concentration of dissolved salts in seawater; average ~35 ppt; affects density and freezing point."),
     ("Thermocline","Layer of rapid temperature decrease with depth between the warm surface and cold deep ocean."),
     ("Surface Current","Wind-driven horizontal movement of surface ocean water; forms large circular gyres."),
     ("Thermohaline Circulation","Global deep ocean circulation driven by differences in water density from temperature and salinity."),
     ("Gyre","Large circular surface current system; five major gyres driven by winds and the Coriolis effect.")],
    [("Average ocean salinity is approximately:",["3.5%","*35 ppt (parts per thousand, or 3.5%)","350 ppt","0.35 ppt"],"Ocean salinity."),
     ("The ocean thermocline is the layer where:",["Temperature is constant","Temperature increases rapidly","*Temperature decreases rapidly with depth (between 200-1,000 m)","Salinity changes most"],"Thermocline."),
     ("Deep ocean water is typically _____ °C.",["10-15","*1-4","20-25","Below 0"],"Deep temperature."),
     ("Surface ocean currents are driven primarily by:",["Tides","Earth's rotation alone","*Wind (modified by continents and the Coriolis effect)","Temperature only"],"Current driver."),
     ("In the Northern Hemisphere, ocean gyres rotate:",["Counterclockwise","Randomly","*Clockwise (due to the Coriolis deflection)","North to south"],"NH gyre."),
     ("The Gulf Stream is a _____ current that carries _____ water.",["Cold; polar","*Warm; warm water from the Gulf of Mexico toward Western Europe","Slow; deep","Surface; cold"],"Gulf Stream."),
     ("Thermohaline circulation is driven by:",["Wind alone","Tides alone","*Density differences caused by temperature and salinity variations (cold, salty water is densest and sinks)","Waves"],"Thermohaline driver."),
     ("Upwelling occurs when:",["Surface water sinks","Wind pushes water against the coast","*Wind or currents move surface water away, and cold, nutrient-rich water rises to replace it","Deep water freezes"],"Upwelling."),
     ("Upwelling zones are biologically productive because:",["They're warm","*Rising deep water brings nutrients to the surface, supporting plankton growth and entire food chains","They're shallow","They have no currents"],"Upwelling productivity."),
     ("El Niño suppresses upwelling along the South American coast, which:",["Increases fish catches","*Decreases fish catches (less nutrients at surface = less plankton = fewer fish)","Has no effect on fish","Only affects temperature"],"El Niño upwelling."),
     ("Salinity is highest in _____ regions where evaporation exceeds precipitation.",["Polar","Equatorial","*Subtropical (around 25-30° latitude — dry, high pressure zones)","All regions equally"],"High salinity zones."),
     ("The ocean absorbs approximately _____ of the heat added to Earth's climate system.",["10%","50%","*~90%","99%"],"Ocean heat absorption."),
     ("This heat absorption by the ocean causes:",["No effects","*Thermal expansion (sea level rise), coral bleaching, altered currents, and delayed surface warming","Cooling of the ocean","Only surface effects"],"Heat consequences."),
     ("Ocean acidification is caused by:",["Acid rain only","*Absorption of excess atmospheric CO₂, which reacts with water to form carbonic acid (lowering pH)","Volcanic eruptions","Industrial waste"],"Acidification cause."),
     ("Ocean acidification threatens _____ organisms.",["No","Only fish","*Shell-building organisms (corals, mollusks, plankton — carbonic acid dissolves calcium carbonate shells)","Only deep-sea"],"Acidification impact."),
     ("The Coriolis effect deflects ocean currents _____ in the Southern Hemisphere.",["Right","*Left","Straight","Not at all"],"SH Coriolis."),
     ("Ekman transport causes surface water to move at an angle _____ to the wind direction.",["Parallel","Opposite","*~90° (to the right in NH, left in SH — due to Coriolis effect on successive water layers)","45°"],"Ekman spiral."),
     ("Phytoplankton produce approximately _____ of Earth's oxygen through photosynthesis.",["10%","*~50%","75%","100%"],"Phytoplankton oxygen."),
     ("The deepest point in the ocean is the Mariana Trench at approximately:",["5,000 m","8,000 m","*~11,000 m (deeper than Mt. Everest is tall)","15,000 m"],"Deepest point."),
     ("Studying the oceans is crucial because they:",["Only affect coastal areas","*Regulate climate, produce oxygen, support food chains, absorb CO₂, and cover 71% of Earth's surface","Are fully explored","Don't interact with land"],"Ocean importance.")]
)
lessons[k]=v

# 3.3
k,v = build_lesson(3,3,"Waves & Tides (Causes, Effects)",
    "<h3>Waves & Tides</h3>"
    "<h4>Waves</h4>"
    "<ul><li>Generated primarily by wind. Wave height depends on wind speed, duration, and fetch.</li>"
    "<li>Waves transport energy, not water — water moves in circular orbits.</li>"
    "<li>Waves break when depth becomes less than half the wavelength.</li></ul>"
    "<h4>Tides</h4>"
    "<ul><li><b>Caused by:</b> Gravitational pull of the Moon (primary) and Sun.</li>"
    "<li><b>Spring tides:</b> Sun and Moon aligned → highest highs, lowest lows.</li>"
    "<li><b>Neap tides:</b> Sun and Moon at 90° → smaller tidal range.</li></ul>",
    [("Wave","A disturbance that transfers energy through water; caused primarily by wind; water particles move in orbits."),
     ("Fetch","The distance over open water that wind blows in a constant direction; longer fetch = larger waves."),
     ("Spring Tide","Highest tidal range when Sun, Moon, and Earth align (new and full moon); gravitational forces combine."),
     ("Neap Tide","Lowest tidal range when Sun and Moon are at right angles (quarter moons); gravitational forces partially cancel."),
     ("Longshore Current","Current flowing parallel to the shore created by waves approaching at an angle; transports sediment along the coast.")],
    [("Ocean waves are generated primarily by:",["Earthquakes","*Wind (blowing across the water surface transfers energy)","The Moon","Underwater volcanoes"],"Wave generation."),
     ("As a wave passes, water particles actually move in:",["Straight lines forward","*Circular orbits (energy moves forward, not the water itself — a floating object bobs, doesn't travel)","Straight lines backward","Triangular paths"],"Water particle motion."),
     ("Wave height is determined by wind speed, wind duration, and:",["Water temperature","Salinity","*Fetch (the distance of open water the wind blows across)","The Moon"],"Wave height factors."),
     ("Waves break when they enter water shallower than _____ their wavelength.",["Equal to","*Approximately half (wave base — the circular orbits interact with the bottom and topple)","Double","One quarter"],"Wave breaking."),
     ("Tides are caused primarily by the gravitational pull of the:",["Sun only","Earth's core","*Moon (with additional influence from the Sun)","Planets"],"Tide cause."),
     ("Most coastlines experience _____ high tides per day.",["One","*Two (semidiurnal — due to the bulge on both the side facing the Moon and the opposite side)","Three","Four"],"Tidal frequency."),
     ("Spring tides occur during:",["Only spring season","First quarter Moon","*New Moon and Full Moon (Sun, Moon, Earth aligned — combined gravitational pull)","Only summer"],"Spring tide timing."),
     ("Neap tides have a _____ tidal range than spring tides.",["Larger","*Smaller (Sun and Moon at right angles — gravitational forces partially cancel)","Same","Variable"],"Neap range."),
     ("The Bay of Fundy has the world's largest tidal range (~16 m) because of its:",["Latitude","Temperature","*Funnel shape that amplifies tidal water (resonance effect)","Depth"],"Bay of Fundy."),
     ("Tsunami waves are caused by _____ rather than wind.",["Tides","*Undersea earthquakes, volcanic eruptions, or landslides displacing water","Storms","Currents"],"Tsunami cause."),
     ("Tsunami waves in the open ocean are _____ but move extremely fast.",["Very tall","*Low in height (often <1 m) but can travel 700+ km/h — they build up as they reach shallow coastal water","Slow","Circular"],"Tsunami open ocean."),
     ("Longshore drift transports _____ along the coast.",["Water only","Heat","*Sediment (sand) in the direction of the longshore current","Fish"],"Longshore drift."),
     ("Rip currents are:",["Tidal currents","*Narrow, fast-moving channels of water flowing seaward through the surf zone — dangerous for swimmers","Always visible","Slow currents"],"Rip currents."),
     ("If caught in a rip current, you should:",["Swim directly toward shore","Panic and fight the current","*Swim parallel to shore until out of the current, then swim back","Dive underwater"],"Rip safety."),
     ("Wave refraction occurs when:",["Waves speed up in shallow water","*Waves bend as they encounter different depths (part of the wave slows in shallows while the rest is still in deeper water)","Waves reflect off cliffs","Waves stop"],"Wave refraction."),
     ("Erosion from waves is most intense on:",["Flat beaches","*Headlands (rocky points that jut out into the ocean — waves focus energy there through refraction)","Bays","Deep water"],"Wave erosion."),
     ("Sea stacks, arches, and sea caves are formed by:",["Deposition","*Wave erosion of headlands over time","River action","Wind erosion"],"Coastal erosion features."),
     ("Tidal energy can be harnessed for renewable electricity by:",["Blocking all tides","*Using tidal barrages or underwater turbines to capture the kinetic energy of tidal water movement","Heating water","Only in theory"],"Tidal energy."),
     ("Storm surge is particularly dangerous during _____ tides.",["Neap","*Spring (already highest tides + storm surge = maximum flooding potential)","Low","Any equally"],"Surge timing."),
     ("Understanding waves and tides is important for:",["Only surfers","*Coastal engineering, navigation, fishing, coastal development, erosion management, and public safety","Only scientists","Only the military"],"Practical applications.")]
)
lessons[k]=v

# 3.4
k,v = build_lesson(3,4,"Freshwater Systems (Rivers, Lakes, Aquifers)",
    "<h3>Freshwater Systems</h3>"
    "<h4>Rivers & Streams</h4>"
    "<ul><li>Drainage networks from headwaters to mouth. Shaped by gradient, discharge, and load.</li>"
    "<li>Meanders form on gently sloping terrain; V-shaped valleys in steep terrain.</li></ul>"
    "<h4>Lakes</h4>"
    "<ul><li>Formed by glaciers, tectonics, volcanic activity, or river/dam processes.</li>"
    "<li>Stratified in summer: warm epilimnion, thermocline, cold hypolimnion.</li></ul>"
    "<h4>Groundwater</h4>"
    "<ul><li>Stored in aquifers — porous rock below the water table. Ogallala Aquifer supplies ~30% of US irrigation.</li></ul>",
    [("Watershed","Area of land where all precipitation drains to a common outlet (river, lake, or ocean); defined by topographic divides."),
     ("Meander","A pronounced curve or loop in a river channel formed as the river erodes its outer bank and deposits on the inner bank."),
     ("Aquifer","Underground layer of permeable rock or sediment that stores and transmits groundwater."),
     ("Floodplain","Flat area adjacent to a river that is periodically inundated during high water; built from deposited sediment."),
     ("Lake Stratification","Layering of a lake by temperature: warm surface (epilimnion), transition zone (thermocline), cold bottom (hypolimnion).")],
    [("A watershed is defined as:",["A building for water","*All land area that drains to a common outlet (every point on land is in a watershed)","A man-made dam","An underground reservoir"],"Watershed def."),
     ("River discharge is measured as:",["Speed only","Width only","*Volume of water passing a point per unit time (cubic meters per second, m³/s)","Depth only"],"Discharge."),
     ("Meanders are most likely to form where:",["Slopes are steep","Rocks are hard","*The gradient is gentle and the river flows through soft sediment","Rivers begin"],"Meander formation."),
     ("An oxbow lake forms when:",["A dam is built","*A meander loop is cut off from the main river channel (the river breaches the narrow neck between loops)","A glacier melts","A spring emerges"],"Oxbow lake."),
     ("Floodplains are created by:",["Erosion only","*Repeated flooding depositing sediment on either side of the river channel over time","Volcanic activity","Human construction"],"Floodplain formation."),
     ("The largest freshwater reservoir on Earth is:",["Rivers","Lakes","*Ice caps and glaciers (~69% of fresh water)","Groundwater"],"Largest reservoir."),
     ("The Ogallala Aquifer, which is being depleted faster than it recharges, supplies:",["10% of US drinking water","*~30% of US agricultural irrigation water","50% of world water","All East Coast water"],"Ogallala."),
     ("An unconfined aquifer has its water table in direct contact with the:",["Bedrock","*Unsaturated zone above (can be recharged directly by infiltration from the surface)","Confined layer","Ocean"],"Unconfined aquifer."),
     ("A confined aquifer is trapped between:",["River banks","*Impermeable layers (confining beds) above and below — water is under pressure","Mountains","Sand layers only"],"Confined aquifer."),
     ("Lake turnover occurs in temperate lakes when:",["Fish migrate","*Surface water cools to the same density as deeper water, allowing complete mixing (bringing nutrients from the bottom)","Wind stops","Ice melts only"],"Lake turnover."),
     ("Eutrophication is the process by which a lake:",["Gets deeper","Loses all water","*Becomes nutrient-enriched (often from agricultural runoff), leading to algal blooms, oxygen depletion, and ecological decline","Becomes saltier"],"Eutrophication."),
     ("Rivers transport sediment as:",["Only dissolved load","*Dissolved load, suspended load, and bed load (rolling/bouncing along the bottom)","Only bed load","Only surface material"],"Sediment transport."),
     ("A delta forms where:",["A river begins","*A river enters a standing body of water (lake or ocean) and deposits its sediment load as flow slows","Groundwater emerges","Rain falls heavily"],"Delta formation."),
     ("An alluvial fan forms where:",["Rivers enter oceans","*A steep mountain stream enters a flat plain (sudden decrease in gradient causes deposition)","Glaciers melt","Lakes overflow"],"Alluvial fan."),
     ("Groundwater contamination is particularly concerning because:",["It's easy to clean","*Aquifers are very slow to flush — contamination can persist for decades or centuries","It doesn't affect drinking water","It's always visible"],"Contamination persistence."),
     ("Levees (natural or artificial) along rivers:",["Prevent all flooding","*Confine the river to its channel, but can worsen flooding downstream and catastrophically fail","Have no effect","Create new rivers"],"Levees."),
     ("Wetlands provide ecosystem services including:",["Only wildlife habitat","*Water filtration, flood control, carbon storage, groundwater recharge, and biodiversity habitat","Only recreation","Nothing valuable"],"Wetland services."),
     ("The water budget equation for a watershed is:",["Input = Output","*P (precipitation) = ET (evapotranspiration) + Q (runoff) + ΔS (change in storage)","Only rainfall matters","Water is unlimited"],"Water budget."),
     ("Karst topography (sinkholes, caves) forms in regions with:",["Granite bedrock","*Soluble rock like limestone (groundwater dissolves the rock over time, creating underground cavities)","Sandy soil","Volcanic rock"],"Karst."),
     ("Managing freshwater resources sustainably requires:",["Unlimited pumping","*Balancing withdrawal with recharge, reducing pollution, conserving water, and protecting watersheds","No regulation","Only building dams"],"Sustainable management.")]
)
lessons[k]=v

# 3.5
k,v = build_lesson(3,5,"Glaciers & Ice Caps (Formation, Melting Impacts)",
    "<h3>Glaciers & Ice Caps</h3>"
    "<h4>Formation & Types</h4>"
    "<ul><li>Glaciers form when snow accumulates faster than it melts, compressing into ice over years.</li>"
    "<li><b>Alpine (valley):</b> Flow down mountain valleys.</li>"
    "<li><b>Continental (ice sheets):</b> Cover vast areas (Greenland, Antarctica).</li></ul>"
    "<h4>Glacial Features</h4>"
    "<ul><li>Erosion: cirques, U-shaped valleys, horns, arêtes.</li>"
    "<li>Deposition: moraines, drumlins, erratics, outwash plains.</li></ul>"
    "<h4>Climate Implications</h4>"
    "<ul><li>If all ice melted, sea level would rise ~65-70 meters. Current rate: ~3.5 mm/year sea level rise.</li></ul>",
    [("Glacier","A persistent body of ice formed from compacted snow that moves under its own weight; stores ~69% of Earth's fresh water."),
     ("Ice Sheet","Continental-scale glacier covering >50,000 km²; only two exist today: Greenland and Antarctica."),
     ("Moraine","Accumulation of glacial sediment (till) deposited at the edges, bottom, or terminus of a glacier."),
     ("U-Shaped Valley","A valley carved by glacial erosion, wider and flatter-bottomed than the V-shaped valleys carved by rivers."),
     ("Glacial Retreat","When a glacier's terminus melts back because melting exceeds accumulation; accelerating globally due to climate change.")],
    [("Glaciers form when annual snowfall _____ annual snowmelt over many years.",["Equals","*Exceeds (accumulated snow compresses into firn, then glacial ice)","Is less than","Has nothing to do with"],"Glacier formation."),
     ("The Antarctic ice sheet contains enough ice to raise sea level by approximately:",["5 m","20 m","*~58 m (if fully melted — contains ~26.5 million km³ of ice)","100 m"],"Antarctic ice volume."),
     ("Glaciers move by:",["Wind","*Internal deformation (ice flow) and basal sliding (sliding over meltwater at the base)","Plate tectonics","Tides"],"Glacial movement."),
     ("A cirque is a glacial erosion feature shaped like a:",["V","U","*Bowl or amphitheater (carved into a mountainside at the head of a glacier)","Flat plain"],"Cirque."),
     ("A horn (like the Matterhorn) forms when:",["A volcano erupts","*Multiple cirques erode a mountain from several sides, leaving a sharp pyramidal peak","Wind erosion occurs","Rivers converge"],"Horn formation."),
     ("Glacial erratics are:",["Normal rocks","*Large boulders transported and deposited by glaciers far from their source — often strikingly different from local rock","Volcanic bombs","Sedimentary layers"],"Erratics."),
     ("U-shaped valleys indicate past _____ erosion, while V-shaped valleys indicate _____ erosion.",["River; glacial","*Glacial; river","Wind; water","No; much"],"Valley shapes."),
     ("Since 1900, global sea level has risen approximately:",["0 cm","5 cm","*~20 cm (accelerating — currently ~3.5 mm/year)","1 m"],"Sea level rise."),
     ("Sea level rise comes from two main sources:",["Only glaciers","Only thermal expansion","*Thermal expansion of warming water AND melting of land-based ice (glaciers and ice sheets)","Only rainfall"],"SLR sources."),
     ("Greenland's ice sheet has been losing mass at an accelerating rate, contributing:",["Nothing to sea level","*Approximately 0.7 mm/year to sea level rise (and increasing)","Only local effects","Cooling to the globe"],"Greenland melt."),
     ("The ice-albedo feedback means that melting ice _____ further warming.",["Slows","*Accelerates (exposed dark land/ocean absorbs more sunlight → more warming → more melting — positive feedback)","Stops","Has no effect on"],"Positive feedback."),
     ("During the last Ice Age (~20,000 years ago), sea level was approximately _____ lower than today.",["10 m","50 m","*~120 m (massive ice sheets locked up water on land)","200 m"],"Ice Age sea level."),
     ("Glacial till is _____ sediment.",["Sorted and layered","*Unsorted, mixed-size (glaciers deposit everything together, unlike water which sorts by size)","Only sand","Only clay"],"Till character."),
     ("An outwash plain forms from:",["Glacial erosion","*Meltwater streams depositing sorted sediment beyond the glacier's terminus","Wind deposition","Volcanic ash"],"Outwash."),
     ("Fjords are:",["River valleys","*Deep, narrow inlets carved by glaciers and flooded by the sea (common in Norway, Alaska, New Zealand)","Volcanic craters","Lake shores"],"Fjords."),
     ("Kettle lakes form when:",["Rivers flood","*Blocks of glacial ice buried in sediment melt, leaving a depression that fills with water","Rain accumulates only","Springs emerge"],"Kettle lakes."),
     ("The Laurentide Ice Sheet covered much of _____ during the last glaciation.",["South America","Europe","*North America (extending to present-day New York, Ohio, and beyond)","Africa"],"Laurentide."),
     ("Isostatic rebound in Scandinavia and Canada occurs because:",["Earthquakes push land up","*The weight of ice sheets depressed the crust — removal of ice allows slow uplift (still rising today)","Volcanic activity","Erosion lightens the surface"],"Post-glacial rebound."),
     ("Glaciers are sometimes called 'rivers of ice' because they:",["Flow like rivers","*Move slowly downhill under gravity, eroding and transporting material — similar to rivers but over much longer timescales","Contain liquid water only","Are exactly like rivers"],"Glacial analogy."),
     ("The study of glaciers is critical today because:",["They're only historical interest","*They indicate climate change rate, affect global sea level, and are crucial freshwater sources for billions of people","Only mountaineers care","They don't affect humanity"],"Glaciology importance.")]
)
lessons[k]=v

# 3.6
k,v = build_lesson(3,6,"Water Resources & Human Use",
    "<h3>Water Resources & Human Use</h3>"
    "<h4>Water Use</h4>"
    "<ul><li>Agriculture (~70% global), Industry (~20%), Domestic (~10%).</li>"
    "<li>Water stress: using >25% of available renewable supply.</li></ul>"
    "<h4>Water Management</h4>"
    "<ul><li>Dams and reservoirs for storage and flood control.</li>"
    "<li>Desalination converting salt water to fresh.</li>"
    "<li>Water recycling and conservation strategies.</li></ul>",
    [("Water Stress","When a region uses more than 25% of its available renewable fresh water supply; affecting ~2 billion people."),
     ("Desalination","Removing salt from seawater to produce fresh water; energy-intensive but increasingly important in arid regions."),
     ("Virtual Water","The hidden water embedded in producing goods (e.g., ~15,000 liters to produce 1 kg of beef)."),
     ("Water Footprint","Total volume of fresh water used to produce goods and services consumed by an individual or community."),
     ("Irrigation Efficiency","Ratio of water used by crops to water applied; drip irrigation (~90%) vs. flood irrigation (~50%).")],
    [("The largest use of fresh water globally is:",["Industrial","Domestic","*Agriculture (~70% of global freshwater withdrawals)","Energy production"],"Agriculture dominance."),
     ("Water stress affects approximately _____ people worldwide.",["100 million","500 million","*~2 billion","5 billion"],"Water stress scale."),
     ("The most water-efficient irrigation method is:",["Flood irrigation","Sprinkler systems","*Drip irrigation (delivers water directly to plant roots with minimal waste, ~90% efficient)","Furrow irrigation"],"Drip efficiency."),
     ("Desalination is limited primarily by:",["Lack of salt water","Technology","*High energy cost (and brine waste disposal challenges)","Demand"],"Desalination limits."),
     ("Producing 1 kg of beef requires approximately:",["100 liters of water","1,000 liters","*~15,000 liters (including water for feed crops, drinking, and processing)","100,000 liters"],"Beef water footprint."),
     ("The Aral Sea shrank dramatically because:",["Climate change alone","Natural drought","*Diversion of rivers for cotton irrigation in Soviet era — one of the worst human-caused ecological disasters","Earthquake"],"Aral Sea."),
     ("Dam benefits include:",["Only hydropower","*Water storage, flood control, hydroelectric power, and recreation","Only flood control","No benefits"],"Dam benefits."),
     ("Dam drawbacks include:",["None","*Disrupted river ecosystems, blocked fish migration, sediment trapping, displaced communities, and downstream changes","Only cost","Only appearance"],"Dam drawbacks."),
     ("Groundwater depletion is occurring in many aquifers because:",["Recharge is too fast","*Withdrawal rates exceed natural recharge rates (some aquifers took thousands of years to fill)","Water is being created","Aquifers are growing"],"Depletion."),
     ("Land subsidence occurs when:",["Mountains grow","*Groundwater is pumped out, causing the ground above to compact and sink (irreversible in many cases)","Rivers flood","Glaciers advance"],"Subsidence."),
     ("Mexico City has sunk up to 9 meters in places due to:",["Earthquakes","*Excessive groundwater pumping from the aquifer beneath the city","Volcanic activity","Erosion"],"Mexico City subsidence."),
     ("Water recycling (reclaimed water) can be used for:",["Nothing","*Irrigation, industrial processes, toilet flushing, and (with advanced treatment) even drinking water","Only decoration","Only cooling"],"Reclaimed water."),
     ("The concept of 'water rights' is important in the western US because:",["There's too much water","*Water is scarce and legally allocated — disputes arise between agriculture, cities, recreation, and environmental needs","Rights are irrelevant","Only the federal government controls water"],"Water rights."),
     ("Rainwater harvesting involves:",["Making it rain","*Collecting and storing rainfall for later use (reduces demand on centralized supplies)","Only measuring rain","Preventing rain"],"Rainwater harvesting."),
     ("Xeriscaping is a landscaping approach that:",["Uses maximum water","*Uses drought-adapted plants to minimize irrigation needs (common in arid regions)","Requires fertilizers","Only uses grass"],"Xeriscaping."),
     ("Wetland preservation is important for water resources because wetlands:",["Waste water","*Filter pollutants, recharge groundwater, reduce flooding, and support biodiversity","Only house mosquitoes","Have no value"],"Wetland value."),
     ("The water-energy nexus refers to:",["Water creating energy only","*The interdependence of water and energy — producing energy requires water, and treating/transporting water requires energy","Energy replacing water","No connection"],"Water-energy."),
     ("Water conflicts between nations are:",["Impossible","*Real and increasing — approximately 260 river basins are shared between countries, creating potential for cooperation or conflict","Only historical","Only in deserts"],"Transboundary water."),
     ("Climate change affects water resources by:",["Having no effect","*Changing precipitation patterns, glacier melt timing, increasing drought/flood frequency, and reducing snowpack","Only increasing supply","Only affecting oceans"],"Climate-water."),
     ("Sustainable water management requires:",["Only building more dams","*Integrated approaches: conservation, efficiency, recycling, equitable allocation, ecosystem protection, and infrastructure investment","Only desalination","Unlimited pumping"],"Sustainability.")]
)
lessons[k]=v

# 3.7
k,v = build_lesson(3,7,"Water Pollution & Conservation",
    "<h3>Water Pollution & Conservation</h3>"
    "<h4>Types of Water Pollution</h4>"
    "<ul><li><b>Point source:</b> Identifiable origin (factory pipe, sewage outfall).</li>"
    "<li><b>Non-point source:</b> Diffuse origin (agricultural runoff, urban stormwater).</li>"
    "<li><b>Pollutant types:</b> Nutrients, pathogens, sediment, chemicals, thermal, plastic.</li></ul>"
    "<h4>Conservation Strategies</h4>"
    "<ul><li>Clean Water Act (1972 US), wastewater treatment, buffer zones, wetland protection.</li></ul>",
    [("Point Source Pollution","Pollution from an identifiable, localized source (e.g., factory discharge pipe, sewage treatment plant)."),
     ("Non-Point Source Pollution","Pollution from diffuse sources (agricultural runoff, urban stormwater); harder to control than point sources."),
     ("Eutrophication","Excess nutrient enrichment (nitrogen, phosphorus) causing algal blooms, oxygen depletion, and aquatic die-offs."),
     ("Biological Oxygen Demand (BOD)","Amount of oxygen consumed by microorganisms decomposing organic matter; high BOD indicates polluted water."),
     ("Riparian Buffer","Strip of vegetation along waterways that filters pollutants, reduces erosion, and provides habitat.")],
    [("Point source pollution comes from:",["Everywhere","*An identifiable, specific location (e.g., a factory discharge pipe or sewage outfall)","Only farms","Only natural sources"],"Point source."),
     ("Non-point source pollution is harder to control because:",["It's visible","*It comes from many diffuse sources across large areas (agricultural runoff, urban stormwater, atmospheric deposition)","It's natural","It's rare"],"NPS challenge."),
     ("The leading cause of water pollution in the US is:",["Industrial waste","Sewage","*Agricultural runoff (nutrients, pesticides, sediment, animal waste)","Mining"],"Leading cause."),
     ("Eutrophication results from excess _____ entering water bodies.",["Oxygen","Sediment","*Nutrients (nitrogen and phosphorus — causing algal blooms)","Salt"],"Eutrophication nutrients."),
     ("Dead zones (hypoxic areas) form when:",["Fish leave","*Decomposition of algal blooms consumes all dissolved oxygen — aquatic life suffocates","Water freezes","Currents stop"],"Dead zones."),
     ("The Gulf of Mexico dead zone is caused primarily by:",["Oil spills","*Nutrient runoff from the Mississippi River basin (primarily agricultural fertilizers)","Natural processes","Ships"],"Gulf dead zone."),
     ("Thermal pollution occurs when:",["Water freezes","*Heated water (e.g., from power plant cooling) is discharged into water bodies, reducing dissolved oxygen and harming aquatic life","Fires heat river water","It rains warm water"],"Thermal pollution."),
     ("Microplastics in water are concerning because they:",["Dissolve quickly","Are visible and removable","*Persist for centuries, absorb toxins, enter food chains, and are found in drinking water worldwide","Only affect oceans"],"Microplastics."),
     ("The US Clean Water Act (1972) significantly reduced _____ pollution.",["Non-point source","*Point source (regulation of industrial and municipal discharges — non-point source remains a major challenge)","All types equally","No pollution"],"CWA impact."),
     ("Wastewater treatment typically involves:",["Only filtration","*Primary (settling solids), secondary (biological decomposition), and sometimes tertiary (advanced chemical/filtration) treatment","Only chlorination","No treatment"],"Treatment stages."),
     ("Riparian buffers protect water quality by:",["Blocking all water","*Filtering runoff, trapping sediment and nutrients, stabilizing banks, and providing shade to cool stream temperature","Only providing shade","Nothing significant"],"Buffer benefit."),
     ("Groundwater contamination from PFAS (forever chemicals) is concerning because:",["PFAS break down quickly","*PFAS are extremely persistent (don't break down), accumulate in organisms, and are linked to health effects","They're natural","They only affect industry"],"PFAS."),
     ("The Safe Drinking Water Act regulates:",["Only bottled water","Only river water","*Public water supply systems (setting maximum contaminant levels for various pollutants)","Only groundwater"],"SDWA."),
     ("Lead in drinking water (Flint, Michigan crisis) came from:",["The river","Water treatment chemicals","*Corrosion of aging lead pipes when the water source was switched (inadequate corrosion control)","Natural sources"],"Flint crisis."),
     ("Constructed wetlands can treat wastewater by:",["Adding chemicals","*Using natural biological processes — plants, microbes, and substrate filter and break down pollutants","Heating water","Freezing pollutants"],"Constructed wetlands."),
     ("Ocean plastic pollution. Approximately _____ million tons of plastic enter the ocean annually.",["0.1","1","*~8-11 million","100"],"Ocean plastic."),
     ("Water quality is measured by parameters including:",["Only color","Only taste","*pH, dissolved oxygen, turbidity, BOD, nutrient levels, heavy metals, and pathogen counts","Only smell"],"Water quality measures."),
     ("Best management practices (BMPs) for agriculture include:",["Maximum fertilizer application","*Cover crops, no-till farming, buffer strips, precision fertilizer application, and controlled drainage","No farming","Only organic methods"],"Agricultural BMPs."),
     ("The cost of preventing water pollution is typically _____ than the cost of cleaning it up.",["Higher","The same","*Much lower (prevention is far more cost-effective than remediation)","Irrelevant"],"Prevention economics."),
     ("Every person can help reduce water pollution by:",["Doing nothing","*Properly disposing of chemicals, reducing lawn fertilizer, picking up pet waste, using less plastic, and supporting clean water policy","Only recycling","Only drinking less water"],"Individual actions.")]
)
lessons[k]=v

# 3.8
k,v = build_lesson(3,8,"Case Studies in Hydrology",
    "<h3>Case Studies in Hydrology</h3>"
    "<h4>The Colorado River</h4>"
    "<p>Supplies 40 million people; over-allocated by 1922 Colorado River Compact; Lake Mead at historic lows.</p>"
    "<h4>Bangladesh Flooding</h4>"
    "<p>Extremely flood-prone: flat delta, monsoon rains, snowmelt from Himalayas, sea level rise. Affects millions annually.</p>"
    "<h4>Ogallala Aquifer Depletion</h4>"
    "<p>Supplies 30% of US irrigation water; being depleted 3-100× faster than recharge in many areas.</p>",
    [("Colorado River Compact","1922 agreement dividing Colorado River water among 7 US states and Mexico; now over-allocated as supply declines."),
     ("Ogallala Aquifer","Massive aquifer under the US Great Plains; supplies ~30% of US irrigation water; being depleted far faster than recharge."),
     ("Bangladesh Flooding","Annual monsoon flooding in the Ganges-Brahmaputra delta; affects millions; worsened by climate change and sea level rise."),
     ("Over-Allocation","When legal water rights exceed actual available supply; creates conflict as water becomes scarcer."),
     ("Water Scarcity Solutions","Conservation, efficient irrigation, desalination, recycling, better allocation policy, and reducing demand.")],
    [("The Colorado River supplies water to approximately:",["5 million people","*~40 million people (across 7 US states, 2 Mexican states, and numerous Indigenous nations)","100 million people","1 million people"],"Colorado scale."),
     ("The Colorado River has not consistently reached the ocean since the _____ due to diversions.",["1880s","*1960s (almost all water is consumed before reaching the Gulf of California)","2000s","It still reaches the ocean"],"River depletion."),
     ("Lake Mead (Hoover Dam reservoir) has dropped to historic lows primarily because:",["The dam is broken","*Multi-year drought combined with over-allocation (demand exceeds supply in a warming climate)","Earthquakes","Only urban use"],"Lake Mead crisis."),
     ("The 1922 Colorado River Compact was based on:",["Average flow","Low flow estimates","*An unusually wet period — allocating more water than the river typically carries (systemic over-allocation)","Current conditions"],"Compact flaw."),
     ("The Ogallala Aquifer is being depleted _____ times faster than it recharges in many areas.",["2","10","*3-100 (some areas will be effectively exhausted within decades)","Equal recharge"],"Ogallala rate."),
     ("The Ogallala Aquifer was filled primarily during:",["Last century","Recent decades","*The last Ice Age (10,000+ years ago — it's essentially fossil water)","Yesterday"],"Aquifer age."),
     ("Bangladesh is extremely flood-prone because:",["It rains once","*It's a low-lying delta where three major rivers converge, receiving monsoon rain AND Himalayan snowmelt","It's a desert","It's mountainous"],"Bangladesh geography."),
     ("Climate change worsens Bangladesh flooding through:",["Only more rain","Only sea level rise","*More intense monsoon rainfall, accelerated Himalayan glacier melt, AND sea level rise (compound threats)","No mechanism"],"Compound threats."),
     ("The Three Gorges Dam in China serves multiple purposes but controversially:",["Has no drawbacks","*Displaced ~1.3 million people, submerged archaeological sites, and altered downstream ecosystems","Only generates power","Was never built"],"Three Gorges."),
     ("The Aral Sea disaster was caused by:",["Natural evaporation","Climate change alone","*Soviet-era diversion of rivers for cotton irrigation — the sea lost ~90% of its volume by 2010","Pollution only"],"Aral Sea."),
     ("Cape Town's 2018 'Day Zero' crisis (nearly running out of water) was caused by:",["Only drought","Only population growth","*Multi-year drought combined with growing demand and aging infrastructure","Only infrastructure"],"Cape Town."),
     ("Mississippi River flooding is managed through:",["Letting it flood freely","*A system of levees, floodways, and reservoirs — but this infrastructure has limits and alters natural flood patterns","Only dams","Only evacuation"],"Mississippi management."),
     ("The Murray-Darling Basin in Australia faces:",["Too much water","*Over-allocation for agriculture, severe drought impacts, and ecosystem degradation (similar to Colorado River issues)","No challenges","Only flooding"],"Murray-Darling."),
     ("China's South-North Water Transfer Project:",["Is small scale","*Is the world's largest infrastructure project, transferring water thousands of km from the south to the water-scarce north","Has been cancelled","Only plans exist"],"China transfer."),
     ("Israel leads in water innovation through:",["Importing water only","*Desalination (producing ~70% of domestic water), drip irrigation, water recycling (~85% of wastewater recycled)","Having abundant water","Only rationing"],"Israel innovation."),
     ("Water pricing affects conservation because:",["Price doesn't matter","*When water is cheap or free, people waste it — appropriate pricing encourages conservation and efficiency","High prices waste water","Only rich people use water"],"Price incentive."),
     ("Transboundary water disputes (e.g., Nile, Mekong, Jordan rivers) require:",["Only military solutions","*International cooperation, treaties, and equitable sharing frameworks","No attention","Only downstream priority"],"Diplomacy."),
     ("The concept of 'water bankruptcy' means:",["A company fails","*A region consumes water faster than nature replenishes it — eventually running out (like the Ogallala in some areas)","Banks control water","Water is free"],"Water bankruptcy."),
     ("Solutions to global water challenges include:",["Only one approach","Only technology","Only policy","*Integrated solutions: conservation, technology (desalination, recycling), policy reform, ecosystem protection, and international cooperation"],"Integrated solutions."),
     ("The key lesson from all water case studies is:",["Water is unlimited","*Fresh water is finite and increasingly stressed — proactive management, conservation, and cooperation are essential before crises develop","We can't affect water supply","Only nature controls water"],"Key lesson.")]
)
lessons[k]=v

# 3.9
k,v = build_lesson(3,9,"AP Prep: Ocean Circulation Models",
    "<h3>AP Prep: Ocean Circulation</h3>"
    "<h4>Surface Circulation</h4>"
    "<p>Wind-driven gyres: North Atlantic, South Atlantic, North Pacific, South Pacific, Indian Ocean. Coriolis deflection + continental blocking.</p>"
    "<h4>Deep Circulation</h4>"
    "<p>Thermohaline conveyor belt: cold, salty water sinks in the North Atlantic → flows along the ocean bottom → upwells in Pacific/Indian → returns via surface currents. Full cycle takes ~1,000 years.</p>"
    "<h4>AP Calculations</h4>"
    "<p>Current velocity, Coriolis parameter, Ekman transport, heat transport calculations.</p>",
    [("Thermohaline Conveyor Belt","Global ocean circulation driven by density; cold salty water sinks in North Atlantic, flows deep, upwells elsewhere; ~1,000 year cycle."),
     ("Western Boundary Currents","Narrow, deep, fast, warm currents on the western side of ocean basins (Gulf Stream, Kuroshio) — intensified by Coriolis and basin geometry."),
     ("AMOC (Atlantic Meridional Overturning Circulation)","Part of thermohaline circulation; transports warm surface water north and cold deep water south in the Atlantic."),
     ("Coriolis Parameter","f = 2Ω sin(φ); increases with latitude; determines the deflection of moving objects (including ocean currents)."),
     ("Ekman Spiral","Successive layers of water are deflected further from the wind direction; net transport is 90° to the wind.")],
    [("The thermohaline circulation's 'pump' is located where:",["At the equator","In the Pacific","*In the North Atlantic (near Greenland and Iceland — where cold, salty water sinks to the deep ocean)","In the Southern Ocean only"],"THC pump."),
     ("Water sinks in the North Atlantic because it becomes _____ and _____.",["Warm; fresh","*Cold and salty (ice formation removes fresh water, leaving dense salty water that sinks)","Hot; deep","Light; fresh"],"Sinking conditions."),
     ("The full cycle of the thermohaline conveyor belt takes approximately:",["1 year","10 years","*~1,000 years","10,000 years"],"Cycle time."),
     ("Western boundary currents (like the Gulf Stream) are _____ compared to eastern boundary currents.",["Slower and wider","Colder","*Faster, narrower, deeper, and warmer (intensified by Coriolis effect and western boundary compression)","Identical"],"WBC properties."),
     ("The Coriolis parameter (f = 2Ω sin φ) equals zero at the:",["Poles","*Equator (sin 0° = 0; no Coriolis deflection at the equator)","30° latitude","60° latitude"],"Coriolis at equator."),
     ("Ekman transport moves the net water flow _____ to the wind direction in the Northern Hemisphere.",["Parallel","Opposite","*90° to the right","45° to the left"],"Ekman NH."),
     ("Coastal upwelling on the western coast of continents occurs when equatorward winds cause Ekman transport:",["Onshore","*Offshore (surface water moves away from shore, drawing cold deep water up to replace it)","Downward","Poleward"],"Coastal upwelling."),
     ("If the AMOC weakened significantly, Europe would likely:",["Warm significantly","*Cool significantly (reduced northward heat transport — the Gulf Stream warming effect would diminish)","Be unaffected","Flood"],"AMOC weakening."),
     ("Climate models suggest that global warming could weaken the AMOC by:",["Cooling the Arctic","*Increasing freshwater input from Greenland ice melt (reducing the density and sinking of North Atlantic water)","Increasing salinity","Strengthening trade winds"],"AMOC threat."),
     ("The Antarctic Circumpolar Current (ACC) is unique because it:",["Is the weakest current","*Flows unimpeded around Antarctica (no continental barriers) — the strongest and largest current on Earth","Only flows south","Doesn't exist"],"ACC."),
     ("Ocean heat transport is important because it:",["Has no climate effect","*Moves enormous amounts of heat from the tropics to the poles, moderating global temperature differences","Only affects fishing","Only affects shipping"],"Heat transport."),
     ("Sverdrup transport theory relates _____ to the wind stress curl over the ocean.",["Temperature","*The total volume of water transported (linking wind patterns to ocean circulation patterns)","Salinity","Depth"],"Sverdrup."),
     ("Geostrophic currents flow:",["In any direction","Directly downhill","*Along lines of constant pressure (balance between pressure gradient force and Coriolis)","Only at the equator"],"Geostrophic flow."),
     ("Sea surface temperature (SST) maps from satellites help scientists:",["Only study weather","*Track current patterns, identify upwelling zones, monitor ENSO, and validate circulation models","Only find fish","Only measure depth"],"SST mapping."),
     ("The Ocean Carbon Cycle involves the ocean absorbing ~25% of anthropogenic CO₂ through:",["Waves only","*Physical dissolution (solubility pump) and biological processes (organisms incorporating carbon)","Only coral","No mechanism"],"Ocean carbon."),
     ("Increasing CO₂ absorption makes ocean water more _____, threatening calcifying organisms.",["Basic","*Acidic (CO₂ + H₂O → carbonic acid; ocean pH has dropped ~0.1 since pre-industrial times)","Neutral","Salty"],"Ocean acidification AP."),
     ("In AP problems, ocean current velocity can be estimated using:",["Only observation","*Geostrophic balance equations, Ekman theory, and Sverdrup balance — connecting physical forces to measurable currents","Only satellites","Only buoys"],"Calculation methods."),
     ("The global ocean circulation is sometimes called a conveyor belt because:",["It carries goods","*It continuously moves water (and heat) through a connected loop — surface warm flow and deep cold return flow","It's mechanical","It stops and starts"],"Conveyor metaphor."),
     ("Changes to ocean circulation could trigger _____ climate events.",["Only gradual","*Abrupt (paleoclimate records show rapid climate shifts linked to circulation changes — e.g., Younger Dryas cooling event)","No","Only warming"],"Abrupt events."),
     ("Mastering ocean circulation for the AP exam requires understanding:",["Only surface currents","Only deep currents","*The integration of wind patterns, Coriolis, thermohaline processes, and their climate implications","Only temperature"],"AP mastery.")]
)
lessons[k]=v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Integrated Science Unit 3: wrote {len(lessons)} lessons")
