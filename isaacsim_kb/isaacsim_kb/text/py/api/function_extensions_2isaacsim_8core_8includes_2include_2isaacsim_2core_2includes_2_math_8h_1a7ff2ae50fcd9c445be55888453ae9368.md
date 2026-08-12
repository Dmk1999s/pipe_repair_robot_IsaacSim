<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a7ff2ae50fcd9c445be55888453ae9368.html | title: normalize — Isaac Sim -->

# normalize
Fully qualified name: `isaacsim::core::includes::math::normalize`
inlinecarb::Float4isaacsim ::core ::includes ::math ::normalize(
constcarb::Float4&q,
)
Normalizes a quaternion to unit length.
Scales the quaternion so its magnitude becomes 1. Returns identity quaternion if input magnitude is 0.
Note
Returns identity quaternion (0,0,0,1) if input magnitude is 0
Parameters:
q – [in] Input quaternion

Returns:
carb::Float4 Normalized quaternion
