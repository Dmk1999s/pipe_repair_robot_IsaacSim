<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2PublishPointCloud.html | title: ROS2 Publish Point Cloud — Isaac Sim -->

# ROS2 Publish Point Cloud
This node publishes LiDAR scans as a ROS2 PointCloud2 message

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Buffer Size ( inputs:bufferSize ) | uint | Size (in bytes) of the buffer (0 if the input is a texture) | 0
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
Cuda Device Index ( inputs:cudaDeviceIndex ) | int | Index of the device where the data lives (-1 for host data) | -1
Data ( inputs:data ) | pointf[3][] | Buffer array data, must contain data if dataPtr is null | []
Data Ptr ( inputs:dataPtr ) | uint64 | Pointer to the buffer data | 0
Exec In ( inputs:execIn ) | execution | The input execution port | None
Frame Id ( inputs:frameId ) | string | FrameId for ROS2 message | sim_lidar
Node Namespace ( inputs:nodeNamespace ) | string | Namespace of ROS2 Node, prepends any published/subscribed topic by the node namespace |
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
Queue Size ( inputs:queueSize ) | uint64 | The number of messages to queue up before throwing some away, in case messages are collected faster than they can be sent. Only honored if ‘history’ QoS policy was set to ‘keep last’. This setting can be overwritten by qosProfile input. | 10
Timestamp ( inputs:timeStamp ) | double | ROS2 Timestamp in seconds | 0.0
Topic Name ( inputs:topicName ) | string | Name of ROS2 Topic | point_cloud
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2PublishPointCloud
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2PublishPointCloud.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Publish Point Cloud
Categories | isaacRos2:publisher
Generated Class Name | OgnROS2PublishPointCloudDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
