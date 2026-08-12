<!-- source: py/api/class_plane.html | title: Plane — Isaac Sim -->

# Plane
classPlane:publicXVector4 <float>

3D plane representation in the form ax + by + cz + d = 0.
This class represents a 3D plane using the implicit equation ax + by + cz + d = 0, where (a, b, c) is the plane normal and d is the distance from origin. It inherits from Vec4 where x, y, z represent the normal components and w represents -d.
Public Types
typedeffloatvalue_type

Type alias for the template parameter T.

Public Functions
inlinePlane()

Default constructor creating an uninitialized plane.

inlinePlane(floatx, floaty, floatz, floatw)

Constructor from plane equation coefficients.
Parameters:

- x – [in] Normal x-component (coefficient a)

- y – [in] Normal y-component (coefficient b)

- z – [in] Normal z-component (coefficient c)

- w – [in] Negative distance from origin (coefficient d)

inlinePlane(constVec3 &p, constVector3 &n)

Constructor from point on plane and normal vector.
Parameters:

- p – [in] A point lying on the plane

- n – [in] Normal vector to the plane

inlineVec3 GetNormal()const

Gets the normal vector of the plane.
Returns:
The plane’s normal vector

inlineVec3 GetPoint()const

Gets a point on the plane closest to the origin.
Returns:
A point on the plane

inlinePlane(constVec3 &v)

Constructor from Vec3 (assumes w=1).
Parameters:
v – [in] Vector containing normal components

inlinePlane(constVec4 &v)

Constructor from Vec4.
Parameters:
v – [in] Vector containing plane equation coefficients

inlineoperatorfloat*()

Conversion operator to non-const pointer to components.
Returns:
Pointer to the first component (x)

inlineoperatorconstfloat*()const

Conversion operator to const pointer to components.
Returns:
Const pointer to the first component (x)

inlinevoidSet(floatx_, floaty_, floatz_, floatw_)

Sets all four components of the vector.
Parameters:

- x_ – [in] New x component value

- y_ – [in] New y component value

- z_ – [in] New z component value

- w_ – [in] New w component value

inlineXVector4 <float>operator*(floatscale)const

Scalar multiplication operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
New vector with each component multiplied by scale

inlineXVector4 <float>operator*(XVector4 <float>scale)const

Component-wise vector multiplication operator.
Parameters:
scale – [in] Vector to multiply component-wise

Returns:
New vector with components multiplied element-wise

inlineXVector4 <float>operator/(floatscale)const

Scalar division operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
New vector with each component divided by scale

inlineXVector4 <float>operator+(constXVector4 <float>&v)const

Vector addition operator.
Parameters:
v – [in] Vector to add

Returns:
New vector that is the sum of this vector and v

inlineXVector4 <float>operator-(constXVector4 <float>&v)const

Vector subtraction operator.
Parameters:
v – [in] Vector to subtract

Returns:
New vector that is the difference of this vector and v

inlineXVector4 <float>operator-()const

Unary negation operator.
Returns:
New vector with all components negated

inlineXVector4 <float>&operator*=(floatscale)

Scalar multiplication assignment operator.
Parameters:
scale – [in] Scalar value to multiply with

Returns:
Reference to this vector after multiplication

inlineXVector4 <float>&operator*=(constXVector4 <float>&v)

Component-wise vector multiplication assignment operator.
Parameters:
v – [in] Vector to multiply component-wise

Returns:
Reference to this vector after component-wise multiplication

inlineXVector4 <float>&operator/=(floatscale)

Scalar division assignment operator.
Parameters:
scale – [in] Scalar value to divide by

Returns:
Reference to this vector after division

inlineXVector4 <float>&operator+=(constXVector4 <float>&v)

Vector addition assignment operator.
Parameters:
v – [in] Vector to add

Returns:
Reference to this vector after addition

inlineXVector4 <float>&operator-=(constXVector4 <float>&v)

Vector subtraction assignment operator.
Parameters:
v – [in] Vector to subtract

Returns:
Reference to this vector after subtraction

inlinebooloperator!=(constXVector4 <float>&v)const

Inequality comparison operator.
Parameters:
v – [in] Vector to compare with

Returns:
True if any component differs, false if all components are equal

Public Members
floatx

X component of the vector.

floaty

Y component of the vector.

floatz

Z component of the vector.

floatw

W component of the vector.
