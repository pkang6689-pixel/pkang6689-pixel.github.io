import os
import re
import json
import random
from bs4 import BeautifulSoup

# Paths
PROJECT_ROOT = "/workspaces/ArisEdu/ArisEdu Project Folder"
CHEM_DIR = os.path.join(PROJECT_ROOT, "ChemistryLessons")
PHYS_DIR = os.path.join(PROJECT_ROOT, "PhysicsLessons")

# Template Source: Chemistry Unit 1
UNIT1_DIR = os.path.join(CHEM_DIR, "Unit1")
TEMPLATE_SUMMARY = os.path.join(UNIT1_DIR, "Lesson 1.1 States_of_Matter Summary.html")
TEMPLATE_PRACTICE = os.path.join(UNIT1_DIR, "Lesson 1.1 States_of_Matter Practice.html")
TEMPLATE_QUIZ = os.path.join(UNIT1_DIR, "Lesson 1.1 States_of_Matter Quiz.html")

# Global data store
lesson_concepts = {}

def get_lesson_info(filename):
    # Support "Lesson X.Y..." and "PhysicsLessonX.Y..."
    
    # Try stricter pattern for Physics no-space
    match_phys = re.search(r"(PhysicsLesson)(\d+\.\d+)(.+?)(Summary|Practice|Quiz)\.html", filename)
    if match_phys:
        prefix = match_phys.group(1)
        lesson_id = match_phys.group(2)
        raw_title = match_phys.group(3)
        title = re.sub(r"([A-Z])", r" \1", raw_title).strip() # CamelCase to Space
        file_type = match_phys.group(4)
        return prefix, lesson_id, title, raw_title, file_type
    
    # Try pattern for Chemistry (Lesson 1.1 Name_of_Lesson Summary.html)
    match_chem = re.search(r"(Lesson) (\d+\.\d+) (.+?) (Summary|Practice|Quiz)\.html", filename)
    if match_chem:
        prefix = match_chem.group(1)
        lesson_id = match_chem.group(2)
        raw_title = match_chem.group(3) # Has underscores
        title = raw_title.replace("_", " ")
        file_type = match_chem.group(4)
        return prefix, lesson_id, title, raw_title, file_type
            
    return None, None, None, None, None

def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def extract_content(html_content, file_type):
    soup = BeautifulSoup(html_content, "html.parser")
    view_id = ""
    if file_type == "Summary": view_id = "summary-content-view"
    elif file_type == "Practice": view_id = "practice-content-view"
    elif file_type == "Quiz": view_id = "quiz-content-view"
    
    div = soup.find("div", id=view_id)
    if div: return str(div)
    if view_id in html_content: return html_content
    return f'<div id="{view_id}"><h1>Content Missing</h1></div>'

def extract_concepts_from_summary(html_content):
    concepts = []
    soup = BeautifulSoup(html_content, "html.parser")
    lis = soup.find_all("li")
    for li in lis:
        text = li.get_text()
        if ":" in text:
            parts = text.split(":", 1)
            concepts.append({"term": parts[0].strip(), "definition": parts[1].strip()})
    return concepts

def generate_flashcards_js(concepts):
    js_data = "const flashcards = [\n"
    for c in concepts:
        t = c["term"].replace("'", "\\'")
        d = c["definition"].replace("'", "\\'")
        js_data += f"    {{ term: '{t}', definition: '{d}' }},\n"
    js_data += "];\n"
    return js_data

def generate_quiz_js(concepts):
    questions = []
    all_defs = [c["definition"] for c in concepts]
    if len(all_defs) < 4: all_defs = all_defs * 4
    
    for c in concepts:
        correct = c["definition"]
        dists = [d for d in all_defs if d != correct]
        if len(dists) < 3: dists += ["A", "B", "C"]
        opts = random.sample(dists, 3) + [correct]
        random.shuffle(opts)
        correct_idx = opts.index(correct)
        
        questions.append({
            "question": f"What is the definition of '{c['term']}'?",
            "options": opts,
            "correct": correct_idx
        })
    return "const quizQuestions = " + json.dumps(questions, indent=4) + ";\n"

def apply_template(target_path, template_content, payload, prefix, lesson_id, title, raw_title, file_type):
    template_soup = BeautifulSoup(template_content, "html.parser")
    
    view_id = f"{file_type.lower()}-content-view"
    target_div = template_soup.find("div", id=view_id)
    if target_div:
        payload_soup = BeautifulSoup(payload, "html.parser")
        if payload_soup.find("div", id=view_id):
            target_div.replace_with(payload_soup.find("div", id=view_id))
        else:
            target_div.clear()
            target_div.append(payload_soup)
            
    if template_soup.find("title"):
        template_soup.find("title").string = f"{prefix} {lesson_id}: {title}"
    
    pt = template_soup.find("h2", class_="page-title")
    if pt: pt.string = f"{prefix} {lesson_id}: {title} {file_type}"
    
    sep = " " if prefix == "Lesson" else ""
    target_base = f"{prefix}{sep}{lesson_id}{sep}{raw_title}"
    
    back_target = ""
    back_text = ""
    if file_type == "Summary":
        back_target = f"{target_base}.html"
        back_text = f"← Back to Lesson {lesson_id}"
    elif file_type == "Practice":
        back_target = f"{target_base}{sep}Summary.html"
        back_text = "← Back to Summary"
    elif file_type == "Quiz":
        back_target = f"{target_base}{sep}Practice.html"
        back_text = "← Back to Practice"
        
    btn = template_soup.find("button", id="back-button")
    if btn: btn.string = back_text
    
    scripts = template_soup.find_all("script")
    for script in scripts:
        if script.string:
            s = script.string
            # Regex replacements
            s = re.sub(r"window\.location\.href\s*=\s*['\"].*?Summary\.html['\"]", f"window.location.href = '{back_target}'", s)
            s = re.sub(r"window\.location\.href\s*=\s*['\"].*?Practice\.html['\"]", f"window.location.href = '{back_target}'", s)
            if file_type == "Summary":
                s = re.sub(r"window\.location\.href\s*=\s*['\"].*?States_Of_Matter\.html['\"]", f"window.location.href = '{back_target}'", s)
            
            s = re.sub(r'backBtn\.innerText\s*=\s*".*?";', f'backBtn.innerText = "{back_text}";', s)
            
            # Inject Data
            key = f"{lesson_id}_{raw_title}"
            concepts = lesson_concepts.get(key, [])
            
            if file_type == "Practice" and concepts and "const flashcards =" in s:
                pattern = r"const flashcards\s*=\s*\[.*?\];"
                s = re.sub(pattern, generate_flashcards_js(concepts), s, flags=re.DOTALL)
            elif file_type == "Quiz" and concepts and "const quizQuestions =" in s:
                pattern = r"const quizQuestions\s*=\s*\[.*?\];"
                s = re.sub(pattern, generate_quiz_js(concepts), s, flags=re.DOTALL)
                
            script.string = s

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(str(template_soup))

def process_directory(base_dir, templates):
    temp_summary, temp_practice, temp_quiz = templates
    
    # 1. Summaries
    for root, dirs, files in os.walk(base_dir):
        # Skip Chem Unit 1 source logic
        if "ChemistryLessons/Unit1" in root.replace("\\", "/"): continue
        if root.endswith("Unit1") and "ChemistryLessons" in base_dir: continue

        for file in files:
            if "Summary.html" in file:
                prefix, lesson_id, title, raw_title, _ = get_lesson_info(file)
                if not lesson_id: continue
                
                path = os.path.join(root, file)
                print(f"Summary: {file}")
                with open(path, "r", encoding="utf-8") as f: content = f.read()
                
                if "<html" in content[:100]: payload = extract_content(content, "Summary")
                else: payload = content
                
                concepts = extract_concepts_from_summary(payload)
                key = f"{lesson_id}_{raw_title}"
                lesson_concepts[key] = concepts
                
                apply_template(path, temp_summary, payload, prefix, lesson_id, title, raw_title, "Summary")

    # 2. Practice/Quiz
    for root, dirs, files in os.walk(base_dir):
        if "ChemistryLessons/Unit1" in root.replace("\\", "/"): continue
        if root.endswith("Unit1") and "ChemistryLessons" in base_dir: continue

        for file in files:
            if "Summary.html" in file: continue
            if "Practice.html" not in file and "Quiz.html" not in file: continue
            
            prefix, lesson_id, title, raw_title, ftype = get_lesson_info(file)
            if not lesson_id: continue
            
            path = os.path.join(root, file)
            print(f"{ftype}: {file}")
            with open(path, "r", encoding="utf-8") as f: content = f.read()
            
            if "<html" in content[:100]: payload = extract_content(content, ftype)
            else: payload = content
            
            tmpl = temp_practice if ftype == "Practice" else temp_quiz
            apply_template(path, tmpl, payload, prefix, lesson_id, title, raw_title, ftype)

def main():
    print("Loading templates...")
    templates = (load_template(TEMPLATE_SUMMARY), load_template(TEMPLATE_PRACTICE), load_template(TEMPLATE_QUIZ))
    
    print("Processing Chemistry...")
    process_directory(CHEM_DIR, templates)
    
    print("Processing Physics...")
    process_directory(PHYS_DIR, templates)

if __name__ == "__main__":
    main()
