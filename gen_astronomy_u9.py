#!/usr/bin/env python3
"""Astronomy Unit 9 – Telescopes & Technology (7 lessons)."""
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

# 9.1
k,v = build_lesson(9,1,"Ground-Based Telescopes",
    "<h3>Ground-Based Telescopes</h3>"
    "<h4>Types</h4>"
    "<ul><li><b>Refracting:</b> Lenses focus light; limited by chromatic aberration and lens size.</li>"
    "<li><b>Reflecting:</b> Mirrors focus light; most modern large telescopes (Keck 10 m, VLT 8.2 m, ELT 39 m under construction).</li></ul>"
    "<h4>Challenges &amp; Solutions</h4>"
    "<ul><li><b>Atmospheric turbulence:</b> Blurs images; mitigated by adaptive optics (deformable mirror corrects in real time).</li>"
    "<li><b>Light pollution:</b> Sites chosen at high altitude, remote, dry locations (Mauna Kea, Atacama Desert).</li>"
    "<li><b>Resolution:</b> Proportional to aperture; larger mirror = finer detail. Interferometry combines multiple telescopes.</li></ul>",
    [("Reflecting Telescope","Uses mirrors to focus light; all major modern telescopes are reflectors (no chromatic aberration, scalable)."),
     ("Adaptive Optics","Technology using deformable mirrors to correct atmospheric distortion in real time; achieves near-space quality."),
     ("Aperture","Diameter of a telescope's primary mirror or lens; larger aperture = more light and resolution."),
     ("Interferometry","Combining signals from multiple telescopes to achieve the resolution of a much larger telescope."),
     ("ELT","Extremely Large Telescope (ESO); 39 m primary mirror; under construction in Chile's Atacama Desert.")],
    [("Most modern large telescopes use _____ to focus light.",["Lenses","*Mirrors (reflecting telescopes — no chromatic aberration, easier to make large)","Prisms","Filters"],"Reflectors dominate."),
     ("Chromatic aberration is a problem specific to:",["Reflecting telescopes","*Refracting telescopes (lenses bend different wavelengths differently, causing color fringes)","Radio telescopes","All telescopes equally"],"Lens limitation."),
     ("The Keck telescopes on Mauna Kea have primary mirrors of:",["1 m","*10 m each (segmented mirror design)","50 m","100 m"],"Among the largest operational."),
     ("Adaptive optics corrects:",["Mirror shape permanently","*Real-time atmospheric distortion using a deformable mirror guided by a reference star or laser","Light pollution","Lens color",""],"Near-space image quality."),
     ("A laser guide star is:",["A natural star","*An artificial reference point created by a laser in the upper atmosphere for adaptive optics calibration","A navigation tool","A decoration"],"Enables AO anywhere."),
     ("Observatory sites are chosen for:",["City access","*High altitude, dry climate, dark skies, and stable atmosphere (e.g., Mauna Kea, Atacama)","Flat terrain","Warmth"],"Optimal conditions."),
     ("The ELT (Extremely Large Telescope) will have a primary mirror of:",["10 m","*~39 m (made of 798 hexagonal segments)","100 m","5 m"],"Largest optical telescope."),
     ("Telescope resolution is primarily determined by:",["Color","*Aperture (diameter of the primary mirror) — larger = finer detail at a given wavelength","Weight","Age"],"Diffraction limit."),
     ("Interferometry achieves:",["Nothing special","*The resolution of a telescope as large as the distance between the individual telescopes","Only speed","Only brightness"],"Virtual giant telescope."),
     ("The Very Large Telescope Interferometer (VLTI) combines:",["2 telescopes","*4 × 8.2 m telescopes (plus auxiliary telescopes) in Chile","10 telescopes","100 telescopes"],"Baselines up to ~200 m."),
     ("Light-gathering power scales with:",["Aperture linearly","*Aperture squared (area of the mirror; doubling diameter = 4× light gathered)","Weight","Focal length only"],"Area = π(D/2)²."),
     ("Segmented mirrors (like Keck) solve the problem of:",["Cost only","*Manufacturing and supporting a single very large monolithic mirror — segments are individually controlled","Weight only","Color"],"Practical large apertures."),
     ("The Giant Magellan Telescope (GMT) uses:",["One mirror","*7 × 8.4 m circular mirrors arranged like a flower (25.4 m effective aperture)","Lenses only","Radio dishes"],"Different approach from ELT."),
     ("The Thirty Meter Telescope (TMT) will have:",["10 m","*30 m primary mirror (492 hexagonal segments)","50 m","100 m"],"Proposed for Mauna Kea."),
     ("Ground-based telescopes are limited primarily by:",["Cost","Power","*Earth's atmosphere (turbulence, absorption of certain wavelengths, scattering)","Gravity"],"Why space telescopes also needed."),
     ("Atmospheric seeing is typically measured in:",["Meters","*Arcseconds (smaller = better; typical ~1 arcsec, excellent <0.5 arcsec)","Degrees","Kilometers"],"Angular measure of blur."),
     ("Spectroscopy with ground telescopes reveals:",["Nothing","*Chemical composition, temperature, velocity, and other properties of astronomical objects","Only color","Only brightness"],"Breaking light into spectrum."),
     ("Multi-object spectrographs can observe:",["1 object at a time","*Hundreds to thousands of objects simultaneously (e.g., DESI)","Only the Moon","Only stars"],"Very efficient surveys."),
     ("The future of ground-based astronomy includes:",["Decline","*ELT, GMT, TMT — extremely large telescopes with advanced AO pushing boundaries","Only space telescopes","No changes"],"Complementary to space."),
     ("Ground-based and space-based telescopes are:",["Competitors","*Complementary — each has strengths (ground: size, upgradeability; space: no atmosphere, all wavelengths)","Identical","Unrelated"],"Both essential.")]
)
lessons[k]=v

# 9.2
k,v = build_lesson(9,2,"Space Telescopes (Hubble & JWST)",
    "<h3>Space Telescopes</h3>"
    "<h4>Hubble Space Telescope</h4>"
    "<p>Launched 1990; 2.4 m mirror; UV/visible/near-IR. Revolutionized astronomy: deep fields, dark energy (accelerating expansion), exoplanet atmospheres, nebula imaging. Serviced 5 times by shuttle crews.</p>"
    "<h4>James Webb Space Telescope</h4>"
    "<p>Launched Dec 25, 2021; 6.5 m gold-coated beryllium mirror; infrared. At L2 (1.5 million km). Seeing the earliest galaxies, exoplanet atmospheres, star formation inside dust clouds. 5-layer sunshield keeps instruments at ~40 K.</p>",
    [("Hubble Space Telescope","NASA/ESA; 2.4 m; UV/vis/near-IR; launched 1990; revolutionized astronomy; serviced 5× by shuttle."),
     ("JWST","James Webb Space Telescope; 6.5 m infrared; at L2; launched 2021; studying earliest galaxies and exoplanets."),
     ("L2 Lagrange Point","Sun-Earth gravitational balance point ~1.5 million km from Earth; JWST's orbit location."),
     ("Hubble Deep Field","Image of a tiny sky patch revealing thousands of galaxies — showed the universe is filled with galaxies."),
     ("Gold-Coated Mirrors","JWST's beryllium mirrors coated with thin gold layer — optimized for reflecting infrared light.")],
    [("Hubble was launched in:",["1980","*1990","2000","2010"],"Over 30 years of operation."),
     ("Hubble's primary mirror is _____ in diameter.",["6.5 m","*2.4 m","10 m","1 m"],"Smaller than JWST."),
     ("Hubble primarily observes in:",["Only X-ray","*UV, visible, and near-infrared wavelengths","Only radio","Only gamma-ray"],"Broad wavelength range."),
     ("Hubble was serviced _____ times by Space Shuttle crews.",["0","3","*5 (SM1 through SM4 in 1993–2009)","10"],"Unique advantage of LEO."),
     ("The initial Hubble mirror flaw was corrected by:",["Replacing the mirror","*Installing corrective optics (COSTAR) during Servicing Mission 1 in 1993","Ignoring it","Refocusing"],"Spherical aberration fix."),
     ("JWST was launched on:",["July 4, 2020","*December 25, 2021","January 1, 2022","March 15, 2020"],"Christmas Day 2021."),
     ("JWST's primary mirror is _____ in diameter.",["2.4 m","*~6.5 m (18 hexagonal gold-coated beryllium segments)","10 m","1 m"],"Largest space telescope."),
     ("JWST primarily observes in:",["UV","Visible","X-ray","*Infrared (to see through dust and detect highly redshifted light)"],"Optimized for IR."),
     ("JWST orbits at:",["LEO","GEO","The Moon","*Sun-Earth L2 Lagrange point (~1.5 million km from Earth)"],"Thermally stable."),
     ("JWST cannot be serviced like Hubble because:",["It doesn't need service","*It's 1.5 million km from Earth (L2) — far too distant for current crewed missions","It's too old","NASA decided not to"],"Designed for unserviced operation."),
     ("JWST's sunshield keeps instruments at approximately:",["Room temperature","*~40 K (-233°C)","0°C","Absolute zero"],"Essential for IR detection."),
     ("The Hubble Deep Field revealed:",["One galaxy","*Thousands of galaxies in a tiny patch of seemingly empty sky — the universe is filled with galaxies","No galaxies","Only stars"],"Paradigm-shifting image."),
     ("JWST has observed galaxies from when the universe was only _____ old.",["1 billion years","*~300–400 million years after the Big Bang","5 billion years","Just formed"],"Earliest galaxies ever seen."),
     ("Hubble helped prove that the universe's expansion is:",["Slowing down","Constant","*Accelerating (led to dark energy discovery — Nobel Prize 2011)","Stopping"],"Type Ia supernovae studies."),
     ("JWST's transit spectroscopy has detected _____ in exoplanet atmospheres.",["Nothing","*Water vapor, CO₂, SO₂, and other molecules","Only helium","Only hydrogen"],"Atmospheric characterization."),
     ("Hubble's observations of Cepheid variables helped refine:",["Planet sizes","*The Hubble constant (rate of universe expansion) and cosmic distance ladder","Star temperatures","Moon distance"],"Distance measurements."),
     ("The Chandra X-ray Observatory observes:",["Infrared","Visible","*X-rays (from supernova remnants, black hole accretion, galaxy clusters)","Radio"],"Complementary to Hubble/JWST."),
     ("The Spitzer Space Telescope observed in:",["UV","X-ray","*Infrared (JWST's predecessor for IR astronomy; 2003–2020)","Visible"],"Retired 2020."),
     ("Future space telescopes being planned include:",["None","*Nancy Grace Roman (wide-field IR), HWO/LUVOIR concept (direct exoplanet imaging)","Only Hubble replacements","Only radio"],"Next generation."),
     ("Space telescopes are essential because:",["They're expensive","*Earth's atmosphere blocks many wavelengths and distorts light — space provides clear, unobstructed views","They're fashionable","Ground telescopes don't work"],"Complementary to ground.")]
)
lessons[k]=v

# 9.3
k,v = build_lesson(9,3,"Radio Astronomy",
    "<h3>Radio Astronomy</h3>"
    "<p>Observing the universe in radio wavelengths (mm to meters). Radio waves pass through dust and atmosphere, revealing hidden structures.</p>"
    "<h4>Key Instruments</h4>"
    "<ul><li><b>Single dishes:</b> Arecibo (collapsed 2020; 305 m), FAST (China; 500 m), Green Bank (100 m).</li>"
    "<li><b>Interferometers:</b> VLA (27 antennas, New Mexico), ALMA (66 dishes, Chile; mm/submm), SKA (under construction; thousands of antennas across Australia/South Africa).</li></ul>"
    "<p><b>Discoveries:</b> Pulsars, quasars, CMB, molecular clouds, fast radio bursts (FRBs).</p>",
    [("Radio Telescope","Telescope detecting radio-wavelength electromagnetic radiation; can observe through dust and clouds."),
     ("ALMA","Atacama Large Millimeter/submillimeter Array; 66 dishes in Chile; studies star/planet formation in dusty regions."),
     ("SKA","Square Kilometre Array; massive international radio telescope under construction; unprecedented sensitivity."),
     ("Pulsar","Rapidly rotating neutron star emitting beams of radio waves; discovered by Jocelyn Bell Burnell in 1967."),
     ("Fast Radio Burst (FRB)","Brief, intense burst of radio emission from distant sources; origin still being studied (magnetars suspected).")],
    [("Radio astronomy observes the universe in:",["Visible light","*Radio wavelengths (millimeters to meters)","X-rays","Gamma rays"],"Long-wavelength EM radiation."),
     ("Radio waves are useful for astronomy because:",["They're loud","*They penetrate dust and gas, revealing structures hidden at optical wavelengths, and pass through Earth's atmosphere","They're colorful","They bounce off stars"],"See through dust."),
     ("The largest single-dish radio telescope is:",["Arecibo","*FAST (Five-hundred-meter Aperture Spherical Telescope, China; 500 m)","Green Bank","A VLA antenna"],"World's largest."),
     ("Arecibo Observatory (305 m, Puerto Rico) collapsed in:",["2010","*2020 (cable failures caused the receiver to crash into the dish)","2000","Never"],"Major loss to science."),
     ("ALMA observes at _____ wavelengths.",["Optical","Radio (long wavelength)","X-ray","*Millimeter and submillimeter (between infrared and radio)"],"Cool dust and molecules."),
     ("Radio interferometry combines multiple antennas to achieve:",["More brightness","*The angular resolution of a telescope as large as the maximum baseline distance between antennas","More color","Louder signals"],"Virtual giant dish."),
     ("The VLA (Very Large Array) consists of:",["1 antenna","*27 antennas in a Y-shaped configuration in New Mexico","100 antennas","3 antennas"],"Iconic radio observatory."),
     ("Very Long Baseline Interferometry (VLBI) can achieve baselines of:",["1 km","100 km","*Earth-diameter or larger (using antennas worldwide or in space)","1 m"],"Highest angular resolution."),
     ("The Event Horizon Telescope (EHT) used VLBI to image:",["A planet","*The shadow of supermassive black holes (M87* in 2019, Sgr A* in 2022)","A star","The Moon"],"Earth-sized virtual telescope."),
     ("Pulsars were discovered by:",["Einstein","*Jocelyn Bell Burnell in 1967 (initially called 'LGM-1' for 'Little Green Men')","Hubble","Newton"],"Rotating neutron stars."),
     ("The Cosmic Microwave Background (CMB) was accidentally discovered in radio by:",["Hubble","*Arno Penzias and Robert Wilson (1965; Bell Labs)","Galileo","SETI"],"Confirmed Big Bang theory."),
     ("Fast Radio Bursts (FRBs) are:",["Slow signals","*Brief (millisecond) intense bursts of radio emission from extragalactic sources","Earth-based signals","Predictable"],"Mysterious phenomenon."),
     ("Radio astronomy has revealed _____ in molecular clouds.",["Nothing","*Complex organic molecules (amino acid precursors, alcohols, sugars) — chemistry of interstellar space","Only hydrogen","Only helium"],"Astrochemistry."),
     ("The 21 cm hydrogen line (1420 MHz) is important because:",["It's red","*Neutral hydrogen is the most abundant element; its emission maps the structure of the Milky Way and other galaxies","It's blue","It's hot"],"Fundamental radio spectral line."),
     ("The SKA (Square Kilometre Array) will be:",["Small","*The world's largest radio telescope — thousands of antennas across Australia and South Africa","One dish","Only in Europe"],"Transformative sensitivity."),
     ("Radio galaxies and quasars emit enormous energy at radio wavelengths from:",["Nuclear fusion in the star","*Supermassive black holes launching relativistic jets of material","Chemical reactions","Collisions"],"Active galactic nuclei."),
     ("Advantages of radio telescopes over optical include:",["Better color","*Observing through dust/clouds, day and night operation, and detecting non-thermal processes","Sharper images always","None"],"Complementary capabilities."),
     ("Limitations of single-dish radio telescopes include:",["No limitations","*Poor angular resolution at long wavelengths (resolution ∝ wavelength/diameter) — need huge dishes or interferometry","Only see near objects","Cost only"],"Diffraction limit."),
     ("Citizen science project SETI@home used:",["Professional telescopes","*Volunteer computers to analyze radio data from Arecibo for potential extraterrestrial signals","Only universities","Only governments"],"Distributed computing."),
     ("Radio astronomy demonstrates that:",["Only visible light matters","*The universe looks completely different at different wavelengths; radio reveals unique physics and chemistry","Radio is unimportant","Only one wavelength matters"],"Multi-wavelength astronomy.")]
)
lessons[k]=v

# 9.4
k,v = build_lesson(9,4,"Spectroscopy in Astronomy",
    "<h3>Spectroscopy in Astronomy</h3>"
    "<p>Analyzing light by wavelength to determine composition, temperature, velocity, and more.</p>"
    "<h4>Types of Spectra</h4>"
    "<ul><li><b>Continuous:</b> Hot, dense object (blackbody radiation).</li>"
    "<li><b>Emission:</b> Hot, low-density gas → bright lines at specific wavelengths.</li>"
    "<li><b>Absorption:</b> Cool gas between source and observer absorbs specific wavelengths → dark lines.</li></ul>"
    "<h4>Applications</h4>"
    "<p>Stellar composition, radial velocity (Doppler shift), exoplanet atmospheres, cosmic expansion (redshift), chemical abundances.</p>",
    [("Spectroscopy","Analysis of electromagnetic radiation by wavelength; reveals composition, temperature, density, motion."),
     ("Absorption Lines","Dark lines in a spectrum where specific wavelengths are absorbed by cooler gas; identify elements."),
     ("Emission Lines","Bright lines in a spectrum at specific wavelengths emitted by hot gas; identify elements and temperature."),
     ("Doppler Shift","Change in wavelength due to relative motion; blueshift = approaching, redshift = receding."),
     ("Blackbody Radiation","Continuous spectrum emitted by a hot, dense object; peak wavelength depends on temperature (Wien's law).")],
    [("Spectroscopy reveals an object's:",["Color only","*Chemical composition, temperature, density, velocity, and magnetic field","Shape","Size only"],"Incredibly powerful tool."),
     ("Absorption lines are produced when:",["Hot gas emits light","*Cooler gas absorbs specific wavelengths from a continuous background source","Stars explode","Nothing absorbs"],"Kirchhoff's laws."),
     ("Emission lines are produced when:",["Cool gas absorbs light","*Hot, low-density gas emits light at specific wavelengths characteristic of its elements","Gravity acts","Nothing emits"],"Kirchhoff's laws."),
     ("Each element produces a unique pattern of spectral lines because:",["All elements are the same","*Each element has a unique electron configuration → unique energy level transitions","Only hydrogen has lines","Lines are random"],"Spectral fingerprint."),
     ("Helium was first discovered in:",["A laboratory","*The Sun's spectrum (1868, solar eclipse — before being found on Earth)","Space","The Moon"],"Named after Helios (Sun)."),
     ("Doppler blueshift indicates:",["Object is receding","*Object is approaching (wavelengths compressed → shorter/bluer)","Object is stationary","Object is spinning"],"Shorter wavelength = moving toward."),
     ("Doppler redshift indicates:",["Object is approaching","*Object is receding (wavelengths stretched → longer/redder)","Object is stationary","Object is hot"],"Longer wavelength = moving away."),
     ("Wien's displacement law states that the peak wavelength of a blackbody:",["Is constant","*Is inversely proportional to temperature (hotter = shorter peak wavelength)","Depends on size","Is always blue"],"λ_max = b/T."),
     ("A star's surface temperature can be determined from:",["Its name","*Its spectrum — the peak wavelength (Wien's law) or spectral line ratios","Its distance","Its mass directly"],"Color ↔ temperature."),
     ("Stellar classification (OBAFGKM) is based on:",["Size","*Spectral characteristics (temperature): O (hottest, ~30,000+ K) to M (coolest, ~3,000 K)","Distance","Age"],"Oh Be A Fine Girl/Guy Kiss Me."),
     ("Spectrographs in modern telescopes can achieve:",["Low precision","*Extremely high spectral resolution — detecting exoplanet-induced stellar wobble of ~1 m/s","Only visible light","No useful data"],"Radial velocity method."),
     ("Cosmological redshift is caused by:",["Object motion only","*The expansion of space itself stretching light wavelengths as it travels across the expanding universe","Gravity only","Nothing"],"Different from Doppler."),
     ("Quasar spectra showed high redshifts, indicating they are:",["Nearby","*Very distant and luminous — among the most distant observable objects","In our solar system","On Earth"],"Discovery of extreme distances."),
     ("Spectral line broadening can indicate:",["Nothing","*Temperature (thermal broadening), rotation, magnetic fields (Zeeman effect), and pressure","Only color","Only distance"],"Multiple physical effects."),
     ("Transit spectroscopy of exoplanets works by:",["Landing on the planet","*Comparing the star's spectrum during transit (planet in front) vs. out of transit — differences reveal the planet's atmosphere","Using radar","Taking photos"],"JWST excels here."),
     ("The Zeeman effect splits spectral lines in the presence of:",["High temperature","*Strong magnetic fields","High pressure","Low density"],"Magnetic field measurement."),
     ("Spectral analysis of interstellar gas reveals:",["Nothing","*Molecular composition (e.g., H₂, CO, H₂O, complex organics) via their rotational/vibrational line spectra","Only dust","Only temperature"],"Astrochemistry."),
     ("The hydrogen Balmer series (visible lines Hα, Hβ, etc.) is important because:",["It's rare","*Hydrogen is the most abundant element; its spectral lines are used throughout astronomy for classification and measurement","It's undetectable","Only in labs"],"Fundamental spectral series."),
     ("Spectroscopy is often called the most important tool in astronomy because:",["It's old","Telescopes are better","*It extracts more physical information from light than any other technique","It's cheap"],"Light as information carrier."),
     ("AP-level spectroscopy problems involve applying:",["Nothing","*Wien's law, Doppler formula (Δλ/λ = v/c), and Kirchhoff's laws to determine physical properties from spectra","Only memorization","Only history"],"Quantitative analysis.")]
)
lessons[k]=v

# 9.5
k,v = build_lesson(9,5,"Computer Modeling in Astronomy",
    "<h3>Computer Modeling in Astronomy</h3>"
    "<p>Simulating complex astronomical phenomena that can't be replicated in labs:</p>"
    "<ul><li><b>N-body simulations:</b> Gravitational interactions of millions/billions of particles (galaxy formation, star clusters).</li>"
    "<li><b>Hydrodynamic codes:</b> Gas dynamics in stellar interiors, accretion disks, supernovae.</li>"
    "<li><b>Climate models:</b> Exoplanet atmospheric modeling (GCMs — General Circulation Models).</li>"
    "<li><b>Machine learning:</b> Classifying galaxies, detecting transients, reducing data from surveys.</li></ul>"
    "<p>Supercomputers process petabytes of data from telescopes like LSST (Vera C. Rubin Observatory).</p>",
    [("N-body Simulation","Computational model tracking gravitational interactions of millions to billions of particles."),
     ("Hydrodynamic Simulation","Modeling fluid dynamics (gas and plasma) in astrophysical objects like stars and accretion disks."),
     ("Machine Learning in Astronomy","AI algorithms classifying galaxies, detecting exoplanet transits, identifying transient events in massive datasets."),
     ("Vera C. Rubin Observatory","Upcoming survey telescope (LSST); will image the entire visible sky every few nights; massive data output."),
     ("Supercomputer","High-performance computing system essential for running large-scale astrophysical simulations.")],
    [("N-body simulations model:",["Chemical reactions","*Gravitational interactions between millions or billions of particles (e.g., galaxy mergers, dark matter structure)","Only 2 bodies","Sound waves"],"Gravity at scale."),
     ("Galaxy formation simulations like IllustrisTNG model:",["Only stars","*Stars, gas, dark matter, black holes, magnetic fields, and feedback processes over cosmic time","Only gravity","Only light"],"Comprehensive models."),
     ("Hydrodynamic codes are needed to model:",["Solid objects","*Gas and plasma dynamics (stellar interiors, accretion disks, supernova explosions)","Only gravity","Only radiative transfer"],"Fluid dynamics in space."),
     ("Machine learning helps astronomers by:",["Replacing telescopes","*Classifying millions of galaxies, detecting weak signals, and finding anomalies in massive datasets","Only making images","Nothing useful"],"AI-assisted discovery."),
     ("The Vera C. Rubin Observatory (LSST) will produce _____ of data per night.",["Kilobytes","Megabytes","*~20 terabytes (imaging the entire visible sky every few nights)","Petabytes per second"],"Enormous data volume."),
     ("Supercomputers are essential for astronomy because:",["They're fast","*Astrophysical simulations require trillions of calculations; no standard computer can handle them","They're expensive","Only for movies"],"Computational necessity."),
     ("General Circulation Models (GCMs) applied to exoplanets simulate:",["Only Earth weather","*Atmospheric dynamics, climate, and potential surface conditions on exoplanets","Only temperature","Nothing"],"Predicting alien climates."),
     ("Monte Carlo methods in astronomy use:",["Precise calculations","*Random sampling to solve complex statistical and radiative transfer problems","Only dice","Only observation"],"Statistical simulations."),
     ("Dark matter distribution is studied through simulations like the Millennium Simulation, which modeled:",["1 million particles","*~10 billion particles tracing dark matter structure formation over cosmic time","Only 100 particles","Only nearby galaxies"],"Cosmic web structure."),
     ("Data pipelines in modern astronomy:",["Are unnecessary","*Automatically process raw telescope data into calibrated, science-ready products","Only store data","Only delete data"],"Essential infrastructure."),
     ("Citizen science projects like Galaxy Zoo leverage:",["Only AI","*Human pattern recognition — volunteers classify galaxy morphologies from survey images","Only professionals","Only computers"],"Crowdsourced astronomy."),
     ("Simulations of stellar evolution model:",["Only birth","*The entire life cycle from gas cloud collapse to main sequence, giant branch, and remnant (white dwarf, neutron star, black hole)","Only death","Only the main sequence"],"Star life tracks."),
     ("Predictive modeling of asteroid orbits is critical for:",["Fun","*Planetary defense — identifying potentially hazardous objects (PHOs) years to decades in advance","Only cataloging","Only historical records"],"Impact risk assessment."),
     ("The Square Kilometre Array (SKA) will require _____ processing capabilities.",["Normal PC","*Exascale computing (among the largest data processing challenges in any scientific field)","Minimal","Calculators"],"Data processing frontier."),
     ("Weather forecasting techniques have been adapted for:",["Nothing astronomical","*Exoplanet atmospheric modeling and space weather prediction","Only Earth","Only Mars"],"Cross-disciplinary applications."),
     ("GPU computing has accelerated astronomical simulations because:",["GPUs are cheap","*GPUs excel at parallel processing — running millions of simple calculations simultaneously","GPUs are new","GPUs are colorful"],"Massive parallelism."),
     ("Gravitational wave detection relies on computational methods to:",["Create waves","*Filter extremely faint signals from noise in detector data (matched filtering)","Replace detectors","Only visualize"],"Signal processing."),
     ("Virtual observatories provide:",["Physical access to telescopes","*Online access to archived astronomical data from multiple missions — enabling research without telescope time","Only images","Only weather data"],"Data accessibility."),
     ("Computer modeling in astronomy is crucial because:",["It replaces observation","*Many phenomena occur over timescales (millions of years) or scales (galaxy clusters) impossible to observe directly","It's cheap","Only for entertainment"],"Bridge theory and observation."),
     ("The interplay between simulation and observation means:",["They're unrelated","*Models make testable predictions; observations verify or refute them — iterative scientific process","Only observation matters","Only simulation matters"],"Scientific method.")]
)
lessons[k]=v

# 9.6
k,v = build_lesson(9,6,"Case Studies: Modern Astronomical Discoveries",
    "<h3>Case Studies: Modern Astronomical Discoveries</h3>"
    "<h4>Gravitational Waves (LIGO, 2015)</h4>"
    "<p>First direct detection of gravitational waves from merging black holes (September 14, 2015). Subsequently detected neutron star mergers (GW170817 — with electromagnetic counterpart; multi-messenger astronomy).</p>"
    "<h4>Black Hole Imaging (EHT, 2019)</h4>"
    "<p>First image of a black hole shadow (M87*). 2022: Sgr A* (Milky Way center). Earth-sized virtual telescope using VLBI.</p>"
    "<h4>Exoplanet Revolution</h4>"
    "<p>Kepler → TESS → JWST: from thousands of discoveries to atmospheric characterization.</p>",
    [("LIGO","Laser Interferometer Gravitational-Wave Observatory; first detected gravitational waves on Sept 14, 2015."),
     ("GW170817","First gravitational wave detection from a neutron star merger (2017); observed in light too — multi-messenger astronomy."),
     ("Event Horizon Telescope","Earth-sized virtual radio telescope using VLBI; imaged M87* (2019) and Sgr A* (2022) black holes."),
     ("Multi-Messenger Astronomy","Combining gravitational waves, electromagnetic radiation, and neutrinos to study a single event."),
     ("Exoplanet Revolution","Kepler/TESS/JWST have transformed exoplanet science from detection to atmospheric characterization.")],
    [("LIGO first detected gravitational waves on:",["January 1, 2000","*September 14, 2015 (from merging black holes ~1.3 billion light-years away)","July 4, 2012","March 15, 2018"],"Nobel Prize 2017."),
     ("Gravitational waves are:",["Sound waves","*Ripples in spacetime produced by accelerating massive objects (predicted by Einstein in 1916)","Light waves","Radio waves"],"Einstein's prediction confirmed."),
     ("LIGO detects gravitational waves by measuring:",["Temperature changes","*Tiny changes in the length of 4 km laser arms (smaller than a proton's width)","Sound","Magnetic fields"],"Incredibly sensitive."),
     ("GW170817 was significant because it was the first:",["Black hole merger detected","*Neutron star merger detected in both gravitational waves AND electromagnetic radiation (multi-messenger)","Supernova detected","Planet detected"],"Multi-messenger astronomy born."),
     ("The Event Horizon Telescope imaged M87* by:",["Launching a space telescope","*Combining radio telescopes worldwide (VLBI) to create an Earth-sized virtual dish","Taking a photograph","Using Hubble"],"Powerful interferometry."),
     ("The M87* image showed:",["A star","*The shadow of a supermassive black hole (6.5 billion solar masses) surrounded by a bright accretion ring","A planet","A galaxy"],"First black hole image."),
     ("Sgr A* is:",["A star in Sagittarius","*The 4-million-solar-mass supermassive black hole at the center of our Milky Way (imaged by EHT in 2022)","A satellite","A nebula"],"Our galaxy's central black hole."),
     ("Multi-messenger astronomy combines:",["Only light","*Gravitational waves, electromagnetic radiation (all bands), and potentially neutrinos from the same event","Only sound","Only gravity"],"Multiple information channels."),
     ("The Kepler Space Telescope's greatest legacy was:",["Finding 10 planets","*Demonstrating that planets are ubiquitous — discovering thousands and showing that almost every star has planets","Finding aliens","Mapping the Moon"],"Statistical revolution."),
     ("TESS expanded exoplanet detection by focusing on:",["Distant stars","*Nearby, bright stars (easier for follow-up atmospheric characterization with JWST)","Only the Moon","Only our solar system"],"Complementary to Kepler."),
     ("JWST's atmospheric studies have shown that exoplanet atmospheres:",["Are all the same","*Are remarkably diverse — some with unexpected chemical compositions challenging formation models","Don't exist","Only contain hydrogen"],"Surprising diversity."),
     ("The detection of element formation in neutron star mergers (GW170817) confirmed that:",["Only hydrogen forms in mergers","*Heavy elements (gold, platinum, rare earths) are produced in neutron star mergers (r-process nucleosynthesis)","No elements form","Only iron forms"],"Origin of heavy elements."),
     ("Dark energy was discovered through observations of:",["Radio galaxies","*Type Ia supernovae appearing fainter than expected — indicating the universe's expansion is accelerating","Stars","Planets"],"Nobel Prize 2011."),
     ("The detection of the Higgs boson (2012) relates to astronomy because:",["It doesn't","*The Higgs field gives particles mass — fundamental to understanding the matter that forms stars, planets, and us","Only particle physics","Only chemistry"],"Connecting fundamental physics."),
     ("Fast Radio Bursts (FRBs) are a modern mystery because:",["They're not detected","*Their brief, intense, and mostly non-repeating nature makes identifying their sources challenging","They're boring","They're well-understood"],"Active research area."),
     ("The discovery of phosphine in Venus's atmosphere (2020) sparked debate about:",["Geology only","*Possible biological origin — on Earth, phosphine is associated with microbial life","Chemistry only","Nothing"],"Controversial finding."),
     ("These case studies share the common theme that:",["Technology doesn't matter","*Technological advances (detectors, telescopes, computing) enable fundamental new discoveries","Only one field matters","Discoveries are random"],"Technology drives discovery."),
     ("International collaboration was essential for:",["Only LIGO","*All these discoveries — LIGO (US/Italy), EHT (global), JWST (NASA/ESA/CSA), Kepler/TESS (global science teams)","Only EHT","None"],"Science is global."),
     ("The pace of astronomical discovery is:",["Slowing","*Accelerating — driven by new instruments, computing power, and multi-wavelength/multi-messenger approaches","Stopping","Constant"],"Golden age."),
     ("Understanding these case studies prepares students for AP exams by:",["Nothing","*Connecting physics principles (gravity, EM radiation, relativity) to real cutting-edge discoveries","Only memorization","Only history"],"Applied physics.")]
)
lessons[k]=v

# 9.7
k,v = build_lesson(9,7,"AP Prep: Data Analysis in Astronomy",
    "<h3>AP Prep: Data Analysis in Astronomy</h3>"
    "<h4>Key Skills</h4>"
    "<ul><li><b>Light curves:</b> Brightness vs. time → transits (dip depth ∝ planet/star area ratio), eclipsing binaries, variable stars.</li>"
    "<li><b>Spectra:</b> Identify elements (absorption/emission lines), measure radial velocity (Δλ/λ = v/c), determine redshift/distance.</li>"
    "<li><b>HR Diagram:</b> Plot luminosity vs. temperature; identify stellar types, evolutionary stages.</li>"
    "<li><b>Error analysis:</b> Uncertainty propagation, significant figures, standard deviation, systematic vs. random errors.</li></ul>",
    [("Light Curve","Graph of brightness vs. time; used to detect transits, eclipses, and stellar variability."),
     ("Transit Depth","Fractional decrease in star brightness during planet transit; depth = (R_planet/R_star)²."),
     ("Radial Velocity Formula","Δλ/λ = v/c; Doppler shift reveals how fast an object moves toward or away from the observer."),
     ("Error Analysis","Assessment of measurement uncertainties; includes random error (precision) and systematic error (accuracy)."),
     ("Hubble's Law","v = H₀ × d; recession velocity is proportional to distance; H₀ ≈ 70 km/s/Mpc.")],
    [("A transit light curve shows a planet's presence as:",["Brightening","*A periodic dip in the star's brightness when the planet passes in front","Color change","Disappearance"],"Dip depth = (R_p/R_*)²."),
     ("If a planet blocks 1% of a star's light, the planet's radius is approximately _____ of the star's radius.",["1%","*~10% (since depth = (R_p/R_*)², √0.01 = 0.1)","50%","0.1%"],"Square root relationship."),
     ("The Doppler formula Δλ/λ = v/c: if a star's Hα line (656.3 nm) is shifted to 656.5 nm, v =:",["0","*~91 km/s (Δλ=0.2 nm, v = c × 0.2/656.3 ≈ 91 km/s)","Speed of light","1 km/s"],"Apply the formula."),
     ("Blueshift in a star's spectrum indicates the star is:",["Receding","*Approaching the observer","Stationary","Rotating only"],"Compressed wavelengths."),
     ("On an HR Diagram, the main sequence runs from:",["Top-right to bottom-left","*Top-left (hot, luminous) to bottom-right (cool, dim)","Horizontal","Vertical"],"Main sequence band."),
     ("Red giants appear in the HR Diagram at:",["Bottom-left","*Top-right (luminous but cool)","Bottom-right","Center"],"Large, cool, bright."),
     ("White dwarfs appear in the HR Diagram at:",["Top-right","*Bottom-left (hot but dim — small)","Top-left","Center"],"Small, hot, faint."),
     ("Hubble's Law (v = H₀d) relates:", ["Star brightness to temperature","*Recession velocity to distance (farther galaxies recede faster)","Mass to luminosity","Radius to volume"],"Basis for cosmic distance measurement."),
     ("If H₀ = 70 km/s/Mpc and a galaxy has v = 7,000 km/s, its distance is:",["10 Mpc","*100 Mpc (d = v/H₀ = 7000/70 = 100 Mpc)","1,000 Mpc","1 Mpc"],"Apply Hubble's Law."),
     ("Parallax is used to measure distances to:",["Distant galaxies","*Nearby stars (up to ~1,000 parsecs with Gaia satellite precision)","Only the Moon","Only planets"],"Trigonometric method."),
     ("If a star has a parallax angle of 0.1 arcsec, its distance is:",["0.1 pc","1 pc","*10 pc (d = 1/p = 1/0.1 = 10 parsecs)","100 pc"],"d(pc) = 1/p(arcsec)."),
     ("Standard candles (like Type Ia supernovae) are useful because:",["They're beautiful","*They have known luminosity — comparing apparent vs. absolute brightness gives distance","They're common","They're nearby"],"Cosmic distance ladder."),
     ("Random errors can be reduced by:",["One measurement","*Repeated measurements and averaging (statistical methods)","Systematic errors","Guessing"],"Improves precision."),
     ("Systematic errors:",["Average out with more data","*Do not average out — they consistently bias measurements in one direction","Are random","Don't exist"],"Accuracy issue."),
     ("Signal-to-noise ratio (S/N) in astronomical data represents:",["Only signal","*The strength of the desired signal relative to background noise — higher = cleaner data","Only noise","Image quality only"],"Data quality measure."),
     ("Photometry measures:",["Spectrum","*The brightness (intensity) of an object in specific wavelength bands","Mass","Distance"],"Magnitude measurements."),
     ("The magnitude scale: a difference of 5 magnitudes = a brightness factor of:",["5","10","*100 (2.512⁵ ≈ 100)","1,000"],"Logarithmic scale."),
     ("Period-luminosity relationship (Leavitt law) for Cepheids:",["Has no use","*Relates pulsation period to absolute luminosity — longer period = more luminous","Is linear in all cases","Only applies to nearby stars"],"Distance indicator."),
     ("Color index (B-V) of a star indicates its:",["Size","Distance","*Surface temperature (bluer/negative B-V = hotter; redder/positive = cooler)","Age directly"],"Temperature proxy."),
     ("Mastering data analysis in astronomy is essential for AP prep because:",["It's not tested","*The AP exam requires interpreting graphs, applying formulas, and drawing conclusions from astronomical data","Only for PhDs","Only for research"],"Quantitative skills.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Astronomy Unit 9: wrote {len(lessons)} lessons")
