#!/usr/bin/env python3
"""Generate real content for Statistics Unit 8: Regression & Correlation (7 lessons)."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "statistics_lessons.json")
COURSE = "Statistics & Probability"

def build_lesson(unit, idx, title, summary_html, flashcards, quiz):
    key = f"u{unit}_l{unit}.{idx}"
    fc = [{"term": t, "definition": d} for t, d in flashcards]
    qs = []
    for qi, (qt, opts, exp) in enumerate(quiz, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        qs.append({"question_number": qi, "question_text": qt, "attempted": 2, "data_i18n": None, "options": options, "explanation": exp})
    return key, {
        "unit": unit, "lesson_number": f"{unit}.{idx}", "title": title, "course": COURSE,
        "summary_sections": [{"title": f"Key Concepts: {title}", "content_html": summary_html, "data_i18n": None}],
        "flashcards": fc, "quiz_questions": qs
    }

lessons = {}

# ── 8.1 Scatterplots & Correlation Coefficient ──
k, v = build_lesson(8, 1, "Scatterplots & Correlation Coefficient",
    "<h3>Scatterplots & Correlation Coefficient</h3>"
    "<p>A <b>scatterplot</b> displays the relationship between two quantitative variables, with each point representing an observation.</p>"
    "<ul><li><b>Direction:</b> Positive (up-right), negative (down-right), or no trend.</li>"
    "<li><b>Form:</b> Linear, curved, or no clear pattern.</li>"
    "<li><b>Strength:</b> How tightly the points follow the pattern (strong, moderate, weak).</li>"
    "<li><b>Correlation coefficient (r):</b> Measures the strength and direction of a <b>linear</b> relationship between two variables.</li>"
    "<li><b>Properties of r:</b> −1 ≤ r ≤ 1. r = 1 means perfect positive linear; r = −1 means perfect negative linear; r = 0 means no linear relationship.</li>"
    "<li><b>r only measures linear relationships</b> — a strong curved pattern can have r ≈ 0.</li>"
    "<li><b>r is unitless</b> and not affected by changes in units or which variable is x vs. y.</li>"
    "<li><b>Outliers</b> can strongly influence r.</li></ul>",
    [
        ("Scatterplot", "A graph displaying the relationship between two quantitative variables using points in the coordinate plane."),
        ("Correlation Coefficient (r)", "A value between −1 and 1 measuring the strength and direction of a linear relationship between two variables."),
        ("Positive Correlation", "As one variable increases, the other tends to increase; points trend upward to the right."),
        ("Negative Correlation", "As one variable increases, the other tends to decrease; points trend downward to the right."),
        ("r = 0", "Indicates no linear relationship, but there may still be a nonlinear association."),
    ],
    [
        ("A scatterplot displays the relationship between:", ["One variable and time", "*Two quantitative variables", "Two categorical variables", "Frequency and value"],
         "Each point represents paired measurements of two quantitative variables."),
        ("r = 0.95 indicates:", ["Weak correlation", "No correlation", "*Strong positive linear correlation", "Strong negative correlation"],
         "r close to 1 means a strong positive linear relationship."),
        ("r = −0.85 indicates:", ["*Strong negative linear correlation", "Weak positive correlation", "No correlation", "Perfect positive correlation"],
         "Negative r near −1 means a strong negative linear relationship."),
        ("r ranges from:", ["0 to 1", "*−1 to 1", "−∞ to ∞", "0 to 100"],
         "The correlation coefficient is bounded between −1 and 1."),
        ("r = 1 means:", ["No correlation", "Strong negative correlation", "*Perfect positive linear relationship", "The variables are independent"],
         "Every point falls exactly on a line with positive slope."),
        ("r only measures __ relationships:", ["Curved", "*Linear", "Exponential", "All types of"],
         "r captures only the linear component; nonlinear patterns require other measures."),
        ("A strong curved pattern can have r ≈ 0 because:", ["r doesn't exist", "The data is wrong", "*r only detects linear relationships", "Curves always have r = 0"],
         "r misses nonlinear structure."),
        ("r is:", ["Expressed in units", "Affected by switching x and y", "*Unitless and unaffected by switching x and y", "Always positive"],
         "r has no units and is symmetric in x and y."),
        ("An outlier can:", ["*Strongly influence r", "Never affect r", "Only increase r", "Only decrease r"],
         "Outliers can pull r toward 0 or inflate it, depending on their position."),
        ("Positive direction in a scatterplot means:", ["Points go down-right", "*Points generally go up-right", "Points form a circle", "There is no pattern"],
         "Both variables increase together."),
        ("If r = 0, that means:", ["The variables are unrelated", "*There is no LINEAR relationship (but there could be a nonlinear one)", "The data is bad", "r was calculated wrong"],
         "r = 0 means no linear trend; other patterns may exist."),
        ("The strength of a correlation is determined by:", ["The sign of r", "*The absolute value of r (closer to 1 = stronger)", "The number of data points", "The units of measurement"],
         "|r| closer to 1 indicates a stronger linear relationship."),
        ("r² = 0.81 means:", ["r = 0.81", "*81% of the variation in y is explained by the linear relationship with x", "There is no correlation", "The regression is invalid"],
         "r² (coefficient of determination) gives the proportion of variation explained."),
        ("Changing the units (e.g., cm to meters) affects r:", ["Yes, it changes r", "*No, r is unitless", "Only if both variables change", "Only for negative correlations"],
         "r is standardized and unaffected by linear unit changes."),
        ("A scatterplot shows no pattern. r is likely:", ["1", "−1", "*Close to 0", "0.5"],
         "No visible pattern = no linear relationship = r ≈ 0."),
        ("Correlation does not imply:", ["Association", "A pattern", "*Causation", "A relationship"],
         "Correlation shows association, not cause and effect."),
        ("To compute r, both variables must be:", ["Categorical", "One categorical, one quantitative", "*Both quantitative", "Both binary"],
         "r is defined for two quantitative variables."),
        ("A scatterplot's form can be:", ["*Linear, curved, or no clear pattern", "Only linear", "Only positive", "Only strong"],
         "The form describes the overall shape of the point cloud."),
        ("If every data point is exactly on a line with negative slope, r = ?", ["0", "1", "*−1", "−0.5"],
         "Perfect negative linear relationship means r = −1."),
        ("The explanatory variable is typically on the:", ["*x-axis", "y-axis", "Neither axis", "Both axes"],
         "Convention places the explanatory (independent) variable on x."),
    ]
)
lessons[k] = v

# ── 8.2 Least Squares Regression Line ──
k, v = build_lesson(8, 2, "Least Squares Regression Line",
    "<h3>Least Squares Regression Line (LSRL)</h3>"
    "<p>The <b>least squares regression line</b> (LSRL) is the line that minimizes the sum of the squared vertical distances (residuals) between the data points and the line.</p>"
    "<p><b>Equation:</b> ŷ = a + bx, where:</p>"
    "<ul><li>b = r(s<sub>y</sub>/s<sub>x</sub>) — the slope.</li>"
    "<li>a = ȳ − bx̄ — the y-intercept.</li>"
    "<li>The line always passes through the point (x̄, ȳ).</li></ul>"
    "<p><b>Interpreting slope (b):</b> For each one-unit increase in x, ŷ changes by b units on average.</p>"
    "<p><b>Interpreting intercept (a):</b> The predicted y-value when x = 0 (may not be meaningful in context).</p>"
    "<p><b>r² (coefficient of determination):</b> The proportion of variation in y explained by the linear model. r² = 0.75 means 75% of the variability in y is explained by x.</p>"
    "<p><b>Extrapolation:</b> Predicting y for x values far outside the data range — unreliable and should be avoided.</p>",
    [
        ("Least Squares Regression Line", "The line ŷ = a + bx that minimizes the sum of squared residuals."),
        ("Slope (b)", "The change in predicted y (ŷ) for each one-unit increase in x; b = r(sᵧ/sₓ)."),
        ("Y-Intercept (a)", "The predicted value of y when x = 0; a = ȳ − bx̄."),
        ("r² (Coefficient of Determination)", "The proportion of variability in y that is explained by the linear relationship with x."),
        ("Extrapolation", "Using the regression line to predict y for x values far outside the range of the data; unreliable."),
    ],
    [
        ("The LSRL minimizes:", ["The sum of residuals", "*The sum of squared residuals", "The correlation", "The intercept"],
         "Least squares means minimizing Σ(residual)² = Σ(y − ŷ)²."),
        ("The slope b represents:", ["The y-intercept", "*The average change in ŷ for each one-unit increase in x", "The correlation", "The sum of squares"],
         "Slope = the rate of change in the predicted response per unit change in x."),
        ("The LSRL always passes through:", ["(0, 0)", "*The point (x̄, ȳ)", "(1, 1)", "The origin"],
         "The line passes through the means of x and y."),
        ("r² = 0.64 means:", ["r = 0.64", "*64% of the variability in y is explained by the regression", "The model is 64% accurate", "There are 64 data points"],
         "r² gives the proportion of variation explained."),
        ("b = r · (sᵧ/sₓ) — if r is positive:", ["b is negative", "*b is positive", "b is zero", "b is undefined"],
         "The sign of b matches the sign of r."),
        ("The y-intercept (a) is the predicted y when:", ["*x = 0", "y = 0", "x = x̄", "x = 1"],
         "The intercept is where the line crosses the y-axis (x = 0)."),
        ("Extrapolation is:", ["Always reliable", "*Predicting y outside the range of observed x values — unreliable", "The same as interpolation", "Required for regression"],
         "The pattern may not hold outside the observed data range."),
        ("If b = 2.5, increasing x by 1 predicts ŷ increases by:", ["1", "0.5", "*2.5", "5"],
         "The slope gives the predicted change in y per unit increase in x."),
        ("The regression line predicts:", ["Exact outcomes", "*Average values of y for given x values", "Only the residuals", "The standard deviation"],
         "ŷ is the predicted average y for a given x."),
        ("ŷ = 10 + 3x. When x = 5:", ["ŷ = 10", "ŷ = 15", "*ŷ = 25", "ŷ = 50"],
         "ŷ = 10 + 3(5) = 25."),
        ("The residual for a point is:", ["ŷ − x", "*y − ŷ (observed minus predicted)", "x − ŷ", "ŷ − ȳ"],
         "Residual = actual value − predicted value."),
        ("A positive residual means the point is:", ["On the line", "*Above the regression line", "Below the regression line", "At the origin"],
         "Positive residual: y > ŷ, so the point is above the line."),
        ("The sum of all residuals for the LSRL = ?", ["A positive number", "A negative number", "*0", "1"],
         "The LSRL is defined such that residuals sum to 0."),
        ("If r = 0.8, r² = ?", ["0.8", "0.80", "*0.64", "0.4"],
         "r² = 0.8² = 0.64."),
        ("A high r² (close to 1) means:", ["*The model explains most of the variation in y", "The prediction is exact", "Causation is established", "The intercept is 1"],
         "High r² means x explains most of y's variability."),
        ("To interpret slope in context: 'For each additional [x unit], we predict [y] changes by __ on average.'", ["The intercept", "r²", "*The slope b", "The residual"],
         "The slope is always interpreted as average change in y per unit change in x."),
        ("If the intercept has no real-world meaning (e.g., x = 0 is impossible):", ["The model is invalid", "Don't use the model", "*Acknowledge this in interpretation but the model is still useful for predictions within the data range", "Set a = 0"],
         "The intercept may be meaningless in context but doesn't invalidate the model."),
        ("Switching x and y in regression:", ["Gives the same line", "*Gives a different regression line", "Doesn't affect the slope", "Doesn't affect r"],
         "The regression of y on x differs from the regression of x on y (except r is the same)."),
        ("The LSRL is appropriate when the scatterplot shows:", ["A strong curved pattern", "*A roughly linear relationship", "No pattern", "Clusters"],
         "Linear regression requires an approximately linear relationship."),
        ("r² = 0 means:", ["Perfect fit", "*The linear model explains none of the variation in y", "r = 1", "The model should be kept"],
         "r² = 0 means x provides no linear prediction of y."),
    ]
)
lessons[k] = v

# ── 8.3 Residuals & Line Fit ──
k, v = build_lesson(8, 3, "Residuals & Line Fit",
    "<h3>Residuals & Line Fit</h3>"
    "<p>A <b>residual</b> is the difference between an observed y-value and the predicted ŷ-value: residual = y − ŷ.</p>"
    "<ul><li><b>Residual plot:</b> A scatterplot of residuals vs. x (or vs. ŷ). Used to assess whether the linear model is appropriate.</li>"
    "<li><b>Good fit:</b> Residuals are randomly scattered around 0 with no clear pattern.</li>"
    "<li><b>Problems:</b> A curved pattern in the residual plot suggests a nonlinear relationship; a fan shape suggests non-constant variance (heteroscedasticity).</li>"
    "<li><b>Standard deviation of residuals (s):</b> Measures the typical size of prediction errors: s = √[Σ(y − ŷ)²/(n − 2)].</li>"
    "<li><b>Influential points:</b> Points with extreme x-values (high leverage) that can dramatically change the regression line.</li>"
    "<li><b>Outliers in regression:</b> Points with large residuals that don't fit the pattern.</li></ul>",
    [
        ("Residual", "The difference between the observed and predicted values: residual = y − ŷ."),
        ("Residual Plot", "A scatterplot of residuals vs. x-values used to check whether the linear model is appropriate."),
        ("Good Residual Pattern", "Random scatter around 0 with no systematic pattern — indicates the linear model fits well."),
        ("Influential Point", "A point (often with extreme x) that has a large effect on the regression line."),
        ("Heteroscedasticity", "Non-constant variance in residuals — seen as a fan or trumpet shape in the residual plot."),
    ],
    [
        ("A residual is:", ["ŷ − ȳ", "*y − ŷ (observed minus predicted)", "x − x̄", "ŷ + y"],
         "Residual = actual observation − predicted value."),
        ("A good residual plot shows:", ["A clear curve", "A fan shape", "*Random scatter around 0", "All points on the zero line"],
         "No pattern means the linear model fits the data well."),
        ("A curved pattern in a residual plot suggests:", ["The model is perfect", "*A nonlinear relationship that the linear model misses", "The data is random", "A good fit"],
         "A curve means a linear model is not appropriate."),
        ("A fan shape in residuals indicates:", ["Perfect predictions", "*Non-constant variance (heteroscedasticity)", "A linear relationship", "Zero residuals"],
         "Increasing spread suggests the model's accuracy varies with x."),
        ("The sum of residuals from the LSRL = ?", ["1", "−1", "*0", "Depends on the data"],
         "By construction, the LSRL has residuals that sum to zero."),
        ("The standard deviation of residuals (s) measures:", ["The slope", "r²", "*The typical size of prediction errors", "The mean residual"],
         "s tells us how far predictions typically are from actual values."),
        ("An influential point:", ["*Can dramatically change the regression line", "Has a small residual", "Is always at the center", "Never affects the slope"],
         "Points with extreme x-values can pull the line substantially."),
        ("High leverage means a point has:", ["A large residual", "A small residual", "*An extreme x-value", "An extreme y-value only"],
         "Leverage refers to how far the x-value is from x̄."),
        ("An outlier in regression has:", ["An x-value at x̄", "*A large residual (far from the line)", "No effect", "r = 0"],
         "Outliers are points that deviate substantially from the predicted pattern."),
        ("Residual = y − ŷ. If residual = 5:", ["The prediction was 5 too high", "*The prediction was 5 too low (actual > predicted)", "The prediction was exact", "ŷ = 5"],
         "Positive residual: the actual value exceeded the prediction by 5."),
        ("If all residuals are 0:", ["The model is bad", "The data is random", "*Every point lies exactly on the regression line (perfect fit)", "r = 0"],
         "Zero residuals mean perfect prediction — r² = 1."),
        ("Residual plots should be checked:", ["Never", "Only for large datasets", "*Always, to verify the linear model is appropriate", "Only when r is high"],
         "Even with high r, the residual plot may reveal problems."),
        ("Removing an influential point:", ["Never changes the line", "*Can substantially change the slope and intercept", "Always improves the model", "Violates ethics"],
         "Influential points have a large effect on the regression — their removal should be justified."),
        ("s = √[Σ(y−ŷ)²/(n−2)] uses n − 2 because:", ["There are n−2 data points", "*Two parameters (slope and intercept) are estimated, using 2 degrees of freedom", "It's a convention", "n − 2 reduces bias"],
         "Estimating a and b uses 2 df, leaving n − 2 for the residual standard deviation."),
        ("A point with high leverage and a large residual is:", ["*Both influential and an outlier — strongest impact on the line", "Not a concern", "Only an outlier", "Only influential"],
         "Such a point dramatically affects the regression."),
        ("The residual plot should be drawn against:", ["y only", "*x (or ŷ)", "The sample size", "The intercept"],
         "Plotting residuals vs. x (or fitted values) reveals patterns."),
        ("If residuals show random scatter but wider spread for larger x:", ["The model is perfect", "*Heteroscedasticity is present", "The data is wrong", "r = 1"],
         "Increasing spread = non-constant variance."),
        ("When the linear model is appropriate, the residual plot looks:", ["*Like a random cloud of points centered at 0", "Like a parabola", "Like a line", "Like a funnel"],
         "Random scatter around zero = good fit."),
        ("Not checking residuals can lead to:", ["Better predictions", "*Using a model that doesn't fit the data", "Higher r²", "More accurate slopes"],
         "Skipping residual analysis risks missing model inadequacies."),
        ("Transformations (like log or √) can help when:", ["The linear model fits perfectly", "*The residual plot shows curvature or non-constant variance", "r = 1", "There are no outliers"],
         "Transformations can straighten curved relationships or stabilize variance."),
    ]
)
lessons[k] = v

# ── 8.4 Multiple Regression (introductory) ──
k, v = build_lesson(8, 4, "Multiple Regression (introductory)",
    "<h3>Multiple Regression (Introduction)</h3>"
    "<p><b>Multiple regression</b> extends simple linear regression to include two or more explanatory variables.</p>"
    "<p><b>Model:</b> ŷ = b₀ + b₁x₁ + b₂x₂ + … + bₖxₖ</p>"
    "<ul><li><b>b₀:</b> The intercept (predicted y when all x's = 0).</li>"
    "<li><b>bᵢ:</b> The predicted change in y for a one-unit increase in xᵢ, <b>holding all other variables constant</b>.</li>"
    "<li><b>R² (multiple):</b> The proportion of variation in y explained by ALL the predictors combined. R² always increases when more predictors are added.</li>"
    "<li><b>Adjusted R²:</b> Penalizes for the number of predictors; only increases if a new variable genuinely improves the model.</li>"
    "<li><b>Multicollinearity:</b> When predictor variables are highly correlated with each other, making individual coefficients unreliable.</li></ul>"
    "<p>Multiple regression is widely used in science, business, economics, and social sciences to model complex relationships.</p>",
    [
        ("Multiple Regression", "A regression model with two or more explanatory variables: ŷ = b₀ + b₁x₁ + b₂x₂ + … + bₖxₖ."),
        ("Holding Other Variables Constant", "Each coefficient bᵢ represents the effect of xᵢ while other predictors are held fixed."),
        ("Adjusted R²", "A modified R² that penalizes for additional predictors; prevents overfitting."),
        ("Multicollinearity", "When predictor variables are highly correlated with each other, making individual coefficients unreliable."),
        ("Overfitting", "Including too many predictors that capture noise rather than true patterns, reducing prediction quality on new data."),
    ],
    [
        ("Multiple regression uses:", ["One predictor", "*Two or more predictor variables", "No predictors", "Only categorical variables"],
         "Multiple regression includes multiple explanatory variables."),
        ("In ŷ = b₀ + b₁x₁ + b₂x₂, b₁ represents:", ["The total effect of all variables", "*The change in ŷ per unit increase in x₁, holding x₂ constant", "The correlation", "The intercept"],
         "Each coefficient controls for the other variables."),
        ("R² always increases when adding more predictors because:", ["Better predictors are always added", "*Any new variable captures at least some noise, reducing residuals", "R² has no maximum", "Math requires it"],
         "Even random variables reduce the sum of squared residuals slightly."),
        ("Adjusted R² is preferred over R² because:", ["It's always higher", "*It penalizes for unnecessary predictors, preventing overfitting", "It's easier to compute", "It equals r"],
         "Adjusted R² only increases if the new variable genuinely improves the model."),
        ("Multicollinearity occurs when:", ["y is correlated with x", "*Predictor variables are highly correlated with each other", "There is no correlation", "The model has one predictor"],
         "Correlated predictors make it hard to separate their individual effects."),
        ("If height and weight (correlated) are both used to predict blood pressure:", ["Only height matters", "Only weight matters", "*Multicollinearity may make it hard to determine the individual effect of each", "The model is invalid"],
         "Correlated predictors share overlapping information."),
        ("ŷ = 5 + 2x₁ − 3x₂. When x₁ = 3 and x₂ = 1, ŷ = ?", ["10", "4", "*8", "14"],
         "ŷ = 5 + 2(3) − 3(1) = 5 + 6 − 3 = 8."),
        ("Overfitting means:", ["The model is too simple", "*The model fits noise in the training data and performs poorly on new data", "R² is too low", "The model has too few predictors"],
         "Too many predictors capture random noise rather than true patterns."),
        ("A significant predictor in multiple regression:", ["Always has the largest coefficient", "*Has a coefficient that is statistically significantly different from 0 (low p-value)", "Has the highest correlation with y", "Is always the first variable entered"],
         "Significance is determined by the p-value for each coefficient."),
        ("Multiple regression can handle:", ["Only quantitative predictors", "*Both quantitative and categorical predictors (using dummy variables)", "Only 2 predictors", "Only one response variable"],
         "Categorical variables are included using indicator (dummy) variables."),
        ("The intercept b₀ is the predicted y when:", ["x₁ = 1", "*All predictor variables = 0", "x₁ = x₂", "y = 0"],
         "The intercept is the baseline prediction."),
        ("A good multiple regression model has:", ["R² = 0", "*High adjusted R², significant predictors, and well-behaved residuals", "Many insignificant variables", "Multicollinearity"],
         "Good models explain variation, have significant predictors, and pass residual checks."),
        ("The F-test in regression tests:", ["Individual predictors", "*Whether the overall model is significant (at least one predictor is useful)", "The intercept", "Multicollinearity"],
         "The F-test evaluates the model as a whole."),
        ("Residual analysis in multiple regression checks:", ["Only normality", "Only linearity", "*Linearity, constant variance, normality, and independence", "Nothing"],
         "All regression assumptions should be verified."),
        ("Adding a variable that is unrelated to y:", ["Greatly increases R²", "*May slightly increase R² but decreases adjusted R²", "Decreases R²", "Has no effect"],
         "Irrelevant variables add noise; adjusted R² penalizes for this."),
        ("In business, multiple regression might predict sales using:", ["Only price", "*Price, advertising, season, and competitor activity", "No variables", "Only one variable"],
         "Multiple predictors capture the complexity of business outcomes."),
        ("Interaction terms (x₁ × x₂) in regression allow:", ["Only main effects", "*The effect of one variable to depend on the level of another", "Simpler models", "Zero coefficients"],
         "Interactions capture synergistic or antagonistic effects between variables."),
        ("Stepwise regression:", ["Uses all variables always", "Removes all variables", "*Adds or removes predictors based on statistical criteria to find a good model", "Is never used"],
         "Stepwise methods automate variable selection (though they have limitations)."),
        ("VIF (Variance Inflation Factor) measures:", ["Prediction accuracy", "R²", "*The degree of multicollinearity for each predictor", "The F-statistic"],
         "High VIF (>5 or 10) indicates problematic multicollinearity."),
        ("Multiple regression assumes residuals are:", ["Correlated", "Skewed", "*Approximately normal, independent, with constant variance", "Exactly zero"],
         "Standard regression assumptions must be checked."),
    ]
)
lessons[k] = v

# ── 8.5 Nonlinear Regression Models ──
k, v = build_lesson(8, 5, "Nonlinear Regression Models",
    "<h3>Nonlinear Regression Models</h3>"
    "<p>When the relationship between x and y is not linear, <b>nonlinear models</b> may fit better.</p>"
    "<ul><li><b>Quadratic model:</b> ŷ = a + bx + cx². Used for U-shaped or inverted-U patterns.</li>"
    "<li><b>Exponential model:</b> ŷ = ab<sup>x</sup>. Used for growth/decay patterns. Taking log(y) can linearize: log(ŷ) = log(a) + x·log(b).</li>"
    "<li><b>Power model:</b> ŷ = ax<sup>b</sup>. Taking logs of both sides: log(ŷ) = log(a) + b·log(x).</li>"
    "<li><b>Logarithmic model:</b> ŷ = a + b·ln(x). Used when growth slows over time.</li>"
    "<li><b>Transformations:</b> Taking log, square root, or reciprocal of x or y to straighten a curved relationship so linear regression can be applied.</li></ul>"
    "<p><b>Choosing a model:</b> Examine the scatterplot, try transformations, check residual plots, and compare r² values of different models.</p>",
    [
        ("Quadratic Model", "ŷ = a + bx + cx²; fits parabolic (U-shaped or inverted-U) patterns."),
        ("Exponential Model", "ŷ = ab^x; models multiplicative growth or decay."),
        ("Power Model", "ŷ = ax^b; linearized by taking logs of both variables."),
        ("Logarithmic Transformation", "Taking log(y) or log(x) to straighten a curved relationship for linear regression."),
        ("Model Selection", "Comparing scatterplots, residual plots, and r² values of different models to choose the best fit."),
    ],
    [
        ("When a scatterplot shows a curved pattern, a linear model:", ["Is always appropriate", "*May not be the best fit — consider nonlinear models", "Should be forced", "Will have r = 1"],
         "Curvature suggests a nonlinear model may fit better."),
        ("A quadratic model ŷ = a + bx + cx² fits:", ["Linear patterns", "*Parabolic (U-shaped or inverted-U) patterns", "Exponential growth", "Random scatter"],
         "The squared term creates a parabolic curve."),
        ("An exponential model ŷ = ab^x is used for:", ["Linear relationships", "*Growth or decay patterns", "U-shaped data", "Random data"],
         "Exponential models capture multiplicative growth or decline."),
        ("Taking log(y) transforms an exponential relationship into:", ["A quadratic", "A power model", "*A linear relationship (log(y) vs. x)", "Nothing"],
         "log(ŷ) = log(a) + x·log(b) is linear in x."),
        ("A power model ŷ = ax^b is linearized by:", ["Taking log of y only", "Taking log of x only", "*Taking log of both x and y", "No transformation"],
         "log(ŷ) = log(a) + b·log(x) is linear in log(x)."),
        ("The purpose of transformations is to:", ["Make data harder to analyze", "*Straighten a curved relationship so linear methods apply", "Always increase r", "Remove data points"],
         "Transformations convert nonlinear patterns into approximately linear ones."),
        ("If a residual plot from a linear model shows a curve:", ["The linear model is fine", "r must be high", "*A nonlinear model should be considered", "More data is needed"],
         "A curved residual pattern indicates linear model inadequacy."),
        ("Common transformations include:", ["Only log", "Only square root", "*Log, square root, reciprocal, and power transformations", "None exist"],
         "Several transformations can help linearize different types of curves."),
        ("After applying log(y), if the plot of log(y) vs. x is linear:", ["*An exponential model fits the original data", "A linear model fits the original data", "A power model fits", "No model fits"],
         "Linearity in log(y) vs. x implies exponential growth/decay in the original data."),
        ("After applying log(y) vs. log(x), if the plot is linear:", ["An exponential model fits", "A linear model fits", "*A power model fits the original data", "A quadratic fits"],
         "Linearity in log-log space implies a power relationship."),
        ("Model selection should consider:", ["Only r²", "Only the scatterplot", "*Scatterplots, residual plots, r² values, and the context of the data", "Only the p-value"],
         "Multiple criteria should guide model selection."),
        ("r² can be compared across models to:", ["Always choose the highest", "*Choose the model that best explains the variation (while checking residuals)", "Ignore nonlinear models", "Compare only linear models"],
         "Higher r² is better, but residual patterns must also be evaluated."),
        ("Population growth is often modeled by:", ["Linear regression", "*Exponential or logistic models", "Only quadratic models", "Only power models"],
         "Populations often grow exponentially or follow logistic curves."),
        ("A logistic model:", ["Is always linear", "*Models growth that levels off (S-shaped curve)", "Has no upper limit", "Is the same as exponential"],
         "Logistic growth has an upper carrying capacity."),
        ("Extrapolation with nonlinear models is:", ["Always safe", "*Still risky and should be done cautiously", "Never done", "Safe for exponential models only"],
         "Extrapolation beyond the data range is unreliable for any model."),
        ("If both linear and quadratic models are tried:", ["The linear always wins", "*Compare r², residual plots, and whether the added complexity is justified", "The quadratic always wins", "Neither works"],
         "Simpler models are preferred unless the more complex one is meaningfully better."),
        ("A logarithmic model ŷ = a + b·ln(x) is used when:", ["Growth accelerates", "*Growth slows as x increases (diminishing returns)", "There is no growth", "The relationship is linear"],
         "Logarithmic models capture diminishing returns."),
        ("Overfitting can occur in nonlinear modeling when:", ["*Too many parameters are used, fitting noise rather than the pattern", "The model is too simple", "r² is low", "Residuals are random"],
         "Complex models risk capturing noise rather than signal."),
        ("The principle of parsimony says:", ["Always use the most complex model", "*Use the simplest model that adequately fits the data", "Nonlinear is always better", "R² should always be 1"],
         "Parsimony favors simplicity — add complexity only when needed."),
        ("A scatterplot of y vs. x curves upward at an increasing rate. This suggests:", ["A linear model", "A logarithmic model", "*An exponential or power model", "No model exists"],
         "Accelerating growth fits exponential or power curves."),
    ]
)
lessons[k] = v

# ── 8.6 Applications in Prediction Models ──
k, v = build_lesson(8, 6, "Applications in Prediction Models",
    "<h3>Applications in Prediction Models</h3>"
    "<p>Regression models are widely used for <b>prediction</b> in many fields.</p>"
    "<ul><li><b>Weather forecasting:</b> Multiple regression with variables like pressure, temperature, humidity to predict rainfall or temperature.</li>"
    "<li><b>Sports analytics:</b> Sabermetrics uses regression to predict player performance and team wins (e.g., MLB's Moneyball approach).</li>"
    "<li><b>Medical prediction:</b> Risk models predict disease likelihood based on patient characteristics (e.g., Framingham cardiovascular risk score).</li>"
    "<li><b>Business:</b> Sales forecasting, customer churn prediction, pricing models.</li>"
    "<li><b>Machine learning:</b> Linear and nonlinear regression are foundational algorithms in predictive modeling and AI.</li></ul>"
    "<p><b>Cross-validation:</b> Testing the model on data not used to build it, ensuring it generalizes well. Common approach: split data into training and testing sets.</p>"
    "<p><b>Prediction intervals</b> are wider than confidence intervals because they account for both the regression uncertainty and individual variation.</p>",
    [
        ("Prediction Model", "A statistical model used to estimate future or unknown values of a response variable based on predictor variables."),
        ("Cross-Validation", "Testing a model on data not used for training to assess how well it generalizes to new data."),
        ("Training vs. Testing Data", "Training data builds the model; testing data evaluates its predictive accuracy on unseen observations."),
        ("Prediction Interval", "A range for an individual future observation; wider than a confidence interval because it includes individual variability."),
        ("Sabermetrics", "The application of statistical analysis to baseball (and other sports) for performance prediction and decision-making."),
    ],
    [
        ("Regression-based predictions are used in:", ["Only statistics courses", "*Weather, medicine, sports, business, and many other fields", "Only physics", "Only economics"],
         "Regression is one of the most versatile predictive tools across disciplines."),
        ("Cross-validation helps ensure:", ["Overfitting", "*The model generalizes well to new, unseen data", "The training set is large", "The test set is small"],
         "Testing on held-out data checks real-world predictive performance."),
        ("A prediction interval is __ than a confidence interval:", ["Narrower", "*Wider", "The same width", "Always zero-width"],
         "Prediction intervals include both model uncertainty and individual variation."),
        ("The Moneyball approach used:", ["No statistics", "Only batting average", "*Regression and analytics to identify undervalued players", "Random selection"],
         "Oakland A's used statistical models to evaluate players others overlooked."),
        ("In medical risk prediction, the Framingham score predicts:", ["Lab costs", "*Cardiovascular disease risk based on patient factors", "Appointment times", "Insurance premiums"],
         "The Framingham model uses age, blood pressure, cholesterol, etc. to estimate heart disease risk."),
        ("Training data is used to:", ["Test the model", "Validate predictions", "*Build (fit) the model", "Replace the model"],
         "Training data is used to estimate model parameters."),
        ("Testing data is used to:", ["Build the model", "*Evaluate how well the model predicts unseen observations", "Increase sample size", "Replace outliers"],
         "Testing on new data checks generalization."),
        ("Overfitting a prediction model means it:", ["Predicts well on new data", "*Fits training data too closely and performs poorly on new data", "Has low r²", "Is too simple"],
         "Overfitting captures noise, reducing generalization."),
        ("A sales forecasting model might include:", ["Only last month's sales", "*Multiple predictors: advertising, price, season, economic indicators", "No variables", "Only random noise"],
         "Multiple predictors capture different factors influencing sales."),
        ("Customer churn prediction uses regression to:", ["Increase churn", "Ignore at-risk customers", "*Identify customers likely to leave so companies can intervene", "Calculate revenue only"],
         "Predicting churn helps businesses retain customers."),
        ("Weather prediction models use:", ["Only temperature", "*Multiple variables including pressure, humidity, wind, and historical data", "No statistics", "Only simple averages"],
         "Weather models are complex multivariate systems."),
        ("A prediction interval for a new observation at x = 10 accounts for:", ["Only the mean's uncertainty", "*Both the regression line's uncertainty and individual observation variability", "Nothing", "Only the residual"],
         "Both sources of variation contribute to prediction intervals."),
        ("Machine learning regression differs from classical regression mainly in:", ["Using different math", "*Emphasis on prediction accuracy and cross-validation over inference", "Having no coefficients", "Not using data"],
         "ML focuses on predictive performance; classical regression also emphasizes interpretation."),
        ("K-fold cross-validation:", ["Uses data once", "*Splits data into k parts, trains on k−1 and tests on the remaining — repeated k times", "Never validates", "Uses all data for training"],
         "Each fold gets a turn as the test set."),
        ("Prediction models should be updated when:", ["Never", "*New data becomes available or the underlying process changes", "Only when r² < 0.5", "Only at year-end"],
         "Models must evolve with changing data and conditions."),
        ("Residuals from a prediction model should be:", ["Large", "Patterned", "*Small with no systematic pattern", "Always positive"],
         "Small random residuals indicate good predictions."),
        ("In sports analytics, regression can predict:", ["Only wins", "*Player performance, game outcomes, contract value, and injury risk", "Nothing useful", "Only batting averages"],
         "Analytics cover many aspects of sports performance."),
        ("A confidence interval for E(y) at x = 10 estimates:", ["A single y", "The slope", "*The average y for all observations where x = 10", "Individual variation"],
         "CI for E(y|x) estimates the mean response, not an individual observation."),
        ("Feature engineering in prediction involves:", ["Removing all variables", "*Creating new variables from existing ones to improve model performance", "Ignoring data", "Using only raw data"],
         "Transformations, interactions, and derived features can enhance predictions."),
        ("The best prediction models balance:", ["*Complexity and generalizability (parsimony)", "Maximum complexity and minimum data", "Only training accuracy", "Only simplicity"],
         "Models should be complex enough to capture real patterns but simple enough to generalize."),
    ]
)
lessons[k] = v

# ── 8.7 Case Studies in Economics & Finance ──
k, v = build_lesson(8, 7, "Case Studies in Economics & Finance",
    "<h3>Case Studies in Economics & Finance</h3>"
    "<p>Statistics and regression analysis are central to economics and finance.</p>"
    "<ul><li><b>Supply and demand:</b> Regression models estimate how price changes affect quantity demanded (elasticity).</li>"
    "<li><b>Stock market:</b> The Capital Asset Pricing Model (CAPM) uses regression: E(Rᵢ) = Rₑ + βᵢ(Rₘ − Rₑ), where β is the stock's sensitivity to market movements.</li>"
    "<li><b>Inflation and unemployment:</b> The Phillips Curve models the inverse relationship — as unemployment decreases, inflation tends to increase.</li>"
    "<li><b>GDP prediction:</b> Multiple regression models forecast GDP using investment, consumption, government spending, and net exports.</li>"
    "<li><b>Risk management:</b> Value at Risk (VaR) uses normal distributions and confidence levels to estimate potential portfolio losses.</li>"
    "<li><b>Consumer behavior:</b> Regression on demographic and economic variables predicts spending patterns.</li></ul>"
    "<p>Economic data often violates regression assumptions (autocorrelation, non-stationarity), requiring specialized techniques like time series analysis.</p>",
    [
        ("Elasticity", "A measure of how much quantity demanded changes in response to a price change; estimated via regression."),
        ("Beta (β) in CAPM", "A stock's sensitivity to market movements; β > 1 means more volatile than the market."),
        ("Phillips Curve", "The historical inverse relationship between unemployment and inflation."),
        ("Value at Risk (VaR)", "The estimated maximum loss of a portfolio at a given confidence level over a specified time period."),
        ("Time Series Analysis", "Statistical methods for data collected over time, addressing autocorrelation and trends."),
    ],
    [
        ("In economics, regression is used to:", ["Only calculate GDP", "Only predict stock prices", "*Model relationships like supply/demand, inflation, and growth", "Avoid data analysis"],
         "Regression is a core tool in economics for modeling relationships."),
        ("β (beta) in CAPM measures:", ["*A stock's sensitivity to overall market movements", "The y-intercept", "The risk-free rate", "The inflation rate"],
         "β quantifies systematic risk — how much a stock moves relative to the market."),
        ("A β > 1 means the stock is:", ["Less volatile than the market", "*More volatile than the market", "Exactly as volatile as the market", "Unrelated to the market"],
         "β > 1 means the stock amplifies market movements."),
        ("The Phillips Curve shows:", ["A positive relationship between inflation and unemployment", "*An inverse relationship — lower unemployment is associated with higher inflation", "No relationship", "A perfect linear relationship"],
         "As unemployment falls, wage and price pressures tend to increase inflation."),
        ("Elasticity is estimated using regression to measure:", ["*How sensitive quantity demanded is to price changes", "Total revenue only", "Consumer happiness", "Market index returns"],
         "Elasticity = % change in quantity / % change in price."),
        ("Value at Risk (VaR) at 95% confidence estimates:", ["Guaranteed profit", "*The maximum loss expected 95% of the time over a specified period", "Average return", "Minimum gain"],
         "VaR provides a threshold: losses exceed this level only 5% of the time."),
        ("GDP forecasting uses:", ["No statistics", "Only past GDP", "*Multiple regression with indicators like consumption, investment, government spending", "Random guessing"],
         "Multiple economic variables are used to forecast GDP."),
        ("Autocorrelation in economic data means:", ["Data points are independent", "*Current values are correlated with past values", "There is no pattern", "The data is random"],
         "Economic time series often have serial correlation."),
        ("Time series analysis is needed because:", ["Economic data is static", "*Economic data changes over time and may have trends, seasonality, or autocorrelation", "Regression doesn't work", "No assumptions exist"],
         "Standard regression assumptions may be violated with time-ordered data."),
        ("If a stock has β = 0.5 and the market rises 10%, the stock is expected to rise:", ["10%", "*5%", "15%", "0%"],
         "β = 0.5 × 10% market return = 5% expected return."),
        ("Regression helps companies set prices by:", ["Guessing", "*Estimating the relationship between price and quantity sold", "Ignoring demand", "Setting random prices"],
         "Price-demand regression models guide pricing strategy."),
        ("The risk-free rate in CAPM represents:", ["The market return", "The stock's return", "*The return on a virtually risk-free investment like government bonds", "β"],
         "The risk-free rate is the baseline return for zero risk."),
        ("A consumer spending model might include:", ["Only income", "*Income, age, education, family size, and regional factors", "No variables", "Only credit score"],
         "Multiple predictors capture the complexity of spending behavior."),
        ("Non-stationarity means:", ["*The statistical properties of the data change over time", "The data is constant", "Regression is perfect", "No trend exists"],
         "Non-stationary data requires differencing or other techniques."),
        ("The 2008 financial crisis revealed flaws in:", ["No models", "Simple portfolios", "*Risk models that underestimated extreme events (tail risk)", "All statistics"],
         "Models using normal distribution assumptions missed extreme market crashes."),
        ("Regression in finance predicts:", ["Only stock prices", "Only interest rates", "*Returns, risk, prices, demand, and many other financial outcomes", "Nothing useful"],
         "Regression is foundational across financial analysis."),
        ("Economic regression models must account for:", ["Nothing special", "*Potential violations like autocorrelation, heteroscedasticity, and endogeneity", "Only sample size", "Only r²"],
         "Economic data often requires specialized diagnostic checks."),
        ("Hedonic pricing models use regression to estimate:", ["Stock returns", "*The value of individual characteristics (e.g., house features) contributing to price", "Government spending", "Inflation"],
         "Hedonic models decompose price into the value of component features."),
        ("Interest rate predictions use regression with:", ["Only guesses", "*Inflation expectations, GDP growth, and monetary policy indicators", "No data", "Only one variable"],
         "Multiple macroeconomic factors influence interest rates."),
        ("Statistics and regression in economics are essential for:", ["Only academic research", "Only government", "Only banks", "*Policy decisions, business strategy, investment, and research across sectors"],
         "Economic statistics inform decisions at all levels."),
    ]
)
lessons[k] = v

# ── Write ──
with open(PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)
data.update(lessons)
with open(PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print(f"Updated {len(lessons)} lessons (Unit 8)")
