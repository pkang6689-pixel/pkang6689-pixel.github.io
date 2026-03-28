import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit10/Lesson10.4_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    3: [
        "Only perform basic mathematical calculations of human population growth rates using census data and standard demographic transition models",
        "Only conduct laboratory measurements of soil pH levels and chemical composition using standard analytical chemistry testing equipment and procedures",
        "Only produce simple hand-drawn paper maps of geographic features using traditional cartographic techniques without any digital spatial data analysis"
    ],
    11: [
        "A detailed financial cost analysis evaluating the economic viability and projected return on investment for building a new manufacturing facility",
        "A mathematical population growth model used by conservation biologists to project future population trajectories for critically endangered species",
        "A comprehensive field study examining the typical lifespan, reproductive behavior, and mortality patterns of organisms in their natural wild habitat"
    ],
    12: [
        "The natural ecological recovery process where damaged ecosystems gradually restore themselves over time without any deliberate human intervention efforts",
        "The emergency population relocation strategy of permanently moving entire residential communities away from heavily contaminated industrial zones",
        "The preventive regulatory approach of implementing strict pollution control measures to stop environmental contamination before it initially occurs"
    ],
    14: [
        "The total financial expense of acquiring land and constructing physical infrastructure for establishing new protected nature reserve conservation areas",
        "The current market price of commercially harvested timber and extracted mineral resources from a specific geographic area or managed forest parcel",
        "The appraised real estate market value of undeveloped land parcels located within or immediately adjacent to designated natural ecosystem conservation areas"
    ],
    16: [
        "The recreational pastime of watching professionally produced nature documentary films and television programs about various global ecosystem environments",
        "A single isolated measurement of one particular environmental variable taken at one specific point in time at one location within the study area",
        "The installation of electronic security surveillance camera systems within fenced nature reserve boundaries to prevent unauthorized human trespassing access"
    ],
    17: [
        "Any occupation or job position that requires employees to perform their regular work duties primarily in outdoor environmental conditions and settings",
        "Unpaid volunteer service positions with registered environmental nonprofit organizations that focus on conservation advocacy and public awareness campaigns",
        "Employment positions exclusively within public parks, botanical gardens, and landscaping maintenance departments with no connection to broader sustainability"
    ],
    18: [
        "A narrow analytical methodology that deliberately focuses on examining one single isolated environmental variable at a time without considering interactions",
        "The educational practice of memorizing individual disconnected facts about specific environmental issues without understanding how they relate to each other",
        "An academic field that is exclusively concerned with studying computer hardware systems and digital information technology rather than natural environmental processes"
    ],
    19: [
        "A formal requirement that an individual must possess an accredited university degree specifically in environmental science to hold any opinion on these matters",
        "The specialized technical ability to read and comprehend peer-reviewed scientific research journal articles published in the field of ecology and conservation",
        "The practical field identification skill of correctly recognizing and naming common plant and animal species found in local natural habitat environments"
    ],
    20: [
        "Research that deliberately avoids developing deep expertise or specialized knowledge in any particular academic field or scientific discipline area",
        "Research collaborations that exclusively take place between scientists at different academic universities rather than within a single research institution",
        "Research investigations conducted entirely by scientists trained in and working within only one single narrow academic field or scientific discipline area"
    ],
    22: [
        "The spatial analysis data should only be used to create a visually appealing and colorful map suitable for inclusion in an annual organizational report",
        "The satellite and GIS data can only be used to confirm and document that tropical forest deforestation has already occurred in the monitored study area",
        "The remote sensing analysis is only useful for calculating the precise total remaining area of standing forest without any predictive or planning application"
    ],
    24: [
        "Exclusively real estate property developers to plan and coordinate the physical relocation of the entire coastal community to higher inland ground elevations",
        "Only elected political officials to draft and pass emergency disaster response legislation without input from scientific or community stakeholder perspectives",
        "Only licensed civil engineers to design and construct progressively higher concrete seawall flood barriers along the entire vulnerable coastal shoreline area"
    ],
    28: [
        "The student should make their career decision based solely on the expected starting salary and compensation package offered by each professional position available",
        "Environmental career fields across all sectors are declining in demand due to reduced regulatory enforcement and should be avoided in favor of other professions",
        "Only one of these three environmental career pathways actually produces meaningful positive environmental outcomes while the other two have negligible real impact"
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

print(f"Fixed {len(fixes)} questions in Lesson10.4_Quiz.json")
