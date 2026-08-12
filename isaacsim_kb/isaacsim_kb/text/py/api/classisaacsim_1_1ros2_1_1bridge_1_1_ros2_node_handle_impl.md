<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_node_handle_impl.html | title: Ros2NodeHandleImpl — Isaac Sim -->

# Ros2NodeHandleImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2NodeHandleImpl`
classRos2NodeHandleImpl:publicisaacsim ::ros2 ::bridge ::Ros2NodeHandle

Implementation of ROS 2 Node Handle.
Manages a ROS 2 node instance, providing access to the node’s context and internal rcl_node_t structure.
Public Functions
Ros2NodeHandleImpl(
constchar*name,
constchar*namespaceName,
Ros2ContextHandle *contextHandle,
)
Constructor for ROS 2 Node Handle implementation.
Parameters:

- name – [in] Name of the ROS 2 node.

- namespaceName – [in] Namespace for the node.

- contextHandle – [in] Pointer to the ROS 2 context handle.

virtual~Ros2NodeHandleImpl()

virtualRos2ContextHandle *getContextHandle()

Gets the pointer to the context handler object.
Retrieves the context handler that owns this node.
See also
Ros2ContextHandle for context management details.
Returns:
Pointer to the context handler.

virtualvoid*getNode()

Gets the pointer to the ROS 2 node structure.
Returns a pointer to the underlying ROS 2 node structure (`rcl_node_t`).
Warning
This is a low-level access method that should be used with caution.
Returns:
Pointer to the node structure.
