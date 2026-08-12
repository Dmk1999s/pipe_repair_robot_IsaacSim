<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a9db5b2694357d04664098daafcd7163c.html | title: lerp — Isaac Sim -->

# lerp
Fully qualified name: `isaacsim::core::includes::math::lerp`
inlinecarb::Float3isaacsim ::core ::includes ::math ::lerp(
constcarb::Float3&start,
constcarb::Float3&end,
constfloatt,
)
Linearly interpolates between two 3D vectors.
Performs linear interpolation between start and end vectors. The parameter t controls the interpolation: 0 returns start, 1 returns end.
Note
For values of t outside [0,1], extrapolation is performed
Parameters:

- start – [in] Starting vector

- end – [in] Ending vector

- t – [in] Interpolation parameter [0,1]

Returns:
carb::Float3 The interpolated vector
