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


base = "c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit10"

# ============================================================
# LESSON 10.4 - Real-World Applications (18 giveaway questions)
# ============================================================
print("Fixing Lesson10.4_Quiz.json...")
fix_file(f"{base}/Lesson10.4_Quiz.json", {
    2: [
        "To establish international trade regulations governing the commercial export and import of wildlife specimens and their derived biological products",
        "To create a comprehensive national database cataloguing all known wildlife species found within the borders of federally managed public land areas",
        "To fund scientific research programs exclusively dedicated to the captive breeding of large mammals housed in nationally accredited zoological facilities",
    ],
    9: [
        "To establish legally binding emission reduction targets that individual industrial manufacturing facilities must achieve during each annual compliance reporting period",
        "To track the seasonal migration corridors of airborne pollen and allergen particles across the major regional atmospheric circulation patterns nationwide",
        "To calibrate and maintain the specialized measurement instruments used at federally operated atmospheric research stations and regional air monitoring laboratories",
    ],
    10: [
        "The comprehensive inventory of all documented plant and animal species within a defined geographic region, compiled through systematic biodiversity assessment surveys conducted over multiple seasons",
        "The total annual financial expenditure allocated by governmental agencies for the operational management and routine maintenance of designated national parks and protected areas",
        "The engineering and construction costs associated with building artificial infrastructure systems specifically designed to replicate natural processes such as water filtration and flood storage",
    ],
    12: [
        "The legal prosecution and judicial sentencing of corporations and individuals found guilty of intentional environmental contamination under applicable federal criminal regulatory statutes",
        "The scientific principle that all ecosystems possess an inherent legal right to exist and flourish independent of their direct or indirect economic value to human populations and societies",
        "A branch of international law that governs the allocation of financial liability and compensation for transboundary environmental pollution between neighboring sovereign nations",
    ],
    13: [
        "A fixed long-term resource management plan established through legislative mandate that remains unchanged regardless of any new environmental monitoring data that may be collected",
        "A management philosophy that prioritizes rapid economic development of natural resources ahead of completing comprehensive environmental baseline assessment studies for the area",
        "A crisis response protocol activated exclusively during officially declared natural disaster emergencies that temporarily suspends all standard environmental regulatory requirements",
    ],
    17: [
        "The deliberate large-scale modification of atmospheric chemistry through stratospheric aerosol injection designed to counteract the effects of rising global average temperatures",
        "International diplomatic negotiations aimed at establishing legally binding greenhouse gas emission reduction targets specifically for industrialized nations under multilateral treaty",
        "The natural evolutionary process by which plant and animal species develop entirely new physical traits over many successive generations in response to changing environmental pressures",
    ],
    18: [
        "The geographic area of land surface required to absorb and sequester the carbon dioxide emissions produced by a single household through natural forest photosynthesis processes",
        "A standardized laboratory measurement of the total carbon concentration found within representative soil samples collected from agricultural land under active seasonal cultivation",
        "The physical impression left in sedimentary rock formations by ancient carbon-based organisms, used by paleontologists to estimate past atmospheric composition and temperature levels",
    ],
    19: [
        "A centralized engineering system designed to collect, purify, and redistribute municipal drinking water through a unified network of treatment plants and underground pipeline infrastructure",
        "A bilateral trade agreement framework governing the commercial sale and export of bottled water products between nations with surplus freshwater and those experiencing chronic water shortages",
        "A standardized industrial protocol requiring all manufacturing facilities to recycle and reuse one hundred percent of their process wastewater before discharging any effluent to surface water",
    ],
    21: [
        "Proposal A, because concentrating all emission reduction resources into government fleet and building projects ensures faster measurable results and simpler program administration overall",
        "Neither proposal will achieve meaningful reductions because municipal-level climate policies cannot generate sufficient impact without simultaneous coordinated action from state and federal agencies",
        "Proposal A, because converting the vehicle fleet to electric and installing solar panels on government buildings directly controls emission sources the city has legal authority to modify immediately",
    ],
    22: [
        "Restore the degraded agricultural land because the four-to-one area advantage provides significantly more total habitat acreage, and the corridor connectivity between protected areas will benefit more species",
        "Purchase the old-growth forest exclusively and permanently abandon any restoration plans for the degraded land, since limited conservation funds should never be divided between competing priorities",
        "Restore the degraded land first because habitat connectivity between existing protected areas has been consistently demonstrated by research to provide greater long-term biodiversity benefits overall",
    ],
    23: [
        "Grant unconditional mining permits immediately because the economic benefits of five thousand new jobs and substantial export revenue clearly outweigh any potential environmental degradation in the surrounding tropical forest watershed",
        "Permanently prohibit all mineral extraction activities within the entire national territory because the long-term ecological value of intact tropical forest ecosystems and watershed protection services will always exceed short-term economic gains",
        "Allow mining operations to proceed without environmental oversight but require the company to plant an equivalent number of trees in a different geographic region to offset the loss of forest biodiversity and watershed services",
    ],
    24: [
        "Allow the upstream country to complete its dam construction project without restriction since international law grants absolute territorial sovereignty over all natural resources located within a nation's borders",
        "Require the downstream countries to independently develop alternative freshwater sources such as desalination plants and deep groundwater wells rather than negotiating shared access to the contested river resources",
        "Establish an international enforcement mechanism authorized to physically dismantle any water infrastructure project constructed by an upstream nation that measurably reduces downstream river flow volume below historical levels",
    ],
    25: [
        "Immediately apply industrial-strength chemical dispersants uniformly across the entire affected estuary surface area to break down the oil slick before it reaches the shoreline, nesting habitats, and productive fishing grounds",
        "Conduct controlled in-situ burning of all visible surface oil throughout the estuary including near shorebird nesting areas because rapid thermal destruction of hydrocarbons is the most efficient method for reducing environmental exposure time",
        "Delay all cleanup operations for a minimum of six months to allow comprehensive baseline environmental assessments before any intervention decisions are made, since premature action could potentially cause more ecological damage than the spill",
    ],
    26: [
        "Issue a public advisory recommending that all community residents boil their drinking water before consumption since thermal treatment effectively neutralizes dissolved nitrate compounds and renders them biologically harmless to consumers",
        "Permanently seal and decommission the contaminated drinking water well and begin drilling a series of deeper replacement wells in the same aquifer formation on the assumption that nitrate contamination is limited to shallow groundwater zones",
        "Implement a mandatory ban on all synthetic fertilizer use within a fifty-kilometer radius of the community well and wait for natural groundwater flushing cycles to gradually reduce nitrate concentrations below the regulatory limit",
    ],
    27: [
        "Construct a large-scale desalination plant powered by imported diesel fuel generators to provide the island's entire freshwater supply independently of increasingly unreliable groundwater and seasonal precipitation sources",
        "Invest all available international development funding exclusively in constructing reinforced concrete seawall infrastructure around the island's entire coastal perimeter to physically prevent future ocean erosion and saltwater intrusion",
        "Develop a comprehensive population relocation plan to permanently evacuate all residents from vulnerable low-lying coastal areas to the island's interior highlands where they would be fully protected from rising sea levels",
    ],
    28: [
        "Focus exclusively on distributing portable air conditioning units to every household in the city because individual residential cooling capacity is the single most important factor in reducing heat-related mortality during extreme events",
        "Invest all available municipal funding in constructing large-scale reflective shade structures over major roadways and public spaces throughout the metropolitan area to reduce direct solar radiation exposure across all neighborhoods equally",
        "Establish a mandatory citywide evacuation protocol that requires all residents in affected neighborhoods to temporarily relocate to designated climate-controlled emergency shelters located in cooler suburban areas during declared heat emergencies",
    ],
    29: [
        "Maintain the existing dam infrastructure indefinitely without modification because the original construction investment and current hydroelectric generation capacity justify continued operation regardless of any documented downstream ecological consequences",
        "Immediately demolish the entire dam structure without conducting any preliminary engineering assessment or downstream flood risk analysis because ecological restoration of the river system should take absolute unconditional priority",
        "Retrofit the dam exclusively with modern fish ladder passage structures while continuing all other dam operations at full capacity because providing fish migration routes alone is sufficient to address all documented ecological impacts",
    ],
    30: [
        "Approve the data center construction with standard evaporative cooling towers because the facility's commitment to using one hundred percent solar-generated electricity for its power supply adequately offsets any additional water consumption",
        "Reject the project application entirely because no technology development proposal should ever be approved in any water-stressed geographic region regardless of what conservation offset measures the project applicant offers",
        "Approve the project without any water-use conditions because the economic benefits of technology sector employment and regional tax revenue from a major data center facility automatically outweigh the environmental cost of increased water extraction",
    ],
})

# ============================================================
# LESSON 10.5 - Capstone Project: Earth Systems Analysis (25 giveaway questions)
# ============================================================
print("Fixing Lesson10.5_Quiz.json...")
fix_file(f"{base}/Lesson10.5_Quiz.json", {
    2: [
        "Gathering the largest possible volume of environmental monitoring data from all available satellite and ground-station sources before formulating any specific questions",
        "Selecting the most visually compelling data visualization format for the final presentation slides before any actual data analysis work has been conducted",
        "Assembling a complete annotated bibliography of every published research article that is even tangentially related to the broad general study topic area",
    ],
    3: [
        "Exclusively the geosphere-atmosphere interaction where mineral dust particles from newly exposed soil surfaces enter the regional atmospheric circulation, with no meaningful effects on water cycling or biological communities in the watershed",
        "Primarily the hydrosphere-geosphere interaction of increased surface water acidification caused by chemical leaching of decomposing root material into nearby stream channels, with negligible atmospheric or broader biological consequences downstream",
        "Only the atmosphere-hydrosphere interaction of significantly increased regional precipitation resulting from enhanced surface water evaporation off newly cleared and directly sun-exposed terrain surfaces throughout the affected watershed basin area",
    ],
    4: [
        "A detailed topographic contour map highlighting measured changes in surface elevation across the entire study area over the full observation period",
        "A comprehensive data inventory spreadsheet listing every variable collected during fieldwork, organized by date, location, and instrument type",
        "A chronological timeline chart displaying each historical environmental event recorded within the specific geographic study region of interest",
    ],
    6: [
        "Temporal analysis is relevant only for atmospheric phenomena such as weather forecasting and seasonal climate prediction, since geological and biological processes remain essentially constant over observable research periods",
        "All meaningful Earth system processes operate exclusively within human-observable timescales of days to decades, which makes longer geological time perspectives unnecessary for practical environmental management decisions",
        "Temporal scale refers exclusively to the duration of individual data collection field campaigns, determining how many consecutive hours of continuous monitoring are required per each sampling session at a given location",
    ],
    7: [
        "Because federal regulatory agencies require all environmental research projects to include a standardized data quality assessment section in their final published reports regardless of the data sources used",
        "Because combining multiple data sources always increases the total error in the final analysis proportionally to the number of sources, making results progressively less reliable with each additional dataset",
        "Because satellite remote sensing data has been definitively established as the only fully reliable source of environmental information for any Earth systems analysis project undertaken at regional scales",
    ],
    8: [
        "Stakeholders serve exclusively as the funding sources for research projects and therefore their primary role is limited to approving annual budgets and setting maximum expenditure limits for all field operations",
        "Stakeholders are consulted only during the final presentation phase of a completed project to provide audience questions, having no influence on the actual research design, data collection methods, or analysis",
        "Stakeholders are relevant only in policy implementation contexts and should be deliberately excluded from the scientific analysis phase to prevent potential bias from influencing objective data interpretation",
    ],
    9: [
        "Models provide definitive proof of specific future environmental outcomes that eliminates all remaining scientific uncertainty from projections and subsequent policy recommendations",
        "Models are valuable primarily as visual presentation aids for communicating completed research findings, rather than as active analytical tools used during the investigation phase itself",
        "Models function exclusively as historical record-keeping tools that archive past environmental conditions but cannot generate any forward-looking predictions or useful scenario analyses",
    ],
    10: [
        "Human activities should be analyzed separately from natural Earth system processes because they operate through fundamentally different physical mechanisms and distinct energy transfer pathways",
        "Human influence on Earth systems remains negligible compared to natural geological and astronomical forcing factors and can therefore be safely excluded from most environmental analysis projects",
        "Human activities only significantly affect the biosphere through direct physical habitat destruction and have no measurable influence on atmospheric composition, ocean chemistry, or geological processes",
    ],
    13: [
        "A fully detailed mathematical simulation that precisely replicates every known physical and chemical process operating within the study system at the highest available computational resolution level",
        "A preliminary research proposal document submitted to funding agencies that describes the intended scope of all data collection activities before any actual fieldwork or analysis has been started",
        "A three-dimensional physical scale model constructed from laboratory materials that accurately reproduces the topographic features and geological structures of the specific geographic study area",
    ],
    14: [
        "A fundamental physical property that can be directly measured from any single isolated component of a system without requiring any knowledge of other component interactions or behaviors",
        "A previously unknown property of a specific chemical element or compound that scientists discover for the first time through the use of advanced laboratory instrumentation and analytical methods",
        "A temporary characteristic that appears only during the initial formation phase of a system and that subsequently disappears once the system reaches its stable long-term equilibrium condition",
    ],
    15: [
        "A conservation strategy focused exclusively on preserving wilderness areas that remain completely unmodified by any documented form of human activity or historical anthropogenic influence",
        "An engineering approach that designs infrastructure systems to operate independently from natural environmental processes in order to maximize construction reliability and operational efficiency",
        "A research methodology that deliberately separates and isolates human behavioral data from ecological measurements to prevent cross-contamination between social science and natural science datasets",
    ],
    16: [
        "The minimum threshold value that any environmental measurement must exceed before it is considered statistically significant for formal inclusion in a peer-reviewed research dataset",
        "The arithmetic average of all environmental measurements collected during the most recent annual monitoring cycle for a given study site or designated regional research station",
        "Preliminary observational data collected during the initial reconnaissance phase of a research project that is routinely discarded before the formal quantitative analytical phase begins",
    ],
    18: [
        "The manual creation of hand-drawn cartographic maps illustrating the physical boundaries and political jurisdictions of geographic regions without using any form of digital computational technology",
        "A statistical method that analyzes only the numerical attributes of environmental data points while deliberately excluding all geographic location information and spatial coordinate references",
        "The photographic documentation of landscape features from ground-level observation points, organized into a systematic visual archive catalogued by geographic region and seasonal collection date",
    ],
    19: [
        "The physical collection of geological rock samples, water specimens, and biological tissue by trained field researchers deployed to remote and difficult-to-access wilderness study locations",
        "The transmission of real-time seismograph readings from earthquake monitoring stations in remote locations to centralized data processing facilities via satellite communication relay networks",
        "An automated laboratory technique that measures the chemical composition of soil and rock samples through spectroscopic analysis without requiring any direct physical contact with the sample material",
    ],
    20: [
        "Waiting until absolute scientific certainty has been conclusively achieved on every relevant research question before authorizing any environmental management action or policy decision whatsoever",
        "Collecting observational evidence only after management decisions have already been fully finalized and implemented, primarily to document the outcomes of the actions that were already taken",
        "Relying exclusively on the professional opinions of senior government administrators and elected political officials who possess the legal authority to make binding environmental policy decisions",
    ],
    21: [
        "Collect additional water samples from the center of the lake at monthly intervals for one full calendar year to build a more comprehensive chemical database before attempting to identify any upstream nutrient sources or develop any causal analysis of the eutrophication process and associated biodiversity impacts",
        "Focus the analysis exclusively on the algal bloom component by identifying the dominant phytoplankton species present and researching their optimal growth conditions in published literature, without investigating any external watershed nutrient sources or downstream ecological consequences of the bloom events throughout the lake system",
        "Install aeration equipment in the deepest portion of the lake to immediately increase dissolved oxygen concentrations and address the fish mortality symptoms directly, while deferring any systematic investigation into the underlying causes of the nutrient enrichment problem and the broader watershed-level eutrophication dynamics that drive the recurring algal blooms",
    ],
    22: [
        "Analyze each environmental dataset independently in separate sections of the final report, presenting the land-use maps, water quality data, biodiversity surveys, and air quality measurements as parallel but unconnected trend descriptions without any cross-referencing between environmental indicators and land-use change patterns over the fifty-year study period",
        "Focus the analysis exclusively on the most recent 2020 dataset because it represents current conditions, and present a detailed snapshot analysis of that single time period without incorporating the historical trajectory demonstrated by the 1970 and 1990 data that could reveal important temporal trends in the relationship between urbanization and environmental degradation",
        "Compare only the total geographic area converted from natural land cover to urban development between each time period without analyzing any of the accompanying environmental quality datasets, since the magnitude of land-use change alone is sufficient to demonstrate the environmental impact of urban sprawl without requiring additional water quality or biodiversity evidence",
    ],
    23: [
        "A detailed engineering feasibility study for constructing continuous reinforced seawall infrastructure along the entire vulnerable coastline, including structural design specifications, material cost projections, and estimated construction timelines for each coastal segment requiring protection from projected sea-level rise scenarios",
        "A recommendation to implement a uniform mandatory evacuation and permanent relocation program for all residents living within the projected inundation zones regardless of individual household income level, community preference, cultural attachment, or the availability of viable alternative housing in safer inland locations",
        "An economic cost-benefit analysis calculating the total assessed market value of real estate properties within each projected inundation zone to determine which specific areas generate sufficient annual tax revenue to justify the substantial public investment required for constructing adequate protective coastal infrastructure",
    ],
    24: [
        "Exclusively the levelized cost of electricity generated by each source measured in dollars per kilowatt-hour, since economic competitiveness is the single most reliable indicator of overall environmental sustainability and long-term viability",
        "Only the total nameplate electrical generation capacity measured in megawatts and the average annual capacity factor for each energy source, since these engineering specifications alone determine overall environmental impact magnitude",
        "Primarily the direct carbon dioxide emissions produced during the electricity generation phase of operations alone, since greenhouse gas output is the only environmental metric with internationally standardized measurement protocols",
    ],
    25: [
        "Recommend that the region immediately resume the historical fire suppression strategy with significantly increased funding for aerial firefighting fleet capacity, since preventing all wildfire ignition remains the most effective approach to protecting communities and forest resources from the combined risks of accumulated fuel loads and extended fire seasons",
        "Attribute the increased wildfire risk entirely to anthropogenic climate change and recommend that the region focus exclusively on global greenhouse gas emission reduction advocacy rather than investing resources in any local-scale forest management, prescribed burn programs, or community wildfire preparedness planning efforts within the mountainous study region",
        "Present the historical fire suppression data and current climate change data as two completely independent contributing factors and analyze each one separately without exploring how their simultaneous interaction creates a compound risk that is significantly greater than either individual factor would produce acting alone in the mountainous region",
    ],
    26: [
        "Conduct a comprehensive statistical ranking of all four contributing factors using published mortality data and identify the single highest-ranked stressor as the primary cause, then recommend directing all available conservation funding exclusively toward eliminating that one dominant threat to pollinator populations in the region",
        "Acknowledge that multiple factors contribute to pollinator decline but argue that limited conservation resources require focusing on the single most cost-effective intervention, recommending a complete ban on the specific pesticide class most frequently associated with laboratory bee mortality studies and controlled field experiments",
        "Conclude that the complexity of multiple interacting stressors makes the pollinator decline problem fundamentally intractable with current scientific understanding, and recommend deferring all management action until controlled factorial experiments can conclusively isolate each individual factor's precise quantitative contribution to overall population loss",
    ],
    27: [
        "Present exclusively the environmental depletion data and recommend an immediate permanent moratorium on all groundwater pumping for agricultural irrigation throughout the entire region until the aquifer has fully recovered to its original pre-development water table elevation, regardless of the economic consequences for farming communities",
        "Present exclusively the economic data demonstrating the agricultural community's financial dependence on irrigation water and recommend that current pumping rates be maintained without reduction, on the grounds that local employment and food production capacity must take unconditional priority over long-term aquifer sustainability concerns",
        "Acknowledge the controversy between farming interests and environmental concerns but conclude that the fundamental disagreement cannot be resolved through scientific analysis alone, and recommend that the decision be delegated entirely to elected government officials without any further technical input or data presentation from the student research team",
    ],
    28: [
        "It relies exclusively on a single data source of satellite imagery analyzed over a continuous multi-decade observation period, which provides sufficient temporal coverage but lacks integration with other environmental or socioeconomic datasets from complementary monitoring systems and field-based data collection programs",
        "It provides a thorough quantitative measurement of glacier area change but treats the cryosphere as an isolated physical system without connecting the observed ice loss to any downstream hydrological, ecological, or human population consequences that would be affected by reduced seasonal meltwater discharge in the river basin",
        "It demonstrates strong technical proficiency in remote sensing image processing and geographic information system analysis techniques but does not extend the investigation beyond the physical measurement of glacier retreat to consider the broader Earth system interactions and coupled human-natural system dynamics involved",
    ],
    29: [
        "Include a single summary paragraph acknowledging that socioeconomic factors exist but maintain the primary analytical focus exclusively on atmospheric temperature measurements, surface albedo calculations, and impervious surface mapping data throughout the rest of the report",
        "Replace the entire physical science analysis of urban heat island atmospheric dynamics with a purely social science investigation of income inequality, housing affordability patterns, and residential segregation across the metropolitan area and its surrounding suburban communities",
        "Add a comparative analysis of municipal government heat emergency response budgets across different city administrative departments to determine whether current public expenditure allocations are proportional to the geographic distribution of measured heat island intensity",
    ],
    30: [
        "Select the single most likely future scenario based on current observed trends and develop highly specific detailed recommendations optimized exclusively for that one projected outcome without considering any alternative possibilities or potential deviations",
        "Acknowledge that uncertainty exists in a brief methodological limitations section at the end of the report but proceed to present all recommendations with full confidence as though the underlying projections carry absolutely no meaningful uncertainty",
        "Conclude that the level of uncertainty in the analysis renders all recommendations premature and unreliable, and advise decision-makers to postpone all water management planning actions until additional research substantially reduces the remaining scientific uncertainty",
    ],
})

# ============================================================
# LESSON 10.6 - Comprehensive Review & AP Exam Prep (22 giveaway questions)
# ============================================================
print("Fixing Lesson10.6_Quiz.json...")
fix_file(f"{base}/Lesson10.6_Quiz.json", {
    2: [
        "Climate describes the daily fluctuations in atmospheric conditions that people experience directly, while weather represents the statistical average of those observations accumulated over long periods",
        "Weather is determined primarily by local geographic features such as elevation and proximity to large water bodies, while climate is controlled entirely by large-scale astronomical orbital cycles",
        "Weather refers exclusively to precipitation events and temperature extremes in tropical and subtropical regions, while climate describes atmospheric conditions measured only at high-latitude polar stations",
    ],
    6: [
        "The rapid deposition of windblown mineral particles across continental surfaces during prolonged regional drought periods that persist over several consecutive decades without significant rainfall",
        "The direct crystallization of dissolved mineral compounds from groundwater solution as it gradually evaporates from porous subsurface rock formations under arid climatic conditions over extended periods",
        "The mechanical grinding and pulverization of bedrock into fine particles by repeated glacial advance and retreat cycles during successive continental ice age periods throughout the Pleistocene epoch",
    ],
    7: [
        "Seasonal variations in the gravitational tidal forces exerted on Pacific Ocean basins by the combined orbital positions of the Moon and nearby inner planets relative to Earth",
        "Long-term shifts in deep ocean thermohaline circulation patterns driven by gradual changes in Antarctic ice sheet meltwater discharge rates flowing into the Southern Ocean basin",
        "Regular oscillations in undersea volcanic activity along the East Pacific Rise spreading center that periodically warm overlying surface waters through direct geothermal heat transfer",
    ],
    8: [
        "A mineral is any naturally occurring solid material found beneath the Earth's surface at depths greater than one kilometer, while a rock is exclusively a surface-level geological formation",
        "Minerals are identified and classified solely on the basis of their external color and visual appearance, while rocks are categorized exclusively based on their total weight and measured density",
        "A mineral is defined as any naturally occurring substance that contains economically valuable metallic elements, while a rock is any geological material that lacks significant commercial extraction value",
    ],
    11: [
        "The observational finding that continents gradually sink deeper into the underlying mantle material over long geological timescales due to the continuous accumulation of heavy sedimentary material on their surfaces",
        "The hypothesis that Earth's interior consists of uniformly composed concentric shells of progressively increasing density, with no lateral variation in composition or mechanical properties at any given depth",
        "The geological principle that all major landforms currently visible on Earth's surface were created during a single catastrophic global event rather than by ongoing gradual processes operating over billions of years",
    ],
    12: [
        "The sequence of metabolic chemical reactions occurring within the cells of a single living organism during its complete individual developmental lifespan from birth to senescence",
        "The industrial manufacturing process through which raw geological mineral deposits are chemically refined and processed into commercially useful synthetic materials and finished products",
        "A periodic fluctuation in the concentration of a specific atmospheric trace gas that follows a predictable annual seasonal pattern driven primarily by changes in solar radiation intensity",
    ],
    13: [
        "The mathematical calculation of the precise angle and compass direction at which tilted sedimentary rock strata are inclined relative to the horizontal reference plane in the field",
        "A laboratory technique for determining the exact mineral composition and chemical elemental abundances present within a single representative hand specimen of any given rock type",
        "The measurement of the total vertical thickness of an uninterrupted sedimentary rock sequence exposed in a single continuous outcrop located at one specific geographic field location",
    ],
    14: [
        "A characteristic fracture pattern in crystalline igneous rocks where cooling contraction produces intersecting joint sets that consistently meet at predictable measurable angles throughout the rock body",
        "A depositional feature formed when sedimentary layers accumulate against a steeply inclined pre-existing surface such as a buried hillside, producing progressively thinning beds that converge at depth",
        "A structural measurement describing the specific compass bearing direction and downward inclination angle of a planar geological feature such as a bedding surface, fault plane, or foliation",
    ],
    15: [
        "The total thermal energy stored within Earth's interior mantle and core layers, originating from residual planetary accretion heat and ongoing radioactive element decay processes",
        "The insulating capacity of Earth's atmospheric gas layers measured by their collective ability to prevent surface heat from escaping to outer space through infrared radiation emission",
        "The intensity of reflected visible light measured from Earth's surface by orbiting satellite radiometers, used primarily to calculate regional and global planetary surface albedo values",
    ],
    16: [
        "The investigation of residual magnetism in ancient archaeological artifacts to determine the geographic origins and continental-scale trade routes of early human civilizations",
        "The measurement of current magnetic field intensity and directional variation at globally distributed ground-based observatory stations for navigation and applied geophysical purposes",
        "The application of powerful artificial electromagnetic fields to subsurface geological formations as an exploration technique for locating economically valuable mineral ore deposits",
    ],
    19: [
        "The engineered distribution of treated municipal drinking water through underground pipeline networks from centralized purification facilities to individual residential and commercial service connections throughout urban areas",
        "The seasonal expansion and contraction of polar ice sheet margins driven by annual temperature variation cycles that redistribute frozen water between continental glaciers and surrounding ocean basins",
        "The gradual geological process through which dissolved mineral compounds are transported by flowing groundwater and progressively deposited as crystalline formations within underground limestone caverns",
    ],
    20: [
        "The narrow band of visible light wavelengths that human eyes can naturally detect, ranging from approximately four hundred to seven hundred nanometers, which defines the only useful portion for satellite imagery",
        "The specific set of radio frequency communication channels officially allocated by international regulatory authorities for transmitting digital data between orbiting satellite platforms and ground receiving stations",
        "The range of electrical current frequencies generated by standard laboratory power supply equipment used to operate the analytical instruments that measure and process returned geological field samples",
    ],
    21: [
        "S-waves lose energy exponentially as they travel through the increasingly dense and hot material of Earth's deep mantle, and beyond 104 degrees the cumulative energy loss renders them too weak for surface seismograph instruments to detect above natural background noise levels at any recording station",
        "S-waves are reflected back toward the surface by the sharp compositional density contrast at the mantle-core boundary and cannot penetrate any deeper into Earth's interior structure, creating a detection shadow on the opposite hemisphere of the planet from the earthquake source regardless of the physical state of the core material",
        "S-waves are absorbed and converted entirely into thermal energy by the extreme temperatures and pressures found at depths greater than 2900 kilometers within the lower mantle transition zone, completely preventing any shear wave seismic energy from reaching recording stations located more than 104 degrees from the epicenter",
    ],
    22: [
        "The upward trends in both global average temperature and atmospheric carbon dioxide concentration since 1880 provide conclusive statistical proof of a direct causal relationship between the two variables, since any two datasets that show similar long-term directional trends over the same period are by definition causally connected without requiring additional mechanistic evidence or independent verification",
        "The observed correlation between rising temperature and rising CO2 concentrations is entirely coincidental because numerous other global variables including human population growth, total industrial output, and worldwide urbanization rates have also increased steadily since 1880, and no statistical method can reliably determine which among many simultaneously correlated variables is the actual underlying cause",
        "The correlation is scientifically meaningful only if every single annual data point in both the temperature and CO2 datasets shows a perfectly synchronized year-to-year increase, and any individual year where measured temperatures declined while CO2 continued rising would completely invalidate the entire hypothesized causal relationship between the two variables",
    ],
    23: [
        "The spreading rate cannot be determined from distance and age data alone because it requires direct real-time GPS measurement from seafloor instruments. Ocean floor age is limited to 180 million years because the Mid-Atlantic Ridge did not begin forming until that time, and all currently existing oceanic crust originated from that single initial rifting event rather than from any ongoing geological process",
        "Spreading rate is calculated by measuring the width of individual magnetic polarity stripes on the ocean floor and multiplying by the known duration of each magnetic reversal interval. Maximum ocean floor age is limited because basaltic oceanic crust chemically decomposes through prolonged exposure to corrosive seawater and completely dissolves after approximately 200 million years of continuous contact",
        "Average spreading rate equals the total width of the Atlantic Ocean divided by twice the age of Earth since oceanic spreading has been continuous throughout all of geological history. Ocean floor older than 180 million years has never been found simply because no deep-ocean drilling or seafloor sampling expeditions have yet explored the most remote and deepest portions of the major ocean basins worldwide",
    ],
    24: [
        "Both the water cycle and nitrogen cycle are driven entirely by physical and chemical processes without any requirement for biological organism involvement. Nitrogen gas dissolves directly into soil water through simple physical diffusion and is immediately absorbed by plant root systems in its molecular diatomic form without requiring any prior chemical transformation or biological mediation by specialized microorganisms in the soil community",
        "The water cycle operates through biological processes because plants actively pump liquid water from the soil through their vascular tissue and release it as water vapor through leaf stomatal transpiration. The nitrogen cycle is purely chemical because lightning strikes in the atmosphere provide sufficient energy to convert all required atmospheric nitrogen into plant-available nitrate compounds through inorganic oxidation reactions alone",
        "The fundamental distinction between the two cycles is temporal rather than mechanistic: water cycles rapidly through the Earth system on timescales of days to weeks through purely physical evaporation and precipitation processes, while nitrogen cycles extremely slowly on geological timescales of millions of years regardless of whether the transformation pathways involved are biological or purely abiotic chemical reactions",
    ],
    25: [
        "Both C-14 and K-40 dating methods are equally effective for materials of any age because the mathematical exponential decay equation governing radioactive transformation can be applied identically regardless of whether the specific isotope's characteristic half-life is measured in thousands of years or in billions of years, making the choice between methods purely a matter of laboratory convenience",
        "C-14 dating is preferred for ancient geological samples billions of years old because the extremely short half-life produces rapid measurable changes in parent-to-daughter isotope ratios that are easy to detect. K-40 is most useful for dating recent organic materials because its very long half-life ensures that easily detectable amounts of the parent isotope always remain present in young samples",
        "C-14 dating is limited to approximately 50,000 years not because of measurement sensitivity limitations but because the cosmic ray production rate of new C-14 atoms in the upper atmosphere has varied so dramatically and unpredictably over geological time that reliable calibration curves simply cannot be extended beyond that temporal range for any practical dating application",
    ],
    26: [
        "The current rate of species extinction is substantially lower than all five previously documented mass extinction events in the geological fossil record, and the widespread public concern about modern biodiversity loss is based primarily on the systematic misinterpretation of incomplete and taxonomically biased sampling data from limited field surveys",
        "The current extinction event is mechanistically identical to the end-Cretaceous mass extinction because both events were triggered by rapid atmospheric composition change, and like the asteroid impact event sixty-six million years ago, the current biodiversity crisis is entirely irreversible once a critical threshold of total species loss has been permanently exceeded",
        "Previous mass extinctions in the geological record eliminated only marine invertebrate species while leaving terrestrial vertebrate populations essentially unaffected, meaning the current crisis affecting primarily land-based mammals, birds, and amphibians represents an entirely unprecedented type of biodiversity loss event with no valid historical comparison",
    ],
    27: [
        "Large volumes of cold Arctic meltwater entering the North Atlantic would directly cool the ocean surface temperature, creating a localized thermal anomaly that physically blocks the passage of warm Gulf Stream water flowing northward from tropical latitudes and forces it to divert southward along the African continental coastline instead of reaching northern Europe",
        "Arctic ice meltwater contains high concentrations of dissolved minerals and suspended sediment particles that significantly increase surface water density and dramatically accelerate the rate of thermohaline conveyor belt circulation, transporting substantially more tropical heat energy to northern Europe and raising regional winter temperatures by several additional degrees",
        "Freshwater input from melting Arctic glaciers would raise global sea level sufficiently to flood the shallow continental shelf regions where thermohaline deep water formation currently takes place, physically eliminating the bathymetric conditions necessary for cold surface water to sink and initiate overturning circulation in the North Atlantic ocean basin",
    ],
    28: [
        "Quartz appears in different rock types because each type contains a chemically distinct variety of quartz with a fundamentally different internal crystal structure and molecular formula. Igneous quartz crystallizes in a hexagonal system, sedimentary quartz forms in an orthorhombic system, and metamorphic quartz develops a monoclinic system, each reflecting the unique physicochemical conditions of its specific formation environment",
        "Quartz forms exclusively through one single geological process of direct crystallization from cooling silica-rich magma and is subsequently transported into sedimentary and metamorphic environments through physical erosion and mechanical redeposition without undergoing any chemical alteration or structural transformation whatsoever. The mineral composition and internal crystal structure remain permanently identical regardless of geological setting",
        "Quartz identified in igneous rocks is the only true form of the mineral, crystallizing directly from silica-saturated magma chambers deep underground. The material identified as quartz in sedimentary sandstone and metamorphic quartzite is actually a different mineral species with a similar visual appearance but a distinct chemical composition and internal crystalline arrangement that forms through entirely separate geological mechanisms",
    ],
    29: [
        "The symmetrical depth profile results from the progressive accumulation of thick marine sediment deposits on the ocean floor with increasing distance from the ridge crest. Near the ridge where the crust is youngest, minimal sediment has had time to accumulate, while older crust farther away supports very thick sediment layers that weigh down the underlying oceanic plate and push it deeper",
        "The ridge stands higher than surrounding seafloor because continuous magma upwelling physically pushes the overlying crust upward at the active spreading center, and the gradual elevation decrease with increasing distance simply reflects the diminishing magnitude of the mechanical upward push force as the plate moves beyond the direct influence zone of the underlying mantle convection plume",
        "Ocean depth increases symmetrically away from the ridge because erosion from powerful deep ocean bottom currents preferentially removes volcanic material from the elevated ridge flanks and redeposits it as thick sediment layers in the deeper ocean basins located farther from the spreading center, gradually leveling the original seafloor topography over long geological time periods",
    ],
    30: [
        "The volcanic eruption releases massive quantities of carbon dioxide into the lower troposphere which dramatically amplifies the greenhouse effect over the following two decades, causing sustained global temperature increases rather than the decreases described in the scenario. The elevated temperatures then accelerate polar glacier melting and significantly increase the intensity of tropical cyclone systems across all major ocean basins, while agricultural impacts result from increased flooding and severe weather rather than any cooling effect whatsoever, since all large volcanic eruptions consistently warm the global climate",
        "The eruption deposits thick layers of volcanic ash and pyroclastic debris across the surrounding landscape within approximately one hundred kilometers of the volcanic vent, creating severe localized environmental damage to vegetation and water quality. However, the effects remain strictly confined to the immediately affected geographic area and do not propagate beyond the proximal zone because atmospheric transport processes are insufficient to distribute volcanic particulate material or sulfate aerosols across hemispheric or global distances, meaning crop failures and health impacts only occur in the region directly adjacent to the volcano",
        "Each environmental impact described in the scenario operates through a completely independent physical mechanism with no causal connection to the others or to the volcanic eruption itself. Temperature decreases are caused by coincidental reduced solar output, monsoon disruptions result from unrelated Pacific Ocean circulation changes, crop yield reductions stem from seasonal agricultural pest outbreaks, and the increase in respiratory illness is attributable entirely to concurrent regional industrial air pollution emissions rather than to any volcanic ash or aerosol particles released during the eruption event",
    ],
})

print("\nAll done! Fixed 65 giveaway questions across 3 files.")
