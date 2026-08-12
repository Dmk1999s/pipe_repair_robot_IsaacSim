<!-- source: py/api/class_x_vector4.html | title: XVector4 — Isaac Sim -->

# XVector4
template<typenameT>
classXVector4

Template class representing a 4-dimensional vector with x, y, z, and w components.
A template-based 4D vector class that provides basic vector operations including arithmetic operations, comparisons, and type conversions. This class is commonly used for homogeneous coordinates in 3D graphics and mathematical computations.
Note
This class includes validation macros in debug builds to ensure finite values
Template Parameters:
T – The numeric type for vector components (typically float or double)

Public Types
typedefT value_type

Type alias for the template parameter T.

Public Functions
inlineXVector4()

Default constructor initializes all components to zero.

inlineXVector4(T a)

Constructor that initializes all components to the same value.
Parameters:
a – [in] Value to assign to all components

inlineXVector4(constT *p)

Constructor that initializes components from an array.
Parameters:
p – [in] Pointer to array of at least 4 elements

inlineXVector4(T x_, T y_, T z_, T w_=1.0f)

Constructor that initializes components with specific values.
Parameters:

- x_ – [in] X component value

- y_ – [in] Y component value

- z_ – [in] Z component value

- w_ – [in] W component value (defaults to 1.0f)

inlineXVector4(constVec3 &v, floatw)

Constructor that creates a 4D vector from a 3D vector and w component.
Parameters:

- v – [in] 3D vector for x, y, z components

- w – [in] W component value

inlineoperatorT *()

Conversion operator to non-const pointer to components.
Returns:
Pointer to the first component (x)

inlineoperatorconstT *()const

Conversion operator to const pointer to components.
Returns:
Const pointer to the first component (x)

inlinevoidSet(T x_, T y_, T z_, T w_)

Sets all four components of the vector.
Parameters:

- x_ – [in] New x component value

- y_ – [in] New y component value

- z_ – [in] New z component value

- w_ – [in] New w component value

inlineXVector4 <T >operator*(T scale)const

Scalar multiplication operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
New vector with each component multiplied by scale

inlineXVector4 <T >operator/(T scale)const

Scalar division operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
New vector with each component divided by scale

inlineXVector4 <T >operator+(constXVector4 <T >&v)const

Vector addition operator.
Parameters:
v – [in] Vector to add

Returns:
New vector that is the sum of this vector and v

inlineXVector4 <T >operator-(constXVector4 <T >&v)const

Vector subtraction operator.
Parameters:
v – [in] Vector to subtract

Returns:
New vector that is the difference of this vector and v

inlineXVector4 <T >operator*(XVector4 <T >scale)const

Component-wise vector multiplication operator.
Parameters:
scale – [in] Vector to multiply component-wise

Returns:
New vector with components multiplied element-wise

inlineXVector4 <T >&operator*=(T scale)

Scalar multiplication assignment operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
Reference to this vector after multiplication

inlineXVector4 <T >&operator/=(T scale)

Scalar division assignment operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
Reference to this vector after division

inlineXVector4 <T >&operator+=(constXVector4 <T >&v)

Vector addition assignment operator.
Parameters:
v – [in] Vector to add

Returns:
Reference to this vector after addition

inlineXVector4 <T >&operator-=(constXVector4 <T >&v)

Vector subtraction assignment operator.
Parameters:
v – [in] Vector to subtract

Returns:
Reference to this vector after subtraction

inlineXVector4 <T >&operator*=(constXVector4 <T >&v)

Component-wise vector multiplication assignment operator.
Parameters:
v – [in] Vector to multiply component-wise

Returns:
Reference to this vector after component-wise multiplication

inlinebooloperator!=(constXVector4 <T >&v)const

Inequality comparison operator.
Parameters:
v – [in] Vector to compare with

Returns:
True if any component differs, false if all components are equal

inlineXVector4 <T >operator-()const

Unary negation operator.
Returns:
New vector with all components negated

Public Members
T x

X component of the vector.

T y

Y component of the vector.

T z

Z component of the vector.

T w

W component of the vector.
