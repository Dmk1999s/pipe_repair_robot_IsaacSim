<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_prim_manager_base.html | title: PrimManagerBase — Isaac Sim -->

# PrimManagerBase
Fully qualified name: `isaacsim::core::includes::PrimManagerBase`
template<classComponentType>
classPrimManagerBase:publicisaacsim ::core ::includes ::ComponentManager ,publicpxr ::TfWeakBase

Base template class for bridge applications managing USD-based components.
Provides core functionality for managing components within a USD stage, including component lifecycle management, event handling, and synchronization with USD changes. This class serves as a bridge between the USD stage and component-based application logic.
Note
This class inherits from ComponentManager and pxr::TfWeakBase
Warning
Derived classes must implement pure virtual functions
Template Parameters:
ComponentType – The base component type managed by this application

Public Functions
PrimManagerBase()=default

Constructs a new PrimManagerBase instance.

inline~PrimManagerBase()

Destroys the application instance and cleans up resources.
Releases the notice listener and deletes all managed components

inlinevirtualvoidinitialize(pxr ::UsdStageWeakPtrstage)

Initializes the application with a USD stage.
Sets up the stage reference and creates the notice listener
Parameters:
stage – [in] Weak pointer to the USD stage to be managed

Post:
Application is initialized with the stage and notice listener

virtualvoidtick(doubledt)=0

Updates the application and all components.
Pure virtual function that must be implemented by derived classes
Parameters:
dt – [in] Time step in seconds since the last tick

inlinevirtualvoidinitComponents()

Initializes components from the current stage.
Scans the USD stage for prims matching component types and creates corresponding components. Uses the USD runtime API for efficient traversal.

virtualstd ::vector<std ::string>getComponentIsAVector()const=0

Gets the list of component type names to search for in the stage.
Returns:
Vector of strings containing component type names

virtualvoidonComponentAdd(constpxr ::UsdPrim&prim)=0

Creates a new component for the given prim.
Pure virtual function that must be implemented by derived classes
Parameters:
prim – [in] The USD prim to create a component for

inlinevirtualvoidonComponentChange(constpxr ::UsdPrim&prim)

Updates a component when its corresponding prim changes.
Triggers the component’s change handler if it exists
Parameters:
prim – [in] The USD prim that changed

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

inlinevirtualvoidonStart()

Handles application start event.
Optional callback that runs when the application starts Override this to implement custom start behavior

inlinevirtualvoidonStop()

Handles application stop event.
Optional callback that runs when the application stops Override this to implement custom stop behavior

inlinepxr ::UsdStageWeakPtrgetStage()

Retrieves the managed USD stage.
Returns:
Weak pointer to the current USD stage

Protected Attributes
std ::unordered_map<std ::string,std ::unique_ptr<ComponentType >>m_components

Map of component paths to their corresponding component instances.

std ::unique_ptr<PrimManagerUsdNoticeListener >m_noticeListener

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
