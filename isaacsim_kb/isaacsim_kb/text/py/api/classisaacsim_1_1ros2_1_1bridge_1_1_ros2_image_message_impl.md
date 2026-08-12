<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_image_message_impl.html | title: Ros2ImageMessageImpl — Isaac Sim -->

# Ros2ImageMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2ImageMessageImpl`
classRos2ImageMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2ImageMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Image message.
Handles the creation and manipulation of sensor_msgs/msg/Image messages, which contain raw or compressed image data.
Public Functions
Ros2ImageMessageImpl()

virtual~Ros2ImageMessageImpl()

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
Allocates and initializes the image buffer.
Parameters:

- height – [in] Image height in pixels

- width – [in] Image width in pixels

- encoding – [in] Image encoding format (e.g., “rgb8”, “bgr8”)

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

Protected Attributes
std ::vector<uint8_t>m_buffer

Buffer (matrix data).

size_tm_totalBytes=0

Buffer size.

void*m_msg=nullptr

Message pointer.
