<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_message.html | title: Ros2Message — Isaac Sim -->

# Ros2Message
Fully qualified name: `isaacsim::ros2::bridge::Ros2Message`
classRos2Message

Base class for all ROS 2 message encapsulations.
Provides the foundation for ROS 2 message handling with basic functionality for message pointer management and type support.
Subclassed by isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessage , isaacsim::ros2::bridge::Ros2BoundingBox2DMessage , isaacsim::ros2::bridge::Ros2BoundingBox3DMessage , isaacsim::ros2::bridge::Ros2CameraInfoMessage , isaacsim::ros2::bridge::Ros2ClockMessage , isaacsim::ros2::bridge::Ros2DynamicMessage , isaacsim::ros2::bridge::Ros2ImageMessage , isaacsim::ros2::bridge::Ros2ImuMessage , isaacsim::ros2::bridge::Ros2JointStateMessage , isaacsim::ros2::bridge::Ros2LaserScanMessage , isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessage , isaacsim::ros2::bridge::Ros2OdometryMessage , isaacsim::ros2::bridge::Ros2PointCloudMessage , isaacsim::ros2::bridge::Ros2RawTfTreeMessage , isaacsim::ros2::bridge::Ros2SemanticLabelMessage , isaacsim::ros2::bridge::Ros2TfTreeMessage , isaacsim::ros2::bridge::Ros2TwistMessage
Public Functions
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
