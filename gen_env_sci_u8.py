#!/usr/bin/env python3
"""Environmental Science Unit 8 – Environmental Policy & Law (6 lessons)."""
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

# 8.1
k,v = build_lesson(8,1,"History of Environmental Movements",
    "<h3>History of Environmental Movements</h3>"
    "<p>Modern environmentalism grew from conservation and preservation movements of the 19th century.</p>"
    "<h4>Key Milestones</h4>"
    "<ul><li><b>1850s–1900s:</b> John Muir (preservation), Gifford Pinchot (conservation/wise use), creation of first national parks.</li>"
    "<li><b>1962:</b> Rachel Carson's <i>Silent Spring</i> — exposed pesticide dangers, sparked modern environmental movement.</li>"
    "<li><b>1970:</b> First <b>Earth Day</b> (20 million participants). EPA established. Clean Air Act, Clean Water Act followed.</li>"
    "<li><b>1980s–present:</b> Environmental justice movement, global issues (ozone, climate), sustainability focus.</li></ul>",
    [("Preservation","Philosophy of protecting wilderness in its natural state (John Muir, Sierra Club)."),
     ("Conservation","Philosophy of managing natural resources for sustainable human use (Gifford Pinchot, 'wise use')."),
     ("Silent Spring","Rachel Carson's 1962 book exposing DDT's ecological damage; catalyzed the modern environmental movement and led to DDT ban."),
     ("Earth Day","First celebrated April 22, 1970; 20 million participants; led directly to the creation of the EPA."),
     ("Environmental Justice Movement","Movement addressing the disproportionate environmental burdens on minority and low-income communities.")],
    [("The preservation vs. conservation debate was between:",["Two politicians","*John Muir (preservation: protect wilderness untouched) vs. Gifford Pinchot (conservation: manage for sustainable use)","Two scientists","Two countries"],"Foundational philosophies."),
     ("Rachel Carson's Silent Spring (1962) focused on the dangers of:",["Nuclear weapons","*Pesticides (especially DDT) and their accumulation in food chains (bioaccumulation/biomagnification)","Air pollution","Water pollution"],"Catalyzed modern environmentalism."),
     ("The first Earth Day (April 22, 1970) attracted approximately:",["1,000 people","100,000 people","*20 million participants across the US","1 billion people"],"Massive mobilization."),
     ("The EPA (Environmental Protection Agency) was established in:",["1950","1962","*1970 (by President Nixon in response to growing public concern)","1990"],"Direct result of Earth Day."),
     ("The environmental justice movement highlights that:",["Pollution is evenly distributed","*Minority and low-income communities disproportionately bear the burden of pollution and environmental hazards","Only wealthy areas have pollution","Environment and justice are unrelated"],"Environmental racism."),
     ("The Cuyahoga River fire (1969) in Cleveland helped spark environmental legislation because:",["It was routine","*A river catching fire (from industrial pollution) was so shocking it galvanized public demand for clean water laws","It was the only fire","Nothing happened after"],"Wake-up call."),
     ("Gifford Pinchot's 'wise use' philosophy advocated:",["No resource use","*Scientifically managed resource use for sustained yield and human benefit","Unlimited exploitation","Only preservation"],"Utilitarian conservation."),
     ("John Muir founded the _____ in 1892.",["EPA","WWF","*Sierra Club","Audubon Society"],"Preservation advocacy."),
     ("The first national park in the world was:",["Grand Canyon","*Yellowstone (1872, US)","Yosemite","Denali"],"First of its kind."),
     ("Aldo Leopold's 'land ethic' argued that:",["Land has no value","*Humans have an ethical duty to protect the integrity of ecological communities (expanded ethics to include land)","Only humans matter","Science alone decides"],"Ethical expansion."),
     ("The environmental movement of the 1960s–70s was influenced by:",["Only one event","*Multiple factors: Silent Spring, pollution disasters, nuclear testing concerns, and a broader social justice climate","Only economics","Only politics"],"Convergent forces."),
     ("Love Canal (1978) was significant because:",["It was a success story","*The discovery of toxic waste buried under a neighborhood led to evacuation and the creation of Superfund (CERCLA)","Nothing happened","Only one family was affected"],"Toxic waste crisis."),
     ("The Bhopal disaster (1984) in India involved:",["A nuclear meltdown","*A chemical plant leak (methyl isocyanate) that killed thousands — highlighting industrial safety and environmental justice","An oil spill","A flood"],"Worst industrial disaster."),
     ("The modern environmental movement has expanded to include:",["Only pollution","*Climate change, biodiversity loss, environmental justice, sustainability, and global governance","Only local issues","Only wildlife"],"Broadened scope."),
     ("Indigenous peoples' environmental knowledge is increasingly recognized as:",["Irrelevant","*Valuable for conservation and resource management (traditional ecological knowledge has sustained ecosystems for millennia)","Only historical","Only cultural"],"TEK integration."),
     ("The relationship between poverty and environmental degradation is:",["Non-existent","*Complex and bidirectional — poverty can drive overexploitation, and degradation deepens poverty (vicious cycle)","Only one-directional","Simple"],"Poverty-environment nexus."),
     ("Environmental movements in developing nations often focus on:",["Only wilderness","*Access to clean water, air quality, land rights, corporate accountability, and resistance to resource extraction","Only climate","Same issues as developed nations"],"Different priorities."),
     ("Youth climate movements (e.g., Fridays for Future) demonstrate that:",["Youth don't care","*Young people are powerful advocates demanding intergenerational justice and faster climate action","Only adults can act","Nothing changes"],"Generational mobilization."),
     ("Corporate environmentalism emerged as companies realized:",["Environment doesn't matter","*Environmental responsibility can be both profitable and demanded by consumers and investors (ESG, green branding)","Only cost matters","Only regulation works"],"Market-driven change."),
     ("For AP, students should trace the evolution of environmental thought from:",["Only modern times","*Preservation → conservation → environmental regulation → environmental justice → global sustainability","Only one era","Only US history"],"Historical progression.")]
)
lessons[k]=v

# 8.2
k,v = build_lesson(8,2,"Environmental Laws & Regulations",
    "<h3>Major US Environmental Laws</h3>"
    "<ul><li><b>NEPA (1970):</b> Requires Environmental Impact Statements (EIS) for federal projects.</li>"
    "<li><b>Clean Air Act (1970, amended 1990):</b> Regulates air pollutants; NAAQS standards; cap-and-trade for SO₂.</li>"
    "<li><b>Clean Water Act (1972):</b> Regulates point-source water pollution; NPDES permits; goal: fishable, swimmable waters.</li>"
    "<li><b>Endangered Species Act (1973):</b> Protects listed species and their critical habitat.</li>"
    "<li><b>RCRA (1976):</b> Regulates hazardous waste from generation to disposal (cradle-to-grave).</li>"
    "<li><b>CERCLA/Superfund (1980):</b> Cleans up contaminated sites; 'polluter pays' principle.</li></ul>",
    [("NEPA","National Environmental Policy Act (1970): requires Environmental Impact Statements for major federal projects."),
     ("Clean Air Act","Federal law (1970) setting National Ambient Air Quality Standards (NAAQS) for criteria pollutants."),
     ("Clean Water Act","Federal law (1972) regulating point-source water pollution through NPDES permits."),
     ("Endangered Species Act","Federal law (1973) protecting listed threatened and endangered species and their critical habitat."),
     ("CERCLA (Superfund)","Comprehensive Environmental Response, Compensation, and Liability Act (1980): cleans up contaminated sites using 'polluter pays' principle.")],
    [("NEPA requires federal agencies to prepare _____ for major projects affecting the environment.",["A budget","*An Environmental Impact Statement (EIS) assessing potential environmental effects","A profit report","A safety plan"],"Environmental review."),
     ("The Clean Air Act established _____ for six criteria air pollutants.",["No standards","*National Ambient Air Quality Standards (NAAQS)","Only guidelines","International standards"],"Air quality benchmarks."),
     ("The six criteria air pollutants under the Clean Air Act are:",["Only CO₂","*PM, ground-level ozone, CO, SO₂, NO₂, and lead","Only SO₂","Only PM2.5"],"Key regulated pollutants."),
     ("The Clean Air Act's acid rain program used _____ to reduce SO₂ emissions.",["Only fines","*Cap-and-trade (market-based approach that achieved reductions faster and cheaper than expected)","Only regulations","Only technology"],"Successful market approach."),
     ("The Clean Water Act primarily regulates _____ pollution.",["Non-point source only","*Point-source (from identifiable discharge points like pipes, with NPDES permits)","Only groundwater","Only ocean"],"Identifiable sources."),
     ("Non-point source pollution (runoff) is _____ regulated than point source.",["More strictly","*Less strictly (harder to identify and control; addressed through voluntary programs and BMPs)","Equally","Not at all"],"Regulatory gap."),
     ("The Endangered Species Act protects:",["Only popular species","*Species listed as threatened or endangered AND their critical habitat","Only mammals","Only US species"],"Species + habitat."),
     ("RCRA regulates hazardous waste:",["Only at disposal","*From generation through transportation, treatment, storage, and disposal ('cradle to grave')","Only at production","Only in landfills"],"Complete lifecycle."),
     ("CERCLA (Superfund) was created to:",["Prevent future pollution","*Clean up existing contaminated sites and hold liable parties responsible ('polluter pays')","Only study contamination","Only fine polluters"],"Cleanup + accountability."),
     ("The 'polluter pays' principle means:",["Taxpayers pay","*The party responsible for contamination bears the cost of cleanup and remediation","Nobody pays","Insurance pays"],"Liability principle."),
     ("The Safe Drinking Water Act regulates:",["Only surface water","*Contaminant levels in public drinking water systems (sets Maximum Contaminant Levels, MCLs)","Only private wells","Only bottled water"],"Tap water safety."),
     ("FIFRA (Federal Insecticide, Fungicide, and Rodenticide Act) regulates:",["Only DDT","*Pesticide registration, sale, distribution, and use in the United States","Only household chemicals","Only agricultural seeds"],"Pesticide regulation."),
     ("Environmental regulations are enforced through:",["Only suggestions","*Permits, monitoring, reporting requirements, inspections, fines, and criminal penalties","Only voluntary compliance","Only lawsuits"],"Multiple mechanisms."),
     ("Cost-benefit analysis in environmental regulation involves:",["Ignoring costs","*Weighing the economic costs of regulation against the environmental and health benefits","Only counting costs","Only counting benefits"],"Policy evaluation."),
     ("Critics of environmental regulation argue they:",["Are always effective","*Can be costly to businesses and may reduce competitiveness (though benefits often exceed costs)","Have no impact","Are too weak"],"Economic concerns."),
     ("Supporters argue environmental regulations:",["Hurt the economy","*Protect public health, save costs from pollution-related damages, and often drive innovation (Porter hypothesis)","Only cost money","Don't create jobs"],"Health and economic benefits."),
     ("Regulatory capture occurs when:",["Agencies are too strict","*Regulated industries gain excessive influence over the agencies meant to regulate them","Agencies are effective","Only in corrupt countries"],"Agency compromise."),
     ("The Toxic Substances Control Act (TSCA, reformed 2016) regulates:",["Only new chemicals","*Chemical substances in commerce — reforms required EPA to evaluate existing chemicals and gave authority to restrict or ban them","Only food additives","Only pesticides"],"Chemical safety."),
     ("For AP, students should know the purpose and key provision of:",["Only one law","*NEPA, Clean Air Act, Clean Water Act, ESA, RCRA, and CERCLA (and compare their approaches)","Only international laws","Only state laws"],"Core environmental laws."),
     ("The most effective environmental laws combine:",["Only penalties","*Clear standards, monitoring/enforcement, market incentives, and public participation","Only voluntary programs","Only technology mandates"],"Multi-pronged approach.")]
)
lessons[k]=v

# 8.3
k,v = build_lesson(8,3,"International Environmental Policy",
    "<h3>International Environmental Policy</h3>"
    "<h4>Key Agreements</h4>"
    "<ul><li><b>Stockholm Conference (1972):</b> First major UN conference on the environment; established UNEP.</li>"
    "<li><b>CITES (1975):</b> Convention on International Trade in Endangered Species — regulates wildlife trade.</li>"
    "<li><b>Montreal Protocol (1987):</b> Phased out CFCs; ozone layer recovering — most successful environmental treaty.</li>"
    "<li><b>CBD (1992):</b> Convention on Biological Diversity — conservation and sustainable use of biodiversity.</li>"
    "<li><b>Kunming-Montreal Framework (2022):</b> '30 by 30' — protect 30% of land and sea by 2030.</li></ul>",
    [("UNEP","United Nations Environment Programme, established 1972 at the Stockholm Conference to coordinate global environmental action."),
     ("Montreal Protocol","1987 treaty phasing out CFCs and other ozone-depleting substances; ozone layer now recovering."),
     ("CITES","Convention on International Trade in Endangered Species: regulates and monitors international wildlife trade."),
     ("Convention on Biological Diversity","1992 treaty for conservation and sustainable use of biodiversity; includes Kunming-Montreal '30 by 30' framework."),
     ("30 by 30","Goal from 2022 Kunming-Montreal Framework to protect 30% of Earth's land and ocean by 2030.")],
    [("The 1972 Stockholm Conference was significant as the:",["Last UN meeting","*First major UN conference specifically on the human environment; established UNEP","Only climate conference","Only biodiversity conference"],"Beginning of global environmental governance."),
     ("UNEP's role is to:",["Enforce laws","*Coordinate international environmental action, provide scientific guidance, and support environmental programs","Replace national agencies","Only study climate"],"Coordination, not enforcement."),
     ("CITES regulates:",["All trade","*International trade in endangered species of wild animals and plants (permits required)","Only domestic trade","Only fishing"],"Wildlife trade control."),
     ("The Montreal Protocol is considered the most successful environmental treaty because:",["It was easy","*CFC production dropped >99%, and the ozone layer is on track to recover by ~2065","It only affected one country","It was never enforced"],"Proven success."),
     ("The Biodiversity Convention (CBD, 1992) aims to:",["Only protect parks","*Conserve biodiversity, promote sustainable use, and ensure fair sharing of genetic resource benefits","Only list species","Only protect forests"],"Three objectives."),
     ("The 30 by 30 target from the Kunming-Montreal Framework (2022) aims to:",["Reduce emissions by 30%","*Protect 30% of Earth's land and 30% of ocean by 2030","Reduce pollution by 30%","Increase forests by 30%"],"Ambitious conservation target."),
     ("Currently, approximately _____ of land and _____ of ocean is protected.",["50% / 50%","*~17% of land / ~8% of ocean","30% / 30%","5% / 1%"],"Far from 30 by 30."),
     ("The Basel Convention (1989) regulates:",["Air pollution","*Transboundary movement of hazardous wastes (preventing dumping in developing countries)","Only nuclear waste","Only exports"],"Hazardous waste trade."),
     ("The Rotterdam Convention requires _____ for trade in hazardous chemicals.",["Nothing","*Prior Informed Consent (importing countries must agree before receiving hazardous chemicals or pesticides)","Only labeling","Only testing"],"PIC procedure."),
     ("The Stockholm Convention (2001) targets:",["CO₂ emissions","*Persistent Organic Pollutants (POPs) — banning or restricting the 'dirty dozen' and others","Only heavy metals","Only pesticides"],"POPs elimination."),
     ("International environmental agreements face the challenge of:",["Too much funding","*Sovereignty — nations may resist binding commitments and there is no global enforcement authority","Too many resources","Too many participants"],"Sovereignty vs. environment."),
     ("The 'tragedy of the commons' in international context means:",["Only local issues","*Nations may overexploit shared global resources (oceans, atmosphere) because no single nation bears the full cost","Only private property issues","Only fishing"],"Global commons problem."),
     ("Free-rider problems in environmental treaties occur when:",["Everyone cooperates","*Some nations benefit from others' environmental efforts without contributing (undermining collective action)","Nobody benefits","Only one nation pollutes"],"Incentive to defect."),
     ("The relationship between trade and environment is:",["Unrelated","*Complex — trade can spread pollution (pollution havens) but also spread clean technology and raise living standards","Always positive","Always negative"],"Trade-environment nexus."),
     ("The World Trade Organization and environmental agreements sometimes conflict because:",["They agree perfectly","*WTO rules promoting free trade may clash with environmental regulations seen as trade barriers","WTO ignores trade","Environment is irrelevant to trade"],"Policy tension."),
     ("Multilateral Environmental Agreements (MEAs) work best when they have:",["No monitoring","*Clear targets, monitoring mechanisms, financial support for developing countries, and compliance incentives","Only penalties","Only good intentions"],"Recipe for success."),
     ("South-South cooperation in environmental policy involves:",["Only North-South aid","*Developing countries sharing knowledge, technology, and strategies for environmental challenges","Only competition","Only UN programs"],"Shared challenges."),
     ("The principle of Precautionary Approach states:",["Only act with certainty","*Where there are threats of serious damage, lack of full scientific certainty should not postpone cost-effective preventive measures","Wait for perfect data","Never act"],"Act despite uncertainty."),
     ("Debt-for-nature swaps involve:",["Borrowing more money","*Reducing a country's foreign debt in exchange for investments in domestic conservation programs","Only debt forgiveness","Only trade"],"Creative conservation finance."),
     ("For the AP exam, international environmental policy requires understanding:",["Only treaty names","*Treaty purposes, effectiveness, challenges (sovereignty, compliance, equity), and connections to environmental outcomes","Only dates","Only signatories"],"Policy analysis.")]
)
lessons[k]=v

# 8.4
k,v = build_lesson(8,4,"Environmental Justice",
    "<h3>Environmental Justice</h3>"
    "<p><b>Environmental justice</b> is the fair treatment and meaningful involvement of all people regardless of race, color, income, or national origin with respect to environmental laws, regulations, and policies.</p>"
    "<h4>Key Issues</h4>"
    "<ul><li>Hazardous waste facilities disproportionately sited in minority and low-income communities.</li>"
    "<li>Flint, MI water crisis (2014): lead contamination from changed water source; primarily affecting Black residents.</li>"
    "<li>Cancer Alley, Louisiana: 85-mile industrial corridor with elevated cancer rates in Black communities.</li>"
    "<li>Executive Order 12898 (1994): required agencies to address environmental justice.</li></ul>",
    [("Environmental Justice","Fair treatment and meaningful involvement of all people regardless of race, income, or origin in environmental decisions."),
     ("Environmental Racism","Disproportionate siting of environmentally hazardous facilities in communities of color."),
     ("Flint Water Crisis","2014–present crisis: lead contamination from changed water source in Flint, MI, disproportionately affecting Black residents."),
     ("Cancer Alley","85-mile stretch along the Mississippi River in Louisiana with concentrated petrochemical plants and elevated cancer rates in predominantly Black communities."),
     ("Executive Order 12898","1994 presidential order requiring federal agencies to identify and address disproportionate environmental and health effects on minority and low-income populations.")],
    [("Environmental justice is defined as:",["Only about wilderness","*Fair treatment and meaningful involvement of all people regardless of race, color, income, or national origin in environmental matters","Only about pollution","Only about climate"],"Equity principle."),
     ("Studies have shown that hazardous waste facilities are disproportionately located in:",["Wealthy areas","*Minority and low-income communities (environmental racism)","Equal distribution","Only rural areas"],"Systematic pattern."),
     ("The landmark 1982 Warren County, NC protest was significant because it:",["Was about a park","*Was the first major environmental justice protest (opposing a PCB landfill in a predominantly Black community) — sparked the EJ movement","Was about air quality","Was about water"],"Birth of EJ movement."),
     ("The Flint, MI water crisis involved:",["Clean water switch","*Switching water sources to save money, which corroded pipes and leached lead into drinking water (primarily affecting Black residents)","Only a small problem","Natural contamination"],"Government failure."),
     ("Cancer Alley in Louisiana demonstrates:",["Equal exposure","*Environmental racism: concentrated petrochemical industries in a predominantly Black corridor → elevated cancer and respiratory disease rates","Only natural disease","Only occupational risk"],"Industrial corridor injustice."),
     ("Executive Order 12898 (1994) required:",["Nothing specific","*Federal agencies to identify and address disproportionately high environmental and health effects on minority and low-income populations","Only state action","Only research"],"Federal directive."),
     ("Environmental justice issues are not limited to race but also include:",["Only race","*Income level, indigenous status, immigrant communities, rural communities, and other marginalized groups","Only wealthy areas","Only one factor"],"Intersectionality."),
     ("NIMBY ('Not In My Back Yard') is related to EJ because:",["It's the same thing","*Wealthy, politically powerful communities successfully push unwanted facilities to less powerful communities","Everyone shares equally","NIMBY doesn't exist"],"Power dynamics."),
     ("Indigenous communities face environmental justice concerns including:",["No issues","*Natural resource extraction on their lands, contaminated water, broken treaties, and loss of cultural resources","Only cultural issues","Only economic issues"],"Indigenous EJ."),
     ("The intersection of environmental justice and climate change shows:",["No connection","*Climate impacts disproportionately affect low-income communities and communities of color (heat islands, flood zones, less access to adaptation resources)","Only global effects","Equal impacts"],"Climate justice."),
     ("Cumulative impacts refer to:",["Only single exposures","*The combined health effects of multiple environmental hazards in one community (air, water, soil, social stressors)","Only one pollutant","Only short-term effects"],"Multiple stressors compound."),
     ("Community-based participatory research in EJ involves:",["Only outside scientists","*Residents of affected communities as partners in designing and conducting research on environmental health threats","Only government research","Only corporate studies"],"Community empowerment."),
     ("Environmental gentrification occurs when:",["Nothing changes","*Environmental cleanup or green amenities raise property values, displacing the original community that suffered the pollution","Only poor people benefit","Only rich people suffer"],"Green displacement."),
     ("Title VI of the Civil Rights Act applies to EJ because:",["It's unrelated","*It prohibits discrimination in federally funded programs — EPA can investigate claims of environmental discrimination","Only about voting","Only about education"],"Civil rights + environment."),
     ("The 2021 Justice40 Initiative aims to:",["Only study issues","*Deliver 40% of benefits from federal climate and environment investments to disadvantaged communities","Only fund research","Only monitor pollution"],"Targeted investment."),
     ("Global environmental justice includes the concept that:",["All nations pollute equally","*Developing nations suffer climate impacts caused largely by developed nations' historical emissions (climate injustice)","Only local issues matter","Only one country is responsible"],"Global equity."),
     ("Health disparities in EJ communities include:",["No disparities","*Higher rates of asthma, cancer, lead poisoning, and other pollution-related diseases compared to wealthier, whiter communities","Only mental health","Only one disease"],"Documented health gaps."),
     ("The solution to environmental injustice requires:",["Only moving people","*Meaningful community participation in decisions, equitable enforcement of laws, investments in cleanup, and addressing root causes of inequality","Only lawsuits","Only compensation"],"Systemic change."),
     ("For AP, environmental justice questions require analyzing:",["Only definitions","*How race, income, and power affect distribution of environmental burdens and benefits with specific examples","Only one case study","Only federal policy"],"Analytical depth."),
     ("Environmental justice is fundamentally about:",["Only environment","*The intersection of environmental protection, civil rights, and social equity — environment and justice are inseparable","Only justice","Only policy"],"Two inseparable goals.")]
)
lessons[k]=v

# 8.5
k,v = build_lesson(8,5,"Case Studies: Policy Implementation",
    "<h3>Case Studies: Policy Implementation</h3>"
    "<h4>Success: Acid Rain Program</h4>"
    "<p>Clean Air Act cap-and-trade reduced SO₂ emissions ~90% from 1990 levels — ahead of schedule and under budget. Lakes and forests recovering.</p>"
    "<h4>Ongoing Challenge: Superfund</h4>"
    "<p>Over 1,300 sites on the National Priorities List. Cleanup slow and expensive; ~400 sites fully cleaned since 1980. Environmental justice concerns.</p>"
    "<h4>Controversial: ESA Implementation</h4>"
    "<p>Spotted owl vs. logging in Pacific Northwest. Species recovery success stories but habitat-economy conflicts persist.</p>",
    [("Acid Rain Program","Clean Air Act Title IV cap-and-trade that reduced SO₂ emissions ~90% — one of the most successful environmental regulations."),
     ("Superfund (NPL)","National Priorities List of ~1,300+ contaminated sites; cleanup has been slow and expensive since 1980."),
     ("Spotted Owl Controversy","Listing northern spotted owl under ESA led to logging restrictions in Pacific Northwest — economy vs. conservation debate."),
     ("Adaptive Management","Policy approach of 'learn by doing' — implementing, monitoring, and adjusting management strategies based on results."),
     ("Regulatory Effectiveness","Measured by whether laws achieve their environmental goals, at what cost, and with what distributional effects.")],
    [("The Acid Rain Program reduced SO₂ emissions by approximately:",["10%","50%","*~90% from 1990 levels (ahead of schedule and under budget)","25%"],"Dramatic success."),
     ("The Acid Rain Program succeeded because:",["It was voluntary","*Cap-and-trade allowed flexibility — companies found cheapest ways to reduce emissions; clear cap ensured total reductions","Only penalties were used","It was never enforced"],"Market-based success."),
     ("Acid rain damaged:",["Nothing","*Lakes (acidification killing fish), forests (nutrient leaching), and buildings/monuments (dissolving limestone)","Only buildings","Only one ecosystem"],"Wide-ranging damage."),
     ("Superfund has fully cleaned approximately _____ of 1,300+ sites since 1980.",["All of them","Only 10","*~400 sites (cleanup is slow, complex, and very expensive)","1,000"],"Slow progress."),
     ("Superfund cleanup is complicated by:",["Simple contamination","*Multiple responsible parties, complex contamination, high costs, community opposition, and environmental justice concerns","Only one factor","Only cost"],"Multi-faceted challenges."),
     ("The spotted owl controversy illustrates the tension between:",["Two bird species","*Endangered species protection (ESA) and economic interests (timber industry and jobs)","Only science","Only politics"],"Conservation vs. economy."),
     ("The ESA has been successful in that:",["No species recovered","*The majority of listed species are stable or improving (bald eagles, gray wolves, grizzly bears among recovery successes)","All species recovered","Only one species]"],"Evidence of effectiveness."),
     ("The Clean Water Act's success is measured by:",["No metrics","*Reduction in point-source pollution — but non-point source pollution and legacy contamination remain major challenges","Only one metric","Only cleanliness"],"Mixed results."),
     ("The Chesapeake Bay cleanup demonstrates:",["Quick fixes work","*The difficulty of addressing non-point source pollution from agriculture, development, and atmospheric deposition across multiple states","Only point-source issues","Only one state's problem"],"Multi-state, multi-source challenge."),
     ("The Montreal Protocol's implementation shows that phaseouts work when:",["Technology doesn't exist","*Affordable substitutes are available, there's industry cooperation, and developing nations receive financial and technical support","Only bans work","Only incentives work"],"Keys to success."),
     ("Environmental regulation's effect on the economy is generally:",["Devastating","*Modest overall costs with significant health and environmental benefits — often driving innovation (e.g., catalytic converters became a new industry)","Zero impact","Only positive"],"Benefits exceed costs."),
     ("The Clean Air Act's benefits have been estimated at _____ its costs.",["Less than","Equal to","*30× or more (trillions in health benefits vs. billions in compliance costs)","Twice"],"Enormous return."),
     ("Enforcement challenges for environmental laws include:",["No challenges","*Limited budgets, political pressure, difficulty monitoring non-point sources, and the revolving door between regulators and industry","Only money","Only politics"],"Systemic obstacles."),
     ("Adaptive management in environmental policy involves:",["Never changing","*Implementing policies, monitoring outcomes, and adjusting strategies based on what's working and what isn't","Only planning","Only studying"],"Learning by doing."),
     ("International cooperation in enforcement is needed because:",["Pollution stops at borders","*Pollution crosses borders, wildlife trafficking is global, and many environmental problems are transboundary","Only for climate","Only for oceans"],"Transboundary nature."),
     ("The Deepwater Horizon spill (2010) led to:",["No policy changes","*Strengthened offshore drilling regulations, $20+ billion in fines/cleanup, and highlighted gaps in oil spill preparedness","Only minor fines","Only one change"],"Disaster-driven reform."),
     ("Cost-effectiveness varies across environmental tools:",["All tools are equal","*Market-based tools (cap-and-trade, taxes) are often cheaper per unit of reduction than command-and-control regulations","Only regulations work","Only voluntary works"],"Tool selection matters."),
     ("Public participation in environmental decisions is important because:",["It slows things down","*It ensures affected communities have input, improves decisions with local knowledge, and strengthens legitimacy","It's unnecessary","Only experts should decide"],"Democratic governance."),
     ("For AP, policy implementation case studies require:",["Only names and dates","*Evaluating what worked, what didn't, comparing approaches, and applying lessons to new situations","Only success stories","Only failures"],"Critical evaluation."),
     ("The key lesson from these case studies is that environmental policy:",["Always works perfectly","*Is iterative — success depends on design, enforcement, funding, public support, and willingness to adapt based on results","Never works","Only works in the US"],"Continuous improvement.")]
)
lessons[k]=v

# 8.6
k,v = build_lesson(8,6,"AP Prep: Policy Analysis",
    "<h3>AP Prep: Policy Analysis</h3>"
    "<h4>FRQ Strategy</h4>"
    "<ul><li><b>Identify the problem:</b> What environmental issue is being addressed?</li>"
    "<li><b>Describe the policy:</b> What does the law/regulation do? Who enforces it?</li>"
    "<li><b>Evaluate effectiveness:</b> Has it achieved its goals? What evidence?</li>"
    "<li><b>Analyze trade-offs:</b> Economic costs vs. environmental/health benefits.</li>"
    "<li><b>Propose improvements:</b> How could the policy be strengthened or reformed?</li></ul>"
    "<h4>Key Comparisons</h4>"
    "<p>Command-and-control vs. market-based approaches. Federal vs. state vs. international. Point source vs. non-point source. Mitigation vs. adaptation.</p>",
    [("Command-and-Control Regulation","Government sets specific standards or technology requirements that regulated entities must meet."),
     ("Market-Based Approaches","Use economic incentives (taxes, cap-and-trade, subsidies) to achieve environmental goals at lower cost."),
     ("Cost-Benefit Analysis","Systematic comparison of the costs and benefits of a policy to determine if benefits justify costs."),
     ("Regulatory Approach Comparison","Command-and-control provides certainty of outcome; market-based provides cost-efficiency — often used together."),
     ("Policy Analysis Framework","Problem identification → policy description → effectiveness evaluation → trade-off analysis → improvement proposals.")],
    [("Command-and-control regulations specify:",["Only goals","*Specific standards, limits, or technologies that must be used (e.g., emission limits, required technology)","Only voluntary measures","Only economic incentives"],"Prescriptive approach."),
     ("Market-based approaches to environmental policy include:",["Only regulations","*Carbon taxes, cap-and-trade, subsidies for clean energy, and deposit-refund systems","Only fines","Only voluntary programs"],"Economic instruments."),
     ("An advantage of market-based approaches is:",["Less flexibility","*Greater cost-effectiveness — allows companies to find the cheapest way to meet environmental goals","Less certainty","More bureaucracy"],"Economic efficiency."),
     ("An advantage of command-and-control is:",["Lower cost","*Greater certainty that specific pollution levels or technology standards will be met","More flexibility","Less enforcement"],"Outcome certainty."),
     ("In policy analysis, students should first:",["Propose solutions","Evaluate effectiveness","*Identify the environmental problem being addressed","Skip to trade-offs"],"Start with the problem."),
     ("Cost-benefit analysis of environmental policy should include:",["Only direct costs","*Direct costs + indirect costs vs. environmental benefits + health benefits + ecosystem services (many benefits are hard to monetize)","Only monetary values","Only short-term costs"],"Comprehensive accounting."),
     ("The 'discount rate' in environmental economics affects policy because:",["It doesn't matter","*A high discount rate undervalues future benefits (like climate damage avoided), favoring short-term economic concerns over long-term environmental protection","It only affects interest rates","It only matters for banks"],"Present vs. future values."),
     ("Externalities are important in policy analysis because:",["They're included in prices","*Environmental costs (pollution, health damage) are not reflected in market prices — policies attempt to 'internalize' these external costs","They don't exist","They're already accounted for"],"Market failure correction."),
     ("The Tragedy of the Commons applies to environmental policy when:",["Resources are privately owned","*Shared resources (air, water, fisheries) are overexploited because individual users don't bear the full cost of degradation","Nothing is shared","The commons don't exist"],"Shared resource problem."),
     ("Federal vs. state environmental regulation involves trade-offs between:",["Only federal authority","*National consistency vs. state flexibility; federal baseline standards vs. state ability to set stricter requirements","Only state authority","No trade-offs"],"Federalism in environment."),
     ("Point-source pollution is easier to regulate than non-point source because:",["It's more dangerous","*It comes from identifiable discharge points (pipes, smokestacks) that can be monitored and permitted","It's less common","No difference"],"Identifiability."),
     ("Voluntary environmental programs (e.g., Energy Star) are:",["All that's needed","*Useful supplements to regulation but insufficient alone (typically only adopted by companies that benefit from compliance)","Useless","Identical to regulation"],"Complementary, not substitute."),
     ("Environmental policy often involves the Precautionary Principle, which means:",["Wait for certainty","*Take preventive action against threats of serious harm even without complete scientific certainty","Only act when certain","Never act preemptively"],"Err on the side of safety."),
     ("Equity in environmental policy analysis considers:",["Only cost","*Who bears the costs and who receives the benefits — ensuring policies don't disproportionately burden vulnerable communities","Only benefits","Only efficiency"],"Distributional justice."),
     ("Stakeholder analysis in environmental policy identifies:",["Only government","*All affected parties (industry, communities, environmental groups, government agencies) and their interests and influence","Only polluters","Only activists"],"Comprehensive impact assessment."),
     ("For AP FRQs on policy analysis, the best responses:",["List facts","*Identify the problem, describe the policy tool, evaluate with evidence, analyze trade-offs, and propose improvements","Only describe one law","Only give opinions"],"Structured response."),
     ("Comparing two environmental policies requires analyzing:",["Only their names","*Their goals, mechanisms, effectiveness, costs, equity impacts, and scalability","Only their costs","Only their dates"],"Multi-dimensional comparison."),
     ("Evidence of policy effectiveness includes:",["Only opinions","*Measured changes in pollution levels, species populations, health outcomes, or economic indicators before and after implementation","Only cost data","Only anecdotes"],"Data-driven evaluation."),
     ("For the AP exam, students should be prepared to:",["Only memorize laws","*Analyze unfamiliar policy scenarios using the analytical framework: problem → policy → evaluation → trade-offs → reform","Only name regulations","Only list dates"],"Applied analysis."),
     ("The most important insight in environmental policy analysis is:",["There are simple answers","*Environmental problems involve complex trade-offs among economic, ecological, equity, and political factors — good analysis weighs all dimensions","Only economics matters","Only science matters"],"Multidimensional thinking.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Environmental Science Unit 8: wrote {len(lessons)} lessons")
