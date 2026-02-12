import os
import re

# Define the source file to extract CSS from
SOURCE_FILE = 'ArisEdu Project Folder/PhysicsLessons/Unit9/PhysicsLesson9.4OpticalInstruments.html'
OUTPUT_CSS = 'ArisEdu Project Folder/styles/main.css'

def normalize_css(css_content):
    """Normalize CSS by stripping whitespace around it."""
    return re.sub(r'\s+', ' ', css_content).strip()

def main():
    # 1. Read the source file
    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {SOURCE_FILE} not found.")
        return

    # 2. Extract the <style> block
    # We grab the *first* style block since it contains the massive copied CSS.
    match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not match:
        print(f"Error: No <style> block found in {SOURCE_FILE}.")
        return

    raw_css = match.group(1).strip()
    
    # 3. Create the output CSS file
    os.makedirs(os.path.dirname(OUTPUT_CSS), exist_ok=True)
    with open(OUTPUT_CSS, 'w', encoding='utf-8') as f:
        f.write(raw_css)
    print(f"Extracted CSS to {OUTPUT_CSS} ({len(raw_css.splitlines())} lines)")

    # 4. Scan and replace in all HTML files
    matches = 0
    workspace_dir = 'ArisEdu Project Folder'
    
    # Pre-calculate normalized first 200 chars for identification
    start_marker = normalize_css(raw_css)[:200]

    for root, _, files in os.walk(workspace_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    
                    # Find the first style block
                    file_match = re.search(r'<style>(.*?)</style>', file_content, re.DOTALL)
                    if file_match:
                        file_css = file_match.group(1)
                        norm_file_css = normalize_css(file_css)
                        
                        # Check if starts with the same ~200 chars
                        if norm_file_css.startswith(start_marker):
                            # It's a match! Replace the block.
                            # We replace the entire <style>...</style> block with <link ...>
                            # Logic needed: replace match.group(0) with replacement
                            
                            # However, re.sub might match multiple times. We only want the first one.
                            # Or specifically the one we matched.
                            
                            replacement = '<link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">'
                            # Adjust path for relative links? But "/ArisEdu Project Folder/styles/main.css" is root-relative for web server?
                            # Usually web servers serve from root.
                            # The script says href="/_sdk/element_sdk.js".
                            # Let's check where index.html is. "ArisEdu Project Folder/index.html" ? No.
                            # workspace structure says "ArisEdu Project Folder/" is inside "/workspaces/ArisEdu".
                            # The root folder has `files_with_board.txt`.
                            # `ArisEdu Project Folder` contains `algebra1.html`.
                            # If serving from `ArisEdu Project Folder`, the path should be `styles/main.css`.
                            # If serving from `/workspaces/ArisEdu`, it depends on the server root.
                            # Looking at context `index.html` is in `/workspaces/ArisEdu`.
                            # So `/ArisEdu Project Folder/styles/main.css` is correct absolute path.
                            
                            new_content = file_content.replace(file_match.group(0), replacement, 1)
                            
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            matches += 1
                            # print(f"Updated: {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    print(f"Updated {matches} HTML files.")

if __name__ == "__main__":
    main()
