<!-- source: py/api/namespace_isaacsim__robot__surface__gripper.html | title: surface_gripper — Isaac Sim -->

# surface_gripper
Fully qualified name: `isaacsim::robot::surface_gripper`
namespacesurface_gripper

## Classes
SurfaceGripperComponent
Component class for managing Surface Gripper functionality.

SurfaceGripperManager
Manager class for handling surface grippers in a scene.

## Enumerations
Axis
Axis enumeration for forward direction.

GripperStatus
PhysxActionType
Action kind for queued PhysX operations.

UsdActionType
USD action kind for queued USD operations.

## Functions
GripperStatusGripperStatusFromToken (const pxr::TfToken &token)
std::stringGripperStatusToString (GripperStatus status)
pxr::TfTokenGripperStatusToToken (GripperStatus status)

## Structs
PhysxAction
Queued PhysX action to be executed serially by the manager.

SurfaceGripperInterface
Interface for controlling surface gripper functionality.

UsdAction
Queued USD action to be executed serially by the manager.
