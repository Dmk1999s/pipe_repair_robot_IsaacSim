<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_imu_message.html | title: Ros2ImuMessage — Isaac Sim -->

# Ros2ImuMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2ImuMessage`
classRos2ImuMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `sensor_msgs/msg/Imu` message.
Provides functionality to write ROS 2 IMU messages that contain orientation, angular velocity, and linear acceleration data.
Subclassed by isaacsim::ros2::bridge::Ros2ImuMessageImpl
Public Functions
virtualvoidwriteHeader(doubletimeStamp, std ::string&frameId)=0

Write the message header.
Sets the header fields in a ROS 2 IMU message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidwriteAcceleration(
boolcovariance=false,
conststd ::vector<double>&acceleration=std ::vector<double>(),
)=0
Write the `linear_acceleration` or its covariance.
Sets the linear acceleration values or marks the covariance as unknown in a ROS 2 IMU message.
Parameters:

- covariance – [in] If true, only the element 0 of the associated covariance matrix will be written to -1, not the acceleration (regardless of its value). If false, the acceleration values will be written.

- acceleration – [in] Linear acceleration.

virtualvoidwriteVelocity(
boolcovariance=false,
conststd ::vector<double>&velocity=std ::vector<double>(),
)=0
Write the `angular_velocity` or its covariance.
Sets the angular velocity values or marks the covariance as unknown in a ROS 2 IMU message.
Parameters:

- covariance – [in] If true, only the element 0 of the associated covariance matrix will be written to -1, not the velocity (regardless of its value). If false, the velocity values will be written.

- velocity – [in] Angular velocity.

virtualvoidwriteOrientation(
boolcovariance=false,
conststd ::vector<double>&orientation=std ::vector<double>(),
)=0
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
