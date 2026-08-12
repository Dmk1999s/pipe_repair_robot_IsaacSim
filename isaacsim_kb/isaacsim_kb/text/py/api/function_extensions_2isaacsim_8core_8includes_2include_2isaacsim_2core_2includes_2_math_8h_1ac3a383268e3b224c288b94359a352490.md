<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1ac3a383268e3b224c288b94359a352490.html | title: slerp — Isaac Sim -->

# slerp
Fully qualified name: `isaacsim::core::includes::math::slerp`
inlinecarb::Float4isaacsim ::core ::includes ::math ::slerp(
constcarb::Float4&start,
constcarb::Float4&end,
constfloatt,
)
Performs spherical linear interpolation between quaternions.
Interpolates along the shortest arc on the quaternion sphere. Maintains constant angular velocity throughout the interpolation.
Note
Both input quaternions must be normalized
Warning
May be unstable for angles close to 180 degrees
Parameters:

- start – [in] Starting quaternion (must be normalized)

- end – [in] Ending quaternion (must be normalized)

- t – [in] Interpolation parameter [0,1]

Returns:
carb::Float4 The interpolated quaternion
