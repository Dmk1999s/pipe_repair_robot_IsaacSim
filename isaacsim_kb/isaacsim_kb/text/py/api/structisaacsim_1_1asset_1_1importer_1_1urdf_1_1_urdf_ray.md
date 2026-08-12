<!-- source: py/api/structisaacsim_1_1asset_1_1importer_1_1urdf_1_1_urdf_ray.html | title: UrdfRay — Isaac Sim -->

# UrdfRay
Fully qualified name: `isaacsim::asset::importer::urdf::UrdfRay`
structUrdfRay:publicisaacsim ::asset ::importer ::urdf ::UrdfSensor

Ray-based sensor configuration for lidar/laser scanners.
Defines properties for ray-casting sensors including horizontal and vertical scanning dimensions and Isaac Sim specific configuration parameters.
Public Members
boolhasHorizontal=false

Whether horizontal scanning dimension is configured.

boolhasVertical=false

Whether vertical scanning dimension is configured.

UrdfRayDim horizontal

Horizontal scanning dimension parameters.

UrdfRayDim vertical

Vertical scanning dimension parameters.

std ::stringisaacSimConfig

Isaac Sim specific configuration string.

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
