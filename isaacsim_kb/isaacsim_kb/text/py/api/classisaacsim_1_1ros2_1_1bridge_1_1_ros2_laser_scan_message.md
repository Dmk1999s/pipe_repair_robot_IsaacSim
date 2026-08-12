<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_laser_scan_message.html | title: Ros2LaserScanMessage — Isaac Sim -->

# Ros2LaserScanMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2LaserScanMessage`
classRos2LaserScanMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `sensor_msgs/msg/LaserScan` message.
Provides functionality to write ROS 2 LaserScan messages that contain data from a planar laser range-finder.
Subclassed by isaacsim::ros2::bridge::Ros2LaserScanMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 LaserScan message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidgenerateBuffers(constsize_tbuffSize)=0

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
)=0
Write the message field values from the given arguments.
Sets all fields in a ROS 2 LaserScan message.
Parameters:

- azimuthRange – [in] Start (`angle_min`) and end (`angle_max`) angles of the scan in degrees.

- rotationRate – [in] Scan frequency in Hz (`1 / scan_time`).

- depthRange – [in] Minimum (`range_min`) and maximum (`range_max`) range values.

- horizontalResolution – [in] Angular distance (`angle_increment`) between measurements in degrees.

- horizontalFov – [in] Horizontal field of view (`360 * time_increment * ranges.size / scan_time`) in degrees.

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

virtualconstvoid*getTypeSupportHandle()=0

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

Protected Attributes
std ::vector<float>m_rangeData

Buffer (range data).

std ::vector<float>m_intensitiesData

Buffer (intensities data).

void*m_msg=nullptr

Message pointer.
