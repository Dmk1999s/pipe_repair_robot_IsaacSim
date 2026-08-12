<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2ServiceServerResponse.html | title: ROS2 Service Server Response — Isaac Sim -->

# ROS2 Service Server Response
This node is a generic service server that provides interface for a ROS service. The response fields of the service are parsed and are made accessible via the node based on the service specified from messagePackage, messageSubfolder, messageName. The server sends a response (commanded from the node inputs) to the client. This node can only receive the requests, and should be connected to a OgnROS2ServiceServerRequest through the out serverHandle parameter in order to send a response.

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Context ( inputs:context ) | uint64 | ROS2 context handle, Default of zero will use the default global context | 0
| Metadata | displayGroup = parameters |
Message Name ( inputs:messageName ) | string | Service name (e.g.: AddTwoInts for example_interfaces/srv/AddTwoInts) |
| Metadata | displayGroup = parameters |
Message Package ( inputs:messagePackage ) | string | Package name (e.g.: example_interfaces for example_interfaces/srv/AddTwoInts) |
| Metadata | displayGroup = parameters |
Message Subfolder ( inputs:messageSubfolder ) | string | Subfolder name (e.g.: srv for example_interfaces/srv/AddTwoInts) | srv
| Metadata | displayGroup = parameters |
Node Namespace ( inputs:nodeNamespace ) | string | Name of ROS2 Node, prepends any topic published/subscribed by the node name |
| Metadata | displayGroup = parameters |
On Received ( inputs:onReceived ) | execution | The input execution port when a request is received | None
Server Handle ( inputs:serverHandle ) | uint64 | handle to the server | 0
| Metadata | displayGroup = parameters |
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Exec Out ( outputs:execOut ) | execution | Output execution triggers when a response is sent | None
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.OgnROS2ServiceServerResponse
Version | 1
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.OgnROS2ServiceServerResponse.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Service Server Response
Categories | isaacRos2:service
Generated Class Name | OgnROS2ServiceServerResponseDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
