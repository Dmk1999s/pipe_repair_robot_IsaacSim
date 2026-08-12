<!-- source: manipulators/manipulators_lula_trajectory_generator.html | title: Lula Trajectory Generator — Isaac Sim Documentation -->

# Lula Trajectory Generator
This tutorial explores how the Lula Trajectory Generator in the Motion Generation extension can be used to create both task-space and c-space trajectories that can be easily applied to a simulated robot `Articulation`.

## Getting Started
Prerequisites

- Complete the Adding a Manipulator Robot tutorial prior to beginning this tutorial.

- You can reference the Lula Robot Description and XRDF Editor to understand how to generate your own `robot_description.yaml` file to be able to use the Lula Trajectory Generator on unsupported robots.

- Review the Loaded Scenario Extension Template to understand how this tutorial is structured and run.

To follow along with the tutorial, you can download a standalone Lula Trajectory Generator example extension here:
Lula Trajectory Generator Tutorial

The provided zip file contains an example of the `LulaTaskSpaceTrajectorygenerator` and `LulaCSpaceTrajectoryGenerator` being used to generate trajectories connecting specified c-space and task-space points. This tutorial explains the contents of the file `/Trajectory_Generator_python/scenario.py`, which contains all trajectory generation code.
[image: ../_images/isim_4.5_full_tut_gui_lula_trajectory_gen.webp]

## Generating a C-Space Trajectory
The `LulaCSpaceTrajectoryGenerator` class is able to generate a trajectory that connects a provided set of c-space waypoints. The code snippet below demonstrates how, given appropriate config files, the `LulaCSpaceTrajectoryGenerator` class can be initialized and used to create a sequence of `ArticulationAction` that can be set on each frame to produce the desired trajectory.
The code snippet below shows the relevant contents of `/Trajectory_Generator_python/scenario.py` from the provided example.

```
1import numpy as np
2import os
3
4import carb
5from isaacsim.core.utils.extensions import get_extension_path_from_name
6from isaacsim.core.utils.stage import add_reference_to_stage
7from isaacsim.core.prims import Articulation
8from isaacsim.core.utils.nucleus import get_assets_root_path
9from isaacsim.core.api.objects.cuboid import FixedCuboid
10from isaacsim.core.prims import XFormPrim
11from isaacsim.core.utils.numpy.rotations import rot_matrices_to_quats
12from isaacsim.core.utils.prims import delete_prim, get_prim_at_path
13
14from isaacsim.robot_motion.motion_generation import (
15 LulaCSpaceTrajectoryGenerator,
16 LulaTaskSpaceTrajectoryGenerator,
17 LulaKinematicsSolver,
18 ArticulationTrajectory
19)
20
21import lula
22
23class UR10TrajectoryGenerationExample():
24 def __init__(self):
25 self._c_space_trajectory_generator = None
26 self._taskspace_trajectory_generator = None
27 self._kinematics_solver = None
28
29 self._action_sequence = []
30 self._action_sequence_index = 0
31
32 self._articulation = None
33
34 def load_example_assets(self):
35 # Add the Franka and target to the stage
36 # The position in which things are loaded is also the position in which they
37
38 robot_prim_path = "/ur10"
39 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"
40
41 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
42 self._articulation = Articulation(robot_prim_path)
43
44 # Return assets that were added to the stage so that they can be registered with the core.World
45 return [self._articulation]
46
47 def setup(self):
48 # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
49 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
50 rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
51
52 #Initialize a LulaCSpaceTrajectoryGenerator object
53 self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
54 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
55 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
56 )
57
58 self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
59 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
60 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
61 )
62
63 self._kinematics_solver = LulaKinematicsSolver(
64 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
65 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
66 )
67
68 self._end_effector_name = "ee_link"
69
70 def setup_cspace_trajectory(self):
71 c_space_points = np.array([
72 [-0.41 , 0.5 , -2.36 , -1.28 , 5.13 , -4.71 , ],
73 [-1.43 , 1.0 , -2.58 , -1.53 , 6.0 , -4.74 , ],
74 [-2.83 , 0.34 , -2.11 , -1.38 , 1.26 , -4.71 , ],
75 [-0.41 , 0.5 , -2.36 , -1.28 , 5.13 , -4.71 , ]
76 ])
77
78 timestamps = np.array([0,5,10,13])
79
80 trajectory_time_optimal = self._c_space_trajectory_generator.compute_c_space_trajectory(c_space_points)
81 trajectory_timestamped = self._c_space_trajectory_generator.compute_timestamped_c_space_trajectory(c_space_points,timestamps)
82
83 # Visualize c-space targets in task space
84 for i,point in enumerate(c_space_points):
85 position,rotation = self._kinematics_solver.compute_forward_kinematics(self._end_effector_name, point)
86 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}")
87 frame = XFormPrim(f"/visualized_frames/target_{i}",scale=[.04,.04,.04])
88 frame.set_world_pose(position,rot_matrices_to_quats(rotation))
89
90 if trajectory_time_optimal is None or trajectory_timestamped is None:
91 carb.log_warn("No trajectory could be computed")
92 self._action_sequence = []
93 else:
94 physics_dt = 1/60
95 self._action_sequence = []
96
97 # Follow both trajectories in a row
98
99 articulation_trajectory_time_optimal = ArticulationTrajectory(self._articulation, trajectory_time_optimal, physics_dt)
100 self._action_sequence.extend(articulation_trajectory_time_optimal.get_action_sequence())
101
102 articulation_trajectory_timestamped = ArticulationTrajectory(self._articulation, trajectory_timestamped, physics_dt)
103 self._action_sequence.extend(articulation_trajectory_timestamped.get_action_sequence())
104
105 def update(self, step: float):
106 if len(self._action_sequence) == 0:
107 return
108
109 if self._action_sequence_index >= len(self._action_sequence):
110 self._action_sequence_index += 1
111 self._action_sequence_index %= len(self._action_sequence) + 10 # Wait 10 frames before repeating trajectories
112 return
113
114 if self._action_sequence_index == 0:
115 self._teleport_robot_to_position(self._action_sequence[0])
116
117 self._articulation.apply_action(self._action_sequence[self._action_sequence_index])
118
119 self._action_sequence_index += 1
120 self._action_sequence_index %= len(self._action_sequence) + 10 # Wait 10 frames before repeating trajectories
121
122 def reset(self):
123 # Delete any visualized frames
124 if get_prim_at_path("/visualized_frames"):
125 delete_prim("/visualized_frames")
126
127 self._action_sequence = []
128 self._action_sequence_index = 0
129
130 def _teleport_robot_to_position(self, articulation_action):
131 initial_positions = np.zeros(self._articulation.num_dof)
132 initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions
133
134 self._articulation.set_joint_positions(initial_positions)
135 self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```
On lines 53-56, the `LulaCSpaceTrajectoryGenerator` class is initialized using a URDF and Lula Robot Description File . The `LulaCSpaceTrajectoryGenerator` takes in a series of waypoints, and it connects them in configuration space using spline-based interpolation. There are two main objectives that can be fulfilled by the trajectory generator:

- time-optimal

- time-stamped

The provided example shows a trajectory that runs quickly, and then runs slowly. This is seen in the code on lines (80-81 and 99-103). On line 80, a time-optimal trajectory is created in the form of a `LulaTrajectory` object, which fulfills the Trajectory Interface . On line 81, a time-stamped trajectory is created that will hit the same waypoints at the times `[0,5,10,13]` seconds (line 78). Time optimality is defined as saturating at least one of velocity, acceleration, or jerk limits of the robot throughout a trajectory.
On lines 99-103, These `LulaTrajectory` objects are passed to `ArticulationTrajectory` to generate a sequence of `ArticulationAction` that can be passed directly to the robot `Articulation`. The function `ArticulationTrajectory.get_action_sequence()` returns a list of `ArticulationAction` that is meant to be consumed at the specified rate. In this case, the framerate of physics is assumed to be fixed at `1/60` seconds.
If no trajectory can be computed that connects the c-space waypoints, the trajectory returned by `LulaCSpaceTrajectoryGenerator.compute_c_space_trajectory` will be `None`. This can occur when one of the specified c-space waypoints is not reachable or is very close to a joint limit. This case is handled on lines 90-92.
On lines 84-88, a visualization of the original `c_space_points` is created by converting them to task-space points. This code is not functional, but it helps to verify that the robot is hitting every target.
The `update()` function is programmed to play the sequence of `ArticulationActions` in a loop, taking a pause of `10 frames` for dramatic effect between trajectories.

## Generating a Task-Space Trajectory

### Simple Case: Linearly Connecting Waypoints
Generating a task-space trajectory is similar to generating a c-space trajectory. In the simplest use-case, you can pass in a set of task-space position and quaternion orientation targets, which will be linearly interpolated in task-space to produce the resulting trajectory. An example is provided in the code snippet below:

```
1class UR10TrajectoryGenerationExample():
2 def __init__(self):
3 self._c_space_trajectory_generator = None
4 self._taskspace_trajectory_generator = None
5 self._kinematics_solver = None
6
7 self._action_sequence = []
8 self._action_sequence_index = 0
9
10 self._articulation = None
11
12 def load_example_assets(self):
13 # Add the Franka and target to the stage
14 # The position in which things are loaded is also the position in which they
15
16 robot_prim_path = "/ur10"
17 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"
18
19 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
20 self._articulation = Articulation(robot_prim_path)
21
22 # Return assets that were added to the stage so that they can be registered with the core.World
23 return [self._articulation]
24
25 def setup(self):
26 # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
27 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
28 rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
29
30 #Initialize a LulaCSpaceTrajectoryGenerator object
31 self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
32 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
33 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
34 )
35
36 self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
37 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
38 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
39 )
40
41 self._kinematics_solver = LulaKinematicsSolver(
42 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
43 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
44 )
45
46 self._end_effector_name = "ee_link"
47
48 def setup_taskspace_trajectory(self):
49 task_space_position_targets = np.array([
50 [0.3, -0.3, 0.1],
51 [0.3, 0.3, 0.1],
52 [0.3, 0.3, 0.5],
53 [0.3, -0.3, 0.5],
54 [0.3, -0.3, 0.1]
55 ])
56
57 task_space_orientation_targets = np.tile(np.array([0,1,0,0]),(5,1))
58
59 trajectory = self._taskspace_trajectory_generator.compute_task_space_trajectory_from_points(
60 task_space_position_targets, task_space_orientation_targets, self._end_effector_name
61 )
62
63 # Visualize task-space targets in task space
64 for i,(position,orientation) in enumerate(zip(task_space_position_targets,task_space_orientation_targets)):
65 add_reference_to_stage(get_assets_root_path() + "/Isaac/Props/UIElements/frame_prim.usd", f"/visualized_frames/target_{i}")
66 frame = XFormPrim(f"/visualized_frames/target_{i}",scale=[.04,.04,.04])
67 frame.set_world_pose(position,orientation)
68
69 if trajectory is None:
70 carb.log_warn("No trajectory could be computed")
71 self._action_sequence = []
72 else:
73 physics_dt = 1/60
74 articulation_trajectory = ArticulationTrajectory(self._articulation, trajectory, physics_dt)
75
76 # Get a sequence of ArticulationActions that are intended to be passed to the robot at 1/60 second intervals
77 self._action_sequence = articulation_trajectory.get_action_sequence()
78
79 def update(self, step: float):
80 if len(self._action_sequence) == 0:
81 return
82
83 if self._action_sequence_index >= len(self._action_sequence):
84 self._action_sequence_index += 1
85 self._action_sequence_index %= len(self._action_sequence) + 10 # Wait 10 frames before repeating trajectories
86 return
87
88 if self._action_sequence_index == 0:
89 self._teleport_robot_to_position(self._action_sequence[0])
90
91 self._articulation.apply_action(self._action_sequence[self._action_sequence_index])
92
93 self._action_sequence_index += 1
94 self._action_sequence_index %= len(self._action_sequence) + 10 # Wait 10 frames before repeating trajectories
95
96 def reset(self):
97 # Delete any visualized frames
98 if get_prim_at_path("/visualized_frames"):
99 delete_prim("/visualized_frames")
100
101 self._action_sequence = []
102 self._action_sequence_index = 0
103
104 def _teleport_robot_to_position(self, articulation_action):
105 initial_positions = np.zeros(self._articulation.num_dof)
106 initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions
107
108 self._articulation.set_joint_positions(initial_positions)
109 self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```
In moving to the task-space trajectory generator, there are few code changes required. The initialization is nearly the same on line 36 as for the c-space trajectory generator. The main changes are on lines 59-61 where a task-space trajectory is specified. When using the function `LulaTaskSpaceTrajectoryGenerator.compute_task_space_trajectory_from_points`, a position and orientation target must be specified for each task-space waypoint. Additionally, a frame from the robot URDF must be specified as the end effector frame. If the waypoints cannot be connected to form a trajectory, the `compute_task_space_trajectory_from_points` function will return `None`. This case is checked on line 69.

### Defining Complicated Trajectories
The `LulaTaskSpaceTrajectoryGenerator` can be used to create paths with more complicated specifications than to connect a set of task-space targets linearly. Using the class `lula.TaskSpacePathSpec`, you can define paths with arcs and circles with multiple options for orientation targets. The code snippet below demonstrates creating a `lula.TaskSpacePathSpec` and gives an example of each available function for adding to a task-space path. Additionally, it shows how a `lula.TaskSpacePathSpec` can be combined with a `lula.CSpacePathSpec` in a `lula.CompositePathSpec` to specify trajectories that contain both c-space and task-space waypoints.

```
1class UR10TrajectoryGenerationExample():
2 def __init__(self):
3 self._c_space_trajectory_generator = None
4 self._taskspace_trajectory_generator = None
5 self._kinematics_solver = None
6
7 self._action_sequence = []
8 self._action_sequence_index = 0
9
10 self._articulation = None
11
12 def load_example_assets(self):
13 # Add the Franka and target to the stage
14 # The position in which things are loaded is also the position in which they
15
16 robot_prim_path = "/ur10"
17 path_to_robot_usd = get_assets_root_path() + "/Isaac/Robots/UniversalRobots/ur10/ur10.usd"
18
19 add_reference_to_stage(path_to_robot_usd, robot_prim_path)
20 self._articulation = Articulation(robot_prim_path)
21
22 # Return assets that were added to the stage so that they can be registered with the core.World
23 return [self._articulation]
24
25 def setup(self):
26 # Config files for supported robots are stored in the motion_generation extension under "/motion_policy_configs"
27 mg_extension_path = get_extension_path_from_name("isaacsim.robot_motion.motion_generation")
28 rmp_config_dir = os.path.join(mg_extension_path, "motion_policy_configs")
29
30 #Initialize a LulaCSpaceTrajectoryGenerator object
31 self._c_space_trajectory_generator = LulaCSpaceTrajectoryGenerator(
32 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
33 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
34 )
35
36 self._taskspace_trajectory_generator = LulaTaskSpaceTrajectoryGenerator(
37 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
38 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
39 )
40
41 self._kinematics_solver = LulaKinematicsSolver(
42 robot_description_path = rmp_config_dir + "/universal_robots/ur10/rmpflow/ur10_robot_description.yaml",
43 urdf_path = rmp_config_dir + "/universal_robots/ur10/ur10_robot.urdf"
44 )
45
46 self._end_effector_name = "ee_link"
47
48 def setup_advanced_trajectory(self):
49 # The following code demonstrates how to specify a complicated cspace and taskspace path
50 # using the lula.CompositePathSpec object
51
52 initial_c_space_robot_pose = np.array([0,0,0,0,0,0])
53
54 # Combine a cspace and taskspace trajectory
55 composite_path_spec = lula.create_composite_path_spec(initial_c_space_robot_pose)
56
57 #############################################################################
58 # Demonstrate all the available movements in a taskspace path spec:
59
60 #Lula has its own classes for Rotations and 6 DOF poses: Rotation3 and Pose3
61 r0 = lula.Rotation3(np.pi/2, np.array([1.0, 0.0, 0.0]))
62 t0 = np.array([.3,-.1,.3])
63 task_space_spec = lula.create_task_space_path_spec(lula.Pose3(r0,t0))
64
65 # Add path linearly interpolating between r0,r1 and t0,t1
66 t1 = np.array([.3,-.1,.5])
67 r1 = lula.Rotation3(np.pi/3,np.array([1,0,0]))
68 task_space_spec.add_linear_path(lula.Pose3(r1, t1))
69
70 # Add pure translation. Constant rotation is assumed
71 task_space_spec.add_translation(t0)
72
73 # Add pure rotation.
74 task_space_spec.add_rotation(r0)
75
76 # Add three-point arc with constant orientation.
77 t2 = np.array([.3,.3,.3,])
78 midpoint = np.array([.3,0,.5])
79 task_space_spec.add_three_point_arc(t2, midpoint, constant_orientation=True)
80
81 # Add three-point arc with tangent orientation.
82 task_space_spec.add_three_point_arc(t0, midpoint, constant_orientation=False)
83
84 # Add three-point arc with orientation target.
85 task_space_spec.add_three_point_arc_with_orientation_target(lula.Pose3(r1, t2), midpoint)
86
87 # Add tangent arc with constant orientation. Tangent arcs are circles that connect two points
88 task_space_spec.add_tangent_arc(t0, constant_orientation=True)
89
90 # Add tangent arc with tangent orientation.
91 task_space_spec.add_tangent_arc(t2, constant_orientation=False)
92
93 # Add tangent arc with orientation target.
94 task_space_spec.add_tangent_arc_with_orientation_target(lula.Pose3(r0, t0))
95
96
97 ###################################################
98 # Demonstrate the usage of a c_space path spec:
99 c_space_spec = lula.create_c_space_path_spec(np.array([0,0,0,0,0,0]))
100
101 c_space_spec.add_c_space_waypoint(np.array([0 , 0.5 , -2.0 , -1.28 , 5.13 , -4.71]))
102
103
104 ##############################################################
105 #Combine the two path specs together into a composite spec:
106
107 # specify how to connect initial_c_space and task_space points with transition_mode option
108 transition_mode = lula.CompositePathSpec.TransitionMode.FREE
109 composite_path_spec.add_task_space_path_spec(task_space_spec, transition_mode)
110
111 transition_mode = lula.CompositePathSpec.TransitionMode.FREE
112 composite_path_spec.add_c_space_path_spec(c_space_spec, transition_mode)
113
114 #Transition Modes:
115 # lula.CompositePathSpec.TransitionMode.LINEAR_TASK_SPACE:
116 # Connect cspace to taskspace points linearly through task space. This mode is only available when adding a task_space path spec.
117 # lula.CompositePathSpec.TransitionMode.FREE:
118 # Put no constraints on how cspace and taskspace points are connected
119 # lula.CompositePathSpec.TransitionMode.SKIP:
120 # Skip the first point of the path spec being added, using the last pose instead
121
122
123 trajectory = self._taskspace_trajectory_generator.compute_task_space_trajectory_from_path_spec(
124 composite_path_spec, self._end_effector_name
125 )
126
127 if trajectory is None:
128 carb.log_warn("No trajectory could be computed")
129 self._action_sequence = []
130 else:
131 physics_dt = 1/60
132 articulation_trajectory = ArticulationTrajectory(self._articulation, trajectory, physics_dt)
133
134 # Get a sequence of ArticulationActions that are intended to be passed to the robot at 1/60 second intervals
135 self._action_sequence = articulation_trajectory.get_action_sequence()
136
137 def update(self, step: float):
138 if len(self._action_sequence) == 0:
139 return
140
141 if self._action_sequence_index >= len(self._action_sequence):
142 self._action_sequence_index += 1
143 self._action_sequence_index %= len(self._action_sequence) + 10 # Wait 10 frames before repeating trajectories
144 return
145
146 if self._action_sequence_index == 0:
147 self._teleport_robot_to_position(self._action_sequence[0])
148
149 self._articulation.apply_action(self._action_sequence[self._action_sequence_index])
150
151 self._action_sequence_index += 1
152 self._action_sequence_index %= len(self._action_sequence) + 10 # Wait 10 frames before repeating trajectories
153
154 def reset(self):
155 # Delete any visualized frames
156 if get_prim_at_path("/visualized_frames"):
157 delete_prim("/visualized_frames")
158
159 self._action_sequence = []
160 self._action_sequence_index = 0
161
162 def _teleport_robot_to_position(self, articulation_action):
163 initial_positions = np.zeros(self._articulation.num_dof)
164 initial_positions[articulation_action.joint_indices] = articulation_action.joint_positions
165
166 self._articulation.set_joint_positions(initial_positions)
167 self._articulation.set_joint_velocities(np.zeros_like(initial_positions))
```
The code snippet above creates a `lula.CompositePathSpec` on line 55 with an initial c-space position. It is combined with a `lula.TaskSpacePathSpec` on lines 108-109 and it is combined with a `lula.CSpacePathSpec` on lines 111-112. The resulting path is one that starts at the specified `initial_c_space_robot_pose`, then follows a series of taskspace targets, then hits two c-space targets. When combining path specs, a transition mode must be specified to determine how c-space and task-space points should be connected to each other. Reference lines 114-120 to see the possible options. In this case, no constraint is made on how the `LulaTrajectoryGenerator` connects these points.
Each available option for specifying a `lula.TaskSpacePathSpec` is demonstrated between lines 63-94. The code snippet above moves mainly between three translations: `t0, t1, t2` with possible rotations `r0, r1`. The `lula.TaskSpacePathSpec` object is created with an initial position on line 63. Each following `add` function that is called adds a path between the last position in the `path_spec` so far and a new position. The basic possibilities are:

- Linearly interpolate translation to a new point while keeping rotation fixed (line 71)

- Linearly interpolate rotation to a new point while keeping translation fixed (line 74)

- Linearly interpolate both rotation and translation to a new 6 DOF point (line 68)

The `lula.TaskSpacePathSpec` also makes it easy to define various arcs and circular paths that connect points in space. A three-point arc can be defined that moves through a midpoint to a translation target. There are three options for the orientation of the robot while moving along the path:

- Keep rotation constant (line 79)

- Always stay oriented tangent to the arc (line 82)

- Linearly interpolate rotation to a rotation target (line 85)

Finally, a circular path can be specified without defining a midpoint as on lines 88, 91, and 94. The same three options for specifying orientation are available.

## Summary
This tutorial shows how to use the Lula Trajectory Generator to generate c-space and task-space trajectories for a robot. Task-space trajectories can be specified using a series of task-space waypoints that will be connected linearly, or they can be defined piecewise with many different options for connecting each pair of points in space.

### Further Learning
Reference the Motion Generation page for a complete description of trajectories in NVIDIA Isaac Sim.
