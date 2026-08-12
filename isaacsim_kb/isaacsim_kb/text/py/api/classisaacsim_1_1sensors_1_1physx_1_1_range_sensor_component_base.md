<!-- source: py/api/classisaacsim_1_1sensors_1_1physx_1_1_range_sensor_component_base.html | title: RangeSensorComponentBase — Isaac Sim -->

# RangeSensorComponentBase
Fully qualified name: `isaacsim::sensors::physx::RangeSensorComponentBase`
template<classPrimType>
classRangeSensorComponentBase:publicisaacsim ::core ::includes ::ComponentBase <PrimType >

Base class which simulates a range sensor.
This template class provides the core functionality for range-based sensors, including initialization, lifecycle management, and data processing. It handles sensor transforms, visualization, and interaction with the physics simulation.
Template Parameters:
PrimType – The USD prim type associated with this sensor component

Subclassed by isaacsim::sensors::physx::GenericSensor , isaacsim::sensors::physx::LidarSensor , isaacsim::sensors::physx::LightBeamSensor
Public Functions
inlineRangeSensorComponentBase(omni ::physx ::IPhysx*physxPtr)

Constructs a new Isaac Component.
Initializes the component with necessary interfaces and creates visualization helpers
Parameters:
physxPtr – [in] Pointer to the PhysX interface for physics simulation

inline~RangeSensorComponentBase()

Destroys the Range Sensor Component Base object.
Cleans up visualization resources

inlinevirtualvoidinitialize(
constPrimType &prim,
pxr ::UsdStageWeakPtrstage,
)
Initializes various pointers and handles in the component.
Must be called after creation, can be overridden to initialize subcomponents
Parameters:

- prim – [in] The USD prim representing this sensor

- stage – [in] The USD stage containing the sensor prim

inlinevirtualvoidonStart()

Function that runs after start is pressed.
Initializes the component and locates the PhysX scene for sensor operations

inlinevirtualvoidpreTick()

Called before tick, sequential, used to get sensor transforms.
Empty base implementation that can be overridden by derived classes

virtualvoidtick()=0

Called every frame in parallel.
Pure virtual function that must be implemented by derived classes to perform the main sensor update during each simulation frame

inlinevirtualvoidonPhysicsStep()

Called after each physics step to update sensor data.
This function is called after each physics simulation step to process and update the range sensor data based on the latest physics state

inlinevirtualvoiddraw()

Called after all sensors have simulated to perform any drawing related tasks.
Renders the debug visualization for both points and lines if enabled

inlinevirtualvoidonStop()

Run when stop is pressed.
Clears all visualization data and ensures it’s properly rendered

inlinevirtualvoidonComponentChange()

Called every time the Prim is changed.
Updates component properties from the USD prim attributes and refreshes transform-related data

inlinevirtualvoidupdateTimestamp(
doubletimeSeconds,
doubledt,
int64_ttimeNano,
)
Updates timestamps for component.
Parameters:

- timeSeconds – [in] Current simulation time in seconds

- dt – [in] Time step duration in seconds

- timeNano – [in] Current simulation time in nanoseconds

inlineboolgetDrawPoints()

Gets the draw points visualization state.
Returns:
True if point visualization is enabled, false otherwise

inlineboolgetDrawLines()

Gets the draw lines visualization state.
Returns:
True if line visualization is enabled, false otherwise

inlinestd ::vector<carb::Float3>&getPointCloud()

Gets the latest point cloud data from the range sensor.
Returns a reference to the vector containing the most recent hit positions detected by the range sensor. Each point represents a detected surface in 3D space.
Returns:
Reference to vector of 3D points representing the latest point cloud data

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

inlinevirtualvoidonRenderEvent()

Called for each rendered frame.
Override this to implement render-specific behavior or visual updates

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
boolm_drawPoints=false

Flag to enable/disable point visualization.

boolm_drawLines=false

Flag to enable/disable line visualization.

std ::vector<carb::Float3>m_lastHitPos

Vector storing the most recent hit positions from the sensor.

floatm_minRange=0.4f

Minimum range of the sensor in meters.

floatm_maxRange=100.0f

Maximum range of the sensor in meters.

floatm_metersPerUnit=1.0

Conversion factor from scene units to meters.

pxr ::UsdPrimm_parentPrim

Reference to the parent USD prim containing this sensor.

omni ::physx ::IPhysx*m_physx=nullptr

Pointer to the PhysX interface.

::physx ::PxScene*m_pxScene=nullptr

Pointer to the PhysX scene.

omni ::timeline::ITimeline*m_timeline=nullptr

Pointer to the timeline interface.

omni ::fabric::IToken*m_token=nullptr

Pointer to the fabric token interface.

carb::tasking::ITasking*m_tasking=nullptr

Pointer to the tasking interface.

std ::shared_ptr<isaacsim ::util::debug_draw::drawing::PrimitiveDrawingHelper>m_lineDrawing

Helper for drawing debug lines.

std ::shared_ptr<isaacsim ::util::debug_draw::drawing::PrimitiveDrawingHelper>m_pointDrawing

Helper for drawing debug points.

pxr ::RangeSensorRangeSensorm_rangeSensorPrim

Reference to the range sensor USD prim.

pxr ::UsdTimeCodem_parentPrimTimeCode

Time code for the parent prim’s current state.

boolm_isParentPrimTimeSampled=false

Flag indicating if the parent prim has time-sampled transforms.

boolm_firstFrame=true

Flag indicating if this is the first frame.

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
