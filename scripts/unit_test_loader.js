// Unit Test Loader - Loads and displays unit tests from JSON files
class UnitTestLoader {
  constructor() {
    this.currentUnit = null;
    this.currentQuestionIndex = 0;
    this.userAnswers = {};
    this.submittedAnswers = {}; // Track which answers have been submitted for feedback
    this.testData = null;
    this.allQuestions = [];
    this.displayedQuestions = [];
    this.questionsPool = [];
    this.questionsToDisplay = 20;
    
    // Course name to folder mapping
    this.courseMapping = {
      'AP Biology': 'ap_biology',
      'AP Chemistry': 'ap_chemistry',
      'AP Environmental Science': 'ap_environmental_science',
      'AP Human Geography': 'ap_human_geography',
      'AP Calculus AB': 'ap_calculus_ab',
      'AP Statistics': 'ap_statistics',
      'AP Physics 2': 'ap_physics_2',
      'AP Physics C': 'ap_physics_c',
      'AP Physics C - Mechanics': 'ap_physics_c'
    };
  }

  // Shuffle array using Fisher-Yates algorithm
  shuffleArray(array) {
    const shuffled = [...array];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  }

  // Get a random question from the pool
  getRandomQuestion() {
    if (this.questionsPool.length === 0) {
      alert('No more questions available!');
      return null;
    }
    
    const randomIndex = Math.floor(Math.random() * this.questionsPool.length);
    const question = this.questionsPool[randomIndex];
    
    // Remove from pool and add to displayed
    this.questionsPool.splice(randomIndex, 1);
    this.displayedQuestions.push(question);
    
    return question;
  }

  // Parse course and unit from the current page URL
  parseLocationInfo() {
    const path = window.location.pathname;
    
    // Match pattern: /ArisEdu Project Folder/AP_Unit_Tests/{Course}/{Unit}/unit_tests.html
    const match = path.match(/AP_Unit_Tests[\/\\]([^\/\\]+)[\/\\]Unit(\d+)[\/\\]/);
    if (match) {
      const courseFolder = match[1].replace(/%20/g, ' ');
      const unitNum = parseInt(match[2]);
      return { courseFolder, unitNum };
    }
    
    return null;
  }

  // Get the slug for a course folder name
  getCourseSlug(courseFolder) {
    for (const [courseName, slug] of Object.entries(this.courseMapping)) {
      if (courseName === courseFolder || courseName.replace(/\s+/g, '%20') === courseFolder) {
        return slug;
      }
    }
    return courseFolder.toLowerCase().replace(/\s+/g, '_');
  }

  // Load the unit test JSON data
  async loadTestData() {
    const locationInfo = this.parseLocationInfo();
    if (!locationInfo) {
      console.error('Could not determine course and unit from URL');
      return false;
    }

    const { courseFolder, unitNum } = locationInfo;
    const courseSlug = this.getCourseSlug(courseFolder);
    
    // Construct the path to the JSON file
    // The JSON files are in: content_data/unit_tests/{course_slug}/unit_{n}_test.json
    // The HTML is at: ArisEdu Project Folder/AP_Unit_Tests/{course}/Unit{n}/unit_tests.html
    // So we need to go up several levels and then into content_data
    const jsonPath = `../../../../content_data/unit_tests/${courseSlug}/unit_${unitNum}_test.json`;

    try {
      const response = await fetch(jsonPath);
      if (!response.ok) {
        console.error(`Failed to load: ${jsonPath} (Status: ${response.status})`);
        return false;
      }
      this.testData = await response.json();
      this.allQuestions = [...this.testData.questions];
      this.currentUnit = unitNum;
      this.currentQuestionIndex = 0;
      this.userAnswers = {};
      this.submittedAnswers = {};
      
      // Initialize the questions pool with all questions
      this.questionsPool = this.shuffleArray(this.allQuestions);
      this.displayedQuestions = [];
      
      // Get the first 20 questions
      for (let i = 0; i < this.questionsToDisplay && this.questionsPool.length > 0; i++) {
        this.displayedQuestions.push(this.questionsPool.shift());
      }
      
      return true;
    } catch (error) {
      console.error('Error loading test data:', error);
      return false;
    }
  }

  // Render the quiz interface
  renderQuiz() {
    const container = document.getElementById('test-content-view');
    if (!container) {
      console.error('test-content-view container not found');
      return;
    }

    if (!this.testData || this.displayedQuestions.length === 0) {
      container.innerHTML = '<div class="diagram-card"><p>Could not load unit test data.</p></div>';
      return;
    }

    const displayedCount = this.displayedQuestions.length;
    const totalQuestions = this.allQuestions.length;
    const question = this.displayedQuestions[this.currentQuestionIndex];
    const wasSubmitted = this.submittedAnswers[this.currentQuestionIndex];
    const userAnswer = this.userAnswers[this.currentQuestionIndex];
    const isCorrect = userAnswer === question.answer;

    let html = `
      <div class="unit-test-container">
        <div class="test-header">
          <h2 class="page-title">${this.testData.course} - Unit ${this.testData.unit} - Unit Test</h2>
          <div class="test-progress">
            Question ${this.currentQuestionIndex + 1} of ${displayedCount} (from ${totalQuestions} total)
            <div class="progress-bar" style="width: ${((this.currentQuestionIndex + 1) / displayedCount) * 100}%"></div>
          </div>
        </div>

        <div class="diagram-card test-question">
          <div class="question-wrapper">
            <h3 class="question-text">${question.q}</h3>
            
            <div class="options-container">
    `;

    // Render options
    question.options.forEach((option, index) => {
      const optionLetters = ['A', 'B', 'C', 'D'];
      const inputId = `option_${index}`;
      const isSelected = userAnswer === option;
      const isDisabled = wasSubmitted ? 'disabled' : '';
      
      html += `
        <label class="option-label ${isSelected ? 'selected' : ''}">
          <input 
            type="radio" 
            name="answer" 
            value="${option}" 
            id="${inputId}"
            ${isSelected ? 'checked' : ''}
            ${isDisabled}
            onchange="unitTestLoader.selectAnswer('${option}')"
          />
          <span class="option-letter">${optionLetters[index]}</span>
          <span class="option-text">${option}</span>
        </label>
      `;
    });

    html += `
            </div>

            <div class="question-meta">
              <span class="difficulty-badge difficulty-${question.difficulty}">${question.difficulty}</span>
              <span class="question-id">ID: ${question.id}</span>
            </div>
            
            ${wasSubmitted ? `
              <div class="answer-feedback ${isCorrect ? 'correct-feedback' : 'incorrect-feedback'}">
                <div class="feedback-header">
                  ${isCorrect ? '✓ Correct!' : '✗ Incorrect'}
                </div>
                <div class="feedback-content">
                  <p>Your answer: <strong>${userAnswer}</strong></p>
                  ${!isCorrect ? `<p class="correct-answer">Correct answer: <strong>${question.answer}</strong></p>` : ''}
                </div>
              </div>
            ` : ''}
          </div>

          <div class="question-navigation">
            <button 
              class="nav-button prev-button" 
              onclick="unitTestLoader.previousQuestion()"
              ${this.currentQuestionIndex === 0 ? 'disabled' : ''}
            >
              ← Previous
            </button>
            
            ${wasSubmitted ? `
              <button 
                class="nav-button next-button" 
                onclick="unitTestLoader.nextQuestion()"
                ${this.currentQuestionIndex === displayedCount - 1 ? 'disabled' : ''}
              >
                Next →
              </button>
              
              ${this.questionsPool.length > 0 ? `
                <button 
                  class="nav-button get-another-button" 
                  onclick="unitTestLoader.getAnotherQuestion()"
                >
                  Get Another Question
                </button>
              ` : ''}
            ` : `
              <button 
                class="nav-button submit-button" 
                onclick="unitTestLoader.submitAnswer()"
                ${!userAnswer ? 'disabled' : ''}
              >
                Submit Answer
              </button>
            `}
          </div>

          <div class="test-summary">
            <h4>Progress Summary</h4>
            <p>Answered: ${Object.keys(this.userAnswers).length} / ${displayedCount}</p>
            <p>Submitted: ${Object.keys(this.submittedAnswers).length} / ${displayedCount}</p>
            ${this.currentQuestionIndex === displayedCount - 1 && Object.keys(this.submittedAnswers).length === displayedCount ? `
              <button class="submit-button" onclick="unitTestLoader.submitTest()">
                Submit Test & View Results
              </button>
            ` : ''}
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // Select an answer
  selectAnswer(answer) {
    this.userAnswers[this.currentQuestionIndex] = answer;
    this.renderQuiz();
  }

  // Submit an answer for the current question
  submitAnswer() {
    if (!this.userAnswers[this.currentQuestionIndex]) {
      alert('Please select an answer first');
      return;
    }
    
    this.submittedAnswers[this.currentQuestionIndex] = true;
    this.renderQuiz();
  }

  // Navigate to next question
  nextQuestion() {
    if (this.currentQuestionIndex < this.displayedQuestions.length - 1) {
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

  // Get another question from the pool
  getAnotherQuestion() {
    if (this.questionsPool.length === 0) {
      alert('No more questions available!');
      return;
    }
    
    const newQuestion = this.getRandomQuestion();
    if (newQuestion) {
      this.currentQuestionIndex = this.displayedQuestions.length - 1;
      this.renderQuiz();
    }
  }

  // Submit the test and show results
  async submitTest() {
    const container = document.getElementById('test-content-view');
    const displayedCount = this.displayedQuestions.length;
    let correct = 0;

    // Calculate score based on displayed questions (only counting submitted answers)
    this.displayedQuestions.forEach((question, index) => {
      const userAnswer = this.userAnswers[index];
      if (userAnswer && userAnswer === question.answer) {
        correct++;
      }
    });

    const percentage = (correct / displayedCount) * 100;
    const grade = this.getLetterGrade(percentage);

    // Mark unit test as complete and sync to Firebase if available
    if (this.currentUnit) {
      const coursePrefix = await this.getCoursePrefix();
      localStorage.setItem(`${coursePrefix}_u${this.currentUnit}_l99_completed`, 'true');
      if (window.courseProgress) {
        await window.courseProgress.markComplete(coursePrefix, this.currentUnit, 99);
      }
    }

    let html = `
      <div class="test-results">
        <h2 class="page-title">Test Results</h2>
        
        <div class="results-card">
          <div class="score-display">
            <div class="score-circle">
              <div class="score-percentage">${percentage.toFixed(1)}%</div>
              <div class="score-grade">Grade: ${grade}</div>
            </div>
            <div class="score-summary">
              <p><strong>${correct} out of ${displayedCount}</strong> questions correct</p>
            </div>
          </div>

          <div class="review-section">
            <h3>Answer Review</h3>
            <div class="answers-list">
    `;

    // Show all answers for displayed questions
    this.displayedQuestions.forEach((question, index) => {
      const userAnswer = this.userAnswers[index];
      const isCorrect = userAnswer === question.answer;
      
      html += `
        <div class="answer-item ${isCorrect ? 'correct' : 'incorrect'}">
          <div class="answer-number">Q${index + 1}</div>
          <div class="answer-details">
            <p class="answer-question">${question.q}</p>
            <p class="answer-user">Your answer: <strong>${userAnswer || '(not answered)'}</strong></p>
            ${!isCorrect ? `<p class="answer-correct">Correct: <strong>${question.answer}</strong></p>` : ''}
          </div>
        </div>
      `;
    });

    html += `
            </div>
          </div>

          <div class="test-actions">
            <button class="action-button" onclick="unitTestLoader.retakeTest()">
              Retake Test
            </button>
            <button class="action-button" onclick="window.history.back()">
              Back to Course
            </button>
          </div>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // Get the course prefix from the current course/unit combination
  async getCoursePrefix() {
    // Try to determine course prefix from the course name or URL
    if (this.courseFolder) {
      const courseMap = {
        'AP Biology': 'ap_bio',
        'AP Chemistry': 'ap_chem',
        'AP Environmental Science': 'ap_env_sci',
        'AP Human Geography': 'ap_hug',
        'AP Calculus AB': 'ap_calc_ab',
        'AP Statistics': 'ap_stats',
        'AP Physics 2': 'ap_phys2',
        'AP Physics C - Mechanics': 'ap_phys_mech'
      };
      return courseMap[this.courseFolder] || 'ap_bio';
    }
    return 'ap_bio';
  }

  // Calculate letter grade
  getLetterGrade(percentage) {
    if (percentage >= 90) return 'A';
    if (percentage >= 80) return 'B';
    if (percentage >= 70) return 'C';
    if (percentage >= 60) return 'D';
    return 'F';
  }

  // Retake test
  retakeTest() {
    this.currentQuestionIndex = 0;
    this.userAnswers = {};
    this.submittedAnswers = {};
    
    // Shuffle all questions again
    this.questionsPool = this.shuffleArray(this.allQuestions);
    this.displayedQuestions = [];
    
    // Get the first 20 questions
    for (let i = 0; i < this.questionsToDisplay && this.questionsPool.length > 0; i++) {
      this.displayedQuestions.push(this.questionsPool.shift());
    }
    
    this.renderQuiz();
  }

  // Initialize on page load
  async init() {
    const loaded = await this.loadTestData();
    if (loaded) {
      this.renderQuiz();
    } else {
      const container = document.getElementById('test-content-view');
      if (container) {
        container.innerHTML = '<div class="diagram-card"><p>Error: Could not load unit test data. Please check the file path.</p></div>';
      }
    }
  }
}

// Create global instance
const unitTestLoader = new UnitTestLoader();

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
  unitTestLoader.init();
});
