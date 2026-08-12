<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_bounding_box3_d_message_impl.html | title: Ros2BoundingBox3DMessageImpl — Isaac Sim -->

# Ros2BoundingBox3DMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2BoundingBox3DMessageImpl`
classRos2BoundingBox3DMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2BoundingBox3DMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 3D Bounding Box message.
Handles the creation and manipulation of vision_msgs/msg/Detection3DArray messages, which contain 3D object detection results.
Public Functions
Ros2BoundingBox3DMessageImpl()

virtual~Ros2BoundingBox3DMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)
Writes the message header.
Parameters:

- timeStamp – [in] Time in seconds

- frameId – [in] Frame ID for the detections

virtualvoidwriteBboxData(constvoid*bboxArray, size_tnumBoxes)

Sets the bounding box data.
Parameters:

- bboxArray – [in] Array of 3D bounding box data

- numBoxes – [in] Number of bounding boxes in the array

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
