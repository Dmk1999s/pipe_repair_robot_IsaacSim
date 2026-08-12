<!-- source: py/api/struct_matrix33.html | title: Matrix33 — Isaac Sim -->

# Matrix33
structMatrix33

3x3 matrix representation with column-major storage.
This structure represents a 3x3 matrix stored in column-major order. It provides matrix operations including arithmetic, element access, construction from quaternions, and static identity matrix creation.
The matrix is commonly used for 3D rotations, scaling, and other linear transformations in 3D space.
Public Functions
inlineMatrix33()

Default constructor creating an uninitialized matrix.

inlineMatrix33(constfloat*ptr)

Constructor from row-major float array.
Creates a matrix from a float array where elements are stored as: [0,1,2, 3,4,5, 6,7,8] representing rows [0], [1], [2]
Parameters:
ptr – [in] Pointer to array of 9 floats in row-major order

inlineMatrix33(constVec3 &c1, constVec3 &c2, constVec3 &c3)

Constructor from three column vectors.
Parameters:

- c1 – [in] First column vector

- c2 – [in] Second column vector

- c3 – [in] Third column vector

inlineMatrix33(constQuat &q)

Constructor from quaternion rotation.
Creates a rotation matrix from the given quaternion by rotating the standard basis vectors (1,0,0), (0,1,0), (0,0,1).
Parameters:
q – [in] Quaternion representing the rotation

inlinefloatoperator()(inti, intj)const

Const element access operator.
Parameters:

- i – [in] Row index (0, 1, or 2)

- j – [in] Column index (0, 1, or 2)

Returns:
Const reference to the matrix element at (i,j)

inlinefloat&operator()(inti, intj)

Mutable element access operator.
Parameters:

- i – [in] Row index (0, 1, or 2)

- j – [in] Column index (0, 1, or 2)

Returns:
Mutable reference to the matrix element at (i,j)

Public Members
Vec3 cols[3]

Column vectors of the matrix.
The matrix is stored as three column vectors in column-major order. cols[0], cols[1], cols[2] represent the first, second, and third columns respectively.

Public Static Functions
staticinlineMatrix33 Identity()

Creates a 3x3 identity matrix.
Returns:
Identity matrix with 1s on the diagonal and 0s elsewhere
