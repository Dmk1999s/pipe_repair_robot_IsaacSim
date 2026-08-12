<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_image_message.html | title: Ros2ImageMessage — Isaac Sim -->

# Ros2ImageMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2ImageMessage`
classRos2ImageMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `sensor_msgs/msg/Image` message.
Provides functionality to write ROS 2 Image messages that contain image data with specified encoding and dimensions.
Subclassed by isaacsim::ros2::bridge::Ros2ImageMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 Image message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidgenerateBuffer(
constuint32_theight,
constuint32_twidth,
conststd ::string&encoding,
)=0
Generate the buffer (matrix data) according to the image metadata.
It allocates memory for the `data` field, and computes and fills in the values of the other message fields.
Parameters:

- height – [in] Image height.

- width – [in] Image width.

- encoding – [in] Encoding of pixels.

inlinevoid*getBufferPtr()

Get the pointer to the buffer (matrix data).
Provides direct access to the underlying buffer containing the image data.
Returns:
Pointer to the buffer.

inlinesize_tgetTotalBytes()

Get the total size (`step * height`) of the buffer, in bytes.
Returns the total size of the image buffer in bytes.
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
std ::vector<uint8_t>m_buffer

Buffer (matrix data).

size_tm_totalBytes=0

Buffer size.

void*m_msg=nullptr

Message pointer.
