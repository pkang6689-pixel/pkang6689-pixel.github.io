import os
import glob
from bs4 import BeautifulSoup
import re

def extract_definitions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    definitions = []
    # Find li tags with b tag inside followed by text starting with :
    for li in soup.find_all('li'):
        b = li.find('b')
        if b:
            key = b.get_text(strip=True)
            # Check sibling text
            sibling_text = ''
            for sibling in b.next_siblings:
                if isinstance(sibling, str):
                    sibling_text += sibling
                else:
                    sibling_text += sibling.get_text()
            
            sibling_text = sibling_text.strip()
            if sibling_text.startswith(':'):
                definitions.append((key, sibling_text))
                
    return definitions

def main():
    root_dir = '../ArisEdu Project Folder'
    summary_files = glob.glob(os.path.join(root_dir, '**/*_Summary.html'), recursive=True)
    
    all_defs = []
    for file_path in summary_files:
        defs = extract_definitions(file_path)
        all_defs.extend(defs)
    
    # Print distinct definitions
    seen = set()
    print("Found definitions:")
    for k, v in all_defs:
        if v not in seen:
            print(f"Key: {k} || Value: {v}")
            seen.add(v)

if __name__ == "__main__":
    main()
