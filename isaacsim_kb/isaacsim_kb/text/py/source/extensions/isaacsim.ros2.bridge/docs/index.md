<!-- source: py/source/extensions/isaacsim.ros2.bridge/docs/index.html | title: [isaacsim.ros2.bridge] ROS 2 Bridge — Isaac Sim -->

# [isaacsim.ros2.bridge] ROS 2 Bridge
Version: 4.12.4
The ROS 2 Bridge extension enables communication between the Isaac Sim and ROS 2 systems. It allows for the publishing and subscribing of ROS 2 topics and services via OmniGraph nodes and Action graphs. ROS 2 publishers, subscribers and services are only active when play is pressed. To enable this extension, ensure ROS 2 libraries are sourced in the terminal before running Isaac Sim or source the lightweight ROS 2 libraries included with Isaac Sim as an alternative.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API
Isaac Sim ROS 2 Bridge Interface
This module provides Python bindings for the ROS 2 bridge functionality in Isaac Sim. It enables communication between Isaac Sim and ROS 2, allowing simulation components to interact with ROS 2 nodes, topics, services, and actions.
The bridge supports creating nodes, publishers, subscribers, service clients, service servers, action clients, and action servers directly from Python scripts in Isaac Sim.
classRos2Bridge
Main interface class for ROS 2 bridge functionality.
This class provides the core interface for interacting with ROS 2 functionality within Isaac Sim. It manages the lifecycle of ROS 2 context handlers and provides factory access for creating ROS 2 related objects.
The Ros2Bridge serves as the entry point for all ROS 2 operations in Isaac Sim, including node creation, message publishing, and service handling.
get_startup_status(
self:isaacsim.ros2.bridge._ros2_bridge.Ros2Bridge,
)→boolChecks the initialization status of the ROS 2 bridge.
This method verifies if both the factory and context handler objects have been properly instantiated. These objects are created when the Ros2Bridge interface is first acquired after the plugin is loaded.
Returns:
True if both factory and context handler are successfully instantiated, False otherwise.

Return type:
bool

Note
This method should be called before attempting to use any other methods of this interface. Using other methods when this returns False may result in undefined behavior.

acquire_ros2_bridge_interface(
plugin_name:str=None,
library_path:str=None,
)→isaacsim.ros2.bridge._ros2_bridge.Ros2Bridgerelease_ros2_bridge_interface(
arg0:isaacsim.ros2.bridge._ros2_bridge.Ros2Bridge,
)→None

## Omnigraph Nodes
The extension exposes the following Omnigraph nodes:

## Settings

### Extension Settings
The table list the extension-specific settings.

[TABLE]
Setting name | Description | Type | Default value
ros_distro | ROS 2 distributions to fallback onto if none were sourced. | str | 'system_default'
publish_without_verification | Whether ROS 2 publishers are allowed to publish even if there is no active subscription for their topics. | bool | False
publish_multithreading_disabled | Whether to disable multithreading use in the ROS2PublishImage OmniGraph node. | bool | False
enable_nitros_bridge | Whether to enable image publishing via NITROS | bool | False
[/TABLE]
The extension-specific settings can be either specified (set) or retrieved (get) in one of the following ways:
