<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_semantic_label_message.html | title: Ros2SemanticLabelMessage — Isaac Sim -->

# Ros2SemanticLabelMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2SemanticLabelMessage`
classRos2SemanticLabelMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `std_msgs/msg/String` message for semantic label.
Provides functionality to write ROS 2 String messages that contain semantic label information.
Subclassed by isaacsim::ros2::bridge::Ros2SemanticLabelMessageImpl
Public Functions
virtualvoidwriteData(conststd ::string&data)=0

Write the message field values from the given arguments.
Sets the string data in a ROS 2 String message.
Parameters:
data – [in] String data.

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
