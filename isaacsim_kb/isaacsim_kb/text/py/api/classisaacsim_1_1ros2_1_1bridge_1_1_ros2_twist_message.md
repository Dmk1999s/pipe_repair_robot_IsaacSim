<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_twist_message.html | title: Ros2TwistMessage — Isaac Sim -->

# Ros2TwistMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2TwistMessage`
classRos2TwistMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `geometry_msgs/msg/Twist`.
Provides functionality to read ROS 2 Twist messages that contain linear and angular velocity information.
Subclassed by isaacsim::ros2::bridge::Ros2TwistMessageImpl
Public Functions
virtualvoidreadData(
pxr ::GfVec3d&linearVelocity,
pxr ::GfVec3d&angularVelocity,
)=0
Read the message field values.
Extracts linear and angular velocity from a ROS 2 Twist message.
Parameters:

- linearVelocity – [out] Linear velocity.

- angularVelocity – [out] Angular velocity.

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
