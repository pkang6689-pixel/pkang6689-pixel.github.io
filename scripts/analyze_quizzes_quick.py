import json
from collections import Counter

with open('/workspaces/ArisEdu/scripts/quiz_strings_en.json', 'r') as f:
    strings = json.load(f)

print(f"Total strings: {len(strings)}")

# Length analysis
lengths = [len(s) for s in strings]
print(f"Avg length: {sum(lengths)/len(lengths):.2f}")
print(f"Max length: {max(lengths)}")
print(f"Min length: {min(lengths)}")

# Prefixes (first word)
prefixes = [s.split()[0] if s.split() else "" for s in strings]
prefix_counts = Counter(prefixes)
print("\nMost common first words:")
for word, count in prefix_counts.most_common(20):
    print(f"{word}: {count}")

# Suffixes (last word)
suffixes = [s.split()[-1] if s.split() else "" for s in strings]
suffix_counts = Counter(suffixes)
print("\nMost common last words:")
for word, count in suffix_counts.most_common(20):
    print(f"{word}: {count}")
