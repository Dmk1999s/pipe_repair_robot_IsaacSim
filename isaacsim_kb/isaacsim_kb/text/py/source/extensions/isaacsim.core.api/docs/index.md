<!-- source: py/source/extensions/isaacsim.core.api/docs/index.html | title: [isaacsim.core.api] Isaac Sim Core — Isaac Sim -->

# [isaacsim.core.api] Isaac Sim Core
Version: 4.8.0
The Core extension provides a set of APIs to control the Simulation State as well as the physics scene. It also provides wrappers for USD objects, physics and visual materials.

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API

### Python API
controllers

[TABLE]
ArticulationController | PD Controller of all degrees of freedom of an articulation, can apply position targets, velocity targets and efforts.
BaseController | [summary]
BaseGripperController | [summary]
[/TABLE]
loggers

[TABLE]
DataLogger | This class takes care of collecting data as well as reading already saved data in order to replay it for instance.
[/TABLE]
materials

[TABLE]
VisualMaterial | [summary]
PreviewSurface | [summary]
OmniPBR | [summary]
OmniGlass | [summary]
PhysicsMaterial | [summary]
ParticleMaterial | A wrapper around position-based-dynamics (PBD) material for particles used to simulate fluids, cloth and inflatables.
ParticleMaterialView | The view class to deal with particleMaterial prims.
DeformableMaterial | A wrapper around deformable material used to simulate soft bodies.
DeformableMaterialView | The view class to deal with deformableMaterial prims.
[/TABLE]
objects

[TABLE]
GroundPlane | High level wrapper to create/encapsulate a ground plane
VisualCapsule | High level wrapper to create/encapsulate a visual capsule
VisualCone | High level wrapper to create/encapsulate a visual cone
VisualCuboid | High level wrapper to create/encapsulate a visual cuboid
VisualCylinder | High level wrapper to create/encapsulate a visual cylinder
VisualSphere | High level wrapper to create/encapsulate a visual sphere
FixedCapsule | High level wrapper to create/encapsulate a fixed capsule
FixedCone | High level wrapper to create/encapsulate a fixed cone
FixedCuboid | High level wrapper to create/encapsulate a fixed cuboid
FixedCylinder | High level wrapper to create/encapsulate a fixed cylinder
FixedSphere | High level wrapper to create/encapsulate a fixed sphere
DynamicCapsule | High level wrapper to create/encapsulate a dynamic capsule
DynamicCone | High level wrapper to create/encapsulate a dynamic cone
DynamicCuboid | High level wrapper to create/encapsulate a dynamic cuboid
DynamicCylinder | High level wrapper to create/encapsulate a dynamic cylinder
DynamicSphere | High level wrapper to create/encapsulate a dynamic sphere
[/TABLE]
physics_context

[TABLE]
PhysicsContext | Provides high level functions to deal with a physics scene and its settings. This will create a
[/TABLE]
robots

[TABLE]
Robot | Implementation (on SingleArticulation class) to deal with an articulation prim as a robot
RobotView | Implementation (on Articulation class) to deal with articulation prims as robots
[/TABLE]
scenes

[TABLE]
Scene | Provide methods to add objects of interest in the stage to retrieve their information and set their reset default state in an easy way
SceneRegistry | Class to keep track of the different types of objects added to the scene
[/TABLE]
sensors

[TABLE]
BaseSensor | Provides a common properties and methods to deal with prims as a sensor
RigidContactView | Provides high level functions to deal with rigid prims (one or many) that track their contacts through filters as well as their attributes/properties.
[/TABLE]
simulation_context

[TABLE]
SimulationContext | This class provide functions that take care of many time-related events such as perform a physics or a render step for instance.
[/TABLE]
world

[TABLE]
World | This class inherits from SimulationContext which provides the following.
[/TABLE]
tasks

[TABLE]
BaseTask | This class provides a way to set up a task in a scene and modularize adding objects to stage, getting observations needed for the behavioral layer, calculating metrics needed about the task, calling certain things pre-stepping, creating multiple tasks at the same time and much more.
FollowTarget | [summary]
PickPlace | [summary]
Stacking | [summary]
[/TABLE]

#### Controllers
classArticulationController
Bases: `object`
PD Controller of all degrees of freedom of an articulation, can apply position targets, velocity targets and efforts.
Checkout the required tutorials at https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
apply_action(
control_actions:ArticulationAction ,
)→None [summary]
Parameters:

- control_actions (ArticulationAction ) – actions to be applied for next physics step.

- indices (Optional[Union[list, np.ndarray]], optional) – degree of freedom indices to apply actions to. Defaults to all degrees of freedom.

Raises:
Exception – [description]

get_applied_action()→ArticulationAction
Raises:
Exception – [description]

Returns:
Gets last applied action.

Return type:
ArticulationAction

get_effort_modes()→List[str]
[summary]
Raises:

- Exception – [description]

- NotImplementedError – [description]

Returns:
[description]

Return type:
np.ndarray

get_gains()→Tuple[ndarray,ndarray]
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
Tuple[np.ndarray, np.ndarray]

get_joint_limits()→Tuple[ndarray,ndarray]
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
Tuple[np.ndarray, np.ndarray]

get_max_efforts()→ndarray
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
np.ndarray

initialize(articulation_view)→None
[summary]
Parameters:
articulation_view ([type]) – [description]

set_effort_modes(
mode:str,
joint_indices:ndarray|list|None =None,
)→None [summary]
Parameters:

- mode (str) – [description]

- indices (Optional[Union[np.ndarray, list]], optional) – [description]. Defaults to None.

Raises:

- Exception – [description]

- Exception – [description]

set_gains(
kps:ndarray|None =None,
kds:ndarray|None =None,
save_to_usd:bool=False,
)→None [summary]
Parameters:

- kps (Optional[np.ndarray], optional) – [description]. Defaults to None.

- kds (Optional[np.ndarray], optional) – [description]. Defaults to None.

Raises:
Exception – [description]

set_max_efforts(
values:ndarray,
joint_indices:ndarray|list|None =None,
)→None [summary]
Parameters:

- value (float, optional) – [description]. Defaults to None.

- indices (Optional[Union[np.ndarray, list]], optional) – [description]. Defaults to None.

Raises:
Exception – [description]

switch_control_mode(mode:str)→None
[summary]
Parameters:
mode (str) – [description]

Raises:
Exception – [description]

switch_dof_control_mode(
dof_index:int,
mode:str,
)→None [summary]
Parameters:

- dof_index (int) – [description]

- mode (str) – [description]

Raises:
Exception – [description]

classBaseController(name:str)
Bases: `ABC`
[summary]
Parameters:
name (str) – [description]

abstractforward(
*args,
**kwargs,
)→ArticulationAction A controller should take inputs and returns an ArticulationAction to be then passed to the
ArticulationController.

Parameters:
observations (dict) – [description]

Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
ArticulationAction

reset()→None
Resets state of the controller.

classBaseGripperController(name:str)
Bases: BaseController
[summary]
Parameters:
name (str) – [description]

abstractclose(
current_joint_positions:ndarray,
)→ArticulationAction [summary]
Parameters:
current_joint_positions (np.ndarray) – [description]

Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
ArticulationAction

forward(
action:str,
current_joint_positions:ndarray,
)→ArticulationAction Action has be “open” or “close”
Parameters:

- action (str) – “open” or “close”

- current_joint_positions (np.ndarray) – [description]

Raises:
Exception – [description]

Returns:
[description]

Return type:
ArticulationAction

abstractopen(
current_joint_positions:ndarray,
)→ArticulationAction [summary]
Parameters:
current_joint_positions (np.ndarray) – [description]

Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
ArticulationAction

reset()→None
[summary]

#### Loggers
classDataLogger
Bases: `object`
This class takes care of collecting data as well as reading already saved data in order to replay it for instance.
add_data(
data:dict,
current_time_step:float,
current_time:float,
)→None Adds data to the log
Parameters:

- data (dict) – Dictionary representing the data to be logged at this time index.

- current_time_step (float) – time step corresponding to the data collected.

- current_time (float) – time in seconds corresponding to the data collected.

add_data_frame_logging_func(
func:Callable[[List[BaseTask ],Scene ],Dict],
)→None Parameters:
func (Callable[[list[BaseTask ], Scene ], None]) –
function to be called at every step when the logger is started. should follow:
def dummy_data_collection_fn(tasks, scene):
return {“data 1”: [data]}

get_data_frame(
data_frame_index:int,
)→DataFrame Parameters:
data_frame_index (int) – index of the data frame to retrieve.

Returns:
Data Frame collected/ retrieved at the specified data frame index.

Return type:
DataFrame

get_num_of_data_frames()→int
Returns:
the number of data frames collected/ retrieved in the data logger.

Return type:
int

is_started()→bool
Returns:
True if data collection is started/ resumed. False otherwise.

Return type:
bool

load(log_path:str)→None
Loads data from a json file to read back a previous saved data or to resume recording data from another time step.
Parameters:
log_path (str) – path of the json file to be used to load the data.

pause()→None
Pauses data collection.

reset()→None
Clears the data in the logger.

save(log_path:str)→None
Saves the current data in the logger to a json file
Parameters:
log_path (str) – path of the json file to be used to save the data.

start()→None
Resumes/ starts data collection.

#### Materials
classVisualMaterial(
name:str,
prim_path:str,
prim:pxr.Usd.Prim,
shaders_list:List[pxr.UsdShade.Shader],
material:pxr.UsdShade.Material,
)Bases: `object`
[summary]
Parameters:

- name (str) – [description]

- prim_path (str) – [description]

- prim (Usd.Prim) – [description]

- shaders_list (list[UsdShade.Shader]) – [description]

- material (UsdShade.Material) – [description]

propertymaterial:pxr.UsdShade.Material
[summary]
Returns:
[description]

Return type:
UsdShade.Material

propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyprim:pxr.Usd.Prim
[summary]
Returns:
[description]

Return type:
Usd.Prim

propertyprim_path:str
[summary]
Returns:
[description]

Return type:
str

propertyshaders_list:List[pxr.UsdShade.Shader]
[summary]
Returns:
[description]

Return type:
[type]

classPreviewSurface(
prim_path:str,
name:str='preview_surface',
shader:pxr.UsdShade.Shader|None =None,
color:ndarray|None =None,
roughness:float|None =None,
metallic:float|None =None,
)Bases: VisualMaterial
[summary]
Parameters:

- prim_path (str) – [description]

- name (str, optional) – [description]. Defaults to “preview_surface”.

- shader (Optional[UsdShade.Shader], optional) – [description]. Defaults to None.

- color (Optional[np.ndarray], optional) – [description]. Defaults to None.

- roughness (Optional[float], optional) – [description]. Defaults to None.

- metallic (Optional[float], optional) – [description]. Defaults to None.

get_color()→ndarray
[summary]
Returns:
[description]

Return type:
np.ndarray

get_metallic()→float
[summary]
Returns:
[description]

Return type:
float

get_roughness()→float
[summary]
Returns:
[description]

Return type:
float

set_color(color:ndarray)→None
[summary]
Parameters:
color (np.ndarray) – [description]

set_metallic(metallic:float)→None
[summary]
Parameters:
metallic (float) – [description]

set_roughness(roughness:float)→None
[summary]
Parameters:
roughness (float) – [description]

propertymaterial:pxr.UsdShade.Material
[summary]
Returns:
[description]

Return type:
UsdShade.Material

propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyprim:pxr.Usd.Prim
[summary]
Returns:
[description]

Return type:
Usd.Prim

propertyprim_path:str
[summary]
Returns:
[description]

Return type:
str

propertyshaders_list:List[pxr.UsdShade.Shader]
[summary]
Returns:
[description]

Return type:
[type]

classOmniPBR(
prim_path:str,
name:str='omni_pbr',
shader:pxr.UsdShade.Shader|None =None,
texture_path:str|None =None,
texture_scale:ndarray|None =None,
texture_translate:ndarray|None =None,
color:ndarray|None =None,
)Bases: VisualMaterial
[summary]
Parameters:

- prim_path (str) – [description]

- name (str, optional) – [description]. Defaults to “omni_pbr”.

- shader (Optional[UsdShade.Shader], optional) – [description]. Defaults to None.

- texture_path (Optional[str], optional) – [description]. Defaults to None.

- texture_scale (Optional[np.ndarray], optional) – [description]. Defaults to None.

- texture_translate (Optional[np.ndarray, optional) – [description]. Defaults to None.

- color (Optional[np.ndarray], optional) – [description]. Defaults to None.

get_color()→ndarray
[summary]
Returns:
[description]

Return type:
np.ndarray

get_metallic_constant()→float
[summary]
Returns:
[description]

Return type:
float

get_project_uvw()→bool
[summary]
Returns:
[description]

Return type:
bool

get_reflection_roughness()→float
[summary]
Returns:
[description]

Return type:
float

get_texture()→str
[summary]
Returns:
[description]

Return type:
str

get_texture_scale()→ndarray
[summary]
Returns:
[description]

Return type:
np.ndarray

get_texture_translate()→ndarray
[summary]
Returns:
[description]

Return type:
np.ndarray

set_color(color:ndarray)→None
[summary]
Parameters:
color (np.ndarray) – [description]

set_metallic_constant(amount:float)→None
[summary]
Parameters:
amount (float) – [description]

set_project_uvw(flag:bool)→None
[summary]
Parameters:
flag (bool) – [description]

set_reflection_roughness(amount:float)→None
[summary]
Parameters:
amount (float) – [description]

set_texture(path:str)→None
[summary]
Parameters:
path (str) – [description]

set_texture_scale(x:float, y:float)→None
[summary]
Parameters:

- x (float) – [description]

- y (float) – [description]

set_texture_translate(x:float, y:float)→None
[summary]
Parameters:

- x (float) – [description]

- y (float) – [description]

propertymaterial:pxr.UsdShade.Material
[summary]
Returns:
[description]

Return type:
UsdShade.Material

propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyprim:pxr.Usd.Prim
[summary]
Returns:
[description]

Return type:
Usd.Prim

propertyprim_path:str
[summary]
Returns:
[description]

Return type:
str

propertyshaders_list:List[pxr.UsdShade.Shader]
[summary]
Returns:
[description]

Return type:
[type]

classOmniGlass(
prim_path:str,
name:str='omni_glass',
shader:pxr.UsdShade.Shader|None =None,
color:ndarray|None =None,
ior:float|None =None,
depth:float|None =None,
thin_walled:bool|None =None,
)Bases: VisualMaterial
[summary]
Parameters:

- prim_path (str) – [description]

- name (str, optional) – [description]. Defaults to “omni_glass”.

- shader (Optional[UsdShade.Shader], optional) – [description]. Defaults to None.

- color (Optional[np.ndarray], optional) – [description]. Defaults to None.

- ior (Optional[float], optional) – [description]. Defaults to None.

- depth (Optional[float], optional) – [description]. Defaults to None.

- thin_walled (Optional[bool], optional) – [description]. Defaults to None.

Raises:
Exception – [description]

get_color()→ndarray|None
[summary]
Returns:
[description]

Return type:
np.ndarray

get_depth()→float|None
get_ior()→float|None
get_thin_walled()→float|None
set_color(color:ndarray)→None
[summary]
Parameters:
color (np.ndarray) – [description]

set_depth(depth:float)→None
set_ior(ior:float)→None
set_thin_walled(thin_walled:float)→None
propertymaterial:pxr.UsdShade.Material
[summary]
Returns:
[description]

Return type:
UsdShade.Material

propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyprim:pxr.Usd.Prim
[summary]
Returns:
[description]

Return type:
Usd.Prim

propertyprim_path:str
[summary]
Returns:
[description]

Return type:
str

propertyshaders_list:List[pxr.UsdShade.Shader]
[summary]
Returns:
[description]

Return type:
[type]

classPhysicsMaterial(
prim_path:str,
name:str='physics_material',
static_friction:float|None =None,
dynamic_friction:float|None =None,
restitution:float|None =None,
)Bases: `object`
[summary]
Parameters:

- prim_path (str) – [description]

- name (str, optional) – [description]. Defaults to “physics_material”.

- static_friction (Optional[float], optional) – [description]. Defaults to None.

- dynamic_friction (Optional[float], optional) – [description]. Defaults to None.

- restitution (Optional[float], optional) – [description]. Defaults to None.

get_dynamic_friction()→float
[summary]
Returns:
[description]

Return type:
float

get_restitution()→float
[summary]
Returns:
[description]

Return type:
float

get_static_friction()→float
[summary]
Returns:
[description]

Return type:
float

set_dynamic_friction(friction:float)→None
[summary]
Parameters:
friction (float) – [description]

set_restitution(restitution:float)→None
[summary]
Parameters:
restitution (float) – [description]

set_static_friction(friction:float)→None
[summary]
Parameters:
friction (float) – [description]

propertymaterial:pxr.UsdShade.Material
[summary]
Returns:
[description]

Return type:
UsdShade.Material

propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyprim:pxr.Usd.Prim
[summary]
Returns:
[description]

Return type:
Usd.Prim

propertyprim_path:str
[summary]
Returns:
[description]

Return type:
str

classParticleMaterial(
prim_path:str,
name:str|None ='particle_material',
friction:float|None =None,
particle_friction_scale:float|None =None,
damping:float|None =None,
viscosity:float|None =None,
vorticity_confinement:float|None =None,
surface_tension:float|None =None,
cohesion:float|None =None,
adhesion:float|None =None,
particle_adhesion_scale:float|None =None,
adhesion_offset_scale:float|None =None,
gravity_scale:float|None =None,
lift:float|None =None,
drag:float|None =None,
)Bases: `object`
A wrapper around position-based-dynamics (PBD) material for particles used to simulate fluids, cloth and inflatables.
Note
Currently, only a single material per particle system is supported which applies to all objects that are associated with the system.
get_adhesion()→float
Returns:
The adhesion for interaction between particles (solid or fluid), and rigids or deformables.

Return type:
float

get_adhesion_offset_scale()→float
Returns:
The adhesion offset scale.

Return type:
float

get_cohesion()→float
Returns:
The cohesion for interaction between fluid particles.

Return type:
float

get_damping()→float
Returns:
The global velocity damping coefficient.

Return type:
float

get_drag()→float
Returns:
The drag coefficient, basic aerodynamic drag model coefficient.

Return type:
float

get_friction()→float
Returns:
The friction coefficient.

Return type:
float

get_gravity_scale()→float
Returns:
The gravitational acceleration scaling factor.

Return type:
float

get_lift()→float
Returns:
The lift coefficient, basic aerodynamic lift model coefficient.

Return type:
float

get_particle_adhesion_scale()→float
Returns:
The particle adhesion scale.

Return type:
float

get_particle_friction_scale()→float
Returns:
The particle friction scale.

Return type:
float

get_surface_tension()→float
Returns:
The surface tension for fluid particles.

Return type:
float

get_viscosity()→float
Returns:
The viscosity.

Return type:
float

get_vorticity_confinement()→float
Returns:
The vorticity confinement for fluid particles.

Return type:
float

initialize(physics_sim_view=None)→None
is_valid()→bool
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

post_reset()→None
Resets the prim to its default state.

set_adhesion(value:float)→None
Sets the adhesion for interaction between particles (solid or fluid), and rigid or deformable objects.
Note
Adhesion also applies to solid-solid particle interactions, but is multiplied with the particle adhesion scale.
Parameters:
value (float) – The adhesion. Range: [0, inf), Units: dimensionless

set_adhesion_offset_scale(value:float)→None
Sets the adhesion offset scale.
It defines the offset at which adhesion ceases to take effect. For interactions between particles (fluid or solid), and rigids or deformables, the adhesion offset is defined relative to the rest offset. For solid particle-particle interactions, the adhesion offset is defined relative to the solid rest offset.
Parameters:
value (float) – The adhesion offset scale. Range: [0, inf), Units: dimensionless

set_cohesion(value:float)→None
Sets the cohesion for interaction between fluid particles.
Parameters:
value (float) – The cohesion. Range: [0, inf), Units: dimensionless

set_damping(value:float)→None
Sets the global velocity damping coefficient.
Parameters:
value (float) – The damping coefficient. Range: [0, inf), Units: dimensionless

set_drag(value:float)→None
Sets the drag coefficient, i.e. basic aerodynamic drag model coefficient.
It is useful for cloth and inflatable particle objects.
Parameters:
value (float) – The drag coefficient. Range: [0, inf), Units: dimensionless

set_friction(value:float)→None
Sets the friction coefficient.
The friction takes effect in all interactions between particles and rigids or deformables. For solid particle-particle interactions it is multiplied by the particle friction scale.
Parameters:
value (float) – The friction coefficient. Range: [0, inf), Units: dimensionless

set_gravity_scale(value:float)→None
Sets the gravitational acceleration scaling factor.
It can be used to approximate lighter-than-air inflatable. For example (-1.0 would invert gravity).
Parameters:
value (float) – The gravity scale. Range: (-inf , inf), Units: dimensionless

set_lift(value:float)→None
Sets the lift coefficient, i.e. basic aerodynamic lift model coefficient.
It is useful for cloth and inflatable particle objects.
Parameters:
value (float) – The lift coefficient. Range: [0, inf), Units: dimensionless

set_particle_adhesion_scale(value:float)→None
Sets the particle adhesion scale.
This coefficient scales the adhesion for solid particle-particle interaction.
Parameters:
value (float) – The adhesion scale. Range: [0, inf), Units: dimensionless

set_particle_friction_scale(value:float)→None
Sets the particle friction scale.
The coefficient that scales friction for solid particle-particle interaction.
Parameters:
value (float) – The particle friction scale. Range: [0, inf), Units: dimensionless

set_surface_tension(value:float)→None
Sets the surface tension for fluid particles.
Parameters:
value (float) – The surface tension. Range: [0, inf), Units: 1 / (distance * distance * distance)

set_viscosity(value:float)→None
Sets the viscosity for fluid particles.
Parameters:
value (float) – The viscosity. Range: [0, inf), Units: dimensionless

set_vorticity_confinement(value:float)→None
Sets the vorticity confinement for fluid particles.
This helps prevent energy loss due to numerical solver by adding vortex-like accelerations to the particles.
Parameters:
value (float) – The vorticity confinement. Range: [0, inf), Units: dimensionless

propertymaterial:pxr.UsdShade.Material
Returns: UsdShade.Material: The USD Material object.

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: The USD prim present.

propertyprim_path:str
Returns: str: The stage path to the material.

classParticleMaterialView(
prim_paths_expr:str,
name:str='particle_material_view',
frictions:ndarray|Tensor|None =None,
particle_friction_scales:ndarray|Tensor|None =None,
dampings:ndarray|Tensor|None =None,
viscosities:ndarray|Tensor|None =None,
vorticity_confinements:ndarray|Tensor|None =None,
surface_tensions:ndarray|Tensor|None =None,
cohesions:ndarray|Tensor|None =None,
adhesions:ndarray|Tensor|None =None,
particle_adhesion_scales:ndarray|Tensor|None =None,
adhesion_offset_scales:ndarray|Tensor|None =None,
gravity_scales:ndarray|Tensor|None =None,
lifts:ndarray|Tensor|None =None,
drags:ndarray|Tensor|None =None,
)Bases: `object`
The view class to deal with particleMaterial prims. Provides high level functions to deal with particle material (1 or more particle materials) as well as its attributes/ properties. This object wraps all matching materials found at the regex provided at the prim_paths_expr. This object wraps all matching materials Prims found at the regex provided at the prim_paths_expr.
get_adhesion_offset_scales(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the adhesion offset scale of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
adhesion offset scale tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_adhesions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the adhesion of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
adhesion tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_cohesions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the cohesion of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
cohesion tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_dampings(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the dampings of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
dampings tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_drags(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the drags of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
drag tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_frictions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the friction of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
friction tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_gravity_scales(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the gravity scale of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
gravity scale tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_lifts(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the lifts of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
lift tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_particle_adhesion_scales(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the adhesion scale of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
adhesion scale tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_particle_friction_scales(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the particle friction scale of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
particle friction scale tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_surface_tensions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the surface tension of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
surface tension tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_viscosities(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the viscosity of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
viscosity tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_vorticity_confinements(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the vorticity confinement of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
vorticity confinement tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and creates a rigid body view in physX.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_physics_handle_valid()→bool
Returns:
True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.

Return type:
bool

is_valid(
indices:ndarray|list|Tensor|None =None,
)→boolParameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
True if all prim paths specified in the view correspond to a valid prim in stage. False otherwise.

Return type:
bool

post_reset()→None
Resets the particles to their initial states.

set_adhesion_offset_scales(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the adhesion offset scale for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material adhesion offset scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_adhesions(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle adhesion for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle adhesion scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_cohesions(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle cohesion for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle cohesion scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_dampings(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the dampings for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material damping tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_drags(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the drags for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material drag tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_frictions(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the friction for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material friction tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_gravity_scales(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the gravity scale for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material gravity scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_lifts(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the lifts for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material lift tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_particle_adhesion_scales(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle adhesion for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle adhesion scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_particle_friction_scales(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle friction scale for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle friction scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_surface_tensions(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle surface tension for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle surface tension scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_viscosities(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle viscosity for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle viscosity scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_vorticity_confinements(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the vorticity confinement for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material particle vorticity confinement scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

propertycount:int
Returns: int: number of rigid shapes for the prims in the view.

propertyname:str
Returns: str: name given to the view when instantiating it.

classDeformableMaterial(
prim_path:str,
name:str|None ='deformable_material',
dynamic_friction:float|None =None,
youngs_modulus:float|None =None,
poissons_ratio:float|None =None,
elasticity_damping:float|None =None,
damping_scale:float|None =None,
)Bases: `object`
A wrapper around deformable material used to simulate soft bodies.
get_damping_scale()→float
Returns:
The damping scale coefficient.

Return type:
float

get_dynamic_friction()→float
Returns:
The dynamic friction coefficient.

Return type:
float

get_elasticity_damping()→float
Returns:
The elasticity damping coefficient.

Return type:
float

get_poissons_ratio()→float
Returns:
The poissons ratio.

Return type:
float

get_youngs_modululs()→float
Returns:
The youngs modululs coefficient.

Return type:
float

initialize(physics_sim_view=None)→None
is_valid()→bool
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

post_reset()→None
Resets the prim to its default state.

set_damping_scale(value:float)→None
Sets the damping scale coefficient.
Parameters:
value (float) – The damping scale coefficient Range: [0, inf)

set_dynamic_friction(value:float)→None
Sets the dynamic_friction coefficient.
The dynamic_friction takes effect in all interactions between particles and rigids or deformables. For solid particle-particle interactions it is multiplied by the particle dynamic_friction scale.
Parameters:
value (float) – The dynamic_friction coefficient. Range: [0, inf), Units: dimensionless

set_elasticity_damping(value:float)→None
Sets the global velocity elasticity damping coefficient.
Parameters:
value (float) – The elasticity damping coefficient. Range: [0, inf), Units: dimensionless

set_poissons_ratio(value:float)→None
Sets the poissons ratio coefficient
Parameters:
value (float) – The poissons ratio. Range: (0 , 0.5)

set_youngs_modululs(value:float)→None
Sets the youngs_modululs for fluid particles.
Parameters:
value (float) – The youngs_modululs. Range: [0, inf)

propertymaterial:pxr.UsdShade.Material
Returns: UsdShade.Material: The USD Material object.

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: The USD prim present.

propertyprim_path:str
Returns: str: The stage path to the material.

classDeformableMaterialView(
prim_paths_expr:str,
name:str='deformable_material_view',
dynamic_frictions:ndarray|Tensor|None =None,
youngs_moduli:ndarray|Tensor|None =None,
poissons_ratios:ndarray|Tensor|None =None,
elasticity_dampings:ndarray|Tensor|None =None,
damping_scales:ndarray|Tensor|None =None,
)Bases: `object`
The view class to deal with deformableMaterial prims. Provides high level functions to deal with deformable material (1 or more deformable materials) as well as its attributes/ properties. This object wraps all matching materials found at the regex provided at the prim_paths_expr. This object wraps all matching materials Prims found at the regex provided at the prim_paths_expr.
get_damping_scales(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the damping scale of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
damping scale tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_dynamic_frictions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the dynamic friction of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
dynamic friction tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_elasticity_dampings(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the elasticity dampings of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
elasticity dampings tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_poissons_ratios(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the poissons ratios of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
poissons ratio tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

get_youngs_moduli(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the Youngs moduli of materials indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
Youngs moduli tensor with shape (M, )

Return type:
Union[np.ndarray, torch.Tensor]

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and creates a rigid body view in physX.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_physics_handle_valid()→bool
Returns:
True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.

Return type:
bool

is_valid(
indices:ndarray|list|Tensor|None =None,
)→boolParameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
True if all prim paths specified in the view correspond to a valid prim in stage. False otherwise.

Return type:
bool

post_reset()→None
Resets the deformables to their initial states.

set_damping_scales(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the damping scale for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material damping scale tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_dynamic_frictions(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the dynamic friction for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material dynamic friction tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_elasticity_dampings(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the elasticity_dampings for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material damping tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_poissons_ratios(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the poissons ratios for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material poissons ratio tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_youngs_moduli(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the youngs moduli for the material prims indicated by the indices.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]], optional) – material drag tensor with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which material prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

propertycount:int
Returns: int: number of rigid shapes for the prims in the view.

propertyname:str
Returns: str: name given to the view when instantiating it.

#### Objects
Modules to create/encapsulate visual, fixed, and dynamic shapes (Capsule, Cone, Cuboid, Cylinder, Sphere) as well as ground planes

[TABLE]
Type | Collider API | Rigid Body API
Visual | No | No
Fixed | Yes | No
Dynamic | Yes | Yes
[/TABLE]
classGroundPlane(
prim_path:str,
name:str='ground_plane',
size:float|None =None,
z_position:float|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
physics_material:PhysicsMaterial |None =None,
visual_material:VisualMaterial |None =None,
)Bases: `object`
High level wrapper to create/encapsulate a ground plane
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “ground_plane”.

- size (Optional[float], optional) – length of each edge. Defaults to 5000.0.

- z_position (float, optional) – ground plane position in the z-axis. Defaults to 0.

- scale (Optional[np.ndarray], optional) – local scale to be applied to the prim’s dimensions. Defaults to None.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual plane. Defaults to None.

- physics_material_path (Optional[PhysicsMaterial ], optional) – path of the physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- static_friction (float, optional) – static friction coefficient. Defaults to 0.5.

- dynamic_friction (float, optional) – dynamic friction coefficient. Defaults to 0.5.

- restitution (float, optional) – restitution coefficient. Defaults to 0.8.

Example:

```
>>> from isaacsim.core.api.objects import GroundPlane
>>> import numpy as np
>>>
>>> # create a ground plane placed at 0 in the z-axis
>>> plane = GroundPlane(prim_path="/World/GroundPlane", z_position=0)
>>> plane
<isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x7f15d003fb50>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> plane.apply_physics_material(material)
```

get_applied_physics_material()→PhysicsMaterial
Returns the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> plane.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f517ff62920>
```

get_default_state()→XFormPrimState
Get the default prim states (spatial position and orientation).
Returns:
an object that contains the default state of the prim (position and orientation)

Return type:
XFormPrimState

Example:

```
>>> state = plane.get_default_state()
>>> state
<isaacsim.core.utils.types.XFormPrimState object at 0x7f6efff41cf0>
>>>
>>> state.position
[0. 0. 0.]
>>> state.orientation
[1. 0. 0. 0.]
```

get_world_pose()→Tuple[ndarray,ndarray]
Get prim’s pose with respect to the world’s frame
Returns:
first index is the position in the world frame (with shape (3, )). Second index is quaternion orientation (with shape (4, )) in the world frame

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> # if the prim is in position (0.0, 0.0, 0.0) with respect to the world frame
>>> position, orientation = prim.get_world_pose()
>>> position
[0. 0. 0.]
>>> orientation
[1. 0. 0. 0.]
```

initialize(physics_sim_view=None)→None
Create a physics simulation view if not passed and using PhysX tensor API
Note
If the prim has been added to the world scene (e.g., `world.scene.add(prim)`), it will be automatically initialized when the world is reset (e.g., `world.reset()`).
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

Example:

```
>>> plane.initialize()
```

is_valid()→bool
Check if the prim path has a valid USD Prim at it
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> # given an existing and valid prim
>>> plane.is_valid()
True
```

post_reset()→None
Reset the prim to its default state (position and orientation).
Example:

```
>>> plane.post_reset()
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
)→None Sets the default state of the prim (position and orientation), that will be used after each reset.
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Example:

```
>>> # configure default state
>>> plane.set_default_state(position=np.array([0.0, 0.0, -1.0]), orientation=np.array([1, 0, 0, 0]))
>>>
>>> # set default states during post-reset
>>> plane.post_reset()
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
>>> plane.set_world_pose(position=np.array([0.0, 0.0, 0.5]), orientation=np.array([1., 0., 0., 0.]))
```

propertycollision_geometry_prim:SingleGeometryPrim
Returns:
wrapped object as a SingleGeometryPrim

Return type:
SingleGeometryPrim

Example:

```
>>> plane.collision_geometry_prim
<isaacsim.core.prims.single_geometry_prim.SingleGeometryPrim object at 0x7f15ff3461a0>
```

propertyname:str|None
Returns:
name given to the prim when instantiating it. Otherwise None.

Return type:
str

Example:

```
>>> plane.name
ground_plane
```

propertyprim:pxr.Usd.Prim
Returns:
USD Prim object that this object holds.

Return type:
Usd.Prim

Example:

```
>>> plane.prim
Usd.Prim(</World/GroundPlane>)
```

propertyprim_path:str
Returns:
prim path in the stage.

Return type:
str

Example:

```
>>> plane.prim_path
/World/GroundPlane
```

propertyxform_prim:SingleXFormPrim
Returns:
wrapped object as a SingleXFormPrim

Return type:
SingleXFormPrim

Example:

```
>>> plane.xform_prim
<isaacsim.core.prims.single_xform_prim.SingleXFormPrim object at 0x7f1578d32560>
```

classVisualCapsule(
prim_path:str,
name:str='visual_capsule',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:float|None =None,
height:float|None =None,
visual_material:VisualMaterial |None =None,
)Bases: SingleGeometryPrim
High level wrapper to create/encapsulate a visual capsule
Note
Visual capsules (Capsule shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “visual_capsule”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – capsule radius. Defaults to None.

- height (Optional[float], optional) – capsule height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

Example:

```
>>> from isaacsim.core.api.objects import VisualCapsule
>>> import numpy as np
>>>
>>> # create a red visual capsule at the given path
... prim = VisualCapsule(
... prim_path="/World/Xform/Capsule",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0])
... )
>>> prim
<isaacsim.core.api.objects.capsule.VisualCapsule object at 0x7f4ff958b0d0>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the capsule height
Returns:
capsule height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the capsule radius
Returns:
capsule radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_height(height:float)→None
Set the capsule height
Parameters:
height (float) – capsule height

Example:

```
>>> prim.set_height(2.0)
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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the capsule radius
Parameters:
radius (float) – capsule radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classVisualCone(
prim_path:str,
name:str='visual_cone',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:float|None =None,
height:float|None =None,
visual_material:VisualMaterial |None =None,
)Bases: SingleGeometryPrim
High level wrapper to create/encapsulate a visual cone
Note
Visual cones (Cone shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “visual_cone”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – base radius. Defaults to None.

- height (Optional[float], optional) – cone height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

Example:

```
>>> from isaacsim.core.api.objects import VisualCone
>>> import numpy as np
>>>
>>> # create a red visual cone at the given path
>>> prim = VisualCone(
... prim_path="/World/Xform/Cone",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0])
... )
>>> prim
<isaacsim.core.api.objects.cone.VisualCone object at 0x7f513413aa70>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the cone height
Returns:
cone height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the base radius
Returns:
base radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_height(height:float)→None
Set the cone height
Parameters:
height (float) – cone height

Example:

```
>>> prim.set_height(2.0)
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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the base radius
Parameters:
radius (float) – base radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classVisualCuboid(
prim_path:str,
name:str='visual_cube',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
color:ndarray|None =None,
size:float|None =None,
visual_material:VisualMaterial |None =None,
)Bases: SingleGeometryPrim
High level wrapper to create/encapsulate a visual cuboid
Note
Visual cuboids (Cube shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “visual_cube”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- size (Optional[float], optional) – length of each cube edge. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

Example:

```
>>> from isaacsim.core.api.objects import VisualCuboid
>>> import numpy as np
>>>
>>> # create a red visual cube at the given path
>>> prim = VisualCuboid(prim_path="/World/Xform/Cube", color=np.array([1.0, 0.0, 0.0]))
>>> prim
<isaacsim.core.api.objects.cuboid.VisualCuboid object at 0x7f12e756fa00>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_size()→ndarray
Get the length of each cube edge
Returns:
edge length

Return type:
float

Example:

```
>>> prim.get_size()
1.0
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_size(size:float)→None
Set the length of each cube edge
Parameters:
size (float) – edge length

Example:

```
>>> prim.set_size(2.0)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classVisualCylinder(
prim_path:str,
name:str='visual_cylinder',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:float|None =None,
height:float|None =None,
visual_material:VisualMaterial |None =None,
)Bases: SingleGeometryPrim
High level wrapper to create/encapsulate a visual cylinder
Note
Visual cylinders (Cylinder shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “visual_cylinder”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – base radius. Defaults to None.

- height (Optional[float], optional) – cylinder height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

Example:

```
>>> from isaacsim.core.api.objects import VisualCylinder
>>> import numpy as np
>>>
>>> # create a red visual cylinder at the given path
>>> prim = VisualCylinder(
... prim_path="/World/Xform/Cylinder",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0])
... )
>>> prim
<isaacsim.core.api.objects.cylinder.VisualCylinder object at 0x7f4e433f22c0>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the cylinder height
Returns:
cylinder height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the base radius
Returns:
base radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_height(height:float)→None
Set the cylinder height
Parameters:
height (float) – cylinder height

Example:

```
>>> prim.set_height(2.0)
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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the base radius
Parameters:
radius (float) – base radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classVisualSphere(
prim_path:str,
name:str='visual_sphere',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =True,
color:ndarray|None =None,
radius:float|None =None,
visual_material:VisualMaterial |None =None,
)Bases: SingleGeometryPrim
High level wrapper to create/encapsulate a visual sphere
Note
Visual spheres (Sphere shape) have no collisions (Collider API) or rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “visual_sphere”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – sphere radius. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

Example:

```
>>> from isaacsim.core.api.objects import VisualSphere
>>> import numpy as np
>>>
>>> # create a red visual sphere at the given path
>>> prim = VisualSphere(prim_path="/World/Xform/Sphere", color=np.array([1.0, 0.0, 0.0]))
>>> prim
<isaacsim.core.api.objects.sphere.VisualSphere object at 0x7f4e3eb3ea70>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the sphere radius
Returns:
sphere radius

Return type:
float

Example:

```
>>> prim.get_radius()
1.0
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the sphere radius
Parameters:
radius (float) – sphere radius

Example:

```
>>> prim.set_radius(2.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classFixedCapsule(
prim_path:str,
name:str='fixed_capsule',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
height:float|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
)Bases: VisualCapsule
High level wrapper to create/encapsulate a fixed capsule
Note
Fixed capsules (Capsule shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “fixed_capsule”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – capsule radius. Defaults to None.

- height (Optional[float], optional) – capsule height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

Example:

```
>>> from isaacsim.core.api.objects import FixedCapsule
>>> import numpy as np
>>>
>>> # create a red fixed capsule at the given path
>>> prim = FixedCapsule(
... prim_path="/World/Xform/Capsule",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0])
... )
>>> print(prim)
<isaacsim.core.api.objects.capsule.FixedCapsule object at 0x7f520c0d4790>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the capsule height
Returns:
capsule height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the capsule radius
Returns:
capsule radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_height(height:float)→None
Set the capsule height
Parameters:
height (float) – capsule height

Example:

```
>>> prim.set_height(2.0)
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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the capsule radius
Parameters:
radius (float) – capsule radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classFixedCone(
prim_path:str,
name:str='fixed_cone',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
height:float|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
)Bases: VisualCone
High level wrapper to create/encapsulate a fixed cone
Note
Fixed cones (Cone shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “fixed_cone”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – base radius. Defaults to None.

- height (Optional[float], optional) – cone height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

Example:

```
>>> from isaacsim.core.api.objects import FixedCone
>>> import numpy as np
>>>
>>> # create a red fixed cone at the given path
>>> prim = FixedCone(
... prim_path="/World/Xform/Cone",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0])
... )
>>> prim
<isaacsim.core.api.objects.cone.FixedCone object at 0x7f51489f09a0>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the cone height
Returns:
cone height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the base radius
Returns:
base radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(approximation_type:str)→None
Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_height(height:float)→None
Set the cone height
Parameters:
height (float) – cone height

Example:

```
>>> prim.set_height(2.0)
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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the base radius
Parameters:
radius (float) – base radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classFixedCuboid(
prim_path:str,
name:str='fixed_cube',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
size:float|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
)Bases: VisualCuboid
High level wrapper to create/encapsulate a fixed cuboid
Note
Fixed cuboids (Cube shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “fixed_cube”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- size (Optional[float], optional) – length of each cube edge. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

Example:

```
>>> from isaacsim.core.api.objects import FixedCuboid
>>> import numpy as np
>>>
>>> # create a red fixed cube at the given path
>>> prim = FixedCuboid(prim_path="/World/Xform/Cube", color=np.array([1.0, 0.0, 0.0]))
>>> prim
<isaacsim.core.api.objects.cuboid.FixedCuboid object at 0x7f7b4d91da80>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_size()→ndarray
Get the length of each cube edge
Returns:
edge length

Return type:
float

Example:

```
>>> prim.get_size()
1.0
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_size(size:float)→None
Set the length of each cube edge
Parameters:
size (float) – edge length

Example:

```
>>> prim.set_size(2.0)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classFixedCylinder(
prim_path:str,
name:str='fixed_cylinder',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
height:float|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
)Bases: VisualCylinder
High level wrapper to create/encapsulate a fixed cylinder
Note
Fixed cylinders (Cylinder shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “fixed_cylinder”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – base radius. Defaults to None.

- height (Optional[float], optional) – cylinder height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

Example:

```
>>> from isaacsim.core.api.objects import FixedCylinder
>>> import numpy as np
>>>
>>> # create a red fixed cylinder at the given path
>>> prim = FixedCylinder(
... prim_path="/World/Xform/Cylinder",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0])
... )
>>> print(prim)
<isaacsim.core.api.objects.cylinder.FixedCylinder object at 0x7f4f24144f40>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the cylinder height
Returns:
cylinder height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the base radius
Returns:
base radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_height(height:float)→None
Set the cylinder height
Parameters:
height (float) – cylinder height

Example:

```
>>> prim.set_height(2.0)
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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the base radius
Parameters:
radius (float) – base radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classFixedSphere(
prim_path:str,
name:str='fixed_sphere',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
)Bases: VisualSphere
High level wrapper to create/encapsulate a fixed sphere
Note
Fixed spheres (Sphere shape) have collisions (Collider API) but no rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “fixed_sphere”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – sphere radius. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

Example:

```
>>> from isaacsim.core.api.objects import FixedSphere
>>> import numpy as np
>>>
>>> # create a red fixed sphere at the given path
>>> prim = FixedSphere(prim_path="/World/Xform/Sphere", color=np.array([1.0, 0.0, 0.0]))
>>> prim
<isaacsim.core.api.objects.sphere.FixedSphere object at 0x7f4e433f2140>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

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

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

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

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the sphere radius
Returns:
sphere radius

Return type:
float

Example:

```
>>> prim.get_radius()
1.0
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

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

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the sphere radius
Parameters:
radius (float) – sphere radius

Example:

```
>>> prim.set_radius(2.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classDynamicCapsule(
prim_path:str,
name:str='dynamic_capsule',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
height:ndarray|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
mass:float|None =None,
density:float|None =None,
linear_velocity:Sequence[float]|None =None,
angular_velocity:Sequence[float]|None =None,
)Bases: SingleRigidPrim , FixedCapsule
High level wrapper to create/encapsulate a dynamic capsule
Note
Dynamic capsules (Capsule shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “dynamic_capsule”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – capsule radius. Defaults to None.

- height (Optional[float], optional) – capsule height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

- mass (Optional[float], optional) – mass in kg. Defaults to None.

- density (Optional[float], optional) – density. Defaults to None.

- linear_velocity (Optional[np.ndarray], optional) – linear velocity in the world frame. Defaults to None.

- angular_velocity (Optional[np.ndarray], optional) – angular velocity in the world frame. Defaults to None.

Example:

```
>>> from isaacsim.core.api.objects import DynamicCapsule
>>> import numpy as np
>>>
>>> # create a red fixed capsule of mass 1kg at the given path
>>> prim = DynamicCapsule(
... prim_path="/World/Xform/Capsule",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0]),
... mass=1.0
... )
>>> prim
<isaacsim.core.api.objects.capsule.DynamicCapsule object at 0x7f4ff915f8e0>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→DynamicState
Get the default rigid body state (position, orientation and linear and angular velocities)
Returns:
returns the default state of the prim that is used after each reset

Return type:
DynamicState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f7411fcbe20>
>>> state.position
[-7.8622378e-07 1.4450421e-06 1.6135601e-07]
>>> state.orientation
[ 9.9999994e-01 -2.7194994e-07 2.9607077e-07 2.7016510e-08]
>>> state.linear_velocity
[0. 0. 0.]
>>> state.angular_velocity
[0. 0. 0.]
```

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the capsule height
Returns:
capsule height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

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

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the capsule radius
Returns:
capsule radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
linear_velocity:ndarray|None =None,
angular_velocity:ndarray|None =None,
)→None Set the default state of the prim (position, orientation and linear and angular velocities), that will be used after each reset
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- linear_velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

- angular_velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

Example:

```
>>> prim.set_default_state(
... position=np.array([1.0, 2.0, 3.0]),
... orientation=np.array([1.0, 0.0, 0.0, 0.0]),
... linear_velocity=np.array([0.0, 0.0, 0.0]),
... angular_velocity=np.array([0.0, 0.0, 0.0])
... )
>>>
>>> prim.post_reset()
```

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_height(height:float)→None
Set the capsule height
Parameters:
height (float) – capsule height

Example:

```
>>> prim.set_height(2.0)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

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

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the capsule radius
Parameters:
radius (float) – capsule radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classDynamicCone(
prim_path:str,
name:str='dynamic_cone',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
height:ndarray|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
mass:float|None =None,
density:float|None =None,
linear_velocity:Sequence[float]|None =None,
angular_velocity:Sequence[float]|None =None,
)Bases: SingleRigidPrim , FixedCone
High level wrapper to create/encapsulate a dynamic cone
Note
Dynamic cones (Cone shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “dynamic_cone”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – base radius. Defaults to None.

- height (Optional[float], optional) – cone height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

- mass (Optional[float], optional) – mass in kg. Defaults to None.

- density (Optional[float], optional) – density. Defaults to None.

- linear_velocity (Optional[np.ndarray], optional) – linear velocity in the world frame. Defaults to None.

- angular_velocity (Optional[np.ndarray], optional) – angular velocity in the world frame. Defaults to None.

Example:

```
>>> from isaacsim.core.api.objects import DynamicCone
>>> import numpy as np
>>>
>>> # create a red dynamic cone of mass 1kg at the given path
>>> prim = DynamicCone(
... prim_path="/World/Xform/Cone",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0]),
... mass=1.0
... )
>>> prim
<isaacsim.core.api.objects.cone.DynamicCone object at 0x7f4f9f5d11b0>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→DynamicState
Get the default rigid body state (position, orientation and linear and angular velocities)
Returns:
returns the default state of the prim that is used after each reset

Return type:
DynamicState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f7411fcbe20>
>>> state.position
[-7.8622378e-07 1.4450421e-06 1.6135601e-07]
>>> state.orientation
[ 9.9999994e-01 -2.7194994e-07 2.9607077e-07 2.7016510e-08]
>>> state.linear_velocity
[0. 0. 0.]
>>> state.angular_velocity
[0. 0. 0.]
```

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the cone height
Returns:
cone height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

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

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the base radius
Returns:
base radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
linear_velocity:ndarray|None =None,
angular_velocity:ndarray|None =None,
)→None Set the default state of the prim (position, orientation and linear and angular velocities), that will be used after each reset
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- linear_velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

- angular_velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

Example:

```
>>> prim.set_default_state(
... position=np.array([1.0, 2.0, 3.0]),
... orientation=np.array([1.0, 0.0, 0.0, 0.0]),
... linear_velocity=np.array([0.0, 0.0, 0.0]),
... angular_velocity=np.array([0.0, 0.0, 0.0])
... )
>>>
>>> prim.post_reset()
```

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_height(height:float)→None
Set the cone height
Parameters:
height (float) – cone height

Example:

```
>>> prim.set_height(2.0)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

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

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the base radius
Parameters:
radius (float) – base radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classDynamicCuboid(
prim_path:str,
name:str='dynamic_cube',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
size:float|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
mass:float|None =None,
density:float|None =None,
linear_velocity:Sequence[float]|None =None,
angular_velocity:Sequence[float]|None =None,
)Bases: SingleRigidPrim , FixedCuboid
High level wrapper to create/encapsulate a dynamic cuboid
Note
Dynamic cuboids (Cube shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “fixed_cube”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- size (Optional[float], optional) – length of each cube edge. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

- mass (Optional[float], optional) – mass in kg. Defaults to None.

- density (Optional[float], optional) – density. Defaults to None.

- linear_velocity (Optional[np.ndarray], optional) – linear velocity in the world frame. Defaults to None.

- angular_velocity (Optional[np.ndarray], optional) – angular velocity in the world frame. Defaults to None.

Example:

```
>>> from isaacsim.core.api.objects import DynamicCuboid
>>> import numpy as np
>>>
>>> # create a red dynamic cube of mass 1kg at the given path
>>> prim = DynamicCuboid(prim_path="/World/Xform/Cube", color=np.array([1.0, 0.0, 0.0]), mass=1.0)
>>> prim
<isaacsim.core.api.objects.cuboid.DynamicCuboid object at 0x7ff14c04d990>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→DynamicState
Get the default rigid body state (position, orientation and linear and angular velocities)
Returns:
returns the default state of the prim that is used after each reset

Return type:
DynamicState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f7411fcbe20>
>>> state.position
[-7.8622378e-07 1.4450421e-06 1.6135601e-07]
>>> state.orientation
[ 9.9999994e-01 -2.7194994e-07 2.9607077e-07 2.7016510e-08]
>>> state.linear_velocity
[0. 0. 0.]
>>> state.angular_velocity
[0. 0. 0.]
```

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

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

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_size()→ndarray
Get the length of each cube edge
Returns:
edge length

Return type:
float

Example:

```
>>> prim.get_size()
1.0
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
linear_velocity:ndarray|None =None,
angular_velocity:ndarray|None =None,
)→None Set the default state of the prim (position, orientation and linear and angular velocities), that will be used after each reset
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- linear_velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

- angular_velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

Example:

```
>>> prim.set_default_state(
... position=np.array([1.0, 2.0, 3.0]),
... orientation=np.array([1.0, 0.0, 0.0, 0.0]),
... linear_velocity=np.array([0.0, 0.0, 0.0]),
... angular_velocity=np.array([0.0, 0.0, 0.0])
... )
>>>
>>> prim.post_reset()
```

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

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

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_size(size:float)→None
Set the length of each cube edge
Parameters:
size (float) – edge length

Example:

```
>>> prim.set_size(2.0)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classDynamicCylinder(
prim_path:str,
name:str='dynamic_cylinder',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
height:ndarray|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
mass:float|None =None,
density:float|None =None,
linear_velocity:Sequence[float]|None =None,
angular_velocity:Sequence[float]|None =None,
)Bases: SingleRigidPrim , FixedCylinder
High level wrapper to create/encapsulate a dynamic cylinder
Note
Dynamic cylinders (Cylinder shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “dynamic_cylinder”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – base radius. Defaults to None.

- height (Optional[float], optional) – cylinder height. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

- mass (Optional[float], optional) – mass in kg. Defaults to None.

- density (Optional[float], optional) – density. Defaults to None.

- linear_velocity (Optional[np.ndarray], optional) – linear velocity in the world frame. Defaults to None.

- angular_velocity (Optional[np.ndarray], optional) – angular velocity in the world frame. Defaults to None.

Example:

```
>>> from isaacsim.core.api.objects import DynamicCylinder
>>> import numpy as np
>>>
>>> # create a red fixed cylinder of mass 1kg at the given path
>>> prim = DynamicCylinder(
... prim_path="/World/Xform/Cylinder",
... radius=0.5,
... height=1.0,
... color=np.array([1.0, 0.0, 0.0]),
... mass=1.0
... )
>>> prim
<isaacsim.core.api.objects.cylinder.DynamicCylinder object at 0x7f4e8f5c4a60>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→DynamicState
Get the default rigid body state (position, orientation and linear and angular velocities)
Returns:
returns the default state of the prim that is used after each reset

Return type:
DynamicState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f7411fcbe20>
>>> state.position
[-7.8622378e-07 1.4450421e-06 1.6135601e-07]
>>> state.orientation
[ 9.9999994e-01 -2.7194994e-07 2.9607077e-07 2.7016510e-08]
>>> state.linear_velocity
[0. 0. 0.]
>>> state.angular_velocity
[0. 0. 0.]
```

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_height()→float
Get the cylinder height
Returns:
cylinder height

Return type:
float

Example:

```
>>> prim.get_height()
1.0
```

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

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

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the base radius
Returns:
base radius

Return type:
float

Example:

```
>>> prim.get_radius()
0.5
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
linear_velocity:ndarray|None =None,
angular_velocity:ndarray|None =None,
)→None Set the default state of the prim (position, orientation and linear and angular velocities), that will be used after each reset
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- linear_velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

- angular_velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

Example:

```
>>> prim.set_default_state(
... position=np.array([1.0, 2.0, 3.0]),
... orientation=np.array([1.0, 0.0, 0.0, 0.0]),
... linear_velocity=np.array([0.0, 0.0, 0.0]),
... angular_velocity=np.array([0.0, 0.0, 0.0])
... )
>>>
>>> prim.post_reset()
```

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_height(height:float)→None
Set the cylinder height
Parameters:
height (float) – cylinder height

Example:

```
>>> prim.set_height(2.0)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

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

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the base radius
Parameters:
radius (float) – base radius

Example:

```
>>> prim.set_radius(1.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

classDynamicSphere(
prim_path:str,
name:str='dynamic_sphere',
position:ndarray|None =None,
translation:ndarray|None =None,
orientation:ndarray|None =None,
scale:ndarray|None =None,
visible:bool|None =None,
color:ndarray|None =None,
radius:ndarray|None =None,
visual_material:VisualMaterial |None =None,
physics_material:PhysicsMaterial |None =None,
mass:float|None =None,
density:float|None =None,
linear_velocity:Sequence[float]|None =None,
angular_velocity:Sequence[float]|None =None,
)Bases: SingleRigidPrim , FixedSphere
High level wrapper to create/encapsulate a dynamic sphere
Note
Dynamic spheres (Sphere shape) have collisions (Collider API) and rigid body dynamics (Rigid Body API)
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “dynamic_sphere”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- color (Optional[np.ndarray], optional) – color of the visual shape. Defaults to None, which means 50% gray

- radius (Optional[float], optional) – sphere radius. Defaults to None.

- visual_material (Optional[VisualMaterial ], optional) – visual material to be applied to the held prim. Defaults to None. If not specified, a default visual material will be added.

- physics_material (Optional[PhysicsMaterial ], optional) – physics material to be applied to the held prim. Defaults to None. If not specified, a default physics material will be added.

- mass (Optional[float], optional) – mass in kg. Defaults to None.

- density (Optional[float], optional) – density. Defaults to None.

- linear_velocity (Optional[np.ndarray], optional) – linear velocity in the world frame. Defaults to None.

- angular_velocity (Optional[np.ndarray], optional) – angular velocity in the world frame. Defaults to None.

Example:

```
>>> from isaacsim.core.api.objects import DynamicSphere
>>> import numpy as np
>>>
>>> # create a red dynamic sphere of mass 1kg at the given path
>>> prim = DynamicSphere(prim_path="/World/Xform/Sphere", color=np.array([1.0, 0.0, 0.0]), mass=1.0)
>>> prim
<isaacsim.core.api.objects.sphere.DynamicSphere object at 0x7f4deaf8f010>
```
apply_physics_material(
physics_material:PhysicsMaterial ,
weaker_than_descendants:bool=False,
)Used to apply physics material to the held prim and optionally its descendants.
Parameters:

- physics_material (PhysicsMaterial ) – physics material to be applied to the held prim. This where you want to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX.

- weaker_than_descendants (bool, optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False.

Example:

```
>>> from isaacsim.core.api.materials import PhysicsMaterial
>>>
>>> # create a rigid body physical material
>>> material = PhysicsMaterial(
... prim_path="/World/physics_material/aluminum", # path to the material prim to create
... dynamic_friction=0.4,
... static_friction=1.1,
... restitution=0.1
... )
>>> prim.apply_physics_material(material)
```

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

disable_rigid_body_physics()→None
Disable the rigid body physics
When disabled, the object will not be moved by external forces such as gravity and collisions
Example:

```
>>> prim.disable_rigid_body_physics()
```

enable_rigid_body_physics()→None
Enable the rigid body physics
When enabled, the object will be moved by external forces such as gravity and collisions
Example:

```
>>> prim.enable_rigid_body_physics()
```

get_angular_velocity()
Get the angular velocity of the rigid body
Returns:
current angular velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

get_applied_physics_material()→PhysicsMaterial
Return the current applied physics material in case it was applied using apply_physics_material or not.
Returns:
the current applied physics material.

Return type:
PhysicsMaterial

Example:

```
>>> # given a physics material applied
>>> prim.get_applied_physics_material()
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7fb66c30cd30>
```

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

get_collision_approximation()→str
Get the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Returns:
approximation used for collision

Return type:
str

Example:

```
>>> prim.get_collision_approximation()
none
```

get_collision_enabled()→bool
Check if the Collision API is enabled
Returns:
True if the Collision API is enabled. Otherwise False

Return type:
bool

Example:

```
>>> prim.get_collision_enabled()
True
```

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

get_contact_force_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed contact forces between the prims in the view and the filter prims including the normal contact forces, normal directions, contact points, separations. The number of contacts per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (self._geometry_prim_view._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor]

get_contact_offset()→float
Get the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
contact offset of the collision shape. Default value is -inf, means default is picked by simulation.

Return type:
float

Example:

```
>>> prim.get_contact_offset()
-inf
```

get_current_dynamic_state()→DynamicState
Get the current rigid body state (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid body prim

Return type:
DynamicState

Example:

```
>>> # for the example the rigid body is in free fall
>>> state = prim.get_current_dynamic_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f740b36f670>
>>> state.position
[ 0.99999857 2.0000017 -74.2862 ]
>>> state.orientation
[ 1.0000000e+00 -2.3961178e-07 -4.9891562e-09 4.9388258e-09]
>>> state.linear_velocity
[ 0. 0. -38.09554]
>>> state.angular_velocity
[0. 0. 0.]
```

get_default_state()→DynamicState
Get the default rigid body state (position, orientation and linear and angular velocities)
Returns:
returns the default state of the prim that is used after each reset

Return type:
DynamicState

Example:

```
>>> state = prim.get_default_state()
>>> state
<isaacsim.core.utils.types.DynamicState object at 0x7f7411fcbe20>
>>> state.position
[-7.8622378e-07 1.4450421e-06 1.6135601e-07]
>>> state.orientation
[ 9.9999994e-01 -2.7194994e-07 2.9607077e-07 2.7016510e-08]
>>> state.linear_velocity
[0. 0. 0.]
>>> state.angular_velocity
[0. 0. 0.]
```

get_density()→float
Get the density of the rigid body
Returns:
density of the rigid body.

Return type:
float

Example:

```
>>> prim.get_density()
0
```

get_friction_data(
dt:float=1.0,
)→ndarray|TensorIf the object is initialized with filter_paths_expr list, this method returns the detailed friction forces between the prims in the view and the filter prims including the tangential forces, and points. The number of points per pair is determined from a static tensor of dimension (self._contact_view.num_filters) while the starting index of the associated contact in the above tensors is determined from another static tensor of dimension (self._contact_view.num_filters).
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), as well as two tensors with shape (self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_linear_velocity()→ndarray
Get the linear velocity of the rigid body
Returns:
current linear velocity of the the rigid prim. Shape (3,).

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[ 1.0812164e-04 6.1415871e-05 -2.1341663e-04]
```

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

get_mass()→float
Get the mass of the rigid body
Returns:
mass of the rigid body in kg.

Return type:
float

Example:

```
>>> prim.get_mass()
0
```

get_min_torsional_patch_radius()→float
Get the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_min_torsional_patch_radius()
0.0
```

get_net_contact_forces(
dt:float=1.0,
)→ndarray|TensorIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (1, 3)
Parameters:
dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (3).

Return type:
Union[np.ndarray, torch.Tensor]

get_radius()→float
Get the sphere radius
Returns:
sphere radius

Return type:
float

Example:

```
>>> prim.get_radius()
1.0
```

get_rest_offset()→float
Get the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Returns:
rest offset of the collision shape.

Return type:
float

Example:

```
>>> prim.get_rest_offset()
-inf
```

get_sleep_threshold()→float
Get the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Returns:
Mass-normalized kinetic energy threshold below which
an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
5e-05
```

get_torsional_patch_radius()→float
Get the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Returns:
radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Return type:
float

Example:

```
>>> prim.get_torsional_patch_radius()
0.0
```

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the rigid body in stage
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

set_collision_approximation(
approximation_type:str,
)→None Set the collision approximation

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders
[/TABLE]
Note
Use Convex Decomposition or SDF (Signed-Distance-Field) tri-meshes to capture details better
Warning
Switching to Convex Decomposition or SDF (Signed-Distance-Field) will have a simulation performance impact due to higher computational cost
Parameters:
approximation_type (str) – approximation used for collision

Example:

```
>>> prim.set_collision_approximation("convexDecomposition")
```

set_collision_enabled(enabled:bool)→None
Enable/disable the Collision API
Parameters:
enabled (bool) – Whether to enable or disable the Collision API

Example:

```
>>> # disable collisions
>>> prim.set_collision_enabled(False)
```

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

set_contact_offset(offset:float)→None
Set the contact offset
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Contact offset of a collision shape. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent.

Example:

```
>>> prim.set_contact_offset(0.02)
```

set_default_state(
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
linear_velocity:ndarray|None =None,
angular_velocity:ndarray|None =None,
)→None Set the default state of the prim (position, orientation and linear and angular velocities), that will be used after each reset
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- linear_velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

- angular_velocity (np.ndarray) – angular velocity to set the rigid prim to. Shape (3,).

Example:

```
>>> prim.set_default_state(
... position=np.array([1.0, 2.0, 3.0]),
... orientation=np.array([1.0, 0.0, 0.0, 0.0]),
... linear_velocity=np.array([0.0, 0.0, 0.0]),
... angular_velocity=np.array([0.0, 0.0, 0.0])
... )
>>>
>>> prim.post_reset()
```

set_density(density:float)→None
Set the density of the rigid body
Parameters:
mass (float) – density of the rigid body.

Example:

```
>>> prim.set_density(0.9)
```

set_linear_velocity(velocity:ndarray)
Set the linear velocity of the rigid body in stage
Warning
This method will immediately set the rigid prim state
Parameters:
velocity (np.ndarray) – linear velocity to set the rigid prim to. Shape (3,).

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

set_mass(mass:float)→None
Set the mass of the rigid body
Parameters:
mass (float) – mass of the rigid body in kg.

Example:

```
>>> prim.set_mass(1.0)
```

set_min_torsional_patch_radius(radius:float)→None
Set the minimum radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_min_torsional_patch_radius(0.05)
```

set_radius(radius:float)→None
Set the sphere radius
Parameters:
radius (float) – sphere radius

Example:

```
>>> prim.set_radius(2.0)
```

set_rest_offset(offset:float)→None
Set the rest offset
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:
offset (float) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset. Default value is -inf, means default is picked by simulation. For rigid bodies its zero.

Example:

```
>>> prim.set_rest_offset(0.01)
```

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
```

set_torsional_patch_radius(radius:float)→None
Set the radius of the contact patch used to apply torsional friction
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
radius (float) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float].

Example:

```
>>> prim.set_torsional_patch_radius(0.1)
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

propertygeom:pxr.UsdGeom.Gprim
Returns: UsdGeom.Gprim: USD geometry object encapsulated.

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

#### Physics Context
classPhysicsContext(
physics_dt:float|None =None,
prim_path:str='/physicsScene',
sim_params:dict=None,
set_defaults:bool=True,
)Bases: `object`
Provides high level functions to deal with a physics scene and its settings. This will create a
a PhysicsScene prim at the specified prim path in case there is no PhysicsScene present in the current stage. If there is a PhysicsScene present, it will discard the prim_path specified and sets the default settings on the current PhysicsScene found.

Parameters:

- physics_dt (float, optional) – specifies the physics_dt of the simulation. Defaults to 1.0 / 60.0.

- prim_path (Optional[str], optional) – specifies the prim path to create a PhysicsScene at, only in the case where no PhysicsScene already defined. Defaults to “/physicsScene”.

- set_defaults (bool, optional) – set to True to use the defaults physics parameters [physics_dt = 1.0/ 60.0, gravity = -9.81 m / s ccd_enabled, stabilization_enabled, gpu dynamics turned off, broadcast type is MBP, solver type is TGS]. Defaults to True.

Raises:

- Exception – If prim_path is not absolute.

- Exception – if prim_path already exists and its type is not a PhysicsScene.

enable_ccd(flag:bool)→None
Enables a second broad phase after integration that makes it possible to prevent objects from tunneling
through each other. If GPU is enabled, CCD is not supported and the request will be ignored. If CCD is enabled and then the GPU pipeline is requested, CCD will be disabled automatically.

Parameters:
flag (bool) – enables or disables ccd on the PhysicsScene. CCD is not supported on GPU, so the request will be ignored if GPU is enabled.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

enable_fabric(enable)
enable_gpu_dynamics(flag:bool)→None
Enables gpu dynamics pipeline, required for deformables for instance.
Parameters:
flag (bool) – enables or disables gpu dynamics on the PhysicsScene

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

enable_residual_reporting(flag:bool)
Set the physx scene flag to enable/disable solver residual reporting.
Parameters:
flag (bool) – enables or disables scene residuals on the PhysicsScene

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

enable_stablization(flag:bool)→None
Enables additional stabilization pass in the solver.
Parameters:
flag (bool) – enables or disables stabilization on the PhysicsScene

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

get_bounce_threshold()→float
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
float

get_broadphase_type()→str
Gets current broadcast phase algorithm type.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
Broadcast phase algorithm used.

Return type:
str

get_current_physics_scene_prim()→pxr.Usd.Prim|None
Used to return the PhysicsScene prim in stage by traversing the stage.
Returns:
returns a PhysicsScene prim if found in current stage. Otherwise, None.

Return type:
Optional[Usd.Prim]

get_enable_scene_query_support()→bool
Retrieves the Enable Scene Query Support attribute in Physx Scene
Raises:
Exception – [description]

Returns:
enable scene query support attribute

Return type:
bool

get_friction_correlation_distance()→float
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
float

get_friction_offset_threshold()→float
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
float

get_gpu_collision_stack_size()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_found_lost_aggregate_pairs_capacity()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_found_lost_pairs_capacity()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_heap_capacity()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_max_num_partitions()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_max_particle_contacts()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_max_rigid_contact_count()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_max_rigid_patch_count()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_max_soft_body_contacts()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_temp_buffer_capacity()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gpu_total_aggregate_pairs_capacity()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_gravity()→Tuple[List,float]
Gets current gravity.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
returns a tuple, first element corresponds to the gravity direction vector and second element is the magnitude.

Return type:
Tuple[list, float]

get_invert_collision_group_filter()→int
[summary]
Raises:
Exception – [description]

Returns:
[description]

Return type:
int

get_physics_dt()→float
Returns the current physics dt.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
physics dt.

Return type:
float

get_physx_update_transformations_settings()→Tuple[bool,bool,bool,bool]
Gets how physx syncs with the usd when transformations are updated.
Returns:
[update_to_usd, update_velocities_to_usd, output_velocities_local_space]

Return type:
Tuple[bool, bool, bool, bool]

get_solve_articulation_contact_last()→bool
Retrieves the `solveArticulationContactLast` state in PhysX scene.
Raises:
Exception – The physics scene path is invalid.

Returns:
Whether the articulation contact constraints and the articulation joint maximum velocity constraints are ordered to be solved last.

Return type:
bool

get_solver_position_residual(report_max:bool=True)
Enable physics scene residual reporting API and chooses between RMS vs Max criteri for position residuals.
Parameters:
report_max (bool) – Use the max residual criterion if True, otherwise use the RMS criterion.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

get_solver_type()→str
Gets current solver type.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
solver used for simulation.

Return type:
str

get_solver_velocity_residual(report_max:bool=True)
Enable physics scene residual reporting API and chooses between RMS vs Max criteri for velocity residuals.
Parameters:
report_max (bool) – Use the max residual criterion if True, otherwise use the RMS criterion.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

is_ccd_enabled()→bool
Checks if ccd is enabled.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
True if ccd is enabled, otherwise False.

Return type:
bool

is_gpu_dynamics_enabled()→bool
Checks if Gpu Dynamics is enabled.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
True if Gpu Dynamics is enabled, otherwise False.

Return type:
bool

is_stablization_enabled()→bool
Checks if stabilization is enabled.
Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

Returns:
True if stabilization is enabled, otherwise False.

Return type:
bool

set_bounce_threshold(value:float)→None
[summary]
Parameters:
value (float) – [description]

Raises:
Exception – [description]

set_broadphase_type(broadcast_type:str)→None
Broadcast phase algorithm used in simulation.
Parameters:
broadcast_type (str) – type of broadcasting to be used, can be “MBP”

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

set_enable_scene_query_support(
enable_scene_query_support:bool,
)→None Sets the Enable Scene Query Support attribute in Physx Scene
Parameters:
enable_scene_query_support (bool) – Whether to enable scene query support

Raises:
Exception – [description]

set_friction_correlation_distance(value:float)→None
[summary]
Parameters:
value (float) – [description]

Raises:
Exception – [description]

set_friction_offset_threshold(value:float)→None
[summary]
Parameters:
value (float) – [description]

Raises:
Exception – [description]

set_gpu_collision_stack_size(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_found_lost_aggregate_pairs_capacity(
value:int,
)→None [summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_found_lost_pairs_capacity(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_heap_capacity(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_max_num_partitions(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_max_particle_contacts(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_max_rigid_contact_count(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_max_rigid_patch_count(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_max_soft_body_contacts(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_temp_buffer_capacity(value:int)→None
[summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gpu_total_aggregate_pairs_capacity(
value:int,
)→None [summary]
Parameters:
value (int) – [description]

Raises:
Exception – [description]

set_gravity(value:float)→None
sets the gravity direction and magnitude.
Parameters:
value (float) – gravity value to be used in simulation.

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

set_invert_collision_group_filter(
invert_collision_group_filter:bool,
)→None [summary]
Parameters:
invert_collision_group_filter (bool) – [description]

Raises:
Exception – [description]

set_physics_dt(
dt:float=0.016666666666666666,
substeps:int=1,
)→None Sets the physics dt on the PhysicsScene
Parameters:

- dt (float, optional) – physics dt. Defaults to 1.0/60.0.

- substeps (int, optional) – number of physics steps to run for before rendering a frame. Defaults to 1.

Raises:

- Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

- ValueError – Physics dt must be a >= 0.

- ValueError – Physics dt must be a <= 1.0.

set_physx_update_transformations_settings(
update_to_usd:bool|None =None,
update_velocities_to_usd:bool|None =None,
output_velocities_local_space:bool|None =None,
)→None Sets how physx syncs with the usd when transformations are updated.
Parameters:

- update_to_usd (bool, optional) – Updates to USD the transformations. Defaults to True.

- update_velocities_to_usd (bool, optional) – Updates Velocities to USD. Defaults to True.

- output_velocities_local_space (bool, optional) – Output the velocities in the local frame and not the world frame. Defaults to False.

set_solve_articulation_contact_last(
solve_articulation_contact_last:bool,
)→None Sets the `solveArticulationContactLast` state in PhysX scene.
When enabled, the solver orders the articulation contact constraints and the articulation joint maximum velocity constraints to be solved after all the other constraints.
Parameters:
solve_articulation_contact_last (bool) – Whether to reorder the constraints to be solved last.

Raises:
Exception – The physics scene path is invalid.

set_solver_type(solver_type:str)→None
solver used for simulation.
Parameters:
solver_type (str) – can be “TGS” or “PGS”. for references look at..

Raises:
Exception – If the prim path registered in context doesn’t correspond to a valid prim path currently.

warm_start()
propertydevice:str
propertyprim_path
propertyuse_fabric
propertyuse_gpu_pipeline
propertyuse_gpu_sim

#### Robots
classRobot(
prim_path:str,
name:str='robot',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool=True,
articulation_controller:ArticulationController |None =None,
)Bases: SingleArticulation
Implementation (on `SingleArticulation` class) to deal with an articulation prim as a robot
Warning
The robot (articulation) object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “robot”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- articulation_controller (Optional[ArticulationController ], optional) – a custom ArticulationController which inherits from it. Defaults to creating the basic ArticulationController.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.api.robots import Robot
>>>
>>> usd_path = "/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd"
>>> prim_path = "/World/envs/env_0/panda"
>>>
>>> # load the Franka Panda robot USD file
>>> stage_utils.add_reference_to_stage(usd_path, prim_path)
>>>
>>> # wrap the prim as a robot (articulation)
>>> prim = Robot(prim_path=prim_path, name="franka_panda")
>>> print(prim)
<isaacsim.core.api.robots.robot.Robot object at 0x7fdd4875a1d0>
```
apply_action(
control_actions:ArticulationAction ,
)→None Apply joint positions, velocities and/or efforts to control an articulation
Parameters:

- control_actions (ArticulationAction ) – actions to be applied for next physics step.

- indices (Optional[Union[list, np.ndarray]], optional) – degree of freedom indices to apply actions to. Defaults to all degrees of freedom.

Hint
High stiffness makes the joints snap faster and harder to the desired target, and higher damping smoothes but also slows down the joint’s movement to target

- For position control, set relatively high stiffness and low damping (to reduce vibrations)

- For velocity control, stiffness must be set to zero with a non-zero damping

- For effort control, stiffness and damping must be set to zero

Example:

```
>>> from isaacsim.core.utils.types import ArticulationAction
>>>
>>> # move all the robot joints to the indicated position
>>> action = ArticulationAction(joint_positions=np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]))
>>> prim.apply_action(action)
>>>
>>> # close the robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> action = ArticulationAction(joint_positions=np.array([0.0, 0.0]), joint_indices=np.array([7, 8]))
>>> prim.apply_action(action)
```

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

disable_gravity()→None
Keep gravity from affecting the robot
Example:

```
>>> prim.disable_gravity()
```

enable_gravity()→None
Gravity will affect the robot
Example:

```
>>> prim.enable_gravity()
```

get_angular_velocity()→ndarray
Get the angular velocity of the root articulation prim
Returns:
3D angular velocity vector. Shape (3,)

Return type:
np.ndarray

Example:

```
>>> prim.get_angular_velocity()
[0. 0. 0.]
```

get_applied_action()→ArticulationAction
Get the last applied action
Returns:
last applied action. Note: a dictionary is used as the object’s string representation

Return type:
ArticulationAction

Example:

```
>>> # last applied action: joint_positions -> [0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]
>>> prim.get_applied_action()
{'joint_positions': [0.0, -1.0, 0.0, -2.200000047683716, 0.0, 2.4000000953674316,
0.800000011920929, 0.03999999910593033, 0.03999999910593033],
'joint_velocities': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
'joint_efforts': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
```

get_applied_joint_efforts(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the efforts applied to the joints set by the `set_joint_efforts` method
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Raises:
Exception – If the handlers are not initialized

Returns:
all or selected articulation joint applied efforts

Return type:
np.ndarray

Example:

```
>>> # get all applied joint efforts
>>> prim.get_applied_joint_efforts()
[ 0. 0. 0. 0. 0. 0. 0. 0. 0.]
>>>
>>> # get finger applied efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_applied_joint_efforts(joint_indices=np.array([7, 8]))
[0. 0.]
```

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

get_articulation_body_count()→int
Get the number of bodies (links) that make up the articulation
Returns:
amount of bodies

Return type:
int

Example:

```
>>> prim.get_articulation_body_count()
12
```

get_articulation_controller()→ArticulationController
Get the articulation controller
Note
If no `articulation_controller` was passed during class instantiation, a default controller of type `ArticulationController` (a Proportional-Derivative controller that can apply position targets, velocity targets and efforts) will be used
Returns:
articulation controller

Return type:
ArticulationController

Example:

```
>>> prim.get_articulation_controller()
<isaacsim.core.api.controllers.articulation_controller.ArticulationController object at 0x7f04a0060190>
```

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

get_dof_index(dof_name:str)→int
Get a DOF index given its name
Parameters:
dof_name (str) – name of the DOF

Returns:
DOF index

Return type:
int

Example:

```
>>> prim.get_dof_index("panda_finger_joint2")
8
```

get_enabled_self_collisions()→int
Get the enable self collisions flag (`physxArticulation:enabledSelfCollisions`)
Returns:
self collisions flag (boolean interpreted as int)

Return type:
int

Example:

```
>>> prim.get_enabled_self_collisions()
0
```

get_joint_positions(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the articulation joint positions
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Returns:
all or selected articulation joint positions

Return type:
np.ndarray

Example:

```
>>> # get all joint positions
>>> prim.get_joint_positions()
[ 1.1999920e-02 -5.6962633e-01 1.3480479e-08 -2.8105433e+00 6.8284894e-06
3.0301569e+00 7.3234749e-01 3.9912373e-02 3.9999999e-02]
>>>
>>> # get finger positions: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_joint_positions(joint_indices=np.array([7, 8]))
[0.03991237 3.9999999e-02]
```

get_joint_velocities(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the articulation joint velocities
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Returns:
all or selected articulation joint velocities

Return type:
np.ndarray

Example:

```
>>> # get all joint velocities
>>> prim.get_joint_velocities()
[ 1.91603772e-06 -7.67638255e-03 -2.19138826e-07 1.10636465e-02 -4.63412944e-05
3.48245539e-02 8.84692147e-02 5.40335372e-04 1.02849208e-05]
>>>
>>> # get finger velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_joint_velocities(joint_indices=np.array([7, 8]))
[5.4033537e-04 1.0284921e-05]
```

get_joints_default_state()→JointsState
Get the default joint states (positions and velocities).
Returns:
an object that contains the default joint positions and velocities

Return type:
JointsState

Example:

```
>>> state = prim.get_joints_default_state()
>>> state
<isaacsim.core.utils.types.JointsState object at 0x7f04a0061240>
>>>
>>> state.positions
[ 0.012 -0.57000005 0. -2.81 0. 3.037 0.785398 0.04 0.04 ]
>>> state.velocities
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

get_joints_state()→JointsState
Get the current joint states (positions and velocities)
Returns:
an object that contains the current joint positions and velocities

Return type:
JointsState

Example:

```
>>> state = prim.get_joints_state()
>>> state
<isaacsim.core.utils.types.JointsState object at 0x7f02f6df57b0>
>>>
>>> state.positions
[ 1.1999920e-02 -5.6962633e-01 1.3480479e-08 -2.8105433e+00 6.8284894e-06
3.0301569e+00 7.3234749e-01 3.9912373e-02 3.9999999e-02]
>>> state.velocities
[ 1.91603772e-06 -7.67638255e-03 -2.19138826e-07 1.10636465e-02 -4.63412944e-05
245539e-02 8.84692147e-02 5.40335372e-04 1.02849208e-05]
```

get_linear_velocity()→ndarray
Get the linear velocity of the root articulation prim
Returns:
3D linear velocity vector. Shape (3,)

Return type:
np.ndarray

Example:

```
>>> prim.get_linear_velocity()
[0. 0. 0.]
```

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

get_measured_joint_efforts(
joint_indices:List|ndarray|None =None,
)→ndarrayReturns the efforts computed/measured by the physics solver of the joint forces in the DOF motion direction
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Raises:
Exception – If the handlers are not initialized

Returns:
all or selected articulation joint measured efforts

Return type:
np.ndarray

Example:

```
>>> # get all joint efforts
>>> prim.get_measured_joint_efforts()
[ 2.7897308e-06 -6.9083519e+00 -3.6398471e-06 1.9158335e+01 -4.3552645e-06
1.1866090e+00 -4.7079347e-06 3.2339853e-04 -3.2044132e-04]
>>>
>>> # get finger efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> prim.get_measured_joint_efforts(joint_indices=np.array([7, 8]))
[ 0.0003234 -0.00032044]
```

get_measured_joint_forces(
joint_indices:List|ndarray|None =None,
)→ndarrayGet the measured joint reaction forces and torques (link incoming joint forces and torques) to external loads.
Forces and torques are reported in the local body reference frame (child joint frame of the link’s incoming joint).
Note
Since the name->index map for joints has not been exposed yet, it is possible to access the joint names and their indices through the articulation metadata.

```
prim._articulation_view._metadata.joint_names # list of names
prim._articulation_view._metadata.joint_indices # dict of name: index
```
To retrieve a specific row for the link incoming joint force/torque use `joint_index + 1`
Parameters:
joint_indices (Optional[Union[List, np.ndarray]], optional) – indices to specify which joints to read. Defaults to None (all joints)

Raises:
Exception – If the handlers are not initialized

Returns:
measured joint forces and torques. Shape is (num_joint + 1, 6). Row index 0 is the incoming joint of the base link. For the last dimension the first 3 values are for forces and the last 3 for torques

Return type:
np.ndarray

Example:

```
>>> # get all measured joint forces and torques
>>> prim.get_measured_joint_forces()
[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 1.4995076e+02 4.2574748e-06 5.6364370e-04 4.8701895e-05 -6.9072924e+00 3.1881387e-05]
[-2.8971717e-05 -1.0677823e+02 -6.8384506e+01 -6.9072924e+00 -5.4927128e-05 6.1222494e-07]
[ 8.7120995e+01 -4.3871860e-05 -5.5795174e+01 5.3687054e-05 -2.4538563e+01 1.3333466e-05]
[ 5.3519474e-05 -4.8109909e+01 6.0709282e+01 1.9157074e+01 -5.9258469e-05 8.2744418e-07]
[-3.1691040e+01 2.3313689e-04 3.9990173e+01 -5.8968733e-05 -1.1863431e+00 2.2335558e-05]
[-1.0809851e-04 1.5340537e+01 -1.5458489e+01 1.1863426e+00 6.1094368e-05 -1.5940281e-05]
[-7.5418940e+00 -5.0814648e+00 -5.6512990e+00 -5.6385466e-05 3.8859999e-01 -3.4943256e-01]
[ 4.7421460e+00 -3.1945827e+00 3.5528181e+00 5.5852943e-05 8.4794536e-03 7.6405057e-03]
[ 4.0760727e+00 2.1640673e-01 -4.0513167e+00 -5.9565349e-04 1.1407082e-02 2.1432268e-06]
[ 5.1680198e-03 -9.7754575e-02 -9.7093947e-02 -8.4155556e-12 -1.2910691e-12 -1.9347857e-11]
[-5.1910793e-03 9.7588278e-02 -9.7106412e-02 8.4155573e-12 1.2910637e-12 -1.9347855e-11]]
>>>
>>> # get measured joint force and torque for the fingers
>>> metadata = prim._articulation_view._metadata
>>> joint_indices = 1 + np.array([
... metadata.joint_indices["panda_finger_joint1"],
... metadata.joint_indices["panda_finger_joint2"],
... ])
>>> joint_indices
[10 11]
>>> prim.get_measured_joint_forces(joint_indices)
[[ 5.1680198e-03 -9.7754575e-02 -9.7093947e-02 -8.4155556e-12 -1.2910691e-12 -1.9347857e-11]
[-5.1910793e-03 9.7588278e-02 -9.7106412e-02 8.4155573e-12 1.2910637e-12 -1.9347855e-11]]
```

get_position_residual(report_max:bool|None =True)→float
Get physics solver position residuals for articulations. This is the residual across all joints that are part of articulations.
The solver residuals are computed according to impulse variation normalized by the effective mass.
Parameters:
report_max (Optional[bool]) – whether to report max or RMS residual. Defaults to True, i.e. max criteria

Returns:
solver position/velocity max/rms residual.

Return type:
float

get_sleep_threshold()→float
Get the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Returns:
sleep threshold

Return type:
float

Example:

```
>>> prim.get_sleep_threshold()
0.005
```

get_solver_position_iteration_count()→int
Get the solver (position) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Returns:
position iteration count

Return type:
int

Example:

```
>>> prim.get_solver_position_iteration_count()
32
```

get_solver_velocity_iteration_count()→int
Get the solver (velocity) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Returns:
velocity iteration count

Return type:
int

Example:

```
>>> prim.get_solver_velocity_iteration_count()
32
```

get_stabilization_threshold()→float
Get the mass-normalized kinetic energy below which the articulation may participate in stabilization
Search for Stabilization Threshold in PhysX docs for more details
Returns:
stabilization threshold

Return type:
float

Example:

```
>>> prim.get_stabilization_threshold()
0.0009999999
```

get_velocity_residual(report_max:bool|None =True)→float
Get physics solver velocity residuals for articulations. This is the residual across all joints that are part of articulations.
The solver residuals are computed according to impulse variation normalized by the effective mass.
Parameters:
report_max (Optional[bool]) – whether to report max or RMS residual. Defaults to True, i.e. max criteria

Returns:
solver velocity max/rms residual.

Return type:
float

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

get_world_velocity()→ndarray
Get the articulation root velocity
Returns:
current velocity of the the root prim. Shape (3,).

Return type:
np.ndarray

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and an articulation view using PhysX tensor API
Note
If the articulation has been added to the world scene (e.g., `world.scene.add(prim)`), it will be automatically initialized when the world is reset (e.g., `world.reset()`).
Warning
This method needs to be called after each hard reset (e.g., Stop + Play on the timeline) before interacting with any other class method.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

Example:

```
>>> prim.initialize()
```

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

post_reset()→None
Reset the robot to its default state
Note
For a robot, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(velocity:ndarray)→None
Set the angular velocity of the root articulation prim
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – 3D angular velocity vector. Shape (3,)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> prim.set_angular_velocity(np.array([0.1, 0.0, 0.0]))
```

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

set_enabled_self_collisions(flag:bool)→None
Set the enable self collisions flag (`physxArticulation:enabledSelfCollisions`)
Parameters:
flag (bool) – whether to enable self collisions

Example:

```
>>> prim.set_enabled_self_collisions(True)
```

set_joint_efforts(
efforts:ndarray,
joint_indices:List|ndarray|None =None,
)→None Set the articulation joint efforts
Note
This method can be used for effort control. For this purpose, there must be no joint drive or the stiffness and damping must be set to zero.
Parameters:

- efforts (np.ndarray) – articulation joint efforts

- joint_indices (Optional[Union[list, np.ndarray]], optional) – indices to specify which joints to manipulate. Defaults to None (all joints)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the robot joint efforts to 0.0
>>> prim.set_joint_efforts(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
>>>
>>> # set only the fingers efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 10
>>> prim.set_joint_efforts(np.array([10, 10]), joint_indices=np.array([7, 8]))
```

set_joint_positions(
positions:ndarray,
joint_indices:List|ndarray|None =None,
)→None Set the articulation joint positions
Warning
This method will immediately set (teleport) the affected joints to the indicated value. Use the `apply_action` method to control robot joints.
Parameters:

- positions (np.ndarray) – articulation joint positions

- joint_indices (Optional[Union[list, np.ndarray]], optional) – indices to specify which joints to manipulate. Defaults to None (all joints)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the robot joints
>>> prim.set_joint_positions(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]))
>>>
>>> # set only the fingers in closed position: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> prim.set_joint_positions(np.array([0.04, 0.04]), joint_indices=np.array([7, 8]))
```

set_joint_velocities(
velocities:ndarray,
joint_indices:List|ndarray|None =None,
)→None Set the articulation joint velocities
Warning
This method will immediately set the affected joints to the indicated value. Use the `apply_action` method to control robot joints.
Parameters:

- velocities (np.ndarray) – articulation joint velocities

- joint_indices (Optional[Union[list, np.ndarray]], optional) – indices to specify which joints to manipulate. Defaults to None (all joints)

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the robot joint velocities to 0.0
>>> prim.set_joint_velocities(np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
>>>
>>> # set only the fingers velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8) to -0.01
>>> prim.set_joint_velocities(np.array([-0.01, -0.01]), joint_indices=np.array([7, 8]))
```

set_joints_default_state(
positions:ndarray|None =None,
velocities:ndarray|None =None,
efforts:ndarray|None =None,
)→None Set the joint default states (positions, velocities and/or efforts) to be applied after each reset.
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- positions (Optional[np.ndarray], optional) – joint positions. Defaults to None.

- velocities (Optional[np.ndarray], optional) – joint velocities. Defaults to None.

- efforts (Optional[np.ndarray], optional) – joint efforts. Defaults to None.

Example:

```
>>> # configure default joint states
>>> prim.set_joints_default_state(
... positions=np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]),
... velocities=np.zeros(shape=(prim.num_dof,)),
... efforts=np.zeros(shape=(prim.num_dof,))
... )
>>>
>>> # set default states during post-reset
>>> prim.post_reset()
```

set_linear_velocity(velocity:ndarray)→None
Set the linear velocity of the root articulation prim
Warning
This method will immediately set the articulation state
Parameters:
velocity (np.ndarray) – 3D linear velocity vector. Shape (3,).

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_linear_velocity`, `set_angular_velocity`, `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> prim.set_linear_velocity(np.array([0.1, 0.0, 0.0]))
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

set_local_scale(scale:Sequence[float]|None )→None
Set prim’s scale with respect to the local frame (the prim’s parent frame).
Parameters:
scale (Optional[Sequence[float]]) – scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

Example:

```
>>> # scale prim 10 times smaller
>>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
```

set_sleep_threshold(threshold:float)→None
Set the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Parameters:
threshold (float) – sleep threshold

Example:

```
>>> prim.set_sleep_threshold(0.01)
```

set_solver_position_iteration_count(count:int)→None
Set the solver (position) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
Parameters:
count (int) – position iteration count

Example:

```
>>> prim.set_solver_position_iteration_count(64)
```

set_solver_velocity_iteration_count(count:int)
Set the solver (velocity) iteration count for the articulation
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
Parameters:
count (int) – velocity iteration count

Example:

```
>>> prim.set_solver_velocity_iteration_count(64)
```

set_stabilization_threshold(threshold:float)→None
Set the mass-normalized kinetic energy below which the articulation may participate in stabilization
Search for Stabilization Threshold in PhysX docs for more details
Parameters:
threshold (float) – stabilization threshold

Example:

```
>>> prim.set_stabilization_threshold(0.005)
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

set_world_velocity(velocity:ndarray)
Set the articulation root velocity
Parameters:
velocity (np.ndarray) – linear and angular velocity to set the root prim to. Shape (6,).

propertydof_names:List[str]
List of prim names for each DOF.
Returns:
prim names

Return type:
list(string)

Example:

```
>>> prim.dof_names
['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5',
'panda_joint6', 'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']
```

propertydof_properties:ndarray
Articulation DOF properties

[TABLE]
Index | Property name | Description
0 | type | DOF type: invalid/unknown/uninitialized (0), rotation (1), translation (2)
1 | hasLimits | Whether the DOF has limits
2 | lower | Lower DOF limit (in radians or meters)
3 | upper | Upper DOF limit (in radians or meters)
4 | driveMode | Drive mode for the DOF: force (1), acceleration (2)
5 | maxVelocity | Maximum DOF velocity. In radians/s, or stage_units/s
6 | maxEffort | Maximum DOF effort. In N or N*stage_units
7 | stiffness | DOF stiffness
8 | damping | DOF damping
[/TABLE]
Returns:
named NumPy array of shape (num_dof, 9)

Return type:
np.ndarray

Example:

```
>>> # get properties for all DOFs
>>> prim.dof_properties
[(1, True, -2.8973, 2.8973, 1, 1.0000000e+01, 5220., 60000., 3000.)
(1, True, -1.7628, 1.7628, 1, 1.0000000e+01, 5220., 60000., 3000.)
(1, True, -2.8973, 2.8973, 1, 5.9390470e+36, 5220., 60000., 3000.)
(1, True, -3.0718, -0.0698, 1, 5.9390470e+36, 5220., 60000., 3000.)
(1, True, -2.8973, 2.8973, 1, 5.9390470e+36, 720., 25000., 3000.)
(1, True, -0.0175, 3.7525, 1, 5.9390470e+36, 720., 15000., 3000.)
(1, True, -2.8973, 2.8973, 1, 1.0000000e+01, 720., 5000., 3000.)
(2, True, 0. , 0.04 , 1, 3.4028235e+38, 720., 6000., 1000.)
(2, True, 0. , 0.04 , 1, 3.4028235e+38, 720., 6000., 1000.)]
>>>
>>> # property names
>>> prim.dof_properties.dtype.names
('type', 'hasLimits', 'lower', 'upper', 'driveMode', 'maxVelocity', 'maxEffort', 'stiffness', 'damping')
>>>
>>> # get DOF upper limits
>>> prim.dof_properties["upper"]
[ 2.8973 1.7628 2.8973 -0.0698 2.8973 3.7525 2.8973 0.04 0.04 ]
>>>
>>> # get the last DOF (panda_finger_joint2) upper limit
>>> prim.dof_properties["upper"][8] # or prim.dof_properties[8][3]
0.04
```

propertyhandles_initialized:bool
Check if articulation handler is initialized
Returns:
whether the handler was initialized

Return type:
bool

Example:

```
>>> prim.handles_initialized
True
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

propertynum_bodies:int
Number of articulation links
Returns:
number of links

Return type:
int

Example:

```
>>> prim.num_bodies
9
```

propertynum_dof:int
Number of DOF of the articulation
Returns:
amount of DOFs

Return type:
int

Example:

```
>>> prim.num_dof
9
```

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: USD Prim object that this object holds.

propertyprim_path:str
Returns: str: prim path in the stage

classRobotView(
prim_paths_expr:str,
name:str='rigid_prim_view',
positions:ndarray|Tensor|None =None,
translations:ndarray|Tensor|None =None,
orientations:ndarray|Tensor|None =None,
scales:ndarray|Tensor|None =None,
visibilities:ndarray|Tensor|None =None,
)Bases: Articulation
Implementation (on `Articulation` class) to deal with articulation prims as robots
This class wraps all matching articulations found at the regex provided at the `prim_paths_expr` argument
Warning
The robot (articulation) view object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Parameters:

- prim_paths_expr (str) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Franka” will match /World/Env1/Franka, /World/Env2/Franka, etc. (a non regex prim path can also be used to encapsulate one rigid prim).

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “rigid_prim_view”.

- positions (Optional[Union[np.ndarray, torch.Tensor]], optional) – default positions in the world frame of the prims. shape is (N, 3). Defaults to None, which means left unchanged.

- translations (Optional[Union[np.ndarray, torch.Tensor]], optional) – default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor]], optional) – default quaternion orientations in the world/ local frame of the prims (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (N, 4).

- scales (Optional[Union[np.ndarray, torch.Tensor]], optional) – local scales to be applied to the prim’s dimensions in the view. shape is (N, 3). Defaults to None, which means left unchanged.

- visibilities (Optional[Union[np.ndarray, torch.Tensor]], optional) – set to false for an invisible prim in the stage while rendering. shape is (N,). Defaults to None.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.cloner import GridCloner
>>> from isaacsim.core.api.robots import RobotView
>>> from pxr import UsdGeom
>>>
>>> usd_path = "/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/frankas.usd"
>>> env_zero_path = "/World/envs/env_0"
>>> num_envs = 5
>>>
>>> # load the Franka Panda robot USD file
>>> stage_utils.add_reference_to_stage(usd_path, prim_path=f"{env_zero_path}/panda") # /World/envs/env_0/panda
>>>
>>> # clone the environment (num_envs)
>>> cloner = GridCloner(spacing=1.5)
>>> cloner.define_base_env(env_zero_path)
>>> UsdGeom.Xform.Define(stage_utils.get_current_stage(), env_zero_path)
>>> cloner.clone(source_prim_path=env_zero_path, prim_paths=cloner.generate_paths("/World/envs/env", num_envs))
>>>
>>> # wrap all robots
>>> prims = RobotView(prim_paths_expr="/World/envs/env.*/panda", name="franka_panda_view")
>>> print(prims)
<isaacsim.core.api.robots.robot_view.RobotView object at 0x7f12785a5fc0>
```
apply_action(
control_actions:ArticulationActions ,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Apply joint positions (targets), velocities (targets) and/or efforts to control an articulation
Note
This method can be used instead of the separate `set_joint_position_targets`, `set_joint_velocity_targets` and `set_joint_efforts`
Parameters:

- control_actions (ArticulationActions ) – actions to be applied for next physics step.

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
High stiffness makes the joints snap faster and harder to the desired target, and higher damping smoothes but also slows down the joint’s movement to target

- For position control, set relatively high stiffness and low damping (to reduce vibrations)

- For velocity control, stiffness must be set to zero with a non-zero damping

- For effort control, stiffness and damping must be set to zero

Example:

```
>>> from isaacsim.core.utils.types import ArticulationActions
>>>
>>> # move all the articulation joints to the indicated position.
>>> # Since there are 5 envs, the joint positions are repeated 5 times
>>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
>>> action = ArticulationActions(joint_positions=positions)
>>> prims.apply_action(action)
>>>
>>> # close the robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> # for the first, middle and last of the 5 envs
>>> positions = np.tile(np.array([0.0, 0.0]), (3, 1))
>>> action = ArticulationActions(joint_positions=positions, joint_indices=np.array([7, 8]))
>>> prims.apply_action(action, indices=np.array([0, 2, 4]))
```

apply_visual_materials(
visual_materials:VisualMaterial |List[VisualMaterial ],
weaker_than_descendants:bool|List[bool]|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Apply visual material to the prims and optionally their prim descendants.
Parameters:

- visual_materials (Union[VisualMaterial , List[VisualMaterial ]]) – visual materials to be applied to the prims. Currently supports PreviewSurface, OmniPBR and OmniGlass. If a list is provided then its size has to be equal the view’s size or indices size. If one material is provided it will be applied to all prims in the view.

- weaker_than_descendants (Optional[Union[bool, List[bool]]], optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False. If a list of visual materials is provided then a list has to be provided with the same size for this arg as well.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Raises:

- Exception – length of visual materials != length of prims indexed

- Exception – length of visual materials != length of weaker descendants bools arg

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
>>> prims.apply_visual_materials(material)
```

destroy()
get_angular_velocities(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the angular velocities of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
angular velocities of the prims in the view. shape is (M, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all articulation angular velocities. Returned shape is (5, 3) for the example: 5 envs, angular (3)
>>> prims.get_angular_velocities()
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
>>>
>>> # get only the articulation angular velocities for the first, middle and last of the 5 envs
>>> # Returned shape is (5, 3) for the example: 3 envs selected, angular (3)
>>> prims.get_angular_velocities(indices=np.array([0, 2, 4]))
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
```

get_applied_actions(
clone:bool=True,
)→ArticulationActions Get the last applied actions
Parameters:
clone (bool, optional) – True to return clones of the internal buffers. Otherwise False. Defaults to True.

Returns:
current applied actions (i.e: current position targets and velocity targets)

Return type:
ArticulationActions

Example:

```
>>> # last applied action: joint_positions -> [0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04].
>>> # Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> actions = prims.get_applied_actions()
>>> actions
<isaacsim.core.utils.types.ArticulationActions object at 0x7f28af31d870>
>>> actions.joint_positions
[[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]]
>>> actions.joint_velocities
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>> actions.joint_efforts
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

get_applied_joint_efforts(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the joint efforts of articulations in the view
This method will return the efforts set by the `set_joint_efforts` method
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
joint efforts of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all applied joint efforts. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_applied_joint_efforts()
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>>
>>> # get finger applied efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_applied_joint_efforts(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[0. 0.]
[0. 0.]
[0. 0.]]
```

get_applied_visual_materials(
indices:ndarray|list|Tensor|warp.array|None =None,
)→List[VisualMaterial ]Get the current applied visual materials
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
a list of the current applied visual materials to the prims if its type is currently supported.

Return type:
List[VisualMaterial ]

Example:

```
>>> # get all applied visual materials. Returned size is 5 for the example: 5 envs
>>> prims.get_applied_visual_materials()
[<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>]
>>>
>>> # get the applied visual materials for the first, middle and last of the 5 envs. Returned size is 3
>>> prims.get_applied_visual_materials(indices=np.array([0, 2, 4]))
[<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>]
```

get_armatures(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet armatures for articulation joints in the view
Search for “Joint Armature” in PhysX docs for more details.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (Optional[bool]) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
joint armatures for articulations in the view. shape (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get joint armatures. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_armatures()
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>>
>>> # get only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) armatures
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_armatures(indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
[[0. 0.]
[0. 0.]
[0. 0.]]
```

get_articulation_body_count()→int
Get the number of rigid bodies (links) of the articulations
Returns:
maximum number of rigid bodies (links) in the articulation

Return type:
int

Example:

```
>>> prims.get_articulation_body_count()
12
```

get_body_coms(
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body center of mass (COM) of articulations in the view.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to query. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body center of mass positions and orientations of articulations in the view. Position shape is (M, K, 3), orientation shape is (M, k, 4).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all body center of mass. Returned shape is (5, 12, 3) for positions and (5, 12, 4) for orientations
>>> # for the example: 5 envs, 12 rigid bodies
>>> positions, orientations = prims.get_body_coms()
>>> positions
[[[0. 0. 0.]
[0. 0. 0.]
...
[0. 0. 0.]
[0. 0. 0.]]]
>>> orientations
[[[1. 0. 0. 0.]
[1. 0. 0. 0.]
...
[1. 0. 0. 0.]
[1. 0. 0. 0.]]]
>>>
>>> # get finger body center of mass: panda_leftfinger (10) and panda_rightfinger (11) for the first,
>>> # middle and last of the 5 envs. Returned shape is (3, 2, 3) for positions and (3, 2, 4) for orientations
>>> positions, orientations = prims.get_body_coms(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
>>> positions
[[[0. 0. 0.]
[0. 0. 0.]]
[[0. 0. 0.]
[0. 0. 0.]]
[[0. 0. 0.]
[0. 0. 0.]]]
>>> orientations
[[[1. 0. 0. 0.]
[1. 0. 0. 0.]]
[[1. 0. 0. 0.]
[1. 0. 0. 0.]]
[[1. 0. 0. 0.]
[1. 0. 0. 0.]]]
```

get_body_disable_gravity(
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet whether the rigid bodies of articulations in the view have gravity disabled or not
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to query. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body gravity activation of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_body_index(body_name:str)→int
Get a ridig body (link) index in the articulation view given its name
Parameters:
body_name (str) – name of the ridig body to query

Returns:
index of the rigid body in the articulation buffers

Return type:
int

Example:

```
>>> # get the index of the left finger: panda_leftfinger
>>> prims.get_body_index("panda_leftfinger")
10
```

get_body_inertias(
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body inertias of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to query. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body inertias of articulations in the view. Shape is (M, K, 9).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all body inertias. Returned shape is (5, 12, 9) for the example: 5 envs, 12 rigid bodies
>>> prims.get_body_inertias()
[[[1.2988697e-06 0.0 0.0 0.0 1.6535528e-06 0.0 0.0 0.0 2.0331163e-06]
[1.8686389e-06 0.0 0.0 0.0 1.4378986e-06 0.0 0.0 0.0 9.0681192e-07]
...
[4.2041304e-10 0.0 0.0 0.0 3.9026365e-10 0.0 0.0 0.0 1.3347495e-10]
[4.2041304e-10 0.0 0.0 0.0 3.9026365e-10 0.0 0.0 0.0 1.3347495e-10]]]
>>>
>>> # get finger body inertias: panda_leftfinger (10) and panda_rightfinger (11)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2, 9)
>>> prims.get_body_inertias(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
[[[4.2041304e-10 0.0 0.0 0.0 3.9026365e-10 0.0 0.0 0.0 1.3347495e-10]
[4.2041304e-10 0.0 0.0 0.0 3.9026365e-10 0.0 0.0 0.0 1.3347495e-10]]
...
[[4.2041304e-10 0.0 0.0 0.0 3.9026365e-10 0.0 0.0 0.0 1.3347495e-10]
[4.2041304e-10 0.0 0.0 0.0 3.9026365e-10 0.0 0.0 0.0 1.3347495e-10]]]
```

get_body_inv_inertias(
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body inverse inertias of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to query. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body inverse inertias of articulations in the view. Shape is (M, K, 9).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all body inverse inertias. Returned shape is (5, 12, 9) for the example: 5 envs, 12 rigid bodies
>>> prims.get_body_inv_inertias()
[[[7.6990012e+05 0.0 0.0 0.0 6.0475844e+05 0.0 0.0 0.0 4.9185578e+05]
[5.3514888e+05 0.0 0.0 0.0 6.9545931e+05 0.0 0.0 0.0 1.1027645e+06]
...
[2.3786132e+09 0.0 0.0 0.0 2.5623703e+09 0.0 0.0 0.0 7.4920422e+09]
[2.3786132e+09 0.0 0.0 0.0 2.5623703e+09 0.0 0.0 0.0 7.4920422e+09]]]
>>>
>>> # get finger body inverse inertias: panda_leftfinger (10) and panda_rightfinger (11)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2, 9)
>>> prims.get_body_inv_inertias(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
[[[2.3786132e+09 0.0 0.0 0.0 2.5623703e+09 0.0 0.0 0.0 7.4920422e+09]
[2.3786132e+09 0.0 0.0 0.0 2.5623703e+09 0.0 0.0 0.0 7.4920422e+09]]
...
[[2.3786132e+09 0.0 0.0 0.0 2.5623703e+09 0.0 0.0 0.0 7.4920422e+09]
[2.3786132e+09 0.0 0.0 0.0 2.5623703e+09 0.0 0.0 0.0 7.4920422e+09]]]
```

get_body_inv_masses(
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body inverse masses of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to query. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body inverse masses of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all body inverse masses. Returned shape is (5, 12) for the example: 5 envs, 12 rigid bodies
>>> prims.get_body_inv_masses()
[[ 0.35534042 0.42372888 0.42025304 0.37737525 0.3710848 0.33542618 0.8860687
2.4673615 10. 1.7910539 71.14793 71.14793]
[ 0.35534042 0.42372888 0.42025304 0.37737525 0.3710848 0.33542618 0.8860687
2.4673615 10. 1.7910539 71.14793 71.14793]
[ 0.35534042 0.42372888 0.42025304 0.37737525 0.3710848 0.33542618 0.8860687
2.4673615 10. 1.7910539 71.14793 71.14793]
[ 0.35534042 0.42372888 0.42025304 0.37737525 0.3710848 0.33542618 0.8860687
2.4673615 10. 1.7910539 71.14793 71.14793]
[ 0.35534042 0.42372888 0.42025304 0.37737525 0.3710848 0.33542618 0.8860687
2.4673615 10. 1.7910539 71.14793 71.14793]]
>>>
>>> # get finger body inverse masses: panda_leftfinger (10) and panda_rightfinger (11)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_body_inv_masses(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
[[71.14793 71.14793]
[71.14793 71.14793]
[71.14793 71.14793]]
```

get_body_masses(
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body masses of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to query. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body masses of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all body masses. Returned shape is (5, 12) for the example: 5 envs, 12 rigid bodies
>>> prims.get_body_masses()
[[2.8142028 2.3599997 2.3795187 2.6498823 2.6948018 2.981282
1.1285807 0.40529126 0.1 0.5583305 0.01405522 0.01405522]
[2.8142028 2.3599997 2.3795187 2.6498823 2.6948018 2.981282
1.1285807 0.40529126 0.1 0.5583305 0.01405522 0.01405522]
[2.8142028 2.3599997 2.3795187 2.6498823 2.6948018 2.981282
1.1285807 0.40529126 0.1 0.5583305 0.01405522 0.01405522]
[2.8142028 2.3599997 2.3795187 2.6498823 2.6948018 2.981282
1.1285807 0.40529126 0.1 0.5583305 0.01405522 0.01405522]
[2.8142028 2.3599997 2.3795187 2.6498823 2.6948018 2.981282
1.1285807 0.40529126 0.1 0.5583305 0.01405522 0.01405522]]
>>>
>>> # get finger body masses: panda_leftfinger (10) and panda_rightfinger (11)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_body_masses(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
[[0.01405522 0.01405522]
[0.01405522 0.01405522]
[0.01405522 0.01405522]]
```

get_coriolis_and_centrifugal_forces(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the Coriolis and centrifugal forces (joint DOF forces required to counteract Coriolis and centrifugal forces for the given articulation state) of articulations in the view
Search for Coriolis and Centrifugal Forces in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs for fixed-based arituclations and K <= num of dofs + 6 for floating-based articulations. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
Coriolis and centrifugal forces of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all coriolis and centrifugal forces. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs for a fixed-based articulation
>>> prims.get_coriolis_and_centrifugal_forces()
[[ 1.6842524e-06 -1.8269569e-04 5.2162073e-07 -9.7677548e-05 3.0365106e-07
6.7375149e-06 6.1105780e-08 -4.6237556e-06 -4.1627968e-06]
[ 1.6842524e-06 -1.8269569e-04 5.2162073e-07 -9.7677548e-05 3.0365106e-07
6.7375149e-06 6.1105780e-08 -4.6237556e-06 -4.1627968e-06]
[ 1.6842561e-06 -1.8269687e-04 5.2162375e-07 -9.7677454e-05 3.0365084e-07
6.7375931e-06 6.1106007e-08 -4.6237533e-06 -4.1627954e-06]
[ 1.6842561e-06 -1.8269687e-04 5.2162375e-07 -9.7677454e-05 3.0365084e-07
6.7375931e-06 6.1106007e-08 -4.6237533e-06 -4.1627954e-06]
[ 1.6842524e-06 -1.8269569e-04 5.2162073e-07 -9.7677548e-05 3.0365106e-07
6.7375149e-06 6.1105780e-08 -4.6237556e-06 -4.1627968e-06]]
>>>
>>> # get finger joint coriolis and centrifugal forces: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_coriolis_and_centrifugal_forces(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[-4.6237556e-06 -4.1627968e-06]
[-4.6237533e-06 -4.1627954e-06]
[-4.6237556e-06 -4.1627968e-06]]
```

get_default_state()→XFormPrimViewState
Get the default states (positions and orientations) defined with the `set_default_state` method
Returns:
returns the default state of the prims that is used after each reset.

Return type:
XFormPrimViewState

Example:

```
>>> state = prims.get_default_state()
>>> state
<isaacsim.core.utils.types.XFormPrimViewState object at 0x7f82f73e3070>
>>> state.positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> state.orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
```

get_dof_index(dof_name:str)→int
Get a DOF index in the joint buffers given its name
Parameters:
dof_name (str) – name of the joint that corresponds to the degree of freedom to query

Returns:
index of the degree of freedom in the joint buffers

Return type:
int

Example:

```
>>> # get the index of the left finger joint: panda_finger_joint1
>>> prims.get_dof_index("panda_finger_joint1")
7
```

get_dof_limits()→ndarray|Tensor
Get the articulations DOFs limits (lower and upper)
Returns:
degrees of freedom position limits. Shape is (N, num_dof, 2). For the last dimension, index 0 corresponds to lower limits and index 1 corresponds to upper limits

Return type:
Union[np.ndarray, torch.Tensor, wp.array]

Example:

```
>>> # get DOF limits. Returned shape is (5, 9, 2) for the example: 5 envs, 9 DOFs
>>> prims.get_dof_limits()
[[[-2.8973 2.8973]
[-1.7628 1.7628]
[-2.8973 2.8973]
[-3.0718 -0.0698]
[-2.8973 2.8973]
[-0.0175 3.7525]
[-2.8973 2.8973]
[ 0. 0.04 ]
[ 0. 0.04 ]]
...
[[-2.8973 2.8973]
[-1.7628 1.7628]
[-2.8973 2.8973]
[-3.0718 -0.0698]
[-2.8973 2.8973]
[-0.0175 3.7525]
[-2.8973 2.8973]
[ 0. 0.04 ]
[ 0. 0.04 ]]]
```

get_dof_types(
dof_names:List[str]=None,
)→List[str]Get the DOF types given the DOF names
Parameters:
dof_names (List[str], optional) – names of the joints that corresponds to the degrees of freedom to query. Defaults to None.

Returns:
types of the joints that corresponds to the degrees of freedom. Types can be invalid, translation or rotation.

Return type:
List[str]

Example:

```
>>> # get all DOF types
>>> prims.get_dof_types()
[<DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
<DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
<DofType.Rotation: 0>, <DofType.Translation: 1>, <DofType.Translation: 1>]
>>>
>>> # get only the finger DOF types: panda_finger_joint1 and panda_finger_joint2
>>> prims.get_dof_types(dof_names=["panda_finger_joint1", "panda_finger_joint2"])
[<DofType.Translation: 1>, <DofType.Translation: 1>]
```

get_drive_types()→ndarray|Tensor
Get the articulations DOFs limits (lower and upper)
Returns:
degrees of freedom position limits. Shape is (N, num_dof). For the last dimension, index 0 corresponds to lower limits and index 1 corresponds to upper limits

Return type:
Union[np.ndarray, torch.Tensor, wp.array]

get_effort_modes(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→List[str]Get effort modes for articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Returns:
Returns a List of size (M, K) indicating the effort modes: `acceleration` or `force`

Return type:
List

Example:

```
>>> # get the effort mode for all joints
>>> prims.get_effort_modes()
[['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration']]
>>>
>>> # get only the finger joints effort modes for the first, middle and last of the 5 envs
>>> prims.get_effort_modes(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[['acceleration', 'acceleration'], ['acceleration', 'acceleration'], ['acceleration', 'acceleration']]
```

get_enabled_self_collisions(
indices:ndarray|List|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet the enable self collisions flag (`physxArticulation:enabledSelfCollisions`) for all articulations
Parameters:
indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
self collisions flags (boolean interpreted as int). shape (M,)

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all self collisions flags. Returned shape is (5,) for the example: 5 envs
>>> prims.get_enabled_self_collisions()
[0 0 0 0 0]
>>>
>>> # get the self collisions flags for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_enabled_self_collisions(indices=np.array([0, 2, 4]))
[0 0 0]
```

get_fixed_tendon_dampings(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the dampings of fixed tendons for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
fixed tendon dampings of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the fixed tendon dampings
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> prims.get_fixed_tendon_dampings()
[[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]]
```

get_fixed_tendon_limit_stiffnesses(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the limit stiffness of fixed tendons for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
fixed tendon stiffnesses of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the fixed tendon limit stiffnesses
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> prims.get_fixed_tendon_limit_stiffnesses()
[[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]]
```

get_fixed_tendon_limits(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the limits of fixed tendons for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
fixed tendon stiffnesses of articulations in the view. Shape is (M, K, 2).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the fixed tendon limits
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> prims.get_fixed_tendon_limits()
[[[-0.001 0.001] [-0.001 0.001] [-0.001 0.001] [-0.001 0.001]]
[[-0.001 0.001] [-0.001 0.001] [-0.001 0.001] [-0.001 0.001]]
[[-0.001 0.001] [-0.001 0.001] [-0.001 0.001] [-0.001 0.001]]
[[-0.001 0.001] [-0.001 0.001] [-0.001 0.001] [-0.001 0.001]]
[[-0.001 0.001] [-0.001 0.001] [-0.001 0.001] [-0.001 0.001]]]
```

get_fixed_tendon_offsets(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the offsets of fixed tendons for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
fixed tendon stiffnesses of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the fixed tendon offsets
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> prims.get_fixed_tendon_offsets()
[[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]]
```

get_fixed_tendon_rest_lengths(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the rest length of fixed tendons for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
fixed tendon stiffnesses of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the fixed tendon rest lengths
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> prims.get_fixed_tendon_rest_lengths()
[[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]]
```

get_fixed_tendon_stiffnesses(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the stiffness of fixed tendons for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
fixed tendon stiffnesses of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the fixed tendon stiffnesses
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> prims.get_fixed_tendon_stiffnesses()
[[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]
[0. 0. 0. 0.]]
```

get_friction_coefficients(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.arrayGet the friction coefficients for the articulation joints in the view
Search for “Joint Friction Coefficient” in PhysX docs for more details.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (Optional[bool]) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
joint friction coefficients for articulations in the view. shape (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get joint friction coefficients. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_friction_coefficients()
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>>
>>> # get only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) friction coefficients
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_friction_coefficients(indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
[[0. 0.]
[0. 0.]
[0. 0.]]
```

get_gains(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→Tuple[ndarray|Tensor,ndarray|Tensor,warp.indexedarray|warp.index]Get the implicit Proportional-Derivative (PD) controller’s Kps (stiffnesses) and Kds (dampings) of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return clones of the internal buffers. Otherwise False. Defaults to True.

Returns:
stiffness and damping of articulations in the view respectively. shapes are (M, K).

Return type:
Tuple[Union[np.ndarray, torch.Tensor], Union[np.ndarray, torch.Tensor], Union[wp.indexedarray, wp.index]]

Example:

```
>>> # get all joint stiffness and damping. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> stiffnesses, dampings = prims.get_gains()
>>> stiffnesses
[[60000. 60000. 60000. 60000. 25000. 15000. 5000. 6000. 6000.]
[60000. 60000. 60000. 60000. 25000. 15000. 5000. 6000. 6000.]
[60000. 60000. 60000. 60000. 25000. 15000. 5000. 6000. 6000.]
[60000. 60000. 60000. 60000. 25000. 15000. 5000. 6000. 6000.]
[60000. 60000. 60000. 60000. 25000. 15000. 5000. 6000. 6000.]]
>>> dampings
[[3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
[3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
[3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
[3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
[3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]]
>>>
>>> # get finger joints stiffness and damping: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> stiffnesses, dampings = prims.get_gains(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
>>> stiffnesses
[[6000. 6000.]
[6000. 6000.]
[6000. 6000.]]
>>> dampings
[[1000. 1000.]
[1000. 1000.]
[1000. 1000.]]
```

get_generalized_gravity_forces(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the generalized gravity forces (joint DOF forces required to counteract gravitational forces for the given articulation pose) of articulations in the view
Search for Generalized Gravity Force in PhysX docs for more details
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs for fixed-based arituclations and K <= num of dofs + 6 for floating-based articulations. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
generalized gravity forces of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>>

>>> # get all generalized gravity forces. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_generalized_gravity_forces()
[[ 1.32438602e-08 -6.90832138e+00 -1.08629465e-05 1.91585541e+01 5.13810664e-06
1.18674076e+00 8.01788883e-06 5.18786255e-03 -5.18784765e-03]
[ 1.32438602e-08 -6.90832138e+00 -1.08629465e-05 1.91585541e+01 5.13810664e-06
1.18674076e+00 8.01788883e-06 5.18786255e-03 -5.18784765e-03]
[ 1.32438585e-08 -6.90830994e+00 -1.08778477e-05 1.91585541e+01 5.14090061e-06
1.18674052e+00 8.02161412e-06 5.18786255e-03 -5.18784765e-03]
[ 1.32438585e-08 -6.90830994e+00 -1.08778477e-05 1.91585541e+01 5.14090061e-06
1.18674052e+00 8.02161412e-06 5.18786255e-03 -5.18784765e-03]
[ 1.32438602e-08 -6.90832138e+00 -1.08629465e-05 1.91585541e+01 5.13810664e-06
1.18674076e+00 8.01788883e-06 5.18786255e-03 -5.18784765e-03]]
>>>
>>> # get finger joint generalized gravity forces: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_generalized_gravity_forces(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[ 0.00518786 -0.00518785]
[ 0.00518786 -0.00518785]
[ 0.00518786 -0.00518785]]
```

get_jacobian_shape()→ndarray|Tensor|warp.array
Get the Jacobian matrix shape of a single articulation
The Jacobian matrix maps the joint space velocities of a DOF to it’s cartesian and angular velocities
The shape of the Jacobian depends on the number of links (rigid bodies), DOFs, and whether the articulation base is fixed (e.g., robotic manipulators) or not (e.g,. mobile robots).

- Fixed articulation base: `(num_bodies - 1, 6, num_dof)`

- Non-fixed articulation base: `(num_bodies, 6, num_dof + 6)`

Each body has 6 values in the Jacobian representing its linear and angular motion along the three coordinate axes. The extra 6 DOFs in the last dimension, for non-fixed base cases, correspond to the linear and angular degrees of freedom of the free root link
Returns:
shape of jacobian for a single articulation.

Return type:
Union[np.ndarray, torch.Tensor, wp.array]

Example:

```
>>> # for the Franka Panda (a robotic manipulator with fixed base):
>>> # - num_bodies: 12
>>> # - num_dof: 9
>>> prims.get_jacobian_shape()
(11, 6, 9)
```

get_jacobians(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the Jacobian matrices of articulations in the view
Note
The first dimension corresponds to the amount of wrapped articulations while the last 3 dimensions are the Jacobian matrix shape. Refer to the `get_jacobian_shape` method for details about the Jacobian matrix shape
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
Jacobian matrices of articulations in the view. Shape is (M, jacobian_shape).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the Jacobian matrices. Returned shape is (5, 11, 6, 9) for the example: 5 envs, 12 links, 9 DOFs
>>> prims.get_jacobians()
[[[[ 4.2254178e-09 0.0000000e+00 0.0000000e+00 ... 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 1.2093576e-08 0.0000000e+00 0.0000000e+00 ... 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[-6.0873992e-16 0.0000000e+00 0.0000000e+00 ... 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 1.4458647e-07 0.0000000e+00 0.0000000e+00 ... 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[-1.8178657e-10 0.0000000e+00 0.0000000e+00 ... 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 9.9999976e-01 0.0000000e+00 0.0000000e+00 ... 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
...
[[-4.5089945e-02 8.1210062e-02 -3.8495898e-02 ... 2.8108317e-02 0.0000000e+00 -4.9317405e-02]
[ 4.2863289e-01 9.7436900e-04 4.0475106e-01 ... 2.4577195e-03 0.0000000e+00 9.9807423e-01]
[ 6.5973169e-09 -4.2914307e-01 -2.1542320e-02 ... 2.8352857e-02 0.0000000e+00 -3.7625343e-02]
[ 1.4458647e-07 -1.1999309e-02 -5.3927803e-01 ... 7.0976764e-01 0.0000000e+00 0.0000000e+00]
[-1.8178657e-10 9.9992776e-01 -6.4710006e-03 ... 8.5178167e-03 0.0000000e+00 0.0000000e+00]
[ 9.9999976e-01 -3.8743019e-07 8.4210289e-01 ... -7.0438433e-01 0.0000000e+00 0.0000000e+00]]]]
```

get_joint_index(joint_name:str)→int
Get a joint index in the joint buffers given its name
Parameters:
joint_name (str) – name of the joint that corresponds to the index of the joint in the articulation

Returns:
index of the joint in the joint buffers

Return type:
int

get_joint_max_velocities(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the maximum joint velocities for articulation dofs in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (Optional[bool]) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
maximum joint velocities for articulations dofs in the view. shape (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_joint_positions(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the joint positions of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
joint positions of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all joint positions. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_joint_positions()
[[ 1.1999921e-02 -5.6962633e-01 1.3219320e-08 -2.8105433e+00 6.8276213e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3219320e-08 -2.8105433e+00 6.8276213e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3220056e-08 -2.8105433e+00 6.8276104e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3220056e-08 -2.8105433e+00 6.8276104e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3219320e-08 -2.8105433e+00 6.8276213e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]]
>>>
>>> # get finger joint positions: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_joint_positions(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[0.03991237 0.04 ]
[0.03991237 0.04 ]
[0.03991237 0.04 ]]
```

get_joint_velocities(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the joint velocities of articulations in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
joint velocities of articulations in the view. Shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all joint velocities. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_joint_velocities()
[[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07 1.1063669e-02 -4.6333633e-05
3.4824573e-02 8.8469200e-02 5.4033857e-04 1.0287426e-05]
[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07 1.1063669e-02 -4.6333633e-05
3.4824573e-02 8.8469200e-02 5.4033857e-04 1.0287426e-05]
[ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07 1.1063648e-02 -4.6333400e-05
3.4824558e-02 8.8469170e-02 5.4033566e-04 1.0287110e-05]
[ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07 1.1063648e-02 -4.6333400e-05
3.4824558e-02 8.8469170e-02 5.4033566e-04 1.0287110e-05]
[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07 1.1063669e-02 -4.6333633e-05
3.4824573e-02 8.8469200e-02 5.4033857e-04 1.0287426e-05]]
>>>
>>> # get finger joint velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_joint_velocities(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[5.4033857e-04 1.0287426e-05]
[5.4033566e-04 1.0287110e-05]
[5.4033857e-04 1.0287426e-05]]
```

get_joints_default_state()→JointsState
Get the default joint states defined with the `set_joints_default_state` method
Returns:
an object that contains the default joint states

Return type:
JointsState

Example:

```
>>> # returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> states = prims.get_joints_default_state()
>>> states
<isaacsim.core.utils.types.JointsState object at 0x7fc2c174fd90>
>>> states.positions
[[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]
[ 0. -1. 0. -2.2 0. 2.4 0.8 0.04 0.04]]
>>> states.velocities
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>> states.efforts
[[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0.]]
```

get_joints_state()→JointsState
Get the current joint states (positions and velocities)
Returns:
an object that contains the current joint positions and velocities

Return type:
JointsState

Example:

```
>>> # returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> states = prims.get_joints_state()
>>> states
<isaacsim.core.utils.types.JointsState object at 0x7fc1a23a82e0>
>>> states.positions
[[ 1.1999921e-02 -5.6962633e-01 1.3219320e-08 -2.8105433e+00 6.8276213e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3219320e-08 -2.8105433e+00 6.8276213e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3220056e-08 -2.8105433e+00 6.8276104e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3220056e-08 -2.8105433e+00 6.8276104e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]
[ 1.1999921e-02 -5.6962633e-01 1.3219320e-08 -2.8105433e+00 6.8276213e-06
3.0301569e+00 7.3234755e-01 3.9912373e-02 3.9999999e-02]]
>>> states.velocities
[[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07 1.1063669e-02 -4.6333633e-05
3.4824573e-02 8.8469200e-02 5.4033857e-04 1.0287426e-05]
[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07 1.1063669e-02 -4.6333633e-05
3.4824573e-02 8.8469200e-02 5.4033857e-04 1.0287426e-05]
[ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07 1.1063648e-02 -4.6333400e-05
3.4824558e-02 8.8469170e-02 5.4033566e-04 1.0287110e-05]
[ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07 1.1063648e-02 -4.6333400e-05
3.4824558e-02 8.8469170e-02 5.4033566e-04 1.0287110e-05]
[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07 1.1063669e-02 -4.6333633e-05
3.4824573e-02 8.8469200e-02 5.4033857e-04 1.0287426e-05]]
```

get_linear_velocities(
indices:ndarray|list|Tensor|warp.array|None =None,
clone=True,
)→ndarray|Tensor|warp.indexedarrayGet the linear velocities of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
linear velocities of the prims in the view. shape is (M, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all articulation linear velocities. Returned shape is (5, 3) for the example: 5 envs, linear (3)
>>> prims.get_linear_velocities()
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
>>>
>>> # get only the articulation linear velocities for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 3) for the example: 3 envs selected, linear (3)
>>> prims.get_linear_velocities(indices=np.array([0, 2, 4]))
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
```

get_link_index(link_name:str)→int
Get a link index in the link buffers given its name
Parameters:
link_name (str) – name of the link that corresponds to the index of the link in the articulation

Returns:
index of the link in the link buffers

Return type:
int

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame).
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

Returns:
first index is positions in the local frame of the prims. shape is (M, 3). Second index is quaternion orientations in the local frame of the prims. Quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all articulation poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[ 0.0000000e+00 0.0000000e+00 -2.8610229e-08]
[ 0.0000000e+00 0.0000000e+00 -2.8610229e-08]
[-4.5299529e-08 0.0000000e+00 -2.8610229e-08]
[-4.5299529e-08 0.0000000e+00 -2.8610229e-08]
[ 0.0000000e+00 0.0000000e+00 -2.8610229e-08]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the articulation poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 0.0000000e+00 0.0000000e+00 -2.8610229e-08]
[-4.5299529e-08 0.0000000e+00 -2.8610229e-08]
[ 0.0000000e+00 0.0000000e+00 -2.8610229e-08]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
```

get_local_scales(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet prim scales in the view with respect to the local frame (the parent’s frame).
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
scales applied to the prim’s dimensions in the local frame. shape is (M, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all prims scales with respect to the local frame.
>>> # Returned shape is (5, 3) for the example: 5 envs
>>> prims.get_local_scales()
[[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]]
>>>
>>> # get only the prims scales with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 3) for the example: 3 envs selected
>>> prims.get_local_scales(indices=np.array([0, 2, 4]))
[[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]]
```

get_mass_matrices(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the mass matrices of articulations in the view
Note
The first dimension corresponds to the amount of wrapped articulations while the last 2 dimensions are the mass matrix shape. Refer to the `get_mass_matrix_shape` method for details about the mass matrix shape
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
mass matrices of articulations in the view. Shape is (M, mass_matrix_shape).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the mass matrices. Returned shape is (5, 9, 9) for the example: 5 envs, 9 DOFs for a fixed-based articulation
>>> prims.get_mass_matrices()
[[[ 5.0900602e-01 1.1794259e-06 4.2570841e-01 -1.6387942e-06 -3.1573933e-02
-1.9736715e-06 -3.1358242e-04 -6.0441834e-03 6.0441834e-03]
[ 1.1794259e-06 1.0598221e+00 7.4729815e-07 -4.2621672e-01 2.3612277e-08
-4.9647894e-02 -2.9080724e-07 -1.8432185e-04 1.8432130e-04]
...
[-6.0441834e-03 -1.8432185e-04 -5.7159867e-03 4.0070520e-04 9.6930371e-04
1.2324301e-04 2.5264668e-10 1.4055224e-02 0.0000000e+00]
[ 6.0441834e-03 1.8432130e-04 5.7159867e-03 -4.0070404e-04 -9.6930366e-04
-1.2324269e-04 -3.6906206e-10 0.0000000e+00 1.4055224e-02]]]
```

get_mass_matrix_shape()→ndarray|Tensor|warp.array
Get the mass matrix shape of a single articulation
The mass matrix contains the generalized mass of the robot depending on the current configuration
The shape of the max matrix depends on the number of DOFs as well as whether the articulation is fixed-base or floating-base. For fixed-base articulation the shape is `(num_dof, num_dof)` while for floating-base articulation the shape is `(num_dof + 6, num_dof + 6)`
Returns:
shape of mass matrix for a single articulation.

Return type:
Union[np.ndarray, torch.Tensor, wp.array]

Example:

```
>>> # for the Franka Panda:
>>> # - num_dof: 9
>>> prims.get_mass_matrix_shape()
(9, 9)
>>> # for Ant robot:
>>> # - num_dof: 8
>>> prims.get_mass_matrix_shape()
(14, 14)
```

get_max_efforts(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the maximum efforts for articulation in the view
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (Optional[bool]) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
maximum efforts for articulations in the view. shape (M, K).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all joint maximum efforts. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_max_efforts()
[[5220. 5220. 5220. 5220. 720. 720. 720. 720. 720.]
[5220. 5220. 5220. 5220. 720. 720. 720. 720. 720.]
[5220. 5220. 5220. 5220. 720. 720. 720. 720. 720.]
[5220. 5220. 5220. 5220. 720. 720. 720. 720. 720.]
[5220. 5220. 5220. 5220. 720. 720. 720. 720. 720.]]
>>>
>>> # get finger joint maximum efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_max_efforts(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[720. 720.]
[720. 720.]
[720. 720.]]
```

get_measured_joint_efforts(
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayReturns the efforts computed/measured by the physics solver of the joint forces in the DOF motion direction
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – joint indices to specify which joints to query. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
computed joint efforts of articulations in the view. shape is (M, K).

Return type:
Union[np.ndarray, torch.Tensor]

Example:

```
>>> # get all measured joint efforts. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
>>> prims.get_measured_joint_efforts()
[[ 4.8250298e-05 -6.9073005e+00 5.3364405e-05 1.9157070e+01 -5.8759182e-05
1.1863427e+00 -5.6388220e-05 5.1680300e-03 -5.1910817e-03]
[ 4.8250298e-05 -6.9073005e+00 5.3364405e-05 1.9157070e+01 -5.8759182e-05
1.1863427e+00 -5.6388220e-05 5.1680300e-03 -5.1910817e-03]
[ 4.8254540e-05 -6.9072919e+00 5.3344327e-05 1.9157072e+01 -5.8761045e-05
1.1863427e+00 -5.6405144e-05 5.1680212e-03 -5.1910840e-03]
[ 4.8254540e-05 -6.9072919e+00 5.3344327e-05 1.9157072e+01 -5.8761045e-05
1.1863427e+00 -5.6405144e-05 5.1680212e-03 -5.1910840e-03]
[ 4.8250298e-05 -6.9073005e+00 5.3364405e-05 1.9157070e+01 -5.8759182e-05
1.1863427e+00 -5.6388220e-05 5.1680300e-03 -5.1910817e-03]]
>>>
>>> # get finger measured joint efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
>>> prims.get_measured_joint_efforts(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
[[ 0.00516803 -0.00519108]
[ 0.00516802 -0.00519108]
[ 0.00516803 -0.00519108]]
```

get_measured_joint_forces(
indices:ndarray|List|Tensor|None =None,
joint_indices:ndarray|List|Tensor|None =None,
joint_names:List[str]|None =None,
clone:bool=True,
)→ndarray|TensorGet the measured joint reaction forces and torques (link incoming joint forces and torques) to external loads.
Forces and torques are reported in the local body reference frame (child joint frame of the link’s incoming joint).
Note
Since the name->index map for joints has not been exposed yet, it is possible to access the joint names and their indices through the articulation metadata.

```
prims._metadata.joint_names # list of names
prims._metadata.joint_indices # dict of name: index
```
To retrieve a specific row for the link incoming joint force/torque use `joint_index + 1` when specifying the `joint_indices` parameter. For the `joint_names` parameter, the conversion is done internally.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – link indices to specify which link’s incoming joints to query. Shape (K,). Where K <= num of links/bodies. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
joint forces and torques of articulations in the view. Shape is (M, num_joint + 1, 6). Column index 0 is the incoming joint of the base link. For the last dimension the first 3 values are for forces and the last 3 for torques

Return type:
Union[np.ndarray, torch.Tensor]

Example:

```
>>> # get all measured joint forces and torques. Returned shape is (5, 12, 6) for the example:
>>> # 5 envs, 9 DOFs (but 12 joints including the fixed and root joints)
>>> prims.get_measured_joint_forces()
[[[ 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00]
[ 1.49950760e+02 3.52353277e-06 5.62586996e-04 4.82502983e-05 -6.90729856e+00 2.69259126e-05]
[-2.60467059e-05 -1.06778236e+02 -6.83844986e+01 -6.90730047e+00 -5.27759657e-05 -1.24897576e-06]
[ 8.71209946e+01 -4.46646191e-05 -5.57951622e+01 5.33644052e-05 -2.45385647e+01 1.38957939e-05]
[ 5.18576926e-05 -4.81099091e+01 6.07092705e+01 1.91570702e+01 -5.81023924e-05 1.46875891e-06]
[-3.16910419e+01 2.31799815e-04 3.99901695e+01 -5.87591821e-05 -1.18634319e+00 2.24427877e-05]
[-1.07621672e-04 1.53405371e+01 -1.54584875e+01 1.18634272e+00 6.09036942e-05 -1.60679410e-05]
[-7.54189777e+00 -5.08146524e+00 -5.65130091e+00 -5.63882204e-05 3.88599992e-01 -3.49432468e-01]
[ 4.74214745e+00 -3.19458222e+00 3.55281782e+00 5.58562024e-05 8.47946014e-03 7.64050474e-03]
[ 4.07607269e+00 2.16406956e-01 -4.05131817e+00 -5.95658377e-04 1.14070829e-02 2.13965313e-06]
[ 5.16803004e-03 -9.77545828e-02 -9.70939621e-02 -8.41282599e-12 -1.29066744e-12 -1.93477560e-11]
[-5.19108167e-03 9.75882635e-02 -9.71064270e-02 8.41282859e-12 1.29066018e-12 -1.93477543e-11]]
...
[[ 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00]
[ 1.49950760e+02 3.52353277e-06 5.62586996e-04 4.82502983e-05 -6.90729856e+00 2.69259126e-05]
[-2.60467059e-05 -1.06778236e+02 -6.83844986e+01 -6.90730047e+00 -5.27759657e-05 -1.24897576e-06]
[ 8.71209946e+01 -4.46646191e-05 -5.57951622e+01 5.33644052e-05 -2.45385647e+01 1.38957939e-05]
[ 5.18576926e-05 -4.81099091e+01 6.07092705e+01 1.91570702e+01 -5.81023924e-05 1.46875891e-06]
[-3.16910419e+01 2.31799815e-04 3.99901695e+01 -5.87591821e-05 -1.18634319e+00 2.24427877e-05]
[-1.07621672e-04 1.53405371e+01 -1.54584875e+01 1.18634272e+00 6.09036942e-05 -1.60679410e-05]
[-7.54189777e+00 -5.08146524e+00 -5.65130091e+00 -5.63882204e-05 3.88599992e-01 -3.49432468e-01]
[ 4.74214745e+00 -3.19458222e+00 3.55281782e+00 5.58562024e-05 8.47946014e-03 7.64050474e-03]
[ 4.07607269e+00 2.16406956e-01 -4.05131817e+00 -5.95658377e-04 1.14070829e-02 2.13965313e-06]
[ 5.16803004e-03 -9.77545828e-02 -9.70939621e-02 -8.41282599e-12 -1.29066744e-12 -1.93477560e-11]
[-5.19108167e-03 9.75882635e-02 -9.71064270e-02 8.41282859e-12 1.29066018e-12 -1.93477543e-11]]]
>>>
>>> # get measured joint forces and torques for the fingers for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 2, 6)
>>> metadata = prims._metadata
>>> joint_indices = 1 + np.array([
>>> metadata.joint_indices["panda_finger_joint1"],
>>> metadata.joint_indices["panda_finger_joint2"],
>>> ])
>>> joint_indices
[10 11]
>>> prims.get_measured_joint_forces(indices=np.array([0, 2, 4]), joint_indices=joint_indices)
[[[ 5.1680300e-03 -9.7754583e-02 -9.7093962e-02 -8.4128260e-12 -1.2906674e-12 -1.9347756e-11]
[-5.1910817e-03 9.7588263e-02 -9.7106427e-02 8.4128286e-12 1.2906602e-12 -1.9347754e-11]]
[[ 5.1680212e-03 -9.7754560e-02 -9.7093947e-02 -8.4141834e-12 -1.2907383e-12 -1.9348209e-11]
[-5.1910840e-03 9.7588278e-02 -9.7106412e-02 8.4141869e-12 1.2907335e-12 -1.9348207e-11]]
[[ 5.1680300e-03 -9.7754583e-02 -9.7093962e-02 -8.4128260e-12 -1.2906674e-12 -1.9347756e-11]
[-5.1910817e-03 9.7588263e-02 -9.7106427e-02 8.4128286e-12 1.2906602e-12 -1.9347754e-11]]]
```

get_position_residuals(
indices:ndarray|list|Tensor|warp.array|None =None,
report_max:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet physics solver position residuals for articulations. This is the residual across all joints that are part of articulations.
The solver residuals are computed according to impulse variation normalized by the effective mass.

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- report_max (Optional[bool]) – whether to report max or RMS residual. Defaults to True, i.e. max criteria

Returns:
Solver residuals for rigid bodies of the view

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_sleep_thresholds(
indices:ndarray|List|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
sleep thresholds. shape (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all sleep thresholds. Returned shape is (5,) for the example: 5 envs
>>> prims.get_sleep_thresholds()
[0.005 0.005 0.005 0.005 0.005]
>>>
>>> # get the sleep thresholds for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_sleep_thresholds(indices=np.array([0, 2, 4]))
[0.005 0.005 0.005]
```

get_solver_position_iteration_counts(
indices:ndarray|List|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet the solver (position) iteration count for the articulations
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Parameters:
indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
position iteration count. Shape (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all position iteration count. Returned shape is (5,) for the example: 5 envs
>>> prims.get_solver_position_iteration_counts()
[32 32 32 32 32]
>>>
>>> # get the position iteration count for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_solver_position_iteration_counts(indices=np.array([0, 2, 4]))
[32 32 32]
```

get_solver_velocity_iteration_counts(
indices:ndarray|List|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet the solver (velocity) iteration count for the articulations
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Parameters:
indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
velocity iteration count. Shape (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all velocity iteration count. Returned shape is (5,) for the example: 5 envs
>>> prims.get_solver_velocity_iteration_counts()
[32 32 32 32 32]
>>>
>>> # get the velocity iteration count for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_solver_velocity_iteration_counts(indices=np.array([0, 2, 4]))
[32 32 32]
```

get_stabilization_thresholds(
indices:ndarray|List|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet the mass-normalized kinetic energy below which the articulations may participate in stabilization
Search for Stabilization Threshold in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
stabilization threshold. Shape (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all stabilization thresholds. Returned shape is (5,) for the example: 5 envs
>>> prims.get_solver_velocity_iteration_counts()
[0.001 0.001 0.001 0.001 0.001]
>>>
>>> # get the stabilization thresholds for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_solver_velocity_iteration_counts(indices=np.array([0, 2, 4]))
[0.001 0.001 0.001]
```

get_velocities(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the linear and angular velocities of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
linear and angular velocities of the prims in the view concatenated. shape is (M, 6). For the last dimension the first 3 values are for linear velocities and the last 3 for angular velocities

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all articulation velocities. Returned shape is (5, 6) for the example: 5 envs, linear (3) and angular (3)
>>> prims.get_velocities()
[[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]]
>>>
>>> # get only the articulation velocities for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 6) for the example: 3 envs selected, linear (3) and angular (3)
>>> prims.get_velocities(indices=np.array([0, 2, 4]))
[[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]]
```

get_velocity_residuals(
indices:ndarray|list|Tensor|warp.array|None =None,
report_max:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet physics solver velocity residuals for articulations. This is the residual across all joints that are part of articulations.
The solver residuals are computed according to impulse variation normalized by the effective mass.

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- report_max (Optional[bool]) – whether to report max or RMS residual. Defaults to True, i.e. max criteria

Returns:
Solver residuals for rigid bodies of the view

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_visibilities(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayReturns the current visibilities of the prims in stage.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
Shape (M,) with type bool, where each item holds True
if the prim is visible in stage. False otherwise.

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all visibilities. Returned shape is (5,) for the example: 5 envs
>>> prims.get_visibilities()
[ True True True True True]
>>>
>>> # get the visibilities for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_visibilities(indices=np.array([0, 2, 4]))
[ True True True]
```

get_world_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
usd:bool=True,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get the poses of the prims in the view with respect to the world’s frame.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Returns:
first index is positions in the world frame of the prims. shape is (M, 3). Second index is quaternion orientations in the world frame of the prims. Quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all articulation poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.5000000e+00 -7.5000000e-01 -2.8610229e-08]
[ 1.5000000e+00 7.5000000e-01 -2.8610229e-08]
[-4.5299529e-08 -7.5000000e-01 -2.8610229e-08]
[-4.5299529e-08 7.5000000e-01 -2.8610229e-08]
[-1.5000000e+00 -7.5000000e-01 -2.8610229e-08]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the articulation poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5000000e+00 -7.5000000e-01 -2.8610229e-08]
[-4.5299529e-08 -7.5000000e-01 -2.8610229e-08]
[-1.5000000e+00 -7.5000000e-01 -2.8610229e-08]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
```

get_world_scales(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet prim scales in the view with respect to the world’s frame
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
scales applied to the prim’s dimensions in the world frame. shape is (M, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all prims scales with respect to the world's frame.
>>> # Returned shape is (5, 3) for the example: 5 envs
>>> prims.get_world_scales()
[[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]]
>>>
>>> # get only the prims scales with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 3) for the example: 3 envs selected
>>> prims.get_world_scales(indices=np.array([0, 2, 4]))
[[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]]
```

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and set other properties using the PhysX tensor API
Note
For this particular class, calling this method will do nothing
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

Example:

```
>>> prims.initialize()
```

is_physics_handle_valid()→bool
Check if articulation view’s physics handler is initialized
Warning
If the physics handler is not valid many of the methods that requires PhysX will return None.
Returns:
False if .initialize() needs to be called again for the physics handle to be valid. Otherwise True

Return type:
bool

Example:

```
>>> prims.is_physics_handle_valid()
True
```

is_valid(
indices:ndarray|list|Tensor|warp.array|None =None,
)→boolCheck that all prims have a valid USD Prim
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
True if all prim paths specified in the view correspond to a valid prim in stage. False otherwise.

Return type:
bool

Example:

```
>>> prims.is_valid()
True
```

is_visual_material_applied(
indices:ndarray|list|Tensor|warp.array|None =None,
)→List[bool]Check if there is a visual material applied
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
True if there is a visual material applied is applied to the corresponding prim in the view. False otherwise.

Return type:
List[bool]

Example:

```
>>> # given a visual material that is applied only to the first and the last environment
>>> prims.is_visual_material_applied()
[True, False, False, False, True]
>>>
>>> # check for the first, middle and last of the 5 envs
>>> prims.is_visual_material_applied(indices=np.array([0, 2, 4]))
[True, False, True]
```

pause_motion()→None
Pauses the motion of all articulations wrapped under the Articulation.

post_reset()→None
Reset the robots to their default states
Note
For the robots, in addition to configuring the root prim’s default positions and spatial orientations (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) and the joint’s stiffness and dampings (defined via the `set_gains` method) are imposed
Example:

```
>>> prims.post_reset()
```

resume_motion()
Resumes the motion of all articulations wrapped under the Articulation using the position and velocity dof targets cached when pause_motion was called.

set_angular_velocities(
velocities:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the angular velocities of the prims in the view
The method does this through the physx API only. It has to be called after initialization. Note: This method is not supported for the gpu pipeline. `set_velocities` method should be used instead.
Warning
This method will immediately set the articulation state
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – angular velocities to set the rigid prims to. shape is (M, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`), `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set each articulation linear velocity to (0.1, 0.1, 0.1)
>>> velocities = np.full((num_envs, 3), fill_value=0.1)
>>> prims.set_angular_velocities(velocities)
>>>
>>> # set only the articulation linear velocities for the first, middle and last of the 5 envs
>>> velocities = np.full((3, 3), fill_value=0.1)
>>> prims.set_angular_velocities(velocities, indices=np.array([0, 2, 4]))
```

set_armatures(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set armatures for articulation joints in the view
Search for “Joint Armature” in PhysX docs for more details.
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – armatures for articulation joints in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Example:

```
>>> # set all joint armatures to 0.05 for all envs
>>> prims.set_armatures(np.full((num_envs, prims.num_dof), 0.05))
>>>
>>> # set only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) armatures
>>> # for the first, middle and last of the 5 envs to 0.05
>>> prims.set_armatures(np.full((3, 2), 0.05), indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
```

set_body_coms(
positions:ndarray|Tensor|warp.array=None,
orientations:ndarray|Tensor|warp.array=None,
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set body center of mass (COM) positions and orientations for articulation bodies in the view.
Parameters:

- positions (Union[np.ndarray, torch.Tensor, wp.array]) – body center of mass positions for articulations in the view. shape (M, K, 3).

- orientations (Union[np.ndarray, torch.Tensor, wp.array]) – body center of mass orientations for articulations in the view. shape (M, K, 4).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to manipulate. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

Example:

```
>>> # set the center of mass for all the articulation rigid bodies to the indicated values.
>>> # Since there are 5 envs, the inertias are repeated 5 times
>>> positions = np.tile(np.array([0.01, 0.02, 0.03]), (num_envs, prims.num_bodies, 1))
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, prims.num_bodies, 1))
>>> prims.set_body_coms(positions, orientations)
>>>
>>> # set the fingers center of mass: panda_leftfinger (10) and panda_rightfinger (11) to 0.2
>>> # for the first, middle and last of the 5 envs
>>> positions = np.tile(np.array([0.01, 0.02, 0.03]), (3, 2, 1))
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 2, 1))
>>> prims.set_body_coms(positions, orientations, indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
```

set_body_disable_gravity(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set body gravity activation articulation bodies in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – body gravity activation for articulations in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to manipulate. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

set_body_inertias(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set body inertias for articulation bodies in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – body inertias for articulations in the view. shape (M, K, 9).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to manipulate. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

Example:

```
>>> # set the inertias for all the articulation rigid bodies to the indicated values.
>>> # Since there are 5 envs, the inertias are repeated 5 times
>>> inertias = np.tile(np.array([0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]), (num_envs, prims.num_bodies, 1))
>>> prims.set_body_inertias(inertias)
>>>
>>> # set the fingers inertias: panda_leftfinger (10) and panda_rightfinger (11) to 0.2
>>> # for the first, middle and last of the 5 envs
>>> inertias = np.tile(np.array([0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]), (3, 2, 1))
>>> prims.set_body_inertias(inertias, indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
```

set_body_masses(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
body_indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set body masses for articulation bodies in the view
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – body masses for articulations in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – body indices to specify which bodies to manipulate. Shape (K,). Where K <= num of bodies. Defaults to None (i.e: all bodies).

Example:

```
>>> # set the masses for all the articulation rigid bodies to the indicated values.
>>> # Since there are 5 envs, the masses are repeated 5 times
>>> masses = np.tile(np.array([1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.2]), (num_envs, 1))
>>> prims.set_body_masses(masses)
>>>
>>> # set the fingers masses: panda_leftfinger (10) and panda_rightfinger (11) to 0.2
>>> # for the first, middle and last of the 5 envs
>>> masses = np.tile(np.array([0.2, 0.2]), (3, 1))
>>> prims.set_body_masses(masses, indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
```

set_default_state(
positions:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the default state of the prims (positions and orientations), that will be used after each reset.
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prim. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # configure default states for all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:, 0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_default_state(positions=positions, orientations=orientations)
>>>
>>> # set default states during post-reset
>>> prims.post_reset()
```

set_effort_modes(
mode:str,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|None =None,
joint_names:List[str]|None =None,
)→None Set effort modes for articulations in the view
Parameters:

- mode (str) – effort mode to be applied to prims in the view: `acceleration` or `force`.

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Example:

```
>>> # set the effort mode for all joints to 'force'
>>> prims.set_effort_modes("force")
>>>
>>> # set only the finger joints effort mode to 'force' for the first, middle and last of the 5 envs
>>> prims.set_effort_modes("force", indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_enabled_self_collisions(
flags:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set the enable self collisions flag (`physxArticulation:enabledSelfCollisions`)
Parameters:

- flags (Union[np.ndarray, torch.Tensor, wp.array]) – true to enable self collision. otherwise false. shape (M,)

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # enable the self collisions flag for all envs
>>> prims.set_enabled_self_collisions(np.full((num_envs,), True))
>>>
>>> # enable the self collisions flag only for the first, middle and last of the 5 envs
>>> prims.set_enabled_self_collisions(np.full((3,), True), indices=np.array([0, 2, 4]))
```

set_fixed_tendon_properties(
stiffnesses:ndarray|Tensor|warp.array=None,
dampings:ndarray|Tensor|warp.array=None,
limit_stiffnesses:ndarray|Tensor|warp.array=None,
limits:ndarray|Tensor|warp.array=None,
rest_lengths:ndarray|Tensor|warp.array=None,
offsets:ndarray|Tensor|warp.array=None,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set fixed tendon properties for articulations in the view
Search for Fixed Tendon in PhysX docs for more details
Parameters:

- stiffnesses (Union[np.ndarray, torch.Tensor, wp.array]) – fixed tendon stiffnesses for articulations in the view. shape (M, K).

- dampings (Union[np.ndarray, torch.Tensor, wp.array]) – fixed tendon dampings for articulations in the view. shape (M, K).

- limit_stiffnesses (Union[np.ndarray, torch.Tensor, wp.array]) – fixed tendon limit stiffnesses for articulations in the view. shape (M, K).

- limits (Union[np.ndarray, torch.Tensor, wp.array]) – fixed tendon limits for articulations in the view. shape (M, K, 2).

- rest_lengths (Union[np.ndarray, torch.Tensor, wp.array]) – fixed tendon rest lengths for articulations in the view. shape (M, K).

- offsets (Union[np.ndarray, torch.Tensor, wp.array]) – fixed tendon offsets for articulations in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the limit stiffnesses and dampings
>>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
>>> limit_stiffnesses = np.full((num_envs, prims.num_fixed_tendons), fill_value=10.0)
>>> dampings = np.full((num_envs, prims.num_fixed_tendons), fill_value=0.1)
>>> prims.set_fixed_tendon_properties(dampings=dampings, limit_stiffnesses=limit_stiffnesses)
```

set_friction_coefficients(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set the friction coefficients for articulation joints in the view
Search for “Joint Friction Coefficient” in PhysX docs for more details.
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – friction coefficients for articulation joints in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Example:

```
>>> # set all joint friction coefficients to 0.05 for all envs
>>> prims.set_friction_coefficients(np.full((num_envs, prims.num_dof), 0.05))
>>>
>>> # set only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) friction coefficients
>>> # for the first, middle and last of the 5 envs to 0.05
>>> prims.set_friction_coefficients(np.full((3, 2), 0.05), indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
```

set_gains(
kps:ndarray|Tensor|warp.array|None =None,
kds:ndarray|Tensor|warp.array|None =None,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
save_to_usd:bool=False,
)→None Set the implicit Proportional-Derivative (PD) controller’s Kps (stiffnesses) and Kds (dampings) of articulations in the view
Parameters:

- kps (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – stiffness of the drives. shape is (M, K). Defaults to None.

- kds (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – damping of the drives. shape is (M, K).. Defaults to None.

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- save_to_usd (bool, optional) – True to save the gains in the usd. otherwise False.

Example:

```
>>> # set the gains (stiffnesses and dampings) for all the articulation joints to the indicated values.
>>> # Since there are 5 envs, the gains are repeated 5 times
>>> stiffnesses = np.tile(np.array([100000, 100000, 100000, 100000, 80000, 80000, 80000, 50000, 50000]), (num_envs, 1))
>>> dampings = np.tile(np.array([8000, 8000, 8000, 8000, 5000, 5000, 5000, 2000, 2000]), (num_envs, 1))
>>> prims.set_gains(kps=stiffnesses, kds=dampings)
>>>
>>> # set the fingers gains (stiffnesses and dampings): panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # to 50000 and 2000 respectively for the first, middle and last of the 5 envs
>>> stiffnesses = np.tile(np.array([50000, 50000]), (3, 1))
>>> dampings = np.tile(np.array([2000, 2000]), (3, 1))
>>> prims.set_gains(kps=stiffnesses, kds=dampings, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_joint_efforts(
efforts:ndarray|Tensor|warp.array|None ,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set the joint efforts of articulations in the view
Note
This method can be used for effort control. For this purpose, there must be no joint drive or the stiffness and damping must be set to zero.
Parameters:

- efforts (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – efforts of articulations in the view to be set to in the next frame. shape is (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Hint
This method belongs to the methods used to set the articulation kinematic states:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`), `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set the efforts for all the articulation joints to the indicated values.
>>> # Since there are 5 envs, the joint efforts are repeated 5 times
>>> efforts = np.tile(np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]), (num_envs, 1))
>>> prims.set_joint_efforts(efforts)
>>>
>>> # set the fingers efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 10
>>> # for the first, middle and last of the 5 envs
>>> efforts = np.tile(np.array([10, 10]), (3, 1))
>>> prims.set_joint_efforts(efforts, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_joint_position_targets(
positions:ndarray|Tensor|warp.array|None ,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set the joint position targets for the implicit Proportional-Derivative (PD) controllers
Note
This is an independent method for controlling joints. To apply multiple targets (position, velocity, and/or effort) in the same call, consider using the `apply_action` method
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – joint position targets for the implicit PD controller. shape is (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Hint
High stiffness makes the joints snap faster and harder to the desired target, and higher damping smoothes but also slows down the joint’s movement to target

- For position control, set relatively high stiffness and low damping (to reduce vibrations)

Example:

```
>>> # apply the target positions (to move all the robot joints) to the indicated values.
>>> # Since there are 5 envs, the joint positions are repeated 5 times
>>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
>>> prims.set_joint_position_targets(positions)
>>>
>>> # close the robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> # for the first, middle and last of the 5 envs
>>> positions = np.tile(np.array([0.0, 0.0]), (3, 1))
>>> prims.set_joint_position_targets(positions, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_joint_positions(
positions:ndarray|Tensor|warp.array|None ,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set the joint positions of articulations in the view
Warning
This method will immediately set (teleport) the affected joints to the indicated value. Use the `set_joint_position_targets` or the `apply_action` methods to control the articulation joints.
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – joint positions of articulations in the view to be set to in the next frame. shape is (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Hint
This method belongs to the methods used to set the articulation kinematic states:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`), `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set all the articulation joints.
>>> # Since there are 5 envs, the joint positions are repeated 5 times
>>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
>>> prims.set_joint_positions(positions)
>>>
>>> # set only the fingers in closed position: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
>>> # for the first, middle and last of the 5 envs
>>> positions = np.tile(np.array([0.0, 0.0]), (3, 1))
>>> prims.set_joint_positions(positions, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_joint_velocities(
velocities:ndarray|Tensor|warp.array|None ,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set the joint velocities of articulations in the view
Warning
This method will immediately set the affected joints to the indicated value. Use the `set_joint_velocity_targets` or the `apply_action` methods to control the articulation joints.
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – joint velocities of articulations in the view to be set to in the next frame. shape is (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Hint
This method belongs to the methods used to set the articulation kinematic states:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`), `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set the velocities for all the articulation joints to the indicated values.
>>> # Since there are 5 envs, the joint velocities are repeated 5 times
>>> velocities = np.tile(np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]), (num_envs, 1))
>>> prims.set_joint_velocities(velocities)
>>>
>>> # set the fingers velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8) to -0.1
>>> # for the first, middle and last of the 5 envs
>>> velocities = np.tile(np.array([-0.1, -0.1]), (3, 1))
>>> prims.set_joint_velocities(velocities, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_joint_velocity_targets(
velocities:ndarray|Tensor|warp.array|None ,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set the joint velocity targets for the implicit Proportional-Derivative (PD) controllers
Note
This is an independent method for controlling joints. To apply multiple targets (position, velocity, and/or effort) in the same call, consider using the `apply_action` method
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – joint velocity targets for the implicit PD controller. shape is (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Hint
High stiffness makes the joints snap faster and harder to the desired target, and higher damping smoothes but also slows down the joint’s movement to target

- For velocity control, stiffness must be set to zero with a non-zero damping

Example:

```
>>> # apply the target velocities for all the articulation joints to the indicated values.
>>> # Since there are 5 envs, the joint velocities are repeated 5 times
>>> velocities = np.tile(np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]), (num_envs, 1))
>>> prims.set_joint_velocity_targets(velocities)
>>>
>>> # apply the fingers target velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8) to -1.0
>>> # for the first, middle and last of the 5 envs
>>> velocities = np.tile(np.array([-0.1, -0.1]), (3, 1))
>>> prims.set_joint_velocity_targets(velocities, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_joints_default_state(
positions:ndarray|Tensor|warp.array|None =None,
velocities:ndarray|Tensor|warp.array|None =None,
efforts:ndarray|Tensor|warp.array|None =None,
)→None Set the joints default state (joint positions, velocities and efforts) to be applied after each reset.
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default joint positions. shape is (N, num of dofs). Defaults to None.

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default joint velocities. shape is (N, num of dofs). Defaults to None.

- efforts (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default joint efforts. shape is (N, num of dofs). Defaults to None.

Example:

```
>>> # configure default joint states for all articulations
>>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
>>> prims.set_joints_default_state(
... positions=positions,
... velocities=np.zeros((num_envs, prims.num_dof)),
... efforts=np.zeros((num_envs, prims.num_dof))
... )
>>>
>>> # set default states during post-reset
>>> prims.post_reset()
```

set_linear_velocities(
velocities:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the linear velocities of the prims in the view
The method does this through the PhysX API only. It has to be called after initialization. Note: This method is not supported for the gpu pipeline. `set_velocities` method should be used instead.
Warning
This method will immediately set the articulation state
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – linear velocities to set the rigid prims to. shape is (M, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`), `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set each articulation linear velocity to (1.0, 1.0, 1.0)
>>> velocities = np.ones((num_envs, 3))
>>> prims.set_linear_velocities(velocities)
>>>
>>> # set only the articulation linear velocities for the first, middle and last of the 5 envs
>>> velocities = np.ones((3, 3))
>>> prims.set_linear_velocities(velocities, indices=np.array([0, 2, 4]))
```

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame).
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – translations in the local frame of the prims (with respect to its parent prim). shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all articulations
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the articulations for the first, middle and last of the 5 envs
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_local_poses(positions, orientations, indices=np.array([0, 2, 4]))
```

set_local_scales(
scales:ndarray|Tensor|warp.array|None ,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim scales in the view with respect to the local frame (the prim’s parent frame)
Parameters:

- scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – scales to be applied to the prim’s dimensions in the view. shape is (M, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the scale for all prims. Since there are 5 envs, the scale is repeated 5 times
>>> scales = np.tile(np.array([1.0, 0.75, 0.5]), (num_envs, 1))
>>> prims.set_local_scales(scales)
>>>
>>> # set the scale for the first, middle and last of the 5 envs
>>> scales = np.tile(np.array([1.0, 0.75, 0.5]), (3, 1))
>>> prims.set_local_scales(scales, indices=np.array([0, 2, 4]))
```

set_max_efforts(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set maximum efforts for articulation in the view
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – maximum efforts for articulations in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Example:

```
>>> # set the max efforts for all the articulation joints to the indicated values.
>>> # Since there are 5 envs, the joint efforts are repeated 5 times
>>> max_efforts = np.tile(np.array([10000, 9000, 8000, 7000, 6000, 5000, 4000, 1000, 1000]), (num_envs, 1))
>>> prims.set_max_efforts(max_efforts)
>>>
>>> # set the fingers max efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 1000
>>> # for the first, middle and last of the 5 envs
>>> max_efforts = np.tile(np.array([1000, 1000]), (3, 1))
>>> prims.set_max_efforts(max_efforts, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

set_max_joint_velocities(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Set maximum velocities for articulation in the view
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – maximum velocities for articulations in the view. shape (M, K).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

set_sleep_thresholds(
thresholds:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Parameters:

- thresholds (Union[np.ndarray, torch.Tensor, wp.array]) – sleep thresholds to be applied. shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the sleep threshold for all envs
>>> prims.set_sleep_thresholds(np.full((num_envs,), 0.01))
>>>
>>> # set only the sleep threshold for the first, middle and last of the 5 envs
>>> prims.set_sleep_thresholds(np.full((3,), 0.01), indices=np.array([0, 2, 4]))
```

set_solver_position_iteration_counts(
counts:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set the solver (position) iteration count for the articulations
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
Parameters:

- counts (Union[np.ndarray, torch.Tensor, wp.array]) – number of iterations for the solver. Shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the position iteration count for all envs
>>> prims.set_solver_position_iteration_counts(np.full((num_envs,), 64))
>>>
>>> # set only the position iteration count for the first, middle and last of the 5 envs
>>> prims.set_solver_position_iteration_counts(np.full((3,), 64), indices=np.array([0, 2, 4]))
```

set_solver_velocity_iteration_counts(
counts:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set the solver (velocity) iteration count for the articulations
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
Parameters:

- counts (Union[np.ndarray, torch.Tensor, wp.array]) – number of iterations for the solver. Shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the velocity iteration count for all envs
>>> prims.set_solver_velocity_iteration_counts(np.full((num_envs,), 64))
>>>
>>> # set only the velocity iteration count for the first, middle and last of the 5 envs
>>> prims.set_solver_velocity_iteration_counts(np.full((3,), 64), indices=np.array([0, 2, 4]))
```

set_stabilization_thresholds(
thresholds:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set the mass-normalized kinetic energy below which the articulation may participate in stabilization
Search for Stabilization Threshold in PhysX docs for more details
Parameters:

- thresholds (Union[np.ndarray, torch.Tensor, wp.array]) – stabilization thresholds to be applied. Shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the stabilization threshold for all envs
>>> prims.set_stabilization_thresholds(np.full((num_envs,), 0.005))
>>>
>>> # set only the stabilization threshold for the first, middle and last of the 5 envs
>>> prims.set_stabilization_thresholds(np.full((3,), 0.0051), indices=np.array([0, 2, 4]))
```

set_velocities(
velocities:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the linear and angular velocities of the prims in the view at once.
The method does this through the PhysX API only. It has to be called after initialization
Warning
This method will immediately set the articulation state
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – linear and angular velocities respectively to set the rigid prims to. shape is (M, 6).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the articulation kinematic state:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`), `set_joint_positions`, `set_joint_velocities`, `set_joint_efforts`
Example:

```
>>> # set each articulation linear velocity to (1., 1., 1.) and angular velocity to (.1, .1, .1)
>>> velocities = np.ones((num_envs, 6))
>>> velocities[:,3:] = 0.1
>>> prims.set_velocities(velocities)
>>>
>>> # set only the articulation velocities for the first, middle and last of the 5 envs
>>> velocities = np.ones((3, 6))
>>> velocities[:,3:] = 0.1
>>> prims.set_velocities(velocities, indices=np.array([0, 2, 4]))
```

set_visibilities(
visibilities:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the visibilities of the prims in stage
Parameters:

- visibilities (Union[np.ndarray, torch.Tensor, wp.array]) – flag to set the visibilities of the usd prims in stage. Shape (M,). Where M <= size of the encapsulated prims in the view.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Defaults to None (i.e: all prims in the view).

Example:

```
>>> # make all prims not visible in the stage
>>> prims.set_visibilities(visibilities=[False] * num_envs)
```

set_world_poses(
positions:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
usd:bool=True,
)→None Set poses of prims in the view with respect to the world’s frame.
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prim. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all articulations in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the articulations for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
```

switch_control_mode(
mode:str,
indices:ndarray|List|Tensor|warp.array|None =None,
joint_indices:ndarray|List|Tensor|warp.array|None =None,
joint_names:List[str]|None =None,
)→None Switch control mode between `"position"`, `"velocity"`, or `"effort"` for all joints
This method will set the implicit Proportional-Derivative (PD) controller’s Kps (stiffnesses) and Kds (dampings), defined via the `set_gains` method, of the selected articulations and joints according to the following rule:

[TABLE]
Control mode | Stiffnesses | Dampings
"position" | Kps | Kds
"velocity" | 0 | Kds
"effort" | 0 | 0
[/TABLE]
Parameters:

- mode (str) – control mode to switch the articulations specified to. It can be `"position"`, `"velocity"`, or `"effort"`

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

Example:

```
>>> # set 'velocity' as control mode for all joints
>>> prims.switch_control_mode("velocity")
>>>
>>> # set 'effort' as control mode only for the fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8)
>>> # for the first, middle and last of the 5 envs
>>> prims.switch_control_mode("effort", indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
```

switch_dof_control_mode(
mode:str,
dof_index:int,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Switch control mode between `"position"`, `"velocity"`, or `"effort"` for the specified DOF
This method will set the implicit Proportional-Derivative (PD) controller’s Kps (stiffnesses) and Kds (dampings), defined via the `set_gains` method, of the selected DOF according to the following rule:

[TABLE]
Control mode | Stiffnesses | Dampings
"position" | Kps | Kds
"velocity" | 0 | Kds
"effort" | 0 | 0
[/TABLE]
Parameters:

- mode (str) – control mode to switch the DOF specified to. It can be `"position"`, `"velocity"` or `"effort"`

- dof_index (int) – dof index to switch the control mode of.

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set 'velocity' as control mode for the panda_joint1 (0) joint for all envs
>>> prims.switch_dof_control_mode("velocity", dof_index=0)
>>>
>>> # set 'effort' as control mode for the panda_joint1 (0) for the first, middle and last of the 5 envs
>>> prims.switch_dof_control_mode("effort", dof_index=0, indices=np.array([0, 2, 4]))
```

propertybody_names:List[str]
List of prim names for each rigid body (link) of the articulations
Returns:
ordered names of bodies that corresponds to links for the articulations in the view

Return type:
List[str]

Example:

```
>>> prims.body_names
['panda_link0', 'panda_link1', 'panda_link2', 'panda_link3', 'panda_link4', 'panda_link5',
'panda_link6', 'panda_link7', 'panda_link8', 'panda_hand', 'panda_leftfinger', 'panda_rightfinger']
```

propertycount:int
Returns:
Number of prims encapsulated in this view.

Return type:
int

Example:

```
>>> prims.count
5
```

propertydof_names:List[str]
List of prim names for each DOF of the articulations
Returns:
ordered names of joints that corresponds to degrees of freedom for the articulations in the view

Return type:
List[str]

Example:

```
>>> prims.dof_names
['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5',
'panda_joint6', 'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']
```

propertyinitialized:bool
Check if prim view is initialized
Returns:
True if the view object was initialized (after the first call of .initialize()). False otherwise.

Return type:
bool

Example:

```
>>> # given an initialized articulation view
>>> prims.initialized
True
```

propertyis_non_root_articulation_link:bool
Returns: bool: True if the prim corresponds to a non root link in an articulation. Otherwise False.

propertyjoint_names:List[str]
List of prim names for each joint of the articulations
Returns:
ordered names of joints that corresponds to degrees of freedom for the articulations in the view

Return type:
List[str]

propertyname:str
Returns: str: name given to the prims view when instantiating it.

propertynum_bodies:int
Number of rigid bodies (links) of the articulations
Returns:
maximum number of rigid bodies for the articulations in the view

Return type:
int

Example:

```
>>> prims.num_bodies
12
```

propertynum_dof:int
Number of DOF of the articulations
Returns:
maximum number of DOFs for the articulations in the view

Return type:
int

Example:

```
>>> prims.num_dof
9
```

propertynum_fixed_tendons:int
Number of fixed tendons of the articulations
Returns:
maximum number of fixed tendons for the articulations in the view

Return type:
int

Example:

```
>>> prims.num_fixed_tendons
0
```

propertynum_joints:int
Number of joints of the articulations
Returns:
number of joints of the articulations in the view

Return type:
int

propertynum_shapes:int
Number of rigid shapes of the articulations
Returns:
maximum number of rigid shapes for the articulations in the view

Return type:
int

Example:

```
>>> prims.num_shapes
17
```

propertyprim_paths:List[str]
Returns:
list of prim paths in the stage encapsulated in this view.

Return type:
List[str]

Example:

```
>>> prims.prim_paths
['/World/envs/env_0', '/World/envs/env_1', '/World/envs/env_2', '/World/envs/env_3', '/World/envs/env_4']
```

propertyprims:List[pxr.Usd.Prim]
Returns:
List of USD Prim objects encapsulated in this view.

Return type:
List[Usd.Prim]

Example:

```
>>> prims.prims
[Usd.Prim(</World/envs/env_0>), Usd.Prim(</World/envs/env_1>), Usd.Prim(</World/envs/env_2>),
Usd.Prim(</World/envs/env_3>), Usd.Prim(</World/envs/env_4>)]
```

#### Scenes
classScene
Bases: `object`
Provide methods to add objects of interest in the stage to retrieve their information and set their reset default state in an easy way
Example:

```
>>> from isaacsim.core.api.scenes import Scene
>>>
>>> scene = Scene()
>>> scene
<isaacsim.core.api.scenes.scene.Scene object at 0x...>
```
add(
obj:SingleXFormPrim ,
)→SingleXFormPrim Add an object to the scene registry
Parameters:
obj (SingleXFormPrim ) – object to be added

Raises:
Exception – The object type is not supported yet

Returns:
object

Return type:
SingleXFormPrim

Example:

```
>>> from isaacsim.core.prims import XFormPrim
>>>
>>> prims = XFormPrim(prim_paths_expr="/World")
>>> scene.add(prims)
<isaacsim.core.prims.XFormPrim object at 0x...>
```

add_default_ground_plane(
z_position:float=0,
name='default_ground_plane',
prim_path:str='/World/defaultGroundPlane',
static_friction:float=0.5,
dynamic_friction:float=0.5,
restitution:float=0.8,
)→GroundPlane Create a ground plane (using the default asset for Isaac Sim environments) and add it to the scene registry
Parameters:

- z_position (float, optional) – ground plane position in the z-axis. Defaults to 0.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “default_ground_plane”.

- prim_path (str, optional) – prim path of the prim to create. Defaults to “/World/defaultGroundPlane”.

- static_friction (float, optional) – static friction coefficient. Defaults to 0.5.

- dynamic_friction (float, optional) – dynamic friction coefficient. Defaults to 0.5.

- restitution (float, optional) – restitution coefficient. Defaults to 0.8.

Returns:
ground plane instance

Return type:
GroundPlane

Example:

```
>>> scene.add_default_ground_plane()
server...
<isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
```

add_ground_plane(
size:float|None =None,
z_position:float=0,
name='ground_plane',
prim_path:str='/World/groundPlane',
static_friction:float=0.5,
dynamic_friction:float=0.5,
restitution:float=0.8,
color:ndarray|None =None,
)→GroundPlane Create a ground plane and add it to the scene registry
Parameters:

- size (Optional[float], optional) – length of each edge. Defaults to 5000.0.

- z_position (float, optional) – ground plane position in the z-axis. Defaults to 0.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “ground_plane”.

- prim_path (str, optional) – prim path of the prim to create. Defaults to “/World/groundPlane”.

- static_friction (float, optional) – static friction coefficient. Defaults to 0.5.

- dynamic_friction (float, optional) – dynamic friction coefficient. Defaults to 0.5.

- restitution (float, optional) – restitution coefficient. Defaults to 0.8.

- color (Optional[np.ndarray], optional) – color of the visual plane. Defaults to None, which means 50% gray

Returns:
ground plane instance

Return type:
GroundPlane

Example:

```
>>> scene.add_ground_plane()
<isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
```

clear(registry_only:bool=False)→None
Clear the stage from all added objects to the scene registry.
Parameters:
registry_only (bool, optional) – True to remove the object from the scene registry only and not the USD. Defaults to False.

Example:

```
>>> scene.clear()
```

compute_object_AABB(
name:str,
)→Tuple[ndarray,ndarray]Compute the bounding box points (minimum and maximum) of a registered object given its name
Warning
The bounding box computations should be enabled, via the `enable_bounding_boxes_computations` method, before querying the Axis-Aligned Bounding Box (AABB) of an object
Parameters:
name (str) – object name

Raises:
Exception – If the bounding box computation is not enabled

Returns:
bounding box points (minimum and maximum)

Return type:
Tuple[np.ndarray, np.ndarray]

Example:

```
>>> scene.enable_bounding_boxes_computations()
>>>
>>> bbox = scene.compute_object_AABB("ground_plane")
>>> bbox[0] # minimum
array([-50., -50., 0.])
>>> bbox[1] # maximum
array([50., 50., 0.])
```

disable_bounding_boxes_computations()→None
Disable the bounding boxes computations
Example:

```
>>> scene.disable_bounding_boxes_computations()
```

enable_bounding_boxes_computations()→None
Enable the bounding boxes computations
Example:

```
>>> scene.enable_bounding_boxes_computations()
```

get_object(
name:str,
)→SingleXFormPrim Get a registered object by its name if exists otherwise None
Note
Object can be registered via the `add` method
Parameters:
str (name) – object name

Returns:
object if it exists otherwise None

Return type:
SingleXFormPrim

Example:

```
>>> # given a default ground plane named 'default_ground_plane'
>>> scene.get_object("default_ground_plane")
<isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
```

object_exists(name:str)→bool
Check if an object exists in the scene registry
Parameters:
name (str) – object name

Returns:
whether the object exists in the scene registry or not

Return type:
bool

Example:

```
>>> # given a default ground plane named 'default_ground_plane'
>>> scene.object_exists("default_ground_plane")
True
```

post_reset()→None
Call the `post_reset` method on all added objects to the scene registry
Example:

```
>>> scene.post_reset()
```

remove_object(name:str, registry_only:bool=False)→None
Remove and object from the scene registry and the USD stage if specified (enable by default)
Parameters:

- name (str) – Name of the prim to be removed.

- registry_only (bool, optional) – True to remove the object from the scene registry only and not the USD. Defaults to False.

Example:

```
>>> # given a default ground plane named 'default_ground_plane'
>>> scene.remove_object("default_ground_plane")
```

propertystage:pxr.Usd.Stage
Returns:
current USD stage

Return type:
Usd.Stage

Example:

```
>>> scene.stage
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x...usd'),
sessionLayer=Sdf.Find('anon:0x...usda'),
pathResolverContext=<invalid repr>)
```

classSceneRegistry
Bases: `object`
Class to keep track of the different types of objects added to the scene
Example:

```
>>> from isaacsim.core.api.scenes import SceneRegistry
>>>
>>> scene_registry = SceneRegistry()
>>> scene_registry
<isaacsim.core.api.scenes.scene_registry.SceneRegistry object at 0x...>
```
add_articulated_system(
name:str,
articulated_system:SingleArticulation ,
)→None Register a `SingleArticulation` (or subclass) object
Parameters:

- name (str) – object name

- articulated_system (SingleArticulation ) – object

add_articulated_view(
name:str,
articulated_view:Articulation ,
)→None Register a `Articulation` (or subclass) object
Parameters:

- name (str) – object name

- articulated_view (Articulation ) – object

add_cloth(
name:str,
cloth:SingleClothPrim ,
)→None Register a `SingleClothPrim` (or subclass) object
Parameters:

- name (str) – object name

- cloth (SingleClothPrim ) – object

add_cloth_view(
name:str,
cloth_prim_view:ClothPrim ,
)→None Register a `ClothPrim` (or subclass) object
Parameters:

- name (str) – object name

- cloth_prim_view (ClothPrim ) – object

add_deformable(
name:str,
deformable:SingleDeformablePrim ,
)→None Register a `SingleDeformablePrim` (or subclass) object
Parameters:

- name (str) – object name

- deformable (SingleDeformablePrim ) – object

add_deformable_material(
name:str,
deformable_material:DeformableMaterial ,
)→None Register a `DeformableMaterial` (or subclass) object
Parameters:

- name (str) – object name

- deformable_material (DeformableMaterial ) – object

add_deformable_material_view(
name:str,
deformable_material_view:DeformableMaterialView ,
)→None Register a `DeformableMaterialView` (or subclass) object
Parameters:

- name (str) – object name

- deformable_material_view (DeformableMaterialView ) – object

add_deformable_view(
name:str,
deformable_prim_view:DeformablePrim ,
)→None Register a `DeformablePrim` (or subclass) object
Parameters:

- name (str) – object name

- deformable_prim_view (DeformablePrim ) – object

add_geometry_object(
name:str,
geometry_object:SingleGeometryPrim ,
)→None Register a `SingleGeometryPrim` (or subclass) object
Parameters:

- name (str) – object name

- geometry_object (SingleGeometryPrim ) – object

add_geometry_prim_view(
name:str,
geometry_prim_view:GeometryPrim ,
)→None Register a `GeometryPrim` (or subclass) object
Parameters:

- name (str) – object name

- geometry_prim_view (GeometryPrim ) – object

add_particle_material(
name:str,
particle_material:ParticleMaterial ,
)→None Register a `ParticleMaterial` (or subclass) object
Parameters:

- name (str) – object name

- particle_material (ParticleMaterial ) – object

add_particle_material_view(
name:str,
particle_material_view:ParticleMaterialView ,
)→None Register a `ParticleMaterialView` (or subclass) object
Parameters:

- name (str) – object name

- particle_material_view (ParticleMaterialView ) – object

add_particle_system(
name:str,
particle_system:SingleParticleSystem ,
)→None Register a `SingleParticleSystem` (or subclass) object
Parameters:

- name (str) – object name

- particle_system (ParticleSystem ) – object

add_particle_system_view(
name:str,
particle_system_view:ParticleSystem ,
)→None Register a `ParticleSystem` (or subclass) object
Parameters:

- name (str) – object name

- particle_system_view (ParticleSystem ) – object

add_rigid_contact_view(
name:str,
rigid_contact_view:RigidContactView ,
)→None Register a `RigidContactView` (or subclass) object
Parameters:

- name (str) – object name

- rigid_contact_view (RigidContactView ) – object

add_rigid_object(
name:str,
rigid_object:SingleRigidPrim ,
)→None Register a `SingleRigidPrim` (or subclass) object
Parameters:

- name (str) – object name

- rigid_object (SingleRigidPrim ) – object

add_rigid_prim_view(
name:str,
rigid_prim_view:RigidPrim ,
)→None Register a `RigidPrim` (or subclass) object
Parameters:

- name (str) – object name

- rigid_prim_view (RigidPrim ) – object

add_robot(
name:str,
robot:Robot ,
)→None Register a `Robot` (or subclass) object
Parameters:

- name (str) – object name

- robot (Robot ) – object

add_robot_view(
name:str,
robot_view:RobotView ,
)→None Register a `RobotView` (or subclass) object
Parameters:

- name (str) – object name

- robot_view (RobotView ) – object

add_sensor(
name:str,
sensor:BaseSensor ,
)→None Register a `BaseSensor` (or subclass) object
Parameters:

- name (str) – object name

- sensor (BaseSensor ) – object

add_xform(
name:str,
xform:SingleXFormPrim ,
)→None Register a `SingleXFormPrim` (or subclass) object
Parameters:

- name (str) – object name

- robot (Robot ) – object

add_xform_view(
name:str,
xform_prim_view:XFormPrim ,
)→None Register a `XFormPrim` (or subclass) object
Parameters:

- name (str) – object name

- xform_prim_view (XFormPrim ) – object

get_object(
name:str,
)→SingleXFormPrim Get a registered object by its name if exists otherwise None
Parameters:
name (str) – object name

Returns:
the object if it exists otherwise None

Return type:
SingleXFormPrim

Example:

```
>>> # given a registered ground plane named 'default_ground_plane'
>>> scene_registry.get_object("default_ground_plane")
<isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
```

name_exists(name:str)→bool
Check if an object exists in the registry by its name
Parameters:
name (str) – object name

Returns:
whether the object is registered or not

Return type:
bool

Example:

```
>>> # given a registered ground plane named 'default_ground_plane'
>>> scene_registry.name_exists("default_ground_plane")
True
```

remove_object(name:str)→None
Remove and object from the registry
Note
This method will only remove the object from the internal registry. The wrapped object will not be removed from the USD stage
Parameters:
name (str) – object name

Raises:
Exception – If the name doesn’t exist in the registry

Example:

```
>>> # given a registered ground plane named 'default_ground_plane'
>>> scene_registry.remove_object("default_ground_plane")
```

propertyarticulated_systems:dict
Registered `SingleArticulation` objects

propertyarticulated_views:dict
Registered `Articulation` objects

propertycloth_prim_views:dict
Registered `ClothPrim` objects

propertycloth_prims:dict
Registered `SingleClothPrim` objects

propertydeformable_material_views:dict
Registered `DeformableMaterialView` objects

propertydeformable_materials:dict
Registered `DeformableMaterial` objects

propertydeformable_prim_views:dict
Registered `DeformablePrim` objects

propertydeformable_prims:dict
Registered `SingleDeformablePrim` objects

propertygeometry_prim_views:dict
Registered `GeometryPrim` objects

propertyparticle_material_views:dict
Registered `particle_material_view` objects

propertyparticle_materials:dict
Registered `ParticleMaterial` objects

propertyparticle_system_views:dict
Registered `ParticleSystem` objects

propertyparticle_systems:dict
Registered `SingleParticleSystem` objects

propertyrigid_contact_views:dict
Registered `RigidContactView` objects

propertyrigid_objects:dict
Registered `SingleRigidPrim` objects

propertyrigid_prim_views:dict
Registered `RigidPrim` objects

propertyrobot_views:dict
Registered `RobotView` objects

propertyrobots:dict
Registered `Robot` objects

propertysensors:dict
Registered `BaseSensor` (and derived) objects

propertyxform_prim_views:dict
Registered `XFormPrim` objects

propertyxforms:dict
Registered `SingleXFormPrim` objects

#### Sensors
classBaseSensor(
prim_path:str,
name:str='base_sensor',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
)Bases: SingleXFormPrim
Provides a common properties and methods to deal with prims as a sensor
Note
This class, which inherits from `SingleXFormPrim`, does not currently add any new property/method to it. Its definition is oriented to future implementations.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “base_sensor”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

Raises:
Exception – if translation and position defined at the same time

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

post_reset()→None
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

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

classRigidContactView(
prim_paths_expr:str|List[str],
filter_paths_expr:List[str]|List[List[str]],
name:str='rigid_contact_view',
prepare_contact_sensors:bool=True,
disable_stablization:bool=True,
max_contact_count:int=0,
)Bases: `object`
Provides high level functions to deal with rigid prims (one or many) that track their contacts through filters as well as their attributes/properties.
This class wraps all matching rigid prims found at the regex provided at the `prim_paths_expr` argument
Warning
The rigid prim view object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Parameters:

- prim_paths_expr (Union[str, List[str]]) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Cube” will match /World/Env1/Cube, /World/Env2/Cube..etc. (a non regex prim path can also be used to encapsulate one rigid prim). Additionally a list of regex can be provided. example [“/World/Env[1-5]/Cube”, “/World/Env[10-19]/Cube”].

- Union[List[str] (filter_paths_expr) – list of prim paths regex to filter the contacts for each corresponding prim_paths_expr. Example: [“/World/envs/env_2/Xform”] will filter the contacts corresponding to the expression passed.

- List[List[str]]] – list of prim paths regex to filter the contacts for each corresponding prim_paths_expr. Example: [“/World/envs/env_2/Xform”] will filter the contacts corresponding to the expression passed.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “rigid_contact_view”.

- prepare_contact_sensors (bool, Optional) – if rigid prims in the view are not cloned from a prim in a prepared state, (although slow for large number of prims) this ensures that appropriate physics settings are applied on all the prim in the view.

- disable_stablization (bool, optional) – disables the contact stabilization parameter in the physics context

- max_contact_count (int, optional) – maximum number of contact data to report when detailed contact information is needed

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.cloner import GridCloner
>>> from isaacsim.core.api.sensors import RigidContactView
>>> from pxr import UsdGeom
>>>
>>> env_zero_path = "/World/envs/env_0"
>>> num_envs = 5
>>>
>>> # clone the environment (num_envs)
>>> cloner = GridCloner(spacing=0)
>>> cloner.define_base_env(env_zero_path)
>>> UsdGeom.Xform.Define(stage_utils.get_current_stage(), env_zero_path)
>>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform", "Xform")
>>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform/Cube", "Cube")
>>> # position the cubes on top of each other
>>> position_offsets = np.zeros((num_envs, 3))
>>> position_offsets[:, 2] = np.arange(num_envs) * 1.1
>>> env_pos = cloner.clone(
... source_prim_path=env_zero_path,
... prim_paths=cloner.generate_paths("/World/envs/env", num_envs),
... position_offsets=position_offsets
... copy_from_source=True,
... )
>>>
>>> # wrap the prims
>>> prims = RigidContactView(
... prim_paths_expr="/World/envs/env.*/Xform",
... name="RigidContactView_view",
... filter_paths_expr=["/World/envs/env_2/Xform"],
... max_contact_count=10,
... )
>>> prims
<isaacsim.core.api.sensors.rigid_contact_view.RigidContactView object at 0x7f8d4eb1abf0>
```
get_contact_force_data(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→Tuple[ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray]Get more detailed contact information between the prims in the view and the filter prims.
Specifically, this method provides individual contact normals, contact points, contact separations as well as contact forces for each pair (the sum of which equals the forces that the `get_contact_force_matrix` method provides as the force aggregate of a pair)
Given to the dynamic nature of collision between bodies, this method will provide buffers of contact data which are arranged sequentially for each pair. The starting index and the number of contact data points for each pair in this stream can be realized from pair_contacts_start_indices, and pair_contacts_count tensors. They both have a dimension of `(num_shapes, num_filters)` where `num_filters` is determined according to the `filter_paths_expr` parameter
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (M, self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

Example:

```
>>> # get detailed contact force data between the prims and the filter prims (the cube in the middle)
>>> data = prims.get_contact_force_data()
>>> data[0] # normal forces
[[-168.53815]
[ -89.57392]
[-156.10307]
[ -75.17234]
[ 98.0681 ]
[ 52.56319]
[ 108.26558]
[ 67.62025]
[ 0. ]
[ 0. ]]
>>> data[1] # points
[[ 0.4948182 -0.49902824 1.5001888 ]
[ 0.4950411 0.49933064 1.5001996 ]
[-0.5024581 0.49930018 1.5001924 ]
[-0.5024276 -0.49880558 1.5001817 ]
[-0.5023767 0.497138 2.5001519 ]
[-0.502735 -0.49877006 2.5001822 ]
[ 0.4947694 -0.4989927 2.500226 ]
[ 0.4949917 0.49677914 2.5001955 ]
[ 0. 0. 0. ]
[ 0. 0. 0. ]]
>>> data[2] # normals
[[-4.3812128e-05 3.0501858e-05 1.0000000e+00]
[-4.3812128e-05 3.0501858e-05 1.0000000e+00]
[-4.3812128e-05 3.0501858e-05 1.0000000e+00]
[-4.3812128e-05 3.0501858e-05 1.0000000e+00]
[ 2.1408198e-06 -7.0731985e-05 1.0000000e+00]
[ 2.1408198e-06 -7.0731985e-05 1.0000000e+00]
[ 2.1408198e-06 -7.0731985e-05 1.0000000e+00]
[ 2.1408198e-06 -7.0731985e-05 1.0000000e+00]
[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
>>> data[3] # distances
[[ 3.7143487e-05]
[-4.0254322e-06]
[-4.0531158e-05]
[ 6.0737699e-07]
[ 1.9307560e-04]
[ 9.2272363e-05]
[ 4.6372414e-05]
[ 1.4718286e-04]
[ 0.0000000e+00]
[ 0.0000000e+00]]
>>> data[4] # pair contacts count
[[0]
[4]
[0]
[4]
[0]]
>>> data[5] # start indices of pair contacts
[[0]
[0]
[4]
[4]
[8]]
```

get_contact_force_matrix(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayGet the contact forces between the prims in the view and the filter prims.
E.g., a matrix of dimension `(num_shapes, num_filters, 3)` where `num_filters` is determined according to the `filter_paths_expr` parameter
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. The function returns contact impulses if the default dt is used

Returns:
Net contact forces between the view prim and the filter prims with shape (M, self.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the contact forces between the prims and the filter prims (the cube in the middle)
>>> prims.get_contact_force_matrix()
[[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
[[ 2.2649009e-02 -1.3710857e-02 -4.9047806e+02]]
[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
[[-3.3276828e-03 -2.3870371e-02 3.2733777e+02]]
[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]]
```

get_friction_data(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→Tuple[ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray]Gets friction data between the prims in the view and the filter prims. Specifically, this method provides frictional contact forces, and points. The data in reported for number of anchor points that includes tangential forces in a single tangent direction to contact normal. Given to the dynamic nature of collision between bodies, this method will provide buffers of friction data arranged sequentially for each pair. The starting index and the number of contact data points for each pair in this stream can be realized from pair_contacts_start_indices, and pair_contacts_count tensors. They both have a dimension of (self.num_shapes, self.num_filters) where filter_count is determined according to the filter_paths_expr parameter.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indicies to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for tangential forces per patch (at number of anchor points, each in a single directions) with shape (max_contact_count, 3), points with shape (max_contact_count, 3), as well as two tensors with shape (M, self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_net_contact_forces(
indices:ndarray|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayGet the overall net contact forces on the prims in the view with respect to the world’s frame.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. The function returns contact impulses if the default dt is used

Returns:
Net contact forces of the prims with shape (M,3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the net contact force on all rigid bodies. Returned shape is (5, 3).
>>> prims.get_net_contact_forces()
[[ 1.8731881e-03 5.4876995e-03 1.6408131e+02]
[ 1.9060407e-02 -2.2513291e-02 1.6358723e+02]
[-2.1011427e-02 3.5647806e-02 1.6371542e+02]
[ 9.4006478e-05 -9.3258200e-03 1.6348369e+02]
[ 9.3709816e-05 -9.2963902e-03 1.6296776e+02]]
>>>
>>> # get the net contact force on the rigid bodies for the first, middle and last of the 5 envs
>>> prims.get_net_contact_forces(indices=np.array([0, 2, 4]))
[[ 1.8731881e-03 5.4876995e-03 1.6408131e+02]
[-2.1011427e-02 3.5647806e-02 1.6371542e+02]
[ 9.3709816e-05 -9.2963902e-03 1.6296776e+02]]
```

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and set other properties using the PhysX tensor API
Note
If the rigid prim view has been added to the world scene (e.g., `world.scene.add(prims)`), it will be automatically initialized when the world is reset (e.g., `world.reset()`).
Warning
This method needs to be called after each hard reset (e.g., Stop + Play on the timeline) before interacting with any other class method.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

Example:

```
>>> prims.initialize()
```

is_physics_handle_valid()→bool
Check if rigid prim view’s physics handler is initialized
Warning
If the physics handler is not valid many of the methods that requires PhysX will return None.
Returns:
True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.

Return type:
bool

Example:

```
>>> prims.is_physics_handle_valid()
True
```

propertynum_filters:int
Returns:
number of filters bodies that report their contact with the rigid prims.

Return type:
int

Example:

```
>>> prims.num_filters
1
```

propertynum_shapes:int
Returns:
number of rigid shapes for the prims in the view.

Return type:
int

Example:

```
>>> prims.num_shapes
5
```

#### Simulation Context
classSimulationContext(*args, **kwargs)
Bases: `object`
This class provide functions that take care of many time-related events such as perform a physics or a render step for instance. Adding/ removing callback functions that gets triggered with certain events such as a physics step, timeline event (pause or play..etc), stage open/ close..etc.
It also includes an instance of PhysicsContext which takes care of many physics related settings such as setting physics dt, solver type..etc.
Parameters:

- physics_dt (Optional[float], optional) – dt between physics steps. Defaults to None.

- rendering_dt (Optional[float], optional) – dt between rendering steps. Note: rendering means rendering a frame of the current application and not only rendering a frame to the viewports/cameras. So UI elements of Isaac Sim will be refreshed with this dt as well if running non-headless. Defaults to None.

- stage_units_in_meters (Optional[float], optional) – The metric units of assets. This will affect gravity value..etc. Defaults to None.

- physics_prim_path (Optional[str], optional) – specifies the prim path to create a PhysicsScene at, only in the case where no PhysicsScene already defined. Defaults to “/physicsScene”.

- set_defaults (bool, optional) – set to True to use the defaults settings [physics_dt = 1.0/ 60.0, stage units in meters = 0.01 (i.e in cms), rendering_dt = 1.0 / 60.0, gravity = -9.81 m / s ccd_enabled, stabilization_enabled, gpu dynamics turned off, broadcast type is MBP, solver type is TGS]. Defaults to True.

- backend (str, optional) – specifies the backend to be used (numpy or torch or warp). Defaults to numpy.

- device (Optional[str], optional) – specifies the device to be used if running on the gpu with torch or warp backend.

- stage (Optional[Usd.Stage], optional) – specifies the stage to be used. Defaults to None.

Example:

```
>>> from isaacsim.core.api import SimulationContext
>>>
>>> simulation_context = SimulationContext()
>>> simulation_context
<isaacsim.core.api.simulation_context.simulation_context.SimulationContext object at 0x...>
```
add_physics_callback(
callback_name:str,
callback_fn:Callable[[float],None ],
)→None Add a callback which will be called before each physics step.
`callback_fn` should take a float argument (e.g., `step_size`)
Parameters:

- callback_name (str) – should be unique.

- callback_fn (Callable[[float], None]) – [description]

Example:

```
>>> def callback_physics(step_size):
... print("physics callback -> step_size:", step_size)
...
>>> simulation_context.add_physics_callback("callback_physics", callback_physics)
```

add_render_callback(
callback_name:str,
callback_fn:Callable,
)→None Add a callback which will be called after each rendering event such as .render().
`callback_fn` should take an argument of type (e.g., `event`)
Parameters:

- callback_name (str) – [description]

- callback_fn (Callable) – [description]

Example:

```
>>> def callback_render(event):
... print("render callback -> event:", event)
...
>>> simulation_context.add_render_callback("callback_render", callback_render)
```

add_stage_callback(
callback_name:str,
callback_fn:Callable,
)→None Add a callback which will be called after each stage event such as open/close among others
`callback_fn` should take an argument of type `omni.usd.StageEvent` (e.g., `event`)
Parameters:

- callback_name (str) – [description]

- callback_fn (Callable[[omni.usd.StageEvent], None]) – [description]

Example:

```
>>> def callback_stage(event):
... print("stage callback -> event:", event)
...
>>> simulation_context.add_stage_callback("callback_stage", callback_stage)
```

add_timeline_callback(
callback_name:str,
callback_fn:Callable,
)→None Add a callback which will be called after each timeline event such as play/pause.
`callback_fn` should take an argument of type `omni.timeline.TimelineEvent` (e.g., `event`)
Parameters:

- callback_name (str) – [description]

- callback_fn (Callable[[omni.timeline.TimelineEvent], None]) – [description]

Example:

```
>>> def callback_timeline(event):
... print("timeline callback -> event:", event)
...
>>> simulation_context.add_timeline_callback("callback_timeline", callback_timeline)
```

clear()→None
Clear the current stage leaving the PhysicsScene and /World
Example:

```
>>> simulation_context.clear()
```

clear_all_callbacks()→None
Clear all callbacks which were added using any `add_*_callback` method
Example:

```
>>> simulation_context.clear_render_callbacks()
```

classmethodclear_instance()→None
Delete the simulation context object, if it was instantiated before, and destroy any subscribed callback
Example:

```
>>> SimulationContext.clear_instance()
```

clear_physics_callbacks()→None
Remove all registered physics callbacks
Example:

```
>>> simulation_context.clear_physics_callbacks()
```

clear_render_callbacks()→None
Remove all registered render callbacks
Example:

```
>>> simulation_context.clear_render_callbacks()
```

clear_stage_callbacks()→None
Remove all registered stage callbacks
Example:

```
>>> simulation_context.clear_stage_callbacks()
```

clear_timeline_callbacks()→None
Remove all registered timeline callbacks
Example:

```
>>> simulation_context.clear_timeline_callbacks()
```

get_block_on_render()→bool
Get the block on render flag for the simulation thread
Returns:
True if one frame lag between any data captured from the render products and the current USD stage is guaranteed by blocking the step call.

Return type:
bool

Example:

```
>>> simulation_context.get_block_on_render()
False
```

get_physics_context()→PhysicsContext
Get the physics context (a class to deal with a physics scene and its settings) instance
Raises:
Exception – if there is no stage currently opened

Returns:
physics context object

Return type:
PhysicsContext

Example:

```
>>> simulation_context.get_physics_context()
<isaacsim.core.api.physics_context.physics_context.PhysicsContext object at 0x...>
```

get_physics_dt()→float
Get the current physics dt of the physics context
Raises:
Exception – if there is no stage currently opened

Returns:
current physics dt of the PhysicsContext

Return type:
float

Example:

```
>>> simulation_context.get_physics_dt()
0.016666666666666666
```

get_rendering_dt()→float
Get the current rendering dt
Raises:
Exception – if there is no stage currently opened

Returns:
current rendering dt

Return type:
float

Example:

```
>>> simulation_context.get_rendering_dt()
0.016666666666666666
```

initialize_physics()→None
Initialize the physics simulation view
Example:

```
>>> simulation_context.initialize_physics()
```

asyncinitialize_simulation_context_async()→None
Initialize the simulation context
Hint
This method is intended to be used in the Isaac Sim’s Extensions workflow where the Kit application has the control over timing of physics and rendering steps
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.initialize_simulation_context_async()
...
>>> run_coroutine(task())
```

classmethodinstance()→SimulationContext
Get the instance of the class, if it was instantiated before
Returns:
SimulationContext object or None

Return type:
SimulationContext

Example:

```
>>> # given that the class has already been instantiated before
>>> simulation_context = SimulationContext.instance()
>>> simulation_context
<isaacsim.core.api.simulation_context.simulation_context.SimulationContext object at 0x...>
```

is_playing()→bool
Check whether the simulation is playing
Returns:
True if the simulator is playing.

Return type:
bool

Example:

```
>>> # given a simulation in play
>>> simulation_context.is_playing()
True
```

is_simulating()→bool
Check whether the simulation is running or not
Warning
With deprecation of Dynamic Control Toolbox, this function is not needed
It can return True if start_simulation is called even if play was pressed/called.
Returns:
bool” True if physics simulation is happening.

Example:

```
>>> # given a running simulation
>>> simulation_context.is_simulating()
True
```

is_stopped()→bool
Check whether the simulation is playing
Returns:
True if the simulator is stopped.

Return type:
bool

Example:

```
>>> # given a simulation in play
>>> simulation_context.is_stopped()
False
```

pause()→None
Pause the physics simulation
Example:

```
>>> simulation_context.pause()
```

asyncpause_async()→None
Pause the physics simulation
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.pause_async()
...
>>> run_coroutine(task())
```

physics_callback_exists(callback_name:str)→bool
Check if a physics callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_physics'
>>> simulation_context.physics_callback_exists("callback_physics")
True
```

play()→None
Start playing simulation
Note
It does one step internally to propagate all physics handles properly.
Example:

```
>>> simulation_context.play()
```

asyncplay_async()→None
Start playing simulation
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.play_async()
...
>>> run_coroutine(task())
```

remove_physics_callback(callback_name:str)→None
Remove a physics callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'callback_physics'
>>> simulation_context.remove_physics_callback("callback_physics")
```

remove_render_callback(callback_name:str)→None
Remove a render callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'callback_render'
>>> simulation_context.remove_render_callback("callback_render")
```

remove_stage_callback(callback_name:str)→None
Remove a stage callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'callback_stage'
>>> simulation_context.remove_stage_callback("callback_stage")
```

remove_timeline_callback(callback_name:str)→None
Remove a timeline callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'timeline'
>>> simulation_context.timeline_callback("timeline")
```

render()→None
Refresh the Isaac Sim app rendering components including UI elements, viewports and others
Warning
This method is not intended to be used in the Isaac Sim’s Extensions workflow since the Kit application has the control over the rendering steps
Example:

```
>>> simulation_context.render()
```

asyncrender_async()→None
Refresh the Isaac Sim app rendering components including UI elements, viewports and others
Hint
This method is intended to be used in the Isaac Sim’s Extensions workflow where the Kit application has the control over timing of physics and rendering steps
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.render_async()
...
>>> run_coroutine(task())
```

render_callback_exists(callback_name:str)→bool
Check if a render callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_render'
>>> simulation_context.render_callback_exists("callback_render")
True
```

reset(soft:bool=False)→None
Reset the physics simulation view.
Warning
This method is not intended to be used in the Isaac Sim’s Extensions workflow since the Kit application has the control over the rendering steps. For the Extensions workflow use the `reset_async` method instead
Parameters:
soft (bool, optional) – if set to True simulation won’t be stopped and start again. It only calls the reset on the scene objects.

Example:

```
>>> simulation_context.reset()
```

asyncreset_async(soft:bool=False)→None
Reset the physics simulation view (asynchronous version).
Parameters:
soft (bool, optional) – if set to True simulation won’t be stopped and start again. It only calls the reset on the scene objects.

Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
>>> await simulation_context.reset_async()
>>>
>>> run_coroutine(task())
```

set_block_on_render(block:bool)→None
Set block on render flag for the simulation thread
Note
This guarantee a one frame lag between any data captured from the render products and the current USD stage if enabled.
Parameters:
block (bool) – True to block the thread until the renderer is done.

Example:

```
>>> simulation_context.set_block_on_render(False)
```

set_simulation_dt(
physics_dt:float|None =None,
rendering_dt:float|None =None,
)→None Specify the physics step and rendering step size to use when stepping and rendering.
Parameters:

- physics_dt (float) – The physics time-step. None means it won’t change the current setting. (default: None).

- rendering_dt (float) – The rendering time-step. None means it won’t change the current setting. (default: None)

Hint
It is recommended that the two values be divisible, with the `rendering_dt` being equal to or greater than the `physics_dt`
Example:

```
>>> set physics dt to 120 Hz and rendering dt to 60Hz (2 physics steps for each rendering)
>>> simulation_context.set_simulation_dt(physics_dt=1.0 / 120.0, rendering_dt=1.0 / 60.0)
```

skip_next_stage_open_callback()
Skip the next stage_open_callback_fn trigger

stage_callback_exists(callback_name:str)→bool
Check if a stage callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_stage'
>>> simulation_context.stage_callback_exists("callback_stage")
True
```

step(
render:bool=True,
update_fabric:bool=False,
)→None Steps the physics simulation while rendering or without.
Warning
Calling this method with the `render` parameter set to True (default value) is not intended to be used in the Isaac Sim’s Extensions workflow since the Kit application has the control over the rendering steps
Parameters:

- render (bool, optional) – Set to False to only do a physics simulation without rendering. Note: app UI will be frozen (since its not rendering) in this case. Defaults to True.

- update_fabric (bool) – Whether to force the update of the physics data to fabric when performing a physics-only step (without rendering). This flag should be enabled when it is desired to read updated data using the fabric interface after performing a physics-only step (e.g., XFormPrim’s world transform).

Raises:
Exception – if there is no stage currently opened

Example:

```
>>> simulation_context.step()
```

stop()→None
Stop the physics simulation
Example:

```
>>> simulation_context.stop()
```

asyncstop_async()→None
Stop the physics simulation
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.stop_async()
...
>>> run_coroutine(task())
```

timeline_callback_exists(callback_name:str)→bool
Check if a timeline callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_timeline'
>>> simulation_context.timeline_callback_exists("callback_timeline")
True
```

propertyapp:omni.kit.app.IApp
Returns:
Omniverse Kit Application interface

Return type:
omni.kit.app.IApp

Example:

```
>>> simulation_context.app
<omni.kit.app._app.IApp object at 0x...>
```

propertybackend:str
Returns:
current backend. Supported backends are: `"numpy"`, `"torch"` and `"warp"`

Return type:
str

Example:

```
>>> simulation_context.backend
numpy
```

propertybackend_utils
Get the current backend utils module

[TABLE]
Backend | Utils module
"numpy" | isaacsim.core.utils.numpy
"torch" | isaacsim.core.utils.torch
"warp" | isaacsim.core.utils.warp
[/TABLE]
Returns:
current backend utils module

Return type:
str

Example:

```
>>> simulation_context.backend_utils
<module 'isaacsim.core.utils.numpy'>
```

propertycurrent_time:float
Returns:
current time (simulated physical time) that have elapsed since the simulation was played

Return type:
float

Example:

```
>>> # given a running Isaac Sim instance and after 911 physics steps at 60 Hz
>>> simulation_context.current_time
15.183334125205874
```

propertycurrent_time_step_index:int
Returns:
current number of physics steps that have elapsed since the simulation was played

Return type:
int

Example:

```
>>> # given a running Isaac Sim instance and after approximately 15 seconds of physics simulation at 60 Hz
>>> simulation_context.current_time_step_index
911
```

propertydevice:str
Returns:
Device used by the physics context. None for numpy backend

Return type:
str

Example:

```
>>> simulation_context.device
None
```

propertyphysics_sim_view
Note
The physics simulation view instance will be only available after initializing the physics (see `initialize_physics`) or resetting the simulation context (see `reset`)
Returns:
Physics simulation view instance

Return type:
PhysicsContext

Example:

```
>>> simulation_context.physics_sim_view
<omni.physics.tensors.impl.api.SimulationView object at 0x...>
```

propertystage:pxr.Usd.Stage
Returns:
current open USD stage

Return type:
Usd.Stage

Example:

```
>>> simulation_context.stage
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x...:World....usd'),
sessionLayer=Sdf.Find('anon:0x...:World...-session.usda'),
pathResolverContext=<invalid repr>)
```

#### World
classWorld(*args, **kwargs)
Bases: SimulationContext
This class inherits from SimulationContext which provides the following.
SimulationContext provide functions that take care of many time-related events such as perform a physics or a render step for instance. Adding/ removing callback functions that gets triggered with certain events such as a physics step, timeline event (pause or play..etc), stage open/ close..etc.
It also includes an instance of PhysicsContext which takes care of many physics related settings such as setting physics dt, solver type..etc.
In addition to what is provided from SimulationContext, this class allows the user to add a task to the world and it contains a scene object.
To control the default reset state of different objects easily, the object could be added to a Scene. Besides this, the object is bound to a short keyword that facilitates objects retrievals, like in a dict.
Checkout the required tutorials at https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
Parameters:

- physics_dt (Optional[float], optional) – dt between physics steps. Defaults to None.

- rendering_dt (Optional[float], optional) – dt between rendering steps. Note: rendering means rendering a frame of the current application and not only rendering a frame to the viewports/ cameras. So UI elements of Isaac Sim will be refreshed with this dt as well if running non-headless. Defaults to None.

- stage_units_in_meters (Optional[float], optional) – The metric units of assets. This will affect gravity value..etc. Defaults to None.

- physics_prim_path (Optional[str], optional) – specifies the prim path to create a PhysicsScene at, only in the case where no PhysicsScene already defined. Defaults to “/physicsScene”.

- set_defaults (bool, optional) – set to True to use the defaults settings [physics_dt = 1.0/ 60.0, stage units in meters = 0.01 (i.e in cms), rendering_dt = 1.0 / 60.0, gravity = -9.81 m / s ccd_enabled, stabilization_enabled, gpu dynamics turned off, broadcast type is MBP, solver type is TGS]. Defaults to True.

- backend (str, optional) – specifies the backend to be used (numpy or torch or warp). Defaults to numpy.

- device (Optional[str], optional) – specifies the device to be used if running on the gpu with torch or warp backends.

Example:

```
>>> from isaacsim.core.api import World
>>>
>>> world = World()
>>> world
<isaacsim.core.api.world.world.World object at 0x...>
```
add_physics_callback(
callback_name:str,
callback_fn:Callable[[float],None ],
)→None Add a callback which will be called before each physics step.
`callback_fn` should take a float argument (e.g., `step_size`)
Parameters:

- callback_name (str) – should be unique.

- callback_fn (Callable[[float], None]) – [description]

Example:

```
>>> def callback_physics(step_size):
... print("physics callback -> step_size:", step_size)
...
>>> simulation_context.add_physics_callback("callback_physics", callback_physics)
```

add_render_callback(
callback_name:str,
callback_fn:Callable,
)→None Add a callback which will be called after each rendering event such as .render().
`callback_fn` should take an argument of type (e.g., `event`)
Parameters:

- callback_name (str) – [description]

- callback_fn (Callable) – [description]

Example:

```
>>> def callback_render(event):
... print("render callback -> event:", event)
...
>>> simulation_context.add_render_callback("callback_render", callback_render)
```

add_stage_callback(
callback_name:str,
callback_fn:Callable,
)→None Add a callback which will be called after each stage event such as open/close among others
`callback_fn` should take an argument of type `omni.usd.StageEvent` (e.g., `event`)
Parameters:

- callback_name (str) – [description]

- callback_fn (Callable[[omni.usd.StageEvent], None]) – [description]

Example:

```
>>> def callback_stage(event):
... print("stage callback -> event:", event)
...
>>> simulation_context.add_stage_callback("callback_stage", callback_stage)
```

add_task(
task:BaseTask ,
)→None Add a task to the task registry
Note
Tasks should have a unique name
Parameters:
task (BaseTask ) – task object

Example:

```
>>> from isaacsim.core.api.tasks import BaseTask
>>>
>>> class Task(BaseTask):
... def get_observations(self):
... return {'obs': [0]}
...
... def calculate_metrics(self):
... return {"reward": 1}
...
... def is_done(self):
... return False
...
>>> task = Task(name="custom_task")
>>> world.add_task(task)
```

add_timeline_callback(
callback_name:str,
callback_fn:Callable,
)→None Add a callback which will be called after each timeline event such as play/pause.
`callback_fn` should take an argument of type `omni.timeline.TimelineEvent` (e.g., `event`)
Parameters:

- callback_name (str) – [description]

- callback_fn (Callable[[omni.timeline.TimelineEvent], None]) – [description]

Example:

```
>>> def callback_timeline(event):
... print("timeline callback -> event:", event)
...
>>> simulation_context.add_timeline_callback("callback_timeline", callback_timeline)
```

calculate_metrics(task_name:str|None =None)→None
Get metrics from all the tasks that were added
Parameters:
task_name (Optional[str], optional) – task name to ask for. Defaults to None, which means all the tasks

Returns:
the computed task (or all tasks) metric

Return type:
dict

Example:

```
>>> world.calculate_metrics("custom_task")
{'reward': 1}
```

clear()→None
Clear the current stage leaving the PhysicsScene and /World
Example:

```
>>> world.clear()
```

clear_all_callbacks()→None
Clear all callbacks which were added using any `add_*_callback` method
Example:

```
>>> simulation_context.clear_render_callbacks()
```

classmethodclear_instance()
Delete the world object, if it was instantiated before, and destroy any subscribed callback
Example:

```
>>> World.clear_instance()
```

clear_physics_callbacks()→None
Remove all registered physics callbacks
Example:

```
>>> simulation_context.clear_physics_callbacks()
```

clear_render_callbacks()→None
Remove all registered render callbacks
Example:

```
>>> simulation_context.clear_render_callbacks()
```

clear_stage_callbacks()→None
Remove all registered stage callbacks
Example:

```
>>> simulation_context.clear_stage_callbacks()
```

clear_timeline_callbacks()→None
Remove all registered timeline callbacks
Example:

```
>>> simulation_context.clear_timeline_callbacks()
```

get_block_on_render()→bool
Get the block on render flag for the simulation thread
Returns:
True if one frame lag between any data captured from the render products and the current USD stage is guaranteed by blocking the step call.

Return type:
bool

Example:

```
>>> simulation_context.get_block_on_render()
False
```

get_current_tasks()→List[BaseTask ]
Get a dictionary of the registered tasks where keys are task names
Returns:
registered tasks

Return type:
List[BaseTask ]

Example:

```
>>> world.get_current_tasks()
{'custom_task': <custom.task.scripts.extension.Task object at 0x...>}
```

get_data_logger()→DataLogger
Return the data logger of the world.
Returns:
data logger instance

Return type:
DataLogger

Example:

```
>>> world.get_data_logger()
<isaacsim.core.api.loggers.data_logger.DataLogger object at 0x...>
```

get_observations(task_name:str|None =None)→dict
Get observations from all the tasks that were added
Parameters:
task_name (Optional[str], optional) – task name to ask for. Defaults to None, which means all the tasks

Returns:
the task (or all tasks) observations

Return type:
dict

Example:

```
>>> world.get_observations("custom_task")
{'obs': [0]}
```

get_physics_context()→PhysicsContext
Get the physics context (a class to deal with a physics scene and its settings) instance
Raises:
Exception – if there is no stage currently opened

Returns:
physics context object

Return type:
PhysicsContext

Example:

```
>>> simulation_context.get_physics_context()
<isaacsim.core.api.physics_context.physics_context.PhysicsContext object at 0x...>
```

get_physics_dt()→float
Get the current physics dt of the physics context
Raises:
Exception – if there is no stage currently opened

Returns:
current physics dt of the PhysicsContext

Return type:
float

Example:

```
>>> simulation_context.get_physics_dt()
0.016666666666666666
```

get_rendering_dt()→float
Get the current rendering dt
Raises:
Exception – if there is no stage currently opened

Returns:
current rendering dt

Return type:
float

Example:

```
>>> simulation_context.get_rendering_dt()
0.016666666666666666
```

get_task(
name:str,
)→BaseTask Get a task by its name
Example:

```
>>> world.get_task("custom_task")
<custom.task.scripts.extension.Task object at 0x...>
```

initialize_physics()→None
Initialize the physics simulation view and each added object to the Scene
Example:

```
>>> world.initialize_physics()
```

asyncinitialize_simulation_context_async()→None
Initialize the simulation context
Hint
This method is intended to be used in the Isaac Sim’s Extensions workflow where the Kit application has the control over timing of physics and rendering steps
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.initialize_simulation_context_async()
...
>>> run_coroutine(task())
```

classmethodinstance()→SimulationContext
Get the instance of the class, if it was instantiated before
Returns:
SimulationContext object or None

Return type:
SimulationContext

Example:

```
>>> # given that the class has already been instantiated before
>>> simulation_context = SimulationContext.instance()
>>> simulation_context
<isaacsim.core.api.simulation_context.simulation_context.SimulationContext object at 0x...>
```

is_done(task_name:str|None =None)→bool
Get done from all the tasks that were added
Parameters:
task_name (Optional[str], optional) – task name to ask for. Defaults to None, which means all the tasks

Returns:
whether the task (or all tasks) is done

Return type:
bool

Example:

```
>>> world.is_done("custom_task")
False
```

is_playing()→bool
Check whether the simulation is playing
Returns:
True if the simulator is playing.

Return type:
bool

Example:

```
>>> # given a simulation in play
>>> simulation_context.is_playing()
True
```

is_simulating()→bool
Check whether the simulation is running or not
Warning
With deprecation of Dynamic Control Toolbox, this function is not needed
It can return True if start_simulation is called even if play was pressed/called.
Returns:
bool” True if physics simulation is happening.

Example:

```
>>> # given a running simulation
>>> simulation_context.is_simulating()
True
```

is_stopped()→bool
Check whether the simulation is playing
Returns:
True if the simulator is stopped.

Return type:
bool

Example:

```
>>> # given a simulation in play
>>> simulation_context.is_stopped()
False
```

is_tasks_scene_built()→bool
Check if the `set_up_scene` method was called for each registered task
Example:

```
>>> # given a world instance that was rested at some point
>>> world.is_tasks_scene_built()
True
```

pause()→None
Pause the physics simulation
Example:

```
>>> simulation_context.pause()
```

asyncpause_async()→None
Pause the physics simulation
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.pause_async()
...
>>> run_coroutine(task())
```

physics_callback_exists(callback_name:str)→bool
Check if a physics callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_physics'
>>> simulation_context.physics_callback_exists("callback_physics")
True
```

play()→None
Start playing simulation
Note
It does one step internally to propagate all physics handles properly.
Example:

```
>>> simulation_context.play()
```

asyncplay_async()→None
Start playing simulation
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.play_async()
...
>>> run_coroutine(task())
```

remove_physics_callback(callback_name:str)→None
Remove a physics callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'callback_physics'
>>> simulation_context.remove_physics_callback("callback_physics")
```

remove_render_callback(callback_name:str)→None
Remove a render callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'callback_render'
>>> simulation_context.remove_render_callback("callback_render")
```

remove_stage_callback(callback_name:str)→None
Remove a stage callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'callback_stage'
>>> simulation_context.remove_stage_callback("callback_stage")
```

remove_timeline_callback(callback_name:str)→None
Remove a timeline callback by its name
Parameters:
callback_name (str) – callback name

Example:

```
>>> # given a registered callback named 'timeline'
>>> simulation_context.timeline_callback("timeline")
```

render()→None
Refresh the Isaac Sim app rendering components including UI elements, viewports and others
Warning
This method is not intended to be used in the Isaac Sim’s Extensions workflow since the Kit application has the control over the rendering steps
Example:

```
>>> simulation_context.render()
```

asyncrender_async()→None
Refresh the Isaac Sim app rendering components including UI elements, viewports and others
Hint
This method is intended to be used in the Isaac Sim’s Extensions workflow where the Kit application has the control over timing of physics and rendering steps
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.render_async()
...
>>> run_coroutine(task())
```

render_callback_exists(callback_name:str)→bool
Check if a render callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_render'
>>> simulation_context.render_callback_exists("callback_render")
True
```

reset(soft:bool=False)→None
Reset the stage to its initial state and each object included in the Scene to its default state
as specified by the `set_default_state` and `__init__` methods

Note

- All tasks should be added before the first reset is called unless the `clear` method was called.

- All articulations should be added before the first reset is called unless the `clear` method was called.

- This method takes care of initializing articulation handles with the first reset called.

- This will do one step internally regardless

- Call `post_reset` on each object in the Scene

- Call `post_reset` on each Task

Things like setting PD gains for instance should happen at a Task reset or a Robot reset since the defaults are restored after `stop` method is called.
Warning
This method is not intended to be used in the Isaac Sim’s Extensions workflow since the Kit application has the control over the rendering steps. For the Extensions workflow use the `reset_async` method instead
Parameters:
soft (bool, optional) – if set to True simulation won’t be stopped and start again. It only calls the reset on the scene objects.

Example:

```
>>> world.reset()
```

asyncreset_async(soft:bool=False)→None
Reset the stage to its initial state and each object included in the Scene to its default state
as specified by the `set_default_state` and `__init__` methods

Note

- All tasks should be added before the first reset is called unless the `clear` method was called.

- All articulations should be added before the first reset is called unless the `clear` method was called.

- This method takes care of initializing articulation handles with the first reset called.

- This will do one step internally regardless

- Call `post_reset` on each object in the Scene

- Call `post_reset` on each Task

Things like setting PD gains for instance should happen at a Task reset or a Robot reset since the defaults are restored after `stop` method is called.
Parameters:
soft (bool, optional) – if set to True simulation won’t be stopped and start again. It only calls the reset on the scene objects.

Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await world.reset_async()
...
>>> run_coroutine(task())
```

asyncreset_async_no_set_up_scene(soft:bool=False)→None
Reset the stage to its initial state and each object included in the Scene to its default state
as specified by the `set_default_state` and `__init__` methods

Note

- All tasks should be added before the first reset is called unless the `clear` method was called.

- All articulations should be added before the first reset is called unless the `clear` method was called.

- This method takes care of initializing articulation handles with the first reset called.

- This will do one step internally regardless

- Call `post_reset` on each object in the Scene

- Call `post_reset` on each Task

Things like setting PD gains for instance should happen at a Task reset or a Robot reset since the defaults are restored after `stop` method is called.
Parameters:
soft (bool, optional) – if set to True simulation won’t be stopped and start again. It only calls the reset on the scene objects.

Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
>>> await world.reset_async_no_set_up_scene()
>>>
>>> run_coroutine(task())
```

asyncreset_async_set_up_scene(soft:bool=False)→None
Reset the stage to its initial state and each object included in the Scene to its default state
as specified by the `set_default_state` and `__init__` methods

Note

- All tasks should be added before the first reset is called unless the `clear` method was called.

- All articulations should be added before the first reset is called unless the `clear` method was called.

- This method takes care of initializing articulation handles with the first reset called.

- This will do one step internally regardless

- Call `post_reset` on each object in the Scene

- Call `post_reset` on each Task

Things like setting PD gains for instance should happen at a Task reset or a Robot reset since the defaults are restored after `stop` method is called.
Parameters:
soft (bool, optional) – if set to True simulation won’t be stopped and start again. It only calls the reset on the scene objects.

Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
>>> await world.reset_async_set_up_scene()
>>>
>>> run_coroutine(task())
```

set_block_on_render(block:bool)→None
Set block on render flag for the simulation thread
Note
This guarantee a one frame lag between any data captured from the render products and the current USD stage if enabled.
Parameters:
block (bool) – True to block the thread until the renderer is done.

Example:

```
>>> simulation_context.set_block_on_render(False)
```

set_simulation_dt(
physics_dt:float|None =None,
rendering_dt:float|None =None,
)→None Specify the physics step and rendering step size to use when stepping and rendering.
Parameters:

- physics_dt (float) – The physics time-step. None means it won’t change the current setting. (default: None).

- rendering_dt (float) – The rendering time-step. None means it won’t change the current setting. (default: None)

Hint
It is recommended that the two values be divisible, with the `rendering_dt` being equal to or greater than the `physics_dt`
Example:

```
>>> set physics dt to 120 Hz and rendering dt to 60Hz (2 physics steps for each rendering)
>>> simulation_context.set_simulation_dt(physics_dt=1.0 / 120.0, rendering_dt=1.0 / 60.0)
```

skip_next_stage_open_callback()
Skip the next stage_open_callback_fn trigger

stage_callback_exists(callback_name:str)→bool
Check if a stage callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_stage'
>>> simulation_context.stage_callback_exists("callback_stage")
True
```

step(
render:bool=True,
step_sim:bool=True,
update_fabric:bool=False,
)→None Step the physics simulation while rendering or without.
Note
The `pre_step` for each task is called before stepping. This method also update the Bounding Box Cache time for computing bounding box if enabled
Warning
Calling this method with the `render` parameter set to True (default value) is not intended to be used in the Isaac Sim’s Extensions workflow since the Kit application has the control over the rendering steps
Parameters:

- render (bool, optional) – Set to False to only do a physics simulation without rendering. Note: app UI will be frozen (since its not rendering) in this case. Defaults to True.

- step_sim (bool) – True to step simulation (physics and/or rendering)

- update_fabric (bool) – Whether to force the update of the physics data to fabric when performing a physics-only step (without rendering). This flag should be enabled when it is desired to read updated data using the fabric interface after performing a physics-only step (e.g., XFormPrim’s world transform).

Example:

```
>>> world.step()
```

step_async(step_size:float|None =None)→None
Call all functions that should be called pre stepping the physics
Note
The `pre_step` for each task is called before stepping. This method also update the Bounding Box Cache time for computing bounding box if enabled
Parameters:
step_size (float) – step size

Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await world.step_async()
...
>>> run_coroutine(task())
```

stop()→None
Stop the physics simulation
Example:

```
>>> simulation_context.stop()
```

asyncstop_async()→None
Stop the physics simulation
Example:

```
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await simulation_context.stop_async()
...
>>> run_coroutine(task())
```

timeline_callback_exists(callback_name:str)→bool
Check if a timeline callback exists
Parameters:
callback_name (str) – callback name

Returns:
whether the callback is registered

Return type:
bool

Example:

```
>>> # given a registered callback named 'callback_timeline'
>>> simulation_context.timeline_callback_exists("callback_timeline")
True
```

propertyapp:omni.kit.app.IApp
Returns:
Omniverse Kit Application interface

Return type:
omni.kit.app.IApp

Example:

```
>>> simulation_context.app
<omni.kit.app._app.IApp object at 0x...>
```

propertybackend:str
Returns:
current backend. Supported backends are: `"numpy"`, `"torch"` and `"warp"`

Return type:
str

Example:

```
>>> simulation_context.backend
numpy
```

propertybackend_utils
Get the current backend utils module

[TABLE]
Backend | Utils module
"numpy" | isaacsim.core.utils.numpy
"torch" | isaacsim.core.utils.torch
"warp" | isaacsim.core.utils.warp
[/TABLE]
Returns:
current backend utils module

Return type:
str

Example:

```
>>> simulation_context.backend_utils
<module 'isaacsim.core.utils.numpy'>
```

propertycurrent_time:float
Returns:
current time (simulated physical time) that have elapsed since the simulation was played

Return type:
float

Example:

```
>>> # given a running Isaac Sim instance and after 911 physics steps at 60 Hz
>>> simulation_context.current_time
15.183334125205874
```

propertycurrent_time_step_index:int
Returns:
current number of physics steps that have elapsed since the simulation was played

Return type:
int

Example:

```
>>> # given a running Isaac Sim instance and after approximately 15 seconds of physics simulation at 60 Hz
>>> simulation_context.current_time_step_index
911
```

propertydevice:str
Returns:
Device used by the physics context. None for numpy backend

Return type:
str

Example:

```
>>> simulation_context.device
None
```

propertyphysics_sim_view
Note
The physics simulation view instance will be only available after initializing the physics (see `initialize_physics`) or resetting the simulation context (see `reset`)
Returns:
Physics simulation view instance

Return type:
PhysicsContext

Example:

```
>>> simulation_context.physics_sim_view
<omni.physics.tensors.impl.api.SimulationView object at 0x...>
```

propertyscene:Scene
Returns:
Scene instance

Return type:
Scene

Example:

```
>>> world.scene
<isaacsim.core.api.scenes.scene.Scene object at 0x>
```

propertystage:pxr.Usd.Stage
Returns:
current open USD stage

Return type:
Usd.Stage

Example:

```
>>> simulation_context.stage
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x...:World....usd'),
sessionLayer=Sdf.Find('anon:0x...:World...-session.usda'),
pathResolverContext=<invalid repr>)
```

#### Tasks
classBaseTask(name:str, offset:ndarray|None =None)
Bases: `object`
This class provides a way to set up a task in a scene and modularize adding objects to stage, getting observations needed for the behavioral layer, calculating metrics needed about the task, calling certain things pre-stepping, creating multiple tasks at the same time and much more.
Checkout the required tutorials at https://docs.isaacsim.omniverse.nvidia.com/latest/index.html
Parameters:

- name (str) – needs to be unique if added to the World.

- offset (Optional[np.ndarray], optional) – offset applied to all assets of the task.

calculate_metrics()→dict
[summary]
Raises:
NotImplementedError – [description]

cleanup()→None
Called before calling a reset() on the world to removed temporary objects that were added during simulation for instance.

get_description()→str
[summary]
Returns:
[description]

Return type:
str

get_observations()→dict
Returns current observations from the objects needed for the behavioral layer.
Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
dict

get_params()→dict
Gets the parameters of the task.
This is defined differently for each task in order to access the task’s objects and values. Note that this is different from get_observations. Things like the robot name, block name..etc can be defined here for faster retrieval. should have the form of params_representation[“param_name”] = {“value”: param_value, “modifiable”: bool}

Raises:
NotImplementedError – [description]

Returns:
defined parameters of the task.

Return type:
dict

get_task_objects()→dict
[summary]
Returns:
[description]

Return type:
dict

is_done()→bool
Returns True of the task is done.
Raises:
NotImplementedError – [description]

post_reset()→None
Calls while doing a .reset() on the world.

pre_step(
time_step_index:int,
simulation_time:float,
)→None called before stepping the physics simulation.
Parameters:

- time_step_index (int) – [description]

- simulation_time (float) – [description]

set_params(*args, **kwargs)→None
Changes the modifiable parameters of the task
Raises:
NotImplementedError – [description]

set_up_scene(
scene:Scene ,
)→None Adding assets to the stage as well as adding the encapsulated objects such as SingleXFormPrim..etc
to the task_objects happens here.

Parameters:
scene (Scene ) – [description]

propertydevice
propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyscene:Scene
Scene of the world
Returns:
[description]

Return type:
Scene

classFollowTarget(
name:str,
target_prim_path:str|None =None,
target_name:str|None =None,
target_position:ndarray|None =None,
target_orientation:ndarray|None =None,
offset:ndarray|None =None,
)Bases: `ABC`, BaseTask
[summary]
Parameters:

- name (str) – [description]

- target_prim_path (Optional[str], optional) – [description]. Defaults to None.

- target_name (Optional[str], optional) – [description]. Defaults to None.

- target_position (Optional[np.ndarray], optional) – [description]. Defaults to None.

- target_orientation (Optional[np.ndarray], optional) – [description]. Defaults to None.

- offset (Optional[np.ndarray], optional) – [description]. Defaults to None.

add_obstacle(position:ndarray=None)
[summary]
Parameters:
position (np.ndarray, optional) – [description]. Defaults to np.array([0.1, 0.1, 1.0]).

calculate_metrics()→dict
[summary]

cleanup()→None
[summary]

get_description()→str
[summary]
Returns:
[description]

Return type:
str

get_observations()→dict
[summary]
Returns:
[description]

Return type:
dict

get_obstacle_to_delete()→None
[summary]
Returns:
[description]

Return type:
[type]

get_params()→dict
[summary]
Returns:
[description]

Return type:
dict

get_task_objects()→dict
[summary]
Returns:
[description]

Return type:
dict

is_done()→bool
[summary]

obstacles_exist()→bool
[summary]
Returns:
[description]

Return type:
bool

post_reset()→None
[summary]

pre_step(
time_step_index:int,
simulation_time:float,
)→None [summary]
Parameters:

- time_step_index (int) – [description]

- simulation_time (float) – [description]

remove_obstacle(name:str|None =None)→None
[summary]
Parameters:
name (Optional[str], optional) – [description]. Defaults to None.

set_params(
target_prim_path:str|None =None,
target_name:str|None =None,
target_position:ndarray|None =None,
target_orientation:ndarray|None =None,
)→None [summary]
Parameters:

- target_prim_path (Optional[str], optional) – [description]. Defaults to None.

- target_name (Optional[str], optional) – [description]. Defaults to None.

- target_position (Optional[np.ndarray], optional) – [description]. Defaults to None.

- target_orientation (Optional[np.ndarray], optional) – [description]. Defaults to None.

abstractset_robot()→None
[summary]
Raises:
NotImplementedError – [description]

set_up_scene(
scene:Scene ,
)→None [summary]
Parameters:
scene (Scene ) – [description]

target_reached()→bool
[summary]
Returns:
[description]

Return type:
bool

propertydevice
propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyscene:Scene
Scene of the world
Returns:
[description]

Return type:
Scene

classPickPlace(
name:str,
cube_initial_position:ndarray|None =None,
cube_initial_orientation:ndarray|None =None,
target_position:ndarray|None =None,
cube_size:ndarray|None =None,
offset:ndarray|None =None,
)Bases: `ABC`, BaseTask
[summary]
Parameters:

- name (str) – [description]

- cube_initial_position (Optional[np.ndarray], optional) – [description]. Defaults to None.

- cube_initial_orientation (Optional[np.ndarray], optional) – [description]. Defaults to None.

- target_position (Optional[np.ndarray], optional) – [description]. Defaults to None.

- cube_size (Optional[np.ndarray], optional) – [description]. Defaults to None.

- offset (Optional[np.ndarray], optional) – [description]. Defaults to None.

calculate_metrics()→dict
[summary]

cleanup()→None
Called before calling a reset() on the world to removed temporary objects that were added during simulation for instance.

get_description()→str
[summary]
Returns:
[description]

Return type:
str

get_observations()→dict
[summary]
Returns:
[description]

Return type:
dict

get_params()→dict
Gets the parameters of the task.
This is defined differently for each task in order to access the task’s objects and values. Note that this is different from get_observations. Things like the robot name, block name..etc can be defined here for faster retrieval. should have the form of params_representation[“param_name”] = {“value”: param_value, “modifiable”: bool}

Raises:
NotImplementedError – [description]

Returns:
defined parameters of the task.

Return type:
dict

get_task_objects()→dict
[summary]
Returns:
[description]

Return type:
dict

is_done()→bool
[summary]

post_reset()→None
Calls while doing a .reset() on the world.

pre_step(
time_step_index:int,
simulation_time:float,
)→None [summary]
Parameters:

- time_step_index (int) – [description]

- simulation_time (float) – [description]

set_params(
cube_position:ndarray|None =None,
cube_orientation:ndarray|None =None,
target_position:ndarray|None =None,
)→None Changes the modifiable parameters of the task
Raises:
NotImplementedError – [description]

abstractset_robot()→None
set_up_scene(
scene:Scene ,
)→None [summary]
Parameters:
scene (Scene ) – [description]

propertydevice
propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyscene:Scene
Scene of the world
Returns:
[description]

Return type:
Scene

classStacking(
name:str,
cube_initial_positions:ndarray,
cube_initial_orientations:ndarray|None =None,
stack_target_position:ndarray|None =None,
cube_size:ndarray|None =None,
offset:ndarray|None =None,
)Bases: `ABC`, BaseTask
[summary]
Parameters:

- name (str) – [description]

- cube_initial_positions (np.ndarray) – [description]

- cube_initial_orientations (Optional[np.ndarray], optional) – [description]. Defaults to None.

- stack_target_position (Optional[np.ndarray], optional) – [description]. Defaults to None.

- cube_size (Optional[np.ndarray], optional) – [description]. Defaults to None.

- offset (Optional[np.ndarray], optional) – [description]. Defaults to None.

calculate_metrics()→dict
[summary]
Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
dict

cleanup()→None
Called before calling a reset() on the world to removed temporary objects that were added during simulation for instance.

get_cube_names()→List[str]
[summary]
Returns:
[description]

Return type:
List[str]

get_description()→str
[summary]
Returns:
[description]

Return type:
str

get_observations()→dict
[summary]
Returns:
[description]

Return type:
dict

get_params()→dict
[summary]
Returns:
[description]

Return type:
dict

get_task_objects()→dict
[summary]
Returns:
[description]

Return type:
dict

is_done()→bool
[summary]
Raises:
NotImplementedError – [description]

Returns:
[description]

Return type:
bool

post_reset()→None
[summary]

pre_step(
time_step_index:int,
simulation_time:float,
)→None [summary]
Parameters:

- time_step_index (int) – [description]

- simulation_time (float) – [description]

set_params(
cube_name:str|None =None,
cube_position:str|None =None,
cube_orientation:str|None =None,
stack_target_position:str|None =None,
)→None [summary]
Parameters:

- cube_name (Optional[str], optional) – [description]. Defaults to None.

- cube_position (Optional[str], optional) – [description]. Defaults to None.

- cube_orientation (Optional[str], optional) – [description]. Defaults to None.

- stack_target_position (Optional[str], optional) – [description]. Defaults to None.

abstractset_robot()→None
[summary]
Raises:
NotImplementedError – [description]

set_up_scene(
scene:Scene ,
)→None [summary]
Parameters:
scene (Scene ) – [description]

propertydevice
propertyname:str
[summary]
Returns:
[description]

Return type:
str

propertyscene:Scene
Scene of the world
Returns:
[description]

Return type:
Scene
