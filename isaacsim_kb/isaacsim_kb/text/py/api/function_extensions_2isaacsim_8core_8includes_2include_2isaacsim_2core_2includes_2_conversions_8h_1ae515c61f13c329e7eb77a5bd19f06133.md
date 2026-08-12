<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_conversions_8h_1ae515c61f13c329e7eb77a5bd19f06133.html | title: asPxQuat — Isaac Sim -->

# asPxQuat
Fully qualified name: `isaacsim::core::includes::conversions::asPxQuat`
inline::physx ::PxQuatisaacsim ::core ::includes ::conversions ::asPxQuat(
constusdrt::GfQuatd&v,
)
Converts usdrt::GfQuatd into PhysX quaternion.
Converts quaternion with component reordering and precision demotion:

- Extracts imaginary and real parts

- Converts from double to float

- Reorders components from USD runtime to PhysX format

Warning
Potential precision loss during double to float conversion
Parameters:
v – [in] Input quaternion in USD runtime format (double precision)

Returns:
PxQuat Equivalent quaternion in PhysX format (single precision)
