<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a2ce0eb0cf0afddbee8e50ad28a5dbacc.html | title: operator* — Isaac Sim -->

# operator*
Fully qualified name: `isaacsim::core::includes::math::operator*`
inlinecarb::Float4isaacsim ::core ::includes ::math ::operator*(
constcarb::Float4&a,
constcarb::Float4&b,
)
Performs quaternion multiplication.
Implements the Hamilton product for quaternions, representing 3D rotation composition. The order of multiplication matters (non-commutative).
Note
The resulting rotation is b followed by a
Parameters:

- a – [in] First quaternion (applied second)

- b – [in] Second quaternion (applied first)

Returns:
carb::Float4 The resulting quaternion
