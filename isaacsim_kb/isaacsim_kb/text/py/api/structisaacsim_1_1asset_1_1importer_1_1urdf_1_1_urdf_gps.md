<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_gps.html | title: UrdfGps — Isaac Sim -->

# UrdfGps
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfGps`
structUrdfGps:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

GPS sensor configuration.
Defines GPS sensor properties including noise characteristics for position and velocity measurements.
Public Members
UrdfNoise positionNoise

Noise characteristics for position measurements.

UrdfNoise velocityNoise

Noise characteristics for velocity measurements.

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
