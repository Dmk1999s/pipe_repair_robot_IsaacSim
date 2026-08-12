<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a64bca8ffa62046fac981eeaafa6b609b.html | title: asGfMatrix4d — Isaac Sim -->

# asGfMatrix4d
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfMatrix4d`
inlinepxr ::GfMatrix4domni ::isaac ::dynamic_control ::conversions ::asGfMatrix4d(
constomni ::isaac ::dynamic_control ::DcTransform &input,
)
Converts a DcTransform to a GfMatrix4d.
Creates a 4x4 transformation matrix in double precision:

- Sets translation component with precision promotion

- Sets rotation component with precision promotion

See also
asGfVec3d
See also
asGfQuatd
Note
Promotes single precision components to double precision
Parameters:
input – [in] Input transform in Dynamic Control format

Returns:
pxr::GfMatrix4d Equivalent transform matrix in USD format
