<!-- source: py/api/class_x_matrix.html | title: XMatrix — Isaac Sim -->

# XMatrix
template<intm,intn,typenameT=double>
classXMatrix

Template class representing an m×n matrix with column-major storage.
A template-based matrix class that provides basic matrix operations including arithmetic operations, element access, and matrix transformations. The matrix uses column-major storage order for compatibility with linear algebra libraries.
Note
Matrix elements are stored in column-major order: data[column][row]
Template Parameters:

- m – Number of rows in the matrix

- n – Number of columns in the matrix

- T – Numeric type for matrix elements (defaults to double)

Public Functions
inlineXMatrix()

Default constructor initializes all elements to zero.

inlineXMatrix(constXMatrix <m ,n >&a)

Copy constructor creates matrix from another matrix.
Parameters:
a – [in] Source matrix to copy from

template<typenameOtherT>
inlineXMatrix(constOtherT *ptr)

Constructor that initializes matrix from pointer to data.
Parameters:
ptr – [in] Pointer to array of m×n elements in row-major order

Template Parameters:
OtherT – Type of source data (automatically converted to T)

inlineconstXMatrix <m ,n >&operator=(constXMatrix <m ,n >&a)

Assignment operator copies data from another matrix.
Parameters:
a – [in] Source matrix to copy from

Returns:
Reference to this matrix after assignment

template<typenameOtherT>
inlinevoidSetCol(
intj,
constXMatrix <m ,1,OtherT >&c,
)
Sets a column of the matrix to the specified column vector.
Parameters:

- j – [in] Column index (0 to n-1)

- c – [in] Column vector of size m×1 to set

Template Parameters:
OtherT – Type of source column vector elements

template<typenameOtherT>
inlinevoidSetRow(
inti,
constXMatrix <1,n ,OtherT >&r,
)
Sets a row of the matrix to the specified row vector.
Parameters:

- i – [in] Row index (0 to m-1)

- r – [in] Row vector of size 1×n to set

Template Parameters:
OtherT – Type of source row vector elements

inlineT &operator()(introw, intcol)

Element access operator (non-const version)
Parameters:

- row – [in] Row index (0 to m-1)

- col – [in] Column index (0 to n-1)

Returns:
Reference to matrix element at specified position

inlineconstT &operator()(introw, intcol)const

Element access operator (const version)
Parameters:

- row – [in] Row index (0 to m-1)

- col – [in] Column index (0 to n-1)

Returns:
Const reference to matrix element at specified position

inlinevoidSetIdentity()

Sets the matrix to identity matrix.
Sets diagonal elements to 1.0 and off-diagonal elements to 0.0
Note
Only valid for square matrices (m == n)

Public Members
T data[n ][m ]

Matrix data stored in column-major order.
data[column][row] accesses element at specified row and column
