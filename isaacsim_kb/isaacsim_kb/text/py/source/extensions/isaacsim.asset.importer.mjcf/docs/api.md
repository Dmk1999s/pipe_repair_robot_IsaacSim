<!-- source: py/source/extensions/isaacsim.asset.importer.mjcf/docs/api.html | title: MJCF Importer Extension [isaacsim.asset.importer.mjcf] — Isaac Sim -->

# MJCF Importer Extension [isaacsim.asset.importer.mjcf]

## MJCF Import Commands
The following commands can be used to simplify the import process. Below is a sample demonstrating how to import the Ant MJCF included with this extension

```
1import omni.kit.commands
2from pxr import UsdLux, Sdf, Gf, UsdPhysics, PhysicsSchemaTools
3
4# setting up import configuration:
5status, import_config = omni.kit.commands.execute("MJCFCreateImportConfig")
6import_config.set_fix_base(True)
7import_config.set_import_inertia_tensor(True)
8
9# Get path to extension data:
10ext_manager = omni.kit.app.get_app().get_extension_manager()
11ext_id = ext_manager.get_enabled_extension_id("isaacsim.asset.importer.mjcf")
12extension_path = ext_manager.get_extension_path(ext_id)
13
14# import MJCF
15omni.kit.commands.execute(
16 "MJCFCreateAsset",
17 mjcf_path=extension_path + "/data/mjcf/nv_ant.xml",
18 import_config=import_config,
19 prim_path="/ant"
20)
21
22# get stage handle
23stage = omni.usd.get_context().get_stage()
24
25# enable physics
26scene = UsdPhysics.Scene.Define(stage, Sdf.Path("/physicsScene"))
27# set gravity
28scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0))
29scene.CreateGravityMagnitudeAttr().Set(9.81)
30
31# add lighting
32distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
33distantLight.CreateIntensityAttr(500)
```
classMJCFCreateAsset(*args:Any, **kwargs:Any)
This command parses and imports a given mjcf file.
Parameters:

- arg0 (`str`) – The absolute path the mjcf file

- arg1 (isaacsim.asset.importer.mjcf._mjcf.ImportConfig ) – Import configuration

- arg2 (`str`) – Path to the robot on the USD stage

- arg3 (`str`) – destination path for robot usd. Default is “” which will load the robot in-memory on the open stage.

classMJCFCreateImportConfig(*args:Any, **kwargs:Any)
Returns an ImportConfig object that can be used while parsing and importing. Should be used with the MJCFCreateAsset command
Returns:
Parsed MJCF stored in an internal structure.

Return type:
isaacsim.asset.importer.mjcf._mjcf.ImportConfig

This extension provides an interface to the MJCF importer.
Example
Setup the configuration parameters before importing. Files must be parsed before imported.

```
>>> import omni
>>> import os
>>> from isaacsim.asset.importer.mjcf import _mjcf
>>> mjcf_interface = _mjcf.acquire_mjcf_interface()
>>>
>>> # setup config params
>>> import_config = _mjcf.ImportConfig()
>>> import_config.fix_base = True
>>>
>>> # parse and import file

>>> ext_manager = omni.kit.app.get_app().get_extension_manager()
>>> ext_id = ext_manager.get_enabled_extension_id("isaacsim.asset.importer.mjcf")
>>> extension_path = ext_manager.get_extension_path(ext_id)
>>> mjcf_path = os.path.abspath(extension_path + "/data/mjcf/nv_ant.xml")
>>> mjcf_interface.create_asset_mjcf(mjcf_path, "", import_config)
```
Refer to the sample documentation for more examples and usage
classMjcf
create_asset_mjcf(
self:isaacsim.asset.importer.mjcf._mjcf.Mjcf ,
fileName:str,
primName:str,
config:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
stage_identifier:str='',
)→None Parse and import MJCF file.
Parameters:

- arg0 (`str`) – The absolute path to the mjcf

- arg1 (`str`) – Path to the robot on the USD stage

- arg2 (isaacsim.asset.importer.mjcf._mjcf.ImportConfig ) – Import configuration

- arg3 (`str`) – optional: path to stage to use for importing. leaving it empty will import on open stage. If the open stage is a new stage, textures will not load.

classImportConfig
set_convex_decomp(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_create_body_for_fixed_joint(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_create_physics_scene(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_default_drive_strength(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:float,
)→None set_density(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:float,
)→None set_distance_scale(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:float,
)→None set_fix_base(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_import_inertia_tensor(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_import_sites(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_instanceable_usd_path(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:str,
)→None set_make_default_prim(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_make_instanceable(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_merge_fixed_joints(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_override_com(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_override_inertia(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_self_collision(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None set_visualize_collision_geoms(
self:isaacsim.asset.importer.mjcf._mjcf.ImportConfig ,
arg0:bool,
)→None propertyconvex_decomp
Decompose a convex mesh into smaller pieces for a closer fit

propertycreate_body_for_fixed_joint
creates body for fixed joint

propertycreate_physics_scene
add a physics scene to the stage on import

propertydefault_drive_strength
default drive stiffness used for joints

propertydensity
default density used for links

propertydistance_scale
Set the unit scaling factor, 1.0 means meters, 100.0 means cm

propertyfix_base
Create fix joint for base link

propertyimport_inertia_tensor
Import inertia tensor from mjcf, if not specified in mjcf it will import as identity

propertyinstanceable_usd_path
USD file to store instanceable mehses in

propertymake_default_prim
set imported robot as default prim

propertymake_instanceable
Creates an instanceable version of the asset. All meshes will be placed in a separate USD file

propertymerge_fixed_joints
Consolidating links that are connected by fixed joints

propertyoverride_com
whether to compute the center of mass from geometry and override values given in the original asset

propertyoverride_inertia_tensor
Whether to compute the inertia tensor from geometry and override values given in the original asset

propertyself_collision
Self collisions between links in the articulation
