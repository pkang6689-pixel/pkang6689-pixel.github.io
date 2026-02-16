import json
import re

def filter_strings(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        strings = json.load(f)

    filtered_strings = []
    
    # Regex for strings consisting only of numbers, symbols, and whitespace
    # Using \W (non-word char) and \d (digit) and _ (underscore)covers most symbols.
    # However, we need to be careful. Is "H2O" a symbol? No, it has letters.
    # So basically if it has NO letters (a-z, A-Z), it should be filtered?
    # "1,000" -> No letters.
    # "1/10" -> No letters.
    # "+1" -> No letters.
    # "1 m" -> "m" is a letter. Should be kept.
    # "1 cm" -> "cm" letters.
    # "1%" -> No letters.
    # So logical rule: Must contain at least one letter [a-zA-Z].
    
    letter_regex = re.compile(r'[a-zA-Z]')
    
    for s in strings:
        # Check criteria 2: Length < 2
        if len(s) < 2:
            continue
            
        # Check criteria 1: Consist only of numbers, symbols, whitespace
        # Equivalent to: Does NOT contain any letters?
        if not letter_regex.search(s):
            continue
            
        filtered_strings.append(s)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_strings, f, indent=4)
        
    print(f"Original count: {len(strings)}")
    print(f"Filtered count: {len(filtered_strings)}")
    
    # Print first 100 for translation
    print("---FIRST 100---")
    print(json.dumps(filtered_strings[:100], indent=4))

if __name__ == "__main__":
    filter_strings('scripts/quiz_strings_en.json', 'scripts/quiz_strings_filtered.json')
