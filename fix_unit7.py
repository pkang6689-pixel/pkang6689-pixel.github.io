import json, os, glob

base = 'content_data/AnatomyLessons'

replacements = {
    # Lesson7.1
    ("Unit7/Lesson7.1_Quiz.json", 11): {
        "The thick muscular wall of the bronchi": "The thick muscular wall of the bronchi that regulates airway diameter through smooth muscle contraction and relaxation",
        "The pleural membrane surrounding each lung": "The pleural membrane surrounding each lung, composed of visceral and parietal layers with lubricating serous fluid between them",
        "The cartilaginous lining of the trachea": "The cartilaginous C-shaped rings lining the trachea that maintain airway patency and prevent collapse during negative-pressure breathing",
    },
    ("Unit7/Lesson7.1_Quiz.json", 18): {
        "The blood vessel network supplying the lungs": "The blood vessel network supplying the lungs, consisting of pulmonary arteries carrying deoxygenated blood and pulmonary veins returning oxygenated blood to the left atrium",
        "The network of alveolar ducts and sacs within the lungs": "The network of alveolar ducts and sacs within the lungs where the final gas exchange surfaces are located, representing the terminal respiratory zone",
        "The lymphatic drainage system of the thorax": "The lymphatic drainage system of the thorax that collects interstitial fluid, filters pathogens through mediastinal lymph nodes, and returns fluid to the venous circulation",
    },
    ("Unit7/Lesson7.1_Quiz.json", 25): {
        "The nasal cavity and pharynx": "The nasal cavity and pharynx, where inhaled air is filtered, warmed, and humidified before reaching the lower airways",
        "The trachea and primary bronchi": "The trachea and primary bronchi, where cartilaginous support prevents airway collapse during forceful inspiration",
        "The pleural membranes": "The pleural membranes, whose serous fluid reduces friction and maintains negative intrapleural pressure for lung expansion",
    },
    # Lesson7.2
    ("Unit7/Lesson7.2_Quiz.json", 6): {
        "Directly proportional": "Directly proportional -- as volume increases, pressure also increases",
        "Always equal": "Always equal -- volume and pressure remain identical at all times",
        "Unrelated to each other": "Unrelated to each other -- volume changes have no effect on pressure",
    },
    # Lesson7.3
    ("Unit7/Lesson7.3_Quiz.json", 4): {
        "10 m\u00b2": "10 m\u00b2 (about the size of a small office desk)",
        "1 m\u00b2": "1 m\u00b2 (about the size of a single floor tile)",
        "200 m\u00b2": "200 m\u00b2 (about the size of a large apartment)",
    },
    ("Unit7/Lesson7.3_Quiz.json", 5): {
        "5 mm": "5 mm (five millimeters thick)",
        "1 mm": "1 mm (one millimeter thick)",
        "10 \u00b5m": "10 \u00b5m (ten micrometers)",
    },
    ("Unit7/Lesson7.3_Quiz.json", 16): {
        "Low CO\u2082 in the blood": "Low CO\u2082 in the blood (PaCO\u2082 below 35 mmHg), indicating hyperventilation",
        "Low O\u2082 in the blood": "Low O\u2082 in the blood (PaO\u2082 below 60 mmHg), indicating significant hypoxemia",
        "Elevated O\u2082 in the blood": "Elevated O\u2082 in the blood (PaO\u2082 above 100 mmHg on room air), indicating hyperoxia",
    },
    ("Unit7/Lesson7.3_Quiz.json", 21): {
        "The fluid blocks blood flow through the pulmonary arteries": "The fluid blocks blood flow through the pulmonary arteries by compressing vessels externally and increasing pulmonary vascular resistance, preventing adequate perfusion of ventilated areas",
        "The fluid paralyzes the diaphragm": "The fluid paralyzes the diaphragm by compressing the phrenic nerve roots within the mediastinum, preventing diaphragmatic contraction and reducing tidal volume and minute ventilation",
        "The fluid destroys surfactant, collapsing all alveoli": "The fluid destroys surfactant molecules through enzymatic degradation, causing all alveoli to collapse from increased surface tension and rendering the lungs unable to expand during inspiration",
    },
    ("Unit7/Lesson7.3_Quiz.json", 29): {
        "Exercise increases dead space ventilation in the upper airways": "Exercise increases dead space ventilation in the upper airways by dilating the trachea and bronchi, so a greater proportion of each breath occupies the conducting zone without reaching the alveoli",
        "Exercise causes her airways to constrict from bronchospasm": "Exercise causes her airways to constrict from bronchospasm as the increased airflow irritates and dries the bronchial mucosa, triggering smooth muscle contraction that narrows the lower airways",
        "Exercise reduces surfactant production, causing alveolar collapse": "Exercise reduces surfactant production by diverting blood flow away from type II pneumocytes, causing progressive alveolar collapse and atelectasis that reduces the available gas exchange surface area",
    },
    # Lesson7.4
    ("Unit7/Lesson7.4_Quiz.json", 7): {
        "Methemoglobin": "Methemoglobin (oxidized iron in the ferric Fe3+ state)",
        "Carboxyhemoglobin": "Carboxyhemoglobin (CO bound to the heme iron group)",
        "Oxyhemoglobin": "Oxyhemoglobin (O\u2082 bound to the heme iron group)",
    },
    ("Unit7/Lesson7.4_Quiz.json", 21): {
        "Carbon monoxide increases true oxygen saturation": "Carbon monoxide increases true oxygen saturation by enhancing the hemoglobin molecule's affinity for oxygen molecules at the tissue level",
        "The pulse oximeter malfunctions in hot environments": "The pulse oximeter sensor malfunctions in hot environments because elevated skin temperature disrupts the infrared light absorption readings",
        "The cherry-red color indicates adequate oxygenation": "The cherry-red skin color indicates adequate oxygenation because it reflects a high concentration of oxyhemoglobin in the peripheral capillary beds",
    },
    ("Unit7/Lesson7.4_Quiz.json", 23): {
        "Carbon monoxide from her kidney disease is blocking hemoglobin": "Carbon monoxide produced as a byproduct of her kidney disease is accumulating in the blood and blocking hemoglobin from binding oxygen molecules at the alveolar level",
        "Her blood pH is too high for hemoglobin to bind oxygen": "Her blood pH is too alkalotic for hemoglobin to bind oxygen effectively, causing a severe left shift of the oxygen-hemoglobin dissociation curve",
        "Her lungs are not functioning properly": "Her lungs are not functioning properly because the chronic kidney disease has caused pulmonary fibrosis and thickening of the respiratory membrane",
    },
    ("Unit7/Lesson7.4_Quiz.json", 25): {
        "The lungs stop functioning below this oxygen level": "The lungs stop functioning below this oxygen level because the alveolar epithelial cells cannot survive when the partial pressure drops below 60 mmHg",
        "Below 60 mmHg, hemoglobin is destroyed by low oxygen levels": "Below 60 mmHg, hemoglobin molecules are destroyed by the low oxygen environment, causing irreversible denaturation of the globin protein chains",
        "Below 60 mmHg, CO\u2082 displaces all O\u2082 from hemoglobin": "Below 60 mmHg, CO\u2082 molecules competitively displace all O\u2082 from hemoglobin binding sites because CO\u2082 has a higher affinity for the heme group at low pressures",
    },
    ("Unit7/Lesson7.4_Quiz.json", 27): {
        "90-95%": "90-95% oxygen saturation on pulse oximetry",
        "95-100%": "95-100% oxygen saturation on pulse oximetry",
        "Any value below 99%": "Any value below 99% oxygen saturation on pulse oximetry",
    },
    ("Unit7/Lesson7.4_Quiz.json", 29): {
        "The pulse oximeter malfunctions in acidotic patients": "The pulse oximeter malfunctions in acidotic patients because the low pH alters the optical properties of hemoglobin and produces inaccurate infrared readings",
        "Acidosis causes the lungs to stop working": "Acidosis causes the lungs to stop working because the low pH paralyzes the smooth muscle in the bronchial walls and prevents normal ventilation",
        "Acidosis destroys hemoglobin molecules in the blood": "Acidosis destroys hemoglobin molecules in the blood through acid-mediated denaturation of the globin protein, reducing total oxygen-carrying capacity",
    },
    # Lesson7.5
    ("Unit7/Lesson7.5_Quiz.json", 2): {
        "Low CO\u2082 levels": "Low CO\u2082 levels (detected by peripheral chemoreceptors in the carotid bodies)",
        "Low O\u2082 levels in the blood": "Low O\u2082 levels in the blood (detected by peripheral chemoreceptors in the carotid bodies)",
        "High O\u2082 levels": "High O\u2082 levels (detected by central chemoreceptors in the medulla oblongata)",
    },
    ("Unit7/Lesson7.5_Quiz.json", 5): {
        "Normal O\u2082 levels": "Normal O\u2082 levels with PaO\u2082 between 80 and 100 mmHg in arterial blood",
        "Low CO\u2082 levels": "Low CO\u2082 levels with PaCO\u2082 below 35 mmHg indicating hyperventilation",
        "High O\u2082 levels": "High O\u2082 levels with PaO\u2082 above 100 mmHg from supplemental oxygen",
    },
    ("Unit7/Lesson7.5_Quiz.json", 6): {
        "Blood pressure changes during breathing": "Blood pressure changes during the respiratory cycle affecting venous return and cardiac output",
        "Coughing during sleep": "Coughing during sleep triggered by postnasal drip irritating the pharyngeal mucosa",
        "Exhalation during exercise": "Exhalation during exercise driven by active contraction of the internal intercostals and abdominals",
    },
    ("Unit7/Lesson7.5_Quiz.json", 10): {
        "They breathe only voluntarily": "They breathe only through voluntary cortical control from the cerebral cortex, bypassing all medullary reflexes",
        "The medulla has been destroyed by the disease": "The medullary respiratory centers have been physically destroyed by the chronic obstructive disease process itself",
        "They have no chemoreceptors": "They have no functional chemoreceptors because chronic lung disease has destroyed both the central and peripheral chemoreceptor cells",
    },
    ("Unit7/Lesson7.5_Quiz.json", 12): {
        "Normal pauses in breathing that occur in all sleeping individuals": "Normal pauses in breathing that occur in all sleeping individuals as part of the physiological transition between sleep stages",
        "Insomnia caused by respiratory infections": "Insomnia caused by upper respiratory infections that produce nasal congestion, coughing, and difficulty falling asleep",
        "Snoring without any breathing interruption": "Snoring without any actual breathing interruption, caused by vibration of the soft palate during normal airflow",
    },
    ("Unit7/Lesson7.5_Quiz.json", 13): {
        "Rapid shallow breathing seen in anxiety attacks": "Rapid shallow breathing seen in anxiety attacks, driven by excessive sympathetic activation that increases respiratory rate while decreasing tidal volume",
        "Deep, labored breathing associated with metabolic acidosis": "Deep, labored breathing associated with metabolic acidosis, driven by peripheral chemoreceptor stimulation of the respiratory center to blow off excess CO\u2082",
        "Normal, even breathing during sleep": "Normal, even breathing during sleep with consistent tidal volumes and regular intervals between breaths throughout all sleep stages",
    },
    ("Unit7/Lesson7.5_Quiz.json", 16): {
        "The normal primary stimulus for breathing driven by CO\u2082 levels": "The normal primary stimulus for breathing in which elevated arterial CO\u2082 is detected by central chemoreceptors in the medulla and drives increased ventilation",
        "The drive to breathe faster during exercise": "The drive to breathe faster during exercise, mediated by proprioceptors in muscles and joints that signal the respiratory center to increase ventilation",
        "The reflex that prevents lung overinflation": "The reflex that prevents lung overinflation by activating stretch receptors in the bronchial smooth muscle when the lungs expand beyond their normal volume",
    },
    ("Unit7/Lesson7.5_Quiz.json", 18): {
        "Deep, labored breathing": "Deep, labored breathing with increased tidal volume (hyperpnea) often seen in metabolic acidosis",
        "Abnormally slow breathing rate": "Abnormally slow breathing rate (below 12 breaths per minute) often seen with CNS depression",
        "Cessation of breathing": "Cessation of breathing (apnea) for periods exceeding twenty seconds or causing desaturation",
    },
    ("Unit7/Lesson7.5_Quiz.json", 22): {
        "She has developed a severe lung infection": "She has developed a severe lung infection from inhaling airborne pathogens during her rapid breathing, causing acute bronchitis and inflammatory airway narrowing",
        "She is not getting enough oxygen to her brain": "She is not getting enough oxygen to her brain because hyperventilation paradoxically reduces oxygen delivery by causing constriction of the cerebral vasculature",
        "Her heart is failing and cannot pump blood to her extremities": "Her heart is failing and cannot pump blood to her extremities because the rapid breathing has increased intrathoracic pressure, compressing the heart and reducing venous return",
    },
    ("Unit7/Lesson7.5_Quiz.json", 23): {
        "The opioids caused his airways to constrict": "The opioids caused his airways to constrict by triggering histamine-mediated bronchospasm in the lower respiratory tract, severely narrowing the bronchioles",
        "The opioids destroyed his peripheral chemoreceptors": "The opioids destroyed his peripheral chemoreceptors in the carotid and aortic bodies through direct cytotoxic damage, eliminating hypoxic drive",
        "The opioids caused pulmonary edema blocking gas exchange": "The opioids caused pulmonary edema by increasing pulmonary capillary permeability, flooding the alveoli with protein-rich fluid that blocked gas exchange",
    },
    ("Unit7/Lesson7.5_Quiz.json", 25): {
        "The patient voluntarily alternates between fast and slow breathing": "The patient voluntarily alternates between fast and slow breathing in a conscious effort to manage dyspnea, producing the characteristic crescendo-decrescendo pattern observed at the bedside",
        "The heart failure has destroyed the medullary respiratory center": "The heart failure has destroyed the medullary respiratory center through chronic hypoxic damage to brainstem neurons, eliminating all automatic respiratory drive",
        "Fluid in the lungs mechanically blocks the breathing muscles": "Fluid in the lungs mechanically blocks the diaphragm and intercostal muscles from generating adequate force for ventilation, producing periodic cessation of breathing",
    },
    ("Unit7/Lesson7.5_Quiz.json", 30): {
        "Pathological apnea only occurs in premature infants, never in full-term babies": "Pathological apnea only occurs in premature infants born before 37 weeks gestation, never in full-term babies, because full-term brainstem respiratory centers are always fully mature at birth",
        "Any pause in breathing during infancy is pathological and requires treatment": "Any pause in breathing during infancy, regardless of duration or associated findings, is pathological and requires immediate medical treatment including intubation and mechanical ventilation",
        "Normal periodic breathing always includes Cheyne-Stokes pattern": "Normal periodic breathing in infants always includes a Cheyne-Stokes pattern of crescendo-decrescendo tidal volumes, and this is considered a benign developmental finding",
    },
    # Lesson7.6
    ("Unit7/Lesson7.6_Quiz.json", 3): {
        "Reversible bronchospasm": "Reversible bronchospasm causing temporary airway narrowing that responds to bronchodilator therapy",
        "Excess mucus production in the bronchi": "Excess mucus production in the bronchi causing chronic productive cough and recurrent airway obstruction",
        "Fluid accumulation in the alveoli": "Fluid accumulation in the alveoli due to increased capillary permeability impairing gas exchange",
    },
    ("Unit7/Lesson7.6_Quiz.json", 6): {
        "A parasite": "A parasitic organism that invades pulmonary tissue through the bloodstream",
        "A fungus": "A fungal organism that colonizes the respiratory tract in immunocompromised hosts",
        "A virus": "A viral pathogen that infects the respiratory epithelium and spreads by aerosol droplets",
    },
    ("Unit7/Lesson7.6_Quiz.json", 11): {
        "A genetic disease causing thick mucus production": "A genetic disease causing abnormally thick mucus production due to a defective chloride channel, leading to chronic lung infections and pancreatic insufficiency",
        "A reversible airway disease characterized by acute bronchospasm": "A reversible airway disease characterized by acute bronchospasm, airway inflammation, and mucus hypersecretion, triggered by allergens, exercise, or irritants",
        "An acute lung infection caused by bacteria": "An acute lung infection caused by bacteria that invade the alveolar spaces, producing consolidation and inflammatory exudate visible on chest radiography",
    },
    ("Unit7/Lesson7.6_Quiz.json", 12): {
        "A bacterial pneumonia limited to one lobe": "A bacterial pneumonia limited to one lobe of the lung, characterized by consolidation and air bronchograms visible on chest imaging with a productive cough",
        "A mild allergic reaction in the airways": "A mild allergic reaction in the airways triggered by inhaled allergens, causing transient bronchospasm and mucus production that resolves with antihistamines",
        "A chronic obstructive lung disease caused by smoking": "A chronic obstructive lung disease caused by smoking, characterized by irreversible airflow limitation from chronic bronchitis and emphysema developing over decades",
    },
    ("Unit7/Lesson7.6_Quiz.json", 18): {
        "Increased air in the lungs appearing hyper-dark": "Increased air in the lungs appearing hyper-dark on X-ray, indicating hyperinflation from air trapping typical of obstructive lung diseases like COPD or severe asthma",
        "Normal air-filled lung appearing dark on X-ray": "Normal air-filled lung appearing dark on X-ray, representing healthy lung parenchyma with no pathological findings and adequate aeration throughout all lobes",
        "A collapsed lung with no air present": "A collapsed lung with no air present, appearing as a dense white opacity on X-ray due to complete atelectasis from bronchial obstruction or pleural effusion",
    },
    ("Unit7/Lesson7.6_Quiz.json", 21): {
        "Acute bacterial infection of the lung parenchyma": "Acute bacterial infection of the lung parenchyma causing alveolar consolidation with inflammatory exudate, producing fever, productive cough, and lobar opacities on imaging",
        "Reversible bronchospasm and temporary mucus production": "Reversible bronchospasm and temporary mucus hypersecretion triggered by allergens or irritants, causing episodic wheezing and dyspnea that responds to bronchodilators",
        "Scarring and thickening of the lung interstitium reducing compliance": "Scarring and thickening of the lung interstitium from chronic inflammatory processes, reducing lung compliance and restricting expansion with progressively worsening dyspnea",
    },
    ("Unit7/Lesson7.6_Quiz.json", 22): {
        "The alveolar damage from asthma was surgically repaired": "The alveolar damage from her asthma attack was surgically repaired through a minimally invasive bronchoscopic procedure that restored the damaged respiratory epithelium",
        "The medications cured her asthma permanently": "The medications administered during the hospitalization permanently cured her asthma by eliminating the underlying airway hypersensitivity and chronic inflammation",
        "The peak flow meter was malfunctioning initially": "The peak flow meter was malfunctioning when the initial low reading was obtained, and the improvement simply reflects accurate measurement with a properly calibrated device",
    },
    ("Unit7/Lesson7.6_Quiz.json", 23): {
        "The clot releases toxins that paralyze the diaphragm": "The clot releases vasoactive toxins that paralyze the diaphragm by inhibiting phrenic nerve transmission, preventing the patient from generating adequate negative intrathoracic pressure",
        "The clot blocks all airflow to the right lung": "The clot physically blocks all airflow to the right lung by lodging in the right main bronchus, completely preventing ventilation of the entire right lung field",
        "The clot causes the alveoli to fill with pus": "The clot causes the alveoli to fill with purulent exudate by triggering an acute bacterial infection in the affected lung segment, producing lobar consolidation",
    },
    ("Unit7/Lesson7.6_Quiz.json", 24): {
        "CF destroys the alveoli, eliminating the gas exchange surface": "CF destroys the alveoli by direct enzymatic degradation of the alveolar walls, eliminating the gas exchange surface area and causing irreversible emphysematous changes",
        "CF causes the trachea to narrow permanently": "CF causes the trachea to narrow permanently through progressive cartilage degradation and fibrotic stricture formation, restricting airflow to both lungs",
        "CF patients lack an immune system": "CF patients lack a functional immune system because the defective CFTR channel impairs white blood cell development, leaving them completely unable to fight infections",
    },
    ("Unit7/Lesson7.6_Quiz.json", 25): {
        "Acute respiratory distress syndrome (ARDS)": "Acute respiratory distress syndrome caused by severe bilateral lung inflammation with non-cardiogenic pulmonary edema and refractory hypoxemia",
        "Obstructive lung disease (like COPD)": "Obstructive lung disease such as COPD, characterized by irreversible airflow limitation with reduced FEV1/FVC ratio from airway narrowing",
        "Reversible asthma triggered by occupational exposure": "Reversible occupational asthma triggered by workplace inhalation of chemical irritants, causing episodic bronchospasm that resolves away from exposure",
    },
    ("Unit7/Lesson7.6_Quiz.json", 26): {
        "ARDS is a mild condition that resolves without treatment": "ARDS is a mild, self-limiting condition that resolves without medical treatment because the lung inflammation subsides spontaneously once the triggering insult is removed",
        "ARDS affects only one lobe, while pneumonia is always bilateral": "ARDS affects only one lobe of the lung in a focal pattern, while pneumonia is always bilateral and diffuse, which is the key distinguishing feature between the two conditions",
        "ARDS is always caused by bacteria, while pneumonia is always viral": "ARDS is always caused by bacterial infection of the lung parenchyma, while pneumonia is always caused by viral pathogens, making the etiological distinction straightforward",
    },
    ("Unit7/Lesson7.6_Quiz.json", 27): {
        "Culture results are never useful in pneumonia management": "Culture results are never clinically useful in pneumonia management because all bacteria respond identically to broad-spectrum antibiotics regardless of species identification",
        "Cultures cannot identify the bacteria causing pneumonia": "Cultures cannot reliably identify the bacteria causing pneumonia because respiratory pathogens do not grow well on standard laboratory culture media and produce false negatives",
        "The physician randomly selected an antibiotic because all antibiotics work equally well": "The physician randomly selected an antibiotic because all antibiotics work equally well against all respiratory pathogens, making targeted therapy based on culture results unnecessary",
    },
    ("Unit7/Lesson7.6_Quiz.json", 28): {
        "Quitting only helps if the smoker has fewer than 10 pack-years": "Quitting only helps if the smoker has fewer than 10 pack-years of cumulative exposure, because beyond that threshold the damage is entirely irreversible",
        "It is indeed too late \u2014 the damage is entirely permanent": "It is indeed too late to benefit from quitting after 40 years because the cumulative damage to the airways and alveoli is entirely permanent and will continue to progress",
        "Only smokers under age 30 benefit from quitting": "Only smokers under age 30 benefit from quitting because the regenerative capacity of lung tissue declines sharply after the third decade and cannot repair itself",
    },
    # Lesson7.7
    ("Unit7/Lesson7.7_Quiz.json", 1): {
        "Surgical intervention": "Surgical intervention to remove inflamed bronchial tissue",
        "Oral antibiotics": "Oral broad-spectrum antibiotics targeting respiratory bacteria",
        "Only supplemental oxygen": "Only supplemental oxygen delivered via a high-flow nasal cannula",
    },
    ("Unit7/Lesson7.7_Quiz.json", 5): {
        "75-80%": "75-80% (using aggressive high-flow oxygen therapy)",
        "98-100%": "98-100% (matching healthy non-COPD patients)",
        "100% on high-flow oxygen": "100% on high-flow oxygen (maximum achievable saturation)",
    },
    ("Unit7/Lesson7.7_Quiz.json", 8): {
        "Adequate sleep": "Adequate sleep and proper nocturnal rest patterns in a controlled environment",
        "Routine physical exercise": "Routine physical exercise within prescribed intensity guidelines from a pulmonary rehab program",
        "Eating large meals": "Eating large meals that distend the abdomen and elevate the diaphragm position",
    },
    ("Unit7/Lesson7.7_Quiz.json", 13): {
        "A radiological imaging study of the chest": "A radiological imaging study of the chest using X-rays or CT to visualize lung parenchyma, airways, and pleural spaces",
        "A blood test to measure oxygen levels": "A blood test measuring arterial oxygen, carbon dioxide, pH, and bicarbonate to assess respiratory and metabolic acid-base status",
        "A pulmonary function test measuring airflow rates": "A pulmonary function test measuring airflow rates, lung volumes, and capacities to differentiate obstructive from restrictive disease",
    },
    ("Unit7/Lesson7.7_Quiz.json", 14): {
        "A gradual improvement in symptoms over time": "A gradual improvement in symptoms over time reflecting the natural healing process and positive response to ongoing maintenance therapy",
        "Complete cure of the disease": "Complete cure of the disease with full resolution of all symptoms and normalization of lung function tests to pre-disease baseline values",
        "The initial diagnosis of a new disease": "The initial diagnosis of a new disease based on the first presentation of symptoms, physical examination findings, and confirmatory diagnostic testing",
    },
    ("Unit7/Lesson7.7_Quiz.json", 15): {
        "A medication regimen consisting only of inhaled bronchodilators": "A medication regimen consisting only of inhaled bronchodilators prescribed at specific doses and frequencies to maintain airway patency without any additional rehabilitative components",
        "A surgical procedure to remove damaged lung tissue": "A surgical procedure to remove damaged or non-functional lung tissue through video-assisted thoracoscopic surgery to improve the ventilatory mechanics of the remaining healthy lung",
        "A diagnostic procedure to identify lung pathogens": "A diagnostic procedure to identify lung pathogens through bronchoalveolar lavage, culture, and sensitivity testing to guide appropriate antimicrobial therapy selection",
    },
    ("Unit7/Lesson7.7_Quiz.json", 16): {
        "A list of foods to avoid to prevent asthma attacks": "A list of foods and environmental triggers to avoid to prevent asthma attacks, including specific allergens, preservatives, and indoor pollutants identified through allergy testing",
        "A schedule for annual spirometry testing only": "A schedule for annual spirometry testing only, without any instructions for daily symptom monitoring, medication adjustment, or emergency response protocols",
        "A surgical plan for removing the patient's lung": "A surgical plan for removing the patient's affected lung through pneumonectomy, including preoperative assessment, the procedure itself, and postoperative rehabilitation milestones",
    },
    ("Unit7/Lesson7.7_Quiz.json", 18): {
        "Normal air movement in healthy lungs": "Normal air movement in healthy lungs producing vesicular breath sounds heard with a stethoscope during quiet breathing over peripheral lung fields",
        "Fluid in the pleural space": "Fluid in the pleural space producing diminished breath sounds and dullness to percussion, indicating a pleural effusion that compresses the underlying lung",
        "Air moving through consolidated lung tissue": "Air moving through consolidated lung tissue producing tubular bronchial breath sounds heard over areas of pneumonia where the alveoli are filled with exudate",
    },
    ("Unit7/Lesson7.7_Quiz.json", 19): {
        "A blood test measuring inflammatory markers from the bronchi": "A blood test measuring inflammatory markers released from the bronchial epithelium, including eosinophil counts, IgE levels, and C-reactive protein concentrations",
        "An X-ray of the chest focused on the bronchi": "An X-ray of the chest focused specifically on the bronchi using specialized radiographic techniques to visualize airway wall thickness and mucus plugging",
        "A spirometry test specifically measuring bronchial airflow": "A spirometry test specifically measuring bronchial airflow through the conducting airways to assess the degree of obstruction at each generation of branching",
    },
    ("Unit7/Lesson7.7_Quiz.json", 20): {
        "Using only chest X-rays to diagnose all respiratory conditions": "Using only chest X-rays to diagnose all respiratory conditions, as imaging alone provides sufficient information for treatment decisions without additional clinical data",
        "Prescribing antibiotics for every respiratory complaint": "Prescribing broad-spectrum antibiotics for every respiratory complaint regardless of whether the etiology is bacterial, viral, allergic, or environmental in nature",
        "Making treatment decisions based solely on one test result": "Making treatment decisions based solely on one diagnostic test result without integrating the clinical history, physical examination, or additional laboratory data",
    },
    ("Unit7/Lesson7.7_Quiz.json", 22): {
        "Metabolic in origin, not respiratory": "Metabolic in origin rather than respiratory, caused by renal bicarbonate loss with secondary hyperventilation as a compensatory mechanism",
        "Acute and uncompensated": "Acute and uncompensated, with the kidneys having had insufficient time to retain bicarbonate in response to the elevated carbon dioxide",
        "Fully compensated with a normal pH": "Fully compensated with a normal pH, indicating the kidneys have retained sufficient bicarbonate to completely normalize the blood pH despite the elevated CO\u2082",
    },
    ("Unit7/Lesson7.7_Quiz.json", 24): {
        "Rib fractures cause permanent COPD": "Rib fractures cause permanent COPD by triggering chronic inflammatory changes in the airways and irreversible alveolar wall destruction",
        "The broken ribs puncture the alveoli directly": "The broken ribs puncture the alveoli directly, causing diffuse alveolar hemorrhage and progressive loss of gas exchange surface area",
        "The fractures block blood flow to the left lung": "The fractures block blood flow to the left lung by compressing the pulmonary vasculature, creating a massive ventilation-perfusion mismatch",
    },
    ("Unit7/Lesson7.7_Quiz.json", 25): {
        "Exercise always causes pneumothorax in young men": "Exercise always causes pneumothorax in young men because the high intrathoracic pressures generated during physical activity routinely rupture the visceral pleura",
        "Their ribs are more likely to fracture and puncture the lung": "Their ribs are more likely to fracture and puncture the lung because tall, thin individuals have longer, thinner ribs with reduced cortical bone density",
        "Tall people have weaker immune systems that make their lungs more fragile": "Tall people have weaker immune systems that make their lungs more fragile and susceptible to spontaneous tissue breakdown, with the apical lung tissue being particularly vulnerable",
    },
    ("Unit7/Lesson7.7_Quiz.json", 26): {
        "Stroke patients cannot cough at all": "Stroke patients cannot cough at all because the stroke destroys the cough reflex center in the medulla, permanently eliminating the ability to clear the airways",
        "Stroke destroys the alveoli making them vulnerable to infection": "Stroke destroys the alveoli through neurogenic inflammation, making the damaged respiratory epithelium highly vulnerable to bacterial colonization and infection",
        "Stroke directly suppresses the immune system in the lungs": "Stroke directly suppresses the immune system in the lungs by reducing pulmonary macrophage activity and impairing the local inflammatory response to pathogens",
    },
    ("Unit7/Lesson7.7_Quiz.json", 27): {
        "The ventilator eliminates all surfactant from the lungs": "The ventilator eliminates all surfactant from the lungs through the high-pressure positive-pressure breaths, causing widespread alveolar collapse and atelectasis",
        "The ventilator delivers bacteria directly into the lungs": "The ventilator delivers bacteria directly into the lungs through the ventilator circuit tubing, which serves as a reservoir for bacterial growth and aerosolization",
        "Mechanical ventilation destroys the alveolar surface": "Mechanical ventilation destroys the alveolar surface through barotrauma and volutrauma from high-pressure breaths, directly rupturing the delicate alveolar walls",
    },
    ("Unit7/Lesson7.7_Quiz.json", 28): {
        "It indicates the cancer is benign and requires no treatment": "It indicates the cancer is benign and requires no treatment because lymph node involvement only occurs with non-malignant inflammatory conditions that resolve spontaneously",
        "Lymph node involvement has no impact on treatment decisions": "Lymph node involvement has no impact on treatment decisions because the staging of lung cancer depends entirely on the size of the primary tumor, not regional spread",
        "It means the cancer has already metastasized to the brain": "It means the cancer has already metastasized to the brain because mediastinal lymph node involvement always indicates simultaneous distant metastatic spread to the CNS",
    },
    ("Unit7/Lesson7.7_Quiz.json", 29): {
        "CPT strengthens the diaphragm to improve breathing mechanics": "CPT strengthens the diaphragm and intercostal muscles through the rhythmic percussion forces applied to the chest wall, improving overall respiratory muscle endurance",
        "CPT increases surfactant production to keep alveoli open": "CPT increases surfactant production by mechanically stimulating type II pneumocytes through the percussion and vibration forces applied to the chest wall",
        "CPT directly kills the bacteria in the mucus": "CPT directly kills the bacteria trapped in the mucus by generating mechanical shear forces that disrupt bacterial cell membranes and prevent biofilm formation",
    },
    ("Unit7/Lesson7.7_Quiz.json", 30): {
        "Presenting multiple findings only serves to impress the attending without clinical benefit": "Presenting multiple findings from different data sources only serves to impress the attending physician during rounds without providing any additional clinical benefit beyond what a single well-chosen test reveals",
        "The data sources are redundant and any single one would suffice": "The data sources are all redundant and any single one would suffice for making an accurate diagnosis and treatment plan for respiratory conditions",
        "Only one data source is ever needed for a respiratory diagnosis": "Only one data source is ever needed for a respiratory diagnosis, as clinical judgment based on the most relevant finding is always sufficient",
    },
    # Lesson7.8
    ("Unit7/Lesson7.8_Quiz.json", 3): {
        "40 mmHg": "40 mmHg (5% of 760 mmHg at sea level)",
        "760 mmHg": "760 mmHg (total atmospheric pressure at sea level)",
        "104 mmHg": "104 mmHg (14% of atmospheric pressure at sea level)",
    },
    ("Unit7/Lesson7.8_Quiz.json", 9): {
        "Respiratory alkalosis": "Respiratory alkalosis (low CO\u2082 with elevated pH indicating hyperventilation)",
        "Normal acid-base status": "Normal acid-base status (pH 7.35-7.45 with normal CO\u2082 and bicarbonate)",
        "Metabolic acidosis": "Metabolic acidosis (low bicarbonate with low pH from metabolic causes)",
    },
    ("Unit7/Lesson7.8_Quiz.json", 10): {
        "Metabolic alkalosis": "Metabolic alkalosis (elevated bicarbonate with high pH from metabolic causes)",
        "Respiratory acidosis": "Respiratory acidosis (elevated CO\u2082 with low pH indicating hypoventilation)",
        "Normal acid-base balance": "Normal acid-base balance (pH 7.35-7.45 with normal CO\u2082 and bicarbonate)",
    },
    ("Unit7/Lesson7.8_Quiz.json", 12): {
        "The reflex that prevents lung overinflation": "The reflex that prevents lung overinflation by activating pulmonary stretch receptors that send inhibitory signals through the vagus nerve to the medullary inspiratory center",
        "The effect of CO\u2082 and pH on hemoglobin's affinity for oxygen": "The effect of CO\u2082 concentration and blood pH on hemoglobin's affinity for oxygen, causing increased oxygen unloading at tissues with high metabolic activity",
        "The principle that gas solubility is proportional to partial pressure": "The principle that the amount of gas dissolved in a liquid is directly proportional to the partial pressure of that gas above the liquid at a given temperature",
    },
    ("Unit7/Lesson7.8_Quiz.json", 14): {
        "The process of completely curing an acid-base imbalance": "The process of completely curing an acid-base imbalance by restoring all blood gas values to their normal ranges through direct medical intervention such as intravenous bicarbonate",
        "Adding bicarbonate intravenously to correct acidosis": "Adding bicarbonate intravenously to correct acidosis by directly buffering excess hydrogen ions in the blood and raising the pH back to the normal physiological range",
        "Administering medications to normalize CO\u2082 levels": "Administering medications to normalize CO\u2082 levels by stimulating the respiratory center in the medulla to increase ventilation rate and depth until PaCO\u2082 returns to normal",
    },
    ("Unit7/Lesson7.8_Quiz.json", 18): {
        "The difference between inspired and expired CO\u2082 levels": "The difference between inspired and expired CO\u2082 levels, which reflects alveolar CO\u2082 production from cellular metabolism and the efficiency of CO\u2082 elimination during ventilation",
        "The total volume of gas exchanged per minute": "The total volume of gas exchanged per minute across the respiratory membrane, calculated by multiplying tidal volume by respiratory rate and subtracting dead space ventilation",
        "The pressure difference between the aorta and the pulmonary artery": "The pressure difference between the aorta and the pulmonary artery, which drives blood flow from the left ventricle through the systemic circuit and from the right ventricle through the pulmonary circuit",
    },
    ("Unit7/Lesson7.8_Quiz.json", 21): {
        "Respiratory alkalosis with metabolic compensation": "Respiratory alkalosis with metabolic compensation, where low CO\u2082 from hyperventilation has raised the pH and the kidneys have responded by excreting bicarbonate to lower pH toward normal",
        "Normal acid-base balance": "Normal acid-base balance, because the slightly abnormal values fall within acceptable laboratory variation and do not represent a clinically significant acid-base disturbance",
        "Metabolic acidosis with respiratory compensation": "Metabolic acidosis with respiratory compensation, where low bicarbonate from metabolic acid production has lowered the pH and the lungs have responded by increasing ventilation to reduce CO\u2082",
    },
    ("Unit7/Lesson7.8_Quiz.json", 23): {
        "Normal lung function": "Normal lung function with all spirometry values within the predicted range for the patient's age, height, and sex",
        "Combined obstructive and restrictive disease": "Combined obstructive and restrictive disease showing both reduced FEV\u2081/FVC ratio and reduced total lung capacity on pulmonary function testing",
        "Obstructive lung disease with reduced FEV\u2081/FVC ratio": "Obstructive lung disease with a reduced FEV\u2081/FVC ratio from airway narrowing, producing air trapping and increased residual volume",
    },
    ("Unit7/Lesson7.8_Quiz.json", 25): {
        "Increasing atmospheric pressure at altitude": "Increasing atmospheric pressure at altitude that pushes more oxygen into the blood through greater alveolar partial pressure gradients across the respiratory membrane",
        "Increased hemoglobin prevents CO\u2082 from entering the blood": "Increased hemoglobin prevents CO\u2082 from entering the blood because the additional hemoglobin molecules preferentially bind CO\u2082 and sequester it before it can dissolve in plasma",
        "Both changes reduce the body's need for oxygen": "Both changes reduce the body's total need for oxygen by lowering the basal metabolic rate at altitude, so less oxygen delivery is required to meet tissue demands",
    },
    ("Unit7/Lesson7.8_Quiz.json", 26): {
        "The infant's hemoglobin cannot bind oxygen": "The infant's hemoglobin cannot bind oxygen because premature infants produce a dysfunctional form of hemoglobin that lacks the ability to carry oxygen molecules to the tissues",
        "The infant's airways are too wide, allowing air to escape": "The infant's airways are too wide and compliant, allowing air to escape during exhalation before it reaches the alveoli, resulting in massive dead space ventilation",
        "The infant's respiratory center in the medulla has not yet formed": "The infant's respiratory center in the medulla has not yet formed because brainstem development occurs late in gestation and is incomplete in premature neonates",
    },
    ("Unit7/Lesson7.8_Quiz.json", 27): {
        "Respiratory acidosis with metabolic compensation": "Respiratory acidosis with partial metabolic compensation, where elevated CO\u2082 from hypoventilation has lowered pH and the kidneys have retained bicarbonate to bring pH back toward normal",
        "Metabolic alkalosis with respiratory compensation": "Metabolic alkalosis with respiratory compensation, where elevated bicarbonate from metabolic causes has raised pH and the lungs have reduced ventilation to retain CO\u2082",
        "Combined metabolic and respiratory acidosis": "Combined metabolic and respiratory acidosis, where both low bicarbonate and elevated CO\u2082 contribute to a severely depressed pH from simultaneous renal and pulmonary failure",
    },
    ("Unit7/Lesson7.8_Quiz.json", 29): {
        "The fractures have caused the diaphragm to rupture": "The fractures have caused the diaphragm to rupture, allowing abdominal contents to herniate into the thoracic cavity and compress the lungs, preventing adequate ventilation and gas exchange",
        "The patient's hemoglobin has been destroyed by the fat": "The patient's hemoglobin has been destroyed by the fat globules circulating in the bloodstream, which coat and denature the hemoglobin molecules, eliminating oxygen-carrying capacity",
        "The fat emboli are blocking all airways mechanically": "The fat emboli are blocking all airways mechanically by lodging in the bronchi and bronchioles, physically preventing airflow from reaching the alveoli and causing complete bilateral obstruction",
    },
    ("Unit7/Lesson7.8_Quiz.json", 30): {
        "The systems are independent \u2014 heart failure does not affect the lungs or kidneys": "The systems are independent and heart failure does not affect the lungs or kidneys because each organ system operates autonomously with its own self-contained regulatory mechanisms",
        "Only the respiratory system is involved in this scenario": "Only the respiratory system is involved in this scenario because the lungs are the sole organ responsible for maintaining acid-base balance and no other system participates",
        "The nervous system alone controls the response to heart failure": "The nervous system alone controls the entire response to heart failure through autonomic reflexes, and the respiratory and renal systems play no role in compensation",
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
files = sorted(glob.glob(os.path.join(base, 'Unit7', '*Quiz*.json')))
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
    print("Unit 7: ALL CLEAR!")
else:
    print(f"Unit 7: {still_flagged} still flagged")
