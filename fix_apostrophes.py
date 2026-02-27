#!/usr/bin/env python3
"""Fix apostrophe mismatches and add remaining emoji-prefixed translations."""
import re

def fix_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_key, new_key in replacements:
        # Find and replace the key (preserving the value)
        pattern = re.escape(old_key)
        if pattern in content:
            # Already exists with straight apostrophe — replace key
            pass
        content = content.replace(f'"{old_key}"', f'"{new_key}"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# The curly apostrophe
CA = '\u2019'

# Keys that need curly apostrophe fix (straight -> curly)
# Format: (straight_version, curly_version)
apostrophe_fixes = [
    (f"Lesson 12.9: Cavalieri's Principle and Applications \u2b50", f"Lesson 12.9: Cavalieri{CA}s Principle and Applications \u2b50"),
    (f"10.9 \u2b50 Maxwell's Equations (introductory)", f"10.9 \u2b50 Maxwell{CA}s Equations (introductory)"),
    (f"6.6 \u2b50 Kepler's Laws", f"6.6 \u2b50 Kepler{CA}s Laws"),
    (f"7. Children's Privacy", f"7. Children{CA}s Privacy"),
]

# Add new entries that need to be added to each file
# Format: dict of {english_key: translated_value}
new_chinese = {
    f"7. Children{CA}s Privacy": "7. 儿童隐私",
    "\U0001f4ca Student Analytics": "\U0001f4ca 学生分析",
    "\U0001f40d SNAKE": "\U0001f40d 贪吃蛇",
    "\U0001f680 SPACE SHOOTER": "\U0001f680 太空射击",
}

new_spanish = {
    f"7. Children{CA}s Privacy": "7. Privacidad Infantil",
    "\U0001f4ca Student Analytics": "\U0001f4ca Análisis Estudiantil",
    "\U0001f40d SNAKE": "\U0001f40d SERPIENTE",
    "\U0001f680 SPACE SHOOTER": "\U0001f680 DISPAROS ESPACIALES",
}

new_hindi = {
    f"7. Children{CA}s Privacy": "7. बच्चों की गोपनीयता",
    "\U0001f4ca Student Analytics": "\U0001f4ca छात्र विश्लेषण",
    "\U0001f40d SNAKE": "\U0001f40d सांप",
    "\U0001f680 SPACE SHOOTER": "\U0001f680 अंतरिक्ष शूटर",
}

BASE = "ArisEdu Project Folder/scripts/"

# Fix apostrophes in all three files
for fname in ["global_translations.js", "spanish_translations.js", "hindi_translations.js"]:
    filepath = BASE + fname
    print(f"Fixing apostrophes in {fname}...")
    fix_file(filepath, apostrophe_fixes)

# Now add new entries with emoji prefixes
def add_entries(filepath, entries, marker):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    idx = content.rfind(marker)
    if idx == -1:
        print(f"  ERROR: marker not found in {filepath}")
        return
    
    # Find the line just before marker
    before = content[:idx].rstrip()
    # Add comma if last char is not comma
    if not before.endswith(','):
        before += ','
    
    lines = []
    for key, value in entries.items():
        k = key.replace('\\', '\\\\').replace('"', '\\"')
        v = value.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'    "{k}": "{v}"')
    
    injection = "\n" + ",\n".join(lines) + "\n"
    content = before + injection + content[idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  Added {len(entries)} entries to {filepath}")

print("\nAdding emoji entries...")
add_entries(BASE + "global_translations.js", new_chinese, "    };\n\n    // \u2500\u2500 Expose Chinese translations globally")
add_entries(BASE + "spanish_translations.js", new_spanish, "};\n\n    // Export to global scope\n    if (typeof spanishTranslations")
add_entries(BASE + "hindi_translations.js", new_hindi, "};\n\n    // Export to global scope\n    if (typeof hindiTranslations")

print("\nDone!")
