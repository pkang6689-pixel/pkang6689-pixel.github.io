#!/usr/bin/env python3
"""Replace placeholder questions for Linear Algebra U1-U2 with real, high-quality questions."""
import json, os

PATH = os.path.join(os.path.dirname(__file__), "content_data", "linear_algebra_lessons.json")

def build_q(num, text, options, explanation):
    """Build a question dict. Options: list of (text, is_correct) tuples."""
    return {
        "question_number": num,
        "question_text": text,
        "attempted": 2,
        "data_i18n": None,
        "options": [{"text": t, "is_correct": c, "data_i18n": None} for t, c in options],
        "explanation": explanation
    }

LESSONS = {
# ───────────────────────────────────────────────
# U1 L1.1  Scalars, Vectors, and Matrices
# ───────────────────────────────────────────────
"u1_l1.1": [
    ("A scalar is best described as:", [("A single numerical value", True), ("An ordered list of numbers", False), ("A rectangular array of numbers", False), ("A function of two variables", False)], "A scalar is just one number — no direction or arrangement, unlike vectors or matrices."),
    ("Which of the following is a vector?", [("7", False), ("[3, −1, 4]", True), ("[[1, 2], [3, 4]]", False), ("π", False)], "A vector is an ordered list of numbers. A single number is a scalar; a rectangular grid is a matrix."),
    ("A matrix differs from a vector because it has:", [("only one column", False), ("both rows and columns", True), ("no numerical entries", False), ("exactly three components", False)], "Vectors are one-dimensional (a single row or column), while matrices are two-dimensional with rows and columns."),
    ("The entry in row 2, column 3 of a matrix is denoted:", [("a₃₂", False), ("a₂₃", True), ("a₂₂", False), ("a₃₃", False)], "Standard notation uses the row index first, then the column index: aᵢⱼ where i = row, j = column."),
    ("How many entries does a 3×4 matrix contain?", [("7", False), ("12", True), ("34", False), ("4", False)], "A matrix with m rows and n columns has m × n entries. Here 3 × 4 = 12."),
    ("If v = [2, 5], what kind of object is v?", [("a 2×2 matrix", False), ("a scalar", False), ("a 2-dimensional vector", True), ("an undefined expression", False)], "An ordered pair of numbers forms a 2D vector, representing a point or direction in two-dimensional space."),
    ("Which statement about scalars is FALSE?", [("Scalars can be negative", False), ("Scalars have magnitude only", False), ("Scalars have direction", True), ("5 is a scalar", False)], "Scalars have magnitude but no direction. Quantities with both magnitude and direction are vectors."),
    ("A column vector with 5 entries can be viewed as a matrix of size:", [("1×5", False), ("5×1", True), ("5×5", False), ("1×1", False)], "A column vector with n entries is an n×1 matrix — n rows and 1 column."),
    ("A row vector with 4 entries has dimensions:", [("4×1", False), ("1×4", True), ("4×4", False), ("2×2", False)], "A row vector is a 1×n matrix — one row and n columns."),
    ("In physics, velocity is represented as a vector because it has:", [("only speed", False), ("both speed and direction", True), ("only direction", False), ("no measurable quantity", False)], "Velocity combines magnitude (speed) and direction, making it a vector quantity."),
    ("The zero vector in ℝ³ is:", [("[1, 1, 1]", False), ("[0, 0, 0]", True), ("[0, 1, 0]", False), ("0", False)], "The zero vector has all components equal to zero. In ℝ³ it has three zero entries; 0 alone is a scalar."),
    ("What is the difference between [3] and the scalar 3?", [("[3] is larger", False), ("[3] is a 1×1 matrix (or 1D vector); 3 is a scalar", True), ("There is no difference", False), ("[3] is undefined", False)], "Although they hold the same number, [3] is a 1-element vector (or 1×1 matrix) while 3 is a plain scalar. Context matters."),
    ("Which real-world quantity is best modeled as a scalar?", [("Wind velocity", False), ("Temperature at a point", True), ("Gravitational force", False), ("Displacement of a car", False)], "Temperature has magnitude only (e.g., 25°C) with no direction, making it a scalar."),
    ("A 1×1 matrix [[7]] behaves most like:", [("a vector", False), ("a scalar", True), ("a 2×2 matrix", False), ("an undefined object", False)], "A 1×1 matrix contains a single entry and in most operations behaves identically to a scalar."),
    ("The number of rows in a matrix is called its:", [("rank", False), ("row dimension", True), ("determinant", False), ("column space", False)], "The row dimension counts how many rows the matrix has. Rank and determinant are different concepts."),
    ("Which is a valid 2×3 matrix?", [("[[1,2],[3,4],[5,6]]", False), ("[[1,2,3],[4,5,6]]", True), ("[[1,2],[3,4]]", False), ("[1,2,3]", False)], "A 2×3 matrix has 2 rows and 3 columns, so each of the 2 rows must have 3 entries."),
    ("Vectors in ℝⁿ have exactly:", [("n² components", False), ("n components", True), ("2n components", False), ("n+1 components", False)], "A vector in ℝⁿ is an ordered list of exactly n real numbers."),
    ("If A is a matrix and c is a scalar, the product cA:", [("is undefined", False), ("multiplies every entry of A by c", True), ("adds c to every entry of A", False), ("changes the dimensions of A", False)], "Scalar multiplication scales each entry of the matrix by the scalar, leaving dimensions unchanged."),
    ("The main diagonal of a square matrix runs:", [("across the bottom row", False), ("from top-left to bottom-right", True), ("from top-right to bottom-left", False), ("along the first column", False)], "The main diagonal consists of entries aᵢᵢ, running from the upper-left corner to the lower-right."),
    ("Two matrices are equal when:", [("they have the same dimensions", False), ("they have the same trace", False), ("they have the same dimensions AND every corresponding entry matches", True), ("their determinants are equal", False)], "Matrix equality requires both identical dimensions and identical entries in every position."),
],

# ───────────────────────────────────────────────
# U1 L1.2  Matrix Notation & Dimensions
# ───────────────────────────────────────────────
"u1_l1.2": [
    ("Matrix A has dimensions 4×6. How many columns does it have?", [("4", False), ("6", True), ("24", False), ("10", False)], "In m×n notation, m is the number of rows and n is the number of columns. So 4×6 means 6 columns."),
    ("The notation aᵢⱼ refers to the entry in:", [("column i, row j", False), ("row i, column j", True), ("row j, column i", False), ("diagonal position i+j", False)], "By convention, the first subscript is the row and the second is the column."),
    ("If B is 3×3, how many entries lie on its main diagonal?", [("6", False), ("9", False), ("3", True), ("1", False)], "A square n×n matrix has exactly n entries on the main diagonal: b₁₁, b₂₂, …, bₙₙ."),
    ("A matrix with more rows than columns is called:", [("wide", False), ("tall (or overdetermined when in a system)", True), ("square", False), ("singular", False)], "When m > n the matrix has more rows than columns, making it taller than it is wide."),
    ("Which dimensions make a square matrix?", [("2×5", False), ("5×2", False), ("5×5", True), ("1×5", False)], "A matrix is square when the number of rows equals the number of columns: n×n."),
    ("The trace of a matrix is the sum of:", [("all entries", False), ("the first row", False), ("the main diagonal entries", True), ("the last column", False)], "Trace is defined only for square matrices and equals a₁₁ + a₂₂ + … + aₙₙ."),
    ("How many entries does a 5×1 matrix have?", [("5", True), ("1", False), ("6", False), ("25", False)], "5 rows × 1 column = 5 entries total; it is simply a column vector."),
    ("If C is 2×4 and D is 4×3, the product CD has dimensions:", [("2×3", True), ("4×4", False), ("2×4", False), ("3×2", False)], "When multiplying an m×n matrix by an n×p matrix, the result is m×p. Here 2×3."),
    ("Matrix dimensions are always written as:", [("columns × rows", False), ("rows × columns", True), ("entries × diagonals", False), ("rank × trace", False)], "The universal convention is rows × columns (m × n)."),
    ("A matrix with dimensions 1×1 is called:", [("a row vector", False), ("a column vector", False), ("a scalar matrix", True), ("undefined", False)], "A 1×1 matrix holds a single entry and is often treated interchangeably with a scalar."),
    ("The entry a₃₁ is located at:", [("row 1, column 3", False), ("row 3, column 1", True), ("row 3, column 3", False), ("row 1, column 1", False)], "First subscript = row, second subscript = column. So a₃₁ means row 3, column 1."),
    ("Two matrices can be added only if:", [("they are both square", False), ("they have the same dimensions", True), ("their determinants are equal", False), ("one is a scalar", False)], "Matrix addition is defined only when both matrices have the same number of rows and the same number of columns."),
    ("A 3×4 matrix and a 3×4 matrix produce what size when added?", [("6×8", False), ("3×4", True), ("9×16", False), ("4×3", False)], "Addition preserves dimensions. Adding two 3×4 matrices yields another 3×4 matrix."),
    ("The notation Aᵀ stands for:", [("the inverse of A", False), ("the transpose of A", True), ("the determinant of A", False), ("the trace of A", False)], "The superscript T denotes the transpose, which flips rows and columns."),
    ("If A is 3×5, then Aᵀ has dimensions:", [("3×5", False), ("5×5", False), ("5×3", True), ("3×3", False)], "Transposing an m×n matrix swaps rows and columns, giving n×m. So 3×5 becomes 5×3."),
    ("A diagonal matrix has non-zero entries only:", [("in the first row", False), ("on the main diagonal", True), ("in the last column", False), ("above the diagonal", False)], "All entries off the main diagonal are zero in a diagonal matrix."),
    ("An upper triangular matrix has zeros:", [("above the diagonal", False), ("below the main diagonal", True), ("on the diagonal", False), ("everywhere", False)], "In an upper triangular matrix, all entries below the main diagonal are zero."),
    ("The size of a matrix is also called its:", [("rank", False), ("order or dimensions", True), ("determinant", False), ("eigenvalue", False)], "The terms 'order,' 'size,' and 'dimensions' all refer to the m×n shape of a matrix."),
    ("If a matrix has 20 entries arranged in 4 rows, how many columns does it have?", [("4", False), ("5", True), ("20", False), ("80", False)], "Total entries = rows × columns. So columns = 20 / 4 = 5."),
    ("Which is NOT a valid way to describe a 3×2 matrix?", [("3 rows, 2 columns", False), ("6 entries total", False), ("2 rows, 3 columns", True), ("a tall matrix", False)], "A 3×2 matrix has 3 rows and 2 columns, not the other way around."),
],

# ───────────────────────────────────────────────
# U1 L1.3  Vector Operations
# ───────────────────────────────────────────────
"u1_l1.3": [
    ("If u = [2, 3] and v = [1, −4], then u + v =", [("[3, −1]", True), ("[1, 7]", False), ("[2, −12]", False), ("[3, 7]", False)], "Add component-wise: [2+1, 3+(−4)] = [3, −1]."),
    ("Scalar multiplication: 3 · [4, −2] =", [("[12, −6]", True), ("[7, 1]", False), ("[4, −6]", False), ("[12, 6]", False)], "Multiply each component by the scalar: [3·4, 3·(−2)] = [12, −6]."),
    ("The zero vector satisfies v + 0 =", [("0", False), ("v", True), ("−v", False), ("2v", False)], "The zero vector is the additive identity: adding it to any vector returns the original vector."),
    ("If w = [5, −3, 2], then −w =", [("[5, 3, −2]", False), ("[−5, 3, −2]", True), ("[−5, −3, −2]", False), ("[5, −3, 2]", False)], "The additive inverse negates every component: −[5, −3, 2] = [−5, 3, −2]."),
    ("Vector addition is commutative, meaning:", [("u + v = v + u", True), ("u + v = u − v", False), ("u · v = v + u", False), ("u + v = uv", False)], "Commutativity of vector addition says the order doesn't matter: u + v equals v + u."),
    ("u − v is the same as:", [("v − u", False), ("u + (−v)", True), ("−u + v", False), ("u · v", False)], "Subtraction is defined as adding the additive inverse: u − v = u + (−v)."),
    ("If a = [1, 0, 0] and b = [0, 1, 0], then a + b =", [("[0, 0, 1]", False), ("[1, 1, 0]", True), ("[1, 0, 1]", False), ("[1, 1, 1]", False)], "Component-wise addition: [1+0, 0+1, 0+0] = [1, 1, 0]."),
    ("2u + 3u equals:", [("6u", False), ("5u", True), ("u", False), ("23u", False)], "Factor out u: 2u + 3u = (2+3)u = 5u. Scalars add normally."),
    ("Which property does vector addition NOT have?", [("Commutativity", False), ("Associativity", False), ("Distributivity over scalars", False), ("An inherent multiplicative inverse", True)], "Vector addition has commutativity, associativity, and distributes with scalars, but there is no general multiplicative inverse for vectors."),
    ("The magnitude (length) of [3, 4] is:", [("7", False), ("5", True), ("12", False), ("25", False)], "Magnitude = √(3² + 4²) = √(9 + 16) = √25 = 5."),
    ("0 · v (scalar zero times any vector) equals:", [("v", False), ("1", False), ("the zero vector", True), ("undefined", False)], "Multiplying any vector by the scalar 0 produces the zero vector, with all components equal to 0."),
    ("If u = [1, 2] and v = [3, 4], what is 2u − v?", [("[−1, 0]", True), ("[5, 8]", False), ("[1, 0]", False), ("[−1, −2]", False)], "2u = [2, 4], then [2, 4] − [3, 4] = [2−3, 4−4] = [−1, 0]."),
    ("Scalar multiplication by −1 produces:", [("the zero vector", False), ("the same vector", False), ("the vector pointing in the opposite direction", True), ("a perpendicular vector", False)], "Multiplying by −1 reverses the direction of the vector while keeping the same magnitude."),
    ("The parallelogram law describes:", [("how to multiply vectors", False), ("geometric vector addition", True), ("matrix transposition", False), ("scalar division", False)], "Two vectors placed tail-to-tail form a parallelogram; the diagonal is their sum."),
    ("Which operation is NOT defined for two vectors in ℝⁿ?", [("Addition", False), ("Subtraction", False), ("Division", True), ("Scalar multiplication of one by a scalar", False)], "You can add, subtract, and scale vectors, but dividing one vector by another is not a standard operation."),
    ("If v has magnitude 6 and you compute (1/6)v, the result has magnitude:", [("0", False), ("1", True), ("6", False), ("36", False)], "Scaling by 1/‖v‖ produces a unit vector with magnitude 1. This process is called normalization."),
    ("(c₁ + c₂)v = c₁v + c₂v is an example of:", [("commutativity", False), ("scalar distributivity", True), ("the triangle inequality", False), ("Cramer's rule", False)], "Scalar multiplication distributes over scalar addition: (c₁ + c₂)v = c₁v + c₂v."),
    ("If u = [a, b] and v = [c, d], under what condition is u + v = [0, 0]?", [("a = c and b = d", False), ("a = −c and b = −d", True), ("a = 0 and c = 0", False), ("a·c + b·d = 0", False)], "u + v = [a+c, b+d] = [0, 0] requires a = −c and b = −d, making v = −u."),
    ("The triangle inequality states ‖u + v‖ ≤", [("‖u‖ · ‖v‖", False), ("‖u‖ + ‖v‖", True), ("‖u‖ − ‖v‖", False), ("‖u − v‖", False)], "The length of the sum never exceeds the sum of the lengths. Equality holds when u and v point in the same direction."),
    ("Multiplying [2, −1, 3] by the scalar −2 gives:", [("[−4, 2, −6]", True), ("[4, −2, 6]", False), ("[0, −3, 1]", False), ("[−4, −2, −6]", False)], "Multiply each component: [−2·2, −2·(−1), −2·3] = [−4, 2, −6]."),
],

# ───────────────────────────────────────────────
# U1 L1.4  Matrix Operations
# ───────────────────────────────────────────────
"u1_l1.4": [
    ("To add two matrices, they must have:", [("the same determinant", False), ("the same dimensions", True), ("square shapes", False), ("equal traces", False)], "Matrix addition requires both matrices to be the same size so corresponding entries can be paired."),
    ("If A = [[1,2],[3,4]] and B = [[5,6],[7,8]], what is A + B?", [("[[6,8],[10,12]]", True), ("[[5,12],[21,32]]", False), ("[[4,4],[4,4]]", False), ("[[6,8],[7,12]]", False)], "Add entry by entry: 1+5=6, 2+6=8, 3+7=10, 4+8=12."),
    ("Matrix multiplication AB requires:", [("A and B to be the same size", False), ("columns of A = rows of B", True), ("rows of A = rows of B", False), ("both to be square", False)], "For AB to be defined, the number of columns in A must equal the number of rows in B."),
    ("If A is 2×3 and B is 3×2, the product AB is:", [("3×3", False), ("2×2", True), ("2×3", False), ("undefined", False)], "A (2×3) times B (3×2) gives a 2×2 result: outer dimensions determine the product size."),
    ("Is matrix multiplication commutative? (Does AB = BA in general?)", [("Yes, always", False), ("No, generally AB ≠ BA", True), ("Only for square matrices", False), ("Only for diagonal matrices", False)], "Matrix multiplication is not commutative in general. AB and BA can be different sizes or have different entries even when both are defined."),
    ("Each entry of AB is computed by:", [("adding corresponding entries", False), ("multiplying corresponding entries", False), ("taking the dot product of a row of A with a column of B", True), ("taking the determinant of a submatrix", False)], "Entry (i,j) of AB equals the dot product of row i of A and column j of B."),
    ("3 · [[1,0],[−2,4]] equals:", [("[[3,0],[−6,12]]", True), ("[[4,3],[1,7]]", False), ("[[3,0],[−2,4]]", False), ("[[1,0],[−6,12]]", False)], "Scalar multiplication: multiply every entry by 3."),
    ("A(B + C) = AB + AC is called:", [("commutativity", False), ("left distributivity", True), ("the inverse property", False), ("transposition", False)], "Matrix multiplication distributes over addition on the left: A(B+C) = AB + AC."),
    ("If A is 4×2 and B is 2×4, what size is BA?", [("4×4", False), ("2×2", True), ("2×4", False), ("4×2", False)], "B (2×4) times A (4×2) gives 2×2. Note this differs from AB which would be 4×4."),
    ("The product of a 1×3 row vector and a 3×1 column vector is:", [("a 3×3 matrix", False), ("a 1×1 scalar", True), ("a 3×1 vector", False), ("undefined", False)], "A 1×3 times a 3×1 yields a 1×1 result — effectively a single number (the dot product)."),
    ("Matrix addition is commutative: A + B =", [("A − B", False), ("B + A", True), ("AB", False), ("BA", False)], "Unlike multiplication, matrix addition is commutative: the order does not matter."),
    ("Which operation is always defined for any two n×n matrices?", [("Division", False), ("Addition and multiplication", True), ("Only addition", False), ("Neither addition nor multiplication", False)], "For same-size square matrices, both addition and multiplication are always defined."),
    ("If A is 2×3 and B is 2×3, is AB defined?", [("Yes, result is 2×3", False), ("Yes, result is 2×2", False), ("No, columns of A ≠ rows of B", True), ("Yes, result is 3×3", False)], "A has 3 columns but B has 2 rows. Since 3 ≠ 2, the product AB is not defined."),
    ("(AB)C = A(BC) illustrates:", [("commutativity", False), ("distributivity", False), ("associativity of matrix multiplication", True), ("the inverse property", False)], "Matrix multiplication is associative: grouping does not affect the result."),
    ("For the product to be defined, A (m×n) times B (p×q) requires:", [("m = p", False), ("n = p", True), ("m = q", False), ("n = q", False)], "The inner dimensions must match: n (columns of A) must equal p (rows of B)."),
    ("What is [[1,0],[0,1]] · [[a,b],[c,d]]?", [("[[a,b],[c,d]]", True), ("[[1,0],[0,1]]", False), ("[[a+c,b+d],[a+c,b+d]]", False), ("[[0,0],[0,0]]", False)], "The 2×2 identity matrix leaves any 2×2 matrix unchanged when multiplied: I·A = A."),
    ("A − B is equivalent to:", [("A + B", False), ("B − A", False), ("A + (−1)B", True), ("A · B", False)], "Subtraction is the same as adding the scalar multiple (−1)B."),
    ("The outer product of a 3×1 vector and a 1×3 vector produces:", [("a scalar", False), ("a 3×3 matrix", True), ("a 3×1 vector", False), ("a 1×1 matrix", False)], "A 3×1 times a 1×3 gives a 3×3 matrix. This is the outer product, distinct from the dot product."),
    ("If A is square, A² means:", [("each entry squared", False), ("A · A", True), ("A + A", False), ("the transpose of A", False)], "A² = A·A, performing matrix multiplication of A with itself. It does NOT mean squaring each entry."),
    ("k(A + B) equals:", [("kA + B", False), ("A + kB", False), ("kA + kB", True), ("k²AB", False)], "Scalar multiplication distributes: k(A + B) = kA + kB."),
],

# ───────────────────────────────────────────────
# U1 L1.5  Identity & Zero Matrices
# ───────────────────────────────────────────────
"u1_l1.5": [
    ("The identity matrix Iₙ has ones on the _____ and zeros elsewhere.", [("first row", False), ("last column", False), ("main diagonal", True), ("anti-diagonal", False)], "The identity matrix has 1s along the main diagonal and 0s in all other positions."),
    ("For any square matrix A, what is A · I?", [("I", False), ("the zero matrix", False), ("A", True), ("A²", False)], "The identity matrix is the multiplicative identity: AI = IA = A."),
    ("The 3×3 identity matrix I₃ has how many non-zero entries?", [("9", False), ("3", True), ("6", False), ("0", False)], "A 3×3 identity matrix has exactly 3 ones (on the diagonal) and 6 zeros."),
    ("The zero matrix 0 satisfies A + 0 = ", [("0", False), ("I", False), ("A", True), ("−A", False)], "The zero matrix is the additive identity: adding it to any matrix returns the original."),
    ("What is A · 0 (where 0 is the zero matrix of appropriate size)?", [("A", False), ("I", False), ("the zero matrix", True), ("undefined", False)], "Any matrix multiplied by a zero matrix of compatible dimensions yields the zero matrix."),
    ("Is the identity matrix symmetric?", [("No", False), ("Only for 2×2", False), ("Yes, for all sizes", True), ("Only when n is odd", False)], "Iᵀ = I for any size, since the diagonal is unchanged and all off-diagonal entries are already zero."),
    ("If A is 3×3, then I₃ · A − A =", [("I₃", False), ("A", False), ("the 3×3 zero matrix", True), ("2A", False)], "I₃·A = A, so A − A = 0."),
    ("The determinant of any identity matrix is:", [("0", False), ("1", True), ("n (the matrix size)", False), ("undefined", False)], "det(Iₙ) = 1 for every n, since the product of the diagonal entries is 1·1·…·1 = 1."),
    ("A zero matrix of size 2×3 has:", [("2 zeros", False), ("3 zeros", False), ("5 zeros", False), ("6 zeros", True)], "All 2×3 = 6 entries are zero in a 2×3 zero matrix."),
    ("Which is true about the identity matrix?", [("It is only defined for 2×2", False), ("It exists for every positive integer size n", True), ("It has a determinant of 0", False), ("It equals the zero matrix", False)], "For every n ≥ 1, the n×n identity matrix Iₙ is defined with 1s on the diagonal."),
    ("I₂ = [[1,0],[0,1]]. What is I₂²?", [("[[2,0],[0,2]]", False), ("[[1,0],[0,1]]", True), ("[[0,0],[0,0]]", False), ("[[1,1],[1,1]]", False)], "I² = I·I = I. Multiplying the identity by itself returns the identity."),
    ("The trace of I₄ is:", [("0", False), ("1", False), ("4", True), ("16", False)], "Trace = sum of diagonal entries = 1+1+1+1 = 4 for the 4×4 identity."),
    ("If O is the zero matrix, what is O²?", [("I", False), ("O", True), ("undefined", False), ("2O", False)], "O·O = O. A zero matrix multiplied by itself is still the zero matrix."),
    ("Adding the identity to itself gives:", [("I", False), ("2I (all diagonal entries become 2)", True), ("the zero matrix", False), ("an undefined result", False)], "I + I = 2I. This is a diagonal matrix with 2s on the diagonal."),
    ("Which matrix A satisfies A + (−A) = 0?", [("Only the identity", False), ("Only square matrices", False), ("Every matrix (its additive inverse always exists)", True), ("No matrix", False)], "Every matrix has an additive inverse −A, and A + (−A) equals the zero matrix of the same size."),
    ("The n×n zero matrix has rank:", [("n", False), ("1", False), ("0", True), ("n − 1", False)], "The zero matrix has no non-zero rows, so its rank is 0."),
    ("If 5I₃ = [[5,0,0],[0,5,0],[0,0,5]], this matrix is called:", [("the zero matrix", False), ("a scalar matrix", True), ("the identity", False), ("an upper triangular matrix only", False)], "A scalar matrix is a multiple of the identity: cI. It has the scalar c on every diagonal entry."),
    ("I₂ · [[3],[7]] =", [("[[3],[7]]", True), ("[[1,0],[0,1]]", False), ("[[10]]", False), ("[[0],[0]]", False)], "The identity preserves any vector: I₂ · v = v. So the result is the original column vector."),
    ("Which statement is FALSE?", [("A · 0 = 0 for compatible zero matrix", False), ("A · I = A for square A", False), ("0 · A = 0", False), ("I · 0 = I", True)], "I · 0 = 0, not I. Multiplying the identity by the zero matrix gives the zero matrix."),
    ("The zero matrix is the additive identity because:", [("it has determinant 0", False), ("multiplying by it gives zero", False), ("adding it to any same-size matrix leaves that matrix unchanged", True), ("it is square", False)], "The defining property of the additive identity is that A + 0 = A for all A of the same dimensions."),
],

# ───────────────────────────────────────────────
# U1 L1.6  Transpose of a Matrix
# ───────────────────────────────────────────────
"u1_l1.6": [
    ("The transpose of a matrix swaps its:", [("determinant and trace", False), ("rows and columns", True), ("diagonal entries", False), ("eigenvalues", False)], "Transposing a matrix turns each row into a column and vice versa."),
    ("If A is 3×5, then Aᵀ is:", [("3×5", False), ("5×3", True), ("5×5", False), ("3×3", False)], "Transposing an m×n matrix produces an n×m matrix."),
    ("(Aᵀ)ᵀ equals:", [("0", False), ("A⁻¹", False), ("A", True), ("I", False)], "Transposing twice returns the original matrix."),
    ("If A = [[1,2,3],[4,5,6]], what is the first column of Aᵀ?", [("[1, 2, 3]", True), ("[4, 5, 6]", False), ("[1, 4]", False), ("[2, 5]", False)], "The first row of A becomes the first column of Aᵀ: [1, 2, 3]."),
    ("(A + B)ᵀ =", [("Aᵀ − Bᵀ", False), ("Aᵀ + Bᵀ", True), ("AᵀBᵀ", False), ("BᵀAᵀ", False)], "The transpose of a sum is the sum of the transposes."),
    ("(AB)ᵀ =", [("AᵀBᵀ", False), ("BᵀAᵀ", True), ("(BA)ᵀ", False), ("AB", False)], "The transpose of a product reverses the order: (AB)ᵀ = BᵀAᵀ."),
    ("A symmetric matrix satisfies:", [("A = −A", False), ("Aᵀ = −A", False), ("Aᵀ = A", True), ("A² = I", False)], "A matrix is symmetric when it equals its own transpose: aᵢⱼ = aⱼᵢ for all i, j."),
    ("A skew-symmetric matrix satisfies:", [("Aᵀ = A", False), ("Aᵀ = −A", True), ("A = I", False), ("A = 0", False)], "Skew-symmetric means Aᵀ = −A, so the diagonal entries must all be zero."),
    ("The transpose of a scalar (1×1 matrix) is:", [("its negative", False), ("zero", False), ("itself", True), ("undefined", False)], "A 1×1 matrix is its own transpose since there's nothing to swap."),
    ("For a symmetric matrix, the entry in row 2, column 5 equals the entry in:", [("row 2, column 2", False), ("row 5, column 5", False), ("row 5, column 2", True), ("row 1, column 5", False)], "Symmetry means a₂₅ = a₅₂, reflecting entries across the main diagonal."),
    ("(kA)ᵀ = ", [("k(Aᵀ)", True), ("k²Aᵀ", False), ("A(kᵀ)", False), ("Aᵀ/k", False)], "Scalar factors pass through the transpose: (kA)ᵀ = kAᵀ."),
    ("If A is 4×4 and symmetric, how many independent entries does it have?", [("16", False), ("10", True), ("8", False), ("4", False)], "For an n×n symmetric matrix: n diagonal + n(n−1)/2 upper entries = n(n+1)/2 = 4·5/2 = 10."),
    ("The transpose of a column vector is:", [("another column vector", False), ("a row vector", True), ("a scalar", False), ("undefined", False)], "Transposing an n×1 column vector produces a 1×n row vector."),
    ("Which matrix is always symmetric?", [("Any rectangular matrix", False), ("Any upper triangular matrix", False), ("AᵀA for any matrix A", True), ("AB for square A, B", False)], "AᵀA is always symmetric because (AᵀA)ᵀ = Aᵀ(Aᵀ)ᵀ = AᵀA."),
    ("The diagonal entries of a skew-symmetric matrix are all:", [("1", False), ("positive", False), ("0", True), ("negative", False)], "If Aᵀ = −A, then aᵢᵢ = −aᵢᵢ, which means 2aᵢᵢ = 0, so each diagonal entry is 0."),
    ("If Aᵀ = A⁻¹, then A is called:", [("symmetric", False), ("orthogonal", True), ("diagonal", False), ("singular", False)], "An orthogonal matrix satisfies AᵀA = I, meaning the transpose equals the inverse."),
    ("Transposing a diagonal matrix produces:", [("the zero matrix", False), ("the identity", False), ("the same diagonal matrix", True), ("a skew-symmetric matrix", False)], "Diagonal matrices are symmetric, so Dᵀ = D."),
    ("det(Aᵀ) = ", [("−det(A)", False), ("1/det(A)", False), ("det(A)", True), ("0", False)], "A matrix and its transpose always have the same determinant."),
    ("If A is 2×4, then AᵀA is:", [("2×2", False), ("4×2", False), ("4×4", True), ("2×4", False)], "Aᵀ is 4×2, so AᵀA = (4×2)(2×4) = 4×4."),
    ("Any square matrix can be written as the sum of:", [("two identity matrices", False), ("a symmetric and a skew-symmetric matrix", True), ("two diagonal matrices", False), ("an inverse and a transpose", False)], "A = ½(A + Aᵀ) + ½(A − Aᵀ). The first term is symmetric, the second is skew-symmetric."),
],

# ───────────────────────────────────────────────
# U1 L1.7  Applications in Geometry
# ───────────────────────────────────────────────
"u1_l1.7": [
    ("In 2D, a point (3, 4) can be represented as the vector:", [("[3, 4]", True), ("[4, 3]", False), ("[[3, 4]]", False), ("3 + 4i", False)], "A 2D point maps directly to a 2-component position vector with the same coordinates."),
    ("Reflecting a point across the x-axis changes:", [("the x-coordinate's sign", False), ("the y-coordinate's sign", True), ("both coordinates' signs", False), ("neither coordinate", False)], "Reflection over x-axis: (x, y) → (x, −y). Only the y-coordinate is negated."),
    ("The transformation matrix for reflection over the y-axis is:", [("[[1,0],[0,−1]]", False), ("[[-1,0],[0,1]]", True), ("[[0,1],[1,0]]", False), ("[[0,−1],[−1,0]]", False)], "Reflection over y-axis sends (x,y) → (−x,y). The matrix [[-1,0],[0,1]] achieves this."),
    ("A 90° counter-clockwise rotation matrix in 2D is:", [("[[1,0],[0,1]]", False), ("[[0,−1],[1,0]]", True), ("[[0,1],[−1,0]]", False), ("[[-1,0],[0,-1]]", False)], "Rotating 90° CCW sends (x,y) → (−y,x), which corresponds to [[0,−1],[1,0]]."),
    ("Scaling a vector [x, y] by factor 2 in both directions gives:", [("[x+2, y+2]", False), ("[2x, 2y]", True), ("[x², y²]", False), ("[x/2, y/2]", False)], "Uniform scaling by factor k multiplies each component: [kx, ky]."),
    ("The area of a parallelogram formed by vectors u and v equals:", [("u · v", False), ("|det([u | v])|", True), ("‖u‖ + ‖v‖", False), ("‖u‖ · ‖v‖", False)], "The absolute value of the determinant of the matrix formed by u and v gives the parallelogram's area."),
    ("Vectors [1, 0] and [0, 1] form a parallelogram with area:", [("0", False), ("2", False), ("1", True), ("4", False)], "det([[1,0],[0,1]]) = 1. These are the standard basis vectors forming a unit square."),
    ("Two vectors are parallel when one is a _____ of the other.", [("transpose", False), ("scalar multiple", True), ("perpendicular projection", False), ("determinant", False)], "Parallel vectors point in the same or opposite directions, meaning v = kw for some scalar k."),
    ("If det([u | v]) = 0, the vectors are:", [("perpendicular", False), ("unit vectors", False), ("parallel (or one is the zero vector)", True), ("forming a unit square", False)], "Zero determinant means the vectors are linearly dependent — parallel or one is the zero vector."),
    ("A translation moves every point by a fixed vector. Can a 2×2 matrix perform translation?", [("Yes, using the identity", False), ("No, you need homogeneous coordinates", True), ("Yes, using the zero matrix", False), ("Yes, using a diagonal matrix", False)], "Standard 2×2 matrices can only do linear transformations (through origin). Translation requires 3×3 homogeneous coordinates."),
    ("The transformation [[2,0],[0,3]] scales:", [("x by 3 and y by 2", False), ("x by 2 and y by 3", True), ("both by 2.5", False), ("both by 6", False)], "A diagonal scaling matrix [[a,0],[0,b]] scales x by a and y by b."),
    ("Rotating by 180° sends (x, y) to:", [("(−y, x)", False), ("(y, −x)", False), ("(−x, −y)", True), ("(x, y)", False)], "A 180° rotation negates both coordinates: (x,y) → (−x,−y)."),
    ("The midpoint between (2, 8) and (6, 4) is:", [("(8, 12)", False), ("(4, 6)", True), ("(−4, 4)", False), ("(3, 2)", False)], "Midpoint = ((2+6)/2, (8+4)/2) = (4, 6)."),
    ("Vectors u = [1, 2] and v = [−2, 1] are perpendicular because:", [("their sum is zero", False), ("their dot product is zero", True), ("their magnitudes are equal", False), ("they are parallel", False)], "u · v = 1(−2) + 2(1) = 0. Zero dot product means perpendicular."),
    ("Applying two transformations A then B results in the matrix:", [("A + B", False), ("AB", False), ("BA", True), ("A − B", False)], "In matrix transformation order, applying A first then B means the combined transformation is BA (B applied to A's result)."),
    ("The identity transformation [[1,0],[0,1]] represents:", [("reflection over x-axis", False), ("a 90° rotation", False), ("no change at all", True), ("scaling by 0", False)], "The identity matrix leaves every vector unchanged — it's the 'do nothing' transformation."),
    ("A shear transformation [[1,k],[0,1]] shifts x by:", [("k units", False), ("k times the y-coordinate", True), ("k times the x-coordinate", False), ("0", False)], "This shear adds k·y to the x-coordinate: (x,y) → (x+ky, y)."),
    ("The determinant of a rotation matrix is always:", [("0", False), ("1", True), ("−1", False), ("depends on the angle", False)], "Rotation preserves area and orientation, so its determinant is always 1."),
    ("A matrix with determinant −1 may represent:", [("a rotation only", False), ("a reflection (reverses orientation)", True), ("a scaling by 2", False), ("the identity", False)], "Determinant of −1 indicates the transformation reverses orientation, like a reflection."),
    ("To find where the unit square maps under transformation A, apply A to:", [("the identity matrix", False), ("only one vertex", False), ("the standard basis vectors [1,0] and [0,1]", True), ("the determinant", False)], "Transforming the standard basis vectors shows where the columns of A point, revealing the image of the unit square."),
],

# ───────────────────────────────────────────────
# U1 L1.8  Applications in Physics
# ───────────────────────────────────────────────
"u1_l1.8": [
    ("In physics, force is a vector because it has:", [("only magnitude", False), ("both magnitude and direction", True), ("only direction", False), ("no measurable properties", False)], "Force requires both how strong (magnitude) and which way (direction) to be fully described."),
    ("The net force on an object equals the _____ of all individual force vectors.", [("scalar product", False), ("vector sum", True), ("cross product", False), ("average", False)], "Net force is found by vector addition of all forces acting on the object."),
    ("If forces F₁ = [3, 0] N and F₂ = [0, 4] N act on an object, the net force magnitude is:", [("7 N", False), ("5 N", True), ("12 N", False), ("1 N", False)], "Net force = [3, 4], magnitude = √(9+16) = √25 = 5 N."),
    ("A displacement vector points from:", [("velocity to acceleration", False), ("start position to end position", True), ("mass to force", False), ("energy to momentum", False)], "Displacement describes the straight-line change in position from start to finish."),
    ("Momentum p = mv is a vector because:", [("mass is a vector", False), ("velocity is a vector, and scalar × vector = vector", True), ("it has no direction", False), ("it is always positive", False)], "Mass (scalar) times velocity (vector) produces momentum, which inherits direction from velocity."),
    ("The work done by a force F over displacement d is:", [("F × d (cross product)", False), ("F · d (dot product)", True), ("|F| + |d|", False), ("F − d", False)], "Work = F · d = |F||d|cos θ, the dot product of force and displacement."),
    ("When two forces are perpendicular, the magnitude of their resultant is found using:", [("simple addition", False), ("the Pythagorean theorem", True), ("subtraction", False), ("the cross product", False)], "For perpendicular vectors with magnitudes a and b, the resultant has magnitude √(a² + b²)."),
    ("A projectile has velocity v = [vₓ, vᵧ]. Its speed is:", [("vₓ + vᵧ", False), ("√(vₓ² + vᵧ²)", True), ("vₓ · vᵧ", False), ("|vₓ − vᵧ|", False)], "Speed is the magnitude of the velocity vector: √(vₓ² + vᵧ²)."),
    ("The torque vector τ = r × F uses the _____ product.", [("dot", False), ("cross", True), ("scalar", False), ("tensor", False)], "Torque is the cross product of the position vector r and the force vector F."),
    ("In equilibrium, the sum of all force vectors equals:", [("[1, 1, 1]", False), ("the weight", False), ("the zero vector", True), ("the largest force", False)], "Equilibrium means net force = 0, so all forces balance to the zero vector."),
    ("An electric field E and magnetic field B are both:", [("scalars", False), ("vector fields", True), ("constants", False), ("dimensionless", False)], "Both E and B are vector quantities that vary in space — they are vector fields."),
    ("Resolving a force vector means:", [("eliminating it", False), ("breaking it into perpendicular components", True), ("doubling its magnitude", False), ("reversing its direction", False)], "Resolution decomposes a vector into x- and y-components using sin and cos."),
    ("A 10 N force at 30° above horizontal has a horizontal component of:", [("5 N", False), ("10 cos 30° ≈ 8.66 N", True), ("10 sin 30° = 5 N", False), ("10 N", False)], "Horizontal component = F cos θ = 10 cos 30° ≈ 8.66 N."),
    ("The position of a particle at time t is r(t) = [2t, 3t²]. Its velocity at t = 1 is:", [("[2, 3]", False), ("[2, 6]", True), ("[1, 3]", False), ("[4, 9]", False)], "Velocity = dr/dt = [2, 6t]. At t = 1: [2, 6]."),
    ("In a coordinate system, unit vectors î and ĵ point along:", [("any two directions", False), ("the x-axis and y-axis respectively", True), ("the same direction", False), ("the diagonal", False)], "î and ĵ are the standard unit vectors along the positive x- and y-axes."),
    ("A force F = 5î − 3ĵ has magnitude:", [("2 N", False), ("8 N", False), ("√34 ≈ 5.83 N", True), ("15 N", False)], "Magnitude = √(5² + (−3)²) = √(25 + 9) = √34 ≈ 5.83."),
    ("The dot product of perpendicular vectors is:", [("maximum", False), ("their product of magnitudes", False), ("zero", True), ("negative", False)], "u · v = |u||v| cos 90° = 0. Perpendicular vectors have zero dot product."),
    ("Matrices are used in physics to represent:", [("only scalars", False), ("rotations, inertia tensors, and coordinate transformations", True), ("only temperatures", False), ("only single forces", False)], "Matrices encode rotations, moments of inertia, stress tensors, and many other multi-component quantities."),
    ("The cross product of two parallel vectors is:", [("maximum", False), ("their magnitudes multiplied", False), ("the zero vector", True), ("undefined", False)], "u × v = |u||v| sin 0° = 0. Parallel vectors have zero cross product."),
    ("A 3D position vector [x, y, z] requires _____ components.", [("1", False), ("2", False), ("3", True), ("6", False)], "Three-dimensional space needs exactly three coordinates to specify a position."),
],

# ───────────────────────────────────────────────
# U2 L2.1  Solving Systems by Substitution & Elimination
# ───────────────────────────────────────────────
"u2_l2.1": [
    ("In the substitution method, you first:", [("add all equations", False), ("solve one equation for one variable, then substitute into another", True), ("multiply all equations together", False), ("set all variables to zero", False)], "Substitution isolates one variable in one equation, then replaces it in the other equation(s)."),
    ("The system x + y = 5, x − y = 1 has solution:", [("x = 2, y = 3", False), ("x = 3, y = 2", True), ("x = 1, y = 4", False), ("x = 4, y = 1", False)], "Adding the equations: 2x = 6, so x = 3. Then y = 5 − 3 = 2."),
    ("Elimination works by _____ equations to cancel a variable.", [("multiplying", False), ("adding or subtracting", True), ("squaring", False), ("differentiating", False)], "Elimination adds or subtracts multiples of equations so that one variable cancels out."),
    ("A system with exactly one solution is called:", [("inconsistent", False), ("dependent", False), ("independent and consistent", True), ("overdetermined", False)], "One unique solution means the system is consistent (has a solution) and independent (lines/planes intersect at one point)."),
    ("The system 2x + 4y = 10, x + 2y = 5 has:", [("no solution", False), ("exactly one solution", False), ("infinitely many solutions", True), ("exactly two solutions", False)], "The second equation is half the first, so they describe the same line — infinitely many solutions."),
    ("The system x + y = 3, x + y = 7 has:", [("one solution", False), ("infinitely many", False), ("no solution", True), ("two solutions", False)], "These are parallel lines (same slope, different intercepts) that never intersect."),
    ("To eliminate y from 3x + 2y = 7 and x − 2y = 1, you:", [("subtract the equations", False), ("add the equations", True), ("multiply both by 2", False), ("divide by y", False)], "Adding: (3x + 2y) + (x − 2y) = 7 + 1 → 4x = 8, so x = 2."),
    ("Back substitution means:", [("restarting the problem", False), ("plugging a found value back into an equation to find remaining unknowns", True), ("reversing all signs", False), ("using determinants", False)], "After finding one variable, substitute its value back to solve for the other(s)."),
    ("A system of 3 equations in 3 unknowns can have at most _____ solutions.", [("3", False), ("1 or infinitely many (or none)", True), ("exactly 3", False), ("2", False)], "A linear system has 0, 1, or infinitely many solutions — never exactly 2 or 3."),
    ("Graphically, two linear equations in 2 variables represent:", [("curves", False), ("two lines in the plane", True), ("circles", False), ("parabolas", False)], "Each linear equation in two variables graphs as a straight line in the xy-plane."),
    ("If two lines intersect at one point, the system is:", [("inconsistent", False), ("dependent", False), ("consistent with a unique solution", True), ("undefined", False)], "One intersection point means exactly one (x, y) satisfies both equations."),
    ("Multiplying both sides of an equation by a non-zero constant:", [("changes the solution set", False), ("preserves the solution set", True), ("makes it inconsistent", False), ("creates a new variable", False)], "Multiplying by a non-zero constant is a valid operation that doesn't change which values satisfy the equation."),
    ("The system 2x − y = 4, 6x − 3y = 12 is:", [("inconsistent", False), ("independent", False), ("dependent (infinitely many solutions)", True), ("has no solutions", False)], "The second equation is 3 times the first, making them the same line — infinitely many solutions."),
    ("Solve: x = 2y + 1, 3x − 6y = 3. How many solutions?", [("None", False), ("Exactly one", False), ("Infinitely many", True), ("Exactly two", False)], "Substitute: 3(2y+1) − 6y = 3 → 6y + 3 − 6y = 3 → 3 = 3, always true. Infinite solutions."),
    ("A consistent system has:", [("no solutions", False), ("at least one solution", True), ("exactly two solutions", False), ("undefined solutions", False)], "Consistent means at least one solution exists — either unique or infinitely many."),
    ("When using elimination, why might you multiply an equation by a constant first?", [("To change the solution", False), ("To make coefficients match so a variable cancels when adding", True), ("To increase the number of variables", False), ("To make the system inconsistent", False)], "Matching coefficients allows variables to cancel through addition or subtraction."),
    ("If solving gives 0 = 5, the system is:", [("consistent", False), ("inconsistent (no solution exists)", True), ("dependent", False), ("has one solution", False)], "A false statement like 0 = 5 means the equations contradict each other."),
    ("If solving gives 0 = 0, the system is:", [("inconsistent", False), ("independent", False), ("dependent (infinitely many solutions)", True), ("undefined", False)], "A true identity like 0 = 0 means the equations are redundant, giving infinitely many solutions."),
    ("The point (1, 2) is a solution to x + y = 3 and 2x − y = 0 because:", [("1 + 2 ≠ 3", False), ("it satisfies both equations simultaneously", True), ("it satisfies only one equation", False), ("no checking is needed", False)], "1 + 2 = 3 ✓ and 2(1) − 2 = 0 ✓. A solution must satisfy ALL equations in the system."),
    ("A system of 2 equations in 3 unknowns typically has:", [("no solution", False), ("exactly one solution", False), ("infinitely many solutions (a line or plane of solutions)", True), ("exactly three solutions", False)], "With more unknowns than equations, there are usually free variables leading to infinitely many solutions."),
],

# ───────────────────────────────────────────────
# U2 L2.2  Matrix Representation of Systems
# ───────────────────────────────────────────────
"u2_l2.2": [
    ("The system 2x + 3y = 7, x − y = 1 has coefficient matrix:", [("[[2,3,7],[1,−1,1]]", False), ("[[2,3],[1,−1]]", True), ("[[7],[1]]", False), ("[[2,1],[3,−1]]", False)], "The coefficient matrix contains only the variable coefficients, arranged by equation (rows) and variable (columns)."),
    ("An augmented matrix includes:", [("only the coefficients", False), ("the coefficients and the constants separated by a line", True), ("only the constants", False), ("the solution", False)], "The augmented matrix appends the constant column to the coefficient matrix: [A | b]."),
    ("For 3x − y = 5, x + 2y = 4, the augmented matrix is:", [("[[3,−1,5],[1,2,4]]", True), ("[[3,1],[−1,2]]", False), ("[[5,4],[3,1]]", False), ("[[3,−1],[1,2],[5,4]]", False)], "Each row represents one equation: coefficients followed by the constant. Row 1: [3, −1 | 5]."),
    ("In Ax = b, A represents:", [("the solution vector", False), ("the coefficient matrix", True), ("the constant vector", False), ("the augmented matrix", False)], "A holds the coefficients, x is the variable vector, and b is the constant vector."),
    ("The system x₁ + x₂ + x₃ = 6 has coefficient matrix of size:", [("1×1", False), ("3×1", False), ("1×3", True), ("3×3", False)], "One equation with three variables gives a 1×3 coefficient matrix."),
    ("Converting a system to matrix form helps because:", [("it removes all variables", False), ("we can apply systematic row operations", True), ("it changes the solution", False), ("it makes the system inconsistent", False)], "Matrix form allows systematic algorithms (like Gaussian elimination) to be applied uniformly."),
    ("The variable vector for a system in x, y, z is:", [("[x, y, z] (row vector)", False), ("[[x],[y],[z]] (column vector)", True), ("[[x,y,z],[0,0,0]]", False), ("a scalar", False)], "The variable vector is written as a column vector to match the matrix equation Ax = b."),
    ("If A is 3×3 and b is 3×1, the augmented matrix [A|b] has dimensions:", [("3×3", False), ("3×4", True), ("4×3", False), ("3×6", False)], "Appending a 3×1 column to a 3×3 matrix gives a 3×4 augmented matrix."),
    ("Each row of the augmented matrix corresponds to:", [("one variable", False), ("one equation in the system", True), ("one solution", False), ("one matrix operation", False)], "Each row represents one equation: the entries are the coefficients and the constant."),
    ("Each column (except the last) of the augmented matrix corresponds to:", [("one equation", False), ("one variable", True), ("one constant", False), ("the solution", False)], "Columns of the coefficient part correspond to variables x₁, x₂, etc. The last column holds constants."),
    ("The system Ax = b has a unique solution when:", [("A is the zero matrix", False), ("A is invertible (det(A) ≠ 0)", True), ("b is the zero vector", False), ("A has more rows than columns", False)], "An invertible coefficient matrix guarantees exactly one solution: x = A⁻¹b."),
    ("A homogeneous system has b =", [("the identity", False), ("any nonzero vector", False), ("the zero vector", True), ("undefined", False)], "Homogeneous systems have the form Ax = 0, where the constant vector is all zeros."),
    ("Every homogeneous system has at least _____ solution(s).", [("no", False), ("one (the trivial solution x = 0)", True), ("two", False), ("infinitely many", False)], "x = 0 always satisfies Ax = 0, so at least the trivial solution exists."),
    ("If a system has 5 equations and 3 unknowns, the coefficient matrix is:", [("3×5", False), ("5×3", True), ("5×5", False), ("3×3", False)], "Each equation is a row and each variable is a column: 5 equations, 3 variables = 5×3."),
    ("Two systems are equivalent if they have:", [("the same coefficient matrix", False), ("the same number of equations", False), ("the same solution set", True), ("the same constants", False)], "Equivalent systems may look different but share exactly the same set of solutions."),
    ("Row operations on the augmented matrix produce:", [("a different solution set", False), ("an equivalent system", True), ("additional equations", False), ("fewer variables", False)], "Elementary row operations preserve the solution set, giving an equivalent system."),
    ("The system x + y = 3, 2x + 2y = 6 corresponds to the augmented matrix:", [("[[1,1,3],[2,2,6]]", True), ("[[1,2],[1,2],[3,6]]", False), ("[[3,6],[1,2]]", False), ("[[1,1],[2,2]]", False)], "Equation 1 → row [1, 1 | 3], Equation 2 → row [2, 2 | 6]."),
    ("A square system (same number of equations as unknowns) can be solved by:", [("only substitution", False), ("matrix inversion if A is invertible", True), ("never using matrices", False), ("only graphing", False)], "When A is square and invertible, x = A⁻¹b gives the unique solution directly."),
    ("The matrix equation Ax = b is equivalent to:", [("b = xA", False), ("the original system of linear equations", True), ("x = Ab", False), ("A = xb", False)], "Multiplying out Ax = b row by row recovers the original equations."),
    ("If A is 2×3, x is 3×1, and b is 2×1, then Ax = b represents:", [("3 equations in 2 unknowns", False), ("2 equations in 3 unknowns", True), ("2 equations in 2 unknowns", False), ("3 equations in 3 unknowns", False)], "A has 2 rows (equations) and 3 columns (unknowns)."),
],

# ───────────────────────────────────────────────
# U2 L2.3  Gaussian Elimination
# ───────────────────────────────────────────────
"u2_l2.3": [
    ("Gaussian elimination reduces a matrix to:", [("diagonal form", False), ("row echelon form (upper triangular with leading 1s)", True), ("the zero matrix", False), ("the identity matrix", False)], "The goal is row echelon form: zeros below each pivot, creating a staircase pattern."),
    ("The three elementary row operations are:", [("add, multiply, transpose", False), ("swap rows, scale a row, add a multiple of one row to another", True), ("add rows, delete rows, copy rows", False), ("transpose, invert, determinant", False)], "Swap, scale (multiply by non-zero constant), and row combination are the three valid operations."),
    ("A pivot is:", [("any zero entry", False), ("the first non-zero entry in each row during elimination", True), ("the determinant", False), ("the last entry in each row", False)], "The pivot is the leading non-zero entry in a row, used to eliminate entries below it."),
    ("After Gaussian elimination, you solve by:", [("starting over", False), ("back substitution (from bottom row upward)", True), ("taking the determinant", False), ("transposing the matrix", False)], "Once in row echelon form, start from the last equation and work upward to find each variable."),
    ("Swapping two rows of the augmented matrix:", [("changes the solution", False), ("preserves the solution set", True), ("makes the system inconsistent", False), ("doubles all entries", False)], "Swapping rows just reorders the equations, which doesn't change the solutions."),
    ("Multiplying a row by a non-zero constant c:", [("changes the solution", False), ("preserves the solution set", True), ("makes the system homogeneous", False), ("is not allowed", False)], "Scaling an equation by a non-zero constant doesn't change which values satisfy it."),
    ("Adding a multiple of row 1 to row 2:", [("destroys information", False), ("preserves the solution set", True), ("changes both rows", False), ("requires c = 1", False)], "This row combination operation produces an equivalent system with the same solutions."),
    ("Starting matrix [[2,1,5],[4,3,11]]. Subtract 2×Row1 from Row2 to get:", [("[[2,1,5],[2,2,6]]", False), ("[[2,1,5],[0,1,1]]", True), ("[[0,−1,−1],[4,3,11]]", False), ("[[2,1,5],[4,3,11]]", False)], "Row2 − 2·Row1: [4−4, 3−2, 11−10] = [0, 1, 1]."),
    ("If a pivot column has zeros below the pivot, that column:", [("needs more elimination", False), ("is already in the correct form", True), ("should be deleted", False), ("indicates no solution", False)], "When all entries below a pivot are zero, elimination for that column is complete."),
    ("A row of all zeros in the augmented matrix (including the constant) indicates:", [("no solution", False), ("a dependent equation (one equation is redundant)", True), ("a unique solution", False), ("an error", False)], "An all-zero row [0 0 ... 0 | 0] represents 0 = 0, meaning that equation was redundant."),
    ("A row [0 0 0 | 5] in the augmented matrix means:", [("x₃ = 5", False), ("the system is dependent", False), ("the system is inconsistent (0 = 5 is false)", True), ("free variable", False)], "This row says 0x₁ + 0x₂ + 0x₃ = 5, i.e., 0 = 5 — a contradiction, so no solution exists."),
    ("The number of pivots determines:", [("the determinant", False), ("the rank of the coefficient matrix", True), ("the trace", False), ("the eigenvalues", False)], "Each pivot corresponds to one independent equation. The number of pivots equals the matrix rank."),
    ("If a 3×3 system has 3 pivots, the solution is:", [("no solution", False), ("infinitely many", False), ("unique", True), ("two solutions", False)], "Full rank (pivots = variables) in a consistent system guarantees a unique solution."),
    ("If a 3×3 system has 2 pivots and is consistent, the solution is:", [("unique", False), ("infinitely many (one free variable)", True), ("impossible", False), ("exactly two solutions", False)], "3 variables − 2 pivots = 1 free variable, leading to infinitely many solutions."),
    ("Which is NOT an elementary row operation?", [("R₂ ← R₂ + 3R₁", False), ("R₁ ← 5R₁", False), ("R₁ ↔ R₃", False), ("R₂ ← R₂ · R₃ (multiply two rows together)", True)], "Multiplying two rows together is not an elementary row operation. Only swap, scale, and add-multiple are valid."),
    ("Forward elimination proceeds:", [("from the bottom row to the top", False), ("from the top row downward, creating zeros below pivots", True), ("by transposing the matrix", False), ("by finding eigenvalues", False)], "Forward elimination works top-to-bottom, creating the upper triangular staircase pattern."),
    ("After elimination, [[1,2,3],[0,1,−1],[0,0,1]] represents:", [("an inconsistent system", False), ("a system in row echelon form ready for back substitution", True), ("the identity matrix", False), ("a degenerate system", False)], "This is proper row echelon form — upper triangular with leading 1s. Back substitution can proceed."),
    ("Partial pivoting means:", [("using the smallest pivot", False), ("swapping rows to use the largest available pivot (for numerical stability)", True), ("eliminating all pivots", False), ("using only the first row", False)], "Choosing the largest pivot reduces rounding errors in computer calculations."),
    ("Gaussian elimination on an n×n system generally takes about _____ operations.", [("n", False), ("n²", False), ("n³/3 (cubic complexity)", True), ("2ⁿ (exponential)", False)], "The operation count is roughly n³/3, making Gaussian elimination efficient for moderate n."),
    ("The augmented matrix [[1,0,2],[0,1,3]] is already solved. The solution is:", [("x = 2, y = 3", True), ("x = 3, y = 2", False), ("x = 0, y = 0", False), ("no solution", False)], "This is reduced row echelon form: x = 2, y = 3 can be read directly."),
],

# ───────────────────────────────────────────────
# U2 L2.4  Gauss-Jordan Elimination
# ───────────────────────────────────────────────
"u2_l2.4": [
    ("Gauss-Jordan elimination produces:", [("row echelon form", False), ("reduced row echelon form (RREF)", True), ("the zero matrix", False), ("a diagonal matrix always", False)], "Gauss-Jordan goes further than Gaussian by also eliminating above pivots, reaching RREF."),
    ("In RREF, each pivot column has:", [("all zeros", False), ("a 1 in the pivot position and 0s everywhere else in that column", True), ("the same value in every entry", False), ("the determinant", False)], "RREF has leading 1s with zeros both above and below each pivot."),
    ("The main difference between Gaussian and Gauss-Jordan elimination:", [("Gauss-Jordan doesn't use row operations", False), ("Gauss-Jordan also eliminates above the pivots", True), ("Gaussian produces RREF", False), ("There is no difference", False)], "Gaussian stops at row echelon form; Gauss-Jordan continues to clear entries above pivots."),
    ("The RREF of any matrix is:", [("not unique", False), ("always the identity", False), ("unique (every matrix has exactly one RREF)", True), ("always the zero matrix", False)], "Every matrix has a unique reduced row echelon form, regardless of the row operations used."),
    ("In RREF, the solution can be read:", [("only by back substitution", False), ("directly from the matrix without back substitution", True), ("by taking the determinant", False), ("by transposing the matrix", False)], "RREF isolates each variable, so solutions are read directly from the last column."),
    ("Starting from [[1,2,5],[0,1,2]], eliminate above the second pivot:", [("R₁ ← R₁ − 2R₂ → [[1,0,1],[0,1,2]]", True), ("R₁ ← R₁ + 2R₂ → [[1,4,9],[0,1,2]]", False), ("R₂ ← R₂ − R₁", False), ("No change needed", False)], "To clear the 2 above the second pivot: Row1 − 2·Row2 = [1−0, 2−2, 5−4] = [1, 0, 1]."),
    ("RREF of [[2,4,6],[1,3,5]] is:", [("[[1,0,−1],[0,1,2]]", True), ("[[2,4,6],[0,1,2]]", False), ("[[1,2,3],[1,3,5]]", False), ("[[1,3,5],[2,4,6]]", False)], "After elimination and scaling: x = −1, y = 2, giving RREF [[1,0,−1],[0,1,2]]."),
    ("If the RREF has a column with no pivot, that variable is:", [("zero", False), ("undefined", False), ("a free variable", True), ("the solution", False)], "Non-pivot columns correspond to free variables that can take any value."),
    ("Free variables arise when:", [("the system is inconsistent", False), ("there are more unknowns than pivots", True), ("all variables are determined", False), ("the determinant is non-zero", False)], "If the number of variables exceeds the number of pivots, the extra variables are free."),
    ("The RREF of a 3×3 invertible matrix is:", [("the zero matrix", False), ("any upper triangular matrix", False), ("the 3×3 identity matrix", True), ("a 3×4 matrix", False)], "An invertible matrix has full rank (3 pivots), so RREF = I₃."),
    ("Gauss-Jordan can be used to find the inverse of A by:", [("computing det(A)", False), ("row reducing [A | I] to [I | A⁻¹]", True), ("transposing A", False), ("squaring A", False)], "Augment A with the identity and row reduce. If A is invertible, the right side becomes A⁻¹."),
    ("How many row operations does Gauss-Jordan typically require compared to Gaussian?", [("Fewer", False), ("The same number", False), ("More (additional upward elimination)", True), ("It depends on the matrix size only", False)], "Gauss-Jordan performs additional operations to clear above pivots, requiring more total operations."),
    ("The pivot positions in RREF form a:", [("column", False), ("staircase pattern (each pivot is to the right of and below the previous)", True), ("diagonal always", False), ("random pattern", False)], "Pivots step down and to the right, creating a staircase from upper-left toward lower-right."),
    ("If row reducing [A | b] produces [I | x], then x is:", [("the determinant", False), ("the solution vector", True), ("the inverse of A", False), ("the zero vector", False)], "When the coefficient part reduces to I, the augmented column gives the solution directly."),
    ("The rank of a matrix can be found by:", [("counting rows", False), ("counting the number of pivots in RREF", True), ("adding all entries", False), ("taking the transpose", False)], "The rank equals the number of non-zero rows (pivots) in the reduced form."),
    ("A system is inconsistent in RREF when:", [("a row is [0 0 ... 0 | c] with c ≠ 0", True), ("all rows have pivots", False), ("there are free variables", False), ("the matrix is square", False)], "A row [0 ... 0 | c] with c ≠ 0 says 0 = c, a contradiction."),
    ("RREF of [[1,1,1,6],[0,1,2,5],[0,0,1,3]]:", [("[[1,0,0,1],[0,1,0,−1],[0,0,1,3]]", True), ("[[1,1,1,6],[0,1,2,5],[0,0,1,3]]", False), ("[[6,5,3],[1,1,1],[0,0,0]]", False), ("[[1,0,0,6],[0,1,0,5],[0,0,1,3]]", False)], "Eliminate upward: From R3 (z=3), clear z from R2 and R1, then clear y from R1. Get x=1, y=−1, z=3."),
    ("In Gauss-Jordan, scaling a pivot row so the pivot becomes 1 is:", [("optional but never done", False), ("required for RREF", True), ("only for 2×2 matrices", False), ("an invalid operation", False)], "RREF requires leading 1s, so each pivot row is scaled to make the pivot exactly 1."),
    ("The system x + y + z = 0, 2x + 2y + 2z = 0 has RREF:", [("[[1,1,1,0],[0,0,0,0]]", True), ("[[1,0,0,0],[0,1,0,0]]", False), ("[[1,1,1,0]]", False), ("[[0,0,0,0],[0,0,0,0]]", False)], "Row 2 is 2×Row 1, so it reduces to a zero row. One equation, three unknowns → two free variables."),
    ("Gauss-Jordan is often preferred when:", [("only one solution is needed", False), ("the inverse is needed or multiple right-hand sides must be solved", True), ("the matrix is 1×1", False), ("the system is inconsistent", False)], "Gauss-Jordan's RREF is especially useful for finding inverses and solving systems with multiple right-hand sides simultaneously."),
],

# ───────────────────────────────────────────────
# U2 L2.5  Row Echelon Form
# ───────────────────────────────────────────────
"u2_l2.5": [
    ("In row echelon form, all entries below each pivot are:", [("equal to 1", False), ("zero", True), ("positive", False), ("equal to the pivot", False)], "REF requires zeros below every pivot, creating the staircase pattern."),
    ("Which is in row echelon form?", [("[[0,1,2],[1,0,3]]", False), ("[[1,3,2],[0,0,1]]", True), ("[[0,0,0],[1,2,3]]", False), ("[[1,2],[3,4]]", False)], "Leading entry in row 1 is to the left of leading entry in row 2, with zeros below each pivot."),
    ("Why must zero rows appear at the bottom?", [("For aesthetics", False), ("The staircase pattern requires pivots to step right-downward; all-zero rows have no pivot", True), ("Zero rows must be first", False), ("They can appear anywhere", False)], "Rows with no leading entry (all zeros) go to the bottom to maintain the staircase structure."),
    ("A leading entry (pivot) must be:", [("on the main diagonal", False), ("the first non-zero entry in its row", True), ("in the last column", False), ("equal to the determinant", False)], "The pivot is the leftmost non-zero entry in each non-zero row."),
    ("Each pivot must be _____ of the pivot in the row above.", [("directly above", False), ("to the left", False), ("strictly to the right", True), ("in the same column", False)], "Pivots step to the right as you move down, creating the staircase shape."),
    ("How many row echelon forms can a matrix have?", [("Exactly one", False), ("Multiple (REF is not unique, unlike RREF)", True), ("Zero", False), ("Always two", False)], "Different sequences of row operations may produce different REFs, but they all share the same pivots and rank."),
    ("The number of non-zero rows in REF equals the matrix's:", [("trace", False), ("rank", True), ("determinant", False), ("dimension", False)], "Each non-zero row has a pivot, and the number of pivots equals the rank."),
    ("[[1,2,3],[0,0,4],[0,0,0]] is in REF with rank:", [("3", False), ("2", True), ("1", False), ("0", False)], "Two non-zero rows, each with a pivot → rank 2."),
    ("If a 4×5 matrix has REF with 3 pivots, how many free variables?", [("3", False), ("2", True), ("4", False), ("5", False)], "Free variables = total variables − pivots = 5 − 3 = 2."),
    ("In REF, can two pivots be in the same column?", [("Yes, always", False), ("No, each column has at most one pivot", True), ("Only in square matrices", False), ("Only if they equal 1", False)], "Each pivot is the sole leading entry in its column — no two pivots share a column."),
    ("Converting from REF to RREF requires:", [("additional forward elimination", False), ("backward elimination (clearing entries above pivots)", True), ("restarting the process", False), ("computing the determinant", False)], "To get from REF to RREF, eliminate entries above each pivot and scale pivots to 1."),
    ("REF of [[1,2],[3,4]]: subtract 3×Row1 from Row2:", [("[[1,2],[0,−2]]", True), ("[[1,2],[3,4]]", False), ("[[1,2],[0,2]]", False), ("[[−2,−2],[3,4]]", False)], "Row2 − 3·Row1: [3−3, 4−6] = [0, −2]. This is now in REF."),
    ("For REF, do pivots need to equal 1?", [("Yes, always", False), ("No, any non-zero leading entry is acceptable in REF", True), ("Only in the first row", False), ("Only for square matrices", False)], "REF only requires the staircase pattern. RREF additionally requires pivots to be 1."),
    ("A matrix in both REF and RREF has:", [("no pivots", False), ("pivots equal to 1 with zeros above and below", True), ("only zero entries", False), ("a non-zero determinant always", False)], "Meeting both conditions means leading 1s with all other entries in pivot columns being zero."),
    ("[[1,0,2],[0,0,0],[0,1,3]] is NOT in REF because:", [("it has a zero row", False), ("row 3's pivot is to the left of where it should be (not below row 1's pivot position, and row 2 is zero)", True), ("it has too many entries", False), ("the pivots aren't 1", False)], "Zero rows must come last. Row 3 has a non-zero entry but row 2 is all zeros, violating REF."),
    ("Every matrix can be brought to REF using:", [("only row swaps", False), ("elementary row operations", True), ("column operations", False), ("determinants", False)], "The three elementary row operations are sufficient to bring any matrix to REF."),
    ("If two rows have the same pivot column, you must:", [("ignore one", False), ("use elimination to make one of them zero in that column, or swap rows", True), ("delete a row", False), ("add a new column", False)], "Eliminate so only one row has the leading entry in that column, maintaining the staircase."),
    ("REF helps determine:", [("only the determinant", False), ("the rank, consistency, and structure of the solution set", True), ("only eigenvalues", False), ("only the inverse", False)], "REF reveals rank (number of pivots), consistency (no contradictory rows), and number of free variables."),
    ("A 3×3 matrix with 3 pivots in REF looks like:", [("all zeros", False), ("upper triangular with non-zero diagonal entries", True), ("the identity necessarily", False), ("lower triangular", False)], "Three pivots stepping right-down in a 3×3 matrix = upper triangular with all diagonal entries non-zero."),
    ("Column operations are _____ used in Gaussian elimination.", [("always", False), ("sometimes", False), ("not (only row operations preserve the solution set)", True), ("required", False)], "Column operations would mix up variables, changing the meaning of the system. Only row operations are used."),
],

# ───────────────────────────────────────────────
# U2 L2.6  Consistent vs. Inconsistent Systems
# ───────────────────────────────────────────────
"u2_l2.6": [
    ("A consistent system has:", [("no solutions", False), ("at least one solution", True), ("only integer solutions", False), ("infinitely many always", False)], "Consistent means the system can be satisfied — it has one or more solutions."),
    ("An inconsistent system has:", [("exactly one solution", False), ("infinitely many solutions", False), ("no solutions", True), ("only trivial solutions", False)], "Inconsistent means the equations contradict each other, so no solution exists."),
    ("The system x + y = 2, x + y = 5 is:", [("consistent", False), ("inconsistent (parallel lines, no intersection)", True), ("dependent", False), ("has a unique solution", False)], "Both equations claim x+y equals different values — a contradiction."),
    ("A row [0, 0, 0 | 4] in the augmented matrix indicates:", [("a free variable", False), ("a dependent system", False), ("inconsistency (0 = 4 is impossible)", True), ("the solution x = 4", False)], "This translates to 0 = 4, which is false, meaning no solution exists."),
    ("If the rank of the coefficient matrix equals the rank of the augmented matrix, the system is:", [("always inconsistent", False), ("consistent", True), ("always has a unique solution", False), ("undefined", False)], "rank(A) = rank([A|b]) means no contradictory rows, so the system is consistent."),
    ("If rank(A) < rank([A|b]), the system is:", [("consistent", False), ("inconsistent", True), ("dependent", False), ("has a unique solution", False)], "rank([A|b]) > rank(A) means a pivot appeared in the constant column — a contradiction row exists."),
    ("A consistent system with rank = number of unknowns has:", [("no solution", False), ("infinitely many solutions", False), ("a unique solution", True), ("two solutions", False)], "Full rank means every variable is a pivot variable — no free variables, so the solution is unique."),
    ("A consistent system where rank < number of unknowns has:", [("no solution", False), ("a unique solution", False), ("infinitely many solutions", True), ("exactly two solutions", False)], "Fewer pivots than variables means free variables exist, giving infinitely many solutions."),
    ("Geometrically, two inconsistent equations in 2D represent:", [("intersecting lines", False), ("the same line", False), ("parallel lines (never intersect)", True), ("perpendicular lines", False)], "Parallel lines have the same slope but different intercepts — no intersection point."),
    ("Three planes meeting at a single point represent:", [("an inconsistent system", False), ("a consistent system with a unique solution", True), ("infinitely many solutions", False), ("a dependent system", False)], "Three non-parallel, non-coincident planes intersecting at one point = one unique solution."),
    ("The Rank-Nullity Theorem states rank + nullity =", [("the determinant", False), ("the trace", False), ("the number of columns (unknowns)", True), ("the number of rows", False)], "rank + nullity = n, where n is the number of columns/variables."),
    ("Nullity measures:", [("the number of pivots", False), ("the number of free variables in the homogeneous system Ax = 0", True), ("the determinant", False), ("the number of equations", False)], "Nullity = dimension of the null space = number of free variables."),
    ("A system of 3 equations in 3 unknowns with rank 2 has:", [("exactly 2 solutions", False), ("no solution necessarily", False), ("either no solution or infinitely many (depends on consistency)", True), ("a unique solution", False)], "Rank 2 < 3 unknowns means either inconsistent or infinitely many solutions with one free variable."),
    ("Which always guarantees a unique solution for an n×n system?", [("n equations", False), ("det(A) ≠ 0", True), ("n > 3", False), ("b = 0", False)], "Non-zero determinant means A is invertible, guaranteeing a unique solution for any b."),
    ("A dependent system:", [("has no solutions", False), ("has at least one equation that is a combination of the others", True), ("has exactly one solution", False), ("is always inconsistent", False)], "Dependent means redundant equations — some equations can be derived from others, leading to infinitely many solutions."),
    ("For the system x − y = 1, 2x − 2y = 2, 3x − 3y = 3:", [("It is inconsistent", False), ("It has a unique solution", False), ("All three equations are the same line — infinitely many solutions", True), ("It has exactly 3 solutions", False)], "All three equations simplify to x − y = 1 — one relationship, two unknowns, infinite solutions."),
    ("Adding a redundant equation to a consistent system:", [("makes it inconsistent", False), ("does not change the solution set", True), ("adds more solutions", False), ("removes solutions", False)], "A redundant equation provides no new information, so the solution set stays the same."),
    ("A system with more equations than unknowns is called:", [("underdetermined", False), ("overdetermined", True), ("square", False), ("homogeneous", False)], "More equations than unknowns = overdetermined. It may be inconsistent, or may still have solutions."),
    ("An underdetermined system (fewer equations than unknowns) typically has:", [("no solution", False), ("a unique solution", False), ("infinitely many solutions (if consistent)", True), ("exactly two solutions", False)], "More unknowns than equations usually means free variables, giving infinitely many solutions."),
    ("The system 0x + 0y = 0 is:", [("inconsistent", False), ("consistent, but tells us nothing about x and y", True), ("only satisfied by x = y = 0", False), ("undefined", False)], "0 = 0 is always true and imposes no constraint — both x and y are free."),
],

# ───────────────────────────────────────────────
# U2 L2.7  Applications in Economics
# ───────────────────────────────────────────────
"u2_l2.7": [
    ("In a supply-demand model, equilibrium occurs when:", [("supply is zero", False), ("demand exceeds supply", False), ("the quantity supplied equals the quantity demanded", True), ("price is at its maximum", False)], "Equilibrium is the price-quantity pair where the supply and demand curves intersect."),
    ("If supply: Qs = 2p − 10 and demand: Qd = −p + 50, equilibrium price is:", [("p = 10", False), ("p = 20", True), ("p = 30", False), ("p = 40", False)], "Set 2p − 10 = −p + 50 → 3p = 60 → p = 20. Then Q = 30."),
    ("Leontief input-output models use matrices to:", [("determine stock prices directly", False), ("describe how industries supply inputs to each other", True), ("calculate interest rates", False), ("measure inflation only", False)], "The input-output model shows interdependencies between sectors of an economy."),
    ("In the Leontief model, total output x satisfies:", [("x = b (demand only)", False), ("x = Ax + d, where A is the technology matrix and d is final demand", True), ("x = A⁻¹ only", False), ("x = 0 always", False)], "Each industry's output covers both inter-industry demand (Ax) and final consumer demand (d)."),
    ("The solution to the Leontief model is x =", [("(A − I)d", False), ("(I − A)⁻¹d", True), ("Ad", False), ("A²d", False)], "From x = Ax + d: (I − A)x = d, so x = (I − A)⁻¹d, provided (I − A) is invertible."),
    ("A two-sector economy with sectors A and B requires solving:", [("1 equation", False), ("a 2×2 system of linear equations", True), ("a differential equation", False), ("a 5×5 system", False)], "Two sectors produce a system of two equations with two unknowns (output of each sector)."),
    ("In a closed economy Leontief model, all output goes to:", [("exports", False), ("consumption and inter-industry use (no external demand)", True), ("government only", False), ("waste", False)], "A closed model has no external demand — all production is consumed within the system."),
    ("Break-even analysis finds where:", [("profit is maximized", False), ("total revenue equals total cost", True), ("demand equals zero", False), ("price equals zero", False)], "Break-even is the point where the business neither profits nor loses: Revenue = Cost."),
    ("If cost = 500 + 10x and revenue = 25x, the break-even quantity is:", [("x = 20", False), ("x ≈ 33.3", True), ("x = 50", False), ("x = 100", False)], "Set 25x = 500 + 10x → 15x = 500 → x ≈ 33.3 units."),
    ("A portfolio allocation problem with 3 asset types requires:", [("1 equation", False), ("a system of equations relating allocations, returns, and constraints", True), ("only multiplication", False), ("no linear algebra", False)], "Constraints on total investment, return target, and risk create a system solvable by matrix methods."),
    ("In market equilibrium with two goods, you solve:", [("one equation", False), ("two simultaneous equations (one for each market)", True), ("only graphically", False), ("by inspection", False)], "Each good has its own supply-demand equation, and both must be in equilibrium simultaneously."),
    ("If two firms set prices p₁ and p₂ based on each other's prices, this is:", [("independent pricing", False), ("a game theory equilibrium solvable as a linear system", True), ("supply-demand analysis", False), ("break-even analysis", False)], "Reaction functions p₁ = f(p₂) and p₂ = g(p₁) form a linear system; the solution is the Nash equilibrium."),
    ("A technology matrix A has entries aᵢⱼ representing:", [("final consumer demand", False), ("the amount of sector i's output needed per unit of sector j's output", True), ("prices", False), ("interest rates", False)], "Entry aᵢⱼ is the input from sector i required to produce one unit of sector j's output."),
    ("For the Leontief model to work, all entries of A must be:", [("negative", False), ("greater than 1", False), ("non-negative, and each column sum should be less than 1", True), ("zero", False)], "Entries represent production requirements (non-negative), and columns summing to less than 1 ensures each sector adds value."),
    ("In a three-market equilibrium problem, the coefficient matrix is:", [("1×1", False), ("2×2", False), ("3×3", True), ("3×1", False)], "Three markets = three equations in three price unknowns → 3×3 coefficient matrix."),
    ("Linear programming differs from systems of linear equations because it:", [("uses no variables", False), ("optimizes an objective subject to inequality constraints", True), ("always has a unique solution", False), ("uses only 2×2 matrices", False)], "Linear programming maximizes or minimizes a linear function subject to inequality constraints."),
    ("Solving economic models with matrices is preferred because it:", [("gives only approximate answers", False), ("handles many variables and equations systematically", True), ("ignores constraints", False), ("only works for small problems", False)], "Matrix methods scale well and can solve large systems that would be impractical by hand."),
    ("If a country trades 3 goods with 3 partners, the trade model involves:", [("a 3×3 system", True), ("a 1×1 system", False), ("no equations", False), ("only subtraction", False)], "Each good's trade balance produces one equation per partner, but given the structure it typically reduces to a 3×3 system."),
    ("The Leontief inverse (I − A)⁻¹ is also called:", [("the technology matrix", False), ("the total requirements matrix", True), ("the demand vector", False), ("the identity matrix", False)], "The Leontief inverse shows the total output each sector must produce per unit of final demand, including all indirect effects."),
    ("An economic system is 'productive' if:", [("(I − A) is singular", False), ("(I − A)⁻¹ exists and has all non-negative entries", True), ("all output is zero", False), ("demand exceeds supply always", False)], "A productive economy can satisfy any non-negative demand — (I − A)⁻¹ exists with non-negative entries."),
],

# ───────────────────────────────────────────────
# U2 L2.8  Applications in Engineering
# ───────────────────────────────────────────────
"u2_l2.8": [
    ("In circuit analysis, Kirchhoff's current law at a node gives:", [("a quadratic equation", False), ("a linear equation relating branch currents", True), ("a differential equation", False), ("no useful equation", False)], "KCL states that currents entering a node equal currents leaving — a linear constraint."),
    ("Kirchhoff's voltage law around a loop gives:", [("a nonlinear equation", False), ("a linear equation summing voltage drops to zero", True), ("a matrix equation directly", False), ("the power in the circuit", False)], "KVL states that the algebraic sum of voltage drops around any closed loop equals zero."),
    ("A circuit with 3 unknown currents requires solving:", [("1 equation", False), ("a 3×3 linear system", True), ("a 6×6 system", False), ("only Ohm's law", False)], "Three unknown currents need three independent equations from KCL and KVL."),
    ("In structural analysis, equilibrium of forces at a joint gives:", [("a volume equation", False), ("linear equations relating member forces", True), ("a temperature equation", False), ("no equations", False)], "Force balance at each joint produces linear equations in the unknown member forces."),
    ("A truss with 5 unknown member forces requires at least:", [("2 equations", False), ("5 independent equations", True), ("10 equations", False), ("1 equation", False)], "Each unknown needs a corresponding independent equation for a unique solution."),
    ("Mesh analysis in circuits assigns:", [("voltage to each node", False), ("a loop current to each independent loop", True), ("resistance to each node", False), ("power to each element", False)], "Mesh analysis defines loop currents; KVL around each mesh produces the linear equations."),
    ("Nodal analysis in circuits assigns:", [("current to each loop", False), ("voltage to each node (relative to a reference)", True), ("power to each branch", False), ("resistance to each mesh", False)], "Nodal analysis uses node voltages as unknowns and applies KCL at each node."),
    ("A bridge circuit with 5 resistors typically needs:", [("1 equation", False), ("a system of 3 equations", True), ("20 equations", False), ("only Ohm's law without a system", False)], "After defining mesh or node variables, a bridge circuit usually reduces to 3 equations in 3 unknowns."),
    ("Finite element analysis (FEA) solves large systems of the form:", [("Ax = b, where A can have thousands of rows", True), ("a single equation", False), ("only 2×2 systems", False), ("no linear systems", False)], "FEA discretizes structures into elements, producing very large sparse systems of linear equations."),
    ("In heat transfer, steady-state temperature distribution leads to:", [("nonlinear equations only", False), ("a system of linear equations at discrete points", True), ("random temperatures", False), ("no equations", False)], "Discretizing the heat equation at grid points yields a linear system for the temperatures."),
    ("The stiffness matrix K in structural analysis is typically:", [("1×1", False), ("symmetric and positive definite", True), ("skew-symmetric", False), ("always diagonal", False)], "Physical properties ensure K is symmetric (Kᵀ = K) and positive definite."),
    ("For Ku = F (stiffness method), u represents:", [("forces", False), ("displacements at nodes", True), ("temperatures", False), ("currents", False)], "In structural analysis, u is the vector of unknown nodal displacements and F is the applied force vector."),
    ("Signal processing uses linear systems to:", [("amplify sound only", False), ("model filters, transformations, and decompositions of signals", True), ("only record audio", False), ("measure weight", False)], "Filters and transforms are linear operations on signals, naturally expressed as matrix equations."),
    ("A system with 3 loops in a circuit and 3 mesh currents is modeled by:", [("a 3×1 vector only", False), ("a 3×3 resistance matrix times a current vector", True), ("a single equation", False), ("a 33×33 system", False)], "Each loop equation relates 3 unknowns through resistances, forming a 3×3 system."),
    ("In control engineering, the state equation ẋ = Ax + Bu uses A as:", [("the input matrix only", False), ("the system matrix describing internal dynamics", True), ("the output matrix", False), ("a scalar", False)], "Matrix A encodes how the system's current state influences its rate of change."),
    ("Least squares in engineering minimizes:", [("the maximum error", False), ("the sum of squared differences between predicted and observed values", True), ("the number of equations", False), ("nothing", False)], "Least squares finds the best approximate solution by minimizing the total squared error."),
    ("The normal equations for least squares are:", [("Ax = b", False), ("AᵀAx = Aᵀb", True), ("A⁻¹x = b", False), ("x = b/A", False)], "Multiplying both sides of Ax ≈ b by Aᵀ gives the normal equations AᵀAx = Aᵀb."),
    ("An overdetermined system in engineering (more measurements than unknowns) is solved by:", [("ignoring extra equations", False), ("least squares approximation", True), ("adding more unknowns", False), ("deleting the system", False)], "With more equations than unknowns, an exact solution rarely exists; least squares gives the best fit."),
    ("Banded matrices (non-zero entries near the diagonal) arise frequently in:", [("abstract algebra only", False), ("finite difference and finite element methods", True), ("pure number theory", False), ("no engineering context", False)], "Discretization of physical systems typically produces banded or sparse matrices."),
    ("Sparsity (most entries being zero) matters in engineering because:", [("it doesn't matter", False), ("it allows efficient storage and faster solution algorithms", True), ("it means the system is inconsistent", False), ("all engineering matrices are dense", False)], "Sparse matrix algorithms exploit the zero structure to solve systems much faster."),
],

}

# ── Write to JSON ──
with open(PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

count = 0
for key, questions in LESSONS.items():
    if key not in data:
        print(f"⚠ Key {key} not found — skipping")
        continue
    new_qs = []
    for i, (qt, opts, expl) in enumerate(questions):
        new_qs.append(build_q(i + 1, qt, opts, expl))
    data[key]["quiz_questions"] = new_qs
    count += 1
    print(f"  ✓ {key}: {len(new_qs)} questions written")

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Linear Algebra U1-U2: replaced questions in {count} lessons")
