<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1afceeac53223eef0685b6a011cc316988.html | title: asPxQuat — Isaac Sim -->

# asPxQuat
Fully qualified name: `isaacsim::core::includes::conversions::asPxQuat`
inline::physx ::PxQuatisaacsim ::core ::includes ::conversions ::asPxQuat(
constcarb::Float4&q,
)
Converts carb::Float4 into PhysX quaternion.
Converts quaternion with component reordering:

- Carb format: (x, y, z, w)

- PhysX format: (x, y, z, w)

Note
Component order matches between formats
Parameters:
q – [in] Input quaternion in Carb format

Returns:
PxQuat Equivalent quaternion in PhysX format
