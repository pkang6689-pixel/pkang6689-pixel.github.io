import os
from bs4 import BeautifulSoup

directory = "ArisEdu Project Folder/ChemistryLessons/Unit1"
files = [f for f in os.listdir(directory) if f.startswith("Lesson 1.") and f.endswith(".html")]

print(f"Found {len(files)} files to check and restore.")

# The HTML block to restore/insert
def create_actions_panel(soup):
    container = soup.new_tag("div", attrs={"class": "Practice-actions", "style": "margin-top:2rem;display:flex;justify-content:flex-end;width:100%;"})
    
    # Menu
    menu = soup.new_tag("div", attrs={"class": "Practices-menu", "style": "position:relative; margin-right: 1rem;"})
    
    btn = soup.new_tag("button", attrs={"class": "side-button view-other-Practices", "onclick": "togglePracticesPanel(this)", "type": "button"})
    btn.string = "Other games"
    menu.append(btn)
    
    panel = soup.new_tag("div", attrs={"class": "Practices-panel", "aria-hidden": "true"})
    
    # Links
    links = [
        ("#flashcard-game", "Flashcard Game", ""),
        ("#climb", "Boost", ""), 
        ("../../GameMatch.html", "Mix & Match", "_blank"),
        ("../../GameBlocks.html", "Block Puzzle", "_blank")
    ]
    
    for href, text, target in links:
        item = soup.new_tag("div", attrs={"class": "Practices-panel-item"})
        a_attrs = {"href": href}
        if target:
            a_attrs["target"] = target
        a = soup.new_tag("a", attrs=a_attrs)
        a.string = text
        item.append(a)
        panel.append(item)
    
    menu.append(panel)
    container.append(menu)
    
    # Next button (Standardize next button? Or try to preserve?)
    # Usually it's "Next Up: Quiz". Let's add it.
    next_btn = soup.new_tag("button", attrs={"class": "side-button", "onclick": "toggleToQuiz(event)"})
    next_btn.string = "Next Up: Quiz"
    container.append(next_btn)
    
    return container

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    modified = False
    
    # Check if panel missing
    practice_actions = soup.find("div", class_="Practice-actions")
    
    if not practice_actions:
        print(f"Restoring panel in {filename}...")
        
        # Find where to insert using #practice-content-view .diagram-card
        practice_view = soup.find(id="practice-content-view")
        if practice_view:
            card = practice_view.find("div", class_="diagram-card")
            if card:
                new_panel = create_actions_panel(soup)
                card.append(new_panel)
                modified = True
                print("  - Appended new Practice-actions panel")
            else:
                print("  - Error: diagram-card not found inside practice-content-view")
        else:
            print("  - Error: practice-content-view not found")
    else:
        # Panel exists (e.g. Lesson 1.1), ensure links are there (already done by previous script usually, but doublcheck)
        panel = practice_actions.find("div", class_="Practices-panel")
        if panel:
            current_hrefs = [a['href'] for a in panel.find_all("a")]
            if "../../GameMatch.html" not in current_hrefs:
                 # Add it
                 item = soup.new_tag("div", attrs={"class": "Practices-panel-item"})
                 a = soup.new_tag("a", href="../../GameMatch.html", target="_blank")
                 a.string = "Mix & Match"
                 item.append(a)
                 panel.append(item)
                 modified = True
                 print("  - Added Mix & Match to existing panel")
            if "../../GameBlocks.html" not in current_hrefs:
                 item = soup.new_tag("div", attrs={"class": "Practices-panel-item"})
                 a = soup.new_tag("a", href="../../GameBlocks.html", target="_blank")
                 a.string = "Block Puzzle"
                 item.append(a)
                 panel.append(item)
                 modified = True
                 print("  - Added Block Puzzle to existing panel")

    # Double check Hub removal just in case
    hub = soup.find(id="lesson-games-hub")
    if hub:
        hub.decompose()
        modified = True
        print("  - Removed leftover lesson-games-hub")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"  - Saved changes.")
    else:
        print(f"  - {filename} is up to date.")
