#!/usr/bin/env python3
"""
Enhance summary files to include all content covered in corresponding quiz files.
This script analyzes each quiz file and creates comprehensive summary sections
that cover all major concepts tested in the quiz.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re

def extract_concepts_from_quiz(quiz_data):
    """Extract key concepts and topics from quiz questions."""
    concepts = defaultdict(list)
    all_text = ""

    if "quiz_questions" not in quiz_data:
        return concepts

    # Collect all text from questions, options, and explanations
    for q in quiz_data["quiz_questions"]:
        question_text = q.get("question_text", "")
        explanation = q.get("explanation", "")

        all_text += question_text + " " + explanation + " "

        # Extract key terms and phrases
        # Look for "what is X", "how to", "define", etc
        if "what is" in question_text.lower():
            # Extract the concept being defined
            match = re.search(r"what is (?:the )?([^?]+)", question_text.lower())
            if match:
                concept = match.group(1).strip()
                concepts["definitions"].append(concept)

        if "calculate" in question_text.lower() or "find the" in question_text.lower():
            concepts["calculations"].append(question_text)

        if "why" in question_text.lower() or "reason" in question_text.lower():
            concepts["reasoning"].append(question_text)

        if "real world" in question_text.lower() or "example" in explanation.lower():
            concepts["applications"].append(question_text)

    return concepts, all_text

def generate_summary_from_quiz(quiz_data, course, unit, lesson_number):
    """Generate comprehensive summary sections from quiz data."""
    summary_sections = []

    if "quiz_questions" not in quiz_data or not quiz_data["quiz_questions"]:
        return summary_sections

    # Group questions by theme
    themes = defaultdict(list)

    for q in quiz_data.get("quiz_questions", []):
        question_text = q.get("question_text", "").lower()

        # Categorize questions
        if any(word in question_text for word in ["mean", "average"]):
            themes["Mean"].append(q)
        elif any(word in question_text for word in ["median", "middle"]):
            themes["Median"].append(q)
        elif any(word in question_text for word in ["mode", "frequent"]):
            themes["Mode"].append(q)
        elif "outlier" in question_text:
            themes["Outliers and Robust Measures"].append(q)
        elif any(word in question_text for word in ["weighted", "weight"]):
            themes["Weighted Calculations"].append(q)
        elif any(word in question_text for word in ["bimodal", "two mode"]):
            themes["Bimodal Distributions"].append(q)
        elif "skewed" in question_text or "skew" in question_text:
            themes["Skewed Data"].append(q)
        else:
            themes["Core Concepts"].append(q)

    # Build comprehensive summary sections
    sections = []

    # Overview section
    overview_html = "<h3>Overview</h3>\n<p>This lesson covers the fundamental measures of center used to analyze and summarize data sets. You'll learn how to calculate and apply the mean, median, and mode, and understand when each is most appropriate.</p>\n"
    sections.append({
        "title": "Lesson Overview",
        "content_html": overview_html,
        "data_i18n": None
    })

    # Definitions section
    definitions_html = "<h3>Key Definitions</h3>\n"
    seen_terms = set()

    for q in quiz_data.get("quiz_questions", []):
        text = q.get("question_text", "")
        explanation = q.get("explanation", "")

        # Extract "What is X?" definitions
        if "what is" in text.lower() and text not in seen_terms:
            definitions_html += f"<p><b>{text}</b></p>\n"
            definitions_html += f"<p>{explanation}</p>\n"
            seen_terms.add(text)

    if len(seen_terms) > 0:
        sections.append({
            "title": "Definitions and Concepts",
            "content_html": definitions_html,
            "data_i18n": None
        })

    # Calculations section
    calculations_html = "<h3>How to Calculate</h3>\n"
    calculation_examples = []

    for q in quiz_data.get("quiz_questions", []):
        text = q.get("question_text", "")
        explanation = q.get("explanation", "")

        if ("find" in text.lower() or "calculate" in text.lower() or "mean" in text.lower()) and "{" in text:
            if explanation not in calculation_examples:
                calculations_html += f"<p><b>Example:</b> {text}</p>\n"
                calculations_html += f"<p><i>Solution:</i> {explanation}</p>\n"
                calculation_examples.append(explanation)

    if len(calculation_examples) > 0:
        sections.append({
            "title": "Calculation Methods",
            "content_html": calculations_html,
            "data_i18n": None
        })

    # Outliers and robustness section
    outliers_html = "<h3>Outliers and Resistant Measures</h3>\n"
    outlier_content = []

    for q in quiz_data.get("quiz_questions", []):
        text = q.get("question_text", "").lower()
        explanation = q.get("explanation", "")

        if "outlier" in text or "resistant" in text or "affected" in text.lower():
            if explanation not in outlier_content:
                outliers_html += f"<p>{explanation}</p>\n"
                outlier_content.append(explanation)

    if len(outlier_content) > 0:
        sections.append({
            "title": "Outliers and Resistant Measures",
            "content_html": outliers_html,
            "data_i18n": None
        })

    # Real-world applications section
    applications_html = "<h3>Real-World Applications</h3>\n"
    app_examples = []

    for q in quiz_data.get("quiz_questions", []):
        text = q.get("question_text", "")
        explanation = q.get("explanation", "")

        # Look for real-world contexts
        contexts = ["score", "sales", "age", "commute", "goal", "tip", "sleep", "cupcake", "exam"]
        if any(ctx in text.lower() for ctx in contexts):
            if text not in app_examples:
                applications_html += f"<p><b>Example:</b> {text}</p>\n"
                applications_html += f"<p>{explanation}</p>\n"
                app_examples.append(text)

    if len(app_examples) > 0:
        sections.append({
            "title": "Real-World Applications",
            "content_html": applications_html,
            "data_i18n": None
        })

    # Additional concepts section
    other_html = "<h3>Important Concepts</h3>\n"
    other_content = []

    for q in quiz_data.get("quiz_questions", []):
        text = q.get("question_text", "")
        explanation = q.get("explanation", "")

        # Look for special topics
        if any(term in text.lower() for term in ["bimodal", "weighted", "frequency", "skewed"]):
            if text not in other_content:
                other_html += f"<p><b>{text.strip('?')}</b></p>\n"
                other_html += f"<p>{explanation}</p>\n"
                other_content.append(text)

    if len(other_content) > 0:
        sections.append({
            "title": "Special Topics",
            "content_html": other_html,
            "data_i18n": None
        })

    return sections if sections else None

def process_quiz_file(quiz_path, summary_path):
    """Process a single quiz and update its corresponding summary."""
    try:
        # Read quiz file
        with open(quiz_path, 'r', encoding='utf-8') as f:
            quiz_data = json.load(f)

        # Normalize the quiz data to use "quiz_questions" key
        if "questions" in quiz_data and "quiz_questions" not in quiz_data:
            quiz_data["quiz_questions"] = quiz_data["questions"]

        # Generate new summary sections
        course = quiz_data.get("course", "")
        unit = quiz_data.get("unit", 1)
        lesson = quiz_data.get("lesson_number", "1")

        new_sections = generate_summary_from_quiz(quiz_data, course, unit, lesson)

        if not new_sections:
            return False

        # Read existing summary if it exists
        summary_data = {
            "unit": quiz_data.get("unit", 1),
            "lesson_number": quiz_data.get("lesson_number", ""),
            "title": quiz_data.get("title", ""),
            "course": quiz_data.get("course", ""),
            "summary_sections": new_sections
        }

        # Write updated summary
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)

        return True

    except Exception as e:
        print(f"Error processing {quiz_path}: {e}")
        return False

def main():
    """Process all quiz files and enhance their summaries."""
    content_data_path = Path("c:/Users/Peter/pkang6689-pixel.github.io/content_data")

    if not content_data_path.exists():
        print(f"Error: {content_data_path} does not exist")
        return

    # Find all quiz files
    quiz_files = list(content_data_path.glob("**/Lesson*_Quiz.json"))

    print(f"Found {len(quiz_files)} quiz files to process")

    processed = 0
    failed = 0

    for i, quiz_file in enumerate(quiz_files, 1):
        # Construct corresponding summary path
        summary_file = quiz_file.with_name(quiz_file.name.replace("_Quiz.json", "_Summary.json"))

        print(f"[{i}/{len(quiz_files)}] Processing {quiz_file.name}...", end=" ")

        if process_quiz_file(quiz_file, summary_file):
            print("[OK]")
            processed += 1
        else:
            print("[FAIL]")
            failed += 1

        # Progress indicator
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(quiz_files)} ({processed} successful, {failed} failed)")

    print(f"\n=== Summary ===")
    print(f"Total files: {len(quiz_files)}")
    print(f"Successfully updated: {processed}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    main()
