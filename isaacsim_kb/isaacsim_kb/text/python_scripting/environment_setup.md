<!-- source: python_scripting/environment_setup.html | title: Scene Setup Snippets — Isaac Sim Documentation -->

# Scene Setup Snippets

## Objects Creation and Manipulation
Note
The following scripts should only be run on the default new stage and only once. You can try these by creating a new stage via File > New and running from Window > Script Editor

### Rigid Object Creation
The following snippet adds a dynamic cube with given properties and a ground plane to the scene.

```
1import numpy as np
2from isaacsim.core.api.objects import DynamicCuboid
3from isaacsim.core.api.objects.ground_plane import GroundPlane
4from isaacsim.core.api.physics_context import PhysicsContext
5
6PhysicsContext()
7GroundPlane(prim_path="/World/groundPlane", size=10, color=np.array([0.5, 0.5, 0.5]))
8DynamicCuboid(prim_path="/World/cube",
9 position=np.array([-.5, -.2, 1.0]),
10 scale=np.array([.5, .5, .5]),
11 color=np.array([.2,.3,0.]))
```

### View Objects
View classes in this extension are collections of similar prims. View classes manipulate the underlying objects in a vectorized way. Most View APIs require the world and the physics simulation to be initialized before they can be used. This can be achieved by adding the view class to the World’s scene and resetting the world as follows

```
1from isaacsim.core.api.world import World
2from isaacsim.core.prims import RigidPrim
3from isaacsim.core.api.objects import DynamicCuboid
4
5# View classes are initialized when they are added to the scene and the world is reset
6world = World()
7cube = DynamicCuboid(prim_path="/World/cube_0")
8rigid_prim = RigidPrim(prim_paths_expr="/World/cube_[0-100]")
9world.scene.add(rigid_prim)
10world.reset()
11# rigid_prim is now initialized and can be used
```
which works when running the script via the Isaac Sim Python script. When using Window > Script Editor, to run the snippets you need to use the asynchronous version of `reset` as follows

```
1import asyncio
2from isaacsim.core.api.world import World
3from isaacsim.core.prims import RigidPrim
4from isaacsim.core.api.objects import DynamicCuboid
5
6async def init():
7 if World.instance():
8 World.instance().clear_instance()
9 world=World()
10 await world.initialize_simulation_context_async()
11 world.scene.add_default_ground_plane(z_position=-1.0)
12 cube = DynamicCuboid(prim_path="/World/cube_0")
13 rigid_prim = RigidPrim(prim_paths_expr="/World/cube_[0-100]")
14 # View classes are internally initialized when they are added to the scene and the world is reset
15 world.scene.add(rigid_prim)
16 await world.reset_async()
17 # rigid_prim is now initialized and can be used
18
19asyncio.ensure_future(init())
```
See Workflows tutorial for more details about various workflows for developing in Isaac Sim.

### Create RigidPrim
The following snippet adds three cubes to the scene and creates a RigidPrim (formerly RigidPrimView) to manipulate the batch.

```
1import asyncio
2import numpy as np
3from isaacsim.core.api.world import World
4from isaacsim.core.prims import RigidPrim
5from isaacsim.core.api.objects import DynamicCuboid
6
7async def example():
8 if World.instance():
9 World.instance().clear_instance()
10 world=World()
11 await world.initialize_simulation_context_async()
12 world.scene.add_default_ground_plane(z_position=-1.0)
13
14 # create rigid cubes
15 for i in range(3):
16 DynamicCuboid(prim_path=f"/World/cube_{i}")
17
18 # create the view object to batch manipulate the cubes
19 rigid_prim = RigidPrim(prim_paths_expr="/World/cube_[0-2]")
20 world.scene.add(rigid_prim)
21 await world.reset_async()
22 # set world poses
23 rigid_prim.set_world_poses(positions=np.array([[0, 0, 2], [0, -2, 2], [0, 2, 2]]))
24
25asyncio.ensure_future(example())
```
See the API Documentation for all the possible operations supported by `RigidPrim`.

### Create RigidContactView
There are scenarios where you are interested in net contact forces on each body and contact forces between specific bodies. This can be achieved via the RigidContactView object managed by the RigidPrim

```
1import asyncio
2import numpy as np
3from isaacsim.core.api.world import World
4from isaacsim.core.prims import RigidPrim
5from isaacsim.core.api.objects import DynamicCuboid
6
7async def example():
8 if World.instance():
9 World.instance().clear_instance()
10 world = World()
11 await world.initialize_simulation_context_async()
12 world.scene.add_default_ground_plane()
13
14 # create three rigid cubes sitting on top of three others
15 for i in range(3):
16 DynamicCuboid(prim_path=f"/World/bottom_box_{i+1}", size=2, color=np.array([0.5, 0, 0]), mass=1.0)
17 DynamicCuboid(prim_path=f"/World/top_box_{i+1}", size=2, color=np.array([0, 0, 0.5]), mass=1.0)
18
19 # as before, create RigidContactView to manipulate bottom boxes but this time specify top boxes as filters to the view object
20 # this allows receiving contact forces between the bottom boxes and top boxes
21 bottom_box = RigidPrim(
22 prim_paths_expr="/World/bottom_box_*",
23 name="bottom_box",
24 positions=np.array([[0, 0, 1.0], [-5.0, 0, 1.0], [5.0, 0, 1.0]]),
25 contact_filter_prim_paths_expr=["/World/top_box_*"],
26 )
27 # create a RigidContactView to manipulate top boxes
28 top_box = RigidPrim(
29 prim_paths_expr="/World/top_box_*",
30 name="top_box",
31 positions=np.array([[0.0, 0, 3.0], [-5.0, 0, 3.0], [5.0, 0, 3.0]]),
32 track_contact_forces=True,
33 )
34
35 world.scene.add(top_box)
36 world.scene.add(bottom_box)
37 await world.reset_async()
38
39 # net contact forces acting on the bottom boxes
40 print(bottom_box.get_net_contact_forces())
41 # contact forces between the top and the bottom boxes
42 print(bottom_box.get_contact_force_matrix())
43
44asyncio.ensure_future(example())
```
More detailed information about the friction and contact forces can be obtained from the `get_friction_data` and `get_contact_force_data` respectively. These APIs provide all the contact forces and contact points between pairs of the sensor prims and filter prims. `get_contact_force_data` API provides the contact distances and contact normal vectors as well.
In the example below, we add three boxes to the scene and apply a tangential force of magnitude 10 to each. Then we use the aforementioned APIs to receive all the contact information and sum across all the contact points to find the friction/normal forces between the boxes and the ground plane.

```
1import asyncio
2import numpy as np
3from isaacsim.core.api.world import World
4from isaacsim.core.prims import RigidPrim
5from isaacsim.core.api.objects import DynamicCuboid
6from isaacsim.core.api.materials.physics_material import PhysicsMaterial
7from isaacsim.core.utils.stage import create_new_stage_async, update_stage_async
8
9async def contact_force_example():
10 g = 10
11 await create_new_stage_async()
12 if World.instance():
13 World.instance().clear_instance()
14 world = World()
15 world.scene.add_default_ground_plane()
16 await world.initialize_simulation_context_async()
17 material = PhysicsMaterial(
18 prim_path="/World/PhysicsMaterials",
19 static_friction=0.5,
20 dynamic_friction=0.5,
21 )
22 # create three rigid cubes sitting on top of three others
23 for i in range(3):
24 DynamicCuboid(
25 prim_path=f"/World/Box_{i+1}", size=2, color=np.array([0, 0, 0.5]), mass=1.0
26 ).apply_physics_material(material)
27
28 # Creating RigidPrim with contact relevant keywords allows receiving contact information
29 # In the following we indicate that we are interested in receiving up to 30 contact points data between the boxes and the ground plane
30 box_view = RigidPrim(
31 prim_paths_expr="/World/Box_*",
32 positions=np.array([[0, 0, 1.0], [-5.0, 0, 1.0], [5.0, 0, 1.0]]),
33 contact_filter_prim_paths_expr=["/World/defaultGroundPlane/GroundPlane/CollisionPlane"],
34 max_contact_count=3 * 10, # we don't expect more than 10 contact points for each box
35 )
36
37 world.scene.add(box_view)
38 await world.reset_async()
39
40 forces = np.array([[g, 0, 0], [g, 0, 0], [g, 0, 0]])
41 box_view.apply_forces(forces)
42 await update_stage_async()
43
44 # tangential forces
45 friction_forces, friction_points, friction_pair_contacts_count, friction_pair_contacts_start_indices = box_view.get_friction_data(dt=1 / 60)
46 # normal forces
47 forces, points, normals, distances, pair_contacts_count, pair_contacts_start_indices = box_view.get_contact_force_data(dt=1 / 60)
48 # pair_contacts_count, pair_contacts_start_indices are tensors of size num_sensors x num_filters
49 # friction_pair_contacts_count, friction_pair_contacts_start_indices are tensors of size num_sensors x num_filters
50 # use the following tensors to sum across all the contact points
51 force_aggregate = np.zeros((box_view._contact_view.num_shapes, box_view._contact_view.num_filters, 3))
52 friction_force_aggregate = np.zeros((box_view._contact_view.num_shapes, box_view._contact_view.num_filters, 3))
53
54 # process contacts for each pair i, j
55 for i in range(pair_contacts_count.shape[0]):
56 for j in range(pair_contacts_count.shape[1]):
57 start_idx = pair_contacts_start_indices[i, j]
58 friction_start_idx = friction_pair_contacts_start_indices[i, j]
59 count = pair_contacts_count[i, j]
60 friction_count = friction_pair_contacts_count[i, j]
61 # sum/average across all the contact points for each pair
62 pair_forces = forces[start_idx : start_idx + count]
63 pair_normals = normals[start_idx : start_idx + count]
64 force_aggregate[i, j] = np.sum(pair_forces * pair_normals, axis=0)
65
66 # sum/average across all the friction pairs
67 pair_forces = friction_forces[friction_start_idx : friction_start_idx + friction_count]
68 friction_force_aggregate[i, j] = np.sum(pair_forces, axis=0)
69
70 print("friction forces: \n", friction_force_aggregate)
71 print("contact forces: \n", force_aggregate)
72 # get_contact_force_matrix API is equivalent to the summation of the individual contact forces computed above
73 print("contact force matrix: \n", box_view.get_contact_force_matrix(dt=1 / 60))
74 # get_net_contact_forces API is the summation of the all forces
75 # in the current example because all the potential contacts are captured by the choice of our filter prims (/World/defaultGroundPlane/GroundPlane/CollisionPlane)
76 # the following is similar to the reduction of the contact force matrix above across the filters
77 print("net contact force: \n", box_view.get_net_contact_forces(dt=1 / 60))
78
79
80asyncio.ensure_future(contact_force_example())
```
See the API Documentation for more information about `RigidContactView`.

### Set Mass Properties for a Mesh
The snippet below shows how to set the mass of a physics object. Density can also be specified as an alternative

```
1import omni
2from pxr import UsdPhysics
3from omni.physx.scripts import utils
4
5stage = omni.usd.get_context().get_stage()
6result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
7# Get the prim
8cube_prim = stage.GetPrimAtPath(path)
9# Make it a rigid body
10utils.setRigidBody(cube_prim, "convexHull", False)
11
12mass_api = UsdPhysics.MassAPI.Apply(cube_prim)
13mass_api.CreateMassAttr(10)
14### Alternatively set the density
15mass_api.CreateDensityAttr(1000)
```

### Get Size of a Mesh
The snippet below shows how to get the size of a mesh.

```
1import omni
2from pxr import Usd, UsdGeom, Gf
3
4stage = omni.usd.get_context().get_stage()
5result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cone")
6# Get the prim
7prim = stage.GetPrimAtPath(path)
8# Get the size
9bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
10bbox_cache.Clear()
11prim_bbox = bbox_cache.ComputeWorldBound(prim)
12prim_range = prim_bbox.ComputeAlignedRange()
13prim_size = prim_range.GetSize()
14print(prim_size)
```

### Apply Semantic Data on Entire Stage
The snippet below shows how to programmatically apply semantic data on objects by iterating the entire stage.

```
1import omni.usd
2from isaacsim.core.utils.semantics import add_labels
3
4def remove_prefix(name, prefix):
5 if name.startswith(prefix):
6 return name[len(prefix) :]
7 return name
8
9def remove_numerical_suffix(name):
10 suffix = name.split("_")[-1]
11 if suffix.isnumeric():
12 return name[: -len(suffix) - 1]
13 return name
14
15def remove_underscores(name):
16 return name.replace("_", "")
17
18stage = omni.usd.get_context().get_stage()
19for prim in stage.Traverse():
20 if prim.GetTypeName() == "Mesh":
21 label = str(prim.GetPrimPath()).split("/")[-1]
22 label = remove_prefix(label, "SM_")
23 label = remove_numerical_suffix(label)
24 label = remove_underscores(label)
25 add_labels(prim, labels=[label], instance_name="class")
```

### Convert Asset to USD
The below script will convert a non-USD asset like OBJ/STL/FBX to USD. This is meant to be used inside the Script Editor . For running it as a Standalone Application , Check Python Environment .

```
1import carb
2import omni
3import asyncio
4
5
6async def convert_asset_to_usd(input_obj: str, output_usd: str):
7 import omni.kit.asset_converter
8
9 def progress_callback(progress, total_steps):
10 pass
11
12 converter_context = omni.kit.asset_converter.AssetConverterContext()
13 # setup converter and flags
14 # converter_context.ignore_material = False
15 # converter_context.ignore_animation = False
16 # converter_context.ignore_cameras = True
17 # converter_context.single_mesh = True
18 # converter_context.smooth_normals = True
19 # converter_context.preview_surface = False
20 # converter_context.support_point_instancer = False
21 # converter_context.embed_mdl_in_usd = False
22 # converter_context.use_meter_as_world_unit = True
23 # converter_context.create_world_as_default_root_prim = False
24 instance = omni.kit.asset_converter.get_instance()
25 task = instance.create_converter_task(input_obj, output_usd, progress_callback, converter_context)
26 success = await task.wait_until_finished()
27 if not success:
28 carb.log_error(task.get_status(), task.get_detailed_error())
29 print("converting done")
30
31
32asyncio.ensure_future(
33 convert_asset_to_usd(
34 "</path/to/mesh.obj>",
35 "</path/to/mesh.usd>",
36 )
37)
```
The details about the optional import options in lines 13-23 can be found here .

## Physics How-Tos

### Create A Physics Scene

```
1import omni
2from pxr import Gf, Sdf, UsdPhysics
3
4stage = omni.usd.get_context().get_stage()
5# Add a physics scene prim to stage
6scene = UsdPhysics.Scene.Define(stage, Sdf.Path("/World/physicsScene"))
7# Set gravity vector
8scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0))
9scene.CreateGravityMagnitudeAttr().Set(981.0)
```
The following can be added to set specific settings, in this case use CPU physics and the TGS solver

```
1from pxr import PhysxSchema
2
3PhysxSchema.PhysxSceneAPI.Apply(stage.GetPrimAtPath("/World/physicsScene"))
4physxSceneAPI = PhysxSchema.PhysxSceneAPI.Get(stage, "/World/physicsScene")
5physxSceneAPI.CreateEnableCCDAttr(True)
6physxSceneAPI.CreateEnableStabilizationAttr(True)
7physxSceneAPI.CreateEnableGPUDynamicsAttr(False)
8physxSceneAPI.CreateBroadphaseTypeAttr("MBP")
9physxSceneAPI.CreateSolverTypeAttr("TGS")
```
Adding a ground plane to a stage can be done via the following code: It creates a Z up plane with a size of 100 cm at a Z coordinate of -100

```
1import omni
2from pxr import PhysicsSchemaTools
3stage = omni.usd.get_context().get_stage()
4PhysicsSchemaTools.addGroundPlane(stage, "/World/groundPlane", "Z", 100, Gf.Vec3f(0, 0, -100), Gf.Vec3f(1.0))
```

### Enable Physics And Collision For a Mesh
The script below assumes there is a physics scene in the stage.

```
1import omni
2from omni.physx.scripts import utils
3
4# Create a cube mesh in the stage
5stage = omni.usd.get_context().get_stage()
6result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
7# Get the prim
8cube_prim = stage.GetPrimAtPath(path)
9# Enable physics on prim
10# If a tighter collision approximation is desired use convexDecomposition instead of convexHull
11utils.setRigidBody(cube_prim, "convexHull", False)
```
If a tighter collision approximation is desired use convexDecomposition

```
1import omni
2from omni.physx.scripts import utils
3
4# Create a cube mesh in the stage
5stage = omni.usd.get_context().get_stage()
6result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
7# Get the prim
8cube_prim = stage.GetPrimAtPath(path)
9# Enable physics on prim
10# If a tighter collision approximation is desired use convexDecomposition instead of convexHull
11utils.setRigidBody(cube_prim, "convexDecomposition", False)
```
To verify that collision meshes have been successfully enabled, click the “eye” icon > “Show By Type” > “Physics Mesh” > “All”. This will show the collision meshes as pink outlines on the objects.

### Traverse a stage and assign collision meshes to children

```
1import omni
2from pxr import Usd, UsdGeom, Gf
3from omni.physx.scripts import utils
4
5stage = omni.usd.get_context().get_stage()
6
7def add_cube(stage, path, size: float = 10, offset: Gf.Vec3d = Gf.Vec3d(0, 0, 0)):
8 cubeGeom = UsdGeom.Cube.Define(stage, path)
9 cubeGeom.CreateSizeAttr(size)
10 cubeGeom.AddTranslateOp().Set(offset)
11
12### The following prims are added for illustrative purposes
13result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Torus")
14# all prims under AddCollision will get collisions assigned
15add_cube(stage, "/World/Cube_0", offset=Gf.Vec3d(100, 100, 0))
16# create a prim nested under without a parent
17add_cube(stage, "/World/Nested/Cube", offset=Gf.Vec3d(100, 0, 100))
18###
19
20# Traverse all prims in the stage starting at this path
21curr_prim = stage.GetPrimAtPath("/")
22
23for prim in Usd.PrimRange(curr_prim):
24 # only process shapes and meshes
25 if (
26 prim.IsA(UsdGeom.Cylinder)
27 or prim.IsA(UsdGeom.Capsule)
28 or prim.IsA(UsdGeom.Cone)
29 or prim.IsA(UsdGeom.Sphere)
30 or prim.IsA(UsdGeom.Cube)
31 ):
32 # use a ConvexHull for regular prims
33 utils.setCollider(prim, approximationShape="convexHull")
34 elif prim.IsA(UsdGeom.Mesh):
35 # "None" will use the base triangle mesh if available
36 # Can also use "convexDecomposition", "convexHull", "boundingSphere", "boundingCube"
37 utils.setCollider(prim, approximationShape="None")
38 pass
39pass
```

### Do Overlap Test
These snippets detect and report when objects overlap with a specified cubic/spherical region. The following is assumed: the stage contains a physics scene, all objects have collision meshes enabled, and the play button has been clicked.
The parameters: extent, origin and rotation (or origin and radius) define the cubic/spherical region to check overlap against. The output of the physX query is the number of objects that overlaps with this cubic/spherical region.

```
1import carb
2import omni
3import omni.physx
4from omni.physx import get_physx_scene_query_interface
5from pxr import UsdGeom, Gf, Vt
6
7
8
9def report_hit(hit):
10 # When a collision is detected, the object color changes to red.
11 hitColor = Vt.Vec3fArray([Gf.Vec3f(180.0 / 255.0, 16.0 / 255.0, 0.0)])
12 usdGeom = UsdGeom.Mesh.Get(omni.usd.get_context().get_stage(), hit.rigid_body)
13 usdGeom.GetDisplayColorAttr().Set(hitColor)
14 return True
15
16def check_overlap():
17 # Defines a cubic region to check overlap with
18 extent = carb.Float3(20.0, 20.0, 20.0)
19 origin = carb.Float3(0.0, 0.0, 0.0)
20 rotation = carb.Float4(0.0, 0.0, 1.0, 0.0)
21 # physX query to detect number of hits for a cubic region
22 numHits = get_physx_scene_query_interface().overlap_box(extent, origin, rotation, report_hit, False)
23 # physX query to detect number of hits for a spherical region
24 # numHits = get_physx_scene_query_interface().overlap_sphere(radius, origin, report_hit, False)
25 return numHits > 0
```

### Do Raycast Test
This snippet detects the closest object that intersects with a specified ray. The following is assumed: the stage contains a physics scene, all objects have collision meshes enabled, and the play button has been clicked.
The parameters: origin, rayDir and distance define a ray along which a ray hit might be detected. The output of the query can be used to access the object’s reference, and its distance from the raycast origin.

```
1import carb
2import omni
3import omni.physx
4from omni.physx import get_physx_scene_query_interface
5from pxr import UsdGeom, Vt, Gf
6
7def check_raycast():
8 # Projects a raycast from 'origin', in the direction of 'rayDir', for a length of 'distance' cm
9 # Parameters can be replaced with real-time position and orientation data (e.g. of a camera)
10 origin = carb.Float3(0.0, 0.0, 0.0)
11 rayDir = carb.Float3(1.0, 0.0, 0.0)
12 distance = 100.0
13 # physX query to detect closest hit
14 hit = get_physx_scene_query_interface().raycast_closest(origin, rayDir, distance)
15 if(hit["hit"]):
16 # Change object color to yellow and record distance from origin
17 usdGeom = UsdGeom.Mesh.Get(omni.usd.get_context().get_stage(), hit["rigidBody"])
18 hitColor = Vt.Vec3fArray([Gf.Vec3f(255.0 / 255.0, 255.0 / 255.0, 0.0)])
19 usdGeom.GetDisplayColorAttr().Set(hitColor)
20 distance = hit["distance"]
21 return usdGeom.GetPath().pathString, distance
22 return None, 10000.0
23
24print(check_raycast())
```

## USD How-Tos

### Creating, Modifying, Assigning Materials

```
1import omni
2from pxr import UsdShade, Sdf, Gf
3
4mtl_created_list = []
5# Create a new material using OmniGlass.mdl
6omni.kit.commands.execute(
7 "CreateAndBindMdlMaterialFromLibrary",
8 mdl_name="OmniGlass.mdl",
9 mtl_name="OmniGlass",
10 mtl_created_list=mtl_created_list,
11)
12# Get reference to created material
13stage = omni.usd.get_context().get_stage()
14mtl_prim = stage.GetPrimAtPath(mtl_created_list[0])
15# Set material inputs, these can be determined by looking at the .mdl file
16# or by selecting the Shader attached to the Material in the stage window and looking at the details panel
17omni.usd.create_material_input(mtl_prim, "glass_color", Gf.Vec3f(0, 1, 0), Sdf.ValueTypeNames.Color3f)
18omni.usd.create_material_input(mtl_prim, "glass_ior", 1.0, Sdf.ValueTypeNames.Float)
19# Create a prim to apply the material to
20result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
21# Get the path to the prim
22cube_prim = stage.GetPrimAtPath(path)
23# Bind the material to the prim
24cube_mat_shade = UsdShade.Material(mtl_prim)
25UsdShade.MaterialBindingAPI(cube_prim).Bind(cube_mat_shade, UsdShade.Tokens.strongerThanDescendants)
```
Assigning a texture to a material that supports it can be done as follows:

```
1import omni
2import carb
3from pxr import UsdShade, Sdf
4
5# Change the server to your Nucleus install, default is set to localhost in omni.isaac.sim.base.kit
6default_server = carb.settings.get_settings().get("/persistent/isaac/asset_root/default")
7mtl_created_list = []
8# Create a new material using OmniPBR.mdl
9omni.kit.commands.execute(
10 "CreateAndBindMdlMaterialFromLibrary",
11 mdl_name="OmniPBR.mdl",
12 mtl_name="OmniPBR",
13 mtl_created_list=mtl_created_list,
14)
15stage = omni.usd.get_context().get_stage()
16mtl_prim = stage.GetPrimAtPath(mtl_created_list[0])
17# Set material inputs, these can be determined by looking at the .mdl file
18# or by selecting the Shader attached to the Material in the stage window and looking at the details panel
19omni.usd.create_material_input(
20 mtl_prim,
21 "diffuse_texture",
22 default_server + "/Isaac/Samples/DR/Materials/Textures/marble_tile.png",
23 Sdf.ValueTypeNames.Asset,
24)
25# Create a prim to apply the material to
26result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
27# Get the path to the prim
28cube_prim = stage.GetPrimAtPath(path)
29# Bind the material to the prim
30cube_mat_shade = UsdShade.Material(mtl_prim)
31UsdShade.MaterialBindingAPI(cube_prim).Bind(cube_mat_shade, UsdShade.Tokens.strongerThanDescendants)
```

### Adding a transform matrix to a prim

```
1import omni
2from pxr import Gf, UsdGeom
3
4# Create a cube mesh in the stage
5stage = omni.usd.get_context().get_stage()
6result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
7# Get the prim and set its transform matrix
8cube_prim = stage.GetPrimAtPath("/World/Cube")
9xform = UsdGeom.Xformable(cube_prim)
10transform = xform.AddTransformOp()
11mat = Gf.Matrix4d()
12mat.SetTranslateOnly(Gf.Vec3d(.10, 1, 1.5))
13mat.SetRotateOnly(Gf.Rotation(Gf.Vec3d(0,1,0), 290))
14transform.Set(mat)
```

### Align two USD prims

```
1import omni
2from pxr import UsdGeom, Gf
3
4stage = omni.usd.get_context().get_stage()
5# Create a cube
6result, path_a = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
7prim_a = stage.GetPrimAtPath(path_a)
8# change the cube pose
9xform = UsdGeom.Xformable(prim_a)
10transform = xform.AddTransformOp()
11mat = Gf.Matrix4d()
12mat.SetTranslateOnly(Gf.Vec3d(.10, 1, 1.5))
13mat.SetRotateOnly(Gf.Rotation(Gf.Vec3d(0, 1, 0), 290))
14transform.Set(mat)
15# Create a second cube
16result, path_b = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
17prim_b = stage.GetPrimAtPath(path_b)
18# Get the transform of the first cube
19pose = omni.usd.utils.get_world_transform_matrix(prim_a)
20# Clear the transform on the second cube
21xform = UsdGeom.Xformable(prim_b)
22xform.ClearXformOpOrder()
23# Set the pose of prim_b to that of prim_b
24xform_op = xform.AddXformOp(UsdGeom.XformOp.TypeTransform, UsdGeom.XformOp.PrecisionDouble, "")
25xform_op.Set(pose)
```

### Get World Transform At Current Timestamp For Selected Prims

```
1import omni
2from pxr import UsdGeom, Gf
3
4usd_context = omni.usd.get_context()
5stage = usd_context.get_stage()
6
7#### For testing purposes we create and select a prim
8#### This section can be removed if you already have a prim selected
9result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
10cube_prim = stage.GetPrimAtPath(path)
11# change the cube pose
12xform = UsdGeom.Xformable(cube_prim)
13transform = xform.AddTransformOp()
14mat = Gf.Matrix4d()
15mat.SetTranslateOnly(Gf.Vec3d(.10, 1, 1.5))
16mat.SetRotateOnly(Gf.Rotation(Gf.Vec3d(0, 1, 0), 290))
17transform.Set(mat)
18omni.usd.get_context().get_selection().set_prim_path_selected(path, True, True, True, False)
19####
20
21# Get list of selected primitives
22selected_prims = usd_context.get_selection().get_selected_prim_paths()
23# Get the current timecode
24timeline = omni.timeline.get_timeline_interface()
25timecode = timeline.get_current_time() * timeline.get_time_codes_per_seconds()
26# Loop through all prims and print their transforms
27for s in selected_prims:
28 curr_prim = stage.GetPrimAtPath(s)
29 print("Selected", s)
30 pose = omni.usd.utils.get_world_transform_matrix(curr_prim, timecode)
31 print("Matrix Form:", pose)
32 print("Translation: ", pose.ExtractTranslation())
33 q = pose.ExtractRotation().GetQuaternion()
34 print(
35 "Rotation: ", q.GetReal(), ",", q.GetImaginary()[0], ",", q.GetImaginary()[1], ",", q.GetImaginary()[2]
36 )
```

### Save current stage to USD
This can be useful if generating a stage in Python and you want to store it to reload later to debugging

```
1import omni
2import carb
3
4
5# Create a prim
6result, path = omni.kit.commands.execute("CreateMeshPrimCommand", prim_type="Cube")
7# Change the path as needed
8omni.usd.get_context().save_as_stage("/path/to/asset/saved.usd", None)
```
