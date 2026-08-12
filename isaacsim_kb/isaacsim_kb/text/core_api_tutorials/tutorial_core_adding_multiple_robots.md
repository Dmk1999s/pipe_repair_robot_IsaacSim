<!-- source: core_api_tutorials/tutorial_core_adding_multiple_robots.html | title: Adding Multiple Robots — Isaac Sim Documentation -->

# Adding Multiple Robots

## Learning Objectives
This tutorial integrates two different types of robot into the same simulation. It details how to build program logic to switch between subtasks. After this tutorial, you will have experience building more complex simulations of robots interacting.
15-20 Minute Tutorial

## Getting Started
Prerequisites

- Review Adding a Manipulator Robot prior to beginning this tutorial.

Begin with the source code open from the previous tutorial, Adding a Manipulator Robot .
Note
Pressing STOP, then PLAY in this workflow might not reset the world properly. Use the RESET button instead.

## Creating the Scene
Begin by adding the Jetbot, Franka Panda, and the Cube from the previous tutorials to the scene. Use a subtask in the task to simplify the code.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4from isaacsim.core.utils.nucleus import get_assets_root_path
5from isaacsim.core.api.tasks import BaseTask
6import numpy as np
7
8
9class RobotsPlaying(BaseTask):
10 def __init__(
11 self,
12 name
13 ):
14 super().__init__(name=name, offset=None)
15 self._jetbot_goal_position = np.array([130, 30, 0])
16 # Add a subtask of pick and place instead
17 # of writing the same task again
18 # we just need to add a jetbot and change the positions of the assets and
19 # the cube target position
20 self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
21 target_position=np.array([0.7, -0.3, 0.0515 / 2.0]))
22 return
23
24 def set_up_scene(self, scene):
25 super().set_up_scene(scene)
26 self._pick_place_task.set_up_scene(scene)
27 assets_root_path = get_assets_root_path()
28 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
29 self._jetbot = scene.add(
30 WheeledRobot(
31 prim_path="/World/Fancy_Robot",
32 name="fancy_robot",
33 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
34 create_robot=True,
35 usd_path=jetbot_asset_path,
36 position=np.array([0, 0.3, 0]))
37 )
38 pick_place_params = self._pick_place_task.get_params()
39 self._franka = scene.get_object(pick_place_params["robot_name"]["value"])
40 # Changes Franka's default position
41 # so that it is set at this position after reset
42 self._franka.set_world_pose(position=np.array([1.0, 0, 0]))
43 self._franka.set_default_state(position=np.array([1.0, 0, 0]))
44 return
45
46 def get_observations(self):
47 current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
48 # Observations needed to drive the jetbot to push the cube
49 observations= {
50 self._jetbot.name: {
51 "position": current_jetbot_position,
52 "orientation": current_jetbot_orientation,
53 "goal_position": self._jetbot_goal_position
54 }
55 }
56 return observations
57
58 def get_params(self):
59 # To avoid hard coding names..etc.
60 pick_place_params = self._pick_place_task.get_params()
61 params_representation = pick_place_params
62 params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
63 params_representation["franka_name"] = pick_place_params["robot_name"]
64 return params_representation
65
66 def post_reset(self):
67 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
68
69
70
71class HelloWorld(BaseSample):
72 def __init__(self) -> None:
73 super().__init__()
74 return
75
76 def setup_scene(self):
77 world = self.get_world()
78 # Add task here
79 world.add_task(RobotsPlaying(name="awesome_task"))
80 return
```

## Integrating a Second Robot
Next, drive the Jetbot to push the cube to the Franka.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4from isaacsim.core.utils.nucleus import get_assets_root_path
5from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
6from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
7from isaacsim.core.api.tasks import BaseTask
8import numpy as np
9
10
11class RobotsPlaying(BaseTask):
12 def __init__(
13 self,
14 name
15 ):
16 super().__init__(name=name, offset=None)
17 self._jetbot_goal_position = np.array([1.3, 0.3, 0])
18 self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
19 target_position=np.array([0.7, -0.3, 0.0515 / 2.0]))
20 return
21
22 def set_up_scene(self, scene):
23 super().set_up_scene(scene)
24 self._pick_place_task.set_up_scene(scene)
25 assets_root_path = get_assets_root_path()
26 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
27 self._jetbot = scene.add(
28 WheeledRobot(
29 prim_path="/World/Fancy_Jetbot",
30 name="fancy_jetbot",
31 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
32 create_robot=True,
33 usd_path=jetbot_asset_path,
34 position=np.array([0, 0.3, 0]),
35 )
36 )
37 pick_place_params = self._pick_place_task.get_params()
38 self._franka = scene.get_object(pick_place_params["robot_name"]["value"])
39 self._franka.set_world_pose(position=np.array([1.0, 0, 0]))
40 self._franka.set_default_state(position=np.array([1.0, 0, 0]))
41 return
42
43 def get_observations(self):
44 current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
45 observations= {
46 self._jetbot.name: {
47 "position": current_jetbot_position,
48 "orientation": current_jetbot_orientation,
49 "goal_position": self._jetbot_goal_position
50 }
51 }
52 return observations
53
54 def get_params(self):
55 pick_place_params = self._pick_place_task.get_params()
56 params_representation = pick_place_params
57 params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
58 params_representation["franka_name"] = pick_place_params["robot_name"]
59 return params_representation
60
61 def post_reset(self):
62 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
63
64
65class HelloWorld(BaseSample):
66 def __init__(self) -> None:
67 super().__init__()
68 return
69
70 def setup_scene(self):
71 world = self.get_world()
72 world.add_task(RobotsPlaying(name="awesome_task"))
73 return
74
75 async def setup_post_load(self):
76 self._world = self.get_world()
77 task_params = self._world.get_task("awesome_task").get_params()
78 self._jetbot = self._world.scene.get_object(task_params["jetbot_name"]["value"])
79 self._cube_name = task_params["cube_name"]["value"]
80 self._jetbot_controller = WheelBasePoseController(name="cool_controller",
81 open_loop_wheel_controller=
82 DifferentialController(name="simple_control",
83 wheel_radius=0.03, wheel_base=0.1125))
84 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
85 await self._world.play_async()
86 return
87
88 async def setup_post_reset(self):
89 self._jetbot_controller.reset()
90 await self._world.play_async()
91 return
92
93 def physics_step(self, step_size):
94 current_observations = self._world.get_observations()
95 self._jetbot.apply_action(
96 self._jetbot_controller.forward(
97 start_position=current_observations[self._jetbot.name]["position"],
98 start_orientation=current_observations[self._jetbot.name]["orientation"],
99 goal_position=current_observations[self._jetbot.name]["goal_position"]))
100 return
```

## Adding Task Logic
Next, drive Jetbot backwards after it delivers the cube to give space to Franka to pick up the cube.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4from isaacsim.core.utils.nucleus import get_assets_root_path
5from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
6from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
7from isaacsim.core.api.tasks import BaseTask
8from isaacsim.core.utils.types import ArticulationAction
9import numpy as np
10
11
12class RobotsPlaying(BaseTask):
13 def __init__(
14 self,
15 name
16 ):
17 super().__init__(name=name, offset=None)
18 self._jetbot_goal_position = np.array([1.3, 0.3, 0])
19 # Add task logic to signal to the robots which task is active
20 self._task_event = 0
21 self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
22 target_position=np.array([0.7, -0.3, 0.0515 / 2.0]))
23 return
24
25 def set_up_scene(self, scene):
26 super().set_up_scene(scene)
27 self._pick_place_task.set_up_scene(scene)
28 assets_root_path = get_assets_root_path()
29 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
30 self._jetbot = scene.add(
31 WheeledRobot(
32 prim_path="/World/Fancy_Jetbot",
33 name="fancy_jetbot",
34 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
35 create_robot=True,
36 usd_path=jetbot_asset_path,
37 position=np.array([0, 0.3, 0]),
38 )
39 )
40 pick_place_params = self._pick_place_task.get_params()
41 self._franka = scene.get_object(pick_place_params["robot_name"]["value"])
42 self._franka.set_world_pose(position=np.array([1.0, 0, 0]))
43 self._franka.set_default_state(position=np.array([1.0, 0, 0]))
44 return
45
46 def get_observations(self):
47 current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
48 observations= {
49 "task_event": self._task_event,
50 self._jetbot.name: {
51 "position": current_jetbot_position,
52 "orientation": current_jetbot_orientation,
53 "goal_position": self._jetbot_goal_position
54 }
55 }
56 return observations
57
58 def get_params(self):
59 pick_place_params = self._pick_place_task.get_params()
60 params_representation = pick_place_params
61 params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
62 params_representation["franka_name"] = pick_place_params["robot_name"]
63 return params_representation
64
65 def pre_step(self, control_index, simulation_time):
66 if self._task_event == 0:
67 current_jetbot_position, _ = self._jetbot.get_world_pose()
68 if np.mean(np.abs(current_jetbot_position[:2] - self._jetbot_goal_position[:2])) < 0.04:
69 self._task_event += 1
70 self._cube_arrive_step_index = control_index
71 elif self._task_event == 1:
72 # Jetbot has 200 time steps to back off from Franka
73 if control_index - self._cube_arrive_step_index == 200:
74 self._task_event += 1
75 return
76
77 def post_reset(self):
78 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
79 self._task_event = 0
80 return
81
82
83
84class HelloWorld(BaseSample):
85 def __init__(self) -> None:
86 super().__init__()
87 return
88
89 def setup_scene(self):
90 world = self.get_world()
91 world.add_task(RobotsPlaying(name="awesome_task"))
92 return
93
94 async def setup_post_load(self):
95 self._world = self.get_world()
96 task_params = self._world.get_task("awesome_task").get_params()
97 self._jetbot = self._world.scene.get_object(task_params["jetbot_name"]["value"])
98 self._cube_name = task_params["cube_name"]["value"]
99 self._jetbot_controller = WheelBasePoseController(name="cool_controller",
100 open_loop_wheel_controller=
101 DifferentialController(name="simple_control",
102 wheel_radius=0.03, wheel_base=0.1125))
103 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
104 await self._world.play_async()
105 return
106
107 async def setup_post_reset(self):
108 self._jetbot_controller.reset()
109 await self._world.play_async()
110 return
111
112 def physics_step(self, step_size):
113 current_observations = self._world.get_observations()
114 if current_observations["task_event"] == 0:
115 self._jetbot.apply_wheel_actions(
116 self._jetbot_controller.forward(
117 start_position=current_observations[self._jetbot.name]["position"],
118 start_orientation=current_observations[self._jetbot.name]["orientation"],
119 goal_position=current_observations[self._jetbot.name]["goal_position"]))
120 elif current_observations["task_event"] == 1:
121 # Go backwards
122 self._jetbot.apply_wheel_actions(ArticulationAction(joint_velocities=[-8, -8]))
123 elif current_observations["task_event"] == 2:
124 # Apply zero velocity to override the velocity applied before.
125 # Note: target joint positions and target joint velocities will stay active unless changed
126 self._jetbot.apply_wheel_actions(ArticulationAction(joint_velocities=[0.0, 0.0]))
127 return
```

## Robot Handover
Now, it’s the Franka’s turn to pick it up.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4from isaacsim.core.utils.nucleus import get_assets_root_path
5from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
6from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
7from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
8from isaacsim.core.api.tasks import BaseTask
9from isaacsim.core.utils.types import ArticulationAction
10import numpy as np
11
12
13class RobotsPlaying(BaseTask):
14 def __init__(
15 self,
16 name
17 ):
18 super().__init__(name=name, offset=None)
19 self._jetbot_goal_position = np.array([1.3, 0.3, 0])
20 self._task_event = 0
21 self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
22 target_position=np.array([0.7, -0.3, 0.0515 / 2.0]))
23 return
24
25 def set_up_scene(self, scene):
26 super().set_up_scene(scene)
27 self._pick_place_task.set_up_scene(scene)
28 assets_root_path = get_assets_root_path()
29 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
30 self._jetbot = scene.add(
31 WheeledRobot(
32 prim_path="/World/Fancy_Jetbot",
33 name="fancy_jetbot",
34 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
35 create_robot=True,
36 usd_path=jetbot_asset_path,
37 position=np.array([0, 0.3, 0]),
38 )
39 )
40 pick_place_params = self._pick_place_task.get_params()
41 self._franka = scene.get_object(pick_place_params["robot_name"]["value"])
42 self._franka.set_world_pose(position=np.array([1.0, 0, 0]))
43 self._franka.set_default_state(position=np.array([1.0, 0, 0]))
44 return
45
46 def get_observations(self):
47 current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
48 observations= {
49 "task_event": self._task_event,
50 self._jetbot.name: {
51 "position": current_jetbot_position,
52 "orientation": current_jetbot_orientation,
53 "goal_position": self._jetbot_goal_position
54 }
55 }
56 # add the subtask's observations as well
57 observations.update(self._pick_place_task.get_observations())
58 return observations
59
60 def get_params(self):
61 pick_place_params = self._pick_place_task.get_params()
62 params_representation = pick_place_params
63 params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
64 params_representation["franka_name"] = pick_place_params["robot_name"]
65 return params_representation
66
67 def pre_step(self, control_index, simulation_time):
68 if self._task_event == 0:
69 current_jetbot_position, _ = self._jetbot.get_world_pose()
70 if np.mean(np.abs(current_jetbot_position[:2] - self._jetbot_goal_position[:2])) < 0.04:
71 self._task_event += 1
72 self._cube_arrive_step_index = control_index
73 elif self._task_event == 1:
74 if control_index - self._cube_arrive_step_index == 200:
75 self._task_event += 1
76 return
77
78 def post_reset(self):
79 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
80 self._task_event = 0
81 return
82
83
84class HelloWorld(BaseSample):
85 def __init__(self) -> None:
86 super().__init__()
87 return
88
89 def setup_scene(self):
90 world = self.get_world()
91 world.add_task(RobotsPlaying(name="awesome_task"))
92 return
93
94 async def setup_post_load(self):
95 self._world = self.get_world()
96 task_params = self._world.get_task("awesome_task").get_params()
97 # We need franka later to apply to it actions
98 self._franka = self._world.scene.get_object(task_params["franka_name"]["value"])
99 self._jetbot = self._world.scene.get_object(task_params["jetbot_name"]["value"])
100 # We need the cube later on for the pick place controller
101 self._cube_name = task_params["cube_name"]["value"]
102 # Add Franka Controller
103 self._franka_controller = PickPlaceController(name="pick_place_controller",
104 gripper=self._franka.gripper,
105 robot_articulation=self._franka)
106 self._jetbot_controller = WheelBasePoseController(name="cool_controller",
107 open_loop_wheel_controller=
108 DifferentialController(name="simple_control",
109 wheel_radius=0.03, wheel_base=0.1125))
110 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
111 await self._world.play_async()
112 return
113
114 async def setup_post_reset(self):
115 self._franka_controller.reset()
116 self._jetbot_controller.reset()
117 await self._world.play_async()
118 return
119
120 def physics_step(self, step_size):
121 current_observations = self._world.get_observations()
122 if current_observations["task_event"] == 0:
123 self._jetbot.apply_wheel_actions(
124 self._jetbot_controller.forward(
125 start_position=current_observations[self._jetbot.name]["position"],
126 start_orientation=current_observations[self._jetbot.name]["orientation"],
127 goal_position=current_observations[self._jetbot.name]["goal_position"]))
128 elif current_observations["task_event"] == 1:
129 self._jetbot.apply_wheel_actions(ArticulationAction(joint_velocities=[-8, -8]))
130 elif current_observations["task_event"] == 2:
131 self._jetbot.apply_wheel_actions(ArticulationAction(joint_velocities=[0.0, 0.0]))
132 # Pick up the block
133 actions = self._franka_controller.forward(
134 picking_position=current_observations[self._cube_name]["position"],
135 placing_position=current_observations[self._cube_name]["target_position"],
136 current_joint_positions=current_observations[self._franka.name]["joint_positions"])
137 self._franka.apply_action(actions)
138 # Pause once the controller is done
139 if self._franka_controller.is_done():
140 self._world.pause()
141 return
```

## Summary
This tutorial covered the following topics:

- Adding multiple robots to the scene

- Controlling robot behavior with program states in the task structure.

### Next Steps
Continue on to the next tutorial in our Essential Tutorials series, Multiple Tasks , to learn how to add multiple tasks and manage them.
