<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_raw_tf_tree_message_impl.html | title: Ros2RawTfTreeMessageImpl — Isaac Sim -->

# Ros2RawTfTreeMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2RawTfTreeMessageImpl`
classRos2RawTfTreeMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2RawTfTreeMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Raw Transform Tree message.
Handles the creation and manipulation of tf2_msgs/msg/TFMessage messages containing a single transform. Used for publishing raw transform data without additional processing.
Public Functions
Ros2RawTfTreeMessageImpl()

virtual~Ros2RawTfTreeMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidwriteData(
constdoubletimeStamp,
conststd ::string&frameId,
conststd ::string&childFrame,
constpxr ::GfVec3d&translation,
constpxr ::GfQuatd&rotation,
)
Sets the transform data.
Parameters:

- timeStamp – [in] Time in seconds

- frameId – [in] Parent frame ID

- childFrame – [in] Child frame ID

- translation – [in] Translation vector

- rotation – [in]Rotation quaternion

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
