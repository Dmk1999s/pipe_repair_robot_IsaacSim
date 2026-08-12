<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_imu.html | title: UrdfImu — Isaac Sim -->

# UrdfImu
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfImu`
structUrdfImu:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Inertial measurement unit sensor configuration.
Defines IMU sensor properties including noise characteristics for gyroscope and accelerometer measurements.
Public Members
UrdfNoise gyroNoise

Noise characteristics for gyroscope measurements.

UrdfNoise accelerationNoise

Noise characteristics for accelerometer measurements.

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
