import os
import re

def analyze_quizzes(root_dir):
    quiz_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith("_Quiz.html"):
                quiz_files.append(os.path.join(root, file))

    total_questions = 0
    total_radios = 0
    unique_questions = set()
    question_counts = {}

    # Regex to find the question block and extract the p tag content
    # Assuming the structure is <div class="quiz-question"...> <p ...> Question </p>
    # We use non-greedy matches.
    div_pattern = re.compile(r'<div\s+class=["\']quiz-question["\']')
    radio_pattern = re.compile(r'<input\s+type=["\']radio["\']')
    
    # Capture the content inside the p tag immediately following the div start
    # This is a bit heuristic. It looks for div with class quiz-question, then allows some whitespace/tags, 
    # then looks for a p tag and captures its content.
    question_pattern = re.compile(r'<div\s+class=["\']quiz-question["\'][^>]*>\s*<p[^>]*>(.*?)</p>', re.DOTALL | re.IGNORECASE)

    for file_path in quiz_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Count questions (divs)
            questions_in_file = len(div_pattern.findall(content))
            total_questions += questions_in_file
            
            # Count radios
            radios_in_file = len(radio_pattern.findall(content))
            total_radios += radios_in_file
            
            # Extract questions
            matches = question_pattern.findall(content)
            for match in matches:
                # Clean the text
                text = match.strip()
                # Remove number prefix like "1. ", "12. "
                cleaned_text = re.sub(r'^\d+\.\s*', '', text)
                unique_questions.add(cleaned_text)
                question_counts[cleaned_text] = question_counts.get(cleaned_text, 0) + 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"Total quiz files: {len(quiz_files)}")
    print(f"Total '<div class=\"quiz-question\">' occurrences (Total Questions): {total_questions}")
    print(f"Total '<input type=\"radio\">' occurrences (Total Options): {total_radios}")
    print(f"Unique questions found: {len(unique_questions)}")
    print("-" * 40)
    print("Unique Questions List (sorted):")
    sorted_questions = sorted(list(unique_questions))
    for q in sorted_questions:
        print(q)

if __name__ == "__main__":
    analyze_quizzes(os.path.join(os.path.dirname(__file__), ".."))
