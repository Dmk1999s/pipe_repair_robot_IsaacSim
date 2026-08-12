<!-- source: cortex_tutorials/tutorial_cortex_7_cortex_extension.html | title: Building Cortex Based Extensions — Isaac Sim Documentation -->

# Building Cortex Based Extensions
This tutorial covers the use of Cortex in a custom extension running directly on Isaac Sim App instead of the Python SimulationApp. For this we use the same behaviors from Walkthrough: Franka Block Stacking and Walkthrough: UR10 Bin Stacking . To use Cortex, similar to Hello Robot , but we create a modified version of the Base Sample that replaces the Core World with a Cortex World:

```
import gc
from abc import abstractmethod

from isaacsim.core.api import World
from isaacsim.core.api.scenes.scene import Scene
from isaacsim.core.api.tasks.base_task import BaseTask
from isaacsim.core.utils.stage import create_new_stage_async, update_stage_async
from isaacsim.cortex.framework.cortex_world import CortexWorld
from isaacsim.examples.interactive import base_sample

class CortexBase(base_sample.BaseSample):
async def load_world_async(self):
"""
Function called when clicking load buttton.
The difference between this class and Base Sample is that we initialize a CortexWorld specialization.
"""
if CortexWorld.instance() is None:
await create_new_stage_async()
self._world = CortexWorld(**self._world_settings)
await self._world.initialize_simulation_context_async()
self.setup_scene()
else:
self._world = CortexWorld.instance()
self._current_tasks = self._world.get_current_tasks()
await self._world.reset_async()
await self._world.pause_async()
await self.setup_post_load()
if len(self._current_tasks) > 0:
self._world.add_physics_callback("tasks_step", self._world.step_async)
return
```
Now, we need to define the world Task, to define how the world behaves, and the Robot Cortex task. That code is equivalent to the standalone examples, except that the functions to step, start and reset the simulation are moved on the callbacks for the task step, and reset callbacks.

## Franka Cortex Examples
The UI is defined in the `exts/isaacsim.examples.interactive/isaacsim/examples/interactive/franka_cortex/franka_cortex_extension.py`, This sample shows how to load many different decider networks for Franka.
First activate Windows > Examples > Robotics Examples which will open the `Robotics Examples` tab. To load the sample navigate to Robotics Examples > Cortex > Franka Cortex Examples.
First, select the behavior you want from the drop-down, then click on LOAD. To begin the decider network, click on START.
[image: Franka Cortex Examples.]On the Diagnostic monitor, you can check the decision stack. Due to the different nature of the tasks, the task diagnostics is showed as a diagnostic message, containing the important information for each task.
Note
Pressing STOP, then PLAY in this workflow might not reset the world properly. Use the RESET button instead.

### Hot-Swapping Behaviors
Cortex allows you to select different behavior policies to run on your robot. In this example you can select which policy is running on the robot, even while it’s executing the previous policy. It will change the behavior to conform to the new policy. To do so, choose a new behavior in the drop-down.

## UR10 Palletizing Example
The UI is defined in the `exts/isaacsim.examples.interactive/isaacsim/examples/interactive/ur10_palletizing/ur10_palletizing_extension.py`.
To load the sample navigate to Robotics Examples > Cortex > UR10 Palletizing.
Click on LOAD to load all the assets and setup the scene. Then, Click on START PALLETIZING to begin the task.
On the Diagnostics section, you can inspect the Cortex Decision stack for the robot, and the flags used by the decision network to move forward to the next steps.
[image: Isaac UR10 Palletizing.]
