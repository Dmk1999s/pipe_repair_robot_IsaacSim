<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1ae6bc3e23dff87fcf76f3dc887eadcbf8.html | title: asGfMatrix4f — Isaac Sim -->

# asGfMatrix4f
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfMatrix4f`
inlinepxr ::GfMatrix4fomni ::isaac ::dynamic_control ::conversions ::asGfMatrix4f(
constomni ::isaac ::dynamic_control ::DcTransform &input,
)
Converts a DcTransform to a GfMatrix4f.
Creates a 4x4 transformation matrix in single precision:

- Sets translation component from position

- Sets rotation component from quaternion

See also
asGfVec3f
See also
asGfQuatf
Note
Uses single precision floating point
Parameters:
input – [in] Input transform in Dynamic Control format

Returns:
pxr::GfMatrix4f Equivalent transform matrix in USD format
