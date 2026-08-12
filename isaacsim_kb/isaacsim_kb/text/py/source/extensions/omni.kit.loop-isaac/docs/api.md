<!-- source: py/source/extensions/omni.kit.loop-isaac/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

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
