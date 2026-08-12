<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_sonar.html | title: UrdfSonar — Isaac Sim -->

# UrdfSonar
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfSonar`
structUrdfSonar:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Sonar sensor configuration.
Defines sonar sensor properties including range limits and detection radius for ultrasonic distance sensing.
Public Members
floatmin

Minimum detection range.

floatmax

Maximum detection range.

floatradius

Detection radius/beam width.

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
