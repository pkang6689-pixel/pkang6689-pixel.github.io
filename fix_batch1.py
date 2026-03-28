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

# FILE 1: Lesson1.4_Quiz.json - The Rock Cycle
print("Fixing Lesson1.4_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit1/Lesson1.4_Quiz.json", {
    4: [
        "Rapid melting of minerals deep within the mantle",
        "Slow cooling and crystallization from liquid magma",
        "Chemical breakdown through acidic groundwater reactions"
    ],
    7: [
        "Fine sediment particles that are scattered by erosion",
        "Compressed fossil impressions preserved within layers",
        "Dense metamorphic rock containing foliated mineral bands"
    ],
    8: [
        "Pushes rocks deeper underground where they eventually melt into magma",
        "Compresses organic sediment layers into economically valuable fossil fuels",
        "Increases confining pressure on buried rocks, triggering recrystallization"
    ],
    9: [
        "Intense underground heat melts adjacent rock layers, fusing sediment into a solid mass",
        "Volcanic eruptions deposit layers of ash that chemically bond with existing surface rock",
        "River currents carry mineral-rich sediment downstream and deposit it in a new basin area"
    ],
    14: [
        "The folding and buckling of rock layers under tectonic compression forces deep within the crust",
        "The slow cooling and solidification of magma within underground chambers to form crystalline rock",
        "The gradual melting of rock at depth due to rising temperatures near tectonic plate boundaries"
    ],
    20: [
        "Crystallized mineral structures that form inside cooling magma chambers deep beneath the surface",
        "The dense layer of liquid iron and nickel that circulates within Earth's outer core region",
        "Hot pressurized molten rock flowing beneath Earth's crust that may eventually erupt at volcanoes"
    ],
    22: [
        "It can only return to the mantle through subduction where it re-melts into magma, since igneous rock lacks the mineral structure needed for metamorphic or sedimentary transformation",
        "It must first be broken down by weathering into sediments and lithified into sedimentary rock before any further transformations are possible within the rock cycle sequence",
        "Once igneous rock has fully cooled and its mineral crystals have locked into place, its composition becomes too stable for any further geological transformation to occur"
    ],
    23: [
        "It is subjected to extreme pressure as it moves downhill, undergoing rapid metamorphism from friction and compression to form new metamorphic rock formations",
        "It dissolves completely in acidic groundwater during transport and is permanently removed from the rock cycle without contributing to any new formation",
        "It is pushed deep underground through cracks in the bedrock where geothermal heat melts it into magma that will later solidify as igneous rock"
    ],
    24: [
        "The rock is vaporized by extreme mantle temperatures and the resulting gases escape through volcanic vents and fractures at the surface",
        "The intense mantle pressure crushes the descending rock into fine sediment particles that are eventually returned to the ocean floor",
        "The rock remains solid and chemically stable because temperatures at that depth in the mantle are not sufficient to alter its mineral structure"
    ],
    25: [
        "Ocean-floor mud was directly compressed by tectonic forces into schist without passing through any intermediate sedimentary rock stage",
        "Erosion carried the mud deep underground where volcanic heat melted it into magma, which cooled and crystallized as the schist formation",
        "The mud was first melted by geothermal heat into magma, which then slowly cooled in a subsurface chamber to form crystalline schist rock"
    ]
})

# FILE 2: Lesson2.5_Quiz.json - Volcanoes & Hot Spots
print("Fixing Lesson2.5_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit2/Lesson2.5_Quiz.json", {
    1: [
        "Extremely high viscosity, which causes it to pile up steeply near the vent",
        "Primarily composed of fragmented volcanic debris and explosive tephra",
        "Rich in dissolved gases that expand rapidly and create lightweight pumice"
    ],
    6: [
        "Absorbing incoming solar radiation in the lower atmosphere and converting it to long-wave infrared heat energy",
        "Opening deep rifts in the ocean floor that allow cold abyssal water to circulate and cool surface temperatures",
        "Releasing heavy volcanic particles that settle in the troposphere and produce no lasting effect on global climate"
    ],
    11: [
        "The internal temperature of molten rock measured in degrees, which determines whether an eruption will be explosive or effusive in character",
        "The visible color spectrum of erupted lava on the surface, ranging from dark basaltic black to light rhyolitic gray depending on mineral content",
        "The total volume of dissolved gas trapped within magma before eruption, which controls the force and height of the resulting volcanic ash column"
    ],
    12: [
        "A region along a convergent plate boundary where two tectonic plates collide and generate volcanic eruptions through crustal compression forces",
        "An area of exceptionally high surface air temperature in arid desert regions caused by intense solar radiation and very low cloud cover",
        "A persistent warm ocean current that flows along continental coastlines and transfers tropical heat energy toward polar regions over time"
    ],
    14: [
        "A type of dense volcanic rock formed when lava cools rapidly under high-pressure conditions deep underground",
        "A seismic event triggered by magma movement beneath a volcano that causes the surrounding ground to shake",
        "A cloud of toxic volcanic gases including sulfur dioxide and carbon dioxide released from an active vent"
    ],
    15: [
        "A hollow cavity deep underground that is filled with pressurized volcanic gases which may vent through fumaroles at the surface",
        "The large bowl-shaped depression at the summit of a volcano formed by the collapse of rock after previous major eruptions",
        "A specially equipped research facility where volcanologists monitor seismic activity and carefully analyze volcanic rock samples"
    ],
    16: [
        "A broad, slow-moving type of lava flow that spreads across wide areas of flat terrain before cooling into a thin layer of basalt",
        "A volcanic island that forms gradually as eruptions from an oceanic hot spot build layers of basaltic lava above the sea surface",
        "A small secondary volcanic vent on the flanks of a larger volcano that intermittently releases steam, gases, and minor lava flows"
    ],
    17: [
        "A hollow underground tunnel formed by flowing lava beneath the surface of a shield volcano that channels molten rock to distant vents",
        "A deep fracture in the ocean floor along a divergent plate boundary where tectonic plates are slowly spreading apart from one another",
        "A towering column of volcanic ash and fine particles ejected high into the atmosphere during an explosive stratovolcano eruption event"
    ],
    19: [
        "Kinetic energy released during earthquakes as seismic waves travel through Earth's crust and cause widespread ground shaking",
        "Chemical potential energy stored within volcanic gases such as sulfur dioxide and hydrogen sulfide at active volcanic vents",
        "Solar radiation absorbed and stored in exposed surface rocks, then gradually released as radiant heat during the nighttime hours"
    ],
    20: [
        "A measurement of the velocity at which lava flows downslope from a volcanic vent, calculated using the lava's viscosity and terrain steepness",
        "A quantitative measure of erupted lava temperature in degrees Celsius, used to classify volcanic eruptions by their total thermal output",
        "A regional count of all currently active volcanic vents within a defined geographic area, updated annually by geological survey agencies"
    ],
    26: [
        "Kilauea has a much smaller magma chamber than Pinatubo, so it cannot build enough gas pressure for the violent explosive eruptions typical of Philippine volcanoes",
        "Kilauea formed more recently than Pinatubo and has not yet developed the deep magma reservoir needed to produce the violent explosive eruptions of older volcanoes",
        "Pacific Ocean water surrounding Hawaii constantly cools Kilauea's erupting lava and absorbs the thermal energy that would otherwise fuel explosive volcanic activity"
    ],
    29: [
        "Lava flows, because their extreme temperatures melt and consume everything in their path for hundreds of kilometers before the molten rock cools enough to solidify",
        "Volcanic gases, because their lightweight molecular composition enables them to spread in all directions from the vent and travel great distances across entire continents",
        "Pyroclastic flows, because their extreme speed of over 700 km/h allows them to travel enormous distances from the volcano, devastating everything along their path"
    ]
})

print("Batch 1 complete!")
