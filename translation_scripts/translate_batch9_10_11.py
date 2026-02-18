
import json
import time
import random
from googletrans import Translator

INPUT_FILE = "../scripts/quiz_strings_filtered.json"
OUTPUT_FILE = "../scripts/quiz_translations_batch9_10_11.json"

def main():
    print(f"Reading from {INPUT_FILE}...")
    with open(INPUT_FILE, "r") as f:
        all_strings = json.load(f)
    
    # Extract batch 1500 to 2400
    batch_strings = all_strings[1500:2400]
    print(f"Extracted {len(batch_strings)} strings.")
    
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
                result = translator.translate(text, dest='zh-cn')
                if result and result.text:
                    translations[text] = result.text
                    # print(f"[{i+1}/{len(batch_strings)}] translated: {result.text}")
                    break
                else:
                    raise Exception("Empty result")
            except Exception as e:
                # print(f"Error on '{text}': {e}. Retry {retry_count+1}/3")
                retry_count += 1
                time.sleep(1 * retry_count) # Backoff
                if retry_count == 3:
                    print(f"Failed to translate '{text}' after 3 tries. Leaving original.")
                    translations[text] = text

        # Small delay
        time.sleep(0.1 + random.random() * 0.1) # randomize delay a bit
        
        if (i+1) % 50 == 0:
            print(f"Processed {i+1} / {len(batch_strings)} items...")
            # Incremental save
            with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
                json.dump(translations, f, indent=2, ensure_ascii=False)

    print(f"Saving final {len(translations)} translations to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
        json.dump(translations, f, indent=2, ensure_ascii=False)
    
    print("Done.")

if __name__ == "__main__":
    main()
