<!-- source: py/api/classisaacsim_1_1sensors_1_1physics_1_1_contact_manager.html | title: ContactManager — Isaac Sim -->

# ContactManager
Fully qualified name: `isaacsim::sensors::physics::ContactManager`
classContactManager

Manages contact events and data in the physics simulation.
Handles the processing and storage of contact events between physical bodies, providing access to raw contact data and managing contact sensor states.
Public Functions
ContactManager()

Default constructor.

virtual~ContactManager()

Virtual destructor.

voidresetSensors()

Resets all contact sensors to their initial state.

voidprocessContact(
constomni ::physx ::ContactEventHeaderc,
constomni ::physx ::ContactData*contactDataBuffer,
uint32_t&dataIdx,
)
Processes a contact event from the physics engine.
Parameters:

- c – [in] Contact event header.

- contactDataBuffer – [in] Buffer containing contact data.

- dataIdx – [inout] Index into the contact data buffer.

CsRawData *getCsRawData(constchar*usdPath, size_t&size)

Gets raw contact data for a specific USD path.
Parameters:

- usdPath – [in] Path to the body in the USD stage.

- size – [out] Number of contact data points.

Returns:
Pointer to array of raw contact data.

CsRawData *getCsRawData(uint64_ttoken, size_t&size)

Gets raw contact data for a specific body token.
Parameters:

- token – [in] Body identifier token.

- size – [out] Number of contact data points.

Returns:
Pointer to array of raw contact data.

voidremoveRawData(constContactPair &p)

Removes raw contact data for a contact pair.
Parameters:
p – [in] Contact pair to remove data for.

voidonPhysicsStep(
constfloat&currentTime,
constfloat&timeElapsed,
)
Updates contact manager state each physics step.
Parameters:

- currentTime – [in] Current simulation time.

- timeElapsed – [in] Time elapsed since last step.

floatgetCurrentTime()

Gets the current simulation time.
Returns:
Current simulation time in seconds.
