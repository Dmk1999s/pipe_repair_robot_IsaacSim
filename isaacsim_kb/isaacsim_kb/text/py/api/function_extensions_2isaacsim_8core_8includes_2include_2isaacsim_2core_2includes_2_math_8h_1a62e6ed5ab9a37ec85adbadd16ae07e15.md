<!-- source: py/api/function_extensions_2isaacsim_8core_8includes_2include_2isaacsim_2core_2includes_2_math_8h_1a62e6ed5ab9a37ec85adbadd16ae07e15.html | title: lookAt — Isaac Sim -->

# lookAt
Fully qualified name: `isaacsim::core::includes::math::lookAt`
inlinepxr ::GfQuatfisaacsim ::core ::includes ::math ::lookAt(
constpxr ::GfVec3f&camera,
constpxr ::GfVec3f&target,
constpxr ::GfVec3f&up,
)
Computes a look-at quaternion rotation.
Creates a rotation that orients an object to look at a target point. The up vector defines the world-space up direction for orientation.
Note
The up vector should not be parallel to the look direction
Parameters:

- camera – [in] Position of the camera/object

- target – [in] Point to look at

- up – [in] World-space up vector (typically {0,1,0})

Returns:
pxr::GfQuatf The resulting look-at rotation
