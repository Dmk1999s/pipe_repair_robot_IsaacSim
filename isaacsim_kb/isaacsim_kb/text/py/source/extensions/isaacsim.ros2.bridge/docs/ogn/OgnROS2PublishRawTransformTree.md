<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2PublishRawTransformTree.html | title: ROS2 Publish Raw Transform Tree — Isaac Sim -->

# ROS2 Publish Raw Transform Tree
This node publishes a user-defined transformation between any two coordinate frames as a ROS2 Transform Tree

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Child Frame Id ( inputs:childFrameId ) | string | Child frameId for ROS2 TF message | base_link
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Exec In ( inputs:execIn ) | execution | The input execution port | None
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Parent Frame Id ( inputs:parentFrameId ) | string | Parent frameId for ROS2 TF message | odom
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be sent. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Rotation ( inputs:rotation ) | quatd[4] | Rotation as a quaternion (IJKR) | [0.0, 0.0, 0.0, 1.0]
Static Publisher ( inputs:staticPublisher ) | bool | If enabled this will override QoS settings to publish static transform trees, similar to tf2::StaticTransformBroadcaster | False
Timestamp ( inputs:timeStamp ) | double | ROS2 Timestamp in seconds | 0.0
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | tf
Translation ( inputs:translation ) | vectord[3] | Translation vector in meters | [0.0, 0.0, 0.0]
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2PublishRawTransformTree
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2PublishRawTransformTree.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Publish Raw Transform Tree
Categories | isaacRos2:publisher
Generated Class Name | OgnROS2PublishRawTransformTreeDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
