
/* 
    Quiz Logic for Unit Reviews
    Contains functions for checking answers and handling quiz interactions.
*/

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
            attemptsInfo.textContent = "Please select an option.";
            attemptsInfo.style.color = "#ef4444";
            setTimeout(() => {
                attemptsInfo.textContent = originalText;
                attemptsInfo.style.color = "#64748b";
            }, 2000);
        } else {
            alert("Please select an answer first.");
        }
        return;
    }

    let attempts = parseInt(parent.dataset.attempts || "2");

    if (selectedValue === correctValue) {
        // Correct Answer
        parent.dataset.status = 'correct';
        if (attemptsInfo) {
            attemptsInfo.textContent = "Correct!";
            attemptsInfo.style.color = "#10b981"; // Green
        }
        
        // Disable interactions
        inputs.forEach(i => i.disabled = true);
        buttonElement.disabled = true;
        buttonElement.textContent = "Correct";
        buttonElement.style.background = "#10b981";
        buttonElement.style.color = "white";
        buttonElement.style.border = "none";
        
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
                attemptsInfo.textContent = `Incorrect. ${attempts} attempts left.`;
                attemptsInfo.style.color = "#f59e0b"; // Orange/Yellow
            }
        } else {
            // No attempts left
            if (attemptsInfo) {
                attemptsInfo.textContent = `Incorrect. The correct answer was ${correctValue.toUpperCase()}.`;
                attemptsInfo.style.color = "#ef4444"; // Red
            }
            parent.dataset.status = 'incorrect';
            
            // Disable interactions
            inputs.forEach(i => i.disabled = true);
            buttonElement.disabled = true;
            buttonElement.textContent = "Incorrect";
            buttonElement.style.background = "#ef4444";
            buttonElement.style.color = "white";
            buttonElement.style.border = "none";

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
    alert("No additional questions are currently available for this topic.");
};
