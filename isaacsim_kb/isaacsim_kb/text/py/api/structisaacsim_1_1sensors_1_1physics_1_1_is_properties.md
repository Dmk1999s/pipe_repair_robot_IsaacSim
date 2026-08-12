<!-- source: py/api/structisaacsim_1_1sensors_1_1physics_1_1_is_properties.html | title: IsProperties — Isaac Sim -->

# IsProperties
Fully qualified name: `isaacsim::sensors::physics::IsProperties`
structIsProperties

Properties configuration for an IMU sensor.
Public Members
usdrt::GfMatrix3dorientation

Orientation matrix relative to the parent body where the sensor is placed.

floatsensorPeriod={0.0f}

Sensor reading speed, in seconds.
Zero means sync with simulation timestep.
