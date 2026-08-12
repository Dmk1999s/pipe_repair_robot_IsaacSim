<!-- source: py/api/class_structisaacsim_1_1sensors_1_1physx_1_1_radar_sensor_interface.html | title: RadarSensorInterface — Isaac Sim -->

# RadarSensorInterface
Fully qualified name: `isaacsim::sensors::physx::RadarSensorInterface`
classRadarSensorInterface

Interface for accessing radar sensor functionality.
Provides methods to interact with radar sensors in the simulation.
Public Members
bool(*isRadarSensor)(constchar*sensorPath)

Checks if a given path refers to a radar sensor.
Param sensorPath:
[in] Path to check.

Return:
True if path refers to a radar sensor, false otherwise.
