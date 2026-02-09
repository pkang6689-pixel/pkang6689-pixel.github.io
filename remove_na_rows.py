from bs4 import BeautifulSoup

def main():
    filepath =('/workspaces/ArisEdu/vidRubric')
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    soup = BeautifulSoup(content, 'html.parser')
    modified = False
    
    # Find all table rows
    rows = soup.find_all('tr')
    
    deleted_count = 0
    
    for row in rows:
        # Check if "N/A" is in the row text
        # Getting text from the whole row
        row_text = row.get_text()
        
        if "N/A" in row_text:
            row.decompose()
            modified = True
            deleted_count += 1

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filepath}. Removed {deleted_count} rows containing 'N/A'.")
    else:
        print("No rows with 'N/A' found.")

if __name__ == "__main__":
    main()
