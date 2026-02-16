
import json
import time
import random
from googletrans import Translator

INPUT_FILE = "scripts/quiz_strings_filtered.json"
OUTPUT_FILE = "scripts/quiz_translations_batch12_13.json"
START_INDEX = 2400
END_INDEX = 3400

def main():
    print(f"Reading from {INPUT_FILE}...")
    with open(INPUT_FILE, "r") as f:
        all_strings = json.load(f)
    
    # Extract batch
    batch_strings = all_strings[START_INDEX:END_INDEX]
    print(f"Extracted {len(batch_strings)} strings (Index {START_INDEX} to {END_INDEX}).")
    
    translator = Translator()
    translations = {}
    
    # Check if we can resume (if file exists)
    try:
        with open(OUTPUT_FILE, "r") as f:
            translations = json.load(f)
            print(f"Resuming with {len(translations)} existing translations...")
    except FileNotFoundError:
        pass
    
    start_time = time.time()
    for i, text in enumerate(batch_strings):
        if text in translations:
            continue
            
        retry_count = 0
        while retry_count < 3:
            try:
                # Use zh-cn for Simplified Chinese as per previous scripts
                result = translator.translate(text, dest='zh-cn')
                if result and result.text:
                    translations[text] = result.text
                    if (i + 1) % 10 == 0:
                        print(f"[{i+1}/{len(batch_strings)}] translated: {text[:20]}... -> {result.text[:20]}...")
                    break
                else:
                    raise Exception("Empty result")
            except Exception as e:
                print(f"Error on '{text}': {e}. Retry {retry_count+1}/3")
                retry_count += 1
                time.sleep(2 * retry_count) # Backoff
                if retry_count == 3:
                    print(f"Failed to translate '{text}' after 3 tries. Leaving original.")
                    # Optionally verify if we should save the original or skip
                    # translations[text] = text # Fallback to original?
        
        # Save progress periodically
        if (i + 1) % 50 == 0:
             with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
                json.dump(translations, f, indent=4, ensure_ascii=False)
    
    # Final save
    print("Saving final translations...")
    with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
        json.dump(translations, f, indent=4, ensure_ascii=False)
    print(f"Done. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
