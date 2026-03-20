#!/usr/bin/env python3
"""Anatomy Unit 6 – Cardiovascular System (8 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "anatomy_lessons.json")
COURSE = "Human Anatomy & Physiology"

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
k,v = build_lesson(6,1,"Structure of the Heart",
    "<h3>Structure of the Heart</h3>"
    "<h4>Chambers &amp; Valves</h4>"
    "<ul><li><b>4 chambers:</b> Right atrium (RA), right ventricle (RV), left atrium (LA), left ventricle (LV).</li>"
    "<li><b>AV valves:</b> Tricuspid (right) and mitral/bicuspid (left) — prevent backflow from ventricles to atria.</li>"
    "<li><b>Semilunar valves:</b> Pulmonary (RV → pulmonary artery) and aortic (LV → aorta).</li></ul>"
    "<h4>Layers &amp; Coverings</h4>"
    "<ul><li><b>Pericardium:</b> Protective sac. <b>Epicardium:</b> Outer. <b>Myocardium:</b> Thick muscular middle. <b>Endocardium:</b> Inner lining.</li></ul>"
    "<h4>Blood Flow Path</h4>"
    "<p>Body → vena cavae → RA → tricuspid → RV → pulmonary valve → lungs → pulmonary veins → LA → mitral → LV → aortic valve → aorta → body.</p>",
    [("Right Ventricle","Pumps deoxygenated blood to the lungs via the pulmonary artery."),
     ("Left Ventricle","Pumps oxygenated blood to the body via the aorta; has the thickest wall."),
     ("Tricuspid Valve","AV valve between the right atrium and right ventricle (3 cusps)."),
     ("Mitral (Bicuspid) Valve","AV valve between the left atrium and left ventricle (2 cusps)."),
     ("Myocardium","The thick muscular layer of the heart wall; responsible for contraction.")],
    [("How many chambers does the heart have?",["2","3","*4","5"],"RA, RV, LA, LV."),
     ("The left ventricle has the thickest wall because:",["It pumps to the lungs","*It pumps blood to the entire body against high systemic resistance","It stores blood","It has more valves"],"Systemic circulation requires greater force."),
     ("The tricuspid valve is located between:",["LA and LV","*RA and RV","RV and pulmonary artery","LV and aorta"],"Three-cusped valve on the right side."),
     ("The mitral (bicuspid) valve is between:",["RA and RV","*LA and LV","Aorta and LV","Pulmonary artery and RV"],"Two cusps, left side."),
     ("The pulmonary semilunar valve controls blood flow from:",["LV to aorta","*RV to pulmonary artery","RA to RV","LA to LV"],"Guards the exit to pulmonary circulation."),
     ("The aortic semilunar valve controls blood flow from:",["RV to pulmonary artery","*LV to aorta","RA to RV","LA to LV"],"Guards the exit to systemic circulation."),
     ("The correct blood flow path is:",["RA → LA → RV → LV","*RA → RV → lungs → LA → LV → body","LV → LA → RV → RA","Lungs → RA → RV → LA"],"Right side pumps to lungs, left to body."),
     ("The myocardium is the:",["Inner lining","Outer covering","*Thick muscular middle layer","Protective sac"],"Myocardium = contractile layer."),
     ("The endocardium:",["Is the outer layer","*Lines the interior of the heart chambers","Is the muscular layer","Surrounds the pericardium"],"Smooth inner lining."),
     ("The pericardium:",["Is the muscular layer","Produces blood","*Is the protective sac surrounding the heart","Is part of the lung"],"Fibrous and serous layers protect the heart."),
     ("Deoxygenated blood enters the right atrium via:",["Aorta","Pulmonary veins","*Superior and inferior vena cavae","Pulmonary artery"],"Venae cavae return blood from body."),
     ("Oxygenated blood enters the left atrium via:",["Vena cavae","*Pulmonary veins","Aorta","Coronary arteries"],"4 pulmonary veins carry O₂-rich blood from lungs."),
     ("The interventricular septum separates:",["The two atria","*The left and right ventricles","The heart and lungs","Arteries and veins"],"Muscular wall between ventricles."),
     ("Coronary arteries supply blood to:",["The lungs","The brain","*The heart muscle itself (myocardium)","The kidneys"],"Heart needs its own blood supply."),
     ("The coronary sinus returns:",["Oxygenated blood to the aorta","*Deoxygenated blood from the heart muscle to the right atrium","Blood to the lungs","CSF to the brain"],"Venous drainage of the myocardium."),
     ("Heart sounds ('lub-dub') are caused by:",["Blood flowing","Muscles contracting","*Closure of heart valves (S1 = AV valves, S2 = semilunar valves)","The pericardium"],"S1=AV close, S2=semilunar close."),
     ("A heart murmur may indicate:",["Normal function always","*Abnormal valve function (stenosis or regurgitation)","A healthy heart","Strong valves"],"Turbulent blood flow through abnormal valves."),
     ("The papillary muscles and chordae tendineae prevent:",["Blood from flowing forward","*AV valve leaflets from everting (prolapsing) into the atria during ventricular contraction","Semilunar valve closure","Heart enlargement"],"Anchor AV valve cusps."),
     ("The fossa ovalis is:",["A valve","*A remnant of the foramen ovale (fetal opening between atria)","A blood vessel","A nerve"],"Closes after birth."),
     ("Understanding heart anatomy is essential for:",["Nothing medical","*Diagnosing heart disease, planning surgeries, and understanding circulation","Only anatomy class","Only cardiologists"],"Foundation for all cardiovascular medicine.")]
)
lessons[k]=v

# 6.2
k,v = build_lesson(6,2,"Blood Vessels & Circulation",
    "<h3>Blood Vessels &amp; Circulation</h3>"
    "<h4>Vessel Types</h4>"
    "<ul><li><b>Arteries:</b> Thick walls, carry blood AWAY from the heart. Elastic (aorta) and muscular (distributing).</li>"
    "<li><b>Arterioles:</b> Small arteries that regulate blood flow to capillary beds.</li>"
    "<li><b>Capillaries:</b> Thin-walled (one cell thick), site of gas/nutrient/waste exchange.</li>"
    "<li><b>Venules → Veins:</b> Return blood to the heart. Thinner walls; valves prevent backflow.</li></ul>"
    "<h4>Circulatory Routes</h4>"
    "<p><b>Pulmonary:</b> RV → lungs → LA. <b>Systemic:</b> LV → body → RA. <b>Hepatic portal:</b> GI tract → liver → hepatic veins → IVC.</p>",
    [("Artery","Thick-walled vessel carrying blood away from the heart; high pressure."),
     ("Capillary","Thinnest vessel (one endothelial cell thick); site of exchange between blood and tissues."),
     ("Vein","Thin-walled vessel carrying blood toward the heart; has valves to prevent backflow."),
     ("Pulmonary Circulation","RV → pulmonary artery → lungs (gas exchange) → pulmonary veins → LA."),
     ("Hepatic Portal System","Venous blood from GI tract goes to the liver for processing before returning to the heart.")],
    [("Arteries carry blood:",["Toward the heart","*Away from the heart","Only oxygenated blood","Only to the lungs"],"Arteries = away."),
     ("Veins carry blood:",["Away from the heart","*Toward the heart","Only deoxygenated blood","Only from the lungs"],"Veins = toward heart."),
     ("Capillaries are the site of:",["Blood storage","*Gas, nutrient, and waste exchange between blood and tissues","Hormone production","Blood cell production"],"One cell thick = exchange surface."),
     ("Arteries have thicker walls than veins because:",["They carry more blood","*They must withstand higher blood pressure","They contain valves","They are longer"],"High-pressure system."),
     ("Veins have valves to:",["Increase pressure","*Prevent backflow of blood (especially against gravity in legs)","Speed blood flow","Produce blood cells"],"One-way valves assist venous return."),
     ("The largest artery is the:",["Pulmonary artery","Vena cava","*Aorta","Femoral artery"],"Aorta exits from the LV."),
     ("Arterioles regulate:",["Heart rate","*Blood flow to capillary beds (via smooth muscle constriction/dilation)","Blood cell production","Hormone release"],"Arterioles = resistance vessels."),
     ("In the pulmonary circuit, the pulmonary arteries carry:",["Oxygenated blood","*Deoxygenated blood to the lungs","Blood to the kidneys","Blood to the brain"],"Exception: pulmonary arteries carry deoxy blood."),
     ("Pulmonary veins carry:",["Deoxygenated blood","*Oxygenated blood from the lungs to the left atrium","Blood to the liver","Blood to the brain"],"Exception: pulmonary veins carry oxy blood."),
     ("The hepatic portal system carries blood from:",["Heart to liver","*GI tract to liver for processing","Liver to heart directly","Kidneys to liver"],"Nutrient-rich blood is processed by the liver first."),
     ("Vasoconstriction causes:",["*Narrowing of blood vessels → increased blood pressure","Widening of vessels","Lower BP","More blood flow"],"Smooth muscle contraction narrows lumen."),
     ("Vasodilation causes:",["Increased BP","*Widening of blood vessels → decreased blood pressure and increased local blood flow","Vessel constriction","Reduced blood flow"],"Smooth muscle relaxation widens lumen."),
     ("Atherosclerosis is:",["A normal finding","*Buildup of plaque (fats, cholesterol) in artery walls, narrowing the lumen","A vein disease","A valve disease"],"Major cause of heart attacks and strokes."),
     ("An aneurysm is:",["A clot","*An abnormal bulging of a weakened arterial wall","A vein valve failure","Normal vessel expansion"],"Risk of rupture → hemorrhage."),
     ("Deep vein thrombosis (DVT) is:",["An arterial clot","*A blood clot in a deep vein (usually leg) — risk of pulmonary embolism","Normal leg swelling","A skin condition"],"DVT can dislodge → pulmonary embolism."),
     ("Varicose veins result from:",["Strong valves","*Incompetent vein valves allowing blood pooling","Arterial disease","Heart failure"],"Failed valves → blood pools → veins enlarge."),
     ("The tunica intima is the:",["Outer layer","*Innermost layer (endothelium) of a blood vessel","Middle layer","Valve layer"],"Smooth inner lining of all vessels."),
     ("The tunica media is the:",["Inner layer","*Middle layer (smooth muscle and elastic tissue)","Outer layer","Valve layer"],"Responsible for vasoconstriction/dilation."),
     ("The tunica adventitia (externa) is the:",["Inner layer","Middle layer","*Outermost layer (connective tissue)","Valve layer"],"Anchors vessel to surrounding tissue."),
     ("Blood returns to the heart from the legs with help from:",["Gravity alone","*The skeletal muscle pump and venous valves","Arterial pressure","The liver"],"Muscle contraction squeezes veins.")]
)
lessons[k]=v

# 6.3
k,v = build_lesson(6,3,"Blood Composition & Function",
    "<h3>Blood Composition &amp; Function</h3>"
    "<h4>Plasma (~55%)</h4>"
    "<p>Water (~92%), proteins (albumin, globulins, fibrinogen), electrolytes, nutrients, waste, gases, hormones.</p>"
    "<h4>Formed Elements (~45%)</h4>"
    "<ul><li><b>Red blood cells (RBCs/erythrocytes):</b> Carry O₂ (hemoglobin); no nucleus; ~4.5–5.5 million/µL.</li>"
    "<li><b>White blood cells (WBCs/leukocytes):</b> Immune defense; 5,000–10,000/µL. Types: neutrophils, lymphocytes, monocytes, eosinophils, basophils.</li>"
    "<li><b>Platelets (thrombocytes):</b> Cell fragments; essential for clotting; 150,000–400,000/µL.</li></ul>",
    [("Plasma","Liquid component of blood (~55%); water, proteins, electrolytes, nutrients, waste."),
     ("Erythrocyte (RBC)","Red blood cell; contains hemoglobin for O₂ transport; no nucleus."),
     ("Leukocyte (WBC)","White blood cell; immune defense. Types: neutrophils, lymphocytes, monocytes, eosinophils, basophils."),
     ("Platelet","Cell fragment from megakaryocytes; essential for blood clotting (hemostasis)."),
     ("Hemoglobin","Iron-containing protein in RBCs that binds and transports oxygen.")],
    [("Blood plasma makes up approximately _____ of blood volume.",["45%","30%","*55%","70%"],"55% plasma, 45% formed elements."),
     ("The hematocrit measures:",["WBC count","*The percentage of blood volume occupied by RBCs (normally ~38-50%)","Plasma proteins","Platelet count"],"Packed cell volume."),
     ("Hemoglobin's primary function is to:",["Fight infection","*Transport oxygen (and some CO₂)","Clot blood","Produce hormones"],"Each Hb binds up to 4 O₂ molecules."),
     ("RBCs lack a nucleus so that:",["They die immediately","*They can carry more hemoglobin (maximizes O₂ transport)","They can divide","They are stronger"],"No nucleus = more room for Hb."),
     ("RBCs are produced in the:",["Liver only","*Red bone marrow (erythropoiesis)","Spleen","Lymph nodes"],"Bone marrow = site of hematopoiesis."),
     ("Erythropoietin (EPO) stimulates:",["WBC production","*RBC production (released by kidneys in response to low O₂)","Platelet production","Plasma production"],"Low O₂ → kidneys release EPO → more RBCs."),
     ("The most abundant WBC type is the:",["Lymphocyte","*Neutrophil","Monocyte","Eosinophil"],"Neutrophils: 60-70% of WBCs."),
     ("Neutrophils are the first responders to:",["Viral infections","*Bacterial infections (phagocytosis)","Parasites","Allergies"],"First line of cellular defense."),
     ("Lymphocytes include:",["Only T cells","*T cells, B cells, and natural killer (NK) cells","Only neutrophils","Only monocytes"],"Adaptive immunity."),
     ("Platelets function in:",["Gas transport","Immune defense","*Hemostasis (blood clotting)","Nutrient transport"],"Form platelet plug → initiate coagulation."),
     ("Albumin, the most abundant plasma protein, maintains:",["Immunity","*Osmotic pressure (prevents fluid leaking out of capillaries)","Blood clotting","O₂ transport"],"Colloid osmotic pressure."),
     ("Fibrinogen is converted to fibrin during:",["Digestion","*Blood clotting (forms the mesh that stabilizes a clot)","Immune response","O₂ transport"],"Final step: fibrinogen → fibrin mesh."),
     ("Anemia is:",["Excess WBCs","*A decrease in RBCs or hemoglobin, reducing O₂-carrying capacity","Excess platelets","Normal"],"Fatigue, pallor, shortness of breath."),
     ("Sickle cell disease involves:",["Normal RBCs","*Abnormal hemoglobin (HbS) causing RBCs to become sickle-shaped","Loss of WBCs","Excess platelets"],"HbS polymerizes under low O₂."),
     ("Leukemia is:",["An RBC disorder","*Cancer of WBCs (abnormal proliferation of leukocytes)","A platelet disorder","A plasma disorder"],"Cancerous WBCs crowd out normal cells."),
     ("Thrombocytopenia means:",["Excess platelets","*Low platelet count → increased bleeding risk","Excess WBCs","Low RBCs"],"Thrombo=platelet, -penia=low."),
     ("Blood type is determined by:",["Plasma proteins","*Antigens on the surface of RBCs (A, B, AB, O and Rh factor)","WBC type","Platelet count"],"ABO and Rh blood group systems."),
     ("Universal donor blood type is:",["AB+","A+","*O− (no A, B, or Rh antigens)","B−"],"O- can be given to anyone in emergencies."),
     ("Universal recipient blood type is:",["O−","*AB+ (has all antigens, so no antibodies to reject donor blood)","A+","B+"],"AB+ can receive from all types."),
     ("A complete blood count (CBC) is important because it:",["Is not useful","*Provides information about RBCs, WBCs, and platelets — essential for diagnosing many conditions","Only measures plasma","Only checks for cancer"],"Most commonly ordered blood test.")]
)
lessons[k]=v

# 6.4
k,v = build_lesson(6,4,"Cardiac Cycle & Heartbeat Regulation",
    "<h3>Cardiac Cycle &amp; Heartbeat Regulation</h3>"
    "<h4>Cardiac Cycle</h4>"
    "<p><b>Systole:</b> Contraction phase (ventricles pump blood). <b>Diastole:</b> Relaxation phase (ventricles fill).</p>"
    "<h4>Conduction System</h4>"
    "<ul><li><b>SA node (sinoatrial):</b> 'Pacemaker'; initiates each heartbeat (~60-100 bpm).</li>"
    "<li><b>AV node:</b> Delays signal briefly → ensures atria finish emptying.</li>"
    "<li><b>Bundle of His → bundle branches → Purkinje fibers:</b> Conduct impulse rapidly through ventricles.</li></ul>"
    "<h4>ECG/EKG</h4>"
    "<p>P wave = atrial depolarization. QRS complex = ventricular depolarization. T wave = ventricular repolarization.</p>",
    [("Systole","Contraction phase; ventricles eject blood into arteries."),
     ("Diastole","Relaxation phase; ventricles fill with blood from atria."),
     ("SA Node","Sinoatrial node; the heart's natural pacemaker (sets the rhythm)."),
     ("AV Node","Atrioventricular node; delays the impulse so atria contract before ventricles."),
     ("ECG (EKG)","Electrocardiogram; records electrical activity: P wave, QRS complex, T wave.")],
    [("Systole refers to:",["Heart relaxation","*Heart contraction (ventricles pumping blood)","Heart arrest","Heart enlargement"],"Systole = squeeze."),
     ("Diastole refers to:",["Heart contraction","*Heart relaxation (ventricles filling with blood)","Heart arrest","Heart murmur"],"Diastole = fill."),
     ("The SA node is called the pacemaker because it:",["Is artificial","*Initiates each heartbeat at a rate of ~60-100 bpm","Is in the ventricle","Responds to conscious control"],"Intrinsic pacemaker of the heart."),
     ("The AV node's main role is to:",["Initiate heartbeat","*Delay the impulse briefly so atria empty before ventricles contract","Speed up conduction","Produce blood cells"],"Brief delay = atria finish before ventricles start."),
     ("The Bundle of His conducts impulses from:",["SA node to atria","*AV node to the ventricular septum (then to bundle branches)","Ventricles to atria","Brain to heart"],"Pathway from AV node to ventricles."),
     ("Purkinje fibers rapidly spread the impulse through:",["The atria","*The ventricular walls (causing synchronized ventricular contraction)","The SA node","The AV node"],"Fast conduction ensures efficient pumping."),
     ("On an ECG, the P wave represents:",["Ventricular contraction","*Atrial depolarization (atrial contraction)","Ventricular repolarization","Heart at rest"],"P = atrial electrical activity."),
     ("The QRS complex represents:",["Atrial depolarization","*Ventricular depolarization (ventricular contraction)","Atrial repolarization","Resting heart"],"Large because ventricles are large."),
     ("The T wave represents:",["Atrial depolarization","Atrial repolarization","*Ventricular repolarization (ventricles recovering)","Ventricular contraction"],"T = ventricles resetting."),
     ("Normal resting heart rate is:",["20-40 bpm","*60-100 bpm","120-160 bpm","200+ bpm"],"Normal adult resting HR."),
     ("Cardiac output (CO) equals:",["HR only","*Heart rate × stroke volume (HR × SV)","Blood pressure × resistance","SV only"],"CO = amount of blood pumped per minute."),
     ("Stroke volume is:",["Total blood pumped per minute","*Volume of blood pumped by one ventricle per beat (~70 mL)","Heart rate","Blood pressure"],"SV = end-diastolic volume − end-systolic volume."),
     ("Bradycardia is a heart rate:",["Above 100 bpm","*Below 60 bpm","Between 60-100 bpm","Exactly 72 bpm"],"Slow heart rate."),
     ("Tachycardia is a heart rate:",["Below 60 bpm","*Above 100 bpm","Between 60-100 bpm","Exactly 60 bpm"],"Fast heart rate."),
     ("Atrial fibrillation (AFib) is:",["Normal heart rhythm","*Chaotic, irregular atrial electrical activity → irregular ventricular response","A stopped heart","A valve problem"],"Most common sustained arrhythmia."),
     ("Ventricular fibrillation (VFib) is:",["A minor arrhythmia","*A life-threatening arrhythmia (no effective pumping) → cardiac arrest","Normal finding","Slow heart rate"],"VFib = medical emergency needing defibrillation."),
     ("The parasympathetic nervous system _____ heart rate via the vagus nerve.",["Increases","*Decreases","Has no effect on","Stops"],"Vagal tone slows the heart."),
     ("The sympathetic nervous system _____ heart rate.",["Decreases","*Increases","Has no effect on","Stops"],"Fight-or-flight → faster HR."),
     ("Cardiac muscle is unique because it has:",["No striations","*Intercalated discs (gap junctions allowing synchronized contraction)","Voluntary control","No blood supply"],"Intercalated discs = electrical syncytium."),
     ("Understanding the cardiac cycle and ECG is essential for:",["Nothing","*Diagnosing arrhythmias, heart disease, and guiding emergency treatment","Only cardiologists","Only anatomy class"],"ECG is a fundamental clinical tool.")]
)
lessons[k]=v

# 6.5
k,v = build_lesson(6,5,"Blood Pressure & Homeostasis",
    "<h3>Blood Pressure &amp; Homeostasis</h3>"
    "<h4>Blood Pressure Basics</h4>"
    "<p><b>Systolic pressure:</b> Pressure during ventricular contraction (~120 mmHg). <b>Diastolic:</b> Pressure during relaxation (~80 mmHg). Normal = 120/80.</p>"
    "<h4>Regulation</h4>"
    "<ul><li><b>Short-term (neural):</b> Baroreceptors in carotid sinus/aortic arch → ANS adjusts HR and vessel diameter.</li>"
    "<li><b>Long-term (renal/hormonal):</b> RAAS system, ADH, ANP — regulate blood volume.</li></ul>"
    "<h4>Hypertension</h4>"
    "<p>Persistently elevated BP (≥130/80). Major risk for heart attack, stroke, kidney disease.</p>",
    [("Systolic Pressure","Peak pressure during ventricular contraction (top number); normal ~120 mmHg."),
     ("Diastolic Pressure","Lowest pressure during ventricular relaxation (bottom number); normal ~80 mmHg."),
     ("Baroreceptors","Pressure sensors in carotid sinus and aortic arch; detect BP changes for short-term regulation."),
     ("RAAS","Renin-Angiotensin-Aldosterone System; long-term BP regulation via blood volume control."),
     ("Hypertension","Chronically elevated blood pressure (≥130/80); 'silent killer'; major cardiovascular risk factor.")],
    [("Normal blood pressure is approximately:",["140/90","*120/80 mmHg","100/60","160/100"],"120 systolic / 80 diastolic."),
     ("Systolic pressure measures pressure during:",["Ventricular relaxation","*Ventricular contraction","Atrial filling","Sleep"],"Systole = contraction."),
     ("Diastolic pressure measures pressure during:",["Ventricular contraction","*Ventricular relaxation","Exercise","Atrial contraction"],"Diastole = relaxation."),
     ("Baroreceptors detect:",["Blood oxygen","*Changes in blood pressure (stretch of vessel walls)","Temperature","Glucose levels"],"Pressure sensors."),
     ("When baroreceptors detect high BP, the response is:",["Increased HR","*Decreased HR and vasodilation (parasympathetic activation)","No response","Increased vasoconstriction"],"Lower BP back to normal."),
     ("The RAAS system is activated by:",["High BP","*Low blood pressure (kidneys release renin)","High glucose","High calcium"],"Low BP → renin → angiotensin II → aldosterone."),
     ("Angiotensin II causes:",["Vasodilation","*Potent vasoconstriction and stimulates aldosterone release → ↑BP","Lower BP","Increased urination"],"Powerful vasoconstrictor."),
     ("Aldosterone increases BP by:",["Dilating vessels","*Causing kidneys to retain sodium and water → ↑blood volume","Decreasing HR","Reducing blood volume"],"Na⁺/H₂O retention → volume expansion."),
     ("ADH (vasopressin) increases BP by:",["Dilating vessels","*Causing kidneys to retain water → ↑blood volume","Increasing urine output","Reducing HR"],"Water retention."),
     ("ANP (atrial natriuretic peptide) is released when:",["BP is low","*Atria are stretched (high blood volume) → promotes sodium/water excretion → ↓BP","Heart rate is low","Dehydration occurs"],"Counter-regulatory to RAAS."),
     ("Hypertension is defined as BP consistently at or above:",["120/80","*130/80 mmHg","140/90","160/100"],"Current guidelines: ≥130/80."),
     ("Hypertension is called the 'silent killer' because:",["It's not dangerous","*It often has no symptoms until serious damage occurs (heart, brain, kidneys)","It's always detected early","It causes pain"],"Asymptomatically damages organs."),
     ("Risk factors for hypertension include:",["Only genetics","*Obesity, high sodium diet, sedentary lifestyle, smoking, genetics, and stress","Only age","Only stress"],"Multifactorial."),
     ("Untreated hypertension can lead to:",["No complications","*Heart failure, stroke, kidney disease, and retinopathy","Only headaches","Only dizziness"],"End-organ damage."),
     ("ACE inhibitors treat hypertension by:",["Increasing angiotensin II","*Blocking conversion of angiotensin I to angiotensin II → vasodilation → ↓BP","Increasing HR","Increasing salt retention"],"Block the angiotensin-converting enzyme."),
     ("Hypotension (low BP) can cause:",["Hypertension","*Dizziness, fainting (syncope), and organ underperfusion","No symptoms ever","High blood sugar"],"Insufficient blood flow to brain."),
     ("Orthostatic hypotension is:",["High BP when standing","*A sudden BP drop when standing up (gravity pools blood in legs)","Normal BP change","Chronic hypertension"],"Common in elderly and dehydrated patients."),
     ("Mean arterial pressure (MAP) is important because it:",["Is irrelevant","*Reflects the average pressure driving blood to organs (must stay above ~60 mmHg)","Only matters in surgery","Is the same as systolic"],"MAP ≈ diastolic + 1/3(systolic − diastolic)."),
     ("Lifestyle modifications for hypertension include:",["None","*DASH diet (low sodium), regular exercise, weight loss, limiting alcohol, stress management","Only medication","Only surgery"],"First-line treatment approach."),
     ("Understanding BP regulation is essential because:",["It's not important","*Hypertension is the leading modifiable risk factor for cardiovascular disease worldwide","Only for cardiologists","Only for research"],"Global health priority.")]
)
lessons[k]=v

# 6.6
k,v = build_lesson(6,6,"Disorders of the Circulatory System",
    "<h3>Disorders of the Circulatory System</h3>"
    "<ul><li><b>Coronary artery disease (CAD):</b> Atherosclerosis of coronary arteries → angina, myocardial infarction (heart attack).</li>"
    "<li><b>Heart failure:</b> Heart can't pump effectively; systolic (reduced ejection fraction) or diastolic (preserved EF).</li>"
    "<li><b>Valvular disease:</b> Stenosis (narrowing) or regurgitation (leaking).</li>"
    "<li><b>Peripheral artery disease (PAD):</b> Atherosclerosis in limb arteries → claudication.</li>"
    "<li><b>Aneurysm:</b> Weakened arterial wall bulges → risk of rupture.</li></ul>",
    [("Coronary Artery Disease","Atherosclerosis of coronary arteries; can cause angina or heart attack (MI)."),
     ("Myocardial Infarction (MI)","Heart attack; death of heart muscle due to blocked coronary artery."),
     ("Heart Failure","Heart unable to pump blood effectively; fluid backs up (edema, dyspnea)."),
     ("Angina Pectoris","Chest pain from reduced blood flow to the myocardium (ischemia without infarction)."),
     ("Peripheral Artery Disease","Atherosclerosis in peripheral arteries; causes leg pain (claudication) with walking.")],
    [("Coronary artery disease is caused primarily by:",["Genetics alone","*Atherosclerosis (plaque buildup) in the coronary arteries","Valve disease","Infection"],"Plaque narrows coronary lumens."),
     ("A myocardial infarction occurs when:",["The heart slows","*A coronary artery is blocked, causing death of heart muscle tissue","Valves fail","BP drops"],"Blocked artery → ischemia → necrosis."),
     ("Symptoms of an MI include:",["Only fatigue","*Chest pain/pressure, shortness of breath, sweating, nausea, arm/jaw pain","Only headache","Only dizziness"],"Classic presentation, though can be atypical."),
     ("Treatment for an acute MI includes:",["Nothing","*Reperfusion therapy (angioplasty/stent or thrombolytics), aspirin, and supportive care","Only bed rest","Only oxygen"],"Restore blood flow ASAP."),
     ("Heart failure means:",["The heart stops completely","*The heart cannot pump efficiently enough to meet the body's needs","A heart attack","An arrhythmia"],"Pump failure → fluid congestion."),
     ("Symptoms of heart failure include:",["No symptoms","*Edema, shortness of breath, fatigue, reduced exercise tolerance","Only chest pain","Only high BP"],"Fluid backs up in lungs and periphery."),
     ("Angina pectoris is:",["A heart attack","*Chest pain from temporary myocardial ischemia (reduced blood flow, no tissue death)","A valve disease","An arrhythmia"],"Warning sign; reversible ischemia."),
     ("Peripheral artery disease causes:",["Arm swelling","*Leg pain with walking (claudication) due to reduced arterial blood flow","Chest pain","Headaches"],"Atherosclerosis in leg arteries."),
     ("An aortic aneurysm:",["Is harmless","*Is a dangerous bulging of the aortic wall that can rupture (life-threatening hemorrhage)","Always causes symptoms","Only affects young people"],"Rupture = surgical emergency."),
     ("Valvular stenosis means:",["A leaking valve","*Narrowing of a valve opening (restricts blood flow)","A normal valve","A missing valve"],"Stenosis = narrowing."),
     ("Valvular regurgitation means:",["A blocked valve","*A leaking valve (blood flows backward)","A normal finding","Valve calcification"],"Incompetent valve → backflow."),
     ("Risk factors for CAD include:",["None","*Hypertension, high cholesterol, smoking, diabetes, obesity, family history","Only genetics","Only age"],"Multiple modifiable and non-modifiable risk factors."),
     ("LDL cholesterol is called 'bad' cholesterol because:",["It's harmless","*High LDL contributes to plaque buildup in arteries","It clears plaque","It raises HDL"],"LDL deposits cholesterol in vessel walls."),
     ("HDL cholesterol is called 'good' cholesterol because:",["It causes plaque","*It helps remove cholesterol from arteries (reverse cholesterol transport)","It has no function","It raises LDL"],"HDL is protective."),
     ("Statin drugs work by:",["Increasing cholesterol","*Inhibiting HMG-CoA reductase → reducing LDL cholesterol production in the liver","Raising HDL only","Lowering blood sugar"],"Lower LDL → reduce CAD risk."),
     ("Cardiac catheterization can:",["Only measure BP","*Visualize coronary artery blockages and allow intervention (angioplasty, stent placement)","Only measure HR","Replace valves only"],"Diagnostic and therapeutic."),
     ("A pacemaker is used to treat:",["Heart failure","*Bradycardia or certain arrhythmias (regulates heart rhythm electrically)","Hypertension","Valve disease"],"Electronic device that paces the heart."),
     ("Heart valve replacement may be needed for:",["Normal valves","*Severe stenosis or regurgitation that cannot be managed medically","Mild murmurs","Hypertension"],"Mechanical or biological valve prostheses."),
     ("Prevention of cardiovascular disease focuses on:",["Nothing","*Healthy diet, exercise, not smoking, managing BP/cholesterol/diabetes, and regular checkups","Only medication","Only genetics"],"Lifestyle is the foundation of prevention."),
     ("Cardiovascular disease is the _____ cause of death worldwide.",["Least common","*Leading (number one)","Fifth","Tenth"],"CVD = #1 killer globally.")]
)
lessons[k]=v

# 6.7
k,v = build_lesson(6,7,"Case Studies in Cardiovascular Health",
    "<h3>Case Studies in Cardiovascular Health</h3>"
    "<h4>Case 1: Acute MI</h4>"
    "<p>A 62-year-old male with chest pain radiating to left arm, diaphoresis, ECG showing ST elevation in leads II, III, aVF. Troponin elevated. Diagnosis: inferior STEMI. Treatment: emergent PCI (percutaneous coronary intervention).</p>"
    "<h4>Case 2: Congestive Heart Failure</h4>"
    "<p>A 70-year-old with progressive dyspnea, pedal edema, and pulmonary crackles. Echocardiogram shows ejection fraction 25%. Diagnosis: systolic heart failure. Management: ACE inhibitor, beta-blocker, diuretic.</p>"
    "<h4>Case 3: Hypertensive Emergency</h4>"
    "<p>BP 220/130 with headache and blurred vision. Requires IV antihypertensives with careful BP reduction.</p>",
    [("STEMI","ST-Elevation Myocardial Infarction; complete coronary artery blockage requiring emergent reperfusion."),
     ("Troponin","Cardiac protein released when heart muscle is damaged; key biomarker for MI."),
     ("Ejection Fraction (EF)","% of blood ejected per beat; normal ~55-70%. Low EF = systolic heart failure."),
     ("PCI","Percutaneous Coronary Intervention; catheter-based procedure to open blocked coronary arteries (angioplasty/stent)."),
     ("Hypertensive Emergency","Severely elevated BP with acute end-organ damage; requires immediate treatment.")],
    [("ST elevation on an ECG indicates:",["Normal heart","*Acute, complete coronary artery occlusion (STEMI)","A slow heart rate","A valve problem"],"ST elevation = active muscle injury."),
     ("Elevated troponin levels indicate:",["Normal heart health","*Myocardial damage (heart muscle cell death releasing troponin)","Liver disease","Kidney disease"],"Highly specific cardiac biomarker."),
     ("A normal ejection fraction is approximately:",["25%","40%","*55-70%","90%"],"Normal heart ejects 55-70% of ventricular volume per beat."),
     ("In the MI case, emergent PCI involves:",["Open heart surgery","*Inserting a catheter to open the blocked artery with a balloon and placing a stent","Medication only","Transplant"],"Restores blood flow quickly."),
     ("In the heart failure case, EF of 25% indicates:",["Normal function","*Severe systolic dysfunction (reduced pumping ability)","Mild disease","No disease"],"25% is significantly below normal."),
     ("ACE inhibitors in heart failure:",["Are harmful","*Reduce afterload, prevent remodeling, and improve survival","Only lower BP","Have no cardiac effect"],"Cornerstone of HF management."),
     ("Diuretics in heart failure help by:",["Increasing blood volume","*Reducing fluid overload (edema and pulmonary congestion)","Increasing heart strength","Raising BP"],"Remove excess fluid."),
     ("Dyspnea in heart failure is caused by:",["Anxiety","*Fluid backing up into the lungs (pulmonary congestion)","Anemia only","Asthma"],"Left-sided failure → pulmonary edema."),
     ("Pedal edema in heart failure is caused by:",["Poor diet","*Right-sided failure (blood backs up → fluid leaks into tissues)","Kidney stones","Infection"],"Fluid retention in dependent areas."),
     ("A hypertensive emergency requires:",["Oral medication at home","*IV antihypertensives with careful, controlled BP reduction","No treatment","Bed rest only"],"Too-rapid reduction can cause stroke."),
     ("In the MI case, aspirin is given to:",["Reduce pain only","*Inhibit platelet aggregation (prevent further clot formation)","Lower cholesterol","Reduce fever"],"Antiplatelet therapy."),
     ("After an MI, long-term medications typically include:",["Nothing","*Aspirin, statin, beta-blocker, and ACE inhibitor","Only aspirin","Only a statin"],"Secondary prevention."),
     ("B-type natriuretic peptide (BNP) is elevated in:",["Normal health","*Heart failure (released by stretched ventricles)","MI only","Hypertension only"],"BNP/NT-proBNP = HF biomarker."),
     ("Cardiac rehabilitation after MI includes:",["Complete rest forever","*Supervised exercise, education, risk factor modification, and psychological support","Only medication","Only surgery"],"Comprehensive recovery program."),
     ("Early recognition of MI symptoms is critical because:",["MI is not serious","*Earlier treatment = more heart muscle saved ('time is muscle')","Symptoms always resolve","Treatment can wait"],"Minutes matter."),
     ("In heart failure management, daily weight monitoring helps detect:",["Nothing","*Fluid retention early (sudden weight gain = fluid accumulation)","Muscle loss","Fat gain"],">2 lbs/day = call physician."),
     ("Echocardiography is used to:",["Measure BP","*Assess heart structure and function (chambers, valves, EF) using ultrasound","Check blood sugar","Test lungs"],"Non-invasive cardiac imaging."),
     ("The case studies illustrate that cardiovascular emergencies:",["Are rare","*Require rapid diagnosis, immediate intervention, and long-term management","Always resolve spontaneously","Only need medication"],"Time-sensitive, multifaceted care."),
     ("Risk factor modification after a cardiac event is important because:",["It doesn't help","*It reduces the chance of future events (secondary prevention)","Only medication matters","Genetics overrides everything"],"Lifestyle changes + medication reduce recurrence."),
     ("Interdisciplinary care for cardiac patients involves:",["Only cardiologists","*Cardiologists, nurses, pharmacists, dietitians, rehabilitation specialists, and mental health professionals","Only surgeons","Only the patient"],"Team-based approach improves outcomes.")]
)
lessons[k]=v

# 6.8
k,v = build_lesson(6,8,"AP Prep: ECG Interpretation",
    "<h3>AP Prep: ECG Interpretation</h3>"
    "<h4>ECG Waveforms Review</h4>"
    "<ul><li><b>P wave:</b> Atrial depolarization (atrial contraction).</li>"
    "<li><b>PR interval:</b> Time from atrial depolarization to ventricular depolarization (0.12–0.20 s).</li>"
    "<li><b>QRS complex:</b> Ventricular depolarization (0.06–0.10 s).</li>"
    "<li><b>T wave:</b> Ventricular repolarization.</li>"
    "<li><b>QT interval:</b> Total ventricular electrical activity.</li></ul>"
    "<h4>Common Findings</h4>"
    "<p>Normal sinus rhythm, sinus bradycardia, sinus tachycardia, atrial fibrillation (no P waves, irregular), ST elevation (MI), heart block.</p>",
    [("P Wave","Atrial depolarization; should precede every QRS in normal sinus rhythm."),
     ("PR Interval","Time from start of P to start of QRS (0.12-0.20 s); prolonged in heart block."),
     ("QRS Complex","Ventricular depolarization; normally 0.06-0.10 s wide."),
     ("ST Segment","Between QRS and T wave; elevation or depression indicates ischemia/injury."),
     ("Atrial Fibrillation","Irregular rhythm with no identifiable P waves; atria quiver instead of contracting.")],
    [("The P wave on an ECG represents:",["Ventricular contraction","*Atrial depolarization","Ventricular relaxation","Heart failure"],"P = atria depolarize."),
     ("A normal PR interval is:",["0.04-0.08 s","*0.12-0.20 s","0.30-0.40 s","0.50-0.60 s"],"Represents conduction through AV node."),
     ("A prolonged PR interval (>0.20 s) suggests:",["Normal conduction","*First-degree AV block (delayed AV conduction)","Atrial fibrillation","Ventricular tachycardia"],"AV node conducts slowly."),
     ("The QRS complex represents:",["Atrial activity","*Ventricular depolarization","Atrial repolarization","Valve closure"],"Largest deflection on ECG."),
     ("A wide QRS (>0.12 s) may indicate:",["Normal conduction","*Bundle branch block or ventricular origin of the rhythm","Fast heart rate","Atrial fibrillation"],"Abnormal ventricular conduction."),
     ("The T wave represents:",["Atrial depolarization","*Ventricular repolarization","Atrial repolarization","Ventricular depolarization"],"T = ventricles resetting."),
     ("ST elevation on an ECG suggests:",["Normal finding","*Acute myocardial injury (STEMI)","Bradycardia","Atrial fibrillation"],"ST elevation = urgent."),
     ("ST depression may indicate:",["Normal","*Myocardial ischemia (reduced blood flow without complete blockage)","MI","Normal variant"],"Ischemia without infarction."),
     ("In normal sinus rhythm:",["There are no P waves","*Each P wave is followed by a QRS, at a regular rate of 60-100 bpm","QRS is absent","T waves are absent"],"Normal pattern."),
     ("Sinus bradycardia shows:",["Rate >100","*Normal P-QRS pattern but rate <60 bpm","No P waves","Wide QRS"],"Slow but normal rhythm."),
     ("Sinus tachycardia shows:",["Rate <60","*Normal P-QRS pattern but rate >100 bpm","No P waves","ST elevation"],"Fast but normal rhythm."),
     ("Atrial fibrillation on ECG shows:",["Regular P waves","*No identifiable P waves, irregularly irregular rhythm","Wide QRS","ST elevation"],"Chaotic atrial activity."),
     ("In second-degree AV block (Type I/Wenckebach):",["PR is constant","*PR interval progressively lengthens until a QRS is dropped","There are no P waves","QRS is absent"],"Progressive PR prolongation then dropped beat."),
     ("In third-degree (complete) heart block:",["Normal conduction","*P waves and QRS complexes are independent (no AV conduction)","No P waves","No QRS"],"Atria and ventricles beat independently."),
     ("Ventricular tachycardia (VT) shows:",["Narrow QRS","*Wide, regular QRS complexes at a fast rate; life-threatening","Normal P waves","Slow rate"],"Can deteriorate to VFib."),
     ("Ventricular fibrillation shows:",["Normal rhythm","*Chaotic, irregular waveform with no identifiable P, QRS, or T; cardiac arrest","Slow regular rhythm","ST elevation only"],"No effective cardiac output."),
     ("The QT interval represents:",["Atrial activity only","*Total duration of ventricular depolarization + repolarization","P wave duration","Only QRS"],"Prolonged QT increases arrhythmia risk."),
     ("A 12-lead ECG provides:",["One view","*Multiple views of the heart's electrical activity from different angles","Only heart rate","Only rhythm"],"Helps localize ischemia/injury."),
     ("To interpret an ECG systematically:",["Guess the rhythm","*Assess rate, rhythm, P waves, PR interval, QRS width, ST/T changes systematically","Only look at one lead","Only check heart rate"],"Systematic approach prevents missed findings."),
     ("ECG interpretation skills are essential for:",["Only cardiologists","*All healthcare providers in emergency and acute care settings","Only researchers","Nobody"],"Basic ECG is a core clinical skill.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 6: wrote {len(lessons)} lessons")
