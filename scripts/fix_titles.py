import os
import re
from bs4 import BeautifulSoup

# Paths
PROJECT_ROOT = "/workspaces/ArisEdu/ArisEdu Project Folder"
CHEM_DIR = os.path.join(PROJECT_ROOT, "ChemistryLessons")
PHYS_DIR = os.path.join(PROJECT_ROOT, "PhysicsLessons")

def get_lesson_info(filename):
    # Physics naming: PhysicsLesson3.3NewtonsSecondLaw...
    # Chemistry naming: Lesson 6.7 Net_Ionic_Equations...
    
    # 1. Physics Pattern
    # Matches: PhysicsLesson3.3NewtonsSecondLawFEqualsMaSummary.html
    match_phys = re.search(r"PhysicsLesson\s?(\d+\.\d+)(.+?)(Summary|Practice|Quiz)?\.html", filename)
    if match_phys:
        lesson_id = match_phys.group(1)
        raw_title = match_phys.group(2)
        # Split CamelCase: "NewtonsSecondLaw" -> "Newtons Second Law"
        title = re.sub(r"([A-Z])", r" \1", raw_title).strip()
        file_type = match_phys.group(3) if match_phys.group(3) else ""
        return lesson_id, title, file_type

    # 2. Chemistry Pattern
    # Matches: Lesson 6.7 Net_Ionic_Equations.html
    match_chem = re.search(r"Lesson (\d+\.\d+) (.+?)( Summary| Practice| Quiz)?\.html", filename)
    if match_chem:
        lesson_id = match_chem.group(1)
        raw_title = match_chem.group(2)
        title = raw_title.replace("_", " ").strip()
        # The regex group 3 includes the space, strip it
        file_type = match_chem.group(3).strip() if match_chem.group(3) else ""
        return lesson_id, title, file_type
        
    return None, None, None

def fix_file(path, lesson_id, title, file_type):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, "html.parser")
    modified = False
    
    # Expected Strings
    # Page Title: "Lesson X.Y: Title [Type]"
    type_suffix = f": {file_type}" if file_type == "Quiz" else f" {file_type}" if file_type else ""
    # Usually: "Lesson 6.7: Net Ionic Equations Summary" or "Lesson 6.7: Net Ionic Equations"
    
    # There is variance in how titles are formatted in the wild.
    # Standard we want: "Lesson {lesson_id}: {title} {file_type}" (stripped)
    
    expected_title_prefix = f"Lesson {lesson_id}"
    
    # 1. Update <title>
    if soup.title and soup.title.string:
        old_title = soup.title.string
        # Replace the "Lesson X.Y" part, or the whole thing?
        # If we replace the whole thing we ensure consistency.
        # Format: "Lesson 6.7: Net Ionic Equations" (even if Summary, usually title tag is simple)
        # Let's match existing content style. 
        # Usually: Lesson 6.4: Net Ionic Equations
        
        # We will preserve the format "Lesson ID: Title"
        # If file_type is present, usually it is appended or checking previous files:
        # Before fix: <title>Lesson 6.4: Net Ionic Equations</title>
        # Desired: <title>Lesson 6.7: Net Ionic Equations</title>
        
        # If it's a Summary file: <title>Lesson 6.7: Net Ionic Equations Summary</title> ?
        # Let's check what `apply_styles.py` did: `f"Lesson {lesson_id}: {title}"` (no file type usually in <title> from my code, but inconsistent)
        
        # Let's construct a robust title string
        if file_type:
            new_title_text = f"Lesson {lesson_id}: {title} {file_type}"
        else:
            new_title_text = f"Lesson {lesson_id}: {title}"
            
        if soup.title.string != new_title_text:
            # print(f"Updating <title> in {os.path.basename(path)}: '{soup.title.string}' -> '{new_title_text}'")
            soup.title.string = new_title_text
            modified = True
            
    # 2. Update h2.page-title
    # Can appear multiple times (visible, hidden views, rubrics)
    page_titles = soup.find_all("h2", class_="page-title")
    for pt in page_titles:
        if not pt.string: continue
        
        text = pt.string
        # Regex to match "Lesson \d+\.\d+"
        if re.search(r"Lesson \d+\.\d+", text):
            # Check if it needs update
            if f"Lesson {lesson_id}" not in text:
                # Replace ID
                new_text = re.sub(r"Lesson \d+\.\d+", f"Lesson {lesson_id}", text)
                
                # Check if Title also mismatches?
                # e.g. "Lesson 6.7: Wrong Title" -> "Lesson 6.7: Correct Title"
                # This is harder to do safely without verifying the rest of string matches.
                # But the user specifically asked for "Lesson number".
                # "The text... says Lesson 6.4... It should correspond to the course unit's lesson number"
                
                # However, if I copied 6.4 file to 6.7, the title text "Net Ionic Equations" might actually be from 6.4 (if 6.4 was "Intermolecular Forces" for example).
                # But in this specific case, the User says content is "Lesson 6.4 Net Ionic Equations". 
                # This suggests the Title text "Net Ionic Equations" IS correct for 6.7, but the Number 6.4 is wrong.
                # OR the file 6.7 is a copy of 6.4, and the text says "Lesson 6.4 Some Other Title".
                
                # PROCEED CAUTIOUSLY: Only update the NUMBER first. 
                # Unless the text specifically looks generic.
                
                # Wait, user said: "the text ... says Lesson 6.4 Net Ionic Equations"
                # This implies the Title Text matches current file (Net Ionic Eqs), but number is wrong.
                # So replacing just the number is safe and requested.
                
                if text != new_text:
                    # print(f"Updating h2 in {os.path.basename(path)}: '{text}' -> '{new_text}'")
                    pt.string = new_text
                    modified = True

    # 3. Update "Back to Lesson X.Y" buttons
    # Often in <button id="back-button"> or JS
    # Grep showed: <button ...>← Back to Lesson 6.4</button>
    
    # HTML Button
    back_btn = soup.find("button", id="back-button")
    if back_btn and back_btn.string:
        text = back_btn.string
        if re.search(r"Back to Lesson \d+\.\d+", text):
             new_text = re.sub(r"Lesson \d+\.\d+", f"Lesson {lesson_id}", text)
             if text != new_text:
                 back_btn.string = new_text
                 modified = True
                 
    # JS Scripts (window.location.href, backBtn.innerText)
    # This is tricky with BeautifulSoup as it parses script contents as string.
    if soup.find("script"):
        for script in soup.find_all("script"):
            if script.string:
                js = script.string
                # Update innerText assignment
                # backBtn.innerText = "← Back to Lesson 6.4";
                new_js = re.sub(r'Back to Lesson \d+\.\d+', f'Back to Lesson {lesson_id}', js)
                
                # Update Navigation Links
                # window.location.href = 'Lesson 6.4 Net_Ionic_Equations.html';
                # If we just change the number, do we break the link?
                # If the TARGET filename also has the wrong number (unlikely in this repo structure), we break it.
                # But here, we have `Lesson 6.7 ...`. The back link should be to `Lesson 6.7 ...`.
                # If the JS says `Lesson 6.4 ...`, it is pointing to a different file.
                # We want it to point to THIS lesson family.
                
                # Regex replace Lesson \d+\.\d+ inside quotes IF it looks like a filename?
                # 'Lesson 6.4 Net_Ionic_Equations.html' -> 'Lesson 6.7 Net_Ionic_Equations.html'
                
                # Strategy: Replace the ID in the JS strings that look like titles or filenames
                if new_js != js:
                    script.string = new_js
                    modified = True

    if modified:
        print(f"Fixed {os.path.basename(path)}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(str(soup))

def main():
    print("Scanning ChemistryLessons...")
    for root, dirs, files in os.walk(CHEM_DIR):
        for file in files:
            if file.endswith(".html"):
                lid, title, ftype = get_lesson_info(file)
                if lid:
                    fix_file(os.path.join(root, file), lid, title, ftype)
                    
    print("Scanning PhysicsLessons...")
    for root, dirs, files in os.walk(PHYS_DIR):
        for file in files:
            if file.endswith(".html"):
                lid, title, ftype = get_lesson_info(file)
                if lid:
                    fix_file(os.path.join(root, file), lid, title, ftype)

if __name__ == "__main__":
    main()
