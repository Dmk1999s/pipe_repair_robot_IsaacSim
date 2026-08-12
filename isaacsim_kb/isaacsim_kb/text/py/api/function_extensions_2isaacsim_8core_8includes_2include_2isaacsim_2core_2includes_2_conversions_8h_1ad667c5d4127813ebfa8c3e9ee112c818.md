<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1ad667c5d4127813ebfa8c3e9ee112c818.html | title: asCarbFloat4 — Isaac Sim -->

# asCarbFloat4
Fully qualified name: `isaacsim::core::includes::conversions::asCarbFloat4`
inlinecarb::Float4isaacsim ::core ::includes ::conversions ::asCarbFloat4(
constpxr ::GfQuatd&v,
)
Converts pxr::GfQuatd to carb::Float4.
Converts quaternion with component reordering and precision demotion:

- Extracts imaginary and real parts

- Converts from double to float

- Reorders components from USD to Carb format

Warning
Potential precision loss during double to float conversion
Parameters:
v – [in] Input quaternion in USD format (double precision)

Returns:
carb::Float4 Equivalent quaternion in Carb format (single precision)
