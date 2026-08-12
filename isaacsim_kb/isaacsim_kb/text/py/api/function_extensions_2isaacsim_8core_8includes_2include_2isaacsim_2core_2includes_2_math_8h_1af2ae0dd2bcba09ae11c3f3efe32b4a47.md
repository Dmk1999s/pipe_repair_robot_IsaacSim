<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1af2ae0dd2bcba09ae11c3f3efe32b4a47.html | title: getBasisVectorZ — Isaac Sim -->

# getBasisVectorZ
Fully qualified name: `isaacsim::core::includes::math::getBasisVectorZ`
inlinecarb::Float3isaacsim ::core ::includes ::math ::getBasisVectorZ(
constcarb::Float4&q,
)
Gets the Z basis vector from a rotation quaternion.
Extracts the local Z axis direction after applying the rotation. Equivalent to rotating the world Z axis (0,0,1) by the quaternion.
Note
Assumes input quaternion is normalized
Parameters:
q – [in]Rotation quaternion (must be normalized)

Returns:
carb::Float3 The rotated Z basis vector
