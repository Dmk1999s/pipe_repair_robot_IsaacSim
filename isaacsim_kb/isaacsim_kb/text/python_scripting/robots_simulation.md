<!-- source: python_scripting/robots_simulation.html | title: Robot Simulation Snippets — Isaac Sim Documentation -->

# Robot Simulation Snippets
Note
The following scripts should only be run on the default new stage and only once. You can try these by creating a new stage via File > New and running from Window > Script Editor

## Create Articulations and ArticulationView
The following snippet adds two Franka articulations to the scene and creates a view object to manipulate their properties in parallel

```
1import asyncio
2import numpy as np
3from isaacsim.core.api.world import World
4from isaacsim.core.prims import Articulation
5from isaacsim.core.utils.nucleus import get_assets_root_path
6from isaacsim.core.utils.stage import add_reference_to_stage
7
8async def example():
9 if World.instance():
10 World.instance().clear_instance()
11 world=World()
12 await world.initialize_simulation_context_async()
13 world.scene.add_default_ground_plane()
14
15 # add franka articulations
16
17 asset_path = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
18 robot1 = add_reference_to_stage(usd_path=asset_path, prim_path="/World/Franka_1")
19 robot1.GetVariantSet("Gripper").SetVariantSelection("AlternateFinger")
20 robot1.GetVariantSet("Mesh").SetVariantSelection("Quality")
21 robot2 = add_reference_to_stage(usd_path=asset_path, prim_path="/World/Franka_2")
22 robot2.GetVariantSet("Gripper").SetVariantSelection("AlternateFinger")
23 robot2.GetVariantSet("Mesh").SetVariantSelection("Quality")
24
25 # batch process articulations via an Articulation
26 frankas_view = Articulation(prim_paths_expr="/World/Franka_[1-2]", name="frankas_view")
27 world.scene.add(frankas_view)
28 await world.reset_async()
29 # set root body poses
30 new_positions = np.array([[-1.0, 1.0, 0], [1.0, 1.0, 0]])
31 frankas_view.set_world_poses(positions=new_positions)
32 # set the joint positions for each articulation
33 frankas_view.set_joint_positions(np.array([[1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
34 [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]]))
35asyncio.ensure_future(example())
```
See the API Documentation for all the possible operations supported by `Articulation`.

## Joints Control
To run the following code snippets:

- The following code snippets assume that the Stage contains a Franka robot at the `/Franka` prim path. Go to the top menu bar and click Create > Robots > Franka Emika Panda Arm to add a Franka to the scene.

- At least one frame of simulation must occur before the Dynamic Control APIs work correctly. To start the simulation:

- (Option #1) Press the `PLAY` button to begin simulating.

- (Option #2) Use the following code snippet to start the simulation using the Python API before running any of the snippets below.

```
1import omni
2omni.timeline.get_timeline_interface().play()
```

We recommend using the built-in Script Editor to test these snippets. For deeper development, please see the Workflows tutorial.
To access the Script Editor, go to the top menu bar and click Window > Script Editor.
Note
The snippets are disparate examples, running them out of order may have unintended consequences.
Note
The snippets are for demonstrative purposes, the resulting movements may not respect the robot’s kinematic limitations.

### Position Control

```
1from omni.isaac.dynamic_control import _dynamic_control
2import numpy as np
3dc = _dynamic_control.acquire_dynamic_control_interface()
4articulation = dc.get_articulation("/Franka")
5# Call this each frame of simulation step if the state of the articulation is changing.
6dc.wake_up_articulation(articulation)
7joint_angles = [np.random.rand(9) * 2 - 1]
8dc.set_articulation_dof_position_targets(articulation, joint_angles)
```

### Single DOF Position Control

```
1from omni.isaac.dynamic_control import _dynamic_control
2import numpy as np
3dc = _dynamic_control.acquire_dynamic_control_interface()
4articulation = dc.get_articulation("/Franka")
5dc.wake_up_articulation(articulation)
6dof_ptr = dc.find_articulation_dof(articulation, "panda_joint2")
7dc.set_dof_position_target(dof_ptr, -1.5)
```

### Velocity Control

```
1from pxr import UsdPhysics
2stage = omni.usd.get_context().get_stage()
3for prim in stage.TraverseAll():
4 prim_type = prim.GetTypeName()
5 if prim_type in ["PhysicsRevoluteJoint" , "PhysicsPrismaticJoint"]:
6 if prim_type == "PhysicsRevoluteJoint":
7 drive = UsdPhysics.DriveAPI.Get(prim, "angular")
8 else:
9 drive = UsdPhysics.DriveAPI.Get(prim, "linear")
10 if drive:
11 drive.GetStiffnessAttr().Set(0)
12from omni.isaac.dynamic_control import _dynamic_control
13import numpy as np
14dc = _dynamic_control.acquire_dynamic_control_interface()
15#Note: getting the articulation has to happen after changing the drive stiffness
16articulation = dc.get_articulation("/Franka")
17dc.wake_up_articulation(articulation)
18joint_vels = [-np.random.rand(9)*10]
19dc.set_articulation_dof_velocity_targets(articulation, joint_vels)
```

### Single DOF Velocity Control

```
1from pxr import UsdPhysics
2stage = omni.usd.get_context().get_stage()
3panda_joint2_drive = UsdPhysics.DriveAPI.Get(stage.GetPrimAtPath("/Franka/panda_link1/panda_joint2"), "angular")
4panda_joint2_drive.GetStiffnessAttr().Set(0)
5from omni.isaac.dynamic_control import _dynamic_control
6import numpy as np
7dc = _dynamic_control.acquire_dynamic_control_interface()
8#Note: getting the articulation has to happen after changing the drive stiffness
9articulation = dc.get_articulation("/Franka")
10dc.wake_up_articulation(articulation)
11dof_ptr = dc.find_articulation_dof(articulation, "panda_joint2")
12dc.set_dof_velocity_target(dof_ptr, 0.2)
```

### Torque Control

```
1from omni.isaac.dynamic_control import _dynamic_control
2import numpy as np
3dc = _dynamic_control.acquire_dynamic_control_interface()
4articulation = dc.get_articulation("/Franka")
5dc.wake_up_articulation(articulation)
6joint_efforts = [-np.random.rand(9) * 1000]
7dc.set_articulation_dof_efforts(articulation, joint_efforts)
```

### Check Object Type

```
1from omni.isaac.dynamic_control import _dynamic_control
2dc = _dynamic_control.acquire_dynamic_control_interface()
3
4# Check to see what type of object the target prim is
5obj_type = dc.peek_object_type("/Franka")
6# This print statement should print ObjectType.OBJECT_ARTICULATION
7print(obj_type)
```

### Query Articulation

```
1from omni.isaac.dynamic_control import _dynamic_control
2dc = _dynamic_control.acquire_dynamic_control_interface()
3
4# Get a handle to the Franka articulation
5# This handle will automatically update if simulation is stopped and restarted
6art = dc.get_articulation("/Franka")
7
8# Get information about the structure of the articulation
9num_joints = dc.get_articulation_joint_count(art)
10num_dofs = dc.get_articulation_dof_count(art)
11num_bodies = dc.get_articulation_body_count(art)
12
13# Get a specific degree of freedom on an articulation
14dof_ptr = dc.find_articulation_dof(art, "panda_joint2")
15
16# print the information
17print("Articulation:", art)
18print("Joint count:", num_joints)
19print("DOF count:", num_dofs)
20print("Body count:", num_bodies)
21print("DOF pointer for panda_joint2:", dof_ptr)
```

### Read Joint State

```
1from omni.isaac.dynamic_control import _dynamic_control
2dc = _dynamic_control.acquire_dynamic_control_interface()
3
4# Print the state of each degree of freedom in the articulation
5art = dc.get_articulation("/Franka")
6dof_states = dc.get_articulation_dof_states(art, _dynamic_control.STATE_ALL)
7print(dof_states)
8
9# Get state for a specific degree of freedom
10dof_ptr = dc.find_articulation_dof(art, "panda_joint2")
11dof_state = dc.get_dof_state(dof_ptr, _dynamic_control.STATE_ALL)
12# print position for the degree of freedom
13print(dof_state.pos)
```
