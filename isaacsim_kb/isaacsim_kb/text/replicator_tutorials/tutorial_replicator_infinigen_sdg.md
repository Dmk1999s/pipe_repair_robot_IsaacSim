<!-- source: replicator_tutorials/tutorial_replicator_infinigen_sdg.html | title: Environment Based Synthetic Dataset Generation with Infinigen — Isaac Sim Documentation -->

# Environment Based Synthetic Dataset Generation with Infinigen
This tutorial explains how to set up a synthetic data generation (SDG) pipeline in Isaac Sim using the omni.replicator extension and procedurally generated environments from Infinigen . The example uses the standalone workflow.
Example of Infinigen generated rooms.
Example data collected from the synthetic dataset generation pipeline.

## Learning Objectives
In this tutorial, you will learn how to:

- Load procedurally generated environments from Infinigen as background scenes.

- Prepare the environments for SDG and physics simulations.

- Load physics-enabled target assets (labeled) for data collection and distractor assets (unlabeled) for scene diversity.

- Use built-in Replicator randomizer graphs manually triggered at custom intervals, detached from the writing process.

- Use custom USD / Isaac Sim API functions for custom randomizers.

- Use multiple Replicator Writers and cameras (render products) to save different types of data from different viewpoints.

- Use config files to easily customize the simulation and data collection process.

- Understand and customize configuration parameters for flexibility.

## Prerequisites
Before starting this tutorial, you should be familiar with:

- USD / Isaac Sim APIs for creating and manipulating USD stages.

- Rigid-body dynamics and physics simulation in Isaac Sim.

- Replicator randomizers and OmniGraph for a better understanding of the Replicator randomization graphs pipeline.

- Running simulations as Standalone Applications .

- Procedurally generating environments using Infinigen .

## Generating Infinigen Environments

- Install Infinigen: Follow the installation instructions on the Infinigen GitHub Repository .

- Generate Environments: Use the Hello Room instructions to generate indoor scenes using various settings and parameters.

- Example Script: Use the following example script (Linux) to generate multiple dining room environments with different seeds:

```
for i in {1..10}
do
python -m infinigen_examples.generate_indoors --seed $i --task coarse --output_folder outputs/indoors/dining_room_$i -g fast_solve.gin singleroom.gin -p compose_indoors.terrain_enabled=False restrict_solving.restrict_parent_rooms=\[\"DiningRoom\"\] &&
python -m infinigen.tools.export --input_folder outputs/indoors/dining_room_$i --output_folder outputs/omniverse/dining_room_$i -f usdc -r 1024 --omniverse
done
```

- This script generates 10 unique dining room environments by varying the seed value.

- The generated environments are stored in outputs/indoors/dining_room_$i.

- The export command converts these environments into USD format, saving them to outputs/omniverse/dining_room_$i.

- The -f usdc flag specifies the USD format for the exported files.

- The –omniverse flag ensures compatibility with Omniverse applications.

## Scenario Overview
In this tutorial, we will use procedurally generated environments as backdrops for synthetic data generation. These environments are then configured with colliders and physics properties, enabling physics-based simulations. Within each indoor environment, we define a “working area”—in this case, the dining table—where we will place both labeled target assets and unlabeled distractor assets.
The assets are divided into two categories:

- Falling assets: Physics-enabled objects that interact with the environment and settle onto surfaces, such as the ground or table.

- Floating assets: Objects equipped only with colliders that remain floating in the air.

For each background environment, we will capture frames in two scenarios:

- Assets floating around the working area.

- Physics-enabled assets that have settled on surfaces like the ground or table.

To capture these frames, we use multiple cameras (render products) configured with one or multiple writers. The cameras will be randomized for each frame, changing their positions around the working area and orienting toward randomly selected target assets.
Once the captures for one environment are complete, a new environment will be loaded, configured with colliders and physics properties, and the process will repeat until the desired number of captures is achieved.
During the capture process, we will apply randomizers at various frames to introduce variability into the scene. These randomizations include:

- Object poses.

- Lighting configurations, including dome light settings.

- Colors of shape distractors.

By incorporating these randomizations, we increase the diversity of the dataset, making it more robust for training machine learning models.

## Getting Started
The main script for this tutorial is located at:
`<install_path>/standalone_examples/replicator/infinigen/infinigen_sdg.py`
This script is designed to run as a Standalone Application. The default configurations are stored within the script itself in the form of a Python dictionary. You can override these defaults by providing custom configuration files in JSON or YAML format.
Helper functions are located in the `infinigen_sdg_utils.py` file. These functions help with loading environments, spawning assets, randomizing object poses, and running physics simulations.
To generate a synthetic dataset using the default configuration, run the following command (on Windows use `python.bat` instead of `python.sh`):

```
./python.sh standalone_examples/replicator/infinigen/infinigen_sdg.py
```
To use a custom configuration file that supports multiple writers and other custom settings, use the –config argument:

```
./python.sh standalone_examples/replicator/infinigen/infinigen_sdg.py \
--config standalone_examples/replicator/infinigen/config/infinigen_multi_writers_pt.yaml
```

## Implementation
The following sections provide an overview of the key steps involved in setting up and running the synthetic data generation pipeline.

### Configuration Files
Example configuration files are provided in the `infinigen/config` directory. These files allow you to customize various aspects of the simulation, such as the number of captures, assets to include, randomization parameters, and writers to use.
Here’s an example of a custom YAML configuration file that demonstrates the use of multiple writers:
Custom YAML Configuration File
```
environments:
folders:
- /Isaac/Samples/Replicator/Infinigen/dining_rooms/
files: []

capture:
total_captures: 12
num_floating_captures_per_env: 2
num_dropped_captures_per_env: 3
num_cameras: 2
resolution: [640, 480]
disable_render_products: true
rt_subframes: 8
path_tracing: true
camera_look_at_target_offset: 0.1
camera_distance_to_target_range: [1.05, 1.25]
num_scene_lights: 4

writers:
- type: BasicWriter
kwargs:
output_dir: "_out_infinigen_basicwriter_pt"
rgb: true
semantic_segmentation: true
colorize_semantic_segmentation: true
use_common_output_dir: false
- type: DataVisualizationWriter
kwargs:
output_dir: "_out_infinigen_dataviswriter_pt"
bounding_box_2d_tight: true
bounding_box_2d_tight_params:
background: rgb
bounding_box_3d: true
bounding_box_3d_params:
background: normals

labeled_assets:
auto_label:
num: 5
gravity_disabled_chance: 0.25
folders:
- /Isaac/Props/YCB/Axis_Aligned/
files:
- /Isaac/Props/YCB/Axis_Aligned/036_wood_block.usd
regex_replace_pattern: "^\\d+_"
regex_replace_repl: ""

manual_label:
- url: /Isaac/Props/YCB/Axis_Aligned/008_pudding_box.usd
label: pudding_box
num: 2
gravity_disabled_chance: 0.25
- url: /Isaac/Props/YCB/Axis_Aligned_Physics/006_mustard_bottle.usd
label: mustard_bottle
num: 2
gravity_disabled_chance: 0.25

distractors:
shape_distractors:
num: 30
gravity_disabled_chance: 0.25
types: ["capsule", "cone", "cylinder", "sphere", "cube"]

mesh_distractors:
num: 10
gravity_disabled_chance: 0.25
folders:
- /NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Floor_Signs/
- /NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Safety/Cones/
files:
- /Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxD_04_1847.usd
- /Isaac/Environments/Simple_Warehouse/Props/SM_CardBoxA_01_414.usd
- /Isaac/Environments/Simple_Warehouse/Props/S_TrafficCone.usd
- /Isaac/Environments/Simple_Warehouse/Props/S_WetFloorSign.usd
- /Isaac/Environments/Office/Props/SM_Book_03.usd
- /Isaac/Environments/Office/Props/SM_Book_34.usd
- /Isaac/Environments/Office/Props/SM_BookOpen_01.usd
- /Isaac/Environments/Office/Props/SM_Briefcase.usd
- /Isaac/Environments/Office/Props/SM_Extinguisher.usd
- /Isaac/Environments/Hospital/Props/SM_MedicalBag_01a.usd
- /Isaac/Environments/Hospital/Props/SM_MedicalBox_01g.usd

debug_mode: true
```

### Configuration Parameters
Here is an explanation of the configuration parameters:

- environments:

- folders: List of directories containing the Infinigen environments to be used.

- files: Specific USD files of environments to be loaded.

- capture:

- total_captures: Total number of captures to generate.

- num_floating_captures_per_env: Number of captures to take before running the physics simulation (assets are floating).

- num_dropped_captures_per_env: Number of captures to take after the physics simulation (assets have settled).

- num_cameras: Number of cameras to use for capturing images.

- resolution: Resolution of the rendered images (width, height).

- disable_render_products: If true, render products are disabled between captures to improve performance.

- rt_subframes: Number of subframes to render for each capture.

- path_tracing: If true, uses path tracing for rendering (higher quality, slower).

- camera_look_at_target_offset: Random offset applied when cameras look at target assets.

- camera_distance_to_target_range: Range of distances for cameras from the target assets.

- num_scene_lights: Number of additional lights to add to the scene.

- writers: List of writers to use for data output.

- type: Type of writer (e.g., BasicWriter, DataVisualizationWriter).

- kwargs: Arguments specific to each writer type.

- labeled_assets:

- auto_label: Configuration for automatically labeled assets.

- num: Number of assets to spawn.

- gravity_disabled_chance: Probability that an asset will have gravity disabled (will float).

- folders and files: Sources for the asset USD files.

- regex_replace_pattern and regex_replace_repl: Used to generate labels from file names.

- manual_label: List of assets with manually specified labels.

- url: USD file path of the asset.

- label: Semantic label to assign.

- num: Number of instances to spawn.

- gravity_disabled_chance: Probability of gravity being disabled.

- distractors:

- shape_distractors: Configuration for primitive shape distractors.

- num: Number of distractors to spawn.

- gravity_disabled_chance: Probability of gravity being disabled.

- types: List of primitive shapes to use.

- mesh_distractors: Configuration for mesh distractors.

- num: Number of distractors to spawn.

- gravity_disabled_chance: Probability of gravity being disabled.

- folders and files: Sources for the distractor USD files.

- debug_mode: When set to true, certain elements like ceilings are hidden to provide a better view of the scene during development and debugging.

### Loading Infinigen Environments
We will load environments generated by Infinigen into the Isaac Sim stage. The environments are specified in the configuration file, either through folders or individual files.
Loading Infinigen Environments
```
# Load the environment URLs from the configuration
env_config = config.get("environments", {})
env_urls = infinigen_sdg_utils.get_usd_paths(
files=env_config.get("files", []),
folders=env_config.get("folders", [])
)

# Cycle through the environments
env_cycle = cycle(env_urls)

# Load the next environment in the cycle
env_url = next(env_cycle)
print(f"Loading environment: {env_url}")
infinigen_sdg_utils.load_env(env_url, prim_path="/Environment")
```
In the above code, we use the get_usd_paths utility function to collect all USD files from the specified folders and files in the configuration. We then cycle through these environments to load them one by one.

### Setting Up the Scene
After loading the environment, we set up the scene by:

- Hiding unnecessary elements (e.g., ceiling) for better visibility if the debugging mode is selected.

- Adding colliders to the environment for physics simulation.

- Spawning labeled assets and distractors at random positions within the working area.

- Adding physics properties to the assets.

Setting Up the Scene
```
# Setup the environment
infinigen_sdg_utils.setup_env(root_path="/Environment", hide_top_walls=config.get("debug_mode", False))

# Get the location of the working area (e.g., dining table)
working_area_loc = infinigen_sdg_utils.get_matching_prim_location("TableDining", root_path="/Environment")

# Spawn labeled assets
target_assets = infinigen_sdg_utils.spawn_labeled_assets(
config=config.get("labeled_assets", {}),
working_area_loc=working_area_loc
)

# Spawn shape distractors
shape_distractors = infinigen_sdg_utils.spawn_shape_distractors(
config=config.get("distractors", {}).get("shape_distractors", {}),
working_area_loc=working_area_loc
)

# Spawn mesh distractors
mesh_distractors = infinigen_sdg_utils.spawn_mesh_distractors(
config=config.get("distractors", {}).get("mesh_distractors", {}),
working_area_loc=working_area_loc
)

# Randomize asset poses
assets_to_randomize = target_assets + mesh_distractors + shape_distractors
infinigen_sdg_utils.randomize_poses(
assets=assets_to_randomize,
working_area_loc=working_area_loc
)
```
Explanation:

- Environment Setup: The setup_env utility function adds colliders to the environment and hides top walls if debug_mode is true. Hiding the top walls provides a clear view of the scene during debugging.

- Working Area Location: We use get_matching_prim_location to find the location of the dining table, which serves as our working area.

- Spawning Assets: We spawn labeled assets (target objects) and distractors (both shape and mesh types) using utility functions. These functions handle loading the assets, adding physics properties, and setting semantic labels.

- Randomizing Poses: The randomize_poses function randomizes the positions, rotations, and scales of the assets within the working area.

### Creating Cameras and Render Products
We create multiple cameras to capture images from different viewpoints. Each camera is assigned a render product, which is used by Replicator writers to save data.
Creating Cameras and Render Products
```
# Create cameras
cameras = []
num_cameras = config.get("capture", {}).get("num_cameras", 2)
for i in range(num_cameras):
cam_prim = stage.DefinePrim(f"/Cameras/cam_{i}", "Camera")
cam_prim.GetAttribute("clippingRange").Set((0.25, 1000))
cameras.append(cam_prim)

# Create render products for the cameras
render_products = []
resolution = config.get("capture", {}).get("resolution", (1280, 720))
for cam in cameras:
rp = rep.create.render_product(cam.GetPath(), resolution, name=f"rp_{cam.GetName()}")
render_products.append(rp)

# Optionally disable render products between captures to improve performance
disable_render_products = config.get("capture", {}).get("disable_render_products", False)
if disable_render_products:
for rp in render_products:
rp.hydra_texture.set_updates_enabled(False)
```
Explanation:

- We use the USD API to define camera prims.

- Render products are created using Replicator’s create.render_product function.

- If disable_render_products is set to true in the configuration, we disable the render products between captures to save computational resources.

### Setting Up Replicator Writers
We use multiple Replicator writers to collect and store different types of data generated during the simulation. Writers are specified in the configuration file and can include various types such as BasicWriter, DataVisualizationWriter, and custom writers.
Setting Up Replicator Writers
```
# Setup writers
writers = []
writers_config = config.get("writers", [])
for writer_config in writers_config:
writer = infinigen_sdg_utils.setup_writer(writer_config)
if writer:
writer.attach(render_products)
writers.append(writer)
print(f"Initialized writer: {writer_config['type']}")
```
Explanation:

- The setup_writer utility function initializes writers based on the configuration.

- Writers are attached to the render products (cameras) to capture data from the specified viewpoints.

- Multiple writers can be used simultaneously to generate different datasets types.

### Domain Randomization
To enhance the diversity of the dataset, we apply domain randomization to various elements in the scene:

- Randomizing Object Poses: Positions, orientations, and scales of assets are randomized within specified ranges.

- Randomizing Lights: Scene lights are randomized in terms of position, intensity, and color.

- Randomizing Dome Light: The environment dome light is randomized to simulate different lighting conditions.

- Randomizing Shape Distractor Colors: Colors of shape distractors are randomized to increase visual diversity.

Domain Randomization
```
# Randomize positions and properties of assets
infinigen_sdg_utils.randomize_poses(
assets=assets_to_randomize,
working_area_loc=working_area_loc
)

# Create and randomize scene lights
num_scene_lights = config.get("capture", {}).get("num_scene_lights", 3)
scene_lights = infinigen_sdg_utils.create_scene_lights(
num_lights=num_scene_lights,
working_area_loc=working_area_loc
)
infinigen_sdg_utils.randomize_lights(scene_lights, working_area_loc)

# Register replicator randomizers
infinigen_sdg_utils.register_dome_light_randomizer()
infinigen_sdg_utils.register_shape_distractors_color_randomizer(shape_distractors)

# Trigger randomizations
rep.orchestrator.register_trigger(rep.trigger.OnFrameEvent(1), infinigen_sdg_utils.randomize_dome_lights)
rep.orchestrator.register_trigger(rep.trigger.OnFrameEvent(1), infinigen_sdg_utils.randomize_shape_distractor_colors)
```
Explanation:

- Asset Randomization: We randomize the poses of assets using the randomize_poses utility function.

- Scene Lights: Additional lights are created and their properties are randomized.

- Randomizers Registration: We register custom randomizers for dome lights and shape distractor colors.

- Randomizations Triggering: The randomizations are manually triggered at specific intervals using Replicator triggers.

### Running Physics Simulation
We run physics simulations to allow objects to interact naturally within the environment. This involves:

- Running a short simulation to resolve any initial overlaps.

- Capturing images before objects have settled (floating captures).

- Running a longer simulation to let objects fall and settle.

- Capturing images after objects have settled (dropped captures).

Running Physics Simulation
```
# Run a short simulation to resolve initial overlaps
infinigen_sdg_utils.run_simulation(num_frames=4, render=True)

# Capture frames with floating objects
for i in range(num_floating_captures_per_env):
# Randomize camera poses
infinigen_sdg_utils.randomize_camera_poses(
cameras,
targets=target_assets,
distance_range=camera_distance_to_target_range,
polar_angle_range=(0, 75)
)
print(f"Capturing floating assets {i+1}/{num_floating_captures_per_env}")
rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)

# Run physics simulation to let objects fall
print("Running physics simulation for dropped captures")
infinigen_sdg_utils.run_simulation(num_frames=200, render=False)

# Capture frames with dropped objects
for i in range(num_dropped_captures_per_env):
# Randomize camera poses
infinigen_sdg_utils.randomize_camera_poses(
cameras,
targets=target_assets,
distance_range=camera_distance_to_target_range,
polar_angle_range=(0, 45)
)
print(f"Capturing dropped assets {i+1}/{num_dropped_captures_per_env}")
rep.orchestrator.step(rt_subframes=rt_subframes, delta_time=0.0)
```
Explanation:

- Initial Simulation: A short simulation resolves any initial overlaps among assets.

- Floating Captures: We capture images while assets are still floating (before physics simulation).

- Physics Simulation: A longer simulation allows assets to fall and settle according to physics.

- Dropped Captures: We capture images after the assets have settled.

### Capturing Data
We capture data at specified intervals, ensuring that we have a diverse set of images covering various object states and viewpoints.

- Randomizing Camera Poses: Cameras are positioned randomly around target assets to capture images from different angles.

- Triggering Randomizations: Randomizations are applied at each step to ensure diversity.

Capturing Data Loop
```
# Start the SDG loop
capture_counter = 0
total_captures = config.get("capture", {}).get("total_captures", 15)
num_floating_captures_per_env = config.get("capture", {}).get("num_floating_captures_per_env", 3)
num_dropped_captures_per_env = config.get("capture", {}).get("num_dropped_captures_per_env", 4)

while capture_counter < total_captures:
# Load and setup the environment
env_url = next(env_cycle)
print(f"Loading environment: {env_url}")
infinigen_sdg_utils.load_env(env_url, prim_path="/Environment")
infinigen_sdg_utils.setup_env(root_path="/Environment", hide_top_walls=debug_mode)

# Spawn and randomize assets
# (As shown in previous sections)

# Capture data with floating assets
# (As shown in previous sections)

# Capture data with dropped assets
# (As shown in previous sections)

capture_counter += num_floating_captures_per_env + num_dropped_captures_per_env

# Wait until the data is written to disk
rep.orchestrator.wait_until_complete()
```
Explanation:

- We loop through the environments, capturing the specified number of images per environment.

- The capture_counter keeps track of the total number of captures made.

- After capturing data for one environment, we load the next one and repeat the process.

## Summary
In this tutorial, you learned how to generate synthetic datasets using Infinigen environments in NVIDIA Omniverse Isaac Sim. The key steps included:

- Generating Infinigen Environments: Using Infinigen to create photorealistic indoor environments.

- Understanding Configuration Parameters: Customizing the simulation and data generation process through configuration files.

- Setting Up the Simulation: Running Isaac Sim as a standalone application and loading Infinigen environments.

- Spawning Assets: Using the Isaac Sim API to place labeled assets and distractors in the environment.

- Configuring the SDG Pipeline: Creating cameras, render products, and using multiple Replicator writers to generate different datasets.

- Applying Domain Randomization: Enhancing dataset diversity through randomizations.

- Running Physics Simulations: Simulating object interactions for realistic scenes.

- Capturing and Saving Data: Collecting images and annotations using multiple Replicator writers.

By following this tutorial, you now have the foundation to create rich, diverse synthetic datasets using procedurally generated environments and advanced randomization techniques.

## Next Steps
With the generated datasets, you can proceed to train machine learning models for tasks like object detection, segmentation, and pose estimation. Consider exploring the TAO Toolkit for training workflows and pre-trained models.
