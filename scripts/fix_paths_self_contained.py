
import os
import re

def update_global_translations_paths(root_dir, script_path):
    # Matches script src referencing global_translations.js with optional version query
    script_pattern = re.compile(r'<script\s+src=["\']([^"\']*global_translations\.js)(?:\?v=[^"\']*)?["\']\s*></script>', re.IGNORECASE)

    updated_files = 0
    script_path = os.path.abspath(script_path)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html"):
                filepath = os.path.join(dirpath, filename)
                
                # Calculate relative path from this file's directory to the script actual location
                # script_path is /workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js
                rel_path_to_script = os.path.relpath(script_path, dirpath)
                
                # Normalize path separators for URL (always forward slash)
                new_src = rel_path_to_script.replace("\\", "/")
                
                # Add version query
                new_src_with_version = f"{new_src}?v=3.2"

                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    if "global_translations.js" in content:
                        
                        # Replace the script tag with the new relative path version
                        new_tag = f'<script src="{new_src_with_version}"></script>'
                        
                        new_content = script_pattern.sub(new_tag, content)
                        
                        if new_content != content:
                            with open(filepath, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            updated_files += 1
                            print(f"Updated: {filepath} -> {new_src_with_version}")

                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

    print(f"Total files updated: {updated_files}")

if __name__ == "__main__":
    target_dir = "/workspaces/ArisEdu/ArisEdu Project Folder"
    # New location of the script
    script_location = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"
    
    update_global_translations_paths(target_dir, script_location)
