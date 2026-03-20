#!/usr/bin/env python3
"""Astronomy Unit 4 – The Sun (7 lessons)."""
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

# 4.1
k,v = build_lesson(4,1,"Structure of the Sun",
    "<h3>Structure of the Sun</h3>"
    "<h4>Interior</h4>"
    "<ul><li><b>Core:</b> ~15 million K; nuclear fusion occurs here. ~25% of solar radius.</li>"
    "<li><b>Radiative zone:</b> Energy moves outward via photon absorption/re-emission; takes ~170,000 years.</li>"
    "<li><b>Convective zone:</b> Energy carried by rising hot plasma and sinking cool plasma (convection cells).</li></ul>"
    "<h4>Atmosphere</h4>"
    "<ul><li><b>Photosphere:</b> Visible surface, ~5,800 K. Granulation visible.</li>"
    "<li><b>Chromosphere:</b> Pinkish layer above photosphere; visible during eclipses.</li>"
    "<li><b>Corona:</b> Outermost atmosphere; extremely hot (~1–3 million K); visible during total solar eclipses.</li></ul>",
    [("Core","Sun's center; ~15 million K; site of hydrogen fusion; produces 99% of the Sun's energy."),
     ("Radiative Zone","Layer where energy travels outward via photon absorption and re-emission."),
     ("Convective Zone","Outer zone where hot plasma rises and cool plasma sinks; creates granulation."),
     ("Photosphere","Visible surface of the Sun; ~5,800 K; shows sunspots and granulation."),
     ("Corona","Outermost solar atmosphere; ~1–3 million K; visible during total solar eclipses.")],
    [("The Sun's core temperature is approximately:",["5,800 K","100,000 K","*~15 million K","1 billion K"],"Hot enough for fusion."),
     ("Nuclear fusion in the Sun occurs in the:",["Photosphere","Corona","*Core","Convective zone"],"Only the core is hot and dense enough."),
     ("In the radiative zone, energy is transferred by:",["Convection","Sound waves","*Photon absorption and re-emission (radiation)","Conduction"],"Photons diffuse outward."),
     ("A photon takes approximately _____ to travel from the core to the surface.",["1 second","1 year","*~170,000 years","1 million years"],"Random walk through the radiative zone."),
     ("The convective zone transports energy by:",["Radiation only","*Rising hot plasma and sinking cool plasma (convection)","Conduction","Sound"],"Bubbling motion."),
     ("The photosphere is the Sun's:",["Core","*Visible surface (~5,800 K)","Corona","Magnetic field"],"What we see as the Sun's disk."),
     ("Granulation on the Sun's surface is caused by:",["Sunspots","Magnetic fields","*Tops of convection cells (hot plasma rises in centers, cool plasma sinks at edges)","Solar wind"],"~1,000 km wide convection cells."),
     ("The chromosphere is:",["The core","*The thin pinkish atmospheric layer just above the photosphere","The outermost layer","The convective zone"],"Visible during eclipses as a red ring."),
     ("The corona is:",["The visible surface","*The Sun's outermost atmosphere; extremely hot (~1–3 million K)","The core","The radiative zone"],"Paradoxically much hotter than the photosphere."),
     ("The coronal heating problem refers to:",["The core being cold","*Why the corona (~1–3 million K) is far hotter than the photosphere (~5,800 K)","Too much rain on the Sun","Nothing"],"One of solar physics' biggest puzzles."),
     ("The Sun's diameter is approximately:",["1,000 km","*~1.4 million km (~109 Earth diameters)","10 million km","100 km"],"Very large."),
     ("The Sun's mass is approximately:",["Equal to Earth","*~2 × 10³⁰ kg (~333,000 Earth masses)","10× Earth","Half of Jupiter"],"Dominates the solar system."),
     ("The Sun is classified as a:",["Red giant","White dwarf","*G-type main sequence star (yellow dwarf)","Neutron star"],"G2V spectral type."),
     ("The Sun is composed primarily of:",["Iron and nickel","*Hydrogen (~73%) and helium (~25%)","Oxygen and nitrogen","Carbon dioxide"],"Like most stars."),
     ("Helioseismology studies the Sun using:",["Light only","*Sound waves (oscillations) that travel through the interior","Gravity waves","X-rays only"],"Like seismology for the Sun."),
     ("The tachocline is:",["A surface feature","*The boundary between the radiative and convective zones; important for generating the magnetic field","The core-surface boundary","Part of the corona"],"Key layer for the solar dynamo."),
     ("The Sun's luminosity is approximately:",["1 watt","1 billion watts","*3.8 × 10²⁶ watts","1 × 10¹⁰ watts"],"Enormous energy output."),
     ("The Sun will eventually evolve into a:",["Black hole","Neutron star","*Red giant, then a white dwarf","Supernova"],"Not massive enough for a supernova."),
     ("The Sun's age is approximately:",["1 billion years","*4.6 billion years","10 billion years","100 million years"],"Middle-aged main-sequence star."),
     ("Understanding solar structure is essential for:",["Nothing","*Comprehending energy production, solar activity, space weather, and stellar physics generally","Only solar panels","Only eclipses"],"Foundation for stellar astrophysics.")]
)
lessons[k]=v

# 4.2
k,v = build_lesson(4,2,"Nuclear Fusion",
    "<h3>Nuclear Fusion in the Sun</h3>"
    "<h4>The Proton-Proton Chain</h4>"
    "<p>Dominant fusion process in the Sun. Net reaction: 4 ¹H → ¹ ⁴He + 2 positrons + 2 neutrinos + energy (26.7 MeV).</p>"
    "<h4>Key Physics</h4>"
    "<ul><li>Mass deficit (Δm) converted to energy via E = mc².</li>"
    "<li>~0.7% of hydrogen mass converted to energy per reaction.</li>"
    "<li>Sun converts ~600 million tons of H into He every second.</li>"
    "<li>Solar neutrinos pass through matter nearly unimpeded → neutrino detectors confirm fusion.</li></ul>",
    [("Proton-Proton Chain","Primary fusion reaction in the Sun; four hydrogen nuclei fuse to form one helium nucleus + energy."),
     ("E = mc²","Einstein's equation; mass deficit is converted to energy in nuclear reactions."),
     ("Mass Deficit","Difference between the mass of reactants and products in a nuclear reaction; released as energy."),
     ("Neutrino","Nearly massless, chargeless particle produced in fusion; escapes the Sun almost immediately."),
     ("Luminosity","Total energy output of a star per unit time; Sun's luminosity = 3.8 × 10²⁶ W.")],
    [("The primary nuclear reaction in the Sun is:",["Fission of uranium","*The proton-proton chain (4 H → He + energy)","Carbon burning","Electron capture"],"Dominant in G-type stars."),
     ("In the proton-proton chain, the net result is:",["Helium → hydrogen","*4 hydrogen nuclei → 1 helium-4 nucleus + 2 positrons + 2 neutrinos + energy","Hydrogen → iron","Carbon → oxygen"],"Net fusion equation."),
     ("The energy released comes from:",["Chemical bonds","*The mass deficit (Δm) converted to energy via E = mc²","Gravity alone","Electrical potential"],"Mass-energy equivalence."),
     ("Approximately _____ of the hydrogen mass is converted to energy per fusion reaction.",["50%","10%","*~0.7%","100%"],"Small fraction, enormous energy due to c²."),
     ("The Sun converts roughly _____ of hydrogen to helium every second.",["1 kg","1,000 tons","*~600 million tons","1 billion tons"],"Enormous rate of fusion."),
     ("Nuclear fusion requires extremely high temperatures because:",["Atoms are cold","*Protons must overcome their electrostatic (Coulomb) repulsion to get close enough for the strong force","Gravity is weak","Neutrons are heavy"],"~15 million K needed."),
     ("Quantum tunneling is important in solar fusion because:",["It isn't","*It allows protons to overcome the Coulomb barrier even without sufficient classical energy","It creates light","It stops reactions"],"Probability of barrier penetration."),
     ("Solar neutrinos are important because:",["They heat the Earth","*They directly confirm that fusion is occurring in the Sun's core (they escape immediately)","They are visible","They cause tides"],"Neutrino detection = fusion proof."),
     ("The solar neutrino problem (now solved) was:",["Too many neutrinos","*Fewer electron neutrinos detected than predicted; explained by neutrino oscillations","No neutrinos at all","Neutrinos were too heavy"],"Neutrinos change flavor."),
     ("The CNO cycle (carbon-nitrogen-oxygen) is:",["The Sun's main reaction","*A secondary fusion process more important in hotter, more massive stars","Combustion","Not real"],"Dominant in stars >1.3 M☉."),
     ("Hydrostatic equilibrium in the Sun means:",["It's falling apart","*Outward radiation/gas pressure balances inward gravitational force","It's expanding","It's cooling"],"Keeps the Sun stable."),
     ("If fusion in the core suddenly stopped, the Sun's photosphere would:",["Go dark instantly","*Continue shining for ~170,000+ years (photons take that long to reach the surface)","Explode","Turn blue"],"Photon travel time through the interior."),
     ("However, the Sun's gravitational structure would be affected in roughly:",["170,000 years","Millions of years","*~30 minutes (the time for a pressure wave to change the structure)","Never"],"Timescale for structural adjustment differs from photon diffusion."),
     ("The Sun has enough hydrogen fuel to last approximately:",["1 million more years","100 years","*~5 billion more years","Forever"],"Total main-sequence lifetime ~10 Gyr."),
     ("Fusion on Earth (e.g., ITER, NIF) is challenging because:",["It's easy","*Confining plasma at >100 million K for sustained reactions is extremely difficult","We lack hydrogen","Fusion doesn't work on Earth"],"Engineering grand challenge."),
     ("Positrons produced in the p-p chain immediately:",["Escape the Sun","*Annihilate with electrons, releasing gamma-ray photons","Become protons","Do nothing"],"Matter-antimatter annihilation."),
     ("The energy produced in the Sun's core is initially in the form of:",["Visible light","Sound","*Gamma rays (very high-energy photons)","Radio waves"],"Downgraded to visible light by the time it reaches the surface."),
     ("The Sun's energy output (luminosity) is approximately:",["100 W","1 million W","*3.8 × 10²⁶ W","1 × 10¹⁵ W"],"Enormous."),
     ("Understanding nuclear fusion is important for:",["Nothing","*Explaining stellar energy, nucleosynthesis, and pursuing fusion energy on Earth","Only bombs","Only the Sun"],"Fundamental astrophysics and energy science."),
     ("Stars more massive than the Sun primarily use:",["The p-p chain","*The CNO cycle for hydrogen fusion (higher temperature-dependent)","No fusion","Chemical reactions"],"CNO dominates at higher T.")]
)
lessons[k]=v

# 4.3
k,v = build_lesson(4,3,"Solar Activity (Sunspots, Flares, Prominences)",
    "<h3>Solar Activity</h3>"
    "<h4>Sunspots</h4>"
    "<p>Dark regions on the photosphere (~3,500–4,500 K vs ~5,800 K); caused by concentrated magnetic fields inhibiting convection. Follow an ~11-year solar cycle.</p>"
    "<h4>Solar Flares</h4>"
    "<p>Sudden eruptions of energy from the Sun's surface; release radiation across the EM spectrum. Can disrupt communications and GPS.</p>"
    "<h4>Prominences &amp; CMEs</h4>"
    "<p>Prominences: arcs of plasma along magnetic field lines. Coronal Mass Ejections (CMEs): massive expulsions of plasma and magnetic field; can trigger geomagnetic storms on Earth.</p>",
    [("Sunspot","Cooler, darker region on the photosphere caused by strong magnetic fields (~3,500–4,500 K)."),
     ("Solar Cycle","~11-year cyclical variation in sunspot number and solar activity; magnetic polarity reverses every cycle."),
     ("Solar Flare","Sudden, intense burst of electromagnetic radiation from the Sun's surface; powered by magnetic reconnection."),
     ("Coronal Mass Ejection","Massive expulsion of plasma and magnetic field from the corona; can cause geomagnetic storms."),
     ("Prominence","Arc of dense, relatively cool plasma suspended above the photosphere by magnetic fields.")],
    [("Sunspots appear darker because they are:",["Hotter than surroundings","Holes in the Sun","*Cooler than the surrounding photosphere (~3,500–4,500 K vs ~5,800 K)","Paint"],"Cooler = darker in contrast."),
     ("Sunspots are caused by:",["Comets hitting the Sun","*Concentrated magnetic fields that inhibit convection, cooling the area","Volcanic eruptions","Chemical reactions"],"Magnetic suppression of convection."),
     ("The solar cycle has a period of approximately:",["1 year","100 years","*~11 years","1,000 years"],"Sunspot number rises and falls."),
     ("At solar maximum, the Sun has:",["No sunspots","*The most sunspots and highest solar activity","Fewer flares","Reduced energy"],"Peak activity."),
     ("The Sun's magnetic polarity reverses every:",["1 year","*~11 years (completing a full 22-year magnetic cycle)","100 years","Never"],"22-year magnetic cycle."),
     ("Solar flares release energy primarily through:",["Nuclear fusion","*Magnetic reconnection (stored magnetic energy suddenly released)","Chemical reactions","Gravity"],"Rapid energy release."),
     ("Solar flares emit radiation across:",["Only visible light","Only X-rays","*The entire electromagnetic spectrum (radio to gamma rays)","Only infrared"],"Broadband emission."),
     ("A coronal mass ejection (CME) differs from a solar flare in that:",["They're the same","*A CME is a massive release of plasma and magnetic field, while a flare is primarily radiation","CMEs are smaller","Flares are bigger"],"Different phenomena, often occur together."),
     ("CMEs reaching Earth can cause:",["Nothing","*Geomagnetic storms → aurora, satellite damage, power grid disruptions, communication interference","Only pretty lights","Only heating"],"Space weather hazards."),
     ("The Carrington Event (1859) was:",["A minor event","*The most intense recorded geomagnetic storm; caused by a massive CME; auroras seen near the equator","A solar eclipse","A comet impact"],"Telegraph systems sparked and caught fire."),
     ("Prominences are:",["Always explosive","*Arcs or loops of plasma suspended by magnetic fields above the photosphere","Part of the core","Inside the Sun"],"Can persist for days-weeks."),
     ("Spicules are:",["Sunspots","*Jet-like columns of plasma shooting up from the chromosphere (~10,000 km tall)","CMEs","Prominences"],"Dynamic solar atmosphere."),
     ("Solar activity affects Earth's:",["Nothing","*Space weather (aurora, satellite drag, communication disruptions, radiation exposure for astronauts)","Core temperature","Orbit"],"Real impacts on technology and astronauts."),
     ("The Maunder Minimum (1645–1715) was a period of:",["High solar activity","*Very few sunspots; coincided with the Little Ice Age (correlation debated)","Many eclipses","No astronomy"],"Reduced solar activity."),
     ("Sunspot polarity follows _____ law.",["Newton's","*Hale's law (leading sunspot polarity is opposite in N/S hemispheres, switching each cycle)","Kepler's","Hubble's"],"Magnetic polarity patterns."),
     ("Modern solar monitoring satellites include:",["Only Hubble","*SDO (Solar Dynamics Observatory), SOHO, and Parker Solar Probe","Only ground telescopes","None"],"Continuous monitoring."),
     ("The Parker Solar Probe is:",["Orbiting Jupiter","*The closest human-made object to the Sun, studying the corona and solar wind directly","A ground telescope","A Mars rover"],"Launched 2018; making progressively closer passes."),
     ("Space weather forecasting is important for:",["Nothing practical","*Protecting satellites, astronauts, power grids, and communication systems","Only military","Only airlines"],"Growing importance as society depends on technology."),
     ("Solar activity research connects to:",["Only Sun study","*Stellar physics, space weather, climate science, and plasma physics","Only sunspots","Only pretty pictures"],"Interdisciplinary significance."),
     ("Students should understand solar activity because it demonstrates:",["Nothing","*How magnetic fields drive dynamic phenomena, affecting both the Sun and Earth","Only physics equations","Only history"],"Real-world applied physics.")]
)
lessons[k]=v

# 4.4
k,v = build_lesson(4,4,"Solar Wind & Magnetic Fields",
    "<h3>Solar Wind &amp; Magnetic Fields</h3>"
    "<h4>Solar Wind</h4>"
    "<p>Continuous stream of charged particles (protons, electrons) flowing from the corona at ~400–800 km/s. Carves out the heliosphere — the Sun's region of influence — extending to ~120 AU.</p>"
    "<h4>Solar Magnetic Field</h4>"
    "<p>Generated by the solar dynamo (differential rotation + convection). Creates complex field lines that trap plasma, drive sunspots, flares, and CMEs. The interplanetary magnetic field (IMF) spirals outward (Parker spiral).</p>",
    [("Solar Wind","Stream of charged particles (plasma) flowing from the Sun's corona at 400–800 km/s."),
     ("Heliosphere","Bubble of space dominated by the solar wind; extends to ~120 AU; Voyager 1 & 2 have crossed its boundary."),
     ("Parker Spiral","The spiral shape of the interplanetary magnetic field due to the Sun's rotation and outward-flowing solar wind."),
     ("Solar Dynamo","The mechanism generating the Sun's magnetic field through differential rotation and convection of conducting plasma."),
     ("Heliopause","Boundary where the solar wind pressure equals the interstellar medium pressure; edge of the heliosphere.")],
    [("The solar wind is composed of:",["Neutral atoms","Light only","*Charged particles (mainly protons and electrons — plasma)","Dust"],"Ionized gas streaming outward."),
     ("Solar wind speeds range from approximately:",["1–10 km/s","*400–800 km/s","Speed of light","1 km/h"],"Fast and slow solar wind."),
     ("The heliosphere extends to approximately:",["1 AU","10 AU","*~120 AU (Voyager 1 crossed it in 2012)","1,000 AU"],"Sun's sphere of influence."),
     ("The heliopause is where:",["The Sun's surface ends","*Solar wind pressure balances the interstellar medium pressure","Earth's atmosphere ends","Nothing happens"],"Edge of the heliosphere."),
     ("The Parker spiral describes:",["A tornado","*The spiral shape of the interplanetary magnetic field due to solar rotation + radial wind outflow","A galaxy shape","A DNA strand"],"Like water from a spinning sprinkler."),
     ("The Sun's magnetic field is generated by:",["Permanent magnets","*The solar dynamo (differential rotation and convection of conducting plasma)","Nuclear fusion directly","External forces"],"Moving conductor → magnetic field."),
     ("Differential rotation means:",["The Sun rotates uniformly","*The Sun rotates faster at the equator (~25 days) than at the poles (~35 days)","The Sun doesn't rotate","Rotation varies randomly"],"Stretches and tangles field lines."),
     ("Earth's magnetosphere protects us from the solar wind by:",["Blocking all particles","*Deflecting most charged particles around Earth via its magnetic field","Nothing","Only creating aurora"],"Magnetic shield."),
     ("Aurora (Northern/Southern Lights) occur when:",["The Sun is visible","*Solar wind particles are funneled along Earth's magnetic field lines into the atmosphere near the poles","Comets pass","The Moon reflects light"],"Particles excite atmospheric gases."),
     ("Geomagnetic storms are caused by:",["Earthquakes","*CMEs or high-speed solar wind streams interacting with Earth's magnetosphere","The Moon","Volcanoes"],"Magnetosphere disturbance."),
     ("The solar wind carries the Sun's magnetic field out into space, creating:",["Nothing","*The interplanetary magnetic field (IMF)","Stars","Galaxies"],"Frozen-in magnetic field carried by plasma."),
     ("Alfvén waves in the solar wind are:",["Sound waves","*Magnetohydrodynamic waves that may help heat the corona and accelerate the solar wind","Light waves","Gravity waves"],"Named after Hannes Alfvén."),
     ("The solar wind strips atmospheres from planets that lack:",["Gravity","*A strong magnetic field (like Mars)","Water","An iron core"],"Magnetic field = atmospheric shield."),
     ("Van Allen radiation belts around Earth are:",["Clouds","*Zones of charged particles trapped by Earth's magnetic field","Part of the atmosphere","Visible"],"Hazard for spacecraft."),
     ("Solar wind measurements help predict:",["Earthquakes","*Space weather events that could affect satellites, power grids, and astronauts","Rain","Tides"],"Space weather forecasting."),
     ("The South Atlantic Anomaly is:",["An ocean current","*A region where Earth's magnetic field is weaker and the inner Van Allen belt dips closer to the surface","A hurricane","A tidal zone"],"Increased radiation exposure for satellites and ISS."),
     ("The Sun's magnetic field reverses polarity every _____ years.",["1","5","*~11 (completing a full 22-year magnetic cycle)","100"],"Tied to the solar cycle."),
     ("Without the heliosphere, Earth would be more exposed to:",["Nothing","*Galactic cosmic rays from outside the solar system","Sunlight","The Moon's gravity"],"Heliosphere partially shields us."),
     ("The Parker Solar Probe aims to understand:",["Mars","*How the solar wind is accelerated and the corona is heated","The outer planets","Comets"],"Key unsolved questions."),
     ("Studying the solar wind and magnetic fields is important for:",["Nothing","*Space weather prediction, understanding stellar physics, and protecting technology","Only solar scientists","Only astronauts"],"Broad significance.")]
)
lessons[k]=v

# 4.5
k,v = build_lesson(4,5,"Impact on Earth's Climate & Technology",
    "<h3>Impact on Earth's Climate &amp; Technology</h3>"
    "<h4>Climate Connections</h4>"
    "<p>Solar irradiance varies ~0.1% over the solar cycle — small but measurable. Longer-term variations (e.g., Maunder Minimum) may influence climate trends. However, current climate change is primarily driven by human greenhouse gas emissions.</p>"
    "<h4>Technology Impacts</h4>"
    "<ul><li>Geomagnetic storms → power grid surges (Québec 1989 blackout).</li>"
    "<li>Satellite drag in expanded upper atmosphere; GPS/communication disruptions.</li>"
    "<li>Radiation exposure for astronauts and high-altitude pilots.</li></ul>",
    [("Total Solar Irradiance","Total solar energy per unit area at Earth's distance; ~1,361 W/m²; varies ~0.1% over the solar cycle."),
     ("Maunder Minimum","Period (1645–1715) of very few sunspots; possibly linked to the Little Ice Age (correlation debated)."),
     ("Geomagnetic Storm","Disturbance of Earth's magnetosphere caused by solar wind/CME; can affect power grids and communications."),
     ("Québec Blackout (1989)","Major geomagnetic storm caused a 12-hour power outage affecting 6 million people in Québec, Canada."),
     ("Space Weather","Conditions in space (solar wind, CMEs, radiation) that affect Earth's technology and human spaceflight.")],
    [("Solar irradiance varies by approximately _____ over the ~11-year solar cycle.",["10%","50%","*~0.1%","0%"],"Small but measurable."),
     ("Total solar irradiance at Earth's distance is approximately:",["100 W/m²","*~1,361 W/m²","10,000 W/m²","1 W/m²"],"Solar constant."),
     ("The Maunder Minimum coincided with:",["A major warming event","*The Little Ice Age (colder European temperatures, 1645–1715)","A solar maximum","Nothing"],"Possible correlation (debate ongoing)."),
     ("Current global climate change is primarily driven by:",["Solar variations alone","*Human emissions of greenhouse gases (CO₂, CH₄, etc.)","The Moon","Volcanic activity alone"],"Scientific consensus."),
     ("Solar variability's contribution to recent warming is:",["Dominant","*Small compared to anthropogenic greenhouse gas effects","100%","Equal"],"IPCC: solar forcing is minor."),
     ("The 1989 Québec blackout was caused by:",["An earthquake","A hurricane","*A geomagnetic storm from a CME inducing currents in the power grid","A software bug"],"GIC (geomagnetically induced currents) damaged transformers."),
     ("Geomagnetic storms can damage satellites by:",["Not at all","*Charging surfaces, degrading electronics, and increasing atmospheric drag (expanding thermosphere)","Only shaking them","Only blocking signals"],"Multiple mechanisms."),
     ("GPS accuracy can be degraded during solar storms because:",["Satellites fail","*Ionospheric disturbances affect signal propagation","Satellites move","GPS clocks stop"],"Ionosphere changes signal path."),
     ("Astronauts on the ISS are at risk from:",["Nothing","*Increased radiation during solar particle events (SPEs)","Meteorite showers only","Extreme cold only"],"Radiation is a real concern."),
     ("High-altitude airline routes over the poles may be rerouted during:",["Calm weather","*Major solar storms (to reduce communication blackouts and radiation exposure for crews/passengers)","Eclipses","Full Moons"],"Operational precaution."),
     ("A Carrington-scale event today could cause:",["No problems","*Trillions of dollars in damage to power grids, satellites, and communication systems globally","Only minor Aurora","Only GPS errors"],"Modern infrastructure is vulnerable."),
     ("Milankovitch cycles (orbital variations) affect climate over:",["Days","*Tens of thousands of years (eccentricity, axial tilt, precession)","Seconds","Millions of years"],"Long-term climate drivers."),
     ("The relationship between sunspots and climate is:",["Simple and direct","*Complex and debated; some correlation exists but the mechanism and magnitude are uncertain","Nonexistent","Fully understood"],"Active area of research."),
     ("Monitoring the Sun for space weather uses:",["Only ground telescopes","*Satellites like SDO, SOHO, STEREO, and DSCOVR positioned for continuous observation","Only amateur astronomers","Nothing"],"Space-based monitoring."),
     ("The NOAA Space Weather Prediction Center:",["Predicts regular weather only","*Issues forecasts and warnings for geomagnetic storms, solar flares, and radiation events","Studies earthquakes","Tracks hurricanes only"],"US space weather forecasting."),
     ("Faraday cages and transformer protections help:",["Nothing","*Shield sensitive electronics from geomagnetically induced currents during storms","Only block light","Only reduce noise"],"Engineering solutions."),
     ("Solar panels on Earth are affected by the solar cycle because:",["They don't work","*Higher solar activity can damage satellites that rely on solar power; ground panels are minimally affected","The Sun turns off","Clouds form more"],"Primarily a satellite concern."),
     ("Understanding how the Sun affects Earth is important for:",["Nobody","*Policy makers, engineers, astronauts, power grid operators, and climate scientists","Only astronomers","Only farmers"],"Wide-ranging stakeholders."),
     ("Solar-terrestrial physics is the study of:",["Only the Sun","*Interactions between the Sun and Earth's magnetosphere, ionosphere, and atmosphere","Only Earth","Only the Moon"],"Interdisciplinary field."),
     ("Preparing for extreme solar events requires:",["Nothing","*Investment in monitoring, early warning systems, grid hardening, and emergency planning","Only waiting","Only praying"],"Proactive approach.")]
)
lessons[k]=v

# 4.6
k,v = build_lesson(4,6,"Case Studies in Solar Observation",
    "<h3>Case Studies in Solar Observation</h3>"
    "<h4>SDO (Solar Dynamics Observatory)</h4>"
    "<p>Launched 2010; provides high-resolution images of the Sun every 12 seconds; studies magnetic field, atmosphere, and energy output in multiple wavelengths.</p>"
    "<h4>Parker Solar Probe</h4>"
    "<p>Launched 2018; will pass within 6.1 million km of the Sun's surface; measures solar wind, magnetic fields, and energetic particles in situ. Uses a carbon-composite heat shield.</p>"
    "<h4>Historical: Galileo's Sunspot Observations</h4>"
    "<p>Galileo (1612) documented sunspots, showing the Sun is not a perfect, unchanging sphere — a revolutionary finding.</p>",
    [("SDO","Solar Dynamics Observatory (NASA, 2010); continuous high-resolution solar imaging in multiple wavelengths."),
     ("Parker Solar Probe","NASA probe making the closest passes to the Sun; studying corona and solar wind in situ."),
     ("SOHO","Solar and Heliospheric Observatory (ESA/NASA, 1995); studies the Sun from the L1 Lagrange point."),
     ("Galileo's Sunspot Observations","Early 1600s telescope observations demonstrating the Sun has blemishes and rotates."),
     ("Solar Spectroscopy","Analyzing sunlight's spectrum to determine the Sun's composition, temperature, and magnetic fields.")],
    [("The Solar Dynamics Observatory (SDO) has revealed:",["Nothing new","*Unprecedented detail of solar flares, CMEs, and magnetic field dynamics through continuous imaging","Only sunspots","Only the corona"],"Revolutionary observations."),
     ("SDO images the Sun every:",["1 minute","1 hour","*~12 seconds (in multiple wavelengths)","Once a day"],"Extremely high cadence."),
     ("The Parker Solar Probe will pass within approximately:",["1 million km","*~6.1 million km (~9.86 solar radii) of the Sun's surface","100 million km","1 AU"],"Closest approach to a star."),
     ("Parker Solar Probe's heat shield can withstand temperatures up to:",["100°C","500°C","*~1,370°C (while keeping instruments at ~30°C)","5,000°C"],"Carbon-composite thermal shield."),
     ("SOHO orbits at the _____ Lagrange point.",["L2","L3","*L1 (between Earth and Sun, ~1.5 million km from Earth)","L4"],"Uninterrupted solar view."),
     ("Galileo's sunspot observations (1612) were revolutionary because:",["Telescopes were new","*They showed the Sun was imperfect and rotated, challenging the prevailing view of celestial perfection","He invented the Sun","He discovered helium"],"Broke the Aristotelian idea of unchanging heavens."),
     ("Spectroscopy of sunlight revealed that the Sun contains:",["Only hydrogen","*All naturally occurring elements (hydrogen, helium — even discovered through solar spectrum — plus metals)","Only helium","Only oxygen"],"Helium was discovered in the solar spectrum first."),
     ("The element helium was first discovered:",["On Earth","*In the Sun's spectrum (1868, during a solar eclipse) before being found on Earth","In the Moon","In a lab"],"Named after Helios (Greek Sun god)."),
     ("Joseph von Fraunhofer identified _____ in the solar spectrum.",["Colors only","*Dark absorption lines (Fraunhofer lines) corresponding to specific elements","Bright spots","Nothing"],"Foundational spectroscopy."),
     ("Solar observatories like Big Bear (California) use:",["Only cameras","*Specialized solar telescopes with adaptive optics for high-resolution surface imaging","Only radio receivers","Only naked-eye viewing"],"Ground-based solar astronomy."),
     ("The Hinode satellite (JAXA) focuses on:",["The Moon","*The Sun's magnetic field structure and its role in driving solar activity","Mars","Asteroids"],"Magnetic field observations."),
     ("Solar Orbiter (ESA) will provide:",["No new data","*The first close-up images of the Sun's poles","Only far-away images","Only magnetic data"],"Complementing Parker Solar Probe."),
     ("Coronagraphs work by:",["Blocking the Moon","*Using an artificial disk to block the Sun's bright photosphere, revealing the corona","Blocking stars","Enlarging the Sun"],"Artificial eclipse."),
     ("Solar radio astronomy detects:",["Only sunlight","*Radio emissions from the Sun's atmosphere, often associated with flares and CMEs","Only pulsars","Nothing from the Sun"],"Different wavelength → different information."),
     ("The Maunder Butterfly Diagram shows:",["Cloud patterns","*How sunspot latitudes migrate from mid-latitudes toward the equator over each solar cycle","Moon phases","Eclipse patterns"],"Classic visualization of the solar cycle."),
     ("Modern solar observations span:",["Only visible light","*The entire electromagnetic spectrum from radio to gamma rays","Only X-rays","Only infrared"],"Multi-wavelength approach."),
     ("Citizen science projects like Solar Stormwatch allow the public to:",["Build telescopes","*Help classify solar events and contribute to space weather research","Only watch videos","Only donate money"],"Public engagement in science."),
     ("Each major solar mission has contributed:",["Nothing unique","*New discoveries that refined our understanding of the Sun and its influence","Only pretty pictures","Only to NASA's budget"],"Cumulative knowledge."),
     ("The history of solar observation demonstrates:",["Science is static","*How technology advances (from Galileo's telescope to space probes) drive scientific progress","Only old techniques matter","Nothing meaningful"],"Progressive improvement."),
     ("Studying these case studies helps students see:",["Only facts and dates","*The scientific process in action — observation, hypothesis, technology innovation, and discovery","Nothing useful","Only history"],"Science as a process.")]
)
lessons[k]=v

# 4.7
k,v = build_lesson(4,7,"AP Prep: Energy Calculations",
    "<h3>AP Prep: Energy Calculations</h3>"
    "<h4>Key Equations</h4>"
    "<ul><li><b>E = mc²:</b> Energy equivalent of mass. For solar fusion: Δm × c² = energy released per reaction.</li>"
    "<li><b>Luminosity:</b> L = 4πR²σT⁴ (Stefan-Boltzmann law for stellar luminosity).</li>"
    "<li><b>Flux:</b> F = L/(4πd²) — brightness decreases with distance squared.</li>"
    "<li><b>Wien's law:</b> λ_max = 2.898 × 10⁶ / T (nm); peak wavelength of emission for a blackbody.</li></ul>",
    [("Stefan-Boltzmann Law","L = 4πR²σT⁴; luminosity depends on surface area and temperature to the 4th power."),
     ("Inverse Square Law (Flux)","F = L/(4πd²); observed brightness decreases with the square of the distance."),
     ("Wien's Displacement Law","λ_max = 2.898 × 10⁶ / T (nm, K); hotter objects peak at shorter wavelengths."),
     ("Blackbody Radiation","Idealized emission spectrum depending only on temperature; stars approximate blackbodies."),
     ("Mass-Energy Equivalence","E = mc²; mass can be converted to energy; explains stellar energy production.")],
    [("E = mc² means that 1 kg of mass is equivalent to:",["9 × 10⁸ J","*9 × 10¹⁶ J","1 J","9 × 10²⁴ J"],"E = 1 × (3×10⁸)² = 9×10¹⁶ J."),
     ("In the Sun's p-p chain, the mass deficit per reaction is ~0.048 × 10⁻²⁷ kg. The energy released is approximately:",["1 eV","*~4.3 × 10⁻¹² J (26.7 MeV)","1 J","1 kJ"],"Δm × c² ≈ 4.3 × 10⁻¹² J."),
     ("The Stefan-Boltzmann law states L = 4πR²σT⁴. If temperature doubles, luminosity changes by a factor of:",["2","4","8","*16 (2⁴)"],"T⁴ dependence."),
     ("If a star's radius doubles (same T), its luminosity changes by a factor of:",["2","*4 (area quadruples)","16","8"],"L ∝ R²."),
     ("The inverse-square law for flux means that at twice the distance, you observe:",["Same brightness","Half the brightness","*1/4 the brightness","1/8 the brightness"],"F ∝ 1/d²."),
     ("Wien's law gives the peak wavelength of a blackbody at 5,800 K as:",["100 nm","*~500 nm (visible light, green-yellow)","1,000 nm","10 nm"],"λ_max = 2.898×10⁶/5800 ≈ 500 nm."),
     ("A star with a surface temperature of 10,000 K would peak at:",["500 nm","*~290 nm (ultraviolet)","1,000 nm","5,000 nm"],"Hotter = shorter wavelength."),
     ("A cool red star (~3,000 K) peaks at approximately:",["300 nm","500 nm","*~970 nm (near-infrared)","5,000 nm"],"2.898×10⁶/3000 ≈ 966 nm."),
     ("σ (Stefan-Boltzmann constant) equals:",["1.0","*5.67 × 10⁻⁸ W m⁻² K⁻⁴","6.67 × 10⁻¹¹","3 × 10⁸"],"Radiation constant."),
     ("The Sun's surface temperature (~5,800 K) and radius (~6.96 × 10⁸ m) give luminosity:",["1 W","*~3.8 × 10²⁶ W (using L = 4πR²σT⁴)","1 × 10¹⁰ W","1 × 10⁵⁰ W"],"Plug in values."),
     ("Solar flux at Earth's distance (1 AU ≈ 1.5 × 10¹¹ m) is:",["100 W/m²","*~1,361 W/m² (solar constant)","10,000 W/m²","1 W/m²"],"F = L/(4πd²)."),
     ("A star with 4× the Sun's luminosity but same distance would appear _____ times brighter.",["2","*4","16","1"],"F = L/(4πd²); proportional to L."),
     ("To use the Stefan-Boltzmann law for AP problems, students need:",["Only luminosity","*Temperature AND radius (or any two of L, R, T to solve for the third)","Only mass","Only distance"],"Two knowns → solve for the third."),
     ("A blackbody is:",["A dark star","*An idealized object that absorbs all radiation and emits a continuous spectrum depending only on temperature","A cold rock","An actual black object"],"Stars approximate blackbodies."),
     ("The total energy released by the Sun per year (L × time) is:",["Small","*~1.2 × 10³⁴ J (3.8×10²⁶ W × 3.15×10⁷ s)","Infinite","Unknown"],"Enormous energy output."),
     ("Comparing two stars: Star A (T=6000K, R=2R☉) vs Star B (T=3000K, R=8R☉). Which is more luminous?",["Star A","*Star B (L = 4πR²σT⁴: A has 4×(6000)⁴ factor=4×1; B has 64×(3000)⁴=64×(1/16)=4; they're equal!)","Same luminosity","Cannot determine"],"A: 4×1296×10¹² and B: 64×81×10¹² — actually A=4×6⁴=5184 units, B=64×3⁴=5184 units. Equal!"),
     ("For AP exams, energy calculations require practice with:",["Only memorization","*Substituting values into equations, converting units, and interpreting results","Only words","Only graphs"],"Quantitative problem-solving essential."),
     ("The luminosity-distance relationship allows astronomers to:",["Only observe stars","*Determine distances to stars (standard candles) if luminosity is known","Only name stars","Only classify stars"],"Distance modulus."),
     ("Photometry measures a star's:",["Mass","*Apparent brightness (flux) through filters at different wavelengths","Temperature directly","Velocity"],"Observational technique."),
     ("Mastering these energy calculations prepares students for:",["Nothing","*AP exam problems on stellar properties, distances, and the physics of radiation","Only physics class","Only solar study"],"Core quantitative skills.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 4: wrote {len(lessons)} lessons")
