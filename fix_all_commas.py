#!/usr/bin/env python3
"""Fix all missing commas in translation files"""

files_to_fix = {
    'ArisEdu Project Folder/scripts/global_translations.js': [
        34282,  # "Zeros and Roots"
        34247,  # "SOYBEANS" 
        35161,  # "η = (useful energy output..."
        35233   # " SPACE SHOOTER"
    ],
    'ArisEdu Project Folder/scripts/spanish_translations.js': [
        31338,  # "Zeros of Polynomials"
        32086,  # "SOYBEANS"
        32121,  # "Zeros and Roots"
        33070,  # "η = (useful energy output..."
        33749,  # "Ten"
        34059,  # "Yes, it is a degenerate..."
        34060   # "Back to Algebra 2"
    ],
    'ArisEdu Project Folder/scripts/hindi_translations.js': [
        31239,  # "Zeros of Polynomials"
        31987,  # "SOYBEANS"
        32022,  # "Zeros and Roots"
        32971,  # "η = (useful energy output..."
        33650,  # "Ten"
        33960,  # "Yes, it is a degenerate..."
        33961   # "Back to Algebra 2"
    ]
}

for filepath, line_numbers in files_to_fix.items():
    print(f'Processing {filepath}...')
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed = 0
    for line_no in sorted(line_numbers, reverse=True):
        idx = line_no - 1  
        if idx < len(lines):
            line = lines[idx]
            # If line ends with quote and no comma
            if line.rstrip().endswith('"') and not line.rstrip().endswith('",'):
                lines[idx] = line.rstrip() + ',\n'
                fixed += 1
                print(f'  Fixed line {line_no}')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f'  ✓ Fixed {fixed} lines\n')

print('✓ All files fixed!')
