// Firebase Configuration - Replace with your config
const FIREBASE_CONFIG = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// Initialize Firebase
async function initializeFirebase() {
  try {
    // Check if Firebase SDK is loaded
    if (typeof firebase === 'undefined') {
      console.log('⚠️ Firebase SDK not loaded, using localStorage fallback');
      return false;
    }
    
    // Initialize Firebase using compat API (doesn't return a promise)
    if (!firebase.apps.length) {
      firebase.initializeApp(FIREBASE_CONFIG);
    }
    db = firebase.firestore();
    
    // Get current user ID
    currentUserId = getCurrentUserId();
    console.log('✅ Firebase initialized successfully with user:', currentUserId);
    return true;
  } catch (error) {
    console.log('⚠️ Firebase initialization failed:', error.message, '- using localStorage fallback');
    return false;
  }
}

function getCurrentUserId() {
  let userId = sessionStorage.getItem('userId');
  if (!userId) {
    userId = 'user_' + Math.random().toString(36).substr(2, 9);
    sessionStorage.setItem('userId', userId);
  }
  return userId;
}

// Get user data from Firebase or localStorage
async function getUser() {
  try {
    if (db && currentUserId) {
      const doc = await db.collection('users').doc(currentUserId).get();
      if (doc.exists) {
        return doc.data();
      }
    }
  } catch (error) {
    console.log('Firebase read failed, using localStorage');
  }
  
  // Fallback to localStorage
  return JSON.parse(localStorage.getItem('user') || '{}');
}

// Save user data to Firebase and localStorage
async function saveUser(user) {
  // Always save to localStorage as backup
  localStorage.setItem('user', JSON.stringify(user));
  
  try {
    if (db && currentUserId) {
      await db.collection('users').doc(currentUserId).set(user, { merge: true });
    }
  } catch (error) {
    console.log('Firebase write failed, data saved to localStorage only');
  }
}

// Update only points
async function updateTokens(newPoints) {
  const user = await getUser();
  user.points = newPoints;
  await saveUser(user);
  return user;
}
