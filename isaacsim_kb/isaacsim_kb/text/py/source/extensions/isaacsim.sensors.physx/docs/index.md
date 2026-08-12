<!-- source: py/source/extensions/isaacsim.sensors.physx/docs/index.html | title: [isaacsim.sensors.physx] Isaac Sim PhysX Sensors — Isaac Sim -->

# [isaacsim.sensors.physx] Isaac Sim PhysX Sensors
Version: 2.3.2
Isaac Sim PhysX Sensors extension provides APIs for PhysX-raycast-based lidars and sensors including Proximity Sensor and Lightbeam Sensor.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API
Commands

[TABLE]
RangeSensorCreatePrim | Base command for creating range sensor prims.
RangeSensorCreateLidar | Command class to create a lidar sensor.
RangeSensorCreateGeneric | Command class to create a generic range sensor.
IsaacSensorCreateLightBeamSensor | Command class to create a light beam sensor.
[/TABLE]
Sensors

[TABLE]
ProximitySensor |
RotatingLidarPhysX |
[/TABLE]

#### Commands
classRangeSensorCreatePrim(*args:Any, **kwargs:Any)
Bases: `Command`
Base command for creating range sensor prims.
This command is used to create each range sensor prim and handles undo operations so that individual prim commands don’t have to implement their own undo logic.
Parameters:

- path – Path for the new prim.

- parent – Parent prim path.

- schema_type – Schema type to use for the prim.

- translation – Translation vector for the prim.

- orientation – Orientation quaternion for the prim.

- visibility – Whether the prim is visible.

- min_range – Minimum range of the sensor.

- max_range – Maximum range of the sensor.

- draw_points – Whether to draw points for visualization.

- draw_lines – Whether to draw lines for visualization.

classRangeSensorCreateLidar(*args:Any, **kwargs:Any)
Bases: `Command`
Command class to create a lidar sensor.
Typical usage example:

```
result, prim = omni.kit.commands.execute(
"RangeSensorCreateLidar",
path="/Lidar",
parent=None,
translation=Gf.Vec3d(0, 0, 0),
orientation=Gf.Quatd(1, 0, 0, 0),
min_range=0.4,
max_range=100.0,
draw_points=False,
draw_lines=False,
horizontal_fov=360.0,
vertical_fov=30.0,
horizontal_resolution=0.4,
vertical_resolution=4.0,
rotation_rate=20.0,
high_lod=False,
yaw_offset=0.0,
enable_semantics=False,
)
```

classRangeSensorCreateGeneric(*args:Any, **kwargs:Any)
Bases: `Command`
Command class to create a generic range sensor.
Typical usage example:

```
result, prim = omni.kit.commands.execute(
"RangeSensorCreateGeneric",
path="/GenericSensor",
parent=None,
translation=Gf.Vec3d(0, 0, 0),
orientation=Gf.Quatd(1, 0, 0, 0),
min_range=0.4,
max_range=100.0,
draw_points=False,
draw_lines=False,
sampling_rate=60,
)
```

classIsaacSensorCreateLightBeamSensor(*args:Any, **kwargs:Any)
Bases: `Command`
Command class to create a light beam sensor.
Parameters:

- path – Path for the new prim.

- parent – Parent prim path.

- translation – Translation vector for the prim.

- orientation – Orientation quaternion for the prim.

- num_rays – Number of rays for the light beam sensor.

- curtain_length – Length of the curtain for multi-ray sensors.

- forward_axis – Forward direction axis.

- curtain_axis – Curtain direction axis.

- min_range – Minimum range of the sensor.

- max_range – Maximum range of the sensor.

- draw_points – Whether to draw points for visualization.

- draw_lines – Whether to draw lines for visualization.

- **kwargs – Additional keyword arguments.

#### Sensors
classProximitySensor(
parent:pxr.Usd.Prim,
callback_fns=[None,None,None],
exclusions=[],
)Bases: `object`
check_for_overlap()
get_active_zones()→List[str]
Returns a list of the prim paths of all the collision meshes the tracker is inside of.
Returns:
prim paths as strings

Return type:
list(str)

get_data()→Dict[str,Dict[str,float]]
Returns dictionary of overlapped geometry and respective metadata.
key: prim_path of overlapped geometry val: dictionary of metadata:
“duration”: float of time since overlap “distance”: distance from origin of tracker to origin of overlapped geometry

Returns:
overlapped geometry and metadata

Return type:
Dict[str, Dict[str, float]]

get_entered_zones()→List[str]
Returns a list of the prim paths of all the collision meshes the tracker just entered.
Returns:
prim paths as strings

Return type:
list(str)

get_exited_zones()→List[str]
Returns a list of the prim paths of all the collision meshes the tracker just exited.
Returns:
prim paths as strings

Return type:
list(str)

is_overlapping()
report_hit(hit)
reset()
status()
to_string()
update()

classRotatingLidarPhysX(
prim_path:str,
name:str='rotating_lidar_physX',
rotation_frequency:float|None =None,
rotation_dt:float|None =None,
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
fov:Tuple[float,float]|None =None,
resolution:Tuple[float,float]|None =None,
valid_range:Tuple[float,float]|None =None,
)Bases: BaseSensor
add_azimuth_data_to_frame()→None
add_depth_data_to_frame()→None
add_intensity_data_to_frame()→None
add_linear_depth_data_to_frame()→None
add_point_cloud_data_to_frame()→None
add_semantics_data_to_frame()→None
add_zenith_data_to_frame()→None
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

disable_semantics()→None
disable_visualization()→None
enable_semantics()→None
enable_visualization(
high_lod:bool=False,
draw_points:bool=True,
draw_lines:bool=True,
)→None get_applied_visual_material()→VisualMaterial
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

get_current_frame()→dict
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

get_fov()→Tuple[float,float]
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
get_num_cols_in_last_step()→int
get_num_rows()→int
get_resolution()→float
get_rotation_frequency()→int
get_valid_range()→Tuple[float,float]
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

initialize(physics_sim_view=None)→None
Create a physics simulation view if not passed and using PhysX tensor API
Note
If the prim has been added to the world scene (e.g., `world.scene.add(prim)`), it will be automatically initialized when the world is reset (e.g., `world.reset()`).
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

Example:

```
>>> prim.initialize()
```

is_paused()→bool
is_semantics_enabled()→bool
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

pause()→None
post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

remove_azimuth_data_from_frame()→None
remove_depth_data_from_frame()→None
remove_intensity_data_from_frame()→None
remove_linear_depth_data_from_frame()→None
remove_point_cloud_data_from_frame()→None
remove_semantics_data_from_frame()→None
remove_zenith_data_from_frame()→None
resume()→None
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

set_fov(value:Tuple[float,float])→None
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

set_resolution(value:float)→None
set_rotation_frequency(value:int)→None
set_valid_range(
value:Tuple[float,float],
)→None set_visibility(visible:bool)→None
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
