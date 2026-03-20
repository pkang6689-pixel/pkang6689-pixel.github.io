# Analytics Integration - Quick Setup Guide

## ✅ Already Integrated (Sample Courses)

The following courses have analytics fully integrated and are ready to use:
- ✅ **Algebra 1** (CourseHomepage/algebra1.html + lessons)
- ✅ **Algebra 2** (CourseHomepage/algebra2.html)
- ✅ **Geometry** (CourseHomepage/geometry.html)
- ✅ **Biology** (CourseHomepage/bio.html)
- ✅ **Chemistry** (CourseHomepage/chem.html)
- ✅ **Physics** (CourseHomepage/physics.html)
- ✅ **Quiz System** (all quizzes - scripts/quiz_loader.js)

**Try it out:**
1. Open any course homepage above
2. Click on a lesson/unit
3. Complete a quiz
4. Check TeacherAnalytics.html to see your progress tracked!

---

## 📋 Integration Checklist

For each course, you need to:

### 1. Course Homepage File
**File:** `CourseHomepage/{course}.html`

**Add to `<head>` section:**
```html
<script src="../scripts/analytics-helper.js"></script>
```

**Add to initialization code (find `DOMContentLoaded` or similar):**
```javascript
if (typeof StudentAnalytics !== 'undefined') {
  try {
    const analytics = new StudentAnalytics();
    analytics.trackLessonView('courseid', 0, 0); // Course visit
    analytics.updateLearningStreak();
  } catch (e) {
    console.warn('Analytics initialization failed:', e);
  }
}
```

---

### 2. Lesson Video Files  
**Files:** All `Lesson*.1_Video.html` files

**Add to `<head>` section:**
```html
<script src="../../../scripts/analytics-helper.js"></script>
```

**Add before `</body>` tag:**
```html
<script>
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof StudentAnalytics !== 'undefined') {
      try {
        const analytics = new StudentAnalytics();
        // Format: analytics.trackLessonView('courseId', unitNum, lessonNum);
        analytics.trackLessonView('courseid', 1, 1);
        analytics.updateLearningStreak();
      } catch (e) {
        console.warn('Analytics tracking failed:', e);
      }
    }
  });
</script>
```

---

### 3. Quiz Files
**Files:** All `Lesson*_Quiz.html` files

**Add to `<head>` section:**
```html
<script src="/../../../scripts/analytics-helper.js"></script>
```

✅ **Quiz tracking is automatic** - quiz_loader.js handles it!

---

## 🔄 Course ID Reference

Use these course IDs in analytics calls:

### High School
| Course | ID |
|--------|-----|
| Algebra 1 | `algebra1` |
| Algebra 2 | `algebra2` |
| Geometry | `geometry` |
| Biology | `bio` or `biology` |
| Chemistry | `chem` or `chemistry` |
| Physics | `physics` |
| Trigonometry | `trig` or `trigonometry` |
| Precalculus | `precalc` or `precalculus` |
| Statistics | `stats` or `statistics` |

### Middle School
| Course | ID |
|--------|-----|
| Pre-Algebra | `ms_prealgebra` |
| Algebra | `ms_algebra` |
| Geometry | `ms_geometry` |
| Physical Science | `ms_physics` |
| Chemistry Foundations | `ms_chem` |
| Life Science | `ms_bio` |

### AP Courses
| Course | ID |
|--------|-----|
| AP Calculus | `ap_calculus` |
| AP Statistics | `ap_statistics` |
| AP Biology | `ap_biology` |
| AP Chemistry | `ap_chemistry` |
| AP Physics 2 | `ap_physics2` |
| AP Physics C: Mechanics | `ap_physics_mechanics` |
| AP Environmental Science | `ap_environmental_science` |
| AP Human Geography | `ap_hug` |

---

## 🚀 How to Apply to Remaining Courses

### Option 1: Manual Updates (Recommended for Understanding)

For each additional course you want to track:

1. **Update CourseHomepage/{course}.html**
   - Add analytics script to head
   - Add initialization code to DOMContentLoaded

2. **Update all Lesson*_Video.html files**
   - Add analytics script to head
   - Add tracking code with correct unit/lesson numbers

3. **Verify quizzes work** (no changes needed - automatic)

### Option 2: Batch Update Script

If you want to update many files at once, use this approach:

```python
# Python script to add analytics to all courses
import os
import re

def add_analytics_to_file(filepath):
    """Add analytics script to head section of HTML files"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added
    if 'analytics-helper.js' in content:
        return False
    
    # Find </head> and add script before it
    script_tag = '<script src="../scripts/analytics-helper.js"></script>'
    if '../' not in filepath:  # Adjust path if needed
        script_tag = '<script src="../../scripts/analytics-helper.js"></script>'
    
    content = content.replace('</head>', f'{script_tag}\n</head>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# Apply to all course homepages
courses_dir = "ArisEdu Project Folder/CourseHomepage"
for file in os.listdir(courses_dir):
    if file.endswith('.html'):
        if add_analytics_to_file(os.path.join(courses_dir, file)):
            print(f"✓ Updated {file}")
```

---

## ✨ What Gets Tracked Automatically

Once integrated, analytics automatically track:

✅ **Lesson Views**
- When student opens a lesson page
- Records course, unit, and lesson number
- Example: "Algebra 1, Unit 2, Lesson 3 viewed"

✅ **Quiz Completions**  
- When student completes any quiz
- Records score as percentage
- Calculates correct answers automatically
- Example: "Algebra 1, Unit 1, Lesson 1 - 85% (17/20 correct)"

✅ **Learning Streaks**
- Automatic daily streak counting
- Increments when student logs in each day
- Breaks if 2+ days without login

✅ **Activity Tracking**
- Records all page visits
- Tracks login dates and times
- Used for engagement heatmap

---

## 🔍 Verify Integration Works

After adding analytics to a course:

1. **Open Developer Tools** (F12)
2. **Go to Application → LocalStorage**
3. **Load a lesson page**
4. **Look for these keys:**
   - `arisEdu_visitedPages` - should show page URL
   - `arisEdu_sessionData` - should show lesson tracking
   - `arisEdu_streak` - should show streak count

4. **Complete a quiz**
5. **Look for:**
   - `arisEdu_quizScores` - should show quiz result with percentage

✅ If these appear, analytics is working!

---

## 📊 View Student Progress

1. Go to **Dashboard.html** (as teacher)
2. Click **"View Student Analytics"**
3. See real-time data:
   - Course progress
   - Quiz scores
   - Student engagement
   - Individual performance

---

## 🛠️ Troubleshooting

### Analytics not tracking?
- ✅ Check that `scripts/analytics-helper.js` is loaded (look in DevTools Network tab)
- ✅ Check browser console for errors (DevTools Console tab)
- ✅ Verify `StudentAnalytics` class is available in console

### Quiz scores showing 0/100?
- ✅ Make sure quiz_loader.js has the tracking code
- ✅ Verify quiz is being submitted (check quiz results screen)
- ✅ Check that `courseSlug` is correct

### Lesson tracking not working?
- ✅ Verify course ID matches the reference table above
- ✅ Check that unit and lesson numbers are correct
- ✅ Ensure tracking code runs before page unloads

---

## 📝 Example: Adding Analytics to Trigonometry

### Step 1: Update `CourseHomepage/trigonometry.html`

**Find line with theme_manager.js** and add after it:
```html
<script src="../scripts/analytics-helper.js"></script>
```

**Find DOMContentLoaded event** and add inside:
```javascript
if (typeof StudentAnalytics !== 'undefined') {
  try {
    const analytics = new StudentAnalytics();
    analytics.trackLessonView('trigonometry', 0, 0);
    analytics.updateLearningStreak();
  } catch (e) {
    console.warn('Analytics initialization failed:', e);
  }
}
```

### Step 2: Update each `Lesson*_Video.html`

**For `Unit1/Lesson1.1_Video.html`:**

Add to `<head>`:
```html
<script src="../../../scripts/analytics-helper.js"></script>
```

Add before `</body>`:
```html
<script>
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof StudentAnalytics !== 'undefined') {
      try {
        const analytics = new StudentAnalytics();
        analytics.trackLessonView('trigonometry', 1, 1);
        analytics.updateLearningStreak();
      } catch (e) {
        console.warn('Analytics tracking failed:', e);
      }
    }
  });
</script>
```

### Step 3: Test it
1. Open TeacherAnalytics on a student/teacher account
2. Visit Trigonometry course
3. Open Lesson 1.1
4. Complete a quiz
5. Check analytics dashboard - should see your progress!

---

## ✅ Next Steps

1. **For sample courses** (Algebra 1, Geometry, Biology, etc.)
   - They're already set up, just test them!
   
2. **For other courses**
   - Follow the integration checklist above
   - Apply to one course first as a test
   - Then batch apply to remaining courses
   
3. **View Results**
   - Dashboard.html → View Student Analytics
   - See all student data in real-time!

---

## 📞 Questions?

See the main documentation:
- [TEACHER_ANALYTICS_GUIDE.md](../TEACHER_ANALYTICS_GUIDE.md) - Full teacher guide
- [ANALYTICS_INTEGRATION_GUIDE.md](../ANALYTICS_INTEGRATION_GUIDE.md) - Full developer guide
- [analytics-helper.js](../scripts/analytics-helper.js) - API documentation in code comments
