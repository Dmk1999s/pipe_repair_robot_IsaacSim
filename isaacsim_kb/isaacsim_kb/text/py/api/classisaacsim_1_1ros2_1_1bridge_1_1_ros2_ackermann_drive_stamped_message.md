<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_ackermann_drive_stamped_message.html | title: Ros2AckermannDriveStampedMessage — Isaac Sim -->

# Ros2AckermannDriveStampedMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessage`
classRos2AckermannDriveStampedMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `ackermann_msgs/msg/AckermannDriveStamped`.
Provides functionality to read and write ROS 2 AckermannDriveStamped messages that contain control commands for a vehicle with Ackermann steering.
Subclassed by isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 AckermannDriveStamped message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidreadData(
double&timeStamp,
std ::string&frameId,
double&steeringAngle,
double&steeringAngleVelocity,
double&speed,
double&acceleration,
double&jerk,
)=0
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

virtualvoidwriteData(
constdouble&steeringAngle,
constdouble&steeringAngleVelocity,
constdouble&speed,
constdouble&acceleration,
constdouble&jerk,
)=0
Write the message field values from the given arguments.
Sets the Ackermann drive parameters in a ROS 2 AckermannDriveStamped message.
Parameters:

- steeringAngle – [in] Virtual angle.

- steeringAngleVelocity – [in] Rate of change.

- speed – [in] Forward speed.

- acceleration – [in] Acceleration.

- jerk – [in] Jerk.

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
