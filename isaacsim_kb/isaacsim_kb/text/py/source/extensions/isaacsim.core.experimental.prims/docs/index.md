<!-- source: py/source/extensions/isaacsim.core.experimental.prims/docs/index.html | title: [isaacsim.core.experimental.prims] Isaac Sim Core (Prims) — Isaac Sim -->

# [isaacsim.core.experimental.prims] Isaac Sim Core (Prims)
Version: 0.8.1
The Core Prims extension provides a set of APIs to wrap one or more USD prims in the stage in order to manipulate (read/write) their attributes and perform other operations during the simulation.
[image: Preview]

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API
Warning
The API featured in this extension is experimental and subject to change without deprecation cycles. Although we will try to maintain backward compatibility in the event of a change, it may not always be possible.

### Python API
The following table summarizes the available wrappers.

[TABLE]
Articulation | High level wrapper for manipulating prims (that have the Root Articulation API applied) and their attributes.
DeformablePrim | High level wrapper for manipulating prims (that have Deformable Schema applied) and their attributes.
GeomPrim | High level wrapper for manipulating geometric prims and their attributes.
Prim | Base wrapper class to manage USD prims.
RigidPrim | High level wrapper for manipulating prims (that have Rigid Body API applied) and their attributes.
XformPrim | High level wrapper for manipulating Xform prims and their attributes.
[/TABLE]

#### Implementation details
The implementation of the wrappers’ properties and methods is done using one or more of the backends listed in the following table. The docstring of such properties and methods will indicate which backends (in order of call) are supported.

[TABLE]
Backend | Description | Performance | Availability
usd | System for authoring, composing, and reading hierarchically organized scene description (see OpenUSD ).
OpenUSD is foundational to NVIDIA Omniverse. | Standard | At any time
usdrt | Omniverse API that mirrors the USD API but reads and writes data to and from Fabric instead of USD (see Fabric Scene Delegate (FSD) and IFabricHierarchy ). | Fast | At any time
fabric | Omniverse library that enables high-performance creation, modification, and access of scene data (see USD, Fabric, and USDRT ). | Fast | At any time
tensor | Interface for interacting with physics simulations in a data-oriented way (see Omni Physics Tensors ). | Fastest | During simulation
[/TABLE]
Note
The selection of a backend (when an implementation supports more than one) will be made according to its availability and according to the listed order. The availability refers to the state of the simulation in which a backend can be used after instantiating a class.
A specific backend can be explicitly requested using the use_backend() context manager.
Warning
If a backend is explicitly requested (using the use_backend() context manager) but is unavailable at the time of the request, resulting in a fallback to another backend, a warning is logged.
Warning
The usdrt and fabric backends require Fabric Scene Delegate (FSD) to be enabled. FSD can be enabled in apps/.kit experience files by setting `app.useFabricSceneDelegate = true`.
Warning
The tensor backend requires the simulation to be running (in play). Calling a property or method implemented only using this backend will raise an `AssertionError` if the simulation is not running. If the implementation supports several backends, and the simulation is not running, the call will fallback to the next listed backend (typically usd).

#### Wrappers
classArticulation(
paths:str|list[str],
*,
resolve_paths:bool=True,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
enable_residual_reports:bool=False,
)Bases: XformPrim
High level wrapper for manipulating prims (that have the Root Articulation API applied) and their attributes.
This class is a wrapper over one or more USD prims in the stage to provide high-level functionality for manipulating articulation properties, and other attributes. The prims are specified using paths that can include regular expressions for matching multiple prims.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

- enable_residual_reports – Whether to enable residual reporting for the articulations.

Raises:

- ValueError – If no prims are found matching the specified path(s).

- AssertionError – If both positions and translations are specified.

Example:

```
>>> import numpy as np
>>> import omni.timeline
>>> from isaacsim.core.experimental.prims import Articulation
>>>
>>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
>>> # where each prim is a reference to the Isaac Sim's Franka Panda USD asset
>>> # - create wrapper over single prim
>>> prim = Articulation("/World/prim_0")
>>> # - create wrapper over multiple prims using regex
>>> prims = Articulation(
... "/World/prim_.*",
... positions=[[x, 0, 0] for x in range(3)],
... reset_xform_op_properties=True,
... enable_residual_reports=True,
... )
>>>
>>> # play the simulation so that the Physics tensor entity becomes valid
>>> omni.timeline.get_timeline_interface().play()
```
apply_visual_materials(
materials:type['VisualMaterial']|list[type['VisualMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply visual materials to the prims, and optionally, to their descendants.
Backends: usd.
Parameters:

- visual_materials – Visual materials to be applied to the prims (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlassMaterial("/World/material/glass")
>>> material.set_input_values("glass_ior", [1.25])
>>> material.set_input_values("depth", [0.001])
>>> material.set_input_values("thin_walled", [False])
>>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
>>>
>>> prims.apply_visual_materials(material)
```

staticensure_api(
prims:list[Usd.Prim],
api:type,
*args,
**kwargs,
)→list[type['UsdAPISchemaBase']]Ensure that all prims have the specified API schema applied.
Backends: usd.
If a prim doesn’t have the API schema, it will be applied. If it already has it, the existing API schema will be returned.
Parameters:

- prims – List of USD Prims to ensure API schema on.

- api – The API schema type to ensure.

- *args – Additional positional arguments passed to API schema when applying it.

- **kwargs – Additional keyword arguments passed to API schema when applying it.

Returns:
List of API schema objects, one for each input prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> from pxr import UsdPhysics
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
>>> # ensure all prims have physics API schema
>>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
>>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
```

get_applied_visual_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['VisualMaterial']|None ]Get the applied visual materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied visual material of the last wrapped prim
>>> prims.get_applied_visual_materials(indices=[2])[0]
<isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
```

get_default_state(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array|None ,wp.array|None ,wp.array|None ,wp.array|None ,wp.array|None ,wp.array|None ,wp.array|None ]Get the default state (root positions, orientations, linear velocities and angular velocities, and DOF positions, velocities and efforts) of the prims.
Backends: usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Seven-elements tuple. 1) The default root positions in the world frame (shape `(N, 3)`). 2) The default root orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). 3) The default root linear velocities (shape `(N, 3)`). 4) The default root angular velocities (shape `(N, 3)`). 5) The default DOF positions (shape `(N, D)`). 6) The default DOF velocities (shape `(N, D)`). 7) The default DOF efforts (shape `(N, D)`). If the default state is not set using the set_default_state() method, `None` is returned.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not initialized.

get_dof_armatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the armatures of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Search for Armature in PhysX docs for more details.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Armatures (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF armatures of all prims
>>> armatures = prims.get_dof_armatures()
>>> armatures.shape
(3, 9)
>>>
>>> # get the DOF armatures of the first and last prims' finger DOFs
>>> armatures = prims.get_dof_armatures(indices=[0, 2], dof_indices=[7, 8])
>>> armatures.shape
(2, 2)
```

get_dof_coriolis_and_centrifugal_compensation_forces(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the Coriolis and centrifugal compensation forces (DOF forces required to counteract Coriolis and centrifugal forces for the given articulation state) of the prims
Backends: tensor.
Search for Coriolis and Centrifugal Compensation Force in PhysX docs for more details.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
The Coriolis and centrifugal compensation forces of the prims. For fixed articulation base shape is `(N, D)`. For non-fixed (floating) articulation base shape is `(N, D + 6)` since the forces acting on the root are also provided.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the coriolis and centrifugal compensation forces (fixed articulation base) of all prims
>>> forces = prims.get_dof_coriolis_and_centrifugal_compensation_forces()
>>> forces.shape
(3, 9)
```

get_dof_drive_model_properties(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array,wp.array]Get the drive model properties of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Three-element tuple. 1) Speed effort gradients (shape `(N, D)`). 2) Maximum actuator velocities (shape `(N, D)`). 3) Velocity-dependent resistances (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF drive model properties of all prims
>>> speed_effort_gradients, maximum_actuator_velocities, velocity_dependent_resistances = prims.get_dof_drive_model_properties()
>>> speed_effort_gradients.shape, maximum_actuator_velocities.shape, velocity_dependent_resistances.shape
((3, 9), (3, 9), (3, 9))
>>>
>>> # get the DOF drive model properties of the first and last prims
>>> speed_effort_gradients, maximum_actuator_velocities, velocity_dependent_resistances = prims.get_dof_drive_model_properties(indices=[0, 2])
>>> speed_effort_gradients.shape, maximum_actuator_velocities.shape, velocity_dependent_resistances.shape
((2, 9), (2, 9), (2, 9))
```

get_dof_drive_types(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→list[list[str]]Get the drive types of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
The drive types. Possible values are `acceleration` or `force` (shape `(N, D)`). If the drive type is not set, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the drive types of the first prim
>>> drive_types = prims.get_dof_drive_types(indices=[0])
>>> print(drive_types)
[['force', 'force', 'force', 'force', 'force', 'force', 'force', 'force', 'none']]
```

get_dof_efforts(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the efforts of the degrees of freedom (DOFs) of the prims.
Backends: tensor.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
DOF efforts (shape `(N, D)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the DOF efforts of all prims
>>> efforts = prims.get_dof_efforts()
>>> efforts.shape
(3, 9)
>>>
>>> # get the DOF efforts of the first and last prims' finger DOFs
>>> efforts = prims.get_dof_efforts(indices=[0, 2], dof_indices=[7, 8])
>>> efforts.shape
(2, 2)
```

get_dof_friction_properties(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array,wp.array]Get the friction properties of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Three-element tuple. 1) Static friction efforts (shape `(N, D)`). 2) Dynamic friction efforts (shape `(N, D)`). 3) Viscous friction coefficients (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF friction properties of all prims
>>> static_frictions, dynamic_frictions, viscous_frictions = prims.get_dof_friction_properties()
>>> static_frictions.shape, dynamic_frictions.shape, viscous_frictions.shape
((3, 9), (3, 9), (3, 9))
>>>
>>> # get the DOF friction properties of the first and last prims
>>> static_frictions, dynamic_frictions, viscous_frictions = prims.get_dof_friction_properties(indices=[0, 2])
>>> static_frictions.shape, dynamic_frictions.shape, viscous_frictions.shape
((2, 9), (2, 9), (2, 9))
```

get_dof_gains(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the implicit Proportional-Derivative (PD) controller’s gains (stiffnesses and dampings) of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Two-elements tuple. 1) Stiffnesses (shape `(N, D)`). 2) Dampings (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF gains of all prims
>>> stiffnesses, dampings = prims.get_dof_gains()
>>> stiffnesses.shape, dampings.shape
((3, 9), (3, 9))
>>>
>>> # get the DOF gains of the first and last prims' finger DOFs
>>> stiffnesses, dampings = prims.get_dof_gains(indices=[0, 2], dof_indices=[7, 8])
>>> stiffnesses.shape, dampings.shape
((2, 2), (2, 2))
```

get_dof_gravity_compensation_forces(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the gravity compensation forces (DOF forces required to counteract gravitational forces for the given articulation pose) of the prims
Backends: tensor.
Search for Gravity Compensation Force in PhysX docs for more details.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
The gravity compensation forces of the prims. For fixed articulation base shape is `(N, D)`. For non-fixed (floating) articulation base shape is `(N, D + 6)` since the forces acting on the root are also provided.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the gravity compensation forces of all prims
>>> forces = prims.get_dof_gravity_compensation_forces()
>>> forces.shape
(3, 9)
>>>
>>> # get the gravity compensation forces of the first and last prims' finger DOFs
>>> forces = prims.get_dof_gravity_compensation_forces(indices=[0, 2], dof_indices=[7, 8])
>>> forces.shape
(2, 2)
```

get_dof_indices(names:str|list[str])→warp.array
Get the indices of one or more degrees of freedom (DOFs) of the prims.
Backends: usd, tensor.
Parameters:
names – Single name or list of names of DOFs to get indices for.

Returns:
Indices of the specified DOF names.

Example:

```
>>> # show all DOF names and their indices
>>> for name in prims.dof_names:
... print(prims.get_dof_indices(name), name)
[0] panda_joint1
[1] panda_joint2
[2] panda_joint3
[3] panda_joint4
[4] panda_joint5
[5] panda_joint6
[6] panda_joint7
[7] panda_finger_joint1
[8] panda_finger_joint2
>>>
>>> # get the indices of Franka Panda's finger DOFs
>>> indices = prims.get_dof_indices(["panda_finger_joint1", "panda_finger_joint2"])
>>> print(indices)
[7 8]
```

get_dof_limits(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the limits of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:

- Lower limits (shape `(N, D)`). 2) Upper limits (shape `(N, D)`).

Return type:
Two-element tuple

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF limits of all prims
>>> lower, upper = prims.get_dof_limits()
>>> lower.shape, upper.shape
((3, 9), (3, 9))
>>>
>>> # get the DOF limits of the first and last prims
>>> lower, upper = prims.get_dof_limits(indices=[0, 2])
>>> lower.shape, upper.shape
((2, 9), (2, 9))
```

get_dof_max_efforts(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the maximum forces applied by the drive of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Maximum forces applied by the drive (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF maximum efforts of all prims
>>> max_efforts = prims.get_dof_max_efforts()
>>> max_efforts.shape
(3, 9)
>>>
>>> # get the DOF maximum efforts of the first and last prims' finger DOFs
>>> max_efforts = prims.get_dof_max_efforts(indices=[0, 2], dof_indices=[7, 8])
>>> max_efforts.shape
(2, 2)
```

get_dof_max_velocities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the maximum velocities of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
Maximum velocities (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF maximum velocities of all prims
>>> max_velocities = prims.get_dof_max_velocities()
>>> max_velocities.shape
(3, 9)
>>>
>>> # get the DOF maximum velocities of the first and last prims' finger DOFs
>>> max_velocities = prims.get_dof_max_velocities(indices=[0, 2], dof_indices=[7, 8])
>>> max_velocities.shape
(2, 2)
```

get_dof_position_targets(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the position targets of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
DOF position targets (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF position targets of all prims
>>> position_targets = prims.get_dof_position_targets()
>>> position_targets.shape
(3, 9)
>>>
>>> # get the DOF position targets of the first and last prims' finger DOFs
>>> position_targets = prims.get_dof_position_targets(indices=[0, 2], dof_indices=[7, 8])
>>> position_targets.shape
(2, 2)
```

get_dof_positions(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the positions of the degrees of freedom (DOFs) of the prims.
Backends: tensor.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
DOF positions (shape `(N, D)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the DOF position of all prims
>>> positions = prims.get_dof_positions()
>>> positions.shape
(3, 9)
>>>
>>> # get the DOF position of the first and last prims' finger DOFs
>>> positions = prims.get_dof_positions(indices=[0, 2], dof_indices=[7, 8])
>>> positions.shape
(2, 2)
```

get_dof_projected_joint_forces(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the degrees of freedom (DOF) projected joint forces of the prims.
Backends: tensor.
This method projects the links incoming joint forces in the motion direction and hence is the active component of the force.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
DOF projected joint forces (shape `(N, D)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the DOF projected joint forces of all prims
>>> forces = prims.get_dof_projected_joint_forces()
>>> forces.shape
(3, 9)
>>>
>>> # get the projected joint forces of the first and last prims' finger DOFs
>>> forces = prims.get_dof_projected_joint_forces(indices=[0, 2], dof_indices=[7, 8])
>>> forces.shape
(2, 2)
```

get_dof_velocities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the velocities of the degrees of freedom (DOFs) of the prims.
Backends: tensor.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
DOF velocities (shape `(N, D)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the DOF velocities of all prims
>>> velocities = prims.get_dof_velocities()
>>> velocities.shape
(3, 9)
>>>
>>> # get the DOF velocity of the first and last prims' finger DOFs
>>> velocities = prims.get_dof_velocities(indices=[0, 2], dof_indices=[7, 8])
>>> velocities.shape
(2, 2)
```

get_dof_velocity_targets(
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the velocity targets of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Returns:
DOF velocity targets (shape `(N, D)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the DOF velocity targets of all prims
>>> velocity_targets = prims.get_dof_velocity_targets()
>>> velocity_targets.shape
(3, 9)
>>>
>>> # get the DOF velocity target of the first and last prims' finger DOFs
>>> velocity_targets = prims.get_dof_velocity_targets(indices=[0, 2], dof_indices=[7, 8])
>>> velocity_targets.shape
(2, 2)
```

get_enabled_self_collisions(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enable state of the self-collisions processing of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the self-collisions processing is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the self-collisions enabled state of all prims
>>> print(prims.get_enabled_self_collisions())
[[False]
[False]
[False]]
```

get_fixed_tendon_dampings(
*,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the dampings of the fixed tendons of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The dampings of the fixed tendons (shape `(N, T)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

get_fixed_tendon_limit_stiffnesses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the limit stiffnesses of the fixed tendons of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The limit stiffnesses of the fixed tendons (shape `(N, T)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

get_fixed_tendon_limits(
*,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the limits of the fixed tendons of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The lower limits of the fixed tendons (shape `(N, T)`). 2) The upper limits of the fixed tendons (shape `(N, T)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

get_fixed_tendon_offsets(
*,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the offsets of the fixed tendons of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The offsets of the fixed tendons (shape `(N, T)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

get_fixed_tendon_rest_lengths(
*,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the rest length of the fixed tendons of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The rest lengths of the fixed tendons (shape `(N, T)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

get_fixed_tendon_stiffnesses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the stiffness of the fixed tendons of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The stiffnesses of the fixed tendons (shape `(N, T)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

get_jacobian_matrices(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the Jacobian matrices of the prims.
Backends: tensor.
Note
The first dimension corresponds to the amount of wrapped prims while the last 3 dimensions are the Jacobian matrix shape. Refer to the jacobian_matrix_shape property for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The Jacobian matrices of the prims (shape `(N, *jacobian_matrix_shape)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the Jacobian matrices of all prims
>>> jacobians = prims.get_jacobian_matrices()
>>> jacobians.shape
(3, 10, 6, 9)
```

get_joint_indices(names:str|list[str])→warp.array
Get the indices of one or more joints of the prims.
Backends: usd, tensor.
Parameters:
names – Single name or list of names of joints to get indices for.

Returns:
Indices of the specified joint names.

Example:

```
>>> # show all joint names and their indices
>>> for name in prims.joint_names:
... print(prims.get_joint_indices(name), name)
[0] panda_joint1
[1] panda_joint2
[2] panda_joint3
[3] panda_joint4
[4] panda_joint5
[5] panda_joint6
[6] panda_joint7
[7] panda_hand_joint
[8] panda_finger_joint1
[9] panda_finger_joint2
>>>
>>> # get the indices of Franka Panda's finger joints
>>> indices = prims.get_joint_indices(["panda_finger_joint1", "panda_finger_joint2"])
>>> print(indices)
[8 9]
```

get_link_coms(
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the center of mass (COM) pose (position and orientation) of the links of the prims.
Backends: tensor.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Returns:
Two-elements tuple. 1) The center of mass positions (shape `(N, L, 3)`). 2) The center of mass orientations (shape `(N, L, 4)`, quaternion `wxyz`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the COM poses of the links of all prims
>>> positions, orientations = prims.get_link_coms()
>>> positions.shape, orientations.shape
((3, 11, 3), (3, 11, 4))
>>>
>>> # get the COM poses of the first and last prims' finger links
>>> positions, orientations = prims.get_link_coms(indices=[0, 2], link_indices=[9, 10])
>>> positions.shape, orientations.shape
((2, 2, 3), (2, 2, 4))
```

get_link_enabled_gravities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the gravity on the links of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Returns:
Boolean flags indicating if the gravity is enabled on the links (shape `(N, L)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the gravity enabled state of the links of all prims
>>> enabled = prims.get_link_enabled_gravities()
>>> enabled.shape
(3, 11)
>>>
>>> # get the gravity enabled state of the first and last prims' finger links
>>> enabled = prims.get_link_enabled_gravities(indices=[0, 2], link_indices=[9, 10])
>>> enabled.shape
(2, 2)
```

get_link_incoming_joint_force(
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the link incoming joint forces and torques to external loads of the prims.
Backends: tensor.
In a kinematic tree, each link has a single incoming joint. This method provides the total 6D force/torque of links incoming joints.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Returns:
Two-elements tuple. 1) The link incoming joint forces (shape `(N, L, 3)`). 2) The link incoming joint torques (shape `(N, L, 3)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the incoming joint forces and torques of the links of all prims
>>> forces, torques = prims.get_link_incoming_joint_force()
>>> forces.shape, torques.shape
((3, 11, 3), (3, 11, 3))
>>>
>>> # get the incoming joint forces and torques of the first and last prims' finger links
>>> forces, torques = prims.get_link_incoming_joint_force(indices=[0, 2], link_indices=[9, 10])
>>> forces.shape, torques.shape
((2, 2, 3), (2, 2, 3))
```

get_link_indices(names:str|list[str])→warp.array
Get the indices of one or more links of the prims.
Backends: usd, tensor.
Parameters:
names – Single name or list of names of links to get indices for.

Returns:
Indices of the specified link names.

Example:

```
>>> # show all link names and their indices
>>> for name in prims.link_names:
... print(prims.get_link_indices(name), name)
[0] panda_link0
[1] panda_link1
[2] panda_link2
[3] panda_link3
[4] panda_link4
[5] panda_link5
[6] panda_link6
[7] panda_link7
[8] panda_hand
[9] panda_leftfinger
[10] panda_rightfinger
>>>
>>> # get the indices of Franka Panda's finger links
>>> indices = prims.get_link_indices(["panda_leftfinger", "panda_rightfinger"])
>>> print(indices)
[ 9 10]
```

get_link_inertias(
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
inverse:bool=False,
)→wp.arrayGet the inertias tensors of the links of the prims.
Backends: tensor.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

- inverse – Whether to return inverse inertia tensors (true) or inertia tensors (false).

Returns:
The inertia tensors or inverse inertia tensors (shape `(N, L, 9)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the inertia tensors of the links of all prims
>>> inertias = prims.get_link_inertias()
>>> inertias.shape
(3, 11, 9)
>>>
>>> # get the inverse inertia tensors of the first and last prims' finger links
>>> inertias = prims.get_link_inertias(indices=[0, 2], link_indices=[9, 10], inverse=True)
>>> inertias.shape
(2, 2, 9)
```

get_link_masses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
inverse:bool=False,
)→wp.arrayGet the masses of the links of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

- inverse – Whether to return inverse masses (true) or masses (false).

Returns:
The link masses (shape `(N, L)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the masses of the links of all prims
>>> masses = prims.get_link_masses()
>>> masses.shape
(3, 11)
>>>
>>> # get the inverse masses of the first and last prims' finger links
>>> inverse_masses = prims.get_link_masses(indices=[0, 2], link_indices=[9, 10], inverse=True)
>>> inverse_masses.shape
(2, 2)
```

get_local_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the root poses (translations and orientations) in the local frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The root translations in the local frame (shape `(N, 3)`). 2) The root orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the local poses of all prims
>>> translations, orientations = prims.get_local_poses()
>>> translations.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the local pose of the first prim
>>> translations, orientations = prims.get_local_poses(indices=[0])
>>> translations.shape, orientations.shape
((1, 3), (1, 4))
```

get_local_scales(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Scales of the prims (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get local scales of all prims
>>> scales = prims.get_local_scales()
>>> scales.shape
(3, 3)
```

get_mass_matrices(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the mass matrices of the prims.
Backends: tensor.
Note
The first dimension corresponds to the amount of wrapped prims while the last 2 dimensions are the mass matrix shape. Refer to the mass_matrix_shape property for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The mass matrices of the prims (shape `(N, *mass_matrix_shape)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the mass matrices of all prims
>>> mass_matrices = prims.get_mass_matrices()
>>> mass_matrices.shape
(3, 9, 9)
```

get_sleep_thresholds(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the sleep thresholds of the prims.
Backends: usd.
Search for Articulations and Sleeping in PhysX docs for more details
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The sleep thresholds (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the sleep thresholds of all prims
>>> thresholds = prims.get_sleep_thresholds()
>>> thresholds.shape
(3, 1)
>>>
>>> # get the sleep threshold of the first and last prims
>>> thresholds = prims.get_sleep_thresholds(indices=[0, 2])
>>> thresholds.shape
(2, 1)
```

get_solver_iteration_counts(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the physics solver iteration counts (position and velocity) of the prims.
Backends: usd.
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:

- Position iteration counts (shape `(N, 1)`).

- Velocity iteration counts (shape `(N, 1)`).

Return type:
Two-element tuple

Example:

```
>>> # get the solver iteration counts of all prims
>>> position_counts, velocity_counts = prims.get_solver_iteration_counts()
>>> position_counts.shape, velocity_counts.shape
((3, 1), (3, 1))
>>>
>>> # get the solver iteration counts of the first and last prims
>>> position_counts, velocity_counts = prims.get_solver_iteration_counts(indices=[0, 2])
>>> position_counts.shape, velocity_counts.shape
((2, 1), (2, 1))
```

get_solver_residual_reports(
*,
indices:int|list|np.ndarray|wp.array|None =None,
report_maximum:bool=True,
)→tuple[wp.array,wp.array]Get the physics solver residuals (position and velocity) of the prims.
Backends: usd.
The solver residual quantifies the convergence of the iterative physics solver. A perfectly converged solution has a residual value of zero. For articulations, the solver residual is computed across all joints that are part of the articulations.
Search for Solver Residual in PhysX docs for more details.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- report_maximum – Whether to report the maximum (true) or the root mean square (false) residual.

Returns:
Two-elements tuple. 1) The solver residuals for position (shape `(N, 1)`). 2) The solver residuals for velocity (shape `(N, 1)`).

Raises:

- AssertionError – Residual reporting is not enabled.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the solver residuals of all prims
>>> position_residuals, velocity_residuals = prims.get_solver_residual_reports()
>>> position_residuals.shape, velocity_residuals.shape
((3, 1), (3, 1))
>>>
>>> # get the solver residuals of the first and last prims
>>> position_residuals, velocity_residuals = prims.get_solver_residual_reports(indices=[0, 2])
>>> position_residuals.shape, velocity_residuals.shape
((2, 1), (2, 1))
```

get_stabilization_thresholds(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the mass-normalized kinetic energy below which the prims may participate in stabilization.
Backends: usd.
Search for Stabilization Threshold in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Stabilization thresholds (shape `(N, 1)`).

Example:

```
>>> # get the stabilization thresholds of all prims
>>> thresholds = prims.get_stabilization_thresholds()
>>> thresholds.shape
(3, 1)
>>>
>>> # get the stabilization threshold of the first and last prims
>>> thresholds = prims.get_stabilization_thresholds(indices=[0, 2])
>>> thresholds.shape
(2, 1)
```

get_velocities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the root velocities (linear and angular) of the prims.
Backends: tensor.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The root linear velocities (shape `(N, 3)`). 2) The root angular velocities (shape `(N, 3)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the velocities of all prims
>>> linear_velocities, angular_velocities = prims.get_velocities()
>>> linear_velocities.shape, angular_velocities.shape
((3, 3), (3, 3))
>>>
>>> # get the velocities of the first prim
>>> linear_velocities, angular_velocities = prims.get_velocities(indices=[0])
>>> linear_velocities.shape, angular_velocities.shape
((1, 3), (1, 3))
```

get_visibilities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating the visibility state (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the visibility states of all prims
>>> visibilities = prims.get_visibilities()
>>> visibilities.list()
[True, True, True]
>>>
>>> # get the visibility states of the first and last prims
>>> visibilities = prims.get_visibilities(indices=[0, 2])
>>> visibilities.list()
[True, True]
```

get_world_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the root poses (positions and orientations) in the world frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The root positions in the world frame (shape `(N, 3)`). 2) The root orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the world poses of all prims
>>> positions, orientations = prims.get_world_poses()
>>> positions.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the world pose of the first prim
>>> positions, orientations = prims.get_world_poses(indices=[0])
>>> positions.shape, orientations.shape
((1, 3), (1, 4))
```

is_physics_tensor_entity_initialized()→bool
Check if the physics tensor entity is initialized.
Returns:
Whether the physics tensor entity is initialized.

is_physics_tensor_entity_valid()→bool
Check if the physics tensor entity is valid.
Returns:
Whether the physics tensor entity is valid.

reset_to_default_state(
*,
warn_on_non_default_state:bool=False,
)→None Reset the prims to the specified default state.
Backends: tensor.
This method applies the default state defined using the set_default_state() method.
Note
This method teleports prims to the specified default state (positions and orientations) and sets the linear and angular velocities and the DOF positions, velocities and efforts immediately.
Warning
This method has no effect when no default state is set. In this case, a warning message is logged if `warn_on_non_default_state` is `True`.
Parameters:
warn_on_non_default_state – Whether to log a warning message when no default state is set.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get default state (no default state set at this point)
>>> prims.get_default_state()
(None, None, None, None, None, None, None)
>>>
>>> # set default state
>>> # - random root positions for each prim
>>> # - same fixed orientation for all prims
>>> # - zero root velocities for all prims
>>> # - random DOF positions for all DOFs
>>> # - zero DOF velocities for all DOFs
>>> # - zero DOF efforts for all DOFs
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_default_state(
... positions=positions,
... orientations=[1.0, 0.0, 0.0, 0.0],
... linear_velocities=np.zeros(3),
... angular_velocities=np.zeros(3),
... dof_positions=np.random.uniform(low=-0.25, high=0.25, size=(3, 9)),
... dof_velocities=np.zeros(9),
... dof_efforts=np.zeros(9),
... )
>>>
>>> # get default state (default state is set)
>>> prims.get_default_state()
(array(shape=(3, 3), dtype=float32),
array(shape=(3, 4), dtype=float32),
array(shape=(3, 3), dtype=float32),
array(shape=(3, 3), dtype=float32),
array(shape=(3, 9), dtype=float32),
array(shape=(3, 9), dtype=float32),
array(shape=(3, 9), dtype=float32))
>>>
>>> # reset prims to default state
>>> prims.reset_to_default_state()
```

reset_xform_op_properties()→None
Reset the transformation operation attributes of the prims to a standard set.
Backends: usd.
It ensures that each prim has only the following transformations in the specified order. Any other transformation operations are removed, so they are not consumed.

- `xformOp:translate` (double precision)

- `xformOp:orient` (double precision)

- `xformOp:scale` (double precision)

Note
This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.
Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # reset transform operations of all prims
>>> prims.reset_xform_op_properties()
>>>
>>> # verify transform operations of the first wrapped prim
>>> prims.prims[0].GetPropertyNames()
[... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
```

staticresolve_paths(
paths:str|list[str],
raise_on_mixed_paths:bool=True,
)→tuple[list[str],list[str]]Resolve paths to prims in the stage to get existing and non-existing paths.
Backends: usd.
Parameters:

- paths – Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.

- raise_on_mixed_paths – Whether to raise an error if resulting paths are mixed or invalid.

Returns:
Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

Raises:
ValueError – If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

set_default_state(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
linear_velocities:list|np.ndarray|wp.array|None =None,
angular_velocities:list|np.ndarray|wp.array|None =None,
dof_positions:float|list|np.ndarray|wp.array|None =None,
dof_velocities:float|list|np.ndarray|wp.array|None =None,
dof_efforts:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the default state (root positions, orientations, linear velocities and angular velocities, and DOF positions, velocities and efforts) of the prims.
Backends: usd.
Hint
Prims can be reset to their default state by calling the reset_to_default_state() method.
Parameters:

- positions – Default root positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Default root orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- linear_velocities – Default root linear velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- angular_velocities – Default root angular velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dof_positions – Default DOF positions (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dof_velocities – Default DOF velocities (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dof_efforts – Default DOF efforts (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

set_dof_armatures(
armatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the armatures of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Search for Armature in PhysX docs for more details.
Parameters:

- armatures – Armatures (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the DOF armatures for all prims
>>> prims.set_dof_armatures([0.5])
>>>
>>> # set the armatures for the first and last prims' finger DOFs
>>> prims.set_dof_armatures([1.5], indices=[0, 2], dof_indices=[7, 8])
```

set_dof_drive_model_properties(
speed_effort_gradients:float|list|np.ndarray|wp.array|None =None,
maximum_actuator_velocities:float|list|np.ndarray|wp.array|None =None,
velocity_dependent_resistances:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the drive model properties of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- speed_effort_gradients – Speed effort gradients (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- maximum_actuator_velocities – Maximum actuator velocities (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- velocity_dependent_resistances – Velocity-dependent resistances (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – If neither speed_effort_gradients, maximum_actuator_velocities, or velocity_dependent_resistances are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the DOF drive model properties for all prims
>>> prims.set_dof_drive_model_properties(
... speed_effort_gradients=[2.0],
... maximum_actuator_velocities=[1.0],
... velocity_dependent_resistances=[1.5],
... )
```

set_dof_drive_types(
types:str|list[list[str]],
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the drive types of the degrees of freedom (DOFs) of the prims.
Backends: usd.
Parameters:

- types – Drive types. Can be a single string or list of strings (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the DOF drive types for all prims to 'acceleration'
>>> # note that dof indices 8 is a mimic joint, it does not have a DOF drive
>>> prims.set_dof_drive_types("acceleration", dof_indices=[0, 1, 2, 3, 4, 5, 6, 7])
>>>
>>> # set the drive types for the all prims' finger DOFs to 'force'
>>> prims.set_dof_drive_types("force", dof_indices=[7])
```

set_dof_efforts(
efforts:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the efforts of the degrees of freedom (DOFs) of the prims.
Backends: tensor.
Note
For effort control, this method must be used. In contrast to the methods that set a target for DOF position/velocity, this method must be called at every update step to ensure effort control.
Hint
For effort control, set zero stiffness and damping, or remove DOF’s drive.
Parameters:

- efforts – Efforts (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random DOF efforts for all prims
>>> prims.set_dof_efforts(np.random.randn(3, 9))
>>>
>>> # set random efforts for the first and last prims' finger DOFs
>>> prims.set_dof_efforts(np.random.randn(2, 2), indices=[0, 2], dof_indices=[7, 8])
```

set_dof_friction_properties(
static_frictions:float|list|np.ndarray|wp.array|None =None,
dynamic_frictions:float|list|np.ndarray|wp.array|None =None,
viscous_frictions:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the friction properties of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Warning
The `static_frictions` must be greater than or equal to the `dynamic_frictions`.
Parameters:

- static_frictions – Static friction efforts (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction efforts (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- viscous_frictions – Viscous friction coefficients (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – If neither static_frictions, dynamic_frictions, or viscous_frictions are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the DOF friction properties for all prims
>>> prims.set_dof_friction_properties(static_frictions=[0.5], dynamic_frictions=[0.2], viscous_frictions=[0.1])
```

set_dof_gains(
stiffnesses:float|list|np.ndarray|wp.array|None =None,
dampings:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
update_default_gains:bool=True,
)→None Set the implicit Proportional-Derivative (PD) controller’s gains (stiffnesses and dampings) of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- stiffnesses – Stiffnesses (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dampings – Dampings (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

- update_default_gains – Whether to update the default gains with the given values.

Raises:

- AssertionError – If neither stiffnesses nor dampings are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the DOF gains for all prims
>>> stiffnesses = np.array([100000, 100000, 100000, 100000, 80000, 80000, 80000, 50000, 50000])
>>> dampings = np.array([8000, 8000, 8000, 8000, 5000, 5000, 5000, 2000, 2000])
>>> prims.set_dof_gains(stiffnesses, dampings)
```

set_dof_limits(
lower:float|list|np.ndarray|wp.array|None =None,
upper:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the limits of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- lower – Lower limits (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- upper – Upper limits (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – If neither lower nor upper limits are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the DOF lower limits for all prims to -0.25
>>> prims.set_dof_limits(lower=[-0.25])
```

set_dof_max_efforts(
max_efforts:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the maximum forces applied by the drive of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- max_efforts – Maximum forces (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the maximum DOF efforts for all prims to 1000
>>> prims.set_dof_max_efforts([1000])
```

set_dof_max_velocities(
max_velocities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the maximum velocities of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Parameters:

- max_velocities – Maximum velocities (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the maximum DOF velocities for all prims to 100
>>> prims.set_dof_max_velocities([100])
```

set_dof_position_targets(
positions:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the position targets of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Note
This method set the desired target position for the DOFs, not the instantaneous positions. It may take several simulation steps to reach the target position (depending on the DOFs’ stiffness and damping values).
Hint
High stiffness causes the DOF to move faster and harder towards the desired target, while high damping softens but also slows the DOF’s movement towards the target.

- For position control, set relatively high stiffness and non-zero low damping (to reduce vibrations).

Parameters:

- positions – Position targets (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random DOF position targets for all prims
>>> prims.set_dof_position_targets(np.random.uniform(low=-0.25, high=0.25, size=(3, 9)))
>>>
>>> # open all the Franka Panda fingers (finger DOFs to 0.04)
>>> prims.set_dof_position_targets([0.04], dof_indices=[7, 8])
```

set_dof_positions(
positions:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the positions of the degrees of freedom (DOFs) of the prims.
Backends: tensor.
Warning
This method teleports prims to the specified DOF positions. Use the set_dof_position_targets() method to control the DOFs’ positions.
Parameters:

- positions – Positions (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random DOF positions for all prims
>>> prims.set_dof_positions(np.random.uniform(low=-0.25, high=0.25, size=(3, 9)))
>>>
>>> # set all the Franka Panda fingers to closed position immediately (finger DOFs to 0.0)
>>> prims.set_dof_positions([0.0], dof_indices=[7, 8])
```

set_dof_velocities(
velocities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the velocities of the degrees of freedom (DOFs) of the prims.
Backends: tensor.
Warning
This method set the specified DOF velocities immediately. Use the set_dof_velocity_targets() method to control the DOFs’ velocities.
Parameters:

- velocities – Velocities (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random DOF velocities for all prims
>>> prims.set_dof_velocities(np.random.uniform(low=-10, high=10, size=(3, 9)))
```

set_dof_velocity_targets(
velocities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the velocity targets of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
Note
This method set the desired target velocity for the DOFs, not the instantaneous velocities. It may take several simulation steps to reach the target velocity (depending on the DOFs’ stiffness and damping values).
Hint
High stiffness causes the DOF to move faster and harder towards the desired target, while high damping softens but also slows the DOF’s movement towards the target.

- For velocity control, set zero stiffness and non-zero damping.

Parameters:

- velocities – Velocity targets (shape `(N, D)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random DOF velocity targets for all prims
>>> prims.set_dof_velocity_targets(np.random.uniform(low=-10, high=10, size=(3, 9)))
```

set_enabled_self_collisions(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the self-collisions processing of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable self-collisions (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # disable the self-collisions for all prims
>>> prims.set_enabled_self_collisions([False])
```

set_fixed_tendon_properties(
*,
stiffnesses:float|list|np.ndarray|wp.array|None =None,
dampings:float|list|np.ndarray|wp.array|None =None,
limit_stiffnesses:float|list|np.ndarray|wp.array|None =None,
lower_limits:float|list|np.ndarray|wp.array|None =None,
upper_limits:float|list|np.ndarray|wp.array|None =None,
rest_lengths:float|list|np.ndarray|wp.array|None =None,
offsets:float|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
tendon_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the fixed tendon properties of the prims.
Backends: tensor.
Search for Fixed Tendons in PhysX docs for more details.
Parameters:

- stiffnesses – The stiffnesses (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dampings – The dampings (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- limit_stiffnesses – The limit stiffnesses (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- lower_limits – The lower limits (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- upper_limits – The upper limits (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- rest_lengths – The rest lengths (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- offsets – The offsets (shape `(N, T)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- tendon_indices – Indices of tendons to process (shape `(T,)`). If not defined, all tendons are processed.

Raises:

- AssertionError – None of the fixed tendon properties are defined.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

set_link_coms(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the center of mass (COM) pose (position and orientation) of the links of the prims.
Backends: tensor.
Parameters:

- positions – Center of mass positions (shape `(N, L, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Center of mass orientations (shape `(N, L, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random COM link positions for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 11, 3))
>>> prims.set_link_coms(positions)
```

set_link_enabled_gravities(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the enabled state of the gravity on the links of the prims.
Backends: tensor, usd.
Parameters:

- enabled – Boolean flags to enable/disable gravity on the links (shape `(N, L)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the gravity of the links for all prims
>>> prims.set_link_enabled_gravities([True])
>>>
>>> # disable the gravity for the first and last prims' finger links
>>> prims.set_link_enabled_gravities([False], indices=[0, 2], link_indices=[9, 10])
```

set_link_inertias(
inertias:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the inertias of the links of the prims.
Backends: tensor.
Parameters:

- inertias – The link inertias (shape `(N, L, 9)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set the inertia tensors of the links for all prims
>>> inertias = np.diag([0.1, 0.1, 0.1]).flatten() # shape: (9,)
>>> prims.set_link_inertias(inertias)
>>>
>>> # set the inertia tensors for the first and last prims' finger links
>>> inertias = np.diag([0.2, 0.2, 0.2]).flatten() # shape: (9,)
>>> prims.set_link_inertias(inertias, indices=[0, 2], link_indices=[9, 10])
```

set_link_masses(
masses:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
link_indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the masses of the links of the prims.
Backends: tensor, usd.
Parameters:

- masses – The link masses (shape `(N, L)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- link_indices – Indices of links to process (shape `(L,)`). If not defined, all links are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the masses of the links for all prims
>>> prims.set_link_masses([10.0])
>>>
>>> # set the masses for the first and last prims' finger links
>>> prims.set_link_masses([0.5], indices=[0, 2], link_indices=[9, 10])
```

set_local_poses(
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the root poses (translations and orientations) in the local frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- translations – Root translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Root orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither translations nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set poses (fixed translations and random orientations) for all prims
>>> translations = [[0, y, 0] for y in range(3)]
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_local_poses(translations, orientations)
```

set_local_scales(
scales:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random positive scales for all prims
>>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
>>> prims.set_local_scales(scales)
```

set_sleep_thresholds(
thresholds:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the sleep thresholds of the prims.
Backends: usd.
Search for Articulations and Sleeping in PhysX docs for more details.
Parameters:

- thresholds – Sleep thresholds (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the sleep thresholds for all prims
>>> prims.set_sleep_thresholds([1e-5])
>>>
>>> # set the sleep thresholds for the first and last prims
>>> prims.set_sleep_thresholds([1.5e-5], indices=[0, 2])
```

set_solver_iteration_counts(
position_counts:int|list|np.ndarray|wp.array|None =None,
velocity_counts:int|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the physics solver iteration counts (position and velocity) of the prims.
Backends: usd.
The solver iteration count determines how accurately contacts, drives, and limits are resolved. Search for Solver Iteration Count in PhysX docs for more details.
Warning
The more iterations, the more accurate the results, at the cost of decreasing simulation performance.
Parameters:

- position_counts – Number of iterations for the position solver (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- velocity_counts – Number of iterations for the velocity solver (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Neither `position_counts` nor `velocity_counts` are defined.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the solver iteration counts (position: 16, velocity: 4) for all prims
>>> prims.set_solver_iteration_counts([16], [4])
```

set_stabilization_thresholds(
thresholds:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the mass-normalized kinetic energy below which the prims may participate in stabilization.
Backends: usd.
Search for Stabilization Threshold in PhysX docs for more details.
Parameters:

- thresholds – Stabilization thresholds to be applied (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the stabilization thresholds for all prims
>>> prims.set_stabilization_thresholds([1e-5])
>>>
>>> # set the stabilization thresholds for the first and last prims
>>> prims.set_stabilization_thresholds([1.5e-5], indices=[0, 2])
```

set_velocities(
linear_velocities:list|np.ndarray|wp.array|None =None,
angular_velocities:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the root velocities (linear and angular) of the prims.
Backends: tensor.
Parameters:

- linear_velocities – Root linear velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- angular_velocities – Root angular velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither linear_velocities nor angular_velocities are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random velocities for all prims
>>> linear_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> angular_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_velocities(linear_velocities, angular_velocities)
```

set_visibilities(
visibilities:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:

- visibilities – Boolean flags to set the visibility state (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # make all prims invisible
>>> prims.set_visibilities([False])
>>>
>>> # make first and last prims invisible
>>> prims.set_visibilities([True]) # restore visibility from previous call
>>> prims.set_visibilities([False], indices=[0, 2])
```

set_world_poses(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the root poses (positions and orientations) in the world frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- positions – Root positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Root orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set poses (fixed positions and random orientations) for all prims
>>> positions = [[0, y, 0] for y in range(3)]
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_world_poses(positions, orientations)
```

switch_dof_control_mode(
mode:str,
*,
indices:int|list|np.ndarray|wp.array|None =None,
dof_indices:int|list|np.ndarray|wp.array|None =None,
)→None Switch the control mode (understood as the gain adjustment) of the degrees of freedom (DOFs) of the prims.
Backends: tensor, usd.
This method sets the implicit Proportional-Derivative (PD) controller’s gains (stiffnesses and dampings) according to the following rules:

[TABLE]
Control mode | Stiffnesses | Dampings
"position" | default stiffnesses | default dampings
"velocity" | 0.0 | default dampings
"effort" | 0.0 | 0.0
[/TABLE]
Parameters:

- mode – Control mode. Supported modes are `"position"`, `"velocity"` and `"effort"`.

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- dof_indices – Indices of DOFs to process (shape `(D,)`). If not defined, all DOFs are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – Invalid control mode.

Example:

```
>>> # switch to 'velocity' control mode for all prims' arm DOFs (except for the fingers)
>>> prims.switch_dof_control_mode("velocity", dof_indices=np.arange(7))
>>>
>>> # switch to 'effort' control mode for all prims' fingers (last 2 DOFs)
>>> prims.switch_dof_control_mode("effort", dof_indices=[7, 8])
```

propertydof_names:list[str]
Degree of freedom (DOFs) names of the prims.
Backends: usd, tensor.
Returns:
Ordered list of DOF names.

Example:

```
>>> prims.dof_names
['panda_joint1', 'panda_joint2', 'panda_joint3',
'panda_joint4', 'panda_joint5', 'panda_joint6',
'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']
```

propertydof_paths:list[list[str]]
Degree of freedom (DOFs) paths of the prims.
Backends: usd, tensor.
Returns:
Ordered list of DOF names.

Example:

```
>>> prims.dof_paths
[['/World/prim_0/panda_link0/panda_joint1', '/World/prim_0/panda_link1/panda_joint2', '/World/prim_0/panda_link2/panda_joint3',
'/World/prim_0/panda_link3/panda_joint4', '/World/prim_0/panda_link4/panda_joint5', '/World/prim_0/panda_link5/panda_joint6',
'/World/prim_0/panda_link6/panda_joint7', '/World/prim_0/panda_hand/panda_finger_joint1', '/World/prim_0/panda_hand/panda_finger_joint2'],
['/World/prim_1/panda_link0/panda_joint1', '/World/prim_1/panda_link1/panda_joint2', '/World/prim_1/panda_link2/panda_joint3',
'/World/prim_1/panda_link3/panda_joint4', '/World/prim_1/panda_link4/panda_joint5', '/World/prim_1/panda_link5/panda_joint6',
'/World/prim_1/panda_link6/panda_joint7', '/World/prim_1/panda_hand/panda_finger_joint1', '/World/prim_1/panda_hand/panda_finger_joint2'],
['/World/prim_2/panda_link0/panda_joint1', '/World/prim_2/panda_link1/panda_joint2', '/World/prim_2/panda_link2/panda_joint3',
'/World/prim_2/panda_link3/panda_joint4', '/World/prim_2/panda_link4/panda_joint5', '/World/prim_2/panda_link5/panda_joint6',
'/World/prim_2/panda_link6/panda_joint7', '/World/prim_2/panda_hand/panda_finger_joint1', '/World/prim_2/panda_hand/panda_finger_joint2']]
```

propertydof_types:list[omni.physics.tensors.DofType]
Degree of freedom (DOFs) types of the prims.
Backends: usd, tensor.
Returns:
Ordered list of DOF types.

Example:

```
>>> prims.dof_types
[<DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
<DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
<DofType.Rotation: 0>, <DofType.Translation: 1>, <DofType.Translation: 1>]
```

propertyis_non_root_articulation_link:bool
Indicate if the wrapped prims are a non-root link in an articulation tree.
Backends: usd.
Warning
Transformation of the poses of non-root links in an articulation tree are not supported.
Returns:
Whether the prims are a non-root link in an articulation tree.

propertyjacobian_matrix_shape:tuple[int,int,int]
Jacobian matrix shape.
Backends: tensor.
The Jacobian matrix shape depends on the number of links, DOFs, and whether the articulation base is fixed (e.g.: robotic manipulators) or not (e.g.: mobile robots).

- Fixed articulation base: `(num_links - 1, 6, num_dofs)`

- Non-fixed (floating) articulation base: `(num_links, 6, num_dofs + 6)`

Each link has 6 values in the Jacobian representing its linear and angular motion along the three coordinate axes. The extra 6 DOFs in the last dimension, for floating bases, correspond to the linear and angular degrees of freedom of the free root link.
Returns:
Shape of Jacobian matrix (for one prim).

Raises:
AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # for the Franka Panda (a robotic manipulator with fixed base):
>>> # - num_links: 11
>>> # - num_dofs: 9
>>> prims.jacobian_matrix_shape
(10, 6, 9)
```

propertyjoint_names:list[str]
Joint names of the prims.
Backends: usd, tensor.
Returns:
Ordered list of joint names.

Example:

```
>>> prims.joint_names
['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4',
'panda_joint5', 'panda_joint6', 'panda_joint7',
'panda_hand_joint', 'panda_finger_joint1', 'panda_finger_joint2']
```

propertyjoint_paths:list[list[str]]
Joint paths of the prims.
Backends: usd, tensor.
Returns:
Ordered list of joint paths.

Example:

```
>>> prims.joint_paths
[['/World/prim_0/panda_link0/panda_joint1', '/World/prim_0/panda_link1/panda_joint2', '/World/prim_0/panda_link2/panda_joint3',
'/World/prim_0/panda_link3/panda_joint4', '/World/prim_0/panda_link4/panda_joint5', '/World/prim_0/panda_link5/panda_joint6',
'/World/prim_0/panda_link6/panda_joint7', '/World/prim_0/panda_link7/panda_hand_joint',
'/World/prim_0/panda_hand/panda_finger_joint1', '/World/prim_0/panda_hand/panda_finger_joint2'],
['/World/prim_1/panda_link0/panda_joint1', '/World/prim_1/panda_link1/panda_joint2', '/World/prim_1/panda_link2/panda_joint3',
'/World/prim_1/panda_link3/panda_joint4', '/World/prim_1/panda_link4/panda_joint5', '/World/prim_1/panda_link5/panda_joint6',
'/World/prim_1/panda_link6/panda_joint7', '/World/prim_1/panda_link7/panda_hand_joint',
'/World/prim_1/panda_hand/panda_finger_joint1', '/World/prim_1/panda_hand/panda_finger_joint2'],
['/World/prim_2/panda_link0/panda_joint1', '/World/prim_2/panda_link1/panda_joint2', '/World/prim_2/panda_link2/panda_joint3',
'/World/prim_2/panda_link3/panda_joint4', '/World/prim_2/panda_link4/panda_joint5', '/World/prim_2/panda_link5/panda_joint6',
'/World/prim_2/panda_link6/panda_joint7', '/World/prim_2/panda_link7/panda_hand_joint',
'/World/prim_2/panda_hand/panda_finger_joint1', '/World/prim_2/panda_hand/panda_finger_joint2']]
```

propertyjoint_types:list[omni.physics.tensors.JointType]
Joint types of the prims.
Backends: tensor.
Returns:
Ordered list of joint types.

Raises:
AssertionError – Physics tensor entity is not initialized.

Example:

```
>>> prims.joint_types
[<JointType.Revolute: 1>, <JointType.Revolute: 1>, <JointType.Revolute: 1>, <JointType.Revolute: 1>,
<JointType.Revolute: 1>, <JointType.Revolute: 1>, <JointType.Revolute: 1>,
<JointType.Fixed: 0>, <JointType.Prismatic: 2>, <JointType.Prismatic: 2>]
```

propertylink_names:list[str]
Link names of the prims.
Backends: usd, tensor.
Returns:
Ordered list of link names.

Example:

```
>>> prims.link_names
['panda_link0', 'panda_link1', 'panda_link2', 'panda_link3',
'panda_link4', 'panda_link5', 'panda_link6', 'panda_link7',
'panda_hand', 'panda_leftfinger', 'panda_rightfinger']
```

propertylink_paths:list[list[str]]
Link paths of the prims.
Backends: usd, tensor.
Returns:
Ordered list of link paths.

Example:

```
>>> prims.link_paths
[['/World/prim_0/panda_link0', '/World/prim_0/panda_link1', '/World/prim_0/panda_link2', '/World/prim_0/panda_link3',
'/World/prim_0/panda_link4', '/World/prim_0/panda_link5', '/World/prim_0/panda_link6', '/World/prim_0/panda_link7',
'/World/prim_0/panda_hand', '/World/prim_0/panda_leftfinger', '/World/prim_0/panda_rightfinger'],
['/World/prim_1/panda_link0', '/World/prim_1/panda_link1', '/World/prim_1/panda_link2', '/World/prim_1/panda_link3',
'/World/prim_1/panda_link4', '/World/prim_1/panda_link5', '/World/prim_1/panda_link6', '/World/prim_1/panda_link7',
'/World/prim_1/panda_hand', '/World/prim_1/panda_leftfinger', '/World/prim_1/panda_rightfinger'],
['/World/prim_2/panda_link0', '/World/prim_2/panda_link1', '/World/prim_2/panda_link2', '/World/prim_2/panda_link3',
'/World/prim_2/panda_link4', '/World/prim_2/panda_link5', '/World/prim_2/panda_link6', '/World/prim_2/panda_link7',
'/World/prim_2/panda_hand', '/World/prim_2/panda_leftfinger', '/World/prim_2/panda_rightfinger']]
```

propertymass_matrix_shape:tuple[int,int]
Mass matrix shape.
Backends: tensor.
The mass matrix shape depends on the number of DOFs, and whether the articulation base is fixed (e.g.: robotic manipulators) or not (e.g.: mobile robots).

- Fixed articulation base: `(num_dofs, num_dofs)`

- Non-fixed (floating) articulation base: `(num_dofs + 6, num_dofs + 6)`

Returns:
Shape of mass matrix (for one prim).

Raises:
AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # for the Franka Panda:
>>> # - num_dofs: 9
>>> prims.mass_matrix_shape
(9, 9)
```

propertynum_dofs:int
Number of degrees of freedom (DOFs) of the prims.
Backends: usd, tensor.
Returns:
Number of DOFs.

Example:

```
>>> prims.num_dofs
9
```

propertynum_fixed_tendons:int
Number of fixed tendons of the prims.
Backends: tensor.
Returns:
Number of fixed tendons.

Raises:
AssertionError – Physics tensor entity is not initialized.

Example:

```
>>> prims.num_fixed_tendons
0
```

propertynum_joints:int
Number of joints of the prims.
Backends: usd, tensor.
Returns:
Number of joints.

Example:

```
>>> prims.num_joints
10
```

propertynum_links:int
Number of links of the prims.
Backends: usd, tensor.
Returns:
Number of links.

Example:

```
>>> prims.num_links
11
```

propertynum_shapes:int
Number of rigid shapes of the prims.
Backends: tensor.
Returns:
Number of rigid shapes.

Raises:
AssertionError – Physics tensor entity is not initialized.

Example:

```
>>> prims.num_shapes
13
```

propertypaths:list[str]
Prim paths in the stage encapsulated by the wrapper.
Returns:
List of prim paths as strings.

Example:

```
>>> prims.paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyprims:list[pxr.Usd.Prim]
USD Prim objects encapsulated by the wrapper.
Returns:
List of USD Prim objects.

Example:

```
>>> prims.prims
[Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
```

propertyvalid:bool
Whether all prims in the wrapper are valid.
Returns:
True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

Example:

```
>>> prims.valid
True
```

classDeformablePrim(
paths:str|list[str],
*,
resolve_paths:bool=False,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
deformable_type:Literal['surface','volume']|None =None,
)Bases: XformPrim
High level wrapper for manipulating prims (that have Deformable Schema applied) and their attributes.
Warning
The deformable prims require the Deformable feature (beta) to be enabled. Deformable feature (beta) can be enabled in apps/.kit experience files by setting `physics.enableDeformableBeta = true` under the `[settings.persistent]` section.
Warning
The current `omni.physics.tensors` implementation does not support `list[str]` as input for deformable body paths. This limitation will be fixed in the future releases. An error message will be logged if a list of paths is provided.
This class is a wrapper over one or more USD prims in the stage to provide high-level functionality for manipulating deformable body properties, and other attributes. The prims are specified using paths that can include regular expressions for matching multiple prims.
Note
If the prims do not already have the Deformable Schema applied to them, it will be applied.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

- deformable_type – Type of deformable body. If not defined, the type will be inferred from the prims.

Raises:

- RuntimeError – If the Deformable feature (beta) is disabled.

- ValueError – If no prims are found matching the specified path(s).

- AssertionError – If both positions and translations are specified.

Example:

```
>>> import numpy as np
>>> import omni.timeline
>>> from isaacsim.core.experimental.prims import DeformablePrim
>>>
>>> # given a USD stage with the tetrahedral mesh prims: /World/prim_0, /World/prim_1, and /World/prim_2
>>> # - create wrapper over single prim (volume deformable body)
>>> prim = DeformablePrim("/World/prim_0", deformable_type="volume")
>>> # - create wrapper over multiple prims using regex (volume deformable body)
>>> prims = DeformablePrim("/World/prim_.*", deformable_type="volume")
>>>
>>> # play the simulation so that the Physics tensor entity becomes valid
>>> omni.timeline.get_timeline_interface().play()
```
apply_physics_materials(
materials:type['PhysicsMaterial']|list[type['PhysicsMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply physics materials to the prims, and optionally, to their descendants.
Backends: usd.
Physics materials define properties like friction and restitution that affect how objects interact during collisions. If no physics material is defined, default values from Physics will be used.
Parameters:

- materials – Physics materials to be applied to the prims (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import VolumeDeformableMaterial
>>>
>>> # create a volume deformable physics material
>>> material = VolumeDeformableMaterial(
... "/World/physics_material/deformable_material",
... static_frictions=[1.1],
... dynamic_frictions=[0.4],
... poissons_ratios=[0.1],
... youngs_moduli=[1000000.0],
... )
>>>
>>> # apply the material to all prims
>>> prims.apply_physics_materials(material) # or [material]
```

apply_visual_materials(
materials:type['VisualMaterial']|list[type['VisualMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply visual materials to the prims, and optionally, to their descendants.
Backends: usd.
Parameters:

- visual_materials – Visual materials to be applied to the prims (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlassMaterial("/World/material/glass")
>>> material.set_input_values("glass_ior", [1.25])
>>> material.set_input_values("depth", [0.001])
>>> material.set_input_values("thin_walled", [False])
>>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
>>>
>>> prims.apply_visual_materials(material)
```

staticensure_api(
prims:list[Usd.Prim],
api:type,
*args,
**kwargs,
)→list[type['UsdAPISchemaBase']]Ensure that all prims have the specified API schema applied.
Backends: usd.
If a prim doesn’t have the API schema, it will be applied. If it already has it, the existing API schema will be returned.
Parameters:

- prims – List of USD Prims to ensure API schema on.

- api – The API schema type to ensure.

- *args – Additional positional arguments passed to API schema when applying it.

- **kwargs – Additional keyword arguments passed to API schema when applying it.

Returns:
List of API schema objects, one for each input prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> from pxr import UsdPhysics
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
>>> # ensure all prims have physics API schema
>>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
>>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
```

get_applied_physics_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['PhysicsMaterial']|None ]Get the applied physics materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied physics materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied material path of the first prim
>>> physics_material = prims.get_applied_physics_materials(indices=[0])[0]
>>> physics_material.paths[0]
'/World/physics_material/deformable_material'
```

get_applied_visual_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['VisualMaterial']|None ]Get the applied visual materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied visual material of the last wrapped prim
>>> prims.get_applied_visual_materials(indices=[2])[0]
<isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
```

get_default_state(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array|None ,wp.array|None ]Get the default state (positions and orientations) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`). 2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the default state is not set using the set_default_state() method, `None` is returned.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

get_element_indices(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array,wp.array]Get the element (triangular faces for surface, tetrahedrons for volume) indices of the simulation, collision and rest meshes of the prims.
Backends: tensor.
Deformable type: surface, volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Three-elements tuple. 1) The simulation mesh’s element indices (shape `(N, num_elements_per_body, num_nodes_per_element)`). 2) The collision mesh’s element indices (shape `(N, num_elements_per_body, num_nodes_per_element)`). 3) The rest mesh’s element indices (shape `(N, num_elements_per_body, num_nodes_per_element)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> simulation_indices, collision_indices, rest_indices = prims.get_element_indices()
>>> print(simulation_indices)
[[[0 1 2 3]]
[[0 1 2 3]]
[[0 1 2 3]]]
>>> print(collision_indices)
[[[0 1 2 3]]
[[0 1 2 3]]
[[0 1 2 3]]]
>>> print(rest_indices)
[[[0 1 2 3]]
[[0 1 2 3]]
[[0 1 2 3]]]
```

get_local_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (translations and orientations) in the local frame of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`). 2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the local poses of all prims
>>> translations, orientations = prims.get_local_poses()
>>> translations.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the local pose of the first prim
>>> translations, orientations = prims.get_local_poses(indices=[0])
>>> translations.shape, orientations.shape
((1, 3), (1, 4))
```

get_local_scales(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Scales of the prims (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get local scales of all prims
>>> scales = prims.get_local_scales()
>>> scales.shape
(3, 3)
```

get_nodal_gradients(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the nodal (tetrahedrons) gradients of the simulation mesh of the prims.
Backends: tensor.
Deformable type: volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The simulation mesh’s nodal gradients (shape `(N, num_elements_per_body)`, where items are 3x3 matrices).

Raises:

- AssertionError – When the deformable body is not a volume.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the nodal gradients of all prims
>>> simulation_gradients = prims.get_nodal_gradients()
>>> simulation_gradients.shape
(3, 1)
>>>
>>> # get the nodal gradients of the first and last prims
>>> simulation_gradients = prims.get_nodal_gradients(indices=[0, 2])
>>> simulation_gradients.shape
(2, 1)
```

get_nodal_kinematic_position_targets(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the nodal (mesh points) kinematic position targets of the simulation mesh of the prims.
Backends: tensor.
Deformable type: volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The simulation mesh’s nodal kinematic position targets (shape `(N, num_nodes_per_body, 3)`). 2) Boolean flags indicating whether the kinematic (true) or dynamic (false) control is enabled (shape `(N, num_nodes_per_body, 1)`).

Raises:

- AssertionError – When the deformable body is not a volume.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the nodal kinematic position targets of all prims
>>> positions, enabled = prims.get_nodal_kinematic_position_targets()
>>> positions.shape, enabled.shape
((3, 4, 3), (3, 4, 1))
>>>
>>> # get the nodal kinematic position targets of the first and last prims
>>> positions, enabled = prims.get_nodal_kinematic_position_targets(indices=[0, 2])
>>> positions.shape, enabled.shape
((2, 4, 3), (2, 4, 1))
```

get_nodal_positions(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array,wp.array]Get the nodal (mesh points) positions of the simulation, collision and rest meshes of the prims.
Backends: tensor.
Deformable type: surface, volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Three-elements tuple. 1) The simulation mesh’s nodal positions (shape `(N, num_nodes_per_body, 3)`). 2) The collision mesh’s nodal positions (shape `(N, num_nodes_per_body, 3)`). 3) The rest mesh’s nodal positions (shape `(N, num_nodes_per_body, 3)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the nodal positions of all prims
>>> simulation_positions, collision_positions, rest_positions = prims.get_nodal_positions()
>>> simulation_positions.shape, collision_positions.shape, rest_positions.shape
((3, 4, 3), (3, 4, 3), (3, 4, 3))
>>>
>>> # get the nodal positions of the first and last prims
>>> simulation_positions, collision_positions, rest_positions = prims.get_nodal_positions(indices=[0, 2])
>>> simulation_positions.shape, collision_positions.shape, rest_positions.shape
((2, 4, 3), (2, 4, 3), (2, 4, 3))
```

get_nodal_rotations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the nodal (tetrahedrons) rotations of the simulation mesh of the prims.
Backends: tensor.
Deformable type: volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The simulation mesh’s nodal rotations (shape `(N, num_nodes_per_body, 3)`).

Raises:

- AssertionError – When the deformable body is not a volume.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the nodal rotations of all prims
>>> simulation_rotations = prims.get_nodal_rotations()
>>> simulation_rotations.shape
(3, 1, 4)
>>>
>>> # get the nodal rotations of the first and last prims
>>> simulation_rotations = prims.get_nodal_rotations(indices=[0, 2])
>>> simulation_rotations.shape
(2, 1, 4)
```

get_nodal_stresses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the nodal (tetrahedrons) stresses of the simulation mesh of the prims.
Backends: tensor.
Deformable type: volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The simulation mesh’s nodal stresses (shape `(N, num_elements_per_body)`, where items are 3x3 matrices).

Raises:

- AssertionError – When the deformable body is not a volume.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the nodal stresses of all prims
>>> simulation_stresses = prims.get_nodal_stresses()
>>> simulation_stresses.shape
(3, 1)
>>>
>>> # get the nodal stresses of the first and last prims
>>> simulation_stresses = prims.get_nodal_stresses(indices=[0, 2])
>>> simulation_stresses.shape
(2, 1)
```

get_nodal_velocities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the nodal (mesh points) velocities of the simulation mesh of the prims.
Backends: tensor.
Deformable type: surface, volume.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The simulation mesh’s nodal velocities (shape `(N, num_nodes_per_body, 3)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the nodal velocities of all prims
>>> simulation_velocities = prims.get_nodal_velocities()
>>> simulation_velocities.shape
(3, 4, 3)
>>>
>>> # get the nodal velocities of the first and last prims
>>> simulation_velocities = prims.get_nodal_velocities(indices=[0, 2])
>>> simulation_velocities.shape
(2, 4, 3)
```

get_visibilities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating the visibility state (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the visibility states of all prims
>>> visibilities = prims.get_visibilities()
>>> visibilities.list()
[True, True, True]
>>>
>>> # get the visibility states of the first and last prims
>>> visibilities = prims.get_visibilities(indices=[0, 2])
>>> visibilities.list()
[True, True]
```

get_world_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (positions and orientations) in the world frame of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`). 2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the world poses of all prims
>>> positions, orientations = prims.get_world_poses()
>>> positions.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the world pose of the first prim
>>> positions, orientations = prims.get_world_poses(indices=[0])
>>> positions.shape, orientations.shape
((1, 3), (1, 4))
```

is_physics_tensor_entity_valid()→bool
Check if the physics tensor entity is valid.
Returns:
Whether the physics tensor entity is valid.

reset_to_default_state(
*,
warn_on_non_default_state:bool=False,
)→None Reset the prims to the specified default state.
Backends: usd, usdrt, fabric.
This method applies the default state defined using the set_default_state() method.
Note
This method teleports prims to the specified default state (positions and orientations).
Warning
This method has no effect on non-root articulation links or when no default state is set. In this case, a warning message is logged if `warn_on_non_default_state` is `True`.
Parameters:
warn_on_non_default_state – Whether to log a warning message when no default state is set.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get default state (no default state set at this point)
>>> prims.get_default_state()
(None, None)
>>>
>>> # set default state
>>> # - random positions for each prim
>>> # - same fixed orientation for all prim
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
>>>
>>> # get default state (default state is set)
>>> prims.get_default_state()
(array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
>>>
>>> # reset prims to default state
>>> prims.reset_to_default_state()
```

reset_xform_op_properties()→None
Reset the transformation operation attributes of the prims to a standard set.
Backends: usd.
It ensures that each prim has only the following transformations in the specified order. Any other transformation operations are removed, so they are not consumed.

- `xformOp:translate` (double precision)

- `xformOp:orient` (double precision)

- `xformOp:scale` (double precision)

Note
This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.
Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # reset transform operations of all prims
>>> prims.reset_xform_op_properties()
>>>
>>> # verify transform operations of the first wrapped prim
>>> prims.prims[0].GetPropertyNames()
[... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
```

staticresolve_paths(
paths:str|list[str],
raise_on_mixed_paths:bool=True,
)→tuple[list[str],list[str]]Resolve paths to prims in the stage to get existing and non-existing paths.
Backends: usd.
Parameters:

- paths – Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.

- raise_on_mixed_paths – Whether to raise an error if resulting paths are mixed or invalid.

Returns:
Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

Raises:
ValueError – If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

set_default_state(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the default state (positions and orientations) of the prims.
Backends: usd.
Hint
Prims can be reset to their default state by calling the reset_to_default_state() method.
Parameters:

- positions – Default positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

set_local_poses(
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (translations and orientations) in the local frame of the prims.
Backends: usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither translations nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_local_poses(translations, orientations)
```

set_local_scales(
scales:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random positive scales for all prims
>>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
>>> prims.set_local_scales(scales)
```

set_nodal_kinematic_position_targets(
positions:list|np.ndarray|wp.array|None =None,
enabled:bool|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the nodal (mesh points) kinematic position targets of the simulation mesh of the prims.
Backends: tensor.
Deformable type: volume.
Parameters:

- positions – Nodal positions (shape `(N, num_nodes_per_body, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- enabled – Boolean flags to enable the kinematic (true) or dynamic (false) control (shape `(N, num_nodes_per_body, 1)`).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – When the deformable body is not a volume.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random nodal kinematic position targets for the first and last prims
>>> positions = np.random.uniform(low=-1, high=1, size=(2, 4, 3))
>>> prims.set_nodal_kinematic_position_targets(positions, enabled=[True], indices=[0, 2])
```

set_nodal_positions(
positions:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the nodal (mesh points) positions of the simulation mesh of the prims.
Backends: tensor.
Deformable type: surface, volume.
Parameters:

- positions – Nodal positions (shape `(N, num_nodes_per_body, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random nodal positions for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 4, 3))
>>> prims.set_nodal_positions(positions)
```

set_nodal_velocities(
velocities:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the nodal (mesh points) velocities of the simulation mesh of the prims.
Backends: tensor.
Deformable type: surface, volume.
Parameters:

- velocities – Nodal velocities (shape `(N, num_nodes_per_body, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random nodal velocities for all prims
>>> velocities = np.random.uniform(low=-1, high=1, size=(3, 4, 3))
>>> prims.set_nodal_velocities(velocities)
```

set_visibilities(
visibilities:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:

- visibilities – Boolean flags to set the visibility state (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # make all prims invisible
>>> prims.set_visibilities([False])
>>>
>>> # make first and last prims invisible
>>> prims.set_visibilities([True]) # restore visibility from previous call
>>> prims.set_visibilities([False], indices=[0, 2])
```

set_world_poses(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (positions and orientations) in the world frame of the prims.
Backends: usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_world_poses(positions, orientations)
```

propertycollision_mesh_paths:list[str]
Collision mesh paths of the prims.
Backends: usd, tensor.
Deformable type: surface, volume.
Returns:
Ordered list of collision mesh paths.

Example:

```
>>> prims.collision_mesh_paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertydeformable_type:Literal['surface','volume']
Type of deformable body.
Backends: usd, tensor.
Deformable type: surface, volume.
Returns:
Type of deformable body.

Example:

```
>>> prims.deformable_type
'volume'
```

propertyis_non_root_articulation_link:bool
Indicate if the wrapped prims are a non-root link in an articulation tree.
Backends: usd.
Warning
Transformation of the poses of non-root links in an articulation tree are not supported.
Returns:
Whether the prims are a non-root link in an articulation tree.

propertynum_elements_per_body:tuple[int,int,int]
Number of elements (triangular faces for surface, tetrahedrons for volume) per body (mesh prim).
Backends: usd, tensor.
Deformable type: surface, volume.
Note
In the current implementation, the rest mesh is limited to the same topology as the simulation mesh. This means that the number of elements per body is the same for the simulation and rest meshes.
Returns:
Tuple of three elements. 1) Number of elements per body (simulation mesh). 2) Number of elements per body (collision mesh). 3) Number of elements per body (rest mesh).

Example:

```
>>> prims.num_elements_per_body
(1, 1, 1)
```

propertynum_nodes_per_body:tuple[int,int,int]
Number of nodes (mesh points) per body (mesh prim).
Backends: usd, tensor.
Deformable type: surface, volume.
Returns:
Tuple of three elements. 1) Number of nodes per body (simulation mesh). 2) Number of nodes per body (collision mesh). 3) Number of nodes per body (rest mesh).

Example:

```
>>> prims.num_nodes_per_body
(4, 4, 4)
```

propertynum_nodes_per_element:int
Number of nodes (mesh points) per element (triangular face for surface, tetrahedron for volume).
Backends: usd, tensor.
Deformable type: surface, volume.
The number of nodes per element is 3 (triangle) for surface and 4 (tetrahedron) for volume.
Returns:
Number of nodes per element.

Example:

```
>>> prims.num_nodes_per_element
4
```

propertypaths:list[str]
Prim paths in the stage encapsulated by the wrapper.
Returns:
List of prim paths as strings.

Example:

```
>>> prims.paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyprims:list[pxr.Usd.Prim]
USD Prim objects encapsulated by the wrapper.
Returns:
List of USD Prim objects.

Example:

```
>>> prims.prims
[Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
```

propertysimulation_mesh_paths:list[str]
Simulation mesh paths of the prims.
Backends: usd, tensor.
Deformable type: surface, volume.
Returns:
Ordered list of simulation mesh paths.

Example:

```
>>> prims.simulation_mesh_paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyvalid:bool
Whether all prims in the wrapper are valid.
Returns:
True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

Example:

```
>>> prims.valid
True
```

classGeomPrim(
paths:str|list[str],
*,
resolve_paths:bool=True,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
apply_collision_apis:bool=False,
)Bases: XformPrim
High level wrapper for manipulating geometric prims and their attributes.
This class is a wrapper over one or more USD geometric prims in the stage to provide high-level functionality for manipulating collision properties, and other attributes. The prims are specified using paths that can include regular expressions for matching multiple prims.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

- apply_collision_apis – Whether to apply collision APIs to the prims during initialization.

Raises:

- ValueError – If no prims are found matching the specified path(s).

- AssertionError – If both positions and translations are specified.

Example:

```
>>> import numpy as np
>>> from isaacsim.core.experimental.prims import GeomPrim
>>>
>>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
>>> # - create wrapper over single prim (with collision APIs enabled)
>>> prim = GeomPrim("/World/prim_0", apply_collision_apis=True)
>>> # - create wrapper over multiple prims using regex (with collision APIs enabled)
>>> prims = GeomPrim("/World/prim_.*", apply_collision_apis=True)
```
apply_collision_apis(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply collision APIs to enable collision detection for prims.
Backends: usd.
This method applies the following APIs to enable collision detection:

- USD: `UsdPhysics.CollisionAPI` and `UsdPhysics.MeshCollisionAPI`

- PhysX: `PhysxSchema.PhysxCollisionAPI`

Note
If a prim in the parent hierarchy has the `RigidBodyAPI` applied, the collider is a part of that body. If there is no body in the parent hierarchy, the collider is considered to be static.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Example:

```
>>> # apply the collision API to all prims
>>> prims.apply_collision_apis()
```

apply_physics_materials(
materials:type['PhysicsMaterial']|list[type['PhysicsMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply physics materials to the prims, and optionally, to their descendants.
Backends: usd.
Physics materials define properties like friction and restitution that affect how objects interact during collisions. If no physics material is defined, default values from Physics will be used.
Parameters:

- materials – Physics materials to be applied to the prims (shape `(N)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import RigidBodyMaterial
>>>
>>> # create a rigid body physics material
>>> material = RigidBodyMaterial(
... "/World/physics_material/aluminum",
... static_frictions=[1.1],
... dynamic_frictions=[0.4],
... restitutions=[0.1],
... )
>>>
>>> # apply the material to all prims
>>> prims.apply_physics_materials(material) # or [material]
```

apply_visual_materials(
materials:type['VisualMaterial']|list[type['VisualMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply visual materials to the prims, and optionally, to their descendants.
Backends: usd.
Parameters:

- visual_materials – Visual materials to be applied to the prims (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlassMaterial("/World/material/glass")
>>> material.set_input_values("glass_ior", [1.25])
>>> material.set_input_values("depth", [0.001])
>>> material.set_input_values("thin_walled", [False])
>>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
>>>
>>> prims.apply_visual_materials(material)
```

staticensure_api(
prims:list[Usd.Prim],
api:type,
*args,
**kwargs,
)→list[type['UsdAPISchemaBase']]Ensure that all prims have the specified API schema applied.
Backends: usd.
If a prim doesn’t have the API schema, it will be applied. If it already has it, the existing API schema will be returned.
Parameters:

- prims – List of USD Prims to ensure API schema on.

- api – The API schema type to ensure.

- *args – Additional positional arguments passed to API schema when applying it.

- **kwargs – Additional keyword arguments passed to API schema when applying it.

Returns:
List of API schema objects, one for each input prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> from pxr import UsdPhysics
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
>>> # ensure all prims have physics API schema
>>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
>>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
```

get_applied_physics_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['PhysicsMaterial']|None ]Get the applied physics materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied physics materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied material path of the first prim
>>> physics_material = prims.get_applied_physics_materials(indices=[0])[0]
>>> physics_material.paths[0]
'/World/physics_material/aluminum'
```

get_applied_visual_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['VisualMaterial']|None ]Get the applied visual materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied visual material of the last wrapped prim
>>> prims.get_applied_visual_materials(indices=[2])[0]
<isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
```

get_collision_approximations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[str]Get the collision approximation types for mesh collision detection.
Backends: usd.
The collision approximation type determines how the mesh geometry is approximated for collision detection. Different approximations offer trade-offs between accuracy and performance.

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation.
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders.
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider.
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider.
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh.
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider.
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape.
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders.
[/TABLE]
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of collision approximation types (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the collision approximation of all prims after setting them to different types
>>> prims.set_collision_approximations(["convexDecomposition", "convexHull", "boundingSphere"])
>>> prims.get_collision_approximations()
['convexDecomposition', 'convexHull', 'boundingSphere']
```

get_default_state(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array|None ,wp.array|None ]Get the default state (positions and orientations) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`). 2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the default state is not set using the set_default_state() method, `None` is returned.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

get_enabled_collisions(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the collision API of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the collision API is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the collision enabled state of all prims after disabling it for the second prim
>>> prims.set_enabled_collisions([False], indices=[1])
>>> print(prims.get_enabled_collisions())
[[ True]
[False]
[ True]]
```

get_local_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (translations and orientations) in the local frame of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`). 2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the local poses of all prims
>>> translations, orientations = prims.get_local_poses()
>>> translations.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the local pose of the first prim
>>> translations, orientations = prims.get_local_poses(indices=[0])
>>> translations.shape, orientations.shape
((1, 3), (1, 4))
```

get_local_scales(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Scales of the prims (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get local scales of all prims
>>> scales = prims.get_local_scales()
>>> scales.shape
(3, 3)
```

get_offsets(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the contact and rest offsets for collision detection between prims.
Backends: usd.
Shapes whose distance is less than the sum of their contact offset values will generate contacts. The rest offset determines the distance at which two shapes will come to rest. Search for Advanced Collision Detection in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The contact offsets (shape `(N, 1)`). 2) The rest offsets (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the offsets of all prims
>>> contact_offsets, rest_offsets = prims.get_offsets()
>>> contact_offsets.shape, rest_offsets.shape
((3, 1), (3, 1))
>>>
>>> # get the offsets of the second prim
>>> contact_offsets, rest_offsets = prims.get_offsets(indices=[1])
>>> contact_offsets.shape, rest_offsets.shape
((1, 1), (1, 1))
```

get_torsional_patch_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
minimum:bool=False,
)→wp.arrayGet the torsional patch radii of the contact patches used to apply torsional frictions.
Backends: usd.
Search for Torsional Patch Radius in PhysX docs for more details.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- minimum – Whether to get the minimum torsional patch radii instead of the standard ones.

Returns:
The (minimum) torsional patch radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the torsional patch radii of all prims
>>> radii = prims.get_torsional_patch_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the torsional patch radii of second prim
>>> radii = prims.get_torsional_patch_radii(indices=[1])
>>> radii.shape
(1, 1)
```

get_visibilities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating the visibility state (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the visibility states of all prims
>>> visibilities = prims.get_visibilities()
>>> visibilities.list()
[True, True, True]
>>>
>>> # get the visibility states of the first and last prims
>>> visibilities = prims.get_visibilities(indices=[0, 2])
>>> visibilities.list()
[True, True]
```

get_world_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (positions and orientations) in the world frame of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`). 2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the world poses of all prims
>>> positions, orientations = prims.get_world_poses()
>>> positions.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the world pose of the first prim
>>> positions, orientations = prims.get_world_poses(indices=[0])
>>> positions.shape, orientations.shape
((1, 3), (1, 4))
```

reset_to_default_state(
*,
warn_on_non_default_state:bool=False,
)→None Reset the prims to the specified default state.
Backends: usd, usdrt, fabric.
This method applies the default state defined using the set_default_state() method.
Note
This method teleports prims to the specified default state (positions and orientations).
Warning
This method has no effect on non-root articulation links or when no default state is set. In this case, a warning message is logged if `warn_on_non_default_state` is `True`.
Parameters:
warn_on_non_default_state – Whether to log a warning message when no default state is set.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get default state (no default state set at this point)
>>> prims.get_default_state()
(None, None)
>>>
>>> # set default state
>>> # - random positions for each prim
>>> # - same fixed orientation for all prim
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
>>>
>>> # get default state (default state is set)
>>> prims.get_default_state()
(array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
>>>
>>> # reset prims to default state
>>> prims.reset_to_default_state()
```

reset_xform_op_properties()→None
Reset the transformation operation attributes of the prims to a standard set.
Backends: usd.
It ensures that each prim has only the following transformations in the specified order. Any other transformation operations are removed, so they are not consumed.

- `xformOp:translate` (double precision)

- `xformOp:orient` (double precision)

- `xformOp:scale` (double precision)

Note
This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.
Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # reset transform operations of all prims
>>> prims.reset_xform_op_properties()
>>>
>>> # verify transform operations of the first wrapped prim
>>> prims.prims[0].GetPropertyNames()
[... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
```

staticresolve_paths(
paths:str|list[str],
raise_on_mixed_paths:bool=True,
)→tuple[list[str],list[str]]Resolve paths to prims in the stage to get existing and non-existing paths.
Backends: usd.
Parameters:

- paths – Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.

- raise_on_mixed_paths – Whether to raise an error if resulting paths are mixed or invalid.

Returns:
Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

Raises:
ValueError – If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

set_collision_approximations(
approximations:str|list[str],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the collision approximation types for mesh collision detection.
Backends: usd.
The collision approximation type determines how the mesh geometry is approximated for collision detection. Different approximations offer trade-offs between accuracy and performance.

[TABLE]
Approximation | Full name | Description
"none" | Triangle Mesh | The mesh geometry is used directly as a collider without any approximation.
"convexDecomposition" | Convex Decomposition | A convex mesh decomposition is performed. This results in a set of convex mesh colliders.
"convexHull" | Convex Hull | A convex hull of the mesh is generated and used as the collider.
"boundingSphere" | Bounding Sphere | A bounding sphere is computed around the mesh and used as a collider.
"boundingCube" | Bounding Cube | An optimally fitting box collider is computed around the mesh.
"meshSimplification" | Mesh Simplification | A mesh simplification step is performed, resulting in a simplified triangle mesh collider.
"sdf" | SDF Mesh | SDF (Signed-Distance-Field) use high-detail triangle meshes as collision shape.
"sphereFill" | Sphere Approximation | A sphere mesh decomposition is performed. This results in a set of sphere colliders.
[/TABLE]
Parameters:

- approximations – Approximation types to use for collision detection (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the collision approximations for all prims to 'convexDecomposition'
>>> prims.set_collision_approximations(["convexDecomposition"])
```

set_default_state(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the default state (positions and orientations) of the prims.
Backends: usd.
Hint
Prims can be reset to their default state by calling the reset_to_default_state() method.
Parameters:

- positions – Default positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

set_enabled_collisions(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the collision API of the prims.
Backends: usd.
When disabled, the prims will not participate in collision detection.
Parameters:

- enabled – Boolean flags to enable/disable collision APIs (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the collision API for all prims
>>> prims.set_enabled_collisions([True])
>>>
>>> # disable the collision API for the first and last prims
>>> prims.set_enabled_collisions([False], indices=[0, 2])
```

set_local_poses(
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (translations and orientations) in the local frame of the prims.
Backends: usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither translations nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_local_poses(translations, orientations)
```

set_local_scales(
scales:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random positive scales for all prims
>>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
>>> prims.set_local_scales(scales)
```

set_offsets(
contact_offsets:float|list|np.ndarray|wp.array=None,
rest_offsets:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the contact and rest offsets for collision detection between prims.
Backends: usd.
Shapes whose distance is less than the sum of their contact offset values will generate contacts. The rest offset determines the distance at which two shapes will come to rest. Search for Advanced Collision Detection in PhysX docs for more details.
Warning
The contact offset must be positive and greater than the rest offset.
Parameters:

- contact_offsets – Contact offsets of the collision shapes (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- rest_offsets – Rest offsets of the collision shapes (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither contact_offsets nor rest_offsets are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same offsets (contact: 0.005, rest: 0.001) for all prims
>>> prims.set_offsets(contact_offsets=[0.005], rest_offsets=[0.001])
>>>
>>> # set only the rest offsets for the second prim
>>> prims.set_offsets(rest_offsets=[0.002], indices=[1])
```

set_torsional_patch_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
minimum:bool=False,
)→None Set the torsional patch radii of the contact patches used to apply torsional frictions.
Backends: usd.
Search for Torsional Patch Radius in PhysX docs for more details.
Parameters:

- radii – Torsional patch radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- minimum – Whether to set the minimum torsional patch radii instead of the standard ones.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the torsional patch radii for all prims
>>> prims.set_torsional_patch_radii([0.1])
>>>
>>> # set the torsional patch radii for the first and last prims
>>> prims.set_torsional_patch_radii([0.2], indices=np.array([0, 2]))
```

set_visibilities(
visibilities:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:

- visibilities – Boolean flags to set the visibility state (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # make all prims invisible
>>> prims.set_visibilities([False])
>>>
>>> # make first and last prims invisible
>>> prims.set_visibilities([True]) # restore visibility from previous call
>>> prims.set_visibilities([False], indices=[0, 2])
```

set_world_poses(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (positions and orientations) in the world frame of the prims.
Backends: usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_world_poses(positions, orientations)
```

propertygeoms:list[pxr.UsdGeom.Gprim]
USD geometric primitives encapsulated by the wrapper.
Returns:
List of USD geometric primitives.

Example:

```
>>> prims.geoms
[UsdGeom.Gprim(Usd.Prim(</World/prim_0>)),
UsdGeom.Gprim(Usd.Prim(</World/prim_1>)),
UsdGeom.Gprim(Usd.Prim(</World/prim_2>))]
```

propertyis_non_root_articulation_link:bool
Indicate if the wrapped prims are a non-root link in an articulation tree.
Backends: usd.
Warning
Transformation of the poses of non-root links in an articulation tree are not supported.
Returns:
Whether the prims are a non-root link in an articulation tree.

propertypaths:list[str]
Prim paths in the stage encapsulated by the wrapper.
Returns:
List of prim paths as strings.

Example:

```
>>> prims.paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyprims:list[pxr.Usd.Prim]
USD Prim objects encapsulated by the wrapper.
Returns:
List of USD Prim objects.

Example:

```
>>> prims.prims
[Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
```

propertyvalid:bool
Whether all prims in the wrapper are valid.
Returns:
True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

Example:

```
>>> prims.valid
True
```

classPrim(paths:str|list[str], *, resolve_paths:bool=True)
Bases: `ABC`
Base wrapper class to manage USD prims.
Creates a wrapper over one or more USD prims in the stage. The prims are specified using paths that can include regular expressions for matching multiple prims.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

Raises:
ValueError – If no prims are found matching the specified path(s).

Example:

```
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
>>> # - create wrapper over single prim
>>> prim = Prim("/World/prim_0")
>>> # - create wrapper over multiple prims using regex
>>> prims = Prim("/World/prim_.*")
```
__len__()→int
Get the number of prims encapsulated by the wrapper.
Returns:
Number of prims in the wrapper.

Example:

```
>>> len(prims)
3
```

staticensure_api(
prims:list[Usd.Prim],
api:type,
*args,
**kwargs,
)→list[type['UsdAPISchemaBase']]Ensure that all prims have the specified API schema applied.
Backends: usd.
If a prim doesn’t have the API schema, it will be applied. If it already has it, the existing API schema will be returned.
Parameters:

- prims – List of USD Prims to ensure API schema on.

- api – The API schema type to ensure.

- *args – Additional positional arguments passed to API schema when applying it.

- **kwargs – Additional keyword arguments passed to API schema when applying it.

Returns:
List of API schema objects, one for each input prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> from pxr import UsdPhysics
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
>>> # ensure all prims have physics API schema
>>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
>>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
```

staticresolve_paths(
paths:str|list[str],
raise_on_mixed_paths:bool=True,
)→tuple[list[str],list[str]]Resolve paths to prims in the stage to get existing and non-existing paths.
Backends: usd.
Parameters:

- paths – Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.

- raise_on_mixed_paths – Whether to raise an error if resulting paths are mixed or invalid.

Returns:
Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

Raises:
ValueError – If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

propertypaths:list[str]
Prim paths in the stage encapsulated by the wrapper.
Returns:
List of prim paths as strings.

Example:

```
>>> prims.paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyprims:list[pxr.Usd.Prim]
USD Prim objects encapsulated by the wrapper.
Returns:
List of USD Prim objects.

Example:

```
>>> prims.prims
[Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
```

propertyvalid:bool
Whether all prims in the wrapper are valid.
Returns:
True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

Example:

```
>>> prims.valid
True
```

classRigidPrim(
paths:str|list[str],
*,
resolve_paths:bool=True,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
masses:float|list|np.ndarray|wp.array|None =None,
densities:float|list|np.ndarray|wp.array|None =None,
)Bases: XformPrim
High level wrapper for manipulating prims (that have Rigid Body API applied) and their attributes.
This class is a wrapper over one or more USD prims in the stage to provide high-level functionality for manipulating rigid body properties, and other attributes. The prims are specified using paths that can include regular expressions for matching multiple prims.
Note
If the prims do not already have the Rigid Body API applied to them, it will be applied.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

- masses – Masses of the rigid bodies (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- densities – Densities of the rigid bodies (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

Raises:

- ValueError – If no prims are found matching the specified path(s).

- AssertionError – If both positions and translations are specified.

Example:

```
>>> import numpy as np
>>> import omni.timeline
>>> from isaacsim.core.experimental.prims import RigidPrim
>>>
>>> # given a USD stage with the prims: /World/prim_0, /World/prim_1, and /World/prim_2
>>> # - create wrapper over single prim (with masses)
>>> prim = RigidPrim("/World/prim_0", masses=[1.0])
>>> # - create wrapper over multiple prims using regex (with masses)
>>> prims = RigidPrim("/World/prim_.*", masses=[1.0])
>>>
>>> # play the simulation so that the Physics tensor entity becomes valid
>>> omni.timeline.get_timeline_interface().play()
```
apply_forces(
forces:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
local_frame:bool=False,
)→None Apply forces at the link transforms on the prims.
Backends: tensor.
Parameters:

- forces – Forces to apply (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- local_frame – Whether to apply forces in the local frame (true) or world frame (false).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # apply an external force to all prims
>>> forces = np.random.uniform(low=0, high=100, size=(3, 3))
>>> prims.apply_forces(forces)
```

apply_forces_and_torques_at_pos(
forces:list|np.ndarray|wp.array|None =None,
torques:list|np.ndarray|wp.array|None =None,
*,
positions:list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
local_frame:bool=False,
)→None Apply forces and torques at specified positions on the prims.
Backends: tensor.
Parameters:

- forces – Forces to apply (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- torques – Torques to apply (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions to apply forces and torques at (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- local_frame – Whether to apply forces and torques in the local frame (true) or world frame (false).

Raises:

- AssertionError – If neither forces nor torques are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # apply an external force and torque to all prims at a specific position
>>> forces = np.random.uniform(low=0, high=100, size=(3, 3))
>>> torques = np.random.uniform(low=0, high=100, size=(3, 3))
>>> prims.apply_forces_and_torques_at_pos(forces, torques, positions=[0.1, 0.0, 0.0])
```

apply_visual_materials(
materials:type['VisualMaterial']|list[type['VisualMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply visual materials to the prims, and optionally, to their descendants.
Backends: usd.
Parameters:

- visual_materials – Visual materials to be applied to the prims (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlassMaterial("/World/material/glass")
>>> material.set_input_values("glass_ior", [1.25])
>>> material.set_input_values("depth", [0.001])
>>> material.set_input_values("thin_walled", [False])
>>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
>>>
>>> prims.apply_visual_materials(material)
```

staticensure_api(
prims:list[Usd.Prim],
api:type,
*args,
**kwargs,
)→list[type['UsdAPISchemaBase']]Ensure that all prims have the specified API schema applied.
Backends: usd.
If a prim doesn’t have the API schema, it will be applied. If it already has it, the existing API schema will be returned.
Parameters:

- prims – List of USD Prims to ensure API schema on.

- api – The API schema type to ensure.

- *args – Additional positional arguments passed to API schema when applying it.

- **kwargs – Additional keyword arguments passed to API schema when applying it.

Returns:
List of API schema objects, one for each input prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> from pxr import UsdPhysics
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
>>> # ensure all prims have physics API schema
>>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
>>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
```

get_applied_visual_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['VisualMaterial']|None ]Get the applied visual materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied visual material of the last wrapped prim
>>> prims.get_applied_visual_materials(indices=[2])[0]
<isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
```

get_coms(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the center of mass (COM) pose (position and orientation) of the prims.
Backends: tensor.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The center of mass positions (shape `(N, 3)`). 2) The center of mass orientations (shape `(N, 4)`, quaternion `wxyz`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the COM poses of all prims
>>> positions, orientations = prims.get_coms()
>>> positions.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the COM poses of the first and last prims
>>> positions, orientations = prims.get_coms(indices=[0, 2])
>>> positions.shape, orientations.shape
((2, 3), (2, 4))
```

get_default_state(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array|None ,wp.array|None ,wp.array|None ,wp.array|None ]Get the default state (positions, orientations, linear velocities and angular velocities) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Four-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`). 2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). 3) The default linear velocities (shape `(N, 3)`). 4) The default angular velocities (shape `(N, 3)`). If the default state is not set using the set_default_state() method, `None` is returned.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

get_densities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the densities of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The densities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the densities of all prims
>>> densities = prims.get_densities()
>>> densities.shape
(3, 1)
>>>
>>> # get densities of the first and last prims
>>> densities = prims.get_densities(indices=[0, 2])
>>> densities.shape
(2, 1)
```

get_enabled_gravities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the gravity on the prims.
Backends: tensor, usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the gravity is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the gravity enabled state of all prims after disabling it for the second prim
>>> prims.set_enabled_gravities([False], indices=[1])
>>> print(prims.get_enabled_gravities())
[[ True]
[False]
[ True]]
```

get_enabled_rigid_bodies(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the rigid body dynamics of the prims.
Backends: tensor, usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the rigid body dynamics is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the rigid body dynamics enabled state of all prims
>>> print(prims.get_enabled_rigid_bodies())
[[ True]
[ True]
[ True]]
```

get_inertias(
*,
indices:int|list|np.ndarray|wp.array|None =None,
inverse:bool=False,
)→wp.arrayGet the inertia tensors of the prims.
Backends: tensor.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- inverse – Whether to return inverse inertia tensors (true) or inertia tensors (false).

Returns:
The inertia tensors or inverse inertia tensors (shape `(N, 9)`).

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # get the inertia tensors of all prims
>>> inertias = prims.get_inertias()
>>> inertias.shape
(3, 9)
>>>
>>> # get the inverse inertia tensors of the first and last prims
>>> inertias = prims.get_inertias(indices=[0, 2], inverse=True)
>>> inertias.shape
(2, 9)
```

get_local_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (translations and orientations) in the local frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`). 2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the local poses of all prims
>>> translations, orientations = prims.get_local_poses()
>>> translations.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the local pose of the first prim
>>> translations, orientations = prims.get_local_poses(indices=[0])
>>> translations.shape, orientations.shape
((1, 3), (1, 4))
```

get_local_scales(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Scales of the prims (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get local scales of all prims
>>> scales = prims.get_local_scales()
>>> scales.shape
(3, 3)
```

get_masses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
inverse:bool=False,
)→wp.arrayGet the masses of the prims.
Backends: tensor, usd.
Parameters:

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

- inverse – Whether to return inverse masses (true) or masses (false).

Returns:
The masses or inverse masses (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the masses of all prims
>>> masses = prims.get_masses()
>>> masses.shape
(3, 1)
>>>
>>> # get the masses of the first and last prims
>>> masses = prims.get_masses(indices=[0, 2])
>>> masses.shape
(2, 1)
```

get_sleep_thresholds(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the sleep thresholds of the prims.
Backends: usd.
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The sleep thresholds (shape `(N, 1)`).

Example:

```
>>> # get the sleep thresholds of all prims
>>> thresholds = prims.get_sleep_thresholds()
>>> thresholds.shape
(3, 1)
>>>
>>> # get the sleep threshold of the first and last prims
>>> thresholds = prims.get_sleep_thresholds(indices=[0, 2])
>>> thresholds.shape
(2, 1)
```

get_velocities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the velocities (linear and angular) of the prims.
Backends: tensor, usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The linear velocities (shape `(N, 3)`). 2) The angular velocities (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the velocities of all prims
>>> linear_velocities, angular_velocities = prims.get_velocities()
>>> linear_velocities.shape, angular_velocities.shape
((3, 3), (3, 3))
>>>
>>> # get the velocities of the first prim
>>> linear_velocities, angular_velocities = prims.get_velocities(indices=[0])
>>> linear_velocities.shape, angular_velocities.shape
((1, 3), (1, 3))
```

get_visibilities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating the visibility state (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the visibility states of all prims
>>> visibilities = prims.get_visibilities()
>>> visibilities.list()
[True, True, True]
>>>
>>> # get the visibility states of the first and last prims
>>> visibilities = prims.get_visibilities(indices=[0, 2])
>>> visibilities.list()
[True, True]
```

get_world_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (positions and orientations) in the world frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`). 2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the world poses of all prims
>>> positions, orientations = prims.get_world_poses()
>>> positions.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the world pose of the first prim
>>> positions, orientations = prims.get_world_poses(indices=[0])
>>> positions.shape, orientations.shape
((1, 3), (1, 4))
```

is_physics_tensor_entity_valid()→bool
Check if the physics tensor entity is valid.
Returns:
Whether the physics tensor entity is valid.

reset_to_default_state(
*,
warn_on_non_default_state:bool=False,
)→None Reset the prims to the specified default state.
Backends: tensor, usd.
This method applies the default state defined using the set_default_state() method.
Note
This method teleports prims to the specified default state (positions and orientations) and sets the linear and angular velocities immediately.
Warning
This method has no effect on non-root articulation links or when no default state is set. In this case, a warning message is logged if `warn_on_non_default_state` is `True`.
Parameters:
warn_on_non_default_state – Whether to log a warning message when no default state is set.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get default state (no default state set at this point)
>>> prims.get_default_state()
(None, None, None, None)
>>>
>>> # set default state
>>> # - random positions for each prim
>>> # - same fixed orientation for all prims
>>> # - zero velocities for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_default_state(
... positions=positions,
... orientations=[1.0, 0.0, 0.0, 0.0],
... linear_velocities=np.zeros(3),
... angular_velocities=np.zeros(3),
... )
>>>
>>> # get default state (default state is set)
>>> prims.get_default_state()
(array(shape=(3, 3), dtype=float32),
array(shape=(3, 4), dtype=float32),
array(shape=(3, 3), dtype=float32),
array(shape=(3, 3), dtype=float32))
>>>
>>> # reset prims to default state
>>> prims.reset_to_default_state()
```

reset_xform_op_properties()→None
Reset the transformation operation attributes of the prims to a standard set.
Backends: usd.
It ensures that each prim has only the following transformations in the specified order. Any other transformation operations are removed, so they are not consumed.

- `xformOp:translate` (double precision)

- `xformOp:orient` (double precision)

- `xformOp:scale` (double precision)

Note
This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.
Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # reset transform operations of all prims
>>> prims.reset_xform_op_properties()
>>>
>>> # verify transform operations of the first wrapped prim
>>> prims.prims[0].GetPropertyNames()
[... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
```

staticresolve_paths(
paths:str|list[str],
raise_on_mixed_paths:bool=True,
)→tuple[list[str],list[str]]Resolve paths to prims in the stage to get existing and non-existing paths.
Backends: usd.
Parameters:

- paths – Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.

- raise_on_mixed_paths – Whether to raise an error if resulting paths are mixed or invalid.

Returns:
Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

Raises:
ValueError – If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

set_coms(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the center of mass (COM) pose (position and orientation) of the prims.
Backends: tensor.
Parameters:

- positions – Center of mass positions (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Center of mass orientations (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set random COM poses for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_coms(positions, orientations)
```

set_default_state(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
linear_velocities:list|np.ndarray|wp.array|None =None,
angular_velocities:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the default state (positions, orientations, linear velocities and angular velocities) of the prims.
Backends: usd.
Hint
Prims can be reset to their default state by calling the reset_to_default_state() method.
Parameters:

- positions – Default positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- linear_velocities – Default linear velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- angular_velocities – Default angular velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

set_densities(
densities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the densities of the prims.
Backends: usd.
Parameters:

- densities – Densities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the densities for all prims
>>> prims.set_densities([100])
>>>
>>> # set the densities for the first and last prims
>>> prims.set_densities([200], indices=[0, 2])
```

set_enabled_gravities(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the gravity on the prims.
Backends: tensor, usd.
When disabled, the prims will not be affected by the gravity.
Parameters:

- enabled – Boolean flags to enable/disable gravity (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the gravity for all prims
>>> prims.set_enabled_gravities([True])
>>>
>>> # disable the gravity for the first and last prims
>>> prims.set_enabled_gravities([False], indices=[0, 2])
```

set_enabled_rigid_bodies(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the rigid body dynamics of the prims.
Backends: tensor, usd.
When disabled, the prims will not participate in the physics simulation.
Parameters:

- enabled – Boolean flags to enable/disable rigid body dynamics (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the rigid body dynamics for all prims
>>> prims.set_enabled_rigid_bodies([True])
```

set_inertias(
inertias:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the inertia tensors of the prims.
Backends: tensor.
Parameters:

- inertias – Inertia tensors (shape `(N, 9)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Physics tensor entity is not valid.

Example:

```
>>> # set the inertia tensors for all prims
>>> inertias = np.diag([0.1, 0.1, 0.1]).flatten() # shape: (9,)
>>> prims.set_inertias(inertias)
>>>
>>> # set the inertia tensors for the first and last prims
>>> inertias = np.diag([0.2, 0.2, 0.2]).flatten() # shape: (9,)
>>> prims.set_inertias(inertias, indices=[0, 2])
```

set_local_poses(
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (translations and orientations) in the local frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither translations nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_local_poses(translations, orientations)
```

set_local_scales(
scales:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random positive scales for all prims
>>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
>>> prims.set_local_scales(scales)
```

set_masses(
masses:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the masses of the prims.
Backends: tensor, usd.
Parameters:

- masses – Masses (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the masses for all prims
>>> prims.set_masses([10.0])
>>>
>>> # set the masses for the first and last prims
>>> prims.set_masses([20.0], indices=[0, 2])
```

set_sleep_thresholds(
thresholds:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the sleep thresholds of the prims.
Backends: usd.
Search for Rigid Body Dynamics > Sleeping in PhysX docs for more details.
Parameters:

- thresholds – Sleep thresholds (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the sleep thresholds for all prims
>>> prims.set_sleep_thresholds([1e-5])
>>>
>>> # set the sleep thresholds for the first and last prims
>>> prims.set_sleep_thresholds([1.5e-5], indices=[0, 2])
```

set_velocities(
linear_velocities:list|np.ndarray|wp.array|None =None,
angular_velocities:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the velocities (linear and angular) of the prims.
Backends: tensor, usd.
Parameters:

- linear_velocities – Linear velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- angular_velocities – Angular velocities (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither linear_velocities nor angular_velocities are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random velocities for all prims
>>> linear_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> angular_velocities = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_velocities(linear_velocities, angular_velocities)
```

set_visibilities(
visibilities:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:

- visibilities – Boolean flags to set the visibility state (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # make all prims invisible
>>> prims.set_visibilities([False])
>>>
>>> # make first and last prims invisible
>>> prims.set_visibilities([True]) # restore visibility from previous call
>>> prims.set_visibilities([False], indices=[0, 2])
```

set_world_poses(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (positions and orientations) in the world frame of the prims.
Backends: tensor, usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_world_poses(positions, orientations)
```

propertyis_non_root_articulation_link:bool
Indicate if the wrapped prims are a non-root link in an articulation tree.
Backends: usd.
Warning
Transformation of the poses of non-root links in an articulation tree are not supported.
Returns:
Whether the prims are a non-root link in an articulation tree.

propertynum_shapes:int
Number of shapes in the rigid body.
Backends: tensor.
Returns:
Number of shapes in the rigid body.

Raises:
AssertionError – Physics tensor entity is not valid.

propertypaths:list[str]
Prim paths in the stage encapsulated by the wrapper.
Returns:
List of prim paths as strings.

Example:

```
>>> prims.paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyprims:list[pxr.Usd.Prim]
USD Prim objects encapsulated by the wrapper.
Returns:
List of USD Prim objects.

Example:

```
>>> prims.prims
[Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
```

propertyvalid:bool
Whether all prims in the wrapper are valid.
Returns:
True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

Example:

```
>>> prims.valid
True
```

classXformPrim(
paths:str|list[str],
*,
resolve_paths:bool=True,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Prim
High level wrapper for manipulating `Xform` prims and their attributes.
This class is a wrapper over one or more USD `Xform` prims in the stage to provide high-level functionality for manipulating transformations and other attributes. The prims are specified using paths that can include regular expressions for matching multiple prims.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If no prims are found matching the specified path(s).

- AssertionError – If both positions and translations are specified.

Example:

```
>>> import numpy as np
>>> from isaacsim.core.experimental.prims import XformPrim
>>>
>>> # given a USD stage with the Xform prims: /World/prim_0, /World/prim_1, and /World/prim_2
>>> # - create wrapper over single prim
>>> prim = XformPrim("/World/prim_0")
>>> # - create wrapper over multiple prims using regex
>>> prims = XformPrim("/World/prim_.*")
>>> prims.reset_xform_op_properties()
```
apply_visual_materials(
materials:type['VisualMaterial']|list[type['VisualMaterial']],
*,
weaker_than_descendants:bool|list|np.ndarray|wp.array|None =None,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Apply visual materials to the prims, and optionally, to their descendants.
Backends: usd.
Parameters:

- visual_materials – Visual materials to be applied to the prims (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- weaker_than_descendants – Boolean flags to indicate whether descendant materials should be overridden (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial
>>>
>>> # create a dark-red glass visual material
>>> material = OmniGlassMaterial("/World/material/glass")
>>> material.set_input_values("glass_ior", [1.25])
>>> material.set_input_values("depth", [0.001])
>>> material.set_input_values("thin_walled", [False])
>>> material.set_input_values("glass_color", [0.5, 0.0, 0.0])
>>>
>>> prims.apply_visual_materials(material)
```

staticensure_api(
prims:list[Usd.Prim],
api:type,
*args,
**kwargs,
)→list[type['UsdAPISchemaBase']]Ensure that all prims have the specified API schema applied.
Backends: usd.
If a prim doesn’t have the API schema, it will be applied. If it already has it, the existing API schema will be returned.
Parameters:

- prims – List of USD Prims to ensure API schema on.

- api – The API schema type to ensure.

- *args – Additional positional arguments passed to API schema when applying it.

- **kwargs – Additional keyword arguments passed to API schema when applying it.

Returns:
List of API schema objects, one for each input prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> from pxr import UsdPhysics
>>> from isaacsim.core.experimental.prims import Prim
>>>
>>> # given a USD stage with 3 prims at paths /World/prim_0, /World/prim_1, /World/prim_2,
>>> # ensure all prims have physics API schema
>>> usd_prims = [prim_utils.get_prim_at_path(f"/World/prim_{i}") for i in range(3)]
>>> physics_apis = Prim.ensure_api(usd_prims, UsdPhysics.RigidBodyAPI)
```

get_applied_visual_materials(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[type['VisualMaterial']|None ]Get the applied visual materials.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List of applied visual materials (shape `(N,)`). If a prim does not have a material, `None` is returned.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the applied visual material of the last wrapped prim
>>> prims.get_applied_visual_materials(indices=[2])[0]
<isaacsim.core.experimental.materials.impl.visual_materials.omni_glass.OmniGlassMaterial object at 0x...>
```

get_default_state(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array|None ,wp.array|None ]Get the default state (positions and orientations) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The default positions in the world frame (shape `(N, 3)`). 2) The default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the default state is not set using the set_default_state() method, `None` is returned.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

get_local_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (translations and orientations) in the local frame of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The translations in the local frame (shape `(N, 3)`). 2) The orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the local poses of all prims
>>> translations, orientations = prims.get_local_poses()
>>> translations.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the local pose of the first prim
>>> translations, orientations = prims.get_local_poses(indices=[0])
>>> translations.shape, orientations.shape
((1, 3), (1, 4))
```

get_local_scales(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Scales of the prims (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get local scales of all prims
>>> scales = prims.get_local_scales()
>>> scales.shape
(3, 3)
```

get_visibilities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating the visibility state (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the visibility states of all prims
>>> visibilities = prims.get_visibilities()
>>> visibilities.list()
[True, True, True]
>>>
>>> # get the visibility states of the first and last prims
>>> visibilities = prims.get_visibilities(indices=[0, 2])
>>> visibilities.list()
[True, True]
```

get_world_poses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the poses (positions and orientations) in the world frame of the prims.
Backends: usd, usdrt, fabric.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The positions in the world frame (shape `(N, 3)`). 2) The orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the world poses of all prims
>>> positions, orientations = prims.get_world_poses()
>>> positions.shape, orientations.shape
((3, 3), (3, 4))
>>>
>>> # get the world pose of the first prim
>>> positions, orientations = prims.get_world_poses(indices=[0])
>>> positions.shape, orientations.shape
((1, 3), (1, 4))
```

reset_to_default_state(
*,
warn_on_non_default_state:bool=False,
)→None Reset the prims to the specified default state.
Backends: usd, usdrt, fabric.
This method applies the default state defined using the set_default_state() method.
Note
This method teleports prims to the specified default state (positions and orientations).
Warning
This method has no effect on non-root articulation links or when no default state is set. In this case, a warning message is logged if `warn_on_non_default_state` is `True`.
Parameters:
warn_on_non_default_state – Whether to log a warning message when no default state is set.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get default state (no default state set at this point)
>>> prims.get_default_state()
(None, None)
>>>
>>> # set default state
>>> # - random positions for each prim
>>> # - same fixed orientation for all prim
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> prims.set_default_state(positions, orientations=[1.0, 0.0, 0.0, 0.0])
>>>
>>> # get default state (default state is set)
>>> prims.get_default_state()
(array(shape=(3, 3), dtype=float32), array(shape=(3, 4), dtype=float32))
>>>
>>> # reset prims to default state
>>> prims.reset_to_default_state()
```

reset_xform_op_properties()→None
Reset the transformation operation attributes of the prims to a standard set.
Backends: usd.
It ensures that each prim has only the following transformations in the specified order. Any other transformation operations are removed, so they are not consumed.

- `xformOp:translate` (double precision)

- `xformOp:orient` (double precision)

- `xformOp:scale` (double precision)

Note
This method preserves the poses of the prims in the world frame while reorganizing the transformation operations.
Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # reset transform operations of all prims
>>> prims.reset_xform_op_properties()
>>>
>>> # verify transform operations of the first wrapped prim
>>> prims.prims[0].GetPropertyNames()
[... 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
```

staticresolve_paths(
paths:str|list[str],
raise_on_mixed_paths:bool=True,
)→tuple[list[str],list[str]]Resolve paths to prims in the stage to get existing and non-existing paths.
Backends: usd.
Parameters:

- paths – Single path or list of paths to USD prims. Paths may contain regular expressions to match multiple prims.

- raise_on_mixed_paths – Whether to raise an error if resulting paths are mixed or invalid.

Returns:
Two-elements tuple. 1) List of existing paths. 2) List of non-existing paths.

Raises:
ValueError – If resulting paths are mixed or invalid and `raise_on_mixed_paths` is True.

set_default_state(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the default state (positions and orientations) of the prims.
Backends: usd.
Hint
Prims can be reset to their default state by calling the reset_to_default_state() method.
Parameters:

- positions – Default positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Default orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

- AssertionError – If prims are non-root articulation links.

set_local_poses(
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (translations and orientations) in the local frame of the prims.
Backends: usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the local frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither translations nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> translations = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_local_poses(translations, orientations)
```

set_local_scales(
scales:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the local scales of the prims.
Backends: usd, usdrt, fabric.
Parameters:

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random positive scales for all prims
>>> scales = np.random.uniform(low=0.5, high=1.5, size=(3, 3))
>>> prims.set_local_scales(scales)
```

set_visibilities(
visibilities:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the visibility state (whether prims are visible or invisible during rendering) of the prims.
Backends: usd.
Parameters:

- visibilities – Boolean flags to set the visibility state (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # make all prims invisible
>>> prims.set_visibilities([False])
>>>
>>> # make first and last prims invisible
>>> prims.set_visibilities([True]) # restore visibility from previous call
>>> prims.set_visibilities([False], indices=[0, 2])
```

set_world_poses(
positions:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the poses (positions and orientations) in the world frame of the prims.
Backends: usd, usdrt, fabric.
Note
This method teleports prims to the specified poses.
Parameters:

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither positions nor orientations are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set random poses for all prims
>>> positions = np.random.uniform(low=-1, high=1, size=(3, 3))
>>> orientations = np.random.randn(3, 4)
>>> orientations = orientations / np.linalg.norm(orientations, axis=-1, keepdims=True) # normalize quaternions
>>> prims.set_world_poses(positions, orientations)
```

propertyis_non_root_articulation_link:bool
Indicate if the wrapped prims are a non-root link in an articulation tree.
Backends: usd.
Warning
Transformation of the poses of non-root links in an articulation tree are not supported.
Returns:
Whether the prims are a non-root link in an articulation tree.

propertypaths:list[str]
Prim paths in the stage encapsulated by the wrapper.
Returns:
List of prim paths as strings.

Example:

```
>>> prims.paths
['/World/prim_0', '/World/prim_1', '/World/prim_2']
```

propertyprims:list[pxr.Usd.Prim]
USD Prim objects encapsulated by the wrapper.
Returns:
List of USD Prim objects.

Example:

```
>>> prims.prims
[Usd.Prim(</World/prim_0>), Usd.Prim(</World/prim_1>), Usd.Prim(</World/prim_2>)]
```

propertyvalid:bool
Whether all prims in the wrapper are valid.
Returns:
True if all prim paths specified in the wrapper correspond to valid prims in stage, False otherwise.

Example:

```
>>> prims.valid
True
```
