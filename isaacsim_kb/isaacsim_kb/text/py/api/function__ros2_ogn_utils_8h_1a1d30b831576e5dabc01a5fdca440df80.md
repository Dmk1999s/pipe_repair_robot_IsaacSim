<!-- source: py/api/function__ros2_ogn_utils_8h_1a1d30b831576e5dabc01a5fdca440df80.html | title: removeDynamicAttributes — Isaac Sim -->

# removeDynamicAttributes
Fully qualified name: `isaacsim::ros2::omnigraph_utils::removeDynamicAttributes`
template<boolremoveInputs=false,boolremoveOutputs=false>
inlineboolisaacsim ::ros2 ::omnigraph_utils ::removeDynamicAttributes(
constNodeObj&nodeObj,
)
Removes dynamic attributes from a node.
Selectively removes dynamic input and/or output attributes from an OmniGraph node. Useful for resetting a node when reconfiguring its interface based on a new message type.
Template Parameters:

- removeInputs – Whether to remove dynamic input attributes

- removeOutputs – Whether to remove dynamic output attributes

Parameters:
nodeObj – [in] OmniGraph node object to modify

Returns:
bool True if all requested attributes were successfully removed
