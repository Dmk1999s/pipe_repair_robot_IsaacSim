<!-- source: core_api_tutorials/tutorial_core_hello_robot.html | title: Hello Robot — Isaac Sim Documentation -->

# Hello Robot

## Learning Objectives
This tutorial details how to add and move a mobile robot in NVIDIA Isaac Sim in an extension application. After this tutorial, you will understand how to add a robot to the simulation and apply actions to its wheels using Python.
10-15 Minute Tutorial

## Getting Started
Prerequisites

- Review Hello World prior to beginning this tutorial.

Begin with the source code of the Awesome Example developed in the previous tutorial: Hello World .

## Adding a Robot
Begin by adding a NVIDIA Jetbot to the scene, which allows you to access the library of NVIDIA Isaac Sim robots, sensors, and environments located on a Omniverse Nucleus Server using Python, as well as navigate through it using the Content window.
Note
The server shown in these steps has been connected to in Workstation Setup . Follow these steps first before proceeding.

- Add the assets by simply dragging them to the stage window or the viewport.

- Try to do the same thing through Python in the Awesome Example.

- Create a new stage: File > new > Don’t Save

- Open the `extension_examples/user_examples/hello_world.py` file by clicking the Open Source Code button in the Awesome Example window.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.utils.nucleus import get_assets_root_path
3from isaacsim.core.utils.stage import add_reference_to_stage
4from isaacsim.core.api.robots import Robot
5import carb
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
16 # you configure a new server with /Isaac folder in it
17 assets_root_path = get_assets_root_path()
18 if assets_root_path is None:
19 # Use carb to log warnings, errors, and infos in your application (shown on terminal)
20 carb.log_error("Could not find nucleus server with /Isaac folder")
21 asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
22 # This will create a new XFormPrim and point it to the USD file as a reference
23 # Similar to how pointers work in memory
24 add_reference_to_stage(usd_path=asset_path, prim_path="/World/Fancy_Robot")
25 # Wrap the jetbot prim root under a Robot class and add it to the Scene
26 # to use high level api to set/ get attributes as well as initializing
27 # physics handles needed..etc.
28 # Note: this call doesn't create the Jetbot in the stage window, it was already
29 # created with the add_reference_to_stage
30 jetbot_robot = world.scene.add(Robot(prim_path="/World/Fancy_Robot", name="fancy_robot"))
31 # Note: before a reset is called, we can't access information related to an Articulation
32 # because physics handles are not initialized yet. setup_post_load is called after
33 # the first reset so we can do so there
34 print("Num of degrees of freedom before first reset: " + str(jetbot_robot.num_dof)) # prints None
35 return
36
37 async def setup_post_load(self):
38 self._world = self.get_world()
39 self._jetbot = self._world.scene.get_object("fancy_robot")
40 # Print info about the jetbot after the first reset is called
41 print("Num of degrees of freedom after first reset: " + str(self._jetbot.num_dof)) # prints 2
42 print("Joint Positions after first reset: " + str(self._jetbot.get_joint_positions()))
43 return
```

Press the PLAY button to start simulating the robot. Although it is being simulated, it is not moving. The next section walks through how to make the robot move.

## Move the Robot
In NVIDIA Isaac Sim, Robots are constructed of physically accurate articulated joints. Applying actions to these articulations make them move.
Next, apply random velocities to the Jetbot articulation controller to get it moving.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.utils.types import ArticulationAction
3from isaacsim.core.utils.nucleus import get_assets_root_path
4from isaacsim.core.utils.stage import add_reference_to_stage
5from isaacsim.core.api.robots import Robot
6import numpy as np
7import carb
8
9
10class HelloWorld(BaseSample):
11 def __init__(self) -> None:
12 super().__init__()
13 return
14
15 def setup_scene(self):
16 world = self.get_world()
17 world.scene.add_default_ground_plane()
18 assets_root_path = get_assets_root_path()
19 if assets_root_path is None:
20 carb.log_error("Could not find nucleus server with /Isaac folder")
21 asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
22 add_reference_to_stage(usd_path=asset_path, prim_path="/World/Fancy_Robot")
23 jetbot_robot = world.scene.add(Robot(prim_path="/World/Fancy_Robot", name="fancy_robot"))
24 return
25
26 async def setup_post_load(self):
27 self._world = self.get_world()
28 self._jetbot = self._world.scene.get_object("fancy_robot")
29 # This is an implicit PD controller of the jetbot/ articulation
30 # setting PD gains, applying actions, switching control modes..etc.
31 # can be done through this controller.
32 # Note: should be only called after the first reset happens to the world
33 self._jetbot_articulation_controller = self._jetbot.get_articulation_controller()
34 # Adding a physics callback to send the actions to apply actions with every
35 # physics step executed.
36 self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
37 return
38
39 def send_robot_actions(self, step_size):
40 # Every articulation controller has apply_action method
41 # which takes in ArticulationAction with joint_positions, joint_efforts and joint_velocities
42 # as optional args. It accepts numpy arrays of floats OR lists of floats and None
43 # None means that nothing is applied to this dof index in this step
44 # ALTERNATIVELY, same method is called from self._jetbot.apply_action(...)
45 self._jetbot_articulation_controller.apply_action(ArticulationAction(joint_positions=None,
46 joint_efforts=None,
47 joint_velocities=5 * np.random.rand(2,)))
48 return
```
Press the PLAY button to start simulating the robot.
Note
Pressing STOP, then PLAY in this workflow might not reset the world properly. Use the RESET button instead.

### Extra Practice
This example applies random velocities to the Jetbot articulation controller. Try the following exercises:

- Make the Jetbot move backwards.

- Make the Jetbot turn right.

- Make the Jetbot stop after 5 seconds.

## Using the WheeledRobot Class
NVIDIA Isaac Sim also has robot-specific extensions that provide further customized functions and access to other controllers and tasks (more on this later). Now you’ll re-write the previous code using the WheeledRobot class to make it simpler.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.utils.nucleus import get_assets_root_path
3from isaacsim.robot.wheeled_robots.robots import WheeledRobot
4from isaacsim.core.utils.types import ArticulationAction
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
16 assets_root_path = get_assets_root_path()
17 jetbot_asset_path = assets_root_path + "/Isaac/Robots/NVIDIA/Jetbot/jetbot.usd"
18 self._jetbot = world.scene.add(
19 WheeledRobot(
20 prim_path="/World/Fancy_Robot",
21 name="fancy_robot",
22 wheel_dof_names=["left_wheel_joint", "right_wheel_joint"],
23 create_robot=True,
24 usd_path=jetbot_asset_path,
25 )
26 )
27 return
28
29 async def setup_post_load(self):
30 self._world = self.get_world()
31 self._jetbot = self._world.scene.get_object("fancy_robot")
32 self._world.add_physics_callback("sending_actions", callback_fn=self.send_robot_actions)
33 return
34
35 def send_robot_actions(self, step_size):
36 self._jetbot.apply_wheel_actions(ArticulationAction(joint_positions=None,
37 joint_efforts=None,
38 joint_velocities=5 * np.random.rand(2,)))
39 return
```

## Summary
This tutorial covered the following topics:

- Adding NVIDIA Isaac Sim library components from a Nucleus Server

- Adding a `Robot` to the `World`

- Using a joint-level controller to articulate a `Robot`

- Using Robot classes

- Using Robot specific extensions

### Next Steps
Continue on to the next tutorial in the Essential Tutorials series, Adding a Controller , to learn how to add a controller to Jetbot.

### Further Learning
Nucleus Server

- For an overview of how to best leverage a Nucleus Server, see the Nucleus Overview in NVIDIA Omniverse tutorial.

Robot Specific Extensions

- NVIDIA Isaac Sim provides several robot extensions such as `isaacsim.robot.manipulators.examples.franka`, `isaacsim.robot.manipulators.examples.universal_robots`, and many more. To learn more, check out the standalone examples located at `standalone_examples/api/isaacsim.robot.manipulators/franka` and `standalone_examples/api/isaacsim.robot.manipulators/universal_robots/`.
