<!-- source: core_api_tutorials/tutorial_core_adding_manipulator.html | title: Adding a Manipulator Robot — Isaac Sim Documentation -->

# Adding a Manipulator Robot

## Learning Objectives
This tutorial introduces a second robot to the simulation, a Franka Panda manipulator. It describes how to add the robot to the scene and use its `PickAndPlaceController` class. After this tutorial, you will have more experience using different robot and controller classes in NVIDIA Isaac Sim.
15-20 Minute Tutorial

## Getting Started
Prerequisites

- Review Adding a Controller prior to beginning this tutorial.

Begin with the source code open from the Adding a Controller tutorial, by clicking the Open Source Code button in the Hello World Example window.
Note
Pressing STOP, then PLAY in this workflow might not reset the world properly. Use the RESET button instead.

## Creating the Scene
Begin by adding a Franka robot from the `isaacsim.robot.manipulators.examples.franka` extension, as well as a cube for the Franka to pick up.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2# This extension has franka related tasks and controllers as well
3from isaacsim.robot.manipulators.examples.franka import Franka
4from isaacsim.core.api.objects import DynamicCuboid
5import numpy as np
6
7
8class HelloWorld(BaseSample):
9 def __init__(self) -> None:
10 super().__init__()
11 return
12
13 def setup_scene(self):
14 world = self.get_world()
15 world.scene.add_default_ground_plane()
16 # Robot specific class that provides extra functionalities
17 # such as having gripper and end_effector instances.
18 franka = world.scene.add(Franka(prim_path="/World/Fancy_Franka", name="fancy_franka"))
19 # add a cube for franka to pick up
20 world.scene.add(
21 DynamicCuboid(
22 prim_path="/World/random_cube",
23 name="fancy_cube",
24 position=np.array([0.3, 0.3, 0.3]),
25 scale=np.array([0.0515, 0.0515, 0.0515]),
26 color=np.array([0, 0, 1.0]),
27 )
28 )
29 return
```

## Using the PickAndPlace Controller
Add a pick-and-place controller from `isaacsim.robot.manipulators.examples.franka` so that the Franka picks up the cube and places it somewhere else.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka import Franka
3from isaacsim.core.api.objects import DynamicCuboid
4from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
5import numpy as np
6
7
8class HelloWorld(BaseSample):
9 def __init__(self) -> None:
10 super().__init__()
11 return
12
13 def setup_scene(self):
14 world = self.get_world()
15 world.scene.add_default_ground_plane()
16 franka = world.scene.add(Franka(prim_path="/World/Fancy_Franka", name="fancy_franka"))
17 world.scene.add(
18 DynamicCuboid(
19 prim_path="/World/random_cube",
20 name="fancy_cube",
21 position=np.array([0.3, 0.3, 0.3]),
22 scale=np.array([0.0515, 0.0515, 0.0515]),
23 color=np.array([0, 0, 1.0]),
24 )
25 )
26 return
27
28 async def setup_post_load(self):
29 self._world = self.get_world()
30 self._franka = self._world.scene.get_object("fancy_franka")
31 self._fancy_cube = self._world.scene.get_object("fancy_cube")
32 # Initialize a pick and place controller
33 self._controller = PickPlaceController(
34 name="pick_place_controller",
35 gripper=self._franka.gripper,
36 robot_articulation=self._franka,
37 )
38 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
39 # World has pause, stop, play..etc
40 # Note: if async version exists, use it in any async function is this workflow
41 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
42 await self._world.play_async()
43 return
44
45 # This function is called after Reset button is pressed
46 # Resetting anything in the world should happen here
47 async def setup_post_reset(self):
48 self._controller.reset()
49 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
50 await self._world.play_async()
51 return
52
53 def physics_step(self, step_size):
54 cube_position, _ = self._fancy_cube.get_world_pose()
55 goal_position = np.array([-0.3, -0.3, 0.0515 / 2.0])
56 current_joint_positions = self._franka.get_joint_positions()
57 actions = self._controller.forward(
58 picking_position=cube_position,
59 placing_position=goal_position,
60 current_joint_positions=current_joint_positions,
61 )
62 self._franka.apply_action(actions)
63 # Only for the pick and place controller, indicating if the state
64 # machine reached the final state.
65 if self._controller.is_done():
66 self._world.pause()
67 return
```

## What is a Task?
The Task class in NVIDIA Isaac Sim provides a way to modularize the scene creation, information retrieval, and calculating metrics. It is useful to create more complex scenes with advanced logic. You will need to re-write the previous code using the `Task` class.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka import Franka
3from isaacsim.core.api.objects import DynamicCuboid
4from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
5from isaacsim.core.api.tasks import BaseTask
6import numpy as np
7
8class FrankaPlaying(BaseTask):
9 #NOTE: we only cover here a subset of the task functions that are available,
10 # checkout the base class for all the available functions to override.
11 # ex: calculate_metrics, is_done..etc.
12 def __init__(self, name):
13 super().__init__(name=name, offset=None)
14 self._goal_position = np.array([-0.3, -0.3, 0.0515 / 2.0])
15 self._task_achieved = False
16 return
17
18 # Here we setup all the assets that we care about in this task.
19 def set_up_scene(self, scene):
20 super().set_up_scene(scene)
21 scene.add_default_ground_plane()
22 self._cube = scene.add(DynamicCuboid(prim_path="/World/random_cube",
23 name="fancy_cube",
24 position=np.array([0.3, 0.3, 0.3]),
25 scale=np.array([0.0515, 0.0515, 0.0515]),
26 color=np.array([0, 0, 1.0])))
27 self._franka = scene.add(Franka(prim_path="/World/Fancy_Franka",
28 name="fancy_franka"))
29 return
30
31 # Information exposed to solve the task is returned from the task through get_observations
32 def get_observations(self):
33 cube_position, _ = self._cube.get_world_pose()
34 current_joint_positions = self._franka.get_joint_positions()
35 observations = {
36 self._franka.name: {
37 "joint_positions": current_joint_positions,
38 },
39 self._cube.name: {
40 "position": cube_position,
41 "goal_position": self._goal_position
42 }
43 }
44 return observations
45
46 # Called before each physics step,
47 # for instance we can check here if the task was accomplished by
48 # changing the color of the cube once its accomplished
49 def pre_step(self, control_index, simulation_time):
50 cube_position, _ = self._cube.get_world_pose()
51 if not self._task_achieved and np.mean(np.abs(self._goal_position - cube_position)) < 0.02:
52 # Visual Materials are applied by default to the cube
53 # in this case the cube has a visual material of type
54 # PreviewSurface, we can set its color once the target is reached.
55 self._cube.get_applied_visual_material().set_color(color=np.array([0, 1.0, 0]))
56 self._task_achieved = True
57 return
58
59 # Called after each reset,
60 # for instance we can always set the gripper to be opened at the beginning after each reset
61 # also we can set the cube's color to be blue
62 def post_reset(self):
63 self._franka.gripper.set_joint_positions(self._franka.gripper.joint_opened_positions)
64 self._cube.get_applied_visual_material().set_color(color=np.array([0, 0, 1.0]))
65 self._task_achieved = False
66 return
67
68
69class HelloWorld(BaseSample):
70 def __init__(self) -> None:
71 super().__init__()
72 return
73
74 def setup_scene(self):
75 world = self.get_world()
76 # We add the task to the world here
77 world.add_task(FrankaPlaying(name="my_first_task"))
78 return
79
80 async def setup_post_load(self):
81 self._world = self.get_world()
82 # The world already called the setup_scene from the task (with first reset of the world)
83 # so we can retrieve the task objects
84 self._franka = self._world.scene.get_object("fancy_franka")
85 self._controller = PickPlaceController(
86 name="pick_place_controller",
87 gripper=self._franka.gripper,
88 robot_articulation=self._franka,
89 )
90 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
91 await self._world.play_async()
92 return
93
94 async def setup_post_reset(self):
95 self._controller.reset()
96 await self._world.play_async()
97 return
98
99 def physics_step(self, step_size):
100 # Gets all the tasks observations
101 current_observations = self._world.get_observations()
102 actions = self._controller.forward(
103 picking_position=current_observations["fancy_cube"]["position"],
104 placing_position=current_observations["fancy_cube"]["goal_position"],
105 current_joint_positions=current_observations["fancy_franka"]["joint_positions"],
106 )
107 self._franka.apply_action(actions)
108 if self._controller.is_done():
109 self._world.pause()
110 return
```

## Use the Pick and Place Task
NVIDIA Isaac Sim also provides different tasks under the many robot extensions. Re-write the previous code using the `PickPlace` class.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.robot.manipulators.examples.franka.tasks import PickPlace
3from isaacsim.robot.manipulators.examples.franka.controllers import PickPlaceController
4
5
6class HelloWorld(BaseSample):
7 def __init__(self) -> None:
8 super().__init__()
9 return
10
11 def setup_scene(self):
12 world = self.get_world()
13 # We add the task to the world here
14 world.add_task(PickPlace(name="awesome_task"))
15 return
16
17 async def setup_post_load(self):
18 self._world = self.get_world()
19 # The world already called the setup_scene from the task so
20 # we can retrieve the task objects
21 # Each defined task in the robot extensions
22 # has set_params and get_params to allow for changing tasks during
23 # simulation, {"task_param_name": "value": [value], "modifiable": [True/ False]}
24 task_params = self._world.get_task("awesome_task").get_params()
25 self._franka = self._world.scene.get_object(task_params["robot_name"]["value"])
26 self._cube_name = task_params["cube_name"]["value"]
27 self._controller = PickPlaceController(
28 name="pick_place_controller",
29 gripper=self._franka.gripper,
30 robot_articulation=self._franka,
31 )
32 self._world.add_physics_callback("sim_step", callback_fn=self.physics_step)
33 await self._world.play_async()
34 return
35
36 async def setup_post_reset(self):
37 self._controller.reset()
38 await self._world.play_async()
39 return
40
41 def physics_step(self, step_size):
42 # Gets all the tasks observations
43 current_observations = self._world.get_observations()
44 actions = self._controller.forward(
45 picking_position=current_observations[self._cube_name]["position"],
46 placing_position=current_observations[self._cube_name]["target_position"],
47 current_joint_positions=current_observations[self._franka.name]["joint_positions"],
48 )
49 self._franka.apply_action(actions)
50 if self._controller.is_done():
51 self._world.pause()
52 return
```

## Summary
This tutorial covered the following topics:

- Adding a manipulator robot to the scene.

- Using Controller Classes from NVIDIA Isaac Sim.

- Modularizing the creation of scene objects and interacting with them through Task Classes.

- Using Task Classes from the robot extensions in NVIDIA Isaac Sim.

### Next Steps
Continue to the next tutorial in our Essential Tutorials series, Adding Multiple Robots , to learn how to add multiple robots to the simulation.
