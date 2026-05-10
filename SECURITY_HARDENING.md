# Security Hardening — Done & TODO

This file lists what the recent security pass changed and what still requires
**manual action in the Firebase / GCP console** that I cannot do for you.

## What was changed in code

1. **Firestore + Storage rules** added.
   - [firestore.rules](firestore.rules) — default-deny, owner-only on `users/`, role-gated on `classes/`, verified-author on `forums/`.
   - [storage.rules](storage.rules) — owner-only `users/*` writes (5 MB image/PDF only), public read-only on `public/*`.
   - [firebase.json](firebase.json) — wires the rules in and adds Firebase Hosting security headers.

2. **XSS hardening**.
   - New helper [ArisEdu Project Folder/scripts/security_utils.js](ArisEdu%20Project%20Folder/scripts/security_utils.js): `escapeHtml`, `escapeAttr`, tagged-template `html` helper, strict `safeMathEval`, debug-aware `safeLog`.
   - Included on every main page (AccountInfo, Dashboard, Login, Signup, Courses, FAQ, forums, lab_simulations, LoginSignup, Preferences, TeacherAnalytics, arcade, template).
   - Patched the highest-risk `innerHTML` sinks to escape user-controlled strings:
     - Known-users list in [AccountInfo.html](ArisEdu%20Project%20Folder/AccountInfo.html).
     - Search results in [Signup.html](ArisEdu%20Project%20Folder/Signup.html).
     - Student row + table in [TeacherAnalytics.html](ArisEdu%20Project%20Folder/TeacherAnalytics.html).

3. **Calculator code-injection fix**.
   - [tools_panel.js](ArisEdu%20Project%20Folder/scripts/tools_panel.js) no longer feeds raw user input into `new Function(...)`; it delegates to `SecurityUtils.safeMathEval`, which tokenises with a strict whitelist before evaluating.

4. **Account impersonation fix**.
   - "Switch user" in [AccountInfo.html](ArisEdu%20Project%20Folder/AccountInfo.html) no longer copies a `known_users` entry into `localStorage.user`. It signs out and routes to the login page so Firebase Auth must verify the new account.

5. **Password / auth hardening**.
   - Signup now requires **≥ 12 chars** and **3 of 4** character classes ([Signup.html](ArisEdu%20Project%20Folder/Signup.html)).
   - Signup calls `sendEmailVerification` after account creation.
   - Plaintext passwords are **no longer stored in localStorage** on signup or login ([Signup.html](ArisEdu%20Project%20Folder/Signup.html), [Login.html](ArisEdu%20Project%20Folder/Login.html)).

6. **CSP + security headers**.
   - [server.py](server.py) now sets `Content-Security-Policy`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, `Cross-Origin-*` on every response.
   - CSP `<meta>` tags added to AccountInfo, Login, Signup, Dashboard, TeacherAnalytics so static hosts (e.g. GitHub Pages) honour the policy.

7. **Server hardening**.
   - [server.py](server.py) rejects path-traversal (`..`) and NUL-byte requests early in `translate_path`.

8. **Logging hygiene**.
   - [firebase-config-script.js](ArisEdu%20Project%20Folder/firebase-config-script.js) no longer logs the user's email; uses `SecurityUtils.safeLog`, which only emits when `localStorage.debug === '1'` (or `window.__DEBUG === true`).

---

## TODO — manual steps for you

These cannot be done from code. Please complete when you get a chance.

### A. Deploy the new rules
```powershell
# from repo root
npm install -g firebase-tools         # if not installed
firebase login
firebase use arisedu-1bb22
firebase deploy --only firestore:rules,storage
```

### B. Restrict the Web API key (very important)
1. Open https://console.cloud.google.com/apis/credentials?project=arisedu-1bb22
2. Click the **Browser key** (the `AIzaSy...` one used in `firebase-config.js`).
3. Under **Application restrictions** → choose **HTTP referrers (web sites)**.
4. Add referrers:
   - `https://pkang6689-pixel.github.io/*`
   - `https://arisedu-1bb22.firebaseapp.com/*`
   - `https://arisedu-1bb22.web.app/*`
   - (and `http://localhost:8082/*` for local dev)
5. Under **API restrictions** → restrict to: Identity Toolkit API, Token Service API, Firebase Installations API, Cloud Firestore API, Firebase Realtime Database API, Cloud Storage for Firebase API, Firebase Cloud Messaging API.

### C. Enable Firebase App Check
1. Open https://console.firebase.google.com/project/arisedu-1bb22/appcheck
2. Register the web app with **reCAPTCHA Enterprise** (preferred) or **reCAPTCHA v3**.
3. Copy the site key, then add to each HTML page (after Firebase init):
   ```html
   <script type="module">
     import { initializeAppCheck, ReCaptchaEnterpriseProvider }
       from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app-check.js";
     import { app } from "./firebase-config.js"; // export `app` if needed
     initializeAppCheck(app, {
       provider: new ReCaptchaEnterpriseProvider("YOUR_SITE_KEY"),
       isTokenAutoRefreshEnabled: true
     });
   </script>
   ```
4. In the App Check console, set **Enforce** for Firestore, Storage, and Auth.

### D. Identity Platform / Auth settings
In https://console.firebase.google.com/project/arisedu-1bb22/authentication/settings:
- Enable **Email enumeration protection**.
- Enable **Password policy** — require length ≥ 12, mixed character classes, **block leaked passwords**.
- (Optional, recommended for teachers) enable **Multi-factor authentication**.
- Add only your real domains to **Authorized domains**; remove any test/sample domains.

### E. Once email verification is enforced
After App Check + email verification are confirmed working, tighten
[firestore.rules](firestore.rules) by replacing `isSignedIn()` with
`isVerified()` on the routes where you want to require a verified email
(e.g. forum writes already use `isVerified`). Re-deploy with
`firebase deploy --only firestore:rules`.

### F. (Optional) Subresource Integrity
Module imports of `https://www.gstatic.com/firebasejs/10.7.1/...` cannot use
SRI. To get integrity protection, either:
- Self-host a vendored copy of the SDK, or
- Switch to the namespaced (compat) SDK loaded via `<script integrity="sha384-...">`.

### G. (Optional) Remove `known_users` localStorage list
The "Switch user" UI is now safe (forces re-login), but `localStorage.known_users`
still leaks a list of accounts that have signed in on the device. Consider
removing the feature entirely or storing only display info (no email).

---
_Last updated: 2026-05-09._
