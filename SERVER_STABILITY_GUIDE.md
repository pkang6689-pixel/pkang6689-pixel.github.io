# Dev Server Stability Guide

## Current Status (March 29, 2026)
✅ **Server running at:** `http://localhost:8082/`
✅ **Process ID visible in:** `netstat -ano | findstr :8082`

## Root Causes of Previous Crashes

### 1. **Absolute Path Issues** ✅ FIXED
**Problem:** HTML files used hardcoded absolute paths that don't resolve on localhost
```html
<!-- ❌ These don't work on local dev server -->
<link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
<script src="/scripts/quiz_loader.js"></script>
<script src="/_sdk/element_sdk.js"></script>
```

**Solution:** Added server-side path redirection in `server.py`'s `translate_path()` method:
- `/search_data.js` → `search_data.js` (root level)
- `/_sdk/*` → `_sdk/*` (root level)
- `/styles/*` → `/ArisEdu Project Folder/styles/*`
- `/scripts/*` → `/ArisEdu Project Folder/scripts/*`

### 2. **Unprotected Fetch Calls** ✅ FIXED
**Problem:** Multiple JS files had fetch requests with no timeout, causing infinite hangs

**Fixed Files:**
- `dev_tools.js` (line 935) - Now has 5s timeout + fixed absolute path
- `update_notifier.js` (lines 60, 287, 302) - Now has 5s timeouts
- `translation_loader.js` (line 63) - Now has 5s timeout
- `ap_explanations_loader.js` (line 48) - Now has 5s timeout
- `practice_games.js` (line 24) - Now has 5s timeout

**Pattern Used:**
```javascript
var timeout = new Promise(function(_, reject) {
  setTimeout(function() { reject(new Error('Fetch timeout')); }, 5000);
});

Promise.race([
  fetch(url),
  timeout
]).then(...)
```

### 3. **Bad Relative Paths** ✅ FIXED
**Problem:** `taskbar.js` line 1124 used absolute path to load dev_tools.js
```javascript
// ❌ OLD - failed to load
script.src = '/ArisEdu Project Folder/scripts/dev_tools.js';

// ✅ NEW - works correctly
script.src = './dev_tools.js';
```

## Server Configuration

### Connection Management
- Connection header: `Connection: close` (prevents hung connections)
- Socket timeout: 5 seconds
- Daemon threads: Disabled (allows graceful shutdown)
- Request handlers are cleaned up immediately after each request

### Resource Monitoring
Server monitor thread logs every 10 seconds:
```
[MONITOR] Active threads: 2, Connections: 0
```

If **Active threads > 50**, this indicates a resource leak.

### Caching Headers
- `Cache-Control: no-store, no-cache, must-revalidate, max-age=0`
- `Pragma: no-cache`
- `Expires: 0`

This ensures browsers always fetch the latest files during development.

## Troubleshooting

### Server Crashes After a While
**Symptoms:** Server is running, then silently closes without error

**Debug Steps:**
1. Check terminal output for error messages (now visible with debug logging)
2. Watch for `[MONITOR]` thread count - if it keeps increasing, there's a leak
3. Check active connections: `netstat -ano | findstr :8082`

### Browser Shows chrome-error://chromewebdata/
**Cause:** Path redirect failed or fetch timeout occurred

**Solution:** 
- Check browser DevTools → Network tab for failed/hung requests
- Look for red status codes (404, 500) or pending requests
- Check server console for `[do_GET error]` messages

### Pages Load Slowly or Partially
**Cause:** Translation loader or practice games loader is stuck

**Solution:**
- The 5-second fetch timeouts should prevent infinite hangs
- If stuck, browser may need manual refresh
- Check if language is set to non-English (translation loading can be slow)

## Manual Server Restart

```powershell
# Kill existing server
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# Start server
cd "c:\Users\Peter\pkang6689-pixel.github.io"
python server.py
```

## Server Code Location
- **Main:** `c:\Users\Peter\pkang6689-pixel.github.io\server.py`
- **Path redirects:** Lines 20-42 (`translate_path` method)
- **Monitoring:** Lines 85-95 (`monitor_resources` function)

## What to Monitor Going Forward

1. **Connection count:** Should stay at 0 when idle, spike during page loads, return to 0
2. **Active threads:** Should stay around 2-3, never exceed 50
3. **Error messages:** Any `[ERROR]`, `[WARNING]`, or `[BIND ERROR]` messages
4. **Browser network tab:** Look for pending requests or 500 errors

## Testing Checklist

- [ ] Load course homepage (e.g., Algebra 1)
- [ ] Refresh the page multiple times
- [ ] Navigate to a lesson quiz
- [ ] Refresh quiz page 2-3 times
- [ ] Open DevTools Network tab, watch all resources load
- [ ] Leave page idle for 5+ minutes, then refresh
- [ ] Check if server is still listening after 30+ minutes

If all tests pass without crashes, the server is stable.
