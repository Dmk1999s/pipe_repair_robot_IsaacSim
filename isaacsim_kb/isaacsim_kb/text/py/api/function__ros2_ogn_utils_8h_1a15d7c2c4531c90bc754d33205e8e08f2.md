<!-- source: py/api/function__ros2_ogn_utils_8h_1a15d7c2c4531c90bc754d33205e8e08f2.html | title: getAttributeReadableData — Isaac Sim -->

# getAttributeReadableData
Fully qualified name: `isaacsim::ros2::omnigraph_utils::getAttributeReadableData`
template<typenameT>
inlineT const*isaacsim ::ros2 ::omnigraph_utils ::getAttributeReadableData(
constNodeObj&nodeObj,
conststd ::string&attrName,
)
Gets read-only data for a simple attribute.
Retrieves a read-only pointer to an attribute’s data. Used for reading attribute values from an OmniGraph node.
Template Parameters:
T – Data type of the attribute

Parameters:

- nodeObj – [in] OmniGraph node object containing the attribute

- attrName – [in] Name of the attribute to retrieve

Returns:
T const* Read-only pointer to the attribute data, or nullptr if not found
