<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_nitros_bridge_image_message_impl.html | title: Ros2NitrosBridgeImageMessageImpl — Isaac Sim -->

# Ros2NitrosBridgeImageMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessageImpl`
classRos2NitrosBridgeImageMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2NitrosBridgeImageMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of NITROS Bridge Image message.
Handles the creation and manipulation of isaac_ros_nitros_bridge_interfaces/msg/NitrosBridgeImage messages, which are used for efficient image data transfer in the NVIDIA Isaac ROS pipeline.
Public Functions
Ros2NitrosBridgeImageMessageImpl()

virtual~Ros2NitrosBridgeImageMessageImpl()

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

- frameId – [in] Frame ID for the image

virtualvoidgenerateBuffer(
constuint32_theight,
constuint32_twidth,
conststd ::string&encoding,
)
Initializes the image metadata.
Parameters:

- height – [in] Image height in pixels

- width – [in] Image width in pixels

- encoding – [in] Image encoding format

virtualvoidwriteData(conststd ::vector<int32_t>&imageData)

Sets the CUDA memory block data.
Parameters:
imageData – [in] Vector containing process ID and CUDA memory block file descriptor

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

Protected Attributes
size_tm_totalBytes=0

Buffer size.

std ::vector<int32_t>m_imageData

Calling process ID and the CUDA memory block file-descriptor.

void*m_msg=nullptr

Message pointer.
