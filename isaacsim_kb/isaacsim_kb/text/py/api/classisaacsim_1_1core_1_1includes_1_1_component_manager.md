<!-- source: py/api/classisaacsim_1_1core_1_1includes_1_1_component_manager.html | title: ComponentManager — Isaac Sim -->

# ComponentManager
Fully qualified name: `isaacsim::core::includes::ComponentManager`
classComponentManager

Base class for managing USD-based components in an application.
ComponentManager provides the core interface for managing components within a USD stage. It handles component lifecycle (creation, updates, deletion), stage management, and application-level events. This class serves as the foundation for building component-based applications that interact with USD stages.
Note
All pure virtual functions must be implemented by derived classes
Warning
This class is not thread-safe by default; derived classes must implement their own thread safety mechanisms if needed
Subclassed by isaacsim::core::includes::PrimManagerBase< SurfaceGripperComponent > , isaacsim::core::includes::PrimManagerBase< IsaacBaseSensorComponent > , isaacsim::core::includes::PrimManagerBase< RangeSensorComponent > , isaacsim::core::includes::PrimManagerBase< ComponentType >
Public Functions
ComponentManager()=default

Constructs a new ComponentManager instance.

~ComponentManager()=default

Virtual destructor for proper cleanup of derived classes.

inlinevirtualvoidinitialize(pxr ::UsdStageWeakPtrstage)

Initializes the manager with a USD stage.
Sets up the stage reference for component management
Parameters:
stage – [in] Weak pointer to the USD stage to be managed

Post:
The manager is initialized with the provided stage

virtualvoidtick(doubledt)=0

Updates the manager and all managed components.
Pure virtual function that must be implemented by derived classes to define the update behavior of components
Parameters:
dt – [in] Time step in seconds since the last tick

virtualvoidinitComponents()=0

Initializes components from the current stage.
Pure virtual function that must be implemented by derived classes to define how components are discovered and initialized from the stage

inlinevirtualvoidonStart()

Handles application start event.
Optional callback that runs when the application starts Override this to implement custom start behavior

inlinevirtualvoidonStop()

Handles application stop event.
Optional callback that runs when the application stops Override this to implement custom stop behavior

virtualvoidonComponentAdd(constpxr ::UsdPrim&prim)=0

Creates a new component for the given prim.
Pure virtual function that must be implemented by derived classes to define component creation behavior
Parameters:
prim – [in] The USD prim to create a component for

virtualvoidonComponentChange(constpxr ::UsdPrim&prim)=0

Updates a component when its corresponding prim changes.
Pure virtual function that must be implemented by derived classes to define how components react to prim changes
Parameters:
prim – [in] The USD prim that changed

virtualvoidonComponentRemove(constpxr ::SdfPath&primPath)=0

Removes a component and its associated resources.
Pure virtual function that must be implemented by derived classes to define component cleanup behavior
Parameters:
primPath – [in] Path to the prim whose component should be removed

virtualvoiddeleteAllComponents()=0

Removes all components and performs cleanup.
Pure virtual function that must be implemented by derived classes to define complete cleanup behavior

inlinepxr ::UsdStageWeakPtrgetStage()

Retrieves the managed USD stage.
Returns:
Weak pointer to the current USD stage

Protected Attributes
pxr ::UsdStageWeakPtrm_stage=nullptr

Weak pointer to the managed USD stage.

doublem_timeSeconds=0

Current simulation time in seconds.

int64_tm_timeNanoSeconds=0

Current simulation time in nanoseconds.

doublem_timeDelta=0

Time delta for current tick in seconds.
