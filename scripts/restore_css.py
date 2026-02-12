import glob
import os
import re

ROOT_DIR = "ArisEdu Project Folder/ChemistryLessons"

# The broken Body CSS snippet
BROKEN_BODY_CSS = r"""
    body {
      box-sizing: border-box;
      background-color: white;
      
    }"""
# The Fixed Body CSS snippet
FIXED_BODY_CSS = r"""
    body {
      box-sizing: border-box;
      background-color: white;
      color: #0f172a;
    }"""

# The broken Quiz CSS snippet (using regex pattern to be safe)
# It has varying whitespace likely? read_file showed 2 blank lines.
# We will target the whole block starting from comment to the closing brace of dark mode rule.
# Note: In Unit1_Test.html, it was inserted before </head>.
BROKEN_QUIZ_CSS_REGEX = r"/\* Dark Mode Support for Quiz Finish Screen \*/\s*#quiz-finish-screen\s*\{\s*\s*\s*transition: background-color 0\.3s, color 0\.3s;\s*\}\s*body\.dark-mode #quiz-finish-screen\s*\{\s*background: #1e293b;\s*color: #e2e8f0;\s*box-shadow: 0 4px 6px rgba\(0,0,0,0\.3\);\s*\}"

# New Quiz CSS
FIXED_QUIZ_CSS = """
    /* Dark Mode Support for Quiz Finish Screen */
    #quiz-finish-screen {
        background: #f8fafc;
        color: #0f172a;
        transition: background-color 0.3s, color 0.3s;
    }
    #quiz-finish-screen h2 {
        color: #0f172a;
    }
    #quiz-finish-screen div {
        color: #334155;
    }
    body.dark-mode #quiz-finish-screen {
        background: #1e293b;
        color: #e2e8f0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    body.dark-mode #quiz-finish-screen h2 {
        color: #f8fafc;
    }
    body.dark-mode #quiz-finish-screen div {
        color: #cbd5e1;
    }
"""

def fix_css_issues():
    files = glob.glob(os.path.join(ROOT_DIR, "Unit*", "*_Test.html"))
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_len = len(content)
        
        # 1. Fix Body CSS
        # Try exact replacement first
        if "background-color: white;\n      \n    }" in content:
            content = content.replace("background-color: white;\n      \n    }", "background-color: white;\n      color: #0f172a;\n    }")
        else:
            # Fallback regex if whitespace differs slightly
             content = re.sub(r"background-color: white;\s+\}", "background-color: white;\n      color: #0f172a;\n    }", content)

        # 2. Fix Quiz CSS
        # Using DOTALL for multi-line matching
        match = re.search(BROKEN_QUIZ_CSS_REGEX, content, re.DOTALL)
        if match:
            content = content.replace(match.group(0), FIXED_QUIZ_CSS.strip())
        else:
            print(f"Warning: Broken Quiz CSS not found in {file_path}")
            # It might have been not broken exactly as expected, or already fixed?
            # Or maybe my regex is too strict on whitespace.
            # Let's try a simpler replacement if regex fails, targeting known unique lines.
            
            simpler_target = """
    #quiz-finish-screen {
        
        
        transition: background-color 0.3s, color 0.3s;
    }"""
            if simpler_target.strip() in content:
                 # Replacing just the first part and appending the rest?
                 # No, better to replacing carefully.
                 pass

        if len(content) != original_len or match:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed CSS in {file_path}")
        else:
             print(f"No changes in {file_path}")

if __name__ == "__main__":
    fix_css_issues()
