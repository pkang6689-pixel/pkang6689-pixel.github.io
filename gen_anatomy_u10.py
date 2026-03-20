#!/usr/bin/env python3
"""Anatomy Unit 10 – Integration & Review (7 lessons)."""
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

# 10.1
k,v = build_lesson(10,1,"Immune System Overview",
    "<h3>Immune System Overview</h3>"
    "<h4>Innate (Non-Specific) Immunity</h4>"
    "<ul><li><b>First line:</b> Skin, mucous membranes, secretions (lysozyme, HCl, sebum).</li>"
    "<li><b>Second line:</b> Phagocytes (neutrophils, macrophages), NK cells, inflammation, fever, complement, interferons.</li></ul>"
    "<h4>Adaptive (Specific) Immunity</h4>"
    "<ul><li><b>Humoral:</b> B cells → plasma cells → antibodies (IgG, IgA, IgM, IgE, IgD).</li>"
    "<li><b>Cell-mediated:</b> T cells — CD4⁺ helper (coordinate response), CD8⁺ cytotoxic (kill infected cells).</li>"
    "<li><b>Memory cells:</b> Long-lived B and T cells for rapid secondary response.</li></ul>",
    [("Innate Immunity","Non-specific, rapid defense present from birth; includes barriers, phagocytes, inflammation, and complement."),
     ("Adaptive Immunity","Specific, slower initial response; involves B cells (antibodies) and T cells; creates immunological memory."),
     ("Antibody (Immunoglobulin)","Protein produced by plasma cells that recognizes and binds specific antigens; IgG, IgA, IgM, IgE, IgD."),
     ("CD4⁺ T Helper Cell","Coordinates adaptive immune responses; activates B cells and CD8⁺ T cells; targeted by HIV."),
     ("Memory Cell","Long-lived lymphocyte that enables faster, stronger immune response upon re-exposure to an antigen.")],
    [("The first line of defense includes:",["Antibodies","*Skin, mucous membranes, and secretions (lysozyme, acid, sebum)","T cells","B cells"],"Physical and chemical barriers."),
     ("Neutrophils are:",["Adaptive immune cells","*The most abundant WBCs; first responders to infection (phagocytes)","Red blood cells","Platelets"],"Arrive first at infection site."),
     ("Macrophages function as:",["Only antigen presenters","*Phagocytes AND antigen-presenting cells (bridge innate and adaptive immunity)","Only in the spleen","Only in the liver"],"Versatile immune cells."),
     ("Inflammation is characterized by:",["Only pain","*Redness, heat, swelling, and pain (rubor, calor, tumor, dolor)","Only fever","Only swelling"],"Cardinal signs of inflammation."),
     ("The complement system:",["Only fights parasites","*Is a cascade of ~30 proteins that enhances phagocytosis, causes lysis, and promotes inflammation","Is part of adaptive immunity","Only makes antibodies"],"Innate defense amplifier."),
     ("B cells mature in the:",["Thymus","*Bone marrow","Lymph nodes","Spleen"],"B = Bone marrow."),
     ("T cells mature in the:",["Bone marrow","*Thymus","Lymph nodes","Liver"],"T = Thymus."),
     ("Plasma cells produce:",["T cell receptors","*Antibodies (immunoglobulins)","Complement","Interferons"],"Differentiated B cells."),
     ("IgG is:",["Only in secretions","*The most abundant antibody in blood; crosses the placenta; provides passive immunity to the fetus","Only on mast cells","Only in mucous membranes"],"Primary antibody of adaptive immunity."),
     ("IgE is associated with:",["Normal infection defense","*Allergic reactions and parasitic infections (binds mast cells → histamine release)","Blood type","Complement activation"],"Mediator of type I hypersensitivity."),
     ("CD4⁺ T helper cells:",["Kill infected cells","*Coordinate the immune response by activating B cells, CD8⁺ T cells, and macrophages","Produce antibodies","Are phagocytes"],"Orchestrators of adaptive immunity."),
     ("CD8⁺ cytotoxic T cells:",["Coordinate responses","*Directly kill virus-infected cells and cancer cells (via perforin/granzymes)","Produce antibodies","Are macrophages"],"Cytotoxic = cell-killing."),
     ("Vaccines work by:",["Causing disease","*Exposing the immune system to antigens (weakened/inactivated pathogen or antigen) → memory cells formed","Producing antibiotics","Enhancing innate immunity only"],"Immunological memory without disease."),
     ("Autoimmune diseases occur when:",["The immune system is weak","*The immune system attacks the body's own tissues (loss of self-tolerance)","Only infections cause them","Vaccines cause them"],"Examples: lupus, RA, MS, type 1 diabetes."),
     ("HIV attacks _____ cells.",["CD8⁺ T","*CD4⁺ T helper","B","NK"],"Immune system collapse → AIDS."),
     ("Anaphylaxis is a:",["Mild reaction","*Severe, life-threatening systemic allergic reaction (IgE-mediated)","Type of infection","Autoimmune disease"],"Emergency: epinephrine is first-line treatment."),
     ("Immunodeficiency disorders can be:",["Only acquired","*Primary (genetic, e.g., SCID) or secondary (acquired, e.g., HIV/AIDS)","Only genetic","Caused by diet alone"],"Both categories exist."),
     ("The lymphatic system's role in immunity includes:",["Only fluid drainage","*Filtering lymph (lymph nodes), housing immune cells, and transporting antigens to lymphoid organs","Only fighting cancer","No role"],"Lymph nodes are immune surveillance hubs."),
     ("Interferons:",["Kill bacteria","*Are proteins released by virus-infected cells that signal neighboring cells to increase antiviral defenses","Are antibodies","Are only produced by T cells"],"Innate antiviral defense."),
     ("Understanding the immune system is essential for:",["Nothing","*Managing infections, autoimmune diseases, allergies, transplant rejection, cancer immunotherapy, and vaccination","Only immunologists","Only researchers"],"One of the most important body systems.")]
)
lessons[k]=v

# 10.2
k,v = build_lesson(10,2,"Interactions Between Organ Systems",
    "<h3>Interactions Between Organ Systems</h3>"
    "<h4>Homeostasis Through Integration</h4>"
    "<p>No organ system works in isolation. Maintaining homeostasis requires coordinated communication between all 11 organ systems.</p>"
    "<h4>Key Interactions</h4>"
    "<ul><li><b>Exercise response:</b> Muscular (contraction) + skeletal (support) + nervous (motor commands) + cardiovascular (↑ CO) + respiratory (↑ ventilation) + endocrine (epinephrine, cortisol).</li>"
    "<li><b>Eating a meal:</b> Digestive (digestion/absorption) + nervous (vagal stimulation) + endocrine (insulin, GI hormones) + cardiovascular (nutrient transport) + urinary (waste excretion).</li>"
    "<li><b>Hemorrhage response:</b> Cardiovascular (↑ HR, vasoconstriction) + nervous (baroreceptor reflex) + endocrine (RAAS, ADH) + urinary (↓ urine output) + immune (clotting).</li></ul>",
    [("Homeostasis","Maintenance of a stable internal environment through coordinated organ system activity."),
     ("Cardiac Output","Volume of blood pumped by the heart per minute (HR × SV); increases during exercise."),
     ("Baroreceptor Reflex","Autonomic reflex that adjusts heart rate and vascular tone in response to blood pressure changes."),
     ("Insulin","Pancreatic hormone that lowers blood glucose by promoting cellular uptake and glycogen storage."),
     ("Epinephrine","Adrenal medulla hormone that increases HR, BP, bronchodilation, and glucose — 'fight-or-flight.'")],
    [("During exercise, cardiac output increases because:",["Only HR increases","*Both heart rate AND stroke volume increase to meet muscle oxygen demand","Only stroke volume increases","Blood pressure drops"],"CO = HR × SV; both rise."),
     ("The respiratory system responds to exercise by:",["Decreasing ventilation","*Increasing ventilation rate and depth (to supply more O₂ and remove CO₂)","Not changing","Only increasing depth"],"Proportional to metabolic demand."),
     ("Epinephrine during exercise:",["Slows the heart","*Increases HR, BP, bronchodilation, and mobilizes glucose from glycogen","Only relaxes muscles","Has no effect"],"Sympathetic activation."),
     ("After eating, the parasympathetic nervous system:",["Inhibits digestion","*Stimulates digestion ('rest and digest' — increases GI secretion and motility)","Increases heart rate","Causes sweating"],"Vagal stimulation of GI tract."),
     ("Insulin released after a meal:",["Raises blood glucose","*Lowers blood glucose by promoting cellular uptake, glycogenesis, and lipogenesis","Has no effect on glucose","Only affects the liver"],"Key postprandial hormone."),
     ("In hemorrhage, baroreceptors detect:",["High blood pressure","*Decreased blood pressure → trigger sympathetic response (↑ HR, vasoconstriction)","High CO₂","Low O₂"],"Baroreceptor reflex compensates for blood loss."),
     ("RAAS activation during hemorrhage leads to:",["Vasodilation","*Na⁺ and water retention + vasoconstriction → restores blood volume and pressure","Diuresis","Decreased HR"],"Compensatory mechanism."),
     ("The integumentary system (skin) interacts with other systems by:",["Having no interactions","*Protecting all systems (barrier), synthesizing vitamin D (skeletal), thermoregulation (cardiovascular), and sensory input (nervous)","Only protection","Only sensation"],"Skin is the body's interface."),
     ("The skeletal system supports other systems by:",["Only providing structure","*Providing structure, protecting organs (brain, heart, lungs), producing blood cells (marrow), and storing minerals (Ca²⁺)","Only storing calcium","Only protecting the brain"],"Hematopoiesis + mineral storage."),
     ("Fever is an example of:",["System failure","*Coordinated response: immune (pyrogens) + nervous (hypothalamic thermostat) + cardiovascular (vasodilation) + muscular (shivering)","Only immune system","Only nervous system"],"Multi-system response to infection."),
     ("Pregnancy involves coordination of:",["Only the reproductive system","*Reproductive, endocrine, cardiovascular, respiratory, urinary, musculoskeletal, immune, and digestive systems","Only two systems","Only hormones"],"Nearly every system adapts."),
     ("The nervous and endocrine systems work together by:",["Operating independently","*The nervous system triggers rapid responses while the endocrine system sustains them (e.g., fight-or-flight)","Only one functioning at a time","Competing against each other"],"Neural-endocrine integration."),
     ("Blood serves as a communication highway by:",["Only carrying oxygen","*Transporting O₂, CO₂, nutrients, hormones, waste, immune cells, and heat","Only carrying waste","Only carrying hormones"],"Circulatory system connects all organs."),
     ("Dehydration affects multiple systems:",["Only the urinary system","*Cardiovascular (↓ blood volume), nervous (confusion), renal (↓ GFR), muscular (cramps), and thermoregulatory","Only causing thirst","Only the kidneys"],"Multi-system impact."),
     ("Diabetes mellitus demonstrates system interactions:",["In the pancreas only","*Endocrine (insulin deficit) → cardiovascular (atherosclerosis), nervous (neuropathy), renal (nephropathy), visual (retinopathy), immune (infections)","Only blood sugar","Only the kidneys"],"Systemic disease."),
     ("Stress (chronic) affects:",["Nothing","*Nervous (HPA axis), endocrine (cortisol), cardiovascular (hypertension), immune (suppression), digestive (ulcers), and mental health","Only mood","Only the heart"],"Chronic cortisol has widespread effects."),
     ("Aging involves:",["Only one system declining","*Gradual decline in all organ systems: decreased GFR, cardiac output, bone density, immune function, etc.","Only joint pain","Nothing significant"],"Multi-system decline."),
     ("A systems approach to medicine means:",["Treating one organ at a time","*Considering how all body systems interact when diagnosing and treating disease","Ignoring other systems","Only using surgery"],"Holistic understanding."),
     ("Clinical integration is important because:",["Diseases affect only one system","*Most diseases affect multiple organ systems, and treatment must consider the whole patient","It's not important","Only for research"],"Real patients have multi-system pathology."),
     ("Studying organ system interactions prepares students for:",["Only anatomy exams","*Understanding complex clinical scenarios, practicing systems-based medicine, and succeeding on AP exams","Only memorizing facts","Nothing"],"Foundation for clinical reasoning.")]
)
lessons[k]=v

# 10.3
k,v = build_lesson(10,3,"Case Studies in Pathophysiology",
    "<h3>Case Studies in Pathophysiology</h3>"
    "<h4>Case 1: Congestive Heart Failure (CHF)</h4>"
    "<p>68 y/o with dyspnea, edema, elevated JVP. Chest X-ray: pulmonary congestion. Echo: reduced EF. CHF involves cardiovascular (pump failure), respiratory (pulmonary edema), renal (fluid retention), and endocrine (RAAS activation) systems.</p>"
    "<h4>Case 2: Type 1 Diabetes (DKA)</h4>"
    "<p>16 y/o with polyuria, polydipsia, weight loss, fruity breath. Labs: glucose 450, pH 7.1, ketones +++. Endocrine (no insulin), renal (glucosuria, osmotic diuresis), respiratory (Kussmaul breathing), and nervous system (altered mental status) involvement.</p>"
    "<h4>Case 3: Sepsis</h4>"
    "<p>45 y/o post-surgical with fever, tachycardia, hypotension, altered mental status. Blood cultures positive. Immune (overwhelming infection), cardiovascular (vasodilation, hypotension), renal (AKI), respiratory (ARDS), and coagulation (DIC) involved.</p>",
    [("CHF","Congestive heart failure; the heart can't pump effectively → fluid backs up into lungs and tissues."),
     ("Ejection Fraction (EF)","Percentage of blood ejected from the ventricle per beat; normal ~55-70%; reduced in heart failure."),
     ("DKA","Diabetic ketoacidosis; life-threatening complication of type 1 diabetes: hyperglycemia + acidosis + ketones."),
     ("Sepsis","Life-threatening organ dysfunction caused by a dysregulated host response to infection."),
     ("ARDS","Acute respiratory distress syndrome; severe lung inflammation/fluid accumulation → respiratory failure.")],
    [("In CHF, the heart:",["Pumps too forcefully","*Cannot pump effectively enough to meet the body's demands","Only produces arrhythmias","Is structurally normal"],"Pump failure."),
     ("Pulmonary edema in left-sided heart failure occurs because:",["Blood drains from lungs","*Blood backs up into pulmonary veins → fluid leaks into alveoli","The lungs produce excess mucus","Airway is obstructed"],"Left ventricle failure → pulmonary congestion."),
     ("In CHF, the kidneys respond by:",["Excreting excess water","*Retaining Na⁺ and water (RAAS activation) → worsening fluid overload","Stopping function","Only filtering waste"],"Compensatory mechanism that backfires."),
     ("ACE inhibitors treat CHF by:",["Increasing fluid retention","*Blocking angiotensin II → vasodilation + reduced preload/afterload + less aldosterone","Increasing HR","Increasing aldosterone"],"First-line CHF medications."),
     ("In DKA, the body uses _____ for energy because insulin is absent.",["Glucose","*Fat (fatty acid oxidation → ketone bodies → acidosis)","Protein only","Carbohydrates"],"Can't use glucose without insulin."),
     ("Kussmaul breathing in DKA is:",["Shallow breathing","*Deep, rapid breathing to blow off CO₂ (respiratory compensation for metabolic acidosis)","Normal breathing","Absent breathing"],"Compensatory hyperventilation."),
     ("Treatment of DKA includes:",["Only oral glucose","*IV insulin, IV fluids, electrolyte replacement (especially K⁺), and monitoring","Only antacids","Only bicarbonate"],"Must correct glucose, volume, and electrolytes."),
     ("In sepsis, vasodilation causes:",["Hypertension","*Hypotension (distributive shock) — despite high cardiac output initially","Vasoconstriction","Normal BP"],"Inflammatory mediators → vasodilation → shock."),
     ("Sepsis can lead to multi-organ failure because:",["Only one organ is affected","*Systemic inflammation damages multiple organs: kidneys (AKI), lungs (ARDS), liver, brain","The infection is localized","Antibiotics fail"],"Cascade of organ dysfunction."),
     ("DIC (disseminated intravascular coagulation) in sepsis causes:",["Only clotting","*Simultaneous excessive clotting AND bleeding (consumption of clotting factors)","Only bleeding","No hematologic problems"],"Paradox of DIC."),
     ("The 'hour-1 bundle' for sepsis includes:",["Only antibiotics","*IV fluids, blood cultures, antibiotics, and lactate measurement — all within 1 hour","Only fluids","Only monitoring"],"Early intervention saves lives."),
     ("Myocardial infarction (MI) involves:",["Only the heart","*Cardiovascular (coronary occlusion), nervous (pain), endocrine (stress hormones), and potentially renal and respiratory systems","Only chest pain","Only the immune system"],"Multi-system emergency."),
     ("Stroke demonstrates:",["Only a brain problem","*Nervous (focal deficits), cardiovascular (cause: embolism or hemorrhage), musculoskeletal (weakness), and respiratory (airway compromise) system involvement","Only weakness","Only speech problems"],"Multi-system implications."),
     ("Chronic obstructive pulmonary disease (COPD) affects:",["Only the lungs","*Respiratory (airflow obstruction), cardiovascular (cor pulmonale), musculoskeletal (cachexia), and mental health","Only breathing","Only smoking-related"],"Systemic disease."),
     ("A patient with liver cirrhosis may present with:",["Only jaundice","*Jaundice, ascites, coagulopathy, portal hypertension, encephalopathy, and renal failure (hepatorenal syndrome)","Only abdominal pain","No symptoms"],"Multi-system hepatic decompensation."),
     ("Understanding pathophysiology requires:",["Memorizing diseases","*Integrating knowledge of anatomy, physiology, and multiple organ system interactions","Only reading textbooks","Only clinical experience"],"Systems thinking."),
     ("These case studies illustrate that:",["Diseases are simple","*Most serious diseases involve multiple organ systems and require a systems-based approach","Only one system is affected","Treatment is straightforward"],"Clinical complexity."),
     ("The best approach to these cases on an AP exam is:",["Guessing","*Systematically identifying which organ systems are involved and explaining the pathophysiology of each","Only naming the disease","Only listing symptoms"],"Organized, systems-based analysis."),
     ("Critical thinking in pathophysiology involves:",["Memorization only","*Connecting cause → mechanism → effect across organ systems","Only knowing anatomy","Only knowing pharmacology"],"Reasoning through disease processes."),
     ("These cases prepare students for:",["Nothing","*Clinical reasoning, AP exam scenarios, and future healthcare careers","Only exams","Only lectures"],"Real-world application of anatomy/physiology.")]
)
lessons[k]=v

# 10.4
k,v = build_lesson(10,4,"Review of Key Concepts",
    "<h3>Review of Key Concepts</h3>"
    "<h4>By Organ System</h4>"
    "<ul><li><b>Skeletal:</b> Support, protection, movement, hematopoiesis, mineral storage.</li>"
    "<li><b>Muscular:</b> Movement, posture, heat production. Sliding filament theory.</li>"
    "<li><b>Nervous:</b> Rapid communication via action potentials. CNS + PNS.</li>"
    "<li><b>Endocrine:</b> Hormonal regulation — feedback loops, HPG/HPA axes.</li>"
    "<li><b>Cardiovascular:</b> Transport of blood, O₂, nutrients. Cardiac cycle.</li>"
    "<li><b>Respiratory:</b> Gas exchange. Ventilation mechanics.</li>"
    "<li><b>Digestive:</b> Mechanical/chemical digestion, absorption. Liver, pancreas.</li>"
    "<li><b>Urinary:</b> Filtration, reabsorption, secretion. Fluid/electrolyte/acid-base balance.</li>"
    "<li><b>Reproductive:</b> Gametogenesis, hormonal regulation (HPG axis), pregnancy.</li>"
    "<li><b>Immune:</b> Innate + adaptive immunity. Memory.</li></ul>",
    [("Sliding Filament Theory","Muscle contraction mechanism: actin filaments slide past myosin; powered by ATP, regulated by Ca²⁺."),
     ("Action Potential","Rapid electrical signal in neurons/muscles: depolarization (Na⁺ in) → repolarization (K⁺ out)."),
     ("Cardiac Cycle","One complete heartbeat: atrial systole → ventricular systole → diastole."),
     ("Negative Feedback","Homeostatic mechanism where the response opposes the stimulus (e.g., thermoregulation)."),
     ("Filtration (Renal)","Passive, pressure-driven movement of fluid from glomerular capillaries into Bowman's capsule.")],
    [("The five functions of the skeletal system include:",["Only support","*Support, protection, movement, hematopoiesis, and mineral storage","Only movement","Only bone production"],"Skeletal system is multifunctional."),
     ("The sliding filament theory explains:",["Bone growth","*How actin and myosin filaments interact to produce muscle contraction","Nerve conduction","Blood flow"],"Actin slides over myosin."),
     ("An action potential involves:",["Only K⁺ movement","*Depolarization (Na⁺ influx) followed by repolarization (K⁺ efflux)","Only Ca²⁺ movement","Only diffusion"],"Electrical signal propagation."),
     ("Negative feedback in homeostasis means:",["The response amplifies the stimulus","*The response opposes the stimulus to restore a set point","There is no regulation","The system fails"],"Most common regulatory mechanism."),
     ("Positive feedback differs from negative in that:",["It maintains homeostasis","*The response amplifies the stimulus (e.g., oxytocin in labor, LH surge at ovulation)","It's more common","It stops processes"],"Drives processes to completion."),
     ("The cardiac cycle consists of:",["Only systole","*Atrial systole → ventricular systole → diastole (one complete heartbeat)","Only diastole","Random contractions"],"Coordinated pumping sequence."),
     ("Gas exchange occurs at the:",["Bronchi","Trachea","*Alveoli (external respiration) and tissues (internal respiration)","Nasal cavity"],"O₂ and CO₂ exchange."),
     ("The three processes of urine formation are:",["Only filtration","*Filtration, reabsorption, and secretion","Only reabsorption","Only excretion"],"Complete nephron function."),
     ("The menstrual cycle involves which key hormones?",["Only estrogen","*FSH, LH, estrogen, and progesterone","Only progesterone","Only testosterone"],"Complete hormonal regulation of the cycle."),
     ("Antibodies are produced by:",["T cells","*Plasma cells (differentiated B cells)","Macrophages","NK cells"],"Humoral immunity."),
     ("Homeostasis is maintained by all organ systems working:",["Independently","*Together in a coordinated manner","In isolation","Only when stressed"],"Integration is key."),
     ("The SA node is the heart's natural pacemaker located in the:",["Left ventricle","Left atrium","*Right atrium","Right ventricle"],"Initiates each heartbeat."),
     ("The diaphragm is essential for:",["Digestion","*Breathing (contraction creates negative intrathoracic pressure → air inhalation)","Circulation","Urination"],"Primary muscle of respiration."),
     ("The hypothalamus regulates:",["Only temperature","*Temperature, thirst, hunger, circadian rhythms, and endocrine function via the pituitary","Only hormones","Only sleep"],"Master integrator."),
     ("Hemoglobin's primary function is:",["Clotting","*Oxygen transport (each molecule carries up to 4 O₂)","Immune defense","Nutrient transport"],"Found in RBCs."),
     ("Insulin and glucagon have _____ effects on blood glucose.",["Similar","*Opposing (insulin lowers, glucagon raises)","No","Identical"],"Antagonistic hormones."),
     ("The liver's role in metabolism includes:",["Only bile production","*Detoxification, bile production, protein synthesis, glycogen storage/release, and bilirubin processing","Only storage","Only filtration"],"Metabolic powerhouse."),
     ("The lymphatic system's dual role is:",["Only drainage","*Fluid return to blood AND immune defense (lymph nodes filter pathogens)","Only immunity","Only fat absorption"],"Fluid balance + immunity."),
     ("Understanding all systems together is important because:",["They don't interact","*Clinical disease almost always involves multiple systems, and effective treatment requires whole-body understanding","Only for exams","Only for specialists"],"Systems medicine."),
     ("To prepare for the AP exam, students should:",["Only memorize terms","*Understand mechanisms, integration, and be able to apply to clinical scenarios","Ignore pathophysiology","Focus on only one system"],"Application and integration are key.")]
)
lessons[k]=v

# 10.5
k,v = build_lesson(10,5,"AP Practice: Multi-System Questions",
    "<h3>AP Practice: Multi-System Questions</h3>"
    "<p>This lesson focuses on higher-order AP-style questions that integrate knowledge from multiple organ systems. Practice identifying connections across anatomy and physiology to strengthen exam readiness.</p>"
    "<h4>Strategy</h4>"
    "<ul><li>Read the clinical scenario carefully.</li>"
    "<li>Identify ALL organ systems involved.</li>"
    "<li>Think about cause → mechanism → effect.</li>"
    "<li>Eliminate obviously wrong answers first.</li></ul>",
    [("Clinical Reasoning","Systematic approach: gather data → identify problems → hypothesize → test → conclude."),
     ("Multi-System Integration","Recognizing that most physiological events and diseases involve interactions among multiple organ systems."),
     ("Physiological Compensation","Body's automatic adjustments to maintain homeostasis when one system is stressed or failing."),
     ("Pathophysiology","Study of how disease disrupts normal physiology; connects anatomy to clinical medicine."),
     ("Differential Diagnosis","Process of listing and narrowing possible diagnoses based on signs, symptoms, and test results.")],
    [("A marathon runner collapses. Which systems are involved?",["Only muscular","Only cardiovascular","*Cardiovascular (dehydration ↓ CO), thermoregulatory (hyperthermia), renal (↓ GFR), musculoskeletal, nervous (confusion), and endocrine","Only respiratory"],"Multi-system stress."),
     ("In anaphylaxis, which systems are affected?",["Only skin","Only respiratory","*Immune (IgE/mast cells → histamine), cardiovascular (vasodilation → shock), respiratory (bronchospasm → airway obstruction), skin (urticaria)","Only cardiovascular"],"Life-threatening multi-system emergency."),
     ("A patient with chronic kidney disease develops anemia because:",["Kidneys don't filter","*Kidneys produce less erythropoietin (EPO) → ↓ RBC production","The liver fails","Bone marrow is destroyed"],"Renal endocrine function."),
     ("Hyperparathyroidism causes:",["Low calcium","*Elevated blood calcium (increased bone resorption, renal Ca²⁺ reabsorption, and intestinal absorption via vitamin D)","Low phosphate excretion","No bone effects"],"PTH affects skeletal, renal, and GI systems."),
     ("A patient with a pulmonary embolism (PE) develops:",["Only leg pain","*Respiratory failure (V/Q mismatch), cardiovascular compromise (right heart strain), and potentially hemodynamic collapse","Only cough","Normal breathing"],"Multi-system emergency."),
     ("Hypothyroidism affects:",["Only the thyroid","*Metabolism (weight gain), cardiovascular (bradycardia), nervous (cognitive slowing), musculoskeletal (weakness), integumentary (cold intolerance, dry skin)","Only weight","Only mood"],"Thyroid hormones affect every organ system."),
     ("A spinal cord injury at C3 can cause:",["Only paralysis","*Loss of voluntary movement below injury, respiratory failure (phrenic nerve to diaphragm at C3-5), autonomic dysreflexia, neurogenic bladder","Only numbness","Only pain"],"High cervical injury = life-threatening."),
     ("Sickle cell disease affects:",["Only blood","*Cardiovascular (anemia), skeletal (bone crisis), splenic (autosplenectomy), renal, pulmonary, and neurological systems","Only bones","Only the spleen"],"Systemic disease from one genetic mutation."),
     ("A patient taking corticosteroids chronically may develop:",["Only weight loss","*Cushing-like features: immunosuppression, osteoporosis, hyperglycemia, muscle wasting, poor wound healing, adrenal suppression","Only skin changes","Only mood changes"],"Wide-ranging steroid effects."),
     ("Pregnancy affects the cardiovascular system by:",["Decreasing blood volume","*Increasing blood volume (~50%), cardiac output (~40%), and heart rate","No changes","Decreasing HR"],"Major cardiovascular adaptations."),
     ("In diabetic nephropathy:",["Kidneys are normal","*Chronic hyperglycemia damages glomerular capillaries → proteinuria → progressive renal failure","Only blood sugar rises","Only the pancreas is affected"],"Endocrine → renal system connection."),
     ("Liver failure can cause cerebral edema because:",["The brain shrinks","*Ammonia accumulates (liver can't convert to urea) → crosses BBB → hepatic encephalopathy","The heart fails","Kidneys stop working"],"Hepatic-neurological connection."),
     ("A patient with COPD develops right heart failure (cor pulmonale) because:",["The left heart fails first","*Chronic hypoxic pulmonary vasoconstriction → pulmonary hypertension → right ventricle overload","The lungs collapse","The kidneys fail"],"Respiratory → cardiovascular connection."),
     ("Burns involving >30% BSA affect:",["Only skin","*Integumentary (barrier loss), immune (infection risk), cardiovascular (fluid loss → shock), renal (↓ perfusion), metabolic (hypermetabolic state)","Only pain","Only fluid loss"],"Major burns = multi-system crisis."),
     ("Obesity increases risk for:",["Nothing","*Cardiovascular disease, type 2 diabetes, joint disease, sleep apnea, certain cancers, and more","Only joint pain","Only diabetes"],"Multi-system health impact."),
     ("To answer AP multi-system questions:",["Memorize only","*Think about cause → mechanism → effect and identify every system involved","Guess","Only know terminology"],"Systematic approach."),
     ("Which is the best strategy for elimination?",["Pick randomly","*Eliminate answers that only mention one system when the scenario clearly involves multiple","Always pick 'all of the above'","Pick the longest answer"],"Think broadly."),
     ("Time management on AP exams:",["Isn't important","*Spend roughly equal time per question; flag difficult ones and return later","Spend all time on hard questions","Rush through all questions"],"Strategic pacing."),
     ("Practice questions help because:",["They're not useful","*They build familiarity with question format, test knowledge application, and identify weak areas","Only for memorization","Only for anxiety"],"Active recall strengthens learning."),
     ("The best AP exam preparation strategy involves:",["Memorization alone","*Understanding mechanisms, practicing application questions, reviewing weak areas, and integrating across systems","Only reading the textbook","Only watching videos"],"Active, integrated study.")]
)
lessons[k]=v

# 10.6
k,v = build_lesson(10,6,"Capstone Project: Human Body Systems",
    "<h3>Capstone Project: Human Body Systems</h3>"
    "<h4>Project Overview</h4>"
    "<p>Students select a clinical condition (e.g., heart attack, diabetes, sepsis) and analyze it from a multi-system perspective, documenting the pathophysiology across all affected organ systems.</p>"
    "<h4>Steps</h4>"
    "<ul><li>1. Choose a disease or case.</li>"
    "<li>2. Identify all organ systems affected.</li>"
    "<li>3. Explain the pathophysiology of each system's involvement.</li>"
    "<li>4. Describe how systems compensate or fail.</li>"
    "<li>5. Discuss treatment strategies that target each system.</li>"
    "<li>6. Present findings in a structured format (paper, poster, or presentation).</li></ul>",
    [("Capstone Project","Culminating assignment that integrates knowledge from across all units into a comprehensive analysis."),
     ("Pathophysiology Analysis","Systematic explanation of how a disease disrupts normal physiology across organ systems."),
     ("Systems-Based Approach","Framework for understanding diseases by analyzing their effects on each organ system."),
     ("Evidence-Based Medicine","Using the best available research evidence to guide clinical decisions and treatments."),
     ("Clinical Presentation","The signs, symptoms, and findings that a patient displays when presenting with a disease.")],
    [("A capstone project in anatomy should:",["Only list facts","*Integrate knowledge from multiple units and organ systems to analyze a clinical condition","Only use one source","Copy a textbook"],"Synthesis and application."),
     ("When selecting a disease for the capstone, a good choice is:",["The easiest disease","*A condition that involves multiple organ systems (e.g., diabetes, heart failure, sepsis)","The rarest disease","Only a skeletal disease"],"Multi-system involvement = richer analysis."),
     ("Step 1 of the project involves:",["Writing the conclusion","*Choosing a disease and defining the scope of analysis","Presenting findings","Doing lab work"],"Start with a clear focus."),
     ("Step 2 requires identifying:",["Only one system","*ALL organ systems affected by the chosen condition","Only symptoms","Only treatments"],"Comprehensive system identification."),
     ("Explaining pathophysiology means:",["Only naming the disease","*Describing the mechanism of how the disease disrupts normal physiology in each system","Only listing treatments","Only giving definitions"],"Cause → mechanism → effect."),
     ("Describing compensation means:",["The disease resolves","*Explaining how the body tries to maintain homeostasis (e.g., ↑ HR in hemorrhage, hyperventilation in acidosis)","Nothing changes","Only medications help"],"Physiological compensation mechanisms."),
     ("When systems fail to compensate, the result is:",["Always recovery","*Decompensation → organ failure → possible multi-organ dysfunction → death if untreated","Nothing","Improved function"],"Progressive decline."),
     ("Treatment strategies should:",["Ignore other systems","*Address each affected organ system and their interactions","Only use one drug","Only use surgery"],"Multi-targeted approach."),
     ("Evidence-based sources include:",["Social media","*Peer-reviewed journals, textbooks, clinical guidelines (e.g., UpToDate, PubMed)","Wikipedia only","Only class notes"],"Credible, peer-reviewed sources."),
     ("A poster presentation should include:",["Only text","*Title, introduction, pathophysiology, multi-system analysis, treatment, conclusion, references, and visuals","Only images","Only a bibliography"],"Complete and visually organized."),
     ("An oral presentation should be:",["Unstructured","*Organized, clear, evidence-based, and demonstrate understanding of multi-system integration","Reading slides word for word","Only listing facts"],"Communication skills matter."),
     ("Peer review of capstone projects helps:",["Nothing","*Identify gaps in reasoning, improve clarity, and strengthen the final product","Only the reviewer","Only find errors"],"Collaborative learning."),
     ("Rubric criteria typically include:",["Only length","*Content accuracy, multi-system integration, evidence use, organization, and presentation quality","Only formatting","Only references"],"Holistic assessment."),
     ("Diabetes mellitus would involve analysis of:",["Only the pancreas","*Endocrine (insulin), cardiovascular (atherosclerosis), nervous (neuropathy), renal (nephropathy), visual (retinopathy), immune (infections)","Only blood sugar","Only diet"],"Excellent multi-system choice."),
     ("Trauma (e.g., car accident) could involve:",["Only broken bones","*Musculoskeletal (fractures), nervous (concussion/spinal cord), cardiovascular (hemorrhage), respiratory (pneumothorax), integumentary (lacerations)","Only skin injuries","Only head injury"],"Multi-system trauma."),
     ("This project develops skills in:",["Only memorization","*Critical thinking, integration, research, analysis, communication, and clinical reasoning","Only writing","Only presentation"],"Multiple competencies."),
     ("A strong capstone connects anatomy to:",["Nothing","*Pathophysiology, clinical medicine, and real-world patient care","Only grades","Only exams"],"Bridge between classroom and clinic."),
     ("Students should avoid:",["Using multiple sources","*Plagiarism, superficial analysis, and ignoring system interactions","Analyzing multiple systems","Using visuals"],"Academic integrity and depth matter."),
     ("The capstone project is valuable because it:",["Is just a grade","*Synthesizes an entire course into a coherent, clinically relevant analysis","Is required","Replaces studying"],"Culminating learning experience."),
     ("This project prepares students for:",["Nothing","*Future healthcare studies, AP exams, college-level coursework, and evidence-based practice","Only the final exam","Only college applications"],"Transferable skills.")]
)
lessons[k]=v

# 10.7
k,v = build_lesson(10,7,"Comprehensive Review & AP Prep",
    "<h3>Comprehensive Review &amp; AP Prep</h3>"
    "<h4>Final Review Checklist</h4>"
    "<ul><li>☐ Body organization, terminology, homeostasis (Unit 1).</li>"
    "<li>☐ Skeletal system: bone types, joints, disorders (Unit 2).</li>"
    "<li>☐ Muscular system: contraction, sliding filament (Unit 3).</li>"
    "<li>☐ Nervous system: action potentials, CNS/PNS, reflexes (Unit 4).</li>"
    "<li>☐ Endocrine system: hormones, feedback, glands (Unit 5).</li>"
    "<li>☐ Cardiovascular: heart, vessels, cardiac cycle, blood (Unit 6).</li>"
    "<li>☐ Respiratory: lungs, gas exchange, ventilation (Unit 7).</li>"
    "<li>☐ Digestive: organs, enzymes, absorption, liver (Unit 8).</li>"
    "<li>☐ Urinary & Reproductive: nephron, hormones, gametogenesis (Unit 9).</li>"
    "<li>☐ Integration: immune system, multi-system interactions (Unit 10).</li></ul>"
    "<p><b>Strategies:</b> Focus on integration, practice multi-system questions, review weak areas, use active recall and spaced repetition.</p>",
    [("Active Recall","Study technique: retrieve information from memory rather than passively re-reading; strengthens retention."),
     ("Spaced Repetition","Reviewing material at increasing intervals to improve long-term retention."),
     ("Bloom's Taxonomy","Educational framework: Remember → Understand → Apply → Analyze → Evaluate → Create; AP tests higher levels."),
     ("Homeostasis","The central theme of anatomy/physiology; all organ systems work to maintain a stable internal environment."),
     ("Clinical Application","Using anatomical and physiological knowledge to understand, diagnose, and treat disease.")],
    [("The central theme of anatomy and physiology is:",["Memorization","*Homeostasis — maintaining a stable internal environment through coordinated organ system function","Only structure","Only disease"],"Unifying concept of the course."),
     ("Anatomical terminology helps clinicians:",["Confuse patients","*Communicate precisely about body locations, directions, and structures","Only pass exams","Only in English"],"Universal language of medicine."),
     ("Histology (tissue study) is important because:",["It's not useful","*Understanding the 4 tissue types explains how organs function and how disease affects them","Only for pathologists","Only for researchers"],"Epithelial, connective, muscle, nervous."),
     ("Bone remodeling involves:",["Only osteoblasts","*Osteoblasts (build bone) and osteoclasts (resorb bone) working in balance","Only osteoclasts","Only calcium"],"Continuous remodeling throughout life."),
     ("The neuromuscular junction uses _____ as the neurotransmitter.",["Epinephrine","*Acetylcholine (ACh)","Dopamine","Serotonin"],"ACh triggers muscle contraction."),
     ("The sympathetic nervous system (fight-or-flight) causes:",["Bronchoconstriction","*↑ HR, ↑ BP, bronchodilation, pupil dilation, ↑ blood glucose","Increased digestion","Pupil constriction"],"Prepare for emergency."),
     ("Hormones travel via the _____ to reach target cells.",["Nerves","*Blood (endocrine = bloodstream delivery)","Lymph","Skin"],"Endocrine signaling."),
     ("The sinoatrial (SA) node generates the heartbeat at a rate of:",["40-60 bpm","*60-100 bpm (normal resting heart rate)","100-150 bpm","20-40 bpm"],"Intrinsic pacemaker rate."),
     ("Tidal volume is:",["Total lung capacity","*The volume of air inhaled/exhaled in a normal breath (~500 mL)","Residual volume","Vital capacity"],"Normal breathing volume."),
     ("Pepsin, trypsin, and chymotrypsin are all _____ enzymes.",["Lipase","*Protease (protein-digesting)","Amylase","Nuclease"],"Break peptide bonds."),
     ("The GFR is the best overall indicator of:",["Liver function","Heart function","*Kidney function","Lung function"],"Filtration rate reflects renal health."),
     ("Spermatogenesis produces _____ sperm from each spermatogonium.",["1","2","*4","8"],"Meiosis: 1 spermatogonium → 4 spermatozoa."),
     ("Oogenesis produces _____ viable ovum per cycle.",["4","2","*1 (plus polar bodies)","3"],"Unequal meiosis → one large egg."),
     ("The immune system's memory cells provide:",["No benefit","*Long-lasting immunity (faster, stronger response upon re-exposure)","Only short-term protection","Only innate defense"],"Basis of vaccination and natural immunity."),
     ("For AP-level questions, students must:",["Only recall facts","*Apply, analyze, and evaluate — not just remember and understand","Only memorize vocabulary","Only draw diagrams"],"Higher-order thinking."),
     ("Spaced repetition is effective because:",["Cramming is better","*Reviewing at increasing intervals strengthens long-term memory consolidation","It's easy","It requires no effort"],"Evidence-based study strategy."),
     ("Active recall is better than re-reading because:",["It's not","*Retrieving information from memory strengthens neural pathways more than passive review","It's faster","It's easier"],"Testing effect."),
     ("Creating concept maps helps by:",["Wasting time","*Visually organizing and connecting concepts across organ systems","Only looking nice","Only for visual learners"],"Integration tool."),
     ("Practice exams under timed conditions are valuable because:",["They cause anxiety","*They simulate the real exam experience, improve pacing, and reveal weak areas","They're not useful","They only help fast learners"],"Authentic practice."),
     ("This course prepares students for:",["Nothing","*College-level anatomy/physiology, healthcare careers, AP exams, and lifelong understanding of the human body","Only exams","Only medical school"],"Foundation for health literacy and careers.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 10: wrote {len(lessons)} lessons")
