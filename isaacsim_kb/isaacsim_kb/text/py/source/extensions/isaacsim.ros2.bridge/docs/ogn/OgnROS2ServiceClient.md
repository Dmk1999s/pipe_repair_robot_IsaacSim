<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2ServiceClient.html | title: ROS2 Service Client — Isaac Sim -->

# ROS2 Service Client
This node is a generic service client that provides interface for a ROS service. The request/response fields of the service are parsed and are made accessible via the node based on the service specified from messagePackage, messageSubfolder, messageName. The client sends a request (commanded from the node inputs) and receives a response (accessible from the node outputs) from the server.

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
| Metadata | displayGroup = parameters |
Exec In ( inputs:execIn ) | execution | The input execution port | None
Message Name ( inputs:messageName ) | string | Service name (e.g.: AddTwoInts for example_interfaces/srv/AddTwoInts) |
| Metadata | displayGroup = parameters |
Message Package ( inputs:messagePackage ) | string | Package name (e.g.: example_interfaces for example_interfaces/srv/AddTwoInts) |
| Metadata | displayGroup = parameters |
Message Subfolder ( inputs:messageSubfolder ) | string | Subfolder name (e.g.: srv for example_interfaces/srv/AddTwoInts) | srv
| Metadata | displayGroup = parameters |
Node Namespace ( inputs:nodeNamespace ) | string | Name of ROS2 Node, prepends any topic published/subscribed by the node name |
| Metadata | displayGroup = parameters |
Qos Profile ( inputs:qosProfile ) | string | QoS profile config |
| Metadata | displayGroup = parameters |
Service Name ( inputs:serviceName ) | string | Name of ROS2 Service | /service_name
| Metadata | displayGroup = parameters |
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output execution triggers when the response is received | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.OgnROS2ServiceClient
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.OgnROS2ServiceClient.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Service Client
Categories | isaacRos2:service
Generated Class Name | OgnROS2ServiceClientDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
