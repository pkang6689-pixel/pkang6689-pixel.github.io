import os

def count_lines_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def count_lines_in_directory(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.html', '.css', '.json', '.sh', '.txt')) or file == 'index.html':
                total_lines += count_lines_in_file(os.path.join(root, file))
    return total_lines

if __name__ == "__main__":
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    total = count_lines_in_directory(workspace_dir)
    print(f"Total lines of code: {total}")
