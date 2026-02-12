import os
import re
from bs4 import BeautifulSoup
import urllib.parse

RUBRIC_PATH = '/workspaces/ArisEdu/vidRubric'
LESSONS_DIR = '/workspaces/ArisEdu/ArisEdu Project Folder/ChemistryLessons/Unit1'

def parse_rubric():
    with open(RUBRIC_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', id='rubric-table')
    
    lessons_data = {}
    
    # Skip header
    rows = table.find_all('tr')[1:] 
    
    for row in rows:
        cells = row.find_all('td')
        if not cells or len(cells) < 7:
            continue
            
        # Parse Link/Topic
        # Column 0: Video Topic (contains Link often)
        link_tag = cells[0].find('a')
        if not link_tag:
            # If no link, skip it as we can't embed it
            continue
            
        video_url = link_tag['href']
        
        # Parse Lesson Number
        lesson_num = cells[1].get_text(strip=True).replace(' ⭐', '') # remove star if present
        
        # Parse Creator
        creator = cells[2].get_text(strip=True)
        
        # Parse Ratings (Text and Color)
        # Col 3: Difficulty
        diff_cell = cells[3]
        diff_text = diff_cell.get_text(strip=True)
        diff_color_style = diff_cell.get('style', '')
        diff_color = extract_color(diff_color_style)
        
        # Col 4: Detail
        detail_cell = cells[4]
        detail_text = detail_cell.get_text(strip=True)
        detail_color_style = detail_cell.get('style', '')
        detail_color = extract_color(detail_color_style)
        
        # Col 5: Length
        length_cell = cells[5]
        length_text = length_cell.get_text(strip=True)
        length_color_style = length_cell.get('style', '')
        length_color = extract_color(length_color_style)

        # Col 6: Pace
        pace_cell = cells[6]
        pace_text = pace_cell.get_text(strip=True)
        pace_color_style = pace_cell.get('style', '')
        pace_color = extract_color(pace_color_style)

        video_data = {
            'url': video_url,
            'creator': creator,
            'difficulty': {'text': diff_text, 'color': diff_color},
            'detail': {'text': detail_text, 'color': detail_color},
            'length': {'text': length_text, 'color': length_color},
            'pace': {'text': pace_text, 'color': pace_color}
        }
        
        if lesson_num not in lessons_data:
            lessons_data[lesson_num] = []
        lessons_data[lesson_num].append(video_data)
        
    return lessons_data

def extract_color(style_str):
    if not style_str:
        return ''
    match = re.search(r'background\s*:\s*(#[0-9a-fA-F]{6}|[a-zA-Z]+)', style_str)
    if match:
        return match.group(1)
    return ''

def convert_to_embed_url(watch_url):
    parsed = urllib.parse.urlparse(watch_url)
    query = urllib.parse.parse_qs(parsed.query)
    video_id = query.get('v', [None])[0]
    
    if not video_id:
        return None, None
        
    embed_src = f"https://www.youtube.com/embed/{video_id}"
    
    start_time = query.get('t', [None])[0]
    if start_time:
        # Convert 1s, 440s to just integers
        seconds = start_time.replace('s', '')
        embed_src += f"?start={seconds}"
        
    return embed_src, video_id

def create_panel_item_html(soup, video_info):
    embed_src, video_id = convert_to_embed_url(video_info['url'])
    if not embed_src:
        return None

    # Outer div
    item_div = soup.new_tag('div', attrs={'class': 'videos-panel-item'})
    
    # Anchor tag
    a_tag = soup.new_tag('a', href=video_info['url'])
    
    # Set data attributes
    a_tag['data-rating-difficulty'] = video_info['difficulty']['text']
    a_tag['data-color-difficulty'] = video_info['difficulty']['color']
    
    a_tag['data-rating-detail'] = video_info['detail']['text']
    a_tag['data-color-detail'] = video_info['detail']['color']
    
    a_tag['data-rating-speed'] = video_info['length']['text']
    a_tag['data-color-speed'] = video_info['length']['color']
    
    a_tag['data-rating-pace'] = video_info['pace']['text']
    a_tag['data-color-pace'] = video_info['pace']['color']
    
    title_text = f"{video_info['creator']}: {video_info['difficulty']['text']} / {video_info['length']['text']}" # Or just creator?
    # Actually, looking at previous HTML it was "Khan Academy: Classification of Matter"
    # We don't have titles in rubric easily, rubric topic is sometimes link itself now.
    # Let's use "Creator: Lesson Topic" if possible, or just "Creator".
    # The file example uses "Khan Academy".
    a_tag['data-video-title'] = f"{video_info['creator']}"
    a_tag['data-video-src'] = embed_src
    a_tag['data-video-id'] = video_id
    
    a_tag.string = video_info['creator']
    
    item_div.append(a_tag)
    
    # Mini rubric div
    rubric_div = soup.new_tag('div', attrs={'class': 'mini-rubric', 'aria-hidden': 'true'})
    
    for cat in ['difficulty', 'detail', 'length', 'pace']:
        color = video_info[cat]['color']
        span = soup.new_tag('span', style=f"background:{color}" if color else "")
        rubric_div.append(span)
        
    item_div.append(rubric_div)
    
    return item_div

def process_files():
    rubric_data = parse_rubric()
    
    for filename in os.listdir(LESSONS_DIR):
        if not filename.endswith('.html') or 'Lesson' not in filename:
            continue
            
        # Extract lesson number "1.1", "1.2" etc.
        match = re.search(r'Lesson\s+(\d+\.\d+)', filename)
        if not match:
            continue
            
        lesson_num = match.group(1)
        
        if lesson_num not in rubric_data:
            print(f"No rubric data for {lesson_num}")
            continue
            
        videos = rubric_data[lesson_num]
        if not videos:
            print(f"Empty video list for {lesson_num}")
            continue
            
        file_path = os.path.join(LESSONS_DIR, filename)
        print(f"Processing {filename}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Update Videos Panel
        panel = soup.find('div', class_='videos-panel')
        if panel:
            # Find title to preserve it
            title_div = panel.find('div', class_='videos-panel-title')
            # Clear everything
            panel.clear()
            # Restore title
            if title_div:
                panel.append(title_div)
            else:
                new_title = soup.new_tag('div', attrs={'class': 'videos-panel-title'})
                new_title.string = f"Lesson {lesson_num} videos"
                panel.append(new_title)
                
            # Add new items
            for vid in videos:
                new_item = create_panel_item_html(soup, vid)
                if new_item:
                    panel.append(new_item)
        
        # 2. Update Main Embed (First video)
        first_video = videos[0]
        embed_src, _ = convert_to_embed_url(first_video['url'])
        
        if embed_src:
            video_embed_div = soup.find('div', class_='video-embed')
            if video_embed_div:
                iframe = video_embed_div.find('iframe')
                if iframe:
                    iframe['src'] = embed_src
                    # Update title if possible
                    iframe['title'] = f"{first_video['creator']} Video"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

if __name__ == "__main__":
    process_files()
