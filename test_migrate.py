import re

ARCADE_GAMES = [
    ('Game2048.html','2048'),('GameArena.html','Apocalypse Arena'),('GameAvoid.html','AVOIDance'),
    ('GameBlocks.html','Block Puzzle (Arcade)'),('GameBreakout.html','Breakout'),('GameBubble.html','Bubble Shooter'),
    ('GameCatch.html','Fruit Catcher'),('GameCraft2D.html','Craft 2D'),('GameFactory.html','Particle Clicker'),
    ('GameFlappy.html','Flappy Bird'),('GameJump.html','Runner'),('GameJumpMaster.html','Jump Master'),
    ('GameMemory.html','Card Match'),('GameMinesweeper.html','Minesweeper'),('GamePacman.html','Pac-Man'),
    ('GamePlatformer.html','Platformer'),('GamePong.html','Pong'),('GameReaction.html','Reaction Test'),
    ('GameShoot.html','Target Aim'),('GameSimon.html','Simon Memory'),('GameSnake.html','Snake'),
    ('GameSpaceship.html','Space Shooter'),('GameTetris.html','Tetris'),('GameTower.html','Lab Defense'),
    ('GameWhack.html','Whack A Mole'),
]
ARCADE_ITEMS = ''.join(
    f'<div class="Practices-panel-item"><a href="../../../games/{f}" target="_blank">{t}</a></div>'
    for f, t in ARCADE_GAMES
)

CLIMB_RE = re.compile(r'\n<div id="climb-game-container".*?(?=\n<style>\n\.mix-match-board)', re.DOTALL)
MIXMATCH_RE = re.compile(r'\n<style>\n\.mix-match-board.*?(?=<div id="blockpuzzle-container")', re.DOTALL)
CLIMB_ITEM_RE = re.compile(r'<div class="Practices-panel-item">\s*<a href="#climb">Boost</a>\s*</div>')
MIXMATCH_ITEM = '<div class="Practices-panel-item"><a href="#mixmatch">Mix &amp; Match</a></div>'
BLOCKPUZZLE_END = '<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div></div>'
BLOCKPUZZLE_NEW = '<div class="Practices-panel-item"><a href="#blockpuzzle">Block Puzzle</a></div>' + ARCADE_ITEMS + '</div>'

fp = 'ArisEdu Project Folder/CourseFiles/Algebra1Lessons/Unit1/Lesson1.1_Practice.html'
content = open(fp, encoding='utf-8').read()
orig_len = len(content)

n1 = CLIMB_RE.subn('', content); content = n1[0]
n2 = MIXMATCH_RE.subn('', content); content = n2[0]
n3 = CLIMB_ITEM_RE.subn('', content); content = n3[0]
content = content.replace(MIXMATCH_ITEM, '')
panel_ok = BLOCKPUZZLE_END in content
if panel_ok:
    content = content.replace(BLOCKPUZZLE_END, BLOCKPUZZLE_NEW)

print(f'climb removed: {n1[1]}  mixmatch removed: {n2[1]}  climb_item: {n3[1]}  panel_ok: {panel_ok}')
print(f'Size: {orig_len} -> {len(content)} (removed {orig_len - len(content)} chars)')

# Show the resulting panel
idx = content.find('class="Practices-panel"')
print('\n=== RESULTING PANEL ===')
print(content[max(0,idx-10):idx+800])

# Verify no climb/mixmatch remain
print('\nclimb-game-container still present:', 'climb-game-container' in content)
print('mixmatch-container still present:', 'mixmatch-container' in content)
print('Boost link still present:', '#climb' in content)
print('MixMatch link still present:', '#mixmatch' in content)
