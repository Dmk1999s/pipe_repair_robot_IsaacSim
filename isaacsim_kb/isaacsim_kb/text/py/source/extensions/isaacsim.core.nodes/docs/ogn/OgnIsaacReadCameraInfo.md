<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacReadCameraInfo.html | title: Isaac Read Camera Info — Isaac Sim -->

# Isaac Read Camera Info
Isaac Sim node that reads camera info for a viewport

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Render Product Path ( inputs:renderProductPath ) | token | Path of the render product |
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Camera Fisheye Params ( outputs:cameraFisheyeParams ) | float[] | Camera fisheye projection parameters | None
Focal Length ( outputs:focalLength ) | float | focal length | None
Height ( outputs:height ) | uint | Height for output image | None
Horizontal Aperture ( outputs:horizontalAperture ) | float | horizontal aperture | None
Horizontal Offset ( outputs:horizontalOffset ) | float | horizontal offset | None
Physical Distortion Coefficients ( outputs:physicalDistortionCoefficients ) | float[] | physical distortion model used for approximation, empty if not specified on camera prim | None
Physical Distortion Model ( outputs:physicalDistortionModel ) | token | physical distortion model used for approximation, empty if not specified on camera prim | None
Projection Type ( outputs:projectionType ) | token | projection type | None
Vertical Aperture ( outputs:verticalAperture ) | float | vertical aperture | None
Vertical Offset ( outputs:verticalOffset ) | float | vertical offset | None
Width ( outputs:width ) | uint | Width for output image | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacReadCameraInfo
Version | 2
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacReadCameraInfo.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read Camera Info
Categories | isaacCore
Generated Class Name | OgnIsaacReadCameraInfoDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
