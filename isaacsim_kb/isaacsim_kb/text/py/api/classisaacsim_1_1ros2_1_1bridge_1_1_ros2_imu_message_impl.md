<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_imu_message_impl.html | title: Ros2ImuMessageImpl — Isaac Sim -->

# Ros2ImuMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2ImuMessageImpl`
classRos2ImuMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2ImuMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 IMU message.
Handles the creation and manipulation of sensor_msgs/msg/Imu messages, which contain inertial measurement unit data including orientation, angular velocity, and linear acceleration.
Public Functions
Ros2ImuMessageImpl()

virtual~Ros2ImuMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualvoidwriteHeader(doubletimeStamp, std ::string&frameId)

Write the message header.
Sets the header fields in a ROS 2 IMU message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidwriteAcceleration(
boolcovariance,
conststd ::vector<double>&acceleration,
)
Write the `linear_acceleration` or its covariance.
Sets the linear acceleration values or marks the covariance as unknown in a ROS 2 IMU message.
Parameters:

- covariance – [in] If true, only the element 0 of the associated covariance matrix will be written to -1, not the acceleration (regardless of its value). If false, the acceleration values will be written.

- acceleration – [in] Linear acceleration.

virtualvoidwriteVelocity(
boolcovariance,
conststd ::vector<double>&velocity,
)
Write the `angular_velocity` or its covariance.
Sets the angular velocity values or marks the covariance as unknown in a ROS 2 IMU message.
Parameters:

- covariance – [in] If true, only the element 0 of the associated covariance matrix will be written to -1, not the velocity (regardless of its value). If false, the velocity values will be written.

- velocity – [in] Angular velocity.

virtualvoidwriteOrientation(
boolcovariance,
conststd ::vector<double>&orientation,
)
Write the `orientation` or its covariance.
Sets the orientation values or marks the covariance as unknown in a ROS 2 IMU message.
Parameters:

- covariance – [in] If true, only the element 0 of the associated covariance matrix will be written to -1, not the orientation (regardless of its value). If false, the orientation values will be written.

- orientation – [in] Orientation.

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
