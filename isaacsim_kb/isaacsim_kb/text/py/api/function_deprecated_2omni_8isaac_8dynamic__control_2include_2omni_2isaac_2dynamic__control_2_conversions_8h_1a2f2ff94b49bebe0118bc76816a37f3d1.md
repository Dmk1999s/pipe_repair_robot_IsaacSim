<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a2f2ff94b49bebe0118bc76816a37f3d1.html | title: asGfVec3f — Isaac Sim -->

# asGfVec3f
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfVec3f`
inlinepxr ::GfVec3fomni ::isaac ::dynamic_control ::conversions ::asGfVec3f(
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
