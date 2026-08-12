<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1af1e6eb6e261627db1b2c69bc66611b71.html | title: lerp — Isaac Sim -->

# lerp
Fully qualified name: `isaacsim::core::includes::math::lerp`
inlinecarb::Float4isaacsim ::core ::includes ::math ::lerp(
constcarb::Float4&start,
constcarb::Float4&end,
constfloatt,
)
Linearly interpolates between two quaternions.
Performs linear interpolation between start and end quaternions. Note that this does not maintain constant angular velocity.
Note
For better rotation interpolation, consider using slerp instead
Parameters:

- start – [in] Starting quaternion

- end – [in] Ending quaternion

- t – [in] Interpolation parameter [0,1]

Returns:
carb::Float4 The interpolated quaternion
