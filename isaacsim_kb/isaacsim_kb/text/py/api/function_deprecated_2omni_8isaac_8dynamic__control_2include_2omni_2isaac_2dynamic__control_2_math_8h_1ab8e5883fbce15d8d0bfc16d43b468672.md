<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_math_8h_1ab8e5883fbce15d8d0bfc16d43b468672.html | title: transformInv — Isaac Sim -->

# transformInv
Fully qualified name: `omni::isaac::dynamic_control::math::transformInv`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::math ::transformInv(
constomni ::isaac ::dynamic_control ::DcTransform &a,
constomni ::isaac ::dynamic_control ::DcTransform &b,
)
Computes the relative transform from a to b.
Calculates the transform that, when applied to a, results in b. This is equivalent to inverse(a) * b.
Parameters:

- a – [in] Reference transform

- b – [in] Target transform

Returns:
DcTransform Transform from a to b
