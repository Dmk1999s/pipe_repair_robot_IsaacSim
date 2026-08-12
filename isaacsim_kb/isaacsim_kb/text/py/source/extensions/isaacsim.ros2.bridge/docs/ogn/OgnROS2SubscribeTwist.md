<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2SubscribeTwist.html | title: ROS2 Subscribe Twist — Isaac Sim -->

# ROS2 Subscribe Twist
This node subscribes to a ROS2 Twist message

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Exec In ( inputs:execIn ) | execution | The input execution port. | None
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be processed. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | cmd_vel
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Angular Velocity ( outputs:angularVelocity ) | vectord[3] | Angular velocity vector in rad/s | [0.0, 0.0, 0.0]
Exec Out ( outputs:execOut ) | execution | Output execution triggers when a new message is received | None
Linear Velocity ( outputs:linearVelocity ) | vectord[3] | Linear velocity vector in m/s | [0.0, 0.0, 0.0]
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2SubscribeTwist
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2SubscribeTwist.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Subscribe Twist
Categories | isaacRos2:subscriber
Generated Class Name | OgnROS2SubscribeTwistDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
