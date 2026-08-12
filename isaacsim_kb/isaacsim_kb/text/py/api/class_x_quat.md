<!-- source: py/api/class_x_quat.html | title: XQuat — Isaac Sim -->

# XQuat
template<typenameT>
classXQuat

Template class representing a quaternion with x, y, z, and w components.
A template-based quaternion class that provides quaternion operations including arithmetic operations, rotations, and conversions. Quaternions are commonly used for representing rotations in 3D space without gimbal lock issues.
The quaternion is stored as (x, y, z, w) where (x, y, z) represents the vector part and w represents the scalar part.
Note
This class follows the Hamilton convention for quaternion multiplication
Template Parameters:
T – The numeric type for quaternion components (typically float or double)

Public Types
typedefT value_type

Type alias for the template parameter T.

Public Functions
inlineXQuat()

Default constructor creates identity quaternion (0, 0, 0, 1)

inlineXQuat(constT *p)

Constructor that initializes components from an array.
Parameters:
p – [in] Pointer to array of at least 4 elements in order [x, y, z, w]

inlineXQuat(T x_, T y_, T z_, T w_)

Constructor that initializes components with specific values.
Parameters:

- x_ – [in] X component (i part)

- y_ – [in] Y component (j part)

- z_ – [in] Z component (k part)

- w_ – [in] W component (scalar part)

inlineXQuat(constVec3 &v, floatw)

Constructor that creates quaternion from vector and scalar parts.
Parameters:

- v – [in] Vector part containing x, y, z components

- w – [in] Scalar part (w component)

inlineexplicitXQuat(constMatrix33 &m)

Constructor that creates quaternion from rotation matrix.
Constructor creating a quaternion from a rotation matrix.
Converts a 3x3 rotation matrix to a quaternion using Shepperd’s method. The algorithm selects the most numerically stable computation path based on the trace and diagonal elements of the matrix.
Parameters:

- m – [in] 3x3 rotation matrix to convert

- m – [in]Rotation matrix to convert to quaternion

Template Parameters:
T – Template type parameter for the quaternion components

inlineoperatorT *()

Conversion operator to non-const pointer to components.
Returns:
Pointer to the first component (x)

inlineoperatorconstT *()const

Conversion operator to const pointer to components.
Returns:
Const pointer to the first component (x)

inlinevoidSet(T x_, T y_, T z_, T w_)

Sets all four components of the quaternion.
Parameters:

- x_ – [in] New x component value

- y_ – [in] New y component value

- z_ – [in] New z component value

- w_ – [in] New w component value

inlineXQuat <T >operator*(T scale)const

Scalar multiplication operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
New quaternion with each component multiplied by scale

inlineXQuat <T >operator/(T scale)const

Scalar division operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
New quaternion with each component divided by scale

inlineXQuat <T >operator+(constXQuat <T >&v)const

Quaternion addition operator.
Parameters:
v – [in] Quaternion to add

Returns:
New quaternion that is the sum of this quaternion and v

inlineXQuat <T >operator-(constXQuat <T >&v)const

Quaternion subtraction operator.
Parameters:
v – [in] Quaternion to subtract

Returns:
New quaternion that is the difference of this quaternion and v

inlineXQuat <T >operator*(XQuat <T >q)const

Quaternion multiplication operator (Hamilton product)
Performs quaternion multiplication following Hamilton convention
Parameters:
q – [in] Quaternion to multiply with

Returns:
New quaternion that is the Hamilton product of this quaternion and q

inlineXQuat <T >&operator*=(T scale)

Scalar multiplication assignment operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
Reference to this quaternion after multiplication

inlineXQuat <T >&operator/=(T scale)

Scalar division assignment operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
Reference to this quaternion after division

inlineXQuat <T >&operator+=(constXQuat <T >&v)

Quaternion addition assignment operator.
Parameters:
v – [in] Quaternion to add

Returns:
Reference to this quaternion after addition

inlineXQuat <T >&operator-=(constXQuat <T >&v)

Quaternion subtraction assignment operator.
Parameters:
v – [in] Quaternion to subtract

Returns:
Reference to this quaternion after subtraction

inlinebooloperator!=(constXQuat <T >&v)const

Inequality comparison operator.
Parameters:
v – [in] Quaternion to compare with

Returns:
True if any component differs, false if all components are equal

inlineXQuat <T >operator-()const

Unary negation operator.
Returns:
New quaternion with all components negated

inlineXVector3 <T >GetAxis()const

Gets the vector part of the quaternion.
Returns:
3D vector containing the x, y, z components

Public Members
T x

X component of the quaternion (i part)

T y

Y component of the quaternion (j part)

T z

Z component of the quaternion (k part)

T w

W component of the quaternion (scalar part)
