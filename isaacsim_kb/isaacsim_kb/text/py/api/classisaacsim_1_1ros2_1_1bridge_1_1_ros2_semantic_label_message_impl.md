<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_semantic_label_message_impl.html | title: Ros2SemanticLabelMessageImpl — Isaac Sim -->

# Ros2SemanticLabelMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2SemanticLabelMessageImpl`
classRos2SemanticLabelMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2SemanticLabelMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Semantic Label message.
Handles the creation and manipulation of std_msgs/msg/String messages used for semantic labeling in perception tasks.
Public Functions
Ros2SemanticLabelMessageImpl()

virtual~Ros2SemanticLabelMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidwriteData(conststd ::string&data)

Sets the semantic label data.
Parameters:
data – [in] String containing the semantic label

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
