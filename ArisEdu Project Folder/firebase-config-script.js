// Firebase Configuration - Non-Module Version for Script Tags
// This version uses the Firebase SDK from global scope (loaded from CDN)

const firebaseConfig = {
  apiKey: "AIzaSyCOauFIB0fu4BSbHBeBo_8dwR3F1Fct5IM",
  authDomain: "arisedu-1bb22.firebaseapp.com",
  projectId: "arisedu-1bb22",
  storageBucket: "arisedu-1bb22.firebasestorage.app",
  messagingSenderId: "1003231707877",
  appId: "1:1003231707877:web:0c97944e04b410941a0a0c",
  measurementId: "G-XEEFF1QH75"
};

let app, auth, db;

// Wait for Firebase SDK to be loaded from CDN
async function initializeFirebase() {
  try {
    // Firebase SDK should be loaded from CDN in the HTML before this script
    if (typeof firebase === 'undefined') {
      console.warn('[Firebase] Firebase SDK not loaded yet, waiting...');
      return;
    }

    app = firebase.initializeApp(firebaseConfig);
    auth = firebase.getAuth(app);
    db = firebase.getFirestore(app);
    
    console.log('Firebase initialized (non-module)');
    
    // Expose to window for other scripts
    window.db = db;
    window.auth = auth;
    window.firebaseApp = app;

    // Set up auth state listener
    firebase.onAuthStateChanged(auth, (user) => {
      const dbg = (typeof window !== 'undefined' && window.SecurityUtils && window.SecurityUtils.safeLog)
        ? window.SecurityUtils.safeLog : { info: function(){} };
      if (user) {
        dbg.info('[Firebase] User authenticated (uid:', user.uid, ')');
        window.currentUser = user;
      } else {
        dbg.info('[Firebase] No user authenticated');
        window.currentUser = null;
      }
    });

  } catch (error) {
    console.error('Firebase Initialization Error (non-module):', error);
  }
}

// Initialize when document is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeFirebase);
} else {
  initializeFirebase();
}
