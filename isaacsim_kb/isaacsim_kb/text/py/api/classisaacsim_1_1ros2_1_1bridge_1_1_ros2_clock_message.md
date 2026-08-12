<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_clock_message.html | title: Ros2ClockMessage — Isaac Sim -->

# Ros2ClockMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2ClockMessage`
classRos2ClockMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `rosgraph_msgs/msg/Clock` message.
Provides functionality to read and write ROS 2 Clock messages that contain simulation time information.
Subclassed by isaacsim::ros2::bridge::Ros2ClockMessageImpl
Public Functions
virtualvoidreadData(double&timeStamp)=0

Read the message field values.
Extracts the timestamp value from a ROS 2 Clock message.
Parameters:
timeStamp – [out] Time (seconds).

virtualvoidwriteData(doubletimeStamp)=0

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

virtualconstvoid*getTypeSupportHandle()=0

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

Protected Attributes
void*m_msg=nullptr

Message pointer.
