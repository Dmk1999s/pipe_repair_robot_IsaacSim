<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a55207ce3869338221bd8fe4ed7c22a80.html | title: asPxTransform — Isaac Sim -->

# asPxTransform
Fully qualified name: `isaacsim::core::includes::conversions::asPxTransform`
inline::physx ::PxTransformisaacsim ::core ::includes ::conversions ::asPxTransform(
constpxr ::GfTransform&trans,
)
Converts USD transform into PhysX transform.
Creates a complete PhysX transform from USD transform:

- Extracts translation and rotation components

- Converts to PhysX format with potential precision demotion

See also
asPxVec3
See also
asPxQuat
Warning
Potential precision loss when converting from double precision USD types
Parameters:
trans – [in] Input transform in USD format

Returns:
PxTransform Equivalent transform in PhysX format
