import os
import re

def fix_physics_links():
    root_dir = os.path.join("ArisEdu Project Folder", "PhysicsLessons")
    
    print(f"Scanning directory: {root_dir}")
    
    processed_count = 0
    fixed_count = 0
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # Regex to find links like 'Lesson2.2_Summary.html' (missing space)
                    # We want to replace it with 'Lesson 2.2_Summary.html' (with space)
                    # Pattern: href="Lesson(\d+\.\d+)_Summary.html"
                    
                    new_content = re.sub(
                        r'href="Lesson(\d+\.\d+)_Summary.html"',
                        r'href="Lesson \1_Summary.html"',
                        content
                    )
                    
                    # Also check for Practice links if they are broken similarly
                    new_content = re.sub(
                        r'href="Lesson(\d+\.\d+)_Practice.html"',
                        r'href="Lesson \1_Practice.html"',
                        new_content
                    )

                    # Also check for Quiz links
                    new_content = re.sub(
                        r'href="Lesson(\d+\.\d+)_Quiz.html"',
                        r'href="Lesson \1_Quiz.html"',
                        new_content
                    )
                    
                    if new_content != content:
                        print(f"Fixing file: {file_path}")
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        fixed_count += 1
                        
                    processed_count += 1
                    
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    print(f"Processed {processed_count} files.")
    print(f"Fixed {fixed_count} files.")

if __name__ == "__main__":
    fix_physics_links()
