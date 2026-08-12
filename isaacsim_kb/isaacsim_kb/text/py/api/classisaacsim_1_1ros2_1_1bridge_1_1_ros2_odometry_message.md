<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_odometry_message.html | title: Ros2OdometryMessage — Isaac Sim -->

# Ros2OdometryMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2OdometryMessage`
classRos2OdometryMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `nav_msgs/msg/Odometry` message.
Provides functionality to write ROS 2 Odometry messages that contain position and velocity information in free space.
Subclassed by isaacsim::ros2::bridge::Ros2OdometryMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 Odometry message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

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
)=0
Write the message field values from the given arguments.
Sets the pose, twist, and child frame fields in a ROS 2 Odometry message. Optionally transforms velocities to the robot’s coordinate frame.
Parameters:

- childFrame – [in] Frame id the pose points to.

- linearVelocity – [in] Linear velocity.

- angularVelocity – [in] Angular velocity.

- robotFront – [in] Front normalized vector.

- robotSide – [in] Side normalized vector.

- robotUp – [in] Up normalized vector.

- unitScale – [in] Unit scale of the stage.

- position – [in] Position.

- orientation – [in] Orientation.

- publishRawVelocities – [in] If enabled, raw velocities are published. Otherwise velocities are projected in the robot frame before being published.

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
void*m_msg=nullptr

Message pointer.
