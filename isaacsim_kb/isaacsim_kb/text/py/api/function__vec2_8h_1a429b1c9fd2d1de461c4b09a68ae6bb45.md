<!-- source: py/api/function__vec2_8h_1a429b1c9fd2d1de461c4b09a68ae6bb45.html | title: operator* — Isaac Sim -->

# operator*
template<typenameT>
XVector2 <T >operator*(
T lhs,
constXVector2 <T >&rhs,
)
Scales a vector by a scalar value (left-hand side scalar).
Template Parameters:
T – The component type of the vector.

Parameters:

- lhs – [in] The scalar multiplier.

- rhs – [in] The vector to scale.

Returns:
A new XVector2 representing the scaled vector.
