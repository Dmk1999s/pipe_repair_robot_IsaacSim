<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1ae21ef6d9b3ea50dad8570c1a928431c2.html | title: asGfRotation — Isaac Sim -->

# asGfRotation
Fully qualified name: `isaacsim::core::includes::conversions::asGfRotation`
inlinepxr ::GfRotationisaacsim ::core ::includes ::conversions ::asGfRotation(
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
