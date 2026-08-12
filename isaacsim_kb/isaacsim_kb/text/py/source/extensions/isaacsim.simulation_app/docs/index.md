<!-- source: py/source/extensions/isaacsim.simulation_app/docs/index.html | title: [isaacsim.simulation_app] Isaac Sim Kit Helpers — Isaac Sim -->

# [isaacsim.simulation_app] Isaac Sim Kit Helpers
Version: 2.12.2
This Extension that provides a way to launch a python app

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

[TABLE]
SimulationApp | Helper class to launch Omniverse Toolkit.
AppFramework | Minimal omniverse application that launches without any application config
[/TABLE]

classSimulationApp(launch_config:dict=None, experience:str='')
Bases: `object`
Helper class to launch Omniverse Toolkit.
Omniverse loads various plugins at runtime which cannot be imported unless the Toolkit is already running. Thus, it is necessary to launch the Toolkit first from your python application and then import everything else.
Usage:

```
# At top of your application
from isaacsim.simulation_app import SimulationApp
config = {
width: "1280",
height: "720",
headless: False,
}
simulation_app = SimulationApp(config)

# Rest of the code follows
...
simulation_app.close()
```
Note
The settings in DEFAULT_LAUNCHER_CONFIG are overwritten by those in `config`.
Parameters:

- config (dict) – A dictionary containing the configuration for the app. (default: None)

- experience (str) –
Path to the application config loaded by the launcher. If not specified, the launcher will load one of the following experience files in order (where `$EXP_PATH` points to the `apps` folder in a default Isaac Sim setup):

- `$EXP_PATH/omni.isaac.sim.python.kit`

- `$EXP_PATH/isaacsim.exp.base.python.kit`

- `$EXP_PATH/isaacsim.exp.base.kit`

close(
wait_for_replicator=True,
skip_cleanup=False,
)→None Close the running Omniverse Toolkit application.
Performs cleanup and shuts down the application. Can either perform a graceful shutdown with full cleanup or an immediate exit.
Parameters:

- wait_for_replicator – Whether to wait for replicator workflows to complete before shutdown.

- skip_cleanup – If True, performs immediate exit without cleanup. If False, performs graceful shutdown with full cleanup.

Example:

```
>>> simulation_app = SimulationApp()
>>> # Do simulation work...
>>> simulation_app.close(wait_for_replicator=True)
>>>
>>> # For immediate exit without cleanup:
>>> simulation_app = SimulationApp()
>>> simulation_app.close(skip_cleanup=True)
```

is_exiting()→bool
Check if the simulation application is in the process of exiting.
Returns True if close() has been called and the application is shutting down, False if the application is still running normally.
Returns:
True if close() was called previously, False otherwise.

Example:

```
>>> simulation_app = SimulationApp()
>>> simulation_app.is_exiting()
False
>>> simulation_app.close()
>>> simulation_app.is_exiting()
True
```

is_running()→bool
Check if the simulation application is currently running.
Returns True if the application is running and has a valid stage, False if the application is stopped or exiting.
Returns:
True if the application is running, False otherwise.

Example:

```
>>> simulation_app = SimulationApp()
>>> simulation_app.is_running()
True
>>> simulation_app.close()
>>> simulation_app.is_running()
False
```

reset_render_settings()
Reset render settings to those specified in the launch configuration.
Re-applies the rendering settings from the initial configuration. This should be used when a new stage is opened and the desired render configuration needs to be re-applied.
Example:

```
>>> config = {"renderer": "PathTracing", "samples_per_pixel_per_frame": 128}
>>> simulation_app = SimulationApp(config)
>>> # Open a new stage
>>> simulation_app.reset_render_settings() # Re-apply config settings
>>> simulation_app.close()
```

run_coroutine(
coroutine:asyncio.Coroutine,
run_until_complete:bool=True,
)→asyncio.Task|asyncio.Future|AnyRun a coroutine using Kit’s asynchronous task engine.
Executes the provided coroutine within Kit’s event loop system. The Kit’s asynchronous task engine runs the event loop every IApp update.
Parameters:

- coroutine – The coroutine to execute.

- run_until_complete – Whether to block and wait for coroutine completion.

Returns:
If run_until_complete is True, returns the coroutine result. Otherwise returns an asyncio.Task (from main thread) or asyncio.Future (from other threads).

Raises:
Exception – Any exception raised by the coroutine.

Example:

```
>>> import asyncio
>>> async def my_async_task():
... await asyncio.sleep(0.1)
... return "completed"
>>>
>>> simulation_app = SimulationApp()
>>> result = simulation_app.run_coroutine(my_async_task())
>>> print(result)
completed
>>> simulation_app.close()
```

set_setting(setting:str, value)→None
Set a Carbonite framework setting.
Sets a configuration value in the Carbonite settings system. The value type is automatically detected and used for proper setting assignment.
Parameters:

- setting – The Carbonite setting path (e.g., “/app/window/width”).

- value – The value to set. Type is automatically detected.

Example:

```
>>> simulation_app = SimulationApp()
>>> simulation_app.set_setting("/app/window/width", 1920)
>>> simulation_app.set_setting("/rtx/rendermode", "PathTracing")
>>> simulation_app.close()
```

update()→None
Step the application forward by one frame.
This is a convenience function that advances the simulation by a single frame, updating all systems and rendering.
Example:

```
>>> simulation_app = SimulationApp()
>>> # Run simulation for 10 frames
>>> for _ in range(10):
... simulation_app.update()
>>> simulation_app.close()
```

DEFAULT_LAUNCHER_CONFIG={'active_gpu':None,'anti_aliasing':3,'create_new_stage':True,'denoiser':True,'disable_viewport_updates':False,'display_options':3094,'enable_crashreporter':True,'extra_args':[],'fast_shutdown':True,'headless':True,'height':720,'hide_ui':None,'limit_cpu_threads':32,'max_bounces':4,'max_gpu_count':None,'max_specular_transmission_bounces':6,'max_volume_bounces':4,'multi_gpu':True,'open_usd':None,'physics_gpu':0,'profiler_backend':[],'renderer':'RaytracedLighting','samples_per_pixel_per_frame':64,'subdiv_refinement_level':0,'sync_loads':True,'width':1280,'window_height':900,'window_width':1440}
The config variable is a dictionary containing the following entries
Parameters:

- headless (bool) – Disable window creation and UI when running. Defaults to True

- hide_ui (bool) – Hide UI when running to improve performance, when headless is set to true, the UI is hidden, set to false to override this behavior when live streaming. Defaults to None

- active_gpu (int) – Specify the GPU to use when running, set to None to use default value which is usually the first gpu, default is None

- physics_gpu (int) – Specify the GPU to use when running physics simulation. Defaults to 0 (first GPU).

- multi_gpu (bool) – Set to true to enable Multi GPU support, Defaults to true

- max_gpu_count (int) – Maximum number of GPUs to use, Defaults to None which will use all available

- sync_loads (bool) – When enabled, will pause rendering until all assets are loaded. Defaults to True

- width (int) – Width of the viewport and generated images. Defaults to 1280

- height (int) – Height of the viewport and generated images. Defaults to 720

- window_width (int) – Width of the application window, independent of viewport, defaults to 1440,

- window_height (int) – Height of the application window, independent of viewport, defaults to 900,

- display_options (int) – used to specify whats visible in the stage by default. Defaults to 3094 so extra objects do not appear in synthetic data. 3286 is another good default, used for the regular isaac-sim editor experience

- subdiv_refinement_level (int) – Number of subdivisons to perform on supported geometry. Defaults to 0

- renderer (str) – Rendering mode, can be RaytracedLighting or PathTracing. Defaults to PathTracing

- anti_aliasing (int) – Antialiasing mode, 0: Disabled, 1: TAA, 2: FXAA, 3: DLSS, 4:RTXAA

- samples_per_pixel_per_frame (int) – The number of samples to render per frame, increase for improved quality, used for PathTracing only. Defaults to 64

- denoiser (bool) – Enable this to use AI denoising to improve image quality, used for PathTracing only. Defaults to True

- max_bounces (int) – Maximum number of bounces, used for PathTracing only. Defaults to 4

- max_specular_transmission_bounces (int) – Maximum number of bounces for specular or transmission, used for PathTracing only. Defaults to 6

- max_volume_bounces (int) – Maximum number of bounces for volumetric materials, used for PathTracing only. Defaults to 4

- open_usd (str) – This is the name of the usd to open when the app starts. It will not be saved over. Default is None and an empty stage is created on startup.

- fast_shutdown (bool) – True to exit process immediately, false to shutdown each extension. If running in a jupyter notebook this is forced to false.

- profiler_backend (list) – List of profiler backends to enable currently only supports the following backends: [“tracy”, “nvtx”]

- create_new_stage (bool) – Set False to not create a new stage on application startup. Defaults to True

- extra_args – (list): List of extra command line arguments to pass down to the kit process

- enable_crashreporter (bool) – Enable crash reporter. Defaults to True

- limit_cpu_threads (int) – Limit the number of CPU threads created to the lesser of cpu core count or specified value. Defaults to 32.

- disable_viewport_updates (bool) – Disable viewport updates to improve performance. Defaults to False.

propertyapp:omni.kit.app.IApp
Get the underlying Omniverse Kit application object.
Provides access to the low-level Kit application interface for advanced operations and direct framework access.
Returns:
The Omniverse Kit application interface object.

Example:

```
>>> simulation_app = SimulationApp()
>>> app = simulation_app.app
>>> app.update() # Direct app update
>>> simulation_app.close()
```

propertycontext:omni.usd.UsdContext
Get the current USD context for stage operations.
Provides access to the USD context which manages the current stage and USD-related operations.
Returns:
The current USD context object.

Example:

```
>>> simulation_app = SimulationApp()
>>> context = simulation_app.context
>>> stage = context.get_stage()
>>> print(stage.GetRootLayer().identifier)
>>> simulation_app.close()
```

classAppFramework(name:str='kit', argv=[])
Bases: `object`
Minimal omniverse application that launches without any application config
close()
Close the running Omniverse Toolkit.

update()→None
Convenience function to step the application forward one frame

propertyapp:omni.kit.app.IApp
omniverse kit application object
Type:
omni.kit.app.IApp

propertyframework:Any
omniverse kit application object
Type:
omni.kit.app.IApp
