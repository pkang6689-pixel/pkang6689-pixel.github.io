import os
import re

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find existing translation scripts (Clean up old inline ones)
        # Matches <script>...(function(){ const translations = ...</script>
        pattern = re.compile(r'<script>\s*\(function\(\)\{\s*const translations = \{.*?\};\s*function translateNode.*?\}\)\(\);\s*</script>', re.DOTALL)
        new_content = re.sub(pattern, '', content)
        
        # Also clean up the simpler version if it exists
        pattern_simple = re.compile(r'<script>\s*\(function\(\)\{\s*const translations = \{.*?\};\s*function translateNode.*?window\.addEventListener\("DOMContentLoaded", translateAll\);\s*\}\)\(\);\s*</script>', re.DOTALL)
        new_content = re.sub(pattern_simple, '', new_content)

        # Remove duplicate new script if already there
        new_script_tag = '<script src="/global_translations.js"></script>'
        new_content = new_content.replace(new_script_tag, '')

        # Use new script tag
        script_to_inject = f'\n    {new_script_tag}'

        # Insert logic
        # 1. Before search_data.js (preferred)
        # 2. Before body end
        
        if '<script src="../search_data.js">' in new_content:
             new_content = new_content.replace('<script src="../search_data.js">', script_to_inject + '\n    <script src="../search_data.js">')
        elif '<script src="search_data.js">' in new_content:
             new_content = new_content.replace('<script src="search_data.js">', script_to_inject + '\n    <script src="search_data.js">')
        elif '<script src="/_sdk/element_sdk.js">' in new_content:
             # Inject after sdk
             new_content = new_content.replace('<script src="/_sdk/element_sdk.js"></script>', '<script src="/_sdk/element_sdk.js"></script>' + script_to_inject)
        elif '</body>' in new_content:
             new_content = new_content.replace('</body>', script_to_inject + '\n</body>')
        else:
             new_content += script_to_inject

        # Clean up double empty lines
        new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
             pass

    except Exception as e:
        print(f"Error updating {filepath}: {e}")

def main():
    root_dir = '..'
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'node_modules' in dirpath: continue
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                update_file(filepath)
                count += 1
    print(f"Processed {count} files.")

if __name__ == '__main__':
    main()
