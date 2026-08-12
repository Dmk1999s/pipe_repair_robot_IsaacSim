<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_dynamic_message_impl.html | title: Ros2DynamicMessageImpl — Isaac Sim -->

# Ros2DynamicMessageImpl
Fully qualified name: `isaacsim::ros2::bridge::Ros2DynamicMessageImpl`
classRos2DynamicMessageImpl:publicisaacsim ::ros2 ::bridge ::Ros2DynamicMessage ,privateisaacsim ::ros2 ::bridge ::Ros2MessageInterfaceImpl

Implementation of ROS 2 Dynamic Message.
Provides functionality for runtime message type handling, including message field introspection, serialization, and deserialization.
Public Functions
Ros2DynamicMessageImpl(
conststd ::string&pkgName,
conststd ::string&msgSubfolder,
conststd ::string&msgName,
BackendMessageType messageType=BackendMessageType ::eMessage ,
)
Constructor for ROS 2 Dynamic Message implementation.
Parameters:

- pkgName – [in] Name of the ROS 2 package containing the message definition.

- msgSubfolder – [in] Subfolder containing the message definition (e.g., “msg” or “srv”).

- msgName – [in] Name of the message type.

- messageType – [in] Type of the message (default: eMessage).

virtual~Ros2DynamicMessageImpl()

virtualconstvoid*getTypeSupportHandle()

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

virtualstd ::stringgenerateSummary(boolprint)

Generates a summary of the message structure.
Parameters:
print – [in] Whether to print the summary to console

Returns:
std::string Formatted summary string

virtualconstnlohmann::json&readData()

Reads message data as JSON.
Returns:
const nlohmann::json& Reference to JSON representation

virtualconststd ::vector<std ::shared_ptr<void>>&readData(
boolasOgnType,
)
Reads message data as vector.
Parameters:
asOgnType – [in] Whether to convert to OmniGraph types

Returns:
const std::vector<std::shared_ptr<void>>& Vector of field data

virtualvoidwriteData(constnlohmann::json&data)

Writes message data from JSON.
Parameters:
data – [in] JSON data to write

virtualvoidwriteData(
conststd ::vector<std ::shared_ptr<void>>&data,
boolfromOgnType,
)
Writes message data from vector.
Parameters:

- data – [in] Vector of field data

- fromOgnType – [in] Whether data is in OmniGraph types

inlineconststd ::vector<DynamicMessageField >&getMessageFields()

Gets the message field descriptions.
Provides access to the field metadata that describes the message structure.
Returns:
Vector of field descriptions.

inlineconststd ::vector<std ::shared_ptr<void>>&getVectorContainer(
boolasOgnType,
)
Gets the message data container as vector.
Returns a constant vector of non-constant shared pointers, allowing modification of field values but not container structure. This means that the elements of the vector (the message fields) cannot be modified but their content (the message fields’ value) can. This is particularly useful when writing the message data using a vector as a container since it is not necessary to create pointers to the required data types. See Ros2DynamicMessage::writeData for use example.
Note
The returned container is read-only, but the pointed-to data can be modified.
Parameters:
asOgnType – [in] Whether to return OmniGraph or ROS 2 data types.

Returns:
Vector container with shared pointers to field data.

inlineboolisValid()

Checks message validity.
Verifies if the underlying message pointer has been properly initialized.
Returns:
True if message is properly created and initialized, false otherwise.

inlinevoid*getPtr()

Retrieves the message pointer.
Returns the pointer to the underlying ROS 2 message if it has been properly created and initialized.
Note
This method does not perform type checking - the caller is responsible for proper casting to the appropriate message type.
Returns:
Pointer to the message or nullptr if not initialized.

Protected Functions
virtualconstvoid*getIntrospectionMembers()

Gets the introspection members of the ROS2 message type.
Retrieves the introspection members that describe the structure and layout of the ROS2 message type. This is used for dynamic message handling and type introspection.
Returns:
A pointer to the message members definition structure.

virtualvoidparseMessageFields(
conststd ::string&parentName,
constvoid*members,
)
Parses message field definitions.
Parameters:

- parentName – [in] Name of the parent field

- members – [in] Pointer to message members definition

virtualvoidgetMessageValues(
constvoid*members,
uint8_t*messageData,
nlohmann::json&container,
)
Gets message field values as JSON.
Parameters:

- members – [in] Pointer to message members definition

- messageData – [in] Pointer to message data

- container – [out] JSON container to fill

virtualvoidgetMessageValues(
constvoid*members,
uint8_t*messageData,
std ::vector<std ::shared_ptr<void>>&container,
size_t&index,
boolasOgnType,
)
Gets message field values as vector.
Parameters:

- members – [in] Pointer to message members definition

- messageData – [in] Pointer to message data

- container – [out] Vector container to fill

- index – [inout] Current field index

- asOgnType – [in] Whether to convert to OmniGraph types

virtualvoidsetMessageValues(
constvoid*members,
uint8_t*messageData,
constnlohmann::json&container,
)
Sets message field values from JSON.
Parameters:

- members – [in] Pointer to message members definition

- messageData – [out] Pointer to message data

- container – [in] JSON container with field values

virtualvoidsetMessageValues(
constvoid*members,
uint8_t*messageData,
conststd ::vector<std ::shared_ptr<void>>&container,
size_t&index,
boolfromOgnType,
)
Sets message field values from vector.
Parameters:

- members – [in] Pointer to message members definition

- messageData – [out] Pointer to message data

- container – [in] Vector container with field values

- index – [inout] Current field index

- fromOgnType – [in] Whether data is in OmniGraph types

template<typenameArrayType,typenameRosType>
voidgetArray(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
nlohmann::json&array,
)
Gets array values from ROS message and converts them to JSON format.
Template function that extracts array data from a ROS message and stores it in a JSON array.
Template Parameters:

- ArrayType – The ROS array type (e.g., rosidl_runtime_c__float__Sequence)

- RosType – The underlying ROS data type (e.g., float)

Parameters:

- member – [in] Pointer to the message member definition

- data – [in] Pointer to the message data

- array – [out] JSON array to store the extracted values

template<typenameArrayType,typenameRosType,typenameOgnType>
voidgetArray(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
std ::shared_ptr<void>&valuePtr,
boolasOgnType,
)
Gets array values from ROS message and converts them to OmniGraph types.
Template function that extracts array data from a ROS message and converts it to OmniGraph format.
Template Parameters:

- ArrayType – The ROS array type

- RosType – The underlying ROS data type

- OgnType – The target OmniGraph data type

Parameters:

- member – [in] Pointer to the message member definition

- data – [in] Pointer to the message data

- valuePtr – [out] Shared pointer to store the converted data

- asOgnType – [in] Whether to convert to OmniGraph type

template<typenameArrayType,typenameRosType>
voidgetArray(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
std ::vector<RosType >&array,
)
Gets array values from ROS message into a vector.
Template function that extracts array data from a ROS message into a std::vector.
Template Parameters:

- ArrayType – The ROS array type

- RosType – The underlying ROS data type

Parameters:

- member – [in] Pointer to the message member definition

- data – [in] Pointer to the message data

- array – [out] Vector to store the extracted values

template<typenameArrayType,autoArrayInit,typenameRosType>
voidsetArray(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
constnlohmann::json&value,
)
Sets array values in ROS message from JSON data.
Template function that populates a ROS message array from JSON data.
Template Parameters:

- ArrayType – The ROS array type

- ArrayInit – Function pointer to array initialization function

- RosType – The underlying ROS data type

Parameters:

- member – [in] Pointer to the message member definition

- data – [out] Pointer to the message data

- value – [in] JSON value containing the array data

template<typenameArrayType,autoArrayInit,typenameRosType,typenameOgnType>
voidsetArray(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
conststd ::shared_ptr<void>&valuePtr,
boolfromOgnType,
)
Sets array values in ROS message from OmniGraph data.
Template function that populates a ROS message array from OmniGraph data.
Template Parameters:

- ArrayType – The ROS array type

- ArrayInit – Function pointer to array initialization function

- RosType – The underlying ROS data type

- OgnType – The source OmniGraph data type

Parameters:

- member – [in] Pointer to the message member definition

- data – [out] Pointer to the message data

- valuePtr – [in] Shared pointer to the source data

- fromOgnType – [in] Whether the source is in OmniGraph format

template<typenameArrayType,autoArrayInit,typenameRosType>
voidsetArray(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
conststd ::vector<RosType >&array,
)
Sets array values in ROS message from vector data.
Template function that populates a ROS message array from a std::vector.
Template Parameters:

- ArrayType – The ROS array type

- ArrayInit – Function pointer to array initialization function

- RosType – The underlying ROS data type

Parameters:

- member – [in] Pointer to the message member definition

- data – [out] Pointer to the message data

- array – [in] Vector containing the source data

template<typenameRosType,typenameOgnType>
voidgetSingleValue(
uint8_t*data,
std ::shared_ptr<void>&valuePtr,
boolasOgnType,
)
Gets a single value from ROS message and converts to OmniGraph type.
Template function that extracts a single value from a ROS message and optionally converts it to OmniGraph format.
Template Parameters:

- RosType – The ROS data type

- OgnType – The target OmniGraph data type

Parameters:

- data – [in] Pointer to the message data

- valuePtr – [out] Shared pointer to store the converted value

- asOgnType – [in] Whether to convert to OmniGraph type

template<typenameRosType,typenameOgnType>
voidsetSingleValue(
uint8_t*data,
conststd ::shared_ptr<void>&valuePtr,
boolfromOgnType,
)
Sets a single value in ROS message from OmniGraph data.
Template function that sets a single value in a ROS message, optionally converting from OmniGraph format.
Template Parameters:

- RosType – The ROS data type

- OgnType – The source OmniGraph data type

Parameters:

- data – [out] Pointer to the message data

- valuePtr – [in] Shared pointer to the source value

- fromOgnType – [in] Whether the source is in OmniGraph format

voidgetArrayEmbeddedMessage(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
nlohmann::json&array,
)
Gets array of embedded messages as JSON.
Extracts an array of embedded messages from a ROS message and converts them to JSON format. This function handles complex message types that contain nested message structures.
Parameters:

- member – [in] Pointer to the message member definition containing the array

- data – [in] Pointer to the message data

- array – [out] JSON array to store the extracted message data

voidsetArrayEmbeddedMessage(
constrosidl_typesupport_introspection_c__MessageMember*member,
uint8_t*data,
constnlohmann::json&array,
)
Sets array of embedded messages from JSON.
Populates an array of embedded messages in a ROS message from JSON data. This function handles complex message types that contain nested message structures.
Parameters:

- member – [in] Pointer to the message member definition for the array

- data – [out] Pointer to the message data to be populated

- array – [in] JSON array containing the source message data

Protected Attributes
std ::vector<DynamicMessageField >m_messagesFields

Message fields description.

nlohmann::jsonm_messageJsonContainer

JSON message container.

std ::vector<std ::shared_ptr<void>>m_messageVectorRosContainer

ROS 2 data types vector container.

std ::vector<std ::shared_ptr<void>>m_messageVectorOgnContainer

OmniGraph data types vector container.

void*m_msg=nullptr

Message pointer.
