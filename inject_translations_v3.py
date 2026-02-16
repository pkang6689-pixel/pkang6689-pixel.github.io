import json
import re
import os

translation_file = "/workspaces/ArisEdu/ArisEdu Project Folder/scripts/global_translations.js"

new_translations = {
    # Climb Game
    "No flashcards found for this lesson!": "未找到本课的抽认卡！",
    "Correct! Adding fuel...": "正确！正在添加燃料...",
    "Oops! Slipping down...": "哎呀！滑下来了...",
    "🏆 New High Score! 🏆": "🏆这也是新高分！🏆",
    "Best:": "最佳:",
    "Game Over": "游戏结束", # ensuring it is there
    "Score:": "分数:",
    "Attempts left:": "剩余尝试次数：",
    "Incorrect. The correct answer was option": "不正确。正确答案是选项",
    "Incorrect. Try again!": "不正确。请重试！",
    "Correct! Great job.": "正确！做得好。",
    "Please select an answer first.": "请先选择一个答案。",
    "Startup Error: ": "启动错误：",
    "Game Module Failed": "游戏模块失败",
    "👁️ View BG": "👁️ 查看背景",
    "🔙 Settings": "🔙 设置"
}

try:
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for the object definition
    match = re.search(r'const translations\s*=\s*({[\s\S]*?});', content)
    if not match:
        match = re.search(r'window\.globalTranslations\s*=\s*({[\s\S]*?});', content)
        
    if not match:
        print("Error: Could not find translation object in file")
        exit(1)
        
    json_str = match.group(1)
    
    # Try parsing
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        json_str_fixed = re.sub(r',\s*}', '}', json_str)
        try:
             data = json.loads(json_str_fixed)
        except:
             print("Fatal: Cannot parse JSON.")
             exit(1)

    # Update data
    added_count = 0
    for key, value in new_translations.items():
        if key not in data:
            data[key] = value
            added_count += 1
            
    print(f"Added {added_count} new translations.")
    
    new_json_str = json.dumps(data, indent=2, ensure_ascii=False)
    new_content = content.replace(match.group(1), new_json_str)
    
    with open(translation_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
except Exception as e:
    print(f"An error occurred: {e}")
