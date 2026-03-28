import json

def fix_file(filepath, fixes):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data["quiz_questions"]:
        qnum = q["question_number"]
        if qnum in fixes:
            new_wrongs = fixes[qnum]
            wrong_idx = 0
            for opt in q["options"]:
                if not opt["is_correct"]:
                    opt["text"] = new_wrongs[wrong_idx]
                    wrong_idx += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"  Fixed {len(fixes)} questions")

# Lesson6.2 - Factors Affecting Climate (19 giveaways)
print("Fixing Lesson6.2_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit6/Lesson6.2_Quiz.json", {
    1: ["Soil composition and its ability to retain surface moisture levels",
        "Proximity to the nearest coastline or large body of water",
        "Prevailing wind direction and average seasonal wind speed patterns"],
    4: ["Uniformly dry conditions on both sides of the range due to elevated evaporation from warm ascending air",
        "No significant impact on regional precipitation because mountains are typically too low to alter major airflow",
        "Equal distribution of rainfall on both sides because atmospheric moisture recirculates over the mountain summit"],
    6: ["Cooling the entire planet by redirecting cold deep ocean water currents toward the surface layer",
        "Producing only localized effects that remain entirely confined within the equatorial Pacific region",
        "Only affecting the western coast of South America through upwelling of nutrient-rich deep water"],
    7: ["Day and night cycles by controlling the speed at which our planet rotates on its axis",
        "Frequent earthquakes by altering gravitational stress placed on major tectonic plate boundaries",
        "Ocean tidal patterns by modifying the gravitational pull angle between the Moon and Earth"],
    8: ["Releasing large quantities of CO2 that accumulate in the atmosphere and trap additional infrared radiation",
        "Creating massive ash clouds that completely disrupt prevailing wind patterns across entire continents",
        "Adding significant amounts of oxygen to the upper atmosphere through rapid mineral decomposition"],
    10: ["Are typically located at lower elevations in valley basins where warm air naturally collects and becomes stagnant",
         "Are generally constructed closer to the equator where incoming solar radiation is strongest throughout the year",
         "Generate increased rainfall through enhanced atmospheric moisture from irrigation and industrial cooling systems"],
    12: ["The influence that large continent size has on the direction and strength of nearby ocean currents along major coastal boundary zones",
         "The gradual effect that continental drift and plate tectonics have on shifting regional climate zones over long geological timescales",
         "The combined influence that the total number and arrangement of continents has on global atmospheric circulation and prevailing wind patterns"],
    14: ["A category of recurring tropical hurricane that forms exclusively in the central Pacific Ocean during the late autumn storm season",
         "A cold deep ocean current flowing northward along the coast of South America that brings nutrient-rich water to the surface year-round",
         "A permanent long-term shift in baseline ocean temperatures across the entire Pacific basin caused by changes in undersea volcanic activity"],
    15: ["The influence that seismic earthquake activity has on local atmospheric conditions through release of subsurface gases and ground heat",
         "The relationship between ocean depth and water temperature, where deeper waters are progressively colder due to reduced solar penetration",
         "The long-term effect that changes in Earth's orbital parameters have on seasonal solar radiation distribution across different latitude zones"],
    16: ["A tropical island that experiences unusually high temperatures compared to mainland areas due to its geographic isolation and solar exposure",
         "The geothermal heat produced by volcanic island chains that raises air and water temperatures in the surrounding ocean and coastal regions",
         "A large island formation that obstructs major ocean current pathways, redirecting warm water flow and altering downstream regional climates"],
    17: ["A climate classification applying exclusively to open ocean environments and the weather conditions experienced by vessels at sea",
         "A climate type defined primarily by receiving all of its precipitation from ocean-sourced moisture rather than continental evaporation",
         "A climate characterized by extremely wide temperature swings between seasons due to strong ocean wind currents alternating warm and cold air"],
    18: ["A permanently cold deep-water current in the North Atlantic Ocean that regulates European climate by transporting cold polar water southward",
         "A sustained warming event in the tropical Pacific Ocean that gradually raises regional sea surface temperatures over a period of several decades",
         "A powerful tropical storm system that develops in the western Pacific basin and produces destructive sustained winds and heavy rainfall on coasts"],
    19: ["A predictable cycle of large volcanic eruptions occurring at regular intervals that temporarily cool the global climate through aerosol injection",
         "The daily pattern of temperature increase during daytime hours and decrease during nighttime hours caused by the rotation of Earth on its axis",
         "The periodic reversal of major ocean current circulation patterns that redistributes heat across ocean basins on a multi-decadal timescale cycle"],
    21: ["The mountain generates its own localized weather system through convective uplift that produces persistent cold conditions at the summit",
         "Cold ocean currents near the coast of East Africa direct chilled maritime air masses up the mountain slopes to the summit peak year-round",
         "Equatorial regions experience significant seasonal temperature variations that periodically drop below freezing, allowing ice to persist"],
    25: ["Construct taller buildings throughout the downtown core to cast shade over streets, directly lowering ambient air temperatures across the urban area",
         "Install more powerful air conditioning in every building to cool indoor spaces, which would gradually reduce outdoor temperatures across the city",
         "Remove all paved surfaces and replace them with unpaved dirt roads and gravel pathways to eliminate the primary source of urban heat absorption"],
    26: ["City A has substantially more urban tree coverage than City B, and the shade and transpiration from this vegetation directly moderates its seasonal temperature swings",
         "City B is located slightly closer to the equator than City A despite being at the same nominal latitude, and this small difference intensifies seasonal heating patterns",
         "The higher elevation and different soil composition at City B cause it to absorb and release solar heat more rapidly than the lower-lying terrain around City A"],
    27: ["The sunspot cycle, which produces periodic changes in the Sun's total energy output that directly drive major shifts in global temperature over geological time",
         "El Nino and La Nina cycles, which periodically redistribute ocean heat and atmospheric moisture patterns strongly enough to trigger full glacial period transitions",
         "Volcanic eruption cycles, in which regularly timed massive eruptions inject enough stratospheric aerosols to cool the planet into extended ice ages"],
    28: ["Persistent El Nino conditions permanently warm the coastal waters near Chile, causing all available atmospheric moisture to evaporate before reaching the Atacama",
         "Chile is located at too high a latitude for tropical moisture systems to reach its coastal desert region, since weather patterns bypass the area entirely all year",
         "The adjacent Pacific Ocean has no measurable effect on the Atacama's climate because onshore winds are permanently blocked by a stable coastal temperature inversion"],
    30: ["The current warming is simply the natural continuation of the regular ice age cycle that has occurred repeatedly throughout Earth's geological history without any human influence",
         "Ice age cycles and the current warming trend operate through completely separate and unrelated physical mechanisms with no common atmospheric or orbital connections",
         "Natural factors such as solar variation and orbital changes have absolutely no influence on Earth's climate, and all observed temperature changes stem from human activity"]
})

# Lesson6.3 - Climate Zones & Biomes (14 giveaways)
print("Fixing Lesson6.3_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit6/Lesson6.3_Quiz.json", {
    4: ["Mid-latitude regions with moderate temperatures and seasonal rainfall",
        "Exclusively along continental coastlines influenced by cold currents",
        "Low-latitude regions near the equator with year-round warm conditions"],
    7: ["Heat-tolerant tropical palm species that thrive in warm and humid climates",
        "Broad-leaved deciduous hardwood trees that shed their foliage each autumn",
        "Extensive grassland prairies with scattered drought-resistant shrub species"],
    11: ["A numerical index used to measure and compare biodiversity levels across different geographic regions and habitat types",
         "A recurring atmospheric weather pattern that influences temperature and precipitation across a broad continental region",
         "A single plant or animal species that serves as an indicator organism for the overall health of its surrounding habitat"],
    14: ["An arid desert biome that receives occasional but unpredictable rainfall events supporting sparse drought-adapted vegetation",
         "A cold treeless plain at high latitudes characterized by permafrost, strong winds, and a very short annual growing season",
         "A dense multi-layered tropical forest with a thick canopy that blocks sunlight and receives heavy rainfall throughout the year"],
    15: ["A tropical forest biome characterized by tall canopy trees, heavy year-round rainfall, and the highest biodiversity of any terrestrial ecosystem on Earth",
         "A semi-arid desert grassland biome with sparse vegetation adapted to prolonged drought and extreme temperature fluctuations throughout the entire year",
         "A cold climate biome found exclusively in polar regions near the Arctic Circle, characterized by permafrost, mosses, and low-growing tundra shrub species"],
    16: ["A high-altitude mountain biome located above the treeline where only lichens and mosses can survive the extreme cold and powerful winds",
         "A tropical grassland ecosystem with widely scattered trees, found in equatorial regions of Africa and South America with distinct wet seasons",
         "A cold arid desert environment found exclusively in the interior of Siberia, characterized by sand dunes and extreme temperature fluctuations"],
    17: ["A climate zone defined by heavy year-round rainfall exceeding 200 cm annually that supports dense vegetation and high biodiversity levels",
         "A humid tropical climate found within 10 degrees of the equator with consistently warm temperatures and abundant daily afternoon rainfall",
         "A climate with moderate temperatures and balanced seasonal precipitation that supports temperate deciduous forests and mixed grasslands"],
    18: ["A climate found exclusively within the equatorial zone between the Tropics of Cancer and Capricorn with consistently warm conditions year-round",
         "A hyper-arid climate found in extreme desert environments that never experiences measurable rainfall in any month of the calendar year",
         "A perpetually cold climate with constant freezing temperatures throughout all twelve months, found only in the polar ice cap regions"],
    19: ["An extremely hot and arid climate found in subtropical desert regions where surface temperatures frequently exceed 50 degrees C in summer",
         "A tropical climate characterized by heavy monsoon rainfall exceeding 300 cm per year concentrated in a distinct wet season period",
         "A climate found exclusively on high mountain peaks above the treeline, where altitude rather than latitude determines the temperature"],
    21: ["The Amazon basin benefits from close proximity to the Atlantic Ocean, which provides constant moisture, while the Sahara is too far inland to receive significant oceanic rainfall",
         "The Sahara Desert sits at a much higher latitude than the Amazon rainforest, placing it well outside the belt of intense tropical rainfall that supports equatorial growth",
         "Ancient volcanic eruptions across the African continent destroyed the Sahara's original vegetation and deposited layers of mineral ash that permanently altered soil composition"],
    23: ["The Great Plains sit at too high an elevation for tree species to grow, since reduced atmospheric pressure and oxygen levels at that altitude limit large woody plant growth",
         "European settlers during the 1800s systematically cleared all native forests for lumber and farmland, and the original tree cover has never been able to reestablish itself",
         "The extremely sandy and nutrient-poor soil across the Great Plains cannot provide adequate anchorage or mineral nutrition for the deep root systems that tree species require"],
    26: ["Chaparral fires occur exclusively during El Nino years when dry warm winds from the Pacific increase temperatures and reduce humidity across the California coastal region",
         "Fires in chaparral ecosystems are triggered primarily by underground volcanic and geothermal activity that heats dry surface vegetation to its ignition temperature point",
         "Chaparral vegetation has no adaptations to survive fire and must be completely replaced by new seeds blown in from distant unburned areas after each major wildfire event"],
    29: ["Tundra biomes cover extremely small geographic areas compared to tropical regions, and this limited spatial extent severely restricts the total number of species that coexist",
         "Tropical regions lack significant predator populations, which eliminates natural selection pressure and allows nearly all species that evolve there to survive without competition",
         "Tropical rainforest soils contain exceptionally high concentrations of nutrients and organic matter that support the abundant plant growth underlying a complex layered food web"],
    30: ["The sandy and mineral-poor desert soil in Phoenix lacks the essential nutrients and organic matter that water-dependent deciduous trees require to establish healthy root systems",
         "Deciduous trees evolved exclusively in the Southern Hemisphere and cannot physiologically adapt to the Northern Hemisphere's reversed seasonal light and temperature cycles",
         "Phoenix's elevated levels of urban air pollution generate excessive ozone and particulate matter that damage leaf tissue and prevent deciduous trees from photosynthesizing"]
})

# Lesson6.4 - The Greenhouse Effect (15 giveaways)
print("Fixing Lesson6.4_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit6/Lesson6.4_Quiz.json", {
    11: ["The process by which thick cloud layers reflect incoming shortwave solar radiation back into space, reducing the energy reaching Earth's surface",
         "The process by which stratospheric ozone molecules absorb harmful ultraviolet radiation from the Sun, preventing it from reaching surface organisms",
         "The physical mechanism by which glass-enclosed agricultural greenhouses trap warm air inside, raising temperatures to extend the growing season"],
    12: ["A specialized gas compound found exclusively inside enclosed glass greenhouses that helps maintain warm temperatures for optimal plant cultivation",
         "A heavy atmospheric gas that completely blocks all incoming solar radiation from reaching Earth's surface, creating cooler conditions underneath",
         "Any gaseous element or compound present in the atmosphere regardless of whether it has any effect on the absorption or emission of radiation"],
    13: ["The total count of individual gas molecules contained within exactly one liter of atmospheric air at standard temperature and sea-level pressure",
         "The partial pressure that a specific gas exerts within the atmosphere, measured in units of atmospheric pressure relative to the total mixture",
         "The molecular weight of a specific gas compound expressed as a ratio to the standard atomic mass unit used in atmospheric chemistry analysis"],
    14: ["The geological process by which elemental carbon is subjected to extreme underground heat and pressure over millions of years, transforming it into diamond",
         "The industrial recycling process that converts discarded plastic products back into reusable raw materials through chemical breakdown and reformation",
         "The industrial combustion process of burning fossil fuels such as coal, oil, and natural gas to release stored chemical energy for power generation"],
    15: ["The ionizing radiation produced by nuclear power plants during uranium fission, which must be carefully contained to prevent environmental contamination",
         "The reflection of incoming solar shortwave radiation by large continental ice sheets and polar glaciers, which increases Earth's overall surface albedo",
         "The total quantity of electromagnetic radiation emitted by the Sun across all wavelengths, including visible light, ultraviolet, and infrared output"],
    17: ["A long-term monitoring chart showing changes in stratospheric ozone concentration measured at Antarctic research stations since the early 1970s",
         "A comprehensive historical graph displaying average global surface temperature changes reconstructed from proxy data and instruments since 1800",
         "A detailed oceanographic map showing the major global thermohaline circulation pathways that redistribute heat between tropical and polar oceans"],
    18: ["A widespread increase in public support and favorable opinion regarding government policies aimed at reducing greenhouse gas emissions and climate impacts",
         "A documented beneficial side effect of climate change such as longer agricultural growing seasons or reduced winter heating costs in cold northern areas",
         "A self-correcting atmospheric process that always returns the global climate to its original equilibrium state regardless of the magnitude of any disturbance"],
    20: ["An industrial facility or natural location where carbon-containing materials are combusted to generate energy or dispose of accumulated organic waste",
         "A natural or human-made source that releases carbon dioxide and other greenhouse gases into the atmosphere through combustion or biological processes",
         "A specialized container or storage vessel designed to hold charcoal, coal, or other solid carbon materials for later use in various industrial applications"],
    21: ["Venus has significantly higher volcanic activity than Mercury, and continuous eruptions release enough geothermal energy to heat its surface directly",
         "Venus rotates much faster on its axis than Mercury, generating substantial internal frictional heat that radiates outward and warms the surface",
         "Mercury's highly reflective metallic surface bounces most incoming sunlight back into space, preventing it from reaching temperatures as high as Venus"],
    22: ["Seasonal wind pattern changes shift large masses of CO2-enriched air between the Northern and Southern Hemispheres, creating alternating concentration peaks",
         "Significantly higher rates of fossil fuel combustion for residential and commercial heating during winter months add enough CO2 to create the seasonal peak",
         "The ocean absorbs substantially more atmospheric CO2 during summer months when warmer surface temperatures increase gas dissolution at the air-sea interface"],
    25: ["Water vapor has essentially no warming effect on Earth's atmosphere because its molecules are too lightweight to effectively absorb and re-emit infrared radiation at scale",
         "CO2 is present at significantly higher atmospheric concentrations than water vapor throughout most of the atmosphere, making it the dominant infrared radiation absorber",
         "Individual CO2 molecules are far more efficient at absorbing infrared radiation than water vapor molecules, which is why small amounts of CO2 dominate the warming effect"],
    26: ["CO2 molecules released by human activity have a different molecular structure than naturally occurring CO2, allowing scientists to chemically distinguish between the sources",
         "Ice core data from polar research stations contains too many measurement errors and contamination artifacts to provide reliable information about past atmospheric conditions",
         "Atmospheric CO2 concentrations have remained completely stable throughout Earth's entire geological history and have never varied through any natural process whatsoever"],
    27: ["Synthetic nitrogen fertilizers applied to agricultural fields undergo chemical reactions with soil minerals that transform their molecular structure into methane gas molecules",
         "Diesel and gasoline engines used in farm machinery and tractors release significant quantities of unburned methane through their exhaust systems during field operations",
         "Chemical pesticides sprayed on crops gradually decompose in the soil through photochemical reactions, and their carbon-hydrogen bonds recombine to form methane molecules"],
    28: ["Mars orbits too far from the Sun for any measurable greenhouse warming to occur, because the solar radiation reaching its surface is too weak to generate trapped infrared",
         "CO2 only functions as a greenhouse gas under the specific atmospheric conditions found on Earth, and its molecular properties change on planets with different gravity levels",
         "Mars does not emit any infrared radiation from its surface because its extremely cold temperatures prevent the ground from radiating measurable thermal energy upward"],
    29: ["The climate models contain fundamental calculation errors that significantly overestimate the warming response to increased atmospheric CO2 concentrations over time",
         "The Sun's luminosity has been steadily increasing at the same time as CO2 rises, and this solar brightening accounts for the additional warming beyond the direct CO2 effect",
         "Other greenhouse gases including methane and nitrous oxide are simultaneously doubling in concentration alongside CO2, and their combined warming adds to the total effect"]
})

print("Batch 3 complete!")
