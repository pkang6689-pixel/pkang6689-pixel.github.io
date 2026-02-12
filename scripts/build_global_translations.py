import json
import re

def main():
    # 1. Read UI translations
    ui_translations = {}
    try:
        with open('ui_translations.json', 'r', encoding='utf-8') as f:
            ui_translations = json.load(f)
    except Exception as e:
        print(f"Error reading ui_translations.json: {e}")

    # 2. Read new flashcard translations
    flashcard_translations = {}
    try:
        with open('flashcard_translations.json', 'r', encoding='utf-8') as f:
            flashcard_translations = json.load(f)
    except Exception as e:
        print(f"Error reading flashcard_translations.json: {e}")

    # 2b. Read summary translations
    summary_translations = {}
    try:
        with open('summary_translations.json', 'r', encoding='utf-8') as f:
            summary_translations = json.load(f)
    except Exception as e:
        print(f"Error reading summary_translations.json: {e}")

    # 3. Merge
    merged = ui_translations.copy()
    merged.update(flashcard_translations)
    merged.update(summary_translations)

    print(f"Merged {len(ui_translations)} UI, {len(flashcard_translations)} flashcards, {len(summary_translations)} summaries. Total: {len(merged)}")

    # 4. Generate JavaScript Content
    js_content = """/* Global Translations for ArisEdu */
(function() {
    const translations = %JSON_CONTENT%;

    function translateNode(node) {
        if (node.nodeType === 3) { // Text node
             let text = node.nodeValue;
             if (!text.trim()) return;
             
             // Exact match check first (Performance)
             if (translations[text.trim()]) {
                 node.nodeValue = node.nodeValue.replace(text.trim(), translations[text.trim()]);
                 return;
             }
             
             // Fallback for partial matches (as per original logic)
             // Iterate keys efficiently? With 1000 keys, loop is slow.
             // Original logic looped. Let's optimize: only loop if exact match fails.
             // Actually, the original logic had a regex loop.
             // "Object.keys(translations).forEach..." 
             // With 1000 keys, doing this on every text node is very heavy.
             // We should prioritize exact matches or larger-phrase matches.
             
             // Optimization: Use a regex to match any key?
             // Constructing a regex of 1000 items is huge.
             
             // Let's stick to the original logic for now but maybe verify performance later?
             // Or at least, only do it for English-looking text.
             
             // Wait, the original applied regex replace for EVERY key.
             // That is O(N_keys * M_text_nodes). With 1000 keys, this will lag.
             
             // Improved Strategy:
             // 1. Exact match lookup.
             // 2. Only if needed, specific replacements for UI terms.
             // Flashcards tend to be full sentences. Exact match is best.
             
             if (translations[text]) {
                 node.nodeValue = translations[text];
                 return;
             }
             
             // Try trimming
             if (translations[text.trim()]) {
                 node.nodeValue = text.replace(text.trim(), translations[text.trim()]);
                 return;
             }
             
             // Legacy loop for UI fragments
             const uiKeys = [
               "Settings", "Appearance", "Account", "Notifications", "Search", 
               "Homepage", "Courses", "Play", "Preferences", "Dark Mode"
               // ... (We might need to categorize them, but for now let's skip the massive loop for performance unless critical)
             ];
             
             // To be safe, we will ONLY do exact/trimmed match for the flashcards.
             // And we can run the loop for short strings?
             
             // Let's iterate ALL keys but check if the key is contained in text first?
             // No, "text.includes(key)".
             
             // Basic implementation for now (might be slow but functional)
             Object.keys(translations).forEach(function(en) {
                if (text.includes(en)) {
                   // Escape special regex chars
                   const escapedEn = en.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
                   text = text.replace(new RegExp(escapedEn, "g"), translations[en]);
                }
             });
             node.nodeValue = text;
             
        } else if (node.nodeType === 1 && node.childNodes.length) {
            // Validate it's not a script or style
            const tag = node.tagName.toLowerCase();
            if (tag === 'script' || tag === 'style') return;
            
            for (let i = 0; i < node.childNodes.length; i++) {
                translateNode(node.childNodes[i]);
            }
        }
    }

    window.applyTranslations = function() {
        if (localStorage.getItem("arisEduLanguage") === "chinese") {
            translateNode(document.body);
            document.documentElement.lang = 'zh';
        }
    };
    
    // Auto-run
    if (document.readyState === 'loading') {
        window.addEventListener("DOMContentLoaded", window.applyTranslations);
    } else {
        window.applyTranslations();
    }

    // Observer
    const observer = new MutationObserver(function(mutations) {
        if (localStorage.getItem("arisEduLanguage") === "chinese") {
            mutations.forEach(function(mutation) {
                mutation.addedNodes.forEach(function(node) {
                    translateNode(node);
                });
                // Handle text content changes on existing nodes
                 if (mutation.type === 'characterData') {
                     // Infinite loop risk if we translate translated text? 
                     // translateNode updates nodeValue -> triggers characterData
                     // We need to check if it's already translated?
                     // Or just check if the new text is in our english dictionary.
                     // translations keys are English. If text is Chinese, it won't be in keys.
                     translateNode(mutation.target);
                 }
            });
        }
    });
    
    // observe characterData to catch simple text updates (like flashcards)
    // NOTE: 'subtree: true' with 'characterData: true' is needed.
    window.onload = function() {
        if(document.body) {
            observer.observe(document.body, { childList: true, subtree: true, characterData: true });
        }
    }

})();
"""
    # Inject JSON
    json_str = json.dumps(merged, ensure_ascii=False, indent=2)
    js_content = js_content.replace('%JSON_CONTENT%', json_str)

    with open('global_translations.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print("Created global_translations.js")

if __name__ == '__main__':
    main()
