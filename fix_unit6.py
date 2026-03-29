import json, os, glob

base = 'content_data/AnatomyLessons'

replacements = {
    # Lesson6.1
    ("Unit6/Lesson6.1_Quiz.json", 8): {
        "Kidneys": "Kidneys (renal parenchyma tissue)",
        "Lungs": "Lungs (pulmonary parenchyma)",
        "Brain": "Brain (cerebral cortex neurons)",
    },
    ("Unit6/Lesson6.1_Quiz.json", 9): {
        "Heart enlargement": "Pathological heart enlargement and dilation of chambers",
        "Semilunar valve closure": "Semilunar valve closure at the aortic and pulmonary roots",
        "Blood from flowing forward": "Blood from flowing forward through the great arteries during systole",
    },
    ("Unit6/Lesson6.1_Quiz.json", 16): {
        "A valve in the right ventricle": "A valve located between the right ventricle and the pulmonary trunk that prevents backflow",
        "A nerve that controls heart rate": "A branch of the vagus nerve that controls heart rate by innervating the sinoatrial node",
        "A coronary blood vessel": "A coronary blood vessel that supplies oxygenated blood to the right atrium and ventricle",
    },
    ("Unit6/Lesson6.1_Quiz.json", 17): {
        "A chamber of the heart": "A chamber of the heart that receives oxygenated blood from the pulmonary veins before ejecting it into systemic circulation",
        "Part of the aorta": "Part of the ascending aorta that gives rise to the coronary arteries and distributes oxygenated blood to the systemic circulation",
        "An artery that supplies blood to the heart": "An artery that supplies oxygenated blood to the myocardium, branching from the aorta just above the aortic semilunar valve",
    },
    ("Unit6/Lesson6.1_Quiz.json", 30): {
        "Aortic stenosis": "Aortic stenosis with narrowing of the aortic valve restricting left ventricular outflow",
        "Pulmonary artery stenosis": "Pulmonary artery stenosis with narrowing of the pulmonary valve restricting right ventricular outflow",
        "Complete heart block": "Complete heart block with dissociation between atrial and ventricular electrical activity",
    },
    # Lesson6.2
    ("Unit6/Lesson6.2_Quiz.json", 3): {
        "Blood storage": "Blood storage in venous reservoirs during low-demand states",
        "Blood cell production": "Blood cell production through hematopoiesis in bone marrow",
        "Hormone production": "Hormone production and endocrine signaling to target organs",
    },
    # Lesson6.5
    ("Unit6/Lesson6.5_Quiz.json", 3): {
        "Blood oxygen levels": "Blood oxygen saturation levels via peripheral chemoreceptors",
        "Body temperature": "Core body temperature via hypothalamic thermoreceptors",
        "Blood glucose levels": "Blood glucose concentration via pancreatic islet sensors",
    },
    ("Unit6/Lesson6.5_Quiz.json", 4): {
        "High blood glucose": "High blood glucose triggering insulin release from the pancreas",
        "High blood pressure": "High blood pressure causing the kidneys to excrete sodium",
        "High calcium levels": "High calcium levels triggering calcitonin from the thyroid",
    },
    ("Unit6/Lesson6.5_Quiz.json", 9): {
        "Blood pressure is low": "Blood pressure is low, triggering renal renin release and sympathetic activation to restore pressure",
        "Dehydration occurs": "Dehydration occurs, triggering ADH release from the posterior pituitary to increase water reabsorption",
        "Heart rate drops below 60 bpm": "Heart rate drops below 60 bpm, triggering sympathetic stimulation of the SA node to increase contractile frequency",
    },
    ("Unit6/Lesson6.5_Quiz.json", 10): {
        "Only excessive exercise": "Only excessive exercise beyond the body's cardiovascular capacity to adapt",
        "Only advanced age": "Only advanced age and the accompanying decline in vascular elasticity",
        "Only genetics": "Only inherited genetic polymorphisms affecting renal sodium handling",
    },
    ("Unit6/Lesson6.5_Quiz.json", 12): {
        "The simple average of systolic and diastolic pressure": "The simple average of systolic and diastolic pressure calculated by adding both values and dividing by two, used as a quick clinical approximation of perfusion pressure",
        "The pressure only in the pulmonary arteries": "The pressure measured only in the pulmonary arteries during right heart catheterization, used to assess right ventricular function and pulmonary vascular resistance",
        "The maximum pressure during exercise": "The maximum arterial pressure achieved during peak exercise stress testing, used to evaluate cardiovascular fitness and detect exercise-induced ischemia",
    },
    ("Unit6/Lesson6.5_Quiz.json", 19): {
        "Rapid heart rate exceeding 150 bpm": "Rapid heart rate exceeding 150 beats per minute, known as supraventricular tachycardia, caused by an abnormal electrical circuit",
        "Chronic high blood pressure": "Chronic high blood pressure exceeding 140/90 mmHg, known as hypertension, caused by increased vascular resistance",
        "Chest pain during exercise": "Chest pain occurring during physical exercise, known as angina pectoris, caused by reduced coronary blood flow to the myocardium",
    },
    # Lesson6.6
    ("Unit6/Lesson6.6_Quiz.json", 3): {
        "Only leg swelling": "Only leg swelling and peripheral edema caused by right-sided venous congestion and elevated hydrostatic pressure",
        "Only a headache": "Only a headache and dizziness caused by temporary cerebral vasospasm and reduced blood flow to the occipital cortex",
        "Only mild fatigue": "Only mild fatigue and general malaise caused by reduced cardiac output and diminished oxygen delivery to skeletal muscles",
    },
    ("Unit6/Lesson6.6_Quiz.json", 6): {
        "Only a sedentary lifestyle": "Only a sedentary lifestyle with prolonged inactivity reducing cardiovascular fitness",
        "Only advanced age": "Only advanced age and the associated loss of vascular elasticity over time",
        "Only genetics": "Only inherited genetic factors predisposing to lipid metabolism abnormalities",
    },
    ("Unit6/Lesson6.6_Quiz.json", 8): {
        "It deposits cholesterol in arteries": "It deposits cholesterol in arterial walls by infiltrating the endothelium and contributing to fatty streak formation and plaque buildup",
        "It has no function in the body": "It has no function in the body and is merely an incidental byproduct of hepatic lipoprotein metabolism with no physiological role",
        "It increases blood clotting": "It increases blood clotting by stimulating platelet aggregation and activating the coagulation cascade at sites of vascular injury",
    },
    ("Unit6/Lesson6.6_Quiz.json", 9): {
        "Headaches and blurred vision": "Headaches and blurred vision from cerebrovascular insufficiency and reduced retinal perfusion",
        "Arm swelling and numbness": "Arm swelling and numbness from compromised venous return and peripheral nerve compression",
        "Chest pain at rest": "Chest pain at rest from coronary vasospasm reducing myocardial perfusion",
    },
    ("Unit6/Lesson6.6_Quiz.json", 13): {
        "A narrowing of the aortic valve": "A narrowing of the aortic valve caused by calcific degeneration, restricting blood flow from the left ventricle into the ascending aorta",
        "A blood clot in the aorta": "A blood clot that forms within the aortic lumen, partially or completely obstructing blood flow and posing a risk of distal embolization",
        "A normal widening of the aorta with age": "A normal physiological widening of the aorta that occurs gradually with age due to elastic fiber degradation, requiring no intervention",
    },
    ("Unit6/Lesson6.6_Quiz.json", 14): {
        "An ECG recording technique": "An ECG recording technique that uses surface electrodes to measure the electrical activity of the heart and detect rhythm abnormalities and ischemic changes",
        "A blood pressure measurement technique": "A blood pressure measurement technique that uses an arterial catheter to provide continuous real-time monitoring of systolic and diastolic pressures in critically ill patients",
        "A non-invasive ultrasound of the heart": "A non-invasive ultrasound of the heart that uses sound waves to visualize chamber size, wall motion, valve function, and ejection fraction in real time",
    },
    ("Unit6/Lesson6.6_Quiz.json", 16): {
        "A surgical procedure to replace heart valves": "A surgical procedure to replace damaged or diseased heart valves with mechanical or bioprosthetic substitutes, restoring normal unidirectional blood flow",
        "A type of external defibrillator": "A type of external defibrillator that delivers electrical shocks through chest wall electrodes to terminate life-threatening ventricular arrhythmias",
        "A medication that controls heart rhythm": "A medication that controls heart rhythm by modifying the electrical conduction properties of the myocardium through ion channel blockade or autonomic modulation",
    },
    ("Unit6/Lesson6.6_Quiz.json", 18): {
        "A type of heart transplant procedure": "A type of heart transplant procedure in which the failing heart is replaced with a donor organ from a brain-dead patient to restore normal cardiac function",
        "A therapy that reduces blood volume": "A therapy that reduces blood volume through therapeutic phlebotomy or diuretic administration to decrease cardiac preload and relieve congestion symptoms",
        "A therapy that permanently increases heart rate": "A therapy that permanently increases heart rate by implanting a device that continuously stimulates the sinoatrial node to maintain adequate cardiac output",
    },
    ("Unit6/Lesson6.6_Quiz.json", 19): {
        "Increased blood cell production": "Increased blood cell production by the bone marrow in response to chronic hypoxia, resulting in polycythemia and elevated blood viscosity",
        "A heart rhythm abnormality": "A heart rhythm abnormality characterized by irregular electrical impulses originating from the atria or ventricles, disrupting normal cardiac synchrony",
        "A type of blood clot": "A type of blood clot that forms within the deep venous system of the lower extremities, posing a risk of pulmonary embolism if dislodged",
    },
    ("Unit6/Lesson6.6_Quiz.json", 21): {
        "Aspirin lowers blood pressure rapidly": "Aspirin lowers blood pressure rapidly by dilating peripheral arteries through direct smooth muscle relaxation, reducing afterload on the left ventricle",
        "Aspirin reduces chest pain by acting as an analgesic": "Aspirin reduces chest pain by acting as a pure analgesic that blocks pain signals at the level of the central nervous system, without affecting the underlying cardiac pathology",
        "Aspirin dissolves the existing blood clot": "Aspirin dissolves the existing blood clot by activating the fibrinolytic system and converting plasminogen to plasmin, which enzymatically breaks down the fibrin mesh",
    },
    ("Unit6/Lesson6.6_Quiz.json", 22): {
        "Anxiety causing hyperventilation during sleep": "Anxiety causing hyperventilation during sleep that lowers arterial CO2 levels and produces respiratory alkalosis, leading to a subjective feeling of breathlessness",
        "A blood clot traveled to the lungs during sleep": "A blood clot that traveled from the deep leg veins to the lungs during sleep, causing acute pulmonary embolism with sudden-onset dyspnea and pleuritic chest pain",
        "Sleep apnea blocking the airway": "Obstructive sleep apnea blocking the upper airway during sleep, causing repeated episodes of hypoxia and arousal with gasping respirations",
    },
    ("Unit6/Lesson6.6_Quiz.json", 25): {
        "CABG is always less invasive than stenting": "CABG is always less invasive than percutaneous stenting because it uses smaller incisions and does not require opening the chest, making it safer for high-risk patients with multiple comorbidities",
        "Stents cannot be placed in arteries larger than 3 mm": "Stents cannot be placed in arteries larger than 3 mm in diameter because the expanded metal mesh would fail to achieve adequate wall apposition and would be prone to migration and embolization",
        "Stenting is never effective for coronary artery blockages": "Stenting is never effective for any coronary artery blockages because the restenosis rate is nearly 100 percent within six months, regardless of drug-eluting or bare-metal stent design",
    },
    ("Unit6/Lesson6.6_Quiz.json", 26): {
        "Right-sided failure causes fluid to leak into the lungs": "Right-sided failure causes fluid to leak into the lungs because elevated right ventricular pressure is transmitted retrograde through the pulmonary veins into the pulmonary capillary bed",
        "Right-sided failure only affects the brain, causing confusion": "Right-sided failure only affects the brain, causing confusion and altered mental status because reduced cardiac output leads to inadequate cerebral perfusion without any peripheral effects",
        "Leg swelling is caused by blocked arteries, not heart failure": "Leg swelling is caused by blocked peripheral arteries rather than heart failure, because arterial occlusion prevents blood from leaving the legs and causes fluid to pool in the interstitial spaces",
    },
    ("Unit6/Lesson6.6_Quiz.json", 28): {
        "It only causes mild coughing that resolves on its own": "It only causes mild coughing that resolves on its own as the body's fibrinolytic system gradually dissolves the clot, and no medical treatment is needed",
        "It blocks blood flow to the brain, causing a stroke": "It blocks blood flow to the brain by lodging in a cerebral artery, causing an embolic stroke with sudden neurological deficits including hemiplegia and aphasia",
        "It causes the aorta to rupture": "It causes the aorta to rupture by lodging in the aortic wall and weakening the vessel lining, leading to acute aortic dissection and massive hemorrhage",
    },
    ("Unit6/Lesson6.6_Quiz.json", 30): {
        "Warfarin helps the body accept the foreign valve material": "Warfarin helps the body accept the foreign valve material by modulating the immune response and preventing the formation of antibodies against the prosthetic surface",
        "Warfarin prevents the mechanical valve from calcifying": "Warfarin prevents the mechanical valve from calcifying by inhibiting calcium-dependent enzymes that deposit hydroxyapatite crystals on the prosthetic valve leaflets",
        "Warfarin reduces the risk of infection on the valve": "Warfarin reduces the risk of bacterial infection on the valve by maintaining smooth laminar flow across the prosthetic surface and preventing biofilm formation",
    },
    # Lesson6.7
    ("Unit6/Lesson6.7_Quiz.json", 2): {
        "Normal heart health": "Normal heart health with intact myocardial tissue integrity",
        "Liver disease": "Liver disease with hepatocellular damage and enzyme release",
        "Kidney disease only": "Kidney disease with glomerular filtration impairment only",
    },
    ("Unit6/Lesson6.7_Quiz.json", 5): {
        "Administering medication only without any procedure": "Administering intravenous thrombolytic medication only to dissolve the clot without any catheter-based intervention",
        "Heart transplant": "Heart transplant in which the entire failing heart is surgically replaced with a healthy donor organ",
        "Open heart surgery with bypass grafts": "Open heart surgery with bypass grafts using saphenous vein or internal mammary artery conduits",
    },
    ("Unit6/Lesson6.7_Quiz.json", 16): {
        "Treatment limited to surgical interventions": "Treatment limited exclusively to surgical and catheter-based interventions performed by interventional cardiologists and cardiac surgeons",
        "Care provided solely by a cardiologist": "Care provided solely by a cardiologist who manages all aspects of the patient's cardiac and non-cardiac health independently",
        "Care provided only by the patient's primary care physician": "Care provided only by the patient's primary care physician without any specialist consultation or multidisciplinary team involvement",
    },
    ("Unit6/Lesson6.7_Quiz.json", 23): {
        "Only one troponin measurement is needed to diagnose MI": "Only one troponin measurement taken at the time of admission is needed to diagnose MI, because troponin levels peak immediately at the onset of chest pain",
        "Troponin levels decrease during an MI": "Troponin levels decrease during an MI because the damaged heart muscle actively reabsorbs the released troponin protein back into the surviving myocardial cells",
        "Troponin levels are always immediately elevated in an MI": "Troponin levels are always immediately elevated at the exact moment chest pain begins during an MI, so a negative initial test definitively rules out myocardial infarction",
    },
    ("Unit6/Lesson6.7_Quiz.json", 25): {
        "Only the aspirin is truly necessary; the rest are optional": "Only the aspirin is truly necessary after the procedure; the statin, beta-blocker, and ACE inhibitor are all optional supplements that provide no proven cardiovascular benefit",
        "These medications are only needed for the first week after the procedure": "These medications are only needed for the first week after the procedure to prevent immediate complications, and can be safely discontinued once the stent has fully endothelialized",
        "The medications all do the same thing and are redundant": "The medications all do the same thing by thinning the blood and reducing clotting risk, making the combination redundant and unnecessarily increasing the risk of bleeding",
    },
    ("Unit6/Lesson6.7_Quiz.json", 29): {
        "Only increasing the diuretic dose without any education": "Only increasing the diuretic dose without any patient education, as pharmacological management alone is sufficient to prevent all future heart failure readmissions",
        "Keeping the patient hospitalized indefinitely": "Keeping the patient hospitalized indefinitely until all symptoms resolve completely, as outpatient management of heart failure is unsafe and unreliable",
        "Prescribing stronger pain medication": "Prescribing stronger pain medication to mask the symptoms of fluid overload, as symptom control is the primary goal and weight monitoring is unnecessary",
    },
    # Lesson6.8
    ("Unit6/Lesson6.8_Quiz.json", 17): {
        "A normal variant in young patients": "A normal variant in young patients reflecting efficient rapid ventricular conduction through the bundle of His and Purkinje fibers",
        "Atrial fibrillation": "Atrial fibrillation with chaotic and disorganized electrical activity originating from multiple foci within the atrial myocardium",
        "Normal, fast conduction through the ventricles": "Normal, fast conduction through the ventricles via the His-Purkinje system, producing a narrow and efficient QRS complex pattern",
    },
    ("Unit6/Lesson6.8_Quiz.json", 18): {
        "The time between two consecutive QRS complexes": "The time between two consecutive QRS complexes, representing the complete cardiac cycle duration and used to calculate instantaneous heart rate",
        "The duration of the T wave": "The duration of the T wave, representing the time required for complete ventricular repolarization as potassium ions flow out of the myocardial cells",
        "The time from ventricular depolarization to repolarization": "The time from ventricular depolarization to repolarization, representing the total duration of ventricular electrical activity during the cardiac cycle",
    },
    ("Unit6/Lesson6.8_Quiz.json", 27): {
        "It indicates the heart is beating too fast": "It indicates the heart is beating too fast, with a ventricular rate exceeding 100 beats per minute that may require pharmacological rate control or cardioversion",
        "It means the P wave is absent": "It means the P wave is absent, indicating that the sinoatrial node has failed and an ectopic pacemaker in the AV node or ventricle has assumed control of the heart rhythm",
        "It indicates first-degree AV block": "It indicates first-degree AV block, where conduction through the AV node is delayed but every atrial impulse still reaches the ventricles with a prolonged PR interval",
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
files = sorted(glob.glob(os.path.join(base, 'Unit6', '*Quiz*.json')))
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
    print("Unit 6: ALL CLEAR!")
else:
    print(f"Unit 6: {still_flagged} still flagged")
