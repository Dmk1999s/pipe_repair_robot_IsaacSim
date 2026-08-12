<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a65692dd9f2a021e8aeeece4255616d83.html | title: asPxVec3 — Isaac Sim -->

# asPxVec3
Fully qualified name: `isaacsim::core::includes::conversions::asPxVec3`
inline::physx ::PxVec3isaacsim ::core ::includes ::conversions ::asPxVec3(
constcarb::Float3&v,
)
Converts carb::Float3 into PhysX vector.
Performs direct component-wise conversion to PhysX format.
Note
No precision loss as both types use single precision
Parameters:
v – [in] Input vector in Carb format

Returns:
PxVec3 Equivalent vector in PhysX format
