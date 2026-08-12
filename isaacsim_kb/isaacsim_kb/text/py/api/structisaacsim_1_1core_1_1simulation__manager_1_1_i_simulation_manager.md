<!-- source: py/api/structisaacsim_1_1core_1_1simulation__manager_1_1_i_simulation_manager.html | title: ISimulationManager — Isaac Sim -->

# ISimulationManager
Fully qualified name: `isaacsim::core::simulation_manager::ISimulationManager`
structISimulationManager

Interface for managing simulation state and callbacks.
Provides functionality for:

- Registering and managing callbacks for simulation events

- Controlling simulation state and timing

- Managing USD notice handlers

- Querying simulation and system time information

This interface serves as the main entry point for simulation management operations in Isaac Sim.
Public Functions
virtualintregisterDeletionCallback(
conststd ::function<void(std ::string)>&callback,
)=0
Registers a callback function to be called when a deletion event occurs.
Parameters:
callback – [in] Function to be called with the path of the deleted item.

Returns:
Unique identifier for the registered callback.

virtualintregisterPhysicsSceneAdditionCallback(
conststd ::function<void(std ::string)>&callback,
)=0
Registers a callback function to be called when a physics scene is added.
Parameters:
callback – [in] Function to be called with the path of the added physics scene.

Returns:
Unique identifier for the registered callback.

virtualboolderegisterCallback(constint&callbackId)=0

Deregisters a previously registered callback.
Parameters:
callbackId – [in] The unique identifier of the callback to deregister.

Returns:
True if callback was successfully deregistered, false otherwise.

virtualvoidreset()=0

Resets the simulation manager to its initial state.

virtualint&getCallbackIter()=0

Gets the current callback iteration counter.
Returns:
Reference to the current callback iteration counter.

virtualvoidsetCallbackIter(intconst&val)=0

Sets the callback iteration counter.
Parameters:
val – [in] New value for the callback iteration counter.

virtualvoidenableUsdNoticeHandler(boolconst&flag)=0

Enables or disables the USD notice handler.
Parameters:
flag – [in] True to enable the handler, false to disable.

virtualvoidenableFabricUsdNoticeHandler(
longstageId,
boolconst&flag,
)=0
Enables or disables the USD notice handler for a specific fabric stage.
Parameters:

- stageId – [in] ID of the fabric stage.

- flag – [in] True to enable the handler, false to disable.

virtualboolisFabricUsdNoticeHandlerEnabled(longstageId)=0

Checks if the USD notice handler is enabled for a specific fabric stage.
Parameters:
stageId – [in] ID of the fabric stage to check.

Returns:
True if the handler is enabled for the stage, false otherwise.

virtualdoublegetSimulationTime()=0

Gets the current simulation time.
Returns:
The current simulation time.

virtualdoublegetSimulationTimeMonotonic()=0

Gets the current simulation time which does not reset when the simulation is stopped.
Returns:
The current simulation time.

virtualdoublegetSystemTime()=0

Gets the current system time.
Returns:
The current system time.

virtualomni ::fabric::RationalTimegetCurrentTime()=0

Gets the current frame time from StageReaderWriter.
Returns the current frame time from StageReaderWriter’s getFrameTime() to ensure temporal consistency between time sample storage and frame timing.
This is useful for testing to track exact frame times being written to storage.
Returns:
Current rational time or kInvalidRationalTime if unavailable.

virtualsize_tgetNumPhysicsSteps()=0

Gets the current physics step count.
Returns:
The current physics step count.

virtualboolisSimulating()=0

Gets the current simulation time.
Returns:
The current simulation time.

virtualboolisPaused()=0

Gets the current simulation pause state.
Returns:
The current simulation pause state.

virtualdoublegetSimulationTimeAtTime(
constomni ::fabric::RationalTime&rtime,
)=0
Gets simulation time at a specific rational time.
Returns the simulation time corresponding to a specific rational time.
Parameters:
rtime – [in] Rational time to query simulation time for.

Returns:
Simulation time in seconds at the specified time.

virtualdoublegetSimulationTimeMonotonicAtTime(
constomni ::fabric::RationalTime&rtime,
)=0
Gets monotonic simulation time at a specific rational time.
Returns the monotonically increasing simulation time corresponding to a specific rational time.
Parameters:
rtime – [in] Rational time to query monotonic simulation time for.

Returns:
Monotonic simulation time in seconds at the specified time.

virtualdoublegetSystemTimeAtTime(
constomni ::fabric::RationalTime&rtime,
)=0
Gets system time at a specific rational time.
Returns the system (real-world) time corresponding to a specific rational time.
Parameters:
rtime – [in] Rational time to query system time for.

Returns:
System time in seconds at the specified time.

virtualstd ::vector<TimeSampleStorage::Entry>getAllSamples()=0

Gets all stored samples for testing and validation.
Returns:
Vector of all stored sample entries.

virtualsize_tgetSampleCount()=0

Gets the count of stored samples.
Returns:
Number of stored samples.

virtualvoidlogStatistics()=0

Logs sample storage statistics for debugging.

virtualstd ::optional<std ::pair<omni ::fabric::RationalTime,omni ::fabric::RationalTime>>getSampleRange(
)=0
Gets the time range of stored samples.
Returns:
Pair of (earliest_time, latest_time), or nullopt if empty.

virtualsize_tgetBufferCapacity()=0

Gets the maximum buffer capacity for time sample storage.
Returns:
Maximum number of samples that can be stored in the buffer.
