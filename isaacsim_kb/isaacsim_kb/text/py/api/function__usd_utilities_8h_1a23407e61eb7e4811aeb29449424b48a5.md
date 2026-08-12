<!-- source: py/api/function__usd_utilities_8h_1a23407e61eb7e4811aeb29449424b48a5.html | title: setLocalTransformMatrix — Isaac Sim -->

# setLocalTransformMatrix
Fully qualified name: `isaacsim::core::includes::setLocalTransformMatrix`
inlineboolisaacsim ::core ::includes ::setLocalTransformMatrix(
pxr ::UsdPrimprim,
constpxr ::GfMatrix4d&mtxIn,
pxr ::UsdTimeCodetimecode=pxr ::UsdTimeCode::Default(),
boolskipEqualSetForTimeSample=false,
std ::unique_ptr<PXR_NS::SdfChangeBlock>*parentChangeBlock=nullptr,
)
Sets local transform matrix of a prim.
Parameters:

- prim – [inout] The prim to set local transform matrix to.

- mtxIn – [in] The local transform matrix.

- timecode – [in] Time code for the transform operation.

- skipEqualSetForTimeSample – [in] Whether to skip setting if value is equal.

- parentChangeBlock – [inout] Optional parent change block for batching operations.

Returns:
true if the operation was successful, false otherwise.
