#!/usr/bin/env python3
"""Runner script that captures output to file."""
import sys, io

# Capture all output to file
log = open('_geo_result.txt', 'w', encoding='utf-8')

try:
    # Check syntax first
    import ast
    with open('batch_geometry.py', encoding='utf-8') as f:
        ast.parse(f.read())
    log.write("Syntax check: OK\n")
    
    # Import and run
    sys.path.insert(0, r'c:\Users\Peter\pkang6689-pixel.github.io')
    
    # Redirect stdout
    old_stdout = sys.stdout
    sys.stdout = log
    
    from batch_geometry import translations
    print(f"Translation count: {len(translations)}")
    
    from inject_translations_util import inject_all
    result = inject_all(translations)
    print(f"Result: {result}")
    
    sys.stdout = old_stdout
    
except Exception as e:
    log.write(f"ERROR: {type(e).__name__}: {e}\n")
    import traceback
    traceback.print_exc(file=log)

finally:
    log.close()
