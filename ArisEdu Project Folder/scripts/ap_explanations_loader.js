/**
 * AP Course Explanation Loader
 * Loads explanations from AP course JSON files and injects them into quiz questions
 */

(function() {
    // Get course info from URL or session storage
    function getCourseInfo() {
        const url = window.location.pathname;
        const session = sessionStorage.getItem('courseOrigin') || '';
        
        // Try to extract course from URL patterns
        // e.g., /APLessons/AP Biology/Unit1/Lesson1.1_Video.html
        // or /AP_Unit_Tests/AP Biology/Unit1/unit_tests.html
        
        const courseMatch = url.match(/(?:APLessons|AP_Unit_Tests)\/([^\/]+)\//);
        if (courseMatch) {
            return courseMatch[1].replace(/%20/g, ' ');
        }
        
        return null;
    }
    
    // Map course names to JSON file names
    function getCourseJsonFile(courseName) {
        const courseMap = {
            'AP Biology': 'ap_biology_lessons.json',
            'AP Calculus AB': 'ap_calculus_ab_lessons.json',
            'AP Chemistry': 'ap_chemistry_lessons.json',
            'AP Environmental Science': 'ap_environmental_science_lessons.json',
            'AP Human Geography': 'ap_human_geography_lessons.json',
            'AP Physics 2': 'ap_physics_2_lessons.json',
            'AP Physics C - Mechanics': 'ap_physics_c_-_mechanics_lessons.json',
            'AP Statistics': 'ap_statistics_lessons.json'
        };
        return courseMap[courseName];
    }
    
    // Load and inject explanations
    window.loadAndInjectExplanations = function() {
        const courseName = getCourseInfo();
        if (!courseName) return; // Not an AP course
        
        const jsonFile = getCourseJsonFile(courseName);
        if (!jsonFile) return; // Unknown course
        
        // Load the JSON file with timeout protection
        var timeout = new Promise(function(_, reject) {
          setTimeout(function() { reject(new Error('Explanations fetch timeout')); }, 5000);
        });
        
        Promise.race([
          fetch(`/content_data/AP_Courses/${jsonFile}`),
          timeout
        ])
            .then(response => response.json())
            .then(data => {
                // Get all quiz questions from all lessons
                const allQuestions = [];
                for (const lesson of Object.values(data)) {
                    if (lesson.quiz_questions && Array.isArray(lesson.quiz_questions)) {
                        allQuestions.push(...lesson.quiz_questions);
                    }
                }
                
                // Inject explanations
                injectExplanationsIntoQuiz(allQuestions);
            })
            .catch(err => console.warn('Could not load explanations:', err.message || err));
    };
    
    // Inject explanations into quiz questions
    function injectExplanationsIntoQuiz(questions) {
        const quizElements = document.querySelectorAll('.quiz-question');
        
        // Match quiz elements with questions data
        // This is tricky because we need to match the question text
        quizElements.forEach((qEl) => {
            const questionText = qEl.querySelector('p');
            if (!questionText) return;
            
            const displayedQuestion = questionText.textContent.trim();
            
            // Find matching question in our data
            const matchingQuestion = questions.find(q => {
                const dataQuestion = q.question_text || '';
                return dataQuestion.toLowerCase().includes(displayedQuestion.substring(0, 50).toLowerCase());
            });
            
            if (matchingQuestion && matchingQuestion.explanation) {
                qEl.dataset.explanation = matchingQuestion.explanation;
            }
        });
    }
    
    // Trigger on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(window.loadAndInjectExplanations, 500);
        });
    } else {
        setTimeout(window.loadAndInjectExplanations, 500);
    }
})();
