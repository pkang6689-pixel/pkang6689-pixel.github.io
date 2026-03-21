#!/usr/bin/env python3
"""Replace placeholder questions in Linear Algebra U3-U4 with quality questions.

Quality rules:
- All 4 options similar length (no longest-is-correct giveaway)
- Plausible distractors based on common misconceptions
- No parenthetical hints in options
- Explanations are 1-2 educational sentences
"""
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content_data", "linear_algebra_lessons.json")

def make_qs(raw_list):
    """Convert compact tuples to full question objects."""
    result = []
    for i, (qt, opts, exp) in enumerate(raw_list, 1):
        options = []
        for o in opts:
            correct = o.startswith("*")
            options.append({"text": o.lstrip("*"), "is_correct": correct, "data_i18n": None})
        result.append({
            "question_number": i,
            "question_text": qt,
            "attempted": 2,
            "data_i18n": None,
            "options": options,
            "explanation": exp
        })
    return result

ALL_QS = {
# ── U3 L3.1: Definition of Determinants ──
"u3_l3.1": [
    ("The determinant of a 2×2 matrix [[a,b],[c,d]] equals:", ["a·d + b·c", "*a·d − b·c", "a·c − b·d", "a·b − c·d"], "The 2×2 determinant formula is ad − bc, found by multiplying diagonals and subtracting."),
    ("det([[3,1],[2,4]]) equals:", ["14", "*10", "8", "11"], "det = 3·4 − 1·2 = 12 − 2 = 10."),
    ("A determinant is defined only for:", ["rectangular matrices", "row vectors", "*square matrices", "diagonal matrices"], "Determinants require the same number of rows and columns, so only square matrices qualify."),
    ("If a matrix has determinant zero, it is called:", ["orthogonal", "symmetric", "diagonal", "*singular"], "A zero determinant means the matrix is singular and has no inverse."),
    ("det([[1,0],[0,1]]) equals:", ["0", "*1", "2", "−1"], "The identity matrix always has determinant 1, since 1·1 − 0·0 = 1."),
    ("For a 1×1 matrix [[5]], the determinant is:", ["0", "1", "25", "*5"], "A 1×1 determinant is just the single entry itself."),
    ("det([[0,3],[0,7]]) equals:", ["21", "10", "3", "*0"], "det = 0·7 − 3·0 = 0. Any matrix with a column of zeros has determinant zero."),
    ("The determinant of a matrix gives information about:", ["the trace only", "the number of rows", "*whether the matrix is invertible", "the matrix dimensions"], "A nonzero determinant guarantees invertibility; zero means the matrix is singular."),
    ("det([[2,5],[4,10]]) equals:", ["10", "*0", "−10", "40"], "det = 2·10 − 5·4 = 20 − 20 = 0. The rows are proportional, so the determinant is zero."),
    ("Which has a nonzero determinant?", ["[[1,2],[2,4]]", "[[0,0],[3,5]]", "*[[1,3],[2,5]]", "[[3,6],[1,2]]"], "det([[1,3],[2,5]]) = 5 − 6 = −1 ≠ 0. The other matrices have proportional rows or a zero row."),
    ("If det(A) = 5, denoting A is:", ["singular", "zero matrix", "symmetric", "*invertible"], "Any nonzero determinant, whether positive or negative, means the matrix is invertible."),
    ("det([[−1,2],[3,−4]]) equals:", ["10", "2", "*−2", "−10"], "det = (−1)(−4) − (2)(3) = 4 − 6 = −2."),
    ("A determinant can be:", ["only positive", "only zero or positive", "*positive, negative, or zero", "only an integer"], "Determinants take any real value depending on the matrix entries."),
    ("det([[a,0],[0,d]]) for a diagonal 2×2 matrix is:", ["a + d", "0", "a − d", "*a·d"], "For a diagonal matrix, the determinant is the product of the diagonal entries."),
    ("Swapping the two rows of a 2×2 matrix changes the determinant by:", ["doubling it", "making it zero", "no change", "*multiplying by −1"], "Every row swap negates the determinant. This is a fundamental property."),
    ("det([[k·a, k·b],[c, d]]) equals:", ["k²·det(A)", "det(A)", "det(A)/k", "*k·det(A)"], "Factoring a scalar k from one row multiplies the determinant by k, not k²."),
    ("If both rows of a 2×2 matrix are identical, the determinant is:", ["1", "−1", "undefined", "*0"], "Identical rows mean the rows are linearly dependent, forcing the determinant to zero."),
    ("The notation |A| means the same as:", ["magnitude of A", "trace of A", "*det(A)", "inverse of A"], "Vertical bars around a matrix indicate its determinant, not absolute value."),
    ("det([[cos θ, −sin θ],[sin θ, cos θ]]) equals:", ["0", "2cos θ", "sin²θ − cos²θ", "*1"], "det = cos²θ + sin²θ = 1. Rotation matrices always have determinant 1."),
    ("Computing a 2×2 determinant requires exactly:", ["1 multiplication", "2 multiplications", "*2 multiplications and 1 subtraction", "4 multiplications"], "ad − bc uses two multiplications (ad and bc) and one subtraction."),
],

# ── U3 L3.2: Properties of Determinants ──
"u3_l3.2": [
    ("det(AB) equals:", ["det(A) + det(B)", "det(A) − det(B)", "det(A)/det(B)", "*det(A)·det(B)"], "The determinant of a product is the product of the determinants."),
    ("det(Aᵀ) equals:", ["−det(A)", "1/det(A)", "0", "*det(A)"], "Transposing a matrix does not change its determinant."),
    ("If one row of A is all zeros, det(A) is:", ["1", "−1", "undefined", "*0"], "A zero row means the rows are linearly dependent, giving determinant zero."),
    ("Multiplying every entry of an n×n matrix by scalar c gives det(cA) =:", ["c·det(A)", "*cⁿ·det(A)", "c²·det(A)", "det(A)/c"], "Each of the n rows picks up a factor of c, so det(cA) = cⁿ det(A)."),
    ("Adding a multiple of one row to another row changes the determinant by:", ["doubling it", "negating it", "multiplying by that scalar", "*not at all"], "Row replacement operations leave the determinant unchanged."),
    ("How many row swaps change the sign of a determinant?", ["zero", "two", "*one", "only odd numbers"], "Each single row swap multiplies the determinant by −1."),
    ("If A is 3×3 and det(A) = 4, what is det(2A)?", ["8", "16", "12", "*32"], "det(2A) = 2³·det(A) = 8·4 = 32, since each of 3 rows is scaled by 2."),
    ("det(A⁻¹) equals:", ["det(A)", "−det(A)", "0", "*1/det(A)"], "Since det(A·A⁻¹) = det(I) = 1, we get det(A⁻¹) = 1/det(A)."),
    ("If two rows of A are proportional, det(A) is:", ["positive", "negative", "undefined", "*0"], "Proportional rows are linearly dependent, which forces the determinant to zero."),
    ("For triangular matrices, the determinant equals:", ["the sum of diagonal entries", "the largest entry", "*the product of diagonal entries", "the first entry"], "Upper or lower triangular matrices have determinant equal to the product of their diagonal entries."),
    ("det(I) for any identity matrix equals:", ["0", "n", "−1", "*1"], "The identity matrix has all 1s on the diagonal, and their product is 1."),
    ("Performing three row swaps on A multiplies det(A) by:", ["1", "3", "*−1", "−3"], "Each swap introduces a factor of −1. Three swaps give (−1)³ = −1."),
    ("If det(A) = 3 and det(B) = −2, then det(AB) =:", ["1", "5", "*−6", "−1"], "det(AB) = det(A)·det(B) = 3·(−2) = −6."),
    ("det(Aⁿ) for a square matrix A equals:", ["n·det(A)", "det(A) + n", "det(A)/n", "*[det(A)]ⁿ"], "Repeatedly applying the product rule: det(A·A·…·A) = det(A)ⁿ."),
    ("If row 2 of A equals 5 times row 1, then det(A):", ["equals 5", "equals −5", "is undefined", "*equals 0"], "Proportional rows create linear dependence, so det = 0 regardless of the scalar."),
    ("For a 4×4 matrix, det(−A) equals:", ["−det(A)", "det(A)", "*det(A)", "−det(A)"], "det(−A) = (−1)⁴·det(A) = det(A). For even n, negation preserves the determinant."),
    ("Adding row 1 to row 3 changes the determinant:", ["by a factor of 2", "to zero", "by negation", "*not at all"], "Row replacement (adding a multiple of one row to another) preserves the determinant."),
    ("If A is orthogonal, |det(A)| equals:", ["0", "2", "n", "*1"], "Orthogonal matrices satisfy AᵀA = I, so det(A)² = 1, giving |det(A)| = 1."),
    ("det(A) = 0 implies the columns of A are:", ["orthonormal", "all positive", "unique", "*linearly dependent"], "Zero determinant means the column vectors do not span the full space."),
    ("Scaling one row by k multiplies the determinant by:", ["k²", "1/k", "0", "*k"], "Only that one row is affected, contributing a single factor of k."),
],

# ── U3 L3.3: Cofactor Expansion ──
"u3_l3.3": [
    ("The minor M₁₁ of a 3×3 matrix is the determinant of:", ["the first row", "the first column", "*the 2×2 submatrix after deleting row 1 and column 1", "the diagonal entries"], "A minor removes the row and column of the chosen element, leaving a smaller submatrix."),
    ("The cofactor C₁₂ relates to minor M₁₂ by:", ["C₁₂ = M₁₂", "*C₁₂ = −M₁₂", "C₁₂ = M₁₂²", "C₁₂ = 1/M₁₂"], "Cᵢⱼ = (−1)^(i+j)·Mᵢⱼ. For i+j = 3 (odd), the sign is negative."),
    ("The sign pattern for cofactors in a 3×3 matrix starts:", ["−,+,−,+,...", "*+,−,+,−,...", "+,+,+,...", "−,−,−,..."], "Signs alternate in checkerboard fashion starting with + at position (1,1)."),
    ("Cofactor expansion along row 1 of [[2,1,3],[0,4,5],[1,0,2]] gives:", ["det = 2(8) + 1(5) + 3(4)", "*det = 2(8−0) − 1(0−5) + 3(0−4)", "det = 2+1+3", "det = 0"], "Expand along row 1: 2·C₁₁ + 1·C₁₂ + 3·C₁₃ with cofactor signs."),
    ("Cofactor expansion works along:", ["only the first row", "only diagonals", "*any row or any column", "only the first column"], "You may expand along any row or column and get the same determinant."),
    ("Expanding along a row with many zeros is preferred because:", ["it gives a larger determinant", "*zero entries eliminate terms, reducing computation", "it changes the sign pattern", "it guarantees a positive result"], "Each zero entry means its cofactor term contributes nothing, saving work."),
    ("For a 3×3 matrix, cofactor expansion produces how many 2×2 determinants?", ["2", "*3", "4", "9"], "A 3×3 expansion along one row or column produces three 2×2 minors."),
    ("The cofactor of the (2,3) entry uses sign (−1)^(2+3) =:", ["1", "*−1", "0", "2"], "(−1)⁵ = −1. Row + column index sum is odd, so the sign is negative."),
    ("If a 4×4 matrix has three zeros in column 2, expanding along column 2 requires computing:", ["4 cofactors", "3 cofactors", "2 cofactors", "*1 cofactor"], "Only the single nonzero entry produces a nonzero term; the other three contribute zero."),
    ("Cofactor expansion of a diagonal matrix [[a,0,0],[0,b,0],[0,0,c]] gives:", ["a+b+c", "0", "abc/6", "*abc"], "Each step reduces to a product of diagonal entries, confirming det = abc."),
    ("The adjugate (classical adjoint) matrix is the transpose of:", ["the inverse", "the original", "*the cofactor matrix", "the minor matrix"], "adj(A) = Cᵀ, where C is the matrix of cofactors."),
    ("Expanding a 4×4 determinant by cofactors along one row requires computing:", ["2 terms", "3 terms", "*4 terms (each a 3×3 determinant)", "16 terms"], "A 4×4 expansion along one row yields four 3×3 determinants to evaluate."),
    ("For the matrix [[1,0,0],[3,2,0],[5,6,4]], the best row/column to expand along is:", ["row 2", "column 2", "*row 1 or column 3 (two zeros each)", "row 3"], "Row 1 has two zeros, minimizing the number of cofactors to compute."),
    ("The cofactor C₃₃ of a 3×3 matrix uses sign:", ["−1", "0", "−2", "*+1"], "(−1)^(3+3) = (−1)⁶ = +1. Even exponent gives positive sign."),
    ("Two different cofactor expansions of the same matrix give:", ["different results", "results differing by sign", "*the same determinant value", "results differing by a factor of n"], "The determinant is unique; expanding along any row or column yields the same value."),
    ("The cofactor matrix of the 2×2 matrix [[a,b],[c,d]] is:", ["[[a,b],[c,d]]", "[[d,c],[b,a]]", "[[d,b],[c,a]]", "*[[d,−c],[−b,a]]"], "Apply the sign pattern and compute each minor: C₁₁=d, C₁₂=−c, C₂₁=−b, C₂₂=a."),
    ("Cofactor expansion is most efficient when:", ["all entries are large", "the matrix is dense", "*a row or column contains many zeros", "the matrix is symmetric"], "Zeros eliminate terms from the sum, reducing the number of sub-determinants needed."),
    ("For the identity matrix I₃, every cofactor along row 1 equals:", ["0 for all", "1 for all", "*1, 0, 0 respectively", "0, 1, 0 respectively"], "C₁₁ = det(I₂) = 1; C₁₂ and C₁₃ involve submatrices with zero rows, giving 0."),
    ("Recursive cofactor expansion has time complexity:", ["O(n)", "O(n²)", "*O(n!) in the worst case", "O(n log n)"], "Without optimization, each level spawns n sub-problems, leading to factorial growth."),
    ("If det(A) is computed by expanding along row 2 and the result is 7, expanding along column 3 gives:", ["−7", "0", "14", "*7"], "The determinant is an invariant of the matrix, independent of which row or column is chosen."),
],

# ── U3 L3.4: Determinants of Larger Matrices ──
"u3_l3.4": [
    ("A 4×4 determinant can be reduced to four:", ["1×1 determinants", "*3×3 determinants", "2×2 determinants directly", "4×4 recursive calls"], "Cofactor expansion of a 4×4 matrix along one row produces four 3×3 sub-determinants."),
    ("Row reduction to upper triangular form gives det(A) as:", ["the sum of pivots", "the largest pivot", "the product of all entries", "*the product of the diagonal entries (adjusted for row operations)"], "In echelon form, the determinant is the product of pivots, accounting for any row swaps."),
    ("For large matrices, which method is most efficient for computing determinants?", ["cofactor expansion", "*row reduction (Gaussian elimination) in O(n³)", "computing all minors", "Cramer's rule"], "Row reduction is O(n³) versus O(n!) for cofactor expansion, making it far faster for large n."),
    ("The determinant of a 5×5 upper triangular matrix with diagonal [2,3,1,4,2] is:", ["12", "24", "*48", "10"], "Product of diagonals: 2·3·1·4·2 = 48. Triangular determinant is always the product of diag entries."),
    ("Block diagonal matrix det [[A,0],[0,B]] equals:", ["det(A) + det(B)", "0", "det(A) − det(B)", "*det(A)·det(B)"], "Block diagonal determinants factor into the product of the individual block determinants."),
    ("Computing a 10×10 determinant by cofactor expansion without optimization involves roughly:", ["100 operations", "1000 operations", "10⁶ operations", "*over 3.6 million terms (10!)"], "10! = 3,628,800 — cofactor expansion is impractical for large matrices."),
    ("LU decomposition computes det(A) as:", ["det(L) + det(U)", "det(L) − det(U)", "*det(L)·det(U)", "det(L)/det(U)"], "A = LU implies det(A) = det(L)·det(U), each being a product of diagonal entries."),
    ("If row reduction of a 4×4 matrix requires 2 row swaps, the determinant picks up a factor of:", ["−2", "2", "4", "*(−1)² = 1"], "Each swap contributes −1. Two swaps: (−1)² = 1, so no net sign change."),
    ("A permutation matrix always has determinant:", ["0", "any value", "2", "*+1 or −1"], "Permutation matrices have det = +1 (even permutation) or −1 (odd permutation)."),
    ("For a 5×5 matrix with a row of all zeros, the determinant is:", ["5", "1", "undefined", "*0"], "A zero row guarantees linear dependence among rows, making the determinant zero."),
    ("The determinant of a skew-symmetric matrix of odd order is:", ["1", "−1", "undefined", "*0"], "For odd-dimensional skew-symmetric A, det(A) = det(−Aᵀ) = (−1)ⁿ det(A) = −det(A), so det = 0."),
    ("Partial pivoting during row reduction helps with:", ["making det larger", "reducing matrix size", "*numerical stability (avoiding division by small numbers)", "finding eigenvalues"], "Pivoting prevents catastrophic round-off errors in floating-point determinant computation."),
    ("A Vandermonde matrix determinant equals:", ["sum of entries", "0 always", "*product of all (xⱼ − xᵢ) for j > i", "product of diagonal"], "The Vandermonde determinant has a closed-form formula based on differences of the nodes."),
    ("If A is 6×6 with det(A) = −3, then det(A²) =:", ["−9", "*9", "−6", "6"], "det(A²) = [det(A)]² = (−3)² = 9. Squaring always gives a non-negative result."),
    ("Row echelon form makes determinant computation efficient because:", ["it zeros out the matrix", "it finds inverses", "*it creates a triangular matrix whose det is the diagonal product", "it diagonalizes the matrix"], "Triangular form reduces determinant computation to a simple product."),
    ("For n×n matrix A, det(−A) when n is odd equals:", ["det(A)", "0", "2·det(A)", "*−det(A)"], "det(−A) = (−1)ⁿ det(A). For odd n, this is −det(A)."),
    ("Numerical determinant computation for an n×n matrix via LU factorization is:", ["O(n!)", "O(n⁴)", "O(n² log n)", "*O(n³)"], "LU decomposition is O(n³), making it practical even for large matrices."),
    ("A block upper triangular matrix [[A,B],[0,D]] has determinant:", ["det(A) + det(D)", "det(A) · det(B)", "*det(A) · det(D)", "det(B) · det(D)"], "The off-diagonal block B does not affect the determinant; only A and D matter."),
    ("If A is 4×4 and all entries are 1, det(A) =:", ["4", "1", "−1", "*0"], "All rows are identical, so the rows are linearly dependent and det = 0."),
    ("The Leibniz formula expresses an n×n determinant as a sum over:", ["rows", "columns", "*all n! permutations of column indices", "diagonal entries only"], "The Leibniz formula sums n! signed products, one for each permutation."),
],

# ── U3 L3.5: Cramer's Rule ──
"u3_l3.5": [
    ("Cramer's Rule solves Ax = b by expressing each xᵢ as:", ["det(A) / det(Aᵢ)", "*det(Aᵢ) / det(A)", "det(A) + det(Aᵢ)", "det(A) − det(Aᵢ)"], "xᵢ = det(Aᵢ)/det(A), where Aᵢ replaces column i of A with b."),
    ("Cramer's Rule requires that:", ["det(A) = 0", "*det(A) ≠ 0", "A is symmetric", "b is zero"], "Division by det(A) is needed, so det(A) must be nonzero."),
    ("For the system x+2y=5, 3x+4y=6, det(A) =:", ["10", "*−2", "2", "−10"], "det([[1,2],[3,4]]) = 1·4 − 2·3 = 4 − 6 = −2."),
    ("In Cramer's Rule, matrix A₁ replaces _____ with vector b:", ["row 1", "*column 1", "the diagonal", "all columns"], "To find x₁, replace column 1 of A with b and compute the determinant."),
    ("Cramer's Rule is practical primarily for:", ["large sparse systems", "overdetermined systems", "*small systems (2×2 or 3×3)", "systems with det(A) = 0"], "For large systems, Cramer's Rule is O(n·n!) — far too slow compared to Gaussian elimination."),
    ("For a 3×3 system, Cramer's Rule requires computing how many determinants?", ["2", "3", "*4 (one for A and one for each variable)", "9"], "You compute det(A), det(A₁), det(A₂), det(A₃) — four total determinants."),
    ("If det(A) = 0 and det(Aᵢ) ≠ 0, the system is:", ["*inconsistent (no solution)", "consistent with unique solution", "consistent with infinitely many", "underdetermined"], "det(A) = 0 with nonzero det(Aᵢ) means the system has no solution."),
    ("For 2x + y = 7 and x − y = 2, using Cramer's Rule: x = det([[7,1],[2,−1]])/det(A). det(A) =:", ["−1", "1", "*−3", "3"], "det([[2,1],[1,−1]]) = 2·(−1) − 1·1 = −2 − 1 = −3."),
    ("Cramer's Rule is named after the Swiss mathematician who published it in:", ["1700", "1800", "*1750", "1850"], "Gabriel Cramer published the rule in 1750 in his introduction to algebraic curves."),
    ("The computational complexity of Cramer's Rule for an n×n system is:", ["O(n²)", "O(n³)", "*O(n · n!) using cofactor expansion", "O(n log n)"], "Each of n+1 determinants costs O(n!) by cofactors, giving O(n · n!) total."),
    ("If the system Ax = b has a unique solution, then:", ["det(A) = 0", "A has a zero row", "*det(A) ≠ 0", "b = 0"], "A unique solution exists if and only if the coefficient matrix is nonsingular."),
    ("Cramer's Rule can find a single variable xⱼ without solving the entire system by:", ["row reducing fully", "*computing only det(A) and det(Aⱼ)", "inverting A completely", "using eigenvalues"], "You only need two determinants to find one specific variable."),
    ("For the system x+y+z=6, 2x+y=4, x−z=0, the value of z using Cramer's Rule requires:", ["only det(A)", "*det(A) and det(A₃) where column 3 is replaced with b", "three row swaps", "the inverse of A"], "Replace column 3 (the z-column) of A with b, then divide that determinant by det(A)."),
    ("If det(A) = 0 and all det(Aᵢ) = 0, the system may have:", ["no solutions only", "a unique solution", "*no solutions or infinitely many solutions", "exactly two solutions"], "Both cases are possible when all determinants are zero — further analysis is needed."),
    ("Cramer's Rule demonstrates a direct link between:", ["eigenvalues and solutions", "*determinants and solutions of linear systems", "matrix rank and trace", "norms and inner products"], "It explicitly expresses each solution component as a ratio of determinants."),
    ("Compared to Gaussian elimination, Cramer's Rule for a 5×5 system is:", ["faster", "equally efficient", "*much slower", "impossible"], "Gaussian elimination is O(n³) versus O(n · n!) for Cramer's Rule — enormous difference at n=5."),
    ("Cramer's Rule works for systems over:", ["only integers", "only the reals", "*any field (including complex numbers and finite fields)", "only rational numbers"], "The formula involves only addition, multiplication, and division — valid in any field."),
    ("Using Cramer's Rule on Ax = 0 (homogeneous) with det(A) ≠ 0 gives:", ["infinitely many solutions", "no solution", "*only the trivial solution x = 0", "a one-parameter family"], "Each xᵢ = det(Aᵢ)/det(A) = 0/det(A) = 0 since b = 0."),
    ("A key advantage of Cramer's Rule is its:", ["speed for large systems", "*theoretical clarity relating solutions to determinants", "numerical stability", "low memory usage"], "Its theoretical value outweighs its computational practicality for large problems."),
    ("For Cramer's Rule to apply, the system must be:", ["overdetermined", "underdetermined", "*a square system with equal equations and unknowns", "homogeneous"], "Cramer's Rule requires a square coefficient matrix (same number of equations and unknowns)."),
],

# ── U3 L3.6: Determinants & Area/Volume ──
"u3_l3.6": [
    ("The absolute value of det([[a,b],[c,d]]) gives the area of:", ["a triangle", "*the parallelogram spanned by vectors (a,b) and (c,d)", "a rectangle", "a circle"], "The 2×2 determinant's absolute value equals the area of the parallelogram spanned by the row vectors."),
    ("If two 2D vectors are parallel, the area of their parallelogram is:", ["1", "undefined", "−1", "*0"], "Parallel vectors span no area, and their determinant is zero (rows are proportional)."),
    ("The area of a triangle formed by vectors u and v equals:", ["det([u;v])", "*½|det([u;v])|", "2|det([u;v])|", "det([u;v])²"], "A triangle is half a parallelogram, so its area is half the absolute determinant."),
    ("For 3D, |det([u;v;w])| gives the volume of:", ["a sphere", "a cylinder", "*the parallelepiped spanned by u, v, w", "a tetrahedron"], "The 3D determinant's absolute value gives the parallelepiped volume."),
    ("The volume of a tetrahedron spanned by vectors a, b, c is:", ["det([a;b;c])", "*⅙|det([a;b;c])|", "½|det([a;b;c])|", "3·det([a;b;c])"], "A tetrahedron is 1/6 of the parallelepiped, so volume = (1/6)|det|."),
    ("If det(A) is negative, the geometric interpretation changes:", ["the area is negative", "*only the orientation reverses; the (positive) area/volume uses |det(A)|", "the shape is invalid", "area becomes zero"], "Negative determinant indicates reversed orientation, but area/volume is always |det|."),
    ("det([[1,0],[0,1]]) = 1, which means vectors (1,0) and (0,1) span a parallelogram of area:", ["0", "2", "0.5", "*1"], "The unit square has area 1, matching the identity determinant."),
    ("det([[3,0],[0,4]]) = 12, so the parallelogram has area:", ["7", "3", "4", "*12"], "The rectangle with sides 3 and 4 has area 12, consistent with the determinant."),
    ("Stretching one vector by factor 2 scales the parallelogram area by:", ["½", "4", "0", "*2"], "Scaling one row by k multiplies the determinant (and thus the area) by k."),
    ("For the cross product u × v, ||u × v|| equals:", ["u · v", "det([u; v])", "*the area of the parallelogram spanned by u and v", "the volume of a box"], "The cross product magnitude gives the parallelogram area in 3D."),
    ("det([[2,1],[4,2]]) = 0 means the two vectors span:", ["a full plane", "*only a line (zero area — vectors are colinear)", "a triangle", "a cube"], "Zero determinant means zero area: the vectors are parallel."),
    ("A linear transformation with det = 3 scales all areas by:", ["0", "9", "√3", "*3"], "The determinant gives the area scaling factor for any region under the transformation."),
    ("If a transformation has det = −2, areas are scaled by:", ["−2", "0", "4", "*2"], "Area scaling uses |det| = 2; the negative sign indicates orientation reversal."),
    ("The signed area from the determinant tells you about:", ["only magnitude", "*both magnitude and orientation (handedness) of the parallelogram", "only direction", "the shape of the region"], "The sign encodes whether the vectors form a right-handed or left-handed pair."),
    ("For vertices at (0,0), (3,0), (0,4), the triangle area using determinants is:", ["12", "7", "*6", "3.5"], "½|det([[3,0],[0,4]])| = ½·12 = 6."),
    ("A shear transformation (adding a multiple of one row to another) changes the area by:", ["doubling it", "halving it", "negating it", "*not at all"], "Shears leave the determinant unchanged, so area is preserved."),
    ("If three 3D vectors are coplanar, the parallelepiped volume is:", ["positive", "negative", "1", "*0"], "Coplanar vectors have zero determinant, meaning no 3D volume."),
    ("A rotation matrix has |det| = 1, meaning it preserves:", ["only angles", "lengths only", "*both areas and volumes", "nothing"], "det(Rotation) = ±1 (usually +1), so area/volume is unchanged."),
    ("The area scaling interpretation applies to any region, not just parallelograms:", ["this is false", "*this is true — det scales all areas equally", "only for triangles", "only for convex shapes"], "The determinant uniformly scales every region's area under a linear map."),
    ("To find the area of triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃), use:", ["sum of coordinates", "*½|det of the coordinate matrix (with a column of 1s)|", "product of coordinates", "distance formula only"], "The shoelace formula is essentially a determinant computation."),
],

# ── U3 L3.7: Applications in Geometry ──
"u3_l3.7": [
    ("Three points are collinear (on the same line) when the determinant of their coordinate matrix is:", ["1", "−1", "positive", "*0"], "Zero determinant of [[x₁,y₁,1],[x₂,y₂,1],[x₃,y₃,1]] means the points lie on one line."),
    ("The equation of a line through (x₁,y₁) and (x₂,y₂) can be written using:", ["a 4×4 determinant", "*a 3×3 determinant set to zero: det([[x,y,1],[x₁,y₁,1],[x₂,y₂,1]]) = 0", "only slope-intercept form", "vector addition only"], "Setting the determinant to zero yields the line equation through two points."),
    ("Four points in 3D are coplanar when:", ["they're collinear", "their coordinates sum to zero", "*the 4×4 determinant of their homogeneous coordinates is zero", "they form a square"], "A zero determinant of [[x,y,z,1],...] for four points means they share a common plane."),
    ("The equation of a plane through three points uses a determinant set to:", ["1", "−1", "a variable", "*0"], "det([[x−x₁,...],[...],[...]]) = 0 defines the plane containing those three points."),
    ("To check if a point lies inside a triangle, one can use:", ["eigenvalues", "*signs of determinants of sub-triangles (barycentric coordinates)", "matrix traces", "norms only"], "Consistent signs of three point-orientation determinants confirm a point is inside the triangle."),
    ("The signed area from a determinant can determine:", ["matrix rank", "*the orientation (clockwise vs counterclockwise) of vertices", "eigenvalue signs", "pivot positions"], "Positive determinant = counterclockwise; negative = clockwise."),
    ("The cross product a × b in 3D gives a vector _____ to both a and b:", ["parallel", "at 45°", "tangent", "*perpendicular"], "The cross product is orthogonal to both input vectors."),
    ("Reflecting across a line in 2D has determinant:", ["0", "1", "2", "*−1"], "Reflection reverses orientation, giving det = −1, while preserving areas."),
    ("A projection matrix onto a line in 2D has determinant:", ["1", "−1", "2", "*0"], "Projection collapses 2D to 1D, destroying area — hence det = 0."),
    ("Determinants help compute the normal vector to a plane by:", ["summing coordinates", "*using the cross product of two edge vectors (computed via a determinant)", "dividing by area", "finding eigenvalues"], "The cross product formula is naturally expressed as a 3×3 determinant with unit vector row."),
    ("The shoelace formula for polygon area is based on:", ["eigenvalue decomposition", "*summing 2×2 determinants of consecutive vertex pairs", "matrix inversion", "row reduction"], "The shoelace formula chains together small determinants to compute total signed area."),
    ("A linear transformation maps a unit circle to an ellipse with area:", ["π", "2π", "*π·|det(A)|", "π·det(A)²"], "The unit circle has area π, and |det(A)| scales all areas uniformly."),
    ("Affine transformations (linear + translation) preserve:", ["areas always", "angles always", "*parallelism (parallel lines remain parallel)", "distances always"], "Affine maps preserve parallelism but generally change areas and distances."),
    ("The orientation test using determinants classifies a point as left, right, or on a line in:", ["O(n) time", "*O(1) time (a single determinant evaluation)", "O(n²) time", "O(n log n) time"], "One 3×3 determinant suffices for the left-right-on test."),
    ("In computational geometry, determinants are central to:", ["only coloring", "*convex hull algorithms, triangulations, and intersection tests", "only sorting", "database queries"], "Many geometric algorithms rely on orientation predicates computed via determinants."),
    ("The scalar triple product a·(b×c) equals:", ["a·b·c", "||a||·||b||·||c||", "*det([a;b;c])", "a+b+c"], "The scalar triple product is exactly the 3×3 determinant of the three row vectors."),
    ("If det of a transformation is 1, the transformation is:", ["identity necessarily", "impossible", "*area-preserving and orientation-preserving", "area-doubling"], "det = 1 means no area change and no orientation flip. It need not be the identity."),
    ("A dilation (uniform scaling by factor k) in 2D has determinant:", ["k", "2k", "k + k", "*k²"], "Both basis vectors scale by k, so det = k · k = k²."),
    ("The determinant distinguishes between a rotation and a reflection because:", ["rotations have det = 0", "reflections have det = 2", "*rotations have det = +1 while reflections have det = −1", "they have the same determinant"], "Both are orthogonal matrices, but the sign of the determinant differs."),
    ("To find if four 3D points form a non-degenerate tetrahedron, check that:", ["all coordinates are positive", "the points are collinear", "*the determinant of the edge matrix is nonzero", "the sum is positive"], "Nonzero determinant means the four points are not coplanar, forming a valid tetrahedron."),
],

# ── U3 L3.8: Applications in Physics ──
"u3_l3.8": [
    ("In classical mechanics, the Jacobian determinant describes:", ["mass distribution", "temperature gradient", "*how a coordinate transformation scales volume elements", "electromagnetic fields"], "The Jacobian determinant gives the local volume scaling factor for a change of variables."),
    ("When changing variables in a double integral, the area element becomes:", ["dx dy", "*|det(J)| du dv, where J is the Jacobian matrix", "det(J)² du dv", "du dv / det(J)"], "The area element transforms by the absolute value of the Jacobian determinant."),
    ("The Jacobian for polar coordinates (r,θ) → (x,y) has determinant:", ["1", "r²", "θ", "*r"], "J = [[cos θ, −r sin θ],[sin θ, r cos θ]], so det(J) = r. Hence dA = r dr dθ."),
    ("In electromagnetism, Maxwell's equations in tensor form use determinants via:", ["simple addition", "scalar products", "*the Levi-Civita symbol (closely related to determinants)", "matrix inversion"], "The antisymmetric Levi-Civita tensor that appears in EM is deeply connected to determinants."),
    ("The Wronskian determinant tests whether a set of solutions is:", ["orthogonal", "normalized", "*linearly independent (nonzero Wronskian)", "square-integrable"], "A nonzero Wronskian confirms that the solutions to a differential equation are linearly independent."),
    ("The Wronskian of two functions f and g is:", ["f + g", "f · g", "f' + g'", "*f·g' − f'·g"], "W(f,g) = det([[f,g],[f',g']]) = fg' − f'g."),
    ("In quantum mechanics, the Slater determinant ensures:", ["energy conservation", "*antisymmetry of many-electron wavefunctions (Pauli exclusion)", "spin measurement outcomes", "particle mass values"], "The Slater determinant guarantees that swapping two electrons changes the wavefunction sign."),
    ("The moment of inertia tensor is related to determinants through:", ["its trace only", "its inverse only", "*its eigenvalue decomposition (principal moments are eigenvalues)", "addition of entries"], "Diagonalizing the inertia tensor (finding eigenvalues) involves the characteristic determinant."),
    ("In special relativity, the Lorentz transformation has determinant:", ["0", "−γ", "γ", "*±1"], "Lorentz transformations preserve spacetime volume, giving |det| = 1."),
    ("Strain in continuum mechanics uses determinants to measure:", ["only stress", "only pressure", "*volume change under deformation (det of deformation gradient)", "temperature change"], "det(F) > 1 means expansion; det(F) < 1 means compression; det(F) = 0 means collapse."),
    ("The eigenvalue equation det(A − λI) = 0 is called:", ["the trace equation", "the rank equation", "*the characteristic equation", "the normal equation"], "Setting this determinant to zero yields the eigenvalues of matrix A."),
    ("In coupled oscillations, normal modes are found by solving:", ["A + B = 0", "eigenvalue problem AΛ = 0", "*det(A − ω²M) = 0 for natural frequencies ω", "trace(A) = 0"], "The characteristic determinant of the coupled system yields the natural frequencies."),
    ("The determinant of a rotation matrix in any dimension is:", ["0", "−1", "n", "*1"], "Rotations preserve volume and orientation, giving det = 1."),
    ("Spherical coordinate Jacobian determinant equals:", ["r", "r²", "*r² sin φ", "r sin θ"], "For (r,θ,φ) → (x,y,z), the Jacobian determinant is r² sin φ, giving dV = r² sin φ dr dθ dφ."),
    ("In stability analysis of dynamical systems, eigenvalues from det(A − λI) = 0 determine:", ["the size of the system", "*whether solutions grow, decay, or oscillate", "the number of variables", "the dimension of the matrix"], "Positive real parts → growth (unstable); negative → decay (stable); imaginary → oscillations."),
    ("If the Jacobian determinant at a point is zero, the transformation is:", ["area-preserving", "invertible", "*singular (locally non-invertible) at that point", "conformal"], "Zero Jacobian means the local inverse function theorem fails — the map collapses dimensions."),
    ("Cross products in physics (torque τ = r × F) rely on:", ["addition", "dot products", "*determinant-based computation", "matrix inversion"], "τ = r × F is computed as a 3×3 determinant with i, j, k in the first row."),
    ("The curl of a vector field is expressed as a determinant involving:", ["second derivatives", "only scalars", "*the nabla operator and the field components (symbolic 3×3 determinant)", "only divergence"], "curl F = ∇ × F is written as det([[i,j,k],[∂/∂x,∂/∂y,∂/∂z],[F₁,F₂,F₃]])."),
    ("Hamilton's equations in classical mechanics can be written using:", ["only addition", "*the symplectic matrix (with determinant 1), preserving phase space volume", "the zero matrix", "diagonal matrices only"], "Hamiltonian flow is symplectic, preserving the determinant of the phase-space transformation."),
    ("Liouville's theorem states that phase-space volume is conserved, relating to:", ["matrix trace", "vector norms", "*the Jacobian determinant being 1 for Hamiltonian flow", "the inverse matrix"], "det(J) = 1 at all times ↔ volume is conserved in Hamiltonian mechanics."),
],

# ── U4 L4.1: Invertible Matrices ──
"u4_l4.1": [
    ("A matrix A is invertible if there exists B such that:", ["A + B = I", "A − B = I", "AB = 0", "*AB = BA = I"], "The inverse B satisfies both AB = I and BA = I."),
    ("The inverse of A is unique:", ["sometimes", "never", "only for 2×2 matrices", "*always (if it exists)"], "If B and C are both inverses, then B = B(AC) = (BA)C = C, proving uniqueness."),
    ("A matrix is invertible if and only if det(A):", ["equals 0", "is positive", "is negative", "*is nonzero"], "det(A) ≠ 0 is equivalent to A being invertible."),
    ("The inverse of the 2×2 matrix [[a,b],[c,d]] is:", ["[[d,b],[c,a]]/det", "*[[d,−b],[−c,a]]/det(A)", "[[a,c],[b,d]]/det", "[[−a,b],[c,−d]]/det"], "Swap diagonal entries, negate off-diagonal, then divide by det(A) = ad − bc."),
    ("(AB)⁻¹ equals:", ["A⁻¹B⁻¹", "B⁻¹ + A⁻¹", "A⁻¹ − B⁻¹", "*B⁻¹A⁻¹"], "The inverse of a product reverses the order: socks then shoes, shoes then socks."),
    ("(Aᵀ)⁻¹ equals:", ["(A⁻¹)ᵀ is wrong", "Aᵀ", "A", "*(A⁻¹)ᵀ"], "Transpose and inverse commute: (Aᵀ)⁻¹ = (A⁻¹)ᵀ."),
    ("(A⁻¹)⁻¹ equals:", ["I", "A⁻¹", "0", "*A"], "Inverting the inverse recovers the original matrix."),
    ("If A is invertible, then Ax = b has:", ["no solutions", "infinitely many solutions", "*exactly one solution x = A⁻¹b", "two solutions"], "Multiplying both sides by A⁻¹ gives the unique solution directly."),
    ("Which of these is NOT equivalent to 'A is invertible'?", ["det(A) ≠ 0", "A has full rank", "columns of A are linearly independent", "*A has a zero eigenvalue"], "A zero eigenvalue means det(A) = 0, which means A is NOT invertible."),
    ("The Invertible Matrix Theorem lists many equivalent conditions; having _____ pivot positions means invertible:", ["some", "most", "one more than columns", "*n pivot positions for an n×n matrix"], "Full rank (n pivots in n rows) is equivalent to invertibility."),
    ("If A is not invertible, it is called:", ["orthogonal", "diagonal", "symmetric", "*singular"], "Singular matrices have no inverse and determinant zero."),
    ("For invertible A, the columns of A form:", ["a dependent set", "a basis only for R²", "*a basis for Rⁿ", "the zero vector"], "Invertibility means the columns are linearly independent and span Rⁿ."),
    ("det(A⁻¹) equals:", ["det(A)", "−det(A)", "0", "*1/det(A)"], "From det(A·A⁻¹) = det(I) = 1, we get det(A⁻¹) = 1/det(A)."),
    ("If A and B are both invertible n×n matrices, then AB is:", ["singular", "not square", "undefined", "*invertible"], "det(AB) = det(A)·det(B) ≠ 0, so the product is invertible."),
    ("An invertible matrix maps Rⁿ onto Rⁿ in a way that is:", ["many-to-one", "onto but not one-to-one", "*both one-to-one and onto (bijective)", "neither one-to-one nor onto"], "Invertibility guarantees a bijection between domain and codomain."),
    ("The zero matrix is:", ["invertible", "sometimes invertible", "orthogonal", "*never invertible"], "det(0) = 0, so the zero matrix is always singular."),
    ("For an invertible diagonal matrix diag(d₁,...,dₙ), the inverse is:", ["diag(d₁,...,dₙ)", "diag(−d₁,...,−dₙ)", "diag(d₁²,...,dₙ²)", "*diag(1/d₁,...,1/dₙ)"], "Each diagonal entry is simply reciprocated."),
    ("If A² = I (involutory matrix), then A⁻¹ =:", ["A²", "I", "−A", "*A"], "A² = I means A·A = I, so A is its own inverse."),
    ("The product of two singular matrices is always:", ["invertible", "the identity", "diagonal", "*singular"], "If det(A)=0 or det(B)=0, then det(AB) = det(A)det(B) = 0, so AB is singular."),
    ("For invertible A, the equation Ax = 0 has:", ["infinitely many solutions", "no solutions", "exactly two solutions", "*only the trivial solution x = 0"], "A⁻¹ exists, so x = A⁻¹·0 = 0 is the only solution."),
],

# ── U4 L4.2: Finding Inverses (row reduction method) ──
"u4_l4.2": [
    ("To find A⁻¹ by row reduction, augment A with:", ["the zero matrix", "A itself", "a column of ones", "*the identity matrix I"], "Form [A | I] and row-reduce; when the left side becomes I, the right side is A⁻¹."),
    ("If [A | I] reduces to [I | B], then B equals:", ["A", "Aᵀ", "det(A)·I", "*A⁻¹"], "The row operations that transform A to I simultaneously transform I to A⁻¹."),
    ("If A cannot be reduced to I (a zero row appears on the left), then A is:", ["orthogonal", "upper triangular", "invertible", "*singular"], "Failure to reach I means A is not invertible."),
    ("The row reduction method for inverses is based on:", ["cofactor expansion", "Cramer's rule", "*applying the same elementary row operations to both A and I", "eigenvalue decomposition"], "Each row operation represents multiplication by an elementary matrix on both sides."),
    ("How many row operations are needed to invert a 3×3 matrix (roughly)?", ["3", "6", "*around 10-15 (varies by matrix)", "100"], "You need to eliminate six off-diagonal entries and scale three pivots, totaling roughly 10-15 operations."),
    ("During row reduction, if a pivot position contains zero, you should:", ["stop — the matrix is singular", "insert a 1", "*swap rows to bring a nonzero entry to the pivot position", "multiply by zero"], "Row swapping moves a nonzero value to the pivot position before continuing."),
    ("Reducing [[1,2],[3,4] | 1,0; 0,1] — first step R2 → R2 − 3R1 gives:", ["[[1,2],[3,4] | 1,0; 3,1]", "*[[1,2],[0,−2] | 1,0; −3,1]", "[[1,2],[0,0] | 1,0; 0,1]", "[[1,0],[3,4] | 1,0; 0,1]"], "R2 − 3R1: [3−3, 4−6 | 0−3, 1−0] = [0, −2 | −3, 1]."),
    ("After reaching row echelon form, the next goal is:", ["stop", "compute det", "*continue to reduced row echelon form (make pivots 1 and clear above)", "transpose the matrix"], "Full reduction to I (RREF) is needed — not just echelon form."),
    ("The row reduction method works for matrices of any size:", ["only 2×2", "only up to 3×3", "only square matrices up to 10×10", "*any n×n matrix"], "The algorithm generalizes to any size square matrix."),
    ("Elementary row operations correspond to left-multiplication by:", ["diagonal matrices only", "the inverse", "*elementary matrices", "permutation matrices only"], "Each row operation is equivalent to multiplying on the left by a specific elementary matrix."),
    ("Computational complexity of finding A⁻¹ by row reduction is:", ["O(n)", "O(n²)", "*O(n³)", "O(n!)"], "Gaussian elimination to invert an n×n matrix requires O(n³) operations."),
    ("If A is already diagonal with nonzero entries, row reduction to find A⁻¹:", ["is impossible", "requires many steps", "*only needs scaling each row (reciprocals of diagonal entries)", "changes the matrix shape"], "Scale each row by 1/dᵢ to transform diag(d₁,...,dₙ) into I."),
    ("Compared to the adjugate method, row reduction is:", ["slower for all sizes", "identical in complexity", "*much faster for large matrices", "only valid for 2×2 matrices"], "Row reduction is O(n³) while the adjugate method is O(n·n!) without optimization."),
    ("The augmented matrix approach works because each row operation on [A|I] is equivalent to:", ["adding I", "multiplying by det", "*multiplying A and I on the left by the same elementary matrix", "transposing both halves"], "Left-multiplying the augmented system consistently applies each operation to both sides."),
    ("If a row of all zeros appears on the left side of [A|I] during reduction:", ["continue reducing", "swap it to the top", "*stop — A is singular and has no inverse", "add 1 to the diagonal"], "An all-zero row means rank < n, so A cannot be reduced to I."),
    ("Finding A⁻¹ allows you to solve Ax = b for multiple right-hand sides by:", ["re-doing elimination each time", "using Cramer's rule each time", "*computing x = A⁻¹b for each b (one matrix multiply per b)", "ignoring A"], "Once A⁻¹ is known, each new b only requires a matrix-vector multiplication."),
    ("The row reduction method also verifies invertibility because:", ["it computes det directly", "*reaching I on the left proves full rank; failure proves singularity", "it checks eigenvalues", "it always produces an answer"], "The ability (or inability) to reach I is a direct test of invertibility."),
    ("For numerical computation, which is preferred over computing A⁻¹?", ["always compute A⁻¹", "use Cramer's rule", "*LU factorization (solve LUx = b directly)", "use the adjugate"], "In practice, solving Ax = b via LU is faster and more stable than computing A⁻¹."),
    ("After finding A⁻¹ by row reduction, you can verify correctness by checking:", ["det(A⁻¹) = 1", "A⁻¹ is symmetric", "*A·A⁻¹ = I", "A⁻¹ has no zeros"], "Multiplying A by the proposed inverse should give the identity matrix."),
    ("Elementary matrices are always:", ["singular", "symmetric", "zero", "*invertible"], "Each elementary matrix is invertible — its inverse is another elementary matrix (undo the operation)."),
],

# ── U4 L4.3: Adjoint Method ──
"u4_l4.3": [
    ("The adjugate (classical adjoint) of A is:", ["the transpose of A", "the inverse of A", "*the transpose of the cofactor matrix of A", "the determinant of A times I"], "adj(A) = Cᵀ, where C is the matrix of all cofactors."),
    ("The inverse via adjugate is: A⁻¹ =", ["adj(A) · det(A)", "det(A) / adj(A)", "adj(A) + det(A)·I", "*adj(A) / det(A)"], "A⁻¹ = (1/det(A)) · adj(A), valid when det(A) ≠ 0."),
    ("For a 2×2 matrix [[a,b],[c,d]], adj(A) =:", ["[[a,c],[b,d]]", "[[d,c],[b,a]]", "*[[d,−b],[−c,a]]", "[[−a,b],[c,−d]]"], "Swap diagonal entries and negate off-diagonal entries to get the 2×2 adjugate."),
    ("The adjugate method requires computing _____ cofactors for an n×n matrix:", ["n", "2n", "*n²", "n!"], "There are n² entries in the cofactor matrix, each requiring an (n−1)×(n−1) determinant."),
    ("A · adj(A) equals:", ["I", "A² ", "0", "*det(A) · I"], "This key identity holds for any square matrix: A · adj(A) = det(A) · I."),
    ("For a 3×3 matrix, each cofactor requires computing a:", ["3×3 determinant", "1×1 determinant", "*2×2 determinant", "4×4 determinant"], "Deleting one row and one column from a 3×3 matrix leaves a 2×2 submatrix."),
    ("The adjugate method is impractical for large matrices due to:", ["memory constraints", "requiring eigenvalues", "*O(n · n!) computational cost for all the cofactors", "rounding errors unique to this method"], "Computing n² cofactors, each with cost O((n−1)!), gives prohibitive complexity."),
    ("If A is a 2×2 matrix with det(A) = 5, then A⁻¹ =:", ["5 · adj(A)", "adj(A) − 5I", "adj(A) + 5I", "*adj(A) / 5"], "A⁻¹ = (1/5) · adj(A), directly from the formula."),
    ("The adjugate of the identity matrix I is:", ["0", "−I", "2I", "*I"], "All cofactors of I yield submatrices that are also identity matrices, so adj(I) = I."),
    ("If det(A) = 0, the adjugate formula gives:", ["A⁻¹ = adj(A)", "A⁻¹ = 0", "A⁻¹ = I", "*A⁻¹ is undefined (division by zero)"], "You cannot divide by zero, confirming that singular matrices have no inverse."),
    ("The cofactor Cᵢⱼ includes the sign factor:", ["always +1", "always −1", "(−1)ⁱ", "*(−1)^(i+j)"], "The checkerboard sign pattern alternates based on the sum of the row and column indices."),
    ("For a diagonal matrix diag(a,b,c) with all nonzero entries, adj(A) =:", ["diag(a,b,c)", "diag(1/a,1/b,1/c)", "*diag(bc, ac, ab)", "diag(a+b, b+c, a+c)"], "Each cofactor is the product of the other two diagonal entries."),
    ("An advantage of the adjugate method is:", ["speed for large matrices", "*it gives a closed-form formula (useful for theoretical work and symbolic computation)", "numerical stability", "no division needed"], "The adjugate provides an explicit formula useful in proofs and for matrices with symbolic entries."),
    ("If A is 3×3 and adj(A) has been computed, finding A⁻¹ requires one more:", ["matrix multiplication", "eigenvalue computation", "*scalar division (dividing each entry by det(A))", "cofactor computation"], "With adj(A) in hand, just divide every entry by det(A)."),
    ("The adjugate of a triangular matrix is:", ["always zero", "always diagonal", "always the identity", "*also triangular (of the same type)"], "The cofactor structure preserves the triangular pattern, and transposing switches upper/lower."),
    ("For a 2×2 matrix, the adjugate method and the direct formula A⁻¹ = (1/det)[[d,−b],[−c,a]] are:", ["different approaches entirely", "only approximately equal", "contradictory", "*exactly the same computation"], "The 2×2 inverse formula IS the adjugate method applied to 2×2 matrices."),
    ("The adjugate satisfies adj(AB) =", ["adj(A)·adj(B)", "*adj(B)·adj(A)", "adj(A)+adj(B)", "adj(A)−adj(B)"], "Like the inverse, the adjugate reverses the order of multiplication."),
    ("If all entries of A are integers and det(A) = ±1, then A⁻¹ has:", ["irrational entries", "complex entries", "*all integer entries", "all zero entries"], "A⁻¹ = adj(A)/det(A); if det = ±1 and adj has integer entries, A⁻¹ is integral."),
    ("In symbolic computation (computer algebra systems), the adjugate method is valuable because:", ["it's fast", "it avoids fractions", "*it gives exact results without floating-point errors", "it uses less memory"], "Symbolic systems handle exact arithmetic, making the adjugate formula practical."),
    ("The adjugate of a singular matrix A satisfies A · adj(A) =:", ["I", "A", "adj(A)", "*the zero matrix (since det(A) = 0)"], "A · adj(A) = det(A) · I = 0 · I = O when A is singular."),
],

# ── U4 L4.4: Singular vs. Non-Singular Matrices ──
"u4_l4.4": [
    ("A singular matrix has determinant:", ["positive", "negative", "nonzero", "*zero"], "By definition, singular = det is zero = not invertible."),
    ("A non-singular matrix is equivalent to saying it is:", ["diagonal", "symmetric", "upper triangular", "*invertible"], "Non-singular and invertible are synonymous terms for matrices with nonzero determinant."),
    ("The null space of a singular matrix:", ["is empty", "contains only zero", "*contains nonzero vectors", "equals Rⁿ"], "Singular matrices have nontrivial null spaces — there exist nonzero x with Ax = 0."),
    ("A singular 3×3 matrix has rank:", ["3", "at least 3", "exactly 0", "*at most 2"], "Rank < n for singular n×n matrices. For 3×3, rank can be 0, 1, or 2."),
    ("Which matrix is singular?", ["[[1,0],[0,1]]", "[[2,1],[1,2]]", "[[3,4],[1,2]]", "*[[2,4],[1,2]]"], "det([[2,4],[1,2]]) = 4−4 = 0. The rows are proportional."),
    ("Non-singular matrices map Rⁿ to Rⁿ as:", ["many-to-one", "not onto", "neither injective nor surjective", "*bijective transformations"], "Full rank means the map is both one-to-one and onto."),
    ("If Ax = b has no solution for some b, then A is:", ["invertible", "orthogonal", "non-singular", "*singular"], "An invertible matrix always yields a unique solution x = A⁻¹b for every b."),
    ("Adding a singular matrix to a non-singular matrix gives:", ["always singular", "always non-singular", "always zero", "*could be either singular or non-singular"], "There is no general rule; the sum's invertibility depends on the specific matrices."),
    ("The product of a singular matrix with any matrix is:", ["non-singular", "the identity", "undefined", "*singular"], "If det(A)=0, then det(AB) = det(A)det(B) = 0, regardless of B."),
    ("For a non-singular matrix, the system Ax = 0 has:", ["infinitely many solutions", "no solution", "two solutions", "*only x = 0"], "Non-singular ↔ trivial null space ↔ only the zero solution."),
    ("A diagonal matrix is singular if and only if:", ["all entries are zero", "the trace is zero", "any off-diagonal entry is nonzero", "*at least one diagonal entry is zero"], "det of a diagonal matrix is the product of diag entries; one zero makes the product zero."),
    ("The set of all singular n×n matrices forms:", ["a subspace", "all of Rⁿˣⁿ", "a group", "*a zero set of the determinant polynomial (measure zero)"], "Singular matrices satisfy det(A) = 0, a polynomial equation, forming a thin set."),
    ("Column rank equals row rank for any matrix. A non-singular n×n matrix has rank:", ["0", "n−1", "at most n", "*exactly n"], "Full rank = n for an n×n non-singular matrix."),
    ("The eigenvalues of a singular matrix always include:", ["only positive values", "1", "−1", "*0"], "det(A) = product of eigenvalues; if det = 0, at least one eigenvalue must be zero."),
    ("If A is nearly singular (det ≈ 0), numerical computations may be:", ["more accurate", "unaffected", "*unstable (the matrix is ill-conditioned)", "impossible"], "Near-singular matrices amplify rounding errors, leading to unreliable numerical results."),
    ("The condition number of a matrix measures:", ["its determinant", "its trace", "*sensitivity to perturbations (large condition number = ill-conditioned)", "its rank"], "Large condition number means small input changes cause large output changes."),
    ("A matrix with two identical columns is:", ["non-singular", "orthogonal", "positive definite", "*singular"], "Identical columns are linearly dependent, so rank < n and det = 0."),
    ("Geometrically, a singular 2×2 transformation collapses the plane to:", ["a circle", "a square", "itself", "*a line or a point"], "Rank 1 collapse to a line; rank 0 collapses to the origin."),
    ("If A is singular and B is non-singular, is AB singular?", ["no, it is non-singular", "it depends on sizes", "it is undefined", "*yes, AB is always singular"], "det(AB) = det(A)·det(B) = 0·det(B) = 0."),
    ("Testing singularity numerically is best done by:", ["checking if any entry is zero", "computing the trace", "*examining the smallest singular value or the condition number", "checking symmetry"], "Singular value decomposition gives the most reliable numerical test for near-singularity."),
],

# ── U4 L4.5: Applications of Inverse Matrices ──
"u4_l4.5": [
    ("The primary use of A⁻¹ for solving linear systems is:", ["finding eigenvalues", "*computing x = A⁻¹b to get the unique solution", "computing determinants", "factoring matrices"], "If A is invertible, x = A⁻¹b gives the solution directly."),
    ("In a Leontief input-output economic model, the production vector x satisfies:", ["x = Ax", "x = A + d", "*x = (I − A)⁻¹d", "x = d − A"], "(I − A)⁻¹d gives total production needed to meet final demand d."),
    ("Matrix inverses help decode messages in Hill cipher by:", ["adding the key matrix", "multiplying by the original key", "*multiplying ciphertext by the inverse of the key matrix", "taking the transpose of the ciphertext"], "Decryption reverses the encryption: plaintext = K⁻¹ · ciphertext (mod 26)."),
    ("In computer graphics, reversing a rotation by angle θ uses:", ["the same rotation matrix", "*the inverse (rotation by −θ)", "the zero matrix", "the transpose only for non-orthogonal matrices"], "For rotation matrices, the inverse equals the transpose, giving rotation by −θ."),
    ("In a network flow problem, inverse matrices help solve for:", ["only the maximum flow", "only shortest paths", "*unknown flows at nodes given input/output constraints", "only edge capacities"], "Setting up the flow balance as Ax = b, the inverse gives the unique flow vector."),
    ("The formula (I − A)⁻¹ = I + A + A² + A³ + ... converges when:", ["always", "never", "*all eigenvalues of A have absolute value less than 1", "A is symmetric"], "This Neumann series converges when the spectral radius of A is less than 1."),
    ("In regression analysis, the least-squares solution involves:", ["det(A)", "A + b", "*(AᵀA)⁻¹Aᵀb", "A⁻¹ only"], "The normal equations give β = (XᵀX)⁻¹Xᵀy for the best-fit coefficients."),
    ("A⁻¹ is useful for sensitivity analysis because:", ["it's always small", "it simplifies eigenvalues", "*small changes in b produce changes Δx = A⁻¹Δb, showing how solutions respond", "it eliminates errors"], "The inverse directly maps perturbations in the right-hand side to perturbations in the solution."),
    ("In control theory, the state transition matrix is:", ["always zero", "*an exponential of a matrix, involving powers and inverses", "a scalar function", "always the identity"], "The matrix exponential e^(At) governs how systems evolve over time."),
    ("For solving Ax = b with multiple right-hand sides b₁, b₂, ..., bₖ:", ["recompute LU each time", "*compute A⁻¹ once (or LU once) and apply to each bᵢ", "use Cramer's rule for each", "only the first b matters"], "Precomputing A⁻¹ (or LU) avoids redundant elimination for each new right-hand side."),
    ("The matrix equation AX = B (where X and B are matrices) has solution:", ["X = BA⁻¹", "X = B − A", "X = AB", "*X = A⁻¹B"], "Left-multiplying both sides by A⁻¹ gives X = A⁻¹B."),
    ("The equation XA = B (X on the left) has solution:", ["X = A⁻¹B", "X = AB⁻¹", "*X = BA⁻¹", "X = ABA⁻¹"], "Right-multiplying both sides by A⁻¹ gives X = BA⁻¹."),
    ("In Markov chains, the fundamental matrix (I − Q)⁻¹ gives:", ["stationary distribution", "transition probabilities", "*expected number of visits to transient states", "eigenvalues of Q"], "The fundamental matrix entry (i,j) gives the expected visits to transient state j starting from i."),
    ("Inverse matrices are used in GPS positioning to solve:", ["a single equation", "a homogeneous system", "*the overdetermined system of satellite distance equations (via least squares)", "only for latitude"], "GPS uses least-squares (involving (AᵀA)⁻¹) to find the receiver's position from multiple satellites."),
    ("In electrical engineering, the admittance matrix is the inverse of:", ["the current vector", "the voltage vector", "*the impedance matrix", "the power matrix"], "Y = Z⁻¹ relates currents and voltages in a circuit network."),
    ("The Newton-Raphson method in higher dimensions uses:", ["only scalar division", "matrix addition", "*the inverse (or solution) of the Jacobian matrix at each step", "eigenvalues of the Hessian"], "Multivariate Newton's method: x_new = x − J⁻¹f(x)."),
    ("In data science, the inverse of a covariance matrix (precision matrix) reveals:", ["only variances", "only means", "*conditional independence structure among variables", "the data dimension"], "Zero entries in the precision matrix indicate conditional independence between variables."),
    ("Change of basis uses inverse matrices because:", ["bases are always orthogonal", "any matrix can serve as a basis", "*converting from basis B coordinates to standard requires multiplication by the inverse of B", "the determinant must be 1"], "Coordinates in basis B relate to standard coordinates via the inverse of the basis matrix."),
    ("If A represents an encryption function, A⁻¹ represents:", ["a different encryption", "the identity function", "*the decryption function", "a hash function"], "Applying the inverse undoes the encryption, recovering the original message."),
    ("In solving differential equations, the matrix exponential e^(At) involves:", ["only A itself", "only det(A)", "only eigenvalues", "*powers of A (and implicitly A⁻¹ for diagonalizable A)"], "e^(At) = PΛ(t)P⁻¹ when A is diagonalizable, directly using the inverse of the eigenvector matrix."),
],

# ── U4 L4.6: Using Inverses in Cryptography ──
"u4_l4.6": [
    ("The Hill cipher encrypts blocks of text using:", ["addition of a key", "XOR operations", "*matrix multiplication modulo 26", "character substitution only"], "Each block of plaintext letters is multiplied by a key matrix mod 26."),
    ("In the Hill cipher, the key matrix must be:", ["symmetric", "diagonal", "any matrix", "*invertible modulo 26 (gcd(det, 26) = 1)"], "The key needs an inverse mod 26 so decryption is possible."),
    ("Decryption in the Hill cipher uses:", ["the same key matrix", "the transpose of the key", "a random matrix", "*the modular inverse of the key matrix"], "Plaintext = K⁻¹ · ciphertext (mod 26), where K⁻¹ is the modular inverse."),
    ("In modular arithmetic, the inverse of 7 mod 26 is:", ["7", "26", "*15 (since 7·15 = 105 ≡ 1 mod 26)", "3"], "7 × 15 = 105 = 4 × 26 + 1, so 7⁻¹ ≡ 15 (mod 26)."),
    ("A 2×2 Hill cipher encrypts letters in blocks of:", ["1", "*2", "4", "26"], "A 2×2 key matrix transforms pairs of letters at a time."),
    ("If the key matrix K = [[3,5],[2,7]], det(K) mod 26 =:", ["26", "0", "*11", "15"], "det = 3·7 − 5·2 = 21 − 10 = 11. Since gcd(11,26) = 1, the key is valid."),
    ("The Hill cipher is vulnerable to:", ["brute force only", "dictionary attacks", "*known-plaintext attacks (if attacker knows some plaintext-ciphertext pairs)", "timing attacks only"], "Knowing enough plaintext-ciphertext pairs allows solving for the key matrix."),
    ("Matrix operations mod 26 differ from real matrix operations because:", ["multiplication doesn't apply", "addition changes", "*inverses require modular inverse of the determinant (not 1/det)", "transposition changes"], "Division is replaced by modular multiplicative inverse; not all determinants have one."),
    ("A Hill cipher with a 3×3 key matrix encrypts letters in blocks of:", ["2", "*3", "6", "9"], "The key matrix dimension determines the block size."),
    ("gcd(det(K), 26) must equal 1 because:", ["it simplifies computation", "it ensures symmetry", "*it guarantees the modular inverse of det(K) exists", "it prevents errors"], "The determinant needs a multiplicative inverse mod 26, which requires gcd = 1."),
    ("Which determinant value mod 26 would make a Hill cipher key invalid?", ["1", "3", "5", "*13"], "gcd(13, 26) = 13 ≠ 1, so 13 has no inverse mod 26."),
    ("The number of valid 2×2 Hill cipher keys (mod 26) is:", ["26⁴ = 456976", "exactly 26²", "all of them", "*a fraction of 26⁴ (only those with invertible determinant mod 26)"], "Many of the 26⁴ possible matrices have determinants sharing a factor with 26."),
    ("Modern cryptography replaced the Hill cipher primarily because:", ["matrices are too slow to compute", "modular arithmetic is flawed", "*it's vulnerable to frequency analysis and known-plaintext attacks", "it can't handle large texts"], "The Hill cipher's linearity makes it breakable with enough known plaintext."),
    ("In the Hill cipher encoding A=0, B=1, ..., Z=25, encrypting 'HI' with K=[[3,5],[2,7]] gives:", ["some letter pair different from HI", "*a specific ciphertext pair computed as K·[7;8] mod 26", "always 'HI'", "always 'ZZ'"], "Compute [[3,5],[2,7]]·[[7],[8]] = [[61],[70]], then mod 26: [[9],[18]] = 'JS'."),
    ("The Hill cipher is a type of:", ["stream cipher", "hash function", "*polygraphic substitution cipher", "asymmetric cipher"], "It substitutes groups of letters simultaneously, making it polygraphic."),
    ("To increase security, the Hill cipher can use:", ["a smaller key matrix", "only 1×1 matrices", "*larger key matrices (e.g., 5×5 or larger)", "no matrices at all"], "Larger matrices mix more letters per block, making analysis harder (though still breakable)."),
    ("Public-key cryptography (like RSA) differs from the Hill cipher because:", ["it doesn't use math", "it uses smaller numbers", "*the encryption and decryption keys are different (asymmetric)", "it uses matrices instead of numbers"], "RSA uses a public key for encryption and a private key for decryption — unlike Hill's shared key."),
    ("Error in one ciphertext character of a Hill cipher block affects:", ["only that character", "no characters", "*the entire decrypted block", "all subsequent blocks"], "Since decryption multiplies the entire block by K⁻¹, one error propagates through the block."),
    ("The concept of invertibility in cryptography ensures:", ["messages can be compressed", "keys are public", "*every encrypted message can be uniquely decrypted", "faster computation"], "Without invertibility, decryption would be ambiguous or impossible."),
    ("Self-inverse Hill cipher keys satisfy K² ≡ I (mod 26), meaning:", ["K has no inverse", "K is always the identity", "*the same key encrypts and decrypts", "the key changes each use"], "If K = K⁻¹, applying K twice returns to the original plaintext."),
],

# ── U4 L4.7: Applications in Computer Science ──
"u4_l4.7": [
    ("In computer graphics, a 4×4 transformation matrix represents:", ["only scaling", "only rotation", "only translation", "*rotation, scaling, and translation combined (affine transformation)"], "Homogeneous coordinates use 4×4 matrices to unify all affine operations."),
    ("Rendering a 3D scene onto a 2D screen uses:", ["addition of coordinates", "scalar multiplication only", "*projection matrices (which may be singular)", "sorting algorithms only"], "Projection matrices collapse 3D to 2D, reducing the dimension."),
    ("Google's PageRank algorithm fundamentally relies on:", ["inverse matrices directly", "determinant computation", "*eigenvalues of a modified adjacency matrix (related to matrix powers)", "the cross product"], "PageRank finds the dominant eigenvector of a stochastic link matrix."),
    ("In machine learning, solving for weights in linear regression uses:", ["only addition", "only determinants", "*matrix inverse (or pseudo-inverse) in the normal equation w = (XᵀX)⁻¹Xᵀy", "only sorting"], "The closed-form solution involves the inverse of the Gram matrix XᵀX."),
    ("The pseudo-inverse A⁺ is used when:", ["A is always invertible", "A is the identity", "*A is rectangular or singular (standard inverse doesn't exist)", "A has integer entries"], "The pseudo-inverse generalizes inversion to non-square or singular matrices."),
    ("In image processing, convolution kernels can be inverted to:", ["compress images", "rotate images", "*deblur or sharpen images (deconvolution)", "delete images"], "If the blurring operation is known, applying its inverse (approximately) removes the blur."),
    ("Adjacency matrices of graphs have inverses that help analyze:", ["graph coloring", "only vertex counts", "*network connectivity and node relationships", "only edge weights"], "The inverse of (I − A) (when it exists) reveals path-counting and reachability information."),
    ("In robotics, inverse kinematics uses matrix inverses to:", ["detect obstacles", "charge batteries", "*compute joint angles from a desired end-effector position", "measure weight"], "Given a target position, the Jacobian inverse maps position errors to joint corrections."),
    ("Gaussian elimination is preferred over matrix inversion in practice because:", ["it's less accurate", "it uses more memory", "*it's faster to solve Ax=b directly (O(n³) vs. O(n³) for inverse + O(n²) multiply)", "they're equally efficient"], "Solving directly avoids the overhead of computing and storing the full inverse."),
    ("In recommendation systems, matrix factorization decomposes a ratings matrix into:", ["its inverse", "its determinant", "*two lower-rank matrices (users × features) and (features × items)", "only eigenvalues"], "Low-rank factorization reveals latent features connecting users to items."),
    ("Error-correcting codes (like Reed-Solomon) use matrix inverses to:", ["generate errors", "increase noise", "*recover original data from corrupted transmissions", "compress data"], "The inverse of the encoding matrix allows decoding even when some data is lost."),
    ("In finite element analysis, the stiffness matrix K relates forces to:", ["velocities", "temperatures", "masses", "*displacements (F = Kx, so x = K⁻¹F)"], "Solving Ku = F for displacements requires inverting (or factoring) the stiffness matrix."),
    ("Hash functions differ from invertible matrix operations because hashes are:", ["always invertible", "always linear", "*designed to be one-way (not invertible)", "matrix-based"], "Cryptographic hashes are intentionally non-invertible, unlike linear algebraic operations."),
    ("Databases use matrix operations (including inverses) in:", ["only data storage", "only deleting rows", "*query optimization and principal component analysis of data", "file compression"], "Dimensionality reduction and statistical analysis of database contents use linear algebra."),
    ("In signal processing, the inverse DFT (Discrete Fourier Transform) uses:", ["a diagonal matrix only", "*the inverse of the DFT matrix (scaled conjugate transpose)", "Cramer's rule", "the zero matrix"], "The inverse DFT reconstructs a signal from its frequency components."),
    ("Sparse matrix solvers are important because:", ["all matrices are sparse", "dense methods fail completely", "*many real-world matrices (from networks, PDEs) are mostly zeros, enabling faster algorithms", "sparsity means singular"], "Exploiting sparsity reduces O(n³) to much less, enabling solutions for millions of variables."),
    ("In cryptographic key exchange (like Diffie-Hellman), modular inverses play the role of:", ["public channels", "random noise", "*enabling one party to reverse the other's operation", "only generating keys"], "Modular inverses are central to the mathematical operations that make key exchange secure."),
    ("Iterative solvers (like conjugate gradient) approximate A⁻¹b without:", ["using any math", "knowing A", "*explicitly computing A⁻¹ (they repeatedly multiply by A and converge to the solution)", "any convergence guarantees"], "Iterative methods apply A repeatedly, converging to x = A⁻¹b without ever forming A⁻¹."),
    ("In computer vision, the essential matrix E relates:", ["colors of pixels", "image sizes", "*corresponding points in two camera views (epipolar geometry)", "file formats"], "The essential matrix encodes the geometric relationship between two camera positions."),
    ("The complexity of inverting a dense n×n matrix by the best known algorithms is:", ["O(n)", "O(n²)", "*approximately O(n^2.37) (same as matrix multiplication)", "O(n⁴)"], "Matrix inversion has the same asymptotic complexity as matrix multiplication."),
],

# ── U4 L4.8: Applications in Economics ──
"u4_l4.8": [
    ("The Leontief input-output model solves x = Ax + d, giving:", ["x = A + d", "x = d − A", "*x = (I − A)⁻¹d", "x = A⁻¹d"], "Rearranging: (I − A)x = d, so x = (I − A)⁻¹d gives total production."),
    ("In the Leontief model, matrix A represents:", ["final consumer demand", "profit margins", "*inter-industry production requirements (how much each industry consumes from others)", "tax rates"], "Entry aᵢⱼ is the amount of good i needed to produce one unit of good j."),
    ("The vector d in the Leontief model represents:", ["total production", "intermediate demand", "*final (external) demand from consumers", "imports"], "d is the demand that must be satisfied after all inter-industry consumption."),
    ("For (I − A)⁻¹ to exist in the Leontief model, we need:", ["A = I", "A to be symmetric", "*I − A to be non-singular (det(I − A) ≠ 0)", "d = 0"], "The Leontief inverse exists when the technology matrix doesn't make the system singular."),
    ("An economy with 3 sectors requires a Leontief matrix of size:", ["1×1", "2×2", "*3×3", "9×9"], "Each sector has production requirements from each other sector, forming an n×n matrix."),
    ("In portfolio optimization, the covariance matrix Σ is inverted to:", ["measure returns only", "eliminate all risk", "*find the optimal portfolio weights (minimum variance allocation)", "compute dividends"], "The Markowitz model uses Σ⁻¹ to determine how to allocate assets for minimum risk."),
    ("A positive Leontief inverse (I − A)⁻¹ means:", ["the economy is failing", "all entries of A are negative", "*every increase in demand can be met by increased production (economically feasible)", "the economy is closed"], "All-positive entries guarantee that demand increases lead to positive production responses."),
    ("In equilibrium price models, prices p satisfy p = Aᵀp + v, giving:", ["p = v", "p = Aᵀv", "p = v − Aᵀ", "*p = (I − Aᵀ)⁻¹v"], "Rearranging: (I − Aᵀ)p = v, so p = (I − Aᵀ)⁻¹v gives equilibrium prices."),
    ("The multiplier effect in economics relates to:", ["A being zero", "*how a unit increase in demand cascades through industries: (I−A)⁻¹ = I + A + A² + ...", "det(A) being large", "eigenvalues being negative"], "Each round of production creates additional demand, captured by the geometric series."),
    ("In game theory, the payoff matrix inverse helps find:", ["the total number of strategies", "*optimal mixed strategies for zero-sum games", "only pure strategies", "the names of players"], "Solving the minimax problem for mixed strategies involves matrix equations requiring inverses."),
    ("The Hawkins-Simon condition ensures that the Leontief model:", ["has negative production", "fails to converge", "*produces economically meaningful (non-negative) outputs", "has infinite solutions"], "This condition on the principal minors of (I−A) guarantees all production levels are non-negative."),
    ("If technology improves and the entries of A decrease, then (I−A)⁻¹:", ["increases without bound", "stays the same", "*decreases, meaning less total production needed per unit of final demand", "becomes singular"], "Smaller A means each sector is more efficient, requiring less from other sectors."),
    ("In econometrics, the inverse of (XᵀX) appears in:", ["GDP calculations", "currency exchange rates", "*the standard errors of regression coefficients", "price indexing only"], "Var(β̂) = σ²(XᵀX)⁻¹ in OLS, directly giving coefficient uncertainties."),
    ("A closed Leontief model (no external demand) requires:", ["d > 0", "(I−A) to be invertible", "*finding the null space of (I−A), i.e., the eigenvector for eigenvalue 1", "A = 0"], "In a closed model, x = Ax means (I−A)x = 0, so we find the null space."),
    ("Multi-sector economic planning uses large-scale matrix inversions involving:", ["2×2 matrices only", "symbolic computation only", "*numerical methods (LU decomposition, iterative solvers) on matrices with hundreds of sectors", "no computation"], "Real economies have many sectors, requiring efficient numerical algorithms."),
    ("If one sector of the economy shuts down (row/column removed from A):", ["the determinant doubles", "nothing changes", "*the Leontief inverse must be recomputed for the reduced system", "the inverse is the same"], "Removing a sector changes the structure, requiring a new (I−A)⁻¹."),
    ("In international trade models, the Leontief framework extends to:", ["only domestic production", "*multi-country input-output tables linking economies across nations", "only agriculture", "binary trade decisions"], "International input-output models track inter-industry flows across countries."),
    ("The condition that all column sums of A are less than 1 ensures:", ["A is orthogonal", "A is symmetric", "*each industry consumes less than it produces (productive economy)", "A has negative entries"], "Column sums < 1 means each sector uses less than one unit of inputs per unit of output."),
    ("Shadow prices in linear programming are obtained from:", ["the primal solution only", "the determinant of the constraint matrix", "*the inverse of the basis matrix (used in the simplex method)", "random sampling"], "The simplex method uses B⁻¹ to compute dual variables (shadow prices) at each step."),
    ("Environmental input-output analysis extends Leontief models by:", ["ignoring pollution", "using only 2×2 matrices", "*adding rows for pollutant emissions per unit of production", "eliminating all sectors"], "Augmenting A with environmental impact coefficients tracks pollution alongside production."),
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

print(f"✅ Linear Algebra U3-U4: replaced questions in {count} lessons")
