#!/usr/bin/env python3
"""Fix quiz giveaway questions where the correct answer is obviously the longest option.

Strategy:
1. FIRST remove parentheticals from correct answers (before any em-dash handling)
2. Then handle em-dash content
3. Expand wrong answers with topic-appropriate qualifying clauses
4. Never truncate original wrong answer text
5. Check for unmatched parentheses in all candidates
"""

import json
import re
import os


def has_unmatched_parens(text):
    """Return True if text has unmatched parentheses."""
    depth = 0
    for ch in text:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        if depth < 0:
            return True
    return depth != 0


def trim_correct(text, avg_wrong_len):
    """Trim correct answer. Prefers result within [0.8x, 2.8x] of avg_wrong."""
    ok_len = avg_wrong_len * 2.8
    min_len = avg_wrong_len * 0.8

    if len(text) <= ok_len:
        return text

    original = text
    candidates = []

    # ========== PHASE 1: Remove parentheticals first (before em-dash handling) ==========
    # This avoids the bug where em-dashes inside parentheticals break the structure.

    # Strategy 1a: Remove long parentheticals (>25 chars inside) from original
    s1a = re.sub(r'\s*\([^)]{25,}\)', '', original)
    s1a = re.sub(r'\s+', ' ', s1a).strip()
    if not has_unmatched_parens(s1a):
        candidates.append(s1a)

    # Strategy 1b: Remove ALL parentheticals from original
    s1b = re.sub(r'\s*\([^)]+\)', '', original)
    s1b = re.sub(r'\s+', ' ', s1b).strip()
    if not has_unmatched_parens(s1b) and s1b != s1a:
        candidates.append(s1b)

    # ========== PHASE 2: Handle em-dashes (applied to phase 1 results + original) ==========

    elaborative_starts = [
        'named by', 'first described', 'identified by', 'coined by',
        'developed by', 'proposed by', 'published by', 'one of the',
        'a term ', 'a concept ', 'a principle', 'higher values',
        'making it', 'and it is', 'this means', 'this is',
    ]

    # Apply em-dash handling to each base text (original, s1a, s1b)
    bases = [('orig', original), ('s1a', s1a), ('s1b', s1b)]
    for label, base in bases:
        # Find em-dash NOT inside parentheses
        dash_pos = -1
        paren_depth = 0
        for i, ch in enumerate(base):
            if ch == '(':
                paren_depth += 1
            elif ch == ')':
                paren_depth -= 1
            elif ch == '\u2014' and paren_depth == 0:
                dash_pos = i
                break

        if dash_pos < 0:
            continue

        # Find the actual dash string (with surrounding spaces)
        start = dash_pos
        end = dash_pos + 1
        if start > 0 and base[start - 1] == ' ':
            start -= 1
        if end < len(base) and base[end] == ' ':
            end += 1
        dash_str = base[start:end]

        before = base[:start].strip().rstrip(',;:')
        after = base[end:].strip()

        is_elab = any(after.lower().startswith(s) for s in elaborative_starts)

        # Strategy 2a: Remove elaborative dash content
        if is_elab:
            c = before
            if not has_unmatched_parens(c) and len(c) >= min_len:
                candidates.append(c)

        # Strategy 2b: Replace dash with comma (keep essential content)
        if not is_elab:
            c = before + ', ' + after
            c = re.sub(r'\s+', ' ', c).strip()
            if not has_unmatched_parens(c):
                candidates.append(c)

            # Strategy 2b2: Replace dash with comma, then remove long parens
            c2 = re.sub(r'\s*\([^)]{25,}\)', '', c)
            c2 = re.sub(r'\s+', ' ', c2).strip()
            if not has_unmatched_parens(c2) and c2 != c:
                candidates.append(c2)

            # Strategy 2b3: Replace dash with comma, then remove ALL parens
            c3 = re.sub(r'\s*\([^)]+\)', '', c)
            c3 = re.sub(r'\s+', ' ', c3).strip()
            if not has_unmatched_parens(c3) and c3 != c2:
                candidates.append(c3)

        # Strategy 2c: Remove dash content entirely (more aggressive)
        if len(before) >= min_len and not has_unmatched_parens(before):
            candidates.append(before)

    # ========== PHASE 3: Additional trimming strategies on candidates ==========

    extra_candidates = []
    for c in candidates:
        # Remove "such as [list]"
        c2 = re.sub(r',?\s+such as\s+[^;]+$', '', c, flags=re.IGNORECASE)
        c2 = c2.rstrip(',;: ').strip()
        if c2 != c and not has_unmatched_parens(c2) and len(c2) >= min_len:
            extra_candidates.append(c2)

        # Remove causal phrases
        for phrase in ['due to ', 'because of ', 'because ', 'resulting from ',
                       'owing to ', 'as a result of ']:
            idx = c.lower().find(phrase)
            if idx > 30:
                c3 = c[:idx].rstrip(',;: ').strip()
                if not has_unmatched_parens(c3) and len(c3) >= min_len:
                    extra_candidates.append(c3)
                break

        # Remove trailing semicolon clauses
        if '; ' in c and len(c) > ok_len:
            clauses = c.split('; ')
            while len('; '.join(clauses)) > ok_len and len(clauses) > 1:
                clauses.pop()
            c4 = '; '.join(clauses)
            if not has_unmatched_parens(c4) and len(c4) >= min_len:
                extra_candidates.append(c4)

        # Remove trailing "and" clause
        if ', and ' in c and len(c) > ok_len:
            c5 = c[:c.rfind(', and ')].rstrip(',;: ').strip()
            if not has_unmatched_parens(c5) and len(c5) >= min_len:
                extra_candidates.append(c5)

    candidates.extend(extra_candidates)

    # ========== PHASE 4: Select the best candidate ==========
    # Deduplicate
    seen = set()
    unique = []
    for c in candidates:
        if c not in seen and c != original:
            seen.add(c)
            unique.append(c)

    if not unique:
        return text  # No trimming possible

    # Prefer the longest candidate under ok_len and above min_len
    valid_under = [c for c in unique if min_len <= len(c) <= ok_len]
    if valid_under:
        return max(valid_under, key=len)

    # If nothing fits in range, pick closest to ok_len from above
    above = [c for c in unique if len(c) > ok_len]
    if above:
        return min(above, key=len)

    # Everything is below min_len; pick longest
    below = [c for c in unique if len(c) > 0]
    if below:
        return max(below, key=len)

    return text


# ========== Expansion system ==========

EXPANSION_POOLS = {
    'genetic': [
        ", as determined through molecular analysis of DNA sequence variation and allele frequency distributions across sampled populations",
        ", measured by comparing heritable allelic variation among individuals within geographically defined breeding populations over generations",
        ", involving comprehensive analysis of genomic markers and heritable phenotypic variation within and between natural populations",
    ],
    'species': [
        ", as documented through systematic field surveys and standardized population sampling methods across representative habitat types",
        ", based on comprehensive taxonomic inventories and ecological census data collected across geographically distinct survey regions",
        ", enumerated through standardized biodiversity sampling protocols that account for detection probability and spatial habitat variation",
    ],
    'ecosystem': [
        ", encompassing the full range of biotic communities, physical environments, and ecological processes that operate within the system",
        ", as characterized by systematic surveys of habitat structure, species composition, and the range of ecological interactions present",
        ", including variation in physical structure, nutrient cycling pathways, energy flow patterns, and characteristic disturbance regimes",
    ],
    'climate': [
        ", as driven by long-term patterns in solar radiation, atmospheric circulation, precipitation, and seasonal temperature variation",
        ", shaped by regional patterns in temperature, precipitation, prevailing winds, and the interactions between ocean and atmosphere",
        ", influenced by geographic position, prevailing wind and ocean current patterns, topographic effects, and seasonal climatic shifts",
    ],
    'conserv': [
        ", with specific management protocols for maintaining viable populations of native species and the ecological processes they depend on",
        ", managed according to science-based conservation guidelines and internationally recognized biodiversity protection targets and protocols",
        ", designed to maintain viable native species populations and the ecological processes that sustain natural community structure long-term",
    ],
    'evolut': [
        ", driven by the interacting mechanisms of mutation, genetic drift, gene flow, and natural selection operating across many generations",
        ", through processes of adaptation, reproductive isolation, and differential survival that operate over extensive evolutionary time",
        ", shaped by selective pressures including predation, interspecific competition, and environmental variability over geological timescales",
    ],
    'area': [
        ", as predicted by mathematical models relating habitat extent to the number of species that can be sustainably supported over time",
        ", based on empirical observations showing that larger habitat patches consistently harbor greater numbers of species across regions",
        ", a quantitative relationship documented through systematic surveys of habitats varying in size across multiple biogeographic regions",
    ],
    'diversity_index': [
        ", which weights each species contribution by its proportional abundance in the sample using logarithmic transformation of count data",
        ", incorporating data on the number of distinct taxa present and the statistical distribution of individual abundances among those taxa",
        ", derived from information theory to quantify the uncertainty in predicting the species identity of a randomly selected individual",
    ],
    'island': [
        ", based on the equilibrium model of species immigration from source populations and local extinction rates on isolated habitat patches",
        ", predicting that isolation distance and habitat area jointly determine the balance between colonization and local species extinction",
        ", supported by empirical studies of species turnover rates on islands varying in size and distance from continental source populations",
    ],
    'food_web': [
        ", determined by the network of trophic interactions and energy transfer pathways connecting primary producers to top-level consumers",
        ", as quantified by measuring standing biomass, energy assimilation rates, and population turnover across all trophic levels present",
        ", reflecting the organism's functional position in the hierarchy of predator-prey relationships and its role in ecosystem energy flow",
    ],
    'water': [
        ", involving the dynamics of freshwater and marine systems as they interact with terrestrial habitats and the organisms that inhabit them",
        ", encompassing the flow of water through atmospheric, surface, and subsurface pathways and its effects on living systems in the region",
        ", as regulated by precipitation patterns, watershed characteristics, and the biological processes that influence the local water cycle",
    ],
    'cell': [
        ", involving the coordinated activity of organelles, enzymes, and signaling pathways that regulate cellular function and reproduction",
        ", as governed by the molecular machinery of gene expression, protein synthesis, and intracellular transport within living cells overall",
        ", through the action of specific biochemical pathways and regulatory mechanisms that maintain cellular homeostasis and normal growth",
    ],
    'default': [
        ", a concept that has been extensively studied and documented in ecological and evolutionary research across diverse biological systems",
        ", as demonstrated through systematic observation and analysis conducted across a wide range of natural ecosystems and taxonomic groups",
        ", which has been well-documented through controlled experimental studies and long-term ecological monitoring programs across many regions",
    ],
}

SHORT_EXPANSIONS = [
    " across diverse biological systems and environmental contexts",
    " based on established principles of ecology and evolutionary biology",
    " as characterized by current ecological and evolutionary research",
]

CATEGORY_KEYWORDS = [
    ('diversity_index', ['index', 'shannon', 'simpson', 'diversity metric', "h'", 'formula', 'equation']),
    ('island', ['island', 'biogeograph', 'immigration', 'coloniz', 'mainland']),
    ('food_web', ['food web', 'food chain', 'trophic', 'predator', 'prey', 'body mass', 'biomass', 'consumer']),
    ('cell', ['cell division', 'dna replication', 'mitosis', 'meiosis', 'organelle', 'protein synth', 'enzyme']),
    ('water', ['aquatic', 'marine', 'freshwater', 'ocean floor', 'river', 'lake ecosystem']),
    ('genetic', ['genetic', 'dna', 'allel', 'genom', 'heritable', 'inbreeding', 'gene ', 'mutation', 'genotype']),
    ('evolut', ['evolut', 'speciat', 'natural selection', 'adapt', 'extinct', 'fossil', 'phylogen']),
    ('conserv', ['conserv', 'protect', 'reserve', 'park', 'endangered', 'iucn', 'wildlife', 'threatened']),
    ('area', [' area', ' km', 'square', 'hectare', 'habitat size', 'land surface']),
    ('climate', ['climate', 'temperature', 'rainfall', 'precipitation', 'warm', 'cold', 'weather', 'season']),
    ('ecosystem', ['ecosystem', 'habitat', 'environment', 'biome', 'communit', 'landscape']),
    ('species', ['species', 'organism', 'population', 'abundance', 'taxonom', 'biodiversity']),
]


def detect_category(text, question_text=''):
    combined = (text + ' ' + question_text).lower()
    for cat, keywords in CATEGORY_KEYWORDS:
        if any(kw in combined for kw in keywords):
            return cat
    return 'default'


def has_word_overlap(original_text, expansion):
    orig_words = set(w.lower().rstrip('.,;:') for w in original_text.split() if len(w) > 4)
    exp_words = [w.lower().rstrip('.,;:') for w in expansion.lstrip(', ').split()[:4] if len(w) > 4]
    return any(w in orig_words for w in exp_words)


def expand_wrong(text, target_len, wrong_idx=0, question_text=''):
    """Expand wrong answer to approximately match target length."""
    if len(text) >= target_len * 0.75:
        return text

    category = detect_category(text, question_text)
    pool = EXPANSION_POOLS.get(category, EXPANSION_POOLS['default'])

    expansion = pool[wrong_idx % len(pool)]

    # Avoid word overlap
    if has_word_overlap(text, expansion):
        for alt_idx in range(len(pool)):
            alt = pool[(wrong_idx + alt_idx + 1) % len(pool)]
            if not has_word_overlap(text, alt):
                expansion = alt
                break

    result = text.rstrip('.') + expansion

    # If way too long, try shorter expansion
    if len(result) > target_len * 1.5:
        short = SHORT_EXPANSIONS[wrong_idx % len(SHORT_EXPANSIONS)]
        alt = text.rstrip('.') + short
        if abs(len(alt) - target_len) < abs(len(result) - target_len):
            result = alt

    # If still too short, try a different category
    if len(result) < target_len * 0.5:
        for bc in ['species', 'ecosystem', 'evolut', 'default']:
            if bc != category and bc in EXPANSION_POOLS:
                backup = EXPANSION_POOLS[bc][wrong_idx % 3]
                alt = text.rstrip('.') + backup
                if len(alt) >= target_len * 0.55:
                    result = alt
                    break

    return result


def truncate_at_word(text, max_len):
    if len(text) <= max_len:
        return text
    pos = text.rfind(' ', 0, max_len)
    if pos > max_len * 0.5:
        return text[:pos].rstrip(' ,;:')
    return text[:max_len].rstrip(' ,;:')


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    fixed = 0

    for q in data['quiz_questions']:
        opts = q['options']
        ci = next(i for i, o in enumerate(opts) if o['is_correct'])
        wis = [i for i, o in enumerate(opts) if not o['is_correct']]

        clen = len(opts[ci]['text'])
        wlens = [len(opts[i]['text']) for i in wis]
        avg_w = sum(wlens) / len(wlens) if wlens else 1
        ratio = clen / avg_w if avg_w > 0 else 0

        if ratio < 3.0:
            continue

        new_correct = trim_correct(opts[ci]['text'], avg_w)

        # Safety check
        if len(new_correct) < avg_w * 0.7:
            new_correct = re.sub(r'\s*\([^)]{25,}\)', '', opts[ci]['text'])
            new_correct = re.sub(r'\s+', ' ', new_correct).strip()
            if has_unmatched_parens(new_correct):
                new_correct = re.sub(r'\s*\([^)]+\)', '', opts[ci]['text'])
                new_correct = re.sub(r'\s+', ' ', new_correct).strip()

        target = len(new_correct)

        for wi, idx in enumerate(wis):
            orig_wrong = opts[idx]['text']
            new_wrong = expand_wrong(orig_wrong, target, wi, q['question_text'])

            # Only truncate expanded portion, never original text
            if len(new_wrong) > len(orig_wrong) and len(new_wrong) > target * 1.4:
                max_cut = max(int(target * 1.25), len(orig_wrong))
                new_wrong = truncate_at_word(new_wrong, max_cut)

            opts[idx]['text'] = new_wrong

        opts[ci]['text'] = new_correct
        fixed += 1

    return data, fixed


def verify_file(data):
    remaining = []
    for q in data['quiz_questions']:
        clen = 0
        wlens = []
        for o in q['options']:
            if o['is_correct']:
                clen = len(o['text'])
            else:
                wlens.append(len(o['text']))
        avg = sum(wlens) / len(wlens) if wlens else 1
        r = clen / avg if avg > 0 else 0
        if r >= 3.0:
            remaining.append((q['question_number'], r, clen, int(avg)))
    return remaining


def check_broken_parens(data, filename):
    """Check for any options with unmatched parentheses."""
    issues = []
    for q in data['quiz_questions']:
        for o in q['options']:
            if has_unmatched_parens(o['text']):
                issues.append((q['question_number'], o['text'][:80]))
    return issues


FILES = [
    'content_data/BiologyLessons/Unit5/Lesson5.1_Quiz.json',
    'content_data/BiologyLessons/Unit5/Lesson5.2_Quiz.json',
    'content_data/BiologyLessons/Unit5/Lesson5.4_Quiz.json',
    'content_data/BiologyLessons/Unit5/Lesson5.5_Quiz.json',
    'content_data/BiologyLessons/Unit6/Lesson6.3_Quiz.json',
    'content_data/BiologyLessons/Unit6/Lesson6.4_Quiz.json',
    'content_data/BiologyLessons/Unit6/Lesson6.6_Quiz.json',
    'content_data/BiologyLessons/Unit7/Lesson7.1_Quiz.json',
    'content_data/BiologyLessons/Unit7/Lesson7.3_Quiz.json',
    'content_data/BiologyLessons/Unit7/Lesson7.4_Quiz.json',
    'content_data/BiologyLessons/Unit7/Lesson7.5_Quiz.json',
    'content_data/BiologyLessons/Unit7/Lesson7.6_Quiz.json',
    'content_data/BiologyLessons/Unit7/Lesson7.7_Quiz.json',
]

MS_MAPPING = {'Unit5': 'Unit2', 'Unit6': 'Unit3', 'Unit7': 'Unit3'}


if __name__ == '__main__':
    total_fixed = 0
    all_remaining = []

    for filepath in FILES:
        basename = os.path.basename(filepath)
        print(f"\nProcessing {basename}...")

        data, fixed = process_file(filepath)
        total_fixed += fixed

        remaining = verify_file(data)
        paren_issues = check_broken_parens(data, basename)

        print(f"  Fixed {fixed} giveaway questions")

        if paren_issues:
            print(f"  WARNING: {len(paren_issues)} broken parentheses:")
            for qn, txt in paren_issues:
                print(f"    Q{qn}: {txt}...")

        if remaining:
            print(f"  WARNING: {len(remaining)} giveaways remain:")
            for qn, r, cl, aw in remaining:
                print(f"    Q{qn}: ratio={r:.1f}x correct={cl} avg_wrong={aw}")
            all_remaining.extend([(basename, qn, r, cl, aw)
                                  for qn, r, cl, aw in remaining])
        else:
            print(f"  All giveaways resolved!")

        # Write Biology file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Written: {filepath}")

        # Copy to MS_Biology
        for uk, mu in MS_MAPPING.items():
            if uk in filepath:
                mp = filepath.replace('BiologyLessons', 'MS_BiologyLessons').replace(uk, mu)
                md = os.path.dirname(mp)
                if os.path.exists(md):
                    with open(mp, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                    print(f"  Copied to: {mp}")
                else:
                    print(f"  WARNING: dir not found: {md}")
                break

    print(f"\n{'='*60}")
    print(f"Total giveaways fixed: {total_fixed}")
    if all_remaining:
        print(f"Remaining issues ({len(all_remaining)}):")
        for bn, qn, r, cl, aw in all_remaining:
            print(f"  {bn} Q{qn}: ratio={r:.1f}x correct={cl} avg_wrong={aw}")
    else:
        print("All giveaways resolved successfully!")
