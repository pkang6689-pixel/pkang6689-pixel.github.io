#!/usr/bin/env python3
"""
Master script to install dependencies and run all three translations.
"""

import subprocess
import sys
import os
from pathlib import Path

def install_dependencies():
    """Install missing dependencies."""
    print("Installing missing dependency: sentencepiece...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "sentencepiece", "-q"],
        capture_output=True
    )
    if result.returncode == 0:
        print("OK: sentencepiece installed")
        return True
    else:
        print("ERROR: Failed to install sentencepiece")
        print(result.stderr.decode() if result.stderr else "")
        return False


def run_translation_script(script_name, language):
    """Run a translation script in the background."""
    print(f"\nStarting {language} translation...")
    try:
        process = subprocess.Popen(
            [sys.executable, script_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"OK: {language} translation running (PID: {process.pid})")
        return True
    except Exception as e:
        print(f"ERROR: Failed to start {language} translation: {e}")
        return False


def main():
    os.chdir(Path(__file__).parent)

    print("=" * 60)
    print("Universal Translation Service")
    print("=" * 60)

    # Install dependencies
    print("\n[1] Installing dependencies...")
    if not install_dependencies():
        print("Cannot proceed without sentencepiece")
        return

    # Run all three translations
    print("\n[2] Starting all translations...")
    scripts = [
        ("translate_spanish_offline.py", "Spanish"),
        ("translate_hindi_offline.py", "Hindi"),
        ("translate_chinese_offline.py", "Chinese"),
    ]

    for script, language in scripts:
        run_translation_script(script, language)

    print("\n" + "=" * 60)
    print("All translations started!")
    print("\nMonitor progress:")
    print("  tail -f translation_progress.log          # Spanish")
    print("  tail -f translation_progress_hindi.log    # Hindi")
    print("  tail -f translation_progress_chinese.log  # Chinese")
    print("=" * 60)


if __name__ == "__main__":
    main()
