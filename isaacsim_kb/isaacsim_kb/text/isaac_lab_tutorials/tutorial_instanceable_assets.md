<!-- source: isaac_lab_tutorials/tutorial_instanceable_assets.html | title: Instanceable Assets — Isaac Sim Documentation -->

# Instanceable Assets
Reinforcement learning often requires training in large simulation scenes with multiple clones of the same robots. As we add more and more robots into the simulation environment, the memory consumption also increases for each additional set of robot and mesh assets added. To reduce memory consumption, we can take advantage of USD’s Scenegraph Instancing functionality to mark common meshes shared by different copies of the same robots as instanceable.
By doing so, each copy of the robot will reference a single copy of meshes, avoiding the need to create multiple copies of the same meshes in the scene, thus reducing memory usage in the overall simulation environment.

## Learning Objectives
In this tutorial, we will show how to create instanceable assets in Isaac Sim. We will

- Explain requirements for making assets instanceable

- Use the URDF and MJCF importers to create instanceable assets

- Show utility methods to convert existing assets to instanceable assets

10-15 Minute Tutorial

## Getting Started

- Please refer to USD Documentation on Scenegraph Instancing for more details on instancing.

- Please refer to Tutorial: Import URDF and Tutorial: Import MJCF for more details on importer functionalities.

## Hierarchy Requirement for Instanceable Assets
USD prohibits modifying properties of prims on descendants of instanced prims. Therefore, we generally only perform instancing on mesh prims for robot assets, since properties on meshes will not differ across different environments during simulation. However, the transforms of the meshes may be different during simulation when robots in each environment are being moved in varying ways. Thus, we have to define the topology of our robot hierarchy in a specific structure in the asset tree definition in order for the instanceable flag to take action.
To mark any mesh or primitive geometry prim in the asset as instanceable, the mesh prim requires a parent Xform prim to be present, which will be used to add a reference to a master USD file containing definition of the mesh prim.
For example, the following definition cannot be marked instanceable:

```
World
|_ Robot
|_ Collisions
|_ Sphere
|_ Box
```
Instead, it will have to be modified to:

```
World
|_ Robot
|_ Collisions
|_ Sphere_Xform
| |_ Sphere
|_ Box_Xform
|_ Box
```
Any references that exist on the original Sphere and Box prims would have to be moved to Sphere_Xform and Box_Xform prims.

## Using URDF and MJCF Importers
Isaac Sim provides two importers - URDF and MJCF - for converting robot assets to USD format to be used in Isaac Sim. Both importers support the option to import robot assets directly as instanceable assets. By selecting this option, imported assets will be split into two separate USD files that follow the above hierarchy definition. Any mesh data will be written to an USD stage to be referenced by the main USD stage, which contains the main robot definition.
To use the Instanceable option in the importers, first check the Create Instanceable Asset option. Then, specify a file path to indicate the location for saving the mesh data in the Instanceable USD Path textbox. This will default to ./instanceable_meshes.usd, which will generate a file instanceable_meshes.usd that is saved to the current directory.
Once the asset is imported with these options enabled, you will see the robot definition in the stage - we will refer to this stage as the master stage. If we expand the robot hierarchy in the Stage, we will notice that the parent prims that have mesh descendants have been marked as Instanceable and they reference a prim in our Instanceable USD Path USD file. We are also no longer able to modify attributes of descendant meshes.
To add our instanced asset into a new stage, we will simply need to add our master USD file.

## Modifying Existing Assets
Due to limitations of the topology requirement for making assets instanceable, it is not as straightforward to convert existing non-instanceable assets to become instanceable. Here, we will try to provide a few small utility methods to help make the process simpler.
All utilities should be copied into and run from the script editor, which can be opened from Window > Script Editor.
First, we need to make sure our existing asset follows the hierarchy constraint defined above, where all mesh prims have a parent XForm prim present that can be used to mark the prim as instanceable. To help with the process of creating new parent prims, we provide a utility method create_parent_xforms() below to automatically insert a new Xform prim as a parent of every mesh prim in the stage.

```
1import omni.usd
2import omni.client
3
4from pxr import UsdGeom, Sdf
5
6def create_parent_xforms(asset_usd_path, source_prim_path, save_as_path=None):
7 """ Adds a new UsdGeom.Xform prim for each Mesh/Geometry prim under source_prim_path.
8 Moves material assignment to new parent prim if any exists on the Mesh/Geometry prim.
9
10 Args:
11 asset_usd_path (str): USD file path for asset
12 source_prim_path (str): USD path of root prim
13 save_as_path (str): USD file path for modified USD stage. Defaults to None, will save in same file.
14 """
15 omni.usd.get_context().open_stage(asset_usd_path)
16 stage = omni.usd.get_context().get_stage()
17
18 prims = [stage.GetPrimAtPath(source_prim_path)]
19 edits = Sdf.BatchNamespaceEdit()
20 while len(prims) > 0:
21 prim = prims.pop(0)
22 print(prim)
23 if prim.GetTypeName() in ["Mesh", "Capsule", "Sphere", "Box"]:
24 new_xform = UsdGeom.Xform.Define(stage, str(prim.GetPath()) + "_xform")
25 print(prim, new_xform)
26 edits.Add(Sdf.NamespaceEdit.Reparent(prim.GetPath(), new_xform.GetPath(), 0))
27 continue
28
29 children_prims = prim.GetChildren()
30 prims = prims + children_prims
31
32 stage.GetRootLayer().Apply(edits)
33
34 if save_as_path is None:
35 omni.usd.get_context().save_stage()
36 else:
37 omni.usd.get_context().save_as_stage(save_as_path)
```
This method can be run on an existing non-instanced USD file for an asset from the script editor, where:

- asset_usd_path is the file path to the current existing USD asset

- source_prim_path is the USD prim path to the root prim of the asset

- save_as_path is a different file path to same the modified asset to. This can be left unspecified to overwrite the existing file.

```
create_parent_xforms(
asset_usd_path=ASSET_USD_PATH,
source_prim_path=SOURCE_PRIM_PATH,
save_as_path=SAVE_AS_PATH
)
```
It is worth noting that any USD Relationships on the referenced meshes will be removed. This is because those USD Relationships originally have targets set to prims in the original prim that may no longer be valid and hence cannot be accessed from the new stage. Common examples of USD Relationships that could exist on the meshes are visual materials, physics materials, and filtered collision pairs. Therefore, it is recommended to set these USD Relationships on the meshes’ parent Xforms instead of the meshes themselves.
The above method can also be run as part of an overall conversion process, which is defined in the utility below. This utility will first insert new parent prims if create_xforms=True is specified, and generate a new USD file that is used for referencing. It will then traverse through the asset tree and mark the parent prim of any mesh or primitive type prims as instanceable, along with inserting a reference to the mesh USD stage.

```
1def convert_asset_instanceable(asset_usd_path, source_prim_path, save_as_path=None, create_xforms=True):
2 """ Makes all mesh/geometry prims instanceable.
3 Can optionally add UsdGeom.Xform prim as parent for all mesh/geometry prims.
4 Makes a copy of the asset USD file, which will be used for referencing.
5 Updates asset file to convert all parent prims of mesh/geometry prims to reference cloned USD file.
6
7 Args:
8 asset_usd_path (str): USD file path for asset
9 source_prim_path (str): USD path of root prim
10 save_as_path (str): USD file path for modified USD stage. Defaults to None, will save in same file.
11 create_xforms (bool): Whether to add new UsdGeom.Xform prims to mesh/geometry prims.
12 """
13
14 if create_xforms:
15 create_parent_xforms(asset_usd_path, source_prim_path, save_as_path)
16 asset_usd_path = save_as_path
17
18 instance_usd_path = ".".join(asset_usd_path.split(".")[:-1]) + "_meshes.usd"
19 omni.client.copy(asset_usd_path, instance_usd_path)
20 omni.usd.get_context().open_stage(asset_usd_path)
21 stage = omni.usd.get_context().get_stage()
22
23 prims = [stage.GetPrimAtPath(source_prim_path)]
24 while len(prims) > 0:
25 prim = prims.pop(0)
26 if prim:
27 if prim.GetTypeName() in ["Mesh", "Capsule", "Sphere", "Box"]:
28 parent_prim = prim.GetParent()
29 if parent_prim and not parent_prim.IsInstance():
30 parent_prim.GetReferences().AddReference(assetPath=instance_usd_path, primPath=str(parent_prim.GetPath()))
31 parent_prim.SetInstanceable(True)
32 continue
33
34 children_prims = prim.GetChildren()
35 prims = prims + children_prims
36
37 if save_as_path is None:
38 omni.usd.get_context().save_stage()
39 else:
40 omni.usd.get_context().save_as_stage(save_as_path)
```

## Summary
This tutorial covered the following topics:

- Requirements for creating instanceable assets

- Using the URDF and MJCF Importers to create instanceable assets

- Making existing assets instanceable
