<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a07074014cd9e390e6b85ee31a9f89464.html | title: asGfQuatf — Isaac Sim -->

# asGfQuatf
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfQuatf`
inlinepxr ::GfQuatfomni ::isaac ::dynamic_control ::conversions ::asGfQuatf(
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
