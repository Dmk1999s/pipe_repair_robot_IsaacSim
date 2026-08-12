<!-- source: py/source/extensions/isaacsim.asset.importer.urdf/docs/api.html | title: URDF Import Extension [isaacsim.asset.importer.urdf] — Isaac Sim -->

# URDF Import Extension [isaacsim.asset.importer.urdf]

## URDF Import Commands
The following commands can be used to simplify the import process. Below is a sample demonstrating how to import the Carter URDF included with this extension

```
1import omni.kit.commands
2from pxr import UsdLux, Sdf, Gf, UsdPhysics, PhysicsSchemaTools
3
4# setting up import configuration:
5status, import_config = omni.kit.commands.execute("URDFCreateImportConfig")
6import_config.merge_fixed_joints = False
7import_config.convex_decomp = False
8import_config.import_inertia_tensor = True
9import_config.fix_base = False
10import_config.collision_from_visuals = False
11
12# Get path to extension data:
13ext_manager = omni.kit.app.get_app().get_extension_manager()
14ext_id = ext_manager.get_enabled_extension_id("isaacsim.asset.importer.urdf")
15extension_path = ext_manager.get_extension_path(ext_id)
16# import URDF
17omni.kit.commands.execute(
18 "URDFParseAndImportFile",
19 urdf_path=extension_path + "/data/urdf/robots/carter/urdf/carter.urdf",
20 import_config=import_config,
21)
22# get stage handle
23stage = omni.usd.get_context().get_stage()
24
25# enable physics
26scene = UsdPhysics.Scene.Define(stage, Sdf.Path("/physicsScene"))
27# set gravity
28scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0))
29scene.CreateGravityMagnitudeAttr().Set(9.81)
30
31# add ground plane
32PhysicsSchemaTools.addGroundPlane(stage, "/World/groundPlane", "Z", 1500, Gf.Vec3f(0, 0, -50), Gf.Vec3f(0.5))
33
34# add lighting
35distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
36distantLight.CreateIntensityAttr(500)
```
classURDFCreateImportConfig(*args:Any, **kwargs:Any)
Returns an ImportConfig object that can be used while parsing and importing. Should be used with URDFParseFile and URDFParseAndImportFile commands
Returns:
Parsed URDF stored in an internal structure.

Return type:
isaacsim.asset.importer.urdf._urdf.ImportConfig

classURDFImportRobot(*args:Any, **kwargs:Any)
This command parses and imports a given urdf and returns a UrdfRobot object
Parameters:

- arg0 (`str`) – The absolute path to where the urdf file is

- arg1 (`UrdfRobot`) – The parsed URDF Robot

- arg2 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import Configuration

- arg3 (`str`) – destination path for robot usd. Default is “” which will load the robot in-memory on the open stage.

- arg4 (`bool`) – if True, return the articulation Root prim path instead of the object’s base path.

Returns:
Path to the robot on the USD stage.

Return type:
`str`

classURDFParseAndImportFile(*args:Any, **kwargs:Any)
This command parses and imports a given urdf and returns a UrdfRobot object
Parameters:

- arg0 (`str`) – The absolute path to where the urdf file is

- arg1 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import Configuration

- arg2 (`str`) – destination path for robot usd. Default is “” which will load the robot in-memory on the open stage.

- arg3 (`bool`) – if True, return the articulation Root prim path instead of the object’s base path.

Returns:
Path to the robot on the USD stage.

Return type:
`str`

classURDFParseFile(*args:Any, **kwargs:Any)
This command parses a given urdf and returns a UrdfRobot object
Parameters:

- arg0 (`str`) – The absolute path to where the urdf file is

- arg1 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import Configuration

Returns:
Parsed URDF stored in an internal structure.

Return type:
`isaacsim.asset.importer.urdf._urdf.UrdfRobot`

classURDFParseText(*args:Any, **kwargs:Any)
This command parses a given urdf and returns a UrdfRobot object
Parameters:

- arg0 (`str`) – The absolute path to where the urdf file is

- arg1 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import Configuration

Returns:
Parsed URDF stored in an internal structure.

Return type:
`isaacsim.asset.importer.urdf._urdf.UrdfRobot`

This extension provides an interface to the URDF importer.
Example
Setup the configuration parameters before importing. Files must be parsed before imported.

```
>>> import omni
>>> import os
>>> from isaacsim.asset.importer.urdf import _urdf
>>> urdf_interface = _urdf.acquire_urdf_interface()
>>>
>>> # setup config params
>>> import_config = _urdf.ImportConfig()
>>> import_config.set_merge_fixed_joints(False)
>>> import_config.set_fix_base(True)
>>>
>>> # parse and import file
>>> ext_manager = omni.kit.app.get_app().get_extension_manager()
>>> ext_id = ext_manager.get_enabled_extension_id("isaacsim.asset.importer.urdf")
>>> extension_path = ext_manager.get_extension_path(ext_id)
>>> urdf_path = os.path.abspath(
... extension_path + "/data/urdf/robots/franka_description/robots/"
... )
>>> filename = "panda_arm_hand.urdf"
>>> imported_robot = urdf_interface.parse_urdf(urdf_path, filename, import_config)
>>> urdf_interface.import_robot(urdf_path, filename, imported_robot, import_config, "")
'/panda'
```
Refer to the sample documentation for more examples and usage
classUrdf
compute_natural_stiffness(
self:isaacsim.asset.importer.urdf._urdf.Urdf ,
arg0:isaacsim.asset.importer.urdf._urdf.UrdfRobot,
arg1:str,
arg2:float,
)→floatCompute the natural stiffness of a joint.
Parameters:

- arg0 (`isaacsim.asset.importer.urdf._urdf.UrdfRobot`) – The parsed URDF, the output from parse_urdf

- arg1 (`str`) – The name of the joint

- arg2 (`float`) – The natural frequency of the joint

Returns:
The natural stiffness of the joint

Return type:
`float`

get_kinematic_chain(
self:isaacsim.asset.importer.urdf._urdf.Urdf ,
arg0:isaacsim.asset.importer.urdf._urdf.UrdfRobot,
)→dictGet the kinematic chain of the robot. Mostly used for graphic display of the kinematic tree.
Parameters:
arg0 (`isaacsim.asset.importer.urdf._urdf.UrdfRobot`) – The parsed URDF, the output from parse_urdf

Returns:
A dictionary with information regarding the parent-child relationship between all the links and joints

Return type:
`dict`

import_robot(
self:isaacsim.asset.importer.urdf._urdf.Urdf ,
assetRoot:str,
assetName:str,
robot:isaacsim.asset.importer.urdf._urdf.UrdfRobot,
importConfig:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
stage:str='',
getArticulationRoot:bool=False,
)→strImporting the robot, from the already parsed URDF file.
Parameters:

- arg0 (`str`) – The absolute path to where the urdf file is

- arg1 (`str`) – The name of the urdf file

- arg2 (`isaacsim.asset.importer.urdf._urdf.UrdfRobot`) – The parsed URDF file, the output from parse_urdf

- arg3 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import configuration parameters

- arg4 (`str`) – optional: path to stage to use for importing. leaving it empty will import on open stage. If the open stage is a new stage, textures will not load.

Returns:
Path to the robot on the USD stage.

Return type:
`str`

parse_string_urdf(
self:isaacsim.asset.importer.urdf._urdf.Urdf ,
arg0:str,
arg1:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
)→isaacsim.asset.importer.urdf._urdf.UrdfRobotParse URDF file into the internal data structure, which is displayed in the importer window for inspection.
Parameters:

- arg0 (`str`) – The urdf in text format

- arg2 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import configuration parameters

Returns:
Parsed URDF stored in an internal structure.

Return type:
`isaacsim.asset.importer.urdf._urdf.UrdfRobot`

parse_urdf(
self:isaacsim.asset.importer.urdf._urdf.Urdf ,
arg0:str,
arg1:str,
arg2:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
)→isaacsim.asset.importer.urdf._urdf.UrdfRobotParse URDF file into the internal data structure, which is displayed in the importer window for inspection.
Parameters:

- arg0 (`str`) – The absolute path to where the urdf file is

- arg1 (`str`) – The name of the urdf file

- arg2 (isaacsim.asset.importer.urdf._urdf.ImportConfig ) – Import configuration parameters

Returns:
Parsed URDF stored in an internal structure.

Return type:
`isaacsim.asset.importer.urdf._urdf.UrdfRobot`

classImportConfig
set_collision_from_visuals(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_convex_decomp(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_create_physics_scene(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_default_drive_strength(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:float,
)→None set_default_drive_type(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:int,
)→None set_default_position_drive_damping(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:float,
)→None set_density(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:float,
)→None set_distance_scale(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:float,
)→None set_fix_base(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_import_inertia_tensor(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_make_default_prim(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_merge_fixed_joints(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_override_joint_dynamics(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_parse_mimic(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_replace_cylinders_with_capsules(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_self_collision(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:bool,
)→None set_subdivision_scheme(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:int,
)→None set_up_vector(
self:isaacsim.asset.importer.urdf._urdf.ImportConfig ,
arg0:float,
arg1:float,
arg2:float,
)→None propertycollision_from_visuals
Generate convex collision from the visual meshes.

propertyconvex_decomp
Decompose a convex mesh into smaller pieces for a closer fit

propertycreate_physics_scene
add a physics scene to the stage on import if none exists

propertydefault_drive_strength
default drive stiffness used for joints if drive type is position or velocity and none is authored

propertydefault_drive_type
default drive type used for joints

propertydefault_position_drive_damping
default drive damping used if drive type is set to position and no damping is authored

propertydensity
default density used for links, use 0 to autocompute

propertydistance_scale
Set the unit scaling factor, 1.0 means meters, 100.0 means cm

propertyfix_base
Create fix joint for base link

propertyimport_inertia_tensor
Import inertia tensor from urdf, if not specified in urdf it will import as identity

propertymake_default_prim
set imported robot as default prim

propertymerge_fixed_joints
Consolidating links that are connected by fixed joints

propertyoverride_joint_dynamics
Use default values for all joints

propertyparse_mimic
Parse Mimic Joint flag using PhysX Tendons

propertyreplace_cylinders_with_capsules
Replace all cylinder bodies in the URDF with capsules.

propertyself_collision
Self collisions between links in the articulation

propertysubdivision_scheme
Subdivision scheme to be used for mesh normals

propertyup_vector
Up vector used for import
