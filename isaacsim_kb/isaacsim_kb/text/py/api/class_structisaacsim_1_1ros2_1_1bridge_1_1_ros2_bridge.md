<!-- source: py/api/class_structisaacsim_1_1ros2_1_1bridge_1_1_ros2_bridge.html | title: Ros2Bridge — Isaac Sim -->

# Ros2Bridge
Fully qualified name: `isaacsim::ros2::bridge::Ros2Bridge`
classRos2Bridge

Main interface class for the ROS 2 bridge functionality.
The Ros2Bridge class provides the core interface for interacting with ROS 2 functionality within Isaac Sim. It manages the lifecycle of ROS 2 context handlers and provides factory access for creating ROS 2 related objects.
Public Members
uint64_tconst(*getDefaultContextHandleAddr)()

Retrieves the memory address of the ROS 2 context handler.
The Ros2ContextHandle object encapsulates a `rcl_context_t` (non-global state of an init/shutdown cycle) instance used in the creation of ROS 2 nodes and other entities.
Note
This address points to a shared pointer object of type Ros2ContextHandle .
Warning
Do not attempt to dereference this address directly without proper casting to the correct type.
Return:
Memory address of the context handler as a 64-bit unsigned integer.

Ros2Factory *const(*getFactory)()

Retrieves the factory instance for creating ROS 2 objects.
Returns a factory instance that can create various ROS 2 related functions and objects according to the sourced ROS 2 distribution. The factory provides a centralized way to instantiate ROS 2 components.
See also
Ros2Factory for the complete list of available factory methods.
Note
The returned pointer is owned by the bridge implementation and should not be deleted.
Return:
Pointer to the factory instance.

boolconst(*getStartupStatus)()

Checks the initialization status of the bridge.
Verifies if both the factory (Ros2Factory ) and the handler (Ros2ContextHandle ) objects have been properly instantiated. These objects are created when the Ros2Bridge interface is first acquired after the plugin is loaded by the isaacsim.ros2.bridge extension.
Note
This method should be called before attempting to use any other methods of this interface.
Warning
Using other methods when this returns false may result in undefined behavior.
Return:
True if both factory and context handler are successfully instantiated, false otherwise.
