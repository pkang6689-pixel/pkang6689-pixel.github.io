import os
import re
import json

def extract_quiz_content(root_dir):
    unique_strings = set()
    quiz_files = []

    # Regex for question paragraph: <p ...>1. Question text</p>
    # Captures: 1=Number (optional), 2=Text
    # We look for <p inside a div with class quiz-question, but simpler to just search
    # for the pattern roughly if we assume the files are fairly clean.
    # However, to be safer, we should look for the context of "quiz-question".
    
    # Python's re doesn't support variable length lookbehind, so we'll confirm structure
    # by finding chunks or just matching reasonably specific patterns.
    
    # Strategy:
    # 1. Find blocks <div class="quiz-question" ...> ... </div> (this might include nested divs, risky with regex)
    # 2. Alternatively, just find <p ...>...</p> and <label ...>...</label> within the file.
    #    Since these appear to be specific to the quiz structure in these files, global search in file might be okay
    #    BUT we want to be sure we are inside a quiz question.
    
    # Let's try a slightly more robust regex approach that iterates over matches.
    
    # Pattern for Question:
    # <p[^>]*>\s*(?:\d+\.\s*)?([^<]+)</p>
    # Note: extracting ([^<]+) might be too simple if there are inner tags (like <b>), 
    # but based on the sample, it looks like plain text.
    # Let's allow for inner tags just in case: <p[^>]*>\s*(?:\d+\.\s*)?(.*?)</p>
    
    # Pattern for Answer:
    # <label[^>]*>\s*<input[^>]*>\s*(.*?)\s*</label>
    
    # Let's refine the "Question" regex to be more specific to the style in the file
    # <p style="font-weight: 700; ...">1. Question</p>
    
    p_regex = re.compile(r'<p[^>]*>\s*(?:(\d+)\.\s*)?(.*?)</p>', re.DOTALL | re.IGNORECASE)
    label_regex = re.compile(r'<label[^>]*>\s*<input[^>]*>\s*(.*?)\s*</label>', re.DOTALL | re.IGNORECASE)

    count = 0 
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip node_modules or hidden dirs if any
        if 'node_modules' in dirnames:
            dirnames.remove('node_modules')
            
        for filename in filenames:
            if filename.endswith('_Quiz.html'):
                file_path = os.path.join(dirpath, filename)
                quiz_files.append(file_path)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Find all quiz-question divs is hard with regex (nested divs).
                        # But we can split by 'class="quiz-question"' or similar.
                        # However, global match for the p and label patterns should be distinct enough 
                        # IF we are sure these patterns don't appear elsewhere.
                        # In the provided file, <p> with that style and <label> with input are quite specific.
                        
                        # Let's iterate through the file content to be slightly safer.
                        # We can find all occurrences of 'class="quiz-question"' and then look at the following text? No.
                        
                        # Let's just Regex strings.
                        # Questions often start with a number.
                        # We only want <p> tags that look like questions. 
                        # In the sample: <p style="font-weight: 700; ...">
                        # Answers: <label ...> <input ...> Text </label>
                        
                        # Extract Questions
                        # We might pick up non-question <p> tags. 
                        # The sample shows wrapper: <div class="quiz-question" ...>
                        # We can try to match the content inside the simple <div> structure if it's not nested deeply.
                        # Valid assumption: The quiz-question div contains the <p> and <labels> directly as children or close descendants.
                        
                        # Let's use string partitioning to find blocks of quiz-questions.
                        blocks = content.split('class="quiz-question"')
                        if len(blocks) > 1:
                            # Skip header/first block
                            for block in blocks[1:]:
                                # The block continues until the next quiz-question or end of file.
                                # Be careful not to overrun into footer etc. 
                                # But usually the next class="quiz-question" starts the next one.
                                # The last block might contain footer garbage. 
                                # We can limit the block search to the immediate vicinity.
                                
                                # Search for the Question <p>
                                # It's usually the first <p> in the block.
                                p_match = p_regex.search(block)
                                if p_match:
                                    # Group 2 is the text
                                    q_text = p_match.group(2).strip()
                                    # Remove HTML tags if any
                                    q_text_clean = re.sub(r'<[^>]+>', '', q_text).strip()
                                    if q_text_clean:
                                        unique_strings.add(q_text_clean)
                                
                                # Search for Answers <label>
                                # There are multiple labels.
                                # We can't easily limit "block" end without parsing HTML structure </div>.
                                # But we can verify "label" is somewhat close?
                                # Actually, just finding all labels in the block (which goes to end of file effectively) 
                                # is risky if we process the same content multiple times.
                                # Splitting by 'class="quiz-question"' makes blocks[i] contain EVERYTHING after it until end string,
                                # wait, split consumes the separator.
                                # So blocks[1] is from first question start to second question start (roughly).
                                # So finding all labels in blocks[i] (except the last one which runs to EOF) is mostly safe,
                                # assuming no other forms with labels exist in the footer.
                                
                                # Let's handle the last block carefully or just filter labels that look like quiz answers.
                                # Quiz answers have <input type="radio" ...>
                                
                                label_matches = label_regex.findall(block)
                                for ans_text in label_matches:
                                    ans_text_clean = re.sub(r'<[^>]+>', '', ans_text).strip()
                                    if ans_text_clean:
                                        unique_strings.add(ans_text_clean)
                                        
                        else:
                            # Fallback if class not found or different structure?
                            # Maybe try global regex if split fails to find anything.
                            pass

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Convert to sorted list
    sorted_strings = sorted(list(unique_strings))
    
    # Save to JSON
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quiz_strings_en.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(sorted_strings, f, indent=4, ensure_ascii=False)
    
    print(f"Found {len(sorted_strings)} unique strings.")
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    root_folder = os.path.join(os.getcwd(), "ArisEdu Project Folder")
    extract_quiz_content(root_folder)
