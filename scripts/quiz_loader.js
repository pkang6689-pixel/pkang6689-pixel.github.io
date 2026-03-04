// Generic Quiz Loader - Loads and displays lesson quizzes from JSON lesson files
class QuizLoader {
  constructor() {
    this.currentQuestionIndex = 0;
    this.userAnswers = {};
    this.quizData = null;
    this.lessonInfo = null;
    this.allQuestions = null; // Store all 20 questions
    this.selectedQuestions = null; // Store 7 selected questions
    this.askedQuestionIndices = new Set(); // Track which of the 7 have been shown
    this.startTime = null; // Track when quiz started
    
    // Course slug mappings
    this.courseMapping = {
      'AP Biology': 'ap_biology',
      'AP Chemistry': 'ap_chemistry',
      'AP Environmental Science': 'ap_environmental_science',
      'AP Human Geography': 'ap_human_geography',
      'AP Calculus AB': 'ap_calculus_ab',
      'AP Statistics': 'ap_statistics',
      'AP Physics 2': 'ap_physics_2',
      'AP Physics C': 'ap_physics_c_-_mechanics',
      'AP Physics C - Mechanics': 'ap_physics_c_-_mechanics'
    };
    
    this.lessonCourseMapping = {
      'Algebra 1': 'algebra_1',
      'Algebra 2': 'algebra_2',
      'Biology': 'biology',
      'Chemistry': 'chemistry',
      'Geometry': 'geometry',
      'Physics': 'physics'
    };
  }

  // Parse course, unit, and lesson from the current page URL
  parseLocationInfo() {
    const path = window.location.pathname;
    
    // URL-encoded spaces are %20, so handle both encoded and decoded versions
    // Match AP pattern: /ArisEdu%20Project%20Folder/APLessons/{Course}/Unit {Number}/Lesson{number}_(Quiz|Practice).html
    let match = path.match(/ArisEdu(?:%20|\s)Project(?:%20|\s)Folder.*?APLessons[\/\\]([^\/\\]+)[\/\\]Unit(?:%20|\s)?(\d+)[\/\\]Lesson(?:%20|\s)?(\d+\.\d+)_(Quiz|Practice)/i);
    if (match) {
      const courseFolder = match[1].replace(/%20/g, ' ');
      const unit = parseInt(match[2]);
      const lesson = match[3];
      return { courseFolder, unit, lesson, isAP: true };
    }
    
    // Match regular pattern: /ArisEdu%20Project%20Folder/{CourseName}Lessons/Unit {Number}/Lesson{number}_(Quiz|Practice).html
    match = path.match(/ArisEdu(?:%20|\s)Project(?:%20|\s)Folder.*?(\w+)Lessons[\/\\]Unit(?:%20|\s)?(\d+)[\/\\]Lesson(?:%20|\s)?(\d+\.\d+)_(Quiz|Practice)/i);
    if (match) {
      const coursePrefix = match[1];  // e.g., "Algebra1", "Biology", "Chemistry"
      const unit = parseInt(match[2]);
      const lesson = match[3];
      
      // Map course prefixes to display names
      const courseNameMap = {
        'Algebra1': 'Algebra 1',
        'Algebra2': 'Algebra 2',
        'Biology': 'Biology',
        'Chemistry': 'Chemistry',
        'Geometry': 'Geometry',
        'Physics': 'Physics',
        'MS_Algebra1': 'Algebra 1',
        'MS_Algebra2': 'Algebra 2',
        'MS_Biology': 'Biology',
        'MS_Chemistry': 'Chemistry',
        'MS_Geometry': 'Geometry',
        'MS_Physics': 'Physics'
      };
      
      const courseFolder = courseNameMap[coursePrefix] || coursePrefix;
      return { courseFolder, unit, lesson, isAP: false };
    }
    
    return null;
  }

  // Get the slug for a course name
  getCourseSlug(courseName, isAP) {
    if (isAP) {
      for (const [name, slug] of Object.entries(this.courseMapping)) {
        if (name === courseName || name.replace(/\s+/g, '%20') === courseName) {
          return slug;
        }
      }
      return courseName.toLowerCase().replace(/\s+/g, '_');
    } else {
      for (const [name, slug] of Object.entries(this.lessonCourseMapping)) {
        if (name === courseName || name.replace(/\s+/g, '%20') === courseName) {
          return slug;
        }
      }
      return courseName.toLowerCase().replace(/\s+/g, '_');
    }
  }

  // Shuffle array and select N items
  shuffleAndSelect(array, count) {
    const shuffled = [...array].sort(() => Math.random() - 0.5);
    return shuffled.slice(0, Math.min(count, shuffled.length));
  }

  // Load the lesson JSON data
  async loadQuizData() {
    const locationInfo = this.parseLocationInfo();
    if (!locationInfo) {
      console.error('Could not determine course, unit, and lesson from URL');
      return false;
    }

    const { courseFolder, unit, lesson, isAP } = locationInfo;
    const courseSlug = this.getCourseSlug(courseFolder, isAP);
    
    // Construct the path to the JSON file
    let jsonPath;
    if (isAP) {
      // AP courses: from ArisEdu Project Folder/APLessons/{Course}/Unit X/ to root = 4 levels up
      // Unit X -> {Course} -> APLessons -> ArisEdu Project Folder -> root
      jsonPath = `../../../../content_data/AP_Courses/${courseSlug}_lessons.json`;
    } else {
      // Regular courses: from ArisEdu Project Folder/{Course}Lessons/Unit X/ to root = 3 levels up
      // Unit X -> {Course}Lessons -> ArisEdu Project Folder -> root
      jsonPath = `../../../content_data/${courseSlug}_lessons.json`;
    }

    try {
      const response = await fetch(jsonPath);
      if (!response.ok) {
        console.error(`Failed to load: ${jsonPath} (Status: ${response.status})`);
        return false;
      }
      
      const allLessons = await response.json();
      
      // Construct the lesson key (e.g., "u1_l1.1")
      const lessonParts = lesson.split('.');
      const lessonKey = `u${unit}_l${lesson}`;
      
      // Find the lesson in the JSON object
      let foundLesson = allLessons[lessonKey];
      
      if (!foundLesson) {
        console.error(`Lesson key not found: ${lessonKey}`);
        console.error('Available keys sample:', Object.keys(allLessons).slice(0, 10));
        return false;
      }
      
      if (!foundLesson.quiz_questions || foundLesson.quiz_questions.length === 0) {
        console.error(`No quiz questions found for lesson ${lessonKey}`);
        return false;
      }
      
      this.lessonInfo = {
        course: courseFolder,
        unit: unit,
        lesson: lesson,
        title: foundLesson.title
      };
      
      // Transform the quiz questions to a standard format
      const transformedQuestions = foundLesson.quiz_questions.map((q, idx) => {
        // Handle both old format (with options array) and new format (with option objects)
        let options = [];
        let answer = '';
        
        if (q.options && Array.isArray(q.options)) {
          // New format: options are objects with text and is_correct
          options = q.options.map(opt => opt.text || opt);
          const correctOpt = q.options.find(opt => opt.is_correct);
          answer = correctOpt ? correctOpt.text : '';
        } else if (q.question_options) {
          // Alternative format
          options = q.question_options.map(opt => opt.text || opt);
          const correctOpt = q.question_options.find(opt => opt.is_correct);
          answer = correctOpt ? correctOpt.text : '';
        }
        
        return {
          q: q.question_text || q.question || q.q || '',
          question: q.question_text || q.question || q.q || '',
          options: options,
          answer: answer,
          difficulty: q.difficulty || 'medium',
          explanation: q.explanation || ''
        };
      });
      
      // Store all questions and select 7 random ones
      this.allQuestions = transformedQuestions;
      this.selectedQuestions = this.shuffleAndSelect(transformedQuestions, 7);
      
      this.quizData = {
        questions: this.selectedQuestions,
        course: courseFolder,
        unit: unit,
        lesson: lesson,
        lessonTitle: foundLesson.title
      };
      
      this.currentQuestionIndex = 0;
      this.userAnswers = {};
      this.submittedAnswers = {}; // Track which answers have been submitted for feedback
      this.attemptCounts = {}; // Track number of attempts per question (max 2)
      this.askedQuestionIndices = new Set();
      this.startTime = Date.now(); // Record when quiz started
      return true;
    } catch (error) {
      console.error('Error loading quiz data:', error);
      return false;
    }
  }

  // Render the quiz interface
  renderQuiz() {
    const container = document.getElementById('quiz-content-view');
    if (!container) {
      console.error('quiz-content-view container not found');
      return;
    }

    if (!this.quizData || !this.quizData.questions) {
      container.innerHTML = '<div class="diagram-card"><p>Could not load quiz data.</p></div>';
      return;
    }

    const totalQuestions = this.quizData.questions.length; // This is now 7
    const question = this.quizData.questions[this.currentQuestionIndex];

    let html = `
      <div class="quiz-container">
        <div class="quiz-header">
          <h2 class="page-title">${this.quizData.course} - Unit ${this.quizData.unit} - Lesson ${this.quizData.lesson}</h2>
          <p class="lesson-title">${this.quizData.lessonTitle}</p>
          <div class="quiz-progress">
            Question ${this.currentQuestionIndex + 1} of ${totalQuestions}
            <div class="progress-bar" style="width: ${((this.currentQuestionIndex + 1) / totalQuestions) * 100}%"></div>
          </div>
        </div>

        <div class="diagram-card quiz-question">
          <div class="question-wrapper">
            <h3 class="question-text">${question.question || question.q}</h3>
            
            <div class="options-container">
    `;

    // Handle different answer formats
    const options = question.options || question.answers || [];
    const optionLetters = ['A', 'B', 'C', 'D', 'E'];
    const attempts = this.attemptCounts[this.currentQuestionIndex] || 0;
    const isLocked = attempts >= 2;
    
    options.forEach((option, index) => {
      if (index >= optionLetters.length) return;
      
      const optionText = typeof option === 'string' ? option : option.text || option;
      const inputId = `option_${index}`;
      const isSelected = this.userAnswers[this.currentQuestionIndex] === optionText;
      
      html += `
        <label class="option-label ${isSelected ? 'selected' : ''}">
          <input 
            type="radio" 
            name="answer" 
            value="${optionText.replace(/"/g, '&quot;')}" 
            id="${inputId}"
            ${isSelected ? 'checked' : ''}
            ${isLocked ? 'disabled' : ''}
            onchange="quizLoader.selectAnswer('${optionText.replace(/'/g, "\\'")}')"
          />
          <span class="option-letter">${optionLetters[index]}</span>
          <span class="option-text">${optionText}</span>
        </label>
      `;
    });

    html += `
            </div>

            <div class="question-meta">
              <span class="question-id">Q${this.currentQuestionIndex + 1}</span>
              <div class="question-meta-right">
                <button class="nav-meta-button" onclick="quizLoader.previousQuestion()" ${this.currentQuestionIndex === 0 ? 'disabled' : ''} title="Go to previous question">← Prev</button>
                <span class="attempt-counter">Attempts: ${attempts} / 2</span>
                <button class="skip-button" onclick="quizLoader.skipQuestion()" ${this.currentQuestionIndex === totalQuestions - 1 ? 'disabled' : ''} title="Skip this question">Skip →</button>
              </div>
            </div>
            
            ${this.submittedAnswers[this.currentQuestionIndex] ? `
              ${(() => {
                const correctAnswer = question.answer || question.correct_answer;
                const userAnswer = this.userAnswers[this.currentQuestionIndex];
                const isCorrect = userAnswer === correctAnswer;
                return `
                  <div class="answer-feedback ${isCorrect ? 'correct-feedback' : 'incorrect-feedback'}">
                    <div class="feedback-header">
                      ${isCorrect ? '✓ Correct!' : '✗ Incorrect'}
                    </div>
                    <div class="feedback-content">
                      <p>Your answer: <strong>${userAnswer}</strong></p>
                      ${attempts < 2 && !isCorrect ? `<p class="attempt-remaining">You have ${2 - attempts} attempt remaining.</p>` : ''}
                      ${attempts >= 2 && !isCorrect ? `<p class="no-attempts">No more attempts available for this question.</p>` : ''}
                    </div>
                  </div>
                  ${question.explanation ? `
                    <div class="explanation-box" style="margin-top: 1rem; padding: 1rem; border-radius: 0.5rem; background-color: #f0f9ff; border-left: 4px solid #3b82f6; color: #1e40af; font-size: 0.95rem;">
                      <strong style="color: #1e40af;">Explanation:</strong><br/>${question.explanation}
                    </div>
                  ` : ''}
                `;
              })()}
            ` : ''}
          </div>

          <div class="question-navigation">
            ${(() => {
              const correctAnswer = question.answer || question.correct_answer;
              const wasSubmitted = this.submittedAnswers[this.currentQuestionIndex];
              const userAnswer = this.userAnswers[this.currentQuestionIndex];
              const isCorrect = userAnswer === correctAnswer;
              const hasAttemptsLeft = attempts < 2;
              
              // If out of attempts and got it wrong, show "Get another question" button
              if (attempts >= 2 && wasSubmitted && !isCorrect) {
                return `
                  <button 
                    class="nav-button another-button" 
                    onclick="quizLoader.getAnotherQuestion()"
                  >
                    Get Another Question
                  </button>
                `;
              }
              
              // Show submit button if: never submitted, OR (submitted wrong AND has attempts left)
              const shouldShowSubmit = !wasSubmitted || (!isCorrect && hasAttemptsLeft);
              
              if (shouldShowSubmit) {
                return `
                  <button 
                    class="nav-button submit-button" 
                    onclick="quizLoader.submitQuestion()"
                    ${!userAnswer ? 'disabled' : ''}
                  >
                    Submit Answer
                  </button>
                `;
              } else {
                // Check if on last question and it's been answered
                const isLastQuestion = this.currentQuestionIndex === totalQuestions - 1;
                const lastQuestionAnswered = this.submittedAnswers[this.currentQuestionIndex];
                
                if (isLastQuestion && lastQuestionAnswered) {
                  // Show "View Results" button on last question after answering
                  return `
                    <button 
                      class="nav-button results-button" 
                      onclick="quizLoader.completeQuiz()"
                      style="background: #16a34a; font-weight: bold;"
                    >
                      View Results
                    </button>
                  `;
                }
                
                return `
                  <button 
                    class="nav-button prev-button" 
                    onclick="quizLoader.previousQuestion()"
                    ${this.currentQuestionIndex === 0 ? 'disabled' : ''}
                  >
                    ← Previous
                  </button>
                  
                  <button 
                    class="nav-button next-button" 
                    onclick="quizLoader.nextQuestion()"
                    ${isLastQuestion ? 'disabled' : ''}
                  >
                    Next →
                  </button>
                `;
              }
            })()}
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // Select an answer
  selectAnswer(answer) {
    // If this is a retry after a wrong submission, clear the submitted state
    // so they can submit again with the new answer
    if (this.submittedAnswers[this.currentQuestionIndex] && 
        this.userAnswers[this.currentQuestionIndex] !== answer) {
      delete this.submittedAnswers[this.currentQuestionIndex];
    }
    
    this.userAnswers[this.currentQuestionIndex] = answer;
    this.renderQuiz();
  }

  // Submit answer for current question and show feedback
  submitQuestion() {
    if (!this.userAnswers[this.currentQuestionIndex]) {
      return; // Don't submit if no answer selected
    }
    
    // Initialize attempt count if not exists
    if (!this.attemptCounts[this.currentQuestionIndex]) {
      this.attemptCounts[this.currentQuestionIndex] = 0;
    }
    
    // Check if already at max attempts
    if (this.attemptCounts[this.currentQuestionIndex] >= 2) {
      return;
    }
    
    // Increment attempt count and mark as submitted
    this.attemptCounts[this.currentQuestionIndex]++;
    this.submittedAnswers[this.currentQuestionIndex] = true;
    this.renderQuiz();
  }

  // Navigate to next question
  nextQuestion() {
    if (this.currentQuestionIndex < this.quizData.questions.length - 1) {
      this.currentQuestionIndex++;
      this.renderQuiz();
    }
  }

  // Navigate to previous question
  previousQuestion() {
    if (this.currentQuestionIndex > 0) {
      this.currentQuestionIndex--;
      this.renderQuiz();
    }
  }

  // Redo the current question (reset its state)
  getAnotherQuestion() {
    // Get a random question from the 7, different from current if possible
    const totalQuestions = this.quizData.questions.length;
    let newIndex = Math.floor(Math.random() * totalQuestions);
    
    // Try to get a different question if possible
    let attempts = 0;
    while (newIndex === this.currentQuestionIndex && attempts < 5) {
      newIndex = Math.floor(Math.random() * totalQuestions);
      attempts++;
    }
    
    this.currentQuestionIndex = newIndex;
    this.renderQuiz();
  }

  // Skip to the next question
  skipQuestion() {
    if (this.currentQuestionIndex < this.quizData.questions.length - 1) {
      this.currentQuestionIndex++;
      this.renderQuiz();
    }
  }

  // Show complete quiz results
  completeQuiz() {
    const container = document.getElementById('quiz-content-view');
    const totalQuestions = this.quizData.questions.length;
    let correct = 0;

    // Calculate score
    this.quizData.questions.forEach((question, index) => {
      const correctAnswer = question.answer || question.correct_answer;
      if (this.userAnswers[index] === correctAnswer) {
        correct++;
      }
    });

    const percentage = (correct / totalQuestions) * 100;
    const grade = this.getLetterGrade(percentage);
    
    // Calculate time spent
    const timeSpent = this.startTime ? Math.round((Date.now() - this.startTime) / 1000) : 0;
    const minutes = Math.floor(timeSpent / 60);
    const seconds = timeSpent % 60;
    const timeDisplay = minutes > 0 ? `${minutes}m ${seconds}s` : `${seconds}s`;
    
    // Award tokens
    const tokensReward = 300;
    this.awardTokens(tokensReward);

    let html = `
      <div class="quiz-results">
        <style>
          .tokens-reward-popup {
            background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            border: 3px solid #b45309;
            border-radius: 1rem;
            padding: 2rem;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 10px 40px rgba(245, 158, 11, 0.4);
            animation: popupBounce 0.6s ease-out;
          }
          .tokens-reward-popup .emoji { font-size: 3rem; margin-bottom: 0.5rem; }
          .tokens-reward-popup .amount { font-size: 2.5rem; font-weight: bold; color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
          .tokens-reward-popup .label { font-size: 1.2rem; color: rgba(255,255,255,0.95); margin-top: 0.5rem; font-weight: 600; }
          @keyframes popupBounce {
            0% { transform: scale(0.8) translateY(-20px); opacity: 0; }
            60% { transform: scale(1.1); }
            100% { transform: scale(1) translateY(0); opacity: 1; }
          }
          .time-spent { font-size: 1rem; color: #666; margin-top: 0.5rem; }
        </style>
        <div class="tokens-reward-popup">
          <div class="emoji">💎</div>
          <div class="amount">+${tokensReward}</div>
          <div class="label">Arcade Tokens Awarded!</div>
          <div class="time-spent">Time spent: ${timeDisplay}</div>
        </div>
        
        <h2 class="page-title">Quiz Results</h2>
        
        <div class="results-card">
          <div class="score-display">
            <div class="score-circle">
              <div class="score-percentage">${percentage.toFixed(1)}%</div>
              <div class="score-grade">Grade: ${grade}</div>
            </div>
            <div class="score-summary">
              <p><strong>${correct} out of ${totalQuestions}</strong> questions correct</p>
              <p class="lesson-info">${this.quizData.course} - Unit ${this.quizData.unit} - Lesson ${this.quizData.lesson}</p>
            </div>
          </div>

          <div class="review-section">
            <h3>Answer Review</h3>
            <div class="answers-list">
    `;

    // Show all answers
    this.quizData.questions.forEach((question, index) => {
      const userAnswer = this.userAnswers[index];
      const correctAnswer = question.answer || question.correct_answer;
      const isCorrect = userAnswer === correctAnswer;
      const questionText = question.question || question.q;
      
      html += `
        <div class="answer-item ${isCorrect ? 'correct' : 'incorrect'}">
          <div class="answer-number">Q${index + 1}</div>
          <div class="answer-details">
            <p class="answer-question">${questionText}</p>
            <p class="answer-user">Your answer: <strong>${userAnswer || '(not answered)'}</strong></p>
            ${!isCorrect ? `<p class="answer-correct">Correct: <strong>${correctAnswer}</strong></p>` : ''}
          </div>
        </div>
      `;
    });

    html += `
            </div>
          </div>

          <div class="quiz-actions">
            <button class="action-button" onclick="quizLoader.retakeQuiz()">
              Retake Quiz
            </button>
            <button class="action-button" onclick="window.history.back()">
              Back to Lesson
            </button>
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // Legacy method name for backward compatibility
  submitQuiz() {
    this.completeQuiz();
  }

  // Calculate letter grade
  getLetterGrade(percentage) {
    if (percentage >= 90) return 'A';
    if (percentage >= 80) return 'B';
    if (percentage >= 70) return 'C';
    if (percentage >= 60) return 'D';
    return 'F';
  }

  // Award tokens to user
  awardTokens(amount) {
    try {
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      user.points = (user.points || 0) + amount;
      localStorage.setItem('user', JSON.stringify(user));
    } catch (e) {
      console.error('Error awarding tokens:', e);
    }
  }

  // Retake quiz
  retakeQuiz() {
    // Reshuffle and select 7 new questions from the 20
    this.selectedQuestions = this.shuffleAndSelect(this.allQuestions, 7);
    this.quizData.questions = this.selectedQuestions;
    
    this.currentQuestionIndex = 0;
    this.userAnswers = {};
    this.submittedAnswers = {};
    this.attemptCounts = {};
    this.askedQuestionIndices = new Set();
    this.startTime = Date.now(); // Reset timer for new attempt
    this.renderQuiz();
  }

  // Initialize on page load
  async init() {
    const loaded = await this.loadQuizData();
    if (loaded) {
      this.renderQuiz();
    } else {
      const container = document.getElementById('quiz-content-view');
      if (container) {
        container.innerHTML = '<div class="diagram-card"><p>Error: Could not load quiz data. Please check the file path.</p></div>';
      }
    }
  }
}

// Create global instance
const quizLoader = new QuizLoader();

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  quizLoader.init();
});
