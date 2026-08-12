<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_message_interface_impl.html | title: Ros2MessageInterfaceImpl — Isaac Sim -->

# Ros2MessageInterfaceImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2MessageInterfaceImpl`
classRos2MessageInterfaceImpl:publicisaacsim ::ros2 ::bridge ::Ros2MessageInterface

Implementation of the ROS 2 message interface.
Provides concrete implementation for ROS 2 message handling, including time, string, and header field management. This class serves as a base for specific message type implementations.
Subclassed by isaacsim::ros2::bridge::Ros2AckermannDriveStampedMessageImpl , isaacsim::ros2::bridge::Ros2BoundingBox2DMessageImpl , isaacsim::ros2::bridge::Ros2BoundingBox3DMessageImpl , isaacsim::ros2::bridge::Ros2CameraInfoMessageImpl , isaacsim::ros2::bridge::Ros2ClockMessageImpl , isaacsim::ros2::bridge::Ros2DynamicMessageImpl , isaacsim::ros2::bridge::Ros2ImageMessageImpl , isaacsim::ros2::bridge::Ros2ImuMessageImpl , isaacsim::ros2::bridge::Ros2JointStateMessageImpl , isaacsim::ros2::bridge::Ros2LaserScanMessageImpl , isaacsim::ros2::bridge::Ros2NitrosBridgeImageMessageImpl , isaacsim::ros2::bridge::Ros2OdometryMessageImpl , isaacsim::ros2::bridge::Ros2PointCloudMessageImpl , isaacsim::ros2::bridge::Ros2RawTfTreeMessageImpl , isaacsim::ros2::bridge::Ros2SemanticLabelMessageImpl , isaacsim::ros2::bridge::Ros2TfTreeMessageImpl , isaacsim::ros2::bridge::Ros2TwistMessageImpl
Public Functions
Ros2MessageInterfaceImpl(
conststd ::string&pkgName,
conststd ::string&msgSubfolder,
conststd ::string&msgName,
BackendMessageType messageType=BackendMessageType ::eMessage ,
boolshowLoadingError=false,
)
Constructor for message interface implementation.
Parameters:

- pkgName – [in] ROS 2 package name containing the message definition

- msgSubfolder – [in] Message subfolder (msg, srv, action)

- msgName – [in] Name of the message type

- messageType – [in] Type of message (default: standard message)

- showLoadingError – [in] Whether to show library loading errors

voidwriteRosTime(
constint64_tnanoseconds,
builtin_interfaces__msg__Time&time,
)
Writes a ROS 2 time field.
Parameters:

- nanoseconds – [in] Time in nanoseconds

- time – [out] ROS 2 time structure to fill

voidwriteRosString(
conststd ::string&input,
rosidl_runtime_c__String&output,
)
Writes a ROS 2 string field.
Parameters:

- input – [in] String to write

- output – [out] ROS 2 string structure to fill

voidwriteRosHeader(
conststd ::string&frameId,
constint64_tnanoseconds,
std_msgs__msg__Header&header,
)
Writes a ROS 2 header field.
Parameters:

- frameId – [in] Frame ID for the header

- nanoseconds – [in] Timestamp in nanoseconds

- header – [out] ROS 2 header structure to fill

inlinevoid*getTypeSupportHandleDynamic()

Gets the pointer to the struct containing ROS IDL message type support data.
Retrieves a pointer to the ROS IDL type support structure for the message. The pointer points to a ROS IDL struct if the message is found. It is resolved by calling the `rosidl_typesupport_c` type support handle symbol for the given message name.

[TABLE]
Message type | ROS IDL struct
Topic (Message) | rosidl_message_type_support_t
Service | rosidl_service_type_support_t
Action | rosidl_action_type_support_t
[/TABLE]
Warning
This method may return nullptr if the necessary ROS IDL libraries are not available in the system.
Returns:
The pointer to the struct, or nullptr if not found.

inlinevoid*getTypeSupportIntrospectionHandleDynamic()

Gets the pointer to the struct containing the ROS IDL introspection data.
Retrieves a pointer to the ROS IDL introspection structure for the message. The pointer points to a ROS IDL struct if the message is found. It is resolved by calling the `rosidl_typesupport_introspection_c` type support handle symbol for the given message name and type.

[TABLE]
Message type | ROS IDL struct
Topic (Message) | rosidl_message_type_support_t
Service | rosidl_service_type_support_t
Action | rosidl_message_type_support_t
[/TABLE]
Warning
This method may return nullptr if the necessary ROS IDL introspection libraries are not available in the system.
Returns:
The pointer to the struct, or nullptr if not found.

inlinevoid*create()

Creates a new ROS 2 message instance.
Allocates memory for a new message of the specified type and initializes it. The pointer is resolved by calling the `rosidl_generator_c``__create` symbol for the given message.
Note
The returned message must be destroyed using the destroy() method to prevent memory leaks.
Returns:
Pointer to the newly created message, or nullptr if creation failed.

template<typenameT>
inlinevoiddestroy(T msg)

Destroys a ROS 2 message.
Finalizes the message by freeing its allocated memory. The function is resolved by calling the `rosidl_generator_c``__destroy` symbol for the given message.
Note
This method does nothing if msg is nullptr.
Parameters:
msg – [in] Pointer to the message to destroy.

Pre:
The msg pointer must be a valid message previously created with create() .

Protected Attributes
std ::stringm_pkgName

Message package name.

std ::stringm_msgSubfolder

Message subfolder name.

std ::stringm_msgName

Message name.

BackendMessageType m_msgType

Message type.

std ::shared_ptr<isaacsim ::core ::includes ::LibraryLoader >m_typesupportIntrospectionLibrary

ROS IDL type support introspection library.

std ::shared_ptr<isaacsim ::core ::includes ::LibraryLoader >m_typesupportLibrary

ROS IDL type support library.

std ::shared_ptr<isaacsim ::core ::includes ::LibraryLoader >m_generatorLibrary

ROS IDL generator library.
