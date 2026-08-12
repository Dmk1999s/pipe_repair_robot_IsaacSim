<!-- source: importer_exporter/ext_isaacsim_asset_importer_mjcf.html | title: MJCF Importer Extension — Isaac Sim Documentation -->

# MJCF Importer Extension
Note
Starting from the Isaac Sim 2023.1.0 release, the MJCF importer has been open-sourced. Source code and information for contributing can be found at our Github repository . As of Isaac sim 5.0, the former dedicated repository has been deprecated, and the code has been moved to the Isaac Sim repository.
The MJCF Importer Extension Extension is used to import MuJoCo representations of robots. MuJoCo Modeling XML File (MJCF) , is an XML format for representing a robot model in the MuJoCo simulator.
To access this extension, go to the top menu bar and click File > Import.
This extension is enabled by default. If it is ever disabled, it can be re-enabled from the Extension Manager by searching for `isaacsim.asset.importer.mjcf`.

## Conventions
Note
Special characters in link or joint names are not supported and are replaced with an underscore. In the event that the name starts with an underscore due to the replacement, an a is pre-pended. It is recommended to make these name changes in the MJCF directly.
Refer to the Isaac Sim Conventions documentation for a complete list of NVIDIA Isaac Sim conventions.

### User Interface
[image: User interface for MJCF Importer]

## Import Options
Model: Provides the Options to Import in Stage, or add as a referenced model. If Create in Stage is selected. Choose the options to Set as the default prim, and Clear Stage on Import. By default both are left unchecked.
Links: Choose:

- Moveable base (for example, a wheeled robot) the base link will be set to moveable.

- Static base (for example, a 6DoF robotic arm) the base link will be fixed in place with a `root_joint`.

The Default Density is used for links that do not have a mass specified in the URDF. If the density is set to `0`, the physics engine will automatically compute the density with its default value.
Colliders:

- Visualize Collision Geometry: When selected, the collision geometry will be visible in the viewport.

- Allow self-collision: Enables self collision between adjacent links. It might cause instability if the collision meshes are intersecting at the joint.

Note

- It is recommended that you set Self Collision to false unless you are certain that links on the robot are not self colliding

- You must have write access to the output directory used for import, it will default to the current open stage, change this as necessary.

### Robot Properties
There might be many properties you want to tune on your robot. These properties can be spread across many different Schemas and APIs.
The general steps of getting and setting a parameter are:

- Find which API the parameter is under. Most common ones can be found in the Pixar USD API .

- Get the prim handle that the API is applied to. For example, Articulation and Drive APIs are applied to joints, and MassAPIs are applied to the rigid bodies.

- Get the handle to the API. From there on, you can Get or Set the attributes associated with that API.

For example, if you want to set the wheel’s drive velocity and the actuators’ stiffness, you must find the DriveAPI:

```
1# get handle to the Drive API for both wheels
2left_wheel_drive = UsdPhysics.DriveAPI.Get(stage.GetPrimAtPath("/carter/chassis_link/left_wheel"), "angular")
3right_wheel_drive = UsdPhysics.DriveAPI.Get(stage.GetPrimAtPath("/carter/chassis_link/right_wheel"), "angular")
4
5# Set the velocity drive target in degrees/second
6left_wheel_drive.GetTargetVelocityAttr().Set(150)
7right_wheel_drive.GetTargetVelocityAttr().Set(150)
8
9# Set the drive damping, which controls the strength of the velocity drive
10left_wheel_drive.GetDampingAttr().Set(15000)
11right_wheel_drive.GetDampingAttr().Set(15000)
12
13# Set the drive stiffness, which controls the strength of the position drive
14# In this case because we want to do velocity control this should be set to zero
15left_wheel_drive.GetStiffnessAttr().Set(0)
16right_wheel_drive.GetStiffnessAttr().Set(0)
```
Alternatively you can use the Omniverse Commands Tool Extension to change a value in the UI and get the associated Omniverse command that changes the property.
Note

- The drive stiffness parameter should be set when using position control on a joint drive.

- The drive damping parameter should be set when using velocity control on a joint drive.

- A combination of setting stiffness and damping on a drive will result in both targets being applied, this can be useful in position control to reduce vibrations.

### References
Refer to the Asset Structure for more information about the asset structure.

### Tutorial
Review Tutorial: Import MJCF .
