<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a0709ae30fef099fea0c9683d7a740854.html | title: getBasisVectorX — Isaac Sim -->

# getBasisVectorX
Fully qualified name: `isaacsim::core::includes::math::getBasisVectorX`
inlinecarb::Float3isaacsim ::core ::includes ::math ::getBasisVectorX(
constcarb::Float4&q,
)
Gets the X basis vector from a rotation quaternion.
Extracts the local X axis direction after applying the rotation. Equivalent to rotating the world X axis (1,0,0) by the quaternion.
Note
Assumes input quaternion is normalized
Parameters:
q – [in]Rotation quaternion (must be normalized)

Returns:
carb::Float3 The rotated X basis vector
