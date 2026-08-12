<!-- source: py/api/function__pose_8h_1ac5c58ed45f9d9b0be6b0ddb6e124fb95.html | title: getRelativeTransform — Isaac Sim -->

# getRelativeTransform
Fully qualified name: `isaacsim::core::includes::pose::getRelativeTransform`
inlineusdrt::GfMatrix4disaacsim ::core ::includes ::pose ::getRelativeTransform(
pxr ::UsdStageRefPtrusdStage,
usdrt::UsdStageRefPtrusdrtStage,
constpxr ::SdfPath&sourcePrim,
constpxr ::SdfPath&targetPrim,
)
Computes the relative transform matrix between two prims.
Calculates the transform that converts coordinates from the source prim’s frame to the target prim’s frame. The computation follows these steps:

- Compute world transforms for both source and target prims

- Invert the target’s world transform

- Multiply to get the relative transform

Note
The returned matrix is in column-major format
Warning
Ensure both prims exist in the stage before calling
Parameters:

- usdStage – [in] Reference to the USD stage

- usdrtStage – [in] Reference to the USDRT stage

- sourcePrim – [in] Path to the source prim

- targetPrim – [in] Path to the target prim

Returns:
usdrt::GfMatrix4d The relative transform matrix (column-major)
