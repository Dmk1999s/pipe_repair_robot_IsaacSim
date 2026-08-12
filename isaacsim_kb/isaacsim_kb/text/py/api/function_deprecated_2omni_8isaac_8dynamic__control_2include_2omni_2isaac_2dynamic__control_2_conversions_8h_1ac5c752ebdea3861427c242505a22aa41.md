<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1ac5c752ebdea3861427c242505a22aa41.html | title: asGfRotation — Isaac Sim -->

# asGfRotation
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfRotation`
inlinepxr ::GfRotationomni ::isaac ::dynamic_control ::conversions ::asGfRotation(
constcarb::Float4&q,
)
Converts a carb::Float4 into a pxr::GfRotation.
Creates a USD rotation representation from a Carb quaternion:

- Converts the quaternion to GfQuatd format

- Constructs a GfRotation from the quaternion

See also
asGfQuatd
Parameters:
q – [in] Input quaternion in Carb format

Returns:
pxr::GfRotation Equivalent rotation in USD format
