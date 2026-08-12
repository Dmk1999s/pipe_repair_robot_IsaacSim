<!-- source: py/api/function__isaac_sensor_component_8h_1a7365f2e5f1048c1fc8351ba167f4d76d.html | title: lerp — Isaac Sim -->

# lerp
Fully qualified name: `isaacsim::sensors::physics::lerp`
inlinefloatisaacsim ::sensors ::physics ::lerp(
constfloat&start,
constfloat&end,
constfloatt,
)
Linear interpolation between two values.
Performs linear interpolation between start and end values based on the interpolation factor t. The interpolation is calculated as: start + ((end - start) * t).
Note
The interpolation factor t should be between 0.0 and 1.0 for expected results.
Parameters:

- start – [in] Starting value for interpolation.

- end – [in] Ending value for interpolation.

- t – [in] Interpolation factor between 0.0 and 1.0.

Returns:
The interpolated value.
