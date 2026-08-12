<!-- source: py/api/classisaacsim_1_1sensors_1_1physics_1_1_contact_sensor.html | title: ContactSensor — Isaac Sim -->

# ContactSensor
Fully qualified name: `isaacsim::sensors::physics::ContactSensor`
classContactSensor:publicisaacsim ::sensors ::physics ::IsaacSensorComponentBase <PrimType>

Component for simulating contact sensors in the physics environment.
Manages a contact sensor that can detect and measure forces between physical bodies. Inherits from IsaacBaseSensorComponent to integrate with the sensor framework.
Public Functions
inlineContactSensor(
omni ::physx ::IPhysx*physXInterface,
ContactManager *contactManager,
)
Constructor for ContactSensor .
Parameters:

- physXInterface – [in] Pointer to the PhysX interface.

- contactManager – [in] Pointer to the contact manager instance.

virtual~ContactSensor()

Virtual destructor.

voidreset()

Resets the sensor to its initial state.

CsRawData *getRawData(size_t&size)

Gets the raw contact data from the sensor.
Parameters:
size – [out] Number of contact data points.

Returns:
Pointer to array of raw contact data.

CsReading getSensorReading(constbool&getLatestValue=false)

Gets the processed sensor reading.
Parameters:
getLatestValue – [in] If true, returns the latest simulation value instead of the last sensor reading.

Returns:
Processed contact sensor reading.

voidprocessRawContacts(
CsRawData *rawContact,
constsize_t&size,
constsize_t&index,
constdouble&time,
)
Processes raw contact data into sensor readings.
Parameters:

- rawContact – [in] Array of raw contact data.

- size – [in] Number of contact data points.

- index – [in] Index indicating data recency (0 for old, 1 for new).

- time – [in] Current simulation time.

virtualvoidonPhysicsStep()

Called each physics step to update sensor state.

inlinevirtualvoidtick()

Called each tick to update sensor state.
Note
onPhysicsStep is used to update the sensor state.

voidsetContactReportApi()

Sets up the contact report API for the sensor.

boolfindValidParent()

Finds a valid parent body for the sensor.
Returns:
True if a valid parent was found, false otherwise.

virtualvoidonComponentChange()

Handles component property changes.

virtualvoidonStop()

Called when the simulation stops.
Redraws the sensor after stopping, unlike the base class implementation.

voidprintRawData(CsRawData *data)

Debug function to print raw contact data.
Parameters:
data – [in] Pointer to raw contact data to print.

voidprintReadingPair()

Debug function to print the current reading pair.

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
