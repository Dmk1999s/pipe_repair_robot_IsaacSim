<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2SubscribeJointState.html | title: ROS2 Subscribe Joint State — Isaac Sim -->

# ROS2 Subscribe Joint State
This node subscribes to a joint state command of a robot in a ROS2 JointState message

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Exec In ( inputs:execIn ) | execution | The input execution port | None
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be sent. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | joint_command
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Effort Command ( outputs:effortCommand ) | double[] | Effort commands | None
Exec Out ( outputs:execOut ) | execution | Output execution triggers when a new message is received | None
Joint Names ( outputs:jointNames ) | token[] | Commanded joint names | None
Position Command ( outputs:positionCommand ) | double[] | Position commands | None
Timestamp ( outputs:timeStamp ) | double | ROS2 Timestamp in seconds | 0.0
Velocity Command ( outputs:velocityCommand ) | double[] | Velocity commands | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2SubscribeJointState
Version | 2
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2SubscribeJointState.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Subscribe Joint State
Categories | isaacRos2:subscriber
Generated Class Name | OgnROS2SubscribeJointStateDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
