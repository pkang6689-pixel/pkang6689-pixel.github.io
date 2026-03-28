import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit4/Lesson4.6_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    2: [
        "Significant improvements in downstream water quality and increased fish populations throughout the Yangtze River basin",
        "Minor cosmetic damage to the dam structure that was repaired within the first year of operation at minimal cost",
        "A net positive effect on regional biodiversity by creating new wetland habitats along the reservoir shoreline"
    ],
    3: [
        "Natural underground springs continuously refilling the aquifer at rates that far exceed any withdrawals by farmers in the region",
        "Government overregulation that prevented farmers from accessing the abundant water resources available beneath the Great Plains",
        "An increase in regional precipitation patterns that has kept aquifer levels stable despite decades of heavy agricultural pumping"
    ],
    4: [
        "A significant reduction in global hunger without any negative environmental side effects or increased chemical dependency",
        "The elimination of all synthetic pesticide and fertilizer use across developing nations through natural farming methods alone",
        "A complete restoration of soil fertility and biodiversity in regions where high-yield crop varieties were widely introduced"
    ],
    5: [
        "A thriving island society that maintained sustainable forestry practices and preserved its natural resources for centuries",
        "A natural volcanic eruption that destroyed all vegetation and forced the population to relocate to nearby island chains",
        "A model of successful resource management where islanders developed renewable alternatives before forests were exhausted"
    ],
    6: [
        "Approximately 50 million gallons over twelve months, contained entirely within a five-mile radius of the drilling platform",
        "Roughly 5 million gallons over a single weekend, quickly cleaned up using advanced dispersant technology without lasting impact",
        "About 500,000 gallons released over several hours, with natural ocean currents dispersing the oil before it reached any shore"
    ],
    8: [
        "International fishing agreements successfully prevented overharvesting by establishing strict and enforceable quotas for all nations",
        "Only a single small-scale fishing company operated in the region, making coordination and sustainable management relatively simple",
        "Advanced fish-farming technology replaced all wild-caught cod long before populations showed any signs of significant decline"
    ],
    9: [
        "A small community-based irrigation project that serves a single province with minimal environmental or social consequences",
        "A natural geological process that gradually redistributes groundwater from southern aquifers to northern river basins over time",
        "An international aid program funded entirely by foreign governments that constructed wells in drought-affected northern villages"
    ],
    12: [
        "A strict regulatory framework where the government assumes direct ownership and management control of all private agricultural land",
        "A penalty-based system that imposes heavy financial fines on landowners who cut down any trees or alter natural vegetation cover",
        "A government-run admission fee program that charges visitors entrance fees to access public parks and protected wilderness areas"
    ],
    13: [
        "A legal standard requiring absolute scientific proof of harm before any regulatory action can be taken against a potentially dangerous activity",
        "A principle stating that economic development should always take priority over unproven environmental or public health concerns",
        "A guideline mandating that all industrial activities must wait for damage to occur before implementing corrective safety measures"
    ],
    14: [
        "Large-scale commercial tourism to popular beach destinations that focuses primarily on maximizing hotel occupancy and resort revenue",
        "International travel packages that prioritize luxury accommodations and entertainment without considering local environmental impacts",
        "Urban tourism programs that concentrate visitors in major metropolitan centers and cultural attractions far from natural environments"
    ],
    15: [
        "All direct and indirect costs that are already fully reflected in the market price of every product sold to consumers today",
        "The total gross revenue generated from the sale of extracted natural resources on domestic and international commodity markets",
        "Formal trade agreements between nations that establish tariffs and quotas on the import and export of natural resource commodities"
    ],
    16: [
        "The maximum total weight of cargo and freight that a commercial transportation vehicle can legally carry on public highways",
        "The total volume of goods and raw materials that an industrial shipping vessel is designed to safely hold during ocean transit",
        "The combined acreage of cultivated cropland and grazing pasture within the legal property boundaries of a farming operation"
    ],
    17: [
        "An economic theory suggesting that countries with large reserves of valuable natural resources always achieve rapid and sustained prosperity",
        "A mystical or superstitious belief held by some traditional mining communities about curses placed on valuable underground mineral deposits",
        "A geological process describing the gradual and inevitable exhaustion of all extractable mineral and energy resources across the planet"
    ],
    19: [
        "Exclusively elected government officials who hold formal legislative authority over natural resource policy and regulatory decisions",
        "Only members of registered environmental advocacy organizations who actively campaign for conservation and habitat protection goals",
        "Specifically those individuals who file legal ownership claims to mineral extraction rights on designated public mining territories"
    ],
    20: [
        "A narrow financial calculation that only considers the direct monetary profits generated from extracting and selling natural resources",
        "An approach that deliberately excludes long-term environmental degradation costs from economic calculations to simplify decision-making",
        "A focused accounting method that only calculates the immediate expenses of cleaning up pollution after environmental damage has occurred"
    ],
    22: [
        "The original construction expenses for building the offshore drilling platform and the subsequent cost of replacing the damaged equipment",
        "Unrelated corporate financial metrics that had no meaningful connection to the environmental damage caused by the oil spill in the Gulf",
        "The total annual revenue that BP generated from all of its worldwide petroleum operations during the fiscal year the spill occurred"
    ],
    23: [
        "A general principle that all farmers everywhere should receive government subsidies regardless of their land management decisions or practices",
        "A conclusion reached by most economists that government spending on forest conservation programs has no measurable economic return whatsoever",
        "A widely accepted view among resource economists that standing forests provide no quantifiable economic benefits to society at any scale"
    ],
    24: [
        "A complete rejection of all modern agricultural science and technology in favor of returning exclusively to pre-industrial farming methods",
        "An exact duplication of the original Green Revolution approach using the same synthetic fertilizers and monoculture crop strategies",
        "A wholesale conversion of all existing farmland into urban residential and commercial development zones to reduce agricultural pressure"
    ],
    25: [
        "Scientific evidence demonstrating that mining operations produce no measurable effects on downstream water quality or aquatic ecosystems",
        "An example of equitable resource management where environmental costs and economic benefits are shared fairly among all affected parties",
        "A demonstration that all communities located near active mining operations receive proportional economic benefits from resource extraction"
    ],
    26: [
        "The fact that Dubai possesses essentially unlimited reserves of natural gas that will never be depleted regardless of consumption rates",
        "A common misconception that the Persian Gulf contains freshwater rather than the highly saline seawater that actually fills the basin",
        "A widely supported scientific conclusion that large-scale industrial desalination processes create absolutely no environmental problems"
    ],
    27: [
        "A demonstration that Easter Island possessed functionally unlimited natural resources that could never be fully exhausted by any population",
        "Historical evidence suggesting that Easter Island was never inhabited by any significant human population before European contact occurred",
        "Archaeological findings showing that Easter Island civilization possessed advanced industrial technology comparable to modern societies today"
    ],
    29: [
        "A proven model of permanently sustainable agricultural practice that can be replicated indefinitely without any environmental consequences",
        "Clear evidence that the Indian subcontinent possesses unlimited underground freshwater reserves that cannot be depleted by irrigation pumping",
        "A scientific demonstration that intensive irrigation agriculture has no measurable impact on regional groundwater levels or aquifer recharge"
    ],
    30: [
        "Simply describe the basic facts of what happened in each case study without any deeper analysis of causes or broader environmental lessons",
        "Only memorize and recite the names, geographic locations, and dates associated with each of the major environmental case studies discussed",
        "Focus exclusively on memorizing specific dates, map coordinates, and location names associated with each environmental disaster or event"
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

print(f"Fixed {len(fixes)} questions in Lesson4.6_Quiz.json")
