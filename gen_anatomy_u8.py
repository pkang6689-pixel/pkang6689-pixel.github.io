#!/usr/bin/env python3
"""Anatomy Unit 8 – Digestive System (7 lessons)."""
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

# 8.1
k,v = build_lesson(8,1,"Anatomy of Digestive Organs",
    "<h3>Anatomy of Digestive Organs</h3>"
    "<h4>GI Tract (Alimentary Canal)</h4>"
    "<ul><li><b>Mouth → pharynx → esophagus → stomach → small intestine (duodenum, jejunum, ileum) → large intestine (cecum, colon, rectum) → anus.</b></li></ul>"
    "<h4>GI Wall Layers</h4>"
    "<ul><li><b>Mucosa:</b> Innermost; epithelium, secretion/absorption. <b>Submucosa:</b> Connective tissue, blood vessels, nerves.</li>"
    "<li><b>Muscularis:</b> Smooth muscle (circular + longitudinal) for peristalsis. <b>Serosa:</b> Outermost covering (visceral peritoneum).</li></ul>"
    "<h4>Accessory Organs</h4>"
    "<p>Salivary glands, liver, gallbladder, pancreas — secrete into the GI tract via ducts.</p>",
    [("Alimentary Canal","The continuous tube from mouth to anus through which food passes."),
     ("Peristalsis","Wave-like smooth muscle contractions that propel food through the GI tract."),
     ("Mucosa","Innermost GI wall layer; responsible for secretion and absorption."),
     ("Small Intestine","Primary site of digestion and absorption; three parts: duodenum, jejunum, ileum."),
     ("Peritoneum","Serous membrane lining the abdominal cavity and covering most abdominal organs.")],
    [("The correct order of the GI tract is:",["Stomach → esophagus → mouth → intestine","*Mouth → pharynx → esophagus → stomach → small intestine → large intestine → anus","Esophagus → mouth → stomach → intestine","Stomach → mouth → intestine"],"Continuous tube, mouth to anus."),
     ("The three parts of the small intestine in order are:",["Ileum, jejunum, duodenum","*Duodenum, jejunum, ileum","Jejunum, duodenum, ileum","Cecum, colon, rectum"],"DJ-I."),
     ("The innermost layer of the GI wall is the:",["Serosa","Muscularis","*Mucosa","Submucosa"],"Mucosa faces the lumen."),
     ("Peristalsis is:",["Voluntary chewing","*Rhythmic, wave-like smooth muscle contractions that propel food along the GI tract","Only in the esophagus","A type of enzyme"],"Peristalsis moves food forward."),
     ("The muscularis layer contains:",["Skeletal muscle only","*Smooth muscle (inner circular and outer longitudinal layers)","Only connective tissue","Only epithelium"],"Two muscle layers for peristalsis."),
     ("The serosa is the:",["Innermost layer","*Outermost layer (visceral peritoneum) of most GI organs","Muscle layer","Nerve layer"],"Serosa = external covering."),
     ("Accessory digestive organs include:",["Only the stomach","*Salivary glands, liver, gallbladder, and pancreas","Only the intestines","The kidneys"],"Produce secretions that aid digestion."),
     ("The stomach has _____ unique muscle layers.",["2","*3 (oblique, circular, longitudinal — for churning)","4","1"],"Extra oblique layer enables churning."),
     ("The duodenum is where:",["*Most chemical digestion begins (receives bile and pancreatic juice)","No digestion occurs","Only absorption happens","Food is stored"],"Bile + pancreatic enzymes enter here."),
     ("The large intestine's primary function is:",["Protein digestion","*Water and electrolyte absorption and feces formation","Fat digestion","Nutrient absorption"],"Absorbs water, compacts waste."),
     ("The cecum connects to the:",["Stomach","*Ileum (small intestine meets large intestine); appendix is attached","Duodenum","Rectum"],"Ileocecal junction + appendix."),
     ("The mesentery:",["Is a muscle","*Is a double layer of peritoneum that suspends the intestines and carries blood vessels","Is a bone","Is an enzyme"],"Mesentery = vascular and structural support."),
     ("The greater omentum:",["Is inside the stomach","*Is a large fold of peritoneum draping over the intestines ('fatty apron')","Is part of the esophagus","Produces bile"],"Stores fat and has immune function."),
     ("The enteric nervous system:",["Is part of the brain","*Is the 'gut brain'; intrinsic nerve plexuses that control GI motility and secretion","Is voluntary","Only detects pain"],"Can function independently of the CNS."),
     ("The lower esophageal sphincter (LES):",["Is always open","*Prevents reflux of stomach acid into the esophagus","Is a bone","Produces acid"],"LES dysfunction → GERD."),
     ("Rugae are:",["Intestinal folds","*Folds in the stomach lining that allow expansion","Muscular structures","Enzyme-producing glands"],"Allow stomach to stretch when full."),
     ("Villi and microvilli in the small intestine:",["Reduce surface area","*Greatly increase surface area for absorption","Produce bile","Store feces"],"Enormous absorptive surface."),
     ("The ileocecal valve:",["Connects stomach to duodenum","*Regulates flow from small intestine to large intestine and prevents backflow","Connects colon to rectum","Is in the esophagus"],"One-way valve between SI and LI."),
     ("The rectum and anal canal:",["Are in the small intestine","*Store feces and control defecation (internal involuntary + external voluntary sphincters)","Produce enzymes","Absorb nutrients"],"Final segments of GI tract."),
     ("Understanding GI anatomy is essential for:",["Nothing","*Diagnosing GI diseases, planning surgeries, and understanding nutrition","Only gastroenterologists","Only anatomy exams"],"GI disorders are extremely common.")]
)
lessons[k]=v

# 8.2
k,v = build_lesson(8,2,"Mechanical & Chemical Digestion",
    "<h3>Mechanical &amp; Chemical Digestion</h3>"
    "<h4>Mechanical Digestion</h4>"
    "<p>Mastication (chewing), churning in the stomach, segmentation in the small intestine. Increases surface area for enzymes.</p>"
    "<h4>Chemical Digestion</h4>"
    "<ul><li><b>Carbohydrates:</b> Salivary amylase (mouth) → pancreatic amylase (SI) → maltase, sucrase, lactase (brush border) → monosaccharides.</li>"
    "<li><b>Proteins:</b> Pepsin (stomach, pH 2) → pancreatic trypsin, chymotrypsin (SI) → peptidases (brush border) → amino acids.</li>"
    "<li><b>Fats:</b> Bile salts emulsify → pancreatic lipase → monoglycerides + fatty acids.</li></ul>",
    [("Mechanical Digestion","Physical breakdown (chewing, churning, segmentation) increasing surface area for enzymes."),
     ("Chemical Digestion","Enzymatic breakdown of macromolecules into absorbable units (monosaccharides, amino acids, fatty acids)."),
     ("Salivary Amylase","Enzyme in saliva that begins starch digestion in the mouth."),
     ("Pepsin","Protein-digesting enzyme active in the stomach's acidic environment (pH ~2)."),
     ("Bile","Produced by liver, stored in gallbladder; emulsifies fats for lipase action.")],
    [("Mechanical digestion in the mouth is called:",["Peristalsis","*Mastication (chewing)","Absorption","Secretion"],"Teeth physically break food."),
     ("Chemical digestion of starch begins in the:",["Stomach","*Mouth (salivary amylase)","Small intestine","Large intestine"],"Salivary amylase starts carbohydrate digestion."),
     ("The stomach's chief cells produce:",["HCl","*Pepsinogen (inactive form of pepsin)","Bile","Amylase"],"Pepsinogen → pepsin in acidic pH."),
     ("Parietal cells in the stomach produce:",["Pepsinogen","*HCl (hydrochloric acid) and intrinsic factor","Bile","Mucus"],"HCl activates pepsinogen and kills bacteria."),
     ("The acidic pH of the stomach (~1.5–3.5) is important for:",["Nothing","*Activating pepsin, killing microbes, and denaturing proteins","Absorbing fat","Producing bile"],"Optimizes protein digestion."),
     ("Bile is produced by the _____ and stored in the _____.",["Gallbladder; liver","*Liver; gallbladder","Pancreas; stomach","Stomach; liver"],"Liver makes bile; gallbladder stores/concentrates it."),
     ("Bile emulsifies fats by:",["Digesting them","*Breaking large fat globules into small droplets (increases surface area for lipase)","Absorbing them","Converting them to sugars"],"Emulsification ≠ digestion; it aids lipase."),
     ("Pancreatic lipase digests fats into:",["Glucose","*Monoglycerides and fatty acids","Amino acids","Nucleotides"],"Lipase hydrolysis."),
     ("Pancreatic amylase continues _____ digestion.",["Protein","*Starch/carbohydrate","Fat","Nucleic acid"],"Completes starch → maltose."),
     ("Trypsin and chymotrypsin are:",["Carbohydrate enzymes","*Pancreatic protein-digesting enzymes (proteases)","Fat enzymes","Produced in the stomach"],"Active in the duodenum."),
     ("Brush border enzymes (maltase, sucrase, lactase) are located in the:",["Stomach","*Small intestine (on the microvilli of enterocytes)","Mouth","Large intestine"],"Final breakdown of disaccharides."),
     ("Lactose intolerance results from:",["Excess lactase","*Deficiency of the enzyme lactase (can't digest dairy sugar)","Too much bile","Excess stomach acid"],"Undigested lactose → gas, bloating, diarrhea."),
     ("Segmentation in the small intestine:",["Propels food forward only","*Mixes chyme with digestive juices (back-and-forth contractions)","Stops digestion","Only occurs in the stomach"],"Mixing contractions, not propulsive."),
     ("Chyme is:",["Solid food","*Semi-liquid mixture of food and gastric juices in the stomach","A type of enzyme","Bile"],"Stomach output."),
     ("The pyloric sphincter controls flow from the:",["Esophagus to stomach","*Stomach to duodenum","Small to large intestine","Mouth to esophagus"],"Regulates gastric emptying."),
     ("Cholecystokinin (CCK) is released in response to:",["Starch","*Fat and protein in the duodenum → stimulates gallbladder contraction and pancreatic enzyme secretion","Low blood sugar","Acid in the mouth"],"CCK = fat/protein signal."),
     ("Secretin is released in response to:",["Fat","*Acid in the duodenum → stimulates pancreatic bicarbonate secretion","Protein","Carbohydrate"],"Neutralizes acidic chyme."),
     ("Gastrin is released by the stomach to:",["Stop acid production","*Stimulate HCl secretion and gastric motility","Produce bile","Digest fat"],"Positive feedback for acid secretion during a meal."),
     ("Nucleases digest:",["Fat","Protein","*Nucleic acids (DNA and RNA) → nucleotides","Carbohydrates"],"Pancreatic nucleases."),
     ("Digestion is complete by the time chyme reaches the:",["Stomach","*End of the small intestine (ileum)","Large intestine","Mouth"],"SI completes all digestion.")]
)
lessons[k]=v

# 8.3
k,v = build_lesson(8,3,"Absorption of Nutrients",
    "<h3>Absorption of Nutrients</h3>"
    "<h4>Small Intestine = Primary Absorption Site</h4>"
    "<ul><li>Villi and microvilli provide ~200 m² surface area.</li>"
    "<li><b>Monosaccharides &amp; amino acids:</b> Absorbed into capillaries → portal vein → liver.</li>"
    "<li><b>Fatty acids &amp; monoglycerides:</b> Absorbed into enterocytes → re-esterified to triglycerides → packaged into chylomicrons → enter lacteals (lymphatic) → eventually blood.</li>"
    "<li><b>Vitamins:</b> Fat-soluble (A, D, E, K) absorbed with fats; water-soluble absorbed with water.</li></ul>"
    "<h4>Large Intestine</h4>"
    "<p>Absorbs remaining water and electrolytes; houses gut microbiome; forms and stores feces.</p>",
    [("Villi","Finger-like projections in the small intestine; each contains capillaries and a lacteal for absorption."),
     ("Microvilli (Brush Border)","Microscopic projections on enterocytes; vastly increase surface area for absorption."),
     ("Chylomicron","Lipoprotein particle that transports dietary fats from enterocytes into lymphatic lacteals."),
     ("Lacteal","Lymphatic capillary within each villus; absorbs dietary fats (chylomicrons)."),
     ("Hepatic Portal Vein","Carries nutrient-rich blood from the GI tract to the liver for processing.")],
    [("The primary site of nutrient absorption is the:",["Stomach","Mouth","*Small intestine","Large intestine"],"SI has vast surface area."),
     ("Villi and microvilli increase the small intestine's surface area to approximately:",["10 m²","50 m²","*~200 m²","1000 m²"],"Enormous absorptive surface."),
     ("Monosaccharides (glucose, fructose, galactose) are absorbed into:",["Lacteals","*Blood capillaries in the villi → hepatic portal vein → liver","Lymph","The stomach"],"Water-soluble nutrients enter blood."),
     ("Amino acids are absorbed into:",["Lacteals","*Blood capillaries → hepatic portal vein → liver","The lymphatic system","The stomach"],"Amino acids enter the portal circulation."),
     ("Dietary fats are absorbed into:",["Blood capillaries directly","*Enterocytes → packaged as chylomicrons → enter lacteals (lymphatic system)","The stomach","The large intestine"],"Fats take the lymphatic route."),
     ("Chylomicrons are:",["Enzymes","*Lipoprotein particles that carry dietary fats through the lymph","Hormones","Cells"],"Transport vehicle for dietary fat."),
     ("Lacteals are:",["Blood vessels","*Lymphatic capillaries within each villus (absorb fats)","Enzymes","Muscle fibers"],"Fat enters lymph before blood."),
     ("Fat-soluble vitamins (A, D, E, K) are absorbed:",["With water","*With dietary fats (require bile for absorption)","Only in the stomach","Through the skin"],"Impaired fat absorption → fat-soluble vitamin deficiency."),
     ("Vitamin B₁₂ absorption requires:",["Only water","*Intrinsic factor (produced by parietal cells) — absorbed in the ileum","Bile","Lipase"],"IF binds B₁₂ for ileal absorption."),
     ("The hepatic portal system carries absorbed nutrients to the:",["Heart directly","*Liver for processing, detoxification, and metabolism","Kidneys","Lungs"],"Liver is the first-pass organ."),
     ("The large intestine absorbs:",["Proteins","*Remaining water and electrolytes","Fats","Sugars"],"Concentrates feces."),
     ("The gut microbiome in the large intestine:",["Has no function","*Synthesizes vitamins (K, biotin), aids digestion, and supports immunity","Only causes disease","Digests protein"],"Trillions of beneficial bacteria."),
     ("Celiac disease impairs absorption because:",["Stomach acid is absent","*Gluten triggers immune-mediated destruction of small intestinal villi","The liver fails","Large intestine is damaged"],"No villi = malabsorption."),
     ("Iron is primarily absorbed in the:",["Stomach","*Duodenum and proximal jejunum","Ileum","Large intestine"],"Duodenum = primary iron absorption site."),
     ("Calcium absorption is enhanced by:",["Low vitamin D","*Vitamin D and PTH","High fiber","Excess iron"],"Vitamin D activates calcium transporters."),
     ("Malabsorption can cause:",["No problems","*Weight loss, nutrient deficiencies, diarrhea, and anemia","Only weight gain","Only constipation"],"Failure to absorb nutrients."),
     ("Enterocytes (intestinal absorptive cells) have a lifespan of:",["Years","*~3-5 days (rapid turnover)","1 month","1 hour"],"Among the fastest-dividing cells in the body."),
     ("Sodium absorption in the SI drives:",["Nothing","*Water absorption (water follows sodium osmotically)","Protein absorption","Fat absorption"],"Na⁺ gradient drives water movement."),
     ("Oral rehydration therapy (ORT) works because:",["It replaces all food","*Sodium + glucose co-transport drives water absorption — critical for treating dehydration","It's medicine","It kills bacteria"],"Saves millions of lives globally."),
     ("Understanding absorption is essential for:",["Nothing","*Managing malnutrition, celiac disease, Crohn's disease, short bowel syndrome, and more","Only dietitians","Only gastroenterologists"],"Absorption disorders are common and impactful.")]
)
lessons[k]=v

# 8.4
k,v = build_lesson(8,4,"Accessory Organs of Digestion",
    "<h3>Accessory Organs of Digestion</h3>"
    "<h4>Liver</h4>"
    "<p>Largest internal organ. Functions: bile production, detoxification, protein synthesis (albumin, clotting factors), glycogen storage, bilirubin metabolism.</p>"
    "<h4>Gallbladder</h4>"
    "<p>Stores and concentrates bile; releases it into the duodenum upon CCK stimulation.</p>"
    "<h4>Pancreas (Exocrine)</h4>"
    "<p>Produces pancreatic juice: bicarbonate (neutralizes acid), amylase, lipase, trypsinogen, chymotrypsinogen, nucleases.</p>"
    "<h4>Salivary Glands</h4>"
    "<p>Parotid, submandibular, sublingual — produce saliva (water, amylase, lysozyme, mucin).</p>",
    [("Liver","Largest internal organ; bile production, detoxification, protein synthesis, storage."),
     ("Gallbladder","Stores and concentrates bile; releases into duodenum when stimulated by CCK."),
     ("Pancreas (Exocrine)","Produces bicarbonate and digestive enzymes (amylase, lipase, proteases)."),
     ("Bilirubin","Breakdown product of hemoglobin; processed by the liver; excess → jaundice."),
     ("Salivary Glands","Produce saliva containing water, amylase (starch digestion), mucin, and lysozyme.")],
    [("The largest internal organ is the:",["Heart","Kidney","*Liver","Stomach"],"Liver ~1.5 kg."),
     ("The liver produces _____ that helps digest fats.",["Insulin","Amylase","*Bile","Pepsin"],"Bile emulsifies fats."),
     ("The liver detoxifies:",["Nothing","*Drugs, alcohol, metabolic waste, and toxins","Only alcohol","Only drugs"],"Hepatic biotransformation."),
     ("The liver synthesizes which plasma proteins?",["Hemoglobin","*Albumin, clotting factors (fibrinogen, prothrombin), and others","Only antibodies","Only enzymes"],"Essential protein factory."),
     ("Bilirubin is a breakdown product of:",["Protein","*Hemoglobin (from old RBCs)","Fat","Carbohydrate"],"Heme → biliverdin → bilirubin."),
     ("Jaundice (yellow skin/eyes) occurs when:",["Hemoglobin is high","*Bilirubin accumulates in the blood (liver disease, bile duct obstruction, or hemolysis)","Iron is low","Albumin is low"],"Excess bilirubin = yellow discoloration."),
     ("The gallbladder stores and concentrates:",["Insulin","Pancreatic juice","*Bile","Amylase"],"Concentrated bile released on demand."),
     ("Gallstones form when:",["Bile is dilute","*Cholesterol or bilirubin precipitates in the gallbladder","The liver fails","The pancreas is inflamed"],"Cholelithiasis."),
     ("CCK stimulates the gallbladder to:",["Stop contracting","*Contract and release bile into the duodenum","Produce enzymes","Absorb fat"],"Fat in duodenum triggers CCK."),
     ("The pancreas produces bicarbonate to:",["Acidify chyme","*Neutralize acidic chyme entering the duodenum","Digest protein","Digest fat"],"Bicarb raises pH for enzyme function."),
     ("Pancreatic lipase digests:",["Protein","Starch","*Fat → fatty acids + monoglycerides","Nucleic acids"],"Primary fat-digesting enzyme."),
     ("Trypsinogen is activated by:",["HCl","*Enterokinase (enteropeptidase) in the duodenum → trypsin","Pepsin","Bile"],"Enterokinase → trypsinogen → trypsin."),
     ("Pancreatitis is inflammation of the pancreas, often caused by:",["Exercise","*Gallstones or alcohol abuse","Stress","Dehydration"],"Two most common causes."),
     ("Hepatitis is:",["A heart disease","*Inflammation of the liver (viral: A, B, C; or alcoholic, autoimmune)","A kidney disease","A GI infection only"],"Multiple etiologies."),
     ("Cirrhosis is:",["Normal liver aging","*Chronic liver scarring (fibrosis) replacing functional tissue","A gallbladder disease","A stomach disease"],"End-stage liver disease from chronic injury."),
     ("The parotid gland is the:",["Smallest salivary gland","*Largest salivary gland (produces serous, enzyme-rich saliva)","A liver lobe","A pancreatic duct"],"Parotid = main salivary amylase source."),
     ("Saliva contains lysozyme, which:",["Digests starch","*Is an antibacterial enzyme","Digests fat","Digests protein"],"First-line defense against oral bacteria."),
     ("The common bile duct:",["Only carries pancreatic juice","*Carries bile from the liver/gallbladder to the duodenum (joins pancreatic duct at ampulla of Vater)","Is in the stomach","Carries blood"],"Bile + pancreatic juice enter duodenum together."),
     ("Liver failure is life-threatening because:",["The heart stops","*Without the liver's detox, synthesis, and metabolic functions, multiple organs fail","Only bile production stops","Only digestion stops"],"Liver = essential for survival."),
     ("Understanding accessory organs is essential for:",["Nothing","*Diagnosing hepatitis, cirrhosis, pancreatitis, gallstones, and nutritional disorders","Only surgeons","Only gastroenterologists"],"Common clinical conditions.")]
)
lessons[k]=v

# 8.5
k,v = build_lesson(8,5,"Disorders of the Digestive System",
    "<h3>Disorders of the Digestive System</h3>"
    "<ul><li><b>GERD:</b> Gastroesophageal reflux — acid damages esophagus. Treatment: PPIs, lifestyle changes.</li>"
    "<li><b>Peptic ulcer:</b> Mucosal erosion in stomach/duodenum; often H. pylori or NSAID-related.</li>"
    "<li><b>IBD:</b> Crohn's disease (any GI segment, transmural) vs. ulcerative colitis (colon only, mucosal).</li>"
    "<li><b>IBS:</b> Functional disorder — altered motility without structural cause.</li>"
    "<li><b>Colorectal cancer:</b> Third most common cancer; screening via colonoscopy.</li>"
    "<li><b>Celiac disease:</b> Autoimmune response to gluten → villous atrophy → malabsorption.</li></ul>",
    [("GERD","Gastroesophageal reflux disease; chronic acid reflux damaging the esophagus."),
     ("Peptic Ulcer","Erosion of the stomach or duodenal lining; H. pylori and NSAIDs are common causes."),
     ("Crohn's Disease","IBD that can affect any GI segment (mouth to anus); transmural inflammation."),
     ("Ulcerative Colitis","IBD limited to the colon; superficial (mucosal) inflammation with continuous lesions."),
     ("Celiac Disease","Autoimmune disorder triggered by gluten; destroys intestinal villi → malabsorption.")],
    [("GERD is caused by:",["Excess bile","*Chronic gastric acid reflux into the esophagus (LES dysfunction)","Too little acid","Food allergies"],"Acid damages esophageal mucosa."),
     ("The most common treatment for GERD includes:",["Antibiotics","*Proton pump inhibitors (PPIs) and lifestyle modifications","Surgery first","No treatment"],"PPIs reduce acid production."),
     ("Most peptic ulcers are caused by:",["Stress only","*H. pylori infection and/or NSAID use","Spicy food","Excess bile"],"H. pylori weakens mucosal defense."),
     ("H. pylori is treated with:",["Surgery","*Triple therapy: two antibiotics + a PPI","Only antacids","No treatment needed"],"Eradicate the bacteria + reduce acid."),
     ("Crohn's disease differs from ulcerative colitis in that it:",["Only affects the colon","*Can affect any GI segment and involves transmural (full-thickness) inflammation","Is not an IBD","Always resolves"],"Crohn's = discontinuous, transmural."),
     ("Ulcerative colitis is limited to the:",["Small intestine","*Colon (continuous mucosal inflammation)","Esophagus","Stomach"],"UC = colon only."),
     ("IBS (irritable bowel syndrome) is a _____ disorder.",["Structural","*Functional (altered motility/sensation without structural damage)","Cancerous","Infectious"],"No visible damage; symptom-based diagnosis."),
     ("Celiac disease is triggered by:",["Lactose","*Gluten (protein in wheat, barley, rye)","Fat","Sugar"],"Autoimmune response to gluten."),
     ("Treatment for celiac disease is:",["Medication","*Strict lifelong gluten-free diet","Surgery","No treatment needed"],"Avoiding gluten allows villi to recover."),
     ("Colorectal cancer screening is recommended starting at age:",["60","*45 (average risk)","30","70"],"Colonoscopy detects and removes precancerous polyps."),
     ("Barrett's esophagus is a complication of:",["Peptic ulcer","*Chronic GERD (metaplasia of esophageal epithelium)","Celiac disease","IBS"],"Squamous → columnar metaplasia; increases cancer risk."),
     ("Appendicitis presents with:",["Chest pain","*Right lower quadrant abdominal pain (McBurney's point), fever, nausea","Left arm pain","Back pain"],"Surgical emergency if ruptures."),
     ("Diverticulitis is:",["A cancer","*Inflammation/infection of diverticula (outpouchings) in the colon wall","A liver disease","An esophageal disease"],"Common in older adults; linked to low-fiber diet."),
     ("Hemorrhoids are:",["Tumors","*Swollen/inflamed veins in the rectal area","Ulcers","Polyps"],"Very common; associated with straining."),
     ("C. difficile (C. diff) infection often follows:",["Healthy eating","*Antibiotic use (disrupts gut flora → C. diff overgrowth → diarrhea)","Exercise","Stress"],"Antibiotic-associated diarrhea."),
     ("Liver cirrhosis can lead to:",["Improved digestion","*Portal hypertension, esophageal varices, ascites, and liver failure","Better absorption","No complications"],"Scarred liver → blood can't flow through."),
     ("Oral rehydration is critical in GI illnesses causing diarrhea because:",["It's not important","*Dehydration from fluid loss is the most dangerous consequence","It cures the infection","It stops diarrhea"],"Dehydration kills, especially in children."),
     ("Fiber is important for GI health because it:",["Is a nutrient","*Promotes regular bowel movements, supports gut microbiome, and may reduce colorectal cancer risk","Has no effect","Only adds bulk"],"Dietary fiber supports overall GI function."),
     ("Fecal occult blood test (FOBT) screens for:",["Liver disease","*Colorectal cancer and other GI bleeding sources","Ulcer disease only","Celiac disease"],"Detects hidden blood in stool."),
     ("Understanding GI disorders is essential because:",["They are rare","*They are among the most common reasons for medical visits and significantly impact quality of life","Only for specialists","Only for research"],"GI problems are extremely prevalent.")]
)
lessons[k]=v

# 8.6
k,v = build_lesson(8,6,"Case Studies in Nutrition & GI Health",
    "<h3>Case Studies in Nutrition &amp; GI Health</h3>"
    "<h4>Case 1: Iron-Deficiency Anemia</h4>"
    "<p>A 28-year-old vegetarian female with fatigue, pallor, low Hb, low ferritin, microcytic hypochromic RBCs. Diagnosis: iron-deficiency anemia. Treatment: iron supplementation + vitamin C to enhance absorption + dietary counseling.</p>"
    "<h4>Case 2: Acute Pancreatitis</h4>"
    "<p>A 50-year-old male with epigastric pain radiating to back after heavy alcohol use. Elevated lipase. Diagnosis: acute pancreatitis. Management: NPO (nothing by mouth), IV fluids, pain control, alcohol cessation.</p>"
    "<h4>Case 3: Celiac Disease</h4>"
    "<p>A child with failure to thrive, chronic diarrhea, and abdominal distension. Anti-tTG antibodies positive; duodenal biopsy shows villous atrophy. Treatment: strict gluten-free diet.</p>",
    [("Ferritin","Storage form of iron; low ferritin = iron stores depleted."),
     ("Microcytic Hypochromic","Small, pale RBCs characteristic of iron-deficiency anemia."),
     ("Lipase (serum)","Elevated serum lipase is the most specific marker for acute pancreatitis."),
     ("Anti-tTG Antibodies","Anti-tissue transglutaminase; serological marker for celiac disease."),
     ("Villous Atrophy","Flattening/loss of intestinal villi; seen in celiac disease on biopsy.")],
    [("Iron-deficiency anemia presents with:",["Only jaundice","*Fatigue, pallor, shortness of breath, and microcytic hypochromic RBCs","Only weight gain","No symptoms"],"Most common anemia worldwide."),
     ("Ferritin levels in iron-deficiency anemia are:",["High","*Low (depleted iron stores)","Normal","Variable"],"Low ferritin confirms iron depletion."),
     ("Vitamin C enhances iron absorption by:",["Blocking absorption","*Converting iron to its more absorbable ferrous (Fe²⁺) form","Producing acid","Diluting iron"],"Reducing Fe³⁺ → Fe²⁺."),
     ("In acute pancreatitis, the most specific lab marker is:",["Amylase","*Lipase (elevated 3× or more above normal)","WBC count","Bilirubin"],"Lipase is more specific than amylase."),
     ("NPO (nil per os) in pancreatitis aims to:",["Reduce weight","*Rest the pancreas by stopping oral intake (reduces enzyme secretion)","Cure the disease","Improve appetite"],"Pancreatic rest is essential."),
     ("The most common causes of acute pancreatitis are:",["Diet and exercise","*Gallstones and alcohol","Infection","Genetics"],"GET SMASHED mnemonic (Gallstones, Ethanol top the list)."),
     ("In the celiac case, anti-tTG antibodies are:",["Normal","*Positive (serological marker for celiac disease)","Negative","Irrelevant"],"First-line screening test."),
     ("Duodenal biopsy in celiac disease shows:",["Normal villi","*Villous atrophy (flattened villi) with intraepithelial lymphocytes","Excess mucus","Normal tissue"],"Gold standard for diagnosis."),
     ("Failure to thrive in a child may indicate:",["Normal growth","*Malabsorption (e.g., celiac disease) or inadequate nutrition","Excess eating","Only dehydration"],"Poor weight gain and growth."),
     ("Iron-rich foods include:",["Only supplements","*Red meat, spinach, lentils, fortified cereals","Only dairy","Only fruit"],"Dietary sources of iron."),
     ("Chronic alcohol use damages the pancreas by:",["Having no effect","*Promoting toxic metabolite accumulation and ductal obstruction","Diluting enzymes","Producing excess insulin"],"Alcohol-induced pancreatic injury."),
     ("Gluten-free alternatives include:",["Only lettuce","*Rice, corn, quinoa, potatoes, and gluten-free oats","Only bread","Nothing"],"Many naturally gluten-free grains exist."),
     ("Malabsorption from celiac disease can cause deficiency of:",["Only iron","*Iron, calcium, fat-soluble vitamins (A, D, E, K), folate, and more","Only vitamin C","Nothing"],"Damaged villi can't absorb properly."),
     ("B₁₂ deficiency can cause:",["No problems","*Megaloblastic anemia and neurological symptoms (neuropathy, cognitive changes)","Only fatigue","Only headache"],"B₁₂ is essential for nerve function and RBC production."),
     ("Lab values in nutritional assessment may include:",["Only weight","*CBC, ferritin, B₁₂, folate, vitamin D, albumin, prealbumin","Only BMI","Only cholesterol"],"Comprehensive labs guide nutritional management."),
     ("Parenteral nutrition (TPN) provides:",["Only water","*Complete nutrition (glucose, amino acids, lipids, vitamins) directly via IV (bypasses GI tract)","Only medications","Only electrolytes"],"For patients who can't eat or absorb."),
     ("Refeeding syndrome occurs when:",["A person eats too much","*A malnourished person is fed too rapidly → dangerous electrolyte shifts (low phosphate, K⁺, Mg²⁺)","A person fasts","Nothing eating-related"],"Life-threatening if not managed carefully."),
     ("Probiotics may help GI health by:",["Causing infection","*Supporting beneficial gut flora, improving GI symptoms in some conditions","Curing all diseases","Having no effect"],"Evidence supports some uses (e.g., antibiotic-associated diarrhea)."),
     ("The Mediterranean diet is associated with:",["No health benefits","*Reduced cardiovascular and GI disease risk","Only weight loss","Only mental health benefits"],"Rich in fruits, vegetables, whole grains, olive oil, fish."),
     ("These case studies demonstrate that:",["Nutrition doesn't matter","*Nutritional assessment, lab workup, and targeted treatment are essential for GI and nutritional disorders","Only medication helps","Symptoms are always obvious"],"Clinical integration is key.")]
)
lessons[k]=v

# 8.7
k,v = build_lesson(8,7,"AP Prep: Digestive Physiology",
    "<h3>AP Prep: Digestive Physiology</h3>"
    "<h4>Key Topics for Exam</h4>"
    "<ul><li>GI tract anatomy and wall layers.</li>"
    "<li>Enzymes: source, substrate, product for carbohydrates, proteins, fats.</li>"
    "<li>Absorption: mechanisms (active transport, facilitated diffusion, osmosis); site specificity.</li>"
    "<li>Hormonal regulation: gastrin, CCK, secretin, GIP.</li>"
    "<li>Liver functions and accessory organ roles.</li>"
    "<li>Common disorders: GERD, ulcers, IBD, celiac.</li></ul>",
    [("Gastrin","Stomach hormone; stimulates HCl secretion and gastric motility."),
     ("CCK (Cholecystokinin)","Released by duodenum in response to fat/protein; stimulates gallbladder contraction and pancreatic enzyme secretion."),
     ("Secretin","Released by duodenum in response to acid; stimulates pancreatic bicarbonate secretion."),
     ("GIP (Gastric Inhibitory Peptide)","Inhibits gastric secretion and motility; stimulates insulin release."),
     ("Enterokinase","Duodenal enzyme that activates trypsinogen → trypsin, initiating protein digestion cascade.")],
    [("Salivary amylase digests _____ to _____.",["Fat to fatty acids","*Starch to maltose","Protein to amino acids","Sucrose to glucose"],"Begins carb digestion in mouth."),
     ("Pepsin digests _____ in the _____.",["Fat in the duodenum","*Protein in the stomach","Starch in the mouth","Nucleic acids in the ileum"],"Pepsin + HCl in stomach."),
     ("Pancreatic juice enters the duodenum via the:",["Stomach","*Hepatopancreatic ampulla (ampulla of Vater)","Ileum","Jejunum"],"Common bile duct + pancreaticduct open here."),
     ("Which hormone stimulates HCl production?",["Secretin","CCK","*Gastrin","GIP"],"Gastrin from G cells."),
     ("CCK stimulates:",["Gastric acid secretion","*Gallbladder contraction + pancreatic enzyme release","Salivary secretion","Colonic motility"],"Response to fat and protein."),
     ("Secretin stimulates:",["Acid secretion","*Pancreatic bicarbonate secretion (neutralizes acid)","Bile production","Gastric motility"],"Response to acid in duodenum."),
     ("GIP inhibits:",["Insulin secretion","*Gastric acid secretion and motility; also stimulates insulin release","Bile secretion","Pancreatic function"],"Gastric Inhibitory Peptide."),
     ("Glucose is absorbed in the SI by:",["Simple diffusion","*Sodium-dependent co-transport (SGLT1) and facilitated diffusion (GLUT2)","Osmosis","Endocytosis"],"Active transport on apical, facilitated on basolateral."),
     ("Amino acids are absorbed by:",["Passive diffusion only","*Active transport and co-transport mechanisms","Osmosis","Through lacteals"],"Multiple amino acid transporters."),
     ("Fatty acids are absorbed into enterocytes by:",["Active transport","Endocytosis","*Simple diffusion (lipid-soluble) then repackaged into chylomicrons","Facilitated diffusion"],"Lipids cross membranes easily."),
     ("The liver converts excess glucose to _____ for storage.",["Fat only","*Glycogen (glycogenesis)","Protein","Amino acids"],"Glycogen = liver and muscle glucose reserve."),
     ("Gluconeogenesis in the liver is:",["Making glycogen","*Making new glucose from non-carbohydrate sources (amino acids, lactate, glycerol)","Glycogen breakdown","Fat synthesis"],"Maintains blood glucose during fasting."),
     ("The cephalic phase of digestion is triggered by:",["Food in the stomach","*Sight, smell, thought of food (vagus nerve stimulation)","Food in the intestines","Chyme in the colon"],"Brain anticipates food → prepares digestion."),
     ("The gastric phase of digestion occurs when:",["Food enters the mouth","*Food enters the stomach (stretch + chemical stimulation → gastrin release)","Food enters the intestines","Food is being chewed"],"Stomach distension triggers acid and enzyme release."),
     ("The intestinal phase of digestion:",["Increases gastric activity","*Mostly inhibits gastric activity (so the duodenum isn't overwhelmed)","Is involuntary only","Doesn't exist"],"Slow gastric emptying to match intestinal capacity."),
     ("Bilirubin in feces gives them their:",["Red color","*Brown color (bilirubin → stercobilin by gut bacteria)","Yellow color","Green color"],"Bacterial bile pigment metabolism."),
     ("Short bowel syndrome results in:",["Improved absorption","*Malabsorption due to insufficient intestinal length (e.g., after surgical resection)","Constipation","No symptoms"],"Less SI = less absorptive surface."),
     ("For the AP exam, you should be able to:",["Only list enzymes","*Trace food digestion from mouth to anus, identify enzymes/hormones/absorption sites, and apply concepts to clinical scenarios","Only name organs","Memorize pH values only"],"Application-level questions."),
     ("The vagus nerve's role in digestion includes:",["No role","*Stimulating gastric secretion, motility, and pancreatic output (parasympathetic)","Only inhibiting digestion","Only sensing pain"],"Parasympathetic = rest and digest."),
     ("Digestive physiology integrates with:",["No other systems","*Endocrine (hormones), nervous (vagal control), circulatory (nutrient transport), and immune systems","Only muscles","Only the brain"],"Whole-body integration.")]
)
lessons[k]=v

# ── Write ──
with open(PATH,"r",encoding="utf-8") as f:
    data = json.load(f)
data.update(lessons)
with open(PATH,"w",encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"✅ Anatomy Unit 8: wrote {len(lessons)} lessons")
