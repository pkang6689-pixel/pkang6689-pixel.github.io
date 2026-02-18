import json

def get_sample(n=100):
    with open('../filtered_flashcards_to_translate.json', 'r', encoding='utf-8') as f:
        terms = json.load(f)
        
    sample = terms[:n]
    
    with open('../flashcard_sample_to_translate.json', 'w', encoding='utf-8') as f:
        json.dump(sample, f, indent=2, ensure_ascii=False)
        
    print(f"Created sample of {len(sample)} terms to translate.")

if __name__ == '__main__':
    get_sample()
