<!-- source: py/api/function__ros2_ogn_utils_8h_1a4a9cb814307d4d7700d55f4b4c88071e.html | title: createOgAttributesForFields — Isaac Sim -->

# createOgAttributesForFields
Fully qualified name: `isaacsim::ros2::omnigraph_utils::createOgAttributesForFields`
template<typenameOgnROS2DatabaseDerivedType,boolisOutput,boolclearExistingAttrs>
inlineboolisaacsim ::ros2 ::omnigraph_utils ::createOgAttributesForFields(
OgnROS2DatabaseDerivedType &db,
constNodeObj&nodeObj,
std ::vector<DynamicMessageField>messageFields,
conststd ::stringprependStr,
std ::stringmessageType,
)
Creates OmniGraph attributes for message fields.
Creates dynamic attributes on an OmniGraph node to match the fields of a ROS 2 message. Optionally clears existing attributes before creating new ones.
Template Parameters:

- OgnROS2DatabaseDerivedType – Database type for OmniGraph-ROS2 integration

- isOutput – Whether to create output (true) or input (false) attributes

- clearExistingAttrs – Whether to clear existing attributes before creating new ones

Parameters:

- db – [in] Database instance

- nodeObj – [in] Node object to modify

- messageFields – [in] Vector of message fields to create attributes for

- prependStr – [in] Optional prefix for attribute names

- messageType – [in] Full message type name (for logging)

Returns:
bool True if all attributes were successfully created
