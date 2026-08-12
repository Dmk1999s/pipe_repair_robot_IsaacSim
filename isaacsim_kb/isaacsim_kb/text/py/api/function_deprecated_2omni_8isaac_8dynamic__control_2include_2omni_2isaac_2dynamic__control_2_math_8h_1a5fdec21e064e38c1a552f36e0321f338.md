<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_math_8h_1a5fdec21e064e38c1a552f36e0321f338.html | title: inverse — Isaac Sim -->

# inverse
Fully qualified name: `omni::isaac::dynamic_control::math::inverse`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::math ::inverse(
constomni ::isaac ::dynamic_control ::DcTransform &transform,
)
Computes the inverse of a transform.
Calculates the inverse transform that, when applied after the original, results in the identity transform.
Note
For a valid transform T, T * inverse(T) equals the identity transform
Parameters:
transform – [in]Transform to invert

Returns:
DcTransform The inverse transform
