<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a8c5f8a72f4ed9cfb126cedd1dbb08908.html | title: rotate — Isaac Sim -->

# rotate
Fully qualified name: `isaacsim::core::includes::math::rotate`
inlinecarb::Float3isaacsim ::core ::includes ::math ::rotate(
constcarb::Float4&q,
constcarb::Float3x,
)
Rotates a vector by a quaternion.
Applies a quaternion rotation to a 3D vector. Uses the quaternion sandwich product: q * v * q^(-1)
Note
Assumes input quaternion is normalized
Parameters:

- q – [in]Rotation quaternion (must be normalized)

- x – [in] Vector to rotate

Returns:
carb::Float3 Rotated vector
