<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2PublishSemanticLabels.html | title: ROS2 Publish Semantic Labels — Isaac Sim -->

# ROS2 Publish Semantic Labels
This node publishes ROS2 semantic label messages

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Exec In ( inputs:execIn ) | execution | The input execution port. | None
Id To Labels ( inputs:idToLabels ) | string | Mapping from id to semantic labels. |
Ids ( inputs:ids ) | uint[] | Unoccluded semantic u ids (or color, if colorize is set to True). | []
Labels ( inputs:labels ) | token[] | Prim path of the prim. | []
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be sent. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Semantics ( inputs:semantics ) | token[] | Semantic labels that correspeond to the ids. | []
Time Stamp ( inputs:timeStamp ) | double | Time in seconds to use when publishing the message | 0.0
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | labels
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2PublishSemanticLabels
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2PublishSemanticLabels.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Publish Semantic Labels
Categories | isaacRos2:publisher
Generated Class Name | OgnROS2PublishSemanticLabelsDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
