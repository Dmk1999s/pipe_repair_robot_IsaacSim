<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1a5c6c30b1358061be9161869c0c378bba.html | title: asPxTransform — Isaac Sim -->

# asPxTransform
Fully qualified name: `isaacsim::core::includes::conversions::asPxTransform`
inline::physx ::PxTransformisaacsim ::core ::includes ::conversions ::asPxTransform(
constusdrt::GfVec3d&translation,
constusdrt::GfQuatd&orientation,
)
Converts USD runtime translation and orientation into PhysX transform.
Creates a PhysX transform from separate position and orientation:

- Converts translation vector to PxVec3

- Converts orientation quaternion to PxQuat

See also
asPxVec3
See also
asPxQuat
Warning
Potential precision loss when converting from double precision USD types
Parameters:

- translation – [in] Position vector in USD runtime format

- orientation – [in]Rotation quaternion in USD runtime format

Returns:
PxTransform Equivalent transform in PhysX format
