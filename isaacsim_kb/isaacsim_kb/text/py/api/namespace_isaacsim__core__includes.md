<!-- source: py/api/namespace_isaacsim__core__includes.html | title: includes — Isaac Sim -->

# includes
Fully qualified name: `isaacsim::core::includes`
namespaceincludes

## Classes
BaseResetNode
Base class for nodes that automatically reset their state when simulation is stopped.

Buffer
Abstract base class for memory buffer management.

ComponentBase
Base class template for USD prim-attached components in an Application.

ComponentManager
Base class for managing USD-based components in an application.

DeviceBufferBase
CUDA device (GPU) memory buffer implementation.

GenericBufferBase
Device-generic (CPU or CUDA device) memory buffer implementation.

HostBufferBase
Host (CPU) memory buffer implementation.

LibraryLoader
Single dynamic library loader.

MultiLibraryLoader
Manager for multiple dynamic libraries.

PrimManagerBase
Base template class for bridge applications managing USD-based components.

PrimManagerUsdNoticeListener
Custom USD notice listener for handling object changes in the stage.

ScopedCudaTextureObject
RAII wrapper for CUDA texture object management.

ScopedDevice
RAII wrapper for CUDA device context management.

ScopedTimer
RAII-style performance timer for code block measurement.

UsdNoticeListener
Helper base class to subscribe to pxr::TfNotice.

## Enumerations
MemoryType
Enumeration specifying the type of memory allocation.

TimeSamplesOnLayer
enum to show effective timesamples in layerstacks based on current authoring layer

## Functions
voidcopyTimeSamplesFromWeakerLayer (pxr::UsdStage &stage, const pxr::UsdAttribute &attr)
Copy TimeSample From Waker Layer.

pxr::GfMatrix4dfindInnerTransform (pxr::UsdPrim prim, const pxr::GfMatrix4d &mtx, bool &foundTransformOp, pxr::UsdTimeCode timecode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false)
Given a target local transform matrix for a prim, determine what value to set just the transformOp when other xformOps are present.

const PXR_NS::TfTokeng_kIsaacNameOveride("isaac:nameOverride")
Token for overriding prim names in Isaac Sim.

TimeSamplesOnLayergetAttributeEffectiveTimeSampleLayerInfo (const pxr::UsdStage &stage, const pxr::UsdAttribute &attr, pxr::SdfLayerRefPtr *outLayer=nullptr)
check if attribute has efficient timesample and these data are on currentlayer/strongerlayer/weakerlayer

pxr::UsdAttributegetCameraAttributeFromRenderProduct (const std::string &attributeString, const std::string &renderProductPathString)
Retrieves a specific attribute from a camera associated with a render product.

pxr::UsdPrimgetCameraPrimFromRenderProduct (const std::string &renderProductPathString)
Retrieves the camera prim associated with a render product.

PXR_NS::SdfLayerRefPtrgetLayerIfDefOnSessionOrItsSublayers (PXR_NS::UsdStageRefPtr stage, const PXR_NS::SdfPath &path)
Finds if the given prim path has a "def" primSpec on session layer or its sublayers.

PXR_NS::SdfLayerRefPtrgetLayerIfSpecOnSessionOrItsSublayers (PXR_NS::UsdStageRefPtr stage, const PXR_NS::SdfPath &path, const std::function< bool(PXR_NS::SdfSpecHandle)> &predicate=nullptr)
Finds if the given path has a spec on session layer or its sublayers.

pxr::GfMatrix4dgetLocalTransformMatrix (const pxr::UsdPrim &prim, pxr::UsdTimeCode time=pxr::UsdTimeCode::Default())
Gets local transform matrix of a prim.

std::stringgetName (const pxr::UsdPrim &prim)
Retrieves the name of a USD prim, with support for custom overrides.

pxr::SdfPathgetSdfPathFromUint64 (uint64_t pathToken)
Converts a uint64_t token to a USD path.

pxr::GfMatrix4dgetWorldTransformMatrix (const pxr::UsdPrim &prim, pxr::UsdTimeCode time=pxr::UsdTimeCode::Default())
Gets world transform matrix of a prim.

boolhasTimeSample (const pxr::UsdAttribute &attribute, pxr::UsdTimeCode timeCode)
Checks if a UsdAttribute instance has time sample on key timeCode.

boolisTimeSampled (const pxr::UsdAttribute &attribute)
Checks if a UsdAttribute instance is time sampled.

voidsafeGetAttribute (const pxr::UsdAttribute &attr, T &inputValue)
Safely retrieves a USD attribute value with error handling.

boolsetAttribute (const pxr::UsdAttribute &attribute, const ValueType &val, pxr::UsdTimeCode timeCode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false, bool autoTargetSessionLayer=true)
Sets attribute value with optional time sampling and session layer targeting.

boolsetLocalTransformMatrix (pxr::UsdPrim prim, const pxr::GfMatrix4d &mtxIn, pxr::UsdTimeCode timecode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false, std::unique_ptr< PXR_NS::SdfChangeBlock > *parentChangeBlock=nullptr)
Sets local transform matrix of a prim.

boolsetValueWithPrecision (pxr::UsdGeomXformOp &xformOp, const ValueType &value, pxr::UsdTimeCode timeCode=pxr::UsdTimeCode::Default(), bool skipEqualSetForTimeSample=false)
Set value with precision based on the UsdGeomXformOp precision type.

## Namespaces
color
conversions
math
pose
posetree
transforms
utils

## Typedefs
Component
Convenience typedef for ComponentBase specialized with pxr::UsdPrim.

DeviceBuffer
Type alias for a device buffer of bytes.

GenericBuffer
Type alias for a generic buffer of bytes.

HostBuffer
Type alias for a host buffer of bytes.

PrimManager
Convenience typedef for PrimManagerBase specialized with the base Component type.
