<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_camera_info_message_impl.html | title: Ros2CameraInfoMessageImpl — Isaac Sim -->

# Ros2CameraInfoMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2CameraInfoMessageImpl`
classRos2CameraInfoMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2CameraInfoMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Camera Info message.
Handles the creation and manipulation of sensor_msgs/msg/CameraInfo messages, which contain camera calibration data and image metadata.
Public Functions
Ros2CameraInfoMessageImpl()

virtual~Ros2CameraInfoMessageImpl()

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

- frameId – [in] Frame ID for the camera

virtualvoidwriteResolution(
constuint32_theight,
constuint32_twidth,
)
Sets the image resolution.
Parameters:

- height – [in] Image height in pixels

- width – [in] Image width in pixels

virtualvoidwriteIntrinsicMatrix(
constdoublearray[],
constsize_tarraySize,
)
Sets the camera intrinsic matrix.
Parameters:

- array – [in] Flattened 3x3 intrinsic matrix

- arraySize – [in] Size of the array (should be 9)

virtualvoidwriteProjectionMatrix(
constdoublearray[],
constsize_tarraySize,
)
Sets the camera projection matrix.
Parameters:

- array – [in] Flattened 3x4 projection matrix

- arraySize – [in] Size of the array (should be 12)

virtualvoidwriteRectificationMatrix(
constdoublearray[],
constsize_tarraySize,
)
Sets the rectification matrix.
Parameters:

- array – [in] Flattened 3x3 rectification matrix

- arraySize – [in] Size of the array (should be 9)

virtualvoidwriteDistortionParameters(
std ::vector<double>&array,
conststd ::string&distortionModel,
)
Sets the distortion parameters.
Parameters:

- array – [in] Vector of distortion coefficients

- distortionModel – [in] Name of the distortion model

inlinevoid*getPtr()

Retrieves the message pointer.
Returns the pointer to the underlying ROS 2 message if it has been properly created and initialized.
Note
This method does not perform type checking - the caller is responsible for proper casting to the appropriate message type.
Returns:
Pointer to the message or nullptr if not initialized.

Protected Attributes
std ::vector<double>m_distortionBuffer

Distortion Buffer (matrix data).

void*m_msg=nullptr

Message pointer.
