/* ================================================================
   ArisEdu Translation Loader v1.0
   ================================================================
   Lazy-loads translations split by language + section (course).
   
   Folder structure:
     translations/{lang}/common.json     — shared UI strings (nav, buttons, badges, etc.)
     translations/{lang}/{section}.json  — per-course strings (algebra1, biology, etc.)
   
   Usage in HTML pages:
     <script src="../../scripts/translation_loader.js"
             data-section="algebra1"
             data-base="../../translations"></script>
   
   The script reads data-section and data-base from its own <script> tag.
   If data-section is omitted, only common.json is loaded.
   If data-base is omitted, it defaults to "../translations" (relative to page).
   ================================================================ */
(function () {
    'use strict';

    // ── 1. Prevent flash of English content ──
    var _lang = null;
    try { _lang = localStorage.getItem('arisEduLanguage'); } catch (e) {}
    var _needsTranslation = (_lang === 'chinese' || _lang === 'traditional' ||
                             _lang === 'zh' || _lang === 'spanish' || _lang === 'hindi');
    if (_needsTranslation) {
        document.documentElement.style.opacity = '0';
    }

    function _revealPage() {
        document.documentElement.style.opacity = '';
    }
    // Safety fallback
    setTimeout(_revealPage, 2000);

    // ── 2. Determine language code for folder lookup ──
    function _langCode() {
        var lang = null;
        try { lang = localStorage.getItem('arisEduLanguage'); } catch (e) {}
        if (lang === 'spanish') return 'es';
        if (lang === 'hindi')   return 'hi';
        if (lang === 'chinese' || lang === 'traditional' || lang === 'zh') return 'zh';
        return null; // English — no fetch needed
    }

    // ── 3. Read config from our own <script> tag ──
    var _scriptEl = document.currentScript;
    var _section  = _scriptEl ? _scriptEl.getAttribute('data-section') : null;
    var _base     = _scriptEl ? (_scriptEl.getAttribute('data-base') || '../translations') : '../translations';

    // ── 4. Translation dictionary (merged common + section) ──
    var _dict = {};

    // Cache in sessionStorage to avoid refetching on same-session navigation
    var _cachePrefix = '_arisTL_';

    function _cacheKey(lang, file) {
        return _cachePrefix + lang + '_' + file;
    }

    function _fetchJSON(url) {
        return fetch(url).then(function (res) {
            if (!res.ok) {
                // Return empty dict if file doesn't exist yet — graceful degradation
                if (res.status === 404) return {};
                throw new Error('Translation fetch failed: ' + res.status);
            }
            return res.json();
        });
    }

    function _loadFile(lang, file) {
        var key = _cacheKey(lang, file);
        try {
            var cached = sessionStorage.getItem(key);
            if (cached) return Promise.resolve(JSON.parse(cached));
        } catch (e) {}

        var url = _base + '/' + lang + '/' + file + '.json';
        return _fetchJSON(url).then(function (data) {
            try { sessionStorage.setItem(key, JSON.stringify(data)); } catch (e) {}
            return data;
        });
    }

    // ── 5. Merge helper ──
    function _merge(target, source) {
        var keys = Object.keys(source);
        for (var i = 0; i < keys.length; i++) {
            target[keys[i]] = source[keys[i]];
        }
    }

    // ── 6. Main load routine ──
    function _loadTranslations() {
        var code = _langCode();
        if (!code) {
            _revealPage();
            return Promise.resolve();
        }

        var promises = [_loadFile(code, 'common')];
        if (_section) {
            promises.push(_loadFile(code, _section));
        }

        return Promise.all(promises).then(function (results) {
            for (var i = 0; i < results.length; i++) {
                _merge(_dict, results[i]);
            }
        });
    }

    // ── 7. Expose a translate-one-key helper ──
    window.arisTranslate = function (key) {
        return _dict[key] || key;
    };

    // ── 8. Apply translations to the DOM ──
    // This is the same battle-tested logic from the original global_translations.js,
    // but it reads from the lazily-loaded _dict instead of an inline object.
    window.applyTranslations = function () {
        var lang = null;
        try { lang = localStorage.getItem('arisEduLanguage'); } catch (e) {}
        var isEnglish = (!lang || lang === 'english');

        // 1) Translate elements with class "translatable" + data-en
        var translatables = document.querySelectorAll('.translatable[data-en]');
        translatables.forEach(function (el) {
            var enText = el.getAttribute('data-en');
            if (isEnglish) {
                el.textContent = enText;
            } else if (_dict[enText]) {
                el.textContent = _dict[enText];
            }
        });

        // 2) Recursive text-node walk
        if (!isEnglish && Object.keys(_dict).length) {
            function walk(node) {
                if (node.nodeType === 3) { // Text node
                    var text = node.nodeValue.trim();
                    if (text) {
                        if (_dict[text]) {
                            node.nodeValue = node.nodeValue.replace(text, _dict[text]);
                        } else {
                            var match = text.match(/^(\d+\.)\s+(.+)$/);
                            if (match && _dict[match[2]]) {
                                node.nodeValue = node.nodeValue.replace(text, match[1] + ' ' + _dict[match[2]]);
                            }
                        }
                    }
                } else if (node.nodeType === 1) { // Element
                    if (['SCRIPT', 'STYLE', 'TEXTAREA', 'INPUT', 'CODE', 'PRE'].indexOf(node.tagName) !== -1) return;

                    var CONTENT_TAGS = ['P', 'LI', 'H3', 'H4', 'LABEL', 'TD', 'TH', 'DT', 'DD'];
                    if (CONTENT_TAGS.indexOf(node.tagName) !== -1 && node.childNodes.length > 1) {
                        var fullText = (node.textContent || '').trim();
                        if (fullText && _dict[fullText]) {
                            node.textContent = _dict[fullText];
                            return;
                        }
                        var numMatch = fullText.match(/^(\d+\.)\s+(.+)$/);
                        if (numMatch && _dict[numMatch[2]]) {
                            node.textContent = numMatch[1] + ' ' + _dict[numMatch[2]];
                            return;
                        }
                    }

                    var children = node.childNodes;
                    for (var i = 0; i < children.length; i++) {
                        walk(children[i]);
                    }
                }
            }

            var roots = document.querySelectorAll('body');
            roots.forEach(function (root) { walk(root); });

            // Attributes: title, placeholder, alt
            var titled = document.querySelectorAll('[title], [placeholder], [alt]');
            titled.forEach(function (el) {
                ['title', 'placeholder', 'alt'].forEach(function (attr) {
                    var val = el.getAttribute(attr);
                    if (val && _dict[val.trim()]) {
                        el.setAttribute(attr, _dict[val.trim()]);
                    }
                });
            });

            // [data-i18n] elements
            var i18nEls = document.querySelectorAll('[data-i18n]');
            i18nEls.forEach(function (el) {
                var key = el.getAttribute('data-i18n');
                if (!key) return;

                if (_dict[key]) { el.textContent = _dict[key]; return; }

                var keyWithDash = key.replace(/(\s+)(Summary|Practice|Quiz|Video)$/, ' - $2');
                if (keyWithDash !== key && _dict[keyWithDash]) {
                    el.textContent = _dict[keyWithDash]; return;
                }

                // Dynamic lesson / key-concepts title translation
                if (key.startsWith('Lesson ') || key.startsWith('Key Concepts')) {
                    try {
                        var parts = key.match(/^Lesson\s+(\d+\.\d+)(.*)/);
                        if (parts) {
                            var num = parts[1], rest = parts[2];
                            var suffixMap = {
                                'chinese':     { Practice: ' - 练习', Quiz: ' - 测验', Summary: ' - 总结' },
                                'traditional': { Practice: ' - 练习', Quiz: ' - 测验', Summary: ' - 总结' },
                                'spanish':     { Practice: ' - Práctica', Quiz: ' - Cuestionario', Summary: ' - Resumen' },
                                'hindi':       { Practice: ' - अभ्यास', Quiz: ' - प्रश्नोत्तरी', Summary: ' - सारांश' }
                            };
                            var lessonPrefixMap = {
                                'chinese': '第 {num} 课', 'traditional': '第 {num} 課',
                                'spanish': 'Lección {num}', 'hindi': 'पाठ {num}'
                            };
                            var sepMap = {
                                'chinese': '：', 'traditional': '：',
                                'spanish': ': ', 'hindi': ': '
                            };

                            var suffixes = suffixMap[lang] || suffixMap['chinese'];
                            var lessonPrefix = (lessonPrefixMap[lang] || lessonPrefixMap['chinese']).replace('{num}', num);
                            var sep = sepMap[lang] || '：';

                            var suffix = '';
                            if (rest.includes('Practice')) {
                                suffix = suffixes.Practice; rest = rest.replace(/\s*-?\s*Practice/g, '');
                            } else if (rest.includes('Quiz')) {
                                suffix = suffixes.Quiz; rest = rest.replace(/\s*-?\s*Quiz/g, '');
                            } else if (rest.includes('Summary')) {
                                suffix = suffixes.Summary; rest = rest.replace(/\s*-?\s*Summary/g, '');
                            }

                            var titlePart = rest.replace(/^:\s*/, '').trim();
                            var translatedTitle = _dict[titlePart] || titlePart;
                            var finalStr = lessonPrefix;
                            if (translatedTitle) finalStr += sep + translatedTitle;
                            finalStr += suffix;
                            el.textContent = finalStr;
                        }

                        var kcParts = key.match(/^Key Concepts:\s*(.+)$/);
                        if (kcParts) {
                            var kcTitle = kcParts[1].trim();
                            var translatedKC = _dict[kcTitle] || kcTitle;
                            var kcPrefixMap = {
                                'chinese': '核心概念：', 'traditional': '核心概念：',
                                'spanish': 'Conceptos Clave: ', 'hindi': 'मुख्य अवधारणाएँ: '
                            };
                            el.textContent = (kcPrefixMap[lang] || kcPrefixMap['chinese']) + translatedKC;
                        }
                    } catch (e) { /* skip */ }
                }
            });

            // [data-i18n-ph] — placeholder translations
            var i18nAttrs = document.querySelectorAll('[data-i18n-ph]');
            i18nAttrs.forEach(function (el) {
                var key = el.getAttribute('data-i18n-ph');
                if (key && _dict[key]) el.setAttribute('placeholder', _dict[key]);
            });

            // Page <title>
            var titleText = document.title.trim();
            if (_dict[titleText]) document.title = _dict[titleText];
        }

        // Traditional Chinese conversion
        if (lang === 'traditional' && window.convertToTraditional) {
            var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
            var wNode;
            while (wNode = walker.nextNode()) {
                wNode.nodeValue = window.convertToTraditional(wNode.nodeValue);
            }
            if (document.title) document.title = window.convertToTraditional(document.title);
        }

        _revealPage();
    };

    // ── 9. Expose dict globally so legacy code can access it ──
    window.arisEduTranslations = _dict;
    window.globalTranslations  = _dict;

    // ── 10. Debug helper (same API as before) ──
    window.getTranslationDebugData = function () {
        var lang = null;
        try { lang = localStorage.getItem('arisEduLanguage'); } catch (e) {}
        if (!lang) lang = 'english';
        var totalKeys = Object.keys(_dict).length;
        var i18nElements = document.querySelectorAll('[data-i18n]');
        var matched = 0, unmatched = [];
        i18nElements.forEach(function (el) {
            var key = el.getAttribute('data-i18n');
            if (key && _dict[key]) matched++;
            else if (key && unmatched.length < 10) unmatched.push(key);
        });
        return {
            lang: lang,
            totalKeys: totalKeys,
            section: _section,
            matchableNodes: i18nElements.length,
            matchedNodes: matched,
            unmatchedNodes: i18nElements.length - matched,
            unmatchedSamples: unmatched
        };
    };

    // ── 11. Load translations, then apply on DOMContentLoaded ──
    var _translationsReady = _loadTranslations();

    function _onReady() {
        var lang = null;
        try { lang = localStorage.getItem('arisEduLanguage'); } catch (e) {}
        if (lang && lang !== 'english') {
            _translationsReady.then(function () {
                window.applyTranslations();
            }).catch(function () {
                _revealPage(); // Don't leave page hidden if fetch fails
            });
        } else {
            _revealPage();
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', _onReady);
    } else {
        _onReady();
    }

    // ── 12. Public API: load an additional section dynamically ──
    // Useful for SPAs or pages that change sections without full reload
    window.arisLoadSection = function (sectionName) {
        var code = _langCode();
        if (!code) return Promise.resolve();
        return _loadFile(code, sectionName).then(function (data) {
            _merge(_dict, data);
        });
    };

})();
