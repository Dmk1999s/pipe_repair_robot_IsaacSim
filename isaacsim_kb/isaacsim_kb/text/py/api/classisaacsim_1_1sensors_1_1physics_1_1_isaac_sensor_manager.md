<!-- source: py/api/classisaacsim_1_1sensors_1_1physics_1_1_isaac_sensor_manager.html | title: IsaacSensorManager — Isaac Sim -->

# IsaacSensorManager
Fully qualified name: `isaacsim::sensors::physics::IsaacSensorManager`
classIsaacSensorManager:publicisaacsim ::core ::includes ::PrimManagerBase <IsaacBaseSensorComponent >

Manager class for handling Isaac physics-based sensors.
This class manages various physics-based sensors in the Isaac environment, including contact sensors and IMU sensors. It handles sensor lifecycle, updates, and provides access to individual sensor components.
The manager inherits from PrimManagerBase and provides functionality for adding, updating, and managing sensor components in the physics simulation.
Public Functions
inlineIsaacSensorManager(omni ::physx ::IPhysx*physXInterface)

Constructs a new IsaacSensorManager instance.
Initializes the manager with a PhysX interface and creates a contact manager instance.
Parameters:
physXInterface – [in] Pointer to the PhysX interface used for physics simulation.

inline~IsaacSensorManager()

Destructor for IsaacSensorManager .
Cleans up all components and releases the contact manager.

inlinevirtualvoidonStop()

Handles the stop event for all managed sensors.
Resets all components to their initial state, stops all sensors, resets the contact manager, and resets internal timers.

inlinevirtualvoidonComponentAdd(constpxr ::UsdPrim&prim)

Handles the addition of a new sensor component.
Creates and initializes appropriate sensor components based on the USD prim type. Supports creation of contact sensors and IMU sensors.
Parameters:
prim – [in] The USD primitive representing the sensor to be added.

inlinevirtualstd ::vector<std ::string>getComponentIsAVector(
)const
Returns a vector of supported sensor component types.
Provides a list of USD prim types that this manager can handle.
Returns:
Vector of strings representing supported sensor types.

inlinevirtualvoidonComponentChange(constpxr ::UsdPrim&prim)

Handles changes to a sensor component’s properties.
Updates the component’s state when its properties change in the USD stage.
Parameters:
prim – [in] The USD primitive whose properties have changed.

inlineIsaacBaseSensorComponent *getComponent(std ::stringpath)

Retrieves a sensor component by its path.
Looks up a sensor component using its USD path string.
Parameters:
path – [in] String representation of the sensor’s USD path.

Returns:
Pointer to the sensor component if found, nullptr otherwise.

inlinevoidonPhysicsStep(constdouble&dt)

Updates all sensor components during the physics simulation step.
Processes physics updates for all sensor components, including contact and IMU sensors. Handles component initialization, timestep updates, and sensor-specific physics calculations.
Parameters:
dt – [in] Time step delta in seconds.

inlinevirtualvoidtick(doubledt)

Performs a tick update for all sensor components.
Updates all enabled sensor components during the simulation tick. Handles component initialization and tick-based updates.
Parameters:
dt – [in] Time step delta in seconds.

inlineContactSensor *getContactSensor(constpxr ::UsdPrim&prim)

Retrieves a contact sensor component for a given USD primitive.
Attempts to find and cast a component to a ContactSensor type.
Parameters:
prim – [in] USD primitive associated with the contact sensor.

Returns:
Pointer to the ContactSensor if found, nullptr otherwise.

inlineContactManager *getContactManager()

Gets the contact manager instance.
Provides access to the manager’s contact handling system.
Returns:
Pointer to the ContactManager instance.

inlineImuSensor *getImuSensor(constpxr ::UsdPrim&prim)

Retrieves an IMU sensor component for a given USD primitive.
Attempts to find and cast a component to an ImuSensor type.
Parameters:
prim – [in] USD primitive associated with the IMU sensor.

Returns:
Pointer to the ImuSensor if found, nullptr otherwise.

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
std ::unordered_map<std ::string,std ::unique_ptr<IsaacBaseSensorComponent >>m_components

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
