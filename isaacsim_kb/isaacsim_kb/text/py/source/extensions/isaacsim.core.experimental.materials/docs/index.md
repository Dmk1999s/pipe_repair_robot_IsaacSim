<!-- source: py/source/extensions/isaacsim.core.experimental.materials/docs/index.html | title: [isaacsim.core.experimental.materials] Isaac Sim Core (Materials) — Isaac Sim -->

# [isaacsim.core.experimental.materials] Isaac Sim Core (Materials)
Version: 0.4.0
The Core Materials extension provides a set of APIs to create and/or wrap one or more USD materials in the stage…

## Enable Extension
The extension can be enabled (if not already) in one of the following ways:

## API
Warning
The API featured in this extension is experimental and subject to change without deprecation cycles. Although we will try to maintain backward compatibility in the event of a change, it may not always be possible.

### Python API
The following table summarizes the available materials.
physics materials

[TABLE]
PhysicsMaterial | Base class for physics materials.
RigidBodyMaterial | High level wrapper for creating/encapsulating Rigid Body material prims.
SurfaceDeformableMaterial | High level wrapper for creating/encapsulating Surface Deformable material prims.
VolumeDeformableMaterial | High level wrapper for creating/encapsulating Volume Deformable material prims.
[/TABLE]
visual materials

[TABLE]
OmniGlassMaterial | High level wrapper for creating/encapsulating Omniverse Glass ( OmniGlass ) material prims.
OmniPbrMaterial | High level wrapper for creating/encapsulating Omniverse Physically-Based Rendering ( OmniPBR ) material prims.
PreviewSurfaceMaterial | High level wrapper for creating/encapsulating USD Preview Surface ( UsdPreviewSurface ) material prims.
VisualMaterial | Base class for visual materials.
[/TABLE]

#### Materials

##### Physics Materials
classPhysicsMaterial(paths:str|list[str], *, resolve_paths:bool=True)
Bases: Prim , `ABC`
Base class for physics materials.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

abstractstaticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

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
)→list[PhysicsMaterial |None ]Fetch instances of physics material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get physics material instances from.

Returns:
List of physics material instances or `None` if the prim is not a supported physics material type.

Example:

```
>>> import omni.kit.commands
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.materials import PhysicsMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "AddRigidBodyMaterialCommand", stage=stage_utils.get_current_stage(), path="/World/A"
... )
>>>
>>> # fetch physics material instances
>>> PhysicsMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.physics_materials.rigid_body.RigidBodyMaterial object at 0x...>]
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

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

classRigidBodyMaterial(
paths:str|list[str],
*,
static_frictions:float|list|np.ndarray|wp.array|None =None,
dynamic_frictions:float|list|np.ndarray|wp.array|None =None,
restitutions:float|list|np.ndarray|wp.array|None =None,
densities:float|list|np.ndarray|wp.array|None =None,
)Bases: PhysicsMaterial
High level wrapper for creating/encapsulating Rigid Body material prims.
Note
This class creates or wraps (one of both) Rigid Body material prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the Rigid Body material prims.

- If the prim paths do not exist, Rigid Body material prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- static_frictions – Static friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- restitutions – Restitution coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- densities – Densities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

Raises:
ValueError – If resulting paths are mixed or invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import RigidBodyMaterial
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create rigid body material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = RigidBodyMaterial(paths)
```
staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = RigidBodyMaterial.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[[False]
[ True]]
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
)→list[PhysicsMaterial |None ]Fetch instances of physics material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get physics material instances from.

Returns:
List of physics material instances or `None` if the prim is not a supported physics material type.

Example:

```
>>> import omni.kit.commands
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.materials import PhysicsMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "AddRigidBodyMaterialCommand", stage=stage_utils.get_current_stage(), path="/World/A"
... )
>>>
>>> # fetch physics material instances
>>> PhysicsMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.physics_materials.rigid_body.RigidBodyMaterial object at 0x...>]
```

get_combine_modes(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[list[Literal['average','max','min','multiply']],list[Literal['average','max','min','multiply']],list[Literal['average','max','min','multiply']]]Get the way two material properties will be combined to yield a coefficient for a collision.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Three-elements tuple. 1) The friction combine modes (shape `(N,)`). 2) The restitution combine modes (shape `(N,)`). 3) The damping combine modes (shape `(N,)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the combine modes of all prims
>>> frictions, restitutions, dampings = prims.get_combine_modes()
>>> frictions
['average', 'average', 'average']
>>> restitutions
['average', 'average', 'average']
>>> dampings
['average', 'average', 'average']
```

get_compliant_contact_gains(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the compliant contact gains (stiffnesses and dampings) of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The stiffnesses (shape `(N, 1)`). 2) The dampings (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the compliant contact gains of all prims
>>> stiffnesses, dampings = prims.get_compliant_contact_gains()
>>> stiffnesses.shape, dampings.shape
((3, 1), (3, 1))
>>>
>>> # get the compliant contact gains of the first and last prims
>>> stiffnesses, dampings = prims.get_compliant_contact_gains(indices=[0, 2])
>>> stiffnesses.shape, dampings.shape
((2, 1), (2, 1))
```

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
>>> # get the densities of the first and last prims
>>> densities = prims.get_densities(indices=[0, 2])
>>> densities.shape
(2, 1)
```

get_enabled_compliant_contacts(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the enabled state of the compliant spring-damper contact effects of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Boolean flags indicating if the compliant contact effects are enabled (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the compliant contact enabled state of all prims after enabling it for the second prim
>>> prims.set_enabled_compliant_contacts([True], indices=[1])
>>> print(prims.get_enabled_compliant_contacts())
[[False]
[ True]
[False]]
```

get_friction_coefficients(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the friction coefficients of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The static friction coefficients (shape `(N, 1)`). 2) The dynamic friction coefficients (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the friction coefficients of all prims
>>> static_frictions, dynamic_frictions = prims.get_friction_coefficients()
>>> static_frictions.shape, dynamic_frictions.shape
((3, 1), (3, 1))
>>>
>>> # get the friction coefficients of the first and last prims
>>> static_frictions, dynamic_frictions = prims.get_friction_coefficients(indices=[0, 2])
>>> static_frictions.shape, dynamic_frictions.shape
((2, 1), (2, 1))
```

get_restitution_coefficients(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the restitution coefficients of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The restitution coefficients (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the restitution coefficients of all prims
>>> restitutions = prims.get_restitution_coefficients()
>>> restitutions.shape
(3, 1)
>>>
>>> # get the restitution coefficients of the first and last prims
>>> restitutions = prims.get_restitution_coefficients(indices=[0, 2])
>>> restitutions.shape
(2, 1)
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

set_combine_modes(
frictions:Literal['average','max','min','multiply']|list[Literal['average','max','min','multiply']]|None =None,
restitutions:Literal['average','max','min','multiply']|list[Literal['average','max','min','multiply']]|None =None,
dampings:Literal['average','max','min','multiply']|list[Literal['average','max','min','multiply']]|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the way two material properties will be combined to yield a coefficient for a collision.
Backends: usd.
Parameters:

- frictions – Friction combine modes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- restitutions – Restitution combine modes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dampings – Damping combine modes (shape `(N,)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules). This argument is only relevant for compliant contact interactions.

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither frictions, restitutions nor dampings are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set the combine modes (frictions: 'average', restitutions: 'max', dampings: 'min') for all prims
>>> prims.set_combine_modes(frictions=["average"], restitutions=["max"], dampings=["min"])
```

set_compliant_contact_gains(
stiffnesses:float|list|np.ndarray|wp.array|None =None,
dampings:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the compliant contact gains (stiffnesses and dampings) of the prims.
Backends: usd.
Warning
The spring stiffnesses must be set to a value greater than 0 before enabling compliant contact effects.
Parameters:

- stiffnesses – Stiffnesses (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dampings – Dampings (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither stiffnesses nor dampings are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same compliant contact gains (stiffnesses: 100.0, dampings: 10.0) for all prims
>>> prims.set_compliant_contact_gains(stiffnesses=[100.0], dampings=[10.0])
>>>
>>> # set only the damping for the second prim
>>> prims.set_compliant_contact_gains(dampings=[15.0], indices=[1])
```

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
>>> # set same densities for all prims
>>> prims.set_densities(densities=[1000])
>>>
>>> # set only the density for the second prim
>>> prims.set_densities(densities=[1500], indices=[1])
```

set_enabled_compliant_contacts(
enabled:bool|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Enable or disable the compliant spring-damper contact effects of the prims.
Backends: usd.
Warning
The spring stiffnesses (see set_compliant_contact_gains() ) must be set to a value greater than 0 before enabling compliant contact effects.
Parameters:

- enabled – Boolean flags to enable/disable compliant contact effects (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # enable the compliant contact effects for all prims
>>> prims.set_enabled_compliant_contacts([True])
>>>
>>> # disable the compliant contact effects for the first and last prims
>>> prims.set_enabled_compliant_contacts([False], indices=[0, 2])
```

set_friction_coefficients(
static_frictions:float|list|np.ndarray|wp.array=None,
dynamic_frictions:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the friction coefficients of the prims.
Backends: usd.
Parameters:

- static_frictions – Static friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither static_frictions nor dynamic_frictions are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same friction coefficients (static: 0.5, dynamic: 0.2) for all prims
>>> prims.set_friction_coefficients(static_frictions=[0.5], dynamic_frictions=[0.2])
>>>
>>> # set only the dynamic friction coefficient for the second prim
>>> prims.set_friction_coefficients(dynamic_frictions=[0.3], indices=[1])
```

set_restitution_coefficients(
restitutions:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the restitution coefficients of the prims.
Backends: usd.
Parameters:

- restitutions – Restitution coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same restitution coefficients for all prims
>>> prims.set_restitution_coefficients(restitutions=[0.005])
>>>
>>> # set only the restitution coefficient for the second prim
>>> prims.set_restitution_coefficients(restitutions=[0.002], indices=[1])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

classSurfaceDeformableMaterial(
paths:str|list[str],
*,
static_frictions:float|list|np.ndarray|wp.array|None =None,
dynamic_frictions:float|list|np.ndarray|wp.array|None =None,
youngs_moduli:float|list|np.ndarray|wp.array|None =None,
poissons_ratios:float|list|np.ndarray|wp.array|None =None,
densities:float|list|np.ndarray|wp.array|None =None,
)Bases: PhysicsMaterial
High level wrapper for creating/encapsulating Surface Deformable material prims.
Warning
The deformable materials require the Deformable feature (beta) to be enabled. Deformable feature (beta) can be enabled in apps/.kit experience files by setting `physics.enableDeformableBeta = true` under the `[settings.persistent]` section.
Note
This class creates or wraps (one of both) Surface Deformable material prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the Surface Deformable material prims.

- If the prim paths do not exist, Surface Deformable material prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- static_frictions – Static friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- youngs_moduli – Young’s moduli (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- poissons_ratios – Poisson’s ratios (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- densities – Densities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

Raises:

- RuntimeError – If the Deformable feature (beta) is disabled.

- ValueError – If material type is invalid.

- ValueError – If resulting paths are mixed or invalid.

- AssertionError – If the created/wrapped prims are not valid USD Materials.

Example:

```
>>> from isaacsim.core.experimental.materials import SurfaceDeformableMaterial
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create surface deformable material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = SurfaceDeformableMaterial(paths)
```
staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = SurfaceDeformableMaterial.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[[False]
[ True]]
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
)→list[PhysicsMaterial |None ]Fetch instances of physics material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get physics material instances from.

Returns:
List of physics material instances or `None` if the prim is not a supported physics material type.

Example:

```
>>> import omni.kit.commands
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.materials import PhysicsMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "AddRigidBodyMaterialCommand", stage=stage_utils.get_current_stage(), path="/World/A"
... )
>>>
>>> # fetch physics material instances
>>> PhysicsMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.physics_materials.rigid_body.RigidBodyMaterial object at 0x...>]
```

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
>>> # get the densities of the first and last prims
>>> densities = prims.get_densities(indices=[0, 2])
>>> densities.shape
(2, 1)
```

get_friction_coefficients(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the friction coefficients of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The static friction coefficients (shape `(N, 1)`). 2) The dynamic friction coefficients (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the friction coefficients of all prims
>>> static_frictions, dynamic_frictions = prims.get_friction_coefficients()
>>> static_frictions.shape, dynamic_frictions.shape
((3, 1), (3, 1))
>>>
>>> # get the friction coefficients of the first and last prims
>>> static_frictions, dynamic_frictions = prims.get_friction_coefficients(indices=[0, 2])
>>> static_frictions.shape, dynamic_frictions.shape
((2, 1), (2, 1))
```

get_poissons_ratios(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the Poisson’s ratios of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The Poisson’s ratios (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the Poisson's ratios of all prims
>>> ratios = prims.get_poissons_ratios()
>>> ratios.shape
(3, 1)
>>>
>>> # get the Poisson's ratios of the first and last prims
>>> ratios = prims.get_poissons_ratios(indices=[0, 2])
>>> ratios.shape
(2, 1)
```

get_surface_stiffnesses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array,wp.array]Get the surface stretch, shear and bend stiffnesses of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Three-elements tuple. 1) The surface stretch stiffnesses (shape `(N, 1)`). 2) The surface shear stiffnesses (shape `(N, 1)`). 3) The surface bend stiffnesses (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the surface stiffnesses of all prims
>>> stretch_stiffnesses, shear_stiffnesses, bend_stiffnesses = prims.get_surface_stiffnesses()
>>> stretch_stiffnesses.shape, shear_stiffnesses.shape, bend_stiffnesses.shape
((3, 1), (3, 1), (3, 1))
>>>
>>> # get the surface stiffnesses of the second prim
>>> stretch_stiffnesses, shear_stiffnesses, bend_stiffnesses = prims.get_surface_stiffnesses(indices=[1])
>>> stretch_stiffnesses.shape, shear_stiffnesses.shape, bend_stiffnesses.shape
((1, 1), (1, 1), (1, 1))
```

get_surface_thicknesses(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the surface thicknesses of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The surface thicknesses (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the surface thicknesses of all prims
>>> surface_thicknesses = prims.get_surface_thicknesses()
>>> surface_thicknesses.shape
(3, 1)
>>>
>>> # get the surface thicknesses of the first and last prims
>>> surface_thicknesses = prims.get_surface_thicknesses(indices=[0, 2])
>>> surface_thicknesses.shape
(2, 1)
```

get_youngs_moduli(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the Young’s moduli of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The Young’s moduli (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the Young's moduli of all prims
>>> moduli = prims.get_youngs_moduli()
>>> moduli.shape
(3, 1)
>>>
>>> # get the Young's moduli of the first and last prims
>>> moduli = prims.get_youngs_moduli(indices=[0, 2])
>>> moduli.shape
(2, 1)
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
>>> # set same densities for all prims
>>> prims.set_densities(densities=[1000])
>>>
>>> # set only the density for the second prim
>>> prims.set_densities(densities=[1500], indices=[1])
```

set_friction_coefficients(
static_frictions:float|list|np.ndarray|wp.array=None,
dynamic_frictions:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the friction coefficients of the prims.
Backends: usd.
Parameters:

- static_frictions – Static friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither static_frictions nor dynamic_frictions are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same friction coefficients (static: 0.5, dynamic: 0.2) for all prims
>>> prims.set_friction_coefficients(static_frictions=[0.5], dynamic_frictions=[0.2])
>>>
>>> # set only the dynamic friction coefficient for the second prim
>>> prims.set_friction_coefficients(dynamic_frictions=[0.3], indices=[1])
```

set_poissons_ratios(
poissons_ratios:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the Poisson’s ratio of the prims.
Backends: usd.
Parameters:

- poissons_ratios – Poisson’s ratios (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same Poisson's ratio for all prims
>>> prims.set_poissons_ratios(poissons_ratios=[0.45])
>>>
>>> # set only the Poisson's ratio for the second prim
>>> prims.set_poissons_ratios(poissons_ratios=[0.4], indices=[1])
```

set_surface_stiffnesses(
stretch_stiffnesses:float|list|np.ndarray|wp.array|None =None,
shear_stiffnesses:float|list|np.ndarray|wp.array|None =None,
bend_stiffnesses:float|list|np.ndarray|wp.array|None =None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the surface stretch, shear and bend stiffness of the prims.
Backends: usd.
Parameters:

- stretch_stiffnesses – Surface stretch stiffnesses (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- shear_stiffnesses – Surface shear stiffnesses (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- bend_stiffnesses – Surface bend stiffnesses (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither stretch_stiffnesses nor shear_stiffnesses nor bend_stiffnesses are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same surface stiffnesses (stretch: 1000, shear: 100, bend: 10) for all prims
>>> prims.set_surface_stiffnesses(stretch_stiffnesses=[1000], shear_stiffnesses=[100], bend_stiffnesses=[10])
>>>
>>> # set only the surface stiffnesses for the second prim
>>> prims.set_surface_stiffnesses(
... stretch_stiffnesses=[1500], shear_stiffnesses=[150], bend_stiffnesses=[15], indices=[1]
... )
```

set_surface_thicknesses(
surface_thicknesses:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the surface thicknesses of the prims.
Backends: usd.
Parameters:

- surface_thicknesses – Surface thicknesses (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same surface thicknesses for all prims
>>> prims.set_surface_thicknesses(surface_thicknesses=[0.001])
>>>
>>> # set only the surface thickness for the second prim
>>> prims.set_surface_thicknesses(surface_thicknesses=[0.002], indices=[1])
```

set_youngs_moduli(
youngs_moduli:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the Young’s modulus of the prims.
Backends: usd.
Parameters:

- youngs_moduli – Young’s moduli (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same Young's modulus for all prims
>>> prims.set_youngs_moduli(youngs_moduli=[500000.0])
>>>
>>> # set only the Young's modulus for the second prim
>>> prims.set_youngs_moduli(youngs_moduli=[600000.0], indices=[1])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

classVolumeDeformableMaterial(
paths:str|list[str],
*,
static_frictions:float|list|np.ndarray|wp.array|None =None,
dynamic_frictions:float|list|np.ndarray|wp.array|None =None,
youngs_moduli:float|list|np.ndarray|wp.array|None =None,
poissons_ratios:float|list|np.ndarray|wp.array|None =None,
densities:float|list|np.ndarray|wp.array|None =None,
)Bases: PhysicsMaterial
High level wrapper for creating/encapsulating Volume Deformable material prims.
Warning
The deformable materials require the Deformable feature (beta) to be enabled. Deformable feature (beta) can be enabled in apps/.kit experience files by setting `physics.enableDeformableBeta = true` under the `[settings.persistent]` section.
Note
This class creates or wraps (one of both) Volume Deformable material prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the Volume Deformable material prims.

- If the prim paths do not exist, Volume Deformable material prims are created at each path and a wrapper is placed over them.

Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- static_frictions – Static friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- youngs_moduli – Young’s moduli (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- poissons_ratios – Poisson’s ratios (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- densities – Densities (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

Raises:

- RuntimeError – If the Deformable feature (beta) is disabled.

- ValueError – If material type is invalid.

- ValueError – If resulting paths are mixed or invalid.

- AssertionError – If the created/wrapped prims are not valid USD Materials.

Example:

```
>>> from isaacsim.core.experimental.materials import VolumeDeformableMaterial
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create volume deformable material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = VolumeDeformableMaterial(paths)
```
staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = VolumeDeformableMaterial.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[[False]
[ True]]
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
)→list[PhysicsMaterial |None ]Fetch instances of physics material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get physics material instances from.

Returns:
List of physics material instances or `None` if the prim is not a supported physics material type.

Example:

```
>>> import omni.kit.commands
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.core.experimental.materials import PhysicsMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "AddRigidBodyMaterialCommand", stage=stage_utils.get_current_stage(), path="/World/A"
... )
>>>
>>> # fetch physics material instances
>>> PhysicsMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.physics_materials.rigid_body.RigidBodyMaterial object at 0x...>]
```

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
>>> # get the densities of the first and last prims
>>> densities = prims.get_densities(indices=[0, 2])
>>> densities.shape
(2, 1)
```

get_friction_coefficients(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→tuple[wp.array,wp.array]Get the friction coefficients of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Two-elements tuple. 1) The static friction coefficients (shape `(N, 1)`). 2) The dynamic friction coefficients (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the friction coefficients of all prims
>>> static_frictions, dynamic_frictions = prims.get_friction_coefficients()
>>> static_frictions.shape, dynamic_frictions.shape
((3, 1), (3, 1))
>>>
>>> # get the friction coefficients of the first and last prims
>>> static_frictions, dynamic_frictions = prims.get_friction_coefficients(indices=[0, 2])
>>> static_frictions.shape, dynamic_frictions.shape
((2, 1), (2, 1))
```

get_poissons_ratios(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the Poisson’s ratios of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The Poisson’s ratios (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the Poisson's ratios of all prims
>>> ratios = prims.get_poissons_ratios()
>>> ratios.shape
(3, 1)
>>>
>>> # get the Poisson's ratios of the first and last prims
>>> ratios = prims.get_poissons_ratios(indices=[0, 2])
>>> ratios.shape
(2, 1)
```

get_youngs_moduli(
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet the Young’s moduli of the prims.
Backends: usd.
Parameters:
indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
The Young’s moduli (shape `(N, 1)`).

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # get the Young's moduli of all prims
>>> moduli = prims.get_youngs_moduli()
>>> moduli.shape
(3, 1)
>>>
>>> # get the Young's moduli of the first and last prims
>>> moduli = prims.get_youngs_moduli(indices=[0, 2])
>>> moduli.shape
(2, 1)
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
>>> # set same densities for all prims
>>> prims.set_densities(densities=[1000])
>>>
>>> # set only the density for the second prim
>>> prims.set_densities(densities=[1500], indices=[1])
```

set_friction_coefficients(
static_frictions:float|list|np.ndarray|wp.array=None,
dynamic_frictions:float|list|np.ndarray|wp.array=None,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the friction coefficients of the prims.
Backends: usd.
Parameters:

- static_frictions – Static friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- dynamic_frictions – Dynamic friction coefficients (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – If neither static_frictions nor dynamic_frictions are specified.

- AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same friction coefficients (static: 0.5, dynamic: 0.2) for all prims
>>> prims.set_friction_coefficients(static_frictions=[0.5], dynamic_frictions=[0.2])
>>>
>>> # set only the dynamic friction coefficient for the second prim
>>> prims.set_friction_coefficients(dynamic_frictions=[0.3], indices=[1])
```

set_poissons_ratios(
poissons_ratios:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the Poisson’s ratio of the prims.
Backends: usd.
Parameters:

- poissons_ratios – Poisson’s ratios (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same Poisson's ratio for all prims
>>> prims.set_poissons_ratios(poissons_ratios=[0.45])
>>>
>>> # set only the Poisson's ratio for the second prim
>>> prims.set_poissons_ratios(poissons_ratios=[0.4], indices=[1])
```

set_youngs_moduli(
youngs_moduli:float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set the Young’s modulus of the prims.
Backends: usd.
Parameters:

- youngs_moduli – Young’s moduli (shape `(N, 1)`). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:
AssertionError – Wrapped prims are not valid.

Example:

```
>>> # set same Young's modulus for all prims
>>> prims.set_youngs_moduli(youngs_moduli=[500000.0])
>>>
>>> # set only the Young's modulus for the second prim
>>> prims.set_youngs_moduli(youngs_moduli=[600000.0], indices=[1])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

##### Visual Materials
classOmniGlassMaterial(paths:str|list[str])
Bases: VisualMaterial
High level wrapper for creating/encapsulating Omniverse Glass (`OmniGlass`) material prims.
The `OmniGlass` is an improved physical glass model that simulates light transmission through thin walled and transmissive surfaces.
Note
This class creates or wraps (one of both) OmniGlass prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the OmniGlass prims.

- If the prim paths do not exist, OmniGlass prims are created at each path and a wrapper is placed over them.

On visual materials, the shader parameters are encoded as inputs. The following tables summarize the `OmniGlass` material shader inputs (by group):

[TABLE]
Input name | Description | Shape / Length | Type
"glass_color" | Color of the glass. | (N, 3) | float
"glass_color_texture" | Texture to be used for the glass color. | (N,) | str
"depth" | Volume absorption scale (control how much light is absorbed through the surface). | (N, 1) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"frosting_roughness" | Roughness of the glass material. | (N, 1) | float
"roughness_texture_influence" | Influence of the roughness texture on the glass material. | (N, 1) | float
"roughness_texture" | Roughness texture. | (N,) | str
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"glass_ior" | Glass Index of refraction (IOR). | (N, 1) | float
"thin_walled" | Whether the glass is thin-walled (when enabled, the material is considered thin-walled). | (N, 1) | bool
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"reflection_color_texture" | Reflection color texture. | (N,) | str
"reflection_color" | Reflection color. | (N, 3) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"normal_map_texture" | Normal map texture. | (N,) | str
"normal_map_strength" | Strength of the normal map. | (N, 1) | float
"geometry_normal_roughness_strength" | Normal map to roughness weight (enables and weights roughness induced by normal maps). | (N, 1) | float
"flip_tangent_u" | Flip tangent U. | (N, 1) | bool
"flip_tangent_v" | Flip tangent V. | (N, 1) | bool
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"enable_opacity" | Enable the use of cutout opacity. | (N, 1) | bool
"cutout_opacity" | Opacity value between 0.0 and 1.0, when opacity map is not valid. | (N, 1) | float
"cutout_opacity_texture" | Opacity map. | (N,) | str
"cutout_opacity_mono_source" | Determines how to lookup opacity from the supplied texture. | (N, 1) | int
"opacity_threshold" | Opacity threshold. | (N, 1) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"project_uvw" | Enable Project UVW Coordinates (UV coordinates will be generated by projecting them from a coordinate system). | (N, 1) | bool
"world_or_object" | Enable world space (when enabled, uses world space for projection, otherwise object space is used). | (N, 1) | bool
"uv_space_index" | UV space index. | (N, 1) | int
"texture_translate" | Controls position of texture. | (N, 2) | float
"texture_rotate" | Rotates angle of texture (in degrees). | (N, 1) | float
"texture_scale" | Controls the repetition of the texture. | (N, 2) | float
[/TABLE]
Parameters:
paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

Raises:
ValueError – If resulting paths are mixed or invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create visual material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = OmniGlassMaterial(paths)
```
staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = OmniGlassMaterial.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[[False]
[ True]]
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
)→list[VisualMaterial |None ]Fetch instances of visual material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get visual material instances from.

Returns:
List of visual material instances or `None` if the prim is not a supported visual material type.

Example:

```
>>> import omni.kit.commands
>>> from isaacsim.core.experimental.materials import VisualMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "CreatePreviewSurfaceMaterialPrim",
... mtl_path=f"/World/A",
... select_new_prim=False,
... )
>>>
>>> # fetch visual material instances
>>> VisualMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.visual_materials.preview_surface.PreviewSurfaceMaterial object at 0x...>]
```

get_input_values(
name:str,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet shaders’ input values.
Warning
Inputs are not initialized by default. They must be initialized before being read (see set_input_values() ).
Parameters:

- name – Shader input name.

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Values (shape and data type depend on the input name).

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

- RuntimeError – If the shader input is not initialized.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # get the glass IOR of all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_ior", values=[1.5])
... glass_ior = prims.get_input_values(name="glass_ior")
>>>
>>> # get the metallic amount of all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="metallic_constant", values=[0.5])
... metallic_constant = prims.get_input_values(name="metallic_constant")
>>>
>>> # get the opacity of all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="opacity", values=[0.1])
... opacity = prims.get_input_values(name="opacity")
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

set_input_values(
name:str,
values:str|bool|int|float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set shaders’ input values.
Parameters:

- name – Shader input name.

- values – Input values (shape and data type depend on the input name). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # set same glass color (green) for all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_color", values=[0.0, 1.0, 0.0])
>>>
>>> # set the Albedo map (textures) for all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="diffuse_texture", values=[
... "/local/path/to/texture_0",
... "/local/path/to/texture_1",
... "/local/path/to/texture_2",
... ])
>>>
>>> # set same diffuse color (red) for all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="diffuseColor", values=[1.0, 0.0, 0.0])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

propertyshaders:list[pxr.UsdShade.Shader]
USD shaders encapsulated by the wrapper.
Returns:
List of USD shaders.

Example:

```
>>> prims.shaders
[UsdShade.Shader(Usd.Prim(</World/prim_0/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_1/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_2/Shader>))]
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

classOmniPbrMaterial(paths:str|list[str])
Bases: VisualMaterial
High level wrapper for creating/encapsulating Omniverse Physically-Based Rendering (`OmniPBR`) material prims.
The `OmniPBR` is the default Physically based material available in Omniverse. This material can describe most opaque dielectric or non-dielectric materials.
Note
This class creates or wraps (one of both) OmniPBR prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the OmniPBR prims.

- If the prim paths do not exist, OmniPBR prims are created at each path and a wrapper is placed over them.

On visual materials, the shader parameters are encoded as inputs. The following tables summarize the `OmniPBR` material shader inputs (by group):

[TABLE]
Input name | Description | Shape / Length | Type
"diffuse_color_constant" | Albedo base color. | (N, 3) | float
"diffuse_texture" | Albedo map. | (N,) | str
"albedo_desaturation" | Albedo map desaturation. | (N, 1) | float
"albedo_add" | Adds constant value to the diffuse color. | (N, 1) | float
"albedo_brightness" | Multiplier for the diffuse color. | (N, 1) | float
"diffuse_tint" | Color tint (when enabled, this color value is multiplied over the final albedo color). | (N, 3) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"reflection_roughness_constant" | Roughness amount (Higher values lead to more blurry reflections). | (N, 1) | float
"reflection_roughness_texture_influence" | Roughness map influence (blends between the constant value and the lookup of the roughness texture). | (N, 1) | float
"reflectionroughness_texture" | Roughness map. | (N,) | str
"metallic_constant" | Metallic amount. | (N, 1) | float
"metallic_texture_influence" | Metallic map influence (blends between the constant value and the lookup of the metallic texture). | (N, 1) | float
"metallic_texture" | Metallic map. | (N,) | str
"specular_level" | Specular level (intensity) of the material. | (N, 1) | float
"enable_ORM_texture" | Enable ORM texture (extracts occlusion, roughness and metallic textures from the RGB channels). | (N, 1) | bool
"ORM_texture" | ORM map (texture that has occlusion, roughness and metallic maps stored in the RGB channels). | (N,) | str
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"ao_to_diffuse" | AO to diffuse (amount of ambient occlusion multiplied against the diffuse color channel). | (N, 1) | float
"ao_texture" | Ambient occlusion map (texture for the material). | (N,) | str
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"enable_emission" | Enable emission (enables the emission of light from the material). | (N, 1) | bool
"emissive_color" | Emission color. | (N, 3) | float
"emissive_color_texture" | Emission color map. | (N,) | str
"emissive_mask_texture" | Emission color mask map. | (N,) | str
"emissive_intensity" | Emission intensity. | (N, 1) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"enable_opacity" | Enable the use of cutout opacity. | (N, 1) | bool
"opacity_texture" | Opacity map. | (N,) | str
"opacity_constant" | Opacity amount (between 0.0 and 1.0, when opacity map is not valid). | (N, 1) | float
"enable_opacity_texture" | Enable or disable the usage of the opacity texture map. | (N, 1) | bool
"opacity_mode" | Determines how to lookup opacity from the supplied texture. | (N, 1) | int
"opacity_threshold" | Opacity threshold (between 0.0 and 1.0). | (N, 1) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"geometry_normal_roughness_strength" | Normal map to roughness weight (enables and weights roughness induced by normal maps). | (N, 1) | float
"bump_factor" | Normal strength. | (N, 1) | float
"normalmap_texture" | Normal map. | (N,) | str
"detail_bump_factor" | Detail normal strength. | (N, 1) | float
"detail_normalmap_texture" | Detail normal map. | (N,) | str
"flip_tangent_u" | Flip tangent U. | (N, 1) | bool
"flip_tangent_v" | Flip tangent V. | (N, 1) | bool
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"project_uvw" | Enable Project UVW Coordinates (UV coordinates will be generated by projecting them from a coordinate system). | (N, 1) | bool
"world_or_object" | Enable world space (when enabled, uses world space for projection, otherwise object space is used). | (N, 1) | bool
"uv_space_index" | UV space index. | (N, 1) | int
"texture_translate" | Controls position of texture. | (N, 2) | float
"texture_rotate" | Rotates angle of texture (in degrees). | (N, 1) | float
"texture_scale" | Controls the repetition of the texture. | (N, 2) | float
"detail_texture_translate" | Controls the position of the detail texture. | (N, 2) | float
"detail_texture_rotate" | Rotates angle of the detail texture (in degrees). | (N, 1) | float
"detail_texture_scale" | Controls the repetition of the detail texture. | (N, 2) | float
[/TABLE]

[TABLE]
Input name | Description | Shape / Length | Type
"round_edges_radius" | Influence radius around the edges (in meters). | (N, 1) | float
"round_edges_roundness" | Determines how round the edge will look. | (N, 1) | float
"round_edges_across_materials" | Round edge across materials. | (N, 1) | bool
[/TABLE]
Parameters:
paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

Raises:
ValueError – If resulting paths are mixed or invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniPbrMaterial
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create visual material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = OmniPbrMaterial(paths)
```
staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = OmniPbrMaterial.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[[False]
[ True]]
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
)→list[VisualMaterial |None ]Fetch instances of visual material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get visual material instances from.

Returns:
List of visual material instances or `None` if the prim is not a supported visual material type.

Example:

```
>>> import omni.kit.commands
>>> from isaacsim.core.experimental.materials import VisualMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "CreatePreviewSurfaceMaterialPrim",
... mtl_path=f"/World/A",
... select_new_prim=False,
... )
>>>
>>> # fetch visual material instances
>>> VisualMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.visual_materials.preview_surface.PreviewSurfaceMaterial object at 0x...>]
```

get_input_values(
name:str,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet shaders’ input values.
Warning
Inputs are not initialized by default. They must be initialized before being read (see set_input_values() ).
Parameters:

- name – Shader input name.

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Values (shape and data type depend on the input name).

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

- RuntimeError – If the shader input is not initialized.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # get the glass IOR of all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_ior", values=[1.5])
... glass_ior = prims.get_input_values(name="glass_ior")
>>>
>>> # get the metallic amount of all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="metallic_constant", values=[0.5])
... metallic_constant = prims.get_input_values(name="metallic_constant")
>>>
>>> # get the opacity of all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="opacity", values=[0.1])
... opacity = prims.get_input_values(name="opacity")
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

set_input_values(
name:str,
values:str|bool|int|float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set shaders’ input values.
Parameters:

- name – Shader input name.

- values – Input values (shape and data type depend on the input name). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # set same glass color (green) for all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_color", values=[0.0, 1.0, 0.0])
>>>
>>> # set the Albedo map (textures) for all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="diffuse_texture", values=[
... "/local/path/to/texture_0",
... "/local/path/to/texture_1",
... "/local/path/to/texture_2",
... ])
>>>
>>> # set same diffuse color (red) for all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="diffuseColor", values=[1.0, 0.0, 0.0])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

propertyshaders:list[pxr.UsdShade.Shader]
USD shaders encapsulated by the wrapper.
Returns:
List of USD shaders.

Example:

```
>>> prims.shaders
[UsdShade.Shader(Usd.Prim(</World/prim_0/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_1/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_2/Shader>))]
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

classPreviewSurfaceMaterial(paths:str|list[str])
Bases: VisualMaterial
High level wrapper for creating/encapsulating USD Preview Surface (`UsdPreviewSurface`) material prims.
The `UsdPreviewSurface` is intended to model a modern physically based surface that strikes a balance between expressiveness and reliable interchange between engines and real-time rendering clients.
Note
This class creates or wraps (one of both) USD Preview Surface prims according to the following rules:

- If the prim paths exist, a wrapper is placed over the USD Preview Surface prims.

- If the prim paths do not exist, USD Preview Surface prims are created at each path and a wrapper is placed over them.

On visual materials, the shader parameters are encoded as inputs. The following table summarizes the `UsdPreviewSurface` material shader inputs:

[TABLE]
Input name | Description | Shape / Length | Type
"diffuseColor" | Color reflected from the material surface when light hits it. | (N, 3) | float
"emissiveColor" | Color of the light emitted by the material. | (N, 3) | float
"specularColor" | Color of the highlights that appear on a surface when it reflects light. | (N, 3) | float
"useSpecularWorkflow" | Operation mode (specular workflow: 1, metallic workflow: 0). | (N, 1) | int
"metallic" | Metallic (1.0 for metallic surfaces and 0.0 for non-metallic surfaces, in between for mixed surfaces). | (N, 1) | float
"roughness" | Roughness (specular lobe). | (N, 1) | float
"clearcoat" | Clearcoat (second specular lobe amount). | (N, 1) | float
"clearcoatRoughness" | Clearcoat roughness (second specular lobe roughness). | (N, 1) | float
"opacity" | Opacity (0.0 for fully transparent, 1.0 for fully opaque, in between for translucent). | (N, 1) | float
"opacityThreshold" | Opacity threshold. | (N, 1) | float
"ior" | Index of refraction (IOR). | (N, 1) | float
"normal" | Normal vector. | (N, 3) | float
"displacement" | Displacement (in the direction of the normal). | (N, 1) | float
[/TABLE]
Parameters:
paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

Raises:
ValueError – If resulting paths are mixed or invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
>>>
>>> # given an empty USD stage with the /World Xform prim,
>>> # create visual material at paths: /World/prim_0, /World/prim_1, and /World/prim_2
>>> paths = ["/World/prim_0", "/World/prim_1", "/World/prim_2"]
>>> prims = PreviewSurfaceMaterial(paths)
```
staticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Backends: usd.
Warning
Since this method is static, the output is always on the CPU.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

Example:

```
>>> # check if the following prims at paths are valid for creating instances
>>> result = PreviewSurfaceMaterial.are_of_type(["/World", "/World/prim_0"])
>>> print(result)
[[False]
[ True]]
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
)→list[VisualMaterial |None ]Fetch instances of visual material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get visual material instances from.

Returns:
List of visual material instances or `None` if the prim is not a supported visual material type.

Example:

```
>>> import omni.kit.commands
>>> from isaacsim.core.experimental.materials import VisualMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "CreatePreviewSurfaceMaterialPrim",
... mtl_path=f"/World/A",
... select_new_prim=False,
... )
>>>
>>> # fetch visual material instances
>>> VisualMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.visual_materials.preview_surface.PreviewSurfaceMaterial object at 0x...>]
```

get_input_values(
name:str,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet shaders’ input values.
Warning
Inputs are not initialized by default. They must be initialized before being read (see set_input_values() ).
Parameters:

- name – Shader input name.

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Values (shape and data type depend on the input name).

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

- RuntimeError – If the shader input is not initialized.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # get the glass IOR of all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_ior", values=[1.5])
... glass_ior = prims.get_input_values(name="glass_ior")
>>>
>>> # get the metallic amount of all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="metallic_constant", values=[0.5])
... metallic_constant = prims.get_input_values(name="metallic_constant")
>>>
>>> # get the opacity of all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="opacity", values=[0.1])
... opacity = prims.get_input_values(name="opacity")
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

set_input_values(
name:str,
values:str|bool|int|float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set shaders’ input values.
Parameters:

- name – Shader input name.

- values – Input values (shape and data type depend on the input name). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # set same glass color (green) for all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_color", values=[0.0, 1.0, 0.0])
>>>
>>> # set the Albedo map (textures) for all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="diffuse_texture", values=[
... "/local/path/to/texture_0",
... "/local/path/to/texture_1",
... "/local/path/to/texture_2",
... ])
>>>
>>> # set same diffuse color (red) for all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="diffuseColor", values=[1.0, 0.0, 0.0])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

propertyshaders:list[pxr.UsdShade.Shader]
USD shaders encapsulated by the wrapper.
Returns:
List of USD shaders.

Example:

```
>>> prims.shaders
[UsdShade.Shader(Usd.Prim(</World/prim_0/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_1/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_2/Shader>))]
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

classVisualMaterial(paths:str|list[str], *, resolve_paths:bool=True)
Bases: Prim , `ABC`
Base class for visual materials.
Parameters:

- paths – Single path or list of paths to USD prims. Can include regular expressions for matching multiple prims.

- resolve_paths – Whether to resolve the given paths (true) or use them as is (false).

abstractstaticare_of_type(
paths:str|Usd.Prim|list[str|Usd.Prim],
)→wp.arrayCheck if the prims at the given paths are valid for creating material instances of this type.
Parameters:
paths – Prim paths (or prims) to check for.

Returns:
Boolean flags indicating if the prims are valid for creating material instances (shape `(N, 1)`).

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
)→list[VisualMaterial |None ]Fetch instances of visual material from prims (or prim paths) at the given paths.
Backends: usd.
Parameters:
paths – Prim paths (or prims) to get visual material instances from.

Returns:
List of visual material instances or `None` if the prim is not a supported visual material type.

Example:

```
>>> import omni.kit.commands
>>> from isaacsim.core.experimental.materials import VisualMaterial
>>>
>>> # given a USD stage with the prims at paths /World, /World/A (USD Preview Surface)
>>> omni.kit.commands.execute(
... "CreatePreviewSurfaceMaterialPrim",
... mtl_path=f"/World/A",
... select_new_prim=False,
... )
>>>
>>> # fetch visual material instances
>>> VisualMaterial.fetch_instances(["/World", "/World/A"])
[None, <isaacsim.core.experimental.materials.impl.visual_materials.preview_surface.PreviewSurfaceMaterial object at 0x...>]
```

get_input_values(
name:str,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→wp.arrayGet shaders’ input values.
Warning
Inputs are not initialized by default. They must be initialized before being read (see set_input_values() ).
Parameters:

- name – Shader input name.

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Returns:
Values (shape and data type depend on the input name).

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

- RuntimeError – If the shader input is not initialized.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # get the glass IOR of all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_ior", values=[1.5])
... glass_ior = prims.get_input_values(name="glass_ior")
>>>
>>> # get the metallic amount of all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="metallic_constant", values=[0.5])
... metallic_constant = prims.get_input_values(name="metallic_constant")
>>>
>>> # get the opacity of all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="opacity", values=[0.1])
... opacity = prims.get_input_values(name="opacity")
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

set_input_values(
name:str,
values:str|bool|int|float|list|np.ndarray|wp.array,
*,
indices:int|list|np.ndarray|wp.array|None =None,
)→None Set shaders’ input values.
Parameters:

- name – Shader input name.

- values – Input values (shape and data type depend on the input name). If the input shape is smaller than expected, data will be broadcasted (following NumPy broadcast rules).

- indices – Indices of prims to process (shape `(N,)`). If not defined, all wrapped prims are processed.

Raises:

- AssertionError – Wrapped prims are not valid.

- ValueError – If the input name is invalid.

Example:

```
>>> from isaacsim.core.experimental.materials import OmniGlassMaterial, OmniPbrMaterial, PreviewSurfaceMaterial
>>>
>>> # set same glass color (green) for all prims (OmniGlass)
>>> if isinstance(prims, OmniGlassMaterial):
... prims.set_input_values(name="glass_color", values=[0.0, 1.0, 0.0])
>>>
>>> # set the Albedo map (textures) for all prims (OmniPBR)
>>> if isinstance(prims, OmniPbrMaterial):
... prims.set_input_values(name="diffuse_texture", values=[
... "/local/path/to/texture_0",
... "/local/path/to/texture_1",
... "/local/path/to/texture_2",
... ])
>>>
>>> # set same diffuse color (red) for all prims (USD Preview Surface)
>>> if isinstance(prims, PreviewSurfaceMaterial):
... prims.set_input_values(name="diffuseColor", values=[1.0, 0.0, 0.0])
```

propertymaterials:list[pxr.UsdShade.Material]
USD materials encapsulated by the wrapper.
Returns:
List of USD materials.

Example:

```
>>> prims.materials
[UsdShade.Material(Usd.Prim(</World/prim_0>)),
UsdShade.Material(Usd.Prim(</World/prim_1>)),
UsdShade.Material(Usd.Prim(</World/prim_2>))]
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

propertyshaders:list[pxr.UsdShade.Shader]
USD shaders encapsulated by the wrapper.
Returns:
List of USD shaders.

Example:

```
>>> prims.shaders
[UsdShade.Shader(Usd.Prim(</World/prim_0/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_1/Shader>)),
UsdShade.Shader(Usd.Prim(</World/prim_2/Shader>))]
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
