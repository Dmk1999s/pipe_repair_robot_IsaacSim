<!-- source: py/api/class_point3.html | title: Point3 — Isaac Sim -->

# Point3
classPoint3

Represents a 3D point in space with floating-point coordinates.
The Point3 class provides a complete set of operations for working with 3D points, including arithmetic operations, conversions, and validation. Points are distinct from vectors in that they represent positions rather than directions or displacements.
Public Functions
inlinePoint3()

Default constructor that initializes the point to the origin (0, 0, 0).

inlinePoint3(floata)

Constructor that initializes all components to the same value.
Parameters:
a – [in] The value to set for all three components (x, y, z).

inlinePoint3(constfloat*p)

Constructor that initializes from a float array.
Warning
The caller must ensure the array has at least 3 elements.
Parameters:
p – [in] Pointer to an array of at least 3 floats [x, y, z].

inlinePoint3(floatx_, floaty_, floatz_)

Constructor that initializes from individual component values.
Parameters:

- x_ – [in] The x-coordinate of the point.

- y_ – [in] The y-coordinate of the point.

- z_ – [in] The z-coordinate of the point.

inlineexplicitPoint3(constVec3 &v)

Explicit constructor from a Vec3 vector.
This conversion treats the vector components as position coordinates.
Parameters:
v – [in] The vector to convert to a point.

inlineoperatorfloat*()

Conversion operator to a mutable float pointer.
Returns:
Pointer to the first component (x) for array-style access.

inlineoperatorconstfloat*()const

Conversion operator to a const float pointer.
Returns:
Const pointer to the first component (x) for array-style access.

inlineoperatorVec4 ()const

Conversion operator to a homogeneous Vec4.
Returns:
Vec4 with (x, y, z, 1.0) representing the point in homogeneous coordinates.

inlinevoidSet(floatx_, floaty_, floatz_)

Sets the coordinates of the point.
Parameters:

- x_ – [in] The new x-coordinate.

- y_ – [in] The new y-coordinate.

- z_ – [in] The new z-coordinate.

inlinePoint3 operator*(floatscale)const

Scales the point by a scalar value.
Parameters:
scale – [in] The scaling factor to apply to all components.

Returns:
A new Point3 representing the scaled point.

inlinePoint3 operator/(floatscale)const

Divides the point by a scalar value.
Warning
Division by zero will result in undefined behavior.
Parameters:
scale – [in] The divisor to apply to all components.

Returns:
A new Point3 representing the divided point.

inlinePoint3 operator+(constVec3 &v)const

Translates the point by a vector.
Parameters:
v – [in] The translation vector to add.

Returns:
A new Point3 representing the translated point.

inlinePoint3 operator-(constVec3 &v)const

Translates the point by the negative of a vector.
Parameters:
v – [in] The translation vector to subtract.

Returns:
A new Point3 representing the translated point.

inlinePoint3 &operator*=(floatscale)

Scales this point by a scalar value in-place.
Parameters:
scale – [in] The scaling factor to apply to all components.

Returns:
Reference to this point after scaling.

inlinePoint3 &operator/=(floatscale)

Divides this point by a scalar value in-place.
Warning
Division by zero will result in undefined behavior.
Parameters:
scale – [in] The divisor to apply to all components.

Returns:
Reference to this point after division.

inlinePoint3 &operator+=(constVec3 &v)

Translates this point by a vector in-place.
Parameters:
v – [in] The translation vector to add.

Returns:
Reference to this point after translation.

inlinePoint3 &operator-=(constVec3 &v)

Translates this point by the negative of a vector in-place.
Parameters:
v – [in] The translation vector to subtract.

Returns:
Reference to this point after translation.

inlinePoint3 &operator=(constVec3 &v)

Assigns a Vec3 to this point.
Parameters:
v – [in] The vector whose components will be copied to this point.

Returns:
Reference to this point after assignment.

inlinebooloperator!=(constPoint3 &v)const

Tests for inequality with another point.
Parameters:
v – [in] The other point to compare against.

Returns:
True if any component differs, false if all components are equal.

inlinePoint3 operator-()const

Returns the negation of this point.
Returns:
A new Point3 with all components negated.

inlinevoidValidate()const

Validates the point’s components for correctness.
Currently performs no validation but serves as a placeholder for future checks.

Public Members
floatx

The x-coordinate of the point.

floaty

The y-coordinate of the point.

floatz

The z-coordinate of the point.
