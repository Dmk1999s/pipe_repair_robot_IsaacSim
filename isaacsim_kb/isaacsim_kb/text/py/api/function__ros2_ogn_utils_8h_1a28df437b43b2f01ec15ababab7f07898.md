<!-- source: py/api/function__ros2_ogn_utils_8h_1a28df437b43b2f01ec15ababab7f07898.html | title: writeNodeAttributeFromMessage — Isaac Sim -->

# writeNodeAttributeFromMessage
Fully qualified name: `isaacsim::ros2::omnigraph_utils::writeNodeAttributeFromMessage`
inlineboolisaacsim ::ros2 ::omnigraph_utils ::writeNodeAttributeFromMessage(
OmniGraphDatabase&db,
std ::shared_ptr<Ros2Message>message,
std ::stringprependStr,
boolisOutput,
)
Reads data from a ROS 2 message and writes it to OmniGraph node attributes.
Transfers data from a ROS 2 message to OmniGraph node attributes. This function handles various data types and their conversion between ROS 2 and OmniGraph representations. It supports both scalar and array values of different primitive types.
Parameters:

- db – [in] OmniGraph database instance

- message – [in] ROS 2 message to read data from

- prependStr – [in] Prefix for attribute names

- isOutput – [in] Whether to write to output (true) or input (false) attributes

Returns:
bool True if data was successfully read from message and written to node attributes
