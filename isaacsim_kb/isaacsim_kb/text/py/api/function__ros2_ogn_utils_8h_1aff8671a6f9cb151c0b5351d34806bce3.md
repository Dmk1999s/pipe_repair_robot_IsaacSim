<!-- source: py/api/function__ros2_ogn_utils_8h_1aff8671a6f9cb151c0b5351d34806bce3.html | title: getAttributeWritableData — Isaac Sim -->

# getAttributeWritableData
Fully qualified name: `isaacsim::ros2::omnigraph_utils::getAttributeWritableData`
template<typenameT>
inlineT *isaacsim ::ros2 ::omnigraph_utils ::getAttributeWritableData(
constNodeObj&nodeObj,
conststd ::string&attrName,
)
Gets writable data for a simple attribute.
Retrieves a writable pointer to an attribute’s data. Used for modifying attribute values in an OmniGraph node.
Template Parameters:
T – Data type of the attribute

Parameters:

- nodeObj – [in] OmniGraph node object containing the attribute

- attrName – [in] Name of the attribute to retrieve

Returns:
T* Writable pointer to the attribute data, or nullptr if not found
