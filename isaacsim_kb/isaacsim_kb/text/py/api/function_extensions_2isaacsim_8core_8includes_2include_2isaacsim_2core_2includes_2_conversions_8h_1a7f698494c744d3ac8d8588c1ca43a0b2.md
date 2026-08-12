<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a7f698494c744d3ac8d8588c1ca43a0b2.html | title: asGfQuatf — Isaac Sim -->

# asGfQuatf
Fully qualified name: `isaacsim::core::includes::conversions::asGfQuatf`
inlinepxr ::GfQuatfisaacsim ::core ::includes ::conversions ::asGfQuatf(
constcarb::Float4&q,
)
Converts a carb::Float4 into a pxr::GfQuatf.
Converts a quaternion from Carb to USD format, handling component reordering:

- Carb format: (x, y, z, w)

- USD format: (w, x, y, z)

Note
Component order is adjusted during conversion
Parameters:
q – [in] Input quaternion in Carb format

Returns:
pxr::GfQuatf Equivalent quaternion in USD format
