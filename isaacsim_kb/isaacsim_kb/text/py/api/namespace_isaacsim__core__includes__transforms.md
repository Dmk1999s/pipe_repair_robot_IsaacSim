<!-- source: py/api/namespace_isaacsim__core__includes__transforms.html | title: transforms — Isaac Sim -->

# transforms
Fully qualified name: `isaacsim::core::includes::transforms`
namespacetransforms

## Functions
voidcreateTensorDesc (TensorDesc &tensorDesc, void *dataPtr, int numElements, TensorDataType type)
voidsetScale (pxr::UsdPrim &prim, pxr::GfVec3f pxBodyScale)
Sets the scale of a USD prim.

voidsetTransform (pxr::UsdPrim &prim, pxr::GfVec3f bodyTranslation, pxr::GfQuatf bodyRotation)
Sets the transform (position and rotation) of a USD prim.
