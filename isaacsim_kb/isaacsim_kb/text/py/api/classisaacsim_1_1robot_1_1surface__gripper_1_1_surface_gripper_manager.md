<!-- source: py/api/classisaacsim_1_1robot_1_1surface__gripper_1_1_surface_gripper_manager.html | title: SurfaceGripperManager — Isaac Sim -->

# SurfaceGripperManager
Fully qualified name: `isaacsim::robot::surface_gripper::SurfaceGripperManager`
classSurfaceGripperManager:publicisaacsim ::core ::includes ::PrimManagerBase <SurfaceGripperComponent >

Manager class for handling surface grippers in a scene.
This class manages all surface gripper components in a USD scene, providing functionality to control and monitor gripper states. It processes physics steps to update gripper behaviors.
Public Functions
inlineSurfaceGripperManager(omni ::physx ::IPhysx*physXInterface)

Constructs a new SurfaceGripperManager .
Parameters:
physXInterface – [in] Pointer to the PhysX interface used for physics simulation

inline~SurfaceGripperManager()

Destructor for SurfaceGripperManager .

virtualstd ::vector<std ::string>getComponentIsAVector()const

Returns a vector of supported component types.
Returns:
Vector of strings representing supported component types

virtualvoidonStop()

Handles the stop event for all managed grippers.

virtualvoidonComponentAdd(constpxr ::UsdPrim&prim)

Handles the addition of a new surface gripper component.
Parameters:
prim – [in] The USD primitive representing the gripper to be added

virtualvoidonComponentChange(constpxr ::UsdPrim&prim)

Handles changes to a gripper component’s properties.
Parameters:
prim – [in] The USD primitive whose properties have changed

voidonPhysicsStep(constdouble&dt)

Called for each physics step to update all grippers.
Parameters:
dt – [in] The time step in seconds

virtualvoidonStart()

Called when the simulation starts.

virtualvoidtick(doubledt)

Tick function called each frame.
Parameters:
dt – [in] The time step in seconds

voidsetWriteToUsd(boolwriteToUsd)

Sets whether to write to USD or keep state in memory only.
Parameters:
writeToUsd – [in] Whether to write to USD or keep state in memory only

boolsetGripperStatus(
conststd ::string&primPath,
GripperStatus status,
)
Sets the status of a specific gripper.
Parameters:

- primPath – [in] The USD path of the gripper to control.

- status – [in] The new status code to set (0: Open, 1: Closed, 2: Closing).

Returns:
True if the status was set successfully, false otherwise.

GripperStatus getGripperStatus(conststd ::string&primPath)

Gets the status code of a specific gripper.
Parameters:
primPath – [in] The USD path of the gripper.

Returns:
The current status code of the gripper, or -1 if not found.

std ::vector<std ::string>getAllGrippers()const

Gets all grippers currently managed by this manager.
Returns:
A vector of prim paths representing all grippers

SurfaceGripperComponent *getGripper(conststd ::string&primPath)

Gets a specific gripper component by its path.
Parameters:
primPath – [in] The USD path of the gripper

Returns:
Pointer to the gripper component if found, nullptr otherwise

SurfaceGripperComponent *getGripper(constpxr ::UsdPrim&prim)

Gets a specific gripper component by its USD prim.
Parameters:
prim – [in] The USD prim of the gripper

Returns:
Pointer to the gripper component if found, nullptr otherwise

virtualvoidinitialize(constpxr ::UsdStageWeakPtrstage)

Initializes the application with a USD stage.
Sets up the stage reference and creates the notice listener
Parameters:
stage – [in] Weak pointer to the USD stage to be managed

Post:
Application is initialized with the stage and notice listener

inlinevirtualvoidinitComponents()

Initializes components from the current stage.
Scans the USD stage for prims matching component types and creates corresponding components. Uses the USD runtime API for efficient traversal.

inlinevirtualvoidonPhysicsStep(floatdt)

Updates components during physics simulation steps.
Override this to implement physics-specific component updates
Parameters:
dt – [in] Physics time step in seconds

inlinevirtualvoidonComponentRemove(constpxr ::SdfPath&primPath)

Removes components associated with a prim and its descendants.
Safely removes components when their corresponding prims are deleted from the stage. Uses a mutex to ensure thread-safe component removal.
Thread Safety
This method is thread-safe

Parameters:
primPath – [in] Path to the prim being removed

inlinevirtualvoiddeleteAllComponents()

Removes all components and performs cleanup.
Thread-safe method to remove all components and release their resources
Thread Safety
This method is thread-safe

inlinepxr ::UsdStageWeakPtrgetStage()

Retrieves the managed USD stage.
Returns:
Weak pointer to the current USD stage

Protected Attributes
std ::unordered_map<std ::string,std ::unique_ptr<SurfaceGripperComponent >>m_components

Map of component paths to their corresponding component instances.

std ::unique_ptr<PrimManagerUsdNoticeListener>m_noticeListener

USD notice listener for stage changes.

std ::mutexm_componentMtx

Mutex for thread-safe component operations.

pxr ::UsdStageWeakPtrm_stage=nullptr

Weak pointer to the managed USD stage.

doublem_timeSeconds=0

Current simulation time in seconds.

int64_tm_timeNanoSeconds=0

Current simulation time in nanoseconds.

doublem_timeDelta=0

Time delta for current tick in seconds.
