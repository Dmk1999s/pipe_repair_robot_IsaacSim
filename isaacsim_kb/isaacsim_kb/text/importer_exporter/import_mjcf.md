<!-- source: importer_exporter/import_mjcf.html | title: Tutorial: Import MJCF — Isaac Sim Documentation -->

# Tutorial: Import MJCF

## Learning Objectives
This tutorial shows how to import a MJCF model and convert it to a USD in NVIDIA Isaac Sim. After this tutorial, you can use MJCF files in your pipeline while using NVIDIA Isaac Sim.
5-10 Minute Tutorial

## Getting Started
Prerequisites

- Review the Quick Tutorials prior to beginning this tutorial.

## Using the MJCF Importer
Begin by importing an Ant MJCF from the Built in MJCF files that come with the extension.

- Load the MJCF Importer extension, which should be automatically loaded when NVIDIA Isaac Sim opens and can be accessed from the File > Import menu. If not MJCF files are not listed in the import formats, go to Window > Extensions and enable `isaacsim.asset.importer.mjcf`.

- In the file selection dialog box, navigate to the desired folder, and select the desired MJCF file. For this example, use the Humanoid `nv_humanoid.xml` file that comes with this extension, included in the extension assets. To find it:

- Click on the folder icon beside AUTOLOAD to find the isaacsim.asset.importer.mjcf extension.

- Navigate to `/data/mjcf` and find `nv_humanoid.xml`.

- Change the import options according to the your needs. Check Import Options for more information on the import options.
[image: Select MJCF to Import]

- Click the Import button to add the robot to the stage.
[image: Imported Humanoid]

The robot is now imported into the stage. You can now use it in your simulation. You can perform additional changes to the asset after it’s imported, such as adding sensors, changing materials, and updating the joint drives and configuration to achieve a more stable simulation. Robots are mapped as articulations in the simulation, and for a complete guide in tuning articulations, refer to Articulation Stability Guide .

## Importing MJCF Using Python
Do the exact same thing with Python scripting instead.

- Open the Script Editor. Go to the top Menu Bar and click Window > Script Editor.

- The window for the Script Editor is visible in the workspace.

- Copy the following code into the Script Editor window.

```
1import omni.kit.commands
2from pxr import UsdLux, Sdf, Gf, UsdPhysics, PhysicsSchemaTools
3
4# create new stage
5omni.usd.get_context().new_stage()
6
7# setting up import configuration:
8status, import_config = omni.kit.commands.execute("MJCFCreateImportConfig")
9import_config.set_fix_base(False)
10import_config.set_make_default_prim(False)
11
12# Get path to extension data:
13ext_manager = omni.kit.app.get_app().get_extension_manager()
14ext_id = ext_manager.get_enabled_extension_id("isaacsim.asset.importer.mjcf")
15extension_path = ext_manager.get_extension_path(ext_id)
16
17# import MJCF
18omni.kit.commands.execute(
19 "MJCFCreateAsset",
20 mjcf_path=extension_path + "/data/mjcf/nv_ant.xml",
21 import_config=import_config,
22 prim_path="/ant"
23)
24
25# get stage handle
26stage = omni.usd.get_context().get_stage()
27
28# enable physics
29scene = UsdPhysics.Scene.Define(stage, Sdf.Path("/physicsScene"))
30
31# set gravity
32scene.CreateGravityDirectionAttr().Set(Gf.Vec3f(0.0, 0.0, -1.0))
33scene.CreateGravityMagnitudeAttr().Set(981.0)
34
35# add lighting
36distantLight = UsdLux.DistantLight.Define(stage, Sdf.Path("/DistantLight"))
37distantLight.CreateIntensityAttr(500)
```

- Click the Run (Ctrl + Enter) button to import the Ant robot.

## Summary
This tutorial covered the following topics:

- Importing MJCF file using GUI

- Importing MJCF file using Python

- Create a Ground Plane

### Further Learning
Review MJCF Importer Extension to learn more about the different configuration settings to import a MJCF in NVIDIA Isaac Sim.
