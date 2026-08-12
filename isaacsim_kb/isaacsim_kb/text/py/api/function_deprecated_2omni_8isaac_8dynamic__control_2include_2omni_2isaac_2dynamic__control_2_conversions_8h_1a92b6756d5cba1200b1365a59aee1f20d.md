<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a92b6756d5cba1200b1365a59aee1f20d.html | title: asDcTransform — Isaac Sim -->

# asDcTransform
Fully qualified name: `omni::isaac::dynamic_control::conversions::asDcTransform`
inlineomni ::isaac ::dynamic_control ::DcTransform omni ::isaac ::dynamic_control ::conversions ::asDcTransform(
constpxr ::GfVec3d&p,
constpxr ::GfQuatd&q,
)
Converts USD double precision position and orientation into Dynamic Control transform.
Creates a Dynamic Control transform from separate components with precision demotion:

- Converts double precision position to Float3

- Converts double precision orientation to Float4

See also
asCarbFloat3
See also
asCarbFloat4
Warning
Potential precision loss during double to float conversion
Parameters:

- p – [in] Position vector in USD format (double precision)

- q – [in]Rotation quaternion in USD format (double precision)

Returns:
omni::isaac::dynamic_control::DcTransform Equivalent transform in Dynamic Control format
