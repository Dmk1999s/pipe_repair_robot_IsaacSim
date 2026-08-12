<!-- source: py/api/function__ros2_ogn_utils_8h_1a6ab9516f1c46609dd77448b2e38ce85c.html | title: createOgAttributesForMessage — Isaac Sim -->

# createOgAttributesForMessage
Fully qualified name: `isaacsim::ros2::omnigraph_utils::createOgAttributesForMessage`
template<typenameOgnROS2DatabaseDerivedType,boolisOutput,boolclearExistingAttrs=true>
inlineboolisaacsim ::ros2 ::omnigraph_utils ::createOgAttributesForMessage(
OgnROS2DatabaseDerivedType &db,
constNodeObj&nodeObj,
conststd ::string&messagePackage,
conststd ::string&messageSubfolder,
conststd ::string&messageName,
std ::shared_ptr<Ros2Message>message,
conststd ::stringprependStr,
)
Creates OmniGraph attributes for a ROS 2 message.
Creates dynamic attributes on an OmniGraph node to match the fields of a ROS 2 message. This is a higher-level function that validates the message type, obtains its fields, and calls createOgAttributesForFields to create the node attributes.
Template Parameters:

- OgnROS2DatabaseDerivedType – Database type for OmniGraph-ROS2 integration

- isOutput – Whether to create output (true) or input (false) attributes

- clearExistingAttrs – Whether to clear existing attributes before creating new ones

Parameters:

- db – [in] Database instance

- nodeObj – [in] Node object to modify

- messagePackage – [in] ROS 2 package containing the message definition

- messageSubfolder – [in] Subfolder within the package (e.g., “msg”, “srv”)

- messageName – [in] Name of the message type

- message – [in] Shared pointer to the message instance

- prependStr – [in] Optional prefix for attribute names

Returns:
bool True if all attributes were successfully created
