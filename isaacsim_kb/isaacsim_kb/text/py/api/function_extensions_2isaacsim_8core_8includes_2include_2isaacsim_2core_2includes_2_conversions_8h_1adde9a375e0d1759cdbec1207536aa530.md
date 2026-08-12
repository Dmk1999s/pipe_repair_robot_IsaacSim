<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1adde9a375e0d1759cdbec1207536aa530.html | title: asGfVec3d — Isaac Sim -->

# asGfVec3d
Fully qualified name: `isaacsim::core::includes::conversions::asGfVec3d`
inlinepxr ::GfVec3disaacsim ::core ::includes ::conversions ::asGfVec3d(
constcarb::Float3&v,
)
Converts a carb::Float3 into a pxr::GfVec3d.
Performs a component-wise conversion with promotion to double precision:

- x, y, z components are converted from float to double

Note
Involves precision promotion from float to double
Parameters:
v – [in] Input vector in Carb format (single precision)

Returns:
pxr::GfVec3d Equivalent vector in USD format (double precision)
