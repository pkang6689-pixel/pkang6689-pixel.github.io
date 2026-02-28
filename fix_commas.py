#!/usr/bin/env python3
"""Fix missing commas in translation files"""

files = {
    'ArisEdu Project Folder/scripts/global_translations.js': [
        (33497, 'Zeros of Polynomials'),
        (34247, 'SOYBEANS'),
        (34282, 'Zeros and Roots'),
        (35161, 'useful energy'),
        (35233, 'SPACE SHOOTER')
    ],
    'ArisEdu Project Folder/scripts/spanish_translations.js': [
        (31338, 'Zeros of Polynomials'),
        (32086, 'SOYBEANS'),
        (32121, 'Zeros and Roots'),
        (33070, 'useful energy'),
        (33749, 'Ten'),
        (34059, 'degenerate triangle'),
        (34060, 'Back to Algebra 2')
    ],
    'ArisEdu Project Folder/scripts/hindi_translations.js': [
        (31239, 'Zeros of Polynomials'),
        (31987, 'SOYBEANS'),
        (32022, 'Zeros and Roots'),
        (32971, 'useful energy'),
        (33650, 'Ten'),
        (33960, 'degenerate triangle'),
        (33961, 'Back to Algebra 2')
    ]
}

for filepath, line_infos in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line_no, key_search in line_infos:
        idx = line_no - 1
        if idx < len(lines):
            line = lines[idx]
            if line.rstrip().endswith('"') and not line.rstrip().endswith('",'):
                lines[idx] = line.rstrip() + ',\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f'✓ Fixed {filepath.split("/")[-1]}')

print('✓ All translation files fixed!')
