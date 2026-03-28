import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit9/Lesson9.5_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    1: [
        "Freiburg has implemented only an effective municipal recycling program but has not addressed transportation, energy, or building efficiency",
        "Freiburg has adopted only one significant environmental policy focused exclusively on promoting rooftop solar panel installations citywide",
        "Freiburg has enacted a comprehensive ban prohibiting all private automobiles from entering any part of the entire metropolitan city area"
    ],
    3: [
        "Approximately 50% of electricity comes from a mix of fossil fuels and renewables, with significant coal and natural gas generation remaining",
        "Roughly 25% of the national electricity supply is generated from renewable sources, with the remainder coming from imported petroleum fuels",
        "About 75% of electricity generation comes from renewable sources, with the remaining quarter still dependent on fossil fuel thermal plants"
    ],
    5: [
        "A government-imposed financial penalty system that levies heavy taxes on all imported timber products entering the national marketplace",
        "A punitive enforcement mechanism that imposes substantial monetary fines on individual landowners who cut down any trees on their property",
        "A tourism revenue program that directly compensates international visitors with cash payments for choosing to visit national park destinations"
    ],
    6: [
        "Bhutan exclusively uses narrow environmental quality metrics that measure only air pollution, water contamination, and deforestation rates across the country",
        "Bhutan relies solely on traditional per capita income measurements to track economic development and material standard of living improvements",
        "Bhutan measures national progress using only the conventional economic growth rate indicator expressed as annual percentage change in gross domestic product"
    ],
    8: [
        "Singapore has implemented only improvements to its public mass transit rail and bus system without addressing water, buildings, or urban design",
        "Singapore has constructed only one small experimental green building as a showcase project without scaling sustainable design across the city",
        "Singapore has developed only a single water recycling program with no other notable sustainability innovations in urban planning or architecture"
    ],
    12: [
        "Rwanda's plastic bag ban only demonstrates that strict environmental restrictions inevitably harm economic activity and business development",
        "The ban proves that comprehensive plastic regulations can only succeed in wealthy industrialized countries with advanced waste management infrastructure",
        "Rwanda's approach shows that only severe punitive enforcement measures without any public education component can reduce single-use plastic consumption"
    ],
    17: [
        "An exclusive premium luxury bus service designed specifically for wealthy daily commuters traveling between affluent suburban areas and downtown offices",
        "A conventional municipal bus route system that operates on a limited schedule only during weekday morning and evening peak rush hour commuting periods",
        "A standard public bus route operating on shared traffic lanes with no special features, priority signaling, or infrastructure to improve travel times"
    ],
    18: [
        "A straightforward opinion survey instrument that simply measures how happy or satisfied individual people report feeling about their daily personal lives",
        "A national tourism industry marketing slogan and promotional branding campaign used exclusively by Bhutan to attract international visitors and travel revenue",
        "A conventional macroeconomic indicator that measures total national economic output in exactly the same way as traditional gross domestic product calculations"
    ],
    21: [
        "Focusing exclusively on constructing additional multi-story parking garage structures downtown to attract more automobile drivers to the commercial center",
        "Implementing an immediate and total prohibition on all private motor vehicles throughout the entire city without any phase-in period or alternative transit",
        "Concentrating all available municipal sustainability funding on building an exact replica of Freiburg's rooftop solar panel infrastructure and nothing else"
    ],
    23: [
        "The island nation should invest exclusively in large-scale seawater desalination technology because water recycling systems are far too technically complex",
        "Singapore's comprehensive water recycling system is fundamentally impossible to implement or adapt anywhere else because of its prohibitively high total cost",
        "The most practical solution is for the island to simply arrange long-term contracts to import all of its freshwater supply by tanker ship from the mainland"
    ],
    24: [
        "Gross domestic product is the only reliable and comprehensive measure of national progress and no additional well-being indicators are needed to supplement it",
        "A comprehensive framework inspired by Gross National Happiness would ultimately produce results and conclusions identical to conventional GDP growth analysis",
        "Gross National Happiness frameworks only measure vague subjective happiness feelings through surveys and have no practical policy applications for governance"
    ],
    25: [
        "The landlocked African country should purchase and import geothermal drilling equipment and power generation technology directly from Iceland for deployment",
        "Absolutely nothing useful can be learned from Iceland's experience because the landlocked African country has no volcanic geology or geothermal energy resources",
        "Only countries located on active volcanic geological formations along tectonic plate boundaries can successfully pursue any form of sustainable renewable energy"
    ],
    27: [
        "The city should focus exclusively on building expensive state-of-the-art modern waste treatment and incineration facilities funded by international development loans",
        "The city should implement strict product bans without providing any alternative livelihood support for the thousands of informal waste workers who depend on collection",
        "The city should rely solely on implementing heavy financial penalties and fines for littering without investing in any complementary waste collection infrastructure"
    ],
    28: [
        "Any country anywhere in the world can immediately achieve carbon-negative status simply by copying and implementing Bhutan's constitutional forest coverage mandate",
        "Bhutan's comprehensive sustainability model offers absolutely no transferable lessons or applicable principles for any other country in any different context",
        "Bhutan's sustainability achievements are solely attributable to its monarchical form of government and cannot be replicated under any other political system or structure"
    ],
    30: [
        "The planner should only attempt to replicate Freiburg's specific car-free neighborhood model exactly as it was originally designed for a European cultural context",
        "The planner should focus exclusively on implementing Bhutan's Gross National Happiness measurement framework without making any physical infrastructure improvements",
        "The planner should only invest in building geothermal power generation plants following Iceland's specific model despite the absence of any volcanic geological activity"
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

print(f"Fixed {len(fixes)} questions in Lesson9.5_Quiz.json")
