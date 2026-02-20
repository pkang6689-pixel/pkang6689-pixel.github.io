import os
import re
import json

# Try importing BS4
try:
    from bs4 import BeautifulSoup, NavigableString
except ImportError:
    print("BeautifulSoup not found. Please install it with: pip install beautifulsoup4")
    exit(1)

# Paths
ROOT_DIR = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\BiologyLessons"
TRANSLATIONS_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"
OUTPUT_FILE = r"c:\Users\Peter\pkang6689-pixel.github.io\missing_summary_translations.json"

def get_existing_translations(filepath):
    """
    Extracts keys from global_translations.js using regex.
    This is approximate as the file is JS, not JSON.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    keys = set()
    # Simple strategy: line based if possible, or robust regex
    # The file has strict formatting: "Key": "Value",
    
    # Let's try to match lines first
    for line in content.splitlines():
        line = line.strip()
        if not line: continue
        # Match "Key": "Value",
        # Pattern: "(.+?)"\s*:\s*".*"
        # This regex is a bit simplistic, might miss escaped quotes in keys. But keys usually don't have quotes.
        match = re.search(r'"(.+?)"\s*:\s*"', line)
        if match:
            k = match.group(1)
            # Remove trailing colon from file path names or similar if erroneously matched? No, keys can contain colons.
            keys.add(k)
        
    return keys

def extract_text_from_file(filepath):
    texts = set()
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    # Focus on summary content
    # <div class="lesson-notes"> is the main container in summaries
    container = soup.find("div", class_="lesson-notes")
    if not container:
        # Fallback to main
        container = soup.find("main")
    
    if not container:
        return texts

    # recursive text extraction
    # We want individual text nodes because that's what the JS replaces
    for element in container.descendants:
        if isinstance(element, NavigableString):
            cleaned = element.string.strip()
            if cleaned and len(cleaned) > 1: # Ignore single chars like punctuation meant to be part of something else? strictly >1 might skip "A".
                # Check for just punctuation
                if not any(c.isalpha() for c in cleaned):
                    continue
                texts.add(cleaned)
    
    return texts

def main():
    print("Loading existing translations...")
    existing_keys = get_existing_translations(TRANSLATIONS_FILE)
    print(f"Found {len(existing_keys)} existing keys.")
    
    all_missing_texts = set()
    
    check_files = []
    print(f"Scanning directory: {ROOT_DIR}")
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith("_Summary.html"):
                check_files.append(os.path.join(root, file))
    
    print(f"Scanning {len(check_files)} summary files...")
    
    count = 0
    for fp in check_files:
        texts = extract_text_from_file(fp)
        for t in texts:
            if t not in existing_keys:
                all_missing_texts.add(t)
        count += 1
        if count % 10 == 0:
            print(f"Processed {count} files...")
    
    sorted_missing = sorted(list(all_missing_texts))
    
    print(f"Found {len(sorted_missing)} missing text fragments.")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted_missing, f, indent=4, ensure_ascii=False)
    
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
