<!-- source: py/source/extensions/isaacsim.core.simulation_manager/docs/index.html | title: [isaacsim.core.simulation_manager] Isaac Sim Core Simulation Manager — Isaac Sim -->

# [isaacsim.core.simulation_manager] Isaac Sim Core Simulation Manager
Version: 1.4.4
The Core Simulation Manager extension provides a set of APIs to control and query the simulation’s state and the different callbacks available.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

[TABLE]
SimulationManager | This class provide functions that take care of many time-related events such as warm starting simulation in order for the physics data to be retrievable.
IsaacEvents |
[/TABLE]

classSimulationManager
Bases: `object`
This class provide functions that take care of many time-related events such as warm starting simulation in order for the physics data to be retrievable. Adding/ removing callback functions that gets triggered with certain events such as a physics step, on post reset, on physics ready..etc.
classmethodassets_loading()→bool
Checks if textures are loaded.
Returns:
True if textures are loading and not done yet, otherwise False.

Return type:
bool

classmethodderegister_callback(callback_id)
Deregisters a callback which was previously registered using register_callback.
Parameters:
callback_id – The ID of the callback returned by register_callback to deregister.

classmethodenable_all_default_callbacks(
enable:bool=True,
)→None Enable or disable all default callbacks. Default callbacks are: warm_start, on_stop, post_warm_start, stage_open.
Parameters:
enable – Whether to enable all callbacks.

classmethodenable_ccd(
flag:bool,
physics_scene:str=None,
)→None Enables Continuous Collision Detection (CCD).
Parameters:

- flag (bool) – enables or disables CCD on the PhysicsScene.

- physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

classmethodenable_fabric(enable)
Enables or disables physics fabric integration and associated settings.
Parameters:
enable – Whether to enable or disable fabric.

classmethodenable_fabric_usd_notice_handler(stage_id, flag)
Enables or disables the fabric usd notice handler.
Parameters:

- stage_id – The stage ID to enable or disable the handler for.

- flag – Whether to enable or disable the handler.

classmethodenable_gpu_dynamics(
flag:bool,
physics_scene:str=None,
)→None Enables gpu dynamics pipeline, required for deformables for instance.
Parameters:

- flag (bool) – enables or disables gpu dynamics on the PhysicsScene. If flag is true, CCD is disabled.

- physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

classmethodenable_on_stop_callback(enable:bool=True)→None
Enable or disable the on stop callback.
Parameters:
enable – Whether to enable the callback.

classmethodenable_post_warm_start_callback(
enable:bool=True,
)→None Enable or disable the post warm start callback.
Parameters:
enable – Whether to enable the callback.

classmethodenable_stablization(
flag:bool,
physics_scene:str=None,
)→None Enables additional stabilization pass in the solver.
Parameters:

- flag (bool) – enables or disables stabilization on the PhysicsScene

- physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

classmethodenable_stage_open_callback(
enable:bool=True,
)→None Enable or disable the stage open callback. Note: This also enables/disables the assets loading and loaded callbacks. If disabled, assets_loading() will always return True.
Parameters:
enable – Whether to enable the callback.

classmethodenable_usd_notice_handler(flag)
Enables or disables the usd notice handler.
Parameters:
flag – Whether to enable or disable the handler.

classmethodenable_warm_start_callback(
enable:bool=True,
)→None Enable or disable the warm start callback.
Parameters:
enable – Whether to enable the callback.

classmethodget_backend()→str
classmethodget_broadphase_type(
physics_scene:str=None,
)→strGets current broadcast phase algorithm type.
Parameters:
physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
Broadcast phase algorithm used.

Return type:
str

classmethodget_default_callback_status()→dict
Get the status of all default callbacks. Default callbacks are: warm_start, on_stop, post_warm_start, stage_open.
Returns:
Dictionary with callback names and their enabled status.

classmethodget_default_physics_scene()→str
classmethodget_num_physics_steps()
classmethodget_physics_dt(physics_scene:str=None)→str
Returns the current physics dt.

Parameters:
physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
physics dt.

Return type:
float

classmethodget_physics_sim_device()→str
classmethodget_physics_sim_view()
classmethodget_simulation_time()
classmethodget_solver_type(physics_scene:str=None)→str
Gets current solver type.
Parameters:
physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
solver used for simulation.

Return type:
str

classmethodinitialize_physics()→None
classmethodis_ccd_enabled(physics_scene:str=None)→bool
Checks if Continuous Collision Detection (CCD) is enabled.
Parameters:
physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
True if CCD is enabled, otherwise False.

Return type:
bool

classmethodis_default_callback_enabled(
callback_name:str,
)→boolCheck if a specific default callback is enabled. Default callbacks are: warm_start, on_stop, post_warm_start, stage_open.
Parameters:
callback_name – Name of the callback to check.

Returns:
Whether the callback is enabled.

classmethodis_fabric_enabled(enable)
Checks if fabric is enabled.
Parameters:
enable – Whether to check if fabric is enabled.

Returns:
True if fabric is enabled, otherwise False.

Return type:
bool

classmethodis_fabric_usd_notice_handler_enabled(stage_id)
Checks if fabric usd notice handler is enabled.
Parameters:
stage_id – The stage ID to check.

Returns:
True if fabric usd notice handler is enabled, otherwise False.

Return type:
bool

classmethodis_gpu_dynamics_enabled(
physics_scene:str=None,
)→boolChecks if Gpu Dynamics is enabled.
Parameters:
physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
True if Gpu Dynamics is enabled, otherwise False.

Return type:
bool

classmethodis_paused()
classmethodis_simulating()
classmethodis_stablization_enabled(
physics_scene:str=None,
)→boolChecks if stabilization is enabled.
Parameters:
physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
True if stabilization is enabled, otherwise False.

Return type:
bool

classmethodregister_callback(
callback:callable,
event,
order:int=0,
name:str=None,
)Registers a callback to be triggered when a specific event occurs.
Parameters:

- callback – The callback function to register.

- event – The event to trigger the callback.

- order – The order in which the callback should be triggered.

- name – The name of the callback.

Returns:
The ID of the callback.

Return type:
int

classmethodset_backend(val:str)→None
classmethodset_broadphase_type(
val:str,
physics_scene:str=None,
)→None Broadcast phase algorithm used in simulation.
Parameters:

- val (str) – type of broadcasting to be used, can be “MBP”.

- physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

classmethodset_default_physics_scene(
physics_scene_prim_path:str,
)set_physics_dt(
dt:float=0.016666666666666666,
physics_scene:str=None,
)→None Sets the physics dt on the physics scene provided.
Parameters:

- dt (float, optional) – physics dt. Defaults to 1.0/60.0.

- physics_scene (str, optional) – physics scene prim path. Defaults to first physics scene found in the stage.

Raises:

- Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

- ValueError – Physics dt must be a >= 0.

- ValueError – Physics dt must be a <= 1.0.

classmethodset_physics_sim_device(val)→None
classmethodset_solver_type(
solver_type:str,
physics_scene:str=None,
)→None solver used for simulation.
Parameters:

- solver_type (str) – can be “TGS” or “PGS”.

- physics_scene (str, optional) – physics scene prim path.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

classmethodstep(render:bool=False)

classIsaacEvents(
value,
names=None,
*,
module=None,
qualname=None,
type=None,
start=1,
boundary=None,
)Bases: `Enum`
PHYSICS_READY='isaac.physics_ready'
PHYSICS_WARMUP='isaac.physics_warmup'
POST_PHYSICS_STEP='isaac.post_physics_step'
POST_RESET='isaac.post_reset'
PRE_PHYSICS_STEP='isaac.pre_physics_step'
PRIM_DELETION='isaac.prim_deletion'
SIMULATION_VIEW_CREATED='isaac.simulation_view_created'
TIMELINE_STOP='isaac.timeline_stop'
