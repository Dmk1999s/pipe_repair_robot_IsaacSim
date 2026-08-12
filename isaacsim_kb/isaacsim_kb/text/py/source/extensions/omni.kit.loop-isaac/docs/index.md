<!-- source: py/source/extensions/omni.kit.loop-isaac/docs/index.html | title: [omni.kit.loop-isaac] Isaac Loop Runner — Isaac Sim -->

# [omni.kit.loop-isaac] Isaac Loop Runner
Version: 1.3.7
Custom Loop Runner for Isaac Sim

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API

[TABLE]
RunLoopRunner |
[/TABLE]

Isaac loop bindings
classRunLoopRunner
Bases: `pybind11_object`
get_manual_mode(
self:omni.kit.loop._loop.RunLoopRunner ,
name:str='',
)→boolGets the manual mode for the run loop.
Parameters:
arg0 (`str`) – The name of the run loop. If name is an empty string, all active run loops are set.

Returns:
True if manual mode is enabled, false otherwise.

Return type:
`bool`

get_manual_step_size(
self:omni.kit.loop._loop.RunLoopRunner ,
name:str='',
)→floatGets dt for run loop.
Parameters:
arg0 (`str`) – The name of the run loop. If name is an empty string, all active run loops are set.

Returns:
The dt value for the run loop.

Return type:
`double`

set_manual_mode(
self:omni.kit.loop._loop.RunLoopRunner ,
enabled:bool='True',
name:str='',
)→None Sets dt for run loop.
Parameters:

- arg0 (`bool`) – Set to true to enable manual mode.

- arg1 (`str`) – The name of the run loop. If name is an empty string, all active run loops are set.

set_manual_step_size(
self:omni.kit.loop._loop.RunLoopRunner ,
dt:float='0.01667',
name:str='',
)→None Sets dt for run loop.
Parameters:

- arg0 (`double`) – The dt value to set to.

- arg1 (`str`) – The name of the run loop. If name is an empty string, all active run loops are set.

acquire_loop_interface(
plugin_name:str=None,
library_path:str=None,
)→omni.kit.loop._loop.RunLoopRunner release_loop_interface(
arg0:omni.kit.loop._loop.RunLoopRunner ,
)→None

## Settings

### Other Settings
The extension changes some settings of the application or other extensions, which are listed in the table below.

[TABLE]
Application/extension setting | Description | Value
app.runLoopsGlobal.syncToPresent | Don’t sync threads to the present thread | False
app.runLoops.main.rateLimitEnabled | Set to true to enable rate limiting for the main run loop | True
app.runLoops.main.rateLimitFrequency | Rate limit frequency in Hz for the main run loop | 120
app.runLoops.main.rateLimitUseBusyLoop | Set to true to use a busy loop for the main run loop | False
app.runLoops.present.rateLimitEnabled | Set to true to enable rate limiting for the present run loop | True
app.runLoops.present.rateLimitFrequency | Rate limit frequency in Hz for the present run loop | 60
app.runLoops.present.rateLimitUseBusyLoop | Set to true to use a busy loop for the present run loop | False
app.runLoops.rendering_0.rateLimitEnabled | Set to true to enable rate limiting for the rendering run loop | True
app.runLoops.rendering_0.rateLimitFrequency | Rate limit frequency in Hz for the rendering run loop | 120
app.runLoops.rendering_0.rateLimitUseBusyLoop | Set to true to use a busy loop for the rendering run loop | False
[/TABLE]
