import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit10/Lesson10.5_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    3: [
        "The scoping process determines only the total project construction budget allocation and financial expenditure limits for each phase of implementation",
        "Scoping is responsible exclusively for selecting which construction contractor will be awarded the contract to physically build the proposed project",
        "The scoping phase determines only the expected completion date and overall timeline for delivering the finished project to its intended end users"
    ],
    10: [
        "Water impact assessments examine only a single narrow aspect of water resources without considering the interconnected dimensions of the hydrological system",
        "Water impact assessment evaluates exclusively the municipal drinking water supply capacity without considering ecological or groundwater quality implications",
        "The water assessment component focuses only on measuring surface water chemical pollution concentrations without analyzing flow patterns or aquatic habitat impacts"
    ],
    12: [
        "A comprehensive financial audit examining only the project's construction and operational budget expenditures to verify fiscal responsibility and compliance",
        "The initial development proposal document submitted by the project developer to the federal agency at the very beginning of the environmental review process",
        "A binding court order issued by a federal judge that permanently stops a proposed development project from proceeding at any point in the foreseeable future"
    ],
    16: [
        "A public opinion survey instrument that asks only whether local residents support or oppose the proposed construction project in their neighborhood area",
        "A narrowly focused economic assessment that measures only the total number of new jobs created by a proposed construction or development project activity",
        "A limited real estate market analysis that evaluates only the projected changes in residential property values in neighborhoods adjacent to the project site"
    ],
    17: [
        "A study limited to cataloging only rare and threatened plant species found at the proposed project development site without broader ecological analysis",
        "A single-species population count focused on surveying only one particular type of organism present within the proposed project development area boundaries",
        "A narrow taxonomic inventory that only records and lists mammal species documented within the immediate geographic boundaries of the proposed project area"
    ],
    18: [
        "Exclusively registered environmental advocacy organizations that actively campaign for conservation goals and habitat protection through public lobbying efforts",
        "Only government regulatory officials and agency administrators who have formal legal authority over environmental permitting and compliance enforcement decisions",
        "Only the project developer, property owner, or sponsoring organization that initiated and submitted the proposal for environmental review and regulatory approval"
    ],
    19: [
        "A financial management plan designed to track and monitor the overall construction budget expenditures throughout the duration of the building project timeline",
        "A workplace safety management plan designed to monitor and ensure employee occupational health and safety conditions on the active construction work site",
        "A one-time comprehensive inspection conducted only after the entire construction project has been fully completed and all building activities have ceased permanently"
    ],
    20: [
        "Indoor air quality standards specifically regulating ventilation, temperature, and pollutant levels within commercial and residential office building environments",
        "Air quality regulations that apply only to designated geographic areas located within close proximity to national parks and federal wilderness preservation areas",
        "Completely voluntary industry guidelines that individual companies and organizations can choose to follow or ignore at their own discretion without legal consequences"
    ],
    21: [
        "Summarily dismiss all public concerns raised during the scoping process as emotional reactions rather than legitimate scientific or evidence-based environmental issues",
        "Only address the specific environmental concerns that can be completely resolved through available civil engineering or technical construction design solutions",
        "Only analyze and respond to the single environmental concern that received the highest total number of public comments during the formal scoping comment period"
    ],
    22: [
        "There is nothing wrong with the proposed approach because the habitat compensation area is double the size of the area that would be directly disturbed by mining",
        "Compensation in the form of habitat protection is never acceptable under any circumstances regardless of how thoroughly other mitigation steps have been evaluated",
        "Only the federal endangered species management agency has the legal authority and scientific expertise to determine appropriate mitigation measures for listed species"
    ],
    24: [
        "Only the country of origin where the solar panel photovoltaic modules were manufactured and the labor conditions at the overseas semiconductor production facilities",
        "Only the visual aesthetic impact of solar panels visible from public streets and sidewalks and whether they conform to neighborhood architectural design standards",
        "Only the physical weight load of the installed solar panel array on the existing roof structural support system and whether reinforcement engineering is necessary"
    ],
    25: [
        "Only compare the total clean electricity energy generating output of each dam alternative without considering ecological, cultural, or social displacement factors",
        "Only compare the estimated construction cost of each alternative dam design without considering any environmental, social, or long-term operational cost factors",
        "Simply select whichever dam construction alternative the project developer or sponsoring government agency has indicated they prefer without independent evaluation"
    ],
    28: [
        "Only the informal opinions and anecdotal observations shared by members of local amateur birdwatching clubs without any systematic scientific data collection methods",
        "Only the projected annual electricity generation output and revenue estimates for the proposed wind farm without any consideration of wildlife mortality or habitat impacts",
        "No additional environmental data of any kind is needed because the existing two-year pre-construction wildlife survey is sufficient to support all impact conclusions"
    ],
    29: [
        "Only a descriptive narrative summary of the current landfill operational procedures and waste handling protocols without any environmental impact analysis components",
        "Only the total projected volume of additional solid waste that the proposed landfill expansion can accommodate without analyzing any environmental impact categories",
        "Only a comprehensive financial feasibility study and detailed construction timeline for the expansion project without addressing any environmental or community impacts"
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

print(f"Fixed {len(fixes)} questions in Lesson10.5_Quiz.json")
