import json
import re
import os

# Configuration
GLOBAL_TRANS_PATH = "ArisEdu Project Folder/scripts/global_translations.js"
REMAINING_WH_PATH = "remaining_wh_strings.json"
OUTPUT_PATH = "generated_quiz_translations_batch6.json"

def load_topic_map(file_path):
    topic_map = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to capture "Understanding concepts in [Topic]": "[Translation]"
        matches = re.finditer(r'"Understanding concepts in (.*?)":\s*"(.*?)"', content)
        count = 0 
        for match in matches:
            topic = match.group(1).lower().replace('\\"', '"')
            translation = match.group(2).replace('\\"', '"')
            
            # Extract Chinese topic: "理解[Topic]的概念" -> "[Topic]"
            if translation.startswith("理解") and translation.endswith("的概念"):
                chinese_topic = translation[2:-3]
                topic_map[topic] = chinese_topic
            else:
                # If not matching "Understanding...concept", check if it's a valid string.
                # Just skip or use full string?
                pass
            count += 1
        print(f"Loaded {len(topic_map)} valid topics from {count} matches.")
    except Exception as e:
        print(f"Error reading global_translations.js: {e}")
    return topic_map

def main():
    topic_map = load_topic_map(GLOBAL_TRANS_PATH)
    
    if not os.path.exists(REMAINING_WH_PATH):
        print(f"{REMAINING_WH_PATH} not found.")
        return

    with open(REMAINING_WH_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translations = {}
    
    # Process "which"
    for s in data.get("which", []):
        if "Which succession is faster?" in s:
             translations[s] = "哪種演替速度更快？"
             continue
        
        # Pattern: Which field of science studies [Topic]?
        m = re.match(r"^Which field of science studies (.*?)\?$", s)
        if m:
            topic = m.group(1).lower()
            if topic in topic_map:
                translations[s] = f"哪個科學領域研究{topic_map[topic]}？"
            else:
                print(f"Warning: Topic '{topic}' not found in map for '{s}'")
        else:
            print(f"Warning: Unmatched 'Which': {s}")

    # Process "why"
    for s in data.get("why", []):
        # Pattern: Why do biologists study [Topic]?
        m = re.match(r"^Why do biologists study (.*?)\?$", s)
        if m:
             topic = m.group(1).lower()
             if topic in topic_map:
                 translations[s] = f"為什麼生物學家要研究{topic_map[topic]}？"
             else:
                 print(f"Warning: Topic '{topic}' not found in map for '{s}'")
        else:
             print(f"Warning: Unmatched 'Why': {s}")

    # Process "misc"
    misc_map = {
        "W": "W",
        "Wildlife biologists study:": "野生動物生物學家研究：",
        "Water cycle": "水循環",
        "Wildlife biologist": "野生動物生物學家",
        "Where it lives": "它居住在哪裡",
        "Water flow": "水流",
        "Weather prediction": "天氣預測",
        "Wild animals": "野生動物"
    }
    
    for s in data.get("misc", []):
        if s in misc_map:
            translations[s] = misc_map[s]
        else:
            print(f"Warning: No translation for misc: {s}")

    # Save
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(translations, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(translations)} translations in {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
