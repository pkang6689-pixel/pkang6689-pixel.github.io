import json, os, glob

base = 'content_data/AnatomyLessons'

replacements = {
    # UNIT 8
    ("Unit8/Lesson8.1_Quiz.json", 4): {
        "4": "4 (oblique, circular, longitudinal, and diagonal)",
        "2": "2 (circular and longitudinal layers only)",
        "1": "1 (a single circular smooth muscle layer)",
    },
    ("Unit8/Lesson8.1_Quiz.json", 6): {
        "Muscularis": "Muscularis (smooth muscle layers)",
        "Submucosa": "Submucosa (connective tissue layer)",
        "Mucosa": "Mucosa (innermost epithelial lining)",
    },
    ("Unit8/Lesson8.1_Quiz.json", 26): {
        "Diarrhea from excessive peristalsis": "Diarrhea from excessive peristalsis driven by overactive enteric nerve plexuses in the affected bowel segment",
        "Excessive bile secretion": "Excessive bile secretion from the liver flooding the intestinal lumen and causing malabsorption of dietary lipids",
        "Acid reflux into the esophagus": "Acid reflux into the esophagus due to failure of the lower esophageal sphincter to maintain adequate resting tone",
    },
    ("Unit8/Lesson8.2_Quiz.json", 3): {
        "Intrinsic factor": "Intrinsic factor (for vitamin B12 absorption)",
        "Bile": "Bile (for fat emulsification in the duodenum)",
        "Hydrochloric acid (HCl)": "Hydrochloric acid produced by parietal cells",
    },
    ("Unit8/Lesson8.2_Quiz.json", 10): {
        "Salivary glands": "Salivary glands on the surface of lingual epithelial cells",
        "Large intestine": "Large intestine on the mucosal surface of colonocytes",
        "Stomach lining": "Stomach lining on the apical surface of gastric cells",
    },
    ("Unit8/Lesson8.3_Quiz.json", 7): {
        "Ileum": "Ileum and terminal small intestine",
        "Distal jejunum only": "Distal jejunum and mid-small intestine only",
        "Cecum": "Cecum and proximal large intestine",
    },
    ("Unit8/Lesson8.3_Quiz.json", 8): {
        "Heart": "Heart for oxygenation and systemic distribution to tissues",
        "Kidneys for filtration": "Kidneys for filtration, reabsorption, and waste excretion",
        "Lungs for oxygenation": "Lungs for oxygenation of venous blood returning from tissues",
    },
    ("Unit8/Lesson8.4_Quiz.json", 15): {
        "An infection of the pancreatic duct by bacteria": "An infection of the pancreatic duct caused by bacteria that ascend from the duodenum, producing purulent inflammation and obstruction of exocrine secretions",
        "A hormonal disorder in which the pancreas produces too much insulin": "A hormonal disorder in which the pancreatic beta cells produce excessive insulin, causing chronic hypoglycemia, confusion, diaphoresis, and recurrent episodes of unconsciousness",
        "A congenital absence of the pancreas at birth": "A congenital absence of the pancreas at birth, resulting in complete lack of digestive enzyme and insulin production requiring lifelong enzyme replacement and insulin therapy",
    },
    ("Unit8/Lesson8.5_Quiz.json", 6): {
        "Small intestine": "Small intestine, with transmural inflammation affecting the ileum and jejunum",
        "Stomach and duodenum": "Stomach and duodenum, with erosion of the gastric and duodenal mucosal linings",
        "Esophagus": "Esophagus, with chronic acid-induced mucosal erosion and inflammatory changes",
    },
    ("Unit8/Lesson8.5_Quiz.json", 10): {
        "Immediate surgical fundoplication for all patients": "Immediate surgical fundoplication for all patients, wrapping the gastric fundus around the lower esophagus to create a mechanical anti-reflux barrier",
        "No treatment is available for GERD": "No treatment is available for GERD because the lower esophageal sphincter cannot be strengthened by any medical or surgical intervention",
        "Antibiotics to treat the underlying infection": "Antibiotics to treat the underlying bacterial infection of the esophageal mucosa that is responsible for the chronic acid reflux symptoms",
    },
    ("Unit8/Lesson8.5_Quiz.json", 11): {
        "A congenital narrowing of the esophagus present from birth": "A congenital narrowing of the esophagus present from birth, caused by incomplete canalization of the esophageal lumen during embryonic development",
        "Inflammation of the esophagus caused by food allergies": "Inflammation of the esophagus caused by food allergies, known as eosinophilic esophagitis, in which eosinophils infiltrate the esophageal mucosa",
        "An acute bacterial infection of the esophageal mucosa": "An acute bacterial infection of the esophageal mucosa, causing ulceration and purulent exudate that narrows the esophageal lumen and impairs swallowing",
    },
    ("Unit8/Lesson8.5_Quiz.json", 15): {
        "Another name for irritable bowel syndrome (IBS)": "Another name for irritable bowel syndrome, a functional GI disorder characterized by abdominal pain and altered bowel habits without any structural inflammation",
        "A single condition that only affects the stomach": "A single condition that only affects the stomach lining, causing chronic gastritis with mucosal atrophy and reduced acid production over time",
        "An acute food poisoning episode that resolves within days": "An acute food poisoning episode caused by bacterial contamination that resolves within days as the immune system clears the pathogen from the GI tract",
    },
    ("Unit8/Lesson8.5_Quiz.json", 19): {
        "A cancerous growth in the stomach or duodenal wall": "A cancerous growth in the stomach or duodenal wall that arises from malignant transformation of mucosal epithelial cells and invades through the layers of the GI wall",
        "A viral infection of the small intestine causing diarrhea": "A viral infection of the small intestine causing watery diarrhea, vomiting, and dehydration, most commonly caused by rotavirus or norovirus in the pediatric population",
        "Inflammation of the esophagus from chronic acid reflux": "Inflammation of the esophageal mucosa from chronic acid reflux, causing heartburn, dysphagia, and potentially leading to stricture formation and metaplastic changes",
    },
    ("Unit8/Lesson8.5_Quiz.json", 26): {
        "Ulcerative colitis flare triggered by the low-fiber diet": "Ulcerative colitis flare triggered by the low-fiber diet, with mucosal inflammation beginning at the rectum and extending proximally through the colon, causing bloody diarrhea",
        "Colorectal cancer caused by her low-fiber diet": "Colorectal cancer caused by her long-term low-fiber diet, with a malignant mass in the sigmoid colon obstructing the lumen and causing a change in bowel habits",
        "Acute appendicitis, since the sigmoid colon is near the appendix": "Acute appendicitis presenting with atypical left-sided pain, since the sigmoid colon is near the cecum and appendiceal inflammation can refer pain to either lower quadrant",
    },
    ("Unit8/Lesson8.6_Quiz.json", 4): {
        "White blood cell count": "White blood cell count (marker of systemic infection or inflammation)",
        "Serum amylase": "Serum amylase (also elevated in pancreatitis but less specific)",
        "Serum bilirubin": "Serum bilirubin (marker of hepatobiliary obstruction or hemolysis)",
    },
    ("Unit8/Lesson8.6_Quiz.json", 12): {
        "Weight gain that occurs after a period of dieting": "Weight gain that occurs after a period of caloric restriction and dieting, due to metabolic adaptation and increased fat storage efficiency when normal caloric intake resumes",
        "An allergic reaction to tube feeding formula": "An allergic reaction to tube feeding formula, characterized by urticaria, gastrointestinal distress, and potentially anaphylaxis from protein components in the enteral nutrition product",
        "Nausea and vomiting that occurs when eating after a short fast": "Nausea and vomiting that occurs when a person eats after a short fast of twelve to twenty-four hours, due to temporary gastric intolerance and reduced gastric motility from the fasting period",
    },
    ("Unit8/Lesson8.6_Quiz.json", 15): {
        "It indicates kidney function and fluid balance": "It indicates kidney function and fluid balance status by reflecting the glomerular filtration rate and the ability of the kidneys to concentrate or dilute urine",
        "It measures the amount of iron stored in the body": "It measures the amount of iron stored in the body as ferritin, indicating whether iron reserves are adequate for hemoglobin synthesis and red blood cell production",
        "It is a marker for liver disease severity": "It is a marker for liver disease severity that reflects hepatocellular damage, with elevated levels indicating ongoing destruction of liver parenchymal cells",
    },
    ("Unit8/Lesson8.6_Quiz.json", 18): {
        "A special oral diet consisting of pureed foods only": "A special oral diet consisting exclusively of pureed foods that have been mechanically processed to a smooth consistency to reduce the risk of aspiration in patients with dysphagia",
        "Nutrition delivered intravenously, bypassing the digestive system entirely": "Nutrition delivered intravenously through a central venous catheter, bypassing the digestive system entirely and providing all macronutrients, electrolytes, and vitamins directly into the bloodstream",
        "Nutrition absorbed through the skin via transdermal patches": "Nutrition absorbed through the skin via transdermal patches that deliver micronutrients and amino acids directly into the subcutaneous tissue and systemic circulation",
    },
    ("Unit8/Lesson8.6_Quiz.json", 20): {
        "Counting the number of calories a patient consumes daily": "Counting the number of calories a patient consumes daily through food diaries and meal tracking, without considering micronutrient status, body composition, or clinical markers",
        "Simply weighing a patient and calculating their BMI": "Simply weighing a patient and calculating their body mass index, which provides a single anthropometric measure without assessing dietary adequacy, micronutrient deficiencies, or protein status",
        "Ordering a single blood test to check cholesterol levels": "Ordering a single blood test to check cholesterol levels, which only reflects lipid metabolism and does not provide information about protein status, vitamin levels, or mineral balance",
    },
    ("Unit8/Lesson8.6_Quiz.json", 25): {
        "She has IBS, and TPN calms the overactive gut": "She has irritable bowel syndrome, and TPN calms the overactive gut by completely resting the GI tract and eliminating all enteral stimulation of peristalsis and secretion",
        "She has celiac disease, and TPN provides gluten-free nutrition": "She has celiac disease, and TPN provides gluten-free nutrition that bypasses the damaged small intestinal mucosa, avoiding the autoimmune response triggered by gluten exposure",
        "She has lactose intolerance, and TPN avoids dairy-based nutrients": "She has lactose intolerance, and TPN avoids dairy-based nutrients that would trigger osmotic diarrhea by delivering all macronutrients directly into the venous system",
    },
    ("Unit8/Lesson8.6_Quiz.json", 30): {
        "TPN is always preferable after surgery because the gut needs complete rest to heal": "TPN is always preferable after surgery because the gut needs complete rest to heal, and any enteral feeding would disrupt the surgical anastomosis and delay tissue repair",
        "There is no evidence-based difference between enteral and parenteral nutrition": "There is no evidence-based difference between enteral and parenteral nutrition in terms of clinical outcomes, infection rates, cost, or length of hospital stay",
        "Enteral nutrition is only preferred because it is cheaper than TPN": "Enteral nutrition is only preferred because it is cheaper than TPN, and there are no physiological advantages to using the gut for nutrition over intravenous delivery",
    },
    ("Unit8/Lesson8.7_Quiz.json", 9): {
        "Sodium-dependent co-transport similar to glucose": "Sodium-dependent co-transport similar to glucose absorption, using the electrochemical sodium gradient to drive fatty acids across the enterocyte membrane",
        "Receptor-mediated endocytosis of micelles": "Receptor-mediated endocytosis of intact micelles by specific surface receptors on enterocytes, which internalize the entire micellar structure",
        "Active transport using ATP-dependent pumps": "Active transport using ATP-dependent pumps embedded in the enterocyte brush border membrane to move fatty acids against their concentration gradient",
    },
    ("Unit8/Lesson8.7_Quiz.json", 12): {
        "The breakdown of stored fat into free fatty acids for energy": "The breakdown of stored fat into free fatty acids for energy during fasting or exercise, mediated by hormone-sensitive lipase in adipose tissue in response to catecholamine and glucagon signaling",
        "The fermentation of glucose by gut bacteria in the colon": "The fermentation of glucose and dietary fiber by gut bacteria in the colon, producing short-chain fatty acids that serve as an energy source for colonocytes and influence systemic metabolism",
        "The synthesis of glycogen from glucose after a meal": "The synthesis of glycogen from glucose after a meal, driven by insulin-mediated activation of glycogen synthase in hepatocytes and skeletal muscle fibers for storage of excess glucose",
    },
    ("Unit8/Lesson8.7_Quiz.json", 17): {
        "The increase in gastric acid secretion that occurs after a large meal": "The increase in gastric acid secretion that occurs after a large meal, mediated by gastrin release from G cells in the antrum and histamine release from enterochromaffin-like cells in the fundus",
        "The gradual increase in enzyme production by the pancreas during growth": "The gradual increase in digestive enzyme production by the pancreas during childhood growth, driven by rising levels of CCK and secretin as the GI tract matures and dietary complexity increases",
        "The increased absorption rate that occurs after a period of fasting": "The increased rate of nutrient absorption that occurs after a period of fasting, due to upregulation of intestinal brush border transporters and increased villous surface area in response to luminal nutrients",
    },
    ("Unit8/Lesson8.7_Quiz.json", 25): {
        "The liver can no longer produce insulin to regulate blood glucose": "The liver can no longer produce insulin to regulate blood glucose because hepatocyte destruction from cirrhosis eliminates the hepatic insulin-producing cells that normally supplement pancreatic secretion",
        "The liver can no longer absorb glucose from the portal vein": "The liver can no longer absorb glucose from the portal vein because the cirrhotic tissue has lost its glucose transporter proteins, allowing all dietary glucose to bypass hepatic uptake and enter systemic circulation",
        "The damaged liver overproduces glucagon, which paradoxically lowers blood sugar": "The damaged liver overproduces glucagon through disinhibited alpha cell signaling, which paradoxically lowers blood sugar by triggering excessive glucose uptake in peripheral skeletal muscle tissues",
    },
    ("Unit8/Lesson8.7_Quiz.json", 29): {
        "The sympathetic system destroys digestive enzymes while the parasympathetic system produces them": "The sympathetic nervous system destroys digestive enzymes through direct chemical degradation while the parasympathetic system produces new enzymes to replace them, creating a cycle of destruction and renewal",
        "Both systems promote digestion equally, but the sympathetic system also adds adrenaline to speed up the process": "Both systems promote digestion equally by stimulating gastric secretion and peristalsis, but the sympathetic system also releases adrenaline that accelerates enzymatic breakdown and nutrient absorption rates",
        "The sympathetic and parasympathetic systems have identical effects on digestion but operate at different times of day": "The sympathetic and parasympathetic systems have identical stimulatory effects on digestion but operate at different times of day, with the sympathetic system active during daytime meals and the parasympathetic system active during nighttime",
    },
    ("Unit8/Lesson8.7_Quiz.json", 30): {
        "The cephalic and gastric phases have no hormonal involvement; only the intestinal phase uses hormones": "The cephalic and gastric phases have no hormonal involvement and rely entirely on neural reflexes; only the intestinal phase uses hormones because the endocrine cells of the GI tract are located exclusively in the duodenum",
        "CCK controls the cephalic phase, secretin controls the gastric phase, and gastrin controls the intestinal phase": "CCK controls the cephalic phase by stimulating salivary and gastric secretion, secretin controls the gastric phase by promoting acid production, and gastrin controls the intestinal phase by triggering pancreatic enzyme release",
        "Gastrin is the only hormone involved, stimulating all phases of digestion from mouth to colon": "Gastrin is the only hormone involved in the regulation of digestion, stimulating all three phases from the mouth through the colon by acting on gastric, pancreatic, and colonic secretory cells",
    },
    # UNIT 9
    ("Unit9/Lesson9.1_Quiz.json", 16): {
        "The tip of a renal pyramid": "The tip of a renal pyramid that projects into the minor calyx and channels urine toward the renal pelvis",
        "A type of nephron found in the cortex": "A type of nephron found exclusively in the renal cortex with short loops of Henle that do not extend into the medulla",
        "The outermost layer of the kidney": "The outermost layer of the kidney containing the glomeruli and proximal and distal convoluted tubules of the nephrons",
    },
    ("Unit9/Lesson9.3_Quiz.json", 29): {
        "Hyperkalemia": "Hyperkalemia from excessive potassium release during surgical tissue manipulation",
        "Hypomagnesemia from blood loss during surgery": "Hypomagnesemia from blood loss during surgery depleting circulating magnesium stores",
        "Hyponatremia": "Hyponatremia from intravenous fluid dilution of serum sodium during the procedure",
    },
    ("Unit9/Lesson9.4_Quiz.json", 2): {
        "FSH": "FSH in response to GnRH pulsatile stimulation",
        "Inhibin": "Inhibin as a negative feedback hormone to the pituitary",
        "Estrogen": "Estrogen via aromatase conversion in peripheral tissues",
    },
    ("Unit9/Lesson9.4_Quiz.json", 4): {
        "7 days": "7 days (approximately one week from start to finish)",
        "1 month": "1 month (approximately 30 days from start to finish)",
        "1 year": "1 year (approximately 365 days from start to finish)",
    },
    ("Unit9/Lesson9.4_Quiz.json", 9): {
        "Testosterone": "Testosterone that promotes secondary sex characteristics and spermatogenesis",
        "Sperm cells": "Sperm cells produced through spermatogenesis in the seminiferous tubules",
        "Fructose-rich fluid for sperm energy": "Fructose-rich fluid produced by the seminal vesicles that provides energy for sperm motility",
    },
    ("Unit9/Lesson9.5_Quiz.json", 1): {
        "At menopause": "At menopause, when the remaining oocytes undergo final maturation and release",
        "At age 5": "At age 5, when the ovarian cortex begins producing primary oocytes de novo",
        "At puberty": "At puberty, when rising gonadotropins first stimulate oocyte production in the ovary",
    },
    ("Unit9/Lesson9.5_Quiz.json", 2): {
        "Vagina": "Vagina (lower birth canal)",
        "Ovary": "Ovary (gonadal tissue)",
        "Uterus": "Uterus (endometrial cavity)",
    },
    ("Unit9/Lesson9.5_Quiz.json", 5): {
        "hCG": "hCG (human chorionic gonadotropin from the placenta)",
        "FSH and LH": "FSH and LH (gonadotropins from the anterior pituitary)",
        "Only estrogen": "Only estrogen (produced by the developing follicle cells)",
    },
    ("Unit9/Lesson9.5_Quiz.json", 6): {
        "Progesterone and inhibin": "Progesterone and inhibin maintaining the corpus luteum and suppressing FSH secretion",
        "Testosterone": "Testosterone produced by theca cells driving follicular androgen synthesis in the ovary",
        "LH only": "LH only, stimulating progesterone production from the corpus luteum after ovulation",
    },
    ("Unit9/Lesson9.5_Quiz.json", 30): {
        "Appendicitis": "Appendicitis presenting with right lower quadrant pain from inflammation of the vermiform appendix",
        "A ruptured ovarian cyst": "A ruptured ovarian cyst causing acute pelvic pain from hemorrhagic fluid irritating the peritoneum",
        "Ovarian torsion": "Ovarian torsion causing acute pelvic pain from rotation of the ovary on its vascular pedicle",
    },
    ("Unit9/Lesson9.6_Quiz.json", 18): {
        "An oral contraceptive that prevents ovulation": "An oral contraceptive that prevents ovulation by providing synthetic estrogen and progestin to suppress the mid-cycle LH surge from the anterior pituitary",
        "An injectable hormone used only during IVF procedures": "An injectable hormone used exclusively during in vitro fertilization procedures to stimulate multiple follicle development and synchronized oocyte maturation for retrieval",
        "A testosterone replacement therapy for men": "A testosterone replacement therapy for men with hypogonadism that restores serum testosterone levels to the normal range and improves libido and muscle mass",
    },
    ("Unit9/Lesson9.6_Quiz.json", 29): {
        "Progesterone": "Progesterone (produced by the corpus luteum of the ovary)",
        "Oxytocin": "Oxytocin (released by the posterior pituitary gland)",
        "Estrogen": "Estrogen (produced by ovarian follicular granulosa cells)",
    },
    ("Unit9/Lesson9.7_Quiz.json", 4): {
        "Stage 1 kidney disease": "Stage 1 kidney disease with normal GFR above 90 mL/min and minimal proteinuria",
        "Acute kidney injury": "Acute kidney injury with sudden onset of elevated creatinine over hours to days",
        "Mild kidney disease": "Mild kidney disease with slightly reduced GFR between 60 and 89 mL/min",
    },
    ("Unit9/Lesson9.7_Quiz.json", 17): {
        "Protein in the urine": "Protein in the urine detected by dipstick or quantitative measurement",
        "Glucose in the urine": "Glucose in the urine indicating hyperglycemia exceeding the renal threshold",
        "Bacteria in the urine": "Bacteria in the urine indicating a urinary tract infection or contamination",
    },
    ("Unit9/Lesson9.7_Quiz.json", 30): {
        "ADPKD can be cured with antibiotics if caught early": "ADPKD can be cured with antibiotics if caught early in the disease course, because the cyst formation is driven by chronic low-grade bacterial infection of the renal parenchyma",
        "ADPKD only affects children and resolves spontaneously by adulthood": "ADPKD only affects children and resolves spontaneously by adulthood as the kidneys mature and the cystic lesions are reabsorbed through normal developmental renal remodeling processes",
        "ADPKD only affects the kidneys and has no other systemic manifestations": "ADPKD only affects the kidneys and has no other systemic manifestations because the PKD1 and PKD2 gene mutations are exclusively expressed in renal tubular epithelial cells",
    },
    ("Unit9/Lesson9.8_Quiz.json", 11): {
        "Cardiac output": "Cardiac output, measuring the total volume of blood pumped by the heart per minute",
        "Glomerular filtration rate (GFR)": "Glomerular filtration rate, measuring the volume of plasma filtered by the glomeruli per minute",
        "Total blood volume": "Total blood volume, measuring the combined volume of plasma and formed elements in circulation",
    },
    ("Unit9/Lesson9.8_Quiz.json", 15): {
        "The venous drainage system of the renal pelvis": "The venous drainage system of the renal pelvis that collects blood from the medullary interstitium and returns it through the renal vein to the inferior vena cava",
        "The afferent and efferent arterioles of the glomerulus": "The afferent and efferent arterioles of the glomerulus that regulate glomerular filtration pressure and rate through changes in their respective vascular tone",
        "The blood vessels supplying the renal cortex only": "The blood vessels supplying the renal cortex only, including the interlobular arteries and cortical peritubular capillaries that support tubular reabsorption",
    },
    ("Unit9/Lesson9.8_Quiz.json", 17): {
        "The adequacy of dialysis treatment": "The adequacy of dialysis treatment, measured by comparing pre- and post-dialysis BUN levels to ensure sufficient clearance of uremic toxins",
        "The severity of proteinuria": "The severity of proteinuria, measured by quantifying the amount of protein excreted in a 24-hour urine collection to assess glomerular barrier integrity",
        "Liver function and bile production": "Liver function and bile production, assessed by measuring serum bilirubin and hepatic transaminase levels to evaluate hepatocellular integrity and biliary patency",
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

# Verify both units
for unit in ['Unit8', 'Unit9']:
    files = sorted(glob.glob(os.path.join(base, unit, '*Quiz*.json')))
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
                print(f'STILL FLAGGED: {unit}/{os.path.basename(f)} Q{q["question_number"]}: ratio={cl/awl:.1f}')
    if still_flagged == 0:
        print(f"{unit}: ALL CLEAR!")
    else:
        print(f"{unit}: {still_flagged} still flagged")
