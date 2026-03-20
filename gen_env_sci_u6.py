#!/usr/bin/env python3
"""Environmental Science Unit 6 – Pollution (7 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "environmental_science_lessons.json")
COURSE = "Environmental Science"

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

# 6.1
k,v = build_lesson(6,1,"Air Pollution",
    "<h3>Air Pollution</h3>"
    "<h4>Primary Pollutants</h4>"
    "<p>Emitted directly: CO, SO₂, NOₓ, particulate matter (PM), volatile organic compounds (VOCs), lead.</p>"
    "<h4>Secondary Pollutants</h4>"
    "<p>Formed by chemical reactions in the atmosphere: ozone (O₃), smog, acid rain.</p>"
    "<h4>Key Issues</h4>"
    "<ul><li><b>Criteria pollutants:</b> 6 regulated by the Clean Air Act (CO, Pb, NO₂, O₃, PM, SO₂).</li>"
    "<li><b>Indoor air pollution:</b> Radon, VOCs, mold, CO — kills ~3.8 million/year globally (cooking with solid fuels).</li></ul>",
    [("Primary Pollutant","Pollutant emitted directly into the atmosphere (CO, SO₂, NOₓ, PM, VOCs, lead)."),
     ("Secondary Pollutant","Formed by chemical reactions of primary pollutants in the atmosphere (ozone, smog, acid deposition)."),
     ("Criteria Pollutants","Six pollutants regulated by the Clean Air Act: CO, Pb (lead), NO₂, O₃ (ozone), PM, SO₂."),
     ("Photochemical Smog","Brown haze formed when sunlight reacts with NOₓ and VOCs; worst in sunny cities with heavy traffic (LA)."),
     ("Thermal Inversion","Warm air layer traps cool air and pollutants near the ground, worsening air quality.")],
    [("Primary pollutants are:",["Formed in the atmosphere","*Emitted directly from a source (e.g., CO from cars, SO₂ from power plants)","Always natural","Only indoors"],"Direct emissions."),
     ("Secondary pollutants are:",["Emitted directly","*Formed by chemical reactions in the atmosphere (e.g., ground-level ozone from NOₓ + VOCs + sunlight)","Only natural","Only indoors"],"Atmospheric chemistry."),
     ("How many criteria pollutants are regulated by the Clean Air Act?",["3","10","*6 (CO, Pb, NO₂, O₃, PM, SO₂)","12"],"Key regulatory framework."),
     ("Photochemical smog forms from:",["Only SO₂","*NOₓ + VOCs + sunlight → ground-level ozone and other oxidants (brown haze)","Only CO₂","Only natural sources"],"Sunny city problem."),
     ("Ground-level ozone is considered _____ at ground level.",["Helpful","*Harmful (causes respiratory damage — it's the main component of photochemical smog)","Neutral","Identical to stratospheric ozone"],"Good up high, bad nearby."),
     ("Thermal inversions worsen air pollution by:",["Increasing wind","*Trapping pollutants near the ground under a warm air lid (preventing normal convective mixing)","Reducing temperature","Creating ozone"],"Atmospheric trapping."),
     ("Indoor air pollution kills approximately _____ people per year globally.",["100,000","1 million","*~3.8 million (mainly from cooking with solid fuels in developing countries)","10 million"],"Major health crisis."),
     ("Radon is a dangerous indoor pollutant because it:",["Has a strong odor","*Is a colorless, odorless radioactive gas that seeps from soil; 2nd leading cause of lung cancer after smoking","Only affects basements","Is always at safe levels"],"Silent killer."),
     ("SO₂ emissions primarily come from:",["Cars","*Coal-burning power plants and industrial processes","Agriculture","Forests"],"Fossil fuel combustion."),
     ("NOₓ emissions come primarily from:",["Agriculture","Forests","*Vehicle engines and power plants (formed at high combustion temperatures)","Oceans"],"Combustion at high temperature."),
     ("Acid deposition (acid rain) forms when:",["Ozone reacts","CO₂ dissolves","*SO₂ and NOₓ react with water vapor in the atmosphere to form H₂SO₄ and HNO₃","Methane reacts"],"Acidic precipitation."),
     ("Effects of acid rain include:",["None","*Lake acidification, forest damage, soil nutrient leaching, and building/monument corrosion","Only aesthetic damage","Only minor pH changes"],"Widespread harm."),
     ("PM2.5 refers to particles:",["Larger than 10 micrometers","*Smaller than 2.5 micrometers in diameter (can penetrate deep into lungs and enter bloodstream)","Exactly 2.5 cm","Only dust"],"Fine particulate matter."),
     ("The Clean Air Act (1970, US) has led to:",["No improvements","*Significant reductions in criteria pollutants (lead down 99%, SO₂ down ~90%) despite population and GDP growth","Only minor changes","Increased pollution"],"Major success story."),
     ("Lead was removed from gasoline because it:",["Was too expensive","*Caused neurological damage, especially in children (leaded gas emissions were the primary source of airborne lead)","Improved engine performance","Was too abundant"],"Public health victory."),
     ("Catalytic converters on cars reduce emissions of:",["CO₂ only","*CO, NOₓ, and unburned hydrocarbons/VOCs","Only noise","Nothing"],"Vehicle emission control."),
     ("Industrial scrubbers reduce:",["Nothing","*SO₂ and particulate emissions from smokestacks (removes pollutants before they enter the atmosphere)","Only CO₂","Only heat"],"Emission control technology."),
     ("Air Quality Index (AQI) measures:",["Only temperature","*How clean or polluted outdoor air is and associated health effects (0-500 scale; higher = worse)","Only humidity","Only wind"],"Public health tool."),
     ("Volatile Organic Compounds (VOCs) come from:",["Only factories","*Paints, solvents, gasoline, cleaning products, and vehicle emissions (contribute to smog formation)","Only nature","Only food"],"Widespread sources."),
     ("For the AP exam, air pollution questions involve:",["Only definitions","*Identifying pollutant sources and types, explaining formation of secondary pollutants, analyzing health impacts, and evaluating control strategies","Only naming laws","Only listing pollutants"],"Comprehensive analysis.")]
)
lessons[k]=v

# 6.2
k,v = build_lesson(6,2,"Water Pollution",
    "<h3>Water Pollution</h3>"
    "<h4>Types</h4>"
    "<ul><li><b>Point source:</b> Single identifiable source (factory pipe, sewage outfall).</li>"
    "<li><b>Non-point source:</b> Diffuse (agricultural runoff, urban stormwater).</li></ul>"
    "<h4>Major Pollutants</h4>"
    "<ul><li><b>Nutrients:</b> N, P → eutrophication → algal blooms → dead zones.</li>"
    "<li><b>Pathogens:</b> Bacteria, viruses from sewage → cholera, dysentery.</li>"
    "<li><b>Toxics:</b> Heavy metals (Hg, Pb), pesticides, pharmaceuticals.</li>"
    "<li><b>Thermal:</b> Heated discharge from power plants reduces dissolved O₂.</li></ul>",
    [("Eutrophication","Excess nutrient enrichment (N, P) → algal blooms → decomposition depletes oxygen → dead zones."),
     ("Biological Oxygen Demand (BOD)","Amount of O₂ needed by microorganisms to decompose organic matter; high BOD = polluted water."),
     ("Dead Zone","Area of very low dissolved oxygen (hypoxia) where most aquatic life cannot survive."),
     ("Pathogen","Disease-causing organism (bacteria, viruses, parasites) in contaminated water."),
     ("Bioaccumulation","Buildup of a persistent chemical in an organism's body over time (e.g., mercury in fish).")],
    [("Point source water pollution comes from:",["Everywhere","*A single, identifiable source (e.g., factory discharge pipe, sewage outfall)","Only farms","Only nature"],"Identifiable."),
     ("Non-point source pollution is the _____ type to control.",["Easiest","*Hardest (diffuse sources: agricultural runoff, urban stormwater, atmospheric deposition)","Same as point","Not a real type"],"Widespread & diffuse."),
     ("Eutrophication is caused by excess:",["Oxygen","*Nutrients (nitrogen and phosphorus) entering waterways","Salt","Acid"],"Nutrient overload."),
     ("The sequence of eutrophication is:",["Algae die first","*Excess nutrients → algal bloom → algae die → decomposition consumes oxygen → dead zone","Plants grow → animals flourish","Water clears"],"Chain reaction."),
     ("The Gulf of Mexico dead zone is primarily caused by:",["Ocean currents","*Agricultural fertilizer runoff from the Mississippi River watershed","Industrial discharge directly","Volcanic vents"],"Non-point source."),
     ("BOD (Biological Oxygen Demand) indicates:",["Clean water","*How much organic pollution is in water (high BOD = lots of organic waste = less dissolved oxygen)","Only temperature","Only pH"],"Pollution indicator."),
     ("Major waterborne pathogens include:",["Only viruses","*Bacteria (cholera, E. coli), viruses (hepatitis A), and parasites (Giardia, Cryptosporidium)","Only animals","Only chemicals"],"Disease-causing organisms."),
     ("Globally, approximately _____ people lack access to safely managed sanitation.",["100 million","*~3.6 billion (nearly half the world)","1 million","None"],"Sanitation crisis."),
     ("Heavy metals in water (mercury, lead) are dangerous because they:",["Decompose quickly","*Bioaccumulate in organisms and biomagnify up food chains; cause neurological and developmental damage","Are harmless","Only affect plants"],"Persistent toxins."),
     ("Mercury contamination in fish is primarily from:",["Natural sources only","*Coal-burning power plants (atmospheric deposition) and gold mining","Agriculture","Plastics"],"Atmospheric pathway."),
     ("Thermal pollution reduces dissolved oxygen because:",["Cold water has less O₂","*Warm water holds less dissolved gas — heated discharge from power plants raises water temperature","Oxygen is destroyed","Fish use more O₂ in cold water"],"Temperature-solubility relationship."),
     ("Microplastics in water are concerning because they:",["Are visible and easily removed","*Are tiny (<5mm), persistent, absorb toxins, and are ingested by organisms throughout the food web","Only affect oceans","Dissolve quickly"],"Emerging pollutant."),
     ("Pharmaceuticals (antibiotics, hormones) in waterways can:",["Be easily removed by treatment","*Disrupt endocrine systems in aquatic life, contribute to antibiotic resistance; not fully removed by most treatment plants","Have no effect","Only affect humans"],"Emerging concern."),
     ("The Clean Water Act (1972, US) primarily regulates:",["Only drinking water","*Point source discharges into surface waters (sets discharge limits and water quality standards)","Only groundwater","Only ocean dumping"],"Major US water law."),
     ("Wastewater treatment includes primary (settling), secondary (biological), and _____ treatment.",["No further steps","*Tertiary (advanced filtration, chemical treatment to remove nutrients, pharmaceuticals)","Only chlorination","Only UV"],"Three levels."),
     ("Wetlands help purify water by:",["Having no effect","*Filtering sediment, absorbing nutrients and toxins, and allowing biological breakdown of pollutants (natural treatment systems)","Only providing habitat","Only flooding"],"Nature's water filter."),
     ("Impervious surfaces in cities increase water pollution by:",["Reducing runoff","*Increasing stormwater runoff that carries oil, metals, trash, and chemicals directly into waterways","Having no connection","Cleaning water"],"Urban runoff."),
     ("Green infrastructure solutions for water pollution include:",["More concrete","*Rain gardens, permeable pavement, green roofs, constructed wetlands, and bioswales","Only pipes","Only treatment plants"],"Nature-based solutions."),
     ("Ocean acidification occurs when CO₂ dissolves in seawater, forming:",["Oxygen","*Carbonic acid (H₂CO₃), which lowers pH and threatens shell-forming organisms","More salt","Hydrogen"],"CO₂ → acid."),
     ("For the AP exam, water pollution questions require:",["Only naming pollutants","*Identifying pollution sources (point vs. non-point), describing impacts on ecosystems, and evaluating remediation strategies","Only one answer","Only definitions"],"Applied analysis.")]
)
lessons[k]=v

# 6.3
k,v = build_lesson(6,3,"Soil Pollution & Land Degradation",
    "<h3>Soil Pollution &amp; Land Degradation</h3>"
    "<p>Soil contamination comes from industrial waste, pesticides, mining, landfills, and atmospheric deposition. Land degradation affects ~25% of Earth's ice-free land.</p>"
    "<h4>Key Issues</h4>"
    "<ul><li><b>Brownfields:</b> Former industrial sites with contamination requiring cleanup.</li>"
    "<li><b>Superfund (CERCLA):</b> US law funding cleanup of the worst hazardous waste sites.</li>"
    "<li><b>Bioremediation:</b> Using organisms to break down contaminants (bacteria, fungi, plants).</li></ul>",
    [("Brownfield","Abandoned or underused industrial/commercial site with real or suspected contamination."),
     ("Superfund (CERCLA)","US law (1980) establishing a program to clean up the nation's worst hazardous waste sites."),
     ("Bioremediation","Using living organisms (bacteria, fungi, plants) to break down or absorb soil and water contaminants."),
     ("Phytoremediation","Using plants to absorb, accumulate, or break down contaminants in soil or water."),
     ("Land Degradation","Decline in land productivity due to erosion, contamination, salinization, or desertification.")],
    [("Land degradation affects approximately _____ of Earth's ice-free land surface.",["1%","10%","*~25% (and worsening due to agriculture, mining, urbanization)","50%"],"Widespread problem."),
     ("Brownfields are:",["National parks","*Abandoned or underused industrial sites with real or suspected contamination","Agricultural land","Green spaces"],"Urban contamination."),
     ("Superfund (CERCLA, 1980) was created to:",["Encourage pollution","*Fund cleanup of the nation's worst uncontrolled hazardous waste sites","Only study pollution","Only regulate new sites"],"Cleanup law."),
     ("The principle of 'polluter pays' means:",["Government always pays","*The party responsible for contamination should bear the cleanup costs","No one pays","Only landowners pay"],"Legal accountability."),
     ("Bioremediation uses _____ to clean up contaminated soil.",["Only chemicals","*Living organisms (bacteria, fungi, or plants that break down or absorb pollutants)","Only machinery","Only heat"],"Biological cleanup."),
     ("Phytoremediation specifically uses:",["Animals","*Plants (e.g., sunflowers to absorb heavy metals, willows for water filtration)","Only chemicals","Only bacteria"],"Plant-based cleanup."),
     ("Advantages of bioremediation over traditional cleanup include:",["Only cost","*Lower cost, less disruptive, in-situ treatment (no soil removal), and more environmentally friendly","Higher speed always","No advantages"],"Green technology."),
     ("Pesticide contamination in soil can:",["Only affect pests","*Persist for years, leach into groundwater, harm soil organisms, and enter the food chain","Decompose instantly","Only affect surface"],"Persistent impact."),
     ("Heavy metals in soil (lead, cadmium, arsenic) are particularly dangerous because they:",["Decompose quickly","*Are persistent (don't break down), bioaccumulate, and are toxic to organisms and humans","Only affect plants","Are harmless in soil"],"Non-degradable toxins."),
     ("Mining waste (tailings) can contaminate soil through:",["No mechanism","*Acid mine drainage (sulfuric acid from exposed minerals), heavy metal leaching, and windblown dust","Only dust","Only water"],"Multiple pathways."),
     ("Landfills can contaminate surrounding soil and groundwater through:",["Clean operations","*Leachate (contaminated liquid that seeps through waste and can escape the landfill liner)","Only odor","Only visual impact"],"Leachate risk."),
     ("Modern sanitary landfills differ from open dumps by having:",["No differences","*Liners (clay + plastic), leachate collection systems, methane capture, and daily cover","Only a fence","Only a sign"],"Engineered protection."),
     ("Soil salinization from irrigation can be reduced by:",["More irrigation","*Drip irrigation, better drainage, growing salt-tolerant crops, and allowing fields to rest","Only flooding","Only chemicals"],"Management solutions."),
     ("Persistent Organic Pollutants (POPs) include:",["Only natural chemicals","*DDT, PCBs, dioxins — chemicals that persist in the environment, bioaccumulate, and are toxic","Only pesticides","Only industrial chemicals"],"Long-lasting toxins."),
     ("The Stockholm Convention (2001) aims to eliminate or restrict:",["Greenhouse gases","*Persistent Organic Pollutants (POPs) because of their global transport and bioaccumulation","Only one chemical","Only in developed countries"],"International POPs treaty."),
     ("Love Canal (1978) was a landmark case because:",["Nothing happened","*A neighborhood built on a buried chemical waste dump had widespread illness → led to Superfund legislation","It was cleaned easily","Only one person was affected"],"Historic contamination."),
     ("Soil contamination disproportionately affects:",["Wealthy communities","*Low-income and minority communities (environmental justice issue — toxic sites often located in disadvantaged areas)","No particular group","Only rural areas"],"Environmental justice."),
     ("Composting reduces landfill waste by:",["Increasing waste","*Diverting organic matter from landfills and converting it to nutrient-rich soil amendment","Only reducing smell","Only for farms"],"Waste reduction."),
     ("Contaminated soil can be treated by thermal desorption, which:",["Freezes contaminants","*Heats soil to vaporize contaminants for collection and treatment","Dissolves contaminants in water","Burns the soil"],"Heat-based cleanup."),
     ("For the AP exam, soil pollution connects to:",["Only chemistry","*Agriculture, water quality, human health, environmental justice, waste management, and policy","Only one topic","Only biology"],"Multi-dimensional topic.")]
)
lessons[k]=v

# 6.4
k,v = build_lesson(6,4,"Solid Waste Management",
    "<h3>Solid Waste Management</h3>"
    "<p>The US generates ~292 million tons of municipal solid waste (MSW) annually (~4.9 lbs/person/day). Globally: ~2 billion tons/year.</p>"
    "<h4>Hierarchy (most to least preferred)</h4>"
    "<ul><li><b>Reduce</b> → <b>Reuse</b> → <b>Recycle/Compost</b> → <b>Energy recovery</b> → <b>Landfill</b></li></ul>"
    "<p>US recycles ~32% of MSW. Landfills remain the primary disposal method despite methane emissions.</p>",
    [("Municipal Solid Waste (MSW)","Everyday trash generated by households and businesses; ~292 million tons/year in the US."),
     ("Waste Hierarchy","Preferred order: Reduce → Reuse → Recycle/Compost → Energy Recovery → Landfill (least preferred)."),
     ("Recycling Rate","Percentage of waste diverted from landfills through recycling and composting; US ~32%."),
     ("Waste-to-Energy (WTE)","Incineration of waste to generate electricity; reduces landfill volume but produces ash and emissions."),
     ("E-Waste","Discarded electronics containing valuable metals and hazardous materials; fastest-growing waste stream.")],
    [("The US generates approximately _____ of MSW per person per day.",["1 lb","*~4.9 lbs (~2.2 kg)","10 lbs","0.5 lbs"],"High per-capita waste."),
     ("The waste management hierarchy prioritizes (most to least preferred):",["Landfill → Burn → Reduce","*Reduce → Reuse → Recycle/Compost → Energy Recovery → Landfill","Burn → Recycle → Reduce","Landfill → Reduce → Recycle"],"Prevention first."),
     ("The US recycling rate is approximately:",["5%","50%","*~32%","75%"],"Room for improvement."),
     ("Landfills are the _____ preferred option in the waste hierarchy.",["Most","*Least (last resort after reduce, reuse, recycle, and energy recovery)","Second","Third"],"Bottom of hierarchy."),
     ("Modern sanitary landfills have liners to prevent:",["Odor only","*Leachate (contaminated liquid) from contaminating groundwater and surrounding soil","Only animals","Only windblown waste"],"Groundwater protection."),
     ("Landfill methane is generated by:",["Oxygen-rich decomposition","*Anaerobic (oxygen-free) decomposition of organic waste by bacteria","Burning waste","Chemical reactions with plastic"],"Greenhouse gas source."),
     ("Landfill methane can be captured and used for:",["Nothing","*Energy generation (methane is essentially natural gas and can generate electricity or heat)","Only flaring","Only venting"],"Turning waste into energy."),
     ("Waste-to-energy (WTE) incineration reduces waste volume by:",["10%","50%","*~87% (ash remains)","100%"],"Massive volume reduction."),
     ("Concerns about WTE incineration include:",["None","*Air emissions (dioxins, heavy metals, particulates), toxic ash disposal, and discouraging recycling","Only cost","Only aesthetics"],"Environmental trade-offs."),
     ("E-waste (electronic waste) is the fastest-growing waste stream because:",["Electronics last forever","*Rapid technology turnover and short product lifespans create massive volumes of discarded electronics","People don't use electronics","Only in one country"],"Planned obsolescence."),
     ("E-waste contains both valuable materials (gold, copper) and:",["Nothing else","*Hazardous substances (lead, mercury, cadmium, flame retardants) requiring careful handling","Only plastic","Only glass"],"Complex waste stream."),
     ("Much of the world's e-waste is exported to:",["Nowhere","*Developing countries (e.g., Ghana, China, India) where informal recycling exposes workers to toxic materials","Only Europe","Only landfills"],"Environmental justice."),
     ("The circular economy model aims to:",["Maximize waste","*Design products for durability, repairability, reuse, and recycling — eliminating waste entirely","Only recycle more","Only burn less"],"Systemic redesign."),
     ("Extended Producer Responsibility (EPR) requires:",["Only consumers to recycle","*Manufacturers to bear responsibility for end-of-life management of their products","Only government action","Only retailers"],"Producer accountability."),
     ("Single-use plastics are problematic because they:",["Decompose quickly","*Are used briefly but persist in the environment for hundreds of years, polluting oceans and land","Are easy to recycle","Are biodegradable"],"Persistent waste."),
     ("Pay-as-you-throw (PAYT) programs charge residents:",["A flat fee","*Based on the amount of waste they generate — incentivizing waste reduction and recycling","Nothing","Only for recycling"],"Economic incentive."),
     ("Composting diverts approximately _____ of MSW that is organic material.",["5%","*~30% (food scraps and yard waste are large portions of MSW)","1%","50%"],"Major diversion potential."),
     ("Ocean plastic pollution is estimated at _____ tons entering oceans annually.",["1,000","*~8-11 million tons","100","1 billion"],"Marine pollution crisis."),
     ("Zero-waste communities aim to:",["Ban all waste","*Divert >90% of waste from landfills through aggressive reduction, reuse, recycling, and composting","Only recycle","Only incinerate"],"Aspirational goal."),
     ("For the AP exam, waste management questions connect to:",["Only chemistry","*Resource use, pollution (air, water, soil), environmental justice, policy, and sustainability","Only one unit","Only landfills"],"Multi-concept topic.")]
)
lessons[k]=v

# 6.5
k,v = build_lesson(6,5,"Hazardous Waste & Recycling",
    "<h3>Hazardous Waste &amp; Recycling</h3>"
    "<p><b>Hazardous waste:</b> Waste that is ignitable, corrosive, reactive, or toxic. Regulated by RCRA (Resource Conservation and Recovery Act, 1976).</p>"
    "<h4>Recycling</h4>"
    "<p>Reduces need for virgin resources, saves energy (recycling aluminum uses 95% less energy than new), and reduces landfill burden. Challenges: contamination, market economics, single-stream confusion.</p>",
    [("Hazardous Waste","Waste with properties that make it dangerous: ignitable, corrosive, reactive, or toxic."),
     ("RCRA","Resource Conservation and Recovery Act (1976); regulates hazardous waste from cradle to grave in the US."),
     ("Cradle-to-Grave Tracking","RCRA system tracking hazardous waste from generation through transport, treatment, storage, and disposal."),
     ("Single-Stream Recycling","All recyclables placed in one bin; convenient but increases contamination (non-recyclable items mixed in)."),
     ("Downcycling","Recycling material into a lower-quality product (e.g., plastic bottles → carpet fiber); common for plastics.")],
    [("Hazardous waste is defined as waste that is:",["Only toxic","*Ignitable, corrosive, reactive, or toxic (RCRA definition)","Only flammable","Only radioactive"],"Four characteristics."),
     ("RCRA (1976) regulates hazardous waste:",["Only at disposal","*From cradle to grave (generation → transport → treatment → storage → disposal)","Only during transport","Only at generation"],"Complete lifecycle."),
     ("Recycling aluminum saves approximately _____ of the energy needed to make new aluminum.",["25%","50%","*~95% (recycling aluminum is enormously energy-efficient)","10%"],"Huge energy savings."),
     ("Recycling paper saves approximately _____ of the energy compared to making new paper.",["10%","*~60-70%","90%","25%"],"Significant savings."),
     ("Single-stream recycling increases convenience but also increases:",["Recycling rates only","*Contamination (when non-recyclable items or food waste are mixed in, entire batches may be landfilled)","Energy use","Only cost"],"Contamination problem."),
     ("Downcycling means:",["Recycling into higher quality","*Recycling into a lower-quality product (e.g., mixed plastics → park benches; less valuable than original)","Perfect recycling","Destroying waste"],"Quality degradation."),
     ("The biggest challenge for plastics recycling is:",["Collecting plastic","*Most plastics can only be downcycled, and many types are not economically recyclable (only ~5-6% of US plastics are recycled)","Melting plastic","Sorting is easy"],"Low recycling rate."),
     ("Wish-cycling (putting non-recyclable items in recycling bins) leads to:",["Better recycling","*Contamination that can cause entire loads to be sent to landfill instead of being recycled","No problems","Higher quality materials"],"Counterproductive."),
     ("Chemical recycling of plastics aims to:",["Burn them","*Break plastics back into monomers or feedstock chemicals, enabling true recycling into same-quality products","Only shred them","Only compress them"],"Emerging technology."),
     ("PCBs (polychlorinated biphenyls) are hazardous because they:",["Decompose quickly","*Are persistent, bioaccumulate, and cause cancer and other health problems (banned in US in 1979 but still present)","Are harmless","Only affect fish"],"Legacy pollutant."),
     ("Proper hazardous waste disposal includes:",["Dumping in regular landfills","*Secure chemical landfills with multiple liners, leak detection, and monitoring — or treatment (incineration, neutralization)","Ocean dumping","Only burning"],"Specialized facilities."),
     ("Deep-well injection involves:",["Surface disposal","*Pumping liquid hazardous waste deep underground into permeable rock formations sealed from aquifers","Dumping in oceans","Only for water"],"Underground disposal."),
     ("The Basel Convention (1989) restricts:",["Only air pollution","*International movement of hazardous waste (prevents rich nations from dumping in poor nations)","Only nuclear waste","Only e-waste"],"Environmental justice treaty."),
     ("Radioactive waste requires isolation for:",["Days","Years","*Thousands to hundreds of thousands of years (high-level waste)","Months"],"Extreme persistence."),
     ("Glass recycling is efficient because glass can be recycled:",["Only once","A few times","*Infinitely (glass doesn't lose quality through recycling)","Never"],"Perfect recyclability."),
     ("Metal recycling is economically viable because:",["Metals are abundant","*Mining and refining virgin ores is energy-intensive and environmentally destructive; recycled metals save significant energy","Metals are cheap to mine","Recycling is free"],"Economic + environmental benefit."),
     ("Composting organic waste is preferable to landfilling because:",["Landfills are fine for organics","*Composting creates useful soil amendment and avoids methane emissions from anaerobic landfill decomposition","Composting costs more always","No difference"],"Better outcome."),
     ("The concept of 'cradle to cradle' design means:",["Products go to landfill","*Products are designed so all materials can be fully recovered and reused in new products (eliminating waste)","Only minimal recycling","Only reducing packaging"],"Design philosophy."),
     ("Illegal dumping of hazardous waste is a problem because:",["It's legal","*It saves money for violators but causes severe environmental contamination and public health risks in affected communities","It's rare","It's always caught"],"Enforcement challenge."),
     ("For the AP exam, hazardous waste and recycling questions often involve:",["Only definitions","*Comparing disposal methods, analyzing policy effectiveness, evaluating environmental justice issues, and calculating energy savings","Only listing waste types","Only naming laws"],"Applied analysis.")]
)
lessons[k]=v

# 6.6
k,v = build_lesson(6,6,"Case Studies: Pollution Control",
    "<h3>Case Studies: Pollution Control</h3>"
    "<h4>US Acid Rain Program (1990 Clean Air Act Amendments)</h4>"
    "<p>Cap-and-trade for SO₂ emissions. Reduced SO₂ by ~90% since 1990. Cost far less than predicted. Model for pollution regulation.</p>"
    "<h4>London Smog (1952)</h4>"
    "<p>Great Smog killed ~12,000 people. Led to UK's Clean Air Act (1956). Spurred global air quality awareness.</p>"
    "<h4>Flint Water Crisis (2014)</h4>"
    "<p>Water source switch corroded lead pipes → lead contamination. Disproportionately affected low-income, majority-Black community. Environmental justice failure.</p>",
    [("Acid Rain Program","US cap-and-trade program for SO₂ under 1990 Clean Air Act Amendments; reduced SO₂ by ~90%."),
     ("Great Smog of London","1952 killer smog (coal smoke + fog) that killed ~12,000 people; led to UK Clean Air Act."),
     ("Flint Water Crisis","2014 lead contamination when Flint, MI switched water sources; a major environmental justice failure."),
     ("Cap-and-Trade","Market-based system: government caps total pollutant emissions; companies trade emission allowances."),
     ("Environmental Justice","The fair treatment of all people regardless of race, income, or origin in environmental policy and protection.")],
    [("The US Acid Rain Program reduced SO₂ emissions by approximately:",["10%","50%","*~90% since 1990","25%"],"Dramatic success."),
     ("The Acid Rain Program used a _____ approach.",["Command-and-control only","*Cap-and-trade (set a cap on total SO₂ emissions; companies trade emission allowances)","Voluntary only","Tax only"],"Market-based regulation."),
     ("The Acid Rain Program cost _____ than initially predicted.",["More","*Much less (industry found cheaper ways to reduce emissions than regulators anticipated)","The same","Nothing"],"Cost-effective success."),
     ("The Great Smog of London (1952) killed approximately:",["100 people","1,000","*~12,000 people (from respiratory and cardiovascular causes over several months)","100,000"],"Lethal air pollution."),
     ("The Great Smog was caused by:",["Cars only","*Coal smoke + cold weather + windless fog trapping pollutants (high SO₂ and PM concentrations)","Factories only","Natural fog"],"Perfect storm of pollution."),
     ("The UK Clean Air Act (1956) was passed directly because of:",["Routine policy","*The Great Smog catastrophe, which made air pollution regulation politically urgent","International pressure","Scientific interest"],"Crisis drove policy."),
     ("The Flint Water Crisis occurred when:",["A factory polluted the water","*The city switched water sources to save money; the new (more corrosive) water leached lead from aging pipes","An earthquake broke pipes","Lead was added intentionally"],"Cost-cutting decision."),
     ("The Flint crisis disproportionately affected:",["Wealthy communities","*A low-income, majority-Black community — highlighting systemic environmental injustice","Only whites","No specific group"],"Environmental justice failure."),
     ("Environmental justice means:",["Only economic justice","*Fair treatment and meaningful involvement of all people regardless of race, income, or origin in environmental decisions","Only for the wealthy","Only in courts"],"Equitable protection."),
     ("The Cuyahoga River (Cleveland) caught fire in 1969 because:",["Lightning struck it","*It was so polluted with industrial chemicals and oil that it was literally flammable","A boat accident","Arson"],"Pollution was that extreme."),
     ("The Cuyahoga River fire contributed to passage of:",["No legislation","*The Clean Water Act (1972) and creation of the EPA (1970)","Only local laws","Only fire codes"],"Catalyzed regulation."),
     ("Bhopal disaster (1984, India) involved:",["A nuclear accident","*A toxic gas leak (methyl isocyanate) from a Union Carbide pesticide plant, killing thousands","An oil spill","A chemical explosion"],"Worst industrial disaster."),
     ("Bhopal's death toll is estimated at:",["100","1,000","*3,800–16,000+ (with ongoing health effects for hundreds of thousands)","50"],"Devastating impact."),
     ("Love Canal (1978) demonstrated:",["Safe waste disposal","*That burying hazardous waste does not make it disappear — chemicals migrated into homes and schools","Successful cleanup","No problem"],"Never goes away."),
     ("Minamata disease (Japan, 1950s) was caused by:",["Natural processes","*Industrial mercury discharge into Minamata Bay → bioaccumulation in fish → severe neurological damage in people","Only genetics","Only bacteria"],"Mercury poisoning."),
     ("These case studies share the pattern of:",["No common thread","*Environmental harm being discovered only after significant damage — highlighting the need for prevention and precaution","Quick resolution","Only affecting one region"],"Recurring theme."),
     ("Environmental regulation typically follows:",["Proactive planning","*Reactive response to crises (disasters → public outrage → legislation) — though this is changing","Random timing","No pattern"],"Crisis-driven policy."),
     ("The lesson from the Acid Rain Program is that:",["Market approaches never work","*Well-designed market-based policies can achieve environmental goals more cheaply than command-and-control regulation","Only bans work","Technology is irrelevant"],"Policy design matters."),
     ("The lesson from Flint is that:",["Infrastructure doesn't matter","*Aging infrastructure, environmental racism, and regulatory failure can create public health disasters — equity must be part of environmental policy","Only new systems work","It was inevitable"],"Justice + infrastructure."),
     ("For the AP exam, pollution case studies require:",["Only naming events","*Analyzing causes, identifying stakeholders, evaluating policy responses, and connecting to broader environmental principles","Only dates","Only locations"],"Critical analysis.")]
)
lessons[k]=v

# 6.7
k,v = build_lesson(6,7,"AP Prep: Pollution Models",
    "<h3>AP Prep: Pollution Models</h3>"
    "<h4>Key Concepts for Calculations</h4>"
    "<ul><li><b>LD50:</b> Dose lethal to 50% of test organisms; measures acute toxicity.</li>"
    "<li><b>Dose-response curve:</b> Plots health effect vs. exposure dose; determines threshold and no-observed-adverse-effect level (NOAEL).</li>"
    "<li><b>Bioaccumulation factor:</b> Concentration in organism / concentration in environment.</li>"
    "<li><b>Biomagnification factor:</b> Concentration at higher trophic level / concentration at lower level.</li>"
    "<li><b>Half-life:</b> Time for pollutant concentration to decrease by half.</li></ul>",
    [("LD50","Lethal Dose 50: the dose of a substance that kills 50% of a test population; measure of acute toxicity."),
     ("Dose-Response Curve","Graph showing the relationship between exposure dose and biological response/health effect."),
     ("NOAEL","No Observed Adverse Effect Level: highest dose with no measurable harmful effect."),
     ("Bioconcentration Factor","Ratio of pollutant concentration in an organism to its concentration in the surrounding environment."),
     ("Pollutant Half-Life","Time for half of a pollutant to break down or be removed from the environment.")],
    [("LD50 measures:",["The lethal dose for all organisms","*The dose that kills 50% of a test population (lower LD50 = more toxic)","Only non-lethal effects","Only chronic effects"],"Acute toxicity measure."),
     ("A substance with a lower LD50 is:",["Less toxic","*More toxic (it takes less of the substance to kill 50% of organisms)","Equally toxic","Non-toxic"],"Inverse relationship."),
     ("If substance A has LD50 = 5 mg/kg and substance B has LD50 = 500 mg/kg, then:",["B is more toxic","*A is more toxic (100× more toxic; requires much less to kill 50%)","They're equal","Neither is toxic"],"Compare LD50."),
     ("A dose-response curve shows:",["Only one data point","*The relationship between increasing exposure (dose) and the severity of biological response","Only LD50","Only mortality"],"Graphical analysis."),
     ("The threshold in a dose-response curve is:",["Always zero","*The dose below which no measurable effect is observed (though some scientists argue no safe threshold exists for carcinogens)","Always high","The LD50"],"Effect onset."),
     ("NOAEL stands for:",["No Obvious Action Expected Locally","*No Observed Adverse Effect Level (highest dose with no measurable harmful effect)","Normal Observation Above Expected Limit","None Of the Above Effects Listed"],"Safety benchmark."),
     ("Bioaccumulation factor is calculated as:",["Environment ÷ organism","*Concentration in organism ÷ concentration in environment","Weight of organism","Volume of water"],"Ratio of concentrations."),
     ("If mercury in water is 0.001 ppm and in a fish is 1 ppm, the bioaccumulation factor is:",["0.001","1","*1,000 (1/0.001 = 1,000)","100"],"1,000× concentration."),
     ("Biomagnification factor is:",["Concentration in prey ÷ predator","*Concentration at higher trophic level ÷ concentration at lower trophic level","Only for mercury","Always 10"],"Trophic amplification."),
     ("If DDT in zooplankton is 0.04 ppm and in fish is 0.5 ppm, the biomagnification factor is:",["0.04","*12.5 (0.5/0.04 = 12.5)","5","50"],"Step-up factor."),
     ("The half-life of a pollutant is:",["Time to completely degrade","*Time for half of the pollutant to break down or be removed","Full degradation time","Only for radioactive materials"],"50% reduction time."),
     ("If a pesticide has a half-life of 30 days and initial concentration is 100 ppm, after 90 days:",["100 ppm remains","50 ppm remains","*12.5 ppm (100 → 50 → 25 → 12.5; three half-lives)","0 ppm"],"Three half-lives."),
     ("Persistent pollutants (long half-lives) are more dangerous because they:",["Degrade quickly","*Remain in the environment longer, increasing exposure time and bioaccumulation potential","Are always non-toxic","Only affect one species"],"Duration of exposure."),
     ("Synergistic effects occur when two pollutants together cause:",["Less damage","*Worse effects than the sum of their individual effects (1+1 > 2)","Equal effects","No interaction"],"More than additive."),
     ("Antagonistic effects occur when one substance _____ the effects of another.",["Increases","*Reduces (e.g., a treatment that counteracts a poison)","Has no effect on","Doubles"],"Protective interaction."),
     ("Acute exposure refers to:",["Long-term, low-dose","*Short-term, high-dose exposure to a substance","Only occupational","Only dietary"],"Brief, intense."),
     ("Chronic exposure refers to:",["Short-term, high-dose","*Long-term, low-dose exposure over weeks to years","Only from one source","Only acute poisoning"],"Prolonged, lower level."),
     ("Risk assessment involves:",["Guessing","*Hazard identification, dose-response assessment, exposure assessment, and risk characterization (4 steps)","Only one calculation","Only LD50"],"Systematic evaluation."),
     ("For AP calculations, students should show:",["Only the answer","*All work: formula used, correct substitution, correct units, and environmental interpretation","Only setup","Only the formula"],"Complete solutions."),
     ("Understanding toxicology and pollution models is essential for AP because:",["It's rarely tested","*Questions on LD50, dose-response, bioaccumulation, and biomagnification appear regularly in both MC and FRQ","Only one question","Only in one unit"],"Core AP content.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 6: wrote {len(lessons)} lessons")
