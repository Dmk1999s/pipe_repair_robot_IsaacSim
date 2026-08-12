<!-- source: py/api/structisaacsim_1_1sensors_1_1physics_1_1_cs_properties.html | title: CsProperties — Isaac Sim -->

# CsProperties
Fully qualified name: `isaacsim::sensors::physics::CsProperties`
structCsProperties

Properties configuration for a contact sensor.
Public Members
floatradius={0.0f}

Radius from the sensor position.
Negative values indicate it’s a full body sensor.

floatminThreshold={0.0f}

Minimum force that the sensor can read.
Forces below this value will not trigger a reading.

floatmaxThreshold={0.0f}

Maximum force that the sensor can register.
Forces above this value will be clamped.

floatsensorPeriod={0.0f}

Sensor reading speed, in seconds.
Zero means sync with simulation timestep.
