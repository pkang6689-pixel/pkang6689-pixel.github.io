// security_utils.js
// Lightweight client-side security helpers shared across the app.
// Exposed on window for non-module scripts.
(function () {
  'use strict';

  // HTML-escape a string so it is safe to interpolate into innerHTML.
  function escapeHtml(value) {
    if (value === null || value === undefined) return '';
    const s = String(value);
    return s.replace(/[&<>"'`/]/g, function (c) {
      return ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '`': '&#96;',
        '/': '&#47;'
      })[c];
    });
  }

  // Escape a value intended to be placed inside an HTML attribute.
  // Same rules as escapeHtml; kept separate so future tightening is easy.
  function escapeAttr(value) {
    return escapeHtml(value);
  }

  // Tagged-template helper:  html`<div>${userName}</div>`  auto-escapes ${...}
  // values. Use this anywhere we previously built innerHTML with template
  // literals containing user-controlled data.
  function html(strings, ...values) {
    let out = '';
    for (let i = 0; i < strings.length; i++) {
      out += strings[i];
      if (i < values.length) {
        const v = values[i];
        // Allow opting out by wrapping with html.raw(...)
        if (v && typeof v === 'object' && v.__rawHtml === true) {
          out += String(v.value);
        } else {
          out += escapeHtml(v);
        }
      }
    }
    return out;
  }
  html.raw = function (value) { return { __rawHtml: true, value: value }; };

  // Strict whitelist-based math expression evaluator. Replaces the unsafe
  // `new Function('return ' + s)()` previously used by the calculator.
  // Returns a finite Number on success, or NaN on any error / disallowed input.
  function safeMathEval(rawExpr, lastAns) {
    if (typeof rawExpr !== 'string') return NaN;
    let s = rawExpr;
    // Normalize visual operators
    s = s.replace(/×/g, '*').replace(/÷/g, '/').replace(/\^/g, '**');
    // Substitute ANS with the previous answer (numeric only)
    const ans = Number(lastAns);
    s = s.replace(/ANS/g, isFinite(ans) ? String(ans) : '0');

    // Allowed function / constant names
    const allowedIdent = new Set([
      'sin','cos','tan','asin','acos','atan','atan2',
      'sqrt','cbrt','abs','log','ln','exp',
      'floor','ceil','round','min','max','pow',
      'pi','e'
    ]);

    // Tokenize: numbers, identifiers, operators, parens, comma, !, whitespace
    const tokenRe = /\s+|(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|([A-Za-z_][A-Za-z_0-9]*)|(\*\*|[+\-*/(),!])/g;
    let m;
    let safe = '';
    let last = 0;
    while ((m = tokenRe.exec(s)) !== null) {
      if (m.index !== last) return NaN; // unrecognised char
      last = tokenRe.lastIndex;
      const [, num, ident, op] = m;
      if (num !== undefined) {
        safe += num;
      } else if (ident !== undefined) {
        const lower = ident.toLowerCase();
        if (!allowedIdent.has(lower)) return NaN;
        if (lower === 'pi') safe += 'Math.PI';
        else if (lower === 'e') safe += 'Math.E';
        else if (lower === 'ln') safe += 'Math.log';
        else if (lower === 'log') safe += 'Math.log10';
        else safe += 'Math.' + lower;
      } else if (op !== undefined) {
        if (op === '!') {
          // Replace trailing  N!  with factorial — only allow on a number/closing paren
          // Simpler: implement after tokenization is more complex; reject ! for safety.
          return NaN;
        }
        safe += op;
      }
    }
    if (last !== s.length) return NaN;
    if (!safe) return NaN;

    try {
      // Safe: only numerals, operators, parentheses, commas and Math.* references
      // are present in `safe` per the whitelist above.
      // eslint-disable-next-line no-new-func
      const fn = new Function('"use strict"; return (' + safe + ');');
      const result = fn();
      if (typeof result !== 'number' || !isFinite(result)) return NaN;
      return Math.round(result * 1e12) / 1e12;
    } catch (_e) {
      return NaN;
    }
  }

  // Debug-aware logger. Set localStorage.debug = '1' (or window.__DEBUG = true)
  // to opt in. By default we don't print PII like emails / UIDs.
  function debugEnabled() {
    try {
      if (window.__DEBUG === true) return true;
      return localStorage.getItem('debug') === '1';
    } catch (_e) { return false; }
  }
  const safeLog = {
    info:  function () { if (debugEnabled()) console.log.apply(console, arguments); },
    warn:  function () { if (debugEnabled()) console.warn.apply(console, arguments); },
    error: function () { console.error.apply(console, arguments); }
  };

  window.SecurityUtils = {
    escapeHtml: escapeHtml,
    escapeAttr: escapeAttr,
    html: html,
    safeMathEval: safeMathEval,
    safeLog: safeLog
  };
  // Backward-compatible globals
  window.escapeHtml = escapeHtml;
  window.htmlSafe = html;
})();
