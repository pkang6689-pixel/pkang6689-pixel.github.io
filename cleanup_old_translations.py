"""
cleanup_old_translations.py
=============================
Removes leftover old translation script tags that weren't caught
by the first migration pass (e.g. tags with charset attribute).
"""

import os
import re
import glob

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
ARIS_DIR = os.path.join(REPO_ROOT, "ArisEdu Project Folder")

# Broader patterns to catch all variations
OLD_PATTERNS = [
    r'\s*<script[^>]*src="[^"]*global_translations\.js[^"]*"[^>]*>\s*</script>\s*\n?',
    r'\s*<script[^>]*src="[^"]*spanish_translations\.js[^"]*"[^>]*>\s*</script>\s*\n?',
    r'\s*<script[^>]*src="[^"]*hindi_translations\.js[^"]*"[^>]*>\s*</script>\s*\n?',
]

def main():
    log_path = os.path.join(REPO_ROOT, "cleanup_log.txt")
    log = open(log_path, "w", encoding="utf-8")

    html_files = glob.glob(os.path.join(ARIS_DIR, "**", "*.html"), recursive=True)
    html_files.sort()

    cleaned = 0
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original = content
        for pat in OLD_PATTERNS:
            content = re.sub(pat, "\n", content)

        # Clean up multiple blank lines that might result
        content = re.sub(r'\n{3,}', '\n\n', content)

        if content != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            rel = os.path.relpath(filepath, REPO_ROOT).replace("\\", "/")
            log.write(f"  CLEANED  {rel}\n")
            cleaned += 1

    log.write(f"\nDone! Cleaned {cleaned} files.\n")
    log.close()
    print(f"Done! Cleaned {cleaned} files. See {log_path}")


if __name__ == "__main__":
    main()
