import json
import os

def combine_results():
    all_translations = {}

    # Handle Batch 1 (Known dictionary)
    try:
        if os.path.exists('translation_result_1.json'):
            with open('translation_result_1.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict):
                    all_translations.update(data)
                    print(f"Batch 1: Added {len(data)} items (dict)")
                else:
                    print(f"Batch 1 Warning: Expected dict, got {type(data)}")
        else:
            print("Batch 1 file not found.")
    except Exception as e:
        print(f"Error Batch 1: {e}")

    # Handle Batches 2-6
    for i in range(2, 7):
        b_file = f'translation_batch_{i}.json'
        r_file = f'translation_result_{i}.json'
        
        if not os.path.exists(b_file) or not os.path.exists(r_file):
            print(f"Skipping Batch {i} (files missing)")
            continue

        try:
            with open(b_file, 'r', encoding='utf-8') as f:
                source = json.load(f)
            with open(r_file, 'r', encoding='utf-8') as f:
                target = json.load(f)

            if len(source) == len(target):
                # Zip them
                batch_dict = dict(zip(source, target))
                all_translations.update(batch_dict)
                print(f"Batch {i}: Added {len(batch_dict)} items (list zip)")
            else:
                print(f"Batch {i} Error: Length mismatch {len(source)} vs {len(target)}")

        except Exception as e:
            print(f"Batch {i} Exception: {e}")

    print(f"Total translations collected: {len(all_translations)}")
    
    with open('combined_flashcard_translations.json', 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    combine_results()
