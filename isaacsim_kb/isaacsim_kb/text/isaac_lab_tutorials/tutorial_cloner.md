<!-- source: isaac_lab_tutorials/tutorial_cloner.html | title: Getting Started with Cloner — Isaac Sim Documentation -->

# Getting Started with Cloner
Training reinforcement learning policies can often benefit from collecting trajectories from vectorized copies of environments performing the same task. The Cloner interface is designed to simplify the environment design process for such a scene by providing APIs that allow users to clone a given environment as many times as desired.
In addition to providing cloning functionality, the Cloner interface also provides utilities to generate target paths, automatically compute target transforms, as well as filtering out collisions between clones.

## Learning Objectives
In this tutorial, we will walk through the Cloner interface:

- Set up an example using the Cloner class

- Set up an example using the GridCloner class

- Use APIs from isaacsim.core.api to access cloned objects

- Understand advanced cloning with physics replication and additional parameters

10-15 Minute Tutorial

## Getting Started
We will first launch Isaac Sim and enable the Cloner extension. Open the Extensions window from the UI by navigating to Window > Extensions from the top menu bar. Find the Isaac Sim Cloner extension, or isaacsim.core.cloner and enable the extension via the toggle switch on the right side of the extension name.
Next, open the Script Editor window from the UI by navigating to Window > Script Editor from the top menu bar. All example code in this tutorial can be pasted into the Script Editor window and executed by clicking on Run.

## Introduction to Cloner
Please make sure isaacsim.core.cloner is enabled from the Extensions window before running the snippets.
Let’s first start with a simple use case of the Cloner interface. In this example, we will create a scene with 4 cubes.

```
1from isaacsim.core.cloner import Cloner # import Cloner interface
2from isaacsim.core.utils.stage import get_current_stage
3from pxr import UsdGeom
4
5# create our base environment with one cube
6base_env_path = "/World/Cube_0"
7UsdGeom.Cube.Define(get_current_stage(), base_env_path)
8
9# create a Cloner instance
10cloner = Cloner()
11
12# generate 4 paths that begin with "/World/Cube" - path will be appended with _{index}
13target_paths = cloner.generate_paths("/World/Cube", 4)
14
15# clone the cube at target paths
16cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths)
```
We should now have 4 cubes in our stage: “/World/Cube_0”, “/World/Cube_1”, “/World/Cube_2”, “/World/Cube_3”. But you may have noticed that the cubes have all been created at the same position.
We can add a transform to each cube, simply replace the last line of the previous code with the following:

```
1import numpy as np
2
3cube_positions = np.array([[0, 0, 0], [3, 0, 0], [6, 0, 0], [9, 0, 0]])
4
5# clone the cube at target paths at specified positions
6cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths, positions=cube_positions)
```
It is also possible to specify the orientations of each clone by passing in an orientations argument, which should also be a np.ndarray.

## Grid Cloner
Grid Cloner is a specialized Cloner class that automatically places clones in a grid, without requiring pre-computed translations and orientations from the user.
To use the Grid Cloner, we will need to specify the spacing we would like between each clone at initialization.

```
1from isaacsim.core.cloner import GridCloner # import GridCloner interface
2from isaacsim.core.utils.stage import get_current_stage
3from pxr import UsdGeom
4
5# create our base environment with one cube
6base_env_path = "/World/Cube_0"
7UsdGeom.Cube.Define(get_current_stage(), base_env_path)
8
9# create a GridCloner instance
10cloner = GridCloner(spacing=3)
11
12# generate 4 paths that begin with "/World/Cube" - path will be appended with _{index}
13target_paths = cloner.generate_paths("/World/Cube", 4)
14
15# clone the cube at target paths
16cloner.clone(source_prim_path="/World/Cube_0", prim_paths=target_paths)
```
Now we have a scene with 4 cubes placed in a grid!

## Accessing Cloned Objects
Now that we have created our scene with the Cloner interface, we can access states for the cloned objects using APIs from isaacsim.core.api. These APIs allow us to collect and apply data as vectorized tensors to all or a subset of objects at once, avoiding iterating through objects in loops.
We will show a simple example of retrieving the global transforms of all of the boxes in the scene, as well as setting a new translation on the boxes.

```
1# import the XFormPrimView interface from isaacsim.core.api for APIs for XForm prims
2from isaacsim.core.prims import XFormPrimView
3
4# retrieve a View containing all 4 boxes by using a wildcard expression that matches the prim paths for all boxes
5boxes = XFormPrimView("/World/Cube_*")
6
7# retrieve the global transforms of all boxes
8# - positions will be a vector of shape (4, 3) for X, Y, Z axes of translation
9# - orientations will be a vector of shape (4, 4) for W, X, Y, Z axes of quaternion
10positions, orientations = boxes.get_world_poses()
11
12# increase positions on the Z axis to move boxes up by 1.5 units
13positions[:, 2] += 1.5
14# apply the new positions
15boxes.set_world_poses(positions, orientations)
```

## Physics Replication
The cloning process can take advantage of faster physics parsing by replicating physics directly in PhysX, avoiding copying of USD physics properties. This feature can be enabled by passing in a new parameter replicate_physics=True when cloning objects in the scene. Note that to use this feature, the user must also specify some additional parameters: base_env_paths and root_path. base_env_paths points to the ancestry prim of all clones and root_path specifies the prefix of each target clone path before the index. This also imposes the limitation that all target clone paths must be appended by an incremental index. If both define_base_env() and generate_paths() APIs have already been called before cloning, the user can avoid specifying base_env_paths and root_path parameters as the information has already been provided to the Cloner class.

```
1cloner.clone(
2 source_prim_path="/World/Ants/Ant_0",
3 prim_paths=target_paths,
4 position_offsets=position_offsets,
5 replicate_physics=True,
6 base_env_path="/World/Ants",
7 root_path="/World/Ants/Ant_"
8)
```
A full example using physics replication can be found at standalone_examples/api/isaacsim.core.cloner/cloner_ants.py.
There are currently some features that are not supported by physics replication. For example, runtime modification of shape properties are not allowed on prims that have been created using physics replication. For scenes that require randomization or modification of shape properties (such as materials, friction, restitution, etc.) at run time, please do not enable physics replication when cloning objects.

## Additional Parameters
In addition to physics replication, the Cloner also provides an option to copy from the source prim. This flag can be set with the copy_from_source argument.

```
1cloner.clone(
2 source_prim_path="/World/Ants/Ant_0",
3 prim_paths=target_paths,
4 position_offsets=position_offsets,
5 replicate_physics=True,
6 base_env_path="/World/Ants",
7 root_path="/World/Ants/Ant_",
8 copy_from_source=True
9)
```
By default, copy_from_source is set to False, in which case the cloned prims will be defined as USD Inherits of the source prim. The cloning process will be faster when USD Inherits are used for cloning. However, any changes that are made to the source prim after cloning will also reflect in the cloned prims.
If this behavior is undesired, please set copy_from_source to True. When copy_from_source is set to True, the cloned prims will be defined as copies of the source prim. After cloning, each cloned prim will be an individual entity and any changes in the source prim will not be reflected on the cloned prims. This setting can be useful in cases where cloned environments are not designed to be identical.

## Summary
This tutorial covered the following topics:

- How to use the Cloner interface

- How to use the GridCloner interface

- How to access states of cloned objects with isaacsim.core.api APIs

- Advanced cloning with physics replication and additional parameters

### Next Steps
Continue on to the next tutorial in our Reinforcement Learning Tutorials series, Instanceable Assets , to learn about instanceable assets for improving memory efficiency.
