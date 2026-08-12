<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1afee8bd1395da1b1460fa839e7a9265b5.html | title: asPxVec3 — Isaac Sim -->

# asPxVec3
Fully qualified name: `isaacsim::core::includes::conversions::asPxVec3`
inline::physx ::PxVec3isaacsim ::core ::includes ::conversions ::asPxVec3(
constusdrt::GfVec3f&v,
)
Converts usdrt::GfVec3f into PhysX vector.
Performs direct component-wise conversion from USD runtime to PhysX format.
Note
No precision loss as both types use single precision
Parameters:
v – [in] Input vector in USD runtime format

Returns:
PxVec3 Equivalent vector in PhysX format
