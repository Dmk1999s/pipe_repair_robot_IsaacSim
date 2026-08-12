<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_twist_message_impl.html | title: Ros2TwistMessageImpl — Isaac Sim -->

# Ros2TwistMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2TwistMessageImpl`
classRos2TwistMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2TwistMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Twist message.
Handles the creation and manipulation of geometry_msgs/msg/Twist messages, which contain linear and angular velocity data.
Public Functions
Ros2TwistMessageImpl()

virtual~Ros2TwistMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidreadData(
pxr ::GfVec3d&linearVelocity,
pxr ::GfVec3d&angularVelocity,
)
Reads the twist message data.
Parameters:

- linearVelocity – [out] Linear velocity vector

- angularVelocity – [out] Angular velocity vector

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
