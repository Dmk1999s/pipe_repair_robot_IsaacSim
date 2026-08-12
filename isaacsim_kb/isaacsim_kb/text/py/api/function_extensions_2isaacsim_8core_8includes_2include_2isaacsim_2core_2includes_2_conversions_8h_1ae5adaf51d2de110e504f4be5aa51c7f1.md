<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1ae5adaf51d2de110e504f4be5aa51c7f1.html | title: asGfQuatd — Isaac Sim -->

# asGfQuatd
Fully qualified name: `isaacsim::core::includes::conversions::asGfQuatd`
inlinepxr ::GfQuatdisaacsim ::core ::includes ::conversions ::asGfQuatd(
constcarb::Float4&q,
)
Converts a carb::Float4 into a pxr::GfQuatd.
Converts a quaternion from Carb to USD format with precision promotion:

- Handles component reordering (x,y,z,w) -> (w,x,y,z)

- Promotes single precision to double precision

Note
Combines component reordering with precision promotion
Parameters:
q – [in] Input quaternion in Carb format (single precision)

Returns:
pxr::GfQuatd Equivalent quaternion in USD format (double precision)
