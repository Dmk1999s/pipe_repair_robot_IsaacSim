<!-- source: py/api/function__ros2_ogn_utils_8h_1aa1812fe37308c80e8b5e9d4451f5ffde.html | title: writeMessageDataFromNode — Isaac Sim -->

# writeMessageDataFromNode
Fully qualified name: `isaacsim::ros2::omnigraph_utils::writeMessageDataFromNode`
inlineboolisaacsim ::ros2 ::omnigraph_utils ::writeMessageDataFromNode(
OmniGraphDatabase&db,
std ::shared_ptr<Ros2Message>message,
std ::stringprependStr,
boolisOutput,
)
Reads attribute data from an OmniGraph node and writes it to a ROS 2 message.
Transfers data from OmniGraph node attributes to a ROS 2 message. This function handles various data types and their conversion between OmniGraph and ROS 2 representations. It supports both scalar and array attributes of different primitive types.
Parameters:

- db – [in] OmniGraph database instance

- message – [inout] ROS 2 message to be populated with node data

- prependStr – [in] Prefix for attribute names

- isOutput – [in] Whether to read from output (true) or input (false) attributes

Returns:
bool True if data was successfully read from node attributes and written to message
