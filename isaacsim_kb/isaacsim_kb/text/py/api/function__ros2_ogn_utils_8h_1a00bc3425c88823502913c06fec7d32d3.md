<!-- source: py/api/function__ros2_ogn_utils_8h_1a00bc3425c88823502913c06fec7d32d3.html | title: checkCondition — Isaac Sim -->

# checkCondition
Fully qualified name: `isaacsim::ros2::omnigraph_utils::checkCondition`
inlineboolisaacsim ::ros2 ::omnigraph_utils ::checkCondition(
constvoid*ptr,
std ::stringmessage,
)
Verifies that a pointer is not null and logs an error message if it is.
Utility function to check for null pointers and log an error message. Useful for validating data pointers during attribute access operations.
Parameters:

- ptr – [in] Pointer to check for nullness

- message – [in] Error message to log if pointer is null

Returns:
bool True if the pointer is valid (non-null), false otherwise
