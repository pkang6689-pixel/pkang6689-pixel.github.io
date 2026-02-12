import os
import re

SCRIPT_SRC = '<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>'

def optimize_game_scripts(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to remove the "Game Switcher Logic" block
        # It usually looks like <script>\n// Game Switcher Logic\n...contents...</script>
        # We need to be careful not to match too much.
        # But since we wrote it specifically, we can target the unique comment.
        
        # Pattern 1: Game Switcher Logic block
        pattern1 = re.compile(r'<script>\s*// Game Switcher Logic.*?</script>', re.DOTALL)
        
        # Pattern 2: Auto-initialize flashcards block
        pattern2 = re.compile(r'<script>\s*// Auto-initialize flashcards.*?</script>', re.DOTALL)
        
        new_content = content
        replaced = False
        
        if pattern1.search(content):
            new_content = pattern1.sub('', new_content)
            replaced = True
            
        if pattern2.search(content):
            new_content = pattern2.sub('', new_content)
            replaced = True
            
        if replaced:
            # Add the new script inclusion before </body>
            if SCRIPT_SRC not in new_content:
                new_content = new_content.replace('</body>', f'{SCRIPT_SRC}\n</body>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return False

def main():
    workspace_dir = 'ArisEdu Project Folder'
    count = 0
    
    for root, _, files in os.walk(workspace_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if optimize_game_scripts(filepath):
                    count += 1
                    # print(f"Optimized: {filepath}")
                    
    print(f"Optimized scripts in {count} HTML files.")

if __name__ == "__main__":
    main()
