import os
import re

project_root = "../ArisEdu Project Folder"

def get_relative_path_to_scripts(file_path):
    # Calculate depth from project root
    rel_path = os.path.relpath(file_path, project_root)
    depth = rel_path.count(os.sep)
    if depth == 0:
        return "scripts/"
    return "../" * depth + "scripts/"

for root, dirs, files in os.walk(project_root):
    if 'Archive' in root or '_Templates' in root or '.git' in root or 'node_modules' in root:
        continue
        
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if already included
                if 'global_translations.js' in content:
                    continue
                
                print(f"Injecting global_translations.js into {file}")
                
                scripts_path = get_relative_path_to_scripts(file_path)
                script_tag = f'<script src="{scripts_path}global_translations.js?v=3.2"></script>\n'
                
                # Insert before </body>
                if '</body>' in content:
                    new_content = content.replace('</body>', script_tag + '</body>')
                else:
                    new_content = content + script_tag
                    
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
            except Exception as e:
                print(f"Error processing {file}: {e}")

print("Done injecting global_translations.js script tags.")
