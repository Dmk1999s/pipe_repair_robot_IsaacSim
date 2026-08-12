<!-- source: py/source/extensions/isaacsim.core.utils/docs/api.html | title: API — Isaac Sim -->

# API

## Python API

### Articulation Utils
Utils for programmatically interacting with Articulations on the Stage.
The utils can be used to:

- Modify Articulation Roots.

- Determine the base paths of every Articulation on the Stage.

add_articulation_root(prim:pxr.Usd.Prim)→None
Add an Articulation Root to prim.
Parameters:
prim (Usd.Prim) – A prim to which an Articulation Root will be added.

find_all_articulation_base_paths()→List
Find all base Articulation paths on the stage.
A base path is defined as the maximal path that contains every part of a robot. For example, the articulation root in the UR10 robot may be at “/World/ur10/base_link”, but the path returned by this function would be “/World/ur10”.
An Articulation base path:

- Contains exactly one Articulation Root in the subtree of prim paths that stem from a base path.

- Is a parent of every link in an Articulation.

On a stage with nested articulation roots, only the inner-most root will be listed.
Returns:
A list of every Articulation base path on the stage.

Return type:
List

move_articulation_root(
src_prim:pxr.Usd.Prim,
dst_prim:pxr.Usd.Prim,
)→None Move the Articulation Root from src_prim to dst_prim. If src_prim is not an Articulation Root, nothing will happen.
Parameters:

- src_prim (Usd.Prim) – A prim from which an Articulation Root will be removed.

- dst_prim (Usd.Prim) – A prim to which an Articulation Root will be added.

remove_articulation_root(prim:pxr.Usd.Prim)→None
Remove the Articulation Root from prim if one exists.
Parameters:
prim (Usd.Prim) – A prim whose Articulation Root will be removed.

### Bounds Utils
Utils for computing the Axis-Aligned Bounding Box (AABB) and the Oriented Bounding Box (OBB) of a prim.

- The AABB is the smallest cuboid that can completely contain the prim it represents. It is defined by the following 3D coordinates: \((x_{min}, y_{min}, z_{min}, x_{max}, y_{max}, z_{max})\).

- Unlike the AABB, which is aligned with the coordinate axes, the OBB can be oriented at any angle in 3D space.

compute_aabb(
bbox_cache:pxr.UsdGeom.BBoxCache,
prim_path:str,
include_children:bool=False,
)→arrayCompute an Axis-Aligned Bounding Box (AABB) for a given `prim_path`
A combined AABB is computed if `include_children` is True
Parameters:

- bbox_cache (UsdGeom.BboxCache) – Existing Bounding box cache to use for computation

- prim_path (str) – prim path to compute AABB for

- include_children (bool, optional) – include children of specified prim in calculation. Defaults to False.

Returns:
Bounding box for this prim, [min x, min y, min z, max x, max y, max z]

Return type:
np.array

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>>
>>> # 1 stage unit length cube centered at (0.0, 0.0, 0.0)
>>> cache = bounds_utils.create_bbox_cache()
>>> bounds_utils.compute_aabb(cache, prim_path="/World/Cube")
[-0.5 -0.5 -0.5 0.5 0.5 0.5]
>>>
>>> # the same cube rotated 45 degrees around the z-axis
>>> cache = bounds_utils.create_bbox_cache()
>>> bounds_utils.compute_aabb(cache, prim_path="/World/Cube")
[-0.70710678 -0.70710678 -0.5 0.70710678 0.70710678 0.5]
```

compute_combined_aabb(
bbox_cache:pxr.UsdGeom.BBoxCache,
prim_paths:List[str],
)→arrayComputes a combined Axis-Aligned Bounding Box (AABB) given a list of prim paths
Parameters:

- bbox_cache (UsdGeom.BboxCache) – Existing Bounding box cache to use for computation

- prim_paths (List[str]) – List of prim paths to compute combined AABB for

Returns:
Bounding box for input prims, [min x, min y, min z, max x, max y, max z]

Return type:
np.array

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>>
>>> # 1 stage unit length cube centered at (0.0, 0.0, 0.0)
>>> # with a 1 stage unit diameter sphere centered at (-0.5, 0.5, 0.5)
>>> cache = bounds_utils.create_bbox_cache()
>>> bounds_utils.compute_combined_aabb(cache, prim_paths=["/World/Cube", "/World/Sphere"])
[-1. -0.5 -0.5 0.5 1. 1. ]
```

compute_obb(
bbox_cache:pxr.UsdGeom.BBoxCache,
prim_path:str,
)→Tuple[ndarray,ndarray,ndarray]Computes the Oriented Bounding Box (OBB) of a prim
Note

- The OBB does not guarantee the smallest possible bounding box, it rotates and scales the default AABB.

- The rotation matrix incorporates any scale factors applied to the object.

- The half_extent values do not include these scaling effects.

Parameters:

- bbox_cache (UsdGeom.BBoxCache) – USD Bounding Box Cache object to use for computation

- prim_path (str) – Prim path to compute OBB for

Returns:
A tuple containing the following OBB information:

- The centroid of the OBB as a NumPy array.

- The axes of the OBB as a 2D NumPy array, where each row represents a different axis.

- The half extent of the OBB as a NumPy array.

Return type:
Tuple[np.ndarray, np.ndarray, np.ndarray]

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>>
>>> # 1 stage unit length cube centered at (0.0, 0.0, 0.0)
>>> cache = bounds_utils.create_bbox_cache()
>>> centroid, axes, half_extent = bounds_utils.compute_obb(cache, prim_path="/World/Cube")
>>> centroid
[0. 0. 0.]
>>> axes
[[1. 0. 0.]
[0. 1. 0.]
[0. 0. 1.]]
>>> half_extent
[0.5 0.5 0.5]
>>>
>>> # the same cube rotated 45 degrees around the z-axis
>>> cache = bounds_utils.create_bbox_cache()
>>> centroid, axes, half_extent = bounds_utils.compute_obb(cache, prim_path="/World/Cube")
>>> centroid
[0. 0. 0.]
>>> axes
[[ 0.70710678 0.70710678 0. ]
[-0.70710678 0.70710678 0. ]
[ 0. 0. 1. ]]
>>> half_extent
[0.5 0.5 0.5]
```

compute_obb_corners(
bbox_cache:pxr.UsdGeom.BBoxCache,
prim_path:str,
)→ndarrayComputes the corners of the Oriented Bounding Box (OBB) of a prim
Parameters:

- bbox_cache (UsdGeom.BBoxCache) – Bounding Box Cache object to use for computation

- prim_path (str) – Prim path to compute OBB for

Returns:
NumPy array of shape (8, 3) containing each corner location of the OBB
\(c_0 = (x_{min}, y_{min}, z_{min})\)
\(c_1 = (x_{min}, y_{min}, z_{max})\)
\(c_2 = (x_{min}, y_{max}, z_{min})\)
\(c_3 = (x_{min}, y_{max}, z_{max})\)
\(c_4 = (x_{max}, y_{min}, z_{min})\)
\(c_5 = (x_{max}, y_{min}, z_{max})\)
\(c_6 = (x_{max}, y_{max}, z_{min})\)
\(c_7 = (x_{max}, y_{max}, z_{max})\)

Return type:
np.ndarray

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>>
>>> cache = bounds_utils.create_bbox_cache()
>>> bounds_utils.compute_obb_corners(cache, prim_path="/World/Cube")
[[-0.5 -0.5 -0.5]
[-0.5 -0.5 0.5]
[-0.5 0.5 -0.5]
[-0.5 0.5 0.5]
[ 0.5 -0.5 -0.5]
[ 0.5 -0.5 0.5]
[ 0.5 0.5 -0.5]
[ 0.5 0.5 0.5]]
```

create_bbox_cache(
time:pxr.Usd.TimeCode=pxr.Usd.TimeCode.Default,
use_extents_hint:bool=True,
)→pxr.UsdGeom.BBoxCacheHelper function to create a Bounding Box Cache object that can be used for computations
Parameters:

- time (Usd.TimeCode, optional) – time at which cache should be initialized. Defaults to Usd.TimeCode.Default().

- use_extents_hint (bool, optional) – Use existing extents attribute on prim to compute bounding box. Defaults to True.

Returns:
Initialized bbox cache

Return type:
UsdGeom.BboxCache

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>>
>>> bounds_utils.create_bbox_cache()
<pxr.UsdGeom.BBoxCache object at 0x7f6720b8bc90>
```

get_obb_corners(
centroid:ndarray,
axes:ndarray,
half_extent:ndarray,
)→ndarrayComputes the corners of the Oriented Bounding Box (OBB) from the given OBB information
Parameters:

- centroid (np.ndarray) – The centroid of the OBB as a NumPy array.

- axes (np.ndarray) – The axes of the OBB as a 2D NumPy array, where each row represents a different axis.

- half_extent (np.ndarray) – The half extent of the OBB as a NumPy array.

Returns:
NumPy array of shape (8, 3) containing each corner location of the OBB
\(c_0 = (x_{min}, y_{min}, z_{min})\)
\(c_1 = (x_{min}, y_{min}, z_{max})\)
\(c_2 = (x_{min}, y_{max}, z_{min})\)
\(c_3 = (x_{min}, y_{max}, z_{max})\)
\(c_4 = (x_{max}, y_{min}, z_{min})\)
\(c_5 = (x_{max}, y_{min}, z_{max})\)
\(c_6 = (x_{max}, y_{max}, z_{min})\)
\(c_7 = (x_{max}, y_{max}, z_{max})\)

Return type:
np.ndarray

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>>
>>> cache = bounds_utils.create_bbox_cache()
>>> centroid, axes, half_extent = bounds_utils.compute_obb(cache, prim_path="/World/Cube")
>>> bounds_utils.get_obb_corners(centroid, axes, half_extent)
[[-0.5 -0.5 -0.5]
[-0.5 -0.5 0.5]
[-0.5 0.5 -0.5]
[-0.5 0.5 0.5]
[ 0.5 -0.5 -0.5]
[ 0.5 -0.5 0.5]
[ 0.5 0.5 -0.5]
[ 0.5 0.5 0.5]]
```

recompute_extents(
prim:pxr.UsdGeom.Boundable,
time:pxr.Usd.TimeCode=pxr.Usd.TimeCode.Default,
include_children:bool=False,
)→None Recomputes and overwrites the extents attribute for a UsdGeom.Boundable prim
Parameters:

- prim (UsdGeom.Boundable) – Input prim to recompute extents for

- time (Usd.TimeCode, optional) – timecode to use for computing extents. Defaults to Usd.TimeCode.Default().

- include_children (bool, optional) – include children of specified prim in calculation. Defaults to False.

Raises:
ValueError – If prim is not of UsdGeom.Boundable type

Example:

```
>>> import isaacsim.core.utils.bounds as bounds_utils
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> prim = stage_utils.get_current_stage().GetPrimAtPath("/World/Cube")
>>> bounds_utils.recompute_extents(prim)
```

### Carb Utils
Carb settings is a generalized subsystem designed to provide a simple to use interface to Kit’s various subsystems, which can be automated, enumerated, serialized and so on.
The most common types of settings are:

- Persistent (saved between sessions): `"/persistent/<setting>"`
(e.g., `"/persistent/physics/numThreads"`)

- Application: `"/app/<setting>"` (e.g., `"/app/viewport/grid/enabled"`)

- Extension: `"/exts/<extension>/<setting>"` (e.g., `"/exts/omni.kit.debug.python/host"`)

get_carb_setting(
carb_settings:carb.settings.ISettings,
setting:str,
)→AnyConvenience function to get settings.
Parameters:

- carb_settings (carb.settings.ISettings) – The interface to carb settings.

- setting (str) – Name of setting to change.

Returns:
Value for the setting.

Return type:
Any

Example:

```
>>> import carb
>>> import isaacsim.core.utils.carb as carb_utils
>>>
>>> settings = carb.settings.get_settings()
>>> carb_utils.get_carb_setting(settings, "/physics/updateToUsd")
False
```

set_carb_setting(
carb_settings:carb.settings.ISettings,
setting:str,
value:Any,
)→None Convenience to set the carb settings.
Parameters:

- carb_settings (carb.settings.ISettings) – The interface to carb settings.

- setting (str) – Name of setting to change.

- value (Any) – New value for the setting.

Raises:
TypeError – If the type of value does not match setting type.

Example:

```
>>> import carb
>>> import isaacsim.core.utils.carb as carb_utils
>>>
>>> settings = carb.settings.get_settings()
>>> carb_utils.set_carb_setting(settings, "/physics/updateToUsd", True)
```

### Collisions Utils
ray_cast(
position:array,
orientation:array,
offset:array,
max_dist:float=100.0,
)→Tuple[None |str,float]Projects a raycast forward along x axis with specified offset
If a hit is found within the maximum distance, then the object’s prim path and distance to it is returned. Otherwise, a None and 10000 is returned.
Parameters:

- position (np.array) – origin’s position for ray cast

- orientation (np.array) – origin’s orientation for ray cast

- offset (np.array) – offset for ray cast

- max_dist (float, optional) – maximum distance to test for collisions in stage units. Defaults to 100.0.

Returns:
path to geometry that was hit and hit distance, returns None, 10000 if no hit occurred

Return type:
Tuple[Union[None, str], float]

### Commands
classIsaacSimDestroyPrim(*args:Any, **kwargs:Any)
Bases: `Command`
Command to set a delete a prim. This variant has less overhead than other commands as it doesn’t store an undo operation
Typical usage example:

```
omni.kit.commands.execute(
"IsaacSimDestroyPrim",
prim_path="/World/Prim,
)
```

classIsaacSimScalePrim(*args:Any, **kwargs:Any)
Bases: `Command`
Command to set a scale of a prim
Typical usage example:

```
omni.kit.commands.execute(
"IsaacSimScalePrim",
prim_path="/World/Prim,
scale=(1.5, 1.5, 1.5),
)
```

classIsaacSimSpawnPrim(*args:Any, **kwargs:Any)
Bases: `Command`
Command to spawn a new prim in the stage and set its transform. This uses dynamic_control to properly handle physics objects and articulation
Typical usage example:

```
omni.kit.commands.execute(
"IsaacSimSpawnPrim",
usd_path="/path/to/file.usd",
prim_path="/World/Prim,
translation=(0, 0, 0),
rotation=(0, 0, 0, 1),
)
```

classIsaacSimTeleportPrim(*args:Any, **kwargs:Any)
Bases: `Command`
Command to set a transform of a prim. This uses dynamic_control to properly handle physics objects and articulation
Typical usage example:

```
omni.kit.commands.execute(
"IsaacSimTeleportPrim",
prim_path="/World/Prim,
translation=(0, 0, 0),
rotation=(0, 0, 0, 1),
)
```

get_current_stage(
fabric:bool=False,
)→pxr.Usd.Stage|usdrt.Usd._Usd.StageGet the current open USD or Fabric stage
Parameters:
fabric (bool, optional) – True to get the fabric stage. False to get the USD stage. Defaults to False.

Returns:
The USD or Fabric stage as specified by the input arg fabric.

Return type:
Union[Usd.Stage, usdrt.Usd._Usd.Stage]

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.get_current_stage()
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x7fba6c04f840:World7.usd'),
sessionLayer=Sdf.Find('anon:0x7fba6c01c5c0:World7-session.usda'),
pathResolverContext=<invalid repr>)
```

get_current_stage_id()→int
Get the current open stage id
Returns:
The stage id.

Return type:
int

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.get_current_stage_id()
1234567890
```

### Constants Utils
AXES_INDICES={'X':0,'Y':1,'Z':2,'x':0,'y':1,'z':2}
Mapping from axis name to axis ID
Example:

```
>>> import isaacsim.core.utils.constants as constants_utils
>>>
>>> # get the x-axis index
>>> constants_utils.AXES_INDICES['x']
0
>>> constants_utils.AXES_INDICES['X']
0
```

AXES_TOKEN={'X':pxr.UsdGeom.Tokens.x,'Y':pxr.UsdGeom.Tokens.y,'Z':pxr.UsdGeom.Tokens.z,'x':pxr.UsdGeom.Tokens.x,'y':pxr.UsdGeom.Tokens.y,'z':pxr.UsdGeom.Tokens.z}
Mapping from axis name to axis USD token

```
>>> import isaacsim.core.utils.constants as constants_utils
>>>
>>> # get the x-axis USD token
>>> constants_utils.AXES_TOKEN['x']
X
>>> constants_utils.AXES_TOKEN['X']
X
```

### Distance Metrics Utils
rotational_distance_angle(
r1:ndarray|pxr.Gf.Matrix3d|pxr.Gf.Matrix4d,
r2:ndarray|pxr.Gf.Matrix3d|pxr.Gf.Matrix4d,
)→ndarrayComputes the weighted distance between two rotations using inner product.
Note
If r1 and r2 are GfMatrix3d() objects, the transformation matrices will be transposed in the distance calculations.
Parameters:

- r1 (Union[np.ndarray, Gf.Matrix3d, Gf.Matrix4d]) – rotation matrices or 4x4 transformation matrices

- r2 (Union[np.ndarray, Gf.Matrix3d, Gf.Matrix4d]) – rotation matrices or 4x4 transformation matrices

Returns:
the magnitude of the angle of rotation from r1 to r2

Return type:
np.ndarray

rotational_distance_identity_matrix_deviation(
r1:ndarray|pxr.Gf.Matrix4d|pxr.Gf.Matrix3d,
r2:ndarray|pxr.Gf.Matrix4d|pxr.Gf.Matrix3d,
)→ndarrayComputes the distance between two rotations using deviation from identity matrix.
Note
If r1 and r2 are GfMatrix3d() objects, the transformation matrices will be transposed in the distance calculations.
Parameters:

- r1 (Union[np.ndarray, Gf.Matrix4d, Gf.Matrix3d]) – rotation matrices or 4x4 transformation matrices

- r2 (Union[np.ndarray, Gf.Matrix4d, Gf.Matrix3d]) – rotation matrices or 4x4 transformation matrices

Returns:
the Frobenius norm |I-r1*r2^T|, where I is the identity matrix

Return type:
np.ndarray

rotational_distance_single_axis(
r1:ndarray|pxr.Gf.Matrix4d|pxr.Gf.Matrix3d,
r2:ndarray|pxr.Gf.Matrix4d|pxr.Gf.Matrix3d,
axis:ndarray,
)→ndarrayComputes the distance between two rotations w.r.t. input axis.
Note
If r1 and r2 are GfMatrix3d() objects, the transformation matrices will be transposed in the distance calculations.
Usage:
If the robot were holding a cup aligned with its z-axis, it would be important to align the z-axis of the robot with the z-axis of the world frame. This could be accomplished by letting
-r1 be the rotation of the robot end effector-r2 be any rotation matrix for a rotation about the z axis-axis = [0,0,1]
Parameters:

- r1 (Union[np.ndarray, Gf.Matrix4d, Gf.Matrix3d]) – rotation matrices or 4x4 transformation matrices

- r2 (Union[np.ndarray, Gf.Matrix4d, Gf.Matrix3d]) – rotation matrices or 4x4 transformation matrices

- axis (np.ndarray) – a 3d vector that will be rotated by r1 and r2

Returns:
the angle between (r1 @ axis) and (r2 @ axis)

Return type:
np.ndarray

weighted_translational_distance(
t1:ndarray|pxr.Gf.Matrix4d,
t2:ndarray|pxr.Gf.Matrix4d,
weight_matrix:ndarray=array([[1.,0.,0.],[0.,1.,0.],[0.,0.,1.]]),
)→ndarrayComputes the weighted distance between two translation vectors.
The distance calculation has the form sqrt(x.T W x), where
- x is the vector difference between t1 and t2.- W is a weight matrix.Given the identity weight matrix, this is equivalent to the |t1-t2|.
Usage:
This formulation can be used to weight an arbitrary axis of the translation difference. Letting x = t1-t2 = a1*b1 + a2*b2 + a3*b3 (where b1,b2,b3 are column basis vectors, and a1,a2,a3 are constants), When W = I: x.T W x = sqrt(a1^2 + a2^2 + a3^2). To weight the b1 axis by 2, let W take the form (R.T @ ([4,1,1]@I) @ R) where:
- I is the identity matrix.- R is a rotation matrix of the form [b1,b2,b3].TThis is effectively equivalent to |[2*e1,e2,e3] @ [b1,b2,b3].T @ x| = sqrt(4*a1^2 + a2^2 + a3^2).
- e1,e2,e3 are the elementary basis vectors.
Parameters:

- t1 (Union[np.ndarray, Gf.Matrix4d]) – 3d translation vectors or 4x4 transformation matrices

- t2 (Union[np.ndarray, Gf.Matrix4d]) – 3d translation vectors or 4x4 transformation matrices

- weight_matrix (np.ndarray, optional) – a 3x3 positive semidefinite matrix of weights. Defaults to np.eye(3).

Returns:
the weighted norm of the difference (t1-t2)

Return type:
np.ndarray

### Extensions Utils
Utilities for enabling and disabling extensions from the Extension Manager and knowing their locations
disable_extension(extension_name:str)→bool
Unload an extension.
Parameters:
extension_name (str) – name of the extension

Returns:
True if extension could be unloaded, False otherwise

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.extensions as extensions_utils
>>>
>>> extensions_utils.disable_extension("omni.kit.window.stage")
True
```

enable_extension(extension_name:str)→bool
Load an extension from the extension manager.
Parameters:
extension_name (str) – name of the extension

Returns:
True if extension could be loaded, False otherwise

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.extensions as extensions_utils
>>>
>>> extensions_utils.enable_extension("omni.kit.window.stage")
True
```

get_extension_id(extension_name:str)→str
Get extension id for a loaded extension
Parameters:
extension_name (str) – name of the extension

Returns:
Full extension id

Return type:
str

Example:

```
>>> import isaacsim.core.utils.extensions as extensions_utils
>>>
>>> extensions_utils.get_extension_id("omni.kit.window.stage")
omni.kit.window.stage-2.4.3
```

get_extension_path(ext_id:str)→str
Get extension path for a loaded extension by its full id
Parameters:
ext_id (str) – full id of extension

Returns:
Path to loaded extension root directory

Return type:
str

Example:

```
>>> import isaacsim.core.utils.extensions as extensions_utils
>>>
>>> ext_id = extensions_utils.get_extension_id("omni.kit.window.stage")
>>> extensions_utils.get_extension_path(ext_id)
/home/user/.local/share/ov/pkg/isaac_sim-<version>/kit/exts/omni.kit.window.stage
```

get_extension_path_from_name(extension_name:str)→str
Get extension path for a loaded extension by its name
Parameters:
extension_name (str) – name of the extension

Returns:
Path to loaded extension root directory

Return type:
str

Example:

```
>>> import isaacsim.core.utils.extensions as extensions_utils
>>>
>>> extensions_utils.get_extension_path_from_name("omni.kit.window.stage")
/home/user/.local/share/ov/pkg/isaac_sim-<version>/kit/exts/omni.kit.window.stage
```

### Interoperability Utils
Utilities for interoperability between different (ML) frameworks.
Supported frameworks are:

- Warp

- PyTorch

- JAX

- TensorFlow

- NumPy

jax2numpy(array:jax.Array)→numpy.ndarray
Convert JAX array to NumPy array
Parameters:
array (jax.Array) – JAX array

Returns:
NumPy array

Return type:
numpy.ndarray

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import jax
>>> import jax.numpy as jnp
>>>
>>> with jax.default_device(jax.devices("cuda")[0]):
... jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
...
>>> numpy_array = interops_utils.jax2numpy(jax_array)
>>> type(numpy_array)
<class 'numpy.ndarray'>
```

jax2tensorflow(array:jax.Array)→tensorflow.Tensor
Convert JAX array to TensorFlow tensor
Parameters:
array (jax.Array) – JAX array

Returns:
TensorFlow tensor

Return type:
tensorflow.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import jax
>>> import jax.numpy as jnp
>>>
>>> with jax.default_device(jax.devices("cuda")[0]):
... jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
...
>>> tensorflow_tensor = interops_utils.jax2tensorflow(jax_array)
>>> type(tensorflow_tensor)
<class 'tensorflow.python...Tensor'>
```

jax2torch(array:jax.Array)→torch.Tensor
Convert JAX array to PyTorch tensor
Parameters:
array (jax.Array) – JAX array

Returns:
PyTorch tensor

Return type:
torch.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import jax
>>> import jax.numpy as jnp
>>>
>>> with jax.default_device(jax.devices("cuda")[0]):
... jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
...
>>> torch_tensor = interops_utils.jax2torch(jax_array)
>>> type(torch_tensor)
<class 'torch.Tensor'>
```

jax2warp(array:jax.Array)→warp.array
Convert JAX array to Warp array
Parameters:
array (jax.Array) – JAX array

Returns:
Warp array

Return type:
warp.array

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import jax
>>> import jax.numpy as jnp
>>>
>>> with jax.default_device(jax.devices("cuda")[0]):
... jax_array = jnp.zeros((100, 10), dtype=jnp.float32)
...
>>> warp_array = interops_utils.jax2warp(jax_array)
>>> type(warp_array)
<class 'warp.types.array'>
```

numpy2jax(array:numpy.ndarray)→jax.Array
Convert NumPy array to JAX array
Parameters:
array (numpy.ndarray) – NumPy array

Returns:
JAX array

Return type:
jax.Array

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import numpy as np
>>>
>>> numpy_array = np.zeros((100, 10), dtype=np.float32)
>>> jax_array = interops_utils.numpy2jax(numpy_array)
>>> type(jax_array)
<class 'jaxlib.xla_extension.ArrayImpl'>
```

numpy2tensorflow(array:numpy.ndarray)→tensorflow.Tensor
Convert NumPy array to TensorFlow tensor
Parameters:
array (numpy.ndarray) – NumPy array

Returns:
TensorFlow tensor

Return type:
tensorflow.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import numpy as np
>>>
>>> numpy_array = np.zeros((100, 10), dtype=np.float32)
>>> tensorflow_tensor = interops_utils.numpy2tensorflow(numpy_array)
>>> type(tensorflow_tensor)
<class 'tensorflow.python...Tensor'>
```

numpy2torch(array:numpy.ndarray)→torch.Tensor
Convert NumPy array to PyTorch tensor
Parameters:
array (numpy.ndarray) – NumPy array

Returns:
PyTorch tensor

Return type:
torch.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import numpy as np
>>>
>>> numpy_array = np.zeros((100, 10), dtype=np.float32)
>>> torch_tensor = interops_utils.numpy2torch(numpy_array)
>>> type(torch_tensor)
<class 'torch.Tensor'>
```

numpy2warp(array:numpy.ndarray)→warp.array
Convert NumPy array to Warp array
Parameters:
array (numpy.ndarray) – NumPy array

Returns:
Warp array

Return type:
warp.array

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import numpy as np
>>>
>>> numpy_array = np.zeros((100, 10), dtype=np.float32)
>>> warp_array = interops_utils.numpy2warp(numpy_array)
>>> type(warp_array)
<class 'warp.types.array'>
```

tensorflow2jax(tensor:tensorflow.Tensor)→jax.Array
Convert TensorFlow tensor to JAX array
Parameters:
tensor (tensorflow.Tensor) – TensorFlow tensor

Returns:
JAX array

Return type:
jax.Array

Warning
It is expected that the conversion of `int32` TensorFlow tensors to other backends will be on the CPU, regardless of which context device is specified (see TensorFlow issues #34071, #41307, #46833)
Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import tensorflow as tf
>>>
>>> with tf.device("/GPU:0"):
... tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
...
>>> jax_array = interops_utils.tensorflow2jax(tensorflow_tensor)
>>> type(jax_array)
<class 'jaxlib.xla_extension.Array...'>
```

tensorflow2numpy(tensor:tensorflow.Tensor)→numpy.ndarray
Convert TensorFlow tensor to NumPy array
Parameters:
tensor (tensorflow.Tensor) – TensorFlow tensor

Returns:
NumPy array

Return type:
numpy.ndarray

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import tensorflow as tf
>>>
>>> with tf.device("/GPU:0"):
... tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
...
>>> numpy_array = interops_utils.tensorflow2numpy(tensorflow_tensor)
>>> type(numpy_array)
<class 'numpy.ndarray'>
```

tensorflow2torch(tensor:tensorflow.Tensor)→torch.Tensor
Convert TensorFlow tensor to PyTorch tensor
Parameters:
tensor (tensorflow.Tensor) – TensorFlow tensor

Returns:
PyTorch tensor

Return type:
torch.Tensor

Warning
It is expected that the conversion of `int32` TensorFlow tensors to other backends will be on the CPU, regardless of which context device is specified (see TensorFlow issues #34071, #41307, #46833)
Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import tensorflow as tf
>>>
>>> with tf.device("/GPU:0"):
... tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
...
>>> torch_tensor = interops_utils.tensorflow2torch(tensorflow_tensor)
>>> type(torch_tensor)
<class 'torch.Tensor'>
```

tensorflow2warp(tensor:tensorflow.Tensor)→warp.array
Convert TensorFlow tensor to Warp array
Parameters:
tensor (tensorflow.Tensor) – TensorFlow tensor

Returns:
Warp array

Return type:
warp.array

Warning
It is expected that the conversion of `int32` TensorFlow tensors to other backends will be on the CPU, regardless of which context device is specified (see TensorFlow issues #34071, #41307, #46833)
Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import tensorflow as tf
>>>
>>> with tf.device("/GPU:0"):
... tensorflow_tensor = tf.zeros((100, 10), dtype=tf.float32)
...
>>> warp_array = interops_utils.tensorflow2warp(tensorflow_tensor)
>>> type(warp_array)
<class 'warp.types.array'>
```

torch2jax(tensor:torch.Tensor)→jax.Array
Convert PyTorch tensor to JAX array
Parameters:
tensor (torch.Tensor) – PyTorch tensor

Returns:
JAX array

Return type:
jax.Array

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import torch
>>>
>>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
>>> jax_array = interops_utils.torch2jax(torch_tensor)
>>> type(jax_array)
<class 'jaxlib.xla_extension.Array...'>
```

torch2numpy(tensor:torch.Tensor)→numpy.ndarray
Convert PyTorch tensor to NumPy array
Parameters:
tensor (torch.Tensor) – PyTorch tensor

Returns:
NumPy array

Return type:
numpy.ndarray

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import torch
>>>
>>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
>>> numpy_array = interops_utils.torch2numpy(torch_tensor)
>>> print(type(numpy_array))
<class 'numpy.ndarray'>
```

torch2tensorflow(tensor:torch.Tensor)→tensorflow.Tensor
Convert PyTorch tensor to TensorFlow tensor
Parameters:
tensor (torch.Tensor) – PyTorch tensor

Returns:
TensorFlow tensor

Return type:
tensorflow.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import torch
>>>
>>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
>>> tensorflow_tensor = interops_utils.torch2tensorflow(torch_tensor)
>>> type(tensorflow_tensor)
<class 'tensorflow.python...Tensor'>
```

torch2warp(tensor:torch.Tensor)→warp.array
Convert PyTorch tensor to Warp array
Parameters:
tensor (torch.Tensor) – PyTorch tensor

Returns:
Warp array

Return type:
warp.array

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import torch
>>>
>>> torch_tensor = torch.zeros((100, 10), dtype=torch.float32, device=torch.device("cuda:0"))
>>> warp_array = interops_utils.torch2warp(torch_tensor)
>>> type(warp_array)
<class 'warp.types.array'>
```

warp2jax(array:warp.array)→jax.Array
Convert Warp array to JAX array
Parameters:
array (warp.array) – Warp array

Returns:
JAX array

Return type:
jax.Array

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import warp as wp
>>>
>>> wp.init()
>>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
>>> jax_array = interops_utils.warp2jax(warp_array)
>>> type(jax_array)
<class 'jaxlib.xla_extension.Array...'>
```

warp2numpy(array:warp.array)→numpy.ndarray
Convert Warp array to NumPy array
Parameters:
array (warp.array) – Warp array

Returns:
NumPy array

Return type:
numpy.ndarray

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import warp as wp
>>>
>>> wp.init()
>>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
>>> numpy_array = interops_utils.warp2numpy(warp_array)
>>> type(numpy_array)
<class 'numpy.ndarray'>
```

warp2tensorflow(array:warp.array)→tensorflow.Tensor
Convert Warp array to TensorFlow tensor
Parameters:
array (warp.array) – Warp array

Returns:
TensorFlow tensor

Return type:
tensorflow.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import warp as wp
>>>
>>> wp.init()
>>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
>>> tensorflow_tensor = interops_utils.warp2tensorflow(warp_array)
>>> type(tensorflow_tensor)
<class 'tensorflow.python...Tensor'>
```

warp2torch(array:warp.array)→torch.Tensor
Convert Warp array to PyTorch tensor
Parameters:
array (warp.array) – Warp array

Returns:
PyTorch tensor

Return type:
torch.Tensor

Example:

```
>>> import isaacsim.core.utils.interops as interops_utils
>>> import warp as wp
>>>
>>> wp.init()
>>> warp_array = wp.zeros((100, 10), dtype=wp.float32, device="cuda:0")
>>> torch_tensor = interops_utils.warp2torch(warp_array)
>>> type(torch_tensor)
<class 'torch.Tensor'>
```

### Math Utils
cross(a:ndarray|list, b:ndarray|list)→list
Computes the cross-product between two 3-dimensional vectors.
Parameters:

- a (np.ndarray, list) – A 3-dimensional vector

- b (np.ndarray, list) – A 3-dimensional vector

Returns:
Cross product between input vectors.

Return type:
np.ndarray

normalize(v)
Normalizes the vector inline (and also returns it).

normalized(v)
Returns a normalized copy of the provided vector.

radians_to_degrees(rad_angles:ndarray)→ndarray
Converts input angles from radians to degrees.
Parameters:
rad_angles (np.ndarray) – Input array of angles (in radians).

Returns:
Array of angles in degrees.

Return type:
np.ndarray

#### Math Utils
This submodule provides math bindings for vector operations, and other facilitators such as lerp functions.
add(arg0:carb::Float3, arg1:carb::Float3)→carb::Float3
Adds two 3D vectors
Args:
arg0 (`carb.Float3`): First 3D vector
arg1 (`carb.Float3`): Second 3D vector

Returns:
`carb.Float3`: `arg0 + arg1`.

cross(arg0:carb::Float3, arg1:carb::Float3)→carb::Float3
Performs Cross product between 3D vectors :param arg0: 3D vector :type arg0: `carb.Float3` :param arg1: 3D vector :type arg1: `carb.Float3`
Returns:
cross poduct `arg0 x arg1`.

Return type:
`carb.Float3`

dot(*args, **kwargs)
Overloaded function.

- dot(arg0: carb::Float3, arg1: carb::Float3) -> float

Performs Dot product between 3D vectors
Args:
arg0 (`carb.Float3`): 3D vector
arg1 (`carb.Float3`): 3D vector

Returns:
`carb.Float3`: dot poduct `arg0 * arg1`.

- dot(arg0: carb::Float4, arg1: carb::Float4) -> float

Performs Dot product between 4D vectors
Args:
arg0 (`carb.Float4`): 4D vector
arg1 (`carb.Float4`): 4D vector

Returns:
`carb.Float4`: dot poduct `arg0 * arg1`.

get_basis_vector_x(arg0:carb::Float4)→carb::Float3
Gets Basis vector X of quaternion
Parameters:
arg0 (`carb.Float4`) – Quaternion

Returns:
Basis Vector X

Return type:
`carb.Float3`

get_basis_vector_y(arg0:carb::Float4)→carb::Float3
Gets Basis vector Y of quaternion
Parameters:
arg0 (`carb.Float4`) – Quaternion

Returns:
Basis Vector Y

Return type:
`carb.Float3`

get_basis_vector_z(arg0:carb::Float4)→carb::Float3
Gets Basis vector Z of quaternion
Parameters:
arg0 (`carb.Float4`) – Quaternion

Returns:
Basis Vector Z

Return type:
`carb.Float3`

inverse(arg0:carb::Float4)→carb::Float4
Gets Inverse Quaternion
Args:
arg0 (`carb.Float4`): quaternion

Returns:
`carb.Float4`: The inverse quaternion

lerp(*args, **kwargs)
Overloaded function.

- lerp(arg0: carb::Float3, arg1: carb::Float3, arg2: float) -> carb::Float3
Performs Linear interpolation between points arg0 and arg1
Args:
arg0 (`carb.Float3`): Point
arg1 (`carb.Float3`): Point
arg2 (`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1

Returns:
`carb.Float3`: Interpolated point

- lerp(arg0: carb::Float4, arg1: carb::Float4, arg2: float) -> carb::Float4
Performs Linear interpolation between quaternions arg0 and arg1
Args:
arg0 (`carb.Float4`): Quaternion
arg1 (`carb.Float4`): Quaternion
arg2 (`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1

Returns:
`carb.Float4`: Interpolated quaternion

mul(*args, **kwargs)
Overloaded function.

- mul(arg0: carb::Float3, arg1: float) -> carb::Float3

Scales a 3D vector by a given value
Args:
arg0 (`carb.Float3`): 3D vector
arg1 (`float`): scale factor

Returns:
`carb.Float3`: scaled vector.

- mul(arg0: carb::Float4, arg1: float) -> carb::Float4

Scales a 4D vector by a given value
Args:
arg0 (`carb.Float4`): 4D vector
arg1 (`float`): scale factor

Returns:
`carb.Float4`: scaled vector.

- mul(arg0: carb::Float4, arg1: carb::Float4) -> carb::Float4

Performs a Quaternion rotation between two 4D vectors
Args:
arg0 (`carb.Float4`): first 4D quaternion vector
arg1 (`carb.Float4`): second 4D quaternion vector

Returns:
`carb.Float4`: rotated 4D quaternion vector.

normalize(*args, **kwargs)
Overloaded function.

- normalize(arg0: carb::Float3) -> carb::Float3
Gets normalized 3D vector
Args:
arg0 (`carb.Float3`): 3D Vector

Returns:
`carb.Float3`: Normalized 3D Vector

- normalize(arg0: carb::Float4) -> carb::Float4
Gets normalized 4D vector Args:
arg0 (`carb.Float4`): 4D Vector

Returns:
`carb.Float4`: Normalized 4D Vector

rotate(arg0:carb::Float4, arg1:carb::Float3)→carb::Float3
rotates the 3D vector arg1 by the quaternion arg0
Parameters:

- arg0 (`carb.Float4`) – quaternion

- arg1 (`carb.Float3`) – 3D Vector

Returns:
Rotated 3D Vector

Return type:
`carb.Float3`

slerp(
arg0:carb::Float4,
arg1:carb::Float4,
arg2:float,
)→carb::Float4Performs Spherical Linear interpolation between quaternions arg0 and arg1
Parameters:

- arg0 (`carb.Float4`) – Quaternion

- arg1 (`carb.Float4`) – Quaternion

- arg2 (`float`) – distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1

Returns:
Interpolated quaternion

Return type:
`carb.Float4`

transform_inv(
arg0:pxrInternal_v0_24__pxrReserved__::GfTransform,
arg1:pxrInternal_v0_24__pxrReserved__::GfTransform,
)→pxrInternal_v0_24__pxrReserved__::GfTransformComputes local Transform of arg1 with respect to arg0: inv(arg0)*arg1
Parameters:

- arg0 (pxr.Transform) – origin Transform

- arg1 (pxr.Transform) – Transform

Returns:
resulting transform of `inv(arg0)*arg1`

Return type:
`oxr.Transform`

set_scale(arg0:int, arg1:str, arg2:carb::Float3)→None
Set scale for an object in the stage
Parameters:

- stageId (`int`) – Stage ID

- primPath (`str`) – Path to the prim

- scale (`carb.Float3`) – Scale vector

set_transform(
arg0:int,
arg1:str,
arg2:carb::Float3,
arg3:carb::Float4,
)→None Set transform for an object in the stage, handles physics objects if simulation is running using dynamic control
Parameters:

- stageId (`int`) – Stage ID

- primPath (`str`) – Path to the prim

- translation (`carb.Float3`) – Translation vector

- rotation (`carb.Float4`) – Rotation quaternion

### Mesh Utils
get_mesh_vertices_relative_to(
mesh_prim:pxr.UsdGeom.Mesh,
coord_prim:pxr.Usd.Prim,
)→ndarrayGet vertices of the mesh prim in the coordinate system of the given prim.
Parameters:

- mesh_prim (UsdGeom.Mesh) – mesh prim to get the vertice points.

- coord_prim (Usd.Prim) – prim used as relative coordinate.

Returns:
vertices of the mesh in the coordinate system of the given prim. Shape is (N, 3).

Return type:
np.ndarray

Example:

```
>>> import isaacsim.core.utils.mesh as mesh_utils
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # 1 stage unit length cube centered at (0.0, 0.0, 0.0)
>>> mesh_prim = stage_utils.get_current_stage().GetPrimAtPath("/World/Cube")
>>> # 1 stage unit diameter sphere centered at (1.0, 1.0, 1.0)
>>> coord_prim = stage_utils.get_current_stage().GetPrimAtPath("/World/Sphere")
>>>
>>> mesh_utils.get_mesh_vertices_relative_to(mesh_prim, coord_prim)
[[-1.5 -1.5 -0.5]
[-0.5 -1.5 -0.5]
[-1.5 -0.5 -0.5]
[-0.5 -0.5 -0.5]
[-1.5 -1.5 -1.5]
[-0.5 -1.5 -1.5]
[-1.5 -0.5 -1.5]
[-0.5 -0.5 -1.5]]
```

### Physics Utils
get_rigid_body_enabled(prim_path:str)→bool|None
Get the `physics:rigidBodyEnabled` attribute from the USD Prim at the given path
Parameters:
prim_path (str) – The path to the USD Prim

Returns:
The value of `physics:rigidBodyEnabled` attribute if it exists, and None if it does not exist.

Return type:
Any

Example:

```
>>> import isaacsim.core.utils.physics as physics_utils
>>>
>>> # prim without the Physics' Rigid Body property
>>> physics_utils.get_rigid_body_enabled("/World/Cube")
None
>>> # prim with the physics Rigid Body property added and enabled
>>> physics_utils.get_rigid_body_enabled("/World/Cube")
True
```

set_rigid_body_enabled(_value, prim_path)
If it exists, set the `physics:rigidBodyEnabled` attribute on the USD Prim at the given path
Note
If the prim does not have the physics Rigid Body property added, calling this function will have no effect
Parameters:

- _value (Any) – Value to set `physics:rigidBodyEnabled` attribute to

- prim_path (str) – The path to the USD Prim

Example:

```
>>> import isaacsim.core.utils.physics as physics_utils
>>>
>>> physics_utils.set_rigid_body_enabled(False, "/World/Cube")
```

asyncsimulate_async(
seconds:float,
steps_per_sec:int=60,
callback:Callable=None,
)→None Helper function to simulate async for `seconds * steps_per_sec frames`.
Parameters:

- seconds (float) – time in seconds to simulate for

- steps_per_sec (int, optional) – steps per second. Defaults to 60.

- callback (Callable, optional) – optional function to run every step. Defaults to None.

Example:

```
>>> import asyncio
>>> import isaacsim.core.utils.physics as physics_utils
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... # simulate 1 second with 120 steps per second
... await physics_utils.simulate_async(1, steps_per_sec=120)
...
>>> run_coroutine(task())
```

```
>>> import asyncio
>>> import isaacsim.core.utils.physics as physics_utils
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> def callback(*args, **kwargs):
... print("callback:", args, kwargs)
...
>>> async def task():
... # simulate 1 second with 120 steps per second and call the callback on each step
... await physics_utils.simulate_async(1, 120, callback)
...
>>> run_coroutine(task())
```

### Prims Utils
create_prim(
prim_path:str,
prim_type:str='Xform',
position:Sequence[float]|None =None,
translation:Sequence[float]|None =None,
orientation:Sequence[float]|None =None,
scale:Sequence[float]|None =None,
usd_path:str|None =None,
semantic_label:str|None =None,
semantic_type:str='class',
attributes:dict|None =None,
)→pxr.Usd.PrimCreate a prim into current USD stage.
The method applies specified transforms, the semantic label and set specified attributes.
Parameters:

- prim_path (str) – The path of the new prim.

- prim_type (str) – Prim type name

- position (Sequence[float], optional) – prim position (applied last)

- translation (Sequence[float], optional) – prim translation (applied last)

- orientation (Sequence[float], optional) – prim rotation as quaternion

- scale (np.ndarray (3), optional) – scaling factor in x, y, z.

- usd_path (str, optional) – Path to the USD that this prim will reference.

- semantic_label (str, optional) – Semantic label.

- semantic_type (str, optional) – set to “class” unless otherwise specified.

- attributes (dict, optional) – Key-value pairs of prim attributes to set.

Raises:
Exception – If there is already a prim at the prim_path

Returns:
The created USD prim.

Return type:
Usd.Prim

Example:

```
>>> import numpy as np
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # create a cube (/World/Cube) of size 2 centered at (1.0, 0.5, 0.0)
>>> prims_utils.create_prim(
... prim_path="/World/Cube",
... prim_type="Cube",
... position=np.array([1.0, 0.5, 0.0]),
... attributes={"size": 2.0}
... )
Usd.Prim(</World/Cube>)
```

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # load an USD file (franka.usd) to the stage under the path /World/panda
>>> prims_utils.create_prim(
... prim_path="/World/panda",
... prim_type="Xform",
... usd_path="/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd"
... )
Usd.Prim(</World/panda>)
```

define_prim(
prim_path:str,
prim_type:str='Xform',
fabric:bool=False,
)→pxr.Usd.PrimCreate a USD Prim at the given prim_path of type prim_type unless one already exists
Note
This method will create a prim of the specified type in the specified path. To apply a transformation (position, orientation, scale), set attributes or load an USD file while creating the prim use the `create_prim` function.
Parameters:

- prim_path (str) – path of the prim in the stage

- prim_type (str, optional) – The type of the prim to create. Defaults to “Xform”.

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Raises:
Exception – If there is already a prim at the prim_path

Returns:
The created USD prim.

Return type:
Usd.Prim

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.define_prim("/World/Shapes", prim_type="Xform")
Usd.Prim(</World/Shapes>)
```

delete_prim(prim_path:str)→None
Remove the USD Prim and its descendants from the scene if able
Parameters:
prim_path (str) – path of the prim in the stage

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.delete_prim("/World/Cube")
```

find_matching_prim_paths(
prim_path_regex:str,
prim_type:str|None =None,
)→List[str]Find all the matching prim paths in the stage based on Regex expression.
Parameters:

- prim_path_regex (str) – The Regex expression for prim path.

- prim_type (Optional[str]) – The type of the prims to filter, only supports articulation and rigid_body currently. Defaults to None.

Returns:
List of prim paths that match input expression.

Return type:
List[str]

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/env/Cube, /World/env_01/Cube, /World/env_02/Cube
>>> # get only the prim Cube paths from env_01 and env_02
>>> prims_utils.find_matching_prim_paths("/World/env_.*/Cube")
['/World/env_01/Cube', '/World/env_02/Cube']
```

get_all_matching_child_prims(prim_path:str,predicate:~typing.Callable[[str],bool]=<function<lambda>>,depth:int|None=None)→List[pxr.Usd.Prim]
Performs a breadth-first search starting from the root and returns all the prims matching the predicate.
Parameters:

- prim_path (str) – root prim path to start traversal from.

- predicate (Callable[[str], bool]) – predicate that checks the prim path of a prim and returns a boolean.

- depth (Optional[int]) – maximum depth for traversal, should be bigger than zero if specified. Defaults to None (i.e: traversal till the end of the tree).

Returns:
A list containing the root and children prims matching specified predicate.

Return type:
List[Usd.Prim]

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # get all hidden prims
>>> predicate = lambda path: prims_utils.is_prim_hidden_in_stage(path) # True if the prim at path is hidden
>>> prims_utils.get_all_matching_child_prims("/", predicate)
[Usd.Prim(</OmniverseKit_Persp>),
Usd.Prim(</OmniverseKit_Front>),
Usd.Prim(</OmniverseKit_Top>),
Usd.Prim(</OmniverseKit_Right>),
Usd.Prim(</Render>)]
```

get_articulation_root_api_prim_path(prim_path)
Get the prim path that has the Articulation Root API
Note
This function assumes that all prims defined by a regular expression correspond to the same articulation type
Parameters:
prim_path (str) – path or regex of the prim(s) on which to search for the prim containing the API

Returns:
path or regex of the prim(s) that has the Articulation Root API.
If no prim has been found, the same input value is returned

Return type:
str

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/env/Ant, /World/env_01/Ant, /World/env_02/Ant
>>> # search specifying the prim with the Articulation Root API
>>> prims_utils.get_articulation_root_api_prim_path("/World/env/Ant/torso")
/World/env/Ant/torso
>>> # search specifying some ancestor prim that does not have the Articulation Root API
>>> prims_utils.get_articulation_root_api_prim_path("/World/env/Ant")
/World/env/Ant/torso
>>> # regular expression search
>>> prims_utils.get_articulation_root_api_prim_path("/World/env.*/Ant")
/World/env.*/Ant/torso
```

get_first_matching_child_prim(
prim_path:str,
predicate:Callable[[str],bool],
fabric:bool=False,
)→pxr.Usd.PrimRecursively get the first USD Prim at the path string that passes the predicate function
Parameters:

- prim_path (str) – path of the prim in the stage

- predicate (Callable[[str], bool]) – Function to test the prims against

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Returns:
The first prim or child of the prim, as defined by GetChildren, that passes the predicate

Return type:
Usd.Prim

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
>>> # Get the first child prim of type Cube
>>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Cube"
>>> prims_utils.get_first_matching_child_prim("/", predicate)
Usd.Prim(</World/Cube>)
```

get_first_matching_parent_prim(
prim_path:str,
predicate:Callable[[str],bool],
)→pxr.Usd.PrimRecursively get the first USD Prim at the parent path string that passes the predicate function
Parameters:

- prim_path (str) – path of the prim in the stage

- predicate (Callable[[str], bool]) – Function to test the prims against

Returns:
The first prim on the parent path, as defined by GetParent, that passes the predicate

Return type:
str

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Get the first parent of Cube prim of type Xform
>>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Xform"
>>> prims_utils.get_first_matching_parent_prim("/World/Cube", predicate)
Usd.Prim(</World>)
```

get_prim_at_path(
prim_path:str,
fabric:bool=False,
)→pxr.Usd.Prim|usdrt.Usd._Usd.PrimGet the USD or Fabric Prim at a given path string
Parameters:

- prim_path (str) – path of the prim in the stage.

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Returns:
USD or Fabric Prim object at the given path in the current stage.

Return type:
Union[Usd.Prim, usdrt.Usd._Usd.Prim]

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.get_prim_at_path("/World/Cube")
Usd.Prim(</World/Cube>)
```

get_prim_attribute_names(
prim_path:str,
fabric:bool=False,
)→List[str]Get all the attribute names of a prim at the path
Parameters:

- prim_path (str) – path of the prim in the stage

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Raises:
Exception – If there is not a valid prim at the given path

Returns:
List of the prim attribute names

Return type:
List[str]

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.get_prim_attribute_names("/World/Cube")
['doubleSided', 'extent', 'orientation', 'primvars:displayColor', 'primvars:displayOpacity',
'purpose', 'size', 'visibility', 'xformOp:orient', 'xformOp:scale', 'xformOp:translate', 'xformOpOrder']
```

get_prim_attribute_value(
prim_path:str,
attribute_name:str,
fabric:bool=False,
)→AnyGet a prim attribute value
Parameters:

- prim_path (str) – path of the prim in the stage

- attribute_name (str) – name of the attribute to get

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Raises:
Exception – If there is not a valid prim at the given path

Returns:
Prim attribute value

Return type:
Any

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.get_prim_attribute_value("/World/Cube", attribute_name="size")
1.0
```

get_prim_children(prim:pxr.Usd.Prim)→List[pxr.Usd.Prim]
Return the call of the USD Prim’s GetChildren member function
Parameters:
prim (Usd.Prim) – The parent USD Prim

Returns:
A list of the prim’s children.

Return type:
List[Usd.Prim]

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
>>> # Get all prims under the prim World
>>> prim = prims_utils.get_prim_at_path("/World")
>>> prims_utils.get_prim_children(prim)
[Usd.Prim(</World/Cube>), Usd.Prim(</World/Cube_01>), Usd.Prim(</World/Cube_02>)]
```

get_prim_object_type(prim_path:str)→str|None
Get the dynamic control object type of the USD Prim at the given path.
If the prim at the path is of Dynamic Control type e.g.: rigid_body, joint, dof, articulation, attractor, d6joint, then the corresponding string returned. If is an Xformable prim, then “xform” is returned. Otherwise None is returned.
Parameters:
prim_path (str) – path of the prim in the stage

Raises:
Exception – If the USD Prim is not a supported type.

Returns:
String corresponding to the object type.

Return type:
str

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.get_prim_object_type("/World/Cube")
xform
```

get_prim_parent(prim:pxr.Usd.Prim)→pxr.Usd.Prim
Return the call of the USD Prim’s GetChildren member function
Parameters:
prim (Usd.Prim) – The USD Prim to call GetParent on

Returns:
The prim’s parent returned from GetParent

Return type:
Usd.Prim

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Get the prim Cube's parent
>>> prim = prims_utils.get_prim_at_path("/World/Cube")
>>> prims_utils.get_prim_parent(prim)
Usd.Prim(</World>)
```

get_prim_path(prim:pxr.Usd.Prim)→str
Get the path of a given USD prim.
Parameters:
prim (Usd.Prim) – The input USD prim.

Returns:
The path to the input prim.

Return type:
str

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prim = prims_utils.get_prim_at_path("/World/Cube") # Usd.Prim(</World/Cube>)
>>> prims_utils.get_prim_path(prim)
/World/Cube
```

get_prim_property(prim_path:str, property_name:str)→Any
Get the attribute of the USD Prim at the given path
Parameters:

- prim_path (str) – path of the prim in the stage

- property_name (str) – name of the attribute to get

Returns:
The attribute if it exists, None otherwise

Return type:
Any

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.get_prim_property("/World/Cube", property_name="size")
1.0
```

get_prim_type_name(prim_path:str, fabric:bool=False)→str
Get the TypeName of the USD Prim at the path if it is valid
Parameters:

- prim_path (str) – path of the prim in the stage

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Raises:
Exception – If there is not a valid prim at the given path

Returns:
The TypeName of the USD Prim at the path string

Return type:
str

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prims_utils.get_prim_type_name("/World/Cube")
Cube
```

is_prim_ancestral(prim_path:str)→bool
Check if any of the prims ancestors were brought in as a reference
Parameters:
prim_path (str) – The path to the USD prim.

Returns:
True if prim is part of a referenced prim, false otherwise.

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # /World/Cube is a prim created
>>> prims_utils.is_prim_ancestral("/World/Cube")
False
>>> # /World/panda is an USD file loaded (as reference) under that path
>>> prims_utils.is_prim_ancestral("/World/panda")
False
>>> prims_utils.is_prim_ancestral("/World/panda/panda_link0")
True
```

is_prim_hidden_in_stage(prim_path:str)→bool
Checks if the prim is hidden in the USd stage or not.
Warning
This function checks for the `hide_in_stage_window` prim metadata. This metadata is not related to the visibility of the prim.
Parameters:
prim_path (str) – The path to the USD prim.

Returns:
True if prim is hidden from stage window, False if not hidden.

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # prim without the 'hide_in_stage_window' metadata
>>> prims_utils.is_prim_hidden_in_stage("/World/Cube")
None
>>> # prim with the 'hide_in_stage_window' metadata set to True
>>> prims_utils.is_prim_hidden_in_stage("/World/Cube")
True
```

is_prim_no_delete(prim_path:str)→bool
Checks whether a prim can be deleted or not from USD stage.
Note
This function checks for the `no_delete` prim metadata. A prim with this metadata set to True cannot be deleted by using the edit menu, the context menu, or by calling the `delete_prim` function, for example.
Parameters:
prim_path (str) – The path to the USD prim.

Returns:
True if prim cannot be deleted, False if it can

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # prim without the 'no_delete' metadata
>>> prims_utils.is_prim_no_delete("/World/Cube")
None
>>> # prim with the 'no_delete' metadata set to True
>>> prims_utils.is_prim_no_delete("/World/Cube")
True
```

is_prim_non_root_articulation_link(prim_path:str)→bool
Used to query if the prim_path corresponds to a link in an articulation which is a non root link.
Parameters:
prim_path (str) – prim_path to query

Returns:
True if the prim path corresponds to a link in an articulation which is a non root link
and can’t have a transformation applied to it.

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # /World/panda contains the prim tree for the Franka panda robot.
>>> # The prim on this path has the Physics Articulation Root property applied
>>> prims_utils.is_prim_non_root_articulation_link("/World/panda")
False
>>> prims_utils.is_prim_non_root_articulation_link("/World/panda/panda_link0")
True
```

is_prim_path_valid(prim_path:str, fabric:bool=False)→bool
Check if a path has a valid USD Prim at it
Parameters:

- prim_path (str) – path of the prim in the stage

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Returns:
True if the path points to a valid prim

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube
>>> prims_utils.is_prim_path_valid("/World/Cube")
True
>>> prims_utils.is_prim_path_valid("/World/Cube/")
False
>>> prims_utils.is_prim_path_valid("/World/Sphere") # it doesn't exist
False
```

is_prim_root_path(prim_path:str)→bool
Checks if the input prim path is root or not.
Parameters:
prim_path (str) – The path to the USD prim.

Returns:
True if the prim path is “/”, False otherwise

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube
>>> prims_utils.is_prim_root_path("/")
True
>>> prims_utils.is_prim_root_path("/World")
False
>>> prims_utils.is_prim_root_path("/World/Cube")
False
```

move_prim(path_from:str, path_to:str)→None
Run the Move command to change a prims USD Path in the stage
Parameters:

- path_from (str) – Path of the USD Prim you wish to move

- path_to (str) – Final destination of the prim

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Move the prim Cube outside the prim World
>>> prims_utils.move_prim("/World/Cube", "/Cube")
```

query_parent_path(
prim_path:str,
predicate:Callable[[str],bool],
)→boolCheck if one of the ancestors of the prim at the prim_path can pass the predicate
Parameters:

- prim_path (str) – path to the USD Prim for which to check the ancestors

- predicate (Callable[[str], bool]) – The condition that must be True about the ancestors

Returns:
True if there is an ancestor that can pass the predicate, False otherwise

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Check is the prim Cube has an ancestor of type Xform
>>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Xform"
>>> prims_utils.query_parent_path("/World/Cube", predicate)
True
```

set_prim_attribute_value(
prim_path:str,
attribute_name:str,
value:Any,
fabric:bool=False,
)Set a prim attribute value
Parameters:

- prim_path (str) – path of the prim in the stage

- attribute_name (str) – name of the attribute to set

- value (Any) – value to set the attribute to

- fabric (bool, optional) – True for fabric stage and False for USD stage. Defaults to False.

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Set the Cube size to 5.0
>>> prims_utils.set_prim_attribute_value("/World/Cube", attribute_name="size", value=5.0)
```

set_prim_hide_in_stage_window(prim:pxr.Usd.Prim, hide:bool)
Set `hide_in_stage_window` metadata for a prim
Warning
This metadata is unrelated to the visibility of the prim. Use the `set_prim_visibility` function for the latter purpose
Parameters:

- prim (Usd.Prim) – Prim to set

- hide (bool) – True to hide in stage window, false to show

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prim = prims_utils.get_prim_at_path("/World/Cube")
>>> prims_utils.set_prim_hide_in_stage_window(prim, True)
```

set_prim_no_delete(prim:pxr.Usd.Prim, no_delete:bool)
Set `no_delete` metadata for a prim
Note
A prim with this metadata set to True cannot be deleted by using the edit menu, the context menu, or by calling the `delete_prim` function, for example.
Parameters:

- prim (Usd.Prim) – Prim to set

- no_delete (bool) – True to make prim undeletable in stage window, false to allow deletion

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> prim = prims_utils.get_prim_at_path("/World/Cube")
>>> prims_utils.set_prim_no_delete(prim, True)
```

set_prim_property(
prim_path:str,
property_name:str,
property_value:Any,
)→None Set the attribute of the USD Prim at the path
Parameters:

- prim_path (str) – path of the prim in the stage

- property_name (str) – name of the attribute to set

- property_value (Any) – value to set the attribute to

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Set the Cube size to 5.0
>>> prims_utils.set_prim_property("/World/Cube", property_name="size", property_value=5.0)
```

set_prim_visibility(prim:pxr.Usd.Prim, visible:bool)→None
Sets the visibility of the prim in the opened stage.
Note
The method does this through the USD API.
Parameters:

- prim (Usd.Prim) – the USD prim

- visible (bool) – flag to set the visibility of the usd prim in stage.

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube. Make the Cube not visible
>>> prim = prims_utils.get_prim_at_path("/World/Cube")
>>> prims_utils.set_prim_visibility(prim, False)
```

set_targets(
prim:pxr.Usd.Prim,
attribute:str,
target_prim_paths:list,
)Set targets for a prim relationship attribute
Parameters:

- prim (Usd.Prim) – Prim to create and set attribute on

- attribute (str) – Relationship attribute to create

- target_prim_paths (list) – list of targets to set

Example:

```
>>> import isaacsim.core.utils.prims as prims_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
>>> # Set each prim Cube to the relationship targetPrim of the prim World
>>> prim = prims_utils.get_prim_at_path("/World")
>>> targets = ["/World/Cube", "/World/Cube_01", "/World/Cube_02"]
>>> prims_utils.set_targets(prim, "targetPrim", targets)
```

### Random Utils
get_random_translation_from_camera(
min_distance:float,
max_distance:float,
fov_x:float,
fov_y:float,
fraction_to_screen_edge:float,
)→ndarrayGet a random translation from the camera, in the camera’s frame, that’s in view of the camera.
Parameters:

- min_distance (float) – minimum distance away from the camera (along the optical axis) of the random translation.

- max_distance (float) – maximum distance away from the camera (along the optical axis) of the random translation.

- fov_x (float) – field of view of the camera in the x-direction in radians.

- fov_y (float) – field of view of the camera in the y-direction in radians.

- fraction_to_screen_edge (float) – maximum allowed fraction to the edge of the screen the translated point may appear when viewed from the camera. A value of 0 corresponds to the translated point being centered in the camera’s view (on the optical axis), whereas a value of 1 corresponds to the translated point being on the edge of the screen in the camera’s view.

Returns:
random translation from the camera, in the camera’s frame, that’s in view of the camera. Shape
is (3, ).

Return type:
np.ndarray

get_random_values_in_range(
min_range:ndarray,
max_range:ndarray,
)→ndarrayGet an array of random values where each element is between the corresponding min_range and max_range element.
Parameters:

- min_range (np.ndarray) – minimum values for each corresponding element of the array of random values. Shape is (num_values, ).

- max_range (np.ndarray) – maximum values for each corresponding element of the array of random values. Shape is (num_values, ).

Returns:
array of random values. Shape is (num_values, ).

Return type:
np.ndarray

get_random_world_pose_in_view(
camera_prim:pxr.Usd.Prim,
min_distance:float,
max_distance:float,
fov_x:float,
fov_y:float,
fraction_to_screen_edge:float,
coord_prim:pxr.Usd.Prim,
min_rotation_range:ndarray,
max_rotation_range:ndarray,
)→Tuple[ndarray,ndarray]Get a pose defined in the world frame that’s in view of the camera.
Parameters:

- camera_prim (Usd.Prim) – prim path of the camera.

- min_distance (float) – minimum distance away from the camera (along the optical axis) of the random translation.

- max_distance (float) – maximum distance away from the camera (along the optical axis) of the random translation.

- fov_x (float) – field of view of the camera in the x-direction in radians.

- fov_y (float) – field of view of the camera in the y-direction in radians.

- fraction_to_screen_edge (float) – maximum allowed fraction to the edge of the screen the translated point may appear when viewed from the camera. A value of 0 corresponds to the translated point being centered in the camera’s view (on the optical axis), whereas a value of 1 corresponds to the translated point being on the edge of the screen in the camera’s view.

- coord_prim (Usd.Prim) – prim whose frame the orientation is defined with respect to.

- min_rotation_range (np.ndarray) – minimum XYZ Euler angles of the random pose, defined with respect to the frame of the prim at coord_prim. Shape is (3, ).

- max_rotation_range (np.ndarray) – maximum XYZ Euler angles of the random pose, defined with respect to the frame of the prim at coord_prim.

Returns:
first index is position in the world frame. Shape is (3, ). Second index is
quaternion orientation in the world frame. Quaternion is scalar-first (w, x, y, z). Shape is (4, ).

Return type:
Tuple[np.ndarray, np.ndarray]

### Render Product Utils
add_aov(render_product_path:str, aov_name:str)
Adds an AOV/Render Var to an existing render product
Parameters:

- render_product_path (str) – path to the render product prim

- aov_name (str) – Name of the render var we want to add to this render product

Raises:

- RuntimeError – If the render product path is invalid

- RuntimeError – If the renderVar could not be created

- RuntimeError – If the renderVar could not be added to the render product

create_hydra_texture(
resolution:Tuple[int],
camera_prim_path:str,
)get_camera_prim_path(render_product_path:str)
Get the current camera for a render product
Parameters:
render_product_path (str) – path to the render product prim

Raises:
RuntimeError – If the render product path is invalid

Returns:
Path to the camera prim attached to this render product

Return type:
str

get_resolution(render_product_path:str)
Get resolution for a render product
Parameters:
render_product_path (str) – path to the render product prim

Raises:
RuntimeError – If the render product path is invalid

Returns:
(width,height)

Return type:
Tuple[int]

set_camera_prim_path(render_product_path:str, camera_prim_path:str)
Sets the camera prim path for a render product
Parameters:

- render_product_path (str) – path to the render product prim

- camera_prim_path (str) – path to the camera prim

Raises:
RuntimeError – If the render product path is invalid

set_resolution(
render_product_path:str,
resolution:Tuple[int],
)Set resolution for a render product
Parameters:

- render_product_path (str) – path to the render product prim

- resolution (Tuple[float]) – width,height for render product

Raises:
RuntimeError – If the render product path is invalid

### Rotations Utils
euler_angles_to_quat(
euler_angles:ndarray,
degrees:bool=False,
extrinsic:bool=True,
)→ndarrayConvert Euler angles to quaternion.
Parameters:

- euler_angles (np.ndarray) – Euler XYZ angles.

- degrees (bool, optional) – Whether input angles are in degrees. Defaults to False.

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
quaternion (w, x, y, z).

Return type:
np.ndarray

euler_to_rot_matrix(
euler_angles:ndarray,
degrees:bool=False,
extrinsic:bool=True,
)→ndarrayConvert Euler XYZ or ZYX angles to rotation matrix.
Parameters:

- euler_angles (np.ndarray) – Euler angles.

- degrees (bool, optional) – Whether passed angles are in degrees.

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
A 3x3 rotation matrix in its extrinsic or intrinsic form depends on the extrinsic argument.

Return type:
np.ndarray

gf_quat_to_np_array(
orientation:pxr.Gf.Quatd|pxr.Gf.Quatf|pxr.Gf.Quaternion,
)→ndarrayConverts a pxr Quaternion type to a numpy array following [w, x, y, z] convention.
Parameters:
orientation (Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]) – Input quaternion object.

Returns:
A (4,) quaternion array in (w, x, y, z).

Return type:
np.ndarray

gf_rotation_to_np_array(
orientation:pxr.Gf.Rotation,
)→ndarrayConverts a pxr Rotation type to a numpy array following [w, x, y, z] convention.
Parameters:
orientation (Gf.Rotation) – Pxr rotation object.

Returns:
A (4,) quaternion array in (w, x, y, z).

Return type:
np.ndarray

lookat_to_quatf(
camera:pxr.Gf.Vec3f,
target:pxr.Gf.Vec3f,
up:pxr.Gf.Vec3f,
)→pxr.Gf.Quatf[summary]
Parameters:

- camera (Gf.Vec3f) – [description]

- target (Gf.Vec3f) – [description]

- up (Gf.Vec3f) – [description]

Returns:
Pxr quaternion object.

Return type:
Gf.Quatf

matrix_to_euler_angles(
mat:ndarray,
degrees:bool=False,
extrinsic:bool=True,
)→ndarrayConvert rotation matrix to Euler XYZ extrinsic or intrinsic angles.
Parameters:

- mat (np.ndarray) – A 3x3 rotation matrix.

- degrees (bool, optional) – Whether returned angles should be in degrees.

- extrinsic (bool, optional) – True if the rotation matrix follows the extrinsic matrix convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic matrix conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
Euler XYZ angles (intrinsic form) if extrinsic is False and Euler XYZ angles (extrinsic form) if extrinsic is True.

Return type:
np.ndarray

quat_to_euler_angles(
quat:ndarray,
degrees:bool=False,
extrinsic:bool=True,
)→ndarrayConvert input quaternion to Euler XYZ or ZYX angles.
Parameters:

- quat (np.ndarray) – Input quaternion (w, x, y, z).

- degrees (bool, optional) – Whether returned angles should be in degrees. Defaults to False.

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
Euler XYZ angles (intrinsic form) if extrinsic is False and Euler XYZ angles (extrinsic form) if extrinsic is True.

Return type:
np.ndarray

quat_to_rot_matrix(quat:ndarray)→ndarray
Convert input quaternion to rotation matrix.
Parameters:
quat (np.ndarray) – Input quaternion (w, x, y, z).

Returns:
A 3x3 rotation matrix.

Return type:
np.ndarray

rot_matrix_to_quat(mat:ndarray)→ndarray
Convert rotation matrix to Quaternion.
Parameters:
mat (np.ndarray) – A 3x3 rotation matrix.

Returns:
quaternion (w, x, y, z).

Return type:
np.ndarray

### Semantics Utils
add_labels(
prim:pxr.Usd.Prim,
labels:list[str],
instance_name:str='class',
overwrite:bool=True,
)→None Apply semantic labels to a prim using the UsdSemantics.LabelsAPI.
Parameters:

- prim (Usd.Prim) – Usd Prim to add or update labels on.

- labels (list) – The list of labels to apply.

- instance_name (str, optional) – The name of the semantic instance. Defaults to “class”.

- overwrite (bool, optional) – If True (default), existing labels for this instance are replaced. If False, the new labels are appended to existing ones (if any).

add_update_semantics(
prim:pxr.Usd.Prim,
semantic_label:str,
type_label:str='class',
suffix='',
)→None [DEPRECATED] Apply a semantic label to a prim or update an existing label using the old SemanticsAPI.
Parameters:

- prim (Usd.Prim) – Usd Prim to add or update semantics on

- semantic_label (str) – The label we want to apply

- type_label (str) – The type of semantic information we are specifying (default = “class”)

- suffix (str) – Additional suffix used to specify multiple semantic attribute names.

check_incorrect_labels(
prim_path:str|None =None,
)→list[list[str]]Returns a list of [prim_path, label] for meshes where at least one semantic label (LabelsAPI)
is not found within the prim’s path string (case-insensitive, ignoring ‘_’ and ‘-‘).

Parameters:
prim_path (str | None) – This will check Prim path and its childrens’ labels. If None, checks the whole stage.

Returns:
List containing pairs of [prim_path, first_incorrect_label].

Return type:
list[list[str]]

check_incorrect_semantics(
prim_path:str=None,
)→List[List[str]][DEPRECATED] Returns a list of prim path of meshes with different semantics labels (old SemanticsAPI) than their prim path and their semantic labels
Parameters:
prim_path (str) – This will check Prim path and its childrens’ semantics

Returns:
List of prim path and semantic label

Return type:
List[List[str]]

check_missing_labels(prim_path:str|None =None)→list[str]
Returns a list of prim paths of meshes with missing semantic labels (UsdSemantics.LabelsAPI).
Parameters:
prim_path (str | None) – This will check Prim path and its childrens’ labels. If None, checks the whole stage.

Returns:
Prim paths of meshes with no LabelsAPI applied.

Return type:
list[str]

check_missing_semantics(prim_path:str=None)→List[str]
[DEPRECATED] Returns a list of prim path of meshes with missing semantics (old SemanticsAPI)
Parameters:
prim_path (str) – This will check Prim path and its childrens’ semantics

Returns:
Prim paths

Return type:
List[str]

count_labels_in_scene(prim_path:str|None =None)→dict[str,int]
Returns a dictionary of semantic labels (UsdSemantics.LabelsAPI) and their corresponding count.
Parameters:
prim_path (str | None) – This will check Prim path and its childrens’ labels. If None, checks the whole stage.

Returns:
Dictionary mapping individual labels to their total count across all instances.
Includes a ‘missing_labels’ count for meshes with no LabelsAPI.

Return type:
dict[str, int]

count_semantics_in_scene(
prim_path:str=None,
)→Dict[str,int][DEPRECATED] Returns a dictionary of labels (old SemanticsAPI) and the corresponding count
Parameters:
prim_path (str) – This will check Prim path and its childrens’ semantics

Returns:
labels and count

Return type:
Dict[str, int]

get_labels(prim:pxr.Usd.Prim)→dict[str,list[str]]
Returns semantic labels (UsdSemantics.LabelsAPI) applied to a prim.
Parameters:
prim (Usd.Prim) – Prim to return labels for.

Returns:
Dictionary mapping instance names to a list of labels.
Returns an empty dict if no LabelsAPI instances are found.

Return type:
dict[str, list[str]]

get_semantics(
prim:pxr.Usd.Prim,
)→Dict[str,Tuple[str,str]][DEPRECATED] Returns semantics (old SemanticsAPI) that are applied to a prim
Parameters:
prim (Usd.Prim) – Prim to return semantics for

Returns:
Dictionary containing the name of the applied semantic, and the type and data associated with that semantic.

Return type:
Dict[str, Tuple[str,str]]

remove_all_semantics(
prim:pxr.Usd.Prim,
recursive:bool=False,
)→None [DEPRECATED] Removes all semantic tags (old SemanticsAPI) from a given prim and its children
Parameters:

- prim (Usd.Prim) – Prim to remove any applied semantic APIs on

- recursive (bool, optional) – Also traverse children and remove semantics recursively. Defaults to False.

remove_labels(
prim:pxr.Usd.Prim,
instance_name:str|None =None,
include_descendants:bool=False,
)→None Removes semantic labels (UsdSemantics.LabelsAPI) from a prim.
Parameters:

- prim (Usd.Prim) – Prim to remove labels from.

- instance_name (str | None, optional) – Specific instance name to remove. If None (default), removes all LabelsAPI instances.

- include_descendants (bool, optional) – Also traverse children and remove labels recursively. Defaults to False.

upgrade_prim_semantics_to_labels(
prim:pxr.Usd.Prim,
include_descendants:bool=False,
)→intUpgrades a prim and optionally its descendants from the deprecated SemanticsAPI to the new UsdSemantics.LabelsAPI.
Converts each found SemanticsAPI instance on the processed prim(s) to a corresponding LabelsAPI instance. The old ‘semanticType’ becomes the new LabelsAPI ‘instance_name’, and the old ‘semanticData’ becomes the single label in the new ‘labels’ list. The old SemanticsAPI is always removed after upgrading.
Parameters:

- prim (Usd.Prim) – The starting prim to upgrade.

- include_descendants (bool, optional) – If True, upgrades the prim and all its descendants. If False (default), upgrades only the specified prim.

Returns:
The total number of SemanticsAPI instances successfully upgraded to LabelsAPI.

Return type:
int

### Stage Utils
add_reference_to_stage(
usd_path:str,
prim_path:str,
prim_type:str='Xform',
)→pxr.Usd.PrimAdd USD reference to the opened stage at specified prim path.
Adds a reference to an external USD file at the specified prim path on the current stage. If the prim does not exist, it will be created with the specified type. This function also handles stage units verification to ensure compatibility.
Parameters:

- usd_path – The path to USD file to reference.

- prim_path – The prim path where the reference will be attached.

- prim_type – The type of prim to create if it doesn’t exist. Defaults to “Xform”.

Returns:
The USD prim at the specified prim path.

Raises:
FileNotFoundError – When the input USD file is not found at the specified path.

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # load an USD file (franka.usd) to the stage under the path /World/panda
>>> prim = stage_utils.add_reference_to_stage(
... usd_path="/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd",
... prim_path="/World/panda"
... )
>>> prim
Usd.Prim(</World/panda>)
```

clear_stage(
predicate:Callable[[str],bool]|None =None,
)→None Deletes all prims in the stage without populating the undo command buffer
Parameters:
predicate (Optional[Callable[[str], bool]], optional) – user defined function that takes a prim_path (str) as input and returns True/False if the prim should/shouldn’t be deleted. If predicate is None, a default is used that deletes all prims

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # clear the whole stage
>>> stage_utils.clear_stage()
>>>
>>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
>>> # Delete only the prims of type Cube
>>> predicate = lambda path: prims_utils.get_prim_type_name(path) == "Cube"
>>> stage_utils.clear_stage(predicate) # after the execution the stage will be /World
```

close_stage(callback_fn:Callable=None)→bool
Closes the current opened USD stage.
Note
Once the stage is closed, it is necessary to open a new stage or create a new one in order to work on it.
Parameters:
callback_fn (Callable, optional) – Callback function to call while closing. Defaults to None.

Returns:
True if operation is successful, otherwise false.

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.close_stage()
True
```

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> def callback(*args, **kwargs):
... print("callback:", args, kwargs)
...
>>> stage_utils.close_stage(callback)
True
>>> stage_utils.close_stage(callback)
callback: (False, 'Stage opening or closing already in progress!!') {}
False
```

create_new_stage()→pxr.Usd.Stage
Create a new stage attached to the USD context.
Returns:
The created USD stage.

Return type:
Usd.Stage

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.create_new_stage()
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x7fba6c04f840:World7.usd'),
sessionLayer=Sdf.Find('anon:0x7fba6c01c5c0:World7-session.usda'),
pathResolverContext=<invalid repr>)
```

asynccreate_new_stage_async()→None
Create a new stage (asynchronous version).
Example:

```
>>> import asyncio
>>> import isaacsim.core.utils.stage as stage_utils
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await stage_utils.create_new_stage_async()
...
>>> run_coroutine(task())
```

create_new_stage_in_memory()→pxr.Usd.Stage
Create a new stage in memory.
Returns:
The created USD stage.

Return type:
Usd.Stage

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.create_new_stage_in_memory()
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0xf7b00e0:tmp.usda'),
sessionLayer=Sdf.Find('anon:0xf7cd2e0:tmp-session.usda'),
pathResolverContext=<invalid repr>)
```

get_current_stage(
fabric:bool=False,
)→pxr.Usd.Stage|usdrt.Usd._Usd.StageGet the current open USD or Fabric stage
Parameters:
fabric (bool, optional) – True to get the fabric stage. False to get the USD stage. Defaults to False.

Returns:
The USD or Fabric stage as specified by the input arg fabric.

Return type:
Union[Usd.Stage, usdrt.Usd._Usd.Stage]

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.get_current_stage()
Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x7fba6c04f840:World7.usd'),
sessionLayer=Sdf.Find('anon:0x7fba6c01c5c0:World7-session.usda'),
pathResolverContext=<invalid repr>)
```

get_current_stage_id()→int
Get the current open stage id
Returns:
The stage id.

Return type:
int

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.get_current_stage_id()
1234567890
```

get_next_free_path(path:str, parent:str=None)→str
Returns the next free usd path for the current stage
Parameters:

- path (str) – path we want to check

- parent (str, optional) – Parent prim for the given path. Defaults to None.

Returns:
a new path that is guaranteed to not exist on the current stage

Return type:
str

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01.
>>> # Get the next available path for /World/Cube
>>> stage_utils.get_next_free_path("/World/Cube")
/World/Cube_02
```

get_stage_units()→float
Get the stage meters per unit currently set
The most common units and their values are listed in the following table:

[TABLE]
Unit | Value
kilometer (km) | 1000.0
meters (m) | 1.0
inch (in) | 0.0254
centimeters (cm) | 0.01
millimeter (mm) | 0.001
[/TABLE]
Returns:
current stage meters per unit

Return type:
float

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.get_stage_units()
1.0
```

get_stage_up_axis()→str
Get the current up-axis of USD stage.
Returns:
The up-axis of the stage.

Return type:
str

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.get_stage_up_axis()
Z
```

is_stage_loading()→bool
Convenience function to see if any files are being loaded.
Returns:
True if loading, False otherwise

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.is_stage_loading()
False
```

open_stage(usd_path:str)→bool
Open the given usd file and replace currently opened stage.
Parameters:
usd_path (str) – Path to the USD file to open.

Raises:
ValueError – When input path is not a supported file type by USD.

Returns:
True if operation is successful, otherwise false.

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.open_stage("/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd")
True
```

asyncopen_stage_async(usd_path:str)→Tuple[bool,int]
Open the given usd file and replace currently opened stage (asynchronous version).
Parameters:
usd_path (str) – Path to the USD file to open.

Raises:
ValueError – When input path is not a supported file type by USD.

Returns:
True if operation is successful, otherwise false.

Return type:
bool

Example:

```
>>> import asyncio
>>> import isaacsim.core.utils.stage as stage_utils
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await stage_utils.open_stage_async("/home/<user>/Documents/Assets/Robots/FrankaRobotics/FrankaPanda/franka.usd")
...
>>> run_coroutine(task())
```

print_stage_prim_paths(fabric:bool=False)→None
Traverses the stage and prints all prim (hidden or not) paths.
Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
>>> stage_utils.print_stage_prim_paths()
/Render
/World
/World/Cube
/World/Cube_01
/World/Cube_02
/OmniverseKit_Persp
/OmniverseKit_Front
/OmniverseKit_Top
/OmniverseKit_Right
```

remove_deleted_references()
Clean up deleted references in the current USD stage.
Removes any deleted items from both payload and references lists for all prims in the stage’s root layer. Prints information about any deleted items that were cleaned up.
Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>> stage_utils.remove_deleted_references()
Removed 2 deleted payload items from </World/Robot>
Removed 1 deleted reference items from </World/Scene>
```

save_stage(usd_path:str, save_and_reload_in_place=True)→bool
Save usd file to path, it will be overwritten with the current stage
Parameters:

- usd_path (str) – File path to save the current stage to

- save_and_reload_in_place (bool, optional) – use `save_as_stage` to save and reload the root layer in place. Defaults to True.

Raises:
ValueError – When input path is not a supported file type by USD.

Returns:
True if operation is successful, otherwise false.

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.save_stage("/home/<user>/Documents/Save/stage.usd")
True
```

set_livesync_stage(usd_path:str, enable:bool)→bool
Save the stage and set the Live Sync mode for real-time live editing of shared files on a Nucleus server
Parameters:

- usd_path (str) – path to enable live sync for, it will be overwritten with the current stage

- enable (bool) – True to enable livesync, false to disable livesync

Returns:
True if operation is successful, otherwise false.

Return type:
bool

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.set_livesync_stage("omniverse://localhost/Users/Live/stage.usd", enable=True)
server omniverse://localhost: ConnectionStatus.CONNECTING
server omniverse://localhost: ConnectionStatus.CONNECTED
True
```

set_stage_units(stage_units_in_meters:float)→None
Set the stage meters per unit
The most common units and their values are listed in the following table:

[TABLE]
Unit | Value
kilometer (km) | 1000.0
meters (m) | 1.0
inch (in) | 0.0254
centimeters (cm) | 0.01
millimeter (mm) | 0.001
[/TABLE]
Parameters:
stage_units_in_meters (float) – units for stage

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.set_stage_units(1.0)
```

set_stage_up_axis(axis:str='z')→None
Change the up axis of the current stage
Parameters:
axis (UsdGeom.Tokens, optional) – valid values are `"x"`, `"y"` and `"z"`

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # set stage up axis to Y-up
>>> stage_utils.set_stage_up_axis("y")
```

traverse_stage(fabric=False)→Iterable
Traverse through prims (hidden or not) in the opened Usd stage.
Returns:
Generator which yields prims from the stage in depth-first-traversal order.

Return type:
Iterable

Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> # given the stage: /World/Cube, /World/Cube_01, /World/Cube_02.
>>> # Traverse through prims in the stage
>>> for prim in stage_utils.traverse_stage():
>>> print(prim)
Usd.Prim(</World>)
Usd.Prim(</World/Cube>)
Usd.Prim(</World/Cube_01>)
Usd.Prim(</World/Cube_02>)
Usd.Prim(</OmniverseKit_Persp>)
Usd.Prim(</OmniverseKit_Front>)
Usd.Prim(</OmniverseKit_Top>)
Usd.Prim(</OmniverseKit_Right>)
Usd.Prim(</Render>)
```

update_stage()→None
Update the current USD stage.
Example:

```
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_utils.update_stage()
```

asyncupdate_stage_async()→None
Update the current USD stage (asynchronous version).
Example:

```
>>> import asyncio
>>> import isaacsim.core.utils.stage as stage_utils
>>> from omni.kit.async_engine import run_coroutine
>>>
>>> async def task():
... await stage_utils.update_stage_async()
...
>>> run_coroutine(task())
```

use_stage(stage:pxr.Usd.Stage)→None
Context manager that sets a thread-local stage.
Parameters:
stage – The stage to set in the context.

Raises:
AssertionError – If the stage is not a USD stage instance.

Example:

```
>>> from pxr import Usd
>>> import isaacsim.core.utils.stage as stage_utils
>>>
>>> stage_in_memory = Usd.Stage.CreateInMemory()
>>> with stage_utils.use_stage(stage_in_memory):
... # operate on the specified stage
... pass
>>> # operate on the default stage attached to the USD context
```

### String Utils
find_root_prim_path_from_regex(
prim_path_regex:str,
)→Tuple[str,int]Find the first prim above the regex pattern prim and its position.
Parameters:
prim_path_regex (str) – full prim path including the regex pattern prim.

Returns:
First position is the prim path to the parent of the regex prim.
Second position represents the level of the regex prim in the USD stage tree representation.

Return type:
Tuple[str, int]

find_unique_string_name(
initial_name:str,
is_unique_fn:Callable[[str],bool],
)→strFind a unique string name based on the predicate function provided.
The string is appended with “_N”, where N is a natural number till the resultant string is unique.
Parameters:

- initial_name (str) – The initial string name.

- is_unique_fn (Callable[[str], bool]) – The predicate function to validate against.

Returns:
A unique string based on input function.

Return type:
str

### Transformations Utils
get_relative_transform(
source_prim:pxr.Usd.Prim,
target_prim:pxr.Usd.Prim,
)→ndarrayGet the relative transformation matrix from the source prim to the target prim.
Parameters:

- source_prim (Usd.Prim) – source prim from which frame to compute the relative transform.

- target_prim (Usd.Prim) – target prim to which frame to compute the relative transform.

Returns:
Column-major transformation matrix with shape (4, 4).

Return type:
np.ndarray

get_transform_with_normalized_rotation(
transform:ndarray,
)→ndarrayGet the transform after normalizing rotation component.
Parameters:
transform (np.ndarray) – transformation matrix with shape (4, 4).

Returns:
transformation matrix with normalized rotation with shape (4, 4).

Return type:
np.ndarray

get_translation_from_target(
translation_from_source:ndarray,
source_prim:pxr.Usd.Prim,
target_prim:pxr.Usd.Prim,
)→ndarrayGet a translation with respect to the target’s frame, from a translation in the source’s frame.
Parameters:

- translation_from_source (np.ndarray) – translation from the frame of the prim at source_path. Shape is (3, ).

- source_prim (Usd.Prim) – prim path of the prim whose frame the original/untransformed translation (translation_from_source) is defined with respect to.

- target_prim (Usd.Prim) – prim path of the prim whose frame corresponds to the target frame that the returned translation will be defined with respect to.

Returns:
translation with respect to the target’s frame. Shape is (3, ).

Return type:
np.ndarray

get_world_pose_from_relative(
coord_prim:pxr.Usd.Prim,
relative_translation:ndarray,
relative_orientation:ndarray,
)→Tuple[ndarray,ndarray]Get a pose defined in the world frame from a pose defined relative to the frame of the coord_prim.
Parameters:

- coord_prim (Usd.Prim) – path of the prim whose frame the relative pose is defined with respect to.

- relative_translation (np.ndarray) – translation relative to the frame of the prim at prim_path. Shape is (3, ).

- relative_orientation (np.ndarray) – quaternion orientation relative to the frame of the prim at prim_path. Quaternion is scalar-first (w, x, y, z). Shape is (4, ).

Returns:
first index is position in the world frame. Shape is (3, ). Second index is
quaternion orientation in the world frame. Quaternion is scalar-first (w, x, y, z). Shape is (4, ).

Return type:
Tuple[np.ndarray, np.ndarray]

pose_from_tf_matrix(
transformation:ndarray,
)→Tuple[ndarray,ndarray]Gets pose corresponding to input transformation matrix.
Parameters:
transformation (np.ndarray) – Column-major transformation matrix. shape is (4, 4).

Returns:
first index is translation corresponding to transformation. shape is (3, ).
second index is quaternion orientation corresponding to transformation. quaternion is scalar-first (w, x, y, z). shape is (4, ).

Return type:
Tuple[np.ndarray, np.ndarray]

tf_matrices_from_poses(
translations:ndarray|Tensor,
orientations:ndarray|Tensor,
)→ndarray|Tensor[summary]
Parameters:

- translations (Union[np.ndarray, torch.Tensor]) – translations with shape (N, 3).

- orientations (Union[np.ndarray, torch.Tensor]) – quaternion representation (scalar first) with shape (N, 4).

Returns:
transformation matrices with shape (N, 4, 4)

Return type:
Union[np.ndarray, torch.Tensor]

tf_matrix_from_pose(
translation:Sequence[float],
orientation:Sequence[float],
)→ndarrayCompute input pose to transformation matrix.
Parameters:

- pos (Sequence[float]) – The translation vector.

- rot (Sequence[float]) – The orientation quaternion.

Returns:
A 4x4 matrix.

Return type:
np.ndarray

### Types Utils
classArticulationAction(
joint_positions:List|ndarray|None =None,
joint_velocities:List|ndarray|None =None,
joint_efforts:List|ndarray|None =None,
joint_indices:List|ndarray|None =None,
)Bases: `object`
[summary]
Parameters:

- joint_positions (Optional[Union[List, np.ndarray]], optional) – [description]. Defaults to None.

- joint_velocities (Optional[Union[List, np.ndarray]], optional) – [description]. Defaults to None.

- joint_efforts (Optional[Union[List, np.ndarray]], optional) – [description]. Defaults to None.

get_dict()→dict
[summary]
Returns:
[description]

Return type:
dict

get_dof_action(index:int)→dict
[summary]
Parameters:
index (int) – [description]

Returns:
[description]

Return type:
dict

get_length()→int|None
[summary]
Returns:
[description]

Return type:
Optional[int]

classArticulationActions(
joint_positions:List|ndarray|None =None,
joint_velocities:List|ndarray|None =None,
joint_efforts:List|ndarray|None =None,
joint_indices:List|ndarray|None =None,
joint_names:List[str]|None =None,
)Bases: `object`
[summary]
Parameters:

- joint_positions (Optional[Union[List, np.ndarray]], optional) – [description]. Defaults to None.

- joint_velocities (Optional[Union[List, np.ndarray]], optional) – [description]. Defaults to None.

- joint_efforts (Optional[Union[List, np.ndarray]], optional) – [description]. Defaults to None.

- joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional) – joint indices to specify which joints to manipulate. Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

- joint_names (Optional[List[str]]) – joint names to specify which joints to manipulate (can’t be sppecified together with joint_indices). Shape (K,). Where K <= num of dofs. Defaults to None (i.e: all dofs).

classDOFInfo(prim_path:str, handle:int, prim:pxr.Usd.Prim, index:int)
Bases: `object`
[summary]
Parameters:

- prim_path (str) – [description]

- handle (int) – [description]

- prim (Usd.Prim) – [description]

- index (int) – [description]

classDataFrame(current_time_step:int, current_time:float, data:dict)
Bases: `object`
[summary]
Parameters:

- current_time_step (int) – [description]

- current_time (float) – [description]

- data (dict) – [description]

get_dict()→dict
[summary]
Returns:
[description]

Return type:
dict

classmethodinit_from_dict(dict_representation:dict)
[summary]
Parameters:
dict_representation (dict) – [description]

Returns:
[description]

Return type:
DataFrame

classDynamicState(
position:ndarray,
orientation:ndarray,
linear_velocity:ndarray,
angular_velocity:ndarray,
)Bases: `object`
[summary]
Parameters:

- position (np.ndarray) – [description]

- orientation (np.ndarray) – [description]

classDynamicsViewState(
positions:ndarray|Tensor,
orientations:ndarray|Tensor,
linear_velocities:ndarray|Tensor,
angular_velocities:ndarray|Tensor,
)Bases: `object`
[summary]
Parameters:

- position (np.ndarray) – [description]

- orientation (np.ndarray) – [description]

classJointsState(
positions:ndarray,
velocities:ndarray,
efforts:ndarray,
)Bases: `object`
[summary]
Parameters:

- positions (np.ndarray) – [description]

- velocities (np.ndarray) – [description]

- efforts (np.ndarray) – [description]

classXFormPrimState(position:ndarray, orientation:ndarray)
Bases: `object`
[summary]
Parameters:

- position (np.ndarray) – [description]

- orientation (np.ndarray) – [description]

classXFormPrimViewState(
positions:ndarray|Tensor,
orientations:ndarray|Tensor,
)Bases: `object`
[summary]
Parameters:

- positions (Union[np.ndarray, torch.Tensor]) – positions with shape of (N, 3).

- orientations (Union[np.ndarray, torch.Tensor]) – quaternion representation of orientation (scalar first) with shape (N, 4).

### Viewports Utils
add_aov_to_viewport(viewport_api, aov_name:str)
backproject_depth(
depth_image:array,
viewport_api:Any,
max_clip_depth:float,
)→arrayBackproject depth image to image space
Parameters:

- depth_image (np.array) – Depth image buffer

- viewport_api (Any) – Handle to viewport api

- max_clip_depth (float) – Depth values larger than this will be clipped

Returns:
[description]

Return type:
np.array

create_viewport_for_camera(
viewport_name:str,
camera_prim_path:str,
width:int=1280,
height:int=720,
position_x:int=0,
position_y:int=0,
)Create a new viewport and peg it to a specific camera specified by camera_prim_path. If the viewport already exists with the specified viewport_name, that viewport will be replaced with the new camera view.
Parameters:

- viewport_name (str) – name of the viewport. If not provided, it will default to camera name.

- camera_prim_path (str) – name of the prim path of the camera

- width (int) – width of the viewport window, in pixels.

- height (int) – height of the viewport window, in pixels.

- position_x (int) – location x of the viewport window.

- position_y (int) – location y of the viewport window.

destroy_all_viewports(
usd_context_name:str=None,
destroy_main_viewport=True,
)Destroys all viewport windows
Parameters:

- usd_context_name (str, optional) – usd context to use. Defaults to None.

- destroy_main_viewport (bool, optional) – set to true to not destroy the default viewport. Defaults to False.

get_id_from_index(index)
Get the viewport id for a given index. This function was added for backwards compatibility for VP2 as viewport IDs are not the same as the viewport index
Parameters:
index (_type_) – viewport index to retrieve ID for

Returns:
Returns None if window index was not found

Return type:
viewport id

get_intrinsics_matrix(viewport_api:Any)→ndarray
Get intrinsic matrix for the camera attached to a specific viewport
Parameters:
viewport (Any) – Handle to viewport api

Returns:
the intrinsic matrix associated with the specified viewport
The following image convention is assumed:
+x should point to the right in the image +y should point down in the image

Return type:
np.ndarray

get_viewport_names(usd_context_name:str=None)→List[str]
Get list of all viewport names
Parameters:
usd_context_name (str, optional) – usd context to use. Defaults to None.

Returns:
List of viewport names

Return type:
List[str]

get_window_from_id(id, usd_context_name:str=None)
Find window that matches a given viewport id
Parameters:

- id (_type_) – Viewport ID to get window for

- usd_context_name (str, optional) – usd context to use. Defaults to None.

Returns:
Returns None if window with matching ID was not found

Return type:
Window

project_depth_to_worldspace(
depth_image:array,
viewport_api:Any,
max_clip_depth:float,
)→List[carb.Float3]Project depth image to world space
Parameters:

- depth_image (np.array) – Depth image buffer

- viewport_api (Any) – Handle to viewport api

- max_clip_depth (float) – Depth values larger than this will be clipped

Returns:
List of points from depth in world space

Return type:
List[carb.Float3]

set_active_viewport_camera(camera_prim_path:str)
Sets the camera for the active viewport.
This method sets the active viewport to display the camera at the specified prim path.
Parameters:
camera_prim_path (str) – name of the prim path of the camera

set_camera_view(
eye:array,
target:array,
camera_prim_path:str='/OmniverseKit_Persp',
viewport_api=None,
)→None Set the location and target for a camera prim in the stage given its path
Parameters:

- eye (np.ndarray) – Location of camera.

- target (np.ndarray,) – Location of camera target.

- camera_prim_path (str, optional) – Path to camera prim being set. Defaults to “/OmniverseKit_Persp”.

set_intrinsics_matrix(
viewport_api:Any,
intrinsics_matrix:ndarray,
focal_length:float=1.0,
)→None Set intrinsic matrix for the camera attached to a specific viewport
Note
We assume cx and cy are centered in the camera horizontal_aperture_offset and vertical_aperture_offset are computed and set on the camera prim but are not used
Parameters:

- viewport (Any) – Handle to viewport api

- intrinsics_matrix (np.ndarray) – A 3x3 intrinsic matrix

- focal_length (float, optional) – Default focal length to use when computing aperture values. Defaults to 1.0.

Raises:

- ValueError – If intrinsic matrix is not a 3x3 matrix.

- ValueError – If camera prim is not valid

### XForms Utils
clear_xform_ops(prim:pxr.Usd.Prim)
Remove all xform ops from input prim.
Parameters:
prim (Usd.Prim) – The input USD prim.

get_local_pose(prim_path)
get_world_pose(prim_path, fabric=False)
reset_and_set_xform_ops(
prim:pxr.Usd.Prim,
translation:pxr.Gf.Vec3d,
orientation:pxr.Gf.Quatd,
scale:pxr.Gf.Vec3d=pxr.Gf.Vec3d,
)Reset xform ops to isaac sim defaults, and set their values
Parameters:

- prim (Usd.Prim) – Prim to reset

- translation (Gf.Vec3d) – translation to set

- orientation (Gf.Quatd) – orientation to set

- scale (Gf.Vec3d, optional) – scale to set. Defaults to Gf.Vec3d([1.0, 1.0, 1.0]).

reset_xform_ops(prim:pxr.Usd.Prim)
Reset xform ops for a prim to isaac sim defaults,
Parameters:
prim (Usd.Prim) – Prim to reset xform ops on

### NumPy Utils

#### Rotations
deg2rad(degree_value:ndarray, device=None)→ndarray
_summary_
Parameters:

- degree_value (np.ndarray) – _description_

- device (_type_, optional) – _description_. Defaults to None.

Returns:
_description_

Return type:
np.ndarray

euler_angles_to_quats(
euler_angles:ndarray,
degrees:bool=False,
extrinsic:bool=True,
device=None,
)→ndarrayVectorized version of converting euler angles to quaternion (scalar first)
Parameters:

- np.ndarray (euler_angles) – euler angles with shape (N, 3) or (3,) representation XYZ in extrinsic coordinates

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

- degrees (bool, optional) – True if degrees, False if radians. Defaults to False.

Returns:
quaternions representation of the angles (N, 4) or (4,) - scalar first.

Return type:
np.ndarray

gf_quat_to_tensor(
orientation:pxr.Gf.Quatd|pxr.Gf.Quatf|pxr.Gf.Quaternion,
device=None,
)→ndarrayConverts a pxr Quaternion type to a numpy array following [w, x, y, z] convention.
Parameters:
orientation (Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]) – [description]

Returns:
[description]

Return type:
np.ndarray

quats_to_euler_angles(
quaternions:ndarray,
degrees:bool=False,
extrinsic:bool=True,
device=None,
)→ndarrayVectorized version of converting quaternions (scalar first) to euler angles
Parameters:

- quaternions (np.ndarray) – quaternions with shape (N, 4) or (4,) - scalar first

- degrees (bool, optional) – Return euler angles in degrees if True, radians if False. Defaults to False.

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
Euler angles in extrinsic or intrinsic coordinates XYZ order with shape (N, 3) or (3,) corresponding to the quaternion rotations

Return type:
np.ndarray

quats_to_rot_matrices(
quaternions:ndarray,
device=None,
)→ndarrayVectorized version of converting quaternions to rotation matrices
Parameters:
quaternions (np.ndarray) – quaternions with shape (N, 4) or (4,) and scalar first

Returns:
N Rotation matrices with shape (N, 3, 3) or (3, 3)

Return type:
np.ndarray

quats_to_rotvecs(
quaternions:ndarray,
device=None,
)→ndarrayVectorized version of converting quaternions to rotation vectors
Parameters:
quaternions (np.ndarray) – quaternions with shape (N, 4) or (4,) and scalar first

Returns:
N rotation vectors with shape (N,3) or (3,). The magnitude of the rotation vector describes the magnitude of the rotation.
The normalized rotation vector represents the axis of rotation.

Return type:
np.ndarray

rad2deg(radian_value:ndarray, device=None)→ndarray
_summary_
Parameters:

- radian_value (np.ndarray) – _description_

- device (_type_, optional) – _description_. Defaults to None.

Returns:
_description_

Return type:
np.ndarray

rot_matrices_to_quats(
rotation_matrices:ndarray,
device=None,
)→ndarrayVectorized version of converting rotation matrices to quaternions
Parameters:
rotation_matrices (np.ndarray) – N Rotation matrices with shape (N, 3, 3) or (3, 3)

Returns:
quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first

Return type:
np.ndarray

rotvecs_to_quats(
rotation_vectors:ndarray,
degrees:bool=False,
device=None,
)→ndarrayVectorized version of converting rotation vectors to quaternions
Parameters:

- rotation_vectors (np.ndarray) – N rotation vectors with shape (N, 3) or (3,). The magnitude of the rotation vector describes the magnitude of the rotation. The normalized rotation vector represents the axis of rotation.

- degrees (bool) – The magnitude of the rotation vector will be interpreted as degrees if True, and radians if False. Defaults to False.

Returns:
quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first

Return type:
np.ndarray

wxyz2xyzw(q, ret_torch=False)
xyzw2wxyz(q, ret_torch=False)

#### Maths
cos(data)
inverse(data)
matmul(matrix_a, matrix_b)
sin(data)
transpose_2d(data)

#### Tensor
as_type(data, dtype)
assign(src, dst, indices)
clone_tensor(data, device=None)
convert(data, device=None, dtype='float32', indexed=None)
create_tensor_from_list(data, dtype, device=None)
create_zeros_tensor(shape, dtype, device=None)
expand_dims(data, axis)
move_data(data, device=None)
pad(data, pad_width, mode='constant', value=None)
resolve_indices(indices, count, device=None)
tensor_cat(data, device=None, dim=-1)
tensor_stack(data, dim=0)
to_list(data)
to_numpy(data)

#### Transformations
assign_pose(
current_positions,
current_orientations,
positions,
orientations,
indices,
device=None,
pose=None,
)get_local_from_world(
parent_transforms,
positions,
orientations,
device=None,
)get_pose(positions, orientations, device=None)
get_world_from_local(
parent_transforms,
translations,
orientations,
device=None,
)tf_matrices_from_poses(
translations:ndarray,
orientations:ndarray,
device=None,
)→ndarray[summary]
Parameters:

- translations (Union[np.ndarray, torch.Tensor]) – translations with shape (N, 3).

- orientations (Union[np.ndarray, torch.Tensor]) – quaternion representation (scalar first) with shape (N, 4).

Returns:
transformation matrices with shape (N, 4, 4)

Return type:
Union[np.ndarray, torch.Tensor]

### Torch Utils

#### Rotations
deg2rad(degree_value:float, device=None)→Tensor
_summary_
Parameters:

- degree_value (torch.Tensor) – _description_

- device (_type_, optional) – _description_. Defaults to None.

Returns:
_description_

Return type:
torch.Tensor

euler_angles_to_quats(
euler_angles:Tensor,
degrees:bool=False,
extrinsic:bool=True,
device=None,
)→TensorVectorized version of converting euler angles to quaternion (scalar first)
Parameters:

- euler_angles (Union[np.ndarray, torch.Tensor]) – euler angles with shape (N, 3)

- degrees (bool, optional) – True if degrees, False if radians. Defaults to False.

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
quaternions representation of the angles (N, 4) - scalar first.

Return type:
Union[np.ndarray, torch.Tensor]

gf_quat_to_tensor(
orientation:pxr.Gf.Quatd|pxr.Gf.Quatf|pxr.Gf.Quaternion,
device=None,
)→TensorConverts a pxr Quaternion type to a torch array (scalar first).
Parameters:
orientation (Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]) – [description]

Returns:
[description]

Return type:
torch.Tensor

normalise_quat_in_pose(pose)
Takes a pose and normalises the quaternion portion of it.
Parameters:
pose – shape N, 7

Returns:
Pose with normalised quat. Shape N, 7

rad2deg(radian_value:Tensor, device=None)→Tensor
_summary_
Parameters:

- radian_value (torch.Tensor) – _description_

- device (_type_, optional) – _description_. Defaults to None.

Returns:
_description_

Return type:
torch.Tensor

rot_matrices_to_quats(
rotation_matrices:Tensor,
device=None,
)→TensorVectorized version of converting rotation matrices to quaternions
Parameters:
rotation_matrices (torch.Tensor) – N Rotation matrices with shape (N, 3, 3) or (3, 3)

Returns:
quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first

Return type:
torch.Tensor

wxyz2xyzw(q)
xyzw2wxyz(q)

#### Maths
cos(data)
inverse(data)
matmul(matrix_a, matrix_b)
set_seed(seed, torch_deterministic=False)
set seed across modules

sin(data)
transpose_2d(data)
unscale_np(x, lower, upper)

#### Tensor
as_type(data, dtype)
assign(src, dst, indices)
clone_tensor(data, device)
convert(data, device, dtype='float32', indexed=None)
create_tensor_from_list(data, dtype, device=None)
create_zeros_tensor(shape, dtype, device=None)
expand_dims(data, axis)
move_data(data, device)
pad(data, pad_width, mode='constant', value=None)
resolve_indices(indices, count, device)
tensor_cat(data, device=None, dim=-1)
tensor_stack(data, dim=0)
to_list(data)
to_numpy(data)

#### Transformations
assign_pose(
current_positions,
current_orientations,
positions,
orientations,
indices,
device,
pose=None,
)get_local_from_world(
parent_transforms,
positions,
orientations,
device,
)get_pose(positions, orientations, device)
get_world_from_local(
parent_transforms,
translations,
orientations,
device,
)normalise_quat_in_pose(pose)
Takes a pose and normalises the quaternion portion of it.
Parameters:
pose – shape N, 7

Returns:
Pose with normalised quat. Shape N, 7

tf_matrices_from_poses(
translations:Tensor,
orientations:Tensor,
device=None,
)→Tensor[summary]
Parameters:

- translations (Union[np.ndarray, torch.Tensor]) – translations with shape (N, 3).

- orientations (Union[np.ndarray, torch.Tensor]) – quaternion representation (scalar first) with shape (N, 4).

Returns:
transformation matrices with shape (N, 4, 4)

Return type:
Union[np.ndarray, torch.Tensor]

### Warp Utils

#### Rotations
deg2rad(degree_value:float, device=None)→Tensor
_summary_
Parameters:

- degree_value (torch.Tensor) – _description_

- device (_type_, optional) – _description_. Defaults to None.

Returns:
_description_

Return type:
torch.Tensor

euler_angles_to_quats(
euler_angles:Tensor,
degrees:bool=False,
extrinsic:bool=True,
device=None,
)→TensorVectorized version of converting euler angles to quaternion (scalar first)
Parameters:

- euler_angles (Union[np.ndarray, torch.Tensor]) – euler angles with shape (N, 3)

- degrees (bool, optional) – True if degrees, False if radians. Defaults to False.

- extrinsic (bool, optional) – True if the euler angles follows the extrinsic angles convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows the intrinsic angles conventions (equivalent to XYZ ordering). Defaults to True.

Returns:
quaternions representation of the angles (N, 4) - scalar first.

Return type:
Union[np.ndarray, torch.Tensor]

gf_quat_to_tensor(
orientation:pxr.Gf.Quatd|pxr.Gf.Quatf|pxr.Gf.Quaternion,
device=None,
)→TensorConverts a pxr Quaternion type to a torch array (scalar first).
Parameters:
orientation (Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]) – [description]

Returns:
[description]

Return type:
torch.Tensor

normalise_quat_in_pose(pose)
Takes a pose and normalises the quaternion portion of it.
Parameters:
pose – shape N, 7

Returns:
Pose with normalised quat. Shape N, 7

rad2deg(radian_value:Tensor, device=None)→Tensor
_summary_
Parameters:

- radian_value (torch.Tensor) – _description_

- device (_type_, optional) – _description_. Defaults to None.

Returns:
_description_

Return type:
torch.Tensor

rot_matrices_to_quats(
rotation_matrices:Tensor,
device=None,
)→TensorVectorized version of converting rotation matrices to quaternions
Parameters:
rotation_matrices (torch.Tensor) – N Rotation matrices with shape (N, 3, 3) or (3, 3)

Returns:
quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first

Return type:
torch.Tensor

wxyz2xyzw(q)
xyzw2wxyz(q)

#### Tensor
as_type(data, dtype)
assign(src, dst, indices)
clone_tensor(data, device)
convert(data, device, dtype='float32', indexed=None)
create_tensor_from_list(data, dtype, device=None)
create_zeros_tensor(shape, dtype, device=None)
expand_dims(data, axis)
move_data(data, device)
pad(data, pad_width, mode='constant', value=None)
resolve_indices(indices, count, device)
tensor_cat(data, device=None, dim=-1)
tensor_stack(data, dim=0)
to_list(data)
to_numpy(data)

#### Transformations
assign_pose(
current_positions,
current_orientations,
positions,
orientations,
indices,
device,
pose=None,
)get_local_from_world(
parent_transforms,
positions,
orientations,
device,
)get_pose(positions, orientations, device)
get_world_from_local(
parent_transforms,
translations,
orientations,
device,
)normalise_quat_in_pose(pose)
Takes a pose and normalises the quaternion portion of it.
Parameters:
pose – shape N, 7

Returns:
Pose with normalised quat. Shape N, 7

tf_matrices_from_poses(
translations:Tensor,
orientations:Tensor,
device=None,
)→Tensor[summary]
Parameters:

- translations (Union[np.ndarray, torch.Tensor]) – translations with shape (N, 3).

- orientations (Union[np.ndarray, torch.Tensor]) – quaternion representation (scalar first) with shape (N, 4).

Returns:
transformation matrices with shape (N, 4, 4)

Return type:
Union[np.ndarray, torch.Tensor]
