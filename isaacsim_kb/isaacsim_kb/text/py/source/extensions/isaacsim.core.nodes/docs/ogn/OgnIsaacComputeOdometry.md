<!-- source: py/source/extensions/isaacsim.core.nodes/docs/ogn/OgnIsaacComputeOdometry.html | title: Isaac Compute Odometry Node — Isaac Sim -->

# Isaac Compute Odometry Node
Holds values related to odometry, this node is not a replcement for the IMU sensor and the associated Read IMU node

## Installation
To use this node enable isaacsim.core.nodes in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Chassis Prim ( inputs:chassisPrim ) | target | Usd prim reference to the articulation root or rigid body prim | None
Exec In ( inputs:execIn ) | execution | The input execution port | None
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Angular Acceleration ( outputs:angularAcceleration ) | vectord[3] | Angular acceleration vector in rad/s^2 | [0.0, 0.0, 0.0]
Angular Velocity ( outputs:angularVelocity ) | vectord[3] | Angular velocity vector in rad/s | [0.0, 0.0, 0.0]
Exec Out ( outputs:execOut ) | execution | The output execution port | None
Global Linear Acceleration ( outputs:globalLinearAcceleration ) | vectord[3] | Global linear acceleration vector in m/s^2 | [0.0, 0.0, 0.0]
Global Linear Velocity ( outputs:globalLinearVelocity ) | vectord[3] | Global linear velocity vector in m/s | [0.0, 0.0, 0.0]
Linear Acceleration ( outputs:linearAcceleration ) | vectord[3] | Linear acceleration vector in m/s^2 | [0.0, 0.0, 0.0]
Linear Velocity ( outputs:linearVelocity ) | vectord[3] | Linear velocity vector in m/s | [0.0, 0.0, 0.0]
Orientation ( outputs:orientation ) | quatd[4] | Rotation as a quaternion (IJKR) | [0.0, 0.0, 0.0, 1.0]
Position ( outputs:position ) | vectord[3] | Position vector in meters | [0.0, 0.0, 0.0]
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.core.nodes.IsaacComputeOdometry
Version | 1
Extension | isaacsim.core.nodes
Icon | ogn/icons/isaacsim.core.nodes.IsaacComputeOdometry.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | Isaac Compute Odometry Node
Categories | isaacCore
Generated Class Name | OgnIsaacComputeOdometryDatabase
Python Module | isaacsim.core.nodes
[/TABLE]
