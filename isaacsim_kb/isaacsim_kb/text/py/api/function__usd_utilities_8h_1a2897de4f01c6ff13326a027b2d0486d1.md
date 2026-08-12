<!-- source: py/api/function__usd_utilities_8h_1a2897de4f01c6ff13326a027b2d0486d1.html | title: getLayerIfDefOnSessionOrItsSublayers — Isaac Sim -->

# getLayerIfDefOnSessionOrItsSublayers
Fully qualified name: `isaacsim::core::includes::getLayerIfDefOnSessionOrItsSublayers`
inlinePXR_NS::SdfLayerRefPtrisaacsim ::core ::includes ::getLayerIfDefOnSessionOrItsSublayers(
PXR_NS::UsdStageRefPtrstage,
constPXR_NS::SdfPath&path,
)
Finds if the given prim path has a “def” primSpec on session layer or its sublayers.
Specialized version of getLayerIfSpecOnSessionOrItsSublayers that specifically looks for prim specifications with “def” specifier type. This excludes “over” prims and focuses only on defining prim specifications.
See also
getLayerIfSpecOnSessionOrItsSublayers for general spec search
Note
If you want to find attributeSpec use getLayerIfSpecOnSessionOrItsSublayers instead
Parameters:

- stage – [in] USD stage containing the layers to search

- path – [in] The prim path to check for “def” primSpec

Returns:
SdfLayerRefPtr Layer that contains the “def” prim spec, or nullptr if not found
