import os
import re

def extract_values(root_dir):
    attributes = {
        "data-difficulty": set(),
        "data-detail": set(),
        "data-speed": set(),
        "data-pace": set()
    }
    rubric_found = False
    
    # Regex to find attributes and their values
    # Matches data-difficulty="Value" or data-difficulty='Value'
    attr_pattern = re.compile(r'(data-difficulty|data-detail|data-speed|data-pace)=["\']([^"\']*)["\']')
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        
                        # Search for attributes
                        matches = attr_pattern.findall(content)
                        for attr, value in matches:
                            attributes[attr].add(value)
                            
                        # Search for "Rubric"
                        if "Rubric" in content:
                            rubric_found = True
                            
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

    return attributes, rubric_found

if __name__ == "__main__":
    project_folder = "/workspaces/ArisEdu/ArisEdu Project Folder"
    unique_values, has_rubric = extract_values(project_folder)
    
    print("Unique Values Found:")
    for attr, values in unique_values.items():
        print(f"\n{attr}:")
        for val in sorted(values):
            print(f"  - {val}")
            
    print(f"\nWord 'Rubric' found in UI: {has_rubric}")
