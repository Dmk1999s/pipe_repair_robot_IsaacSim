<!-- source: py/api/classisaacsim_1_1sensors_1_1physx_1_1_light_beam_sensor.html | title: LightBeamSensor — Isaac Sim -->

# LightBeamSensor
Fully qualified name: `isaacsim::sensors::physx::LightBeamSensor`
classLightBeamSensor:publicisaacsim ::sensors ::physx ::RangeSensorComponentBase <PrimType>

A sensor that simulates a curtain of light beams for range detection.
This sensor projects multiple light beams in a curtain pattern to detect objects and measure distances. It is useful for applications like safety curtains, area monitoring, and object detection along a plane. The sensor uses PhysX ray casting to detect intersections with objects and provides hit status, depth measurements, and hit positions for each beam.
Public Functions
explicitLightBeamSensor(omni ::physx ::IPhysx*physXInterface)

Constructs a new Light Beam Sensor instance.
Parameters:
physXInterface – [in] Pointer to the PhysX interface for physics simulation

virtual~LightBeamSensor()=default

Virtual destructor for proper cleanup.

virtualvoidonStart()override

Initializes the light beam sensor when the component starts.
Sets up initial parameters, allocates memory for beam data, and prepares the sensor for operation

inlinevirtualvoidpreTick()override

Performs pre-tick operations before the main sensor update.
Empty implementation as no pre-tick operations are needed

inlinevirtualvoidtick()override

Performs the main sensor update during each tick.
Empty implementation as updates are handled in onPhysicsStep

inlinevirtualvoidonStop()override

Cleans up resources when the component stops.
Empty implementation as no specific cleanup is needed

virtualvoidonPhysicsStep()override

Updates sensor data during physics simulation steps.
Performs ray casting and updates beam hit data based on the current physics state

virtualvoidonComponentChange()override

Handles component property changes.
Updates sensor configuration when properties are modified through the interface

inlineintgetNumRays()const

Gets the number of rays in the light curtain.
Returns:
Number of individual light beams

inlinestd ::vector<uint8_t>&getBeamHitData()

Gets the hit status for each beam.
Returns:
Reference to vector containing hit flags (0 for no hit, 1 for hit)

inlinestd ::vector<float>&getLinearDepthData()

Gets the linear depth measurements for each beam.
Returns:
Reference to vector containing depth values in meters

inlinestd ::vector<carb::Float3>&getHitPosData()

Gets the hit positions for each beam.
Returns:
Reference to vector containing 3D hit positions

inlinevoidgetTransformData(
omni ::math::linalg::matrix4d&matrixOutput,
)
Gets the current transform of the sensor.
Parameters:
matrixOutput – [out] Output matrix containing the sensor’s position and orientation

inlinestd ::vector<carb::Float3>&getBeamOrigins()

Gets the origin points of all beams.
Returns:
Reference to vector containing 3D beam origin positions

inlinestd ::vector<carb::Float3>&getBeamEndPoints()

Gets the end points of all beams.
Returns:
Reference to vector containing 3D beam end positions

inlinevirtualvoidinitialize(
constPrimType&prim,
pxr ::UsdStageWeakPtrstage,
)
Initializes various pointers and handles in the component.
Must be called after creation, can be overridden to initialize subcomponents
Parameters:

- prim – [in] The USD prim representing this sensor

- stage – [in] The USD stage containing the sensor prim

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

inlinevirtualvoiddraw()

Called after all sensors have simulated to perform any drawing related tasks.
Renders the debug visualization for both points and lines if enabled

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
