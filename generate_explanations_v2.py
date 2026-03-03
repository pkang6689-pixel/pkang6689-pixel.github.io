"""
Improved Explanation Generator v2
Generates high-quality, content-aware explanations for quiz questions.

Strategy:
1. Extract plain text from each lesson's summary_sections
2. Find relevant sentences from lesson content that explain the correct answer
3. Reference wrong answer choices and explain why they're incorrect
4. For math: attempt to show calculation steps
5. Fallback: generate educational explanation using question+answer analysis
"""

import json
import os
import re
import string
from collections import Counter

# ─── Configuration ───────────────────────────────────────────────────────────

CONTENT_DIR = "content_data"
AP_DIR = "content_data/AP_Courses"

# Common stopwords to ignore when matching
STOPWORDS = {
    'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
    'should', 'may', 'might', 'shall', 'can', 'need', 'dare', 'ought',
    'used', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from',
    'as', 'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'between', 'out', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'both',
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just',
    'because', 'but', 'and', 'or', 'if', 'while', 'that', 'this', 'which',
    'what', 'who', 'whom', 'these', 'those', 'it', 'its', 'they', 'them',
    'their', 'we', 'our', 'you', 'your', 'he', 'him', 'his', 'she', 'her',
    'about', 'up', 'also', 'following', 'best', 'describes', 'statement',
    'true', 'false', 'correct', 'incorrect', 'among', 'given', 'one',
    'two', 'three', 'four', 'answer', 'question', 'option', 'none',
}


# ─── Utility Functions ───────────────────────────────────────────────────────

def strip_html(text):
    """Remove HTML tags and decode entities."""
    text = re.sub(r'<br\s*/?>', '. ', text)
    # Convert list items to sentences
    text = re.sub(r'<li[^>]*>', '\n', text)
    text = re.sub(r'</li>', '. ', text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&nbsp;', ' ').replace('&#39;', "'").replace('&quot;', '"')
    # Decode numeric HTML entities
    text = re.sub(r'&#x([0-9a-fA-F]+);', lambda m: chr(int(m.group(1), 16)), text)
    text = re.sub(r'&#(\d+);', lambda m: chr(int(m.group(1))), text)
    # Fix double spaces, space before period
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\.\s*\.', '.', text)
    return text.strip()


def split_sentences(text):
    """Split text into clean sentences."""
    # Split on newlines first
    lines = text.split('\n')
    all_sentences = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Split on sentence-ending punctuation followed by space+uppercase
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', line)
        all_sentences.extend(parts)

    cleaned = []
    for s in all_sentences:
        s = s.strip().strip('•').strip()
        # Skip very short fragments
        if len(s) < 20:
            continue
        # Skip boilerplate lesson intro sentences
        s_lower = s.lower()
        if any(s_lower.startswith(bp) for bp in [
            'this lesson covers', 'learning objectives',
            'in this lesson', 'by the end of this lesson', 'you will learn',
            'this section covers',
        ]):
            continue
        # Also catch boilerplate phrases appearing mid-sentence (e.g. after a title prefix)
        if any(bp in s_lower for bp in [
            'this lesson covers the fundamental',
            'this lesson covers key',
            'this section covers the fundamental',
        ]):
            continue
        # Skip standalone section titles that are just labels
        if re.match(r'^key concepts[\s:—-]', s_lower) and len(s) < 60:
            continue
        if 'important topic in' in s_lower and 'covering fundamental' in s_lower:
            continue
        # Skip generic AP boilerplate content
        if any(bp in s_lower for bp in [
            'include terminology, processes, and relationships',
            'has practical applications and real-world examples that demonstrate',
            'requires grasping how its concepts interact',
            'covering fundamental concepts and principles',
        ]):
            continue
        # Convert "Term: definition" style to "Term — definition" or proper sentence
        colon_match = re.match(r'^([A-Z][A-Za-z\s]{1,35}):\s+(.+)', s)
        if colon_match:
            term = colon_match.group(1).strip()
            definition = colon_match.group(2).strip()
            if definition:
                # Only convert if the term is a standalone concept word, not part of a sentence
                # Check if term looks like a label (short, no verbs)
                if len(term.split()) <= 3 and not any(v in term.lower() for v in ['comes', 'goes', 'has', 'was', 'were', 'word']):
                    s = f"{term} — {definition}"
                # Otherwise keep the colon as-is (it's part of a sentence)
        # Ensure ends with period
        if s and s[-1] not in '.!?':
            s += '.'
        # Fix space before period
        s = re.sub(r'\s+\.', '.', s)
        cleaned.append(s)
    return cleaned


def extract_keywords(text):
    """Extract meaningful keywords from text."""
    # Remove LaTeX/math notation for keyword extraction
    clean = re.sub(r'\$[^$]+\$', '', text)
    clean = re.sub(r'[^\w\s-]', ' ', clean.lower())
    words = clean.split()
    return {w for w in words if w not in STOPWORDS and len(w) > 2}


def keyword_overlap(text_keywords, target_keywords):
    """Score how well two keyword sets overlap."""
    if not text_keywords or not target_keywords:
        return 0
    overlap = text_keywords & target_keywords
    return len(overlap) / max(len(target_keywords), 1)


def get_lesson_content(lesson):
    """Extract plain text content from a lesson's summary_sections."""
    sections = lesson.get('summary_sections', [])
    all_text = []
    for s in sections:
        html = s.get('content_html', '')
        if html:
            plain = strip_html(html)
            all_text.append(plain)
    return ' '.join(all_text)


def find_relevant_sentences(lesson_text, question_text, correct_answer, max_sentences=2):
    """Find the most relevant sentences from lesson content for this question."""
    sentences = split_sentences(lesson_text)
    if not sentences:
        return []

    # Keywords from question and correct answer
    q_keywords = extract_keywords(question_text)
    a_keywords = extract_keywords(correct_answer)
    combined_keywords = q_keywords | a_keywords

    # Also get the correct answer as a phrase for direct matching
    answer_lower = correct_answer.lower().strip()
    # Extract key noun phrases from the answer (words > 3 chars)
    answer_important = {w for w in answer_lower.split() if len(w) > 3 and w not in STOPWORDS}

    scored = []
    for sent in sentences:
        sent_lower = sent.lower()
        sent_keywords = extract_keywords(sent)

        if not sent_keywords:
            continue

        # Base score: keyword overlap with question+answer
        overlap = combined_keywords & sent_keywords
        score = len(overlap) / max(len(combined_keywords), 1)

        # Strong bonus: sentence contains the correct answer text verbatim
        if answer_lower in sent_lower:
            score += 3.0
        # Medium bonus: sentence contains most important answer words
        elif answer_important:
            a_overlap = len(answer_important & sent_keywords) / len(answer_important)
            if a_overlap >= 0.7:
                score += 1.5
            elif a_overlap >= 0.5:
                score += 0.8

        # Bonus: sentence has definition/explanation patterns
        if any(pat in sent_lower for pat in [' is defined as', ' refers to', ' means ', ' describes ']):
            score += 0.5
        elif ' is ' in sent_lower or ' are ' in sent_lower:
            score += 0.2

        # Penalty: too generic (very short or very long)
        if len(sent) < 25:
            score -= 0.5
        if len(sent) > 350:
            score -= 0.3

        # Penalty: sentence doesn't share any question keywords
        if not (q_keywords & sent_keywords):
            score -= 0.5

        # Minimum threshold: must share at least 2 keywords with question+answer
        if len(overlap) < 2:
            score -= 1.0

        if score > 0.3:
            scored.append((score, sent))

    # Sort by score descending
    scored.sort(key=lambda x: -x[0])

    # Return top sentences, deduplicating and avoiding contradictions
    results = []
    seen_keywords = set()
    for score, sent in scored[:max_sentences * 3]:
        sent_kw = extract_keywords(sent)
        # Skip if too similar to already-selected sentences
        if seen_keywords and len(sent_kw & seen_keywords) / max(len(sent_kw), 1) > 0.8:
            continue
        results.append(sent)
        seen_keywords |= sent_kw
        if len(results) >= max_sentences:
            break

    return results


def format_distractor_analysis(question_text, correct_answer, wrong_answers, course):
    """Generate text explaining why wrong answers are incorrect."""
    if not wrong_answers:
        return ""

    q_lower = question_text.lower()
    is_not_question = any(phrase in q_lower for phrase in [
        'is not', 'are not', 'is not a', 'not a ', 'not an ', 'not true',
        'does not', 'do not', 'cannot', 'except', 'least likely',
        'would not', 'is false', 'incorrect'
    ])

    # Filter empty wrong answers
    wrong = [w.strip() for w in wrong_answers if w.strip()]
    if not wrong:
        return ""

    if is_not_question:
        # For NOT questions, the "wrong" answers are actually correct things
        if len(wrong) == 1:
            return f"Unlike '{correct_answer}', {wrong[0]} is a valid example of what the question describes."
        parts = [f"'{w}'" for w in wrong]
        if len(parts) == 2:
            joined = f"{parts[0]} and {parts[1]}"
        else:
            joined = f"{', '.join(parts[:-1])}, and {parts[-1]}"
        return f"The other options — {joined} — are all valid examples, making '{correct_answer}' the correct exception."
    else:
        parts = [f"'{w}'" for w in wrong]
        if len(parts) == 1:
            return f"{parts[0]} is a common misconception but does not apply here."
        elif len(parts) == 2:
            joined = f"{parts[0]} and {parts[1]}"
        else:
            joined = f"{', '.join(parts[:-1])}, and {parts[-1]}"
        return f"The other options — {joined} — are related concepts but do not correctly answer this specific question."


# ─── Math-Specific Helpers ────────────────────────────────────────────────────

def try_math_explanation(question_text, correct_answer, options):
    """Try to generate a step-by-step math explanation."""
    # Normalize HTML entities and Unicode math symbols before matching
    import html
    question_text = html.unescape(question_text)
    correct_answer = html.unescape(correct_answer)
    # Normalize Unicode math symbols to ASCII for matching
    _norm = {'\u2212': '-', '\u2264': '<=', '\u2265': '>=', '\u221a': 'sqrt',
             '\u221b': 'cbrt', '\u00d7': '*', '\u00f7': '/', '\u2260': '!='}
    q_normalized = question_text
    for uc, asc in _norm.items():
        q_normalized = q_normalized.replace(uc, asc)
    q = q_normalized.lower().strip()
    answer = correct_answer.strip()

    # Mean calculation
    match = re.search(r'mean\s+of\s+(?:the\s+)?(?:data\s+set\s+)?[{\[](\d[\d,\s.]*\d)[}\]]', q)
    if match:
        nums_str = match.group(1)
        nums = [float(x.strip()) for x in nums_str.split(',') if x.strip()]
        if nums:
            total = sum(nums)
            mean = total / len(nums)
            nums_display = ' + '.join(str(int(n) if n == int(n) else n) for n in nums)
            return (f"The mean is calculated by adding all values and dividing by the count: "
                    f"({nums_display}) / {len(nums)} = {total:g} / {len(nums)} = {mean:g}.")

    # Median
    if 'median' in q:
        match = re.search(r'[{\[](\d[\d,\s.]*\d)[}\]]', q)
        if match:
            nums = sorted([float(x.strip()) for x in match.group(1).split(',') if x.strip()])
            if nums:
                n = len(nums)
                if n % 2 == 1:
                    median = nums[n // 2]
                    return (f"To find the median, sort the values and pick the middle one. "
                            f"Sorted: {[int(x) if x==int(x) else x for x in nums]}. "
                            f"The middle value (position {n//2+1} of {n}) is {median:g}.")
                else:
                    median = (nums[n//2-1] + nums[n//2]) / 2
                    return (f"To find the median, sort the values and average the two middle ones. "
                            f"Sorted: {[int(x) if x==int(x) else x for x in nums]}. "
                            f"Middle values: {nums[n//2-1]:g} and {nums[n//2]:g}. "
                            f"Median = ({nums[n//2-1]:g} + {nums[n//2]:g}) / 2 = {median:g}.")

    # Range
    if 'range' in q:
        match = re.search(r'[{\[]([-−]?\d[\d,\s.\-−]*\d)[}\]]', q)
        if match:
            nums_text = match.group(1).replace('−', '-')
            nums = [float(x.strip()) for x in nums_text.split(',') if x.strip()]
            if nums:
                r = max(nums) - min(nums)
                return (f"The range is the difference between the largest and smallest values: "
                        f"{max(nums):g} - ({min(nums):g}) = {r:g}.")

    # Slope between two points
    match = re.search(r'slope.*?\((-?\d+)\s*,\s*(-?\d+)\).*?\((-?\d+)\s*,\s*(-?\d+)\)', q)
    if match:
        x1, y1, x2, y2 = [int(match.group(i)) for i in range(1, 5)]
        if x2 != x1:
            slope = (y2 - y1) / (x2 - x1)
            return (f"Slope = (y₂ - y₁) / (x₂ - x₁) = ({y2} - {y1}) / ({x2} - {x1}) "
                    f"= {y2-y1} / {x2-x1} = {slope:g}.")

    # Simple arithmetic in answer (look for number answers)
    if re.match(r'^-?\d+\.?\d*$', answer):
        # It's a plain number answer - try to see if question has calculation context
        if 'sum' in q or 'add' in q or 'total' in q:
            return f"Adding the values together gives {answer}."
        if 'difference' in q or 'subtract' in q:
            return f"Subtracting the values gives {answer}."
        if 'product' in q or 'multiply' in q:
            return f"Multiplying the values gives {answer}."
        if 'quotient' in q or 'divide' in q:
            return f"Dividing the values gives {answer}."

    # Density formula
    if 'density' in q and ('mass' in q or 'volume' in q):
        return "Density is defined as mass divided by volume (d = m/v). Rearrange or substitute values as needed to solve."

    # Percent yield
    if 'percent yield' in q or '% yield' in q:
        return "Percent yield = (actual yield / theoretical yield) × 100%. This measures how efficient a reaction was compared to its theoretical maximum."

    # Quadratic formula
    if 'quadratic formula' in q:
        return "The quadratic formula x = (-b ± √(b²-4ac)) / 2a solves any equation of the form ax² + bx + c = 0."

    # Pythagorean theorem
    if 'pythagorean' in q or ('hypotenuse' in q and ('leg' in q or 'triangle' in q)):
        return "By the Pythagorean theorem, a² + b² = c², where c is the hypotenuse. Substitute the known values and solve for the unknown side."

    # Area/perimeter
    if 'area' in q and 'circle' in q:
        return "The area of a circle is A = πr². Substitute the radius and calculate."
    if 'circumference' in q:
        return "The circumference of a circle is C = 2πr (or πd). Substitute the radius or diameter and calculate."
    if 'area' in q and 'triangle' in q:
        return "The area of a triangle is A = ½ × base × height. Substitute the given values and calculate."
    if 'area' in q and 'rectangle' in q:
        return "The area of a rectangle is A = length × width. Substitute the given values and calculate."

    # Integration
    if '\\int' in question_text or 'integral' in q or 'integrate' in q:
        return f"Apply the power rule for integration: ∫xⁿ dx = xⁿ⁺¹/(n+1) + C. The result is {correct_answer}."

    # Derivative
    if 'derivative' in q or 'differentiate' in q or "d/dx" in q or "f'(" in question_text:
        return f"Apply the appropriate differentiation rule (power rule, chain rule, product rule, etc.). The derivative evaluates to {correct_answer}."

    # Limit (mathematical - avoid matching "limiting factor" in biology)
    if re.search(r'\blim\b|\blimit\b', q) and not re.search(r'limiting\s+(factor|reagent|reactant)', q):
        return f"Evaluate the limit by substitution, factoring, or L'Hôpital's rule as appropriate. The limit equals {correct_answer}."

    # Volume of shapes
    if 'volume' in q and ('sphere' in q or 'ball' in q):
        return "The volume of a sphere is V = (4/3)πr³. Substitute the radius and calculate."
    if 'volume' in q and ('cylinder' in q):
        return "The volume of a cylinder is V = πr²h, where r is the radius and h is the height."
    if 'volume' in q and ('cone' in q):
        return "The volume of a cone is V = (1/3)πr²h, where r is the base radius and h is the height."
    if 'volume' in q and ('prism' in q or 'rectangular' in q or 'box' in q):
        return "The volume of a rectangular prism is V = length × width × height."

    # Surface area
    if 'surface area' in q and 'sphere' in q:
        return "The surface area of a sphere is SA = 4πr². Substitute the radius and calculate."
    if 'surface area' in q and ('cylinder' in q):
        return "The surface area of a cylinder is SA = 2πr² + 2πrh (two circles plus the lateral surface)."

    # Probability
    if 'probability' in q:
        return f"Probability = (favorable outcomes) / (total outcomes). Working through the calculation gives {correct_answer}."

    # Standard deviation / variance
    if 'standard deviation' in q:
        return f"Standard deviation measures the average distance of data points from the mean. The answer is {correct_answer}."
    if 'variance' in q:
        return f"Variance is the average of squared deviations from the mean (σ² = Σ(x-μ)²/n). The answer is {correct_answer}."

    # Solve for x
    if 'solve for' in q or 'find x' in q or 'value of x' in q:
        return f"Isolate the variable by performing inverse operations on both sides of the equation. Solving gives {answer}."

    # Factorial
    if re.search(r'\d+\s*!', q) and 'factor' not in q.replace('factorial', ''):
        return f"n! (n factorial) = n × (n-1) × (n-2) × ... × 2 × 1. For example, 5! = 5×4×3×2×1 = 120. By definition, 0! = 1. The answer is {answer}."

    # Combinations C(n,r)
    if re.search(r'c\s*\(\s*\d+\s*,\s*\d+\s*\)', q):
        return f"Combinations C(n,r) = n! / [r!(n-r)!] count selections where order doesn't matter. Substitute the given values and simplify. The answer is {answer}."

    # Permutations P(n,r)
    if re.search(r'p\s*\(\s*\d+\s*,\s*\d+\s*\)', q):
        return f"Permutations P(n,r) = n! / (n-r)! count arrangements where order matters. Substitute the given values and simplify. The answer is {answer}."

    # Complete the square
    if 'complete' in q and ('square' in q or 'the sq' in q):
        return f"To complete the square for x² + bx: add (b/2)². For x² + bx + (b/2)², the result factors as (x + b/2)². The answer is {answer}."

    # Complete (without "square" — catch "Complete: x² + 6x + ?")
    if 'complete' in q and re.search(r'x\s*[²\^2]', q):
        return f"To complete the square for x² + bx: take half the coefficient of x, then square it → (b/2)². This makes a perfect square trinomial: (x + b/2)². The answer is {answer}."

    # Parabola opens up or down
    if ('open' in q or 'direction' in q) and ('up' in q or 'down' in q or 'parabola' in q):
        return f"A parabola y = ax² + bx + c opens upward if a > 0 and downward if a < 0. The leading coefficient determines the direction. The answer is '{answer}'."

    # Discriminant
    if 'discriminant' in q:
        return f"The discriminant Δ = b² - 4ac determines the nature of roots: Δ > 0 → two real roots, Δ = 0 → one repeated root, Δ < 0 → no real roots (two complex roots). The answer is '{answer}'."

    # Matrix / augmented matrix
    if 'augmented' in q and 'matrix' in q:
        return f"An augmented matrix [A|b] represents a system of equations. Each row is an equation; the last column (after the bar) contains the constants. The answer is '{answer}'."
    if 'matrix' in q and ('row' in q or 'echelon' in q or 'reduce' in q or 'gauss' in q):
        return f"Row reduction (Gaussian elimination) transforms the augmented matrix to row echelon form using elementary row operations: swap rows, multiply by a scalar, or add a multiple of one row to another. The answer is '{answer}'."

    # Free variable / parametric
    if 'free variable' in q or 'parametric' in q:
        return f"A free variable occurs when a system has infinitely many solutions. It can take any value, and the other variables are expressed in terms of it (parametric form). The answer is '{answer}'."

    # 3×3 system / three variables
    if re.search(r'3\s*[×x]\s*3|three.*variable|three.*equation', q) and ('system' in q or 'solve' in q):
        return f"A 3×3 system of equations can be solved using elimination (eliminate one variable at a time), substitution, or matrices (row reduction). The answer is '{answer}'."

    # Systems of equations
    if 'system' in q and ('equation' in q or 'simultaneous' in q):
        return f"Use substitution or elimination to solve the system of equations. The solution is {answer}."

    # Factoring
    if 'factor' in q:
        return f"Factor the expression by finding common factors or using patterns (difference of squares, trinomial factoring, etc.). The factored form is {answer}."

    # ─── Algebra 2 / Precalculus ──────────────────────────────────────────

    # Function evaluation f(x) = ... find f(a)
    if re.search(r'f\s*\(\s*-?\d', q) and ('find' in q or 'what' in q or 'evaluate' in q or '=' in q):
        return f"Substitute the input value into the function expression and simplify using order of operations. The result is {answer}."

    # Domain
    if 'domain' in q:
        if 'sqrt' in q or '√' in question_text or 'radical' in q or 'square root' in q:
            return f"For square root functions, the expression under the radical must be ≥ 0. Set the radicand ≥ 0 and solve. The domain is {answer}."
        if 'rational' in q or 'fraction' in q or 'denominator' in q:
            return f"For rational functions, the domain excludes values that make the denominator zero. Set the denominator ≠ 0 and solve. The domain is {answer}."
        if 'log' in q or 'logarithm' in q:
            return f"For logarithmic functions, the argument must be > 0. Set the argument > 0 and solve. The domain is {answer}."
        return f"The domain is the set of all valid input values for the function. Consider restrictions from square roots (≥ 0), denominators (≠ 0), and logarithms (> 0). The domain is {answer}."

    # Range
    if 'range' in q and ('function' in q or 'f(x)' in q or 'graph' in q):
        return f"The range is the set of all possible output values of the function. Analyze the function's behavior, transformations, and any bounds. The range is {answer}."

    # Composition of functions
    if 'composition' in q or re.search(r'f\s*[∘°]\s*g|g\s*[∘°]\s*f|\(f\s*∘\s*g\)|\(f\s*[○]\s*g\)', q):
        return f"For function composition (f ∘ g)(x), substitute g(x) into f: f(g(x)). Replace each x in f with the expression for g(x), then simplify. The result is {answer}."

    # Inverse function
    if 'inverse' in q and ('function' in q or 'f' in q.split()):
        return f"To find the inverse f⁻¹(x): swap x and y in y = f(x), then solve for y. The inverse 'undoes' the original function. The result is {answer}."

    # Y-intercept
    if 'y-intercept' in q or 'y intercept' in q:
        return f"The y-intercept is the point where the graph crosses the y-axis (x = 0). Substitute x = 0 into the equation and solve for y. The y-intercept is {answer}."

    # X-intercept / zeros / roots
    if 'x-intercept' in q or 'x intercept' in q or ('zero' in q and 'function' in q):
        return f"The x-intercepts (zeros) are where the graph crosses the x-axis (y = 0). Set the function equal to zero and solve. The answer is {answer}."

    # Slope
    if 'slope' in q:
        if 'perpendicular' in q:
            return f"Perpendicular lines have slopes that are negative reciprocals. If the original slope is m, the perpendicular slope is -1/m. The answer is {answer}."
        if 'parallel' in q:
            return f"Parallel lines have equal slopes. The slope is {answer}."
        return f"Slope measures the rate of change: rise/run = (y₂ - y₁)/(x₂ - x₁). From the given information, the slope is {answer}."

    # Point-slope / equation of a line
    if ('equation' in q and ('line' in q or 'point' in q and 'slope' in q)):
        return f"Use point-slope form: y - y₁ = m(x - x₁), where m is the slope and (x₁, y₁) is a point on the line. Simplify to slope-intercept form. The equation is {answer}."

    # Exponential growth/decay
    if 'exponential' in q and ('growth' in q or 'decay' in q or 'model' in q):
        return f"Exponential functions have the form f(x) = a·bˣ, where b > 1 means growth and 0 < b < 1 means decay. The initial value is a, and b is the growth/decay factor. The answer is {answer}."

    # Logarithm
    # Logarithm
    if re.search(r'\blog\b|\blogarithm', q):
        return f"Logarithms are the inverse of exponentials: log_b(x) = y means bʸ = x. Use logarithm properties (product, quotient, power rules) to simplify. The answer is {answer}."

    # Asymptote
    if 'asymptote' in q:
        if 'horizontal' in q:
            return f"A horizontal asymptote describes end behavior as x → ±∞. Compare the degrees of numerator and denominator. The horizontal asymptote is {answer}."
        if 'vertical' in q:
            return f"Vertical asymptotes occur where the denominator equals zero (and the numerator doesn't). Set the denominator = 0 and solve. The vertical asymptote is {answer}."
        return f"Asymptotes are lines the graph approaches but never reaches. The answer is {answer}."

    # Polynomial degree / end behavior
    if 'end behavior' in q:
        return f"End behavior is determined by the leading term (highest-degree term). Even degree → same direction on both ends; odd degree → opposite directions. Positive leading coefficient → rises right. The answer is {answer}."

    # Absolute value
    if 'absolute value' in q or '|' in question_text:
        return f"The absolute value |x| gives the distance from zero, always non-negative. For equations |expression| = k, split into two cases: expression = k and expression = -k. The answer is {answer}."

    # Simplify expression
    if 'simplify' in q:
        return f"Combine like terms, factor where possible, and reduce fractions by canceling common factors. The simplified result is {answer}."

    # Vertex of parabola
    if 'vertex' in q:
        return f"The vertex of a parabola y = ax² + bx + c is at x = -b/(2a). Substitute back to find y. In vertex form y = a(x-h)² + k, the vertex is (h, k). The vertex is {answer}."

    # Axis of symmetry
    if 'axis of symmetry' in q:
        return f"The axis of symmetry of a parabola y = ax² + bx + c is the vertical line x = -b/(2a). The axis of symmetry is {answer}."

    # ─── Systems of Equations (broader patterns) ──────────────────────────

    # Detect two-equation patterns: "solve: ... and ..." or "y = ... and y = ..."
    if re.search(r'solve.*?\band\b', q) and re.search(r'[=].*\band\b.*[=]', q):
        return f"Solve the system by substitution (express one variable in terms of the other, then substitute) or elimination (add/subtract equations to eliminate a variable). The solution is {answer}."
    if 'substitute into' in q or 'substitution' in q:
        return f"With substitution, replace one variable with an equivalent expression from the other equation, then solve. The result is {answer}."
    if 'intersection' in q and ('=' in q or 'y' in q or 'line' in q or 'graph' in q):
        return f"The intersection point is where two equations have the same x and y values. Set the expressions equal and solve. The intersection is {answer}."
    if 'solve by graphing' in q or ('graph' in q and 'solve' in q):
        return f"When solving by graphing, plot both equations and find where the lines/curves cross. The point of intersection is the solution: {answer}."
    if 'express' in q and 'in terms of' in q:
        return f"To express one variable in terms of another, isolate that variable on one side of the equation using inverse operations. The result is {answer}."
    if 'elimination' in q and ('solve' in q or 'system' in q):
        return f"Elimination method: multiply equations if needed so one variable has opposite coefficients, then add the equations to eliminate it. Solve for the remaining variable. The solution is {answer}."

    # f⁻¹ (inverse function notation)
    if 'f⁻¹' in question_text or 'f^(-1)' in q or 'f^{-1}' in q or 'f-1' in q:
        return f"To find f⁻¹(x): replace f(x) with y, swap x and y, then solve for y. The inverse function 'undoes' the original. The result is {answer}."

    # ─── Radicals ─────────────────────────────────────────────────────────

    if 'rationalize' in q:
        return f"To rationalize a denominator, multiply numerator and denominator by the radical (or its conjugate) to eliminate the square root from the denominator. The result is {answer}."
    if '√' in question_text or '\\sqrt' in question_text:
        if '·' in question_text or '×' in question_text or '*' in question_text:
            return f"Use the product property of radicals: √(a·b) = √a · √b. Simplify each radical if possible, then multiply. The result is {answer}."
        if '+' in question_text or '-' in question_text or '−' in question_text:
            return f"Simplify each radical first (find perfect square factors), then combine like radicals (same radicand). The result is {answer}."
        return f"Simplify radicals by factoring out perfect squares: √(n) = √(a²·b) = a√b. The result is {answer}."
    if 'radical' in q and ('simplif' in q or 'add' in q or 'subtract' in q or 'multiply' in q):
        return f"To work with radicals: simplify by extracting perfect squares, combine like radicals, and use √a · √b = √(ab). The result is {answer}."

    # ─── IQR / Interquartile Range ────────────────────────────────────────

    if 'iqr' in q or 'interquartile' in q:
        return f"The IQR (Interquartile Range) = Q3 - Q1. It measures the spread of the middle 50% of data and is resistant to outliers. The answer is {answer}."
    if ('q1' in q or 'q3' in q) and ('quartile' in q or 'q1' in q and 'q3' in q):
        return f"Quartiles divide sorted data into four equal parts. Q1 is the median of the lower half, Q3 is the median of the upper half, and IQR = Q3 - Q1. The answer is {answer}."

    # ─── Geometry Basics ──────────────────────────────────────────────────

    # Segment addition postulate
    if 'between' in q and re.search(r'\b[A-Z]\b.*\b[A-Z]\b.*\b[A-Z]\b', question_text):
        return f"The Segment Addition Postulate states that if point B is between A and C, then AB + BC = AC. Add the given segment lengths. The answer is {answer}."

    # Distance formula
    if 'distance' in q and ('between' in q or 'from' in q) and re.search(r'\(.*?,.*?\)', q):
        return f"The distance formula: d = √[(x₂-x₁)² + (y₂-y₁)²]. Substitute the coordinates, compute the differences, square them, add, and take the square root. The answer is {answer}."

    # Midpoint
    if 'midpoint' in q:
        return f"The midpoint of a segment with endpoints (x₁,y₁) and (x₂,y₂) is M = ((x₁+x₂)/2, (y₁+y₂)/2). The midpoint divides the segment into two equal parts. The answer is {answer}."

    # Polygon sides
    if re.search(r'how many sides', q) or re.search(r'sides\s+does\s+a\s+\w+\s+have', q):
        return f"Common polygons: triangle (3), quadrilateral (4), pentagon (5), hexagon (6), heptagon (7), octagon (8), nonagon (9), decagon (10). The answer is {answer}."
    if 'hexagon' in q and ('side' in q or 'angle' in q or 'area' in q):
        return f"A regular hexagon has 6 equal sides and interior angles of 120° each. Sum of interior angles = (n-2)×180° = 720°. The answer is {answer}."

    # 3D shapes
    if ('cube' in q or 'rectangular prism' in q) and ('face' in q or 'edge' in q or 'vertices' in q or 'vertex' in q):
        return f"A cube has 6 faces, 12 edges, and 8 vertices. For any polyhedron, Euler's formula: V - E + F = 2. The answer is {answer}."

    # Circle theorems
    if 'circle' in q and ('similar' in q or 'congruent' in q):
        return f"All circles are similar because any circle can be mapped to another through a dilation (scaling). Circles are congruent only if they have the same radius. The answer is {answer}."
    if 'circle' in q and ('chord' in q or 'arc' in q or 'inscribed' in q or 'central angle' in q):
        return f"Key circle theorems: a central angle equals its intercepted arc; an inscribed angle = ½ its intercepted arc; two chords intersecting inside form angles = ½(sum of arcs). The answer is {answer}."

    # Conic sections
    if 'parabola' in q and ('focus' in q or 'directrix' in q):
        return f"A parabola is the set of all points equidistant from a focus (point) and a directrix (line). The vertex is midway between focus and directrix. The answer is {answer}."

    # Congruence / similarity
    if ('sss' in q or 'sas' in q or 'asa' in q or 'aas' in q or 'hl' in q) and ('congruen' in q or 'triangle' in q or 'prove' in q):
        return f"Triangle congruence can be proven with: SSS (3 sides), SAS (2 sides + included angle), ASA (2 angles + included side), AAS (2 angles + non-included side), or HL (right triangle hypotenuse-leg). The answer is {answer}."

    # Angle relationships
    if 'supplement' in q and 'angle' in q:
        return f"Supplementary angles add up to 180°. If two angles form a linear pair, they are supplementary. The answer is {answer}."
    if 'complement' in q and 'angle' in q:
        return f"Complementary angles add up to 90°. The answer is {answer}."
    if 'vertical angle' in q or 'vertically opposite' in q:
        return f"Vertical angles (formed by intersecting lines) are always congruent (equal in measure). The answer is {answer}."

    # Parallel lines + transversal
    if ('parallel' in q and 'transversal' in q) or ('alternate interior' in q or 'corresponding angle' in q or 'co-interior' in q):
        return f"When a transversal crosses parallel lines: corresponding angles are equal, alternate interior angles are equal, and co-interior (same-side interior) angles are supplementary (sum to 180°). The answer is {answer}."

    # Interior/exterior angles of polygon
    if 'interior angle' in q and ('polygon' in q or 'sum' in q):
        return f"Sum of interior angles of an n-sided polygon = (n-2) × 180°. Each interior angle of a regular polygon = (n-2) × 180° / n. The answer is {answer}."
    if 'exterior angle' in q and ('polygon' in q or 'sum' in q or 'triangle' in q):
        return f"The sum of exterior angles of any convex polygon is always 360°. Each exterior angle of a regular n-gon = 360°/n. An exterior angle of a triangle = sum of the two non-adjacent interior angles. The answer is {answer}."

    # Transformation
    if 'reflection' in q or 'translate' in q or 'rotation' in q or 'dilation' in q:
        if 'dilation' in q:
            return f"A dilation scales a figure by a factor k from a center point. If k > 1, it enlarges; if 0 < k < 1, it reduces. Dilations produce similar figures. The answer is {answer}."
        if 'reflection' in q:
            return f"A reflection flips a figure over a line (axis of reflection). The image is the same distance from the line as the original, on the opposite side. The answer is {answer}."
        if 'rotation' in q:
            return f"A rotation turns a figure around a fixed point by a given angle. 90° rotations: (x,y) → (-y,x). 180°: (x,y) → (-x,-y). The answer is {answer}."
        return f"Translations slide every point the same distance and direction. The shape and size are preserved (rigid motion/isometry). The answer is {answer}."

    # ─── Rational Exponents / Fractional Exponents ────────────────────────

    if re.search(r'\d+\s*\^\s*\(\s*\d+\s*/\s*\d+\s*\)', q) or re.search(r'\d+\^[⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞½]', q):
        return f"For rational exponents: a^(m/n) = ⁿ√(aᵐ) = (ⁿ√a)ᵐ. First find the nth root, then raise to the mth power (or vice versa). The result is {answer}."
    if re.search(r'x\s*\^\s*\(\s*1\s*/\s*2\s*\)', q) or 'x^(1/2)' in q:
        return f"The rational exponent x^(1/2) is equivalent to √x (the square root of x). In general, x^(1/n) = ⁿ√x. The answer is {answer}."
    if re.search(r'\^\s*\(\s*\d+\s*/\s*\d+\s*\)', q):
        return f"For rational exponents: a^(m/n) means take the nth root of a, then raise to the mth power. Equivalently, (ⁿ√a)ᵐ = ⁿ√(aᵐ). The result is {answer}."

    # ─── Solving Radical Equations ────────────────────────────────────────

    if ('solve' in q or 'find' in q) and ('√' in question_text or '∛' in question_text or 'âˆš' in question_text):
        return f"To solve a radical equation: isolate the radical, then raise both sides to the appropriate power (square for √, cube for ∛) to eliminate it. Always check for extraneous solutions. The solution is {answer}."

    # ─── Word Problems ────────────────────────────────────────────────────

    # Mixture problems
    if ('mixture' in q or 'mix' in q or '%' in q) and ('solution' in q or 'concentration' in q or 'percent' in q):
        return f"For mixture problems, use the equation: amount₁·concentration₁ + amount₂·concentration₂ = total·target_concentration. Set up the equation and solve. The answer is {answer}."
    if re.search(r'\d+%.*\+.*\d+%', q) or ('percent' in q and ('mix' in q or 'combine' in q)):
        return f"Mixture problems: (quantity₁ × rate₁) + (quantity₂ × rate₂) = total × desired rate. Set up the equation from the given percentages and amounts, then solve. The answer is {answer}."

    # Age problems
    if 'age' in q and ('years' in q or 'year' in q or 'old' in q):
        return f"For age problems: assign variables to current ages, write equations from the given relationships (e.g., 'in 10 years' means add 10), and solve the system. The answer is {answer}."

    # Distance/rate/time problems
    if ('mph' in q or 'km/h' in q or 'speed' in q) and ('apart' in q or 'meet' in q or 'travel' in q or 'arrive' in q):
        return f"Distance = Rate × Time. For objects moving apart, their combined rate is the sum of speeds. Set up d = rt equations and solve. The answer is {answer}."
    if 'train' in q or ('two' in q and ('car' in q or 'vehicle' in q) and ('speed' in q or 'mph' in q)):
        return f"For distance problems: d = rt. When objects move in opposite directions, their separation rate is the sum of speeds. When in the same direction, it's the difference. The answer is {answer}."

    # Combined work rate problems
    if ('fill' in q or 'drain' in q or 'complete' in q) and ('hour' in q or 'hr' in q) and ('together' in q or 'combined' in q or 'both' in q):
        return f"For combined work: if A takes a hours and B takes b hours alone, together their rate is 1/a + 1/b. Time together = 1/(1/a + 1/b) = ab/(a+b). The answer is {answer}."
    if re.search(r'(\d+)\s*hr|(\d+)\s*hour', q) and ('rate' in q or 'work' in q or 'fill' in q or 'job' in q):
        return f"Work rate problems: Rate = 1/Time. Combined rate = sum of individual rates. Combined time = 1/combined_rate. The answer is {answer}."

    # Interest problems
    if 'interest' in q and ('rate' in q or '%' in q or 'invest' in q):
        return f"For simple interest problems: I = Prt (Interest = Principal × rate × time). Set up equations from the given conditions and solve. The answer is {answer}."

    # Check/verify solution
    if ('check' in q or 'verify' in q or 'is .* a solution' in q) and re.search(r'\(\s*-?\d+\s*,\s*-?\d+\s*\)', q):
        return f"To check a solution, substitute the x and y values into the equation. If both sides are equal, the ordered pair is a valid solution. The answer is {answer}."
    if 'advantage' in q and ('elimination' in q or 'substitution' in q or 'graphing' in q):
        return f"Each method of solving systems has advantages: substitution when one variable is isolated, elimination when coefficients align for easy cancellation, graphing for visual understanding. The answer is {answer}."

    # ─── Geometry: Conic Sections ─────────────────────────────────────────

    if 'ellipse' in q and ('foci' in q or 'focus' in q or 'distance' in q or 'sum' in q):
        return f"An ellipse is the set of all points where the sum of distances from two foci is constant. The standard form is x²/a² + y²/b² = 1 (a > b). The answer is {answer}."
    if 'hyperbola' in q and ('foci' in q or 'focus' in q or 'difference' in q):
        return f"A hyperbola is the set of all points where the absolute difference of distances from two foci is constant. Standard form: x²/a² - y²/b² = 1. The answer is {answer}."
    if 'cavalieri' in q:
        return f"Cavalieri's Principle: two figures with equal cross-sectional widths at every height have equal areas (2D) or volumes (3D). The answer is {answer}."
    if 'area under' in q and ('curve' in q or 'y' in q or 'x' in q):
        return f"The area under a curve y = f(x) from a to b is found by integration: ∫ₐᵇ f(x) dx. For simple shapes (triangles, trapezoids), use geometry formulas. The answer is {answer}."

    # ─── Inequalities / Interval Notation ─────────────────────────────────

    # Solving simple inequalities
    if ('solve' in q or 'solution' in q) and re.search(r'[<>≤≥]|\\le|\\ge|â‰¤|â‰¥', q):
        return f"Solve inequalities like equations, but reverse the inequality sign when multiplying/dividing by a negative number. The solution is {answer}."
    if 'interval' in q or re.search(r'\[.*,.*\]|\(.*,.*\)', answer) and ('≤' in question_text or '≥' in question_text or '<' in question_text or '>' in question_text or 'â‰¤' in question_text or 'â‰¥' in question_text):
        return f"Interval notation: use [ ] for included endpoints (≤, ≥) and ( ) for excluded endpoints (<, >). Use ∞ or -∞ for unbounded intervals (always with parentheses). The answer is {answer}."
    if 'compound' in q and ('inequality' in q or re.search(r'[<>≤≥]|â‰¤|â‰¥', q)):
        return f"A compound inequality combines two conditions. 'And' means both must be true (intersection); 'or' means at least one (union). The solution is {answer}."

    # Linear programming / optimization with constraints
    if ('max' in q or 'min' in q or 'maximize' in q or 'minimize' in q) and ('subject to' in q or 'constraint' in q or re.search(r'[≤≥].*[≤≥]|â‰¤.*â‰¤|â‰¥.*â‰¥', q)):
        return f"In linear programming, evaluate the objective function at each vertex (corner point) of the feasible region. The maximum/minimum occurs at a vertex. The answer is {answer}."
    if ('optimal' in q or 'vertex' in q or 'corner' in q) and ('lp' in q or 'programming' in q or 'linear' in q or 'feasible' in q):
        return f"In linear programming, optimal values occur at vertices (corner points) of the feasible region. Evaluate the objective function at each vertex to find the maximum or minimum. The answer is '{answer}'."
    if ('max' in q or 'min' in q or 'optimal' in q) and ('corner' in q or 'edge' in q or 'vertex' in q):
        return f"The optimal solution in linear programming is always at a vertex of the feasible region. If the max/min occurs at two adjacent vertices, every point on the connecting edge is also optimal. The answer is '{answer}'."

    # Test a point in an inequality
    if 'test' in q and re.search(r'\(\s*-?\d+\s*,\s*-?\d+\s*\)', q):
        return f"To test a point in an inequality, substitute the x and y values. If the result satisfies the inequality, the point is in the solution region. The answer is {answer}."

    # Boundary line
    if 'boundary' in q and ('line' in q or 'solid' in q or 'dashed' in q):
        return f"For graphing inequalities: use a solid boundary line for ≤ or ≥ (points on the line are included) and a dashed line for < or > (points on the line are excluded). The answer is {answer}."

    # ─── Sequences ────────────────────────────────────────────────────────

    # Arithmetic sequence (find nth term)
    if re.search(r'(\d+)\w*\s*term', q) and re.search(r'\d+\s*,\s*\d+\s*,\s*\d+', q):
        # Check if arithmetic (constant difference) or geometric (constant ratio)
        nums = re.findall(r'-?\d+', q)
        if len(nums) >= 3:
            return f"For an arithmetic sequence, a(n) = a(1) + (n-1)d where d is the common difference. For geometric, a(n) = a(1)·rⁿ⁻¹ where r is the common ratio. Identify the pattern and apply the formula. The answer is {answer}."
    if 'arithmetic sequence' in q or 'common difference' in q:
        return f"In an arithmetic sequence, each term increases by a constant difference d: a(n) = a(1) + (n-1)d. The answer is {answer}."
    if 'geometric sequence' in q or 'common ratio' in q:
        return f"In a geometric sequence, each term is multiplied by a constant ratio r: a(n) = a(1)·rⁿ⁻¹. The answer is {answer}."
    if 'recursive' in q and 'explicit' in q:
        return f"A recursive formula defines each term using the previous term: a(n) = a(n-1) + d. An explicit formula gives any term directly: a(n) = a(1) + (n-1)d. Convert by finding the pattern. The answer is {answer}."
    if 'recursive' in q or 'a(n' in q and ('a(n-1)' in q or 'a(n−1)' in q):
        return f"A recursive formula defines each term using the previous term(s). To find a specific term, start with the initial value and apply the rule repeatedly. The answer is {answer}."
    if re.search(r'general term|nth term|explicit', q) and ('sequence' in q or re.search(r'a\s*\(\s*n\s*\)', q)):
        return f"The explicit (general) formula gives any term directly. For arithmetic: a(n) = a(1) + (n-1)d. For geometric: a(n) = a(1)·rⁿ⁻¹. The answer is {answer}."

    # ─── Basic Probability ────────────────────────────────────────────────

    if re.search(r'p\s*\(.*die|p\s*\(.*coin|p\s*\(.*card|p\s*\(.*roll', q):
        return f"Probability = favorable outcomes / total outcomes. For a die: 6 outcomes. For a coin: 2 outcomes. For a deck: 52 cards. The answer is {answer}."
    if re.search(r'p\s*\(', q) and ('=' in q or 'mean' in q or 'impossible' in q or 'certain' in q):
        return f"P(E) = 0 means the event is impossible; P(E) = 1 means it's certain. P(not E) = 1 - P(E) (complement rule). Probabilities always range from 0 to 1. The answer is {answer}."
    if 'complement' in q and ('probability' in q or 'p(' in q):
        return f"The complement rule: P(not A) = 1 - P(A). If you know the probability of an event, subtract from 1 to find the probability of it NOT occurring. The answer is {answer}."
    if 'how many ways' in q or 'how many different' in q:
        return f"Count arrangements using: permutations (order matters) = n!/(n-r)!, or combinations (order doesn't matter) = n!/[r!(n-r)!]. The answer is {answer}."

    # ─── Half-life ────────────────────────────────────────────────────────

    if 'half-life' in q or 'half life' in q:
        return f"Half-life is the time for half the substance to decay/react. After n half-lives, the remaining amount = initial × (1/2)ⁿ. The answer is {answer}."

    # ─── Scale models / similar figures volume ────────────────────────────

    if 'scale' in q and ('model' in q or 'factor' in q) and ('volume' in q or 'area' in q):
        return f"For similar figures with scale factor k: lengths scale by k, areas by k², and volumes by k³. If the scale is 1/n, the volume ratio is 1/n³. The answer is {answer}."

    # Euler's formula for polyhedra
    if 'euler' in q and ('formula' in q or 'vertices' in q or 'edges' in q or 'faces' in q):
        return f"Euler's formula for polyhedra: V - E + F = 2, where V = vertices, E = edges, F = faces. Substitute the known values and solve for the unknown. The answer is {answer}."

    # Prism vs pyramid
    if ('prism' in q and 'pyramid' in q) or ('prism' in q and ('distinguish' in q or 'differ' in q)):
        return f"A prism has 2 congruent parallel bases connected by rectangular faces; a pyramid has 1 base and triangular faces meeting at an apex. The answer is {answer}."

    # Geodesic
    if 'geodesic' in q:
        return f"A geodesic is the shortest path between two points on a curved surface. On a sphere, geodesics are great circle arcs (like the equator). The answer is {answer}."

    # ─── Catch-all for rate problems ──────────────────────────────────────

    if ('boat' in q or 'plane' in q or 'current' in q or 'wind' in q) and ('mph' in q or 'speed' in q or 'downstream' in q or 'upstream' in q):
        return f"For rate problems with current/wind: downstream/downwind speed = boat/plane speed + current/wind speed; upstream/upwind = speed - current/wind. Use d = rt. The answer is {answer}."

    # ─── Polynomial long division / remainder ─────────────────────────────

    if 'remainder' in q or 'long division' in q and 'polynomial' in q:
        return f"Use polynomial long division or the Remainder Theorem: f(c) equals the remainder when f(x) is divided by (x - c). The answer is {answer}."
    if 'synthetic division' in q:
        return f"Synthetic division is a shortcut for dividing a polynomial by (x - c). Bring down the leading coefficient, multiply by c, add columns. The last number is the remainder. The answer is {answer}."

    # LCD (Least Common Denominator)
    if 'lcd' in q or 'least common denominator' in q:
        return f"The Least Common Denominator (LCD) is the smallest expression that all denominators divide into evenly. Factor each denominator and take the highest power of each factor. The answer is {answer}."

    # Extraneous solutions
    if 'extraneous' in q:
        return f"Extraneous solutions are values that arise from the solving process but don't satisfy the original equation. They're common with radical equations, rational equations, and logarithms. Always check by substituting back. The answer is {answer}."

    # Sign analysis / number line test
    if 'sign analysis' in q or 'sign chart' in q or 'number line' in q and ('test' in q or 'inequality' in q):
        return f"Sign analysis: find critical values (zeros/undefined points), divide the number line into intervals, test a point in each interval to determine the sign of the expression. The answer is {answer}."

    # ─── Broad catch: "Solve: [equation]" without "solve for" ─────────────
    # This must be LAST in try_math to avoid overriding more specific patterns.
    if q.startswith('solve') and ('=' in question_text or '=' in question_text) and re.search(r'[xyz]', q):
        return f"Isolate the variable by performing inverse operations on both sides of the equation. Combine like terms, then divide or multiply to solve. The answer is {answer}."

    # Broad catch: "What is the first step in solving..."
    if 'first step' in q and ('solving' in q or 'solve' in q):
        return f"The first step in solving an equation is to simplify each side (distribute, combine like terms) and then isolate the variable using inverse operations. The answer is '{answer}'."

    # Broad catch: "Which solution should be rejected..."
    if 'reject' in q or ('no valid' in answer.lower() or 'cannot be negative' in answer.lower()):
        return f"When solving, check each candidate solution in the original equation. Square roots cannot equal negative numbers, and logarithms require positive arguments. Reject solutions that violate these domain restrictions. The answer is '{answer}'."

    # Broad catch: Inner function / outer function identification
    if 'inner function' in q or 'outer function' in q:
        return f"In a composite function f(g(x)), the inner function g(x) is evaluated first, and the outer function f is applied to the result. For the chain rule: d/dx[f(g(x))] = f'(g(x))·g'(x). The answer is '{answer}'."

    # Exponential growth/decay / compound interest
    if re.search(r'\d+\s*%.*growth|grow.*\d+\s*%|\d+\s*%.*annual|compound', q) and ('year' in q or 'after' in q or 'becomes' in q):
        return f"For compound growth: A = P(1 + r)ⁿ where P = principal, r = rate (as decimal), n = years. For compound interest, the formula may use A = P(1 + r/n)^(nt) for n compoundings per year. The answer is {answer}."
    if re.search(r'y\s*=\s*a\s*[·*]\s*b', q) and ('initial' in q or 'represent' in q or 'y-intercept' in q or "'a'" in q):
        return f"In the exponential function y = a·bˣ: 'a' is the initial value (y-intercept when x=0), and 'b' is the growth/decay factor. If b > 1, it grows; if 0 < b < 1, it decays. The answer is '{answer}'."

    # Floor / ceiling functions
    if re.search(r'floor|ceil|\u230a|\u230b|\u2308|\u2309', q) or re.search(r'\u230a', question_text):
        return f"The floor function rounds down to the nearest integer (e.g., floor(2.7) = 2, floor(-2.3) = -3). The ceiling function rounds up. The answer is {answer}."

    # Sequence with a(1) and d or r notation
    if re.search(r'a\s*\(\s*1\s*\)\s*=\s*-?\d+', q) and ('d' in q.split() or 'd =' in q):
        return f"In an arithmetic sequence with first term a(1) and common difference d: a(n) = a(1) + (n-1)d. Substitute the given values and simplify. The answer is {answer}."
    if re.search(r'a\s*\(\s*1\s*\)\s*=\s*-?\d+', q) and ('r' in q.split() or 'r =' in q or 'r=' in q):
        return f"In a geometric sequence with first term a(1) and common ratio r: a(n) = a(1)·rⁿ⁻¹. Substitute the given values and simplify. The answer is {answer}."

    # Optimization with area/perimeter constraint
    if ('max' in q or 'min' in q) and ('area' in q or 'perimeter' in q) and re.search(r'\d+', q):
        return f"For optimization with a constraint (e.g., fixed perimeter): express the quantity to optimize in terms of one variable, then find the vertex (for quadratics) or use calculus. A square maximizes area for a given perimeter. The answer is {answer}."

    # Function transformations: stretch, compress, shift, reflect
    if re.search(r'transformation|y\s*=\s*\d+\s*f\s*\(|f\s*\(\s*\d+\s*x\s*\)', q) and ('stretch' in q or 'compress' in q or 'shift' in q or 'reflect' in q or 'vertical' in q or 'horizontal' in q or 'stretch' in answer.lower() or 'compress' in answer.lower() or 'shift' in answer.lower()):
        return f"Function transformations: y = af(x) stretches/compresses vertically by |a|; y = f(bx) horizontally by 1/|b|; y = f(x-h)+k shifts h right and k up; negative signs reflect. The answer is '{answer}'."
    if 'transformation' in q and re.search(r'[yf]\s*=', q):
        return f"Function transformations: vertical stretch/compress changes the coefficient outside f; horizontal changes the coefficient inside. Additions/subtractions shift the graph. Negative signs cause reflections. The answer is '{answer}'."

    # Vertex form max/min
    if ('max' in q or 'min' in q) and re.search(r'f\s*\(\s*x\s*\)\s*=.*\(.*x', q):
        return f"In vertex form f(x) = a(x-h)² + k, the vertex is (h, k). If a > 0, the vertex is a minimum; if a < 0, it's a maximum. The min/max value is k. The answer is '{answer}'."

    # From squared equation: (x-a)² = b
    if re.search(r'\(\s*x\s*[-−+]\s*\d+\s*\)\s*[²\^2]\s*=\s*\d+', q):
        return f"To solve (x - a)² = b: take the square root of both sides → x - a = ±√b, then add a → x = a ± √b. This gives two solutions. The answer is {answer}."

    # Distributing / distributive property
    if 'distribut' in q:
        return f"The distributive property: a(b + c) = ab + ac. Multiply each term inside the parentheses by the outside factor. The answer is {answer}."

    # Identity equation
    if 'identity' in q and ('equation' in q or 'true for all' in q or 'called' in q):
        return f"An identity is an equation that is true for all values of the variable (e.g., 2(x+3) = 2x+6). A contradiction is true for no values. A conditional equation is true for specific values only. The answer is '{answer}'."
    if 'true for all' in q and ('values' in q or 'variable' in q):
        return f"An equation true for ALL values of the variable is called an identity. This means both sides simplify to the same expression. The answer is '{answer}'."
    if 'identity' in answer.lower() and ('equation' in q or 'called' in q or 'true' in q):
        return f"An identity is an equation that holds for every possible value of the variable. Examples include 2(x+3) = 2x+6 and sin²θ + cos²θ = 1. The answer is '{answer}'."

    # AND/OR inequality graph
    if ('and' in q or 'or' in q) and ('inequality' in q or 'graph' in q) and ('overlap' in q or 'region' in q or 'shows' in q or 'represent' in q):
        return f"For compound inequalities: 'AND' means the solution is the intersection (overlap) of the two regions. 'OR' means the solution is the union — points satisfying either condition. The answer is '{answer}'."

    # Graphing inequality (dashed/solid line, shade above/below)
    if ('graph' in q or 'draw' in q) and re.search(r'[<>≤≥]', q) and ('line' in answer.lower() or 'shade' in answer.lower() or 'dashed' in answer.lower() or 'solid' in answer.lower()):
        return f"To graph a linear inequality: draw the boundary line (dashed for < or >, solid for ≤ or ≥). Shade above the line for > or ≥, below for < or ≤. Test a point to verify. The answer is '{answer}'."

    # Vieta's formulas (sum/product of roots)
    if ('sum' in q and 'root' in q) or ('product' in q and 'root' in q) or "vieta" in q:
        return f"Vieta's formulas for ax² + bx + c = 0: the sum of roots = −b/a and the product of roots = c/a. These relate coefficients directly to roots without solving. The answer is {answer}."

    # Expand / standard form from factored (FOIL)
    if ('standard form' in q or 'expand' in q or 'foil' in q) and re.search(r'\(.*x.*\)\s*\(.*x.*\)', q):
        return f"Use FOIL (First, Outer, Inner, Last) to expand: multiply each term in the first parentheses by each term in the second, then combine like terms. The answer is {answer}."

    # Polynomial arithmetic: addition, subtraction, multiplication
    # Match patterns like (3x²+2x−5)+(x²−3x+7) or (2x+1)²
    if re.search(r'\(.*x.*\)\s*[\+\-]\s*\(.*x.*\)', q) or re.search(r'\(.*x.*\)\s*\(.*x.*\)\s*=', q):
        return f"Combine polynomials by distributing each term and collecting like terms. For addition/subtraction, add/subtract coefficients of matching powers. For multiplication, multiply each term by every term in the other factor. The answer is {answer}."
    if re.search(r'\(.*x.*\)\s*[²\^2]\s*=', q):
        return f"To square a binomial: (a + b)² = a² + 2ab + b². Alternatively, FOIL the expression with itself. The answer is {answer}."

    # Polynomial from zeros / roots
    if ('zero' in q or 'root' in q) and ('passes' in q or 'through' in q or 'write' in q or 'find' in q) and re.search(r'-?\d+.*-?\d+', q):
        return f"If a polynomial has zeros r₁, r₂, ... then f(x) = a(x - r₁)(x - r₂)... Use a known point to find the leading coefficient 'a'. The answer is {answer}."

    # Quadratic max height / vertex time (h(t) = -16t² + bt + c)
    if re.search(r'h\s*\(\s*t\s*\)|height', q) and re.search(r'-?\d+t\s*[²\^2]', q):
        return f"For h(t) = at² + bt + c, the maximum height occurs at t = -b/(2a). Substitute this time back into h(t) to find the maximum height. The answer is {answer}."

    # Break-even / revenue
    if 'break-even' in q or 'break even' in q or ('revenue' in q and ('cost' in q or 'profit' in q)):
        return f"Break-even occurs when Revenue = Cost (or Profit = 0). Set the revenue and cost functions equal and solve. Alternatively, set the profit function equal to zero. The answer is {answer}."

    # Increasing/decreasing intervals
    if 'increasing' in q and 'decreasing' in q:
        return f"A function is increasing where f'(x) > 0 and decreasing where f'(x) < 0. Find critical points (f'(x) = 0), then test intervals. For a parabola, the vertex divides the increasing/decreasing intervals. The answer is '{answer}'."

    # Regression / prediction (ŷ)
    if 'predict' in q and re.search(r'[ŷy]\s*=', q):
        return f"The regression equation ŷ = mx + b predicts the y-value for a given x. Substitute the x-value into the equation and simplify. The answer is {answer}."
    if 'residual' in q:
        return f"A residual = actual value - predicted value. Residuals measure how far data points are from the regression line. The sum of residuals is approximately zero for a least-squares regression. The answer is '{answer}'."
    if 'lurking' in q or 'confounding' in q or ('correlation' in q and 'causation' in q) or ('correlated' in q and 'because' in q):
        return f"Correlation does not imply causation. A lurking (confounding) variable may cause both variables to change together without a direct causal relationship between them. The answer is '{answer}'."
    if re.search(r'relative frequenc', q) and ('sum' in q or 'total' in q or 'add' in q):
        return f"All relative frequencies in a distribution must sum to 1 (or 100%), since they represent the proportion of each category relative to the whole. The answer is '{answer}'."

    # Function definition / vertical line test
    if 'function' in q and ('vertical line' in q or 'is it' in q or 'maps to' in q or 'one output' in q or 'two output' in q) or ('is {' in q and 'function' in q):
        return f"A function assigns exactly one output to each input. The vertical line test: if any vertical line crosses the graph more than once, it's not a function. The answer is '{answer}'."
    if 'f(0)' in q and ('represent' in q or 'means' in q or 'when' in q):
        return f"f(0) is the output when x = 0 — the y-intercept. Substitute 0 for x in the function expression to evaluate. The answer is '{answer}'."

    # Scientific notation operations
    if re.search(r'\d+\s*[×x]\s*10\s*[⁰¹²³⁴⁵⁶⁷⁸⁹]+', q) or ('scientific notation' in q and ('multiply' in q or 'divide' in q or 'add' in q)):
        return f"In scientific notation: multiply/divide the coefficients and add/subtract the exponents. For (a × 10ᵐ)(b × 10ⁿ) = (a·b) × 10^(m+n). Adjust so the coefficient is between 1 and 10. The answer is {answer}."

    # Significant figures
    if 'sig fig' in q or 'significant figure' in q or 'significant digit' in q:
        return f"Rules: all nonzero digits are significant; leading zeros are not; trailing zeros after a decimal point are; captive zeros are. For multiplication/division, use the fewest sig figs of any factor. For addition/subtraction, use the fewest decimal places. The answer is '{answer}'."

    # Metric unit conversions
    if re.search(r'(centi|milli|kilo|micro|nano).*meter|liter|gram', q) and ('equal' in q or 'how many' in q or 'convert' in q):
        return f"Metric prefixes: kilo = 10³, centi = 10⁻², milli = 10⁻³, micro = 10⁻⁶, nano = 10⁻⁹. To convert, multiply/divide by the appropriate power of 10. The answer is {answer}."
    if ('smaller' in q or 'larger' in q) and 'unit' in q and ('convert' in q or 'numerical' in q or 'value' in q):
        return f"When converting smaller units to larger units, the numerical value decreases (fewer large units needed). When converting larger to smaller, it increases. The answer is '{answer}'."

    return None


def try_science_explanation(question_text, correct_answer, course_name):
    """Try to generate domain-specific science explanations for common patterns.
    Checks both question text AND correct answer for known science terms."""
    import html
    question_text = html.unescape(question_text)
    correct_answer = html.unescape(correct_answer)
    # Normalize Unicode math symbols to ASCII for matching
    _norm = {'\u2212': '-', '\u2264': '<=', '\u2265': '>=', '\u221a': 'sqrt',
             '\u221b': 'cbrt', '\u00d7': '*', '\u00f7': '/', '\u2260': '!='}
    q_normalized = question_text
    for uc, asc in _norm.items():
        q_normalized = q_normalized.replace(uc, asc)
    q = q_normalized.lower().strip()
    answer = correct_answer.strip()
    a = answer.lower()
    course = course_name.lower()
    # Combined text for matching: includes both question and answer
    qa = q + ' ' + a

    # Gibbs free energy
    if 'spontaneous' in q and ('δg' in q or 'gibbs' in q or 'δh' in q or 'δs' in q):
        if 'temperature' in q or 'transition' in q:
            return f"At the transition temperature, ΔG = 0. Since ΔG = ΔH - TΔS, solving for T gives T = ΔH/ΔS. Plug in values (ensuring consistent units) to get {answer}."
        if 'negative' in answer.lower() or answer.lower().startswith('yes'):
            return "A reaction is spontaneous when ΔG < 0. Since ΔG = ΔH - TΔS, exothermic reactions (negative ΔH) with increased entropy (positive ΔS) are always spontaneous."
        return f"Spontaneity depends on the sign of ΔG = ΔH - TΔS. The conditions described yield {answer}."

    # pH / pOH (exclude biology enzyme context)
    if ('ph' in q.split() or q.startswith('ph ') or 'ph =' in q) and 'enzyme' not in q and 'protein' not in q and 'denatur' not in q:
        return f"pH = -log[H⁺]. For strong acids/bases, [H⁺] comes directly from dissociation. For weak ones, use Ka/Kb equilibrium. The pH is {answer}."

    # Molarity / concentration
    if 'molarity' in q or 'concentration' in q or 'moles per liter' in q:
        return f"Molarity (M) = moles of solute / liters of solution. Apply the formula to find {answer}."

    # Cell biology
    if 'mitosis' in q and 'meiosis' in q:
        return f"Mitosis produces 2 identical diploid cells for growth/repair, while meiosis produces 4 unique haploid gametes for reproduction. The answer is '{answer}'."
    if 'mitosis' in q:
        return f"Mitosis is cell division that produces two genetically identical daughter cells. It includes prophase, metaphase, anaphase, and telophase. The answer is '{answer}'."
    if 'meiosis' in q:
        return f"Meiosis is a two-stage cell division (meiosis I and II) that produces four haploid gametes from one diploid cell, introducing genetic variation through crossing over. The answer is '{answer}'."

    # DNA/RNA
    if 'transcription' in q and ('translation' not in q):
        return f"Transcription is the process of creating mRNA from a DNA template, occurring in the nucleus. RNA polymerase reads the template strand 3'→5'. The answer is '{answer}'."
    if 'translation' in q:
        return f"Translation is protein synthesis at the ribosome, where mRNA codons are read and matched with tRNA anticodons carrying specific amino acids. The answer is '{answer}'."
    if 'dna replication' in q:
        return f"DNA replication is semiconservative — each new double helix contains one original and one new strand. Helicase unwinds, primase adds primers, and DNA polymerase synthesizes new strands. The answer is '{answer}'."

    # Newton's laws
    if "newton's" in q or 'newtons' in q:
        if 'first' in q or '1st' in q:
            return f"Newton's First Law (inertia): An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted upon by a net external force. The answer is '{answer}'."
        if 'second' in q or '2nd' in q:
            return f"Newton's Second Law: F = ma. The net force on an object equals its mass times its acceleration. The answer is '{answer}'."
        if 'third' in q or '3rd' in q:
            return f"Newton's Third Law: For every action force, there is an equal and opposite reaction force. The answer is '{answer}'."

    # Ohm's law / circuits
    if "ohm's law" in q or ('voltage' in q and 'current' in q and 'resistance' in q):
        return f"Ohm's Law states V = IR (voltage = current × resistance). Rearrange to find the unknown quantity. The answer is {answer}."

    # Kinetic/potential energy
    if 'kinetic energy' in q:
        return f"Kinetic energy is the energy of motion: KE = ½mv². The answer is {answer}."
    if 'potential energy' in q and 'gravitational' in q:
        return f"Gravitational potential energy: PE = mgh (mass × gravity × height). The answer is {answer}."

    # Periodic table trends
    if 'electronegativity' in q:
        return f"Electronegativity increases going up and to the right on the periodic table (toward fluorine). This trend occurs because smaller atoms with more protons attract bonding electrons more strongly. The answer is '{answer}'."
    if 'ionization energy' in q:
        return f"Ionization energy increases going up and to the right on the periodic table. Smaller atoms with more nuclear charge hold their electrons more tightly. The answer is '{answer}'."
    if 'atomic radius' in q or 'atomic radii' in q:
        return f"Atomic radius increases going down a group (more electron shells) and decreases going left to right across a period (more protons pulling electrons closer). The answer is '{answer}'."
    if 'ionic radius' in q:
        return f"For cations, ionic radius < atomic radius (lost electrons). For anions, ionic radius > atomic radius (gained electrons). Among isoelectronic ions, higher nuclear charge means smaller radius. The answer is '{answer}'."

    # Bonding
    if 'ionic bond' in q:
        return f"Ionic bonds form between metals and nonmetals through electron transfer, creating oppositely charged ions that attract. The answer is '{answer}'."
    if 'covalent bond' in q:
        return f"Covalent bonds form between nonmetals through electron sharing. Polar covalent bonds have unequal sharing due to electronegativity differences. The answer is '{answer}'."

    # Acids and bases
    if 'acid' in q and 'base' in q:
        return f"Acids donate H⁺ (protons) while bases accept H⁺. Strong acids/bases fully dissociate; weak ones partially dissociate. The answer is '{answer}'."

    # Ecology
    if 'food chain' in q or 'food web' in q or 'trophic' in q:
        return f"Energy flows through trophic levels: producers → primary consumers → secondary consumers → tertiary consumers. Only about 10% of energy transfers between levels. The answer is '{answer}'."
    if 'ecosystem' in q and ('biotic' in q or 'abiotic' in q):
        return f"Biotic factors are living components (organisms, interactions), while abiotic factors are non-living (temperature, water, sunlight, soil). The answer is '{answer}'."
    if 'ecosystem' in q:
        return f"An ecosystem includes all living organisms (biotic) and their physical environment (abiotic) interacting as a system. Energy flows and nutrients cycle through ecosystems. The answer is '{answer}'."

    # ─── General Biology / Scientific Method ──────────────────────────────

    # Scientific method
    if 'scientific method' in q or ('hypothesis' in q and ('test' in q or 'experiment' in q)):
        return f"The scientific method: observe → ask a question → form a hypothesis → design an experiment → collect data → analyze → draw conclusions. A hypothesis must be testable and falsifiable. The answer is '{answer}'."
    if 'independent variable' in q or 'dependent variable' in q or 'control variable' in q:
        return f"The independent variable is what the scientist changes; the dependent variable is what is measured in response; controlled variables are kept constant. The answer is '{answer}'."
    if re.search(r'\bvariable\b', q) and ('change' in q or 'scientist' in q or 'experiment' in q):
        return f"In an experiment, the independent variable is deliberately changed, the dependent variable is measured as a response, and controlled variables are held constant for a fair test. The answer is '{answer}'."
    if 'control group' in q or 'experimental group' in q:
        return f"The control group receives no treatment/standard treatment for comparison, while the experimental group receives the treatment being tested. This comparison isolates the effect of the variable. The answer is '{answer}'."
    if re.search(r'\bdata\b', q) and ('collect' in q or 'information' in q or 'experiment' in q) and len(q) < 80:
        return f"Data is information collected through observation or experimentation. Quantitative data is numerical; qualitative data describes qualities or characteristics. The answer is '{answer}'."

    # Cell organization
    if 'cell' in q and ('tissue' in q or 'organ' in q or 'system' in q) and 'order' in q:
        return f"Biological organization from smallest to largest: cell → tissue → organ → organ system → organism. Each level has emergent properties not present at lower levels. The answer is '{answer}'."

    # Characteristics of life
    if 'characteristic' in q and 'life' in q:
        return f"The characteristics of life include: cellular organization, reproduction, metabolism, homeostasis, response to stimuli, growth/development, adaptation/evolution, and use of energy. The answer is '{answer}'."

    # Stimulus / response
    if 'stimulus' in q or 'respond' in q and 'environment' in q:
        return f"Responding to stimuli is a fundamental characteristic of life. Organisms detect changes in their environment (stimuli) and react accordingly to maintain survival. The answer is '{answer}'."

    # Biotechnology
    if 'biotechnology' in q or 'genetic engineering' in q or 'gmo' in q:
        return f"Biotechnology uses living systems or organisms to develop products. Genetic engineering (recombinant DNA technology) allows scientists to modify organisms by inserting, deleting, or modifying genes. The answer is '{answer}'."

    # Biologist careers / branches
    if 'biologist' in q or 'biology' in q and 'study' in q:
        return f"Biology is the study of life. Its branches include zoology (animals), botany (plants), ecology (ecosystems), microbiology (microorganisms), genetics (heredity), and many more. The answer is '{answer}'."

    # Agronomist / specific biology careers
    if 'agronomist' in q or 'agronomy' in q:
        return f"An agronomist studies crops and soil science to improve agricultural production, soil management, and sustainable farming practices. The answer is '{answer}'."
    if 'zoologist' in q or 'zoology' in q:
        return f"A zoologist studies animals, their behavior, classification, physiology, and habitats. The answer is '{answer}'."
    if 'ecologist' in q or 'ecology' in q and 'study' in q:
        return f"An ecologist studies the relationships between organisms and their environments, including population dynamics, community interactions, and ecosystems. The answer is '{answer}'."

    # Mendelian genetics (fallback pattern for generic questions)
    if 'mendelian genetics' in q or 'mendel' in q:
        return f"Mendelian genetics describes inheritance patterns based on Gregor Mendel's laws: the Law of Segregation (alleles separate during gamete formation) and the Law of Independent Assortment (genes on different chromosomes sort independently). The answer is '{answer}'."

    # Data definition (standalone short question)
    if q.startswith('data is') or q.startswith('what is data') or (re.search(r'\bdata\b', q) and len(q) < 30):
        return f"Data is information gathered through observation, measurement, or experimentation. It can be quantitative (numerical) or qualitative (descriptive). The answer is '{answer}'."

    # Biology generic fallback questions (circular Q&A patterns in data)
    if re.search(r'what is the main focus of\s+(.+)', q):
        topic = re.search(r'what is the main focus of\s+(.+)', q).group(1).rstrip('?').strip()
        return f"The study of {topic} examines the underlying biological mechanisms and principles that govern this area. Understanding {topic} helps explain how living systems function and interact. The answer is '{answer}'."
    if re.search(r'how is (.+?) best described', q):
        topic = re.search(r'how is (.+?) best described', q).group(1).strip()
        return f"{topic.title()} is a field of biology that explores how organisms develop, function, and maintain life processes through molecular, cellular, and organismal mechanisms. The answer is '{answer}'."
    if re.search(r'what evidence supports our understanding of\s+(.+)', q):
        topic = re.search(r'what evidence supports our understanding of\s+(.+)', q).group(1).rstrip('?').strip()
        return f"Our understanding of {topic} is supported by controlled experiments, molecular analysis, observational studies, and decades of peer-reviewed research. The answer is '{answer}'."
    if re.search(r'how does (.+?) affect living organisms', q):
        topic = re.search(r'how does (.+?) affect living organisms', q).group(1).strip()
        return f"{topic.title()} affects living organisms through changes in cellular processes, gene expression, development, and physiological responses at multiple levels of biological organization. The answer is '{answer}'."
    if re.search(r'what is true about\s+(.+)', q) and ('biology' in course or 'bio' in course):
        topic = re.search(r'what is true about\s+(.+)', q).group(1).rstrip('?').strip()
        return f"{topic.title()} is studied through the scientific method, involving hypothesis testing, controlled experiments, and data analysis to understand biological principles. The answer is '{answer}'."

    # Ecology: energy flow / nutrient cycling / decomposers / biogeochemical cycles
    if 'energy flow' in q and ('ecosystem' in q or 'linear' in q or 'trophic' in q or 'food' in q):
        return f"Energy flows through ecosystems in one direction (sun → producers → consumers → decomposers). Energy is lost as heat at each trophic level (~10% rule), making it linear, not cyclical. The answer is '{answer}'."
    if 'nutrient cycl' in q or 'biogeochemical cycle' in q or 'biogeochemical' in q:
        return f"Nutrient cycles (biogeochemical cycles) are cyclical — matter is recycled through ecosystems. Carbon, nitrogen, phosphorus, and water cycle between living organisms and the abiotic environment. The answer is '{answer}'."
    if 'decomposer' in q and ('role' in q or 'play' in q or 'nutrient' in q or 'cycling' in q):
        return f"Decomposers (bacteria, fungi) break down dead organic matter, returning nutrients to the soil for uptake by producers. They are essential for nutrient recycling in ecosystems. The answer is '{answer}'."
    if ('nutrient' in q and 'cycle' in q and 'cyclical' in q) or ('energy' in q and 'linear' in q):
        return f"Nutrient cycles are cyclical because matter is continuously recycled. Energy flow is linear because energy is lost as heat at each trophic level and cannot be recycled. The answer is '{answer}'."

    # Cell organization order
    if 'order' in q and ('small' in q or 'large' in q or 'least' in q or 'most' in q) and ('cell' in q or 'tissue' in q or 'organ' in q):
        return f"Biological organization from smallest to largest: cell → tissue → organ → organ system → organism. Each level has emergent properties arising from interactions at lower levels. The answer is '{answer}'."

    # ─── AP Biology specific ──────────────────────────────────────────────

    # Negative feedback / homeostasis
    if 'negative feedback' in q or ('feedback' in q and 'homeostasis' in q):
        return f"Negative feedback reverses a change to maintain homeostasis. When a variable deviates from its set point, the system responds to bring it back (e.g., body temperature regulation, blood glucose control). The answer is '{answer}'."
    if 'positive feedback' in q:
        return f"Positive feedback amplifies a change, pushing the system further from equilibrium (e.g., childbirth contractions, blood clotting). It continues until an external factor stops it. The answer is '{answer}'."
    if 'homeostasis' in q:
        return f"Homeostasis is the maintenance of a stable internal environment despite changing external conditions. It relies primarily on negative feedback mechanisms involving receptors, control centers, and effectors. The answer is '{answer}'."

    # Mutation
    if 'mutation' in q:
        return f"Mutations are changes in DNA sequence that can be caused by errors in replication, environmental factors (mutagens), or radiation. They may be harmful, neutral, or beneficial, and are the ultimate source of genetic variation. The answer is '{answer}'."

    # Immune system
    if 'immune' in q or 'antibod' in q or 'antigen' in q or 'pathogen' in q:
        return f"The immune system has innate (nonspecific) and adaptive (specific) components. Adaptive immunity involves B cells (antibodies) and T cells. Memory cells enable faster secondary responses. The answer is '{answer}'."

    # Cell signaling
    if 'cell signal' in q or 'signal transduction' in q:
        return f"Cell signaling involves: (1) reception — a signal molecule binds a receptor, (2) transduction — a cascade of molecular changes, (3) response — the cell's action (gene expression, enzyme activity, etc.). The answer is '{answer}'."

    # Water properties
    if 'water' in q and ('property' in q or 'properties' in q or 'hydrogen bond' in q or 'cohesion' in q):
        return f"Water's unique properties arise from hydrogen bonding: high specific heat, cohesion/adhesion, surface tension, universal solvent, ice floating (less dense as solid). The answer is '{answer}'."

    # Taxonomy / classification
    if 'taxonomy' in q or 'classification' in q or ('domain' in q and ('kingdom' in q or 'phylum' in q)):
        return f"Biological classification organizes life hierarchically: Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species. The three domains are Bacteria, Archaea, and Eukarya. The answer is '{answer}'."

    # Biomolecules
    if 'protein' in q and ('amino acid' in q or 'structure' in q or 'function' in q):
        return f"Proteins are polymers of amino acids linked by peptide bonds. They have four structural levels: primary (sequence), secondary (α-helix/β-sheet), tertiary (3D fold), and quaternary (multi-subunit). The answer is '{answer}'."
    if 'lipid' in q or 'fatty acid' in q:
        return f"Lipids include fats, phospholipids, and steroids. Saturated fatty acids have no double bonds (solid at room temp); unsaturated have double bonds (liquid at room temp). The answer is '{answer}'."
    if 'carbohydrate' in q or 'monosaccharide' in q or 'polysaccharide' in q:
        return f"Carbohydrates include monosaccharides (glucose), disaccharides (sucrose), and polysaccharides (starch, glycogen, cellulose). They serve as energy sources and structural components. The answer is '{answer}'."
    if 'nucleic acid' in q or ('dna' in q and 'rna' in q):
        return f"Nucleic acids (DNA and RNA) are polymers of nucleotides. DNA stores genetic info (double helix, deoxyribose, ATGC). RNA assists in protein synthesis (single-stranded, ribose, AUGC). The answer is '{answer}'."

    # Cell cycle
    if 'cell cycle' in q or 'interphase' in q:
        return f"The cell cycle includes interphase (G1, S, G2 — growth and DNA replication) and the mitotic phase (mitosis + cytokinesis). Checkpoints regulate progression to ensure accurate division. The answer is '{answer}'."

    # Codon / anticodon
    if 'codon' in q or 'anticodon' in q:
        return f"A codon is a three-nucleotide sequence on mRNA that specifies an amino acid (or stop signal). The anticodon on tRNA is complementary to the codon and carries the corresponding amino acid. The answer is '{answer}'."

    # Carbohydrate subtypes (specific patterns)
    if ('glucose' in q or 'fructose' in q or 'galactose' in q) and ('isomer' in q or 'same' in q or 'differ' in q):
        return f"Glucose, fructose, and galactose are structural isomers — they share the molecular formula C₆H₁₂O₆ but differ in the arrangement of atoms, giving them different properties. The answer is '{answer}'."
    if 'starch' in q and ('glycogen' in q or 'cellulose' in q):
        return f"Starch (plant energy storage), glycogen (animal energy storage), and cellulose (plant structural support) are all polysaccharides of glucose but differ in branching and linkage types. The answer is '{answer}'."
    if 'cellulose' in q:
        return f"Cellulose is a structural polysaccharide in plant cell walls. Its β-1,4 glycosidic linkages create straight chains that form rigid fibers via hydrogen bonding. Most animals cannot digest it. The answer is '{answer}'."
    if 'monosaccharide' in q or ('sugar' in q and 'simple' in q):
        return f"Monosaccharides (simple sugars like glucose, fructose, galactose) have the general formula CₙH₂ₙOₙ. They are the building blocks of more complex carbohydrates. The answer is '{answer}'."

    # Diploid / haploid
    if 'diploid' in q or 'haploid' in q or '2n' in q:
        return f"Diploid cells (2n) have two sets of chromosomes (one from each parent). Haploid cells (n) have one set. In humans, diploid = 46 chromosomes, haploid (gametes) = 23. The answer is '{answer}'."

    # Cell membrane / selectively permeable
    if 'cell membrane' in q or 'plasma membrane' in q or 'selectively permeable' in q or 'phospholipid bilayer' in q:
        return f"The cell membrane is a selectively permeable phospholipid bilayer with embedded proteins. Small nonpolar molecules pass freely; ions and large molecules need transport proteins or vesicles. The answer is '{answer}'."

    # Photoperiodism
    if 'photoperiod' in q or ('dark' in q and 'light' in q and ('period' in q or 'hour' in q or 'flower' in q or 'plant' in q)):
        return f"Photoperiodism is the response of organisms to the length of day and night. In plants, flowering is triggered by the critical night length using the phytochrome system. The answer is '{answer}'."

    # Crossing over / recombination
    if 'crossing over' in q or 'recombination' in q:
        return f"Crossing over occurs during prophase I of meiosis when homologous chromosomes exchange segments, creating new combinations of alleles and increasing genetic variation. The answer is '{answer}'."

    # DNA base pairing
    if 'base pair' in q or ('bases' in q and 'pair' in q) or ('adenine' in q and ('thymine' in q or 'uracil' in q)):
        return f"In DNA, adenine (A) pairs with thymine (T) and guanine (G) pairs with cytosine (C) through hydrogen bonds. In RNA, uracil (U) replaces thymine. This is Chargaff's rule. The answer is '{answer}'."

    # DNA structure
    if 'dna' in q and ('structure' in q or 'double helix' in q or 'watson' in q or 'crick' in q):
        return f"DNA has a double helix structure, discovered by Watson, Crick, and Franklin (1953). Two antiparallel sugar-phosphate backbones are connected by complementary base pairs (A-T, G-C). The answer is '{answer}'."

    # Nuclear envelope
    if 'nuclear envelope' in q or 'nuclear membrane' in q:
        return f"The nuclear envelope is a double membrane surrounding the nucleus, with nuclear pores that regulate transport of molecules (mRNA, proteins) between the nucleus and cytoplasm. The answer is '{answer}'."

    # ATP
    if 'atp' in q and ('energy' in q or 'currency' in q or 'cell' in q or 'phosphate' in q):
        return f"ATP (adenosine triphosphate) is the cell's primary energy currency. Energy is stored in high-energy phosphate bonds and released when ATP is hydrolyzed to ADP + Pi for cellular work. The answer is '{answer}'."

    # Hardy-Weinberg
    if 'hardy-weinberg' in q or 'hardy weinberg' in q or ('allele' in q and 'frequency' in q):
        return f"Under Hardy-Weinberg equilibrium, p² + 2pq + q² = 1 and p + q = 1, where p and q are allele frequencies. Deviations indicate evolution is occurring. The answer is '{answer}'."

    # Natural selection / evolution
    if 'natural selection' in q:
        return f"Natural selection acts on phenotypic variation within a population. Individuals with traits better suited to their environment have higher fitness (reproductive success), passing those traits to offspring. The answer is '{answer}'."
    if 'evolution' in q and ('evidence' in q or 'support' in q):
        return f"Evidence for evolution includes the fossil record, comparative anatomy (homologous and vestigial structures), molecular biology (DNA/protein similarities), biogeography, and direct observation. The answer is '{answer}'."
    if 'speciation' in q:
        return f"Speciation occurs when populations become reproductively isolated. Allopatric speciation involves geographic barriers; sympatric speciation occurs without physical separation. The answer is '{answer}'."

    # Genetics
    if 'genotype' in q or 'phenotype' in q:
        return f"Genotype is the genetic makeup (alleles) of an organism, while phenotype is the observable traits expressed by those genes in a given environment. The answer is '{answer}'."
    if 'dominant' in q and 'recessive' in q:
        return f"A dominant allele is expressed in heterozygotes (one copy is sufficient), while a recessive allele is only expressed in homozygotes (two copies needed). The answer is '{answer}'."
    if 'punnett square' in q or 'cross' in q and ('offspring' in q or 'ratio' in q):
        return f"A Punnett square predicts the offspring genotype/phenotype ratios from a genetic cross by combining all possible gamete combinations. The answer is '{answer}'."

    # Photosynthesis
    if 'photosynthesis' in q:
        return f"Photosynthesis converts light energy to chemical energy: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂. The light reactions occur in the thylakoids, the Calvin cycle in the stroma. The answer is '{answer}'."
    # Cellular respiration
    if 'cellular respiration' in q or 'aerobic respiration' in q:
        return f"Cellular respiration breaks down glucose to produce ATP: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP. It includes glycolysis, the Krebs cycle, and the electron transport chain. The answer is '{answer}'."
    if 'glycolysis' in q:
        return f"Glycolysis occurs in the cytoplasm, splitting one glucose molecule into two pyruvate molecules, producing a net gain of 2 ATP and 2 NADH. It does not require oxygen. The answer is '{answer}'."
    if 'krebs cycle' in q or 'citric acid cycle' in q:
        return f"The Krebs cycle occurs in the mitochondrial matrix. Acetyl-CoA is oxidized, producing CO₂, NADH, FADH₂, and ATP (GTP). It completes the oxidation of glucose. The answer is '{answer}'."
    if 'electron transport chain' in q or 'etc' == q.split()[-1] or 'oxidative phosphorylation' in q:
        return f"The electron transport chain in the inner mitochondrial membrane uses NADH and FADH₂ to create a proton gradient, which drives ATP synthase to produce the majority of ATP (~30-32 per glucose). The answer is '{answer}'."
    if 'fermentation' in q:
        return f"Fermentation is an anaerobic process that regenerates NAD⁺ so glycolysis can continue without oxygen. Lactic acid fermentation produces lactate; alcoholic fermentation produces ethanol and CO₂. The answer is '{answer}'."

    # Cell structure
    if 'mitochondri' in q:
        return f"Mitochondria are the 'powerhouse of the cell' — they perform cellular respiration to produce ATP. They have a double membrane, their own DNA, and are thought to have originated through endosymbiosis. The answer is '{answer}'."
    if 'chloroplast' in q:
        return f"Chloroplasts are the site of photosynthesis in plant and algae cells. They contain thylakoids (where light reactions occur) and stroma (where the Calvin cycle occurs). The answer is '{answer}'."
    if 'endoplasmic reticulum' in q or ' er ' in q:
        return f"The rough ER (with ribosomes) synthesizes and processes proteins; the smooth ER synthesizes lipids and detoxifies substances. The answer is '{answer}'."
    if 'golgi' in q:
        return f"The Golgi apparatus modifies, packages, and sorts proteins and lipids received from the ER, then ships them to their final destinations via vesicles. The answer is '{answer}'."
    if 'prokaryot' in q and 'eukaryot' in q:
        return f"Prokaryotes lack a membrane-bound nucleus and organelles (bacteria, archaea). Eukaryotes have a nucleus and membrane-bound organelles (plants, animals, fungi, protists). The answer is '{answer}'."

    # Enzymes
    if 'enzyme' in q or 'substrate' in q or 'active site' in q:
        return f"Enzymes are biological catalysts that lower activation energy. They bind substrates at the active site with high specificity. Factors like temperature, pH, and concentration affect enzyme activity. The answer is '{answer}'."

    # Population ecology
    if 'carrying capacity' in q or 'logistic growth' in q:
        return f"Logistic growth follows an S-shaped curve where population growth slows as it approaches carrying capacity (K), the maximum population an environment can sustain. The answer is '{answer}'."
    if 'exponential growth' in q:
        return f"Exponential growth (J-shaped curve) occurs when resources are unlimited and the population grows at a constant rate. The growth rate equation is dN/dt = rN, where r is the per-capita growth rate. The answer is '{answer}'."
    if 'limiting factor' in q or 'density-dependent' in q or 'density dependent' in q:
        return f"Density-dependent limiting factors (disease, competition, predation) intensify as population size increases, while density-independent factors (weather, natural disasters) affect populations regardless of size. The answer is '{answer}'."
    if 'density-independent' in q or 'density independent' in q:
        return f"Density-independent factors (weather, natural disasters, climate) affect populations regardless of their size, unlike density-dependent factors that intensify with population density. The answer is '{answer}'."

    # ─── AP Chemistry specific ────────────────────────────────────────────

    # Isotopes / atomic number / mass number / subatomic particles
    if 'isotope' in q:
        return f"Isotopes are atoms of the same element with different numbers of neutrons (same atomic number, different mass number). They have identical chemical properties but different masses. The answer is '{answer}'."
    if 'atomic number' in q:
        return f"The atomic number (Z) equals the number of protons in the nucleus. It defines the element's identity and determines its position on the periodic table. The answer is '{answer}'."
    if 'mass number' in q:
        return f"The mass number (A) equals the total number of protons + neutrons in the nucleus. Isotopes differ in mass number. A = Z + N. The answer is '{answer}'."
    if ('proton' in q or 'neutron' in q or 'electron' in q) and ('number' in q or 'charge' in q or 'mass' in q or 'locate' in q):
        return f"Protons (+1 charge, in nucleus) determine element identity. Neutrons (0 charge, in nucleus) add mass. Electrons (-1 charge, in orbitals) determine chemical behavior. The answer is '{answer}'."

    # General equilibrium (broader than constant/expression patterns)
    if 'equilibrium' in q and ('reach' in q or 'reversible' in q or 'shift' in q or 'favor' in q):
        return f"Chemical equilibrium is a dynamic state where the forward and reverse reaction rates are equal, so concentrations remain constant (not necessarily equal). Le Chatelier's principle predicts shifts. The answer is '{answer}'."

    # Brønsted-Lowry acid/base
    if 'brønsted' in q or 'bronsted' in q or 'br\\u00f8nsted' in q or ('acid' in q and 'proton' in q and ('donate' in q or 'accept' in q)):
        return f"A Brønsted-Lowry acid donates a proton (H⁺) and a base accepts a proton. Every acid-base reaction involves a conjugate acid-base pair. The answer is '{answer}'."

    # Hydrogen bonding (general)
    if 'hydrogen bond' in q or 'hydrogen bonding' in q:
        return f"Hydrogen bonding occurs when H is bonded to a highly electronegative atom (F, O, or N) and attracted to a lone pair on another F, O, or N. H-F bonds are strongest. The answer is '{answer}'."

    # Balanced chemical equation
    if 'balanced' in q and ('equation' in q or 'chemical' in q or 'reaction' in q):
        return f"A balanced chemical equation has equal numbers of each type of atom on both sides, satisfying the law of conservation of mass. Adjust coefficients (not subscripts) to balance. The answer is '{answer}'."

    # ΔH / phase change temperature calculations
    if re.search(r'δh|Δh|delta h|hfus|hvap', q, re.IGNORECASE) or ('temperature' in q and ('solid' in q or 'liquid' in q or 'phase' in q)):
        return f"For phase transitions, ΔG = 0 at the transition temperature: T = ΔH/ΔS. Use consistent units (convert kJ to J or vice versa). The answer is '{answer}'."

    # Molecular formula / isomers
    if 'molecular formula' in q or ('isomer' in q and ('structural' in q or 'same' in q)):
        return f"Isomers share the same molecular formula but differ in structure (structural isomers) or spatial arrangement (stereoisomers). Different structures give different properties. The answer is '{answer}'."

    # Ion / ionic compound properties
    if 'ion' in q and ('positive' in q or 'negative' in q or 'cation' in q or 'anion' in q):
        return f"Cations are positive ions (formed by losing electrons); anions are negative ions (formed by gaining electrons). Metals typically form cations; nonmetals form anions. The answer is '{answer}'."

    # Electronegativity
    if 'electronegativity' in q:
        return f"Electronegativity measures an atom's ability to attract shared electrons. It increases across a period (left→right) and up a group. Fluorine is the most electronegative element. The answer is '{answer}'."

    # Ionization energy
    if 'ionization energy' in q:
        return f"Ionization energy is the energy required to remove an electron from a gaseous atom. It generally increases across a period and up a group. The answer is '{answer}'."

    # Atomic radius
    if 'atomic radius' in q:
        return f"Atomic radius decreases across a period (more protons pull electrons closer) and increases down a group (more electron shells). The answer is '{answer}'."

    # Rate law / reaction rate
    if 'rate law' in q or 'rate constant' in q or 'reaction rate' in q or 'rate of reaction' in q:
        return f"The rate law Rate = k[A]ᵐ[B]ⁿ is determined experimentally. The exponents (m, n) are the reaction orders; they don't necessarily match stoichiometric coefficients. k is the rate constant. The answer is '{answer}'."

    # Reaction mechanism
    if 'mechanism' in q and ('step' in q or 'rate' in q or 'reaction' in q):
        return f"A reaction mechanism is a series of elementary steps. The slowest step (rate-determining step) controls the overall rate. Intermediates are produced and consumed. The answer is '{answer}'."

    # Bond energy / bond strength
    if 'bond' in q and ('energy' in q or 'strength' in q or 'stronger' in q or 'weaker' in q):
        return f"Bond energy is the energy needed to break a bond. Shorter bonds are generally stronger. Triple > double > single bond strength. ΔH_rxn ≈ Σ(bonds broken) - Σ(bonds formed). The answer is '{answer}'."

    # Solubility
    if 'solubility' in q or 'soluble' in q or 'dissolve' in q:
        return f"Solubility follows 'like dissolves like': polar/ionic solutes dissolve in polar solvents; nonpolar solutes dissolve in nonpolar solvents. Temperature and pressure also affect solubility. The answer is '{answer}'."

    # Phase change
    if 'phase change' in q or 'boiling point' in q or 'melting point' in q or 'phase diagram' in q:
        return f"Phase changes (solid↔liquid↔gas) depend on temperature and pressure. Stronger intermolecular forces give higher melting/boiling points. At the triple point, all three phases coexist. The answer is '{answer}'."

    # Sublimation / deposition
    if 'sublimation' in q:
        return f"Sublimation is the phase change from solid directly to gas, skipping the liquid phase (e.g., dry ice, frost disappearing). It requires energy input. The answer is '{answer}'."
    if 'deposition' in q:
        return f"Deposition is the phase change from gas directly to solid, skipping the liquid phase (e.g., frost forming, snow). It releases energy. The answer is '{answer}'."

    # Plasma
    if 'plasma' in q and ('state' in q or 'gas' in q or 'ionize' in q or 'energy' in q or 'matter' in q):
        return f"Plasma is the fourth state of matter, formed when a gas gains enough energy to ionize its atoms (strip electrons). It consists of free-moving ions and electrons. Examples: stars, lightning, neon signs. The answer is '{answer}'."

    # Density (concept)
    if 'density' in q and ('float' in q or 'sink' in q or 'less than' in q or 'greater than' in q or 'water' in q):
        return f"Density = mass/volume. Objects with density less than the surrounding fluid float; denser objects sink. Water's density at standard conditions is 1 g/mL. The answer is '{answer}'."
    if q.startswith('what is the density') or q.startswith('what is density') or 'density of water' in q:
        return f"Density is the ratio of mass to volume (d = m/v). Water's density is 1 g/mL (or 1 g/cm³) at standard conditions. The answer is '{answer}'."
    if 'density' in q and ('highest' in q or 'lowest' in q or 'most' in q or 'least' in q):
        return f"Density = mass/volume. Materials with tightly packed, heavy atoms (like lead, gold) have higher density. Gases are least dense; solids are typically densest. The answer is '{answer}'."

    # Molecular motion / temperature relationship
    if ('molecular motion' in q or 'molecule' in q and 'motion' in q) or ('kinetic energy' in q and 'temperature' in q):
        return f"Temperature is a measure of the average kinetic energy of molecules. As temperature increases, molecular motion increases (molecules move faster and more vigorously). The answer is '{answer}'."
    if 'temperature' in q and ('increase' in q or 'decrease' in q) and ('motion' in q or 'kinetic' in q or 'speed' in q):
        return f"Temperature directly relates to molecular motion. Higher temperature means faster molecular movement (greater kinetic energy); lower temperature means slower movement. The answer is '{answer}'."

    # States of matter (general)
    if ('solid' in q or 'liquid' in q or 'gas' in q) and ('property' in q or 'properties' in q or 'characteristic' in q):
        return f"Solids have fixed shape and volume (particles vibrate in place). Liquids have fixed volume but take the shape of their container. Gases expand to fill any container. The answer is '{answer}'."

    # Physical vs chemical property/change
    if 'physical property' in q or ('physical' in q and 'property' in q):
        return f"Physical properties can be observed without changing the substance's identity: color, density, melting/boiling point, hardness, malleability, luster. The answer is '{answer}'."
    if 'chemical property' in q or ('chemical' in q and 'property' in q):
        return f"Chemical properties describe a substance's ability to undergo chemical change: flammability, reactivity, toxicity, ability to rust/tarnish. They can only be observed by changing the substance. The answer is '{answer}'."
    if 'physical change' in q or ('physical' in q and 'change' in q and ('example' in q or 'which' in q)):
        return f"Physical changes alter form or appearance without changing chemical composition: melting, freezing, dissolving, cutting, phase changes. The substance's identity remains the same. The answer is '{answer}'."
    if 'chemical change' in q or ('chemical' in q and 'change' in q and ('example' in q or 'sign' in q or 'evidence' in q or 'which' in q)):
        return f"Chemical changes produce new substances: burning, rusting, cooking, decomposition. Signs include gas production, color change, temperature change, precipitate formation, and new odor. The answer is '{answer}'."
    if 'malleab' in q or 'ductil' in q:
        return f"Malleability (can be hammered into sheets) and ductility (can be drawn into wires) are physical properties characteristic of metals. The answer is '{answer}'."

    # Formula for density (when asked as text, not calculation)
    if 'formula for density' in q or 'density formula' in q:
        return f"The formula for density is d = m/v (density = mass ÷ volume). Units are typically g/mL or g/cm³. Rearrange to find mass (m = d·v) or volume (v = m/d). The answer is '{answer}'."

    # Lewis structure / dot structure
    if 'lewis' in q and ('structure' in q or 'dot' in q):
        return f"Lewis structures show valence electrons as dots/lines. Follow the octet rule (8 electrons around most atoms, 2 for H). Count total valence electrons, connect atoms with bonds, then distribute remaining electrons. The answer is '{answer}'."

    # Equilibrium
    if 'equilibrium' in q and ('constant' in q or 'expression' in q or 'keq' in q or 'kc' in q or 'kp' in q):
        return f"The equilibrium constant (K) equals the ratio of product concentrations to reactant concentrations, each raised to their stoichiometric coefficients. K > 1 favors products; K < 1 favors reactants. The answer is '{answer}'."
    if "le chatelier" in q or 'lechatelier' in q:
        return f"Le Chatelier's Principle states that a system at equilibrium will shift to counteract any applied stress (changes in concentration, pressure, or temperature). The answer is '{answer}'."

    # Stoichiometry
    if 'limiting reagent' in q or 'limiting reactant' in q:
        return f"The limiting reagent is the reactant completely consumed first, determining the maximum product formed. Calculate moles of product from each reactant; the one giving less product is limiting. The answer is '{answer}'."
    if 'molar mass' in q:
        return f"Molar mass is the mass of one mole of a substance (g/mol), found by summing the atomic masses of all atoms in the formula. The answer is '{answer}'."
    if 'stoichiometr' in q:
        return f"Stoichiometry uses mole ratios from balanced equations to calculate reactant/product quantities. Convert between grams, moles, and particles using molar mass and Avogadro's number. The answer is '{answer}'."

    # Thermodynamics
    if 'entropy' in q:
        return f"Entropy (S) measures disorder/randomness. Entropy increases when: solids→liquids→gases, solutions form, temperature increases, or the number of particles increases. The answer is '{answer}'."
    if 'enthalpy' in q or 'exothermic' in q or 'endothermic' in q:
        return f"Enthalpy (ΔH) measures heat flow at constant pressure. Exothermic reactions release heat (ΔH < 0); endothermic reactions absorb heat (ΔH > 0). The answer is '{answer}'."
    if 'thermodynamic' in q:
        if 'first law' in q:
            return f"The First Law of Thermodynamics: energy is conserved. ΔU = q + w (internal energy change = heat + work). Energy can be transferred but not created or destroyed. The answer is '{answer}'."
        if 'second law' in q:
            return f"The Second Law of Thermodynamics: the total entropy of an isolated system always increases. Heat flows spontaneously from hot to cold, never the reverse. The answer is '{answer}'."
        if 'third law' in q:
            return f"The Third Law of Thermodynamics: the entropy of a perfect crystal at absolute zero (0 K) is exactly zero. The answer is '{answer}'."
        return f"Thermodynamics studies energy transformations. Key concepts: ΔG = ΔH - TΔS determines spontaneity, ΔH indicates heat flow, and ΔS indicates entropy change. The answer is '{answer}'."
    if 'heat' in q and ('transfer' in q or 'capacity' in q or 'specific' in q):
        return f"Heat transfer occurs by conduction (contact), convection (fluid movement), and radiation (electromagnetic waves). Specific heat capacity (c) is the energy needed to raise 1 g by 1°C: q = mcΔT. The answer is '{answer}'."

    # Acid/base (standalone)
    if 'acid' in q and ('strong' in q or 'weak' in q or 'dissociat' in q or 'ioniz' in q):
        return f"Strong acids completely dissociate in water (HCl, HNO₃, H₂SO₄); weak acids partially dissociate (HF, CH₃COOH). Ka measures acid strength — larger Ka means stronger acid. The answer is '{answer}'."
    if ('buffer' in q) and ('solution' in q or 'ph' in q.split() or 'acid' in q):
        return f"A buffer solution resists pH changes by containing a weak acid and its conjugate base (or weak base and its conjugate acid). Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA]). The answer is '{answer}'."

    # Periodic table / element properties
    if 'periodic table' in q or 'periodic trend' in q:
        return f"The periodic table organizes elements by atomic number with similar properties in columns (groups). Trends include atomic radius, ionization energy, electronegativity, and electron affinity. The answer is '{answer}'."
    if 'valence electron' in q:
        return f"Valence electrons are the outermost electrons that participate in bonding. The group number indicates valence electrons for main-group elements (e.g., Group 1 → 1 valence electron). The answer is '{answer}'."

    # Gas laws
    if 'ideal gas' in q or 'pv = nrt' in q or 'pv=nrt' in q:
        return f"The ideal gas law PV = nRT relates pressure (P), volume (V), moles (n), and temperature (T). R is the gas constant. Real gases approximate ideal behavior at high T and low P. The answer is '{answer}'."
    if ("boyle" in q or "charles" in q or "avogadro" in q or "dalton" in q) and ('law' in q or 'gas' in q):
        return f"Boyle's Law: P₁V₁ = P₂V₂ (inverse P-V at constant T). Charles's Law: V₁/T₁ = V₂/T₂ (direct V-T at constant P). Dalton's Law: total pressure = sum of partial pressures. The answer is '{answer}'."

    # Electron configuration / orbitals
    if 'electron configuration' in q or 'orbital' in q:
        return f"Electrons fill orbitals following the Aufbau principle (lowest energy first), Pauli exclusion principle (max 2 electrons per orbital), and Hund's rule (fill degenerate orbitals singly before pairing). The answer is '{answer}'."

    # VSEPR / molecular geometry
    if 'vsepr' in q or 'molecular geometry' in q or 'molecular shape' in q:
        return f"VSEPR theory predicts molecular geometry based on minimizing electron pair repulsion around the central atom. Lone pairs occupy more space than bonding pairs, affecting bond angles. The answer is '{answer}'."

    # Intermolecular forces
    if 'intermolecular force' in q or 'van der waals' in q or 'london dispersion' in q or 'dipole' in q:
        return f"Intermolecular forces (weakest to strongest): London dispersion forces (all molecules) < dipole-dipole (polar molecules) < hydrogen bonding (H bonded to N, O, or F). They affect boiling point, viscosity, and surface tension. The answer is '{answer}'."

    # Oxidation / reduction
    if 'oxidation' in q or 'reduction' in q or 'redox' in q:
        return f"In redox reactions, oxidation is loss of electrons (increase in oxidation number) and reduction is gain of electrons (decrease in oxidation number). OIL RIG: Oxidation Is Loss, Reduction Is Gain. The answer is '{answer}'."

    # ─── AP Environmental Science ─────────────────────────────────────────

    # Ecological succession
    if 'succession' in q:
        if 'primary' in q:
            return f"Primary succession begins on barren surfaces (bare rock, new lava) where no soil exists. Pioneer species (lichens, mosses) colonize first, gradually building soil for later species. The answer is '{answer}'."
        if 'secondary' in q:
            return f"Secondary succession occurs after a disturbance (fire, flood) in an area that still has soil. It progresses faster than primary succession because soil and seed banks remain. The answer is '{answer}'."
        return f"Ecological succession is the gradual change in species composition over time. Primary succession starts on bare surfaces; secondary succession occurs after disturbances. Both trend toward a climax community. The answer is '{answer}'."

    # Biome
    if 'biome' in q:
        return f"Biomes are large geographic regions with distinct climates and characteristic organisms. Major biomes include tropical rainforest, desert, grassland, temperate deciduous forest, taiga, and tundra. The answer is '{answer}'."

    # Pollution types
    if 'pollution' in q and ('water' in q or 'air' in q or 'soil' in q or 'source' in q):
        return f"Point source pollution comes from a single identifiable source (factory pipe, sewage outlet). Nonpoint source pollution comes from diffuse origins (agricultural runoff, urban stormwater). The answer is '{answer}'."

    # Invasive species
    if 'invasive' in q:
        return f"Invasive species are non-native organisms that spread rapidly in new environments, often outcompeting native species due to lack of natural predators or competitors. They can devastate ecosystems and biodiversity. The answer is '{answer}'."

    # Soil
    if 'soil' in q and ('horizon' in q or 'layer' in q or 'erosion' in q or 'composition' in q):
        return f"Soil has layers (horizons): O (organic), A (topsoil), B (subsoil), C (parent material), R (bedrock). Soil formation depends on climate, organisms, relief, parent material, and time (CLORPT). The answer is '{answer}'."

    # Sustainability
    if 'sustainability' in q or 'sustainable development' in q:
        return f"Sustainable development meets present needs without compromising future generations' ability to meet theirs. It balances economic growth, environmental protection, and social equity. The answer is '{answer}'."

    # Water cycle details
    if 'aquifer' in q or 'groundwater' in q:
        return f"Aquifers are underground layers of permeable rock or sediment that store groundwater. Water enters through infiltration and is extracted via wells. They are critical freshwater reservoirs. The answer is '{answer}'."
    if 'watershed' in q:
        return f"A watershed is an area of land where all precipitation drains to a common water body (river, lake, ocean). Watersheds are separated by ridgelines. The answer is '{answer}'."
    if 'water' in q and ('return' in q or 'atmosphere' in q or 'evaporat' in q or 'precipitat' in q or 'transpir' in q):
        return f"Water returns to the atmosphere through evaporation (from water surfaces), transpiration (from plants), and sublimation (ice to vapor). Precipitation (rain, snow) returns water to the surface. The answer is '{answer}'."
    if 'residence time' in q:
        return f"Residence time is the average time a substance spends in a particular reservoir. For water: oceans have long residence time (∼3,000 years), atmosphere short (∼9 days). The answer is '{answer}'."

    # Global warming / climate change
    if 'global warming' in q or 'climate change' in q:
        return f"Global warming is primarily caused by increased greenhouse gas emissions (CO₂, CH₄) from burning fossil fuels, deforestation, and agriculture. This enhances the greenhouse effect, raising average temperatures. The answer is '{answer}'."
    if 'carbon dioxide' in q or 'co2' in q or 'co₂' in q:
        return f"CO₂ is a major greenhouse gas released by fossil fuel combustion, deforestation, and cement production. It's absorbed by photosynthesis and the oceans. Rising CO₂ levels drive climate change. The answer is '{answer}'."

    # Deforestation
    if 'deforestation' in q:
        return f"Deforestation reduces carbon sinks, decreases biodiversity, accelerates soil erosion, and disrupts water cycles. Tropical deforestation is a major contributor to greenhouse gas emissions. The answer is '{answer}'."

    # Endangered species / conservation
    if 'endangered' in q or 'conservation' in q:
        return f"Endangered species face risk of extinction due to habitat loss, overexploitation, pollution, invasive species, and climate change. Conservation efforts include habitat protection, breeding programs, and legislation. The answer is '{answer}'."

    if 'biodiversity' in q:
        return f"Biodiversity refers to the variety of life at genetic, species, and ecosystem levels. Greater biodiversity generally increases ecosystem resilience and stability. The answer is '{answer}'."
    if 'greenhouse' in q and ('effect' in q or 'gas' in q):
        return f"Greenhouse gases (CO₂, CH₄, N₂O, H₂O vapor) trap infrared radiation in the atmosphere, warming Earth's surface. Human activities have increased these gases, intensifying the natural greenhouse effect. The answer is '{answer}'."
    if 'ozone' in q:
        return f"Stratospheric ozone (O₃) absorbs harmful UV radiation. CFCs and other pollutants catalytically destroy ozone. The Montreal Protocol successfully reduced CFC emissions. The answer is '{answer}'."
    if 'renewable' in q and 'energy' in q:
        return f"Renewable energy sources (solar, wind, hydroelectric, geothermal, biomass) are replenished naturally and produce fewer greenhouse gas emissions than fossil fuels. The answer is '{answer}'."
    if 'fossil fuel' in q:
        return f"Fossil fuels (coal, oil, natural gas) are non-renewable energy sources formed from ancient organisms over millions of years. Their combustion releases CO₂ and other pollutants. The answer is '{answer}'."
    if 'eutrophication' in q:
        return f"Eutrophication occurs when excess nutrients (nitrogen, phosphorus) enter water bodies, causing algal blooms. When algae die and decompose, oxygen is depleted, creating dead zones. The answer is '{answer}'."
    if 'water cycle' in q or 'hydrologic' in q:
        return f"The water cycle includes evaporation, transpiration, condensation, precipitation, and runoff. Water moves between the atmosphere, surface water, groundwater, and oceans. The answer is '{answer}'."
    if 'nitrogen cycle' in q:
        return f"The nitrogen cycle converts N₂ gas to usable forms via nitrogen fixation (by bacteria), nitrification, assimilation, ammonification, and denitrification. The answer is '{answer}'."
    if 'carbon cycle' in q:
        return f"Carbon cycles through the atmosphere (CO₂), biosphere (photosynthesis/respiration), hydrosphere (dissolved CO₂), and lithosphere (fossil fuels, limestone). The answer is '{answer}'."

    # ─── AP Physics ───────────────────────────────────────────────────────

    # Projectile motion
    if 'projectile' in q:
        return f"In projectile motion (ignoring air resistance): horizontal velocity stays constant (a_x = 0), vertical acceleration = g = 9.8 m/s² downward. Range is maximized at 45°. Use kinematics equations for each component independently. The answer is '{answer}'."

    # Friction
    if 'friction' in q:
        if 'static' in q:
            return f"Static friction prevents motion: f_s ≤ μ_s·N. It adjusts up to its maximum value (μ_s·N). Static friction coefficient is always ≥ kinetic. The answer is '{answer}'."
        if 'kinetic' in q or 'coefficient' in q:
            return f"Kinetic friction opposes motion: f_k = μ_k·N, where μ_k is the kinetic friction coefficient and N is the normal force. The answer is '{answer}'."
        return f"Friction opposes relative motion between surfaces. Static friction (f_s ≤ μ_s·N) prevents motion; kinetic friction (f_k = μ_k·N) opposes motion. The answer is '{answer}'."

    # Kinematics equations
    if 'kinematics' in q or ('constant acceleration' in q) or ('uniformly accelerat' in q):
        return f"The kinematic equations for constant acceleration: v = v₀ + at, x = x₀ + v₀t + ½at², v² = v₀² + 2a(x - x₀). The answer is '{answer}'."

    # Free fall
    if 'free fall' in q or ('drop' in q and ('height' in q or 'ground' in q or 'fall' in q)):
        return f"In free fall, all objects accelerate at g = 9.8 m/s² regardless of mass (ignoring air resistance). Use kinematics with a = g. The answer is '{answer}'."

    # Vectors
    if 'vector' in q and ('scalar' in q or 'magnitude' in q or 'direction' in q):
        return f"Vectors have both magnitude and direction (velocity, force, acceleration). Scalars have only magnitude (speed, mass, energy). Vectors can be decomposed into perpendicular components. The answer is '{answer}'."

    # Free body diagram / net force
    if 'free body' in q or 'net force' in q:
        return f"A free body diagram shows all forces acting on an object. The net force (vector sum) determines acceleration via F_net = ma. If F_net = 0, the object is in equilibrium. The answer is '{answer}'."

    # Equilibrium (physics)
    if 'equilibrium' in q and ('force' in q or 'object' in q or 'rest' in q):
        return f"An object is in mechanical equilibrium when the net force is zero (ΣF = 0). For static equilibrium, it's also at rest. For translational equilibrium, velocity is constant. The answer is '{answer}'."

    # Collision
    if 'collision' in q or 'collide' in q:
        if 'elastic' in q and 'inelastic' not in q:
            return f"In an elastic collision, both momentum AND kinetic energy are conserved. Objects bounce off each other. The answer is '{answer}'."
        if 'inelastic' in q:
            return f"In an inelastic collision, momentum is conserved but kinetic energy is not. In a perfectly inelastic collision, the objects stick together: m₁v₁ + m₂v₂ = (m₁+m₂)v_f. The answer is '{answer}'."
        return f"In all collisions, total momentum is conserved (in an isolated system). Elastic collisions also conserve kinetic energy; inelastic do not. The answer is '{answer}'."

    # Hooke's law / springs
    if 'spring' in q or "hooke's" in q or 'hooke' in q:
        return f"Hooke's Law: F = -kx, where k is the spring constant and x is displacement from equilibrium. Elastic PE = ½kx². The answer is '{answer}'."

    # Coulomb's law / electric charge
    if 'coulomb' in q or ('charge' in q and ('force' in q or 'between' in q)):
        return f"Coulomb's Law: F = kq₁q₂/r², where k = 8.99×10⁹ N·m²/C². Like charges repel; opposite charges attract. Force varies inversely with distance squared. The answer is '{answer}'."

    # Gravitational force
    if 'gravitational' in q and ('force' in q or 'field' in q or 'acceleration' in q):
        return f"Gravitational force: F = Gm₁m₂/r² (universal gravitation). Near Earth's surface, F = mg with g ≈ 9.8 m/s². Gravitational PE = mgh. The answer is '{answer}'."

    # Power
    if 'power' in q and ('energy' in q or 'work' in q or 'watt' in q or 'rate' in q):
        return f"Power is the rate of doing work: P = W/t = Fv. It measures how quickly energy is transferred. Measured in watts (W = J/s). The answer is '{answer}'."

    # Circular motion
    if 'circular motion' in q or 'orbit' in q:
        return f"For uniform circular motion, the object moves at constant speed in a circle. Centripetal acceleration a_c = v²/r points toward the center. The centripetal force provides this acceleration. The answer is '{answer}'."

    if 'momentum' in q and 'conservation' in q:
        return f"The law of conservation of momentum states that in an isolated system (no external forces), total momentum before = total momentum after a collision or interaction: Σp_initial = Σp_final. The answer is '{answer}'."
    if 'impulse' in q:
        return f"Impulse (J) equals the change in momentum: J = FΔt = Δp. A larger force or longer contact time produces a greater impulse. The answer is '{answer}'."
    if 'centripetal' in q:
        return f"Centripetal acceleration points toward the center of circular motion: a_c = v²/r. The centripetal force F_c = mv²/r is provided by gravity, tension, friction, or other forces. The answer is '{answer}'."
    if 'torque' in q:
        return f"Torque (τ) = r × F × sin(θ), the rotational equivalent of force. It measures the tendency to cause rotation about an axis. Net torque = Iα (moment of inertia × angular acceleration). The answer is '{answer}'."
    if 'work-energy' in q or ('work' in q and 'kinetic' in q):
        return f"The work-energy theorem states that the net work done on an object equals its change in kinetic energy: W_net = ΔKE = ½mv² - ½mv₀². The answer is '{answer}'."
    if 'conservation of energy' in q:
        return f"The law of conservation of energy states that energy cannot be created or destroyed, only transformed. In a closed system, total energy (KE + PE + other forms) remains constant. The answer is '{answer}'."
    if 'electric field' in q:
        return f"An electric field E exerts force on charges: F = qE. The field points away from positive charges and toward negative charges. Field strength: E = kQ/r² (point charge). The answer is '{answer}'."
    if 'magnetic field' in q or 'magnetic force' in q:
        return f"A magnetic force acts on moving charges: F = qv × B. The direction follows the right-hand rule. Current-carrying wires create magnetic fields and experience forces in external fields. The answer is '{answer}'."
    if 'wave' in q and ('frequency' in q or 'wavelength' in q or 'amplitude' in q):
        return f"Wave properties: v = fλ (velocity = frequency × wavelength). Amplitude determines energy/intensity. Frequency and wavelength are inversely related at constant wave speed. The answer is '{answer}'."
    if 'refraction' in q or "snell's law" in q:
        return f"Snell's Law: n₁sin(θ₁) = n₂sin(θ₂). Light bends toward the normal when entering a denser medium (higher index of refraction) and away from normal when entering a less dense medium. The answer is '{answer}'."
    if 'capacitor' in q or 'capacitance' in q:
        return f"Capacitance C = Q/V measures a capacitor's ability to store charge. For parallel plates: C = ε₀A/d. Energy stored: U = ½CV². The answer is '{answer}'."
    if 'resistance' in q and ('series' in q or 'parallel' in q):
        return f"Resistors in series: R_total = R₁ + R₂ + ... (currents equal, voltages add). In parallel: 1/R_total = 1/R₁ + 1/R₂ + ... (voltages equal, currents add). The answer is '{answer}'."

    # Circuit (general)
    if 'circuit' in q:
        if 'series' in q:
            return f"In a series circuit, components share one path for current. Current is the same throughout; voltage divides across components. Total resistance adds: R_total = R₁ + R₂ + ... The answer is '{answer}'."
        if 'parallel' in q:
            return f"In a parallel circuit, components have multiple paths. Voltage is the same across all branches; current divides. 1/R_total = 1/R₁ + 1/R₂ + ... The answer is '{answer}'."
        return f"Electric circuits provide a path for current flow. Voltage (V) drives current (I) through resistance (R). Ohm's Law: V = IR. Power: P = IV = I²R = V²/R. The answer is '{answer}'."

    # Velocity / speed / acceleration (broad physics)
    if ('velocity' in q or 'speed' in q) and ('time' in q or 'distance' in q or 'acceleration' in q):
        return f"Velocity = displacement/time (vector). Speed = distance/time (scalar). For constant acceleration: v = v₀ + at, and average velocity = (v + v₀)/2. The answer is '{answer}'."
    if 'acceleration' in q and ('velocity' in q or 'speed' in q or 'time' in q):
        return f"Acceleration is the rate of change of velocity: a = Δv/Δt. Positive acceleration means increasing velocity; negative (deceleration) means decreasing. The answer is '{answer}'."

    # Upward throw / peak
    if ('thrown' in q or 'launch' in q or 'toss' in q) and ('upward' in q or 'vertical' in q or 'height' in q):
        return f"When thrown upward, an object decelerates at g = 9.8 m/s². At the highest point, velocity = 0. Use v² = v₀² - 2gΔy for max height, or t_peak = v₀/g. The answer is '{answer}'."

    # Object on surface / normal force
    if 'normal force' in q or ('surface' in q and 'force' in q):
        return f"The normal force is the contact force perpendicular to a surface. On a flat surface: N = mg. On an incline: N = mg·cos(θ). It adjusts to prevent objects from passing through surfaces. The answer is '{answer}'."

    # Displacement (standalone definition)
    if 'displacement' in q and ('is' in q or 'define' in q or 'what' in q or 'change' in q):
        return f"Displacement is the change in position — a vector quantity with both magnitude and direction. It differs from distance (scalar, total path length). Displacement = final position - initial position. The answer is '{answer}'."

    # Conservative forces
    if 'conservative force' in q or 'conservative' in q and 'force' in q:
        return f"Conservative forces (gravity, spring force, electric force) do work independent of the path taken — only the start and end positions matter. They have associated potential energy. Friction is non-conservative. The answer is '{answer}'."

    # Work and energy (physics)
    if 'work' in q and ('done' in q or 'force' in q or 'distance' in q or 'displacement' in q) and 'energy' not in q:
        return f"Work is done when a force causes displacement: W = F·d·cos(θ). When force and displacement are in the same direction, W = Fd. Work is measured in joules (J). The answer is '{answer}'."

    # Units / Dimensions / Prefixes (physics)
    if 'derived unit' in q or ('unit' in q and ('derived' in q or 'newton' in q or 'joule' in q)):
        return f"Derived units are combinations of base units. Newton (N) = kg·m/s² (force). Joule (J) = kg·m²/s² (energy). Watt (W) = J/s (power). Pascal (Pa) = N/m² (pressure). The answer is '{answer}'."
    if 'prefix' in q and (re.search(r'milli|micro|nano|kilo|mega|giga|centi', q)):
        return f"SI prefixes: kilo (10³), centi (10⁻²), milli (10⁻³), micro (10⁻⁶), nano (10⁻⁹), pico (10⁻¹²), mega (10⁶), giga (10⁹). The answer is '{answer}'."
    if 'dimension' in q and ('velocity' in q or 'energy' in q or 'force' in q or 'acceleration' in q):
        return f"Dimensional analysis uses base quantities [M] (mass), [L] (length), [T] (time). Velocity: [L][T]⁻¹. Acceleration: [L][T]⁻². Force: [M][L][T]⁻². Energy: [M][L]²[T]⁻². The answer is '{answer}'."
    if 'convert' in q and (re.search(r'mg|kg|cm|km|ml|mm', q)):
        return f"For unit conversions, use the appropriate conversion factor (e.g., 1 g = 1000 mg, 1 km = 1000 m, 1 kg = 1000 g). Multiply by the conversion factor to change units. The answer is '{answer}'."
    if ('unit' in q and 'different' in q and 'add' in q) or ('different units' in q):
        return f"You cannot meaningfully add or subtract quantities with different units (e.g., meters + seconds). Operations require matching units; convert to the same units first. The answer is '{answer}'."
    if 'significant figure' in q or 'sig fig' in q:
        return f"Significant figures indicate measurement precision. Rules: all non-zero digits are significant, zeros between non-zeros are significant, leading zeros are not, trailing zeros after a decimal are significant. The answer is '{answer}'."
    if 'scientific notation' in q:
        return f"Scientific notation expresses numbers as a × 10ⁿ where 1 ≤ a < 10. It makes very large or very small numbers manageable and clarifies significant figures. The answer is '{answer}'."

    # Uniform acceleration calculation
    if 'accelerat' in q and ('rest' in q or 'uniformly' in q) and (re.search(r'\d+\s*m', q) or re.search(r'\d+\s*s', q)):
        return f"For uniform acceleration from rest: d = ½at² (since v₀ = 0). Rearranging for acceleration: a = 2d/t². Substitute the given values and solve. The answer is '{answer}'."

    # ─── AP Statistics ────────────────────────────────────────────────────

    # Z-score
    if 'z-score' in q or 'z score' in q or 'z-value' in q:
        return f"A z-score measures how many standard deviations a value is from the mean: z = (x - μ)/σ. Positive z: above mean; negative z: below mean. The answer is '{answer}'."

    # R² / coefficient of determination
    if 'r²' in q or 'r-squared' in q or 'coefficient of determination' in q or 'r squared' in q:
        return f"The coefficient of determination (R²) represents the proportion of variance in the dependent variable explained by the independent variable(s). R² ranges from 0 to 1; higher values indicate a better fit. The answer is '{answer}'."

    # Significance level
    if 'significance level' in q or 'alpha' in q and 'level' in q:
        return f"The significance level (α) is the threshold for rejecting the null hypothesis. Common values are 0.05 (5%) and 0.01 (1%). If p-value < α, reject H₀. The answer is '{answer}'."

    # Independent events / probability
    if 'independent' in q and ('event' in q or 'probability' in q):
        return f"Two events are independent if the occurrence of one does not affect the probability of the other. For independent events: P(A and B) = P(A) × P(B). The answer is '{answer}'."

    # Mutually exclusive
    if 'mutually exclusive' in q:
        return f"Mutually exclusive events cannot occur simultaneously: P(A and B) = 0. For mutually exclusive events: P(A or B) = P(A) + P(B). The answer is '{answer}'."

    # Outliers
    if 'outlier' in q:
        return f"Outliers are extreme values that fall far from the rest of the data. They disproportionately affect the mean and standard deviation but have little effect on the median and IQR. The answer is '{answer}'."

    # Mean vs median
    if 'mean' in q and ('median' in q or 'skew' in q or 'affect' in q):
        return f"The mean is sensitive to extreme values (outliers), while the median is resistant. In right-skewed data: mean > median. In left-skewed: mean < median. The answer is '{answer}'."

    # Chi-square
    if 'chi-square' in q or 'chi square' in q or 'χ²' in q:
        return f"The chi-square test compares observed vs. expected frequencies. A goodness-of-fit test checks one variable; a test of independence checks association between two categorical variables. The answer is '{answer}'."

    # Sample vs population
    if 'sample' in q and ('population' in q or 'statistic' in q or 'parameter' in q):
        return f"A parameter describes a population (e.g., μ, σ), while a statistic describes a sample (e.g., x̄, s). Statistics are used to estimate parameters. The answer is '{answer}'."

    # Bias / random sampling
    if 'bias' in q or 'random sample' in q or 'sampling method' in q:
        return f"Bias occurs when the sampling method systematically favors certain outcomes. Simple random sampling (SRS) gives every member an equal chance of selection, minimizing bias. The answer is '{answer}'."

    # Observational vs experimental
    if 'observational' in q or ('experiment' in q and 'observ' in q):
        return f"In experiments, researchers assign treatments to establish causation. In observational studies, they observe without intervention — only association can be established. The answer is '{answer}'."

    # Conditional probability
    if 'conditional' in q and 'probability' in q:
        return f"Conditional probability P(A|B) = P(A and B)/P(B) — the probability of A given B has occurred. The answer is '{answer}'."

    # Standard error
    if 'standard error' in q:
        return f"Standard error measures the variability of a sample statistic: SE = σ/√n (for means). Larger samples produce smaller standard errors. The answer is '{answer}'."

    # "Which statistical concept is most relevant" catch-all
    if 'statistical' in q and ('concept' in q or 'method' in q or 'technique' in q):
        return f"Statistical methods are chosen based on data type and research question: t-tests compare means, chi-square tests compare frequencies, regression models relationships, ANOVA compares multiple groups. The answer is '{answer}'."

    if 'confidence interval' in q:
        return f"A confidence interval estimates a population parameter. A 95% CI means that 95% of similarly constructed intervals would contain the true parameter. Width depends on sample size and confidence level. The answer is '{answer}'."
    if 'p-value' in q or 'p value' in q:
        return f"The p-value is the probability of observing data as extreme as (or more extreme than) the sample results, assuming the null hypothesis is true. A small p-value (< α) leads to rejecting H₀. The answer is '{answer}'."
    if 'null hypothesis' in q or 'hypothesis test' in q:
        return f"In hypothesis testing, H₀ (null) assumes no effect/difference. H₁ (alternative) claims an effect. We reject H₀ if evidence (p-value < significance level α) is strong enough. The answer is '{answer}'."
    if 'type i error' in q or 'type 1 error' in q:
        return f"A Type I error is rejecting a true null hypothesis (false positive). Its probability equals α, the significance level. The answer is '{answer}'."
    if 'type ii error' in q or 'type 2 error' in q:
        return f"A Type II error is failing to reject a false null hypothesis (false negative). Its probability is β. Power = 1 - β is the probability of correctly rejecting H₀. The answer is '{answer}'."
    if 'correlation' in q and ('coefficient' in q or 'r ' in q or q.endswith('r')):
        return f"The correlation coefficient r measures the strength and direction of a linear relationship. r ranges from -1 to 1; values near ±1 indicate strong linear association. The answer is '{answer}'."
    if 'regression' in q:
        return f"Linear regression fits the best line ŷ = a + bx to data, where b = r(s_y/s_x) is the slope and a = ȳ - bx̄ is the intercept. r² measures the proportion of variation explained. The answer is '{answer}'."
    if 'normal distribution' in q or 'bell curve' in q:
        return f"The normal distribution is symmetric and bell-shaped. The empirical rule: ~68% within 1σ, ~95% within 2σ, ~99.7% within 3σ of the mean. The answer is '{answer}'."
    if 'binomial' in q:
        return f"A binomial distribution models the number of successes in n independent trials with constant probability p. P(X=k) = C(n,k)p^k(1-p)^(n-k). Mean = np, SD = √(np(1-p)). The answer is '{answer}'."
    if 'sampling distribution' in q:
        return f"A sampling distribution shows the distribution of a statistic over many samples. By the Central Limit Theorem, the sampling distribution of the mean approaches normal as n increases. The answer is '{answer}'."
    if 'central limit theorem' in q:
        return f"The Central Limit Theorem states that the sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the population's shape. The answer is '{answer}'."

    # ─── AP Human Geography ───────────────────────────────────────────────

    # Age structure pyramids
    if 'age structure' in q or 'population pyramid' in q:
        return f"Age structure pyramids display population distribution by age and sex. Broad bases indicate rapid growth; narrow bases suggest slow/negative growth. They help predict future population trends. The answer is '{answer}'."

    # Migration
    if 'migration' in q and ('push' in q or 'pull' in q):
        return f"Push factors drive people away (war, poverty, persecution). Pull factors attract people (jobs, safety, freedom). Migration patterns reflect both economic and social forces. The answer is '{answer}'."
    if 'migration' in q:
        return f"Migration is the permanent or semi-permanent movement of people. Types include internal (within a country) and international. Factors include economic opportunity, safety, and family ties. The answer is '{answer}'."

    # Supranational organizations
    if 'supranational' in q or 'european union' in q or 'nato' in q:
        return f"Supranational organizations (EU, NATO, UN) are multinational unions where member states cooperate by transferring some sovereign authority to achieve shared goals. The answer is '{answer}'."

    # Culture
    if 'cultural landscape' in q:
        return f"A cultural landscape is the visible imprint of human activity on a place — buildings, land-use patterns, and modifications that reflect a group's values and practices. The answer is '{answer}'."
    if 'acculturation' in q:
        return f"Acculturation is the process of adopting traits from another culture while retaining one's own cultural identity. It differs from assimilation, where the original culture is largely lost. The answer is '{answer}'."

    # Agriculture
    if 'green revolution' in q:
        return f"The Green Revolution introduced high-yield crop varieties, chemical fertilizers, and irrigation to developing countries, dramatically increasing food production but also raising environmental and economic concerns. The answer is '{answer}'."
    if 'subsistence' in q and ('agriculture' in q or 'farming' in q):
        return f"Subsistence agriculture produces food primarily for the farmer's family, not for sale. Types include shifting cultivation, pastoral nomadism, and intensive subsistence farming. The answer is '{answer}'."
    if 'commercial' in q and ('agriculture' in q or 'farming' in q):
        return f"Commercial agriculture produces crops and livestock for sale in the market, using mechanization and technology for large-scale production. The answer is '{answer}'."

    # Sovereignty / nation-state
    if 'sovereignty' in q or 'nation-state' in q or 'nation state' in q:
        return f"A nation-state is a political unit where the state's boundaries correspond to the territory occupied by a particular nation/ethnic group. Sovereignty means supreme authority within a territory. The answer is '{answer}'."

    # Gerrymandering
    if 'gerrymandering' in q:
        return f"Gerrymandering is the manipulation of electoral district boundaries to favor a particular political party. Techniques include 'packing' (concentrating opposition) and 'cracking' (splitting opposition). The answer is '{answer}'."

    if 'demographic transition' in q:
        return f"The Demographic Transition Model describes 4-5 stages of population change based on birth/death rates: Stage 1 (high both), Stage 2 (declining death), Stage 3 (declining birth), Stage 4 (low both), Stage 5 (below replacement). The answer is '{answer}'."
    if 'urbanization' in q:
        return f"Urbanization is the increasing concentration of population in cities. Push factors (rural poverty) and pull factors (urban jobs, services) drive rural-to-urban migration. The answer is '{answer}'."
    if 'globalization' in q:
        return f"Globalization is the increasing interconnection of economies, cultures, and politics worldwide through trade, technology, and migration. It has both benefits (economic growth) and costs (cultural homogenization). The answer is '{answer}'."
    if 'diffusion' in q and ('cultural' in q or 'spatial' in q):
        return f"Cultural diffusion is the spread of cultural traits. Types include relocation (migration), expansion (hierarchical, contagious, stimulus). Barriers like distance and culture affect diffusion rates. The answer is '{answer}'."

    # Region types (formal, functional, vernacular)
    if 'formal region' in q or ('region' in q and ('climate' in q or 'vegetation' in q or 'language' in q) and 'defined' in q):
        return f"A formal (uniform) region is defined by one or more measurable characteristics shared throughout the area — e.g., language spoken, climate type, or political boundaries. The answer is '{answer}'."
    if 'functional region' in q or ('region' in q and ('served' in q or 'node' in q or 'hinterland' in q)):
        return f"A functional (nodal) region is organized around a central node or focal point and defined by connections/interactions — e.g., a city's commuter zone, newspaper circulation area, or transit network. The answer is '{answer}'."
    if 'vernacular region' in q or 'perceptual region' in q or ('region' in q and ('mental' in q or 'perception' in q or 'perceived' in q)):
        return f"A vernacular (perceptual) region is defined by people's mental images and cultural identity rather than official boundaries — e.g., 'the South,' 'the Midwest,' or 'Silicon Valley.' The answer is '{answer}'."
    if 'region' in q and ('type' in q or 'classif' in q or 'which' in q) and ('formal' in q or 'functional' in q or 'vernacular' in q or 'perceptual' in q):
        return f"The three types of regions: formal (defined by shared characteristics), functional (organized around a node/hub), and vernacular/perceptual (based on mental images and cultural identity). The answer is '{answer}'."

    # Political boundaries / colonialism
    if 'political boundar' in q and ('africa' in q or 'colonial' in q or 'established' in q):
        return f"Many political boundaries in Africa were drawn by European colonial powers at the Berlin Conference (1884-85), often with little regard for existing ethnic, linguistic, or cultural boundaries, leading to ongoing conflicts. The answer is '{answer}'."
    if 'political boundar' in q and ('superimposed' in q or 'artificial' in q or 'straight' in q):
        return f"Superimposed boundaries are drawn by outside powers (often colonial), ignoring local ethnic and cultural divisions. Geometric (straight-line) boundaries in Africa and the Middle East are classic examples. The answer is '{answer}'."

    # Developed / developing country
    if 'developed country' in q or ('development' in q and ('gdp' in q or 'hdi' in q)):
        return f"A developed country is characterized by high GDP per capita, advanced technology and infrastructure, high HDI (Human Development Index), high life expectancy, and low birth rates. The answer is '{answer}'."
    if 'developing country' in q or 'least developed' in q:
        return f"A developing (less developed) country has lower GDP per capita, limited infrastructure, lower HDI, higher birth rates, and higher rates of poverty compared to developed nations. The answer is '{answer}'."

    # Nationalism
    if 'nationalism' in q:
        return f"Nationalism is a sense of loyalty and devotion to a nation-state and its interests. It can unify a country (centripetal force) but can also lead to separatist movements and conflict. The answer is '{answer}'."

    # Colonialism / imperialism
    if 'colonialism' in q or 'imperialism' in q:
        return f"Colonialism is the practice of acquiring political control over another country, exploiting its resources and people. European colonialism profoundly shaped political boundaries, economies, and cultures worldwide. The answer is '{answer}'."

    # Place / space / location
    if 'sense of place' in q or 'place identity' in q:
        return f"Sense of place is the subjective attachment people feel toward a location, shaped by personal experiences, cultural associations, and emotional connections. The answer is '{answer}'."
    if 'site' in q and 'situation' in q:
        return f"Site refers to a place's internal physical characteristics (terrain, climate). Situation refers to its external location relative to other places (accessibility, connectivity). Both influence settlement and development. The answer is '{answer}'."

    # ─── AP Calculus specific ─────────────────────────────────────────────

    if 'chain rule' in q:
        return f"The chain rule differentiates composite functions: d/dx[f(g(x))] = f'(g(x)) · g'(x). Identify the outer and inner functions, differentiate each, then multiply. The answer is {answer}."
    if 'product rule' in q:
        return f"The product rule: d/dx[f(x)g(x)] = f'(x)g(x) + f(x)g'(x). Differentiate each factor and sum the cross-products. The answer is {answer}."
    if 'quotient rule' in q:
        return f"The quotient rule: d/dx[f(x)/g(x)] = [f'(x)g(x) - f(x)g'(x)] / [g(x)]². The answer is {answer}."
    if 'mean value theorem' in q:
        return f"The Mean Value Theorem states that if f is continuous on [a,b] and differentiable on (a,b), there exists c in (a,b) where f'(c) = [f(b)-f(a)]/(b-a). The answer is '{answer}'."
    if 'fundamental theorem' in q and 'calculus' in q:
        return f"The Fundamental Theorem of Calculus links differentiation and integration: ∫ₐᵇ f(x)dx = F(b) - F(a) where F' = f, and d/dx[∫ₐˣ f(t)dt] = f(x). The answer is '{answer}'."
    if 'critical point' in q or 'critical number' in q:
        return f"Critical points occur where f'(x) = 0 or f'(x) is undefined. They are candidates for local maxima, minima, or inflection points. Use the first or second derivative test to classify. The answer is '{answer}'."
    if 'inflection point' in q:
        return f"An inflection point is where the concavity of a function changes. It occurs where f''(x) = 0 or is undefined, AND the sign of f''(x) actually changes. The answer is '{answer}'."
    if 'riemann sum' in q:
        return f"A Riemann sum approximates a definite integral by dividing the interval into n subintervals and summing the areas of rectangles (left, right, or midpoint). As n→∞, it converges to the exact integral. The answer is '{answer}'."
    if 'convergent' in q or 'divergent' in q or 'convergence' in q:
        return f"A series converges if the sum of its terms approaches a finite limit; it diverges otherwise. Tests include ratio test, integral test, comparison test, and p-series test (converges if p > 1). The answer is '{answer}'."

    # Mathematical modeling (very common AP Calc topic)
    if 'mathematical model' in q or 'modeling' in q:
        return f"Mathematical modeling uses functions to represent real-world situations. A good model identifies key variables, captures the essential relationship, and balances accuracy with simplicity. The answer is '{answer}'."

    # Continuity
    if 'continuous' in q and ('point' in q or 'function' in q or 'interval' in q or 'at' in q):
        return f"A function is continuous at x = a if three conditions hold: (1) f(a) is defined, (2) lim(x→a) f(x) exists, and (3) lim(x→a) f(x) = f(a). The answer is '{answer}'."

    # Removable discontinuity
    if 'removable discontinuity' in q or 'removable' in q:
        return f"A removable discontinuity (hole) occurs when the limit exists but the function is either undefined or has a different value at that point. It can be 'removed' by redefining the function. The answer is '{answer}'."
    if 'discontinuit' in q:
        return f"Types of discontinuities: removable (hole — limit exists), jump (left/right limits differ), and infinite (vertical asymptote). The answer is '{answer}'."

    # Intermediate Value Theorem
    if 'intermediate value' in q:
        return f"The Intermediate Value Theorem (IVT) states that if f is continuous on [a,b], then f takes every value between f(a) and f(b) at some point in [a,b]. This guarantees the existence of roots. The answer is '{answer}'."

    # L'Hôpital's Rule
    if "l'h" in q or 'lhopital' in q or 'hopital' in q:
        return f"L'Hôpital's Rule: for indeterminate forms 0/0 or ∞/∞, lim f(x)/g(x) = lim f'(x)/g'(x). Differentiate numerator and denominator separately, then re-evaluate the limit. The answer is '{answer}'."

    # Related rates
    if 'related rate' in q:
        return f"Related rates problems use implicit differentiation with respect to time. Identify the equation relating the variables, differentiate both sides with respect to t, substitute known values, and solve. The answer is '{answer}'."

    # Optimization
    if 'optimization' in q or 'optimize' in q or ('maximum' in q and 'minimum' in q and 'find' in q):
        return f"Optimization problems: (1) express the quantity to optimize as a function, (2) find critical points where f'(x) = 0, (3) verify using the second derivative or endpoint test. The answer is '{answer}'."

    # u-substitution
    if 'u-substitution' in q or 'u substitution' in q or 'u-sub' in q:
        return f"u-substitution reverses the chain rule for integration. Let u = inner function, compute du, rewrite the integral in terms of u, integrate, then substitute back. The answer is '{answer}'."

    # Taylor / Maclaurin series
    if 'taylor' in q or 'maclaurin' in q:
        return f"A Taylor series represents a function as an infinite sum of terms: f(x) = Σ f⁽ⁿ⁾(a)(x-a)ⁿ/n!. A Maclaurin series is centered at a = 0. The answer is '{answer}'."

    # Area between curves
    if 'area between' in q and 'curve' in q:
        return f"The area between curves f(x) and g(x) from a to b is ∫ₐᵇ |f(x) - g(x)| dx. Determine which function is on top in each interval. The answer is '{answer}'."

    # Concavity
    if 'concav' in q:
        return f"A function is concave up when f''(x) > 0 (bowl shape, ∪) and concave down when f''(x) < 0 (cap shape, ∩). The answer is '{answer}'."

    # Increasing / decreasing
    if ('increasing' in q or 'decreasing' in q) and ('function' in q or 'interval' in q or 'f(' in q):
        return f"A function is increasing where f'(x) > 0 and decreasing where f'(x) < 0. Find critical points, then test the sign of f' in each interval. The answer is '{answer}'."

    # Integration technique (broad - catches "which substitution" etc.)
    if 'substitution' in q and ('integration' in q or 'integral' in q or 'antiderivative' in q):
        return f"Integration by substitution (u-sub) is the reverse of the chain rule. Identify the inner function as u, express du, rewrite the integrand in terms of u, integrate, then substitute back. The answer is '{answer}'."
    if 'integration' in q and ('technique' in q or 'method' in q or 'best' in q or 'appropriate' in q):
        return f"Common integration techniques: u-substitution (reverse chain rule), integration by parts (∫u dv = uv - ∫v du), partial fractions (rational functions), and trig substitution. Choose based on the integrand's form. The answer is '{answer}'."
    if 'integration by parts' in q:
        return f"Integration by parts: ∫u dv = uv - ∫v du. Use LIATE (Logarithmic, Inverse trig, Algebraic, Trig, Exponential) to choose u. The answer is '{answer}'."

    # Antiderivative
    if 'antiderivative' in q:
        return f"The antiderivative (indefinite integral) reverses differentiation. For f(x) = xⁿ, the antiderivative is xⁿ⁺¹/(n+1) + C. Always include the constant of integration C. The answer is '{answer}'."

    # Differential equation
    if 'differential equation' in q:
        return f"A differential equation involves derivatives of an unknown function. Separable DEs can be solved by separating variables: ∫f(y)dy = ∫g(x)dx. The answer is '{answer}'."

    # Squeeze theorem
    if 'squeeze' in q or 'sandwich' in q:
        return f"The Squeeze Theorem: if g(x) ≤ f(x) ≤ h(x) near a point, and lim g(x) = lim h(x) = L, then lim f(x) = L. Useful when direct evaluation is difficult. The answer is '{answer}'."

    # Composite function (not composition per se, but questions about composite functions)
    if 'composite' in q and 'function' in q:
        return f"A composite function f(g(x)) applies one function to the output of another. To differentiate, use the chain rule: d/dx[f(g(x))] = f'(g(x))·g'(x). The answer is '{answer}'."

    # ─── Chemistry: Litmus / Indicators ──────────────────────────────────
    if 'litmus' in q or ('indicator' in q and ('acid' in q or 'base' in q or 'ph' in q.split())):
        return f"Litmus paper turns red in acidic solutions (pH < 7) and blue in basic solutions (pH > 7). Other indicators like phenolphthalein change color at specific pH ranges. The answer is '{answer}'."

    # Chemistry: Acid naming / nomenclature
    if ('name' in q or 'naming' in q or 'nomenclature' in q or 'called' in q) and ('acid' in q) and ('chem' in course or 'ap_chem' in course):
        return f"Binary acids use 'hydro-___-ic acid' (HCl → hydrochloric acid). Oxyacids ending in -ate use '-ic acid' (HNO₃ → nitric acid); those ending in -ite use '-ous acid' (HNO₂ → nitrous acid). The answer is '{answer}'."

    # Chemistry: Arrhenius acid/base
    if 'arrhenius' in q:
        return f"Arrhenius acids produce H⁺ ions in water; Arrhenius bases produce OH⁻ ions in water. This definition is limited to aqueous solutions. The answer is '{answer}'."

    # Chemistry: Lewis acid/base
    if 'lewis' in q and ('acid' in q or 'base' in q):
        return f"A Lewis acid is an electron-pair acceptor; a Lewis base is an electron-pair donor. This is the broadest acid-base definition and includes reactions without H⁺ transfer. The answer is '{answer}'."

    # Chemistry: Brønsted-Lowry (broader catch)
    if 'bronsted' in q or 'brønsted' in q or 'br\u00f8nsted' in q:
        return f"A Brønsted-Lowry acid donates a proton (H⁺); a Brønsted-Lowry base accepts a proton. Conjugate acid-base pairs differ by one proton. The answer is '{answer}'."

    # Chemistry: Salt / neutralization
    if 'neutralization' in q or ('salt' in q and ('acid' in q or 'base' in q)):
        return f"Neutralization is the reaction of an acid and base to produce water and a salt: Acid + Base → Salt + H₂O. The salt's pH depends on the strength of its parent acid and base. The answer is '{answer}'."

    # Chemistry: Strong vs weak acids/bases
    if ('strong' in q or 'weak' in q) and ('acid' in q or 'base' in q) and ('chem' in course or 'ap_chem' in course):
        return f"Strong acids/bases ionize completely in water (HCl, NaOH). Weak acids/bases only partially ionize (CH₃COOH, NH₃). The degree of ionization determines the equilibrium constant Ka or Kb. The answer is '{answer}'."

    # Chemistry: Significant figures
    if ('sig fig' in q or 'significant figure' in q or 'significant digit' in q) and ('chem' in course or 'ap_chem' in course or 'physics' in course):
        return f"Significant figures rules: all nonzero digits are significant; leading zeros are not; trailing zeros after a decimal are; captive zeros are. For multiplication/division, keep the fewest sig figs. The answer is '{answer}'."
    if ('fewest' in q or 'fewer' in q) and ('sig fig' in q or 'significant' in q or 'decimal' in q or 'sig fig' in answer.lower()):
        return f"In multiplication/division, the answer should have the same number of significant figures as the factor with the FEWEST sig figs. In addition/subtraction, use the fewest decimal places. The answer is '{answer}'."

    # Chemistry: Scientific notation arithmetic
    if re.search(r'\d+\s*[×x]\s*10\s*[⁰¹²³⁴⁵⁶⁷⁸⁹]+', q) and ('chem' in course or 'physics' in course):
        return f"Scientific notation: (a × 10ᵐ) × (b × 10ⁿ) = (a·b) × 10^(m+n). For division, subtract exponents. Ensure the coefficient is between 1 and 10. The answer is {answer}."

    # Chemistry: Metric conversions
    if re.search(r'(centi|milli|kilo|micro|nano).*meter|liter|gram', q) and ('equal' in q or 'how many' in q or 'convert' in q):
        return f"Metric prefixes: kilo = 10³ (1000×), centi = 10⁻² (0.01×), milli = 10⁻³ (0.001×). 1 km = 1000 m, 1 m = 100 cm = 1000 mm, 1 L = 1000 mL, 1 kg = 1000 g. The answer is {answer}."
    if ('smaller' in q or 'larger' in q) and 'unit' in q and ('convert' in q or 'numerical' in q or 'value' in q):
        return f"Converting to larger units → smaller number. Converting to smaller units → larger number. Think: 1 km = 1000 m, so fewer km than meters. The answer is '{answer}'."

    # AP Biology: Light reactions / photosystems
    if 'light reaction' in q or 'light-dependent' in q or 'light dependent' in q:
        return f"The light-dependent reactions occur in the thylakoid membranes. Light energy splits water (photolysis), produces ATP via chemiosmosis, and reduces NADP⁺ to NADPH. Oxygen is released as a byproduct. The answer is '{answer}'."
    if 'photosystem' in q:
        if 'photosystem i' in q or 'psi' in q or 'ps i' in q or 'p700' in q:
            return f"Photosystem I (PSI, P700) re-energizes electrons to reduce NADP⁺ to NADPH. It works in series with PSII during noncyclic electron flow. The answer is '{answer}'."
        return f"Photosystem II (PSII, P680) absorbs light and splits water to replace lost electrons. Energized electrons pass through the electron transport chain to produce ATP. The answer is '{answer}'."
    if 'thylakoid' in q:
        return f"Thylakoids are membrane-bound compartments in chloroplasts where the light-dependent reactions occur. Their stacked form (grana) maximizes surface area for chlorophyll and photosystems. The answer is '{answer}'."

    # AP Biology: Proton gradient / chemiosmosis (broader)
    if 'proton gradient' in q or 'chemiosmosis' in q or 'electrochemical gradient' in q:
        return f"Chemiosmosis uses a proton (H⁺) gradient across a membrane to drive ATP synthase, producing ATP. In chloroplasts the gradient is in the thylakoid; in mitochondria it's across the inner membrane. The answer is '{answer}'."

    # Biology: Resource partitioning
    if 'resource partitioning' in q or 'niche partitioning' in q:
        return f"Resource partitioning is the division of limited resources among species to reduce competition. Species may use different parts of the habitat, different food sources, or be active at different times. The answer is '{answer}'."

    # Biology: Omnivore / herbivore / carnivore
    if 'omnivore' in q or 'herbivore' in q or 'carnivore' in q:
        return f"Herbivores eat plants, carnivores eat animals, and omnivores eat both. These feeding relationships determine an organism's trophic level in a food web. The answer is '{answer}'."

    # Biology: Sustainability / overexploitation
    if 'sustainability' in q or 'overexploitation' in q or 'overharvesting' in q:
        return f"Sustainability means using resources at a rate that allows natural replenishment. Overexploitation harvests resources faster than they can regenerate, threatening species and ecosystems. The answer is '{answer}'."

    # Physics: Generator / electromagnetic induction
    if 'generator' in q or 'electromagnetic induction' in q:
        return f"A generator converts mechanical energy to electrical energy via electromagnetic induction. A rotating coil in a magnetic field induces an EMF (Faraday's Law). The answer is '{answer}'."

    # Physics: Relativity / gamma factor
    if 'gamma' in q or 'γ' in q or 'γ' in question_text:
        if 'relativity' in q or 'lorentz' in q or 'time dilation' in q or 'v →' in question_text or 'v→' in question_text or 'infinity' in answer.lower():
            return f"The Lorentz factor γ = 1/√(1 - v²/c²) describes relativistic effects. As an object's speed approaches c, γ → ∞, causing time dilation and length contraction. The answer is '{answer}'."

    # Physics: Quantum / photon energy / wave-particle duality
    if 'quantum' in q or 'photon energy' in q or 'wave-particle' in q or 'de broglie' in q:
        return f"Quantum mechanics describes matter and energy at the atomic scale. Photon energy E = hf. De Broglie wavelength λ = h/mv relates particle momentum to wave behavior. The answer is '{answer}'."

    # Physics: Quarks / standard model
    if 'quark' in q or 'standard model' in q:
        return f"Quarks are fundamental particles that combine to form hadrons (protons = uud, neutrons = udd). The Standard Model classifies all known fundamental particles and three of four forces. The answer is '{answer}'."

    # Physics: SUVAT / kinematic equations (broad catch)
    if ('suvat' in q) or ('kinematic' in q and 'equation' in q):
        return f"The SUVAT (kinematic) equations relate displacement (s), initial velocity (u), final velocity (v), acceleration (a), and time (t) for constant acceleration: v = u + at, s = ut + ½at², v² = u² + 2as. The answer is '{answer}'."

    # Physics: g = 9.8 m/s² / free fall acceleration  
    if 'free fall' in q or ('acceleration' in q and 'gravity' in q and 'due to' in q):
        return f"In free fall near Earth's surface, all objects accelerate at g ≈ 9.8 m/s² (ignoring air resistance). This value comes from Newton's law of gravitation: g = GM/R². The answer is '{answer}'."

    # AP Calculus: Integral properties (splitting, constant multiple)
    if ('integral' in q or '∫' in q) and ('property' in q or 'properties' in q or 'split' in q or 'sum' in q):
        return f"Key integral properties: ∫[a+b]dx = ∫a dx + ∫b dx (sum rule), ∫cf(x)dx = c∫f(x)dx (constant multiple), and ∫ₐᵇ f(x)dx = -∫ᵇₐ f(x)dx (reversing limits). The answer is '{answer}'."

    # AP Calculus: Simple definite/indefinite integrals (broad catch)
    if ('∫' in q or 'integral' in q or 'integrate' in q) and 'calculus' in course:
        return f"To evaluate an integral, find the antiderivative F(x), then apply the Fundamental Theorem: ∫ₐᵇ f(x)dx = F(b) - F(a). For indefinite integrals, add +C. The answer is '{answer}'."

    # AP Calculus: Limit statements (broad catch beyond specific limit patterns)
    if ('limit' in q or 'lim' in q.split()) and 'calculus' in course:
        return f"To evaluate a limit, try direct substitution first. If that gives 0/0 or ∞/∞, apply L'Hôpital's Rule, factoring, or rationalization. One-sided limits check behavior from left and right. The answer is '{answer}'."

    # AP Statistics: Broader catch for statistics concepts
    if ('statistic' in course or 'ap_stat' in course) and ('which' in q or 'what' in q):
        if 'sampling' in q or 'sample' in q:
            return f"Sampling methods include SRS (every individual equally likely), stratified (divide into groups then sample each), cluster (randomly select entire groups), and systematic (every kth individual). The answer is '{answer}'."
        if 'bias' in q:
            return f"Bias is systematic error that makes results unrepresentative. Sources include selection bias, response bias, nonresponse bias, and undercoverage. Good study design minimizes bias. The answer is '{answer}'."
        if 'distribution' in q:
            return f"A distribution describes the values a variable takes and how often. Key features: shape (symmetric, skewed), center (mean, median), and spread (range, IQR, standard deviation). The answer is '{answer}'."

    # ─── Chemistry: Calorimetry / Heat ────────────────────────────────────
    if 'calorimeter' in q or 'calorimetry' in q:
        return f"A calorimeter measures heat by tracking temperature change: q = mcΔT (mass × specific heat × temperature change). The heat released by a reaction equals the heat absorbed by the water. The answer is '{answer}'."
    if ('calorie' in q or 'kilocalorie' in q or 'kcal' in q or 'joule' in q) and ('equal' in q or 'convert' in q or 'unit' in q or 'dietary' in q):
        return f"A dietary Calorie (capital C) = 1 kilocalorie = 1,000 calories = 4,184 joules. Calories measure the energy content of food. The answer is '{answer}'."
    if 'q = mc' in q or ('heat' in q and ('mc' in q or 'specific heat' in q or 'temperature change' in q)):
        return f"The heat equation q = mcΔT relates heat (q) to mass (m), specific heat capacity (c), and temperature change (ΔT). ΔT = final temp - initial temp. The answer is '{answer}'."

    # Chemistry: Chemical formula naming (broad - catches H₂SO₄, HNO₃, etc.)
    if re.search(r'h[₂₃]?\w+[₂₃₄]', q) and ('named' in q or 'name' in q or 'is:' in q or 'called' in q):
        return f"Acid naming: binary acids → 'hydro-___-ic acid'; oxyacids from -ate polyatomic ions → '-ic acid'; from -ite → '-ous acid'. Match the polyatomic ion to determine the acid name. The answer is '{answer}'."

    # Chemistry: Heat released = heat absorbed (calorimetry broader catch)
    if 'heat' in q and ('released' in q or 'absorbed' in q or 'equals' in q) and ('reaction' in q or 'water' in q):
        return f"By conservation of energy, the heat released by a reaction equals the heat absorbed by the surroundings: q = mcΔT. In a calorimeter, this means q_reaction = -q_water. The answer is '{answer}'."

    # Chemistry: Salt from acid + base reaction
    if ('salt' in q) and ('+' in q or 'produce' in q or 'react' in q) and ('chem' in course or 'ap_chem' in course):
        return f"When an acid reacts with a base: Acid + Base → Salt + Water. The salt is formed from the cation of the base and the anion of the acid. The answer is '{answer}'."

    # ─── Nuclear Chemistry ────────────────────────────────────────────────
    if 'alpha' in q and ('decay' in q or 'particle' in q or 'radiation' in q or 'stopped' in q or 'penetrat' in q):
        return f"Alpha particles (⁴₂He) are heavy (+2 charge) and can be stopped by paper or skin. In alpha decay, the parent loses 2 protons and 2 neutrons (atomic number -2, mass number -4). The answer is '{answer}'."
    if 'beta' in q and ('decay' in q or 'particle' in q or 'radiation' in q):
        return f"Beta particles are high-energy electrons (β⁻) or positrons (β⁺). In β⁻ decay, a neutron converts to a proton (atomic number +1). Beta particles are stopped by aluminum foil. The answer is '{answer}'."
    if 'gamma' in q and ('decay' in q or 'radiation' in q or 'ray' in q or 'penetrat' in q):
        return f"Gamma rays (γ) are high-energy electromagnetic radiation with no mass or charge. They are the most penetrating, requiring thick lead or concrete to block. The answer is '{answer}'."
    if 'positron' in q:
        return f"A positron (β⁺) is the antiparticle of an electron — same mass but positive charge. In positron emission, a proton converts to a neutron (atomic number -1). The answer is '{answer}'."
    if 'fission' in q and ('fusion' in q):
        return f"Fission splits heavy nuclei into lighter ones (nuclear power plants), while fusion combines light nuclei into heavier ones (the Sun). Both release enormous energy via E = mc². The answer is '{answer}'."
    if 'fission' in q:
        return f"Nuclear fission splits a heavy nucleus (like uranium-235) into lighter nuclei, releasing neutrons and energy. A chain reaction occurs when released neutrons trigger more fissions. The answer is '{answer}'."
    if 'fusion' in q and ('nuclear' in q or 'star' in q or 'sun' in q or 'temperature' in q or 'hydrogen' in q or 'require' in q or 'high' in q):
        return f"Nuclear fusion combines light nuclei (like hydrogen) into heavier ones, releasing energy. It requires extremely high temperatures (millions of degrees) to overcome electrostatic repulsion. The answer is '{answer}'."
    if 'half-life' in q or 'half life' in q or 'half-lives' in q:
        return f"After n half-lives, the fraction remaining = (1/2)ⁿ. After 1 half-life: 1/2 remains. After 2: 1/4. After 3: 1/8. After 4: 1/16. The answer is '{answer}'."
    if 'radioactive' in q and ('tracer' in q or 'medicine' in q or 'medical' in q):
        return f"Radioactive tracers are isotopes used in medicine to track biological processes (e.g., PET scans use fluorine-18). They emit detectable radiation while posing minimal health risk due to short half-lives. The answer is '{answer}'."
    if 'nuclear' in q and ('power' in q or 'concern' in q or 'waste' in q or 'safety' in q):
        return f"Nuclear power generates electricity via fission. Main concerns include radioactive waste disposal (remains hazardous for thousands of years), potential meltdowns, and weapons proliferation. The answer is '{answer}'."
    if ('uranium' in q or 'thorium' in q or 'radium' in q) and 'decay' in q:
        return f"In nuclear decay: alpha decay reduces atomic number by 2 and mass number by 4; beta decay changes atomic number by ±1 with no mass change. Use conservation of mass number and atomic number. The answer is '{answer}'."

    # Chemistry: Temperature conversion
    if ('kelvin' in q or 'celsius' in q) and ('convert' in q or 'add' in q or 'relationship' in q):
        return f"To convert Celsius to Kelvin: K = °C + 273.15. To convert Kelvin to Celsius: °C = K - 273.15. Absolute zero (0 K) = -273.15°C. The answer is '{answer}'."

    # Chemistry/Physics: Planck's constant / E = hf
    if 'planck' in q:
        return f"Planck's constant h ≈ 6.626 × 10⁻³⁴ J·s relates a photon's energy to its frequency: E = hf. It is fundamental to quantum mechanics. The answer is '{answer}'."
    if ('energy' in q and 'frequency' in q) and ('proportional' in q or 'relationship' in q or 'e = hf' in q or 'e=hf' in q):
        return f"Photon energy is directly proportional to frequency: E = hf (where h is Planck's constant). Higher frequency light (like UV, X-rays) has more energy than lower frequency (radio waves). The answer is '{answer}'."

    # Chemistry: Radiometric dating / Carbon-14
    if 'carbon-14' in q or 'carbon 14' in q or 'radiometric dating' in q or 'radiocarbon' in q:
        return f"Carbon-14 dating measures the ratio of C-14 to C-12 in organic materials. C-14 has a half-life of ~5,730 years, making it useful for dating materials up to ~50,000 years old. The answer is '{answer}'."

    # Chemistry: General radioactivity / heavier elements
    if 'radioactive' in q and ('heav' in q or 'z >' in q or 'unstable' in q or 'generally' in q):
        return f"Elements with atomic number Z > 83 (bismuth) have no stable isotopes — all are radioactive. Heavier nuclei have too many protons, causing instability due to proton-proton repulsion. The answer is '{answer}'."

    # Geometry: Circle similarity / always true about circles
    if 'circle' in q and ('similar' in q or 'always true' in q or 'always' in q):
        return f"All circles are similar because any circle can be mapped to any other circle through a dilation (scaling). The ratio of circumference to diameter (π) is constant for all circles. The answer is '{answer}'."

    # Geometry: Chords intersecting inside / angle and arcs
    if ('chord' in q or 'arc' in q) and ('intersect' in q or 'angle' in q or 'formula' in q):
        return f"When two chords intersect inside a circle, the angle = ½(sum of intercepted arcs). Also, the products of their segments are equal: (segment₁)(segment₂) = (segment₃)(segment₄). The answer is '{answer}'."

    # Geometry: Parabola focus/directrix (check both question and answer)
    if 'parabola' in q and ('focus' in q or 'directrix' in q or 'focus' in answer.lower() or 'directrix' in answer.lower()):
        return f"A parabola is the set of all points equidistant from a fixed point (focus) and a fixed line (directrix). The vertex is the midpoint between them. The answer is '{answer}'."

    # Geometry: Method of disks / integration for volume
    if ('disk' in q or 'washer' in q or 'shell' in q) and ('volume' in q or 'revolve' in q or 'rotate' in q):
        return f"Volumes of revolution: Disk method uses V = π∫[R(x)]²dx. Washer method: V = π∫([R(x)]²-[r(x)]²)dx. Shell method: V = 2π∫x·f(x)dx. Choose based on the axis of rotation. The answer is '{answer}'."

    # Physics: Starts from rest (u = 0)
    if 'starts from rest' in q or ('from rest' in q and ('initial' in q or 'velocity' in q or 'speed' in q)):
        return f"'Starts from rest' means the initial velocity u = 0 m/s. Use this in kinematic equations like v = u + at and s = ut + ½at². The answer is '{answer}'."

    # Physics: Newton's Third Law application (same force)
    if ('hit' in q or 'collide' in q or 'push' in q) and ('force' in q or 'greater' in q) and ('same' in a or 'equal' in a or 'both' in a):
        return f"Newton's Third Law: when two objects interact, they exert equal and opposite forces on each other. The truck and car experience the SAME force, but different accelerations (F = ma). The answer is '{answer}'."

    # Physics: KE calculation (specific numbers)
    if re.search(r'ke|kinetic energy', q) and re.search(r'\d+\s*kg', q) and re.search(r'\d+\s*m/s', q):
        return f"Kinetic energy KE = ½mv². Substitute the given mass and velocity, then calculate. Remember to square the velocity first. The answer is {answer}."

    # Physics: Unit conversions / SI units (horsepower, etc.)
    if 'horsepower' in q or 'si unit' in q and ('momentum' in q or 'energy' in q or 'force' in q or 'work' in q or 'power' in q):
        return f"SI units: Force = Newton (N = kg·m/s²), Energy/Work = Joule (J = kg·m²/s²), Power = Watt (W = J/s), Momentum = kg·m/s. 1 horsepower ≈ 746 W. The answer is '{answer}'."

    # Physics: Why bend knees (impulse application)
    if 'bend' in q and 'knee' in q:
        return f"Bending your knees increases the stopping time during a landing. Since impulse J = FΔt = Δp (change in momentum is fixed), increasing Δt reduces the average force on your body. The answer is '{answer}'."

    # Physics: Can average velocity be zero?
    if 'average velocity' in q and ('zero' in q or 'return' in q or 'can' in q):
        return f"Yes — average velocity = displacement / time. If an object returns to its starting position, displacement = 0, so average velocity = 0, even though it was moving. The answer is '{answer}'."

    # Physics: Period / frequency relationship
    if re.search(r't\s*=.*f\s*=|f\s*=.*t\s*=|period.*frequency|frequency.*period', q) or (re.search(r'[tf]\s*=\s*[\d.]+', q) and ('period' in q or 'frequency' in q or 'hz' in q)):
        return f"Period (T) and frequency (f) are reciprocals: T = 1/f and f = 1/T. If T = 0.5 s, then f = 1/0.5 = 2 Hz. The answer is '{answer}'."
    if re.search(r'if\s+t\s*=\s*[\d.]+', q) and ('f' in q.split() or 'frequency' in q):
        return f"Frequency and period are reciprocals: f = 1/T. Substitute the given period to find the frequency. The answer is '{answer}'."
    if 'geostationary' in q or 'geosynchronous' in q:
        return f"A geostationary satellite orbits Earth with a period of exactly 24 hours, matching Earth's rotation. It stays above the same point on the equator. The answer is '{answer}'."
    if 'pendulum' in q and ('period' in q or 'depend' in q or 'mass' in q):
        return f"The period of a simple pendulum T = 2π√(L/g) depends only on length (L) and gravitational acceleration (g). It does NOT depend on mass or amplitude (for small angles). The answer is '{answer}'."
    if 'beat' in q and ('frequency' in q or 'hz' in q or 'tuning fork' in q):
        return f"Beat frequency = |f₁ - f₂|. When two sources of slightly different frequencies interfere, you hear periodic amplitude variations at the beat frequency. The answer is '{answer}'."
    if 'polariz' in q:
        return f"Polarization restricts light waves to vibrate in a single plane. Polarizing sunglasses block horizontally polarized light (glare from surfaces) while transmitting vertically polarized light. The answer is '{answer}'."
    if 'interference' in q and ('electron' in q or 'double slit' in q or 'pattern' in q):
        return f"Wave-particle duality: electrons (and other particles) exhibit interference patterns in double-slit experiments, confirming they have wave-like properties. The answer is '{answer}'."
    if 'rocket' in q and ('law' in q or 'propulsion' in q or 'newton' in q):
        return f"Rockets work by Newton's Third Law: the rocket pushes exhaust gases backward (action), and the gases push the rocket forward (reaction) with equal force. The answer is '{answer}'."

    # Geometry: Logic / proof concepts
    if 'negation' in q or ('~' in question_text and ('true' in q or 'false' in q)):
        return f"Negation (~p or ¬p) reverses the truth value: if p is true, ~p is false, and vice versa. Negation simply adds 'not' to the statement. The answer is '{answer}'."
    if 'counterexample' in q:
        return f"A counterexample is a specific case that disproves a statement. Finding just ONE counterexample proves a universal claim is false. The answer is '{answer}'."
    if 'random walk' in q:
        return f"A random walk is a path made of successive random steps. In mathematics and physics, it models diffusion, stock prices, and other stochastic processes. The answer is '{answer}'."
    if 'converse' in q and ('inverse' in q or 'contrapositive' in q or 'statement' in q):
        return f"For a conditional p → q: Converse = q → p; Inverse = ~p → ~q; Contrapositive = ~q → ~p. The contrapositive is logically equivalent to the original. The answer is '{answer}'."
    if 'converse' in q and ('if' in q or 'then' in q or 'conditional' in q):
        return f"The converse of 'If p, then q' is 'If q, then p.' The converse is NOT logically equivalent to the original; it may be true or false independently. The answer is '{answer}'."
    if ('law of detachment' in q) or ('syllogism' in q) or ('a→b' in q.replace(' ', '') and 'b→c' in q.replace(' ', '')):
        return f"Law of Detachment: if p → q is true and p is true, then q is true. Law of Syllogism (transitivity): if p → q and q → r, then p → r. The answer is '{answer}'."
    if 'proof' in q and ('begin' in q or 'start' in q or 'first' in q or 'structure' in q or 'justify' in q or 'justifies' in q):
        return f"A proof begins with the given information and what needs to be proved. Each step must be justified by a definition, postulate, or previously proven theorem. The answer is '{answer}'."

    # Geometry: Properties (symmetric, transitive, reflexive)
    if 'symmetric property' in q or ('symmetric' in q and ('property' in q or 'states' in q)):
        return f"The Symmetric Property of Congruence/Equality states: if A = B, then B = A. Order doesn't matter in equality or congruence. The answer is '{answer}'."
    if 'transitive property' in q or ('transitive' in q and ('property' in q or 'if.*and.*then' in q)):
        return f"The Transitive Property states: if A = B and B = C, then A = C. It allows you to chain equalities/congruences together. The answer is '{answer}'."
    if 'reflexive property' in q or ('reflexive' in q and 'property' in q):
        return f"The Reflexive Property states that any quantity is equal to itself: A = A. This is often used as a starting point in proofs. The answer is '{answer}'."

    # Logic: Law of Detachment / Syllogism (broader catch)  
    if 'all' in q and 'then' in answer.lower() or ('law of detachment' in answer.lower() or 'law of syllogism' in answer.lower()):
        return f"Law of Detachment: if p → q is true and p is true, then q is true. Law of Syllogism: if p → q and q → r, then p → r. The answer is '{answer}'."

    # AP Calculus: Chain rule with specific function notation (LaTeX)
    if re.search(r'g\s*\'\s*\(\s*x\s*\)|h\s*\'\s*\(\s*x\s*\)', q) or ("$g'(x)$" in question_text or "$h'(x)$" in question_text):
        return f"Apply the chain rule: d/dx[f(g(x))] = f'(g(x))·g'(x). Identify the outer and inner functions, differentiate each, and multiply. The answer is {answer}."

    # AP Statistics: Mean definition
    if 'mean is' in q or ('mean' in q and ('average' in q or 'definition' in q or 'sum' in q)):
        return f"The mean (average) is calculated by adding all values and dividing by the number of values: x̄ = Σxᵢ / n. It is sensitive to outliers. The answer is '{answer}'."

    # AP Human Geography: Crude birth/death rate 
    if 'crude' in q and ('birth' in q or 'death' in q) and 'rate' in q:
        return f"Crude birth rate (CBR) and crude death rate (CDR) are measured as the number of births or deaths per 1,000 people per year. They are key indicators in the demographic transition model. The answer is '{answer}'."

    # Geometry: Probability / simulation (expected outcomes)
    if ('expect' in q or 'expected' in q or 'simulate' in q or 'simulation' in q) and ('roll' in q or 'die' in q or 'dice' in q or 'coin' in q or 'times' in q):
        return f"Expected value = probability × number of trials. For a fair die, each face has P = 1/6. Over n trials, expect about n/6 occurrences of each number. The answer is {answer}."

    # Geometry: Marble / drawing with/without replacement
    if ('bag' in q or 'marble' in q or 'draw' in q) and ('red' in q or 'blue' in q or 'green' in q) and ('replace' in q or 'p(' in q or 'probability' in q):
        return f"With replacement: P(A then B) = P(A) × P(B) since events are independent. Without replacement: probabilities change after each draw. Multiply the individual probabilities. The answer is {answer}."

    # ─── Answer-text matching ─────────────────────────────────────────────
    # When the question asks "Which process/structure/concept...?" and the answer
    # contains a known science term, provide a definition-based explanation.
    answer_templates = {
        # Biology - Processes
        'glycolysis': "Glycolysis occurs in the cytoplasm, splitting one glucose molecule into two pyruvate molecules, producing a net gain of 2 ATP and 2 NADH. It does not require oxygen.",
        'krebs cycle': "The Krebs cycle (citric acid cycle) occurs in the mitochondrial matrix. Acetyl-CoA is oxidized, producing CO₂, NADH, FADH₂, and ATP (GTP).",
        'citric acid cycle': "The citric acid cycle (Krebs cycle) occurs in the mitochondrial matrix. Acetyl-CoA is oxidized, producing CO₂, NADH, FADH₂, and ATP (GTP).",
        'electron transport chain': "The electron transport chain in the inner mitochondrial membrane uses NADH and FADH₂ to create a proton gradient, which drives ATP synthase to produce the majority of ATP (~30-32 per glucose).",
        'fermentation': "Fermentation is an anaerobic process that regenerates NAD⁺ so glycolysis can continue without oxygen. Lactic acid fermentation produces lactate; alcoholic fermentation produces ethanol and CO₂.",
        'photosynthesis': "Photosynthesis converts light energy to chemical energy: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂. Light reactions occur in the thylakoids; the Calvin cycle occurs in the stroma.",
        'cellular respiration': "Cellular respiration breaks down glucose to produce ATP: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP. It includes glycolysis, the Krebs cycle, and the electron transport chain.",
        'transcription': "Transcription is the process of creating mRNA from a DNA template. RNA polymerase reads the template strand 3'→5' in the nucleus.",
        'translation': "Translation is protein synthesis at the ribosome, where mRNA codons are matched with tRNA anticodons carrying specific amino acids to build a polypeptide chain.",
        'dna replication': "DNA replication is semiconservative — each new double helix contains one original and one new strand. Helicase unwinds, primase adds primers, DNA polymerase synthesizes.",
        'mitosis': "Mitosis is cell division that produces two genetically identical daughter cells. It includes prophase, metaphase, anaphase, and telophase.",
        'meiosis': "Meiosis is a two-stage cell division producing four haploid gametes, introducing genetic variation through crossing over and independent assortment.",
        'osmosis': "Osmosis is the passive movement of water across a semipermeable membrane from an area of low solute concentration to high solute concentration.",
        'diffusion': "Diffusion is the passive movement of molecules from an area of high concentration to low concentration, driven by the concentration gradient.",
        'active transport': "Active transport moves molecules against their concentration gradient, requiring ATP energy. Examples include the sodium-potassium pump (Na⁺/K⁺ ATPase).",
        'natural selection': "Natural selection is the mechanism of evolution where individuals with favorable traits have greater reproductive success, causing those traits to become more common over generations.",
        'speciation': "Speciation occurs when populations become reproductively isolated. Allopatric speciation involves geographic barriers; sympatric speciation occurs without physical separation.",
        # Biology - Structures
        'mitochondria': "Mitochondria are the 'powerhouse of the cell,' performing cellular respiration to produce ATP. They have a double membrane and their own DNA (evidence for endosymbiosis).",
        'chloroplast': "Chloroplasts are the site of photosynthesis in plant cells. They contain thylakoids (light reactions) and stroma (Calvin cycle), and have their own DNA.",
        'ribosome': "Ribosomes are the sites of protein synthesis (translation). They can be free in the cytoplasm or bound to the rough endoplasmic reticulum.",
        'nucleus': "The nucleus houses the cell's DNA and controls gene expression. It is surrounded by a double membrane (nuclear envelope) with nuclear pores for transport.",
        'cell membrane': "The cell membrane is a phospholipid bilayer that controls what enters and exits the cell. It contains proteins for transport, signaling, and structural support.",
        'golgi apparatus': "The Golgi apparatus modifies, packages, and sorts proteins and lipids received from the ER, then ships them to their destinations via vesicles.",
        'endoplasmic reticulum': "The rough ER (with ribosomes) synthesizes proteins; the smooth ER synthesizes lipids and detoxifies substances.",
        'lysosome': "Lysosomes contain digestive enzymes that break down waste, cellular debris, and foreign invaders. They function at an acidic pH (~5).",
        'vacuole': "Vacuoles are membrane-bound sacs for storage. Plant cells have a large central vacuole that maintains turgor pressure and stores water, nutrients, and waste.",
        # Chemistry
        'ionic bond': "Ionic bonds form between metals and nonmetals through electron transfer, creating oppositely charged ions held together by electrostatic attraction.",
        'covalent bond': "Covalent bonds form between nonmetals through electron sharing. Polar covalent bonds have unequal sharing due to electronegativity differences.",
        'hydrogen bond': "Hydrogen bonds are intermolecular attractions between a hydrogen atom bonded to N, O, or F and a lone pair on another electronegative atom. They explain water's unique properties.",
        'le chatelier': "Le Chatelier's Principle: a system at equilibrium shifts to counteract applied stress (changes in concentration, pressure, or temperature).",
        'oxidation': "Oxidation is the loss of electrons (increase in oxidation number). In redox reactions, one species is oxidized while another is reduced. OIL RIG.",
        'reduction': "Reduction is the gain of electrons (decrease in oxidation number). The reducing agent donates electrons and is itself oxidized.",
        'exothermic': "An exothermic reaction releases heat to the surroundings (ΔH < 0). The products are at a lower energy state than the reactants.",
        'endothermic': "An endothermic reaction absorbs heat from the surroundings (ΔH > 0). The products are at a higher energy state than the reactants.",
        # Physics
        'inertia': "Inertia is the tendency of an object to resist changes in its state of motion. An object at rest stays at rest, and a moving object keeps moving, unless acted on by a net force (Newton's First Law).",
        'momentum': "Momentum (p = mv) is the product of mass and velocity. It is conserved in isolated systems. Greater mass or velocity means greater momentum.",
        'impulse': "Impulse (J = FΔt = Δp) is the change in momentum caused by a force acting over a time interval. A larger force or longer contact time creates greater impulse.",
        'centripetal': "Centripetal acceleration points toward the center of circular motion: a_c = v²/r. The centripetal force (mv²/r) can be provided by gravity, tension, friction, or other forces.",
        'torque': "Torque (τ = rF sin θ) is the rotational equivalent of force. It measures the tendency to cause rotation about an axis.",
        # Environmental Science
        'biodiversity': "Biodiversity refers to the variety of life at genetic, species, and ecosystem levels. Greater biodiversity increases ecosystem resilience and stability.",
        'eutrophication': "Eutrophication occurs when excess nutrients (N, P) enter water bodies, causing algal blooms. Decomposition of dead algae depletes oxygen, creating dead zones.",
        'greenhouse effect': "The greenhouse effect traps infrared radiation via atmospheric gases (CO₂, CH₄, N₂O), warming Earth's surface. Human activities intensify this natural process.",
        # Statistics
        'type i error': "A Type I error is rejecting a true null hypothesis (false positive). Its probability equals α, the significance level.",
        'type ii error': "A Type II error is failing to reject a false null hypothesis (false negative). Power (1 - β) is the probability of avoiding this error.",
        # Biology - More processes
        'anaphase': "Anaphase is the stage of cell division where sister chromatids (mitosis) or homologous chromosomes (meiosis I) are pulled apart to opposite poles by spindle fibers.",
        'metaphase': "During metaphase, chromosomes line up along the cell's equator (metaphase plate), attached to spindle fibers at their centromeres.",
        'prophase': "During prophase, chromatin condenses into visible chromosomes, the nuclear envelope begins to break down, and spindle fibers form.",
        'telophase': "During telophase, chromosomes arrive at opposite poles, the nuclear envelope reforms, and chromosomes begin to decondense. Cytokinesis typically follows.",
        'calvin cycle': "The Calvin cycle (light-independent reactions) occurs in the stroma, using CO₂ and ATP/NADPH from light reactions to produce G3P (glucose precursor).",
        'atp synthase': "ATP synthase is the enzyme that produces ATP from ADP + Pi, driven by the flow of H⁺ ions through it down their concentration gradient (chemiosmosis).",
        'homeostasis': "Homeostasis is the maintenance of stable internal conditions (temperature, pH, glucose) despite external changes, primarily through negative feedback mechanisms.",
        'negative feedback': "Negative feedback reverses deviations from a set point to maintain homeostasis. Example: high blood glucose triggers insulin release, which lowers glucose.",
        'independent variable': "The independent variable is what the researcher deliberately changes or manipulates in an experiment to test its effect on the dependent variable.",
        'dependent variable': "The dependent variable is what is measured or observed in an experiment — it responds to changes in the independent variable.",
        # Physics - More terms
        'velocity': "Velocity is a vector quantity describing both speed and direction of motion. Unlike speed (scalar), velocity can be negative, indicating direction.",
        'acceleration': "Acceleration is the rate of change of velocity: a = Δv/Δt. It's a vector — positive means speeding up (or decelerating in the negative direction).",
        'displacement': "Displacement is the straight-line distance from start to finish with direction (vector). It differs from distance, which is the total path length (scalar).",
        'equilibrium': "An object is in equilibrium when the net force is zero (ΣF = 0). Static equilibrium: at rest. Dynamic equilibrium: moving at constant velocity.",
        'conduction': "Conduction is heat transfer through direct molecular contact. Metals are good conductors; insulators (wood, air) resist heat flow.",
        'convection': "Convection is heat transfer through fluid (liquid/gas) movement. Warm fluid rises, cool fluid sinks, creating convection currents.",
        'radiation': "Radiation is heat transfer through electromagnetic waves — no medium needed. All objects emit thermal radiation; hotter objects emit more.",
        # Environmental Science answers
        'primary succession': "Primary succession begins on bare, lifeless surfaces (rock, lava). Pioneer species like lichens colonize first, gradually building soil for more complex communities.",
        'secondary succession': "Secondary succession occurs after a disturbance (fire, flood) in areas where soil remains. It progresses faster than primary succession.",
        'point source': "Point source pollution comes from a single identifiable location (factory pipe, sewage plant). It's easier to regulate than nonpoint source pollution.",
        'nonpoint source': "Nonpoint source pollution comes from diffuse, widespread origins like agricultural runoff, urban stormwater, or atmospheric deposition.",
        # Human Geography answers
        'relocation diffusion': "Relocation diffusion occurs when people physically move and bring their cultural traits to a new location (e.g., immigration spreading cuisines and languages).",
        'hierarchical diffusion': "Hierarchical diffusion spreads from authority figures or large cities downward through a hierarchy (e.g., fashion trends from major cities to smaller towns).",
        'contagious diffusion': "Contagious diffusion spreads rapidly through direct contact with nearby people, like a disease or viral social media trend.",
        'stimulus diffusion': "Stimulus diffusion occurs when a cultural trait inspires adaptation rather than direct adoption (e.g., McDonald's modifying menus for local tastes).",
        # Chemistry - More answer terms
        'neutrons': "Neutrons are neutral (uncharged) subatomic particles in the nucleus. Isotopes of an element differ in the number of neutrons, which affects mass but not chemical properties.",
        'protons': "Protons are positively charged particles in the nucleus. The number of protons (atomic number) defines the element's identity.",
        'sublimation': "Sublimation is the direct phase change from solid to gas, bypassing the liquid phase (e.g., dry ice turning to CO₂ gas).",
        'deposition': "Deposition is the direct phase change from gas to solid (the reverse of sublimation), such as frost forming on cold surfaces.",
        'plasma': "Plasma is the fourth state of matter — an ionized gas with free electrons and ions. Found in stars, lightning, and fluorescent lights.",
        'isotope': "Isotopes are atoms of the same element with different numbers of neutrons, giving them different mass numbers but identical chemical properties.",
        # Biology - More specific terms
        'starch': "Starch is a polysaccharide used by plants for energy storage. It consists of amylose (unbranched) and amylopectin (branched) chains of glucose.",
        'glycogen': "Glycogen is a highly branched polysaccharide used by animals for energy storage, primarily in the liver and muscles.",
        'cellulose': "Cellulose is a structural polysaccharide in plant cell walls. Its β-1,4 glycosidic linkages form rigid fibers that provide structural support.",
        'phospholipid bilayer': "The phospholipid bilayer is the foundation of cell membranes — hydrophilic heads face outward, hydrophobic tails face inward, creating a selectively permeable barrier.",
        'crossing over': "Crossing over occurs during prophase I of meiosis when homologous chromosomes exchange genetic material, increasing genetic diversity.",
        'diploid': "Diploid cells (2n) contain two complete sets of chromosomes — one from each parent. In humans, diploid cells have 46 chromosomes.",
        'haploid': "Haploid cells (n) contain one set of chromosomes. Gametes (sperm and egg) are haploid. In humans, haploid = 23 chromosomes.",
        # Human Geography - More terms
        'formal region': "A formal region is defined by uniform characteristics (language, climate, government) present throughout the area.",
        'functional region': "A functional region is organized around a central hub or node, defined by connections and interactions (e.g., a city's metro area).",
        'vernacular region': "A vernacular (perceptual) region is defined by cultural identity and popular perception rather than official boundaries (e.g., 'the South').",
        'colonialism': "Colonialism is the practice of one nation controlling another territory, exploiting its resources and people. It profoundly shaped modern political boundaries.",
        'nationalism': "Nationalism is devotion and loyalty to one's nation, often based on shared culture, language, or ethnicity. It can unite or divide populations.",
        'sovereignty': "Sovereignty is supreme authority over a territory. A sovereign state has independent control of domestic and foreign affairs.",
        # Math - More answer terms
        'inverse': "An inverse function f⁻¹(x) 'undoes' the original function. To find it: swap x and y, then solve for y.",
        'rational': "A rational expression is a fraction with polynomials in the numerator and/or denominator. The domain excludes values that make the denominator zero.",
        'asymptote': "An asymptote is a line that a graph approaches but never reaches. Vertical asymptotes occur at undefined points; horizontal asymptotes describe end behavior.",
        # More chemistry terms
        'covalent': "A covalent bond forms when two atoms share electrons. Nonpolar covalent bonds share equally; polar covalent bonds share unequally due to electronegativity differences.",
        'ionic': "An ionic bond forms through electron transfer between a metal and nonmetal, creating oppositely charged ions held together by electrostatic attraction.",
        'physical property': "A physical property can be observed without changing the substance's composition: color, density, melting point, boiling point, hardness, malleability.",
        'chemical change': "A chemical change produces a new substance with different properties. Signs: gas production, color change, precipitate formation, energy change, new odor.",
        'physical change': "A physical change alters form or appearance without changing chemical composition. Examples: melting, freezing, dissolving, cutting.",
        # DNA / genetics terms
        'adenine': "In DNA, adenine (A) pairs with thymine (T) through two hydrogen bonds. In RNA, adenine pairs with uracil (U). This base pairing is fundamental to genetic information storage.",
        'thymine': "Thymine (T) is a pyrimidine base in DNA that pairs with adenine (A). In RNA, uracil (U) replaces thymine.",
        'guanine': "Guanine (G) is a purine base that pairs with cytosine (C) through three hydrogen bonds in both DNA and RNA.",
        'cytosine': "Cytosine (C) is a pyrimidine base that pairs with guanine (G) through three hydrogen bonds in both DNA and RNA.",
        'double helix': "DNA has a double helix structure — two antiparallel strands of nucleotides wound around each other, connected by complementary base pairs (A-T, G-C).",
        'nuclear envelope': "The nuclear envelope is a double membrane with pores that encloses the nucleus, regulating transport between the nucleus and cytoplasm.",
        # Ecology terms
        'decomposer': "Decomposers (bacteria, fungi) break down dead organic matter, releasing nutrients back into the ecosystem for producers to use again.",
        'trophic level': "Trophic levels describe positions in a food chain: producers (Level 1), primary consumers (2), secondary consumers (3), tertiary consumers (4). Energy decreases ~90% per level.",
        'food web': "A food web shows the interconnected food chains in an ecosystem, illustrating how energy and nutrients flow through multiple pathways.",
        # Chemistry acid-base answer terms
        'arrhenius': "An Arrhenius acid produces H⁺ in water; an Arrhenius base produces OH⁻ in water. This is the most restrictive acid-base definition.",
        'lewis acid': "A Lewis acid accepts an electron pair; a Lewis base donates an electron pair. This is the broadest acid-base definition.",
        'lewis base': "A Lewis base donates an electron pair to form a coordinate covalent bond. Common examples include NH₃, H₂O, and halide ions.",
        'litmus': "Litmus paper is an acid-base indicator: it turns red in acidic solutions and blue in basic solutions.",
        'phenolphthalein': "Phenolphthalein is an indicator that turns pink/magenta in basic solutions (pH > 8.2) and is colorless in acidic solutions.",
        'neutralization': "Neutralization is an acid-base reaction producing water and a salt: Acid + Base → Salt + H₂O.",
        'conjugate acid': "A conjugate acid forms when a base gains a proton (H⁺). Every base has a conjugate acid.",
        'conjugate base': "A conjugate base forms when an acid loses a proton (H⁺). Every acid has a conjugate base.",
        # Physics answer terms
        'generator': "A generator converts mechanical energy into electrical energy through electromagnetic induction (Faraday's Law).",
        'electromagnetic induction': "Electromagnetic induction produces an EMF when magnetic flux through a conductor changes (Faraday's Law: ε = -dΦ/dt).",
        'quark': "Quarks are fundamental particles. Protons contain two up quarks and one down quark (uud); neutrons contain one up and two down (udd).",
        'gamma ray': "Gamma rays are the highest-energy electromagnetic radiation, emitted during nuclear transitions. They have no charge or mass.",
        # Biology answer terms
        'omnivore': "An omnivore eats both plants and animals. Examples include humans, bears, and pigs.",
        'herbivore': "A herbivore eats only plants. Adaptations include flat teeth for grinding and long digestive tracts.",
        'carnivore': "A carnivore eats only animals. Adaptations include sharp teeth, claws, and strong jaw muscles.",
        'resource partitioning': "Resource partitioning reduces competition by dividing resources — species may use different food sources, habitats, or be active at different times.",
        'light reactions': "Light reactions occur in the thylakoid membranes, converting light energy to ATP and NADPH while splitting water and releasing O₂.",
        'photosystem': "Photosystems are protein complexes in thylakoids that absorb light energy. PSII splits water; PSI reduces NADP⁺ to NADPH.",
        'thylakoid': "Thylakoids are membrane structures in chloroplasts where light-dependent reactions occur. Their stacked arrangement (grana) increases surface area.",
        'chemiosmosis': "Chemiosmosis uses a proton gradient across a membrane to drive ATP synthase, producing ATP from ADP + Pi.",
        # AP Statistics answer terms
        'stratified': "Stratified sampling divides the population into homogeneous groups (strata) and randomly samples from each, ensuring representation of all subgroups.",
        'cluster': "Cluster sampling randomly selects entire groups (clusters), then surveys all members within chosen clusters. It's practical when populations are geographically spread.",
        'systematic': "Systematic sampling selects every kth individual from a list. It's simple but can be biased if the list has a periodic pattern.",
        # Nuclear chemistry answers
        'alpha particle': "Alpha particles (⁴₂He) consist of 2 protons and 2 neutrons. They are heavy, doubly charged, and stopped by paper/skin.",
        'beta particle': "Beta particles are high-energy electrons (β⁻) or positrons (β⁺) emitted during nuclear decay. They are stopped by aluminum foil.",
        'half-life': "Half-life is the time for half of a radioactive sample to decay. After n half-lives, the remaining fraction = (1/2)ⁿ.",
        'fission': "Nuclear fission splits heavy nuclei into lighter ones, releasing neutrons and energy. It's the basis for nuclear power plants.",
        'fusion': "Nuclear fusion combines light nuclei into heavier ones, releasing enormous energy. It requires extremely high temperatures (millions of degrees).",
        # Logic answers
        'counterexample': "A counterexample is a single case that disproves a general statement. One counterexample is sufficient to prove a claim false.",
        'negation': "Negation (~p or ¬p) flips the truth value of a statement. If p is true, ~p is false; if p is false, ~p is true.",
        'contrapositive': "The contrapositive of p → q is ~q → ~p. It is logically equivalent to the original conditional statement.",
        'converse': "The converse of p → q is q → p. Unlike the contrapositive, the converse is NOT logically equivalent to the original.",
    }

    for term, explanation in answer_templates.items():
        if term in a and term not in q:
            return f"{explanation} The answer is '{answer}'."

    return None


# ─── Main Explanation Generator ───────────────────────────────────────────────

def generate_explanation(question_text, options, correct_answer, wrong_answers, lesson_content, course_name):
    """
    Generate a high-quality explanation using:
    1. Math step detection
    2. Lesson content matching
    3. Wrong answer analysis
    4. Subject-aware fallback
    """
    distractor = format_distractor_analysis(question_text, correct_answer, wrong_answers, course_name)

    # 1. Try math-specific explanation first
    math_expl = try_math_explanation(question_text, correct_answer, options)
    if math_expl:
        if distractor:
            return f"{math_expl} {distractor}"
        return math_expl

    # 2. Try science-specific explanation
    sci_expl = try_science_explanation(question_text, correct_answer, course_name)
    if sci_expl:
        if distractor:
            return f"{sci_expl} {distractor}"
        return sci_expl

    # 3. Try to find relevant content from lesson summary
    if lesson_content:
        relevant = find_relevant_sentences(lesson_content, question_text, correct_answer, max_sentences=2)
        if relevant:
            # Build explanation from lesson content
            content_text = ' '.join(relevant)

            # Clean up: remove trailing fragments
            if not content_text.rstrip()[-1] in '.!?':
                last_period = content_text.rfind('.')
                if last_period > len(content_text) * 0.4:
                    content_text = content_text[:last_period + 1]
                else:
                    content_text += '.'

            # Truncate if too long
            if len(content_text) > 350:
                last_period = content_text[:350].rfind('.')
                if last_period > 150:
                    content_text = content_text[:last_period + 1]
                else:
                    content_text = content_text[:347] + '...'

            # Only add distractor if content isn't already very long
            if distractor and len(content_text) < 250:
                return f"{content_text} {distractor}"
            return content_text

    # 3. Fallback: Generate from question analysis + wrong answers
    return generate_fallback_explanation(question_text, correct_answer, wrong_answers, course_name)


def generate_fallback_explanation(question_text, correct_answer, wrong_answers, course_name):
    """
    Fallback for when no lesson content matched and it's not a math problem.
    Generates educational explanations by analyzing the question structure,
    answer content, and wrong answers.
    """
    q = question_text.lower().strip()
    correct = correct_answer.strip()
    distractor = format_distractor_analysis(question_text, correct_answer, wrong_answers, course_name)

    # Check for NOT/EXCEPT questions
    is_not_question = any(phrase in q for phrase in [
        'is not', 'are not', 'not a ', 'not an ', 'not true',
        'does not', 'do not', 'cannot', 'except', 'least likely',
        'would not', 'is false', 'incorrect'
    ])

    if is_not_question:
        base = f"'{correct}' is the exception here because it does not fit the category or criteria described in the question."
        if distractor:
            return f"{base} {distractor}"
        return base

    # True/False questions
    if correct.lower().startswith('true') or correct.lower().startswith('false'):
        # Extract the statement being evaluated
        base = f"The statement is {correct}."
        if distractor:
            return f"{base} {distractor}"
        return base

    # Definition questions: "What is X?"
    match = re.match(r'what (?:is|are|does)\s+(?:a |an |the )?(.+?)[\?.]?$', q)
    if match:
        topic = match.group(1).strip().rstrip('?')
        base = f"{topic.capitalize()} is defined as {correct.lower() if correct[0].isupper() and len(correct) > 20 else correct}."
        if distractor:
            return f"{base} {distractor}"
        return base

    # "Which of the following" / selection questions
    if 'which of the following' in q or q.startswith('which'):
        base = f"'{correct}' is correct because it most precisely fits the criteria described in the question."
        if distractor:
            return f"{base} {distractor}"
        return base

    # "How" process/mechanism questions
    if q.startswith('how'):
        base = f"The answer is '{correct}' — this describes the mechanism or process involved."
        if distractor:
            return f"{base} {distractor}"
        return base

    # "Why" causation questions
    if q.startswith('why'):
        base = f"The reason is '{correct}' — this provides the underlying cause or justification."
        if distractor:
            return f"{base} {distractor}"
        return base

    # "When" temporal questions
    if q.startswith('when'):
        base = f"This occurs when {correct.lower() if correct[0].isupper() and len(correct) > 15 else correct}."
        if distractor:
            return f"{base} {distractor}"
        return base

    # "Where" location questions
    if q.startswith('where'):
        base = f"This takes place in/at {correct}."
        if distractor:
            return f"{base} {distractor}"
        return base

    # Calculate/solve
    if any(word in q for word in ['calculate', 'solve', 'find the value', 'compute', 'evaluate', 'simplify']):
        base = f"Working through the calculation step by step yields {correct}."
        if distractor:
            return f"{base} {distractor}"
        return base

    # Function/purpose/role
    if any(word in q for word in ['function of', 'purpose of', 'role of', 'responsible for']):
        # Try to extract what we're asking about
        for pattern in [r'function of (?:the |a )?(.+?)[\?]?$', r'purpose of (?:the |a )?(.+?)[\?]?$', r'role of (?:the |a )?(.+?)[\?]?$']:
            m = re.search(pattern, q)
            if m:
                thing = m.group(1).strip().rstrip('?')
                base = f"The primary function of {thing} is {correct.lower() if correct[0].isupper() and len(correct) > 15 else correct}."
                if distractor:
                    return f"{base} {distractor}"
                return base

    # Fill-in / completion style ("The ___ is...")
    if '___' in question_text or '...' in question_text:
        base = f"The blank is filled by '{correct}', which completes the statement accurately."
        if distractor:
            return f"{base} {distractor}"
        return base

    # Default: still reference the answer and distractors meaningfully
    base = f"The correct answer is '{correct}'."
    if distractor:
        return f"{base} {distractor}"
    return base


# ─── File Processing ──────────────────────────────────────────────────────────

def process_file(filepath, course_name):
    """Process a single JSON file and regenerate all explanations."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    generated = 0
    content_matched = 0
    math_matched = 0
    science_matched = 0
    fallback_count = 0

    for lesson_key, lesson in data.items():
        if not isinstance(lesson, dict) or 'quiz_questions' not in lesson:
            continue

        # Get lesson content for this lesson
        lesson_content = get_lesson_content(lesson)

        for q in lesson['quiz_questions']:
            question_text = q.get('question_text', q.get('question', ''))
            options = q.get('options', [])

            # Separate correct and wrong answers
            correct_answer = ''
            wrong_answers = []
            for opt in options:
                if isinstance(opt, dict):
                    if opt.get('is_correct'):
                        correct_answer = opt.get('text', '')
                    else:
                        wrong_answers.append(opt.get('text', ''))

            if not question_text or not correct_answer:
                continue

            # Generate new explanation
            explanation = generate_explanation(
                question_text, options, correct_answer,
                wrong_answers, lesson_content, course_name
            )

            # Track which method was used
            math_check = try_math_explanation(question_text, correct_answer, options)
            sci_check = try_science_explanation(question_text, correct_answer, course_name)
            if math_check:
                math_matched += 1
            elif sci_check:
                science_matched += 1
            elif lesson_content:
                relevant = find_relevant_sentences(lesson_content, question_text, correct_answer, max_sentences=2)
                if relevant:
                    content_matched += 1
                else:
                    fallback_count += 1
            else:
                fallback_count += 1

            q['explanation'] = explanation
            generated += 1

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return generated, content_matched, math_matched, science_matched, fallback_count


def main():
    print("=" * 70)
    print("  Improved Explanation Generator v2")
    print("  Generating content-aware explanations for ALL courses")
    print("=" * 70)

    total_generated = 0
    total_content = 0
    total_math = 0
    total_science = 0
    total_fallback = 0

    # Process regular courses
    print("\n--- Regular Courses ---")
    for filename in sorted(os.listdir(CONTENT_DIR)):
        if not filename.endswith('.json'):
            continue
        filepath = os.path.join(CONTENT_DIR, filename)
        if not os.path.isfile(filepath):
            continue

        course_name = filename.replace('_lessons.json', '')
        gen, content, math, science, fallback = process_file(filepath, course_name)
        total_generated += gen
        total_content += content
        total_math += math
        total_science += science
        total_fallback += fallback
        print(f"  {filename}: {gen} explanations "
              f"(content: {content}, math: {math}, science: {science}, fallback: {fallback})")

    # Process AP courses
    print("\n--- AP Courses ---")
    for filename in sorted(os.listdir(AP_DIR)):
        if not filename.endswith('.json'):
            continue
        filepath = os.path.join(AP_DIR, filename)
        if not os.path.isfile(filepath):
            continue

        course_name = filename.replace('_lessons.json', '')
        gen, content, math, science, fallback = process_file(filepath, course_name)
        total_generated += gen
        total_content += content
        total_math += math
        total_science += science
        total_fallback += fallback
        print(f"  {filename}: {gen} explanations "
              f"(content: {content}, math: {math}, science: {science}, fallback: {fallback})")

    print(f"\n{'=' * 70}")
    print(f"  TOTAL: {total_generated} explanations generated")
    print(f"    Content-matched: {total_content} ({total_content/max(total_generated,1)*100:.1f}%)")
    print(f"    Math-detected:   {total_math} ({total_math/max(total_generated,1)*100:.1f}%)")
    print(f"    Science-specific:{total_science} ({total_science/max(total_generated,1)*100:.1f}%)")
    print(f"    Fallback:        {total_fallback} ({total_fallback/max(total_generated,1)*100:.1f}%)")
    print(f"{'=' * 70}")


if __name__ == '__main__':
    main()
