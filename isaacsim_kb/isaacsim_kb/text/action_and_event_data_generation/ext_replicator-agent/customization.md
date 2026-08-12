<!-- source: action_and_event_data_generation/ext_replicator-agent/customization.html | title: Customization — Isaac Sim Documentation -->

# Customization
`Isaacsim.Replicator.Agent` (IRA) supports custom environment assets, custom character assets, and custom character animations. This section will guide you through the process of setting up your custom assets for use in IRA.

## Custom Environment Assets
You can use your custom scene assets. To use custom environment assets, they must be in USD format and have the correct root layer attributes. This guide helps you find environment assets, convert scene assets to `.usd` format, configure and light the scene, and create the Navigation Mesh for the scene.

### Find Environment Assets
We recommend browsing the Content Browser for high quality assets that are ready-to-use for Omniverse.
You can also browse 3D asset stores like Turbosquid and Sketchfab . You can filter asset search on these sites by “USD” to find Omniverse-ready assets. Any non-USD environment asset you want to use must be converted to USD.

### Converting Non-USD Assets to USD
Omniverse offers a wide range of tools to convert your asset to USD. Follow the Omniverse Connections Overview for more information.

### Configure the Environment Asset
With your environment asset in USD format, you can adjust scale or lighting before importing it into Isaac Sim.
To use a custom environment asset with IRA, you must create a Navigation Mesh for it. This section aims to help you set up your new environment asset so it’s ready for the extension.

#### Unit and Coordinates System
IRA assumes that the environment asset is using meter as the unit and Z-up as the world coordinate system.
With the environment asset open in Isaac Sim, go to the right panel and select the Layer tab. Click the “Root Layer”, and the properties of the “World” are shown in the bottom right Property panel.
Typically, using Isaac Sim to convert the unit and system is the easiest way to get consistent coordinates:

- Open the Isaac Sim default empty stage.

- Drag your asset into the Stage panel on the left side.

Isaac Sim automatically creates a new Xform for it and converts it to the right config.
Alternatively, you can change the World Axis to Z and Meters Per Unit to `1` from the Layer Metadata attribute under the Root Layer Property, which can be found as the below default image shows. After changing the numbers, the scene is rotated in the wrong direction and in the wrong scale. You need to manually rotate and scale it to the right direction and size. To verify that the scene is in the right configuration, drag a character into the stage and see if it matches the size and direction of the environment.
Note
Some scenes might be created without having real-world-scale in mind. For these assets, it is recommended to drag a character into the stage and scale the root xform of the environment asset according to how big it is compared to the scene.

#### Lighting the Environment
Typically, the original lighting of an asset isn’t compatible with Isaac Sim after the conversion, or there might be no lighting at all. Follow the Omniverse lighting guide to create the lighting setup for your environment. We recommend starting with a Dome Light for your environment.

#### Building the NavMesh
NavMesh defines the area that the actors can stand on and navigate to. It is essential for the random spawning function and command generation to work. The Omni.Anim.Navigation extension has greatly simplified this process and is continuing to evolve.
This section guides you through building a basic navigation mesh and teaches you some tricks for making modifications to the NavMesh. The steps to build a NavMesh are as follows:

- Add NavMesh Volume.

- Adjust settings.

- Bake the NavMesh.

- NavMesh Volume
Any polygons that intersect with the NavMesh Volume are considered walkable area. If you have a giant polygon as the ground, and the navmesh volume only encloses a small part of the ground, it still generates navmesh on the whole ground because it’s determined by intersecting polygons instead of enclosing ones.
Follow these steps to create a Navmesh Volume:

- Right-click the Stage panel.

- Select Create > Navigation > NavMesh Include Volume. The NavMeshVolume appears in the viewport as a box wireframe.

- Change its scale in the regular way to cover the whole floor area.

- (Optional) Assign navigation area for the current NavMesh. To do this, you can go to Window > Navigation > NavMesh, and modify settings under Areas section.

## Custom Character Assets
IRA supports using your own USD character assets. Custom characters must be retargeted to the NVIDIA biped character before animations can be correctly applied. Refer to Animation Retargeting for how to retarget a character. In addition, make sure the characters are in the same measurement (in meter) and have the same orientation (Z as up axis, -Y as forward axis) as our supplied characters if you want to use our animations.
IRA also expects the character folder to contain a list of sub-folders, where each sub-folder has only 1 USD inside (the character USD). Organize your custom character assets in this manner. Now you can set the character asset folder in the config file to your custom character assets folder and spawn custom characters. Review below image for the folder structure.
Note
You can also refer to `[Isaac Sim Assets Path]/Isaac/People/Characters` as an example for the expected folder structure.

### Import Unreal Characters
The Unreal Engine Marketplace offers high-quality content that can potentially be used in IRA. In this section, we demonstrate how to enable Unreal characters for use in Isaac Sim.

- Export characters from Unreal as USD. Refer to Unreal Engine Connector for details.

- Import USD Unreal characters into Isaac Sim. Because Unreal characters are in centimeters and have a different skeleton hierarchy than the NVIDIA biped character, the following steps are required:

- Run the following script in the script editor to scale characters from centimeters to meters.
Scale a character prim
```
1from pxr import Gf, Usd
2import omni.usd
3
4def convert_mesh(mesh_prim, scaleMatrix):
5 # convert points
6 points_attr = mesh_prim.GetAttribute("points")
7 if points_attr != None:
8 points = points_attr.Get()
9 for i in range(len(points)):
10 p = points[i]
11 p = scaleMatrix.Transform(p) # change unit
12 points[i] = p
13 points_attr.Set(points)
14 # convert extent
15 extent_attr = mesh_prim.GetAttribute("extent")
16 if extent_attr != None:
17 extents = extent_attr.Get()
18 else:
19 extents = None
20 if extents != None:
21 for i in range(len(extents)):
22 extent = extents[i]
23 extent = scaleMatrix.Transform(extent) # change unit
24 extents[i] = extent
25 extent_attr.Set(extents)
26
27def convert_transform(transform, scaleMatrix):
28 trans = transform.ExtractTranslation()
29 rot = transform.ExtractRotation()
30 trans = scaleMatrix.Transform(trans) # unit conversion
31 transform.SetTranslateOnly(trans)
32 transform.SetRotateOnly(rot)
33 return transform
34
35def convert_skeleton(skeleton_prim, scaleMatrix):
36 # Convert bind pose
37 bind_transforms_attr = skeleton_prim.GetAttribute("bindTransforms")
38 if bind_transforms_attr != None:
39 bind_transforms = bind_transforms_attr.Get()
40 if bind_transforms != None:
41 for i in range(0, len(bind_transforms)):
42 bind_transforms[i] = convert_transform(bind_transforms[i], scaleMatrix)
43 bind_transforms_attr.Set(bind_transforms)
44 # Convert rest pose
45 rest_transforms_attr = skeleton_prim.GetAttribute("restTransforms")
46 if rest_transforms_attr != None:
47 rest_transforms = rest_transforms_attr.Get()
48 if rest_transforms != None:
49 for i in range(0, len(rest_transforms)):
50 rest_transforms[i] = convert_transform(rest_transforms[i], scaleMatrix)
51 rest_transforms_attr.Set(rest_transforms)
52 # Convert retarget pose
53 retarget_transforms_attr = skeleton_prim.GetAttribute("controlRig:retargetTransforms")
54 if retarget_transforms_attr != None:
55 retarget_transforms = retarget_transforms_attr.Get()
56 if retarget_transforms != None:
57 for i in range(len(retarget_transforms)):
58 if i == 0:
59 retarget_transforms[i] = convert_transform(retarget_transforms[i], scaleMatrix)
60 else:
61 retarget_transforms[i] = convert_transform(retarget_transforms[i], scaleMatrix)
62 retarget_transforms_attr.Set(retarget_transforms)
63 # Convert default animation source
64 animation_source_attr = skeleton_prim.GetRelationship("skel:animationSource")
65 if animation_source_attr != None:
66 skeleton_prim.CreateRelationship("skel:animationSource")
67
68# From centimeter to meter
69scale_factor = 0.01
70character_root_prim_path = "[your character prim root]"
71
72scaleMatrix = Gf.Matrix4d(1.0)
73scaleMatrix.SetScale(scale_factor)
74
75character_root_prim = omni.usd.get_context().get_stage().GetPrimAtPath(character_root_prim_path)
76for prim in Usd.PrimRange(character_root_prim):
77 if prim.GetTypeName() == "Mesh":
78 convert_mesh(prim, scaleMatrix)
79 elif prim.GetTypeName() == "Skeleton":
80 convert_skeleton(prim, scaleMatrix)
```

- Retarget the characters to NVIDIA biped character by following Animation Retargeting .

If the characters are correctly setup, they can replicate the movement of an NVIDIA biped character by running its animation graph.

## Custom Character Animations
IRA supports custom character animations in the form of custom command. Refer to the IRA Custom Character Commands guide for more information.
However, before an animation is ready to be imported, you need to make sure that the animation is compatible with the NVIDIA biped skeleton. You can run the following script to retarget an animation from one skeleton to another.

```
omni.kit.commands.execute( 'CreateRetargetAnimationsCommand', source_skeleton_path='',
target_skeleton_path='',
source_animation_paths=[''],
target_animation_parent_path='',
set_root_identity=False )
```
