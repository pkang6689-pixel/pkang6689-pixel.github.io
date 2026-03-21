#!/usr/bin/env python3
"""Replace placeholder questions in Linear Algebra U5-U6 with quality questions."""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "linear_algebra_lessons.json")

def make_qs(raw_list):
    result = []
    for i, (qt, opts, exp) in enumerate(raw_list, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        result.append({
            "question_number": i, "question_text": qt, "attempted": 2,
            "data_i18n": None, "options": options, "explanation": exp
        })
    return result

ALL_QS = {
# ── U5 L5.1: Definition of Vector Spaces ──
"u5_l5.1": [
    ("A vector space must satisfy how many axioms?", ["4", "6", "8", "*10"], "There are 10 axioms: closure under addition/scalar multiplication, associativity, commutativity, zero vector, additive inverses, and four scalar multiplication properties."),
    ("Which of the following is a vector space over ℝ?", ["the set of positive reals under standard addition", "*the set of all 2×2 matrices with standard addition and scalar multiplication", "the set of integers under standard operations", "the set of polynomials of degree exactly 3"], "The set of all 2×2 matrices satisfies all 10 axioms. Polynomials of degree exactly 3 is not closed under addition."),
    ("The zero vector in the vector space of polynomials of degree ≤ n is:", ["1", "x", "x^n", "*the zero polynomial (all coefficients = 0)"], "The zero polynomial has all zero coefficients and serves as the additive identity."),
    ("Closure under addition means that for any u, v in V:", ["u + v is in ℝ", "*u + v is also in V", "u + v = 0", "u + v is defined but may not be in V"], "The sum of any two vectors in the space must remain in the space."),
    ("Closure under scalar multiplication means for any scalar c and v in V:", ["cv = v", "cv is in ℝ only", "cv = 0", "*cv is also in V"], "Scaling any vector by any scalar must produce another vector in the same space."),
    ("The set {(x, y) : x + y = 1} is NOT a vector space because:", ["it has no elements", "it contains zero", "*it does not contain the zero vector (0+0≠1)", "it is infinite"], "The zero vector (0,0) fails the condition 0+0=1, violating the zero vector axiom."),
    ("Which axiom states v + w = w + v?", ["associativity", "*commutativity of addition", "closure", "distributivity"], "Commutativity of addition requires that the order of addition does not matter."),
    ("In the vector space ℝ³, the additive inverse of (1, −2, 3) is:", ["(1, 2, 3)", "(−1, 2, 3)", "(0, 0, 0)", "*(−1, 2, −3)"], "Negate each component: the additive inverse of (a,b,c) is (−a,−b,−c)."),
    ("The axiom 1·v = v for all v is called:", ["closure", "*the multiplicative identity axiom", "commutativity", "the zero axiom"], "Scalar multiplication by 1 must leave every vector unchanged."),
    ("Is the empty set a vector space?", ["yes, trivially", "*no, it lacks a zero vector", "yes, all axioms are vacuously true", "only if defined over ℝ"], "A vector space must contain at least the zero vector, so the empty set cannot qualify."),
    ("The vector space of continuous functions on [0,1] has dimension:", ["1", "0", "100", "*infinite"], "The space of continuous functions is infinite-dimensional — no finite basis spans it."),
    ("For vector spaces, 0·v always equals:", ["v", "1", "−v", "*the zero vector"], "This follows from the axioms: 0·v = (0+0)·v − 0·v = 0."),
    ("The set of solutions to a homogeneous linear system forms:", ["a ring", "*a vector space (subspace of ℝⁿ)", "an empty set", "a field"], "The solution set of Ax = 0 is closed under addition and scalar multiplication."),
    ("c(u + v) = cu + cv is the _____ property.", ["associative", "commutative", "*distributive (scalar over vector addition)", "identity"], "This distributive law connects scalar multiplication with vector addition."),
    ("(c + d)v = cv + dv is the _____ property.", ["associative", "commutative", "*distributive (scalar addition over vector)", "closure"], "This law distributes vector scaling over the sum of two scalars."),
    ("The set {(x, 0) : x ∈ ℝ} is:", ["not a vector space", "*a vector space (the x-axis)", "only a group", "a field"], "It contains the zero vector and is closed under addition and scalar multiplication."),
    ("A vector space must be defined over:", ["only ℝ", "only ℤ", "any set of numbers", "*a field (ℝ, ℂ, ℚ, etc.)"], "Scalars come from a field, which provides addition, multiplication, and inverses."),
    ("The vector space Pₙ consists of all polynomials of degree:", ["exactly n", "at least n", "greater than n", "*at most n (including the zero polynomial)"], "Pₙ includes all polynomials from degree 0 up to degree n, plus the zero polynomial."),
    ("Which fails to be a vector space? The set of all:", ["2×3 matrices", "continuous functions on ℝ", "*invertible 2×2 matrices", "polynomials of degree ≤ 5"], "The sum of two invertible matrices need not be invertible, violating closure under addition."),
    ("The additive identity (zero vector) in a vector space is:", ["not always required", "only in ℝⁿ", "chosen arbitrarily", "*unique (there is exactly one zero vector)"], "The uniqueness of the zero vector follows from the axioms."),
],

# ── U5 L5.2: Subspaces ──
"u5_l5.2": [
    ("A subspace of V must contain:", ["all vectors in V", "at least two vectors", "only unit vectors", "*the zero vector of V"], "The zero vector test is the first check: every subspace contains the zero vector."),
    ("To verify a subset W is a subspace, check:", ["only closure under addition", "only that W is nonempty", "*closure under addition AND scalar multiplication (plus nonemptiness)", "only that W is finite"], "Both closure properties plus containing at least the zero vector are needed."),
    ("Which is NOT a subspace of ℝ²?", ["the origin {(0,0)}", "any line through the origin", "*the line y = x + 1", "ℝ² itself"], "y = x+1 does not pass through the origin, so it doesn't contain the zero vector."),
    ("The intersection of two subspaces is:", ["never a subspace", "sometimes a subspace", "empty", "*always a subspace"], "The intersection of subspaces is always a subspace (closed under both operations and contains 0)."),
    ("The union of two subspaces is a subspace:", ["always", "*only if one is contained in the other", "never", "only in ℝ²"], "Unless one subspace contains the other, their union fails closure under addition."),
    ("A plane through the origin in ℝ³ is:", ["not a subspace", "*a 2-dimensional subspace", "a 3-dimensional subspace", "1-dimensional"], "Planes through the origin are closed under addition and scalar multiplication with dimension 2."),
    ("The trivial subspace of Rⁿ is:", ["all of Rⁿ", "any line", "any plane", "*{0} (the set containing only the zero vector)"], "The smallest possible subspace contains just the zero vector."),
    ("The column space of an m×n matrix A is a subspace of:", ["ℝⁿ", "*ℝᵐ", "ℝᵐˣⁿ", "ℝ¹"], "Columns of A are vectors in ℝᵐ, so their span lives in ℝᵐ."),
    ("The null space of an m×n matrix A is a subspace of:", ["ℝᵐ", "*ℝⁿ", "ℝᵐˣⁿ", "ℝ¹"], "Null space = {x ∈ ℝⁿ : Ax = 0}, so it lives in the domain ℝⁿ."),
    ("The set of solutions to Ax = b (with b ≠ 0) is:", ["a subspace", "always empty", "*not a subspace (it doesn't contain the zero vector)", "the column space"], "If b ≠ 0, then x = 0 is not a solution, so the solution set is not a subspace."),
    ("The sum of two subspaces S₁ + S₂ = {s₁+s₂ : s₁∈S₁, s₂∈S₂} is:", ["not always a subspace", "*always a subspace", "always all of V", "always S₁ or S₂"], "The sum of subspaces is always itself a subspace."),
    ("A subspace of ℝ³ can have dimension:", ["only 3", "only 0 or 3", "*0, 1, 2, or 3", "any positive integer"], "Subspaces of ℝ³ are: {0} (dim 0), lines (dim 1), planes (dim 2), or ℝ³ (dim 3)."),
    ("{(x,y) : x² + y² ≤ 1} (the unit disk) is:", ["a subspace", "*not a subspace (not closed under scalar multiplication)", "a basis", "empty"], "Scaling (1,0) by 2 gives (2,0), which is outside the disk. Closure fails."),
    ("The row space of a matrix is a subspace of:", ["ℝᵐ", "*ℝⁿ (where n is the number of columns)", "ℝᵐˣⁿ", "the null space"], "Rows are n-component vectors, so their span is a subspace of ℝⁿ."),
    ("If W is a subspace and v, w ∈ W, then v − w is:", ["not necessarily in W", "in V but not W", "undefined", "*also in W"], "v − w = v + (−1)w, and both addition and scalar multiplication by −1 preserve membership."),
    ("Span{v₁, v₂, ..., vₖ} is always:", ["linearly independent", "a basis", "*a subspace", "finite-dimensional only"], "The span of any set of vectors is a subspace (it's closed under both operations)."),
    ("{(x, y, z) : x + 2y − z = 0} is a subspace of ℝ³ with dimension:", ["0", "1", "*2", "3"], "One homogeneous equation in 3 unknowns defines a 2-dimensional subspace (a plane through the origin)."),
    ("The set of all upper triangular n×n matrices is:", ["*a subspace of the n×n matrix space", "not closed under addition", "not a subspace", "only closed under scalar multiplication"], "The sum of two upper triangular matrices is upper triangular, and scalar multiples are too."),
    ("The set of all symmetric n×n matrices forms:", ["a non-subspace", "*a subspace of the n×n matrix space", "a field", "a group under multiplication"], "Symmetric matrices are closed under addition and scalar multiplication."),
    ("Complementary subspaces V₁ and V₂ satisfy V₁ ∩ V₂ = {0} and V₁ + V₂ =:", ["V₁", "V₂", "*V (the whole space)", "{0}"], "Complementary subspaces together span the entire space with only the zero vector in common."),
],

# ── U5 L5.3: Linear Independence ──
"u5_l5.3": [
    ("Vectors v₁,...,vₖ are linearly independent if the only solution to c₁v₁ + ... + cₖvₖ = 0 is:", ["c₁ = 1, ..., cₖ = 1", "any real numbers", "c₁ = −1, ..., cₖ = −1", "*c₁ = c₂ = ... = cₖ = 0"], "Linear independence means the trivial combination is the only way to get the zero vector."),
    ("If v₂ = 3v₁, the set {v₁, v₂} is:", ["linearly independent", "*linearly dependent", "a basis for ℝ²", "orthogonal"], "v₂ is a scalar multiple of v₁, so c₁v₁ + c₂v₂ = 0 has nontrivial solutions (e.g., c₁=3, c₂=−1)."),
    ("Any set containing the zero vector is:", ["linearly independent", "*linearly dependent", "a basis", "undefined"], "You can assign a nonzero coefficient to the zero vector (e.g., 1·0 + 0·v₁ + ... = 0), giving a nontrivial relation."),
    ("In ℝ³, the maximum number of linearly independent vectors is:", ["2", "*3", "4", "unlimited"], "ℝ³ has dimension 3, so at most 3 vectors can be linearly independent."),
    ("Checking if {v₁, v₂, v₃} are independent requires solving:", ["v₁ + v₂ + v₃ = 0", "det = 0", "*[v₁ v₂ v₃]c = 0 and checking if only c = 0 works", "three separate equations"], "Place vectors as columns, row-reduce, and check if there are free variables."),
    ("{(1,0), (0,1), (1,1)} in ℝ² is:", ["linearly independent", "*linearly dependent", "a basis for ℝ²", "not a valid set"], "Three vectors in ℝ² (dim 2) must be dependent: (1,1) = (1,0) + (0,1)."),
    ("A single nonzero vector is always:", ["linearly dependent", "a basis", "*linearly independent", "orthogonal to itself"], "There's no nontrivial scalar multiple of a nonzero vector that equals zero."),
    ("If the matrix [v₁|v₂|...|vₖ] has a pivot in every column:", ["the vectors are dependent", "*the vectors are linearly independent", "the vectors span ℝⁿ", "the matrix is square"], "A pivot in every column means no free variables, so only the trivial solution exists."),
    ("Adding a vector to a linearly independent set can make it:", ["always still independent", "*dependent (if the new vector is in the span of the existing ones)", "always dependent", "orthogonal"], "If the new vector is a combination of the others, independence is lost."),
    ("Removing a vector from a linearly dependent set:", ["always makes it independent", "always makes it dependent", "*may or may not result in an independent set", "is not allowed"], "It depends on which vector is removed and the specific dependency relation."),
    ("{e₁, e₂, ..., eₙ} (standard basis vectors) in ℝⁿ are:", ["linearly dependent", "*linearly independent", "not a basis", "only orthogonal"], "The identity matrix row-reduces without free variables; the standard basis is independent."),
    ("Linear dependence of columns of A is equivalent to:", ["det(A) ≠ 0", "*Ax = 0 having a nontrivial solution", "A being invertible", "rank(A) = n"], "Nontrivial null space ↔ free variables ↔ dependent columns."),
    ("If det(A) ≠ 0 for the matrix of column vectors, the vectors are:", ["dependent", "parallel", "*linearly independent", "orthogonal"], "Nonzero determinant means no nontrivial solutions to Ax = 0."),
    ("Two vectors in ℝ² are linearly dependent if and only if they are:", ["perpendicular", "unit vectors", "*parallel (one is a scalar multiple of the other)", "equal"], "In 2D, dependence means the vectors point in the same (or opposite) direction."),
    ("The Wronskian tests linear independence of:", ["matrix columns", "real numbers", "*functions (as solutions to differential equations)", "only polynomials"], "The Wronskian determinant of functions and their derivatives checks functional independence."),
    ("A set of more than n vectors in ℝⁿ is always:", ["independent", "a basis", "orthogonal", "*linearly dependent"], "In an n-dimensional space, any set of more than n vectors must be dependent."),
    ("If {v₁, v₂} is independent and v₃ ∉ span{v₁, v₂}, then {v₁, v₂, v₃} is:", ["linearly dependent", "*linearly independent", "a basis only if n=3", "undefined"], "v₃ not being in the span means there's no way to write it as a combination of v₁ and v₂."),
    ("Linearly independent vectors that span V form:", ["just a subspace", "an independent set only", "*a basis for V", "an overcomplete set"], "A basis is exactly a linearly independent spanning set."),
    ("Geometric interpretation of 3 independent vectors in ℝ³:", ["they lie on a line", "they lie on a plane", "*they span all of 3D space (not coplanar)", "they are perpendicular"], "Three independent vectors in ℝ³ span the full space, but they need not be perpendicular."),
    ("The rank of a matrix equals the number of:", ["rows", "columns", "zero entries", "*linearly independent columns (or rows)"], "Rank counts the maximum number of linearly independent columns, which equals the pivot count."),
],

# ── U5 L5.4: Basis & Dimension ──
"u5_l5.4": [
    ("A basis for a vector space V is:", ["any spanning set", "any independent set", "*a linearly independent spanning set", "only the standard basis"], "A basis must be both independent (no redundancy) and spanning (reaches everything)."),
    ("The dimension of ℝⁿ is:", ["n−1", "n+1", "2n", "*n"], "The standard basis {e₁,...,eₙ} has n vectors, so dim(ℝⁿ) = n."),
    ("The dimension of the space of 2×3 matrices is:", ["2", "3", "5", "*6"], "A 2×3 matrix has 6 entries, each acting as an independent coordinate. Basis: 6 matrix units."),
    ("If V has dimension d, every basis of V has exactly:", ["d+1 vectors", "d−1 vectors", "at most d vectors", "*d vectors"], "All bases of a finite-dimensional space have the same number of elements."),
    ("The standard basis for ℝ³ is:", ["(1,1,1), (0,1,1), (0,0,1)", "(1,0,0), (1,1,0), (1,1,1)", "*(1,0,0), (0,1,0), (0,0,1)", "(1,2,3), (4,5,6), (7,8,9)"], "The standard basis consists of the unit vectors along each coordinate axis."),
    ("dim(Pₙ) — the space of polynomials of degree ≤ n — is:", ["n", "n−1", "2n", "*n+1"], "The basis {1, x, x², ..., xⁿ} has n+1 elements."),
    ("If a set of 4 vectors spans ℝ⁴ and is linearly independent, it is:", ["too large", "too small", "not a basis", "*a basis for ℝ⁴"], "Exactly dim(V) independent vectors that span V form a basis."),
    ("Any linearly independent set in V can be:", ["a basis already", "*extended to a basis for V (by adding more vectors if needed)", "reduced", "made dependent"], "You can always add vectors until you have a basis, as long as you maintain independence."),
    ("Any spanning set for V can be:", ["left unchanged", "made larger", "*reduced to a basis (by removing dependent vectors)", "made empty"], "Remove redundant vectors (those in the span of the rest) until independence is achieved."),
    ("The dimension of the null space of an m×n matrix plus the rank equals:", ["m", "m+n", "mn", "*n (the number of columns)"], "The Rank-Nullity Theorem: rank(A) + nullity(A) = n."),
    ("{ (1,2), (3,6) } spans a subspace of ℝ² with dimension:", ["0", "*1", "2", "3"], "(3,6) = 3·(1,2), so one vector is redundant. The span is a line (dimension 1)."),
    ("A 4×4 matrix with rank 3 has a null space of dimension:", ["0", "3", "4", "*1"], "Rank-Nullity: 3 + nullity = 4, so nullity = 1."),
    ("Two different bases for the same space are related by:", ["addition", "a singular matrix", "*an invertible change-of-basis matrix", "the zero matrix"], "The change-of-basis matrix converts coordinates from one basis to another and must be invertible."),
    ("Dimension is a property of:", ["individual vectors", "matrices only", "scalars", "*the vector space itself (independent of basis choice)"], "Dimension depends only on the space, not on the particular basis chosen."),
    ("The space of symmetric n×n matrices has dimension:", ["n²", "n", "*n(n+1)/2", "n(n−1)/2"], "Symmetric matrices are determined by the diagonal and upper triangle: n(n+1)/2 independent entries."),
    ("The space of n×n skew-symmetric matrices has dimension:", ["n²", "n", "n(n+1)/2", "*n(n−1)/2"], "The diagonal must be zero and the upper triangle determines the rest: n(n−1)/2 entries."),
    ("If dim(V) = n, then any set of n+1 vectors in V is:", ["independent", "a basis", "*linearly dependent", "orthogonal"], "More vectors than the dimension guarantees dependence."),
    ("If dim(V) = n, then any set of n−1 vectors cannot:", ["be independent", "be a subset of a basis", "*span all of V", "exist"], "Fewer than n vectors cannot span an n-dimensional space."),
    ("The column space and row space of a matrix have:", ["different dimensions always", "dimensions that add to n", "*the same dimension (both equal to the rank)", "dimension equal to m+n"], "Column rank = row rank, a fundamental theorem of linear algebra."),
    ("The dimension of the zero subspace {0} is:", ["1", "−1", "undefined", "*0"], "The zero subspace has no basis vectors (the empty set is its basis), giving dimension 0."),
],

# ── U5 L5.5: Span of a Set ──
"u5_l5.5": [
    ("span{v₁, v₂} is the set of all vectors of the form:", ["v₁ + v₂", "v₁ · v₂", "*c₁v₁ + c₂v₂ for all scalars c₁, c₂", "only v₁ and v₂ themselves"], "The span includes every possible linear combination of the given vectors."),
    ("span{(1,0,0)} in ℝ³ is:", ["a point", "*the x-axis (a line)", "a plane", "all of ℝ³"], "All scalar multiples of (1,0,0) trace out the x-axis."),
    ("span{(1,0), (0,1)} in ℝ² is:", ["a line", "just two points", "a triangle", "*all of ℝ²"], "These two independent vectors span the entire plane."),
    ("span of the empty set is:", ["undefined", "all of V", "any line", "*{0} (the zero subspace)"], "By convention, the span of no vectors is just the zero vector."),
    ("Adding a redundant vector to a spanning set:", ["changes the span", "decreases the span", "*leaves the span unchanged", "makes the span empty"], "A redundant vector is already in the span, so including it doesn't enlarge the set."),
    ("span{(1,2), (2,4)} in ℝ² is:", ["all of ℝ²", "a point", "two lines", "*a single line through the origin"], "Since (2,4) = 2·(1,2), the span is just scalar multiples of one vector — a line."),
    ("If v ∈ span{v₁,...,vₖ}, adding v to the set:", ["increases the span", "makes it independent", "*does not change the span", "makes it empty"], "Since v is already a combination of v₁,...,vₖ, adding it is redundant."),
    ("span{v₁, v₂, v₃} could have dimension:", ["only 3", "only 0", "only 0 or 3", "*0, 1, 2, or 3 depending on independence"], "The span's dimension is the number of linearly independent vectors among them."),
    ("To determine if w ∈ span{v₁, v₂}, solve:", ["v₁ · v₂ = w", "w = v₁ × v₂", "*c₁v₁ + c₂v₂ = w for scalars c₁, c₂", "det([v₁,v₂]) = w"], "If the system has a solution for c₁ and c₂, then w is in the span."),
    ("Is (3,5) in span{(1,2), (1,1)}? Solve c₁ + c₂ = 3, 2c₁ + c₂ = 5:", ["no solution", "c₁=0, c₂=3", "*c₁=2, c₂=1 (yes, it's in the span)", "c₁=3, c₂=0"], "Subtract equations: c₁ = 2, then c₂ = 1. Check: 2(1,2) + 1(1,1) = (3,5)."),
    ("The span of any set of vectors is always:", ["linearly independent", "finite", "an independent set", "*a subspace"], "Spans are closed under addition and scalar multiplication and contain the zero vector."),
    ("In ℝ⁴, span{e₁, e₂} is a subspace of dimension:", ["0", "1", "*2", "4"], "Two independent standard basis vectors span a 2D plane in ℝ⁴."),
    ("If S₁ ⊂ S₂ (as sets of vectors), then span(S₁) ⊂ span(S₂):", ["is false", "depends on V", "only when S₁ is empty", "*is true always"], "Adding more vectors to a set can only maintain or enlarge the span, never shrink it."),
    ("span{(1,0,0), (0,1,0), (0,0,1)} in ℝ³ equals:", ["a line", "a plane", "the origin", "*all of ℝ³"], "The three standard basis vectors span the entire 3D space."),
    ("The column space of A = Col(A) is the span of:", ["the rows of A", "the diagonal of A", "*the columns of A", "the entries of A"], "Col(A) is built from all linear combinations of the column vectors of A."),
    ("The span of a single nonzero vector in ℝ³ is:", ["a point", "*a line through the origin", "a plane", "all of ℝ³"], "One nonzero vector spans a 1D subspace, which is a line through the origin."),
    ("Two non-parallel vectors in ℝ³ span:", ["a line", "all of ℝ³", "*a plane through the origin", "a cube"], "Two independent vectors in 3D span a 2D plane through the origin."),
    ("To reduce a spanning set to a basis:", ["add more vectors", "multiply by scalars", "*remove linearly dependent vectors until independence is achieved", "transpose the vectors"], "Iterate: remove any vector that's a combination of the rest until the set is independent."),
    ("span{v₁,...,vₙ} = V combined with independence of {v₁,...,vₙ} means the set is:", ["just a spanning set", "just an independent set", "overcomplete", "*a basis for V"], "A basis is exactly a linearly independent spanning set."),
    ("Geometrically, the span of two independent vectors in ℝⁿ (n ≥ 2) is:", ["always ℝⁿ", "always a line", "a torus", "*a 2D plane through the origin"], "Two linearly independent vectors always span a plane, regardless of the ambient dimension."),
],

# ── U5 L5.6: Null Space & Column Space ──
"u5_l5.6": [
    ("The null space of A is:", ["{Ax : x ∈ ℝⁿ}", "the set of columns of A", "*{x ∈ ℝⁿ : Ax = 0}", "the row space of A"], "Nul(A) consists of all vectors that A maps to the zero vector."),
    ("The column space of A is:", ["the null space", "*{Ax : x ∈ ℝⁿ} = span of columns of A", "the rows of A", "all of ℝⁿ"], "Col(A) is all possible outputs Ax — the span of the columns."),
    ("The null space of a 3×5 matrix is a subspace of:", ["ℝ³", "*ℝ⁵", "ℝ³ˣ⁵", "ℝ¹"], "Null space consists of vectors x ∈ ℝⁿ where n = 5 (the number of columns)."),
    ("The column space of a 3×5 matrix is a subspace of:", ["ℝ⁵", "*ℝ³", "ℝ³ˣ⁵", "ℝ¹"], "Columns are in ℝᵐ where m = 3, so Col(A) ⊆ ℝ³."),
    ("Rank-Nullity Theorem: rank(A) + dim(Nul(A)) =:", ["m", "m + n", "*n (number of columns)", "rank squared"], "The dimensions of the column space and null space always sum to the number of columns."),
    ("If A is 4×6 with rank 3, then dim(Nul(A)) =:", ["1", "2", "*3", "4"], "By Rank-Nullity: 3 + nullity = 6, so nullity = 3."),
    ("Ax = b is consistent if and only if b is in:", ["Nul(A)", "the row space", "*Col(A)", "ℝⁿ"], "The system has a solution precisely when b can be written as a linear combination of A's columns."),
    ("To find a basis for Nul(A), you row-reduce A and:", ["read off the columns", "compute the determinant", "*identify free variables and write the parametric solution", "find eigenvalues"], "Free variables generate the null space vectors; each gives one basis vector."),
    ("To find a basis for Col(A), you row-reduce A and:", ["use the non-pivot columns", "use the reduced columns", "*identify pivot columns and use the corresponding ORIGINAL columns of A", "compute cofactors"], "The pivot columns of A (not the reduced form) form a basis for the column space."),
    ("If A has a trivial null space (only 0), the columns are:", ["dependent", "all zero", "*linearly independent", "all equal"], "Trivial null space means Ax = 0 has only x = 0, which is the definition of independent columns."),
    ("The null space of an invertible n×n matrix is:", ["ℝⁿ", "n-dimensional", "a hyperplane", "*{0} (only the zero vector)"], "Invertible means Ax = 0 has only the trivial solution."),
    ("The column space of an invertible n×n matrix is:", ["a proper subspace", "{0}", "a line", "*all of ℝⁿ"], "Full rank means the columns span the entire space."),
    ("dim(Col(A)) is called the _____ of A:", ["nullity", "trace", "determinant", "*rank"], "The rank is the dimension of the column space."),
    ("The left null space of A is the null space of:", ["A", "A⁻¹", "*Aᵀ", "A²"], "The left null space is Nul(Aᵀ) = {y : Aᵀy = 0}, equivalent to {y : yᵀA = 0ᵀ}."),
    ("The four fundamental subspaces of A are Col(A), Nul(A), Row(A), and:", ["span(A)", "det(A)", "*the left null space Nul(Aᵀ)", "the eigenspace"], "These four subspaces (from A and Aᵀ) are the fundamental subspaces in the theory."),
    ("Row(A) and Nul(A) are _____ subspaces:", ["parallel", "identical", "*orthogonal complements in ℝⁿ", "the same subspace"], "Every vector in the null space is perpendicular to every row, and together they fill ℝⁿ."),
    ("Col(A) and Nul(Aᵀ) are orthogonal complements in:", ["ℝⁿ", "*ℝᵐ", "ℝᵐˣⁿ", "ℝ¹"], "Both live in ℝᵐ and their dimensions sum to m."),
    ("A 5×5 matrix with rank 5 has null space of dimension:", ["5", "4", "1", "*0"], "Rank 5 + nullity = 5, so nullity = 0: only the trivial null space."),
    ("If Ax = b has infinitely many solutions, then Nul(A):", ["is empty", "has dimension 0", "*has dimension ≥ 1 (there are free variables)", "equals Col(A)"], "Infinitely many solutions means there are free variables, giving a nontrivial null space."),
    ("The null space gives the _____ of the transformation represented by A:", ["image", "range", "*kernel (what maps to zero)", "codomain"], "Kernel and null space are synonyms — vectors that A sends to the zero vector."),
],

# ── U5 L5.7: Applications in Computer Graphics ──
"u5_l5.7": [
    ("In 3D graphics, objects are positioned using:", ["addition only", "scalar multiplication only", "*transformation matrices (rotation, scaling, translation)", "sorting algorithms"], "Matrices compactly represent all geometric transformations applied to 3D models."),
    ("Homogeneous coordinates use an extra coordinate to enable:", ["faster rendering", "better color", "*translation as a matrix multiplication (not just linear operations)", "smaller matrices"], "The 4th coordinate lets translation be expressed as multiplication, unifying all affine transforms."),
    ("A 4×4 transformation matrix in homogeneous coordinates combines:", ["only rotation", "only translation", "only scaling", "*rotation, scaling, and translation in a single matrix"], "The unified matrix handles all three operations simultaneously."),
    ("The order of matrix multiplications in graphics matters because:", ["matrices commute", "order doesn't matter", "*matrix multiplication is non-commutative (AB ≠ BA generally)", "only the last matrix matters"], "Applying rotation then translation gives a different result than translation then rotation."),
    ("A camera (view) matrix transforms world coordinates into:", ["model space", "texture space", "*camera (eye) space", "screen pixels directly"], "The view matrix shifts and rotates the scene to align with the camera's perspective."),
    ("Perspective projection makes distant objects appear:", ["larger", "the same size", "brighter", "*smaller (simulating depth perception)"], "Perspective division by the z-coordinate creates the depth illusion."),
    ("An orthographic projection preserves:", ["perspective depth cues", "only colors", "only rotations", "*parallel lines and relative sizes (no foreshortening)"], "Ortho projection maps objects without perspective distortion — useful for engineering views."),
    ("To rotate, then scale, then translate an object, multiply:", ["T · S · R · point", "R · S · T · point", "*T · S · R · point (rightmost applied first)", "point · R · S · T"], "In column-vector convention, the rightmost matrix acts first: rotate, then scale, then translate."),
    ("A normal vector transforms differently from vertex positions because:", ["normals are colors", "normals are scalars", "*non-uniform scaling distorts normals; they need the inverse-transpose matrix", "normals don't transform"], "Normals must be multiplied by (M⁻¹)ᵀ to stay perpendicular after non-uniform scaling."),
    ("The GPU (graphics processing unit) is optimized for:", ["text processing", "database queries", "*parallel matrix operations on thousands of vertices simultaneously", "sorting strings"], "GPUs are massively parallel processors specifically designed for matrix math."),
    ("Vertex shaders in a graphics pipeline perform:", ["only color changes", "only texture lookup", "*per-vertex transformations using matrices (model-view-projection)", "only lighting"], "Each vertex is multiplied by the combined transformation matrix in the vertex shader."),
    ("Model-View-Projection (MVP) matrix combines:", ["three addition operations", "three scalar multiplications", "*model, view, and projection matrices into one transformation", "only two matrices"], "MVP = Projection × View × Model, applied as a single matrix to each vertex."),
    ("Interpolation between two rotations (slerp) is used for:", ["pixel shading", "memory management", "*smooth animation transitions between orientations", "data compression"], "Spherical linear interpolation (slerp) smoothly transitions between rotation states."),
    ("Scaling a 3D object by factor 2 in all directions uses:", ["a 2×2 matrix", "a 3×3 identity", "*a 4×4 matrix with 2,2,2,1 on the diagonal", "scalar addition to coordinates"], "In homogeneous coords, diag(2,2,2,1) scales x,y,z by 2 while keeping the w-coordinate."),
    ("The determinant of a pure rotation matrix is:", ["0", "−1", "2", "*1"], "Rotations preserve volume and orientation, giving det = 1."),
    ("Reflection across a plane in 3D has determinant:", ["0", "1", "2", "*−1"], "Reflections reverse orientation, giving det = −1."),
    ("Frustum culling uses the projection matrix to:", ["add vertices", "smooth edges", "*discard objects outside the camera's view volume (saving rendering time)", "increase resolution"], "Objects outside the frustum are culled early, avoiding unnecessary rendering work."),
    ("Skeletal animation transforms vertices based on:", ["fixed positions", "random matrices", "*weighted combinations of multiple bone transformation matrices", "only translation"], "Each vertex is influenced by nearby bones with blend weights for smooth deformation."),
    ("The z-buffer (depth buffer) uses z-values to:", ["store colors", "compute normals", "*determine which surfaces are visible (resolving occlusion)", "animate objects"], "Closer fragments overwrite farther ones in the depth buffer, handling visibility."),
    ("Modern real-time rendering performs billions of matrix operations per second using:", ["CPU only", "RAM only", "*the GPU's parallel matrix hardware", "the hard drive"], "GPUs achieve massive throughput by processing many vertices and pixels in parallel."),
],

# ── U5 L5.8: Applications in Data Science ──
"u5_l5.8": [
    ("In PCA (Principal Component Analysis), data is projected onto:", ["random directions", "the coordinate axes", "*directions of maximum variance (principal components)", "the smallest eigenvectors"], "PCA finds the orthogonal directions that capture the most variation in the data."),
    ("Principal components are eigenvectors of:", ["the data matrix itself", "the mean vector", "*the covariance matrix of the data", "the identity matrix"], "The covariance matrix eigenvectors point in the directions of greatest variance."),
    ("Dimensionality reduction helps with:", ["adding more features", "making data larger", "*reducing noise, computation, and overfitting in high-dimensional data", "increasing the number of variables"], "Fewer dimensions mean faster computation and often better generalization."),
    ("In linear regression, the normal equation is:", ["y = mx + b", "AᵀA = 0", "*(AᵀA)β = Aᵀy", "β = y/A"], "The normal equation minimizes the sum of squared residuals in closed form."),
    ("The least-squares solution minimizes:", ["the maximum error", "the average error", "*the sum of squared residuals (||Ax − b||²)", "the number of data points"], "Least squares finds β that minimizes the total squared distance from the model to the data."),
    ("If AᵀA is singular, the least-squares solution:", ["is unique", "doesn't exist", "*is not unique (there are infinitely many solutions)", "equals zero"], "Singular AᵀA means there are free variables, leading to infinitely many minimizers."),
    ("SVD (Singular Value Decomposition) factors A into:", ["LU", "QR", "*UΣVᵀ", "A = A²"], "Any matrix can be decomposed as A = UΣVᵀ with orthogonal U,V and diagonal Σ."),
    ("In recommendation systems, matrix factorization approximates a user-item matrix as:", ["A⁻¹", "A + B", "*the product of two lower-rank matrices", "a diagonal matrix"], "Low-rank factorization reveals latent features connecting users and items."),
    ("The rank of the approximation in truncated SVD controls:", ["the color of plots", "the file format", "*the number of latent features (complexity vs. accuracy tradeoff)", "the data type"], "Higher rank retains more information but is more complex; lower rank compresses more."),
    ("A data matrix with 1000 samples and 50 features has dimensions:", ["50×50", "1000×1000", "50×1000", "*1000×50"], "Rows = samples, columns = features, giving a 1000×50 matrix."),
    ("Feature scaling (standardization) before PCA ensures:", ["larger features are prioritized", "nothing changes", "*all features contribute equally regardless of their original units", "fewer data points"], "Without scaling, features with larger magnitude dominate the principal components."),
    ("The explained variance ratio of a principal component tells:", ["the computation time", "*what fraction of total variance that component captures", "the number of features", "the data size"], "High explained variance means the component captures substantial information."),
    ("If the first 3 principal components capture 95% of the variance, you can:", ["ignore PCA", "use all 50 features", "*project the data to 3 dimensions with minimal information loss", "double the features"], "95% variance captured by 3 components means 3D is an excellent approximation."),
    ("The pseudo-inverse A⁺ (Moore-Penrose) is used when:", ["A is square and invertible", "A is the zero matrix", "*A is not square or not invertible (standard inverse doesn't work)", "A is orthogonal"], "The pseudo-inverse generalizes the inverse to handle rectangular and singular matrices."),
    ("In image compression, SVD keeps only the top k singular values to:", ["encrypt the image", "*approximate the image with much less data (lossy compression)", "increase resolution", "change the format"], "Truncated SVD stores only k modes, significantly reducing storage."),
    ("The condition number of AᵀA affects:", ["the color scheme", "only the size of the result", "*numerical stability of the least-squares solution", "nothing practical"], "A large condition number means small data perturbations cause large solution changes."),
    ("Word embeddings (Word2Vec, GloVe) represent words as:", ["single numbers", "strings", "*vectors in high-dimensional space, learned via matrix factorization", "binary codes"], "These tools map words to vectors where geometric relationships encode semantic meaning."),
    ("In clustering (K-means), the data matrix is used to:", ["perform regression", "solve equations", "*compute distances between data points and cluster centers", "find eigenvalues"], "K-means repeatedly computes distances (using vector operations) and updates centers."),
    ("Regularization (like Ridge regression) modifies the normal equation to:", ["remove the data", "square the answer", "*add λI to AᵀA, ensuring invertibility: β = (AᵀA + λI)⁻¹Aᵀy", "double the matrix"], "The regularization term λI prevents singularity and reduces overfitting."),
    ("The kernel trick in machine learning implicitly maps data to:", ["fewer dimensions", "the same space", "a smaller dataset", "*a higher-dimensional feature space (without explicitly computing the mapping)"], "Kernel functions compute inner products in the higher-dimensional space efficiently."),
],

# ── U6 L6.1: Definition of Linear Transformations ──
"u6_l6.1": [
    ("A function T: V → W is a linear transformation if it preserves:", ["only addition", "only scalar multiplication", "*both addition (T(u+v)=T(u)+T(v)) and scalar multiplication (T(cv)=cT(v))", "neither operation"], "Both properties must hold for T to be linear."),
    ("T(0) for any linear transformation equals:", ["1", "undefined", "v", "*0 (the zero vector of the codomain)"], "T(0) = T(0·v) = 0·T(v) = 0. Linearity forces the zero vector to map to zero."),
    ("T(x,y) = (2x+y, x−3y) is:", ["not a function", "nonlinear", "*a linear transformation from ℝ² to ℝ²", "a quadratic map"], "Each output component is a linear combination of inputs, with no constants or higher powers."),
    ("T(x,y) = (x+1, y) is NOT linear because:", ["it maps to ℝ²", "it depends on x", "*T(0,0) = (1,0) ≠ (0,0)", "it's too simple"], "A linear map must send 0 to 0. The constant +1 violates this."),
    ("T(x,y) = (xy, x+y) is NOT linear because:", ["it maps two variables", "it involves addition", "*the term xy is nonlinear (product of inputs)", "it's not a function"], "xy is a nonlinear term — it cannot be expressed as a linear combination of inputs."),
    ("Every linear transformation from ℝⁿ to ℝᵐ can be represented by:", ["a scalar", "a vector", "*an m×n matrix", "a polynomial"], "T(x) = Ax for some m×n matrix A, determined by where T sends the standard basis vectors."),
    ("The matrix of a linear transformation T is found by computing:", ["T(0)", "det(T)", "*[T(e₁) | T(e₂) | ... | T(eₙ)] (images of standard basis as columns)", "T⁻¹"], "Place the images of the standard basis vectors as columns of the matrix."),
    ("The identity transformation I(v) = v is represented by:", ["the zero matrix", "a random matrix", "*the identity matrix Iₙ", "a singular matrix"], "I sends each eᵢ to itself, making each column [eᵢ], which is the identity matrix."),
    ("The zero transformation T(v) = 0 is represented by:", ["the identity matrix", "*the zero matrix", "a diagonal matrix", "an undefined matrix"], "Every standard basis vector maps to 0, giving all-zero columns."),
    ("T: ℝ² → ℝ³ defined by T(x,y) = (x, y, x+y) has matrix:", ["2×3", "3×3", "2×2", "*3×2"], "T maps 2D to 3D; the matrix has 3 rows (output dim) and 2 columns (input dim)."),
    ("T(cu+dv) = cT(u) + dT(v) for all scalars c,d and vectors u,v is called:", ["bilinearity", "nonlinearity", "*superposition (combines both linearity conditions)", "orthogonality"], "This single condition is equivalent to the two separate linearity conditions combined."),
    ("Linear transformations map lines through the origin to:", ["circles", "curves", "*lines through the origin (or the zero vector)", "planes"], "A line through the origin is {tv : t ∈ ℝ}. T(tv) = tT(v) traces a line (or collapses to 0)."),
    ("The projection T(x,y) = (x,0) is linear because:", ["T(0) ≠ 0", "*T(u+v) = T(u)+T(v) and T(cv) = cT(v) both hold", "it involves subtraction", "it maps to ℝ¹"], "Projection onto a coordinate axis satisfies both linearity conditions."),
    ("Linear transformations are completely determined by their action on:", ["all vectors", "a single vector", "the zero vector", "*a basis for the domain"], "Once you know T(bᵢ) for each basis vector, linearity determines T(v) for all v."),
    ("Differentiation d/dx: Pₙ → Pₙ₋₁ is:", ["nonlinear", "undefined", "only for real numbers", "*a linear transformation"], "d/dx(f+g) = f'+g' and d/dx(cf) = cf', so differentiation is linear."),
    ("Integration from a to b: C[a,b] → ℝ is:", ["nonlinear", "undefined", "*a linear transformation", "only for polynomials"], "∫(f+g) = ∫f + ∫g and ∫(cf) = c∫f, so integration is linear."),
    ("T: ℝ² → ℝ² given by T(x,y) = (|x|, y) is:", ["linear", "*nonlinear (absolute value violates T(cv)=cT(v) for negative c)", "undefined", "only linear for positive inputs"], "T(−1·(1,0)) = (1,0) but −1·T(1,0) = (−1,0). These differ, so T is not linear."),
    ("The composition of two linear transformations is:", ["nonlinear", "undefined", "linear only sometimes", "*always linear"], "If S and T are linear, then (S∘T)(u+v) = S(T(u+v)) = S(T(u)+T(v)) = S(T(u))+S(T(v))."),
    ("A linear transformation that maps ℝⁿ to ℝ¹ is called:", ["a matrix", "*a linear functional", "a projection", "an eigenfunction"], "A linear map to the scalar field (ℝ) is called a linear functional."),
    ("Linearity is the key property that makes matrix algebra work because:", ["it simplifies addition", "*it means T(x) = Ax, connecting abstract transformations to concrete matrix computations", "it eliminates multiplication", "it's only theoretical"], "Linearity allows every transformation to be encoded as matrix multiplication."),
],

# ── U6 L6.2: Kernel & Image ──
"u6_l6.2": [
    ("The kernel (null space) of T is:", ["{T(v) : v ∈ V}", "the range of T", "*{v ∈ V : T(v) = 0}", "V itself"], "The kernel consists of all vectors that T sends to the zero vector."),
    ("The image (range) of T is:", ["*{T(v) : v ∈ V}", "{v : T(v) = 0}", "V itself", "the domain of T"], "The image is all possible output vectors — everything T can produce."),
    ("If ker(T) = {0}, then T is:", ["surjective", "zero", "*injective (one-to-one)", "not a function"], "Trivial kernel means distinct inputs produce distinct outputs."),
    ("If im(T) = W (the entire codomain), then T is:", ["injective", "zero", "*surjective (onto)", "not linear"], "Surjective means every vector in the codomain is hit by some input."),
    ("The dimension theorem: dim(ker T) + dim(im T) =:", ["dim(W)", "dim(V) + dim(W)", "*dim(V) (dimension of the domain)", "0"], "This is the Rank-Nullity Theorem applied to linear transformations."),
    ("If T: ℝ⁵ → ℝ³ has dim(im T) = 3, then dim(ker T) =:", ["0", "3", "5", "*2"], "5 = dim(ker T) + 3, so dim(ker T) = 2."),
    ("The kernel of T is always:", ["all of V", "empty", "*a subspace of the domain V", "a subspace of W"], "ker(T) is closed under addition and scalar mult (since T(u+v) = T(u)+T(v) = 0+0 = 0)."),
    ("The image of T is always:", ["all of W", "empty", "a subspace of V", "*a subspace of the codomain W"], "im(T) is a subspace of W, potentially proper if T is not surjective."),
    ("Projection onto the x-axis: T(x,y)=(x,0). ker(T) is:", ["the x-axis", "*the y-axis ({(0,y)})", "the origin only", "all of ℝ²"], "T(0,y) = (0,0) for all y, so the entire y-axis maps to zero."),
    ("For the same projection, im(T) is:", ["ℝ²", "the y-axis", "*the x-axis ({(x,0)})", "the origin"], "Outputs are all of the form (x,0) — exactly the x-axis."),
    ("T is an isomorphism if and only if:", ["ker(T) = V", "im(T) = {0}", "*ker(T) = {0} and im(T) = W (bijective)", "T is the zero map"], "An isomorphism is a bijective linear transformation — both injective and surjective."),
    ("If T: ℝⁿ → ℝⁿ with ker(T) = {0}, then T is also:", ["not surjective", "only injective", "*surjective (hence bijective in finite dimensions)", "undefined"], "For maps between same-dimensional spaces, injective implies surjective."),
    ("A rank-1 transformation maps all of ℝⁿ to:", ["all of ℝⁿ", "a plane", "*a line through the origin", "a point"], "Rank 1 means dim(im T) = 1, which is a line."),
    ("If T(v₁) = T(v₂), then:", ["v₁ = v₂", "T is surjective", "*v₁ − v₂ ∈ ker(T)", "T is zero"], "T(v₁ − v₂) = T(v₁) − T(v₂) = 0, so the difference is in the kernel."),
    ("For a matrix A, ker(T_A) = Nul(A) and im(T_A) = Col(A):", ["only for square A", "never", "*always (this connects abstract and matrix notions)", "only for invertible A"], "The kernel and image of the transformation correspond exactly to null space and column space."),
    ("If dim(ker T) = 0 for T: ℝ³ → ℝ⁵, then dim(im T) =:", ["0", "5", "2", "*3"], "dim(ker T) + dim(im T) = 3, so dim(im T) = 3. T is injective but not surjective."),
    ("The rank of T is defined as:", ["dim(ker T)", "dim(V)", "*dim(im T)", "dim(V) − dim(W)"], "The rank of a transformation is the dimension of its image (range)."),
    ("Nullity of T is:", ["*dim(ker T)", "dim(im T)", "dim(V)", "rank + dimension"], "Nullity = dimension of the kernel = number of 'dimensions lost' by the transformation."),
    ("If T: V → W is surjective and dim(V) = dim(W), then ker(T):", ["is all of V", "has dimension 1", "is nonempty", "*equals {0} (T is also injective)"], "In equal dimensions: surjective + linear → injective, so the kernel is trivial."),
    ("Finding the kernel requires solving:", ["T(v) = v", "det(A) = 0", "*Ax = 0 (the homogeneous system)", "AᵀA = I"], "The kernel consists of all solutions to the homogeneous system Ax = 0."),
],

# ── U6 L6.3: Matrix Representation of Transformations ──
"u6_l6.3": [
    ("The matrix of T relative to bases B and C is denoted:", ["T(B)", "det(T)", "*[T]_B^C", "T×B×C"], "[T]_B^C means the matrix that represents T using basis B for the domain and C for the codomain."),
    ("Changing the basis of the domain corresponds to:", ["adding a matrix", "transposing", "*right-multiplying by a change-of-basis matrix", "computing the determinant"], "A new basis in the domain changes how input coordinates are expressed, affecting columns."),
    ("Changing the basis of the codomain corresponds to:", ["adding a matrix", "transposing", "*left-multiplying by a change-of-basis matrix", "computing the trace"], "A new codomain basis changes how output coordinates are expressed, affecting the left side."),
    ("If A represents T in standard bases, then in bases B,C: [T]_B^C =", ["A + P", "PA", "AQ", "*C⁻¹AQ, where Q is the domain change and C is the codomain change matrix"], "Transform domain coordinates by Q, apply A, then transform output coordinates by C⁻¹."),
    ("Similar matrices A and B = P⁻¹AP represent:", ["different transformations", "unrelated operations", "*the same transformation T in two different bases for both domain and codomain", "transposes of each other"], "Similarity changes the basis while preserving the abstract transformation."),
    ("The matrix representation depends on:", ["only the transformation", "only the domain basis", "*both the transformation and the choice of bases", "the dimension only"], "Different bases yield different matrices for the same transformation."),
    ("A diagonal matrix representation means the transformation:", ["is zero", "has no inverse", "*scales each basis vector independently (no mixing)", "is the identity"], "Diagonal form means T(bᵢ) = dᵢbᵢ — each basis vector just gets scaled."),
    ("To find [T]_B where B = {v₁, v₂}, compute:", ["v₁ + v₂", "det([v₁, v₂])", "*T(v₁) and T(v₂) expressed as coordinates in basis B", "v₁ × v₂"], "Apply T to each basis vector, then write the results in B-coordinates."),
    ("The standard matrix of T: ℝ² → ℝ² with T(e₁) = (3,1) and T(e₂) = (−2,4) is:", ["[[3,−2],[1,4]]ᵀ", "[[3,1],[−2,4]]", "*[[3,−2],[1,4]]", "[[1,4],[3,−2]]"], "Columns are T(e₁) and T(e₂): [[3,−2],[1,4]]."),
    ("The purpose of finding a 'nice' basis is to make:", ["the matrix larger", "the computation impossible", "*the matrix representation as simple as possible (e.g., diagonal)", "the basis orthogonal necessarily"], "A well-chosen basis simplifies the matrix, making computations and analysis easier."),
    ("For T: V → V (same space), the matrix in basis B is:", ["always diagonal", "*P⁻¹AP where A is the standard matrix and P is the change-of-basis", "always symmetric", "always the identity"], "Similarity transformation P⁻¹AP changes from standard to basis B."),
    ("The trace of a matrix representation is:", ["basis-dependent", "always 0", "*the same for all similar matrices (basis-independent)", "equal to the determinant"], "Trace is invariant under similarity: tr(P⁻¹AP) = tr(A)."),
    ("The determinant of a matrix representation is:", ["basis-dependent usually", "always 1", "*the same for all similar matrices", "equal to the trace"], "det(P⁻¹AP) = det(A), so the determinant is basis-independent."),
    ("An eigenbasis (basis of eigenvectors) diagonalizes the matrix because:", ["eigenvectors are zero", "eigenvectors are orthogonal always", "*each eigenvector scales by its eigenvalue, giving a diagonal matrix", "eigenvalues are zero"], "In the eigenbasis, T(vᵢ) = λᵢvᵢ, so the matrix has eigenvalues on the diagonal."),
    ("If no eigenbasis exists, the best achievable form is:", ["diagonal", "the identity", "*Jordan normal form (blocks with eigenvalues and possibly 1s above the diagonal)", "the zero matrix"], "JNF is the closest to diagonal form when full diagonalization isn't possible."),
    ("The matrix of composition T₂∘T₁ in the standard basis is:", ["A₁ + A₂", "A₁ − A₂", "*A₂A₁ (matrix product, applied right to left)", "A₁A₂"], "Apply T₁ first (rightmost), then T₂: the matrix is A₂A₁."),
    ("Two square matrices are similar if and only if they represent:", ["different transformations in the same basis", "the same matrix", "*the same transformation in different bases", "transposes of each other"], "Similarity captures the idea of 'same transformation, different coordinate systems.'"),
    ("The number of nonzero entries in the matrix can change with basis, but what stays the same?", ["individual entries", "the number of zeros", "*rank, determinant, trace, and eigenvalues", "the exact matrix"], "These invariants are properties of the transformation, not the coordinate system."),
    ("A real symmetric matrix can always be diagonalized with:", ["any invertible P", "lower triangular P", "*an orthogonal matrix P (orthogonal eigenvectors)", "a singular P"], "The Spectral Theorem guarantees real symmetric matrices have orthogonal eigenvectors."),
    ("The coordinate vector [v]_B represents v in terms of:", ["the standard basis", "the zero vector", "*the basis B (coefficients of v as a combination of B's vectors)", "the eigenvectors"], "[v]_B gives the scalars such that v = c₁b₁ + c₂b₂ + ... + cₙbₙ."),
],

# ── U6 L6.4: Composition of Transformations ──
"u6_l6.4": [
    ("The composition (S∘T)(v) means:", ["S(v) + T(v)", "T(S(v))", "S·T", "*first apply T, then apply S: S(T(v))"], "Composition applies the inner function first: T, then S."),
    ("If T is represented by A and S by B, then S∘T is represented by:", ["A + B", "A − B", "*BA (matrix product)", "AB"], "S∘T corresponds to BA because T acts first (rightmost matrix)."),
    ("Matrix multiplication is associative: (AB)C = A(BC). This means:", ["order matters for individual matrices", "they can be added", "*composition of three transformations can be grouped either way", "they commute"], "Associativity lets us compose transformations without worrying about grouping."),
    ("Composing a rotation by 30° followed by a rotation by 60° gives:", ["a rotation by 30°", "a rotation by 1800°", "a reflection", "*a rotation by 90°"], "Rotation angles add: 30° + 60° = 90°."),
    ("If T: ℝ² → ℝ³ and S: ℝ³ → ℝ⁴, then S∘T maps:", ["ℝ⁴ to ℝ²", "ℝ³ to ℝ³", "ℝ² to ℝ³", "*ℝ² to ℝ⁴"], "The composition maps from T's domain (ℝ²) to S's codomain (ℝ⁴)."),
    ("The matrix of S∘T has dimensions:", ["2×4", "3×3", "3×2", "*4×2"], "S is 4×3 and T is 3×2, so BA is 4×2."),
    ("Composing a transformation with its inverse gives:", ["the zero transformation", "the transformation squared", "an undefined result", "*the identity transformation"], "T∘T⁻¹ = T⁻¹∘T = I, by definition of the inverse."),
    ("In general, is S∘T the same as T∘S?", ["yes, always", "only for rotations", "*no, composition is generally non-commutative", "only for 2×2 matrices"], "Just as AB ≠ BA in general for matrices, composition order matters."),
    ("A rotation followed by a scaling:", ["always equals scaling then rotation", "is undefined", "*generally differs from scaling then rotation, but equals it for uniform scaling", "cancels out"], "Uniform scaling commutes with rotation, but non-uniform scaling does not."),
    ("The rank of S∘T satisfies:", ["rank(S∘T) = rank(S) + rank(T)", "*rank(S∘T) ≤ min(rank(S), rank(T))", "rank(S∘T) = rank(T) always", "rank(S∘T) > rank(S)"], "The composition can only lose rank (or keep it), never exceed the minimum of the two."),
    ("If both S and T are bijective (isomorphisms), then S∘T is:", ["singular", "not a function", "injective only", "*also bijective"], "Composing two bijections gives a bijection with inverse T⁻¹∘S⁻¹."),
    ("(S∘T)⁻¹ equals:", ["S⁻¹∘T⁻¹", "T∘S", "*T⁻¹∘S⁻¹ (reverse order)", "S∘T"], "To undo S∘T, first undo S, then undo T: the order reverses."),
    ("Applying a projection P twice (P∘P) gives:", ["zero", "2P", "P⁻¹", "*P (projections are idempotent: P² = P)"], "Projecting again doesn't change anything — the result is already in the subspace."),
    ("In a graphics pipeline with Model (M), View (V), Projection (P), the combined matrix is:", ["M+V+P", "MV+P", "M·V·P applied left to right", "*P·V·M (applied right to left: M first)"], "The rightmost matrix acts first on the vertex coordinates."),
    ("Composing a reflection with itself gives:", ["another reflection", "the zero map", "a rotation", "*the identity transformation"], "Reflecting twice returns to the original position."),
    ("For T: V → V, the map T^n means:", ["T multiplied by n", "T + T + ... n times", "nT", "*T composed with itself n times"], "T^n = T∘T∘...∘T (n times), corresponding to matrix Aⁿ."),
    ("If T maps ℝ² → ℝ² and has eigenvalues λ₁, λ₂, then T^n has eigenvalues:", ["nλ₁, nλ₂", "λ₁+n, λ₂+n", "λ₁/n, λ₂/n", "*λ₁ⁿ, λ₂ⁿ"], "Eigenvalues of Aⁿ are the eigenvalues of A raised to the nth power."),
    ("The composition of two linear transformations is always:", ["nonlinear", "undefined", "linear only if both are bijective", "*linear"], "Composing two linear maps preserves both linearity conditions."),
    ("Functional iteration (applying T repeatedly) is important in:", ["only pure math", "only physics", "*dynamical systems, Markov chains, and numerical methods", "nothing practical"], "Many algorithms and models involve iterating a linear map to convergence."),
    ("If T shrinks all vectors (||T(v)|| < ||v||), then T^n approaches:", ["the zero matrix", "the identity", "infinity", "*the zero transformation (all vectors shrink to 0)"], "Repeated contraction drives everything to zero."),
],

# ── U6 L6.5: Rotations & Reflections ──
"u6_l6.5": [
    ("The 2D rotation matrix by angle θ is:", ["[[cos θ, cos θ],[sin θ, sin θ]]", "*[[cos θ, −sin θ],[sin θ, cos θ]]", "[[sin θ, cos θ],[cos θ, sin θ]]", "[[1, θ],[0, 1]]"], "This matrix rotates every vector counterclockwise by angle θ."),
    ("A rotation matrix is always:", ["singular", "symmetric", "skew-symmetric", "*orthogonal (columns are orthonormal)"], "Rotation matrices satisfy RᵀR = I, making them orthogonal."),
    ("det(rotation matrix) equals:", ["0", "−1", "θ", "*1"], "Rotations preserve both volume and orientation, giving determinant 1."),
    ("Rotating by 90° counterclockwise maps (1,0) to:", ["(1,0)", "(0,−1)", "(−1,0)", "*(0,1)"], "R₉₀ = [[0,−1],[1,0]], so (1,0) → (0,1)."),
    ("The reflection matrix across the x-axis is:", ["[[0,1],[1,0]]", "*[[1,0],[0,−1]]", "[[−1,0],[0,1]]", "[[0,−1],[−1,0]]"], "x stays the same, y negates: (x,y) → (x,−y)."),
    ("det(reflection matrix) equals:", ["0", "1", "2", "*−1"], "Reflections reverse orientation, giving determinant −1."),
    ("Reflection across the line y = x is:", ["[[1,0],[0,−1]]", "*[[0,1],[1,0]]", "[[−1,0],[0,−1]]", "[[1,1],[1,1]]"], "This swaps the x and y coordinates: (x,y) → (y,x)."),
    ("Composing two reflections (across different lines through the origin) gives:", ["another reflection", "the identity", "*a rotation (by twice the angle between the lines)", "a scaling"], "Two reflections compose to a rotation whose angle is twice the angle between the reflection lines."),
    ("Rotation by 180° is the same as:", ["the identity", "a reflection", "a scaling by 2", "*multiplication by −I (negating both coordinates)"], "R₁₈₀ = [[−1,0],[0,−1]] = −I, which negates every vector."),
    ("Rotation matrices satisfy Rᵀ = R⁻¹, meaning:", ["R is singular", "R is symmetric", "*the transpose equals the inverse", "R has no inverse"], "This is the defining property of orthogonal matrices, which rotations are."),
    ("In 3D, a rotation about the z-axis by θ affects:", ["only x and z", "only y and z", "*only x and y (z stays fixed)", "all three equally"], "The rotation matrix is [[cosθ,−sinθ,0],[sinθ,cosθ,0],[0,0,1]], leaving z unchanged."),
    ("3D rotations about different axes generally:", ["commute", "cancel out", "are identical", "*do not commute (order matters)"], "Rotating about x then y gives a different result than y then x."),
    ("An improper rotation (rotation + reflection) has determinant:", ["0", "1", "2", "*−1"], "Improper rotations include a reflection component, flipping the sign of the determinant."),
    ("Householder reflections use the matrix H = I − 2uuᵀ to:", ["rotate vectors", "scale vectors", "*reflect vectors across the hyperplane perpendicular to u", "project vectors"], "Householder matrices are used in QR decomposition to zero out entries."),
    ("Rotation preserves:", ["only angles", "only lengths", "only areas", "*lengths, angles, and areas (all geometric properties)"], "Rotations are rigid motions: they preserve the full geometric structure."),
    ("The composition of two 2D rotations by angles α and β gives rotation by:", ["α·β", "α−β", "max(α,β)", "*α+β"], "Rotations compose by adding angles: R_α · R_β = R_(α+β)."),
    ("Euler's rotation theorem states that any 3D rotation has:", ["no fixed points", "a fixed plane", "*a fixed axis (eigenvector with eigenvalue 1)", "three fixed axes"], "Every rotation in 3D fixes an axis — the line around which everything rotates."),
    ("Quaternions represent rotations as:", ["2×2 matrices", "3D vectors", "polynomials", "*4-component numbers (avoiding gimbal lock issues of Euler angles)"], "Quaternions smoothly parameterize rotations without the singularities of Euler angles."),
    ("Gimbal lock occurs when:", ["all axes are free", "no rotation is applied", "*two rotation axes align, losing a degree of freedom", "the matrix is singular"], "Gimbal lock is a practical problem with Euler angle representations."),
    ("A rotation matrix in ℝⁿ belongs to the group:", ["GL(n)", "SL(n)", "O(n)", "*SO(n) (special orthogonal group: det = 1)"], "SO(n) = orthogonal matrices with det = +1, which are exactly the rotations."),
],

# ── U6 L6.6: Scaling & Shearing ──
"u6_l6.6": [
    ("Uniform scaling by factor k in 2D uses the matrix:", ["[[k,k],[k,k]]", "[[k,0],[0,1]]", "[[1,k],[k,1]]", "*[[k,0],[0,k]]"], "Both axes scale by k, so the diagonal matrix is kI."),
    ("Non-uniform scaling stretches different axes by:", ["the same factor", "zero", "*different factors (e.g., 2 in x and 3 in y)", "undefined amounts"], "diag(s_x, s_y) applies different scaling factors to each axis."),
    ("det(diag(2,3)) = 6 means the transformation:", ["compresses area by 6", "*scales area by a factor of 6", "rotates by 6°", "translates by 6 units"], "The determinant gives the area scaling factor."),
    ("Scaling by factor 0 in one direction:", ["is invertible", "*collapses that dimension (the matrix becomes singular)", "does nothing", "doubles the area"], "A zero diagonal entry means rank drops: information is lost and the transform is irreversible."),
    ("Negative scaling (factor −1) along one axis is equivalent to:", ["a rotation", "an identity", "*a reflection across the other axis", "a translation"], "Negating one coordinate reflects across its perpendicular axis."),
    ("A shear in the x-direction by factor k maps (x,y) to:", ["(x, y+kx)", "(kx, y)", "(x+k, y)", "*(x+ky, y)"], "x shifts by k times the y-coordinate, while y stays fixed: [[1,k],[0,1]]."),
    ("The shear matrix [[1,k],[0,1]] has determinant:", ["k", "1+k", "0", "*1"], "det = 1·1 − k·0 = 1. Shears preserve area."),
    ("Shearing preserves:", ["angles", "perpendicularity", "lengths", "*area (but distorts shapes)"], "det = 1 means area is preserved, but the shape deforms (e.g., square → parallelogram)."),
    ("The inverse of shear [[1,k],[0,1]] is:", ["[[1,k],[0,1]]", "[[1,0],[k,1]]", "[[k,1],[1,0]]", "*[[1,−k],[0,1]]"], "Shear by −k undoes shear by k: [[1,k],[0,1]]·[[1,−k],[0,1]] = I."),
    ("Composing a shear with itself [[1,k],[0,1]]² gives:", ["the identity", "[[1,k²],[0,1]]", "[[1,2k],[0,4]]", "*[[1,2k],[0,1]]"], "Shearing by k twice is equivalent to shearing by 2k."),
    ("In typography, italic text is created using:", ["rotation", "uniform scaling", "*horizontal shearing", "translation"], "Italicizing is essentially a shear that tilts vertical strokes."),
    ("The eigenvalues of shear [[1,k],[0,1]] (k≠0) are:", ["1 and k", "1 and −1", "k and −k", "*both equal to 1 (repeated eigenvalue)"], "det(A−λI) = (1−λ)² = 0, giving λ = 1 with multiplicity 2 but only one eigenvector."),
    ("A shear matrix is not diagonalizable when k ≠ 0 because:", ["it has no eigenvalues", "*it has only one linearly independent eigenvector for the repeated eigenvalue 1", "its determinant is zero", "it equals the identity"], "The eigenspace for λ=1 is 1-dimensional, so there aren't enough eigenvectors."),
    ("Scaling by factors (2,3) then (3,2) gives overall scaling by:", ["(5,5)", "(2,3)", "(6,5)", "*(6,6)"], "Factors multiply componentwise: (2·3, 3·2) = (6,6), which is uniform scaling by 6."),
    ("Non-uniform scaling distorts:", ["nothing", "only sizes", "*angles and shapes (circles become ellipses)", "only colors"], "Different stretching in different directions changes angles between lines."),
    ("In principal component basis, a covariance transformation becomes:", ["a shear", "a rotation", "singular", "*a diagonal scaling (by the eigenvalues/variances)"], "PCA diagonalizes the covariance matrix, revealing independent scaling along each component."),
    ("A squeeze mapping preserves area by scaling x by k and y by:", ["k", "k²", "0", "*1/k"], "det(diag(k, 1/k)) = k·(1/k) = 1, preserving area."),
    ("The decomposition of any 2×2 matrix into rotation, scaling, and rotation (SVD) shows:", ["matrices can only rotate", "scaling is impossible", "*every linear transformation is a rotation, then scaling, then another rotation", "only symmetric matrices have this form"], "SVD: A = UΣVᵀ — rotate (Vᵀ), scale (Σ), rotate again (U)."),
    ("In 3D animation, non-uniform scaling requires careful treatment of:", ["colors", "frame rates", "*normal vectors (which must use the inverse-transpose)", "vertex count"], "Normals transform by (M⁻¹)ᵀ to remain perpendicular after non-uniform scaling."),
    ("Affine transformations combine linear transforms (scaling, rotation, shear) with:", ["multiplication only", "inversion", "*translation (shift)", "determinant computation"], "Affine = linear + translation, handled in homogeneous coordinates."),
],

# ── U6 L6.7: Applications in Physics ──
"u6_l6.7": [
    ("In classical mechanics, the rotation of a rigid body is described by:", ["a scalar", "a vector alone", "*a rotation matrix (or angular velocity tensor)", "a polynomial"], "The orientation of a rigid body at any time is encoded by a rotation matrix."),
    ("The moment of inertia tensor I maps angular velocity ω to:", ["force", "energy", "position", "*angular momentum L = Iω"], "This linear relationship connects rotation rate to rotational momentum."),
    ("Diagonalizing the inertia tensor reveals:", ["the mass of the object", "the center of gravity", "*the principal axes and principal moments of inertia", "the force vectors"], "Eigenvectors are principal axes; eigenvalues are principal moments of inertia."),
    ("In quantum mechanics, observables are represented by:", ["complex numbers only", "diagonal matrices only", "*Hermitian (self-adjoint) operators/matrices", "anti-symmetric matrices"], "Hermitian operators guarantee real eigenvalues, which correspond to measurable values."),
    ("The state of a quantum system is described by:", ["a real number", "a classical trajectory", "*a vector (state vector) in a complex vector space (Hilbert space)", "a single matrix"], "Quantum states are vectors whose components encode probability amplitudes."),
    ("Measurement in QM projects the state vector onto:", ["a random direction", "the origin", "*an eigenspace of the observable being measured", "the null space"], "Measurement collapses the state to an eigenvector corresponding to the measured eigenvalue."),
    ("The Pauli matrices σₓ, σᵧ, σᵤ are used in:", ["thermodynamics", "optics only", "*spin-½ quantum mechanics", "classical mechanics only"], "These 2×2 matrices represent spin operators for spin-½ particles like electrons."),
    ("Lorentz transformations in special relativity are:", ["translations only", "non-invertible", "*linear transformations preserving the spacetime interval", "purely rotational"], "Lorentz transforms mix space and time coordinates while preserving the metric signature."),
    ("The stress tensor in continuum mechanics maps:", ["force to mass", "velocity to position", "*a surface normal vector to the stress (force per area) on that surface", "temperature to pressure"], "The stress tensor σ linearly maps unit normal n to traction vector t = σn."),
    ("The strain tensor relates:", ["force to acceleration", "*displacement gradients to deformation measures", "mass to volume", "time to distance"], "Strain is derived from the gradient of the displacement field — a linear relationship."),
    ("Maxwell's equations in vacuum can be written using:", ["only scalar functions", "only vectors", "*linear operators (curl, divergence) acting on field vectors", "nonlinear equations"], "The differential operators in Maxwell's equations are linear."),
    ("Normal modes of a coupled oscillator system are:", ["arbitrary vibration patterns", "only longitudinal", "*eigenvectors of the system matrix (independent vibration patterns)", "impossible to find"], "Each normal mode oscillates at a single frequency, determined by the eigenvalue."),
    ("In optics, a Jones matrix describes the transformation of:", ["light intensity only", "sound waves", "*the polarization state of light (a 2D complex vector)", "wavelength only"], "Jones matrices multiply polarization vectors to model optical elements."),
    ("The tensor product of two vector spaces creates:", ["a smaller space", "a scalar", "*a larger vector space (encoding multi-particle states in QM)", "a subspace"], "The tensor product V ⊗ W has dim(V)·dim(W) dimensions and describes composite systems."),
    ("Symmetry transformations in physics form:", ["random sets", "empty sets", "*groups (closed under composition with inverses)", "only pairs"], "Physical symmetries satisfy group axioms: closure, associativity, identity, inverses."),
    ("The eigenvectors of the Hamiltonian operator are:", ["force vectors", "velocity vectors", "*energy eigenstates (stationary states)", "position vectors"], "The Hamiltonian's eigenvectors are states with definite energy."),
    ("Conservation laws arise from symmetries via:", ["dimensional analysis", "coordinate changes", "*Noether's theorem (each continuous symmetry yields a conservation law)", "random processes"], "Noether's theorem connects symmetries (described by linear transformations) to conserved quantities."),
    ("Phase space in Hamiltonian mechanics is a vector space where points represent:", ["only positions", "only velocities", "*pairs (position, momentum) of a system", "forces"], "Each state is a point in 2n-dimensional phase space (n positions + n momenta)."),
    ("Unitary transformations in QM preserve:", ["only energy", "only position", "*inner products (probability amplitudes)", "nothing"], "Unitarity (U†U = I) preserves the norm of state vectors, ensuring probabilities sum to 1."),
    ("The transfer matrix method in optics tracks light through components by:", ["adding matrices", "averaging matrices", "*multiplying 2×2 matrices (one per optical element) in sequence", "inverting matrices"], "Each optical element contributes a matrix; the total effect is the product."),
],

# ── U6 L6.8: Applications in Engineering ──
"u6_l6.8": [
    ("In control theory, the state-space model ẋ = Ax + Bu uses:", ["only scalars", "only B", "*matrix A to describe system dynamics and B for input coupling", "only differential equations without matrices"], "The state matrix A governs how the system evolves; B couples external inputs."),
    ("The eigenvalues of the system matrix A determine:", ["the input signals", "the matrix dimensions", "*system stability (negative real parts → stable)", "the output format"], "Eigenvalues with negative real parts mean perturbations decay — the system is stable."),
    ("In signal processing, the DFT (Discrete Fourier Transform) is:", ["nonlinear", "a differential equation", "a random process", "*a linear transformation represented by a specific N×N matrix"], "The DFT matrix transforms time-domain samples to frequency-domain coefficients."),
    ("Filter design in digital signal processing relies on:", ["geometry", "combinatorics", "*convolution (linear operation) and transfer functions", "graph theory"], "Linear filters are described by their impulse response, applied via convolution."),
    ("In circuit analysis, Kirchhoff's laws can be written as:", ["nonlinear equations", "a single scalar equation", "*a linear system Ax = b (relating currents/voltages)", "differential equations only"], "KCL and KVL produce linear equations that matrix methods solve efficiently."),
    ("The impedance matrix Z relates voltage and current vectors:", ["V + I = Z", "V − I = Z", "VI = Z", "*V = ZI"], "This linear relationship extends Ohm's law to multi-port networks."),
    ("Finite element analysis (FEA) assembles:", ["one large equation", "random matrices", "*a global stiffness matrix from individual element matrices", "only diagonal matrices"], "Each finite element contributes a small stiffness matrix; these are assembled into a large system."),
    ("The global stiffness matrix in FEA is typically:", ["dense and small", "*sparse and large (most entries are zero)", "triangular", "singular"], "Elements interact only with neighbors, creating a sparse pattern with mostly zero entries."),
    ("In structural engineering, the stiffness matrix relates:", ["temperature to pressure", "mass to velocity", "*applied forces to nodal displacements (F = Ku)", "time to distance"], "Ku = F, where K is stiffness, u is displacement, and F is the applied force vector."),
    ("MIMO (Multiple-Input Multiple-Output) systems are described by:", ["a single transfer function", "a scalar equation", "*transfer function matrices", "only time-domain equations"], "MIMO systems couple multiple inputs and outputs through matrix-valued transfer functions."),
    ("The observability matrix tests whether:", ["the system is stable", "*internal states can be determined from output measurements", "inputs exist", "the matrix is square"], "If the observability matrix has full rank, all states can be reconstructed from outputs."),
    ("The controllability matrix tests whether:", ["outputs are observable", "the system has eigenvalues", "*any desired state can be reached by choosing appropriate inputs", "the system is linear"], "Full-rank controllability matrix means every state is reachable from any initial condition."),
    ("Kalman filtering uses linear algebra to:", ["sort data", "compress signals", "*optimally estimate states from noisy measurements", "encrypt communications"], "The Kalman filter recursively updates state estimates using matrix equations."),
    ("In power systems, the admittance matrix Y connects:", ["only resistance", "only capacitance", "*bus voltages to injected currents (I = YV)", "only inductance"], "The admittance matrix describes the electrical network's linear response."),
    ("Eigenvalues of the system matrix in vibration analysis give:", ["only mode shapes", "only damping ratios", "*natural frequencies (related to eigenvalues) and mode shapes (eigenvectors)", "only the matrix rank"], "Each eigenvalue-eigenvector pair corresponds to a natural frequency and vibration pattern."),
    ("The pseudoinverse is used in robotics when the Jacobian is:", ["square and invertible", "the identity", "*non-square or singular (more joints than coordinates or vice versa)", "zero"], "Redundant robots have more joints than task-space dimensions, requiring the pseudoinverse."),
    ("In telecommunications, MIMO antenna systems use matrix operations to:", ["reduce antenna count", "make antennas larger", "*separate multiple simultaneous data streams (spatial multiplexing)", "decrease bandwidth"], "Matrix processing at receiver and transmitter enables multiple parallel data channels."),
    ("The Singular Value Decomposition (SVD) reveals:", ["only eigenvalues", "only the determinant", "*the principal directions and magnitudes of a transformation (geometric structure)", "nothing about the matrix"], "SVD gives the axes and scale factors of how a matrix stretches space."),
    ("In process control, to stabilize an unstable system, engineers design:", ["larger matrices", "singular controllers", "*feedback gain matrices K that shift eigenvalues to stable locations", "zero matrices"], "Pole placement uses feedback K to make all eigenvalues of (A−BK) have negative real parts."),
    ("Model predictive control (MPC) repeatedly solves:", ["eigenvalue problems", "symbolic integrals", "*optimization problems involving matrix-based system models", "random searches"], "MPC optimizes control inputs over a prediction horizon using the linear state-space model."),
],
}

# ── Write ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, raw_qs in ALL_QS.items():
    if key not in data:
        print(f"Warning: {key} not found")
        continue
    data[key]["quiz_questions"] = make_qs(raw_qs)
    count += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Linear Algebra U5-U6: replaced questions in {count} lessons")
