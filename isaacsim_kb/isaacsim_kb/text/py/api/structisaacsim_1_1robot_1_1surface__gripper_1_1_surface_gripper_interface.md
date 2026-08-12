<!-- source: py/api/structisaacsim_1_1robot_1_1surface__gripper_1_1_surface_gripper_interface.html | title: SurfaceGripperInterface — Isaac Sim -->

# SurfaceGripperInterface
Fully qualified name: `isaacsim::robot::surface_gripper::SurfaceGripperInterface`
structSurfaceGripperInterface

Interface for controlling surface gripper functionality.
Provides function pointers for controlling surface grippers in the simulation. Surface grippers can attach to and manipulate objects through surface contact rather than traditional mechanical gripping.
All functions operate on grippers identified by their USD prim path.
Public Members
int(*getGripperStatus)(constchar*primPath)

Function pointer to get the current status of a surface gripper.

bool(*openGripper)(constchar*primPath)

Function pointer to open/release a surface gripper.

bool(*closeGripper)(constchar*primPath)

Function pointer to close/activate a surface gripper.

bool(*setGripperAction)(constchar*primPath,constfloataction)

Function pointer to set a specific gripper action value.

std ::vector<std ::string>(*getGrippedObjects)(constchar*primPath)

Function pointer to get the list of objects currently gripped.

bool(*setWriteToUsd)(constboolwriteToUsd)

Function pointer to set whether to write to USD.

std ::vector<int>(*getGripperStatusBatch)(constchar*const*primPaths,size_tcount)

Function pointer to get statuses for multiple surface grippers.

std ::vector<bool>(*openGripperBatch)(constchar*const*primPaths,size_tcount)

Function pointer to open multiple surface grippers.

std ::vector<bool>(*closeGripperBatch)(constchar*const*primPaths,size_tcount)

Function pointer to close multiple surface grippers.

std ::vector<bool>(*setGripperActionBatch)(constchar*const*primPaths,constfloat*actions,size_tcount)

Function pointer to set actions for multiple surface grippers.

std ::vector<std ::vector<std ::string>>(*getGrippedObjectsBatch)(constchar*const*primPaths,size_tcount)

Function pointer to get gripped objects for multiple surface grippers.
