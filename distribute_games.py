import os
import re
from bs4 import BeautifulSoup

# Configuration
SOURCE_FILE = '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/Unit1/Lesson 1.1 States_Of_Matter.html'
TARGET_DIRS = [
    '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/',
    '/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons/'
]

def load_source_components(source_path):
    print(f"Loading source from {source_path}...")
    with open(source_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    components = {}

    # 2. Extract Game Containers (HTML)
    mixmatch_container = soup.find(id='mixmatch-container')
    blockpuzzle_container = soup.find(id='blockpuzzle-container')
    
    if not mixmatch_container or not blockpuzzle_container:
        print("Could not find game containers in source file!")
        # Fallback handling or error
        # If I can't find them, I cannot proceed.
        # But wait, maybe the source file content I read earlier has them.
        # Let's hope the file in workspace is up to date.
        pass
        
    components['mixmatch_html'] = str(mixmatch_container) if mixmatch_container else ""
    components['blockpuzzle_html'] = str(blockpuzzle_container) if blockpuzzle_container else ""

    # 3. Extract JavaScript
    scripts = soup.find_all('script')
    game_script = None
    for script in scripts:
        if script.string and ('window.switchToMixMatch' in script.string or 'const mixMatchData' in script.string):
            game_script = script.string
            break
            
    if not game_script:
         # Try finding by content length or other features
        for script in scripts:
             if script.string and 'mixMatchData' in script.string:
                 game_script = script.string
                 break
    
    if not game_script:
        print("Could not find game script!")
        
    components['js_logic'] = game_script

    return components

def process_file(file_path, components):
    print(f"Processing {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
        
        # Check if already processed
        has_games = soup.find(id='mixmatch-container')
        
        # 1. Locate the Practice View's diagram-card
        # It's usually in <div id="practice-content-view"> -> <div class="diagram-card">
        practice_view = soup.find(id='practice-content-view')
        if not practice_view:
            print(f"Skipping {file_path} - no practice view found.")
            return
            
        diagram_card = practice_view.find('div', class_='diagram-card')
        if not diagram_card:
            print(f"Skipping {file_path} - no diagram-card in practice view.")
            return

        # 2. Insert Game Containers (if not present)
        if not has_games:
            # We append them before the .Practice-actions div, or at the end if not found
            practice_actions = diagram_card.find('div', class_='Practice-actions')
            
            # Convert HTML strings to BeautifulSoup objects
            mixmatch_soup = BeautifulSoup(components['mixmatch_html'], 'html.parser')
            blockpuzzle_soup = BeautifulSoup(components['blockpuzzle_html'], 'html.parser')
            
            # Copy to avoid reference issues
            mm_tag = mixmatch_soup.find(id='mixmatch-container')
            bp_tag = blockpuzzle_soup.find(id='blockpuzzle-container')
            
            if mm_tag and bp_tag:
                if practice_actions:
                    practice_actions.insert_before(mm_tag)
                    practice_actions.insert_before(bp_tag)
                else:
                    diagram_card.append(mm_tag)
                    diagram_card.append(bp_tag)
        else:
            print(f"Games containers already present in {file_path}")

        # 3. Update the Action Menu ("Other games")
        # Ensure the .Practice-actions div has the dropdown
        # IMPROVEMENT: Search for Practice-actions in diagram-card first, then fallback to practice_view
        practice_actions = diagram_card.find('div', class_='Practice-actions')
        if not practice_actions:
             # Fallback: it might be a sibling if HTML structure got messed up
             practice_actions = practice_view.find('div', class_='Practice-actions')
             
        if practice_actions:
            # Check if it already has the Practices-menu
            menu = practice_actions.find('div', class_='Practices-menu')
            
            # If menu exists, remove it to ensure we have the latest version with all links
            if menu:
                menu.decompose()
            
            # Create the menu logic (Always create fresh)
            menu_html = '''
<div class="Practices-menu" style="position:relative; margin-right: 1rem;">
<button class="side-button view-other-Practices" onclick="togglePracticesPanel(this)" type="button">Other games</button>
<div aria-hidden="true" class="Practices-panel">
<div class="Practices-panel-item"><a href="#flashcard-game">Flashcard Game</a></div>
<div class="Practices-panel-item"><a href="#climb">Boost</a></div>
<div class="Practices-panel-item"><a href="#mixmatch">Mix & Match</a></div>
<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>
</div>
</div>
'''
            menu_soup = BeautifulSoup(menu_html, 'html.parser')
            # Insert at the beginning of practice_actions
            practice_actions.insert(0, menu_soup)

        # 4. Inject JavaScript
        body = soup.find('body')
        if body and components['js_logic']:
            # Check if script already injected
            # We can check if 'const mixMatchData' is already in the text of any script tag
            already_has_js = False
            for s in body.find_all('script'):
                if s.string and 'window.mixMatchData' in s.string: # using a more reliable unique string
                    already_has_js = True
                    break
            
            if not already_has_js:
                script_tag = soup.new_tag('script')
                script_tag.string = components['js_logic']
                body.append(script_tag)

        # 5. Inject CSS
        style_tag = soup.find('style')
        if style_tag and components.get('game_css'):
             if '.mix-match-board' not in style_tag.string:
                style_tag.string += "\n" + components['game_css']

        # Save
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Updated {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    # 1. Get Source Info
    components = load_source_components(SOURCE_FILE)
    
    if not components['mixmatch_html'] or not components['blockpuzzle_html'] or not components['js_logic']:
        print("Critical components missing from source. Aborting.")
        return

    # 2. Extract CSS Manually
    components['game_css'] = """
    /* Embedded Game Styles Swapped In */
    .Practices-menu {
      position: relative;
      display: inline-block;
    }
    .Practices-panel {
      position: absolute;
      bottom: 100%;
      right: 0;
      width: 12rem;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 0.75rem;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
      padding: 0.5rem;
      margin-bottom: 0.5rem;
      opacity: 0;
      visibility: hidden;
      transform: translateY(10px);
      transition: all 0.2s ease-out;
      z-index: 50;
    }
    .Practices-panel.is-open {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }
    body.dark-mode .Practices-panel {
      background: #1e293b;
      border-color: #334155;
    }
    .Practices-panel-item a {
      display: block;
      padding: 0.75rem 1rem;
      color: #334155;
      text-decoration: none;
      border-radius: 0.5rem;
      transition: background-color 0.15s;
    }
    .Practices-panel-item a:hover {
      background-color: #f1f5f9;
      color: #0f172a;
    }
    body.dark-mode .Practices-panel-item a {
      color: #cbd5e1;
    }
    body.dark-mode .Practices-panel-item a:hover {
      background-color: #334155;
      color: #f8fafc;
    }

    /* Mix & Match Styles */
    .mix-match-board {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
      width: 100%;
    }
    .mm-card {
      background: #f8fafc;
      border: 2px solid #e2e8f0;
      border-radius: 0.75rem;
      padding: 1.5rem;
      min-height: 100px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      cursor: pointer;
      font-weight: 500;
      color: #334155;
      transition: all 0.2s;
      user-select: none;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    body.dark-mode .mm-card {
      background: #1e293b;
      border-color: #334155;
      color: #cbd5e1;
    }
    .mm-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      border-color: #94a3b8;
    }
    .mm-card.selected {
      background: #eff6ff;
      border-color: #3b82f6;
      color: #1d4ed8;
      transform: scale(1.02);
      box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2);
    }
    body.dark-mode .mm-card.selected {
      background: #172554;
      border-color: #60a5fa;
      color: #bfdbfe;
    }
    .mm-card.matched {
      background: #f0fdf4;
      border-color: #22c55e;
      color: #15803d;
      opacity: 0.8;
      cursor: default;
    }
    body.dark-mode .mm-card.matched {
      background: #052e16;
      border-color: #22c55e;
      color: #86efac;
    }
    .mm-card.wrong {
      background: #fef2f2;
      border-color: #ef4444;
      animation: shake 0.5s;
    }
    body.dark-mode .mm-card.wrong {
      background: #450a0a;
      border-color: #ef4444;
    }
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      25% { transform: translateX(-5px); }
      75% { transform: translateX(5px); }
    }
    .mm-modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0,0,0,0.5);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 100;
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s;
    }
    .mm-modal.active {
      opacity: 1;
      visibility: visible;
    }
    .mm-modal-content {
      background: white;
      padding: 2rem;
      border-radius: 1rem;
      text-align: center;
      max-width: 90%;
      width: 400px;
      transform: scale(0.9);
      transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .mm-modal.active .mm-modal-content {
      transform: scale(1);
    }
    body.dark-mode .mm-modal-content {
      background: #1e293b;
      color: #ffffff;
    }

    /* Block Puzzle Styles */
    .block-puzzle-container {
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.5rem;
    }
    .bp-grid {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 2px;
      background: #cbd5e1;
      padding: 2px;
      border-radius: 0.5rem;
      width: 100%;
      aspect-ratio: 1;
    }
    body.dark-mode .bp-grid {
      background: #475569;
    }
    .bp-cell {
      background: #f1f5f9;
      border-radius: 2px;
      position: relative;
    }
    body.dark-mode .bp-cell {
      background: #334155;
    }
    .bp-cell.filled {
      background: #3b82f6; 
      box-shadow: inset 0 0 4px rgba(0,0,0,0.2);
    }
    .bp-blocks-area {
      display: flex;
      justify-content: center;
      gap: 2rem;
      min-height: 120px;
      width: 100%;
      padding: 1rem;
      background: rgba(241, 245, 249, 0.5);
      border-radius: 1rem;
    }
    body.dark-mode .bp-blocks-area {
      background: rgba(30, 41, 59, 0.5);
    }
    .bp-block-option {
      cursor: grab;
      transition: transform 0.2s;
    }
    .bp-block-option:active {
      cursor: grabbing;
      transform: scale(1.1);
    }
    .bp-preview {
      display: grid;
      gap: 2px;
      pointer-events: none;
    }
    .bp-preview-cell {
      width: 20px;
      height: 20px;
      border-radius: 2px;
    }
    """

    # 3. Iterate and Process
    for root_dir in TARGET_DIRS:
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.html') and ('Lesson' in file or 'Physics' in file) and file != 'Lesson 1.1 States_Of_Matter.html':
                    file_path = os.path.join(root, file)
                    process_file(file_path, components)

if __name__ == "__main__":
    main()
