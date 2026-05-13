"""
migrate_practice_games.py
Removes the Climb game and Mix & Match game from all practice files,
then adds all Arcade games to the "Other games" dropdown.

Files affected: ~826 practice files that currently contain these game sections.
"""

import os
import re
import glob

COURSE_FILES = r"C:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\CourseFiles"

ARCADE_GAMES = [
    ("Game2048.html",        "2048"),
    ("GameArena.html",       "Apocalypse Arena"),
    ("GameAvoid.html",       "AVOIDance"),
    ("GameBlocks.html",      "Block Puzzle (Arcade)"),
    ("GameBreakout.html",    "Breakout"),
    ("GameBubble.html",      "Bubble Shooter"),
    ("GameCatch.html",       "Fruit Catcher"),
    ("GameCraft2D.html",     "Craft 2D"),
    ("GameFactory.html",     "Particle Clicker"),
    ("GameFlappy.html",      "Flappy Bird"),
    ("GameJump.html",        "Runner"),
    ("GameJumpMaster.html",  "Jump Master"),
    ("GameMemory.html",      "Card Match"),
    ("GameMinesweeper.html", "Minesweeper"),
    ("GamePacman.html",      "Pac-Man"),
    ("GamePlatformer.html",  "Platformer"),
    ("GamePong.html",        "Pong"),
    ("GameReaction.html",    "Reaction Test"),
    ("GameShoot.html",       "Target Aim"),
    ("GameSimon.html",       "Simon Memory"),
    ("GameSnake.html",       "Snake"),
    ("GameSpaceship.html",   "Space Shooter"),
    ("GameTetris.html",      "Tetris"),
    ("GameTower.html",       "Lab Defense"),
    ("GameWhack.html",       "Whack A Mole"),
]

# Build arcade game HTML for dropdown
ARCADE_ITEMS = ''.join(
    f'<div class="Practices-panel-item">'
    f'<a href="../../../games/{fname}" target="_blank">{title}</a>'
    f'</div>'
    for fname, title in ARCADE_GAMES
)


# ── Patterns ─────────────────────────────────────────────────────────────────

# 1. Climb game: from its opening div to just before the MixMatch <style> block
CLIMB_RE = re.compile(
    r'\n<div id="climb-game-container".*?(?=\n<style>\n\.mix-match-board)',
    re.DOTALL
)

# 2. MixMatch: the separate CSS <style> block + the container div,
#    up to (but not including) <div id="blockpuzzle-container"
MIXMATCH_RE = re.compile(
    r'\n<style>\n\.mix-match-board.*?(?=<div id="blockpuzzle-container")',
    re.DOTALL
)

# 3. Climb item in dropdown (multi-line format)
CLIMB_ITEM_RE = re.compile(
    r'<div class="Practices-panel-item">\s*<a href="#climb">Boost</a>\s*</div>'
)

# 4. MixMatch item in dropdown (inline format)
MIXMATCH_ITEM = '<div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div>'

# 5. Block Puzzle item + panel-closing </div> → insert arcade items in between
BLOCKPUZZLE_PANEL_END = '<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div></div>'
BLOCKPUZZLE_PANEL_NEW = (
    '<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>'
    + ARCADE_ITEMS
    + '</div>'
)


def process_file(filepath, dry_run=False):
    """
    Returns True if the file was (or would be) modified.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only process files that have all three game sections
    if 'id="climb-game-container"' not in content:
        return False

    original = content

    # Step 1 – remove Climb game HTML + its embedded CSS
    content, n1 = CLIMB_RE.subn('', content)

    # Step 2 – remove MixMatch CSS block + MixMatch container HTML
    content, n2 = MIXMATCH_RE.subn('', content)

    # Step 3 – remove Climb item from dropdown
    content, n3 = CLIMB_ITEM_RE.subn('', content)

    # Step 4 – remove MixMatch item from dropdown
    content = content.replace(MIXMATCH_ITEM, '')
    n4 = 1 if MIXMATCH_ITEM in original else 0

    # Step 5 – insert arcade game links after Block Puzzle in dropdown
    if BLOCKPUZZLE_PANEL_END in content:
        content = content.replace(BLOCKPUZZLE_PANEL_END, BLOCKPUZZLE_PANEL_NEW)
        n5 = 1
    else:
        n5 = 0

    if content == original:
        return False

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return True


def main(dry_run=False):
    label = "[DRY RUN] " if dry_run else ""
    practice_files = glob.glob(
        os.path.join(COURSE_FILES, '**', '*_Practice.html'), recursive=True
    )
    print(f"{label}Total practice files found: {len(practice_files)}")

    modified = 0
    skipped = 0
    errors = []

    for i, fp in enumerate(practice_files):
        try:
            if process_file(fp, dry_run=dry_run):
                modified += 1
            else:
                skipped += 1
        except Exception as e:
            errors.append((fp, str(e)))
        if (i + 1) % 200 == 0:
            print(f"  ...processed {i + 1}/{len(practice_files)}")

    print(f"\n{label}Modified : {modified}")
    print(f"{label}Skipped  : {skipped} (no games to remove)")
    print(f"{label}Errors   : {len(errors)}")
    if errors:
        for fp, err in errors[:10]:
            print(f"  ERROR: {os.path.basename(fp)} — {err}")


if __name__ == '__main__':
    import sys
    dry = '--dry-run' in sys.argv
    main(dry_run=dry)
