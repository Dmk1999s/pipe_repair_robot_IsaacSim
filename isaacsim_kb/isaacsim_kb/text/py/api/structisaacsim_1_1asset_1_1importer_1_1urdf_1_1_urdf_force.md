<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_force.html | title: UrdfForce — Isaac Sim -->

# UrdfForce
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfForce`
structUrdfForce:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Force sensor configuration.
Defines force sensor properties including the reference frame and measurement direction for force/torque sensing.
Public Members
std ::stringframe

The child element frame to measure force relative to.

intmeasureDirection

Direction of force measurement (0: parent_to_child, 1: child_to_parent).

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
