<!-- source: py/api/function__usd_utilities_8h_1a2bd99a985e0ec96d087159dd7caa977b.html | title: findInnerTransform — Isaac Sim -->

# findInnerTransform
Fully qualified name: `isaacsim::core::includes::findInnerTransform`
inlinepxr ::GfMatrix4disaacsim ::core ::includes ::findInnerTransform(
pxr ::UsdPrimprim,
constpxr ::GfMatrix4d&mtx,
bool&foundTransformOp,
pxr ::UsdTimeCodetimecode=pxr ::UsdTimeCode::Default(),
boolskipEqualSetForTimeSample=false,
)
Given a target local transform matrix for a prim, determine what value to set just the transformOp when other xformOps are present.
Parameters:

- prim – The prim in question

- mtx – The desired final transform matrix for the prim including all ops

- foundTransformOp – returns true if there is a transform xformOp
