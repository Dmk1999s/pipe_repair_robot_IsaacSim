<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1aada915f7400f7cb49003f25851068dfa.html | title: asPxVec3 — Isaac Sim -->

# asPxVec3
Fully qualified name: `isaacsim::core::includes::conversions::asPxVec3`
inline::physx ::PxVec3isaacsim ::core ::includes ::conversions ::asPxVec3(
constpxr ::GfVec3f&v,
)
Converts pxr::GfVec3f into PhysX vector.
Performs direct component-wise conversion from USD to PhysX format.
Note
No precision loss as both types use single precision
Parameters:
v – [in] Input vector in USD format

Returns:
PxVec3 Equivalent vector in PhysX format
