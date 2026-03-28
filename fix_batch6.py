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

# FILE 1: Lesson5.7_Quiz.json - Case Studies in Energy Policy
print("Fixing Lesson5.7_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit5/Lesson5.7_Quiz.json", {
    11: [  # What is a feed-in tariff?
        "A mandatory surcharge added to monthly electricity bills that funds transmission grid maintenance and infrastructure upgrades for all utility customers",
        "A government-imposed import duty on foreign-manufactured solar panels and wind turbines designed to protect domestic renewable energy equipment manufacturers",
        "A regulatory penalty charged to power companies that fail to meet annual electricity generation quotas established by their regional energy commission"
    ],
    16: [  # What is energy subsidy?
        "A standardized international tariff applied to cross-border electricity sales between neighboring countries under bilateral trade agreements",
        "A mandatory insurance premium that energy companies must pay to cover potential environmental damage from their power generation operations",
        "A consumer rebate program funded by utility companies that reimburses customers for purchasing energy-efficient household appliances and lighting"
    ],
    19: [  # What is the IPCC?
        "A multinational regulatory agency with binding legal authority to enforce emission reduction targets on individual nations under international treaty obligations",
        "A consortium of private energy corporations that collaboratively fund research into next-generation nuclear reactor designs and fusion energy technology",
        "A specialized division within the World Meteorological Organization responsible for issuing seasonal weather forecasts and long-range precipitation outlooks"
    ],
    20: [  # What is a green new deal?
        "A bilateral trade agreement between the European Union and United States that eliminates tariffs specifically on solar panels, wind turbines, and battery storage systems",
        "A standardized international certification label awarded to consumer products that meet verified benchmarks for sustainable sourcing and low-carbon manufacturing processes",
        "A voluntary corporate sustainability pledge through which companies publicly commit to purchasing carbon offset credits equal to their total annual operational emissions"
    ],
    21: [  # Denmark wind energy surplus - how addressed?
        "Denmark curtails all wind turbine output during high-production periods by electronically disconnecting generators from the grid to prevent dangerous frequency fluctuations",
        "Denmark converts all surplus wind electricity into hydrogen fuel through large-scale electrolysis plants, then stores the hydrogen in underground salt cavern facilities",
        "Denmark distributes excess wind-generated electricity directly to individual household battery storage systems installed as a mandatory requirement in all new construction"
    ],
    23: [  # California climate policies - what evidence to evaluate?
        "Historical records of annual wildfire acreage burned in California forests over the past century, compared to wildfire trends in neighboring western states with different land management practices",
        "The total number of registered electric vehicles in California compared to each other state, without adjusting for differences in population size, income levels, or urban density",
        "Public opinion survey results measuring voter satisfaction with state government environmental policies, collected from a representative sample of registered voters in each state"
    ],
    24: [  # Nuclear reconsideration for climate goals
        "European nations discovered previously unknown uranium deposits within their own borders, eliminating the need to import nuclear fuel from geopolitically unstable regions",
        "International nuclear safety standards were permanently relaxed after Fukushima, allowing construction of cheaper reactors with fewer redundant safety systems and backup cooling mechanisms",
        "Global natural gas reserves were completely exhausted by 2020, leaving nuclear fission as the only remaining option for baseload electricity generation in industrialized countries"
    ],
    25: [  # China coal + renewables simultaneously
        "China intentionally builds renewable energy installations solely as demonstration projects for foreign diplomatic purposes, with no connection to the domestic electricity grid system",
        "Chinese government policy mandates that each province must generate electricity from only one energy source, creating a patchwork of single-fuel regional grids across the country",
        "China's geographic location receives insufficient solar radiation and wind speeds to generate meaningful electricity from renewable sources, limiting their practical contribution"
    ],
    29: [  # UK Climate Change Act - addresses distant-target criticism
        "The act includes a provision allowing the government to indefinitely postpone emission reduction deadlines whenever economic growth falls below a specified annual threshold",
        "The act delegates all climate policy decisions entirely to private-sector corporations, which voluntarily set and enforce their own individual emission reduction targets",
        "The act establishes a single national emission reduction target for the year 2050 only, with no intermediate milestones, benchmarks, or accountability mechanisms in between"
    ],
    30: [  # Iceland vs Trinidad and Tobago - what explains Iceland's renewable success?
        "Iceland invested more money per capita in renewable energy research than Trinidad and Tobago, which is the sole reason for the difference in their energy profiles",
        "Trinidad and Tobago's tropical latitude receives insufficient solar radiation for viable renewable energy generation compared to Iceland's higher-latitude position",
        "Iceland's smaller geographic area makes renewable energy distribution far more efficient, while Trinidad and Tobago's larger land mass prevents effective grid connectivity"
    ]
})

# FILE 2: Lesson7.7_Quiz.json - AP Prep: Cross-Disciplinary Applications
print("Fixing Lesson7.7_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit7/Lesson7.7_Quiz.json", {
    5: [  # Correlation - correct way to describe on AP exams
        "Identify the variable with the larger numerical values as the independent cause and the smaller-valued variable as the dependent effect in all cases",
        "Present only the data points that confirm the expected relationship while excluding any outliers or contradictory observations from the final analysis",
        "Calculate the arithmetic mean of both variables and report whether the averages are similar or different without referencing any directional trend"
    ],
    7: [  # Ocean acidification chemistry concept
        "The thermal expansion coefficient of seawater molecules as ocean temperatures steadily rise above historical averages",
        "The rate at which dissolved sodium chloride concentrations increase due to accelerated continental rock weathering processes",
        "The photosynthetic conversion of dissolved nitrogen compounds into organic biomass by surface-dwelling marine phytoplankton"
    ],
    8: [  # Nitrogen cycle - which disciplines?
        "Stellar nucleosynthesis, planetary geology, and theoretical astrophysics",
        "Quantum mechanics, semiconductor physics, and materials engineering",
        "Marine vertebrate anatomy, deep-sea oceanography, and plate tectonics"
    ],
    9: [  # Describe AND explain on AP exams
        "Drawing a clearly labeled diagram with arrows and annotations is sufficient to earn full credit without any written text explanation",
        "Restating the question prompt in different words and adding a personal anecdote about the topic to demonstrate familiarity with the concept",
        "Listing every relevant scientific vocabulary term from the unit in alphabetical order to demonstrate comprehensive knowledge of the course material"
    ],
    10: [  # Water cycle cross-disciplinary application
        "Increased irrigation in agricultural regions accelerates aquifer depletion, which strengthens tropical cyclone formation patterns and increases annual hurricane frequency across all ocean basins",
        "Urban heat islands in metropolitan areas alter the chemical composition of precipitation, converting normal rainfall into acidic solutions that accelerate the weathering of all exposed limestone surfaces",
        "Glacial retreat in polar regions increases global albedo by exposing lighter-colored land surfaces, which reflects additional solar radiation back to space and accelerates atmospheric cooling worldwide"
    ],
    12: [  # What is the greenhouse effect?
        "The gradual increase in atmospheric oxygen concentration caused by accelerating rates of global photosynthesis in tropical rainforest ecosystems and oceanic phytoplankton blooms",
        "The process by which Earth's magnetic field deflects charged solar wind particles away from the atmosphere, thereby preventing the upper atmospheric layers from overheating",
        "The periodic oscillation in global ocean circulation patterns that redistributes thermal energy between the equatorial and polar regions on a multi-decadal timescale cycle"
    ],
    14: [  # Difference between weather and climate
        "Weather refers exclusively to precipitation and humidity measurements while climate encompasses only temperature and wind speed recordings taken at standardized meteorological stations",
        "Weather and climate are functionally identical terms that both describe average atmospheric conditions but are used interchangeably depending on which scientific discipline is reporting the data",
        "Weather describes atmospheric conditions observed specifically over ocean surfaces while climate refers to atmospheric conditions measured exclusively over continental land masses"
    ],
    18: [  # What does pH measure?
        "The total concentration of dissolved mineral salts and trace metals present in a natural water body, expressed as parts per million on a standardized scale",
        "The partial pressure of dissolved atmospheric gases within a liquid sample, reported in units of millimeters of mercury at standard laboratory temperature",
        "The relative electrical conductivity of a solution determined by measuring current flow between two submerged electrodes at a standardized temperature of twenty-five degrees"
    ],
    20: [  # What is an ecological footprint?
        "A quantitative index measuring the total number of distinct species found within a defined geographic area, used to compare biodiversity levels across different regional ecosystems",
        "A standardized laboratory assessment of the decomposition rate of organic waste materials under controlled aerobic conditions, used to evaluate municipal composting program efficiency",
        "A geographical mapping technique that tracks the seasonal migration routes and territorial range of keystone predator species across continental landscapes using satellite telemetry"
    ],
    21: [  # CO2 + temperature + ocean pH - cross-disciplinary connection
        "Rising ocean temperatures increase evaporation rates that concentrate dissolved salts in surface waters, raising pH through alkaline mineral precipitation and stimulating coral reef expansion",
        "Decreased solar radiation output during the current solar minimum cycle has reduced photosynthetic activity in marine phytoplankton, shifting the oceanic carbon equilibrium and lowering overall surface pH",
        "Natural volcanic emissions of sulfur dioxide into the upper atmosphere create sulfate aerosols that scatter incoming solar radiation and independently reduce both global temperatures and ocean alkalinity"
    ],
    22: [  # Ice-albedo feedback loop
        "Melting polar ice releases trapped methane hydrates from permafrost and ocean sediments, which directly cools the lower atmosphere by absorbing infrared radiation and re-emitting it toward space in a stabilizing negative feedback loop",
        "As ice melts the increased freshwater input into polar oceans disrupts thermohaline circulation patterns, which redistributes equatorial heat more evenly and ultimately produces a net cooling effect across high-latitude regions worldwide",
        "Polar ice loss increases the total volume of liquid ocean water, which raises sea level and increases the ocean surface area available for evaporation, producing more cloud cover that reflects incoming solar radiation and counteracts the initial warming signal"
    ],
    23: [  # Eutrophication sequence - fertilizer to fish kill
        "Fertilizer nitrogen volatilizes into ammonia gas that rises into the upper atmosphere, depletes stratospheric ozone, increases ultraviolet radiation reaching the lake surface, and causes sunburn in fish populations",
        "Agricultural phosphorus binds permanently to clay soil particles in the watershed and never reaches surface water bodies, so fertilizer application has no measurable effect on downstream aquatic ecosystem health",
        "Rainfall dissolves fertilizer salts that flow into the lake and directly increase water salinity beyond the physiological tolerance range of freshwater fish species, causing lethal osmotic stress"
    ],
    24: [  # Acid rain cross-disciplinary mechanism
        "Coal combustion releases particulate carbon soot that is carried by wind currents and settles directly onto remote lake surfaces, where it absorbs solar radiation and raises water temperatures beyond fish tolerance limits",
        "Sulfur dioxide from power plant emissions reacts with stratospheric ozone to form sulfur trioxide, which permanently depletes the protective ozone layer and increases ultraviolet radiation damage to aquatic organisms in exposed water bodies",
        "Industrial nitrogen oxide emissions dissolve into nearby river systems at the point of release and flow downstream through connected waterways until reaching distant lakes, where they accumulate and directly poison fish through gill membrane absorption"
    ],
    25: [  # Great Oxidation Event - cross-disciplinary
        "Cyanobacteria evolved photosynthetic pigments that absorbed all available solar radiation, dramatically cooling Earth's surface temperature and triggering a global glaciation event that covered the entire planet in ice",
        "Photosynthetic cyanobacteria consumed all dissolved carbon dioxide from the ancient oceans, causing a catastrophic collapse of the marine food web that eliminated most early multicellular organisms from the fossil record",
        "Cyanobacteria released large quantities of methane gas through their metabolic processes, which accumulated in the atmosphere and created an extreme greenhouse effect that raised global temperatures by over fifty degrees"
    ],
    26: [  # Global fish catch decline - cross-disciplinary analysis
        "Fish populations naturally follow predictable boom-and-bust population cycles on a fifty-year timescale, and the observed decline since the 1980s represents the expected trough phase that will reverse without intervention",
        "Advances in fishing vessel navigation technology have improved fleet efficiency so dramatically that fewer boats can now catch the same tonnage, creating the statistical illusion of declining catches in aggregate data",
        "Global fish populations have actually increased substantially since the 1980s, but international reporting agencies have systematically underestimated catch totals due to outdated survey methodologies and incomplete data"
    ],
    27: [  # Mangroves reduce coastal flood damage - cross-disciplinary explanation
        "Mangrove forests produce airborne chemical compounds that suppress cyclone formation in nearby ocean waters, thereby reducing the frequency and intensity of storm events that would otherwise cause severe coastal flooding",
        "Mangrove root systems extend deep enough into bedrock to anchor the shoreline against tectonic subsidence, which is the primary geological cause of increased coastal flooding in tropical and subtropical regions worldwide",
        "Mangrove forests lower regional air temperatures through extensive canopy evapotranspiration, which reduces the atmospheric moisture available for precipitation and thereby decreases the total volume of rainfall reaching coastal flood zones"
    ],
    28: [  # Solar farm in desert - cross-disciplinary concern
        "Desert regions receive insufficient direct solar radiation for photovoltaic energy generation because persistent cloud cover and atmospheric dust scatter most incoming sunlight before it reaches ground-level panel arrays",
        "Solar panel manufacturing requires rare earth elements that can only be mined in tropical rainforest regions, so building desert solar farms actually accelerates deforestation in distant equatorial countries through supply chain demand",
        "Large-scale solar installations generate powerful electromagnetic fields that interfere with migratory bird navigation systems, disrupt underground aquifer flow patterns, and destabilize local atmospheric pressure gradients across the entire region"
    ],
    29: [  # Volcanic cooling mechanism - cross-disciplinary chain
        "Volcanic eruptions release massive volumes of liquid water stored within magma chambers directly into the upper atmosphere, forming persistent cloud layers that reflect incoming solar radiation for decades",
        "Large eruptions physically eject fine rock debris into stable orbital trajectories around Earth, creating a temporary ring of volcanic material that blocks a significant portion of incoming solar radiation for years",
        "Volcanic lava flows cool ocean surface temperatures by direct contact as molten rock enters coastal waters, and the resulting thermal shock propagates across entire ocean basins through deep-water circulation currents"
    ],
    30: [  # Mountain ecosystem research plan - cross-disciplinary design
        "Conduct a single aerial photograph survey of the mountain summit during peak summer conditions and compare the resulting image to a historical photograph from approximately the same date and vantage point taken fifty years earlier",
        "Install one automated weather station at the mountain base that records temperature every hour for one calendar year, then extrapolate conditions at all higher elevations using a standard atmospheric lapse rate equation",
        "Collect rock samples from three different elevations on the mountain and analyze their mineral composition in a laboratory to determine whether geological substrate differences explain observed variations in vegetation cover"
    ]
})

print("Batch 6 complete!")
