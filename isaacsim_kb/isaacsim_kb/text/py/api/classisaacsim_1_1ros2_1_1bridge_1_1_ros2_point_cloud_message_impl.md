<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_point_cloud_message_impl.html | title: Ros2PointCloudMessageImpl — Isaac Sim -->

# Ros2PointCloudMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2PointCloudMessageImpl`
classRos2PointCloudMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2PointCloudMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Point Cloud message.
Handles the creation and manipulation of sensor_msgs/msg/PointCloud2 messages, which contain 3D point cloud data with customizable fields.
Public Functions
Ros2PointCloudMessageImpl()

virtual~Ros2PointCloudMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidgenerateBuffer(
constdouble&timeStamp,
conststd ::string&frameId,
constsize_t&width,
constsize_t&height,
constuint32_t&pointStep,
)
Allocates and initializes the point cloud buffer.
Parameters:

- timeStamp – [in] Time in seconds

- frameId – [in] Frame ID for the point cloud

- width – [in] Number of points in a row

- height – [in] Number of rows (1 for unorganized clouds)

- pointStep – [in] Size of a single point in bytes

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

Protected Attributes
std ::vector<uint8_t>m_buffer

Buffer (data).

size_tm_totalBytes=0

Buffer size.

void*m_msg=nullptr

Message pointer.
