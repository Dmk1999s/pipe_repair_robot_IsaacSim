<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a0ef3fefb015aa29ae917a8b89f0f8383.html | title: asCarbFloat4 — Isaac Sim -->

# asCarbFloat4
Fully qualified name: `isaacsim::core::includes::conversions::asCarbFloat4`
inlinecarb::Float4isaacsim ::core ::includes ::conversions ::asCarbFloat4(
constpxr ::GfQuatf&v,
)
Converts pxr::GfQuatf to carb::Float4.
Converts quaternion with component reordering:

- USD format: (w, x, y, z)

- Carb format: (x, y, z, w)

Note
Component order is adjusted during conversion
Parameters:
v – [in] Input quaternion in USD format

Returns:
carb::Float4 Equivalent quaternion in Carb format
