<!-- source: reference_material/benchmarks.html | title: Isaac Sim Benchmarks — Isaac Sim Documentation -->

# Isaac Sim Benchmarks
This page contains key performance indicators (KPIs) for Isaac Sim, captured across different reference hardware and measured using the `isaacsim.benchmark.services` extension. It also contains a guide on how to collect the same KPIs on your hardware, to compare to our published performance specs.

## GPU-Independent KPIs
These KPIs measure Isaac Sim performance independent of the GPU on which Isaac Sim is running.
Note
These KPIs were measured on a standardized reference machine using an Intel i9-14900k CPU and 32GB of DDR5 RAM.

[TABLE]
Name | Definition | Units | Value
Binary package size (Windows) | Size of Windows binary package | GB | 7.37
Binary package size (Ubuntu) | Size of Ubuntu binary package | GB | 8.17
Docker container size | Size of Docker container before extraction on NGC | GB |
pip package size | Size of pip package as downloaded | GB |
Startup time (async) | Time from launching Isaac Sim executable to app ready appearing in logs | seconds | 31.472 [ 1 ] 6.31 [ 2 ]
Startup time (non-async) | Time from initializing SimulationApp in standalone Python to app ready appearing in logs | seconds | 263 [ 3 ] 4.43 [ 4 ]
[/TABLE]
[1 ]Includes shader installation, which is typically one-time when shaders are cached.
[2 ]Startup time (async) using cached shaders.
[3 ]Includes shader installation, which is typically one-time when shaders are cached.
[4 ]Startup time (non-async) using cached shaders.

## GPU-Dependent KPIs
These KPIs measure Isaac Sim performance on reference hardware, including frame rate for benchmark scenes and render rate for specific sensor combinations. KPIs are reported as the average KPI value across 600 frames.
Note
SDG KPIs are measured using two (2) 720p cameras in a blank scene with 500 objects generated each frame.
Note
ROS2 Render & Publishing Speed is measured using the reference Nova Carter asset, rendering all 4 stereo cameras, 1 3D lidar and 2 2D lidars, and publishing all possible messages.
Note
The following KPIs were measured with Motion BVH enabled. This is a rendering setting that allows for higher accuracy when modeling motion-related sensor effects. It is disabled by default in Isaac Sim 5.1 onwards, and can be enabled by following the instructions in How to Enable Motion BVH .

## Measuring KPIs on Local Hardware
Isaac Sim KPIs can be measured using the Python scripts provided in `standalone_examples/benchmarks`. The KPIs provided above are computed using the scripts as follows. Commands are providing in `bash` syntax (for Ubuntu); for Windows, replace `.sh` with `.bat` and `\` for multiline commands to ```.

- Startup time (async): Measured as `Runtime` for `phase: startup` from the logs after running

```
./isaac-sim.sh --no-window --/app/quitAfter=200 --/app/file/ignoreUnsavedOnExit=1 \
--enable isaacsim.benchmark.services
```

- Startup time (non-async): Measured as `Runtime` for `phase: startup` from the logs after running

```
./python.sh standalone_examples/api/isaacsim.simulation_app/hello_world.py \
--enable isaacsim.benchmark.services
```

- Full Warehouse Sample Scene load time & FPS: Load time is measured as `Runtime` for `phase: loading` and FPS is measured as `Mean FPS` for `phase: benchmark`.

```
./python.sh standalone_examples/benchmarks/benchmark_scene_loading.py \
--env-url /Isaac/Environments/Simple_Warehouse/full_warehouse.usd
```

- Physics Steps per second: Physics steps per second is measured as `1000.0/Mean Physics Frametime` for `phase: benchmark`. An additional physics argument is available to switch between CPU and GPU (default) physics

```
./python.sh standalone_examples/benchmarks/benchmark_robots_o3dyn.py \
--num-robots 10 --num-gpus 1
```

- Isaac ROS Sample Scene FPS: FPS is measured as `Mean FPS` for `phase: benchmark`.

```
./python.sh standalone_examples/benchmarks/benchmark_scene_loading.py \
--env-url /Isaac/Samples/ROS2/Scenario/carter_warehouse_apriltags_worker.usd
```

- ROS2 Render & Publishing Speed: FPS is measured as `Mean FPS` for `phase: benchmark`.

```
./python.sh standalone_examples/benchmarks/benchmark_robots_nova_carter_ros2.py \
--num-robots 1 --enable-3d-lidar 1 --enable-2d-lidar 2 --enable-hawks 4
```

- SDG images per second (simple): FPS is measured as `Mean FPS` for `phase: benchmark`.

```
./python.sh standalone_examples/benchmarks/benchmark_sdg.py \
--num-cameras 2 --resolution 1280 720 --asset-count 100
--annotators rgb distance_to_image_plane --skip-write
```

- SDG images per second (complex): FPS is measured as `Mean FPS` for `phase: benchmark`.

```
./python.sh standalone_examples/benchmarks/benchmark_sdg.py \
--num-cameras 2 --resolution 1280 720 --asset-count 100
--annotators all --skip-write
```
