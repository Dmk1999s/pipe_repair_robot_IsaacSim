<!-- source: reference_material/sim_performance_optimization_handbook.html | title: Isaac Sim Performance Optimization Handbook — Isaac Sim Documentation -->

# Isaac Sim Performance Optimization Handbook
The speed of the simulation is primarily determined by the physics step size and the minimum simulation frame rate. However, these settings can be influenced by other factors such as the complexity of the scene, the number of physics objects, number of cameras and sensors, and the computational resources available.

## Physics Simulation Optimizations

- Physics Step Size: The physics step size determines the time interval for each physics simulation step.

- A smaller step size will result in a more accurate simulation but will also require more computational resources and thus slow down the simulation.

- A larger step size will speed up the simulation but may result in less accurate physics.

Note
Adjust the physics step size in your script using the `world.set_physics_step_size(step_size)` function, where step_size is the desired step size in seconds.

- Minimum Simulation Frame Rate: The minimum simulation frame rate determines the minimum number of physics simulation steps per second. If the actual frame rate drops below this value, the simulation will slow down to maintain the accuracy of the physics.

Note
Adjust the minimum simulation frame rate in your script using the `world.set_min_simulation_frame_rate(frame_rate)` function, where frame_rate is the desired frame rate in frames per second.

- GPU Dynamics: Enabling GPU dynamics can potentially speed up the simulation by offloading the physics calculations to the GPU.

Note
This will only be beneficial if your GPU is powerful enough and not already fully utilized by other tasks. Enable or disable GPU dynamics in your script using the `world.set_gpu_dynamics_enabled(enabled)` function, where enabled is a boolean value indicating whether GPU dynamics should be enabled.
Checkout the Physics Simulation Performance guide for more optimization tricks!

## Robot Asset Optimizations
A step-by-step tutorial to optimize a sample asset is provided in Tutorial 12: Asset Optimization .

- Merge Mesh Tool: Using the Merge Mesh tool at Tools > Robotics > Asset Editors > Mesh Merge Tool can allow for a more streamlined asset structure and reduction in total mesh count.

- Scenegraph Instancing: Instancing enables shareable, referenceable prim subgraphs. Using pointers to shared reference assets can reduce total memory usage for assets with repeated, identical meshes (e.g. wheels).

- An example of instancing is described in Tutorial 12: Asset Optimization . A general guide to instanceable assets can be found at Instanceable Assets .

Note
Instancing inherently carries some limitations related to attributes as children cannot have modified attributes from the parent reference object.

- Simplify Colliders: Colliders have high computational costs. The simpler, the collision shape, the more performant the simulation behaves.

- A reduction in contact points brings substantial performance improvements. For wheel colliders, it’s recommended to use a simple cylinder or sphere collider instead of a mesh collider. This greatly simplifies contact with the ground plane, increasing performance and allows the robot to drive smoothly over terrain.

- For a robot, use the simplest approximations possible that provide the needed level of precision. For example, for a mobile robot, a cube approximation is often sufficient for the body.

- Reducing the total number of colliders is also beneficial. Consider whether every collider added to the asset needs to be enabled. Selectively disabling/enabling colliders can greatly reduce computational cost.

Note
Higher precision applications require using mesh colliders rather than simplified shapes. There are different approximations available and the choice of each one is a tradeoff between performance and precision.

- Disable Self Collisions: Disabling self collisions from an Articulation Root could reduce computational load and create substantial speedups at runtime if not needed.

Note
This is highly usecase-dependent. With a complex articulated hand, self collisions are necessary to avoid interpenetrations and provide realistic collisions. For a wheeled mobile robot with some internal geometries, it is likely an unnecessary load to compute any collisions other than those with the external environment.

## Scene and Rendering Optimizations

- Simplify the Scene: Reducing the complexity of the scene, implementing level of detail (LOD), culling invisible objects, and optimizing the physics settings.

Note
Isaac Sim provides several tools for simplifying your scene

- Scene Optimizer : kit extension that performs scene optimization on the USD level

- Mesh Merge Tool : Isaac Sim utility to merge multiple meshes to a single mesh

Note
During realtime simulation, the gizmos (including floor grids) automatically disappear to optimize performance. They reappear when the simulation is paused or stopped.

- Using RTX – Realtime Mode: (see here )

Note
This affects opacity, and user may need to set partial opacity checkbox
[image: The Fractional Cutout Opacity checkbox]

- Disable Materials and Lights:

- Disabling all materials, set it to -1 to go back to regular.

```
1import carb
2carb.settings.get_settings().set_int("/rtx/debugMaterialType", 0)
```

- Hide lights

- Turn off rendering features in the render settings panel (these will also have equivalent carb settings that can be set in python). There is no non-rtx rendering mode in the Isaac Sim GUI application, but you can disable almost everything (reflections, transparency, etc) to increase execution speed. To disable rendering completely unless explicitly needed by a sensor, you can use the headless application workflow.

- Adjust DLSS Performance Mode: DLSS performance mode is toggled by the `--/rtx/post/dlss/execMode=<value>` setting. Values are as follows:

- Performance (`0`) - the most performant setting, reducing VRAM consumption and rendering time but decreasing render quality. This is the default value in Isaac Sim.

- Balanced (`1`) - offers both optimized performance and image quality.

- Quality (`2`) - offers higher image quality than balanced mode, at the cost of increased render time and VRAM consumption.

- Auto (`3`) - Selects the best DLSS Mode for the current output resolution. When rendering 720p cameras, Auto mode tends to select Quality, so you may see performance impacts by running in Auto mode while rendering cameras at lower resolution.

Note
The DLSS mode is currently set to `Auto` by default. `Performance` mode will yield the best performance, but may result in artifacts such as smearing when rendering cameras at lower resolution (720p).

- Disabling viewport updates in headless mode: Running in headless mode with `./python.sh` still renders viewports by default.

- To improve performance, viewport updates can be disabled by setting the `SimulationApp` configuration parameter `disable_viewport_updates=True`.

```
simulation_app = SimulationApp({"headless": True,
"disable_viewport_updates": True})
```

- When not using SimulationApp, users can also disable viewport updates with the following code snippet:

```
from omni.kit.viewport.utility import get_active_viewport
viewport = get_active_viewport()
viewport.updates_enabled = False
```

Note
Setting `disable_viewport_updates` in SimulationApp is only supported if running in headless mode. For streaming usecases, this option should not be used.

- Disabling texture streaming: Texture streaming is a feature that helps minimize GPU memory consumption, particularly in large scenes.

- Disabling texture streaming can have positive performance benefits but will result in increased GPU memory consumption. There’s also possible negative UX impacts if memory is running low - leading to crashes or missing some textures.

- To disable texture streaming, modify the value of the `/rtx-transient/resourcemanager/texturestreaming/enabled` setting.

```
"--/rtx-transient/resourcemanager/texturestreaming/enabled=false"
```

Note
This is not recommended for the majority of use cases. It should be used on a case-by-case basis and evaluated for each workflow to determine its suitability. This may lead to unintended rendering behavior.

## CPU Thread Count Optimizations
Three settings control the number of CPU threads used by Isaac Sim. When left unset (the default behavior), Isaac Sim will use all available threads on the system. Standalone Python workflows are limited to 32 threads by default and can be modified by changing the `limit_cpu_threads` argument in the `SimulationApp` constructor.

- `--/plugins/carb.tasking.plugin/threadCount`: Sets Carbonite’s maximum worker thread count.

- `--/persistent/physics/numThreads`: Sets how many Carbonite worker threads to use for physics simulation.

- `--/plugins/omni.tbb.globalcontrol/maxThreadCount`: Sets Omniverse TBB scheduler’s maximmum worker thread count.

Spawning too many worker threads may lead to CPU bottlenecking. Consider limiting the number of CPU threads used by Isaac Sim to fewer than the number of virtual cores on the system. Current testing indicates that 32 threads is optimal for most use cases.
For example, on Ubuntu:

```
./isaac-sim.sh --/plugins/carb.tasking.plugin/threadCount=16 --/plugins/omni.tbb.globalcontrol/maxThreadCount=16
```
Standalone Python:

```
simulation_app = SimulationApp({"headless": False, "limit_cpu_threads": 16})
```

## CPU Governor Settings on Linux
CPU governors dictate the operating clock frequency range and scaling of the CPU. This can be a limiting factor for Isaac Sim performance. For maximum performance, the CPU governor should be set to `performance`. To modify the CPU governor, run the following commands:

```
sudo apt-get install linux-tools-common
cpupower frequency-info # Check available governors
sudo cpupower frequency-set -g performance # Set governor with root permissions
```
Note
Not all governors are available on all systems. Governors enabling higher clock speed are typically more performance-centric and will yield better performance for Isaac Sim.

## Asynchronous Rendering
Asynchronous rendering is a feature that allows the rendering to run in a separate thread from the simulation thread. Starting in Isaac Sim 5.1.0, asynchronous rendering is enabled by default whenever Isaac Sim is in a stoppped or paused state. This greatly improves UI responsiveness and viewport FPS, particularly for complex scenes.
This is set in the isaacsim.core.throttling extension. To disable this feature in the event of unexpected behavior, set the `exts."isaacsim.core.throttling".enable_async` setting to `false` when starting the application.

```
./isaac-sim.sh --exts."isaacsim.core.throttling".enable_async=false
```
Note
This setting is only set true when running with `isaacsim.exp.full.kit`, not when running via a Python-based workflow. It could be enabled manually using the above setting for other workflows if desired. In certain use cases, particularly with Replicator-based SDG workflows, it may be necessary to disable asynchronous rendering to ensure proper behavior.

## Multi-GPU Support
The following rules of thumb may help improve multi-GPU performance, based on our multi-GPU benchmarks.
Note
Exact Isaac Sim performance when using multiple data-center-grade GPUs can be found here .

- Add as many GPUs as cameras being rendered - but no more. When rendering 2 720p cameras with 2 GPUs, we saw a speed up of 72% to 89% compared to single GPU performance, but using 4 GPUs yielded only 61 - 81% improvement.

- Performance scales better the more cameras you’re rendering. Our 4 camera with 4x GPUs test scaled well with an overall speed up of about 213% - 233%, but our 8 camera with 4 GPUs test scaled even better with an overall speedup of 271% - 281%.

- Synthetic Data Generation performs best with 2 GPUs. When collecting only RGB and depth data we saw an improvement of 78% - 90% compared to single GPU performance, with more improvement when scenes are more complex. However, when collecting data from all the annotators, performance improved 199% to 646%, with more complex scenes improving more. Refer to our benchmarks for more details.

- Single high-resolution cameras render faster on multiple GPUs. An exception to our earlier rules - if you are rendering a single high-resolution (4K or higher) camera, multiple GPUs can help accelerate rendering.

- Increasing GPU count does not improve scene load time. GPU count does not influence the amount of time it takes to load a USD, or the maximum USD scene size that can be loaded.

- GPU Physics simulation only utilizes 1 GPU. Increasing GPU count will not improve GPU physics simulation performance.

### Disabling IOMMU On Linux
Per the CUDA C++ Programming Guide , users on bare-metal Linux should disable the IOMMU to improve multi-GPU performance.
IOMMU may be disabled from system BIOS (exact instructions vary based on motherboard specification), or from the command line via:

```
sudo bash -c 'echo GRUB_CMDLINE_LINUX="amd_iommu=off" >> /etc/default/grub'
sudo update-grub
sudo reboot
```
After rebooting, the IOMMU should be disabled.
Note
If IOMMU is enabled, you will receive a warning like `IOMMU is enabled.` below the `nvidia-smi` output in the logs when running Isaac Sim.

## Reducing GPU Memory Utilization
These are suggestions to help reduce Isaac Sim GPU memory utilization:

- Reduce the Texture Streaming Budget. Select the `Render Settings` tab, then select the `Common` settings. Under `Debug` > `Streaming Settings`, reduce `"Texture Streaming Budget (% of GPU memory)"`. By default this value is set to 0.6, 60% of GPU memory capacity. To reduce GPU memory consumption, the number can be reduced further. For standalone Python workflows, you can modify the value of the `/rtx-transient/resourcemanager/texturestreaming/memoryBudget` setting.

- Reduce total rendered pixel count by turning off unnecessary viewports or reducing rendered camera resolution, if possible.

## Experimental: Reducing Potential Memory Leaks
Experimental suggestion to help reduce Isaac Sim RAM consumption in the event of memory leaks in long-running workflows:

- Adjusting the memory allocator to reduce memory leaks in long running workflows, particularly where stages are loaded and unloaded repeatedly.

- To change the allocator configuration, set the following environment variable:

```
export GLIBC_TUNABLES=glibc.malloc.arena_max=1:glibc.malloc.mmap_max=0:glibc.malloc.mmap_threshold=2147483647
```

## Useful Tools

### Windows
Task Manager is a great resource for giving nice clean graphs and can show peak usage on a variety of system information regarding performance.
[image: Task Manager]

- Click on the Start icon

- Type “Task Manager”

- In Task Manager, Select the “Performance” Tab

On the left side of this pane you will see various graphs like CPU, Memory and GPU. Select any of these to get a more detailed view of the data. Generally speaking if any of these are spiking and peaking out, you should look into its cause and begin to troubleshoot.

### Linux
`nvidia-smi` is a great resource for giving useful data on Linux.
See these documents for further information:

- NVIDIA-SMI

- NVIDIA-SMI Documentation (PDF)
