#!/usr/bin/env python3
"""
Fix quiz giveaway questions where the correct answer is obviously the longest option.
Expands wrong answers to be similar in length to correct answers using context-aware
expansion with natural-sounding academic phrases and domain keywords.
"""

import json
import os
import re
import hashlib
import glob

BASE_DIR = "c:/Users/Peter/pkang6689-pixel.github.io/content_data"

THRESHOLD = 3.0
TARGET_RATIO = 0.50   # Each wrong answer should be >= 50% of correct length
MAX_RATIO = 0.92      # Don't exceed 92% of correct length

STOP_WORDS = {
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'can', 'shall', 'to', 'of', 'in', 'for',
    'on', 'with', 'at', 'by', 'from', 'as', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'between', 'out', 'off', 'over',
    'under', 'again', 'further', 'then', 'once', 'that', 'this', 'these',
    'those', 'which', 'what', 'who', 'whom', 'when', 'where', 'why', 'how',
    'all', 'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    'just', 'because', 'but', 'and', 'or', 'if', 'while', 'about', 'up',
    'down', 'it', 'its', 'they', 'their', 'them', 'he', 'she', 'his', 'her',
    'we', 'our', 'you', 'your', 'my', 'me', 'also', 'like', 'well',
    'still', 'many', 'much', 'get', 'gets', 'got', 'make', 'makes', 'made',
    'one', 'two', 'three', 'new', 'use', 'used', 'using', 'way', 'need',
    'needs', 'take', 'takes', 'know', 'say', 'says', 'said', 'tell',
    'told', 'see', 'seen', 'come', 'comes', 'came', 'give', 'gives',
    'given', 'think', 'thought', 'look', 'looks', 'want', 'wants',
    'tend', 'tends', 'refer', 'refers', 'called', 'often', 'typically',
    'generally', 'means', 'meaning', 'example', 'involves', 'include',
    'including', 'includes', 'based', 'help', 'helps', 'different',
    'following', 'rather', 'within', 'among', 'across', 'related',
}

DANGLING_ENDINGS = {
    'the', 'a', 'an', 'and', 'or', 'of', 'in', 'for', 'to', 'with',
    'by', 'at', 'from', 'on', 'into', 'through', 'between', 'over',
    'broader', 'overall', 'related', 'significant', 'important',
    'relevant', 'various', 'multiple', 'different', 'consistent',
    'lasting', 'measurable', 'predictable', 'considerable', 'notable',
}

ADJECTIVE_LIKE = {
    'cultural', 'economic', 'political', 'social', 'financial',
    'monetary', 'fiscal', 'commercial', 'physical', 'natural',
    'religious', 'ethnic', 'industrial', 'agricultural', 'urban',
    'rural', 'domestic', 'international', 'global', 'regional',
    'local', 'federal', 'national', 'institutional', 'historical',
    'traditional', 'conventional', 'structural', 'demographic',
    'geographic', 'spatial', 'hierarchical', 'contagious',
    'behavioral', 'ecological', 'biological', 'geological',
    'environmental', 'theoretical', 'practical', 'functional',
}


def find_all_quiz_files():
    """Dynamically find ALL quiz JSON files across both course directories."""
    ap_files = glob.glob(os.path.join(BASE_DIR, 'APLessons', '**', '*_Quiz.json'), recursive=True)
    fm_files = glob.glob(os.path.join(BASE_DIR, 'FinancialMathLessons', '**', '*_Quiz.json'), recursive=True)
    all_files = sorted(ap_files + fm_files)
    return [os.path.relpath(f, BASE_DIR).replace('\\', '/') for f in all_files]


def extract_keywords(text, n=8):
    """Extract meaningful keywords from text, preserving capitalization for proper nouns
    and deduplicating singular/plural forms. Uses sentence-position-aware capitalization
    detection to correctly handle words like 'Roman' that appear both mid-sentence and
    at sentence starts."""
    # Split text into sentences for position-aware analysis
    sentences = re.split(r'[.!?]\s+', text)

    freq = {}
    cap_count = {}       # capitalized in non-sentence-start position
    total_nonsent = {}   # total in non-sentence-start position
    any_cap = {}         # any capitalized occurrence at all (including sentence-start)

    for sentence in sentences:
        words = re.findall(r'[a-zA-Z]+', sentence)
        for i, w in enumerate(words):
            lower = w.lower()
            if lower not in STOP_WORDS and len(lower) > 3:
                freq[lower] = freq.get(lower, 0) + 1
                # Track capitalization: is this word at the start of a sentence?
                if i > 0:
                    # Non-sentence-start position: reliable for proper noun detection
                    total_nonsent[lower] = total_nonsent.get(lower, 0) + 1
                    if w[0].isupper():
                        cap_count[lower] = cap_count.get(lower, 0) + 1
                # Track any capitalization (even sentence-start) as fallback
                if w[0].isupper():
                    any_cap[lower] = any_cap.get(lower, 0) + 1

    # Deduplicate singular/plural
    to_remove = set()
    sorted_keys = sorted(freq.keys())
    for k in sorted_keys:
        for suffix in ['s', 'es']:
            plural = k + suffix
            if plural in freq and plural not in to_remove:
                if freq[k] >= freq[plural]:
                    to_remove.add(plural)
                else:
                    to_remove.add(k)
            if k.endswith(suffix):
                base = k[:-len(suffix)]
                if base in freq and base not in to_remove and k not in to_remove:
                    if freq[base] >= freq[k]:
                        to_remove.add(k)
                    else:
                        to_remove.add(base)

    for r in to_remove:
        del freq[r]

    # Sort by frequency
    sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Build result, preserving capitalization for likely proper nouns
    result = []
    for word, _ in sorted_words[:n]:
        ns_total = total_nonsent.get(word, 0)
        ns_caps = cap_count.get(word, 0)

        if ns_total >= 1 and ns_caps >= ns_total * 0.5:
            # Appears capitalized in mid-sentence positions -> proper noun
            result.append(word.capitalize())
        elif ns_total == 0 and any_cap.get(word, 0) >= 2:
            # Only appeared at sentence starts but always capitalized with 2+ occurrences
            # Likely a proper noun (e.g., "Roman" starting multiple sentences)
            result.append(word.capitalize())
        else:
            result.append(word)

    # Pad with fallbacks if needed
    fallbacks = ['overall', 'fundamental', 'standard', 'primary', 'general',
                 'typical', 'broader', 'underlying', 'practical', 'relevant']
    while len(result) < 6:
        for fb in fallbacks:
            if fb not in result:
                result.append(fb)
                if len(result) >= 6:
                    break
    return result


def make_seed(question_text, wrong_text, option_index):
    """Generate a deterministic seed for consistent variety."""
    key = f"{question_text}|{wrong_text}|{option_index}"
    h = hashlib.md5(key.encode()).hexdigest()
    return int(h[:8], 16)


def trim_to_word_boundary(text, max_len, min_len):
    """Trim text to max_len at a word boundary, avoiding dangling adjectives/prepositions."""
    if len(text) <= max_len:
        return text
    trimmed = text[:max_len]
    last_space = trimmed.rfind(' ')
    if last_space > min_len:
        trimmed = trimmed[:last_space]
    words = trimmed.rsplit(' ', 1)
    if len(words) == 2 and words[1].lower().rstrip('.,:;') in DANGLING_ENDINGS:
        candidate = words[0]
        if len(candidate) > min_len:
            return candidate
    return trimmed


def get_templates(keywords, needed):
    """Get expansion templates appropriate for the needed character count."""
    kw = keywords
    k1, k2, k3, k4, k5 = kw[0], kw[1], kw[2], kw[3], kw[4]

    short_templates = [
        f", particularly in the context of {k1}",
        f", especially during periods of significant change",
        f" regardless of prevailing conditions in practice",
        f" under most circumstances involving {k1}",
        f", at least according to standard theory",
        f" in most scenarios involving {k1} factors",
        f" when considering all relevant {k1} factors",
        f", based on conventional assumptions about {k1}",
        f", even when conditions shift significantly",
        f" within the broader context of {k1} analysis",
        f", as conventional {k1} theory would suggest",
        f" without accounting for additional influences",
        f", despite what intuition might initially suggest",
        f" according to widely held views on this topic",
        f", which is a common assumption in the field",
        f" when viewed through a simplified analytical lens",
    ]

    medium_templates = [
        f", since the relevant {k1} factors typically produce this outcome in practice",
        f" because conventional analysis of {k1} suggests this would be the expected result",
        f", as the dynamics involved tend to push conditions in this direction over time",
        f" when the interaction between {k1} and {k2} factors is taken into full account",
        f", particularly when {k1} considerations are weighed against competing pressures",
        f" due to the well-established relationship between {k1} trends and broader outcomes",
        f", which is consistent with how {k1} mechanisms are understood to operate in theory",
        f" given that prevailing {k1} conditions tend to reinforce this particular trajectory",
        f", since standard models of {k1} behavior predict this outcome under normal conditions",
        f" because the underlying forces at work tend to produce exactly this type of outcome",
        f", as most introductory frameworks would predict when analyzing {k1} dynamics",
        f" considering that the key variables involved tend to move in this direction together",
        f", although this interpretation oversimplifies the actual {k1} mechanisms at work",
        f" based on the conventional understanding of how {k1} processes interact in practice",
        f", which represents a common but incomplete view of how these {k1} dynamics operate",
        f", since the prevailing theory about {k1} would support this particular interpretation",
    ]

    long_templates = [
        f", primarily because the key {k1} forces at work tend to drive outcomes in this direction rather than others",
        f" as a result of how the dynamics of {k1} interact with {k2} factors to produce measurable and consistent effects",
        f", since the patterns governing {k1} behavior generally combine with {k2} conditions to create this type of result",
        f" because the underlying {k1} mechanisms produce effects that consistently shape outcomes in this direction over time",
        f", given that the pressures related to {k1} and {k2} tend to work together in reinforcing this particular trajectory",
        f" due to the way that {k1} variables and related {k2} indicators affect conditions across different time periods",
        f", which reflects how the principles of {k1} and {k2} jointly determine behavioral patterns in real applications",
        f" when the {k1} conditions align with {k2} trends and related pressures within the broader analytical framework",
        f", as the combined effect of {k1} dynamics and {k2} changes creates predictable patterns that point in this direction",
        f" because both theoretical frameworks and empirical evidence suggest that {k1} outcomes follow consistent trajectories",
        f", since developments in {k1} typically cascade through {k2} channels to reshape conditions in exactly this manner",
        f" given that the interplay between {k1} forces and related {k2} mechanisms determines behavior over extended periods",
    ]

    very_long_templates = [
        f", primarily because the key {k1} forces at work tend to drive {k2} outcomes in this direction, creating lasting effects that compound across the broader landscape",
        f" as a result of how the dynamics of {k1} interact with {k2} factors to produce {k3} effects that build through multiple channels over extended periods of time",
        f", since the interplay between {k1} patterns and {k2} conditions creates outcomes that persist through {k3} cycles in most practical situations and real-world contexts",
        f" because the underlying {k1} mechanisms produce {k2} effects that shape broader outcomes and reinforce {k3} trends across many different scenarios and time horizons",
        f", given that {k1} pressures working alongside {k2} influences create patterns that interact with {k3} factors to determine overall results in practice and over time",
        f" due to the complex relationship between {k1} variables and {k2} indicators, which affects {k3} conditions and broader patterns over sustained periods of observation",
        f", reflecting how the principles of {k1} combine with {k2} dynamics and {k3} factors to shape outcomes in most real-world applications and observed situations broadly",
        f" when {k1} conditions align with {k2} trends and {k3} pressures, creating compounding effects that influence the overall trajectory in significant and measurable ways",
        f", as the combined influence of {k1} shifts, {k2} adjustments, and {k3} responses produces movement patterns that are difficult to reverse once they become established",
        f" because {k1} theory, {k2} evidence, and {k3} data all point to outcomes that follow consistent and reinforcing trajectories under comparable conditions over time",
        f", since {k1} developments typically cascade through {k2} and {k3} channels, reshaping conditions in ways that persist well beyond the initial triggering event itself",
        f" given that the complex interplay between {k1} forces, {k2} mechanisms, and {k3} constraints determines behavior in most observed real-world circumstances and contexts",
    ]

    if needed < 35:
        return short_templates
    elif needed < 65:
        return medium_templates
    elif needed < 100:
        return long_templates
    else:
        return very_long_templates


def expand_wrong_answer(wrong_text, correct_text, question_text, explanation, option_index):
    """Expand a wrong answer to reduce length disparity with the correct answer."""
    target_len = int(len(correct_text) * TARGET_RATIO)

    if len(wrong_text) >= target_len:
        return wrong_text

    needed = target_len - len(wrong_text)
    context = question_text + " " + explanation
    keywords = extract_keywords(context)
    seed = make_seed(question_text, wrong_text, option_index)
    templates = get_templates(keywords, needed)

    # Use seed + option_index offset to prevent collisions within the same question
    template = templates[(seed + option_index * 5) % len(templates)]

    base = wrong_text.rstrip('.,:;')
    expanded = base + template

    max_len = int(len(correct_text) * MAX_RATIO)
    if len(expanded) > max_len:
        expanded = trim_to_word_boundary(expanded, max_len, len(wrong_text))

    # Fix dangling adjective endings
    last_word = expanded.rsplit(' ', 1)[-1].lower().rstrip('.,:;')
    if last_word in ADJECTIVE_LIKE:
        completion_nouns = ['dynamics', 'factors', 'processes', 'patterns',
                           'conditions', 'developments']
        expanded = expanded + " " + completion_nouns[seed % len(completion_nouns)]
        if len(expanded) > max_len:
            expanded = trim_to_word_boundary(expanded, max_len, len(wrong_text))

    # If still below target, add a secondary phrase
    if len(expanded) < target_len:
        secondary = [
            " and related considerations",
            " in broader terms",
            " across different contexts",
            " under these conditions",
            " over extended periods",
            " in practical scenarios",
        ]
        expanded = expanded + secondary[seed % len(secondary)]
        if len(expanded) > max_len:
            expanded = trim_to_word_boundary(expanded, max_len, len(wrong_text))

    return expanded


def is_flagged(question):
    """Check if a question has the giveaway pattern (correct >= 3x avg wrong)."""
    correct_text = None
    wrong_texts = []
    for opt in question['options']:
        if opt['is_correct']:
            correct_text = opt['text']
        else:
            wrong_texts.append(opt['text'])

    if not correct_text or not wrong_texts:
        return False

    avg_wrong_len = sum(len(w) for w in wrong_texts) / len(wrong_texts)
    if avg_wrong_len == 0:
        return True

    return len(correct_text) / avg_wrong_len >= THRESHOLD


def fix_question(question):
    """Fix a flagged question by expanding its wrong answers."""
    correct_text = None
    for opt in question['options']:
        if opt['is_correct']:
            correct_text = opt['text']
            break

    if not correct_text:
        return False

    question_text = question.get('question_text', '')
    explanation = question.get('explanation', '')

    changed = False
    wrong_idx = 0
    for opt in question['options']:
        if not opt['is_correct']:
            new_text = expand_wrong_answer(
                opt['text'], correct_text, question_text, explanation, wrong_idx
            )
            if new_text != opt['text']:
                opt['text'] = new_text
                changed = True
            wrong_idx += 1

    return changed


def process_file(filepath):
    """Process a single quiz file, fixing flagged questions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions_fixed = 0
    for q in data['quiz_questions']:
        if is_flagged(q):
            if fix_question(q):
                questions_fixed += 1

    if questions_fixed > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')

    return questions_fixed


def verify_file(filepath):
    """Verify a file has no more flagged questions."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    still_flagged = 0
    for q in data['quiz_questions']:
        if is_flagged(q):
            still_flagged += 1

    return still_flagged


def main():
    FILES = find_all_quiz_files()

    total_fixed = 0
    total_still_flagged = 0
    total_before = 0

    print("=" * 70)
    print("FIXING QUIZ GIVEAWAY QUESTIONS")
    print(f"Threshold: correct/avg_wrong >= {THRESHOLD}")
    print(f"Target: each wrong answer >= {TARGET_RATIO*100:.0f}% of correct length")
    print(f"Quiz files found: {len(FILES)}")
    print("=" * 70)

    for rel_path in FILES:
        filepath = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        before_count = sum(1 for q in data['quiz_questions'] if is_flagged(q))
        total_before += before_count

        if before_count == 0:
            continue  # Skip clean files for cleaner output

        fixed = process_file(filepath)
        total_fixed += fixed

        still_flagged = verify_file(filepath)
        total_still_flagged += still_flagged

        status = "CLEAN" if still_flagged == 0 else f"!! {still_flagged} REMAINING !!"
        print(f"  {rel_path}: {before_count} flagged -> {fixed} fixed -> {status}")

    print()
    print("=" * 70)
    print(f"SUMMARY")
    print(f"  Files scanned: {len(FILES)}")
    print(f"  Questions flagged before: {total_before}")
    print(f"  Questions fixed: {total_fixed}")
    print(f"  Still flagged: {total_still_flagged}")
    print("=" * 70)


if __name__ == '__main__':
    main()
