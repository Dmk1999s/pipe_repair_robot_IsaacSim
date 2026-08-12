<!-- source: py/api/function_deprecated_2omni_8isaac_8dynamic__control_2include_2omni_2isaac_2dynamic__control_2_conversions_8h_1a1fef98e503fc21e6dac3397bb7d81e04.html | title: asGfVec3d — Isaac Sim -->

# asGfVec3d
Fully qualified name: `omni::isaac::dynamic_control::conversions::asGfVec3d`
inlinepxr ::GfVec3domni ::isaac ::dynamic_control ::conversions ::asGfVec3d(
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
