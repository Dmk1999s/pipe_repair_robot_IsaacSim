<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1addffe63c3aca2b90b916028965eddb11.html | title: asCarbFloat3 — Isaac Sim -->

# asCarbFloat3
Fully qualified name: `isaacsim::core::includes::conversions::asCarbFloat3`
inlinecarb::Float3isaacsim ::core ::includes ::conversions ::asCarbFloat3(
constpxr ::GfVec3f&v,
)
Converts pxr::GfVec3f to carb::Float3.
Performs direct component-wise conversion from USD to Carb format.
Note
No precision loss as both types use single precision
Parameters:
v – [in] Input vector in USD format

Returns:
carb::Float3 Equivalent vector in Carb format
