import json
import sys

def fix_file(filepath, fixes):
    with open(filepath, encoding='utf-8') as fh:
        data = json.load(fh)

    for q in data['quiz_questions']:
        qn = q['question_number']
        if qn in fixes:
            wrong_idx = 0
            for opt in q['options']:
                if not opt['is_correct']:
                    opt['text'] = fixes[qn][wrong_idx]
                    wrong_idx += 1

    with open(filepath, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)

    # Verify
    with open(filepath, encoding='utf-8') as fh:
        data2 = json.load(fh)
    bad = 0
    for q in data2['quiz_questions']:
        correct_len = 0
        wrong_lens = []
        for opt in q['options']:
            if opt['is_correct']:
                correct_len = len(opt['text'])
            else:
                wrong_lens.append(len(opt['text']))
        avg_wrong = sum(wrong_lens) / len(wrong_lens) if wrong_lens else 1
        ratio = correct_len / avg_wrong if avg_wrong > 0 else 0
        if ratio >= 3.0:
            bad += 1
            print(f"  STILL BAD Q{q['question_number']}: ratio={ratio:.1f}x, correct={correct_len}, avg_wrong={avg_wrong:.0f}")
    lesson = data2.get('lesson_number', filepath)
    print(f"Lesson {lesson}: {bad} remaining giveaways")

if __name__ == '__main__':
    pass
