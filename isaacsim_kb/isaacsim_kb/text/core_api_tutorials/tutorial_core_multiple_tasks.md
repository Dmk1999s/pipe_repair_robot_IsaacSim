<!-- source: core_api_tutorials/tutorial_core_multiple_tasks.html | title: Multiple Tasks — Isaac Sim Documentation -->

# Multiple Tasks

## Learning Objectives
This tutorial describes how to add multiple tasks in NVIDIA Isaac Sim. It explains how to add parameters to Tasks to scale your simulations. After this tutorial, you will have more experience building multi-task simulations in NVIDIA Isaac Sim.
15-20 Minute Tutorial

## Getting Started
Prerequisites

- Review Adding Multiple Robots prior to beginning this tutorial.

Begin with the source code open from the previous tutorial, Adding Multiple Robots .
Note
Pressing STOP, then PLAY in this workflow might not reset the world properly. Use the RESET button instead.

## Parameterizing Tasks
Adding parameters to tasks is a useful method to coordinate complex behaviors across multiple tasks. Start by adding an `offset` parameter to the task. This `offset` parameter will allow you to translate the assets of all tasks by the offset.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
3from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
4from isaacsim.robot.wheeled_robots.robots import WheeledRobot
5from isaacsim.core.utils.nucleus import get_assets_root_path
6from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
7from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
8from isaacsim.core.api.tasks import BaseTask
9from isaacsim.core.utils.types import ArticulationAction
10# Find a unique string name, to use it for prim paths and scene names
11from isaacsim.core.utils.string import find_unique_string_name # Creates a unique prim path
12from isaacsim.core.utils.prims import is_prim_path_valid # Checks if a prim path is valid
13from isaacsim.core.api.objects.cuboid import VisualCuboid
14import numpy as np
15
16
17class RobotsPlaying(BaseTask):
18 # Adding offset to move the task objects with and the targets..etc
19 def __init__(self, name, offset=None):
20 super().__init__(name=name, offset=offset)
21 self._task_event = 0
22 self._jetbot_goal_position = np.array([1.3, 0.3, 0]) + self._offset #defined in the base task
23 self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
24 target_position=np.array([0.7, -0.3, 0.0515 / 2.0]),
25 offset=offset)
26 return
27
28 def set_up_scene(self, scene):
29 super().set_up_scene(scene)
30 #This will already translate the pick and place assets by the offset
31 self._pick_place_task.set_up_scene(scene)
32 # Find a unique scene name
33 jetbot_name = find_unique_string_name(
34 initial_name="fancy_jetbot", is_unique_fn=lambda x: not self.scene.object_exists(x)
35 )
36 # Find a unique prim path
37 jetbot_prim_path = find_unique_string_name(
38 initial_name="/World/Fancy_Jetbot", is_unique_fn=lambda x: not is_prim_path_valid(x)
39 )
40 assets_root_path = get_assets_root_path()
41 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
42 self._jetbot = scene.add(
43 WheeledRobot(
44 prim_path=jetbot_prim_path,
45 name=jetbot_name,
46 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
47 create_robot=True,
48 usd_path=jetbot_asset_path,
49 position=np.array([0, 0.3, 0]),
50 )
51 )
52 # Add Jetbot to this task objects
53 self._task_objects[self._jetbot.name] = self._jetbot
54 pick_place_params = self._pick_place_task.get_params()
55 self._franka = scene.get_object(pick_place_params["robot_name"]["value"])
56 # translate the franka by 100 in the x direction
57 current_position, _ = self._franka.get_world_pose()
58 self._franka.set_world_pose(position=current_position + np.array([1.0, 0, 0]))
59 self._franka.set_default_state(position=current_position + np.array([1.0, 0, 0]))
60 # This will only translate the task_objects by the offset specified (defined in the BaseTask)
61 # Note: PickPlace task objects were already translated when setting up its scene
62 self._move_task_objects_to_their_frame()
63 return
64
65 def get_observations(self):
66 current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
67 observations= {
68 "task_event": self._task_event,
69 self._jetbot.name: {
70 "position": current_jetbot_position,
71 "orientation": current_jetbot_orientation,
72 "goal_position": self._jetbot_goal_position
73 }
74 }
75 observations.update(self._pick_place_task.get_observations())
76 return observations
77
78 def get_params(self):
79 pick_place_params = self._pick_place_task.get_params()
80 params_representation = pick_place_params
81 params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
82 params_representation["franka_name"] = pick_place_params["robot_name"]
83 return params_representation
84
85 def pre_step(self, control_index, simulation_time):
86 if self._task_event == 0:
87 current_jetbot_position, _ = self._jetbot.get_world_pose()
88 if np.mean(np.abs(current_jetbot_position[:2] - self._jetbot_goal_position[:2])) < 0.04:
89 self._task_event += 1
90 self._cube_arrive_step_index = control_index
91 elif self._task_event == 1:
92 if control_index - self._cube_arrive_step_index == 200:
93 self._task_event += 1
94 return
95
96 def post_reset(self):
97 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
98 self._task_event = 0
99 return
100
101
102class HelloWorld(BaseSample):
103 def __init__(self) -> None:
104 super().__init__()
105 return
106
107 def setup_scene(self):
108 world = self.get_world()
109 world.add_task(RobotsPlaying(name="awesome_task", offset=np.array([0, -1.0, 0])))
110 # For visualization purposes only, so we don't need to add it to the scene
111 # Its there to only see where Franka was supposed to be vs after adding the offset
112 VisualCuboid(prim_path="/new_cube_1",
113 name="visual_cube",
114 position=np.array([1.0, 0, 0.05]),
115 scale=np.array([0.1, 0.1, 0.1]))
116 return
117
118 async def setup_post_load(self):
119 self._world = self.get_world()
120 task_params = self._world.get_task("awesome_task").get_params()
121 self._franka = self._world.scene.get_object(task_params["franka_name"]["value"])
122 self._jetbot = self._world.scene.get_object(task_params["jetbot_name"]["value"])
123 self._cube_name = task_params["cube_name"]["value"]
124 self._franka_controller = PickPlaceController(name="pick_place_controller",
125 gripper=self._franka.gripper,
126 robot_articulation=self._franka)
127 self._jetbot_controller = WheelBasePoseController(name="cool_controller",
128 open_loop_wheel_controller=
129 DifferentialController(name="simple_control",
130 wheel_radius=0.03, wheel_base=0.1125))
131 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
132 await self._world.play_async()
133 return
134
135 async def setup_post_reset(self):
136 self._franka_controller.reset()
137 self._jetbot_controller.reset()
138 await self._world.play_async()
139 return
140
141 def physics_step(self, step_size):
142 current_observations = self._world.get_observations()
143 if current_observations["task_event"] == 0:
144 self._jetbot.apply_wheel_actions(
145 self._jetbot_controller.forward(
146 start_position=current_observations[self._jetbot.name]["position"],
147 start_orientation=current_observations[self._jetbot.name]["orientation"],
148 goal_position=current_observations[self._jetbot.name]["goal_position"]))
149 elif current_observations["task_event"] == 1:
150 self._jetbot.apply_wheel_actions(ArticulationAction(joint_velocities=[-8.0, -8.0]))
151 elif current_observations["task_event"] == 2:
152 self._jetbot.apply_wheel_actions(ArticulationAction(joint_velocities=[0.0, 0.0]))
153 actions = self._franka_controller.forward(
154 picking_position=current_observations[self._cube_name]["position"],
155 placing_position=current_observations[self._cube_name]["target_position"],
156 current_joint_positions=current_observations[self._franka.name]["joint_positions"])
157 self._franka.apply_action(actions)
158 if self._franka_controller.is_done():
159 self._world.pause()
160 return
```

## Scaling to Many Tasks
To scale to many tasks, you can add the same or different tasks in the world and decide where they operate in the world using the `offset` parameter. Each task will have its own controller.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.utils.nucleus import get_assets_root_path
3from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
4from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
5from isaacsim.robot.wheeled_robots.robots import WheeledRobot
6from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
7from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
8from isaacsim.core.api.tasks import BaseTask
9from isaacsim.core.utils.types import ArticulationAction
10from isaacsim.core.utils.string import find_unique_string_name
11from isaacsim.core.utils.prims import is_prim_path_valid
12import numpy as np
13
14
15class RobotsPlaying(BaseTask):
16 def __init__(self, name, offset=None):
17 super().__init__(name=name, offset=offset)
18 self._task_event = 0
19 # Randomize the task a bit
20 self._jetbot_goal_position = np.array([np.random.uniform(1.2, 1.6), 0.3, 0]) + self._offset
21 self._pick_place_task = PickPlace(cube_initial_position=np.array([0.1, 0.3, 0.05]),
22 target_position=np.array([0.7, -0.3, 0.0515 / 2.0]),
23 offset=offset)
24 return
25
26 def set_up_scene(self, scene):
27 super().set_up_scene(scene)
28 self._pick_place_task.set_up_scene(scene)
29 jetbot_name = find_unique_string_name(
30 initial_name="fancy_jetbot", is_unique_fn=lambda x: not self.scene.object_exists(x)
31 )
32 jetbot_prim_path = find_unique_string_name(
33 initial_name="/World/Fancy_Jetbot", is_unique_fn=lambda x: not is_prim_path_valid(x)
34 )
35 assets_root_path = get_assets_root_path()
36 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
37 self._jetbot = scene.add(
38 WheeledRobot(
39 prim_path=jetbot_prim_path,
40 name=jetbot_name,
41 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
42 create_robot=True,
43 usd_path=jetbot_asset_path,
44 position=np.array([0, 0.3, 0]),
45 )
46 )
47 self._task_objects[self._jetbot.name] = self._jetbot
48 pick_place_params = self._pick_place_task.get_params()
49 self._franka = scene.get_object(pick_place_params["robot_name"]["value"])
50 current_position, _ = self._franka.get_world_pose()
51 self._franka.set_world_pose(position=current_position + np.array([1.0, 0, 0]))
52 self._franka.set_default_state(position=current_position + np.array([1.0, 0, 0]))
53 self._move_task_objects_to_their_frame()
54 return
55
56 def get_observations(self):
57 current_jetbot_position, current_jetbot_orientation = self._jetbot.get_world_pose()
58 observations= {
59 self.name + "_event": self._task_event, #change task event to make it unique
60 self._jetbot.name: {
61 "position": current_jetbot_position,
62 "orientation": current_jetbot_orientation,
63 "goal_position": self._jetbot_goal_position
64 }
65 }
66 observations.update(self._pick_place_task.get_observations())
67 return observations
68
69 def get_params(self):
70 pick_place_params = self._pick_place_task.get_params()
71 params_representation = pick_place_params
72 params_representation["jetbot_name"] = {"value": self._jetbot.name, "modifiable": False}
73 params_representation["franka_name"] = pick_place_params["robot_name"]
74 return params_representation
75
76 def pre_step(self, control_index, simulation_time):
77 if self._task_event == 0:
78 current_jetbot_position, _ = self._jetbot.get_world_pose()
79 if np.mean(np.abs(current_jetbot_position[:2] - self._jetbot_goal_position[:2])) < 0.04:
80 self._task_event += 1
81 self._cube_arrive_step_index = control_index
82 elif self._task_event == 1:
83 if control_index - self._cube_arrive_step_index == 200:
84 self._task_event += 1
85 return
86
87 def post_reset(self):
88 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
89 self._task_event = 0
90 return
91
92
93class HelloWorld(BaseSample):
94 def __init__(self) -> None:
95 super().__init__()
96 # Add lists for tasks,
97 self._tasks = []
98 self._num_of_tasks = 3
99 # Add lists for controllers
100 self._franka_controllers = []
101 self._jetbot_controllers = []
102 # Add lists for variables needed for control
103 self._jetbots = []
104 self._frankas = []
105 self._cube_names = []
106 return
107
108 def setup_scene(self):
109 world = self.get_world()
110 for i in range(self._num_of_tasks):
111 world.add_task(RobotsPlaying(name="my_awesome_task_" + str(i), offset=np.array([0, (i * 2) - 3, 0])))
112 return
113
114 async def setup_post_load(self):
115 self._world = self.get_world()
116 for i in range(self._num_of_tasks):
117 self._tasks.append(self._world.get_task(name="my_awesome_task_" + str(i)))
118 # Get variables needed for control
119 task_params = self._tasks[i].get_params()
120 self._frankas.append(self._world.scene.get_object(task_params["franka_name"]["value"]))
121 self._jetbots.append(self._world.scene.get_object(task_params["jetbot_name"]["value"]))
122 self._cube_names.append(task_params["cube_name"]["value"])
123 # Define controllers
124 self._franka_controllers.append(PickPlaceController(name="pick_place_controller",
125 gripper=self._frankas[i].gripper,
126 robot_articulation=self._frankas[i],
127 # Change the default events dt of the
128 # pick and place controller to slow down some of the transitions
129 # to pick up further blocks
130 # Note: this is a simple pick and place state machine
131 # based on events dt and not event success
132 # check the different events description in the api
133 # documentation
134 events_dt=[0.008, 0.002, 0.5, 0.1, 0.05, 0.05, 0.0025, 1, 0.008, 0.08]))
135 self._jetbot_controllers.append(WheelBasePoseController(name="cool_controller",
136 open_loop_wheel_controller=
137 DifferentialController(name="simple_control",
138 wheel_radius=0.03, wheel_base=0.1125)))
139 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
140 await self._world.play_async()
141 return
142
143 async def setup_post_reset(self):
144 for i in range(len(self._tasks)):
145 # Reset all controllers
146 self._franka_controllers[i].reset()
147 self._jetbot_controllers[i].reset()
148 await self._world.play_async()
149 return
150
151 def physics_step(self, step_size):
152 current_observations = self._world.get_observations()
153 for i in range(len(self._tasks)):
154 # Apply actions for each task
155 if current_observations[self._tasks[i].name + "_event"] == 0:
156 self._jetbots[i].apply_wheel_actions(
157 self._jetbot_controllers[i].forward(
158 start_position=current_observations[self._jetbots[i].name]["position"],
159 start_orientation=current_observations[self._jetbots[i].name]["orientation"],
160 goal_position=current_observations[self._jetbots[i].name]["goal_position"]))
161 elif current_observations[self._tasks[i].name + "_event"] == 1:
162 self._jetbots[i].apply_wheel_actions(ArticulationAction(joint_velocities=[-8.0, -8.0]))
163 elif current_observations[self._tasks[i].name + "_event"] == 2:
164 self._jetbots[i].apply_wheel_actions(ArticulationAction(joint_velocities=[0.0, 0.0]))
165 actions = self._franka_controllers[i].forward(
166 picking_position=current_observations[self._cube_names[i]]["position"],
167 placing_position=current_observations[self._cube_names[i]]["target_position"],
168 current_joint_positions=current_observations[self._frankas[i].name]["joint_positions"])
169 self._frankas[i].apply_action(actions)
170 return
171
172 # This function is called after a hot reload or a clear
173 # to delete the variables defined in this extension application
174 def world_cleanup(self):
175 self._tasks = []
176 self._franka_controllers = []
177 self._jetbot_controllers = []
178 self._jetbots = []
179 self._frankas = []
180 self._cube_names = []
181 return
```

## Summary
This tutorial covered the following topics:

- Parameterizing `Tasks`

- Changing event velocities of the `PickPlace` controller

- Using `world_cleanup` to clear the extension application properly while hot reloading and creating a new stage.

- Choosing valid prim paths and scene names.

### Further Learning

- See the standalone application at `standalone_examples/api/isaacsim.robot.manipulators/universal_robots/multiple_tasks.py` for adding different tasks.
