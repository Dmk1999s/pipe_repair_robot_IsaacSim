<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacConvertDepthToPointCloud.html | title: Isaac Depth to Point Cloud — Isaac Sim -->

# Isaac Depth to Point Cloud
Converts a 32FC1 image buffer into Point Cloud data

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Buffer Size ( inputs:bufferSize ) | uint | Size (in bytes) of the buffer (0 if the input is a texture) | 0
Cuda Device Index ( inputs:cudaDeviceIndex ) | int | Index of the device where the data lives (-1 for host data) | -1
Data Ptr ( inputs:dataPtr ) | uint64 | Pointer to the raw rgba array data | 0
Exec In ( inputs:execIn ) | execution | The input execution port | None
Focal Length ( inputs:focalLength ) | float | focal length | 0.0
Format ( inputs:format ) | uint64 | Format | 33
Height ( inputs:height ) | uint | Buffer array height, same as input | 0
Horizontal Aperture ( inputs:horizontalAperture ) | float | horizontal aperture | 0.0
Vertical Aperture ( inputs:verticalAperture ) | float | vertical aperture | 0.0
Width ( inputs:width ) | uint | Buffer array width, same as input | 0
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Buffer Size ( outputs:bufferSize ) | uint | Size (in bytes) of the buffer (0 if the input is a texture) | None
Cuda Device Index ( outputs:cudaDeviceIndex ) | int | Index of the device where the data lives (-1 for host data) | -1
Data Ptr ( outputs:dataPtr ) | uint64 | Pointer to the rgb buffer data | 0
Exec Out ( outputs:execOut ) | execution | Output execution triggers when lidar sensor has completed a full scan | None
Height ( outputs:height ) | uint | Height of point cloud buffer, will always return 1 | 1
Width ( outputs:width ) | uint | number of points in point cloud buffer | 0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacConvertDepthToPointCloud
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacConvertDepthToPointCloud.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Depth to Point Cloud
Categories | isaacCore
Generated Class Name | OgnIsaacConvertDepthToPointCloudDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
