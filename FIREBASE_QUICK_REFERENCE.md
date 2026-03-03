Firebase Integration - Quick Reference for Developers
=====================================================

Quick commands to test and debug Firebase integration in browser console.

ENABLE DETAILED LOGGING
=======================
// Add this to enable detailed Firebase progress logging
localStorage.setItem('COURSE_PROGRESS_DEBUG', 'true');
// Then reload page. Console will show all [Course Progress] debug messages.

// Disable later
localStorage.removeItem('COURSE_PROGRESS_DEBUG');


FIREBASE STATUS CHECKS
=====================
// Check if Firebase is enabled and working
window.courseProgress.isFirebaseEnabled()
// Returns: true/false

// Check if user is authenticated
firebase.auth().currentUser
// Returns: User object if logged in, null if not

// Get current user ID
firebase.auth().currentUser?.uid
// Returns: User ID string or undefined


MANUAL PROGRESS MARKING
=======================
// Mark a specific lesson complete
await window.courseProgress.markComplete('ap_bio', 1, 5)
// "ap_bio" = course prefix, 1 = unit, 5 = lesson

// Mark a lesson as started
await window.courseProgress.markStarted('ap_bio', 1, 5)

// Mark unit test complete (lesson 99 = unit test)
await window.courseProgress.markComplete('ap_chem', 2, 99)


COURSE PREFIXES
===============
'ap_bio'       → AP Biology
'ap_chem'      → AP Chemistry
'ap_env_sci'   → AP Environmental Science
'ap_hug'       → AP Human Geography
'ap_calc_ab'   → AP Calculus AB
'ap_stats'     → AP Statistics
'ap_phys2'     → AP Physics 2
'ap_phys_mech' → AP Physics C: Mechanics


LOAD AND SYNC DATA
=================
// Load all progress from Firebase for current user
const data = await window.courseProgress.loadFromFirebase()
// Returns: Object with all completion flags

// Sync Firebase data to localStorage
await window.courseProgress.syncToLocalStorage()

// Get progress for specific course
const progress = await window.courseProgress.getCourseProgress('ap_bio')
// Returns: { totalLessons, completedLessons, completionPercent }


FIREBASE DOCUMENT INSPECT
=========================
// In Firebase Console, check the progress document directly:
Collection: userProgress
Document ID: <current userId>

// Or use Firebase SDK to fetch:
const userDoc = await firebase.firestore()
  .collection('userProgress')
  .doc(firebase.auth().currentUser.uid)
  .get()

console.log(userDoc.data())


CLEAR DATA
==========
// Clear ALL progress from both Firebase and localStorage (WARNING: IRREVERSIBLE)
await window.courseProgress.clearAllProgress()

// Or manually clear just localStorage
Object.keys(localStorage).forEach(key => {
  if (key.includes('_u') && key.includes('_l')) {
    localStorage.removeItem(key)
  }
})

// Check what's in localStorage
Object.entries(localStorage)
  .filter(([k,v]) => k.includes('_u') && k.includes('_l'))
  .forEach(([k,v]) => console.log(k, '=', v))


FIREBASE WRITE VERIFICATION
===========================
// Add temporary console logging to Firebase module
// Edit: /ArisEdu Project Folder/scripts/course-progress-firebase.js
// Add to markProgressComplete() function:
console.log('Writing to Firebase:', {
  coursePrefix, unit, lesson,
  path: `userProgress/${user.uid}`
})

// Then check Network tab in DevTools:
// Should see POST request to firestore.googleapis.com


DEV TOOLS FUNCTION
=================
// Complete all courses at once (both Firebase and localStorage)
window.completeAllAPCourses()

// This updates:
// - 362 lessons across 8 courses
// - 64 unit tests
// - All synced to Firebase if logged in


TROUBLESHOOTING COMMANDS
=======================
// 1. Check if Firebase module loaded
window.courseProgress
// Should show object with functions

// 2. Test marking a single lesson
try {
  await window.courseProgress.markComplete('ap_bio', 1, 1)
  console.log('Success!')
} catch(e) {
  console.error('Error:', e)
}

// 3. Check localStorage entry
localStorage.getItem('ap_bio_u1_l1_completed')
// Should return 'true'

// 4. Check Firebase document (if logged in)
const user = firebase.auth().currentUser
if (user) {
  const userDoc = await firebase.firestore()
    .collection('userProgress')
    .doc(user.uid)
    .get()
  console.log('Firebase doc:', userDoc.data())
}

// 5. View all localStorage progress entries
const entries = Object.entries(localStorage).filter(([k]) => 
  k.match(/^ap_\w+_u\d+_l\d+_completed$/)
)
console.table(entries)

// 6. Test offline fallback
// In DevTools: Network tab → throttle to Offline
// Try marking lesson → should still save to localStorage
// Reconnect and reload → progress still there


SYNC STATUS MONITORING
=====================
// Watch for sync status changes
firebase.auth().onAuthStateChanged(user => {
  if (user) {
    console.log('User logged in:', user.uid)
    window.courseProgress.initializeProgressFirebase()
  } else {
    console.log('User logged out - using localStorage only')
  }
})


COMMON ERROR MESSAGES
====================
"[Course Progress] Firebase not available"
→ Firebase module failed to load, using localStorage

"[Course Progress] No user logged in, skipping Firebase"
→ User not authenticated, saving to localStorage only

"[Course Progress] Firestore write error"
→ Firebase write failed, check console for details, data in localStorage

"Permission denied" (in console)
→ Firestore security rules don't allow write access, check FIREBASE_RULES_GUIDE.md


PERFORMANCE PROFILING
====================
// Measure time to mark lesson complete
console.time('markComplete')
await window.courseProgress.markComplete('ap_bio', 1, 1)
console.timeEnd('markComplete')

// Measure time to load progress
console.time('loadProgress')
const data = await window.courseProgress.loadFromFirebase()
console.timeEnd('loadProgress')

// Measure time to complete all courses
console.time('completeAllCourses')
await window.completeAllAPCourses()
console.timeEnd('completeAllCourses')


STATE DUMP FOR DEBUGGING
=======================
// Get complete state snapshot for bug reports
const state = {
  userId: firebase.auth().currentUser?.uid,
  isFirebaseEnabled: window.courseProgress.isFirebaseEnabled(),
  localStorageCount: Object.keys(localStorage).filter(k => 
    k.includes('_u') && k.includes('_l')
  ).length,
  firebaseDocSize: 0, // Will be filled below
}

if (firebase.auth().currentUser) {
  const doc = await firebase.firestore()
    .collection('userProgress')
    .doc(firebase.auth().currentUser.uid)
    .get()
  state.firebaseDocSize = JSON.stringify(doc.data()).length
  state.firebaseEntries = Object.keys(doc.data()).length
}

console.log('State Snapshot:', state)
console.log('JSON:', JSON.stringify(state))
// Copy and paste into bug report


BATCH OPERATIONS
================
// Mark multiple units complete at once
const units = [1, 2, 3, 4, 5]
for (const unit of units) {
  await window.courseProgress.markComplete('ap_bio', unit, 99)  // Mark unit test
}
console.log('Marked 5 unit tests complete')

// Get completion status for all courses
const courses = ['ap_bio', 'ap_chem', 'ap_env_sci', 'ap_hug', 'ap_calc_ab', 'ap_stats', 'ap_phys2', 'ap_phys_mech']
const report = {}
for (const course of courses) {
  report[course] = await window.courseProgress.getCourseProgress(course)
}
console.table(report)


FIREBASE CONSOLE NAVIGATION
==========================
1. Go to: https://console.firebase.google.com
2. Select project: "arisedu-1bb22"
3. Go to: Firestore Database
4. Collection: "userProgress"
5. Look for documents with user ID matching firebase.auth().currentUser.uid
6. View completion flags in document data

---
Last Updated: March 2026
For issues: Check console for [Course Progress] messages
