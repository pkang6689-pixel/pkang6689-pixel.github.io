# Quick Start Guide: HS→MS Completion Sync

## 🚀 What's New?

When a **high school student completes a lesson**, the corresponding **middle school lesson is automatically marked complete** too. This is a one-way sync - completing MS lessons does NOT affect HS.

---

## 📋 Implementation Summary

### What Was Changed

1. **quiz_ui.js** - Added automatic mirroring logic
   - New function: `mirrorHSToMSCompletion()` 
   - Automatically called after HS students complete lessons
   - Uses existing `_msMap_` mappings from taskbar.js

2. **No changes needed in individual quiz files**
   - The mirroring happens at the framework level
   - All courses automatically benefit from this feature

### Key Features

✅ **Automatic** - No manual action needed after a quiz is completed  
✅ **One-way** - Only HS→MS, never MS→HS  
✅ **Safe** - Silently fails if mapping missing, never breaks quiz flow  
✅ **Non-destructive** - Never deletes data, only adds new keys  
✅ **Backward compatible** - Works with existing code and lessons  

---

## 🔄 How to Migrate Existing Data

### For Users with Existing Completed Lessons

Run ONE of these methods to apply the sync to past lessons:

#### Method A: Web Interface (Easy)
```
1. Open this file in your browser:
   migrate_lessons.html
   
2. Click "Run Migration"

3. Watch the log output

4. See the summary of migrated lessons
```

#### Method B: Browser Console (Advanced)
```
1. Open the browser console (F12 → Console tab)

2. Copy all code from migrate_hs_completion_to_ms.js

3. Paste into console and press Enter

4. View output and migration report
```

#### Method C: Programmatic (For Developers)
```javascript
// If you need to run migration in code:
fetch('migrate_hs_completion_to_ms.js')
  .then(r => r.text())
  .then(code => eval(code));
```

---

## 📊 Understanding the Data

### Storage Keys

Each completed lesson creates a localStorage key:

```
High School:  {subject}_u{unit}_l{lesson}_completed = 'true'
Middle School: ms_{subject}_u{unit}_l{lesson}_completed = 'true'

Examples:
  HS Physics: physics_u2_l1_completed = 'true'
  MS Physics: ms_phys_u2_l1_completed = 'true'
```

### Checking Your Data

In **DevTools** (F12):
1. Go to **Application** tab
2. Click **LocalStorage**
3. Search for your subject (e.g., "alg1", "ms_phys")
4. You'll see all completed lessons listed

---

## ✅ Testing the Feature

### Quick Test

```javascript
// In browser console, complete this test:

// 1. Set a HS lesson as complete
localStorage.setItem('test_u1_l1_completed', 'true');

// 2. Run the mirror function
mirrorHSToMSCompletion();

// 3. Check if MS key was created
console.log(localStorage.getItem('ms_test_u1_l1_completed'));
// Should output: 'true'
```

### Real Test

1. **Log in as HS student**
2. **Complete a quiz**
3. **Open DevTools** (F12)
4. **Go to Application → LocalStorage**
5. **Search for the lesson subject** (e.g., "physics")
6. **Verify both keys exist:**
   - `physics_u2_l1_completed = 'true'`
   - `ms_phys_u2_l1_completed = 'true'`

---

## 📁 Files Created/Modified

### Modified
- `ArisEdu Project Folder/scripts/quiz_ui.js`
  - Added `mirrorHSToMSCompletion()` function
  - Updated `awardLessonTokensIfFirstCompletion()` to call mirror

### Created
- `migrate_hs_completion_to_ms.js` - Migration script
- `migrate_lessons.html` - Web UI for migration
- `HS_TO_MS_COMPLETION_SYNC.md` - Detailed documentation
- `QUICK_START.md` - This file

---

## 🛠️ Technical Details

### How It Works

```
1. HS Student Completes Quiz
         ↓
2. awardLessonTokensIfFirstCompletion() called
         ↓
3. HS completion key set in localStorage
         ↓
4. mirrorHSToMSCompletion() called
         ↓
5. Parse HS lesson from URL
         ↓
6. Load _msMap_ from localStorage
         ↓
7. Find MS lesson mapping
         ↓
8. Set MS completion key
         ↓
9. Done! (no errors shown to user)
```

### One-Way Logic

```javascript
// Pseudo-code of one-way sync
if (isMS) {
  // MS student: ONLY set MS key, do NOT set HS
  setMSKey();
} else {
  // HS student: set HS key AND mirror to MS
  setHSKey();
  setMSKey();  // via mirrorHSToMSCompletion()
}
```

---

## ❓ Common Questions

**Q: Will this affect historical data?**
A: Only if you run the migration. New completions are automatically synced.

**Q: What if an MS mapping doesn't exist?**
A: The function silently skips that lesson. It won't cause errors.

**Q: Can MS students see HS progress?**
A: No. MS completion is independent. Only HS→MS sync, never reverse.

**Q: How do I verify it's working?**
A: Check localStorage after completing a quiz. Both HS and MS keys should exist.

**Q: What if I want to undo migrations?**
A: The migration only adds keys, never removes them. To undo, delete MS keys manually, but use with caution.

---

## 🐛 Troubleshooting

### Migration finds no lessons
- Ensure both HS and MS courses have been visited
- Check that `_msMap_` keys exist in localStorage
- Verify you have completed HS lessons

### Some lessons not syncing
- Check if the MS course has that lesson
- Verify the `_msMap_` contains the mapping
- Review migration log for specific failures

### JavaScript errors
- Check browser console for errors
- Ensure quiz_ui.js loaded successfully
- Try clearing cache and refreshing

---

## 📞 Next Steps

1. ✅ Read the implementation above
2. ✅ Run the migration tool if you have historical data
3. ✅ Test by completing a quiz
4. ✅ Verify in DevTools that both keys are set
5. ✅ Monitor student progress as they complete lessons

For detailed technical documentation, see: **HS_TO_MS_COMPLETION_SYNC.md**

---

## 📝 Developer Notes

### Integration Points

- **quiz_ui.js**: Main implementation (lines 727-780)
- **taskbar.js**: Creates `_msMap_` mappings (line 1361)
- **unit_test.js**: Already has similar sync logic (lines 460-485)

### Testing Checklist

- [ ] HS student completes lesson → both keys set
- [ ] MS student completes lesson → only MS key set
- [ ] Migration updates all historical HS lessons
- [ ] No errors in console
- [ ] Tokens awarded correctly
- [ ] Progress bar reflects completion

### Future Enhancements

- Consider adding visual indicator in dashboard
- Add audit logging for all sync operations
- Create admin tool to view/manage all mappings
- Extend sync to other progress states (started, attempted)
