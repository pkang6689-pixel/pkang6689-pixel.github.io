/**
 * Quiz Explanation Injector
 * Watches for quiz feedback and injects explanations
 */

(function() {
    let observer;
    let quizLoaderRetries = 0;
    const maxRetries = 50;
    
    // Function to inject explanation into current feedback
    function injectExplanation() {
        // Need access to quizLoader
        if (!window.quizLoader) {
            return false;
        }

        const loader = window.quizLoader;
        if (!loader.selectedQuestions || !loader.selectedQuestions[loader.currentQuestionIndex]) {
            console.log('No selectedQuestions or current question found');
            return false;
        }

        const currentQ = loader.selectedQuestions[loader.currentQuestionIndex];
        const explanation = currentQ.explanation;
        
        if (!explanation) {
            console.log('No explanation for question at index', loader.currentQuestionIndex);
            return false;
        }

        // Find the feedback div
        const feedbackDiv = document.querySelector('.answer-feedback');
        if (!feedbackDiv) {
            return false;
        }

        // Check if explanation already added
        if (feedbackDiv.parentElement.querySelector('.explanation-box')) {
            return true; // Already there
        }

        // Create explanation box
        const explanationBox = document.createElement('div');
        explanationBox.className = 'explanation-box';
        explanationBox.style.marginTop = '1rem';
        explanationBox.style.padding = '1rem';
        explanationBox.style.borderRadius = '0.5rem';
        explanationBox.style.backgroundColor = '#f0f9ff';
        explanationBox.style.borderLeft = '4px solid #3b82f6';
        explanationBox.style.color = '#1e40af';
        explanationBox.style.fontSize = '0.95rem';
        explanationBox.innerHTML = `<strong style="color: #1e40af;">Explanation:</strong><br/>${explanation}`;
        
        // Insert after feedback
        feedbackDiv.parentElement.insertBefore(explanationBox, feedbackDiv.nextSibling);
        console.log('✓ Explanation injected:', explanation.substring(0, 50) + '...');
        return true;
    }

    // Set up mutation observer to watch for feedback div
    function setupObserver() {
        if (observer) return;
        
        observer = new MutationObserver(() => {
            // When DOM changes, try to inject explanation
            setTimeout(injectExplanation, 50);
        });

        const container = document.querySelector('[rel="diagram-container"]') || document.body;
        observer.observe(container, {
            childList: true,
            subtree: true,
            characterData: false
        });
        
        console.log('✓ Mutation observer set up for explanation injection');
    }

    // Try to set up observer with quizLoader
    function initializeInjection() {
        quizLoaderRetries++;
        
        if (window.quizLoader) {
            console.log('✓ quizLoader found, setting up observation');
            setupObserver();
            
            // Hook renderQuiz to trigger injection
            const originalRender = window.quizLoader.renderQuiz;
            window.quizLoader.renderQuiz = function() {
                originalRender.call(this);
                setTimeout(() => {
                    console.log('→ renderQuiz called, attempting injection...');
                    injectExplanation();
                }, 100);
            };
        } else if (quizLoaderRetries < maxRetries) {
            setTimeout(initializeInjection, 200);
        } else {
            console.log('⚠ quizLoader not found after max retries');
        }
    }

    // Start when document is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeInjection);
    } else {
        initializeInjection();
    }
})();
