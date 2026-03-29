#!/usr/bin/env python3
"""
Install sentencepiece and run all translations
"""
import subprocess
import sys

# First, install sentencepiece
print("Installing sentencepiece...")
result = subprocess.run([sys.executable, "-m", "pip", "install", "sentencepiece"], check=False)

if result.returncode == 0:
    print("Sentencepiece installed successfully")

    # Now run the master script
    print("\nRunning all translations...")
    result2 = subprocess.run([sys.executable, "run_all_translations.py"], check=False)
    sys.exit(result2.returncode)
else:
    print("Failed to install sentencepiece")
    sys.exit(1)
