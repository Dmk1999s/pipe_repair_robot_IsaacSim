<!-- source: py/api/function__pose_8h_1ae0efb4e214474d8f0b6c9992a49e8773.html | title: computeWorldXformNoCache — Isaac Sim -->

# computeWorldXformNoCache
Fully qualified name: `isaacsim::core::includes::pose::computeWorldXformNoCache`
staticusdrt::GfMatrix4disaacsim ::core ::includes ::pose ::computeWorldXformNoCache(
pxr ::UsdStageRefPtrusdStage,
usdrt::UsdStageRefPtrusdrtStage,
constpxr ::SdfPath&path,
pxr ::UsdTimeCodetimecode=pxr ::UsdTimeCode::Default(),
booluseFabricHierarchy=true,
boollogWarningOnFallback=false,
)
Computes the world transform of a prim.
Calculates the complete world transform by:

- Checking for world transform attributes (position, orientation, scale)

- Falling back to local transform computation if world transform unavailable

- Recursively computing parent transforms when needed

The function handles three cases:

- Prims with world transform attributes

- Prims with local transform only

- Regular USD prims without USDRT extensions

Warning
May be computationally expensive for deep hierarchies
Parameters:

- usdStage – [in] Reference to the USD stage

- usdrtStage – [in] Reference to the USDRT stage

- path – [in] Path to the prim whose transform to compute

- timecode – [in] Time code for the transform evaluation (default: Default())

- useFabricHierarchy – [in] Whether to use IFabricHierarchy (default: true). If enabled, but Fabric Scene Delegate (/app/useFabricSceneDelegate) is disabled or the retrieved data is invalid, the call will fall back to non-IFabricHierarchy implementation.

- logWarningOnFallback – [in] Whether to log a warning when falling back to non-IFabricHierarchy (default: false).

Returns:
usdrt::GfMatrix4d The computed world transform matrix
