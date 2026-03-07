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
      'Physics': 'physics',
      'Precalculus': 'precalculus',
      'Trigonometry': 'trigonometry',
      'Statistics & Probability': 'statistics',
      'Linear Algebra': 'linear_algebra',
      'Financial Math': 'financial_math',
      'Earth Science': 'earth_science',
      'Environmental Science': 'environmental_science',
      'Astronomy': 'astronomy',
      'Human Anatomy & Physiology': 'anatomy',
      'Marine Science': 'marine_science'
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
        'Precalculus': 'Precalculus',
        'Trigonometry': 'Trigonometry',
        'Statistics': 'Statistics & Probability',
        'LinearAlgebra': 'Linear Algebra',
        'FinancialMath': 'Financial Math',
        'EarthScience': 'Earth Science',
        'EnvironmentalScience': 'Environmental Science',
        'Astronomy': 'Astronomy',
        'Anatomy': 'Human Anatomy & Physiology',
        'MarineScience': 'Marine Science',
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
              const isLastQuestion = this.currentQuestionIndex === totalQuestions - 1;

              // Check if all questions have been attempted (submitted at least once)
              const allQuestionsAttempted = Object.keys(this.submittedAnswers).length >= totalQuestions;

              // If out of attempts and got it wrong, show "Get another question" button
              // But if all questions have been attempted OR this is the last question, also show View Results
              if (attempts >= 2 && wasSubmitted && !isCorrect) {
                if (allQuestionsAttempted || isLastQuestion) {
                  return `
                    <button 
                      class="nav-button another-button" 
                      onclick="quizLoader.getAnotherQuestion()"
                    >
                      Get Another Question
                    </button>
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
                // If all questions answered or on last question, show View Results
                const lastQuestionAnswered = this.submittedAnswers[this.currentQuestionIndex];
                
                if (allQuestionsAttempted || (isLastQuestion && lastQuestionAnswered)) {
                  // Show "View Results" button
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

    // Mark lesson as completed
    this.markLessonComplete();

    // Show arcade intro tour on first-ever lesson completion
    const isFirstCompletion = !localStorage.getItem('arisEdu_arcadeTourShown');
    if (isFirstCompletion) {
      setTimeout(() => this.showArcadeTour(), 1200);
    }

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

  // Determine relevant key for completion
  markLessonComplete() {
    try {
      if (!this.quizData) return;
      
      const { unit, lesson, course } = this.quizData; // course is loose name
      
      let prefix = '';
      const path = window.location.pathname;
      
      // Course-specific prefix logic
      if (path.includes('APLessons')) {
        if (path.includes('Biology')) prefix = 'ap_bio';
        else if (path.includes('Chemistry')) prefix = 'ap_chem'; 
        else if (path.includes('Environmental')) prefix = 'ap_env_sci';
        else if (path.includes('Human')) prefix = 'ap_hug';
        else if (path.includes('Calculus')) prefix = 'ap_calc_ab';
        else if (path.includes('Statistics')) prefix = 'ap_stats';
        else if (path.includes('hysics_2')) prefix = 'ap_phys2';
        else if (path.includes('echanics')) prefix = 'ap_phys_mech';
        else if (path.includes('hysics_1')) prefix = 'ap_phys1';
      } else if (path.includes('MS_')) {
        // Middle School Logic
        if (path.includes('Algebra1') || path.includes('Pre-Algebra')) prefix = 'alg1_ms';
        else if (path.includes('Algebra2')) prefix = 'alg2_ms';
        else if (path.includes('Biology') || path.includes('Life')) prefix = 'bio_ms';
        else if (path.includes('Chemistry')) {
           // Special case: check if ms_chem.html uses chem_u or chem_ms_u
           // Based on inspection, ms_chem.html currently uses chem_u (shared with HS)
           // But intended might be chem_ms. 
           // For safety, we will write BOTH to ensure it works regardless of the bug in ms_chem.html
           prefix = 'chem_ms'; 
        }
        else if (path.includes('Geometry')) prefix = 'ms_geom';
        else if (path.includes('Physics')) prefix = 'ms_phys';
      } else {
        // High School Logic
        if (path.includes('Algebra1')) prefix = 'alg1';
        else if (path.includes('Algebra2')) prefix = 'alg2';
        else if (path.includes('Biology')) prefix = 'bio';
        else if (path.includes('Chemistry')) prefix = 'chem';
        else if (path.includes('Geometry')) prefix = 'geometry';
        else if (path.includes('Physics')) prefix = 'physics';
      }

      if (prefix) {
        // Parse lesson number (e.g. "1.2" -> "2")
        // NOTE: Some files might be "Lesson 5.html" -> "5"
        let lessonNum = lesson;
        if (lesson.toString().includes('.')) {
            lessonNum = lesson.toString().split('.')[1];
        }
        
        // Write primary key
        const key = `${prefix}_u${unit}_l${lessonNum}_completed`;
        localStorage.setItem(key, 'true');
        
        // Also write started key
        localStorage.setItem(`${prefix}_u${unit}_l${lessonNum}_started`, 'true');
        
        // Hack for MS Chemistry: write to HS prefix too if it's MS Chemistry
        if (prefix === 'chem_ms') {
            localStorage.setItem(`chem_u${unit}_l${lessonNum}_completed`, 'true');
            localStorage.setItem(`chem_u${unit}_l${lessonNum}_started`, 'true');
        }

        console.log(`Marked lesson complete: ${key}`);
        
        // Notify any listeners
        if (window.checkQuizCompletion) window.checkQuizCompletion();
      }
    } catch (e) {
      console.error('Error marking completion:', e);
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

  // Arcade intro tour — shown once on first-ever quiz completion
  showArcadeTour() {
    localStorage.setItem('arisEdu_arcadeTourShown', 'true');

    // Inject CSS
    const style = document.createElement('style');
    style.textContent = `
      .arcade-tour-overlay {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        z-index: 99999; pointer-events: none; opacity: 0;
        transition: opacity 0.4s ease;
      }
      .arcade-tour-overlay.active { opacity: 1; pointer-events: auto; }
      .arcade-tour-backdrop {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0,0,0,0.65); z-index: 99998;
      }
      .arcade-tour-card {
        position: fixed; background: white; border-radius: 1rem; padding: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3); z-index: 100000;
        max-width: 440px; width: 90%;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%) scale(0.9);
        opacity: 0;
        transition: transform 0.4s cubic-bezier(0.34,1.56,0.64,1), opacity 0.3s ease;
      }
      .arcade-tour-card.visible {
        transform: translate(-50%, -50%) scale(1); opacity: 1;
      }
      body.dark-mode .arcade-tour-card {
        background: #1e293b; box-shadow: 0 20px 60px rgba(0,0,0,0.5);
      }
      .arcade-tour-card .at-icon { font-size: 3rem; margin-bottom: 0.75rem; text-align: center; }
      .arcade-tour-card h2 {
        font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;
        color: #1e293b; text-align: center;
      }
      body.dark-mode .arcade-tour-card h2 { color: #f1f5f9; }
      .arcade-tour-card p {
        font-size: 1rem; line-height: 1.6; color: #475569;
        text-align: center; margin-bottom: 0.25rem;
      }
      body.dark-mode .arcade-tour-card p { color: #94a3b8; }
      .arcade-tour-card .at-flow {
        display: flex; align-items: center; justify-content: center;
        gap: 0.5rem; margin: 1rem 0; flex-wrap: wrap;
      }
      .arcade-tour-card .at-flow-step {
        display: flex; flex-direction: column; align-items: center; gap: 0.25rem;
        padding: 0.5rem 0.75rem; border-radius: 0.5rem;
        background: #f1f5f9; font-size: 0.85rem; font-weight: 600; color: #334155;
      }
      body.dark-mode .arcade-tour-card .at-flow-step { background: #334155; color: #e2e8f0; }
      .arcade-tour-card .at-flow-step .fi { font-size: 1.4rem; }
      .arcade-tour-card .at-flow-arrow { font-size: 1.2rem; color: #94a3b8; }
      .arcade-tour-nav {
        display: flex; align-items: center; justify-content: space-between;
        margin-top: 1.5rem; gap: 0.75rem;
      }
      .arcade-tour-dots { display: flex; gap: 6px; }
      .arcade-tour-dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #cbd5e1; transition: all 0.3s ease;
      }
      .arcade-tour-dot.active { background: #f59e0b; width: 24px; border-radius: 4px; }
      body.dark-mode .arcade-tour-dot { background: #475569; }
      body.dark-mode .arcade-tour-dot.active { background: #f59e0b; }
      .at-btn {
        padding: 0.5rem 1.25rem; border-radius: 0.5rem; font-weight: 600;
        font-size: 0.9rem; cursor: pointer; border: none; transition: all 0.2s ease;
      }
      .at-btn-primary {
        background: linear-gradient(135deg, #f59e0b, #d97706); color: white;
      }
      .at-btn-primary:hover { opacity: 0.9; transform: translateY(-1px); }
      .at-btn-secondary { background: #f1f5f9; color: #475569; }
      body.dark-mode .at-btn-secondary { background: #334155; color: #cbd5e1; }
      .at-btn-secondary:hover { background: #e2e8f0; }
      body.dark-mode .at-btn-secondary:hover { background: #475569; }
      .at-btn-skip {
        background: none; color: #94a3b8; font-size: 0.85rem; padding: 0.5rem 0.75rem;
      }
      .at-btn-skip:hover { color: #64748b; }
      .at-btn-arcade {
        display: inline-block; margin-top: 0.75rem;
        background: linear-gradient(135deg, #f59e0b, #d97706); color: white;
        padding: 0.6rem 1.5rem; border-radius: 0.5rem; font-weight: 700;
        font-size: 1rem; text-decoration: none; border: none; cursor: pointer;
        transition: all 0.2s ease;
      }
      .at-btn-arcade:hover { opacity: 0.9; transform: translateY(-1px); }
    `;
    document.head.appendChild(style);

    // Tour steps
    const steps = [
      {
        icon: '🎉',
        title: 'You Earned Arcade Tokens!',
        body: 'Every time you complete a lesson quiz, you earn <b>💎 300 Arcade Tokens</b>. These tokens unlock fun games!',
        btnText: 'Tell Me More'
      },
      {
        icon: '🎮',
        title: 'Welcome to the Arcade',
        body: 'The Arcade is packed with games you can play using your tokens. Spend tokens to start a gaming session and have fun between study breaks!',
        flow: [
          { icon: '✅', label: 'Complete Quiz' },
          { icon: '💎', label: 'Earn Tokens' },
          { icon: '🎮', label: 'Play Games' }
        ]
      },
      {
        icon: '🏆',
        title: 'How It Works',
        body: 'Each game session costs tokens. The more lessons you complete, the more you can play! Balance learning and fun.'
      },
      {
        icon: '🚀',
        title: 'Ready to Play?',
        body: 'Head to the <b>Arcade</b> from the main menu to browse games and start playing. Keep completing lessons to stock up on tokens!',
        btnText: 'Got It!',
        showArcadeLink: true
      }
    ];

    let currentStep = 0;

    // Build overlay
    const overlay = document.createElement('div');
    overlay.className = 'arcade-tour-overlay';
    overlay.innerHTML = `
      <div class="arcade-tour-backdrop"></div>
      <div class="arcade-tour-card" id="arcade-tour-card"></div>
    `;
    document.body.appendChild(overlay);

    const card = overlay.querySelector('#arcade-tour-card');

    function buildCard(step, index) {
      let html = '';
      if (step.icon) html += `<div class="at-icon">${step.icon}</div>`;
      html += `<h2>${step.title}</h2>`;
      html += `<p>${step.body}</p>`;

      if (step.flow) {
        html += '<div class="at-flow">';
        step.flow.forEach((f, i) => {
          html += `<div class="at-flow-step"><span class="fi">${f.icon}</span>${f.label}</div>`;
          if (i < step.flow.length - 1) html += '<span class="at-flow-arrow">→</span>';
        });
        html += '</div>';
      }

      if (step.showArcadeLink) {
        // Build arcade link relative to current page
        const path = window.location.pathname;
        let arcadeHref = '/ArisEdu%20Project%20Folder/arcade.html';
        // If we can detect the project folder base, adjust
        const folderMatch = path.match(/(.*ArisEdu(?:%20|\s)Project(?:%20|\s)Folder)/i);
        if (folderMatch) {
          arcadeHref = folderMatch[1].replace(/ /g, '%20') + '/arcade.html';
        }
        html += `<div style="text-align:center;"><a class="at-btn-arcade" href="${arcadeHref}">🎮 Visit Arcade</a></div>`;
      }

      // Navigation
      html += '<div class="arcade-tour-nav">';
      if (index > 0) {
        html += `<button class="at-btn at-btn-secondary" onclick="window._arcadeTourPrev()">← Back</button>`;
      } else {
        html += `<button class="at-btn at-btn-skip" onclick="window._arcadeTourFinish()">Skip</button>`;
      }
      html += '<div class="arcade-tour-dots">';
      for (let i = 0; i < steps.length; i++) {
        html += `<div class="arcade-tour-dot${i === index ? ' active' : ''}"></div>`;
      }
      html += '</div>';
      const isLast = index === steps.length - 1;
      const nextLabel = step.btnText || (isLast ? 'Finish' : 'Next →');
      html += `<button class="at-btn at-btn-primary" onclick="${isLast ? 'window._arcadeTourFinish()' : 'window._arcadeTourNext()'}">${nextLabel}</button>`;
      html += '</div>';
      return html;
    }

    function showStep(index) {
      currentStep = index;
      card.classList.remove('visible');
      setTimeout(() => {
        card.innerHTML = buildCard(steps[index], index);
        requestAnimationFrame(() => card.classList.add('visible'));
      }, 200);
    }

    window._arcadeTourNext = () => {
      if (currentStep < steps.length - 1) showStep(currentStep + 1);
    };
    window._arcadeTourPrev = () => {
      if (currentStep > 0) showStep(currentStep - 1);
    };
    window._arcadeTourFinish = () => {
      card.classList.remove('visible');
      overlay.classList.remove('active');
      setTimeout(() => overlay.remove(), 400);
    };

    // Activate
    requestAnimationFrame(() => {
      overlay.classList.add('active');
      showStep(0);
    });
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
