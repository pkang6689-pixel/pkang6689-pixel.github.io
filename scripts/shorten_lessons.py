#!/usr/bin/env python3
"""
shorten_lessons.py — Strip duplicated inline HTML/JS from physics lesson files.

For each lesson .html file (not Summary, Practice, Quiz, or Test):
1. Remove the embedded practice view HTML (flashcard game, climb game, mix & match, block puzzle)
2. Remove the inline climb game JS (the big IIFE)
3. Remove the inline game switcher JS
4. Remove the inline climb CSS <style> block
5. Replace with script tags for: inject_games.js, climb_game.js, game_switcher.js
6. Keep the practice-content-view div with just its title

This keeps:
 - The <head> and lesson-content-view (unique per file)
 - The summary-content-view (unique placeholder per file)
 - The quiz-content-view (unique placeholder per file)  
 - All unique script references at the bottom
"""

import os
import re
import glob

BASE = "/workspaces/ArisEdu/ArisEdu Project Folder/PhysicsLessons"

# Find all main lesson files (not Summary, Practice, Quiz, Test)
pattern = os.path.join(BASE, "Unit*", "*.html")
all_files = sorted(glob.glob(pattern))
lesson_files = [f for f in all_files if ("_Video" in f or "PhysicsLesson" in f) and not any(x in f for x in ['Summary', '_Practice', '_Quiz', '_Test'])]

print(f"Found {len(lesson_files)} lesson files to process")

count = 0
errors = []

for filepath in lesson_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_len = len(content.splitlines())
        
        # --- 1. Replace the embedded practice view ---
        # The practice view starts with: <div id="practice-content-view" style="display: none;">
        # and contains everything up to <!-- Quiz View
        # We want to keep the div container with the title but remove the games HTML
        
        # Find the practice content view div
        practice_start = content.find('<div id="practice-content-view"')
        quiz_comment = content.find('<!-- Quiz View', practice_start) if practice_start != -1 else -1
        
        if practice_start != -1 and quiz_comment != -1:
            # Extract the title from within the practice view
            practice_section = content[practice_start:quiz_comment]
            title_match = re.search(r'<h2 class="page-title">(.*?)</h2>', practice_section)
            practice_title = title_match.group(1) if title_match else 'Practice'
            
            # Replace entire practice section with slim version
            new_practice = (
                '<div id="practice-content-view" style="display: none;">\n'
                f'<h2 class="page-title">{practice_title}</h2>\n'
                '</div>\n'
            )
            content = content[:practice_start] + new_practice + content[quiz_comment:]

        # --- 2. Remove inline climb game CSS (the <style> block within the practice area) ---
        # Pattern: <style> ... @keyframes twinkle ... climb-option-btn ... </style>
        # This may have been removed already with the practice view, but check for any remaining
        content = re.sub(
            r'<style>\s*\n\s*@keyframes twinkle.*?</style>',
            '',
            content,
            flags=re.DOTALL
        )

        # --- 3. Remove the inline game switcher script ---
        # Pattern: <script>\n  window.switchToClimb = ...  </script>
        content = re.sub(
            r'<script>\s*\n\s*window\.switchToClimb\s*=.*?</script>',
            '',
            content,
            flags=re.DOTALL
        )

        # --- 4. Remove the inline climb game logic script ---
        # Pattern: <script>\n// Climb Game Logic\n(function() { ... })();\n</script>
        content = re.sub(
            r'<script>\s*\n\s*// Climb Game Logic.*?</script>',
            '',
            content,
            flags=re.DOTALL
        )

        # --- 5. Add the new shared script tags before the closing </body> ---
        # Check if they're not already present
        new_scripts = ''
        if 'inject_games.js' not in content:
            new_scripts += '<script src="../../scripts/inject_games.js"></script>\n'
        if 'climb_game.js' not in content:
            new_scripts += '<script src="../../scripts/climb_game.js"></script>\n'
        if 'game_switcher.js' not in content:
            new_scripts += '<script src="../../scripts/game_switcher.js"></script>\n'

        if new_scripts:
            content = content.replace('</body>', new_scripts + '</body>')

        # --- 6. Clean up extra blank lines ---
        content = re.sub(r'\n{3,}', '\n\n', content)

        new_len = len(content.splitlines())

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        reduction = original_len - new_len
        print(f"  {os.path.basename(filepath)}: {original_len} -> {new_len} lines (saved {reduction})")
        count += 1

    except Exception as e:
        errors.append((filepath, str(e)))
        print(f"  ERROR: {os.path.basename(filepath)}: {e}")

print(f"\nDone! Processed {count} files.")
if errors:
    print(f"\nErrors ({len(errors)}):")
    for path, err in errors:
        print(f"  {os.path.basename(path)}: {err}")
