<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a6dbb7d6a273aea63fa3f8ab48df97daf.html | title: asPxVec3 — Isaac Sim -->

# asPxVec3
Fully qualified name: `isaacsim::core::includes::conversions::asPxVec3`
inline::physx ::PxVec3isaacsim ::core ::includes ::conversions ::asPxVec3(
constusdrt::GfVec3d&v,
)
Converts usdrt::GfVec3d into PhysX vector.
Performs component-wise conversion with precision demotion:

- x, y, z components are converted from double to float

Warning
Potential precision loss during double to float conversion
Parameters:
v – [in] Input vector in USD runtime format (double precision)

Returns:
PxVec3 Equivalent vector in PhysX format (single precision)
