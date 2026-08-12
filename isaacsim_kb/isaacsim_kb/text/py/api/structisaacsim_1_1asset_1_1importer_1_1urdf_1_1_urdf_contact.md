<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_contact.html | title: UrdfContact — Isaac Sim -->

# UrdfContact
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfContact`
structUrdfContact:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Contact sensor configuration.
Defines contact sensor properties including the collision elements that are monitored for contact detection.
Public Members
std ::vector<UrdfCollision >collision

Collision elements monitored for contact detection.

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
