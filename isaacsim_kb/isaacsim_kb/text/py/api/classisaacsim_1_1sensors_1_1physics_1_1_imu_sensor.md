<!-- source: py/api/classisaacsim_1_1sensors_1_1physics_1_1_imu_sensor.html | title: ImuSensor — Isaac Sim -->

# ImuSensor
Fully qualified name: `isaacsim::sensors::physics::ImuSensor`
classImuSensor:publicisaacsim ::sensors ::physics ::IsaacSensorComponentBase <PrimType>

Implementation of an Inertial Measurement Unit (IMU) sensor component.
This class provides functionality for simulating an IMU sensor in the Isaac environment. It handles acceleration, angular velocity, and orientation measurements, with support for raw data buffering and interpolation. The sensor supports configurable filtering for various measurements and maintains a history of readings for signal processing.
Public Functions
inlineImuSensor()

Default constructor for the IMU sensor.
Initializes the raw data buffer and resets the sensor to its initial state

voidinitialize(
std ::vector<float>*rigidBodyDataBuffer,
size_t&m_dataBufferIndex,
)
Initializes the IMU sensor with a data buffer.
Parameters:

- rigidBodyDataBuffer – [in] Pointer to the buffer storing rigid body data

- m_dataBufferIndex – [inout] Reference to the current buffer index

virtual~ImuSensor()

Virtual destructor for proper cleanup.

IsReading getSensorReading(
conststd ::function<IsReading (std ::vector<IsReading >,float)>&interpolateFunction=nullptr,
constbool&getLatestValue=false,
constbool&readGravity=true,
)
Retrieves the current sensor reading with optional interpolation.
Parameters:

- interpolateFunction – [in] Optional function for interpolating between readings

- getLatestValue – [in] Whether to return the most recent value without interpolation

- readGravity – [in] Whether to include gravity in the acceleration readings

Returns:
The current IMU sensor reading

voidreset()

Resets the sensor to its initial state.
Clears all buffers and resets internal state variables to their default values

virtualvoidonPhysicsStep()

Called by component manager tick to update sensor data.
Processes finite difference data in mRawReadingList and saves in m_readingPair

inlinevirtualvoidtick()

Empty tick implementation as processing is done in onPhysicsStep.

boolfindValidParent()

Searches for and validates the parent rigid body for the IMU sensor.
Returns:
True if a valid parent is found, false otherwise

virtualvoidonComponentChange()

Handles component property changes.
Updates sensor configuration when properties are modified through the interface

virtualvoidonStop()

Called when simulation is stopped.
The virtual onStop will clear everything on stop

voidprintIsReading(constIsReading &reading)

Utility function to print IMU sensor reading data for debugging.
Parameters:
reading – [in] The sensor reading to print

inlinevirtualvoidinitialize(
constPrimType&prim,
constpxr ::UsdStageWeakPtrstage,
)
Initializes the sensor component.
Sets up the sensor component with its USD prim and stage references.
Parameters:

- prim – [in] USD prim representing the sensor.

- stage – [in] USD stage containing the prim.

inlinevirtualvoidonStart()

Called when the sensor starts.
Handles sensor initialization when the component is started. Triggers onComponentChange to ensure proper initial state.

inlinevirtualvoidpreTick()

Called before each tick to prepare sensor state.
Provides an opportunity to prepare the sensor state before the main tick update. Default implementation does nothing.

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

inlinepxr ::UsdPrimgetParentPrim()

Gets the parent prim of the sensor.
Retrieves the USD prim that is the parent of this sensor.
Returns:
USD prim that is the parent of this sensor.

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
pxr ::UsdPrimm_parentPrim

USD prim that is the parent of this sensor.
Stores a reference to the parent USD prim that contains this sensor.

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
