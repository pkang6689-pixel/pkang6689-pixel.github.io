# Analytics Integration Quick Start

## For Course Developers

This guide explains how to add student analytics tracking to your course pages.

## Step 1: Add the Analytics Script

Include this line in your course HTML file (in the `<head>` or before `</body>`):

```html
<script src="../scripts/analytics-helper.js"></script>
```

## Step 2: Initialize Analytics

Add this code to your course page initialization:

```javascript
// Initialize the analytics tracker
const studentAnalytics = new StudentAnalytics();

// Update learning streak on page load
studentAnalytics.updateLearningStreak();
```

## Step 3: Track Lesson Views

When a student opens a lesson, track it:

```javascript
// Call this when lesson loads
function loadLesson(courseId, unitNumber, lessonNumber) {
  studentAnalytics.trackLessonView(courseId, unitNumber, lessonNumber);
  
  // ... load lesson content ...
}

// Example usage:
loadLesson('algebra1', 2, 3); // Algebra 1, Unit 2, Lesson 3
```

## Step 4: Track Quiz Completion

When a student completes a quiz, track the score:

```javascript
// Call this when quiz is submitted
function submitQuiz(courseId, unitNumber, lessonNumber, score, totalPoints) {
  const studentAnalytics = new StudentAnalytics();
  studentAnalytics.trackQuizCompletion(
    courseId, 
    unitNumber, 
    lessonNumber, 
    score,           // e.g., 85
    totalPoints      // e.g., 100
  );
  
  // ... show results, update UI ...
}

// Example usage:
submitQuiz('geometry', 1, 2, 92, 100); // 92% on Geometry U1 L2
```

## Step 5: Track Flashcard Progress

When students review flashcards:

```javascript
// Call when student marks a card as "mastered"
function markCardMastered(courseId, cardId) {
  studentAnalytics.trackFlashcardReview(
    courseId,
    cardId,
    true  // true = mastered, false = still learning
  );
}

// Example usage:
markCardMastered('chemistry', 'card_42'); // Marked flashcard as learned
```

## Complete Example

Here's a complete example for a quiz page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Algebra 1 Unit 2 Quiz</title>
</head>
<body>
  <div id="quiz-container">
    <!-- Quiz questions here -->
  </div>

  <script src="../scripts/analytics-helper.js"></script>
  <script>
    // Initialize analytics
    const analytics = new StudentAnalytics();
    
    // Track lesson view on page load
    window.addEventListener('load', () => {
      analytics.trackLessonView('algebra1', 2, 1);
      analytics.updateLearningStreak();
    });

    // Submit quiz
    function submitQuiz() {
      const answers = getAnswers(); // Your quiz logic
      const score = calculateScore(answers);
      const maxScore = 100;
      
      // Track the quiz completion
      analytics.trackQuizCompletion(
        'algebra1',  // Course ID
        2,           // Unit number
        1,           // Lesson number
        score,       // Their score
        maxScore     // Max possible
      );
      
      // Show results
      showResults(score, maxScore);
    }
  </script>
</body>
</html>
```

## Course ID Naming Convention

Use these course IDs for consistency:

### High School Courses
- `algebra1` - Algebra 1
- `algebra2` - Algebra 2
- `geometry` - Geometry
- `physics` - Physics
- `chemistry` - Chemistry
- `biology` - Biology

### Middle School Courses
- `ms_prealgebra` - Pre-Algebra
- `ms_algebra` - Algebra
- `ms_geometry` - Geometry
- `ms_physics` - Physical Science
- `ms_chemistry` - Chemistry Foundations
- `ms_biology` - Life Science

### AP Courses
- `ap_calculus` - AP Calculus
- `ap_statistics` - AP Statistics
- `ap_biology` - AP Biology
- `ap_chemistry` - AP Chemistry
- `ap_physics2` - AP Physics 2
- `ap_physics_mechanics` - AP Physics C: Mechanics
- `ap_environmental_science` - AP Environmental Science
- `ap_hug` - AP Human Geography

## Common Scenarios

### Scenario 1: Multi-lesson Course
```javascript
// Track viewing each lesson
function goToLesson(unitNum, lessonNum) {
  analytics.trackLessonView('algebra1', unitNum, lessonNum);
  loadLessonContent(unitNum, lessonNum);
}

// Track quiz at end of lesson
function completeQuiz(unitNum, lessonNum, score) {
  analytics.trackQuizCompletion('algebra1', unitNum, lessonNum, score, 100);
}
```

### Scenario 2: Flashcard Practice
```javascript
// In your flashcard component
function handleCardReview(cardId, mastered) {
  analytics.trackFlashcardReview('physics', cardId, mastered);
  
  // Update UI to indicate progress
  updateCardProgress(cardId, mastered);
}

// Show progress
function showFlashcardStats() {
  const stats = analytics.getFlashcardProgress('physics');
  console.log(`Mastered: ${stats.mastered}/${stats.reviewed}`);
}
```

### Scenario 3: Check Student Progress
```javascript
// Display student's course progress
function displayProgress() {
  const completion = analytics.getCourseCompletion('geometry', 200);
  const avgScore = analytics.getAverageQuizScore('geometry');
  const streak = analytics.getLearningStreak();
  
  document.getElementById('completion').textContent = completion + '%';
  document.getElementById('avg-score').textContent = avgScore + '%';
  document.getElementById('streak').textContent = streak + ' days';
}
```

### Scenario 4: Get Full Summary
```javascript
// Get complete student analytics
function showStudentDashboard() {
  const summary = analytics.getAnalyticsSummary();
  
  console.log('Completed Lessons:', summary.completedLessons);
  console.log('Average Quiz Score:', summary.avgQuizScore);
  console.log('Total Quizzes:', summary.totalQuizzes);
  console.log('Badges Earned:', summary.badges);
  console.log('Current Streak:', summary.streak);
  console.log('Time Spent Today:', summary.sessionTimeSpent, 'minutes');
}
```

## Testing Your Integration

### Test in Browser Console

```javascript
// 1. Create analytics instance
const analytics = new StudentAnalytics();

// 2. Track a lesson
analytics.trackLessonView('algebra1', 1, 1);

// 3. Track a quiz
analytics.trackQuizCompletion('algebra1', 1, 1, 85, 100);

// 4. Check localStorage
localStorage.getItem('arisEdu_quizScores') // Should show quiz data
localStorage.getItem('arisEdu_visitedPages') // Should show visited pages

// 5. View summary
analytics.getAnalyticsSummary() // Should show all tracked data
```

### Expected localStorage Keys

After tracking, you should see these in DevTools → Application → LocalStorage:

```
arisEdu_visitedPages      // Array of visited pages
arisEdu_quizScores        // Object with quiz results
arisEdu_flashcardProgress // Object with flashcard data
arisEdu_sessionData       // Current session info
arisEdu_streak            // Current streak count
arisEdu_lastLoginDate     // Date of last login
```

## Automatic Tracking (No Code Needed)

These are tracked automatically by the dashboard:

- ✅ Page visits (when course page loads)
- ✅ Login dates (when user logs in)
- ✅ Badges earned (from badge system)
- ✅ Streak counting (automatic daily increment)

## Manual Data Entry (If Needed)

To manually add historical data:

```javascript
// Create quiz scores directly
const quizScores = JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}');
quizScores['algebra1_u1_l1'] = [
  { score: 85, maxScore: 100, completedAt: '2024-01-01T10:00:00Z' }
];
localStorage.setItem('arisEdu_quizScores', JSON.stringify(quizScores));

// Refresh analytics
const analytics = new StudentAnalytics();
analytics.getAnalyticsSummary(); // Will include new data
```

## Do's and Don'ts

### ✅ Do:
- Track both views and quiz completions
- Use consistent course IDs
- Call `updateLearningStreak()` on page load
- Use course ID from the naming convention list
- Track quizzes with actual scores

### ❌ Don't:
- Make up course IDs (not in the list)
- Track the same event twice
- Store scores > 100%
- Track events without course ID
- Manually manipulate quiz score data

## Debugging

### Check tracked data:
```javascript
// See all localStorage analytics keys
Object.keys(localStorage).filter(k => k.includes('arisEdu')).forEach(k => {
  console.log(k, ':', localStorage.getItem(k));
});
```

### View quiz scores:
```javascript
console.log(JSON.parse(localStorage.getItem('arisEdu_quizScores')));
```

### Verify flashcard progress:
```javascript
console.log(JSON.parse(localStorage.getItem('arisEdu_flashcardProgress')));
```

### Check session data:
```javascript
const analytics = new StudentAnalytics();
console.log(analytics.sessionData);
```

## Questions?

See the main guide: [TEACHER_ANALYTICS_GUIDE.md](TEACHER_ANALYTICS_GUIDE.md)

For API documentation, check the comments in: `scripts/analytics-helper.js`
