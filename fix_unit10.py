import json, os, glob

base = 'content_data/AnatomyLessons'

replacements = {
    # Lesson10.1
    ("Unit10/Lesson10.1_Quiz.json", 22): {
        "HIV directly infects the lung tissue causing pneumonia": "HIV directly infects the lung tissue by binding to receptors on pneumocytes, causing direct pneumonia through viral replication within the alveolar epithelial cells and destruction of the respiratory membrane",
        "HIV causes excessive antibody production that damages the lungs": "HIV causes excessive antibody production by overstimulating B cells, leading to immune complex deposition in the pulmonary vasculature that damages the alveolar-capillary membrane and causes pneumonia",
        "The complement system is entirely destroyed by HIV": "The complement system is entirely destroyed by HIV through direct viral lysis of complement proteins, eliminating all innate immune defenses and leaving the patient unable to opsonize pathogens",
    },
    ("Unit10/Lesson10.1_Quiz.json", 30): {
        "PEP is a vaccine that stimulates memory cell production against HIV": "PEP is a vaccine that stimulates memory B and T cell production against HIV surface glycoproteins, providing long-term adaptive immunity that prevents viral entry into CD4+ cells after future exposures",
        "PEP works by immediately boosting the innate immune system to destroy all HIV particles": "PEP works by immediately boosting the innate immune system through rapid activation of natural killer cells and macrophages that identify and destroy all HIV particles before they can infect any CD4+ cells",
        "PEP replaces the destroyed CD4+ T cells with donor lymphocytes": "PEP replaces the destroyed CD4+ T cells with donor lymphocytes through an infusion of HLA-matched T cells that engraft in the patient's lymphoid tissue and restore adaptive immune function",
    },
    # Lesson10.2
    ("Unit10/Lesson10.2_Quiz.json", 8): {
        "Only producing melanin for UV protection": "Only producing melanin through melanocyte activity for UV protection, shielding the DNA of keratinocytes from ultraviolet radiation damage",
        "Only serving as a physical barrier against pathogens": "Only serving as a physical barrier against pathogens by providing a continuous layer of keratinized stratified squamous epithelium and antimicrobial peptides",
        "Only regulating fluid loss through perspiration": "Only regulating fluid loss through perspiration from eccrine and apocrine sweat glands distributed across the body surface",
    },
    ("Unit10/Lesson10.2_Quiz.json", 16): {
        "A hormonal pathway that controls the menstrual cycle": "A hormonal pathway that controls the menstrual cycle through pulsatile GnRH release from the hypothalamus, stimulating FSH and LH from the anterior pituitary to drive follicular development",
        "A pathway that controls voluntary skeletal muscle movement": "A pathway that controls voluntary skeletal muscle movement through upper motor neurons in the motor cortex descending through the corticospinal tract to lower motor neurons in the spinal cord",
        "A reflex arc that regulates heart rate during exercise": "A reflex arc that regulates heart rate during exercise through baroreceptor feedback to the cardiovascular center in the medulla, adjusting sympathetic and parasympathetic output",
    },
    ("Unit10/Lesson10.2_Quiz.json", 19): {
        "Before eating a meal": "Before eating a meal, referring to the fasting metabolic state driven by glucagon and cortisol that mobilizes stored energy reserves",
        "During the act of chewing and swallowing food": "During the act of chewing and swallowing food, referring to the oral and pharyngeal phases of deglutition coordinated by cranial nerves",
        "The period of fasting between meals": "The period of fasting between meals when the body shifts from absorptive to post-absorptive metabolism using glycogenolysis and lipolysis",
    },
    ("Unit10/Lesson10.2_Quiz.json", 21): {
        "Only the muscular system is affected because the muscles are fatigued from lactic acid buildup": "Only the muscular system is affected because the muscles are fatigued from lactic acid buildup during prolonged exercise, and all other symptoms such as confusion and rapid heart rate are simply manifestations of extreme muscle fatigue",
        "The runner is experiencing a heart attack from coronary artery disease": "The runner is experiencing a heart attack from coronary artery disease because the prolonged exercise caused a coronary plaque rupture, and all the symptoms including confusion and hyperthermia are secondary to acute myocardial infarction",
        "The runner's muscular system has simply run out of glycogen, and only rest is needed": "The runner's muscular system has simply run out of glycogen stores from the prolonged exercise, and all the symptoms including tachycardia, confusion, and elevated temperature will resolve spontaneously with rest alone",
    },
    ("Unit10/Lesson10.2_Quiz.json", 23): {
        "Stress hormones only affect the nervous system and cannot cause physical symptoms": "Stress hormones only affect the nervous system and cannot cause physical symptoms because cortisol and catecholamines exclusively bind to receptors in the central nervous system and do not interact with peripheral organs or immune cells",
        "The student's symptoms are entirely caused by poor diet alone": "The student's symptoms are entirely caused by poor diet alone because nutritional deficiencies can produce all of these symptoms independently, and chronic stress has no physiological effect on the immune, cardiovascular, or digestive systems",
        "Chronic stress only affects mood and has no physical consequences": "Chronic stress only affects mood and emotional well-being through changes in serotonin and dopamine levels, and has absolutely no physical consequences for the immune, cardiovascular, or gastrointestinal systems",
    },
    ("Unit10/Lesson10.2_Quiz.json", 25): {
        "Each organ system ages independently with no effect on other systems": "Each organ system ages independently with no effect on other systems because age-related changes are organ-specific and do not produce cascading effects on neighboring or interconnected organ systems",
        "Only the skeletal system declines with age, causing all other symptoms": "Only the skeletal system declines with age through progressive bone density loss, and all other symptoms including reduced cardiac output and cognitive decline are secondary to the skeletal deterioration",
        "Aging only affects organs that have been previously damaged by disease": "Aging only affects organs that have been previously damaged by disease or injury, and organs that have remained healthy throughout life maintain full function indefinitely without any age-related decline",
    },
    ("Unit10/Lesson10.2_Quiz.json", 26): {
        "The rapid pulse is caused by anxiety about the heat, not a physiological response": "The rapid pulse is caused by psychological anxiety about the heat rather than a physiological cardiovascular response, because emotional stress alone can produce tachycardia even without any actual fluid loss or thermoregulatory challenge",
        "Only the muscular system is affected because the cramps are from overuse": "Only the muscular system is affected because the cramps are from mechanical overuse of skeletal muscles during physical labor, and the rapid pulse and sweating are normal baseline variations unrelated to the heat stress",
        "Only the cardiovascular system is affected because blood flow increases during heat exposure": "Only the cardiovascular system is affected because blood flow increases during heat exposure to distribute heat to the skin surface, and the muscle cramps and sweating are unrelated consequences of physical exertion rather than heat stress",
    },
    ("Unit10/Lesson10.2_Quiz.json", 28): {
        "The rapid heart rate is abnormal and indicates the body has stopped compensating": "The rapid heart rate is abnormal and indicates the body has already stopped compensating for the blood loss, meaning the cardiovascular system has completely failed and the patient is in irreversible shock",
        "Only the cardiovascular system responds to hemorrhage, and the other signs are unrelated": "Only the cardiovascular system responds to hemorrhage through increased heart rate and vasoconstriction, and the pale skin, rapid breathing, and concentrated urine are all unrelated findings from other concurrent conditions",
        "Pale skin indicates an allergic reaction to something at the accident scene": "Pale skin indicates an allergic reaction to an environmental allergen at the accident scene rather than peripheral vasoconstriction, and the tachycardia is a response to the allergic reaction rather than the blood loss",
    },
    ("Unit10/Lesson10.2_Quiz.json", 30): {
        "Heart failure caused the COPD, not the other way around": "Heart failure caused the COPD rather than the other way around, because reduced cardiac output leads to chronic pulmonary congestion that damages the airways and produces the obstructive pattern seen on spirometry",
        "COPD only affects the lungs, and the other conditions developed independently": "COPD only affects the lungs through airway obstruction and alveolar destruction, and the heart failure, muscle wasting, and depression all developed independently as separate disease processes",
        "The depression is unrelated to the physical illness": "The depression is an unrelated psychiatric condition that developed independently from the COPD and heart failure, because chronic physical illness has no established physiological or psychological connection to mood disorders",
    },
    # Lesson10.3
    ("Unit10/Lesson10.3_Quiz.json", 3): {
        "The patient has consumed too much dietary fat": "The patient has consumed too much dietary fat, overwhelming the liver's capacity to metabolize lipids and causing excess fatty acid oxidation and ketone body production",
        "Glucose is completely absent from the bloodstream": "Glucose is completely absent from the bloodstream because the pancreas has stopped producing any glucose, and without circulating glucose the body resorts to fat metabolism",
        "The liver stops producing glucose entirely": "The liver stops producing glucose entirely through gluconeogenesis and glycogenolysis, leaving the body completely dependent on fat oxidation for energy",
    },
    ("Unit10/Lesson10.3_Quiz.json", 21): {
        "He has developed pneumonia from a bacterial infection of the lungs": "He has developed pneumonia from a bacterial infection of the lungs, with bacteria colonizing the alveoli and producing purulent exudate that impairs gas exchange and causes the pink frothy sputum",
        "He is experiencing an asthma attack causing airway narrowing": "He is experiencing an asthma attack causing severe bronchospasm and airway narrowing, with mucus plugging and inflammatory edema in the bronchioles producing the crackles and pink frothy sputum",
        "His right ventricle is failing, causing blood to pool in the systemic veins": "His right ventricle is failing, causing blood to pool in the systemic veins and producing peripheral edema, hepatomegaly, and jugular venous distension rather than pulmonary symptoms",
    },
    ("Unit10/Lesson10.3_Quiz.json", 23): {
        "The patient is losing blood volume through internal hemorrhage": "The patient is losing blood volume through internal hemorrhage from a ruptured abdominal organ, and the persistent hypotension reflects ongoing blood loss rather than a vasodilatory state",
        "Antibiotics are causing the low blood pressure as a side effect": "Antibiotics are causing the low blood pressure as a direct pharmacological side effect through vasodilation and myocardial depression, rather than the sepsis itself producing the hemodynamic instability",
        "The heart has stopped pumping and needs vasopressors to restart it": "The heart has stopped pumping effectively and needs vasopressors to restart contractile function, because sepsis has caused direct toxic injury to the myocardial cells rather than peripheral vasodilation",
    },
    ("Unit10/Lesson10.3_Quiz.json", 25): {
        "She is having an allergic reaction to the ACE inhibitor": "She is having an allergic reaction to the ACE inhibitor that is causing systemic vasodilation, angioedema, and hypotension through mast cell degranulation and histamine release, requiring epinephrine rather than medication adjustment",
        "Her heart failure has suddenly worsened and she needs hospitalization": "Her heart failure has suddenly worsened and decompensated into cardiogenic shock, requiring immediate hospitalization for inotropic support and mechanical circulatory assistance rather than outpatient medication adjustment",
        "The dizziness is an unrelated inner ear problem": "The dizziness is an unrelated inner ear problem caused by benign paroxysmal positional vertigo from calcium carbonate crystals dislodged in the semicircular canals, and is completely independent of her medications",
    },
    ("Unit10/Lesson10.3_Quiz.json", 26): {
        "Only the nervous system because the patient feels pain": "Only the nervous system is involved because the patient feels chest pain, and pain transmission through sensory neurons is the sole physiological process affected during a myocardial infarction",
        "Only the respiratory system because the patient is short of breath": "Only the respiratory system is involved because the patient is short of breath, and dyspnea is exclusively a pulmonary problem without any connection to cardiovascular function or perfusion",
        "Only the cardiovascular system is involved since it is a heart attack": "Only the cardiovascular system is involved since it is a heart attack, and myocardial infarction is a purely cardiovascular event that does not trigger responses in the nervous, endocrine, or respiratory systems",
    },
    ("Unit10/Lesson10.3_Quiz.json", 27): {
        "The patient has developed hemophilia from the sepsis infection": "The patient has developed hemophilia from the sepsis infection because the bacterial toxins have caused a genetic mutation in the clotting factor genes, permanently eliminating the ability to produce clotting factors VIII and IX",
        "The patient has two separate conditions: a clotting disorder and a bleeding disorder": "The patient has two separate and unrelated conditions: a hereditary clotting disorder causing the microthrombi and a coincidental acquired bleeding disorder from liver failure causing the oozing from IV sites",
        "The IV antibiotics are causing the bleeding as a drug side effect": "The IV antibiotics are causing the bleeding as a direct drug side effect through inhibition of vitamin K-dependent clotting factor synthesis in the liver, and the microthrombi are from a separate unrelated process",
    },
    ("Unit10/Lesson10.3_Quiz.json", 29): {
        "Only the cardiovascular and nervous systems are involved": "Only the cardiovascular and nervous systems are involved in a hemorrhagic stroke, because bleeding in the brain affects only these two systems and does not produce any consequences for the musculoskeletal, respiratory, or digestive systems",
        "Only the muscular system because the patient has weakness": "Only the muscular system is involved because the patient has right-sided weakness, which indicates a primary muscle disease rather than upper motor neuron damage from the brain hemorrhage",
        "Only the nervous system is affected since stroke is a brain disease": "Only the nervous system is affected since stroke is a brain disease, and all neurological deficits remain confined to the central nervous system without producing any secondary effects on other organ systems",
    },
    # Lesson10.4
    ("Unit10/Lesson10.4_Quiz.json", 15): {
        "A hormone that stimulates red blood cell production": "A hormone that stimulates red blood cell production in the bone marrow, secreted by the kidneys in response to low oxygen levels detected by peritubular interstitial cells",
        "A plasma protein involved in blood clotting": "A plasma protein involved in blood clotting that is synthesized by the liver and circulates in inactive form until the coagulation cascade converts it to fibrin strands",
        "A white blood cell that fights infection": "A white blood cell that fights infection by phagocytosing pathogens and presenting antigens to T helper cells, playing a central role in the adaptive immune response",
    },
    ("Unit10/Lesson10.4_Quiz.json", 23): {
        "Ligaments and muscles heal at exactly the same rate when properly treated": "Ligaments and muscles heal at exactly the same rate when properly treated because all connective tissues share the same regenerative capacity regardless of their blood supply or cellular composition",
        "The ACL is made of bone tissue which takes longer to repair than soft tissue": "The ACL is made of bone tissue rather than dense connective tissue, which takes longer to repair because the process of bone remodeling through osteoblast and osteoclast activity is inherently slower",
        "Ligaments cannot heal at all and always require surgical replacement": "Ligaments cannot heal at all because they lack any regenerative capacity, and every ligament tear requires complete surgical replacement with an autograft or allograft tendon",
    },
    ("Unit10/Lesson10.4_Quiz.json", 24): {
        "Connective tissue, found in tendons and ligaments": "Connective tissue, found in tendons and ligaments, characterized by widely scattered cells in an extensive extracellular matrix with abundant collagen fibers and direct blood supply",
        "Muscle tissue, found in the heart and skeletal muscles": "Muscle tissue, found in the heart and skeletal muscles, characterized by elongated contractile cells containing actin and myosin filaments arranged in sarcomeres for force generation",
        "Nervous tissue, found in the brain and spinal cord": "Nervous tissue, found in the brain and spinal cord, characterized by neurons that generate and conduct electrical impulses and glial cells that provide structural and metabolic support",
    },
    ("Unit10/Lesson10.4_Quiz.json", 25): {
        "Only filtration is impaired; reabsorption and secretion continue normally": "Only filtration is impaired because the glomerular capillaries are damaged, but the tubular epithelial cells remain fully functional and continue normal reabsorption and secretion processes",
        "Only reabsorption is impaired, causing the patient to lose too many nutrients in the urine": "Only reabsorption is impaired because the tubular epithelial cells are damaged, causing the patient to lose excessive nutrients and electrolytes in the urine while filtration and secretion continue normally",
        "The kidneys are only failing to produce erythropoietin; filtration is not affected": "The kidneys are only failing to produce erythropoietin because the peritubular interstitial cells are damaged, and the glomerular filtration, tubular reabsorption, and secretion processes all remain normal",
    },
    ("Unit10/Lesson10.4_Quiz.json", 26): {
        "The motor neurons are dying, similar to ALS": "The motor neurons in the spinal cord and brainstem are dying through a process similar to ALS, causing progressive denervation of skeletal muscles and irreversible loss of voluntary motor function",
        "The muscle fibers themselves are degenerating due to a genetic defect": "The muscle fibers themselves are degenerating due to a genetic defect in the dystrophin protein, causing progressive loss of contractile tissue and replacement with fibrotic scar tissue",
        "The sarcoplasmic reticulum cannot release calcium during muscle contraction": "The sarcoplasmic reticulum cannot release calcium during muscle contraction because the ryanodine receptors are defective, preventing excitation-contraction coupling and producing progressive muscle weakness",
    },
    ("Unit10/Lesson10.4_Quiz.json", 28): {
        "Low FSH and LH only affect mood and energy, not fertility": "Low FSH and LH only affect mood and energy levels through reduced gonadal steroid production, but they have no direct effect on fertility because ovulation occurs independently of gonadotropin levels",
        "Low FSH and LH cause excessive estrogen production that prevents pregnancy": "Low FSH and LH paradoxically cause excessive estrogen production from the ovaries through a compensatory feedback mechanism, and it is the estrogen excess rather than the gonadotropin deficiency that prevents pregnancy",
        "These hormones only affect male fertility and have no role in female reproduction": "These hormones only affect male fertility by stimulating spermatogenesis and testosterone production in the testes, and they have no role in female reproduction because ovulation is controlled by different hormones",
    },
    ("Unit10/Lesson10.4_Quiz.json", 30): {
        "The diuretic directly damaged the heart muscle and skeletal muscles": "The diuretic directly damaged the heart muscle and skeletal muscle fibers through a toxic effect on the contractile proteins, causing structural degeneration of myocardial and skeletal muscle cells independent of electrolyte changes",
        "Lowering blood pressure with diuretics always causes muscle cramps and arrhythmias": "Lowering blood pressure with diuretics always causes muscle cramps and cardiac arrhythmias regardless of the electrolyte balance, because the reduction in blood pressure itself directly impairs muscle and cardiac function",
        "The patient is dehydrated from the diuretic, and dehydration alone causes all these symptoms": "The patient is dehydrated from the diuretic, and dehydration alone causes all of these symptoms through reduced blood volume and tissue perfusion, independent of any specific electrolyte imbalance or ion channel dysfunction",
    },
    # Lesson10.5
    ("Unit10/Lesson10.5_Quiz.json", 3): {
        "Only metabolism and weight changes": "Only metabolism and weight changes from reduced thyroid hormone levels, with no effects on any other organ system beyond the thyroid gland itself",
        "Only the thyroid gland itself": "Only the thyroid gland itself is affected, with structural changes to the gland that do not produce any downstream effects on metabolism, cardiovascular, or nervous function",
        "Only mood and mental function": "Only mood and mental function are affected through reduced neurotransmitter activity, with no effects on heart rate, body weight, skin condition, or muscle strength",
    },
    ("Unit10/Lesson10.5_Quiz.json", 4): {
        "Only the veins in the legs where the clot originated": "Only the veins in the legs where the clot originally formed are affected, because deep venous thrombosis remains localized and does not travel to or impact the pulmonary or cardiovascular systems",
        "Only the lungs with no cardiovascular effects": "Only the lungs are affected by the embolism through mechanical obstruction of airways, with no consequences for the right heart, pulmonary vasculature, or systemic hemodynamics",
        "Only the immune system through inflammatory activation": "Only the immune system is affected through inflammatory activation triggered by the clot, with no consequences for gas exchange, pulmonary vascular resistance, or right ventricular function",
    },
    ("Unit10/Lesson10.5_Quiz.json", 6): {
        "Only loss of bowel and bladder control": "Only loss of bowel and bladder control from damage to the sacral parasympathetic outflow, with preservation of all motor, sensory, and respiratory function below the injury",
        "Only paralysis of the legs with preserved arm function": "Only paralysis of the legs with preserved arm function and completely intact respiratory drive, autonomic regulation, and sensory function in all dermatomes",
        "Only loss of sensation below the injury": "Only loss of sensation below the injury level, with complete preservation of all motor function, autonomic regulation, and respiratory capacity",
    },
    ("Unit10/Lesson10.5_Quiz.json", 7): {
        "Only mild anemia with no other systemic effects": "Only mild anemia with no other systemic effects because sickle hemoglobin functions nearly identically to normal hemoglobin and does not cause vascular occlusion or organ damage",
        "Only pain crises in the bones": "Only pain crises in the bones from vaso-occlusion in the bone marrow vasculature, without affecting the spleen, kidneys, lungs, or central nervous system",
        "Only splenic enlargement and immune system overactivation": "Only splenic enlargement and immune system overactivation from sequestration of sickled cells, without producing anemia, bone pain, renal damage, or pulmonary complications",
    },
    ("Unit10/Lesson10.5_Quiz.json", 10): {
        "Only the skin and underlying muscles at the burn site": "Only the skin and underlying muscles at the burn site are affected, because the thermal injury remains localized and does not produce any systemic inflammatory, cardiovascular, or metabolic consequences",
        "Only fluid balance and temperature regulation": "Only fluid balance and temperature regulation are affected through transepidermal water loss and impaired thermoregulatory sweating, with no consequences for immune function, cardiovascular stability, or renal perfusion",
        "Only the integumentary system since burns are a skin injury": "Only the integumentary system is affected since burns are a skin injury by definition, and the systemic inflammatory response, fluid shifts, and immune suppression are not features of burn pathophysiology",
    },
    ("Unit10/Lesson10.5_Quiz.json", 14): {
        "Chronically elevated blood pressure that damages organs over time": "Chronically elevated blood pressure that damages target organs over time through sustained increases in systemic vascular resistance and left ventricular afterload, leading to progressive end-organ damage",
        "A sudden spike in blood pressure caused by anxiety or stress": "A sudden spike in blood pressure caused by anxiety or stress-related sympathetic activation that produces a transient increase in heart rate and vascular resistance, typically resolving when the stressor is removed",
        "Low blood pressure that only occurs during sleep": "Low blood pressure that only occurs during sleep due to reduced sympathetic tone and decreased cardiac output associated with the normal circadian dip in autonomic nervous system activity",
    },
    ("Unit10/Lesson10.5_Quiz.json", 21): {
        "The runner is experiencing a cardiac arrhythmia unrelated to the exercise or heat": "The runner is experiencing a cardiac arrhythmia that is completely unrelated to the exercise or heat exposure, and the confusion, hot dry skin, and tachycardia are all manifestations of a primary electrical conduction abnormality in the heart",
        "The runner simply ran out of energy and needs to eat a snack": "The runner simply ran out of energy from glycogen depletion and needs to eat a snack to restore blood glucose, and all the symptoms including confusion, tachycardia, and hot skin will resolve with caloric intake alone",
        "Only the muscular system is affected from exercise fatigue": "Only the muscular system is affected from exercise fatigue due to lactic acid accumulation and ATP depletion in the working skeletal muscles, and the cardiovascular, integumentary, and nervous system symptoms are coincidental",
    },
    ("Unit10/Lesson10.5_Quiz.json", 22): {
        "The headache and visual changes are from migraine, not preeclampsia": "The headache and visual changes are from a migraine headache with aura that developed coincidentally during the pregnancy, and they are completely unrelated to the elevated blood pressure or proteinuria findings",
        "Only the kidneys are affected, causing protein to leak into the urine": "Only the kidneys are affected by the condition, causing protein to leak into the urine through damaged glomeruli, and the hypertension, headache, and visual changes are all separate unrelated findings",
        "This is simply normal pregnancy-related hypertension with no multi-system implications": "This is simply normal pregnancy-related hypertension that occurs commonly in the third trimester and has no multi-system implications, requiring only observation without intervention",
    },
    ("Unit10/Lesson10.5_Quiz.json", 23): {
        "The edema is from kidney failure unrelated to the lung disease": "The edema is from primary kidney failure completely unrelated to the chronic lung disease, because renal dysfunction developed independently and the pulmonary hypertension is not connected to the chronic hypoxia",
        "Left-sided heart failure occurred first, then caused the right side to fail": "Left-sided heart failure occurred first from a separate process and then caused the right side to fail through backward transmission of elevated pressures, with the COPD being coincidental and unrelated",
        "Smoking directly damages the heart muscle causing right-sided heart failure": "Smoking directly damages the right ventricular myocardium through toxic effects of nicotine and tar on cardiomyocytes, causing right-sided heart failure independent of any pulmonary vascular changes",
    },
    ("Unit10/Lesson10.5_Quiz.json", 24): {
        "These are all coincidental findings unrelated to the prednisone": "These are all coincidental findings completely unrelated to the prednisone therapy, because corticosteroids only suppress the immune system and do not affect bone metabolism, glucose regulation, or wound healing",
        "The lupus itself is causing all of these symptoms, not the prednisone": "The lupus itself is causing all of these symptoms rather than the prednisone, because autoimmune disease directly produces osteoporosis, hyperglycemia, impaired wound healing, and immunosuppression independent of any medication",
        "Prednisone only affects the immune system; the other effects are from a different medication": "Prednisone only affects the immune system through suppression of T cells and cytokine production, and the osteoporosis, hyperglycemia, and impaired wound healing are side effects of a different medication in her regimen",
    },
    ("Unit10/Lesson10.5_Quiz.json", 25): {
        "Only the lungs are affected since the symptoms are respiratory": "Only the lungs are affected since the presenting symptoms are respiratory in nature, and acute chest syndrome in sickle cell disease is a purely pulmonary condition without any hematologic, immunologic, or cardiovascular consequences",
        "This is a simple pneumonia requiring only antibiotics": "This is a simple community-acquired pneumonia requiring only antibiotics, because sickle cell patients develop ordinary lung infections that respond to standard antimicrobial therapy without any unique pathophysiology",
        "The patient is having a heart attack caused by the sickle cell disease": "The patient is having a heart attack caused by sickle cell disease occluding the coronary arteries, and the chest pain, fever, and pulmonary infiltrate are all secondary manifestations of acute myocardial infarction",
    },
    ("Unit10/Lesson10.5_Quiz.json", 26): {
        "The liver failure is causing a stroke that explains the neurological symptoms": "The liver failure is causing a hemorrhagic stroke that explains the neurological symptoms, because portal hypertension leads to cerebrovascular rupture and intracranial hemorrhage rather than metabolic encephalopathy",
        "The confusion is from pain medications and is unrelated to liver function": "The confusion is from pain medications prescribed for abdominal discomfort and is completely unrelated to liver function, because hepatic failure does not produce any neurological effects or cognitive impairment",
        "The liver directly produces neurotransmitters, and failure stops their production": "The liver directly produces neurotransmitters including serotonin and dopamine, and hepatic failure stops their production, causing the confusion, asterixis, and somnolence through neurotransmitter deficiency",
    },
    ("Unit10/Lesson10.5_Quiz.json", 27): {
        "The elevated red blood cell count is causing the sleep apnea by thickening the blood": "The elevated red blood cell count is causing the sleep apnea by thickening the blood and increasing its viscosity, which slows circulation through the pharyngeal vasculature and causes the airway tissue to swell and obstruct",
        "These are four separate, unrelated medical conditions": "These are four separate, completely unrelated medical conditions that developed independently through different pathological mechanisms and are coincidentally present in the same patient",
        "Only the daytime sleepiness is related to sleep apnea; the other findings have different causes": "Only the daytime sleepiness is related to the sleep apnea through disrupted sleep architecture, while the hypertension, elevated red blood cells, and morning headaches all have separate unrelated etiologies",
    },
    ("Unit10/Lesson10.5_Quiz.json", 28): {
        "Blood is leaking externally through the burn wounds causing hemorrhagic shock": "Blood is leaking externally through the burn wounds causing hemorrhagic shock, because the thermal injury disrupts major blood vessels beneath the skin surface and produces significant ongoing external hemorrhage",
        "The patient is losing blood into the burned tissue only, not systemically": "The patient is losing blood into the burned tissue only through localized hemorrhage and hematoma formation, and the systemic hypotension is from pain-related vasovagal syncope rather than distributive shock",
        "The IV fluids are causing fluid overload and heart failure": "The IV fluids are causing fluid overload and acute heart failure by exceeding the heart's ability to handle the volume, and the hypotension is from cardiogenic shock rather than hypovolemia",
    },
    ("Unit10/Lesson10.5_Quiz.json", 29): {
        "The skin cancer was present before the transplant and is coincidental": "The skin cancer was present before the kidney transplant and is purely coincidental, because immunosuppressive drugs do not alter the immune system's ability to perform cancer surveillance",
        "The transplanted kidney produced hormones that caused the skin cancer": "The transplanted kidney produced abnormal hormones that directly stimulated malignant transformation of keratinocytes in the skin, because donor kidney cells can secrete oncogenic growth factors",
        "The immunosuppressive drugs are directly carcinogenic and caused the skin cancer": "The immunosuppressive drugs are directly carcinogenic through DNA-damaging mechanisms similar to chemotherapy agents, and they caused the skin cancer through direct mutagenic effects on keratinocyte DNA",
    },
    ("Unit10/Lesson10.5_Quiz.json", 30): {
        "These three conditions always occur together and cannot exist independently": "These three conditions always occur together as a mandatory triad and cannot exist independently, because destruction of one endocrine gland automatically triggers autoimmune attack on all other endocrine organs",
        "The medications for one condition caused damage to the other endocrine glands": "The medications prescribed for one condition caused iatrogenic damage to the other endocrine glands, because insulin therapy damages the thyroid and thyroid hormone replacement damages the adrenal cortex",
        "Having one endocrine disease directly causes the other endocrine glands to fail": "Having one endocrine disease directly causes the other endocrine glands to fail through a hormonal cascade, because the loss of one hormone disrupts the entire endocrine axis and leads to sequential gland failure",
    },
    # Lesson10.6
    ("Unit10/Lesson10.6_Quiz.json", 6): {
        "Improved function through adaptation": "Improved function through physiological adaptation and compensatory mechanisms that restore normal homeostatic balance over time",
        "Automatic recovery without treatment": "Automatic recovery without treatment as the body's self-healing mechanisms repair the damaged tissues and restore normal organ function",
        "No change in patient condition": "No change in patient condition, with vital signs remaining stable and organ function continuing at the same level indefinitely",
    },
    ("Unit10/Lesson10.6_Quiz.json", 12): {
        "Financial compensation given to patients for participating in clinical trials": "Financial compensation given to patients for participating in clinical trials that test new medications and treatment protocols, providing monetary incentives for research participation",
        "The replacement of damaged tissues with scar tissue": "The replacement of damaged tissues with scar tissue through fibroblast proliferation and collagen deposition, representing the body's permanent structural repair mechanism",
        "The use of medications to treat a disease": "The use of medications to treat a disease by targeting specific molecular pathways, receptors, or enzymes to restore normal physiological function",
    },
    ("Unit10/Lesson10.6_Quiz.json", 17): {
        "A textbook chapter summary": "A textbook chapter summary that condenses key concepts, vocabulary, and clinical correlations from the assigned reading into a concise review format",
        "A type of laboratory equipment used in anatomy courses": "A type of laboratory equipment used in anatomy courses for dissection, histological examination, and physiological measurement of organ system function",
        "A type of exam question format": "A type of exam question format that tests higher-order thinking skills through clinical scenarios requiring integration of multiple organ system concepts",
    },
    ("Unit10/Lesson10.6_Quiz.json", 21): {
        "Copying a diagram from a textbook without any original analysis": "Copying a diagram from a textbook without any original analysis, reorganization, or integration of concepts across organ systems to demonstrate personal understanding of the material",
        "Listing each organ system on a separate page without showing connections between them": "Listing each organ system on a separate page without showing any connections, feedback loops, or pathophysiological relationships between them to demonstrate integrated understanding",
        "Only describing the pancreatic pathology without connecting to other systems": "Only describing the pancreatic pathology without connecting it to the downstream cardiovascular, renal, neurological, or integumentary complications that result from chronic hyperglycemia",
    },
    ("Unit10/Lesson10.6_Quiz.json", 23): {
        "Only adding surgical intervention as an additional treatment option": "Only adding surgical intervention as an additional treatment option, such as surgical drainage of infected tissue, without addressing the cardiovascular, respiratory, renal, or hematologic complications of sepsis",
        "No expansion is needed since antibiotics are the only treatment for sepsis": "No expansion is needed since antibiotics are the only treatment required for sepsis, and the hemodynamic instability, respiratory failure, and organ dysfunction all resolve automatically once the infection is controlled",
        "Adding alternative medicine therapies to complement the antibiotics": "Adding alternative medicine therapies such as herbal supplements and acupuncture to complement the antibiotics, without addressing the multi-organ physiological derangements that characterize severe sepsis",
    },
    ("Unit10/Lesson10.6_Quiz.json", 24): {
        "Decompensated shock only occurs in elderly patients": "Decompensated shock only occurs in elderly patients because younger individuals have sufficient physiological reserve to maintain compensation indefinitely regardless of the severity of blood loss or hemodynamic insult",
        "Compensated shock always occurs after decompensated shock": "Compensated shock always occurs after decompensated shock as a recovery phase, because the body first experiences organ failure and then gradually activates compensatory mechanisms to restore blood pressure",
        "Compensated and decompensated shock are the same thing with different names": "Compensated and decompensated shock are the same pathophysiological condition with different names used interchangeably, because there is no clinically meaningful distinction between the two stages",
    },
    ("Unit10/Lesson10.6_Quiz.json", 25): {
        "Only adding the cardiovascular system since COPD and heart disease are related": "Only adding the cardiovascular system since COPD and heart disease are related through cor pulmonale, without addressing the musculoskeletal, hematologic, or neuropsychiatric consequences of chronic hypoxia",
        "Adding information about the digestive and reproductive systems even though COPD has minimal impact on them": "Adding information about the digestive and reproductive systems even though COPD has minimal direct impact on them, because including every organ system demonstrates thoroughness regardless of relevance",
        "Adding brief mentions of the heart, muscles, and brain without explaining pathophysiological connections": "Adding brief mentions of the heart, muscles, and brain without explaining the pathophysiological connections between chronic hypoxia, systemic inflammation, and the specific mechanisms causing dysfunction",
    },
    ("Unit10/Lesson10.6_Quiz.json", 27): {
        "The heart pumps extra fluid into the legs when it is failing": "The heart pumps extra fluid directly into the legs when it is failing because the weakened ventricle redirects blood flow preferentially to the lower extremities rather than to the vital organs",
        "Gravity pulls blood into the legs because the heart is too weak to pump it back up": "Gravity pulls blood into the legs because the heart is too weak to pump it back up against gravitational force, and the fluid simply accumulates due to the mechanical failure of venous return",
        "Leg swelling is unrelated to heart failure and is caused by a separate kidney problem": "Leg swelling is unrelated to heart failure and is caused by a separate primary kidney problem that impairs sodium and water excretion independently of the cardiovascular hemodynamic changes",
    },
    ("Unit10/Lesson10.6_Quiz.json", 28): {
        "Only the musculoskeletal system is additionally affected through paralysis": "Only the musculoskeletal system is additionally affected through paralysis from spinal cord compression, because traumatic brain injury does not produce endocrine, respiratory, cardiovascular, or immune dysfunction",
        "TBI only affects the nervous system because it is a brain injury": "TBI only affects the nervous system because it is a brain injury confined to the cranial vault, and the pathology does not extend to any peripheral organ systems or produce systemic complications",
        "TBI only affects the cardiovascular system through changes in blood pressure": "TBI only affects the cardiovascular system through changes in blood pressure regulation from damaged baroreceptor pathways, without producing any endocrine, respiratory, digestive, or immune consequences",
    },
    ("Unit10/Lesson10.6_Quiz.json", 29): {
        "Because listing all the organs affected shows thorough memorization": "Because listing all the organs affected by sickle cell disease shows thorough memorization of the clinical manifestations, which is the highest level of understanding expected in an anatomy course",
        "Because mentioning the genetic mutation is enough to explain the disease": "Because mentioning the genetic mutation in the beta-globin gene is sufficient to explain the entire disease, since identifying the molecular cause demonstrates complete understanding of the condition",
        "Because the student included many references from peer-reviewed sources": "Because the student included many references from peer-reviewed sources in their case study, which demonstrates research skills that are more important than understanding pathophysiological mechanisms",
    },
    ("Unit10/Lesson10.6_Quiz.json", 30): {
        "It does not better prepare students; exams are always superior for learning": "It does not better prepare students for clinical practice because traditional examinations are always superior for learning, and standardized testing is the most effective method for developing clinical reasoning",
        "Only students pursuing medical school benefit from this type of project": "Only students pursuing medical school benefit from this type of integrative capstone project, because other healthcare professionals such as nurses, therapists, and technicians do not need systems-level thinking",
        "Capstone projects are easier than exams and give students more time": "Capstone projects are easier than traditional examinations and simply give students more time to complete the work, without requiring any additional critical thinking, integration, or clinical reasoning skills",
    },
    # Lesson10.7
    ("Unit10/Lesson10.7_Quiz.json", 11): {
        "Any position the patient assumes during a physical examination": "Any position the patient assumes during a physical examination, including seated, supine, and lateral decubitus positions used for different assessment purposes",
        "Sitting in a chair with arms crossed": "Sitting upright in a chair with arms crossed over the chest, commonly used during respiratory assessment and posterior lung auscultation",
        "Lying face down on an examination table": "Lying face down (prone) on an examination table, commonly used for examination of the posterior thorax, spine, and gluteal region",
    },
    ("Unit10/Lesson10.7_Quiz.json", 12): {
        "The study of gross anatomical structures visible to the naked eye": "The study of gross anatomical structures visible to the naked eye, including organ morphology, regional relationships, and surface anatomy used in clinical examination",
        "The study of chemical reactions within living cells": "The study of chemical reactions within living cells, including metabolic pathways, enzyme kinetics, and the biochemical basis of cellular energy production",
        "The study of human history and evolution": "The study of human history and evolution, including comparative anatomy, phylogenetic relationships, and the developmental origins of anatomical structures",
    },
    ("Unit10/Lesson10.7_Quiz.json", 21): {
        "Each symptom represents a different, unrelated disease process": "Each symptom represents a different, unrelated disease process: the tingling is from carpal tunnel syndrome, the foot ulcer is from peripheral vascular disease, and the blurry vision is from age-related macular degeneration",
        "Only the foot ulcer is related to diabetes; the other symptoms are from aging": "Only the foot ulcer is related to diabetes through impaired wound healing, and the tingling in the hands and blurry vision are normal age-related changes unrelated to the chronic hyperglycemia",
        "The blurry vision caused the patient to injure his foot, and the tingling is from the foot injury": "The blurry vision caused the patient to injure his foot by tripping due to impaired visual acuity, and the tingling in his hands is referred pain from the foot injury rather than a separate neurological process",
    },
    ("Unit10/Lesson10.7_Quiz.json", 22): {
        "Metabolic acidosis with respiratory compensation": "Metabolic acidosis with respiratory compensation, characterized by low bicarbonate from metabolic acid production with secondary hyperventilation to lower CO2 and partially normalize pH",
        "Respiratory alkalosis from hyperventilation": "Respiratory alkalosis from hyperventilation, characterized by low pCO2 from excessive ventilation with compensatory renal excretion of bicarbonate to bring pH back toward normal",
        "Metabolic alkalosis from excessive bicarbonate": "Metabolic alkalosis from excessive bicarbonate accumulation, characterized by elevated HCO3 from prolonged vomiting or diuretic use with compensatory hypoventilation to retain CO2",
    },
    ("Unit10/Lesson10.7_Quiz.json", 23): {
        "The patient is allergic to the blood products causing an immune-mediated calcium loss": "The patient is allergic to the blood products causing an immune-mediated calcium loss through mast cell degranulation and histamine release that triggers parathyroid suppression and accelerated renal calcium excretion",
        "The blood transfusion directly destroyed the patient's parathyroid glands": "The blood transfusion directly destroyed the patient's parathyroid glands through a transfusion-related autoimmune reaction that targets parathyroid tissue, permanently eliminating PTH production",
        "Massive transfusion always causes permanent calcium deficiency": "Massive transfusion always causes permanent calcium deficiency because the stored blood products deplete the body's total calcium reserves irreversibly, requiring lifelong calcium and vitamin D supplementation",
    },
    ("Unit10/Lesson10.7_Quiz.json", 24): {
        "A map showing only the kidneys filtering blood to regulate pressure": "A map showing only the kidneys filtering blood to regulate pressure through adjustments in urine output volume, without including baroreceptors, cardiac output, hormonal regulation, or vascular resistance",
        "A map showing only the heart pumping blood through arteries": "A map showing only the heart pumping blood through arteries to generate pressure, without including the kidneys, hormones, autonomic nervous system, or vascular compliance contributions",
        "A map listing medications that treat hypertension without explaining mechanisms": "A map listing medications that treat hypertension such as ACE inhibitors, beta-blockers, and diuretics, without explaining the physiological mechanisms they target or their effects on the integrated regulatory system",
    },
    ("Unit10/Lesson10.7_Quiz.json", 25): {
        "The adrenal glands only produce adrenaline, so failure only causes fatigue": "The adrenal glands only produce adrenaline from the medulla, so adrenal failure only causes fatigue from reduced catecholamine output without affecting sodium balance, potassium regulation, or skin pigmentation",
        "Each symptom is caused by a different disease process": "Each symptom is caused by a different, unrelated disease process: the fatigue is from chronic fatigue syndrome, the hypotension is from cardiac disease, and the hyperpigmentation is from a skin condition",
        "Skin hyperpigmentation is an allergic reaction unrelated to adrenal function": "Skin hyperpigmentation is an allergic reaction to environmental allergens that is completely unrelated to adrenal function, ACTH levels, or melanocyte-stimulating hormone production",
    },
    ("Unit10/Lesson10.7_Quiz.json", 26): {
        "Only the integumentary system responds because the skin is what contacts the ice": "Only the integumentary system responds because the skin is what directly contacts the ice, and the response is limited to local temperature sensation without involving the nervous, cardiovascular, muscular, or endocrine systems",
        "Only the nervous system is involved because it detects the cold sensation": "Only the nervous system is involved because it detects the cold sensation through peripheral thermoreceptors, and the neural response does not trigger any cardiovascular, muscular, or endocrine responses",
        "Only the cardiovascular system responds through vasoconstriction": "Only the cardiovascular system responds through local vasoconstriction of cutaneous arterioles, without involving thermoreceptors, shivering, or stress hormone release from any other system",
    },
    ("Unit10/Lesson10.7_Quiz.json", 27): {
        "The ribcage of a premature infant is too rigid to expand during breathing": "The ribcage of a premature infant is too rigid to expand during breathing because premature cartilage ossifies prematurely, creating a stiff thorax that cannot generate adequate negative pressure for inspiration",
        "The premature infant's airways are too small to allow air passage": "The premature infant's airways are too small to allow adequate air passage because the bronchial tree has not yet developed sufficient luminal diameter, creating prohibitive airway resistance to flow",
        "The premature infant has an undeveloped diaphragm that cannot contract": "The premature infant has an undeveloped diaphragm that cannot contract effectively because diaphragmatic muscle fiber maturation occurs late in gestation and is incomplete in premature neonates",
    },
    ("Unit10/Lesson10.7_Quiz.json", 28): {
        "The patient has four separate, unrelated medical conditions": "The patient has four separate, unrelated medical conditions that developed through independent pathological mechanisms and are coincidentally present simultaneously without any shared etiology",
        "The hypertension caused all the other conditions independently": "The hypertension caused all the other conditions independently through sustained elevated blood pressure that directly produced the polycythemia, sleep disruption, and cognitive impairment through separate mechanisms",
        "Only the elevated red blood cell count is related to sleep apnea": "Only the elevated red blood cell count is related to the sleep apnea through chronic hypoxia-stimulated EPO production, while the hypertension, cardiac changes, and cognitive impairment are unrelated",
    },
    ("Unit10/Lesson10.7_Quiz.json", 29): {
        "The immune system and skeletal system are the primary systems involved in digestion": "The immune system and skeletal system are the primary systems involved in digestion because gut-associated lymphoid tissue drives nutrient processing and skeletal muscle generates the chewing forces that initiate breakdown",
        "Food enters the stomach, gets digested, and nutrients are absorbed": "Food enters the stomach where it is completely digested by gastric acid alone, and nutrients are absorbed directly through the stomach wall into the bloodstream without involvement of any other organ system",
        "Only the digestive system is involved in eating a meal": "Only the digestive system is involved in eating a meal because the mechanical and chemical breakdown of food occurs entirely within the GI tract without requiring input from the nervous, endocrine, or cardiovascular systems",
    },
    ("Unit10/Lesson10.7_Quiz.json", 30): {
        "Integration is only important for doctors, not nurses or other healthcare professionals": "Integration is only important for doctors who make diagnostic decisions, not for nurses or other healthcare professionals whose roles do not require understanding how disease in one organ system affects others",
        "Studying systems in isolation is actually more effective for clinical practice": "Studying systems in isolation is actually more effective for clinical practice because mastering each organ system individually provides a stronger foundation than attempting to understand complex inter-system relationships",
        "It helps only with memorizing facts for the AP exam and has no real-world application": "It helps only with memorizing facts for the AP exam and has no real-world application in clinical settings, because actual patient care relies on protocol-based algorithms rather than integrated physiological understanding",
    },
}

files_modified = set()
for (rel_path, qnum), text_map in replacements.items():
    full_path = os.path.join(base, rel_path)
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for q in data['quiz_questions']:
        if q['question_number'] == qnum:
            for opt in q['options']:
                if not opt['is_correct'] and opt['text'] in text_map:
                    opt['text'] = text_map[opt['text']]
            break

    with open(full_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    files_modified.add(full_path)

print(f"Modified {len(files_modified)} files")

# Verify
files = sorted(glob.glob(os.path.join(base, 'Unit10', '*Quiz*.json')))
still_flagged = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    for q in data['quiz_questions']:
        correct_text = ''
        wrong_texts = []
        for opt in q['options']:
            if opt['is_correct']:
                correct_text = opt['text']
            else:
                wrong_texts.append(opt['text'])
        if not wrong_texts: continue
        cl = len(correct_text)
        awl = sum(len(w) for w in wrong_texts) / len(wrong_texts)
        if awl > 0 and cl / awl >= 3.0:
            still_flagged += 1
            print(f'STILL FLAGGED: {os.path.basename(f)} Q{q["question_number"]}: ratio={cl/awl:.1f}')
if still_flagged == 0:
    print("Unit 10: ALL CLEAR!")
else:
    print(f"Unit 10: {still_flagged} still flagged")
