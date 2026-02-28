// Local fallback stub for Element SDK.
// Some pages include /_sdk/element_sdk.js; this prevents 404s in local/dev.
window.ElementSDK = window.ElementSDK || {
  init() {},
};
