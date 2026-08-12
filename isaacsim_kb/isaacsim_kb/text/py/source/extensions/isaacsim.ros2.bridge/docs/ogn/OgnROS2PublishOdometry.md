<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2PublishOdometry.html | title: ROS2 Publish Odometry — Isaac Sim -->

# ROS2 Publish Odometry
This node publishes odometry as a ROS2 Odometry message

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Angular Velocity ( inputs:angularVelocity ) | vectord[3] | Angular velocity vector in rad/s | [0.0, 0.0, 0.0]
Chassis Frame Id ( inputs:chassisFrameId ) | string | FrameId for robot chassis frame | base_link
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Exec In ( inputs:execIn ) | execution | The input execution port | None
Linear Velocity ( inputs:linearVelocity ) | vectord[3] | Linear velocity vector in m/s | [0.0, 0.0, 0.0]
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Odom Frame Id ( inputs:odomFrameId ) | string | FrameId for ROS2 odometry message | odom
Orientation ( inputs:orientation ) | quatd[4] | Orientation as a quaternion (IJKR) | [0.0, 0.0, 0.0, 1.0]
Position ( inputs:position ) | vectord[3] | Position vector in meters | [0.0, 0.0, 0.0]
Publish Raw Velocities ( inputs:publishRawVelocities ) | bool | When enabled, linear and angular velocities are published as provided, without transformation. When disabled, the given world velocities are projected into the robot’s frame before publishing. | False
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be sent. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Robot Front ( inputs:robotFront ) | vectord[3] | The front of the robot. The robotFront vector utilizes x and y, and drops the z component. We assume a robotUp vector of [0.0, 0.0, 1.0] to project given world linear and angular velocities into the robot’s local frame. | [1.0, 0.0, 0.0]
Timestamp ( inputs:timeStamp ) | double | ROS2 Timestamp in seconds | 0.0
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | odom
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2PublishOdometry
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2PublishOdometry.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Publish Odometry
Categories | isaacRos2:publisher
Generated Class Name | OgnROS2PublishOdometryDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
