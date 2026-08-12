<!-- source: py/api/classisaacsim_1_1ros2_1_1bridge_1_1_ros2_dynamic_message.html | title: Ros2DynamicMessage — Isaac Sim -->

# Ros2DynamicMessage
Fully qualified name: `isaacsim::ros2::bridge::Ros2DynamicMessage`
classRos2DynamicMessage:publicisaacsim ::ros2 ::bridge ::Ros2Message

Class implementing dynamic ROS 2 messages.
Provides runtime definition and manipulation of ROS 2 message types. Supports both JSON and vector-based message processing.
Warning
JSON processing has significant computational overhead compared to vector processing.
Subclassed by isaacsim::ros2::bridge::Ros2DynamicMessageImpl
Public Functions
virtualstd ::stringgenerateSummary(boolprint)=0

Generates a human-readable message structure summary.
Creates a formatted table showing the message structure including:

```
Message: sensor_msgs/msg/PointCloud2 (topic | message)
Idx Array ROS type OGN type Name
=== ===== ========================= ========================= ====
0 no INT32 (int32_t) eInt (int32_t) header:stamp:sec
1 no UINT32 (uint32_t) eUInt (uint32_t) header:stamp:nanosec
2 no STRING (std::string) eToken (std::string) header:frame_id
3 no UINT32 (uint32_t) eUInt (uint32_t) height
4 no UINT32 (uint32_t) eUInt (uint32_t) width
5 yes MESSAGE (nlohmann::json) eUnknown (nlohmann::json) fields
6 no BOOLEAN (bool) eBool (bool) is_bigendian
7 no UINT32 (uint32_t) eUInt (uint32_t) point_step
8 no UINT32 (uint32_t) eUInt (uint32_t) row_step
9 yes UINT8 (uint8_t) eUInt (uint32_t) data
10 no BOOLEAN (bool) eBool (bool) is_dense
```
Parameters:
print – [in] Whether to output the summary to console.

Returns:
Formatted string containing the message structure.

virtualconstnlohmann::json&readData()=0

Reads message data as JSON.
Retrieves the current message data as a JSON object for easy manipulation.
Warning
JSON processing is convenient but has higher computational overhead.
Returns:
Reference to JSON object containing message data.

virtualconststd ::vector<std ::shared_ptr<void>>&readData(
boolasOgnType,
)=0
Reads message data as vector of shared pointers.
Retrieves the current message data as a vector of type-erased shared pointers, which can hold either ROS or OmniGraph data types.
Note
Vector-based operations are more efficient than JSON for performance-critical code.
Parameters:
asOgnType – [in] Whether to return OmniGraph or ROS 2 data types.

Returns:
Vector of message field data.

virtualvoidwriteData(constnlohmann::json&data)=0

Writes message data from JSON.
Updates the message with data provided in a JSON object.
Warning
JSON processing is convenient but has higher computational overhead.
Parameters:
data – [in] JSON object containing message data.

virtualvoidwriteData(
conststd ::vector<std ::shared_ptr<void>>&data,
boolfromOgnType,
)=0
Writes message data from vector of shared pointers.
Updates the message with data provided in a vector of type-erased shared pointers.
Note
Vector-based operations are more efficient than JSON for performance-critical code.
Parameters:

- data – [in] Vector containing message field data.

- fromOgnType – [in] Whether input data uses OmniGraph types.

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

virtualconstvoid*getTypeSupportHandle()=0

Gets the type support handle for the message.
Returns a pointer to the ROS IDL message type support data structure. The actual type depends on the message category:

- Topic: rosidl_message_type_support_t

- Service: rosidl_service_type_support_t

- Action: rosidl_action_type_support_t

Returns:
Pointer to the type support structure or nullptr.

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
