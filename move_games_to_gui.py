import os
from bs4 import BeautifulSoup

directory = "ArisEdu Project Folder/ChemistryLessons/Unit1"
files = [f for f in os.listdir(directory) if f.startswith("Lesson 1.") and f.endswith(".html")]

print(f"Found {len(files)} files to process.")

for filename in files:
    filepath = os.path.join(directory, filename)
    print(f"Processing {filename}...")
    
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    modified = False
    
    # 1. Remove the Hub (Big Buttons)
    hub = soup.find(id="lesson-games-hub")
    if hub:
        hub.decompose()
        print(f"  - Removed lesson-games-hub")
        modified = True
    
    # 2. Add to Other Games Details
    panel = soup.find("div", class_="Practices-panel")
    if panel:
        # Check if links already exist
        links = panel.find_all("a")
        hrefs = [a['href'] for a in links]
        
        # Add Mix & Match
        if "../../GameMatch.html" not in hrefs:
            new_div = soup.new_tag("div", attrs={"class": "Practices-panel-item"})
            new_link = soup.new_tag("a", href="../../GameMatch.html", target="_blank")
            new_link.string = "Mix & Match"
            new_div.append(new_link)
            panel.append(new_div)
            print("  - Added Mix & Match link")
            modified = True
            
        # Add Block Puzzle
        if "../../GameBlocks.html" not in hrefs:
            new_div = soup.new_tag("div", attrs={"class": "Practices-panel-item"})
            new_link = soup.new_tag("a", href="../../GameBlocks.html", target="_blank")
            new_link.string = "Block Puzzle"
            new_div.append(new_link)
            panel.append(new_div)
            print("  - Added Block Puzzle link")
            modified = True
    else:
        print("  - WARNING: Practices-panel not found!")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"  - Saved changes to {filename}")
    else:
        print(f"  - No changes needed.")
