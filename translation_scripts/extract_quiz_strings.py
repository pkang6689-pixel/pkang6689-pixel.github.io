import os
import json
import re
from bs4 import BeautifulSoup

def extract():
    root_dir = "../ArisEdu Project Folder"
    quiz_files = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith("_Quiz.html"):
                quiz_files.append(os.path.join(dirpath, filename))
    
    unique_questions = set()
    unique_answers = set()
    
    for file_path in quiz_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                
            questions = soup.find_all("div", class_="quiz-question")
            for q in questions:
                # Question text
                p_tag = q.find("p")
                if p_tag:
                    raw_text = p_tag.get_text(strip=True)
                    # Strip "1. ", "5. " prefix
                    match = re.match(r"^\d+\.\s*(.*)$", raw_text)
                    if match:
                        q_text = match.group(1).strip()
                    else:
                        q_text = raw_text
                    
                    if q_text:
                        unique_questions.add(q_text)
                
                # Answer text
                labels = q.find_all("label")
                for label in labels:
                    # Remove input element from soup copy just for text extraction?
                    # Or manually iterate contents.
                    text_parts = []
                    for content in label.contents:
                        if content.name == "input":
                            continue 
                        if isinstance(content, str):
                            text_parts.append(content.strip())
                        else:
                            text_parts.append(content.get_text(strip=True))
                    
                    full_text = " ".join(filter(None, text_parts)).strip()
                    if full_text:
                        unique_answers.add(full_text)
                        
        except Exception as e:
            pass # Ignore errors for now
            
    # Filter numeric only answers
    filtered_answers = []
    for a in unique_answers:
        # Keep if it contains letters. "5.0 g" matches. "5" doesn't.
        if re.search(r'[a-zA-Z]', a):
            filtered_answers.append(a)
    
    print(f"Found {len(unique_questions)} unique questions.")
    print(f"Found {len(filtered_answers)} unique text-based answers (from {len(unique_answers)} total).")
    
    data = {
        "questions": sorted(list(unique_questions)),
        "answers": sorted(filtered_answers)
    }
    
    with open("../quiz_dataset.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    extract()
