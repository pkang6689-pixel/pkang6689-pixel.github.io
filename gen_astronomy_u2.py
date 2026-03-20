#!/usr/bin/env python3
"""Astronomy Unit 2 – Earth, Moon & Sun (7 lessons)."""
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

# 2.1
k,v = build_lesson(2,1,"Earth's Rotation & Revolution",
    "<h3>Earth's Rotation &amp; Revolution</h3>"
    "<p><b>Rotation:</b> Earth spins on its axis once every ~23 h 56 min (sidereal day). Causes day/night cycle. Tilted 23.5° from the orbital plane.</p>"
    "<p><b>Revolution:</b> Earth orbits the Sun in ~365.25 days. Orbit is slightly elliptical (eccentricity ~0.017). Closest approach = perihelion (~Jan 3); farthest = aphelion (~Jul 4).</p>"
    "<p><b>Coriolis Effect:</b> Earth's rotation deflects moving objects (right in NH, left in SH); affects winds and ocean currents.</p>",
    [("Sidereal Day","Time for one full 360° rotation relative to stars; ~23 h 56 min."),
     ("Solar Day","Time from noon to noon (~24 h); slightly longer than sidereal due to Earth's orbital advance."),
     ("Perihelion","Closest point of Earth's orbit to the Sun (~Jan 3, ~147 million km)."),
     ("Aphelion","Farthest point of Earth's orbit from the Sun (~Jul 4, ~152 million km)."),
     ("Coriolis Effect","Deflection of moving objects due to Earth's rotation; right in NH, left in SH.")],
    [("Earth completes one rotation in approximately:",["24 hours exactly","*23 hours 56 minutes (sidereal day)","12 hours","48 hours"],"Sidereal vs solar day."),
     ("A solar day is about 4 minutes longer than a sidereal day because:",["Earth slows down","*Earth advances in its orbit, so it must rotate slightly more to face the Sun again","The Moon pulls on Earth","The Sun moves"],"Orbital geometry."),
     ("Earth's axial tilt is approximately:",["0°","10°","*23.5°","45°"],"Causes the seasons."),
     ("Perihelion occurs around:",["July","*January 3","March","September"],"Closest to the Sun in Northern Hemisphere winter."),
     ("Seasons are caused by:",["Earth's distance from the Sun","*Earth's axial tilt (23.5°) causing varying angles of sunlight","The Moon's phases","Sunspot activity"],"Tilt, not distance!"),
     ("At perihelion, Earth is about _____ from the Sun.",["152 million km","*147 million km","100 million km","200 million km"],"Closest approach."),
     ("The Coriolis effect causes moving objects in the Northern Hemisphere to deflect:",["Left","Upward","*Right","Downward"],"Right in NH, left in SH."),
     ("Earth's orbital eccentricity (~0.017) means its orbit is:",["Perfectly circular","*Nearly circular (slightly elliptical)","Highly elongated","Parabolic"],"Close to circular."),
     ("Earth's revolution period is:",["30 days","*~365.25 days","24 hours","1,000 days"],"One year."),
     ("The equatorial bulge of Earth is caused by:",["Gravity alone","*Earth's rotation (centrifugal effect makes equator slightly wider)","Tides","Solar wind"],"~43 km wider at equator."),
     ("Foucault's pendulum demonstrates:",["Earth's revolution","*Earth's rotation (plane of swing appears to rotate)","Gravity","Magnetism"],"Classic rotation proof."),
     ("If Earth had no axial tilt, there would be:",["Extreme seasons","*No seasons (uniform Sun angle at each latitude year-round)","Only winter","Constant summer"],"Tilt = seasons."),
     ("The ecliptic is:",["Earth's equator","*The apparent path of the Sun across the sky (plane of Earth's orbit)","The Moon's orbit","The Milky Way"],"Earth orbits in the ecliptic plane."),
     ("Time zones exist because:",["The Sun is far away","*Earth rotates 360° in 24 hours (15° per hour); different longitudes see the Sun at different times","Gravity changes","Countries decided randomly"],"15° per hour."),
     ("Leap years add an extra day because:",["The Moon requires it","*Earth's orbital period is ~365.25 days; the extra 0.25 day accumulates","Earth speeds up","The calendar is wrong"],"Every 4 years (with exceptions)."),
     ("The celestial equator is:",["The ecliptic","*The projection of Earth's equator onto the celestial sphere","The horizon","The Milky Way"],"Earth's equator extended to the sky."),
     ("Precession of Earth's axis:",["Doesn't exist","*Is a slow wobble (~26,000 year cycle) caused by gravitational torques from the Sun and Moon","Completes in 1 year","Only changes tilt angle"],"Like a spinning top's wobble."),
     ("Currently, the North Celestial Pole points near:",["Vega","*Polaris (the North Star)","Sirius","Alpha Centauri"],"Due to precession, this changes over millennia."),
     ("Understanding Earth's rotation and revolution is foundational for:",["Nothing","*Explaining day/night, seasons, time zones, calendars, and celestial navigation","Only navigation","Only physics"],"Core astronomical concepts."),
     ("The analemma (figure-8 pattern of the Sun's position at the same time each day) results from:",["Random motion","*The combination of Earth's axial tilt and orbital eccentricity","Atmospheric refraction","The Moon's influence"],"Tilt + elliptical orbit.")]
)
lessons[k]=v

# 2.2
k,v = build_lesson(2,2,"Seasons & Tilt of Axis",
    "<h3>Seasons &amp; Tilt of Axis</h3>"
    "<h4>Mechanism</h4>"
    "<p>Earth's 23.5° axial tilt → as Earth orbits, different hemispheres receive more/less direct sunlight. Summer solstice (June ~21): NH tilted toward Sun; winter solstice (Dec ~21): NH tilted away.</p>"
    "<h4>Key Points</h4>"
    "<ul><li>Equinoxes (March ~20, Sept ~22): Sun over equator; ~12 h day everywhere.</li>"
    "<li>Longer days + more direct sunlight → warmer temperatures.</li>"
    "<li>Seasons are reversed in the Southern Hemisphere.</li></ul>",
    [("Summer Solstice","~June 21 in NH; longest day; Sun highest in sky; most direct sunlight."),
     ("Winter Solstice","~Dec 21 in NH; shortest day; Sun lowest in sky; least direct sunlight."),
     ("Equinox","~March 20 and Sept 22; Sun directly over equator; ~equal day and night globally."),
     ("Angle of Insolation","Angle at which sunlight strikes Earth's surface; more direct = more energy per unit area."),
     ("Arctic/Antarctic Circles","Latitudes 66.5° N/S; mark boundaries of 24-h daylight/darkness at solstices.")],
    [("Seasons are primarily caused by:",["Earth's distance from the Sun","*Earth's 23.5° axial tilt","Solar flares","The Moon's gravity"],"Tilt changes sunlight angle and day length."),
     ("At the June solstice, the Northern Hemisphere has:",["Shortest day","*Longest day and most direct sunlight","Equal day and night","Total darkness"],"NH summer begins."),
     ("At the December solstice, the Southern Hemisphere has:",["Winter","*Summer (it's tilted toward the Sun)","Equal day and night","No sunlight"],"Seasons reversed."),
     ("During an equinox:",["One hemisphere has 24-hour daylight","*Day and night are approximately equal (~12 h each) everywhere","The Sun doesn't rise","It only occurs once a year"],"Equi- (equal) nox (night)."),
     ("More direct sunlight means:",["Less energy per area","*More solar energy per unit area (higher insolation angle)","No temperature change","Only UV increases"],"Direct rays heat more effectively."),
     ("The Arctic Circle experiences 24 hours of daylight (",["During equinoxes","*At the summer solstice (midnight Sun)","At the winter solstice","Never"],"Sun never sets on summer solstice at 66.5°N."),
     ("The tropics (23.5° N and S) are where:",["It's always cold","*The Sun can be directly overhead (zenith) at least once per year","Seasons don't exist","Only rain occurs"],"Tropic of Cancer (N) and Capricorn (S)."),
     ("At the equator, seasons are:",["Extreme","*Minimal — relatively consistent temperatures year-round","Reversed","Nonexistent completely"],"Near-equal sunlight year-round."),
     ("Earth is actually closest to the Sun during:",["Northern summer","*Northern winter (~January; perihelion has minimal effect on seasons)","Both equinoxes","There's no variation"],"Distance isn't the cause of seasons."),
     ("The Sun's declination changes throughout the year between:",["0° and 90°","*+23.5° (June) and −23.5° (December)","0° and 45°","None; it's constant"],"Matches axial tilt."),
     ("Day length at the North Pole on the summer solstice is:",["12 hours","*24 hours (continuous daylight)","0 hours","6 hours"],"Midnight Sun."),
     ("Day length at the North Pole on the winter solstice is:",["24 hours","*0 hours (polar night — continuous darkness)","12 hours","6 hours"],"No sunlight for months."),
     ("Seasonal lag (warmest days occurring after the solstice) is due to:",["Delayed tilt","*Thermal inertia (land and oceans take time to heat up and cool down)","Sun's distance","Calendar error"],"July is warmest in NH despite June solstice."),
     ("If Earth's axial tilt increased to 45°, seasons would be:",["The same","*Much more extreme (hotter summers, colder winters)","Eliminated","Reversed"],"Greater tilt = more extreme seasonal contrast."),
     ("If Earth had zero axial tilt:",["Seasons would be extreme","*There would be no seasons","Only the equator would have seasons","Winter would last all year"],"No tilt = no seasons."),
     ("The analemma is 'taller' (north-south) primarily because of:",["Orbital eccentricity","*Earth's axial tilt (Sun's declination changes ±23.5°)","Precession","The Moon"],"Tilt stretches the analemma vertically."),
     ("In the Southern Hemisphere, Christmas occurs during:",["Winter","*Summer","Spring","Autumn"],"December = SH summer."),
     ("The Tropic of Cancer is at:",["0° latitude","*23.5° N latitude","23.5° S latitude","66.5° N latitude"],"Sun is directly overhead at June solstice."),
     ("Seasons affect:",["Only temperature","*Temperature, day length, plant growth, animal behavior, weather patterns, and human culture","Only daylight hours","Nothing significant"],"Wide-ranging impacts."),
     ("Understanding seasons requires knowledge of:",["Only calendars","*Earth's axial tilt, orbital motion, and the geometry of sunlight","Only geography","Only weather"],"Geometric reasoning.")]
)
lessons[k]=v

# 2.3
k,v = build_lesson(2,3,"Lunar Phases",
    "<h3>Lunar Phases</h3>"
    "<p>The Moon orbits Earth every ~29.5 days (synodic period). Phases result from the changing angle between the Sun, Earth, and Moon.</p>"
    "<h4>Phase Sequence</h4>"
    "<ul><li><b>New Moon:</b> Moon between Sun and Earth; dark side faces us.</li>"
    "<li><b>Waxing crescent → First quarter → Waxing gibbous → Full Moon:</b> Illuminated portion grows.</li>"
    "<li><b>Waning gibbous → Third quarter → Waning crescent → New Moon:</b> Illuminated portion shrinks.</li></ul>"
    "<p><b>Tidal locking:</b> Moon's rotation period = orbital period (~27.3 days sidereal); same face always toward Earth.</p>",
    [("Synodic Period","Time between identical phases of the Moon as seen from Earth; ~29.5 days."),
     ("New Moon","Moon between Sun and Earth; illuminated side faces away; Moon not visible."),
     ("Full Moon","Earth between Sun and Moon; fully illuminated face visible from Earth."),
     ("Waxing","Increasing illumination (new → full); visible portion growing night by night."),
     ("Tidal Locking","Moon's rotation period equals its orbital period; same hemisphere always faces Earth.")],
    [("The Moon's synodic period (phase cycle) is approximately:",["27 days","*29.5 days","30.5 days","15 days"],"New Moon to New Moon."),
     ("During a new Moon, the Moon is:",["Opposite the Sun","*Between the Sun and Earth (dark side toward us)","Behind Earth","Above the Sun"],"Not visible."),
     ("During a full Moon, the Moon is:",["Between Sun and Earth","*Opposite the Sun (Earth between Sun and Moon)","Next to the Sun","Behind the Sun"],"Fully illuminated."),
     ("'Waxing' means the Moon's illuminated portion is:",["Decreasing","*Increasing","Constant","Invisible"],"Growing toward full."),
     ("'Waning' means the Moon's illuminated portion is:",["Increasing","*Decreasing","Full","New"],"Shrinking toward new."),
     ("The first quarter Moon shows:",["Full illumination","*The right half illuminated (in the Northern Hemisphere)","Only a crescent","The entire Moon"],"Half-lit at first quarter."),
     ("The third (last) quarter Moon shows:",["Right half","*Left half illuminated (in the NH)","Full disc","No illumination"],"Opposite half from first quarter."),
     ("Tidal locking causes the Moon to:",["Spin rapidly","*Always show the same face toward Earth","Not rotate at all","Change shape"],"Rotation period = orbital period."),
     ("The Moon's sidereal orbital period is approximately:",["29.5 days","*27.3 days","24 hours","365 days"],"With respect to the stars."),
     ("The difference between sidereal and synodic periods is due to:",["The Moon's mass","*Earth's simultaneous orbital motion around the Sun","The Moon's rotation","Gravity changes"],"Moon must travel extra to reach the same Sun-Earth-Moon alignment."),
     ("A waxing crescent Moon is visible:",["All night","At midnight","*In the western sky after sunset","Before sunrise only"],"Sets shortly after the Sun."),
     ("A waning crescent Moon is visible:",["After sunset","All night","*Before sunrise in the eastern sky","At midnight"],"Rises just before the Sun."),
     ("The Moon produces light by:",["Nuclear fusion","*Reflecting sunlight (the Moon has no light of its own)","Chemical reactions","Radioactive decay"],"Moon = reflector."),
     ("Earthshine on a crescent Moon is caused by:",["Starlight","*Sunlight reflected from Earth illuminating the Moon's dark portion","Moonlight","Nothing"],"Earth reflects light back to the Moon."),
     ("The Moon rises about _____ later each day.",["1 hour","*~50 minutes","10 minutes","2 hours"],"Orbital advance of ~12° per day."),
     ("A full Moon rises at approximately:",["Noon","Midnight","*Sunset (and sets at sunrise)","3 AM"],"Opposite the Sun."),
     ("A new Moon rises at approximately:",["Sunset","Midnight","*Sunrise (and sets at sunset)","3 PM"],"Same direction as the Sun."),
     ("Blue Moon refers to:",["A blue-colored Moon","*The second full Moon in a calendar month (colloquial usage)","A lunar eclipse","A first quarter"],"Fairly rare occurrence."),
     ("The lunar cycle has influenced:",["Nothing","*Calendars, agriculture, religious observances, and tidal patterns across many cultures","Only tides","Only calendars"],"Cultural significance."),
     ("Understanding lunar phases is essential for:",["Nothing","*Predicting tides, planning observations, understanding eclipses, and cultural contexts","Only astrology","Only navigation"],"Foundational astronomy.")]
)
lessons[k]=v

# 2.4
k,v = build_lesson(2,4,"Solar & Lunar Eclipses",
    "<h3>Solar &amp; Lunar Eclipses</h3>"
    "<h4>Solar Eclipse</h4>"
    "<p>Moon passes between Earth and Sun, casting a shadow on Earth. Total solar eclipse: umbra (~100 km wide path); partial: penumbra. Moon's apparent size ≈ Sun's apparent size (cosmic coincidence).</p>"
    "<h4>Lunar Eclipse</h4>"
    "<p>Earth between Sun and Moon; Earth's shadow falls on the Moon. Total lunar eclipse: Moon turns reddish ('blood Moon') — refracted red light through Earth's atmosphere.</p>"
    "<h4>Why Not Every Month?</h4>"
    "<p>Moon's orbit is tilted ~5° from the ecliptic; eclipses occur only at nodes (where orbits cross). Eclipse seasons ~2× per year.</p>",
    [("Solar Eclipse","Moon's shadow falls on Earth; Sun is blocked. Total (umbra) or partial (penumbra)."),
     ("Lunar Eclipse","Earth's shadow falls on the Moon; Moon darkens or turns red."),
     ("Umbra","Darkest central part of a shadow; total eclipse visible within the umbra."),
     ("Penumbra","Lighter outer part of a shadow; partial eclipse visible within the penumbra."),
     ("Eclipse Node","Point where the Moon's orbit crosses the ecliptic plane; eclipses occur near nodes.")],
    [("A solar eclipse occurs when the:",["Earth blocks the Sun","*Moon passes between the Earth and Sun","Moon enters Earth's shadow","Sun blocks the Moon"],"Moon's shadow on Earth."),
     ("A lunar eclipse occurs when:",["The Moon blocks the Sun","*Earth is between the Sun and Moon, casting its shadow on the Moon","The Sun blocks the Moon","Two moons align"],"Earth's shadow on Moon."),
     ("A total solar eclipse is visible from:",["The entire Earth","Half the Earth","*A narrow path (umbra) on Earth's surface (~100 km wide)","Only at the poles"],"Very limited path of totality."),
     ("During a total lunar eclipse, the Moon appears:",["White","Black","*Reddish ('blood Moon')","Blue"],"Refracted red light from Earth's atmosphere."),
     ("Eclipses don't occur every month because:",["The Moon is too small","*The Moon's orbit is tilted ~5° from the ecliptic — alignment only at nodes","The Sun moves","Earth's orbit changes"],"5° tilt prevents monthly eclipses."),
     ("The umbra is:",["Bright","*The darkest part of the shadow (total eclipse zone)","The outer shadow","Invisible"],"Total eclipse within umbra."),
     ("The penumbra is:",["The darkest part","*The lighter outer part of the shadow (partial eclipse zone)","Only visible during lunar eclipses","Not a real shadow"],"Partial eclipse within penumbra."),
     ("An annular solar eclipse occurs when:",["The Moon is closest to Earth","*The Moon is too far from Earth (near apogee) to fully cover the Sun — a ring of sunlight remains","Earth is between Sun and Moon","The Sun is larger than normal"],"Ring of fire."),
     ("Eclipse seasons occur roughly:",["Monthly","*Twice per year (when the Sun is near the lunar nodes)","Once per decade","Randomly"],"Sun near node → eclipse possible."),
     ("The saros cycle predicts eclipses repeating every:",["1 year","*~18 years, 11 days, 8 hours","100 years","29.5 days"],"Babylonians discovered this cycle."),
     ("During a total solar eclipse, the _____ of the Sun becomes visible.",["Core","Photosphere","*Corona (outer atmosphere)","Chromosphere only"],"Only visible when the bright disk is blocked."),
     ("It is dangerous to look at a solar eclipse without protection because:",["The Moon is bright","*The Sun's UV and IR radiation can permanently damage the retina (solar retinopathy)","The corona is toxic","Nothing happens"],"Never view the Sun without proper filters."),
     ("Safe solar eclipse viewing methods include:",["Regular sunglasses","Binoculars","*ISO-certified eclipse glasses or pinhole projection","Squinting"],"Special solar filters only."),
     ("A partial solar eclipse means:",["The Moon passes through Earth's shadow","*The Moon only partially covers the Sun's disk (viewer in penumbra)","The Sun is half-visible normally","The Moon is between phases"],"Partial coverage."),
     ("The coincidence that allows total solar eclipses is:",["The Moon's orbit is circular","*The Moon's apparent size is nearly identical to the Sun's apparent size from Earth","The Moon is the same size as the Sun","Earth has an atmosphere"],"Moon ~400× smaller but ~400× closer."),
     ("A lunar eclipse can be seen by:",["Only a small area","*Everyone on the night side of Earth (where the Moon is visible)","Only at the equator","Only one continent"],"Much wider visibility than solar eclipses."),
     ("During totality in a solar eclipse, stars and planets become visible because:",["It's nighttime","*The sky darkens dramatically as the Moon blocks the Sun","Clouds form","The atmosphere changes"],"Brief daytime darkness."),
     ("Eclipse prediction requires understanding:",["Only the Moon's phase","*The Moon's orbital inclination, nodes, and relative positions of Sun-Earth-Moon","Only the Sun's position","Only calendars"],"Geometric alignment calculations."),
     ("Historical eclipses have been important for:",["Nothing","*Dating ancient events, confirming general relativity (1919), and studying the solar corona","Only religion","Only art"],"Scientific and historical significance."),
     ("The study of eclipses connects:",["Nothing","*Orbital mechanics, geometry, history, culture, and solar physics","Only superstition","Only mythology"],"Rich interdisciplinary topic.")]
)
lessons[k]=v

# 2.5
k,v = build_lesson(2,5,"Tides & Gravitational Effects",
    "<h3>Tides &amp; Gravitational Effects</h3>"
    "<h4>Tidal Force</h4>"
    "<p>Caused by the difference in gravitational pull across Earth's diameter. The Moon is the primary cause (~2/3 of tidal force); the Sun contributes ~1/3.</p>"
    "<h4>Tidal Patterns</h4>"
    "<ul><li><b>Spring tides:</b> Sun, Moon aligned (new/full Moon) → larger tidal range.</li>"
    "<li><b>Neap tides:</b> Sun, Moon at right angles (quarter Moons) → smaller tidal range.</li>"
    "<li>Most coasts have 2 high and 2 low tides per day (semidiurnal).</li></ul>",
    [("Tidal Force","Differential gravitational force across an object's diameter; stretches the object."),
     ("Spring Tide","Extra-large tidal range when Sun and Moon are aligned (new or full Moon)."),
     ("Neap Tide","Smaller tidal range when Sun and Moon are at 90° (first/third quarter Moon)."),
     ("Tidal Bulge","Elongation of Earth's water toward (and away from) the Moon due to differential gravity."),
     ("Tidal Locking","Gravitational effect that synchronized the Moon's rotation with its orbit around Earth.")],
    [("The primary cause of ocean tides is:",["The Sun's gravity","Wind","*The Moon's gravitational pull (differential force across Earth)","Earth's rotation"],"Moon causes ~2/3 of tidal force."),
     ("Spring tides occur during:",["Only spring season","*New Moon AND full Moon (Sun and Moon aligned)","Quarter Moons only","Equinoxes only"],"Alignment = stronger combined pull."),
     ("Neap tides occur during:",["New and full Moons","*First quarter and third quarter Moons (Sun and Moon at 90°)","Only summer","Equinoxes"],"Opposing pulls partially cancel."),
     ("There are typically _____ high tides per day on most coasts.",["1","*2 (semidiurnal pattern)","3","4"],"Two tidal bulges: toward and away from Moon."),
     ("The tidal bulge on the side of Earth AWAY from the Moon exists because:",["The Sun pulls it","*That side of Earth is farthest from the Moon and experiences the least gravitational pull, so water 'falls behind'","The Moon pushes water","Centrifugal force alone"],"Differential gravity (and inertia)."),
     ("The Sun's tidal effect is about _____ of the Moon's.",["Equal","Twice","*About 46% (roughly half)","10%"],"Sun is far more massive but much farther away."),
     ("Tidal range is the difference between:",["Two oceans","*High tide level and low tide level","Spring and neap tides","Fresh and salt water"],"Vertical difference in water level."),
     ("The Bay of Fundy (Canada) has the world's largest tidal range (~16 m) due to:",["Only the Moon","*The bay's shape (long, narrow funnel) amplifying tidal waves through resonance","Only the Sun","Only geography"],"Tidal resonance in the bay."),
     ("Tidal forces from the Moon are gradually:",["Speeding up Earth's rotation","*Slowing Earth's rotation (and the Moon is moving farther away)","Having no effect","Making Earth wobble more"],"Tidal friction transfers angular momentum."),
     ("The Moon is moving away from Earth at about _____ per year.",["1 mm","*~3.8 cm","1 km","10 m"],"Measured by laser retroreflectors on the Moon."),
     ("Tidal locking of the Moon was caused by:",["Random chance","*Gravitational tidal forces from Earth slowing the Moon's rotation over billions of years","Magnetic fields","Solar wind"],"Differential gravity dissipated rotational energy."),
     ("King tides occur when:",["The Moon is far away","*The Moon is at perigee (closest approach) during a spring tide → extra-high tides","The Sun is at aphelion","Nothing special"],"Perigean spring tides."),
     ("In addition to oceans, tidal forces affect:",["Nothing else","*Earth's crust (solid Earth tides), atmosphere, and the interiors of other celestial bodies","Only rivers","Only lakes"],"Solid body tides ~20 cm."),
     ("Jupiter's moon Io has intense volcanism because of:",["Internal heat alone","*Tidal heating from Jupiter's immense gravitational tidal forces","Solar radiation","Wind",""],"Tidal flexing generates enormous heat."),
     ("Tidal forces can tear apart objects that come too close to a massive body, creating:",["Moons","*Ring systems (Roche limit — below which tidal forces exceed self-gravity)","Stars","Planets"],"Saturn's rings may be tidally disrupted material."),
     ("The Roche limit is the distance within which:",["Objects gain mass","*A celestial body held together only by gravity will be torn apart by tidal forces","Tides disappear","Objects orbit faster"],"Critical distance."),
     ("Tidal heating plays a role in the potential habitability of:",["Mars","*Europa and Enceladus (subsurface oceans maintained by tidal heat)","Venus","Mercury"],"Tidal heat may keep liquid water under ice."),
     ("Understanding tides is important for:",["Nothing practical","*Navigation, coastal flooding prediction, marine biology, fishing, and coastal engineering","Only sailors","Only scientists"],"Practical applications."),
     ("Tidal predictions use:",["Only Moon phase","*Harmonic analysis based on Moon phase, distance, Sun position, and local geography","Guessing","Only historical data"],"Complex mathematical models."),
     ("Tides connect astronomy to:",["Nothing","*Oceanography, geology, planetary science, and even astrobiology","Only physics","Only geography"],"Interdisciplinary significance.")]
)
lessons[k]=v

# 2.6
k,v = build_lesson(2,6,"Case Studies in Earth-Moon-Sun Interactions",
    "<h3>Case Studies in Earth-Moon-Sun Interactions</h3>"
    "<h4>Case 1: The 2017 Total Solar Eclipse</h4>"
    "<p>Path of totality crossed the entire contiguous US. Millions observed safely. Demonstrated the importance of eclipse glasses from ground, while scientists studied the corona.</p>"
    "<h4>Case 2: Supermoon vs. Micromoon</h4>"
    "<p>A supermoon occurs when the full Moon coincides with perigee (~357,000 km); appears ~14% larger and ~30% brighter. A micromoon occurs at apogee (~406,000 km).</p>"
    "<h4>Case 3: Tidal Effects on Coastal Communities</h4>"
    "<p>King tides + sea level rise = increased coastal flooding. Communities like Miami and Venice face challenges from rising waters amplified by tidal cycles.</p>",
    [("Path of Totality","Narrow ground track (~100 km) where a total solar eclipse is visible."),
     ("Supermoon","Full Moon near perigee; appears up to ~14% larger and ~30% brighter than average."),
     ("Perigee","Closest point of the Moon's orbit to Earth (~357,000 km)."),
     ("Apogee","Farthest point of the Moon's orbit from Earth (~406,000 km)."),
     ("King Tide","Exceptionally high tide during perigean spring tides; exacerbated by sea level rise.")],
    [("The 2017 Great American Eclipse was significant because:",["It was the first eclipse ever","*Its path of totality crossed the entire contiguous US coast-to-coast","It was a lunar eclipse","It was the longest eclipse"],"Rare coast-to-coast path."),
     ("A supermoon appears larger because:",["The Moon grows","*The full Moon coincides with perigee (closest orbital approach)","The Sun is farther","Atmospheric magnification"],"~14% larger diameter."),
     ("The difference between perigee and apogee distance is approximately:",["1,000 km","*~50,000 km (357,000 to 406,000 km)","500,000 km","1 million km"],"Elliptical orbit variation."),
     ("King tides pose risks to coastal cities because:",["They are rare","*Combined with sea level rise, they can cause flooding in low-lying areas","They only affect boats","They last for weeks"],"Increasing threat with climate change."),
     ("During the 2017 eclipse, scientists studied the Sun's:",["Surface spots only","*Corona (only visible during totality) to understand solar wind and magnetic fields","Interior","Only brightness"],"Rare opportunity for corona research."),
     ("Eclipse tourism has _____ in recent decades.",["Decreased","*Grown significantly (millions travel to see total eclipses)","Stayed the same","Disappeared"],"Major tourism events."),
     ("Sea level rise makes tidal flooding:",["Less common","*More severe and more frequent in coastal cities","No different","Only seasonal"],"Rising baseline + tides = worse flooding."),
     ("Venice, Italy experiences frequent flooding (acqua alta) due to:",["Only rain","*Tides combined with land subsidence and sea level rise","Only wind","Only storms"],"Multi-factor coastal flooding."),
     ("The Moon's orbital eccentricity causes its distance to vary by:",["1%","5%","*~12% (from perigee to apogee)","50%"],"Noticeable variation."),
     ("Annular eclipses are more common than total because:",["The Moon is shrinking","*The Moon is (on average) at a distance where it appears slightly smaller than the Sun; it must be near perigee for total","The Sun is growing","They happen every month"],"Angular size relationship."),
     ("Tidal flooding in Miami Beach has increased by _____ since 2000.",["Not at all","*Over 300% (tide gauges show increasing high-tide flooding)","10%","50%"],"Sea level rise + local factors."),
     ("The next US total solar eclipse (after 2017) was/will be in:",["2050","*April 8, 2024","2030","2100"],"Another US total eclipse."),
     ("Lunar libration allows us to see slightly more than 50% of the Moon's surface over time because:",["The Moon rotates differently","*The Moon's orbit is elliptical and tilted, causing slight rocking motions","Earth rotates","The Sun moves"],"We can see ~59% over time."),
     ("The 'Earthrise' photo taken from Apollo 8 (1968) was significant because:",["It showed the Moon","*It showed Earth from the Moon for the first time, sparking environmental awareness","It proved the Moon exists","It was the first photo from space"],"Iconic image."),
     ("Tidal energy can be harnessed as:",["Only theoretical","*A renewable energy source using tidal barrages or tidal stream generators","Only by the Moon","Not possible"],"Tidal power stations exist."),
     ("The Saros cycle allows prediction of future eclipses by:",["Random guessing","*Recognizing that similar eclipses repeat every ~6,585.3 days (18 years, 11 days)","Using telescopes","Measuring brightness"],"Predictive power from cyclic behavior."),
     ("These case studies show that Earth-Moon-Sun interactions affect:",["Only astronomers","*Daily life, coastal infrastructure, energy, tourism, science, and culture","Only scientists","Only navigation"],"Practical relevance."),
     ("Studying real-world examples helps students:",["Memorize formulas","*Connect astronomical concepts to tangible impacts and deepen understanding","Only pass exams","Not at all"],"Application strengthens learning."),
     ("Future challenges from tidal flooding will require:",["Ignoring the problem","*Engineering solutions, policy changes, and understanding tidal science","Only seawalls","Only moving inland"],"Multi-disciplinary responses."),
     ("Understanding Earth-Moon-Sun dynamics is essential for:",["Nothing","*Predicting eclipses, tides, seasons, and understanding our place in the solar system","Only calendars","Only hobbyists"],"Foundational astronomical knowledge.")]
)
lessons[k]=v

# 2.7
k,v = build_lesson(2,7,"AP Prep: Orbital Calculations",
    "<h3>AP Prep: Orbital Calculations</h3>"
    "<h4>Key Formulas</h4>"
    "<ul><li><b>Kepler's 3rd law:</b> T² = a³ (years, AU) or T² = (4π²/GM)a³.</li>"
    "<li><b>Newton's gravity:</b> F = Gm₁m₂/r²; G = 6.674 × 10⁻¹¹ N·m²/kg².</li>"
    "<li><b>Orbital velocity:</b> v = √(GM/r).</li>"
    "<li><b>Escape velocity:</b> v_esc = √(2GM/r).</li>"
    "<li><b>Gravitational PE:</b> U = −Gm₁m₂/r.</li></ul>",
    [("Kepler's Third Law","T² ∝ a³; relates orbital period to semi-major axis; with Newton: T² = (4π²/GM)a³."),
     ("Gravitational Constant G","6.674 × 10⁻¹¹ N·m²/kg²; universal constant in Newton's law of gravity."),
     ("Orbital Velocity","Speed needed to maintain a circular orbit: v = √(GM/r); decreases with distance."),
     ("Escape Velocity","Minimum speed to escape a body's gravity: v_esc = √(2GM/r); independent of projectile mass."),
     ("Gravitational Potential Energy","U = −Gm₁m₂/r; negative because work must be done to separate masses.")],
    [("Kepler's third law in simplified form (AU, years) is:",["T = a","T² = a²","*T² = a³","T³ = a²"],"Period squared = semi-major axis cubed."),
     ("A planet at 4 AU from the Sun has an orbital period of:",["4 years","16 years","*8 years (T² = 4³ = 64; T = 8)","2 years"],"T² = a³ = 64; T = √64 = 8."),
     ("Newton's law of gravitation is:",["F = ma","*F = Gm₁m₂/r²","F = mv²/r","F = Gm/r"],"Inverse-square law of gravity."),
     ("If the distance between two objects doubles, gravitational force:",["Doubles","Halves","*Decreases to 1/4","Quadruples"],"F ∝ 1/r² → 1/4 at 2r."),
     ("The gravitational constant G equals:",["9.8 m/s²","*6.674 × 10⁻¹¹ N·m²/kg²","3 × 10⁸ m/s","1.0"],"Very small number."),
     ("Orbital velocity is given by v = √(GM/r). As r increases, v:",["Increases","*Decreases","Stays constant","Becomes zero"],"Farther orbits are slower."),
     ("Escape velocity depends on:",["The projectile's mass","*The central body's mass and radius (v_esc = √(2GM/r))","Only speed","Color"],"Independent of the escaping object's mass."),
     ("Earth's escape velocity is approximately:",["1 km/s","*11.2 km/s","100 km/s","300,000 km/s"],"Must reach 11.2 km/s to leave Earth."),
     ("Gravitational potential energy is negative by convention because:",["It's always negative","*Objects must gain energy to separate; the zero reference is at infinite separation","It doesn't exist","Gravity pushes"],"Bound systems have negative energy."),
     ("For a circular orbit, gravitational force provides the:",["Tangential force","*Centripetal force (keeping the object in orbit)","No force","Push force"],"F_gravity = F_centripetal."),
     ("The mass of a central body can be calculated from orbital data using:",["Only distance","*Kepler's third law with Newton's modification: M = 4π²a³/(GT²)","Only velocity","Only brightness"],"Powerful tool."),
     ("A geosynchronous orbit has a period of:",["12 hours","*24 hours (matches Earth's rotation)","1 hour","1 year"],"Satellite stays above the same point."),
     ("The altitude of a geosynchronous orbit is approximately:",["200 km","*~35,800 km above Earth's surface","100,000 km","1,000 km"],"Calculated from Kepler's third law."),
     ("Hohmann transfer orbit is:",["A circular orbit","*An elliptical orbit used to transfer between two circular orbits using minimum energy","A hyperbolic trajectory","A straight line"],"Efficient orbital maneuver."),
     ("An object in a higher orbit has _____ orbital velocity and _____ period.",["Higher; shorter","*Lower; longer","Same; same","Lower; shorter"],"Farther = slower and longer period."),
     ("The vis-viva equation v² = GM(2/r − 1/a) relates:",["Only mass and speed","*Orbital speed at any point to the semi-major axis and current distance","Only distance and time","Only energy and mass"],"General energy equation for orbits."),
     ("At the AP level, students should solve problems involving:",["Only definitions","*Orbital periods, velocities, escape velocities, and gravitational forces using formulas","Only history","Only descriptions"],"Quantitative problem-solving."),
     ("The Moon's orbital velocity around Earth is approximately:",["11.2 km/s","*~1 km/s","100 km/s","0.1 km/s"],"Much slower than Earth's escape velocity."),
     ("Tidal forces are proportional to:",["1/r²","*1/r³ (tidal force depends on the DIFFERENCE in gravity across an object)","1/r","r²"],"Falls off faster than gravity."),
     ("Understanding orbital calculations is essential for:",["Nothing","*Space mission planning, satellite placement, planetary science, and understanding celestial mechanics","Only NASA","Only physics class"],"Applied physics.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 2: wrote {len(lessons)} lessons")
