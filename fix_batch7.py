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

# FILE 1: Lesson9.2_Quiz.json - Feedback Loops (Positive & Negative)
print("Fixing Lesson9.2_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit9/Lesson9.2_Quiz.json", {
    13: [  # What is homeostasis?
        "A gradual shift in system conditions that accelerates over time due to compounding external factors",
        "A specific category of positive feedback loop that generates beneficial environmental outcomes",
        "The predictable final stage that all Earth systems inevitably reach at the end of their evolutionary cycle"
    ],
    15: [  # What is a tipping point?
        "The specific temperature at which negative feedback mechanisms reach their peak operational effectiveness",
        "A periodic fluctuation in the Sun's energy output that drives natural cycles of warming and cooling",
        "The long-term statistical average of global surface temperature measured across all monitoring stations"
    ],
    16: [  # What does 'dynamic equilibrium' mean?
        "A system that oscillates unpredictably between extreme states without any stabilizing mechanism",
        "A system that has ceased all internal processes and reached a state of complete physical motionlessness",
        "A condition in which all active feedback mechanisms within a system operate as positive reinforcement"
    ],
    18: [  # What is the weathering-CO2 feedback?
        "A process that operates exclusively within ocean basins through marine chemical precipitation reactions",
        "The physical erosion of rock formations by wind and precipitation patterns during severe weather events",
        "A positive feedback mechanism that continuously increases atmospheric carbon dioxide concentrations"
    ],
    20: [  # What is cloud feedback in climate science?
        "The straightforward cooling effect that all cloud types uniformly produce by reflecting incoming solar radiation",
        "An atmospheric phenomenon that operates independently of surface temperature changes across all regions",
        "The straightforward warming effect that all cloud types uniformly produce by trapping outgoing thermal radiation"
    ],
    21: [  # Arctic permafrost vs plant growth - which dominates?
        "Only the positive permafrost-methane feedback is currently active in Arctic regions, with no competing processes observed",
        "Only the negative vegetation feedback is currently active in Arctic regions, with no competing processes observed",
        "The two competing feedback processes cancel each other with mathematical precision, resulting in zero net change"
    ],
    22: [  # Thermostat analogy to silicate weathering
        "The two systems operate on fundamentally different physical principles and share no meaningful conceptual relationship",
        "Both systems function as positive feedback loops that continuously amplify warming trends without any self-regulation",
        "The home thermostat represents a positive feedback mechanism that amplifies temperature change until external limits"
    ],
    23: [  # Boreal forest competing feedbacks - how to model?
        "Assume the competing carbon release and albedo change effects perfectly cancel in every scenario at all times",
        "Only include the positive carbon-release feedback in the model while excluding the negative albedo-change feedback",
        "Exclude both feedback processes from the model since their complexity makes accurate simulation impossible"
    ],
    25: [  # Warmer oceans absorb less CO2 - why concerning?
        "The reduced absorption rate has no feedback effect on atmospheric greenhouse gas concentrations or global temperature",
        "Warmer ocean temperatures actually increase dissolved gas solubility, allowing oceans to absorb substantially more CO2",
        "The reduced ocean uptake functions as a negative feedback mechanism that effectively slows the rate of atmospheric warming"
    ],
    27: [  # Cloud feedback uncertainty
        "Clouds form at spatial scales too small for any current or future observational satellite instruments to detect reliably",
        "Clouds exert no measurable influence on Earth's radiative energy balance at either regional or global atmospheric scales",
        "The scientific community has fully resolved all uncertainties associated with cloud feedback in recent climate assessments"
    ],
    28: [  # Natural negative feedbacks won't prevent climate change
        "Earth's climate system contains no natural negative feedback mechanisms that could counteract any temperature perturbation",
        "Negative feedback mechanisms respond instantaneously to any perturbation and can neutralize even the largest changes immediately",
        "The student's reasoning is scientifically accurate because natural self-correcting mechanisms will fully offset emissions"
    ],
    30: [  # Lake eutrophication - identify feedback types
        "Both Scenario A and Scenario B represent negative feedback loops that promote ecosystem stability through self-correction",
        "Both Scenario A and Scenario B represent positive feedback loops that amplify the initial environmental disturbance",
        "Neither scenario involves any type of feedback mechanism because the described processes are strictly one-directional"
    ]
})

# FILE 2: Lesson9.3_Quiz.json - Modeling Climate Systems
print("Fixing Lesson9.3_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit9/Lesson9.3_Quiz.json", {
    1: [  # What is a climate model?
        "A scaled-down physical replica of Earth's atmosphere and oceans constructed in a controlled laboratory environment",
        "A detailed cartographic map showing current temperature readings at weather stations distributed across the globe",
        "A short-range forecast of weather conditions for the upcoming week based on current atmospheric observations"
    ],
    2: [  # What is the difference between weather and climate?
        "Weather phenomena occur exclusively in tropical latitudes while climate patterns are limited to polar regions",
        "Climate conditions fluctuate on a daily basis while weather patterns remain relatively constant over extended periods",
        "There is no scientifically meaningful distinction between the two terms and they can be used interchangeably"
    ],
    8: [  # What does the IPCC do?
        "Operates and maintains a worldwide network of automated weather monitoring stations and satellite systems",
        "Directly regulates and controls the global climate system through international policy enforcement mechanisms",
        "Designs, develops, and commercially manufactures the computer hardware used to run all global climate models"
    ],
    11: [  # What is a General Circulation Model (GCM)?
        "A ground-based weather radar system used to track the movement of individual storm cells across regional airspace in real time",
        "A simplified two-dimensional graphical illustration of the major surface ocean current pathways across Earth's ocean basins",
        "A statistical model of daily human commuting and transportation circulation patterns within large metropolitan urban areas"
    ],
    16: [  # What is an emission scenario?
        "A standardized regulatory framework established by national governments to set legal limits on industrial air pollutant emissions",
        "A real-time instrumental measurement of current atmospheric pollution concentrations at a single ground-based monitoring site",
        "A comprehensive historical database compiling all recorded greenhouse gas emission measurements from previous decades only"
    ],
    20: [  # What is an ensemble model run?
        "Repeated execution of the exact same climate model configuration with identical parameter values to verify computational consistency",
        "A collaborative interdisciplinary research group composed of musicians and climate scientists studying acoustic atmospheric patterns",
        "A single simulation run of one individual climate model using one specific set of initial conditions and parameter assumptions"
    ],
    24: [  # Policymaker says models are useless since they can't predict a specific day
        "Acknowledge that the criticism is fully valid and confirm that climate models can in fact predict exact daily temperature values for any future date with high precision",
        "Concede that the policymaker is entirely correct and that climate models provide no useful information whatsoever for infrastructure planning or policy decisions",
        "Recommend that the scientific community discontinue all climate modeling research programs since the models cannot achieve daily forecast-level temporal accuracy"
    ],
    26: [  # Agricultural company drought projections
        "Disregard the model projections entirely because the inherent uncertainty in climate science makes all long-term projections unreliable for practical decisions",
        "Delay all adaptation planning until the projected drought conditions actually materialize and begin directly affecting current crop yields in the region",
        "Immediately cease all agricultural operations in the region and permanently relocate farming activities to a different climate zone with higher projected rainfall"
    ],
    27: [  # Early models matched observations
        "The agreement between early model projections and subsequent observations is merely a statistical coincidence with no scientific significance",
        "The close match between predictions and observations proves that climate models are mathematically perfect and contain no remaining uncertainty",
        "The agreement indicates that all specific future model predictions will prove exactly correct down to the decimal place at every spatial location"
    ],
    29: [  # Emission scenarios produce different projections - why?
        "Each emission scenario applies fundamentally different physical laws and equations of thermodynamics within the model calculation framework",
        "The choice of emission scenario has no measurable influence on the resulting temperature projections produced by the climate model simulation",
        "Climate models generate essentially random temperature projections that vary between runs regardless of the emission scenario used as input data"
    ]
})

# FILE 3: Lesson9.7_Quiz.json - Applications in Environmental Engineering
print("Fixing Lesson9.7_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/IntegratedScienceLessons/Unit9/Lesson9.7_Quiz.json", {
    4: [  # Catalytic converter reduces what pollutants?
        "Engine noise and mechanical vibration transmitted through the exhaust system to the vehicle body",
        "Only the carbon dioxide produced by complete combustion of hydrocarbon fuel in the engine cylinders",
        "Microscopic tire rubber particles and brake dust shed from wheel components during vehicle operation"
    ],
    19: [  # What is a Superfund site?
        "An exceptionally well-funded private construction project that has received multiple rounds of venture capital investment for its development phase",
        "A secure federal government facility where surplus tax revenues and emergency budget reserve funds are stored in protected underground vaults",
        "A large-scale fundraising event organized annually by national environmental advocacy organizations to generate donations for conservation projects"
    ],
    20: [  # What is non-point source pollution?
        "Contamination originating from a single identifiable industrial factory discharge pipe that releases effluent directly into a receiving water body",
        "A category of pollution that occurs exclusively within arid desert environments due to wind-driven redistribution of naturally occurring mineral particulates",
        "A theoretical classification of pollution that produces no measurable environmental impact because its concentrations remain below analytical detection limits"
    ],
    21: [  # Nitrate in river - source and solution
        "Leaking underground industrial chemical storage tanks at a nearby manufacturing facility; install a concrete containment dam across the river to trap contaminants",
        "Coastal saltwater intrusion into the freshwater river system driven by tidal forces; increase the rate of groundwater extraction from wells along the riverbank",
        "Naturally occurring volcanic mineral dissolution from upstream geothermal hot springs; no engineering intervention is possible for naturally occurring contamination"
    ],
    23: [  # CSO comprehensive solution
        "Instruct all residents connected to the combined sewer system to minimize household water consumption during major rainfall events to reduce total sewer flow volume",
        "Permanently decommission and seal the entire combined sewer system infrastructure, redirecting all wastewater and stormwater to surface channels and open drainage ditches",
        "Simply replace all existing sewer pipes throughout the system with larger-diameter pipes to increase the total volumetric capacity of the combined collection network"
    ],
    25: [  # Landfill design comparison
        "Neither design meets minimum environmental standards because all municipal solid waste should be processed through high-temperature thermal incineration instead of burial in landfills",
        "Design A is superior because simpler engineering configurations are inherently more reliable, easier to maintain, and less likely to experience the mechanical or structural failures that plague complex systems",
        "Design A is the better option because methane gas collection systems require excessive capital investment that cannot be justified by the modest revenue generated from recovered energy"
    ],
    26: [  # Factory meets BOD limits but still causing oxygen sags
        "Discontinue all downstream dissolved oxygen monitoring programs since the discharge already complies with existing regulatory permit requirements for effluent quality",
        "Increase the total volume of wastewater discharged from the treatment plant during each release cycle to achieve greater dilution of organic constituents in the receiving stream",
        "Physically trap and relocate all fish populations from the affected downstream reach to locations upstream of the factory's wastewater discharge outfall structure"
    ],
    27: [  # Acid mine drainage passive treatment
        "Extracting all contaminated water from the stream and transporting it by pipeline to a fully equipped active chemical treatment facility located in a neighboring state",
        "Filling the entire abandoned underground mine complex with bulk Portland cement and concrete aggregate to permanently seal all remaining acid-generating mineral surfaces from further contact with water",
        "Taking no remedial action and allowing the acid mine drainage to disperse and attenuate naturally over time through dilution and downstream chemical weathering processes"
    ],
    28: [  # Indoor air quality VOC solution
        "Permanently seal all windows and exterior ventilation openings throughout the building to completely prevent outdoor air pollutants from entering the indoor environment",
        "Apply additional coats of the same conventional paint products that originally caused the elevated volatile organic compound concentrations in the indoor air space",
        "Relocate all classroom instruction and administrative activities to permanent outdoor facilities on the school grounds to eliminate all indoor air quality exposure"
    ],
    29: [  # Island freshwater + sea level rise solution
        "Arrange long-term contracts to import all required freshwater supplies by ocean tanker ship from the nearest continental mainland port facility",
        "Construct a continuous reinforced concrete seawall around the entire island perimeter to physically block all seawater intrusion into the coastal aquifer system",
        "Accelerate the rate of groundwater extraction from the coastal aquifer to remove as much freshwater as possible before advancing saltwater contamination reaches the wells"
    ],
    30: [  # LCA plastic vs cotton bags - policy recommendation
        "Disregard the life cycle assessment findings entirely because the methodology is too complicated for policymakers and the general public to interpret accurately",
        "Implement an immediate regulatory ban on both single-use plastic bags and reusable cotton bags because the assessment demonstrates that both product types generate unacceptable environmental impacts",
        "Consider only the production-phase environmental impacts and recommend continued use of single-use plastic bags because they require fewer resources to manufacture"
    ]
})

print("Batch 7 complete!")
