<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1aa3dddc657f9f3bc45fa82a64cd171ee0.html | title: getBasisVectorY — Isaac Sim -->

# getBasisVectorY
Fully qualified name: `isaacsim::core::includes::math::getBasisVectorY`
inlinecarb::Float3isaacsim ::core ::includes ::math ::getBasisVectorY(
constcarb::Float4&q,
)
Gets the Y basis vector from a rotation quaternion.
Extracts the local Y axis direction after applying the rotation. Equivalent to rotating the world Y axis (0,1,0) by the quaternion.
Note
Assumes input quaternion is normalized
Parameters:
q – [in]Rotation quaternion (must be normalized)

Returns:
carb::Float3 The rotated Y basis vector
