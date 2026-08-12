<!-- source: robot_setup_tutorials/tutorial_pickplace_example.html | title: Tutorial 9: Pick and Place Example — Isaac Sim Documentation -->

# Tutorial 9: Pick and Place Example

## Learning Objectives
This is the final manipulator tutorial in a series of four tutorials. This tutorial tie everything together by showing how to use the UR10e robot and the 2F-140 gripper to follow a target and pick up a block. We will be using the robot imported in Tutorial 6: Setup a Manipulator , tuned in Tutorial 7: Configure a Manipulator , and the robot configuration file generated in Tutorial 8: Generate Robot Configuration File .
In this tutorial, we will be using the Lula kinematics solver to follow a target and the RMPFlow to pick up a block.
Note
All the files created in this tutorial are available at `standalone_examples/api/isaacsim.robot.manipulators/ur10e` for verification.
30 Minutes Tutorial

## Prerequisites

- Review Tutorial 8: Generate Robot Configuration File tutorial prior to beginning this tutorial, continue the following steps from the asset built in the previous tutorial.

Note
If you have not completed the previous tutorial, you can find the prebuilt asset in the content browser at `Isaac Sim/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd`.

## Gripper Control Example
The script below uses the `Parallel Gripper` class to control the gripper joints and the `Manipulator` class to control the robot joints. Steps 0 to 400 close the gripper slowly. Steps 400 to 800, open the gripper slowly, and then reset the gripper position to 0.
Note
The provided script can be run using:

```
./python.sh standalone_examples/api/isaacsim.robot.manipulators/ur10e/gripper_control.py
```
gripper_control.py
```
1from isaacsim import SimulationApp
2
3simulation_app = SimulationApp({"headless": False})
4
5import argparse
6
7import numpy as np
8from isaacsim.core.api import World
9from isaacsim.core.utils.stage import add_reference_to_stage
10from isaacsim.core.utils.types import ArticulationAction
11from isaacsim.robot.manipulators import SingleManipulator
12from isaacsim.robot.manipulators.grippers import ParallelGripper
13from isaacsim.storage.native import get_assets_root_path
14
15parser = argparse.ArgumentParser()
16parser.add_argument("--test", default=False, action="store_true", help="Run in test mode")
17args, unknown = parser.parse_known_args()
18
19my_world = World(stage_units_in_meters=1.0)
20assets_root_path = get_assets_root_path()
21if assets_root_path is None:
22 raise Exception("Could not find Isaac Sim assets folder")
23asset_path = assets_root_path + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd"
24add_reference_to_stage(usd_path=asset_path, prim_path="/ur")
25# define the gripper
26gripper = ParallelGripper(
27 # We chose the following values while inspecting the articulation
28 end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
29 joint_prim_names=["finger_joint"],
30 joint_opened_positions=np.array([0]),
31 joint_closed_positions=np.array([40]),
32 action_deltas=np.array([-40]),
33 use_mimic_joints=True,
34)
35# define the manipulator
36my_ur10 = my_world.scene.add(
37 SingleManipulator(
38 prim_path="/ur",
39 name="ur10_robot",
40 end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
41 gripper=gripper,
42 )
43)
44
45my_world.scene.add_default_ground_plane()
46my_world.reset()
47
48i = 0
49reset_needed = False
50while simulation_app.is_running():
51 my_world.step(render=True)
52 if my_world.is_stopped() and not reset_needed:
53 reset_needed = True
54 if my_world.is_playing():
55 if reset_needed:
56 my_world.reset()
57 reset_needed = False
58 i += 1
59 gripper_positions = my_ur10.gripper.get_joint_positions()
60 if i < 400:
61 # close the gripper slowly
62 my_ur10.gripper.apply_action(ArticulationAction(joint_positions=[gripper_positions[0] + 0.1]))
63 if i > 400:
64 # open the gripper slowly
65 my_ur10.gripper.apply_action(ArticulationAction(joint_positions=[gripper_positions[0] - 0.1]))
66 if i == 800:
67 i = 0
68 if args.test is True:
69 break
70
71simulation_app.close()
```

## Follow Target Example using Lula Kinematics Solver
Create a follow target task using the Lula kinematics solver, where you can specify the target position using a cube and the robot will move its end effector to the target position. The inverse kinematics solver will use the Lula robot descriptor created in the Tutorial 8: Generate Robot Configuration File tutorial.
The generated robot descriptor file is available at `source/standalone_examples/api/isaacsim.robot.manipulators/ur10e/rmpflow/robot_descriptor.yaml`.
Note
The provided script can be run using:

```
./python.sh standalone_examples/api/isaacsim.robot.manipulators/ur10e/follow_target_example.py
```
Move the cube to the target location and run the script to see the robot move its end effector to the target location.
The `ik_solver.py` script initializes the `KinematicsSolver` class and the `LulaKinematicsSolver` class.
controllers/ik_solver.py
```
1import os
2from typing import Optional
3
4from isaacsim.core.prims import Articulation
5from isaacsim.robot_motion.motion_generation import ArticulationKinematicsSolver, LulaKinematicsSolver
6
7
8class KinematicsSolver(ArticulationKinematicsSolver):
9 def __init__(self, robot_articulation: Articulation, end_effector_frame_name: Optional[str] = None) -> None:
10 # TODO: change the config path
11 self._kinematics = LulaKinematicsSolver(
12 robot_description_path=os.path.join(os.path.dirname(__file__), "../rmpflow/robot_descriptor.yaml"),
13 urdf_path=os.path.join(os.path.dirname(__file__), "../rmpflow/ur10e.urdf"),
14 )
15 if end_effector_frame_name is None:
16 end_effector_frame_name = "ee_link_robotiq_arg2f_base_link"
17 ArticulationKinematicsSolver.__init__(self, robot_articulation, self._kinematics, end_effector_frame_name)
18 return
```
The `follow_target.py` script initializes the `FollowTarget` class and sets up the `manipulator` and `parallel_gripper` objects.
tasks/follow_target.py
```
1from typing import Optional
2
3import isaacsim.core.api.tasks as tasks
4import numpy as np
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.robot.manipulators.grippers import ParallelGripper
7from isaacsim.robot.manipulators.manipulators import SingleManipulator
8from isaacsim.storage.native import get_assets_root_path
9
10
11# Inheriting from the base class Follow Target
12class FollowTarget(tasks.FollowTarget):
13 def __init__(
14 self,
15 name: str = "ur10e_follow_target",
16 target_prim_path: Optional[str] = None,
17 target_name: Optional[str] = None,
18 target_position: Optional[np.ndarray] = None,
19 target_orientation: Optional[np.ndarray] = None,
20 offset: Optional[np.ndarray] = None,
21 ) -> None:
22 tasks.FollowTarget.__init__(
23 self,
24 name=name,
25 target_prim_path=target_prim_path,
26 target_name=target_name,
27 target_position=target_position,
28 target_orientation=target_orientation,
29 offset=offset,
30 )
31 return
32
33 def set_robot(self) -> SingleManipulator:
34
35 assets_root_path = get_assets_root_path()
36 if assets_root_path is None:
37 raise Exception("Could not find Isaac Sim assets folder")
38 asset_path = (
39 assets_root_path + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd"
40 )
41 add_reference_to_stage(usd_path=asset_path, prim_path="/ur")
42 # define the gripper
43 gripper = ParallelGripper(
44 # We chose the following values while inspecting the articulation
45 end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
46 joint_prim_names=["finger_joint"],
47 joint_opened_positions=np.array([0]),
48 joint_closed_positions=np.array([40]),
49 action_deltas=np.array([-40]),
50 use_mimic_joints=True,
51 )
52 # define the manipulator
53 manipulator = SingleManipulator(
54 prim_path="/ur",
55 name="ur10_robot",
56 end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
57 gripper=gripper,
58 )
59 return manipulator
```
The `follow_target_example.py` script initializes the `FollowTarget` task and the `KinematicsSolver` created in the previous step with a target location for the cube to be followed by the end effector.
follow_target_example.py
```
1from isaacsim import SimulationApp
2
3simulation_app = SimulationApp({"headless": False})
4
5import numpy as np
6from controller.ik_solver import KinematicsSolver
7from isaacsim.core.api import World
8from tasks.follow_target import FollowTarget
9
10my_world = World(stage_units_in_meters=1.0)
11# Initialize the Follow Target task with a target location for the cube to be followed by the end effector
12my_task = FollowTarget(name="ur10e_follow_target", target_position=np.array([0.5, 0, 0.5]))
13my_world.add_task(my_task)
14my_world.reset()
15task_params = my_world.get_task("ur10e_follow_target").get_params()
16target_name = task_params["target_name"]["value"]
17ur10e_name = task_params["robot_name"]["value"]
18my_ur10e = my_world.scene.get_object(ur10e_name)
19
20# initialize the ik solver
21ik_solver = KinematicsSolver(my_ur10e)
22articulation_controller = my_ur10e.get_articulation_controller()
23
24# run the simulation
25while simulation_app.is_running():
26 my_world.step(render=True)
27 if my_world.is_playing():
28 if my_world.current_time_step_index == 0:
29 my_world.reset()
30
31 observations = my_world.get_observations()
32 actions, succ = ik_solver.compute_inverse_kinematics(
33 target_position=observations[target_name]["position"],
34 target_orientation=observations[target_name]["orientation"],
35 )
36 if succ:
37 articulation_controller.apply_action(actions)
38 else:
39 print("IK did not converge to a solution. No action is being taken.")
40simulation_app.close()
```

## RMP Flow Configuration
Use RMPFlow to control the end effector. See RMPflow for more details about RMPFlow.
The `ur10e_rmpflow_common.yaml` file is available at `source/standalone_examples/api/isaacsim.robot.manipulators/ur10e/rmpflow/ur10e_rmpflow_common.yaml`, it specifies various parameters for the RMPFlow controller.
rmpflow/ur10e_rmpflow_common.yaml
```
1joint_limit_buffers: [.01, .01, .01, .01, .01, .01]
2rmp_params:
3 cspace_target_rmp:
4 metric_scalar: 50.
5 position_gain: 100.
6 damping_gain: 50.
7 robust_position_term_thresh: .5
8 inertia: 1.
9 cspace_trajectory_rmp:
10 p_gain: 100.
11 d_gain: 10.
12 ff_gain: .25
13 weight: 50.
14 cspace_affine_rmp:
15 final_handover_time_std_dev: .25
16 weight: 2000.
17 joint_limit_rmp:
18 metric_scalar: 1000.
19 metric_length_scale: .01
20 metric_exploder_eps: 1e-3
21 metric_velocity_gate_length_scale: .01
22 accel_damper_gain: 200.
23 accel_potential_gain: 1.
24 accel_potential_exploder_length_scale: .1
25 accel_potential_exploder_eps: 1e-2
26 joint_velocity_cap_rmp:
27 max_velocity: 1.
28 velocity_damping_region: .3
29 damping_gain: 1000.0
30 metric_weight: 100.
31 target_rmp:
32 accel_p_gain: 30.
33 accel_d_gain: 85.
34 accel_norm_eps: .075
35 metric_alpha_length_scale: .05
36 min_metric_alpha: .01
37 max_metric_scalar: 10000
38 min_metric_scalar: 2500
39 proximity_metric_boost_scalar: 20.
40 proximity_metric_boost_length_scale: .02
41 xi_estimator_gate_std_dev: 20000.
42 accept_user_weights: false
43 axis_target_rmp:
44 accel_p_gain: 210.
45 accel_d_gain: 60.
46 metric_scalar: 10
47 proximity_metric_boost_scalar: 3000.
48 proximity_metric_boost_length_scale: .08
49 xi_estimator_gate_std_dev: 20000.
50 accept_user_weights: false
51 collision_rmp:
52 damping_gain: 50.
53 damping_std_dev: .04
54 damping_robustness_eps: 1e-2
55 damping_velocity_gate_length_scale: .01
56 repulsion_gain: 800.
57 repulsion_std_dev: .01
58 metric_modulation_radius: .5
59 metric_scalar: 10000.
60 metric_exploder_std_dev: .02
61 metric_exploder_eps: .001
62 damping_rmp:
63 accel_d_gain: 30.
64 metric_scalar: 50.
65 inertia: 100.
66canonical_resolve:
67 max_acceleration_norm: 50.
68 projection_tolerance: .01
69 verbose: false
70body_cylinders:
71 - name: base
72 pt1: [0,0,.10]
73 pt2: [0,0,0.]
74 radius: .2
75body_collision_controllers:
76 - name: ee_link_robotiq_arg2f_base_link
77 radius: .05
```

## Follow Target Example using RMP Flow
Create an RMP flow controller to move the robot end effector to the target location.
Note
The provided script can be run using:

```
./python.sh standalone_examples/api/isaacsim.robot.manipulators/ur10e/follow_target_example_rmpflow.py
```
The `rmpflow.py` initializes Lula motion generation policy using the `ur10e_rmpflow_common.yaml` file above, the `ur10e.urdf` and the robot descriptor file created in Tutorial 8: Generate Robot Configuration File .
controllers/rmpflow.py
```
1import os
2
3import isaacsim.robot_motion.motion_generation as mg
4from isaacsim.core.prims import Articulation
5
6class RMPFlowController(mg.MotionPolicyController):
7 def __init__(self, name: str, robot_articulation: Articulation, physics_dt: float = 1.0 / 60.0) -> None:
8
9 self.rmpflow = mg.lula.motion_policies.RmpFlow(
10 robot_description_path=os.path.join(os.path.dirname(__file__), "../rmpflow/robot_descriptor.yaml"),
11 rmpflow_config_path=os.path.join(os.path.dirname(__file__), "../rmpflow/ur10e_rmpflow_common.yaml"),
12 urdf_path=os.path.join(os.path.dirname(__file__), "../rmpflow/ur10e.urdf"),
13 end_effector_frame_name="ee_link_robotiq_arg2f_base_link",
14 maximum_substep_size=0.00334,
15 )
16
17 self.articulation_rmp = mg.ArticulationMotionPolicy(robot_articulation, self.rmpflow, physics_dt)
18
19 mg.MotionPolicyController.__init__(self, name=name, articulation_motion_policy=self.articulation_rmp)
20 self._default_position, self._default_orientation = (
21 self._articulation_motion_policy._robot_articulation.get_world_pose()
22 )
23 self._motion_policy.set_robot_base_pose(
24 robot_position=self._default_position, robot_orientation=self._default_orientation
25 )
26 return
27
28 def reset(self):
29 mg.MotionPolicyController.reset(self)
30 self._motion_policy.set_robot_base_pose(
31 robot_position=self._default_position, robot_orientation=self._default_orientation
32 )
```
The `follow_target_example_rmpflow.py` script initializes the `FollowTarget` task and the `RMPFlowController` created in the previous step with a target location for the cube to be followed by the end effector.
follow_target_example_rmpflow.py
```
1from isaacsim import SimulationApp
2
3simulation_app = SimulationApp({"headless": False})
4
5import numpy as np
6from controller.rmpflow import RMPFlowController
7from isaacsim.core.api import World
8from tasks.follow_target import FollowTarget
9
10my_world = World(stage_units_in_meters=1.0)
11# Initialize the Follow Target task with a target location for the cube to be followed by the end effector
12my_task = FollowTarget(name="ur10e_follow_target", target_position=np.array([0.5, 0, 0.5]))
13my_world.add_task(my_task)
14my_world.reset()
15task_params = my_world.get_task("ur10e_follow_target").get_params()
16target_name = task_params["target_name"]["value"]
17ur10e_name = task_params["robot_name"]["value"]
18my_ur10e = my_world.scene.get_object(ur10e_name)
19articulation_controller = my_ur10e.get_articulation_controller()
20
21
22# initialize the ik solver
23my_controller = RMPFlowController(name="target_follower_controller", robot_articulation=my_ur10e)
24my_controller.reset()
25
26# run the simulation
27while simulation_app.is_running():
28 my_world.step(render=True)
29 if my_world.is_playing():
30 if my_world.current_time_step_index == 0:
31 my_world.reset()
32 my_controller.reset()
33
34 observations = my_world.get_observations()
35 actions = my_controller.forward(
36 target_end_effector_position=observations[target_name]["position"],
37 target_end_effector_orientation=observations[target_name]["orientation"],
38 )
39 articulation_controller.apply_action(actions)
40simulation_app.close()
```

## Basic Pick and Place Task using RMP Flow
Use the RMPFlow controller to pick up a block and place it in a target location.
Note
The provided script can be run using:

```
./python.sh standalone_examples/api/isaacsim.robot.manipulators/ur10e/pick_up_example.py
```
The `controllers/pick_place.py` script creates a `PickPlace` controller that will pick up a block and place it in a target location.
controllers/pick_place.py
```
1import isaacsim.robot.manipulators.controllers as manipulators_controllers
2from isaacsim.core.prims import SingleArticulation
3from isaacsim.robot.manipulators.grippers import ParallelGripper
4
5from .rmpflow import RMPFlowController
6
7
8class PickPlaceController(manipulators_controllers.PickPlaceController):
9 def __init__(
10 self, name: str, gripper: ParallelGripper, robot_articulation: SingleArticulation, events_dt=None
11 ) -> None:
12 if events_dt is None:
13 events_dt = [0.005, 0.002, 1, 0.05, 0.0008, 0.005, 0.0008, 0.1, 0.0008, 0.008]
14 manipulators_controllers.PickPlaceController.__init__(
15 self,
16 name=name,
17 cspace_controller=RMPFlowController(
18 name=name + "_cspace_controller", robot_articulation=robot_articulation
19 ),
20 gripper=gripper,
21 events_dt=events_dt,
22 end_effector_initial_height=0.6,
23 )
24 return
```
The `tasks/pick_place.py` script creates a `PickPlace` task that sets up the UR10e manipulator and the gripper to pick up a block and place it in a target location.
tasks/pick_place.py
```
1from typing import Optional
2
3import isaacsim.core.api.tasks as tasks
4import numpy as np
5from isaacsim.core.utils.stage import add_reference_to_stage
6from isaacsim.robot.manipulators.grippers import ParallelGripper
7from isaacsim.robot.manipulators.manipulators import SingleManipulator
8from isaacsim.storage.native import get_assets_root_path
9
10
11class PickPlace(tasks.PickPlace):
12 def __init__(
13 self,
14 name: str = "ur10e_pick_place",
15 cube_initial_position: Optional[np.ndarray] = None,
16 cube_initial_orientation: Optional[np.ndarray] = None,
17 target_position: Optional[np.ndarray] = None,
18 offset: Optional[np.ndarray] = None,
19 cube_size: Optional[np.ndarray] = np.array([0.0515, 0.0515, 0.0515]),
20 ) -> None:
21 tasks.PickPlace.__init__(
22 self,
23 name=name,
24 cube_initial_position=cube_initial_position,
25 cube_initial_orientation=cube_initial_orientation,
26 target_position=target_position,
27 cube_size=cube_size,
28 offset=offset,
29 )
30 return
31
32 def set_robot(self) -> SingleManipulator:
33 assets_root_path = get_assets_root_path()
34 if assets_root_path is None:
35 raise Exception("Could not find Isaac Sim assets folder")
36 asset_path = (
37 assets_root_path + "/Isaac/Samples/Rigging/Manipulator/configure_manipulator/ur10e/ur/ur_gripper.usd"
38 )
39 add_reference_to_stage(usd_path=asset_path, prim_path="/ur")
40 # define the gripper
41 gripper = ParallelGripper(
42 # We chose the following values while inspecting the articulation
43 end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
44 joint_prim_names=["finger_joint"],
45 joint_opened_positions=np.array([0]),
46 joint_closed_positions=np.array([40]),
47 action_deltas=np.array([-40]),
48 use_mimic_joints=True,
49 )
50 # define the manipulator
51 manipulator = SingleManipulator(
52 prim_path="/ur",
53 name="ur10_robot",
54 end_effector_prim_path="/ur/ee_link/robotiq_arg2f_base_link",
55 gripper=gripper,
56 )
57 return manipulator
```
The `pick_place_example.py` script puts everything together and runs the simulation.
Important
Make sure to tune the `end_effector_offset` parameter to get the best results, this is the offset between the end effector link on the robot and optimal grasp position for the claw.
pick_place_example.py
```
1from isaacsim import SimulationApp
2
3simulation_app = SimulationApp({"headless": False})
4import numpy as np
5from controller.pick_place import PickPlaceController
6from isaacsim.core.api import World
7from tasks.pick_place import PickPlace
8
9my_world = World(stage_units_in_meters=1.0, physics_dt=1 / 200, rendering_dt=20 / 200)
10
11target_position = np.array([-0.3, 0.6, 0])
12target_position[2] = 0.0515 / 2.0
13my_task = PickPlace(name="ur10e_pick_place", target_position=target_position, cube_size=np.array([0.1, 0.0515, 0.1]))
14my_world.add_task(my_task)
15my_world.reset()
16task_params = my_world.get_task("ur10e_pick_place").get_params()
17ur10e_name = task_params["robot_name"]["value"]
18my_ur10e = my_world.scene.get_object(ur10e_name)
19# initialize the controller
20
21my_controller = PickPlaceController(name="controller", robot_articulation=my_ur10e, gripper=my_ur10e.gripper)
22task_params = my_world.get_task("ur10e_pick_place").get_params()
23articulation_controller = my_ur10e.get_articulation_controller()
24
25reset_needed = False
26
27while simulation_app.is_running():
28 my_world.step(render=True)
29 if my_world.is_playing():
30 if reset_needed:
31 my_world.reset()
32 reset_needed = False
33 my_controller.reset()
34 if my_world.current_time_step_index == 0:
35 my_controller.reset()
36
37 observations = my_world.get_observations()
38 # forward the observation values to the controller to get the actions
39 actions = my_controller.forward(
40 picking_position=observations[task_params["cube_name"]["value"]]["position"],
41 placing_position=observations[task_params["cube_name"]["value"]]["target_position"],
42 current_joint_positions=observations[task_params["robot_name"]["value"]]["joint_positions"],
43 # This offset needs tuning as well
44 end_effector_offset=np.array([0, 0, 0.20]),
45 )
46 if my_controller.is_done():
47 print("done picking and placing")
48 articulation_controller.apply_action(actions)
49
50 if my_world.is_stopped():
51 reset_needed = True
52
53
54simulation_app.close()
```

## Advanced Pick and Place Task using RMPFlow and Foundation Pose
In the pick and place example above, you used the RMPFlow controller to pick up a block and place it in a target location. However there are some limitations to this approach.

- The robot gets the cube pose directly from the simulator observation, which does not translate to the real world.

- The class set up is limited to the cube, and in real life different objects have different shapes and sizes, and different grasping strategies.

To address these limitations, see Isaac Manipulator tutorials for more advanced pick and place tasks.

## Summary
In this tutorial, you learned how to use the Lula kinematics solver to follow a target and the RMPFlow to pick up a block.
