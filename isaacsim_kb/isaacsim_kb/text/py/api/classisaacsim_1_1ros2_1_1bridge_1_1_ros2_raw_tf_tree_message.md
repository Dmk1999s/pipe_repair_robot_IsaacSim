<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_raw_tf_tree_message.html | title: Ros2RawTfTreeMessage — Isaac Sim -->

# Ros2RawTfTreeMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2RawTfTreeMessage`
classRos2RawTfTreeMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `tf2_msgs/msg/TFMessage` message with only one transform.
Provides functionality to write ROS 2 TFMessage messages that contain a single transform between coordinate frames.
Subclassed by isaacsim::ros2::bridge::Ros2RawTfTreeMessageImpl
Public Functions
virtualvoidwriteData(
constdoubletimeStamp,
conststd ::string&frameId,
conststd ::string&childFrame,
constpxr ::GfVec3d&translation,
constpxr ::GfQuatd&rotation,
)=0
Write the message field values from the given arguments.
Sets the transform data in a ROS 2 TFMessage message with a single transform.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

- childFrame – [in] Frame ID of the child frame to which this transform points.

- translation – [in] Translation of child frame from header frame.

- rotation – [in]Rotation of child frame from header frame.

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
