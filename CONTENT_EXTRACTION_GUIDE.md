# Content Extraction Framework - Complete Guide

## Overview

The Content Extraction Framework allows you to extract all educational content (notes, flashcards, practice questions, and quizzes) from your existing HTML lesson files and store them in Python/JSON data structures.

This makes it easy to:
- **Modify content** without touching HTML
- **Add translations** to all languages
- **Maintain consistency** across all lessons
- **Regenerate HTML** with all formatting and functionality preserved
- **Version control** your content separately from presentations

---

## What Gets Extracted

### 1. **Summary Notes**
- Extracted from `.lesson-notes` divs in `*_Summary.html` files
- Includes formatted HTML content, tables, formulas, etc.
- Organized by sections (h3 headings)

### 2. **Flashcards**
- Extracted from `window.lessonFlashcards` JavaScript arrays
- Question/answer pairs
- Used in practice games

### 3. **Quiz Questions**
- Extracted from quiz forms in `*_Quiz.html` files  
- Each question includes:
  - Question text
  - Multiple choice options
  - Correct answer indicator
  - Attempt limit

---

## Quick Start

### Step 1: Extract All Courses

Extract content from all 6 courses:

```bash
python extract_all_courses.py
```

This will:
- Extract Chemistry, Algebra 1&2, Biology, Geometry, Physics
- Create JSON files in `content_data/` folder
- Generate extraction summaries

**Output files:**
- `content_data/chemistry_lessons.json`
- `content_data/algebra_1_lessons.json`
- `content_data/algebra_2_lessons.json`
- `content_data/biology_lessons.json`
- `content_data/geometry_lessons.json`
- `content_data/physics_lessons.json`

### Step 2: Modify Content (Optional)

Edit any JSON file to:
- Change question wording
- Add/remove options
- Update answers
- Modify summary notes

Example editing a quiz question:

```json
{
  "question_number": 1,
  "question_text": "What is the sum of interior angles?",
  "options": [
    {
      "text": "(n − 2) × 180°",
      "is_correct": true
    },
    {
      "text": "n × 180°", 
      "is_correct": false
    }
  ]
}
```

### Step 3: Add Translations

Add translations to any JSON file:

```json
{
  "data_i18n": "Lesson 6.1: Angles of Polygons - Quiz",
  "data_i18n_q": "What are interior angles?",
  "data_i18n_a": "Angles inside a polygon"
}
```

### Step 4: Regenerate HTML

Regenerate all HTML files with your changes:

```bash
python regenerate_all_html.py
```

This will:
- Read all JSON files from `content_data/`
- Generate new HTML files with full functionality
- Preserve all formatting, buttons, games
- Output to original lesson folders

---

## File Purpose Reference

| File | Purpose |
|------|---------|
| `content_extraction_framework.py` | Core framework with data classes and extractors |
| `extract_course_content.py` | Generic extraction for any course |
| `extract_geometry_content.py` | Geometry-specific extraction (example) |
| `extract_all_courses.py` | Master extraction for all courses |
| `regenerate_geometry_html.py` | Geometry-specific HTML regeneration (example) |
| `regenerate_all_html.py` | Master regeneration for all courses |
| `content_data/` | Output folder with extracted JSON data |

---

## Advanced Usage

### Extract a Single Course

```bash
python extract_course_content.py Chemistry "c:\path\to\ChemistryLessons"
```

### Create a Custom Extraction Script

For a specific course, based on `extract_geometry_content.py`:

```python
from content_extraction_framework import HTMLExtractor, Lesson

extractor = HTMLExtractor()

# Extract from a specific HTML file
summary_file = r"C:\path\to\Lesson.html"
with open(summary_file, 'r') as f:
    content = f.read()
    
# Extract different content types
notes = HTMLExtractor.extract_summary_notes(content)
quiz_q = HTMLExtractor.extract_quiz_questions(content)
cards = HTMLExtractor.extract_flashcards(content)
```

### Manual JSON Editing

Edit `content_data/geometry_lessons.json` to:

1. **Change a question:**
   ```json
   "question_text": "New question here?"
   ```

2. **Add a flashcard:**
   ```json
   {
     "question": "What is a polygon?",
     "answer": "A closed shape with straight sides"
   }
   ```

3. **Remove options:**
   Delete from the `options` array

4. **Update summary notes:**
   Edit the `content_html` field with HTML

---

## Content Structure

### Directory Organization

```
content_data/
├── geometry_lessons.json          # All Geometry lessons
├── chemistry_lessons.json         # All Chemistry lessons
├── algebra_1_lessons.json         # All Algebra 1 lessons
├── algebra_2_lessons.json         # All Algebra 2 lessons
├── biology_lessons.json           # All Biology lessons
├── physics_lessons.json           # All Physics lessons
├── geometry_extraction_summary.txt
├── chemistry_extraction_summary.txt
└── ... (more summaries)
```

### JSON Lesson Structure

```json
{
  "u6_l1": {
    "unit": 6,
    "lesson_number": "6.1",
    "title": "Angles of Polygons",
    "course": "Geometry",
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

## Translation Integration

### Adding Multi-Language Support

1. **In JSON, add translation fields:**
   ```json
   {
     "data_i18n": "Lesson 6.1: Angles of Polygons",
     "data_i18n_q": "The sum of interior angles",
     "data_i18n_a": "(n − 2) × 180°"
   }
   ```

2. **Regenerate HTML:**
   ```bash
   python regenerate_all_html.py
   ```

3. **HTML will include:**
   ```html
   <h2 data-i18n="Lesson 6.1: Angles of Polygons">Lesson 6.1...</h2>
   ```

4. **Translation system will use i18n framework** to apply actual translations

---

## Common Workflows

### Adding a New Question to a Quiz

1. Open `content_data/geometry_lessons.json`
2. Find the lesson you want to edit
3. Add to `quiz_questions` array:
   ```json
   {
     "question_number": 8,
     "question_text": "Your new question?",
     "options": [
       {"text": "Correct answer", "is_correct": true},
       {"text": "Wrong answer", "is_correct": false}
     ]
   }
   ```
4. In your terminal:
   ```bash
   python regenerate_all_html.py
   ```
5. HTML file is automatically updated with full functionality!

### Fixing a Typo in All Lessons

1. Open the JSON file: `content_data/geometry_lessons.json`
2. Use Find & Replace to fix "Polygon" → "polygon" everywhere
3. Save
4. Run: `python regenerate_all_html.py`
5. All HTML files update automatically

### Translating All Content

1. Each JSON file has all English content
2. Create a translation script that:
   - Reads JSON
   - Calls translation API
   - Updates `data_i18n*` fields
3. Run regeneration
4. All HTML files now support the new language

### Backup & Version Control

```bash
# Git workflow for content management:
git add content_data/
git commit -m "Updated geometry quiz questions"
git push

# If you need to revert:
git revert <commit_hash>
python regenerate_all_html.py
```

---

## Troubleshooting

### Issue: "JSON file not found" when regenerating

**Solution:** Make sure you ran extraction first:
```bash
python extract_all_courses.py
```

### Issue: HTML regeneration creates empty files

**Solution:** Check that JSON files have valid syntax:
```bash
python -m json.tool content_data/geometry_lessons.json
```

### Issue: Custom quiz styling not preserved

**Current limitation:** The renderer uses standard styling. To customize:
1. Edit `HTMLRenderer.QUIZ_TEMPLATE` in `content_extraction_framework.py`
2. Run regeneration
3. Your custom template will apply to all courses

### Issue: Missing formulas or special characters

**Solution:** Check that HTML entities are properly escaped in JSON:
- Use `°` instead of `°` 
- Use `&nbsp;` for spaces
- Use `<br>` for line breaks

---

## Performance Notes

- **Extraction time:** ~2-5 seconds per course
- **Regeneration time:** ~3-10 seconds per course  
- **JSON file sizes:** 500KB - 2MB per course
- **Total extracted content:** ~500KB across all courses

---

## Next Steps

1. **Run extraction:**
   ```bash
   python extract_all_courses.py
   ```

2. **Review generated files:**
   - Check `content_data/` for JSON files
   - Read extraction summary files
   - Verify all lessons were captured

3. **Customize lessons** as needed by editing JSON

4. **Add translations** by updating JSON with i18n fields

5. **Regenerate HTML:**
   ```bash
   python regenerate_all_html.py
   ```

6. **Test your changes:**
   - Open regenerated HTML files
   - Verify all functionality works
   - Check formatting preserved

---

## Support

For issues or questions:
1. Check this guide's Troubleshooting section
2. Review the JSON file syntax
3. Check framework error messages during extraction/regeneration
4. Verify all source HTML files exist and are readable

---

**Framework Version:** 1.0  
**Last Updated:** 2026-03-02  
**Courses Supported:** Chemistry, Algebra 1&2, Biology, Geometry, Physics
