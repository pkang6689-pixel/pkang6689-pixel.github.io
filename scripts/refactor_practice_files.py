import os
import re

def extract_flashcards_by_bracket_counting(content):
    start_marker = "const flashcards = ["
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return None
    
    # Start counting from the '[' character
    array_start_idx = content.find('[', start_idx)
    if array_start_idx == -1:
        return None

    depth = 0
    for i in range(array_start_idx, len(content)):
        char = content[i]
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            if depth == 0:
                # Found the closing bracket
                return content[array_start_idx : i+1]
    return None

def process_file(filepath):
    print(f"Processing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'src="../../scripts/practice_games.js"' in content:
        print("  Skipping: Already refactored.")
        return

    flashcards_json = extract_flashcards_by_bracket_counting(content)
    if not flashcards_json:
        print("  Skipping: Could not find flashcards definition.")
        return

    # Find where the game logic script starts
    found_any = False
    best_cutoff = len(content)
    
    # Looking for where the game logic was likely copy-pasted
    markers = [
        'window.togglePracticesPanel =',
        'window.initFlashcards ='
    ]
    
    for marker in markers:
        idx = content.find(marker)
        if idx != -1 and idx < best_cutoff:
            best_cutoff = idx
            found_any = True
            
    if not found_any:
        # Fallback: maybe just where initFlashcards is?
        idx = content.find('window.initFlashcards')
        if idx != -1:
            best_cutoff = idx
            found_any = True
        else:
            print("  Skipping: Could not find logic split point.")
            return

    # Backtrack to find the <script> start
    script_start_idx = content.rfind('<script', 0, best_cutoff)
    if script_start_idx == -1:
         print("  Skipping: Logic found but no preceding script tag??")
         return
    
    # Check if this script tag is very far away (meaning mismatched logic)
    # The logic is usually within the first few lines of the script block.
    if best_cutoff - script_start_idx > 500:
        # Maybe comments or whitespace? Or maybe we found the wrong script tag?
        # But usually it's fine.
        pass

    new_html = content[:script_start_idx].strip()
    
    script_block = f"""<!-- Game Logic & Data -->
<script>
    window.lessonFlashcards = {flashcards_json};
</script>
<script src="../../scripts/practice_games.js"></script>
</body>
</html>"""
    
    final_content = new_html + "\n\n" + script_block
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("  Success: File rewritten.")

def main():
    base_dir = '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/Unit1'
    if not os.path.exists(base_dir):
        print(f"Directory not found: {base_dir}")
        return

    for filename in sorted(os.listdir(base_dir)):
        if filename.endswith("Practice.html"):
            process_file(os.path.join(base_dir, filename))

if __name__ == "__main__":
    main()
