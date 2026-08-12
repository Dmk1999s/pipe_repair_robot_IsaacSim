<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1ac7626728d3f0f75cff3625152be198d0.html | title: asGfQuatd — Isaac Sim -->

# asGfQuatd
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfQuatd`
inlinepxr ::GfQuatdomni ::isaac ::dynamic_control ::conversions ::asGfQuatd(
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
