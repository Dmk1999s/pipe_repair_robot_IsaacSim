<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_context_handle.html | title: Ros2ContextHandle — Isaac Sim -->

# Ros2ContextHandle
Fully qualified name: `isaacsim::ros2::bridge::Ros2ContextHandle`
classRos2ContextHandle

Encapsulates a ROS 2 context for initialization and cleanup.
Base class that encapsulates a non-global state of a ROS 2 init/shutdown cycle (`rcl_context_t`) instance used in the creation of ROS 2 nodes and other entities. This class manages the lifecycle of a ROS 2 context, including initialization parameters like domain ID, and provides access to the underlying context pointer.
Subclassed by isaacsim::ros2::bridge::Ros2ContextHandleImpl
Public Functions
virtualvoid*getContext()=0

Retrieves the pointer to the ROS 2 context.
Returns a pointer to the underlying ROS 2 context structure (`rcl_context_t`), which is needed when creating nodes and other ROS 2 entities.
Warning
This method may return nullptr if the context is not properly initialized. Always check isValid() before using the returned pointer.
Returns:
Pointer to the ROS 2 context structure.

virtualvoidinit(
intargc,
charconst*const*argv,
boolsetDomainId=false,
size_tdomainId=0,
)=0
Initializes the ROS 2 context.
Initializes the RCL (ROS Client Library) context with the provided command line arguments and domain ID settings. This prepares the context for use with nodes, publishers, subscribers, and other ROS 2 entities.
Note
If setDomainId is false, the domain ID will be determined by the ROS_DOMAIN_ID environment variable, or will default to 0 if not set.
Parameters:

- argc – [in] Number of strings in argv.

- argv – [in] Command line arguments.

- setDomainId – [in] Whether to set the ROS domain ID (if true, overrides ROS_DOMAIN_ID environment variable).

- domainId – [in] ROS domain ID value to use if setDomainId is true.

virtualboolisValid()=0

Checks if the context is valid.
Verifies whether the object holds a valid and initialized ROS 2 context instance.
Note
This method should be called before attempting to use the context for any operations.
Returns:
True if the context is valid and initialized, false otherwise.

virtualboolshutdown(constchar*shutdownReason=nullptr)=0

Shuts down the ROS 2 context.
Performs an orderly shutdown of the ROS 2 context, cleaning up all resources associated with it. This should be called before destroying the context handle to ensure proper cleanup.
Note
If shutdownReason is nullptr, no reason will be provided in logs.
Warning
Failing to shut down a context properly may lead to resource leaks.
Parameters:
shutdownReason – [in] Optional human-readable string describing the shutdown reason.

Returns:
True if the shutdown was completed successfully, false otherwise.
