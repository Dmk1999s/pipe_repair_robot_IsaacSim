<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a96325b5230dfc7c7b47532050981ee99.html | title: inverse — Isaac Sim -->

# inverse
Fully qualified name: `isaacsim::core::includes::math::inverse`
inlinecarb::Float4isaacsim ::core ::includes ::math ::inverse(
constcarb::Float4&q,
)
Computes the inverse of a quaternion.
For unit quaternions, the inverse is equal to the conjugate. This function assumes the input quaternion is normalized.
Note
Assumes input quaternion is normalized
Parameters:
q – [in] Input quaternion

Returns:
carb::Float4 The inverse quaternion
