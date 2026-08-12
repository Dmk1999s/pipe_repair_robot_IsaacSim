<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_nitros_bridge_image_message.html | title: Ros2NitrosBridgeImageMessage — Isaac Sim -->

# Ros2NitrosBridgeImageMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessage`
classRos2NitrosBridgeImageMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `isaac_ros_nitros_bridge_interfaces/msg/NitrosBridgeImage` message.
Provides functionality to write ROS 2 NitrosBridgeImage messages that enable zero-copy transfer of image data between processes using CUDA memory.
Subclassed by isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 NitrosBridgeImage message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidgenerateBuffer(
constuint32_theight,
constuint32_twidth,
conststd ::string&encoding,
)=0
Compute and fill in the values of the other message fields.
This method is named the same as Ros2ImageMessage::generateBuffer for compatibility. Since the NitrosBridgeImage message does not define a buffer, no memory allocation is performed. It only computes and fills in the values of the other message fields.
Parameters:

- height – [in] Image height.

- width – [in] Image width.

- encoding – [in] Encoding of pixels.

virtualvoidwriteData(conststd ::vector<int32_t>&data)=0

Write the `data` field.
Sets the data field containing the process ID and CUDA memory block file-descriptor in a ROS 2 NitrosBridgeImage message.
Parameters:
data – [in] Calling process ID and the CUDA memory block file-descriptor.

inlinevoid*getBufferPtr()

Get the pointer to the buffer.
This method is named the same as Ros2ImageMessage::getBufferPtr for compatibility. Since the NitrosBridgeImage message does not define a buffer, it always return `nullptr`.
Returns:
`nullptr`.

inlinesize_tgetTotalBytes()

Get the total size (`step * height`) of the buffer, in bytes.
Returns the total size of the image data in bytes.
Returns:
Buffer size.

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
size_tm_totalBytes=0

Buffer size.

std ::vector<int32_t>m_imageData

Calling process ID and the CUDA memory block file-descriptor.

void*m_msg=nullptr

Message pointer.
