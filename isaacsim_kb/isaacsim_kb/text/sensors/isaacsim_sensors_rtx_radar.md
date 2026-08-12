<!-- source: sensors/isaacsim_sensors_rtx_radar.html | title: RTX Radar Sensor — Isaac Sim Documentation -->

# RTX Radar Sensor
RTX Radar sensors are simulated at render time on the GPU with RTX hardware. Their results are then copied to the `GenericModelOutput` AOV for use.

## Overview
Note
In Isaac Sim 4.5 and earlier, RTX sensors were based on `Camera` prims. If the `Camera` prim’s `sensorModelPluginName` attribute was set to `omni.sensors.nv.radar.wpm_dmatapprox.plugin`, then the `Camera` prim was used to render the Radar. The Radar was configured using a JSON file whose filename (without extension) was set in the `Camera` prim’s `sensorModelConfig` attribute, assuming the file was present in a folder specified by the `app.sensors.nv.radar.profileBaseFolder` setting. Support for `Camera` prims as RTX Radars was deprecated in Isaac Sim 5.0.
RTX Radars are rendered using `OmniRadar` prims, with the `OmniSensorGenericRadarWpmDmatAPI` schema applied, as configured by attributes on the prim. After attaching a render product to the `OmniRadar` prim, and setting the `GenericModelOutput` AOV on the render product, the RTXSensor renderer will write Radar render results to the AOV.

## How to Create an RTX Radar
The `isaacsim.sensors.rtx` extension provides one API for creating RTX Radars. In addition, the `omni.replicator.core` extension provides even lower-level APIs for creating `OmnRadar` prims (including batch creation) and attaching render products to them.

### Create an RTX Radar using Command
The `IsaacSensorCreateRtxRadar` command creates a generic `OmniRadar` prim with the appropriate schemas applied, or a `Camera` prim with the appropriate attributes to support deprecated workflows.

```
import omni
from pxr import Gf

# Specify attributes to apply to the ``OmniRadar`` prim.
sensor_attributes = {'omni:sensor:tickRate': 10}

_, sensor = omni.kit.commands.execute(
"IsaacSensorCreateRtxRadar",
translation=Gf.Vec3d(0, 0, 0),
orientation=Gf.Quatd(1, 0, 0, 0,),
path="/radar",
parent=None,
visibility=False,
variant=None,
force_camera_prim=False,
**sensor_attributes,
)
```
The example command above creates an `OmniRadar` prim in the stage at the specified `translation` with the specified `orientation`, at path `/radar`. The prim is set to be invisible in the stage. The prim’s `omni:sensor:Core:tickRate` attribute is set to 10 Hz from 20 Hz (default).
Review the OmniSensorGenericRadarWpmDmatAPI schema in the `omni.usd.schema.omni_sensors` extension to learn which attributes can be set on the `OmniRadar` prim.
Setting `force_camera_prim` to `True` will instead create an invisible `Camera` prim at the specified `translation` and `orientation`.
Annotators can then be attached to the `OmniRadar` prim to visualize the Radar results. Details about available annotators can be explored here .

## Sensor Materials
The material system for RTX Radar allows content creators to assign sensor material types to partial material prim names on a USD stage. Radar return behavior depends on material properties (for example, emissivity, reflectivity), as described below.

## Standalone Examples
For examples of creating RTX Radar refer to the examples:

```
./python.sh standalone_examples/api/isaacsim.util.debug_draw/rtx_radar.py
```
Note
Refer to the Isaac Sim Conventions documentation for a complete list of Isaac Sim conventions.
