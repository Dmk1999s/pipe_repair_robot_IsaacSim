<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_ackermann_drive_stamped_message_impl.html | title: Ros2AckermannDriveStampedMessageImpl — Isaac Sim -->

# Ros2AckermannDriveStampedMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessageImpl`
classRos2AckermannDriveStampedMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2AckermannDriveStampedMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Ackermann Drive Stamped message.
Handles the creation and manipulation of ackermann_msgs/msg/AckermannDriveStamped messages, which contain Ackermann steering control commands.
Public Functions
Ros2AckermannDriveStampedMessageImpl()

virtual~Ros2AckermannDriveStampedMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidreadData(
double&timeStamp,
std ::string&frameId,
double&steeringAngle,
double&steeringAngleVelocity,
double&speed,
double&acceleration,
double&jerk,
)
Read the message field values.
Extracts timestamp, frame ID, and Ackermann drive parameters from a ROS 2 AckermannDriveStamped message.
Parameters:

- timeStamp – [out] Time (seconds).

- frameId – [out]Transform frame with which this data is associated.

- steeringAngle – [out] Virtual angle.

- steeringAngleVelocity – [out] Rate of change.

- speed – [out] Forward speed.

- acceleration – [out] Acceleration.

- jerk – [out] Jerk.

virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)
Writes the message header.
Parameters:

- timeStamp – [in] Time in seconds

- frameId – [in] Frame ID for the command

virtualvoidwriteData(
constdouble&steeringAngle,
constdouble&steeringAngleVelocity,
constdouble&speed,
constdouble&acceleration,
constdouble&jerk,
)
Sets the Ackermann drive data.
Parameters:

- steeringAngle – [in] Steering angle in radians

- steeringAngleVelocity – [in] Rate of change of steering angle

- speed – [in] Forward speed

- acceleration – [in] Forward acceleration

- jerk – [in] Rate of change of acceleration

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
