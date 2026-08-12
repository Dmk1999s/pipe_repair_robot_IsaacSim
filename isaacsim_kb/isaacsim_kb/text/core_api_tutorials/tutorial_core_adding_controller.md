<!-- source: core_api_tutorials/tutorial_core_adding_controller.html | title: Adding a Controller — Isaac Sim Documentation -->

# Adding a Controller

## Learning Objectives
This tutorial describes how to create and use a custom controller to move a mobile robot. It then describes how to use the controllers available in NVIDIA Isaac Sim. After this tutorial, you should be more comfortable with adding and controlling robots in NVIDIA Isaac Sim.
10 Minute Tutorial

## Getting Started
Prerequisites

- Review Hello Robot prior to beginning this tutorial.

Begin with the source code open from the Hello Robot tutorial, by clicking the Open Source Code button in the Hello World Example window.
Note
Pressing STOP, then PLAY in this workflow might not reset the world properly. Use the RESET button instead.

## Creating a Custom Controller
First, code an open-loop controller that uses the unicycle model for differential drive. Controllers in NVIDIA Isaac Sim inherit from the BaseController interface. You will need to implement a forward method, and it has to return an ArticulationAction type.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.utils.nucleus import get_assets_root_path
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4from isaacsim.core.utils.types import ArticulationAction
5from isaacsim.core.api.controllers import BaseController
6import numpy as np
7
8
9class CoolController(BaseController):
10 def __init__(self):
11 super().__init__(name="my_cool_controller")
12 # An open loop controller that uses a unicycle model
13 self._wheel_radius = 0.03
14 self._wheel_base = 0.1125
15 return
16
17 def forward(self, command):
18 # command will have two elements, first element is the forward velocity
19 # second element is the angular velocity (yaw only).
20 joint_velocities = [0.0, 0.0]
21 joint_velocities[0] = ((2 * command[0]) - (command[1] * self._wheel_base)) / (2 * self._wheel_radius)
22 joint_velocities[1] = ((2 * command[0]) + (command[1] * self._wheel_base)) / (2 * self._wheel_radius)
23 # A controller has to return an ArticulationAction
24 return ArticulationAction(joint_velocities=joint_velocities)
25
26
27class HelloWorld(BaseSample):
28 def __init__(self) -> None:
29 super().__init__()
30 return
31
32 def setup_scene(self):
33 world = self.get_world()
34 world.scene.add_default_ground_plane()
35 assets_root_path = get_assets_root_path()
36 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
37 world.scene.add(
38 WheeledRobot(
39 prim_path="/World/Fancy_Robot",
40 name="fancy_robot",
41 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
42 create_robot=True,
43 usd_path=jetbot_asset_path,
44 )
45 )
46 return
47
48 async def setup_post_load(self):
49 self._world = self.get_world()
50 self._jetbot = self._world.scene.get_object("fancy_robot")
51 self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
52 # Initialize our controller after load and the first reset
53 self._my_controller = CoolController()
54 return
55
56 def send_robot_actions(self, step_size):
57 #apply the actions calculated by the controller
58 self._jetbot.apply_action(self._my_controller.forward(command=[0.20, np.pi / 4]))
59 return
```

## Using the Available Controllers
NVIDIA Isaac Sim also provides different controllers under many robot extensions. Re-write the previous code using the `DifferentialController` class and add a `WheelBasePoseController`.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.utils.nucleus import get_assets_root_path
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4# This extension includes several generic controllers that could be used with multiple robots
5from isaacsim.robot.wheeled_robots.controllers.wheel_base_pose_controller import WheelBasePoseController
6# Robot specific controller
7from isaacsim.robot.wheeled_robots.controllers.differential_controller import DifferentialController
8import numpy as np
9
10
11class HelloWorld(BaseSample):
12 def __init__(self) -> None:
13 super().__init__()
14 return
15
16 def setup_scene(self):
17 world = self.get_world()
18 world.scene.add_default_ground_plane()
19 assets_root_path = get_assets_root_path()
20 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
21 world.scene.add(
22 WheeledRobot(
23 prim_path="/World/Fancy_Robot",
24 name="fancy_robot",
25 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
26 create_robot=True,
27 usd_path=jetbot_asset_path,
28 )
29 )
30 return
31
32 async def setup_post_load(self):
33 self._world = self.get_world()
34 self._jetbot = self._world.scene.get_object("fancy_robot")
35 self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
36 # Initialize our controller after load and the first reset
37 self._my_controller = WheelBasePoseController(name="cool_controller",
38 open_loop_wheel_controller=
39 DifferentialController(name="simple_control",
40 wheel_radius=0.03, wheel_base=0.1125),
41 is_holonomic=False)
42 return
43
44 def send_robot_actions(self, step_size):
45 position, orientation = self._jetbot.get_world_pose()
46 self._jetbot.apply_action(self._my_controller.forward(start_position=position,
47 start_orientation=orientation,
48 goal_position=np.array([0.8, 0.8])))
49 return
```

Press `Ctrl+S` to save and hot reload the example. Then press the LOAD button to reload the scene.

## Summary
This tutorial covered the following topics:

- Creating a custom controller to move a mobile robot

- Using Controller classes from NVIDIA Isaac Sim

### Next Steps
Continue to the next tutorial in the Essential Tutorials series, Adding a Manipulator Robot , to learn how to add a manipulator robot to the simulation.
