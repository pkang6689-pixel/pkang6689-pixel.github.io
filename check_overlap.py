import json
import re
import os

def check_overlap_and_report():
    if not os.path.exists('extracted_flashcards.json'):
        print("extracted_flashcards.json not found.")
        return

    with open('extracted_flashcards.json', 'r', encoding='utf-8') as f:
        flashcards = json.load(f)

    global_trans_path = '/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js'

    if not os.path.exists(global_trans_path):
        print(f"{global_trans_path} not found.")
        return

    with open(global_trans_path, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content)
    if not match:
        print("Could not find translations object in global_translations.js.")
        return

    raw_js = match.group(1)
    
    # Extract keys: "Key": or 'Key': or Key:
    # We'll assume quoted keys for simplicity as they are translations.
    # We can use a simpler regex if we assume consistent formatting.
    existing_keys = set(re.findall(r'["\'](.*?)["\']\s*:', raw_js))
    
    overlap = 0
    missing = []
    
    for term in flashcards:
        if term in existing_keys:
            overlap += 1
        else:
            missing.append(term)
            
    print(f"Total unique flashcard terms: {len(flashcards)}")
    print(f"Already translated: {overlap}")
    print(f"Missing (need translation): {len(missing)}")
    
    with open('missing_flashcards.json', 'w', encoding='utf-8') as f:
        json.dump(missing, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    check_overlap_and_report()
