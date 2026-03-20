#!/usr/bin/env python3
"""
Generate course content for all maintenance-break high school courses.
Creates: course page HTML, lesson folders, JSON content data, and lesson HTML files.
"""
import json
import os
import html

BASE = os.path.dirname(os.path.abspath(__file__))
ARISEDU = os.path.join(BASE, "ArisEdu Project Folder")
COURSE_FILES = os.path.join(ARISEDU, "CourseFiles")
COURSE_HOMEPAGE = os.path.join(ARISEDU, "CourseHomepage")
CONTENT_DATA = os.path.join(BASE, "content_data")

# ─── Course Definitions ───────────────────────────────────────────────
COURSES = [
    {
        "id": "precalculus",
        "title": "Precalculus",
        "page_title": "High School: Precalculus",
        "html_file": "precalculus.html",
        "lessons_folder": "PrecalculusLessons",
        "json_slug": "precalculus",
        "course_prefix": "precalc",
        "link_id": "precalc-link",
        "category": "math",
        "color": "#a78bfa",
        "units": {
            1: {"name": "Foundations of Algebra and Functions", "lessons": [
                "Review of Algebra (factoring, radicals, rational expressions)",
                "Order of Operations & Exponents",
                "Relations vs. Functions",
                "Domain & Range (interval notation)",
                "Function Notation & Evaluation",
                "Graphing Basics (intercepts, symmetry)",
                "Transformations (shifts, reflections, stretches)",
                "⭐ Inverse Functions & Composition",
                "Piecewise Functions",
                "Applications in Modeling"
            ]},
            2: {"name": "Linear and Quadratic Functions", "lessons": [
                "Linear Equations & Graphs",
                "Slope, Intercepts, and Parallel/Perpendicular Lines",
                "Quadratic Functions (vertex form, standard form)",
                "Completing the Square",
                "Quadratic Formula & Complex Solutions",
                "Graphing Quadratic Functions",
                "⭐ Applications of Linear & Quadratic Models",
                "Absolute Value Functions",
                "Inequalities (linear & quadratic)"
            ]},
            3: {"name": "Polynomial Functions", "lessons": [
                "Characteristics of Polynomials (degree, leading coefficient)",
                "End Behavior & Graph Shapes",
                "Factoring Techniques (synthetic division, long division)",
                "Roots, Zeros, and Multiplicity",
                "⭐ Intermediate Value Theorem",
                "Graphing Polynomial Functions",
                "⭐ Rational Root Theorem",
                "Applications of Polynomial Models",
                "Case Studies in Economics & Physics"
            ]},
            4: {"name": "Rational Functions", "lessons": [
                "Rational Expressions & Simplification",
                "Vertical, Horizontal, and Oblique Asymptotes",
                "Holes and Discontinuities",
                "Graphing Rational Functions",
                "⭐ Partial Fraction Decomposition",
                "Applications in Real-World Ratios (rates, proportions)",
                "Rational Inequalities",
                "Case Studies in Engineering"
            ]},
            5: {"name": "Exponential and Logarithmic Functions", "lessons": [
                "Exponential Growth & Decay Models",
                "Compound Interest & Continuous Growth",
                "Properties of Logarithms",
                "Change of Base Formula",
                "Solving Exponential & Logarithmic Equations",
                "Applications: pH, Richter Scale, Population Growth",
                "⭐ Graphing Exponential & Logarithmic Functions",
                "Logistic Growth Models",
                "Case Studies in Biology & Finance"
            ]},
            6: {"name": "Trigonometric Foundations", "lessons": [
                "Angles in Degrees & Radians",
                "Arc Length & Sector Area",
                "Unit Circle & Special Angles",
                "Sine, Cosine, Tangent Definitions",
                "Graphs of Trigonometric Functions (amplitude, period, phase shift)",
                "Inverse Trigonometric Functions",
                "⭐ Applications in Physics & Engineering",
                "Coterminal & Reference Angles",
                "Case Studies in Navigation"
            ]},
            7: {"name": "Trigonometric Identities and Equations", "lessons": [
                "Pythagorean Identities",
                "Sum & Difference Formulas",
                "Double-Angle & Half-Angle Formulas",
                "⭐ Product-to-Sum and Sum-to-Product Identities",
                "Solving Trigonometric Equations",
                "Applications in Modeling Periodic Phenomena",
                "Case Studies in Engineering",
                "⭐ AP Calculus Prep"
            ]},
            8: {"name": "Sequences and Series", "lessons": [
                "Arithmetic Sequences (nth term, partial sums)",
                "Geometric Sequences (nth term, infinite series)",
                "Sigma Notation & Summation Rules",
                "⭐ Mathematical Induction",
                "⭐ Binomial Theorem",
                "Applications in Finance & Growth Patterns",
                "Case Studies in Probability"
            ]},
            9: {"name": "Limits and Continuity", "lessons": [
                "Concept of Limits (graphical, numerical approaches)",
                "Evaluating Limits Algebraically",
                "One-Sided Limits",
                "Continuity & Types of Discontinuities",
                "Infinite Limits & Asymptotic Behavior",
                "⭐ Applications: Instantaneous Rate of Change",
                "Piecewise Functions & Limits",
                "⭐ AP Calculus Prep"
            ]},
            10: {"name": "Introduction to Calculus Concepts", "lessons": [
                "Derivative as Slope of Tangent Line",
                "Derivative Rules (power rule basics)",
                "Applications in Optimization",
                "Area Under Curves (intro to integration)",
                "⭐ Connecting Precalculus to Calculus",
                "⭐ AP-Style Practice Problems",
                "⭐ Capstone Project: Modeling with Functions",
                "⭐ Comprehensive Review & AP Exam Prep"
            ]},
        }
    },
    {
        "id": "trigonometry",
        "title": "Trigonometry",
        "page_title": "High School: Trigonometry",
        "html_file": "trigonometry.html",
        "lessons_folder": "TrigonometryLessons",
        "json_slug": "trigonometry",
        "course_prefix": "trig",
        "link_id": "trig-link",
        "category": "math",
        "color": "#a78bfa",
        "units": {
            1: {"name": "Foundations of Trigonometry", "lessons": [
                "Angles in Degrees & Radians",
                "Arc Length & Sector Area",
                "Right Triangle Ratios (SOH-CAH-TOA)",
                "Special Triangles (30°–60°–90°, 45°–45°–90°)",
                "⭐ Unit Circle Basics",
                "Coterminal Angles & Reference Angles",
                "Applications in Geometry"
            ]},
            2: {"name": "Trigonometric Functions", "lessons": [
                "Definition of Sine, Cosine, Tangent",
                "Reciprocal Functions (csc, sec, cot)",
                "Graphs of Sine & Cosine",
                "Graphs of Tangent, Cotangent, Secant, Cosecant",
                "⭐ Transformations of Trig Graphs (amplitude, period, phase shift)",
                "Symmetry & Periodicity",
                "Applications in Sound Waves"
            ]},
            3: {"name": "Inverse Trigonometric Functions", "lessons": [
                "Definition & Domains",
                "Graphs of Inverse Trig Functions",
                "Solving Equations with Inverse Trig",
                "⭐ Applications in Geometry & Physics",
                "Restrictions & Principal Values",
                "Applications in Engineering"
            ]},
            4: {"name": "Trigonometric Identities", "lessons": [
                "Pythagorean Identities",
                "Reciprocal Identities",
                "Quotient Identities",
                "Cofunction Identities",
                "⭐ Verifying Identities",
                "Applications in Simplifying Expressions",
                "Case Studies in Physics"
            ]},
            5: {"name": "Advanced Trigonometric Identities", "lessons": [
                "Sum & Difference Formulas",
                "Double-Angle Formulas",
                "Half-Angle Formulas",
                "⭐ Product-to-Sum & Sum-to-Product Formulas",
                "Applications in Simplifying Expressions",
                "Case Studies in Engineering",
                "⭐ Applications in AP Calculus"
            ]},
            6: {"name": "Solving Trigonometric Equations", "lessons": [
                "Linear Trig Equations",
                "Quadratic Trig Equations",
                "Multiple-Angle Equations",
                "General Solutions & Periodicity",
                "⭐ Applications in Modeling Cyclical Behavior",
                "Case Studies in Physics",
                "⭐ Applications in AP Prep"
            ]},
            7: {"name": "Laws of Sines and Cosines", "lessons": [
                "Law of Sines (ambiguous case)",
                "Law of Cosines",
                "Area of Triangles (Heron's Formula, sine area formula)",
                "⭐ Applications in Navigation",
                "Applications in Surveying",
                "Case Studies in Engineering",
                "Applications in Astronomy"
            ]},
            8: {"name": "Polar Coordinates and Complex Numbers", "lessons": [
                "Polar Coordinate System",
                "Graphing Polar Equations",
                "Converting Between Polar & Rectangular Coordinates",
                "Complex Numbers in Polar Form",
                "⭐ De Moivre's Theorem",
                "Applications in Electrical Engineering",
                "Case Studies in Physics"
            ]},
            9: {"name": "Vectors and Applications", "lessons": [
                "Vector Basics (magnitude, direction)",
                "Vector Operations (addition, scalar multiplication)",
                "Dot Product & Applications",
                "Cross Product (introductory)",
                "⭐ Applications in Physics & Engineering",
                "Case Studies in Computer Graphics",
                "⭐ Applications in AP Calculus"
            ]},
            10: {"name": "Analytic Trigonometry & AP Prep", "lessons": [
                "⭐ Trigonometric Proofs",
                "⭐ Trigonometric Substitutions (integration prep)",
                "Parametric Equations & Trigonometry",
                "⭐ Applications in Calculus (limits, derivatives of trig functions)",
                "⭐ Comprehensive Review & AP Exam Practice",
                "⭐ Capstone Project: Real-World Trigonometric Model"
            ]},
        }
    },
    {
        "id": "statistics",
        "title": "Statistics & Probability",
        "page_title": "High School: Statistics & Probability",
        "html_file": "statistics.html",
        "lessons_folder": "StatisticsLessons",
        "json_slug": "statistics",
        "course_prefix": "stats",
        "link_id": "statistics-link",
        "category": "math",
        "color": "#a78bfa",
        "units": {
            1: {"name": "Introduction to Statistics", "lessons": [
                "What is Statistics?",
                "Populations vs. Samples",
                "Experimental Design & Bias",
                "Types of Data (qualitative vs. quantitative)",
                "Levels of Measurement (nominal, ordinal, interval, ratio)",
                "⭐ Random Sampling & Randomization",
                "Case Studies in Statistical Misuse"
            ]},
            2: {"name": "Data Representation", "lessons": [
                "Frequency Tables",
                "Histograms & Bar Graphs",
                "Stem-and-Leaf Plots",
                "Boxplots & Quartiles",
                "Scatterplots & Correlation",
                "Pie Charts & Circle Graphs",
                "⭐ Choosing Appropriate Graphs",
                "Case Studies in Data Visualization"
            ]},
            3: {"name": "Descriptive Statistics", "lessons": [
                "Measures of Central Tendency (mean, median, mode)",
                "Measures of Spread (range, variance, standard deviation)",
                "Percentiles & Quartiles",
                "⭐ Z-Scores & Standardization",
                "Coefficient of Variation",
                "Interpreting Data in Context",
                "Case Studies in Sports & Medicine"
            ]},
            4: {"name": "Probability Foundations", "lessons": [
                "Basic Probability Rules",
                "Counting Principles (permutations, combinations)",
                "Independent & Dependent Events",
                "Conditional Probability",
                "Probability Trees",
                "Venn Diagrams",
                "Applications in Games of Chance",
                "⭐ Probability in Genetics"
            ]},
            5: {"name": "Random Variables & Distributions", "lessons": [
                "Discrete Random Variables",
                "Continuous Random Variables",
                "Binomial Distribution",
                "⭐ Normal Distribution",
                "⭐ Central Limit Theorem",
                "Poisson Distribution",
                "Applications in Quality Control",
                "Case Studies in Real-World Distributions"
            ]},
            6: {"name": "Sampling & Experimental Design", "lessons": [
                "Sampling Methods (systematic, stratified, cluster)",
                "Bias in Sampling",
                "Designing Surveys & Experiments",
                "⭐ Randomization & Control Groups",
                "Simulation Models",
                "Case Studies in Political Polling",
                "Ethics in Data Collection"
            ]},
            7: {"name": "Statistical Inference", "lessons": [
                "⭐ Confidence Intervals (mean, proportion)",
                "Margin of Error",
                "⭐ Hypothesis Testing (null vs. alternative)",
                "Type I & Type II Errors",
                "⭐ P-values & Significance Levels",
                "Interpreting Statistical Results",
                "Case Studies in Medical Trials"
            ]},
            8: {"name": "Regression & Correlation", "lessons": [
                "Scatterplots & Correlation Coefficient",
                "⭐ Least Squares Regression Line",
                "Residuals & Line Fit",
                "Multiple Regression (introductory)",
                "Nonlinear Regression Models",
                "Applications in Prediction Models",
                "Case Studies in Economics & Finance"
            ]},
            9: {"name": "Advanced Probability & Statistics", "lessons": [
                "Law of Large Numbers",
                "Expected Value",
                "Probability Distributions in Real Life",
                "⭐ Chi-Square Tests",
                "⭐ ANOVA (Analysis of Variance)",
                "Nonparametric Tests",
                "Case Studies in Psychology & Biology"
            ]},
            10: {"name": "AP Prep & Applications", "lessons": [
                "⭐ Review of Key Formulas",
                "⭐ AP-Style Practice Problems",
                "⭐ Interpreting Graphical Data in AP Exams",
                "Real-World Applications (medicine, economics, sports)",
                "⭐ Capstone Project: Statistical Analysis of a Dataset",
                "⭐ Comprehensive Review & AP Exam Practice"
            ]},
        }
    },
    {
        "id": "linear_algebra",
        "title": "Linear Algebra",
        "page_title": "High School: Linear Algebra",
        "html_file": "linear_algebra.html",
        "lessons_folder": "LinearAlgebraLessons",
        "json_slug": "linear_algebra",
        "course_prefix": "linalg",
        "link_id": "linalg-link",
        "category": "math",
        "color": "#a78bfa",
        "units": {
            1: {"name": "Foundations of Linear Algebra", "lessons": [
                "Scalars, Vectors, and Matrices",
                "Matrix Notation & Dimensions",
                "Vector Operations (addition, scalar multiplication)",
                "Matrix Operations (addition, multiplication)",
                "Identity & Zero Matrices",
                "Transpose of a Matrix",
                "Applications in Geometry",
                "Applications in Physics"
            ]},
            2: {"name": "Systems of Linear Equations", "lessons": [
                "Solving Systems by Substitution & Elimination",
                "Matrix Representation of Systems",
                "⭐ Gaussian Elimination",
                "⭐ Gauss-Jordan Elimination",
                "Row Echelon Form",
                "Consistent vs. Inconsistent Systems",
                "Applications in Economics",
                "Applications in Engineering"
            ]},
            3: {"name": "Determinants", "lessons": [
                "Definition of Determinants",
                "Properties of Determinants",
                "Cofactor Expansion",
                "Determinants of Larger Matrices",
                "⭐ Cramer's Rule",
                "Determinants & Area/Volume",
                "Applications in Geometry",
                "Applications in Physics"
            ]},
            4: {"name": "Matrix Inverses", "lessons": [
                "Invertible Matrices",
                "Finding Inverses (row reduction method)",
                "Adjoint Method",
                "Singular vs. Non-Singular Matrices",
                "Applications of Inverse Matrices",
                "⭐ Using Inverses in Cryptography",
                "Applications in Computer Science",
                "Applications in Economics"
            ]},
            5: {"name": "Vector Spaces", "lessons": [
                "Definition of Vector Spaces",
                "Subspaces",
                "Linear Independence",
                "⭐ Basis & Dimension",
                "Span of a Set",
                "Null Space & Column Space",
                "Applications in Computer Graphics",
                "Applications in Data Science"
            ]},
            6: {"name": "Linear Transformations", "lessons": [
                "Definition of Linear Transformations",
                "Kernel & Image",
                "Matrix Representation of Transformations",
                "Composition of Transformations",
                "⭐ Rotations & Reflections",
                "Scaling & Shearing",
                "Applications in Physics",
                "Applications in Engineering"
            ]},
            7: {"name": "Eigenvalues and Eigenvectors", "lessons": [
                "Characteristic Polynomial",
                "Finding Eigenvalues",
                "Finding Eigenvectors",
                "⭐ Diagonalization",
                "Applications in Differential Equations",
                "Applications in Physics",
                "Applications in Computer Science",
                "Applications in Economics"
            ]},
            8: {"name": "Orthogonality and Inner Products", "lessons": [
                "Dot Product & Orthogonality",
                "Orthogonal Projections",
                "⭐ Gram-Schmidt Process",
                "Orthogonal Matrices",
                "Inner Product Spaces",
                "⭐ Applications in Data Compression (PCA)",
                "Applications in Machine Learning",
                "Applications in Quantum Mechanics"
            ]},
            9: {"name": "Advanced Topics", "lessons": [
                "Complex Vector Spaces",
                "⭐ Jordan Canonical Form",
                "⭐ Singular Value Decomposition (SVD)",
                "Applications in Machine Learning",
                "Applications in Quantum Mechanics",
                "Applications in Image Processing",
                "Applications in Signal Processing",
                "Applications in Statistics"
            ]},
            10: {"name": "AP Prep & Capstone", "lessons": [
                "⭐ Proofs in Linear Algebra",
                "⭐ AP-Style Practice Problems",
                "Applications in Computer Science (networks, algorithms)",
                "Applications in Engineering (structural analysis)",
                "Applications in Physics (quantum states)",
                "Applications in Economics (input-output models)",
                "⭐ Capstone Project: Real-World Linear Algebra Model",
                "⭐ Comprehensive Review & AP Exam Practice"
            ]},
        }
    },
    {
        "id": "financial_math",
        "title": "Financial Math",
        "page_title": "High School: Financial Math",
        "html_file": "financial_math.html",
        "lessons_folder": "FinancialMathLessons",
        "json_slug": "financial_math",
        "course_prefix": "finmath",
        "link_id": "finmath-link",
        "category": "math",
        "color": "#a78bfa",
        "units": {
            1: {"name": "Foundations of Financial Literacy", "lessons": [
                "Importance of Financial Literacy",
                "Sources of Income (wages, salaries, investments)",
                "Budgeting Basics",
                "Needs vs. Wants",
                "Opportunity Cost in Financial Decisions",
                "Short-Term vs. Long-Term Goals",
                "Case Studies in Personal Finance",
                "Financial Decision-Making Models"
            ]},
            2: {"name": "Simple and Compound Interest", "lessons": [
                "Simple Interest Formula",
                "Compound Interest Formula",
                "⭐ Continuous Compounding",
                "Growth vs. Decay Models",
                "Applications in Savings Accounts",
                "Comparing Interest Scenarios",
                "Case Studies in Banking",
                "Technology Tools for Interest Calculations"
            ]},
            3: {"name": "Loans and Mortgages", "lessons": [
                "Loan Terminology (principal, interest, term)",
                "Amortization Schedules",
                "Mortgages (fixed vs. variable rates)",
                "Credit Cards & Debt Management",
                "Student Loans & Repayment Options",
                "⭐ Real Estate Financing",
                "Case Studies in Borrowing",
                "Loan Comparison & Decision Making"
            ]},
            4: {"name": "Investments and Annuities", "lessons": [
                "Stocks, Bonds, and Mutual Funds",
                "Risk vs. Return",
                "Annuities (ordinary vs. annuity due)",
                "Retirement Accounts (401k, IRA)",
                "⭐ Long-Term Investment Strategies",
                "Diversification & Portfolio Management",
                "Case Studies in Investing",
                "Technology in Investment Planning"
            ]},
            5: {"name": "Personal Budgeting", "lessons": [
                "Creating a Personal Budget",
                "Tracking Expenses",
                "Emergency Funds",
                "Short-Term vs. Long-Term Planning",
                "Case Studies in Budgeting",
                "Technology Tools for Budgeting",
                "Lifestyle Choices & Financial Impact",
                "Budget Adjustments & Flexibility"
            ]},
            6: {"name": "Taxes and Insurance", "lessons": [
                "Basics of Income Tax",
                "Tax Brackets & Deductions",
                "Property & Sales Taxes",
                "Insurance Types (health, auto, life)",
                "⭐ Risk Management Strategies",
                "Case Studies in Tax Planning",
                "Insurance in Real Life",
                "Tax Software & Filing Tools"
            ]},
            7: {"name": "Business and Entrepreneurship", "lessons": [
                "Business Start-Up Costs",
                "Profit & Loss Statements",
                "Break-Even Analysis",
                "Small Business Financing",
                "⭐ Entrepreneurship Case Studies",
                "Marketing & Financial Planning",
                "Business Risk & Reward",
                "Technology in Business Finance"
            ]},
            8: {"name": "Financial Markets", "lessons": [
                "Stock Market Basics",
                "Reading Stock Tables",
                "Market Indices (Dow, S&P 500)",
                "Trading Strategies",
                "⭐ Global Financial Systems",
                "Case Studies in Market Behavior",
                "Technology in Financial Markets",
                "Behavioral Finance"
            ]},
            9: {"name": "Advanced Financial Applications", "lessons": [
                "⭐ Time Value of Money",
                "Net Present Value (NPV)",
                "Internal Rate of Return (IRR)",
                "Financial Modeling with Spreadsheets",
                "Case Studies in Corporate Finance",
                "Risk Analysis & Forecasting",
                "⭐ Applications in AP Economics",
                "Case Studies in International Finance"
            ]},
            10: {"name": "AP Prep & Capstone", "lessons": [
                "⭐ Review of Key Formulas",
                "⭐ AP-Style Practice Problems",
                "⭐ Financial Math in AP Economics Context",
                "Real-World Applications (housing, retirement, investing)",
                "⭐ Capstone Project: Personal Financial Plan",
                "⭐ Comprehensive Review & AP Exam Practice",
                "Case Studies in AP-Level Scenarios"
            ]},
        }
    },
    {
        "id": "earth_science",
        "title": "Earth Science",
        "page_title": "High School: Earth Science",
        "html_file": "earth_science.html",
        "lessons_folder": "EarthScienceLessons",
        "json_slug": "earth_science",
        "course_prefix": "earthsci",
        "link_id": "earthsci-link",
        "category": "science",
        "color": "#3b82f6",
        "units": {
            1: {"name": "Earth's Structure & Minerals", "lessons": [
                "Earth's Layers (Crust, Mantle, Core)", "Mineral Identification",
                "Types of Rocks (Igneous, Sedimentary, Metamorphic)", "The Rock Cycle",
                "Soil Formation & Composition"
            ]},
            2: {"name": "Plate Tectonics", "lessons": [
                "Continental Drift & Evidence", "Seafloor Spreading",
                "Plate Boundaries (Convergent, Divergent, Transform)",
                "Earthquakes & Seismic Waves", "Volcanoes & Hot Spots"
            ]},
            3: {"name": "Earth's Surface Processes", "lessons": [
                "Weathering (Mechanical & Chemical)", "Erosion & Deposition",
                "River Systems & Landforms", "Glaciers & Ice Ages",
                "Mass Wasting & Landslides"
            ]},
            4: {"name": "Earth's History", "lessons": [
                "Relative Dating (Superposition, Cross-Cutting)",
                "Absolute Dating & Radiometric Methods", "The Geologic Time Scale",
                "Fossils & the Fossil Record", "Mass Extinctions & Evolution"
            ]},
            5: {"name": "Atmosphere & Weather", "lessons": [
                "Composition & Layers of the Atmosphere",
                "Energy Transfer (Radiation, Conduction, Convection)",
                "Air Pressure, Wind & Coriolis Effect",
                "Cloud Types & Precipitation", "Weather Fronts & Storms"
            ]},
            6: {"name": "Climate & Climate Change", "lessons": [
                "Climate vs. Weather", "Factors Affecting Climate",
                "Climate Zones & Biomes", "The Greenhouse Effect",
                "Evidence of Climate Change", "Human Impact on Climate"
            ]},
            7: {"name": "Oceanography", "lessons": [
                "Ocean Floor Features", "Ocean Water Properties",
                "Ocean Currents & Circulation", "Tides & Their Causes",
                "Marine Ecosystems"
            ]},
        }
    },
    {
        "id": "environmental_science",
        "title": "Environmental Science",
        "page_title": "High School: Environmental Science",
        "html_file": "environmental_science.html",
        "lessons_folder": "EnvironmentalScienceLessons",
        "json_slug": "environmental_science",
        "course_prefix": "envsci",
        "link_id": "envscience-link",
        "category": "science",
        "color": "#3b82f6",
        "units": {
            1: {"name": "Introduction to Environmental Science", "lessons": [
                "What is Environmental Science?",
                "Interdisciplinary Nature of the Field",
                "Ecosystem Basics (Producers, Consumers, Decomposers)",
                "Biogeochemical Cycles (Carbon, Nitrogen, Water)",
                "Sustainability Concepts",
                "Case Studies in Environmental Issues",
                "⭐ AP Prep: Systems Thinking"
            ]},
            2: {"name": "Ecology and Ecosystems", "lessons": [
                "Energy Flow in Ecosystems",
                "Food Chains & Food Webs",
                "Population Dynamics",
                "Community Interactions (Competition, Symbiosis)",
                "Succession (Primary & Secondary)",
                "Biodiversity & Conservation",
                "Case Studies in Ecology",
                "⭐ AP Prep: Population Models"
            ]},
            3: {"name": "Human Population and Demographics", "lessons": [
                "Human Population Growth",
                "Demographic Transition Model",
                "Age Structure Diagrams",
                "Carrying Capacity",
                "Urbanization & Land Use",
                "Case Studies in Population Policy",
                "⭐ AP Prep: Demographic Calculations"
            ]},
            4: {"name": "Natural Resources", "lessons": [
                "Renewable vs. Nonrenewable Resources",
                "Water Resources & Management",
                "Soil & Agriculture",
                "Forests & Deforestation",
                "Fisheries & Ocean Resources",
                "Case Studies in Resource Use",
                "⭐ AP Prep: Resource Management Models"
            ]},
            5: {"name": "Energy Resources", "lessons": [
                "Fossil Fuels (Coal, Oil, Natural Gas)",
                "Nuclear Energy",
                "Renewable Energy (Solar, Wind, Hydro, Geothermal)",
                "Energy Efficiency & Conservation",
                "Case Studies in Energy Policy",
                "⭐ AP Prep: Energy Calculations"
            ]},
            6: {"name": "Pollution and Waste Management", "lessons": [
                "Air Pollution (Sources, Effects, Control)",
                "Water Pollution (Sources, Effects, Control)",
                "Soil Pollution & Land Degradation",
                "Solid Waste Management",
                "Hazardous Waste & Recycling",
                "Case Studies in Pollution Control",
                "⭐ AP Prep: Pollution Models"
            ]},
            7: {"name": "Climate Change and Global Issues", "lessons": [
                "Greenhouse Effect & Global Warming",
                "Evidence of Climate Change",
                "Impacts on Ecosystems & Humans",
                "Mitigation & Adaptation Strategies",
                "International Agreements (Kyoto, Paris)",
                "Case Studies in Climate Policy",
                "⭐ AP Prep: Climate Models"
            ]},
            8: {"name": "Environmental Policy and Ethics", "lessons": [
                "History of Environmental Movements",
                "Environmental Laws & Regulations",
                "International Environmental Policy",
                "Environmental Justice",
                "Case Studies in Policy Implementation",
                "⭐ AP Prep: Policy Analysis"
            ]},
            9: {"name": "Sustainable Development", "lessons": [
                "Principles of Sustainability",
                "Sustainable Agriculture",
                "Sustainable Energy",
                "Green Building & Urban Planning",
                "Case Studies in Sustainable Practices",
                "⭐ AP Prep: Sustainability Metrics"
            ]},
            10: {"name": "AP Prep & Capstone", "lessons": [
                "⭐ Review of Key Environmental Science Concepts",
                "⭐ AP-Style Practice Problems",
                "⭐ Case Studies in AP Environmental Science",
                "Real-World Applications (Policy, Conservation, Engineering)",
                "⭐ Capstone Project: Environmental Impact Study",
                "⭐ Comprehensive Review & AP Exam Prep"
            ]},
        }
    },
    {
        "id": "astronomy",
        "title": "Astronomy",
        "page_title": "High School: Astronomy / Space Science",
        "html_file": "astronomy.html",
        "lessons_folder": "AstronomyLessons",
        "json_slug": "astronomy",
        "course_prefix": "astro",
        "link_id": "astronomy-link",
        "category": "science",
        "color": "#fbbf24",
        "units": {
            1: {"name": "Introduction to Astronomy", "lessons": [
                "History of Astronomy",
                "Tools of Astronomy (Telescopes, Satellites)",
                "Scales of the Universe",
                "Scientific Method in Astronomy",
                "Observational Techniques",
                "Case Studies in Ancient Astronomy",
                "⭐ AP Prep: Measurement & Units"
            ]},
            2: {"name": "Earth, Moon, and Sun System", "lessons": [
                "Earth's Rotation & Revolution",
                "Seasons & Tilt of Axis",
                "Lunar Phases",
                "Solar & Lunar Eclipses",
                "Tides & Gravitational Effects",
                "Case Studies in Earth-Moon-Sun Interactions",
                "⭐ AP Prep: Orbital Calculations"
            ]},
            3: {"name": "The Solar System", "lessons": [
                "Formation of the Solar System",
                "Terrestrial Planets",
                "Gas Giants",
                "Dwarf Planets & Asteroids",
                "Comets & Meteoroids",
                "Planetary Atmospheres",
                "Case Studies in Space Exploration",
                "⭐ AP Prep: Kepler's Laws"
            ]},
            4: {"name": "The Sun", "lessons": [
                "Structure of the Sun",
                "Nuclear Fusion",
                "Solar Activity (Sunspots, Flares, Prominences)",
                "Solar Wind & Magnetic Fields",
                "Impact on Earth's Climate & Technology",
                "Case Studies in Solar Observation",
                "⭐ AP Prep: Energy Calculations"
            ]},
            5: {"name": "Stars and Stellar Evolution", "lessons": [
                "Properties of Stars (Temperature, Luminosity, Size)",
                "⭐ Hertzsprung-Russell Diagram",
                "Star Formation (Nebulae)",
                "Main Sequence Stars",
                "Red Giants & White Dwarfs",
                "Supernovae & Neutron Stars",
                "Black Holes",
                "Case Studies in Stellar Observation"
            ]},
            6: {"name": "Galaxies and the Universe", "lessons": [
                "Types of Galaxies (Spiral, Elliptical, Irregular)",
                "Milky Way Structure",
                "Galaxy Clusters",
                "⭐ Dark Matter & Dark Energy",
                "Expansion of the Universe",
                "Case Studies in Cosmology",
                "⭐ AP Prep: Hubble's Law"
            ]},
            7: {"name": "Space Exploration", "lessons": [
                "History of Space Missions",
                "Satellites & Space Probes",
                "Human Spaceflight",
                "International Space Station",
                "Future of Space Travel (Mars, Beyond)",
                "Case Studies in Space Technology",
                "⭐ AP Prep: Rocket Science Basics"
            ]},
            8: {"name": "Astrobiology", "lessons": [
                "Conditions for Life",
                "Extremophiles on Earth",
                "Search for Extraterrestrial Life",
                "SETI & Radio Astronomy",
                "⭐ Exoplanets & Habitable Zones",
                "Case Studies in Astrobiology",
                "⭐ AP Prep: Probability Models"
            ]},
            9: {"name": "Modern Astronomy Tools", "lessons": [
                "Ground-Based Telescopes",
                "Space Telescopes (Hubble, James Webb)",
                "Radio Astronomy",
                "⭐ Spectroscopy",
                "Computer Modeling in Astronomy",
                "Case Studies in Modern Discoveries",
                "⭐ AP Prep: Data Analysis"
            ]},
            10: {"name": "AP Prep & Capstone", "lessons": [
                "⭐ Review of Key Astronomy Concepts",
                "⭐ AP-Style Practice Problems",
                "⭐ Case Studies in AP Astronomy",
                "Real-World Applications (Satellites, Navigation, Climate Science)",
                "⭐ Capstone Project: Space Science Research",
                "⭐ Comprehensive Review & AP Exam Prep"
            ]},
        }
    },
    {
        "id": "anatomy",
        "title": "Human Anatomy & Physiology",
        "page_title": "High School: Human Anatomy & Physiology",
        "html_file": "anatomy.html",
        "lessons_folder": "AnatomyLessons",
        "json_slug": "anatomy",
        "course_prefix": "anat",
        "link_id": "anatomy-link",
        "category": "science",
        "color": "#22c55e",
        "units": {
            1: {"name": "Introduction to Anatomy & Physiology", "lessons": [
                "Levels of Organization (Cells → Tissues → Organs → Systems)",
                "Anatomical Terminology (Planes, Directions, Cavities)",
                "⭐ Homeostasis & Feedback Mechanisms",
                "Basic Histology (Tissue Types)",
                "Medical Imaging Techniques",
                "Case Studies in Homeostasis",
                "⭐ AP Prep: Anatomical Terminology"
            ]},
            2: {"name": "The Skeletal System", "lessons": [
                "Bone Structure & Function",
                "Types of Bones (Long, Short, Flat, Irregular)",
                "Axial Skeleton",
                "Appendicular Skeleton",
                "Joints & Movement",
                "Bone Growth & Remodeling",
                "Disorders of the Skeletal System",
                "⭐ AP Prep: Bone Identification"
            ]},
            3: {"name": "The Muscular System", "lessons": [
                "Muscle Tissue Types (Skeletal, Cardiac, Smooth)",
                "Muscle Anatomy & Physiology",
                "⭐ Sliding Filament Theory",
                "Muscle Contraction & Energy Use",
                "Major Muscle Groups",
                "Disorders of the Muscular System",
                "Case Studies in Sports Medicine",
                "⭐ AP Prep: Muscle Physiology"
            ]},
            4: {"name": "The Nervous System", "lessons": [
                "Neurons & Neuroglia",
                "⭐ Action Potentials & Synaptic Transmission",
                "Central Nervous System (Brain & Spinal Cord)",
                "Peripheral Nervous System",
                "Autonomic Nervous System",
                "Reflex Arcs",
                "Disorders of the Nervous System",
                "⭐ AP Prep: Neurophysiology"
            ]},
            5: {"name": "The Endocrine System", "lessons": [
                "Hormones & Chemical Signaling",
                "Major Endocrine Glands",
                "⭐ Hormonal Regulation of Homeostasis",
                "Feedback Loops in Endocrine Control",
                "Disorders of the Endocrine System",
                "Case Studies in Endocrinology",
                "⭐ AP Prep: Hormone Pathways"
            ]},
            6: {"name": "The Circulatory System", "lessons": [
                "Structure of the Heart",
                "Blood Vessels & Circulation",
                "Blood Composition & Function",
                "⭐ Cardiac Cycle & Heartbeat Regulation",
                "Blood Pressure & Homeostasis",
                "Disorders of the Circulatory System",
                "Case Studies in Cardiovascular Health",
                "⭐ AP Prep: ECG Interpretation"
            ]},
            7: {"name": "The Respiratory System", "lessons": [
                "Anatomy of the Respiratory System",
                "Mechanics of Breathing",
                "⭐ Gas Exchange in Alveoli",
                "Transport of Oxygen & Carbon Dioxide",
                "Regulation of Breathing",
                "Disorders of the Respiratory System",
                "Case Studies in Pulmonology",
                "⭐ AP Prep: Respiratory Physiology"
            ]},
            8: {"name": "The Digestive System", "lessons": [
                "Anatomy of Digestive Organs",
                "Mechanical & Chemical Digestion",
                "Absorption of Nutrients",
                "Accessory Organs (Liver, Pancreas, Gallbladder)",
                "Disorders of the Digestive System",
                "Case Studies in Nutrition",
                "⭐ AP Prep: Digestive Physiology"
            ]},
            9: {"name": "The Urinary & Reproductive Systems", "lessons": [
                "Anatomy of the Urinary System",
                "⭐ Kidney Function & Filtration",
                "Fluid & Electrolyte Balance",
                "Male Reproductive System",
                "Female Reproductive System",
                "Hormonal Regulation of Reproduction",
                "Disorders of Urinary & Reproductive Systems",
                "⭐ AP Prep: Renal Physiology"
            ]},
            10: {"name": "Integration & AP Prep", "lessons": [
                "Immune System Overview",
                "Interactions Between Organ Systems",
                "Case Studies in Pathophysiology",
                "⭐ Review of Key Anatomy & Physiology Concepts",
                "⭐ AP-Style Practice Problems",
                "⭐ Capstone Project: Human Body Systems Integration",
                "⭐ Comprehensive Review & AP Exam Prep"
            ]},
        }
    },
    {
        "id": "marine_science",
        "title": "Marine Science",
        "page_title": "High School: Marine Science / Biology",
        "html_file": "marine_science.html",
        "lessons_folder": "MarineScienceLessons",
        "json_slug": "marine_science",
        "course_prefix": "marine",
        "link_id": "marine-link",
        "category": "science",
        "color": "#22c55e",
        "units": {
            1: {"name": "Introduction to Marine Science", "lessons": [
                "What is Marine Science?",
                "History of Ocean Exploration",
                "Tools of Marine Science (Submersibles, Sonar, Satellites)",
                "Oceanographic Disciplines (Biology, Chemistry, Geology, Physics)",
                "Careers in Marine Science",
                "Case Studies in Ocean Research",
                "⭐ AP Prep: Scientific Method in Marine Biology"
            ]},
            2: {"name": "Physical Oceanography", "lessons": [
                "Properties of Seawater (Salinity, Density, Temperature)",
                "Ocean Currents (Surface, Deep, Thermohaline)",
                "Waves & Tides",
                "Coastal Processes (Erosion, Deposition)",
                "Ocean-Atmosphere Interactions",
                "Case Studies in Climate-Ocean Systems",
                "⭐ AP Prep: Ocean Circulation Models"
            ]},
            3: {"name": "Marine Geology", "lessons": [
                "Structure of the Ocean Floor",
                "Plate Tectonics & Seafloor Spreading",
                "Mid-Ocean Ridges & Trenches",
                "Marine Sediments",
                "Hydrothermal Vents",
                "Case Studies in Marine Geology",
                "⭐ AP Prep: Plate Tectonics Calculations"
            ]},
            4: {"name": "Marine Chemistry", "lessons": [
                "Chemical Composition of Seawater",
                "Gas Exchange (Oxygen, Carbon Dioxide)",
                "⭐ Ocean Acidification",
                "Nutrient Cycles (Nitrogen, Phosphorus)",
                "Case Studies in Marine Chemistry",
                "⭐ AP Prep: Chemical Equilibria in Oceans"
            ]},
            5: {"name": "Marine Ecology", "lessons": [
                "Marine Ecosystems (Estuaries, Coral Reefs, Open Ocean, Deep Sea)",
                "Food Chains & Food Webs",
                "Energy Flow in Marine Systems",
                "Symbiotic Relationships",
                "Biodiversity & Conservation",
                "Case Studies in Marine Ecology",
                "⭐ AP Prep: Population Models"
            ]},
            6: {"name": "Marine Invertebrates", "lessons": [
                "Sponges & Cnidarians",
                "Mollusks (Clams, Squid, Octopus)",
                "Crustaceans (Crabs, Lobsters, Shrimp)",
                "Echinoderms (Starfish, Sea Urchins)",
                "Case Studies in Invertebrate Biology",
                "⭐ AP Prep: Comparative Anatomy"
            ]},
            7: {"name": "Marine Vertebrates", "lessons": [
                "Fish (Cartilaginous vs. Bony)",
                "Amphibians (Limited Marine Species)",
                "Marine Reptiles (Sea Turtles, Sea Snakes)",
                "Marine Birds (Penguins, Albatross)",
                "Marine Mammals (Whales, Dolphins, Seals)",
                "Case Studies in Vertebrate Biology",
                "⭐ AP Prep: Evolutionary Adaptations"
            ]},
            8: {"name": "Human Impact on Oceans", "lessons": [
                "Overfishing & Fisheries Management",
                "Pollution (Plastic, Oil Spills, Chemical Runoff)",
                "⭐ Climate Change & Coral Bleaching",
                "Marine Protected Areas",
                "Case Studies in Conservation Policy",
                "⭐ AP Prep: Environmental Models"
            ]},
            9: {"name": "Marine Technology and Exploration", "lessons": [
                "Submersibles & ROVs",
                "Satellites & Remote Sensing",
                "Deep-Sea Exploration",
                "Marine Biotechnology",
                "Case Studies in Ocean Technology",
                "⭐ AP Prep: Data Analysis in Marine Science"
            ]},
            10: {"name": "AP Prep & Capstone", "lessons": [
                "⭐ Review of Key Marine Science Concepts",
                "⭐ AP-Style Practice Problems",
                "⭐ Case Studies in AP Marine Biology",
                "Real-World Applications (Conservation, Fisheries, Climate Science)",
                "⭐ Capstone Project: Marine Ecosystem Study",
                "⭐ Comprehensive Review & AP Exam Prep"
            ]},
        }
    },
    {
        "id": "integrated_science",
        "title": "Integrated Science",
        "page_title": "High School: Integrated Science",
        "html_file": "integrated_science.html",
        "lessons_folder": "IntegratedScienceLessons",
        "json_slug": "integrated_science",
        "course_prefix": "intsci",
        "link_id": "intsci-link",
        "category": "science",
        "color": "#3b82f6",
        "units": {
            1: {"name": "Earth's Structure and Composition", "lessons": [
                "Layers of the Earth (Crust, Mantle, Core)",
                "Minerals (Classification, Identification Tests)",
                "Rock Cycle (Igneous, Sedimentary, Metamorphic)",
                "Plate Tectonics (Continental Drift, Seafloor Spreading)",
                "Earthquakes (Seismic Waves, Measurement, Prediction)",
                "Volcanoes (Types, Eruptions, Hazards)",
                "Mountain Building & Geological Structures",
                "Geological Resources (Ores, Fossil Fuels)",
                "Case Studies in Natural Hazards"
            ]},
            2: {"name": "Atmosphere and Weather", "lessons": [
                "Composition & Layers of the Atmosphere",
                "Energy Transfer (Radiation, Conduction, Convection)",
                "Weather Systems (Fronts, Pressure Systems)",
                "Clouds & Precipitation Types",
                "Climate Zones & Global Circulation",
                "Severe Weather (Hurricanes, Tornadoes, Blizzards)",
                "Human Impact on Atmosphere (Pollution, Greenhouse Gases)",
                "⭐ Weather Prediction Models",
                "Case Studies in Climate Events"
            ]},
            3: {"name": "Hydrosphere and Water Systems", "lessons": [
                "Hydrologic Cycle (Evaporation, Condensation, Precipitation)",
                "Oceans (Currents, Salinity, Temperature Layers)",
                "Waves & Tides (Causes, Effects)",
                "Freshwater Systems (Rivers, Lakes, Aquifers)",
                "Glaciers & Ice Caps (Formation, Melting Impacts)",
                "Water Resources & Human Use",
                "Water Pollution & Conservation",
                "Case Studies in Hydrology",
                "⭐ AP Prep: Ocean Circulation Models"
            ]},
            4: {"name": "Earth's History and Geologic Time", "lessons": [
                "Fossils & Fossil Formation",
                "Relative Dating (Stratigraphy, Index Fossils)",
                "⭐ Radiometric Dating & Half-Life",
                "Geologic Time Scale (Eras, Periods, Epochs)",
                "Mass Extinctions & Evolutionary Events",
                "Origin of Earth & Early Atmosphere",
                "Plate Movements Through Time (Supercontinents)",
                "Case Studies in Paleontology",
                "⭐ AP Prep: Geologic Time Calculations"
            ]},
            5: {"name": "Natural Resources and Energy", "lessons": [
                "Renewable Resources (Solar, Wind, Hydro)",
                "Nonrenewable Resources (Coal, Oil, Natural Gas)",
                "Nuclear Energy (Fission, Fusion Potential)",
                "Resource Extraction Methods (Mining, Drilling)",
                "Environmental Impacts of Resource Use",
                "Sustainability & Conservation Strategies",
                "Case Studies in Energy Policy",
                "⭐ AP Prep: Energy Calculations"
            ]},
            6: {"name": "Human Impact on Earth Systems", "lessons": [
                "Deforestation & Land Use Changes",
                "Urbanization & Soil Degradation",
                "Pollution (Air, Water, Soil)",
                "⭐ Climate Change & Global Warming",
                "Conservation & Restoration Strategies",
                "Future Challenges (Population Growth, Resource Scarcity)",
                "Case Studies in Environmental Policy",
                "⭐ AP Prep: Climate Models"
            ]},
            7: {"name": "Integrated Science Connections", "lessons": [
                "Earth Science & Biology (Ecosystems, Biogeochemical Cycles)",
                "Earth Science & Chemistry (Atmospheric Composition, Reactions)",
                "Earth Science & Physics (Energy Transfer, Waves, Forces)",
                "Earth Science & Technology (Satellites, Climate Modeling)",
                "Careers in Earth & Environmental Sciences",
                "Case Studies in Interdisciplinary Science",
                "⭐ AP Prep: Cross-Disciplinary Applications"
            ]},
            8: {"name": "Astronomy Connections", "lessons": [
                "Earth's Place in the Universe",
                "Seasons & Earth's Tilt",
                "Lunar Phases & Eclipses",
                "Solar Energy & Earth Systems",
                "Gravity & Orbital Motion",
                "Case Studies in Space-Earth Interactions",
                "⭐ AP Prep: Orbital Calculations"
            ]},
            9: {"name": "Earth Systems Modeling", "lessons": [
                "Systems Thinking in Earth Science",
                "Feedback Loops (Positive & Negative)",
                "Modeling Climate Systems",
                "Modeling Geological Processes",
                "Case Studies in Predictive Modeling",
                "⭐ AP Prep: Earth System Simulations",
                "Applications in Environmental Engineering"
            ]},
            10: {"name": "AP Prep & Capstone", "lessons": [
                "⭐ Review of Key Earth Science Concepts",
                "⭐ AP-Style Practice Problems",
                "⭐ Case Studies in AP Earth Science",
                "Real-World Applications (Policy, Conservation, Engineering)",
                "⭐ Capstone Project: Earth Systems Analysis",
                "⭐ Comprehensive Review & AP Exam Prep"
            ]},
        }
    },
]


# ─── Content generators ───────────────────────────────────────────────

def strip_star(title):
    """Remove leading ⭐ prefix from lesson titles for use in content."""
    return title.lstrip('⭐ ').strip()


def make_summary_html(lesson_title):
    """Generate a placeholder summary HTML for a lesson."""
    lesson_title = strip_star(lesson_title)
    safe = html.escape(lesson_title)
    return f'<h3>Key Concepts: {safe}</h3>\n<p>Content for <b>{safe}</b> is coming soon. Check back for detailed notes and key concepts.</p>'


def make_quiz_questions(lesson_title, n=20):
    """Generate placeholder quiz questions."""
    lesson_title = strip_star(lesson_title)
    questions = []
    for i in range(1, n + 1):
        questions.append({
            "question_number": i,
            "question_text": f"Sample question {i} for {lesson_title}",
            "attempted": 2,
            "data_i18n": None,
            "options": [
                {"text": "Option A (correct)", "is_correct": True, "data_i18n": None},
                {"text": "Option B", "is_correct": False, "data_i18n": None},
                {"text": "Option C", "is_correct": False, "data_i18n": None},
                {"text": "Option D", "is_correct": False, "data_i18n": None},
            ],
            "explanation": f"This is a placeholder explanation for question {i} of {lesson_title}."
        })
    return questions


def make_flashcards(lesson_title, n=5):
    """Generate placeholder flashcards."""
    lesson_title = strip_star(lesson_title)
    cards = []
    for i in range(1, n + 1):
        cards.append({
            "term": f"Term {i} for {lesson_title}",
            "definition": f"Definition {i} for {lesson_title} — placeholder content."
        })
    return cards


def generate_json(course):
    """Generate the lesson JSON file for a course."""
    data = {}
    for unit_num, unit_info in course["units"].items():
        for idx, lesson_title_raw in enumerate(unit_info["lessons"], 1):
            lesson_title = strip_star(lesson_title_raw)
            lesson_number = f"{unit_num}.{idx}"
            key = f"u{unit_num}_l{lesson_number}"
            data[key] = {
                "unit": unit_num,
                "lesson_number": lesson_number,
                "title": lesson_title,
                "course": course["title"],
                "summary_sections": [
                    {
                        "title": f"Key Concepts: {lesson_title}",
                        "content_html": make_summary_html(lesson_title),
                        "data_i18n": None
                    }
                ],
                "flashcards": make_flashcards(lesson_title),
                "quiz_questions": make_quiz_questions(lesson_title)
            }
    return data


# ─── HTML Templates ───────────────────────────────────────────────────

def video_html(unit_num, lesson_num, lesson_title, course):
    lesson_title = strip_star(lesson_title)
    folder = course["lessons_folder"]
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Lesson {unit_num}.{lesson_num}: {html.escape(lesson_title)}</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../../scripts/global_translations.js?v=7.4"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.4"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.4"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
    <script src="../../../theme_manager.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{ window.applyTranslations(); }}, 50);
            }}
        }});
    </script>
</head>
<body class="dark-mode h-full">
<script src="../../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="lesson-content-view">
    <h2 class="page-title">Lesson {unit_num}.{lesson_num}: {html.escape(lesson_title)}</h2>
    <div class="courses-container">
        <div class="lesson-layout">
            <div class="video-stack">
                <div class="video-embed">
                    <div style="display:flex;align-items:center;justify-content:center;height:100%;min-height:20rem;background:rgba(0,0,0,0.05);border-radius:1rem;">
                        <p style="color:#94a3b8;font-size:1.25rem;font-weight:600;">Video coming soon</p>
                    </div>
                </div>
            </div>
            <div class="side-buttons">
                <a class="side-button" href="Lesson {unit_num}.{lesson_num}_Summary.html">Next Up: Summary</a>
            </div>
        </div>
    </div>
</div>
</main>
<script src="../../../scripts/lesson_video.js"></script>
<script src="../../../../search_data.js"></script>
<script src="../../../../search_logic.js"></script>
<script src="../../../scripts/inject_games.js"></script>
<script src="../../../scripts/climb_game.js"></script>
<script src="../../../scripts/game_switcher.js"></script>
</body>
</html>'''


def summary_html(unit_num, lesson_num, lesson_title, course):
    lesson_title = strip_star(lesson_title)
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Lesson {unit_num}.{lesson_num}: {html.escape(lesson_title)} - Summary</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../../scripts/global_translations.js?v=7.4"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.4"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.4"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
    <script src="../../../theme_manager.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{ window.applyTranslations(); }}, 50);
            }}
        }});
    </script>
</head>
<body class="dark-mode h-full">
<script src="../../../scripts/taskbar.js"></script>
<main class="main-container">
<div id="summary-content-view">
    <h2 class="page-title">Lesson {unit_num}.{lesson_num}: {html.escape(lesson_title)} - Summary</h2>
    <div class="diagram-card">
        <div class="lesson-notes">
            <h3>Key Concepts: {html.escape(lesson_title)}</h3>
            <p>Detailed summary content for <b>{html.escape(lesson_title)}</b> is coming soon.</p>
            <p>Check back for comprehensive notes and key concepts.</p>
        </div>
        <div class="summary-actions">
            <a class="side-button" href="Lesson {unit_num}.{lesson_num}_Practice.html" style="text-align:center; text-decoration:none; display:block;">Next Up: Play</a>
        </div>
    </div>
</div>
</main>
<script src="../../../../search_data.js"></script>
<script src="../../../../search_logic.js"></script>
<script src="/ArisEdu Project Folder/scripts/game_utils.js"></script>
</body>
</html>'''


def quiz_html(unit_num, lesson_num, lesson_title, page_type="Quiz"):
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Lesson {unit_num}.{lesson_num}_{page_type}</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="/ArisEdu Project Folder/scripts/global_translations.js?v=7.4"></script>
    <script src="/ArisEdu Project Folder/scripts/spanish_translations.js?v=1.4"></script>
    <script src="/ArisEdu Project Folder/scripts/hindi_translations.js?v=1.4"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
    <link href="/styles/unit_test.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
    <script src="/ArisEdu Project Folder/theme_manager.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{ window.applyTranslations(); }}, 50);
            }}
        }});
    </script>
</head>
<body class="dark-mode h-full">
    <script src="/ArisEdu Project Folder/scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="quiz-content-view">
            <div style="text-align: center; padding: 2rem;">
                <p>Loading quiz...</p>
            </div>
        </div>
    </main>
    <script src="/search_data.js"></script>
    <script src="/search_logic.js"></script>
    <script src="/ArisEdu Project Folder/scripts/analytics-helper.js"></script>
    <script src="/scripts/quiz_loader.js"></script>
</body>
</html>'''


def practice_html(unit_num, lesson_num, lesson_title, course):
    lesson_title = strip_star(lesson_title)
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Lesson {unit_num}.{lesson_num}: {html.escape(lesson_title)} - Practice</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="../../../scripts/global_translations.js?v=7.4"></script>
    <script src="../../../scripts/spanish_translations.js?v=1.4"></script>
    <script src="../../../scripts/hindi_translations.js?v=1.4"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
    <link href="/styles/unit_test.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
    <script src="/ArisEdu Project Folder/theme_manager.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            if (window.applyTranslations) {{
                setTimeout(function() {{ window.applyTranslations(); }}, 50);
            }}
        }});
    </script>
</head>
<body class="dark-mode h-full">
    <script src="/ArisEdu Project Folder/scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="quiz-content-view">
            <div style="text-align: center; padding: 2rem;">
                <p>Loading practice...</p>
            </div>
        </div>
    </main>
    <script src="/search_data.js"></script>
    <script src="/search_logic.js"></script>
    <script src="/scripts/quiz_loader.js"></script>
</body>
</html>'''


def unit_test_html(unit_num, course):
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Unit {unit_num} Test</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="/ArisEdu Project Folder/scripts/global_translations.js?v=7.4"></script>
    <script src="/ArisEdu Project Folder/scripts/spanish_translations.js?v=1.4"></script>
    <script src="/ArisEdu Project Folder/scripts/hindi_translations.js?v=1.4"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
    <link href="/styles/unit_test.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
    <script src="/ArisEdu Project Folder/theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
    <script src="/ArisEdu Project Folder/scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="unit-test-view">
            <h2 class="page-title">Unit {unit_num} Test — {html.escape(course["title"])}</h2>
            <div class="diagram-card" style="text-align:center;padding:3rem;">
                <p style="font-size:1.25rem;color:#94a3b8;">Unit test coming soon.</p>
            </div>
        </div>
    </main>
    <script src="/search_data.js"></script>
    <script src="/search_logic.js"></script>
    <script src="/scripts/unit_test_loader.js"></script>
</body>
</html>'''


def unit_test_practice_html(unit_num, course):
    return f'''<!DOCTYPE html>
<html class="h-full" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Unit {unit_num} Test Practice</title>
    <script src="/_sdk/element_sdk.js"></script>
    <script src="/ArisEdu Project Folder/scripts/global_translations.js?v=7.4"></script>
    <script src="/ArisEdu Project Folder/scripts/spanish_translations.js?v=1.4"></script>
    <script src="/ArisEdu Project Folder/scripts/hindi_translations.js?v=1.4"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="/ArisEdu Project Folder/styles/main.css" rel="stylesheet"/>
    <link href="/styles/unit_test.css" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&amp;display=swap" rel="stylesheet"/>
    <script src="/ArisEdu Project Folder/theme_manager.js"></script>
</head>
<body class="dark-mode h-full">
    <script src="/ArisEdu Project Folder/scripts/taskbar.js"></script>
    <main class="main-container">
        <div id="unit-test-view">
            <h2 class="page-title">Unit {unit_num} Test Practice — {html.escape(course["title"])}</h2>
            <div class="diagram-card" style="text-align:center;padding:3rem;">
                <p style="font-size:1.25rem;color:#94a3b8;">Test practice coming soon.</p>
            </div>
        </div>
    </main>
    <script src="/search_data.js"></script>
    <script src="/search_logic.js"></script>
    <script src="/scripts/unit_test_loader.js"></script>
</body>
</html>'''


# ─── Course page (dynamic grid like ms_physics.html) ─────────────────

def course_page_html(course):
    prefix = course["course_prefix"]
    title = course["page_title"]
    folder = course["lessons_folder"]
    color = course["color"]

    # Build unit config
    units_js = "{\n"
    for unit_num, unit_info in sorted(course["units"].items()):
        count = len(unit_info["lessons"])
        units_js += f"      {unit_num}: {count},\n"
    units_js += "    }"

    num_units = len(course["units"])

    # Build lesson mappings JS
    lesson_mappings_js = "{\n"
    for unit_num, unit_info in sorted(course["units"].items()):
        lesson_mappings_js += f"      {unit_num}: ["
        entries = []
        for idx, name in enumerate(unit_info["lessons"], 1):
            safe_name = name.replace("'", "\\'").replace('"', '\\"')
            entries.append(f"{{num: {idx}, name: '{safe_name}'}}")
        lesson_mappings_js += ", ".join(entries)
        lesson_mappings_js += "],\n"
    lesson_mappings_js += "    }"

    return f'''<!doctype html>
<html lang="en" class="h-full">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <script src="/_sdk/element_sdk.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/ArisEdu Project Folder/styles/main.css">
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
  <script src="../theme_manager.js"></script>
  <script charset="UTF-8" src="../scripts/global_translations.js?v=7.4"></script>
  <script src="../scripts/spanish_translations.js?v=1.4"></script>
  <script src="../scripts/hindi_translations.js?v=1.4"></script>
</head>
 <body class="dark-mode h-full">
<script src="../scripts/taskbar.js"></script>
  <main class="main-container">
    <div class="logo-title-wrapper" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;">
      <h1 id="company-name" class="logo-font page-title" style="font-size: 3rem; margin-bottom: 0;">{html.escape(title)}</h1>
    </div>
    <div class="courses-container">
      <div style="position: relative; transform: translateY(0); display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; padding: 1rem; min-height: 60rem;" id="grid-container"></div>
    </div>
  </main>

  <style>
    #lesson-tooltip {{
        position: fixed;
        background: rgba(15, 23, 42, 0.95);
        backdrop-filter: blur(12px);
        color: #f1f5f9;
        padding: 0.75rem 1.25rem;
        border-radius: 0.75rem;
        font-size: 0.95rem;
        font-weight: 600;
        pointer-events: none;
        z-index: 10000;
        opacity: 0;
        transition: opacity 0.15s ease;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
        white-space: nowrap;
        display: none;
    }}
    #lesson-tooltip[data-visible="true"] {{
        opacity: 1;
        display: block;
    }}

    rect[id^="u"], path[id^="u"] {{
        transform-box: fill-box;
        transform-origin: center;
        transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), filter 0.2s ease, stroke-width 0.2s ease;
    }}
    .segment-hover {{
        transform: scale(1.05);
        filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.9));
        fill-opacity: 0.15;
    }}

    @keyframes star-pulse {{
      0%, 100% {{ stroke-opacity: 0.8; stroke-width: 0.12; filter: drop-shadow(0 0 2px {color}); }}
      50% {{ stroke-opacity: 1; stroke-width: 0.25; filter: drop-shadow(0 0 6px {color}); }}
    }}
    .starred-lesson-glow {{
      stroke: {color} !important;
      stroke-dasharray: 0.3, 0.1;
      animation: star-pulse 1.5s infinite ease-in-out;
    }}
    @keyframes star-twinkle {{
        0%, 100% {{ opacity: 0.4; transform: scale(0.8); }}
        50% {{ opacity: 1; transform: scale(1.3); }}
    }}
    .star-icon {{
        animation: star-twinkle 2s infinite ease-in-out;
        font-family: inherit;
        pointer-events: none;
        transform-box: fill-box;
        transform-origin: center;
        font-size: 0.6px;
        user-select: none;
    }}
  </style>

  <div id="lesson-tooltip"></div>

  <script>
  const courseConfig = {{
    units: {units_js},
    numUnits: {num_units},
    coursePrefix: '{prefix}'
  }};

  const lessonMappings = {lesson_mappings_js};

  function generateUnitSVG(unitNum, lessonCount) {{
    let segments = '';
    const lessons = lessonMappings[unitNum] || [];
    const totalSpace = 30;
    const rectHeight = (totalSpace / lessons.length).toFixed(3);

    for (let i = 0; i < lessons.length; i++) {{
      const lesson = lessons[i];
      const yPos = (3 + totalSpace - ((i + 1) * rectHeight)).toFixed(3);
      segments += '<a href="../CourseFiles/{folder}/Unit' + unitNum + '/Lesson ' + unitNum + '.' + lesson.num + '_Video.html" onclick="markLessonStarted(\\'' + unitNum + '\\', ' + (i+1) + ')">\\n' +
        '    <rect id="u' + unitNum + '-l' + (i+1) + '" stroke="none" x="3" y="' + yPos + '" width="18" height="' + rectHeight + '" fill="white" fill-opacity="0" cursor="pointer" pointer-events="auto" onmouseenter="showLessonPopup(event, \\'Lesson ' + unitNum + '.' + lesson.num + ': ' + lesson.name.replace(/'/g, "\\\\'") + '\\')" onmousemove="moveLessonPopup(event)" onmouseleave="hideLessonPopup()"></rect>\\n' +
        '</a>\\n' +
        '  <line x1="3" y1="' + yPos + '" x2="21" y2="' + yPos + '" stroke="currentColor" stroke-width="0.08" stroke-opacity="0.3" pointer-events="none" />\\n';
    }}

    return '<div style="position: relative; display: flex; align-items: flex-start; justify-content: center; height: 100%;"><svg viewBox="0 0 24 38" fill="none" stroke="currentColor" stroke-width="0.4" stroke-linecap="round" stroke-linejoin="round" style="width: 100%; height: 100%; max-height: 45rem; color: inherit;"><rect x="3" y="3" width="18" height="30" rx="1.5" ry="1.5" fill="none" stroke="currentColor" stroke-width="0.5" /><rect id="fill-unit-' + unitNum + '" x="3" y="3" width="18" height="30" rx="1.5" ry="1.5" fill="#9ca3af" fill-opacity="0.15" stroke="none" /><g id="segments-unit-' + unitNum + '">\\n' + segments + '</g><text x="12" y="36" text-anchor="middle" fill="currentColor" stroke="none" font-size="1.8" font-family="ui-sans-serif, system-ui, sans-serif" font-weight="600" style="pointer-events: none;">Unit ' + unitNum + '</text></svg></div>';
  }}

  function populateGrid() {{
    const container = document.getElementById('grid-container');
    container.innerHTML = '';
    for (const [unitNum, lessonCount] of Object.entries(courseConfig.units)) {{
      container.innerHTML += generateUnitSVG(parseInt(unitNum), lessonCount);
    }}
  }}

  function markLessonStarted(unit, lesson) {{
    const startedKey = courseConfig.coursePrefix + '_u' + unit + '_l' + lesson + '_started';
    const completedKey = courseConfig.coursePrefix + '_u' + unit + '_l' + lesson + '_completed';
    if (localStorage.getItem(completedKey) !== 'true') {{
      localStorage.setItem(startedKey, 'true');
    }}
  }}

  function applyProgressColors() {{
    for (let u = 1; u <= courseConfig.numUnits; u++) {{
      const lessonCount = courseConfig.units[u] || 0;
      for (let l = 1; l <= lessonCount; l++) {{
        const element = document.getElementById('u' + u + '-l' + l);
        if(element) {{
          const completed = localStorage.getItem(courseConfig.coursePrefix + '_u' + u + '_l' + l + '_completed') === 'true';
          const started = localStorage.getItem(courseConfig.coursePrefix + '_u' + u + '_l' + l + '_started') === 'true';
          if (completed) {{
            element.setAttribute('fill', '#16a34a');
            element.setAttribute('fill-opacity', '0.7');
          }} else if (started) {{
            element.setAttribute('fill', '#f97316');
            element.setAttribute('fill-opacity', '0.6');
          }}
        }}
      }}
    }}
  }}

  let tooltipEl = null;
  function getOrCreateTooltip() {{
    if (!tooltipEl) {{
      tooltipEl = document.createElement('div');
      tooltipEl.id = 'lesson-tooltip';
      document.body.appendChild(tooltipEl);
    }}
    return tooltipEl;
  }}
  function showLessonPopup(event, title) {{
    const tooltip = getOrCreateTooltip();
    const target = event.target;
    if (target && target.id && target.id.match(/^u\\d+-l\\d+$/)) {{
      target.classList.add('segment-hover');
    }}
    let status = '';
    const match = target.id ? target.id.match(/u(\\d+)-l(\\d+)/) : null;
    if (match) {{
      const u = match[1], l = match[2];
      const isCompleted = localStorage.getItem(courseConfig.coursePrefix + '_u' + u + '_l' + l + '_completed') === 'true';
      const isStarted = localStorage.getItem(courseConfig.coursePrefix + '_u' + u + '_l' + l + '_started') === 'true';
      if (isCompleted) status = 'COMPLETED \\u2714 ';
      else if (isStarted) status = 'IN PROGRESS ';
    }}
    tooltip.textContent = status + title;
    tooltip.setAttribute('data-visible', 'true');
  }}
  function moveLessonPopup(e) {{
    const tooltip = getOrCreateTooltip();
    if (tooltip.getAttribute('data-visible') !== 'true') return;
    const offset = 15;
    let x = e.clientX + offset, y = e.clientY + offset;
    const rect = tooltip.getBoundingClientRect();
    if (x + rect.width > window.innerWidth) x = e.clientX - rect.width - offset;
    if (y + rect.height > window.innerHeight) y = e.clientY - rect.height - offset;
    tooltip.style.left = x + 'px';
    tooltip.style.top = y + 'px';
  }}
  function hideLessonPopup() {{
    const tooltip = getOrCreateTooltip();
    tooltip.setAttribute('data-visible', 'false');
    document.querySelectorAll('.segment-hover').forEach(function(el) {{ el.classList.remove('segment-hover'); }});
  }}

  document.addEventListener('DOMContentLoaded', function() {{
    populateGrid();
    applyProgressColors();
  }});

  window.addEventListener('storage', function(e) {{
    if (e.key && e.key.indexOf(courseConfig.coursePrefix + '_u') === 0) {{
      applyProgressColors();
    }}
  }});
  </script>

  <script src="../../search_data.js"></script>
  <script src="../../search_logic.js"></script>
  <script src="../scripts/dev_tools.js"></script>
</body>
</html>
'''


# ─── Main ─────────────────────────────────────────────────────────────

def main():
    os.makedirs(COURSE_HOMEPAGE, exist_ok=True)
    total_files = 0

    for course in COURSES:
        print(f"\n{'='*60}")
        print(f"Generating: {course['title']}")
        print(f"{'='*60}")

        # 1. Create JSON content data
        json_path = os.path.join(CONTENT_DATA, f"{course['json_slug']}_lessons.json")
        json_data = generate_json(course)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        print(f"  Created JSON: {json_path}")
        total_files += 1

        # 2. Create lesson folders and files
        for unit_num, unit_info in sorted(course["units"].items()):
            unit_dir = os.path.join(COURSE_FILES, course["lessons_folder"], f"Unit{unit_num}")
            os.makedirs(unit_dir, exist_ok=True)

            for idx, lesson_title in enumerate(unit_info["lessons"], 1):
                # Video
                vpath = os.path.join(unit_dir, f"Lesson {unit_num}.{idx}_Video.html")
                with open(vpath, "w", encoding="utf-8") as f:
                    f.write(video_html(unit_num, idx, lesson_title, course))
                total_files += 1

                # Summary
                spath = os.path.join(unit_dir, f"Lesson {unit_num}.{idx}_Summary.html")
                with open(spath, "w", encoding="utf-8") as f:
                    f.write(summary_html(unit_num, idx, lesson_title, course))
                total_files += 1

                # Quiz
                qpath = os.path.join(unit_dir, f"Lesson {unit_num}.{idx}_Quiz.html")
                with open(qpath, "w", encoding="utf-8") as f:
                    f.write(quiz_html(unit_num, idx, lesson_title))
                total_files += 1

                # Practice
                ppath = os.path.join(unit_dir, f"Lesson {unit_num}.{idx}_Practice.html")
                with open(ppath, "w", encoding="utf-8") as f:
                    f.write(practice_html(unit_num, idx, lesson_title, course))
                total_files += 1

            # Unit Test
            tpath = os.path.join(unit_dir, "Unit{}_Test.html".format(unit_num))
            with open(tpath, "w", encoding="utf-8") as f:
                f.write(unit_test_html(unit_num, course))
            total_files += 1

            # Unit Test Practice
            tppath = os.path.join(unit_dir, "Unit{}_Test_Practice.html".format(unit_num))
            with open(tppath, "w", encoding="utf-8") as f:
                f.write(unit_test_practice_html(unit_num, course))
            total_files += 1

            print(f"  Unit {unit_num}: {len(unit_info['lessons'])} lessons + 2 tests")

        # 3. Create course page HTML
        course_html_path = os.path.join(COURSE_HOMEPAGE, course["html_file"])
        with open(course_html_path, "w", encoding="utf-8") as f:
            f.write(course_page_html(course))
        print(f"  Created course page: {course_html_path}")
        total_files += 1

    print(f"\n{'='*60}")
    print(f"DONE! Created {total_files} files across {len(COURSES)} courses.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
