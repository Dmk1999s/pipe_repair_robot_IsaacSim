<!-- source: py/api/structomni_1_1kit_1_1_i_run_loop_runner_impl.html | title: IRunLoopRunnerImpl — Isaac Sim -->

# IRunLoopRunnerImpl
Fully qualified name: `omni::kit::IRunLoopRunnerImpl`
structIRunLoopRunnerImpl

Interface for controlling the run loop execution.
Provides functionality to control the simulation loop’s execution mode and timing, allowing for manual stepping and mode control
Public Members
void(*setManualMode)(constboolenabled,conststd ::string&name)

Enables or disables manual stepping mode.
Param enabled:
[in] True to enable manual stepping, false for automatic

Param name:
[in] Identifier for the run loop instance

void(*setManualStepSize)(constdoubledt,conststd ::string&name)

Sets the time step size for manual stepping.
Param dt:
[in] Time step size in seconds

Param name:
[in] Identifier for the run loop instance

bool(*getManualMode)(conststd ::string&name)

Gets the manual mode for the run loop.
Param name:
[in] Identifier for the run loop instance

Return:
True if manual mode is enabled, false otherwise

double(*getManualStepSize)(conststd ::string&name)

Gets the manual step size for the run loop.
Param name:
[in] Identifier for the run loop instance

Return:
Manual step size in seconds
