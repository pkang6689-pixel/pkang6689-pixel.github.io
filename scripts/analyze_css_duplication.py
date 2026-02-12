import os
import re

# Define the source file to extract CSS from
SOURCE_FILE = 'ArisEdu Project Folder/PhysicsLessons/Unit9/PhysicsLesson9.4OpticalInstruments.html'
OUTPUT_CSS = 'ArisEdu Project Folder/styles/main.css'

def normalize_css(css_content):
    """Normalize CSS content by removing comments and extra whitespace."""
    # Remove CSS comments
    css = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    # Remove extra whitespace
    css = re.sub(r'\s+', ' ', css).strip()
    return css

def extract_style_block(filepath):
    """Extract content of the first <style> block found."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return None

def main():
    # 1. Extract CSS from source file
    source_css = extract_style_block(SOURCE_FILE)
    if not source_css:
        print(f"Could not extract CSS from {SOURCE_FILE}")
        return

    # Normalize source CSS for comparison
    normalized_source = normalize_css(source_css)
    
    # 2. Scan all HTML files
    matches = 0
    total_files = 0
    
    workspace_dir = 'ArisEdu Project Folder'
    
    for root, _, files in os.walk(workspace_dir):
        for file in files:
            if file.endswith('.html'):
                total_files += 1
                filepath = os.path.join(root, file)
                
                file_css = extract_style_block(filepath)
                if file_css:
                    normalized_file = normalize_css(file_css)
                    
                    # Simple check: does the file content contain the unique first few lines of the source CSS?
                    start_marker = normalized_source[:200]
                    if start_marker in normalized_file:
                        matches += 1
                        # print(f"Match: {filepath}")
                    else:
                        pass # print(f"No match: {filepath}")

    print(f"Total HTML files: {total_files}")
    print(f"Files with matching CSS base: {matches}")

if __name__ == "__main__":
    main()
