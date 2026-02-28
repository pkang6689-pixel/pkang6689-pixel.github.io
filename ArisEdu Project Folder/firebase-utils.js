// Firebase Configuration - Replace with your config
const FIREBASE_CONFIG = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT.appspot.com",
  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
  appId: "YOUR_APP_ID"
};

let currentUserId = null;

// Initialize Firebase (REST API - no SDK needed)
async function initializeFirebase() {
  try {
    // Get current user ID
    currentUserId = getCurrentUserId();
    console.log('✅ Firebase REST API initialized with user:', currentUserId);
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

// Get user data from Firebase or localStorage using REST API
async function getUser() {
  // Always return localStorage first (fast), Firebase is backup
  const localUser = JSON.parse(localStorage.getItem('user') || '{}');
  
  try {
    if (!FIREBASE_CONFIG.projectId || FIREBASE_CONFIG.projectId === 'YOUR_PROJECT_ID') {
      return localUser;
    }
    
    // Bypass ORB by using REST API with API key
    const docPath = `users/${currentUserId}`;
    const url = `https://firestore.googleapis.com/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/${docPath}?key=${FIREBASE_CONFIG.apiKey}`;
    
    const response = await fetch(url);
    
    if (response.ok) {
      const doc = await response.json();
      if (doc.fields) {
        return {
          points: parseInt(doc.fields.points?.integerValue || 0),
          timestamp: doc.fields.timestamp?.stringValue || new Date().toISOString()
        };
      }
    }
  } catch (error) {
    // Silently fail, use localStorage
  }
  
  return localUser;
}

// Save user data to Firebase and localStorage using REST API
async function saveUser(user) {
  // Always save to localStorage as primary store
  localStorage.setItem('user', JSON.stringify(user));
  
  try {
    if (!FIREBASE_CONFIG.projectId || FIREBASE_CONFIG.projectId === 'YOUR_PROJECT_ID') {
      return; // Config not set, skip Firebase
    }
    
    const docPath = `users/${currentUserId}`;
    const firebaseData = {
      fields: {
        points: { integerValue: String(user.points || 0) },
        timestamp: { stringValue: new Date().toISOString() }
      }
    };
    
    const url = `https://firestore.googleapis.com/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/${docPath}?key=${FIREBASE_CONFIG.apiKey}`;
    
    await fetch(url, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(firebaseData)
    });
  } catch (error) {
    // Silently fail - localStorage still has the data
  }
}

// Update only points
async function updateTokens(newPoints) {
  const user = await getUser();
  user.points = newPoints;
  await saveUser(user);
  return user;
}
