<!-- source: py/api/classisaacsim_1_1sensors_1_1physics_1_1_isaac_sensor_component_base.html | title: IsaacSensorComponentBase — Isaac Sim -->

# IsaacSensorComponentBase
Fully qualified name: `isaacsim::sensors::physics::IsaacSensorComponentBase`
template<classPrimType>
classIsaacSensorComponentBase:publicisaacsim ::core ::includes ::ComponentBase <PrimType >

Base class template for non-RTX Isaac sensors.
This class serves as the foundation for implementing non-RTX sensors in Isaac Sim. It provides the basic structure and lifecycle methods that all sensors should implement.
Note
This class inherits from ComponentBase to integrate with the Isaac Sim component system.
Template Parameters:
PrimType – The USD prim type representing the sensor. This type parameter allows different sensor implementations to use their specific USD prim types.

Subclassed by isaacsim::sensors::physics::ContactSensor , isaacsim::sensors::physics::ImuSensor
Public Functions
IsaacSensorComponentBase()=default

Default constructor.
Constructs a new instance of the sensor component.

~IsaacSensorComponentBase()=default

Virtual destructor.
Ensures proper cleanup of derived sensor classes.

inlinevirtualvoidinitialize(
constPrimType &prim,
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

inlinevirtualvoidonComponentChange()

Called when sensor component properties change.
Updates the sensor’s enabled state when component properties are modified.

inlinevirtualvoidpreTick()

Called before each tick to prepare sensor state.
Provides an opportunity to prepare the sensor state before the main tick update. Default implementation does nothing.

virtualvoidtick()=0

Pure virtual function called each tick to update sensor state.
This method must be implemented by derived classes to define the sensor’s behavior during each simulation tick.

inlinevirtualvoidonPhysicsStep()

Called each physics step to update sensor state.
Allows sensors to update their state based on physics simulation steps. Default implementation does nothing.

inlinevirtualvoidonStop()

Called when the sensor stops.
Handles cleanup when the sensor component is stopped. Default implementation does nothing.

inlinepxr ::UsdPrimgetParentPrim()

Gets the parent prim of the sensor.
Retrieves the USD prim that is the parent of this sensor.
Returns:
USD prim that is the parent of this sensor.

inlinevirtualvoidonPhysicsStep(floatdt)

Called during each physics simulation step.
Override this to implement physics-based behavior
Parameters:
dt – [in] Time step size in seconds

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
pxr ::UsdPrimm_parentPrim

USD prim that is the parent of this sensor.
Stores a reference to the parent USD prim that contains this sensor.

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
