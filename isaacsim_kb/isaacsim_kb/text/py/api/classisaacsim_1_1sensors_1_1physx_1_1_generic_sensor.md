<!-- source: py/api/classisaacsim_1_1sensors_1_1physx_1_1_generic_sensor.html | title: GenericSensor — Isaac Sim -->

# GenericSensor
Fully qualified name: `isaacsim::sensors::physx::GenericSensor`
classGenericSensor:publicisaacsim ::sensors ::physx ::RangeSensorComponentBase <PrimType>

A generic range sensor implementation that supports customizable scanning patterns.
This sensor class provides a flexible range sensing capability with configurable azimuth and zenith angles, allowing for custom scanning patterns. It supports batch processing of sensor data and visualization options. The sensor can be configured to operate in streaming mode with adjustable sampling rates and batch sizes for efficient data processing.
Public Functions
explicitGenericSensor(omni ::physx ::IPhysx*physxPtr)

Constructs a new Generic Sensor instance.
Parameters:
physxPtr – [in] Pointer to the PhysX interface for physics simulation

~GenericSensor()

Virtual destructor for proper cleanup.

virtualvoidonStart()

Initializes the generic sensor when the component starts.
Sets up initial parameters, allocates memory for scan data, and prepares the sensor for operation

virtualvoidpreTick()

Performs pre-tick operations before the main sensor update.
Updates sensor parameters and prepares for the next scan cycle

virtualvoidtick()

Performs the main sensor update during each tick.
Executes the scanning operation and processes sensor data based on current configuration

virtualvoidonComponentChange()

Handles component property changes.
Updates sensor configuration when properties are modified through the interface

inlineintgetNumSamplesTicked()const

Gets the number of samples processed in the last tick.
Returns:
Number of samples processed

inlinestd ::vector<uint16_t>&getDepthData()

Gets the latest depth data from the sensor.
Returns:
Reference to vector containing normalized depth values (0-65535)

inlinestd ::vector<float>&getLinearDepthData()

Gets the latest linear depth data in meters.
Returns:
Reference to vector containing depth values in meters

inlinestd ::vector<uint8_t>&getIntensityData()

Gets the latest intensity data from the sensor.
Returns:
Reference to vector containing intensity values (0-255)

inlinestd ::vector<float>&getZenithData()

Gets the zenith angles for each sensor ray.
Returns:
Reference to vector containing zenith angles in radians

inlinestd ::vector<float>&getAzimuthData()

Gets the azimuth angles for each sensor ray.
Returns:
Reference to vector containing azimuth angles in radians

inlinestd ::vector<carb::Float3>&getOffsetData()

Gets the offset positions for each sensor ray.
Returns:
Reference to vector containing 3D offset positions

boolsendNextBatch()

Checks if the next batch of sensor pattern vectors should be sent.
Returns:
True if ready for next batch, false otherwise

voidsetNextBatchRays(
constfloat*azimuthAngles,
constfloat*zenithAngles,
constintsampleLength,
)
Sets the next batch of sensor pattern angles.
Parameters:

- azimuthAngles – [in] Array of azimuth angles in radians

- zenithAngles – [in] Array of zenith angles in radians

- sampleLength – [in] Number of samples in the batch

voidsetNextBatchOffsets(
constfloat*originOffsets,
constintsampleLength,
)
Sets the origin offsets for each ray in the next batch.
Parameters:

- originOffsets – [in] Array of 3D offset positions for each ray

- sampleLength – [in] Number of samples in the batch

inlinevirtualvoidinitialize(
constPrimType&prim,
pxr ::UsdStageWeakPtrstage,
)
Initializes various pointers and handles in the component.
Must be called after creation, can be overridden to initialize subcomponents
Parameters:

- prim – [in] The USD prim representing this sensor

- stage – [in] The USD stage containing the sensor prim

inlinevirtualvoidonPhysicsStep()

Called after each physics step to update sensor data.
This function is called after each physics simulation step to process and update the range sensor data based on the latest physics state

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

inlinevirtualvoiddraw()

Called after all sensors have simulated to perform any drawing related tasks.
Renders the debug visualization for both points and lines if enabled

inlinevirtualvoidonStop()

Run when stop is pressed.
Clears all visualization data and ensures it’s properly rendered

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

inlinevirtualvoidonRenderEvent()

Called for each rendered frame.
Override this to implement render-specific behavior or visual updates

inlinePrimType&getPrim()

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

PrimTypem_prim

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
