<!-- source: py/api/function__ros2_ogn_utils_8h_1a0c0c0453e39aa111b4b27a6d7e7f6a0a.html | title: getAttributeWritableArrayData — Isaac Sim -->

# getAttributeWritableArrayData
Fully qualified name: `isaacsim::ros2::omnigraph_utils::getAttributeWritableArrayData`
template<typenameT>
inlineT *isaacsim ::ros2 ::omnigraph_utils ::getAttributeWritableArrayData(
constNodeObj&nodeObj,
conststd ::string&attrName,
size_tnewCount,
)
Gets writable data for an array attribute with resizing.
Retrieves a writable pointer to an array attribute’s data, resizing the array to the specified size. Used for modifying array attribute values in an OmniGraph node.
Template Parameters:
T – Data type of the array elements

Parameters:

- nodeObj – [in] OmniGraph node object containing the attribute

- attrName – [in] Name of the attribute to retrieve

- newCount – [in] New size to set for the array

Returns:
T* Writable pointer to the array data, or nullptr if not found
