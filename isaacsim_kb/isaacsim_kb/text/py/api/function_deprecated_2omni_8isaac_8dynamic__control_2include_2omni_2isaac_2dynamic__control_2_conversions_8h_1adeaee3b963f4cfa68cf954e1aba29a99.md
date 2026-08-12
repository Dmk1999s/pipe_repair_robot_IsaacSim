<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1adeaee3b963f4cfa68cf954e1aba29a99.html | title: asGfTransform — Isaac Sim -->

# asGfTransform
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfTransform`
inlinepxr ::GfTransformomni ::isaac ::dynamic_control ::conversions ::asGfTransform(
constomni ::isaac ::dynamic_control ::DcTransform &pose,
)
Converts a DcTransform into a pxr::GfTransform.
Creates a complete transform from a Dynamic Control transform:

- Sets rotation using quaternion conversion

- Sets translation using vector conversion

See also
asGfRotation
See also
asGfVec3d
Parameters:
pose – [in] Input transform in Dynamic Control format

Returns:
pxr::GfTransform Equivalent transform in USD format
