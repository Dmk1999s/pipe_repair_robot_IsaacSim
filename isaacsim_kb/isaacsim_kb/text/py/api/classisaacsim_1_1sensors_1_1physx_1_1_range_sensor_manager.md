<!-- source: py/api/classisaacsim_1_1sensors_1_1physx_1_1_range_sensor_manager.html | title: RangeSensorManager — Isaac Sim -->

# RangeSensorManager
Fully qualified name: `isaacsim::sensors::physx::RangeSensorManager`
classRangeSensorManager:publicisaacsim ::core ::includes ::PrimManagerBase <RangeSensorComponent >

Manager class for handling multiple range sensor components in the simulation.
This class manages the lifecycle and updates of various range sensor types including Lidar sensors, generic range sensors, and light beam sensors. It handles sensor initialization, updates, and cleanup while providing thread-safe access to sensor data. The manager supports parallel processing of multiple sensors and ensures proper synchronization with the physics simulation timeline.
Public Functions
inlineRangeSensorManager(
omni ::physx ::IPhysx*physxPtr,
carb::tasking::ITasking*taskingPtr,
)
Constructs a new Sensor Manager object.
Parameters:

- physxPtr – [in] Pointer to the PhysX interface for physics simulation

- taskingPtr – [in] Pointer to the tasking interface for parallel processing

~RangeSensorManager()=default

Virtual destructor for proper cleanup.

inlinevoidonPhysicsStep(constdouble&dt)

Updates all sensor components after each physics simulation step.
Processes each enabled sensor component, updating their timestamps and triggering their physics step handlers. Also manages the initialization of components that haven’t started yet.
Parameters:
dt – [in] The time step duration in seconds

inlinevirtualvoidtick(doubledt)

Updates all sensor components during the simulation tick.
Processes each enabled sensor component in parallel if multiple sensors exist. Handles component initialization, pre-tick operations, main tick updates, and visualization drawing.
Parameters:
dt – [in] The time step duration in seconds

inlinevirtualvoidonStop()

Handles cleanup when the simulation scene is stopped.
Resets all components to ensure proper reinitialization on next start

inlinevirtualvoidonComponentAdd(constpxr ::UsdPrim&prim)

Creates a new sensor component based on the USD prim type.
Instantiates the appropriate sensor type (Lidar, Generic, or LightBeam) based on the prim type and initializes it with the provided parameters
Parameters:
prim – [in] The USD prim representing the sensor to create

inlinevirtualstd ::vector<std ::string>getComponentIsAVector(
)const
Gets the list of supported sensor component types.
Returns:
Vector of strings containing the supported sensor type names

inlinevirtualvoidonComponentChange(constpxr ::UsdPrim&prim)

Handles property changes for a sensor component.
Updates the corresponding sensor component with the new property values
Parameters:
prim – [in] The USD prim whose properties have changed

inlineLidarSensor *getLidarSensor(constpxr ::UsdPrim&prim)

Retrieves a Lidar sensor component associated with the given USD prim.
Parameters:
prim – [in] The USD prim associated with the desired Lidar sensor

Returns:
Pointer to the LidarSensor component if found, nullptr otherwise

inlineGenericSensor *getGenericSensor(constpxr ::UsdPrim&prim)

Retrieves a generic range sensor component associated with the given USD prim.
Parameters:
prim – [in] The USD prim associated with the desired generic sensor

Returns:
Pointer to the GenericSensor component if found, nullptr otherwise

inlineLightBeamSensor *getLightBeamSensor(constpxr ::UsdPrim&prim)

Retrieves a light beam sensor component associated with the given USD prim.
Parameters:
prim – [in] The USD prim associated with the desired light beam sensor

Returns:
Pointer to the LightBeamSensor component if found, nullptr otherwise

inlinevirtualvoidinitialize(pxr ::UsdStageWeakPtrstage)

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

inlinevirtualvoidonStart()

Handles application start event.
Optional callback that runs when the application starts Override this to implement custom start behavior

inlinepxr ::UsdStageWeakPtrgetStage()

Retrieves the managed USD stage.
Returns:
Weak pointer to the current USD stage

Protected Attributes
std ::unordered_map<std ::string,std ::unique_ptr<RangeSensorComponent >>m_components

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
