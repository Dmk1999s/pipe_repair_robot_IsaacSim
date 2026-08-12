<!-- source: py/api/class_x_matrix44.html | title: XMatrix44 — Isaac Sim -->

# XMatrix44
template<typenameT>
classXMatrix44

Template class representing a 4x4 matrix stored in column-major order.
A template-based 4x4 matrix class that provides matrix operations including arithmetic operations, transformations, and conversions. This class stores column vectors in column-major order, which is compatible with OpenGL and many graphics APIs.
The matrix is organized as follows:

- columns[0] = first column vector

- columns[1] = second column vector

- columns[2] = third column vector

- columns[3] = fourth column vector (often translation in transformation matrices)

Note
Matrix operations follow column-major conventions common in graphics programming
Template Parameters:
T – The numeric type for matrix elements (typically float or double)

Public Functions
inlineXMatrix44()

Default constructor initializes matrix to zero.

inlineXMatrix44(constT *d)

Constructor that initializes matrix from array data.
Parameters:
d – [in] Pointer to array of 16 elements in column-major order

inlineXMatrix44(
T c11,
T c21,
T c31,
T c41,
T c12,
T c22,
T c32,
T c42,
T c13,
T c23,
T c33,
T c43,
T c14,
T c24,
T c34,
T c44,
)
Constructor that initializes matrix with individual element values.
Parameters:

- c11 – [in] Element at row 1, column 1

- c21 – [in] Element at row 2, column 1

- c31 – [in] Element at row 3, column 1

- c41 – [in] Element at row 4, column 1

- c12 – [in] Element at row 1, column 2

- c22 – [in] Element at row 2, column 2

- c32 – [in] Element at row 3, column 2

- c42 – [in] Element at row 4, column 2

- c13 – [in] Element at row 1, column 3

- c23 – [in] Element at row 2, column 3

- c33 – [in] Element at row 3, column 3

- c43 – [in] Element at row 4, column 3

- c14 – [in] Element at row 1, column 4

- c24 – [in] Element at row 2, column 4

- c34 – [in] Element at row 3, column 4

- c44 – [in] Element at row 4, column 4

inlineXMatrix44(
constVec4 &c1,
constVec4 &c2,
constVec4 &c3,
constVec4 &c4,
)
Constructor that initializes matrix from four column vectors.
Parameters:

- c1 – [in] First column vector

- c2 – [in] Second column vector

- c3 – [in] Third column vector

- c4 – [in] Fourth column vector

inlineoperatorT *()

Conversion operator to non-const pointer to matrix data.
Returns:
Pointer to the first element in column-major order

inlineoperatorconstT *()const

Conversion operator to const pointer to matrix data.
Returns:
Const pointer to the first element in column-major order

inlineXMatrix44 <T >operator*(constXMatrix44 <T >&rhs)const

Matrix multiplication operator (right multiply)
Parameters:
rhs – [in] Matrix to multiply with (right operand)

Returns:
New matrix that is the product of this matrix and rhs

inlineXMatrix44 <T >&operator*=(constXMatrix44 <T >&rhs)

Matrix multiplication assignment operator (right multiply)
Parameters:
rhs – [in] Matrix to multiply with (right operand)

Returns:
Reference to this matrix after multiplication

inlinefloatoperator()(introw, intcol)const

Element access operator (const version)
Parameters:

- row – [in] Row index (0-3)

- col – [in] Column index (0-3)

Returns:
Const reference to matrix element at specified row and column

inlinefloat&operator()(introw, intcol)

Element access operator (non-const version)
Parameters:

- row – [in] Row index (0-3)

- col – [in] Column index (0-3)

Returns:
Reference to matrix element at specified row and column

inlineXMatrix44 <T >&operator*=(constT &s)

Scalar multiplication assignment operator.
Parameters:
s – [in] Scalar value to multiply all elements with

Returns:
Reference to this matrix after scalar multiplication

inlinevoidMatrixMultiply(constT*__restrictlhs,constT*__restrictrhs,T*__restrictresult)const
Performs matrix multiplication of two 4x4 matrices.
Computes result = lhs * rhs using column-major storage
Parameters:

- lhs – [in] Left-hand side matrix (as array of 16 elements)

- rhs – [in] Right-hand side matrix (as array of 16 elements)

- result – [out] Output matrix (as array of 16 elements)

Pre:
lhs, rhs, and result must point to different memory locations

inlinevoidSetCol(intindex, constVec4 &c)

Sets a column of the matrix to the specified 4D vector.
Parameters:

- index – [in] Column index (0-3)

- c – [in] 4D vector to set as the column

inlinevoidSetAxis(uint32_tindex, constXVector3 <T >&a)

Sets a column of the matrix to the specified 3D vector (w=0)
Parameters:

- index – [in] Column index (0-3)

- a – [in] 3D vector to set as the column (w component set to 0)

inlinevoidSetTranslation(constPoint3 &p)

Sets the translation column (fourth column) of the matrix.
Parameters:
p – [in] 3D point representing the translation

inlineconstVec3 &GetAxis(inti)const

Gets a column as a 3D vector (ignoring w component)
Parameters:
i – [in] Column index (0-3)

Returns:
Const reference to 3D vector representing the column

inlineconstVec4 &GetCol(inti)const

Gets a column as a 4D vector.
Parameters:
i – [in] Column index (0-3)

Returns:
Const reference to 4D vector representing the column

inlineconstPoint3 &GetTranslation()const

Gets the translation from the matrix (fourth column as 3D point)
Returns:
Const reference to 3D point representing the translation

inlineVec4 GetRow(inti)const

Gets a row of the matrix as a 4D vector.
Parameters:
i – [in] Row index (0-3)

Returns:
4D vector representing the row

Public Members
T columns[4][4]

Matrix data stored as column vectors in column-major order.
columns[i][j] represents element at row j, column i

Public Static Functions
staticinlineXMatrix44 Identity()

Creates and returns an identity matrix.
Returns:
4x4 identity matrix
