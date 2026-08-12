<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_math_8h_1afaea7ee04f2f4fda37537a34c7efbaa9.html | title: lerp — Isaac Sim -->

# lerp
Fully qualified name: `omni::isaac::dynamic_control::math::lerp`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::math ::lerp(
constomni ::isaac ::dynamic_control ::DcTransform &a,
constomni ::isaac ::dynamic_control ::DcTransform &b,
constfloatt,
)
Linearly interpolates between two transforms.
Performs separate linear interpolation on position and rotation components. Position uses vector lerp, rotation uses quaternion lerp.
Parameters:

- a – [in] Starting transform

- b – [in] Ending transform

- t – [in] Interpolation parameter [0,1]

Returns:
DcTransform The interpolated transform
