<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_sensor.html | title: UrdfSensor — Isaac Sim -->

# UrdfSensor
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfSensor`
structUrdfSensor

Base sensor definition for URDF sensors.
Provides common properties for all sensor types including name, pose, type identification, and update rate configuration.
Subclassed by isaacsim::asset::importer::urdf::UrdfCamera , isaacsim::asset::importer::urdf::UrdfContact , isaacsim::asset::importer::urdf::UrdfForce , isaacsim::asset::importer::urdf::UrdfGps , isaacsim::asset::importer::urdf::UrdfImu , isaacsim::asset::importer::urdf::UrdfMagnetometer , isaacsim::asset::importer::urdf::UrdfRay , isaacsim::asset::importer::urdf::UrdfRfid , isaacsim::asset::importer::urdf::UrdfRfidTag , isaacsim::asset::importer::urdf::UrdfSonar
Public Members
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
