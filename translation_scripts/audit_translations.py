import os
import re
import json

project_root = "../ArisEdu Project Folder"
translation_file = os.path.join(project_root, "scripts/global_translations.js")

# Load existing translations
try:
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content) or             re.search(r'window\.globalTranslations\s*=\s*({[\s\S]*?});', content)
    
    if match:
        # Use loose parsing to get keys
        raw_json = match.group(1)
        # Extract keys using regex as json.loads might fail on comments/syntax
        # Keys are "Key": "Value" or 'Key': "Value"
        existing_keys = set(re.findall(r'["\'](.*?)["\']\s*:', raw_json))
        # Add keys that might have been missed by simple regex
        try:
             import ast
             # Try to evaluate the dict literal using ast.literal_eval if possible, 
             # but it might conform to JS not Py.
             pass
        except:
             pass
    else:
        existing_keys = set()
except Exception as e:
    print(f"Error loading translations: {e}")
    existing_keys = set()

print(f"Loaded {len(existing_keys)} existing translation keys.")

# Patterns to find user-facing strings
html_text_pattern = re.compile(r'>([^<]+)<')
js_string_pattern = re.compile(r'["\']([^"\']+)["\']')

# Exclusions
stopwords = {'Start', 'End', 'utf-8', 'viewport', 'width', 'height', 'style', 'script', 'link', 'rel', 'href', 'src', 'type', 'class', 'id', 'name', 'value', 'data', 'br', 'div', 'span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ul', 'ol', 'table', 'tr', 'td', 'th', 'form', 'input', 'button', 'a', 'img', 'header', 'footer', 'main', 'section', 'nav', 'aside', 'article', 'details', 'summary', 'dialog', 'menu', 'menuitem', 'b', 'i', 'u', 's', 'strong', 'em', 'code', 'pre', 'blockquote', 'q', 'cite', 'abbr', 'acronym', 'address', 'time', 'date', 'datetime', 'ins', 'del', 'var', 'samp', 'kbd', 'tt', 'sup', 'sub', 'big', 'small', 'top', 'middle', 'bottom', 'left', 'right', 'center', 'justify', 'inherit', 'initial', 'unset', 'none', 'block', 'inline', 'inline-block', 'flex', 'grid', 'table-cell', 'table-row', 'table-column', 'table-caption', 'list-item', 'run-in', 'compact', 'marker', 'inside', 'outside', 'disc', 'circle', 'square', 'decimal', 'decimal-leading-zero', 'lower-roman', 'upper-roman', 'lower-greek', 'lower-latin', 'upper-latin', 'armenian', 'georgian', 'hebrew', 'hiragana', 'katakana', 'hiragana-iroha', 'katakana-iroha'}

candidates = set()

# Traverse
for root, dirs, files in os.walk(project_root):
    if 'Archive' in root or '_Templates' in root or '.git' in root or 'node_modules' in root:
        continue
        
    for file in files:
        path = os.path.join(root, file)
        
        if file.endswith('.html'):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    matches = html_text_pattern.findall(text)
                    for m in matches:
                        s = m.strip()
                        if s and len(s) > 2 and not s.startswith('{') and not s.startswith('arisedu') and not s.startswith('http'):
                            candidates.add(s)
            except: pass
            
        elif file.endswith('.js') and not file == 'global_translations.js' and not file == 'search_data.js':
            # JS is harder, lots of noise. Skip for now or be very selective.
            # Maybe just look for specific variable assignments?
            pass

# Filter candidates
missing = []
for c in candidates:
    # Cleanup
    c_clean = c.strip()
    # Check if translated
    if c_clean not in existing_keys:
        # Heuristic: must contain at least one letter
        if re.search(r'[A-Za-z]', c_clean):
             missing.append(c_clean)

# Print top missing
print(f"Found {len(missing)} potentially missing translations.")
for m in sorted(missing)[:50]:
    print(f"MISSING: {m}")

