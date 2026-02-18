import json
import re

def filter_flashcards():
    with open('../missing_flashcards.json', 'r', encoding='utf-8') as f:
        missing = json.load(f)
        
    filtered = []
    skipped = []
    
    for term in missing:
        # Filter out if length < 2 (single chars like 'A', '1')
        if len(term) < 2:
            skipped.append(term)
            continue
            
        # Filter out if it looks like a formula or number
        # e.g. "H2O", "1.5", "1.5 M"
        if not re.search(r'[a-zA-Z]{2,}', term): # Must have at least 2 consecutive letters? 
            # Risk: "pH" has 2 letters. "O2" has 1.
            # Maybe just check if it has ANY letters?
            if not re.search(r'[a-zA-Z]', term):
                 skipped.append(term)
                 continue
                 
        filtered.append(term)
        
    print(f"Original missing: {len(missing)}")
    print(f"Filtered (to translate): {len(filtered)}")
    print(f"Skipped: {len(skipped)}")
    
    with open('../filtered_flashcards_to_translate.json', 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    filter_flashcards()
