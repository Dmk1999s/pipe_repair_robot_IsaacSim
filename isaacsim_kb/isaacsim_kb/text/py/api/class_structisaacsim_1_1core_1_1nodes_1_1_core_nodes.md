<!-- source: py/api/class_structisaacsim_1_1core_1_1nodes_1_1_core_nodes.html | title: CoreNodes — Isaac Sim -->

# CoreNodes
Fully qualified name: `isaacsim::core::nodes::CoreNodes`
classCoreNodes

Minimal interface for core node functionality.
This interface doesn’t have any functions, but just implementing it and acquiring will load your plugin, trigger calls of carbOnPluginStartup() and carbOnPluginShutdown() methods and allow you to use other Carbonite plugins. That by itself can get you quite far and is useful as a basic building block for Kit extensions. One can define their own interface with own python bindings when needed and abandon this one.
Public Members
double(*getSimTime)()

Gets the current simulation time.
Returns the current time in the simulation.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getSimulationTime() instead.

Return:
Current simulation time in seconds.

double(*getSimTimeMonotonic)()

Gets the monotonic simulation time.
Returns a simulation time that is guaranteed to be monotonically increasing.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getSimulationTimeMonotonic() instead.

Return:
Monotonically increasing simulation time in seconds.

double(*getSystemTime)()

Gets the current system time.
Returns the current system (real-world) time.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getSystemTime() instead.

Return:
Current system time in seconds.

size_t(*getPhysicsNumSteps)()

Gets the number of physics steps executed.
Returns the total count of physics steps that have been completed since simulation start.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getNumPhysicsSteps() instead.

Return:
Number of physics steps completed since simulation start.

uint64_t(*addHandle)(void*handle)

Adds a handle to the handle registry.
Registers a new handle in the handle registry and returns a unique identifier for it.
Param handle:
[in] Pointer to the handle to add.

Return:
Unique identifier for the added handle.

void*(*getHandle)(constuint64_thandleId)

Retrieves a handle from the handle registry.
Looks up and returns a handle by its unique identifier.
Param handleId:
[in] Unique identifier of the handle to retrieve.

Return:
Pointer to the handle if found, nullptr otherwise.

bool(*removeHandle)(constuint64_thandleId)

Removes a handle from the handle registry.
Unregisters a handle from the handle registry by its unique identifier.
Param handleId:
[in] Unique identifier of the handle to remove.

Return:
True if handle was successfully removed, false otherwise.

double(*getSimTimeAtTime)(constomni ::fabric::RationalTime&time)

Gets simulation time at a specific rational time.
Returns the simulation time corresponding to a specific rational time.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getSimulationTimeAtTime() instead.

Param time:
[in] Rational time to query simulation time for.

Return:
Simulation time in seconds at the specified time.

double(*getSimTimeMonotonicAtTime)(constomni ::fabric::RationalTime&time)

Gets monotonic simulation time at a specific rational time.
Returns the monotonically increasing simulation time corresponding to a specific rational time.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getSimulationTimeMonotonicAtTime() instead.

Param time:
[in] Rational time to query monotonic simulation time for.

Return:
Monotonic simulation time in seconds at the specified time.

double(*getSystemTimeAtTime)(constomni ::fabric::RationalTime&time)

Gets system time at a specific rational time.
Returns the system (real-world) time corresponding to a specific rational time.
Deprecated:
Use isaacsim::core::simulation_manager::ISimulationManager::getSystemTimeAtTime() instead.

Param time:
[in] Rational time to query system time for.

Return:
System time in seconds at the specified time.
