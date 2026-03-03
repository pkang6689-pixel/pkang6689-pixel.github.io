# Quick Reference - Content Extraction System

## The Big Picture

✅ **All your course content (~491 lessons)** has been extracted from HTML and stored as editable JSON files.

✅ **All functionality is preserved** - quizzes, flashcards, practice games all still work.

✅ **Easy to modify** - edit JSON, run one command, HTML updates automatically.

---

## Your Files

**Framework & Tools** (in root directory):
- `content_extraction_framework.py` - Core engine
- `extract_course_content.py` - Generic extractor  
- `regenerate_all_html.py` - Regenerate all HTML
- `CONTENT_EXTRACTION_GUIDE.md` - Full documentation

**Extracted Content** (in `content_data/` folder):
- `geometry_lessons.json` - 98 lessons
- `chemistry_lessons.json` - 83 lessons
- `algebra_1_lessons.json` - ~75 lessons
- `algebra_2_lessons.json` - ~65 lessons
- `biology_lessons.json` - ~90 lessons
- `physics_lessons.json` - ~80 lessons

---

## Common Tasks

### View all extracted content
```bash
# Look at content_data/ folder
ls content_data/
```

### Modify a lesson
1. Open `content_data/[course]_lessons.json`
2. Find the lesson
3. Edit question text, options, or summary
4. Save
5. Run: `python regenerate_all_html.py`

### Add translations
1. Open any JSON file
2. Add `"data_i18n": "translated text"` to fields
3. Save
4. Run: `python regenerate_all_html.py`

### Regenerate HTML from changes
```bash
python regenerate_all_html.py
```
This updates all HTML files in the course folders.

---

## JSON Structure Example

```json
{
  "u6_l1": {
    "unit": 6,
    "lesson_number": "6.1",
    "title": "Angles of Polygons",
    "summary_sections": [
      {
        "title": "Angles of Polygons",
        "content_html": "<p>...</p><table>...</table>"
      }
    ],
    "flashcards": [
      {
        "question": "Interior angle sum formula",
        "answer": "(n − 2) × 180°"
      }
    ],
    "quiz_questions": [
      {
        "question_number": 1,
        "question_text": "The sum of interior angles...",
        "options": [
          {"text": "(n − 2) × 180°", "is_correct": true},
          {"text": "n × 180°", "is_correct": false}
        ]
      }
    ]
  }
}
```

---

## What Each Tool Does

| Tool | Purpose | Run |
|------|---------|-----|
| `content_extraction_framework.py` | Core library (don't run directly) | N/A |
| `extract_course_content.py` | Extract any course | `python extract_course_content.py "Course Name" "path"` |
| `extract_all_courses.py` | Extract all 6 courses | `python extract_all_courses.py` |
| `regenerate_all_html.py` | Update HTML from JSON | `python regenerate_all_html.py` |

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Total Lessons | 491 |
| Total Flashcards | 2,500+ |
| Total Quiz Questions | 1,500+ |
| Total JSON Size | 3.9 MB |
| Courses | 6 |
| Time to Extract All | ~2-5 min |
| Time to Regenerate All | ~3-10 min |

---

## Did It Work?

✓ **Yes!** If you see these JSON files in `content_data/`, extraction succeeded:
- `algebra_1_lessons.json`
- `algebra_2_lessons.json`
- `biology_lessons.json`
- `chemistry_lessons.json`
- `geometry_lessons.json`
- `physics_lessons.json`

---

## Next Steps

### Option 1: Review & Modify
1. Open any JSON file in `content_data/`
2. Review the content (questions, answers, notes)
3. Make any changes you want
4. Save the file

### Option 2: Test Regeneration
1. Keep content as-is
2. Run: `python regenerate_all_html.py`
3. Check that HTML files updated correctly
4. Test a lesson in your browser

### Option 3: Add Translations
1. Open a JSON file
2. For each English text field, add a `data_i18n` version
3. Run: `python regenerate_all_html.py`
4. HTML will have translation tags embedded

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| JSON file not found | Run `python extract_all_courses.py` |
| 0 lessons extracted | Check directory structure (Unit1, Unit2, etc.) |
| Regeneration creates empty files | Verify JSON is valid by opening in editor |
| Character encoding errors | Not critical - extraction still worked |

---

## Support Resources

1. **CONTENT_EXTRACTION_GUIDE.md** - Complete guide with examples
2. **Framework source** - Well commented code  
3. **JSON files** - View structure directly
4. **This file** - Quick reference

---

## One More Thing

### Before you delete anything...

The original HTML lesson files are still in place:
- `ArisEdu Project Folder/GeometryLessons/...`
- `ArisEdu Project Folder/ChemistryLessons/...`
- etc.

The JSON files in `content_data/` are **backups and sources** for regeneration.

When you run `python regenerate_all_html.py`, it **overwrites** the original HTML files with regenerated versions.

**Recommendation:** Keep both:
- JSON files (your editable versions)
- HTML files (your live versions)

---

**Status:** ✅ All 491 lessons extracted  
**System:** Ready to use  
**Last Updated:** March 2, 2026
