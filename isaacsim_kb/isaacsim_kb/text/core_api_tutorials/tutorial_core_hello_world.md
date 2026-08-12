<!-- source: core_api_tutorials/tutorial_core_hello_world.html | title: Hello World — Isaac Sim Documentation -->

# Hello World
NVIDIA Omniverse™ Kit , the toolkit that NVIDIA Isaac Sim uses to build its applications, provides a Python interpreter for scripting. This means every single GUI command, as well as many additional functions are available as Python APIs. However, the learning curve for interfacing with Omniverse Kit using Pixar’s USD Python API is steep and steps are frequently tedious. Therefore we’ve provided a set of APIs that are designed to be used in robotics applications, APIs that abstract away the complexity of USD APIs and merge multiple steps into one for frequently performed tasks.
In this tutorial, we will present the concepts of Core APIs and how to use them. We will start with adding a cube to an empty stage, and we’ll build upon it to create a scene with multiple robots executing multiple tasks simultaneously, as seen below.

## Learning Objectives
This tutorial series introduces the Core API. After this tutorial, you learn:

- Creating a World and Scene as defined by the Core API.

- How to add a rigid body to the Stage and simulate it using Python in NVIDIA Isaac Sim.

- The difference between running Python in an Extension Workflow vs a Standalone Workflow, and in Jupyter Notebook.

10-15 Minute Tutorial

## Getting Started
Prerequisites

- Intermediate knowledge in Python and asynchronous programming is required for this tutorial.

- Please download and install Visual Studio Code prior to beginning this tutorial.

- Please review Quick Tutorials and Workflows prior to beginning this tutorial.

Begin by opening the Hello World example. First activate Windows > Examples > Robotics Examples which will open the `Robotics Examples` tab.

- Click Robotics Examples > General > Hello World.

- Verify that the window for the Hello World example extension is visible in the workspace.

- Click the Open Source Code button to launch the source code for editing in Visual Studio Code .

- Click the Open Containing Folder button to open the directory containing the example files.

This folder contains three files: `hello_world.py`, `hello_world_extension.py`, and `__init__.py`.
The `hello_world.py` script is where the logic of the application will be added, while the UI elements of the application will be added in `hello_world_extension.py` script and thus linked to the logic.

- Click the LOAD button to load the World.

- click File > New From Stage Template > Empty to create a new stage, click Don’t Save when prompted to save the current stage.

- Click the LOAD button to load the World again.

- Open `hello_world.py` and press “Ctrl+S” to use the hot-reload feature. You will notice that the menu disappears from the workspace (because it was restarted).

- Open the example menu again and click the LOAD button.

Now you can begin adding to this example.

## Code Overview
This example inherits from BaseSample, which is a boilerplate extension application that sets up the basics for every robotics extension application. The following are a few examples of the actions BaseSample performs:

- Loading the world with its corresponding assets using a button.

- Clearing the world when a new stage is created.

- Resetting the world’s objects to their default states.

- Handling hot reloading.

World is the core class that enables you to interact with the simulator in an easy and modular way. It handles many time-related events such as adding callbacks, stepping physics, resetting the scene, adding tasks (this will be covered later in Adding a Manipulator Robot ), etc.
A world contains an instance of a Scene . The Scene class manages simulation assets of interest in the USD Stage . It provides an easy API to add, manipulate, inspect, and reset different USD assets in the stage.

```
1from isaacsim.examples.interactive.base_sample import BaseSample #boiler plate of a robotics extension application
2
3class HelloWorld(BaseSample):
4 def __init__(self) -> None:
5 super().__init__()
6 return
7
8 # This function is called to setup the assets in the scene for the first time
9 # Class variables should not be assigned here, since this function is not called
10 # after a hot-reload, its only called to load the world starting from an EMPTY stage
11 def setup_scene(self):
12 # A world is defined in the BaseSample, can be accessed everywhere EXCEPT __init__
13 world = self.get_world()
14 world.scene.add_default_ground_plane() # adds a default ground plane to the scene
15 return
```

### Singleton World
World is a Singleton, which means only one World can exist while running NVIDIA Isaac Sim. The code below demonstrates how to retrieve the current instance of the World across different files and extensions.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2from isaacsim.core.api import World
3
4class HelloWorld(BaseSample):
5 def __init__(self) -> None:
6 super().__init__()
7 return
8
9 def setup_scene(self):
10 world = World.instance()
11 world.scene.add_default_ground_plane()
12 return
```

## Adding to the Scene
Use the Python API to add a cube as a rigid body to the scene.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2import numpy as np
3# Can be used to create a new cube or to point to an already existing cube in stage.
4from isaacsim.core.api.objects import DynamicCuboid
5
6class HelloWorld(BaseSample):
7 def __init__(self) -> None:
8 super().__init__()
9 return
10
11 def setup_scene(self):
12 world = self.get_world()
13 world.scene.add_default_ground_plane()
14 fancy_cube = world.scene.add(
15 DynamicCuboid(
16 prim_path="/World/random_cube", # The prim path of the cube in the USD stage
17 name="fancy_cube", # The unique name used to retrieve the object from the scene later on
18 position=np.array([0, 0, 1.0]), # Using the current stage units which is in meters by default.
19 scale=np.array([0.5015, 0.5015, 0.5015]), # most arguments accept mainly numpy arrays.
20 color=np.array([0, 0, 1.0]), # RGB channels, going from 0-1
21 ))
22 return
```

- Press Ctrl+S to save the code and hot-reload NVIDIA Isaac Sim.

- Open the menu again.

- click File > New From Stage Template > Empty, then the LOAD button. You need to perform this action if you change anything in the setup_scene. Otherwise, you only need to press the LOAD button.

- Press the PLAY button to start simulating the dynamic cube and see it falling.

Note
Every time the code is edited or changed, press Ctrl+S to save the code and hot-reload NVIDIA Isaac Sim.

## Inspecting Object Properties
Print the world pose and velocity of the cube. The highlighted lines show how you can get the objects using the name and query their properties.

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2import numpy as np
3from isaacsim.core.api.objects import DynamicCuboid
4
5class HelloWorld(BaseSample):
6 def __init__(self) -> None:
7 super().__init__()
8 return
9
10 def setup_scene(self):
11 world = self.get_world()
12 world.scene.add_default_ground_plane()
13 fancy_cube = world.scene.add(
14 DynamicCuboid(
15 prim_path="/World/random_cube",
16 name="fancy_cube",
17 position=np.array([0, 0, 1.0]),
18 scale=np.array([0.5015, 0.5015, 0.5015]),
19 color=np.array([0, 0, 1.0]),
20 ))
21 return
22
23 # Here we assign the class's variables
24 # this function is called after load button is pressed
25 # regardless starting from an empty stage or not
26 # this is called after setup_scene and after
27 # one physics time step to propagate appropriate
28 # physics handles which are needed to retrieve
29 # many physical properties of the different objects
30 async def setup_post_load(self):
31 self._world = self.get_world()
32 self._cube = self._world.scene.get_object("fancy_cube")
33 position, orientation = self._cube.get_world_pose()
34 linear_velocity = self._cube.get_linear_velocity()
35 # will be shown on terminal
36 print("Cube position is : " + str(position))
37 print("Cube's orientation is : " + str(orientation))
38 print("Cube's linear velocity is : " + str(linear_velocity))
39 return
```

### Continuously Inspecting the Object Properties during Simulation
Print the world pose and velocity of the cube during simulation at every physics step executed. As mentioned in Workflows , in this workflow the application is running asynchronously and can’t control when to step physics. However, you can add callbacks to ensure certain things happen before certain events.
Add a physics callback as follows:

```
1from isaacsim.examples.interactive.base_sample import BaseSample
2import numpy as np
3from isaacsim.core.api.objects import DynamicCuboid
4
5class HelloWorld(BaseSample):
6 def __init__(self) -> None:
7 super().__init__()
8 return
9
10 def setup_scene(self):
11 world = self.get_world()
12 world.scene.add_default_ground_plane()
13 fancy_cube = world.scene.add(
14 DynamicCuboid(
15 prim_path="/World/random_cube",
16 name="fancy_cube",
17 position=np.array([0, 0, 1.0]),
18 scale=np.array([0.5015, 0.5015, 0.5015]),
19 color=np.array([0, 0, 1.0]),
20 ))
21 return
22
23 async def setup_post_load(self):
24 self._world = self.get_world()
25 self._cube = self._world.scene.get_object("fancy_cube")
26 self._world.add_physics_callback("sim_step", callback_fn=self.print_cube_info) #callback names have to be unique
27 return
28
29 # here we define the physics callback to be called before each physics step, all physics callbacks must take
30 # step_size as an argument
31 def print_cube_info(self, step_size):
32 position, orientation = self._cube.get_world_pose()
33 linear_velocity = self._cube.get_linear_velocity()
34 # will be shown on terminal
35 print("Cube position is : " + str(position))
36 print("Cube's orientation is : " + str(orientation))
37 print("Cube's linear velocity is : " + str(linear_velocity))
```

## Converting the Example to a Standalone Application
Note

- On windows use python.bat instead of python.sh

- The details of how python.sh works below are similar to how python.bat works

As mentioned in Workflows , in this workflow, the robotics application is started when launched from Python right away, and you can control when to step physics and rendering.

- Open a new `my_application.py` file and add the following:

```
1#launch Isaac Sim before any other imports
2#default first two lines in any standalone application
3from isaacsim import SimulationApp
4simulation_app = SimulationApp({"headless": False}) # we can also run as headless.
5
6from isaacsim.core.api import World
7from isaacsim.core.api.objects import DynamicCuboid
8import numpy as np
9
10world = World()
11world.scene.add_default_ground_plane()
12fancy_cube = world.scene.add(
13 DynamicCuboid(
14 prim_path="/World/random_cube",
15 name="fancy_cube",
16 position=np.array([0, 0, 1.0]),
17 scale=np.array([0.5015, 0.5015, 0.5015]),
18 color=np.array([0, 0, 1.0]),
19 ))
20# Resetting the world needs to be called before querying anything related to an articulation specifically.
21# Its recommended to always do a reset after adding your assets, for physics handles to be propagated properly
22world.reset()
23for i in range(500):
24 position, orientation = fancy_cube.get_world_pose()
25 linear_velocity = fancy_cube.get_linear_velocity()
26 # will be shown on terminal
27 print("Cube position is : " + str(position))
28 print("Cube's orientation is : " + str(orientation))
29 print("Cube's linear velocity is : " + str(linear_velocity))
30 # we have control over stepping physics and rendering in this workflow
31 # things run in sync
32 world.step(render=True) # execute one physics step and one rendering step
33
34simulation_app.close() # close Isaac Sim
```

- Run it using `./python.sh ./exts/isaacsim.examples.interactive/isaacsim/examples/interactive/user_examples/my_application.py`.

## Summary
This tutorial covered the following topics:

- Overview of the `World` and `Scene` classes.

- Adding content to the Scene via Python.

- Adding callbacks.

- Accessing dynamic properties for objects.

- The main differences in a standalone application.

### Next Steps
Continue to Hello Robot to learn how to add a robot to the simulation.
Note
The next tutorials will be developed mainly using the extensions application workflow. However, conversion to other workflows is similar given what was covered in this tutorial.
