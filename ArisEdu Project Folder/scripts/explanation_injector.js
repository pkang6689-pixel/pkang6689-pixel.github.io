/**
 * Explanation Injector
 * Automatically injects quiz explanations into quiz questions after they load
 */

(function() {
    // Watch for quiz questions being added to the DOM
    // Then inject explanations if available
    
    function injectExplanations() {
        const quizQuestions = document.querySelectorAll('.quiz-question');
        
        quizQuestions.forEach((questionEl) => {
            // Skip if already processed
            if (questionEl.dataset.explanationsInjected === 'true') return;
            
            // Mark as processed
            questionEl.dataset.explanationsInjected = 'true';
            
            // Get question text to find matching explanation
            const questionText = questionEl.querySelector('p');
            if (!questionText) return;
            
            const question = questionText.textContent.trim();
            
            // Try to find correct answer
            const correctOption = questionEl.querySelector('input[value="correct"]');
            if (!correctOption) return;
            
            const correctText = correctOption.parentElement.textContent.trim();
            
            // Create explanation from context if available
            // For now, we'll mark it as available for future population
            questionEl.dataset.quizQuestion = question;
            questionEl.dataset.correctAnswer = correctText;
        });
    }
    
    // Run on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectExplanations);
    } else {
        injectExplanations();
    }
    
    // Also watch for dynamically added content (for quiz regeneration/changing questions)
    const observer = new MutationObserver(() => {
        // Debounce the injection to avoid excessive calls
        clearTimeout(observer.timeout);
        observer.timeout = setTimeout(injectExplanations, 100);
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    // Expose a function to manually inject explanations with quiz data
    window.injectQuizExplanations = function(explanations) {
        if (!explanations || typeof explanations !== 'object') return;
        
        const quizQuestions = document.querySelectorAll('.quiz-question');
        quizQuestions.forEach((questionEl, index) => {
            if (explanations[index]) {
                questionEl.dataset.explanation = explanations[index];
            }
        });
    };
})();
