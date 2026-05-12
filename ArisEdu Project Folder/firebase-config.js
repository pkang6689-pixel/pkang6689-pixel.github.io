import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, sendPasswordResetEmail, updateProfile, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc, collection, addDoc, getDocs, updateDoc, deleteDoc, deleteField, orderBy, query, limit, serverTimestamp, where } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
import { initializeAppCheck, ReCaptchaV3Provider } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app-check.js";


const firebaseConfig = {
  apiKey: "AIzaSyCOauFIB0fu4BSbHBeBo_8dwR3F1Fct5IM",
  authDomain: "arisedu-1bb22.firebaseapp.com",
  projectId: "arisedu-1bb22",
  storageBucket: "arisedu-1bb22.firebasestorage.app",
  messagingSenderId: "1003231707877",
  appId: "1:1003231707877:web:0c97944e04b410941a0a0c",
  measurementId: "G-XEEFF1QH75"
};

// reCAPTCHA v3 site key for App Check (free tier, no billing required)
const APP_CHECK_SITE_KEY = "6LftjuUsAAAAAOVl1yf6NaFC7xuFGrAgEOiinIe4";

// Enable App Check debug tokens on localhost so local dev still works.
// Uses the pre-registered debug token so no localStorage dependency.
if (typeof self !== "undefined" &&
    typeof location !== "undefined" &&
    (location.hostname === "localhost" || location.hostname === "127.0.0.1")) {
  self.FIREBASE_APPCHECK_DEBUG_TOKEN = "1ce7ac59-1eb4-41de-a2db-4eb657366167";
}

// Initialize Firebase
let app, auth, db, appCheck;

try {
    app = initializeApp(firebaseConfig);

    // Initialize App Check BEFORE other Firebase services start making requests.
    try {
        appCheck = initializeAppCheck(app, {
            provider: new ReCaptchaV3Provider(APP_CHECK_SITE_KEY),
            isTokenAutoRefreshEnabled: true
        });
    } catch (acErr) {
        console.error("App Check initialization failed:", acErr);
    }

    auth = getAuth(app);
    db = getFirestore(app);
    console.log("Firebase initialized");
} catch (e) {
    console.error("Firebase Initialization Error", e);
}

// Export the services and functions so other files can use them
export { 
  auth, 
  db, 
  createUserWithEmailAndPassword, 
  signInWithEmailAndPassword, 
  sendPasswordResetEmail, 
  updateProfile, 
  onAuthStateChanged,
  signOut,
  doc, 
  setDoc, 
  getDoc,
  collection,
  addDoc,
  getDocs,
  updateDoc,
  deleteDoc,
  deleteField,
  orderBy,
  query,
  limit,
  serverTimestamp,
  where
};
