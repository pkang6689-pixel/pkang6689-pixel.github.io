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

# FILE 3: Lesson5.5_Quiz.json - Weather Fronts & Storms
print("Fixing Lesson5.5_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit5/Lesson5.5_Quiz.json", {
    3: [  # Hurricanes form over:
        "Flat continental land masses heated by intense tropical sunlight",
        "Cold polar ocean waters with temperatures below 10 degrees Celsius",
        "High-altitude mountain ranges that force air upward past 3,000 meters"
    ],
    4: [  # A warm front produces:
        "Brief but intense thunderstorms concentrated along a narrow band",
        "Clear skies and steadily rising temperatures across the whole region",
        "Only dense fog banks forming along coastal and low-lying valley areas"
    ],
    6: [  # An occluded front forms when:
        "A warm front and cold front diverge from each other, leaving a broad region of stable dry air between them",
        "A tropical cyclone moves inland and disrupts pre-existing frontal boundaries across the continental interior",
        "Atmospheric pressure stabilizes uniformly across a large region, causing all active frontal boundaries to dissolve"
    ],
    10: [  # Most dangerous part of hurricane:
        "Outer rain bands that extend hundreds of kilometers outward from the center",
        "Central eye where rapidly descending air creates dangerous turbulent gusts",
        "Trailing back side of the storm where residual winds briefly intensify"
    ],
    16: [  # What is a mid-latitude cyclone?
        "A localized rotating windstorm that forms over continental interiors where extreme surface heating creates strong convective instability",
        "A large-scale tropical storm system that develops over warm ocean waters and produces sustained rotating winds exceeding 119 km/h",
        "A persistent high-pressure system at middle latitudes that blocks approaching fronts and maintains extended periods of dry, fair weather"
    ],
    17: [  # What does 'wind shear' mean?
        "The destructive erosion force that sustained winds exert on exposed structures and terrain during severe storm events",
        "The temporary period of calm air occurring between successive wind gusts during a thunderstorm or frontal passage",
        "The aggregate total wind speed measured at all atmospheric levels from the surface through the upper troposphere"
    ],
    18: [  # What is a blizzard?
        "A brief snow squall that produces light accumulation and moderate winds but clears within an hour as the frontal boundary quickly passes",
        "Any snowstorm that produces measurable snow accumulation on the ground regardless of wind speed, temperature, or total duration of snowfall",
        "An ice storm characterized by freezing rain that coats all surfaces with a thick glaze of ice, bringing down power lines and tree branches"
    ],
    20: [  # What does 'tropical depression' mean?
        "A formal classification on the Saffir-Simpson scale for hurricanes with sustained winds between 178 and 208 km/h at peak intensity",
        "A persistent region of below-average rainfall in the tropics caused by large-scale atmospheric subsidence that suppresses cloud formation",
        "An unusual period of below-normal temperatures in equatorial regions caused by shifts in ocean circulation and atmospheric cooling patterns"
    ],
    26: [  # Green sky + freight train sound
        "A heavy rain event producing flash flooding, since the green sky results from sunlight filtering through thick rain-saturated storm clouds",
        "An approaching blizzard with very heavy snowfall, since green skies and rumbling sounds can precede major winter storm systems in spring",
        "A hurricane making landfall in the region, since the greenish tint and roaring noise are features of tropical cyclone outer rain bands"
    ],
    27: [  # Two cities hit by same hurricane, different flooding
        "City A has a denser arrangement of tall buildings that blocked wind flow and created pressure channels amplifying flood water through streets",
        "City B was located at a higher latitude where the hurricane's rotation was weaker due to reduced Coriolis effect at that distance from the tropics",
        "The hurricane lost significant wind speed and energy as it traveled between the two cities, producing substantially less rainfall when reaching City B"
    ],
    28: [  # Mid-latitude cyclone - occluded front forms
        "The occluded front generates severe instability that typically produces a new wave of tornadoes along the boundary between merging air masses",
        "Both the cold front and warm front dissolve simultaneously when their temperature contrasts equalize, causing the entire storm to end abruptly",
        "The warm front accelerates and overtakes the slower-moving cold front, forcing cold air aloft and significantly intensifying the storm system"
    ]
})

# FILE 4: Lesson6.1_Quiz.json - Climate vs. Weather
print("Fixing Lesson6.1_Quiz.json...")
fix_file("c:/Users/Peter/pkang6689-pixel.github.io/content_data/EarthScienceLessons/Unit6/Lesson6.1_Quiz.json", {
    1: [  # Weather describes atmospheric conditions over:
        "Extended periods spanning several hundred years",
        "Continuous periods of multiple consecutive decades",
        "Geological timescales covering millions of years"
    ],
    10: [  # "Climate is what you expect, weather is what you get"
        "Weather events occur randomly and have no statistical connection to the long-term climate averages recorded for a given region",
        "Climate data can precisely predict daily weather conditions because atmospheric patterns follow consistent, repeating annual cycles",
        "Climate and weather are interchangeable terms that both describe the same atmospheric conditions observed at different spatial scales"
    ],
    11: [  # What is weather?
        "The statistical average of atmospheric conditions recorded over a 30-year period that defines a region's typical expected conditions",
        "The long-term recurring pattern of seasonal temperature and precipitation changes that characterizes a particular geographic region",
        "The scientific classification system that organizes geographic regions into distinct zones based on their average annual temperatures"
    ],
    12: [  # What is climate?
        "A short-range prediction of upcoming atmospheric conditions for the next one to seven days ahead in a particular area",
        "The single highest temperature measurement recorded during the warmest calendar day of the year at a weather station",
        "A compilation of twelve consecutive months of weather observations collected from a single monitoring station location"
    ],
    19: [  # What does 'paleoclimatology' mean?
        "The scientific discipline focused on predicting future climate conditions using computer models and statistical projection methods",
        "The branch of atmospheric science that studies current global climate patterns through satellite imagery and remote sensing data",
        "The comparative study of atmospheric conditions on other planets in the solar system to better understand their weather processes"
    ],
    21: [  # Tourist in Miami - cold day
        "Miami is classified as a temperate zone rather than tropical, so cold winter days are expected and normal for its climate category",
        "January data is excluded from climate normal calculations because winter months show too much variability to be statistically useful",
        "Climate change only influences summer heat extremes and has no measurable effect on winter temperatures in subtropical coastal areas"
    ],
    24: [  # Ice core data - what type of data?
        "Instrumental weather station records compiled from a global network of meteorological observatories operating continuously since the 1800s",
        "Computer model simulations that reconstruct historical climate conditions by running atmospheric physics equations backward through time",
        "Satellite remote sensing data collected by orbiting instruments that have continuously monitored Earth's atmosphere since the space age"
    ],
    25: [  # Heat wave proves global warming?
        "Every individual hot day is directly caused by climate change because rising global temperatures ensure all extreme heat events stem from human emissions",
        "Heat waves are entirely natural weather phenomena driven by atmospheric circulation patterns and have no connection to long-term global temperature trends",
        "Climate change influences only winter temperatures by reducing cold extremes, while summer heat waves are controlled entirely by natural solar radiation cycles"
    ],
    26: [  # Two cities same latitude, coastal vs inland
        "City B sits at a higher elevation on a continental plateau, where reduced atmospheric pressure amplifies seasonal temperature extremes noticeably",
        "City A has a denser network of weather stations that captures milder average readings, while City B has fewer stations recording more extreme values",
        "City A has extensive urban tree canopy cover that provides substantial cooling shade and transpiration, effectively moderating its temperature range"
    ],
    27: [  # More snow = no global warming argument
        "The student's reasoning is scientifically valid because increased snowfall directly contradicts the warming trend predicted by climate models for all regions",
        "Global warming eliminates snowfall everywhere on Earth because rising temperatures prevent water vapor from crystallizing into snow in any region whatsoever",
        "Snowfall patterns are completely independent of air temperature and are determined solely by wind direction, making them irrelevant to any climate discussion"
    ],
    30: [  # Weather forecaster vs climate projections
        "Weather forecasting and climate modeling rely on fundamentally different scientific principles with no overlap, so predictions from each cannot be compared using common physics",
        "Climate models rely on statistical extrapolation rather than physical laws, making their long-term projections unreliable estimates that lack the rigor of short-range forecasts",
        "Weather forecasts based on real-time observations are inherently more accurate than climate projections at every timescale, because direct measurements always outperform models"
    ]
})

print("Batch 2 complete!")
