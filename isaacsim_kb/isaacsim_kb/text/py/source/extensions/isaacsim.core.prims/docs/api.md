<!-- source: py/source/extensions/isaacsim.core.prims/docs/api.html | title: API — Isaac Sim -->

# API

## Python API
Warning
The use of Single Prim classes (a particular case of the Prims classes for a single prim) is discouraged as they will be removed in future versions. Use Prims classes (formerly Prim Views) instead.
Prims

[TABLE]
Articulation | High level wrapper to deal with prims (one or many) that have the Root Articulation API applied and their attributes/properties
ClothPrim | The view class for cloth prims.
DeformablePrim | The view class for deformable prims.
GeometryPrim | High level wrapper to deal with geom prims (one or many) as well as their attributes/properties.
ParticleSystem | Provides high level functions to deal with particle systems (1 or more particle systems) as well as its attributes/ properties.
RigidPrim | Provides high level functions to deal with prims (one or many) that have Rigid Body API applied to them as well as their attributes/properties.
SdfShapePrim | High level functions to deal with geometry prims that provide their Signed Distance Field (SDF).
XFormPrim | Provides high level functions to deal with a Xform prim view (one or many) and its descendants as well as its attributes/properties.
[/TABLE]
Single Prims

[TABLE]
SingleArticulation | High level wrapper to deal with an articulation prim (only one articulation prim) and its attributes/properties.
SingleClothPrim | Cloth primitive object provide functionalities to create and control cloth parameters
SingleDeformablePrim | Deformable primitive object provide functionalities to create and control deformable objects
SingleGeometryPrim | High level wrapper to deal with a Geom prim (only one geometry prim) and its attributes/properties.
SingleParticleSystem | A wrapper around PhysX particle system.
SingleRigidPrim | High level wrapper to deal with a rigid body prim (only one rigid body prim) and its attributes/properties.
SingleXFormPrim | Provides high level functions to deal with an Xform prim (only one Xform prim) and its attributes/properties
[/TABLE]

### Prims
classArticulation(
prim_paths_expr:str|List[str],
name:str='articulation_prim_view',
positions:ndarray|Tensor|warp.array|None =None,
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
scales:ndarray|Tensor|warp.array|None =None,
visibilities:ndarray|Tensor|warp.array|None =None,
reset_xform_properties:bool=True,
enable_residual_reports:bool=False,
)Bases: XFormPrim
High level wrapper to deal with prims (one or many) that have the Root Articulation API applied and their attributes/properties
This class wraps all matching articulations found at the regex provided at the `prim_paths_expr` argument
Note
Each prim will have `xformOp:orient`, `xformOp:translate` and `xformOp:scale` only post-init, unless it is a non-root articulation link.
Warning
The articulation view object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Parameters:

- prim_paths_expr (Union[str, List[str]]) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Franka” will match /World/Env1/Franka, /World/Env2/Franka..etc. (a non regex prim path can also be used to encapsulate one rigid prim).

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “articulation_prim_view”.

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default positions in the world frame of the prims. shape is (N, 3). Defaults to None, which means left unchanged.

- translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default quaternion orientations in the world/ local frame of the prims (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (N, 4).

- scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – local scales to be applied to the prim’s dimensions in the view. shape is (N, 3). Defaults to None, which means left unchanged.

- visibilities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – set to false for an invisible prim in the stage while rendering. shape is (N,). Defaults to None.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- enable_residual_reports (bool optional) – Setting to True will enable using the residual reporting APIs. Defaults to False.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.cloner import GridCloner
>>> from isaacsim.core.prims import Articulation
>>> from pxr import UsdGeom
>>>
>>> usd_path = "/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd"
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
>>> # wrap all articulations
>>> prims = Articulation(prim_paths_expr="/World/envs/env.*/panda", name="franka_panda_view")
>>> prims
<isaacsim.core.prims.articulation.Articulation object at 0x7ff174054b20>
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
Reset the prims to its default state
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

classClothPrim(
prim_paths_expr:str,
particle_systems:ndarray|Tensor=None,
particle_materials:ndarray|Tensor|None =None,
name:str='cloth_prim_view',
reset_xform_properties:bool=True,
positions:ndarray|Tensor|None =None,
translations:ndarray|Tensor|None =None,
orientations:ndarray|Tensor|None =None,
scales:ndarray|Tensor|None =None,
visibilities:ndarray|Tensor|None =None,
particle_masses:ndarray|Tensor|None =None,
pressures:ndarray|Tensor|None =None,
particle_groups:ndarray|Tensor|None =None,
self_collisions:ndarray|Tensor|None =None,
self_collision_filters:ndarray|Tensor|None =None,
stretch_stiffnesses:ndarray|Tensor|None =None,
bend_stiffnesses:ndarray|Tensor|None =None,
shear_stiffnesses:ndarray|Tensor|None =None,
spring_dampings:ndarray|Tensor|None =None,
)Bases: XFormPrim
The view class for cloth prims.
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

get_cloths_bend_stiffnesses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the value of bend stiffness set to all the springs within cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
bend stiffness tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_cloths_dampings(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the value of damping set for all the springs within cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
damping tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_cloths_shear_stiffnesses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the value of shear stiffness set to all the springs within cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
shear stiffness tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_cloths_stretch_stiffnesses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the value of stretch stiffness set to all the springs within cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
stretch stiffness tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

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

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame)
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
first index is translations in the local frame of the prims. shape is (M, 3).
second index is quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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

get_particle_groups(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the particle groups of the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
particle groups with shape (M, ).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_particle_masses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the particle masses for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
mass tensor with shape (M, max_particles_per_cloth)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_pressures(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the pressures of the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
cloths pressure with shape (M, ).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_self_collision_filters(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the self collision filters for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the self collision filters tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_self_collisions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the self collision for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the self collision tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_spring_dampings(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the spring damping for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
damping tensor with shape (M, max_springs_per_cloth)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_stretch_stiffnesses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the spring stretch stiffness for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
stiffness tensor with shape (M, max_springs_per_cloth)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_velocities(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the particle velocities for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
velocity tensor with shape (M, max_particles_per_cloth, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

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
usd:bool=True,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get the poses of the prims in the view with respect to the world’s frame
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Returns:
first index is positions in the world frame of the prims. shape is (M, 3).
second index is quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
```

get_world_positions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the particle world positions for the cloths indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
position tensor with shape (M, max_particles_per_cloth, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

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
)→None Create a physics simulation view if not passed and creates a rigid body view in physX.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_physics_handle_valid()→bool
Returns:
True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.

Return type:
bool

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

post_reset()→None
Reset the prims to its default state
Example:

```
>>> prims.post_reset()
```

set_cloths_bend_stiffnesses(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets a single value of bend stiffnesses to all the springs within cloths indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – cloth spring bend stiffness values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_cloths_dampings(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets a single value of damping to all the springs within cloths indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – cloth spring damping with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_cloths_shear_stiffnesses(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets a single value of shear stiffnesses to all the springs within cloths indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – cloth spring shear stiffness values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_cloths_stretch_stiffnesses(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets a single value of stretch stiffnesses to all the springs within cloths indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – cloth spring stretch stiffness values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

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

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame)
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
>>> # reposition all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs
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

set_particle_groups(
particle_groups:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle group of the cloths indicated by the indices.
Parameters:

- particle_groups (Union[np.ndarray, torch.Tensor]) – particle group with shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_particle_masses(
masses:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle masses for the cloths indicated by the indices.
Parameters:

- masses (Union[np.ndarray, torch.Tensor]) – cloth particle masses with the shape (M, max_particles_per_cloth, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_pressures(
pressures:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the pressures of the cloths indicated by the indices.
Parameters:

- pressures (Union[np.ndarray, torch.Tensor]) – cloths pressure with shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_self_collision_filters(
self_collision_filters:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the self collision filters for the cloths indicated by the indices.
Parameters:

- self_collision_filters (Union[np.ndarray, torch.Tensor]) – self collision filters with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_self_collisions(
self_collisions:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the self collision flags for the cloths indicated by the indices.
Parameters:

- self_collisions (Union[np.ndarray, torch.Tensor]) – self collision flag with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_spring_dampings(
damping:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the spring damping for the cloths indicated by the indices.
Parameters:

- damping (Union[np.ndarray, torch.Tensor]) – cloth spring damping with the shape (M, max_springs_per_cloth).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_stretch_stiffnesses(
stiffness:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the spring stretch stiffness values for springs within the cloths indicated by the indices.
Parameters:

- stiffness (Union[np.ndarray, torch.Tensor]) – cloth spring stiffness with the shape (M, max_springs_per_cloth).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_velocities(
velocities:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle velocities for the cloths indicated by the indices.
Parameters:

- velocities (Union[np.ndarray, torch.Tensor]) – particle velocities with the shape (M, max_particles_per_cloth, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

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
)→None Set prim poses in the view with respect to the world’s frame
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prims. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all prims in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
```

set_world_positions(
positions:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the particle world positions for the cloths indicated by the indices.
Parameters:

- positions (Union[np.ndarray, torch.Tensor]) – particle positions with the shape (M, max_particles_per_cloth, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which cloth prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

propertycount:int
Returns: int: cloth counts.

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

propertymax_particles_per_cloth:int
Returns: int: maximum number of particles per cloth.

propertymax_springs_per_cloth:int
Returns: int: maximum number of springs per cloth.

propertyname:str
Returns: str: name given to the prims view when instantiating it.

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

classDeformablePrim(
prim_paths_expr:str,
deformable_materials:ndarray|Tensor|None =None,
name:str='deformable_prim_view',
reset_xform_properties:bool=True,
positions:ndarray|Tensor|None =None,
translations:ndarray|Tensor|None =None,
orientations:ndarray|Tensor|None =None,
scales:ndarray|Tensor|None =None,
visibilities:ndarray|Tensor|None =None,
vertex_velocity_dampings:ndarray|Tensor|None =None,
sleep_dampings:ndarray|Tensor|None =None,
sleep_thresholds:ndarray|Tensor|None =None,
settling_thresholds:ndarray|Tensor|None =None,
self_collisions:ndarray|Tensor|None =None,
self_collision_filter_distances:ndarray|Tensor|None =None,
solver_position_iteration_counts:ndarray|Tensor|None =None,
)Bases: XFormPrim
The view class for deformable prims.
apply_deformable_materials(
deformable_materials:DeformableMaterial |List[DeformableMaterial ],
indices:ndarray|list|Tensor|None =None,
)→None Used to apply deformable material to prims in the view.
Parameters:

- deformable_materials (Union[DeformableMaterial , List[DeformableMaterial ]]) – deformable materials to be applied to prims in the view. Note: if a physics material is not defined, the defaults will be used from PhysX. If a list is provided then its size has to be equal the view’s size or indices size. If one material is provided it will be applied to all prims in the view.

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Raises:
Exception – length of physics materials != length of prims indexed

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
get_applied_deformable_materials(
indices:ndarray|list|Tensor|None =None,
)→List[DeformableMaterial ]Gets the applied deformable material to prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
the current applied deformable materials for prims in the view.

Return type:
List[DeformableMaterial ]

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

get_collision_mesh_element_deformation_gradients(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the collision mesh element-wise second-order deformation gradient tensors for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
collision mesh deformation gradients with shape (M, max_collision_mesh_elements_per_body, 3, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_collision_mesh_element_rest_poses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the collision mesh rest poses for the deformable bodies indicated by the indices. This method will return the 3x3 matrix inv([x1-x0, x2-x0, x3-x0]) where x0, x1, x2, x3 are the rest points of collision mesh elements
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
collision mesh rest poses with shape (M, max_collision_mesh_elements_per_body, 3, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_collision_mesh_element_rotations(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the collision mesh element-wise rotations as quaternions for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
collision mesh rotations with shape (M, max_collision_mesh_elements_per_body, 4)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_collision_mesh_element_stresses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the collision mesh element-wise second-order stress tensors for bodies indicated by the indices. This method will return the collision mesh element-wise stresses of the deformable bodies
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
collision mesh stresses with shape (M, max_collision_mesh_elements_per_body, 3, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_collision_mesh_indices(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the collision mesh element indices of the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
deformable bodies collision mesh element indices
with shape (M, self.max_collision_mesh_elements_per_body, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_collision_mesh_nodal_positions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the nodal positions of the collision mesh for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
position tensor with shape (M, max_collision_mesh_vertices_per_body, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

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

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame)
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
first index is translations in the local frame of the prims. shape is (M, 3).
second index is quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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

get_self_collision_filter_distances(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the self collision filter distance for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the self collision filter distance tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_self_collisions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the self collision parameters for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the self collision tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_settling_thresholds(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the settling threshold for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the settling threshold tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_element_deformation_gradients(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the simulation mesh element-wise second-order deformation gradient tensors for the deformable bodies indicated by the indices. This method will return the simulation mesh element-wise deformation gradient of the deformable bodies
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
simulation mesh element-wise deformation gradients with shape (M, max_simulation_mesh_elements_per_body, 3, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_element_rest_poses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the simulation mesh rest poses for the deformable bodies indicated by the indices. This method will return the 3x3 matrix inv([x1-x0, x2-x0, x3-x0]) where x0, x1, x2, x3 are the rest points of the simulation mesh elements
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
simulation mesh rest poses with
shape (M, max_simulation_mesh_elements_per_body, 3, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_element_rotations(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the simulation mesh element-wise rotations as quaternions for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
simulation mesh element-wise rotations with shape (M, max_simulation_mesh_elements_per_body, 4)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_element_stresses(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the simulation mesh element-wise second-order stress tensors for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
simulation mesh element-wise stresses with shape (M, max_simulation_mesh_elements_per_body, 3, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_indices(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the simulation mesh element indices of the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
deformable bodies simulation mesh element indices
with shape (M, self.max_simulation_mesh_elements_per_body, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_kinematic_targets(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the nodal kinematic targets of the simulation mesh for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
kinematic targets tensor,
with shape (M, max_simulation_mesh_vertices_per_body, 4) the first three components are the position targets and the last value (0 or 1) indicate whether the node is kinematically driven or not.

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_nodal_positions(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the nodal positions of the simulation mesh for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
position tensor with shape (M, max_simulation_mesh_vertices_per_body, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_nodal_velocities(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the vertex velocities for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
velocity tensor with shape (M, max_simulation_mesh_vertices_per_body, 3)

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_simulation_mesh_rest_points(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the simulation mesh rest points of the deformable bodies indicated by the indices.
rest point are the nodal positions with respect to the local prim transform, while the values returned by get_simulation_mesh_nodal_positions are the nodal positions with respect to the origin

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
deformable bodies simulation mesh rest points
with shape (M, self.max_simulation_mesh_vertices_per_body, 3).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_sleep_dampings(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the sleep damping for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the sleep damping tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_sleep_thresholds(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the sleep threshold for the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
the sleep threshold tensor with shape (M, )

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_solver_position_iteration_counts(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the solver’s positional iteration counts of the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (int, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
solver’s positional iteration counts with shape (M, ).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

get_vertex_velocity_dampings(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets the vertex velocity dampings of the deformable bodies indicated by the indices.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (float, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
deformable bodies vertex velocity dampings with shape (M, ).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor]]

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
usd:bool=True,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get the poses of the prims in the view with respect to the world’s frame
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Returns:
first index is positions in the world frame of the prims. shape is (M, 3).
second index is quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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
)→None Create a physics simulation view if not passed and creates a deformable body view in physX.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_physics_handle_valid()→bool
Returns:
True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.

Return type:
bool

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

post_reset()→None
Reset the prims to its default state
Example:

```
>>> prims.post_reset()
```

set_collision_mesh_indices(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the collision mesh element indices of the deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – element indices with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_collision_mesh_rest_points(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the collision mesh vertices rest positions of the deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – vertices rest positions values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

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

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame)
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
>>> # reposition all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs
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

set_self_collision_filter_distances(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the self collisions filter distance values for deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_self_collisions(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the self collisions values for deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_settling_thresholds(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the settling threshold values for deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_simulation_mesh_indices(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the simulation mesh element indices of the deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – element indices with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_simulation_mesh_kinematic_targets(
positions:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the kinematic targets of the simulation mesh for the deformable bodies indicated by the indices.
Parameters:

- positions (Union[np.ndarray, torch.Tensor]) – kinematic targets with the shape (M, max_simulation_mesh_vertices_per_body, 4).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_simulation_mesh_nodal_positions(
positions:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the nodal positions of the simulation mesh for the deformable bodies indicated by the indices.
Parameters:

- positions (Union[np.ndarray, torch.Tensor]) – nodal positions with the shape (M, max_simulation_mesh_vertices_per_body, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_simulation_mesh_nodal_velocities(
velocities:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the vertex velocities for the deformable bodies indicated by the indices.
Parameters:

- velocities (Union[np.ndarray, torch.Tensor]) – vertex velocities with the shape (M, max_simulation_mesh_vertices_per_body, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_simulation_mesh_rest_points(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the simulation mesh vertices rest positions of the deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – vertices rest positions values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_sleep_dampings(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the sleep dampings values for deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_sleep_thresholds(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets the sleep threshold values for deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_solver_position_iteration_counts(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets values of the solver position iteration counts to deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_vertex_velocity_dampings(
values:ndarray|Tensor|None ,
indices:ndarray|list|Tensor|None =None,
)→None Sets values of the vertex velocity damping values to deformable bodies indicated by the indices.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – solver position iteration counts values with the shape (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which deformable prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

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
)→None Set prim poses in the view with respect to the world’s frame
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prims. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all prims in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
```

propertycount:int
Returns: int: deformable counts.

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

propertymax_collision_mesh_elements_per_body:int
Returns: int: maximum number of collision mesh elements per deformable body.

propertymax_collision_mesh_vertices_per_body:int
Returns: int: maximum number of collision mesh vertices per deformable body.

propertymax_simulation_mesh_elements_per_body:int
Returns: int: maximum number of simulation mesh elements per deformable body.

propertymax_simulation_mesh_vertices_per_body:int
Returns: int: maximum number of simulation mesh vertices per deformable body.

propertyname:str
Returns: str: name given to the prims view when instantiating it.

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

classGeometryPrim(
prim_paths_expr:str,
name:str='geometry_prim_view',
positions:ndarray|Tensor|warp.array|None =None,
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
scales:ndarray|Tensor|warp.array|None =None,
visibilities:ndarray|Tensor|warp.array|None =None,
reset_xform_properties:bool=True,
collisions:ndarray|Tensor|warp.array|None =None,
track_contact_forces:bool=False,
prepare_contact_sensors:bool=False,
disable_stablization:bool=True,
contact_filter_prim_paths_expr:List[str]|None =[],
max_contact_count:int=0,
)Bases: XFormPrim
High level wrapper to deal with geom prims (one or many) as well as their attributes/properties.
This class wraps all matching geom prims found at the regex provided at the `prim_paths_expr` argument
Note
Each prim will have `xformOp:orient`, `xformOp:translate` and `xformOp:scale` only post-init, unless it is a non-root articulation link.
Warning
The geometry prim view object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Warning
Some methods require the prims to have the Physx Collision API. Instantiate the class with the `collision` parameter to a list of True values to apply the collision API.
Parameters:

- prim_paths_expr (str) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Microwave” will match /World/Env1/Microwave, /World/Env2/Microwave..etc. (a non regex prim path can also be used to encapsulate one XForm).

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “geometry_prim_view”.

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default positions in the world frame of the prim. shape is (N, 3). Defaults to None, which means left unchanged.

- translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default quaternion orientations in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (N, 4). Defaults to None, which means left unchanged.

- scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – local scales to be applied to the prim’s dimensions. shape is (N, 3). Defaults to None, which means left unchanged.

- visibilities (Optional[Union[np.ndarray, torch.Tensor, wp.array], optional) – set to false for an invisible prim in the stage while rendering. shape is (N,). Defaults to None.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- collisions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – Set to True if the geometry already have/ should have a collider (i.e not only a visual geometry). shape is (N,). Defaults to None.

- track_contact_forces (bool, Optional) – if enabled, the view will track the net contact forces on each geometry prim in the view. Note that the collision flag should be set to True to report contact forces. Defaults to False.

- prepare_contact_sensors (bool, Optional) – applies contact reporter API to the prim if it already does not have one. Defaults to False.

- disable_stablization (bool, optional) – disables the contact stabilization parameter in the physics context. Defaults to True.

- contact_filter_prim_paths_expr (Optional[List[str]], Optional) – a list of filter expressions which allows for tracking contact forces between the geometry prim and this subset through get_contact_force_matrix().

- max_contact_count (int, optional) – maximum number of contact data to report when detailed contact information is needed

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.cloner import GridCloner
>>> from isaacsim.core.prims import GeometryPrim
>>> from pxr import UsdGeom
>>>
>>> env_zero_path = "/World/envs/env_0"
>>> num_envs = 5
>>>
>>> # clone the environment (num_envs)
>>> cloner = GridCloner(spacing=1.5)
>>> cloner.define_base_env(env_zero_path)
>>> UsdGeom.Xform.Define(stage_utils.get_current_stage(), env_zero_path)
>>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform", "Xform")
>>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform/Cube", "Cube")
>>> env_pos = cloner.clone(
... source_prim_path=env_zero_path,
... prim_paths=cloner.generate_paths("/World/envs/env", num_envs),
... copy_from_source=True
... )
>>>
>>> # wrap the prims
>>> prims = GeometryPrim(
... prim_paths_expr="/World/envs/env.*/Xform",
... name="geometry_prim_view",
... collisions=[True] * num_envs
... )
>>> prims
<isaacsim.core.prims.geometry_prim.GeometryPrim object at 0x7f372bb21630>
```
apply_collision_apis(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Apply the collision API to prims in the view and update internal variables
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # apply the collision API for all prims
>>> prims.apply_collision_apis()
>>>
>>> # apply the collision API for the first, middle and last of the 5 envs
>>> prims.apply_collision_apis(indices=np.array([0, 2, 4]))
```

apply_physics_materials(
physics_materials:PhysicsMaterial |List[PhysicsMaterial ],
weaker_than_descendants:bool|List[bool]|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Used to apply physics material to prims in the view and optionally its descendants.
Parameters:

- physics_materials (Union[PhysicsMaterial , List[PhysicsMaterial ]]) – physics materials to be applied to prims in the view. Physics material can be used to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX. If a list is provided then its size has to be equal the view’s size or indices size. If one material is provided it will be applied to all prims in the view.

- weaker_than_descendants (Optional[Union[bool, List[bool]]], optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False. If a list of visual materials is provided then a list has to be provided with the same size for this arg as well.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Raises:

- Exception – length of physics materials != length of prims indexed

- Exception – length of physics materials != length of weaker descendants arg

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
>>>
>>> # apply the material to all prims
>>> prims.apply_physics_materials(material) # or [material] * num_envs
>>>
>>> # apply the collision API for the first, middle and last of the 5 envs
>>> prims.apply_physics_materials(material, indices=np.array([0, 2, 4]))
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
disable_collision(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Disables collision on prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # disable the collision API for all prims
>>> prims.disable_collision()
>>>
>>> # disable the collision API for the prims for the first, middle and last of the 5 envs
>>> prims.disable_collision(indices=np.array([0, 2, 4]))
```

enable_collision(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Enables collision on prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # enable the collision API for all prims
>>> prims.enable_collision()
>>>
>>> # enable the collision API for the prims for the first, middle and last of the 5 envs
>>> prims.enable_collision(indices=np.array([0, 2, 4]))
```

get_applied_physics_materials(
indices:ndarray|list|Tensor|warp.array|None =None,
)→List[PhysicsMaterial ]Get the applied physics material to prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
the current applied physics materials for prims in the view.

Return type:
List[PhysicsMaterial ]

Example:

```
>>> # get the applied material for all prims
>>> prims.get_applied_physics_materials()
[<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>]
>>>
>>> # get the applied material for the first, middle and last of the 5 envs
>>> prims.get_applied_physics_materials(indices=np.array([0, 2, 4]))
[<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>]
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

get_collision_approximations(
indices:ndarray|list|Tensor|warp.array|None =None,
)→List[str]Get collision approximation types for prims in the view.

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
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
approximations used for collision. size == M or size of the view.

Return type:
List[str]

Example:

```
>>> # get the collision approximation of all prims. Returned size is (5,).
>>> prims.get_collision_approximations()
['none', 'none', 'none', 'none', 'none']
>>>
>>> # get the collision approximation of the prims for the first, middle and last of the 5 envs
>>> prims.get_collision_approximations(indices=np.array([0, 2, 4]))
['none', 'none', 'none']
```

get_contact_force_data(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→Tuple[ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray]Get more detailed contact information between the prims in the view and the filter prims. Specifically, this method provides individual contact normals, contact points, contact separations as well as contact forces for each pair (the sum of which equals the forces that the get_contact_force_matrix method provides as the force aggregate of a pair) Given to the dynamic nature of collision between bodies, this method will provide buffers of contact data which are arranged sequentially for each pair. The starting index and the number of contact data points for each pair in this stream can be realized from pair_contacts_start_indices, and pair_contacts_count tensors. They both have a dimension of (self.num_shapes, self.num_filters) where filter_count is determined according to the filter_paths_expr parameter.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (M, self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self.count, self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (M, self._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_contact_offsets(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet contact offsets for prims in the view.
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
Contact offsets of the collision shapes. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the contact offsets of all prims. Returned shape is (5,).
>>> prims.get_contact_offsets()
[-inf -inf -inf -inf -inf]
>>>
>>> # get the contact offsets of the prims for the first, middle and last of the 5 envs
>>> prims.get_contact_offsets(indices=np.array([0, 2, 4]))
[-inf -inf -inf]
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

get_friction_data(
indices:ndarray|List|Tensor|warp.array|None =None,
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

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame)
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
first index is translations in the local frame of the prims. shape is (M, 3).
second index is quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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

get_min_torsional_patch_radii(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorGet minimum torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
minimum radius of the contact patch used to apply torsional friction. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor]

Example:

```
>>> # get the minimum torsional patch radius of all prims. Returned shape is (5,).
>>> prims.get_min_torsional_patch_radii()
[0. 0. 0. 0. 0.]
>>>
>>> # get the minimum torsional patch radius of the prims for the first, middle and last of the 5 envs
>>> prims.get_min_torsional_patch_radii(indices=np.array([0, 2, 4]))
[0. 0. 0.]
```

get_net_contact_forces(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (self.count, 3)
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (M,3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_rest_offsets(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet rest offsets for prims in the view.
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
Rest offsets of the collision shapes. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the rest offsets of all prims. Returned shape is (5,).
>>> prims.get_rest_offsets()
[-inf -inf -inf -inf -inf]
>>>
>>> # get the rest offsets of the prims for the first, middle and last of the 5 envs
>>> prims.get_rest_offsets(indices=np.array([0, 2, 4]))
[-inf -inf -inf]
```

get_torsional_patch_radii(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
radius of the contact patch used to apply torsional friction. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the torsional patch radius of all prims. Returned shape is (5,).
>>> prims.get_torsional_patch_radii()
[0. 0. 0. 0. 0.]
>>>
>>> # get the torsional patch radius of the prims for the first, middle and last of the 5 envs
>>> prims.get_torsional_patch_radii(indices=np.array([0, 2, 4]))
[0. 0. 0.]
```

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
usd:bool=True,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get the poses of the prims in the view with respect to the world’s frame
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Returns:
first index is positions in the world frame of the prims. shape is (M, 3).
second index is quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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
If the rigid prim view has been added to the world scene (e.g., `world.scene.add(prims)`), it will be automatically initialized when the world is reset (e.g., `world.reset()`).
Warning
This method needs to be called after each hard reset (e.g., Stop + Play on the timeline) before interacting with any other class method.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

Example:

```
>>> prims.initialize()
```

is_collision_enabled(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayQueries if collision is enabled on prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
True if collision is enabled. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # check if the collision is enabled for all prims. Returned size is (5,).
>>> prims.is_collision_enabled()
[ True True True True True]
>>>
>>> # check if the collision is enabled for the first, middle and last of the 5 envs
>>> prims.is_collision_enabled(indices=np.array([0, 2, 4]))
[ True True True]
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

post_reset()→None
Reset the prims to its default state
Example:

```
>>> prims.post_reset()
```

set_collision_approximations(
approximation_types:List[str],
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set collision approximation types for prims in the view.

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
Parameters:

- approximation_types (List[str]) – approximations used for collision. List size == M or the size of the view.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the collision approximations for all the prims to the specified values.
>>> prims.set_collision_approximations(["convexDecomposition"] * num_envs)
>>>
>>> # set the collision approximations for the first, middle and last of the 5 envs
>>> types = ["convexDecomposition", "convexHull", "meshSimplification"]
>>> prims.set_collision_approximations(types, indices=np.array([0, 2, 4]))
```

set_contact_offsets(
offsets:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set contact offsets for prims in the view.
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Parameters:

- offsets (Union[np.ndarray, torch.Tensor, wp.array]) – Contact offsets of the collision shapes. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent. Shape (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the contact offset for all the prims to the specified values.
>>> prims.set_contact_offsets(np.full(num_envs, 0.02))
>>>
>>> # set the contact offset for the first, middle and last of the 5 envs
>>> prims.set_contact_offsets(np.full(3, 0.02), indices=np.array([0, 2, 4]))
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

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame)
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
>>> # reposition all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs
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

set_min_torsional_patch_radii(
radii:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set minimum torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:

- radii (Union[np.ndarray, torch.Tensor, wp.array]) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float]. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the minimum torsional patch radius for all the prims to the specified values.
>>> prims.set_min_torsional_patch_radii(np.full(num_envs, 0.05))
>>>
>>> # set the minimum torsional patch radius for the first, middle and last of the 5 envs
>>> prims.set_min_torsional_patch_radii(np.full(3, 0.05), indices=np.array([0, 2, 4]))
```

set_rest_offsets(
offsets:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set rest offsets for prims in the view.
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:

- offsets (Union[np.ndarray, torch.Tensor, wp.array]) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset]. Default value is -inf, means default is picked by simulation. For rigid bodies its zero. Shape (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the rest offset for all the prims to the specified values.
>>> prims.set_rest_offsets(np.full(num_envs, 0.01))
>>>
>>> # set the rest offset for the first, middle and last of the 5 envs
>>> prims.set_rest_offsets(np.full(3, 0.01), indices=np.array([0, 2, 4]))
```

set_torsional_patch_radii(
radii:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:

- radii (Union[np.ndarray, torch.Tensor, wp.array]) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float]. shape is (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the torsional patch radius for all the prims to the specified values.
>>> prims.set_torsional_patch_radii(np.full(num_envs, 0.1))
>>>
>>> # set the torsional patch radius for the first, middle and last of the 5 envs
>>> prims.set_torsional_patch_radii(np.full(3, 0.1), indices=np.array([0, 2, 4]))
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
)→None Set prim poses in the view with respect to the world’s frame
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prims. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all prims in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
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

propertygeoms:List[pxr.UsdGeom.Gprim]
Returns:
USD geom objects encapsulated.

Return type:
List[UsdGeom.Gprim]

Example:

```
>>> prims.geoms
[UsdGeom.Gprim(Usd.Prim(</World/envs/env_0/Xform>)), UsdGeom.Gprim(Usd.Prim(</World/envs/env_1/Xform>)),
UsdGeom.Gprim(Usd.Prim(</World/envs/env_2/Xform>)), UsdGeom.Gprim(Usd.Prim(</World/envs/env_3/Xform>)),
UsdGeom.Gprim(Usd.Prim(</World/envs/env_4/Xform>))]
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

propertyname:str
Returns: str: name given to the prims view when instantiating it.

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

classParticleSystem(
prim_paths_expr:str,
name:str='particle_system_view',
particle_systems_enabled:ndarray|Tensor|None =None,
simulation_owners:Sequence[str]|None =None,
contact_offsets:ndarray|Tensor|None =None,
rest_offsets:ndarray|Tensor|None =None,
particle_contact_offsets:ndarray|Tensor|None =None,
solid_rest_offsets:ndarray|Tensor|None =None,
fluid_rest_offsets:ndarray|Tensor|None =None,
enable_ccds:ndarray|Tensor|None =None,
solver_position_iteration_counts:ndarray|Tensor|None =None,
max_depenetration_velocities:ndarray|Tensor|None =None,
winds:ndarray|Tensor|None =None,
max_neighborhoods:int|None =None,
max_velocities:ndarray|Tensor|None =None,
global_self_collisions_enabled:ndarray|Tensor|None =None,
)Bases: `object`
Provides high level functions to deal with particle systems (1 or more particle systems) as well as its attributes/ properties. This object wraps all matching particle systems found at the regex provided at the prim_paths_expr. Note: not all the attributes of the PhysxSchema.PhysxParticleSystem is currently controlled with this view class Tensor API support will be added in the future to extend the functionality of this class to applications beyond cloth.
apply_particle_materials(
particle_materials:ParticleMaterial |List[ParticleMaterial ],
indices:ndarray|list|Tensor|None =None,
)→None Used to apply particle material to prims in the view.
Parameters:

- particle_materials (Union[ParticleMaterial , List[ParticleMaterial ]]) – particle materials to be applied to prims in the view. Note: if a physics material is not defined, the defaults will be used from PhysX. If a list is provided then its size has to be equal the view’s size or indices size. If one material is provided it will be applied to all prims in the view.

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Raises:
Exception – length of physics materials != length of prims indexed

get_applied_particle_materials(
indices:ndarray|list|Tensor|None =None,
)→List[ParticleMaterial ]Gets the applied particle material to prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
the current applied particle materials for prims in the view.

Return type:
List[ParticleMaterial ]

get_contact_offsets(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
The contact offset used for collisions with non-particle objects for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_enable_ccds(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
Whether continuous collision detection for particles is enabled or disabled for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_fluid_rest_offsets(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorReturns:
The rest offset used for fluid-fluid particle interactions. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

get_global_self_collisions_enabled(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
Whether self collisions to follow particle-object-specific settings
is enabled or disabled. for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_max_depenetration_velocities(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
The maximum velocity permitted to be introduced by the solver to
depenetrate intersecting particles for particle systems for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_max_neighborhoods(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
The particle neighborhood size for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_max_velocities(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
The maximum particle velocities for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_particle_contact_offsets(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorReturns:
The contact offset used for interactions between particles in the view concatenated. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

get_particle_systems_enabled(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
Whether particle system is enabled or not for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_rest_offsets(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
The rest offset used for collisions with non-particle objects for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_simulation_owners(
indices:ndarray|list|Tensor|None =None,
)→Sequence[str]Returns:
The physics scene prim path attached to particle system. shape is (M, ).

Return type:
Sequence[str]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_solid_rest_offsets(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorReturns:
The rest offset used for solid-solid or solid-fluid particle interactions. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

get_solver_position_iteration_counts(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorReturns:
The number of solver iterations for positions for each particle system. shape is (M, ).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

get_winds(
indices:ndarray|list|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorReturns:
The winds applied to the current particle system. shape is (M, 3).

Return type:
Union[np.ndarray, torch.Tensor]

Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

initialize(
physics_sim_view:omni.physics.tensors.SimulationView=None,
)→None Create a physics simulation view if not passed and creates a Particle System View.
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

set_contact_offsets(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the contact offset used for collisions with non-particle objects such as rigid or deformable bodies for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_enable_ccds(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Enable continuous collision detection for particles for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_fluid_rest_offsets(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the rest offset used for fluid-fluid particle interactions.
Note: Must be smaller than particle contact offset.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – fluid rest offset to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_global_self_collisions_enabled(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Enable self collisions to follow particle-object-specific settings for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_max_depenetration_velocities(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the maximum velocity permitted to be introduced by the solver to depenetrate intersecting particles for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_max_neighborhoods(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the particle neighborhood size for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_max_velocities(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the maximum particle velocity for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_particle_contact_offsets(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the contact offset used for interactions between particles.
Note: Must be larger than solid and fluid rest offsets.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – The contact offset.

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_particle_systems_enabled(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set enabling of the particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_rest_offsets(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the rest offset used for collisions with non-particle objects such as rigid or deformable bodies for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_simulation_owners(
values:Sequence[str],
indices:ndarray|List|Tensor|None =None,
)→None Set the PhysicsScene that simulates particle systems.
Parameters:

- values (Sequence[str]) – PhysicsScene list to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_solid_rest_offsets(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the rest offset used for solid-solid or solid-fluid particle interactions.
Note: Must be smaller than particle contact offset.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – solid rest offset to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_solver_position_iteration_counts(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the number of solver iterations for position for particle systems.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – maximum particle velocity tensor to set particle systems to. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_winds(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Set the winds velocities applied to the current particle system.
Parameters:

- values (Optional[Union[np.ndarray, torch.Tensor]]) – The wind applied to the current particle system. shape is (M, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

propertycount:int
Returns: int: number of rigid shapes for the prims in the view.

propertyname:str
Returns: str: name given to the view when instantiating it.

classRigidPrim(
prim_paths_expr:str|List[str],
name:str='rigid_prim_view',
positions:ndarray|Tensor|warp.array|None =None,
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
scales:ndarray|Tensor|warp.array|None =None,
visibilities:ndarray|Tensor|warp.array|None =None,
reset_xform_properties:bool=True,
masses:ndarray|Tensor|warp.array|None =None,
densities:ndarray|Tensor|warp.array|None =None,
linear_velocities:ndarray|Tensor|warp.array|None =None,
angular_velocities:ndarray|Tensor|warp.array|None =None,
track_contact_forces:bool=False,
prepare_contact_sensors:bool=True,
disable_stablization:bool=True,
contact_filter_prim_paths_expr:List[str]|None =[],
max_contact_count:int=0,
)Bases: XFormPrim
Provides high level functions to deal with prims (one or many) that have Rigid Body API applied to them as well as their attributes/properties.
This class wraps all matching rigid prims found at the regex provided at the `prim_paths_expr` argument
Note
Each prim will have `xformOp:orient`, `xformOp:translate` and `xformOp:scale` only post-init, unless it is a non-root articulation link.
If the prims do not already have the Rigid Body API applied to them before init, it will apply it.
Warning
The rigid prim view object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Parameters:

- prim_paths_expr (Union[str, List[str]]) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Cube” will match /World/Env1/Cube, /World/Env2/Cube..etc. (a non regex prim path can also be used to encapsulate one rigid prim). Additionally a list of regex can be provided. example [“/World/Env[1-5]/Cube”, “/World/Env[10-19]/Cube”].

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “rigid_prim_view”.

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default positions in the world frame of the prims. shape is (N, 3). Defaults to None, which means left unchanged.

- translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default quaternion orientations in the world/ local frame of the prims (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (N, 4). Defaults to None, which means left unchanged.

- scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – local scales to be applied to the prim’s dimensions in the view. shape is (N, 3). Defaults to None, which means left unchanged.

- visibilities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – set to false for an invisible prim in the stage while rendering. shape is (N,). Defaults to None.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- masses (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – mass in kg specified for each prim in the view. shape is (N,). Defaults to None.

- densities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – density in kg/m^3 specified for each prim in the view. shape is (N,). Defaults to None.

- linear_velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default linear velocity of each prim in the view (to be applied in the first frame and on resets). Shape is (N, 3). Defaults to None.

- angular_velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default angular velocity of each prim in the view (to be applied in the first frame and on resets). Shape is (N, 3). Defaults to None.

- track_contact_forces (bool, Optional) – if enabled, the view will track the net contact forces on each rigid prim in the view

- prepare_contact_sensors (bool, Optional) – if rigid prims in the view are not cloned from a prim in a prepared state, (although slow for large number of prims) this ensures that appropriate physics settings are applied on all the prim in the view.

- disable_stablization (bool, optional) – disables the contact stabilization parameter in the physics context

- contact_filter_prim_paths_expr (Optional[List[str]], Optional) – a list of filter expressions which allows for tracking contact forces between prims and this subset through get_contact_force_matrix().

- max_contact_count (int, optional) – maximum number of contact data to report when detailed contact information is needed

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.cloner import GridCloner
>>> from isaacsim.core.prims import RigidPrim
>>> from pxr import UsdGeom
>>>
>>> env_zero_path = "/World/envs/env_0"
>>> num_envs = 5
>>>
>>> # clone the environment (num_envs)
>>> cloner = GridCloner(spacing=1.5)
>>> cloner.define_base_env(env_zero_path)
>>> UsdGeom.Xform.Define(stage_utils.get_current_stage(), env_zero_path)
>>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform", "Xform")
>>> stage_utils.get_current_stage().DefinePrim(f"{env_zero_path}/Xform/Cube", "Cube")
>>> env_pos = cloner.clone(
... source_prim_path=env_zero_path,
... prim_paths=cloner.generate_paths("/World/envs/env", num_envs),
... copy_from_source=True
... )
>>>
>>> # wrap the prims
>>> prims = RigidPrim(prim_paths_expr="/World/envs/env.*/Xform", name="rigid_prim_view")
>>> prims
<isaacsim.core.prims.rigid_prim.RigidPrim object at 0x7f9a23b8bb80>
```
apply_forces(
forces:ndarray|Tensor|warp.array|None ,
indices:ndarray|list|Tensor|warp.array|None =None,
is_global:bool=True,
)→None Applies forces to prims in the view.
Parameters:

- forces (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – forces to be applied to the prims.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- is_global (bool, optional) – True if forces are in the global frame. Otherwise False. Defaults to True.

Example:

```
>>> # apply an external force to all the rigid bodies to the indicated values.
>>> # Since there are 5 envs, the inertias are repeated 5 times
>>> forces = np.tile(np.array([2e5, 1e5, 0.0]), (num_envs, 1))
>>> prims.apply_forces(forces)
>>>
>>> # apply an external force to the rigid bodies for the first, middle and last of the 5 envs
>>> forces = np.tile(np.array([2e5, 1e5, 0.0]), (3, 1))
>>> prims.apply_forces(forces, indices=np.array([0, 2, 4]))
```

apply_forces_and_torques_at_pos(
forces:ndarray|Tensor|warp.array|None =None,
torques:ndarray|Tensor|warp.array|None =None,
positions:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
is_global:bool=True,
)→None Applies forces and torques to prims in the view. The forces and/or torques can be in local or global coordinates. The forces can applied at a location given by positions variable.
Parameters:

- forces (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – forces to be applied to the prims. If not specified, no force will be applied. Defaults to None (i.e: no forces will be applied).

- torques (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – torques to be applied to the prims. If not specified, no torque will be applied. Defaults to None (i.e: no torques will be applied).

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – position of the forces with respect to the body frame. If not specified, the forces are applied at the origin of the body frame. Defaults to None (i.e: applied forces will be at the origin of the body frame).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- is_global (bool, optional) – True if forces, torques, and positions are in the global frame. False if forces, torques, and positions are in the local frame. Defaults to True.

Example:

```
>>> # apply an external force and torque to all the rigid bodies to the indicated values.
>>> # Since there are 5 envs, the inertias are repeated 5 times
>>> forces = np.tile(np.array([2e5, 1e5, 0.0]), (num_envs, 1))
>>> torques = np.tile(np.array([2e5, 1e5, 0.0]), (num_envs, 1))
>>> prims.apply_forces_and_torques_at_pos(forces, torques)
>>>
>>> # apply an external force and torque to the rigid bodies for the first, middle and last of the 5 envs
>>> forces = np.tile(np.array([2e5, 1e5, 0.0]), (3, 1))
>>> torques = np.tile(np.array([2e5, 1e5, 0.0]), (3, 1))
>>> prims.apply_forces_and_torques_at_pos(forces, torques, indices=np.array([0, 2, 4]))
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
disable_gravities(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Disable gravity on rigid bodies (enabled by default).
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # disable the gravity for all rigid bodies
>>> prims.disable_gravities()
>>>
>>> # disable the rigid body gravity for the first, middle and last of the 5 envs
>>> prims.disable_gravities(indices=np.array([0, 2, 4]))
```

disable_rigid_body_physics(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Disable rigid body physics (enabled by default)
When disabled, the objects will not be moved by external forces such as gravity and collisions
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # enable the rigid body dynamics for all rigid bodies
>>> prims.disable_rigid_body_physics()
>>>
>>> # enable the rigid body dynamics for the first, middle and last of the 5 envs
>>> prims.disable_rigid_body_physics(indices=np.array([0, 2, 4]))
```

enable_gravities(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Enable gravity on rigid bodies (enabled by default).
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # enable the gravity for all rigid bodies
>>> prims.enable_gravities()
>>>
>>> # enable the rigid body gravity for the first, middle and last of the 5 envs
>>> prims.enable_gravities(indices=np.array([0, 2, 4]))
```

enable_rigid_body_physics(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Enable rigid body physics (enabled by default)
When enabled, the objects will be moved by external forces such as gravity and collisions
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # enable the rigid body dynamics for all rigid bodies
>>> prims.enable_rigid_body_physics()
>>>
>>> # enable the rigid body dynamics for the first, middle and last of the 5 envs
>>> prims.enable_rigid_body_physics(indices=np.array([0, 2, 4]))
```

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
>>> # get all rigid prim angular velocities. Returned shape is (5, 3) for the example: 5 envs, angular (3)
>>> prims.get_angular_velocities()
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
>>>
>>> # get only the rigid prim angular velocities for the first, middle and last of the 5 envs
>>> # Returned shape is (5, 3) for the example: 3 envs selected, angular (3)
>>> prims.get_angular_velocities(indices=np.array([0, 2, 4]))
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
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

get_coms(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body center of mass (COM) of bodies in the view.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body center of mass positions and orientations of prims in the view. position shape is (M, 1, 3), orientation shape is (M, 1, 4).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid body center of mass.
>>> # Returned shape is (5, 1, 3) for positions and (5, 1, 4) for orientations for the example: 5 envs
>>> positions, orientations = prims.get_coms()
>>> positions
[[[0. 0. 0.]]
[[0. 0. 0.]]
[[0. 0. 0.]]
[[0. 0. 0.]]
[[0. 0. 0.]]]
>>> orientations
[[[1. 0. 0. 0.]]
[[1. 0. 0. 0.]]
[[1. 0. 0. 0.]]
[[1. 0. 0. 0.]]
[[1. 0. 0. 0.]]]
>>>
>>> # get rigid body center of mass for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 1, 3) for positions and (3, 1, 4) for orientations
>>> positions, orientations = prims.get_coms(indices=np.array([0, 2, 4]))
>>> positions
[[[0. 0. 0.]]
[[0. 0. 0.]]
[[0. 0. 0.]]]
>>> orientations
[[[1. 0. 0. 0.]]
[[1. 0. 0. 0.]]
[[1. 0. 0. 0.]]]
```

get_contact_force_data(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→Tuple[ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray]Get more detailed contact information between the prims in the view and the filter prims.
Specifically, this method provides individual contact normals, contact points, contact separations as well as contact forces for each pair (the sum of which equals the forces that the `get_contact_force_matrix` method provides as the force aggregate of a pair)
Given to the dynamic nature of collision between bodies, this method will provide buffers of contact data which are arranged sequentially for each pair. The starting index and the number of contact data points for each pair in this stream can be realized from pair_contacts_start_indices, and pair_contacts_count tensors. They both have a dimension of `(num_shapes, _contact_view.num_filters)` where `_contact_view.num_filters` is determined according to the `contact_filter_prim_paths_expr` parameter
Note
This method requires that the contact forces of the prims in the view be tracked by defining the `contact_filter_prim_paths_expr` argument to a list of the prim paths from which to generate the information and the `max_contact_count` argument be greater than 0 during view creation
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (M, self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

Example:

```
>>> # for the example, the cubes are on top of each other. The view was instantiated with the following
>>> # extra parameters: contact_filter_prim_paths_expr=["/World/envs/env_2/Xform"], max_contact_count=10
>>> # This indicates that only contacts with the middle cube will be reported
>>> data = prims.get_contact_force_data()
>>> data[0] # normal forces
[[-156.449 ]
[ -81.736336]
[-169.73076 ]
[ -82.397804]
[ 110.11985 ]
[ 59.646057]
[ 98.660545]
[ 58.43006 ]
[ 0. ]
[ 0. ]]
>>> data[1] # points
[[-0.50145745 0.49872556 0.7056795 ]
[-0.50184476 -0.5010655 0.7057198 ]
[ 0.49793154 -0.50147027 0.70576656]
[ 0.4983363 0.49833822 0.70572615]
[ 0.49818155 -0.5016888 1.7058725 ]
[ 0.49856627 0.4913648 1.7058672 ]
[-0.49732465 0.4915302 1.705814 ]
[-0.49748957 -0.501303 1.7058194 ]
[ 0. 0. 0. ]
[ 0. 0. 0. ]]
>>> data[2] # normals
[[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 1.6479074e-05 -1.6995813e-05 1.0000000e+00]
[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]
[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
>>> data[3] # distances
[[ 6.3175990e-05]
[ 5.8271162e-06]
[-5.7399273e-05]
[-1.0989098e-08]
[ 1.6338757e-04]
[ 1.4112510e-04]
[ 7.1585178e-05]
[ 9.3835908e-05]
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
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayReturn the contact forces between the prims in the view and the filter prims
E.g., a matrix of dimension `(self.count, _contact_view.num_filters, 3)` where `_contact_view.num_filters` is determined according to the `contact_filter_prim_paths_expr` parameter
Note
This method requires that the contact forces of the prims in the view be tracked by defining the `contact_filter_prim_paths_expr` argument to a list of the prim paths from which to generate the information and the `max_contact_count` argument be greater than 0 during view creation
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (M, self._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # for the example, the cubes are on top of each other. The view was instantiated with the following
>>> # extra parameters: contact_filter_prim_paths_expr=["/World/envs/env_2/Xform"], max_contact_count=10
>>> # This indicates that only contacts with the middle cube will be reported
>>> prims.get_contact_force_matrix()
[[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
[[-7.8665102e-03 8.3034458e-03 -4.9063504e+02]]
[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]
[[ 5.2445102e-03 -5.5358098e-03 3.2710065e+02]]
[[ 0.0000000e+00 0.0000000e+00 0.0000000e+00]]]
```

get_current_dynamic_state()→DynamicsViewState
Get the current rigid body states (position, orientation and linear and angular velocities)
Returns:
the dynamic state of the rigid bodies

Return type:
DynamicState

Example:

```
>>> # for the example the rigid bodies are in free fall
>>> state = prims.get_default_state()
<isaacsim.core.utils.types.DynamicsViewState object at 0x7f182bd72590>
>>> state
>>> state.positions
[[ 1.5 -0.75 -207.76808]
[ 1.5 0.75 -207.76808]
[ 0. -0.75 -207.76808]
[ 0. 0.75 -207.76808]
[ -1.5 -0.75 -207.76808]]
>>> state.orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>> state.linear_velocities
[[ 0. 0. -63.765312]
[ 0. 0. -63.765312]
[ 0. 0. -63.765312]
[ 0. 0. -63.765312]
[ 0. 0. -63.765312]]
>>> state.angular_velocities
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
```

get_default_state()→DynamicsViewState
Get the default state (position, orientation and linear and angular velocities) of prims in the view, that will be used after each reset.
Returns:
returns the default state of the prims that is used after each reset.

Return type:
DynamicsViewState

Example:

```
>>> state = prims.get_default_state()
<isaacsim.core.utils.types.DynamicsViewState object at 0x7f184e555480>
>>> state
>>> state.positions
[[ 1.4999989e+00 -7.4999851e-01 -1.5118626e-07]
[ 1.4999989e+00 7.5000149e-01 -2.5988294e-07]
[-1.0017333e-06 -7.4999845e-01 7.6070329e-08]
[-9.5906785e-07 7.5000149e-01 1.0593490e-07]
[-1.5000011e+00 -7.4999851e-01 1.9655154e-07]]
>>> state.orientations
[[ 9.9999994e-01 -8.8168377e-07 -4.1946004e-07 -1.5067183e-08]
[ 9.9999994e-01 -8.8691013e-07 -4.2665880e-07 -2.7188951e-09]
[ 1.0000000e+00 -9.5171310e-07 -2.2615541e-07 5.5922797e-08]
[ 1.0000000e+00 -8.9923367e-07 -1.4408238e-07 1.3476099e-08]
[ 1.0000000e+00 -7.9806580e-07 -1.3064776e-07 5.3154917e-08]]
>>> state.linear_velocities
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
>>> state.angular_velocities
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
```

get_densities(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet densities of prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

Returns:
densities of prims in the view in kg/m^3. shape (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid body densities. Returned shape is (5,) for the example: 5 envs
>>> prims.get_densities()
[0. 0. 0. 0. 0.]
>>>
>>> # get rigid body densities for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_densities(indices=np.array([0, 2, 4]))
[0. 0. 0.]
```

get_friction_data(
indices:ndarray|List|Tensor|warp.array|None =None,
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

get_inertias(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body inertias of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body inertias of prims in the view. Shape is (M, 9).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid body inertias. Returned shape is (5, 9) for the example: 5 envs
>>> prims.get_inertias()
[[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]
[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]
[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]
[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]
[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]]
>>>
>>> # get rigid body inertias for the first, middle and last of the 5 envs. Returned shape is (3, 9)
>>> prims.get_inertias(indices=np.array([0, 2, 4]))
[[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]
[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]
[166.66667 0. 0. 0. 166.66667 0. 0. 0. 166.66667]]
```

get_inv_inertias(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body inverse inertias of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body inverse inertias of prims in the view. Shape is (M, 9).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid body inverse inertias. Returned shape is (5, 9) for the example: 5 envs
>>> prims.get_inv_inertias()
[[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]
[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]
[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]
[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]
[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]]
>>>
>>> # get rigid body inverse inertias for the first, middle and last of the 5 envs. Returned shape is (3, 9)
>>> prims.get_inv_inertias(indices=np.array([0, 2, 4]))
[[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]
[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]
[0.006 0. 0. 0. 0.006 0. 0. 0. 0.006]]
```

get_inv_masses(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body inverse masses of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
rigid body inverse masses of prims in the view. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid body inverse masses. Returned shape is (5, 1) for the example: 5 envs
>>> prims.get_inv_masses()
[[0.001]
[0.001]
[0.001]
[0.001]
[0.001]]
>>>
>>> # get rigid body inverse masses for the first, middle and last of the 5 envs. Returned shape is (3, 1)
>>> prims.get_inv_masses(indices=np.array([0, 2, 4]))
[[0.001]
[0.001]
[0.001]]
```

get_linear_velocities(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
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
>>> # get all rigid prim linear velocities. Returned shape is (5, 3) for the example: 5 envs, linear (3)
>>> prims.get_linear_velocities()
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
>>>
>>> # get only the rigid prim linear velocities for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 3) for the example: 3 envs selected, linear (3)
>>> prims.get_linear_velocities(indices=np.array([0, 2, 4]))
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]
```

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame).
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

Returns:
first index is positions in the local frame of the prims. shape is (M, 3). second index is quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all rigid prim poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[-1.0728836e-06 1.4901161e-06 -1.5118626e-07]
[-1.0728836e-06 1.4901161e-06 -2.5988294e-07]
[-1.0017333e-06 1.5497208e-06 7.6070329e-08]
[-9.5906785e-07 1.4901161e-06 1.0593490e-07]
[-1.0728836e-06 1.4901161e-06 1.9655154e-07]]
>>> orientations
[[ 1.0000000e+00 -8.8174920e-07 -4.1949116e-07 -1.5068302e-08]
[ 1.0000000e+00 -8.8696777e-07 -4.2668654e-07 -2.7190719e-09]
[ 1.0000000e+00 -9.5164734e-07 -2.2613979e-07 5.5918935e-08]
[ 1.0000000e+00 -8.9923157e-07 -1.4408204e-07 1.3476067e-08]
[ 1.0000000e+00 -7.9806864e-07 -1.3064822e-07 5.3155105e-08]]
>>>
>>> # get only the rigid prim poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[-1.0728836e-06 1.4901161e-06 -1.5118626e-07]
[-1.0017333e-06 1.5497208e-06 7.6070329e-08]
[-1.0728836e-06 1.4901161e-06 1.9655154e-07]]
>>> orientations
[[ 1.0000000e+00 -8.8174920e-07 -4.1949116e-07 -1.5068302e-08]
[ 1.0000000e+00 -9.5164734e-07 -2.2613979e-07 5.5918935e-08]
[ 1.0000000e+00 -7.9806864e-07 -1.3064822e-07 5.3155105e-08]]
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

get_masses(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet rigid body masses of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
masses of in kg of prims in the view. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid body masses. Returned shape is (5,) for the example: 5 envs
>>> prims.get_masses()
[999.99994 999.99994 999.99994 999.99994 999.99994]
>>>
>>> # get rigid body masses for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_masses(indices=np.array([0, 2, 4]))
[999.99994 999.99994 999.99994]
```

get_net_contact_forces(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayReturn the net contact forces on prims
Note
This method requires that the contact forces of the prims in the view be tracked by defining the `track_contact_forces` argument to True (default to False) during view creation
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (M,3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the net contact force on all rigid bodies. Returned shape is (5, 3).
>>> # For the example the view was instantiated with the extra parameter: track_contact_forces=True
>>> prims.get_net_contact_forces()
[[2.1967362e-05 0.0000000e+00 1.6349771e+02]
[2.1967124e-05 0.0000000e+00 1.6349591e+02]
[2.1967891e-05 0.0000000e+00 1.6350165e+02]
[2.1967257e-05 0.0000000e+00 1.6349693e+02]
[2.1966895e-05 0.0000000e+00 1.6349425e+02]]
>>>
>>> # get the net contact force on the rigid bodies for the first, middle and last of the 5 envs
>>> prims.get_net_contact_forces(indices=np.array([0, 2, 4]))
[[2.1967362e-05 0.0000000e+00 1.6349771e+02]
[2.1967891e-05 0.0000000e+00 1.6350165e+02]
[2.1966895e-05 0.0000000e+00 1.6349425e+02]]
```

get_sleep_thresholds(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet sleep thresholds of prims in the view.
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

Returns:
Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf). Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2. shape (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all sleep threshold. Returned shape is (5,) for the example: 5 envs
>>> prims.get_sleep_thresholds()
[5.e-05 5.e-05 5.e-05 5.e-05 5.e-05]
>>>
>>> # get sleep threshold for the first, middle and last of the 5 envs. Returned shape is (3,)
>>> prims.get_sleep_thresholds(indices=np.array([0, 2, 4]))
[5.e-05 5.e-05 5.e-05]
```

get_velocities(
indices:ndarray|list|Tensor|warp.array|None =None,
clone:bool=True,
)→ndarray|Tensor|warp.indexedarrayGet the linear and angular velocities of prims in the view.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view)

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
linear and angular velocities of the prims in the view concatenated. shape is (M, 6).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get all rigid prim velocities. Returned shape is (5, 6) for the example: 5 envs, linear (3) and angular (3)
>>> prims.get_velocities()
[[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]]
>>>
>>> # get only the rigid prim velocities for the first, middle and last of the 5 envs.
>>> # Returned shape is (3, 6) for the example: 3 envs selected, linear (3) and angular (3)
>>> prims.get_velocities(indices=np.array([0, 2, 4]))
[[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0.]]
```

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
first index is positions in the world frame of the prims. shape is (M, 3). second index is quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all rigid prim poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.4999989e+00 -7.4999851e-01 -1.5118626e-07]
[ 1.4999989e+00 7.5000149e-01 -2.5988294e-07]
[-1.0017333e-06 -7.4999845e-01 7.6070329e-08]
[-9.5906785e-07 7.5000149e-01 1.0593490e-07]
[-1.5000011e+00 -7.4999851e-01 1.9655154e-07]]
>>> orientations
[[ 9.9999994e-01 -8.8168377e-07 -4.1946004e-07 -1.5067183e-08]
[ 9.9999994e-01 -8.8691013e-07 -4.2665880e-07 -2.7188951e-09]
[ 1.0000000e+00 -9.5171310e-07 -2.2615541e-07 5.5922797e-08]
[ 1.0000000e+00 -8.9923367e-07 -1.4408238e-07 1.3476099e-08]
[ 1.0000000e+00 -7.9806580e-07 -1.3064776e-07 5.3154917e-08]]
>>>
>>> # get only the rigid prim poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.4999989e+00 -7.4999851e-01 -1.5118626e-07]
[-1.0017333e-06 -7.4999845e-01 7.6070329e-08]
[-1.5000011e+00 -7.4999851e-01 1.9655154e-07]]
>>> orientations
[[ 9.9999994e-01 -8.8168377e-07 -4.1946004e-07 -1.5067183e-08]
[ 1.0000000e+00 -9.5171310e-07 -2.2615541e-07 5.5922797e-08]
[ 1.0000000e+00 -7.9806580e-07 -1.3064776e-07 5.3154917e-08]]
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

post_reset()→None
Reset the prims to its default state
Example:

```
>>> prims.post_reset()
```

set_angular_velocities(
velocities:ndarray|Tensor|warp.array|None ,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the angular velocities of the prims in the view
The method does this through the physx API only. It has to be called after initialization. Note: This method is not supported for the gpu pipeline. `set_velocities` method should be used instead.
Warning
This method will immediately set the rigid prim state
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – angular velocities to set the rigid prims to. shape is (M, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the rigid prim kinematic state:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`)
Example:

```
>>> # set each rigid prim linear velocity to (5.0, 5.0, 5.0)
>>> velocities = np.full((num_envs, 3), fill_value=5.0)
>>> prims.set_angular_velocities(velocities)
>>>
>>> # set only the rigid prim linear velocities for the first, middle and last of the 5 envs
>>> velocities = np.full((3, 3), fill_value=5.0)
>>> prims.set_angular_velocities(velocities, indices=np.array([0, 2, 4]))
```

set_coms(
positions:ndarray|Tensor|warp.array=None,
orientations:ndarray|Tensor|warp.array=None,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set body center of mass (COM) positions and orientations for bodies in the view.
Parameters:

- positions (Union[np.ndarray, torch.Tensor, wp.array]) – body center of mass positions for bodies in the view. shape (M, 1, 3).

- orientations (Union[np.ndarray, torch.Tensor, wp.array]) – body center of mass orientations for bodies in the view. shape (M, 1, 4).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the center of mass for all the rigid bodies to the specified values.
>>> # Since there are 5 envs, the inertias are repeated 5 times
>>> positions = np.tile(np.array([0.01, 0.02, 0.03]), (num_envs, 1, 1))
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1, 1))
>>> prims.set_coms(positions, orientations)
>>>
>>> # set the rigid bodies center of mass for the first, middle and last of the 5 envs
>>> positions = np.tile(np.array([0.01, 0.02, 0.03]), (3, 1, 1))
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1, 1))
>>> prims.set_coms(positions, orientations, indices=np.array([0, 2, 4]))
```

set_default_state(
positions:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
linear_velocities:ndarray|Tensor|warp.array|None =None,
angular_velocities:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the default state (position, orientation and linear and angular velocities) of prims in the view, that will be used after each reset.
Note
The default states will be set during post-reset (e.g., calling `.post_reset()` or `world.reset()` methods)
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default positions in the world frame of the prim. shape is (M, 3).

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

- linear_velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default linear velocities of each prim in the view (to be applied in the first frame and on resets). Shape is (M, 3). Defaults to None.

- angular_velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default angular velocities of each prim in the view (to be applied in the first frame and on resets). Shape is (M, 3). Defaults to None.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # configure default states for all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:, 0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> linear_velocities = np.zeros((num_envs, 3))
>>> angular_velocities = np.zeros((num_envs, 3))
>>> prims.set_default_state(
... positions=positions,
... orientations=orientations,
... linear_velocities=linear_velocities,
... angular_velocities=angular_velocities
... )
>>>
>>> # set default states during post-reset
>>> prims.post_reset()
```

set_densities(
densities:ndarray|Tensor|warp.array|None ,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set densities of prims in the view.
Parameters:

- densities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – density in kg/m^3 specified for each prim in the view. shape is (M,). Defaults to None.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set all rigid body densities to the specified values
>>> prims.set_densities(np.full(num_envs, 0.9))
>>>
>>> # set rigid body densities for the first, middle and last of the 5 envs
>>> prims.set_densities(np.full(3, 0.9), indices=np.array([0, 2, 4]))
```

set_inertias(
values:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set rigid body inertias for prims in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor, wp.array]) – body inertias for prims in the view. shape (M, 1, 9).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the rigid body inertias for all the rigid bodies to the specified values.
>>> # Since there are 5 envs, the inertias are repeated 5 times
>>> inertias = np.tile(np.array([0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]), (num_envs, 1))
>>> prims.set_inertias(inertias)
>>>
>>> # set the rigid body inertias for the first, middle and last of the 5 envs
>>> inertias = np.tile(np.array([0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]), (3, 1))
>>> prims.set_inertias(inertias, indices=np.array([0, 2, 4]))
```

set_linear_velocities(
velocities:ndarray|Tensor|warp.array|None ,
indices:ndarray|list|Tensor|warp.array|None =None,
)Set the linear velocities of the prims in the view
The method does this through the PhysX API only. It has to be called after initialization. Note: This method is not supported for the gpu pipeline. `set_velocities` method should be used instead.
Warning
This method will immediately set the rigid prim state
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – linear velocities to set the rigid prims to. shape is (M, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the rigid prim kinematic state:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`)
Example:

```
>>> # set each rigid prim linear velocity to (1.0, 1.0, 1.0)
>>> velocities = np.ones((num_envs, 3))
>>> prims.set_linear_velocities(velocities)
>>>
>>> # set only the rigid prim linear velocities for the first, middle and last of the 5 envs
>>> velocities = np.ones((3, 3))
>>> prims.set_linear_velocities(velocities, indices=np.array([0, 2, 4]))
```

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame).
Parameters:

- translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – translations in the local frame of the prims (with respect to its parent prim). shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # reposition all rigid prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the rigid prims for the first, middle and last of the 5 envs
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

set_masses(
masses:ndarray|Tensor|warp.array,
indices:ndarray|List|Tensor|warp.array|None =None,
)→None Set body masses for prims in the view.
Parameters:

- masses (Union[np.ndarray, torch.Tensor, wp.array]) – body masses for prims in kg. shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the rigid body masses for all the rigid bodies to the indicated values.
>>> prims.set_masses(np.full(num_envs, 10.0))
>>>
>>> # set the rigid body masses for the first, middle and last of the 5 envs
>>> prims.set_masses(np.full(3, 10.0), indices=np.array([0, 2, 4]))
```

set_sleep_thresholds(
thresholds:ndarray|Tensor|warp.array|None ,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set sleep thresholds of prims in the view.
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:

- thresholds (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2. shape (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set all rigid body densities to the specified values
>>> prims.set_sleep_thresholds(np.full(num_envs, 1e-5))
>>>
>>> # set rigid body densities for the first, middle and last of the 5 envs
>>> prims.set_sleep_thresholds(np.full(3, 1e-5), indices=np.array([0, 2, 4]))
```

set_velocities(
velocities:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set the linear and angular velocities of the prims in the view at once.
The method does this through the PhysX API only. It has to be called after initialization
Warning
This method will immediately set the rigid prim state
Parameters:

- velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]) – linear and angular velocities respectively to set the rigid prims to. shape is (M, 6).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Hint
This method belongs to the methods used to set the rigid prim kinematic state:
`set_velocities` (`set_linear_velocities`, `set_angular_velocities`)
Example:

```
>>> # set each rigid prim linear velocity to (1., 1., 1.) and angular velocity to (5., 5., 5.)
>>> velocities = np.ones((num_envs, 6))
>>> velocities[:,3:] = 5.0
>>> prims.set_velocities(velocities)
>>>
>>> # set only the rigid prim velocities for the first, middle and last of the 5 envs
>>> velocities = np.ones((3, 6))
>>> velocities[:,3:] = 5.0
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
This method will change (teleport) the prim poses immediately to the specified value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prim. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all rigid prims in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the rigid prims for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
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

propertyname:str
Returns: str: name given to the prims view when instantiating it.

propertynum_shapes:int
Returns:
number of rigid shapes for the prims in the view.

Return type:
int

Example:

```
>>> prims.num_shapes
1
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

classSdfShapePrim(
prim_paths_expr:str,
num_query_points:int,
prepare_sdf_schemas:bool=True,
name:str='sdf_shape_view',
positions:ndarray|Tensor|warp.array|None =None,
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
scales:ndarray|Tensor|warp.array|None =None,
visibilities:ndarray|Tensor|warp.array|None =None,
reset_xform_properties:bool=True,
collisions:ndarray|Tensor|warp.array|None =None,
track_contact_forces:bool=False,
prepare_contact_sensors:bool=False,
disable_stablization:bool=True,
contact_filter_prim_paths_expr:List[str]|None =[],
)Bases: GeometryPrim
High level functions to deal with geometry prims that provide their Signed Distance Field (SDF).
This object wraps all matching mesh geometry prims found at the regex provided at the prim_paths_expr.
Parameters:

- prim_paths_expr (str) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Microwave” will match /World/Env1/Microwave, /World/Env2/Microwave..etc. (a non regex prim path can also be used to encapsulate one XForm).

- num_query_points (int) – number of points queried by this view object

- prepare_sdf_schemas (bool, optional) – apply PhysxSDFMeshCollisionAPI to prims in prim_paths_expr. Defaults to True.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “sdf_shape_view”.

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default positions in the world frame of the prim. shape is (N, 3). Defaults to None, which means left unchanged.

- translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – default quaternion orientations in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (N, 4). Defaults to None, which means left unchanged.

- scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – local scales to be applied to the prim’s dimensions. shape is (N, 3). Defaults to None, which means left unchanged.

- visibilities (Optional[Union[np.ndarray, torch.Tensor, wp.array], optional) – set to false for an invisible prim in the stage while rendering. shape is (N,). Defaults to None.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- collisions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – Set to True if the geometry already have/ should have a collider (i.e not only a visual geometry). shape is (N,). Defaults to None.

- track_contact_forces (bool, Optional) – if enabled, the view will track the net contact forces on each geometry prim in the view. Note that the collision flag should be set to True to report contact forces. Defaults to False.

- prepare_contact_sensors (bool, Optional) – applies contact reporter API to the prim if it already does not have one. Defaults to False.

- disable_stablization (bool, optional) – disables the contact stabilization parameter in the physics context. Defaults to True.

- contact_filter_prim_paths_expr (Optional[List[str]], Optional) – a list of filter expressions which allows for tracking contact forces between the geometry prim and this subset through get_contact_force_matrix().

apply_collision_apis(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Apply the collision API to prims in the view and update internal variables
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # apply the collision API for all prims
>>> prims.apply_collision_apis()
>>>
>>> # apply the collision API for the first, middle and last of the 5 envs
>>> prims.apply_collision_apis(indices=np.array([0, 2, 4]))
```

apply_physics_materials(
physics_materials:PhysicsMaterial |List[PhysicsMaterial ],
weaker_than_descendants:bool|List[bool]|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Used to apply physics material to prims in the view and optionally its descendants.
Parameters:

- physics_materials (Union[PhysicsMaterial , List[PhysicsMaterial ]]) – physics materials to be applied to prims in the view. Physics material can be used to define friction, restitution..etc. Note: if a physics material is not defined, the defaults will be used from PhysX. If a list is provided then its size has to be equal the view’s size or indices size. If one material is provided it will be applied to all prims in the view.

- weaker_than_descendants (Optional[Union[bool, List[bool]]], optional) – True if the material shouldn’t override the descendants materials, otherwise False. Defaults to False. If a list of visual materials is provided then a list has to be provided with the same size for this arg as well.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Raises:

- Exception – length of physics materials != length of prims indexed

- Exception – length of physics materials != length of weaker descendants arg

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
>>>
>>> # apply the material to all prims
>>> prims.apply_physics_materials(material) # or [material] * num_envs
>>>
>>> # apply the collision API for the first, middle and last of the 5 envs
>>> prims.apply_physics_materials(material, indices=np.array([0, 2, 4]))
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
disable_collision(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Disables collision on prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # disable the collision API for all prims
>>> prims.disable_collision()
>>>
>>> # disable the collision API for the prims for the first, middle and last of the 5 envs
>>> prims.disable_collision(indices=np.array([0, 2, 4]))
```

enable_collision(
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Enables collision on prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # enable the collision API for all prims
>>> prims.enable_collision()
>>>
>>> # enable the collision API for the prims for the first, middle and last of the 5 envs
>>> prims.enable_collision(indices=np.array([0, 2, 4]))
```

get_applied_physics_materials(
indices:ndarray|list|Tensor|warp.array|None =None,
)→List[PhysicsMaterial ]Get the applied physics material to prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
the current applied physics materials for prims in the view.

Return type:
List[PhysicsMaterial ]

Example:

```
>>> # get the applied material for all prims
>>> prims.get_applied_physics_materials()
[<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>]
>>>
>>> # get the applied material for the first, middle and last of the 5 envs
>>> prims.get_applied_physics_materials(indices=np.array([0, 2, 4]))
[<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>,
<isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f720859ece0>]
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

get_collision_approximations(
indices:ndarray|list|Tensor|warp.array|None =None,
)→List[str]Get collision approximation types for prims in the view.

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
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
approximations used for collision. size == M or size of the view.

Return type:
List[str]

Example:

```
>>> # get the collision approximation of all prims. Returned size is (5,).
>>> prims.get_collision_approximations()
['none', 'none', 'none', 'none', 'none']
>>>
>>> # get the collision approximation of the prims for the first, middle and last of the 5 envs
>>> prims.get_collision_approximations(indices=np.array([0, 2, 4]))
['none', 'none', 'none']
```

get_contact_force_data(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→Tuple[ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray,ndarray|Tensor|warp.indexedarray]Get more detailed contact information between the prims in the view and the filter prims. Specifically, this method provides individual contact normals, contact points, contact separations as well as contact forces for each pair (the sum of which equals the forces that the get_contact_force_matrix method provides as the force aggregate of a pair) Given to the dynamic nature of collision between bodies, this method will provide buffers of contact data which are arranged sequentially for each pair. The starting index and the number of contact data points for each pair in this stream can be realized from pair_contacts_start_indices, and pair_contacts_count tensors. They both have a dimension of (self.num_shapes, self.num_filters) where filter_count is determined according to the filter_paths_expr parameter.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Tuple[Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray],
Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray], Union[np.ndarray, torch.Tensor, wp.indexedarray]]: A set of buffers for normal forces with shape (max_contact_count, 1), points with shape (max_contact_count, 3), normals with shape (max_contact_count, 3), and distances with shape (max_contact_count, 1), as well as two tensors with shape (M, self.num_filters) to indicate the starting index and the number of contact data points per pair in the aforementioned buffers.

get_contact_force_matrix(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayIf the object is initialized with filter_paths_expr list, this method returns the contact forces between the prims in the view and the filter prims. i.e., a matrix of dimension (self.count, self._contact_view.num_filters, 3) where num_filters is the determined according to the filter_paths_expr parameter.
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (M, self._contact_view.num_filters, 3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_contact_offsets(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet contact offsets for prims in the view.
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
Contact offsets of the collision shapes. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the contact offsets of all prims. Returned shape is (5,).
>>> prims.get_contact_offsets()
[-inf -inf -inf -inf -inf]
>>>
>>> # get the contact offsets of the prims for the first, middle and last of the 5 envs
>>> prims.get_contact_offsets(indices=np.array([0, 2, 4]))
[-inf -inf -inf]
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

get_friction_data(
indices:ndarray|List|Tensor|warp.array|None =None,
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

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame)
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
first index is translations in the local frame of the prims. shape is (M, 3).
second index is quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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

get_min_torsional_patch_radii(
indices:ndarray|list|Tensor|None =None,
)→ndarray|TensorGet minimum torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
minimum radius of the contact patch used to apply torsional friction. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor]

Example:

```
>>> # get the minimum torsional patch radius of all prims. Returned shape is (5,).
>>> prims.get_min_torsional_patch_radii()
[0. 0. 0. 0. 0.]
>>>
>>> # get the minimum torsional patch radius of the prims for the first, middle and last of the 5 envs
>>> prims.get_min_torsional_patch_radii(indices=np.array([0, 2, 4]))
[0. 0. 0.]
```

get_net_contact_forces(
indices:ndarray|List|Tensor|warp.array|None =None,
clone:bool=True,
dt:float=1.0,
)→ndarray|Tensor|warp.indexedarrayIf contact forces of the prims in the view are tracked, this method returns the net contact forces on prims. i.e., a matrix of dimension (self.count, 3)
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

- dt (float) – time step multiplier to convert the underlying impulses to forces. If the default value is used then the forces are in fact contact impulses

Returns:
Net contact forces of the prims with shape (M,3).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

get_rest_offsets(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet rest offsets for prims in the view.
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
Rest offsets of the collision shapes. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the rest offsets of all prims. Returned shape is (5,).
>>> prims.get_rest_offsets()
[-inf -inf -inf -inf -inf]
>>>
>>> # get the rest offsets of the prims for the first, middle and last of the 5 envs
>>> prims.get_rest_offsets(indices=np.array([0, 2, 4]))
[-inf -inf -inf]
```

get_sdf_and_gradients(
points:ndarray|Tensor,
indices:ndarray|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGet the SDF values and gradients of the query points
Parameters:

- points ([Union[np.ndarray, torch.Tensor]]) – points (represented in the local frames of meshes) to be queried for sdf and gradients. shape is (self.num_shapes, self.num_query_points, 3).

- indices (Optional[Union[np.ndarray, list, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
SDF values and gradients of points for prims with shape (self.num_shapes, self.num_query_points, 4). The first component is the SDF value while the last three represent the gradient

Return type:
Union[np.ndarray, torch.Tensor]

get_sdf_margins(
indices:ndarray|List|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets sdf margin values.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
margins of the sdf collision apis for prims in the view. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor]

get_sdf_narrow_band_thickness(
indices:ndarray|List|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets sdf collision narrow band thickness values.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
narrow band thickness of the sdf collision apis for prims in the view. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor]

get_sdf_resolution(
indices:ndarray|List|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets sdf collision resolution values.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
resolutions of the sdf collision apis for prims in the view. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor]

get_sdf_subgrid_resolution(
indices:ndarray|List|Tensor|None =None,
clone:bool=True,
)→ndarray|TensorGets sdf collision subgrid resolution values.
Parameters:

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- clone (bool, optional) – True to return a clone of the internal buffer. Otherwise False. Defaults to True.

Returns:
subgrid resolutions of the sdf collision apis for prims in the view. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor]

get_torsional_patch_radii(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayGet torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
radius of the contact patch used to apply torsional friction. shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # get the torsional patch radius of all prims. Returned shape is (5,).
>>> prims.get_torsional_patch_radii()
[0. 0. 0. 0. 0.]
>>>
>>> # get the torsional patch radius of the prims for the first, middle and last of the 5 envs
>>> prims.get_torsional_patch_radii(indices=np.array([0, 2, 4]))
[0. 0. 0.]
```

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
usd:bool=True,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get the poses of the prims in the view with respect to the world’s frame
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Returns:
first index is positions in the world frame of the prims. shape is (M, 3).
second index is quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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
)→None Create a physics simulation view if not passed and creates a sdf shape view in physX.
Parameters:
physics_sim_view (omni.physics.tensors.SimulationView, optional) – current physics simulation view. Defaults to None.

is_collision_enabled(
indices:ndarray|list|Tensor|warp.array|None =None,
)→ndarray|Tensor|warp.indexedarrayQueries if collision is enabled on prims in the view.
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
True if collision is enabled. Shape is (M,).

Return type:
Union[np.ndarray, torch.Tensor, wp.indexedarray]

Example:

```
>>> # check if the collision is enabled for all prims. Returned size is (5,).
>>> prims.is_collision_enabled()
[ True True True True True]
>>>
>>> # check if the collision is enabled for the first, middle and last of the 5 envs
>>> prims.is_collision_enabled(indices=np.array([0, 2, 4]))
[ True True True]
```

is_physics_handle_valid()→bool
Returns:
True if the physics handle of the view is valid (i.e physics is initialized for the view). Otherwise False.

Return type:
bool

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

post_reset()→None
Reset the prims to its default state
Example:

```
>>> prims.post_reset()
```

set_collision_approximations(
approximation_types:List[str],
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set collision approximation types for prims in the view.

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
Parameters:

- approximation_types (List[str]) – approximations used for collision. List size == M or the size of the view.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the collision approximations for all the prims to the specified values.
>>> prims.set_collision_approximations(["convexDecomposition"] * num_envs)
>>>
>>> # set the collision approximations for the first, middle and last of the 5 envs
>>> types = ["convexDecomposition", "convexHull", "meshSimplification"]
>>> prims.set_collision_approximations(types, indices=np.array([0, 2, 4]))
```

set_contact_offsets(
offsets:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set contact offsets for prims in the view.
Shapes whose distance is less than the sum of their contact offset values will generate contacts
Search for Advanced Collision Detection in PhysX docs for more details
Parameters:

- offsets (Union[np.ndarray, torch.Tensor, wp.array]) – Contact offsets of the collision shapes. Allowed range [maximum(0, rest_offset), 0]. Default value is -inf, means default is picked by simulation based on the shape extent. Shape (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the contact offset for all the prims to the specified values.
>>> prims.set_contact_offsets(np.full(num_envs, 0.02))
>>>
>>> # set the contact offset for the first, middle and last of the 5 envs
>>> prims.set_contact_offsets(np.full(3, 0.02), indices=np.array([0, 2, 4]))
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

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame)
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
>>> # reposition all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs
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

set_min_torsional_patch_radii(
radii:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set minimum torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:

- radii (Union[np.ndarray, torch.Tensor, wp.array]) – minimum radius of the contact patch used to apply torsional friction. Allowed range [0, max_float]. shape is (M, ).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the minimum torsional patch radius for all the prims to the specified values.
>>> prims.set_min_torsional_patch_radii(np.full(num_envs, 0.05))
>>>
>>> # set the minimum torsional patch radius for the first, middle and last of the 5 envs
>>> prims.set_min_torsional_patch_radii(np.full(3, 0.05), indices=np.array([0, 2, 4]))
```

set_rest_offsets(
offsets:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set rest offsets for prims in the view.
Two shapes will come to rest at a distance equal to the sum of their rest offset values. If the rest offset is 0, they should converge to touching exactly
Search for Advanced Collision Detection in PhysX docs for more details
Warning
The contact offset must be positive and greater than the rest offset
Parameters:

- offsets (Union[np.ndarray, torch.Tensor, wp.array]) – Rest offset of a collision shape. Allowed range [-max_float, contact_offset]. Default value is -inf, means default is picked by simulation. For rigid bodies its zero. Shape (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the rest offset for all the prims to the specified values.
>>> prims.set_rest_offsets(np.full(num_envs, 0.01))
>>>
>>> # set the rest offset for the first, middle and last of the 5 envs
>>> prims.set_rest_offsets(np.full(3, 0.01), indices=np.array([0, 2, 4]))
```

set_sdf_margins(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Sets signed distance field margins for prims in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – sdf margins to be set. shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_sdf_narrow_band_thickness(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Sets signed distance field narrow band thicknesses for prims in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – sdf margins to be set. shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_sdf_resolution(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Sets signed distance field subgrid resolutions for prims in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – sdf margins to be set. shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_sdf_subgrid_resolution(
values:ndarray|Tensor,
indices:ndarray|List|Tensor|None =None,
)→None Sets signed distance field subgrid resolutions for prims in the view.
Parameters:

- values (Union[np.ndarray, torch.Tensor]) – sdf margins to be set. shape (M,).

- indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

set_torsional_patch_radii(
radii:ndarray|Tensor|warp.array,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set torsional patch radii for prims in the view.
Search for “Torsional Patch Radius” in PhysX docs for more details
Parameters:

- radii (Union[np.ndarray, torch.Tensor, wp.array]) – radius of the contact patch used to apply torsional friction. Allowed range [0, max_float]. shape is (M,).

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to manipulate. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Example:

```
>>> # set the torsional patch radius for all the prims to the specified values.
>>> prims.set_torsional_patch_radii(np.full(num_envs, 0.1))
>>>
>>> # set the torsional patch radius for the first, middle and last of the 5 envs
>>> prims.set_torsional_patch_radii(np.full(3, 0.1), indices=np.array([0, 2, 4]))
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
)→None Set prim poses in the view with respect to the world’s frame
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prims. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all prims in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
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

propertygeoms:List[pxr.UsdGeom.Gprim]
Returns:
USD geom objects encapsulated.

Return type:
List[UsdGeom.Gprim]

Example:

```
>>> prims.geoms
[UsdGeom.Gprim(Usd.Prim(</World/envs/env_0/Xform>)), UsdGeom.Gprim(Usd.Prim(</World/envs/env_1/Xform>)),
UsdGeom.Gprim(Usd.Prim(</World/envs/env_2/Xform>)), UsdGeom.Gprim(Usd.Prim(</World/envs/env_3/Xform>)),
UsdGeom.Gprim(Usd.Prim(</World/envs/env_4/Xform>))]
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

propertyname:str
Returns: str: name given to the prims view when instantiating it.

propertynum_query_points:int
Returns: int: number of points queried by this view object.

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

classXFormPrim(
prim_paths_expr:str|List[str],
name:str='xform_prim_view',
positions:ndarray|Tensor|None =None,
translations:ndarray|Tensor|None =None,
orientations:ndarray|Tensor|None =None,
scales:ndarray|Tensor|None =None,
visibilities:ndarray|Tensor|None =None,
reset_xform_properties:bool=True,
usd:bool=True,
)Bases: `Prim`
Provides high level functions to deal with a Xform prim view (one or many) and its descendants as well as its attributes/properties.
This class wraps all matching Xforms found at the regex provided at the `prim_paths_expr` argument
Note
Each prim will have `xformOp:orient`, `xformOp:translate` and `xformOp:scale` only post-init, unless it is a non-root articulation link.
Parameters:

- prim_paths_expr (Union[str, List[str]]) – prim paths regex to encapsulate all prims that match it. example: “/World/Env[1-5]/Franka” will match /World/Env1/Franka, /World/Env2/Franka..etc. (a non regex prim path can also be used to encapsulate one Xform). Additionally a list of regex can be provided. example [“/World/Env[1-5]/Franka”, “/World/Env[10-19]/Franka”].

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “xform_prim_view”.

- positions (Optional[Union[np.ndarray, torch.Tensor]], optional) – default positions in the world frame of the prim. shape is (N, 3). Defaults to None, which means left unchanged.

- translations (Optional[Union[np.ndarray, torch.Tensor]], optional) – default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor]], optional) – default quaternion orientations in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (N, 4). Defaults to None, which means left unchanged.

- scales (Optional[Union[np.ndarray, torch.Tensor]], optional) – local scales to be applied to the prim’s dimensions. shape is (N, 3). Defaults to None, which means left unchanged.

- visibilities (Optional[Union[np.ndarray, torch.Tensor]], optional) – set to false for an invisible prim in the stage while rendering. shape is (N,). Defaults to None.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- usd (bool, optional) – True to strictly read/ write from usd. Otherwise False to allow read/ write from Fabric during initialization. Defaults to True.

Raises:

- Exception – if translations and positions defined at the same time.

- Exception – No prim was matched using the prim_paths_expr provided.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.cloner import GridCloner
>>> from isaacsim.core.prims import XFormPrim
>>> from pxr import UsdGeom
>>>
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
>>> env_pos = cloner.clone(
... source_prim_path=env_zero_path,
... prim_paths=cloner.generate_paths("/World/envs/env", num_envs),
... copy_from_source=True
... )
>>>
>>> # wrap all Xforms
>>> prims = XFormPrim(prim_paths_expr="/World/envs/env.*", name="xform_view")
>>> prims
<isaacsim.core.prims.xform_prim.XFormPrim object at 0x7f8ffd22ebc0>
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

get_local_poses(
indices:ndarray|list|Tensor|warp.array|None =None,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get prim poses in the view with respect to the local frame (the prim’s parent frame)
Parameters:
indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

Returns:
first index is translations in the local frame of the prims. shape is (M, 3).
second index is quaternion orientations in the local frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the local frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_local_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the local frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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
usd:bool=True,
)→Tuple[ndarray,ndarray]|Tuple[Tensor,Tensor]|Tuple[warp.indexedarray,warp.indexedarray]Get the poses of the prims in the view with respect to the world’s frame
Parameters:

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Returns:
first index is positions in the world frame of the prims. shape is (M, 3).
second index is quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4).

Return type:
Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]

Example:

```
>>> # get all prims poses with respect to the world's frame.
>>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
>>> positions, orientations = prims.get_world_poses()
>>> positions
[[ 1.5 -0.75 0. ]
[ 1.5 0.75 0. ]
[ 0. -0.75 0. ]
[ 0. 0.75 0. ]
[-1.5 -0.75 0. ]]
>>> orientations
[[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]
[1. 0. 0. 0.]]
>>>
>>> # get only the prims poses with respect to the world's frame for the first, middle and last of the 5 envs.
>>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
>>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
>>> positions
[[ 1.5 -0.75 0. ]
[ 0. -0.75 0. ]
[-1.5 -0.75 0. ]]
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

post_reset()→None
Reset the prims to its default state
Example:

```
>>> prims.post_reset()
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

set_local_poses(
translations:ndarray|Tensor|warp.array|None =None,
orientations:ndarray|Tensor|warp.array|None =None,
indices:ndarray|list|Tensor|warp.array|None =None,
)→None Set prim poses in the view with respect to the local frame (the prim’s parent frame)
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
>>> # reposition all prims
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_local_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs
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
)→None Set prim poses in the view with respect to the world’s frame
Warning
This method will change (teleport) the prim poses immediately to the indicated value
Parameters:

- positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – positions in the world frame of the prims. shape is (M, 3). Defaults to None, which means left unchanged.

- orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional) – quaternion orientations in the world frame of the prims. quaternion is scalar-first (w, x, y, z). shape is (M, 4). Defaults to None, which means left unchanged.

- indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional) – indices to specify which prims to query. Shape (M,). Where M <= size of the encapsulated prims in the view. Defaults to None (i.e: all prims in the view).

- usd (bool, optional) – True to query from usd. Otherwise False to query from Fabric data. Defaults to True.

Hint
This method belongs to the methods used to set the prim state
Example:

```
>>> # reposition all prims in row (x-axis)
>>> positions = np.zeros((num_envs, 3))
>>> positions[:,0] = np.arange(num_envs)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
>>> prims.set_world_poses(positions, orientations)
>>>
>>> # reposition only the prims for the first, middle and last of the 5 envs in column (y-axis)
>>> positions = np.zeros((3, 3))
>>> positions[:,1] = np.arange(3)
>>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
>>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
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

propertyname:str
Returns: str: name given to the prims view when instantiating it.

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

### Single Prims
Warning
The use of Single Prim classes (a particular case of the Prims classes for a single prim) is discouraged as they will be removed in future versions. Use Prims classes (formerly Prim Views) instead.
classSingleArticulation(
prim_path:str,
name:str='articulation',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
reset_xform_properties:bool=True,
articulation_controller:ArticulationController |None =None,
enable_residual_reports:bool=False,
)Bases: `_SinglePrimWrapper`
High level wrapper to deal with an articulation prim (only one articulation prim) and its attributes/properties.
Warning
The articulation object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “articulation”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. Shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). Shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). Shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. Shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- articulation_controller (Optional[ArticulationController ], optional) – a custom ArticulationController which inherits from it. Defaults to creating the basic ArticulationController.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.prims import SingleArticulation
>>>
>>> usd_path = "/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd"
>>> prim_path = "/World/envs/env_0/panda"
>>>
>>> # load the Franka Panda robot USD file
>>> stage_utils.add_reference_to_stage(usd_path, prim_path)
>>>
>>> # wrap the prim as an articulation
>>> prim = SingleArticulation(prim_path=prim_path, name="franka_panda")
>>> prim
<isaacsim.core.prims.single_articulation.SingleArticulation object at 0x7fdd165bf520>
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

get_position_residual(
report_max:bool|None =True,
)→floatGet physics solver position residuals for articulations. This is the residual across all joints that are part of articulations.
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

get_velocity_residual(
report_max:bool|None =True,
)→floatGet physics solver velocity residuals for articulations. This is the residual across all joints that are part of articulations.
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
Reset the prim to its default state (position and orientation).
Note
For an articulation, in addition to configuring the root prim’s default position and spatial orientation (defined via the `set_default_state` method), the joint’s positions, velocities, and efforts (defined via the `set_joints_default_state` method) are imposed
Example:

```
>>> prim.post_reset()
```

set_angular_velocity(
velocity:ndarray,
)→None Set the angular velocity of the root articulation prim
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

set_linear_velocity(
velocity:ndarray,
)→None Set the linear velocity of the root articulation prim
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

set_sleep_threshold(threshold:float)→None
Set the threshold for articulations to enter a sleep state
Search for Articulations and Sleeping in PhysX docs for more details
Parameters:
threshold (float) – sleep threshold

Example:

```
>>> prim.set_sleep_threshold(0.01)
```

set_solver_position_iteration_count(
count:int,
)→None Set the solver (position) iteration count for the articulation
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

set_stabilization_threshold(
threshold:float,
)→None Set the mass-normalized kinetic energy below which the articulation may participate in stabilization
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

classSingleClothPrim(
prim_path:str,
particle_system:SingleParticleSystem ,
particle_material:ParticleMaterial |None =None,
name:str|None ='cloth',
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
particle_mass:float|None =0.01,
pressure:float|None =None,
particle_group:int|None =0,
self_collision:bool|None =True,
self_collision_filter:bool|None =True,
stretch_stiffness:float|None =None,
bend_stiffness:float|None =None,
shear_stiffness:float|None =None,
spring_damping:float|None =None,
)Bases: `_SinglePrimWrapper`
Cloth primitive object provide functionalities to create and control cloth parameters
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

get_cloth_bend_stiffness()→float
Reports a single value that would be used to generate the stiffnesses. This API does not report the actually created stiffnesses.
Returns:
The bend stiffness.

Return type:
float

get_cloth_damping()→ndarray|Tensor
Reports a single value that would be used to generate the dampings. This API does not report the actually created dampings.
Returns:
The spring damping.

Return type:
float

get_cloth_shear_stiffness()→float
Reports a single value that would be used to generate the stiffnesses. This API does not report the actually created stiffnesses.
Returns:
The shear stiffness.

Return type:
float

get_cloth_stretch_stiffness()→float
Reports a single value that would be used to generate the stiffnesses. This API does not report the actually created stiffnesses.
Returns:
The stretch stiffness.

Return type:
float

get_current_dynamic_state()→DynamicState
Return the DynamicState that contains the position and orientation of the cloth prim
Returns:
position (np.ndarray, optional):
position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

orientation (np.ndarray, optional):
quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Return type:
DynamicState

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

get_particle_group()→int
Returns:
self collision.

Return type:
bool

get_pressure()→float
Returns:
pressure value.

Return type:
float

get_self_collision()→bool
Returns:
self collision.

Return type:
bool

get_self_collision_filter()→bool
Returns:
self collision filter.

Return type:
bool

get_spring_damping()→ndarray|Tensor
Gets damping values of spring constraints
Returns:
The spring damping.

Return type:
Union[np.ndarray, torch.Tensor]

get_stretch_stiffness()→ndarray|Tensor
Gets stretch stiffness values of spring constraints
Returns:
The stretch stiffness.

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

set_cloth_bend_stiffness(stiffness:float)→None
Sets a single bend stiffness value to all springs constraints in the cloth
Parameters:
stiffness (float) – The cloth springs bend stiffness value. Range: [0 , inf), Units: force/distance = mass/second/second

set_cloth_damping(damping:float)→None
Sets a single damping value to all springs constraints in the cloth
Parameters:
damping (float) – The cloth springs damping value. Range: [0 , inf), Units: force/velocity = mass/second

set_cloth_shear_stiffness(stiffness:float)→None
Sets a single shear stiffness value to all springs constraints in the cloth
Parameters:
stiffness (float) – The cloth springs shear stiffness value. Range: [0 , inf), Units: force/distance = mass/second/second

set_cloth_stretch_stiffness(
stiffness:ndarray|Tensor,
)→None Sets a single stretch stiffness value to all springs constraints in the cloth
Parameters:
stiffness (Union[np.ndarray, torch.Tensor]) – The cloth springs stretch stiffness value. Range: [0 , inf), Units: force/distance = mass/second/second

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

set_particle_group(particle_group:int)→None
Parameters:
particle_group (int) – particle group.

set_pressure(pressure:float)→None
Parameters:
pressure (float) – pressure value.

set_self_collision(self_collision:bool)→None
Parameters:
self_collision (bool) – self collision.

set_self_collision_filter(
self_collision_filter:bool,
)→None Parameters:
self_collision_filter (bool) – self collision filter.

set_spring_damping(
damping:ndarray|Tensor,
)→None Sets damping values of spring constraints in the cloth
Parameters:
damping (List[float]) – The damping values of springs. Range: [0 , inf), Units: force/distance = mass/second

set_stretch_stiffness(
stiffness:ndarray|Tensor,
)→None Sets stretch stiffness values of spring constraints in the cloth It represents a stiffness for linear springs placed between particles to counteract stretching.
Parameters:
stiffness (Union[np.ndarray, torch.Tensor]) – The stretch stiffnesses. Range: [0 , inf), Units: force/distance = mass/second/second

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

propertymesh:pxr.UsdGeom.Mesh
Returns: Usd.Prim: USD Prim object that this object tracks.

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

classSingleDeformablePrim(
prim_path:str,
deformable_material:DeformableMaterial |None =None,
name:str|None ='deformable',
position:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
vertex_velocity_damping:float|None =None,
sleep_damping:float|None =None,
sleep_threshold:float|None =None,
settling_threshold:float|None =None,
self_collision:bool|None =True,
self_collision_filter_distance:float|None =None,
solver_position_iteration_count:int|None =None,
kinematic_enabled:bool|None =False,
simulation_rest_points:Sequence[float]|None =None,
simulation_indices:Sequence[int]|None =None,
simulation_hexahedral_resolution:int|None =10,
collision_rest_points:Sequence[float]|None =None,
collision_indices:Sequence[int]|None =None,
collision_simplification:bool|None =True,
collision_simplification_remeshing:bool|None =True,
collision_simplification_remeshing_resolution:int|None =0,
collision_simplification_target_triangle_count:int|None =0,
collision_simplification_force_conforming:bool|None =False,
embedding:Sequence[int]|None =None,
)Bases: `_SinglePrimWrapper`
Deformable primitive object provide functionalities to create and control deformable objects
apply_deformable_material(
deformable_materials:DeformableMaterial ,
)→None apply_visual_material(
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

get_applied_deformable_material()→DeformableMaterial
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

get_collision_mesh_indices()→ndarray|Tensor
Gets the collision mesh element indices
Returns:
collision mesh element indices

Return type:
Union[np.ndarray, torch.Tensor]

get_current_dynamic_state()→DynamicState
Return the DynamicState that contains the position and orientation of the underlying xform prim
Returns:
position (np.ndarray, optional):
position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

orientation (np.ndarray, optional):
quaternion orientation in the world frame of the prim. quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

Return type:
DynamicState

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

get_self_collision()→bool
Gets the deformable body self collision
Returns:
self collision

Return type:
float

get_self_collision_filter_distance()→float
Gets the deformable body self collision filter distance
Returns:
self collision filter distance

Return type:
float

get_settling_threshold()→float
Gets the deformable body settling threshold
Returns:
settling threshold

Return type:
float

get_simulation_mesh_indices()→ndarray|Tensor
Gets the simulation mesh element indices
Returns:
simulation mesh element indices

Return type:
Union[np.ndarray, torch.Tensor]

get_simulation_mesh_rest_points()→ndarray|Tensor
Gets the simulation mesh rest positions
Returns:
simulation mesh vertices rest positions

Return type:
Union[np.ndarray, torch.Tensor]

get_sleep_damping()→float
Gets the deformable body sleep damping parameter
Returns:
sleep damping

Return type:
float

get_sleep_threshold()→float
Gets the deformable body sleep threshold
Returns:
sleep threshold

Return type:
float

get_solver_position_iteration_count()→int
Gets the solver’s positional iteration count
Returns:
positional iteration count

Return type:
int

get_vertex_velocity_damping()→float
Gets the deformable body vertex velocity damping parameter
Returns:
vertex velocity damping

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

set_self_collision(self_collision:bool)→None
Parameters:
self_collision (bool) – deformable body self collision parameter.

set_self_collision_filter_distance(
self_collision_filter_distance:float,
)→None Parameters:
self_collision_filter_distance (float) – deformable body self collision filter distance parameter.

set_settling_threshold(
settling_threshold:float,
)→None Parameters:
settling_threshold (float) – deformable body settling threshold parameter.

set_sleep_damping(sleep_damping:float)→None
Parameters:
sleep_damping (float) – deformable body sleep damping parameter.

set_sleep_threshold(
sleep_threshold:float,
)→None Parameters:
sleep_threshold (float) – deformable body sleep threshold parameter.

set_solver_position_iteration_count(
iterations:int,
)→None Parameters:
iterations (float) – solver position iteration count

set_vertex_velocity_damping(
vertex_velocity_damping:float,
)→None Parameters:
vertex_velocity_damping (float) – deformable body vertex velocity damping parameter.

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

propertymesh:pxr.UsdGeom.Mesh
Returns: Usd.Prim: USD Prim object that this object tracks.

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

classSingleGeometryPrim(
prim_path:str,
name:str='geometry_prim',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
reset_xform_properties:bool=True,
collision:bool=False,
track_contact_forces:bool=False,
prepare_contact_sensor:bool=False,
disable_stablization:bool=True,
contact_filter_prim_paths_expr:List[str]|None =[],
)Bases: `_SinglePrimWrapper`
High level wrapper to deal with a Geom prim (only one geometry prim) and its attributes/properties.
The `prim_path` should correspond to type UsdGeom.Cube, UsdGeom.Capsule, UsdGeom.Cone, UsdGeom.Cylinder, UsdGeom.Sphere or UsdGeom.Mesh.
Warning
The geometry object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Warning
Some methods require the prim to have the Physx Collision API. Instantiate the class with the `collision` parameter to True to apply the collision API.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “xform_prim”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- collision (bool, optional) – Set to True if the geometry should have a collider (i.e not only a visual geometry). Defaults to False.

- track_contact_forces (bool, Optional) – if enabled, the view will track the net contact forces on each geometry prim in the view. Note that the collision flag should be set to True to report contact forces. Defaults to False.

- prepare_contact_sensors (bool, Optional) – applies contact reporter API to the prim if it already does not have one. Defaults to False.

- disable_stablization (bool, optional) – disables the contact stabilization parameter in the physics context. Defaults to True.

- contact_filter_prim_paths_expr (Optional[List[str]], Optional) – a list of filter expressions which allows for tracking contact forces between the geometry prim and this subset through get_contact_force_matrix().

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.prims import SingleGeometryPrim
>>>
>>> # create a Cube at the given path
>>> stage_utils.get_current_stage().DefinePrim("/World/Xform", "Xform")
>>> stage_utils.get_current_stage().DefinePrim("/World/Xform/Cube", "Cube")
>>>
>>> # wrap the prim as geometry prim
>>> prim = SingleGeometryPrim("/World/Xform", collision=True)
>>> prim
<isaacsim.core.prims.single_geometry_prim.SingleGeometryPrim object at 0x7fe960247400>
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

set_min_torsional_patch_radius(
radius:float,
)→None Set the minimum radius of the contact patch used to apply torsional friction
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

classSingleParticleSystem(
prim_path:str,
name:str|None ='particle_system',
particle_system_enabled:bool|None =None,
simulation_owner:str|None =None,
contact_offset:float|None =None,
rest_offset:float|None =None,
particle_contact_offset:float|None =None,
solid_rest_offset:float|None =None,
fluid_rest_offset:float|None =None,
enable_ccd:bool|None =None,
solver_position_iteration_count:float|None =None,
max_depenetration_velocity:float|None =None,
wind:Sequence[float]=None,
max_neighborhood:int|None =None,
max_velocity:float|None =None,
global_self_collision_enabled:bool|None =None,
non_particle_collision_enabled:bool|None =None,
)Bases: `object`
A wrapper around PhysX particle system.
PhysX uses GPU-accelerated position-based-dynamics (PBD) particle simulation [1]. The particle system can be used to simulate fluids, cloth and inflatables [2].
The wrapper is useful for creating and setting solver parameters common to the particle objects associated with the system. The particle system’s solver parameters cannot be changed once the scene is playing.
Note
CPU simulation of particles is not supported. PhysX must be simulated with GPU enabled.
Reference:
[1] https://mmacklin.com/pbf_sig_preprint.pdf [2] https://docs.omniverse.nvidia.com/prod_extensions/prod_extensions/ext_physics.html#particle-simulation

apply_particle_anisotropy()→pxr.PhysxSchema.PhysxParticleAnisotropyAPI
Applies anisotropy to the particle system.
This is used to compute anisotropic scaling of particles in a post-processing step. It only affects the rendering output including iso-surface generation.

apply_particle_isotropy()→pxr.PhysxSchema.PhysxParticleAnisotropyAPI
Applies iso-surface extraction to the particle system.
This is used to define settings to extract an iso-surface from the particles in a post-processing step. It only affects the rendering output including iso-surface generation.

apply_particle_material(
particle_materials:ParticleMaterial ,
)→None apply_particle_smoothing()→pxr.PhysxSchema.PhysxParticleSmoothingAPI
Applies smoothing to the simulated particle system.
This is used to control smoothing of particles in a post-processing step. It only affects the rendering output including iso-surface generation.

get_applied_particle_material()→ParticleMaterial
get_contact_offset()→float
Returns:
The contact offset used for collisions with non-particle objects.

Return type:
float

get_enable_ccd()→bool
Returns:
Whether continuous collision detection for particles is enabled or disabled.

Return type:
bool

get_fluid_rest_offset()→float
Returns:
The rest offset used for fluid-fluid particle interactions.

Return type:
float

get_global_self_collision_enabled()→bool
Returns:
Whether self collisions to follow particle-object-specific settings
is enabled or disabled.

Return type:
bool

get_max_depenetration_velocity()→None
Returns:
The maximum velocity permitted between intersecting particles.

Return type:
float

get_max_neighborhood()→int
Returns:
The particle neighborhood size.

Return type:
int

get_max_velocity()→float
Returns:
The maximum particle velocity.

Return type:
float

get_particle_contact_offset()→float
Returns:
The contact offset used for interactions between particles.

Return type:
float

get_particle_system_enabled()→bool
Returns:
Whether particle system is enabled or not.

Return type:
bool

get_rest_offset()→float
Returns:
The rest offset used for collisions with non-particle objects.

Return type:
float

get_simulation_owner()→pxr.Usd.Prim
Returns:
The physics scene prim attached to particle system.

Return type:
Usd.Prim

get_solid_rest_offset()→float
Returns:
The rest offset used for solid-solid or solid-fluid particle interactions.

Return type:
float

get_solver_position_iteration_count()→int
Returns:
The number of solver iterations for positions.

Return type:
int

get_wind()→Sequence[float]
Returns:
The wind applied to the current particle system.

Return type:
Sequence[float]

initialize(physics_sim_view=None)→None
is_valid()→bool
Returns:
True is the current prim path corresponds to a valid prim in stage. False otherwise.

Return type:
bool

post_reset()→None
set_contact_offset(value:float)→None
Set the contact offset used for collisions with non-particle objects such as rigid or deformable bodies.
Parameters:
value (float) – The contact offset.

set_enable_ccd(value:bool)→None
Enable continuous collision detection for particles.
Parameters:
value (bool) – Whether to enable or disable.

set_fluid_rest_offset(value:float)→None
Set the rest offset used for fluid-fluid particle interactions.
Note: Must be smaller than particle contact offset.
Parameters:
value (float) – The rest offset.

set_global_self_collision_enabled(
value:bool,
)→None Enable self collisions to follow particle-object-specific settings.
If True, self collisions follow particle-object-specific settings. If False, all particle self collisions are disabled, regardless of any other settings.
Note: Improves performance if self collisions are not needed.
Parameters:
value (bool) – Whether to enable or disable.

set_max_depenetration_velocity(
value:float,
)→None Set the maximum velocity permitted to be introduced by the solver to depenetrate intersecting particles.
Parameters:
value (float) – The maximum depenetration velocity.

set_max_neighborhood(value:int)→None
Set the particle neighborhood size.
Parameters:
value (int) – The neighborhood size.

set_max_velocity(value:float)→None
Set the maximum particle velocity.
Parameters:
value (float) – The maximum velocity.

set_particle_contact_offset(value:float)→None
Set the contact offset used for interactions between particles.
Note: Must be larger than solid and fluid rest offsets.
Parameters:
value (float) – The contact offset.

set_particle_system_enabled(value:bool)→None
Set enabling of the particle system.
Parameters:
value (bool) – Whether to enable or disable.

set_rest_offset(value:float)→None
Set the rest offset used for collisions with non-particle objects such as rigid or deformable bodies.
Parameters:
value (float) – The rest offset.

set_simulation_owner(value:str)→None
Set the PhysicsScene that simulates this particle system.
Parameters:
value (str) – The prim path to the physics scene.

set_solid_rest_offset(value:float)→None
Set the rest offset used for solid-solid or solid-fluid particle interactions.
Note: Must be smaller than particle contact offset.
Parameters:
value (float) – The rest offset.

set_solver_position_iteration_count(
value:int,
)→None Set the number of solver iterations for position.
Parameters:
value (int) – Number of solver iterations.

set_wind(value:Sequence[float])→None
Set the wind velocity applied to the current particle system.
Parameters:
value (Sequence[float]) – The wind applied to the current particle system.

propertyname:str|None
Returns: str: name given to the prim when instantiating it. Otherwise None.

propertyparticle_system:pxr.PhysxSchema.PhysxParticleSystem
Returns: PhysxSchema.PhysxParticleSystem: The particle system.

propertyprim:pxr.Usd.Prim
Returns: Usd.Prim: The USD prim present.

propertyprim_path:str
Returns: str: The stage path to the particle system.

classSingleRigidPrim(
prim_path:str,
name:str='rigid_prim',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
reset_xform_properties:bool=True,
mass:float|None =None,
density:float|None =None,
linear_velocity:ndarray|None =None,
angular_velocity:ndarray|None =None,
)Bases: `_SinglePrimWrapper`
High level wrapper to deal with a rigid body prim (only one rigid body prim) and its attributes/properties.
Warning
The rigid body object must be initialized in order to be able to operate on it. See the `initialize` method for more details.
Note
If the prim does not already have the Rigid Body API applied to it before init, it will apply it.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “rigid_prim”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

- mass (Optional[float], optional) – mass in kg. Defaults to None.

- density (Optional[float], optional) – density. Defaults to None.

- linear_velocity (Optional[np.ndarray], optional) – linear velocity in the world frame. Defaults to None.

- angular_velocity (Optional[np.ndarray], optional) – angular velocity in the world frame. Defaults to None.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> from isaacsim.core.prims import SingleRigidPrim
>>>
>>> # create a Cube at the given path
>>> stage_utils.get_current_stage().DefinePrim("/World/Xform", "Xform")
>>> stage_utils.get_current_stage().DefinePrim("/World/Xform/Cube", "Cube")
>>>
>>> # wrap the prim as rigid prim
>>> prim = SingleRigidPrim("/World/Xform")
>>> prim
<isaacsim.core.prims.single_rigid_prim.SingleRigidPrim object at 0x7fc4a7f56e90>
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

get_com()→float
Get the center of mass pose of the rigid body
Returns:
position of the center of mass of the rigid body. np.ndarray: orientation of the center of mass of the rigid body.

Return type:
np.ndarray

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

set_com(
position:ndarray,
orientation:ndarray,
)→None Set the center of mass pose of the rigid body
Parameters:

- position (np.ndarray) – center of mass position. Shape (3,).

- orientation (np.ndarray) – center of mass orientation. Shape (4,).

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

set_sleep_threshold(threshold:float)→None
Set the threshold for the rigid body to enter a sleep state
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details
Parameters:
threshold (float) – Mass-normalized kinetic energy threshold below which an actor may go to sleep. Range: [0, inf) Defaults: 0.00005 * tolerancesSpeed* tolerancesSpeed Units: distance^2 / second^2.

Example:

```
>>> prim.set_sleep_threshold(1e-5)
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

classSingleXFormPrim(
prim_path:str,
name:str='xform_prim',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
visible:bool|None =None,
reset_xform_properties:bool=True,
)Bases: `_SinglePrimWrapper`
Provides high level functions to deal with an Xform prim (only one Xform prim) and its attributes/properties
If there is an Xform prim present at the path, it will use it. Otherwise, a new XForm prim at the specified prim path will be created
Note
The prim will have `xformOp:orient`, `xformOp:translate` and `xformOp:scale` only post-init, unless it is a non-root articulation link.
Parameters:

- prim_path (str) – prim path of the Prim to encapsulate or create.

- name (str, optional) – shortname to be used as a key by Scene class. Note: needs to be unique if the object is added to the Scene. Defaults to “xform_prim”.

- position (Optional[Sequence[float]], optional) – position in the world frame of the prim. shape is (3, ). Defaults to None, which means left unchanged.

- translation (Optional[Sequence[float]], optional) – translation in the local frame of the prim (with respect to its parent prim). shape is (3, ). Defaults to None, which means left unchanged.

- orientation (Optional[Sequence[float]], optional) – quaternion orientation in the world/ local frame of the prim (depends if translation or position is specified). quaternion is scalar-first (w, x, y, z). shape is (4, ). Defaults to None, which means left unchanged.

- scale (Optional[Sequence[float]], optional) – local scale to be applied to the prim’s dimensions. shape is (3, ). Defaults to None, which means left unchanged.

- visible (bool, optional) – set to false for an invisible prim in the stage while rendering. Defaults to True.

- reset_xform_properties (bool, optional) – True if the prims don’t have the right set of xform properties (i.e: translate, orient and scale) ONLY and in that order. Set this parameter to False if the object were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.

Raises:
Exception – if translation and position defined at the same time

Example:

```
>>> from isaacsim.core.prims import SingleXFormPrim
>>>
>>> # given the stage: /World. Get the Xform prim at /World
>>> prim = SingleXFormPrim("/World")
>>> prim
<isaacsim.core.prims.single_xform_prim.SingleXFormPrim object at 0x7f52381547c0>
>>>
>>> # create a new Xform prim at path: /World/Objects
>>> prim = SingleXFormPrim("/World/Objects", name="objects")
>>> prim
<isaacsim.core.prims.single_xform_prim.SingleXFormPrim object at 0x7f525c11d420>
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
