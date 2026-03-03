"""
Content Extraction and Rendering Framework for ArisEdu
Extracts lessons, summaries, flashcards, practice questions, and quizzes from HTML
Stores in Python data structures for easy modification and translation
Regenerates HTML with full functionality
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
import json
import re
from pathlib import Path


@dataclass
class QuizOption:
    """A single option in a quiz question"""
    text: str
    is_correct: bool
    data_i18n: Optional[str] = None


@dataclass
class QuizQuestion:
    """A complete quiz question with options"""
    question_number: int
    question_text: str
    options: List[QuizOption]
    attempted: int = 2
    data_i18n: Optional[str] = None


@dataclass
class Flashcard:
    """A flashcard with question and answer"""
    question: str
    answer: str
    data_i18n_q: Optional[str] = None
    data_i18n_a: Optional[str] = None


@dataclass
class PracticeQuestion:
    """Practice questions (may include multiple choice, etc)"""
    question_number: int
    question_text: str
    options: List[QuizOption]
    data_i18n: Optional[str] = None


@dataclass
class SummarySection:
    """A section of summary notes"""
    title: str
    content_html: str  # Raw HTML content for notes
    data_i18n: Optional[str] = None


@dataclass
class Lesson:
    """Complete lesson with all content"""
    unit: int
    lesson_number: str  # e.g., "6.1"
    title: str
    
    # Content
    summary_sections: List[SummarySection] = field(default_factory=list)
    flashcards: List[Flashcard] = field(default_factory=list)
    practice_questions: List[PracticeQuestion] = field(default_factory=list)
    quiz_questions: List[QuizQuestion] = field(default_factory=list)
    
    # Metadata
    course: str = ""  # e.g., "Geometry"
    translations: Dict[str, Dict[str, str]] = field(default_factory=dict)  # {lang: {key: value}}


class HTMLExtractor:
    """Extracts content from existing HTML files"""
    
    @staticmethod
    def extract_quiz_questions(html_content: str) -> List[QuizQuestion]:
        """Extract quiz questions from HTML"""
        questions = []
        
        # Find all quiz-question divs
        pattern = r'<div class="quiz-question"[^>]*data-attempts="(\d+)"[^>]*>(.*?)</div>\s*(?=<div class="quiz-question"|</form>)'
        matches = re.findall(pattern, html_content, re.DOTALL)
        
        question_num = 1
        for attempts_str, question_html in matches:
            attempts = int(attempts_str)
            
            # Extract question text
            q_text_match = re.search(r'<p[^>]*style="font-weight: 700[^>]*>.*?(\d+)\.\s*(.*?)</p>', question_html, re.DOTALL)
            if not q_text_match:
                continue
            
            question_text = q_text_match.group(2).strip()
            
            # Extract options
            options = []
            option_pattern = r'<input type="radio" name="[^"]*" value="(correct|wrong)"\s*>\s*(.*?)\s*</label>'
            for value, option_text in re.findall(option_pattern, question_html):
                options.append(QuizOption(
                    text=option_text.strip(),
                    is_correct=(value == "correct")
                ))
            
            if options:
                questions.append(QuizQuestion(
                    question_number=question_num,
                    question_text=question_text,
                    options=options,
                    attempted=attempts
                ))
                question_num += 1
        
        return questions
    
    @staticmethod
    def extract_flashcards(js_script: str) -> List[Flashcard]:
        """Extract flashcards from JavaScript window.lessonFlashcards"""
        flashcards = []
        
        # Find the window.lessonFlashcards array - use greedy match to capture all content
        pattern = r'window\.lessonFlashcards\s*=\s*\[([\s\S]*?)\];'
        match = re.search(pattern, js_script, re.DOTALL)
        
        if not match:
            return flashcards
        
        cards_text = match.group(1)
        
        # Extract individual card objects using JSON parsing approach
        # Look for "question": "..." and "answer": "..." patterns
        card_pattern = r'\{\s*"question"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*,\s*"answer"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)"\s*\}'
        
        for q_match in re.finditer(card_pattern, cards_text, re.DOTALL):
            question = q_match.group(1)
            answer = q_match.group(2)
            # Unescape JSON strings
            question = question.replace('\\"', '"').replace('\\/', '/').replace('\\\\', '\\')
            answer = answer.replace('\\"', '"').replace('\\/', '/').replace('\\\\', '\\')
            flashcards.append(Flashcard(
                question=question.strip(),
                answer=answer.strip()
            ))
        
        return flashcards
    
    @staticmethod
    def extract_summary_notes(html_content: str) -> List[SummarySection]:
        """Extract summary notes from HTML"""
        sections = []
        
        # Find the lesson-notes div
        pattern = r'<div class="lesson-notes">(.*?)</div>'
        match = re.search(pattern, html_content, re.DOTALL)
        
        if not match:
            return sections
        
        notes_html = match.group(1)
        
        # Parse sections by h3 tags
        h3_pattern = r'<h3>(.*?)</h3>'
        current_title = "Notes"
        current_content = ""
        
        for h3_match in re.finditer(h3_pattern, notes_html):
            if current_content:
                sections.append(SummarySection(
                    title=current_title,
                    content_html=current_content
                ))
            current_title = h3_match.group(1).strip()
            current_content = ""
        
        # Add remaining content
        last_h3_pos = 0
        for h3_match in re.finditer(h3_pattern, notes_html):
            last_h3_pos = h3_match.end()
        
        remaining = notes_html[last_h3_pos:] if last_h3_pos else notes_html
        sections.append(SummarySection(
            title=current_title,
            content_html=remaining.strip()
        ))
        
        return sections


class HTMLRenderer:
    """Renders Lesson data back to HTML with full functionality"""
    
    TEMPLATE_BASE = """<!DOCTYPE html>
<html lang="en" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../scripts/global_translations.js?v=7.2"></script>
    <script src="../../scripts/spanish_translations.js?v=1.0"></script>
    <script src="../../scripts/hindi_translations.js?v=1.0"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
    <style>@view-transition { navigation: auto; }</style>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="../../theme_manager.js"></script>
    <script>
        // Apply translations when DOM is ready
        document.addEventListener('DOMContentLoaded', function() {
            if (window.applyTranslations) {
                setTimeout(function() {
                    window.applyTranslations();
                }, 50);
            }
        });
    </script>
</head>
<body class="dark-mode h-full">
    <script src="../../scripts/taskbar.js"></script>
    <main class="main-container">
        {content}
    </main>
    <script src="../../../search_data.js"></script>
    <script src="../../../search_logic.js"></script>
    {scripts}
</body>
</html>"""

    SUMMARY_TEMPLATE = """<div id="summary-content-view">
    <h2 class="page-title" data-i18n="{title_i18n}">{title}</h2>
    <div class="diagram-card">
        <div class="lesson-notes">
{sections}
        </div>
        <div class="summary-actions">
            <a class="side-button" href="{lesson}_Practice.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Play</a>
        </div>
    </div>
</div>"""

    PRACTICE_TEMPLATE = """<div id="practice-content-view">
    <h2 class="page-title" data-i18n="{title_i18n}">{title}</h2>
    <div class="diagram-card">
        <div id="flashcard-game" class="flashcard-game" style="margin-top:2rem;">
            <div id="flashcard" class="flashcard-box" style="background:#fff;border-radius:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.12);padding:2rem 3rem;display:flex;align-items:center;justify-content:center;text-align:center;min-width:calc(320px + 56rem);min-height:calc(120px + 24rem);font-weight:600;color:#0f172a;margin-bottom:1rem;cursor:pointer;transition:background 0.2s, color 0.2s;">
                <span id="flashcard-content" style="width:100%;display:block;"></span>
            </div>
            <div style="display:flex;gap:1rem;">
                <button id="prev-flashcard" style="background:#ef4444;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
                    <svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
                        <path d="M15 6l-6 6 6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
                    </svg>
                </button>
                <button id="next-flashcard" style="background:#10b981;padding:0.75rem 1.5rem;border:none;border-radius:0.5rem;cursor:pointer;display:flex;align-items:center;justify-content:center;">
                    <svg fill="none" height="28" viewBox="0 0 24 24" width="28" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9 6l6 6-6 6" stroke="#fff" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"></path>
                    </svg>
                </button>
                <span id="flashcard-counter" style="display:flex;align-items:center;font-weight:600;font-size:1rem;color:#64748b;white-space:nowrap;"></span>
            </div>
        </div>
        <div class="Practice-actions" style="margin-top:2rem;display:flex;justify-content:flex-end;width:100%;">
            <a class="side-button" href="{lesson}_Quiz.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Quiz</a>
        </div>
    </div>
</div>"""

    QUIZ_TEMPLATE = """<div id="quiz-content-view">
    <h2 class="page-title" data-i18n="{title_i18n}">{title}</h2>
    <div class="diagram-card">
        <div class="quiz-container" style="padding: 2rem; width: 100%; height: 75vh; overflow-y: auto;">
            <form id="quiz-form">
{questions}
            </form>
            <div id="quiz-results" style="margin-top: 2rem; font-weight: bold; display:none; padding: 1rem; border-radius: 0.5rem;"></div>
            <div class="summary-actions" style="display: flex; gap: 1rem; justify-content: center; margin-top: 2rem;">
                <button type="button" class="side-button" onclick="window.location.href='../../{course_lower}.html'">Back to {course}</button>
                <button type="button" class="side-button" onclick="window.location.href='{next_lesson}.html'">Next Lesson</button>
            </div>
        </div>
    </div>
</div>"""

    @staticmethod
    def render_summary(lesson: Lesson, lesson_file: str) -> str:
        """Render summary HTML"""
        sections_html = ""
        for section in lesson.summary_sections:
            sections_html += f"<h3>{section.title}</h3>\n"
            sections_html += section.content_html + "\n"
        
        content = HTMLRenderer.SUMMARY_TEMPLATE.format(
            title=f"Lesson {lesson.lesson_number}: {lesson.title}",
            title_i18n=f"Lesson {lesson.lesson_number}: {lesson.title} Summary",
            sections=sections_html,
            lesson=lesson_file
        )
        
        return HTMLRenderer.TEMPLATE_BASE.format(
            title=f"Lesson {lesson.lesson_number}: {lesson.title} - Summary",
            content=content,
            scripts='<script src="../../scripts/lesson_video.js"></script>'
        )
    
    @staticmethod
    def render_practice(lesson: Lesson, lesson_file: str) -> str:
        """Render practice HTML with flashcards"""
        content = HTMLRenderer.PRACTICE_TEMPLATE.format(
            title=f"Lesson {lesson.lesson_number}: {lesson.title}",
            title_i18n=f"Lesson {lesson.lesson_number}: {lesson.title} Practice",
            lesson=lesson_file
        )
        
        flashcards_js = HTMLRenderer._generate_flashcards_js(lesson)
        
        return HTMLRenderer.TEMPLATE_BASE.format(
            title=f"Lesson {lesson.lesson_number}: {lesson.title} - Practice",
            content=content,
            scripts=f'<script src="../../scripts/practice_games.js"></script>\n<script>{flashcards_js}</script>'
        )
    
    @staticmethod
    def render_quiz(lesson: Lesson, course: str, next_lesson: str) -> str:
        """Render quiz HTML"""
        questions_html = ""
        for q in lesson.quiz_questions:
            questions_html += f'<div class="quiz-question" style="margin-bottom: 2rem;" data-attempts="{q.attempted}">\n'
            questions_html += f'<p style="font-weight: 700; font-size: 1.45rem; margin-bottom: 1rem;">{q.question_number}. {q.question_text}</p>\n'
            
            for i, option in enumerate(q.options):
                correct_class = "correct" if option.is_correct else "wrong"
                questions_html += f'<label style="display:block;margin-bottom:0.8rem;cursor:pointer;font-size:1.3rem;">\n'
                questions_html += f'<input type="radio" name="q{q.question_number}" value="{correct_class}"> {option.text}\n'
                questions_html += '</label>\n'
            
            questions_html += '<div class="attempts-indicator"></div>\n'
            questions_html += '<div style="margin-top:1.5rem;">\n'
            questions_html += f'<button type="button" class="action-button" onclick="window.checkQuizAnswer(\'q{q.question_number}\', \'correct\', this)">Submit Answer</button>\n'
            questions_html += '<button type="button" class="nav-button" onclick="window.resetQuizQuestion(this)" style="margin-left:0.5rem;">Try Again</button>\n'
            questions_html += '</div>\n'
            questions_html += '</div>\n'
        
        content = HTMLRenderer.QUIZ_TEMPLATE.format(
            title=f"Lesson {lesson.lesson_number}: {lesson.title} - Quiz",
            title_i18n=f"Lesson {lesson.lesson_number}: {lesson.title} Quiz",
            questions=questions_html,
            course=course,
            course_lower=course.lower(),
            next_lesson=next_lesson
        )
        
        return HTMLRenderer.TEMPLATE_BASE.format(
            title=f"Lesson {lesson.lesson_number}: {lesson.title} - Quiz",
            content=content,
            scripts='<script src="../../scripts/quiz_ui.js"></script>'
        )
    
    @staticmethod
    def _generate_flashcards_js(lesson: Lesson) -> str:
        """Generate JavaScript flashcards array"""
        flashcards_js = "window.lessonFlashcards = [\n"
        for card in lesson.flashcards:
            qa = card.question.replace("'", "\\'")
            aa = card.answer.replace("'", "\\'")
            flashcards_js += f"  {{ question: '{qa}', answer: '{aa}' }},\n"
        flashcards_js += "];"
        return flashcards_js


def serialize_lesson(lesson: Lesson) -> Dict:
    """Serialize lesson to dictionary for JSON storage"""
    return {
        'unit': lesson.unit,
        'lesson_number': lesson.lesson_number,
        'title': lesson.title,
        'course': lesson.course,
        'summary_sections': [
            {
                'title': s.title,
                'content_html': s.content_html,
                'data_i18n': s.data_i18n
            }
            for s in lesson.summary_sections
        ],
        'flashcards': [
            {
                'question': f.question,
                'answer': f.answer,
                'data_i18n_q': f.data_i18n_q,
                'data_i18n_a': f.data_i18n_a
            }
            for f in lesson.flashcards
        ],
        'quiz_questions': [
            {
                'question_number': q.question_number,
                'question_text': q.question_text,
                'attempted': q.attempted,
                'data_i18n': q.data_i18n,
                'options': [
                    {
                        'text': opt.text,
                        'is_correct': opt.is_correct,
                        'data_i18n': opt.data_i18n
                    }
                    for opt in q.options
                ]
            }
            for q in lesson.quiz_questions
        ]
    }


def deserialize_lesson(data: Dict) -> Lesson:
    """Deserialize lesson from dictionary"""
    lesson = Lesson(
        unit=data['unit'],
        lesson_number=data['lesson_number'],
        title=data['title'],
        course=data.get('course', '')
    )
    
    for s in data.get('summary_sections', []):
        lesson.summary_sections.append(SummarySection(
            title=s['title'],
            content_html=s['content_html'],
            data_i18n=s.get('data_i18n')
        ))
    
    for f in data.get('flashcards', []):
        lesson.flashcards.append(Flashcard(
            question=f['question'],
            answer=f['answer'],
            data_i18n_q=f.get('data_i18n_q'),
            data_i18n_a=f.get('data_i18n_a')
        ))
    
    for q in data.get('quiz_questions', []):
        options = [QuizOption(
            text=opt['text'],
            is_correct=opt['is_correct'],
            data_i18n=opt.get('data_i18n')
        ) for opt in q.get('options', [])]
        
        lesson.quiz_questions.append(QuizQuestion(
            question_number=q['question_number'],
            question_text=q['question_text'],
            options=options,
            attempted=q.get('attempted', 2),
            data_i18n=q.get('data_i18n')
        ))
    
    return lesson
