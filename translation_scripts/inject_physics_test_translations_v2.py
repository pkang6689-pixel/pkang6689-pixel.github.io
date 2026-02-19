"""
Inject Simplified Chinese translations for all 11 Physics Unit Test pages
into global_translations.js. Traditional Chinese is handled at runtime by OpenCC.

Reads translations from physics_test_translations.json (clean JSON, no quoting issues).
"""
import os, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SCRIPT_DIR, 'physics_test_translations.json')
TRANSLATIONS_PATH = os.path.normpath(os.path.join(
    SCRIPT_DIR, '..', 'ArisEdu Project Folder', 'scripts', 'global_translations.js'
))


def build_translation_block(data):
    """Build the JS translation entries string from the JSON dict."""
    lines = []
    lines.append("")
    lines.append("  /* ═══════ Physics Unit Test Translations ═══════ */")
    for en, zh in data.items():
        escaped_en = en.replace('\\', '\\\\').replace('"', '\\"')
        escaped_zh = zh.replace('\\', '\\\\').replace('"', '\\"')
        lines.append(f'  "{escaped_en}": "{escaped_zh}",')
    return "\n".join(lines)


def main():
    # Load translations from JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} translation entries from JSON")

    # Read global_translations.js
    with open(TRANSLATIONS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already injected
    if "Physics Unit Test Translations" in content:
        print("Physics Unit Test translations already present — skipping.")
        return

    block = build_translation_block(data)

    # Insert before the closing }; of the translations object
    # The marker appears twice; we need the LAST occurrence (near the end)
    marker = '"Next Up: Practice": "\u4e0b\u4e00\u6b65: \u7ec3\u4e60",'
    last_idx = content.rfind(marker)
    if last_idx == -1:
        print("ERROR: Could not find insertion marker in global_translations.js")
        return

    insert_pos = last_idx + len(marker)
    content = content[:insert_pos] + "\n" + block + content[insert_pos:]

    with open(TRANSLATIONS_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    count = len(data)
    print(f"Successfully injected {count} physics unit test translations into global_translations.js")


if __name__ == '__main__':
    main()
