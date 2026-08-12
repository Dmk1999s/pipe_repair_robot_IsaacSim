<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_node_handle.html | title: Ros2NodeHandle — Isaac Sim -->

# Ros2NodeHandle
Fully qualified name: `isaacsim::ros2::bridge::Ros2NodeHandle`
classRos2NodeHandle

Base class that encapsulates a ROS 2 node (`rcl_node_t`) instance.
Provides the interface for managing ROS 2 nodes, which are the primary entry points for communication in the ROS 2 system.
Subclassed by isaacsim::ros2::bridge::Ros2NodeHandleImpl
Public Functions
virtualRos2ContextHandle *getContextHandle()=0

Gets the pointer to the context handler object.
Retrieves the context handler that owns this node.
See also
Ros2ContextHandle for context management details.
Returns:
Pointer to the context handler.

virtualvoid*getNode()=0

Gets the pointer to the ROS 2 node structure.
Returns a pointer to the underlying ROS 2 node structure (`rcl_node_t`).
Warning
This is a low-level access method that should be used with caution.
Returns:
Pointer to the node structure.
