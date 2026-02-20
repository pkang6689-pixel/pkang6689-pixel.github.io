import json
import re

# Load remaining strings
with open('quiz_strings_remaining.json', 'r', encoding='utf-8') as f:
    remaining = json.load(f)

# Load existing translations to look up topics
existing_translations = {}
# Rough parsing of global_translations.js to get a lookup dict
with open('ArisEdu Project Folder/scripts/global_translations.js', 'r', encoding='utf-8') as f:
    content = f.read()
    # Extract "key": "value"
    matches = re.findall(r'"((?:[^"\\]|\\.)+)"\s*:\s*"((?:[^"\\]|\\.)+)"', content)
    for k, v in matches:
        k_clean = k.encode('utf-8').decode('unicode_escape')
        v_clean = v.encode('utf-8').decode('unicode_escape')
        existing_translations[k_clean] = v_clean

# Patterns
# Note: "Select the definition of: " has a trailing space in regex or text?
# Let's be lenient with whitespace around colon
patterns = [
    (r"How does (.+) affect living organisms\?", "{}如何影响生物？"),
    (r"How is (.+) best described\?", "{}最好被描述为？"),
    (r"Select the definition of:\s*(.+)", "选择{}的定义：")
]

print(f"Loaded {len(existing_translations)} existing translations.")
if "Animal behavior" in existing_translations:
    print("Found 'Animal behavior' in existing translations.")
else:
    print("Did NOT find 'Animal behavior' in existing translations.")

generated_translations = {}
topics_missing = set()
processed_indices = []

for i, text in enumerate(remaining):
    matched = False
    for pat, template in patterns:
        m = re.match(pat, text, re.IGNORECASE)
        if m:
            topic = m.group(1).strip() # Strip extra spaces from captured group
            # Try to find topic translation
            candidates = [topic, topic.lower(), topic.capitalize(), topic.title()]
            trans = None
            for c in candidates:
                if c in existing_translations:
                    trans = existing_translations[c]
                    break
            
            if trans:
                generated_translations[text] = template.format(trans)
                processed_indices.append(i)
                matched = True
            else:
                topics_missing.add(topic)
            break # Stop after first pattern match

print(f"Generated {len(generated_translations)} translations automatically.")
print(f"Missing topics: {len(topics_missing)}")
# Save missing topics to see if I need to translate them
with open('missing_topics.json', 'w', encoding='utf-8') as f:
    json.dump(sorted(list(topics_missing)), f, indent=4)

# Create script to inject these
with open('generated_quiz_translations.json', 'w', encoding='utf-8') as f:
    json.dump(generated_translations, f, indent=4, ensure_ascii=False)
