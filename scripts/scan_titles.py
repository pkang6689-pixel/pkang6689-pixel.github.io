import os
import re

def extract_from_chem_html(filepath):
    found_titles = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract from showLessonPopup
            matches = re.findall(r"onmouseenter=\"showLessonPopup\(event, '([^']+)'\)\"", content)
            found_titles.update(matches)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return found_titles

def extract_from_lesson_files(root_dir):
    found_titles = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Only scan if it looks like a lesson file (contains title/h1/h2)
                        title_found = False
                        
                        # Priority 1: h1
                        h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.IGNORECASE | re.DOTALL)
                        if h1_match:
                            title_text = h1_match.group(1).strip()
                            # Remove tags if any inside h1
                            title_text = re.sub(r'<[^>]+>', '', title_text)
                            if title_text:
                                found_titles.add(title_text)
                                title_found = True
                        
                        # Priority 2: h2 with class page-title
                        if not title_found:
                            h2_match = re.search(r"<h2[^>]*class=[\"'][^\"']*page-title[^\"']*[\"'][^>]*>(.*?)</h2>", content, re.IGNORECASE | re.DOTALL)
                            if h2_match:
                                title_text = h2_match.group(1).strip()
                                title_text = re.sub(r'<[^>]+>', '', title_text)
                                if title_text:
                                    found_titles.add(title_text)
                                    title_found = True
                        
                        # Priority 3: title tag
                        if not title_found:
                            title_tag_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
                            if title_tag_match:
                                title_text = title_tag_match.group(1).strip()
                                if title_text:
                                    found_titles.add(title_text)
                                    title_found = True

                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
    return found_titles

def main():
    root_dir = "/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons"
    chem_html_path = "/workspaces/ArisEdu/ArisEdu Project Folder/chem.html"
    
    # 1. Scan chem.html
    chem_titles = extract_from_chem_html(chem_html_path)
    print(f"Found {len(chem_titles)} titles in chem.html")
    
    # 2. Scan lesson files
    lesson_titles = extract_from_lesson_files(root_dir)
    print(f"Found {len(lesson_titles)} titles in lesson files (including h1/h2/title)")
    
    # 3. Combine and print
    all_titles = sorted(list(chem_titles.union(lesson_titles)))
    
    print("\n--- Unique Titles Found ---")
    for title in all_titles:
        print(title)

if __name__ == "__main__":
    main()
