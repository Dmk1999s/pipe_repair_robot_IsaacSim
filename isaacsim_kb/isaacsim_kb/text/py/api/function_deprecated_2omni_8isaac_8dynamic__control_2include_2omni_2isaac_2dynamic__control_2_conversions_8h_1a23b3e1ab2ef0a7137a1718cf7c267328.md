<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a23b3e1ab2ef0a7137a1718cf7c267328.html | title: asDcTransform — Isaac Sim -->

# asDcTransform
Fully qualified name: `omni::isaac::dynamic_control::conversions::asDcTransform`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::conversions ::asDcTransform(
constpxr ::GfVec3f&p,
constpxr ::GfQuatf&q,
)
Converts USD position and orientation into Dynamic Control transform.
Creates a Dynamic Control transform from separate components:

- Converts position vector to Float3

- Converts orientation quaternion to Float4

See also
asCarbFloat3
See also
asCarbFloat4
Note
No precision loss when using single precision USD types
Parameters:

- p – [in] Position vector in USD format

- q – [in]Rotation quaternion in USD format

Returns:
omni::isaac::dynamic_control::DcTransform Equivalent transform in Dynamic Control format
