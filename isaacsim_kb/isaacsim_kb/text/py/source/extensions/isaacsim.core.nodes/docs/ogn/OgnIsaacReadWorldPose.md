<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacReadWorldPose.html | title: Isaac Read World Pose — Isaac Sim -->

# Isaac Read World Pose
Isaac Sim node that reads world pose of an xform

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Prim ( inputs:prim ) | target | Usd prim reference from which the fabric pose will be read | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Orientation ( outputs:orientation ) | quatd[4] | Orientation as a quaternion (IJKR) | [0.0, 0.0, 0.0, 1.0]
Scale ( outputs:scale ) | vectord[3] | Scale vector in meters | [0.0, 0.0, 0.0]
Translation ( outputs:translation ) | vectord[3] | Translation vector in meters | [0.0, 0.0, 0.0]
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacReadWorldPose
Version | 2
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacReadWorldPose.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Read World Pose
Categories | isaacCore
Generated Class Name | OgnIsaacReadWorldPoseDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
