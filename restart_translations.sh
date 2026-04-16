#!/bin/bash

echo "Restarting all translation processes..."

# Find and kill Python processes running translation scripts
for pid in $(ps aux | grep "translate.*offline" | grep -v grep | awk '{print $2}'); do
    echo "Killing process $pid"
    kill -9 $pid 2>/dev/null
done

sleep 2

cd "$(dirname "$0")"

echo "Starting Spanish translation..."
python translate_spanish_offline.py >> translation_progress.log 2>&1 &

echo "Starting Hindi translation..."
python translate_hindi_offline.py >> translation_progress_hindi.log 2>&1 &

echo "Starting Chinese translation..."
python translate_chinese_offline.py >> translation_progress_chinese.log 2>&1 &

echo "All processes restarted!"
sleep 5
echo "Current status:"
tail -3 translation_progress.log
tail -3 translation_progress_hindi.log
tail -3 translation_progress_chinese.log
