<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2PublishImu.html | title: ROS2 Publish Imu — Isaac Sim -->

# ROS2 Publish Imu
This node publishes IMU data as a ROS2 IMU message

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Angular Velocity ( inputs:angularVelocity ) | vectord[3] | Angular velocity vector in rad/s | [0.0, 0.0, 0.0]
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Exec In ( inputs:execIn ) | execution | The input execution port | None
Frame Id ( inputs:frameId ) | string | FrameId for ROS2 message | sim_imu
Linear Acceleration ( inputs:linearAcceleration ) | vectord[3] | Linear acceleration vector in m/s^2 | [0.0, 0.0, 0.0]
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Orientation ( inputs:orientation ) | quatd[4] | Orientation as a quaternion (IJKR) | [0.0, 0.0, 0.0, 1.0]
Publish Angular Velocity ( inputs:publishAngularVelocity ) | bool | Include Angular velocity in msg | True
Publish Linear Acceleration ( inputs:publishLinearAcceleration ) | bool | Include Linear acceleration in msg | True
Publish Orientation ( inputs:publishOrientation ) | bool | Include orientation in msg | True
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be sent. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Timestamp ( inputs:timeStamp ) | double | ROS2 Timestamp in seconds | 0.0
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | imu
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2PublishImu
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2PublishImu.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Publish Imu
Categories | isaacRos2:publisher
Generated Class Name | OgnROS2PublishImuDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
