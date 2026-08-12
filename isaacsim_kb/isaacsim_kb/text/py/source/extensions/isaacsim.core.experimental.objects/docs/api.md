<!-- source: py/source/extensions/isaacsim.core.experimental.objects/docs/api.html | title: API — Isaac Sim -->

# API
Warning
The API featured in this extension is experimental and subject to change without deprecation cycles. Although we will try to maintain backward compatibility in the event of a change, it may not always be possible.

## Python API
The following table summarizes the available objects.
ground plane

[TABLE]
GroundPlane | High level class for creating/wrapping ground plane prims.
[/TABLE]
shapes

[TABLE]
Capsule | High level class for creating/wrapping USD Capsule (primitive cylinder capped by two half spheres, centered at the origin, whose spine is along the specified axis) prims.
Cone | High level class for creating/wrapping USD Cone (primitive cone, centered at the origin, whose spine is along the specified axis, with the apex of the cone pointing in the direction of the positive axis) prims.
Cube | High level class for creating/wrapping USD Cube (primitive rectilinear cube centered at the origin) prims.
Cylinder | High level class for creating/wrapping USD Cylinder (primitive cylinder with closed ends, centered at the origin, whose spine is along the specified axis) prims.
Plane | High level class for creating/wrapping USD Plane (primitive plane centered at the origin) prims.
Shape | Base class for creating/wrapping USD Geom shape prims.
Sphere | High level class for creating/wrapping USD Sphere (primitive sphere centered at the origin) prims.
[/TABLE]
meshes

[TABLE]
Mesh | High level class for creating/wrapping USD Mesh (points that are connected into edges and faces) prims.
[/TABLE]
lights

[TABLE]
CylinderLight | High level class for creating/wrapping USD Cylinder Light (light emitted outward from a cylinder) prims.
DiskLight | High level class for creating/wrapping USD Disk Light (light emitted from one side of a circular disk) prims.
DistantLight | High level class for creating/wrapping USD Distant Light (light emitted from a distant source along the -Z axis) prims.
DomeLight | High level class for creating/wrapping USD Dome Light (light emitted inward from a distant external environment) prims.
Light | Base class for creating/wrapping USD Light prims.
RectLight | High level class for creating/wrapping USD Rect Light (light emitted from one side of a rectangle) prims.
SphereLight | High level class for creating/wrapping USD Sphere Light (Light emitted outward from a sphere) prims.
[/TABLE]

### Ground Plane
classGroundPlane(
paths:str|list[str],
*,
sizes:float|list|np.ndarray|wp.array=100.0,
colors:list|np.ndarray|wp.array=[0.5,0.5,0.5],
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: XformPrim
High level class for creating/wrapping ground plane prims.
Ground plane prims have the following USD structure:

```
Xform // GroundPlane instance
|-- Plane // for collision and physics
|-- Mesh // for rendering, since Plane is unsupported by Hydra rendering
```
Note
This class creates or wraps (one of both) ground plane prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the ground plane prims.

- If the prim paths do not exist, ground plane prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) ground plane prims. Can include regular expressions for matching multiple prims.

- sizes – Sizes of the ground planes (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules). It has effect only when new ground plane prims are created. Ignored when wrapping existing prims.

- colors – Colors of the ground planes (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules). It has effect only when new ground plane prims are created. Ignored when wrapping existing prims.

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not ground planes.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import GroundPlane
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create a ground plane at path: /World/ground_plane
>>> prim = GroundPlane("/World/ground_plane")
>>>
>>> # create ground planes at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = GroundPlane(paths)
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
>>> prims.set_torsional_patch_radii([0.2], indices=[0, 2])
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

propertymeshes:Mesh
Mesh instance that encapsulated the USD Mesh prims that compose the ground planes.
Returns:
Mesh instance.

Example:

```
>>> prims.meshes
<isaacsim.core.experimental.objects.impl.mesh.Mesh object at 0x...>
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

propertyplanes:Plane
Plane instance that encapsulated the USD Plane prims that compose the ground planes.
Returns:
Plane instance.

Example:

```
>>> prims.planes
<isaacsim.core.experimental.objects.impl.shapes.plane.Plane object at 0x...>
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

### Shapes
classCapsule(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
heights:float|list|np.ndarray|wp.array|None =None,
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Shape
High level class for creating/wrapping USD Capsule (primitive cylinder capped by two half spheres, centered at the origin, whose spine is along the specified axis) prims.
Note
This class creates or wraps (one of both) USD Capsule prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Capsule prims.

- If the prim paths do not exist, USD Capsule prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (capsule’s two half-spheres radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- heights – Heights (capsule’s spine length along the axis excluding the size of the two half spheres) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- axes – Axes (capsule’s axis along which the spine is aligned) (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Capsule.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Capsule
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create capsules at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Capsule(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Capsule.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

get_axes(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[Literal['X','Y','Z']]Get the axes (capsule’s axis along which the spine is aligned) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The axes (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the axes of all prims
>>> axes = prims.get_axes()
>>> axes
['Z', 'Z', 'Z']
>>>
>>> # get the axes of the first and last prims
>>> axes = prims.get_axes(indices=[0, 2])
>>> axes
['Z', 'Z']
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

get_heights(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the heights (capsule’s spine length along the axis excluding the size of the two half spheres) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The heights (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the heights of all prims
>>> heights = prims.get_heights()
>>> heights.shape
(3, 1)
>>>
>>> # get the heights of the first and last prims
>>> heights = prims.get_heights(indices=[0, 2])
>>> heights.shape
(2, 1)
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

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii (capsule’s two half-spheres radius) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_axes(
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the axes (capsule’s axis along which the spine is aligned) of the prims.
Backends: usd.
Parameters:

- axes – Axes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Invalid axis token.

Example:

```
>>> # set a different axis for each prim
>>> prims.set_axes(axes=["X", "Y", "Z"])
>>>
>>> # set the axis for the second prim
>>> prims.set_axes(axes=["X"], indices=[1])
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

set_heights(
heights:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the heights (capsule’s spine length along the axis excluding the size of the two half spheres) of the prims.
Backends: usd.
Parameters:

- heights – Heights (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same heights for all prims
>>> prims.set_heights(heights=[0.1])
>>>
>>> # set only the height for the second prim
>>> prims.set_heights(heights=[0.2], indices=[1])
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

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii (capsule’s two half-spheres radius) of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Capsule])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

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

classCone(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
heights:float|list|np.ndarray|wp.array|None =None,
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Shape
High level class for creating/wrapping USD Cone (primitive cone, centered at the origin, whose spine is along the specified axis, with the apex of the cone pointing in the direction of the positive axis) prims.
Note
This class creates or wraps (one of both) USD Cone prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Cone prims.

- If the prim paths do not exist, USD Cone prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (cone’s radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- heights – Heights (cone’s spine length along the axis) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- axes – Axes (cone’s axis along which the spine is aligned) (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Cone.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Cone
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create cones at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Cone(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Cone.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

get_axes(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[Literal['X','Y','Z']]Get the axes (cone’s axis along which the spine is aligned) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The axes (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the axes of all prims
>>> axes = prims.get_axes()
>>> axes
['Z', 'Z', 'Z']
>>>
>>> # get the axes of the first and last prims
>>> axes = prims.get_axes(indices=[0, 2])
>>> axes
['Z', 'Z']
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

get_heights(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the heights (cone’s spine length along the axis) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The heights (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the heights of all prims
>>> heights = prims.get_heights()
>>> heights.shape
(3, 1)
>>>
>>> # get the heights of the first and last prims
>>> heights = prims.get_heights(indices=[0, 2])
>>> heights.shape
(2, 1)
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

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii (cone’s radius) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_axes(
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the axes (cone’s axis along which the spine is aligned) of the prims.
Backends: usd.
Parameters:

- axes – Axes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Invalid axis token.

Example:

```
>>> # set a different axis for each prim
>>> prims.set_axes(axes=["X", "Y", "Z"])
>>>
>>> # set the axis for the second prim
>>> prims.set_axes(axes=["X"], indices=[1])
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

set_heights(
heights:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the heights (cone’s spine length along the axis) of the prims.
Backends: usd.
Parameters:

- heights – Heights (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same heights for all prims
>>> prims.set_heights(heights=[0.1])
>>>
>>> # set only the height for the second prim
>>> prims.set_heights(heights=[0.2], indices=[1])
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

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii (cone’s radius) of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Cone])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

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

classCube(
paths:str|list[str],
*,
sizes:float|list|np.ndarray|wp.array|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Shape
High level class for creating/wrapping USD Cube (primitive rectilinear cube centered at the origin) prims.
Note
This class creates or wraps (one of both) USD Cube prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Cube prims.

- If the prim paths do not exist, USD Cube prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- sizes – Sizes (cube’s edge length) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Cube.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Cube
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create cubes at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Cube(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Cube.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

get_sizes(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the sizes (cube’s edge length) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The sizes (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the sizes of all prims
>>> sizes = prims.get_sizes()
>>> sizes.shape
(3, 1)
>>>
>>> # get the sizes of the first and last prims
>>> sizes = prims.get_sizes(indices=[0, 2])
>>> sizes.shape
(2, 1)
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

set_sizes(
sizes:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the sizes (cube’s edge length) of the prims.
Backends: usd.
Parameters:

- sizes – Sizes (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same sizes for all prims
>>> prims.set_sizes(sizes=[0.1])
>>>
>>> # set only the size for the second prim
>>> prims.set_sizes(sizes=[0.2], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Cube])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

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

classCylinder(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
heights:float|list|np.ndarray|wp.array|None =None,
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Shape
High level class for creating/wrapping USD Cylinder (primitive cylinder with closed ends, centered at the origin, whose spine is along the specified axis) prims.
Note
This class creates or wraps (one of both) USD Cylinder prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Cylinder prims.

- If the prim paths do not exist, USD Cylinder prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (cylinder’s radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- heights – Heights (cylinder’s spine length along the axis) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- axes – Axes (cylinder’s axis along which the spine is aligned) (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Cylinder.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Cylinder
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create cylinders at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Cylinder(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Cylinder.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

get_axes(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[Literal['X','Y','Z']]Get the axes (cylinder’s axis along which the spine is aligned) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The axes (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the axes of all prims
>>> axes = prims.get_axes()
>>> axes
['Z', 'Z', 'Z']
>>>
>>> # get the axes of the first and last prims
>>> axes = prims.get_axes(indices=[0, 2])
>>> axes
['Z', 'Z']
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

get_heights(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the heights (cylinder’s spine length along the axis) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The heights (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the heights of all prims
>>> heights = prims.get_heights()
>>> heights.shape
(3, 1)
>>>
>>> # get the heights of the first and last prims
>>> heights = prims.get_heights(indices=[0, 2])
>>> heights.shape
(2, 1)
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

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii (cylinder’s radius) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_axes(
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the axes (cylinder’s axis along which the spine is aligned) of the prims.
Backends: usd.
Parameters:

- axes – Axes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Invalid axis token.

Example:

```
>>> # set a different axis for each prim
>>> prims.set_axes(axes=["X", "Y", "Z"])
>>>
>>> # set the axis for the second prim
>>> prims.set_axes(axes=["X"], indices=[1])
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

set_heights(
heights:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the heights (cylinder’s spine length along the axis) of the prims.
Backends: usd.
Parameters:

- heights – Heights (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same heights for all prims
>>> prims.set_heights(heights=[0.1])
>>>
>>> # set only the height for the second prim
>>> prims.set_heights(heights=[0.2], indices=[1])
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

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii (cylinder’s radius) of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Cylinder])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

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

classPlane(
paths:str|list[str],
*,
widths:float|list|np.ndarray|wp.array|None =None,
lengths:float|list|np.ndarray|wp.array|None =None,
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Shape
High level class for creating/wrapping USD Plane (primitive plane centered at the origin) prims.
Warning
USD Plane is currently not supported by Omniverse Hydra rendering. Authoring operations can still be applied, but there will be no rendering in the viewport.
Note
This class creates or wraps (one of both) USD Plane prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Plane prims.

- If the prim paths do not exist, USD Plane prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- widths – Widths (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- lengths – Lengths (plane’s length) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- axes – Axes (plane’s axis along which the surface is aligned) (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Plane.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Plane
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create planes at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Plane(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Plane.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

get_axes(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[Literal['X','Y','Z']]Get the axes (plane’s axis along which the surface is aligned) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The axes (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the axes of all prims
>>> axes = prims.get_axes()
>>> axes
['Z', 'Z', 'Z']
>>>
>>> # get the axes of the first and last prims
>>> axes = prims.get_axes(indices=[0, 2])
>>> axes
['Z', 'Z']
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

get_lengths(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the lengths of the prims.
Backends: usd.
The length aligns to the y-axis when axis is `'X'` or `'Z'`, or to the z-axis when axis is `'Y'`.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The lengths (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the lengths of all prims
>>> lengths = prims.get_lengths()
>>> lengths.shape
(3, 1)
>>>
>>> # get the lengths of the first and last prims
>>> lengths = prims.get_lengths(indices=[0, 2])
>>> lengths.shape
(2, 1)
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

get_widths(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the widths of the prims.
Backends: usd.
The width aligns to the x-axis when axis is `'Y'` or `'Z'`, or to the z-axis when axis is `'X'`.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The widths (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the widths of all prims
>>> widths = prims.get_widths()
>>> widths.shape
(3, 1)
>>>
>>> # get the widths of the first and last prims
>>> widths = prims.get_widths(indices=[0, 2])
>>> widths.shape
(2, 1)
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

set_axes(
axes:Literal['X','Y','Z']|list[Literal['X','Y','Z']],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the axes (plane’s axis along which the surface is aligned) of the prims.
Backends: usd.
Parameters:

- axes – Axes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – Invalid axis token.

Example:

```
>>> # set a different axis for each prim
>>> prims.set_axes(axes=["X", "Y", "Z"])
>>>
>>> # set the axis for the second prim
>>> prims.set_axes(axes=["X"], indices=[1])
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

set_lengths(
lengths:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the lengths of the prims.
Backends: usd.
The length aligns to the y-axis when axis is `'X'` or `'Z'`, or to the z-axis when axis is `'Y'`.
Parameters:

- lengths – Lengths (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same lengths for all prims
>>> prims.set_lengths(lengths=[0.1])
>>>
>>> # set only the length for the second prim
>>> prims.set_lengths(lengths=[0.2], indices=[1])
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

set_widths(
widths:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the widths of the prims.
Backends: usd.
The width aligns to the x-axis when axis is `'Y'` or `'Z'`, or to the z-axis when axis is `'X'`.
Parameters:

- widths – Widths (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same widths for all prims
>>> prims.set_widths(widths=[0.1])
>>>
>>> # set only the width for the second prim
>>> prims.set_widths(widths=[0.2], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Plane])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

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

classShape(
paths:str|list[str],
*,
resolve_paths:bool=True,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: XformPrim , `ABC`
Base class for creating/wrapping USD Geom shape prims.
Note
This class creates or wraps (one of both) USD Cube prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Cube prims.

- If the prim paths do not exist, USD Cube prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:
ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

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

abstractstaticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

abstractstaticupdate_extents(geoms:list[pxr.UsdGeom.Gprim])→None
Update the gprims’ extents.
Parameters:
geoms – Geoms to process.

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

classSphere(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Shape
High level class for creating/wrapping USD Sphere (primitive sphere centered at the origin) prims.
Note
This class creates or wraps (one of both) USD Sphere prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Sphere prims.

- If the prim paths do not exist, USD Sphere prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (sphere’s radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Sphere.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Sphere
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create spheres at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Sphere(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Shape instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Shape instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Sphere.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Shape |None ]Fetch instances of Shape from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Shape instances from.

Returns:
List of Shape instances or `None` if the prim is not a supported Shape type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Shape
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cube), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "Cube")
>>> stage_utils.define_prim(f"/World/B", "Sphere")
>>>
>>> # fetch shape instances
>>> Shape.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.shapes.cube.Cube object at 0x...>,
<isaacsim.core.experimental.objects.impl.shapes.sphere.Sphere object at 0x...>]
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

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii (sphere’s radius) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii (sphere’s radius) of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Sphere])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

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

### Meshes
classMesh(
paths:str|list[str],
*,
primitives:Literal['Cone','Cube','Cylinder','Disk','Plane','Sphere','Torus']|list[Literal['Cone','Cube','Cylinder','Disk','Plane','Sphere','Torus']]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: XformPrim
High level class for creating/wrapping USD Mesh (points that are connected into edges and faces) prims.
Note
This class creates or wraps (one of both) USD Mesh prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Mesh prims.

- If the prim paths do not exist, USD Mesh prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- primitives – Primitives to be created (shape `(N,)`). If not defined, an empty mesh is created. Primitives are used only for creating operations. For wrapping operations, primitives are ignored. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Mesh.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import Mesh
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create Plane meshes at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = Mesh(paths, primitives="Plane")
```
Example (create mesh from external package: trimesh):

```
>>> from isaacsim.core.experimental.objects import Mesh
>>> import trimeshx
>>>
>>> # icosahedron mesh (20 faces)
>>> mesh = trimesh.creation.icosahedron()
>>>
>>> # create an USD Mesh from the icosahedron defined by trimesh
>>> mesh_prim = Mesh("/World/icosahedron")
>>> mesh_prim.set_points([mesh.vertices])
>>> mesh_prim.set_face_specs(
... vertex_indices=[mesh.faces.flatten()],
... vertex_counts=[[3] * len(mesh.faces)]
... )
>>> mesh_prim.set_subdivision_specs(subdivision_schemes=["bilinear"])
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Mesh instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Mesh instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = Mesh.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Mesh |None ]Fetch instances of Mesh from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Mesh instances from.

Returns:
List of Mesh instances or `None` if the prim is not a supported Mesh type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Mesh
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Mesh)
>>> stage_utils.define_prim(f"/World/A", "Mesh")
>>>
>>> # fetch mesh instances
>>> Mesh.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.objects.impl.mesh.Mesh object at 0x...>]
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

get_corner_specs(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[list[wp.array],list[wp.array]]Get the corner specifications of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) List (shape `(N,)`) of indices of points (shape `(number of target points,)`). 2) List (shape `(N,)`) of sharpness values (shape `(number of target points,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the corner specifications of all prims
>>> corner_indices, corner_sharpnesses = prims.get_corner_specs()
```

get_crease_specs(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[list[wp.array],list[wp.array],list[wp.array]]Get the crease (set of adjacent sharpened edges) specifications of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Three-elements tuple. 1) List (shape `(N,)`) of indices of points (shape `(sum of all elements of the creaseLengths,)`). 2) List (shape `(N,)`) of number of points of each crease (shape `(number of creases,)`). 3) List (shape `(N,)`) of sharpness values (shape `(number of creases,)` or `(sum over all X of (creaseLengths[X] - 1),)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the crease specifications of all prims
>>> crease_indices, crease_lengths, crease_sharpnesses = prims.get_crease_specs()
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

get_face_specs(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[list[wp.array],list[wp.array],list[Literal['none','cornersOnly','cornersPlus1','cornersPlus2','boundaries','all']],list[wp.array]]Get the face (3D model flat surface) specifications of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Four-elements tuple. 1) List (shape `(N,)`) of indices (of points) of each vertex of each face (shape `(sum of all elements of the vertexCounts,)`). 2) List (shape `(N,)`) of number of vertices in each face (shape `(number of faces,)`). 3) List (shape `(N,)`) of face-varying interpolation rules. 4) List (shape `(N,)`) of indices of all face holes (shape `(up to the number of faces,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the face specifications of all prims
>>> face_indices, face_counts, face_interpolations, face_holes = prims.get_face_specs()
>>> # print the first prim's face specifications (Plane mesh composed of 4 points with 1 face)
>>> print(face_indices[0]) # points indices of the face
[0 1 3 2]
>>> print(face_counts[0]) # number of points in the face
[4]
>>> face_interpolations[0] # face-varying interpolation rule
'cornersPlus1'
>>> print(face_holes[0]) # indices of the face holes (empty: no face holes)
[]
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

get_normals(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[wp.array]Get the mesh normals (object-space orientation for individual points) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List (shape `(N,)`) of mesh normals (shape `(number of normals, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the normals of all prims
>>> normals = prims.get_normals()
>>> normals[0].shape # normals' shape of the first prim
(4, 3)
```

get_points(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[wp.array]Get the mesh points (in local space) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
List (shape `(N,)`) of mesh points (shape `(number of points, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the points of all prims
>>> points = prims.get_points()
>>> points[0].shape # points' shape of the first prim
(4, 3)
```

get_subdivision_specs(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[list[Literal['catmullClark','loop','bilinear','none']],list[Literal['none','edgeOnly','edgeAndCorner']],list[Literal['catmullClark','smooth']]]Get the subdivision specifications of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Three-elements tuple. 1) Subdivision schemes (shape `(N,)`). 2) Boundary interpolation rules (shape `(N,)`). 3) Triangle subdivision rules (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the subdivision specifications of all prims
>>> subdivision_schemes, interpolate_boundaries, triangle_subdivision_rules = prims.get_subdivision_specs()
>>> # print the first prim's subdivision specifications
>>> subdivision_schemes[0] # subdivision scheme
'none'
>>> interpolate_boundaries[0] # boundary interpolation rule
'edgeAndCorner'
>>> triangle_subdivision_rules[0] # triangle subdivision rule
'catmullClark'
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

set_corner_specs(
corner_indices:list[list|np.ndarray|wp.array],
corner_sharpnesses:list[list|np.ndarray|wp.array],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the corner specifications of the prims.
Backends: usd.
Parameters:

- corner_indices – List (shape `(N,)`) of indices of points (shape `(number of target points,)`) for which a corresponding sharpness value is specified in `cornerSharpnesses`. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- corner_sharpnesses – List (shape `(N,)`) of sharpness values (shape `(number of target points,)`) associated with a corresponding set of points specified in `cornerIndices`. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If each respective pair of items (from `corner_indices` and `corner_sharpnesses`) has a different shape.

Example:

```
>>> # set the corner specifications (mesh points: 1, 2) for the second prim
>>> prims.set_corner_specs(corner_indices=[[1, 2]], corner_sharpnesses=[[5.0, 10.0]], indices=[1])
```

set_crease_specs(
crease_indices:list[list|np.ndarray|wp.array],
crease_lengths:list[list|np.ndarray|wp.array],
crease_sharpnesses:list[list|np.ndarray|wp.array],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the crease (set of adjacent sharpened edges) specifications of the prims.
Backends: usd.
Parameters:

- crease_indices – List (shape `(N,)`) of indices of points grouped into sets of successive pairs that identify edges to be creased (shape `(sum of all elements of the creaseLengths,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- crease_lengths – List (shape `(N,)`) of number of points of each crease, whose indices are successively laid out in the `creaseIndices` attribute (shape `(number of creases,)`). Since each crease must be at least one edge long, each element of this array must be at least two. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- crease_sharpnesses – List (shape `(N,)`) of per-crease or per-edge sharpness values (shape `(number of creases,)` or `(sum over all X of (creaseLengths[X] - 1),)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- AssertionError – If the sum of the elements of `crease_lengths` is not equal to the number of elements of `crease_indices`.

- AssertionError – If the number of elements of `crease_sharpnesses` is not equal to the number of elements of `crease_lengths` or the sum over all X of `(crease_lengths[X] - 1)`.

Example:

```
>>> # set the crease specifications (mesh points: 0, 3) for the second prim
>>> prims.set_crease_specs(
... crease_indices=[[0, 3]],
... crease_lengths=[[2]],
... crease_sharpnesses=[[10.0]],
... indices=[1]
... )
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

set_face_specs(
vertex_indices:list[list|np.ndarray|wp.array]|None =None,
vertex_counts:list[list|np.ndarray|wp.array]|None =None,
varying_linear_interpolations:list[Literal['none','cornersOnly','cornersPlus1','cornersPlus2','boundaries','all']]|None =None,
hole_indices:list[list|np.ndarray|wp.array]|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the face (3D model flat surface) specifications of the prims.
Backends: usd.
Parameters:

- vertex_indices – List (shape `(N,)`) of indices (of points) of each vertex of each face (shape `(sum of all elements of the vertexCounts,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- vertex_counts – List (shape `(N,)`) of number of vertices in each face, which is also the number of consecutive indices in `faceVertexIndices` that define the face (shape `(number of faces,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- varying_linear_interpolations – Face-varying interpolation rules in the interior of face-varying regions (smooth or linear) and at the boundaries for subdivision surfaces (shape `(N,)`).

- hole_indices – List (shape `(N,)`) of indices of all faces that should be treated as holes, e.g.: made invisible (shape `(up to the number of faces,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither vertex_indices, vertex_counts, varying_linear_interpolations nor hole_indices are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the face specifications (2 triangles) for the second prim
>>> prims.set_face_specs(vertex_indices=[[0, 1, 3, 0, 2, 3]], vertex_counts=[[3, 3]], indices=[1])
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

set_normals(
normals:list[list|np.ndarray|wp.array],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the mesh normals (object-space orientation for individual points) of the prims.
Backends: usd.
Note
Normals should not be authored on any USD Mesh that is subdivided, since the subdivision algorithm will define its own normals.
Parameters:

- normals – List (shape `(N,)`) of mesh normals (shape `(number of normals, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # clear the normals for the second prim
>>> prims.set_normals([[]], indices=[1])
```

set_points(
points:list[list|np.ndarray|wp.array],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the mesh points (in local space) of the prims.
Backends: usd.
Parameters:

- points – List (shape `(N,)`) of mesh points (shape `(number of points, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the points (fold each face diagonally) for the second prim
>>> prims.set_points([[(-0.5, -0.5, 0.0), (0.5, -0.5, 1.0), (-0.5, 0.5, 1.0), (0.5, 0.5, 0.0)]], indices=[1])
```

set_subdivision_specs(
subdivision_schemes:list[Literal['catmullClark','loop','bilinear','none']]|None =None,
interpolate_boundaries:list[Literal['none','edgeOnly','edgeAndCorner']]|None =None,
triangle_subdivision_rules:list[Literal['catmullClark','smooth']]|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the subdivision specifications of the prims.
Backends: usd.
Parameters:

- subdivision_schemes – Subdivision schemes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- interpolate_boundaries – Boundary interpolation rules for faces adjacent to boundary edges and points (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- triangle_subdivision_rules – Subdivision rules for the Catmull-Clark scheme to try and improve undesirable artifacts when subdividing triangles (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither subdivision_schemes, interpolate_boundaries nor triangle_subdivision_rules are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the subdivision specifications for the second prim
>>> prims.set_subdivision_specs(subdivision_schemes=["bilinear"], indices=[1])
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

staticupdate_extents(geoms:list[pxr.UsdGeom.Mesh])→None
Update the gprims’ extents.
Backends: usd.
Parameters:
geoms – Geoms to process.

propertygeoms:list[pxr.UsdGeom.Mesh]
USD Mesh encapsulated by the wrapper.
Returns:
List of USD Mesh.

Example:

```
>>> prims.geoms
[UsdGeom.Mesh(Usd.Prim(</World/prim_0>)),
UsdGeom.Mesh(Usd.Prim(</World/prim_1>)),
UsdGeom.Mesh(Usd.Prim(</World/prim_2>))]
```

propertyis_non_root_articulation_link:bool
Indicate if the wrapped prims are a non-root link in an articulation tree.
Backends: usd.
Warning
Transformation of the poses of non-root links in an articulation tree are not supported.
Returns:
Whether the prims are a non-root link in an articulation tree.

propertynum_faces:list[int]
Number of faces of the meshes.
Returns:
List of number of faces as defined by the size of the `faceVertexCounts` array.

Example:

```
>>> prims.num_faces
[1, 1, 1]
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

### Lights
classCylinderLight(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
lengths:float|list|np.ndarray|wp.array|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Light
High level class for creating/wrapping USD Cylinder Light (light emitted outward from a cylinder) prims.
The cylinder is centered at the origin and has its major axis on the X axis. The cylinder does not emit light from the flat end-caps.
Note
This class creates or wraps (one of both) USD Cylinder Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Cylinder Light prims.

- If the prim paths do not exist, USD Cylinder Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (cylinder’s radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- lengths – Lengths (cylinder’s spine length along the axis) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Cylinder Light.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import CylinderLight
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create cylinder lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = CylinderLight(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = CylinderLight.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_enabled_treat_as_lines(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the treat as lines (effectively, a zero-radius cylinder) of the prims.
Backends: usd.
Warning
Renderers that do not support non-area lighting can ignore this.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if treat as lines is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the treat as lines enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_treat_as_lines([True], indices=[1])
>>> print(prims.get_enabled_treat_as_lines())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
```

get_lengths(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the lengths (in the local X axis) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The lengths (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the lengths of all prims
>>> lengths = prims.get_lengths()
>>> lengths.shape
(3, 1)
>>>
>>> # get the lengths of the first and last prims
>>> lengths = prims.get_lengths(indices=[0, 2])
>>> lengths.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
```

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_enabled_treat_as_lines(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the treat as lines (effectively, a zero-radius cylinder) of the prims.
Backends: usd.
Warning
Renderers that do not support non-area lighting can ignore this.
Parameters:

- enabled – Boolean flags to enable/disable treat as lines (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the treat as lines for all prims
>>> prims.set_enabled_treat_as_lines([True])
>>>
>>> # disable the treat as lines for the first and last prims
>>> prims.set_enabled_treat_as_lines([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
```

set_lengths(
lengths:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the lengths (in the local X axis) of the prims.
Backends: usd.
Parameters:

- lengths – Lengths (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same lengths for all prims
>>> prims.set_lengths(lengths=[0.1])
>>>
>>> # set only the length for the second prim
>>> prims.set_lengths(lengths=[0.2], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
```

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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

classDiskLight(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Light
High level class for creating/wrapping USD Disk Light (light emitted from one side of a circular disk) prims.
The disk is centered in the XY plane and emits light along the -Z axis.
Note
This class creates or wraps (one of both) USD Disk Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Disk Light prims.

- If the prim paths do not exist, USD Disk Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (disk’s radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Disk Light.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import DiskLight
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create disk lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = DiskLight(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = DiskLight.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
```

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
```

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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

classDistantLight(
paths:str|list[str],
*,
angles:float|list|np.ndarray|wp.array|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Light
High level class for creating/wrapping USD Distant Light (light emitted from a distant source along the -Z axis) prims.
Note
This class creates or wraps (one of both) USD Distant Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Distant Light prims.

- If the prim paths do not exist, USD Distant Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- angles – Angles (shape `(N, 1)`). The values are assumed to be in the range `[0, 2 * pi)`. If a value is 0, the light represents a perfectly parallel light source. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Distant Light.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import DistantLight
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create distant lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = DistantLight(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = DistantLight.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
```

get_angles(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the angles (angular diameter of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The angles (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the angles of all prims
>>> angles = prims.get_angles()
>>> angles.shape
(3, 1)
>>>
>>> # get the angles of the first and last prims
>>> angles = prims.get_angles(indices=[0, 2])
>>> angles.shape
(2, 1)
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
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

set_angles(
angles:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the angles (angular diameter of the light) of the prims.
Backends: usd.
Parameters:

- angles – Angles (shape `(N, 1)`). The values are assumed to be in the range `[0, 2 * pi)`. If a value is 0, the light represents a perfectly parallel light source. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same angles for all prims
>>> prims.set_angles(angles=[0.5236])
>>>
>>> # set only the angle for the second prim
>>> prims.set_angles(angles=[0.7854], indices=[1])
```

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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

classDomeLight(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
texture_files:str|list[str]|None =None,
texture_formats:Literal['automatic','latlong','mirroredBall','angular','cubeMapVerticalCross']|list[Literal['automatic','latlong','mirroredBall','angular','cubeMapVerticalCross']]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Light
High level class for creating/wrapping USD Dome Light (light emitted inward from a distant external environment) prims.
Note
This class creates or wraps (one of both) USD Dome Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Dome Light prims.

- If the prim paths do not exist, USD Dome Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Guide radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- texture_files – Color texture files (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- texture_formats – Texture formats (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Dome Light.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import DomeLight
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create dome lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = DomeLight(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = DomeLight.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_guide_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the guide radii (use to visualize the dome light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The guide radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the guide radii of all prims
>>> radii = prims.get_guide_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the guide radii of the first and last prims
>>> radii = prims.get_guide_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
```

get_texture_files(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[str]Get the color texture files (e.g.: High Dynamic Range (HDR) texture intended for Image Based Lighting (IBL)) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color texture files (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the color texture file for the second prim
>>> prims.set_texture_files(["/local/path/to/texture_1"], indices=[1])
>>>
>>> # get the color texture files of all prims
>>> prims.get_texture_files()
[None, '/local/path/to/texture_1', None]
```

get_texture_formats(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[Literal['automatic','latlong','mirroredBall','angular','cubeMapVerticalCross']]Get the texture formats (parameterization of the color map file) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The texture formats (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the texture formats of all prims
>>> prims.get_texture_formats()
['automatic', 'automatic', 'automatic']
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

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_guide_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the guide radii (use to visualize the dome light) of the prims.
Backends: usd.
Parameters:

- radii – Guide radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same guide radii for all prims
>>> prims.set_guide_radii(radii=[0.1])
>>>
>>> # set only the guide radius for the second prim
>>> prims.set_guide_radii(radii=[0.2], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
```

set_texture_files(
texture_files:str|list[str],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color texture files (e.g.: High Dynamic Range (HDR) texture intended for Image Based Lighting (IBL)) of the prims.
Backends: usd.
Parameters:

- texture_files – Color texture files (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set color texture files for all prims
>>> prims.set_texture_files(texture_files=[
... "/local/path/to/texture_0",
... "/local/path/to/texture_1",
... "/local/path/to/texture_2",
... ])
```

set_texture_formats(
texture_formats:Literal['automatic','latlong','mirroredBall','angular','cubeMapVerticalCross']|list[Literal['automatic','latlong','mirroredBall','angular','cubeMapVerticalCross']],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the texture formats (parameterization of the color map file) of the prims.
Backends: usd.
Parameters:

- texture_formats – Texture formats (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the texture formats for the second prim
>>> prims.set_texture_formats(texture_formats=["latlong"], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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

classLight(
paths:str|list[str],
*,
resolve_paths:bool=True,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: XformPrim , `ABC`
Base class for creating/wrapping USD Light prims.
Note
This class creates or wraps (one of both) USD Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Light prims.

- If the prim paths do not exist, USD Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If both positions and translations are specified.

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

abstractstaticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
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

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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

classRectLight(
paths:str|list[str],
*,
widths:float|list|np.ndarray|wp.array|None =None,
heights:float|list|np.ndarray|wp.array|None =None,
texture_files:str|list[str]|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Light
High level class for creating/wrapping USD Rect Light (light emitted from one side of a rectangle) prims.
The rectangle, centered in the XY plane, emits light along the -Z axis.
Note
This class creates or wraps (one of both) USD Rect Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Rect Light prims.

- If the prim paths do not exist, USD Rect Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- widths – Widths (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- heights – Heights (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- texture_files – Color texture files (shape `(N,)`). In the default position, the texture file’s minimum and maximum coordinates should be at `(+X, +Y)` and `(-X, -Y)` respectively. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Rect Light.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import RectLight
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create rect lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = RectLight(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = RectLight.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_heights(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the heights of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The heights (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the heights of all prims
>>> heights = prims.get_heights()
>>> heights.shape
(3, 1)
>>>
>>> # get the heights of the first and last prims
>>> heights = prims.get_heights(indices=[0, 2])
>>> heights.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
```

get_texture_files(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→list[str|None ]Get the color texture files (to use on the rectangle) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color texture files or `None` if no texture is set (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the color texture file for the second prim
>>> prims.set_texture_files(["/local/path/to/texture_1"], indices=[1])
>>>
>>> # get the color texture files of all prims
>>> prims.get_texture_files()
[None, '/local/path/to/texture_1', None]
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

get_widths(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the widths of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The widths (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the widths of all prims
>>> widths = prims.get_widths()
>>> widths.shape
(3, 1)
>>>
>>> # get the widths of the first and last prims
>>> widths = prims.get_widths(indices=[0, 2])
>>> widths.shape
(2, 1)
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

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_heights(
heights:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the heights of the prims.
Backends: usd.
Parameters:

- heights – Heights (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same heights for all prims
>>> prims.set_heights(heights=[0.1])
>>>
>>> # set only the height for the second prim
>>> prims.set_heights(heights=[0.2], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
```

set_texture_files(
texture_files:str|list[str],
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color texture files (to use on the rectangle) of the prims.
Backends: usd.
Parameters:

- texture_files – Color texture files (shape `(N,)`). In the default position, the texture file’s minimum and maximum coordinates should be at `(+X, +Y)` and `(-X, -Y)` respectively. If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set color texture files for all prims
>>> prims.set_texture_files(texture_files=[
... "/local/path/to/texture_0",
... "/local/path/to/texture_1",
... "/local/path/to/texture_2",
... ])
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

set_widths(
widths:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the widths of the prims.
Backends: usd.
Parameters:

- lengths – Lengths (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same widths for all prims
>>> prims.set_widths(widths=[0.1])
>>>
>>> # set only the width for the second prim
>>> prims.set_widths(widths=[0.2], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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

classSphereLight(
paths:str|list[str],
*,
radii:float|list|np.ndarray|wp.array|None =None,
positions:list|np.ndarray|wp.array|None =None,
translations:list|np.ndarray|wp.array|None =None,
orientations:list|np.ndarray|wp.array|None =None,
scales:list|np.ndarray|wp.array|None =None,
reset_xform_op_properties:bool=False,
)Bases: Light
High level class for creating/wrapping USD Sphere Light (Light emitted outward from a sphere) prims.
Note
This class creates or wraps (one of both) USD Sphere Light prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Sphere Light prims.

- If the prim paths do not exist, USD Sphere Light prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to existing or non-existing (one of both) USD prims. Can include regular expressions for matching multiple prims.

- radii – Radii (sphere’s radius) (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- positions – Positions in the world frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- translations – Translations in the local frame (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- orientations – Orientations in the world frame (shape `(N, 4)`, quaternion `wxyz`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- scales – Scales to be applied to the prims (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- reset_xform_op_properties – Whether to reset the transformation operation attributes of the prims to a standard set. See reset_xform_op_properties() for more details.

Raises:

- ValueError – If resulting paths are mixed (existing and non-existing prims) or invalid.

- AssertionError – If wrapped prims are not USD Sphere Light.

- AssertionError – If both positions and translations are specified.

Example:

```
>>> from isaacsim.core.experimental.objects import SphereLight
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create sphere lights at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = SphereLight(paths)
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

staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating Light instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating Light instances.

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = SphereLight.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[False True]
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

staticfetch_instances(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→list[Light |None ]Fetch instances of Light from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get Light instances from.

Returns:
List of Light instances or `None` if the prim is not a supported Light type.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.objects import Light
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (Cylinder), /World/B (Sphere)
>>> stage_utils.define_prim(f"/World/A", "CylinderLight")
>>> stage_utils.define_prim(f"/World/B", "SphereLight")
>>>
>>> # fetch light instances
>>> Light.fetch_instances(["/World", "/World/A", "/World/B"])
[None,
<isaacsim.core.experimental.objects.impl.lights.cylinder.CylinderLight object at 0x...>,
<isaacsim.core.experimental.objects.impl.lights.sphere.SphereLight object at 0x...>]
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

get_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The color temperatures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the color temperatures of all prims
>>> color_temperatures = prims.get_color_temperatures()
>>> color_temperatures.shape
(3, 1)
>>>
>>> # get the color temperatures of the first and last prims
>>> color_temperatures = prims.get_color_temperatures(indices=[0, 2])
>>> color_temperatures.shape
(2, 1)
```

get_colors(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The colors (shape `(N, 3)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the colors of all prims
>>> colors = prims.get_colors()
>>> colors.shape
(3, 3)
>>>
>>> # get the colors of the first and last prims
>>> colors = prims.get_colors(indices=[0, 2])
>>> colors.shape
(2, 3)
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

get_enabled_color_temperatures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the use of color temperatures is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the use of color temperatures enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_color_temperatures([True], indices=[1])
>>> print(prims.get_enabled_color_temperatures())
[[False]
[ True]
[False]]
```

get_enabled_normalizations(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the power normalization is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the power normalization enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_normalizations([True], indices=[1])
>>> print(prims.get_enabled_normalizations())
[[False]
[ True]
[False]]
```

get_enabled_treat_as_points(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the treat as points (effectively, a zero-radius sphere) of the prims.
Backends: usd.
Warning
Renderers that do not support non-area lighting can ignore this.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if treat as points is enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the treat as points enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_treat_as_points([True], indices=[1])
>>> print(prims.get_enabled_treat_as_points())
[[False]
[ True]
[False]]
```

get_exposures(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The exposures (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the exposures of all prims
>>> exposures = prims.get_exposures()
>>> exposures.shape
(3, 1)
>>>
>>> # get the exposures of the first and last prim
>>> exposures = prims.get_exposures(indices=[0, 2])
>>> exposures.shape
(2, 1)
```

get_intensities(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The intensities (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the intensities of all prims
>>> intensities = prims.get_intensities()
>>> intensities.shape
(3, 1)
>>>
>>> # get the intensities of the first and last prims
>>> intensities = prims.get_intensities(indices=[0, 2])
>>> intensities.shape
(2, 1)
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

get_multipliers(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The diffuse multipliers (shape `(N, 1)`). 2) The specular multipliers (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the multipliers of all prims
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers()
>>> diffuse_multipliers.shape, specular_multipliers.shape
((3, 1), (3, 1))
>>>
>>> # get the multipliers of the first and last prim
>>> diffuse_multipliers, specular_multipliers = prims.get_multipliers(indices=[0, 2])
>>> diffuse_multipliers.shape, specular_multipliers.shape
((2, 1), (2, 1))
```

get_radii(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the radii of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The radii (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the radii of all prims
>>> radii = prims.get_radii()
>>> radii.shape
(3, 1)
>>>
>>> # get the radii of the first and last prims
>>> radii = prims.get_radii(indices=[0, 2])
>>> radii.shape
(2, 1)
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

set_color_temperatures(
color_temperatures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
The valid range is from 1000 to 10000, where D65 (~6500 K) is the standard white point (lower values are warmer and higher values are cooler). The values only take effect when `enableColorTemperature` is set to true (see set_enabled_color_temperatures() ).
Parameters:

- color_temperatures – Color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same color temperatures for all prims
>>> prims.set_color_temperatures([8000])
>>>
>>> # set only the color temperature for the second prim
>>> prims.set_color_temperatures([5000], indices=[1])
```

set_colors(
colors:list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the color (normalized RGB) of emitted light (in energy-linear terms) of the prims.
Backends: usd.
Parameters:

- colors – Colors (shape `(N, 3)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same colors (red) for all prims
>>> prims.set_colors([1.0, 0.0, 0.0])
>>>
>>> # set only the color (green) for the second prim
>>> prims.set_colors([0.0, 1.0, 0.0], indices=[1])
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

set_enabled_color_temperatures(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the use of color temperatures (in degrees Kelvin) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable color temperatures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the use of color temperatures for all prims
>>> prims.set_enabled_color_temperatures([True])
>>>
>>> # disable the use of color temperatures for the first and last prims
>>> prims.set_enabled_color_temperatures([False], indices=[0, 2])
```

set_enabled_normalizations(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the power normalization (by the surface area of the light) of the prims.
Backends: usd.
Parameters:

- enabled – Boolean flags to enable/disable power normalization (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the power normalization for all prims
>>> prims.set_enabled_normalizations([True])
>>>
>>> # disable the power normalization for the first and last prims
>>> prims.set_enabled_normalizations([False], indices=[0, 2])
```

set_enabled_treat_as_points(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the treat as points (effectively, a zero-radius sphere) of the prims.
Backends: usd.
Warning
Renderers that do not support non-area lighting can ignore this.
Parameters:

- enabled – Boolean flags to enable/disable treat as points (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the treat as points for all prims
>>> prims.set_enabled_treat_as_points([True])
>>>
>>> # disable the treat as points for the first and last prims
>>> prims.set_enabled_treat_as_points([False], indices=[0, 2])
```

set_exposures(
exposures:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the exposures (scale light power exponentially as a power of 2) of the prims.
Backends: usd.
The result is multiplied against the intensity of the light.
Parameters:

- exposures – Exposures (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same exposures for all prims
>>> prims.set_exposures(exposures=[10])
>>>
>>> # set only the exposure for the second prim
>>> prims.set_exposures(exposures=[100], indices=[1])
```

set_intensities(
intensities:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the intensities (scale light power linearly) of the prims.
Backends: usd.
Parameters:

- intensities – Intensities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same intensities for all prims
>>> prims.set_intensities(intensities=[1000])
>>>
>>> # set only the intensity for the second prim
>>> prims.set_intensities(intensities=[1500], indices=[1])
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

set_multipliers(
diffuse_multipliers:float|list|np.ndarray|wp.array=None,
specular_multipliers:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the multipliers (for the effect on the diffuse and specular response of materials) of the prims.
Backends: usd.
Parameters:

- diffuse_multipliers – Diffuse multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- specular_multipliers – Specular multipliers (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither diffuse_multipliers nor specular_multipliers are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same multipliers for all prims
>>> prims.set_multipliers(diffuse_multipliers=[0.5], specular_multipliers=[0.1])
>>>
>>> # set only the specular multiplier for the second prim
>>> prims.set_multipliers(specular_multipliers=[0.2], indices=[1])
```

set_radii(
radii:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the radii of the prims.
Backends: usd.
Parameters:

- radii – Radii (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same radii for all prims
>>> prims.set_radii(radii=[0.1])
>>>
>>> # set only the radius for the second prim
>>> prims.set_radii(radii=[0.2], indices=[1])
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

propertylights:list[pxr.UsdLux.Light]
USD Light encapsulated by the wrapper.
Returns:
List of USD Light.

Example:

```
>>> prims.lights
[UsdLux.Light(Usd.Prim(</World/prim_0>)),
UsdLux.Light(Usd.Prim(</World/prim_1>)),
UsdLux.Light(Usd.Prim(</World/prim_2>))]
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
