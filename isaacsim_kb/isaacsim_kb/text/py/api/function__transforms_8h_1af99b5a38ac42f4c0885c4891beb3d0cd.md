<!-- source: py/api/function__transforms_8h_1af99b5a38ac42f4c0885c4891beb3d0cd.html | title: setTransform — Isaac Sim -->

# setTransform
Fully qualified name: `isaacsim::core::includes::transforms::setTransform`
inlinevoidisaacsim ::core ::includes ::transforms ::setTransform(
pxr ::UsdPrim&prim,
pxr ::GfVec3fbodyTranslation,
pxr ::GfQuatfbodyRotation,
)
Sets the transform (position and rotation) of a USD prim.
Handles different types of objects appropriately:

- For articulated objects:

- Wakes up the articulation

- Sets root body pose

- Resets velocities

- For rigid bodies:

- Wakes up the body

- Sets pose directly

- Resets velocities

- For regular prims:

- Computes and sets local transform

- Handles parent space correctly

Note
For physics objects, this function only works during simulation
Warning
Resets linear and angular velocities to zero for physics objects
Parameters:

- prim – [inout] USD prim to transform

- bodyTranslation – [in] New position in world space

- bodyRotation – [in] New rotation in world space
