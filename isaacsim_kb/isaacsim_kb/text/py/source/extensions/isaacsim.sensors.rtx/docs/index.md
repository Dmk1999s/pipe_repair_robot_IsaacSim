<!-- source: py/source/extensions/isaacsim.sensors.rtx/docs/index.html | title: [isaacsim.sensors.rtx] Isaac Sim Isaac Sensor Simulation — Isaac Sim -->

# [isaacsim.sensors.rtx] Isaac Sim Isaac Sensor Simulation
Version: 15.8.4
Provides APIs for RTX-based sensors, including RTX Lidar & RTX Radar.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API
Commands

[TABLE]
IsaacSensorCreateRtxLidar | Command class for creating RTX Lidar sensors.
IsaacSensorCreateRtxIDS | Command class for creating RTX Idealized Depth Sensors (IDSs).
IsaacSensorCreateRtxRadar | Command class for creating RTX Radar sensors.
[/TABLE]
Sensors

[TABLE]
LidarRtx | RTX-based Lidar sensor implementation.
[/TABLE]

#### Commands
classIsaacSensorCreateRtxLidar(*args:Any, **kwargs:Any)
Bases: `IsaacSensorCreateRtxSensor`
Command class for creating RTX Lidar sensors.
This class specializes the base RTX sensor creation for Lidar sensors, providing specific configuration and plugin settings for Lidar functionality.
_replicator_api
Static method reference to the Lidar Replicator API.

_sensor_type
Set to “lidar”.

_supported_configs
List of supported Lidar configurations.

_schema
Schema for Lidar sensors.

_sensor_plugin_name
Name of the Lidar sensor plugin.

classIsaacSensorCreateRtxIDS(*args:Any, **kwargs:Any)
Bases: `IsaacSensorCreateRtxSensor`
Command class for creating RTX Idealized Depth Sensors (IDSs).
This class specializes the base RTX sensor creation for IDSs, providing specific configuration and plugin settings for IDS functionality.
_sensor_type
Set to “ids”.

_sensor_plugin_name
Name of the IDS sensor plugin.

classIsaacSensorCreateRtxRadar(*args:Any, **kwargs:Any)
Bases: `IsaacSensorCreateRtxSensor`
Command class for creating RTX Radar sensors.
This class specializes the base RTX sensor creation for Radar sensors, providing specific configuration and plugin settings for Radar functionality.
_replicator_api
Static method reference to the Radar Replicator API.

_sensor_type
Set to “radar”.

_schema
Schema for Radar sensors.

_sensor_plugin_name
Name of the Radar sensor plugin.

#### Sensors
classLidarRtx(
prim_path:str,
name:str='lidar_rtx',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
config_file_name:str|None =None,
**kwargs,
)Bases: BaseSensor
RTX-based Lidar sensor implementation.
This class provides functionality for creating and managing RTX-based Lidar sensors in Isaac Sim. It supports various annotators and writers for data collection and visualization.
The sensor can be configured with different parameters and supports both point cloud and flat scan data collection.
add_azimuth_data_to_frame()
Add azimuth data to the current frame.
This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.

add_azimuth_range_to_frame()
Add azimuth range data to the current frame.
This method is deprecated as of Isaac Sim 5.0. Use attach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

add_elevation_data_to_frame()
Add elevation data to the current frame.
This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.

add_horizontal_resolution_to_frame()
Add horizontal resolution data to the current frame.
This method is deprecated as of Isaac Sim 5.0. Use attach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

add_intensities_data_to_frame()
Add intensities data to the current frame.
This method is deprecated as of Isaac Sim 5.0. Use attach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

add_linear_depth_data_to_frame()
Add linear depth data to the current frame.
This method is deprecated as of Isaac Sim 5.0. Use attach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

add_point_cloud_data_to_frame()
Add point cloud data to the current frame.
This method is deprecated as of Isaac Sim 5.0. Use attach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

add_range_data_to_frame()
Add range data to the current frame.
This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.

apply_visual_material(
visual_material:VisualMaterial ,
weaker_than_descendants:bool=False,
)→None Apply visual material to the held prim and optionally its descendants.
Parameters:

- visual_material (VisualMaterial ) – visual material to be applied to the held prim. Currently supports PreviewSurface, OmniPBR and OmniGlass.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import OmniGlass
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlass(
... prim_path="/World/material/glass", # path to the material prim to create
... ior=1.25,
... depth=0.001,
... thin_walled=False,
... color=np.array([0.5, 0.0, 0.0])
... )
>>> prim.apply_visual_material(material)
```

attach_annotator(
annotator_name:Literal['IsaacComputeRTXLidarFlatScan','IsaacExtractRTXSensorPointCloudNoAccumulator','IsaacCreateRTXLidarScanBuffer','StableIdMap','GenericModelOutput'],
**kwargs,
)→None Attach an annotator to the Lidar sensor.
Parameters:

- annotator_name (param) – Name of the annotator to attach. Must be one of: - “IsaacComputeRTXLidarFlatScan” - “IsaacExtractRTXSensorPointCloudNoAccumulator” - “IsaacCreateRTXLidarScanBuffer” - “StableIdMap” - “GenericModelOutput”

- **kwargs – Additional arguments to pass to the annotator on initialization.

attach_writer(writer_name:str, **kwargs)→None
Attach a writer to the Lidar sensor.
Parameters:

- writer_name (param) – Name of the writer to attach.

- **kwargs – Additional arguments to pass to the writer on initialization.

staticdecode_stable_id_mapping(stable_id_mapping_raw:bytes)
Decode the StableIdMap buffer into a dictionary of stable IDs to labels. The buffer is a sequence of 6-byte entries, each containing: - 4 bytes for the stable ID (uint32) - 1 byte for the label length (uint8) - 1 byte for the label offset (uint8) The label is a UTF-8 string of the specified length, starting at the offset.

detach_all_annotators()→None
Detach all annotators from the Lidar sensor.

detach_all_writers()→None
Detach all writers from the Lidar sensor.

detach_annotator(annotator_name:str)→None
Detach an annotator from the Lidar sensor.
Parameters:
annotator_name (param) – Name of the annotator to detach.

detach_writer(writer_name:str)→None
Detach a writer from the Lidar sensor.
Parameters:
writer_name (param) – Name of the writer to detach.

disable_visualization()
Disable visualization of the Lidar point cloud data.

enable_visualization()
Enable visualization of the Lidar point cloud data.

get_annotators()→dict
Get all attached annotators.
Returns:
Dictionary mapping annotator names to their instances.

Return type:
dict

get_applied_visual_material()→VisualMaterial
Return the current applied visual material in case it was applied using apply_visual_material or it’s one of the following materials that was already applied before: PreviewSurface, OmniPBR and OmniGlass.
Returns:
the current applied visual material if its type is currently supported.

Return type:
VisualMaterial

Example:

```
>>> # given a visual material applied
>>> prim.get_applied_visual_material()
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f36263106a0>
```

get_azimuth_range()→Tuple[float,float]
Get the azimuth range of the Lidar sensor.
This method is deprecated as of Isaac Sim 5.0. Use the azimuth_range attribute in the current frame instead.
Returns:
Tuple of (min_azimuth, max_azimuth) if available, None otherwise.

Return type:
Optional[Tuple[float, float]]

get_current_frame()→dict
Get the current frame data from the Lidar sensor.
Returns:
Dictionary containing the current frame data including rendering time,
frame number, and any attached annotator data.

Return type:
dict

get_default_state()→XFormPrimState
Get the default prim states (spatial position and orientation).
Returns:
an object that contains the default state of the prim (position and orientation)

Return type:
XFormPrimState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.XFormPrimState object at 0x7f33addda650>
>>>
>>> state.position
[-4.5299529e-08 -1.8347054e-09 -2.8610229e-08]
>>> state.orientation
[1. 0. 0. 0.]
```

get_depth_range()→Tuple[float,float]
Get the depth range of the Lidar sensor.
This method is deprecated as of Isaac Sim 5.0. Use the depth_range attribute in the current frame instead.
Returns:
Tuple of (min_depth, max_depth) if available, None otherwise.

Return type:
Optional[Tuple[float, float]]

get_horizontal_fov()→float
Get the horizontal field of view of the Lidar sensor.
This method is deprecated as of Isaac Sim 5.0. Use the horizontal_fov attribute in the current frame instead.
Returns:
The horizontal field of view value if available, None otherwise.

Return type:
Optional[float]

get_horizontal_resolution()→float
Get the horizontal resolution of the Lidar sensor.
This method is deprecated as of Isaac Sim 5.0. Use the horizontal_resolution attribute in the current frame instead.
Returns:
The horizontal resolution value if available, None otherwise.

Return type:
Optional[float]

get_local_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the local frame (the prim’s parent frame)
Returns:
first index is the position in the local frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the local frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_local_pose()
>>> position
[0. 0. 0.]
>>> orientation
[0. 0. 0.]
```

get_local_scale()→ndarray
Get prim’s scale with respect to the local frame (the parent’s frame)
Returns:
scale applied to the prim’s dimensions in the local frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_local_scale()
[1. 1. 1.]
```

get_num_cols()→int
Get the number of columns in the Lidar scan.
This method is deprecated as of Isaac Sim 5.0. Use the num_cols attribute in the current frame instead.
Returns:
The number of columns if available, None otherwise.

Return type:
Optional[int]

get_num_rows()→int
Get the number of rows in the Lidar scan.
This method is deprecated as of Isaac Sim 5.0. Use the num_rows attribute in the current frame instead.
Returns:
The number of rows if available, None otherwise.

Return type:
Optional[int]

staticget_object_ids(obj_ids:ndarray)→List[int]
Get Object IDs from the GenericModelOutput object ID buffer. The buffer is an array of dtype uint8 that must be converted to a list of dtype uint128 (stride 16). Each uint128 is a unique stable ID for a prim in the scene, which can be used to look up the prim path in the map provided by the StableIdMap annotator (see above).
Parameters:
obj_ids (np.ndarray) – The GenericModelOutput object ID buffer.

Returns:
The object IDs as a list of uint128.

Return type:
List[int]

get_render_product_path()→str
Get the path to the render product used by the Lidar.
Returns:
Path to the render product.

Return type:
str

get_rotation_frequency()→float
Get the rotation frequency of the Lidar sensor.
This method is deprecated as of Isaac Sim 5.0. Use the rotation_frequency attribute in the current frame instead.
Returns:
The rotation frequency value if available, None otherwise.

Return type:
Optional[float]

get_visibility()→bool
Returns:
true if the prim is visible in stage. false otherwise.

Return type:
bool

Example:

```
>>> # get the visible state of an visible prim on the stage
>>> prim.get_visibility()
True
```

get_world_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the world’s frame
Returns:
first index is the position in the world frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the world frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
>>> position, orientation = prim.get_world_pose()
>>> position
[1. 0.5 0. ]
>>> orientation
[1. 0. 0. 0.]
```

get_world_scale()→ndarray
Get prim’s scale with respect to the world’s frame
Returns:
scale applied to the prim’s dimensions in the world frame. shape is (3, ).

Return type:
np.ndarray

Example:

```
>>> prim.get_world_scale()
[1. 1. 1.]
```

get_writers()→dict
Get all attached writers.
Returns:
Dictionary mapping writer names to their instances.

Return type:
dict

initialize(physics_sim_view=None)→None
Initialize the Lidar sensor.
Parameters:
physics_sim_view (param) – Optional physics simulation view.

is_paused()→bool
Check if the Lidar sensor is paused.
Returns:
True if the sensor is paused, False otherwise.

is_valid()→bool
Check if the prim path has a valid USD Prim at it
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> # given an existing and valid prim
>>> prims.is_valid()
True
```

is_visual_material_applied()→bool
Check if there is a visual material applied
Returns:
True if there is a visual material applied. False otherwise.

Return type:
bool

Example:

```
>>> # given a visual material applied
>>> prim.is_visual_material_applied()
True
```

staticmake_add_remove_deprecated_attr(deprecated_attr:str)
Creates deprecated add/remove attribute methods.
Parameters:
deprecated_attr (param) – Name of the deprecated attribute to create methods for.

Returns:
List of method functions for adding and removing the deprecated attribute.

Return type:
list

pause()→None
Pause data acquisition for the Lidar sensor.

post_reset()→None
Perform post-reset operations for the Lidar sensor.

remove_azimuth_data_to_frame()
Remove azimuth data from the current frame.
This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.

remove_azimuth_range_to_frame()
Remove azimuth range data from the current frame.
This method is deprecated as of Isaac Sim 5.0. Use detach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

remove_elevation_data_to_frame()
Remove elevation data from the current frame.
This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.

remove_horizontal_resolution_to_frame()
Remove horizontal resolution data from the current frame.
This method is deprecated as of Isaac Sim 5.0. Use detach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

remove_intensities_data_to_frame()
Remove intensities data from the current frame.
This method is deprecated as of Isaac Sim 5.0. Use detach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

remove_linear_depth_data_to_frame()
Remove linear depth data from the current frame.
This method is deprecated as of Isaac Sim 5.0. Use detach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

remove_point_cloud_data_to_frame()
Remove point cloud data from the current frame.
This method is deprecated as of Isaac Sim 5.0. Use detach_annotator(‘IsaacComputeRTXLidarFlatScan’) instead.

remove_range_data_to_frame()
Remove range data from the current frame.
This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.

resume()→None
Resume data acquisition for the Lidar sensor.

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set the default state of the prim (position and orientation), that will be used after each reset.
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Example:

```
>>> # configure default state
>>> prim.set_default_state(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1, 0, 0, 0]))
>>>
>>> # set default states during post-reset
>>> prim.post_reset()
```

set_local_pose(
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Set prim’s pose with respect to the local frame (the prim’s parent frame).
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the local frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_local_pose(translation=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

set_local_scale(
scale:Sequence[float]|None ,
)→None Set prim’s scale with respect to the local frame (the prim’s parent frame).
Parameters:
scale (Optional[Sequence[float]]) – scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

Example:

```
>>> # scale prim 10 times smaller
>>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
```

set_visibility(visible:bool)→None
Set the visibility of the prim in stage
Parameters:
visible (bool) – flag to set the visibility of the usd prim in stage.

Example:

```
>>> # make prim not visible in the stage
>>> prim.set_visibility(visible=False)
```

set_world_pose(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Ses prim’s pose with respect to the world’s frame
Warning
This method will change (teleport) the prim pose immediately to the indicated value
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> prim.set_world_pose(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
```

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertynon_root_articulation_link:bool
Used to query if the prim is a non root articulation link
Returns:
True if the prim itself is a non root link

Return type:
bool

Example:

```
>>> # for a wrapped articulation (where the root prim has the Physics Articulation Root property applied)
>>> prim.non_root_articulation_link
False
```

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: USD Prim object that this object holds.

propertyprim_path:str
Returns: str: prim path in the stage

## Omnigraph Nodes
The extension exposes the following Omnigraph nodes:

## Settings

### Other Settings
The extension changes some settings of the application or other extensions, which are listed in the table below.

[TABLE]
Application/extension setting | Description | Value
app.sensors.nv.lidar.profileBaseFolder | List of directories which renderer will search to find Lidar profile for (deprecated) camera-based Lidar | ['${omni.sensors.nv.common}/data/lidar/', '${isaacsim.sensors.rtx}/data/lidar_configs/HESAI/', '${isaacsim.sensors.rtx}/data/lidar_configs/NVIDIA/', '${isaacsim.sensors.rtx}/data/lidar_configs/Ouster/OS0/', '${isaacsim.sensors.rtx}/data/lidar_configs/Ouster/OS1/', '${isaacsim.sensors.rtx}/data/lidar_configs/Ouster/OS2/', '${isaacsim.sensors.rtx}/data/lidar_configs/SICK/', '${isaacsim.sensors.rtx}/data/lidar_configs/SLAMTEC/', '${isaacsim.sensors.rtx}/data/lidar_configs/Velodyne/', '${isaacsim.sensors.rtx}/data/lidar_configs/ZVISION/', '${isaacsim.sensors.rtx}/data/lidar_configs/']
app.sensors.nv.lidar.outputBufferOnGPU | Renderer keeps Lidar return buffer on GPU for post-processing. | True
app.sensors.nv.radar.outputBufferOnGPU | Renderer keeps Radar return buffer on GPU for post-processing. | True
rtx.materialDb.nonVisualMaterialCSV.enabled | Enable non-visual materials using USD attributes | False
rtx.materialDb.nonVisualMaterialSemantics.prefix | Specify non-visual material USD attribute prefix | 'omni:simready:nonvisual'
[/TABLE]
