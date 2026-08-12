<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_camera.html | title: UrdfCamera — Isaac Sim -->

# UrdfCamera
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfCamera`
structUrdfCamera:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Camera sensor configuration extending base sensor.
Defines camera-specific properties for visual sensors including image dimensions, field of view, and rendering parameters.
Public Members
floatwidth

Image width in pixels.

floatheight

Image height in pixels.

std ::stringformat

Image format specification.

floathfov

Horizontal field of view in radians.

floatclipNear

Near clipping plane distance.

floatclipFar

Far clipping plane distance.

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
