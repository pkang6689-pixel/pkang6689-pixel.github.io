import json

path = "C:/Users/Peter/pkang6689-pixel.github.io/content_data/EnvironmentalScienceLessons/Unit10/Lesson10.6_Quiz.json"
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

fixes = {
    4: [
        "Only the agricultural farming practices are involved in the chain without any downstream aquatic or ecological processes contributing to the outcome",
        "Only water pollution originating from a single identifiable industrial discharge source is responsible for creating oxygen-depleted dead zones",
        "Only one isolated link in the multi-step cause-effect chain actually matters while all the other intermediate stages are environmentally insignificant"
    ],
    5: [
        "Primary and secondary succession differ only in the geographic location where the ecological community development process takes place in nature",
        "The two types of succession differ only in the total amount of time required for the ecological community to reach its final climax state",
        "There is absolutely no meaningful ecological difference between primary and secondary succession as both processes follow identical pathways and timelines"
    ],
    17: [
        "There is no meaningful functional difference between renewable and nonrenewable natural resources as both are equally available for sustainable human use",
        "All natural resources found on Earth are technically renewable if they are properly managed with appropriate conservation strategies and sustainable harvest practices",
        "Nonrenewable natural resources are always more economically valuable in commercial markets than renewable resources regardless of supply and demand dynamics"
    ],
    19: [
        "Government-managed administrative programs that oversee and operate the day-to-day management and maintenance of designated national park and wilderness areas",
        "Public utility infrastructure services such as electrical power distribution, treated water supply, and sewage treatment systems that are delivered to natural ecosystems",
        "Professional consulting services provided by commercial environmental engineering and management companies to clients in the private and public development sectors"
    ],
    20: [
        "A localized atmospheric phenomenon that occurs exclusively in tropical latitudes and has no measurable effect on climate patterns at higher latitudes",
        "A harmful and entirely unnatural phenomenon caused solely by human industrial activity that should be completely eliminated through aggressive emission reductions",
        "The thermal heat that is generated and trapped inside commercial glass-walled agricultural greenhouse structures due to the physical barrier preventing air circulation"
    ],
    21: [
        "The student's claim is entirely correct because total national emissions are the only metric that matters when comparing countries' climate change contributions",
        "Per capita analysis would show that both countries have exactly identical per-person emission levels despite their vastly different total national population sizes",
        "Per capita emission analysis is completely irrelevant and provides no useful information for understanding or addressing international climate change policy questions"
    ],
    22: [
        "The rancher must have applied synthetic chemical herbicides or pesticides that permanently sterilized the soil and prevented any future vegetation from establishing",
        "Both the clear-cut area and the burned area are undergoing primary ecological succession at exactly the same rate with no difference in recovery trajectory",
        "Fire disturbance always promotes faster and more vigorous plant growth than mechanical logging regardless of the severity of soil disturbance or seed bank loss"
    ],
    23: [
        "Only a general policy recommendation to immediately and permanently ban all agricultural pesticide products without any scientific analysis of specific mechanisms",
        "Only a brief statement that frog populations are declining because of general environmental pollution without identifying specific causes or interaction mechanisms",
        "Only a basic mathematical calculation of the percentage population decline rate without any analysis of contributing environmental factors or ecological implications"
    ],
    24: [
        "Only a direct financial cost comparison between the current per-kilowatt-hour price of diesel-generated electricity versus solar photovoltaic panel electricity",
        "Only a brief description of the general environmental benefits of transitioning from fossil fuel energy sources to renewable energy generation without specific details",
        "Only naming the installation of solar photovoltaic panels as the complete energy solution without discussing storage, grid integration, or implementation strategy"
    ],
    25: [
        "Only the municipal wastewater treatment plant discharge located within the city is responsible for all of the elevated nitrogen concentrations measured downstream",
        "Only agricultural fertilizer runoff from upstream farming operations is responsible for all nitrogen contamination measured at every downstream sampling location",
        "Only naturally occurring biological nitrogen fixation processes in the soil and water are responsible for the elevated nitrogen concentrations found throughout the watershed"
    ],
    26: [
        "Only a technical engineering recommendation to drill progressively deeper water supply wells in Country B to reach aquifer layers below the current pumping depth",
        "Only a precise geological calculation of the total remaining recoverable water volume stored in the shared transboundary aquifer underlying both countries' territories",
        "Only a detailed geological description explaining the general hydrogeological principles of how confined and unconfined aquifer groundwater storage systems function"
    ],
    27: [
        "The student's reasoning is entirely sound and logically correct, and absolutely no additional environmental data is needed to validate their air quality conclusion",
        "Regional ambient air quality conditions can only be accurately measured and assessed through comprehensive monitoring programs administered at the federal government level",
        "The factory's reported 40% emission reduction data must be fabricated or incorrect because industrial pollution control technology cannot achieve such significant reductions"
    ],
    28: [
        "Only a practical recommendation that international cargo ships should be inspected more carefully at port facilities to prevent accidental invasive species introduction",
        "Only that the island has a small total geographic land area, which makes it generally more vulnerable to any type of ecological disturbance regardless of the specific cause",
        "Only that rats are known to consume bird eggs and nestlings, which directly reduces reproductive success without considering broader evolutionary or ecological vulnerability factors"
    ],
    29: [
        "Reject all three proposed policy approaches entirely and instead recommend a complete prohibition on all agricultural activities near any waterway or riparian buffer zone",
        "Only compare which of the three proposed approaches would be the least expensive for the government treasury to implement and administer over the coming fiscal year period",
        "Only recommend whichever policy approach the agricultural farming community and industry stakeholders indicate they would most prefer and be most willing to voluntarily adopt"
    ],
    30: [
        "Deforestation connects only to the loss of biological diversity through habitat destruction and has no meaningful linkage to any other environmental science course topics",
        "Deforestation connects to at most two different environmental science course topics and cannot be meaningfully analyzed across a broader range of interconnected subject areas",
        "Deforestation is only directly relevant to the commercial forestry and timber harvesting industry and has no broader significance for environmental science course material"
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

print(f"Fixed {len(fixes)} questions in Lesson10.6_Quiz.json")
