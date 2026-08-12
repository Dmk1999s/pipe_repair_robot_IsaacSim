<!-- source: manipulators/manipulators_lula_rrt.html | title: Lula RRT — Isaac Sim Documentation -->

# Lula RRT
This tutorial shows how the Lula RRT class in the Motion Generation extension can be used to produce a collision free path from a starting configuration space (c-space) position to a c-space or task-space target.

## Getting Started
Prerequisites

- Complete the Adding a Manipulator Robot tutorial prior to beginning this tutorial.

- You can reference the Lula Robot Description Editor to understand how to generate your own robot_description.yaml file to be able to use RRT on unsupported robots.

- Review the Loaded Scenario Extension Template to understand how this tutorial is structured and run.

To follow along with the tutorial, you can download a standalone RRT example extension:
RRT Tutorial

The provided zip file contains a fully functional example of RRT being used to plan to a task-space target. This tutorial explains the contents of the file /RRT_Example_python/scenario.py, which contains all `RRT` related code.

## Generating a Path Using an RRT Instance

### Required Configuration Files
Lula RRT requires three configuration files to identify a specific robot in Lula RRT Configuration . Paths to these configuration files are used to initialize the `RRT` class along with an end effector name matching a frame in the robot URDF.
One of the required files contains parameters for the RRT algorithm specifically, and is not shared with any other Lula algorithms. This tutorial loads the following RRT config file for the Franka robot:

```
1seed: 123456
2step_size: 0.05
3max_iterations: 50000
4max_sampling: 10000
5distance_metric_weights: [3.0, 2.0, 2.0, 1.5, 1.5, 1.0, 1.0]
6task_space_frame_name: "panda_rightfingertip"
7task_space_limits: [[0.0, 0.7], [-0.6, 0.6], [0.0, 0.8]]
8cuda_tree_params:
9 max_num_nodes: 10000
10 max_buffer_size: 30
11 num_nodes_cpu_gpu_crossover: 3000
12c_space_planning_params:
13 exploration_fraction: 0.5
14task_space_planning_params:
15 translation_target_zone_tolerance: 0.05
16 orientation_target_zone_tolerance: 0.09
17 translation_target_final_tolerance: 1e-4
18 orientation_target_final_tolerance: 0.005
19 translation_gradient_weight: 1.0
20 orientation_gradient_weight: 0.125
21 nn_translation_distance_weight: 1.0
22 nn_orientation_distance_weight: 0.125
23 task_space_exploitation_fraction: 0.4
24 task_space_exploration_fraction: 0.1
25 max_extension_substeps_away_from_target: 6
26 max_extension_substeps_near_target: 50
27 extension_substep_target_region_scale_factor: 2.0
28 unexploited_nodes_culling_scalar: 1.0
29 gradient_substep_size: 0.025
```
You can reference the `docstring` to the function `RRT.set_param()` in our API Documentation for a description of each parameter.

### RRT Example
The file `/RRT_Example_python/scenario.py` loads the Franka robot and uses `RRT` to move it around obstacles to a target. Every 60 frames, the planner replans to move to the current target position (if possible). In this example, the planner does not attempt to plan to the same target multiple times if a failure is encountered. The returned plan will be `None` and no actions will be taken.

```
1import numpy as np
2import os
3
4from isaacsim.core.utils.extensions import get_extension_path_from_name
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.core.prims import Articulation
7from isaacsim.core.utils.nucleus import get_assets_root_path
8from isaacsim.core.api.objects.cuboid import VisualCuboid
9from isaacsim.core.prims import XFormPrim
10from isaacsim.core.utils.numpy.rotations import euler_angles_to_quats, quats_to_rot_matrices
11from isaacsim.core.utils.distance_metrics import rotational_distance_angle
12
13from isaacsim.robot_motion.motion_generation import PathPlannerVisualizer
14from isaacsim.robot_motion.motion_generation.lula import RRT
15from isaacsim.robot_motion.motion_generation import interface_config_loader
16
17class FrankaRrtExample():
18 def __init__(self):
19 self._rrt = None
20 self._path_planner_visualizer = None
21 self._plan = []
22
23 self._articulation = None
24 self._target = None
25 self._target_position = None
26
27 self._frame_counter = 0
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
41 self._target.set_default_state(np.array([.45, .5, .7]),euler_angles_to_quats([3*np.pi/4, 0, np.pi]))
42
43 self._obstacle = VisualCuboid("/World/Wall", position = np.array([.3,.6,.6]), size = 1.0, scale = np.array([.1,.4,.4]))
44
45 # Return assets that were added to the stage so that they can be registered with the core.World
46 return self._articulation, self._target
47
48 def setup(self):
49 # Lula config files for supported robots are stored in the motion_generation extension under
50 # "/path_planner_configs" and "/motion_policy_configs"
51 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
52 rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
53 rrt_config_dir = os.path.join(mg_extension_path, "path_planner_configs")
54
55 #Initialize an RRT object
56 self._rrt = RRT(
57 robot_description_path = rmp_config_dir + "/franka/rmpflow/robot_descriptor.yaml",
58 urdf_path = rmp_config_dir + "/franka/lula_franka_gen.urdf",
59 rrt_config_path = rrt_config_dir + "/franka/rrt/franka_planner_config.yaml",
60 end_effector_frame_name = "right_gripper"
61 )
62
63 # RRT for supported robots can also be loaded with a simpler equivalent:
64 # rrt_config = interface_config_loader.load_supported_path_planner_config("Franka", "RRT")
65 # self._rrt = RRT(**rrt_confg)
66
67 self._rrt.add_obstacle(self._obstacle)
68
69 # Set the maximum number of iterations of RRT to prevent it from blocking Isaac Sim for
70 # too long.
71 self._rrt.set_max_iterations(5000)
72
73 # Use the PathPlannerVisualizer wrapper to generate a trajectory of ArticulationActions
74 self._path_planner_visualizer = PathPlannerVisualizer(self._articulation, self._rrt)
75
76 self.reset()
77
78 def update(self, step: float):
79 current_target_translation, current_target_orientation = self._target.get_world_pose()
80 current_target_rotation = quats_to_rot_matrices(current_target_orientation)
81
82 translation_distance = np.linalg.norm(self._target_translation - current_target_translation)
83 rotation_distance = rotational_distance_angle(current_target_rotation, self._target_rotation)
84 target_moved = translation_distance > 0.01 or rotation_distance > 0.01
85
86 if (self._frame_counter % 60 == 0 and target_moved):
87 # Replan every 60 frames if the target has moved
88 self._rrt.set_end_effector_target(current_target_translation, current_target_orientation)
89 self._rrt.update_world()
90 self._plan = self._path_planner_visualizer.compute_plan_as_articulation_actions(max_cspace_dist=.01)
91
92 self._target_translation = current_target_translation
93 self._target_rotation = current_target_rotation
94
95 if self._plan:
96 action = self._plan.pop(0)
97 self._articulation.apply_action(action)
98
99 self._frame_counter += 1
100
101 def reset(self):
102 self._target_translation = np.zeros(3)
103 self._target_rotation = np.eye(3)
104 self._frame_counter = 0
105 self._plan = []
```
The `RRT` class is initialized on lines 51-61. For supported robots, this can be simplified as on lines 63-65. `RRT` is made aware of the obstacle it needs to watch on line 67. Any time `RRT.update_world()` is called (line 89), it will query the current position of watched obstacles.
`RRT` outputs sparse plans that, when linearly interpolated, form a collision-free path to the goal position. As an instance of the `PathPlanner` interface, `RRT` can be passed to a Path Planner Visualizer to convert its output to a form that is directly usable by the robot `Articulation` (line 74).
In this example, `RRT` replans every second if the target has been moved. The replanning is performed on lines 88-90.

- First, `RRT` is informed of the new target position.

- Then it is told to query the position of watched obstacles.

- Finally, the `path_planner_visualizer` wrapping `RRT` is used to generate a plan in the form of a list of `ArticulationAction`.

The `max_cspace_dist` argument passed to the `path_planner_visualizer` interpolates the sparse output with a maximum l2 norm of `.01` between any two commanded robot positions. On every frame, one of the actions in the plan is removed from the plan and sent to the robot (lines 92-93).
[image: ../_images/isim_4.5_full_tut_gui_rrt.webp]

## Current Limitations

### Following a Plan with Exactness
The `PathPlannerVisualizer` class is called a “Visualizer” because it is only meant to give a visualization of an output plan, but it is not likely to be useful beyond this. By densely linearly interpolating an `RRT` plan, the resulting trajectory is far from time-optimal or smooth. To follow a plan in a more theoretically sound way, the output of `RRT` can be combined with the `LulaTrajectoryGenerator`. This is demonstrated in the NVIDIA Isaac Sim Path Planning Example in the Robotics Examples tab. You can activate Robotics Examples tab from Windows > Examples > Robotics Examples.

## Summary
This tutorial reviews using the `RRT` class to generate a collision-free path through an environment from a starting position to a task-space target.

### Further Learning
To understand the motivation behind the structure and usage of `RRT` in NVIDIA Isaac Sim, reference the Motion Generation page.
