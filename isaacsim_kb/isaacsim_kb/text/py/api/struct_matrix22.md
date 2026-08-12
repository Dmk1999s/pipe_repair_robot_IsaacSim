<!-- source: py/api/struct_matrix22.html | title: Matrix22 — Isaac Sim -->

# Matrix22
structMatrix22

2x2 matrix representation with column-major storage.
This structure represents a 2x2 matrix stored in column-major order. It provides basic matrix operations including arithmetic, element access, and static identity matrix creation.
The matrix is stored as two Vec2 columns, making it suitable for 2D transformations and linear algebra operations.
Public Functions
inlineMatrix22()

Default constructor creating an uninitialized matrix.

inlineMatrix22(floata, floatb, floatc, floatd)

Constructor from individual matrix elements.
Creates a matrix with the specified elements: | a b | | c d |
Parameters:

- a – [in] Element at position (0,0)

- b – [in] Element at position (0,1)

- c – [in] Element at position (1,0)

- d – [in] Element at position (1,1)

inlineMatrix22(constVec2 &c1, constVec2 &c2)

Constructor from two column vectors.
Parameters:

- c1 – [in] First column vector

- c2 – [in] Second column vector

inlinefloatoperator()(inti, intj)const

Const element access operator.
Parameters:

- i – [in] Row index (0 or 1)

- j – [in] Column index (0 or 1)

Returns:
Const reference to the matrix element at (i,j)

inlinefloat&operator()(inti, intj)

Mutable element access operator.
Parameters:

- i – [in] Row index (0 or 1)

- j – [in] Column index (0 or 1)

Returns:
Mutable reference to the matrix element at (i,j)

Public Members
Vec2 cols[2]

Column vectors of the matrix.
The matrix is stored as two column vectors in column-major order. cols[0] represents the first column, cols[1] represents the second column.

Public Static Functions
staticinlineMatrix22 Identity()

Creates a 2x2 identity matrix.
Returns:
Identity matrix with 1s on the diagonal and 0s elsewhere
