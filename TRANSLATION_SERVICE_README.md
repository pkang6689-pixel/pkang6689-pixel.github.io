# Spanish Translation Background Service

Two approaches available:

## Approach 1: OFFLINE (Recommended - No API Key Needed)
Uses local Hugging Face models - perfect for overnight processing.

## Approach 2: API-based (If Google available in your region)
Uses Google's Gemini API with free tier.

---

## OFFLINE Translation (Recommended)

**Best for:**
- No API key needed
- Completely offline after model download
- Perfect overnight processing
- Works in any region

### Prerequisites

```bash
pip install transformers torch
```

### Usage

#### Test First (30 seconds)
```bash
python translate_spanish_offline_test.py
```

#### Run Full Translation
```bash
python translate_spanish_offline.py
```

**First run:** Downloads model (~200MB), then translates all 25 courses
- Estimated time: 30-60 minutes for full translation
- No internet needed after first model download
- Can pause/resume anytime (Ctrl+C)
- Safe to leave running overnight

---

## API-Based Translation (Google Gemini)

Only use if Google API is available in your region.

### Prerequisites: Get a Free API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy the API key

### Setup

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=your-api-key-here
python translate_spanish_test.py
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your-api-key-here"
python translate_spanish_test.py
```

**Linux/Mac:**
```bash
export GOOGLE_API_KEY="your-api-key-here"
python translate_spanish_test.py
```

### Usage

#### Test First
```bash
python translate_spanish_test.py
```

#### Run Full Translation
```bash
python translate_spanish.py
```

---

## Files

- `translate_spanish_offline.py` - Main offline service (Recommended)
- `translate_spanish_offline_test.py` - Test offline setup
- `translate_spanish.py` - API-based service (Google Gemini)
- `translate_spanish_test.py` - Test API setup
- `TRANSLATION_SERVICE_README.md` - This file

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
