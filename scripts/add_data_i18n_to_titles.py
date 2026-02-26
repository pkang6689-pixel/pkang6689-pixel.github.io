import os
import re

def fix_lesson_titles():
    # Directories to scan
    # Algebra 1, 2, Geometry, Biology, Chemistry, Physics
    base_dirs = [
        "Algebra1Lessons", "Algebra2Lessons", "GeometryLessons",
        "BiologyLessons", "ChemistryLessons", "PhysicsLessons"
    ]
    
    root_path = "ArisEdu Project Folder"
    
    title_pattern = re.compile(r'<h2 class="page-title">(.*?)</h2>')
    
    files_processed = 0
    files_fixed = 0
    
    for course_dir in base_dirs:
        full_path = os.path.join(root_path, course_dir)
        if not os.path.exists(full_path):
            continue
            
        for root, dirs, files in os.walk(full_path):
            for file in files:
                if file.endswith(".html"):
                    file_path = os.path.join(root, file)
                    
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                        
                        # Find title
                        match = title_pattern.search(content)
                        if match:
                            original_tag = match.group(0)
                            title_text = match.group(1).strip()
                            
                            # Skip if already has data-i18n
                            if "data-i18n" in original_tag:
                                continue
                                
                            # Create new tag with data-i18n
                            # We escape quotes in the title just in case
                            safe_title = title_text.replace('"', '&quot;')
                            new_tag = f'<h2 class="page-title" data-i18n="{safe_title}">{title_text}</h2>'
                            
                            new_content = content.replace(original_tag, new_tag)
                            
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(new_content)
                            
                            files_fixed += 1
                        
                        files_processed += 1
                        
                    except Exception as e:
                        print(f"Error processing {file_path}: {e}")

    print(f"Processed {files_processed} files.")
    print(f"Updated {files_fixed} titles with data-i18n.")

if __name__ == "__main__":
    fix_lesson_titles()
