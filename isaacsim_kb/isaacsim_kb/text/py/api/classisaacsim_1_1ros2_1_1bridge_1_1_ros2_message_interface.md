<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_message_interface.html | title: Ros2MessageInterface — Isaac Sim -->

# Ros2MessageInterface
Fully qualified name: `isaacsim::ros2::bridge::Ros2MessageInterface`
classRos2MessageInterface

Base class for ROS 2 message definition/generation via ROS Interface Definition Language (IDL).
Provides facilities for dynamically loading and creating ROS 2 message types using the ROS IDL mechanism. This class handles the loading of message type libraries and creation/destruction of message instances.
Subclassed by isaacsim::ros2::bridge::Ros2MessageInterfaceImpl
Public Functions
inlineRos2MessageInterface(
std ::stringpkgName,
std ::stringmsgSubfolder,
std ::stringmsgName,
BackendMessageType messageType=BackendMessageType ::eMessage ,
boolshowLoadingError=false,
)
Constructor for Ros2MessageInterface .
Initializes the message interface by loading the required ROS IDL libraries for the specified message type.
Note
The full message type is constructed as `pkgName`/`msgSubfolder`/`msgName`.
Parameters:

- pkgName – [in] Message package name (e.g.: `"std_msgs"` for `std_msgs/msg/Int32`).

- msgSubfolder – [in] Message subfolder name (e.g.: `"msg"` for `std_msgs/msg/Int32`).

- msgName – [in] Message name (e.g.: `"Int32"` for `std_msgs/msg/Int32`).

- messageType – [in] Message type specification.

- showLoadingError – [in] Whether to print ROS IDL libraries load errors to the console.

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
