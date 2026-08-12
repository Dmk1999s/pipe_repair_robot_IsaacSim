<!-- source: py/api/function__ros2_ogn_utils_8h_1a4126c1d760d422108fe5793e5ec209dc.html | title: getAttributeReadableArrayData — Isaac Sim -->

# getAttributeReadableArrayData
Fully qualified name: `isaacsim::ros2::omnigraph_utils::getAttributeReadableArrayData`
template<typenameT>
inlineT const*isaacsim ::ros2 ::omnigraph_utils ::getAttributeReadableArrayData(
constNodeObj&nodeObj,
conststd ::string&attrName,
size_t&newCount,
)
Gets read-only data for an array attribute.
Retrieves a read-only pointer to an array attribute’s data and returns its current size. Used for reading array attribute values from an OmniGraph node.
Template Parameters:
T – Data type of the array elements

Parameters:

- nodeObj – [in] OmniGraph node object containing the attribute

- attrName – [in] Name of the attribute to retrieve

- newCount – [out] Variable to receive the array size

Returns:
T const* Read-only pointer to the array data, or nullptr if not found
