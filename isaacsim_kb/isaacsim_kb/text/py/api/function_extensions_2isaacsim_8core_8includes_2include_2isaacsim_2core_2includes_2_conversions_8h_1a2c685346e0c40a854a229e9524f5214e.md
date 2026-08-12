<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a2c685346e0c40a854a229e9524f5214e.html | title: asPxQuat — Isaac Sim -->

# asPxQuat
Fully qualified name: `isaacsim::core::includes::conversions::asPxQuat`
inline::physx ::PxQuatisaacsim ::core ::includes ::conversions ::asPxQuat(
constusdrt::GfQuatf&v,
)
Converts usdrt::GfQuatf into PhysX quaternion.
Converts quaternion with component reordering:

- USD runtime format: (w, x, y, z)

- PhysX format: (x, y, z, w)

Note
Component order is adjusted during conversion
Parameters:
v – [in] Input quaternion in USD runtime format

Returns:
PxQuat Equivalent quaternion in PhysX format
