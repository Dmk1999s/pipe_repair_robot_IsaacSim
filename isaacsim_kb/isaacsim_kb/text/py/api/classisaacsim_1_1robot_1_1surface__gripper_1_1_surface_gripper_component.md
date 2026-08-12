<!-- source: py/api/classisaacsim_1_1robot_1_1surface__gripper_1_1_surface_gripper_component.html | title: SurfaceGripperComponent — Isaac Sim -->

# SurfaceGripperComponent
Fully qualified name: `isaacsim::robot::surface_gripper::SurfaceGripperComponent`
classSurfaceGripperComponent:publicisaacsim ::core ::includes ::ComponentBase <pxr ::UsdPrim>

Component class for managing Surface Gripper functionality.
This class represents a surface gripper component that can be attached to a robot to enable gripping functionality. It manages the D6 joints that act as attachment points for the gripper.
Public Functions
SurfaceGripperComponent()=default

Default constructor.

virtual~SurfaceGripperComponent()=default

Virtual destructor.

virtualvoidinitialize(
constpxr ::UsdPrim&prim,
constpxr ::UsdStageWeakPtrstage,
boolwriteToUsd,
)
Initializes the surface gripper component.
Parameters:

- prim – [in] USD prim representing the surface gripper

- stage – [in] USD stage containing the prim

virtualvoidonComponentChange()

Called when component properties change.
Updates the gripper’s configuration when component properties are modified

virtualvoidonStart()

Called when the gripper starts.

virtualvoidonPhysicsStep(doubledt)

Called each physics step to update gripper state.

virtualvoidpreTick()

Called before each tick to prepare sensor state.

virtualvoidtick()

Called each tick to update the gripper state.

virtualvoidonStop()

Called when the gripper stops.

virtualboolsetGripperStatus(GripperStatus status)

Sets the gripper status.
Parameters:
status – [in] New status for the gripper.

Returns:
True if the status was changed successfully.

voidconsumePhysxActions(std ::vector<PhysxAction >&outActions)

Drains this component’s queued PhysX actions into the provided vector.
Parameters:
outActions – [out] Destination vector where actions will be appended.

voidconsumeUsdActions(std ::vector<UsdAction >&outActions)

Drains this component’s queued USD actions into the provided vector.
Parameters:
outActions – [out] Destination vector where actions will be appended.

inlineGripperStatus getGripperStatus()const

Gets the current status of the gripper.
Returns:
Current status.

inlinestd ::stringgetPrimPath()const

Gets the prim path of this gripper.
Returns:
The USD prim path as a string

inlinestd ::vector<std ::string>getGrippedObjects()const

Gets the list of currently gripped objects.
Returns:
Vector of prim paths for gripped objects

inlinevoidsetWriteToUsd(boolwriteToUsd)

Sets whether to write to USD or keep state in memory only.
Parameters:
writeToUsd – [in] Whether to write to USD or keep state in memory only

inlineboolhasPhysxActions()const

inlineboolhasUsdActions()const

inlinevirtualvoidinitialize(
constpxr ::UsdPrim&prim,
pxr ::UsdStageWeakPtrstage,
)
Initializes the component with USD prim and stage references.
Sets up the component’s USD context and prepares it for execution
Parameters:

- prim – [in] The USD prim to attach this component to

- stage – [in] The USD stage containing the prim

Post:
Component is initialized with valid USD prim and stage references

Post:
mDoStart is set to true, indicating the component is ready to start

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

inlinevirtualvoidonRenderEvent()

Called for each rendered frame.
Override this to implement render-specific behavior or visual updates

inlinevirtualvoidupdateTimestamp(
doubletimeSeconds,
doubledt,
int64_ttimeNano,
)
Updates the component’s internal timing information.
Maintains synchronized timing state across the component
Parameters:

- timeSeconds – [in] Current simulation time in seconds

- dt – [in] Time step size in seconds

- timeNano – [in] Current simulation time in nanoseconds

inlinepxr ::UsdPrim&getPrim()

Retrieves the component’s USD prim.
Returns:
Reference to the component’s USD prim

inlineboolgetEnabled()

Checks if the component is enabled.
Returns:
true if the component is enabled, false otherwise

inlineuint64_tgetSequenceNumber()

Gets the component’s sequence number.
Returns:
The component’s sequence number

Public Members
boolmDoStart

Flag indicating whether onStart should be called.

Protected Attributes
pxr ::UsdPrimm_prim

USD prim reference storing component settings.

pxr ::UsdStageWeakPtrm_stage

Weak pointer to the USD stage containing the prim.

usdrt::UsdStageRefPtrm_usdrtStage

Runtime USD stage reference.

doublem_timeSeconds

Current simulation time in seconds.

int64_tm_timeNanoSeconds

Current simulation time in nanoseconds.

doublem_timeDelta

Time delta for current tick in seconds.

uint64_tm_sequenceNumber

Component sequence number for ordering/identification.

boolm_enabled

Component enabled state flag.
