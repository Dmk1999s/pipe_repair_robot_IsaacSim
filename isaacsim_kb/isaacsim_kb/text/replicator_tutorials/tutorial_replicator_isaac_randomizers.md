<!-- source: replicator_tutorials/tutorial_replicator_isaac_randomizers.html | title: Randomization Snippets — Isaac Sim Documentation -->

# Randomization Snippets
Examples of randomization using USD and Isaac Sim APIs. These examples demonstrate how to randomize scenes for synthetic data generation (SDG) in scenarios where default replicator randomizers are not sufficient or applicable.
The snippets are designed to align with the structure and function names used in the replicator example snippets. In comparison they also have the option to write the data to disk by stetting `write_data=True`.
Prerequisites:

- Familiarity with USD .

- Ability to execute code from the Script Editor .

- Understanding basic replicator concepts, such as subframes .

## Randomizing Light Sources
This snippet sets up a new environment containing a cube and a sphere. It then spawns a given number of lights and randomizes selected attributes for these lights over a specified number of frames.
Randomizing Light Sources
```
1import asyncio
2import os
3
4import numpy as np
5import omni.kit.commands
6import omni.replicator.core as rep
7import omni.usd
8from isaacsim.core.utils.semantics import add_labels
9from pxr import Gf, Sdf, UsdGeom
10
11omni.usd.get_context().new_stage()
12stage = omni.usd.get_context().get_stage()
13
14sphere = stage.DefinePrim("/World/Sphere", "Sphere")
15UsdGeom.Xformable(sphere).AddTranslateOp().Set((0.0, 1.0, 1.0))
16add_labels(sphere, labels=["sphere"], instance_name="class")
17
18cube = stage.DefinePrim("/World/Cube", "Cube")
19UsdGeom.Xformable(cube).AddTranslateOp().Set((0.0, -2.0, 2.0))
20add_labels(cube, labels=["cube"], instance_name="class")
21
22plane_path = "/World/Plane"
23omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_path=plane_path, prim_type="Plane")
24plane_prim = stage.GetPrimAtPath(plane_path)
25plane_prim.CreateAttribute("xformOp:scale", Sdf.ValueTypeNames.Double3, False).Set(Gf.Vec3d(10, 10, 1))
26
27
28def sphere_lights(num):
29 lights = []
30 for i in range(num):
31 # "CylinderLight", "DiskLight", "DistantLight", "DomeLight", "RectLight", "SphereLight"
32 prim_type = "SphereLight"
33 next_free_path = omni.usd.get_stage_next_free_path(stage, f"/World/{prim_type}", False)
34 light_prim = stage.DefinePrim(next_free_path, prim_type)
35 UsdGeom.Xformable(light_prim).AddTranslateOp().Set((0.0, 0.0, 0.0))
36 UsdGeom.Xformable(light_prim).AddRotateXYZOp().Set((0.0, 0.0, 0.0))
37 UsdGeom.Xformable(light_prim).AddScaleOp().Set((1.0, 1.0, 1.0))
38 light_prim.CreateAttribute("inputs:enableColorTemperature", Sdf.ValueTypeNames.Bool).Set(True)
39 light_prim.CreateAttribute("inputs:colorTemperature", Sdf.ValueTypeNames.Float).Set(6500.0)
40 light_prim.CreateAttribute("inputs:radius", Sdf.ValueTypeNames.Float).Set(0.5)
41 light_prim.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(30000.0)
42 light_prim.CreateAttribute("inputs:color", Sdf.ValueTypeNames.Color3f).Set((1.0, 1.0, 1.0))
43 light_prim.CreateAttribute("inputs:exposure", Sdf.ValueTypeNames.Float).Set(0.0)
44 light_prim.CreateAttribute("inputs:diffuse", Sdf.ValueTypeNames.Float).Set(1.0)
45 light_prim.CreateAttribute("inputs:specular", Sdf.ValueTypeNames.Float).Set(1.0)
46 lights.append(light_prim)
47 return lights
48
49
50async def run_randomizations_async(num_frames, lights, write_data=True, delay=0):
51 if write_data:
52 writer = rep.WriterRegistry.get("BasicWriter")
53 out_dir = os.path.join(os.getcwd(), "_out_rand_lights")
54 print(f"Writing data to {out_dir}..")
55 writer.initialize(output_dir=out_dir, rgb=True)
56 rp = rep.create.render_product("/OmniverseKit_Persp", (512, 512))
57 writer.attach(rp)
58
59 for _ in range(num_frames):
60 for light in lights:
61 light.GetAttribute("xformOp:translate").Set(
62 (np.random.uniform(-5, 5), np.random.uniform(-5, 5), np.random.uniform(4, 6))
63 )
64 scale_rand = np.random.uniform(0.5, 1.5)
65 light.GetAttribute("xformOp:scale").Set((scale_rand, scale_rand, scale_rand))
66 light.GetAttribute("inputs:colorTemperature").Set(np.random.normal(4500, 1500))
67 light.GetAttribute("inputs:intensity").Set(np.random.normal(25000, 5000))
68 light.GetAttribute("inputs:color").Set(
69 (np.random.uniform(0.1, 0.9), np.random.uniform(0.1, 0.9), np.random.uniform(0.1, 0.9))
70 )
71
72 if write_data:
73 await rep.orchestrator.step_async(rt_subframes=16)
74 else:
75 await omni.kit.app.get_app().next_update_async()
76 if delay > 0:
77 await asyncio.sleep(delay)
78
79
80num_frames = 10
81lights = sphere_lights(10)
82asyncio.ensure_future(run_randomizations_async(num_frames=num_frames, lights=lights, delay=0.2))
```

## Randomizing Textures
The snippet sets up an environment, spawns a given number of cubes and spheres, and randomizes their textures for the given number of frames. After the randomizations their original materials are reassigned. The snippet also showcases how to create a new material and assign it to a prim.
Randomizing Textures
```
1import asyncio
2import os
3
4import numpy as np
5import omni.replicator.core as rep
6import omni.usd
7from isaacsim.storage.native import get_assets_root_path
8from isaacsim.core.utils.semantics import add_labels, get_labels
9from pxr import Gf, Sdf, UsdGeom, UsdShade
10
11omni.usd.get_context().new_stage()
12stage = omni.usd.get_context().get_stage()
13dome_light = stage.DefinePrim("/World/DomeLight", "DomeLight")
14dome_light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(1000.0)
15
16sphere = stage.DefinePrim("/World/Sphere", "Sphere")
17UsdGeom.Xformable(sphere).AddTranslateOp().Set((0.0, 0.0, 1.0))
18add_labels(sphere, labels=["sphere"], instance_name="class")
19
20num_cubes = 10
21for _ in range(num_cubes):
22 prim_type = "Cube"
23 next_free_path = omni.usd.get_stage_next_free_path(stage, f"/World/{prim_type}", False)
24 cube = stage.DefinePrim(next_free_path, prim_type)
25 UsdGeom.Xformable(cube).AddTranslateOp().Set((np.random.uniform(-3.5, 3.5), np.random.uniform(-3.5, 3.5), 1))
26 scale_rand = np.random.uniform(0.25, 0.5)
27 UsdGeom.Xformable(cube).AddScaleOp().Set((scale_rand, scale_rand, scale_rand))
28 add_labels(cube, labels=["cube"], instance_name="class")
29
30plane_path = "/World/Plane"
31omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_path=plane_path, prim_type="Plane")
32plane_prim = stage.GetPrimAtPath(plane_path)
33plane_prim.CreateAttribute("xformOp:scale", Sdf.ValueTypeNames.Double3, False).Set(Gf.Vec3d(10, 10, 1))
34
35
36def get_shapes():
37 stage = omni.usd.get_context().get_stage()
38 shapes = []
39 for prim in stage.Traverse():
40 labels = get_labels(prim)
41 if class_labels := labels.get("class"):
42 if "cube" in class_labels or "sphere" in class_labels:
43 shapes.append(prim)
44 return shapes
45
46
47shapes = get_shapes()
48
49def create_omnipbr_material(mtl_url, mtl_name, mtl_path):
50 stage = omni.usd.get_context().get_stage()
51 omni.kit.commands.execute("CreateMdlMaterialPrim", mtl_url=mtl_url, mtl_name=mtl_name, mtl_path=mtl_path)
52 material_prim = stage.GetPrimAtPath(mtl_path)
53 shader = UsdShade.Shader(omni.usd.get_shader_from_material(material_prim, get_prim=True))
54
55 # Add value inputs
56 shader.CreateInput("diffuse_color_constant", Sdf.ValueTypeNames.Color3f)
57 shader.CreateInput("reflection_roughness_constant", Sdf.ValueTypeNames.Float)
58 shader.CreateInput("metallic_constant", Sdf.ValueTypeNames.Float)
59
60 # Add texture inputs
61 shader.CreateInput("diffuse_texture", Sdf.ValueTypeNames.Asset)
62 shader.CreateInput("reflectionroughness_texture", Sdf.ValueTypeNames.Asset)
63 shader.CreateInput("metallic_texture", Sdf.ValueTypeNames.Asset)
64
65 # Add other attributes
66 shader.CreateInput("project_uvw", Sdf.ValueTypeNames.Bool)
67
68 # Add texture scale and rotate
69 shader.CreateInput("texture_scale", Sdf.ValueTypeNames.Float2)
70 shader.CreateInput("texture_rotate", Sdf.ValueTypeNames.Float)
71
72 material = UsdShade.Material(material_prim)
73 return material
74
75
76def create_materials(num):
77 MDL = "OmniPBR.mdl"
78 mtl_name, _ = os.path.splitext(MDL)
79 MAT_PATH = "/World/Looks"
80 materials = []
81 for _ in range(num):
82 prim_path = omni.usd.get_stage_next_free_path(stage, f"{MAT_PATH}/{mtl_name}", False)
83 mat = create_omnipbr_material(mtl_url=MDL, mtl_name=mtl_name, mtl_path=prim_path)
84 materials.append(mat)
85 return materials
86
87
88materials = create_materials(len(shapes))
89
90
91async def run_randomizations_async(num_frames, materials, textures, write_data=True, delay=0):
92 if write_data:
93 writer = rep.WriterRegistry.get("BasicWriter")
94 out_dir = os.path.join(os.getcwd(), "_out_rand_textures")
95 print(f"Writing data to {out_dir}..")
96 writer.initialize(output_dir=out_dir, rgb=True)
97 rp = rep.create.render_product("/OmniverseKit_Persp", (512, 512))
98 writer.attach(rp)
99
100 # Apply the new materials and store the initial ones to reassign later
101 initial_materials = {}
102 for i, shape in enumerate(shapes):
103 cur_mat, _ = UsdShade.MaterialBindingAPI(shape).ComputeBoundMaterial()
104 initial_materials[shape] = cur_mat
105 UsdShade.MaterialBindingAPI(shape).Bind(materials[i], UsdShade.Tokens.strongerThanDescendants)
106
107 for _ in range(num_frames):
108 for mat in materials:
109 shader = UsdShade.Shader(omni.usd.get_shader_from_material(mat, get_prim=True))
110 diffuse_texture = np.random.choice(textures)
111 shader.GetInput("diffuse_texture").Set(diffuse_texture)
112 project_uvw = np.random.choice([True, False], p=[0.9, 0.1])
113 shader.GetInput("project_uvw").Set(bool(project_uvw))
114 texture_scale = np.random.uniform(0.1, 1)
115 shader.GetInput("texture_scale").Set((texture_scale, texture_scale))
116 texture_rotate = np.random.uniform(0, 45)
117 shader.GetInput("texture_rotate").Set(texture_rotate)
118
119 if write_data:
120 await rep.orchestrator.step_async(rt_subframes=4)
121 else:
122 await omni.kit.app.get_app().next_update_async()
123 if delay > 0:
124 await asyncio.sleep(delay)
125
126 # Reassign the initial materials
127 for shape, mat in initial_materials.items():
128 if mat:
129 UsdShade.MaterialBindingAPI(shape).Bind(mat, UsdShade.Tokens.strongerThanDescendants)
130 else:
131 UsdShade.MaterialBindingAPI(shape).UnbindAllBindings()
132
133
134assets_root_path = get_assets_root_path()
135textures = [
136 assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/aggregate_exposed_diff.jpg",
137 assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/gravel_track_ballast_diff.jpg",
138 assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/gravel_track_ballast_multi_R_rough_G_ao.jpg",
139 assets_root_path + "/NVIDIA/Materials/vMaterials_2/Ground/textures/rough_gravel_rough.jpg",
140]
141
142num_frames = 10
143asyncio.ensure_future(run_randomizations_async(num_frames, materials, textures, delay=0.2))
```

## Sequential Randomizations
The snippet provides an example of more complex randomizations, where the results of the first randomization are used to determine the next randomization. It uses a custom sampler function to set the location of the camera by iterating over (almost) equidistant points on a sphere. The snippet starts by setting up the environment, a forklift, a pallet, a bin, and a dome light. For every randomization frame, it cycles through the dome light textures, moves the pallet to a random location, and then moves the bin so that it is fully on top of the pallet. Finally, it moves the camera to a new location on the sphere, ensuring it faces the bin.
Sequential Randomizations
```
1import asyncio
2import itertools
3import os
4
5import numpy as np
6import omni.replicator.core as rep
7import omni.usd
8from isaacsim.storage.native import get_assets_root_path
9from pxr import Gf, Usd, UsdGeom, UsdLux
10
11
12# https://arxiv.org/pdf/0912.4540.pdf
13def next_point_on_sphere(idx, num_points, radius=1, origin=(0, 0, 0)):
14 offset = 2.0 / num_points
15 inc = np.pi * (3.0 - np.sqrt(5.0))
16 z = ((idx * offset) - 1) + (offset / 2)
17 phi = ((idx + 1) % num_points) * inc
18 r = np.sqrt(1 - pow(z, 2))
19 y = np.cos(phi) * r
20 x = np.sin(phi) * r
21 return [(x * radius) + origin[0], (y * radius) + origin[1], (z * radius) + origin[2]]
22
23
24assets_root_path = get_assets_root_path()
25FORKLIFT_PATH = assets_root_path + "/Isaac/Props/Forklift/forklift.usd"
26PALLET_PATH = assets_root_path + "/Isaac/Props/Pallet/pallet.usd"
27BIN_PATH = assets_root_path + "/Isaac/Props/KLT_Bin/small_KLT_visual.usd"
28
29omni.usd.get_context().new_stage()
30stage = omni.usd.get_context().get_stage()
31
32dome_light = UsdLux.DomeLight.Define(stage, "/World/Lights/DomeLight")
33dome_light.GetIntensityAttr().Set(1000)
34
35forklift_prim = stage.DefinePrim("/World/Forklift", "Xform")
36forklift_prim.GetReferences().AddReference(FORKLIFT_PATH)
37if not forklift_prim.GetAttribute("xformOp:translate"):
38 UsdGeom.Xformable(forklift_prim).AddTranslateOp()
39forklift_prim.GetAttribute("xformOp:translate").Set((-4.5, -4.5, 0))
40
41pallet_prim = stage.DefinePrim("/World/Pallet", "Xform")
42pallet_prim.GetReferences().AddReference(PALLET_PATH)
43if not pallet_prim.GetAttribute("xformOp:translate"):
44 UsdGeom.Xformable(pallet_prim).AddTranslateOp()
45if not pallet_prim.GetAttribute("xformOp:rotateXYZ"):
46 UsdGeom.Xformable(pallet_prim).AddRotateXYZOp()
47
48bin_prim = stage.DefinePrim("/World/Bin", "Xform")
49bin_prim.GetReferences().AddReference(BIN_PATH)
50if not bin_prim.GetAttribute("xformOp:translate"):
51 UsdGeom.Xformable(bin_prim).AddTranslateOp()
52if not bin_prim.GetAttribute("xformOp:rotateXYZ"):
53 UsdGeom.Xformable(bin_prim).AddRotateXYZOp()
54
55cam = stage.DefinePrim("/World/Camera", "Camera")
56if not cam.GetAttribute("xformOp:translate"):
57 UsdGeom.Xformable(cam).AddTranslateOp()
58if not cam.GetAttribute("xformOp:orient"):
59 UsdGeom.Xformable(cam).AddOrientOp()
60
61
62async def run_randomizations_async(
63 num_frames, dome_light, dome_textures, pallet_prim, bin_prim, write_data=True, delay=0
64):
65 if write_data:
66 writer = rep.WriterRegistry.get("BasicWriter")
67 out_dir = os.path.join(os.getcwd(), "_out_rand_sphere_scan")
68 print(f"Writing data to {out_dir}..")
69 writer.initialize(output_dir=out_dir, rgb=True)
70 rp_persp = rep.create.render_product("/OmniverseKit_Persp", (512, 512), name="PerspView")
71 rp_cam = rep.create.render_product(str(cam.GetPath()), (512, 512), name="SphereView")
72 writer.attach([rp_cam, rp_persp])
73
74 textures_cycle = itertools.cycle(dome_textures)
75
76 bb_cache = UsdGeom.BBoxCache(time=Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
77 pallet_size = bb_cache.ComputeWorldBound(pallet_prim).GetRange().GetSize()
78 pallet_length = pallet_size.GetLength()
79 bin_size = bb_cache.ComputeWorldBound(bin_prim).GetRange().GetSize()
80
81 for i in range(num_frames):
82 # Set next background texture every nth frame and run an app update
83 if i % 5 == 0:
84 dome_light.GetTextureFileAttr().Set(next(textures_cycle))
85 await omni.kit.app.get_app().next_update_async()
86
87 # Randomize pallet pose
88 pallet_prim.GetAttribute("xformOp:translate").Set(
89 Gf.Vec3d(np.random.uniform(-1.5, 1.5), np.random.uniform(-1.5, 1.5), 0)
90 )
91 rand_z_rot = np.random.uniform(-90, 90)
92 pallet_prim.GetAttribute("xformOp:rotateXYZ").Set(Gf.Vec3d(0, 0, rand_z_rot))
93 pallet_tf_mat = omni.usd.get_world_transform_matrix(pallet_prim)
94 pallet_rot = pallet_tf_mat.ExtractRotation()
95 pallet_pos = pallet_tf_mat.ExtractTranslation()
96
97 # Randomize bin position on top of the rotated pallet area making sure the bin is fully on the pallet
98 rand_transl_x = np.random.uniform(-pallet_size[0] / 2 + bin_size[0] / 2, pallet_size[0] / 2 - bin_size[0] / 2)
99 rand_transl_y = np.random.uniform(-pallet_size[1] / 2 + bin_size[1] / 2, pallet_size[1] / 2 - bin_size[1] / 2)
100
101 # Adjust bin position to account for the random rotation of the pallet
102 rand_z_rot_rad = np.deg2rad(rand_z_rot)
103 rot_adjusted_transl_x = rand_transl_x * np.cos(rand_z_rot_rad) - rand_transl_y * np.sin(rand_z_rot_rad)
104 rot_adjusted_transl_y = rand_transl_x * np.sin(rand_z_rot_rad) + rand_transl_y * np.cos(rand_z_rot_rad)
105 bin_prim.GetAttribute("xformOp:translate").Set(
106 Gf.Vec3d(
107 pallet_pos[0] + rot_adjusted_transl_x,
108 pallet_pos[1] + rot_adjusted_transl_y,
109 pallet_pos[2] + pallet_size[2] + bin_size[2] / 2,
110 )
111 )
112 # Keep bin rotation aligned with pallet
113 bin_prim.GetAttribute("xformOp:rotateXYZ").Set(pallet_rot.GetAxis() * pallet_rot.GetAngle())
114
115 # Get next camera position on a sphere looking at the bin with a randomized distance
116 rand_radius = np.random.normal(3, 0.5) * pallet_length
117 bin_pos = omni.usd.get_world_transform_matrix(bin_prim).ExtractTranslation()
118 cam_pos = next_point_on_sphere(i, num_points=num_frames, radius=rand_radius, origin=bin_pos)
119 cam.GetAttribute("xformOp:translate").Set(Gf.Vec3d(*cam_pos))
120
121 eye = Gf.Vec3d(*cam_pos)
122 target = Gf.Vec3d(*bin_pos)
123 up_axis = Gf.Vec3d(0, 0, 1)
124 look_at_quatd = Gf.Matrix4d().SetLookAt(eye, target, up_axis).GetInverse().ExtractRotation().GetQuat()
125 cam.GetAttribute("xformOp:orient").Set(Gf.Quatf(look_at_quatd))
126
127 if write_data:
128 await rep.orchestrator.step_async(rt_subframes=4)
129 else:
130 await omni.kit.app.get_app().next_update_async()
131 if delay > 0:
132 await asyncio.sleep(delay)
133
134
135num_frames = 90
136dome_textures = [
137 assets_root_path + "/NVIDIA/Assets/Skies/Cloudy/champagne_castle_1_4k.hdr",
138 assets_root_path + "/NVIDIA/Assets/Skies/Clear/evening_road_01_4k.hdr",
139 assets_root_path + "/NVIDIA/Assets/Skies/Clear/mealie_road_4k.hdr",
140 assets_root_path + "/NVIDIA/Assets/Skies/Clear/qwantani_4k.hdr",
141]
142asyncio.ensure_future(run_randomizations_async(num_frames, dome_light, dome_textures, pallet_prim, bin_prim, delay=0.2))
```

## Physics-based Randomized Volume Filling
The snippet randomizes the stacking of objects on multiple surfaces. It randomly spawns a given number of pallets in the selected areas and then spawns physically simulated boxes on top of them. A temporary collision box area is created around the pallets to prevent the boxes from falling off. After all the boxes have been dropped, they are moved in various directions and finally pulled towards the center of the pallet for more stable stacking. Finally, the collision area is removed, after which the boxes can also fall to the ground. To allow easier sliding of the boxes into more stable positions, their friction is temporarily reduced during the simulation.
Physics-based Randomized Volume Filling
```
1import asyncio
2import random
3from itertools import chain
4
5import carb
6import omni.kit.app
7import omni.usd
8from isaacsim.core.utils.bounds import compute_aabb, compute_obb, create_bbox_cache
9from isaacsim.storage.native import get_assets_root_path
10from omni.physx import get_physx_simulation_interface
11from pxr import (
12 Gf,
13 PhysicsSchemaTools,
14 PhysxSchema,
15 Sdf,
16 Usd,
17 UsdGeom,
18 UsdPhysics,
19 UsdShade,
20 UsdUtils,
21)
22
23
24# Add transformation properties to the prim (if not already present)
25def set_transform_attributes(prim, location=None, orientation=None, rotation=None, scale=None):
26 if location is not None:
27 if not prim.HasAttribute("xformOp:translate"):
28 UsdGeom.Xformable(prim).AddTranslateOp()
29 prim.GetAttribute("xformOp:translate").Set(location)
30 if orientation is not None:
31 if not prim.HasAttribute("xformOp:orient"):
32 UsdGeom.Xformable(prim).AddOrientOp()
33 prim.GetAttribute("xformOp:orient").Set(orientation)
34 if rotation is not None:
35 if not prim.HasAttribute("xformOp:rotateXYZ"):
36 UsdGeom.Xformable(prim).AddRotateXYZOp()
37 prim.GetAttribute("xformOp:rotateXYZ").Set(rotation)
38 if scale is not None:
39 if not prim.HasAttribute("xformOp:scale"):
40 UsdGeom.Xformable(prim).AddScaleOp()
41 prim.GetAttribute("xformOp:scale").Set(scale)
42
43
44# Enables collisions with the asset (without rigid body dynamics the asset will be static)
45def add_colliders(prim):
46 # Iterate descendant prims (including root) and add colliders to mesh or primitive types
47 for desc_prim in Usd.PrimRange(prim):
48 if desc_prim.IsA(UsdGeom.Mesh) or desc_prim.IsA(UsdGeom.Gprim):
49 # Physics
50 if not desc_prim.HasAPI(UsdPhysics.CollisionAPI):
51 collision_api = UsdPhysics.CollisionAPI.Apply(desc_prim)
52 else:
53 collision_api = UsdPhysics.CollisionAPI(desc_prim)
54 collision_api.CreateCollisionEnabledAttr(True)
55
56 # Add mesh specific collision properties only to mesh types
57 if desc_prim.IsA(UsdGeom.Mesh):
58 if not desc_prim.HasAPI(UsdPhysics.MeshCollisionAPI):
59 mesh_collision_api = UsdPhysics.MeshCollisionAPI.Apply(desc_prim)
60 else:
61 mesh_collision_api = UsdPhysics.MeshCollisionAPI(desc_prim)
62 mesh_collision_api.CreateApproximationAttr().Set("convexHull")
63
64
65# Enables rigid body dynamics (physics simulation) on the prim (having valid colliders is recommended)
66def add_rigid_body_dynamics(prim, disable_gravity=False, angular_damping=None):
67 # Physics
68 if not prim.HasAPI(UsdPhysics.RigidBodyAPI):
69 rigid_body_api = UsdPhysics.RigidBodyAPI.Apply(prim)
70 else:
71 rigid_body_api = UsdPhysics.RigidBodyAPI(prim)
72 rigid_body_api.CreateRigidBodyEnabledAttr(True)
73 # PhysX
74 if not prim.HasAPI(PhysxSchema.PhysxRigidBodyAPI):
75 physx_rigid_body_api = PhysxSchema.PhysxRigidBodyAPI.Apply(prim)
76 else:
77 physx_rigid_body_api = PhysxSchema.PhysxRigidBodyAPI(prim)
78 physx_rigid_body_api.GetDisableGravityAttr().Set(disable_gravity)
79 if angular_damping is not None:
80 physx_rigid_body_api.CreateAngularDampingAttr().Set(angular_damping)
81
82
83# Create a new prim with the provided asset URL and transform properties
84def create_asset(stage, asset_url, path, location=None, rotation=None, orientation=None, scale=None):
85 prim_path = omni.usd.get_stage_next_free_path(stage, path, False)
86 reference_url = asset_url if asset_url.startswith("omniverse://") else get_assets_root_path() + asset_url
87 prim = stage.DefinePrim(prim_path, "Xform")
88 prim.GetReferences().AddReference(reference_url)
89 set_transform_attributes(prim, location=location, rotation=rotation, orientation=orientation, scale=scale)
90 return prim
91
92
93# Create a new prim with the provided asset URL and transform properties including colliders
94def create_asset_with_colliders(stage, asset_url, path, location=None, rotation=None, orientation=None, scale=None):
95 prim = create_asset(stage, asset_url, path, location, rotation, orientation, scale)
96 add_colliders(prim)
97 return prim
98
99
100# Create collision walls around the top surface of the prim with the given height and thickness
101def create_collision_walls(stage, prim, bbox_cache=None, height=2, thickness=0.3, material=None, visible=False):
102 # Use the untransformed axis-aligned bounding box to calculate the prim surface size and center
103 if bbox_cache is None:
104 bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
105 local_range = bbox_cache.ComputeWorldBound(prim).GetRange()
106 width, depth, local_height = local_range.GetSize()
107 # Raise the midpoint height to the prim's surface
108 mid = local_range.GetMidpoint() + Gf.Vec3d(0, 0, local_height / 2)
109
110 # Define the walls (name, location, size) with the specified thickness added externally to the surface and height
111 walls = [
112 ("floor", (mid[0], mid[1], mid[2] - thickness / 2), (width, depth, thickness)),
113 ("ceiling", (mid[0], mid[1], mid[2] + height + thickness / 2), (width, depth, thickness)),
114 ("left_wall", (mid[0] - (width + thickness) / 2, mid[1], mid[2] + height / 2), (thickness, depth, height)),
115 ("right_wall", (mid[0] + (width + thickness) / 2, mid[1], mid[2] + height / 2), (thickness, depth, height)),
116 ("front_wall", (mid[0], mid[1] + (depth + thickness) / 2, mid[2] + height / 2), (width, thickness, height)),
117 ("back_wall", (mid[0], mid[1] - (depth + thickness) / 2, mid[2] + height / 2), (width, thickness, height)),
118 ]
119
120 # Use the parent prim path to create the walls as children (use local coordinates)
121 prim_path = prim.GetPath()
122 collision_walls = []
123 for name, location, size in walls:
124 prim = stage.DefinePrim(f"{prim_path}/{name}", "Cube")
125 scale = (size[0] / 2.0, size[1] / 2.0, size[2] / 2.0)
126 set_transform_attributes(prim, location=location, scale=scale)
127 add_colliders(prim)
128 if not visible:
129 UsdGeom.Imageable(prim).MakeInvisible()
130 if material is not None:
131 mat_binding_api = UsdShade.MaterialBindingAPI.Apply(prim)
132 mat_binding_api.Bind(material, UsdShade.Tokens.weakerThanDescendants, "physics")
133 collision_walls.append(prim)
134 return collision_walls
135
136
137# Slide the assets independently in perpendicular directions and then pull them all together towards the given center
138async def apply_forces_async(stage, boxes, pallet, strength=550, strength_center_multiplier=2):
139 timeline = omni.timeline.get_timeline_interface()
140 timeline.play()
141 # Get the pallet center and forward vector to apply forces in the perpendicular directions and towards the center
142 pallet_tf: Gf.Matrix4d = UsdGeom.Xformable(pallet).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
143 pallet_center = pallet_tf.ExtractTranslation()
144 pallet_rot: Gf.Rotation = pallet_tf.ExtractRotation()
145 force_forward = Gf.Vec3d(pallet_rot.TransformDir(Gf.Vec3d(1, 0, 0))) * strength
146 force_right = Gf.Vec3d(pallet_rot.TransformDir(Gf.Vec3d(0, 1, 0))) * strength
147
148 physx_api = get_physx_simulation_interface()
149 stage_id = UsdUtils.StageCache.Get().GetId(stage).ToLongInt()
150 for box_prim in boxes:
151 body_path = PhysicsSchemaTools.sdfPathToInt(box_prim.GetPath())
152 forces = [force_forward, force_right, -force_forward, -force_right]
153 for force in chain(forces, forces):
154 box_tf: Gf.Matrix4d = UsdGeom.Xformable(box_prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
155 box_position = carb.Float3(*box_tf.ExtractTranslation())
156 physx_api.apply_force_at_pos(stage_id, body_path, carb.Float3(force), box_position, "Force")
157 for _ in range(10):
158 await omni.kit.app.get_app().next_update_async()
159
160 # Pull all box at once to the pallet center
161 for box_prim in boxes:
162 body_path = PhysicsSchemaTools.sdfPathToInt(box_prim.GetPath())
163 box_tf: Gf.Matrix4d = UsdGeom.Xformable(box_prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
164 box_location = box_tf.ExtractTranslation()
165 force_to_center = (pallet_center - box_location) * strength * strength_center_multiplier
166 physx_api.apply_force_at_pos(stage_id, body_path, carb.Float3(*force_to_center), carb.Float3(*box_location))
167 for _ in range(20):
168 await omni.kit.app.get_app().next_update_async()
169 timeline.pause()
170
171
172# Create a new stage and and run the example scenario
173async def stack_boxes_on_pallet_async(pallet_prim, boxes_urls_and_weights, num_boxes, drop_height=1.5, drop_margin=0.2):
174 pallet_path = pallet_prim.GetPath()
175 print(f"[BoxStacking] Running scenario for pallet {pallet_path} with {num_boxes} boxes..")
176 stage = omni.usd.get_context().get_stage()
177 bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), includedPurposes=[UsdGeom.Tokens.default_])
178
179 # Create a custom physics material to allow the boxes to easily slide into stacking positions
180 material_path = f"{pallet_path}/Looks/PhysicsMaterial"
181 default_material = UsdShade.Material.Define(stage, material_path)
182 physics_material = UsdPhysics.MaterialAPI.Apply(default_material.GetPrim())
183 physics_material.CreateRestitutionAttr().Set(0.0) # Inelastic collision (no bouncing)
184 physics_material.CreateStaticFrictionAttr().Set(0.01) # Small friction to allow sliding of stationary boxes
185 physics_material.CreateDynamicFrictionAttr().Set(0.01) # Small friction to allow sliding of moving boxes
186
187 # Apply the physics material to the pallet
188 mat_binding_api = UsdShade.MaterialBindingAPI.Apply(pallet_prim)
189 mat_binding_api.Bind(default_material, UsdShade.Tokens.weakerThanDescendants, "physics")
190
191 # Create collision walls around the top of the pallet and apply the physics material to them
192 collision_walls = create_collision_walls(
193 stage, pallet_prim, bbox_cache, height=drop_height + drop_margin, material=default_material
194 )
195
196 # Create the random boxes (without physics) with the specified weights and sort them by size (volume)
197 box_urls, box_weights = zip(*boxes_urls_and_weights)
198 rand_boxes_urls = random.choices(box_urls, weights=box_weights, k=num_boxes)
199 boxes = [create_asset(stage, box_url, f"{pallet_path}_Boxes/Box_{i}") for i, box_url in enumerate(rand_boxes_urls)]
200 boxes.sort(key=lambda box: bbox_cache.ComputeLocalBound(box).GetVolume(), reverse=True)
201
202 # Calculate the drop area above the pallet taking into account the pallet surface, drop height and the margin
203 # Note: The boxes can be spawned colliding with the surrounding collision walls as they will be pushed inwards
204 pallet_range = bbox_cache.ComputeWorldBound(pallet_prim).GetRange()
205 pallet_width, pallet_depth, pallet_heigth = pallet_range.GetSize()
206 # Move the spawn center at the given height above the pallet surface
207 spawn_center = pallet_range.GetMidpoint() + Gf.Vec3d(0, 0, pallet_heigth / 2 + drop_height)
208 spawn_width, spawn_depth = pallet_width / 2 - drop_margin, pallet_depth / 2 - drop_margin
209
210 # Use the pallet local-to-world transform to apply the local random offsets relative to the pallet
211 pallet_tf: Gf.Matrix4d = UsdGeom.Xformable(pallet_prim).ComputeLocalToWorldTransform(Usd.TimeCode.Default())
212 pallet_rot: Gf.Rotation = pallet_tf.ExtractRotation()
213
214 # Simulate dropping the boxes from random poses on the pallet
215 timeline = omni.timeline.get_timeline_interface()
216 for box_prim in boxes:
217 # Create a random location and orientation for the box within the drop area in local frame
218 local_loc = spawn_center + Gf.Vec3d(
219 random.uniform(-spawn_width, spawn_width), random.uniform(-spawn_depth, spawn_depth), 0
220 )
221 axes = [Gf.Vec3d(1, 0, 0), Gf.Vec3d(0, 1, 0), Gf.Vec3d(0, 0, 1)]
222 angles = [random.choice([180, 90, 0, -90, -180]) + random.uniform(-3, 3) for _ in axes]
223 local_rot = Gf.Rotation()
224 for axis, angle in zip(axes, angles):
225 local_rot *= Gf.Rotation(axis, angle)
226
227 # Transform the local pose to the pallet's world coordinate system
228 world_loc = pallet_tf.Transform(local_loc)
229 world_quat = Gf.Quatf((pallet_rot * local_rot).GetQuat())
230
231 # Set the spawn pose and enable collisions and rigid body dynamics with dampened angular movements
232 set_transform_attributes(box_prim, location=world_loc, orientation=world_quat)
233 add_colliders(box_prim)
234 add_rigid_body_dynamics(box_prim, angular_damping=0.9)
235
236 # Bind the physics material to the box (allow frictionless sliding)
237 mat_binding_api = UsdShade.MaterialBindingAPI.Apply(box_prim)
238 mat_binding_api.Bind(default_material, UsdShade.Tokens.weakerThanDescendants, "physics")
239 # Wait for an app update to load the new attributes
240 await omni.kit.app.get_app().next_update_async()
241
242 # Play simulation for a few frames for each box
243 timeline.play()
244 for _ in range(20):
245 await omni.kit.app.get_app().next_update_async()
246 timeline.pause()
247
248 # Iteratively apply forces to the boxes to move them around then pull them all together towards the pallet center
249 await apply_forces_async(stage, boxes, pallet_prim)
250
251 # Remove rigid body dynamics of the boxes until all other scenarios are completed
252 for box in boxes:
253 UsdPhysics.RigidBodyAPI(box).GetRigidBodyEnabledAttr().Set(False)
254
255 # Increase the friction to prevent sliding of the boxes on the pallet before removing the collision walls
256 physics_material.CreateStaticFrictionAttr().Set(0.9)
257 physics_material.CreateDynamicFrictionAttr().Set(0.9)
258
259 # Remove collision walls
260 for wall in collision_walls:
261 stage.RemovePrim(wall.GetPath())
262 return boxes
263
264
265# Run the example scenario
266async def run_box_stacking_scenarios_async(num_pallets=1, env_url=None):
267 # List of pallets and boxes to randomly choose from with their respective weights
268 pallets_urls_and_weights = [
269 ("/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_01.usd", 0.25),
270 ("/Isaac/Environments/Simple_Warehouse/Props/SM_PaletteA_02.usd", 0.75),
271 ]
272 boxes_urls_and_weights = [
273 ("/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01.usd", 0.02),
274 ("/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxB_01.usd", 0.06),
275 ("/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxC_01.usd", 0.12),
276 ("/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_01.usd", 0.80),
277 ]
278
279 # Load a predefined or create a new stage
280 if env_url is not None:
281 env_path = env_url if env_url.startswith("omniverse://") else get_assets_root_path() + env_url
282 omni.usd.get_context().open_stage(env_path)
283 stage = omni.usd.get_context().get_stage()
284 else:
285 omni.usd.get_context().new_stage()
286 stage = omni.usd.get_context().get_stage()
287 distant_light = stage.DefinePrim("/World/Lights/DistantLight", "DistantLight")
288 distant_light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(400.0)
289 if not distant_light.HasAttribute("xformOp:rotateXYZ"):
290 UsdGeom.Xformable(distant_light).AddRotateXYZOp()
291 distant_light.GetAttribute("xformOp:rotateXYZ").Set((0, 60, 0))
292 dome_light = stage.DefinePrim("/World/Lights/DomeLight", "DomeLight")
293 dome_light.CreateAttribute("inputs:intensity", Sdf.ValueTypeNames.Float).Set(500.0)
294
295 # Spawn the pallets
296 pallets = []
297 pallets_urls, pallets_weights = zip(*pallets_urls_and_weights)
298 rand_pallet_urls = random.choices(pallets_urls, weights=pallets_weights, k=num_pallets)
299 # Custom pallet poses for the environment
300 custom_pallet_locations = [
301 (-9.3, 5.3, 1.3),
302 (-9.3, 7.3, 1.3),
303 (-9.3, -0.6, 1.3),
304 ]
305 random.shuffle(custom_pallet_locations)
306 for i, pallet_url in enumerate(rand_pallet_urls):
307 # Use a custom location for every other pallet
308 if env_url is not None:
309 if i % 2 == 0 and custom_pallet_locations:
310 rand_loc = Gf.Vec3d(*custom_pallet_locations.pop())
311 else:
312 rand_loc = Gf.Vec3d(-6.5, i * 1.75, 0) + Gf.Vec3d(random.uniform(-0.2, 0.2), random.uniform(0, 0.2), 0)
313 else:
314 rand_loc = Gf.Vec3d(i * 1.5, 0, 0) + Gf.Vec3d(random.uniform(0, 0.2), random.uniform(-0.2, 0.2), 0)
315 rand_rot = (0, 0, random.choice([180, 90, 0, -90, -180]) + random.uniform(-15, 15))
316 pallet_prim = create_asset_with_colliders(
317 stage, pallet_url, f"/World/Pallet_{i}", location=rand_loc, rotation=rand_rot
318 )
319 pallets.append(pallet_prim)
320
321 # Stack the boxes on the pallets
322 total_boxes = []
323 for pallet in pallets:
324 if env_url is not None:
325 rand_num_boxes = random.randint(8, 15)
326 stacked_boxes = await stack_boxes_on_pallet_async(
327 pallet, boxes_urls_and_weights, num_boxes=rand_num_boxes, drop_height=1.0
328 )
329 else:
330 rand_num_boxes = random.randint(12, 20)
331 stacked_boxes = await stack_boxes_on_pallet_async(pallet, boxes_urls_and_weights, num_boxes=rand_num_boxes)
332 total_boxes.extend(stacked_boxes)
333
334 # Re-enable rigid body dynamics of the boxes and run the simulation for a while
335 for box in total_boxes:
336 UsdPhysics.RigidBodyAPI(box).GetRigidBodyEnabledAttr().Set(True)
337 timeline = omni.timeline.get_timeline_interface()
338 timeline.play()
339 for _ in range(200):
340 await omni.kit.app.get_app().next_update_async()
341 timeline.pause()
342
343
344async def run_scenarios_async():
345 await run_box_stacking_scenarios_async(num_pallets=6)
346 await run_box_stacking_scenarios_async(num_pallets=6, env_url="/Isaac/Environments/Simple_Warehouse/warehouse.usd")
347
348
349asyncio.ensure_future(run_scenarios_async())
```

## Simready Assets SDG Example
Script editor example for using SimReady Assets to randomize the scene. SimReady Assets are physically accurate 3D objects with realistic properties, behavior, and data connections that are optimized for simulation.
Note
The example can only run in async mode and requires the SimReady Explorer window to be enabled to process the search requests.
The example script will create an SDG randomization and capture pipeline scenario with a table, a plate, and a number of items on top of the plate. The scene will be simulated for a while and then the captured images will be saved to disk.
The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/simready_assets_sdg.py
```
[image: ../_images/isim_5.0_replicator_tut_viewport_randomization_simready_assets.jpg]
