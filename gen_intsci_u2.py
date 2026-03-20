#!/usr/bin/env python3
"""Integrated Science Unit 2 – Atmosphere & Weather (9 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "integrated_science_lessons.json")
COURSE = "Integrated Science"

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for qi, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2,
                    "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": COURSE,
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# 2.1
k,v = build_lesson(2,1,"Composition & Layers of the Atmosphere",
    "<h3>Atmospheric Composition & Structure</h3>"
    "<h4>Composition</h4>"
    "<ul><li>Nitrogen 78%, Oxygen 21%, Argon 0.93%, CO₂ 0.04%, trace gases and water vapor.</li></ul>"
    "<h4>Atmospheric Layers</h4>"
    "<ul><li><b>Troposphere (0-12 km):</b> Weather occurs here; temperature decreases with altitude.</li>"
    "<li><b>Stratosphere (12-50 km):</b> Contains ozone layer; temperature increases with altitude.</li>"
    "<li><b>Mesosphere (50-85 km):</b> Coldest layer; meteors burn up here.</li>"
    "<li><b>Thermosphere (85-600 km):</b> Very hot but thin; auroras occur here.</li>"
    "<li><b>Exosphere (600+ km):</b> Transitions into space.</li></ul>",
    [("Troposphere","Lowest atmospheric layer (0-12 km); where weather occurs; temperature decreases with altitude."),
     ("Stratosphere","Layer above troposphere (12-50 km); contains the ozone layer; temperature increases with altitude."),
     ("Ozone Layer","Region in the stratosphere where O₃ absorbs UV radiation, protecting life on Earth."),
     ("Mesosphere","Third atmospheric layer (50-85 km); coldest layer; where meteors burn up."),
     ("Thermosphere","Fourth layer (85-600 km); extremely hot molecules but very thin atmosphere; where auroras occur.")],
    [("The most abundant gas in Earth's atmosphere is:",["Oxygen","Carbon dioxide","*Nitrogen (~78%)","Argon"],"Nitrogen dominance."),
     ("Weather occurs in the _____ because it contains most atmospheric water vapor.",["Stratosphere","*Troposphere","Mesosphere","Thermosphere"],"Weather layer."),
     ("In the troposphere, temperature _____ with altitude.",["Increases","Stays constant","*Decreases (average lapse rate ~6.5°C per km)","Fluctuates randomly"],"Lapse rate."),
     ("The ozone layer is located in the:",["Troposphere","*Stratosphere (absorbs harmful UV radiation)","Mesosphere","Thermosphere"],"Ozone location."),
     ("CFCs (chlorofluorocarbons) damage the ozone layer by:",["Adding oxygen","*Releasing chlorine atoms that catalytically destroy ozone molecules (one Cl can destroy thousands of O₃)","Creating CO₂","Heating the air"],"CFC mechanism."),
     ("The Montreal Protocol (1987) addressed:",["Climate change","*The ozone hole — banning CFCs (one of the most successful environmental treaties)","Acid rain","Air pollution only"],"Montreal Protocol."),
     ("The coldest temperatures in the atmosphere are found at the top of the:",["Troposphere","Stratosphere","*Mesosphere (~-90°C at the mesopause)","Thermosphere"],"Coldest layer."),
     ("Auroras (Northern/Southern Lights) occur in the:",["Troposphere","Stratosphere","Mesosphere","*Thermosphere (charged solar particles interact with atmospheric gases)"],"Aurora location."),
     ("The exosphere is the atmospheric layer that:",["Has the most weather","*Gradually transitions into the vacuum of outer space","Is the densest","Contains the ozone"],"Exosphere."),
     ("A tropopause is the boundary between the:",["Stratosphere and mesosphere","*Troposphere and stratosphere","Mesosphere and thermosphere","Thermosphere and exosphere"],"Tropopause."),
     ("Atmospheric pressure _____ with altitude.",["Increases","Stays constant","*Decreases (less air above = less weight = less pressure)","Increases then decreases"],"Pressure decrease."),
     ("At sea level, atmospheric pressure is approximately:",["500 mb","*1,013 mb (or 1 atm, or 29.92 inches Hg)","2,000 mb","100 mb"],"Standard pressure."),
     ("The greenhouse effect is caused primarily by:",["Nitrogen and oxygen","*Water vapor, CO₂, and methane trapping infrared radiation","Ozone only","Argon"],"Greenhouse gases."),
     ("Without the natural greenhouse effect, Earth's average temperature would be approximately:",["15°C (current average)","0°C","*-18°C (too cold for liquid water — life as we know it wouldn't exist)","100°C"],"Natural greenhouse."),
     ("CO₂ makes up only ~0.04% of the atmosphere but is significant because:",["It's abundant","*It strongly absorbs infrared radiation (a powerful greenhouse gas despite low concentration)","It's colorful","It's heavy"],"CO₂ significance."),
     ("Jet streams are high-altitude winds found at the:",["Surface","*Tropopause boundary (strong wind bands that influence weather patterns below)","Mesopause","In the ozone layer"],"Jet streams."),
     ("The ionosphere (within thermosphere) is important for:",["Weather prediction","*Radio communication (ionized layers reflect certain radio frequencies back to Earth)","Aviation","Agriculture"],"Ionosphere."),
     ("Air density is highest at:",["High altitude","The stratosphere","*Sea level (more air molecules compressed by the weight of air above)","The mesosphere"],"Density distribution."),
     ("Rayleigh scattering causes the sky to appear blue because:",["Air is blue","*Shorter blue wavelengths of light are scattered more by atmospheric molecules","Blue light is absorbed","Water is blue"],"Blue sky."),
     ("Understanding atmospheric layers is essential for:",["Only aviation","Only meteorology","Only space exploration","*Aviation, meteorology, climate science, satellite operations, and understanding life-supporting conditions on Earth"],"Multi-disciplinary importance.")]
)
lessons[k]=v

# 2.2
k,v = build_lesson(2,2,"Energy Transfer (Radiation, Conduction, Convection)",
    "<h3>Energy Transfer in Earth's Atmosphere</h3>"
    "<h4>Three Methods</h4>"
    "<ul><li><b>Radiation:</b> Transfer by electromagnetic waves; how the Sun heats Earth (no medium required).</li>"
    "<li><b>Conduction:</b> Direct contact transfer; Earth's surface heats air touching it.</li>"
    "<li><b>Convection:</b> Transfer by fluid movement; warm air rises, cool air sinks → convection cells.</li></ul>"
    "<h4>Earth's Energy Budget</h4>"
    "<ul><li>~30% of solar radiation reflected (albedo), ~70% absorbed by surface and atmosphere.</li>"
    "<li>Earth radiates infrared back; greenhouse gases absorb and re-emit some, warming the surface.</li></ul>",
    [("Radiation","Energy transfer via electromagnetic waves; requires no medium (how sunlight reaches Earth through space)."),
     ("Conduction","Heat transfer through direct molecular contact; ground heats air touching its surface."),
     ("Convection","Heat transfer through fluid movement; warm fluid rises, cool fluid sinks, creating circulation cells."),
     ("Albedo","The fraction of incoming solar radiation reflected by a surface; ice/snow have high albedo, dark surfaces low."),
     ("Energy Budget","The balance between incoming solar radiation and outgoing reflected/emitted radiation; determines Earth's temperature.")],
    [("Sunlight reaches Earth through space by:",["Conduction","Convection","*Radiation (electromagnetic waves don't need a medium)","All three equally"],"Solar radiation."),
     ("When you feel heat from touching a hot rock, the transfer method is:",["Radiation","*Conduction (direct contact between your hand and rock)","Convection","Reflection"],"Conduction example."),
     ("Hot air rising and cool air sinking creates:",["Radiation patterns","*Convection cells (the primary mechanism driving atmospheric circulation)","Conduction layers","Static air"],"Convection."),
     ("Earth's albedo is approximately 30%, meaning:",["30% absorbed","*30% of incoming solar radiation is reflected back to space","30% reaches Earth","30% is infrared"],"Albedo."),
     ("Fresh snow has a high albedo (~80-90%), meaning it:",["Absorbs most radiation","*Reflects most radiation (why snowy landscapes feel cold — less absorption = less heating)","Emits radiation","Conducts heat well"],"Snow albedo."),
     ("Dark ocean water has low albedo (~6%), meaning it:",["Reflects most light","*Absorbs most solar radiation (why ice loss creates a positive feedback: less ice → more absorption → more warming)","Is cold always","Emits UV light"],"Ocean albedo."),
     ("The greenhouse effect involves the atmosphere absorbing and re-emitting:",["Visible light","Ultraviolet radiation","*Infrared (longwave) radiation emitted by Earth's surface","Radio waves"],"Greenhouse mechanism."),
     ("Without greenhouse gases, Earth would be about _____ colder.",["5°C","15°C","*33°C colder (average -18°C instead of +15°C)","50°C"],"Greenhouse warming."),
     ("The Sun emits mostly _____ radiation.",["Infrared","*Visible light (peak emission around 500 nm wavelength)","Ultraviolet only","Radio waves"],"Solar spectrum."),
     ("Earth emits mostly _____ radiation.",["Visible light","UV light","*Infrared (longwave, due to Earth's much lower temperature than the Sun)","X-rays"],"Earth emission."),
     ("The reason land heats up faster than water is:",["Land is darker","Water is reflective","*Water has a much higher specific heat capacity (takes more energy to raise its temperature)","Land is thinner"],"Land vs. water heating."),
     ("Sea breezes occur during the day because:",["Water heats faster","*Land heats faster than water → air over land rises → cooler air from the sea flows in (convection)","Wind always blows inland","The Moon's gravity"],"Sea breeze."),
     ("At night, land breezes blow from _____ to _____.",["Sea to land","*Land to sea (land cools faster; cooler air over land flows toward warmer air over water)","South to north","East to west always"],"Land breeze."),
     ("Hadley cells are:",["Radiation patterns","*Large-scale atmospheric convection cells between the equator and ~30° latitude","Conduction zones","Ozone layers"],"Hadley cells."),
     ("Insolation is greatest at the equator because:",["The equator is closer to the Sun","*Sunlight hits the equator at a more direct angle, concentrating energy over a smaller area","The equator spins fastest","It rains less there"],"Equatorial insolation."),
     ("The ice-albedo feedback is a positive feedback because:",["It stabilizes temperature","*Melting ice reduces albedo → more absorption → more warming → more melting (amplifies initial change)","It creates ice","It cools Earth"],"Positive feedback."),
     ("Specific heat capacity of water is ~4,184 J/(kg·°C), meaning water:",["Heats quickly","*Requires a lot of energy to change temperature (moderating coastal climates)","Freezes easily","Evaporates slowly"],"Water specific heat."),
     ("Urban heat islands form because:",["Cities are cooler","*Dark surfaces (asphalt, buildings) absorb more heat, and lack of vegetation reduces evaporative cooling","Wind is stronger in cities","Cities have higher albedo"],"Urban heat."),
     ("Earth maintains a relatively stable temperature because incoming solar energy approximately equals:",["Absorbed energy only","*Total outgoing energy (reflected + emitted infrared) — the energy budget is roughly balanced","Nothing","Convection energy"],"Energy balance."),
     ("Human burning of fossil fuels affects the energy budget by:",["Increasing albedo","Reflecting more sunlight","*Adding CO₂ that absorbs more outgoing infrared radiation, trapping more heat (enhanced greenhouse effect)","Reducing convection"],"Anthropogenic impact.")]
)
lessons[k]=v

# 2.3
k,v = build_lesson(2,3,"Weather Systems (Fronts, Pressure Systems)",
    "<h3>Weather Systems</h3>"
    "<h4>Air Masses & Fronts</h4>"
    "<ul><li><b>Air masses:</b> Large bodies of air with uniform T and humidity (Continental/Maritime × Tropical/Polar/Arctic).</li>"
    "<li><b>Cold front:</b> Cold air pushes under warm air → steep boundary, heavy rain, then clearing.</li>"
    "<li><b>Warm front:</b> Warm air slides over cold air → gradual boundary, steady precipitation.</li>"
    "<li><b>Stationary front:</b> Neither air mass advances; prolonged cloudiness/rain.</li>"
    "<li><b>Occluded front:</b> Cold front catches warm front; complex weather.</li></ul>"
    "<h4>Pressure Systems</h4>"
    "<ul><li><b>Low pressure (cyclone):</b> Rising air, convergence, clouds, precipitation.</li>"
    "<li><b>High pressure (anticyclone):</b> Sinking air, divergence, clear skies.</li></ul>",
    [("Air Mass","Large body of air with relatively uniform temperature and humidity; classified by source region."),
     ("Cold Front","Boundary where cold air advances under warm air; produces heavy, brief precipitation and sharp temperature drops."),
     ("Warm Front","Boundary where warm air advances over cold air; produces gradual, steady precipitation."),
     ("Low Pressure (Cyclone)","Area of rising air, convergence at the surface, and divergence aloft; associated with clouds and precipitation."),
     ("High Pressure (Anticyclone)","Area of sinking air, divergence at the surface; associated with clear skies and calm weather.")],
    [("A continental polar (cP) air mass is:",["Warm and moist","Warm and dry","*Cold and dry (forms over cold land areas like Canada/Siberia)","Cold and moist"],"cP classification."),
     ("A maritime tropical (mT) air mass is:",["Cold and dry","*Warm and moist (forms over warm ocean areas like the Gulf of Mexico)","Warm and dry","Cold and moist"],"mT classification."),
     ("When a cold front passes through, you typically experience:",["Gradual warming","*Sharp temperature drop, heavy but brief precipitation, then clearing with colder air","No change","Only wind"],"Cold front weather."),
     ("Warm fronts produce _____ precipitation.",["Heavy, brief","*Light to moderate, steady, and prolonged","No","Severe only"],"Warm front precipitation."),
     ("On a weather map, cold fronts are shown with:",["Red semicircles","*Blue triangles pointing in the direction of movement","Green arrows","Yellow dots"],"Cold front symbol."),
     ("Low pressure systems rotate _____ in the Northern Hemisphere.",["Clockwise","*Counterclockwise (due to the Coriolis effect)","Not at all","Randomly"],"Cyclonic rotation."),
     ("High pressure systems are associated with:",["Storms and rain","*Clear skies, calm conditions, and fair weather (sinking air suppresses cloud formation)","Tornadoes","Hurricanes"],"High pressure weather."),
     ("The Coriolis effect causes moving air to curve because of:",["Wind speed","Temperature differences","*Earth's rotation (deflects moving objects right in NH, left in SH)","Pressure alone"],"Coriolis effect."),
     ("An occluded front forms when:",["Two warm fronts merge","*A fast-moving cold front catches up to a warm front, lifting the warm air completely off the surface","Fronts dissipate","Pressure equalizes"],"Occlusion."),
     ("A stationary front produces:",["Sudden storms","*Prolonged cloudiness and precipitation (neither air mass is advancing)","Clear skies","Tornadoes"],"Stationary front."),
     ("Wind blows from _____ pressure to _____ pressure.",["Low to high","*High to low (air flows from areas of high pressure toward areas of low pressure)","East to west always","North to south always"],"Pressure gradient."),
     ("The pressure gradient force is stronger when isobars on a weather map are:",["Far apart","*Close together (steep pressure gradient = stronger winds)","Parallel","Circular"],"Isobar spacing."),
     ("Convergence in a low pressure system means air at the surface is:",["Spreading out","Sinking","*Moving inward toward the center (then rising)","Not moving"],"Convergence."),
     ("Divergence in a high pressure system means air at the surface is:",["Rising","*Spreading outward from the center (sinking air at center, flowing out at surface)","Moving inward","Converging"],"Divergence."),
     ("Frontal lifting occurs when:",["Air sinks","*Air masses of different temperatures meet, and warmer air is forced upward over denser cold air","Air heats equally","Pressure is constant"],"Frontal lifting."),
     ("The dew point is the temperature at which:",["All water evaporates","Rain stops","*Air becomes saturated and water vapor begins to condense (forming clouds, dew, or fog)","Wind changes direction"],"Dew point."),
     ("A barometer measures:",["Temperature","Humidity","Wind speed","*Atmospheric pressure"],"Barometer."),
     ("If a weather map shows a large L with tightly packed isobars approaching your location, expect:",["Clear weather","Light winds","*Strong winds and precipitation (low pressure system with steep pressure gradient)","No change"],"Map reading."),
     ("Mid-latitude cyclones (low pressure storms) typically move across North America from:",["East to west","North to south","*West to east (carried by prevailing westerlies)","South to north"],"Storm tracks."),
     ("Understanding weather systems is critical for:",["Only meteorologists","*Aviation, agriculture, transportation, emergency preparedness, and daily life planning","Only farmers","Only sailors"],"Practical importance.")]
)
lessons[k]=v

# 2.4
k,v = build_lesson(2,4,"Clouds & Precipitation Types",
    "<h3>Clouds & Precipitation</h3>"
    "<h4>Cloud Classification</h4>"
    "<ul><li><b>Cirrus:</b> High, thin, wispy. Made of ice crystals.</li>"
    "<li><b>Stratus:</b> Low, flat, layered. Steady drizzle or overcast.</li>"
    "<li><b>Cumulus:</b> Puffy, vertical development. Fair weather or thunderstorms (cumulonimbus).</li>"
    "<li><b>Nimbus prefix/suffix:</b> Rain-bearing (nimbostratus, cumulonimbus).</li></ul>"
    "<h4>Precipitation Formation</h4>"
    "<ul><li><b>Bergeron process:</b> Ice crystals grow at the expense of supercooled water droplets in mixed clouds.</li>"
    "<li><b>Collision-coalescence:</b> Droplets collide and merge (warm tropical clouds).</li></ul>",
    [("Cirrus Clouds","High-altitude, thin, wispy clouds made of ice crystals; often indicate fair weather but can signal approaching fronts."),
     ("Cumulonimbus","Towering vertical cloud (thunderstorm cloud); produces heavy rain, lightning, hail, and potentially tornadoes."),
     ("Stratus Clouds","Low, flat, layered clouds covering the sky; associated with overcast conditions and steady light precipitation."),
     ("Bergeron Process","Precipitation formation in cold clouds where ice crystals grow at the expense of supercooled water droplets."),
     ("Orographic Lifting","Air forced upward by terrain (mountains); causes cloud formation and precipitation on windward side; rain shadow on leeward.")],
    [("Cirrus clouds form at _____ altitudes and are made of:",["Low; water droplets","*High (6,000+ m); ice crystals","Medium; mixed","Ground level; fog"],"Cirrus properties."),
     ("Cumulus clouds with significant vertical development can become:",["Stratus","*Cumulonimbus (thunderstorm clouds producing heavy rain, lightning, and hail)","Cirrus","Fog"],"Cumulonimbus development."),
     ("Nimbostratus clouds produce:",["Lightning only","*Steady, prolonged precipitation (continuous rain or snow)","Clear skies","Only wind"],"Nimbostratus."),
     ("Clouds form when air rises and:",["Heats up","Absorbs moisture","*Cools to its dew point, causing water vapor to condense on condensation nuclei","Loses pressure only"],"Cloud formation."),
     ("Condensation nuclei are:",["Large water drops","Ice cubes","*Tiny particles (dust, pollen, salt, pollution) that water vapor condenses onto","Not needed"],"CCN."),
     ("The Bergeron process operates in clouds that contain:",["Only liquid water","Only ice","*Both ice crystals and supercooled liquid water (mixed-phase clouds)","Only warm air"],"Bergeron conditions."),
     ("Collision-coalescence is the primary precipitation process in:",["Cold clouds","*Warm tropical clouds (where cloud tops don't reach freezing — no ice crystals)","All clouds equally","Only cirrus"],"Warm rain."),
     ("Fog is essentially a _____ at ground level.",["Cumulus cloud","*Stratus cloud (cloud formed at or near the surface)","Cirrus cloud","Cumulonimbus"],"Fog definition."),
     ("Orographic precipitation occurs when air is forced upward by:",["Cold fronts","*Mountains (terrain — windward side gets precipitation, leeward side is dry 'rain shadow')","Low pressure only","Convection"],"Orographic effect."),
     ("The rain shadow effect creates _____ conditions on the leeward side of mountains.",["Wet","*Dry (air descends, warms, and humidity drops after rain falls on the windward side)","Cold","Unchanged"],"Rain shadow."),
     ("Hail forms in:",["Stratiform clouds","*Cumulonimbus clouds (strong updrafts repeatedly lift ice particles through the cloud, adding layers of ice)","Cirrus clouds","Fog"],"Hail formation."),
     ("Sleet is formed when:",["Rain freezes in a cloud","*Rain falls through a cold layer near the surface and freezes into ice pellets before reaching the ground","Snow melts completely","Fog freezes"],"Sleet."),
     ("Freezing rain occurs when:",["Snow doesn't melt","*Rain remains liquid until it contacts a surface below 0°C and freezes on impact (dangerous ice coating)","Hail melts","Sleet bounces"],"Freezing rain."),
     ("Cloud altitude prefixes: 'alto-' means:",["Low (0-2 km)","*Mid-level (2-6 km)","High (6+ km)","Ground-level"],"Alto- prefix."),
     ("Lenticular clouds form over or downwind of:",["Oceans","Deserts","*Mountains (standing wave patterns in the airflow — often mistaken for UFOs)","Cities"],"Lenticular."),
     ("Convective precipitation results from:",["Fronts only","Orographic lifting only","*Intense surface heating causing rapid uplift (common in summer afternoon thunderstorms)","Steady rain"],"Convective precip."),
     ("The global average annual precipitation is approximately:",["50 mm","250 mm","*~1,000 mm (varies enormously from deserts <250 mm to tropical >2,000 mm)","5,000 mm"],"Global precipitation."),
     ("A weather observer reports 'overcast with steady light rain.' The clouds are likely:",["Cumulus","Cirrus","*Nimbostratus or stratus","Cumulonimbus"],"Sky observation."),
     ("Understanding cloud types helps pilots because:",["Clouds are pretty","*Different clouds indicate different hazards: turbulence (cumulonimbus), icing (certain altitudes), visibility (stratus/fog)","Clouds don't affect flight","Only for passengers"],"Aviation meteorology."),
     ("Cloud seeding attempts to increase precipitation by:",["Spraying water","Heating clouds","*Introducing condensation nuclei (silver iodide or dry ice) to stimulate ice crystal growth","Reducing humidity"],"Cloud seeding.")]
)
lessons[k]=v

# 2.5
k,v = build_lesson(2,5,"Climate Zones & Global Circulation",
    "<h3>Climate Zones & Global Circulation</h3>"
    "<h4>Global Wind Belts</h4>"
    "<ul><li><b>Trade Winds:</b> 0-30° latitude; blow NE in NH, SE in SH.</li>"
    "<li><b>Westerlies:</b> 30-60°; prevailing winds from west to east.</li>"
    "<li><b>Polar Easterlies:</b> 60-90°; cold, dry winds from the poles.</li></ul>"
    "<h4>Climate Classification (Köppen)</h4>"
    "<ul><li><b>A (Tropical):</b> Warm year-round, high precipitation.</li>"
    "<li><b>B (Dry/Arid):</b> Evaporation exceeds precipitation.</li>"
    "<li><b>C (Temperate):</b> Moderate; mild winters.</li>"
    "<li><b>D (Continental):</b> Large temperature range; cold winters.</li>"
    "<li><b>E (Polar):</b> Cold year-round.</li></ul>",
    [("Hadley Cell","Tropical convection cell: warm air rises at the equator, flows poleward, sinks at ~30° latitude."),
     ("Trade Winds","Persistent winds blowing from ~30° toward the equator; NE trades in NH, SE trades in SH."),
     ("Westerlies","Prevailing winds between 30-60° latitude blowing from west to east; drive mid-latitude weather."),
     ("Intertropical Convergence Zone (ITCZ)","Belt near the equator where trade winds converge; rising air produces heavy tropical rainfall."),
     ("Köppen Climate Classification","System categorizing climates into 5 main groups (A-E) based on temperature and precipitation patterns.")],
    [("Hadley cells circulate air between the equator and approximately _____ latitude.",["60°","90°","*30°","15°"],"Hadley extent."),
     ("The trade winds blow from the _____ toward the _____.",["Equator; poles","Poles; equator","*Subtropics (~30°); equator","West; east always"],"Trade wind direction."),
     ("The prevailing westerlies are responsible for weather in the _____ moving generally west to east.",["Tropics","*Mid-latitudes (30-60°)","Polar regions","Everywhere"],"Westerlies."),
     ("The ITCZ is characterized by:",["Dry conditions","Cold temperatures","*Heavy rainfall and rising air (convergence of trade winds at the equator)","Snow"],"ITCZ."),
     ("Deserts frequently form at ~30° N/S because:",["It's too hot","They're far from oceans","*Sinking air in the descending branch of Hadley cells creates dry, high-pressure conditions","Wind erodes everything"],"Subtropical arid."),
     ("The Coriolis effect deflects winds to the _____ in the Northern Hemisphere.",["Left","*Right","Straight up","It doesn't"],"Coriolis NH."),
     ("The horse latitudes (~30° N/S) are zones of:",["High winds","Heavy rain","*Calm, dry conditions (sinking air from Hadley cells creates subtropical highs)","Tornadoes"],"Horse latitudes."),
     ("El Niño involves _____ of the central/eastern tropical Pacific Ocean.",["Cooling","*Warming (weakened trade winds allow warm water to spread eastward, disrupting global weather patterns)","Freezing","No change"],"El Niño."),
     ("La Niña is the opposite phase, with _____ than normal Pacific waters.",["Warmer","*Cooler (strengthened trade winds, enhanced upwelling — also affects global weather)","Same temperature","Saltier"],"La Niña."),
     ("Köppen climate type A (Tropical) requires every month to have an average temperature above:",["0°C","10°C","*18°C","25°C"],"Tropical threshold."),
     ("Köppen type B (Dry) is defined by:",["Temperature","*Evaporation exceeding precipitation (potential evapotranspiration > rainfall)","Altitude","Latitude only"],"Dry climate."),
     ("Continental climates (Köppen D) are characterized by:",["Mild winters","*Large annual temperature ranges with cold winters and warm summers","Constant temperature","Only snow"],"Continental."),
     ("Ocean currents affect climate by:",["Having no effect","*Transporting heat; warm currents warm adjacent coasts, cold currents cool them (e.g., Gulf Stream warms Western Europe)","Only affecting marine life","Creating waves only"],"Ocean current climate."),
     ("The Gulf Stream carries warm water from the Gulf of Mexico to:",["South America","Asia","*Western Europe (keeping it much warmer than other regions at the same latitude)","Antarctica"],"Gulf Stream."),
     ("Monsoons are caused by:",["Only wind","Only rain","*Seasonal reversal of wind direction due to differential heating of land and ocean (summer onshore, winter offshore)","Only geography"],"Monsoon mechanism."),
     ("Rain forests occur near the equator primarily because:",["They're planted there","*Warm temperatures and heavy ITCZ rainfall year-round provide ideal growing conditions","There's no wind","It's always sunny"],"Tropical forests."),
     ("Alpine/highland climates are influenced primarily by:",["Latitude alone","*Altitude (temperature decreases ~6.5°C per km of elevation, creating climate zones on mountains)","Ocean proximity only","Longitude"],"Altitude effect."),
     ("The thermohaline circulation (global ocean conveyor belt) is driven by:",["Wind only","*Differences in water density caused by temperature and salinity variations","Tides only","Earth's rotation only"],"Thermohaline."),
     ("If the thermohaline circulation slowed or stopped, Europe would:",["Get warmer","*Get significantly colder (loss of Gulf Stream heat transport)","Be unaffected","Get drier only"],"Circulation shutdown."),
     ("Understanding global climate zones is essential for:",["Only geography class","*Agriculture, infrastructure planning, biodiversity conservation, and predicting how climate change will shift these zones","Only map-making","Only pilots"],"Climate zone importance.")]
)
lessons[k]=v

# 2.6
k,v = build_lesson(2,6,"Severe Weather (Hurricanes, Tornadoes, Blizzards)",
    "<h3>Severe Weather</h3>"
    "<h4>Hurricanes (Tropical Cyclones)</h4>"
    "<ul><li>Form over warm ocean water (≥26.5°C). Fueled by latent heat from condensation.</li>"
    "<li>Saffir-Simpson scale: Cat 1 (119 km/h) to Cat 5 (252+ km/h).</li></ul>"
    "<h4>Tornadoes</h4>"
    "<ul><li>Violently rotating column of air from a thunderstorm to the ground.</li>"
    "<li>Enhanced Fujita (EF) scale: EF0-EF5 based on damage.</li></ul>"
    "<h4>Blizzards</h4>"
    "<ul><li>Sustained winds ≥56 km/h with heavy snow (or blowing snow) reducing visibility to <400 m for ≥3 hours.</li></ul>",
    [("Hurricane","Intense tropical cyclone with sustained winds ≥119 km/h; fueled by warm ocean water (≥26.5°C); has a calm eye."),
     ("Tornado","Violently rotating column of air extending from a thunderstorm to the ground; most destructive winds on Earth."),
     ("Storm Surge","Abnormal rise in sea level caused by a hurricane's winds pushing water onshore; often the deadliest aspect."),
     ("Saffir-Simpson Scale","Rates hurricanes Category 1-5 based on sustained wind speed; Category 5 = 252+ km/h."),
     ("Enhanced Fujita Scale","Rates tornadoes EF0-EF5 based on observed damage; EF5 = total destruction of well-built structures.")],
    [("Hurricanes require ocean surface temperatures of at least:",["10°C","20°C","*26.5°C (warm water provides energy through evaporation and latent heat release)","35°C"],"Hurricane threshold."),
     ("The calm center of a hurricane is called the:",["Wall cloud","Funnel","*Eye (surrounded by the eyewall — the most intense part of the storm)","Front"],"Hurricane eye."),
     ("Storm surge is dangerous because:",["Wind alone causes it","*It's a wall of water pushed ashore by hurricane winds, causing massive coastal flooding — the #1 cause of hurricane deaths","It's cold","It's predictable"],"Storm surge danger."),
     ("Category 5 hurricanes have sustained winds of:",["119 km/h","180 km/h","*252+ km/h (catastrophic potential)","500 km/h"],"Cat 5."),
     ("Tornadoes most commonly form in association with:",["Hurricanes only","High pressure systems","*Supercell thunderstorms (rotating updrafts — mesocyclones)","Clear weather"],"Tornado source."),
     ("Tornado Alley in the US includes parts of:",["New England","*The Great Plains (Texas to Nebraska) where warm mT and cold cP air masses frequently collide","The Pacific Coast","Alaska"],"Tornado Alley."),
     ("An EF5 tornado has estimated winds of:",["65 km/h","*>322 km/h (incredible destruction — well-built homes leveled, cars thrown hundreds of meters)","150 km/h","200 km/h"],"EF5 winds."),
     ("Doppler radar detects tornadoes by measuring:",["Cloud height","Temperature","*Wind velocity and direction (identifying rotation within storms)","Rainfall only"],"Doppler radar."),
     ("A tornado watch means:",["A tornado has been spotted","*Conditions are favorable for tornado development — be prepared","The danger has passed","Stay outside"],"Watch vs. warning."),
     ("A tornado warning means:",["Conditions are favorable","*A tornado has been sighted or detected on radar — take shelter immediately","The tornado passed","It's safe"],"Warning definition."),
     ("Blizzards require all EXCEPT:",["Sustained winds ≥56 km/h","Heavy or blowing snow","Visibility <400 m","*Temperatures below -20°C (blizzards are defined by wind, snow, and visibility — not a specific temperature)"],"Blizzard criteria."),
     ("Hurricanes weaken rapidly when they:",["Reach the ocean","*Move over land or cold water (cutting off the warm water energy source)","Move toward the equator","Encounter low pressure"],"Hurricane weakening."),
     ("The Coriolis effect is necessary for hurricane rotation, which is why hurricanes:",["Form at the poles","*Don't form within ~5° of the equator (Coriolis is too weak to initiate rotation)","Only form over land","Form everywhere"],"Coriolis and hurricanes."),
     ("Hurricane Katrina (2005) was devastating primarily due to:",["Wind damage","*Storm surge (levee failures in New Orleans caused catastrophic flooding — ~1,800 deaths, $125B+ damage)","Tornadoes","Blizzard conditions"],"Katrina."),
     ("Derecho is a:",["Hurricane","Tornado","*Widespread, long-lived windstorm associated with a fast-moving band of severe thunderstorms (straight-line winds ≥93 km/h)","Blizzard"],"Derecho."),
     ("Lightning kills approximately _____ people per year in the US.",["5","*~20 (and injures hundreds more — lightning is extremely dangerous)","500","2,000"],"Lightning deaths."),
     ("The safest place during a tornado is:",["Near windows","In a car","*In a basement or interior room on the lowest floor away from windows","On the roof"],"Tornado safety."),
     ("Climate change may affect severe weather by:",["Reducing all storms","*Providing warmer oceans (potentially stronger hurricanes), more atmospheric moisture (heavier precipitation), and shifting storm patterns","Having no effect","Only increasing blizzards"],"Climate-weather link."),
     ("Microbursts are dangerous for aviation because they:",["Create fog","*Produce sudden, powerful downdrafts and wind shear that can cause aircraft to lose altitude rapidly","Are predictable","Only occur at night"],"Microburst."),
     ("Understanding severe weather is important because it:",["Is just interesting","*Saves lives through forecasting, warning systems, building codes, and emergency preparedness","Only affects rural areas","Can't be predicted"],"Severe weather importance.")]
)
lessons[k]=v

# 2.7
k,v = build_lesson(2,7,"Human Impact on Atmosphere (Pollution, Greenhouse Gases)",
    "<h3>Human Impact on the Atmosphere</h3>"
    "<h4>Air Pollution</h4>"
    "<ul><li><b>Primary pollutants:</b> Emitted directly (CO, SO₂, NOx, particulates, VOCs).</li>"
    "<li><b>Secondary pollutants:</b> Formed by reactions (ozone, smog, acid rain).</li></ul>"
    "<h4>Enhanced Greenhouse Effect</h4>"
    "<ul><li>Burning fossil fuels increases CO₂ (from ~280 ppm pre-industrial to 420+ ppm today).</li>"
    "<li>Other greenhouse gases: methane (CH₄), nitrous oxide (N₂O), fluorinated gases.</li>"
    "<li>Global average temperature has risen ~1.1°C since pre-industrial times.</li></ul>",
    [("Primary Pollutant","A pollutant emitted directly into the atmosphere from a source (e.g., CO, SO₂, particulates from burning)."),
     ("Secondary Pollutant","A pollutant formed by chemical reactions in the atmosphere (e.g., ground-level ozone formed from NOx + VOCs + sunlight)."),
     ("Acid Rain","Precipitation with pH below 5.6; formed when SO₂ and NOx react with water vapor; damages ecosystems and structures."),
     ("Enhanced Greenhouse Effect","The additional warming caused by human-added greenhouse gases beyond the natural greenhouse effect."),
     ("Carbon Footprint","Total greenhouse gas emissions caused by an individual, organization, event, or product, expressed as CO₂ equivalent.")],
    [("CO₂ levels have risen from ~280 ppm pre-industrial to over _____ ppm today.",["300","350","*420","500"],"CO₂ increase."),
     ("The primary source of anthropogenic CO₂ is:",["Respiration","Volcanoes","*Burning fossil fuels (coal, oil, natural gas)","Deforestation only"],"CO₂ source."),
     ("Ground-level ozone is a _____ pollutant.",["Primary","*Secondary (formed from reactions between NOx and VOCs in sunlight — different from protective stratospheric ozone)","Natural","Beneficial"],"Ozone type."),
     ("Acid rain forms when _____ react with atmospheric water.",["CO₂ only","Methane","*SO₂ and NOx (forming sulfuric and nitric acids)","Argon"],"Acid rain chemistry."),
     ("The pH of normal rain is approximately _____, while acid rain is below _____.",["7.0; 6.0","*5.6; 5.6 (normal rain is slightly acidic due to dissolved CO₂)","6.0; 4.0","7.0; 7.0"],"Rain pH."),
     ("Methane (CH₄) is a powerful greenhouse gas that is _____ times more effective at trapping heat than CO₂ per molecule.",["2","10","*~80 (over 20 years; ~28 times over 100 years)","1,000"],"Methane potency."),
     ("Major sources of methane include:",["Only fossil fuels","Only agriculture","*Agriculture (livestock, rice paddies), fossil fuel extraction, landfills, and wetlands","Only volcanoes"],"Methane sources."),
     ("Particulate matter (PM2.5) is dangerous because particles smaller than 2.5 μm:",["Are visible","Fall quickly","*Can penetrate deep into lungs and even enter the bloodstream, causing cardiovascular and respiratory disease","Are harmless"],"PM2.5 health."),
     ("The Clean Air Act (US, 1970) has:",["Had no effect","*Significantly reduced many pollutants despite economic growth (SO₂, lead, CO all decreased dramatically)","Only addressed CO₂","Increased pollution"],"Clean Air Act."),
     ("Temperature inversions worsen air pollution because:",["They increase wind","*Warm air traps cool air and pollutants near the surface, preventing normal dispersal (common in valleys and cities)","They cause rain","They clean the air"],"Inversions."),
     ("The global average temperature has risen approximately _____ since pre-industrial times.",["0.1°C","0.5°C","*~1.1°C","5°C"],"Observed warming."),
     ("The IPCC (Intergovernmental Panel on Climate Change) concludes that warming is:",["Natural only","Uncertain","*Unequivocally caused by human activities (primarily fossil fuel burning and deforestation)","Not happening"],"Scientific consensus."),
     ("Deforestation contributes to climate change because trees:",["Don't affect CO₂","*Absorb CO₂ during photosynthesis — cutting them down releases stored carbon AND removes a carbon sink","Only produce CO₂","Only affect local weather"],"Deforestation impact."),
     ("The carbon cycle is disrupted by fossil fuel burning because it:",["Moves carbon slowly","*Releases carbon that was stored underground for millions of years back into the atmosphere in decades","Removes carbon","Creates new carbon"],"Carbon cycle disruption."),
     ("Renewable energy sources reduce atmospheric pollution because they:",["Require no infrastructure","*Produce little to no greenhouse gases or air pollutants during operation (solar, wind, hydro)","Are free","Are always available"],"Renewable benefit."),
     ("Sea level rise from climate change is caused by:",["Only glacier melting","Only thermal expansion","*Both thermal expansion of warming water AND melting of land ice (glaciers and ice sheets)","Only rainfall"],"Sea level causes."),
     ("An individual can reduce their carbon footprint by:",["Doing nothing","*Driving less, using renewable energy, eating less meat, reducing consumption, and supporting clean energy policies","Only recycling","Only buying electric cars"],"Individual action."),
     ("Carbon capture and storage (CCS) technology aims to:",["Increase emissions","*Capture CO₂ from power plants and industrial sources and store it underground","Release more CO₂","Only the monitoring of CO₂"],"CCS."),
     ("Indoor air pollution from cooking fuels kills approximately _____ people worldwide annually.",["1,000","100,000","*~4 million (mostly in developing countries using solid fuels in poorly ventilated homes)","None"],"Indoor pollution."),
     ("Addressing atmospheric pollution requires:",["Only technology","Only policy","Only individual action","*A combination of technology, policy, international cooperation, and individual choices — it's a systemic challenge"],"Comprehensive solution.")]
)
lessons[k]=v

# 2.8
k,v = build_lesson(2,8,"Weather Prediction Models",
    "<h3>Weather Prediction</h3>"
    "<h4>Numerical Weather Prediction (NWP)</h4>"
    "<ul><li>Computer models solve atmospheric equations using current observations as initial conditions.</li>"
    "<li>Models like GFS, ECMWF, NAM use different resolutions and physics.</li></ul>"
    "<h4>Data Sources</h4>"
    "<ul><li>Surface stations, weather balloons (radiosondes), satellites, radar, aircraft, ocean buoys.</li></ul>"
    "<h4>Forecast Accuracy</h4>"
    "<ul><li>3-day forecasts now are as accurate as 1-day forecasts were 30 years ago.</li>"
    "<li>Accuracy decreases significantly beyond ~10 days (chaos theory).</li></ul>",
    [("Numerical Weather Prediction","Computer models that solve atmospheric physics equations using current observations to forecast future weather."),
     ("Radiosonde","Instrument package carried by weather balloon that measures temperature, humidity, pressure, and wind through the atmosphere."),
     ("Doppler Radar","Radar that measures precipitation intensity AND wind velocity/direction by detecting the Doppler shift of returned signals."),
     ("Ensemble Forecasting","Running multiple model simulations with slightly varied initial conditions to assess forecast uncertainty and probability."),
     ("Chaos Theory","Sensitivity to initial conditions means small errors grow over time, limiting weather forecast reliability beyond ~10 days.")],
    [("Modern weather forecasting relies primarily on:",["Almanacs","Animal behavior","*Numerical weather prediction (NWP) models run on supercomputers","Only surface observations"],"NWP basis."),
     ("The GFS and ECMWF are:",["Satellite types","Radar networks","*Major global weather prediction models (Global Forecast System and European Centre for Medium-Range Weather Forecasts)","Observation stations"],"Model names."),
     ("Radiosondes are launched twice daily from hundreds of stations worldwide to measure:",["Only temperature","Only pressure","*Temperature, humidity, pressure, and wind speed/direction through the atmosphere (vertical profile)","Only wind"],"Radiosonde."),
     ("Weather satellites in geostationary orbit:",["Move with weather systems","Orbit the poles","*Remain stationary relative to Earth's surface at ~36,000 km, providing continuous coverage of one region","Are on the ground"],"Geostationary."),
     ("Polar-orbiting satellites provide:",["Continuous single-region coverage","*Global coverage by orbiting from pole to pole as Earth rotates beneath them (higher resolution than geostationary)","Only ocean data","Only nighttime imagery"],"Polar orbit."),
     ("Doppler radar is particularly valuable for detecting:",["Only rainfall amount","*Rotation within thunderstorms (potential tornadoes) via wind velocity measurements","Only temperature","Only cloud height"],"Doppler value."),
     ("Weather model resolution refers to:",["Screen resolution","*The size of grid cells in the model (smaller = more detail but more computationally expensive)","Image quality only","Number of models"],"Model resolution."),
     ("Ensemble forecasting runs multiple simulations to:",["Save time","*Quantify forecast uncertainty — if most runs agree, confidence is high; if they diverge, the forecast is uncertain","Use less data","Reduce computing"],"Ensemble purpose."),
     ("A 5-day forecast is generally:",["Perfect","Useless","*Reasonably accurate for temperature/precipitation trends but becomes less precise with each day","Only 10% accurate"],"5-day accuracy."),
     ("Forecasts beyond ~10 days are unreliable due to:",["Lack of data","Bad models","*Chaos — tiny errors in initial conditions amplify exponentially over time (the 'butterfly effect')","No interest"],"Chaos limit."),
     ("The 'butterfly effect' suggests that:",["Butterflies cause storms","*Small perturbations in initial conditions can lead to vastly different outcomes — inherent limit on prediction","Weather is random","Models are useless"],"Butterfly effect."),
     ("Weather model accuracy has improved because of:",["Only better computers","Only more observations","*Better computers, more data (satellites, radar), improved physics in models, and better data assimilation techniques","Luck"],"Improvement factors."),
     ("Data assimilation is the process of:",["Deleting old data","*Combining observations with model predictions to create the best possible estimate of current atmospheric conditions (initial conditions)","Storing data","Only surface readings"],"Data assimilation."),
     ("A model's forecast is only as good as its:",["User","*Initial conditions and the physics it represents (garbage in = garbage out)","Screen display","Speed"],"Model quality."),
     ("Automated weather stations measure:",["Only temperature","*Temperature, humidity, pressure, wind, precipitation, and visibility automatically and continuously","Only wind","Only rainfall"],"Auto stations."),
     ("Aircraft Meteorological Data Relay (AMDAR) provides:",["Only runway conditions","*Temperature, wind, and humidity measurements during flights — a major data source for upper atmosphere","Only turbulence data","Pilot opinions"],"Aircraft data."),
     ("Nowcasting (0-6 hour forecasts) relies heavily on:",["Only NWP models","*Current radar and satellite observations (extrapolating current weather features forward)","Only surface data","Historical data"],"Nowcasting."),
     ("AI and machine learning are being applied to weather prediction to:",["Replace all models","*Improve pattern recognition, post-processing of model output, and potentially faster and more accurate short-term forecasts","Make weather controllable","Only for historical analysis"],"AI meteorology."),
     ("Climate models differ from weather models because they:",["Are the same thing","*Focus on long-term (decades to centuries) trends and averages rather than day-to-day weather predictions","Don't use computers","Only study storms"],"Climate vs. weather models."),
     ("Improved weather forecasting saves lives and money by:",["Only being interesting","*Enabling evacuations for severe weather, optimizing agriculture, aviation, transportation, and energy decisions","Only affecting meteorologists","Having no economic value"],"Forecasting value.")]
)
lessons[k]=v

# 2.9
k,v = build_lesson(2,9,"Case Studies in Climate Events",
    "<h3>Case Studies in Climate Events</h3>"
    "<h4>El Niño / La Niña (ENSO)</h4>"
    "<p>El Niño: warm Pacific → increased US winter rainfall, droughts in Australia. La Niña: cool Pacific → more Atlantic hurricanes, flooding in SE Asia.</p>"
    "<h4>Drought & Heat Events</h4>"
    "<p>2012 US drought (worst since 1950s). European heat wave 2003 (~70,000 excess deaths). Rising frequency linked to climate change.</p>"
    "<h4>Polar Vortex Events</h4>"
    "<p>Weakened polar vortex allows Arctic air to plunge into mid-latitudes, causing extreme cold events (e.g., February 2021 Texas freeze).</p>",
    [("ENSO (El Niño-Southern Oscillation)","Climate pattern of Pacific Ocean temperature oscillation; El Niño (warm) and La Niña (cool) affect global weather."),
     ("Polar Vortex","A band of cold air circling the Arctic; when it weakens, it can allow frigid air to plunge into mid-latitudes."),
     ("Drought","Extended period of below-normal precipitation causing water shortages; can be worsened by higher temperatures increasing evaporation."),
     ("Heat Wave","Prolonged period of excessive heat; exacerbated by urban heat islands, humidity, and climate change."),
     ("Attribution Science","Field that determines how much climate change contributed to the likelihood or intensity of a specific weather event.")],
    [("El Niño events occur every _____ years on average.",["1","*2-7 (irregular but recurrent)","10-20","50"],"ENSO frequency."),
     ("During El Niño, the eastern tropical Pacific becomes _____ than normal.",["Cooler","Saltier","*Warmer (weakened trade winds allow warm water to spread east)","Deeper"],"El Niño Pacific."),
     ("El Niño typically brings to the southern US:",["Drought","*Increased rainfall and flooding (especially California and the Gulf states)","Colder temperatures","No effect"],"El Niño US impact."),
     ("La Niña tends to increase:",["US winter rainfall","Pacific hurricanes","*Atlantic hurricane activity (reduced wind shear in the Atlantic basin)","Snowfall everywhere"],"La Niña hurricanes."),
     ("The 2003 European heat wave killed approximately _____ people.",["1,000","10,000","*~70,000 (one of the deadliest natural disasters in European history)","100,000"],"2003 heat wave."),
     ("Heat waves are becoming more frequent and intense due to:",["Only urban growth","Natural cycles only","*Climate change (higher baseline temperatures mean extreme heat events are more likely and more severe)","Reduced wind"],"Heat-climate link."),
     ("The 2021 Texas freeze was caused by:",["Normal winter weather","Global warming making it colder","*A weakened polar vortex allowing Arctic air to plunge deep into the southern US","A hurricane"],"Texas freeze."),
     ("During the Texas freeze, the power grid failed because:",["Power lines froze","*Natural gas infrastructure, wind turbines, and power plants were not winterized for extreme cold — widespread outages","There was no wind","Solar panels failed only"],"Grid failure."),
     ("The Dust Bowl of the 1930s was caused by:",["Only weather","Only farming","*A combination of severe drought AND poor farming practices that stripped protective grassland, exposing soil to wind erosion","Only industrialization"],"Dust Bowl."),
     ("Attribution science can determine:",["Exact future events","*How much climate change increased the probability or intensity of a specific weather event (e.g., 'this heat wave was 5× more likely due to climate change')","Nothing useful","Only past events exactly"],"Attribution."),
     ("Droughts reduce agricultural output, leading to:",["Lower food prices","*Higher food prices, food insecurity, economic losses, and potential social instability","More crops","Better harvests"],"Drought impacts."),
     ("The 2019-2020 Australian bushfires were intensified by:",["Only arson","*Record heat, drought, and climate change creating extreme fire conditions","Only lightning","Only wind"],"Australia fires."),
     ("Monsoon variability can cause:",["Only flooding","Only drought","*Both — too much monsoon rainfall causes devastating floods; too little causes drought and famine (affects billions in South Asia)","Neither"],"Monsoon impacts."),
     ("Hurricane Harvey (2017) was notable for:",["Wind damage mainly","*Exceptional rainfall (~1,500 mm in some areas) — climate warming increases atmospheric moisture, making heavy rain events heavier","Cold temperatures","Its track over the Atlantic"],"Harvey rainfall."),
     ("Climate change is expected to make wet regions _____ and dry regions _____.",["Drier; wetter","*Wetter; drier ('wet get wetter, dry get drier' — amplification of existing precipitation patterns)","Both wetter","Both drier"],"Precipitation changes."),
     ("Ice core records show that past climate changes:",["Were always gradual","Never involved CO₂","*Correlate strongly with CO₂ levels — and current CO₂ rise is far faster than any natural change in the record","Were random"],"Ice core evidence."),
     ("The Pacific Decadal Oscillation (PDO) is:",["An annual event","*A long-term (20-30 year) pattern of Pacific climate variability that modulates ENSO and affects North American weather","A single storm","A policy decision"],"PDO."),
     ("Compound events (e.g., heat + drought + wildfire) are concerning because:",["They cancel out","*The combined impact is far worse than individual events — and climate change is increasing the likelihood of multiple hazards occurring simultaneously","They're rare","They only affect one region"],"Compound events."),
     ("Insurance losses from weather-related disasters have:",["Decreased","Stayed constant","*Increased dramatically (due to climate change intensifying events AND more people/property in vulnerable areas)","Only changed in one region"],"Economic trend."),
     ("Studying climate events teaches us that:",["We can't do anything","*Understanding climate systems enables better preparation, adaptation, and mitigation — science-informed policy saves lives and money","They're unpredictable","Historical events don't repeat"],"Lesson of case studies.")]
)
lessons[k]=v

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Integrated Science Unit 2: wrote {len(lessons)} lessons")
