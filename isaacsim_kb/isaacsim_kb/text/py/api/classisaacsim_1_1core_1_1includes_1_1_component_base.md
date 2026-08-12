<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_component_base.html | title: ComponentBase — Isaac Sim -->

# ComponentBase
Fully qualified name: `isaacsim::core::includes::ComponentBase`
template<classPrimType>
classComponentBase

Base class template for USD prim-attached components in an Application.
ComponentBase provides the foundational structure for components that are attached to USD prims within an Application. It manages the lifecycle, timing, and state of components while providing virtual interfaces for key operations like initialization, updates, and event handling.
Note
All derived components must implement the pure virtual functions
Warning
Components must be properly initialized with a valid USD prim and stage before use
Template Parameters:
PrimType – The USD prim type that this component will be attached to

Subclassed by isaacsim::sensors::physics::IsaacSensorComponentBase< PrimType > , isaacsim::sensors::physx::RangeSensorComponentBase< PrimType >
Public Functions
virtual~ComponentBase()=default

Virtual destructor ensuring proper cleanup of derived classes.

inlinevirtualvoidinitialize(
constPrimType &prim,
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

virtualvoidonStart()=0

Pure virtual function called after simulation start.
Implement this to define component behavior at simulation start

inlinevirtualvoidonStop()

Called when simulation is stopped.
Override this to implement cleanup or state reset behavior

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

inlinevirtualvoidonRenderEvent()

Called for each rendered frame.
Override this to implement render-specific behavior or visual updates

virtualvoidtick()=0

Pure virtual function called every frame.
Implement this to define the component’s per-frame behavior

virtualvoidonComponentChange()=0

Pure virtual function called when the component’s prim changes.
Implement this to handle USD prim attribute or relationship changes

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

inlinePrimType &getPrim()

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
boolmDoStart=true

Flag indicating whether onStart should be called.

Protected Attributes
PrimType m_prim

USD prim reference storing component settings.

pxr ::UsdStageWeakPtrm_stage=nullptr

Weak pointer to the USD stage containing the prim.

usdrt::UsdStageRefPtrm_usdrtStage=nullptr

Runtime USD stage reference.

doublem_timeSeconds=0

Current simulation time in seconds.

int64_tm_timeNanoSeconds=0

Current simulation time in nanoseconds.

doublem_timeDelta=0

Time delta for current tick in seconds.

uint64_tm_sequenceNumber=0

Component sequence number for ordering/identification.

boolm_enabled=true

Component enabled state flag.
