<!-- source: py/api/function__ros2_ogn_utils_8h_1aff79b645d5c8cab2a20547920e25de80.html | title: findMatchingAttribute — Isaac Sim -->

# findMatchingAttribute
Fully qualified name: `isaacsim::ros2::omnigraph_utils::findMatchingAttribute`
template<classOgnROS2DatabaseDerivedType,boolisOutput,boolclearExistingAttrs>
inlineboolisaacsim ::ros2 ::omnigraph_utils ::findMatchingAttribute(
OgnROS2DatabaseDerivedType &db,
constNodeObj&nodeObj,
std ::vector<DynamicMessageField>messageFields,
conststd ::stringprependStr,
)
Checks if node attributes match message fields.
Verifies if a node’s dynamic attributes match the specified message fields in name and type. Used to determine if a node needs to be reconfigured for a different message type.
Template Parameters:

- OgnROS2DatabaseDerivedType – Database type for OmniGraph-ROS2 integration

- isOutput – Whether to check output (true) or input (false) attributes

- clearExistingAttrs – Whether to check all attributes match (true) or just that required ones exist (false)

Parameters:

- db – [in] Database instance

- nodeObj – [in] Node object to check

- messageFields – [in] Vector of message fields to match against node attributes

- prependStr – [in] Optional prefix for attribute names

Returns:
bool True if attributes match message fields according to specified criteria
