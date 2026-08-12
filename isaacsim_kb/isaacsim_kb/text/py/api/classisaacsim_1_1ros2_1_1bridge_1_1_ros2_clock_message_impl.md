<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_clock_message_impl.html | title: Ros2ClockMessageImpl — Isaac Sim -->

# Ros2ClockMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2ClockMessageImpl`
classRos2ClockMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2ClockMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Clock message.
Handles the creation and manipulation of rosgraph_msgs/msg/Clock messages, which are used for time synchronization in ROS 2.
Public Functions
Ros2ClockMessageImpl()

virtual~Ros2ClockMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidreadData(double&timeStamp)

Read the message field values.
Extracts the timestamp value from a ROS 2 Clock message.
Parameters:
timeStamp – [out] Time (seconds).

virtualvoidwriteData(doubletimeStamp)

Write the message field values from the given arguments.
Sets the timestamp value in a ROS 2 Clock message.
Parameters:
timeStamp – [in] Time (seconds).

inlinevoid*getPtr()

Retrieves the message pointer.
Returns the pointer to the underlying ROS 2 message if it has been properly created and initialized.
Note
This method does not perform type checking - the caller is responsible for proper casting to the appropriate message type.
Returns:
Pointer to the message or nullptr if not initialized.

Protected Attributes
void*m_msg=nullptr

Message pointer.
