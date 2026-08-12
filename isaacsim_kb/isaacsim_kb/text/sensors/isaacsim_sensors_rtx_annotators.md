<!-- source: sensors/isaacsim_sensors_rtx_annotators.html | title: RTX Sensor Annotators — Isaac Sim Documentation -->

# RTX Sensor Annotators
The `isaacsim.sensors.rtx` extension uses Omniverse Replicator to provide Annotators for RTX Lidar and Radar data collection. Annotators can be attached to render products, attached to `OmniSensor` prims (for example, `OmniLidar` or `OmniRadar`); for example, when run in the Script Editor, the following snippet creates an `OmniLidar` prim at `/lidar`, a render product for the sensor, and attaches an `IsaacExtractRTXSensorPointCloudNoAccumulator` annotator to the render product.

```
import omni
import omni.replicator.core as rep
from pxr import Gf

# Create an OmniLidar prim at prim path /lidar
_, sensor = omni.kit.commands.execute(
"IsaacSensorCreateRtxLidar",
translation=Gf.Vec3d(0.0, 0.0, 0.0),
orientation=Gf.Quatd(1.0, 0.0, 0.0, 0.0),
path="/lidar",
)

# Create a render product for the sensor.
render_product = rep.create.render_product(sensor.GetPath(), resolution=(1024, 1024))

# Create an annotator
annotator = rep.AnnotatorRegistry.get_annotator("IsaacExtractRTXSensorPointCloudNoAccumulator")

# Attach the render product after the annotator is initialized.
annotator.attach([render_product.path])
```
Alternatively, the `LidarRtx` class offers a single API for attaching any annotator to an `OmniLidar` prim and collecting data. For example, in a standalone Python workflow, the following snippet creates an `OmniLidar` prim at `/lidar`, creates a render product for the sensor, and attaches an `IsaacExtractRTXSensorPointCloudNoAccumulator` annotator to it, then collects data from the annotator on each simulation frame. Note that this snippet will not run in the script editor window.

```
from isaacsim import SimulationApp

kit = SimulationApp()

import numpy as np
import omni
from isaacsim.sensors.rtx import LidarRtx

# Create the RTX Lidar with the specified attributes.
sensor = LidarRtx(
prim_path="/lidar",
translation=np.array([0.0, 0.0, 1.0]),
orientation=np.array([1.0, 0.0, 0.0, 0.0]),
config_file_name="Example_Rotary",
)

# Initialize the LidarRtx object, which creates a render product for the sensor.
sensor.initialize()

# Attach an annotator to the sensor.
sensor.attach_annotator("IsaacExtractRTXSensorPointCloudNoAccumulator")

# Play the timeline to initialize the OmniGraph associated with the annotator and render product,
# and begin collecting data.
timeline = omni.timeline.get_timeline_interface()
timeline.play()

# Collect data from the annotator on each simulation frame.
while kit.is_running():
# Step the simulation
kit.update()
# Print data collected by each annotator attached to the sensor as a Python dict
print(sensor.get_current_frame())

timeline.stop()
kit.close()
```
Warning
RTX Sensor Annotators rely on the simulation timeline to collect data. If the timeline is not playing (e.g. if the simulation is paused or stopped), the annotators will not collect data. The `GenericModelOutput` AOV produced by RTX Sensors contains an internal timestamp, which increases monotonically starting when `App Ready` appears in the simulation logs. This timestamp is independent of the animation timeline (`omni.timeline`), so the sensor timestamp will continue to increase even if the timeline is paused or stopped. If the user pauses the timeline, then resumes, timestamps in the `GenericModelOutput` point cloud (eg. the `timestamp` field of `IsaacCreateRTXLidarScanBuffer` below) may be discontinuous. This also means the simulation must be stepped using `omni.kit.app.get_app().update` or `omni.kit.app.get_app().next_update_async()` rather than `omni.replicatore.core.orchestrator.step()` or `omni.replicatore.core.orchestrator.step_async()` when collecting data using these Annotators. Note Isaac Sim APIs for updating the simulation state use the former two methods rather than the latter two.

## Annotators
Each `isaacsim.sensors.rtx` Annotator is associated with a specific `isaacsim.sensors.rtx` OmniGraph node, which is linked in that Annotator’s subsection below. The inputs and outputs of the Annotator are the same as the inputs and outputs of the corresponding OmniGraph node.
Note
In Isaac Sim 5.0, several existing `isaacsim.sensors.rtx` annotators were removed in favor of simpler annotators that can handle output from the new `OmniLidar` or `OmniRadar` prims, in addition to the deprecated `Camera`-prim-based workflows. See Deprecated Annotators for details.
If the Lidar rotation rate is slower than the frame rate, data from Annotators for accumulated Lidar scans will contain returns from multiple frames. If the Lidar prim moves between frames, or objects move in the scene, the buffer might contain returns from before the Lidar or objects moved, causing points to appear as though they are “dragging” behind objects when viewed with the `DebugDrawPointCloud` or `DebugDrawPointCloudBuffer` writers.
`isaacsim.sensors.rtx` annotators rely on the `GenericModelOutput` AOV from the `OmniLidar` prim being provided on device. If `--/app/sensors/nv/lidar/outputBufferOnGPU` or `--/app/sensors/nv/radar/outputBufferOnGPU` is set to `false`, the annotators will not function correctly.

### IsaacCreateRTXLidarScanBuffer
The `IsaacCreateRTXLidarScanBuffer` Annotator accumulates frames of data from an `OmniLidar` prim into a single scan, and provides the accumulated scan data as outputs. It is associated with the IsaacCreateRTXLidarScanBuffer node.
By default the node outputs a 3D Cartesian point cloud, and can optionally output the following data if the user sets the corresponding input flag to `True` when initializing the Annotator.
If creating the Annotator directly using the Replicator API, this can be done as follows:

```
import omni.replicator.core as rep
annotator = rep.AnnotatorRegistry.get_annotator("IsaacCreateRTXLidarScanBuffer")
# Initialize the Annotator with the desired outputs.
# Note: This must be done before attaching the Annotator to a render product.
annotator.initialize(outputTimestamp=True, outputMaterialId=True)
```
If creating the Annotator through the `LidarRtx` class, this can be done as follows:

```
sensor = LidarRtx(
prim_path="/lidar",
translation=np.array([0.0, 0.0, 1.0]),
orientation=np.array([1.0, 0.0, 0.0, 0.0]),
config_file_name="Example_Rotary")
sensor.initialize()
# Initialize the specified Annotator with the flags as keyword arguments, then attach it to the render product.
sensor.attach_annotator("IsaacCreateRTXLidarScanBuffer", outputTimestamp=True, outputMaterialId=True)
```
The node outputs data as pointers to buffers and the table below specifies the data type of each buffer.

[TABLE]
Output | Type | Description | Notes
data | float3 | 3D Cartesian point cloud. | Always provided.
azimuth | float | Azimuth of each return, in degrees. | Provided if outputAzimuth is set to true .
elevation | float | Elevation of each return, in degrees. | Provided if outputElevation is set to true .
distance | float | Range of each return, in world units (by default, meters). | Provided if outputDistance is set to true .
intensity | float | Intensity of each return, normalized as described here . | Provided if outputIntensity is set to true .
timestamp | uint64 | Timestamp of each return, in nanoseconds since the start of the simulation. | Provided if outputTimestamp is set to true .
emitterId | uint32 | ID of the emitter that emitted the return. | Provided if outputEmitterId is set to true , and omni:sensor:Core:auxOutputType is set to BASIC (or higher) on the OmniLidar prim.
materialId | uint32 | ID of the material of the object that generated the return. | Provided if outputMaterialId is set to true , and omni:sensor:Core:auxOutputType is set to EXTRA (or higher) on the OmniLidar prim. Refer to RTX Sensor Non-Visual Materials for more details on how material IDs are computed.
objectId | uint8 | ID of the object that generated the return. | Provided if outputObjectId is set to true , and omni:sensor:Core:auxOutputType is set to EXTRA (or higher) on the OmniLidar prim, and --/rtx-transient/stableIds/enabled=true is set. Object ID is a stable, unique 128-bit unsigned integer mapping to the prim path of the object that generated the corresponding return. See Semantic Segmentation with RTX Sensor using Object IDs for more details.
normal | float3 | Normal to the surface of the object that generated the return. | Provided if outputNormal is set to true , omni:sensor:Core:auxOutputType is set to FULL on the OmniLidar prim, and --/app/sensors/nv/lidar/publishNormals=true is set.
velocity | float3 | Velocity of the object that generated the return. | Provided if outputVelocity is set to true , and omni:sensor:Core:auxOutputType is set to FULL on the OmniLidar prim.
[/TABLE]
Warning
Enabling nonzero `normal` output by setting `--/app/sensors/nv/lidar/publishNormals=true` will increase VRAM usage and might negatively impact performance.

### IsaacComputeRTXLidarFlatScan
The `IsaacComputeRTXLidarFlatScan` Annotator extracts depth and azimuth data from an accumulated 2D RTX Lidar scan. It is associated with the IsaacComputeRTXLidarFlatScan node.
The `IsaacComputeRTXLidarFlatScan` Annotator does not support RTX Radar.
If the annotator is attached to a 3D Lidar (defined as having emitters at nonzero elevation angles), the annotator will not return any data.
Even if `--/app/sensors/nv/lidar/outputBufferOnGPU=true` is set, `IsaacComputeRTXLidarFlatScanSimulationTime` output data will be on host memory.

### IsaacExtractRTXSensorPointCloudNoAccumulator
The `IsaacExtractRTXSensorPointCloud` Annotator extracts the `GenericModelOutput` buffer’s point cloud data into a Cartesian vector `data` buffer every frame. It is associated with the IsaacCreateRTXLidarScanBuffer node, with `enablePerFrameOutput` set to `true`.
Note
Isaac Sim 5.0 previously used the `IsaacExtractRTXSensorPointCloud` node for this annotator, but that node was removed after performance improvements were made to the `IsaacCreateRTXLidarScanBuffer` node.

## Reading Data from the GenericModelOutput Buffer
Note
Isaac Sim 4.5 included the `OgnIsaacReadRTXLidarData` node, which provided an example of reading data from the `GenericModelOutput` buffer in Python. This node has been removed as of Isaac Sim 5.0 and replaced by the utility module and functions described below.
The `isaacsim.sensors.rtx.generic_model_output` Python module provides APIs for inspecting the `GenericModelOutput` buffer, generated by the `GenericModelOutput` annotator.
For more information on the `GenericModelOutput` buffer, see the API documentation. .
For an example of reading data from the `GenericModelOutput` buffer from Isaac Sim, checkout the standalone example located at `standalone_examples/api/isaacsim.sensors.rtx/inspect_lidar_metadata.py`.

### Semantic Segmentation with RTX Sensor using Object IDs
The `GenericModelOutput` struct includes a `objId` field and the `IsaacCreateRTXLidarScanBuffer` node outputs an optional `objectId` output.
In both cases, the data is provided as a `numpy` array of `dtype``np.uint8`, and is only populated if `--/rtx-transient/stableIds/enabled=true` is set. This data is meant to be interpreted as a sequence of 128-bit unsigned integers (effectively `stride` 16), which are stable, unique IDs corresponding to unique prim paths in the scene. In other words, the `i`-th 128-bit unsigned integer in the array corresponds to prim generating the `i`-th return from the sensor. This can be used for semantic segmentation of the scene, by mapping the object IDs to prim paths and then retrieving semantic labels from the prims.
The `isaacsim.sensors.rtx.LidarRtx` class provides two utility functions for resolving object IDs as prim paths.
First, `LidarRtx.decode_stable_id_mapping` resolves the output of the `StableIdMap` AOV (which can be generated from an `OmniLidar`, `OmniRadar`, or `Camera` prim) as a Python `dict` mapping 128-bit unsigned integers to prim paths.
Second, `LidarRtx.get_object_ids` resolves the object ID array output from `GenericModelOutput` or `IsaacCreateRTXLidarScanBuffer` as 128-bit unsigned integers.
Refer to `standalone_examples/api/isaacsim.sensors.rtx/resolve_object_ids_from_gmo.py` for an example of using these functions to resolve object IDs as prim paths.

## Deprecated Annotators
Several annotators have been removed and or replaced by the annotators described above, as of Isaac Sim 5.0.
New annotator outputs are not guaranteed to be the same as the outputs of the deprecated annotators, gmoBufferPointer the table below describes affected annotators and how to replace them.

[TABLE]
Deprecated Isaac Sim 4.5 Annotator | Replacement | Details
IsaacComputeRTXLidarFlatScanSimulationTime | IsaacComputeRTXLidarFlatScan | The new annotator outputs the same data as the old annotator. To get an associated timestamp, use the IsaacReadSimulationTime annotator.
IsaacComputeRTXLidarFlatScanSystemTime | IsaacComputeRTXLidarFlatScan | The new annotator outputs the same data as the old annotator. To get an associated timestamp, use the IsaacReadSystemTime annotator.
RtxSensorCpuIsaacComputeRTXLidarPointCloud | IsaacExtractRTXSensorPointCloudNoAccumulator | The new annotator outputs the same data as the old annotator, excluding azimuth , elevation , and range . These values can be computed from the Cartesian data buffer. The new annotator also automatically supports CPU or GPU output based on the --/app/sensors/nv/lidar/outputBufferOnGPU and --/app/sensors/nv/radar/outputBufferOnGPU settings, rather than Annotator type.
RtxSensorGpuIsaacComputeRTXLidarPointCloud | IsaacExtractRTXSensorPointCloudNoAccumulator | See above.
RtxSensorCpuIsaacComputeRTXRadarPointCloud | IsaacExtractRTXSensorPointCloudNoAccumulator | See above.
RtxSensorGpuIsaacComputeRTXRadarPointCloud | IsaacExtractRTXSensorPointCloudNoAccumulator | See above.
IsaacReadRTXLidarData | isaacsim.sensors.rtx.read_gmo_data utility. | See Reading Data from the GenericModelOutput Buffer for details.
[/TABLE]
