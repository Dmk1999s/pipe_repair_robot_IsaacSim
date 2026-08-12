<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1ad093d5dd82929800fa80219780d57c06.html | title: asGfVec3f — Isaac Sim -->

# asGfVec3f
Fully qualified name: `isaacsim::core::includes::conversions::asGfVec3f`
inlinepxr ::GfVec3fisaacsim ::core ::includes ::conversions ::asGfVec3f(
constcarb::Float3&v,
)
Converts a carb::Float3 into a pxr::GfVec3f.
Performs a direct component-wise conversion from Carb’s Float3 to USD’s GfVec3f.
Note
No precision loss as both types use single precision
Parameters:
v – [in] Input vector in Carb format

Returns:
pxr::GfVec3f Equivalent vector in USD format
