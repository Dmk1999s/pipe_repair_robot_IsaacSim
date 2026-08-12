<!-- source: py/api/class_x_vector3.html | title: XVector3 — Isaac Sim -->

# XVector3
template<typenameT=float>
classXVector3

Template class representing a 3-dimensional vector with x, y, and z components.
A template-based 3D vector class that provides basic vector operations including arithmetic operations, comparisons, and type conversions. This class is commonly used for 3D coordinates, directions, and mathematical computations in graphics and physics applications.
Note
This class includes validation macros in debug builds to ensure finite values
Template Parameters:
T – The numeric type for vector components (defaults to float)

Public Types
typedefT value_type

Type alias for the template parameter T.

Public Functions
inlineXVector3()

Default constructor initializes all components to zero.

inlineXVector3(T a)

Constructor that initializes all components to the same value.
Parameters:
a – [in] Value to assign to all components

inlineXVector3(constT *p)

Constructor that initializes components from an array.
Parameters:
p – [in] Pointer to array of at least 3 elements

inlineXVector3(T x_, T y_, T z_)

Constructor that initializes components with specific values.
Parameters:

- x_ – [in] X component value

- y_ – [in] Y component value

- z_ – [in] Z component value

inlineoperatorT *()

Conversion operator to non-const pointer to components.
Returns:
Pointer to the first component (x)

inlineoperatorconstT *()const

Conversion operator to const pointer to components.
Returns:
Const pointer to the first component (x)

inlinevoidSet(T x_, T y_, T z_)

Sets all three components of the vector.
Parameters:

- x_ – [in] New x component value

- y_ – [in] New y component value

- z_ – [in] New z component value

inlineXVector3 <T >operator*(T scale)const

Scalar multiplication operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
New vector with each component multiplied by scale

inlineXVector3 <T >operator/(T scale)const

Scalar division operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
New vector with each component divided by scale

inlineXVector3 <T >operator+(constXVector3 <T >&v)const

Vector addition operator.
Parameters:
v – [in] Vector to add

Returns:
New vector that is the sum of this vector and v

inlineXVector3 <T >operator-(constXVector3 <T >&v)const

Vector subtraction operator.
Parameters:
v – [in] Vector to subtract

Returns:
New vector that is the difference of this vector and v

inlineXVector3 <T >operator/(constXVector3 <T >&v)const

Component-wise vector division operator.
Parameters:
v – [in] Vector to divide by component-wise

Returns:
New vector with components divided element-wise

inlineXVector3 <T >operator*(constXVector3 <T >&v)const

Component-wise vector multiplication operator.
Parameters:
v – [in] Vector to multiply component-wise

Returns:
New vector with components multiplied element-wise

inlineXVector3 <T >&operator*=(T scale)

Scalar multiplication assignment operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
Reference to this vector after multiplication

inlineXVector3 <T >&operator/=(T scale)

Scalar division assignment operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
Reference to this vector after division

inlineXVector3 <T >&operator+=(constXVector3 <T >&v)

Vector addition assignment operator.
Parameters:
v – [in] Vector to add

Returns:
Reference to this vector after addition

inlineXVector3 <T >&operator-=(constXVector3 <T >&v)

Vector subtraction assignment operator.
Parameters:
v – [in] Vector to subtract

Returns:
Reference to this vector after subtraction

inlineXVector3 <T >&operator/=(constXVector3 <T >&v)

Component-wise vector division assignment operator.
Parameters:
v – [in] Vector to divide by component-wise

Returns:
Reference to this vector after component-wise division

inlineXVector3 <T >&operator*=(constXVector3 <T >&v)

Component-wise vector multiplication assignment operator.
Parameters:
v – [in] Vector to multiply component-wise

Returns:
Reference to this vector after component-wise multiplication

inlinebooloperator!=(constXVector3 <T >&v)const

Inequality comparison operator.
Parameters:
v – [in] Vector to compare with

Returns:
True if any component differs, false if all components are equal

inlineXVector3 <T >operator-()const

Unary negation operator.
Returns:
New vector with all components negated

inlinevoidValidate()

Validates vector components for finite values.
Calls internal validation macro to check for NaN and infinite values

Public Members
T x

X component of the vector.

T y

Y component of the vector.

T z

Z component of the vector.
