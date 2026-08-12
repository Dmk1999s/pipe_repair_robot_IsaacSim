<!-- source: py/api/function__ros2_ogn_utils_8h_1a50ec6511c78cf0f67fcdc87c3eeb6744.html | title: inputOutput — Isaac Sim -->

# inputOutput
Fully qualified name: `isaacsim::ros2::omnigraph_utils::inputOutput`
inlinestd ::stringisaacsim ::ros2 ::omnigraph_utils ::inputOutput(
boolisOutput,
)
Returns the OmniGraph attribute prefix based on direction.
Returns “outputs” for output attributes or “inputs” for input attributes. Used to construct attribute names in OmniGraph compatible format.
Parameters:
isOutput – [in] True for output attributes, false for input attributes

Returns:
std::string Either “outputs” or “inputs” based on direction
