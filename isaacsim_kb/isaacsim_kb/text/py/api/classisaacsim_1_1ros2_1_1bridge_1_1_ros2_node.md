<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_node.html | title: Ros2Node — Isaac Sim -->

# Ros2Node
Fully qualified name: `isaacsim::ros2::bridge::Ros2Node`
classRos2Node:publicisaacsim ::core ::includes ::BaseResetNode

Base class for ROS 2 bridge nodes.
This class provides the foundation for ROS 2 nodes in the Isaac Sim bridge. It handles node lifecycle management, initialization, and automatic cleanup of the internal ROS 2 node handle. Derived classes should implement specific node functionality while relying on this base class for core ROS 2 operations.
Public Functions
inlineRos2Node()

Constructor for the ROS 2 node.
Initializes the node by retrieving necessary interfaces:

- Core node framework interface

- ROS 2 bridge interface

- Settings interface for configuration

- ROS 2 factory for node creation

The constructor also configures publishing verification settings based on the extension configuration.

inline~Ros2Node()

Destructor.
Ensures proper cleanup by calling reset()

inlinevirtualvoidreset()

Resets the node handle.
Cleans up the ROS 2 node handle. Derived classes should call this method after cleaning up their own publishers/subscribers.
Note
This is a virtual method that can be overridden by derived classes

inlineboolinitializeNodeHandle(
conststd ::string&nodeName,
conststd ::string&namespaceName,
uint64_tcontextHandleAddr,
)
Initializes the ROS 2 node handle.
Creates and initializes the ROS 2 node handle with the specified name and namespace. This method should be called before performing any operations with the node. Node name changes are only applied after a Stop and Play cycle.
Note
The method sanitizes node names and validates them before initialization
Parameters:

- nodeName – [in] Name for the ROS 2 node

- namespaceName – [in] Namespace for the ROS 2 node

- contextHandleAddr – [in] Memory address of the context handler

Returns:
bool True if initialization succeeded, false otherwise

inlineboolisInitialized()const

Checks if the node is initialized.
Verifies if the node handle has been properly created and initialized
Returns:
bool True if the node handle exists, false otherwise

Public Static Functions
staticinlinestd ::stringaddTopicPrefix(
conststd ::string&prefix,
conststd ::string&topicName,
)
Adds a prefix to a topic name.
Prepends the specified prefix to a topic name, ensuring proper separator character (/) placement between prefix and topic name.
Note
Returns empty string if input topic name is empty
Parameters:

- prefix – [in] Prefix to add to the topic name

- topicName – [in] Original topic name

Returns:
std::string The prefixed topic name

staticinlinestd ::stringcollectNamespace(
conststd ::string&namespaceInput,
constPXR_NS::UsdPrim&startPrim,
constbooltfNode=false,
)
Collects namespace information from USD stage.
Traverses up the USD stage hierarchy from the start prim, collecting namespace information from isaac:namespace attributes. For non-TF nodes, builds a hierarchical namespace. For TF nodes, only uses the highest-level namespace.
Note
Returns input namespace if not empty
Parameters:

- namespaceInput – [in] Initial namespace (if not empty, skips collection)

- startPrim – [in] USD Prim to start namespace collection from

- tfNode – [in] Whether collecting namespace for a TF node

Returns:
std::string Collected namespace string

Protected Attributes
isaacsim ::ros2 ::bridge ::Ros2Bridge *m_ros2Bridge=nullptr

Ros2Bridge (carb) interface.

std ::shared_ptr<Ros2NodeHandle >m_nodeHandle=nullptr

Node handler.

carb::settings::ISettings*m_settings=nullptr

Settings (carb) interface.

boolm_publishWithoutVerification

Whether to publish in a topic even if there are no subscription to it.

std ::shared_ptr<Ros2ContextHandle >*m_contextHandle

Context handler.

isaacsim ::core ::nodes ::CoreNodes *m_coreNodeFramework

CoreNodes (carb) interface.

Ros2Factory *m_factory=nullptr

Factory instance for creating ROS 2 related objects according to the sourced ROS 2 distribution.

std ::stringm_namespaceName

Namespace name.
