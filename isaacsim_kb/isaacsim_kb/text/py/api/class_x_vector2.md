<!-- source: py/api/class_x_vector2.html | title: XVector2 — Isaac Sim -->

# XVector2
template<typenameT>
classXVector2

A template class representing a 2D vector with templated component type.
XVector2 provides a complete set of vector operations including arithmetic, comparison, and conversion operators. The class includes debug validation for finite and non-NaN values when appropriate.
Template Parameters:
T – The numeric type of the vector components (typically float or double).

Public Types
typedefT value_type

Type definition for the component type.

Public Functions
inlineXVector2()

Default constructor that initializes both components to zero.

inlineXVector2(T _x)

Constructor that initializes both components to the same value.
Parameters:
_x – [in] The value to set for both x and y components.

inlineXVector2(T _x, T _y)

Constructor that initializes components from individual values.
Parameters:

- _x – [in] The x-component value.

- _y – [in] The y-component value.

inlineXVector2(constT *p)

Constructor that initializes from an array.
Warning
The caller must ensure the array has at least 2 elements.
Parameters:
p – [in] Pointer to an array of at least 2 elements [x, y].

template<typenameU>
inlineexplicitXVector2(
constXVector2 <U >&v,
)
Template copy constructor for type conversion.
Performs explicit type conversion between different numeric types.
Template Parameters:
U – The source component type.

Parameters:
v – [in] The vector to convert from.

inlineoperatorT *()

Conversion operator to a mutable pointer.
Returns:
Pointer to the first component for array-style access.

inlineoperatorconstT *()const

Conversion operator to a const pointer.
Returns:
Const pointer to the first component for array-style access.

inlinevoidSet(T x_, T y_)

Sets the vector components.
Parameters:

- x_ – [in] The new x-component value.

- y_ – [in] The new y-component value.

inlineXVector2 <T >operator*(T scale)const

Scales the vector by a scalar value.
Parameters:
scale – [in] The scaling factor to apply to both components.

Returns:
A new XVector2 representing the scaled vector.

inlineXVector2 <T >operator/(T scale)const

Divides the vector by a scalar value.
Warning
Division by zero will result in undefined behavior.
Parameters:
scale – [in] The divisor to apply to both components.

Returns:
A new XVector2 representing the divided vector.

inlineXVector2 <T >operator+(constXVector2 <T >&v)const

Adds two vectors component-wise.
Parameters:
v – [in] The vector to add.

Returns:
A new XVector2 representing the sum.

inlineXVector2 <T >operator-(constXVector2 <T >&v)const

Subtracts two vectors component-wise.
Parameters:
v – [in] The vector to subtract.

Returns:
A new XVector2 representing the difference.

inlineXVector2 <T >&operator*=(T scale)

Scales this vector by a scalar value in-place.
Parameters:
scale – [in] The scaling factor to apply to both components.

Returns:
Reference to this vector after scaling.

inlineXVector2 <T >&operator/=(T scale)

Divides this vector by a scalar value in-place.
Warning
Division by zero will result in undefined behavior.
Parameters:
scale – [in] The divisor to apply to both components.

Returns:
Reference to this vector after division.

inlineXVector2 <T >&operator+=(constXVector2 <T >&v)

Adds another vector to this vector in-place.
Parameters:
v – [in] The vector to add.

Returns:
Reference to this vector after addition.

inlineXVector2 <T >&operator-=(constXVector2 <T >&v)

Subtracts another vector from this vector in-place.
Parameters:
v – [in] The vector to subtract.

Returns:
Reference to this vector after subtraction.

inlineXVector2 <T >&operator*=(constXVector2 <T >&scale)

Multiplies this vector by another vector component-wise in-place.
Parameters:
scale – [in] The vector to multiply by.

Returns:
Reference to this vector after multiplication.

inlineXVector2 <T >operator-()const

Returns the negation of this vector.
Returns:
A new XVector2 with both components negated.

Public Members
T x

The x-component of the vector.

T y

The y-component of the vector.
