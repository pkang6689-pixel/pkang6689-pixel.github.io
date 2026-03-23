# AP Courses Content Library

This folder contains comprehensive lesson data for all AP courses offered through ArisEdu.

## Course Files

| Course | File | Lessons | Content |
|--------|------|---------|---------|
| AP Biology | `ap_biology_lessons.json` | 40 | Comprehensive summaries, flashcards, quiz questions |
| AP Chemistry | `ap_chemistry_lessons.json` | 41 | Comprehensive summaries, flashcards, quiz questions |
| AP Calculus AB | `ap_calculus_ab_lessons.json` | 76 | Comprehensive summaries, flashcards, quiz questions |
| AP Statistics | `ap_statistics_lessons.json` | 45 | Comprehensive summaries, flashcards, quiz questions |
| AP Environmental Science | `ap_environmental_science_lessons.json` | 45 | Comprehensive summaries, flashcards, quiz questions |
| AP Human Geography | `ap_human_geography_lessons.json` | 41 | Comprehensive summaries, flashcards, quiz questions |
| AP Physics 2 | `ap_physics_2_lessons.json` | 35 | Comprehensive summaries, flashcards, quiz questions |
| AP Physics C - Mechanics | `ap_physics_c_-_mechanics_lessons.json` | 28 | Comprehensive summaries, flashcards, quiz questions |

## Total Content
- **8 AP Courses**
- **351 Lessons Total**
- **Per Lesson**: 4 summary sections, 10 flashcards, 7 quiz questions

## JSON Structure

Each JSON file contains an object where:
- **Keys**: Lesson IDs (e.g., "lesson_1_1")
- **Values**: Lesson objects with:
  - `title`: Lesson title
  - `unit_number`: Unit within the course
  - `lesson_number`: Lesson number within the unit
  - `course_name`: Name of the AP course
  - `summary_sections`: Array of 4 summary sections
  - `flashcards`: Array of 10 flashcard Q&A pairs
  - `quiz_questions`: Array of 7 multiple-choice quiz questions
  - `practice_questions`: Practice problems

## Usage

To access AP lessons programmatically:

```python
import json

# Load a specific course
with open('ap_biology_lessons.json', 'r', encoding='utf-8') as f:
    biology_lessons = json.load(f)

# Access specific lesson
lesson = biology_lessons['lesson_1_1']
print(lesson['title'])
print(lesson['summary_sections'])
print(lesson['flashcards'])
print(lesson['quiz_questions'])
```

## Organization

All AP course content is now organized in this dedicated folder for:
- Easy maintenance and updates
- Clear separation from other course materials
- Scalability for adding new AP courses
- Streamlined access for content management systems
