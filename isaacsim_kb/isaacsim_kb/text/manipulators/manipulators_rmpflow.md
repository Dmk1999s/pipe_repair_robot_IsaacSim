<!-- source: manipulators/manipulators_rmpflow.html | title: Lula RMPflow — Isaac Sim Documentation -->

# Lula RMPflow
This tutorial shows how the RMPflow class in the Motion Generation can be used to generate smooth motions to reach task-space targets while avoiding dynamic obstacles. This tutorial demonstrates how:

- `RmpFlow` can be directly instantiated and used to generate motions

- `RmpFlow` can be loaded and used on supported robots

- built-in debugging features can improve easy of use and integration

## Getting Started
Prerequisites

- Complete the Adding a Manipulator Robot tutorial prior to beginning this tutorial.

- Review the Loaded Scenario Extension Template to understand how this tutorial is structured and run.

To follow along with the tutorial, you can download a standalone RMPflow example extension here:
RMPflow Tutorial

The provided zip file provides a fully functional example of RMPflow including following a target, world awareness, and a debugging option. The sections of this tutorial build up the file `scenario.py` from basic functionality to the completed code. To follow along with this tutorial, you can download the provided extension and replace the contents of `/RmpFlow_Example_python/scenario.py` with the code snippets provided.

## Generating Motions with an RMPflow Instance
RMPflow is used heavily throughout NVIDIA Isaac Sim for controlling robot manipulators. As documented in RMPflow Configuration , there are three configuration files needed to directly instantiate the `RmpFlow` class directly. After these configuration files are loaded and an end effector target has been specified, actions can be computed to move the robot to the desired target.

```
1import numpy as np
2import os
3
4from isaacsim.core.utils.extensions import get_extension_path_from_name
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.core.prims import SingleArticulation as Articulation
7from isaacsim.core.utils.nucleus import get_assets_root_path
8from isaacsim.core.prims import SingleXFormPrim as XFormPrim
9from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
10from isaacsim.core.api.objects.cuboid import FixedCuboid
11
12from isaacsim.robot_motion.motion_generation import RmpFlow, ArticulationMotionPolicy
13
14class FrankaRmpFlowExample():
15 def __init__(self):
16 self._rmpflow = None
17 self._articulation_rmpflow = None
18
19 self._articulation = None
20 self._target = None
21
22 def load_example_assets(self):
23 # Add the Franka and target to the stage
24 # The position in which things are loaded is also the position in which they
25
26 robot_prim_path = "/panda"
27 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
28
29 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
30 self._articulation = Articulation(robot_prim_path)
31
32 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
33 self._target = XFormPrim("/World/target", scale=[.04,.04,.04])
34
35 # Return assets that were added to the stage so that they can be registered with the core.World
36 return self._articulation, self._target
37
38 def setup(self):
39 # RMPflow config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
40 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
41 rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
42
43 #Initialize an RmpFlow object
44 self._rmpflow = RmpFlow(
45 robot_description_path = rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
46 urdf_path = rmp_config_dir + "/franka/lula_franka_gen.urdf",
47 rmpflow_config_path = rmp_config_dir + "/franka/rmpflow/franka_rmpflow_common.yaml",
48 end_effector_frame_name = "right_gripper",
49 maximum_substep_size = 0.00334
50 )
51
52 #Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
53 self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation,self._rmpflow)
54
55 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
56
57 def update(self, step: float):
58 # Step is the time elapsed on this frame
59 target_position, target_orientation = self._target.get_world_pose()
60
61 self._rmpflow.set_end_effector_target(
62 target_position, target_orientation
63 )
64
65 action = self._articulation_rmpflow.get_next_articulation_action(step)
66 self._articulation.apply_action(action)
67
68 def reset(self):
69 # Rmpflow is stateless unless it is explicitly told not to be
70
71 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
```
`RMPflow` is an implementation of the Motion Policy Algorithm interface. Any MotionPolicy can be passed to an Articulation Motion Policy to start moving a robot on the USD stage. On line 43, an instance of `RmpFlow` is instantiated with the required configuration information. The `ArticulationMotionPolicy` created on line 52 acts as a translational layer between `RmpFlow` and the simulated Franka robot `Articulation`. You can interact with `RmpFlow` directly to communicate the world state, set an end effector target, or modify internal settings. On each frame, an end effector target is passed directly to the `RmpFlow` object (line 60). The `ArticulationMotionPolicy` is used on line 64 to compute an action that can be directly consumed by the Franka `Articulation`.
Note
The RMPflow algorithm takes in consideration the robot structure provided by the configuration URDF file. If working on a robot with assembled components (for example, a UR10 with a gripper attached), the URDF file should be updated to reflect the correct robot structure and contain the offset of the gripper at the end effector frame, or additional control joints. The final assembly URDF can be exported with the USD to URDF Exporter . When modifying the source URDF file, it is recommended to review and update the Robot Description file to ensure that the correct supplemental file is being used.
[image: ../_images/isim_4.5_full_tut_gui_rmpflow.webp]

### World State
As a Motion Policy Algorithm , `RmpFlow` is capable of dynamic collision avoidance while navigating the end effector to a target. The world state can be changing over time while `RmpFlow` is navigating to its target. Objects created with the `isaacsim.core.api.objects` package (see Inputs: World State ) can be registered with `RmpFlow` and the policy will automatically avoid collisions with these obstacles. `RmpFlow` is triggered to query the current state of all tracked objects whenever `RmpFlow.update_world()` is called.
`RmpFlow` can also be informed about a change in the robot base pose on a given frame by calling `RmpFlow.set_robot_base_pose()`. As object positions are queried in world coordinates, it is critical to use this function, if the base of the robot is moved within the USD stage.

```
1import numpy as np
2import os
3
4from isaacsim.core.utils.extensions import get_extension_path_from_name
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.core.prims import SingleArticulation as Articulation
7from isaacsim.core.utils.nucleus import get_assets_root_path
8from isaacsim.core.prims import SingleXFormPrim as XFormPrim
9from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
10from isaacsim.core.api.objects.cuboid import FixedCuboid
11
12from isaacsim.robot_motion.motion_generation import RmpFlow, ArticulationMotionPolicy
13
14from isaacsim.robot_motion.motion_generation.interface_config_loader import (
15 get_supported_robot_policy_pairs,
16 load_supported_motion_policy_config,
17)
18
19class FrankaRmpFlowExample():
20 def __init__(self):
21 self._rmpflow = None
22 self._articulation_rmpflow = None
23
24 self._articulation = None
25 self._target = None
26
27 def load_example_assets(self):
28 # Add the Franka and target to the stage
29 # The position in which things are loaded is also the position in which they
30
31 robot_prim_path = "/panda"
32 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
33
34 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
35 self._articulation = Articulation(robot_prim_path)
36
37 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
38 self._target = XFormPrim("/World/target", scale=[.04,.04,.04])
39
40 self._obstacle = FixedCuboid("/World/obstacle",size=.05,position=np.array([0.4, 0.0, 0.65]),color=np.array([0.,0.,1.]))
41
42 # Return assets that were added to the stage so that they can be registered with the core.World
43 return self._articulation, self._target, self._obstacle
44
45 def setup(self):
46 # RMPflow config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
47 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
48 rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
49
50 #Initialize an RmpFlow object
51 self._rmpflow = RmpFlow(
52 robot_description_path = rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
53 urdf_path = rmp_config_dir + "/franka/lula_franka_gen.urdf",
54 rmpflow_config_path = rmp_config_dir + "/franka/rmpflow/franka_rmpflow_common.yaml",
55 end_effector_frame_name = "right_gripper",
56 maximum_substep_size = 0.00334
57 )
58 self._rmpflow.add_obstacle(self._obstacle)
59
60 #Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
61 self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation,self._rmpflow)
62
63 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
64
65 def update(self, step: float):
66 # Step is the time elapsed on this frame
67 target_position, target_orientation = self._target.get_world_pose()
68
69 self._rmpflow.set_end_effector_target(
70 target_position, target_orientation
71 )
72
73 # Track any movements of the cube obstacle
74 self._rmpflow.update_world()
75
76 #Track any movements of the robot base
77 robot_base_translation,robot_base_orientation = self._articulation.get_world_pose()
78 self._rmpflow.set_robot_base_pose(robot_base_translation,robot_base_orientation)
79
80 action = self._articulation_rmpflow.get_next_articulation_action(step)
81 self._articulation.apply_action(action)
82
83 def reset(self):
84 # Rmpflow is stateless unless it is explicitly told not to be
85
86 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
```
On lines 22, an obstacle is added to the stage, and on line 40, it is registered as an obstacle with `RmpFlow`. On each frame, `RmpFlow.update_world()` is called (line 56). This triggers `RmpFlow` to query the current position of the cube to account for any movement.
On lines 59-60, the current position of the robot base is queried and passed to `RmpFlow`. This step is separated from other world state because it is often unnecessary (when the robot base never moves from the origin), or this step might require extra consideration (for example, `RmpFlow` is controlling an arm that is mounted on a moving base).

## Loading RMPflow for Supported Robots
In the previous sections, observe that `RmpFlow` requires five arguments to be initialized. Three of these arguments are file paths to required configuration files. The `end_effector_frame_name` argument specifies what frame on the robot (from the frames found in the referenced URDF file) should be considered the end effector. The `maximum_substep_size` argument specifies a maximum step-size when internally performing the Euler Integration.
For manipulators in the NVIDIA Isaac Sim library, appropriate config information for loading RmpFlow can be found in the `isaacsim.robot_motion.motion_generation` extension. This information is indexed by robot name and can be accessed simply. The following change shows how loading configs for supported robots can be simplified.

```
1import numpy as np
2import os
3
4from isaacsim.core.utils.extensions import get_extension_path_from_name
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.core.prims import SingleArticulation as Articulation
7from isaacsim.core.utils.nucleus import get_assets_root_path
8from isaacsim.core.prims import SingleXFormPrim as XFormPrim
9from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
10from isaacsim.core.api.objects.cuboid import FixedCuboid
11
12from isaacsim.robot_motion.motion_generation import RmpFlow, ArticulationMotionPolicy
13
14from isaacsim.robot_motion.motion_generation.interface_config_loader import (
15 get_supported_robot_policy_pairs,
16 load_supported_motion_policy_config,
17)
18
19class FrankaRmpFlowExample():
20 def __init__(self):
21 self._rmpflow = None
22 self._articulation_rmpflow = None
23
24 self._articulation = None
25 self._target = None
26
27 def load_example_assets(self):
28 # Add the Franka and target to the stage
29 # The position in which things are loaded is also the position in which they
30
31 robot_prim_path = "/panda"
32 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
33
34 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
35 self._articulation = Articulation(robot_prim_path)
36
37 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
38 self._target = XFormPrim("/World/target", scale=[.04,.04,.04])
39
40 self._obstacle = FixedCuboid("/World/obstacle",size=.05,position=np.array([0.4, 0.0, 0.65]),color=np.array([0.,0.,1.]))
41
42 # Return assets that were added to the stage so that they can be registered with the core.World
43 return self._articulation, self._target, self._obstacle
44
45 def setup(self):
46 # Loading RMPflow can be done quickly for supported robots
47 print("Supported Robots with a Provided RMPflow Config:", list(get_supported_robot_policy_pairs().keys()))
48 rmp_config = load_supported_motion_policy_config("Franka","RMPflow")
49
50 #Initialize an RmpFlow object
51 self._rmpflow = RmpFlow(**rmp_config)
52 self._rmpflow.add_obstacle(self._obstacle)
53
54 #Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
55 self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation,self._rmpflow)
56
57 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
58
59 def update(self, step: float):
60 # Step is the time elapsed on this frame
61 target_position, target_orientation = self._target.get_world_pose()
62
63 self._rmpflow.set_end_effector_target(
64 target_position, target_orientation
65 )
66
67 # Track any movements of the cube obstacle
68 self._rmpflow.update_world()
69
70 #Track any movements of the robot base
71 robot_base_translation,robot_base_orientation = self._articulation.get_world_pose()
72 self._rmpflow.set_robot_base_pose(robot_base_translation,robot_base_orientation)
73
74 action = self._articulation_rmpflow.get_next_articulation_action(step)
75 self._articulation.apply_action(action)
76
77 def reset(self):
78 # Rmpflow is stateless unless it is explicitly told not to be
79
80 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
```
A supported set of robots can have their RMPflow configs loaded by name. Line 34 prints the names of every supported robot with a provided RMPflow config (at the time of writing this tutorial):
[‘Franka’, ‘UR3’, ‘UR3e’, ‘UR5’, ‘UR5e’, ‘UR10’, ‘UR10e’, ‘UR16e’, ‘Rizon4’, ‘Cobotta_Pro_900’, ‘Cobotta_Pro_1300’, ‘RS007L’, ‘RS007N’, ‘RS013N’, ‘RS025N’, ‘RS080N’, ‘FestoCobot’, ‘Techman_TM12’, ‘Kuka_KR210’, ‘Fanuc_CRX10IAL’]

On lines 35,38, the RmpFlow class initializer is simplified to unpacking a dictionary of loaded keyword arguments. The `load_supported_motion_policy_config()` function is the simplest way to load supported robots.

## Debugging Features
The `RmpFlow` class has contains debugging features that are not generally available in the Motion Policy Algorithm interface. These debugging features allow decoupling of the simulator from the RmpFlow algorithm to help diagnose any undesirable behaviors that are encountered (RMPflow Debugging Features ).
`RmpFlow` uses collision spheres internally to avoid collisions with external objects. These spheres can be visualized with the `RmpFlow.visualize_collision_spheres()` function. This helps to determine whether `RmpFlow` has a reasonable representation of the simulated robot.
The visualization can be used alongside a flag `RmpFlow.set_ignore_state_updates(True)` to ignore state updates from the robot `Articulation` and instead assume that robot joint targets returned by `RmpFlow` are always perfectly achieved. This causes `RmpFlow` to compute a robot path over time that is independent of the simulated robot `Articulation`. At each timestep, `RmpFlow` returns joint targets that are passed to the robot `Articulation`.

```
1import numpy as np
2import os
3
4from isaacsim.core.utils.extensions import get_extension_path_from_name
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.core.prims import SingleArticulation as Articulation
7from isaacsim.core.utils.nucleus import get_assets_root_path
8from isaacsim.core.prims import SingleXFormPrim as XFormPrim
9from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
10from isaacsim.core.api.objects.cuboid import FixedCuboid
11
12from isaacsim.robot_motion.motion_generation import RmpFlow, ArticulationMotionPolicy
13
14from isaacsim.robot_motion.motion_generation.interface_config_loader import (
15 get_supported_robot_policy_pairs,
16 load_supported_motion_policy_config,
17)
18
19class FrankaRmpFlowExample():
20 def __init__(self):
21 self._rmpflow = None
22 self._articulation_rmpflow = None
23
24 self._articulation = None
25 self._target = None
26
27 self._dbg_mode = True
28
29 def load_example_assets(self):
30 # Add the Franka and target to the stage
31 # The position in which things are loaded is also the position in which they
32
33 robot_prim_path = "/panda"
34 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
35
36 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
37 self._articulation = Articulation(robot_prim_path)
38
39 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
40 self._target = XFormPrim("/World/target", scale=[.04,.04,.04])
41
42 self._obstacle = FixedCuboid("/World/obstacle",size=.05,position=np.array([0.4, 0.0, 0.65]),color=np.array([0.,0.,1.]))
43
44 # Return assets that were added to the stage so that they can be registered with the core.World
45 return self._articulation, self._target, self._obstacle
46
47 def setup(self):
48 # Loading RMPflow can be done quickly for supported robots
49 print("Supported Robots with a Provided RMPflow Config:", list(get_supported_robot_policy_pairs().keys()))
50 rmp_config = load_supported_motion_policy_config("Franka","RMPflow")
51
52 #Initialize an RmpFlow object
53 self._rmpflow = RmpFlow(**rmp_config)
54 self._rmpflow.add_obstacle(self._obstacle)
55
56 if self._dbg_mode:
57 self._rmpflow.set_ignore_state_updates(True)
58 self._rmpflow.visualize_collision_spheres()
59
60 # Set the robot gains to be deliberately poor
61 bad_proportional_gains = self._articulation.get_articulation_controller().get_gains()[0]/50
62 self._articulation.get_articulation_controller().set_gains(kps = bad_proportional_gains)
63
64 #Use the ArticulationMotionPolicy wrapper object to connect rmpflow to the Franka robot articulation.
65 self._articulation_rmpflow = ArticulationMotionPolicy(self._articulation,self._rmpflow)
66
67 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
68
69 def update(self, step: float):
70 # Step is the time elapsed on this frame
71 target_position, target_orientation = self._target.get_world_pose()
72
73 self._rmpflow.set_end_effector_target(
74 target_position, target_orientation
75 )
76
77 # Track any movements of the cube obstacle
78 self._rmpflow.update_world()
79
80 #Track any movements of the robot base
81 robot_base_translation,robot_base_orientation = self._articulation.get_world_pose()
82 self._rmpflow.set_robot_base_pose(robot_base_translation,robot_base_orientation)
83
84 action = self._articulation_rmpflow.get_next_articulation_action(step)
85 self._articulation.apply_action(action)
86
87 def reset(self):
88 # Rmpflow is stateless unless it is explicitly told not to be
89 if self._dbg_mode:
90 # RMPflow was set to roll out robot state internally, assuming that all returned joint targets were hit exactly.
91 self._rmpflow.reset()
92 self._rmpflow.visualize_collision_spheres()
93
94 self._target.set_world_pose(np.array([.5,0,.7]),euler_angles_to_quats([0,np.pi,0]))
```
The collision sphere visualization can be very helpful to distinguish between behaviors that are coming from the simulator, and behaviors that are coming from `RmpFlow`. In the video below, the Franka robot is given weak proportional gains (lines 43-44). Using the debugging visualization, it is easy to determine that RmpFlow is producing reasonable motions, but the simulated robot is simply not able to follow the motions. When RMPflow moves the robot quickly, the Franka robot `Articulation` lags significantly behind the commanded position.

## Summary
This tutorial reviews using the `RmpFlow` class to generate reactive motions in response to a dynamic environment. The `RmpFlow` class can be used to generate motions directly alongside an Articulation Motion Policy .
This tutorial reviewed four of the main features of `RmpFlow`:

- Navigating the robot through an environment to a target position and orientation.

- Adapting to a dynamic world on every frame.

- Adapting to a change in the robot’s position on the USD stage.

- Using visualization to decouple the simulated robot `Articulation` from the RMPflow algorithm for quick and easy debugging.

### Further Learning
To learn how to configure RMPflow for a new robot, review the basic formalism , and then read the RMPflow tuning guide for practical advice.
To understand the motivation behind the structure and usage of `RmpFlow` in NVIDIA Isaac Sim, reference the Motion Generation page.
