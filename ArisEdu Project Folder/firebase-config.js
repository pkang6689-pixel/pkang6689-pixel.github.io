import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, sendPasswordResetEmail, updateProfile } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js";
import { getFirestore, doc, setDoc, getDoc, collection, addDoc, getDocs, updateDoc, deleteDoc, orderBy, query, limit, serverTimestamp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyCOauFIB0fu4BSbHBeBo_8dwR3F1Fct5IM",
  authDomain: "arisedu-1bb22.firebaseapp.com",
  databaseURL: "https://arisedu-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "arisedu-1bb22",
  storageBucket: "arisedu-1bb22.firebasestorage.app",
  messagingSenderId: "1003231707877",
  appId: "1:1003231707877:web:0c97944e04b410941a0a0c",
  measurementId: "G-XEEFF1QH75"
};

// Initialize Firebase
let app, auth, db;

try {
    app = initializeApp(firebaseConfig);
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
  doc, 
  setDoc, 
  getDoc,
  collection,
  addDoc,
  getDocs,
  updateDoc,
  deleteDoc,
  orderBy,
  query,
  limit,
  serverTimestamp
};
