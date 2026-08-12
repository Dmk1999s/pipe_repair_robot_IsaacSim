<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a8b31d08b3d56ecc00d73c13400895839.html | title: asGfMatrix4fT — Isaac Sim -->

# asGfMatrix4fT
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfMatrix4fT`
inlinepxr ::GfMatrix4fomni ::isaac ::dynamic_control ::conversions ::asGfMatrix4fT(
constomni ::isaac ::dynamic_control ::DcTransform &input,
)
Converts a DcTransform to a transposed GfMatrix4f.
Creates a transposed 4x4 transformation matrix:

- Sets translation and rotation components

- Transposes the resulting matrix

See also
asGfMatrix4f
Note
Useful for operations requiring column-major matrix format
Parameters:
input – [in] Input transform in Dynamic Control format

Returns:
pxr::GfMatrix4f Transposed transform matrix in USD format
