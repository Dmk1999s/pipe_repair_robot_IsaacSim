<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_point_cloud_message.html | title: Ros2PointCloudMessage — Isaac Sim -->

# Ros2PointCloudMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2PointCloudMessage`
classRos2PointCloudMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `sensor_msgs/msg/PointCloud2` message.
Provides functionality to write ROS 2 PointCloud2 messages that contain point cloud data with an arbitrary number of fields per point.
Subclassed by isaacsim::ros2::bridge::Ros2PointCloudMessageImpl
Public Functions
virtualvoidgenerateBuffer(
constdouble&timeStamp,
conststd ::string&frameId,
constsize_t&width,
constsize_t&height,
constuint32_t&pointStep,
)=0
Generate the buffer (data) according to the point cloud metadata.
It allocates memory for the `data` field, and computes and fills in the values of the other message fields.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

- width – [in] Point cloud width.

- height – [in] Point cloud height.

- pointStep – [in] Length of a point in bytes.

inlinevoid*getBufferPtr()

Get the pointer to the buffer (data).
Provides direct access to the underlying buffer containing the point cloud data.
Returns:
Pointer to the buffer.

inlinesize_tgetTotalBytes()

Get the total size (`width * point_step`) of the buffer, in bytes.
Returns the total size of the point cloud buffer in bytes.
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

Buffer (data).

size_tm_totalBytes=0

Buffer size.

void*m_msg=nullptr

Message pointer.
