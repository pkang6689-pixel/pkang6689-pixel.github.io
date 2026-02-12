import os
from bs4 import BeautifulSoup

directory = "ArisEdu Project Folder/ChemistryLessons/Unit1"
files = [f for f in os.listdir(directory) if f.startswith("Lesson 1.") and f.endswith(".html")]

print(f"fixing {len(files)} files...")

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    modified = False

    # 1. Locate the containers
    mixmatch = soup.find(id="mixmatch-container")
    blockpuzzle = soup.find(id="blockpuzzle-container")
    
    # 2. Locate the correct destination
    practice_view = soup.find(id="practice-content-view")
    if practice_view:
        practice_card = practice_view.find("div", class_="diagram-card")
        
        if practice_card:
            # Move MixMatch
            if mixmatch and mixmatch.parent != practice_card:
                print(f"Moving MixMatch in {filename}")
                mixmatch.extract() # Remove from current location
                practice_card.append(mixmatch) # Add to correct location
                modified = True
            
            # Move BlockPuzzle
            if blockpuzzle and blockpuzzle.parent != practice_card:
                print(f"Moving BlockPuzzle in {filename}")
                blockpuzzle.extract()
                practice_card.append(blockpuzzle)
                modified = True
            
            # 3. Fix Flashcard ID
            # Currently it expects id="flashcard-game" for switching logic
            # But the div only has class="flashcard-game"
            flashcard_div = practice_view.find("div", class_="flashcard-game")
            if flashcard_div:
                if not flashcard_div.get("id"):
                    flashcard_div["id"] = "flashcard-game"
                    print(f"Added ID to flashcard-game in {filename}")
                    modified = True
        else:
            print(f"Warning: No diagram-card found in practice view for {filename}")
    else:
        print(f"Warning: No practice-content-view found for {filename}")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Saved {filename}")
    else:
        print(f"No changes for {filename}")
