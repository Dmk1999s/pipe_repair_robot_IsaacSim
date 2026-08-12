<!-- source: py/source/extensions/isaacsim.core.experimental.utils/docs/api.html | title: API — Isaac Sim -->

# API
Warning
The API featured in this extension is experimental and subject to change without deprecation cycles. Although we will try to maintain backward compatibility in the event of a change, it may not always be possible.

## Python API

### Backend Utils
get_current_backend(
supported_backends:list[str],
*,
raise_on_unsupported:bool|None =None,
)→strGet the current backend value if it exists.
Parameters:

- supported_backends – The list of supported backends.

- raise_on_unsupported – Whether to raise an error if the backend is not supported when requested. If set to a value other than `None`, this parameter has precedence over the context value.

Returns:
The current backend value or the default value (first supported backend) if no backend is active.

is_backend_set()→bool
Check if a backend is set in the context.
Returns:
Whether a backend is set in the context.

should_raise_on_fallback()→bool
Check whether an exception should be raised, depending on the context’s raise on fallback state.
Returns:
Whether an exception should be raised on fallback backend.

should_raise_on_unsupported()→bool
Check whether an exception should be raised, depending on the context’s raise on unsupported state.
Returns:
Whether an exception should be raised on unsupported backend.

use_backend(
backend:Literal['usd','usdrt','fabric','tensor'],
*,
raise_on_unsupported:bool=False,
raise_on_fallback:bool=False,
)→Generator[None ,None ,None ]Context manager that sets a thread-local backend value.
Warning
The usdrt and fabric backends require Fabric Scene Delegate (FSD) to be enabled. FSD can be enabled in apps/.kit experience files by setting `app.useFabricSceneDelegate = true`.
Parameters:

- backend – The value to set in the context.

- raise_on_unsupported – Whether to raise an exception if the backend is not supported when requested.

- raise_on_fallback – Whether to raise an exception if the backend is supported, but a fallback is being used at a particular point in time when requested.

Raises:
RuntimeError – If the `usdrt` or `fabric` backend is specified but Fabric Scene Delegate (FSD) is disabled.

Example:

```
>>> import isaacsim.core.experimental.utils.backend as backend_utils
>>>
>>> with backend_utils.use_backend("usdrt"):
... # operate on the specified backend
... pass
>>> # operate on the default backend
```

### Foundation Utils
get_value_type_names(
*,
format:Literal[str,
Sdf.ValueTypeNames,
usdrt.Sdf.ValueTypeNames]=<class'str'>,
)→list[str|Sdf.ValueTypeName|usdrt.Sdf.ValueTypeName]Get all supported (from Isaac Sim’s Core API perspective) value type names.
Parameters:
format – Format to get the value type names in.

Returns:
List of value type names.

Raises:
ValueError – If the format is invalid.

Example:

```
>>> import isaacsim.core.experimental.utils.foundation as foundation_utils
>>> import usdrt
>>> from pxr import Sdf
>>>
>>> foundation_utils.get_value_type_names(format=str)
['asset', 'asset[]', 'bool', 'bool[]', 'color3d', ...]
>>> foundation_utils.get_value_type_names(format=Sdf.ValueTypeNames)
[<pxr.Sdf.ValueTypeName object at 0x...>, <pxr.Sdf.ValueTypeName object at 0x...>, ...]
>>> foundation_utils.get_value_type_names(format=usdrt.Sdf.ValueTypeNames)
[Sdf.ValueTypeName('asset'), Sdf.ValueTypeName('asset[]'), Sdf.ValueTypeName('bool'), ...]
```

resolve_value_type_name(
type_name:str|Sdf.ValueTypeName|usdrt.Sdf.ValueTypeName,
*,
backend:str|None =None,
)→Sdf.ValueTypeName|usdrt.Sdf.ValueTypeNameResolve the value type name for a given (value) type name according to the USD/USDRT specifications.
Backends: usd, usdrt, fabric.
Parameters:

- type_name – Type name.

- backend – Backend to use to get the value type name. If not `None`, it has precedence over the current backend set via the use_backend() context manager.

Returns:
Value type name instance.

Raises:

- ValueError – If the backend is not supported.

- ValueError –
If the type name is invalid.
Example:

```
>>> import isaacsim.core.experimental.utils.foundation as foundation_utils
>>>
>>> foundation_utils.resolve_value_type_name("color3f", backend="usd")
<pxr.Sdf.ValueTypeName object at 0x...>
>>> foundation_utils.resolve_value_type_name("color3f", backend="usdrt")
Sdf.ValueTypeName('float3 (color)')
```

value_type_name_to_str(
type_name:str|Sdf.ValueTypeName|usdrt.Sdf.ValueTypeName,
)→strGet the string representation of a given value type name.
Parameters:
type_name – Value type name.

Returns:
String representation of the value type name.

Raises:
ValueError – If the type name is invalid.

Example:

```
>>> import isaacsim.core.experimental.utils.foundation as foundation_utils
>>> import usdrt
>>> from pxr import Sdf
>>>
>>> foundation_utils.value_type_name_to_str("color3f[]")
'color3f[]'
>>> foundation_utils.value_type_name_to_str(Sdf.ValueTypeNames.Color3fArray)
'color3f[]'
>>> foundation_utils.value_type_name_to_str(usdrt.Sdf.ValueTypeNames.Color3fArray)
'color3f[]'
```

### Ops Utils
broadcast_to(
x:bool|int|float|list|np.ndarray|wp.array,
*,
shape:list[int],
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayBroadcast a Python primitive or list, a NumPy array, or a Warp array to a Warp array with a new shape.
Note
Broadcasting follows NumPy’s rules: Two shapes are compatible if by comparing their dimensions element-wise, starting with the trailing dimension (i.e., rightmost) and moving leftward

- they are equal, or

- one of them is 1.

Parameters:

- x – Python primitive or list, NumPy array, or Warp array.

- shape – Shape of the desired array.

- dtype – Data type of the output array. If `None`, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Warp array with the given shape.

Raises:

- ValueError – If the input list or array is not compatible with the new shape according to the broadcasting rules.

- TypeError – If the input argument `x` is not a supported data container.

Example:

```
>>> import isaacsim.core.experimental.utils.ops as ops_utils
>>> import numpy as np
>>> import warp as wp
>>>
>>> # Python primitive
>>> # - bool
>>> array = ops_utils.broadcast_to(True, shape=(1, 3))
>>> print(array)
[[ True True True]]
>>> # - int
>>> array = ops_utils.broadcast_to(2, shape=(1, 3))
>>> print(array)
[[2 2 2]]
>>> # - float
>>> array = ops_utils.broadcast_to(3.0, shape=(1, 3))
>>> print(array)
[[3. 3. 3.]]
>>>
>>> # Python list
>>> array = ops_utils.broadcast_to([1, 2, 3], shape=(1, 3))
>>> print(array)
[[1 2 3]]
>>>
>>> # NumPy array (with shape (1, 3))
>>> array = ops_utils.broadcast_to(np.array([[1, 2, 3]]), shape=(2, 3))
>>> print(array)
[[1 2 3]
[1 2 3]]
>>>
>>> # Warp array (with different device)
>>> array = ops_utils.broadcast_to(wp.array([1, 2, 3], device="cpu"), shape=(3, 3), device="cuda")
>>> print(array)
[[1 2 3]
[1 2 3]
[1 2 3]]
```

place(
x:bool|int|float|list|np.ndarray|wp.array,
*,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayCreate a Warp array from a Python primitive or list, a NumPy array, or a Warp array.
Parameters:

- x – Python primitive or list, NumPy array, or Warp array. If the input is a Warp array with the same device and dtype, it is returned as is.

- dtype – Data type of the output array. If not provided, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Warp array instance.

Raises:
TypeError – If the input argument `x` is not a supported data container.

Example:

```
>>> import isaacsim.core.experimental.utils.ops as ops_utils
>>> import numpy as np
>>> import warp as wp
>>>
>>> # Python primitive
>>> # - bool
>>> array = ops_utils.place(True, device="cpu")
>>> print(array, array.dtype, array.device, array.shape)
[ True] <class 'warp.types.bool'> cpu (1,)
>>> # - int
>>> array = ops_utils.place(1, device="cpu")
>>> print(array, array.dtype, array.device, array.shape)
[1] <class 'warp.types.int64'> cpu (1,)
>>> # - float
>>> array = ops_utils.place(1.0, device="cpu")
>>> print(array, array.dtype, array.device, array.shape)
[1.] <class 'warp.types.float64'> cpu (1,)
>>>
>>> # Python list
>>> array = ops_utils.place([1.0, 2.0, 3.0], device="cpu")
>>> print(array, array.dtype, array.device, array.shape)
[1. 2. 3.] <class 'warp.types.float64'> cpu (3,)
>>>
>>> # NumPy array (with shape (3, 1))
>>> array = ops_utils.place(np.array([[1], [2], [3]], dtype=np.uint8), dtype=wp.float32)
>>> print(array, array.dtype, array.device, array.shape)
[[1.] [2.] [3.]] <class 'warp.types.float32'> cuda:0 (3, 1)
>>>
>>> # Warp array (with different device)
>>> array = ops_utils.place(wp.array([1.0, 2.0, 3.0], device="cpu"), device="cuda")
>>> print(array, array.dtype, array.device, array.shape)
[1. 2. 3.] <class 'warp.types.float64'> cuda:0 (3,)
```

resolve_indices(
x:bool|int|float|list|np.ndarray|wp.array|None ,
*,
count:int|None =None,
dtype:type|None =warp.int32,
device:str|wp.context.Device|None =None,
)→wp.arrayCreate a flattened (1D) Warp array to be used as indices from a Python primitive or list, a NumPy array, or a Warp array.
Parameters:

- x – Python primitive or list, NumPy array, or Warp array.

- count – Number of indices to resolve. If input argument `x` is `None`, the indices are generated from 0 to `count - 1`. If input argument `x` is not `None`, this value is ignored.

- dtype – Data type of the output array. If `None`, `wp.int32` is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Flattened (1D) Warp array instance.

Raises:

- ValueError – If input argument `x` is `None` and `count` is not provided.

- TypeError – If the input argument `x` is not a supported data container.

Example:

```
>>> import isaacsim.core.experimental.utils.ops as ops_utils
>>> import numpy as np
>>> import warp as wp
>>>
>>> # Python primitive
>>> # - bool
>>> indices = ops_utils.resolve_indices(True, device="cpu")
>>> print(indices, indices.dtype, indices.device, indices.shape)
[1] <class 'warp.types.int32'> cpu (1,)
>>> # - int
>>> indices = ops_utils.resolve_indices(2, device="cpu")
>>> print(indices, indices.dtype, indices.device, indices.shape)
[2] <class 'warp.types.int32'> cpu (1,)
>>> # - float
>>> indices = ops_utils.resolve_indices(3.0, device="cpu")
>>> print(indices, indices.dtype, indices.device, indices.shape)
[3] <class 'warp.types.int32'> cpu (1,)
>>>
>>> # Python list
>>> indices = ops_utils.resolve_indices([1, 2, 3], device="cpu")
>>> print(indices, indices.dtype, indices.device, indices.shape)
[1 2 3] <class 'warp.types.int32'> cpu (3,)
>>>
>>> # NumPy array (with shape (3, 1))
>>> indices = ops_utils.resolve_indices(np.array([[1], [2], [3]], dtype=np.uint8))
>>> print(indices, indices.dtype, indices.device, indices.shape)
[1 2 3] <class 'warp.types.int32'> cuda:0 (3,)
>>>
>>> # Warp array (with different device)
>>> indices = ops_utils.resolve_indices(wp.array([1, 2, 3], device="cpu"), device="cuda")
>>> print(indices, indices.dtype, indices.device, indices.shape)
[1 2 3] <class 'warp.types.int32'> cuda:0 (3,)
```

### Prim Utils
create_prim_attribute(
prim:str|Usd.Prim|usdrt.Usd.Prim,
*,
name:str,
type_name:Sdf.ValueTypeName|usdrt.Sdf.ValueTypeName,
exist_ok:bool=True,
)→Usd.Attribute|usdrt.Usd.AttributeCreate a new attribute on a USD prim.
Backends: usd.
Parameters:

- prim – Prim path or prim instance.

- name – Name of the attribute to create.

- type_name – Type of the attribute to create.

- exist_ok – Whether to do not raise an error if the attribute already exists.

Returns:
Created attribute, or the existing attribute if it already exists (and `exist_ok` is `True`).

Raises:

- RuntimeError – If the attribute already exists and `exist_ok` is `False`.

- ValueError – If the attribute already exists with a different type name (and `exist_ok` is `True`).

get_all_matching_child_prims(
prim:str|Usd.Prim|usdrt.Usd.Prim,
*,
predicate:Callable[[Usd.Prim|usdrt.Usd.Prim,str],bool],
include_self:bool=False,
max_depth:int|None =None,
)→list[Usd.Prim|usdrt.Usd.Prim]Get all prim children of the given prim (excluding itself by default) that pass the predicate.
Backends: usd, usdrt, fabric.
Parameters:

- prim – Prim path or prim instance.

- predicate – Function to test the prims against. The function should take two positional arguments: a prim instance and its path. The function should return a boolean value indicating whether a prim passes the predicate.

- include_self – Whether to include the given prim in the search.

- max_depth – Maximum depth to search (current prim is at depth 0). If `None`, search till the end of the tree.

Returns:
List of matching prim children.

Raises:
ValueError – If `max_depth` is defined and is less than 0.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # define some prims
>>> stage_utils.define_prim("/World/Cube_0", "Cube")
>>> stage_utils.define_prim("/World/Cube_0/Cube_1", "Cube")
>>>
>>> # get all `/World`'s child prims of type Cube
>>> predicate = lambda prim, path: prim.GetTypeName() == "Cube"
>>> prim_utils.get_all_matching_child_prims("/World", predicate=predicate)
[Usd.Prim(</World/Cube_0>), Usd.Prim(</World/Cube_0/Cube_1>)]
>>>
>>> # get all `/World`'s child prims of type Cube with max depth 1
>>> prim_utils.get_all_matching_child_prims("/World", predicate=predicate, max_depth=1)
[Usd.Prim(</World/Cube_0>)]
```

get_first_matching_child_prim(
prim:str|Usd.Prim|usdrt.Usd.Prim,
*,
predicate:Callable[[Usd.Prim|usdrt.Usd.Prim,str],bool],
include_self:bool=False,
)→Usd.Prim|usdrt.Usd.Prim|None Get the first prim child of the given prim (excluding itself by default) that passes the predicate.
Backends: usd, usdrt, fabric.
Parameters:

- prim – Prim path or prim instance.

- predicate – Function to test the prims against. The function should take two positional arguments: a prim instance and its path. The function should return a boolean value indicating whether a prim passes the predicate.

- include_self – Whether to include the given prim in the search.

Returns:
First prim child or `None` if no prim child passes the predicate.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # define some prims
>>> stage_utils.define_prim("/World/Cube", "Cube")
>>> stage_utils.define_prim("/World/Cylinder", "Cylinder")
>>> stage_utils.define_prim("/World/Sphere", "Sphere")
>>>
>>> # get the first `/World`'s child prim of type Sphere
>>> predicate = lambda prim, path: prim.GetTypeName() == "Sphere"
>>> prim_utils.get_first_matching_child_prim("/World", predicate=predicate)
Usd.Prim(</World/Sphere>)
```

get_first_matching_parent_prim(
prim:str|Usd.Prim|usdrt.Usd.Prim,
*,
predicate:Callable[[Usd.Prim|usdrt.Usd.Prim,str],bool],
include_self:bool=False,
)→Usd.Prim|usdrt.Usd.Prim|None Get the first prim parent of the given prim (excluding itself by default) that passes the predicate.
Backends: usd, usdrt, fabric.
Warning
The root prim (`/`) is not considered a valid parent prim but a pseudo-root prim. Therefore, it is not taken into account by this function, and any match for this prim will return `None`.
Parameters:

- prim – Prim path or prim instance.

- predicate – Function to test the prims against. The function should take two positional arguments: a prim instance and its path. The function should return a boolean value indicating whether a prim passes the predicate.

- include_self – Whether to include the given prim in the search.

Returns:
First prim parent or `None` if no prim parent passes the predicate.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # define some nested prims
>>> stage_utils.define_prim("/World/Cube", "Cube")
>>> stage_utils.define_prim("/World/Cube/Cylinder", "Cylinder")
>>> stage_utils.define_prim("/World/Cube/Cylinder/Sphere", "Sphere")
>>>
>>> # get the first `Sphere`'s parent prim of type Cube
>>> predicate = lambda prim, path: prim.GetTypeName() == "Cube"
>>> prim_utils.get_first_matching_parent_prim("/World/Cube/Cylinder/Sphere", predicate=predicate)
Usd.Prim(</World/Cube>)
```

get_prim_at_path(path:str)→Usd.Prim|usdrt.Usd.Prim
Get the prim at a given path.
Backends: usd, usdrt, fabric.
Parameters:
path – Prim path.

Returns:
Prim.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.define_prim(f"/World/Cube", "Cube")
>>>
>>> prim_utils.get_prim_at_path("/World/Cube")
Usd.Prim(</World/Cube>)
```

get_prim_path(prim:Usd.Prim|usdrt.Usd.Prim)→str
Get the path of a given prim.
Backends: usd, usdrt, fabric.
Parameters:
prim – Prim instance.

Returns:
Prim path.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> prim = stage_utils.define_prim(f"/World/Cube", "Cube")
>>> prim_utils.get_prim_path(prim)
'/World/Cube'
```

get_prim_variant_collection(
prim:str|Usd.Prim,
)→dict[str,list[str]]Get variant collection (all variant sets and selections) for a USD prim.
Backends: usd.
Parameters:
prim – Prim path or prim instance.

Returns:
Variant collection (variant sets and selections).

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.storage.native import get_assets_root_path
>>>
>>> stage_utils.open_stage(
... get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
... )
>>>
>>> prim_utils.get_prim_variant_collection("/panda")
{'Mesh': ['Performance', 'Quality'], 'Gripper': ['AlternateFinger', 'Default', 'None', 'Robotiq_2F_85']}
```

get_prim_variants(prim:str|Usd.Prim)→list[tuple[str,str]]
Get variants (variant sets and selections) authored on a USD prim.
Backends: usd.
Parameters:
prim – Prim path or prim instance.

Returns:
Authored variants (variant sets and selections).

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.storage.native import get_assets_root_path
>>>
>>> stage_utils.open_stage(
... get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
... )
>>>
>>> prim_utils.get_prim_variants("/panda")
[('Gripper', 'Default'), ('Mesh', 'Performance')]
```

has_api(
prim:str|Usd.Prim,
api:str|type|list[str|type],
*,
test:Literal['all','any','none']='all',
)→boolCheck if a prim has or not the given API schema(s) applied.
Backends: usd.
Parameters:

- prim – Prim path or prim instance.

- api – API schema name or type, or a list of them.

- test – Checking operation to test for. - “all”: All APIs must be present. - “any”: Any API must be present. - “none”: No APIs must be present.

Returns:
Whether the prim has or not (depending on the test) the given API schema applied.

Raises:
ValueError – If the test operation is invalid.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from pxr import UsdLux
>>>
>>> prim = stage_utils.define_prim("/World/Light", "SphereLight")
>>> prim_utils.has_api(prim, UsdLux.LightAPI)
True
```

set_prim_variants(
prim:str|Usd.Prim,
*,
variants:list[tuple[str,str]],
)→None Set/author variants (variant sets and selections) on a USD prim.
Backends: usd.
Parameters:

- prim – Prim path or prim instance.

- variants – Variants (variant sets and selections) to author on the USD prim.

Raises:
ValueError – If a variant set or selection is invalid.

Example:

```
>>> import isaacsim.core.experimental.utils.prim as prim_utils
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.storage.native import get_assets_root_path
>>>
>>> stage_utils.open_stage(
... get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
... )
>>>
>>> prim_utils.set_prim_variants("/panda", variants=[("Mesh", "Quality"), ("Gripper", "AlternateFinger")])
```

### Stage Utils
add_reference_to_stage(
usd_path:str,
path:str,
*,
prim_type:str='Xform',
variants:list[tuple[str,str]]=[],
)→pxr.Usd.PrimAdd a USD file reference to the stage at the specified prim path.
Backends: usd.
Note
This function handles stage units verification to ensure compatibility.
Parameters:

- usd_path – USD file path to reference.

- path – Prim path where the reference will be attached.

- prim_type – Prim type to create if the given `path` doesn’t exist.

- variants – Variants (variant sets and selections) to author on the USD prim.

Returns:
USD prim.

Raises:

- Exception – The USD file might not exist or might not be a valid USD file.

- ValueError – If a variant set or selection is invalid.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.storage.native import get_assets_root_path
>>>
>>> prim = stage_utils.add_reference_to_stage(
... usd_path=get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd",
... path="/panda",
... variants=[("Gripper", "AlternateFinger"), ("Mesh", "Performance")],
... )
```

close_stage()→bool
Close the stage attached to the USD context.
Backends: usd.
Returns:
Whether the stage was closed successfully.

create_new_stage(*, template:str|None =None)→pxr.Usd.Stage
Create a new USD stage attached to the USD context.
Backends: usd.
Note
At least the following templates should be available. Other templates might be available depending on app customizations.

[TABLE]
Template | Description
"default stage" | Stage with a gray gridded plane, dome and distant lights, and the /World Xform prim.
"empty" | Empty stage with the /World Xform prim.
"sunlight" | Stage with a distant light and the /World Xform prim.
[/TABLE]
Parameters:
template – The template to use to create the stage. If `None`, a new stage is created with nothing.

Returns:
New USD stage instance.

Raises:
ValueError – When the template is not found.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # create a new stage from the 'sunlight' template
>>> stage_utils.create_new_stage(template="sunlight")
Usd.Stage.Open(rootLayer=Sdf.Find('anon:...usd'), ...)

>>> # get the list of available templates
>>> import omni.kit.stage_templates
>>>
>>> [name for item in omni.kit.stage_templates.get_stage_template_list() for name in item]
['empty', 'sunlight', 'default stage']
```

asynccreate_new_stage_async(
*,
template:str|None =None,
)→pxr.Usd.StageCreate a new USD stage attached to the USD context.
Backends: usd.
This function is the asynchronous version of create_new_stage() .
Parameters:
template – The template to use to create the stage. If `None`, a new stage is created with nothing.

Returns:
New USD stage instance.

Raises:
ValueError – When the template is not found.

define_prim(
path:str,
type_name:str='Xform',
)→Usd.Prim|usdrt.Usd.PrimAttempt to define a prim of the specified type at the given path.
Backends: usd, usdrt, fabric.
Common token values for `type_name` are:

- `"Camera"`, `"Mesh"`, `"PhysicsScene"`, `"Scope"`, `"Xform"`

- Shapes (`"Capsule"`, `"Cone"`, `"Cube"`, `"Cylinder"`, `"Plane"`, `"Sphere"`)

- Lights (`"CylinderLight"`, `"DiskLight"`, `"DistantLight"`, `"DomeLight"`, `"RectLight"`, `"SphereLight"`)

Parameters:

- path – Absolute prim path.

- type_name – Token identifying the prim type.

Raises:

- ValueError – If the path is not a valid or absolute path string.

- RuntimeError – If there is already a prim at the given path with a different type.

Returns:
Defined prim.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.define_prim("/World/Sphere", type_name="Sphere")
Usd.Prim(</World/Sphere>)
```

generate_next_free_path(
path:str|None =None,
*,
prepend_default_prim:bool=True,
)→strGenerate the next free usd path for the current stage.
Backends: usd.
Parameters:

- path – Base path to generate the next free path from. If empty, pseudo-root or not defined, `"Prim"` will be used as the default name.

- prepend_default_prim – Whether to prepend the default prim path to the base path.

Returns:
Next free path.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01
>>> stage_utils.define_prim("/World/Cube", type_name="Cube")
>>> stage_utils.define_prim("/World/Cube_01", type_name="Cube")
>>>
>>> # generate the next available path for /World/Cube
>>> stage_utils.generate_next_free_path("/World/Cube")
'/World/Cube_02'
```

get_current_stage(
*,
backend:str|None =None,
)→Usd.Stage|usdrt.Usd.StageGet the stage set in the context manager or the default stage attached to the USD context.
Backends: usd, usdrt, fabric.
Parameters:
backend – Backend to use to get the stage. If not `None`, it has precedence over the current backend set via the use_backend() context manager.

Returns:
The current stage instance or the default stage attached to the USD context if no stage is set.

Raises:

- ValueError – If the backend is not supported.

- ValueError – If there is no stage (set via context manager or attached to the USD context).

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.get_current_stage()
Usd.Stage.Open(rootLayer=Sdf.Find('anon:...usd'), ...)
```

get_stage_id(stage:pxr.Usd.Stage)→int
Get the stage ID of a USD stage.
Backends: usd.
Parameters:
stage – The stage to get the ID of.

Returns:
The stage ID.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage = stage_utils.get_current_stage()
>>> stage_utils.get_stage_id(stage)
9223006
```

get_stage_time_code()→tuple[float,float,float]
Get the stage time code (start, end, and time codes per second).
Backends: usd.
Returns:
The stage time code (start, end, and time codes per second).

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.get_stage_time_code()
(0.0, 100.0, 60.0)
```

get_stage_units()→tuple[float,float]
Get the stage meters per unit and kilograms per unit currently set.
Backends: usd.
The most common distance units and their values are listed in the following table:

[TABLE]
Unit | Value
kilometer (km) | 1000.0
meters (m) | 1.0
inch (in) | 0.0254
centimeters (cm) | 0.01
millimeter (mm) | 0.001
[/TABLE]
The most common mass units and their values are listed in the following table:

[TABLE]
Unit | Value
metric ton (t) | 1000.0
kilogram (kg) | 1.0
gram (g) | 0.001
pound (lb) | 0.4536
ounce (oz) | 0.0283
[/TABLE]
Returns:
Current stage meters per unit and kilograms per unit.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.get_stage_units()
(1.0, 1.0)
```

get_stage_up_axis()→Literal['Y','Z']
Get the stage up axis.
Backends: usd.
Note
According to the USD specification, only `"Y"` and `"Z"` axes are supported.
Returns:
The stage up axis.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.get_stage_up_axis()
'Z'
```

is_stage_set()→bool
Check if a stage is set in the context manager.
Returns:
Whether a stage is set in the context manager.

open_stage(usd_path:str)→tuple[bool,Usd.Stage|None ]
Open a USD file attached to the USD context.
Backends: usd.
Parameters:
usd_path – USD file path to open.

Returns:
Two-elements tuple. 1) Whether the USD file was opened successfully. 2) Opened USD stage instance or None if the USD file was not opened.

Raises:
ValueError – If the USD file does not exist or is not a valid (shallow check).

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>> from isaacsim.storage.native import get_assets_root_path
>>>
>>> # open a USD file
>>> result, stage = stage_utils.open_stage(
... get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
... )
>>> result
True
>>> stage
Usd.Stage.Open(rootLayer=Sdf.Find('...'), ...)
```

asyncopen_stage_async(usd_path:str)→tuple[bool,Usd.Stage|None ]
Open a USD file attached to the USD context.
Backends: usd.
This function is the asynchronous version of open_stage() .
Parameters:
usd_path – USD file path to open.

Returns:
Two-elements tuple. 1) Whether the USD file was opened successfully. 2) Opened USD stage instance or None if the USD file was not opened.

Raises:
ValueError – If the USD file does not exist or is not a valid (shallow check).

save_stage(usd_path:str)→bool
Save the current stage to a USD file.
Backends: usd.
Parameters:
usd_path – USD file path to save the current stage to.

Returns:
Whether the stage was saved successfully.

Example:

```
>>> import os
>>> import tempfile
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # save the current stage to a USD file
>>> usd_path = os.path.join(tempfile.gettempdir(), "test.usd")
>>> stage_utils.save_stage(usd_path)
True
```

set_stage_time_code(
*,
start_time_code:float|None =None,
end_time_code:float|None =None,
time_codes_per_second:float|None =None,
)→None Set the stage time code (start, end, and time codes per second).
Backends: usd.
Parameters:

- start_time_code – The start time code.

- end_time_code – The end time code.

- time_codes_per_second – The time codes per second.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.set_stage_time_code(start_time_code=0.0, end_time_code=100.0, time_codes_per_second=10.0)
```

set_stage_units(
*,
meters_per_unit:float|None =None,
kilograms_per_unit:float|None =None,
)→None Set the stage meters per unit and kilograms per unit.
Backends: usd.
The most common distance units and their values are listed in the following table:

[TABLE]
Unit | Value
kilometer (km) | 1000.0
meters (m) | 1.0
inch (in) | 0.0254
centimeters (cm) | 0.01
millimeter (mm) | 0.001
[/TABLE]
The most common mass units and their values are listed in the following table:

[TABLE]
Unit | Value
metric ton (t) | 1000.0
kilogram (kg) | 1.0
gram (g) | 0.001
pound (lb) | 0.4536
ounce (oz) | 0.0283
[/TABLE]
Returns:
Current stage meters per unit and kilograms per unit.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> # set stage units to inch and pound respectively
>>> stage_utils.set_stage_units(meters_per_unit=0.0254, kilograms_per_unit=0.4536)
```

set_stage_up_axis(up_axis:Literal['Y','Z'])→None
Set the stage up axis.
Backends: usd.
Note
According to the USD specification, only `"Y"` and `"Z"` axes are supported.
Parameters:
up_axis – The stage up axis.

Raises:
ValueError – If the up axis is not a valid token.

Example:

```
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_utils.set_stage_up_axis("Y")
```

use_stage(stage:pxr.Usd.Stage)→Generator[None ,None ,None ]
Context manager that sets a thread-local stage instance.
Parameters:
stage – The stage to set in the context.

Raises:
AssertionError – If the stage is not a USD stage instance.

Example:

```
>>> from pxr import Usd
>>> import isaacsim.core.experimental.utils.stage as stage_utils
>>>
>>> stage_in_memory = Usd.Stage.CreateInMemory()
>>> with stage_utils.use_stage(stage_in_memory):
... # operate on the specified stage
... pass
>>> # operate on the default stage attached to the USD context
```

### Transform Utils
euler_angles_to_quaternion(
euler_angles:list|np.ndarray|wp.array,
*,
degrees:bool=False,
extrinsic:bool=True,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayConvert Euler angles to quaternion.
Parameters:

- euler_angles – Euler XYZ angles or batch of Euler angles with shape (…, 3).

- degrees – Whether input angles are in degrees. Defaults to False.

- extrinsic – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

- dtype – Data type of the output array. If `None`, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Quaternion (w, x, y, z) or batch of quaternions with shape (…, 4).

Example:

```
>>> import isaacsim.core.experimental.utils.transform as transform_utils
>>> import numpy as np
>>>
>>> # Convert 90 degree rotation around Y axis
>>> euler = np.array([0, np.pi/2, 0])
>>> quaternion = transform_utils.euler_angles_to_quaternion(euler)
>>> quaternion.numpy()
array([0.70710678, 0. , 0.70710678, 0. ])
```

euler_angles_to_rotation_matrix(
euler_angles:list|np.ndarray|wp.array,
*,
degrees:bool=False,
extrinsic:bool=True,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayConvert Euler XYZ or ZYX angles to rotation matrix.
Parameters:

- euler_angles – Euler angles or batch of Euler angles with shape (…, 3).

- degrees – Whether passed angles are in degrees. Defaults to False.

- extrinsic – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

- dtype – Data type of the output array. If `None`, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
A 3x3 rotation matrix or batch of 3x3 rotation matrices with shape (…, 3, 3).

Example:

```
>>> import isaacsim.core.experimental.utils.transform as transform_utils
>>> import numpy as np
>>>
>>> # Zero rotation
>>> euler = np.array([0, 0, 0])
>>> rotation_matrix = transform_utils.euler_angles_to_rotation_matrix(euler)
>>> rotation_matrix.numpy()
array([[1., 0., 0.],
[0., 1., 0.],
[0., 0., 1.]], dtype=float32)
```

quaternion_conjugate(
quaternion:list|np.ndarray|wp.array,
*,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayCompute quaternion conjugate by negating the vector part.
Quaternion conjugate is used to compute the inverse rotation. For unit quaternions, conjugate equals inverse.
Parameters:

- quaternion – Quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.

- dtype – Data type of the output array. If `None`, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Conjugate quaternion with shape (…, 4).

Example:

```
>>> import isaacsim.core.experimental.utils.transform as transform_utils
>>> import numpy as np
>>>
>>> # Conjugate of a simple rotation quaternion
>>> quaternion = np.array([0.7071, 0.7071, 0.0, 0.0]) # 90 deg around X
>>> conjugate = transform_utils.quaternion_conjugate(quaternion)
>>> conjugate.numpy()
array([ 0.7071, -0.7071, 0. , 0. ])
```

quaternion_multiplication(
first_quaternion:list|np.ndarray|wp.array,
second_quaternion:list|np.ndarray|wp.array,
*,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayMultiply two quaternions using Hamilton product.
Quaternion multiplication is used for combining rotations. Input quaternions are in [w, x, y, z] format.
Parameters:

- first_quaternion – First quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.

- second_quaternion – Second quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.

- dtype – Data type of the output array. If `None`, the data type of the first input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Result of quaternion multiplication with shape (…, 4).

Example:

```
>>> import isaacsim.core.experimental.utils.transform as transform_utils
>>> import numpy as np
>>>
>>> # Identity quaternion multiplied with itself
>>> identity = np.array([1.0, 0.0, 0.0, 0.0])
>>> result = transform_utils.quaternion_multiplication(identity, identity)
>>> result.numpy()
array([1., 0., 0., 0.])
```

quaternion_to_rotation_matrix(
quaternion:list|np.ndarray|wp.array,
*,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayConvert quaternion to rotation matrix.
Converts quaternions in [w, x, y, z] format to 3x3 rotation matrices using the standard quaternion-to-matrix formula.
Parameters:

- quaternion – Quaternion or batch of quaternions with shape (…, 4) in [w, x, y, z] format.

- dtype – Data type of the output array. If `None`, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
A 3x3 rotation matrix or batch of 3x3 rotation matrices with shape (…, 3, 3).

Example:

```
>>> import isaacsim.core.experimental.utils.transform as transform_utils
>>> import numpy as np
>>>
>>> # Identity quaternion to rotation matrix
>>> identity = np.array([1.0, 0.0, 0.0, 0.0])
>>> rotation_matrix = transform_utils.quaternion_to_rotation_matrix(identity)
>>> rotation_matrix.numpy()
array([[1., 0., 0.],
[0., 1., 0.],
[0., 0., 1.]])
```

rotation_matrix_to_quaternion(
rotation_matrix:list|np.ndarray|wp.array,
*,
dtype:type|None =None,
device:str|wp.context.Device|None =None,
)→wp.arrayConvert rotation matrix to quaternion.
Parameters:

- rotation_matrix – A 3x3 rotation matrix or batch of 3x3 rotation matrices with shape (…, 3, 3).

- dtype – Data type of the output array. If `None`, the data type of the input is used.

- device – Device to place the output array on. If `None`, the default device is used, unless the input is a Warp array (in which case the input device is used).

Returns:
Quaternion (w, x, y, z) or batch of quaternions with shape (…, 4).

Example:

```
>>> import isaacsim.core.experimental.utils.transform as transform_utils
>>> import numpy as np
>>>
>>> # Identity matrix to quaternion
>>> identity = np.eye(3)
>>> quaternion = transform_utils.rotation_matrix_to_quaternion(identity)
>>> quaternion.numpy()
array([1., 0., 0., 0.])
```
