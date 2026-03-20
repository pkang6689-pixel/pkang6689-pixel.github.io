#!/usr/bin/env python3
"""Astronomy Unit 3 – The Solar System (8 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "astronomy_lessons.json")
COURSE = "Astronomy"

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

# 3.1
k,v = build_lesson(3,1,"Formation of the Solar System",
    "<h3>Formation of the Solar System</h3>"
    "<p><b>Nebular Hypothesis:</b> ~4.6 billion years ago, a giant molecular cloud (solar nebula) collapsed — possibly triggered by a nearby supernova. Conservation of angular momentum caused the collapsing cloud to spin and flatten into a protoplanetary disk.</p>"
    "<h4>Steps</h4>"
    "<ul><li>Core heats → proto-Sun ignites hydrogen fusion.</li>"
    "<li>Dust grains collide and stick → planetesimals → protoplanets (accretion).</li>"
    "<li>Inner disk: too hot for volatiles → rocky terrestrial planets.</li>"
    "<li>Outer disk: frost line → ices + gas accumulate → gas/ice giants.</li>"
    "<li>Solar wind clears remaining gas; late heavy bombardment shapes surfaces.</li></ul>",
    [("Nebular Hypothesis","Solar system formed from a collapsing, rotating cloud of gas and dust ~4.6 Gya."),
     ("Protoplanetary Disk","Flattened disk of gas and dust orbiting the young Sun; planets formed within it."),
     ("Accretion","Process of growth by collisions: dust → planetesimals → protoplanets → planets."),
     ("Frost Line","Distance from the Sun beyond which water and volatiles could condense as ice (~3-5 AU)."),
     ("Late Heavy Bombardment","Period ~4.1–3.8 Gya of intense asteroid/comet impacts throughout the inner solar system.")],
    [("The solar system formed approximately:",["1 billion years ago","10 billion years ago","*4.6 billion years ago","100 million years ago"],"Radiometric dating of meteorites."),
     ("The nebular hypothesis explains:",["Only star formation","*The formation of the entire solar system from a collapsing gas-and-dust cloud","Only planet formation","Only comet origins"],"Comprehensive formation model."),
     ("The protoplanetary disk formed because of:",["Magnetism","*Conservation of angular momentum (collapsing cloud spins faster and flattens)","The Sun's light","Random motion"],"Angular momentum is conserved."),
     ("Accretion is the process by which:",["Stars explode","*Small particles collide and stick together, building larger bodies over time","Planets lose mass","Moons form oceans"],"Growth from dust to planets."),
     ("The frost line is approximately _____ AU from the Sun.",["0.5","1","*3–5 AU","50"],"Beyond this, ices can condense."),
     ("Inside the frost line, planets are mostly:",["Gaseous","Icy","*Rocky (terrestrial) — too hot for volatiles to condense","Liquid"],"Mercury, Venus, Earth, Mars."),
     ("Beyond the frost line, planets could accumulate:",["Only rock","*Large amounts of ice and gas, becoming gas/ice giants","Only metal","Nothing"],"Jupiter, Saturn, etc."),
     ("The Sun ignited when:",["It was hit by a comet","*The core of the proto-Sun reached ~10 million K, initiating hydrogen fusion","It absorbed enough light","Gravity stopped"],"Nuclear fusion threshold."),
     ("Evidence for the nebular hypothesis includes:",["Only theoretical models","*The planets orbiting in the same plane and direction, plus isotopic analysis of meteorites","Only telescopes","Only simulations"],"Multiple lines of evidence."),
     ("Planetesimals are:",["Full-sized planets","*Intermediate bodies (km-scale) formed by accretion of dust and small particles","Stars","Moons"],"Building blocks of planets."),
     ("The late heavy bombardment occurred approximately:",["100 years ago","*4.1–3.8 billion years ago","1 million years ago","At the Big Bang"],"Intense cratering period."),
     ("What likely triggered the initial collapse of the solar nebula?",["Sunlight","*A nearby supernova shock wave","Magnetic fields only","Nothing specific"],"One leading hypothesis."),
     ("All planets orbit in roughly the same plane because:",["Gravity pulls them flat","*They formed from the same flattened protoplanetary disk","The Sun is flat","Random chance"],"Inherited disk geometry."),
     ("Most planets orbit the Sun in the _____ direction.",["Clockwise (from above)","*Counterclockwise (prograde, from above the North Pole)","Random directions","No consistent direction"],"Inherited rotation of the original nebula."),
     ("Chondrites (primitive meteorites) are important because:",["They're pretty","*They preserve the original composition of the early solar nebula","They come from Mars","They contain life"],"Time capsules of the early solar system."),
     ("Differentiation in early planets means:",["They stayed uniform","*Heavier elements (iron) sank to cores while lighter materials rose to surfaces","They split apart","They lost mass"],"Density-driven layering."),
     ("The Nice model explains:",["Earth's formation","*The migration of giant planets and the late heavy bombardment","Star formation","Galaxy formation"],"Giant planet orbital restructuring."),
     ("Our solar system's formation took approximately _____ to go from nebula to mature planets.",["1 year","1,000 years","*~100 million years for the main accretion phase","10 billion years"],"Rapid on cosmic timescales."),
     ("Studying exoplanetary systems has:",["Disproved the nebular hypothesis","*Confirmed and refined our understanding (many systems show disks and forming planets)","Had no impact","Only confused scientists"],"Direct imaging of protoplanetary disks."),
     ("Understanding solar system formation connects:",["Nothing","*Astronomy, physics, chemistry, and geology","Only astronomy","Only physics"],"Interdisciplinary topic.")]
)
lessons[k]=v

# 3.2
k,v = build_lesson(3,2,"Terrestrial Planets",
    "<h3>Terrestrial Planets</h3>"
    "<p>Mercury, Venus, Earth, Mars — the four inner, rocky planets.</p>"
    "<h4>Characteristics</h4>"
    "<ul><li><b>Mercury:</b> Smallest; no atmosphere; extreme temperature swings (−180°C to 430°C); heavily cratered.</li>"
    "<li><b>Venus:</b> Dense CO₂ atmosphere; runaway greenhouse → ~465°C surface; retrograde rotation; similar size to Earth.</li>"
    "<li><b>Earth:</b> Liquid water; magnetic field; plate tectonics; supports life.</li>"
    "<li><b>Mars:</b> Thin CO₂ atmosphere; Olympus Mons (tallest volcano); Valles Marineris; evidence of past water.</li></ul>",
    [("Terrestrial Planet","Rocky planet with solid surface; relatively small with high density (Mercury, Venus, Earth, Mars)."),
     ("Runaway Greenhouse Effect","Positive feedback loop on Venus: CO₂ traps heat → oceans evaporate → more greenhouse gases → hotter."),
     ("Olympus Mons","Largest known volcano in the solar system, on Mars; ~22 km high, ~600 km wide."),
     ("Plate Tectonics","Earth's lithosphere is divided into moving plates; drives earthquakes, volcanism, mountain building."),
     ("Retrograde Rotation","Rotation opposite to orbital direction; Venus rotates clockwise (east to west); very slow (~243 Earth days).")],
    [("How many terrestrial planets are in our solar system?",["2","3","*4 (Mercury, Venus, Earth, Mars)","6"],"Inner rocky worlds."),
     ("Which terrestrial planet is the smallest?",["Mars","Venus","*Mercury","Earth"],"~4,880 km diameter."),
     ("Venus's surface temperature (~465°C) is due to:",["Proximity to the Sun alone","*A runaway greenhouse effect from its dense CO₂ atmosphere","Volcanic activity alone","Nuclear reactions"],"Atmosphere traps enormous heat."),
     ("Venus rotates:",["Rapidly like Jupiter","The same direction as Earth","*Retrograde (backward) and very slowly (~243 Earth days per rotation)","Not at all"],"Unique among planets."),
     ("Earth is unique among terrestrial planets because it has:",["The most craters","*Liquid water on its surface, a magnetic field, and active plate tectonics","The thickest atmosphere","The most moons"],"Conditions supporting life."),
     ("Mars is known as the Red Planet because:",["It's hot","*Iron oxide (rust) on its surface gives it a reddish appearance","It's close to the Sun","It has red oceans"],"Oxidized iron."),
     ("Olympus Mons on Mars is:",["A small hill","*The largest known volcano in the solar system (~22 km high)","A crater","An ocean basin"],"Enormous shield volcano."),
     ("Valles Marineris on Mars is:",["A small valley","*A vast canyon system ~4,000 km long and up to 7 km deep","A volcano","A river"],"Dwarfs Earth's Grand Canyon."),
     ("Mercury's extreme temperature swings are because:",["It has a thick atmosphere","*It has virtually no atmosphere to retain or distribute heat","It's made of ice","The Sun is inconsistent"],"−180°C night to 430°C day."),
     ("Evidence of past liquid water on Mars includes:",["Only theoretical models","*Dry riverbeds, mineral deposits, polar ice caps, and rover findings","Only ice at poles","No evidence exists"],"Multiple lines of evidence."),
     ("The terrestrial planets formed inside the frost line where:",["Everything was cold","*It was too hot for ices and gases to condense, leaving rocky/metallic materials","There was no gravity","The Sun didn't shine"],"Rocky materials survived."),
     ("Earth's magnetic field is generated by:",["Solar wind","The atmosphere","*Convection currents in its liquid iron outer core (dynamo effect)","Surface rocks"],"Geodynamo."),
     ("Mars likely lost its magnetic field because:",["It never had one","*Its core cooled and solidified, stopping the dynamo","The Sun demagnetized it","Its moons pulled it away"],"Smaller planet cooled faster."),
     ("Venus has no detectable magnetic field, possibly because:",["It's too hot","*Its very slow rotation limits dynamo action despite having a liquid core","It has no core","Solar wind destroyed it"],"Slow rotation hypothesis."),
     ("Mercury has a surprisingly large iron core (~75% of its radius), possibly because:",["It formed that way","*A giant impact stripped away much of its outer rocky mantle","Iron migrated there","The Sun pulled outer layers"],"Impact hypothesis."),
     ("Comparative planetology studies:",["Only Earth","*How different conditions on similar worlds lead to different outcomes","Only gas giants","Only moons"],"Comparing terrestrial planets reveals processes."),
     ("The density of terrestrial planets is generally _____ that of gas giants.",["Less than","Equal to","*Greater than (~4–5.5 g/cm³ vs ~0.7–1.6 g/cm³)","Unrelated to"],"Rock and metal vs gas."),
     ("Mars's thin atmosphere (~1% of Earth's) means:",["Surface pressure is high","*Liquid water cannot exist on the surface now (too low pressure)","It's very warm","There's lots of oxygen"],"Low pressure = sublimation/evaporation."),
     ("Which terrestrial planet has the most moons?",["Venus","Mercury","Earth","*Mars (Phobos and Deimos)"],"Two small moons (Earth has 1; Mercury and Venus have 0)."),
     ("Studying terrestrial planets helps us understand:",["Nothing about Earth","*Earth's geology, climate, habitability, and the potential for life elsewhere","Only Mars","Only space travel"],"Broader context for Earth science.")]
)
lessons[k]=v

# 3.3
k,v = build_lesson(3,3,"Gas Giants",
    "<h3>Gas Giants (Jovian Planets)</h3>"
    "<h4>Jupiter</h4>"
    "<p>Largest planet; mostly H/He; Great Red Spot (persistent storm); strong magnetosphere; 95+ known moons (Io, Europa, Ganymede, Callisto are Galilean moons).</p>"
    "<h4>Saturn</h4>"
    "<p>Famous ring system (mostly ice particles); density < water (~0.69 g/cm³); 146+ known moons (Titan has thick atmosphere).</p>"
    "<h4>Uranus &amp; Neptune (Ice Giants)</h4>"
    "<ul><li><b>Uranus:</b> Extreme axial tilt (~98°, rolls on its side); blue-green from methane; 27 known moons.</li>"
    "<li><b>Neptune:</b> Strong winds (2,100 km/h); deep blue; Triton (large retrograde moon). Both have interiors rich in water, ammonia, methane ices.</li></ul>",
    [("Jovian Planet","Large, gaseous planet with low density, thick atmosphere, and many moons (Jupiter, Saturn)."),
     ("Ice Giant","Outer planets (Uranus, Neptune) with interiors rich in water, ammonia, and methane ices."),
     ("Great Red Spot","Jupiter's massive anticyclonic storm; larger than Earth; observed for over 350 years."),
     ("Galilean Moons","Jupiter's four largest moons discovered by Galileo: Io, Europa, Ganymede, Callisto."),
     ("Ring System","Disk of ice and rock particles orbiting a planet; Saturn's are the most prominent.")],
    [("The largest planet in our solar system is:",["Saturn","Earth","*Jupiter","Neptune"],"~11× Earth's diameter."),
     ("Jupiter is composed primarily of:",["Rock and iron","Water and ice","*Hydrogen and helium","Carbon dioxide"],"Similar composition to the Sun."),
     ("The Great Red Spot on Jupiter is:",["A mountain","A crater","*A massive, long-lived storm (anticyclone) larger than Earth","A volcano"],"Observed for centuries."),
     ("The Galilean moons of Jupiter are:",["Mercury, Venus, Earth, Mars","*Io, Europa, Ganymede, Callisto","Titan, Triton, Charon, Phobos","All 95+ moons"],"Discovered by Galileo in 1610."),
     ("Europa is of great interest to astrobiologists because:",["It has an atmosphere","*It likely has a subsurface liquid water ocean beneath its icy crust","It's the largest moon","It's closest to the Sun"],"Potential habitat."),
     ("Saturn's density is:",["Very high","Same as Earth","*Less than water (~0.69 g/cm³ — it would float!)","Zero"],"Least dense planet."),
     ("Saturn's rings are mostly composed of:",["Gas","Liquid water","*Ice particles (with some rock), ranging in size from tiny grains to house-sized chunks","Metal"],"Primarily water ice."),
     ("Titan (Saturn's moon) is remarkable because:",["It's the smallest moon","*It has a thick nitrogen atmosphere and liquid methane/ethane lakes on its surface","It has no atmosphere","It's made of metal"],"Only moon with a dense atmosphere."),
     ("Uranus's extreme axial tilt (~98°) means:",["It spins fast","*It essentially rolls on its side as it orbits the Sun","It has no seasons","It tilts toward the Sun always"],"Possibly caused by a giant impact."),
     ("The blue-green color of Uranus is due to:",["Oceans","Oxygen","*Methane in its atmosphere absorbing red light","Algae"],"Methane absorption."),
     ("Neptune has the strongest _____ in the solar system.",["Gravity","Magnetism","*Winds (up to ~2,100 km/h)","Rings"],"Supersonic wind speeds."),
     ("Triton (Neptune's largest moon) orbits retrograde, which suggests:",["It formed with Neptune","*It was captured from the Kuiper Belt","It was always retrograde","Nothing"],"Retrograde orbit = likely captured."),
     ("Ice giants differ from gas giants primarily in:",["Size only","Color only","*Interior composition — ice giants have more water, ammonia, and methane ices; less H/He","Nothing"],"Different internal makeup."),
     ("How many known moons does Jupiter have (as of recent count)?",["4","16","*95+ (and counting)","2"],"Regular and irregular moons."),
     ("Saturn's moon Enceladus is interesting because:",["It's the largest","*It has geysers of water vapor erupting from subsurface ocean through ice cracks","It has rings","It has an atmosphere like Titan"],"Ocean world candidate."),
     ("The Roche limit explains why:",["Moons form far away","*Ring particles close to a planet cannot coalesce into moons (tidal forces prevent it)","Planets have atmospheres","Stars have planets"],"Tidal disruption zone."),
     ("Jupiter's magnetic field is:",["Weak","Nonexistent","*The strongest of any planet (~20,000× Earth's)","Same as Earth's"],"Enormous magnetosphere."),
     ("Gas giants formed beyond the frost line because:",["They were pushed there","*Ices could condense there, adding mass for cores to accrete huge gas envelopes","It was darker","There was more gravity"],"More solid material → bigger cores → captured gas."),
     ("Voyager 2 is the only spacecraft to have visited:",["Only Jupiter","*Both Uranus and Neptune (flyby in 1986 and 1989)","Only Mars","Saturn's rings"],"Unique mission."),
     ("Studying gas/ice giants helps us understand:",["Nothing about other star systems","*Exoplanet diversity, planet formation, and atmospheric physics","Only our solar system","Only Jupiter"],"Many exoplanets are giant planets.")]
)
lessons[k]=v

# 3.4
k,v = build_lesson(3,4,"Dwarf Planets & Asteroids",
    "<h3>Dwarf Planets &amp; Asteroids</h3>"
    "<h4>Dwarf Planets</h4>"
    "<p>Orbit the Sun, have enough mass for hydrostatic equilibrium (round shape), but have NOT cleared their orbital neighborhood. Examples: Pluto, Eris, Haumea, Makemake, Ceres.</p>"
    "<h4>Asteroids</h4>"
    "<p>Rocky/metallic remnants from the early solar system. Most are in the asteroid belt (between Mars and Jupiter). Types: C-type (carbonaceous), S-type (silicaceous), M-type (metallic).</p>"
    "<p>Near-Earth Asteroids (NEAs) are monitored for potential impact hazards. Missions: NEAR Shoemaker, Hayabusa2, OSIRIS-REx, DART.</p>",
    [("Dwarf Planet","Orbits the Sun, spherical, but hasn't cleared its orbital neighborhood (e.g., Pluto, Ceres)."),
     ("Asteroid Belt","Region between Mars and Jupiter containing most asteroids; total mass < Earth's Moon."),
     ("Near-Earth Asteroid","Asteroid with orbit that brings it close to Earth's orbit; monitoring for impact risk."),
     ("C-type Asteroid","Carbonaceous asteroid; most common type; dark, primitive composition."),
     ("DART Mission","NASA's Double Asteroid Redirection Test (2022); demonstrated kinetic impactor deflection of asteroid Dimorphos.")],
    [("A dwarf planet differs from a planet because it:",["Is too small","Has no gravity","*Has not cleared its orbital neighborhood of other debris","Doesn't orbit the Sun"],"IAU definition (2006)."),
     ("Pluto was reclassified as a dwarf planet in:",["1990","*2006 (by the IAU)","2020","1950"],"Controversial but based on orbital clearing criterion."),
     ("The largest object in the asteroid belt is:",["An asteroid","*Ceres (also classified as a dwarf planet, ~950 km diameter)","Pluto","Jupiter"],"Only dwarf planet in the inner solar system."),
     ("Most asteroids are found:",["Near Earth","Beyond Neptune","*In the asteroid belt between Mars and Jupiter","Inside Mercury's orbit"],"Main belt."),
     ("The total mass of the asteroid belt is:",["As much as Earth","As much as the Moon","*Less than 4% of the Moon's mass","More than Jupiter"],"Surprisingly little total mass."),
     ("C-type (carbonaceous) asteroids are:",["Bright and metallic","*Dark, carbon-rich, and the most common type","Only found near Earth","Made of ice"],"Primitive composition."),
     ("S-type asteroids are mostly composed of:",["Carbon","*Silicate minerals and some metals","Pure iron","Ice"],"Rocky, moderate brightness."),
     ("M-type asteroids are primarily:",["Rocky","Icy","*Metallic (iron-nickel)","Gaseous"],"May be cores of differentiated bodies."),
     ("Near-Earth Asteroids (NEAs) are monitored because:",["They are beautiful","*Some could potentially impact Earth, posing hazards","They contain gold","They block sunlight"],"Planetary defense."),
     ("The DART mission (2022) succeeded in:",["Landing on an asteroid","*Deflecting the asteroid Dimorphos by kinetic impact (changed its orbit)","Mining an asteroid","Discovering a new asteroid"],"First planetary defense test."),
     ("OSIRIS-REx successfully:",["Observed Jupiter","*Collected a sample from asteroid Bennu and returned it to Earth (2023)","Landed on Mars","Deflected a comet"],"Sample return mission."),
     ("Hayabusa2 returned samples from:",["The Moon","Mars","*Asteroid Ryugu","Ceres"],"JAXA mission."),
     ("Eris is a dwarf planet located in:",["The asteroid belt","*The scattered disk (beyond Neptune's orbit), larger than Pluto in mass","The inner solar system","Jupiter's orbit"],"Its discovery helped trigger Pluto's reclassification."),
     ("The Kirkwood gaps in the asteroid belt are:",["Filled with asteroids","*Orbital resonance zones with Jupiter where asteroids are depleted","Caused by Mars","Random"],"Jupiter's gravity creates gaps."),
     ("Trojan asteroids share an orbit with:",["Earth","Mars","*Jupiter (at Lagrange points L4 and L5)","Saturn"],"Gravitationally stable regions."),
     ("Binary asteroids (two orbiting each other) are:",["Impossible","*Relatively common; DART's target Dimorphos orbits Didymos","Only theoretical","Extremely rare"],"Many asteroids have companions."),
     ("Asteroids provide information about:",["Nothing useful","*The early solar system's composition and conditions (they are primitive remnants)","Only future mining","Only impact risks"],"Time capsules."),
     ("Asteroid mining in the future could provide:",["Nothing","*Metals (platinum, iron, nickel), water, and other resources","Only research data","Only tourism"],"Potential resource."),
     ("The Chicxulub impact ~66 million years ago was caused by:",["A comet","*A ~10 km asteroid that struck the Yucatán Peninsula, contributing to dinosaur extinction","A volcanic eruption","A meteoroid"],"Major extinction event."),
     ("Understanding asteroids and dwarf planets helps us:",["Not at all","*Understand solar system formation, assess impact risks, and plan future exploration","Only pass exams","Only name celestial objects"],"Scientific and practical importance.")]
)
lessons[k]=v

# 3.5
k,v = build_lesson(3,5,"Comets & Meteoroids",
    "<h3>Comets &amp; Meteoroids</h3>"
    "<h4>Comets</h4>"
    "<p>Icy bodies ('dirty snowballs') from the Kuiper Belt or Oort Cloud. As they approach the Sun, ices sublimate → coma and tails (ion tail points away from Sun; dust tail curves).</p>"
    "<h4>Meteors &amp; Meteorites</h4>"
    "<ul><li><b>Meteoroid:</b> Small rocky/metallic debris in space.</li>"
    "<li><b>Meteor:</b> Streak of light when a meteoroid enters Earth's atmosphere ('shooting star').</li>"
    "<li><b>Meteorite:</b> Remnant that reaches the ground.</li>"
    "<li>Meteor showers occur when Earth passes through a comet's debris trail (e.g., Perseids from Comet Swift-Tuttle).</li></ul>",
    [("Comet","Icy body from the Kuiper Belt or Oort Cloud; develops coma and tails when near the Sun."),
     ("Oort Cloud","Spherical shell of icy bodies at ~2,000–200,000 AU; source of long-period comets."),
     ("Kuiper Belt","Disk of icy objects beyond Neptune (~30–50 AU); source of short-period comets and dwarf planets."),
     ("Meteor","Streak of light (shooting star) produced when a meteoroid burns up in Earth's atmosphere."),
     ("Meteor Shower","Increased meteor activity when Earth passes through a comet's debris trail.")],
    [("A comet's nucleus is primarily composed of:",["Rock only","Metal","*Ice (water, CO₂, CO) mixed with dust and rock — 'dirty snowball'","Gas"],"Icy core."),
     ("The Kuiper Belt is located:",["Between Mars and Jupiter","Inside Earth's orbit","*Beyond Neptune (~30–50 AU)","Near the Sun"],"Source of short-period comets."),
     ("The Oort Cloud is:",["A visible nebula","*A hypothesized spherical shell of icy bodies at ~2,000–200,000 AU from the Sun","A cloud on Earth","A galaxy"],"Source of long-period comets."),
     ("A comet's ion tail always points:",["Toward the Sun","Along the orbit","*Away from the Sun (pushed by solar wind)","Toward Earth"],"Solar wind drives ionized gas."),
     ("A comet's dust tail:",["Points toward the Sun","*Curves along the comet's orbit (pushed by solar radiation pressure)","Is invisible","Doesn't exist"],"Slightly different direction from ion tail."),
     ("The coma of a comet is:",["The tail","*The cloud of gas and dust surrounding the nucleus when heated by the Sun","The nucleus","The orbit"],"Can be larger than Earth."),
     ("A meteoroid is:",["A meteor on the ground","*A small rocky or metallic body in space (before entering atmosphere)","A comet","An asteroid"],"Space debris."),
     ("A meteor is:",["An object in space","A rock on the ground","*The streak of light when a meteoroid enters and burns up in Earth's atmosphere","A comet"],"'Shooting star.'"),
     ("A meteorite is:",["An object in space","A streak of light","*A meteoroid remnant that survives passage through the atmosphere and reaches the ground","A comet tail"],"Reached the surface."),
     ("Meteor showers occur when:",["Random meteoroids hit Earth","*Earth passes through the debris trail left by a comet","Comets hit Earth","The Moon is full"],"Predictable annual events."),
     ("The Perseid meteor shower (August) is associated with:",["Halley's Comet","*Comet Swift-Tuttle","The asteroid belt","Jupiter"],"Annual shower from Swift-Tuttle's debris."),
     ("Halley's Comet has an orbital period of approximately:",["10 years","*~76 years","1,000 years","1 year"],"Short-period comet, last seen 1986."),
     ("Short-period comets originate from:",["The Oort Cloud","*The Kuiper Belt (orbital periods < 200 years)","The asteroid belt","The Sun"],"Kuiper Belt objects."),
     ("Long-period comets originate from:",["The Kuiper Belt","*The Oort Cloud (orbital periods > 200 years)","Mars","The Sun"],"Perturbed inward by passing stars."),
     ("When a comet approaches the Sun, ices:",["Melt into water","*Sublimate (change directly from solid to gas), creating the coma and tails","Freeze further","Evaporate slowly"],"Sublimation, not melting (very low pressure)."),
     ("The Rosetta mission (ESA) accomplished:",["Only observing a comet","*Orbiting Comet 67P/Churyumov–Gerasimenko and landing the Philae probe on it","Landing on Mars","Visiting the Oort Cloud"],"First comet landing (2014)."),
     ("Comets may have delivered _____ to early Earth.",["Nothing","*Water and organic molecules — contributing to oceans and building blocks of life","Only rocks","Only metals"],"Cometary delivery hypothesis."),
     ("A bolide is:",["A small meteor","*An exceptionally bright meteor or fireball, often exploding in the atmosphere","A comet","A satellite"],"Very bright meteors."),
     ("The Chelyabinsk event (2013) involved:",["A comet impact","Nothing","*A ~20 m meteoroid that exploded over Russia, injuring ~1,500 people from the shockwave","A planned explosion"],"Recent dramatic event."),
     ("Studying comets and meteoroids provides information about:",["Nothing useful","*The early solar system's composition, the origin of water and organics, and impact hazards","Only pretty lights","Only naming conventions"],"Primitive material.")]
)
lessons[k]=v

# 3.6
k,v = build_lesson(3,6,"Planetary Atmospheres",
    "<h3>Planetary Atmospheres</h3>"
    "<h4>Key Factors</h4>"
    "<ul><li><b>Gravity:</b> Determines escape velocity; larger planets retain lighter gases (H, He).</li>"
    "<li><b>Distance from Sun:</b> Affects temperature → molecular speeds → ability to retain gases.</li>"
    "<li><b>Composition:</b> Earth: N₂ 78%, O₂ 21%. Venus: CO₂ 96.5%. Mars: CO₂ 95% but very thin. Jupiter: H₂/He.</li></ul>"
    "<h4>Atmospheric Effects</h4>"
    "<p>Greenhouse effect, weather systems, protection from radiation, spectroscopic detection of exoplanet atmospheres (transit spectroscopy).</p>",
    [("Escape Velocity","Minimum speed for gas molecules to escape a planet's gravity; determines atmospheric retention."),
     ("Greenhouse Effect","Atmospheric gases (CO₂, H₂O, CH₄) trap infrared radiation → surface warming."),
     ("Transit Spectroscopy","Technique for analyzing exoplanet atmospheres by observing starlight filtered through them during transit."),
     ("Scale Height","Height over which atmospheric pressure drops by a factor of e (~2.72); indicates atmosphere thickness."),
     ("Atmospheric Composition","Mix of gases in a planet's atmosphere; determined by mass, temperature, volcanism, and biology.")],
    [("Earth's atmosphere is primarily composed of:",["Oxygen and CO₂","*Nitrogen (~78%) and oxygen (~21%)","Hydrogen and helium","Carbon dioxide and nitrogen"],"N₂ dominant."),
     ("Venus's atmosphere is dominated by:",["Nitrogen","Oxygen","*Carbon dioxide (~96.5%)","Methane"],"Dense CO₂ → runaway greenhouse."),
     ("Mars's atmosphere is mostly _____ but very thin.",["Oxygen","Nitrogen","*Carbon dioxide (~95%)","Hydrogen"],"~1% of Earth's surface pressure."),
     ("Jupiter retains hydrogen and helium because:",["It's close to the Sun","*Its enormous mass → high escape velocity prevents light gases from escaping","It has no atmosphere","Magnetic fields hold them"],"Massive = strong gravity."),
     ("A planet's ability to retain an atmosphere depends primarily on:",["Color","*Mass (gravity/escape velocity) and temperature (molecular speed)","Rotation speed alone","Distance from other planets"],"Balance of gravity vs thermal escape."),
     ("The greenhouse effect is:",["Always harmful","*A natural process where atmospheric gases trap infrared radiation, warming the surface","Only on Earth","Caused by volcanoes alone"],"Natural and essential (but can become extreme)."),
     ("Venus's surface temperature (~465°C) exceeds Mercury's despite being farther from the Sun because:",["Venus is larger","*Venus's thick CO₂ atmosphere creates an extreme greenhouse effect","Venus rotates slowly","Mercury has no surface"],"Atmosphere matters more than distance."),
     ("Saturn's moon Titan has an atmosphere primarily of:",["Oxygen","CO₂","*Nitrogen (with methane and ethane)","Hydrogen"],"Dense nitrogen atmosphere."),
     ("Mars lost most of its atmosphere likely because:",["It chose to","*Its low gravity and loss of magnetic field allowed solar wind to strip away gases","The Sun absorbed it","It was never thick"],"Multiple factors."),
     ("Transit spectroscopy works by:",["Looking at a planet directly","*Analyzing starlight that passes through a planet's atmosphere during transit, revealing atmospheric composition","Sending probes","Listening for radio signals"],"Light absorbed at characteristic wavelengths."),
     ("Atmospheric pressure on Venus's surface is about:",["1 atm","*~90 atm (equivalent to ~900 m underwater on Earth)","0.01 atm","1,000 atm"],"Crushing pressure."),
     ("Ozone (O₃) in Earth's stratosphere protects life by:",["Producing heat","*Absorbing harmful ultraviolet radiation from the Sun","Creating weather","Nothing"],"UV shield."),
     ("Earth's oxygen-rich atmosphere is largely due to:",["Volcanic outgassing","Chemical reactions alone","*Photosynthesis by cyanobacteria and plants over billions of years","Solar wind"],"Biological origin."),
     ("Atmospheric escape mechanisms include:",["Only gravity","*Thermal escape (Jeans escape), solar wind stripping, impact erosion, and photodissociation","Only UV light","Only impacts"],"Multiple processes."),
     ("A planet with no atmosphere would experience:",["Mild weather","*Extreme temperature swings between day and night (like Mercury)","Constant temperature","Rain"],"No thermal regulation."),
     ("The discovery of phosphine in Venus's atmosphere (debated) would be significant because:",["It's a common gas","*Phosphine could indicate biological processes (as known on Earth)","It proves there's water","Nothing"],"Potential biosignature (still debated)."),
     ("Wind speeds on Neptune reach ~2,100 km/h, driven partly by:",["Solar heating (small)","*Internal heat from the planet (Neptune radiates ~2.6× more than it receives from the Sun)","Only the Sun","Magnetism"],"Internal energy drives weather."),
     ("Spectroscopy identifies atmospheric gases by their:",["Color alone","*Unique absorption or emission lines at specific wavelengths","Temperature","Pressure"],"Each gas has a spectral signature."),
     ("Studying planetary atmospheres helps us understand:",["Nothing","*Climate science, habitability, exoplanet characterization, and Earth's own atmosphere","Only Jupiter","Only weather"],"Comparative atmospherics."),
     ("The James Webb Space Telescope advances atmospheric study by:",["Only taking photos","*Providing unprecedented infrared spectroscopy of exoplanet atmospheres","Only studying stars","Only visible light"],"JWST = game-changer for exoplanet atmospheres.")]
)
lessons[k]=v

# 3.7
k,v = build_lesson(3,7,"Case Studies in Space Exploration",
    "<h3>Case Studies in Space Exploration</h3>"
    "<h4>Voyager Program (1977–present)</h4>"
    "<p>Voyager 1 & 2 explored Jupiter, Saturn (both), plus Uranus and Neptune (Voyager 2 only). Both are now in interstellar space. Carried the Golden Record.</p>"
    "<h4>Cassini-Huygens (1997–2017)</h4>"
    "<p>Orbited Saturn for 13 years. Huygens probe landed on Titan (2005). Discovered Enceladus's water plumes.</p>"
    "<h4>Mars Rovers</h4>"
    "<p>Spirit, Opportunity, Curiosity, Perseverance — progressively more capable. Perseverance is collecting samples for Mars Sample Return; Ingenuity achieved first powered flight on another planet.</p>",
    [("Voyager Golden Record","Gold-plated phonograph records aboard Voyager 1 & 2 carrying sounds and images of Earth for potential alien finders."),
     ("Cassini-Huygens","Joint NASA/ESA mission; orbited Saturn 2004–2017; Huygens landed on Titan."),
     ("Perseverance Rover","NASA Mars rover (2021–present); collecting samples, studying geology, and searching for biosignatures."),
     ("Ingenuity Helicopter","First aircraft to achieve powered flight on another planet (Mars, 2021); originally a tech demo."),
     ("New Horizons","NASA probe that flew by Pluto (2015) and Kuiper Belt object Arrokoth (2019).")],
    [("Voyager 2 is the only spacecraft to have visited all four giant planets:",["True","*True — Jupiter, Saturn, Uranus, and Neptune","False","Only three"],"Unique grand tour."),
     ("Voyager 1 entered interstellar space in approximately:",["2000","*2012","2020","1990"],"First human-made object in interstellar space."),
     ("The Cassini mission discovered water plumes erupting from:",["Titan","Europa","*Enceladus","Ganymede"],"Through ice cracks, indicating a subsurface ocean."),
     ("The Huygens probe landed on Titan and revealed:",["Oceans of water","*A surface with methane lakes, rivers, and hydrocarbon dunes","A lifeless rock","Only ice"],"Remarkably Earth-like landscape (with different chemistry)."),
     ("The Mars rover Opportunity was designed for a 90-day mission but lasted:",["100 days","1 year","*Over 14 years (2004–2018)","90 days exactly"],"Far exceeded expectations."),
     ("Perseverance rover's primary mission includes:",["Only taking photos","*Collecting rock samples for future return to Earth and searching for signs of ancient life","Only driving","Only weather monitoring"],"Mars Sample Return campaign."),
     ("Ingenuity helicopter demonstrated:",["Only hovering","*Powered flight is possible in Mars's thin atmosphere","Mars has thick air","It couldn't fly"],"Historic first flight on another world."),
     ("New Horizons revealed that Pluto:",["Is a dead world","*Has a complex geology with mountains, glaciers, and a nitrogen atmosphere","Is a gas giant","Has oceans"],"Surprisingly active."),
     ("The Juno mission is studying:",["Mars","Saturn","*Jupiter's atmosphere, magnetic field, and interior structure","The Sun"],"Still operating in Jupiter orbit."),
     ("The Mars InSight lander studied:",["Surface geology","*Mars's interior using a seismometer (detected marsquakes)","The atmosphere only","Mars's moons"],"Interior Exploration using Seismic Investigations."),
     ("The Golden Record contains:",["Only music","*Greetings in 55 languages, sounds of Earth, music, and images encoded in analog form","Only images","Only math"],"Message to the cosmos."),
     ("Curiosity rover discovered that Mars's Gale Crater:",["Was always dry","*Once had a habitable freshwater lake environment","Has current life","Is made of ice"],"Evidence of past habitability."),
     ("The Pioneer 10 and 11 spacecraft carry:",["Golden Records","*Gold-anodized aluminum plaques with human figures and solar system diagram","Nothing","Radio transmitters only"],"Simpler message than Voyager's Golden Record."),
     ("The MESSENGER mission orbited:",["Mars","*Mercury (first spacecraft to orbit Mercury, 2011–2015)","Venus","Jupiter"],"Studied Mercury's surface, composition, and magnetic field."),
     ("Magellan spacecraft mapped _____ using radar.",["Mars","*Venus's surface (through its thick cloud cover)","The Moon","Jupiter"],"Radar pierced the clouds."),
     ("The Dawn spacecraft visited:",["Only asteroids","*Both Vesta and Ceres (first to orbit two different extraterrestrial bodies)","Jupiter's moons","Saturn's moons"],"Asteroid belt exploration."),
     ("Future Europa Clipper mission will:",["Land on Europa","*Perform multiple flybys of Jupiter's moon Europa to study its subsurface ocean","Visit Saturn","Study the Sun"],"Planned detailed investigation."),
     ("Space exploration missions have:",["Wasted resources","*Revolutionized our understanding of the solar system, developed technology, and inspired generations","Only cost money","Had no impact"],"Enormous scientific and cultural impact."),
     ("International collaboration in space exploration includes:",["Only NASA","*NASA, ESA, JAXA, Roscosmos, ISRO, CNSA, and others working together","Only Europe and US","No collaboration"],"Global effort."),
     ("Studying case histories of missions helps students:",["Not at all","*Understand the scientific method in action, engineering challenges, and the excitement of discovery","Only memorize dates","Only learn acronyms"],"Real-world science.")]
)
lessons[k]=v

# 3.8
k,v = build_lesson(3,8,"AP Prep: Kepler's Laws",
    "<h3>AP Prep: Kepler's Laws</h3>"
    "<h4>Kepler's Three Laws of Planetary Motion</h4>"
    "<ul><li><b>1st Law (Ellipses):</b> Planets orbit the Sun in ellipses with the Sun at one focus.</li>"
    "<li><b>2nd Law (Equal Areas):</b> A line from Sun to planet sweeps equal areas in equal times → planets move faster at perihelion.</li>"
    "<li><b>3rd Law (Harmonics):</b> T² = a³ (years, AU). Newton's form: T² = (4π²/GM)a³.</li></ul>"
    "<h4>Problem-Solving</h4>"
    "<p>Use Kepler's 3rd to find period from semi-major axis and vice versa. Derive central mass from orbital data.</p>",
    [("Kepler's 1st Law","Planets orbit in ellipses with the Sun at one focus."),
     ("Kepler's 2nd Law","A planet sweeps equal areas in equal time; moves faster at perihelion, slower at aphelion."),
     ("Kepler's 3rd Law","T² = a³ (simplified); period squared is proportional to semi-major axis cubed."),
     ("Semi-Major Axis","Half the longest diameter of an ellipse; average distance from the Sun; denoted 'a'."),
     ("Eccentricity","Measure of how elongated an ellipse is; 0 = circle, close to 1 = very elongated.")],
    [("Kepler's first law states that planetary orbits are:",["Circular","Parabolic","*Elliptical with the Sun at one focus","Hyperbolic"],"Ellipses, not circles."),
     ("Kepler's second law (equal areas) implies that a planet moves:",["At constant speed","Faster at aphelion","*Faster at perihelion (closest to Sun) and slower at aphelion","Only in straight lines"],"Conservation of angular momentum."),
     ("Using Kepler's 3rd law (T² = a³), a planet at 9 AU has a period of:",["9 years","81 years","*27 years (T² = 729, T = 27)","3 years"],"T² = 9³ = 729; T = √729 = 27."),
     ("If T = 8 years, what is the semi-major axis?",["8 AU","2 AU","*4 AU (a³ = T² = 64; a = 4)","64 AU"],"a³ = 64; a = ∛64 = 4."),
     ("The eccentricity of a perfect circle is:",["1","0.5","*0","Infinity"],"No elongation."),
     ("Earth's orbital eccentricity (~0.017) means its orbit is:",["Highly elliptical","*Nearly circular","A parabola","A hyperbola"],"Almost circular."),
     ("A comet with a very elongated orbit has an eccentricity close to:",["0","*1 (but less than 1 for a bound orbit)","0.5","−1"],"Highly eccentric."),
     ("Newton's generalized form of Kepler's 3rd law adds:",["Nothing","*The masses of the orbiting bodies: T² = 4π²a³/(G(M+m))","Only velocity","Only direction"],"Allows calculation of masses."),
     ("Using the generalized 3rd law, you can determine the mass of a central body if you know:",["Only its color","*The orbital period and semi-major axis of an orbiting object","Only its distance","Nothing"],"M = 4π²a³/(GT²)."),
     ("This is how astronomers determine the mass of:",["Nothing","*Stars, planets, and even black holes (by observing orbiting companions)","Only the Sun","Only Earth"],"Powerful technique."),
     ("At perihelion, orbital speed is highest because:",["Gravity is weaker","*The planet is closest to the Sun and gravitational PE converts to kinetic energy","The planet is farthest","Kepler's 1st law"],"Energy conservation + Kepler's 2nd law."),
     ("Kepler discovered his laws by analyzing:",["Galileo's data","*Tycho Brahe's precise observations of planetary positions (especially Mars)","His own telescope data","Newton's equations"],"Brahe's data was key."),
     ("Newton showed Kepler's laws follow from:",["Magnetism","*His law of universal gravitation and laws of motion","Electricity","Random chance"],"Gravity explains Kepler's empirical laws."),
     ("For the AP exam, students should be able to:",["Only state the laws","*Derive, apply, and solve problems using Kepler's laws and Newton's gravity","Only memorize names","Only draw orbits"],"Quantitative application required."),
     ("The focus of an ellipse where the Sun is located is:",["At the center","At the edge","*At one of the two foci (not the center unless eccentricity is 0)","Outside the ellipse"],"Off-center."),
     ("If you triple the semi-major axis of an orbit, the period changes by a factor of:",["3","9","*3√3 ≈ 5.2 (T² = 27; T = 3^(3/2))","27"],"T = a^(3/2); 3^(3/2) = 3√3 ≈ 5.196."),
     ("An object in a bound orbit has total energy that is:",["Positive","Zero","*Negative (gravitational PE magnitude > kinetic energy)","Infinite"],"Bound = negative total energy."),
     ("Kepler's laws apply to:",["Only planets","*Any orbiting body — moons, asteroids, comets, satellites, binary stars, exoplanets","Only the Sun","Only Earth"],"Universal applicability."),
     ("Calculating the orbital period of a satellite in low Earth orbit (~400 km altitude):",["Requires only height","*Use T = 2π√(r³/(GM_Earth)) with r = R_Earth + altitude ≈ 6,771 km → ~92 minutes","Cannot be done","Requires the satellite's mass"],"ISS orbital period ~92 min."),
     ("Mastering Kepler's laws and orbital calculations is essential for:",["Nothing","*Understanding planetary motion, space mission design, and fundamental astrophysics","Only history","Only Kepler fans"],"Core AP astronomy/physics content.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 3: wrote {len(lessons)} lessons")
