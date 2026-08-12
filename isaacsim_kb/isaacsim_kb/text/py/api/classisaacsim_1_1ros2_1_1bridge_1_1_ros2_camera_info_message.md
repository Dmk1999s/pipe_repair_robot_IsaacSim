<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_camera_info_message.html | title: Ros2CameraInfoMessage — Isaac Sim -->

# Ros2CameraInfoMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2CameraInfoMessage`
classRos2CameraInfoMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing a `sensor_msgs/msg/CameraInfo` message.
Provides functionality to write ROS 2 CameraInfo messages that contain camera calibration information such as resolution, intrinsic parameters, distortion parameters, and projection matrices.
Subclassed by isaacsim::ros2::bridge::Ros2CameraInfoMessageImpl
Public Functions
virtualvoidwriteHeader(
constdoubletimeStamp,
conststd ::string&frameId,
)=0
Write the message header.
Sets the header fields in a ROS 2 CameraInfo message.
Parameters:

- timeStamp – [in] Time (seconds).

- frameId – [in]Transform frame with which this data is associated.

virtualvoidwriteResolution(
constuint32_theight,
constuint32_twidth,
)=0
Write the image dimensions (resolution).
Sets the height and width fields in a ROS 2 CameraInfo message.
Parameters:

- height – [in] Image height.

- width – [in] Image width.

virtualvoidwriteIntrinsicMatrix(
constdoublearray[],
constsize_tarraySize,
)=0
Write the intrinsic camera matrix (`K`).
Sets the 3x3 intrinsic camera matrix in a ROS 2 CameraInfo message.
Parameters:

- array – [in] Flattened intrinsic camera matrix.

- arraySize – [in] Array size.

virtualvoidwriteProjectionMatrix(
constdoublearray[],
constsize_tarraySize,
)=0
Write the projection/camera matrix (`P`).
Sets the 3x4 projection matrix in a ROS 2 CameraInfo message.
Parameters:

- array – [in] Flattened projection/camera matrix.

- arraySize – [in] Array size.

virtualvoidwriteRectificationMatrix(
constdoublearray[],
constsize_tarraySize,
)=0
Write the rectification matrix (`R`).
Sets the 3x3 rectification matrix in a ROS 2 CameraInfo message.
Parameters:

- array – [in] Flattened rectification matrix.

- arraySize – [in] Array size.

virtualvoidwriteDistortionParameters(
std ::vector<double>&array,
conststd ::string&distortionModel,
)=0
Write the distortion parameters (`D`).
Sets the distortion parameters in a ROS 2 CameraInfo message based on the specified distortion model.
Parameters:

- array – [in] Distortion parameters (size depending on the distortion model).

- distortionModel – [in] Distortion model.

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
std ::vector<double>m_distortionBuffer

Distortion Buffer (matrix data).

void*m_msg=nullptr

Message pointer.
