/**
 * Course Progress Firebase Integration
 * Stores and retrieves course completion and progress data from Firebase
 * Falls back to localStorage if Firebase is unavailable
 */

let db = null;
let auth = null;
let currentUser = null;
let useFirebase = false;

/**
 * Initialize Firebase connection for course progress
 */
async function initializeProgressFirebase() {
  try {
    const { db: firebaseDb, auth: firebaseAuth } = await import('../firebase-config.js');
    const { onAuthStateChanged } = await import('https://www.gstatic.com/firebasejs/10.7.1/firebase-auth.js');
    
    db = firebaseDb;
    auth = firebaseAuth;
    useFirebase = true;
    
    // Listen for auth state changes
    onAuthStateChanged(auth, (user) => {
      currentUser = user;
      if (user) {
        console.log('[Course Progress] Firebase user authenticated:', user.email);
      }
    });
    
    console.log('[Course Progress] Firebase initialized successfully');
    return true;
  } catch (error) {
    console.warn('[Course Progress] Firebase initialization failed, using localStorage:', error.message);
    useFirebase = false;
    return false;
  }
}

/**
 * Save course completion to Firebase and localStorage
 * @param {string} coursePrefix - e.g., 'ap_bio', 'ap_chem'
 * @param {number} unit - Unit number
 * @param {number} lesson - Lesson number (99 for unit test)
 */
async function saveProgressToFirebase(coursePrefix, unit, lesson) {
  if (!currentUser) {
    console.log('[Course Progress] No user authenticated, skipping Firebase save');
    return false;
  }

  try {
    if (!useFirebase || !db) {
      return false;
    }

    const { doc, setDoc, updateDoc } = await import('../firebase-config.js');
    
    const userId = currentUser.uid;
    const progressDocRef = doc(db, 'userProgress', userId);
    
    const progressKey = `${coursePrefix}_u${unit}_l${lesson}_completed`;
    const timestamp = new Date().toISOString();
    
    // Update or create the progress document
    await updateDoc(progressDocRef, {
      [progressKey]: true,
      [`${progressKey}_timestamp`]: timestamp,
      lastUpdated: timestamp
    }).catch(async (error) => {
      // If document doesn't exist, create it
      if (error.code === 'not-found') {
        await setDoc(progressDocRef, {
          [progressKey]: true,
          [`${progressKey}_timestamp`]: timestamp,
          lastUpdated: timestamp,
          userId: userId,
          createdAt: timestamp
        });
      } else {
        throw error;
      }
    });
    
    console.log(`[Course Progress] Saved ${progressKey} to Firebase`);
    return true;
  } catch (error) {
    console.warn('[Course Progress] Failed to save to Firebase:', error.message);
    return false;
  }
}

/**
 * Load all progress for a user from Firebase
 */
async function loadProgressFromFirebase() {
  if (!currentUser) {
    console.log('[Course Progress] No user authenticated, skipping Firebase load');
    return null;
  }

  try {
    if (!useFirebase || !db) {
      return null;
    }

    const { doc, getDoc } = await import('../firebase-config.js');
    
    const userId = currentUser.uid;
    const progressDocRef = doc(db, 'userProgress', userId);
    
    const docSnap = await getDoc(progressDocRef);
    
    if (docSnap.exists()) {
      console.log('[Course Progress] Loaded progress from Firebase:', docSnap.data());
      return docSnap.data();
    } else {
      console.log('[Course Progress] No progress document found in Firebase');
      return null;
    }
  } catch (error) {
    console.warn('[Course Progress] Failed to load from Firebase:', error.message);
    return null;
  }
}

/**
 * Sync Firebase progress to localStorage
 */
async function syncFirebaseToLocalStorage() {
  const firebaseData = await loadProgressFromFirebase();
  
  if (!firebaseData) {
    return 0;
  }

  let syncCount = 0;
  
  // Extract all completion entries (those not ending with _timestamp, lastUpdated, etc.)
  for (const [key, value] of Object.entries(firebaseData)) {
    if (key.endsWith('_completed') && value === true) {
      localStorage.setItem(key, 'true');
      syncCount++;
    }
  }
  
  console.log(`[Course Progress] Synced ${syncCount} items from Firebase to localStorage`);
  return syncCount;
}

/**
 * Mark a lesson/test complete and sync to both Firebase and localStorage
 * @param {string} coursePrefix - e.g., 'ap_bio', 'ap_chem'
 * @param {number} unit - Unit number
 * @param {number} lesson - Lesson number (99 for unit test)
 */
async function markProgressComplete(coursePrefix, unit, lesson) {
  const key = `${coursePrefix}_u${unit}_l${lesson}_completed`;
  
  // Always save to localStorage
  localStorage.setItem(key, 'true');
  
  // Also save to Firebase if available
  if (useFirebase && currentUser) {
    await saveProgressToFirebase(coursePrefix, unit, lesson);
  }
  
  // Trigger progress update on current page if available
  if (typeof window.applyProgressColors === 'function') {
    window.applyProgressColors();
  }
  
  return key;
}

/**
 * Mark a lesson as started and sync to both Firebase and localStorage
 * @param {string} coursePrefix - e.g., 'ap_bio', 'ap_chem'
 * @param {number} unit - Unit number
 * @param {number} lesson - Lesson number (99 for unit test)
 */
async function markProgressStarted(coursePrefix, unit, lesson) {
  const key = `${coursePrefix}_u${unit}_l${lesson}_started`;
  
  // Always save to localStorage
  localStorage.setItem(key, 'true');
  
  // Trigger progress update on current page if available
  if (typeof window.applyProgressColors === 'function') {
    window.applyProgressColors();
  }
  
  return key;
}

/**
 * Get progress for a specific course from both sources
 * Prefers Firebase if available and synced, falls back to localStorage
 */
async function getCourseProgress(coursePrefix) {
  const progress = {
    completed: [],
    started: [],
    source: 'localStorage'
  };

  // First try Firebase if authenticated
  if (useFirebase && currentUser) {
    const firebaseData = await loadProgressFromFirebase();
    if (firebaseData) {
      for (const [key, value] of Object.entries(firebaseData)) {
        if (key.startsWith(coursePrefix) && value === true) {
          if (key.includes('_completed')) {
            progress.completed.push(key);
          } else if (key.includes('_started')) {
            progress.started.push(key);
          }
        }
      }
      progress.source = 'firebase';
    }
  }

  // Fall back to localStorage
  if (progress.completed.length === 0) {
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key.startsWith(coursePrefix) && localStorage.getItem(key) === 'true') {
        if (key.includes('_completed')) {
          progress.completed.push(key);
        } else if (key.includes('_started')) {
          progress.started.push(key);
        }
      }
    }
    progress.source = 'localStorage';
  }

  return progress;
}

/**
 * Clear all progress for a user (admin/dev function)
 */
async function clearAllProgress() {
  // Clear localStorage
  const keysToRemove = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && (key.includes('_completed') || key.includes('_started'))) {
      keysToRemove.push(key);
    }
  }
  
  keysToRemove.forEach(key => localStorage.removeItem(key));
  
  // Clear Firebase if available
  if (useFirebase && currentUser) {
    try {
      const { doc, deleteDoc } = await import('../firebase-config.js');
      const userId = currentUser.uid;
      const progressDocRef = doc(db, 'userProgress', userId);
      await deleteDoc(progressDocRef);
      console.log('[Course Progress] Cleared all Firebase progress');
    } catch (error) {
      console.warn('[Course Progress] Failed to clear Firebase progress:', error.message);
    }
  }
  
  console.log(`[Course Progress] Cleared ${keysToRemove.length} local progress entries`);
  return keysToRemove.length;
}

/**
 * Clear progress matching a prefix (e.g. 'chem_u') from both sources
 */
async function clearProgressByPrefix(prefix) {
  if (!prefix) return 0;

  // Clear localStorage
  const keysToRemove = [];
  for (let i = 0; i < localStorage.length; i++) {
    const key = localStorage.key(i);
    if (key && key.startsWith(prefix)) {
      keysToRemove.push(key);
    }
  }
  
  keysToRemove.forEach(key => localStorage.removeItem(key));
  
  // Clear from Firebase if available
  if (useFirebase && currentUser) {
    try {
      const { doc, updateDoc, deleteField } = await import('../firebase-config.js');
      
      const userId = currentUser.uid;
      const progressDocRef = doc(db, 'userProgress', userId);
      
      // We need to know which keys to delete from Firebase.
      // Since we don't store a separate list, we must read the document first.
      const firebaseData = await loadProgressFromFirebase();
      
      if (firebaseData) {
        const updates = {};
        for (const [key, value] of Object.entries(firebaseData)) {
          if (key.startsWith(prefix)) {
            updates[key] = deleteField();
            // Also try to delete associated timestamp if it exists
            if (firebaseData[`${key}_timestamp`]) {
                updates[`${key}_timestamp`] = deleteField();
            }
          }
        }
        
        if (Object.keys(updates).length > 0) {
            await updateDoc(progressDocRef, updates);
            console.log(`[Course Progress] Cleared ${Object.keys(updates).length} Firebase entries for prefix ${prefix}`);
        }
      }
    } catch (error) {
      console.warn('[Course Progress] Failed to clear Firebase progress by prefix:', error.message);
    }
  }
  
  console.log(`[Course Progress] Cleared ${keysToRemove.length} local progress entries for prefix ${prefix}`);
  return keysToRemove.length;
}

// Initialize Firebase on script load
initializeProgressFirebase().then(success => {
  if (success) {
    // Sync Firebase data to localStorage on page load
    setTimeout(syncFirebaseToLocalStorage, 500);
  }
});

// Export functions globally
window.courseProgress = {
  markComplete: markProgressComplete,
  markStarted: markProgressStarted,
  loadFromFirebase: loadProgressFromFirebase,
  syncToLocalStorage: syncFirebaseToLocalStorage,
  getCourseProgress: getCourseProgress,
  clearAllProgress: clearAllProgress,
  clearProgressByPrefix: clearProgressByPrefix,
  isFirebaseEnabled: () => useFirebase && currentUser
};

// Also export for direct imports
export {
  initializeProgressFirebase,
  markProgressComplete,
  markProgressStarted,
  loadProgressFromFirebase,
  syncFirebaseToLocalStorage,
  getCourseProgress,
  clearAllProgress,
  clearProgressByPrefix
};
