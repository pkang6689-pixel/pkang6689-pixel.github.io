from bs4 import BeautifulSoup

def main():
    filepath = '/workspaces/ArisEdu/vidRubric'
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    # Find all table data cells that might contain the video links (First column)
    # We can just iterate all 'a' tags or iterate rows to be safe.
    # Iterating rows is safer to ensure we are in the right table structure.
    
    rows = soup.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
            
        # First cell is Video Topic
        topic_cell = cells[0]
        link = topic_cell.find('a')
        
        if link and link.get('href'):
            href = link['href']
            # Update the text of the link to be the URL
            if link.string != href:
                link.string = href
                modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}: Replaced lesson names with URLs.")
    else:
        print("No changes needed.")

if __name__ == "__main__":
    main()
