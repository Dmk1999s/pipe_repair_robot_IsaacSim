<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_odometry_message_impl.html | title: Ros2OdometryMessageImpl — Isaac Sim -->

# Ros2OdometryMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2OdometryMessageImpl`
classRos2OdometryMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2OdometryMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Odometry message.
Handles the creation and manipulation of nav_msgs/msg/Odometry messages, which contain robot pose and velocity information.
Public Functions
Ros2OdometryMessageImpl()

virtual~Ros2OdometryMessageImpl()

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

- frameId – [in] Frame ID for the odometry data

virtualvoidwriteData(
std ::string&childFrame,
constpxr ::GfVec3d&linearVelocity,
constpxr ::GfVec3d&angularVelocity,
constpxr ::GfVec3d&robotFront,
constpxr ::GfVec3d&robotSide,
constpxr ::GfVec3d&robotUp,
doubleunitScale,
constpxr ::GfVec3d&position,
constpxr ::GfQuatd&orientation,
boolpublishRawVelocities,
)
Sets the odometry data.
Parameters:

- childFrame – [in] Child frame ID for the transform

- linearVelocity – [in] Linear velocity vector

- angularVelocity – [in] Angular velocity vector

- robotFront – [in] Robot’s front direction vector

- robotSide – [in] Robot’s side direction vector

- robotUp – [in] Robot’s up direction vector

- unitScale – [in] Scale factor for unit conversion

- position – [in] Robot’s position vector

- orientation – [in] Robot’s orientation quaternion

- publishRawVelocities – [in] Whether to publish raw velocities

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
