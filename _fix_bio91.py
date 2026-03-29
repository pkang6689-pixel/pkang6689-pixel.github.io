import json

# Fix remaining flagged questions in 3 files

# 1) Bio Lesson9.5 Q29, Q30
f = 'content_data/BiologyLessons/Unit9/Lesson9.5_Quiz.json'
with open(f, 'r', encoding='utf-8') as fh:
    data = json.load(fh)
fixes = {
    29: {"wrong": [
        "Organoids can fully replace all forms of animal testing with immediate effect because they perfectly replicate every physiological function of complete human organs, including systemic blood supply, immune responses, and hormonal regulation from connected endocrine glands",
        "Organoids are structurally and functionally identical to fully developed human brains complete with mature neural circuits, long-range axonal projections, blood-brain barrier vasculature, and emergent consciousness — making them equivalent to actual brain tissue in every measurable way",
        "Organoids do not require any stem cells or progenitor cells to create and can be grown entirely from simple inorganic chemical precursors such as amino acids, nucleotides, and salts placed in standard culture media without any biological starting material"
    ]},
    30: {"wrong": [
        "iPSCs naturally and spontaneously correct all genetic mutations during the reprogramming process from somatic cells back to pluripotency, making any additional gene editing step with CRISPR-Cas9 or other nuclease systems completely unnecessary for treating genetic diseases like sickle cell anemia",
        "This combined approach only provides temporary symptomatic relief and requires lifelong repeated treatments because the fundamental genetic defect remains permanently embedded in the patient's bone marrow stem cell population and cannot be corrected at the genomic level by current methods",
        "CRISPR-Cas9 nuclease technology alone is sufficient to cure sickle cell disease without any stem cell involvement, iPSC reprogramming, or bone marrow transplantation — a single injection of the CRISPR components directly into the patient's bloodstream edits all circulating red blood cells"
    ]},
}
for q in data['quiz_questions']:
    if q['question_number'] in fixes:
        wi = 0
        for opt in q['options']:
            if not opt['is_correct']:
                opt['text'] = fixes[q['question_number']]['wrong'][wi]
                wi += 1
with open(f, 'w', encoding='utf-8') as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False)
print(f'Fixed {f}')

# 2) Bio Lesson11.4 Q30
f = 'content_data/BiologyLessons/Unit11/Lesson11.4_Quiz.json'
with open(f, 'r', encoding='utf-8') as fh:
    data = json.load(fh)
fixes = {
    30: {"wrong": [
        "Lactose intolerance occurs because the stomach lining cannot produce enough hydrochloric acid to properly curdle and denature the casein and whey proteins in milk, resulting in incomplete protein digestion and the accumulation of undigested protein fragments in the intestinal lumen",
        "The intolerant person's gallbladder and liver cannot produce sufficient bile salts to emulsify the milk fat globules into smaller droplets, preventing lipase enzymes from accessing and hydrolyzing the dairy triglycerides needed for proper fat absorption across intestinal villi",
        "The intolerant person has developed an IgE-mediated type I hypersensitivity allergic reaction to the milk protein casein, which triggers mast cell degranulation, histamine release, and an inflammatory cascade throughout the gastrointestinal mucosa upon exposure to dairy products"
    ]},
}
for q in data['quiz_questions']:
    if q['question_number'] in fixes:
        wi = 0
        for opt in q['options']:
            if not opt['is_correct']:
                opt['text'] = fixes[q['question_number']]['wrong'][wi]
                wi += 1
with open(f, 'w', encoding='utf-8') as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False)
print(f'Fixed {f}')

# 3) Bio Lesson12.1 Q29
f = 'content_data/BiologyLessons/Unit12/Lesson12.1_Quiz.json'
with open(f, 'r', encoding='utf-8') as fh:
    data = json.load(fh)
fixes = {
    29: {"wrong": [
        "Gene drives modify only one individual mosquito at a time, requiring the physical capture, laboratory genetic editing, and re-release of every single mosquito in a wild population — making large-scale deployment logistically impossible without trapping millions of individual insects",
        "Gene drive technology only functions under highly controlled laboratory conditions with specific temperature, humidity, and nutrient requirements, and the genetic modifications would immediately fail and revert to wild-type sequences when engineered mosquitoes are released into natural field environments",
        "Gene drives operate by completely sterilizing every mosquito that carries the modification, rapidly eliminating the entire Anopheles species within a single generation of field release — there is no mechanism for the trait to spread through reproduction since carriers cannot produce offspring"
    ]},
}
for q in data['quiz_questions']:
    if q['question_number'] in fixes:
        wi = 0
        for opt in q['options']:
            if not opt['is_correct']:
                opt['text'] = fixes[q['question_number']]['wrong'][wi]
                wi += 1
with open(f, 'w', encoding='utf-8') as fh:
    json.dump(data, fh, indent=2, ensure_ascii=False)
print(f'Fixed {f}')
