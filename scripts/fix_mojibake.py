import json
import re

FILE_PATH = r"c:\Users\Peter\pkang6689-pixel.github.io\ArisEdu Project Folder\scripts\global_translations.js"

def fix_mojibake(text):
    try:
        # The specific corruption seen: UTF-8 bytes interpreted as CP437
        # e.g. "₂" (E2 82 82) -> "Γéé"
        fixed = text.encode('cp437').decode('utf-8')
        return fixed
    except UnicodeEncodeError:
        return text
    except UnicodeDecodeError:
        return text

def main():
    print(f"Reading {FILE_PATH}...")
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Strategy: Find strings that explicitly contain the corrupted Gamma character '\u0393'
    # and attempt to fix them.
    # We use a regex to capture "Key": "Value" pairs to be safe, or just replace globally?
    # Global replacement might be safer if we target the specific mojibake sequences.
    
    # Common mojibake patterns based on observation:
    # Γéé -> ₂
    # Γéâ -> ₃
    # ΓåÆ -> →
    # ΓÇö -> —
    # ΓÜÖ∩╕Å -> ⚙️
    # ΓÜí -> ⚡
    # Γ¡É -> ⭐
    # Γü┤ -> ⁴ (E2 81 B4 -> Γ ü ┤)
    # ┬│ -> ³ (C2 B3 -> ┬ │) - Wait, C2 in CP437 is ┬, B3 is │. Correct.
    
    # Let's try to fix line by line to be safer and report changes
    lines = content.split('\n')
    new_lines = []
    changes = 0
    
    for line in lines:
        if 'Γ' in line or '┬' in line: # fast check for likely mojibake
            old_line = line
            
            # Attempt fix on the whole line? 
            # DANGER: Valid characters might be outside CP437 and cause encode error, 
            # causing the whole line fix to fail even if a substring is fixable.
            # We should fallback to regex replacement or chunking.
            
            # Better approach: Find quoted strings and try to fix them individually
            # But the corruption might cross quote boundaries? Unlikely for this file format.
            
            # Regex to find potential mojibake sequences
            # We look for sequences containing likely mojibake chars from CP437
            # Gamma (0393), etc.
            
            def replace_callback(match):
                g = match.group(0)
                return fix_mojibake(g)

            # A simplistic regex for words containing these chars
            # But "Γéé" is multiple chars.
            # Let's try to fix the string literals inside the line.
            
            # Find content inside quotes
            # We can use the fact that the file is JS object properties.
            # "Key": "Value",
            
            match = re.match(r'^(\s*["\'])(.+)["\']\s*:\s*["\'](.+)["\'],?$', line)
            if match:
                prefix = match.group(1) # indentation + quote
                key = match.group(2)
                val = match.group(3) # This might have the end quote if regex is not greedy enough, but .+ is greedy.
                
                # The regex above is a bit loose. Let's rely on exact replacement for known corrupted substrings if general fix fails.
                
                # Try to fix key
                fixed_key = fix_mojibake(key)
                
                # Optimization: if key was fixed, we use it.
                if fixed_key != key:
                    # Construct new line (careful with quotes and commas)
                    # We need to preserve the original line structure exactly
                    pass

            # Alternative: Just replace known sequences globally which is safer than blind encoding
            # But there are too many combinations (UTF-8 is huge).
            
            # Let's try to fix the *entire* line content if it contains specific markers
            # But we must handle the UnicodeDecodeError if the line contains valid chars that aren't CP437 compatible?
            # Actually, `encode('cp437')` will fail if the line has Chinese chars (which it does).
            # So we CANNOT encode the whole line.
            
            # We must isolate the corrupted parts.
            # The corrupted parts are composed of CP437 characters.
            # Identifying "chunks of CP437 characters that form valid UTF-8" is the goal.
            
            # Heuristic: Scan for sequences of characters that map to 'cp437' and decode to valid 'utf-8'.
            # This is hard to regex.
            
            # Simpler Plan:
            # Extract the key and value from the line.
            # Try to fix the key separately.
            # Try to fix the value separately.
            # Reassemble.
            
            # Regex for "Key": "Value" (standard JS props)
            item_match = re.search(r'^\s*(["\'])(.*?)\1\s*:\s*(["\'])(.*?)\3(,?)$', line)
            if item_match:
                quote1 = item_match.group(1)
                key = item_match.group(2)
                quote2 = item_match.group(3)
                val = item_match.group(4)
                comma = item_match.group(5)
                indent = line[:line.find(quote1)]
                
                fixed_key = fix_mojibake(key)
                # Value generally seems fine (Chinese), but let's check. 
                # Actually, values like "：去掉 \\" for H2SO3 example suggest value might be corrupted too or just bad.
                # But the user only complained about the key corruption in the example.
                
                if fixed_key != key:
                    # Reconstruct
                    new_line = f'{indent}{quote1}{fixed_key}{quote1}: {quote2}{val}{quote2}{comma}'
                    # Warning: simple reconstruction might lose some formatting like escaping.
                    # JS strings use backslash escapes. `fix_mojibake` handles raw string in memory.
                    # If `key` had `\"`, regex `.*?` might stop early or consume it. 
                    # The regex `.*?` is non-greedy.
                    # Use a more robust split?
                    
                    # Given the risk of breaking valid file structure,
                    # Check if the fix actually changed anything meaningful.
                    
                    # Let's use string replacement on the line for the specific key substring
                    new_line_str = line.replace(key, fixed_key)
                    new_lines.append(new_line_str)
                    changes += 1
                    # print(f"Fixed: {key} -> {fixed_key}")
                    continue

        new_lines.append(line)

    if changes > 0:
        print(f"Fixed {changes} lines.")
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
    else:
        print("No changes found/made.")

if __name__ == "__main__":
    main()
