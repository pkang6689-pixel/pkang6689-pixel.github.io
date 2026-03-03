
/* 
    Quiz Logic for Unit Reviews
    Contains functions for checking answers and handling quiz interactions.
*/

function _t(key, fallback) {
    var langMode = null;
    try { langMode = localStorage.getItem('arisEduLanguage'); } catch(e) {}
    
    // Default to English if no language preference
    var isEnglish = (!langMode || langMode === 'english');
    
    if (isEnglish) {
        // English mode: return English (key itself as fallback)
        return fallback || key;
    }
    
    // Spanish mode
    if (langMode === 'spanish') {
        var es = window.arisEduSpanishTranslations;
        return (es && es[key]) || fallback || key;
    }

    // Chinese mode: return Chinese translation
    var t = window.arisEduTranslations || window.globalTranslations;
    return (t && t[key]) || fallback || key;
}

window.checkQuizAnswer = function(questionId, correctValue, buttonElement) {
    const parent = buttonElement.closest('.quiz-question');
    if (!parent) return;

    // Find all inputs for this question
    const inputs = parent.querySelectorAll(`input[name="${questionId}"]`);
    let selectedValue = null;
    
    inputs.forEach(input => {
        if (input.checked) {
            selectedValue = input.value;
        }
    });

    const attemptsInfo = parent.querySelector('.attempts-indicator');

    if (!selectedValue) {
        // Visual feedback for no selection
        if (attemptsInfo) {
            const originalText = attemptsInfo.textContent;
            attemptsInfo.textContent = _t("Please select an option.");
            attemptsInfo.style.color = "#ef4444";
            setTimeout(() => {
                attemptsInfo.textContent = originalText;
                attemptsInfo.style.color = "#64748b";
            }, 2000);
        } else {
            alert(_t("Please select an answer first."));
        }
        return;
    }

    let attempts = parseInt(parent.dataset.attempts || "2");

    // Helper function to display explanation if available
    function displayExplanation(parent) {
        const explanation = parent.dataset.explanation;
        if (explanation) {
            // Remove old explanation if exists
            const existingExpl = parent.querySelector('.explanation-text');
            if (existingExpl) existingExpl.remove();
            
            // Create explanation div
            const expl = document.createElement('div');
            expl.className = 'explanation-text';
            expl.style.marginTop = '1rem';
            expl.style.padding = '1rem';
            expl.style.borderRadius = '0.5rem';
            expl.style.backgroundColor = '#f0f9ff';
            expl.style.borderLeft = '4px solid #3b82f6';
            expl.style.color = '#1e40af';
            expl.style.fontSize = '0.95rem';
            expl.style.lineHeight = '1.5';
            expl.innerHTML = '<strong>Explanation:</strong> ' + explanation;
            parent.appendChild(expl);
        }
    }

    if (selectedValue === correctValue) {
        // Correct Answer
        parent.dataset.status = 'correct';
        if (attemptsInfo) {
            attemptsInfo.textContent = _t("Correct!", "Correct!");
            attemptsInfo.style.color = "#10b981"; // Green
        }
        
        // Award Quiz Master Badge
        if (window.BadgeSystem) {
            window.BadgeSystem.award('quiz_master');
        }

        // Disable interactions
        inputs.forEach(i => i.disabled = true);
        buttonElement.disabled = true;
        buttonElement.textContent = _t("Correct", "Correct");
        buttonElement.style.background = "#10b981";
        buttonElement.style.color = "white";
        buttonElement.style.border = "none";
        
        // Display explanation
        displayExplanation(parent);
        
        // Hide "Get another question" button if it exists nearby
        const siblings = parent.querySelectorAll('button');
        siblings.forEach(btn => {
            if (btn !== buttonElement) btn.style.display = 'none';
        });

    } else {
        // Incorrect Answer
        attempts--;
        parent.dataset.attempts = attempts;
        
        if (attempts > 0) {
            if (attemptsInfo) {
                attemptsInfo.textContent = _t("Incorrect.", "Incorrect.") + " " + attempts + " " + _t("attempts left.", "attempts left.");
                attemptsInfo.style.color = "#f59e0b"; // Orange/Yellow
            }
        } else {
            // No attempts left
            if (attemptsInfo) {
                attemptsInfo.textContent = _t("Incorrect. The correct answer was", "Incorrect. The correct answer was") + " " + correctValue.toUpperCase() + ".";
                attemptsInfo.style.color = "#ef4444"; // Red
            }
            parent.dataset.status = 'incorrect';
            
            // Disable interactions
            inputs.forEach(i => i.disabled = true);
            buttonElement.disabled = true;
            buttonElement.textContent = _t("Incorrect", "Incorrect");
            buttonElement.style.background = "#ef4444";
            buttonElement.style.color = "white";
            buttonElement.style.border = "none";

            // Display explanation
            displayExplanation(parent);

             // Hide "Get another question" button
             const siblings = parent.querySelectorAll('button');
             siblings.forEach(btn => {
                 if (btn !== buttonElement) btn.style.display = 'none';
             });
        }
    }
    
    // Update global completion status
    if (window.checkQuizCompletion) {
        window.checkQuizCompletion();
    }
};

window.getAnotherQuestion = function(buttonElement) {
    // Stub for future functionality
    // Since we don't have a backend or extra questions loaded, we alert the user.
    alert(_t("No additional questions are currently available for this topic."));
};
