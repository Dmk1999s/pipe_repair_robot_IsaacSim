<!-- source: replicator_tutorials/tutorial_replicator_modular_scripting.html | title: Modular Behavior Scripting — Isaac Sim Documentation -->

# Modular Behavior Scripting

## Overview
This tutorial introduces the `isaacsim.replicator.behavior` extension, providing multiple examples of modular behavior scripts in Isaac Sim Replicator for synthetic data generation (SDG). By utilizing Behavior Scripts (Python Scripting Component) , reusable, shareable, and easily modifiable behaviors can be developed and attached to prims in a USD stage, acting as randomizers or custom smart-asset behaviors.
The behavior script examples can be found under:
`/exts/isaacsim.replicator.behavior/isaacsim/replicator/behavior/behaviors/*`

### Learning Objectives
After completing this tutorial, you will understand how to:

- Use pre-built behavior scripts for common synthetic data generation tasks, including:

- Location Randomizer - randomizes prim positions within specified bounds for object placement variety

- Rotation Randomizer - applies random rotations to enhance orientation diversity in datasets

- Look At Behavior - makes prims continuously face target locations or other prims for camera tracking

- Light Randomizer - randomizes light properties like color and intensity to simulate different lighting conditions

- Texture Randomizer - applies random textures to materials for increased visual variety

- Volume Stack Randomizer - uses physics simulation to randomly stack objects for realistic arrangements

- Understand behavior script architecture - how modular Python scripts attach to prims and can be customized through exposed USD attributes, with configurable parameters like update intervals and randomization ranges

- Control behavior execution - configure behaviors to run on timeline events (start, update, stop) or trigger them independently using custom events for advanced workflows

- Create custom behavior scripts - develop your own behaviors using the provided templates and base classes for specific synthetic data generation needs

- Build complex SDG pipelines - combine multiple behaviors, simulations, and events to create sophisticated data generation workflows, such as physics-based object stacking followed by automated data capture

### Prerequisites
It is recommended that you have a basic understanding of the following concepts before proceeding with the tutorial:

- USD and Isaac Sim APIs for creating and manipulating USD stages

- Python Scripting Component in Isaac Sim

- The timeline and custom events system

- omni.replicator and its Isaac Sim tutorials for synthetic data generation

- Writers and annotators for data capture

- Running scripts using the Script Editor to setup and run pipelines

### Demonstration
The example section provides a demonstration of how to use the behavior scripts to create a custom synthetic data generation pipeline:

### Behavior Scripts
Behavior Scripts are modular Python scripts attached to prims in a USD stage. By default, they include template code that responds to timeline events such as start, pause, stop, and update. These scripts define specific behaviors or randomizations applied to prims during simulation or data generation.
Attaching scripts directly to prims integrates the behaviors into the USD, making them modular because scripts can be easily attached, detached, or swapped on prims without altering core logic. They are sharable because behaviors can be embedded within assets and shared across different projects or stages.
They are configurable because variables can be exposed through USD attributes for customization without modifying the script code. Additionally, they are persistent; because scripts reside on the prims, they persist with the USD stage and can be versioned and managed accordingly.
The advantages of behavior scripts include reusability, allowing them to be written once and reused across multiple prims or projects. They offer encapsulation by containing behavior logic within the prims, reducing external dependencies. They provide interactivity because parameters can be adjusted through the UI, enabling modifications without programming. Finally, they ensure integration by becoming an integral part of the asset, which maintains consistency across different environments.
[image: Behavior Scripts with Exposed Variables]

### Exposing Variables Through USD Attributes
To enhance flexibility and accessibility, the input parameters in the provided behavior scripts examples can be exposed as USD attributes on prims. This approach allows you to modify behavior parameters directly from the UI without altering the script code.
The benefits of exposing variables include customization, interactivity, and consistency. Parameters such as target locations, ranges, or other settings can be adjusted per prim instance, using the UI to tweak behaviors and observe immediate effects, while maintaining a uniform interface for modifying behaviors across different scripts.
The exposed variables are implemented using the USD API to create custom attributes with appropriate namespaces on the prim. These attributes are then read by the behavior scripts during execution to adjust their logic accordingly.
The UI implementation for exposing the variables is done in `isaacsim.replicator.behavior.ui`. It extends the Property panel of the selected prims in the stage with a custom section for the exposed variables. The UI is automatically generated based on the exposed variables defined in the behavior script, displaying them as editable fields in the generated widget.
Example of Exposed Variables Definition:

```
VARIABLES_TO_EXPOSE = [
{
"attr_name": "targetLocation",
"attr_type": Sdf.ValueTypeNames.Vector3d,
"default_value": Gf.Vec3d(0.0, 0.0, 0.0),
"doc": "The 3D vector specifying the location to look at.",
},
{
"attr_name": "targetPrimPath",
"attr_type": Sdf.ValueTypeNames.String,
"default_value": "",
"doc": "The path of the target prim to look at. If specified, it has priority over the target location.",
},
# Additional variables...
]
```

### Custom Event-Based Behavior Scripts
While behavior scripts are timeline-based by default, some behaviors need to operate independently of the simulation timeline. Event-based scripting allows behaviors to be triggered by custom events , providing greater control over when and how they execute. This is achieved by skipping the default behavior functions and instead listening to and publishing custom events.
Custom events are defined and managed within Omniverse using an event bus system, enabling scripts to publish or subscribe to these events and facilitating communication between different components or behaviors.
Event-based scripting offers flexibility by allowing customization of when behaviors are executed, independent of the simulation timeline. It enhances modularity by decoupling behaviors from the core simulation loop, making them more modular. Additionally, it improves scalability by managing complex workflows through orchestrating multiple behaviors via events.
For example, the volume_stack_randomizer.py script randomizes the stacking of objects by simulating physics before the simulation starts. By using custom events, behaviors can be triggered before the simulation, execution flow can be controlled by starting, stopping, or resetting behaviors based on specific events rather than timeline updates, and performance can be enhanced by avoiding unnecessary computations during each simulation frame through decoupling certain behaviors.

## Script Examples
In this section, various behavior scripts available in the `isaacsim.replicator.behavior` extension are explored. Each script provides specific functionality that can enhance synthetic data generation workflows. The scripts are designed to be modular, reusable, and customizable through exposed variables.
The folder path for the behavior scripts is:
`/exts/isaacsim.replicator.behavior/isaacsim/replicator/behavior/behaviors/*`

### Location Randomizer
The `location_randomizer.py` script randomizes the location of prims within specified bounds during runtime, providing position variability for enhanced synthetic datasets.

### Rotation Randomizer
The `rotation_randomizer.py` script applies random rotations to prims during runtime, enhancing orientation diversity in synthetic datasets.

### Look At Behavior
The `look_at_behavior.py` script orients prims to continuously face a specified target, ideal for camera tracking and sensor alignment.

### Light Randomizer
The `light_randomizer.py` script randomizes light properties to simulate different lighting conditions for enhanced scene variability.

### Texture Randomizer
The `texture_randomizer.py` script randomly applies textures to materials for increased visual variety of objects.

### Volume Stack Randomizer
The `volume_stack_randomizer.py` script uses physics simulation to randomly stack objects for realistic object arrangements.

### Templates
This section provides template scripts that serve as starting points for creating custom behaviors.
Available TemplatesTemplate Scripts:

- example_behavior.py: Basic template with boilerplate code for new behaviors

- base_behavior.py and example_base_behavior.py: Demonstrate base behavior class inheritance for structured development

- example_custom_event_behavior.py: Shows implementation of event-based behaviors

Key Template Features:

- Variable Exposure: Demonstrates exposing variables as USD attributes for UI customization

- Behavior Structure: Provides necessary methods (on_init, on_play, on_update, on_stop, on_destroy) for timeline integration

- Extensibility: Base behavior classes enable easy extension and reuse in new behaviors

- Event Integration: Shows both timeline-based and custom event-based approaches

## Example
Below is an example demonstrating the use of behavior scripts to set up and run synthetic data generation in Isaac Sim. It showcases how to utilize behavior scripts for stacking simulations, texture randomization, light behavior, and camera tracking, ultimately capturing synthetic data with randomized scene configurations.
Key Highlights of the Example:

- Volume Stacking Simulation: Randomly stack assets using physics simulation to create realistic arrangements.

- Texture Randomization: Apply randomized textures to assets for scene diversity.

- Light and Camera Behaviors: Add randomization to light properties and make the camera track a specific target.

- Synthetic Data Capture: Generate and save synthetic images with the configured behaviors.

Example Script:
The demo script can be run directly from the Script Editor :
Behavior script-based SDG script:
```
import asyncio
import inspect
import os
import random

import omni.kit.app
import omni.replicator.core as rep
import omni.timeline
import omni.usd
from isaacsim.core.utils.semantics import add_labels, remove_labels
from isaacsim.replicator.behavior.behaviors import (
LightRandomizer,
LocationRandomizer,
LookAtBehavior,
RotationRandomizer,
TextureRandomizer,
VolumeStackRandomizer,
)
from isaacsim.replicator.behavior.global_variables import EXPOSED_ATTR_NS
from isaacsim.replicator.behavior.utils.behavior_utils import (
add_behavior_script_with_parameters_async,
publish_event_and_wait_for_completion_async,
)
from isaacsim.storage.native import get_assets_root_path_async
from pxr import Gf, UsdGeom

async def setup_and_run_stacking_simulation_async(prim):
STACK_ASSETS_CSV = (
"/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxC_01.usd,"
"/Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_01.usd,"
"/Isaac/Props/KLT_Bin/small_KLT_visual.usd,"
)

# Add the behavior script with custom parameters
script_path = inspect.getfile(VolumeStackRandomizer)
parameters = {
f"{EXPOSED_ATTR_NS}:{VolumeStackRandomizer.BEHAVIOR_NS}:assets:csv": STACK_ASSETS_CSV,
f"{EXPOSED_ATTR_NS}:{VolumeStackRandomizer.BEHAVIOR_NS}:assets:numRange": Gf.Vec2i(2, 15),
}
await add_behavior_script_with_parameters_async(prim, script_path, parameters)

# Helper function to handle publishing and waiting for events
async def handle_event(action, expected_state, max_wait):
return await publish_event_and_wait_for_completion_async(
publish_payload={"prim_path": prim.GetPath(), "action": action},
expected_payload={"prim_path": prim.GetPath(), "state_name": expected_state},
publish_event_name=VolumeStackRandomizer.EVENT_NAME_IN,
subscribe_event_name=VolumeStackRandomizer.EVENT_NAME_OUT,
max_wait_updates=max_wait,
)

# Define and execute the stacking simulation steps
actions = [("reset", "RESET", 10), ("setup", "SETUP", 500), ("run", "FINISHED", 1500)]
for action, state, wait in actions:
print(f"Executing '{action}' and waiting for state '{state}'...")
if not await handle_event(action, state, wait):
print(f"Failed to complete '{action}' with state '{state}'.")
return

print("Stacking simulation finished.")

async def setup_texture_randomizer_async(prim):
TEXTURE_ASSETS_CSV = (
"/Isaac/Materials/Textures/Patterns/nv_bamboo_desktop.jpg,"
"/Isaac/Materials/Textures/Patterns/nv_wood_boards_brown.jpg,"
"/Isaac/Materials/Textures/Patterns/nv_wooden_wall.jpg,"
)

script_path = inspect.getfile(TextureRandomizer)
parameters = {
f"{EXPOSED_ATTR_NS}:{TextureRandomizer.BEHAVIOR_NS}:interval": 5,
f"{EXPOSED_ATTR_NS}:{TextureRandomizer.BEHAVIOR_NS}:textures:csv": TEXTURE_ASSETS_CSV,
}
await add_behavior_script_with_parameters_async(prim, script_path, parameters)

async def setup_light_behaviors_async(prim):
# Light randomization
light_script_path = inspect.getfile(LightRandomizer)
light_parameters = {
f"{EXPOSED_ATTR_NS}:{LightRandomizer.BEHAVIOR_NS}:interval": 4,
f"{EXPOSED_ATTR_NS}:{LightRandomizer.BEHAVIOR_NS}:range:intensity": Gf.Vec2f(20000, 120000),
}
await add_behavior_script_with_parameters_async(prim, light_script_path, light_parameters)

# Location randomization
location_script_path = inspect.getfile(LocationRandomizer)
location_parameters = {
f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:interval": 2,
f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:minPosition": Gf.Vec3d(-1.25, -1.25, 0.0),
f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:maxPosition": Gf.Vec3d(1.25, 1.25, 0.0),
}
await add_behavior_script_with_parameters_async(prim, location_script_path, location_parameters)

async def setup_target_asset_behaviors_async(prim):
# Rotation randomization with default parameters
rotation_script_path = inspect.getfile(RotationRandomizer)
await add_behavior_script_with_parameters_async(prim, rotation_script_path, {})

# Location randomization
location_script_path = inspect.getfile(LocationRandomizer)
location_parameters = {
f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:interval": 3,
f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:minPosition": Gf.Vec3d(-0.2, -0.2, -0.2),
f"{EXPOSED_ATTR_NS}:{LocationRandomizer.BEHAVIOR_NS}:range:maxPosition": Gf.Vec3d(0.2, 0.2, 0.2),
}
await add_behavior_script_with_parameters_async(prim, location_script_path, location_parameters)

async def setup_camera_behaviors_async(prim, target_prim_path):
# Look at behavior following the target asset
script_path = inspect.getfile(LookAtBehavior)
parameters = {
f"{EXPOSED_ATTR_NS}:{LookAtBehavior.BEHAVIOR_NS}:targetPrimPath": target_prim_path,
}
await add_behavior_script_with_parameters_async(prim, script_path, parameters)

async def setup_writer_and_capture_data_async(camera_path, num_captures):
# Create the writer and the render product
rp = rep.create.render_product(camera_path, (512, 512))
writer = rep.writers.get("BasicWriter")
output_directory = os.path.join(os.getcwd(), "out_behaviors_sdg")
print(f"output_directory: {output_directory}")
writer.initialize(output_dir=output_directory, rgb=True)
writer.attach(rp)

# Disable capture on play, data is captured manually using the step function
rep.orchestrator.set_capture_on_play(False)

# Start the timeline for the behavior scripts to run
timeline = omni.timeline.get_timeline_interface()
timeline.play()
await omni.kit.app.get_app().next_update_async()

# Capture frames
for i in range(num_captures):
# Advance the app (including the timeline)
await omni.kit.app.get_app().next_update_async()

# Capture and write frame
print(f"Capturing frame {i} at time {timeline.get_current_time():.4f}")
await rep.orchestrator.step_async(rt_subframes=32, delta_time=0.0, pause_timeline=False)

# Stop the timeline (and the behavior scripts triggering)
timeline.stop()

# Free the renderer resources
writer.detach()
rp.destroy()

# Make sure all the frames are written from the backend queue
await rep.orchestrator.wait_until_complete_async()

async def run_example_async():
STAGE_URL = "/Isaac/Samples/Replicator/Stage/warehouse_pallets_behavior_scripts.usd"
PALLETS_ROOT_PATH = "/Root/Pallets"
LIGHTS_ROOT_PATH = "/Root/Lights"
CAMERA_PATH = "/Root/Camera_01"
TARGET_ASSET_URL = "/Isaac/Props/YCB/Axis_Aligned/035_power_drill.usd"
TARGET_ASSET_PATH = "/Root/Target"
TARGET_ASSET_LABEL = "power_drill"
TARGET_ASSET_LOCATION = (-1.5, 5.5, 1.5)

# Open stage
assets_root_path = await get_assets_root_path_async()
print(f"Opening stage from {assets_root_path + STAGE_URL}")
await omni.usd.get_context().open_stage_async(assets_root_path + STAGE_URL)
stage = omni.usd.get_context().get_stage()

# Check if all required prims exist in the stage
pallets_root_prim = stage.GetPrimAtPath(PALLETS_ROOT_PATH)
lights_root_prim = stage.GetPrimAtPath(LIGHTS_ROOT_PATH)
camera_prim = stage.GetPrimAtPath(CAMERA_PATH)
if not all([pallets_root_prim.IsValid(), lights_root_prim.IsValid(), camera_prim.IsValid()]):
print(f"Not all required prims exist in the stage.")
return

# Spawn the target asset at the requested location, label it with the target asset label
target_prim = stage.DefinePrim(TARGET_ASSET_PATH, "Xform")
target_prim.GetReferences().AddReference(assets_root_path + TARGET_ASSET_URL)
if not target_prim.HasAttribute("xformOp:translate"):
UsdGeom.Xformable(target_prim).AddTranslateOp()
target_prim.GetAttribute("xformOp:translate").Set(TARGET_ASSET_LOCATION)
remove_labels(target_prim, include_descendants=True)
add_labels(target_prim, labels=[TARGET_ASSET_LABEL], instance_name="class")

# Setup and run the stacking simulation before capturing the data
await setup_and_run_stacking_simulation_async(pallets_root_prim)

# Setup texture randomizer
await setup_texture_randomizer_async(pallets_root_prim)

# Setup the light behaviors
await setup_light_behaviors_async(lights_root_prim)

# Setup the target asset behaviors
await setup_target_asset_behaviors_async(target_prim)

# Setup the camera behaviors
await setup_camera_behaviors_async(camera_prim, str(target_prim.GetPath()))

# Setup the writer and capture the data, behavior scripts are triggered by running the timeline
await setup_writer_and_capture_data_async(camera_path=camera_prim.GetPath(), num_captures=6)

random.seed(10)
rep.set_global_seed(10)

asyncio.ensure_future(run_example_async())
```
