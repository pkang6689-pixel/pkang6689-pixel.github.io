from bs4 import BeautifulSoup
import urllib.parse

def add_timestamps():
    file_path = '/workspaces/ArisEdu/vidRubric'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    
    # Locate the rubric table
    table = soup.find('table', id='rubric-table')
    if not table:
        print("Could not find table with id 'rubric-table'")
        return

    rows = table.find_all('tr')
    count = 0

    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        
        # First column is Video Topic
        topic_cell = cells[0]
        link = topic_cell.find('a')
        
        if link and link.get('href'):
            url = link['href']
            parsed_url = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            
            if 't' in query_params:
                timestamp = query_params['t'][0]
                # Check if timestamp is already in the text to avoid double adding
                current_text = link.string.strip() if link.string else ""
                if f"[{timestamp}]" not in current_text:
                    new_text = f"{current_text} [{timestamp}]"
                    link.string = new_text
                    count += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Updated {count} links with timestamps.")

if __name__ == "__main__":
    add_timestamps()
