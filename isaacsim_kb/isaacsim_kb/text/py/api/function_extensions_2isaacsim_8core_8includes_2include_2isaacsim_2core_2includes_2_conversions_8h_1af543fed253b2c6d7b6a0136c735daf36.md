<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1af543fed253b2c6d7b6a0136c735daf36.html | title: asPxQuat — Isaac Sim -->

# asPxQuat
Fully qualified name: `isaacsim::core::includes::conversions::asPxQuat`
inline::physx ::PxQuatisaacsim ::core ::includes ::conversions ::asPxQuat(
constpxr ::GfQuatf&v,
)
Converts pxr::GfQuatf into PhysX quaternion.
Converts quaternion with component reordering:

- USD format: (w, x, y, z)

- PhysX format: (x, y, z, w)

Note
Component order is adjusted during conversion
Parameters:
v – [in] Input quaternion in USD format

Returns:
PxQuat Equivalent quaternion in PhysX format
