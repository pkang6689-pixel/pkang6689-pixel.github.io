import os

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        target_string = "localStorage.setItem('arisEduDarkMode', String(isDark));"
        
        if target_string in content:
            # Check if it's already updated
            if "window.applyArisTheme" in content and "String(isDark)" in content:
                 # It might be in another place, but let's be careful.
                 # The specific block we want to patch usually ends with the event listener closure
                 pass

            # We want to insert the call inside the event listener.
            # Typical structure:
            # checkbox.addEventListener('change', (event) => {
            #   const isDark = event.target.checked;
            #   localStorage.setItem('arisEduDarkMode', String(isDark));
            #   if (isDark) {
            #     document.body.classList.add('dark-mode');
            #   } else {
            #     document.body.classList.remove('dark-mode');
            #   }
            # });

            # We can simply append the call after the if/else block.
            
            search_pattern = """      if (isDark) {
        document.body.classList.add('dark-mode');
      } else {
        document.body.classList.remove('dark-mode');
      }"""
            
            replacement = """      if (isDark) {
        document.body.classList.add('dark-mode');
      } else {
        document.body.classList.remove('dark-mode');
      }
      if (window.applyArisTheme) { window.applyArisTheme(); }"""

            if search_pattern in content:
                new_content = content.replace(search_pattern, replacement)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
            else:
                print(f"Pattern not found exactly in {filepath}")
                # Fallback for slightly different indentation or formatting?
                # Most files seem generated/consistent.
                pass
                
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

def main():
    root_dir = '/workspaces/ArisEdu'
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                update_file(filepath)

if __name__ == '__main__':
    main()
