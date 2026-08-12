<!-- source: py/source/extensions/isaacsim.sensors.physx/docs/ogn/OgnIsaacReadLidarPointCloud.html | title: Isaac Read Lidar Point Cloud Node — Isaac Sim -->

# Isaac Read Lidar Point Cloud Node
This node reads from the lidar sensor and holds point cloud data buffers for a full scan

## Installation
To use this node enable isaacsim.sensors.physx in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Exec In ( inputs:execIn ) | execution | The input execution port | None
Lidar Prim ( inputs:lidarPrim ) | target | Usd prim reference to the lidar prim | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Data ( outputs:data ) | pointf[3][] | Buffer of 3d points containing point cloud data | []
Exec Out ( outputs:execOut ) | execution | Output execution triggers when lidar sensor has completed a full scan | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.sensors.physx.IsaacReadLidarPointCloud
Version | 2
Extension | isaacsim.sensors.physx
Icon | ogn/icons/isaacsim.sensors.physx.IsaacReadLidarPointCloud.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read Lidar Point Cloud Node
Categories | isaacPhysxSensor
Generated Class Name | OgnIsaacReadLidarPointCloudDatabase
Python Module | isaacsim.sensors.physx
[/TABLE]
