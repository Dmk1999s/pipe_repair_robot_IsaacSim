<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_bounding_box3_d_message.html | title: Ros2BoundingBox3DMessage — Isaac Sim -->

# Ros2BoundingBox3DMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2BoundingBox3DMessage`
classRos2BoundingBox3DMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `vision_msgs/msg/Detection3DArray` message.
Provides functionality to write ROS 2 Detection3DArray messages that contain 3D bounding box detection information.
Subclassed by isaacsim::ros2::bridge::Ros2BoundingBox3DMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 Detection3DArray message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidwriteBboxData(constvoid*bboxArray, size_tnumBoxes)=0

Write the message field values from the given arguments.
Sets the detection array in a ROS 2 Detection3DArray message.
Parameters:

- bboxArray – [in] Array of `Bbox3DData` struct.

- numBoxes – [in] Number of boxed defined in the array.

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
