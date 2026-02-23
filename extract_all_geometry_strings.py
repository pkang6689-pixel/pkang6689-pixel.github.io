#!/usr/bin/env python3
"""Extract all unique English strings from geometry summary JSON files."""
import json
from pathlib import Path
from collections import defaultdict

# List of geometry summary files to process
summary_files = [
    'geometry_summary_batch2.json',
    'geometry_summary_new_translations.json',
    'missing_geometry_summary_strings.json'
]

all_strings = set()
file_sources = defaultdict(list)  # Track which file each string came from

# Process each file
for filename in summary_files:
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"⚠ File not found: {filename}")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract all English keys (only the keys, not values)
        for key in data.keys():
            all_strings.add(key)
            file_sources[key].append(filename)
        
        print(f"✓ Loaded {filename}: {len(data)} entries")
    
    except Exception as e:
        print(f"✗ Error loading {filename}: {e}")

# Sort strings for consistency
sorted_strings = sorted(all_strings)

print(f"\n{'='*60}")
print(f"Total unique strings extracted: {len(sorted_strings)}")
print(f"{'='*60}\n")

# Create output JSON with all unique strings
output = {
    "total_unique_strings": len(sorted_strings),
    "strings": sorted_strings,
    "string_count_by_source": {
        filename: sum(1 for s in sorted_strings if filename in file_sources[s])
        for filename in summary_files
    }
}

# Save to JSON file
output_file = 'geometry_summary_unique_strings.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"✓ Saved all unique strings to: {output_file}")

# Also create a simple text file with one string per line
text_output_file = 'geometry_summary_unique_strings.txt'
with open(text_output_file, 'w', encoding='utf-8') as f:
    for i, string in enumerate(sorted_strings, 1):
        f.write(f"{i}. {string}\n")

print(f"✓ Saved strings as numbered list to: {text_output_file}")

# Print a summary by source file
print("\nString count by source file:")
for filename in summary_files:
    count = output["string_count_by_source"][filename]
    print(f"  {filename}: {count} strings")

# Print first 20 strings as preview
print("\nFirst 20 strings:")
print("-" * 60)
for i, string in enumerate(sorted_strings[:20], 1):
    print(f"{i:3d}. {string}")

print("\n" + "="*60)
print("Extraction complete! All unique geometry summary strings")
print("have been saved to JSON and text files.")
print("="*60)
