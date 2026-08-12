<!-- source: replicator_tutorials/tutorial_replicator_getting_started.html | title: Getting Started Scripts — Isaac Sim Documentation -->

# Getting Started Scripts
This guide outlines a series of example scripts designed to facilitate typical Isaac Sim Replicator workflows. The examples include both “asynchronous” usage through the Script Editor and “synchronous” usage through the Standalone Application . These scripts cover simulation-based scenarios and configurations for synthetic data generation (SDG).

## Prerequisites
Before starting with these examples, ensure you have:

- Basic understanding of Python programming

- Familiarity with USD (Universal Scene Description) concepts

- Access to NVIDIA Omniverse™ Isaac Sim

- Sufficient disk space for data capture (varies based on resolution and number of frames)

- GPU with sufficient memory for rendering (recommended: 8GB+)

## Setup and Configuration
This section introduces configurations typically used in such workflows.

## Orchestrator Step Function
In Replicator, the `orchestrator.step()` function is used to trigger the entire synthetic data generation (SDG) process, including executing randomizations and capturing data. For Isaac Sim workflows, this function is used solely to trigger data capture only, with randomization triggers assigned to custom events and manually activated.
The `step()` function has the following signature:

```
rep.orchestrator.step(rt_subframes: int = -1, pause_timeline: bool = True, delta_time: float = None)
```
Where:

- `rt_subframes`: Specifies the number of subframes to render. A value greater than 0 enables subframe generation, reducing rendering artifacts or allowing materials to load fully.

- `pause_timeline`: Pauses the timeline (if currently playing) after the step if set to `True`.

- `delta_time`: Specifies the time to advance the timeline during a step. Defaults to the timeline’s rate if `None`.

More details on graph-based replicator randomizers can be found in the Randomizer Details , and for custom Isaac Sim or USD API-based randomizations, refer to the Isaac Sim Randomizers Guide .

## Capture on Play Flag
By default, Replicator captures data every frame during playback. For Isaac Sim workflows, data capture is configured to occur at user-defined frames using the `step()` function. To achieve this, the capture-on-play flag is disabled:

```
import omni.replicator.core as rep
rep.orchestrator.set_capture_on_play(False)
# OR
import carb.settings
carb.settings.get_settings().set("/omni/replicator/captureOnPlay", False)
```

## RT Subframes Parameter
In scenarios where reducing temporal rendering artifacts is needed, such as ghosting caused by quickly moving or teleporting assets, or under weak lighting conditions, RTSubframes can be used to render the same frame multiple times. This pauses the simulation and renders additional subframes, improving rendering quality.
The `rt_subframes` parameter is typically set during the capture request in the `step()` function but can also be configured globally:

```
# Set the rt_subframes parameter for a specific capture step
rep.orchestrator.step(rt_subframes=4)

# Set the rt_subframes parameter globally
import carb.settings
carb.settings.get_settings().set("/omni/replicator/RTSubframes", 4)
```
Refer to the documentation examples for additional details.

## DLSS Quality Mode for SDG
When using Replicator for synthetic data generation (SDG) workflows, it is recommended to set the DLSS model to Quality mode to avoid rendering artifacts. At lower resolutions (especially below 600x600), the default Performance mode may cause issues such as transparent or incorrectly rendered edges in the generated images.

```
import carb.settings
# Set DLSS to Quality mode (2) for best SDG results (Options: 0 (Performance), 1 (Balanced), 2 (Quality), 3 (Auto))
carb.settings.get_settings().set("/rtx/post/dlss/execMode", 2)
```

## Custom Event Randomizations
To provide flexibility, replicator randomizers can be triggered independently using custom events. This is achieved by registering the randomizer trigger through `trigger.on_custom_event` and activating it with `utils.send_og_event`. For instance, the following example creates a randomization graph for a dome light and randomizes its color. The randomization graph is then triggered manually through its custom event name. The `step()` function does not trigger this randomization graph.

```
# Create a randomization graph for creating a dome light and randomizing its color
with rep.trigger.on_custom_event(event_name="randomize_dome_light_color"):
rep.create.light(light_type="Dome", color=rep.distribution.uniform((0, 0, 0), (1, 1, 1)))

# Trigger the randomization graph using its custom event name
rep.utils.send_og_event(event_name="randomize_dome_light_color")
```
An example snippet for custom events is also available here .

## Wait Until Complete
Ensuring that all data is fully written to disk before closing the application is essential to prevent data loss. High data throughput, such as from multiple cameras or large resolutions, may introduce I/O bottlenecks; refer to the I/O Optimization Guide for strategies to mitigate such issues.
The `wait_until_complete` function ensures that all writing tasks are finalized by waiting for the writer backend to complete its operations. This process allows the application to continue updating until all writing tasks are complete, safeguarding against potential data loss.

```
while not BackendDispatch.is_done_writing():
await omni.kit.app.get_app().next_update_async()
```

## Examples

### Data Capture: BasicWriter
This example demonstrates how to use the `BasicWriter` for data capture with RGB and bounding box annotators. It sets up a scene with a cube and a dome light, attaches semantic labels to the cube, and saves captured data to disk. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_01.py
```
The output directory will contain the captured data, including RGB images and bounding box annotations in `.npy` and `.json` formats:
[image: ../_images/isim_4.5_replicator_tut_external_getting_started_01.jpg]

### Custom Writer and Annotators with Multiple Cameras
This example demonstrates data capture by creating a custom writer to access annotator data such as camera parameters and 3D bounding boxes. It configures two cameras (custom and viewport perspective), uses annotators to access data directly, writes data to disk using `PoseWriter`. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_02.py
```
The output directory will contain the captured data, including RGB with the 3D bounding box annotations as overlays together with `.json` files with the frame data. The annotator and custom writer data is printed to the terminal.
[image: ../_images/isim_4.5_replicator_tut_external_getting_started_02.jpg]

### Custom Randomizations: Replicator Graph and USD API
This example demonstrates creating a custom randomization using Replicator’s graph-based randomizers triggered by custom events and a custom USD API-based randomization. A dome light’s color is randomized through custom events, while a cube’s location is randomized through USD API. Data is captured using the `BasicWriter` with semantic segmentation. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_03.py
```
The output directory will contain the RGB and semantic segmentation images with the captured data. The cube is randomized each capture, while the dome light color is randomized every second capture.
[image: ../_images/isim_4.5_replicator_tut_external_getting_started_03.jpg]

### Event-Triggered Data Capture: Timeline and Simulation
This example shows how to capture simulation data when specific conditions are met. A cube and sphere are dropped in a physics simulation, and data is captured at specific intervals based on the cube’s height. The timeline is paused during capture to ensure data consistency. The standalone example can also be run directly (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/api/isaacsim.replicator.examples/sdg_getting_started_04.py
```
The output directory will contain the RGB and semantic segmentation images with the captured data at specific simulation times (cube drop height intervals) and the cube hidden during capture. During every second capture with the cube hidden, the timeline will not advance (`delta_time=0.0`) ensuring the same simulation state can be captured multiple times.
[image: ../_images/isim_4.5_replicator_tut_external_getting_started_04.jpg]

## Troubleshooting
For troubleshooting information related to the Getting Started Scripts, refer to the Getting Started Scripts Issues section in the Replicator Troubleshooting page.

## Next Steps
After completing these examples, consider exploring:

- Advanced randomizations using the Randomizer Details

- Custom annotators for specialized data capture

- Distributed data generation using multiple GPUs

- Integration with machine learning pipelines

- Advanced physics-based simulations

For more information, refer to: - Replicator Documentation - Isaac Sim Randomizers Guide - I/O Optimization Guide
