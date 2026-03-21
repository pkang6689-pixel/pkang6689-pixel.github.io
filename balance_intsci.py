#!/usr/bin/env python3
"""
Post-process Integrated Science questions to balance option lengths.
Target: ~30-35% of questions should have correct answer as the longest option.
Strategy: For units with too-high rate, extend wrong answers.
         For units with too-low rate, extend correct answers.
"""
import json, os, random, re

random.seed(42)  # Reproducible

PATH = os.path.join("content_data", "integrated_science_lessons.json")
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

TARGET_LOW = 0.28
TARGET_HIGH = 0.38

# Phrases to naturally extend answer options
EXTEND_PHRASES = [
    " in this particular context",
    " under these specific conditions",
    " based on the available evidence",
    " when properly measured and analyzed",
    " as documented in the scientific literature",
    " within the relevant system boundaries",
    " during the time period in question",
    " according to well-established research",
    " given the conditions described here",
    " as observed across multiple studies",
]

# Filler words commonly found in verbose wrong answers - can be trimmed
TRIM_PATTERNS = [
    (r'\babsolutely ', ''),
    (r'\bcompletely ', ''),
    (r'\bwhatsoever\b', ''),
    (r'\bindefinitely\b', ''),
    (r'\bwithout any exception[s]?\b', ''),
    (r'\bin all possible circumstances\b', ''),
    (r'\bat all\b', ''),
    (r'\bever\b ', ''),
    (r'\bentirely\b ', ''),
    (r'\bexclusively ', ''),
    (r'\buniversally\b', ''),
    (r'\bwhatever\b', ''),
    (r'\bin every (?:possible |conceivable )?(?:situation|case|scenario|circumstance)\b', ''),
]

def get_longest_idx(opts):
    lens = [len(o["text"]) for o in opts]
    return lens.index(max(lens))

def get_correct_idx(opts):
    for i, o in enumerate(opts):
        if o["is_correct"]:
            return i
    return -1

def correct_is_longest(opts):
    ci = get_correct_idx(opts)
    li = get_longest_idx(opts)
    return ci == li

def extend_text(text, amount=1):
    """Add a natural phrase to extend text length."""
    phrase = random.choice(EXTEND_PHRASES)
    # Add before the last period if present, or at end
    text = text.rstrip()
    if text.endswith(('.', '!', '?')):
        return text
    return text + phrase

def trim_text(text):
    """Remove verbose filler words to shorten text."""
    result = text
    for pattern, replacement in TRIM_PATTERNS:
        result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
    # Clean up double spaces
    result = re.sub(r'  +', ' ', result).strip()
    return result

# Process each unit
units = {}
for key in sorted(data.keys()):
    if not key.startswith("u") or "_l" not in key:
        continue
    unit = key.split("_")[0]
    if unit not in units:
        units[unit] = []
    units[unit].append(key)

changes_made = 0

for unit in sorted(units.keys(), key=lambda x: int(x[1:])):
    lessons = units[unit]
    
    # Count current rate
    all_qs = []
    for lkey in lessons:
        for qi, q in enumerate(data[lkey].get("quiz_questions", [])):
            all_qs.append((lkey, qi, q))
    
    if not all_qs:
        continue
    
    longest_count = sum(1 for _, _, q in all_qs if correct_is_longest(q["options"]))
    rate = longest_count / len(all_qs)
    
    if TARGET_LOW <= rate <= TARGET_HIGH:
        print(f"{unit}: {rate:.0%} — already in target range, skipping")
        continue
    
    if rate > TARGET_HIGH:
        # Too many questions have correct as longest — need to make some wrongs longer
        target_longest = int(len(all_qs) * (TARGET_LOW + TARGET_HIGH) / 2)
        need_to_fix = longest_count - target_longest
        
        # Collect questions where correct IS longest
        fixable = [(lk, qi, q) for lk, qi, q in all_qs if correct_is_longest(q["options"])]
        random.shuffle(fixable)
        fixed = 0
        
        for lk, qi, q in fixable:
            if fixed >= need_to_fix:
                break
            opts = q["options"]
            ci = get_correct_idx(opts)
            # Find a wrong answer to extend
            wrong_indices = [i for i in range(len(opts)) if i != ci]
            # Pick the shortest wrong answer and extend it
            wrong_indices.sort(key=lambda i: len(opts[i]["text"]))
            target_idx = wrong_indices[0]
            
            old_len = len(opts[target_idx]["text"])
            correct_len = len(opts[ci]["text"])
            
            # Extend the wrong answer to be longer than correct
            new_text = opts[target_idx]["text"]
            attempts = 0
            while len(new_text) <= correct_len and attempts < 3:
                new_text = extend_text(new_text)
                attempts += 1
            
            if len(new_text) > correct_len:
                data[lk]["quiz_questions"][qi]["options"][target_idx]["text"] = new_text
                fixed += 1
                changes_made += 1
        
        new_longest = sum(1 for lk in lessons for q in data[lk].get("quiz_questions", []) 
                         if correct_is_longest(q["options"]))
        new_rate = new_longest / len(all_qs)
        print(f"{unit}: {rate:.0%} -> {new_rate:.0%} (fixed {fixed} questions, extended wrong answers)")
    
    else:
        # Too few questions have correct as longest — need to make some corrects longer
        target_longest = int(len(all_qs) * (TARGET_LOW + TARGET_HIGH) / 2)
        need_to_fix = target_longest - longest_count
        
        # Collect questions where correct is NOT longest
        fixable = [(lk, qi, q) for lk, qi, q in all_qs if not correct_is_longest(q["options"])]
        random.shuffle(fixable)
        fixed = 0
        
        for lk, qi, q in fixable:
            if fixed >= need_to_fix:
                break
            opts = q["options"]
            ci = get_correct_idx(opts)
            li = get_longest_idx(opts)
            
            longest_len = len(opts[li]["text"])
            correct_text = opts[ci]["text"]
            
            # First try trimming the longest wrong answer
            if li != ci:
                trimmed = trim_text(opts[li]["text"])
                # Also extend the correct
                extended_correct = extend_text(correct_text)
                
                if len(extended_correct) > len(trimmed):
                    data[lk]["quiz_questions"][qi]["options"][li]["text"] = trimmed
                    data[lk]["quiz_questions"][qi]["options"][ci]["text"] = extended_correct
                    fixed += 1
                    changes_made += 1
                elif len(extended_correct) > longest_len:
                    data[lk]["quiz_questions"][qi]["options"][ci]["text"] = extended_correct
                    fixed += 1
                    changes_made += 1
        
        new_longest = sum(1 for lk in lessons for q in data[lk].get("quiz_questions", []) 
                         if correct_is_longest(q["options"]))
        new_rate = new_longest / len(all_qs)
        print(f"{unit}: {rate:.0%} -> {new_rate:.0%} (fixed {fixed} questions, extended correct answers)")

# Save
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nTotal changes: {changes_made}")
print("\n--- Final audit ---")
for unit in sorted(units.keys(), key=lambda x: int(x[1:])):
    lessons = units[unit]
    total = 0
    longest = 0
    for lk in lessons:
        for q in data[lk].get("quiz_questions", []):
            total += 1
            if correct_is_longest(q["options"]):
                longest += 1
    print(f"{unit}: {longest}/{total} = {longest/total*100:.0f}%")
