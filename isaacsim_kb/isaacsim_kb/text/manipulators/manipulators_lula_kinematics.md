<!-- source: manipulators/manipulators_lula_kinematics.html | title: Lula Kinematics Solver — Isaac Sim Documentation -->

# Lula Kinematics Solver
This tutorial shows how the Lula Kinematics Solver class is used to compute forward and inverse kinematics on a robot in NVIDIA Isaac Sim.

## Getting Started
Prerequisites

- Complete the Adding a Manipulator Robot tutorial prior to beginning this tutorial.

- You can reference the Lula Robot Description and XRDF Editor to understand how to generate your own robot_description.yaml file to be able to use `LulaKinematicsSolver` on unsupported robots.

- Review the Loaded Scenario Extension Template to understand how this tutorial is structured and run.

To follow along with the tutorial, you can download a standalone Lula Kinematics example extension:
Lula Kinematics Tutorial

The provided zip file contains an example of the `LulaKinematicsSolver` being used to compute forward and inverse kinematics solutions for a specified target. This tutorial explains the contents of the file `/Lula_Kinematics_python/scenario.py`, which contains all `LulaKinematicsSolver` related code.

## Using the LulaKinematicsSolver to Compute Forward and Inverse Kinematics
The Lula Kinematics Solver is able to calculate forward and inverse kinematics for a robot that is defined by two configuration files (see Lula Kinematics Solver Configuration ). The `LulaKinematicsSolver` can be paired with an Articulation Kinematics Solver to compute kinematics in a way that can be directly applied to the robot `Articulation`.
The file `/Lula_Kinematics_python/scenario.py` uses the `LulaKinematicsSolver` to generate inverse kinematic solutions to move the robot to a target.

```
1import numpy as np
2import os
3import carb
4
5from isaacsim.core.utils.extensions import get_extension_path_from_name
6from isaacsim.core.utils.stage import add_reference_to_stage
7from isaacsim.core.prims import Articulation
8from isaacsim.core.utils.nucleus import get_assets_root_path
9from isaacsim.core.prims import XFormPrim
10from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats
11
12from isaacsim.robot_motion.motion_generation import ArticulationKinematicsSolver, LulaKinematicsSolver
13from isaacsim.robot_motion.motion_generation import interface_config_loader
14
15class FrankaKinematicsExample():
16 def __init__(self):
17 self._kinematics_solver = None
18 self._articulation_kinematics_solver = None
19
20 self._articulation = None
21 self._target = None
22
23 def load_example_assets(self):
24 # Add the Franka and target to the stage
25
26 robot_prim_path = "/panda"
27 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/FrankaRobotics/FrankaPanda/franka.usd"
28
29 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
30 self._articulation = Articulation(robot_prim_path)
31
32 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", "/World/target")
33 self._target = XFormPrim("/World/target")
34 self._target.set_local_scales([0.04, 0.04, 0.04])
35 self._target.set_default_state(np.array([.3,0,.5]),euler_angles_to_quats([0,np.pi,0]))
36
37 # Return assets that were added to the stage so that they can be registered with the core.World
38 return self._articulation, self._target
39
40 def setup(self):
41 # Load a URDF and Lula Robot Description File for this robot:
42 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
43 kinematics_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
44
45 self._kinematics_solver = LulaKinematicsSolver(
46 robot_description_path = kinematics_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
47 urdf_path = kinematics_config_dir + "/franka/lula_franka_gen.urdf"
48 )
49
50 # Kinematics for supported robots can be loaded with a simpler equivalent
51 # print("Supported Robots with a Lula Kinematics Config:", interface_config_loader.get_supported_robots_with_lula_kinematics())
52 # kinematics_config = interface_config_loader.load_supported_lula_kinematics_solver_config("Franka")
53 # self._kinematics_solver = LulaKinematicsSolver(**kinematics_config)
54
55 print("Valid frame names at which to compute kinematics:", self._kinematics_solver.get_all_frame_names())
56
57 end_effector_name = "right_gripper"
58 self._articulation_kinematics_solver = ArticulationKinematicsSolver(self._articulation,self._kinematics_solver, end_effector_name)
59
60
61 def update(self, step: float):
62 target_position, target_orientation = self._target.get_world_poses()
63
64 #Track any movements of the robot base
65 robot_base_translation,robot_base_orientation = self._articulation.get_world_poses()
66 self._kinematics_solver.set_robot_base_pose(robot_base_translation,robot_base_orientation)
67
68 action, success = self._articulation_kinematics_solver.compute_inverse_kinematics(target_position, target_orientation)
69
70 if success:
71 self._articulation.apply_action(action)
72 else:
73 carb.log_warn("IK did not converge to a solution. No action is being taken")
74
75 # Unused Forward Kinematics:
76 # ee_position,ee_rot_mat = articulation_kinematics_solver.compute_end_effector_pose()
77
78 def reset(self):
79 # Kinematics is stateless
80 pass
```
The `LulaKinematicsSolver` is instantiated on lines 41-47 using file paths to the appropriate configuration files. The `LulaKinematicsSolver` uses the same robot description files as the Lula-based RMPflow Motion Policy Algorithm . The `LulaKinematicsSolver` can solve forward and inverse kinematics at any frame that exists in the robot URDF file. On line 54, the complete list of recognized frames in the Franka robot is printed:

```
Valid frame names at which to compute kinematics:
['base_link', 'panda_link0', 'panda_link1', 'panda_link2', 'panda_link3', 'panda_link4', 'panda_forearm_end_pt', 'panda_forearm_mid_pt',
'panda_forearm_mid_pt_shifted', 'panda_link5', 'panda_forearm_distal', 'panda_link6', 'panda_link7', 'panda_link8', 'panda_hand',
'camera_bottom_screw_frame', 'camera_link', 'camera_depth_frame', 'camera_color_frame', 'camera_color_optical_frame', 'camera_depth_optical_frame',
'camera_left_ir_frame', 'camera_left_ir_optical_frame', 'camera_right_ir_frame', 'camera_right_ir_optical_frame', 'panda_face_back_left',
'panda_face_back_right', 'panda_face_left', 'panda_face_right', 'panda_leftfinger', 'panda_leftfingertip', 'panda_rightfinger', 'panda_rightfingertip', 'right_gripper', 'panda_wrist_end_pt']
```
Supported robots can be loaded directly by name as on lines 50-52. This is equivalent to lines 41-47.
On line 57, an Articulation Kinematics Solver is instantiated with the Franka robot `Articulation`, the `LulaKinematicsSolver` instance, and the end effector name. The `ArticulationKinematicsSolver` class allows you to compute the end effector position and orientation for the robot `Articulation` in a single line (line 75).
The `ArticulationKinematicsSolver` also allows you to compute inverse kinematics. The current position of the robot `Articulation` is used as a warm start in the IK calculation, and the result is returned as an `ArticulationAction` that can be consumed by the robot `Articulation` to move the specified end effector frame to a target position (lines 67 and 70).
The `LulaKinematicsSolver` returns a flag marking the success or failure of the inverse kinematics computation. On line 67, the script applies the inverse kinematics solution to the robot `Articulation` only if the kinematics converged successfully to a solution, otherwise no new action is sent to the robot, and a warning is thrown. The `LulaKinematicsSolver` exposes settings that allow you to specify how quickly it terminates its search. These settings are outside the scope of this tutorial.
The `LulaKinematicsSolver` assumes that the robot base is positioned at the origin unless another location is specified. On lines 64-65, the `LulaKinematicsSolver` is given the current position of the robot base on every frame. This allows the forward and inverse kinematics to operate using world coordinates. For example, the position of the target is queried in world coordinates and passed to the `LulaKinematicsSolver`, which internally performs the necessary transformation to compute accurate inverse kinematics.
The `LulaKinematicsSolver` can be used on its own to compute forward kinematics at any position and to compute inverse kinematics with any warm start. A robot `Articulation` does not need to be present on the USD stage. See Kinematics Solvers for more details.
Additionally, sending an inverse kinematic solution directly to the robot is not likely to be useful beyond demonstrations. In a realistic scenario, you need to determine not only the end position of the robot, but also the path to get there. An IK solver on its own can make for only a rudimentary trajectory through space that is not likely to be optimal.
[image: ../_images/isim_4.5_full_tut_gui_lula_kinematics.webp]

## Summary
This tutorial reviews how to load the `LulaKinematicsSolver` class and use it alongside the `ArticulationKinematicsSolver` helper class to compute forward and inverse kinematics at any frame specified in the robot URDF file.

### Further Learning
To understand the motivation behind the structure and usage of `LulaKinematicsSolver` in NVIDIA Isaac Sim, reference the Motion Generation page.
