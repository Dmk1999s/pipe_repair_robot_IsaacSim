<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/ogn/OgnROS2Context.html | title: ROS2 Context — Isaac Sim -->

# ROS2 Context
This node creates a ROS2 Context for a given domain ID

## Installation
To use this node enable isaacsim.ros2.bridge in the Extension Manager.

## Inputs

[TABLE]
Name | Type | Descripton | Default
Domain Id ( inputs:domain_id ) | uchar | Domain ID for ROS context | 0
Use Domain ID Env Var ( inputs:useDomainIDEnvVar ) | bool | Set to true to use ROS_DOMAIN_ID environment variable if set. Defaults to domain_id if not found | True
[/TABLE]

## Outputs

[TABLE]
Name | Type | Descripton | Default
Context ( outputs:context ) | uint64 | handle to initialized ROS2 context | 0
[/TABLE]

## Metadata

[TABLE]
Name | Value
Unique ID | isaacsim.ros2.bridge.ROS2Context
Version | 2
Extension | isaacsim.ros2.bridge
Icon | ogn/icons/isaacsim.ros2.bridge.ROS2Context.svg
Has State? | False
Implementation Language | C++
Default Memory Type | cpu
Generated Code Exclusions | None
uiName | ROS2 Context
Categories | isaacRos2
Generated Class Name | OgnROS2ContextDatabase
Python Module | isaacsim.ros2.bridge
[/TABLE]
