"""
Merge all physics lesson translation JSONs (unit1-11, summary_U1-U6, quiz batches, batch1)
and inject into global_translations.js.

Handles deduplication and avoids re-injecting existing entries.
"""
import json, glob, os, re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
GT_PATH = os.path.join(ROOT, "ArisEdu Project Folder", "scripts", "global_translations.js")

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"  WARNING: Could not load {path}: {e}")
        return {}

def get_existing_keys(content):
    """Extract all existing translation keys from JS content."""
    keys = set()
    for m in re.finditer(r'"([^"\\]*(?:\\.[^"\\]*)*)"\s*:', content):
        keys.add(m.group(1))
    return keys

def main():
    # Collect ALL translation sources
    all_translations = {}
    
    # 1. Unit quiz+flashcard translations (unit1-11)
    for f in sorted(glob.glob(os.path.join(SCRIPT_DIR, "unit*_translations.json"))):
        data = load_json(f)
        print(f"Loaded {os.path.basename(f)}: {len(data)} entries")
        all_translations.update(data)
    
    # 2. Summary translations (summary_U1-U6)
    for f in sorted(glob.glob(os.path.join(SCRIPT_DIR, "summary_U*_translations.json"))):
        data = load_json(f)
        print(f"Loaded {os.path.basename(f)}: {len(data)} entries")
        all_translations.update(data)
    
    # 3. Quiz batch translations
    for f in sorted(glob.glob(os.path.join(SCRIPT_DIR, "quiz_translations_batch*.json"))):
        data = load_json(f)
        print(f"Loaded {os.path.basename(f)}: {len(data)} entries")
        all_translations.update(data)
    
    # 4. batch1_translations.json
    b1_path = os.path.join(SCRIPT_DIR, "batch1_translations.json")
    if os.path.exists(b1_path):
        data = load_json(b1_path)
        print(f"Loaded batch1_translations.json: {len(data)} entries")
        all_translations.update(data)
    
    # 5. missing_translations.json (summary fragments for U7-U11 + remaining)
    missing_path = os.path.join(SCRIPT_DIR, "missing_translations.json")
    if os.path.exists(missing_path):
        data = load_json(missing_path)
        print(f"Loaded missing_translations.json: {len(data)} entries")
        all_translations.update(data)
    
    print(f"\nTotal merged translations: {len(all_translations)}")
    
    # Read global_translations.js
    with open(GT_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Get existing keys
    existing_keys = get_existing_keys(content)
    print(f"Existing keys in global_translations.js: {len(existing_keys)}")
    
    # Filter out already-present entries
    new_translations = {}
    for k, v in all_translations.items():
        if k not in existing_keys:
            new_translations[k] = v
    
    print(f"New entries to inject: {len(new_translations)}")
    
    if not new_translations:
        print("Nothing new to inject!")
        return
    
    # Check for marker
    if "Physics Lesson Content Translations" in content:
        print("Physics Lesson Content translations block already exists — will append to it.")
        # Find end of existing block and append
        marker = "/* ═══════ Physics Lesson Content Translations ═══════ */"
        idx = content.index(marker) + len(marker)
        # Build new entries
        lines = []
        for en, zh in sorted(new_translations.items()):
            escaped_en = en.replace('\\', '\\\\').replace('"', '\\"')
            escaped_zh = zh.replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'  "{escaped_en}": "{escaped_zh}",')
        block = "\n" + "\n".join(lines)
        content = content[:idx] + block + content[idx:]
    else:
        # Build the full block
        lines = []
        lines.append("")
        lines.append("  /* ═══════ Physics Lesson Content Translations ═══════ */")
        for en, zh in sorted(new_translations.items()):
            escaped_en = en.replace('\\', '\\\\').replace('"', '\\"')
            escaped_zh = zh.replace('\\', '\\\\').replace('"', '\\"')
            lines.append(f'  "{escaped_en}": "{escaped_zh}",')
        block = "\n".join(lines)
        
        # Find insertion point — after Physics Unit Test block or before };
        if "Physics Unit Test Translations" in content:
            # Find the dictionary closing }; — it's the first one that appears
            # at the start of a line (the translations dict close)
            closing = content.find("\n};")
            if closing == -1:
                print("ERROR: Could not find closing }; in global_translations.js")
                return
            content = content[:closing] + "\n" + block + content[closing:]
        else:
            # Fallback: insert before first };
            closing = content.find("\n};")
            if closing == -1:
                print("ERROR: Could not find closing }; in global_translations.js")
                return
            content = content[:closing] + "\n" + block + content[closing:]
    
    with open(GT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"\nSuccessfully injected {len(new_translations)} physics lesson content translations!")

if __name__ == "__main__":
    main()
