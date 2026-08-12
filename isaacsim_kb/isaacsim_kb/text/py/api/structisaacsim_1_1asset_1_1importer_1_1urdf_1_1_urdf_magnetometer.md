<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_magnetometer.html | title: UrdfMagnetometer — Isaac Sim -->

# UrdfMagnetometer
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfMagnetometer`
structUrdfMagnetometer:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Magnetometer sensor configuration.
Defines magnetometer sensor properties including noise characteristics for magnetic field measurements.
Public Members
UrdfNoise noise

Noise characteristics for magnetometer measurements.

std ::stringname

Name identifier for the sensor.

Transform origin

Transform from link frame to sensor frame.

UrdfSensorType type

Type of sensor (camera, lidar, IMU, etc.).

std ::stringid

Unique identifier for the sensor.

floatupdateRate

Update rate of the sensor in Hz.
