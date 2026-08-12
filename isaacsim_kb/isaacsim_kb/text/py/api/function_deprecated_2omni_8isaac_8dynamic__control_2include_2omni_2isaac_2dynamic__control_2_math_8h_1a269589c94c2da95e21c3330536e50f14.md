<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_math_8h_1a269589c94c2da95e21c3330536e50f14.html | title: slerp — Isaac Sim -->

# slerp
Fully qualified name: `omni::isaac::dynamic_control::math::slerp`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::math ::slerp(
constomni ::isaac ::dynamic_control ::DcTransform &a,
constomni ::isaac ::dynamic_control ::DcTransform &b,
constfloatt,
)
Performs spherical linear interpolation between transforms.
Interpolates position linearly and rotation using slerp. This provides smoother rotation interpolation than regular lerp.
Parameters:

- a – [in] Starting transform

- b – [in] Ending transform

- t – [in] Interpolation parameter [0,1]

Returns:
DcTransform The interpolated transform
