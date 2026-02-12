import os
import re

root_dir = "ArisEdu Project Folder/ChemistryLessons"

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return
    
    original_content = content
    
    # --- CSS Fix 1: .rubric-hover-wrap position & .rubric-hover-dot margin ---
    # Fix .rubric-hover-wrap: top: 0 -> top: 4.3rem
    pattern_wrap = r'(\.rubric-hover-wrap\s*\{\s*position:\s*absolute;\s*)top:\s*0;'
    if re.search(pattern_wrap, content):
        content = re.sub(pattern_wrap, r'\1top: 4.3rem;', content)
        
    # Fix .rubric-hover-dot: remove margin-top: 4.3rem
    pattern_dot = r'(\.rubric-hover-dot\s*\{[^}]*?)margin-top:\s*4\.3rem;\s*'
    if re.search(pattern_dot, content):
        content = re.sub(pattern_dot, r'\1', content)

    # --- CSS Fix 2: .rubric-hover-panel color ---
    pattern_panel_block = r'(\.rubric-hover-panel\s*\{[^}]*\})'
    def add_color_to_panel(match):
        block = match.group(1)
        if 'color: #e2e8f0;' not in block:
            return block.replace('background: #0f172a;', 'background: #0f172a;\n      color: #e2e8f0;')
        return block
    
    content = re.sub(pattern_panel_block, add_color_to_panel, content)

    # --- CSS Fix 3: .rubric-hover-panel p color ---
    pattern_p_block = r'(\.rubric-hover-panel\s*p\s*\{[^}]*\})'
    def add_color_to_p(match):
        block = match.group(1)
        if 'color: #fff;' not in block:
             # Just add it before closing brace
             return  block.rstrip('}') + '  color: #fff;\n    }'
        return block

    content = re.sub(pattern_p_block, add_color_to_p, content)

    # --- JS Fix 1: Initial Back Button ---
    # window.location.href = '/.../ChemistryUnit...html'; -> ../../chem.html
    # This regex is tricky, let's keep it somewhat broad but safe
    pattern_back_init = r"(document\.getElementById\('back-button'\)\.addEventListener\('click',\s*\(\)\s*=>\s*\{\s*window\.location\.href\s*=\s*['\"`])([^'\"`]+)(['\"`];\s*\}\);)"
    
    content = re.sub(pattern_back_init, r"\1../../chem.html\3", content)

    # --- JS Fix 2: Restore Back Button ---
    # restoreBtn.innerText = "← Back to Unit X" -> "← Back to Chemistry"
    # url -> ../../chem.html
    
    # We match roughly: restoreBtn.innerText = "..."; ... window.location.href = "...";
    # Note: The innerText might be "← Back to Unit 1", "← Back to Unit 2", etc.
    pattern_restore = r"(restoreBtn\.innerText\s*=\s*['\"`]← Back to )Unit \d+(['\"`];\s*[\s\S]*?window\.location\.href\s*=\s*['\"`])[^'\"`]+(['\"`];\s*\}\);)"
    
    if re.search(pattern_restore, content):
        content = re.sub(pattern_restore, r"\1Chemistry\2../../chem.html\3", content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))
