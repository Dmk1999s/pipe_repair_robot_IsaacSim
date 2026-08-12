<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1abf5dca0983934b0fec2dc534657ff37d.html | title: asPxTransform — Isaac Sim -->

# asPxTransform
Fully qualified name: `omni::isaac::dynamic_control::conversions::asPxTransform`
inline::physx ::PxTransformomni ::isaac ::dynamic_control ::conversions ::asPxTransform(
constomni ::isaac ::dynamic_control ::DcTransform &pose,
)
Converts DcTransform into PhysX transform.
Creates a complete PhysX transform from Dynamic Control transform:

- Converts position to PxVec3

- Converts rotation to PxQuat

See also
asPxVec3
See also
asPxQuat
Note
No precision loss as both formats use single precision
Parameters:
pose – [in] Input transform in Dynamic Control format

Returns:
PxTransform Equivalent transform in PhysX format
