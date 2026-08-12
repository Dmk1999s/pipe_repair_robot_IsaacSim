<!-- source: py/api/function__usd_utilities_8h_1a41d8ad54bdade99a59705cc78c350823.html | title: getLayerIfSpecOnSessionOrItsSublayers — Isaac Sim -->

# getLayerIfSpecOnSessionOrItsSublayers
Fully qualified name: `isaacsim::core::includes::getLayerIfSpecOnSessionOrItsSublayers`
inlinePXR_NS::SdfLayerRefPtrisaacsim ::core ::includes ::getLayerIfSpecOnSessionOrItsSublayers(
PXR_NS::UsdStageRefPtrstage,
constPXR_NS::SdfPath&path,
conststd ::function<bool(PXR_NS::SdfSpecHandle)>&predicate=nullptr,
)
Finds if the given path has a spec on session layer or its sublayers.
Searches through session layer and its sublayers to find if a specification (prim, attribute, property, or other USD object) exists at the given path. Optionally applies a predicate function to validate the found specification.
See also
getLayerIfDefOnSessionOrItsSublayers for prim-specific “def” search
Note
Searches only session layers and their sublayers, stops at root layer
Parameters:

- stage – [in] USD stage containing the layers to search

- path – [in] The USD path to check for specification existence

- predicate – [in] Optional validation function called if spec is found on the layer

Returns:
SdfLayerRefPtr Layer that contains the spec at given path, or nullptr if not found
