# Spanish Translation Background Service

This system automatically translates all course content to Spanish using Google's Gemini API (free tier with generous quota).

## Prerequisites: Get a Free API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key"**
3. Select your project (or create a new one)
4. Copy the API key

Google provides:
- **Free tier**: 15 API calls/minute, unlimited monthly quota (~$5/month credit minimum)
- Perfect for our translation use case
- No credit card required for free tier

## Setup

### Windows (Command Prompt)
```cmd
set GOOGLE_API_KEY=your-api-key-here
python translate_spanish_test.py
```

### Windows (PowerShell)
```powershell
$env:GOOGLE_API_KEY="your-api-key-here"
python translate_spanish_test.py
```

### Linux/Mac
```bash
export GOOGLE_API_KEY="your-api-key-here"
python translate_spanish_test.py
```

## Files

- `translate_spanish.py` - Main translation service that fills in all Spanish translation JSON files
- `translate_spanish_test.py` - Test mode with a small subset to verify API connection
- This README

## How It Works

1. **Finds all Spanish translation JSON files** in `ArisEdu Project Folder/translations/es/`
2. **Uses Google Gemini API** (free tier) to translate English text to Spanish
3. **Processes in batches** (10 items/batch with 2-second delays to respect rate limits)
4. **Saves progress** to `translation_progress.log`
5. **Recovers from errors** with automatic retries and exponential backoff

## Usage

### Test Mode First (Recommended!)
Always test your API key before running full translation:

```bash
python translate_spanish_test.py
```

This:
- Verifies API key is valid
- Tests translation quality
- Checks file structure
- Takes ~30 seconds

### Basic Translation (Full Suite)
Once test passes:

```bash
python translate_spanish.py
```

This will:
- Translate all 25 courses (6,400+ JSON files)
- Run with automatic rate limiting (safe at free tier limits)
- Log all progress to `translation_progress.log`
- Takes 2-4 hours to complete but runs safely in background
- Can be paused anytime (Ctrl+C) and resumed - only translates empty entries

## Progress Tracking

Check progress anytime:
```bash
tail -f translation_progress.log
```

## API Limits

- **Free Tier**: 15 API calls per minute (across all Gemini models)
- **Our Rate Limiting**: 1 batch per 2 seconds = ~30 per minute, but we'll stay under quota
- **Estimated Time**: ~2-4 hours for full translation of all courses

## Features

- ✅ Automatic error recovery with exponential backoff
- ✅ Skips already-translated items
- ✅ Batch processing to maximize efficiency
- ✅ Detailed logging
- ✅ Can be paused (Ctrl+C) and resumed safely
- ✅ Free tier friendly - no expensive API calls
- ✅ Handles rate limiting gracefully

## Next: Hindi and Chinese

After Spanish is complete, can create similar scripts:
- `translate_hindi.py`
- `translate_chinese.py`

These will use the same approach and infrastructure.

## Troubleshooting

### "ModuleNotFoundError: No module named 'google'"
Make sure the venv has google.generativeai installed:
```bash
pip install google-generativeai
```

### API Rate Limit Errors
- Script already handles these with exponential backoff
- Delays automatically increase between retries
- Usually resolves within minutes

### Partial Translations?
You can safely re-run the script - it only translates empty entries, so:
- Won't retranslate completed items
- Can pause and resume anytime
- Each file can be verified independently
