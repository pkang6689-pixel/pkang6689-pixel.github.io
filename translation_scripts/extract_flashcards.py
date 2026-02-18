import os
import re
import json

ROOT_DIR = '../ArisEdu Project Folder'

def main():
    flashcard_data = [] # List of {question: ..., answer: ...}
    
    # Regex to find window.lessonFlashcards = [{...}];
    # We find the array content first
    array_pattern = re.compile(r'window\.lessonFlashcards\s*=\s*\[(.*?)\];', re.DOTALL)
    
    # Regex to find objects inside the array: { question: "...", answer: "..." }
    # Handles both ' and " quotes
    object_pattern = re.compile(r'\{\s*question:\s*["\'](.*?)["\'],\s*answer:\s*["\'](.*?)["\']\s*\}', re.DOTALL)
    
    count_files = 0
    total_cards = 0

    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                match = array_pattern.search(content)
                if match:
                    array_content = match.group(1)
                    pairs = object_pattern.findall(array_content)
                    if pairs:
                        count_files += 1
                        total_cards += len(pairs)
                        for q, a in pairs:
                            flashcard_data.append({'question': q, 'answer': a})

    print(f"Found {total_cards} flashcards across {count_files} files.")
    
    # Extract unique terms
    unique_terms = set()
    for item in flashcard_data:
        unique_terms.add(item['question'])
        unique_terms.add(item['answer'])
        
    sorted_terms = sorted(list(unique_terms))
    print(f"Unique terms to translate: {len(sorted_terms)}")
    
    with open('../extracted_flashcards.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_terms, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
