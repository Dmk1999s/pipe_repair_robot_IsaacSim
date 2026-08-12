<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1aa6cb8d0ae3cc96e9f9188b1e32e176d1.html | title: asCarbFloat3 — Isaac Sim -->

# asCarbFloat3
Fully qualified name: `isaacsim::core::includes::conversions::asCarbFloat3`
inlinecarb::Float3isaacsim ::core ::includes ::conversions ::asCarbFloat3(
constpxr ::GfVec3d&v,
)
Converts pxr::GfVec3d to carb::Float3.
Performs component-wise conversion with precision demotion:

- x, y, z components are converted from double to float

Warning
Potential precision loss during double to float conversion
Parameters:
v – [in] Input vector in USD format (double precision)

Returns:
carb::Float3 Equivalent vector in Carb format (single precision)
