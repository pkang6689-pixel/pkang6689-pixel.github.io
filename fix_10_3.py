import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit10/Lesson10.3_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    4: [
        "Approximately 22.5 GW of installed generating capacity, making it the largest hydroelectric power station ever constructed in the world",
        "Roughly 10 GW of total installed electrical generating capacity spread across its network of turbine generators on the Yangtze River",
        "An estimated 50 GW of combined hydroelectric and thermal generating capacity when operating alongside its auxiliary coal-fired backup units"
    ],
    12: [
        "The natural migration patterns of native desert animal species as they move into new unfamiliar habitats in response to changing conditions",
        "The gradual geological formation of new desert landscapes through natural long-term tectonic uplift processes occurring over millions of years",
        "The progressive expansion and widening of sandy coastal beach environments along ocean shorelines due to natural wave erosion and sand deposition"
    ],
    14: [
        "The naturally occurring concentration of dissolved salt minerals found in standard ocean seawater across all of the world's major ocean basins",
        "The traditional food preservation technique of applying concentrated salt solutions to perishable food products to extend their shelf storage life",
        "The common winter road maintenance practice of spreading de-icing salt compounds on highway and street surfaces during freezing storm weather events"
    ],
    15: [
        "A sudden and dramatic increase in the rate of primary photosynthetic productivity across all trophic levels of an aquatic or terrestrial ecosystem",
        "The physical movement of flowing water through a sequential series of waterfalls cascading down from elevated mountain terrain to lower valleys",
        "The fundamental biochemical process of converting light energy into chemical energy during the photosynthesis reactions within plant chloroplasts"
    ],
    17: [
        "A condition of uniform consistent temperature throughout the entire water column from the surface to the bottom of the lake or reservoir body",
        "The artificial warming of water bodies caused by thermal pollution from industrial cooling water discharge from nearby power generation facilities",
        "The seasonal physical process of lake surface water freezing from the top surface layer progressively downward toward the deeper bottom sediments"
    ],
    19: [
        "A specialized guideline that applies exclusively to nuclear energy production facilities and has no relevance to any other industrial activity sectors",
        "A statutory insurance requirement mandating that all commercial companies must purchase comprehensive environmental damage liability coverage policies",
        "A regulatory principle that permanently delays and halts all proposed industrial activities until every conceivable risk has been reduced to absolute zero"
    ],
    22: [
        "A clear parallel to the Bhopal chemical disaster where an industrial facility released toxic gases that caused widespread casualties in surrounding neighborhoods",
        "A direct comparison to the Chesapeake Bay dead zone caused by nutrient pollution flowing from agricultural operations across a multi-state watershed drainage area",
        "A scenario that closely resembles the Deepwater Horizon oil spill where a catastrophic well blowout released millions of barrels of crude oil into ocean waters"
    ],
    23: [
        "Exclusively the direct monetary construction cost measured against the projected electricity revenue generated over the operational lifetime of the dam facility",
        "Only the total number of displaced residents compared against the total number of construction and operational jobs created by the hydroelectric dam project",
        "Solely the total clean electricity generating output of the dam compared against equivalent energy production potential from alternative solar panel installations"
    ],
    27: [
        "Environmental justice considerations including the impact on vulnerable populations, regulatory failures involving different safety standards between nations, corporate accountability for worker and community safety, long-term public health consequences, and the need for uniform international industrial safety regulations",
        "Exclusively the specific mechanical and structural engineering failure that caused the initial chemical leak without examining any broader systemic or policy factors",
        "Only the total estimated financial cost of environmental cleanup operations and monetary victim compensation payments without analyzing root causes or prevention"
    ],
    30: [
        "A detailed side-by-side comparison of environmental impacts on ecosystems, effects on local human communities, governance and jurisdictional challenges, attempted policy solutions and their effectiveness, and broader transferable lessons about managing shared natural resources",
        "Only a single narrow technological recommendation for solving each environmental problem without considering policy, governance, or community engagement factors",
        "Exclusively a comprehensive taxonomic list of all aquatic species affected in each ecosystem without analyzing causes, human impacts, or management responses"
    ]
}

for q in data['quiz_questions']:
    qn = q['question_number']
    if qn in fixes:
        wrong_idx = 0
        for opt in q['options']:
            if not opt['is_correct']:
                opt['text'] = fixes[qn][wrong_idx]
                wrong_idx += 1

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Fixed {len(fixes)} questions in Lesson10.3_Quiz.json")
