import os
import glob
from bs4 import BeautifulSoup
from collections import Counter

def extract_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    texts = []
    
    # Target specific semantic tags common in summaries
    for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'li', 'b', 'strong', 'a']):
        text = tag.get_text(strip=True)
        if text and len(text) > 1: # Ignore single chars
            texts.append(text)
            
    return texts

def main():
    root_dir = os.path.join(os.path.dirname(__file__), '..', 'ArisEdu Project Folder')
    summary_files = glob.glob(os.path.join(root_dir, '**/*_Summary.html'), recursive=True)
    
    all_texts = []
    for file_path in summary_files:
        all_texts.extend(extract_text_from_html(file_path))
        
    counter = Counter(all_texts)
    
    # Print most common phrases to identify headers/UI elements
    print("Top 50 most common phrases in summaries:")
    for text, count in counter.most_common(50):
        print(f"{count}: {text}")

if __name__ == "__main__":
    main()
