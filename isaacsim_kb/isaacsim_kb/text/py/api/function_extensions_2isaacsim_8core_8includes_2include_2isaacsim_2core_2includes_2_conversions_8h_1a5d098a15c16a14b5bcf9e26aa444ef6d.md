<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a5d098a15c16a14b5bcf9e26aa444ef6d.html | title: asPxTransform — Isaac Sim -->

# asPxTransform
Fully qualified name: `isaacsim::core::includes::conversions::asPxTransform`
inline::physx ::PxTransformisaacsim ::core ::includes ::conversions ::asPxTransform(
constusdrt::GfMatrix4d&mat,
)
Converts USD runtime matrix into PhysX transform.
Creates a PhysX transform from a USD runtime 4x4 matrix:

- Creates a GfTransform from the matrix

- Extracts translation and rotation components

- Converts to PhysX format with potential precision demotion

See also
asPxTransform(const pxr::GfTransform&)
Warning
Potential precision loss when converting from double precision USD types
Parameters:
mat – [in] Input 4x4 matrix in USD runtime format

Returns:
PxTransform Equivalent transform in PhysX format
