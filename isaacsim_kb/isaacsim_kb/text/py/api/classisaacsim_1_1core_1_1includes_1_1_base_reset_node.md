<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_base_reset_node.html | title: BaseResetNode — Isaac Sim -->

# BaseResetNode
Fully qualified name: `isaacsim::core::includes::BaseResetNode`
classBaseResetNode

Base class for nodes that automatically reset their state when simulation is stopped.
This class provides automatic reset functionality for nodes in the simulation graph. It subscribes to the timeline event stream and triggers a reset when a stop event is received. Derived classes must implement the reset() function to define their specific reset behavior.
The class handles:

- Timeline event subscription management

- Automatic cleanup of subscriptions

- Reset triggering on simulation stop

Note
This class uses RAII principles to manage timeline event subscriptions
Warning
Derived classes must implement reset() or a compilation error will occur
Subclassed by isaacsim::ros2::bridge::Ros2Node
Public Functions
inlineBaseResetNode()

Constructs a new BaseResetNode instance.
Sets up the timeline event subscription to automatically trigger reset on simulation stop. The subscription is created with the following characteristics:

- Listens for eStop events from the timeline

- Automatically triggers reset() when stop occurs

- Uses a unique handler name for identification

Post:
Timeline event subscription is created and active

Post:
Timeline interface is cached and ready for use

inlinevirtual~BaseResetNode()

Virtual destructor to ensure proper cleanup of derived classes.
Cleans up the timeline event subscription using RAII principles. The subscription is automatically released when the object is destroyed.
Note
The timeline interface pointer is not explicitly cleaned up as it’s managed by carb

virtualvoidreset()=0

Pure virtual function to reset the node’s state.
This function is called automatically when the simulation is stopped. Derived classes must implement this function to define their specific reset behavior.
Note
This function is called from the timeline event handler thread
Warning
Implementation must be thread-safe as it may be called asynchronously
