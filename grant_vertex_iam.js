// Grants roles/aiplatform.user to the Cloud Function service account
// Uses Firebase CLI's stored OAuth token
const fs = require("fs");
const path = require("path");
const https = require("https");

const PROJECT_ID = "arisedu-1bb22";
const SERVICE_ACCOUNT = "serviceAccount:1003231707877-compute@developer.gserviceaccount.com";
const ROLE = "roles/aiplatform.user";

function httpsRequest(options, body) {
  return new Promise((resolve, reject) => {
    const req = https.request(options, (res) => {
      let data = "";
      res.on("data", (chunk) => (data += chunk));
      res.on("end", () => resolve({ status: res.statusCode, body: data }));
    });
    req.on("error", reject);
    if (body) req.write(body);
    req.end();
  });
}

async function refreshToken(refreshToken) {
  const body = new URLSearchParams({
    grant_type: "refresh_token",
    client_id: "563584335869-fgrhgmd47bqnekij5i8b5pr03ho849e6.apps.googleusercontent.com",
    client_secret: "j9iVZfS8lje4JpTgHKMkPGyd",
    refresh_token: refreshToken,
  }).toString();

  const res = await httpsRequest(
    {
      hostname: "oauth2.googleapis.com",
      path: "/token",
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    },
    body
  );
  if (res.status !== 200) throw new Error("Token refresh failed: " + res.body);
  return JSON.parse(res.body).access_token;
}

async function main() {
  const cfgPath = path.join(require("os").homedir(), ".config", "configstore", "firebase-tools.json");
  const cfg = JSON.parse(fs.readFileSync(cfgPath, "utf8"));
  const tokens = cfg.tokens;

  let accessToken = tokens.access_token;
  // Refresh if expired
  if (Date.now() > tokens.expires_at) {
    console.log("Token expired, refreshing...");
    accessToken = await refreshToken(tokens.refresh_token);
  }

  // 1. GET current IAM policy
  const getRes = await httpsRequest({
    hostname: "cloudresourcemanager.googleapis.com",
    path: `/v1/projects/${PROJECT_ID}:getIamPolicy`,
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      "Content-Type": "application/json",
    },
  }, "{}");

  if (getRes.status !== 200) {
    console.error("Failed to get IAM policy:", getRes.status, getRes.body);
    process.exit(1);
  }

  const policy = JSON.parse(getRes.body);
  console.log("Got IAM policy, etag:", policy.etag);

  // Check if binding already exists
  const existing = (policy.bindings || []).find((b) => b.role === ROLE);
  if (existing && existing.members.includes(SERVICE_ACCOUNT)) {
    console.log(`Binding already exists: ${ROLE} -> ${SERVICE_ACCOUNT}`);
    return;
  }

  // 2. Add binding
  if (!policy.bindings) policy.bindings = [];
  if (existing) {
    existing.members.push(SERVICE_ACCOUNT);
  } else {
    policy.bindings.push({ role: ROLE, members: [SERVICE_ACCOUNT] });
  }

  // 3. SET IAM policy
  const setRes = await httpsRequest(
    {
      hostname: "cloudresourcemanager.googleapis.com",
      path: `/v1/projects/${PROJECT_ID}:setIamPolicy`,
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
    },
    JSON.stringify({ policy })
  );

  if (setRes.status === 200) {
    console.log(`SUCCESS: Granted ${ROLE} to ${SERVICE_ACCOUNT}`);
  } else {
    console.error("Failed to set IAM policy:", setRes.status, setRes.body);
  }
}

main().catch(console.error);
