<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_laser_scan_message_impl.html | title: Ros2LaserScanMessageImpl — Isaac Sim -->

# Ros2LaserScanMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2LaserScanMessageImpl`
classRos2LaserScanMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2LaserScanMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Laser Scan message.
Handles the creation and manipulation of sensor_msgs/msg/LaserScan messages, which contain 2D laser range finder data.
Public Functions
Ros2LaserScanMessageImpl()

virtual~Ros2LaserScanMessageImpl()

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
)override
Write the message header.
Sets the header fields in a ROS 2 LaserScan message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidgenerateBuffers(constsize_tbuffSize)override

Generate the buffers according to the LaserScan metadata.
It allocates memory for the range and intensities data.
Parameters:
buffSize – [in] buffer size.

virtualvoidwriteData(
constpxr ::GfVec2f&azimuthRange,
constfloat&rotationRate,
constpxr ::GfVec2f&depthRange,
floathorizontalResolution,
floathorizontalFov,
)override
Sets the laser scan data.
Parameters:

- azimuthRange – [in] Min and max angles in degrees

- rotationRate – [in] Scan frequency in Hz

- depthRange – [in] Min and max range values

- horizontalResolution – [in] Angular resolution in degrees

- horizontalFov – [in] Horizontal field of view in degrees

inlinestd ::vector<float>&getRangeData()

Get the buffer (range data).
Provides direct access to the underlying buffer containing the range data.
Returns:
Buffer.

inlinestd ::vector<float>&getIntensitiesData()

Get the buffer (intensities data).
Provides direct access to the underlying buffer containing the intensities data.
Returns:
Buffer.

inlinevoid*getPtr()

Retrieves the message pointer.
Returns the pointer to the underlying ROS 2 message if it has been properly created and initialized.
Note
This method does not perform type checking - the caller is responsible for proper casting to the appropriate message type.
Returns:
Pointer to the message or nullptr if not initialized.

Protected Attributes
std ::vector<float>m_rangeData

Buffer (range data).

std ::vector<float>m_intensitiesData

Buffer (intensities data).

void*m_msg=nullptr

Message pointer.
