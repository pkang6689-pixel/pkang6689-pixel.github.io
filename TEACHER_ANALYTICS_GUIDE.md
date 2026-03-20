# Teacher Analytics Dashboard - Complete Guide

## Overview

The Teacher Analytics Dashboard is a comprehensive system for monitoring student progress, engagement, and performance across all courses. It provides teachers with real-time insights into class-wide trends and individual student metrics.

## Features

### 1. **Overview Tab** 📈
Displays class-wide statistics and trends:
- **Total Students**: Count of enrolled students
- **Average Quiz Score**: Class average across all quizzes
- **Average Completion**: Percentage of lessons completed on average
- **Total Lessons Completed**: Sum across entire class
- **Average Learning Time**: Mean hours spent learning
- **Active Today**: Students who logged in today

**Visualizations:**
- Course Progress Distribution (doughnut chart)
- Quiz Score Distribution (bar chart)
- Learning Time Distribution (bar chart)
- Class Activity Over Time (line chart)

### 2. **Students Tab** 👥
Interactive list of all students in the class with:
- Student name and email
- Completion percentage
- Average quiz score
- Learning streak
- Lessons completed count

**Features:**
- Click any student to view detailed analytics
- Search/filter by name or email
- Sort and compare student metrics

### 3. **Performance Tab** 🎯
Detailed table view showing:
- Course completion percentages
- Average quiz scores with visual progress bars
- Flashcards mastered/reviewed
- Learning streak status
- Last active date

**Sorting:**
Automatically sorted by completion percentage (highest first)

### 4. **Engagement Tab** 🔥
Heatmap visualization showing:
- 30-day activity log
- Color intensity indicates engagement level
  - Empty = no activity
  - Light = low activity
  - Medium = moderate activity
  - High = high engagement

**Engagement Statistics:**
- Average daily active students
- Weekly active count (all time)
- Inactive students (7+ days)
- Streak leaders (7+ day streaks)

### 5. **Individual Student Detail View**
Click on any student to see:
- Student profile information
- Course-by-course progress bars
- Quiz scores and averages
- Badges earned and achievement progress
- Activity timeline (first login, last active)
- Learning streak status

## Data Tracked

### Student Progress Data
```
{
  visitedPages: [],              // Pages accessed
  progressFlags: {},             // Course-specific progress
  courseCompletion: 0-100,       // % of lessons done
  lessonsCompleted: 0,           // Total lessons finished
  
  quizScores: {                  // Quiz results by lesson
    "course_u1_l1": [
      { score: 85, date: "2024-01-01" }
    ]
  },
  
  flashcardProgress: {           // Flashcard mastery
    "course_id": [
      { cardId: "card1", mastered: true }
    ]
  },
  
  badges: [],                    // Earned badges/achievements
  streakCount: 0,                // Consecutive login days
  lastLogin: "2024-01-01",      // ISO timestamp
  createdAt: "2024-01-01",      // Registration date
}
```

### Aggregated Class Metrics
The dashboard calculates:
- **Completion Rate** = Sum of individual completion / student count
- **Average Quiz Score** = Mean of all quiz results
- **Engagement Score** = Active students in last 7 days / total
- **Class Momentum** = Trend of activity over time

## How to Use

### For Teachers

#### Accessing the Dashboard
1. Log in as a teacher
2. On Dashboard.html, click "View Student Analytics"
3. You'll be redirected to TeacherAnalytics.html

#### Creating a Class
1. Go to Dashboard.html
2. Enter a class name in the teacher section
3. Click "Create Class"
4. Share the generated class code with students
5. Students enter this code to join your class

#### Monitoring Progress
1. **Overview Tab**: Get immediate class health snapshot
2. **Students Tab**: See per-student metrics at a glance
3. **Click any student**: Dive deep into individual progress
4. **Performance Tab**: Compare students side-by-side
5. **Engagement Tab**: Identify at-risk or high-performing groups

#### Identifying Issues
- **Low completion**: Check Engagement tab - may indicate access issues
- **Low quiz scores**: Review Performance tab - students may need help
- **Inactive students**: See gray cells in heatmap - follow up with these students
- **High performers**: Recognize streak leaders for motivation

### For Students

#### Tracking Progress
Progress is automatically tracked when students:
1. Visit a lesson page
2. Complete a quiz
3. Review flashcards
4. Log in daily (streak tracking)

**No manual data entry needed** - everything is automatic!

## Integration with Course Pages

### Adding Analytics to a Course Page

Include the analytics helper and track events:

```html
<!-- Add to your course page -->
<script src="scripts/analytics-helper.js"></script>

<script>
  // Initialize analytics
  const analytics = new StudentAnalytics();
  
  // Track lesson view
  analytics.trackLessonView('algebra1', 1, 1); // Course, unit, lesson
  
  // Track quiz completion
  analytics.trackQuizCompletion('algebra1', 1, 1, 85, 100); // Score: 85/100
  
  // Track flashcard review
  analytics.trackFlashcardReview('algebra1', 'card_1', true); // Card mastered
  
  // Update streak on page load
  analytics.updateLearningStreak();
</script>
```

### Data Model for Courses

Each course should use consistent naming:
- **courseId**: `algebra1`, `geometry`, `physics`, etc.
- **unitNumber**: 1-based (Unit 1, Unit 2, etc.)
- **lessonNumber**: 1-based within unit
- **quizScore**: 0-100 percentage

Example: `algebra1_u2_l3_completed` = Algebra 1, Unit 2, Lesson 3

## Charts and Visualizations

### Chart.js Integration
The dashboard uses Chart.js v3.9.1 for:
- **Doughnut charts**: Course distribution
- **Bar charts**: Score and time distribution
- **Line charts**: Activity trends

All charts are:
- Responsive (adapt to screen size)
- Dark-mode compatible
- Interactive (hover for details)
- Auto-updating based on student data

## Database Structure (Firebase)

### Users Collection
```
users/
  {uid}/
    displayName: "John Doe"
    email: "john@example.com"
    role: "teacher" | "student"
    
    # For teachers:
    classInfo: {
      name: "Algebra Period 1"
      code: "ABC123"
    }
    
    # For students:
    classInfo: {
      code: "ABC123"
      name: "Algebra Period 1"
    }
    
    # Shared student tracking:
    visitedPages: []
    quizScores: {}
    flashcardProgress: {}
    badges: []
    streakCount: 0
    lastLogin: "ISO-date"
    createdAt: "ISO-date"
```

## Performance Optimization

The dashboard is optimized for:
- **Fast load times**: Lazy-loads charts on tab switch
- **Efficient queries**: Filters data on client side
- **Dark mode**: Reduces eye strain and battery usage
- **Responsive design**: Works on mobile, tablet, desktop

## Troubleshooting

### No Students Showing
- Check student class code - must match teacher's code
- Ensure students are set as "role: student" in Firebase
- Verify class code hasn't expired

### Empty Charts
- Wait for students to complete quizzes/lessons
- Check browser console for Firebase errors
- Ensure data is being tracked in localStorage

### Incorrect Metrics
- Clear browser cache and reload
- Check localStorage data in DevTools
- Verify course naming conventions (courseId)

### Performance Slow
- Check number of students (100+ may need pagination)
- Clear old data with `StudentAnalytics.clearAnalyticsData()`
- Enable browser caching

## Future Enhancements

### Planned Features
- [ ] Export reports to PDF
- [ ] Custom time period filters
- [ ] Assignment submission tracking
- [ ] Parent notification system
- [ ] Predictive analytics (at-risk detection)
- [ ] Individual learning paths
- [ ] Adaptive difficulty based on performance
- [ ] Video analytics integration
- [ ] Peer comparison (anonymous)
- [ ] Mobile app for on-the-go monitoring

### API Integrations (Potential)
- Send email alerts for low performers
- Sync with LMS systems
- Export to Google Classroom
- Slack notifications for milestones

## Security & Privacy

### Data Privacy
- Student data is encrypted in Transit (Firebase SSL)
- No personal data is shared between students
- Teachers can only see their own class
- Data is removed after account deletion

### Permissions
- **Teachers**: Can view all student data in their class
- **Students**: Can only see their own progress
- **Admin**: Can modify user roles and classes

### GDPR Compliance
- Data can be exported and deleted
- Student consent not required (school context)
- Minimal data collection (no tracking outside app)

## Support & Documentation

For questions or issues:
1. Check this guide first
2. Review browser console for errors
3. Verify Firebase configuration
4. Check student data tracking is active
5. Contact development team if issues persist

## API Reference

### StudentAnalytics Class

```javascript
// Initialize
analytics = new StudentAnalytics(userId)

// Tracking methods
analytics.trackLessonView(courseId, unitNum, lessonNum)
analytics.trackQuizCompletion(courseId, unitNum, lessonNum, score, maxScore)
analytics.trackFlashcardReview(courseId, cardId, mastered)

// Query methods
analytics.getAverageQuizScore(courseId)
analytics.getCourseCompletion(courseId, totalLessons)
analytics.getSessionTimeSpent()
analytics.getLearningStreak()
analytics.getAnalyticsSummary()

// Data methods
analytics.exportAnalyticsData()
analytics.clearAnalyticsData()
```

## Version History

- **v1.0** (Current)
  - Initial release
  - Overview, Students, Performance, Engagement tabs
  - Student detail modal
  - Chart visualizations
  - Dark mode support
  - Mobile responsive
