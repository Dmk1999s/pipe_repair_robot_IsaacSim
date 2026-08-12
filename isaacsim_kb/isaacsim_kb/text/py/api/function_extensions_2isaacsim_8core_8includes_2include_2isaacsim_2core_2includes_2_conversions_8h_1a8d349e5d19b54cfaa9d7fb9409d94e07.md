<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a8d349e5d19b54cfaa9d7fb9409d94e07.html | title: asGfTransform — Isaac Sim -->

# asGfTransform
Fully qualified name: `isaacsim::core::includes::conversions::asGfTransform`
inlinepxr ::GfTransformisaacsim ::core ::includes ::conversions ::asGfTransform(
constcarb::Float3&p,
constcarb::Float4&r,
)
Converts position and rotation into a pxr::GfTransform.
Creates a complete transform from separate position and rotation:

- Sets rotation using quaternion conversion

- Sets translation using vector conversion

See also
asGfRotation
See also
asGfVec3d
Parameters:

- p – [in] Position vector in Carb format

- r – [in]Rotation quaternion in Carb format

Returns:
pxr::GfTransform Equivalent transform in USD format
