<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2SubscribeAckermann.html | title: ROS2 Subscribe AckermannDrive — Isaac Sim -->

# ROS2 Subscribe AckermannDrive
This node subscribes to a ROS2 AckermannDriveStamped message

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
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | ackermann_cmd
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Acceleration ( outputs:acceleration ) | double | Desired acceleration in m/s^2 | 0.0
Exec Out ( outputs:execOut ) | execution | Output execution triggers when a new message is received | None
Frame Id ( outputs:frameId ) | string | FrameId for ROS2 message |
Jerk ( outputs:jerk ) | double | Desired jerk in m/s^3 | 0.0
Speed ( outputs:speed ) | double | Desired forward speed in m/s | 0.0
Steering Angle ( outputs:steeringAngle ) | double | Desired virtual angle in radians. Corresponds to the yaw of a virtual wheel located at the center of the front axle | 0.0
Steering Angle Velocity ( outputs:steeringAngleVelocity ) | double | Desired rate of change of virtual angle in rad/s. Corresponds to the yaw of a virtual wheel located at the center of the front axle | 0.0
Time Stamp ( outputs:timeStamp ) | double | Timestamp of message in seconds | 0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2SubscribeAckermannDrive
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2SubscribeAckermannDrive.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Subscribe AckermannDrive
Categories | isaacRos2:subscriber
Generated Class Name | OgnROS2SubscribeAckermannDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
