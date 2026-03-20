/**
 * Analytics Helper Module
 * Provides utilities for tracking student progress, quiz scores, time spent, and more
 * Used by: Course pages, Quiz pages, and TeacherAnalytics.html
 * 
 * Now includes Firebase sync for persisting data to teacher dashboards
 */

// Firebase exports for direct SDK access
let firebaseDb = null;
let firebaseAuth = null;

// Try to get Firebase SDK imports
async function getFirebaseSDK() {
  // First check if Firebase is available on window (set by course pages)
  if (typeof window !== 'undefined' && window.db && window.auth) {
    firebaseDb = window.db;
    firebaseAuth = window.auth;
    return { db: firebaseDb, auth: firebaseAuth };
  }
  
  // If already cached, return cached version
  if (firebaseDb && firebaseAuth) {
    return { db: firebaseDb, auth: firebaseAuth };
  }
  
  // Try dynamic import as fallback
  try {
    const { db, auth } = await import('../firebase-config.js');
    firebaseDb = db;
    firebaseAuth = auth;
    return { db, auth };
  } catch (e) {
    console.warn('⚠️ Could not import Firebase SDK:', e.message);
    return null;
  }
}

// Firebase REST API Configuration (fallback only)
const FIREBASE_REST_CONFIG = {
  projectId: "arisedu-1bb22",
  apiKey: "AIzaSyCOauFIB0fu4BSbHBeBo_8dwR3F1Fct5IM"
};

// Try to get Firebase auth from window (if available)
function getFirebaseAuth() {
  try {
    // Check if window.auth exists (set by firebase-config.js or other scripts)
    if (typeof window !== 'undefined' && window.auth) {
      return window.auth;
    }
  } catch (e) {
    // Firebase auth not available
  }
  return null;
}

class StudentAnalytics {
  constructor(userId = null) {
    this.userId = userId || this.getCurrentUserId();
    this.auth = getFirebaseAuth();
    this.sessionStartTime = Date.now();
    this.sessionData = {
      lessonsViewed: [],
      quizzesCompleted: [],
      timeSpent: 0,
      flashcardsReviewed: [],
      dayDate: new Date().toDateString()
    };
    this.syncInProgress = false;
    this.lastSyncTime = 0;

    this.loadSessionData();
    
    // Try to initialize Firebase and update userId with real Firebase UID if available
    this.initializeFirebaseAsync();
    
    // Backfill: Sync pre-existing localStorage data to Firebase (for progress that existed before sync was added)
    this.syncExistingDataToFirebase();
  }

  /**
   * Initialize Firebase asynchronously and update user ID if Firebase user found
   */
  async initializeFirebaseAsync() {
    try {
      const firebaseSDK = await getFirebaseSDK();
      if (firebaseSDK && firebaseSDK.auth && firebaseSDK.auth.currentUser) {
        const firebaseUID = firebaseSDK.auth.currentUser.uid;
        if (firebaseUID && firebaseUID !== this.userId) {
          console.log('🔄 Updated user ID from session to Firebase UID:', firebaseUID);
          this.userId = firebaseUID;
        }
      }
    } catch (error) {
      // Firebase not available, continue with session ID
      console.log('ℹ️ Firebase async init skipped, using session ID:', this.userId);
    }
  }

  /**
   * Get current user ID - tries Firebase first, falls back to session storage
   */
  getCurrentUserId() {
    // Try to get Firebase user ID first from window (set by course pages)
    if (typeof window !== 'undefined' && window.auth && window.auth.currentUser) {
      console.log('✅ Using Firebase user ID:', window.auth.currentUser.uid);
      return window.auth.currentUser.uid;
    }
    
    // Fallback to session storage ID
    let userId = sessionStorage.getItem('userId');
    if (!userId) {
      userId = 'user_' + Math.random().toString(36).substr(2, 9);
      sessionStorage.setItem('userId', userId);
      console.log('⚠️ No Firebase user found, using session ID:', userId);
    } else {
      console.log('✅ Using session ID:', userId);
    }
    return userId;
  }

  /**
   * Load existing session data from localStorage
   */
  loadSessionData() {
    const stored = localStorage.getItem('arisEdu_sessionData');
    if (stored) {
      try {
        this.sessionData = JSON.parse(stored);
      } catch (e) {
        console.warn('Could not load session data:', e);
      }
    }
  }

  /**
   * Save session data to localStorage
   */
  saveSessionData() {
    this.sessionData.timeSpent = Math.round((Date.now() - this.sessionStartTime) / 1000 / 60); // Minutes
    localStorage.setItem('arisEdu_sessionData', JSON.stringify(this.sessionData));
  }

  /**
   * Sync analytics data to Firebase (persists for teacher dashboard)
   * Uses Firebase SDK for reliable persistence
   */
  async syncToFirebase() {
    // Avoid concurrent syncs
    if (this.syncInProgress) return;
    
    // Throttle sync to prevent excessive writes
    const timeSinceLastSync = Date.now() - this.lastSyncTime;
    if (timeSinceLastSync < 5000) return; // Wait at least 5 seconds between syncs
    
    this.syncInProgress = true;
    this.lastSyncTime = Date.now();

    try {
      // Compile all analytics data
      const analyticsData = {
        quizScores: JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}'),
        visitedPages: JSON.parse(localStorage.getItem('arisEdu_visitedPages') || '[]'),
        badges: JSON.parse(localStorage.getItem('arisEdu_badges') || '[]'),
        streak: parseInt(localStorage.getItem('arisEdu_streak') || '0'),
        progressFlags: this.buildProgressFlags(),
        lastLoginDate: localStorage.getItem('arisEdu_lastLoginDate') || new Date().toDateString(),
        lastSyncTime: new Date().toISOString()
      };

      // Try Firebase SDK first (preferred - uses real auth)
      const firebaseSDK = await getFirebaseSDK();
      
      if (firebaseSDK && firebaseSDK.db) {
        await this.syncToFirebaseSDK(firebaseSDK.db, analyticsData);
      } else {
        console.warn('⚠️ Firebase SDK not available, analytics sync skipped');
      }
    } catch (error) {
      console.warn('⚠️ Firebase sync error:', error.message);
    } finally {
      this.syncInProgress = false;
    }
  }

  /**
   * Sync using Firebase SDK (setDoc with merge to create or update)
   */
  async syncToFirebaseSDK(db, analyticsData) {
    try {
      const { doc, setDoc } = await import('../firebase-config.js');
      
      console.log('📤 Syncing analytics to Firebase for user:', this.userId);
      console.log('   📋 Quiz Scores to sync:', analyticsData.quizScores);
      
      // Get reference to user document
      const userDocRef = doc(db, 'users', this.userId);
      
      // Use setDoc with merge: true to create document if it doesn't exist, or update if it does
      await setDoc(userDocRef, {
        quizScores: analyticsData.quizScores,
        visitedPages: analyticsData.visitedPages,
        badges: analyticsData.badges,
        streak: analyticsData.streak,
        progressFlags: analyticsData.progressFlags,
        lastLoginDate: analyticsData.lastLoginDate,
        lastSyncTime: analyticsData.lastSyncTime
      }, { merge: true });  // merge: true preserves existing fields like displayName, email, role
      
      console.log('✅ Analytics synced to Firebase');
      console.log('   User ID:', this.userId);
      console.log('   Quizzes synced:', Object.keys(analyticsData.quizScores).length);
      console.log('   Streak:', analyticsData.streak);
      console.log('   Last Sync:', analyticsData.lastSyncTime);
      
    } catch (error) {
      console.error('❌ Firebase SDK sync failed:', error.message);
      throw error;
    }
  }

  /**
   * Convert JavaScript data to Firestore document format
   */
  convertToFirestoreFormat(data) {
    const fields = {};

    // Quiz scores - convert to stringValue (JSON string)
    fields.quizScores = {
      stringValue: JSON.stringify(data.quizScores)
    };

    // Visited pages - convert array to arrayValue
    fields.visitedPages = {
      arrayValue: {
        values: data.visitedPages.map(page => ({
          stringValue: page
        }))
      }
    };

    // Progress flags - convert to stringValue
    fields.progressFlags = {
      stringValue: JSON.stringify(this.buildProgressFlags())
    };

    // Badges
    fields.badges = {
      arrayValue: {
        values: data.badges.map(badge => ({
          stringValue: badge
        }))
      }
    };

    // Streak
    fields.streak = {
      integerValue: String(data.streak)
    };

    // Last login date
    fields.lastLoginDate = {
      stringValue: data.lastLoginDate
    };

    // Last sync timestamp
    fields.lastSyncTime = {
      stringValue: data.lastSyncTime
    };

    // Role (preserve existing)
    fields.role = {
      stringValue: 'student'
    };

    return fields;
  }

  /**
   * Build progress flags object from localStorage
   */
  buildProgressFlags() {
    const flags = {};
    Object.keys(localStorage).forEach(key => {
      if (key.includes('_completed') && !key.includes('arisEdu_')) {
        flags[key] = localStorage.getItem(key);
      }
    });
    return flags;
  }

  /**
   * Sync pre-existing data from localStorage to Firebase (backfill for old progress)
   * Called on initialization to ensure existing student data appears in teacher dashboard
   */
  syncExistingDataToFirebase() {
    // Only run once per session to avoid duplicate syncs
    const backfillKey = 'arisEdu_backfillSynced_' + this.userId;
    if (sessionStorage.getItem(backfillKey)) {
      return; // Already backfilled this session
    }

    // Check if there's existing data that needs syncing
    const quizScores = JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}');
    const hasExistingData = Object.keys(quizScores).length > 0;

    if (hasExistingData) {
      // Mark that we've attempted backfill
      sessionStorage.setItem(backfillKey, 'true');
      
      // Perform sync with a small delay to allow page to load
      setTimeout(() => {
        this.syncToFirebase();
      }, 1000);
    }
  }

  /**
   * Track lesson viewed
   * @param {string} courseId - Course identifier
   * @param {number} unitNumber - Unit number
   * @param {number} lessonNumber - Lesson number
   */
  trackLessonView(courseId, unitNumber, lessonNumber) {
    const lessonId = `${courseId}_u${unitNumber}_l${lessonNumber}`;
    
    if (!this.sessionData.lessonsViewed.includes(lessonId)) {
      this.sessionData.lessonsViewed.push(lessonId);
    }

    // Also track in progress flags for backwards compatibility
    const flagKey = `${courseId}_u${unitNumber}_l${lessonNumber}_viewed`;
    localStorage.setItem(flagKey, Date.now().toString());

    // Save to visited pages
    const currentUrl = window.location.pathname;
    const visited = JSON.parse(localStorage.getItem('arisEdu_visitedPages') || '[]');
    if (!visited.includes(currentUrl)) {
      visited.push(currentUrl);
      localStorage.setItem('arisEdu_visitedPages', JSON.stringify(visited));
    }

    this.saveSessionData();
    
    // Sync to Firebase (throttled to prevent excessive writes)
    this.syncToFirebase();
  }

  /**
   * Track quiz completion
   * @param {string} courseId - Course identifier
   * @param {number} unitNumber - Unit number
   * @param {number} lessonNumber - Lesson number
   * @param {number} score - Quiz score (0-100)
   * @param {number} maxScore - Max possible score
   */
  trackQuizCompletion(courseId, unitNumber, lessonNumber, score, maxScore = 100) {
    const quizId = `${courseId}_u${unitNumber}_l${lessonNumber}`;
    const percentage = Math.round((score / maxScore) * 100);

    const quizData = {
      quizId,
      score: percentage,
      maxScore,
      completedAt: new Date().toISOString(),
      courseId,
      unitNumber,
      lessonNumber
    };

    console.log(`🎯 Quiz Completion: ${quizId} = ${percentage}%`);

    if (!this.sessionData.quizzesCompleted.includes(quizId)) {
      this.sessionData.quizzesCompleted.push(quizId);
    }

    // Store quiz score history
    const quizScores = JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}');
    if (!quizScores[quizId]) {
      quizScores[quizId] = [];
    }
    quizScores[quizId].push(quizData);
    localStorage.setItem('arisEdu_quizScores', JSON.stringify(quizScores));
    
    console.log(`📝 Stored in localStorage. Current arisEdu_quizScores:`, JSON.parse(localStorage.getItem('arisEdu_quizScores')));

    // Update progress flag
    const flagKey = `${courseId}_u${unitNumber}_l${lessonNumber}_completed`;
    localStorage.setItem(flagKey, percentage.toString());

    this.saveSessionData();
    
    // Sync to Firebase for teacher dashboard visibility
    console.log(`🔄 Triggering Firebase sync for quiz completion...`);
    this.syncToFirebase();
    
    return quizData;
  }

  /**
   * Track flashcard review
   * @param {string} courseId - Course identifier
   * @param {string} cardId - Flashcard ID
   * @param {boolean} mastered - Whether student mastered this card
   */
  trackFlashcardReview(courseId, cardId, mastered = false) {
    const cardData = {
      cardId,
      courseId,
      mastered,
      reviewedAt: new Date().toISOString()
    };

    if (!this.sessionData.flashcardsReviewed.includes(cardId)) {
      this.sessionData.flashcardsReviewed.push(cardId);
    }

    // Store flashcard progress
    const flashcardProgress = JSON.parse(localStorage.getItem('arisEdu_flashcardProgress') || '{}');
    if (!flashcardProgress[courseId]) {
      flashcardProgress[courseId] = [];
    }
    flashcardProgress[courseId].push(cardData);
    localStorage.setItem('arisEdu_flashcardProgress', JSON.stringify(flashcardProgress));

    this.saveSessionData();
    
    // Sync to Firebase (throttled)
    this.syncToFirebase();
  }

  /**
   * Get student's average quiz score for a course
   * @param {string} courseId - Course identifier
   * @returns {number} Average score (0-100)
   */
  getAverageQuizScore(courseId = null) {
    const allScores = JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}');
    
    let scores = [];
    if (courseId) {
      Object.keys(allScores).forEach(quizId => {
        if (quizId.startsWith(courseId)) {
          scores = scores.concat(allScores[quizId]);
        }
      });
    } else {
      Object.values(allScores).forEach(quizList => {
        scores = scores.concat(quizList);
      });
    }

    if (scores.length === 0) return 0;
    const avg = scores.reduce((sum, q) => sum + q.score, 0) / scores.length;
    return Math.round(avg);
  }

  /**
   * Get completion percentage for a course
   * @param {string} courseId - Course identifier
   * @param {number} totalLessons - Total lessons in the course
   * @returns {number} Completion percentage (0-100)
   */
  getCourseCompletion(courseId, totalLessons = 200) {
    const allFlags = {};
    Object.keys(localStorage).forEach(key => {
      if (key.includes(courseId) && key.includes('_completed')) {
        allFlags[key] = localStorage.getItem(key);
      }
    });

    const completedCount = Object.keys(allFlags).length;
    return Math.min(100, Math.round((completedCount / totalLessons) * 100));
  }

  /**
   * Get total time spent learning (session only)
   * @returns {number} Time in minutes
   */
  getSessionTimeSpent() {
    return this.sessionData.timeSpent || 0;
  }

  /**
   * Get all quiz scores for a course
   * @param {string} courseId - Course identifier
   * @returns {array} Array of quiz scores
   */
  getCourseQuizScores(courseId) {
    const allScores = JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}');
    const courseScores = [];

    Object.keys(allScores).forEach(quizId => {
      if (quizId.startsWith(courseId)) {
        courseScores.push(...allScores[quizId]);
      }
    });

    return courseScores;
  }

  /**
   * Get flashcard mastery for a course
   * @param {string} courseId - Course identifier
   * @returns {object} Summary of flashcard progress
   */
  getFlashcardProgress(courseId) {
    const allProgress = JSON.parse(localStorage.getItem('arisEdu_flashcardProgress') || '{}');
    const courseProgress = allProgress[courseId] || [];

    const masteredCount = courseProgress.filter(p => p.mastered).length;
    const reviewedCount = courseProgress.length;

    return {
      reviewed: reviewedCount,
      mastered: masteredCount,
      percentage: reviewedCount > 0 ? Math.round((masteredCount / reviewedCount) * 100) : 0
    };
  }

  /**
   * Get student's learning streak
   * @returns {number} Number of consecutive days
   */
  getLearningStreak() {
    return parseInt(localStorage.getItem('arisEdu_streak') || '0');
  }

  /**
   * Update learning streak
   */
  updateLearningStreak() {
    const lastLoginDate = localStorage.getItem('arisEdu_lastLoginDate');
    const today = new Date().toDateString();

    if (lastLoginDate === today) {
      // Already updated today
      return;
    }

    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toDateString();

    if (lastLoginDate === yesterdayStr) {
      // Streak continues
      let streak = parseInt(localStorage.getItem('arisEdu_streak') || '0');
      streak++;
      localStorage.setItem('arisEdu_streak', streak.toString());
      localStorage.setItem('arisEdu_lastLoginDate', today);
    } else if (lastLoginDate === null || lastLoginDate === today) {
      // First login or already today
      localStorage.setItem('arisEdu_streak', '1');
      localStorage.setItem('arisEdu_lastLoginDate', today);
    } else {
      // Streak broken
      localStorage.setItem('arisEdu_streak', '1');
      localStorage.setItem('arisEdu_lastLoginDate', today);
    }

    // Sync to Firebase for teacher dashboard visibility
    this.syncToFirebase();
  }

  /**
   * Get completed lessons count
   * @returns {number} Number of completed lessons
   */
  getCompletedLessonsCount() {
    let count = 0;
    Object.keys(localStorage).forEach(key => {
      if (key.includes('_completed') && !isNaN(localStorage.getItem(key))) {
        count++;
      }
    });
    return count;
  }

  /**
   * Get all student analytics summary
   * @returns {object} Complete analytics summary
   */
  getAnalyticsSummary() {
    const badges = JSON.parse(localStorage.getItem('arisEdu_badges') || '[]');
    const streak = this.getLearningStreak();
    const completedLessons = this.getCompletedLessonsCount();
    const allQuizzes = JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}');

    let totalQuizzes = 0;
    let totalQuizScore = 0;
    Object.values(allQuizzes).forEach(quizList => {
      totalQuizzes += quizList.length;
      quizList.forEach(q => {
        totalQuizScore += q.score;
      });
    });

    const avgQuizScore = totalQuizzes > 0 ? Math.round(totalQuizScore / totalQuizzes) : 0;

    return {
      completedLessons,
      avgQuizScore,
      totalQuizzes,
      badges: badges.length,
      streak,
      sessionTimeSpent: this.getSessionTimeSpent()
    };
  }

  /**
   * Export analytics data (for teacher view or backup)
   * @returns {string} JSON string of all analytics data
   */
  exportAnalyticsData() {
    const data = {
      exported: new Date().toISOString(),
      visitedPages: JSON.parse(localStorage.getItem('arisEdu_visitedPages') || '[]'),
      quizScores: JSON.parse(localStorage.getItem('arisEdu_quizScores') || '{}'),
      flashcardProgress: JSON.parse(localStorage.getItem('arisEdu_flashcardProgress') || '{}'),
      badges: JSON.parse(localStorage.getItem('arisEdu_badges') || '[]'),
      streak: this.getLearningStreak(),
      summary: this.getAnalyticsSummary()
    };
    return JSON.stringify(data, null, 2);
  }

  /**
   * Clear all analytics data (use with caution)
   */
  clearAnalyticsData() {
    if (confirm('Are you sure you want to clear all analytics data? This cannot be undone.')) {
      localStorage.removeItem('arisEdu_quizScores');
      localStorage.removeItem('arisEdu_flashcardProgress');
      localStorage.removeItem('arisEdu_sessionData');
      localStorage.removeItem('arisEdu_streak');
      localStorage.removeItem('arisEdu_lastLoginDate');
      console.log('Analytics data cleared');
    }
  }
}

// Export for use as ES6 module
if (typeof module !== 'undefined' && module.exports) {
  module.exports = StudentAnalytics;
}

// Expose to window for direct access by other scripts (like quiz_ui.js)
if (typeof window !== 'undefined') {
  window.StudentAnalytics = StudentAnalytics;
}
