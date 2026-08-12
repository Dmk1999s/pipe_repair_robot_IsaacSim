<!-- source: py/api/function__transforms_8h_1a9b6e3e24896f2b910cddc545033a522f.html | title: setScale — Isaac Sim -->

# setScale
Fully qualified name: `isaacsim::core::includes::transforms::setScale`
inlinevoidisaacsim ::core ::includes ::transforms ::setScale(
pxr ::UsdPrim&prim,
pxr ::GfVec3fpxBodyScale,
)
Sets the scale of a USD prim.
Applies scaling to the prim’s local transform, with special handling for physics objects:

- Only scales non-physics objects during simulation

- Preserves existing transform components

- Applies scale in local space

Note
During simulation, only non-physics objects can be scaled
Warning
Scaling physics objects during simulation may have unexpected results
Parameters:

- prim – [inout] USD prim to scale

- pxBodyScale – [in] Scale factors for x, y, and z axes
