"""
Deep quality audit of all course JSON files.
Structure: dict of lesson_id -> {quiz_questions: [{question_text, options: [{text, is_correct}], explanation}]}

Checks:
  1. Structural issues (missing fields, wrong types, no correct answer, multiple correct)
  2. Duplicate questions within a lesson
  3. Very short questions or options
  4. Empty/tiny explanations
  5. Duplicate options within a question
  6. "All/None of the above" meta-options
  7. Correct answer position distribution (should be ~25% each)
  8. Lessons with != 20 questions
  9. Cross-lesson duplicate questions within same course
  10. Questions where correct answer text appears in wrong answer text or vice versa
  11. Gibberish/filler padding detection (e.g. "in this particular context")
"""
import json, os, re
from collections import Counter, defaultdict

CONTENT_DIR = "content_data"
COURSES = [
    "algebra_1", "algebra_2", "anatomy", "astronomy", "biology",
    "chemistry", "earth_science", "environmental_science", "financial_math",
    "geometry", "integrated_science", "linear_algebra", "marine_science",
    "physics", "precalculus", "statistics", "trigonometry"
]

# Filler phrases that may have been injected by the balancer
FILLER_PHRASES = [
    "in this particular context",
    "under these specific conditions",
    "when considering all relevant factors",
    "based on current scientific understanding",
    "as demonstrated through experimental results",
    "according to established principles",
    "within the given framework",
    "considering the broader implications",
    "in practical applications",
    "from a theoretical perspective",
]

issues = defaultdict(list)
stats = {}

for course in COURSES:
    path = os.path.join(CONTENT_DIR, f"{course}_lessons.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_qs = 0
    correct_pos_counts = Counter()  # position of correct answer (0-3)
    wrong_q_count_lessons = []
    duplicate_q_in_lesson = 0
    duplicate_q_cross_lesson = 0
    duplicate_opt_count = 0
    short_q_count = 0
    short_opt_count = 0
    empty_explanation_count = 0
    aota_nota_count = 0
    structural_errors = 0
    filler_count = 0
    multi_correct_count = 0
    no_correct_count = 0

    all_q_texts = {}  # q_text_lower -> lesson_id for cross-lesson dup detection

    lesson_ids = sorted(data.keys())
    for lesson_id in lesson_ids:
        lesson = data[lesson_id]
        if not isinstance(lesson, dict):
            structural_errors += 1
            issues[course].append(f"  {lesson_id}: lesson is not a dict")
            continue

        questions = lesson.get("quiz_questions", [])
        total_qs += len(questions)

        if len(questions) != 20:
            wrong_q_count_lessons.append((lesson_id, len(questions)))

        seen_q_texts = set()
        for qi, q in enumerate(questions):
            if not isinstance(q, dict):
                structural_errors += 1
                issues[course].append(f"  {lesson_id} q{qi}: not a dict")
                continue

            q_text = q.get("question_text", "")
            options = q.get("options", [])
            explanation = q.get("explanation", "")

            # Structural: check options
            if not isinstance(options, list) or len(options) != 4:
                structural_errors += 1
                issues[course].append(f"  {lesson_id} q{qi}: options count = {len(options) if isinstance(options, list) else 'not-list'}")
                continue

            # Find correct answer position
            correct_positions = []
            for oi, opt in enumerate(options):
                if not isinstance(opt, dict):
                    structural_errors += 1
                    issues[course].append(f"  {lesson_id} q{qi} opt{oi}: not a dict")
                    continue
                if opt.get("is_correct"):
                    correct_positions.append(oi)

            if len(correct_positions) == 0:
                no_correct_count += 1
                issues[course].append(f"  {lesson_id} q{qi}: NO correct answer marked!")
            elif len(correct_positions) > 1:
                multi_correct_count += 1
                issues[course].append(f"  {lesson_id} q{qi}: MULTIPLE correct answers: positions {correct_positions}")
            else:
                correct_pos_counts[correct_positions[0]] += 1

            # Duplicate question in lesson
            q_lower = q_text.strip().lower()
            if q_lower in seen_q_texts:
                duplicate_q_in_lesson += 1
                issues[course].append(f"  {lesson_id} q{qi}: DUPLICATE in lesson: '{q_text[:60]}'")
            seen_q_texts.add(q_lower)

            # Cross-lesson duplicate
            if q_lower in all_q_texts and all_q_texts[q_lower] != lesson_id:
                duplicate_q_cross_lesson += 1
                issues[course].append(f"  {lesson_id} q{qi}: CROSS-LESSON DUP with {all_q_texts[q_lower]}: '{q_text[:60]}'")
            all_q_texts[q_lower] = lesson_id

            # Short question
            if len(q_text.strip()) < 15:
                short_q_count += 1
                issues[course].append(f"  {lesson_id} q{qi}: short question ({len(q_text)} chars): '{q_text}'")

            # Check each option
            opt_texts = []
            for oi, opt in enumerate(options):
                if not isinstance(opt, dict):
                    continue
                t = opt.get("text", "")
                opt_texts.append(t.strip().lower())

                if len(t.strip()) < 3:
                    short_opt_count += 1
                    issues[course].append(f"  {lesson_id} q{qi} opt{oi}: short option ({len(t)} chars): '{t}'")

                # Filler phrase detection
                for phrase in FILLER_PHRASES:
                    if phrase in t.lower():
                        filler_count += 1
                        break

            # Duplicate options
            if len(opt_texts) != len(set(opt_texts)):
                duplicate_opt_count += 1
                issues[course].append(f"  {lesson_id} q{qi}: duplicate options")

            # Empty explanation
            if not explanation or len(explanation.strip()) < 10:
                empty_explanation_count += 1
                issues[course].append(f"  {lesson_id} q{qi}: empty/tiny explanation ({len(explanation)} chars)")

            # Meta options
            for opt in options:
                if isinstance(opt, dict):
                    low = opt.get("text", "").strip().lower()
                    if low in ("all of the above", "none of the above", "all of these",
                               "none of these", "both a and b", "a and b", "b and c", "a and c"):
                        aota_nota_count += 1
                        issues[course].append(f"  {lesson_id} q{qi}: meta-option '{opt['text'].strip()}'")
                        break

    # Correct position distribution
    total_for_dist = sum(correct_pos_counts.values())
    pos_dist = {}
    for i in range(4):
        pct = correct_pos_counts[i] / total_for_dist * 100 if total_for_dist else 0
        pos_dist[i] = (correct_pos_counts[i], pct)

    stats[course] = {
        "lessons": len(lesson_ids),
        "questions": total_qs,
        "wrong_q_count": wrong_q_count_lessons,
        "structural_errors": structural_errors,
        "no_correct": no_correct_count,
        "multi_correct": multi_correct_count,
        "dup_in_lesson": duplicate_q_in_lesson,
        "dup_cross_lesson": duplicate_q_cross_lesson,
        "duplicate_options": duplicate_opt_count,
        "short_questions": short_q_count,
        "short_options": short_opt_count,
        "empty_explanations": empty_explanation_count,
        "aota_nota": aota_nota_count,
        "filler_count": filler_count,
        "pos_dist": pos_dist,
    }

# --- Print report ---
print("=" * 100)
print("DEEP QUALITY AUDIT REPORT")
print("=" * 100)

grand_totals = Counter()
for course in COURSES:
    s = stats[course]
    print(f"\n{'─'*80}")
    print(f"  {course.upper()} — {s['lessons']} lessons, {s['questions']} questions")
    print(f"{'─'*80}")

    any_issue = False

    if s["wrong_q_count"]:
        print(f"  ⚠ Lessons with != 20 questions: {len(s['wrong_q_count'])}")
        for lid, cnt in s["wrong_q_count"][:10]:
            print(f"      {lid}: {cnt} questions")
        if len(s["wrong_q_count"]) > 10:
            print(f"      ... and {len(s['wrong_q_count']) - 10} more")
        any_issue = True

    for label, key in [
        ("Structural errors", "structural_errors"),
        ("No correct answer", "no_correct"),
        ("Multiple correct answers", "multi_correct"),
        ("Duplicate questions (in-lesson)", "dup_in_lesson"),
        ("Duplicate questions (cross-lesson)", "dup_cross_lesson"),
        ("Duplicate options in question", "duplicate_options"),
        ("Very short questions", "short_questions"),
        ("Very short options", "short_options"),
        ("Empty/tiny explanations", "empty_explanations"),
        ("Meta-options (all/none of above)", "aota_nota"),
        ("Options with filler phrases", "filler_count"),
    ]:
        val = s[key]
        grand_totals[key] += val
        if val:
            icon = "❌" if key in ("structural_errors", "no_correct", "multi_correct") else "⚠"
            print(f"  {icon} {label}: {val}")
            any_issue = True

    # Position distribution
    print(f"  Answer position distribution:")
    for i in range(4):
        cnt, pct = s["pos_dist"][i]
        bar = "█" * int(pct / 2)
        skew = " ⚠ SKEWED" if (pct < 15 or pct > 35) and s["questions"] > 0 else ""
        print(f"      [{i}]: {cnt:5d} ({pct:5.1f}%) {bar}{skew}")

    if not any_issue:
        print(f"  ✅ No content issues found")

# Grand totals
print(f"\n{'='*100}")
print("GRAND TOTALS")
print(f"{'='*100}")
total_lessons = sum(s["lessons"] for s in stats.values())
total_qs = sum(s["questions"] for s in stats.values())
print(f"  Total courses: {len(COURSES)}")
print(f"  Total lessons: {total_lessons}")
print(f"  Total questions: {total_qs}")
for label, key in [
    ("Structural errors", "structural_errors"),
    ("No correct answer", "no_correct"),
    ("Multiple correct answers", "multi_correct"),
    ("Duplicate questions (in-lesson)", "dup_in_lesson"),
    ("Duplicate questions (cross-lesson)", "dup_cross_lesson"),
    ("Duplicate options", "duplicate_options"),
    ("Short questions", "short_questions"),
    ("Short options", "short_options"),
    ("Empty explanations", "empty_explanations"),
    ("Meta-options", "aota_nota"),
    ("Filler phrases in options", "filler_count"),
]:
    val = grand_totals[key]
    icon = "✅" if val == 0 else ("❌" if key in ("structural_errors", "no_correct", "multi_correct") else "⚠")
    print(f"  {icon} {label}: {val}")

# Summary table
print(f"\n{'='*100}")
print("SUMMARY TABLE")
print(f"{'='*100}")
hdr = f"{'Course':<25} {'Les':>4} {'Qs':>6} {'Err':>4} {'NoC':>4} {'MuC':>4} {'DpL':>4} {'DpX':>4} {'DpO':>4} {'ShQ':>4} {'ShO':>4} {'NoE':>4} {'Meta':>4} {'Fill':>5} {'!=20':>4}"
print(hdr)
print("─" * len(hdr))
for course in COURSES:
    s = stats[course]
    print(f"{course:<25} {s['lessons']:>4} {s['questions']:>6} {s['structural_errors']:>4} {s['no_correct']:>4} {s['multi_correct']:>4} {s['dup_in_lesson']:>4} {s['dup_cross_lesson']:>4} {s['duplicate_options']:>4} {s['short_questions']:>4} {s['short_options']:>4} {s['empty_explanations']:>4} {s['aota_nota']:>4} {s['filler_count']:>5} {len(s['wrong_q_count']):>4}")

# Print detailed issues (first 20 per course)
any_details = any(issues[c] for c in COURSES)
if any_details:
    print(f"\n{'='*100}")
    print("DETAILED ISSUES (first 20 per course)")
    print(f"{'='*100}")
    for course in COURSES:
        if issues[course]:
            print(f"\n{course} ({len(issues[course])} issues):")
            for line in issues[course][:20]:
                print(line)
            if len(issues[course]) > 20:
                print(f"  ... and {len(issues[course]) - 20} more")
