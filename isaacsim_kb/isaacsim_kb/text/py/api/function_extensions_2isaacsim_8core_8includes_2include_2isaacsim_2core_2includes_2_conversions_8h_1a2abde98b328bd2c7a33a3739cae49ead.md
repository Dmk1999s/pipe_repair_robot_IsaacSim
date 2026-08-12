<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a2abde98b328bd2c7a33a3739cae49ead.html | title: asPxVec3 — Isaac Sim -->

# asPxVec3
Fully qualified name: `isaacsim::core::includes::conversions::asPxVec3`
inline::physx ::PxVec3isaacsim ::core ::includes ::conversions ::asPxVec3(
constpxr ::GfVec3d&v,
)
Converts pxr::GfVec3d into PhysX vector.
Performs component-wise conversion with precision demotion:

- x, y, z components are converted from double to float

Warning
Potential precision loss during double to float conversion
Parameters:
v – [in] Input vector in USD format (double precision)

Returns:
PxVec3 Equivalent vector in PhysX format (single precision)
